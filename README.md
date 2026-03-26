# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-03-26 01:19:54

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
- [Acceleration](#acceleration) (116 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (500 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (161 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (201 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (31 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (207 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (16 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (217 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (131 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (22 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (71 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (74 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (134 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: ar, vr, 3d gaussian, survey, gaussian splatting  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v2)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v2.pdf)  
  Keywords: ar, ray tracing, mapping, 3d gaussian, survey, gaussian splatting  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: ar, efficient, face, motion, tracking, slam, mapping, 3d gaussian, survey, gaussian splatting, dynamic, localization  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: ar, 3d gaussian, robotics, survey, gaussian splatting  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v3)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v3.pdf)  
  Keywords: ar, efficient, 3d gaussian, nerf, geometry, survey, gaussian splatting  
- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197v1)**  
  Authors: Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07197v1.pdf)  
  Keywords: ar, high-fidelity, efficient, compression, 3d gaussian, 3d reconstruction, survey, gaussian splatting, dynamic, compact, 4d  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v2)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v2.pdf)  
  Keywords: ar, understanding, slam, mapping, 3d gaussian, nerf, robotics, survey, gaussian splatting, semantic, localization  

### Acceleration

*Showing the latest 50 out of 116 papers*

- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: ar, high-fidelity, fast, efficient, face, 3d gaussian, 3d reconstruction, gaussian splatting  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: ar, high-fidelity, fast, efficient, face, animation, 3d gaussian, avatar, geometry, head  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: ar, face, path tracing, 3d gaussian, real-time rendering, geometry  
- **[Fast undersampled dynamic MRI reconstruction using explicit representation learning with Gaussian splatting](https://arxiv.org/abs/2603.21980v1)**  
  Authors: M. L. Terpstra, C. A. T. van den Berg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21980v1.pdf)  
  Keywords: ar, fast, efficient, motion, gaussian splatting, dynamic  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: ar, high-fidelity, fast, efficient, face, ray tracing, 3d gaussian, nerf, geometry, real-time rendering, gaussian splatting  
- **[F4Splat: Feed-Forward Predictive Densification for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.21304v2)**  
  Authors: Injae Kim, Chaehyeon Kim, Minseong Bae, Minseok Joo, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21304v2.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, gaussian splatting, compact  
- **[Fast and Robust Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2603.20857v1)**  
  Authors: Han Jiao, Jiakai Sun, Lei Zhao, Zhanjie Zhang, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20857v1.pdf)  
  Keywords: deformation, ar, fast, efficient, 3d gaussian, real-time rendering, gaussian splatting, dynamic  
- **[GaussianPile: A Unified Sparse Gaussian Splatting Framework for Slice-based Volumetric Reconstruction](https://arxiv.org/abs/2603.20611v1)**  
  Authors: Di Kong, Yikai Wang, Wenjie Guo, Yifan Bu, Boya Zhang, Yuexin Duan, Xiawei Yue, Wenbiao Du, Yiman Zhong, Yuwen Chen, Cheng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20611v1.pdf)  
  Keywords: ar, fast, 3d gaussian, nerf, real-time rendering, gaussian splatting, compression, compact  
- **[TRGS-SLAM: IMU-Aided Gaussian Splatting SLAM for Blurry, Rolling Shutter, and Noisy Thermal Images](https://arxiv.org/abs/2603.20443v1)**  
  Authors: Spencer Carmichael, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20443v1.pdf)  
  Keywords: ar, fast, motion, tracking, slam, mapping, 3d gaussian, robotics, gaussian splatting, dynamic, illumination, localization  
- **[Fourier Splatting: Generalized Fourier encoded primitives for scalable radiance fields](https://arxiv.org/abs/2603.19834v1)**  
  Authors: Mihnea-Bogdan Jurca, Bert Van hauwermeiren, Adrian Munteanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19834v1.pdf)  
  Keywords: ar, high-fidelity, efficient, 3d gaussian, real-time rendering, gaussian splatting  

### Applications

*Showing the latest 50 out of 500 papers*

- **[SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision](https://arxiv.org/abs/2603.24036v1)**  
  Authors: Avigail Cohen Rimon, Amir Mann, Mirela Ben Chen, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24036v1.pdf)  
  Keywords: deformation, ar, tracking, 3d gaussian, gaussian splatting, compact  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: ar, efficient, face, large scene, neural rendering, 3d gaussian, gaussian splatting, head  
- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: ar, high-fidelity, fast, efficient, face, 3d gaussian, 3d reconstruction, gaussian splatting  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v1)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v1.pdf)  
  Keywords: ar, ray tracing, reflection, mapping, 3d gaussian, relightable, gaussian splatting, shadow  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: ar, high-fidelity, fast, efficient, face, animation, 3d gaussian, avatar, geometry, head  
