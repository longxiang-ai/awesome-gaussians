# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-gaussians/)**: an interactive paper map, monthly trends, topic network and co-author network of every tracked paper.

> Last Update: 2026-11-26 05:55:01

## 📰 Latest Updates

🗺️ **[2026-09-30] Paper Atlas on GitHub Pages**
- New [interactive site](https://longxiang-ai.github.io/awesome-gaussians/) built from all daily snapshots, rebuilt after every update

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
- [Acceleration](#acceleration) (91 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (500 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (159 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (171 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (31 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (205 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (31 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (184 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (43 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (5 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (51 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (70 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (88 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Urban State Representation for Autonomous Mobility: A Survey of Multimodal Perception, Architectures, Datasets, and Benchmarks](https://arxiv.org/abs/2611.28129v1)**  
  Authors: Binay Kumar Singh, Niels Da Vitoria Lobo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.28129v1.pdf) | [![GitHub](https://img.shields.io/github/stars/binayksingh/Awesome-Urban-State-Representation?style=social)](https://github.com/binayksingh/Awesome-Urban-State-Representation)  
  Keywords: survey, 3d gaussian, head, autonomous driving, ar  
- **[Spectro-Spatial Survey Fusion](https://arxiv.org/abs/2611.21798v1)**  
  Authors: Georgios N. Vassilakis, Miles Cranmer, Vasily Belokurov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.21798v1.pdf)  
  Keywords: survey, ar, face, gaussian splatting  
- **[Gaussian Splatting for Real-Time Scene Reconstruction: Methods, Systems, and Trade-offs](https://arxiv.org/abs/2610.17513v1)**  
  Authors: Ashim Dahal, Rabab Abdelfattah, Nick Rahimi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17513v1.pdf)  
  Keywords: real-time rendering, survey, slam, gaussian splatting, 3d gaussian, compression, tracking, ar, sparse-view, dynamic, mapping, localization  
- **[OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones](https://arxiv.org/abs/2609.24253v1)**  
  Authors: Zhongrui You, Zhen Li, Junli Liu, Zhigang Wang, Bin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24253v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://openflyscan.github.io)  
  Keywords: survey, gaussian splatting, 3d gaussian, face, ar, high-fidelity  
- **[Quality Assessment of 3D Gaussian Splatting: Distortions, Benchmarks, and Open Challenges](https://arxiv.org/abs/2609.23027v1)**  
  Authors: Shuai Liu, Binqiang Liu, Qingyu Mao, Jiacong Chen, Yongsheng Liang, Youneng Bao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23027v1.pdf)  
  Keywords: survey, gaussian splatting, 3d gaussian, compression, ar  

### Acceleration

*Showing the latest 50 out of 91 papers*

- **[A Mesh for Every Moment](https://arxiv.org/abs/2611.34939v1)**  
  Authors: Roy Or-El, Jeong Joon Park, Ira Kemelmacher-Shlizerman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34939v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://memo-4d.github.io)  
  Keywords: gaussian splatting, geometry, 4d, motion, face, ar, dynamic, fast  
- **[WorldExpand: Building Coherent 3D Worlds via Sparse Joint Panoramic Expansion](https://arxiv.org/abs/2611.34810v1)**  
  Authors: Yuyang Yin, Chenjie Cao, Xuhui Zuo, Yuning Gong, Pengfei Wang, Junta Wu, Zhenwei Wang, Yao Zhao, Tengfei Wang, Yunchao Wei, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34810v1.pdf)  
  Keywords: ar, fast, 3d reconstruction  
- **[Feed-Forward Adaptive Gaussian Splatting for Interactive Medical Volume Rendering](https://arxiv.org/abs/2611.34478v1)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Chaoyi Zhou, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34478v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/renderfmnext)  
  Keywords: lighting, gaussian splatting, medical, head, face, ar, fast  
- **[UPP-Gauss: Ultrasound Propagation Physics-informed Gaussian Splatting for B-mode Novel-View Synthesis](https://arxiv.org/abs/2611.33920v1)**  
  Authors: Guil Jung, Seok-Hwan Oh, Myeong-Gee Kim, Young-Min Kim, Hyeon-Jik Lee, Sang-Yun Kim, Hyeok-Jun Kwon, Hyuk-Sool Kwon, Hyeon-Min Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33920v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient rendering, efficient, ar  
- **[SprintGS: Eliminating Redundancy for Fast 3D Gaussian Splatting Training](https://arxiv.org/abs/2611.33796v1)**  
  Authors: Ryosuke Watanabe, Tomoaki Konno  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33796v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, face, ar, sparse-view, dynamic, fast, compact  
- **[SplatWAM: Splatting World Action Models for Real-Time 3D Imagination](https://arxiv.org/abs/2611.33467v1)**  
  Authors: Frank Tsu-Fang Lu, Karthik Sundar Senthilkumar, Christopher Thirgood, Oscar Mendez, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33467v1.pdf)  
  Keywords: 3d gaussian, head, ar, lightweight, dynamic, fast, compact  
- **[FOCI: Trajectory Optimization on Gaussian Splats for Gaussian Robots](https://arxiv.org/abs/2611.33380v1)**  
  Authors: Mario Gomez Andreu, Carlos Martinez Cuenca, Maximum Wilder-Smith, Victor Klemm, Vaishakh Patil, Marco Hutter, Jesus Tordesillas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33380v1.pdf) | [![GitHub](https://img.shields.io/github/stars/leggedrobotics/foci?style=social)](https://github.com/leggedrobotics/foci)  
  Keywords: nerf, 3d reconstruction, robotics, gaussian splatting, 3d gaussian, ar, dynamic, fast  
- **[VersionGS: Compact and Motion-Robust Dynamic Gaussian Splatting via Versioned Gaussians](https://arxiv.org/abs/2611.33374v1)**  
  Authors: Shihang Wei, Yichi Zhang, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33374v1.pdf)  
  Keywords: gaussian splatting, motion, ar, dynamic, fast, compact  
- **[AnyPrune: Optimization-Free Pruning for Any Feedforward 3D Gaussian Splatting Pipeline](https://arxiv.org/abs/2611.32735v1)**  
  Authors: Nicola Leonetti, Federico Stella, Aoxiang Fan, Saqib Javed, Pascal Fua, Luigi Di Stefano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32735v1.pdf)  
  Keywords: 3d gaussian, ar, fast, gaussian splatting  
- **[Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation](https://arxiv.org/abs/2611.32718v1)**  
  Authors: Itai Mizlish, Boaz Ben-Moshe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32718v1.pdf) | [![GitHub](https://img.shields.io/github/stars/itaim18/DANIEL?style=social)](https://github.com/itaim18/DANIEL)  
  Keywords: slam, mapping, outdoor, ar, fast  

### Applications

*Showing the latest 50 out of 500 papers*

- **[A Mesh for Every Moment](https://arxiv.org/abs/2611.34939v1)**  
  Authors: Roy Or-El, Jeong Joon Park, Ira Kemelmacher-Shlizerman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34939v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://memo-4d.github.io)  
  Keywords: gaussian splatting, geometry, 4d, motion, face, ar, dynamic, fast  
- **[MERLoc: Robust Robot Localization in Dynamic Environments with Pose-Based Retrieval over 3D Gaussian Splatting References](https://arxiv.org/abs/2611.34932v1)**  
  Authors: Michael Baumgartner, Dario Mylonopoulos, Sammy Christen, Markus Gross, Moritz Bacher  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34932v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, motion, ar, dynamic, localization  
- **[WorldExpand: Building Coherent 3D Worlds via Sparse Joint Panoramic Expansion](https://arxiv.org/abs/2611.34810v1)**  
  Authors: Yuyang Yin, Chenjie Cao, Xuhui Zuo, Yuning Gong, Pengfei Wang, Junta Wu, Zhenwei Wang, Yao Zhao, Tengfei Wang, Yunchao Wei, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34810v1.pdf)  
  Keywords: ar, fast, 3d reconstruction  
- **[Neural Rendering Compiler: Generative Video Models as Programmable Renderers](https://arxiv.org/abs/2611.34680v1)**  
  Authors: Yuxia Zhu, Xinglong Xu, Hao Liang, Linzhuang Sun, Caijun Jia, Qifeng Cai, Jincen Luo, Lei Li, Alden Cai, Asher Qin, Wentao Zhang, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34680v1.pdf)  
  Keywords: lighting, neural rendering, semantic, face, ar  
- **[Feed-Forward Adaptive Gaussian Splatting for Interactive Medical Volume Rendering](https://arxiv.org/abs/2611.34478v1)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Chaoyi Zhou, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34478v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/renderfmnext)  
  Keywords: lighting, gaussian splatting, medical, head, face, ar, fast  
- **[AnyCam4D: Ray-Based 4D Gaussian Rendering for Arbitrary Camera Models](https://arxiv.org/abs/2611.34223v1)**  
  Authors: Sascha Kirch, Rafael Pagés, Jan Ondřej, Clara Pérez-Molina, Sergio Martin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34223v1.pdf)  
  Keywords: gaussian splatting, 4d, motion, ar, dynamic  
- **[OceanFix: Reference-Guided Diffusion for Sparse-View Underwater 3D Reconstruction](https://arxiv.org/abs/2611.34155v1)**  
  Authors: Gen Li, Maoxin Chen, Yao Xiao, Xinyang Li, Yu Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34155v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, efficient, sparse-view, ar  
- **[UPP-Gauss: Ultrasound Propagation Physics-informed Gaussian Splatting for B-mode Novel-View Synthesis](https://arxiv.org/abs/2611.33920v1)**  
  Authors: Guil Jung, Seok-Hwan Oh, Myeong-Gee Kim, Young-Min Kim, Hyeon-Jik Lee, Sang-Yun Kim, Hyeok-Jun Kwon, Hyuk-Sool Kwon, Hyeon-Min Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33920v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient rendering, efficient, ar  
- **[Tortho-Gaussian++: Suppressing Geometric Drift and Floaters for Robust Gravity-Aligned TDOM Generation in Large-Scale Aerial Scenes](https://arxiv.org/abs/2611.33905v1)**  
  Authors: Xiang Wang, Xin Wang, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33905v1.pdf)  
  Keywords: 3d gaussian, ar, vr, gaussian splatting  
- **[Revisiting Monocular In-Hand Object Scanning: Dataset, Pose Estimation, and Surface Reconstruction](https://arxiv.org/abs/2611.33824v1)**  
  Authors: Di Wu, Jeeeun Kim, Shu Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33824v1.pdf)  
  Keywords: gaussian splatting, motion, face, ar, dynamic, high-fidelity  

### Avatar Generation

*Showing the latest 50 out of 159 papers*

- **[A Mesh for Every Moment](https://arxiv.org/abs/2611.34939v1)**  
  Authors: Roy Or-El, Jeong Joon Park, Ira Kemelmacher-Shlizerman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34939v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://memo-4d.github.io)  
  Keywords: gaussian splatting, geometry, 4d, motion, face, ar, dynamic, fast  
- **[Neural Rendering Compiler: Generative Video Models as Programmable Renderers](https://arxiv.org/abs/2611.34680v1)**  
  Authors: Yuxia Zhu, Xinglong Xu, Hao Liang, Linzhuang Sun, Caijun Jia, Qifeng Cai, Jincen Luo, Lei Li, Alden Cai, Asher Qin, Wentao Zhang, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34680v1.pdf)  
  Keywords: lighting, neural rendering, semantic, face, ar  
- **[Feed-Forward Adaptive Gaussian Splatting for Interactive Medical Volume Rendering](https://arxiv.org/abs/2611.34478v1)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Chaoyi Zhou, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34478v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/renderfmnext)  
  Keywords: lighting, gaussian splatting, medical, head, face, ar, fast  
- **[Revisiting Monocular In-Hand Object Scanning: Dataset, Pose Estimation, and Surface Reconstruction](https://arxiv.org/abs/2611.33824v1)**  
  Authors: Di Wu, Jeeeun Kim, Shu Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33824v1.pdf)  
  Keywords: gaussian splatting, motion, face, ar, dynamic, high-fidelity  
- **[SprintGS: Eliminating Redundancy for Fast 3D Gaussian Splatting Training](https://arxiv.org/abs/2611.33796v1)**  
  Authors: Ryosuke Watanabe, Tomoaki Konno  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33796v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, face, ar, sparse-view, dynamic, fast, compact  
- **[Efficient Scene-Distribution-Aware Second-Order Optimization for 3D Gaussian Splatting](https://arxiv.org/abs/2611.33698v1)**  
  Authors: Hyunseung Son, Young Sun Choi, Youngsik Yun, Kibeom Hong, Youngjung Uh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33698v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, head, efficient, ar  
- **[SplatWAM: Splatting World Action Models for Real-Time 3D Imagination](https://arxiv.org/abs/2611.33467v1)**  
  Authors: Frank Tsu-Fang Lu, Karthik Sundar Senthilkumar, Christopher Thirgood, Oscar Mendez, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33467v1.pdf)  
  Keywords: 3d gaussian, head, ar, lightweight, dynamic, fast, compact  
- **[First-Hit Photoconsistency for Neural Surface Reconstruction](https://arxiv.org/abs/2611.32998v1)**  
  Authors: Gabriel Lenain, Edmond Boyer, Jean Ponce  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32998v1.pdf)  
  Keywords: gaussian splatting, geometry, efficient, face, ar  
- **[GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM](https://arxiv.org/abs/2611.32335v2)**  
  Authors: Weicong Zhang, Yuan Huang, Yu Zheng, Lin Chenxiao, Yingying Li, Lilong Fan, Liangdong Zhuang, Yufan Chen, Ruiping Liu, Junwei Zheng, Jiaming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32335v2.pdf)  
  Keywords: slam, gaussian splatting, geometry, tracking, face, ar, dynamic, mapping  
- **[View Management with Gaussian Placement and Opacity Regularization for Online 3DGS](https://arxiv.org/abs/2611.32025v1)**  
  Authors: Dong Hwi Kim, Park Sangwon, Chaehyeon Song, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32025v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, geometry, face, ar, mapping, localization  

### Dynamic Scene

*Showing the latest 50 out of 171 papers*

- **[A Mesh for Every Moment](https://arxiv.org/abs/2611.34939v1)**  
  Authors: Roy Or-El, Jeong Joon Park, Ira Kemelmacher-Shlizerman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34939v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://memo-4d.github.io)  
  Keywords: gaussian splatting, geometry, 4d, motion, face, ar, dynamic, fast  
- **[MERLoc: Robust Robot Localization in Dynamic Environments with Pose-Based Retrieval over 3D Gaussian Splatting References](https://arxiv.org/abs/2611.34932v1)**  
  Authors: Michael Baumgartner, Dario Mylonopoulos, Sammy Christen, Markus Gross, Moritz Bacher  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34932v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, motion, ar, dynamic, localization  
- **[AnyCam4D: Ray-Based 4D Gaussian Rendering for Arbitrary Camera Models](https://arxiv.org/abs/2611.34223v1)**  
  Authors: Sascha Kirch, Rafael Pagés, Jan Ondřej, Clara Pérez-Molina, Sergio Martin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34223v1.pdf)  
  Keywords: gaussian splatting, 4d, motion, ar, dynamic  
- **[Revisiting Monocular In-Hand Object Scanning: Dataset, Pose Estimation, and Surface Reconstruction](https://arxiv.org/abs/2611.33824v1)**  
  Authors: Di Wu, Jeeeun Kim, Shu Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33824v1.pdf)  
  Keywords: gaussian splatting, motion, face, ar, dynamic, high-fidelity  
- **[SprintGS: Eliminating Redundancy for Fast 3D Gaussian Splatting Training](https://arxiv.org/abs/2611.33796v1)**  
  Authors: Ryosuke Watanabe, Tomoaki Konno  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33796v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, face, ar, sparse-view, dynamic, fast, compact  
- **[SplatWAM: Splatting World Action Models for Real-Time 3D Imagination](https://arxiv.org/abs/2611.33467v1)**  
  Authors: Frank Tsu-Fang Lu, Karthik Sundar Senthilkumar, Christopher Thirgood, Oscar Mendez, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33467v1.pdf)  
  Keywords: 3d gaussian, head, ar, lightweight, dynamic, fast, compact  
- **[FOCI: Trajectory Optimization on Gaussian Splats for Gaussian Robots](https://arxiv.org/abs/2611.33380v1)**  
  Authors: Mario Gomez Andreu, Carlos Martinez Cuenca, Maximum Wilder-Smith, Victor Klemm, Vaishakh Patil, Marco Hutter, Jesus Tordesillas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33380v1.pdf) | [![GitHub](https://img.shields.io/github/stars/leggedrobotics/foci?style=social)](https://github.com/leggedrobotics/foci)  
  Keywords: nerf, 3d reconstruction, robotics, gaussian splatting, 3d gaussian, ar, dynamic, fast  
- **[VersionGS: Compact and Motion-Robust Dynamic Gaussian Splatting via Versioned Gaussians](https://arxiv.org/abs/2611.33374v1)**  
  Authors: Shihang Wei, Yichi Zhang, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33374v1.pdf)  
  Keywords: gaussian splatting, motion, ar, dynamic, fast, compact  
- **[NRG-Twins: Pixel-Level Ground Truth for Rigidity Violations in Generated Videos](https://arxiv.org/abs/2611.32431v1)**  
  Authors: Chenrui Fan, Qiyang Hu, Luca Scharr, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32431v1.pdf)  
  Keywords: segmentation, ar, motion, 3d reconstruction  
- **[GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM](https://arxiv.org/abs/2611.32335v2)**  
  Authors: Weicong Zhang, Yuan Huang, Yu Zheng, Lin Chenxiao, Yingying Li, Lilong Fan, Liangdong Zhuang, Yufan Chen, Ruiping Liu, Junwei Zheng, Jiaming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32335v2.pdf)  
  Keywords: slam, gaussian splatting, geometry, tracking, face, ar, dynamic, mapping  

### Few-shot

- **[OceanFix: Reference-Guided Diffusion for Sparse-View Underwater 3D Reconstruction](https://arxiv.org/abs/2611.34155v1)**  
  Authors: Gen Li, Maoxin Chen, Yao Xiao, Xinyang Li, Yu Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34155v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, efficient, sparse-view, ar  
- **[SprintGS: Eliminating Redundancy for Fast 3D Gaussian Splatting Training](https://arxiv.org/abs/2611.33796v1)**  
  Authors: Ryosuke Watanabe, Tomoaki Konno  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33796v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, face, ar, sparse-view, dynamic, fast, compact  
- **[Enhancing Sparse-View Gaussian Splatting with Feed-Forward Priors via Spectral Fusion and Distillation](https://arxiv.org/abs/2611.31428v1)**  
  Authors: Weikai Lin, Jun Dai, Sheng Zhao, Junjie Zhao, Yuhao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31428v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://linwk20.github.io/spectral-fusion-gs)  
  Keywords: sparse-view, ar, gaussian splatting  
- **[Not All Directions Are Flat: Decomposed-Gradient Flatness for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2611.28802v1)**  
  Authors: Ungbae Yoon, Kwanyoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.28802v1.pdf)  
  Keywords: robotics, gaussian splatting, 3d gaussian, sparse view, sparse-view, ar  
- **[Stage-wise Lineage-aware Dropout for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2611.17752v1)**  
  Authors: Yan Xing, Zhi Chen, Fanglue Zhang, Junhong Zhao, Bing Xue, Mengjie Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.17752v1.pdf)  
  Keywords: nerf, gaussian splatting, 3d gaussian, geometry, sparse-view, ar  
- **[ThermalSplat: Generalizable Pose-Free Gaussian Splatting for Sparse-View Thermal 3D Reconstruction](https://arxiv.org/abs/2611.15435v1)**  
  Authors: Prasanna S, Gopi Raju Matta, Divya Madhuri Vemunuri, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.15435v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, efficient, sparse-view, ar  
- **[A Reproducible Reconstruction and Evaluation Framework for Photorealistic Lunar Analog Scene Reconstruction Toward Digital Twins](https://arxiv.org/abs/2611.00870v1)**  
  Authors: Antar Mazumder, Ryan Hartzell, Luke Boyd, Alexander Robinson, Neha Sharma, Chance Carnival, Frances Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00870v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rose-lab-admin.github.io/rose-lunar-dt-rec)  
  Keywords: gaussian splatting, 3d gaussian, geometry, motion, human, sparse view, ar  
- **[P^2-Gaussian: Prior-Driven and Projection-Guided Gaussian Splatting for Sparse-View Cone-Beam CT Reconstruction](https://arxiv.org/abs/2610.39359v1)**  
  Authors: Jinqiu Xia, Jianhui Ma, Bin Ouyang, Xiaoyan Huang, Yuan Xu, Zun Piao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39359v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ballbo5354/P-2-Gaussian?style=social)](https://github.com/Ballbo5354/P-2-Gaussian)  
  Keywords: gaussian splatting, 3d gaussian, sparse-view, ar, compact  
- **[DUET4D: Self-Corrective Coupled Guidance for Sparse-View 4D Reconstruction](https://arxiv.org/abs/2610.35002v1)**  
  Authors: Beizhen Zhao, Nanjie Yao, Boyi Fu, Qingsong Yan, Haofan Ren, Kaiyong Zhao, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35002v1.pdf)  
  Keywords: sparse-view, 4d, ar, gaussian splatting  
- **[PixGR: Pixel-Space Generative Decoding for Fast Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2610.31908v1)**  
  Authors: Ranran Huang, Wenjing Bian, Weixun Luo, Ye Mao, Krystian Mikolajczyk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.31908v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ranrhuang.github.io/pixgr)  
  Keywords: 3d reconstruction, 3d gaussian, compression, efficient, lightweight, sparse-view, ar, fast  

### Geometry Reconstruction

*Showing the latest 50 out of 205 papers*

- **[A Mesh for Every Moment](https://arxiv.org/abs/2611.34939v1)**  
  Authors: Roy Or-El, Jeong Joon Park, Ira Kemelmacher-Shlizerman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34939v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://memo-4d.github.io)  
  Keywords: gaussian splatting, geometry, 4d, motion, face, ar, dynamic, fast  
- **[WorldExpand: Building Coherent 3D Worlds via Sparse Joint Panoramic Expansion](https://arxiv.org/abs/2611.34810v1)**  
  Authors: Yuyang Yin, Chenjie Cao, Xuhui Zuo, Yuning Gong, Pengfei Wang, Junta Wu, Zhenwei Wang, Yao Zhao, Tengfei Wang, Yunchao Wei, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34810v1.pdf)  
  Keywords: ar, fast, 3d reconstruction  
- **[OceanFix: Reference-Guided Diffusion for Sparse-View Underwater 3D Reconstruction](https://arxiv.org/abs/2611.34155v1)**  
  Authors: Gen Li, Maoxin Chen, Yao Xiao, Xinyang Li, Yu Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34155v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, efficient, sparse-view, ar  
- **[FOCI: Trajectory Optimization on Gaussian Splats for Gaussian Robots](https://arxiv.org/abs/2611.33380v1)**  
  Authors: Mario Gomez Andreu, Carlos Martinez Cuenca, Maximum Wilder-Smith, Victor Klemm, Vaishakh Patil, Marco Hutter, Jesus Tordesillas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33380v1.pdf) | [![GitHub](https://img.shields.io/github/stars/leggedrobotics/foci?style=social)](https://github.com/leggedrobotics/foci)  
  Keywords: nerf, 3d reconstruction, robotics, gaussian splatting, 3d gaussian, ar, dynamic, fast  
- **[First-Hit Photoconsistency for Neural Surface Reconstruction](https://arxiv.org/abs/2611.32998v1)**  
  Authors: Gabriel Lenain, Edmond Boyer, Jean Ponce  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32998v1.pdf)  
  Keywords: gaussian splatting, geometry, efficient, face, ar  
- **[Completion-Aware Compression for Progressive 3D Gaussian Splatting](https://arxiv.org/abs/2611.32628v1)**  
  Authors: Reagan Koo, Yeong-Gyu Kim, Eun-Seok Ryu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32628v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, 3d gaussian, compression, large scene, ar, compact  
- **[NRG-Twins: Pixel-Level Ground Truth for Rigidity Violations in Generated Videos](https://arxiv.org/abs/2611.32431v1)**  
  Authors: Chenrui Fan, Qiyang Hu, Luca Scharr, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32431v1.pdf)  
  Keywords: segmentation, ar, motion, 3d reconstruction  
- **[GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM](https://arxiv.org/abs/2611.32335v2)**  
  Authors: Weicong Zhang, Yuan Huang, Yu Zheng, Lin Chenxiao, Yingying Li, Lilong Fan, Liangdong Zhuang, Yufan Chen, Ruiping Liu, Junwei Zheng, Jiaming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32335v2.pdf)  
  Keywords: slam, gaussian splatting, geometry, tracking, face, ar, dynamic, mapping  
- **[View Management with Gaussian Placement and Opacity Regularization for Online 3DGS](https://arxiv.org/abs/2611.32025v1)**  
  Authors: Dong Hwi Kim, Park Sangwon, Chaehyeon Song, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32025v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, geometry, face, ar, mapping, localization  
- **[BendGS: Observation-Conditioned Gaussian Self-Modeling for Continuum Robots](https://arxiv.org/abs/2611.31844v1)**  
  Authors: Jeong Woon Lee, Doungjun Kim, Namho Kim, Seungheon Chae, Jongwoo Kim, Hyoseok Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31844v1.pdf)  
  Keywords: body, 3d gaussian, geometry, deformation, ar  

### Large Scene

- **[Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](https://arxiv.org/abs/2611.33145v1)**  
  Authors: Zehan Zheng, Yanyuan Chen, Deming Li, Yutao Tang, Jianwen Xie, Alan Yuille, Jieneng Chen, Cheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33145v1.pdf)  
  Keywords: semantic, gaussian splatting, 3d gaussian, outdoor, ar, localization  
- **[Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation](https://arxiv.org/abs/2611.32718v1)**  
  Authors: Itai Mizlish, Boaz Ben-Moshe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32718v1.pdf) | [![GitHub](https://img.shields.io/github/stars/itaim18/DANIEL?style=social)](https://github.com/itaim18/DANIEL)  
  Keywords: slam, mapping, outdoor, ar, fast  
- **[Completion-Aware Compression for Progressive 3D Gaussian Splatting](https://arxiv.org/abs/2611.32628v1)**  
  Authors: Reagan Koo, Yeong-Gyu Kim, Eun-Seok Ryu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32628v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, 3d gaussian, compression, large scene, ar, compact  
- **[Mitigating SM-Level Load Imbalance in 3D Gaussian Splatting on GPUs](https://arxiv.org/abs/2611.12319v1)**  
  Authors: Junha Ryu, Hoi-Jun Yoo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.12319v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, 3d gaussian, autonomous driving, lightweight, ar, urban scene  
- **[PLS-GS: Probabilistic Lidar Scaffolds for Compact, Surface-Aligned Gaussian Splatting](https://arxiv.org/abs/2611.10699v1)**  
  Authors: Krishnan Harikumar, Alejandro Fontan, Thierry Peynot, Emili Hernández, Niko Sünderhauf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.10699v1.pdf) | [![GitHub](https://img.shields.io/github/stars/k-harikumar/PLS-GS?style=social)](https://github.com/k-harikumar/PLS-GS)  
  Keywords: robotics, gaussian splatting, 3d gaussian, mapping, outdoor, face, ar, fast, compact  
- **[IGSW: Multi-Weather Urban Scene Reconstruction with Intrinsic-Decoupled Gaussian Splatting](https://arxiv.org/abs/2611.04374v1)**  
  Authors: Zhongquan Wang, Long Cao, Peijia Xie, Senlei Ma, Jie Li, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04374v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://akaxi6.github.io/IGSW)  
  Keywords: semantic, gaussian splatting, 4d, autonomous driving, ar, dynamic, urban scene, high-fidelity, illumination  
- **[DomeGS: Perceptually Consistent Background Completion for Unbounded 3D Gaussian Splatting in Virtual Reality](https://arxiv.org/abs/2610.37172v1)**  
  Authors: Anastasiya Pechko, Agata Szymańska, Piotr Borycki, Joanna Szelewska, Michał Mnich, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37172v1.pdf)  
  Keywords: vr, gaussian splatting, 3d gaussian, geometry, outdoor, ar, high-fidelity  
- **[D4GS: Efficient Gaussian Splatting SLAM with Depth Priors](https://arxiv.org/abs/2610.36853v2)**  
  Authors: Da Li, Yihan Zang, Ivan Viola, Zeyu Wang, Dominik Engel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36853v2.pdf)  
  Keywords: slam, gaussian splatting, efficient, tracking, outdoor, ar, fast  
- **[SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation](https://arxiv.org/abs/2610.36312v1)**  
  Authors: Ziang Guo, Didar Seyidov, Yixiao Zhou, Xuefeng Zhang, Ali Alridha Abdulkarim, Chen Min, Zufeng Zhang, Dzmitry Tsetserukou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36312v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, geometry, motion, tracking, outdoor, ar, mapping  
- **[BoundedGS: Memory-Efficient High-Resolution Training for 3D Gaussian Splatting](https://arxiv.org/abs/2610.34233v1)**  
  Authors: Xiaobin Deng, Changyu Diao, Min Li, Duanqing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34233v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiaobin2001.github.io/BoundedGS-Web)  
  Keywords: gaussian splatting, 3d gaussian, efficient, outdoor, ar, compact  

### Model Compression

*Showing the latest 50 out of 184 papers*

- **[OceanFix: Reference-Guided Diffusion for Sparse-View Underwater 3D Reconstruction](https://arxiv.org/abs/2611.34155v1)**  
  Authors: Gen Li, Maoxin Chen, Yao Xiao, Xinyang Li, Yu Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34155v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, efficient, sparse-view, ar  
- **[UPP-Gauss: Ultrasound Propagation Physics-informed Gaussian Splatting for B-mode Novel-View Synthesis](https://arxiv.org/abs/2611.33920v1)**  
  Authors: Guil Jung, Seok-Hwan Oh, Myeong-Gee Kim, Young-Min Kim, Hyeon-Jik Lee, Sang-Yun Kim, Hyeok-Jun Kwon, Hyuk-Sool Kwon, Hyeon-Min Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33920v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient rendering, efficient, ar  
- **[SprintGS: Eliminating Redundancy for Fast 3D Gaussian Splatting Training](https://arxiv.org/abs/2611.33796v1)**  
  Authors: Ryosuke Watanabe, Tomoaki Konno  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33796v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, face, ar, sparse-view, dynamic, fast, compact  
- **[Efficient Scene-Distribution-Aware Second-Order Optimization for 3D Gaussian Splatting](https://arxiv.org/abs/2611.33698v1)**  
  Authors: Hyunseung Son, Young Sun Choi, Youngsik Yun, Kibeom Hong, Youngjung Uh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33698v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, head, efficient, ar  
- **[SplatWAM: Splatting World Action Models for Real-Time 3D Imagination](https://arxiv.org/abs/2611.33467v1)**  
  Authors: Frank Tsu-Fang Lu, Karthik Sundar Senthilkumar, Christopher Thirgood, Oscar Mendez, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33467v1.pdf)  
  Keywords: 3d gaussian, head, ar, lightweight, dynamic, fast, compact  
- **[VersionGS: Compact and Motion-Robust Dynamic Gaussian Splatting via Versioned Gaussians](https://arxiv.org/abs/2611.33374v1)**  
  Authors: Shihang Wei, Yichi Zhang, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33374v1.pdf)  
  Keywords: gaussian splatting, motion, ar, dynamic, fast, compact  
- **[First-Hit Photoconsistency for Neural Surface Reconstruction](https://arxiv.org/abs/2611.32998v1)**  
  Authors: Gabriel Lenain, Edmond Boyer, Jean Ponce  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32998v1.pdf)  
  Keywords: gaussian splatting, geometry, efficient, face, ar  
- **[Completion-Aware Compression for Progressive 3D Gaussian Splatting](https://arxiv.org/abs/2611.32628v1)**  
  Authors: Reagan Koo, Yeong-Gyu Kim, Eun-Seok Ryu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32628v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, 3d gaussian, compression, large scene, ar, compact  
- **[SplatTok: Data-Driven Compression of 3D Gaussian Splats with Scene-Level Tokens](https://arxiv.org/abs/2611.32202v1)**  
  Authors: Sai Karthikey Pentapati, Shashank Nelamangala Sridhara, Birendra Kathariya, Peng Yin, Guandao Yang, Alan C. Bovik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32202v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, compression, ar, compact  
- **[InterGS+: Inter-Frame Gaussian Splatting Compression with Geometry-Aware Transformer Prediction and Adaptive Residual Coding](https://arxiv.org/abs/2611.31482v1)**  
  Authors: Muhammad Talha, Zhu Li, Joel Jung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31482v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, compression, geometry, efficient, ar, lightweight, dynamic  

### Quality Enhancement

- **[Revisiting Monocular In-Hand Object Scanning: Dataset, Pose Estimation, and Surface Reconstruction](https://arxiv.org/abs/2611.33824v1)**  
  Authors: Di Wu, Jeeeun Kim, Shu Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33824v1.pdf)  
  Keywords: gaussian splatting, motion, face, ar, dynamic, high-fidelity  
- **[SemGuard: Semantics-Decoupled Watermarking for Gaussian Splatting](https://arxiv.org/abs/2611.28636v1)**  
  Authors: Yingying Shi, Zhong Zhou, Bin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.28636v1.pdf)  
  Keywords: semantic, gaussian splatting, efficient, ar, dynamic, high-fidelity  
- **[DOOM-GS: Dynamic Out-of-core Optimization for Massive Gaussian Splatting](https://arxiv.org/abs/2611.22805v1)**  
  Authors: Doğa Yılmaz, Jialin Zhu, Binglun Wang, He Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.22805v1.pdf)  
  Keywords: dynamic, high quality, gaussian splatting, ar, fast  
- **[RF3DGS: Reflection-Free 3D Gaussian Splatting with Self-Priors](https://arxiv.org/abs/2611.13772v2)**  
  Authors: Qiang Wen, Guotao Meng, Junhong Ruan, Hongyu Liu, Chenyang Lei, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.13772v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, reflection, ar, high-fidelity  
- **[Plant Orbiter: 3D Plant Reconstruction and Generation with Video Diffusion Orbit Cameras and 3D Gaussian Splatting](https://arxiv.org/abs/2611.12739v1)**  
  Authors: Zane K. J. Hartley, Yong En Kok, Lewis A. G. Stuart, Andrew P. French, Michael P. Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.12739v1.pdf)  
  Keywords: 3d gaussian, ar, high quality, gaussian splatting  
- **[URL-Sim: Unified and Regulated LiDAR Simulation for High-Fidelity Reconstruction of Dynamic Driving Scenes](https://arxiv.org/abs/2611.12932v1)**  
  Authors: Kefei Qian, Xipeng Feng, Jie Li, Long Cao, Yuhan Chen, Xiangfei Huang, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.12932v1.pdf)  
  Keywords: nerf, gaussian splatting, 3d gaussian, geometry, autonomous driving, ar, dynamic, high-fidelity  
- **[Perception Over Geometry: Rethinking Gaussian Allocation in Mesh-based Splatting](https://arxiv.org/abs/2611.07979v1)**  
  Authors: Yuting Wang, Yang Zhao, Shanding Diao, Penglin Wang, Yuan Chen, Wei Jia, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07979v1.pdf)  
  Keywords: high quality, gaussian splatting, 3d gaussian, geometry, deformation, face, ar, compact  
- **[Wide View Synthesis from Overlapping Perspective Cameras in Autonomous Driving](https://arxiv.org/abs/2611.07081v1)**  
  Authors: Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07081v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, autonomous driving, ar, high-fidelity  
- **[IGSW: Multi-Weather Urban Scene Reconstruction with Intrinsic-Decoupled Gaussian Splatting](https://arxiv.org/abs/2611.04374v1)**  
  Authors: Zhongquan Wang, Long Cao, Peijia Xie, Senlei Ma, Jie Li, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04374v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://akaxi6.github.io/IGSW)  
  Keywords: semantic, gaussian splatting, 4d, autonomous driving, ar, dynamic, urban scene, high-fidelity, illumination  
- **[EndoS3:Endoscopic Semantic Splatting SLAM](https://arxiv.org/abs/2611.04358v1)**  
  Authors: Mona Sheikh Zeinoddin, Benjamin Wright, Zafer Tandogdu, Greg Shaw, Evangelos Mazomenos, Danail Stoyanov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04358v1.pdf)  
  Keywords: understanding, semantic, slam, gaussian splatting, motion, tracking, deformation, ar, dynamic, mapping, high-fidelity  

### Ray Tracing

- **[Neural Render Proxies for Interactive and Differentiable Lighting](https://arxiv.org/abs/2611.17185v1)**  
  Authors: Sergio Sancho, Alexander Rath, Marco Manzi, Pascal Chang, Amit H. Bermano, Derek Nowrouzezahrai, Markus Gross, Marios Papas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.17185v1.pdf)  
  Keywords: path tracing, light transport, lighting, animation, relighting, efficient, lightweight, ar, fast, global illumination, illumination  
- **[FastGRT: Accelerating Training of 3D Gaussian Ray Tracing](https://arxiv.org/abs/2611.11586v1)**  
  Authors: Meet Banthia, Xiaoteng Liu, Hexu Zhao, Aurojit Panda, Jinyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.11586v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ray tracing, ar, fast  
- **[GraftRay: Physically Based Mesh Insertion into Gaussian Splatting Scenes via Path Tracing](https://arxiv.org/abs/2610.37036v3)**  
  Authors: Jinxin Ai, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37036v3.pdf)  
  Keywords: path tracing, lighting, gaussian splatting, 3d gaussian, reflection, ar, shadow  
- **[Spatial MIMO Channel Rendering: A 3D Gaussian Splatting Approach](https://arxiv.org/abs/2610.36880v1)**  
  Authors: Juntaek Han, Geonha Kim, Chaozheng Wen, Ahmed Alkhateeb, Jun Zhang, Jeonghun Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36880v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, head, ray tracing, ar, fast  
- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: lighting, gaussian splatting, 3d gaussian, head, ray tracing, efficient, ar  

### Relighting

*Showing the latest 50 out of 51 papers*

- **[Neural Rendering Compiler: Generative Video Models as Programmable Renderers](https://arxiv.org/abs/2611.34680v1)**  
  Authors: Yuxia Zhu, Xinglong Xu, Hao Liang, Linzhuang Sun, Caijun Jia, Qifeng Cai, Jincen Luo, Lei Li, Alden Cai, Asher Qin, Wentao Zhang, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34680v1.pdf)  
  Keywords: lighting, neural rendering, semantic, face, ar  
- **[Feed-Forward Adaptive Gaussian Splatting for Interactive Medical Volume Rendering](https://arxiv.org/abs/2611.34478v1)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Chaoyi Zhou, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34478v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/renderfmnext)  
  Keywords: lighting, gaussian splatting, medical, head, face, ar, fast  
- **[WildAnySplat: Feed-Forward 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2611.31023v1)**  
  Authors: Richard Shaw, Arthur Moreau, Athanasios Papaioannou, Thomas Tanay, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31023v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, head, ar, fast, illumination  
- **[NNS-GS: Non-Local Neural Scattering for Relightable Gaussian Splatting](https://arxiv.org/abs/2611.30351v1)**  
  Authors: Shiyu Liang, Yang Gao, Lili Wang, Aimin Hao, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.30351v1.pdf)  
  Keywords: lighting, relightable, gaussian splatting, geometry, reflection, face, ar, shadow, illumination  
- **[VeilGS: Solving Darkness as a Veil of 2D Basis Maps over Retinex 3DGS](https://arxiv.org/abs/2611.27719v1)**  
  Authors: Mohab Kishawy, Chengzhou Tang, Shahram Shirani, Jun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.27719v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, 3d gaussian, efficient, face, ar, illumination  
- **[BladeR: Scalable, Shape-Guided 3D Reconstruction of Wind Turbine Blades from UAV Imagery](https://arxiv.org/abs/2611.27407v1)**  
  Authors: Jonathan Sterckx, Michiel Vlaminck, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.27407v1.pdf)  
  Keywords: lighting, 3d reconstruction, gaussian splatting, efficient, ar, localization  
- **[Multi-View Relighting with Mergeable Radiance Fields](https://arxiv.org/abs/2611.25523v1)**  
  Authors: Yinan Wang, Rohan Kadkol, Hyunjin Yoo, Jean-François Lalonde, James J. Clark  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.25523v1.pdf)  
  Keywords: light transport, nerf, lighting, gaussian splatting, 3d gaussian, relighting, geometry, efficient, ar  
- **[VideoRNG: Relightable Neural Gaussians from Generative Video Models](https://arxiv.org/abs/2611.25338v1)**  
  Authors: Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Ravi Ramamoorthi, Zahra Montazeri, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.25338v1.pdf)  
  Keywords: light transport, relightable, geometry, face, ar, compact, illumination  
- **[Beyond Appearance: Evidence-Guided Programmatic 3D Scene Reconstruction with Agentic Lighting Reasoning](https://arxiv.org/abs/2611.24565v1)**  
  Authors: Zeting Luo, Yifan Li, Shuai Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.24565v1.pdf)  
  Keywords: lighting, relighting, geometry, reflection, ar, shadow, illumination  
- **[Neural Render Proxies for Interactive and Differentiable Lighting](https://arxiv.org/abs/2611.17185v1)**  
  Authors: Sergio Sancho, Alexander Rath, Marco Manzi, Pascal Chang, Amit H. Bermano, Derek Nowrouzezahrai, Markus Gross, Marios Papas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.17185v1.pdf)  
  Keywords: path tracing, light transport, lighting, animation, relighting, efficient, lightweight, ar, fast, global illumination, illumination  

### SLAM

*Showing the latest 50 out of 70 papers*

- **[MERLoc: Robust Robot Localization in Dynamic Environments with Pose-Based Retrieval over 3D Gaussian Splatting References](https://arxiv.org/abs/2611.34932v1)**  
  Authors: Michael Baumgartner, Dario Mylonopoulos, Sammy Christen, Markus Gross, Moritz Bacher  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34932v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, motion, ar, dynamic, localization  
- **[Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](https://arxiv.org/abs/2611.33145v1)**  
  Authors: Zehan Zheng, Yanyuan Chen, Deming Li, Yutao Tang, Jianwen Xie, Alan Yuille, Jieneng Chen, Cheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33145v1.pdf)  
  Keywords: semantic, gaussian splatting, 3d gaussian, outdoor, ar, localization  
- **[Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation](https://arxiv.org/abs/2611.32718v1)**  
  Authors: Itai Mizlish, Boaz Ben-Moshe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32718v1.pdf) | [![GitHub](https://img.shields.io/github/stars/itaim18/DANIEL?style=social)](https://github.com/itaim18/DANIEL)  
  Keywords: slam, mapping, outdoor, ar, fast  
- **[GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM](https://arxiv.org/abs/2611.32335v2)**  
  Authors: Weicong Zhang, Yuan Huang, Yu Zheng, Lin Chenxiao, Yingying Li, Lilong Fan, Liangdong Zhuang, Yufan Chen, Ruiping Liu, Junwei Zheng, Jiaming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32335v2.pdf)  
  Keywords: slam, gaussian splatting, geometry, tracking, face, ar, dynamic, mapping  
- **[View Management with Gaussian Placement and Opacity Regularization for Online 3DGS](https://arxiv.org/abs/2611.32025v1)**  
  Authors: Dong Hwi Kim, Park Sangwon, Chaehyeon Song, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32025v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, geometry, face, ar, mapping, localization  
- **[BladeR: Scalable, Shape-Guided 3D Reconstruction of Wind Turbine Blades from UAV Imagery](https://arxiv.org/abs/2611.27407v1)**  
  Authors: Jonathan Sterckx, Michiel Vlaminck, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.27407v1.pdf)  
  Keywords: lighting, 3d reconstruction, gaussian splatting, efficient, ar, localization  
- **[Facet-SLAM: Real-Time Triangle Splatting SLAM](https://arxiv.org/abs/2611.23935v1)**  
  Authors: Edward Beng Wai Tan, Siew-Kei Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.23935v1.pdf) | [![GitHub](https://img.shields.io/github/stars/edward62740/Facet-SLAM?style=social)](https://github.com/edward62740/Facet-SLAM)  
  Keywords: slam, gaussian splatting, 3d gaussian, geometry, tracking, face, ar, fast, localization  
- **[ReTouchGS: Ultralight Render-free Aesthetic Color Enhancement and Transfer for 3D Gaussian Splatting](https://arxiv.org/abs/2611.23054v1)**  
  Authors: Chuanzhi Xu, Boyu Wei, Chengkun Yue, Xuanhua Yin, Yiyang Li, Haodong Chen, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.23054v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, ar, mapping  
- **[CoSphere-SLAM: Multi-Agent Panoramic Gaussian Splatting SLAM with Spherical Loop Closure](https://arxiv.org/abs/2611.22235v2)**  
  Authors: Qi Shao, Zhihao Cao, Shuhao Zhai, Taoyu Wu, Zhuoxiao Li, Anh Nguyen, Long Hu, Xianzhi Li, Hong Liang, Liang Li, Baoru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.22235v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cosphere-slam.github.io)  
  Keywords: slam, gaussian splatting, mapping, head, face, ar, fast  
- **[QuantileGS: Quantile-Based Conformal Bounds on RGB Rendering Errors for Novel View Synthesis with 3D Gaussian Splatting](https://arxiv.org/abs/2611.21253v1)**  
  Authors: Haiyang Xu, Ziye Zhang, Bin Pan, Xia Xu, Zhenwei Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.21253v1.pdf)  
  Keywords: nerf, gaussian splatting, 3d gaussian, ar, mapping, localization  

### Scene Understanding

*Showing the latest 50 out of 88 papers*

- **[Neural Rendering Compiler: Generative Video Models as Programmable Renderers](https://arxiv.org/abs/2611.34680v1)**  
  Authors: Yuxia Zhu, Xinglong Xu, Hao Liang, Linzhuang Sun, Caijun Jia, Qifeng Cai, Jincen Luo, Lei Li, Alden Cai, Asher Qin, Wentao Zhang, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.34680v1.pdf)  
  Keywords: lighting, neural rendering, semantic, face, ar  
- **[Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](https://arxiv.org/abs/2611.33145v1)**  
  Authors: Zehan Zheng, Yanyuan Chen, Deming Li, Yutao Tang, Jianwen Xie, Alan Yuille, Jieneng Chen, Cheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33145v1.pdf)  
  Keywords: semantic, gaussian splatting, 3d gaussian, outdoor, ar, localization  
- **[NRG-Twins: Pixel-Level Ground Truth for Rigidity Violations in Generated Videos](https://arxiv.org/abs/2611.32431v1)**  
  Authors: Chenrui Fan, Qiyang Hu, Luca Scharr, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32431v1.pdf)  
  Keywords: segmentation, ar, motion, 3d reconstruction  
- **[Tornado4D: Physics-Guided 4D Gaussian Reconstruction of a Laboratory Tornado from Sparse One-Sided Videos](https://arxiv.org/abs/2611.31435v1)**  
  Authors: Yucheng Zhu, Maria J. Molina, Christopher Metzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31435v1.pdf)  
  Keywords: understanding, 3d reconstruction, 4d, geometry, motion, ar  
- **[SemGuard: Semantics-Decoupled Watermarking for Gaussian Splatting](https://arxiv.org/abs/2611.28636v1)**  
  Authors: Yingying Shi, Zhong Zhou, Bin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.28636v1.pdf)  
  Keywords: semantic, gaussian splatting, efficient, ar, dynamic, high-fidelity  
- **[A Hierarchical Onboard Vision-Language-Navigation Framework for Aerial Robots in Complex Environments](https://arxiv.org/abs/2611.23930v1)**  
  Authors: Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Zhaoqi Wang, Yuxin Fan, Wenjun Li, Kenghou Hoi, Zhichao Han, Xin Zhou, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wyz000.github.io/VLN-AR)  
  Keywords: semantic, gaussian splatting, 3d gaussian, ar, lightweight, dynamic  
- **[GaussianMamba: Geometric and Relational State Space Scanning of 3D Gaussian Primitives](https://arxiv.org/abs/2611.22742v1)**  
  Authors: A. Enes Doruk, Ozgur Erkent  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.22742v1.pdf)  
  Keywords: semantic, 3d gaussian, geometry, efficient, ar  
- **[The Mask Is Not the Object: Volumetric Supervision for 3D Gaussian Segmentation](https://arxiv.org/abs/2611.21383v1)**  
  Authors: Jeonghwan Cho, Minsu Kim, Junyoung Hong, Seon Joo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.21383v1.pdf)  
  Keywords: 3d gaussian, segmentation, ar, gaussian splatting  
- **[InterRSGaussian: Interactive Multi-view Instance Segmentation for 3D Remote Sensing Scenes](https://arxiv.org/abs/2611.20425v1)**  
  Authors: Zipeng Qi, Zhengxia Zou, Zhenwei Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.20425v1.pdf)  
  Keywords: 3d gaussian, segmentation, ar, understanding  
- **[SemLite-GS: Semantic-Selective Parallel Gaussian Splatting for Lightweight Building Reconstruction from UAV Oblique Imagery](https://arxiv.org/abs/2611.19773v1)**  
  Authors: Tengfei Wang, Xin Wang, Zihan Li, Quanjian Ji, Yifei Yu, Dong Lin, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.19773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRIS-LAB-whu/SemLite-GS?style=social)](https://github.com/IRIS-LAB-whu/SemLite-GS)  
  Keywords: semantic, gaussian splatting, 3d gaussian, efficient, lightweight, ar  



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
