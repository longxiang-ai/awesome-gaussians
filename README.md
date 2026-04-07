# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-04-07 01:21:46

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

- [3DGS Surveys](#3dgs-surveys) (5 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (114 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (159 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (207 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (33 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (210 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (17 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (213 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (131 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (21 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (73 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (76 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (131 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Nevis Digital Twin: Photogrammetry and Immersive Visualization of Historical Sites](https://arxiv.org/abs/2603.20560v1)**  
  Authors: Alex Apffel, Huy Tran, Vuthea Chheang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20560v1.pdf)  
  Keywords: ar, survey, 3d gaussian, vr, gaussian splatting  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: ar, survey, mapping, 3d gaussian, gaussian splatting, ray tracing  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: efficient, motion, dynamic, tracking, localization, face, ar, survey, mapping, 3d gaussian, gaussian splatting, slam  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: ar, survey, 3d gaussian, robotics, gaussian splatting  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v3)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v3.pdf)  
  Keywords: efficient, geometry, ar, survey, 3d gaussian, gaussian splatting, nerf  

### Acceleration

*Showing the latest 50 out of 114 papers*

- **[TrackerSplat: Exploiting Point Tracking for Fast and Robust Dynamic 3D Gaussians Reconstruction](https://arxiv.org/abs/2604.02586v1)**  
  Authors: Daheng Yin, Isaac Ding, Yili Jin, Jianxin Shi, Jiangchuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02586v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yindaheng98/TrackerSplat?style=social)](https://github.com/yindaheng98/TrackerSplat)  
  Keywords: efficient, motion, dynamic, tracking, ar, 3d gaussian, robotics, gaussian splatting, 3d reconstruction, fast  
- **[GEMM-GS: Accelerating 3D Gaussian Splatting on Tensor Cores with GEMM-Compatible Blending](https://arxiv.org/abs/2604.02120v1)**  
  Authors: Haomin Li, Bowen Zhu, Fangxin Liu, Zongwu Wang, Xinran Liang, Li Jiang, Haibing Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02120v1.pdf) | [![GitHub](https://img.shields.io/github/stars/shieldforever/GEMM-GS?style=social)](https://github.com/shieldforever/GEMM-GS)  
  Keywords: gaussian splatting, 3d gaussian, nerf, acceleration  
- **[GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2604.01884v1)**  
  Authors: Xianben Yang, Tao Wang, Yuxuan Li, Yi Jin, Haibin Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01884v1.pdf)  
  Keywords: real-time rendering, dynamic, ar, 3d gaussian, compact, gaussian splatting  
- **[FaCT-GS: Fast and Scalable CT Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2604.01844v1)**  
  Authors: Pawel Tomasz Pieta, Rasmus Juul Pedersen, Sina Borgi, Jakob Sauer Jørgensen, Jens Wenzel Andreasen, Vedrana Andersen Dahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01844v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PaPieta/fact-gs?style=social)](https://github.com/PaPieta/fact-gs)  
  Keywords: ar, gaussian splatting, fast  
- **[Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty-aware Differentiable Optimization](https://arxiv.org/abs/2604.01030v1)**  
  Authors: Yueh-Cheng Liu, Jozef Hladký, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01030v1.pdf)  
  Keywords: ar, 3d gaussian, sparse-view, gaussian splatting, fast  
- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394v1)**  
  Authors: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29394v1.pdf)  
  Keywords: ar, 3d gaussian, sparse-view, gaussian splatting, 3d reconstruction, fast  
- **[LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2603.28431v3)**  
  Authors: Xuan Deng, Xiandong Meng, Hengyu Man, Qiang Zhu, Tiange Zhang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28431v3.pdf)  
  Keywords: real-time rendering, geometry, compression, head, ar, high-fidelity, 3d gaussian, compact, gaussian splatting, nerf, lightweight  
- **[ObjectMorpher: 3D-Aware Image Editing via Deformable 3DGS Models](https://arxiv.org/abs/2603.28152v1)**  
  Authors: Yuhuan Xie, Aoxuan Pan, Yi-Hua Huang, Chirui Chang, Peng Dai, Xin Yu, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28152v1.pdf)  
  Keywords: geometry, deformation, ar, lighting, 3d gaussian, gaussian splatting, fast  
- **[Physically Inspired Gaussian Splatting for HDR Novel View Synthesis](https://arxiv.org/abs/2603.28020v1)**  
  Authors: Huimin Zeng, Yue Bai, Hailing Wang, Yun Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huimin-zeng.github.io/PhysHDR-GS)  
  Keywords: real-time rendering, dynamic, illumination, ar, gaussian splatting  
