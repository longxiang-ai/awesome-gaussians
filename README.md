# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-04-11 01:18:16

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
  Keywords: 3d gaussian, ar, vr, survey, gaussian splatting  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: 3d gaussian, ar, ray tracing, survey, gaussian splatting, mapping  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: face, 3d gaussian, localization, ar, motion, dynamic, efficient, survey, tracking, gaussian splatting, mapping, slam  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: robotics, 3d gaussian, ar, survey, gaussian splatting  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v3)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v3.pdf)  
  Keywords: 3d gaussian, ar, nerf, geometry, efficient, survey, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 108 papers*

- **[ReconPhys: Reconstruct Appearance and Physical Attributes from Single Video](https://arxiv.org/abs/2604.07882v1)**  
  Authors: Boyuan Wang, Xiaofeng Wang, Yongkang Li, Zheng Zhu, Yifan Chang, Angen Ye, Guosheng Zhao, Chaojun Ni, Guan Huang, Yijie Ren, Yueqi Duan, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07882v1.pdf)  
  Keywords: fast, robotics, 3d gaussian, ar, geometry, dynamic, gaussian splatting  
- **[From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians](https://arxiv.org/abs/2604.07337v1)**  
  Authors: Diego Gomez, Antoine Guédon, Nissim Maruani, Bingchen Gong, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07337v1.pdf)  
  Keywords: face, fast, 3d gaussian, ar, high-fidelity, gaussian splatting  
- **[Genie Sim PanoRecon: Fast Immersive Scene Generation from Single-View Panorama](https://arxiv.org/abs/2604.07105v1)**  
  Authors: Zhijun Li, Yongxin Su, Di Yang, Jichao Wang, Zheyuan Xing, Qian Wang, Maoqing Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07105v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AgibotTech/genie_sim?style=social)](https://github.com/AgibotTech/genie_sim)  
  Keywords: face, fast, 3d gaussian, ar, high-fidelity  
- **[TrackerSplat: Exploiting Point Tracking for Fast and Robust Dynamic 3D Gaussians Reconstruction](https://arxiv.org/abs/2604.02586v1)**  
  Authors: Daheng Yin, Isaac Ding, Yili Jin, Jianxin Shi, Jiangchuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02586v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yindaheng98/TrackerSplat?style=social)](https://github.com/yindaheng98/TrackerSplat)  
  Keywords: 3d reconstruction, fast, robotics, 3d gaussian, ar, motion, dynamic, efficient, tracking, gaussian splatting  
- **[GEMM-GS: Accelerating 3D Gaussian Splatting on Tensor Cores with GEMM-Compatible Blending](https://arxiv.org/abs/2604.02120v2)**  
  Authors: Haomin Li, Bowen Zhu, Fangxin Liu, Zongwu Wang, Xinran Liang, Li Jiang, Haibing Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02120v2.pdf) | [![GitHub](https://img.shields.io/github/stars/shieldforever/GEMM-GS?style=social)](https://github.com/shieldforever/GEMM-GS)  
  Keywords: 3d gaussian, nerf, gaussian splatting, acceleration  
- **[GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2604.01884v1)**  
  Authors: Xianben Yang, Tao Wang, Yuxuan Li, Yi Jin, Haibin Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01884v1.pdf)  
  Keywords: compact, real-time rendering, 3d gaussian, ar, dynamic, gaussian splatting  
- **[FaCT-GS: Fast and Scalable CT Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2604.01844v1)**  
  Authors: Pawel Tomasz Pieta, Rasmus Juul Pedersen, Sina Borgi, Jakob Sauer Jørgensen, Jens Wenzel Andreasen, Vedrana Andersen Dahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01844v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PaPieta/fact-gs?style=social)](https://github.com/PaPieta/fact-gs)  
  Keywords: ar, fast, gaussian splatting  
- **[Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty-aware Differentiable Optimization](https://arxiv.org/abs/2604.01030v1)**  
  Authors: Yueh-Cheng Liu, Jozef Hladký, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01030v1.pdf)  
  Keywords: fast, 3d gaussian, ar, sparse-view, gaussian splatting  
- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394v1)**  
  Authors: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29394v1.pdf)  
  Keywords: 3d reconstruction, fast, 3d gaussian, sparse-view, ar, gaussian splatting  
- **[LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2603.28431v3)**  
  Authors: Xuan Deng, Xiandong Meng, Hengyu Man, Qiang Zhu, Tiange Zhang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28431v3.pdf)  
  Keywords: compact, head, real-time rendering, 3d gaussian, compression, nerf, geometry, ar, high-fidelity, gaussian splatting, lightweight  

### Applications

*Showing the latest 50 out of 498 papers*

- **[Visually-grounded Humanoid Agents](https://arxiv.org/abs/2604.08509v1)**  
  Authors: Hang Ye, Xiaoxuan Ma, Fan Lu, Wayne Wu, Kwan-Yee Lin, Yizhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08509v1.pdf)  
  Keywords: avatar, 3d gaussian, ar, body, human, semantic  
- **[BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields](https://arxiv.org/abs/2604.08410v1)**  
  Authors: Fan Yang, Wenrui Chen, Guorun Yan, Ruize Liao, Wanjun Jia, Dongsheng Luo, Kailun Yang, Zhiyong Li, Yaonan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08410v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PopeyePxx/BLaDA?style=social)](https://github.com/PopeyePxx/BLaDA)  
  Keywords: 3d gaussian, localization, ar, understanding, gaussian splatting, semantic  
- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370v1)**  
  Authors: Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08370v1.pdf)  
  Keywords: face, 3d gaussian, sparse-view, ar, geometry, efficient, gaussian splatting  
- **[DP-DeGauss: Dynamic Probabilistic Gaussian Decomposition for Egocentric 4D Scene Reconstruction](https://arxiv.org/abs/2604.07986v1)**  
  Authors: Tingxi Chen, Zhengxue Cheng, Houqiang Zhong, Su Wang, Rong Xie, Li Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07986v1.pdf)  
  Keywords: 3d gaussian, ar, vr, deformation, motion, 4d, dynamic, understanding  
