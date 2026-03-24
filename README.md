# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-03-24 01:09:22

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

- [3DGS Surveys](#3dgs-surveys) (7 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (118 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (499 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (164 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (207 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (31 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (203 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (16 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (215 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (132 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (19 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (70 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (77 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (135 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: 3d gaussian, vr, gaussian splatting, survey, ar  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v1)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v1.pdf)  
  Keywords: ray tracing, 3d gaussian, gaussian splatting, survey, ar, mapping  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: 3d gaussian, face, dynamic, motion, gaussian splatting, survey, slam, localization, tracking, ar, efficient, mapping  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: robotics, 3d gaussian, gaussian splatting, survey, ar  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v3)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v3.pdf)  
  Keywords: 3d gaussian, gaussian splatting, geometry, survey, ar, efficient, nerf  
- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197v1)**  
  Authors: Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07197v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, high-fidelity, gaussian splatting, dynamic, survey, compression, ar, compact, efficient, 4d  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v2)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v2.pdf)  
  Keywords: robotics, 3d gaussian, semantic, mapping, gaussian splatting, slam, survey, localization, ar, nerf, understanding  

### Acceleration

*Showing the latest 50 out of 118 papers*

- **[Fast and Robust Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2603.20857v1)**  
  Authors: Han Jiao, Jiakai Sun, Lei Zhao, Zhanjie Zhang, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20857v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, dynamic, gaussian splatting, fast, ar, efficient, deformation  
