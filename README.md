# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-03-08 01:12:03

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
- [Acceleration](#acceleration) (110 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (499 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (164 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (208 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (37 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (202 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (18 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (214 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (129 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (15 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (73 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (76 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (127 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: survey, efficient, localization, dynamic, mapping, slam, tracking, ar, gaussian splatting, motion, face, 3d gaussian  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: survey, ar, gaussian splatting, robotics, 3d gaussian  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v2)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v2.pdf)  
  Keywords: survey, efficient, geometry, ar, nerf, gaussian splatting, 3d gaussian  
- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197v1)**  
  Authors: Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07197v1.pdf)  
  Keywords: survey, efficient, dynamic, compact, ar, 4d, gaussian splatting, high-fidelity, compression, 3d gaussian, 3d reconstruction  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v2)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v2.pdf)  
  Keywords: survey, localization, slam, ar, semantic, nerf, gaussian splatting, robotics, mapping, understanding, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 110 papers*

- **[GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins](https://arxiv.org/abs/2603.05108v1)**  
  Authors: Yichen Cai, Paul Jansonnie, Cristiana de Farias, Oleg Arenz, Jan Peters  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05108v1.pdf)  
  Keywords: efficient, dynamic, efficient rendering, tracking, ar, gaussian splatting, segmentation  
- **[GloSplat: Joint Pose-Appearance Optimization for Faster and More Accurate 3D Reconstruction](https://arxiv.org/abs/2603.04847v1)**  
  Authors: Tianyu Xiong, Rui Li, Linjie Li, Jiaqi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04847v1.pdf)  
  Keywords: efficient, ar, nerf, gaussian splatting, motion, fast, 3d gaussian, 3d reconstruction  
- **[LLM-supported 3D Modeling Tool for Radio Radiance Field Reconstruction](https://arxiv.org/abs/2603.04368v1)**  
  Authors: Chengling Xu, Huiwen Zhang, Haijian Sun, Feng Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04368v1.pdf)  
  Keywords: ar, fast, geometry, semantic  
- **[Generalized non-exponential Gaussian splatting](https://arxiv.org/abs/2603.02887v2)**  
  Authors: Sébastien Speierer, Adrian Jarabo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02887v2.pdf)  
  Keywords: fast, gaussian splatting, 3d gaussian, ar  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: relightable, illumination, outdoor, relighting, reflection, ar, nerf, gaussian splatting, lighting, fast, 3d gaussian, 3d reconstruction  
- **[Sparse View Distractor-Free Gaussian Splatting](https://arxiv.org/abs/2603.01603v1)**  
  Authors: Yi Gu, Zhaorui Wang, Jiahang Cao, Jiaxu Wang, Mingle Zhao, Dongjun Ye, Renjing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01603v1.pdf)  
  Keywords: efficient, sparse-view, geometry, ar, semantic, gaussian splatting, sparse view, fast, 3d gaussian  
- **[GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction](https://arxiv.org/abs/2602.24161v1)**  
  Authors: Chao Xu, Xiaochen Zhao, Xiang Deng, Jingxiang Sun, Zhuo Su, Donglin Di, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24161v1.pdf)  
  Keywords: real-time rendering, geometry, ar, 4d, head, high-fidelity, face, avatar, 3d gaussian  
- **[Prune Wisely, Reconstruct Sharply: Compact 3D Gaussian Splatting via Adaptive Pruning and Difference-of-Gaussian Primitives](https://arxiv.org/abs/2602.24136v1)**  
  Authors: Haoran Wang, Guoxi Huang, Fan Zhang, David Bull, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24136v1.pdf)  
  Keywords: real-time rendering, efficient, compact, ar, gaussian splatting, 3d gaussian  
- **[SwiftNDC: Fast Neural Depth Correction for High-Fidelity 3D Reconstruction](https://arxiv.org/abs/2602.22565v1)**  
  Authors: Kang Han, Wei Xiang, Lu Yu, Mathew Wyatt, Gaowen Liu, Ramana Rao Kompella  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22565v1.pdf)  
  Keywords: efficient, geometry, ar, gaussian splatting, lighting, high-fidelity, fast, face, 3d gaussian, 3d reconstruction  
- **[Interactive Augmented Reality-enabled Outdoor Scene Visualization For Enhanced Real-time Disaster Response](https://arxiv.org/abs/2602.21874v1)**  
  Authors: Dimitrios Apostolakis, Georgios Angelidis, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21874v1.pdf)  
  Keywords: outdoor, lightweight, ar, semantic, gaussian splatting, lighting, fast, face, 3d gaussian  

### Applications

*Showing the latest 50 out of 499 papers*

- **[SSR-GS: Separating Specular Reflection in Gaussian Splatting for Glossy Surface Reconstruction](https://arxiv.org/abs/2603.05152v1)**  
  Authors: Ningjing Fan, Yiqun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05152v1.pdf)  
  Keywords: efficient, illumination, geometry, reflection, ar, gaussian splatting, face, 3d gaussian  
- **[GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins](https://arxiv.org/abs/2603.05108v1)**  
  Authors: Yichen Cai, Paul Jansonnie, Cristiana de Farias, Oleg Arenz, Jan Peters  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05108v1.pdf)  
  Keywords: efficient, dynamic, efficient rendering, tracking, ar, gaussian splatting, segmentation  
- **[Orthogonal Spatial-temporal Distributional Transfer for 4D Generation](https://arxiv.org/abs/2603.05081v1)**  
  Authors: Wei Liu, Shengqiong Wu, Bobo Li, Haoyu Zhao, Hao Fei, Mong-Li Lee, Wynne Hsu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05081v1.pdf)  
  Keywords: 4d, deformation, ar  
- **[GloSplat: Joint Pose-Appearance Optimization for Faster and More Accurate 3D Reconstruction](https://arxiv.org/abs/2603.04847v1)**  
  Authors: Tianyu Xiong, Rui Li, Linjie Li, Jiaqi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04847v1.pdf)  
  Keywords: efficient, ar, nerf, gaussian splatting, motion, fast, 3d gaussian, 3d reconstruction  
- **[DSA-SRGS: Super-Resolution Gaussian Splatting for Dynamic Sparse-View DSA Reconstruction](https://arxiv.org/abs/2603.04770v1)**  
  Authors: Shiyu Zhang, Zhicong Wu, Huangxuan Zhao, Zhentao Liu, Lei Chen, Yong Luo, Lefei Zhang, Zhiming Cui, Ziwen Ke, Bo Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04770v1.pdf)  
  Keywords: sparse-view, dynamic, ar, 4d, gaussian splatting  
