# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-08-05 01:39:09

## 📰 Latest Updates

🚀 **[2026-02] Major Feature Update — v2.0**
- **Unified CLI**: Single entry point `python main.py` with subcommands: `init`, `search`, `suggest`, `export-bib`, `readme`
- **Interactive Configuration Wizard**: Run `python main.py init` to set up keywords, domains, time range, and API keys step-by-step
- **Custom Time Range Filtering**: Support relative periods (`6m`, `1y`, `2y`) and absolute date ranges (`2024-01-01` to `2025-06-01`)
- **Smart Link Extraction**: Automatically extracts and classifies GitHub, project page, dataset, video, demo, and HuggingFace links from paper abstracts
- **BibTeX Export**: Fetch BibTeX from arXiv and export to `.bib` files with category/date filters
- **LLM Keyword Suggestion**: Paste a few paper titles or arXiv IDs, and an LLM automatically generates optimized search keywords
- **arXiv Domain Filtering**: Restrict searches to specific arXiv categories (e.g., `cs.CV`, `cs.GR`)

🔧 **[2025-06-26] HTTP 301 Redirect Issue Completely Resolved!** 
- Implemented multi-layer fallback strategy to thoroughly solve network compatibility issues

🔧 **[2025-06-26] Configurable Search Keywords Feature Added!**
- You can now customize search keywords by modifying `data/search_config.json`

- View detailed updates: [News.md](News.md) 📋

---

## Categories

- [3DGS Surveys](#3dgs-surveys) (3 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (98 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (173 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (195 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (39 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (213 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (22 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (192 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (119 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (13 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (55 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (76 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (119 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: localization, tracking, efficient, slam, dynamic, survey, 3d gaussian, mapping, ar, high-fidelity  
- **[Recent Advances and Trends in Learning-based 3D Representations](https://arxiv.org/abs/2606.04871v1)**  
  Authors: Adrien Schockaert, Hamid Laga, Hazem Wannous, Vincent Magnier, Guillaume Dufaye, Jean-françois Witz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.04871v1.pdf)  
  Keywords: medical, autonomous driving, survey, neural rendering, 3d gaussian, motion, ar, vr, compact, gaussian splatting, 4d, recognition, 3d reconstruction  
- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137v1)**  
  Authors: Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00137v1.pdf)  
  Keywords: animation, mapping, geometry, survey, ar, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 98 papers*

- **[FAST-GS: Frequency Aware Space-time Gaussian Splatting for Photorealistic Dynamic Novel View Synthesis](https://arxiv.org/abs/2608.01958v1)**  
  Authors: Zhengyang Zhang, Ziyu Lu, PengCheng Li, Hongbo Duan, Yi Liu, Pengting Luo, Peiyu Zhuang, Xinghui Li, Shaohua Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01958v1.pdf)  
  Keywords: fast, efficient, dynamic, ar, motion, gaussian splatting, 4d, real-time rendering, 3d reconstruction  
- **[G-Skin: Learning to Bind 3D Gaussians with Generative Visual Priors](https://arxiv.org/abs/2608.01726v1)**  
  Authors: Yuxin Yao, Kendong Liu, Shiqi Zhou, Jiazhi Xia, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01726v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yaoyx689.github.io/GSkin.html)  
  Keywords: animation, efficient rendering, efficient, geometry, 3d gaussian, ar, motion, face, gaussian splatting, high-fidelity  
- **[D^2-4DGS: Dual-Depth Guided Sparse-Camera 4D Gaussian Splatting](https://arxiv.org/abs/2608.01588v1)**  
  Authors: Jijian Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01588v1.pdf)  
  Keywords: efficient, dynamic, geometry, ar, gaussian splatting, 4d, real-time rendering, sparse-view  
- **[Struct-GStream: Towards Efficient Free-Viewpoint Video Streaming at Low-Bitrates with Structured 3D Gaussians](https://arxiv.org/abs/2608.01053v1)**  
  Authors: Han Jiao, Jiakai Sun, Lei Zhao, Wei Xing, Huaizhong Lin, Zhanjie Zhang, Ao Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01053v1.pdf)  
  Keywords: fast, efficient, dynamic, neural rendering, 3d gaussian, motion, ar, real-time rendering, high-fidelity  
- **[Stipple: Real-Time Incremental Gaussian Splatting with Visual-Inertial Tracking](https://arxiv.org/abs/2608.00931v1)**  
  Authors: Kilian Northoff, Mateo de Mayo, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00931v1.pdf)  
  Keywords: localization, robotics, efficient rendering, tracking, efficient, mapping, 3d gaussian, ar, gaussian splatting, slam, 3d reconstruction  
- **[Split and Drive: Dual-Axis Disentanglement for Real-Time Gaussian Head Avatars](https://arxiv.org/abs/2607.28032v1)**  
  Authors: MD Wahiduzzaman Khan, Mingshan Jia, Xiaolin Zhang, En Yu, Kaska Musial-Gabrys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28032v1.pdf)  
  Keywords: fast, human, tracking, avatar, 3d gaussian, ar, gaussian splatting, head  
- **[AtlasLC: Fast Codec-Ready Compression of Object-Centric 3D Gaussian Splatting](https://arxiv.org/abs/2607.26525v1)**  
  Authors: ByungHyun Kim, Jinwoo Jeon, Woontack Woo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26525v1.pdf)  
  Keywords: fast, compression, mapping, geometry, 3d gaussian, semantic, ar, compact, gaussian splatting, lightweight, real-time rendering  
- **[SplatStream: Fine Granular Scalable Gaussian Splatting for Adaptive 3D Scene Streaming](https://arxiv.org/abs/2607.25971v2)**  
  Authors: Muhammad Talha, William Gordon, Sajid Umair, Zhu Li, Anique Akhtar, Joel Jung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25971v2.pdf)  
  Keywords: high quality, dynamic, 3d gaussian, ar, gaussian splatting, lightweight, real-time rendering  
- **[Head Avatars with Dynamic Explicit Hair](https://arxiv.org/abs/2607.23861v1)**  
  Authors: Vanessa Sklyarova, Haonan Chen, Berna Kabadayi, Tobias Kirschstein, Zicong Fan, Xi Wang, Gerard Pons-Moll, Matthias Nießner, Marc Pollefeys, Michael J. Black, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.23861v1.pdf)  
  Keywords: deformation, human, tracking, avatar, dynamic, 3d gaussian, ar, acceleration, motion, face, gaussian splatting, head  