- **[GaussianPile: A Unified Sparse Gaussian Splatting Framework for Slice-based Volumetric Reconstruction](https://arxiv.org/abs/2603.20611v1)**  
  Authors: Di Kong, Yikai Wang, Wenjie Guo, Yifan Bu, Boya Zhang, Yuexin Duan, Xiawei Yue, Wenbiao Du, Yiman Zhong, Yuwen Chen, Cheng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20611v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, gaussian splatting, compression, fast, ar, compact, nerf  
- **[TRGS-SLAM: IMU-Aided Gaussian Splatting SLAM for Blurry, Rolling Shutter, and Noisy Thermal Images](https://arxiv.org/abs/2603.20443v1)**  
  Authors: Spencer Carmichael, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20443v1.pdf)  
  Keywords: robotics, illumination, 3d gaussian, dynamic, gaussian splatting, motion, slam, localization, fast, tracking, ar, mapping  
- **[Fourier Splatting: Generalized Fourier encoded primitives for scalable radiance fields](https://arxiv.org/abs/2603.19834v1)**  
  Authors: Mihnea-Bogdan Jurca, Bert Van hauwermeiren, Adrian Munteanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19834v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, high-fidelity, gaussian splatting, ar, efficient  
- **[GHOST: Fast Category-agnostic Hand-Object Interaction Reconstruction from RGB Videos using Gaussian Splatting](https://arxiv.org/abs/2603.18912v1)**  
  Authors: Ahmed Tawfik Aboukhadra, Marcel Rogge, Nadia Robertini, Abdalla Arafa, Jameel Malik, Ahmed Elhayek, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18912v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ATAboukhadra/GHOST?style=social)](https://github.com/ATAboukhadra/GHOST)  
  Keywords: robotics, vr, 3d reconstruction, dynamic, gaussian splatting, fast, ar, efficient, understanding  
- **[Adaptive Anchor Policies for Efficient 4D Gaussian Streaming](https://arxiv.org/abs/2603.17227v1)**  
  Authors: Ashim Dahal, Rabab Abdelfattah, Nick Rahimi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17227v1.pdf)  
  Keywords: real-time rendering, dynamic, gaussian splatting, fast, ar, efficient, 4d  
- **[Feed-forward Gaussian Registration for Head Avatar Creation and Editing](https://arxiv.org/abs/2603.15811v1)**  
  Authors: Malte Prinzler, Paulo Gotardo, Siyu Tang, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15811v1.pdf)  
  Keywords: semantic, geometry, head, fast, avatar, tracking, ar  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: 3d gaussian, real-time rendering, high-fidelity, gaussian splatting, ray marching, ar, efficient  
- **[E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction](https://arxiv.org/abs/2603.14684v1)**  
  Authors: Yunsoo Kim, Changki Sung, Dasol Hong, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14684v1.pdf)  
  Keywords: lighting, 3d gaussian, 3d reconstruction, dynamic, gaussian splatting, motion, fast, tracking, ar, nerf  
- **[Scene Generation at Absolute Scale: Utilizing Semantic and Geometric Guidance From Text for Accurate and Interpretable 3D Indoor Scene Generation](https://arxiv.org/abs/2603.13910v1)**  
  Authors: Stefan Ainetter, Thomas Deixelberger, Edoardo A. Dominici, Philipp Drescher, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13910v1.pdf)  
  Keywords: 3d gaussian, semantic, gaussian splatting, fast, ar  

### Applications

*Showing the latest 50 out of 499 papers*

- **[Two Experts Are Better Than One Generalist: Decoupling Geometry and Appearance for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.21064v1)**  
  Authors: Hwasik Jeong, Seungryong Lee, Gyeongjin Kang, Seungkwon Yang, Xiangyu Sun, Seungtae Nam, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21064v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, geometry, ar  
- **[SGAD-SLAM: Splatting Gaussians at Adjusted Depth for Better Radiance Fields in RGBD SLAM](https://arxiv.org/abs/2603.21055v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21055v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/SGAD-SLAM-Project)  
  Keywords: 3d gaussian, slam, gaussian splatting, tracking, ar, mapping  
- **[Fast and Robust Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2603.20857v1)**  
  Authors: Han Jiao, Jiakai Sun, Lei Zhao, Zhanjie Zhang, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20857v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, dynamic, gaussian splatting, fast, ar, efficient, deformation  
- **[Glove2Hand: Synthesizing Natural Hand-Object Interaction from Multi-Modal Sensing Gloves](https://arxiv.org/abs/2603.20850v1)**  
  Authors: Xinyu Zhang, Ziyi Kou, Chuan Qin, Mia Huang, Ergys Ristani, Ankit Kumar, Lele Chen, Kun He, Abdeslam Boularias, Li Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20850v1.pdf)  
  Keywords: robotics, 3d gaussian, vr, dynamic, motion, tracking, ar, deformation, understanding  
- **[The Role and Relationship of Initialization and Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.20714v1)**  
  Authors: Ivan Desiatov, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20714v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, motion, gaussian splatting, geometry, ar, efficient  
- **[GaussianPile: A Unified Sparse Gaussian Splatting Framework for Slice-based Volumetric Reconstruction](https://arxiv.org/abs/2603.20611v1)**  
  Authors: Di Kong, Yikai Wang, Wenjie Guo, Yifan Bu, Boya Zhang, Yuexin Duan, Xiawei Yue, Wenbiao Du, Yiman Zhong, Yuwen Chen, Cheng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20611v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, gaussian splatting, compression, fast, ar, compact, nerf  
- **[Nevis Digital Twin: Photogrammetry and Immersive Visualization of Historical Sites](https://arxiv.org/abs/2603.20560v1)**  
  Authors: Alex Apffel, Huy Tran, Vuthea Chheang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20560v1.pdf)  
  Keywords: 3d gaussian, vr, gaussian splatting, survey, ar  
- **[TRGS-SLAM: IMU-Aided Gaussian Splatting SLAM for Blurry, Rolling Shutter, and Noisy Thermal Images](https://arxiv.org/abs/2603.20443v1)**  
  Authors: Spencer Carmichael, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20443v1.pdf)  
  Keywords: robotics, illumination, 3d gaussian, dynamic, gaussian splatting, motion, slam, localization, fast, tracking, ar, mapping  
- **[Benchmarking Efficient & Effective Camera Pose Estimation Strategies for Novel View Synthesis](https://arxiv.org/abs/2603.20428v1)**  
  Authors: Jhacson Meza, Martin R. Oswald, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20428v1.pdf)  
  Keywords: motion, geometry, ar, efficient, nerf  
- **[Fourier Splatting: Generalized Fourier encoded primitives for scalable radiance fields](https://arxiv.org/abs/2603.19834v1)**  
  Authors: Mihnea-Bogdan Jurca, Bert Van hauwermeiren, Adrian Munteanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19834v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, high-fidelity, gaussian splatting, ar, efficient  

### Avatar Generation

*Showing the latest 50 out of 164 papers*

- **[3D Gaussian Splatting with Self-Constrained Priors for High Fidelity Surface Reconstruction](https://arxiv.org/abs/2603.19682v1)**  
  Authors: Takeshi Noda, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19682v1.pdf)  
  Keywords: 3d gaussian, face, gaussian splatting, geometry, ar, nerf  
- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: 3d gaussian, face, semantic, mapping, gaussian splatting, segmentation, slam, ar, lighting, understanding  
- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: 3d gaussian, gaussian splatting, body, head, avatar, ar, human  
- **[CrowdGaussian: Reconstructing High-Fidelity 3D Gaussians for Human Crowd from a Single Image](https://arxiv.org/abs/2603.17779v1)**  
  Authors: Yizheng Song, Yiyu Zhuang, Qipeng Xu, Haixiang Wang, Jiahe Zhu, Jing Tian, Siyu Zhu, Hao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17779v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, geometry, ar, human  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: face, 3d reconstruction, high-fidelity, dynamic, geometry, neural rendering, ar  
- **[SMAL-pets: SMAL Based Avatars of Pets from Single Image](https://arxiv.org/abs/2603.17131v1)**  
  Authors: Piotr Borycki, Joanna Waczyńska, Yizhe Zhu, Yongqiang Gao, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17131v1.pdf)  
  Keywords: 3d gaussian, face, animation, high-fidelity, gaussian splatting, avatar, ar, human  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: dynamic, gaussian splatting, slam, outdoor, head, tracking, ar, efficient  
- **[ProgressiveAvatars: Progressive Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2603.16447v1)**  
  Authors: Kaiwen Song, Jinkai Cui, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16447v1.pdf)  
  Keywords: 3d gaussian, face, motion, head, avatar, ar  
- **[Feed-forward Gaussian Registration for Head Avatar Creation and Editing](https://arxiv.org/abs/2603.15811v1)**  
  Authors: Malte Prinzler, Paulo Gotardo, Siyu Tang, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15811v1.pdf)  
  Keywords: semantic, geometry, head, fast, avatar, tracking, ar  
- **[KGS-GCN: Enhancing Sparse Skeleton Sensing via Kinematics-Driven Gaussian Splatting and Probabilistic Topology for Action Recognition](https://arxiv.org/abs/2603.16943v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Liping Zhang, Jie Li, Jiaxin Gao, Wenbo Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16943v1.pdf)  
  Keywords: semantic, recognition, dynamic, gaussian splatting, ar, human  

### Dynamic Scene

*Showing the latest 50 out of 207 papers*

- **[Fast and Robust Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2603.20857v1)**  
  Authors: Han Jiao, Jiakai Sun, Lei Zhao, Zhanjie Zhang, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20857v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, dynamic, gaussian splatting, fast, ar, efficient, deformation  
- **[Glove2Hand: Synthesizing Natural Hand-Object Interaction from Multi-Modal Sensing Gloves](https://arxiv.org/abs/2603.20850v1)**  
  Authors: Xinyu Zhang, Ziyi Kou, Chuan Qin, Mia Huang, Ergys Ristani, Ankit Kumar, Lele Chen, Kun He, Abdeslam Boularias, Li Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20850v1.pdf)  
  Keywords: robotics, 3d gaussian, vr, dynamic, motion, tracking, ar, deformation, understanding  
- **[The Role and Relationship of Initialization and Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.20714v1)**  
  Authors: Ivan Desiatov, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20714v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, motion, gaussian splatting, geometry, ar, efficient  
- **[TRGS-SLAM: IMU-Aided Gaussian Splatting SLAM for Blurry, Rolling Shutter, and Noisy Thermal Images](https://arxiv.org/abs/2603.20443v1)**  
  Authors: Spencer Carmichael, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20443v1.pdf)  
  Keywords: robotics, illumination, 3d gaussian, dynamic, gaussian splatting, motion, slam, localization, fast, tracking, ar, mapping  
- **[Benchmarking Efficient & Effective Camera Pose Estimation Strategies for Novel View Synthesis](https://arxiv.org/abs/2603.20428v1)**  
  Authors: Jhacson Meza, Martin R. Oswald, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20428v1.pdf)  
  Keywords: motion, geometry, ar, efficient, nerf  
- **[StreetForward: Perceiving Dynamic Street with Feedforward Causal Attention](https://arxiv.org/abs/2603.19552v1)**  
  Authors: Zhongrui Yu, Zhao Wang, Yijia Xie, Yida Wang, Xueyang Zhang, Yifei Zhan, Kun Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19552v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://streetforward.github.io)  
  Keywords: 3d gaussian, high-fidelity, dynamic, gaussian splatting, geometry, motion, ar, efficient, autonomous driving  
- **[Zero Shot Deformation Reconstruction for Soft Robots Using a Flexible Sensor Array and Cage Based 3D Gaussian Modeling](https://arxiv.org/abs/2603.19543v1)**  
  Authors: Linrui Shou, Zilang Chen, Wenjia Xu, Yiyue Luo, Tingyu Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19543v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, ar, deformation  
- **[Reconstruction Matters: Learning Geometry-Aligned BEV Representation through 3D Gaussian Splatting](https://arxiv.org/abs/2603.19193v1)**  
  Authors: Yiren Lu, Xin Ye, Burhaneddin Yaman, Jingru Luo, Zhexiao Xiong, Liu Ren, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19193v1.pdf)  
  Keywords: 3d gaussian, semantic, 3d reconstruction, motion, gaussian splatting, segmentation, geometry, ar, understanding, autonomous driving  
- **[GHOST: Fast Category-agnostic Hand-Object Interaction Reconstruction from RGB Videos using Gaussian Splatting](https://arxiv.org/abs/2603.18912v1)**  
  Authors: Ahmed Tawfik Aboukhadra, Marcel Rogge, Nadia Robertini, Abdalla Arafa, Jameel Malik, Ahmed Elhayek, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18912v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ATAboukhadra/GHOST?style=social)](https://github.com/ATAboukhadra/GHOST)  
  Keywords: robotics, vr, 3d reconstruction, dynamic, gaussian splatting, fast, ar, efficient, understanding  
- **[Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning](https://arxiv.org/abs/2603.18402v1)**  
  Authors: Yonghan Lee, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18402v1.pdf)  
  Keywords: motion, dynamic, segmentation, gaussian splatting, tracking, ar, 4d  

### Few-shot

- **[UniSem: Generalizable Semantic 3D Reconstruction from Sparse Unposed Images](https://arxiv.org/abs/2603.17519v1)**  
  Authors: Guibiao Liao, Qian Ren, Kaimin Liao, Hua Wang, Zhi Chen, Luchao Wang, Yaohua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17519v1.pdf)  
  Keywords: sparse-view, 3d gaussian, semantic, 3d reconstruction, gaussian splatting, segmentation, geometry, ar  
- **[S2D: Sparse to Dense Lifting for 3D Reconstruction with Minimal Inputs](https://arxiv.org/abs/2603.10893v1)**  
  Authors: Yuzhou Ji, Qijian Tian, He Zhu, Xiaoqi Jiang, Guangzhi Cao, Lizhuang Ma, Yuan Xie, Xin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10893v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, high-fidelity, sparse view, gaussian splatting, ar, efficient, understanding  
- **[Active View Selection with Perturbed Gaussian Ensemble for Tomographic Reconstruction](https://arxiv.org/abs/2603.06852v1)**  
  Authors: Yulun Wu, Ruyi Zha, Wei Cao, Yingying Li, Yuanhao Cai, Yaoyao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06852v1.pdf)  
  Keywords: sparse-view, 3d gaussian, gaussian splatting, fast, ar  
- **[CylinderSplat: 3D Gaussian Splatting with Cylindrical Triplanes for Panoramic Novel View Synthesis](https://arxiv.org/abs/2603.05882v1)**  
  Authors: Qiwei Wang, Xianghui Ze, Jingyi Yu, Yujiao Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05882v1.pdf)  
  Keywords: sparse-view, 3d gaussian, gaussian splatting, geometry, ar  
- **[DSA-SRGS: Super-Resolution Gaussian Splatting for Dynamic Sparse-View DSA Reconstruction](https://arxiv.org/abs/2603.04770v1)**  
  Authors: Shiyu Zhang, Zhicong Wu, Huangxuan Zhao, Zhentao Liu, Lei Chen, Yong Luo, Lefei Zhang, Zhiming Cui, Ziwen Ke, Bo Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04770v1.pdf)  
  Keywords: sparse-view, dynamic, gaussian splatting, ar, 4d  
- **[Intrinsic Geometry-Appearance Consistency Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2603.02893v1)**  
  Authors: Kaiqiang Xiong, Rui Peng, Jiahao Wu, Zhanke Wang, Jie Liang, Xiaoyun Zheng, Feng Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02893v1.pdf)  
  Keywords: sparse-view, 3d gaussian, high-fidelity, gaussian splatting, geometry, ar, human  
- **[Multimodal-Prior-Guided Importance Sampling for Hierarchical Gaussian Splatting in Sparse-View Novel View Synthesis](https://arxiv.org/abs/2603.02866v1)**  
  Authors: Kaiqiang Xiong, Zhanke Wang, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02866v1.pdf)  
  Keywords: sparse-view, 3d gaussian, semantic, gaussian splatting, ar  
- **[SemGS: Feed-Forward Semantic 3D Gaussian Splatting from Sparse Views for Generalizable Scene Understanding](https://arxiv.org/abs/2603.02548v1)**  
  Authors: Sheng Ye, Zhen-Hui Dong, Ruoyu Fan, Tian Lv, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02548v1.pdf)  
  Keywords: 3d gaussian, semantic, sparse view, gaussian splatting, ar, understanding  
- **[Sparse View Distractor-Free Gaussian Splatting](https://arxiv.org/abs/2603.01603v1)**  
  Authors: Yi Gu, Zhaorui Wang, Jiahang Cao, Jiaxu Wang, Mingle Zhao, Dongjun Ye, Renjing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01603v1.pdf)  
  Keywords: sparse-view, 3d gaussian, semantic, sparse view, gaussian splatting, geometry, fast, ar, efficient  
- **[HeroGS: Hierarchical Guidance for Robust 3D Gaussian Splatting under Sparse Views](https://arxiv.org/abs/2603.01099v2)**  
  Authors: Jiashu Li, Xumeng Han, Zhaoyang Wei, Zipeng Wang, Kuiran Wang, Guorong Li, Zhenjun Han, Jianbin Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01099v2.pdf)  
  Keywords: sparse-view, 3d gaussian, high-fidelity, sparse view, gaussian splatting, geometry, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 203 papers*

- **[Two Experts Are Better Than One Generalist: Decoupling Geometry and Appearance for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.21064v1)**  
  Authors: Hwasik Jeong, Seungryong Lee, Gyeongjin Kang, Seungkwon Yang, Xiangyu Sun, Seungtae Nam, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21064v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, geometry, ar  
- **[The Role and Relationship of Initialization and Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.20714v1)**  
  Authors: Ivan Desiatov, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20714v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, motion, gaussian splatting, geometry, ar, efficient  
- **[Benchmarking Efficient & Effective Camera Pose Estimation Strategies for Novel View Synthesis](https://arxiv.org/abs/2603.20428v1)**  
  Authors: Jhacson Meza, Martin R. Oswald, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20428v1.pdf)  
  Keywords: motion, geometry, ar, efficient, nerf  
- **[HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks](https://arxiv.org/abs/2603.19822v1)**  
  Authors: Jingyu Guo, Ziye Chen, Ziwen Li, Zhengqing Gao, Jiaxin Huang, Hanlue Zhang, Fengming Huang, Yu Yao, Tongliang Liu, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19822v1.pdf)  
  Keywords: 3d gaussian, semantic, gaussian splatting, geometry, ar, lighting  
- **[3D Gaussian Splatting with Self-Constrained Priors for High Fidelity Surface Reconstruction](https://arxiv.org/abs/2603.19682v1)**  
  Authors: Takeshi Noda, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19682v1.pdf)  
  Keywords: 3d gaussian, face, gaussian splatting, geometry, ar, nerf  
- **[StreetForward: Perceiving Dynamic Street with Feedforward Causal Attention](https://arxiv.org/abs/2603.19552v1)**  
  Authors: Zhongrui Yu, Zhao Wang, Yijia Xie, Yida Wang, Xueyang Zhang, Yifei Zhan, Kun Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19552v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://streetforward.github.io)  
  Keywords: 3d gaussian, high-fidelity, dynamic, gaussian splatting, geometry, motion, ar, efficient, autonomous driving  
- **[Zero Shot Deformation Reconstruction for Soft Robots Using a Flexible Sensor Array and Cage Based 3D Gaussian Modeling](https://arxiv.org/abs/2603.19543v1)**  
  Authors: Linrui Shou, Zilang Chen, Wenjia Xu, Yiyue Luo, Tingyu Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19543v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, ar, deformation  
- **[Reconstruction Matters: Learning Geometry-Aligned BEV Representation through 3D Gaussian Splatting](https://arxiv.org/abs/2603.19193v1)**  
  Authors: Yiren Lu, Xin Ye, Burhaneddin Yaman, Jingru Luo, Zhexiao Xiong, Liu Ren, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19193v1.pdf)  
  Keywords: 3d gaussian, semantic, 3d reconstruction, motion, gaussian splatting, segmentation, geometry, ar, understanding, autonomous driving  
- **[GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning](https://arxiv.org/abs/2603.19137v1)**  
  Authors: Yiren Lu, Yi Du, Disheng Liu, Yunlai Zhou, Chen Wang, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19137v1.pdf)  
  Keywords: 3d gaussian, semantic, high-fidelity, gaussian splatting, geometry, ar  
- **[GHOST: Fast Category-agnostic Hand-Object Interaction Reconstruction from RGB Videos using Gaussian Splatting](https://arxiv.org/abs/2603.18912v1)**  
  Authors: Ahmed Tawfik Aboukhadra, Marcel Rogge, Nadia Robertini, Abdalla Arafa, Jameel Malik, Ahmed Elhayek, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18912v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ATAboukhadra/GHOST?style=social)](https://github.com/ATAboukhadra/GHOST)  
  Keywords: robotics, vr, 3d reconstruction, dynamic, gaussian splatting, fast, ar, efficient, understanding  

### Large Scene

- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: dynamic, gaussian splatting, slam, outdoor, head, tracking, ar, efficient  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, outdoor, geometry, localization, ar  
- **[EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.06216v1)**  
  Authors: Miriam Jäger, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06216v1.pdf)  
  Keywords: 3d gaussian, face, 3d reconstruction, gaussian splatting, geometry, urban scene, ar  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: illumination, lighting, 3d gaussian, reflection, relighting, relightable, 3d reconstruction, gaussian splatting, outdoor, fast, ar, nerf  
- **[Interactive Augmented Reality-enabled Outdoor Scene Visualization For Enhanced Real-time Disaster Response](https://arxiv.org/abs/2602.21874v1)**  
  Authors: Dimitrios Apostolakis, Georgios Angelidis, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21874v1.pdf)  
  Keywords: 3d gaussian, face, semantic, gaussian splatting, lightweight, outdoor, fast, ar, lighting  
- **[Large-scale Photorealistic Outdoor 3D Scene Reconstruction from UAV Imagery Using Gaussian Splatting Techniques](https://arxiv.org/abs/2602.20342v1)**  
  Authors: Christos Maikos, Georgios Angelidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20342v1.pdf)  
  Keywords: 3d gaussian, vr, 3d reconstruction, high-fidelity, gaussian splatting, neural rendering, outdoor, ar, efficient, nerf  
- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: 3d gaussian, semantic, gaussian splatting, outdoor, geometry, localization, head, ar, lighting, mapping  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: illumination, lighting, 3d gaussian, real-time rendering, global illumination, gaussian splatting, outdoor, ar, nerf, autonomous driving  
- **[Zero-Shot UAV Navigation in Forests via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2602.07101v2)**  
  Authors: Zinan Lv, Yeqian Qian, Chen Sang, Hao Liu, Danping Zou, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07101v2.pdf)  
  Keywords: illumination, 3d gaussian, relightable, high-fidelity, gaussian splatting, dynamic, geometry, outdoor, lightweight, ar, lighting  
- **[3DGS$^2$-TR: Scalable Second-Order Trust-Region Method for 3D Gaussian Splatting](https://arxiv.org/abs/2602.00395v1)**  
  Authors: Roger Hsiao, Yuchen Fang, Xiangru Huang, Ruilong Li, Hesam Rabeti, Zan Gojcic, Javad Lavaei, James Demmel, Sophia Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00395v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, ar, efficient, large scene  

### Model Compression

*Showing the latest 50 out of 215 papers*

- **[Fast and Robust Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2603.20857v1)**  
  Authors: Han Jiao, Jiakai Sun, Lei Zhao, Zhanjie Zhang, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20857v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, dynamic, gaussian splatting, fast, ar, efficient, deformation  
- **[The Role and Relationship of Initialization and Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.20714v1)**  
  Authors: Ivan Desiatov, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20714v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, motion, gaussian splatting, geometry, ar, efficient  
- **[GaussianPile: A Unified Sparse Gaussian Splatting Framework for Slice-based Volumetric Reconstruction](https://arxiv.org/abs/2603.20611v1)**  
  Authors: Di Kong, Yikai Wang, Wenjie Guo, Yifan Bu, Boya Zhang, Yuexin Duan, Xiawei Yue, Wenbiao Du, Yiman Zhong, Yuwen Chen, Cheng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20611v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, gaussian splatting, compression, fast, ar, compact, nerf  
- **[Benchmarking Efficient & Effective Camera Pose Estimation Strategies for Novel View Synthesis](https://arxiv.org/abs/2603.20428v1)**  
  Authors: Jhacson Meza, Martin R. Oswald, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20428v1.pdf)  
  Keywords: motion, geometry, ar, efficient, nerf  
- **[Fourier Splatting: Generalized Fourier encoded primitives for scalable radiance fields](https://arxiv.org/abs/2603.19834v1)**  
  Authors: Mihnea-Bogdan Jurca, Bert Van hauwermeiren, Adrian Munteanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19834v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, high-fidelity, gaussian splatting, ar, efficient  
- **[StreetForward: Perceiving Dynamic Street with Feedforward Causal Attention](https://arxiv.org/abs/2603.19552v1)**  
  Authors: Zhongrui Yu, Zhao Wang, Yijia Xie, Yida Wang, Xueyang Zhang, Yifei Zhan, Kun Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19552v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://streetforward.github.io)  
  Keywords: 3d gaussian, high-fidelity, dynamic, gaussian splatting, geometry, motion, ar, efficient, autonomous driving  
- **[GHOST: Fast Category-agnostic Hand-Object Interaction Reconstruction from RGB Videos using Gaussian Splatting](https://arxiv.org/abs/2603.18912v1)**  
  Authors: Ahmed Tawfik Aboukhadra, Marcel Rogge, Nadia Robertini, Abdalla Arafa, Jameel Malik, Ahmed Elhayek, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18912v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ATAboukhadra/GHOST?style=social)](https://github.com/ATAboukhadra/GHOST)  
  Keywords: robotics, vr, 3d reconstruction, dynamic, gaussian splatting, fast, ar, efficient, understanding  
- **[OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2603.18510v1)**  
  Authors: Hongjia Zhai, Qi Zhang, Xiaokun Pan, Xiyu Zhang, Yitong Dong, Huaqi Zhang, Dan Xu, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18510v1.pdf)  
  Keywords: 3d gaussian, semantic, mapping, gaussian splatting, ar, efficient, understanding  
- **[ReLaGS: Relational Language Gaussian Splatting](https://arxiv.org/abs/2603.17605v1)**  
  Authors: Yaxu Xie, Abdalla Arafa, Alireza Javanmardi, Christen Millerdurai, Jia Cheng Hu, Shaoxiang Wang, Alain Pagani, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17605v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dfki-av.github.io/ReLaGS)  
  Keywords: semantic, gaussian splatting, segmentation, geometry, ar, efficient, understanding  
- **[Adaptive Anchor Policies for Efficient 4D Gaussian Streaming](https://arxiv.org/abs/2603.17227v1)**  
  Authors: Ashim Dahal, Rabab Abdelfattah, Nick Rahimi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17227v1.pdf)  
  Keywords: real-time rendering, dynamic, gaussian splatting, fast, ar, efficient, 4d  

### Quality Enhancement

*Showing the latest 50 out of 132 papers*

- **[Two Experts Are Better Than One Generalist: Decoupling Geometry and Appearance for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.21064v1)**  
  Authors: Hwasik Jeong, Seungryong Lee, Gyeongjin Kang, Seungkwon Yang, Xiangyu Sun, Seungtae Nam, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21064v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, geometry, ar  
- **[Fourier Splatting: Generalized Fourier encoded primitives for scalable radiance fields](https://arxiv.org/abs/2603.19834v1)**  
  Authors: Mihnea-Bogdan Jurca, Bert Van hauwermeiren, Adrian Munteanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19834v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, high-fidelity, gaussian splatting, ar, efficient  
- **[StreetForward: Perceiving Dynamic Street with Feedforward Causal Attention](https://arxiv.org/abs/2603.19552v1)**  
  Authors: Zhongrui Yu, Zhao Wang, Yijia Xie, Yida Wang, Xueyang Zhang, Yifei Zhan, Kun Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19552v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://streetforward.github.io)  
  Keywords: 3d gaussian, high-fidelity, dynamic, gaussian splatting, geometry, motion, ar, efficient, autonomous driving  
- **[GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning](https://arxiv.org/abs/2603.19137v1)**  
  Authors: Yiren Lu, Yi Du, Disheng Liu, Yunlai Zhou, Chen Wang, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19137v1.pdf)  
  Keywords: 3d gaussian, semantic, high-fidelity, gaussian splatting, geometry, ar  
- **[CrowdGaussian: Reconstructing High-Fidelity 3D Gaussians for Human Crowd from a Single Image](https://arxiv.org/abs/2603.17779v1)**  
  Authors: Yizheng Song, Yiyu Zhuang, Qipeng Xu, Haixiang Wang, Jiahe Zhu, Jing Tian, Siyu Zhu, Hao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17779v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, geometry, ar, human  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: face, 3d reconstruction, high-fidelity, dynamic, geometry, neural rendering, ar  
- **[SMAL-pets: SMAL Based Avatars of Pets from Single Image](https://arxiv.org/abs/2603.17131v1)**  
  Authors: Piotr Borycki, Joanna Waczyńska, Yizhe Zhu, Yongqiang Gao, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17131v1.pdf)  
  Keywords: 3d gaussian, face, animation, high-fidelity, gaussian splatting, avatar, ar, human  
- **[MessyKitchens: Contact-rich object-level 3D scene reconstruction](https://arxiv.org/abs/2603.16868v1)**  
  Authors: Junaid Ahmed Ansari, Ran Ding, Fabio Pizzati, Ivan Laptev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16868v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://messykitchens.github.io)  
  Keywords: ar, robotics, animation, high-fidelity  
- **[NanoGS: Training-Free Gaussian Splat Simplification](https://arxiv.org/abs/2603.16103v1)**  
  Authors: Butian Xiong, Rong Liu, Tiantian Zhou, Meida Chen, Zhiwen Fan, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16103v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://saliteta.github.io/NanoGS)  
  Keywords: 3d gaussian, high-fidelity, lightweight, ar, compact, efficient, compression  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: 3d gaussian, real-time rendering, high-fidelity, gaussian splatting, ray marching, ar, efficient  

### Ray Tracing

- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v1)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v1.pdf)  
  Keywords: ray tracing, 3d gaussian, gaussian splatting, survey, ar, mapping  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: 3d gaussian, real-time rendering, high-fidelity, gaussian splatting, ray marching, ar, efficient  
- **[Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction](https://arxiv.org/abs/2603.08503v1)**  
  Authors: Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08503v1.pdf) | [![GitHub](https://img.shields.io/github/stars/1170632760/Spherical-GOF?style=social)](https://github.com/1170632760/Spherical-GOF)  
  Keywords: robotics, 3d gaussian, gaussian splatting, geometry, fast, ar, efficient, ray casting  
- **[Ref-DGS: Reflective Dual Gaussian Splatting](https://arxiv.org/abs/2603.07664v2)**  
  Authors: Ningjing Fan, Yiqun Wang, Dongming Yan, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07664v2.pdf)  
  Keywords: ray tracing, face, reflection, gaussian splatting, lightweight, geometry, fast, ar, efficient  
- **[Radiometrically Consistent Gaussian Surfels for Inverse Rendering](https://arxiv.org/abs/2603.01491v1)**  
  Authors: Kyu Beom Han, Jaeyoon Kim, Woo Jae Kim, Jinhwan Seo, Sung-eui Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01491v1.pdf)  
  Keywords: ray tracing, illumination, reflection, relighting, global illumination, gaussian splatting, ar, efficient, lighting  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: illumination, lighting, 3d gaussian, real-time rendering, global illumination, gaussian splatting, outdoor, ar, nerf, autonomous driving  
- **[Rotated Lights for Consistent and Efficient 2D Gaussians Inverse Rendering](https://arxiv.org/abs/2602.08724v1)**  
  Authors: Geng Lin, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08724v1.pdf)  
  Keywords: shadow, illumination, relighting, global illumination, gaussian splatting, geometry, ar, efficient, lighting  
- **[Radioactive 3D Gaussian Ray Tracing for Tomographic Reconstruction](https://arxiv.org/abs/2602.01057v1)**  
  Authors: Ling Chen, Bao Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01057v1.pdf)  
  Keywords: ar, ray tracing, 3d gaussian, gaussian splatting  
- **[EAG-PT: Emission-Aware Gaussians and Path Tracing for Indoor Scene Reconstruction and Editing](https://arxiv.org/abs/2601.23065v1)**  
  Authors: Xijie Yang, Mulin Yu, Changjian Jiang, Kerui Ren, Tao Lu, Jiangmiao Pang, Dahua Lin, Bo Dai, Linning Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.23065v1.pdf)  
  Keywords: path tracing, light transport, illumination, geometry, ar, efficient, nerf  
- **[Hybrid Foveated Path Tracing with Peripheral Gaussians for Immersive Anatomy](https://arxiv.org/abs/2601.22026v1)**  
  Authors: Constantin Kleinbeck, Luisa Theelke, Hannah Schieber, Ulrich Eck, Rüdiger von Eisenhart-Rothe, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22026v1.pdf)  
  Keywords: path tracing, vr, lightweight, gaussian splatting, medical, head, ar, understanding  

### Relighting

*Showing the latest 50 out of 70 papers*

- **[TRGS-SLAM: IMU-Aided Gaussian Splatting SLAM for Blurry, Rolling Shutter, and Noisy Thermal Images](https://arxiv.org/abs/2603.20443v1)**  
  Authors: Spencer Carmichael, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20443v1.pdf)  
  Keywords: robotics, illumination, 3d gaussian, dynamic, gaussian splatting, motion, slam, localization, fast, tracking, ar, mapping  
- **[HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks](https://arxiv.org/abs/2603.19822v1)**  
  Authors: Jingyu Guo, Ziye Chen, Ziwen Li, Zhengqing Gao, Jiaxin Huang, Hanlue Zhang, Fengming Huang, Yu Yao, Tongliang Liu, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19822v1.pdf)  
  Keywords: 3d gaussian, semantic, gaussian splatting, geometry, ar, lighting  
- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: 3d gaussian, face, semantic, mapping, gaussian splatting, segmentation, slam, ar, lighting, understanding  
- **[E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction](https://arxiv.org/abs/2603.14684v1)**  
  Authors: Yunsoo Kim, Changki Sung, Dasol Hong, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14684v1.pdf)  
  Keywords: lighting, 3d gaussian, 3d reconstruction, dynamic, gaussian splatting, motion, fast, tracking, ar, nerf  
- **[PhyGaP: Physically-Grounded Gaussians with Polarization Cues](https://arxiv.org/abs/2603.14001v1)**  
  Authors: Jiale Wu, Xiaoyang Bai, Zongqi He, Weiwei Xu, Yifan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14001v1.pdf)  
  Keywords: 3d gaussian, face, reflection, relighting, high-fidelity, gaussian splatting, ar, lighting  
- **[LR-SGS: Robust LiDAR-Reflectance-Guided Salient Gaussian Splatting for Self-Driving Scene Reconstruction](https://arxiv.org/abs/2603.12647v1)**  
  Authors: Ziyu Chen, Fan Zhu, Hui Zhu, Deyi Kong, Xinkai Kuang, Yujia Zhang, Chunmao Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12647v1.pdf)  
  Keywords: 3d gaussian, motion, gaussian splatting, ar, efficient, lighting  
- **[InstantHDR: Single-forward Gaussian Splatting for High Dynamic Range 3D Reconstruction](https://arxiv.org/abs/2603.11298v2)**  
  Authors: Dingqiang Ye, Jiacong Xu, Jianglu Ping, Yuxiang Guo, Chao Fan, Vishal M. Patel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11298v2.pdf)  
  Keywords: 3d reconstruction, dynamic, gaussian splatting, geometry, ar, lighting, mapping  
- **[Ref-DGS: Reflective Dual Gaussian Splatting](https://arxiv.org/abs/2603.07664v2)**  
  Authors: Ningjing Fan, Yiqun Wang, Dongming Yan, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07664v2.pdf)  
  Keywords: ray tracing, face, reflection, gaussian splatting, lightweight, geometry, fast, ar, efficient  
- **[3DGS-HPC: Distractor-free 3D Gaussian Splatting with Hybrid Patch-wise Classification](https://arxiv.org/abs/2603.07587v1)**  
  Authors: Jiahao Chen, Yipeng Qin, Ganlong Zhao, Xin Li, Wenping Wang, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07587v1.pdf)  
  Keywords: shadow, 3d gaussian, semantic, gaussian splatting, ar  
- **[Spectral Probing of Feature Upsamplers in 2D-to-3D Scene Reconstruction](https://arxiv.org/abs/2603.05787v1)**  
  Authors: Ling Xiao, Yuliang Xiu, Yue Chen, Guoming Wang, Toshihiko Yamasaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05787v1.pdf)  
  Keywords: geometry, lighting, 3d reconstruction, ar  

### SLAM

*Showing the latest 50 out of 77 papers*

- **[SGAD-SLAM: Splatting Gaussians at Adjusted Depth for Better Radiance Fields in RGBD SLAM](https://arxiv.org/abs/2603.21055v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21055v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/SGAD-SLAM-Project)  
  Keywords: 3d gaussian, slam, gaussian splatting, tracking, ar, mapping  
- **[Glove2Hand: Synthesizing Natural Hand-Object Interaction from Multi-Modal Sensing Gloves](https://arxiv.org/abs/2603.20850v1)**  
  Authors: Xinyu Zhang, Ziyi Kou, Chuan Qin, Mia Huang, Ergys Ristani, Ankit Kumar, Lele Chen, Kun He, Abdeslam Boularias, Li Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20850v1.pdf)  
  Keywords: robotics, 3d gaussian, vr, dynamic, motion, tracking, ar, deformation, understanding  
- **[TRGS-SLAM: IMU-Aided Gaussian Splatting SLAM for Blurry, Rolling Shutter, and Noisy Thermal Images](https://arxiv.org/abs/2603.20443v1)**  
  Authors: Spencer Carmichael, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20443v1.pdf)  
  Keywords: robotics, illumination, 3d gaussian, dynamic, gaussian splatting, motion, slam, localization, fast, tracking, ar, mapping  
- **[OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2603.18510v1)**  
  Authors: Hongjia Zhai, Qi Zhang, Xiaokun Pan, Xiyu Zhang, Yitong Dong, Huaqi Zhang, Dan Xu, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18510v1.pdf)  
  Keywords: 3d gaussian, semantic, mapping, gaussian splatting, ar, efficient, understanding  
- **[Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning](https://arxiv.org/abs/2603.18402v1)**  
  Authors: Yonghan Lee, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18402v1.pdf)  
  Keywords: motion, dynamic, segmentation, gaussian splatting, tracking, ar, 4d  
- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: 3d gaussian, face, semantic, mapping, gaussian splatting, segmentation, slam, ar, lighting, understanding  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v1)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v1.pdf)  
  Keywords: ray tracing, 3d gaussian, gaussian splatting, survey, ar, mapping  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: dynamic, gaussian splatting, slam, outdoor, head, tracking, ar, efficient  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, outdoor, geometry, localization, ar  
- **[OGScene3D: Incremental Open-Vocabulary 3D Gaussian Scene Graph Mapping for Scene Understanding](https://arxiv.org/abs/2603.16301v2)**  
  Authors: Siting Zhu, Ziyun Lu, Guangming Wang, Chenguang Huang, Yongbo Chen, I-Ming Chen, Wolfram Burgard, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16301v2.pdf)  
  Keywords: 3d gaussian, semantic, mapping, dynamic, ar, understanding  

### Scene Understanding

*Showing the latest 50 out of 135 papers*

- **[Glove2Hand: Synthesizing Natural Hand-Object Interaction from Multi-Modal Sensing Gloves](https://arxiv.org/abs/2603.20850v1)**  
  Authors: Xinyu Zhang, Ziyi Kou, Chuan Qin, Mia Huang, Ergys Ristani, Ankit Kumar, Lele Chen, Kun He, Abdeslam Boularias, Li Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20850v1.pdf)  
  Keywords: robotics, 3d gaussian, vr, dynamic, motion, tracking, ar, deformation, understanding  
- **[HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks](https://arxiv.org/abs/2603.19822v1)**  
  Authors: Jingyu Guo, Ziye Chen, Ziwen Li, Zhengqing Gao, Jiaxin Huang, Hanlue Zhang, Fengming Huang, Yu Yao, Tongliang Liu, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19822v1.pdf)  
  Keywords: 3d gaussian, semantic, gaussian splatting, geometry, ar, lighting  
- **[Reconstruction Matters: Learning Geometry-Aligned BEV Representation through 3D Gaussian Splatting](https://arxiv.org/abs/2603.19193v1)**  
  Authors: Yiren Lu, Xin Ye, Burhaneddin Yaman, Jingru Luo, Zhexiao Xiong, Liu Ren, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19193v1.pdf)  
  Keywords: 3d gaussian, semantic, 3d reconstruction, motion, gaussian splatting, segmentation, geometry, ar, understanding, autonomous driving  
- **[GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning](https://arxiv.org/abs/2603.19137v1)**  
  Authors: Yiren Lu, Yi Du, Disheng Liu, Yunlai Zhou, Chen Wang, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19137v1.pdf)  
  Keywords: 3d gaussian, semantic, high-fidelity, gaussian splatting, geometry, ar  
- **[GHOST: Fast Category-agnostic Hand-Object Interaction Reconstruction from RGB Videos using Gaussian Splatting](https://arxiv.org/abs/2603.18912v1)**  
  Authors: Ahmed Tawfik Aboukhadra, Marcel Rogge, Nadia Robertini, Abdalla Arafa, Jameel Malik, Ahmed Elhayek, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18912v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ATAboukhadra/GHOST?style=social)](https://github.com/ATAboukhadra/GHOST)  
  Keywords: robotics, vr, 3d reconstruction, dynamic, gaussian splatting, fast, ar, efficient, understanding  
- **[OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2603.18510v1)**  
  Authors: Hongjia Zhai, Qi Zhang, Xiaokun Pan, Xiyu Zhang, Yitong Dong, Huaqi Zhang, Dan Xu, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18510v1.pdf)  
  Keywords: 3d gaussian, semantic, mapping, gaussian splatting, ar, efficient, understanding  
- **[Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning](https://arxiv.org/abs/2603.18402v1)**  
  Authors: Yonghan Lee, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18402v1.pdf)  
  Keywords: motion, dynamic, segmentation, gaussian splatting, tracking, ar, 4d  
- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: 3d gaussian, face, semantic, mapping, gaussian splatting, segmentation, slam, ar, lighting, understanding  
- **[ReLaGS: Relational Language Gaussian Splatting](https://arxiv.org/abs/2603.17605v1)**  
  Authors: Yaxu Xie, Abdalla Arafa, Alireza Javanmardi, Christen Millerdurai, Jia Cheng Hu, Shaoxiang Wang, Alain Pagani, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17605v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dfki-av.github.io/ReLaGS)  
  Keywords: semantic, gaussian splatting, segmentation, geometry, ar, efficient, understanding  
- **[UniSem: Generalizable Semantic 3D Reconstruction from Sparse Unposed Images](https://arxiv.org/abs/2603.17519v1)**  
  Authors: Guibiao Liao, Qian Ren, Kaimin Liao, Hua Wang, Zhi Chen, Luchao Wang, Yaohua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17519v1.pdf)  
  Keywords: sparse-view, 3d gaussian, semantic, 3d reconstruction, gaussian splatting, segmentation, geometry, ar  



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