- **[LLM-supported 3D Modeling Tool for Radio Radiance Field Reconstruction](https://arxiv.org/abs/2603.04368v1)**  
  Authors: Chengling Xu, Huiwen Zhang, Haijian Sun, Feng Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04368v1.pdf)  
  Keywords: ar, fast, geometry, semantic  
- **[Gaussian Wardrobe: Compositional 3D Gaussian Avatars for Free-Form Virtual Try-On](https://arxiv.org/abs/2603.04290v2)**  
  Authors: Zhiyi Chen, Hsuan-I Ho, Tianjian Jiang, Jie Song, Manuel Kaufmann, Chen Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04290v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ait.ethz.ch/gaussianwardrobe)  
  Keywords: body, dynamic, ar, human, high-fidelity, avatar, 3d gaussian  
- **[EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2603.04254v1)**  
  Authors: Seungjun Lee, Zihan Wang, Yunsong Wang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04254v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://0nandon.github.io/EmbodiedSplat)  
  Keywords: efficient, ar, semantic, understanding, 3d gaussian, 3d reconstruction  
- **[DM-CFO: A Diffusion Model for Compositional 3D Tooth Generation with Collision-Free Optimization](https://arxiv.org/abs/2603.03602v1)**  
  Authors: Yan Tian, Pengcheng Xue, Weiping Ding, Mahmoud Hassaballah, Karen Egiazarian, Aura Conci, Abdulkadir Sengur, Leszek Rutkowski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03602v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://amateurc.github.io/CF-3DTeeth)  
  Keywords: face, 3d gaussian, ar  
- **[VIRGi: View-dependent Instant Recoloring of 3D Gaussians Splats](https://arxiv.org/abs/2603.02986v1)**  
  Authors: Alessio Mazzucchelli, Ivan Ojeda-Martin, Fernando Rivas-Manzaneque, Elena Garces, Adrian Penate-Sanchez, Francesc Moreno-Noguer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02986v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, segmentation, 3d gaussian, 3d reconstruction  

### Avatar Generation

*Showing the latest 50 out of 164 papers*

- **[SSR-GS: Separating Specular Reflection in Gaussian Splatting for Glossy Surface Reconstruction](https://arxiv.org/abs/2603.05152v1)**  
  Authors: Ningjing Fan, Yiqun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05152v1.pdf)  
  Keywords: efficient, illumination, geometry, reflection, ar, gaussian splatting, face, 3d gaussian  
- **[Gaussian Wardrobe: Compositional 3D Gaussian Avatars for Free-Form Virtual Try-On](https://arxiv.org/abs/2603.04290v2)**  
  Authors: Zhiyi Chen, Hsuan-I Ho, Tianjian Jiang, Jie Song, Manuel Kaufmann, Chen Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04290v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ait.ethz.ch/gaussianwardrobe)  
  Keywords: body, dynamic, ar, human, high-fidelity, avatar, 3d gaussian  
- **[DM-CFO: A Diffusion Model for Compositional 3D Tooth Generation with Collision-Free Optimization](https://arxiv.org/abs/2603.03602v1)**  
  Authors: Yan Tian, Pengcheng Xue, Weiping Ding, Mahmoud Hassaballah, Karen Egiazarian, Aura Conci, Abdulkadir Sengur, Leszek Rutkowski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03602v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://amateurc.github.io/CF-3DTeeth)  
  Keywords: face, 3d gaussian, ar  
- **[Intrinsic Geometry-Appearance Consistency Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2603.02893v1)**  
  Authors: Kaiqiang Xiong, Rui Peng, Jiahao Wu, Zhanke Wang, Jie Liang, Xiaoyun Zheng, Feng Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02893v1.pdf)  
  Keywords: sparse-view, geometry, ar, gaussian splatting, human, high-fidelity, 3d gaussian  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: efficient, animation, ar, gaussian splatting, head, high-fidelity, avatar, 3d gaussian  
- **[FLICKER: A Fine-Grained Contribution-Aware Accelerator for Real-Time 3D Gaussian Splatting](https://arxiv.org/abs/2603.01158v1)**  
  Authors: Wenhui Ou, Zhuoyu Wu, Yipu Zhang, Dongjun Wu, Freddy Ziyang Hong, Chik Patrick Yue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01158v1.pdf)  
  Keywords: vr, ar, gaussian splatting, head, 3d gaussian  
- **[D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping](https://arxiv.org/abs/2603.01151v1)**  
  Authors: Haozhe Lou, Mingtong Zhang, Haoran Geng, Hanyang Zhou, Sicheng He, Zhiyuan Gao, Siheng Zhao, Jiageng Mao, Pieter Abbeel, Jitendra Malik, Daniel Seita, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01151v1.pdf)  
  Keywords: human, dynamic, high-fidelity, ar  
- **[GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction](https://arxiv.org/abs/2602.24161v1)**  
  Authors: Chao Xu, Xiaochen Zhao, Xiang Deng, Jingxiang Sun, Zhuo Su, Donglin Di, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24161v1.pdf)  
  Keywords: real-time rendering, geometry, ar, 4d, head, high-fidelity, face, avatar, 3d gaussian  
- **[Latent Gaussian Splatting for 4D Panoptic Occupancy Tracking](https://arxiv.org/abs/2602.23172v1)**  
  Authors: Maximilian Luz, Rohit Mohan, Thomas Nürnberg, Yakov Miron, Daniele Cattaneo, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23172v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lags.cs.uni-freiburg.de)  
  Keywords: efficient, dynamic, tracking, ar, 4d, gaussian splatting, head, segmentation, understanding, 3d gaussian  
- **[SwiftNDC: Fast Neural Depth Correction for High-Fidelity 3D Reconstruction](https://arxiv.org/abs/2602.22565v1)**  
  Authors: Kang Han, Wei Xiang, Lu Yu, Mathew Wyatt, Gaowen Liu, Ramana Rao Kompella  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22565v1.pdf)  
  Keywords: efficient, geometry, ar, gaussian splatting, lighting, high-fidelity, fast, face, 3d gaussian, 3d reconstruction  

### Dynamic Scene

*Showing the latest 50 out of 208 papers*

- **[GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins](https://arxiv.org/abs/2603.05108v1)**  
  Authors: Yichen Cai, Paul Jansonnie, Cristiana de Farias, Oleg Arenz, Jan Peters  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05108v1.pdf)  
  Keywords: efficient, dynamic, efficient rendering, tracking, ar, gaussian splatting, segmentation  
- **[Orthogonal Spatial-temporal Distributional Transfer for 4D Generation](https://arxiv.org/abs/2603.05081v1)**  
  Authors: Wei Liu, Shengqiong Wu, Bobo Li, Haoyu Zhao, Hao Fei, Mong-Li Lee, Wynne Hsu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05081v1.pdf)  
  Keywords: 4d, deformation, ar  
- **[GloSplat: Joint Pose-Appearance Optimization for Faster and More Accurate 3D Reconstruction](https://arxiv.org/abs/2603.04847v1)**  
  Authors: Tianyu Xiong, Rui Li, Linjie Li, Jiaqi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04847v1.pdf)  
  Keywords: efficient, ar, nerf, gaussian splatting, motion, fast, 3d gaussian, 3d reconstruction  
- **[DSA-SRGS: Super-Resolution Gaussian Splatting for Dynamic Sparse-View DSA Reconstruction](https://arxiv.org/abs/2603.04770v1)**  
  Authors: Shiyu Zhang, Zhicong Wu, Huangxuan Zhao, Zhentao Liu, Lei Chen, Yong Luo, Lefei Zhang, Zhiming Cui, Ziwen Ke, Bo Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04770v1.pdf)  
  Keywords: sparse-view, dynamic, ar, 4d, gaussian splatting  
- **[Gaussian Wardrobe: Compositional 3D Gaussian Avatars for Free-Form Virtual Try-On](https://arxiv.org/abs/2603.04290v2)**  
  Authors: Zhiyi Chen, Hsuan-I Ho, Tianjian Jiang, Jie Song, Manuel Kaufmann, Chen Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04290v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ait.ethz.ch/gaussianwardrobe)  
  Keywords: body, dynamic, ar, human, high-fidelity, avatar, 3d gaussian  
- **[Articulation in Motion: Prior-free Part Mobility Analysis for Articulated Objects By Dynamic-Static Disentanglement](https://arxiv.org/abs/2603.02910v1)**  
  Authors: Hao Ai, Wenjie Chang, Jianbo Jiao, Ales Leonardis, Ofek Eyal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02910v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haoai-1997.github.io/AiM)  
  Keywords: dynamic, ar, segmentation, motion, 3d gaussian  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: efficient, animation, ar, gaussian splatting, head, high-fidelity, avatar, 3d gaussian  
- **[D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping](https://arxiv.org/abs/2603.01151v1)**  
  Authors: Haozhe Lou, Mingtong Zhang, Haoran Geng, Hanyang Zhou, Sicheng He, Zhiyuan Gao, Siheng Zhao, Jiageng Mao, Pieter Abbeel, Jitendra Malik, Daniel Seita, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01151v1.pdf)  
  Keywords: human, dynamic, high-fidelity, ar  
- **[Decoupling Motion and Geometry in 4D Gaussian Splatting](https://arxiv.org/abs/2603.00952v1)**  
  Authors: Yi Zhang, Yulei Kang, Jian-Fang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00952v1.pdf)  
  Keywords: geometry, dynamic, ar, 4d, gaussian splatting, high-fidelity, motion, deformation  
- **[UFO-4D: Unposed Feedforward 4D Reconstruction from Two Images](https://arxiv.org/abs/2602.24290v2)**  
  Authors: Junhwa Hur, Charles Herrmann, Songyou Peng, Philipp Henzler, Zeyu Ma, Todd Zickler, Deqing Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24290v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ufo-4d.github.io)  
  Keywords: geometry, dynamic, ar, 4d, high-fidelity, motion, 3d gaussian  

### Few-shot

- **[DSA-SRGS: Super-Resolution Gaussian Splatting for Dynamic Sparse-View DSA Reconstruction](https://arxiv.org/abs/2603.04770v1)**  
  Authors: Shiyu Zhang, Zhicong Wu, Huangxuan Zhao, Zhentao Liu, Lei Chen, Yong Luo, Lefei Zhang, Zhiming Cui, Ziwen Ke, Bo Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04770v1.pdf)  
  Keywords: sparse-view, dynamic, ar, 4d, gaussian splatting  
- **[Intrinsic Geometry-Appearance Consistency Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2603.02893v1)**  
  Authors: Kaiqiang Xiong, Rui Peng, Jiahao Wu, Zhanke Wang, Jie Liang, Xiaoyun Zheng, Feng Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02893v1.pdf)  
  Keywords: sparse-view, geometry, ar, gaussian splatting, human, high-fidelity, 3d gaussian  
- **[Multimodal-Prior-Guided Importance Sampling for Hierarchical Gaussian Splatting in Sparse-View Novel View Synthesis](https://arxiv.org/abs/2603.02866v1)**  
  Authors: Kaiqiang Xiong, Zhanke Wang, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02866v1.pdf)  
  Keywords: sparse-view, ar, semantic, gaussian splatting, 3d gaussian  
- **[SemGS: Feed-Forward Semantic 3D Gaussian Splatting from Sparse Views for Generalizable Scene Understanding](https://arxiv.org/abs/2603.02548v1)**  
  Authors: Sheng Ye, Zhen-Hui Dong, Ruoyu Fan, Tian Lv, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02548v1.pdf)  
  Keywords: ar, semantic, gaussian splatting, sparse view, understanding, 3d gaussian  
- **[Sparse View Distractor-Free Gaussian Splatting](https://arxiv.org/abs/2603.01603v1)**  
  Authors: Yi Gu, Zhaorui Wang, Jiahang Cao, Jiaxu Wang, Mingle Zhao, Dongjun Ye, Renjing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01603v1.pdf)  
  Keywords: efficient, sparse-view, geometry, ar, semantic, gaussian splatting, sparse view, fast, 3d gaussian  
- **[HeroGS: Hierarchical Guidance for Robust 3D Gaussian Splatting under Sparse Views](https://arxiv.org/abs/2603.01099v2)**  
  Authors: Jiashu Li, Xumeng Han, Zhaoyang Wei, Zipeng Wang, Kuiran Wang, Guorong Li, Zhenjun Han, Jianbin Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01099v2.pdf)  
  Keywords: sparse-view, geometry, ar, gaussian splatting, high-fidelity, sparse view, 3d gaussian  
- **[GIFSplat: Generative Prior-Guided Iterative Feed-Forward 3D Gaussian Splatting from Sparse Views](https://arxiv.org/abs/2602.22571v1)**  
  Authors: Tianyu Chen, Wei Xiang, Kang Han, Yu Lu, Di Wu, Gaowen Liu, Ramana Rao Kompella  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22571v1.pdf)  
  Keywords: ar, gaussian splatting, sparse view, 3d gaussian, 3d reconstruction  
- **[Dropping Anchor and Spherical Harmonics for Sparse-view Gaussian Splatting](https://arxiv.org/abs/2602.20933v1)**  
  Authors: Shuangkang Fang, I-Chao Shen, Xuanyang Zhang, Zesheng Wang, Yufeng Wang, Wenrui Ding, Gang Yu, Takeo Igarashi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20933v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sk-fun.fun/DropAnSH-GS)  
  Keywords: efficient, sparse-view, ar, gaussian splatting, head, compression, 3d gaussian  
- **[TG-Field: Geometry-Aware Radiative Gaussian Fields for Tomographic Reconstruction](https://arxiv.org/abs/2602.11705v1)**  
  Authors: Yuxiang Zhong, Jun Wei, Chaoqi Chen, Senyou An, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11705v1.pdf)  
  Keywords: sparse-view, geometry, dynamic, ar, gaussian splatting, motion, deformation, 3d gaussian  
- **[Pi-GS: Sparse-View Gaussian Splatting with Dense π^3 Initialization](https://arxiv.org/abs/2602.03327v1)**  
  Authors: Manuel Hofer, Markus Steinberger, Thomas Köhler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03327v1.pdf)  
  Keywords: real-time rendering, sparse-view, ar, nerf, gaussian splatting, motion, 3d gaussian  

### Geometry Reconstruction

*Showing the latest 50 out of 202 papers*

- **[SSR-GS: Separating Specular Reflection in Gaussian Splatting for Glossy Surface Reconstruction](https://arxiv.org/abs/2603.05152v1)**  
  Authors: Ningjing Fan, Yiqun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05152v1.pdf)  
  Keywords: efficient, illumination, geometry, reflection, ar, gaussian splatting, face, 3d gaussian  
- **[GloSplat: Joint Pose-Appearance Optimization for Faster and More Accurate 3D Reconstruction](https://arxiv.org/abs/2603.04847v1)**  
  Authors: Tianyu Xiong, Rui Li, Linjie Li, Jiaqi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04847v1.pdf)  
  Keywords: efficient, ar, nerf, gaussian splatting, motion, fast, 3d gaussian, 3d reconstruction  
- **[LLM-supported 3D Modeling Tool for Radio Radiance Field Reconstruction](https://arxiv.org/abs/2603.04368v1)**  
  Authors: Chengling Xu, Huiwen Zhang, Haijian Sun, Feng Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04368v1.pdf)  
  Keywords: ar, fast, geometry, semantic  
- **[EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2603.04254v1)**  
  Authors: Seungjun Lee, Zihan Wang, Yunsong Wang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04254v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://0nandon.github.io/EmbodiedSplat)  
  Keywords: efficient, ar, semantic, understanding, 3d gaussian, 3d reconstruction  
- **[VIRGi: View-dependent Instant Recoloring of 3D Gaussians Splats](https://arxiv.org/abs/2603.02986v1)**  
  Authors: Alessio Mazzucchelli, Ivan Ojeda-Martin, Fernando Rivas-Manzaneque, Elena Garces, Adrian Penate-Sanchez, Francesc Moreno-Noguer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02986v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, segmentation, 3d gaussian, 3d reconstruction  
- **[Intrinsic Geometry-Appearance Consistency Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2603.02893v1)**  
  Authors: Kaiqiang Xiong, Rui Peng, Jiahao Wu, Zhanke Wang, Jie Liang, Xiaoyun Zheng, Feng Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02893v1.pdf)  
  Keywords: sparse-view, geometry, ar, gaussian splatting, human, high-fidelity, 3d gaussian  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: relightable, illumination, outdoor, relighting, reflection, ar, nerf, gaussian splatting, lighting, fast, 3d gaussian, 3d reconstruction  
- **[OnlineX: Unified Online 3D Reconstruction and Understanding with Active-to-Stable State Evolution](https://arxiv.org/abs/2603.02134v2)**  
  Authors: Chong Xia, Fangfu Liu, Yule Wang, Yize Pang, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02134v2.pdf)  
  Keywords: vr, geometry, ar, semantic, gaussian splatting, robotics, understanding, 3d gaussian, 3d reconstruction  
- **[Sparse View Distractor-Free Gaussian Splatting](https://arxiv.org/abs/2603.01603v1)**  
  Authors: Yi Gu, Zhaorui Wang, Jiahang Cao, Jiaxu Wang, Mingle Zhao, Dongjun Ye, Renjing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01603v1.pdf)  
  Keywords: efficient, sparse-view, geometry, ar, semantic, gaussian splatting, sparse view, fast, 3d gaussian  
- **[HeroGS: Hierarchical Guidance for Robust 3D Gaussian Splatting under Sparse Views](https://arxiv.org/abs/2603.01099v2)**  
  Authors: Jiashu Li, Xumeng Han, Zhaoyang Wei, Zipeng Wang, Kuiran Wang, Guorong Li, Zhenjun Han, Jianbin Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01099v2.pdf)  
  Keywords: sparse-view, geometry, ar, gaussian splatting, high-fidelity, sparse view, 3d gaussian  

### Large Scene

- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: relightable, illumination, outdoor, relighting, reflection, ar, nerf, gaussian splatting, lighting, fast, 3d gaussian, 3d reconstruction  
- **[Interactive Augmented Reality-enabled Outdoor Scene Visualization For Enhanced Real-time Disaster Response](https://arxiv.org/abs/2602.21874v1)**  
  Authors: Dimitrios Apostolakis, Georgios Angelidis, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21874v1.pdf)  
  Keywords: outdoor, lightweight, ar, semantic, gaussian splatting, lighting, fast, face, 3d gaussian  
- **[Large-scale Photorealistic Outdoor 3D Scene Reconstruction from UAV Imagery Using Gaussian Splatting Techniques](https://arxiv.org/abs/2602.20342v1)**  
  Authors: Christos Maikos, Georgios Angelidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20342v1.pdf)  
  Keywords: efficient, neural rendering, vr, outdoor, ar, nerf, gaussian splatting, high-fidelity, 3d gaussian, 3d reconstruction  
- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: localization, outdoor, geometry, ar, semantic, gaussian splatting, lighting, head, mapping, 3d gaussian  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: real-time rendering, global illumination, illumination, outdoor, ar, autonomous driving, nerf, gaussian splatting, lighting, 3d gaussian  
- **[Zero-Shot UAV Navigation in Forests via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2602.07101v2)**  
  Authors: Zinan Lv, Yeqian Qian, Chen Sang, Hao Liu, Danping Zou, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07101v2.pdf)  
  Keywords: relightable, illumination, geometry, dynamic, outdoor, lightweight, ar, gaussian splatting, lighting, high-fidelity, 3d gaussian  