- **[Generative 3D Gaussian Splatting for Arbitrary-ResolutionAtmospheric Downscaling and Forecasting](https://arxiv.org/abs/2604.07928v1)**  
  Authors: Tao Hana, Zhibin Wen, Zhenghao Chen, Fenghua Lin, Junyu Gao, Song Guo, Lei Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07928v1.pdf) | [![GitHub](https://img.shields.io/github/stars/binbin2xs/weather-GS?style=social)](https://github.com/binbin2xs/weather-GS)  
  Keywords: efficient, 3d gaussian, ar, gaussian splatting  
- **[ReconPhys: Reconstruct Appearance and Physical Attributes from Single Video](https://arxiv.org/abs/2604.07882v1)**  
  Authors: Boyuan Wang, Xiaofeng Wang, Yongkang Li, Zheng Zhu, Yifan Chang, Angen Ye, Guosheng Zhao, Chaojun Ni, Guan Huang, Yijie Ren, Yueqi Duan, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07882v1.pdf)  
  Keywords: fast, robotics, 3d gaussian, ar, geometry, dynamic, gaussian splatting  
- **[GEAR: GEometry-motion Alternating Refinement for Articulated Object Modeling with Gaussian Splatting](https://arxiv.org/abs/2604.07728v1)**  
  Authors: Jialin Li, Bin Fu, Ruiping Wang, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07728v1.pdf)  
  Keywords: ar, geometry, motion, high-fidelity, segmentation, gaussian splatting  
- **[From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians](https://arxiv.org/abs/2604.07337v1)**  
  Authors: Diego Gomez, Antoine Guédon, Nissim Maruani, Bingchen Gong, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07337v1.pdf)  
  Keywords: face, fast, 3d gaussian, ar, high-fidelity, gaussian splatting  
- **[Splats under Pressure: Exploring Performance-Energy Trade-offs in Real-Time 3D Gaussian Splatting under Constrained GPU Budgets](https://arxiv.org/abs/2604.07177v1)**  
  Authors: Muhammad Fahim Tajwar, Arthur Wuhrlin, Bhojan Anand  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07177v1.pdf)  
  Keywords: 3d gaussian, ar, head, gaussian splatting  
- **[Genie Sim PanoRecon: Fast Immersive Scene Generation from Single-View Panorama](https://arxiv.org/abs/2604.07105v1)**  
  Authors: Zhijun Li, Yongxin Su, Di Yang, Jichao Wang, Zheyuan Xing, Qian Wang, Maoqing Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07105v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AgibotTech/genie_sim?style=social)](https://github.com/AgibotTech/genie_sim)  
  Keywords: face, fast, 3d gaussian, ar, high-fidelity  

### Avatar Generation

*Showing the latest 50 out of 162 papers*

- **[Visually-grounded Humanoid Agents](https://arxiv.org/abs/2604.08509v1)**  
  Authors: Hang Ye, Xiaoxuan Ma, Fan Lu, Wayne Wu, Kwan-Yee Lin, Yizhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08509v1.pdf)  
  Keywords: avatar, 3d gaussian, ar, body, human, semantic  
- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370v1)**  
  Authors: Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08370v1.pdf)  
  Keywords: face, 3d gaussian, sparse-view, ar, geometry, efficient, gaussian splatting  
- **[From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians](https://arxiv.org/abs/2604.07337v1)**  
  Authors: Diego Gomez, Antoine Guédon, Nissim Maruani, Bingchen Gong, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07337v1.pdf)  
  Keywords: face, fast, 3d gaussian, ar, high-fidelity, gaussian splatting  
- **[Splats under Pressure: Exploring Performance-Energy Trade-offs in Real-Time 3D Gaussian Splatting under Constrained GPU Budgets](https://arxiv.org/abs/2604.07177v1)**  
  Authors: Muhammad Fahim Tajwar, Arthur Wuhrlin, Bhojan Anand  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07177v1.pdf)  
  Keywords: 3d gaussian, ar, head, gaussian splatting  