- **[DiffSoup: Direct Differentiable Rasterization of Triangle Soup for Extreme Radiance Field Simplification](https://arxiv.org/abs/2603.27151v1)**  
  Authors: Kenji Tojo, Bernd Bickel, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27151v1.pdf) | [![GitHub](https://img.shields.io/github/stars/kenji-tojo/diffsoup?style=social)](https://github.com/kenji-tojo/diffsoup)  
  Keywords: efficient, real-time rendering, ar, 3d gaussian, gaussian splatting  

### Applications

*Showing the latest 50 out of 498 papers*

- **[4C4D: 4 Camera 4D Gaussian Splatting](https://arxiv.org/abs/2604.04063v1)**  
  Authors: Junsheng Zhou, Zhifan Yang, Liang Han, Wenyuan Zhang, Kanle Shi, Shenkun Xu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04063v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://junshengzhou.github.io/4C4D)  
  Keywords: 4d, dynamic, geometry, ar, high-fidelity, sparse-view, gaussian splatting  
- **[HOIGS: Human-Object Interaction Gaussian Splatting](https://arxiv.org/abs/2604.04016v1)**  
  Authors: Taewoo Kim, Suwoong Yeom, Jaehyun Pyun, Geonho Cha, Dongyoon Wee, Joonsik Nam, Yun-Seong Jeong, Kyeongbo Kong, Suk-Ju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04016v1.pdf)  
  Keywords: motion, 4d, dynamic, deformation, human, ar, high-fidelity, lighting, gaussian splatting  
- **[M2StyleGS: Multi-Modality 3D Style Transfer with Gaussian Splatting](https://arxiv.org/abs/2604.03773v1)**  
  Authors: Xingyu Miao, Xueqi Qiu, Haoran Duan, Yawen Huang, Xian Wu, Jingjing Deng, Yang Long  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03773v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian  
- **[CGHair: Compact Gaussian Hair Reconstruction with Card Clustering](https://arxiv.org/abs/2604.03716v1)**  
  Authors: Haimin Luo, Srinjay Sarkar, Albert Mosella-Montoro, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03716v1.pdf)  
  Keywords: geometry, ar, high-fidelity, 3d gaussian, compact, gaussian splatting  
- **[SpectralSplat: Appearance-Disentangled Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2604.03462v1)**  
  Authors: Quentin Herau, Tianshuo Xu, Depu Meng, Jiezhi Yang, Chensheng Peng, Spencer Sherk, Yihan Hu, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03462v1.pdf)  
  Keywords: relighting, geometry, ar, lighting, 3d gaussian, autonomous driving, gaussian splatting  
- **[Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM](https://arxiv.org/abs/2604.03092v1)**  
  Authors: Zicheng Zhang, Ke Wu, Xiangting Meng, Keyu Liu, Jieru Zhao, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://victkk.github.io/flash-mono)  
  Keywords: efficient, geometry, tracking, ar, lighting, mapping, 3d gaussian, compact, gaussian splatting, slam  
- **[SparseSplat: Towards Applicable Feed-Forward 3D Gaussian Splatting with Pixel-Unaligned Prediction](https://arxiv.org/abs/2604.03069v1)**  
  Authors: Zicheng Zhang, Xiangting Meng, Ke Wu, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03069v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://victkk.github.io/SparseSplat-page)  
  Keywords: efficient, ar, 3d gaussian, compact, gaussian splatting  
- **[GenSmoke-GS: A Multi-Stage Method for Novel View Synthesis from Smoke-Degraded Images Using a Generative Model](https://arxiv.org/abs/2604.03039v1)**  
  Authors: Qida Cao, Xinyuan Hu, Changyue Shi, Jiajun Ding, Zhou Yu, Jun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03039v1.pdf) | [![GitHub](https://img.shields.io/github/stars/plbbl/GenSmoke-GS?style=social)](https://github.com/plbbl/GenSmoke-GS) | [![Project](https://img.shields.io/badge/-Project-blue)](https://www.codabench.org/competitions/13993/#/results-tab)  
  Keywords: ar  
- **[Rendering Multi-Human and Multi-Object with 3D Gaussian Splatting](https://arxiv.org/abs/2604.02996v1)**  
  Authors: Weiquan Wang, Jun Xiao, Feifei Shao, Yi Yang, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02996v1.pdf)  
  Keywords: dynamic, human, ar, high-fidelity, 3d gaussian, robotics, sparse-view, vr, gaussian splatting  
- **[GP-4DGS: Probabilistic 4D Gaussian Splatting from Monocular Video via Variational Gaussian Processes](https://arxiv.org/abs/2604.02915v1)**  
  Authors: Mijeong Kim, Jungtaek Kim, Bohyung Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02915v1.pdf)  
  Keywords: motion, 4d, dynamic, deformation, ar, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 159 papers*

- **[HOIGS: Human-Object Interaction Gaussian Splatting](https://arxiv.org/abs/2604.04016v1)**  
  Authors: Taewoo Kim, Suwoong Yeom, Jaehyun Pyun, Geonho Cha, Dongyoon Wee, Joonsik Nam, Yun-Seong Jeong, Kyeongbo Kong, Suk-Ju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04016v1.pdf)  
  Keywords: motion, 4d, dynamic, deformation, human, ar, high-fidelity, lighting, gaussian splatting  
- **[Rendering Multi-Human and Multi-Object with 3D Gaussian Splatting](https://arxiv.org/abs/2604.02996v1)**  
  Authors: Weiquan Wang, Jun Xiao, Feifei Shao, Yi Yang, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02996v1.pdf)  
  Keywords: dynamic, human, ar, high-fidelity, 3d gaussian, robotics, sparse-view, vr, gaussian splatting  
- **[UNICA: A Unified Neural Framework for Controllable 3D Avatars](https://arxiv.org/abs/2604.02799v1)**  
  Authors: Jiahe Zhu, Xinyao Wang, Yiyu Zhuang, Yanwen Wang, Jing Tian, Yao Yao, Hao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02799v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zjh21/UNICA?style=social)](https://github.com/zjh21/UNICA)  
  Keywords: motion, dynamic, geometry, human, ar, high-fidelity, avatar, 3d gaussian, vr, gaussian splatting  
- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: motion, 4d, dynamic, deformation, head, segmentation, high-fidelity, ar, 3d gaussian, gaussian splatting, lightweight  
- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: semantic, motion, 4d, dynamic, geometry, human, face, high-fidelity, segmentation, ar, understanding, gaussian splatting, tracking  
- **[F3DGS: Federated 3D Gaussian Splatting for Decentralized Multi-Agent World Modeling](https://arxiv.org/abs/2604.01605v1)**  
  Authors: Morui Zhu, Mohammad Dehghani Tezerjani, Mátyás Szántó, Márton Vaitkus, Song Fu, Qing Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01605v1.pdf)  
  Keywords: efficient, head, ar, 3d gaussian, gaussian splatting, 3d reconstruction  
- **[Better Rigs, Not Bigger Networks: A Body Model Ablation for Gaussian Avatars](https://arxiv.org/abs/2604.01447v2)**  
  Authors: Derek Austin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01447v2.pdf)  
  Keywords: human, deformation, ar, avatar, body, 3d gaussian, gaussian splatting  
- **[LESV: Language Embedded Sparse Voxel Fusion for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2604.01388v1)**  
  Authors: Fusang Wang, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Fabien Moutarde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01388v1.pdf)  
  Keywords: semantic, geometry, head, ar, 3d gaussian, vr, understanding, gaussian splatting  
- **[Autoregressive Appearance Prediction for 3D Gaussian Avatars](https://arxiv.org/abs/2604.00928v1)**  
  Authors: Michael Steiner, Zhang Chen, Alexander Richard, Vasu Agrawal, Markus Steinberger, Michael Zollhöfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00928v1.pdf)  
  Keywords: motion, dynamic, human, ar, high-fidelity, avatar, 3d gaussian, compact, gaussian splatting  
- **[TRiGS: Temporal Rigid-Body Motion for Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2604.00538v1)**  
  Authors: Suwoong Yeom, Joonsik Nam, Seunggyu Choi, Lucas Yunkyu Lee, Sangmin Kim, Jaesik Park, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong, Sukju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00538v1.pdf)  
  Keywords: motion, 4d, dynamic, ar, body, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 207 papers*

- **[4C4D: 4 Camera 4D Gaussian Splatting](https://arxiv.org/abs/2604.04063v1)**  
  Authors: Junsheng Zhou, Zhifan Yang, Liang Han, Wenyuan Zhang, Kanle Shi, Shenkun Xu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04063v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://junshengzhou.github.io/4C4D)  
  Keywords: 4d, dynamic, geometry, ar, high-fidelity, sparse-view, gaussian splatting  
- **[HOIGS: Human-Object Interaction Gaussian Splatting](https://arxiv.org/abs/2604.04016v1)**  
  Authors: Taewoo Kim, Suwoong Yeom, Jaehyun Pyun, Geonho Cha, Dongyoon Wee, Joonsik Nam, Yun-Seong Jeong, Kyeongbo Kong, Suk-Ju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04016v1.pdf)  
  Keywords: motion, 4d, dynamic, deformation, human, ar, high-fidelity, lighting, gaussian splatting  
- **[Rendering Multi-Human and Multi-Object with 3D Gaussian Splatting](https://arxiv.org/abs/2604.02996v1)**  
  Authors: Weiquan Wang, Jun Xiao, Feifei Shao, Yi Yang, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02996v1.pdf)  
  Keywords: dynamic, human, ar, high-fidelity, 3d gaussian, robotics, sparse-view, vr, gaussian splatting  
- **[GP-4DGS: Probabilistic 4D Gaussian Splatting from Monocular Video via Variational Gaussian Processes](https://arxiv.org/abs/2604.02915v1)**  
  Authors: Mijeong Kim, Jungtaek Kim, Bohyung Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02915v1.pdf)  
  Keywords: motion, 4d, dynamic, deformation, ar, gaussian splatting  
- **[Streaming Real-Time Rendered Scenes as 3D Gaussians](https://arxiv.org/abs/2604.02851v1)**  
  Authors: Matti Siekkinen, Teemu Kämäräinen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02851v1.pdf)  
  Keywords: relighting, dynamic, ar, lighting, 3d gaussian, gaussian splatting  
- **[UNICA: A Unified Neural Framework for Controllable 3D Avatars](https://arxiv.org/abs/2604.02799v1)**  
  Authors: Jiahe Zhu, Xinyao Wang, Yiyu Zhuang, Yanwen Wang, Jing Tian, Yao Yao, Hao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02799v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zjh21/UNICA?style=social)](https://github.com/zjh21/UNICA)  
  Keywords: motion, dynamic, geometry, human, ar, high-fidelity, avatar, 3d gaussian, vr, gaussian splatting  
- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2604.02781v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02781v1.pdf)  
  Keywords: semantic, dynamic, geometry, 3d gaussian, gaussian splatting, reflection  
- **[TrackerSplat: Exploiting Point Tracking for Fast and Robust Dynamic 3D Gaussians Reconstruction](https://arxiv.org/abs/2604.02586v1)**  
  Authors: Daheng Yin, Isaac Ding, Yili Jin, Jianxin Shi, Jiangchuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02586v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yindaheng98/TrackerSplat?style=social)](https://github.com/yindaheng98/TrackerSplat)  
  Keywords: efficient, motion, dynamic, tracking, ar, 3d gaussian, robotics, gaussian splatting, 3d reconstruction, fast  
- **[ProDiG: Progressive Diffusion-Guided Gaussian Splatting for Aerial to Ground Reconstruction](https://arxiv.org/abs/2604.02003v1)**  
  Authors: Sirshapan Mitra, Yogesh S. Rawat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02003v1.pdf)  
  Keywords: ar, gaussian splatting, dynamic, geometry  
- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: motion, 4d, dynamic, deformation, head, segmentation, high-fidelity, ar, 3d gaussian, gaussian splatting, lightweight  

### Few-shot

- **[4C4D: 4 Camera 4D Gaussian Splatting](https://arxiv.org/abs/2604.04063v1)**  
  Authors: Junsheng Zhou, Zhifan Yang, Liang Han, Wenyuan Zhang, Kanle Shi, Shenkun Xu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04063v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://junshengzhou.github.io/4C4D)  
  Keywords: 4d, dynamic, geometry, ar, high-fidelity, sparse-view, gaussian splatting  
- **[Rendering Multi-Human and Multi-Object with 3D Gaussian Splatting](https://arxiv.org/abs/2604.02996v1)**  
  Authors: Weiquan Wang, Jun Xiao, Feifei Shao, Yi Yang, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02996v1.pdf)  
  Keywords: dynamic, human, ar, high-fidelity, 3d gaussian, robotics, sparse-view, vr, gaussian splatting  
- **[TRACE: High-Fidelity 3D Scene Editing via Tangible Reconstruction and Geometry-Aligned Contextual Video Masking](https://arxiv.org/abs/2604.01207v1)**  
  Authors: Jiyuan Hu, Zechuan Zhang, Zongxin Yang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01207v1.pdf)  
  Keywords: ar, high-fidelity, geometry, sparse-view  
- **[Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty-aware Differentiable Optimization](https://arxiv.org/abs/2604.01030v1)**  
  Authors: Yueh-Cheng Liu, Jozef Hladký, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01030v1.pdf)  
  Keywords: ar, 3d gaussian, sparse-view, gaussian splatting, fast  
- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394v1)**  
  Authors: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29394v1.pdf)  
  Keywords: ar, 3d gaussian, sparse-view, gaussian splatting, 3d reconstruction, fast  
- **[\textit{4DSurf}: High-Fidelity Dynamic Scene Surface Reconstruction](https://arxiv.org/abs/2603.28064v1)**  
  Authors: Renjie Wu, Hongdong Li, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28064v1.pdf)  
  Keywords: motion, 4d, dynamic, geometry, deformation, face, high-fidelity, ar, sparse-view, gaussian splatting  
- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516v2)**  
  Authors: Jiahao Niu, Rongjia Zheng, Wenju Xu, Wei-Shi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27516v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GrumpySloths/SGS_Intrinsic.github.io?style=social)](https://github.com/GrumpySloths/SGS_Intrinsic.github.io)  
  Keywords: semantic, geometry, illumination, shadow, ar, sparse view, 3d gaussian, sparse-view, gaussian splatting  
- **[Detailed Geometry and Appearance from Opportunistic Motion](https://arxiv.org/abs/2603.26665v1)**  
  Authors: Ryosuke Hirai, Kohei Yamashita, Antoine Guédon, Ryo Kawahara, Vincent Lepetit, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26665v1.pdf)  
  Keywords: motion, geometry, illumination, ar, sparse view, gaussian splatting  
- **[AirSplat: Alignment and Rating for Robust Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.25129v1)**  
  Authors: Minh-Quan Viet Bui, Jaeho Moon, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25129v1.pdf)  
  Keywords: geometry, ar, high-fidelity, 3d gaussian, sparse-view, gaussian splatting  
- **[EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](https://arxiv.org/abs/2603.21332v2)**  
  Authors: Haolan Xu, Keli Cheng, Lei Wang, Ning Bi, Xiaoming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21332v2.pdf)  
  Keywords: motion, head, face, ar, lighting, few-shot, 3d gaussian, gaussian splatting, nerf  

### Geometry Reconstruction

*Showing the latest 50 out of 210 papers*

- **[4C4D: 4 Camera 4D Gaussian Splatting](https://arxiv.org/abs/2604.04063v1)**  
  Authors: Junsheng Zhou, Zhifan Yang, Liang Han, Wenyuan Zhang, Kanle Shi, Shenkun Xu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04063v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://junshengzhou.github.io/4C4D)  
  Keywords: 4d, dynamic, geometry, ar, high-fidelity, sparse-view, gaussian splatting  
- **[CGHair: Compact Gaussian Hair Reconstruction with Card Clustering](https://arxiv.org/abs/2604.03716v1)**  
  Authors: Haimin Luo, Srinjay Sarkar, Albert Mosella-Montoro, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03716v1.pdf)  
  Keywords: geometry, ar, high-fidelity, 3d gaussian, compact, gaussian splatting  
- **[SpectralSplat: Appearance-Disentangled Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2604.03462v1)**  
  Authors: Quentin Herau, Tianshuo Xu, Depu Meng, Jiezhi Yang, Chensheng Peng, Spencer Sherk, Yihan Hu, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03462v1.pdf)  
  Keywords: relighting, geometry, ar, lighting, 3d gaussian, autonomous driving, gaussian splatting  
- **[Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM](https://arxiv.org/abs/2604.03092v1)**  
  Authors: Zicheng Zhang, Ke Wu, Xiangting Meng, Keyu Liu, Jieru Zhao, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://victkk.github.io/flash-mono)  
  Keywords: efficient, geometry, tracking, ar, lighting, mapping, 3d gaussian, compact, gaussian splatting, slam  
- **[NavCrafter: Exploring 3D Scenes from a Single Image](https://arxiv.org/abs/2604.02828v1)**  
  Authors: Hongbo Duan, Peiyu Zhuang, Yi Liu, Zhengyang Zhang, Yuxin Zhang, Pengting Luo, Fangming Liu, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02828v1.pdf)  
  Keywords: geometry, ar, 3d gaussian, gaussian splatting, 3d reconstruction  
- **[UNICA: A Unified Neural Framework for Controllable 3D Avatars](https://arxiv.org/abs/2604.02799v1)**  
  Authors: Jiahe Zhu, Xinyao Wang, Yiyu Zhuang, Yanwen Wang, Jing Tian, Yao Yao, Hao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02799v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zjh21/UNICA?style=social)](https://github.com/zjh21/UNICA)  
  Keywords: motion, dynamic, geometry, human, ar, high-fidelity, avatar, 3d gaussian, vr, gaussian splatting  
- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2604.02781v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02781v1.pdf)  
  Keywords: semantic, dynamic, geometry, 3d gaussian, gaussian splatting, reflection  
- **[TrackerSplat: Exploiting Point Tracking for Fast and Robust Dynamic 3D Gaussians Reconstruction](https://arxiv.org/abs/2604.02586v1)**  
  Authors: Daheng Yin, Isaac Ding, Yili Jin, Jianxin Shi, Jiangchuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02586v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yindaheng98/TrackerSplat?style=social)](https://github.com/yindaheng98/TrackerSplat)  
  Keywords: efficient, motion, dynamic, tracking, ar, 3d gaussian, robotics, gaussian splatting, 3d reconstruction, fast  
- **[ProDiG: Progressive Diffusion-Guided Gaussian Splatting for Aerial to Ground Reconstruction](https://arxiv.org/abs/2604.02003v1)**  
  Authors: Sirshapan Mitra, Yogesh S. Rawat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02003v1.pdf)  
  Keywords: ar, gaussian splatting, dynamic, geometry  
- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: semantic, motion, 4d, dynamic, geometry, human, face, high-fidelity, segmentation, ar, understanding, gaussian splatting, tracking  

### Large Scene

- **[Neural Harmonic Textures for High-Quality Primitive Based Neural Reconstruction](https://arxiv.org/abs/2604.01204v1)**  
  Authors: Jorge Condor, Nicolas Moenne-Loccoz, Merlin Nimier-David, Piotr Didyk, Zan Gojcic, Qi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01204v1.pdf)  
  Keywords: semantic, large scene, ar, 3d gaussian, gaussian splatting  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: efficient, motion, large scene, geometry, dynamic, 4d, shadow, ar, high-fidelity, neural rendering, understanding, gaussian splatting  
- **[Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting](https://arxiv.org/abs/2603.29185v1)**  
  Authors: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29185v1.pdf)  
  Keywords: efficient, localization, ar, gaussian splatting, outdoor  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: efficient, large scene, head, face, ar, neural rendering, 3d gaussian, gaussian splatting  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: efficient, dynamic, head, tracking, ar, gaussian splatting, slam, outdoor  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: geometry, localization, ar, 3d gaussian, gaussian splatting, outdoor  
- **[EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.06216v1)**  
  Authors: Miriam Jäger, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06216v1.pdf)  
  Keywords: urban scene, geometry, face, ar, 3d gaussian, gaussian splatting, 3d reconstruction  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: relighting, outdoor, relightable, illumination, ar, lighting, 3d gaussian, gaussian splatting, 3d reconstruction, nerf, reflection, fast  
