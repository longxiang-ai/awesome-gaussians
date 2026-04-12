# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-04-12 01:27:47

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
- [Acceleration](#acceleration) (108 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (162 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (203 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (36 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (209 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (17 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (207 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (129 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (18 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (69 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (78 papers) - Papers about SLAM using Gaussian Splatting
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
  Keywords: vr, survey, 3d gaussian, ar, gaussian splatting  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: ray tracing, mapping, survey, 3d gaussian, ar, gaussian splatting  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: ar, slam, localization, efficient, tracking, motion, mapping, survey, 3d gaussian, face, dynamic, gaussian splatting  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: robotics, survey, 3d gaussian, ar, gaussian splatting  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v3)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v3.pdf)  
  Keywords: efficient, geometry, nerf, survey, 3d gaussian, ar, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 108 papers*

- **[ReconPhys: Reconstruct Appearance and Physical Attributes from Single Video](https://arxiv.org/abs/2604.07882v1)**  
  Authors: Boyuan Wang, Xiaofeng Wang, Yongkang Li, Zheng Zhu, Yifan Chang, Angen Ye, Guosheng Zhao, Chaojun Ni, Guan Huang, Yijie Ren, Yueqi Duan, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07882v1.pdf)  
  Keywords: geometry, robotics, fast, 3d gaussian, ar, dynamic, gaussian splatting  
- **[From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians](https://arxiv.org/abs/2604.07337v1)**  
  Authors: Diego Gomez, Antoine Guédon, Nissim Maruani, Bingchen Gong, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07337v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, fast, 3d gaussian, ar, face  
- **[Genie Sim PanoRecon: Fast Immersive Scene Generation from Single-View Panorama](https://arxiv.org/abs/2604.07105v1)**  
  Authors: Zhijun Li, Yongxin Su, Di Yang, Jichao Wang, Zheyuan Xing, Qian Wang, Maoqing Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07105v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AgibotTech/genie_sim?style=social)](https://github.com/AgibotTech/genie_sim)  
  Keywords: high-fidelity, fast, 3d gaussian, ar, face  
- **[TrackerSplat: Exploiting Point Tracking for Fast and Robust Dynamic 3D Gaussians Reconstruction](https://arxiv.org/abs/2604.02586v1)**  
  Authors: Daheng Yin, Isaac Ding, Yili Jin, Jianxin Shi, Jiangchuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02586v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yindaheng98/TrackerSplat?style=social)](https://github.com/yindaheng98/TrackerSplat)  
  Keywords: ar, efficient, robotics, tracking, motion, fast, 3d gaussian, 3d reconstruction, dynamic, gaussian splatting  
- **[GEMM-GS: Accelerating 3D Gaussian Splatting on Tensor Cores with GEMM-Compatible Blending](https://arxiv.org/abs/2604.02120v2)**  
  Authors: Haomin Li, Bowen Zhu, Fangxin Liu, Zongwu Wang, Xinran Liang, Li Jiang, Haibing Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02120v2.pdf) | [![GitHub](https://img.shields.io/github/stars/shieldforever/GEMM-GS?style=social)](https://github.com/shieldforever/GEMM-GS)  
  Keywords: 3d gaussian, acceleration, nerf, gaussian splatting  
- **[GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2604.01884v1)**  
  Authors: Xianben Yang, Tao Wang, Yuxuan Li, Yi Jin, Haibin Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01884v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, 3d gaussian, ar, dynamic, compact  
- **[FaCT-GS: Fast and Scalable CT Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2604.01844v1)**  
  Authors: Pawel Tomasz Pieta, Rasmus Juul Pedersen, Sina Borgi, Jakob Sauer Jørgensen, Jens Wenzel Andreasen, Vedrana Andersen Dahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01844v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PaPieta/fact-gs?style=social)](https://github.com/PaPieta/fact-gs)  
  Keywords: ar, fast, gaussian splatting  
- **[Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty-aware Differentiable Optimization](https://arxiv.org/abs/2604.01030v1)**  
  Authors: Yueh-Cheng Liu, Jozef Hladký, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01030v1.pdf)  
  Keywords: sparse-view, fast, 3d gaussian, ar, gaussian splatting  
- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394v1)**  
  Authors: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29394v1.pdf)  
  Keywords: ar, fast, 3d gaussian, sparse-view, 3d reconstruction, gaussian splatting  
- **[LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2603.28431v3)**  
  Authors: Xuan Deng, Xiandong Meng, Hengyu Man, Qiang Zhu, Tiange Zhang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28431v3.pdf)  
  Keywords: real-time rendering, high-fidelity, geometry, nerf, head, lightweight, 3d gaussian, ar, compression, compact, gaussian splatting  

### Applications

*Showing the latest 50 out of 498 papers*

- **[Visually-grounded Humanoid Agents](https://arxiv.org/abs/2604.08509v1)**  
  Authors: Hang Ye, Xiaoxuan Ma, Fan Lu, Wayne Wu, Kwan-Yee Lin, Yizhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08509v1.pdf)  
  Keywords: body, human, semantic, 3d gaussian, ar, avatar  
- **[BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields](https://arxiv.org/abs/2604.08410v1)**  
  Authors: Fan Yang, Wenrui Chen, Guorun Yan, Ruize Liao, Wanjun Jia, Dongsheng Luo, Kailun Yang, Zhiyong Li, Yaonan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08410v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PopeyePxx/BLaDA?style=social)](https://github.com/PopeyePxx/BLaDA)  
  Keywords: localization, semantic, understanding, 3d gaussian, ar, gaussian splatting  
- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370v1)**  
  Authors: Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08370v1.pdf)  
  Keywords: ar, efficient, geometry, 3d gaussian, sparse-view, face, gaussian splatting  
