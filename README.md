# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-11-12 00:54:10

## 📰 Latest Updates

🔧 **[2025-06-26] HTTP 301 Redirect Issue Completely Resolved!** 
- Implemented multi-layer fallback strategy to thoroughly solve network compatibility issues

🔧 **[2025-06-26] Configurable Search Keywords Feature Added!**
- You can now customize search keywords by modifying `data/search_config.json`
- Support for different search scopes: abstract-only, title-only, or both
- Flexible keyword configuration for targeted paper collection

- View detailed updates: [News.md](News.md) 📋

---

## Categories

- [3DGS Surveys](#3dgs-surveys) (12 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (327 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (993 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (347 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (362 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (70 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (323 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (67 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (428 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (161 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (24 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (106 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (138 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (166 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, survey, high-fidelity, semantic, localization, slam, robotics, ar, gaussian splatting, mapping, 3d gaussian  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, animation, efficient rendering, survey, lighting, ar, gaussian splatting, real-time rendering, avatar, 3d reconstruction, face, 3d gaussian  
- **[A Study of the Framework and Real-World Applications of Language Embedding for 3D Scene Understanding](https://arxiv.org/abs/)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, survey, semantic, robotics, ar, gaussian splatting, nerf, understanding, 3d gaussian  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, segmentation, survey, localization, semantic, slam, ar, gaussian splatting, mapping, nerf, 3d gaussian  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, survey, ar, gaussian splatting, 3d reconstruction  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, survey, semantic, lighting, robotics, ar, gaussian splatting, 3d gaussian  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: survey, dynamic, ar, gaussian splatting, real-time rendering, 3d gaussian  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, survey, ar, gaussian splatting, real-time rendering, understanding, 3d gaussian  
- **[Survey on Fundamental Deep Learning 3D Reconstruction Techniques](https://arxiv.org/abs/)**  
  Authors: Yonge Bai, LikHang Wong, TszYin Twan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: survey, lighting, ar, gaussian splatting, 3d reconstruction, nerf, 3d gaussian  
- **[Recent Advances in 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Tong Wu, Yu-Jie Yuan, Ling-Xiao Zhang, Jie Yang, Yan-Pei Cao, Ling-Qi Yan, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, efficient rendering, survey, geometry, dynamic, ar, gaussian splatting, 3d reconstruction, nerf, understanding, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 327 papers*

- **[ConeGS: Error-Guided Densification Using Pixel Cones for Improved Reconstruction with Fewer Primitives](https://arxiv.org/abs/)**  
  Authors: Bartłomiej Baranowski, Stefano Esposito, Patricia Gschoßmann, Anpei Chen, Andreas Geiger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, geometry, ar, gaussian splatting, 3d gaussian  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, large scene, head, gaussian splatting, ar, 3d gaussian  
- **[3D Gaussian Point Encoders](https://arxiv.org/abs/)**  
  Authors: Jim James, Ben Wilson, Simon Lucey, James Hays  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, lightweight, geometry, recognition, ar, gaussian splatting, 3d reconstruction, nerf, 3d gaussian  
- **[4D Neural Voxel Splatting: Dynamic Scene Rendering with Voxelized Guassian Splatting](https://arxiv.org/abs/)**  
  Authors: Chun-Tin Wu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, efficient rendering, compact, dynamic, head, gaussian splatting, real-time rendering, ar, 3d gaussian, 4d, deformation  
- **[SAGS: Self-Adaptive Alias-Free Gaussian Splatting for Dynamic Surgical Endoscopic Reconstruction](https://arxiv.org/abs/)**  
  Authors: Wenfeng Huang, Xiangyun Liao, Yinling Qian, Hao Liu, Yongming Yang, Wenjing Jia, Qiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, dynamic, ar, gaussian splatting, nerf, 3d gaussian, 4d, deformation  
- **[Explicit Memory through Online 3D Gaussian Splatting Improves Class-Agnostic Video Segmentation](https://arxiv.org/abs/)**  
  Authors: Anthony Opipari, Aravindhan K Krishnan, Shreekant Gayaka, Min Sun, Cheng-Hao Kuo, Arnie Sen, Odest Chadwicke Jenkins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://topipari.com/projects/FastSAM-Splat/)  
  Keywords: fast, segmentation, ar, gaussian splatting, 3d gaussian  
- **[DynamicTree: Interactive Real Tree Animation via Sparse Voxel Spectrum](https://arxiv.org/abs/)**  
  Authors: Yaokun Li, Lihe Ding, Xiao Chen, Guang Tan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, animation, compact, semantic, dynamic, motion, gaussian splatting, ar, face, 3d gaussian, 4d  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, animation, efficient rendering, survey, lighting, ar, gaussian splatting, real-time rendering, avatar, 3d reconstruction, face, 3d gaussian  
- **[ArchitectHead: Continuous Level of Detail Control for 3D Gaussian Head Avatars](https://arxiv.org/abs/)**  
  Authors: Peizhi Yan, Rabab Ward, Qiang Tang, Shan Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, lightweight, dynamic, head, gaussian splatting, real-time rendering, avatar, ar, 3d gaussian  
- **[Optimized Minimal 4D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee, Eunsoo Lee, Sangmin Kim, Seunghyeon Song, Joo Chan Lee, Jong Hwan Ko, Jaesik Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://minshirley.github.io/OMG4/.)  
  Keywords: compression, high-fidelity, compact, dynamic, motion, gaussian splatting, real-time rendering, head, ar, face, 4d  

### Applications

*Showing the latest 50 out of 993 papers*

- **[Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction](https://arxiv.org/abs/)**  
  Authors: Changyue Shi, Chuxiao Yang, Xinyuan Hu, Minghao Chen, Wenwen Pan, Yan Yang, Jiajun Ding, Zhou Yu, Jun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: few-shot, dynamic, ar, gaussian splatting, nerf, 4d, deformation  
- **[ConeGS: Error-Guided Densification Using Pixel Cones for Improved Reconstruction with Fewer Primitives](https://arxiv.org/abs/)**  
  Authors: Bartłomiej Baranowski, Stefano Esposito, Patricia Gschoßmann, Anpei Chen, Andreas Geiger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, geometry, ar, gaussian splatting, 3d gaussian  
- **[Physics-Informed Deformable Gaussian Splatting: Towards Unified Constitutive Laws for Time-Evolving Material Field](https://arxiv.org/abs/)**  
  Authors: Haoqin Hong, Ding Fan, Fubin Dou, Zhi-Li Zhou, Haoran Sun, Congcong Zhu, Jingrun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, geometry, dynamic, motion, gaussian splatting, ar, 3d gaussian, 4d  
- **[4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes from Monocular Videos](https://arxiv.org/abs/)**  
  Authors: Mengqi Guo, Bo Xu, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, segmentation, neural rendering, geometry, dynamic, motion, gaussian splatting, ar, nerf, 3d gaussian, 4d, deformation  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, large scene, head, gaussian splatting, ar, 3d gaussian  
- **[3D Gaussian Point Encoders](https://arxiv.org/abs/)**  
  Authors: Jim James, Ben Wilson, Simon Lucey, James Hays  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, lightweight, geometry, recognition, ar, gaussian splatting, 3d reconstruction, nerf, 3d gaussian  
- **[CaRF: Enhancing Multi-View Consistency in Referring 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/)**  
  Authors: Yuwen Tao, Kanglei Zhou, Xin Tan, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, geometry, ar, gaussian splatting, understanding, vr, 3d gaussian  
- **[4D Neural Voxel Splatting: Dynamic Scene Rendering with Voxelized Guassian Splatting](https://arxiv.org/abs/)**  
  Authors: Chun-Tin Wu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, efficient rendering, compact, dynamic, head, gaussian splatting, real-time rendering, ar, 3d gaussian, 4d, deformation  
- **[SAGS: Self-Adaptive Alias-Free Gaussian Splatting for Dynamic Surgical Endoscopic Reconstruction](https://arxiv.org/abs/)**  
  Authors: Wenfeng Huang, Xiangyun Liao, Yinling Qian, Hao Liu, Yongming Yang, Wenjing Jia, Qiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, dynamic, ar, gaussian splatting, nerf, 3d gaussian, 4d, deformation  
- **[6D Channel Knowledge Map Construction via Bidirectional Wireless Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Juncong Zhou, Chao Hu, Guanlin Wu, Zixiang Ren, Han Hu, Juyong Zhang, Rui Zhang, Jie Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: dynamic, ar, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 347 papers*

- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, large scene, head, gaussian splatting, ar, 3d gaussian  
- **[4D Neural Voxel Splatting: Dynamic Scene Rendering with Voxelized Guassian Splatting](https://arxiv.org/abs/)**  
  Authors: Chun-Tin Wu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, efficient rendering, compact, dynamic, head, gaussian splatting, real-time rendering, ar, 3d gaussian, 4d, deformation  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians](https://arxiv.org/abs/)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: semantic, urban scene, ar, gaussian splatting, 3d reconstruction, face  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, human, high-fidelity, outdoor, slam, dynamic, ar, gaussian splatting, mapping, 3d gaussian  
- **[DynamicTree: Interactive Real Tree Animation via Sparse Voxel Spectrum](https://arxiv.org/abs/)**  
  Authors: Yaokun Li, Lihe Ding, Xiao Chen, Guang Tan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, animation, compact, semantic, dynamic, motion, gaussian splatting, ar, face, 3d gaussian, 4d  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, animation, efficient rendering, survey, lighting, ar, gaussian splatting, real-time rendering, avatar, 3d reconstruction, face, 3d gaussian  
- **[2DGS-R: Revisiting the Normal Consistency Regularization in 2D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Haofan Ren, Qingsong Yan, Ming Lu, Rongfeng Lu, Zunjie Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: high-fidelity, lighting, head, gaussian splatting, ar, face, 3d gaussian  
- **[Leveraging Learned Image Prior for 3D Gaussian Compression](https://arxiv.org/abs/)**  
  Authors: Seungjoo Shin, Jaesik Park, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: compression, compact, head, gaussian splatting, ar, 3d gaussian  
- **[Instant Skinned Gaussian Avatars for Web, Mobile and VR Applications](https://arxiv.org/abs/)**  
  Authors: Naruya Kondo, Yuto Asano, Yoichi Ochiai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaussian-vrm.github.io/)  
  Keywords: efficient, lightweight, dynamic, ar, gaussian splatting, avatar, vr  
- **[InsideOut: Integrated RGB-Radiative Gaussian Splatting for Comprehensive 3D Object Representation](https://arxiv.org/abs/)**  
  Authors: Jungmin Lee, Seonghyuk Hong, Juyong Lee, Jaeyoon Lee, Jongwon Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: medical, high-fidelity, ar, gaussian splatting, face, 3d gaussian  

### Dynamic Scene

*Showing the latest 50 out of 362 papers*

- **[Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction](https://arxiv.org/abs/)**  
  Authors: Changyue Shi, Chuxiao Yang, Xinyuan Hu, Minghao Chen, Wenwen Pan, Yan Yang, Jiajun Ding, Zhou Yu, Jun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: few-shot, dynamic, ar, gaussian splatting, nerf, 4d, deformation  
- **[Physics-Informed Deformable Gaussian Splatting: Towards Unified Constitutive Laws for Time-Evolving Material Field](https://arxiv.org/abs/)**  
  Authors: Haoqin Hong, Ding Fan, Fubin Dou, Zhi-Li Zhou, Haoran Sun, Congcong Zhu, Jingrun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, geometry, dynamic, motion, gaussian splatting, ar, 3d gaussian, 4d  
- **[4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes from Monocular Videos](https://arxiv.org/abs/)**  
  Authors: Mengqi Guo, Bo Xu, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, segmentation, neural rendering, geometry, dynamic, motion, gaussian splatting, ar, nerf, 3d gaussian, 4d, deformation  
- **[4D Neural Voxel Splatting: Dynamic Scene Rendering with Voxelized Guassian Splatting](https://arxiv.org/abs/)**  
  Authors: Chun-Tin Wu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, efficient rendering, compact, dynamic, head, gaussian splatting, real-time rendering, ar, 3d gaussian, 4d, deformation  
- **[SAGS: Self-Adaptive Alias-Free Gaussian Splatting for Dynamic Surgical Endoscopic Reconstruction](https://arxiv.org/abs/)**  
  Authors: Wenfeng Huang, Xiangyun Liao, Yinling Qian, Hao Liu, Yongming Yang, Wenjing Jia, Qiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, dynamic, ar, gaussian splatting, nerf, 3d gaussian, 4d, deformation  
- **[6D Channel Knowledge Map Construction via Bidirectional Wireless Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Juncong Zhou, Chao Hu, Guanlin Wu, Zixiang Ren, Han Hu, Juyong Zhang, Rui Zhang, Jie Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: dynamic, ar, gaussian splatting  
- **[HEIR: Learning Graph-Based Motion Hierarchies](https://arxiv.org/abs/)**  
  Authors: Cheng Zheng, William Koch, Baiang Li, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://light.princeton.edu/HEIR/)  
  Keywords: robotics, dynamic, motion, gaussian splatting, ar, 3d gaussian, deformation  
- **[DynaPose4D: High-Quality 4D Dynamic Content Generation via Pose Alignment Loss](https://arxiv.org/abs/)**  
  Authors: Jing Yang, Yufeng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: animation, geometry, dynamic, motion, gaussian splatting, ar, 3d gaussian, 4d  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, human, high-fidelity, outdoor, slam, dynamic, ar, gaussian splatting, mapping, 3d gaussian  
- **[DynamicTree: Interactive Real Tree Animation via Sparse Voxel Spectrum](https://arxiv.org/abs/)**  
  Authors: Yaokun Li, Lihe Ding, Xiao Chen, Guang Tan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, animation, compact, semantic, dynamic, motion, gaussian splatting, ar, face, 3d gaussian, 4d  

### Few-shot

*Showing the latest 50 out of 70 papers*

- **[Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction](https://arxiv.org/abs/)**  
  Authors: Changyue Shi, Chuxiao Yang, Xinyuan Hu, Minghao Chen, Wenwen Pan, Yan Yang, Jiajun Ding, Zhou Yu, Jun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: few-shot, dynamic, ar, gaussian splatting, nerf, 4d, deformation  
- **[D$^2$GS: Depth-and-Density Guided Gaussian Splatting for Stable and Accurate Sparse-View Reconstruction](https://arxiv.org/abs/)**  
  Authors: Meixi Song, Xin Lin, Dizhe Zhang, Haodong Li, Xiangtai Li, Bo Du, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insta360-research-team.github.io/DDGS-website/.)  
  Keywords: sparse-view, high-fidelity, ar, gaussian splatting, 3d gaussian, sparse view  
- **[FSFSplatter: Build Surface and Novel Views with Sparse-Views within 2min](https://arxiv.org/abs/)**  
  Authors: Yibin Zhao, Yihan Pan, Jun Nan, Liwei Chen, Jianjun Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, sparse-view, geometry, head, gaussian splatting, ar, face  
- **[HART: Human Aligned Reconstruction Transformer](https://arxiv.org/abs/)**  
  Authors: Xiyi Chen, Shaofei Wang, Marko Mihajlovic, Taewon Kang, Sergey Prokudin, Ming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: human, sparse-view, geometry, body, ar  
- **[OracleGS: Grounding Generative Priors for Sparse-View Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Atakan Topaloglu, Kunyi Li, Michael Niemeyer, Nassir Navab, A. Murat Tekalp, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: sparse-view, ar, gaussian splatting, nerf, 3d gaussian, sparse view  
- **[SPFSplatV2: Efficient Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views](https://arxiv.org/abs/)**  
  Authors: Ranran Huang, Krystian Mikolajczyk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ranrhuang.github.io/spfsplatv2/.)  
  Keywords: efficient, ar, gaussian splatting, 3d gaussian, sparse view  
- **[Segmentation-Driven Initialization for Sparse-view 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Yi-Hsin Li, Thomas Sikora, Sebastian Knorr, Måarten Sjöström  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, segmentation, sparse-view, geometry, motion, ar, gaussian splatting, real-time rendering, 3d gaussian  
- **[${C}^{3}$-GS: Learning Context-aware, Cross-dimension, Cross-scale Feature for Generalizable Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Yuxi Hu, Jun Zhang, Kuangyi Chen, Zhe Zhang, Friedrich Fraundorfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: lightweight, geometry, ar, gaussian splatting, sparse view  
- **[Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Kangjie Chen, Yingji Zhong, Zhihao Li, Jiaqi Lin, Youyu Chen, Minghan Qin, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: sparse-view, lightweight, ar, gaussian splatting, understanding, 3d gaussian  
- **[Toward Human-Robot Teaming: Learning Handover Behaviors from 3D Scenes](https://arxiv.org/abs/)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: human, gaussian splatting, sparse-view, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 323 papers*

- **[ConeGS: Error-Guided Densification Using Pixel Cones for Improved Reconstruction with Fewer Primitives](https://arxiv.org/abs/)**  
  Authors: Bartłomiej Baranowski, Stefano Esposito, Patricia Gschoßmann, Anpei Chen, Andreas Geiger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, geometry, ar, gaussian splatting, 3d gaussian  
- **[Physics-Informed Deformable Gaussian Splatting: Towards Unified Constitutive Laws for Time-Evolving Material Field](https://arxiv.org/abs/)**  
  Authors: Haoqin Hong, Ding Fan, Fubin Dou, Zhi-Li Zhou, Haoran Sun, Congcong Zhu, Jingrun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, geometry, dynamic, motion, gaussian splatting, ar, 3d gaussian, 4d  
- **[4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes from Monocular Videos](https://arxiv.org/abs/)**  
  Authors: Mengqi Guo, Bo Xu, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, segmentation, neural rendering, geometry, dynamic, motion, gaussian splatting, ar, nerf, 3d gaussian, 4d, deformation  
- **[3D Gaussian Point Encoders](https://arxiv.org/abs/)**  
  Authors: Jim James, Ben Wilson, Simon Lucey, James Hays  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, lightweight, geometry, recognition, ar, gaussian splatting, 3d reconstruction, nerf, 3d gaussian  
- **[CaRF: Enhancing Multi-View Consistency in Referring 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/)**  
  Authors: Yuwen Tao, Kanglei Zhou, Xin Tan, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, geometry, ar, gaussian splatting, understanding, vr, 3d gaussian  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians](https://arxiv.org/abs/)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: semantic, urban scene, ar, gaussian splatting, 3d reconstruction, face  
- **[DynaPose4D: High-Quality 4D Dynamic Content Generation via Pose Alignment Loss](https://arxiv.org/abs/)**  
  Authors: Jing Yang, Yufeng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: animation, geometry, dynamic, motion, gaussian splatting, ar, 3d gaussian, 4d  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, animation, efficient rendering, survey, lighting, ar, gaussian splatting, real-time rendering, avatar, 3d reconstruction, face, 3d gaussian  
- **[GauSSmart: Enhanced 3D Reconstruction through 2D Foundation Models and Geometric Filtering](https://arxiv.org/abs/)**  
  Authors: Alexander Valverde, Brian Xu, Yuyin Zhou, Meng Xu, Hongyun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, semantic, lighting, ar, gaussian splatting, 3d reconstruction, nerf, 3d gaussian  
- **[BalanceGS: Algorithm-System Co-design for Efficient 3D Gaussian Splatting Training on GPU](https://arxiv.org/abs/)**  
  Authors: Junyi Wu, Jiaming Xu, Jinhao Li, Yongkang Zhou, Jiayi Pan, Xingyang Li, Guohao Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, dynamic, ar, gaussian splatting, mapping, 3d reconstruction, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 67 papers*

- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, large scene, head, gaussian splatting, ar, 3d gaussian  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians](https://arxiv.org/abs/)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: semantic, urban scene, ar, gaussian splatting, 3d reconstruction, face  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, human, high-fidelity, outdoor, slam, dynamic, ar, gaussian splatting, mapping, 3d gaussian  
- **[Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering](https://arxiv.org/abs/)**  
  Authors: Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, tracking, urban scene, dynamic, motion, gaussian splatting, ar, 3d gaussian, deformation  
- **[Two-Stage Gaussian Splatting Optimization for Outdoor Scene Reconstruction](https://arxiv.org/abs/)**  
  Authors: Deborah Pintani, Ariel Caputo, Noah Lewis, Marc Stamminger, Fabio Pellacini, Andrea Giachetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: illumination, outdoor, motion, ar, gaussian splatting  
- **[LOBE-GS: Load-Balanced and Efficient 3D Gaussian Splatting for Large-Scale Scene Reconstruction](https://arxiv.org/abs/)**  
  Authors: Sheng-Hsiang Hung, Ting-Yu Yen, Wei-Fang Sun, Simon See, Shih-Hsuan Hung, Hung-Kuo Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, lightweight, high-fidelity, outdoor, head, gaussian splatting, ar, 3d gaussian  
- **[ROSGS: Relightable Outdoor Scenes With Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Lianjun Liao, Chunhui Zhang, Tong Wu, Henglei Lv, Bailin Deng, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, relightable, efficient rendering, illumination, geometry, outdoor, lighting, compact, head, gaussian splatting, ar, nerf, 3d gaussian, relighting  
- **[GSVisLoc: Generalizable Visual Localization for Gaussian Splatting Scene Representations](https://arxiv.org/abs/)**  
  Authors: Fadi Khatib, Dror Moran, Guy Trostianetsky, Yoni Kasten, Meirav Galun, Ronen Basri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: localization, outdoor, ar, gaussian splatting, 3d gaussian  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: illumination, outdoor, lighting, ar, gaussian splatting, 3d reconstruction, understanding, 3d gaussian  
- **[Multi-view Normal and Distance Guidance Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/)**  
  Authors: Bo Jia, Yanan Guo, Ying Chang, Benkui Zhang, Ying Xie, Kangning Du, Lin Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: geometry, outdoor, ar, gaussian splatting, face, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 428 papers*

- **[ConeGS: Error-Guided Densification Using Pixel Cones for Improved Reconstruction with Fewer Primitives](https://arxiv.org/abs/)**  
  Authors: Bartłomiej Baranowski, Stefano Esposito, Patricia Gschoßmann, Anpei Chen, Andreas Geiger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, geometry, ar, gaussian splatting, 3d gaussian  
- **[Physics-Informed Deformable Gaussian Splatting: Towards Unified Constitutive Laws for Time-Evolving Material Field](https://arxiv.org/abs/)**  
  Authors: Haoqin Hong, Ding Fan, Fubin Dou, Zhi-Li Zhou, Haoran Sun, Congcong Zhu, Jingrun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, geometry, dynamic, motion, gaussian splatting, ar, 3d gaussian, 4d  
- **[4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes from Monocular Videos](https://arxiv.org/abs/)**  
  Authors: Mengqi Guo, Bo Xu, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, segmentation, neural rendering, geometry, dynamic, motion, gaussian splatting, ar, nerf, 3d gaussian, 4d, deformation  
- **[3D Gaussian Point Encoders](https://arxiv.org/abs/)**  
  Authors: Jim James, Ben Wilson, Simon Lucey, James Hays  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, lightweight, geometry, recognition, ar, gaussian splatting, 3d reconstruction, nerf, 3d gaussian  
- **[4D Neural Voxel Splatting: Dynamic Scene Rendering with Voxelized Guassian Splatting](https://arxiv.org/abs/)**  
  Authors: Chun-Tin Wu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, efficient rendering, compact, dynamic, head, gaussian splatting, real-time rendering, ar, 3d gaussian, 4d, deformation  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, survey, high-fidelity, semantic, localization, slam, robotics, ar, gaussian splatting, mapping, 3d gaussian  
- **[DynamicTree: Interactive Real Tree Animation via Sparse Voxel Spectrum](https://arxiv.org/abs/)**  
  Authors: Yaokun Li, Lihe Ding, Xiao Chen, Guang Tan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, animation, compact, semantic, dynamic, motion, gaussian splatting, ar, face, 3d gaussian, 4d  
- **[MoE-GS: Mixture of Experts for Dynamic Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: In-Hwan Jin, Hyeongju Mun, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anonymous.4open.science/w/MoE-GS-68BA/.)  
  Keywords: lightweight, dynamic, ar, gaussian splatting, 3d gaussian  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, animation, efficient rendering, survey, lighting, ar, gaussian splatting, real-time rendering, avatar, 3d reconstruction, face, 3d gaussian  
- **[BalanceGS: Algorithm-System Co-design for Efficient 3D Gaussian Splatting Training on GPU](https://arxiv.org/abs/)**  
  Authors: Junyi Wu, Jiaming Xu, Jinhao Li, Yongkang Zhou, Jiayi Pan, Xingyang Li, Guohao Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, dynamic, ar, gaussian splatting, mapping, 3d reconstruction, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 161 papers*

- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, survey, high-fidelity, semantic, localization, slam, robotics, ar, gaussian splatting, mapping, 3d gaussian  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, human, high-fidelity, outdoor, slam, dynamic, ar, gaussian splatting, mapping, 3d gaussian  
- **[2DGS-R: Revisiting the Normal Consistency Regularization in 2D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Haofan Ren, Qingsong Yan, Ming Lu, Rongfeng Lu, Zunjie Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: high-fidelity, lighting, head, gaussian splatting, ar, face, 3d gaussian  
- **[InsideOut: Integrated RGB-Radiative Gaussian Splatting for Comprehensive 3D Object Representation](https://arxiv.org/abs/)**  
  Authors: Jungmin Lee, Seonghyuk Hong, Juyong Lee, Jaeyoon Lee, Jongwon Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: medical, high-fidelity, ar, gaussian splatting, face, 3d gaussian  
- **[Capture, Canonicalize, Splat: Zero-Shot 3D Gaussian Avatars from Unstructured Phone Images](https://arxiv.org/abs/)**  
  Authors: Emanuel Garbin, Guy Adam, Oded Krams, Zohar Barzelay, Eran Guendelman, Michael Schwarz, Matteo Presutto, Moran Vatelmacher, Yigal Shenkman, Eli Peker, Itai Druker, Uri Patish, Yoav Blum, Max Bluvstein, Junxuan Li, Rawal Khirodkar, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: high-fidelity, body, ar, gaussian splatting, avatar, face, 3d gaussian  
- **[UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal Rendering](https://arxiv.org/abs/)**  
  Authors: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: geometry, high-fidelity, semantic, ar, gaussian splatting, 3d reconstruction, face, 3d gaussian  
- **[D$^2$GS: Depth-and-Density Guided Gaussian Splatting for Stable and Accurate Sparse-View Reconstruction](https://arxiv.org/abs/)**  
  Authors: Meixi Song, Xin Lin, Dizhe Zhang, Haodong Li, Xiangtai Li, Bo Du, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insta360-research-team.github.io/DDGS-website/.)  
  Keywords: sparse-view, high-fidelity, ar, gaussian splatting, 3d gaussian, sparse view  
- **[Optimized Minimal 4D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee, Eunsoo Lee, Sangmin Kim, Seunghyeon Song, Joo Chan Lee, Jong Hwan Ko, Jaesik Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://minshirley.github.io/OMG4/.)  
  Keywords: compression, high-fidelity, compact, dynamic, motion, gaussian splatting, real-time rendering, head, ar, face, 4d  
- **[LOBE-GS: Load-Balanced and Efficient 3D Gaussian Splatting for Large-Scale Scene Reconstruction](https://arxiv.org/abs/)**  
  Authors: Sheng-Hsiang Hung, Ting-Yu Yen, Wei-Fang Sun, Simon See, Shih-Hsuan Hung, Hung-Kuo Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, lightweight, high-fidelity, outdoor, head, gaussian splatting, ar, 3d gaussian  
- **[GS-Scale: Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading](https://arxiv.org/abs/)**  
  Authors: Donghyun Lee, Dawoon Jeong, Jae W. Lee, Hongil Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, high quality, ar, gaussian splatting, 3d gaussian  

### Ray Tracing

- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: illumination, geometry, ray tracing, ar, gaussian splatting, reflection  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: efficient, ray marching, geometry, ar, gaussian splatting, 3d gaussian  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, ray marching, relightable, efficient rendering, geometry, lighting, ar, gaussian splatting, face, 3d gaussian, relighting  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and Rasterizer](https://arxiv.org/abs/)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, ray tracing, high-fidelity, ar, gaussian splatting, real-time rendering  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, shadow, human, relightable, ray tracing, geometry, lighting, ar, gaussian splatting, avatar, relighting  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, efficient rendering, ray tracing, lighting, acceleration, ar, gaussian splatting, 3d gaussian, relighting  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: efficient, ray tracing, illumination, lighting, global illumination, gaussian splatting, real-time rendering, ar, face, 3d gaussian  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, shadow, neural rendering, ray tracing, ar, gaussian splatting, reflection, 3d gaussian  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: shadow, ray tracing, lighting, gaussian splatting, face, reflection  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, light transport, ray tracing, acceleration, ar, gaussian splatting, reflection  

### Relighting

*Showing the latest 50 out of 106 papers*

- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, animation, efficient rendering, survey, lighting, ar, gaussian splatting, real-time rendering, avatar, 3d reconstruction, face, 3d gaussian  
- **[2DGS-R: Revisiting the Normal Consistency Regularization in 2D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Haofan Ren, Qingsong Yan, Ming Lu, Rongfeng Lu, Zunjie Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: high-fidelity, lighting, head, gaussian splatting, ar, face, 3d gaussian  
- **[GauSSmart: Enhanced 3D Reconstruction through 2D Foundation Models and Geometric Filtering](https://arxiv.org/abs/)**  
  Authors: Alexander Valverde, Brian Xu, Yuyin Zhou, Meng Xu, Hongyun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, semantic, lighting, ar, gaussian splatting, 3d reconstruction, nerf, 3d gaussian  
- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: illumination, geometry, ray tracing, ar, gaussian splatting, reflection  
- **[VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via View Alignment](https://arxiv.org/abs/)**  
  Authors: Qing Li, Huifang Feng, Xun Gong, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, illumination, geometry, lighting, ar, gaussian splatting, face, 3d gaussian  
- **[Two-Stage Gaussian Splatting Optimization for Outdoor Scene Reconstruction](https://arxiv.org/abs/)**  
  Authors: Deborah Pintani, Ariel Caputo, Noah Lewis, Marc Stamminger, Fabio Pellacini, Andrea Giachetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: illumination, outdoor, motion, ar, gaussian splatting  
- **[Spec-Gloss Surfels and Normal-Diffuse Priors for Relightable Glossy Objects](https://arxiv.org/abs/)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: relightable, neural rendering, illumination, geometry, lighting, dynamic, ar, gaussian splatting, face, reflection, relighting  
- **[Universal Beta Splatting](https://arxiv.org/abs/)**  
  Authors: Rong Liu, Zhongpai Gao, Benjamin Planche, Meida Chen, Van Nguyen Nguyen, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Yue Wang, Andrew Feng, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rongliu-leo.github.io/universal-beta-splatting/.)  
  Keywords: light transport, dynamic, ar, gaussian splatting, real-time rendering, face, 3d gaussian  
- **[Large Material Gaussian Model for Relightable 3D Generation](https://arxiv.org/abs/)**  
  Authors: Jingrui Ye, Lingting Zhu, Runze Zhang, Zeyu Hu, Yingda Yin, Lanjiong Li, Lequan Yu, Qingmin Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, relightable, lighting, dynamic, ar, gaussian splatting, 3d gaussian, relighting  
- **[Seeing Through Reflections: Advancing 3D Scene Reconstruction in Mirror-Containing Environments with Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Zijing Guo, Yunyang Zhao, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: geometry, ar, gaussian splatting, mapping, 3d reconstruction, nerf, face, reflection, 3d gaussian  

### SLAM

*Showing the latest 50 out of 138 papers*

- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, survey, high-fidelity, semantic, localization, slam, robotics, ar, gaussian splatting, mapping, 3d gaussian  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, human, high-fidelity, outdoor, slam, dynamic, ar, gaussian splatting, mapping, 3d gaussian  
- **[BalanceGS: Algorithm-System Co-design for Efficient 3D Gaussian Splatting Training on GPU](https://arxiv.org/abs/)**  
  Authors: Junyi Wu, Jiaming Xu, Jinhao Li, Yongkang Zhou, Jiayi Pan, Xingyang Li, Guohao Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, dynamic, ar, gaussian splatting, mapping, 3d reconstruction, 3d gaussian  
- **[Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering](https://arxiv.org/abs/)**  
  Authors: Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, tracking, urban scene, dynamic, motion, gaussian splatting, ar, 3d gaussian, deformation  
- **[SCas4D: Structural Cascaded Optimization for Boosting Persistent 4D Novel View Synthesis](https://arxiv.org/abs/)**  
  Authors: Jipeng Lyu, Jiahua Dong, Yu-Xiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, tracking, dynamic, ar, gaussian splatting, 3d gaussian, 4d, deformation  
- **[Learning Unified Representation of 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Yuelin Xin, Yuheng Liu, Xiaohui Xie, Xinke Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, ar, gaussian splatting, mapping, 3d reconstruction, 3d gaussian  
- **[Seeing Through Reflections: Advancing 3D Scene Reconstruction in Mirror-Containing Environments with Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Zijing Guo, Yunyang Zhao, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: geometry, ar, gaussian splatting, mapping, 3d reconstruction, nerf, face, reflection, 3d gaussian  
- **[MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping](https://arxiv.org/abs/)**  
  Authors: Zhihao Cao, Hanyu Wu, Li Wa Tang, Zizhou Luo, Zihan Zhu, Wei Zhang, Marc Pollefeys, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: high-fidelity, slam, robotics, ar, gaussian splatting, mapping, autonomous driving, 3d gaussian  
- **[MemGS: Memory-Efficient Gaussian Splatting for Real-Time SLAM](https://arxiv.org/abs/)**  
  Authors: Yinlong Bai, Hongxin Zhang, Sheng Zhong, Junkai Niu, Hai Li, Yijia He, Yi Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, slam, ar, gaussian splatting, face, 3d gaussian  
- **[On the Skinning of Gaussian Avatars](https://arxiv.org/abs/)**  
  Authors: Nikolaos Zioulis, Nikolaos Kotarelas, Georgios Albanis, Spyridon Thermos, Anargyros Chatzitofis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, human, ar, gaussian splatting, mapping, avatar, deformation  

### Scene Understanding

*Showing the latest 50 out of 166 papers*

- **[4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes from Monocular Videos](https://arxiv.org/abs/)**  
  Authors: Mengqi Guo, Bo Xu, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, segmentation, neural rendering, geometry, dynamic, motion, gaussian splatting, ar, nerf, 3d gaussian, 4d, deformation  
- **[3D Gaussian Point Encoders](https://arxiv.org/abs/)**  
  Authors: Jim James, Ben Wilson, Simon Lucey, James Hays  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, fast, lightweight, geometry, recognition, ar, gaussian splatting, 3d reconstruction, nerf, 3d gaussian  
- **[CaRF: Enhancing Multi-View Consistency in Referring 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/)**  
  Authors: Yuwen Tao, Kanglei Zhou, Xin Tan, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, geometry, ar, gaussian splatting, understanding, vr, 3d gaussian  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians](https://arxiv.org/abs/)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: semantic, urban scene, ar, gaussian splatting, 3d reconstruction, face  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: efficient, survey, high-fidelity, semantic, localization, slam, robotics, ar, gaussian splatting, mapping, 3d gaussian  
- **[Explicit Memory through Online 3D Gaussian Splatting Improves Class-Agnostic Video Segmentation](https://arxiv.org/abs/)**  
  Authors: Anthony Opipari, Aravindhan K Krishnan, Shreekant Gayaka, Min Sun, Cheng-Hao Kuo, Arnie Sen, Odest Chadwicke Jenkins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://topipari.com/projects/FastSAM-Splat/)  
  Keywords: fast, segmentation, ar, gaussian splatting, 3d gaussian  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, human, high-fidelity, outdoor, slam, dynamic, ar, gaussian splatting, mapping, 3d gaussian  
- **[DynamicTree: Interactive Real Tree Animation via Sparse Voxel Spectrum](https://arxiv.org/abs/)**  
  Authors: Yaokun Li, Lihe Ding, Xiao Chen, Guang Tan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: fast, animation, compact, semantic, dynamic, motion, gaussian splatting, ar, face, 3d gaussian, 4d  
- **[GauSSmart: Enhanced 3D Reconstruction through 2D Foundation Models and Geometric Filtering](https://arxiv.org/abs/)**  
  Authors: Alexander Valverde, Brian Xu, Yuyin Zhou, Meng Xu, Hongyun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, semantic, lighting, ar, gaussian splatting, 3d reconstruction, nerf, 3d gaussian  
- **[Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering](https://arxiv.org/abs/)**  
  Authors: Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/.pdf)  
  Keywords: segmentation, tracking, urban scene, dynamic, motion, gaussian splatting, ar, 3d gaussian, deformation  



## Classic Papers
- **[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)** (SIGGRAPH 2023)  
  Authors: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis  
  Code: 🔗 [GitHub](https://github.com/graphdeco-inria/gaussian-splatting)  
  Keywords: Real-time Rendering, Neural Rendering, Point-based Graphics

## Open Source Projects
- [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) - Original implementation of 3D Gaussian Splatting
- [taichi-3d-gaussian-splatting](https://github.com/wanmeihuali/taichi-3d-gaussian-splatting) - 3D Gaussian Splatting implemented in Taichi

## Applications
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering Demo](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) - Online Demo

## Tutorials & Blogs
- [Introduction to 3D Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting) - Official Tutorial

## 📋 Project Features

### 🛠️ Core Features
- **Configurable Search System**: Customize search keywords through `data/search_config.json` for targeted paper collection
- **Automated Paper Collection**: Daily automatic crawling of latest Gaussian Splatting related papers
- **Intelligent Classification System**: Automatically categorize papers into different topics (Acceleration, Applications, Dynamic Scenes, etc.)
- **Flexible Search Scopes**: Support for abstract-only, title-only, or combined searches
- **Cross-Platform Compatibility**: Support for Windows/Linux/macOS with automatic environment detection

### 🛠️ Technical Features
- **Robust Error Handling**: Multi-layer retry and fallback strategies ensure stable operation
- **GitHub Actions Integration**: Automated CI/CD workflows
- **Real-time Update Mechanism**: Daily automatic paper data updates
- **Detailed Logging**: Comprehensive logging for debugging and monitoring

### 📚 Documentation System
- **User Guides**: Detailed configuration and usage instructions
- **Update Logs**: [News.md](News.md) - Records all important updates
- **Validation Reports**: Automated testing and validation results

## 🚀 Quick Start

### Customize Search Keywords
Edit `data/search_config.json` to target specific research areas:

```json
{
  "search_config": {
    "both_abstract_and_title": [
      "gaussian splatting",
      "3d gaussian",
      "neural rendering"
    ],
    "abstract_only": [
      "volumetric rendering",
      "point cloud reconstruction"
    ],
    "title_only": [
      "real-time rendering",
      "3D reconstruction"
    ]
  }
}
```

### Run the Crawler
```bash
# Basic usage
python scripts/arxiv_crawler.py

# Custom number of papers
python scripts/arxiv_crawler.py --max-results 200

# Validate configuration
python scripts/validate_search_config.py
```

## Contribution Guidelines
Feel free to submit Pull Requests to improve this list! Please follow these formats:
- Paper entry format: `**[Paper Title](link)** - Brief description`
- Project entry format: `[Project Name](link) - Project description`

## License
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) 