- **[Interactive Augmented Reality-enabled Outdoor Scene Visualization For Enhanced Real-time Disaster Response](https://arxiv.org/abs/2602.21874v1)**  
  Authors: Dimitrios Apostolakis, Georgios Angelidis, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21874v1.pdf)  
  Keywords: fast, semantic, face, ar, lighting, 3d gaussian, gaussian splatting, lightweight, outdoor  
- **[Large-scale Photorealistic Outdoor 3D Scene Reconstruction from UAV Imagery Using Gaussian Splatting Techniques](https://arxiv.org/abs/2602.20342v1)**  
  Authors: Christos Maikos, Georgios Angelidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20342v1.pdf)  
  Keywords: efficient, ar, high-fidelity, neural rendering, 3d gaussian, vr, gaussian splatting, 3d reconstruction, nerf, outdoor  

### Model Compression

*Showing the latest 50 out of 213 papers*

- **[CGHair: Compact Gaussian Hair Reconstruction with Card Clustering](https://arxiv.org/abs/2604.03716v1)**  
  Authors: Haimin Luo, Srinjay Sarkar, Albert Mosella-Montoro, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03716v1.pdf)  
  Keywords: geometry, ar, high-fidelity, 3d gaussian, compact, gaussian splatting  
- **[Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM](https://arxiv.org/abs/2604.03092v1)**  
  Authors: Zicheng Zhang, Ke Wu, Xiangting Meng, Keyu Liu, Jieru Zhao, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://victkk.github.io/flash-mono)  
  Keywords: efficient, geometry, tracking, ar, lighting, mapping, 3d gaussian, compact, gaussian splatting, slam  
- **[SparseSplat: Towards Applicable Feed-Forward 3D Gaussian Splatting with Pixel-Unaligned Prediction](https://arxiv.org/abs/2604.03069v1)**  
  Authors: Zicheng Zhang, Xiangting Meng, Ke Wu, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03069v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://victkk.github.io/SparseSplat-page)  
  Keywords: efficient, ar, 3d gaussian, compact, gaussian splatting  
- **[Differentiable Stroke Planning with Dual Parameterization for Efficient and High-Fidelity Painting Creation](https://arxiv.org/abs/2604.02752v1)**  
  Authors: Jinfan Liu, Wuze Zhang, Zhangli Hu, Zhehan Zhao, Ye Chen, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02752v1.pdf)  
  Keywords: efficient, ar, high-fidelity, mapping  
- **[VBGS-SLAM: Variational Bayesian Gaussian Splatting Simultaneous Localization and Mapping](https://arxiv.org/abs/2604.02696v1)**  
  Authors: Yuhan Zhu, Yanyu Zhang, Jie Xu, Wei Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02696v1.pdf)  
  Keywords: efficient, tracking, localization, ar, mapping, 3d gaussian, gaussian splatting, slam  
- **[TrackerSplat: Exploiting Point Tracking for Fast and Robust Dynamic 3D Gaussians Reconstruction](https://arxiv.org/abs/2604.02586v1)**  
  Authors: Daheng Yin, Isaac Ding, Yili Jin, Jianxin Shi, Jiangchuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02586v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yindaheng98/TrackerSplat?style=social)](https://github.com/yindaheng98/TrackerSplat)  
  Keywords: efficient, motion, dynamic, tracking, ar, 3d gaussian, robotics, gaussian splatting, 3d reconstruction, fast  
- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: motion, 4d, dynamic, deformation, head, segmentation, high-fidelity, ar, 3d gaussian, gaussian splatting, lightweight  
- **[GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2604.01884v1)**  
  Authors: Xianben Yang, Tao Wang, Yuxuan Li, Yi Jin, Haibin Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01884v1.pdf)  
  Keywords: real-time rendering, dynamic, ar, 3d gaussian, compact, gaussian splatting  
- **[F3DGS: Federated 3D Gaussian Splatting for Decentralized Multi-Agent World Modeling](https://arxiv.org/abs/2604.01605v1)**  
  Authors: Morui Zhu, Mohammad Dehghani Tezerjani, Mátyás Szántó, Márton Vaitkus, Song Fu, Qing Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01605v1.pdf)  
  Keywords: efficient, head, ar, 3d gaussian, gaussian splatting, 3d reconstruction  
- **[Satellite-Free Training for Drone-View Geo-Localization](https://arxiv.org/abs/2604.01581v2)**  
  Authors: Tao Liu, Yingzhi Zhang, Kan Ren, Xiaoqi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01581v2.pdf)  
  Keywords: geometry, localization, ar, 3d gaussian, gaussian splatting, lightweight  

### Quality Enhancement

*Showing the latest 50 out of 131 papers*

- **[4C4D: 4 Camera 4D Gaussian Splatting](https://arxiv.org/abs/2604.04063v1)**  
  Authors: Junsheng Zhou, Zhifan Yang, Liang Han, Wenyuan Zhang, Kanle Shi, Shenkun Xu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04063v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://junshengzhou.github.io/4C4D)  
  Keywords: 4d, dynamic, geometry, ar, high-fidelity, sparse-view, gaussian splatting  
- **[HOIGS: Human-Object Interaction Gaussian Splatting](https://arxiv.org/abs/2604.04016v1)**  
  Authors: Taewoo Kim, Suwoong Yeom, Jaehyun Pyun, Geonho Cha, Dongyoon Wee, Joonsik Nam, Yun-Seong Jeong, Kyeongbo Kong, Suk-Ju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04016v1.pdf)  
  Keywords: motion, 4d, dynamic, deformation, human, ar, high-fidelity, lighting, gaussian splatting  
- **[CGHair: Compact Gaussian Hair Reconstruction with Card Clustering](https://arxiv.org/abs/2604.03716v1)**  
  Authors: Haimin Luo, Srinjay Sarkar, Albert Mosella-Montoro, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03716v1.pdf)  
  Keywords: geometry, ar, high-fidelity, 3d gaussian, compact, gaussian splatting  
- **[Rendering Multi-Human and Multi-Object with 3D Gaussian Splatting](https://arxiv.org/abs/2604.02996v1)**  
  Authors: Weiquan Wang, Jun Xiao, Feifei Shao, Yi Yang, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02996v1.pdf)  
  Keywords: dynamic, human, ar, high-fidelity, 3d gaussian, robotics, sparse-view, vr, gaussian splatting  
- **[UNICA: A Unified Neural Framework for Controllable 3D Avatars](https://arxiv.org/abs/2604.02799v1)**  
  Authors: Jiahe Zhu, Xinyao Wang, Yiyu Zhuang, Yanwen Wang, Jing Tian, Yao Yao, Hao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02799v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zjh21/UNICA?style=social)](https://github.com/zjh21/UNICA)  
  Keywords: motion, dynamic, geometry, human, ar, high-fidelity, avatar, 3d gaussian, vr, gaussian splatting  
- **[Differentiable Stroke Planning with Dual Parameterization for Efficient and High-Fidelity Painting Creation](https://arxiv.org/abs/2604.02752v1)**  
  Authors: Jinfan Liu, Wuze Zhang, Zhangli Hu, Zhehan Zhao, Ye Chen, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02752v1.pdf)  
  Keywords: efficient, ar, high-fidelity, mapping  
- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: motion, 4d, dynamic, deformation, head, segmentation, high-fidelity, ar, 3d gaussian, gaussian splatting, lightweight  
- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: semantic, motion, 4d, dynamic, geometry, human, face, high-fidelity, segmentation, ar, understanding, gaussian splatting, tracking  
- **[TRACE: High-Fidelity 3D Scene Editing via Tangible Reconstruction and Geometry-Aligned Contextual Video Masking](https://arxiv.org/abs/2604.01207v1)**  
  Authors: Jiyuan Hu, Zechuan Zhang, Zongxin Yang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01207v1.pdf)  
  Keywords: ar, high-fidelity, geometry, sparse-view  
- **[Autoregressive Appearance Prediction for 3D Gaussian Avatars](https://arxiv.org/abs/2604.00928v1)**  
  Authors: Michael Steiner, Zhang Chen, Alexander Richard, Vasu Agrawal, Markus Steinberger, Michael Zollhöfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00928v1.pdf)  
  Keywords: motion, dynamic, human, ar, high-fidelity, avatar, 3d gaussian, compact, gaussian splatting  

### Ray Tracing

- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: ray tracing, face, ar, gaussian splatting, reflection  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, ray casting, reflection  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: efficient, semantic, tracking, localization, face, ar, mapping, 3d gaussian, gaussian splatting, slam, ray tracing  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: relightable, reflection, shadow, ar, mapping, 3d gaussian, gaussian splatting, ray tracing  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: real-time rendering, geometry, face, ar, 3d gaussian, path tracing  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: efficient, real-time rendering, geometry, face, ar, high-fidelity, 3d gaussian, gaussian splatting, nerf, ray tracing, fast  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: ar, survey, mapping, 3d gaussian, gaussian splatting, ray tracing  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: efficient, ray marching, real-time rendering, ar, high-fidelity, 3d gaussian, gaussian splatting  
- **[Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction](https://arxiv.org/abs/2603.08503v1)**  
  Authors: Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08503v1.pdf) | [![GitHub](https://img.shields.io/github/stars/1170632760/Spherical-GOF?style=social)](https://github.com/1170632760/Spherical-GOF)  
  Keywords: efficient, geometry, ar, 3d gaussian, robotics, gaussian splatting, ray casting, fast  
- **[Ref-DGS: Reflective Dual Gaussian Splatting](https://arxiv.org/abs/2603.07664v2)**  
  Authors: Ningjing Fan, Yiqun Wang, Dongming Yan, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07664v2.pdf)  
  Keywords: efficient, ray tracing, geometry, face, ar, gaussian splatting, lightweight, reflection, fast  

### Relighting

*Showing the latest 50 out of 73 papers*

- **[HOIGS: Human-Object Interaction Gaussian Splatting](https://arxiv.org/abs/2604.04016v1)**  
  Authors: Taewoo Kim, Suwoong Yeom, Jaehyun Pyun, Geonho Cha, Dongyoon Wee, Joonsik Nam, Yun-Seong Jeong, Kyeongbo Kong, Suk-Ju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04016v1.pdf)  
  Keywords: motion, 4d, dynamic, deformation, human, ar, high-fidelity, lighting, gaussian splatting  
- **[SpectralSplat: Appearance-Disentangled Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2604.03462v1)**  
  Authors: Quentin Herau, Tianshuo Xu, Depu Meng, Jiezhi Yang, Chensheng Peng, Spencer Sherk, Yihan Hu, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03462v1.pdf)  
  Keywords: relighting, geometry, ar, lighting, 3d gaussian, autonomous driving, gaussian splatting  
- **[Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM](https://arxiv.org/abs/2604.03092v1)**  
  Authors: Zicheng Zhang, Ke Wu, Xiangting Meng, Keyu Liu, Jieru Zhao, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://victkk.github.io/flash-mono)  
  Keywords: efficient, geometry, tracking, ar, lighting, mapping, 3d gaussian, compact, gaussian splatting, slam  
- **[Streaming Real-Time Rendered Scenes as 3D Gaussians](https://arxiv.org/abs/2604.02851v1)**  
  Authors: Matti Siekkinen, Teemu Kämäräinen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02851v1.pdf)  
  Keywords: relighting, dynamic, ar, lighting, 3d gaussian, gaussian splatting  
- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2604.02781v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02781v1.pdf)  
  Keywords: semantic, dynamic, geometry, 3d gaussian, gaussian splatting, reflection  
- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: ray tracing, face, ar, gaussian splatting, reflection  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: efficient, motion, large scene, geometry, dynamic, 4d, shadow, ar, high-fidelity, neural rendering, understanding, gaussian splatting  
- **[LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting](https://arxiv.org/abs/2603.29209v1)**  
  Authors: Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29209v1.pdf)  
  Keywords: efficient, geometry, illumination, shadow, ar, high-fidelity, lighting, 3d gaussian, vr, gaussian splatting  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, ray casting, reflection  
- **[ObjectMorpher: 3D-Aware Image Editing via Deformable 3DGS Models](https://arxiv.org/abs/2603.28152v1)**  
  Authors: Yuhuan Xie, Aoxuan Pan, Yi-Hua Huang, Chirui Chang, Peng Dai, Xin Yu, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28152v1.pdf)  
  Keywords: geometry, deformation, ar, lighting, 3d gaussian, gaussian splatting, fast  

### SLAM

*Showing the latest 50 out of 76 papers*

- **[Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM](https://arxiv.org/abs/2604.03092v1)**  
  Authors: Zicheng Zhang, Ke Wu, Xiangting Meng, Keyu Liu, Jieru Zhao, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://victkk.github.io/flash-mono)  
  Keywords: efficient, geometry, tracking, ar, lighting, mapping, 3d gaussian, compact, gaussian splatting, slam  
- **[Differentiable Stroke Planning with Dual Parameterization for Efficient and High-Fidelity Painting Creation](https://arxiv.org/abs/2604.02752v1)**  
  Authors: Jinfan Liu, Wuze Zhang, Zhangli Hu, Zhehan Zhao, Ye Chen, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02752v1.pdf)  
  Keywords: efficient, ar, high-fidelity, mapping  
- **[VBGS-SLAM: Variational Bayesian Gaussian Splatting Simultaneous Localization and Mapping](https://arxiv.org/abs/2604.02696v1)**  
  Authors: Yuhan Zhu, Yanyu Zhang, Jie Xu, Wei Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02696v1.pdf)  
  Keywords: efficient, tracking, localization, ar, mapping, 3d gaussian, gaussian splatting, slam  
- **[TrackerSplat: Exploiting Point Tracking for Fast and Robust Dynamic 3D Gaussians Reconstruction](https://arxiv.org/abs/2604.02586v1)**  
  Authors: Daheng Yin, Isaac Ding, Yili Jin, Jianxin Shi, Jiangchuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02586v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yindaheng98/TrackerSplat?style=social)](https://github.com/yindaheng98/TrackerSplat)  
  Keywords: efficient, motion, dynamic, tracking, ar, 3d gaussian, robotics, gaussian splatting, 3d reconstruction, fast  
- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: semantic, motion, 4d, dynamic, geometry, human, face, high-fidelity, segmentation, ar, understanding, gaussian splatting, tracking  
- **[Satellite-Free Training for Drone-View Geo-Localization](https://arxiv.org/abs/2604.01581v2)**  
  Authors: Tao Liu, Yingzhi Zhang, Kan Ren, Xiaoqi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01581v2.pdf)  
  Keywords: geometry, localization, ar, 3d gaussian, gaussian splatting, lightweight  
- **[Compact Keyframe-Optimized Multi-Agent Gaussian Splatting SLAM](https://arxiv.org/abs/2604.00804v1)**  
  Authors: Monica M. Q. Li, Pierre-Yves Lajoie, Jialiang Liu, Giovanni Beltrame  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00804v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lemonci/coko-slam?style=social)](https://github.com/lemonci/coko-slam)  
  Keywords: efficient, localization, ar, mapping, 3d gaussian, compact, gaussian splatting, slam, lightweight  
- **[GRVS: a Generalizable and Recurrent Approach to Monocular Dynamic View Synthesis](https://arxiv.org/abs/2603.29734v1)**  
  Authors: Thomas Tanay, Mohammed Brahimi, Michal Nazarczuk, Qingwen Zhang, Sibi Catley-Chandar, Arthur Moreau, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29734v1.pdf)  
  Keywords: efficient, motion, 4d, dynamic, ar, mapping, gaussian splatting  
- **[Efficient Camera Pose Augmentation for View Generalization in Robotic Policy Learning](https://arxiv.org/abs/2603.29192v1)**  
  Authors: Sen Wang, Huaiyi Dong, Jingyi Tian, Jiayi Li, Zhuo Yang, Tongtong Cao, Anlin Chen, Shuang Wu, Le Wang, Sanping Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29192v1.pdf)  
  Keywords: efficient, ar, high-fidelity, mapping, 3d gaussian, gaussian splatting  
- **[Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting](https://arxiv.org/abs/2603.29185v1)**  
  Authors: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29185v1.pdf)  
  Keywords: efficient, localization, ar, gaussian splatting, outdoor  

### Scene Understanding

*Showing the latest 50 out of 131 papers*

- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2604.02781v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02781v1.pdf)  
  Keywords: semantic, dynamic, geometry, 3d gaussian, gaussian splatting, reflection  
- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: motion, 4d, dynamic, deformation, head, segmentation, high-fidelity, ar, 3d gaussian, gaussian splatting, lightweight  
- **[A3R: Agentic Affordance Reasoning via Cross-Dimensional Evidence in 3D Gaussian Scenes](https://arxiv.org/abs/2604.01882v1)**  
  Authors: Di Li, Jie Feng, Guanbin Li, Ronghua Shang, Yuhui Zheng, Weisheng Dong, Guangming Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01882v1.pdf)  
  Keywords: ar, semantic, 3d gaussian  
- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: semantic, motion, 4d, dynamic, geometry, human, face, high-fidelity, segmentation, ar, understanding, gaussian splatting, tracking  
- **[LESV: Language Embedded Sparse Voxel Fusion for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2604.01388v1)**  
  Authors: Fusang Wang, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Fabien Moutarde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01388v1.pdf)  
  Keywords: semantic, geometry, head, ar, 3d gaussian, vr, understanding, gaussian splatting  
- **[Neural Harmonic Textures for High-Quality Primitive Based Neural Reconstruction](https://arxiv.org/abs/2604.01204v1)**  
  Authors: Jorge Condor, Nicolas Moenne-Loccoz, Merlin Nimier-David, Piotr Didyk, Zan Gojcic, Qi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01204v1.pdf)  
  Keywords: semantic, large scene, ar, 3d gaussian, gaussian splatting  
- **[DLWM: Dual Latent World Models enable Holistic Gaussian-centric Pre-training in Autonomous Driving](https://arxiv.org/abs/2604.00969v1)**  
  Authors: Yiyao Zhu, Ying Xue, Haiming Zhang, Guangfeng Jiang, Wending Zhou, Xu Yan, Jiantao Gao, Yingjie Cai, Bingbing Liu, Zhen Li, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00969v1.pdf)  
  Keywords: semantic, motion, 4d, ar, 3d gaussian, autonomous driving  
- **[TreeGaussian: Tree-Guided Cascaded Contrastive Learning for Hierarchical Consistent 3D Gaussian Scene Segmentation and Understanding](https://arxiv.org/abs/2604.03309v1)**  
  Authors: Jingbin You, Zehao Li, Hao Jiang, Xinzhu Ma, Shuqin Gao, Honglong Zhao, Congcong Zheng, Tianlu Mao, Feng Dai, Yucheng Zhang, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03309v1.pdf)  
  Keywords: semantic, ar, segmentation, 3d gaussian, understanding, gaussian splatting  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: efficient, motion, large scene, geometry, dynamic, 4d, shadow, ar, high-fidelity, neural rendering, understanding, gaussian splatting  
- **[DipGuava: Disentangling Personalized Gaussian Features for 3D Head Avatars from Monocular Video](https://arxiv.org/abs/2603.28003v1)**  
  Authors: Jeonghaeng Lee, Seok Keun Choi, Zhixuan Li, Weisi Lin, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28003v1.pdf)  
  Keywords: semantic, dynamic, geometry, deformation, head, ar, avatar, 3d gaussian  



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