- **[DP-DeGauss: Dynamic Probabilistic Gaussian Decomposition for Egocentric 4D Scene Reconstruction](https://arxiv.org/abs/2604.07986v1)**  
  Authors: Tingxi Chen, Zhengxue Cheng, Houqiang Zhong, Su Wang, Rong Xie, Li Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07986v1.pdf)  
  Keywords: vr, deformation, understanding, motion, 3d gaussian, ar, 4d, dynamic  
- **[Generative 3D Gaussian Splatting for Arbitrary-ResolutionAtmospheric Downscaling and Forecasting](https://arxiv.org/abs/2604.07928v1)**  
  Authors: Tao Hana, Zhibin Wen, Zhenghao Chen, Fenghua Lin, Junyu Gao, Song Guo, Lei Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07928v1.pdf) | [![GitHub](https://img.shields.io/github/stars/binbin2xs/weather-GS?style=social)](https://github.com/binbin2xs/weather-GS)  
  Keywords: 3d gaussian, efficient, ar, gaussian splatting  
- **[ReconPhys: Reconstruct Appearance and Physical Attributes from Single Video](https://arxiv.org/abs/2604.07882v1)**  
  Authors: Boyuan Wang, Xiaofeng Wang, Yongkang Li, Zheng Zhu, Yifan Chang, Angen Ye, Guosheng Zhao, Chaojun Ni, Guan Huang, Yijie Ren, Yueqi Duan, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07882v1.pdf)  
  Keywords: geometry, robotics, fast, 3d gaussian, ar, dynamic, gaussian splatting  
- **[GEAR: GEometry-motion Alternating Refinement for Articulated Object Modeling with Gaussian Splatting](https://arxiv.org/abs/2604.07728v1)**  
  Authors: Jialin Li, Bin Fu, Ruiping Wang, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07728v1.pdf)  
  Keywords: segmentation, high-fidelity, geometry, motion, ar, gaussian splatting  
- **[From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians](https://arxiv.org/abs/2604.07337v1)**  
  Authors: Diego Gomez, Antoine Guédon, Nissim Maruani, Bingchen Gong, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07337v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, fast, 3d gaussian, ar, face  
- **[Splats under Pressure: Exploring Performance-Energy Trade-offs in Real-Time 3D Gaussian Splatting under Constrained GPU Budgets](https://arxiv.org/abs/2604.07177v1)**  
  Authors: Muhammad Fahim Tajwar, Arthur Wuhrlin, Bhojan Anand  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07177v1.pdf)  
  Keywords: 3d gaussian, ar, head, gaussian splatting  
- **[Genie Sim PanoRecon: Fast Immersive Scene Generation from Single-View Panorama](https://arxiv.org/abs/2604.07105v1)**  
  Authors: Zhijun Li, Yongxin Su, Di Yang, Jichao Wang, Zheyuan Xing, Qian Wang, Maoqing Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07105v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AgibotTech/genie_sim?style=social)](https://github.com/AgibotTech/genie_sim)  
  Keywords: high-fidelity, fast, 3d gaussian, ar, face  

### Avatar Generation

*Showing the latest 50 out of 162 papers*

- **[Visually-grounded Humanoid Agents](https://arxiv.org/abs/2604.08509v1)**  
  Authors: Hang Ye, Xiaoxuan Ma, Fan Lu, Wayne Wu, Kwan-Yee Lin, Yizhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08509v1.pdf)  
  Keywords: body, human, semantic, 3d gaussian, ar, avatar  
- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370v1)**  
  Authors: Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08370v1.pdf)  
  Keywords: ar, efficient, geometry, 3d gaussian, sparse-view, face, gaussian splatting  
- **[From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians](https://arxiv.org/abs/2604.07337v1)**  
  Authors: Diego Gomez, Antoine Guédon, Nissim Maruani, Bingchen Gong, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07337v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, fast, 3d gaussian, ar, face  
- **[Splats under Pressure: Exploring Performance-Energy Trade-offs in Real-Time 3D Gaussian Splatting under Constrained GPU Budgets](https://arxiv.org/abs/2604.07177v1)**  
  Authors: Muhammad Fahim Tajwar, Arthur Wuhrlin, Bhojan Anand  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07177v1.pdf)  
  Keywords: 3d gaussian, ar, head, gaussian splatting  
- **[Genie Sim PanoRecon: Fast Immersive Scene Generation from Single-View Panorama](https://arxiv.org/abs/2604.07105v1)**  
  Authors: Zhijun Li, Yongxin Su, Di Yang, Jichao Wang, Zheyuan Xing, Qian Wang, Maoqing Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07105v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AgibotTech/genie_sim?style=social)](https://github.com/AgibotTech/genie_sim)  
  Keywords: high-fidelity, fast, 3d gaussian, ar, face  
- **[Radio-Frequency Inverse Rendering for Wireless Environment Modeling](https://arxiv.org/abs/2604.07086v1)**  
  Authors: Fuhai Wang, Zihan Jin, Lehang Wang, Xuehui Dong, Tiebin Mi, Robert Caiming Qiu, Zenan ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07086v1.pdf)  
  Keywords: neural rendering, geometry, gaussian splatting, ar, face  
- **[4D Vessel Reconstruction for Benchtop Thrombectomy Analysis](https://arxiv.org/abs/2604.06671v1)**  
  Authors: Ethan Nguyen, Javier Carmona, Arisa Matsuzaki, Naoki Kaneko, Katsushi Arisaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06671v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ethanuser.github.io/vessel4D)  
  Keywords: deformation, gaussian splatting, tracking, motion, mapping, ar, 4d, face  
- **[PhysHead: Simulation-Ready Gaussian Head Avatars](https://arxiv.org/abs/2604.06467v1)**  
  Authors: Berna Kabadayi, Vanessa Sklyarova, Wojciech Zielonka, Justus Thies, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06467v1.pdf)  
  Keywords: motion, dynamic, head, 3d gaussian, ar, avatar, animation  
- **[GS-Surrogate: Deformable Gaussian Splatting for Parameter Space Exploration of Ensemble Simulations](https://arxiv.org/abs/2604.06358v1)**  
  Authors: Ziwei Li, Rumali Perera, Angus Forbes, Ken Moreland, Dave Pugmire, Scott Klasky, Wei-Lun Chao, Han-Wei Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06358v1.pdf)  
  Keywords: deformation, efficient, gaussian splatting, ar, face  
- **[Appearance Decomposition Gaussian Splatting for Multi-Traversal Reconstruction](https://arxiv.org/abs/2604.05908v1)**  
  Authors: Yangyi Xiao, Siting Zhu, Baoquan Yang, Tianchen Deng, Yongbo Chen, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05908v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRMVLab/ADM-GS?style=social)](https://github.com/IRMVLab/ADM-GS)  
  Keywords: illumination, ar, lighting, reflection, high-fidelity, geometry, autonomous driving, face, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 203 papers*

- **[DP-DeGauss: Dynamic Probabilistic Gaussian Decomposition for Egocentric 4D Scene Reconstruction](https://arxiv.org/abs/2604.07986v1)**  
  Authors: Tingxi Chen, Zhengxue Cheng, Houqiang Zhong, Su Wang, Rong Xie, Li Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07986v1.pdf)  
  Keywords: vr, deformation, understanding, motion, 3d gaussian, ar, 4d, dynamic  
- **[ReconPhys: Reconstruct Appearance and Physical Attributes from Single Video](https://arxiv.org/abs/2604.07882v1)**  
  Authors: Boyuan Wang, Xiaofeng Wang, Yongkang Li, Zheng Zhu, Yifan Chang, Angen Ye, Guosheng Zhao, Chaojun Ni, Guan Huang, Yijie Ren, Yueqi Duan, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07882v1.pdf)  
  Keywords: geometry, robotics, fast, 3d gaussian, ar, dynamic, gaussian splatting  
- **[GEAR: GEometry-motion Alternating Refinement for Articulated Object Modeling with Gaussian Splatting](https://arxiv.org/abs/2604.07728v1)**  
  Authors: Jialin Li, Bin Fu, Ruiping Wang, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07728v1.pdf)  
  Keywords: segmentation, high-fidelity, geometry, motion, ar, gaussian splatting  
- **[4D Vessel Reconstruction for Benchtop Thrombectomy Analysis](https://arxiv.org/abs/2604.06671v1)**  
  Authors: Ethan Nguyen, Javier Carmona, Arisa Matsuzaki, Naoki Kaneko, Katsushi Arisaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06671v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ethanuser.github.io/vessel4D)  
  Keywords: deformation, gaussian splatting, tracking, motion, mapping, ar, 4d, face  
- **[Spatiotemporal Gaussian representation-based dynamic reconstruction and motion estimation framework for time-resolved volumetric MR imaging (DREME-GSMR)](https://arxiv.org/abs/2604.06482v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, Can Wu, Ricardo Otazo, Jie Deng, Mu-Han Lin, Tsuicheng Chiu, Jacob Buatti, Viktor Iakovenko, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06482v1.pdf)  
  Keywords: efficient, tracking, motion, 3d gaussian, ar, dynamic  
- **[PhysHead: Simulation-Ready Gaussian Head Avatars](https://arxiv.org/abs/2604.06467v1)**  
  Authors: Berna Kabadayi, Vanessa Sklyarova, Wojciech Zielonka, Justus Thies, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06467v1.pdf)  
  Keywords: motion, dynamic, head, 3d gaussian, ar, avatar, animation  
- **[GS-Surrogate: Deformable Gaussian Splatting for Parameter Space Exploration of Ensemble Simulations](https://arxiv.org/abs/2604.06358v1)**  
  Authors: Ziwei Li, Rumali Perera, Angus Forbes, Ken Moreland, Dave Pugmire, Scott Klasky, Wei-Lun Chao, Han-Wei Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06358v1.pdf)  
  Keywords: deformation, efficient, gaussian splatting, ar, face  
- **[PanopticQuery: Unified Query-Time Reasoning for 4D Scenes](https://arxiv.org/abs/2604.05638v1)**  
  Authors: Ruilin Tang, Yang Zhou, Zhong Ye, Wenxi Liu, Yan Huang, Shengfeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05638v1.pdf)  
  Keywords: semantic, high-fidelity, understanding, ar, 4d, dynamic, gaussian splatting  
- **[Part-Level 3D Gaussian Vehicle Generation with Joint and Hinge Axis Estimation](https://arxiv.org/abs/2604.05070v1)**  
  Authors: Shiyao Qian, Yuan Ren, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05070v1.pdf)  
  Keywords: segmentation, autonomous driving, motion, head, 3d gaussian, ar, dynamic  
- **[AvatarPointillist: AutoRegressive 4D Gaussian Avatarization](https://arxiv.org/abs/2604.04787v1)**  
  Authors: Hongyu Liu, Xuan Wang, Yating Wang, Zijian Wu, Ziyu Wan, Yue Ma, Runtao Liu, Boyao Zhou, Yujun Shen, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04787v1.pdf)  
  Keywords: dynamic, avatar, 3d gaussian, ar, 4d, animation, gaussian splatting  

### Few-shot

- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370v1)**  
  Authors: Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08370v1.pdf)  
  Keywords: ar, efficient, geometry, 3d gaussian, sparse-view, face, gaussian splatting  
- **[DOC-GS: Dual-Domain Observation and Calibration for Reliable Sparse-View Gaussian Splatting](https://arxiv.org/abs/2604.06739v1)**  
  Authors: Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06739v1.pdf)  
  Keywords: sparse-view, understanding, 3d gaussian, ar, gaussian splatting  
- **[3D Gaussian Splatting for Annular Dark Field Scanning Transmission Electron Microscopy Tomography Reconstruction](https://arxiv.org/abs/2604.04693v1)**  
  Authors: Beiyuan Zhang, Hesong Li, Ruiwen Shao, Ying Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04693v1.pdf)  
  Keywords: sparse-view, ar, efficient, high-fidelity, 3d gaussian, 3d reconstruction, gaussian splatting  
- **[PR-IQA: Partial-Reference Image Quality Assessment for Diffusion-Based Novel View Synthesis](https://arxiv.org/abs/2604.04576v2)**  
  Authors: Inseong Choi, Siwoo Lee, Seung-Hun Nam, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04576v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kakaomacao.github.io/pr-iqa-project-page)  
  Keywords: sparse-view, 3d gaussian, ar, 3d reconstruction, gaussian splatting  
- **[4C4D: 4 Camera 4D Gaussian Splatting](https://arxiv.org/abs/2604.04063v1)**  
  Authors: Junsheng Zhou, Zhifan Yang, Liang Han, Wenyuan Zhang, Kanle Shi, Shenkun Xu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04063v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://junshengzhou.github.io/4C4D)  
  Keywords: ar, high-fidelity, geometry, sparse-view, 4d, dynamic, gaussian splatting  
- **[Rendering Multi-Human and Multi-Object with 3D Gaussian Splatting](https://arxiv.org/abs/2604.02996v2)**  
  Authors: Weiquan Wang, Jun Xiao, Feifei Shao, Yi Yang, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02996v2.pdf)  
  Keywords: vr, ar, human, high-fidelity, robotics, 3d gaussian, sparse-view, dynamic, gaussian splatting  
- **[TRACE: High-Fidelity 3D Scene Editing via Tangible Reconstruction and Geometry-Aligned Contextual Video Masking](https://arxiv.org/abs/2604.01207v1)**  
  Authors: Jiyuan Hu, Zechuan Zhang, Zongxin Yang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01207v1.pdf)  
  Keywords: high-fidelity, geometry, sparse-view, ar  
- **[Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty-aware Differentiable Optimization](https://arxiv.org/abs/2604.01030v1)**  
  Authors: Yueh-Cheng Liu, Jozef Hladký, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01030v1.pdf)  
  Keywords: sparse-view, fast, 3d gaussian, ar, gaussian splatting  
- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394v1)**  
  Authors: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29394v1.pdf)  
  Keywords: ar, fast, 3d gaussian, sparse-view, 3d reconstruction, gaussian splatting  