- **[Pose-Free Omnidirectional Gaussian Splatting for 360-Degree Videos with Consistent Depth Priors](https://arxiv.org/abs/2603.23324v1)**  
  Authors: Chuanqing Zhuang, Xin Lu, Zehui Deng, Zhengda Lu, Yiqun Wang, Junqi Diao, Jun Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23324v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zcq15/PFGS360?style=social)](https://github.com/zcq15/PFGS360)  
  Keywords: gaussian splatting, ar, 3d gaussian, efficient  
- **[GTLR-GS: Geometry-Texture Aware LiDAR-Regularized 3D Gaussian Splatting for Realistic Scene Reconstruction](https://arxiv.org/abs/2603.23192v1)**  
  Authors: Yan Fang, Jianfei Ge, Jiangjian Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23192v1.pdf)  
  Keywords: ar, motion, 3d gaussian, geometry, gaussian splatting, dynamic  
- **[GSwap: Realistic Head Swapping with Dynamic Neural Gaussian Field](https://arxiv.org/abs/2603.23168v1)**  
  Authors: Jingtao Zhou, Xuan Gao, Dongyu Liu, Junhui Hou, Yudong Guo, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23168v1.pdf)  
  Keywords: ar, high-fidelity, efficient, face, motion, 3d gaussian, body, dynamic, head  
- **[Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction](https://arxiv.org/abs/2603.22852v1)**  
  Authors: Chengxin Lv, Yihui Li, Hongyu Yang, YunHong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22852v1.pdf)  
  Keywords: ar, autonomous driving, efficient, 3d gaussian, geometry, semantic, compact  
- **[UniQueR: Unified Query-based Feedforward 3D Reconstruction](https://arxiv.org/abs/2603.22851v1)**  
  Authors: Chensheng Peng, Quentin Herau, Jiezhi Yang, Yichen Xie, Yihan Hu, Wenzhao Zheng, Matthew Strong, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22851v1.pdf)  
  Keywords: ar, efficient, face, vr, 3d gaussian, nerf, 3d reconstruction, geometry, compact  

### Avatar Generation

*Showing the latest 50 out of 161 papers*

- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: ar, efficient, face, large scene, neural rendering, 3d gaussian, gaussian splatting, head  
- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: ar, high-fidelity, fast, efficient, face, 3d gaussian, 3d reconstruction, gaussian splatting  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: ar, high-fidelity, fast, efficient, face, animation, 3d gaussian, avatar, geometry, head  
- **[GSwap: Realistic Head Swapping with Dynamic Neural Gaussian Field](https://arxiv.org/abs/2603.23168v1)**  
  Authors: Jingtao Zhou, Xuan Gao, Dongyu Liu, Junhui Hou, Yudong Guo, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23168v1.pdf)  
  Keywords: ar, high-fidelity, efficient, face, motion, 3d gaussian, body, dynamic, head  
- **[UniQueR: Unified Query-based Feedforward 3D Reconstruction](https://arxiv.org/abs/2603.22851v1)**  
  Authors: Chensheng Peng, Quentin Herau, Jiezhi Yang, Yichen Xie, Yihan Hu, Wenzhao Zheng, Matthew Strong, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22851v1.pdf)  
  Keywords: ar, efficient, face, vr, 3d gaussian, nerf, 3d reconstruction, geometry, compact  
- **[FullCircle: Effortless 3D Reconstruction from Casual 360$^\circ$ Captures](https://arxiv.org/abs/2603.22572v1)**  
  Authors: Yalda Foroutan, Ipek Oztas, Daniel Rebain, Aysegul Dundar, Kwang Moo Yi, Lily Goli, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22572v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://theialab.github.io/fullcircle)  
  Keywords: human, ar, 3d reconstruction  
- **[Drop-In Perceptual Optimization for 3D Gaussian Splatting](https://arxiv.org/abs/2603.23297v1)**  
  Authors: Ezgi Ozyilkan, Zhiqi Chen, Oren Rippel, Jona Ballé, Kedar Tatwawadi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23297v1.pdf)  
  Keywords: ar, human, 3d gaussian, gaussian splatting, compression  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: ar, face, path tracing, 3d gaussian, real-time rendering, geometry  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: ar, high-fidelity, fast, efficient, face, ray tracing, 3d gaussian, nerf, geometry, real-time rendering, gaussian splatting  
- **[EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](https://arxiv.org/abs/2603.21332v1)**  
  Authors: Haolan Xu, Keli Cheng, Lei Wang, Ning Bi, Xiaoming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21332v1.pdf)  
  Keywords: ar, face, few-shot, motion, lighting, 3d gaussian, nerf, gaussian splatting, head  

### Dynamic Scene

*Showing the latest 50 out of 201 papers*

- **[SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision](https://arxiv.org/abs/2603.24036v1)**  
  Authors: Avigail Cohen Rimon, Amir Mann, Mirela Ben Chen, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24036v1.pdf)  
  Keywords: deformation, ar, tracking, 3d gaussian, gaussian splatting, compact  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: ar, high-fidelity, fast, efficient, face, animation, 3d gaussian, avatar, geometry, head  
- **[GTLR-GS: Geometry-Texture Aware LiDAR-Regularized 3D Gaussian Splatting for Realistic Scene Reconstruction](https://arxiv.org/abs/2603.23192v1)**  
  Authors: Yan Fang, Jianfei Ge, Jiangjian Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23192v1.pdf)  
  Keywords: ar, motion, 3d gaussian, geometry, gaussian splatting, dynamic  
- **[GSwap: Realistic Head Swapping with Dynamic Neural Gaussian Field](https://arxiv.org/abs/2603.23168v1)**  
  Authors: Jingtao Zhou, Xuan Gao, Dongyu Liu, Junhui Hou, Yudong Guo, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23168v1.pdf)  
  Keywords: ar, high-fidelity, efficient, face, motion, 3d gaussian, body, dynamic, head  
- **[FreeArtGS: Articulated Gaussian Splatting Under Free-moving Scenario](https://arxiv.org/abs/2603.22102v1)**  
  Authors: Hang Dai, Hongwei Fan, Han Zhang, Duojin Wu, Jiyao Zhang, Hao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22102v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://freeartgs.github.io)  
  Keywords: ar, motion, tracking, segmentation, geometry, robotics, gaussian splatting  
- **[Fast undersampled dynamic MRI reconstruction using explicit representation learning with Gaussian splatting](https://arxiv.org/abs/2603.21980v1)**  
  Authors: M. L. Terpstra, C. A. T. van den Berg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21980v1.pdf)  
  Keywords: ar, fast, efficient, motion, gaussian splatting, dynamic  
- **[EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](https://arxiv.org/abs/2603.21332v1)**  
  Authors: Haolan Xu, Keli Cheng, Lei Wang, Ning Bi, Xiaoming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21332v1.pdf)  
  Keywords: ar, face, few-shot, motion, lighting, 3d gaussian, nerf, gaussian splatting, head  
- **[Fast and Robust Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2603.20857v1)**  
  Authors: Han Jiao, Jiakai Sun, Lei Zhao, Zhanjie Zhang, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20857v1.pdf)  
  Keywords: deformation, ar, fast, efficient, 3d gaussian, real-time rendering, gaussian splatting, dynamic  
- **[Glove2Hand: Synthesizing Natural Hand-Object Interaction from Multi-Modal Sensing Gloves](https://arxiv.org/abs/2603.20850v1)**  
  Authors: Xinyu Zhang, Ziyi Kou, Chuan Qin, Mia Huang, Ergys Ristani, Ankit Kumar, Lele Chen, Kun He, Abdeslam Boularias, Li Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20850v1.pdf)  
  Keywords: deformation, ar, understanding, motion, tracking, vr, 3d gaussian, robotics, dynamic  
- **[The Role and Relationship of Initialization and Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.20714v1)**  
  Authors: Ivan Desiatov, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20714v1.pdf)  
  Keywords: ar, efficient, motion, 3d gaussian, geometry, 3d reconstruction, gaussian splatting  

### Few-shot

- **[EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](https://arxiv.org/abs/2603.21332v1)**  
  Authors: Haolan Xu, Keli Cheng, Lei Wang, Ning Bi, Xiaoming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21332v1.pdf)  
  Keywords: ar, face, few-shot, motion, lighting, 3d gaussian, nerf, gaussian splatting, head  
- **[UniSem: Generalizable Semantic 3D Reconstruction from Sparse Unposed Images](https://arxiv.org/abs/2603.17519v1)**  
  Authors: Guibiao Liao, Qian Ren, Kaimin Liao, Hua Wang, Zhi Chen, Luchao Wang, Yaohua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17519v1.pdf)  
  Keywords: ar, 3d reconstruction, segmentation, 3d gaussian, sparse-view, geometry, gaussian splatting, semantic  
- **[S2D: Sparse to Dense Lifting for 3D Reconstruction with Minimal Inputs](https://arxiv.org/abs/2603.10893v1)**  
  Authors: Yuzhou Ji, Qijian Tian, He Zhu, Xiaoqi Jiang, Guangzhi Cao, Lizhuang Ma, Yuan Xie, Xin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10893v1.pdf)  
  Keywords: ar, high-fidelity, sparse view, efficient, understanding, 3d gaussian, 3d reconstruction, gaussian splatting  
- **[Active View Selection with Perturbed Gaussian Ensemble for Tomographic Reconstruction](https://arxiv.org/abs/2603.06852v1)**  
  Authors: Yulun Wu, Ruyi Zha, Wei Cao, Yingying Li, Yuanhao Cai, Yaoyao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06852v1.pdf)  
  Keywords: ar, fast, 3d gaussian, sparse-view, gaussian splatting  
- **[CylinderSplat: 3D Gaussian Splatting with Cylindrical Triplanes for Panoramic Novel View Synthesis](https://arxiv.org/abs/2603.05882v1)**  
  Authors: Qiwei Wang, Xianghui Ze, Jingyi Yu, Yujiao Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05882v1.pdf)  
  Keywords: ar, 3d gaussian, sparse-view, geometry, gaussian splatting  
- **[DSA-SRGS: Super-Resolution Gaussian Splatting for Dynamic Sparse-View DSA Reconstruction](https://arxiv.org/abs/2603.04770v1)**  
  Authors: Shiyu Zhang, Zhicong Wu, Huangxuan Zhao, Zhentao Liu, Lei Chen, Yong Luo, Lefei Zhang, Zhiming Cui, Ziwen Ke, Bo Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04770v1.pdf)  
  Keywords: ar, sparse-view, gaussian splatting, dynamic, 4d  
- **[Intrinsic Geometry-Appearance Consistency Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2603.02893v1)**  
  Authors: Kaiqiang Xiong, Rui Peng, Jiahao Wu, Zhanke Wang, Jie Liang, Xiaoyun Zheng, Feng Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02893v1.pdf)  
  Keywords: ar, high-fidelity, human, 3d gaussian, sparse-view, geometry, gaussian splatting  