- **[Genie Sim PanoRecon: Fast Immersive Scene Generation from Single-View Panorama](https://arxiv.org/abs/2604.07105v1)**  
  Authors: Zhijun Li, Yongxin Su, Di Yang, Jichao Wang, Zheyuan Xing, Qian Wang, Maoqing Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07105v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AgibotTech/genie_sim?style=social)](https://github.com/AgibotTech/genie_sim)  
  Keywords: face, fast, 3d gaussian, ar, high-fidelity  
- **[Radio-Frequency Inverse Rendering for Wireless Environment Modeling](https://arxiv.org/abs/2604.07086v1)**  
  Authors: Fuhai Wang, Zihan Jin, Lehang Wang, Xuehui Dong, Tiebin Mi, Robert Caiming Qiu, Zenan ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07086v1.pdf)  
  Keywords: face, ar, geometry, neural rendering, gaussian splatting  
- **[4D Vessel Reconstruction for Benchtop Thrombectomy Analysis](https://arxiv.org/abs/2604.06671v1)**  
  Authors: Ethan Nguyen, Javier Carmona, Arisa Matsuzaki, Naoki Kaneko, Katsushi Arisaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06671v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ethanuser.github.io/vessel4D)  
  Keywords: face, ar, deformation, motion, 4d, tracking, gaussian splatting, mapping  
- **[PhysHead: Simulation-Ready Gaussian Head Avatars](https://arxiv.org/abs/2604.06467v1)**  
  Authors: Berna Kabadayi, Vanessa Sklyarova, Wojciech Zielonka, Justus Thies, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06467v1.pdf)  
  Keywords: head, avatar, 3d gaussian, ar, animation, motion, dynamic  
- **[GS-Surrogate: Deformable Gaussian Splatting for Parameter Space Exploration of Ensemble Simulations](https://arxiv.org/abs/2604.06358v1)**  
  Authors: Ziwei Li, Rumali Perera, Angus Forbes, Ken Moreland, Dave Pugmire, Scott Klasky, Wei-Lun Chao, Han-Wei Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06358v1.pdf)  
  Keywords: face, ar, deformation, efficient, gaussian splatting  
- **[Appearance Decomposition Gaussian Splatting for Multi-Traversal Reconstruction](https://arxiv.org/abs/2604.05908v1)**  
  Authors: Yangyi Xiao, Siting Zhu, Baoquan Yang, Tianchen Deng, Yongbo Chen, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05908v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRMVLab/ADM-GS?style=social)](https://github.com/IRMVLab/ADM-GS)  
  Keywords: face, lighting, reflection, autonomous driving, ar, geometry, illumination, high-fidelity, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 203 papers*

- **[DP-DeGauss: Dynamic Probabilistic Gaussian Decomposition for Egocentric 4D Scene Reconstruction](https://arxiv.org/abs/2604.07986v1)**  
  Authors: Tingxi Chen, Zhengxue Cheng, Houqiang Zhong, Su Wang, Rong Xie, Li Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07986v1.pdf)  
  Keywords: 3d gaussian, ar, vr, deformation, motion, 4d, dynamic, understanding  
- **[ReconPhys: Reconstruct Appearance and Physical Attributes from Single Video](https://arxiv.org/abs/2604.07882v1)**  
  Authors: Boyuan Wang, Xiaofeng Wang, Yongkang Li, Zheng Zhu, Yifan Chang, Angen Ye, Guosheng Zhao, Chaojun Ni, Guan Huang, Yijie Ren, Yueqi Duan, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07882v1.pdf)  
  Keywords: fast, robotics, 3d gaussian, ar, geometry, dynamic, gaussian splatting  
- **[GEAR: GEometry-motion Alternating Refinement for Articulated Object Modeling with Gaussian Splatting](https://arxiv.org/abs/2604.07728v1)**  
  Authors: Jialin Li, Bin Fu, Ruiping Wang, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07728v1.pdf)  
  Keywords: ar, geometry, motion, high-fidelity, segmentation, gaussian splatting  
- **[4D Vessel Reconstruction for Benchtop Thrombectomy Analysis](https://arxiv.org/abs/2604.06671v1)**  
  Authors: Ethan Nguyen, Javier Carmona, Arisa Matsuzaki, Naoki Kaneko, Katsushi Arisaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06671v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ethanuser.github.io/vessel4D)  
  Keywords: face, ar, deformation, motion, 4d, tracking, gaussian splatting, mapping  
- **[Spatiotemporal Gaussian representation-based dynamic reconstruction and motion estimation framework for time-resolved volumetric MR imaging (DREME-GSMR)](https://arxiv.org/abs/2604.06482v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, Can Wu, Ricardo Otazo, Jie Deng, Mu-Han Lin, Tsuicheng Chiu, Jacob Buatti, Viktor Iakovenko, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06482v1.pdf)  
  Keywords: 3d gaussian, ar, motion, dynamic, efficient, tracking  
- **[PhysHead: Simulation-Ready Gaussian Head Avatars](https://arxiv.org/abs/2604.06467v1)**  
  Authors: Berna Kabadayi, Vanessa Sklyarova, Wojciech Zielonka, Justus Thies, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06467v1.pdf)  
  Keywords: head, avatar, 3d gaussian, ar, animation, motion, dynamic  
- **[GS-Surrogate: Deformable Gaussian Splatting for Parameter Space Exploration of Ensemble Simulations](https://arxiv.org/abs/2604.06358v1)**  
  Authors: Ziwei Li, Rumali Perera, Angus Forbes, Ken Moreland, Dave Pugmire, Scott Klasky, Wei-Lun Chao, Han-Wei Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06358v1.pdf)  
  Keywords: face, ar, deformation, efficient, gaussian splatting  
- **[PanopticQuery: Unified Query-Time Reasoning for 4D Scenes](https://arxiv.org/abs/2604.05638v1)**  
  Authors: Ruilin Tang, Yang Zhou, Zhong Ye, Wenxi Liu, Yan Huang, Shengfeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05638v1.pdf)  
  Keywords: ar, 4d, dynamic, understanding, high-fidelity, gaussian splatting, semantic  
- **[Part-Level 3D Gaussian Vehicle Generation with Joint and Hinge Axis Estimation](https://arxiv.org/abs/2604.05070v1)**  
  Authors: Shiyao Qian, Yuan Ren, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05070v1.pdf)  
  Keywords: head, autonomous driving, 3d gaussian, ar, motion, dynamic, segmentation  
- **[AvatarPointillist: AutoRegressive 4D Gaussian Avatarization](https://arxiv.org/abs/2604.04787v1)**  
  Authors: Hongyu Liu, Xuan Wang, Yating Wang, Zijian Wu, Ziyu Wan, Yue Ma, Runtao Liu, Boyao Zhou, Yujun Shen, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04787v1.pdf)  
  Keywords: 3d gaussian, avatar, ar, animation, 4d, dynamic, gaussian splatting  

### Few-shot

- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370v1)**  
  Authors: Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08370v1.pdf)  
  Keywords: face, 3d gaussian, sparse-view, ar, geometry, efficient, gaussian splatting  
- **[DOC-GS: Dual-Domain Observation and Calibration for Reliable Sparse-View Gaussian Splatting](https://arxiv.org/abs/2604.06739v1)**  
  Authors: Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06739v1.pdf)  
  Keywords: 3d gaussian, sparse-view, ar, understanding, gaussian splatting  