- **[\textit{4DSurf}: High-Fidelity Dynamic Scene Surface Reconstruction](https://arxiv.org/abs/2603.28064v1)**  
  Authors: Renjie Wu, Hongdong Li, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28064v1.pdf)  
  Keywords: deformation, ar, high-fidelity, geometry, motion, sparse-view, face, 4d, dynamic, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 209 papers*

- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370v1)**  
  Authors: Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08370v1.pdf)  
  Keywords: ar, efficient, geometry, 3d gaussian, sparse-view, face, gaussian splatting  
- **[ReconPhys: Reconstruct Appearance and Physical Attributes from Single Video](https://arxiv.org/abs/2604.07882v1)**  
  Authors: Boyuan Wang, Xiaofeng Wang, Yongkang Li, Zheng Zhu, Yifan Chang, Angen Ye, Guosheng Zhao, Chaojun Ni, Guan Huang, Yijie Ren, Yueqi Duan, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07882v1.pdf)  
  Keywords: geometry, robotics, fast, 3d gaussian, ar, dynamic, gaussian splatting  
- **[GEAR: GEometry-motion Alternating Refinement for Articulated Object Modeling with Gaussian Splatting](https://arxiv.org/abs/2604.07728v1)**  
  Authors: Jialin Li, Bin Fu, Ruiping Wang, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07728v1.pdf)  
  Keywords: segmentation, high-fidelity, geometry, motion, ar, gaussian splatting  
