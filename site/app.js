/* Paper Atlas: renders data.json built by scripts/build_viz_data.py */
(() => {
  "use strict";

  if (typeof d3 === "undefined") {
    document.getElementById("lede").textContent =
      "The chart library did not load, so the charts cannot be drawn. Please reload the page.";
    return;
  }

  const PAGE_SIZE = 50;
  const AUTHOR_NODES = 80;
  const RANK_PAGE = 20;
  const state = { period: "all", topic: -1, search: "", shown: PAGE_SIZE, authorSort: "total", authorsShown: RANK_PAGE };
  let DATA, papers, topicLayout;

  const $ = (id) => document.getElementById(id);
  const css = (name) => getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  const fmt = d3.format(",");
  const monthKey = (date) => date.slice(0, 7);
  const monthLabel = (key, long = true) =>
    d3.utcFormat(long ? "%b %Y" : "%b")(new Date(`${key}-01T00:00:00Z`));
  const arxivUrl = (id) => `https://arxiv.org/abs/${id}`;

  function monthsBetween(first, last) {
    const out = [];
    let [y, m] = first.split("-").map(Number);
    const [ly, lm] = last.split("-").map(Number);
    while (y < ly || (y === ly && m <= lm)) {
      out.push(`${y}-${String(m).padStart(2, "0")}`);
      if (++m > 12) { m = 1; y += 1; }
    }
    return out;
  }

  /* ---------- tooltip (DOM built with textContent: titles are untrusted data) ---------- */
  const tip = $("tooltip");
  function showTip(event, lines) {
    tip.replaceChildren();
    lines.forEach(([cls, text]) => {
      const el = document.createElement(cls === "strong" ? "strong" : "div");
      if (cls === "key") {
        const key = document.createElement("span");
        key.className = "key";
        el.append(key);
      } else if (cls !== "strong") {
        el.className = cls;
      }
      el.append(document.createTextNode(text));
      tip.append(el);
    });
    tip.hidden = false;
    const box = tip.getBoundingClientRect();
    let x, y;
    if (event.clientX !== undefined && event.type.startsWith("pointer")) {
      x = event.clientX + 14;
      y = event.clientY + 14;
    } else {
      const r = event.target.getBoundingClientRect();
      x = r.right + 8;
      y = r.top;
    }
    if (x + box.width > innerWidth - 8) x = Math.max(8, x - box.width - 28);
    if (y + box.height > innerHeight - 8) y = Math.max(8, y - box.height - 28);
    tip.style.left = `${x}px`;
    tip.style.top = `${y}px`;
  }
  const hideTip = () => { tip.hidden = true; };

  /* ---------- filtering ---------- */
  function periodRange(period) {
    const last = DATA.last_update;
    if (period === "all") return [null, null];
    if (period === "12m") {
      const d = new Date(`${last}T00:00:00Z`);
      d.setUTCFullYear(d.getUTCFullYear() - 1);
      return [d.toISOString().slice(0, 10), last];
    }
    return [`${period}-01-01`, `${period}-12-31`];
  }

  function filtered() {
    const [from, to] = periodRange(state.period);
    const q = state.search.trim().toLowerCase();
    return papers.filter((p) =>
      (!from || (p.d >= from && p.d <= to)) &&
      (state.topic < 0 || p.k.includes(state.topic)) &&
      (!q || p.search.includes(q)));
  }
  const isFiltered = () => state.period !== "all" || state.topic >= 0 || state.search.trim() !== "";

  function syncUrl() {
    const params = new URLSearchParams();
    if (state.period !== "all") params.set("period", state.period);
    if (state.topic >= 0) params.set("topic", DATA.topics[state.topic].name);
    if (state.search.trim()) params.set("q", state.search.trim());
    const qs = params.toString();
    history.replaceState(null, "", qs ? `?${qs}${location.hash}` : location.pathname + location.hash);
  }

  /* ---------- summary ---------- */
  function renderTiles(rows) {
    const cutoff = new Date(`${DATA.last_update}T00:00:00Z`);
    cutoff.setUTCDate(cutoff.getUTCDate() - 30);
    const recent = cutoff.toISOString().slice(0, 10);
    $("s-papers").textContent = fmt(rows.length);
    $("s-recent").textContent = fmt(rows.filter((p) => p.d > recent).length);
    $("s-code").textContent = fmt(rows.filter((p) => p.g).length);
    $("s-authors").textContent = fmt(new Set(rows.flatMap((p) => p.a)).size);
  }

  /* ---------- papers per month ---------- */
  function roundedTop(x, y, w, h, r) {
    r = Math.min(r, w / 2, h);
    return `M${x},${y + h}V${y + r}Q${x},${y} ${x + r},${y}H${x + w - r}Q${x + w},${y} ${x + w},${y + r}V${y + h}Z`;
  }

  function renderTrend(rows) {
    const el = $("trend-chart");
    el.replaceChildren();
    const trackingMonth = monthKey(DATA.tracking_start);
    const lastMonth = monthKey(DATA.last_update);
    const [from, to] = periodRange(state.period);
    const allMonths = papers.map((p) => monthKey(p.d));
    const first = from ? monthKey(from) : d3.min(allMonths);
    const last = to && monthKey(to) < lastMonth ? monthKey(to) : lastMonth;
    const months = monthsBetween(first, last);
    const counts = d3.rollup(rows, (v) => v.length, (p) => monthKey(p.d));
    // The latest month is still being collected unless the data runs to its last day.
    const lastDay = new Date(`${DATA.last_update}T00:00:00Z`);
    lastDay.setUTCDate(lastDay.getUTCDate() + 1);
    const lastMonthDone = lastDay.getUTCDate() === 1;
    const series = months.map((m) => ({
      m, n: counts.get(m) || 0, partial: m < trackingMonth, inProgress: m === lastMonth && !lastMonthDone,
    }));

    const width = el.clientWidth;
    const height = 240;
    const margin = { top: 22, right: 4, bottom: 28, left: 40 };
    const svg = d3.select(el).append("svg").attr("width", width).attr("height", height)
      .attr("role", "img").attr("aria-label", "Papers per month bar chart");
    const x = d3.scaleBand().domain(months).range([margin.left, width - margin.right]);
    x.paddingInner(Math.min(0.5, 2 / Math.max(x.step(), 1)));
    const y = d3.scaleLinear().domain([0, d3.max(series, (d) => d.n) || 1]).nice()
      .range([height - margin.bottom, margin.top]);

    svg.append("g").attr("class", "axis").attr("transform", `translate(${margin.left},0)`)
      .call(d3.axisLeft(y).ticks(4).tickSize(-(width - margin.left - margin.right)).tickFormat(d3.format("~s")))
      .call((g) => g.select(".domain").remove());

    const everyN = Math.ceil(64 / x.step());
    const quarterly = months.filter((m) => ["01", "04", "07", "10"].includes(m.slice(5)));
    const ticks = everyN <= 3 ? quarterly : months.filter((m) => m.endsWith("-01"));
    svg.append("g").attr("class", "axis").attr("transform", `translate(0,${height - margin.bottom})`)
      .call(d3.axisBottom(x).tickValues(ticks.length ? ticks : [months[0]]).tickSize(0).tickPadding(8)
        .tickFormat((m) => (m.endsWith("-01") || ticks.length < 3 ? monthLabel(m) : monthLabel(m, false))))
      .call((g) => g.select(".domain").attr("stroke", css("--axis")));

    const bars = svg.append("g");
    bars.selectAll("path").data(series).join("path")
      .attr("d", (d) => roundedTop(x(d.m), y(d.n), x.bandwidth(), y(0) - y(d.n), d.n ? 4 : 0))
      .attr("fill", (d) => (d.partial ? css("--context") : css("--accent")))
      .attr("fill-opacity", (d) => (d.inProgress ? 0.4 : 1));

    const lastBar = series[series.length - 1];
    if (lastBar && lastBar.n) {
      svg.append("text").attr("x", x(lastBar.m) + x.bandwidth() / 2).attr("y", y(lastBar.n) - 6)
        .attr("text-anchor", "end").attr("font-size", 12).attr("font-weight", 600)
        .attr("fill", css("--ink")).text(fmt(lastBar.n));
    }
    const notes = [];
    if (series.some((d) => d.partial)) notes.push(`Gray: before tracking began (${monthLabel(trackingMonth)}), incomplete`);
    if (lastBar && lastBar.inProgress) notes.push(`Faded: ${monthLabel(lastBar.m)} so far`);
    if (notes.length) {
      svg.append("text").attr("x", margin.left + 4).attr("y", margin.top - 8)
        .attr("font-size", 11).attr("fill", css("--muted")).text(notes.join(" · "));
    }

    svg.append("g").selectAll("rect").data(series).join("rect")
      .attr("x", (d) => x(d.m) - (x.step() - x.bandwidth()) / 2).attr("width", x.step())
      .attr("y", margin.top).attr("height", height - margin.top - margin.bottom)
      .attr("fill", "transparent").attr("tabindex", 0).attr("aria-label", (d) => `${monthLabel(d.m)}: ${d.n} papers`)
      .on("pointermove focus", function (event, d) {
        bars.selectAll("path").attr("opacity", (b) => (b === d ? 1 : 0.55));
        const lines = [["strong", `${fmt(d.n)} papers`], ["sub", monthLabel(d.m)]];
        if (d.partial) lines.push(["sub", "Before tracking began, so incomplete"]);
        if (d.inProgress) lines.push(["sub", `Month in progress, through ${DATA.last_update}`]);
        showTip(event, lines);
      })
      .on("pointerleave blur", () => { bars.selectAll("path").attr("opacity", 1); hideTip(); });

    $("trend-note").textContent = `Tracking began on ${DATA.tracking_start}; earlier months only include papers that were still in the first snapshot.`;
    const table = document.createElement("table");
    table.innerHTML = "<thead><tr><th>Month</th><th class='num'>Papers</th></tr></thead>";
    const body = table.createTBody();
    series.slice().reverse().forEach((d) => {
      const tr = body.insertRow();
      tr.insertCell().textContent = monthLabel(d.m) + (d.partial ? " (incomplete)" : "");
      const td = tr.insertCell(); td.className = "num"; td.textContent = fmt(d.n);
    });
    $("trend-table").replaceChildren(table);
  }

  /* ---------- paper map ---------- */
  function renderMap(rows) {
    const frame = $("map-chart");
    frame.replaceChildren();
    const width = frame.clientWidth;
    const height = frame.clientHeight;
    const dpr = window.devicePixelRatio || 1;
    const pad = 14;
    const canvas = document.createElement("canvas");
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    canvas.setAttribute("aria-label", "Scatter map of papers by similarity; use the paper table below for the same data");
    frame.append(canvas);
    const ctx = canvas.getContext("2d");
    ctx.scale(dpr, dpr);

    const px = (p) => pad + p.x * (width - pad * 2);
    const py = (p) => pad + (1 - p.y) * (height - pad * 2);
    const selected = new Set(rows);
    const filteredView = isFiltered();
    const accent = css("--accent");
    const context = css("--context");
    const surface = css("--surface");
    const small = width < 560;

    function draw(hovered) {
      ctx.clearRect(0, 0, width, height);
      ctx.globalAlpha = 0.55;
      ctx.fillStyle = context;
      if (filteredView) {
        papers.forEach((p) => {
          if (selected.has(p)) return;
          ctx.beginPath(); ctx.arc(px(p), py(p), small ? 1.4 : 1.8, 0, Math.PI * 2); ctx.fill();
        });
      }
      ctx.globalAlpha = filteredView ? 0.85 : 0.6;
      ctx.fillStyle = accent;
      rows.forEach((p) => {
        ctx.beginPath(); ctx.arc(px(p), py(p), small ? 1.8 : 2.4, 0, Math.PI * 2); ctx.fill();
      });
      ctx.globalAlpha = 1;
      if (hovered) {
        ctx.beginPath(); ctx.arc(px(hovered), py(hovered), 6, 0, Math.PI * 2);
        ctx.fillStyle = selected.has(hovered) ? accent : context; ctx.fill();
        ctx.lineWidth = 2; ctx.strokeStyle = surface; ctx.stroke();
      }
    }
    draw(null);

    // Cluster labels, largest first, skipping any that would collide with one already placed.
    const svg = d3.select(frame).append("svg").attr("width", width).attr("height", height);
    const placed = [];
    DATA.clusters.slice().sort((a, b) => b.n - a.n).forEach((c) => {
      const w = c.label.length * 6.6;
      const box = { x0: px(c) - w / 2, x1: px(c) + w / 2, y0: py(c) - 10, y1: py(c) + 6 };
      if (box.x0 < 2 || box.x1 > width - 2) {
        const shift = box.x0 < 2 ? 2 - box.x0 : width - 2 - box.x1;
        box.x0 += shift; box.x1 += shift;
      }
      if (placed.some((b) => b.x0 < box.x1 && box.x0 < b.x1 && b.y0 < box.y1 && box.y0 < b.y1)) return;
      placed.push(box);
      svg.append("text").attr("class", "cluster-label").attr("x", (box.x0 + box.x1) / 2).attr("y", py(c))
        .attr("text-anchor", "middle").text(c.label);
    });

    const delaunay = d3.Delaunay.from(papers, px, py);
    let current = null;
    const pick = (event) => {
      const r = canvas.getBoundingClientRect();
      const mx = event.clientX - r.left;
      const my = event.clientY - r.top;
      const p = papers[delaunay.find(mx, my)];
      return p && Math.hypot(px(p) - mx, py(p) - my) < 24 ? p : null;
    };
    canvas.addEventListener("pointermove", (event) => {
      const p = pick(event);
      if (p !== current) { current = p; draw(p); }
      canvas.style.cursor = p ? "pointer" : "crosshair";
      if (!p) return hideTip();
      const names = p.a.slice(0, 3).map((i) => DATA.authors[i]).join(", ") + (p.a.length > 3 ? " et al." : "");
      const lines = [["strong", p.t], ["sub", `${p.d} · ${names}`]];
      if (p.k.length) lines.push(["sub", p.k.map((k) => DATA.topics[k].name).join(", ")]);
      if (filteredView && !selected.has(p)) lines.push(["sub", "Outside your current filters"]);
      showTip(event, lines);
    });
    canvas.addEventListener("pointerleave", () => { current = null; draw(null); hideTip(); });
    canvas.addEventListener("click", (event) => {
      const p = pick(event);
      if (p) window.open(arxivUrl(p.id), "_blank", "noopener");
    });
  }

  /* ---------- topics ---------- */
  function sparkline(values, width, height) {
    const svg = d3.create("svg").attr("class", "spark").attr("width", width).attr("height", height)
      .attr("aria-hidden", "true");
    const x = d3.scaleLinear().domain([0, Math.max(values.length - 1, 1)]).range([1, width - 3]);
    const y = d3.scaleLinear().domain([0, d3.max(values) || 1]).range([height - 2, 2]);
    svg.append("path").attr("fill", "none").attr("stroke", css("--accent")).attr("stroke-width", 2)
      .attr("stroke-linejoin", "round").attr("stroke-linecap", "round")
      .attr("d", d3.line((v, i) => x(i), y)(values));
    return svg.node();
  }

  function renderTopicBars(rows) {
    const el = $("topic-bars");
    el.replaceChildren();
    const counts = DATA.topics.map((_, i) => rows.filter((p) => p.k.includes(i)).length);
    const max = d3.max(counts) || 1;
    const sparkMonths = monthsBetween(monthKey(DATA.tracking_start), monthKey(DATA.last_update));
    const sparkWidth = el.clientWidth > 720 ? 180 : 84;
    el.style.setProperty("--spark-w", `${sparkWidth}px`);
    const head = document.createElement("div");
    head.className = "topic-head";
    ["Topic", "", "Papers", "Since tracking"].forEach((t) => {
      const s = document.createElement("span"); s.textContent = t; head.append(s);
    });
    el.append(head);

    topicLayout.order.forEach((i) => {
      const topic = DATA.topics[i];
      const row = document.createElement("button");
      row.type = "button";
      row.className = `topic-row${state.topic === i ? " active" : ""}`;
      row.setAttribute("aria-pressed", state.topic === i);
      row.title = topic.description;
      const name = document.createElement("span"); name.textContent = topic.name;
      const track = document.createElement("span"); track.className = "bar-track";
      const bar = document.createElement("span"); bar.className = "bar";
      bar.style.display = "block";
      bar.style.width = `${(counts[i] / max) * 100}%`;
      if (!counts[i]) bar.style.opacity = 0;
      track.append(bar);
      const count = document.createElement("span"); count.className = "count"; count.textContent = fmt(counts[i]);
      const byMonth = d3.rollup(rows.filter((p) => p.k.includes(i)), (v) => v.length, (p) => monthKey(p.d));
      row.append(name, track, count, sparkline(sparkMonths.map((m) => byMonth.get(m) || 0), sparkWidth, 22));
      row.addEventListener("click", () => setState({ topic: state.topic === i ? -1 : i }));
      el.append(row);
    });
  }

  function buildTopicLayout() {
    const n = DATA.topics.length;
    const counts = DATA.topics.map((_, i) => papers.filter((p) => p.k.includes(i)).length);
    const pairs = [];
    for (let a = 0; a < n; a++) {
      for (let b = a + 1; b < n; b++) {
        const both = papers.filter((p) => p.k.includes(a) && p.k.includes(b)).length;
        const jaccard = both / (counts[a] + counts[b] - both || 1);
        pairs.push({ source: a, target: b, jaccard });
      }
    }
    // Keep each topic's three strongest links.
    const keep = new Set();
    for (let i = 0; i < n; i++) {
      pairs.filter((l) => l.source === i || l.target === i).sort((a, b) => b.jaccard - a.jaccard)
        .slice(0, 3).forEach((l) => keep.add(l));
    }
    const links = [...keep];

    // Place topics on a circle, ordered by a force layout so related topics sit side by side.
    const nodes = DATA.topics.map((t, i) => ({ i }));
    const sim = d3.forceSimulation(nodes)
      .force("link", d3.forceLink(links.map((l) => ({ ...l }))).strength((l) => 0.1 + l.jaccard * 2))
      .force("charge", d3.forceManyBody().strength(-200))
      .force("center", d3.forceCenter())
      .stop();
    for (let t = 0; t < 400; t++) sim.tick();
    nodes.slice().sort((a, b) => Math.atan2(a.y, a.x) - Math.atan2(b.y, b.x))
      .forEach((d, slot) => { d.angle = ((slot + 0.5) / n) * Math.PI * 2 - Math.PI / 2; });
    const order = d3.range(n).sort((a, b) => counts[b] - counts[a]);
    return { nodes, links, order };
  }

  // Word-wrap a topic name to lines of at most maxChars (a single long word keeps its own line).
  function wrapLabel(name, maxChars) {
    const lines = [];
    let current = "";
    name.split(" ").forEach((word) => {
      if (current && `${current} ${word}`.length > maxChars) {
        lines.push(current);
        current = word;
      } else {
        current = current ? `${current} ${word}` : word;
      }
    });
    lines.push(current);
    return lines;
  }

  function renderTopicPairs(el, both) {
    const pairs = [];
    DATA.topics.forEach((_, a) => DATA.topics.forEach((__, b) => {
      if (a < b) pairs.push({ a, b, n: both(a, b) });
    }));
    const top = pairs.filter((p) => p.n).sort((x, y) => y.n - x.n).slice(0, 10);
    if (!top.length) {
      const empty = document.createElement("p");
      empty.className = "empty";
      empty.textContent = "No papers in this selection mention two topics.";
      return el.append(empty);
    }
    const max = top[0].n;
    top.forEach((p) => {
      const row = document.createElement("div");
      row.className = "pair-row";
      const name = document.createElement("span");
      name.textContent = `${DATA.topics[p.a].name} + ${DATA.topics[p.b].name}`;
      const track = document.createElement("span");
      const bar = document.createElement("span");
      bar.className = "bar";
      bar.style.width = `${(p.n / max) * 100}%`;
      track.append(bar);
      const count = document.createElement("span");
      count.className = "count";
      count.textContent = fmt(p.n);
      row.append(name, track, count);
      el.append(row);
    });
  }

  function renderTopicNet(rows) {
    const el = $("topic-net");
    el.replaceChildren();
    const width = el.clientWidth;
    const counts = DATA.topics.map((_, i) => rows.filter((p) => p.k.includes(i)).length);
    const both = (a, b) => rows.filter((p) => p.k.includes(a) && p.k.includes(b)).length;
    const links = topicLayout.links.map((l) => ({ ...l, n: both(l.source, l.target) }));
    const maxCount = d3.max(counts) || 1;
    const narrow = width < 520;
    $("topic-net-note").textContent = narrow
      ? "The topic pairs that appear together in the most papers."
      : "Lines join topics that appear in the same papers; thicker means more overlap. Circle size is the paper count. Hover a topic to isolate its links.";
    // A circle of long topic names cannot fit on a phone, so list the strongest pairs instead.
    if (narrow) return renderTopicPairs(el, both);
    const labels = DATA.topics.map((t) => wrapLabel(t.name, narrow ? 10 : 18));
    const longestLine = d3.max(labels.flat(), (line) => line.length);
    const labelRoom = Math.min(width * 0.32, 16 + longestLine * 6.4);
    const maxLines = d3.max(labels, (lines) => lines.length);
    const radius = Math.max(60, Math.min(width / 2 - labelRoom, 150 + DATA.topics.length * 4));
    const height = radius * 2 + 50 + maxLines * 26;
    const cx = width / 2;
    const cy = height / 2;
    const r = d3.scaleSqrt().domain([0, maxCount]).range([3, Math.min(22, radius / 6)]);
    const w = d3.scaleLinear().domain([0, d3.max(links, (l) => l.n) || 1]).range([0.5, 8]);
    const pos = topicLayout.nodes.map((d) => ({
      x: cx + Math.cos(d.angle) * radius, y: cy + Math.sin(d.angle) * radius, cos: Math.cos(d.angle), sin: Math.sin(d.angle),
    }));

    const svg = d3.select(el).append("svg").attr("width", width).attr("height", height)
      .attr("role", "img").attr("aria-label", "Network of topics that appear in the same papers");
    // Chords bow toward the centre so links between neighbours stay readable.
    const chord = (l) => {
      const a = pos[l.source];
      const b = pos[l.target];
      const qx = cx + ((a.x + b.x) / 2 - cx) * 0.35;
      const qy = cy + ((a.y + b.y) / 2 - cy) * 0.35;
      return `M${a.x},${a.y}Q${qx},${qy} ${b.x},${b.y}`;
    };
    const linkSel = svg.append("g").selectAll("path").data(links.filter((l) => l.n > 0)).join("path")
      .attr("class", "net-link").attr("fill", "none").attr("d", chord)
      .attr("stroke-width", (l) => w(l.n));
    const nodeSel = svg.append("g").selectAll("circle").data(DATA.topics).join("circle")
      .attr("class", "net-node").attr("cx", (_, i) => pos[i].x).attr("cy", (_, i) => pos[i].y)
      .attr("r", (_, i) => r(counts[i])).attr("tabindex", 0)
      .attr("aria-label", (t, i) => `${t.name}: ${counts[i]} papers`)
      .attr("stroke-width", (_, i) => (state.topic === i ? 3 : 2))
      .attr("stroke", (_, i) => (state.topic === i ? css("--ink") : css("--surface")));
    const labelSel = svg.append("g").selectAll("text").data(DATA.topics).join("text")
      .attr("class", "node-label")
      .attr("text-anchor", (_, i) => (pos[i].cos > 0.05 ? "start" : pos[i].cos < -0.05 ? "end" : "middle"))
      .attr("x", (_, i) => pos[i].x + pos[i].cos * (r(counts[i]) + 6))
      .each(function (t, i) {
        // Long names wrap onto two lines so they fit beside the circle.
        const lines = labels[i];
        const base = pos[i].y + pos[i].sin * (r(counts[i]) + 6);
        const shift = pos[i].sin > 0.5 ? 10 : pos[i].sin < -0.5 ? -2 - (lines.length - 1) * 13 : 4 - (lines.length - 1) * 6.5;
        d3.select(this).attr("y", base + shift).selectAll("tspan").data(lines).join("tspan")
          .attr("x", d3.select(this).attr("x")).attr("dy", (_, j) => (j ? 13 : 0)).text((line) => line);
      });

    nodeSel
      .on("pointermove focus", (event, t) => {
        const i = DATA.topics.indexOf(t);
        const mine = links.filter((l) => l.source === i || l.target === i);
        const near = new Set([i, ...mine.flatMap((l) => [l.source, l.target])]);
        nodeSel.classed("dim", (_, j) => !near.has(j));
        labelSel.classed("dim", (_, j) => !near.has(j));
        linkSel.classed("dim", (l) => l.source !== i && l.target !== i);
        const partners = DATA.topics.map((_, j) => ({ j, n: j === i ? 0 : both(i, j) }))
          .sort((a, b) => b.n - a.n).slice(0, 3).filter((d) => d.n);
        showTip(event, [
          ["strong", `${fmt(counts[i])} papers`], ["sub", t.name],
          ...partners.map((d) => ["key", `${fmt(d.n)} also mention ${DATA.topics[d.j].name}`]),
        ]);
      })
      .on("pointerleave blur", () => {
        nodeSel.classed("dim", false); labelSel.classed("dim", false); linkSel.classed("dim", false); hideTip();
      })
      .on("click", (_, t) => {
        const i = DATA.topics.indexOf(t);
        setState({ topic: state.topic === i ? -1 : i });
      });
  }

  /* ---------- co-author network ---------- */
  function renderAuthors(rows) {
    const el = $("author-net");
    el.replaceChildren();
    const width = el.clientWidth;
    const height = width < 560 ? 440 : 540;
    const counts = new Map();
    rows.forEach((p) => p.a.forEach((a) => counts.set(a, (counts.get(a) || 0) + 1)));
    const top = [...counts].filter(([, n]) => n >= 2).sort((a, b) => b[1] - a[1]).slice(0, AUTHOR_NODES);
    const noteText = top.length
      ? `The ${top.length} most prolific authors in your selection (2+ papers each). Lines join people who wrote a paper together; thicker means more joint papers. Different people who share a name are merged. Click a person to search their papers.`
      : "";
    $("people-note").textContent = noteText;
    if (!top.length) {
      const empty = document.createElement("p");
      empty.className = "empty";
      empty.textContent = "No author has two or more papers in this selection.";
      el.append(empty);
      return;
    }

    const ids = new Set(top.map(([a]) => a));
    const edgeMap = new Map();
    rows.forEach((p) => {
      const members = p.a.filter((a) => ids.has(a));
      for (let i = 0; i < members.length; i++) {
        for (let j = i + 1; j < members.length; j++) {
          const key = members[i] < members[j] ? `${members[i]}|${members[j]}` : `${members[j]}|${members[i]}`;
          edgeMap.set(key, (edgeMap.get(key) || 0) + 1);
        }
      }
    });
    const nodes = top.map(([a, n]) => ({ id: a, n, degree: 0 }));
    const byId = new Map(nodes.map((d) => [d.id, d]));
    const links = [...edgeMap].map(([key, n]) => {
      const [s, t] = key.split("|").map(Number);
      byId.get(s).degree += 1;
      byId.get(t).degree += 1;
      return { source: s, target: t, n };
    });
    const r = d3.scaleSqrt().domain([2, d3.max(nodes, (d) => d.n)]).range([4, width < 560 ? 11 : 16]);
    const sim = d3.forceSimulation(nodes)
      .force("link", d3.forceLink(links).id((d) => d.id).distance(34).strength((l) => Math.min(1, 0.15 + l.n * 0.1)))
      .force("charge", d3.forceManyBody().strength(-70))
      .force("collide", d3.forceCollide((d) => r(d.n) + 3))
      .force("x", d3.forceX(0).strength((d) => (d.degree ? 0.07 : 0.3) * (height / width)))
      .force("y", d3.forceY(0).strength((d) => (d.degree ? 0.07 : 0.3)))
      .stop();
    for (let t = 0; t < 320; t++) sim.tick();

    const pad = 24;
    const xs = d3.extent(nodes, (d) => d.x);
    const ys = d3.extent(nodes, (d) => d.y);
    const scale = Math.min((width - pad * 2) / (xs[1] - xs[0] || 1), (height - pad * 2) / (ys[1] - ys[0] || 1), 1.6);
    const ox = (width - (xs[1] - xs[0]) * scale) / 2;
    const oy = (height - (ys[1] - ys[0]) * scale) / 2;
    nodes.forEach((d) => { d.px = ox + (d.x - xs[0]) * scale; d.py = oy + (d.y - ys[0]) * scale; });

    const neighbors = new Map(nodes.map((d) => [d.id, new Map()]));
    links.forEach((l) => {
      neighbors.get(l.source.id).set(l.target.id, l.n);
      neighbors.get(l.target.id).set(l.source.id, l.n);
    });
    const labelled = new Set(nodes.slice(0, width < 560 ? 8 : 16).map((d) => d.id));
    const wScale = d3.scaleLinear().domain([1, d3.max(links, (l) => l.n) || 1]).range([1, 5]);

    const svg = d3.select(el).append("svg").attr("width", width).attr("height", height)
      .attr("role", "img").attr("aria-label", "Co-author network of the most prolific authors");
    const linkSel = svg.append("g").selectAll("line").data(links).join("line").attr("class", "net-link")
      .attr("x1", (l) => l.source.px).attr("y1", (l) => l.source.py)
      .attr("x2", (l) => l.target.px).attr("y2", (l) => l.target.py)
      .attr("stroke-width", (l) => wScale(l.n));
    const nodeSel = svg.append("g").selectAll("circle").data(nodes).join("circle").attr("class", "net-node")
      .attr("cx", (d) => d.px).attr("cy", (d) => d.py).attr("r", (d) => r(d.n)).attr("tabindex", 0)
      .attr("aria-label", (d) => `${DATA.authors[d.id]}: ${d.n} papers`);
    const labelSel = svg.append("g").selectAll("text").data(nodes).join("text").attr("class", "node-label")
      .attr("x", (d) => d.px + r(d.n) + 4).attr("y", (d) => d.py + 4)
      .attr("text-anchor", (d) => (d.px > width - 120 ? "end" : "start"))
      .attr("dx", (d) => (d.px > width - 120 ? -(r(d.n) * 2 + 8) : 0))
      .attr("display", (d) => (labelled.has(d.id) ? null : "none"))
      .text((d) => DATA.authors[d.id]);

    nodeSel
      .on("pointermove focus", (event, d) => {
        const near = neighbors.get(d.id);
        nodeSel.classed("dim", (o) => o.id !== d.id && !near.has(o.id));
        linkSel.classed("dim", (l) => l.source.id !== d.id && l.target.id !== d.id);
        labelSel.attr("display", (o) => (o.id === d.id || near.has(o.id) ? null : "none"));
        const partners = [...near].sort((a, b) => b[1] - a[1]).slice(0, 3);
        showTip(event, [
          ["strong", `${fmt(d.n)} papers`], ["sub", DATA.authors[d.id]],
          ...partners.map(([id, n]) => ["key", `${n} with ${DATA.authors[id]}`]),
        ]);
      })
      .on("pointerleave blur", () => {
        nodeSel.classed("dim", false); linkSel.classed("dim", false);
        labelSel.attr("display", (o) => (labelled.has(o.id) ? null : "none"));
        hideTip();
      })
      .on("click", (_, d) => {
        searchAuthor(DATA.authors[d.id]);
      });
  }

  /* ---------- author rankings ---------- */
  function searchAuthor(name) {
    $("f-search").value = name;
    setState({ search: name });
    document.getElementById("papers").scrollIntoView();
  }

  function renderAuthorRank(rows) {
    const body = $("rank-rows");
    body.replaceChildren();
    document.querySelectorAll("#authors .seg button").forEach((b) =>
      b.setAttribute("aria-pressed", b.dataset.sort === state.authorSort));

    const [recentFrom] = periodRange("12m");
    const stats = new Map();
    rows.forEach((p) => p.a.forEach((a) => {
      let s = stats.get(a);
      if (!s) stats.set(a, (s = { id: a, total: 0, recent: 0, latest: "" }));
      s.total += 1;
      if (p.d >= recentFrom) s.recent += 1;
      if (p.d > s.latest) s.latest = p.d;
    }));
    const key = state.authorSort;
    const other = key === "total" ? "recent" : "total";
    const ranked = [...stats.values()].filter((s) => s[key] > 0)
      .sort((a, b) => b[key] - a[key] || b[other] - a[other] || DATA.authors[a.id].localeCompare(DATA.authors[b.id]));
    const shown = ranked.slice(0, state.authorsShown);

    // Co-authors and topics only for the rows on screen.
    const detail = new Map(shown.map((s) => [s.id, { co: new Map(), topics: new Map() }]));
    rows.forEach((p) => p.a.forEach((a) => {
      const d = detail.get(a);
      if (!d) return;
      p.a.forEach((b) => { if (b !== a) d.co.set(b, (d.co.get(b) || 0) + 1); });
      p.k.forEach((k) => d.topics.set(k, (d.topics.get(k) || 0) + 1));
    }));

    const max = ranked.length ? ranked[0].total : 1;
    const top = (map, n) => [...map].sort((a, b) => b[1] - a[1]).slice(0, n);
    shown.forEach((s) => {
      // Tied authors share a rank.
      const rank = 1 + ranked.findIndex((o) => o[key] === s[key]);
      const tr = body.insertRow();
      const rankCell = tr.insertCell(); rankCell.className = "num c-rank"; rankCell.textContent = rank;
      const nameCell = tr.insertCell();
      const name = document.createElement("button");
      name.type = "button"; name.className = "link"; name.textContent = DATA.authors[s.id];
      name.title = "Show this author's papers";
      name.addEventListener("click", () => searchAuthor(DATA.authors[s.id]));
      nameCell.append(name);

      const barCell = tr.insertCell(); barCell.className = "c-bar";
      const bar = document.createElement("span"); bar.className = "rank-bar";
      bar.style.width = `${(s.total / max) * 100}%`;
      const count = document.createElement("span"); count.className = "rank-count"; count.textContent = fmt(s.total);
      barCell.append(bar, count);

      const recent = tr.insertCell(); recent.className = "num c-recent"; recent.textContent = fmt(s.recent);
      const latest = tr.insertCell(); latest.className = "c-latest"; latest.textContent = s.latest;
      const d = detail.get(s.id);
      const topics = tr.insertCell(); topics.className = "c-topics";
      topics.textContent = top(d.topics, 2).map(([k]) => DATA.topics[k].name).join(", ") || "–";
      const co = tr.insertCell(); co.className = "c-co";
      co.textContent = top(d.co, 2).map(([id, n]) => `${DATA.authors[id]} (${n})`).join(", ") || "–";
    });

    if (!ranked.length) {
      const td = body.insertRow().insertCell();
      td.colSpan = 7; td.className = "empty";
      td.textContent = state.authorSort === "recent" && rows.length
        ? "No papers from the last 12 months in this selection."
        : "No authors in this selection.";
    }
    $("rank-note").textContent = ranked.length
      ? `${fmt(ranked.length)} authors in your selection, ranked by ${key === "total" ? "paper count" : "papers in the last 12 months"}. ` +
        "Topics and co-authors are counted within your selection; numbers in brackets are joint papers. Click a name to see their papers."
      : "";
    $("rank-more").hidden = ranked.length <= state.authorsShown;
  }

  /* ---------- paper table ---------- */
  function renderTable(rows) {
    const body = $("paper-rows");
    body.replaceChildren();
    rows.slice(0, state.shown).forEach((p) => {
      const tr = body.insertRow();
      tr.insertCell().textContent = p.d;
      const cell = tr.insertCell();
      const link = document.createElement("a");
      link.className = "title"; link.href = arxivUrl(p.id); link.target = "_blank"; link.rel = "noopener";
      link.textContent = p.t;
      cell.append(link);
      if (p.k.length) {
        const topics = document.createElement("span");
        topics.className = "topics";
        topics.textContent = p.k.map((k) => DATA.topics[k].name).join(" · ");
        cell.append(topics);
      }
      const authors = tr.insertCell();
      authors.className = "authors";
      authors.textContent = p.a.slice(0, 4).map((i) => DATA.authors[i]).join(", ") + (p.a.length > 4 ? " et al." : "");
      const code = tr.insertCell();
      if (p.g) {
        const a = document.createElement("a");
        a.href = p.g; a.target = "_blank"; a.rel = "noopener"; a.textContent = "Code";
        code.append(a);
      }
    });
    if (!rows.length) {
      const td = body.insertRow().insertCell();
      td.colSpan = 4; td.className = "empty"; td.textContent = "No papers match these filters.";
    }
    $("table-note").textContent = rows.length
      ? `Newest first. Showing ${fmt(Math.min(state.shown, rows.length))} of ${fmt(rows.length)}.`
      : "";
    $("more").hidden = rows.length <= state.shown;
  }

  /* ---------- wiring ---------- */
  function renderAll() {
    const rows = filtered();
    renderTiles(rows);
    renderTrend(rows);
    renderMap(rows);
    renderTopicBars(rows);
    renderTopicNet(rows);
    renderAuthors(rows);
    renderAuthorRank(rows);
    renderTable(rows);
  }

  function setState(patch) {
    Object.assign(state, { shown: PAGE_SIZE, authorsShown: RANK_PAGE }, patch);
    $("f-period").value = state.period;
    $("f-topic").value = String(state.topic);
    syncUrl();
    hideTip();
    renderAll();
  }

  function initControls() {
    const years = [...new Set(papers.map((p) => p.d.slice(0, 4)))].sort().reverse();
    const periods = [["all", "All time"], ["12m", "Last 12 months"], ...years.map((y) => [y, y])];
    $("f-period").replaceChildren(...periods.map(([v, t]) => new Option(t, v)));
    const topicOptions = [[-1, "All topics"], ...topicLayout.order.map((i) => [i, DATA.topics[i].name])];
    $("f-topic").replaceChildren(...topicOptions.map(([v, t]) => new Option(t, String(v))));

    const params = new URLSearchParams(location.search);
    if (periods.some(([v]) => v === params.get("period"))) state.period = params.get("period");
    const topic = DATA.topics.findIndex((t) => t.name === params.get("topic"));
    if (topic >= 0) state.topic = topic;
    if (params.get("q")) state.search = params.get("q");
    $("f-search").value = state.search;
    $("f-period").value = state.period;
    $("f-topic").value = String(state.topic);

    $("f-period").addEventListener("change", (e) => setState({ period: e.target.value }));
    $("f-topic").addEventListener("change", (e) => setState({ topic: Number(e.target.value) }));
    let timer;
    $("f-search").addEventListener("input", (e) => {
      clearTimeout(timer);
      timer = setTimeout(() => setState({ search: e.target.value }), 200);
    });
    $("f-reset").addEventListener("click", () => {
      $("f-search").value = "";
      setState({ period: "all", topic: -1, search: "" });
    });
    document.querySelectorAll("#authors .seg button").forEach((b) =>
      b.addEventListener("click", () => setState({ authorSort: b.dataset.sort })));
    $("rank-more").addEventListener("click", () => {
      state.authorsShown += RANK_PAGE;
      renderAuthorRank(filtered());
    });
    $("more").addEventListener("click", () => {
      state.shown += PAGE_SIZE;
      renderTable(filtered());
    });

    let lastWidth = document.querySelector("main").clientWidth;
    new ResizeObserver(() => {
      const w = document.querySelector("main").clientWidth;
      if (w !== lastWidth) { lastWidth = w; renderAll(); }
    }).observe(document.querySelector("main"));
    matchMedia("(prefers-color-scheme: dark)").addEventListener("change", renderAll);
  }

  async function init() {
    try {
      const response = await fetch("data.json");
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      DATA = await response.json();
    } catch (err) {
      $("lede").textContent = `Could not load paper data (${err.message}).`;
      return;
    }
    papers = DATA.papers.map((p) => ({
      ...p,
      search: `${p.t} ${p.a.map((i) => DATA.authors[i]).join(" ")}`.toLowerCase(),
    }));
    topicLayout = buildTopicLayout();
    $("lede").textContent =
      `${fmt(papers.length)} arXiv papers on ${DATA.site.subject}, collected daily since ${DATA.tracking_start} ` +
      `and last updated ${DATA.last_update}. Filter below; every chart follows the same filters.`;
    $("footer-note").textContent =
      `Data from arXiv via the ${DATA.site.repo} crawler. Topics are keyword matches from data/keywords.json. ` +
      `Map layout: TF-IDF of titles and abstracts, projected with t-SNE. Built ${DATA.generated}.`;
    initControls();
    renderAll();
  }

  init();
})();