- **[3D Gaussian Splatting for Annular Dark Field Scanning Transmission Electron Microscopy Tomography Reconstruction](https://arxiv.org/abs/2604.04693v1)**  
  Authors: Beiyuan Zhang, Hesong Li, Ruiwen Shao, Ying Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04693v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, sparse-view, ar, efficient, high-fidelity, gaussian splatting  
- **[PR-IQA: Partial-Reference Image Quality Assessment for Diffusion-Based Novel View Synthesis](https://arxiv.org/abs/2604.04576v2)**  
  Authors: Inseong Choi, Siwoo Lee, Seung-Hun Nam, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04576v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kakaomacao.github.io/pr-iqa-project-page)  
  Keywords: 3d reconstruction, 3d gaussian, sparse-view, ar, gaussian splatting  
- **[4C4D: 4 Camera 4D Gaussian Splatting](https://arxiv.org/abs/2604.04063v1)**  
  Authors: Junsheng Zhou, Zhifan Yang, Liang Han, Wenyuan Zhang, Kanle Shi, Shenkun Xu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04063v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://junshengzhou.github.io/4C4D)  
  Keywords: sparse-view, ar, geometry, 4d, dynamic, high-fidelity, gaussian splatting  
- **[Rendering Multi-Human and Multi-Object with 3D Gaussian Splatting](https://arxiv.org/abs/2604.02996v2)**  
  Authors: Weiquan Wang, Jun Xiao, Feifei Shao, Yi Yang, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02996v2.pdf)  
  Keywords: robotics, 3d gaussian, sparse-view, ar, vr, dynamic, high-fidelity, human, gaussian splatting  
- **[TRACE: High-Fidelity 3D Scene Editing via Tangible Reconstruction and Geometry-Aligned Contextual Video Masking](https://arxiv.org/abs/2604.01207v1)**  
  Authors: Jiyuan Hu, Zechuan Zhang, Zongxin Yang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01207v1.pdf)  
  Keywords: high-fidelity, ar, geometry, sparse-view  
- **[Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty-aware Differentiable Optimization](https://arxiv.org/abs/2604.01030v1)**  
  Authors: Yueh-Cheng Liu, Jozef Hladký, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01030v1.pdf)  
  Keywords: fast, 3d gaussian, ar, sparse-view, gaussian splatting  
- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394v1)**  
  Authors: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29394v1.pdf)  
  Keywords: 3d reconstruction, fast, 3d gaussian, sparse-view, ar, gaussian splatting  
- **[\textit{4DSurf}: High-Fidelity Dynamic Scene Surface Reconstruction](https://arxiv.org/abs/2603.28064v1)**  
  Authors: Renjie Wu, Hongdong Li, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28064v1.pdf)  
  Keywords: face, sparse-view, ar, geometry, 4d, dynamic, motion, deformation, high-fidelity, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 209 papers*

- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370v1)**  
  Authors: Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08370v1.pdf)  
  Keywords: face, 3d gaussian, sparse-view, ar, geometry, efficient, gaussian splatting  
- **[ReconPhys: Reconstruct Appearance and Physical Attributes from Single Video](https://arxiv.org/abs/2604.07882v1)**  
  Authors: Boyuan Wang, Xiaofeng Wang, Yongkang Li, Zheng Zhu, Yifan Chang, Angen Ye, Guosheng Zhao, Chaojun Ni, Guan Huang, Yijie Ren, Yueqi Duan, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07882v1.pdf)  
  Keywords: fast, robotics, 3d gaussian, ar, geometry, dynamic, gaussian splatting  
- **[GEAR: GEometry-motion Alternating Refinement for Articulated Object Modeling with Gaussian Splatting](https://arxiv.org/abs/2604.07728v1)**  
  Authors: Jialin Li, Bin Fu, Ruiping Wang, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07728v1.pdf)  
  Keywords: ar, geometry, motion, high-fidelity, segmentation, gaussian splatting  
- **[Radio-Frequency Inverse Rendering for Wireless Environment Modeling](https://arxiv.org/abs/2604.07086v1)**  
  Authors: Fuhai Wang, Zihan Jin, Lehang Wang, Xuehui Dong, Tiebin Mi, Robert Caiming Qiu, Zenan ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07086v1.pdf)  
  Keywords: face, ar, geometry, neural rendering, gaussian splatting  
