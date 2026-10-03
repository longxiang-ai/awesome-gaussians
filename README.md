# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-gaussians/)**: an interactive paper map, monthly trends, topic network and co-author network of every tracked paper.

> Last Update: 2026-10-03 02:51:35

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
- [Acceleration](#acceleration) (85 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (162 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (191 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (40 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (212 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (26 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (193 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (77 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (4 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (39 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (80 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (102 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: gaussian splatting, 3d gaussian, high-fidelity, survey, face, ar  
- **[Quality Assessment of 3D Gaussian Splatting: Distortions, Benchmarks, and Open Challenges](https://arxiv.org/abs/2609.23027v1)**  
  Authors: Shuai Liu, Binqiang Liu, Qingyu Mao, Jiacong Chen, Yongsheng Liang, Youneng Bao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23027v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, survey, ar, compression  
- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: geometry, gaussian splatting, motion, survey, ar, 3d reconstruction, illumination  
- **[UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys](https://arxiv.org/abs/2608.06404v1)**  
  Authors: Junxiong Zhou, Xuechen Li, Chonghao Qiu, Lang Qiao, Xiaowei Jia, Qi Yang, Chishan Zhang, Leikun Yin, Nanshan You, Vipin Kumar, David Mulla, Ce Yang, Zhenong Jin, Licheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06404v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://link-dev.github.io/UAV3DCrop)  
  Keywords: nerf, geometry, gaussian splatting, dynamic, 3d gaussian, survey, ar, 3d reconstruction  
- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: dynamic, localization, 3d gaussian, high-fidelity, survey, slam, ar, mapping, efficient, tracking  

### Acceleration

*Showing the latest 50 out of 85 papers*

- **[One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time Avatars](https://arxiv.org/abs/2610.02207v1)**  
  Authors: Ramazan Fazylov, Stamatis Lefkimmiatis, Ivan Laptev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02207v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ramazan793.github.io/gala)  
  Keywords: dynamic, avatar, 3d gaussian, ar, animation, efficient, fast  
- **[Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation](https://arxiv.org/abs/2610.01114v1)**  
  Authors: Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01114v1.pdf)  
  Keywords: deformation, gaussian splatting, motion, ar, efficient, fast  
- **[Dirichlet Splatting: Differentiable Rendering for Wave-Based Inverse Problems](https://arxiv.org/abs/2610.00618v1)**  
  Authors: Xingyu Chen, Wuqiong Zhao, Xinyu Zhang, Tzu-Mao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00618v1.pdf)  
  Keywords: ar, 3d gaussian, fast, gaussian splatting  
- **[EffGS: Efficient and High-Fidelity Gaussian Splatting](https://arxiv.org/abs/2609.39553v1)**  
  Authors: Changbai Li, Shuo Yang, Yichen Yang, Shuwei Shao, Huobin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39553v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, high-fidelity, ar, efficient, compact, acceleration  
- **[RLX: A Unified Multi-Backend Tensor Compiler and Distributed Runtime in Rust](https://arxiv.org/abs/2609.37916v1)**  
  Authors: Eugene Hauptmann, Nataliya Kosmyna  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37916v1.pdf)  
  Keywords: ar, 3d gaussian, fast, gaussian splatting  
- **[EndoPrior-GS: Dynamic Endoscopic Reconstruction with a Joint Texture Prior](https://arxiv.org/abs/2609.37874v1)**  
  Authors: Jiaqi Huang, Shidong Wang, Tong Xin, Kabita Adhikari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiaqi-huang-77.github.io/EndoPrior-GS)  
  Keywords: nerf, geometry, gaussian splatting, dynamic, 3d gaussian, real-time rendering, ar, illumination  
- **[WINGS: Reference-Free Gaussian Splatting Inpainting with 3D-Native Generative Priors](https://arxiv.org/abs/2609.37816v1)**  
  Authors: Noé Lallouet, Michael Fischer, Elie Michel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37816v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, ar, fast  
- **[Distilling Privileged Control Barrier Functions into RGB-Only Safety Filters for Dynamic Visual Navigation](https://arxiv.org/abs/2609.36520v1)**  
  Authors: Seungyeon Yoo, Gawon Lee, Seungwoo Jung, Inkyu Jang, H. Jin Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36520v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://syeon-yoo.github.io/distill-cbf-site)  
  Keywords: dynamic, gaussian splatting, motion, real-time rendering, ar, 3d reconstruction  
- **[Rate-Distortion Adaptive Primitive Selection for Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2609.34367v2)**  
  Authors: Yulong Cheng, Youneng Bao, Junfeng Zhou, Mu Li, Jie Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34367v2.pdf)  
  Keywords: gaussian splatting, ar, lightweight, vr, efficient, fast  
- **[AGILE-GS: Anchor-Guided Fast Next-Best-View Selection for Active 3D Gaussian Splatting](https://arxiv.org/abs/2609.34176v1)**  
  Authors: Amirhossein Mollaei Khass, Nader Motee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34176v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, ar, fast  

### Applications

*Showing the latest 50 out of 498 papers*

- **[One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time Avatars](https://arxiv.org/abs/2610.02207v1)**  
  Authors: Ramazan Fazylov, Stamatis Lefkimmiatis, Ivan Laptev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02207v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ramazan793.github.io/gala)  
  Keywords: dynamic, avatar, 3d gaussian, ar, animation, efficient, fast  
- **[EvenSplat: Coupled 2D-3D Decomposition for Gaussian Splatting under Exposure and Illumination Variation](https://arxiv.org/abs/2610.01876v1)**  
  Authors: Tongyu Wu, Jacob Edwards, Ziteng Cui, Caigui Jiang, Cheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01876v1.pdf)  
  Keywords: geometry, shadow, gaussian splatting, lighting, 3d gaussian, face, ar, illumination  
- **[3DROID: A Renderable 3D Gaussian Dataset with Measured Per-Scene Reliability](https://arxiv.org/abs/2610.01744v1)**  
  Authors: Wonguen Cho, Junhoo Lee, Nojun Kwak  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01744v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/wonguen/3DROID) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/wonguen/3DROID)  
  Keywords: face, ar, 3d gaussian  
- **[MEGA: Object-Level Mesh Extraction from 3D Gaussian Splatting via Spatial Visual Distillation](https://arxiv.org/abs/2610.01707v1)**  
  Authors: Liwei Liao, Yingkui Zhang, Qianqian Tong, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01707v1.pdf)  
  Keywords: ar, face, 3d gaussian, gaussian splatting  
- **[VoxelSynth3D: Interpretable Volumetric Image-Domain Metal Artifact Reduction with a Paired Synthetic CLINIC-Metal Benchmark](https://arxiv.org/abs/2610.01512v1)**  
  Authors: Amritesh Banerjee, Abdul Basit, Renil Renji Joseph, Nouhaila Innan, Muhammad Shafique  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01512v1.pdf)  
  Keywords: face, ar, 3d gaussian, localization  
- **[Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation](https://arxiv.org/abs/2610.01114v1)**  
  Authors: Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01114v1.pdf)  
  Keywords: deformation, gaussian splatting, motion, ar, efficient, fast  
- **[TRACE: Privacy-Preserving Next-Best-View Selection over Distributed 3D Gaussian-Splat Maps](https://arxiv.org/abs/2610.00822v1)**  
  Authors: Amirhossein Mollaei Khass, Athanasios Cosse, Qiyu Sun, Nader Motee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00822v1.pdf)  
  Keywords: head, 3d gaussian, gaussian splatting, ar  
- **[What Builds the Scene? Luminance Dominates Geometry Formation in 3D Gaussian Splatting](https://arxiv.org/abs/2610.00749v1)**  
  Authors: Rezvan Joshaghani, Steven Cutchin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00749v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, face, ar  
- **[Measuring Asset and Scene Reconstruction Effects in Real-to-Sim Robot Evaluation](https://arxiv.org/abs/2610.00731v1)**  
  Authors: Sanya Verma, Luca Cilio, Velissarios Christodoulou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00731v1.pdf)  
  Keywords: ar, geometry  
- **[Dirichlet Splatting: Differentiable Rendering for Wave-Based Inverse Problems](https://arxiv.org/abs/2610.00618v1)**  
  Authors: Xingyu Chen, Wuqiong Zhao, Xinyu Zhang, Tzu-Mao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00618v1.pdf)  
  Keywords: ar, 3d gaussian, fast, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 162 papers*

- **[One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time Avatars](https://arxiv.org/abs/2610.02207v1)**  
  Authors: Ramazan Fazylov, Stamatis Lefkimmiatis, Ivan Laptev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02207v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ramazan793.github.io/gala)  
  Keywords: dynamic, avatar, 3d gaussian, ar, animation, efficient, fast  
- **[EvenSplat: Coupled 2D-3D Decomposition for Gaussian Splatting under Exposure and Illumination Variation](https://arxiv.org/abs/2610.01876v1)**  
  Authors: Tongyu Wu, Jacob Edwards, Ziteng Cui, Caigui Jiang, Cheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01876v1.pdf)  
  Keywords: geometry, shadow, gaussian splatting, lighting, 3d gaussian, face, ar, illumination  
- **[3DROID: A Renderable 3D Gaussian Dataset with Measured Per-Scene Reliability](https://arxiv.org/abs/2610.01744v1)**  
  Authors: Wonguen Cho, Junhoo Lee, Nojun Kwak  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01744v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/wonguen/3DROID) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/wonguen/3DROID)  
  Keywords: face, ar, 3d gaussian  
- **[MEGA: Object-Level Mesh Extraction from 3D Gaussian Splatting via Spatial Visual Distillation](https://arxiv.org/abs/2610.01707v1)**  
  Authors: Liwei Liao, Yingkui Zhang, Qianqian Tong, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01707v1.pdf)  
  Keywords: ar, face, 3d gaussian, gaussian splatting  
- **[VoxelSynth3D: Interpretable Volumetric Image-Domain Metal Artifact Reduction with a Paired Synthetic CLINIC-Metal Benchmark](https://arxiv.org/abs/2610.01512v1)**  
  Authors: Amritesh Banerjee, Abdul Basit, Renil Renji Joseph, Nouhaila Innan, Muhammad Shafique  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01512v1.pdf)  
  Keywords: face, ar, 3d gaussian, localization  
- **[TRACE: Privacy-Preserving Next-Best-View Selection over Distributed 3D Gaussian-Splat Maps](https://arxiv.org/abs/2610.00822v1)**  
  Authors: Amirhossein Mollaei Khass, Athanasios Cosse, Qiyu Sun, Nader Motee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00822v1.pdf)  
  Keywords: head, 3d gaussian, gaussian splatting, ar  
- **[What Builds the Scene? Luminance Dominates Geometry Formation in 3D Gaussian Splatting](https://arxiv.org/abs/2610.00749v1)**  
  Authors: Rezvan Joshaghani, Steven Cutchin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00749v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, face, ar  
- **[UGOD: Uncertainty-Guided Opacity and Dropout for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.39089v1)**  
  Authors: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Chenghao Qian, Ziyang Wang, Xinqi Fan, Liangxiu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39089v1.pdf)  
  Keywords: nerf, gaussian splatting, head, 3d gaussian, ar, sparse-view, lightweight, compact  
- **[StereoGaussians: Feed-Forward 3D Gaussian Splatting from Stereo Images](https://arxiv.org/abs/2609.38592v1)**  
  Authors: Boyuan Tian, Huangying Zhan, Zhan Li, Shin-Fang Chng, Hanwen Yang, Zirui Wang, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38592v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, face, ar  
- **[Beyond Monoscopic Viewing: A Study on 3D Gaussian Splatting Quality in VR](https://arxiv.org/abs/2609.38525v1)**  
  Authors: Shreyas Shivakumara, Gabriel Eilertsen, Karljohan Lundin Palmerius  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38525v1.pdf)  
  Keywords: geometry, gaussian splatting, head, 3d gaussian, ar, vr  

### Dynamic Scene

*Showing the latest 50 out of 191 papers*

- **[One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time Avatars](https://arxiv.org/abs/2610.02207v1)**  
  Authors: Ramazan Fazylov, Stamatis Lefkimmiatis, Ivan Laptev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02207v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ramazan793.github.io/gala)  
  Keywords: dynamic, avatar, 3d gaussian, ar, animation, efficient, fast  
- **[Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation](https://arxiv.org/abs/2610.01114v1)**  
  Authors: Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01114v1.pdf)  
  Keywords: deformation, gaussian splatting, motion, ar, efficient, fast  
- **[Reconstructing the Dynamic World: A Representation-Centric View of 4D Scene Reconstruction](https://arxiv.org/abs/2609.39960v1)**  
  Authors: Ziren Gong, Guo Chen, Yongjia Li, Yihua Shao, Fabio Tosi, Stefano Mattoccia, Matteo Poggi, Hao Tang, Fei Ma, Shuyan Li, Ziyang Yan, Nicu Sebe, Ling Shao, Jianfei Cai, Qi Tian, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39960v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ZiyangYan/Awesome-4D-Scene-Reconstruction?style=social)](https://github.com/ZiyangYan/Awesome-4D-Scene-Reconstruction)  
  Keywords: nerf, geometry, gaussian splatting, dynamic, 4d, motion, 3d gaussian, understanding, ar  
- **[Eulerian Motion Reconstruction for Water Scenery](https://arxiv.org/abs/2609.38622v1)**  
  Authors: Chuhan Chen, Yen-Chi Cheng, Ayush Saraf, Rajvi Shah, Tuotuo Li, Johannes Kopf, Chen Gao, Hung-Yu Tseng, Deva Ramanan, Matthew O'Toole, Changil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38622v1.pdf)  
  Keywords: 4d, dynamic, motion, ar, animation  
- **[PneuTac: Tactile Manipulation with Soft Pneumatic Robots via Unified MPM-Gaussian Splatting Simulation](https://arxiv.org/abs/2609.38418v1)**  
  Authors: Shaohong Zhong, Marco Pontin, Joe Watson, Perla Maiolino, Ingmar Posner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38418v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, ar, efficient  
- **[EndoPrior-GS: Dynamic Endoscopic Reconstruction with a Joint Texture Prior](https://arxiv.org/abs/2609.37874v1)**  
  Authors: Jiaqi Huang, Shidong Wang, Tong Xin, Kabita Adhikari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiaqi-huang-77.github.io/EndoPrior-GS)  
  Keywords: nerf, geometry, gaussian splatting, dynamic, 3d gaussian, real-time rendering, ar, illumination  
- **[Prior-Driven Enhancements in 3D Gaussian Splatting: Normals and Depths Regularization](https://arxiv.org/abs/2609.36969v1)**  
  Authors: Gyeonggwan Lee, Seunghwan Hong, Junghun Suh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36969v1.pdf)  
  Keywords: gaussian splatting, motion, 3d gaussian, face, ar  
- **[DispFlow-GS: Displacement Flow Supervision with Motion Disentangling for Monocular Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2609.36940v1)**  
  Authors: Thai Duy Nguyen, Haitian Zhang, Addison Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36940v1.pdf)  
  Keywords: geometry, gaussian splatting, dynamic, deformation, motion, localization, 3d gaussian, ar  
- **[Distilling Privileged Control Barrier Functions into RGB-Only Safety Filters for Dynamic Visual Navigation](https://arxiv.org/abs/2609.36520v1)**  
  Authors: Seungyeon Yoo, Gawon Lee, Seungwoo Jung, Inkyu Jang, H. Jin Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36520v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://syeon-yoo.github.io/distill-cbf-site)  
  Keywords: dynamic, gaussian splatting, motion, real-time rendering, ar, 3d reconstruction  
- **[CollisionSplatting: Collision-Aware Motion Planning in 3DGS Scenes with Image-Conditioned Objectives and Adjustable Conservatism](https://arxiv.org/abs/2609.35619v1)**  
  Authors: R. Khorrambakht, Joaquim Ortiz-Haro, Stephan Weiss, Ludovic Righetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35619v1.pdf)  
  Keywords: gaussian splatting, lighting, motion, 3d gaussian, ar, vr  

### Few-shot

- **[UGOD: Uncertainty-Guided Opacity and Dropout for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.39089v1)**  
  Authors: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Chenghao Qian, Ziyang Wang, Xinqi Fan, Liangxiu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39089v1.pdf)  
  Keywords: nerf, gaussian splatting, head, 3d gaussian, ar, sparse-view, lightweight, compact  
- **[Remote Sensing Sparse-View 3D Gaussian Splatting via Depth Image-Based Rendering](https://arxiv.org/abs/2609.35612v1)**  
  Authors: Jiaming Kang, Zhengxia Zou, Zhenwei Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35612v1.pdf) | [![GitHub](https://img.shields.io/github/stars/kanehub/DIBR-GS?style=social)](https://github.com/kanehub/DIBR-GS)  
  Keywords: nerf, gaussian splatting, 3d gaussian, face, ar, sparse-view  
- **[GAPS: Generative Active Pseudo-view Selection for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.23436v2)**  
  Authors: Hongfei Zhu, Haochen Deng, Sitao Zhang, Ling Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23436v2.pdf)  
  Keywords: nerf, geometry, gaussian splatting, 3d gaussian, real-time rendering, ar, sparse-view  
- **[D3GS: Depth, DINO, and RGB Diffusion Co-Guided 3D Gaussian Splatting for Sparse-View Reconstruction](https://arxiv.org/abs/2609.22941v1)**  
  Authors: Yunqi Gao, Zhanfeng Liao, Hanzhang Tu, Zhaoqi Su, Guoqing Zheng, Songtao Wang, Hongwen Zhang, Zhou Xue, Leyuan Liu, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.22941v1.pdf)  
  Keywords: nerf, geometry, gaussian splatting, 3d gaussian, ar, sparse-view  
- **[LINGO: Latent Initialization and Gradient Optimization for Sparse-view X-ray Novel View Synthesis and CT Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2609.22849v1)**  
  Authors: Lifeng Xing, Dequan Jin, Kunpeng Bu, Peigeng He, Shihui Ying  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.22849v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, ar, sparse-view  
- **[4DGS-Fixer: Generative Sparse-View 4D Gaussian Splatting with Iterative Refinement Guided by Video Diffusion Priors](https://arxiv.org/abs/2609.21176v3)**  
  Authors: Haitao Huang, Shenghao Zhao, Boyuan Tian, Shin-Fang Chng, Songlin Yang, Sheila Lim, Huangying Zhan, Yi Xu, Anyi Rao, Frank Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21176v3.pdf)  
  Keywords: large scene, 4d, gaussian splatting, dynamic, ar, sparse-view  
- **[Geometry beneath the Waves: Dense Priors for Sparse-View Underwater 3D Gaussian Splatting](https://arxiv.org/abs/2609.18737v2)**  
  Authors: Harvey Caldeira, Haoran Wang, Guoxi Huang, Shaoyu Cai, Rachel Fu, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18737v2.pdf)  
  Keywords: nerf, geometry, gaussian splatting, head, motion, 3d gaussian, sparse view, ar, sparse-view, 3d reconstruction  
- **[CADSplat: Sparse-View 3D Gaussian Splatting Aided by CAD Models for Robust, Photorealistic Digital-Twin Reconstruction](https://arxiv.org/abs/2609.18473v1)**  
  Authors: Kristof Overdulve, Lode Jorissen, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18473v1.pdf)  
  Keywords: few-shot, deformation, gaussian splatting, 3d gaussian, face, ar, sparse-view  
- **[Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement](https://arxiv.org/abs/2609.17039v1)**  
  Authors: Yuetong Wang, Jinsheng Quan, Yi Yang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17039v1.pdf)  
  Keywords: geometry, gaussian splatting, motion, 3d gaussian, ar, sparse-view  
- **[CGGT: Curve-Grounded Geometry Transformer for 3D Parametric Curve Reconstruction](https://arxiv.org/abs/2609.14521v1)**  
  Authors: Zhirui Gao, Renjiao Yi, Yunfan Ye, Ruizhen Hu, Chenyang Zhu, Wei Chen, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14521v1.pdf)  
  Keywords: nerf, geometry, compact, ar, sparse-view, fast  

### Geometry Reconstruction

*Showing the latest 50 out of 212 papers*

- **[EvenSplat: Coupled 2D-3D Decomposition for Gaussian Splatting under Exposure and Illumination Variation](https://arxiv.org/abs/2610.01876v1)**  
  Authors: Tongyu Wu, Jacob Edwards, Ziteng Cui, Caigui Jiang, Cheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01876v1.pdf)  
  Keywords: geometry, shadow, gaussian splatting, lighting, 3d gaussian, face, ar, illumination  
- **[What Builds the Scene? Luminance Dominates Geometry Formation in 3D Gaussian Splatting](https://arxiv.org/abs/2610.00749v1)**  
  Authors: Rezvan Joshaghani, Steven Cutchin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00749v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, face, ar  
- **[Measuring Asset and Scene Reconstruction Effects in Real-to-Sim Robot Evaluation](https://arxiv.org/abs/2610.00731v1)**  
  Authors: Sanya Verma, Luca Cilio, Velissarios Christodoulou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00731v1.pdf)  
  Keywords: ar, geometry  
- **[Reconstructing the Dynamic World: A Representation-Centric View of 4D Scene Reconstruction](https://arxiv.org/abs/2609.39960v1)**  
  Authors: Ziren Gong, Guo Chen, Yongjia Li, Yihua Shao, Fabio Tosi, Stefano Mattoccia, Matteo Poggi, Hao Tang, Fei Ma, Shuyan Li, Ziyang Yan, Nicu Sebe, Ling Shao, Jianfei Cai, Qi Tian, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39960v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ZiyangYan/Awesome-4D-Scene-Reconstruction?style=social)](https://github.com/ZiyangYan/Awesome-4D-Scene-Reconstruction)  
  Keywords: nerf, geometry, gaussian splatting, dynamic, 4d, motion, 3d gaussian, understanding, ar  
- **[TSGL: Teacher-Student Graph Learning for 3DGS Compression](https://arxiv.org/abs/2609.38635v1)**  
  Authors: Matin Bani Saedi, Matthew Kyan, Gene Cheung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38635v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, ar, compression, efficient, compact  
- **[StereoGaussians: Feed-Forward 3D Gaussian Splatting from Stereo Images](https://arxiv.org/abs/2609.38592v1)**  
  Authors: Boyuan Tian, Huangying Zhan, Zhan Li, Shin-Fang Chng, Hanwen Yang, Zirui Wang, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38592v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, face, ar  
- **[Beyond Monoscopic Viewing: A Study on 3D Gaussian Splatting Quality in VR](https://arxiv.org/abs/2609.38525v1)**  
  Authors: Shreyas Shivakumara, Gabriel Eilertsen, Karljohan Lundin Palmerius  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38525v1.pdf)  
  Keywords: geometry, gaussian splatting, head, 3d gaussian, ar, vr  
- **[Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering](https://arxiv.org/abs/2609.38177v1)**  
  Authors: Jaewoo Jung, Hyeonseo Yu, Honggyu An, Jisang Han, Mungyeom Kim, Minkyeong Jeon, Heeseong Shin, Wonjun Moon, Federico Tombari, Daniel Barath, Marc Pollefeys, Seungryong Kim, Sunghwan Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38177v1.pdf)  
  Keywords: geometry, gaussian splatting, human, 3d gaussian, understanding, body, ar, compact  
- **[EndoPrior-GS: Dynamic Endoscopic Reconstruction with a Joint Texture Prior](https://arxiv.org/abs/2609.37874v1)**  
  Authors: Jiaqi Huang, Shidong Wang, Tong Xin, Kabita Adhikari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiaqi-huang-77.github.io/EndoPrior-GS)  
  Keywords: nerf, geometry, gaussian splatting, dynamic, 3d gaussian, real-time rendering, ar, illumination  
- **[WINGS: Reference-Free Gaussian Splatting Inpainting with 3D-Native Generative Priors](https://arxiv.org/abs/2609.37816v1)**  
  Authors: Noé Lallouet, Michael Fischer, Elie Michel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37816v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, ar, fast  

### Large Scene

- **[LEGO-Anything: Coding Agents for 3D Scene Reconstruction](https://arxiv.org/abs/2609.36380v1)**  
  Authors: Xirui Li, Peng Shi, Mingwen Dong, Sheng Zhang, Zhuoyan Xu, Dongkyu Lee, Shuaichen Chang, Yi Xiang, Lin Pan, Jiarong Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36380v1.pdf)  
  Keywords: face, ar, geometry, outdoor  
- **[Federated 3D Gaussian Splatting for Large-Scale Scene Reconstruction at Wireless Edge](https://arxiv.org/abs/2609.32177v1)**  
  Authors: Guanlin Wu, Chao Hu, Pu Chen, Juyong Zhang, Han Hu, Shuguang Cui, Jie Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32177v1.pdf)  
  Keywords: large scene, gaussian splatting, 3d gaussian, face, ar, lightweight, efficient  
- **[ChronoFuseGS: Multi-Temporal Gaussian Fusion with Per-Splat Persistence and Change Visualization](https://arxiv.org/abs/2609.31339v1)**  
  Authors: Tobias Batik, Diana Marin, Peter Kán, Hannes Kaufmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31339v1.pdf)  
  Keywords: ar, gaussian splatting, outdoor  
- **[OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning](https://arxiv.org/abs/2609.29985v1)**  
  Authors: Haoran Wang, Shaoyu Cai, Adrian Azzarelli, Zhuodong Jiang, Guoxi Huang, Eng Tat Khoo, Brett Seymour, Fan Zhang, David Bull, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29985v1.pdf)  
  Keywords: nerf, large scene, gaussian splatting, compact, 3d gaussian, real-time rendering, ar, 3d reconstruction, efficient, fast  
- **[Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models](https://arxiv.org/abs/2609.26007v1)**  
  Authors: Yuhang Zhang, Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Weiying Wang, Steven Yang, Qingsong Yan, Chao Yan, Mir Feroskhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26007v1.pdf)  
  Keywords: gaussian splatting, motion, 3d gaussian, ar, outdoor  
- **[Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking](https://arxiv.org/abs/2609.25746v1)**  
  Authors: Edward Beng Wai Tan, Siew-Kei Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25746v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, slam, face, ar, tracking, outdoor  
- **[Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene Reconstruction](https://arxiv.org/abs/2609.23796v2)**  
  Authors: Yang-Tian Sun, Tianjia Liu, Zehuan Huang, Yi-Hua Huang, Xiaoyang Lyu, Ziyi Yang, Zi-Xin Zou, Yuan-Chen Guo, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23796v2.pdf)  
  Keywords: geometry, high-fidelity, face, ar, outdoor  
- **[Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization](https://arxiv.org/abs/2609.21347v1)**  
  Authors: Xiangfei Guo, Hao Shi, Yufan Zhang, Zhonghua Yi, Yongqi Mao, Xiaoting Yin, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21347v1.pdf) | [![GitHub](https://img.shields.io/github/stars/guoxf304/CubeSplat?style=social)](https://github.com/guoxf304/CubeSplat)  
  Keywords: gaussian splatting, 3d gaussian, high-fidelity, slam, face, ar, mapping, tracking, outdoor  
- **[4DGS-Fixer: Generative Sparse-View 4D Gaussian Splatting with Iterative Refinement Guided by Video Diffusion Priors](https://arxiv.org/abs/2609.21176v3)**  
  Authors: Haitao Huang, Shenghao Zhao, Boyuan Tian, Shin-Fang Chng, Songlin Yang, Sheila Lim, Huangying Zhan, Yi Xu, Anyi Rao, Frank Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21176v3.pdf)  
  Keywords: large scene, 4d, gaussian splatting, dynamic, ar, sparse-view  
- **[The Neverwhere Visual Parkour Benchmark Suite](https://arxiv.org/abs/2609.16443v1)**  
  Authors: Ziyu Chen, Henghui Bao, Haoran Chang, Alan Yu, Ran Choi, Kai McClennen, Gio Huh, Kevin Yang, Ri-Zhao Qiu, Yajvan Ravan, John J. Leonard, Xiaolong Wang, Phillip Isola, Ge Yang, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16443v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziyc.github.io/neverwhere-bench)  
  Keywords: gaussian splatting, motion, 3d gaussian, ar, outdoor  

### Model Compression

*Showing the latest 50 out of 193 papers*

- **[One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time Avatars](https://arxiv.org/abs/2610.02207v1)**  
  Authors: Ramazan Fazylov, Stamatis Lefkimmiatis, Ivan Laptev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02207v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ramazan793.github.io/gala)  
  Keywords: dynamic, avatar, 3d gaussian, ar, animation, efficient, fast  
- **[Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation](https://arxiv.org/abs/2610.01114v1)**  
  Authors: Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01114v1.pdf)  
  Keywords: deformation, gaussian splatting, motion, ar, efficient, fast  
- **[EffGS: Efficient and High-Fidelity Gaussian Splatting](https://arxiv.org/abs/2609.39553v1)**  
  Authors: Changbai Li, Shuo Yang, Yichen Yang, Shuwei Shao, Huobin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39553v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, high-fidelity, ar, efficient, compact, acceleration  
- **[UGOD: Uncertainty-Guided Opacity and Dropout for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.39089v1)**  
  Authors: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Chenghao Qian, Ziyang Wang, Xinqi Fan, Liangxiu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39089v1.pdf)  
  Keywords: nerf, gaussian splatting, head, 3d gaussian, ar, sparse-view, lightweight, compact  
- **[TSGL: Teacher-Student Graph Learning for 3DGS Compression](https://arxiv.org/abs/2609.38635v1)**  
  Authors: Matin Bani Saedi, Matthew Kyan, Gene Cheung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38635v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, ar, compression, efficient, compact  
- **[Gaussian Stippling: Efficient Sorting-Free 3D Gaussian Rendering through Hybrid Sampling and Spatiotemporal Reconstruction](https://arxiv.org/abs/2609.38488v1)**  
  Authors: Zijian Huang, Suiliang Mai, Chuankun Zheng, Yuan Meng, Yuchi Huo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38488v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, high-fidelity, ar, lightweight, efficient  
- **[PneuTac: Tactile Manipulation with Soft Pneumatic Robots via Unified MPM-Gaussian Splatting Simulation](https://arxiv.org/abs/2609.38418v1)**  
  Authors: Shaohong Zhong, Marco Pontin, Joe Watson, Perla Maiolino, Ingmar Posner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38418v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, ar, efficient  
- **[Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering](https://arxiv.org/abs/2609.38177v1)**  
  Authors: Jaewoo Jung, Hyeonseo Yu, Honggyu An, Jisang Han, Mungyeom Kim, Minkyeong Jeon, Heeseong Shin, Wonjun Moon, Federico Tombari, Daniel Barath, Marc Pollefeys, Seungryong Kim, Sunghwan Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38177v1.pdf)  
  Keywords: geometry, gaussian splatting, human, 3d gaussian, understanding, body, ar, compact  
- **[NRF-GS: Neural Residual Fields for Expressive and Compact Gaussian Splatting](https://arxiv.org/abs/2609.37115v1)**  
  Authors: Pratik Singh Bisht, Andreas Kolb  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37115v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, lightweight, compact  
- **[AESplat: Advancing Pose-Free Feed-Forward 3D Gaussian Splatting via Decoupled Appearance Modeling](https://arxiv.org/abs/2609.36693v1)**  
  Authors: Shiwei Ren, Zhiang Liu, Yongchun Fang, Hongwei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36693v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aesplat.github.io)  
  Keywords: ar, efficient, 3d gaussian, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 77 papers*

- **[EffGS: Efficient and High-Fidelity Gaussian Splatting](https://arxiv.org/abs/2609.39553v1)**  
  Authors: Changbai Li, Shuo Yang, Yichen Yang, Shuwei Shao, Huobin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39553v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, high-fidelity, ar, efficient, compact, acceleration  
- **[Gaussian Stippling: Efficient Sorting-Free 3D Gaussian Rendering through Hybrid Sampling and Spatiotemporal Reconstruction](https://arxiv.org/abs/2609.38488v1)**  
  Authors: Zijian Huang, Suiliang Mai, Chuankun Zheng, Yuan Meng, Yuchi Huo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38488v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, high-fidelity, ar, lightweight, efficient  
- **[Robot-GST: geometry-aware spatial-temporal robot policy representation and evaluation](https://arxiv.org/abs/2609.33872v1)**  
  Authors: Sichao Liu, Zekun Wang, Lixuan Tang, Yiming Li, Xiaohan Wang, Hanzhi Zhang, Daqiang Guo, Peng Zhou, Lihui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.33872v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robot-gst.github.io)  
  Keywords: geometry, gaussian splatting, 3d gaussian, high-fidelity, ar  
- **[Dynamic Thermal Gaussians: Multimodal 4D Gaussian Splatting](https://arxiv.org/abs/2609.24531v1)**  
  Authors: Rongfeng Lu, Lifeng Lin, Xiaobao Wei, Quan Chen, Ming Lu, Yitian Xue, Yaoqi Sun, Yuhan Gao, Anke Xue, Chenggang Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24531v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LinLif1869/DTG?style=social)](https://github.com/LinLif1869/DTG)  
  Keywords: 4d, dynamic, geometry, gaussian splatting, motion, deformation, high-fidelity, ar  
- **[OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones](https://arxiv.org/abs/2609.24253v1)**  
  Authors: Zhongrui You, Zhen Li, Junli Liu, Zhigang Wang, Bin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24253v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://openflyscan.github.io)  
  Keywords: gaussian splatting, 3d gaussian, high-fidelity, survey, face, ar  
- **[Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene Reconstruction](https://arxiv.org/abs/2609.23796v2)**  
  Authors: Yang-Tian Sun, Tianjia Liu, Zehuan Huang, Yi-Hua Huang, Xiaoyang Lyu, Ziyi Yang, Zi-Xin Zou, Yuan-Chen Guo, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23796v2.pdf)  
  Keywords: geometry, high-fidelity, face, ar, outdoor  
- **[GARO: Geometry-Aware Redundancy Optimization for Real-Time and High-Fidelity Dynamic Gaussian Splatting](https://arxiv.org/abs/2609.23509v1)**  
  Authors: Huiwen Xue, Kaixing Zhao, Zuheng Ming, Tingcheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23509v1.pdf)  
  Keywords: geometry, dynamic, gaussian splatting, high-fidelity, face, ar, compact  
- **[Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization](https://arxiv.org/abs/2609.21347v1)**  
  Authors: Xiangfei Guo, Hao Shi, Yufan Zhang, Zhonghua Yi, Yongqi Mao, Xiaoting Yin, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21347v1.pdf) | [![GitHub](https://img.shields.io/github/stars/guoxf304/CubeSplat?style=social)](https://github.com/guoxf304/CubeSplat)  
  Keywords: gaussian splatting, 3d gaussian, high-fidelity, slam, face, ar, mapping, tracking, outdoor  
- **[AirSplan: Risk-Aware Motion Planning for Quadrotors in Cluttered 3D Gaussian Splats](https://arxiv.org/abs/2609.21226v1)**  
  Authors: Seth Isaacson, William Hong, Katherine A. Skinner, Ram Vasudevan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21226v1.pdf)  
  Keywords: geometry, gaussian splatting, motion, 3d gaussian, high-fidelity, ar  
- **[Demonstration Synthesis from a Single Scan via Gaussian Splatting for Visuomotor Policy Learning](https://arxiv.org/abs/2609.21112v1)**  
  Authors: Beichen Wang, Yuen-Hei Yeung, V. R. Sridhar Devarakonda, Xuesu Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21112v1.pdf)  
  Keywords: dynamic, gaussian splatting, human, 3d gaussian, high-fidelity, ar  

### Ray Tracing

- **[Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)**  
  Authors: Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/vorotracing)  
  Keywords: nerf, gaussian splatting, ray tracing, compact, motion, 3d gaussian, face, real-time rendering, ar, fast  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: nerf, gaussian splatting, ray tracing, shadow, compact, 3d gaussian, ar, mapping, efficient, reflection, fast  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: ray tracing, gaussian splatting, lighting, relighting, face, ar, efficient, illumination, reflection  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: geometry, ray tracing, gaussian splatting, dynamic, motion, human, 3d gaussian, high-fidelity, face, ar, reflection  

### Relighting

- **[EvenSplat: Coupled 2D-3D Decomposition for Gaussian Splatting under Exposure and Illumination Variation](https://arxiv.org/abs/2610.01876v1)**  
  Authors: Tongyu Wu, Jacob Edwards, Ziteng Cui, Caigui Jiang, Cheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01876v1.pdf)  
  Keywords: geometry, shadow, gaussian splatting, lighting, 3d gaussian, face, ar, illumination  
- **[EndoPrior-GS: Dynamic Endoscopic Reconstruction with a Joint Texture Prior](https://arxiv.org/abs/2609.37874v1)**  
  Authors: Jiaqi Huang, Shidong Wang, Tong Xin, Kabita Adhikari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiaqi-huang-77.github.io/EndoPrior-GS)  
  Keywords: nerf, geometry, gaussian splatting, dynamic, 3d gaussian, real-time rendering, ar, illumination  
- **[CollisionSplatting: Collision-Aware Motion Planning in 3DGS Scenes with Image-Conditioned Objectives and Adjustable Conservatism](https://arxiv.org/abs/2609.35619v1)**  
  Authors: R. Khorrambakht, Joaquim Ortiz-Haro, Stephan Weiss, Ludovic Righetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35619v1.pdf)  
  Keywords: gaussian splatting, lighting, motion, 3d gaussian, ar, vr  
- **[PePESeg3D: Perception Prior Enhances Multi-Scale Segmentation for 3D Gaussian Splatting](https://arxiv.org/abs/2609.28645v1)**  
  Authors: Sungjae Choi, Seunghee Koh, Junmo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28645v1.pdf) | [![GitHub](https://img.shields.io/github/stars/BeCow5X5/PePESeg3D?style=social)](https://github.com/BeCow5X5/PePESeg3D)  
  Keywords: semantic, nerf, geometry, gaussian splatting, lighting, 3d gaussian, ar, segmentation  
- **[Relightable 3D Avatar Reconstruction with Semantic-Adaptive Motion-Illumination Responses](https://arxiv.org/abs/2609.24158v1)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Jijie Li, Baiqin Wang, Shukai Chen, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24158v1.pdf)  
  Keywords: semantic, lightweight, relightable, avatar, lighting, motion, head, 3d gaussian, relighting, ar, animation, illumination, compact  
- **[RawSLAM: Online HDR Gaussian SLAM from Linear Radiance](https://arxiv.org/abs/2609.20589v1)**  
  Authors: Marina Orozco González, Luis Merino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.20589v1.pdf)  
  Keywords: shadow, gaussian splatting, dynamic, lighting, motion, slam, ar, mapping, illumination, tracking  
- **[GS-PI: An Optimization-Decoupled Appearance Decomposition Approach for Generating PBR Gaussian Assets](https://arxiv.org/abs/2609.19907v1)**  
  Authors: Jieting Xu, Rengan Xie, Zijian Huang, Zehui Jin, Rui Wang, Yuchi Huo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.19907v1.pdf)  
  Keywords: semantic, relightable, geometry, gaussian splatting, lighting, ar, efficient, illumination  
- **[RGS: Reflection-aware Gaussian Splatting via Learning Geometry Continuity for Reflective Objects](https://arxiv.org/abs/2609.19421v1)**  
  Authors: Xiaobiao Du, Yida Wang, Cheng Bi, Kun Zhan, Xin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.19421v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, face, ar, reflection  
- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: geometry, gaussian splatting, dynamic, localization, lighting, motion, robotics, 3d gaussian, slam, tracking, ar, mapping, fast  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: 4d, gaussian splatting, dynamic, human, ar, illumination, fast, outdoor  

### SLAM

*Showing the latest 50 out of 80 papers*

- **[VoxelSynth3D: Interpretable Volumetric Image-Domain Metal Artifact Reduction with a Paired Synthetic CLINIC-Metal Benchmark](https://arxiv.org/abs/2610.01512v1)**  
  Authors: Amritesh Banerjee, Abdul Basit, Renil Renji Joseph, Nouhaila Innan, Muhammad Shafique  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01512v1.pdf)  
  Keywords: face, ar, 3d gaussian, localization  
- **[Lens Flare Removal and Reconstruction](https://arxiv.org/abs/2609.39527v1)**  
  Authors: Tarun Yenamandra, Jonathon Luiten, Daniel Cremers, Nathan Matsuda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39527v1.pdf)  
  Keywords: ar, gaussian splatting, localization  
- **[DispFlow-GS: Displacement Flow Supervision with Motion Disentangling for Monocular Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2609.36940v1)**  
  Authors: Thai Duy Nguyen, Haitian Zhang, Addison Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36940v1.pdf)  
  Keywords: geometry, gaussian splatting, dynamic, deformation, motion, localization, 3d gaussian, ar  
- **[EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation](https://arxiv.org/abs/2609.34853v1)**  
  Authors: Sungho Moon, Kota Shimomura, Junwoo Park, Wonhyeok Choi, Seunghun Lee, Takayoshi Yamashita, Sunghoon Im  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34853v1.pdf)  
  Keywords: gaussian splatting, localization, 3d gaussian, understanding, ar, segmentation, compact  
- **[Reliability-Regulated Trajectory Optimization for Progressive COLMAP-Free 3D Gaussian Splatting](https://arxiv.org/abs/2609.30865v1)**  
  Authors: Zijian Wu, Jinliang Wang, Zidian Lin, Ying Song, Ziqian Lu, Hanjie Ma, Zhen Ye, Mingfeng Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30865v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Zijian1026/RRTO-CF3DGS?style=social)](https://github.com/Zijian1026/RRTO-CF3DGS)  
  Keywords: gaussian splatting, dynamic, motion, 3d gaussian, ar, tracking  
- **[SplatLabel: Pseudo-Labelling through 4D Gaussian Splatting](https://arxiv.org/abs/2609.29836v1)**  
  Authors: Nitya Nanvani, Andras Palffy, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29836v1.pdf)  
  Keywords: semantic, 4d, geometry, gaussian splatting, dynamic, ar, segmentation, tracking  
- **[From Scattered Gaussians to Structured Maps: Efficient Gaussian Splatting Coding via Dual-phase Morton Sorting](https://arxiv.org/abs/2609.29041v1)**  
  Authors: Bolin Chen, Shanzhi Yin, Ru-Ling Liao, Yibo Fan, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29041v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, mapping, compression, efficient  
- **[ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards](https://arxiv.org/abs/2609.26315v1)**  
  Authors: Alessandro Masini, Matteo Frosi, Mirko Usuelli, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26315v1.pdf)  
  Keywords: semantic, gaussian splatting, 3d gaussian, slam, face, ar, fast  
- **[Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking](https://arxiv.org/abs/2609.25746v1)**  
  Authors: Edward Beng Wai Tan, Siew-Kei Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25746v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, slam, face, ar, tracking, outdoor  
- **[BayesianGS-SLAM: Uncertainty-Aware Neural Rendering SLAM via Probabilistic Formulation](https://arxiv.org/abs/2609.24140v1)**  
  Authors: Kyeongsu Kang, Seongbo Ha, Sibaek Lee, Hyeonwoo Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24140v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, slam, neural rendering, ar, mapping, tracking  

### Scene Understanding

*Showing the latest 50 out of 102 papers*

- **[Reconstructing the Dynamic World: A Representation-Centric View of 4D Scene Reconstruction](https://arxiv.org/abs/2609.39960v1)**  
  Authors: Ziren Gong, Guo Chen, Yongjia Li, Yihua Shao, Fabio Tosi, Stefano Mattoccia, Matteo Poggi, Hao Tang, Fei Ma, Shuyan Li, Ziyang Yan, Nicu Sebe, Ling Shao, Jianfei Cai, Qi Tian, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39960v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ZiyangYan/Awesome-4D-Scene-Reconstruction?style=social)](https://github.com/ZiyangYan/Awesome-4D-Scene-Reconstruction)  
  Keywords: nerf, geometry, gaussian splatting, dynamic, 4d, motion, 3d gaussian, understanding, ar  
- **[Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering](https://arxiv.org/abs/2609.38177v1)**  
  Authors: Jaewoo Jung, Hyeonseo Yu, Honggyu An, Jisang Han, Mungyeom Kim, Minkyeong Jeon, Heeseong Shin, Wonjun Moon, Federico Tombari, Daniel Barath, Marc Pollefeys, Seungryong Kim, Sunghwan Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38177v1.pdf)  
  Keywords: geometry, gaussian splatting, human, 3d gaussian, understanding, body, ar, compact  
- **[EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation](https://arxiv.org/abs/2609.34853v1)**  
  Authors: Sungho Moon, Kota Shimomura, Junwoo Park, Wonhyeok Choi, Seunghun Lee, Takayoshi Yamashita, Sunghoon Im  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34853v1.pdf)  
  Keywords: gaussian splatting, localization, 3d gaussian, understanding, ar, segmentation, compact  
- **[GraphWrit3R: End-to-End 3D Scene Graph Writing](https://arxiv.org/abs/2609.31595v1)**  
  Authors: Luka Milivojevic, Nikola Popovic, Sayan Deb Sarkar, Sebastian Koch, Iro Armeni, Luc Van Gool, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31595v1.pdf)  
  Keywords: semantic, ar  
- **[SplatLabel: Pseudo-Labelling through 4D Gaussian Splatting](https://arxiv.org/abs/2609.29836v1)**  
  Authors: Nitya Nanvani, Andras Palffy, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29836v1.pdf)  
  Keywords: semantic, 4d, geometry, gaussian splatting, dynamic, ar, segmentation, tracking  
- **[PlenoCI: Plenoptic CharacterIstics for View Dependence Aware Change Classification](https://arxiv.org/abs/2609.28930v1)**  
  Authors: Jason Lai, Chamuditha Jayanga Galappaththige, Niko Suenderhauf, Dimity Miller, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://js0n-lai.github.io/plenoci)  
  Keywords: gaussian splatting, 3d gaussian, ar, understanding, efficient  
- **[PePESeg3D: Perception Prior Enhances Multi-Scale Segmentation for 3D Gaussian Splatting](https://arxiv.org/abs/2609.28645v1)**  
  Authors: Sungjae Choi, Seunghee Koh, Junmo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28645v1.pdf) | [![GitHub](https://img.shields.io/github/stars/BeCow5X5/PePESeg3D?style=social)](https://github.com/BeCow5X5/PePESeg3D)  
  Keywords: semantic, nerf, geometry, gaussian splatting, lighting, 3d gaussian, ar, segmentation  
- **[ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards](https://arxiv.org/abs/2609.26315v1)**  
  Authors: Alessandro Masini, Matteo Frosi, Mirko Usuelli, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26315v1.pdf)  
  Keywords: semantic, gaussian splatting, 3d gaussian, slam, face, ar, fast  
- **[Agentic Building-Aware Satellite Gaussian Splatting for Auditable Urban DSM Reconstruction](https://arxiv.org/abs/2609.25578v1)**  
  Authors: Wentao Sun, Zhengsen Xu, Yiping Chen, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25578v1.pdf)  
  Keywords: semantic, gaussian splatting, face, neural rendering, ar, 3d reconstruction  
- **[ZVeC: A Zero-Shot Framework for Instance-Level Vehicle Extraction and Generative Point Cloud Completion](https://arxiv.org/abs/2609.24825v1)**  
  Authors: Daisy Li, Kyle Gao, Quanyun Wu, Boris Jutzi, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24825v1.pdf)  
  Keywords: semantic, ar, 3d gaussian  



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