- **[Multimodal-Prior-Guided Importance Sampling for Hierarchical Gaussian Splatting in Sparse-View Novel View Synthesis](https://arxiv.org/abs/2603.02866v1)**  
  Authors: Kaiqiang Xiong, Zhanke Wang, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02866v1.pdf)  
  Keywords: ar, 3d gaussian, sparse-view, gaussian splatting, semantic  
- **[SemGS: Feed-Forward Semantic 3D Gaussian Splatting from Sparse Views for Generalizable Scene Understanding](https://arxiv.org/abs/2603.02548v1)**  
  Authors: Sheng Ye, Zhen-Hui Dong, Ruoyu Fan, Tian Lv, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02548v1.pdf)  
  Keywords: ar, sparse view, understanding, 3d gaussian, gaussian splatting, semantic  
- **[Sparse View Distractor-Free Gaussian Splatting](https://arxiv.org/abs/2603.01603v1)**  
  Authors: Yi Gu, Zhaorui Wang, Jiahang Cao, Jiaxu Wang, Mingle Zhao, Dongjun Ye, Renjing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01603v1.pdf)  
  Keywords: ar, sparse view, fast, efficient, 3d gaussian, geometry, sparse-view, gaussian splatting, semantic  

### Geometry Reconstruction

*Showing the latest 50 out of 207 papers*

- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: ar, high-fidelity, fast, efficient, face, 3d gaussian, 3d reconstruction, gaussian splatting  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: ar, high-fidelity, fast, efficient, face, animation, 3d gaussian, avatar, geometry, head  
- **[GTLR-GS: Geometry-Texture Aware LiDAR-Regularized 3D Gaussian Splatting for Realistic Scene Reconstruction](https://arxiv.org/abs/2603.23192v1)**  
  Authors: Yan Fang, Jianfei Ge, Jiangjian Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23192v1.pdf)  
  Keywords: ar, motion, 3d gaussian, geometry, gaussian splatting, dynamic  
- **[Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction](https://arxiv.org/abs/2603.22852v1)**  
  Authors: Chengxin Lv, Yihui Li, Hongyu Yang, YunHong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22852v1.pdf)  
  Keywords: ar, autonomous driving, efficient, 3d gaussian, geometry, semantic, compact  
- **[UniQueR: Unified Query-based Feedforward 3D Reconstruction](https://arxiv.org/abs/2603.22851v1)**  
  Authors: Chensheng Peng, Quentin Herau, Jiezhi Yang, Yichen Xie, Yihan Hu, Wenzhao Zheng, Matthew Strong, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22851v1.pdf)  
  Keywords: ar, efficient, face, vr, 3d gaussian, nerf, 3d reconstruction, geometry, compact  
- **[Instrument-Splatting++: Towards Controllable Surgical Instrument Digital Twin Using Gaussian Splatting](https://arxiv.org/abs/2603.22792v2)**  
  Authors: Shuojue Yang, Zijian Wu, Chengjiaao Liao, Qian Li, Daiyun Shen, Chang Han Low, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22792v2.pdf)  
  Keywords: ar, tracking, 3d gaussian, geometry, gaussian splatting, semantic  
- **[FullCircle: Effortless 3D Reconstruction from Casual 360$^\circ$ Captures](https://arxiv.org/abs/2603.22572v1)**  
  Authors: Yalda Foroutan, Ipek Oztas, Daniel Rebain, Aysegul Dundar, Kwang Moo Yi, Lily Goli, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22572v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://theialab.github.io/fullcircle)  
  Keywords: human, ar, 3d reconstruction  
- **[FreeArtGS: Articulated Gaussian Splatting Under Free-moving Scenario](https://arxiv.org/abs/2603.22102v1)**  
  Authors: Hang Dai, Hongwei Fan, Han Zhang, Duojin Wu, Jiyao Zhang, Hao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22102v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://freeartgs.github.io)  
  Keywords: ar, motion, tracking, segmentation, geometry, robotics, gaussian splatting  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: ar, face, path tracing, 3d gaussian, real-time rendering, geometry  
- **[Cross-Instance Gaussian Splatting Registration via Geometry-Aware Feature-Guided Alignment](https://arxiv.org/abs/2603.21936v1)**  
  Authors: Roy Amoyal, Oren Freifeld, Chaim Baskin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21936v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bgu-cs-vil.github.io/GSA-project)  
  Keywords: gaussian splatting, ar, 3d gaussian, geometry  

### Large Scene

- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: ar, efficient, face, large scene, neural rendering, 3d gaussian, gaussian splatting, head  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: outdoor, ar, efficient, tracking, slam, gaussian splatting, dynamic, head  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: outdoor, ar, 3d gaussian, geometry, gaussian splatting, localization  
- **[EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.06216v1)**  
  Authors: Miriam Jäger, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06216v1.pdf)  
  Keywords: ar, face, 3d gaussian, geometry, 3d reconstruction, gaussian splatting, urban scene  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: relighting, outdoor, ar, fast, reflection, lighting, 3d gaussian, nerf, 3d reconstruction, relightable, gaussian splatting, illumination  
- **[Interactive Augmented Reality-enabled Outdoor Scene Visualization For Enhanced Real-time Disaster Response](https://arxiv.org/abs/2602.21874v1)**  
  Authors: Dimitrios Apostolakis, Georgios Angelidis, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21874v1.pdf)  
  Keywords: lightweight, outdoor, ar, fast, face, lighting, 3d gaussian, gaussian splatting, semantic  
- **[Large-scale Photorealistic Outdoor 3D Scene Reconstruction from UAV Imagery Using Gaussian Splatting Techniques](https://arxiv.org/abs/2602.20342v1)**  
  Authors: Christos Maikos, Georgios Angelidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20342v1.pdf)  
  Keywords: outdoor, high-fidelity, ar, efficient, neural rendering, vr, 3d gaussian, nerf, 3d reconstruction, gaussian splatting  
- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: outdoor, ar, lighting, mapping, 3d gaussian, geometry, gaussian splatting, semantic, head, localization  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: outdoor, ar, autonomous driving, lighting, global illumination, 3d gaussian, nerf, real-time rendering, gaussian splatting, illumination  
- **[Zero-Shot UAV Navigation in Forests via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2602.07101v2)**  
  Authors: Zinan Lv, Yeqian Qian, Chen Sang, Hao Liu, Danping Zou, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07101v2.pdf)  
  Keywords: lightweight, outdoor, high-fidelity, ar, lighting, 3d gaussian, geometry, relightable, gaussian splatting, dynamic, illumination  