- **[AnchorSplat: Feed-Forward 3D Gaussian Splatting with 3D Geometric Priors](https://arxiv.org/abs/2604.07053v2)**  
  Authors: Xiaoxue Zhang, Xiaoxu Zheng, Yixuan Yin, Tiao Zhao, Kaihua Tang, Michael Bi Mi, Zhan Xu, Dave Zhenyu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07053v2.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry  
- **[Appearance Decomposition Gaussian Splatting for Multi-Traversal Reconstruction](https://arxiv.org/abs/2604.05908v1)**  
  Authors: Yangyi Xiao, Siting Zhu, Baoquan Yang, Tianchen Deng, Yongbo Chen, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05908v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRMVLab/ADM-GS?style=social)](https://github.com/IRMVLab/ADM-GS)  
  Keywords: face, lighting, reflection, autonomous driving, ar, geometry, illumination, high-fidelity, gaussian splatting  
- **[GaussianGrow: Geometry-aware Gaussian Growing from 3D Point Clouds with Text Guidance](https://arxiv.org/abs/2604.05721v1)**  
  Authors: Weiqi Zhang, Junsheng Zhou, Haotian Geng, Kanle Shi, Shenkun Xu, Yi Fang, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05721v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weiqi-zhang.github.io/GaussianGrow)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry  
- **[In Depth We Trust: Reliable Monocular Depth Supervision for Gaussian Splatting](https://arxiv.org/abs/2604.05715v1)**  
  Authors: Wenhui Xiao, Ethan Goan, Rodrigo Santa Cruz, David Ahmedt-Aristizabal, Olivier Salvado, Clinton Fookes, Leo Lebrat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05715v1.pdf)  
  Keywords: face, 3d gaussian, ar, geometry, gaussian splatting  
- **[3DTurboQuant: Training-Free Near-Optimal Quantization for 3D Reconstruction Models](https://arxiv.org/abs/2604.05366v1)**  
  Authors: Jae Joong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05366v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JaeLee18/3DTurboQuant?style=social)](https://github.com/JaeLee18/3DTurboQuant)  
  Keywords: 3d reconstruction, 3d gaussian, compression, nerf, ar, gaussian splatting  
- **[SmokeGS-R: Physics-Guided Pseudo-Clean 3DGS for Real-World Multi-View Smoke Restoration](https://arxiv.org/abs/2604.05301v1)**  
  Authors: Xueming Fu, Lixia Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05301v1.pdf) | [![GitHub](https://img.shields.io/github/stars/windrise/3drr_Track2_SmokeGS-R?style=social)](https://github.com/windrise/3drr_Track2_SmokeGS-R)  
  Keywords: 3d reconstruction, 3d gaussian, ar, geometry, gaussian splatting  

### Large Scene

- **[Neural Harmonic Textures for High-Quality Primitive Based Neural Reconstruction](https://arxiv.org/abs/2604.01204v2)**  
  Authors: Jorge Condor, Nicolas Moenne-Loccoz, Merlin Nimier-David, Piotr Didyk, Zan Gojcic, Qi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01204v2.pdf)  
  Keywords: 3d gaussian, ar, large scene, gaussian splatting, semantic  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: ar, geometry, 4d, dynamic, motion, efficient, understanding, neural rendering, high-fidelity, large scene, gaussian splatting, shadow  
- **[Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting](https://arxiv.org/abs/2603.29185v1)**  
  Authors: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29185v1.pdf)  
  Keywords: outdoor, localization, ar, efficient, gaussian splatting  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: face, head, 3d gaussian, ar, efficient, neural rendering, large scene, gaussian splatting  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: head, outdoor, ar, dynamic, efficient, tracking, gaussian splatting, slam  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: outdoor, 3d gaussian, localization, ar, geometry, gaussian splatting  
- **[EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.06216v1)**  
  Authors: Miriam Jäger, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06216v1.pdf)  
  Keywords: 3d reconstruction, urban scene, face, 3d gaussian, ar, geometry, gaussian splatting  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: 3d reconstruction, lighting, fast, reflection, outdoor, 3d gaussian, ar, nerf, relightable, relighting, illumination, gaussian splatting  
- **[Interactive Augmented Reality-enabled Outdoor Scene Visualization For Enhanced Real-time Disaster Response](https://arxiv.org/abs/2602.21874v1)**  
  Authors: Dimitrios Apostolakis, Georgios Angelidis, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21874v1.pdf)  
  Keywords: face, lighting, fast, outdoor, 3d gaussian, ar, gaussian splatting, semantic, lightweight  
- **[Large-scale Photorealistic Outdoor 3D Scene Reconstruction from UAV Imagery Using Gaussian Splatting Techniques](https://arxiv.org/abs/2602.20342v1)**  
  Authors: Christos Maikos, Georgios Angelidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20342v1.pdf)  
  Keywords: 3d reconstruction, outdoor, 3d gaussian, ar, nerf, vr, efficient, neural rendering, high-fidelity, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 207 papers*

- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370v1)**  
  Authors: Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08370v1.pdf)  
  Keywords: face, 3d gaussian, sparse-view, ar, geometry, efficient, gaussian splatting  