- **[3D Gaussian Splatting for Scientific Particle Data Compression and Rendering](https://arxiv.org/abs/2607.22956v1)**  
  Authors: Bo Jiang, Youyuan Liu, Taolue Yang, Sheng Di, Sian Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22956v1.pdf)  
  Keywords: fast, compression, 3d gaussian, ar, compact, gaussian splatting, lightweight  

### Applications

*Showing the latest 50 out of 498 papers*

- **[3DGSI-Assessor: A Large-Scale Dataset and An LMM-based Method for 3D Gaussian Splatting Image Quality Assessment](https://arxiv.org/abs/2608.03279v1)**  
  Authors: Yuke Xing, Jiarui Wang, William Gordon, Zhu Li, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03279v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YukeXing/3DGSI-Assessor?style=social)](https://github.com/YukeXing/3DGSI-Assessor)  
  Keywords: compression, geometry, 3d gaussian, ar, face, gaussian splatting, semantic  
- **[Standalone DINOv3 for Training-Free Open-Vocabulary Semantic Segmentation in Remote Sensing](https://arxiv.org/abs/2608.03023v1)**  
  Authors: Changhao Zhao, Haoxiang Li, Yuke Li, Hai Liu, LingLin Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03023v1.pdf)  
  Keywords: ar, segmentation, semantic, gaussian splatting  
- **[InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular View Synthesis](https://arxiv.org/abs/2608.02437v2)**  
  Authors: Jiawei Wang, Hao Yu, Yongzhen Hu, Xinyi Yang, Tao Ni, Xin Zhan, Junbo Chen, Xiaowei Zhou, Ruizhen Hu, Sida Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02437v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/InfiniSplat)  
  Keywords: geometry, 3d gaussian, ar, face, gaussian splatting  
- **[TRACE: Ergodic Trajectory Optimization for Active Scene Reconstruction](https://arxiv.org/abs/2608.02304v1)**  
  Authors: Ziyue Zheng, Linli Shi, Bingkun He, Wen Jiang, Ziyun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02304v1.pdf) | [![GitHub](https://img.shields.io/github/stars/spikelab-jhu/trace-active-reconstruction?style=social)](https://github.com/spikelab-jhu/trace-active-reconstruction)  
  Keywords: ar, efficient, mapping  
- **[CLEAR: Conflict-aware Learning via Evidence-guided Adaptive Routing for Unified Sparse-View 3D Gaussian Super-Resolution](https://arxiv.org/abs/2608.02206v1)**  
  Authors: Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02206v1.pdf)  
  Keywords: ar, sparse-view, gaussian splatting, 3d gaussian  
- **[DerainSplat: Feed-Forward Clean 3D Gaussian Splatting from Sparse Rainy Views](https://arxiv.org/abs/2608.02191v1)**  
  Authors: Fuzhen Jiang, Changyue Shi, Chuxiao Yang, Xinyuan Hu, Wenjie Ye, Minghao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02191v1.pdf)  
  Keywords: autonomous driving, nerf, geometry, illumination, 3d gaussian, ar, gaussian splatting  
- **[GSRAIN: Physically Calibrated High-/Low-Frequency Rainfall Synthesis for 3D Gaussian Driving Scenes](https://arxiv.org/abs/2608.02177v1)**  
  Authors: Fanyu Wang, Longgao Zhang, Junyi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02177v1.pdf)  
  Keywords: autonomous driving, geometry, 3d gaussian, ar, gaussian splatting  
- **[UniqueSplat: View-conditioned 3D Gaussian Splatting for Generalizable 3D Reconstruction](https://arxiv.org/abs/2608.02145v1)**  
  Authors: Haixu Song, Xiaoke Yang, Shengjun Zhang, Jiwen Lu, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02145v1.pdf)  
  Keywords: dynamic, 3d gaussian, ar, gaussian splatting, 3d reconstruction  
- **[DeGS: A Scalable 3DGS Architecture via Decoupled Workload Parsing and Reorganization](https://arxiv.org/abs/2608.02099v1)**  
  Authors: Minnan Pei, Gang Li, Zeyu Zhu, Siting Wang, Junwen Si, Zhuoran Song, Yu Feng, Fangxin Liu, Xiaoyao Liang, Jian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02099v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, compact, gaussian splatting  
- **[MANGO-Grasp: Mahalanobis Fields over Geometry-Oriented 3D Gaussians for Cross-Embodiment Dexterous Grasping](https://arxiv.org/abs/2608.02014v1)**  
  Authors: Heng Zhang, Kevin Yuchen Ma, Mike Zheng Shou, Weisi Lin, Yan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02014v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://connor-zh.github.io/MANGO-Grasp)  
  Keywords: ar, face, geometry, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 173 papers*

- **[3DGSI-Assessor: A Large-Scale Dataset and An LMM-based Method for 3D Gaussian Splatting Image Quality Assessment](https://arxiv.org/abs/2608.03279v1)**  
  Authors: Yuke Xing, Jiarui Wang, William Gordon, Zhu Li, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03279v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YukeXing/3DGSI-Assessor?style=social)](https://github.com/YukeXing/3DGSI-Assessor)  
  Keywords: compression, geometry, 3d gaussian, ar, face, gaussian splatting, semantic  
- **[InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular View Synthesis](https://arxiv.org/abs/2608.02437v2)**  
  Authors: Jiawei Wang, Hao Yu, Yongzhen Hu, Xinyi Yang, Tao Ni, Xin Zhan, Junbo Chen, Xiaowei Zhou, Ruizhen Hu, Sida Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02437v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/InfiniSplat)  
  Keywords: geometry, 3d gaussian, ar, face, gaussian splatting  
- **[MANGO-Grasp: Mahalanobis Fields over Geometry-Oriented 3D Gaussians for Cross-Embodiment Dexterous Grasping](https://arxiv.org/abs/2608.02014v1)**  
  Authors: Heng Zhang, Kevin Yuchen Ma, Mike Zheng Shou, Weisi Lin, Yan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02014v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://connor-zh.github.io/MANGO-Grasp)  
  Keywords: ar, face, geometry, 3d gaussian  
- **[G-Skin: Learning to Bind 3D Gaussians with Generative Visual Priors](https://arxiv.org/abs/2608.01726v1)**  
  Authors: Yuxin Yao, Kendong Liu, Shiqi Zhou, Jiazhi Xia, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01726v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yaoyx689.github.io/GSkin.html)  
  Keywords: animation, efficient rendering, efficient, geometry, 3d gaussian, ar, motion, face, gaussian splatting, high-fidelity  
- **[GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian Splatting with Graph Optimization](https://arxiv.org/abs/2608.01492v1)**  
  Authors: Baihan Yang, Tiexin Li, Yuheng Liu, Xin Lin, Xinke Li, Xiaohui Xie, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01492v1.pdf)  
  Keywords: human, 3d gaussian, ar, sparse view, gaussian splatting, head, lightweight  
- **[Swimm3R: Splatting with Medium-aware SfM for Underwater 3D Reconstruction](https://arxiv.org/abs/2608.00950v1)**  
  Authors: Minseong Kweon, Junaed Sattar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00950v1.pdf)  
  Keywords: localization, geometry, ar, motion, gaussian splatting, head, 3d reconstruction  
- **[Manifold-GS: Certified Hybrid Assets via Varifold-Conservative Gaussian Splatting](https://arxiv.org/abs/2608.00214v1)**  
  Authors: Boyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00214v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, face, gaussian splatting, sparse-view  
- **[OASIS: Occlusion-aware Single-image Hand Avatar Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2607.29633v1)**  
  Authors: Zhisheng Han, Shiyao Wu, Jiayan Qiu, Yakun Ju, Lu Liu, Le Zhang, Pengfei Feng, Huiyu Zhou, Zheheng Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.29633v1.pdf)  
  Keywords: deformation, nerf, avatar, geometry, 3d gaussian, ar, face, gaussian splatting  
- **[MonoVoc: Decoupling Geometry and Semantics for Lightweight Monocular Open-Vocabulary 3D Gaussians](https://arxiv.org/abs/2607.28300v1)**  
  Authors: Pouya Ardekhani, Zahra Dehghanian, Morteza Abolghasemi, Hamid R. Rabiee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28300v1.pdf)  
  Keywords: efficient, segmentation, geometry, 3d gaussian, understanding, mapping, ar, compact, head, lightweight, semantic  
- **[S-Avatar: Diffusion-Guided Gaussian Head Avatars from a Single Image](https://arxiv.org/abs/2607.28164v1)**  
  Authors: Hail Song, Seokhwan Yang, Jiwon Yang, Woojin Cho, Woontack Woo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28164v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hailsong/savatar?style=social)](https://github.com/hailsong/savatar)  
  Keywords: efficient, avatar, dynamic, 3d gaussian, ar, vr, gaussian splatting, head  

### Dynamic Scene

*Showing the latest 50 out of 195 papers*

- **[UniqueSplat: View-conditioned 3D Gaussian Splatting for Generalizable 3D Reconstruction](https://arxiv.org/abs/2608.02145v1)**  
  Authors: Haixu Song, Xiaoke Yang, Shengjun Zhang, Jiwen Lu, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02145v1.pdf)  
  Keywords: dynamic, 3d gaussian, ar, gaussian splatting, 3d reconstruction  
- **[ASTRA: Asynchronous Spatio-Temporal Reconstruction via Trajectory Alignment](https://arxiv.org/abs/2608.02006v1)**  
  Authors: Junyu Zhu, Hao Zhu, Xinzhuo Zhang, Hongdong Li, Zhan Ma, Xun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02006v1.pdf)  
  Keywords: deformation, dynamic, geometry, ar, motion, gaussian splatting  
- **[3D Gaussian Splatting and Mesh-Based Digital Twins: An Exploratory Study for Virtual Reality Tourism](https://arxiv.org/abs/2608.01969v1)**  
  Authors: Maximilian Warsinke, Francesco Vona, Abm Tariqul Islam, Tanja Kojić, Jan-Niklas Voigt-Antons, Sebastian Möller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01969v1.pdf)  
  Keywords: 3d gaussian, ar, motion, vr, gaussian splatting, understanding, high-fidelity  
- **[FAST-GS: Frequency Aware Space-time Gaussian Splatting for Photorealistic Dynamic Novel View Synthesis](https://arxiv.org/abs/2608.01958v1)**  
  Authors: Zhengyang Zhang, Ziyu Lu, PengCheng Li, Hongbo Duan, Yi Liu, Pengting Luo, Peiyu Zhuang, Xinghui Li, Shaohua Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01958v1.pdf)  
  Keywords: fast, efficient, dynamic, ar, motion, gaussian splatting, 4d, real-time rendering, 3d reconstruction  
- **[DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing](https://arxiv.org/abs/2608.01761v1)**  
  Authors: Siying Li, Ying Ni, Jie Sun, Jian Sun, Haotian Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01761v1.pdf)  
  Keywords: autonomous driving, compression, lighting, illumination, neural rendering, 3d gaussian, dynamic, ar, gaussian splatting, semantic, high-fidelity, relighting  
- **[G-Skin: Learning to Bind 3D Gaussians with Generative Visual Priors](https://arxiv.org/abs/2608.01726v1)**  
  Authors: Yuxin Yao, Kendong Liu, Shiqi Zhou, Jiazhi Xia, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01726v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yaoyx689.github.io/GSkin.html)  
  Keywords: animation, efficient rendering, efficient, geometry, 3d gaussian, ar, motion, face, gaussian splatting, high-fidelity  
- **[D^2-4DGS: Dual-Depth Guided Sparse-Camera 4D Gaussian Splatting](https://arxiv.org/abs/2608.01588v1)**  
  Authors: Jijian Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01588v1.pdf)  
  Keywords: efficient, dynamic, geometry, ar, gaussian splatting, 4d, real-time rendering, sparse-view  
- **[DynActiveGS: Active Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2608.01178v1)**  
  Authors: Hongbo Duan, Pengting Luo, Chengzhi Zhao, Yuanhao Chiang, Fangming Liu, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01178v1.pdf)  
  Keywords: dynamic, 3d gaussian, ar, motion, gaussian splatting  
- **[Struct-GStream: Towards Efficient Free-Viewpoint Video Streaming at Low-Bitrates with Structured 3D Gaussians](https://arxiv.org/abs/2608.01053v1)**  
  Authors: Han Jiao, Jiakai Sun, Lei Zhao, Wei Xing, Huaizhong Lin, Zhanjie Zhang, Ao Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01053v1.pdf)  
  Keywords: fast, efficient, dynamic, neural rendering, 3d gaussian, motion, ar, real-time rendering, high-fidelity  
- **[Swimm3R: Splatting with Medium-aware SfM for Underwater 3D Reconstruction](https://arxiv.org/abs/2608.00950v1)**  
  Authors: Minseong Kweon, Junaed Sattar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00950v1.pdf)  
  Keywords: localization, geometry, ar, motion, gaussian splatting, head, 3d reconstruction  

### Few-shot

- **[CLEAR: Conflict-aware Learning via Evidence-guided Adaptive Routing for Unified Sparse-View 3D Gaussian Super-Resolution](https://arxiv.org/abs/2608.02206v1)**  
  Authors: Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02206v1.pdf)  
  Keywords: ar, sparse-view, gaussian splatting, 3d gaussian  
- **[D^2-4DGS: Dual-Depth Guided Sparse-Camera 4D Gaussian Splatting](https://arxiv.org/abs/2608.01588v1)**  
  Authors: Jijian Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01588v1.pdf)  
  Keywords: efficient, dynamic, geometry, ar, gaussian splatting, 4d, real-time rendering, sparse-view  
- **[GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian Splatting with Graph Optimization](https://arxiv.org/abs/2608.01492v1)**  
  Authors: Baihan Yang, Tiexin Li, Yuheng Liu, Xin Lin, Xinke Li, Xiaohui Xie, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01492v1.pdf)  
  Keywords: human, 3d gaussian, ar, sparse view, gaussian splatting, head, lightweight  
- **[Manifold-GS: Certified Hybrid Assets via Varifold-Conservative Gaussian Splatting](https://arxiv.org/abs/2608.00214v1)**  
  Authors: Boyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00214v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, face, gaussian splatting, sparse-view  
- **[Visual Relocalization from Sparse Views in Aliased and Low-Texture Environments via Novel View Synthesis](https://arxiv.org/abs/2607.22147v1)**  
  Authors: Maria Peribañez, Javier Civera, Rudolph Triebel, Riccardo Giubilato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22147v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DLR-RM/multimodal-gsplat-relocalization?style=social)](https://github.com/DLR-RM/multimodal-gsplat-relocalization)  
  Keywords: localization, geometry, illumination, 3d gaussian, motion, sparse view, ar, gaussian splatting  
- **[Posterior Variance Is a Constraint Map, Not an Error Map: Closed-Form Uncertainty for Radiative Gaussian Splatting in Sparse-View CT](https://arxiv.org/abs/2607.13682v2)**  
  Authors: Chulin Zhao, Yiran Xu, Shu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13682v2.pdf)  
  Keywords: ar, sparse-view, gaussian splatting, fast  
- **[MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction](https://arxiv.org/abs/2607.10792v1)**  
  Authors: Jinqian Yang, Yichen Wu, Wanhua Li, Haokun Lin, Renzhen Wang, Xiangchu Feng, Xixi Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.10792v1.pdf)  
  Keywords: geometry, neural rendering, 3d gaussian, ar, gaussian splatting, sparse-view, semantic, high-fidelity  
- **[Rendering-Aware Bayesian 3D Gaussian Splatting with Native Uncertainty and Adaptive Complexity Control](https://arxiv.org/abs/2607.05522v1)**  
  Authors: Gaoxiang Jia, Vikram Appia, Junzhou Huang, Xinlei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05522v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, sparse view, gaussian splatting  
- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771v1)**  
  Authors: Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03771v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/VOP-GS)  
  Keywords: efficient, geometry, 3d gaussian, ar, sparse view, face, large scene, gaussian splatting  
- **[Sparse-View Surface Reconstruction using Gaussian Splatting through High-Confidence Depth Propagation with Normal Priors](https://arxiv.org/abs/2607.03765v1)**  
  Authors: Liang Han, Bangcai Wei, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03765v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/DP-GS)  
  Keywords: geometry, 3d gaussian, ar, sparse view, face, gaussian splatting, sparse-view, high-fidelity, 3d reconstruction  

### Geometry Reconstruction

*Showing the latest 50 out of 213 papers*

- **[3DGSI-Assessor: A Large-Scale Dataset and An LMM-based Method for 3D Gaussian Splatting Image Quality Assessment](https://arxiv.org/abs/2608.03279v1)**  
  Authors: Yuke Xing, Jiarui Wang, William Gordon, Zhu Li, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03279v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YukeXing/3DGSI-Assessor?style=social)](https://github.com/YukeXing/3DGSI-Assessor)  
  Keywords: compression, geometry, 3d gaussian, ar, face, gaussian splatting, semantic  
- **[InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular View Synthesis](https://arxiv.org/abs/2608.02437v2)**  
  Authors: Jiawei Wang, Hao Yu, Yongzhen Hu, Xinyi Yang, Tao Ni, Xin Zhan, Junbo Chen, Xiaowei Zhou, Ruizhen Hu, Sida Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02437v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/InfiniSplat)  
  Keywords: geometry, 3d gaussian, ar, face, gaussian splatting  
- **[DerainSplat: Feed-Forward Clean 3D Gaussian Splatting from Sparse Rainy Views](https://arxiv.org/abs/2608.02191v1)**  
  Authors: Fuzhen Jiang, Changyue Shi, Chuxiao Yang, Xinyuan Hu, Wenjie Ye, Minghao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02191v1.pdf)  
  Keywords: autonomous driving, nerf, geometry, illumination, 3d gaussian, ar, gaussian splatting  
- **[GSRAIN: Physically Calibrated High-/Low-Frequency Rainfall Synthesis for 3D Gaussian Driving Scenes](https://arxiv.org/abs/2608.02177v1)**  
  Authors: Fanyu Wang, Longgao Zhang, Junyi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02177v1.pdf)  
  Keywords: autonomous driving, geometry, 3d gaussian, ar, gaussian splatting  
- **[UniqueSplat: View-conditioned 3D Gaussian Splatting for Generalizable 3D Reconstruction](https://arxiv.org/abs/2608.02145v1)**  
  Authors: Haixu Song, Xiaoke Yang, Shengjun Zhang, Jiwen Lu, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02145v1.pdf)  
  Keywords: dynamic, 3d gaussian, ar, gaussian splatting, 3d reconstruction  
- **[MANGO-Grasp: Mahalanobis Fields over Geometry-Oriented 3D Gaussians for Cross-Embodiment Dexterous Grasping](https://arxiv.org/abs/2608.02014v1)**  
  Authors: Heng Zhang, Kevin Yuchen Ma, Mike Zheng Shou, Weisi Lin, Yan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02014v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://connor-zh.github.io/MANGO-Grasp)  
  Keywords: ar, face, geometry, 3d gaussian  
- **[ASTRA: Asynchronous Spatio-Temporal Reconstruction via Trajectory Alignment](https://arxiv.org/abs/2608.02006v1)**  
  Authors: Junyu Zhu, Hao Zhu, Xinzhuo Zhang, Hongdong Li, Zhan Ma, Xun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02006v1.pdf)  
  Keywords: deformation, dynamic, geometry, ar, motion, gaussian splatting  
- **[FAST-GS: Frequency Aware Space-time Gaussian Splatting for Photorealistic Dynamic Novel View Synthesis](https://arxiv.org/abs/2608.01958v1)**  
  Authors: Zhengyang Zhang, Ziyu Lu, PengCheng Li, Hongbo Duan, Yi Liu, Pengting Luo, Peiyu Zhuang, Xinghui Li, Shaohua Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01958v1.pdf)  
  Keywords: fast, efficient, dynamic, ar, motion, gaussian splatting, 4d, real-time rendering, 3d reconstruction  
- **[G-Skin: Learning to Bind 3D Gaussians with Generative Visual Priors](https://arxiv.org/abs/2608.01726v1)**  
  Authors: Yuxin Yao, Kendong Liu, Shiqi Zhou, Jiazhi Xia, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01726v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yaoyx689.github.io/GSkin.html)  
  Keywords: animation, efficient rendering, efficient, geometry, 3d gaussian, ar, motion, face, gaussian splatting, high-fidelity  
- **[StreamSplat: Streaming Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2608.01659v1)**  
  Authors: Changhao Song, Yuxuan Wang, Qibiao Li, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01659v1.pdf)  
  Keywords: efficient, geometry, 3d gaussian, ar, gaussian splatting  

### Large Scene

- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: localization, tracking, mapping, outdoor, geometry, 3d gaussian, ar, gaussian splatting, lightweight, slam  
- **[Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering](https://arxiv.org/abs/2607.19893v1)**  
  Authors: Zhenxiang Ma, Zeyu He, Yuanzhen Zhou, Zhenyu Yang, Yuchang Zhang, Miao Tao, Rong Fu, Jidong Zhai, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19893v1.pdf)  
  Keywords: ar, head, large scene, neural rendering  
- **[AniGS: Bridging Rendering and Diffusion Prior for 3D Scene Animation](https://arxiv.org/abs/2607.18539v1)**  
  Authors: Yen-Chi Cheng, Chen Gao, Chuhan Chen, Tuotuo Li, Rajvi Shah, Ayush Saraf, Changil Kim, Liangyan Gui, Alexander Schwing, Johannes Kopf, Hung-Yu Tseng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18539v1.pdf)  
  Keywords: animation, deformation, dynamic, 3d gaussian, outdoor, motion, ar, gaussian splatting  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: tracking, mapping, geometry, dynamic, illumination, motion, 3d gaussian, outdoor, ar, vr  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: fast, efficient, slam, 3d gaussian, ar, motion, gaussian splatting, large scene, real-time rendering, recognition  
- **[GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors](https://arxiv.org/abs/2607.11184v1)**  
  Authors: Ruilan Gao, Letian Jin, Yu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11184v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rlgao.github.io/geogs_slam)  
  Keywords: tracking, mapping, outdoor, geometry, 3d gaussian, ar, gaussian splatting, slam  
- **[Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction](https://arxiv.org/abs/2607.08769v1)**  
  Authors: Weijian Chen, Weibo Yao, Yuhang Zhang, Xiaolin Tang, Guo Wang, Weijun Zhang, Xitong Gao, Yihao Chen, Hongde Qin, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08769v1.pdf)  
  Keywords: outdoor, geometry, ar, 3d gaussian, gaussian splatting  
- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771v1)**  
  Authors: Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03771v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/VOP-GS)  
  Keywords: efficient, geometry, 3d gaussian, ar, sparse view, face, large scene, gaussian splatting  
- **[Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673v1)**  
  Authors: Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu, Krishna Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00673v1.pdf)  
  Keywords: deformation, human, outdoor, 3d gaussian, ar  
- **[GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping](https://arxiv.org/abs/2606.30809v1)**  
  Authors: Annika Thomas, Mason Peterson, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30809v1.pdf)  
  Keywords: mapping, outdoor, geometry, 3d gaussian, ar, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 192 papers*

- **[3DGSI-Assessor: A Large-Scale Dataset and An LMM-based Method for 3D Gaussian Splatting Image Quality Assessment](https://arxiv.org/abs/2608.03279v1)**  
  Authors: Yuke Xing, Jiarui Wang, William Gordon, Zhu Li, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03279v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YukeXing/3DGSI-Assessor?style=social)](https://github.com/YukeXing/3DGSI-Assessor)  
  Keywords: compression, geometry, 3d gaussian, ar, face, gaussian splatting, semantic  
- **[TRACE: Ergodic Trajectory Optimization for Active Scene Reconstruction](https://arxiv.org/abs/2608.02304v1)**  
  Authors: Ziyue Zheng, Linli Shi, Bingkun He, Wen Jiang, Ziyun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02304v1.pdf) | [![GitHub](https://img.shields.io/github/stars/spikelab-jhu/trace-active-reconstruction?style=social)](https://github.com/spikelab-jhu/trace-active-reconstruction)  
  Keywords: ar, efficient, mapping  
- **[DeGS: A Scalable 3DGS Architecture via Decoupled Workload Parsing and Reorganization](https://arxiv.org/abs/2608.02099v1)**  
  Authors: Minnan Pei, Gang Li, Zeyu Zhu, Siting Wang, Junwen Si, Zhuoran Song, Yu Feng, Fangxin Liu, Xiaoyao Liang, Jian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02099v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, compact, gaussian splatting  
- **[FAST-GS: Frequency Aware Space-time Gaussian Splatting for Photorealistic Dynamic Novel View Synthesis](https://arxiv.org/abs/2608.01958v1)**  
  Authors: Zhengyang Zhang, Ziyu Lu, PengCheng Li, Hongbo Duan, Yi Liu, Pengting Luo, Peiyu Zhuang, Xinghui Li, Shaohua Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01958v1.pdf)  
  Keywords: fast, efficient, dynamic, ar, motion, gaussian splatting, 4d, real-time rendering, 3d reconstruction  
- **[DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing](https://arxiv.org/abs/2608.01761v1)**  
  Authors: Siying Li, Ying Ni, Jie Sun, Jian Sun, Haotian Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01761v1.pdf)  
  Keywords: autonomous driving, compression, lighting, illumination, neural rendering, 3d gaussian, dynamic, ar, gaussian splatting, semantic, high-fidelity, relighting  
- **[G-Skin: Learning to Bind 3D Gaussians with Generative Visual Priors](https://arxiv.org/abs/2608.01726v1)**  
  Authors: Yuxin Yao, Kendong Liu, Shiqi Zhou, Jiazhi Xia, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01726v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yaoyx689.github.io/GSkin.html)  
  Keywords: animation, efficient rendering, efficient, geometry, 3d gaussian, ar, motion, face, gaussian splatting, high-fidelity  
- **[StreamSplat: Streaming Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2608.01659v1)**  
  Authors: Changhao Song, Yuxuan Wang, Qibiao Li, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01659v1.pdf)  
  Keywords: efficient, geometry, 3d gaussian, ar, gaussian splatting  
- **[D^2-4DGS: Dual-Depth Guided Sparse-Camera 4D Gaussian Splatting](https://arxiv.org/abs/2608.01588v1)**  
  Authors: Jijian Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01588v1.pdf)  
  Keywords: efficient, dynamic, geometry, ar, gaussian splatting, 4d, real-time rendering, sparse-view  
- **[GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian Splatting with Graph Optimization](https://arxiv.org/abs/2608.01492v1)**  
  Authors: Baihan Yang, Tiexin Li, Yuheng Liu, Xin Lin, Xinke Li, Xiaohui Xie, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01492v1.pdf)  
  Keywords: human, 3d gaussian, ar, sparse view, gaussian splatting, head, lightweight  
- **[QuerySplat: Decoupling Geometry and Appearance Representations in 3DGS Prediction](https://arxiv.org/abs/2608.01186v1)**  
  Authors: Yinglong Li, Donghui Shen, Xiaoyu Zhang, Zhichao Ye, Hongyu Wu, Aimin Hao, Guofeng Zhang, Haomin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01186v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://inspatio.github.io/querysplat)  
  Keywords: efficient, geometry, 3d gaussian, ar, gaussian splatting, understanding, high-fidelity, 3d reconstruction  

### Quality Enhancement

*Showing the latest 50 out of 119 papers*

- **[3D Gaussian Splatting and Mesh-Based Digital Twins: An Exploratory Study for Virtual Reality Tourism](https://arxiv.org/abs/2608.01969v1)**  
  Authors: Maximilian Warsinke, Francesco Vona, Abm Tariqul Islam, Tanja Kojić, Jan-Niklas Voigt-Antons, Sebastian Möller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01969v1.pdf)  
  Keywords: 3d gaussian, ar, motion, vr, gaussian splatting, understanding, high-fidelity  
- **[DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing](https://arxiv.org/abs/2608.01761v1)**  
  Authors: Siying Li, Ying Ni, Jie Sun, Jian Sun, Haotian Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01761v1.pdf)  
  Keywords: autonomous driving, compression, lighting, illumination, neural rendering, 3d gaussian, dynamic, ar, gaussian splatting, semantic, high-fidelity, relighting  
- **[G-Skin: Learning to Bind 3D Gaussians with Generative Visual Priors](https://arxiv.org/abs/2608.01726v1)**  
  Authors: Yuxin Yao, Kendong Liu, Shiqi Zhou, Jiazhi Xia, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01726v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yaoyx689.github.io/GSkin.html)  
  Keywords: animation, efficient rendering, efficient, geometry, 3d gaussian, ar, motion, face, gaussian splatting, high-fidelity  
- **[QuerySplat: Decoupling Geometry and Appearance Representations in 3DGS Prediction](https://arxiv.org/abs/2608.01186v1)**  
  Authors: Yinglong Li, Donghui Shen, Xiaoyu Zhang, Zhichao Ye, Hongyu Wu, Aimin Hao, Guofeng Zhang, Haomin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01186v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://inspatio.github.io/querysplat)  
  Keywords: efficient, geometry, 3d gaussian, ar, gaussian splatting, understanding, high-fidelity, 3d reconstruction  
- **[Struct-GStream: Towards Efficient Free-Viewpoint Video Streaming at Low-Bitrates with Structured 3D Gaussians](https://arxiv.org/abs/2608.01053v1)**  
  Authors: Han Jiao, Jiakai Sun, Lei Zhao, Wei Xing, Huaizhong Lin, Zhanjie Zhang, Ao Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01053v1.pdf)  
  Keywords: fast, efficient, dynamic, neural rendering, 3d gaussian, motion, ar, real-time rendering, high-fidelity  
- **[Genie Sim PanoWorld: An Infinite Indoor 3D World Generation Pipeline via Panoramic Scene Modeling and Simulation](https://arxiv.org/abs/2607.26646v1)**  
  Authors: Yongxin Su, Linjie Hou, Feng Wang, Jialin Tang, Zhijun Li, Qian Wang, Maoqing Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26646v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, motion, high-fidelity, 3d reconstruction  
- **[SplatStream: Fine Granular Scalable Gaussian Splatting for Adaptive 3D Scene Streaming](https://arxiv.org/abs/2607.25971v2)**  
  Authors: Muhammad Talha, William Gordon, Sajid Umair, Zhu Li, Anique Akhtar, Joel Jung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25971v2.pdf)  
  Keywords: high quality, dynamic, 3d gaussian, ar, gaussian splatting, lightweight, real-time rendering  
- **[PanoLess: Environment Reconstruction from Partial Reflective Views](https://arxiv.org/abs/2607.25362v1)**  
  Authors: Ahitagni Das, Ashok Veeraraghavan, Vivek Boominathan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25362v1.pdf)  
  Keywords: reflection, illumination, ar, face, high-fidelity  
- **[GenSplatCodec: Feed-Forward Gaussian Splatting Compression via One-Step Diffusion](https://arxiv.org/abs/2607.24403v1)**  
  Authors: Qiang Hu, Zhenlong Wu, Lei Huang, Zihan Zheng, Xiaoyun Zhang, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24403v1.pdf)  
  Keywords: compression, geometry, 3d gaussian, ar, compact, gaussian splatting, lightweight, high-fidelity  
- **[SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization](https://arxiv.org/abs/2607.20813v1)**  
  Authors: Jiun Lee, Jaekwang Kim, Sangmin Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20813v1.pdf)  
  Keywords: efficient, ar, face, gaussian splatting, high-fidelity  

### Ray Tracing

- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: reflection, efficient, lighting, illumination, ar, face, gaussian splatting, ray tracing, relighting  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: reflection, human, geometry, 3d gaussian, dynamic, motion, ar, face, gaussian splatting, ray tracing, high-fidelity  
- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: human, geometry, ar, compact, gaussian splatting, ray casting  
- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869v1)**  
  Authors: Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30869v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gray)  
  Keywords: fast, 3d gaussian, ar, gaussian splatting, ray tracing  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: fast, reflection, efficient, geometry, 3d gaussian, ar, path tracing, gaussian splatting, ray tracing, real-time rendering  
- **[RenderFormer++: Scalable and Physically Grounded Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v1)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jinyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v1.pdf)  
  Keywords: illumination, neural rendering, ar, global illumination, compact, light transport  
- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: efficient, illumination, 3d gaussian, geometry, global illumination, ar, gaussian splatting, 3d reconstruction  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: illumination, ar, global illumination, gaussian splatting, high-fidelity  
- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314v1)**  
  Authors: Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11314v1.pdf)  
  Keywords: lighting, geometry, neural rendering, 3d gaussian, dynamic, motion, ar, lightweight, ray tracing, light transport, 3d reconstruction, relighting  
- **[PTIR-GS: Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606v3)**  
  Authors: Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09606v3.pdf)  
  Keywords: reflection, lighting, illumination, 3d gaussian, shadow, global illumination, ar, path tracing, compact, ray tracing, light transport, relighting  

### Relighting

*Showing the latest 50 out of 55 papers*

- **[DerainSplat: Feed-Forward Clean 3D Gaussian Splatting from Sparse Rainy Views](https://arxiv.org/abs/2608.02191v1)**  
  Authors: Fuzhen Jiang, Changyue Shi, Chuxiao Yang, Xinyuan Hu, Wenjie Ye, Minghao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02191v1.pdf)  
  Keywords: autonomous driving, nerf, geometry, illumination, 3d gaussian, ar, gaussian splatting  
- **[DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing](https://arxiv.org/abs/2608.01761v1)**  
  Authors: Siying Li, Ying Ni, Jie Sun, Jian Sun, Haotian Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01761v1.pdf)  
  Keywords: autonomous driving, compression, lighting, illumination, neural rendering, 3d gaussian, dynamic, ar, gaussian splatting, semantic, high-fidelity, relighting  
- **[Endo-NeRF++: Uncertainty-Aware Neural Rendering with Multi-Resolution Hash Encoding for Dynamic Surgical Scene Reconstruction](https://arxiv.org/abs/2607.27825v1)**  
  Authors: Gousia Habib, Laura Ruotsalainen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.27825v1.pdf)  
  Keywords: reflection, deformation, nerf, dynamic, neural rendering, ar  
- **[PanoLess: Environment Reconstruction from Partial Reflective Views](https://arxiv.org/abs/2607.25362v1)**  
  Authors: Ahitagni Das, Ashok Veeraraghavan, Vivek Boominathan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25362v1.pdf)  
  Keywords: reflection, illumination, ar, face, high-fidelity  
- **[Meshless Domain Randomization via Explicit Parameter Perturbation of 3D Gaussian Splatting](https://arxiv.org/abs/2607.22890v1)**  
  Authors: Felipe Nunes Carbone de Carvalho, Joyce de Morais Souza, Alan de Aguiar, Charles Morphy D. Santos, João Paulo Gois  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22890v1.pdf)  
  Keywords: efficient, illumination, 3d gaussian, ar, gaussian splatting  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: reflection, efficient, lighting, illumination, ar, face, gaussian splatting, ray tracing, relighting  
- **[Visual Relocalization from Sparse Views in Aliased and Low-Texture Environments via Novel View Synthesis](https://arxiv.org/abs/2607.22147v1)**  
  Authors: Maria Peribañez, Javier Civera, Rudolph Triebel, Riccardo Giubilato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22147v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DLR-RM/multimodal-gsplat-relocalization?style=social)](https://github.com/DLR-RM/multimodal-gsplat-relocalization)  
  Keywords: localization, geometry, illumination, 3d gaussian, motion, sparse view, ar, gaussian splatting  
- **[ECoNGS: Efficient Compressive Neural Gaussian Splats for Volume Visualization](https://arxiv.org/abs/2607.18466v1)**  
  Authors: Kaiyuan Tang, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18466v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/ECoNGS?style=social)](https://github.com/TouKaienn/ECoNGS)  
  Keywords: efficient, lighting, dynamic, ar, vr, compact, gaussian splatting, lightweight  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: tracking, mapping, geometry, dynamic, illumination, motion, 3d gaussian, outdoor, ar, vr  
- **[FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System](https://arxiv.org/abs/2607.17803v1)**  
  Authors: Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17803v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CPREgroup/FF-ProCams?style=social)](https://github.com/CPREgroup/FF-ProCams)  
  Keywords: mapping, illumination, 3d gaussian, ar, face, gaussian splatting, head, lightweight, relightable, high-fidelity, 3d reconstruction  

### SLAM

*Showing the latest 50 out of 76 papers*

- **[TRACE: Ergodic Trajectory Optimization for Active Scene Reconstruction](https://arxiv.org/abs/2608.02304v1)**  
  Authors: Ziyue Zheng, Linli Shi, Bingkun He, Wen Jiang, Ziyun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02304v1.pdf) | [![GitHub](https://img.shields.io/github/stars/spikelab-jhu/trace-active-reconstruction?style=social)](https://github.com/spikelab-jhu/trace-active-reconstruction)  
  Keywords: ar, efficient, mapping  
- **[Swimm3R: Splatting with Medium-aware SfM for Underwater 3D Reconstruction](https://arxiv.org/abs/2608.00950v1)**  
  Authors: Minseong Kweon, Junaed Sattar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00950v1.pdf)  
  Keywords: localization, geometry, ar, motion, gaussian splatting, head, 3d reconstruction  
- **[Stipple: Real-Time Incremental Gaussian Splatting with Visual-Inertial Tracking](https://arxiv.org/abs/2608.00931v1)**  
  Authors: Kilian Northoff, Mateo de Mayo, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00931v1.pdf)  
  Keywords: localization, robotics, efficient rendering, tracking, efficient, mapping, 3d gaussian, ar, gaussian splatting, slam, 3d reconstruction  
- **[MonoVoc: Decoupling Geometry and Semantics for Lightweight Monocular Open-Vocabulary 3D Gaussians](https://arxiv.org/abs/2607.28300v1)**  
  Authors: Pouya Ardekhani, Zahra Dehghanian, Morteza Abolghasemi, Hamid R. Rabiee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28300v1.pdf)  
  Keywords: efficient, segmentation, geometry, 3d gaussian, understanding, mapping, ar, compact, head, lightweight, semantic  
- **[Split and Drive: Dual-Axis Disentanglement for Real-Time Gaussian Head Avatars](https://arxiv.org/abs/2607.28032v1)**  
  Authors: MD Wahiduzzaman Khan, Mingshan Jia, Xiaolin Zhang, En Yu, Kaska Musial-Gabrys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28032v1.pdf)  
  Keywords: fast, human, tracking, avatar, 3d gaussian, ar, gaussian splatting, head  
- **[AtlasLC: Fast Codec-Ready Compression of Object-Centric 3D Gaussian Splatting](https://arxiv.org/abs/2607.26525v1)**  
  Authors: ByungHyun Kim, Jinwoo Jeon, Woontack Woo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26525v1.pdf)  
  Keywords: fast, compression, mapping, geometry, 3d gaussian, semantic, ar, compact, gaussian splatting, lightweight, real-time rendering  
- **[Head Avatars with Dynamic Explicit Hair](https://arxiv.org/abs/2607.23861v1)**  
  Authors: Vanessa Sklyarova, Haonan Chen, Berna Kabadayi, Tobias Kirschstein, Zicong Fan, Xi Wang, Gerard Pons-Moll, Matthias Nießner, Marc Pollefeys, Michael J. Black, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.23861v1.pdf)  
  Keywords: deformation, human, tracking, avatar, dynamic, 3d gaussian, ar, acceleration, motion, face, gaussian splatting, head  
- **[Visual Relocalization from Sparse Views in Aliased and Low-Texture Environments via Novel View Synthesis](https://arxiv.org/abs/2607.22147v1)**  
  Authors: Maria Peribañez, Javier Civera, Rudolph Triebel, Riccardo Giubilato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22147v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DLR-RM/multimodal-gsplat-relocalization?style=social)](https://github.com/DLR-RM/multimodal-gsplat-relocalization)  
  Keywords: localization, geometry, illumination, 3d gaussian, motion, sparse view, ar, gaussian splatting  
- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: localization, tracking, mapping, outdoor, geometry, 3d gaussian, ar, gaussian splatting, lightweight, slam  
- **[FlexiAvatar: Unified 3D Gaussian Human Avatars Under Arbitrary Body Visibility](https://arxiv.org/abs/2607.19100v1)**  
  Authors: Yihalem Yimolal Tiruneh, Muhammad Salman Ali, Uyoung Jeong, Muneeb A. Khan, MD Khalequzzaman Chowdhury Sayem, Allanur Bayramgeldiyev, Binod Bhattarai, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19100v1.pdf)  
  Keywords: human, tracking, avatar, neural rendering, 3d gaussian, ar, vr, gaussian splatting, head, body  

### Scene Understanding

*Showing the latest 50 out of 119 papers*

- **[3DGSI-Assessor: A Large-Scale Dataset and An LMM-based Method for 3D Gaussian Splatting Image Quality Assessment](https://arxiv.org/abs/2608.03279v1)**  
  Authors: Yuke Xing, Jiarui Wang, William Gordon, Zhu Li, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03279v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YukeXing/3DGSI-Assessor?style=social)](https://github.com/YukeXing/3DGSI-Assessor)  
  Keywords: compression, geometry, 3d gaussian, ar, face, gaussian splatting, semantic  
- **[Standalone DINOv3 for Training-Free Open-Vocabulary Semantic Segmentation in Remote Sensing](https://arxiv.org/abs/2608.03023v1)**  
  Authors: Changhao Zhao, Haoxiang Li, Yuke Li, Hai Liu, LingLin Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03023v1.pdf)  
  Keywords: ar, segmentation, semantic, gaussian splatting  
- **[3D Gaussian Splatting and Mesh-Based Digital Twins: An Exploratory Study for Virtual Reality Tourism](https://arxiv.org/abs/2608.01969v1)**  
  Authors: Maximilian Warsinke, Francesco Vona, Abm Tariqul Islam, Tanja Kojić, Jan-Niklas Voigt-Antons, Sebastian Möller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01969v1.pdf)  
  Keywords: 3d gaussian, ar, motion, vr, gaussian splatting, understanding, high-fidelity  
- **[DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing](https://arxiv.org/abs/2608.01761v1)**  
  Authors: Siying Li, Ying Ni, Jie Sun, Jian Sun, Haotian Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01761v1.pdf)  
  Keywords: autonomous driving, compression, lighting, illumination, neural rendering, 3d gaussian, dynamic, ar, gaussian splatting, semantic, high-fidelity, relighting  
- **[QuerySplat: Decoupling Geometry and Appearance Representations in 3DGS Prediction](https://arxiv.org/abs/2608.01186v1)**  
  Authors: Yinglong Li, Donghui Shen, Xiaoyu Zhang, Zhichao Ye, Hongyu Wu, Aimin Hao, Guofeng Zhang, Haomin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01186v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://inspatio.github.io/querysplat)  
  Keywords: efficient, geometry, 3d gaussian, ar, gaussian splatting, understanding, high-fidelity, 3d reconstruction  
- **[MonoVoc: Decoupling Geometry and Semantics for Lightweight Monocular Open-Vocabulary 3D Gaussians](https://arxiv.org/abs/2607.28300v1)**  
  Authors: Pouya Ardekhani, Zahra Dehghanian, Morteza Abolghasemi, Hamid R. Rabiee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28300v1.pdf)  
  Keywords: efficient, segmentation, geometry, 3d gaussian, understanding, mapping, ar, compact, head, lightweight, semantic  
- **[StructureGS: Structure-aware Gaussian Splatting for Articulated Object Reconstruction](https://arxiv.org/abs/2607.26889v1)**  
  Authors: Gahye Lee, Gyoonseo Kim, Wonjong Jang, Jooeun Son, Seungyong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26889v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, motion, compact, gaussian splatting, understanding  
- **[SpatialQ: Understanding 3D Gaussian Splatting Scene Quality via Visual-based MLLM](https://arxiv.org/abs/2607.26595v1)**  
  Authors: Jingxuan Su, Shenglin Wang, Tiesong Zhao, Ge Li, Wei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26595v1.pdf)  
  Keywords: understanding, 3d gaussian, ar, gaussian splatting, head  
- **[AtlasLC: Fast Codec-Ready Compression of Object-Centric 3D Gaussian Splatting](https://arxiv.org/abs/2607.26525v1)**  
  Authors: ByungHyun Kim, Jinwoo Jeon, Woontack Woo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26525v1.pdf)  
  Keywords: fast, compression, mapping, geometry, 3d gaussian, semantic, ar, compact, gaussian splatting, lightweight, real-time rendering  
- **[SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation](https://arxiv.org/abs/2607.25219v1)**  
  Authors: Weiqi Huang, Dianyi Yang, Jiaxin Li, Shuangyi Dong, Hao Xu, Zan Wang, Wei Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25219v1.pdf)  
  Keywords: human, avatar, 3d gaussian, ar, motion, gaussian splatting, body, semantic  



## Classic Papers
- **[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)** (SIGGRAPH 2023)  
  Authors: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis  
  Code: 🔗 [GitHub](https://github.com/graphdeco-inria/gaussian-splatting)  
  Keywords: Real-time Rendering, Neural Rendering, Point-based Graphics

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