### Model Compression

*Showing the latest 50 out of 217 papers*

- **[SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision](https://arxiv.org/abs/2603.24036v1)**  
  Authors: Avigail Cohen Rimon, Amir Mann, Mirela Ben Chen, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24036v1.pdf)  
  Keywords: deformation, ar, tracking, 3d gaussian, gaussian splatting, compact  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: ar, efficient, face, large scene, neural rendering, 3d gaussian, gaussian splatting, head  
- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: ar, high-fidelity, fast, efficient, face, 3d gaussian, 3d reconstruction, gaussian splatting  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: ar, high-fidelity, fast, efficient, face, animation, 3d gaussian, avatar, geometry, head  
- **[Pose-Free Omnidirectional Gaussian Splatting for 360-Degree Videos with Consistent Depth Priors](https://arxiv.org/abs/2603.23324v1)**  
  Authors: Chuanqing Zhuang, Xin Lu, Zehui Deng, Zhengda Lu, Yiqun Wang, Junqi Diao, Jun Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23324v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zcq15/PFGS360?style=social)](https://github.com/zcq15/PFGS360)  
  Keywords: gaussian splatting, ar, 3d gaussian, efficient  
- **[GSwap: Realistic Head Swapping with Dynamic Neural Gaussian Field](https://arxiv.org/abs/2603.23168v1)**  
  Authors: Jingtao Zhou, Xuan Gao, Dongyu Liu, Junhui Hou, Yudong Guo, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23168v1.pdf)  
  Keywords: ar, high-fidelity, efficient, face, motion, 3d gaussian, body, dynamic, head  
- **[Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction](https://arxiv.org/abs/2603.22852v1)**  
  Authors: Chengxin Lv, Yihui Li, Hongyu Yang, YunHong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22852v1.pdf)  
  Keywords: ar, autonomous driving, efficient, 3d gaussian, geometry, semantic, compact  
- **[UniQueR: Unified Query-based Feedforward 3D Reconstruction](https://arxiv.org/abs/2603.22851v1)**  
  Authors: Chensheng Peng, Quentin Herau, Jiezhi Yang, Yichen Xie, Yihan Hu, Wenzhao Zheng, Matthew Strong, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22851v1.pdf)  
  Keywords: ar, efficient, face, vr, 3d gaussian, nerf, 3d reconstruction, geometry, compact  
- **[Predictive Photometric Uncertainty in Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2603.22786v1)**  
  Authors: Chamuditha Jayanga Galappaththige, Thomas Gottwald, Peter Stehr, Edgar Heinert, Niko Suenderhauf, Dimity Miller, Matthias Rottmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22786v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, 3d gaussian  
- **[Drop-In Perceptual Optimization for 3D Gaussian Splatting](https://arxiv.org/abs/2603.23297v1)**  
  Authors: Ezgi Ozyilkan, Zhiqi Chen, Oren Rippel, Jona Ballé, Kedar Tatwawadi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23297v1.pdf)  
  Keywords: ar, human, 3d gaussian, gaussian splatting, compression  

### Quality Enhancement

*Showing the latest 50 out of 131 papers*

- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: ar, high-fidelity, fast, efficient, face, 3d gaussian, 3d reconstruction, gaussian splatting  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: ar, high-fidelity, fast, efficient, face, animation, 3d gaussian, avatar, geometry, head  
- **[GSwap: Realistic Head Swapping with Dynamic Neural Gaussian Field](https://arxiv.org/abs/2603.23168v1)**  
  Authors: Jingtao Zhou, Xuan Gao, Dongyu Liu, Junhui Hou, Yudong Guo, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23168v1.pdf)  
  Keywords: ar, high-fidelity, efficient, face, motion, 3d gaussian, body, dynamic, head  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: ar, high-fidelity, fast, efficient, face, ray tracing, 3d gaussian, nerf, geometry, real-time rendering, gaussian splatting  
- **[Training-Free Instance-Aware 3D Scene Reconstruction and Diffusion-Based View Synthesis from Sparse Images](https://arxiv.org/abs/2603.21166v1)**  
  Authors: Jiatong Xia, Lingqiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21166v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiatongxia.github.io/TID3R)  
  Keywords: ar, high-fidelity, efficient, understanding, segmentation, geometry  
- **[2Xplat: Two Experts Are Better Than One Generalist](https://arxiv.org/abs/2603.21064v2)**  
  Authors: Hwasik Jeong, Seungryong Lee, Gyeongjin Kang, Seungkwon Yang, Xiangyu Sun, Seungtae Nam, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21064v2.pdf)  
  Keywords: ar, high-fidelity, 3d gaussian, geometry, gaussian splatting  
- **[Fourier Splatting: Generalized Fourier encoded primitives for scalable radiance fields](https://arxiv.org/abs/2603.19834v1)**  
  Authors: Mihnea-Bogdan Jurca, Bert Van hauwermeiren, Adrian Munteanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19834v1.pdf)  
  Keywords: ar, high-fidelity, efficient, 3d gaussian, real-time rendering, gaussian splatting  
- **[StreetForward: Perceiving Dynamic Street with Feedforward Causal Attention](https://arxiv.org/abs/2603.19552v1)**  
  Authors: Zhongrui Yu, Zhao Wang, Yijia Xie, Yida Wang, Xueyang Zhang, Yifei Zhan, Kun Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19552v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://streetforward.github.io)  
  Keywords: ar, high-fidelity, autonomous driving, efficient, motion, 3d gaussian, geometry, gaussian splatting, dynamic  
- **[GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning](https://arxiv.org/abs/2603.19137v1)**  
  Authors: Yiren Lu, Yi Du, Disheng Liu, Yunlai Zhou, Chen Wang, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19137v1.pdf)  
  Keywords: ar, high-fidelity, 3d gaussian, geometry, gaussian splatting, semantic  
- **[CrowdGaussian: Reconstructing High-Fidelity 3D Gaussians for Human Crowd from a Single Image](https://arxiv.org/abs/2603.17779v2)**  
  Authors: Yizheng Song, Yiyu Zhuang, Qipeng Xu, Haixiang Wang, Jiahe Zhu, Jing Tian, Siyu Zhu, Hao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17779v2.pdf)  
  Keywords: ar, high-fidelity, human, 3d gaussian, geometry, gaussian splatting  

### Ray Tracing

- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v1)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v1.pdf)  
  Keywords: ar, ray tracing, reflection, mapping, 3d gaussian, relightable, gaussian splatting, shadow  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: ar, face, path tracing, 3d gaussian, real-time rendering, geometry  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: ar, high-fidelity, fast, efficient, face, ray tracing, 3d gaussian, nerf, geometry, real-time rendering, gaussian splatting  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v2)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v2.pdf)  
  Keywords: ar, ray tracing, mapping, 3d gaussian, survey, gaussian splatting  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: ar, high-fidelity, efficient, 3d gaussian, real-time rendering, gaussian splatting, ray marching  