- **[Generative 3D Gaussian Splatting for Arbitrary-ResolutionAtmospheric Downscaling and Forecasting](https://arxiv.org/abs/2604.07928v1)**  
  Authors: Tao Hana, Zhibin Wen, Zhenghao Chen, Fenghua Lin, Junyu Gao, Song Guo, Lei Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07928v1.pdf) | [![GitHub](https://img.shields.io/github/stars/binbin2xs/weather-GS?style=social)](https://github.com/binbin2xs/weather-GS)  
  Keywords: efficient, 3d gaussian, ar, gaussian splatting  
- **[Spatiotemporal Gaussian representation-based dynamic reconstruction and motion estimation framework for time-resolved volumetric MR imaging (DREME-GSMR)](https://arxiv.org/abs/2604.06482v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, Can Wu, Ricardo Otazo, Jie Deng, Mu-Han Lin, Tsuicheng Chiu, Jacob Buatti, Viktor Iakovenko, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06482v1.pdf)  
  Keywords: 3d gaussian, ar, motion, dynamic, efficient, tracking  
- **[GS-Surrogate: Deformable Gaussian Splatting for Parameter Space Exploration of Ensemble Simulations](https://arxiv.org/abs/2604.06358v1)**  
  Authors: Ziwei Li, Rumali Perera, Angus Forbes, Ken Moreland, Dave Pugmire, Scott Klasky, Wei-Lun Chao, Han-Wei Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06358v1.pdf)  
  Keywords: face, ar, deformation, efficient, gaussian splatting  
- **[3D Smoke Scene Reconstruction Guided by Vision Priors from Multimodal Large Language Models](https://arxiv.org/abs/2604.05687v1)**  
  Authors: Xinye Zheng, Fei Wang, Yiqi Nie, Kun Li, Junjie Chen, Jiaqi Zhao, Yanyan Wei, Zhiliang Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05687v1.pdf)  
  Keywords: 3d gaussian, ar, efficient, gaussian splatting, lightweight  
- **[3DTurboQuant: Training-Free Near-Optimal Quantization for 3D Reconstruction Models](https://arxiv.org/abs/2604.05366v1)**  
  Authors: Jae Joong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05366v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JaeLee18/3DTurboQuant?style=social)](https://github.com/JaeLee18/3DTurboQuant)  
  Keywords: 3d reconstruction, 3d gaussian, compression, nerf, ar, gaussian splatting  
- **[GaussFly: Contrastive Reinforcement Learning for Visuomotor Policies in 3D Gaussian Fields](https://arxiv.org/abs/2604.05062v1)**  
  Authors: Yuhang Zhang, Mingsheng Li, Yujing Shang, Zhuoyuan Yu, Chao Yan, Jiaping Xiao, Mir Feroskhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05062v1.pdf)  
  Keywords: compact, 3d gaussian, ar, high-fidelity, gaussian splatting  
- **[3D Gaussian Splatting for Annular Dark Field Scanning Transmission Electron Microscopy Tomography Reconstruction](https://arxiv.org/abs/2604.04693v1)**  
  Authors: Beiyuan Zhang, Hesong Li, Ruiwen Shao, Ying Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04693v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, sparse-view, ar, efficient, high-fidelity, gaussian splatting  
- **[CGHair: Compact Gaussian Hair Reconstruction with Card Clustering](https://arxiv.org/abs/2604.03716v1)**  
  Authors: Haimin Luo, Srinjay Sarkar, Albert Mosella-Montoro, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03716v1.pdf)  
  Keywords: compact, 3d gaussian, ar, geometry, high-fidelity, gaussian splatting  
- **[Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM](https://arxiv.org/abs/2604.03092v1)**  
  Authors: Zicheng Zhang, Ke Wu, Xiangting Meng, Keyu Liu, Jieru Zhao, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://victkk.github.io/flash-mono)  
  Keywords: lighting, compact, 3d gaussian, ar, geometry, efficient, tracking, gaussian splatting, mapping, slam  

### Quality Enhancement

*Showing the latest 50 out of 129 papers*

- **[GEAR: GEometry-motion Alternating Refinement for Articulated Object Modeling with Gaussian Splatting](https://arxiv.org/abs/2604.07728v1)**  
  Authors: Jialin Li, Bin Fu, Ruiping Wang, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07728v1.pdf)  
  Keywords: ar, geometry, motion, high-fidelity, segmentation, gaussian splatting  
- **[From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians](https://arxiv.org/abs/2604.07337v1)**  
  Authors: Diego Gomez, Antoine Guédon, Nissim Maruani, Bingchen Gong, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07337v1.pdf)  
  Keywords: face, fast, 3d gaussian, ar, high-fidelity, gaussian splatting  
- **[Genie Sim PanoRecon: Fast Immersive Scene Generation from Single-View Panorama](https://arxiv.org/abs/2604.07105v1)**  
  Authors: Zhijun Li, Yongxin Su, Di Yang, Jichao Wang, Zheyuan Xing, Qian Wang, Maoqing Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07105v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AgibotTech/genie_sim?style=social)](https://github.com/AgibotTech/genie_sim)  
  Keywords: face, fast, 3d gaussian, ar, high-fidelity  
- **[Appearance Decomposition Gaussian Splatting for Multi-Traversal Reconstruction](https://arxiv.org/abs/2604.05908v1)**  
  Authors: Yangyi Xiao, Siting Zhu, Baoquan Yang, Tianchen Deng, Yongbo Chen, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05908v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRMVLab/ADM-GS?style=social)](https://github.com/IRMVLab/ADM-GS)  
  Keywords: face, lighting, reflection, autonomous driving, ar, geometry, illumination, high-fidelity, gaussian splatting  
- **[PanopticQuery: Unified Query-Time Reasoning for 4D Scenes](https://arxiv.org/abs/2604.05638v1)**  
  Authors: Ruilin Tang, Yang Zhou, Zhong Ye, Wenxi Liu, Yan Huang, Shengfeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05638v1.pdf)  
  Keywords: ar, 4d, dynamic, understanding, high-fidelity, gaussian splatting, semantic  
- **[GaussFly: Contrastive Reinforcement Learning for Visuomotor Policies in 3D Gaussian Fields](https://arxiv.org/abs/2604.05062v1)**  
  Authors: Yuhang Zhang, Mingsheng Li, Yujing Shang, Zhuoyuan Yu, Chao Yan, Jiaping Xiao, Mir Feroskhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05062v1.pdf)  
  Keywords: compact, 3d gaussian, ar, high-fidelity, gaussian splatting  
- **[3D Gaussian Splatting for Annular Dark Field Scanning Transmission Electron Microscopy Tomography Reconstruction](https://arxiv.org/abs/2604.04693v1)**  
  Authors: Beiyuan Zhang, Hesong Li, Ruiwen Shao, Ying Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04693v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, sparse-view, ar, efficient, high-fidelity, gaussian splatting  
- **[4C4D: 4 Camera 4D Gaussian Splatting](https://arxiv.org/abs/2604.04063v1)**  
  Authors: Junsheng Zhou, Zhifan Yang, Liang Han, Wenyuan Zhang, Kanle Shi, Shenkun Xu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04063v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://junshengzhou.github.io/4C4D)  
  Keywords: sparse-view, ar, geometry, 4d, dynamic, high-fidelity, gaussian splatting  
- **[HOIGS: Human-Object Interaction Gaussian Splatting](https://arxiv.org/abs/2604.04016v1)**  
  Authors: Taewoo Kim, Suwoong Yeom, Jaehyun Pyun, Geonho Cha, Dongyoon Wee, Joonsik Nam, Yun-Seong Jeong, Kyeongbo Kong, Suk-Ju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04016v1.pdf)  
  Keywords: lighting, ar, deformation, 4d, dynamic, motion, high-fidelity, human, gaussian splatting  
- **[CGHair: Compact Gaussian Hair Reconstruction with Card Clustering](https://arxiv.org/abs/2604.03716v1)**  
  Authors: Haimin Luo, Srinjay Sarkar, Albert Mosella-Montoro, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03716v1.pdf)  
  Keywords: compact, 3d gaussian, ar, geometry, high-fidelity, gaussian splatting  

### Ray Tracing

- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: face, reflection, ar, ray tracing, gaussian splatting  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: reflection, 3d gaussian, ar, efficient, ray casting  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: face, 3d gaussian, localization, ar, efficient, ray tracing, mapping, tracking, gaussian splatting, semantic, slam  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: reflection, 3d gaussian, ar, relightable, ray tracing, gaussian splatting, mapping, shadow  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: face, path tracing, real-time rendering, 3d gaussian, ar, geometry  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: face, fast, real-time rendering, 3d gaussian, ar, nerf, geometry, efficient, high-fidelity, ray tracing, gaussian splatting  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: 3d gaussian, ar, ray tracing, survey, gaussian splatting, mapping  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: real-time rendering, ray marching, 3d gaussian, ar, efficient, high-fidelity, gaussian splatting  
- **[Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction](https://arxiv.org/abs/2603.08503v1)**  
  Authors: Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08503v1.pdf) | [![GitHub](https://img.shields.io/github/stars/1170632760/Spherical-GOF?style=social)](https://github.com/1170632760/Spherical-GOF)  
  Keywords: fast, robotics, 3d gaussian, ar, geometry, efficient, ray casting, gaussian splatting  
- **[Ref-DGS: Reflective Dual Gaussian Splatting](https://arxiv.org/abs/2603.07664v2)**  
  Authors: Ningjing Fan, Yiqun Wang, Dongming Yan, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07664v2.pdf)  
  Keywords: face, reflection, fast, ar, geometry, efficient, ray tracing, gaussian splatting, lightweight  

### Relighting

*Showing the latest 50 out of 69 papers*

- **[Appearance Decomposition Gaussian Splatting for Multi-Traversal Reconstruction](https://arxiv.org/abs/2604.05908v1)**  
  Authors: Yangyi Xiao, Siting Zhu, Baoquan Yang, Tianchen Deng, Yongbo Chen, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05908v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRMVLab/ADM-GS?style=social)](https://github.com/IRMVLab/ADM-GS)  
  Keywords: face, lighting, reflection, autonomous driving, ar, geometry, illumination, high-fidelity, gaussian splatting  
- **[HOIGS: Human-Object Interaction Gaussian Splatting](https://arxiv.org/abs/2604.04016v1)**  
  Authors: Taewoo Kim, Suwoong Yeom, Jaehyun Pyun, Geonho Cha, Dongyoon Wee, Joonsik Nam, Yun-Seong Jeong, Kyeongbo Kong, Suk-Ju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04016v1.pdf)  
  Keywords: lighting, ar, deformation, 4d, dynamic, motion, high-fidelity, human, gaussian splatting  
- **[SpectralSplat: Appearance-Disentangled Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2604.03462v1)**  
  Authors: Quentin Herau, Tianshuo Xu, Depu Meng, Jiezhi Yang, Chensheng Peng, Spencer Sherk, Yihan Hu, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03462v1.pdf)  
  Keywords: lighting, autonomous driving, 3d gaussian, ar, geometry, relighting, gaussian splatting  
- **[Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM](https://arxiv.org/abs/2604.03092v1)**  
  Authors: Zicheng Zhang, Ke Wu, Xiangting Meng, Keyu Liu, Jieru Zhao, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://victkk.github.io/flash-mono)  
  Keywords: lighting, compact, 3d gaussian, ar, geometry, efficient, tracking, gaussian splatting, mapping, slam  
- **[Streaming Real-Time Rendered Scenes as 3D Gaussians](https://arxiv.org/abs/2604.02851v1)**  
  Authors: Matti Siekkinen, Teemu Kämäräinen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02851v1.pdf)  
  Keywords: lighting, 3d gaussian, ar, dynamic, relighting, gaussian splatting  
- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2604.02781v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02781v1.pdf)  
  Keywords: reflection, 3d gaussian, geometry, dynamic, gaussian splatting, semantic  
- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: face, reflection, ar, ray tracing, gaussian splatting  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: ar, geometry, 4d, dynamic, motion, efficient, understanding, neural rendering, high-fidelity, large scene, gaussian splatting, shadow  
- **[LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting](https://arxiv.org/abs/2603.29209v1)**  
  Authors: Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29209v1.pdf)  
  Keywords: lighting, 3d gaussian, ar, vr, geometry, efficient, illumination, high-fidelity, gaussian splatting, shadow  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: reflection, 3d gaussian, ar, efficient, ray casting  

### SLAM

*Showing the latest 50 out of 78 papers*

- **[BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields](https://arxiv.org/abs/2604.08410v1)**  
  Authors: Fan Yang, Wenrui Chen, Guorun Yan, Ruize Liao, Wanjun Jia, Dongsheng Luo, Kailun Yang, Zhiyong Li, Yaonan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08410v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PopeyePxx/BLaDA?style=social)](https://github.com/PopeyePxx/BLaDA)  
  Keywords: 3d gaussian, localization, ar, understanding, gaussian splatting, semantic  
- **[4D Vessel Reconstruction for Benchtop Thrombectomy Analysis](https://arxiv.org/abs/2604.06671v1)**  
  Authors: Ethan Nguyen, Javier Carmona, Arisa Matsuzaki, Naoki Kaneko, Katsushi Arisaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06671v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ethanuser.github.io/vessel4D)  
  Keywords: face, ar, deformation, motion, 4d, tracking, gaussian splatting, mapping  
- **[Spatiotemporal Gaussian representation-based dynamic reconstruction and motion estimation framework for time-resolved volumetric MR imaging (DREME-GSMR)](https://arxiv.org/abs/2604.06482v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, Can Wu, Ricardo Otazo, Jie Deng, Mu-Han Lin, Tsuicheng Chiu, Jacob Buatti, Viktor Iakovenko, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06482v1.pdf)  
  Keywords: 3d gaussian, ar, motion, dynamic, efficient, tracking  
- **[LSGS-Loc: Towards Robust 3DGS-Based Visual Localization for Large-Scale UAV Scenarios](https://arxiv.org/abs/2604.05402v1)**  
  Authors: Xiang Zhang, Tengfei Wang, Fang Xu, Xin Wang, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05402v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xzhang-z/LSGS-Loc?style=social)](https://github.com/xzhang-z/LSGS-Loc)  
  Keywords: 3d gaussian, ar, gaussian splatting, localization  
- **[Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM](https://arxiv.org/abs/2604.03092v1)**  
  Authors: Zicheng Zhang, Ke Wu, Xiangting Meng, Keyu Liu, Jieru Zhao, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://victkk.github.io/flash-mono)  
  Keywords: lighting, compact, 3d gaussian, ar, geometry, efficient, tracking, gaussian splatting, mapping, slam  
- **[Differentiable Stroke Planning with Dual Parameterization for Efficient and High-Fidelity Painting Creation](https://arxiv.org/abs/2604.02752v1)**  
  Authors: Jinfan Liu, Wuze Zhang, Zhangli Hu, Zhehan Zhao, Ye Chen, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02752v1.pdf)  
  Keywords: efficient, high-fidelity, ar, mapping  
- **[VBGS-SLAM: Variational Bayesian Gaussian Splatting Simultaneous Localization and Mapping](https://arxiv.org/abs/2604.02696v1)**  
  Authors: Yuhan Zhu, Yanyu Zhang, Jie Xu, Wei Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02696v1.pdf)  
  Keywords: 3d gaussian, localization, ar, efficient, tracking, gaussian splatting, mapping, slam  
- **[TrackerSplat: Exploiting Point Tracking for Fast and Robust Dynamic 3D Gaussians Reconstruction](https://arxiv.org/abs/2604.02586v1)**  
  Authors: Daheng Yin, Isaac Ding, Yili Jin, Jianxin Shi, Jiangchuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02586v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yindaheng98/TrackerSplat?style=social)](https://github.com/yindaheng98/TrackerSplat)  
  Keywords: 3d reconstruction, fast, robotics, 3d gaussian, ar, motion, dynamic, efficient, tracking, gaussian splatting  
- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: face, ar, geometry, 4d, dynamic, motion, understanding, high-fidelity, human, segmentation, tracking, gaussian splatting, semantic  
- **[Satellite-Free Training for Drone-View Geo-Localization](https://arxiv.org/abs/2604.01581v2)**  
  Authors: Tao Liu, Yingzhi Zhang, Kan Ren, Xiaoqi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01581v2.pdf)  
  Keywords: 3d gaussian, localization, ar, geometry, gaussian splatting, lightweight  

### Scene Understanding

*Showing the latest 50 out of 131 papers*

- **[Visually-grounded Humanoid Agents](https://arxiv.org/abs/2604.08509v1)**  
  Authors: Hang Ye, Xiaoxuan Ma, Fan Lu, Wayne Wu, Kwan-Yee Lin, Yizhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08509v1.pdf)  
  Keywords: avatar, 3d gaussian, ar, body, human, semantic  
- **[BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields](https://arxiv.org/abs/2604.08410v1)**  
  Authors: Fan Yang, Wenrui Chen, Guorun Yan, Ruize Liao, Wanjun Jia, Dongsheng Luo, Kailun Yang, Zhiyong Li, Yaonan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08410v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PopeyePxx/BLaDA?style=social)](https://github.com/PopeyePxx/BLaDA)  
  Keywords: 3d gaussian, localization, ar, understanding, gaussian splatting, semantic  
- **[DP-DeGauss: Dynamic Probabilistic Gaussian Decomposition for Egocentric 4D Scene Reconstruction](https://arxiv.org/abs/2604.07986v1)**  
  Authors: Tingxi Chen, Zhengxue Cheng, Houqiang Zhong, Su Wang, Rong Xie, Li Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07986v1.pdf)  
  Keywords: 3d gaussian, ar, vr, deformation, motion, 4d, dynamic, understanding  
- **[GEAR: GEometry-motion Alternating Refinement for Articulated Object Modeling with Gaussian Splatting](https://arxiv.org/abs/2604.07728v1)**  
  Authors: Jialin Li, Bin Fu, Ruiping Wang, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07728v1.pdf)  
  Keywords: ar, geometry, motion, high-fidelity, segmentation, gaussian splatting  
- **[DOC-GS: Dual-Domain Observation and Calibration for Reliable Sparse-View Gaussian Splatting](https://arxiv.org/abs/2604.06739v1)**  
  Authors: Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06739v1.pdf)  
  Keywords: 3d gaussian, sparse-view, ar, understanding, gaussian splatting  
- **[PanopticQuery: Unified Query-Time Reasoning for 4D Scenes](https://arxiv.org/abs/2604.05638v1)**  
  Authors: Ruilin Tang, Yang Zhou, Zhong Ye, Wenxi Liu, Yan Huang, Shengfeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05638v1.pdf)  
  Keywords: ar, 4d, dynamic, understanding, high-fidelity, gaussian splatting, semantic  
- **[Indoor Asset Detection in Large Scale 360° Drone-Captured Imagery via 3D Gaussian Splatting](https://arxiv.org/abs/2604.05316v1)**  
  Authors: Monica Tang, Avideh Zakhor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05316v1.pdf)  
  Keywords: 3d gaussian, ar, segmentation, gaussian splatting, semantic  
- **[Part-Level 3D Gaussian Vehicle Generation with Joint and Hinge Axis Estimation](https://arxiv.org/abs/2604.05070v1)**  
  Authors: Shiyao Qian, Yuan Ren, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05070v1.pdf)  
  Keywords: head, autonomous driving, 3d gaussian, ar, motion, dynamic, segmentation  
- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2604.02781v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02781v1.pdf)  
  Keywords: reflection, 3d gaussian, geometry, dynamic, gaussian splatting, semantic  
- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: head, 3d gaussian, ar, deformation, 4d, dynamic, motion, high-fidelity, segmentation, gaussian splatting, lightweight  



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