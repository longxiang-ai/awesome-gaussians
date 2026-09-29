# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-09-29 03:13:58

## 📰 Latest Updates

🔧 **[2026-08-08] Resilient arXiv Updates**
- Switched the crawler to the official HTTPS export API endpoint
- Added bounded retries for rate limits, server errors, and network timeouts
- Temporary arXiv outages now preserve existing data and finish scheduled runs with a warning
- Added atomic, non-empty JSON writes and fallback to the latest valid data when generating README

📚 **[2026-08-08] Community Paper Added**
- Added the HDR Gaussian Splatting paper suggested in [Issue #3](https://github.com/longxiang-ai/awesome-gaussians/issues/3)

🚀 **[2026-02] Major Feature Update — v2.0**
- **Unified CLI**: Single entry point `python main.py` with subcommands: `init`, `search`, `suggest`, `export-bib`, `readme`
- **Interactive Configuration Wizard**: Run `python main.py init` to set up keywords, domains, time range, and API keys step-by-step
- **Custom Time Range Filtering**: Support relative periods (`6m`, `1y`, `2y`) and absolute date ranges (`2024-01-01` to `2025-06-01`)
- **Smart Link Extraction**: Automatically extracts and classifies GitHub, project page, dataset, video, demo, and HuggingFace links from paper abstracts
- **BibTeX Export**: Fetch BibTeX from arXiv and export to `.bib` files with category/date filters
- **LLM Keyword Suggestion**: Paste a few paper titles or arXiv IDs, and an LLM automatically generates optimized search keywords
- **arXiv Domain Filtering**: Restrict searches to specific arXiv categories (e.g., `cs.CV`, `cs.GR`)

🔧 **[2025-06-26] Configurable Search Keywords Added**
- You can now customize search keywords by modifying `data/search_config.json`

- View detailed updates: [News.md](News.md) 📋

---

## Categories

- [3DGS Surveys](#3dgs-surveys) (5 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (89 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (160 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (193 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (41 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (213 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (28 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (194 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (84 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (8 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (43 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (81 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (107 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones](https://arxiv.org/abs/2609.24253v1)**  
  Authors: Zhongrui You, Zhen Li, Junli Liu, Zhigang Wang, Bin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24253v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://openflyscan.github.io)  
  Keywords: survey, ar, 3d gaussian, face, gaussian splatting, high-fidelity  
- **[Quality Assessment of 3D Gaussian Splatting: Distortions, Benchmarks, and Open Challenges](https://arxiv.org/abs/2609.23027v1)**  
  Authors: Shuai Liu, Binqiang Liu, Qingyu Mao, Jiacong Chen, Yongsheng Liang, Youneng Bao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23027v1.pdf)  
  Keywords: survey, ar, 3d gaussian, gaussian splatting, compression  
- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: survey, ar, gaussian splatting, illumination, 3d reconstruction, motion, geometry  
- **[UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys](https://arxiv.org/abs/2608.06404v1)**  
  Authors: Junxiong Zhou, Xuechen Li, Chonghao Qiu, Lang Qiao, Xiaowei Jia, Qi Yang, Chishan Zhang, Leikun Yin, Nanshan You, Vipin Kumar, David Mulla, Ce Yang, Zhenong Jin, Licheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06404v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://link-dev.github.io/UAV3DCrop)  
  Keywords: nerf, survey, dynamic, ar, 3d gaussian, gaussian splatting, 3d reconstruction, geometry  
- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: survey, dynamic, tracking, mapping, efficient, ar, 3d gaussian, high-fidelity, slam, localization  

### Acceleration

*Showing the latest 50 out of 89 papers*

- **[Rate-Distortion Adaptive Primitive Selection for Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2609.34367v1)**  
  Authors: Yulong Cheng, Youneng Bao, Junfeng Zhou, Mu Li, Jie Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34367v1.pdf)  
  Keywords: ar, efficient, fast, gaussian splatting, lightweight, vr  
- **[AGILE-GS: Anchor-Guided Fast Next-Best-View Selection for Active 3D Gaussian Splatting](https://arxiv.org/abs/2609.34176v1)**  
  Authors: Amirhossein Mollaei Khass, Nader Motee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34176v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, fast, geometry  
- **[Towards Practical Compression of 3D Gaussian Splatting](https://arxiv.org/abs/2609.30245v1)**  
  Authors: Pengpeng Yu, Yueru Chen, Fei Song, Tai Qin, Qi Zhang, Jing Wang, Yulan Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30245v1.pdf) | [![GitHub](https://img.shields.io/github/stars/pengpeng-yu/COSA-GS?style=social)](https://github.com/pengpeng-yu/COSA-GS)  
  Keywords: ar, compact, 3d gaussian, gaussian splatting, fast, compression, geometry  
- **[OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning](https://arxiv.org/abs/2609.29985v1)**  
  Authors: Haoran Wang, Shaoyu Cai, Adrian Azzarelli, Zhuodong Jiang, Guoxi Huang, Eng Tat Khoo, Brett Seymour, Fan Zhang, David Bull, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29985v1.pdf)  
  Keywords: nerf, ar, real-time rendering, efficient, compact, 3d gaussian, large scene, gaussian splatting, fast, 3d reconstruction  
- **[ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards](https://arxiv.org/abs/2609.26315v1)**  
  Authors: Alessandro Masini, Matteo Frosi, Mirko Usuelli, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26315v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, face, gaussian splatting, fast, slam  
- **[Ultra-fast Neural Inference for Stochastic Gaussian Splatting Denoising](https://arxiv.org/abs/2609.25604v1)**  
  Authors: Chenxiao Hu, Hao Zhang, Yanchen Zhang, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25604v1.pdf)  
  Keywords: fast, gaussian splatting, head, ar  
- **[GAPS: Generative Active Pseudo-view Selection for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.23436v2)**  
  Authors: Hongfei Zhu, Haochen Deng, Sitao Zhang, Ling Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23436v2.pdf)  
  Keywords: nerf, sparse-view, ar, real-time rendering, 3d gaussian, gaussian splatting, geometry  
- **[LiteTex-GS: Fast and Lightweight Texturing for Gaussian Splatting](https://arxiv.org/abs/2609.23380v1)**  
  Authors: Zhiwei Li, Yijia Guo, Yishi Lu, Liwen Hu, Hong Rao, Shengbo Chen, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23380v1.pdf)  
  Keywords: head, ar, compact, fast, gaussian splatting, lightweight, geometry  
- **[Splat-CBF: Safe Next-Best-View Control in 3D Gaussian-Splat Maps](https://arxiv.org/abs/2609.23100v1)**  
  Authors: Amirhossein Mollaei Khass, Athanasios Cosse, Nader Motee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23100v1.pdf)  
  Keywords: 3d gaussian, fast, motion, ar  
- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: localization, dynamic, tracking, mapping, robotics, ar, lighting, 3d gaussian, gaussian splatting, fast, slam, motion, geometry  

### Applications

*Showing the latest 50 out of 498 papers*

- **[EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation](https://arxiv.org/abs/2609.34853v1)**  
  Authors: Sungho Moon, Kota Shimomura, Junwoo Park, Wonhyeok Choi, Seunghun Lee, Takayoshi Yamashita, Sunghoon Im  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34853v1.pdf)  
  Keywords: segmentation, ar, compact, 3d gaussian, gaussian splatting, understanding, localization  
- **[GenNVS: Geometry-enhanced Novel View Synthesis via Disentangled 3D Prior](https://arxiv.org/abs/2609.34579v1)**  
  Authors: Yajiao Xiong, Youyu Luan, Xiaoyu Zhou, Yongtao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34579v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, geometry  
- **[Rate-Distortion Adaptive Primitive Selection for Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2609.34367v1)**  
  Authors: Yulong Cheng, Youneng Bao, Junfeng Zhou, Mu Li, Jie Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34367v1.pdf)  
  Keywords: ar, efficient, fast, gaussian splatting, lightweight, vr  
- **[AGILE-GS: Anchor-Guided Fast Next-Best-View Selection for Active 3D Gaussian Splatting](https://arxiv.org/abs/2609.34176v1)**  
  Authors: Amirhossein Mollaei Khass, Nader Motee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34176v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, fast, geometry  
- **[Gaussian Splatting-based Volumetric Video Compression with Sparse 4D Anchors](https://arxiv.org/abs/2609.33969v1)**  
  Authors: Ge Gao, Siyue Teng, Chanqgi Wang, Fan Zhang, Nantheera Anantrasirichai, Jui Chiu Chiang, Wen-Hsiao Peng, David Bull  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.33969v1.pdf)  
  Keywords: dynamic, ar, efficient, 4d, compact, 3d gaussian, gaussian splatting, compression, motion, geometry  
- **[Robot-GST: geometry-aware spatial-temporal robot policy representation and evaluation](https://arxiv.org/abs/2609.33872v1)**  
  Authors: Sichao Liu, Zekun Wang, Lixuan Tang, Yiming Li, Xiaohan Wang, Hanzhi Zhang, Daqiang Guo, Peng Zhou, Lihui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.33872v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robot-gst.github.io)  
  Keywords: ar, 3d gaussian, gaussian splatting, high-fidelity, geometry  
- **[FeCoSplat: Feedback-Guided Compression for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2609.33330v1)**  
  Authors: Yuxuan Li, Yihang Chen, Yufeng Zhang, Jianfei Cai, Weiyao Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.33330v1.pdf)  
  Keywords: ar, efficient, compact, 3d gaussian, gaussian splatting, lightweight, compression  
- **[ProDyGS: Dynamic Gaussian Splatting from a Single Static Monocular Camera](https://arxiv.org/abs/2609.32711v1)**  
  Authors: Ugo Leone Cavalcanti, Fabio Tosi, Matteo Poggi, Andrea Conti, Vladimir Zlokolica, Valerio Cambareri, Stefano Mattoccia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32711v1.pdf)  
  Keywords: nerf, dynamic, ar, deformation, 3d gaussian, gaussian splatting, motion  
- **[Endo-TSR: Temporal Spectral Modeling of Appearance and Motion for Endoscopic Reconstruction](https://arxiv.org/abs/2609.32399v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Qi Shao, Zhuoxiao Li, Zhe Tang, Limin Yu, Baoru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32399v1.pdf)  
  Keywords: nerf, ar, efficient, gaussian splatting, face, motion  
- **[FoundDSR: A Generalizable Foundation Model with Guided 2D Gaussian Splatting for Depth Super-Resolution](https://arxiv.org/abs/2609.32323v1)**  
  Authors: Zhengxue Wang, Zhiqiang Yan, Yuan Wu, Guangwei Gao, Xiang Li, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32323v1.pdf)  
  Keywords: gaussian splatting, ar  

### Avatar Generation

*Showing the latest 50 out of 160 papers*

- **[Endo-TSR: Temporal Spectral Modeling of Appearance and Motion for Endoscopic Reconstruction](https://arxiv.org/abs/2609.32399v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Qi Shao, Zhuoxiao Li, Zhe Tang, Limin Yu, Baoru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32399v1.pdf)  
  Keywords: nerf, ar, efficient, gaussian splatting, face, motion  
- **[Federated 3D Gaussian Splatting for Large-Scale Scene Reconstruction at Wireless Edge](https://arxiv.org/abs/2609.32177v1)**  
  Authors: Guanlin Wu, Chao Hu, Pu Chen, Juyong Zhang, Han Hu, Shuguang Cui, Jie Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32177v1.pdf)  
  Keywords: ar, efficient, 3d gaussian, gaussian splatting, face, lightweight, large scene  
- **[ControlGS: Conditioning Neural Gaussians for Downstream-Processing-Aware XR Rendering](https://arxiv.org/abs/2609.32038v1)**  
  Authors: Weikai Lin, Junjie Zhao, Carl Marshall, Sushant Kondguli, Yuhao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32038v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://horizon-lab.org/controlgs)  
  Keywords: ar, human, head, dynamic  
- **[Gauss What You Need: Compact Gaussian Splatting Across Scene Scales](https://arxiv.org/abs/2609.31248v1)**  
  Authors: Afif Boudaoud, Jiayi Liu, Alexandru Calotoiu, Torsten Hoefler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31248v1.pdf)  
  Keywords: ar, compact, 3d gaussian, face, gaussian splatting  
- **[3dgs-sc: a controlled static screen-content benchmark for 3d gaussian splatting](https://arxiv.org/abs/2609.31756v1)**  
  Authors: Shicheng Cai, Hao Zhang, Dong Dai, Xuerui Ma, Ying Hu, Tao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31756v1.pdf)  
  Keywords: 3d gaussian, face, gaussian splatting, ar  
- **[ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards](https://arxiv.org/abs/2609.26315v1)**  
  Authors: Alessandro Masini, Matteo Frosi, Mirko Usuelli, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26315v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, face, gaussian splatting, fast, slam  
- **[Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking](https://arxiv.org/abs/2609.25746v1)**  
  Authors: Edward Beng Wai Tan, Siew-Kei Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25746v1.pdf)  
  Keywords: tracking, ar, 3d gaussian, face, gaussian splatting, outdoor, slam, geometry  
- **[Ultra-fast Neural Inference for Stochastic Gaussian Splatting Denoising](https://arxiv.org/abs/2609.25604v1)**  
  Authors: Chenxiao Hu, Hao Zhang, Yanchen Zhang, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25604v1.pdf)  
  Keywords: fast, gaussian splatting, head, ar  
- **[Agentic Building-Aware Satellite Gaussian Splatting for Auditable Urban DSM Reconstruction](https://arxiv.org/abs/2609.25578v1)**  
  Authors: Wentao Sun, Zhengsen Xu, Yiping Chen, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25578v1.pdf)  
  Keywords: semantic, ar, neural rendering, face, gaussian splatting, 3d reconstruction  
- **[OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones](https://arxiv.org/abs/2609.24253v1)**  
  Authors: Zhongrui You, Zhen Li, Junli Liu, Zhigang Wang, Bin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24253v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://openflyscan.github.io)  
  Keywords: survey, ar, 3d gaussian, face, gaussian splatting, high-fidelity  

### Dynamic Scene

*Showing the latest 50 out of 193 papers*

- **[Gaussian Splatting-based Volumetric Video Compression with Sparse 4D Anchors](https://arxiv.org/abs/2609.33969v1)**  
  Authors: Ge Gao, Siyue Teng, Chanqgi Wang, Fan Zhang, Nantheera Anantrasirichai, Jui Chiu Chiang, Wen-Hsiao Peng, David Bull  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.33969v1.pdf)  
  Keywords: dynamic, ar, efficient, 4d, compact, 3d gaussian, gaussian splatting, compression, motion, geometry  
- **[ProDyGS: Dynamic Gaussian Splatting from a Single Static Monocular Camera](https://arxiv.org/abs/2609.32711v1)**  
  Authors: Ugo Leone Cavalcanti, Fabio Tosi, Matteo Poggi, Andrea Conti, Vladimir Zlokolica, Valerio Cambareri, Stefano Mattoccia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32711v1.pdf)  
  Keywords: nerf, dynamic, ar, deformation, 3d gaussian, gaussian splatting, motion  
- **[Endo-TSR: Temporal Spectral Modeling of Appearance and Motion for Endoscopic Reconstruction](https://arxiv.org/abs/2609.32399v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Qi Shao, Zhuoxiao Li, Zhe Tang, Limin Yu, Baoru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32399v1.pdf)  
  Keywords: nerf, ar, efficient, gaussian splatting, face, motion  
- **[OneFixer: High-Quality and Consistent One-Step Autoregressive 3DGS Refinement for Driving Scenes](https://arxiv.org/abs/2609.32175v1)**  
  Authors: Boseong Jeon, Junhyeop Lee, Juhan Cha, Hayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32175v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://onefixer-web.vercel.app/) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://onefixer-web.vercel.app)  
  Keywords: dynamic, ar, 3d gaussian, gaussian splatting, geometry  
- **[ControlGS: Conditioning Neural Gaussians for Downstream-Processing-Aware XR Rendering](https://arxiv.org/abs/2609.32038v1)**  
  Authors: Weikai Lin, Junjie Zhao, Carl Marshall, Sushant Kondguli, Yuhao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32038v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://horizon-lab.org/controlgs)  
  Keywords: ar, human, head, dynamic  
- **[OC-GS: Gaussian Splatting for Irregular Turntable Capture](https://arxiv.org/abs/2609.31572v1)**  
  Authors: Jae Joong Lee, Bedrich Benes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31572v1.pdf)  
  Keywords: ar, gaussian splatting, motion, geometry  
- **[RECAST: From Log Replay to Closed-Loop Driving Simulation with View-Complete Actors](https://arxiv.org/abs/2609.31374v1)**  
  Authors: Zijun Zhao, Liewen Liao, Kang Shen, Songan Zhang, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31374v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zijunkr.github.io/RECAST)  
  Keywords: ar, dynamic, 3d gaussian, gaussian splatting, motion  
- **[Reliability-Regulated Trajectory Optimization for Progressive COLMAP-Free 3D Gaussian Splatting](https://arxiv.org/abs/2609.30865v1)**  
  Authors: Zijian Wu, Jinliang Wang, Zidian Lin, Ying Song, Ziqian Lu, Hanjie Ma, Zhen Ye, Mingfeng Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30865v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Zijian1026/RRTO-CF3DGS?style=social)](https://github.com/Zijian1026/RRTO-CF3DGS)  
  Keywords: tracking, dynamic, ar, 3d gaussian, gaussian splatting, motion  
- **[From Mono to Stereo: Accelerating Binocular Gaussian Splatting via Reprojection and Selective Patching](https://arxiv.org/abs/2609.30741v1)**  
  Authors: Hongfei Zhu, Ling Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30741v1.pdf)  
  Keywords: nerf, ar, gaussian splatting, vr, motion  
- **[ADATEX4D: adaptive texture capacity allocation for 4D gaussian splatting](https://arxiv.org/abs/2609.29963v1)**  
  Authors: De Jiang, Peiqiang Wang, Kehong Yuan, Shaohua Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29963v1.pdf)  
  Keywords: dynamic, ar, efficient, deformation, 4d, gaussian splatting  

### Few-shot

- **[GAPS: Generative Active Pseudo-view Selection for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.23436v2)**  
  Authors: Hongfei Zhu, Haochen Deng, Sitao Zhang, Ling Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23436v2.pdf)  
  Keywords: nerf, sparse-view, ar, real-time rendering, 3d gaussian, gaussian splatting, geometry  
- **[D3GS: Depth, DINO, and RGB Diffusion Co-Guided 3D Gaussian Splatting for Sparse-View Reconstruction](https://arxiv.org/abs/2609.22941v1)**  
  Authors: Yunqi Gao, Zhanfeng Liao, Hanzhang Tu, Zhaoqi Su, Guoqing Zheng, Songtao Wang, Hongwen Zhang, Zhou Xue, Leyuan Liu, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.22941v1.pdf)  
  Keywords: nerf, sparse-view, ar, 3d gaussian, gaussian splatting, geometry  
- **[LINGO: Latent Initialization and Gradient Optimization for Sparse-view X-ray Novel View Synthesis and CT Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2609.22849v1)**  
  Authors: Lifeng Xing, Dequan Jin, Kunpeng Bu, Peigeng He, Shihui Ying  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.22849v1.pdf)  
  Keywords: sparse-view, ar, dynamic, 3d gaussian, gaussian splatting  
- **[4DGS-Fixer: Generative Sparse-View 4D Gaussian Splatting with Iterative Refinement Guided by Video Diffusion Priors](https://arxiv.org/abs/2609.21176v2)**  
  Authors: Haitao Huang, Shenghao Zhao, Boyuan Tian, Shin-Fang Chng, Songlin Yang, Sheila Lim, Huangying Zhan, Yi Xu, Anyi Rao, Frank Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21176v2.pdf)  
  Keywords: sparse-view, dynamic, ar, 4d, gaussian splatting, large scene  
- **[Geometry beneath the Waves: Dense Priors for Sparse-View Underwater 3D Gaussian Splatting](https://arxiv.org/abs/2609.18737v1)**  
  Authors: Harvey Caldeira, Haoran Wang, Guoxi Huang, Shaoyu Cai, Rachel Fu, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18737v1.pdf)  
  Keywords: sparse-view, ar, 3d gaussian, gaussian splatting, 3d reconstruction, geometry  
- **[CADSplat: Sparse-View 3D Gaussian Splatting Aided by CAD Models for Robust, Photorealistic Digital-Twin Reconstruction](https://arxiv.org/abs/2609.18473v1)**  
  Authors: Kristof Overdulve, Lode Jorissen, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18473v1.pdf)  
  Keywords: sparse-view, ar, few-shot, deformation, 3d gaussian, gaussian splatting, face  
- **[Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement](https://arxiv.org/abs/2609.17039v1)**  
  Authors: Yuetong Wang, Jinsheng Quan, Yi Yang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17039v1.pdf)  
  Keywords: sparse-view, ar, 3d gaussian, gaussian splatting, motion, geometry  
- **[CGGT: Curve-Grounded Geometry Transformer for 3D Parametric Curve Reconstruction](https://arxiv.org/abs/2609.14521v1)**  
  Authors: Zhirui Gao, Renjiao Yi, Yunfan Ye, Ruizhen Hu, Chenyang Zhu, Wei Chen, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14521v1.pdf)  
  Keywords: nerf, sparse-view, ar, compact, fast, geometry  
- **[VS-Splat: Voxel-Selective feed-forward Gaussian Splatting for end-to-end 3D object reconstruction from sparse-views](https://arxiv.org/abs/2609.12343v1)**  
  Authors: Yunsu Jeong, Hyuk Heo, Youngsang Kwak, Jaehwa Kwak, Il Yong Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.12343v1.pdf)  
  Keywords: sparse-view, gaussian splatting, ar  
- **[Shape-guided Gaussian Splatting for Sparse-View X-ray 3D Reconstruction](https://arxiv.org/abs/2609.10376v1)**  
  Authors: Pranav Poudel, Florence Dell'Aniello Picard, Nairouz Shehata, Frédéric Lavoie, Herve Lombaert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.10376v1.pdf) | [![GitHub](https://img.shields.io/github/stars/polyshape-lab/ShapeGuidedGaussian?style=social)](https://github.com/polyshape-lab/ShapeGuidedGaussian)  
  Keywords: sparse-view, ar, 3d gaussian, gaussian splatting, 3d reconstruction, geometry  

### Geometry Reconstruction

*Showing the latest 50 out of 213 papers*

- **[GenNVS: Geometry-enhanced Novel View Synthesis via Disentangled 3D Prior](https://arxiv.org/abs/2609.34579v1)**  
  Authors: Yajiao Xiong, Youyu Luan, Xiaoyu Zhou, Yongtao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34579v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, geometry  
- **[AGILE-GS: Anchor-Guided Fast Next-Best-View Selection for Active 3D Gaussian Splatting](https://arxiv.org/abs/2609.34176v1)**  
  Authors: Amirhossein Mollaei Khass, Nader Motee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34176v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, fast, geometry  
- **[Gaussian Splatting-based Volumetric Video Compression with Sparse 4D Anchors](https://arxiv.org/abs/2609.33969v1)**  
  Authors: Ge Gao, Siyue Teng, Chanqgi Wang, Fan Zhang, Nantheera Anantrasirichai, Jui Chiu Chiang, Wen-Hsiao Peng, David Bull  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.33969v1.pdf)  
  Keywords: dynamic, ar, efficient, 4d, compact, 3d gaussian, gaussian splatting, compression, motion, geometry  
- **[Robot-GST: geometry-aware spatial-temporal robot policy representation and evaluation](https://arxiv.org/abs/2609.33872v1)**  
  Authors: Sichao Liu, Zekun Wang, Lixuan Tang, Yiming Li, Xiaohan Wang, Hanzhi Zhang, Daqiang Guo, Peng Zhou, Lihui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.33872v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robot-gst.github.io)  
  Keywords: ar, 3d gaussian, gaussian splatting, high-fidelity, geometry  
- **[OneFixer: High-Quality and Consistent One-Step Autoregressive 3DGS Refinement for Driving Scenes](https://arxiv.org/abs/2609.32175v1)**  
  Authors: Boseong Jeon, Junhyeop Lee, Juhan Cha, Hayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32175v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://onefixer-web.vercel.app/) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://onefixer-web.vercel.app)  
  Keywords: dynamic, ar, 3d gaussian, gaussian splatting, geometry  
- **[OC-GS: Gaussian Splatting for Irregular Turntable Capture](https://arxiv.org/abs/2609.31572v1)**  
  Authors: Jae Joong Lee, Bedrich Benes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31572v1.pdf)  
  Keywords: ar, gaussian splatting, motion, geometry  
- **[Towards Practical Compression of 3D Gaussian Splatting](https://arxiv.org/abs/2609.30245v1)**  
  Authors: Pengpeng Yu, Yueru Chen, Fei Song, Tai Qin, Qi Zhang, Jing Wang, Yulan Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30245v1.pdf) | [![GitHub](https://img.shields.io/github/stars/pengpeng-yu/COSA-GS?style=social)](https://github.com/pengpeng-yu/COSA-GS)  
  Keywords: ar, compact, 3d gaussian, gaussian splatting, fast, compression, geometry  
- **[OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning](https://arxiv.org/abs/2609.29985v1)**  
  Authors: Haoran Wang, Shaoyu Cai, Adrian Azzarelli, Zhuodong Jiang, Guoxi Huang, Eng Tat Khoo, Brett Seymour, Fan Zhang, David Bull, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29985v1.pdf)  
  Keywords: nerf, ar, real-time rendering, efficient, compact, 3d gaussian, large scene, gaussian splatting, fast, 3d reconstruction  
- **[SplatLabel: Pseudo-Labelling through 4D Gaussian Splatting](https://arxiv.org/abs/2609.29836v1)**  
  Authors: Nitya Nanvani, Andras Palffy, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29836v1.pdf)  
  Keywords: semantic, segmentation, dynamic, tracking, ar, 4d, gaussian splatting, geometry  
- **[PePESeg3D: Perception Prior Enhances Multi-Scale Segmentation for 3D Gaussian Splatting](https://arxiv.org/abs/2609.28645v1)**  
  Authors: Sungjae Choi, Seunghee Koh, Junmo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28645v1.pdf) | [![GitHub](https://img.shields.io/github/stars/BeCow5X5/PePESeg3D?style=social)](https://github.com/BeCow5X5/PePESeg3D)  
  Keywords: nerf, semantic, segmentation, ar, lighting, 3d gaussian, gaussian splatting, geometry  

### Large Scene

- **[Federated 3D Gaussian Splatting for Large-Scale Scene Reconstruction at Wireless Edge](https://arxiv.org/abs/2609.32177v1)**  
  Authors: Guanlin Wu, Chao Hu, Pu Chen, Juyong Zhang, Han Hu, Shuguang Cui, Jie Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32177v1.pdf)  
  Keywords: ar, efficient, 3d gaussian, gaussian splatting, face, lightweight, large scene  
- **[ChronoFuseGS: Multi-Temporal Gaussian Fusion with Per-Splat Persistence and Change Visualization](https://arxiv.org/abs/2609.31339v1)**  
  Authors: Tobias Batik, Diana Marin, Peter Kán, Hannes Kaufmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31339v1.pdf)  
  Keywords: outdoor, gaussian splatting, ar  
- **[OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning](https://arxiv.org/abs/2609.29985v1)**  
  Authors: Haoran Wang, Shaoyu Cai, Adrian Azzarelli, Zhuodong Jiang, Guoxi Huang, Eng Tat Khoo, Brett Seymour, Fan Zhang, David Bull, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29985v1.pdf)  
  Keywords: nerf, ar, real-time rendering, efficient, compact, 3d gaussian, large scene, gaussian splatting, fast, 3d reconstruction  
- **[Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models](https://arxiv.org/abs/2609.26007v1)**  
  Authors: Yuhang Zhang, Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Weiying Wang, Steven Yang, Qingsong Yan, Chao Yan, Mir Feroskhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26007v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, outdoor, motion  
- **[Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking](https://arxiv.org/abs/2609.25746v1)**  
  Authors: Edward Beng Wai Tan, Siew-Kei Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25746v1.pdf)  
  Keywords: tracking, ar, 3d gaussian, face, gaussian splatting, outdoor, slam, geometry  
- **[Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene Reconstruction](https://arxiv.org/abs/2609.23796v2)**  
  Authors: Yang-Tian Sun, Tianjia Liu, Zehuan Huang, Yi-Hua Huang, Xiaoyang Lyu, Ziyi Yang, Zi-Xin Zou, Yuan-Chen Guo, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23796v2.pdf)  
  Keywords: ar, face, high-fidelity, outdoor, geometry  
- **[Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization](https://arxiv.org/abs/2609.21347v1)**  
  Authors: Xiangfei Guo, Hao Shi, Yufan Zhang, Zhonghua Yi, Yongqi Mao, Xiaoting Yin, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21347v1.pdf) | [![GitHub](https://img.shields.io/github/stars/guoxf304/CubeSplat?style=social)](https://github.com/guoxf304/CubeSplat)  
  Keywords: tracking, mapping, ar, 3d gaussian, face, gaussian splatting, high-fidelity, outdoor, slam  
- **[4DGS-Fixer: Generative Sparse-View 4D Gaussian Splatting with Iterative Refinement Guided by Video Diffusion Priors](https://arxiv.org/abs/2609.21176v2)**  
  Authors: Haitao Huang, Shenghao Zhao, Boyuan Tian, Shin-Fang Chng, Songlin Yang, Sheila Lim, Huangying Zhan, Yi Xu, Anyi Rao, Frank Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21176v2.pdf)  
  Keywords: sparse-view, dynamic, ar, 4d, gaussian splatting, large scene  
- **[The Neverwhere Visual Parkour Benchmark Suite](https://arxiv.org/abs/2609.16443v1)**  
  Authors: Ziyu Chen, Henghui Bao, Haoran Chang, Alan Yu, Ran Choi, Kai McClennen, Gio Huh, Kevin Yang, Ri-Zhao Qiu, Yajvan Ravan, John J. Leonard, Xiaolong Wang, Phillip Isola, Ge Yang, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16443v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziyc.github.io/neverwhere-bench)  
  Keywords: ar, 3d gaussian, gaussian splatting, outdoor, motion  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: human, dynamic, ar, 4d, fast, gaussian splatting, illumination, outdoor  

### Model Compression

*Showing the latest 50 out of 194 papers*

- **[EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation](https://arxiv.org/abs/2609.34853v1)**  
  Authors: Sungho Moon, Kota Shimomura, Junwoo Park, Wonhyeok Choi, Seunghun Lee, Takayoshi Yamashita, Sunghoon Im  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34853v1.pdf)  
  Keywords: segmentation, ar, compact, 3d gaussian, gaussian splatting, understanding, localization  
- **[Rate-Distortion Adaptive Primitive Selection for Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2609.34367v1)**  
  Authors: Yulong Cheng, Youneng Bao, Junfeng Zhou, Mu Li, Jie Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34367v1.pdf)  
  Keywords: ar, efficient, fast, gaussian splatting, lightweight, vr  
- **[Gaussian Splatting-based Volumetric Video Compression with Sparse 4D Anchors](https://arxiv.org/abs/2609.33969v1)**  
  Authors: Ge Gao, Siyue Teng, Chanqgi Wang, Fan Zhang, Nantheera Anantrasirichai, Jui Chiu Chiang, Wen-Hsiao Peng, David Bull  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.33969v1.pdf)  
  Keywords: dynamic, ar, efficient, 4d, compact, 3d gaussian, gaussian splatting, compression, motion, geometry  
- **[FeCoSplat: Feedback-Guided Compression for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2609.33330v1)**  
  Authors: Yuxuan Li, Yihang Chen, Yufeng Zhang, Jianfei Cai, Weiyao Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.33330v1.pdf)  
  Keywords: ar, efficient, compact, 3d gaussian, gaussian splatting, lightweight, compression  
- **[Endo-TSR: Temporal Spectral Modeling of Appearance and Motion for Endoscopic Reconstruction](https://arxiv.org/abs/2609.32399v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Qi Shao, Zhuoxiao Li, Zhe Tang, Limin Yu, Baoru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32399v1.pdf)  
  Keywords: nerf, ar, efficient, gaussian splatting, face, motion  
- **[Federated 3D Gaussian Splatting for Large-Scale Scene Reconstruction at Wireless Edge](https://arxiv.org/abs/2609.32177v1)**  
  Authors: Guanlin Wu, Chao Hu, Pu Chen, Juyong Zhang, Han Hu, Shuguang Cui, Jie Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32177v1.pdf)  
  Keywords: ar, efficient, 3d gaussian, gaussian splatting, face, lightweight, large scene  
- **[Scaling Density Functional Theory with Gaussian Splatting](https://arxiv.org/abs/2609.31483v1)**  
  Authors: Andrés Guzmán-Cordero, Cindy Zhang, Majdi Hassan, Marta Skreta, Kirill Neklyudov, Matija Medvidović  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31483v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, ar  
- **[Gauss What You Need: Compact Gaussian Splatting Across Scene Scales](https://arxiv.org/abs/2609.31248v1)**  
  Authors: Afif Boudaoud, Jiayi Liu, Alexandru Calotoiu, Torsten Hoefler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31248v1.pdf)  
  Keywords: ar, compact, 3d gaussian, face, gaussian splatting  
- **[Spackle: Completing Large View Single Image NVS with Adaptive Gaussians](https://arxiv.org/abs/2609.30941v1)**  
  Authors: Xuanzhi Liu, Yuhe Zhou, Xinyi Wu, Zhenyao Wu, Jinghao Chen, Ruize Han, Song Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30941v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, lightweight  
- **[LiTe-GS: Oracle-Efficient Next Best View Selection for 3D Gaussian Splatting](https://arxiv.org/abs/2609.30393v1)**  
  Authors: Vivek Pandey, Amirhossein Mollaei Khass, Nader Motee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30393v1.pdf)  
  Keywords: nerf, ar, efficient, 3d gaussian, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 84 papers*

- **[Robot-GST: geometry-aware spatial-temporal robot policy representation and evaluation](https://arxiv.org/abs/2609.33872v1)**  
  Authors: Sichao Liu, Zekun Wang, Lixuan Tang, Yiming Li, Xiaohan Wang, Hanzhi Zhang, Daqiang Guo, Peng Zhou, Lihui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.33872v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robot-gst.github.io)  
  Keywords: ar, 3d gaussian, gaussian splatting, high-fidelity, geometry  
- **[Dynamic Thermal Gaussians: Multimodal 4D Gaussian Splatting](https://arxiv.org/abs/2609.24531v1)**  
  Authors: Rongfeng Lu, Lifeng Lin, Xiaobao Wei, Quan Chen, Ming Lu, Yitian Xue, Yaoqi Sun, Yuhan Gao, Anke Xue, Chenggang Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24531v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LinLif1869/DTG?style=social)](https://github.com/LinLif1869/DTG)  
  Keywords: dynamic, ar, deformation, 4d, gaussian splatting, high-fidelity, motion, geometry  
- **[OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones](https://arxiv.org/abs/2609.24253v1)**  
  Authors: Zhongrui You, Zhen Li, Junli Liu, Zhigang Wang, Bin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24253v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://openflyscan.github.io)  
  Keywords: survey, ar, 3d gaussian, face, gaussian splatting, high-fidelity  
- **[Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene Reconstruction](https://arxiv.org/abs/2609.23796v2)**  
  Authors: Yang-Tian Sun, Tianjia Liu, Zehuan Huang, Yi-Hua Huang, Xiaoyang Lyu, Ziyi Yang, Zi-Xin Zou, Yuan-Chen Guo, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23796v2.pdf)  
  Keywords: ar, face, high-fidelity, outdoor, geometry  
- **[GARO: Geometry-Aware Redundancy Optimization for Real-Time and High-Fidelity Dynamic Gaussian Splatting](https://arxiv.org/abs/2609.23509v1)**  
  Authors: Huiwen Xue, Kaixing Zhao, Zuheng Ming, Tingcheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23509v1.pdf)  
  Keywords: dynamic, ar, compact, gaussian splatting, face, high-fidelity, geometry  
- **[Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization](https://arxiv.org/abs/2609.21347v1)**  
  Authors: Xiangfei Guo, Hao Shi, Yufan Zhang, Zhonghua Yi, Yongqi Mao, Xiaoting Yin, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21347v1.pdf) | [![GitHub](https://img.shields.io/github/stars/guoxf304/CubeSplat?style=social)](https://github.com/guoxf304/CubeSplat)  
  Keywords: tracking, mapping, ar, 3d gaussian, face, gaussian splatting, high-fidelity, outdoor, slam  
- **[AirSplan: Risk-Aware Motion Planning for Quadrotors in Cluttered 3D Gaussian Splats](https://arxiv.org/abs/2609.21226v1)**  
  Authors: Seth Isaacson, William Hong, Katherine A. Skinner, Ram Vasudevan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21226v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, high-fidelity, motion, geometry  
- **[Demonstration Synthesis from a Single Scan via Gaussian Splatting for Visuomotor Policy Learning](https://arxiv.org/abs/2609.21112v1)**  
  Authors: Beichen Wang, Yuen-Hei Yeung, V. R. Sridhar Devarakonda, Xuesu Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21112v1.pdf)  
  Keywords: human, dynamic, ar, 3d gaussian, gaussian splatting, high-fidelity  
- **[DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230v1)**  
  Authors: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17230v1.pdf)  
  Keywords: dynamic, ar, efficient, compact, 3d gaussian, fast, high-fidelity, 3d reconstruction, motion  
- **[Deformable 2D Gaussian Splatting for Efficient 4K Video Compression](https://arxiv.org/abs/2609.14129v1)**  
  Authors: Chenhao Zhang, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14129v1.pdf)  
  Keywords: ar, efficient, deformation, fast, gaussian splatting, high-fidelity, lightweight, compression  

### Ray Tracing

- **[Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)**  
  Authors: Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/vorotracing)  
  Keywords: nerf, ray tracing, ar, real-time rendering, compact, 3d gaussian, gaussian splatting, fast, face, motion  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: nerf, ray tracing, ar, mapping, shadow, efficient, compact, 3d gaussian, gaussian splatting, fast, reflection  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: ray tracing, ar, efficient, lighting, gaussian splatting, illumination, relighting, face, reflection  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: ray tracing, human, dynamic, ar, 3d gaussian, gaussian splatting, face, high-fidelity, motion, reflection, geometry  
- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: human, ar, ray casting, compact, gaussian splatting, geometry  
- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869v1)**  
  Authors: Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30869v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gray)  
  Keywords: ray tracing, ar, 3d gaussian, gaussian splatting, fast  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: ray tracing, ar, real-time rendering, efficient, 3d gaussian, gaussian splatting, fast, reflection, path tracing, geometry  
- **[RenderFormer++: Scalable and Physics-Informed Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v2)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v2.pdf)  
  Keywords: ar, neural rendering, compact, light transport, illumination, global illumination  

### Relighting

- **[PePESeg3D: Perception Prior Enhances Multi-Scale Segmentation for 3D Gaussian Splatting](https://arxiv.org/abs/2609.28645v1)**  
  Authors: Sungjae Choi, Seunghee Koh, Junmo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28645v1.pdf) | [![GitHub](https://img.shields.io/github/stars/BeCow5X5/PePESeg3D?style=social)](https://github.com/BeCow5X5/PePESeg3D)  
  Keywords: nerf, semantic, segmentation, ar, lighting, 3d gaussian, gaussian splatting, geometry  
- **[Relightable 3D Avatar Reconstruction with Semantic-Adaptive Motion-Illumination Responses](https://arxiv.org/abs/2609.24158v1)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Jijie Li, Baiqin Wang, Shukai Chen, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24158v1.pdf)  
  Keywords: head, semantic, ar, lighting, relightable, 3d gaussian, animation, compact, illumination, relighting, avatar, lightweight, motion  
- **[RawSLAM: Online HDR Gaussian SLAM from Linear Radiance](https://arxiv.org/abs/2609.20589v1)**  
  Authors: Marina Orozco González, Luis Merino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.20589v1.pdf)  
  Keywords: dynamic, tracking, shadow, mapping, ar, lighting, gaussian splatting, illumination, slam, motion  
- **[GS-PI: An Optimization-Decoupled Appearance Decomposition Approach for Generating PBR Gaussian Assets](https://arxiv.org/abs/2609.19907v1)**  
  Authors: Jieting Xu, Rengan Xie, Zijian Huang, Zehui Jin, Rui Wang, Yuchi Huo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.19907v1.pdf)  
  Keywords: semantic, ar, efficient, lighting, relightable, gaussian splatting, illumination, geometry  
- **[RGS: Reflection-aware Gaussian Splatting via Learning Geometry Continuity for Reflective Objects](https://arxiv.org/abs/2609.19421v1)**  
  Authors: Xiaobiao Du, Yida Wang, Cheng Bi, Kun Zhan, Xin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.19421v1.pdf)  
  Keywords: ar, 3d gaussian, face, gaussian splatting, reflection, geometry  
- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: localization, dynamic, tracking, mapping, robotics, ar, lighting, 3d gaussian, gaussian splatting, fast, slam, motion, geometry  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: human, dynamic, ar, 4d, fast, gaussian splatting, illumination, outdoor  
- **[RenderFormer-V2: Neural Rendering with Heterogeneous Scene Primitives](https://arxiv.org/abs/2609.05738v1)**  
  Authors: Chong Zeng, Yue Dong, Pieter Peers, Lvmin Zhang, Maneesh Agrawala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05738v1.pdf)  
  Keywords: ar, neural rendering, lighting, light transport, face  
- **[Where Appearance Fails, Geometry Recognizes: A CAD-Free 3D Shape Prior That Complements Vision Foundation Models](https://arxiv.org/abs/2609.04381v1)**  
  Authors: Chenxi Tao, Seung-Kyum Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04381v1.pdf)  
  Keywords: ar, robotics, lighting, 3d gaussian, gaussian splatting, recognition, geometry  
- **[Sparse auto-regressive modeling for scene generation from multi-view images](https://arxiv.org/abs/2609.03931v1)**  
  Authors: Thomas Lucas, Maxime Pietrantoni, Philippe Weinzaepfel, Wonjune Cho, Bardienus Pieter Duisterhof, Vincent Leroy, Jerome Revaud  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03931v1.pdf)  
  Keywords: ar, efficient, lighting, compact, 3d gaussian, gaussian splatting  

### SLAM

*Showing the latest 50 out of 81 papers*

- **[EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation](https://arxiv.org/abs/2609.34853v1)**  
  Authors: Sungho Moon, Kota Shimomura, Junwoo Park, Wonhyeok Choi, Seunghun Lee, Takayoshi Yamashita, Sunghoon Im  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34853v1.pdf)  
  Keywords: segmentation, ar, compact, 3d gaussian, gaussian splatting, understanding, localization  
- **[Reliability-Regulated Trajectory Optimization for Progressive COLMAP-Free 3D Gaussian Splatting](https://arxiv.org/abs/2609.30865v1)**  
  Authors: Zijian Wu, Jinliang Wang, Zidian Lin, Ying Song, Ziqian Lu, Hanjie Ma, Zhen Ye, Mingfeng Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30865v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Zijian1026/RRTO-CF3DGS?style=social)](https://github.com/Zijian1026/RRTO-CF3DGS)  
  Keywords: tracking, dynamic, ar, 3d gaussian, gaussian splatting, motion  
- **[SplatLabel: Pseudo-Labelling through 4D Gaussian Splatting](https://arxiv.org/abs/2609.29836v1)**  
  Authors: Nitya Nanvani, Andras Palffy, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29836v1.pdf)  
  Keywords: semantic, segmentation, dynamic, tracking, ar, 4d, gaussian splatting, geometry  
- **[From Scattered Gaussians to Structured Maps: Efficient Gaussian Splatting Coding via Dual-phase Morton Sorting](https://arxiv.org/abs/2609.29041v1)**  
  Authors: Bolin Chen, Shanzhi Yin, Ru-Ling Liao, Yibo Fan, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29041v1.pdf)  
  Keywords: ar, mapping, efficient, 3d gaussian, gaussian splatting, compression  
- **[ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards](https://arxiv.org/abs/2609.26315v1)**  
  Authors: Alessandro Masini, Matteo Frosi, Mirko Usuelli, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26315v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, face, gaussian splatting, fast, slam  
- **[Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking](https://arxiv.org/abs/2609.25746v1)**  
  Authors: Edward Beng Wai Tan, Siew-Kei Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25746v1.pdf)  
  Keywords: tracking, ar, 3d gaussian, face, gaussian splatting, outdoor, slam, geometry  
- **[BayesianGS-SLAM: Uncertainty-Aware Neural Rendering SLAM via Probabilistic Formulation](https://arxiv.org/abs/2609.24140v1)**  
  Authors: Kyeongsu Kang, Seongbo Ha, Sibaek Lee, Hyeonwoo Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24140v1.pdf)  
  Keywords: tracking, mapping, neural rendering, ar, 3d gaussian, gaussian splatting, slam  
- **[Elevator-VIGS: Separating Elevator Motion from Robot Motion in Visual-Inertial Gaussian Splatting SLAM](https://arxiv.org/abs/2609.23491v1)**  
  Authors: Rui Zhou, Zihan Zhu, Wei Zhang, Zizhou Luo, Norbert Haala, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ruizhou-cn.github.io/elevator-vigs)  
  Keywords: tracking, mapping, ar, 3d gaussian, gaussian splatting, slam, motion  
- **[VDGS: Visibility-Driven Large-Scale 3D Gaussian Splatting for Aerial Scene Reconstruction](https://arxiv.org/abs/2609.23049v1)**  
  Authors: Haolin Yu, Jiadong Tang, YiXian Wang, Yu Gao, Shi He, Zhilin Lai, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23049v1.pdf)  
  Keywords: ar, mapping, 3d gaussian, face, gaussian splatting, autonomous driving  
- **[Kinematic Interface for the Wild: Modular Bimanual Loco-Manipulation Capture from 360$^{\circ}$ Cameras Alone](https://arxiv.org/abs/2609.22809v1)**  
  Authors: Benjamin Yang, Weiying Wang, Shenggao Li, Keming Yan, Sasha Wilkinson, Zelin Wang, Yip Fun Yeung, Lingfeng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.22809v1.pdf)  
  Keywords: head, tracking, ar, 3d gaussian, face, localization  

### Scene Understanding

*Showing the latest 50 out of 107 papers*

- **[EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation](https://arxiv.org/abs/2609.34853v1)**  
  Authors: Sungho Moon, Kota Shimomura, Junwoo Park, Wonhyeok Choi, Seunghun Lee, Takayoshi Yamashita, Sunghoon Im  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34853v1.pdf)  
  Keywords: segmentation, ar, compact, 3d gaussian, gaussian splatting, understanding, localization  
- **[GraphWrit3R: End-to-End 3D Scene Graph Writing](https://arxiv.org/abs/2609.31595v1)**  
  Authors: Luka Milivojevic, Nikola Popovic, Sayan Deb Sarkar, Sebastian Koch, Iro Armeni, Luc Van Gool, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31595v1.pdf)  
  Keywords: semantic, ar  
- **[SplatLabel: Pseudo-Labelling through 4D Gaussian Splatting](https://arxiv.org/abs/2609.29836v1)**  
  Authors: Nitya Nanvani, Andras Palffy, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29836v1.pdf)  
  Keywords: semantic, segmentation, dynamic, tracking, ar, 4d, gaussian splatting, geometry  
- **[PlenoCI: Plenoptic CharacterIstics for View Dependence Aware Change Classification](https://arxiv.org/abs/2609.28930v1)**  
  Authors: Jason Lai, Chamuditha Jayanga Galappaththige, Niko Suenderhauf, Dimity Miller, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://js0n-lai.github.io/plenoci)  
  Keywords: ar, efficient, 3d gaussian, gaussian splatting, understanding  
- **[PePESeg3D: Perception Prior Enhances Multi-Scale Segmentation for 3D Gaussian Splatting](https://arxiv.org/abs/2609.28645v1)**  
  Authors: Sungjae Choi, Seunghee Koh, Junmo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28645v1.pdf) | [![GitHub](https://img.shields.io/github/stars/BeCow5X5/PePESeg3D?style=social)](https://github.com/BeCow5X5/PePESeg3D)  
  Keywords: nerf, semantic, segmentation, ar, lighting, 3d gaussian, gaussian splatting, geometry  
- **[ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards](https://arxiv.org/abs/2609.26315v1)**  
  Authors: Alessandro Masini, Matteo Frosi, Mirko Usuelli, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26315v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, face, gaussian splatting, fast, slam  
- **[Agentic Building-Aware Satellite Gaussian Splatting for Auditable Urban DSM Reconstruction](https://arxiv.org/abs/2609.25578v1)**  
  Authors: Wentao Sun, Zhengsen Xu, Yiping Chen, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25578v1.pdf)  
  Keywords: semantic, ar, neural rendering, face, gaussian splatting, 3d reconstruction  
- **[ZVeC: A Zero-Shot Framework for Instance-Level Vehicle Extraction and Generative Point Cloud Completion](https://arxiv.org/abs/2609.24825v1)**  
  Authors: Daisy Li, Kyle Gao, Quanyun Wu, Boris Jutzi, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24825v1.pdf)  
  Keywords: 3d gaussian, semantic, ar  
- **[Relightable 3D Avatar Reconstruction with Semantic-Adaptive Motion-Illumination Responses](https://arxiv.org/abs/2609.24158v1)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Jijie Li, Baiqin Wang, Shukai Chen, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24158v1.pdf)  
  Keywords: head, semantic, ar, lighting, relightable, 3d gaussian, animation, compact, illumination, relighting, avatar, lightweight, motion  
- **[CoRef-GS: Cooperative Referring Gaussian Splatting for Multi-Agent Scene Understanding](https://arxiv.org/abs/2609.20586v1)**  
  Authors: Zhikun Zhou, Kunyu Peng, Runyi Yang, Junhao Cai, Di Wen, Ruiping Liu, Danda Pani Paudel, Yi Zhou, Luc Van Gool, Kailun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.20586v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ruojiruoli17/CoRef-GS.git?style=social)](https://github.com/ruojiruoli17/CoRef-GS.git)  
  Keywords: understanding, gaussian splatting, semantic, ar  



## Classic Papers
- **[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)** (SIGGRAPH 2023)  
  Authors: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis  
  Code: 🔗 [GitHub](https://github.com/graphdeco-inria/gaussian-splatting)  
  Keywords: Real-time Rendering, Neural Rendering, Point-based Graphics

- **[A Study on the Use of High Dynamic Range Imaging for Gaussian Splatting Methods: Are 8 Bits Enough?](https://doi.org/10.2312/stag.20241341)** (STAG 2024)  
  Authors: Valentina Piras, Amedeo F. Bonatti, Carmelo De Maria, Paolo Cignoni, Francesco Banterle  
  Paper: 📄 [PDF](https://iris.cnr.it/bitstream/20.500.14243/513755/3/Piras-Cignoni-Banterle_STAG20241341.pdf)  
  Keywords: High Dynamic Range, HDR, Tone Mapping, 3D Gaussian Splatting, Neural Radiance Fields

- **[Instruct-4DGS: Efficient Dynamic Scene Editing via 4D Gaussian-based Static-Dynamic Separation](https://hanbyelcho.info/instruct-4dgs/)** (CVPR 2025)  
  Authors: Hanbyel Cho, Juhyeon Kwon, et al.  
  Paper: 📄 [arXiv](https://arxiv.org/abs/2502.02091)  
  Code: 🔗 [GitHub](https://github.com/juhyeon-kwon/efficient_4d_gaussian_editing)  
  Keywords: Dynamic Scene Editing, 4D Gaussian Splatting, Static-Dynamic Separation

## Open Source Projects
- [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) - Original implementation of 3D Gaussian Splatting
- [taichi-3d-gaussian-splatting](https://github.com/wanmeihuali/taichi-3d-gaussian-splatting) - 3D Gaussian Splatting implemented in Taichi

## Applications
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering Demo](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) - Online Demo

## Tutorials & Blogs
- [Introduction to 3D Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting) - Official Tutorial

## 📋 Project Features

### 🛠️ Core Features
- **Unified CLI** (`main.py`): Single entry point with `init`, `search`, `suggest`, `export-bib`, `readme` subcommands
- **Interactive Config Wizard**: Guided setup for keywords, domains, time range, and API keys via `python main.py init`
- **Custom Search Keywords**: Configure keywords for title, abstract, or both; with arXiv domain filtering (`cs.CV`, `cs.GR`, etc.)
- **Time Range Filtering**: Relative periods (`30d`, `6m`, `1y`, `2y`) or absolute date ranges (`YYYY-MM-DD` to `YYYY-MM-DD`)
- **Smart Link Extraction**: Auto-classifies URLs from abstracts into GitHub, project page, dataset, video, demo, HuggingFace links
- **BibTeX Export**: Fetch BibTeX from arXiv official API; export to `.bib` files with category and date filters
- **LLM Keyword Suggestion**: Input paper titles or arXiv IDs to auto-generate optimized search keywords via OpenAI-compatible API
- **Automated Paper Collection**: Daily automatic crawling with GitHub Actions
- **Intelligent Classification**: Auto-categorize papers into 14+ topics (Acceleration, Dynamic Scenes, SLAM, etc.)

### 🛠️ Technical Features
- **Robust Error Handling**: Multi-layer retry and fallback strategies ensure stable operation
- **GitHub Actions Integration**: Automated CI/CD workflows for daily updates
- **Multi-type Link Badges**: README entries display PDF, GitHub (with stars), Project, Dataset, Video, Demo, HuggingFace, and Citation badges
- **Detailed Logging**: Comprehensive logging for debugging and monitoring
- **Cross-Platform**: Support for Windows/Linux/macOS

### 📚 Data Output
- **Paper JSON files** (`data/papers_YYYY-MM-DD.json`): Full paper metadata with title, authors, abstract, links, keywords, BibTeX
- **BibTeX files** (`output/*.bib`): Ready-to-use bibliography files for LaTeX
- **Auto-generated README**: Categorized and formatted paper listings

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Interactive Setup (Recommended)

```bash
python main.py init
```

This wizard walks you through:
- Setting search keywords (for title, abstract, or both)
- Selecting arXiv domains (e.g., `cs.CV`, `cs.GR`, `cs.AI`)
- Configuring time range (relative like `6m`/`1y`, or absolute dates)
- Setting max results
- Optionally configuring an OpenAI-compatible API key for keyword suggestion

### 3. Search Papers

```bash
# Search with settings from user_config.json
python main.py search

# Override: fetch 200 papers from the last 6 months, include BibTeX
python main.py search --max-results 200 --recent 6m --bibtex

# Search with absolute date range
python main.py search --date-from 2024-01-01 --date-to 2025-01-01

# Include citation counts from Semantic Scholar
python main.py search --citations
```

### 4. Export BibTeX

```bash
# Export all papers from the latest data file
python main.py export-bib --output output/references.bib

# Export only "Dynamic Scene" papers
python main.py export-bib --category "Dynamic Scene" --output output/dynamic.bib

# Export papers from a specific date range
python main.py export-bib --date-from 2024-06-01 --date-to 2025-01-01 --output output/recent.bib
```

### 5. LLM Keyword Suggestion

```bash
# Generate keywords from paper titles
python main.py suggest --titles "3D Gaussian Splatting for Real-Time Rendering" "Dynamic 3D Gaussians"

# Generate from arXiv IDs (auto-fetches titles)
python main.py suggest --arxiv-ids 2308.04079 2311.12897

# Auto-write suggested keywords to config
python main.py suggest --titles "NeRF" "Gaussian Splatting" --apply

# Use a custom API endpoint (e.g., DeepSeek)
python main.py suggest --titles "Paper Title" --base-url https://api.deepseek.com/v1 --api-key sk-xxx --model deepseek-chat
```

### 6. Generate README

```bash
# Basic README
python main.py readme

# Include latest papers section and abstracts
python main.py readme --show-latest --show-abstracts
```

### Configuration File

All settings are stored in `data/user_config.json`:

```json
{
  "search": {
    "keywords": {
      "both_abstract_and_title": ["gaussian splatting", "3d gaussian"],
      "abstract_only": ["neural radiance field gaussian"],
      "title_only": ["3D scene reconstruction"]
    },
    "domains": ["cs.CV", "cs.GR"],
    "time_range": {
      "mode": "relative",
      "relative": "1y"
    },
    "max_results": 500
  },
  "api_keys": {
    "openai_api_key": "",
    "openai_base_url": "https://api.openai.com/v1",
    "openai_model": "gpt-4o-mini"
  }
}
```

## Contribution Guidelines
Feel free to submit Pull Requests to improve this list! Please follow these formats:
- Paper entry format: `**[Paper Title](link)** - Brief description`
- Project entry format: `[Project Name](link) - Project description`

## License
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) 