- **[3DGS$^2$-TR: Scalable Second-Order Trust-Region Method for 3D Gaussian Splatting](https://arxiv.org/abs/2602.00395v1)**  
  Authors: Roger Hsiao, Yuchen Fang, Xiangru Huang, Ruilong Li, Hesam Rabeti, Zan Gojcic, Javad Lavaei, James Demmel, Sophia Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00395v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, head, large scene, 3d gaussian  
- **[EVolSplat4D: Efficient Volume-based Gaussian Splatting for 4D Urban Scene Synthesis](https://arxiv.org/abs/2601.15951v1)**  
  Authors: Sheng Miao, Sijin Li, Pan Wang, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15951v1.pdf)  
  Keywords: efficient, urban scene, geometry, dynamic, ar, 4d, gaussian splatting, semantic, autonomous driving, motion, 3d gaussian  
- **[ScenDi: 3D-to-2D Scene Diffusion Cascades for Urban Generation](https://arxiv.org/abs/2601.15221v1)**  
  Authors: Hanlei Guo, Jiahao Shao, Xinya Chen, Xiyang Tan, Sheng Miao, Yujun Shen, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15221v1.pdf)  
  Keywords: urban scene, 3d gaussian, ar  
- **[Clean-GS: Semantic Mask-Guided Pruning for 3D Gaussian Splatting](https://arxiv.org/abs/2601.00913v1)**  
  Authors: Subhankar Mishra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00913v1.pdf) | [![GitHub](https://img.shields.io/github/stars/smlab-niser/clean-gs?style=social)](https://github.com/smlab-niser/clean-gs)  
  Keywords: vr, outdoor, ar, semantic, gaussian splatting, segmentation, compression, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 214 papers*

- **[SSR-GS: Separating Specular Reflection in Gaussian Splatting for Glossy Surface Reconstruction](https://arxiv.org/abs/2603.05152v1)**  
  Authors: Ningjing Fan, Yiqun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05152v1.pdf)  
  Keywords: efficient, illumination, geometry, reflection, ar, gaussian splatting, face, 3d gaussian  
- **[GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins](https://arxiv.org/abs/2603.05108v1)**  
  Authors: Yichen Cai, Paul Jansonnie, Cristiana de Farias, Oleg Arenz, Jan Peters  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05108v1.pdf)  
  Keywords: efficient, dynamic, efficient rendering, tracking, ar, gaussian splatting, segmentation  
- **[GloSplat: Joint Pose-Appearance Optimization for Faster and More Accurate 3D Reconstruction](https://arxiv.org/abs/2603.04847v1)**  
  Authors: Tianyu Xiong, Rui Li, Linjie Li, Jiaqi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04847v1.pdf)  
  Keywords: efficient, ar, nerf, gaussian splatting, motion, fast, 3d gaussian, 3d reconstruction  
- **[EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2603.04254v1)**  
  Authors: Seungjun Lee, Zihan Wang, Yunsong Wang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04254v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://0nandon.github.io/EmbodiedSplat)  
  Keywords: efficient, ar, semantic, understanding, 3d gaussian, 3d reconstruction  
- **[VIRGi: View-dependent Instant Recoloring of 3D Gaussians Splats](https://arxiv.org/abs/2603.02986v1)**  
  Authors: Alessio Mazzucchelli, Ivan Ojeda-Martin, Fernando Rivas-Manzaneque, Elena Garces, Adrian Penate-Sanchez, Francesc Moreno-Noguer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02986v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, segmentation, 3d gaussian, 3d reconstruction  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: efficient, animation, ar, gaussian splatting, head, high-fidelity, avatar, 3d gaussian  
- **[Sparse View Distractor-Free Gaussian Splatting](https://arxiv.org/abs/2603.01603v1)**  
  Authors: Yi Gu, Zhaorui Wang, Jiahang Cao, Jiaxu Wang, Mingle Zhao, Dongjun Ye, Renjing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01603v1.pdf)  
  Keywords: efficient, sparse-view, geometry, ar, semantic, gaussian splatting, sparse view, fast, 3d gaussian  
- **[Radiometrically Consistent Gaussian Surfels for Inverse Rendering](https://arxiv.org/abs/2603.01491v1)**  
  Authors: Kyu Beom Han, Jaeyoon Kim, Woo Jae Kim, Jinhwan Seo, Sung-eui Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01491v1.pdf)  
  Keywords: efficient, global illumination, illumination, relighting, reflection, ar, gaussian splatting, lighting, ray tracing  
- **[ArtiFixer: Enhancing and Extending 3D Reconstruction with Auto-Regressive Diffusion Models](https://arxiv.org/abs/2603.00492v1)**  
  Authors: Riccardo de Lutio, Tobias Fischer, Yen-Yu Chang, Yuxuan Zhang, Jay Zhangjie Wu, Xuanchi Ren, Tianchang Shen, Katarina Tothova, Zan Gojcic, Haithem Turki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00492v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Station2Radar: query conditioned gaussian splatting for precipitation field](https://arxiv.org/abs/2603.00418v1)**  
  Authors: Doyi Kim, Minseok Seo, Changick Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00418v1.pdf)  
  Keywords: gaussian splatting, efficient, ar  

### Quality Enhancement

*Showing the latest 50 out of 129 papers*

- **[Gaussian Wardrobe: Compositional 3D Gaussian Avatars for Free-Form Virtual Try-On](https://arxiv.org/abs/2603.04290v2)**  
  Authors: Zhiyi Chen, Hsuan-I Ho, Tianjian Jiang, Jie Song, Manuel Kaufmann, Chen Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04290v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ait.ethz.ch/gaussianwardrobe)  
  Keywords: body, dynamic, ar, human, high-fidelity, avatar, 3d gaussian  
- **[Intrinsic Geometry-Appearance Consistency Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2603.02893v1)**  
  Authors: Kaiqiang Xiong, Rui Peng, Jiahao Wu, Zhanke Wang, Jie Liang, Xiaoyun Zheng, Feng Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02893v1.pdf)  
  Keywords: sparse-view, geometry, ar, gaussian splatting, human, high-fidelity, 3d gaussian  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: efficient, animation, ar, gaussian splatting, head, high-fidelity, avatar, 3d gaussian  
- **[D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping](https://arxiv.org/abs/2603.01151v1)**  
  Authors: Haozhe Lou, Mingtong Zhang, Haoran Geng, Hanyang Zhou, Sicheng He, Zhiyuan Gao, Siheng Zhao, Jiageng Mao, Pieter Abbeel, Jitendra Malik, Daniel Seita, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01151v1.pdf)  
  Keywords: human, dynamic, high-fidelity, ar  
- **[HeroGS: Hierarchical Guidance for Robust 3D Gaussian Splatting under Sparse Views](https://arxiv.org/abs/2603.01099v2)**  
  Authors: Jiashu Li, Xumeng Han, Zhaoyang Wei, Zipeng Wang, Kuiran Wang, Guorong Li, Zhenjun Han, Jianbin Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01099v2.pdf)  
  Keywords: sparse-view, geometry, ar, gaussian splatting, high-fidelity, sparse view, 3d gaussian  
- **[Decoupling Motion and Geometry in 4D Gaussian Splatting](https://arxiv.org/abs/2603.00952v1)**  
  Authors: Yi Zhang, Yulei Kang, Jian-Fang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00952v1.pdf)  
  Keywords: geometry, dynamic, ar, 4d, gaussian splatting, high-fidelity, motion, deformation  
- **[UFO-4D: Unposed Feedforward 4D Reconstruction from Two Images](https://arxiv.org/abs/2602.24290v2)**  
  Authors: Junhwa Hur, Charles Herrmann, Songyou Peng, Philipp Henzler, Zeyu Ma, Todd Zickler, Deqing Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24290v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ufo-4d.github.io)  
  Keywords: geometry, dynamic, ar, 4d, high-fidelity, motion, 3d gaussian  
- **[GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction](https://arxiv.org/abs/2602.24161v1)**  
  Authors: Chao Xu, Xiaochen Zhao, Xiang Deng, Jingxiang Sun, Zhuo Su, Donglin Di, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24161v1.pdf)  
  Keywords: real-time rendering, geometry, ar, 4d, head, high-fidelity, face, avatar, 3d gaussian  
- **[ArtPro: Self-Supervised Articulated Object Reconstruction with Adaptive Integration of Mobility Proposals](https://arxiv.org/abs/2602.22666v1)**  
  Authors: Xuelu Li, Zhaonan Wang, Xiaogang Wang, Lei Wu, Manyi Li, Changhe Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22666v1.pdf)  
  Keywords: geometry, dynamic, ar, gaussian splatting, high-fidelity, segmentation, motion, 3d gaussian  
- **[SwiftNDC: Fast Neural Depth Correction for High-Fidelity 3D Reconstruction](https://arxiv.org/abs/2602.22565v1)**  
  Authors: Kang Han, Wei Xiang, Lu Yu, Mathew Wyatt, Gaowen Liu, Ramana Rao Kompella  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22565v1.pdf)  
  Keywords: efficient, geometry, ar, gaussian splatting, lighting, high-fidelity, fast, face, 3d gaussian, 3d reconstruction  

### Ray Tracing

- **[Radiometrically Consistent Gaussian Surfels for Inverse Rendering](https://arxiv.org/abs/2603.01491v1)**  
  Authors: Kyu Beom Han, Jaeyoon Kim, Woo Jae Kim, Jinhwan Seo, Sung-eui Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01491v1.pdf)  
  Keywords: efficient, global illumination, illumination, relighting, reflection, ar, gaussian splatting, lighting, ray tracing  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: real-time rendering, global illumination, illumination, outdoor, ar, autonomous driving, nerf, gaussian splatting, lighting, 3d gaussian  
- **[Rotated Lights for Consistent and Efficient 2D Gaussians Inverse Rendering](https://arxiv.org/abs/2602.08724v1)**  
  Authors: Geng Lin, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08724v1.pdf)  
  Keywords: efficient, global illumination, illumination, geometry, relighting, ar, gaussian splatting, lighting, shadow  
- **[Radioactive 3D Gaussian Ray Tracing for Tomographic Reconstruction](https://arxiv.org/abs/2602.01057v1)**  
  Authors: Ling Chen, Bao Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01057v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, ray tracing  
- **[EAG-PT: Emission-Aware Gaussians and Path Tracing for Indoor Scene Reconstruction and Editing](https://arxiv.org/abs/2601.23065v1)**  
  Authors: Xijie Yang, Mulin Yu, Changjian Jiang, Kerui Ren, Tao Lu, Jiangmiao Pang, Dahua Lin, Bo Dai, Linning Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.23065v1.pdf)  
  Keywords: efficient, illumination, geometry, light transport, ar, nerf, path tracing  
- **[Hybrid Foveated Path Tracing with Peripheral Gaussians for Immersive Anatomy](https://arxiv.org/abs/2601.22026v1)**  
  Authors: Constantin Kleinbeck, Luisa Theelke, Hannah Schieber, Ulrich Eck, Rüdiger von Eisenhart-Rothe, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22026v1.pdf)  
  Keywords: vr, medical, lightweight, ar, gaussian splatting, head, understanding, path tracing  
- **[GRTX: Efficient Ray Tracing for 3D Gaussian-Based Rendering](https://arxiv.org/abs/2601.20429v1)**  
  Authors: Junseo Lee, Sangyun Jeon, Jungi Lee, Junyong Park, Jaewoong Sim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20429v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, head, acceleration, 3d gaussian, ray tracing  
- **[ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2601.00939v1)**  
  Authors: Feng Luo, Hongbo Pan, Xiang Yang, Baoyu Jiang, Fengqing Liu, Tao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00939v1.pdf)  
  Keywords: ray marching, efficient, illumination, sparse-view, efficient rendering, ar, gaussian splatting, shadow, 3d gaussian, 3d reconstruction  
- **[Geometric-Photometric Event-based 3D Gaussian Ray Tracing](https://arxiv.org/abs/2512.18640v1)**  
  Authors: Kai Kohyama, Yoshimitsu Aoki, Guillermo Gallego, Shintaro Shiba  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18640v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, 3d reconstruction, motion, fast, understanding, 3d gaussian, ray tracing  
- **[MatSpray: Fusing 2D Material World Knowledge on 3D Geometry](https://arxiv.org/abs/2512.18314v1)**  
  Authors: Philipp Langsteiner, Jan-Niklas Dihlmann, Hendrik P. A. Lensch  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18314v1.pdf)  
  Keywords: relightable, geometry, relighting, ar, gaussian splatting, lighting, 3d reconstruction, ray tracing  

### Relighting

*Showing the latest 50 out of 73 papers*

- **[SSR-GS: Separating Specular Reflection in Gaussian Splatting for Glossy Surface Reconstruction](https://arxiv.org/abs/2603.05152v1)**  
  Authors: Ningjing Fan, Yiqun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05152v1.pdf)  
  Keywords: efficient, illumination, geometry, reflection, ar, gaussian splatting, face, 3d gaussian  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: relightable, illumination, outdoor, relighting, reflection, ar, nerf, gaussian splatting, lighting, fast, 3d gaussian, 3d reconstruction  
- **[Radiometrically Consistent Gaussian Surfels for Inverse Rendering](https://arxiv.org/abs/2603.01491v1)**  
  Authors: Kyu Beom Han, Jaeyoon Kim, Woo Jae Kim, Jinhwan Seo, Sung-eui Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01491v1.pdf)  
  Keywords: efficient, global illumination, illumination, relighting, reflection, ar, gaussian splatting, lighting, ray tracing  
- **[DiffusionHarmonizer: Bridging Neural Reconstruction and Photorealistic Simulation with Online Diffusion Enhancer](https://arxiv.org/abs/2602.24096v2)**  
  Authors: Yuxuan Zhang, Katarína Tóthová, Zian Wang, Kangxue Yin, Haithem Turki, Riccardo de Lutio, Yen-Yu Chang, Or Litany, Sanja Fidler, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24096v2.pdf)  
  Keywords: dynamic, ar, nerf, gaussian splatting, lighting, 3d gaussian  
- **[SwiftNDC: Fast Neural Depth Correction for High-Fidelity 3D Reconstruction](https://arxiv.org/abs/2602.22565v1)**  
  Authors: Kang Han, Wei Xiang, Lu Yu, Mathew Wyatt, Gaowen Liu, Ramana Rao Kompella  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22565v1.pdf)  
  Keywords: efficient, geometry, ar, gaussian splatting, lighting, high-fidelity, fast, face, 3d gaussian, 3d reconstruction  
- **[Interactive Augmented Reality-enabled Outdoor Scene Visualization For Enhanced Real-time Disaster Response](https://arxiv.org/abs/2602.21874v1)**  
  Authors: Dimitrios Apostolakis, Georgios Angelidis, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21874v1.pdf)  
  Keywords: outdoor, lightweight, ar, semantic, gaussian splatting, lighting, fast, face, 3d gaussian  
- **[DAGS-SLAM: Dynamic-Aware 3DGS SLAM via Spatiotemporal Motion Probability and Uncertainty-Aware Scheduling](https://arxiv.org/abs/2602.21644v2)**  
  Authors: Li Zhang, Yu-An Liu, Xijia Jiang, Conghao Huang, Danyang Li, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21644v2.pdf)  
  Keywords: efficient, localization, illumination, dynamic, mapping, lightweight, slam, tracking, ar, semantic, gaussian splatting, segmentation, motion, 3d gaussian  
- **[WildGHand: Learning Anti-Perturbation Gaussian Hand Avatars from Monocular In-the-Wild Videos](https://arxiv.org/abs/2602.20556v1)**  
  Authors: Hanhui Li, Xuan Huang, Wanquan Liu, Yuhao Cheng, Long Chen, Yiqiang Yan, Xiaodan Liang, Chenqiang Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20556v1.pdf) | [![GitHub](https://img.shields.io/github/stars/XuanHuang0/WildGHand?style=social)](https://github.com/XuanHuang0/WildGHand)  
  Keywords: illumination, dynamic, ar, gaussian splatting, high-fidelity, motion, avatar, 3d gaussian  
- **[Augmented Radiance Field: A General Framework for Enhanced Gaussian Splatting](https://arxiv.org/abs/2602.19916v1)**  
  Authors: Yixin Yang, Bojian Wu, Yang Zhou, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19916v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiaoxinyyx.github.io/augs)  
  Keywords: real-time rendering, reflection, ar, nerf, gaussian splatting, 3d gaussian  
- **[DefenseSplat: Enhancing the Robustness of 3D Gaussian Splatting via Frequency-Aware Filtering](https://arxiv.org/abs/2602.19323v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19323v1.pdf)  
  Keywords: ar, gaussian splatting, lighting, high-fidelity, 3d gaussian, 3d reconstruction  

### SLAM

*Showing the latest 50 out of 76 papers*

- **[GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins](https://arxiv.org/abs/2603.05108v1)**  
  Authors: Yichen Cai, Paul Jansonnie, Cristiana de Farias, Oleg Arenz, Jan Peters  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05108v1.pdf)  
  Keywords: efficient, dynamic, efficient rendering, tracking, ar, gaussian splatting, segmentation  
- **[SR3R: Rethinking Super-Resolution 3D Reconstruction With Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2602.24020v1)**  
  Authors: Xiang Feng, Xiangbo Wang, Tieshi Zhong, Chengkai Wang, Yiting Zhao, Tianxiang Xu, Zhenzhong Kuang, Feiwei Qin, Xuefei Yin, Yanming Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24020v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, mapping, 3d gaussian, 3d reconstruction  
- **[Latent Gaussian Splatting for 4D Panoptic Occupancy Tracking](https://arxiv.org/abs/2602.23172v1)**  
  Authors: Maximilian Luz, Rohit Mohan, Thomas Nürnberg, Yakov Miron, Daniele Cattaneo, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23172v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lags.cs.uni-freiburg.de)  
  Keywords: efficient, dynamic, tracking, ar, 4d, gaussian splatting, head, segmentation, understanding, 3d gaussian  
- **[Sapling-NeRF: Geo-Localised Sapling Reconstruction in Forests for Ecological Monitoring](https://arxiv.org/abs/2602.22731v1)**  
  Authors: Miguel Ángel Muñoz-Bañón, Nived Chebrolu, Sruthi M. Krishna Moorthy, Yifu Tao, Fernando Torres, Roberto Salguero-Gómez, Maurice Fallon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22731v1.pdf)  
  Keywords: dynamic, slam, ar, nerf, gaussian splatting, 3d gaussian, 3d reconstruction  
- **[DAGS-SLAM: Dynamic-Aware 3DGS SLAM via Spatiotemporal Motion Probability and Uncertainty-Aware Scheduling](https://arxiv.org/abs/2602.21644v2)**  
  Authors: Li Zhang, Yu-An Liu, Xijia Jiang, Conghao Huang, Danyang Li, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21644v2.pdf)  
  Keywords: efficient, localization, illumination, dynamic, mapping, lightweight, slam, tracking, ar, semantic, gaussian splatting, segmentation, motion, 3d gaussian  
- **[RU4D-SLAM: Reweighting Uncertainty in Gaussian Splatting SLAM for 4D Scene Reconstruction](https://arxiv.org/abs/2602.20807v1)**  
  Authors: Yangfan Zhao, Hanwei Zhang, Ke Huang, Qiufeng Wang, Zhenzhou Shao, Dengyu Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20807v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ru4d-slam.github.io)  
  Keywords: efficient, localization, dynamic, mapping, slam, tracking, ar, 4d, gaussian splatting, semantic, motion, 3d gaussian, 3d reconstruction  
- **[NRGS-SLAM: Monocular Non-Rigid SLAM for Endoscopy via Deformation-Aware 3D Gaussian Splatting](https://arxiv.org/abs/2602.17182v1)**  
  Authors: Jiwei Shan, Zeyu Cai, Yirui Li, Yongbo Chen, Lijun Han, Yun-hui Liu, Hesheng Wang, Shing Shin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17182v1.pdf)  
  Keywords: efficient, localization, mapping, slam, tracking, ar, gaussian splatting, motion, deformation, 3d gaussian  
- **[Time-Archival Camera Virtualization for Sports and Visual Performances](https://arxiv.org/abs/2602.15181v1)**  
  Authors: Yunxiao Zhang, William Stone, Suryansh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15181v1.pdf)  
  Keywords: efficient, neural rendering, dynamic, tracking, ar, 4d, gaussian splatting, motion, fast, 3d gaussian  
- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: localization, outdoor, geometry, ar, semantic, gaussian splatting, lighting, head, mapping, 3d gaussian  
- **[High-fidelity 3D reconstruction for planetary exploration](https://arxiv.org/abs/2602.13909v1)**  
  Authors: Alfonso Martínez-Petersen, Levin Gerdes, David Rodríguez-Martínez, C. J. Pérez-del-Pulgar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13909v1.pdf)  
  Keywords: efficient, localization, mapping, slam, ar, nerf, gaussian splatting, high-fidelity, robotics, motion, face, 3d reconstruction  

### Scene Understanding

*Showing the latest 50 out of 127 papers*

- **[GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins](https://arxiv.org/abs/2603.05108v1)**  
  Authors: Yichen Cai, Paul Jansonnie, Cristiana de Farias, Oleg Arenz, Jan Peters  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05108v1.pdf)  
  Keywords: efficient, dynamic, efficient rendering, tracking, ar, gaussian splatting, segmentation  
- **[LLM-supported 3D Modeling Tool for Radio Radiance Field Reconstruction](https://arxiv.org/abs/2603.04368v1)**  
  Authors: Chengling Xu, Huiwen Zhang, Haijian Sun, Feng Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04368v1.pdf)  
  Keywords: ar, fast, geometry, semantic  
- **[EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2603.04254v1)**  
  Authors: Seungjun Lee, Zihan Wang, Yunsong Wang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04254v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://0nandon.github.io/EmbodiedSplat)  
  Keywords: efficient, ar, semantic, understanding, 3d gaussian, 3d reconstruction  
- **[VIRGi: View-dependent Instant Recoloring of 3D Gaussians Splats](https://arxiv.org/abs/2603.02986v1)**  
  Authors: Alessio Mazzucchelli, Ivan Ojeda-Martin, Fernando Rivas-Manzaneque, Elena Garces, Adrian Penate-Sanchez, Francesc Moreno-Noguer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02986v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, segmentation, 3d gaussian, 3d reconstruction  
- **[Articulation in Motion: Prior-free Part Mobility Analysis for Articulated Objects By Dynamic-Static Disentanglement](https://arxiv.org/abs/2603.02910v1)**  
  Authors: Hao Ai, Wenjie Chang, Jianbo Jiao, Ales Leonardis, Ofek Eyal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02910v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haoai-1997.github.io/AiM)  
  Keywords: dynamic, ar, segmentation, motion, 3d gaussian  
- **[Multimodal-Prior-Guided Importance Sampling for Hierarchical Gaussian Splatting in Sparse-View Novel View Synthesis](https://arxiv.org/abs/2603.02866v1)**  
  Authors: Kaiqiang Xiong, Zhanke Wang, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02866v1.pdf)  
  Keywords: sparse-view, ar, semantic, gaussian splatting, 3d gaussian  
- **[SemGS: Feed-Forward Semantic 3D Gaussian Splatting from Sparse Views for Generalizable Scene Understanding](https://arxiv.org/abs/2603.02548v1)**  
  Authors: Sheng Ye, Zhen-Hui Dong, Ruoyu Fan, Tian Lv, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02548v1.pdf)  
  Keywords: ar, semantic, gaussian splatting, sparse view, understanding, 3d gaussian  
- **[OnlineX: Unified Online 3D Reconstruction and Understanding with Active-to-Stable State Evolution](https://arxiv.org/abs/2603.02134v2)**  
  Authors: Chong Xia, Fangfu Liu, Yule Wang, Yize Pang, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02134v2.pdf)  
  Keywords: vr, geometry, ar, semantic, gaussian splatting, robotics, understanding, 3d gaussian, 3d reconstruction  
- **[Sparse View Distractor-Free Gaussian Splatting](https://arxiv.org/abs/2603.01603v1)**  
  Authors: Yi Gu, Zhaorui Wang, Jiahang Cao, Jiaxu Wang, Mingle Zhao, Dongjun Ye, Renjing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01603v1.pdf)  
  Keywords: efficient, sparse-view, geometry, ar, semantic, gaussian splatting, sparse view, fast, 3d gaussian  
- **[TokenSplat: Token-aligned 3D Gaussian Splatting for Feed-forward Pose-free Reconstruction](https://arxiv.org/abs/2603.00697v1)**  
  Authors: Yihui Li, Chengxin Lv, Zichen Tang, Hongyu Yang, Di Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00697v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kidleyh.github.io/tokensplat)  
  Keywords: semantic, gaussian splatting, 3d gaussian, ar  



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