- **[Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction](https://arxiv.org/abs/2603.08503v1)**  
  Authors: Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08503v1.pdf) | [![GitHub](https://img.shields.io/github/stars/1170632760/Spherical-GOF?style=social)](https://github.com/1170632760/Spherical-GOF)  
  Keywords: ar, fast, efficient, 3d gaussian, geometry, robotics, gaussian splatting, ray casting  
- **[Ref-DGS: Reflective Dual Gaussian Splatting](https://arxiv.org/abs/2603.07664v2)**  
  Authors: Ningjing Fan, Yiqun Wang, Dongming Yan, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07664v2.pdf)  
  Keywords: lightweight, ar, fast, efficient, face, ray tracing, reflection, geometry, gaussian splatting  
- **[Radiometrically Consistent Gaussian Surfels for Inverse Rendering](https://arxiv.org/abs/2603.01491v1)**  
  Authors: Kyu Beom Han, Jaeyoon Kim, Woo Jae Kim, Jinhwan Seo, Sung-eui Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01491v1.pdf)  
  Keywords: relighting, ar, efficient, ray tracing, reflection, lighting, global illumination, gaussian splatting, illumination  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: outdoor, ar, autonomous driving, lighting, global illumination, 3d gaussian, nerf, real-time rendering, gaussian splatting, illumination  
- **[Rotated Lights for Consistent and Efficient 2D Gaussians Inverse Rendering](https://arxiv.org/abs/2602.08724v1)**  
  Authors: Geng Lin, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08724v1.pdf)  
  Keywords: relighting, ar, efficient, lighting, global illumination, geometry, shadow, gaussian splatting, illumination  

### Relighting

*Showing the latest 50 out of 71 papers*

- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v1)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v1.pdf)  
  Keywords: ar, ray tracing, reflection, mapping, 3d gaussian, relightable, gaussian splatting, shadow  
- **[PhotoAgent: A Robotic Photographer with Spatial and Aesthetic Understanding](https://arxiv.org/abs/2603.22796v1)**  
  Authors: Lirong Che, Zhenfeng Gan, Yanbo Chen, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22796v1.pdf)  
  Keywords: ar, understanding, reflection, 3d gaussian, gaussian splatting, semantic  