- **[Radio-Frequency Inverse Rendering for Wireless Environment Modeling](https://arxiv.org/abs/2604.07086v1)**  
  Authors: Fuhai Wang, Zihan Jin, Lehang Wang, Xuehui Dong, Tiebin Mi, Robert Caiming Qiu, Zenan ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07086v1.pdf)  
  Keywords: neural rendering, geometry, gaussian splatting, ar, face  
- **[AnchorSplat: Feed-Forward 3D Gaussian Splatting with 3D Geometric Priors](https://arxiv.org/abs/2604.07053v2)**  
  Authors: Xiaoxue Zhang, Xiaoxu Zheng, Yixuan Yin, Tiao Zhao, Kaihua Tang, Michael Bi Mi, Zhan Xu, Dave Zhenyu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07053v2.pdf)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting  
- **[Appearance Decomposition Gaussian Splatting for Multi-Traversal Reconstruction](https://arxiv.org/abs/2604.05908v1)**  
  Authors: Yangyi Xiao, Siting Zhu, Baoquan Yang, Tianchen Deng, Yongbo Chen, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05908v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRMVLab/ADM-GS?style=social)](https://github.com/IRMVLab/ADM-GS)  
  Keywords: illumination, ar, lighting, reflection, high-fidelity, geometry, autonomous driving, face, gaussian splatting  
- **[GaussianGrow: Geometry-aware Gaussian Growing from 3D Point Clouds with Text Guidance](https://arxiv.org/abs/2604.05721v1)**  
  Authors: Weiqi Zhang, Junsheng Zhou, Haotian Geng, Kanle Shi, Shenkun Xu, Yi Fang, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05721v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weiqi-zhang.github.io/GaussianGrow)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting  
- **[In Depth We Trust: Reliable Monocular Depth Supervision for Gaussian Splatting](https://arxiv.org/abs/2604.05715v1)**  
  Authors: Wenhui Xiao, Ethan Goan, Rodrigo Santa Cruz, David Ahmedt-Aristizabal, Olivier Salvado, Clinton Fookes, Leo Lebrat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05715v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, ar, face  
- **[3DTurboQuant: Training-Free Near-Optimal Quantization for 3D Reconstruction Models](https://arxiv.org/abs/2604.05366v1)**  
  Authors: Jae Joong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05366v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JaeLee18/3DTurboQuant?style=social)](https://github.com/JaeLee18/3DTurboQuant)  
  Keywords: ar, nerf, 3d gaussian, 3d reconstruction, compression, gaussian splatting  
- **[SmokeGS-R: Physics-Guided Pseudo-Clean 3DGS for Real-World Multi-View Smoke Restoration](https://arxiv.org/abs/2604.05301v1)**  
  Authors: Xueming Fu, Lixia Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05301v1.pdf) | [![GitHub](https://img.shields.io/github/stars/windrise/3drr_Track2_SmokeGS-R?style=social)](https://github.com/windrise/3drr_Track2_SmokeGS-R)  
  Keywords: geometry, 3d gaussian, ar, 3d reconstruction, gaussian splatting  

### Large Scene

- **[Neural Harmonic Textures for High-Quality Primitive Based Neural Reconstruction](https://arxiv.org/abs/2604.01204v2)**  
  Authors: Jorge Condor, Nicolas Moenne-Loccoz, Merlin Nimier-David, Piotr Didyk, Zan Gojcic, Qi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01204v2.pdf)  
  Keywords: semantic, large scene, 3d gaussian, ar, gaussian splatting  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: neural rendering, efficient, high-fidelity, geometry, large scene, understanding, shadow, motion, ar, 4d, dynamic, gaussian splatting  
- **[Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting](https://arxiv.org/abs/2603.29185v1)**  
  Authors: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29185v1.pdf)  
  Keywords: localization, efficient, outdoor, ar, gaussian splatting  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: neural rendering, ar, efficient, large scene, head, 3d gaussian, face, gaussian splatting  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: slam, efficient, tracking, head, outdoor, ar, dynamic, gaussian splatting  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: outdoor, localization, geometry, 3d gaussian, ar, gaussian splatting  
- **[EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.06216v1)**  
  Authors: Miriam Jäger, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06216v1.pdf)  
  Keywords: ar, geometry, 3d gaussian, 3d reconstruction, face, urban scene, gaussian splatting  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: illumination, outdoor, ar, lighting, reflection, fast, relighting, nerf, relightable, 3d gaussian, 3d reconstruction, gaussian splatting  
- **[Interactive Augmented Reality-enabled Outdoor Scene Visualization For Enhanced Real-time Disaster Response](https://arxiv.org/abs/2602.21874v1)**  
  Authors: Dimitrios Apostolakis, Georgios Angelidis, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21874v1.pdf)  
  Keywords: outdoor, ar, lighting, semantic, fast, lightweight, 3d gaussian, face, gaussian splatting  
- **[Large-scale Photorealistic Outdoor 3D Scene Reconstruction from UAV Imagery Using Gaussian Splatting Techniques](https://arxiv.org/abs/2602.20342v1)**  
  Authors: Christos Maikos, Georgios Angelidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20342v1.pdf)  
  Keywords: neural rendering, vr, outdoor, ar, efficient, high-fidelity, nerf, 3d gaussian, 3d reconstruction, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 207 papers*

- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370v1)**  
  Authors: Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08370v1.pdf)  
  Keywords: ar, efficient, geometry, 3d gaussian, sparse-view, face, gaussian splatting  
- **[Generative 3D Gaussian Splatting for Arbitrary-ResolutionAtmospheric Downscaling and Forecasting](https://arxiv.org/abs/2604.07928v1)**  
  Authors: Tao Hana, Zhibin Wen, Zhenghao Chen, Fenghua Lin, Junyu Gao, Song Guo, Lei Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07928v1.pdf) | [![GitHub](https://img.shields.io/github/stars/binbin2xs/weather-GS?style=social)](https://github.com/binbin2xs/weather-GS)  
  Keywords: 3d gaussian, efficient, ar, gaussian splatting  
- **[Spatiotemporal Gaussian representation-based dynamic reconstruction and motion estimation framework for time-resolved volumetric MR imaging (DREME-GSMR)](https://arxiv.org/abs/2604.06482v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, Can Wu, Ricardo Otazo, Jie Deng, Mu-Han Lin, Tsuicheng Chiu, Jacob Buatti, Viktor Iakovenko, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06482v1.pdf)  
  Keywords: efficient, tracking, motion, 3d gaussian, ar, dynamic  
- **[GS-Surrogate: Deformable Gaussian Splatting for Parameter Space Exploration of Ensemble Simulations](https://arxiv.org/abs/2604.06358v1)**  
  Authors: Ziwei Li, Rumali Perera, Angus Forbes, Ken Moreland, Dave Pugmire, Scott Klasky, Wei-Lun Chao, Han-Wei Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06358v1.pdf)  
  Keywords: deformation, efficient, gaussian splatting, ar, face  
- **[3D Smoke Scene Reconstruction Guided by Vision Priors from Multimodal Large Language Models](https://arxiv.org/abs/2604.05687v1)**  
  Authors: Xinye Zheng, Fei Wang, Yiqi Nie, Kun Li, Junjie Chen, Jiaqi Zhao, Yanyan Wei, Zhiliang Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05687v1.pdf)  
  Keywords: efficient, lightweight, 3d gaussian, ar, gaussian splatting  
- **[3DTurboQuant: Training-Free Near-Optimal Quantization for 3D Reconstruction Models](https://arxiv.org/abs/2604.05366v1)**  
  Authors: Jae Joong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05366v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JaeLee18/3DTurboQuant?style=social)](https://github.com/JaeLee18/3DTurboQuant)  
  Keywords: ar, nerf, 3d gaussian, 3d reconstruction, compression, gaussian splatting  
- **[GaussFly: Contrastive Reinforcement Learning for Visuomotor Policies in 3D Gaussian Fields](https://arxiv.org/abs/2604.05062v1)**  
  Authors: Yuhang Zhang, Mingsheng Li, Yujing Shang, Zhuoyuan Yu, Chao Yan, Jiaping Xiao, Mir Feroskhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05062v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, ar, compact  
- **[3D Gaussian Splatting for Annular Dark Field Scanning Transmission Electron Microscopy Tomography Reconstruction](https://arxiv.org/abs/2604.04693v1)**  
  Authors: Beiyuan Zhang, Hesong Li, Ruiwen Shao, Ying Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04693v1.pdf)  
  Keywords: sparse-view, ar, efficient, high-fidelity, 3d gaussian, 3d reconstruction, gaussian splatting  
- **[CGHair: Compact Gaussian Hair Reconstruction with Card Clustering](https://arxiv.org/abs/2604.03716v1)**  
  Authors: Haimin Luo, Srinjay Sarkar, Albert Mosella-Montoro, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03716v1.pdf)  
  Keywords: high-fidelity, geometry, gaussian splatting, 3d gaussian, ar, compact  
- **[Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM](https://arxiv.org/abs/2604.03092v1)**  
  Authors: Zicheng Zhang, Ke Wu, Xiangting Meng, Keyu Liu, Jieru Zhao, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://victkk.github.io/flash-mono)  
  Keywords: slam, lighting, efficient, geometry, gaussian splatting, tracking, mapping, 3d gaussian, ar, compact  

### Quality Enhancement

*Showing the latest 50 out of 129 papers*

- **[GEAR: GEometry-motion Alternating Refinement for Articulated Object Modeling with Gaussian Splatting](https://arxiv.org/abs/2604.07728v1)**  
  Authors: Jialin Li, Bin Fu, Ruiping Wang, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07728v1.pdf)  
  Keywords: segmentation, high-fidelity, geometry, motion, ar, gaussian splatting  
- **[From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians](https://arxiv.org/abs/2604.07337v1)**  
  Authors: Diego Gomez, Antoine Guédon, Nissim Maruani, Bingchen Gong, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07337v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, fast, 3d gaussian, ar, face  
- **[Genie Sim PanoRecon: Fast Immersive Scene Generation from Single-View Panorama](https://arxiv.org/abs/2604.07105v1)**  
  Authors: Zhijun Li, Yongxin Su, Di Yang, Jichao Wang, Zheyuan Xing, Qian Wang, Maoqing Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07105v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AgibotTech/genie_sim?style=social)](https://github.com/AgibotTech/genie_sim)  
  Keywords: high-fidelity, fast, 3d gaussian, ar, face  
- **[Appearance Decomposition Gaussian Splatting for Multi-Traversal Reconstruction](https://arxiv.org/abs/2604.05908v1)**  
  Authors: Yangyi Xiao, Siting Zhu, Baoquan Yang, Tianchen Deng, Yongbo Chen, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05908v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRMVLab/ADM-GS?style=social)](https://github.com/IRMVLab/ADM-GS)  
  Keywords: illumination, ar, lighting, reflection, high-fidelity, geometry, autonomous driving, face, gaussian splatting  
- **[PanopticQuery: Unified Query-Time Reasoning for 4D Scenes](https://arxiv.org/abs/2604.05638v1)**  
  Authors: Ruilin Tang, Yang Zhou, Zhong Ye, Wenxi Liu, Yan Huang, Shengfeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05638v1.pdf)  
  Keywords: semantic, high-fidelity, understanding, ar, 4d, dynamic, gaussian splatting  
- **[GaussFly: Contrastive Reinforcement Learning for Visuomotor Policies in 3D Gaussian Fields](https://arxiv.org/abs/2604.05062v1)**  
  Authors: Yuhang Zhang, Mingsheng Li, Yujing Shang, Zhuoyuan Yu, Chao Yan, Jiaping Xiao, Mir Feroskhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05062v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, ar, compact  
- **[3D Gaussian Splatting for Annular Dark Field Scanning Transmission Electron Microscopy Tomography Reconstruction](https://arxiv.org/abs/2604.04693v1)**  
  Authors: Beiyuan Zhang, Hesong Li, Ruiwen Shao, Ying Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04693v1.pdf)  
  Keywords: sparse-view, ar, efficient, high-fidelity, 3d gaussian, 3d reconstruction, gaussian splatting  
- **[4C4D: 4 Camera 4D Gaussian Splatting](https://arxiv.org/abs/2604.04063v1)**  
  Authors: Junsheng Zhou, Zhifan Yang, Liang Han, Wenyuan Zhang, Kanle Shi, Shenkun Xu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04063v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://junshengzhou.github.io/4C4D)  
  Keywords: ar, high-fidelity, geometry, sparse-view, 4d, dynamic, gaussian splatting  
- **[HOIGS: Human-Object Interaction Gaussian Splatting](https://arxiv.org/abs/2604.04016v1)**  
  Authors: Taewoo Kim, Suwoong Yeom, Jaehyun Pyun, Geonho Cha, Dongyoon Wee, Joonsik Nam, Yun-Seong Jeong, Kyeongbo Kong, Suk-Ju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04016v1.pdf)  
  Keywords: deformation, lighting, human, high-fidelity, motion, ar, 4d, dynamic, gaussian splatting  
- **[CGHair: Compact Gaussian Hair Reconstruction with Card Clustering](https://arxiv.org/abs/2604.03716v1)**  
  Authors: Haimin Luo, Srinjay Sarkar, Albert Mosella-Montoro, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03716v1.pdf)  
  Keywords: high-fidelity, geometry, gaussian splatting, 3d gaussian, ar, compact  

### Ray Tracing

- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: reflection, gaussian splatting, ray tracing, ar, face  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: reflection, efficient, ray casting, 3d gaussian, ar  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: slam, semantic, efficient, localization, gaussian splatting, ray tracing, tracking, mapping, 3d gaussian, ar, face  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: reflection, ray tracing, shadow, mapping, relightable, 3d gaussian, ar, gaussian splatting  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: real-time rendering, geometry, 3d gaussian, ar, path tracing, face  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: ar, real-time rendering, efficient, high-fidelity, geometry, ray tracing, fast, nerf, 3d gaussian, face, gaussian splatting  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: ray tracing, mapping, survey, 3d gaussian, ar, gaussian splatting  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: real-time rendering, efficient, high-fidelity, ray marching, 3d gaussian, ar, gaussian splatting  
- **[Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction](https://arxiv.org/abs/2603.08503v1)**  
  Authors: Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08503v1.pdf) | [![GitHub](https://img.shields.io/github/stars/1170632760/Spherical-GOF?style=social)](https://github.com/1170632760/Spherical-GOF)  
  Keywords: efficient, geometry, robotics, fast, ray casting, 3d gaussian, ar, gaussian splatting  
- **[Ref-DGS: Reflective Dual Gaussian Splatting](https://arxiv.org/abs/2603.07664v2)**  
  Authors: Ningjing Fan, Yiqun Wang, Dongming Yan, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07664v2.pdf)  
  Keywords: ar, reflection, efficient, geometry, ray tracing, fast, lightweight, face, gaussian splatting  

### Relighting

*Showing the latest 50 out of 69 papers*

- **[Appearance Decomposition Gaussian Splatting for Multi-Traversal Reconstruction](https://arxiv.org/abs/2604.05908v1)**  
  Authors: Yangyi Xiao, Siting Zhu, Baoquan Yang, Tianchen Deng, Yongbo Chen, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05908v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRMVLab/ADM-GS?style=social)](https://github.com/IRMVLab/ADM-GS)  
  Keywords: illumination, ar, lighting, reflection, high-fidelity, geometry, autonomous driving, face, gaussian splatting  
- **[HOIGS: Human-Object Interaction Gaussian Splatting](https://arxiv.org/abs/2604.04016v1)**  
  Authors: Taewoo Kim, Suwoong Yeom, Jaehyun Pyun, Geonho Cha, Dongyoon Wee, Joonsik Nam, Yun-Seong Jeong, Kyeongbo Kong, Suk-Ju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04016v1.pdf)  
  Keywords: deformation, lighting, human, high-fidelity, motion, ar, 4d, dynamic, gaussian splatting  
- **[SpectralSplat: Appearance-Disentangled Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2604.03462v1)**  
  Authors: Quentin Herau, Tianshuo Xu, Depu Meng, Jiezhi Yang, Chensheng Peng, Spencer Sherk, Yihan Hu, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03462v1.pdf)  
  Keywords: lighting, geometry, autonomous driving, relighting, 3d gaussian, ar, gaussian splatting  
- **[Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM](https://arxiv.org/abs/2604.03092v1)**  
  Authors: Zicheng Zhang, Ke Wu, Xiangting Meng, Keyu Liu, Jieru Zhao, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://victkk.github.io/flash-mono)  
  Keywords: slam, lighting, efficient, geometry, gaussian splatting, tracking, mapping, 3d gaussian, ar, compact  
- **[Streaming Real-Time Rendered Scenes as 3D Gaussians](https://arxiv.org/abs/2604.02851v1)**  
  Authors: Matti Siekkinen, Teemu Kämäräinen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02851v1.pdf)  
  Keywords: lighting, relighting, 3d gaussian, ar, dynamic, gaussian splatting  
- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2604.02781v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02781v1.pdf)  
  Keywords: reflection, semantic, geometry, 3d gaussian, dynamic, gaussian splatting  
- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: reflection, gaussian splatting, ray tracing, ar, face  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: neural rendering, efficient, high-fidelity, geometry, large scene, understanding, shadow, motion, ar, 4d, dynamic, gaussian splatting  
- **[LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting](https://arxiv.org/abs/2603.29209v1)**  
  Authors: Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29209v1.pdf)  
  Keywords: vr, illumination, lighting, efficient, high-fidelity, geometry, shadow, 3d gaussian, ar, gaussian splatting  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: reflection, efficient, ray casting, 3d gaussian, ar  

### SLAM

*Showing the latest 50 out of 78 papers*

- **[BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields](https://arxiv.org/abs/2604.08410v1)**  
  Authors: Fan Yang, Wenrui Chen, Guorun Yan, Ruize Liao, Wanjun Jia, Dongsheng Luo, Kailun Yang, Zhiyong Li, Yaonan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08410v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PopeyePxx/BLaDA?style=social)](https://github.com/PopeyePxx/BLaDA)  
  Keywords: localization, semantic, understanding, 3d gaussian, ar, gaussian splatting  
- **[4D Vessel Reconstruction for Benchtop Thrombectomy Analysis](https://arxiv.org/abs/2604.06671v1)**  
  Authors: Ethan Nguyen, Javier Carmona, Arisa Matsuzaki, Naoki Kaneko, Katsushi Arisaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06671v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ethanuser.github.io/vessel4D)  
  Keywords: deformation, gaussian splatting, tracking, motion, mapping, ar, 4d, face  
- **[Spatiotemporal Gaussian representation-based dynamic reconstruction and motion estimation framework for time-resolved volumetric MR imaging (DREME-GSMR)](https://arxiv.org/abs/2604.06482v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, Can Wu, Ricardo Otazo, Jie Deng, Mu-Han Lin, Tsuicheng Chiu, Jacob Buatti, Viktor Iakovenko, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06482v1.pdf)  
  Keywords: efficient, tracking, motion, 3d gaussian, ar, dynamic  
- **[LSGS-Loc: Towards Robust 3DGS-Based Visual Localization for Large-Scale UAV Scenarios](https://arxiv.org/abs/2604.05402v1)**  
  Authors: Xiang Zhang, Tengfei Wang, Fang Xu, Xin Wang, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05402v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xzhang-z/LSGS-Loc?style=social)](https://github.com/xzhang-z/LSGS-Loc)  
  Keywords: localization, 3d gaussian, ar, gaussian splatting  
- **[Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM](https://arxiv.org/abs/2604.03092v1)**  
  Authors: Zicheng Zhang, Ke Wu, Xiangting Meng, Keyu Liu, Jieru Zhao, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://victkk.github.io/flash-mono)  
  Keywords: slam, lighting, efficient, geometry, gaussian splatting, tracking, mapping, 3d gaussian, ar, compact  
- **[Differentiable Stroke Planning with Dual Parameterization for Efficient and High-Fidelity Painting Creation](https://arxiv.org/abs/2604.02752v1)**  
  Authors: Jinfan Liu, Wuze Zhang, Zhangli Hu, Zhehan Zhao, Ye Chen, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02752v1.pdf)  
  Keywords: efficient, high-fidelity, mapping, ar  
- **[VBGS-SLAM: Variational Bayesian Gaussian Splatting Simultaneous Localization and Mapping](https://arxiv.org/abs/2604.02696v1)**  
  Authors: Yuhan Zhu, Yanyu Zhang, Jie Xu, Wei Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02696v1.pdf)  
  Keywords: slam, localization, efficient, tracking, mapping, 3d gaussian, ar, gaussian splatting  
- **[TrackerSplat: Exploiting Point Tracking for Fast and Robust Dynamic 3D Gaussians Reconstruction](https://arxiv.org/abs/2604.02586v1)**  
  Authors: Daheng Yin, Isaac Ding, Yili Jin, Jianxin Shi, Jiangchuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02586v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yindaheng98/TrackerSplat?style=social)](https://github.com/yindaheng98/TrackerSplat)  
  Keywords: ar, efficient, robotics, tracking, motion, fast, 3d gaussian, 3d reconstruction, dynamic, gaussian splatting  
- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: segmentation, ar, human, semantic, high-fidelity, geometry, understanding, tracking, motion, face, 4d, dynamic, gaussian splatting  
- **[Satellite-Free Training for Drone-View Geo-Localization](https://arxiv.org/abs/2604.01581v2)**  
  Authors: Tao Liu, Yingzhi Zhang, Kan Ren, Xiaoqi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01581v2.pdf)  
  Keywords: localization, geometry, lightweight, 3d gaussian, ar, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 131 papers*

- **[Visually-grounded Humanoid Agents](https://arxiv.org/abs/2604.08509v1)**  
  Authors: Hang Ye, Xiaoxuan Ma, Fan Lu, Wayne Wu, Kwan-Yee Lin, Yizhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08509v1.pdf)  
  Keywords: body, human, semantic, 3d gaussian, ar, avatar  
- **[BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields](https://arxiv.org/abs/2604.08410v1)**  
  Authors: Fan Yang, Wenrui Chen, Guorun Yan, Ruize Liao, Wanjun Jia, Dongsheng Luo, Kailun Yang, Zhiyong Li, Yaonan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08410v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PopeyePxx/BLaDA?style=social)](https://github.com/PopeyePxx/BLaDA)  
  Keywords: localization, semantic, understanding, 3d gaussian, ar, gaussian splatting  
- **[DP-DeGauss: Dynamic Probabilistic Gaussian Decomposition for Egocentric 4D Scene Reconstruction](https://arxiv.org/abs/2604.07986v1)**  
  Authors: Tingxi Chen, Zhengxue Cheng, Houqiang Zhong, Su Wang, Rong Xie, Li Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07986v1.pdf)  
  Keywords: vr, deformation, understanding, motion, 3d gaussian, ar, 4d, dynamic  
- **[GEAR: GEometry-motion Alternating Refinement for Articulated Object Modeling with Gaussian Splatting](https://arxiv.org/abs/2604.07728v1)**  
  Authors: Jialin Li, Bin Fu, Ruiping Wang, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07728v1.pdf)  
  Keywords: segmentation, high-fidelity, geometry, motion, ar, gaussian splatting  
- **[DOC-GS: Dual-Domain Observation and Calibration for Reliable Sparse-View Gaussian Splatting](https://arxiv.org/abs/2604.06739v1)**  
  Authors: Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06739v1.pdf)  
  Keywords: sparse-view, understanding, 3d gaussian, ar, gaussian splatting  
- **[PanopticQuery: Unified Query-Time Reasoning for 4D Scenes](https://arxiv.org/abs/2604.05638v1)**  
  Authors: Ruilin Tang, Yang Zhou, Zhong Ye, Wenxi Liu, Yan Huang, Shengfeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05638v1.pdf)  
  Keywords: semantic, high-fidelity, understanding, ar, 4d, dynamic, gaussian splatting  
- **[Indoor Asset Detection in Large Scale 360° Drone-Captured Imagery via 3D Gaussian Splatting](https://arxiv.org/abs/2604.05316v1)**  
  Authors: Monica Tang, Avideh Zakhor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05316v1.pdf)  
  Keywords: segmentation, semantic, 3d gaussian, ar, gaussian splatting  
- **[Part-Level 3D Gaussian Vehicle Generation with Joint and Hinge Axis Estimation](https://arxiv.org/abs/2604.05070v1)**  
  Authors: Shiyao Qian, Yuan Ren, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05070v1.pdf)  
  Keywords: segmentation, autonomous driving, motion, head, 3d gaussian, ar, dynamic  
- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2604.02781v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02781v1.pdf)  
  Keywords: reflection, semantic, geometry, 3d gaussian, dynamic, gaussian splatting  
- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: segmentation, deformation, high-fidelity, motion, head, lightweight, 3d gaussian, ar, 4d, dynamic, gaussian splatting  



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