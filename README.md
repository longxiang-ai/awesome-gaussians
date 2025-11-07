# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-11-07 00:53:40

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

- [3DGS Surveys](#3dgs-surveys) (1 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (3 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (25 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (7 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (11 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (1 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (9 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (4 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (8 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (6 papers) - Papers focusing on improving rendering quality
- [Relighting](#relighting) (1 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (6 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (9 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: survey, ar, slam, localization, efficient, gaussian splatting, robotics, 3d gaussian, mapping, semantic, high-fidelity  

### Acceleration

- **[4D Neural Voxel Splatting: Dynamic Scene Rendering with Voxelized
  Guassian Splatting](https://arxiv.org/abs/2511.00560v1)**  
  Authors: Chun-Tin Wu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.00560v1.pdf)  
  Keywords: ar, deformation, efficient rendering, compact, real-time rendering, efficient, gaussian splatting, 3d gaussian, fast, 4d, head, dynamic  
- **[SAGS: Self-Adaptive Alias-Free Gaussian Splatting for Dynamic Surgical
  Endoscopic Reconstruction](https://arxiv.org/abs/2510.27318v1)**  
  Authors: Wenfeng Huang, Xiangyun Liao, Yinling Qian, Hao Liu, Yongming Yang, Wenjing Jia, Qiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.27318v1.pdf)  
  Keywords: ar, deformation, gaussian splatting, 3d gaussian, fast, 4d, nerf, dynamic  
- **[Explicit Memory through Online 3D Gaussian Splatting Improves
  Class-Agnostic Video Segmentation](https://arxiv.org/abs/2510.23521v1)**  
  Authors: Anthony Opipari, Aravindhan K Krishnan, Shreekant Gayaka, Min Sun, Cheng-Hao Kuo, Arnie Sen, Odest Chadwicke Jenkins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23521v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://topipari.com/projects/FastSAM-Splat/)  
  Keywords: ar, segmentation, gaussian splatting, 3d gaussian, fast  

### Applications

- **[DentalSplat: Dental Occlusion Novel View Synthesis from Sparse
  Intra-Oral Photographs](https://arxiv.org/abs/2511.03099v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Sihao Li, Ji Jiang, Youpeng Yang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.03099v1.pdf)  
  Keywords: ar, 3d reconstruction, sparse view, gaussian splatting, 3d gaussian  
- **[PercHead: Perceptual Head Model for Single-Image 3D Head Reconstruction
  & Editing](https://arxiv.org/abs/2511.02777v1)**  
  Authors: Antonio Oroz, Matthias Nießner, Tobias Kirschstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.02777v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://antoniooroz.github.io/PercHead)  
  Keywords: ar, geometry, segmentation, gaussian splatting, head, lightweight, semantic  
- **[Object-Centric 3D Gaussian Splatting for Strawberry Plant Reconstruction
  and Phenotyping](https://arxiv.org/abs/2511.02207v1)**  
  Authors: Jiajia Li, Keyi Zhu, Qianwen Zhang, Dong Chen, Qi Sun, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.02207v1.pdf)  
  Keywords: ar, 3d reconstruction, dynamic, gaussian splatting, 3d gaussian, nerf, neural rendering, high-fidelity  
- **[4D Neural Voxel Splatting: Dynamic Scene Rendering with Voxelized
  Guassian Splatting](https://arxiv.org/abs/2511.00560v1)**  
  Authors: Chun-Tin Wu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.00560v1.pdf)  
  Keywords: ar, deformation, efficient rendering, compact, real-time rendering, efficient, gaussian splatting, 3d gaussian, fast, 4d, head, dynamic  
- **[SAGS: Self-Adaptive Alias-Free Gaussian Splatting for Dynamic Surgical
  Endoscopic Reconstruction](https://arxiv.org/abs/2510.27318v1)**  
  Authors: Wenfeng Huang, Xiangyun Liao, Yinling Qian, Hao Liu, Yongming Yang, Wenjing Jia, Qiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.27318v1.pdf)  
  Keywords: ar, deformation, gaussian splatting, 3d gaussian, fast, 4d, nerf, dynamic  
- **[WildfireX-SLAM: A Large-scale Low-altitude RGB-D Dataset for Wildfire
  SLAM and Beyond](https://arxiv.org/abs/2510.27133v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.27133v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhicongsun.github.io/wildfirexslam.)  
  Keywords: ar, slam, localization, gaussian splatting, 3d gaussian, mapping  
- **[DC4GS: Directional Consistency-Driven Adaptive Density Control for 3D
  Gaussian Splatting](https://arxiv.org/abs/2510.26921v1)**  
  Authors: Moonsoo Jeong, Dongbeen Kim, Minseong Kim, Sungkil Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26921v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian  
- **[HEIR: Learning Graph-Based Motion Hierarchies](https://arxiv.org/abs/2510.26786v1)**  
  Authors: Cheng Zheng, William Koch, Baiang Li, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26786v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://light.princeton.edu/HEIR/)  
  Keywords: ar, deformation, motion, gaussian splatting, robotics, 3d gaussian, dynamic  
- **[The Impact and Outlook of 3D Gaussian Splatting](https://arxiv.org/abs/2510.26694v1)**  
  Authors: Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26694v1.pdf)  
  Keywords: ar, efficient, body, gaussian splatting, 3d gaussian, 4d, dynamic  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian
  Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: ar, motion, slam, geometry, understanding, gaussian splatting, outdoor, 3d gaussian, mapping  

### Avatar Generation

- **[PercHead: Perceptual Head Model for Single-Image 3D Head Reconstruction
  & Editing](https://arxiv.org/abs/2511.02777v1)**  
  Authors: Antonio Oroz, Matthias Nießner, Tobias Kirschstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.02777v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://antoniooroz.github.io/PercHead)  
  Keywords: ar, geometry, segmentation, gaussian splatting, head, lightweight, semantic  
- **[4D Neural Voxel Splatting: Dynamic Scene Rendering with Voxelized
  Guassian Splatting](https://arxiv.org/abs/2511.00560v1)**  
  Authors: Chun-Tin Wu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.00560v1.pdf)  
  Keywords: ar, deformation, efficient rendering, compact, real-time rendering, efficient, gaussian splatting, 3d gaussian, fast, 4d, head, dynamic  
- **[The Impact and Outlook of 3D Gaussian Splatting](https://arxiv.org/abs/2510.26694v1)**  
  Authors: Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26694v1.pdf)  
  Keywords: ar, efficient, body, gaussian splatting, 3d gaussian, 4d, dynamic  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit
  Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: ar, 3d reconstruction, gaussian splatting, face, urban scene, semantic  
- **[PlanarGS: High-Fidelity Indoor 3D Gaussian Splatting Guided by
  Vision-Language Planar Priors](https://arxiv.org/abs/2510.23930v1)**  
  Authors: Xirui Jin, Renbiao Jin, Boying Li, Danping Zou, Wenxian Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://planargs.github.io)  
  Keywords: ar, geometry, segmentation, efficient, gaussian splatting, face, 3d gaussian, high-fidelity  
- **[Gen-LangSplat: Generalized Language Gaussian Splatting with Pre-Trained
  Feature Compression](https://arxiv.org/abs/2510.22930v1)**  
  Authors: Pranav Saxena  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22930v1.pdf)  
  Keywords: ar, compact, efficient, gaussian splatting, compression, 3d gaussian, human  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical
  Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/2510.22669v1)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22669v1.pdf)  
  Keywords: ar, high-fidelity, slam, segmentation, outdoor, gaussian splatting, 3d gaussian, mapping, human, dynamic  

### Dynamic Scene

- **[Object-Centric 3D Gaussian Splatting for Strawberry Plant Reconstruction
  and Phenotyping](https://arxiv.org/abs/2511.02207v1)**  
  Authors: Jiajia Li, Keyi Zhu, Qianwen Zhang, Dong Chen, Qi Sun, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.02207v1.pdf)  
  Keywords: ar, 3d reconstruction, dynamic, gaussian splatting, 3d gaussian, nerf, neural rendering, high-fidelity  
- **[4D Neural Voxel Splatting: Dynamic Scene Rendering with Voxelized
  Guassian Splatting](https://arxiv.org/abs/2511.00560v1)**  
  Authors: Chun-Tin Wu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.00560v1.pdf)  
  Keywords: ar, deformation, efficient rendering, compact, real-time rendering, efficient, gaussian splatting, 3d gaussian, fast, 4d, head, dynamic  
- **[SAGS: Self-Adaptive Alias-Free Gaussian Splatting for Dynamic Surgical
  Endoscopic Reconstruction](https://arxiv.org/abs/2510.27318v1)**  
  Authors: Wenfeng Huang, Xiangyun Liao, Yinling Qian, Hao Liu, Yongming Yang, Wenjing Jia, Qiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.27318v1.pdf)  
  Keywords: ar, deformation, gaussian splatting, 3d gaussian, fast, 4d, nerf, dynamic  
- **[HEIR: Learning Graph-Based Motion Hierarchies](https://arxiv.org/abs/2510.26786v1)**  
  Authors: Cheng Zheng, William Koch, Baiang Li, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26786v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://light.princeton.edu/HEIR/)  
  Keywords: ar, deformation, motion, gaussian splatting, robotics, 3d gaussian, dynamic  
- **[The Impact and Outlook of 3D Gaussian Splatting](https://arxiv.org/abs/2510.26694v1)**  
  Authors: Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26694v1.pdf)  
  Keywords: ar, efficient, body, gaussian splatting, 3d gaussian, 4d, dynamic  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian
  Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: ar, motion, slam, geometry, understanding, gaussian splatting, outdoor, 3d gaussian, mapping  
- **[6D Channel Knowledge Map Construction via Bidirectional Wireless
  Gaussian Splatting](https://arxiv.org/abs/2510.26166v1)**  
  Authors: Juncong Zhou, Chao Hu, Guanlin Wu, Zixiang Ren, Han Hu, Juyong Zhang, Rui Zhang, Jie Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26166v1.pdf)  
  Keywords: ar, gaussian splatting, dynamic  
- **[LagMemo: Language 3D Gaussian Splatting Memory for Multi-modal
  Open-vocabulary Multi-goal Visual Navigation](https://arxiv.org/abs/2510.24118v1)**  
  Authors: Haotian Zhou, Xiaole Wang, He Li, Fusheng Sun, Shengyu Guo, Guolei Qi, Jianghuan Xu, Huijing Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.24118v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weekgoodday.github.io/lagmemo)  
  Keywords: ar, localization, gaussian splatting, 3d gaussian, dynamic  
- **[EndoWave: Rational-Wavelet 4D Gaussian Splatting for Endoscopic
  Reconstruction](https://arxiv.org/abs/2510.23087v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Jiaxin Guo, Ziyan Chen, Sihang Zhao, Zhuoxiao Li, Zhe Tang, Baoru Huang, Limin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23087v1.pdf)  
  Keywords: ar, motion, 3d reconstruction, gaussian splatting, 4d, nerf, dynamic  
- **[Scaling Up Occupancy-centric Driving Scene Generation: Dataset and
  Method](https://arxiv.org/abs/2510.22973v1)**  
  Authors: Bohan Li, Xin Jin, Hu Zhu, Hongsi Liu, Ruikai Li, Jiazhe Guo, Kaiwen Cai, Chao Ma, Yueming Jin, Hao Zhao, Xiaokang Yang, Wenjun Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22973v1.pdf)  
  Keywords: ar, high-fidelity, autonomous driving, gaussian splatting, 4d, semantic, dynamic  

### Few-shot

- **[DentalSplat: Dental Occlusion Novel View Synthesis from Sparse
  Intra-Oral Photographs](https://arxiv.org/abs/2511.03099v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Sihao Li, Ji Jiang, Youpeng Yang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.03099v1.pdf)  
  Keywords: ar, 3d reconstruction, sparse view, gaussian splatting, 3d gaussian  

### Geometry Reconstruction

- **[DentalSplat: Dental Occlusion Novel View Synthesis from Sparse
  Intra-Oral Photographs](https://arxiv.org/abs/2511.03099v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Sihao Li, Ji Jiang, Youpeng Yang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.03099v1.pdf)  
  Keywords: ar, 3d reconstruction, sparse view, gaussian splatting, 3d gaussian  
- **[PercHead: Perceptual Head Model for Single-Image 3D Head Reconstruction
  & Editing](https://arxiv.org/abs/2511.02777v1)**  
  Authors: Antonio Oroz, Matthias Nießner, Tobias Kirschstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.02777v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://antoniooroz.github.io/PercHead)  
  Keywords: ar, geometry, segmentation, gaussian splatting, head, lightweight, semantic  
- **[Object-Centric 3D Gaussian Splatting for Strawberry Plant Reconstruction
  and Phenotyping](https://arxiv.org/abs/2511.02207v1)**  
  Authors: Jiajia Li, Keyi Zhu, Qianwen Zhang, Dong Chen, Qi Sun, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.02207v1.pdf)  
  Keywords: ar, 3d reconstruction, dynamic, gaussian splatting, 3d gaussian, nerf, neural rendering, high-fidelity  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian
  Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: ar, motion, slam, geometry, understanding, gaussian splatting, outdoor, 3d gaussian, mapping  
- **[D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene
  Reconstruction](https://arxiv.org/abs/2510.25173v2)**  
  Authors: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25173v2.pdf)  
  Keywords: ar, geometry, autonomous driving, gaussian splatting, urban scene  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit
  Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: ar, 3d reconstruction, gaussian splatting, face, urban scene, semantic  
- **[PlanarGS: High-Fidelity Indoor 3D Gaussian Splatting Guided by
  Vision-Language Planar Priors](https://arxiv.org/abs/2510.23930v1)**  
  Authors: Xirui Jin, Renbiao Jin, Boying Li, Danping Zou, Wenxian Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://planargs.github.io)  
  Keywords: ar, geometry, segmentation, efficient, gaussian splatting, face, 3d gaussian, high-fidelity  
- **[EndoWave: Rational-Wavelet 4D Gaussian Splatting for Endoscopic
  Reconstruction](https://arxiv.org/abs/2510.23087v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Jiaxin Guo, Ziyan Chen, Sihang Zhao, Zhuoxiao Li, Zhe Tang, Baoru Huang, Limin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23087v1.pdf)  
  Keywords: ar, motion, 3d reconstruction, gaussian splatting, 4d, nerf, dynamic  
- **[Region-Adaptive Learned Hierarchical Encoding for 3D Gaussian Splatting
  Data](https://arxiv.org/abs/2510.22812v1)**  
  Authors: Shashank N. Sridhara, Birendra Kathariya, Fangjun Pu, Peng Yin, Eduardo Pavez, Antonio Ortega  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22812v1.pdf)  
  Keywords: ar, geometry, efficient, gaussian splatting, compression, 3d gaussian, lightweight  

### Large Scene

- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian
  Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: ar, motion, slam, geometry, understanding, gaussian splatting, outdoor, 3d gaussian, mapping  
- **[D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene
  Reconstruction](https://arxiv.org/abs/2510.25173v2)**  
  Authors: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25173v2.pdf)  
  Keywords: ar, geometry, autonomous driving, gaussian splatting, urban scene  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit
  Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: ar, 3d reconstruction, gaussian splatting, face, urban scene, semantic  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical
  Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/2510.22669v1)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22669v1.pdf)  
  Keywords: ar, high-fidelity, slam, segmentation, outdoor, gaussian splatting, 3d gaussian, mapping, human, dynamic  

### Model Compression

- **[PercHead: Perceptual Head Model for Single-Image 3D Head Reconstruction
  & Editing](https://arxiv.org/abs/2511.02777v1)**  
  Authors: Antonio Oroz, Matthias Nießner, Tobias Kirschstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.02777v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://antoniooroz.github.io/PercHead)  
  Keywords: ar, geometry, segmentation, gaussian splatting, head, lightweight, semantic  
- **[4D Neural Voxel Splatting: Dynamic Scene Rendering with Voxelized
  Guassian Splatting](https://arxiv.org/abs/2511.00560v1)**  
  Authors: Chun-Tin Wu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.00560v1.pdf)  
  Keywords: ar, deformation, efficient rendering, compact, real-time rendering, efficient, gaussian splatting, 3d gaussian, fast, 4d, head, dynamic  
- **[The Impact and Outlook of 3D Gaussian Splatting](https://arxiv.org/abs/2510.26694v1)**  
  Authors: Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26694v1.pdf)  
  Keywords: ar, efficient, body, gaussian splatting, 3d gaussian, 4d, dynamic  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: survey, ar, slam, localization, efficient, gaussian splatting, robotics, 3d gaussian, mapping, semantic, high-fidelity  
- **[PlanarGS: High-Fidelity Indoor 3D Gaussian Splatting Guided by
  Vision-Language Planar Priors](https://arxiv.org/abs/2510.23930v1)**  
  Authors: Xirui Jin, Renbiao Jin, Boying Li, Danping Zou, Wenxian Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://planargs.github.io)  
  Keywords: ar, geometry, segmentation, efficient, gaussian splatting, face, 3d gaussian, high-fidelity  
- **[Gen-LangSplat: Generalized Language Gaussian Splatting with Pre-Trained
  Feature Compression](https://arxiv.org/abs/2510.22930v1)**  
  Authors: Pranav Saxena  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22930v1.pdf)  
  Keywords: ar, compact, efficient, gaussian splatting, compression, 3d gaussian, human  
- **[Region-Adaptive Learned Hierarchical Encoding for 3D Gaussian Splatting
  Data](https://arxiv.org/abs/2510.22812v1)**  
  Authors: Shashank N. Sridhara, Birendra Kathariya, Fangjun Pu, Peng Yin, Eduardo Pavez, Antonio Ortega  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22812v1.pdf)  
  Keywords: ar, geometry, efficient, gaussian splatting, compression, 3d gaussian, lightweight  
- **[Edge Collaborative Gaussian Splatting with Integrated Rendering and
  Communication](https://arxiv.org/abs/2510.22718v1)**  
  Authors: Yujie Wan, Chenxuan Liu, Shuai Wang, Tong Zhang, James Jianqiao Yu, Kejiang Ye, Dusit Niyato, Chengzhong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22718v1.pdf)  
  Keywords: efficient, gaussian splatting, ar  

### Quality Enhancement

- **[Object-Centric 3D Gaussian Splatting for Strawberry Plant Reconstruction
  and Phenotyping](https://arxiv.org/abs/2511.02207v1)**  
  Authors: Jiajia Li, Keyi Zhu, Qianwen Zhang, Dong Chen, Qi Sun, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.02207v1.pdf)  
  Keywords: ar, 3d reconstruction, dynamic, gaussian splatting, 3d gaussian, nerf, neural rendering, high-fidelity  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: survey, ar, slam, localization, efficient, gaussian splatting, robotics, 3d gaussian, mapping, semantic, high-fidelity  
- **[PlanarGS: High-Fidelity Indoor 3D Gaussian Splatting Guided by
  Vision-Language Planar Priors](https://arxiv.org/abs/2510.23930v1)**  
  Authors: Xirui Jin, Renbiao Jin, Boying Li, Danping Zou, Wenxian Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://planargs.github.io)  
  Keywords: ar, geometry, segmentation, efficient, gaussian splatting, face, 3d gaussian, high-fidelity  
- **[Scaling Up Occupancy-centric Driving Scene Generation: Dataset and
  Method](https://arxiv.org/abs/2510.22973v1)**  
  Authors: Bohan Li, Xin Jin, Hu Zhu, Hongsi Liu, Ruikai Li, Jiazhe Guo, Kaiwen Cai, Chao Ma, Yueming Jin, Hao Zhao, Xiaokang Yang, Wenjun Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22973v1.pdf)  
  Keywords: ar, high-fidelity, autonomous driving, gaussian splatting, 4d, semantic, dynamic  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical
  Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/2510.22669v1)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22669v1.pdf)  
  Keywords: ar, high-fidelity, slam, segmentation, outdoor, gaussian splatting, 3d gaussian, mapping, human, dynamic  
- **[RoGER-SLAM: A Robust Gaussian Splatting SLAM System for Noisy and
  Low-light Environment Resilience](https://arxiv.org/abs/2510.22600v1)**  
  Authors: Huilin Yin, Zhaolin Yang, Linchuan Zhang, Gerhard Rigoll, Johannes Betz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22600v1.pdf)  
  Keywords: ar, slam, tracking, localization, mapping, gaussian splatting, 3d gaussian, illumination, semantic, high-fidelity  

### Relighting

- **[RoGER-SLAM: A Robust Gaussian Splatting SLAM System for Noisy and
  Low-light Environment Resilience](https://arxiv.org/abs/2510.22600v1)**  
  Authors: Huilin Yin, Zhaolin Yang, Linchuan Zhang, Gerhard Rigoll, Johannes Betz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22600v1.pdf)  
  Keywords: ar, slam, tracking, localization, mapping, gaussian splatting, 3d gaussian, illumination, semantic, high-fidelity  

### SLAM

- **[WildfireX-SLAM: A Large-scale Low-altitude RGB-D Dataset for Wildfire
  SLAM and Beyond](https://arxiv.org/abs/2510.27133v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.27133v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhicongsun.github.io/wildfirexslam.)  
  Keywords: ar, slam, localization, gaussian splatting, 3d gaussian, mapping  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian
  Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: ar, motion, slam, geometry, understanding, gaussian splatting, outdoor, 3d gaussian, mapping  
- **[LagMemo: Language 3D Gaussian Splatting Memory for Multi-modal
  Open-vocabulary Multi-goal Visual Navigation](https://arxiv.org/abs/2510.24118v1)**  
  Authors: Haotian Zhou, Xiaole Wang, He Li, Fusheng Sun, Shengyu Guo, Guolei Qi, Jianghuan Xu, Huijing Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.24118v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weekgoodday.github.io/lagmemo)  
  Keywords: ar, localization, gaussian splatting, 3d gaussian, dynamic  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: survey, ar, slam, localization, efficient, gaussian splatting, robotics, 3d gaussian, mapping, semantic, high-fidelity  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical
  Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/2510.22669v1)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22669v1.pdf)  
  Keywords: ar, high-fidelity, slam, segmentation, outdoor, gaussian splatting, 3d gaussian, mapping, human, dynamic  
- **[RoGER-SLAM: A Robust Gaussian Splatting SLAM System for Noisy and
  Low-light Environment Resilience](https://arxiv.org/abs/2510.22600v1)**  
  Authors: Huilin Yin, Zhaolin Yang, Linchuan Zhang, Gerhard Rigoll, Johannes Betz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22600v1.pdf)  
  Keywords: ar, slam, tracking, localization, mapping, gaussian splatting, 3d gaussian, illumination, semantic, high-fidelity  

### Scene Understanding

- **[PercHead: Perceptual Head Model for Single-Image 3D Head Reconstruction
  & Editing](https://arxiv.org/abs/2511.02777v1)**  
  Authors: Antonio Oroz, Matthias Nießner, Tobias Kirschstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.02777v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://antoniooroz.github.io/PercHead)  
  Keywords: ar, geometry, segmentation, gaussian splatting, head, lightweight, semantic  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian
  Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: ar, motion, slam, geometry, understanding, gaussian splatting, outdoor, 3d gaussian, mapping  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit
  Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: ar, 3d reconstruction, gaussian splatting, face, urban scene, semantic  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: survey, ar, slam, localization, efficient, gaussian splatting, robotics, 3d gaussian, mapping, semantic, high-fidelity  
- **[PlanarGS: High-Fidelity Indoor 3D Gaussian Splatting Guided by
  Vision-Language Planar Priors](https://arxiv.org/abs/2510.23930v1)**  
  Authors: Xirui Jin, Renbiao Jin, Boying Li, Danping Zou, Wenxian Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://planargs.github.io)  
  Keywords: ar, geometry, segmentation, efficient, gaussian splatting, face, 3d gaussian, high-fidelity  
- **[Explicit Memory through Online 3D Gaussian Splatting Improves
  Class-Agnostic Video Segmentation](https://arxiv.org/abs/2510.23521v1)**  
  Authors: Anthony Opipari, Aravindhan K Krishnan, Shreekant Gayaka, Min Sun, Cheng-Hao Kuo, Arnie Sen, Odest Chadwicke Jenkins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23521v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://topipari.com/projects/FastSAM-Splat/)  
  Keywords: ar, segmentation, gaussian splatting, 3d gaussian, fast  
- **[Scaling Up Occupancy-centric Driving Scene Generation: Dataset and
  Method](https://arxiv.org/abs/2510.22973v1)**  
  Authors: Bohan Li, Xin Jin, Hu Zhu, Hongsi Liu, Ruikai Li, Jiazhe Guo, Kaiwen Cai, Chao Ma, Yueming Jin, Hao Zhao, Xiaokang Yang, Wenjun Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22973v1.pdf)  
  Keywords: ar, high-fidelity, autonomous driving, gaussian splatting, 4d, semantic, dynamic  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical
  Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/2510.22669v1)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22669v1.pdf)  
  Keywords: ar, high-fidelity, slam, segmentation, outdoor, gaussian splatting, 3d gaussian, mapping, human, dynamic  
- **[RoGER-SLAM: A Robust Gaussian Splatting SLAM System for Noisy and
  Low-light Environment Resilience](https://arxiv.org/abs/2510.22600v1)**  
  Authors: Huilin Yin, Zhaolin Yang, Linchuan Zhang, Gerhard Rigoll, Johannes Betz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22600v1.pdf)  
  Keywords: ar, slam, tracking, localization, mapping, gaussian splatting, 3d gaussian, illumination, semantic, high-fidelity  



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