- **[EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](https://arxiv.org/abs/2603.21332v1)**  
  Authors: Haolan Xu, Keli Cheng, Lei Wang, Ning Bi, Xiaoming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21332v1.pdf)  
  Keywords: ar, face, few-shot, motion, lighting, 3d gaussian, nerf, gaussian splatting, head  
- **[TRGS-SLAM: IMU-Aided Gaussian Splatting SLAM for Blurry, Rolling Shutter, and Noisy Thermal Images](https://arxiv.org/abs/2603.20443v1)**  
  Authors: Spencer Carmichael, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20443v1.pdf)  
  Keywords: ar, fast, motion, tracking, slam, mapping, 3d gaussian, robotics, gaussian splatting, dynamic, illumination, localization  
- **[HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks](https://arxiv.org/abs/2603.19822v1)**  
  Authors: Jingyu Guo, Ziye Chen, Ziwen Li, Zhengqing Gao, Jiaxin Huang, Hanlue Zhang, Fengming Huang, Yu Yao, Tongliang Liu, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19822v1.pdf)  
  Keywords: ar, lighting, 3d gaussian, geometry, gaussian splatting, semantic  
- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: ar, face, understanding, lighting, slam, mapping, segmentation, 3d gaussian, gaussian splatting, semantic  
- **[E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction](https://arxiv.org/abs/2603.14684v1)**  
  Authors: Yunsoo Kim, Changki Sung, Dasol Hong, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14684v1.pdf)  
  Keywords: ar, fast, motion, tracking, lighting, 3d gaussian, nerf, 3d reconstruction, gaussian splatting, dynamic  
- **[PhyGaP: Physically-Grounded Gaussians with Polarization Cues](https://arxiv.org/abs/2603.14001v1)**  
  Authors: Jiale Wu, Xiaoyang Bai, Zongqi He, Weiwei Xu, Yifan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14001v1.pdf)  
  Keywords: relighting, ar, high-fidelity, face, reflection, lighting, 3d gaussian, gaussian splatting  
- **[LR-SGS: Robust LiDAR-Reflectance-Guided Salient Gaussian Splatting for Self-Driving Scene Reconstruction](https://arxiv.org/abs/2603.12647v1)**  
  Authors: Ziyu Chen, Fan Zhu, Hui Zhu, Deyi Kong, Xinkai Kuang, Yujia Zhang, Chunmao Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12647v1.pdf)  
  Keywords: ar, efficient, motion, lighting, 3d gaussian, gaussian splatting  
- **[InstantHDR: Single-forward Gaussian Splatting for High Dynamic Range 3D Reconstruction](https://arxiv.org/abs/2603.11298v2)**  
  Authors: Dingqiang Ye, Jiacong Xu, Jianglu Ping, Yuxiang Guo, Chao Fan, Vishal M. Patel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11298v2.pdf)  
  Keywords: ar, lighting, mapping, geometry, 3d reconstruction, gaussian splatting, dynamic  

### SLAM

*Showing the latest 50 out of 74 papers*

- **[SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision](https://arxiv.org/abs/2603.24036v1)**  
  Authors: Avigail Cohen Rimon, Amir Mann, Mirela Ben Chen, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24036v1.pdf)  
  Keywords: deformation, ar, tracking, 3d gaussian, gaussian splatting, compact  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v1)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v1.pdf)  
  Keywords: ar, ray tracing, reflection, mapping, 3d gaussian, relightable, gaussian splatting, shadow  
- **[Instrument-Splatting++: Towards Controllable Surgical Instrument Digital Twin Using Gaussian Splatting](https://arxiv.org/abs/2603.22792v2)**  
  Authors: Shuojue Yang, Zijian Wu, Chengjiaao Liao, Qian Li, Daiyun Shen, Chang Han Low, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22792v2.pdf)  
  Keywords: ar, tracking, 3d gaussian, geometry, gaussian splatting, semantic  
- **[FreeArtGS: Articulated Gaussian Splatting Under Free-moving Scenario](https://arxiv.org/abs/2603.22102v1)**  
  Authors: Hang Dai, Hongwei Fan, Han Zhang, Duojin Wu, Jiyao Zhang, Hao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22102v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://freeartgs.github.io)  
  Keywords: ar, motion, tracking, segmentation, geometry, robotics, gaussian splatting  
- **[SGAD-SLAM: Splatting Gaussians at Adjusted Depth for Better Radiance Fields in RGBD SLAM](https://arxiv.org/abs/2603.21055v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21055v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/SGAD-SLAM-Project)  
  Keywords: ar, tracking, slam, gaussian splatting, 3d gaussian, mapping  
- **[Glove2Hand: Synthesizing Natural Hand-Object Interaction from Multi-Modal Sensing Gloves](https://arxiv.org/abs/2603.20850v1)**  
  Authors: Xinyu Zhang, Ziyi Kou, Chuan Qin, Mia Huang, Ergys Ristani, Ankit Kumar, Lele Chen, Kun He, Abdeslam Boularias, Li Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20850v1.pdf)  
  Keywords: deformation, ar, understanding, motion, tracking, vr, 3d gaussian, robotics, dynamic  
- **[TRGS-SLAM: IMU-Aided Gaussian Splatting SLAM for Blurry, Rolling Shutter, and Noisy Thermal Images](https://arxiv.org/abs/2603.20443v1)**  
  Authors: Spencer Carmichael, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20443v1.pdf)  
  Keywords: ar, fast, motion, tracking, slam, mapping, 3d gaussian, robotics, gaussian splatting, dynamic, illumination, localization  
- **[OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2603.18510v1)**  
  Authors: Hongjia Zhai, Qi Zhang, Xiaokun Pan, Xiyu Zhang, Yitong Dong, Huaqi Zhang, Dan Xu, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18510v1.pdf)  
  Keywords: ar, efficient, understanding, mapping, 3d gaussian, gaussian splatting, semantic  
- **[Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning](https://arxiv.org/abs/2603.18402v1)**  
  Authors: Yonghan Lee, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18402v1.pdf)  
  Keywords: ar, motion, tracking, segmentation, gaussian splatting, dynamic, 4d  
- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: ar, face, understanding, lighting, slam, mapping, segmentation, 3d gaussian, gaussian splatting, semantic  

### Scene Understanding

*Showing the latest 50 out of 134 papers*

- **[Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction](https://arxiv.org/abs/2603.22852v1)**  
  Authors: Chengxin Lv, Yihui Li, Hongyu Yang, YunHong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22852v1.pdf)  
  Keywords: ar, autonomous driving, efficient, 3d gaussian, geometry, semantic, compact  
- **[PhotoAgent: A Robotic Photographer with Spatial and Aesthetic Understanding](https://arxiv.org/abs/2603.22796v1)**  
  Authors: Lirong Che, Zhenfeng Gan, Yanbo Chen, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22796v1.pdf)  
  Keywords: ar, understanding, reflection, 3d gaussian, gaussian splatting, semantic  
- **[Instrument-Splatting++: Towards Controllable Surgical Instrument Digital Twin Using Gaussian Splatting](https://arxiv.org/abs/2603.22792v2)**  
  Authors: Shuojue Yang, Zijian Wu, Chengjiaao Liao, Qian Li, Daiyun Shen, Chang Han Low, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22792v2.pdf)  
  Keywords: ar, tracking, 3d gaussian, geometry, gaussian splatting, semantic  
- **[FreeArtGS: Articulated Gaussian Splatting Under Free-moving Scenario](https://arxiv.org/abs/2603.22102v1)**  
  Authors: Hang Dai, Hongwei Fan, Han Zhang, Duojin Wu, Jiyao Zhang, Hao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22102v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://freeartgs.github.io)  
  Keywords: ar, motion, tracking, segmentation, geometry, robotics, gaussian splatting  
- **[Training-Free Instance-Aware 3D Scene Reconstruction and Diffusion-Based View Synthesis from Sparse Images](https://arxiv.org/abs/2603.21166v1)**  
  Authors: Jiatong Xia, Lingqiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21166v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiatongxia.github.io/TID3R)  
  Keywords: ar, high-fidelity, efficient, understanding, segmentation, geometry  
- **[Glove2Hand: Synthesizing Natural Hand-Object Interaction from Multi-Modal Sensing Gloves](https://arxiv.org/abs/2603.20850v1)**  
  Authors: Xinyu Zhang, Ziyi Kou, Chuan Qin, Mia Huang, Ergys Ristani, Ankit Kumar, Lele Chen, Kun He, Abdeslam Boularias, Li Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20850v1.pdf)  
  Keywords: deformation, ar, understanding, motion, tracking, vr, 3d gaussian, robotics, dynamic  
- **[HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks](https://arxiv.org/abs/2603.19822v1)**  
  Authors: Jingyu Guo, Ziye Chen, Ziwen Li, Zhengqing Gao, Jiaxin Huang, Hanlue Zhang, Fengming Huang, Yu Yao, Tongliang Liu, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19822v1.pdf)  
  Keywords: ar, lighting, 3d gaussian, geometry, gaussian splatting, semantic  
- **[Reconstruction Matters: Learning Geometry-Aligned BEV Representation through 3D Gaussian Splatting](https://arxiv.org/abs/2603.19193v1)**  
  Authors: Yiren Lu, Xin Ye, Burhaneddin Yaman, Jingru Luo, Zhexiao Xiong, Liu Ren, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19193v1.pdf)  
  Keywords: ar, autonomous driving, understanding, motion, segmentation, 3d gaussian, geometry, 3d reconstruction, gaussian splatting, semantic  
- **[GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning](https://arxiv.org/abs/2603.19137v1)**  
  Authors: Yiren Lu, Yi Du, Disheng Liu, Yunlai Zhou, Chen Wang, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19137v1.pdf)  
  Keywords: ar, high-fidelity, 3d gaussian, geometry, gaussian splatting, semantic  
- **[GHOST: Fast Category-agnostic Hand-Object Interaction Reconstruction from RGB Videos using Gaussian Splatting](https://arxiv.org/abs/2603.18912v1)**  
  Authors: Ahmed Tawfik Aboukhadra, Marcel Rogge, Nadia Robertini, Abdalla Arafa, Jameel Malik, Ahmed Elhayek, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18912v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ATAboukhadra/GHOST?style=social)](https://github.com/ATAboukhadra/GHOST)  
  Keywords: ar, efficient, fast, understanding, vr, robotics, 3d reconstruction, gaussian splatting, dynamic  



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