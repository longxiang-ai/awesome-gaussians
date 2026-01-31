# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-01-31 01:05:35

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

- [3DGS Surveys](#3dgs-surveys) (23 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (241 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (345 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (395 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (82 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (360 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (69 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (417 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (208 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (18 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (125 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (153 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (217 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v2)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v2.pdf)  
  Keywords: survey, gaussian splatting, ar, efficient, 3d gaussian, geometry, nerf  
- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197v1)**  
  Authors: Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07197v1.pdf)  
  Keywords: survey, high-fidelity, compact, dynamic, gaussian splatting, 4d, ar, efficient, 3d gaussian, 3d reconstruction, compression  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v2)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v2.pdf)  
  Keywords: survey, slam, robotics, semantic, gaussian splatting, ar, localization, mapping, understanding, 3d gaussian, nerf  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: survey, high-fidelity, slam, robotics, semantic, gaussian splatting, ar, efficient, localization, mapping, 3d gaussian  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: survey, motion, gaussian splatting, 4d, ar, fast, 3d gaussian, geometry, nerf  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: survey, lighting, animation, gaussian splatting, ar, efficient, real-time rendering, efficient rendering, face, 3d gaussian, 3d reconstruction, avatar  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: survey, human, gaussian splatting, ar, efficient, lightweight, understanding, nerf  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: survey, slam, neural rendering, gaussian splatting, ar, efficient, understanding, fast, 3d gaussian, nerf  
- **[A-TDOM: Active TDOM via On-the-Fly 3DGS](https://arxiv.org/abs/2509.12759v3)**  
  Authors: Yiwei Xu, Xiang Wang, Yifei Yu, Wentian Gan, Luca Morelli, Giulio Perda, Xin Wang, Zongqian Zhan, Fabio Remondino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.12759v3.pdf)  
  Keywords: survey, ar, gaussian splatting, face, 3d gaussian  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977v3)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v3.pdf)  
  Keywords: survey, lighting, high-fidelity, compact, semantic, gaussian splatting, ar, efficient, segmentation, understanding, 3d gaussian, nerf  

### Acceleration

*Showing the latest 50 out of 241 papers*

- **[PLANING: A Loosely Coupled Triangle-Gaussian Framework for Streaming 3D Reconstruction](https://arxiv.org/abs/2601.22046v1)**  
  Authors: Changjian Jiang, Kerui Ren, Xudong Li, Kaiwen Song, Linning Xu, Tao Lu, Junting Dong, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22046v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://city-super.github.io/PLANING/)  
  Keywords: gaussian splatting, ar, efficient, fast, geometry, 3d reconstruction  
- **[GRTX: Efficient Ray Tracing for 3D Gaussian-Based Rendering](https://arxiv.org/abs/2601.20429v1)**  
  Authors: Junseo Lee, Sangyun Jeon, Jungi Lee, Junyong Park, Jaewoong Sim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20429v1.pdf)  
  Keywords: acceleration, gaussian splatting, ar, efficient, head, ray tracing, 3d gaussian  
- **[WaterClear-GS: Optical-Aware Gaussian Splatting for Underwater Reconstruction and Restoration](https://arxiv.org/abs/2601.19753v1)**  
  Authors: Xinrui Zhang, Yufeng Wang, Shuangkang Fang, Zesheng Wang, Dacheng Qi, Wenrui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19753v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://buaaxrzhang.github.io/WaterClear-GS/.)  
  Keywords: gaussian splatting, ar, nerf, real-time rendering, 3d gaussian, geometry, 3d reconstruction  
- **[Advancing Structured Priors for Sparse-Voxel Surface Reconstruction](https://arxiv.org/abs/2601.17720v1)**  
  Authors: Ting-Hsun Chi, Chu-Rong Chen, Chi-Tun Hsu, Hsuan-Ting Lin, Sheng-Yu Huang, Cheng Sun, Yu-Chiang Frank Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17720v1.pdf)  
  Keywords: gaussian splatting, ar, face, 3d gaussian, geometry, fast  
- **[SplatBus: A Gaussian Splatting Viewer Framework via GPU Interprocess Communication](https://arxiv.org/abs/2601.15431v1)**  
  Authors: Yinghan Xu, Théo Morales, John Dingliana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15431v1.pdf)  
  Keywords: lighting, high-fidelity, robotics, autonomous driving, gaussian splatting, ar, real-time rendering, 3d gaussian  
- **[POTR: Post-Training 3DGS Compression](https://arxiv.org/abs/2601.14821v1)**  
  Authors: Bert Ramlot, Martijn Courteaux, Peter Lambert, Glenn Van Wallendael  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.14821v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, efficient, fast, 3d gaussian, nerf, compression  
- **[Structured Image-based Coding for Efficient Gaussian Splatting Compression](https://arxiv.org/abs/2601.14510v2)**  
  Authors: Pedro Martin, Antonio Rodrigues, Joao Ascenso, Maria Paula Queluz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.14510v2.pdf)  
  Keywords: gaussian splatting, ar, efficient, real-time rendering, mapping, nerf, compression  
- **[CSGaussian: Progressive Rate-Distortion Compression and Segmentation for 3D Gaussian Splatting](https://arxiv.org/abs/2601.12814v1)**  
  Authors: Yu-Jen Tseng, Chia-Hao Kao, Jing-Zhong Chen, Alessandro Gnutti, Shao-Yuan Lo, Yen-Yu Lin, Wen-Hsiao Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12814v1.pdf)  
  Keywords: semantic, gaussian splatting, ar, efficient, real-time rendering, lightweight, segmentation, understanding, 3d gaussian, compression  
- **[GaussianFluent: Gaussian Simulation for Dynamic Scenes with Mixed Materials](https://arxiv.org/abs/2601.09265v1)**  
  Authors: Bei Huang, Yixin Chen, Ruijie Lu, Gang Zeng, Hongbin Zha, Yuru Pei, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.09265v1.pdf)  
  Keywords: lighting, high-fidelity, robotics, dynamic, gaussian splatting, ar, real-time rendering, vr, 3d gaussian  
- **[MOSAIC-GS: Monocular Scene Reconstruction via Advanced Initialization for Complex Dynamic Environments](https://arxiv.org/abs/2601.05368v1)**  
  Authors: Svitlana Morkva, Maximum Wilder-Smith, Michael Oechsle, Alessio Tonioni, Marco Hutter, Vaishakh Patil  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05368v1.pdf)  
  Keywords: tracking, compact, motion, dynamic, deformation, gaussian splatting, ar, efficient, real-time rendering, segmentation, high-fidelity, geometry, fast  

### Applications

*Showing the latest 50 out of 995 papers*

- **[PLANING: A Loosely Coupled Triangle-Gaussian Framework for Streaming 3D Reconstruction](https://arxiv.org/abs/2601.22046v1)**  
  Authors: Changjian Jiang, Kerui Ren, Xudong Li, Kaiwen Song, Linning Xu, Tao Lu, Junting Dong, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22046v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://city-super.github.io/PLANING/)  
  Keywords: gaussian splatting, ar, efficient, fast, geometry, 3d reconstruction  
- **[Hybrid Foveated Path Tracing with Peripheral Gaussians for Immersive Anatomy](https://arxiv.org/abs/2601.22026v1)**  
  Authors: Constantin Kleinbeck, Luisa Theelke, Hannah Schieber, Ulrich Eck, Rüdiger von Eisenhart-Rothe, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22026v1.pdf)  
  Keywords: medical, path tracing, gaussian splatting, ar, head, lightweight, vr, understanding  
- **[FreeFix: Boosting 3D Gaussian Splatting via Fine-Tuning-Free Diffusion Models](https://arxiv.org/abs/2601.20857v1)**  
  Authors: Hongyu Zhou, Zisen Shao, Sheng Miao, Pan Wang, Dongfeng Bai, Bingbing Liu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20857v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, face  
- **[GRTX: Efficient Ray Tracing for 3D Gaussian-Based Rendering](https://arxiv.org/abs/2601.20429v1)**  
  Authors: Junseo Lee, Sangyun Jeon, Jungi Lee, Junyong Park, Jaewoong Sim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20429v1.pdf)  
  Keywords: acceleration, gaussian splatting, ar, efficient, head, ray tracing, 3d gaussian  
- **[GVGS: Gaussian Visibility-Aware Multi-View Geometry for Accurate Surface Reconstruction](https://arxiv.org/abs/2601.20331v1)**  
  Authors: Mai Su, Qihan Yu, Zhongtao Wang, Yilong Li, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20331v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, face, 3d gaussian, geometry  
- **[Graphical X Splatting (GraphiXS): A Graphical Model for 4D Gaussian Splatting under Uncertainty](https://arxiv.org/abs/2601.19843v1)**  
  Authors: Doga Yilmaz, Jialin Zhu, Deshan Gong, He Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19843v1.pdf)  
  Keywords: ar, neural rendering, gaussian splatting, 4d  
- **[WaterClear-GS: Optical-Aware Gaussian Splatting for Underwater Reconstruction and Restoration](https://arxiv.org/abs/2601.19753v1)**  
  Authors: Xinrui Zhang, Yufeng Wang, Shuangkang Fang, Zesheng Wang, Dacheng Qi, Wenrui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19753v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://buaaxrzhang.github.io/WaterClear-GS/.)  
  Keywords: gaussian splatting, ar, nerf, real-time rendering, 3d gaussian, geometry, 3d reconstruction  
- **[ClipGS-VR: Immersive and Interactive Cinematic Visualization of Volumetric Medical Data in Mobile Virtual Reality](https://arxiv.org/abs/2601.19310v1)**  
  Authors: Yuqi Tong, Ruiyang Li, Chengkun Li, Qixuan Liu, Shi Qiu, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19310v1.pdf)  
  Keywords: medical, high-fidelity, gaussian splatting, ar, head, vr, 3d gaussian  
- **[TIGaussian: Disentangle Gaussians for Spatial-Awared Text-Image-3D Alignment](https://arxiv.org/abs/2601.19247v1)**  
  Authors: Jiarun Liu, Qifeng Chen, Yiru Zhao, Minghua Liu, Baorui Ma, Sheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19247v1.pdf)  
  Keywords: compact, ar, gaussian splatting, 3d gaussian, recognition  
- **[UniMGS: Unifying Mesh and 3D Gaussian Splatting with Single-Pass Rasterization and Proxy-Based Deformation](https://arxiv.org/abs/2601.19233v1)**  
  Authors: Zeyu Xiao, Mingyang Sun, Yimin Cong, Lintao Wang, Dongliang Kou, Zhenyi Wu, Dingkang Yang, Peng Zhai, Zeyu Wang, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19233v1.pdf)  
  Keywords: deformation, ar, gaussian splatting, face, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 345 papers*

- **[Hybrid Foveated Path Tracing with Peripheral Gaussians for Immersive Anatomy](https://arxiv.org/abs/2601.22026v1)**  
  Authors: Constantin Kleinbeck, Luisa Theelke, Hannah Schieber, Ulrich Eck, Rüdiger von Eisenhart-Rothe, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22026v1.pdf)  
  Keywords: medical, path tracing, gaussian splatting, ar, head, lightweight, vr, understanding  
- **[FreeFix: Boosting 3D Gaussian Splatting via Fine-Tuning-Free Diffusion Models](https://arxiv.org/abs/2601.20857v1)**  
  Authors: Hongyu Zhou, Zisen Shao, Sheng Miao, Pan Wang, Dongfeng Bai, Bingbing Liu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20857v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, face  
- **[GRTX: Efficient Ray Tracing for 3D Gaussian-Based Rendering](https://arxiv.org/abs/2601.20429v1)**  
  Authors: Junseo Lee, Sangyun Jeon, Jungi Lee, Junyong Park, Jaewoong Sim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20429v1.pdf)  
  Keywords: acceleration, gaussian splatting, ar, efficient, head, ray tracing, 3d gaussian  
- **[GVGS: Gaussian Visibility-Aware Multi-View Geometry for Accurate Surface Reconstruction](https://arxiv.org/abs/2601.20331v1)**  
  Authors: Mai Su, Qihan Yu, Zhongtao Wang, Yilong Li, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20331v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, face, 3d gaussian, geometry  
- **[ClipGS-VR: Immersive and Interactive Cinematic Visualization of Volumetric Medical Data in Mobile Virtual Reality](https://arxiv.org/abs/2601.19310v1)**  
  Authors: Yuqi Tong, Ruiyang Li, Chengkun Li, Qixuan Liu, Shi Qiu, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19310v1.pdf)  
  Keywords: medical, high-fidelity, gaussian splatting, ar, head, vr, 3d gaussian  
- **[UniMGS: Unifying Mesh and 3D Gaussian Splatting with Single-Pass Rasterization and Proxy-Based Deformation](https://arxiv.org/abs/2601.19233v1)**  
  Authors: Zeyu Xiao, Mingyang Sun, Yimin Cong, Lintao Wang, Dongliang Kou, Zhenyi Wu, Dingkang Yang, Peng Zhai, Zeyu Wang, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19233v1.pdf)  
  Keywords: deformation, ar, gaussian splatting, face, 3d gaussian  
- **[Splat-Portrait: Generalizing Talking Heads with Gaussian Splatting](https://arxiv.org/abs/2601.18633v1)**  
  Authors: Tong Shi, Melonie de Almeida, Daniela Ivanova, Nicolas Pugeault, Paul Henderson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18633v1.pdf)  
  Keywords: animation, motion, gaussian splatting, ar, head, 3d reconstruction, avatar  
- **[ExoGS: A 4D Real-to-Sim-to-Real Framework for Scalable Manipulation Data Collection](https://arxiv.org/abs/2601.18629v1)**  
  Authors: Yiming Wang, Ruogu Zhang, Minyang Li, Hao Shi, Junbo Wang, Deyi Li, Jieji Ren, Wenhai Liu, Weiming Wang, Hao-Shu Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18629v1.pdf)  
  Keywords: human, dynamic, semantic, gaussian splatting, 4d, ar, efficient, lightweight, 3d gaussian, geometry  
- **[Advancing Structured Priors for Sparse-Voxel Surface Reconstruction](https://arxiv.org/abs/2601.17720v1)**  
  Authors: Ting-Hsun Chi, Chu-Rong Chen, Chi-Tun Hsu, Hsuan-Ting Lin, Sheng-Yu Huang, Cheng Sun, Yu-Chiang Frank Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17720v1.pdf)  
  Keywords: gaussian splatting, ar, face, 3d gaussian, geometry, fast  
- **[PocketGS: On-Device Training of 3D Gaussian Splatting for High Perceptual Modeling](https://arxiv.org/abs/2601.17354v2)**  
  Authors: Wenzhi Guo, Guangchi Fang, Shu Yang, Bing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17354v2.pdf)  
  Keywords: high-fidelity, compact, gaussian splatting, ar, efficient, face, 3d gaussian, geometry  

### Dynamic Scene

*Showing the latest 50 out of 395 papers*

- **[Graphical X Splatting (GraphiXS): A Graphical Model for 4D Gaussian Splatting under Uncertainty](https://arxiv.org/abs/2601.19843v1)**  
  Authors: Doga Yilmaz, Jialin Zhu, Deshan Gong, He Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19843v1.pdf)  
  Keywords: ar, neural rendering, gaussian splatting, 4d  
- **[UniMGS: Unifying Mesh and 3D Gaussian Splatting with Single-Pass Rasterization and Proxy-Based Deformation](https://arxiv.org/abs/2601.19233v1)**  
  Authors: Zeyu Xiao, Mingyang Sun, Yimin Cong, Lintao Wang, Dongliang Kou, Zhenyi Wu, Dingkang Yang, Peng Zhai, Zeyu Wang, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19233v1.pdf)  
  Keywords: deformation, ar, gaussian splatting, face, 3d gaussian  
- **[Splat-Portrait: Generalizing Talking Heads with Gaussian Splatting](https://arxiv.org/abs/2601.18633v1)**  
  Authors: Tong Shi, Melonie de Almeida, Daniela Ivanova, Nicolas Pugeault, Paul Henderson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18633v1.pdf)  
  Keywords: animation, motion, gaussian splatting, ar, head, 3d reconstruction, avatar  
- **[ExoGS: A 4D Real-to-Sim-to-Real Framework for Scalable Manipulation Data Collection](https://arxiv.org/abs/2601.18629v1)**  
  Authors: Yiming Wang, Ruogu Zhang, Minyang Li, Hao Shi, Junbo Wang, Deyi Li, Jieji Ren, Wenhai Liu, Weiming Wang, Hao-Shu Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18629v1.pdf)  
  Keywords: human, dynamic, semantic, gaussian splatting, 4d, ar, efficient, lightweight, 3d gaussian, geometry  
- **[LoD-Structured 3D Gaussian Splatting for Streaming Video Reconstruction](https://arxiv.org/abs/2601.18475v1)**  
  Authors: Xinhui Liu, Can Wang, Lei Liu, Zhenghao Chen, Wei Jiang, Wei Wang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18475v1.pdf)  
  Keywords: high-fidelity, motion, dynamic, gaussian splatting, ar, efficient, 3d gaussian, sparse-view  
- **[EVolSplat4D: Efficient Volume-based Gaussian Splatting for 4D Urban Scene Synthesis](https://arxiv.org/abs/2601.15951v1)**  
  Authors: Sheng Miao, Sijin Li, Pan Wang, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15951v1.pdf)  
  Keywords: motion, dynamic, autonomous driving, semantic, gaussian splatting, 4d, ar, efficient, 3d gaussian, geometry, urban scene  
- **[ThermoSplat: Cross-Modal 3D Gaussian Splatting with Feature Modulation and Geometry Decoupling](https://arxiv.org/abs/2601.15897v1)**  
  Authors: Zhaoqi Su, Shihai Chen, Xinyan Lin, Liqin Huang, Zhipeng Su, Xiaoqiang Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15897v1.pdf)  
  Keywords: lighting, dynamic, semantic, gaussian splatting, ar, 3d gaussian, geometry  
- **[LL-GaussianImage: Efficient Image Representation for Zero-shot Low-Light Enhancement with 2D Gaussian Splatting](https://arxiv.org/abs/2601.15772v1)**  
  Authors: Yuhan Chen, Wenxuan Yu, Guofa Li, Yijun Xu, Ying Fang, Yicui Shi, Long Cao, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15772v1.pdf)  
  Keywords: dynamic, semantic, gaussian splatting, ar, efficient, quality enhancement, compression  
- **[Rig-Aware 3D Reconstruction of Vehicle Undercarriages using Gaussian Splatting](https://arxiv.org/abs/2601.14208v1)**  
  Authors: Nitin Kulkarni, Akhil Devarashetti, Charlie Cluss, Livio Forte, Dan Buckmaster, Philip Schneider, Chunming Qiao, Alina Vereshchaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.14208v1.pdf)  
  Keywords: motion, ar, gaussian splatting, 3d reconstruction  
- **[ParkingTwin: Training-Free Streaming 3D Reconstruction for Parking-Lot Digital Twins](https://arxiv.org/abs/2601.13706v1)**  
  Authors: Xinhao Liu, Yu Wang, Xiansheng Guo, Gordon Owusu Boateng, Yu Cao, Haonan Si, Xingchen Guo, Nirwan Ansari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.13706v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mihoutao-liu.github.io/ParkingTwin/)  
  Keywords: lighting, high-fidelity, illumination, neural rendering, dynamic, semantic, gaussian splatting, ar, lightweight, mapping, face, 3d gaussian, geometry, 3d reconstruction  

### Few-shot

*Showing the latest 50 out of 82 papers*

- **[LoD-Structured 3D Gaussian Splatting for Streaming Video Reconstruction](https://arxiv.org/abs/2601.18475v1)**  
  Authors: Xinhui Liu, Can Wang, Lei Liu, Zhenghao Chen, Wei Jiang, Wei Wang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18475v1.pdf)  
  Keywords: high-fidelity, motion, dynamic, gaussian splatting, ar, efficient, 3d gaussian, sparse-view  
- **[LGDWT-GS: Local and Global Discrete Wavelet-Regularized 3D Gaussian Splatting for Sparse-View Scene Reconstruction](https://arxiv.org/abs/2601.17185v1)**  
  Authors: Shima Salehi, Atharva Agashe, Andrew J. McFarland, Joshua Peeples  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17185v1.pdf)  
  Keywords: gaussian splatting, sparse-view, ar, few-shot, 3d gaussian, geometry, 3d reconstruction  
- **[SA-ResGS: Self-Augmented Residual 3D Gaussian Splatting for Next Best View Selection](https://arxiv.org/abs/2601.03024v2)**  
  Authors: Kim Jun-Seong, Tae-Hyun Oh, Eduardo Pérez-Pellitero, Youngkyoon Jang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03024v2.pdf)  
  Keywords: ar, gaussian splatting, efficient, 3d gaussian, sparse-view  
- **[360-GeoGS: Geometrically Consistent Feed-Forward 3D Gaussian Splatting Reconstruction for 360 Images](https://arxiv.org/abs/2601.02102v1)**  
  Authors: Jiaqi Yao, Zhongmiao Yan, Jingyi Xu, Songpengcheng Xia, Yan Xiang, Ling Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02102v1.pdf)  
  Keywords: robotics, neural rendering, sparse view, gaussian splatting, ar, efficient, efficient rendering, face, 3d gaussian, 3d reconstruction  
- **[ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2601.00939v1)**  
  Authors: Feng Luo, Hongbo Pan, Xiang Yang, Baoyu Jiang, Fengqing Liu, Tao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00939v1.pdf)  
  Keywords: shadow, illumination, gaussian splatting, sparse-view, ar, efficient, efficient rendering, 3d gaussian, ray marching, 3d reconstruction  
- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v2)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: high-fidelity, motion, sparse view, gaussian splatting, ar, 3d gaussian, 3d reconstruction  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: lighting, gaussian splatting, ar, segmentation, light transport, relighting, geometry, sparse-view  
- **[Splatent: Splatting Diffusion Latents for Novel View Synthesis](https://arxiv.org/abs/2512.09923v1)**  
  Authors: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09923v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, efficient rendering, face, 3d gaussian, 3d reconstruction, sparse-view  
- **[Tessellation GS: Neural Mesh Gaussians for Robust Monocular Reconstruction of Dynamic Objects](https://arxiv.org/abs/2512.07381v1)**  
  Authors: Shuohan Tao, Boyao Zhou, Hanzhang Tu, Yuwang Wang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07381v1.pdf)  
  Keywords: dynamic, deformation, gaussian splatting, ar, face, 3d gaussian, sparse-view  
- **[MuSASplat: Efficient Sparse-View 3D Gaussian Splats via Lightweight Multi-Scale Adaptation](https://arxiv.org/abs/2512.07165v1)**  
  Authors: Muyu Xu, Fangneng Zhan, Xiaoqin Zhang, Ling Shao, Shijian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07165v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, lightweight, head, 3d gaussian, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 360 papers*

- **[PLANING: A Loosely Coupled Triangle-Gaussian Framework for Streaming 3D Reconstruction](https://arxiv.org/abs/2601.22046v1)**  
  Authors: Changjian Jiang, Kerui Ren, Xudong Li, Kaiwen Song, Linning Xu, Tao Lu, Junting Dong, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22046v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://city-super.github.io/PLANING/)  
  Keywords: gaussian splatting, ar, efficient, fast, geometry, 3d reconstruction  
- **[GVGS: Gaussian Visibility-Aware Multi-View Geometry for Accurate Surface Reconstruction](https://arxiv.org/abs/2601.20331v1)**  
  Authors: Mai Su, Qihan Yu, Zhongtao Wang, Yilong Li, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20331v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, face, 3d gaussian, geometry  
- **[WaterClear-GS: Optical-Aware Gaussian Splatting for Underwater Reconstruction and Restoration](https://arxiv.org/abs/2601.19753v1)**  
  Authors: Xinrui Zhang, Yufeng Wang, Shuangkang Fang, Zesheng Wang, Dacheng Qi, Wenrui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19753v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://buaaxrzhang.github.io/WaterClear-GS/.)  
  Keywords: gaussian splatting, ar, nerf, real-time rendering, 3d gaussian, geometry, 3d reconstruction  
- **[Bridging Visual and Wireless Sensing: A Unified Radiation Field for 3D Radio Map Construction](https://arxiv.org/abs/2601.19216v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Zehong Lin, Chenghong Bian, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19216v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, understanding, 3d gaussian, geometry, nerf  
- **[Splat-Portrait: Generalizing Talking Heads with Gaussian Splatting](https://arxiv.org/abs/2601.18633v1)**  
  Authors: Tong Shi, Melonie de Almeida, Daniela Ivanova, Nicolas Pugeault, Paul Henderson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18633v1.pdf)  
  Keywords: animation, motion, gaussian splatting, ar, head, 3d reconstruction, avatar  
- **[ExoGS: A 4D Real-to-Sim-to-Real Framework for Scalable Manipulation Data Collection](https://arxiv.org/abs/2601.18629v1)**  
  Authors: Yiming Wang, Ruogu Zhang, Minyang Li, Hao Shi, Junbo Wang, Deyi Li, Jieji Ren, Wenhai Liu, Weiming Wang, Hao-Shu Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18629v1.pdf)  
  Keywords: human, dynamic, semantic, gaussian splatting, 4d, ar, efficient, lightweight, 3d gaussian, geometry  
- **[Geometry-Grounded Gaussian Splatting](https://arxiv.org/abs/2601.17835v2)**  
  Authors: Baowen Zhang, Chenxing Jiang, Heng Li, Shaojie Shen, Ping Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17835v2.pdf)  
  Keywords: ar, gaussian splatting, efficient, shape reconstruction, geometry  
- **[Advancing Structured Priors for Sparse-Voxel Surface Reconstruction](https://arxiv.org/abs/2601.17720v1)**  
  Authors: Ting-Hsun Chi, Chu-Rong Chen, Chi-Tun Hsu, Hsuan-Ting Lin, Sheng-Yu Huang, Cheng Sun, Yu-Chiang Frank Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17720v1.pdf)  
  Keywords: gaussian splatting, ar, face, 3d gaussian, geometry, fast  
- **[PocketGS: On-Device Training of 3D Gaussian Splatting for High Perceptual Modeling](https://arxiv.org/abs/2601.17354v2)**  
  Authors: Wenzhi Guo, Guangchi Fang, Shu Yang, Bing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17354v2.pdf)  
  Keywords: high-fidelity, compact, gaussian splatting, ar, efficient, face, 3d gaussian, geometry  
- **[LGDWT-GS: Local and Global Discrete Wavelet-Regularized 3D Gaussian Splatting for Sparse-View Scene Reconstruction](https://arxiv.org/abs/2601.17185v1)**  
  Authors: Shima Salehi, Atharva Agashe, Andrew J. McFarland, Joshua Peeples  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17185v1.pdf)  
  Keywords: gaussian splatting, sparse-view, ar, few-shot, 3d gaussian, geometry, 3d reconstruction  

### Large Scene

*Showing the latest 50 out of 69 papers*

- **[EVolSplat4D: Efficient Volume-based Gaussian Splatting for 4D Urban Scene Synthesis](https://arxiv.org/abs/2601.15951v1)**  
  Authors: Sheng Miao, Sijin Li, Pan Wang, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15951v1.pdf)  
  Keywords: motion, dynamic, autonomous driving, semantic, gaussian splatting, 4d, ar, efficient, 3d gaussian, geometry, urban scene  
- **[Clean-GS: Semantic Mask-Guided Pruning for 3D Gaussian Splatting](https://arxiv.org/abs/2601.00913v1)**  
  Authors: Subhankar Mishra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00913v1.pdf)  
  Keywords: outdoor, semantic, gaussian splatting, ar, segmentation, vr, 3d gaussian, compression  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: illumination, gaussian splatting, ar, efficient, face, 3d gaussian, geometry, 3d reconstruction, urban scene  
- **[Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries](https://arxiv.org/abs/2512.13796v1)**  
  Authors: Victor Rong, Jan Held, Victor Chu, Daniel Rebain, Marc Van Droogenbroeck, Kiriakos N. Kutulakos, Andrea Tagliasacchi, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13796v1.pdf)  
  Keywords: compact, outdoor, gaussian splatting, ar, 3d gaussian, geometry, fast  
- **[Flux4D: Flow-based Unsupervised 4D Reconstruction](https://arxiv.org/abs/2512.03210v1)**  
  Authors: Jingkang Wang, Henry Che, Yun Chen, Ze Yang, Lily Goli, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03210v1.pdf)  
  Keywords: robotics, motion, dynamic, outdoor, gaussian splatting, 4d, ar, efficient, 3d gaussian, nerf  
- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: outdoor, gaussian splatting, ar, understanding, 3d gaussian, geometry, 3d reconstruction  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: outdoor, semantic, gaussian splatting, ar, geometry, fast  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: lighting, illumination, outdoor, semantic, gaussian splatting, ar, efficient, segmentation, relighting, face, high-fidelity, geometry  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: high-fidelity, outdoor, gaussian splatting, ar, 3d gaussian, geometry  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: human, dynamic, autonomous driving, gaussian splatting, 4d, ar, urban scene  

### Model Compression

*Showing the latest 50 out of 417 papers*

- **[PLANING: A Loosely Coupled Triangle-Gaussian Framework for Streaming 3D Reconstruction](https://arxiv.org/abs/2601.22046v1)**  
  Authors: Changjian Jiang, Kerui Ren, Xudong Li, Kaiwen Song, Linning Xu, Tao Lu, Junting Dong, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22046v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://city-super.github.io/PLANING/)  
  Keywords: gaussian splatting, ar, efficient, fast, geometry, 3d reconstruction  
- **[Hybrid Foveated Path Tracing with Peripheral Gaussians for Immersive Anatomy](https://arxiv.org/abs/2601.22026v1)**  
  Authors: Constantin Kleinbeck, Luisa Theelke, Hannah Schieber, Ulrich Eck, Rüdiger von Eisenhart-Rothe, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22026v1.pdf)  
  Keywords: medical, path tracing, gaussian splatting, ar, head, lightweight, vr, understanding  
- **[GRTX: Efficient Ray Tracing for 3D Gaussian-Based Rendering](https://arxiv.org/abs/2601.20429v1)**  
  Authors: Junseo Lee, Sangyun Jeon, Jungi Lee, Junyong Park, Jaewoong Sim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20429v1.pdf)  
  Keywords: acceleration, gaussian splatting, ar, efficient, head, ray tracing, 3d gaussian  
- **[GVGS: Gaussian Visibility-Aware Multi-View Geometry for Accurate Surface Reconstruction](https://arxiv.org/abs/2601.20331v1)**  
  Authors: Mai Su, Qihan Yu, Zhongtao Wang, Yilong Li, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20331v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, face, 3d gaussian, geometry  
- **[TIGaussian: Disentangle Gaussians for Spatial-Awared Text-Image-3D Alignment](https://arxiv.org/abs/2601.19247v1)**  
  Authors: Jiarun Liu, Qifeng Chen, Yiru Zhao, Minghua Liu, Baorui Ma, Sheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19247v1.pdf)  
  Keywords: compact, ar, gaussian splatting, 3d gaussian, recognition  
- **[ExoGS: A 4D Real-to-Sim-to-Real Framework for Scalable Manipulation Data Collection](https://arxiv.org/abs/2601.18629v1)**  
  Authors: Yiming Wang, Ruogu Zhang, Minyang Li, Hao Shi, Junbo Wang, Deyi Li, Jieji Ren, Wenhai Liu, Weiming Wang, Hao-Shu Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18629v1.pdf)  
  Keywords: human, dynamic, semantic, gaussian splatting, 4d, ar, efficient, lightweight, 3d gaussian, geometry  
- **[LoD-Structured 3D Gaussian Splatting for Streaming Video Reconstruction](https://arxiv.org/abs/2601.18475v1)**  
  Authors: Xinhui Liu, Can Wang, Lei Liu, Zhenghao Chen, Wei Jiang, Wei Wang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18475v1.pdf)  
  Keywords: high-fidelity, motion, dynamic, gaussian splatting, ar, efficient, 3d gaussian, sparse-view  
- **[Geometry-Grounded Gaussian Splatting](https://arxiv.org/abs/2601.17835v2)**  
  Authors: Baowen Zhang, Chenxing Jiang, Heng Li, Shaojie Shen, Ping Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17835v2.pdf)  
  Keywords: ar, gaussian splatting, efficient, shape reconstruction, geometry  
- **[PocketGS: On-Device Training of 3D Gaussian Splatting for High Perceptual Modeling](https://arxiv.org/abs/2601.17354v2)**  
  Authors: Wenzhi Guo, Guangchi Fang, Shu Yang, Bing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17354v2.pdf)  
  Keywords: high-fidelity, compact, gaussian splatting, ar, efficient, face, 3d gaussian, geometry  
- **[EVolSplat4D: Efficient Volume-based Gaussian Splatting for 4D Urban Scene Synthesis](https://arxiv.org/abs/2601.15951v1)**  
  Authors: Sheng Miao, Sijin Li, Pan Wang, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15951v1.pdf)  
  Keywords: motion, dynamic, autonomous driving, semantic, gaussian splatting, 4d, ar, efficient, 3d gaussian, geometry, urban scene  

### Quality Enhancement

*Showing the latest 50 out of 208 papers*

- **[ClipGS-VR: Immersive and Interactive Cinematic Visualization of Volumetric Medical Data in Mobile Virtual Reality](https://arxiv.org/abs/2601.19310v1)**  
  Authors: Yuqi Tong, Ruiyang Li, Chengkun Li, Qixuan Liu, Shi Qiu, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19310v1.pdf)  
  Keywords: medical, high-fidelity, gaussian splatting, ar, head, vr, 3d gaussian  
- **[Bridging Visual and Wireless Sensing: A Unified Radiation Field for 3D Radio Map Construction](https://arxiv.org/abs/2601.19216v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Zehong Lin, Chenghong Bian, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19216v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, understanding, 3d gaussian, geometry, nerf  
- **[LoD-Structured 3D Gaussian Splatting for Streaming Video Reconstruction](https://arxiv.org/abs/2601.18475v1)**  
  Authors: Xinhui Liu, Can Wang, Lei Liu, Zhenghao Chen, Wei Jiang, Wei Wang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18475v1.pdf)  
  Keywords: high-fidelity, motion, dynamic, gaussian splatting, ar, efficient, 3d gaussian, sparse-view  
- **[PocketGS: On-Device Training of 3D Gaussian Splatting for High Perceptual Modeling](https://arxiv.org/abs/2601.17354v2)**  
  Authors: Wenzhi Guo, Guangchi Fang, Shu Yang, Bing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17354v2.pdf)  
  Keywords: high-fidelity, compact, gaussian splatting, ar, efficient, face, 3d gaussian, geometry  
- **[ReWeaver: Towards Simulation-Ready and Topology-Accurate Garment Reconstruction](https://arxiv.org/abs/2601.16672v1)**  
  Authors: Ming Li, Hui Shan, Kai Zheng, Chentao Shen, Siyu Liu, Yanwei Fu, Zhen Chen, Xiangru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16672v1.pdf)  
  Keywords: human, body, high-fidelity, ar, 3d gaussian, geometry, avatar  
- **[LL-GaussianImage: Efficient Image Representation for Zero-shot Low-Light Enhancement with 2D Gaussian Splatting](https://arxiv.org/abs/2601.15772v1)**  
  Authors: Yuhan Chen, Wenxuan Yu, Guofa Li, Yijun Xu, Ying Fang, Yicui Shi, Long Cao, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15772v1.pdf)  
  Keywords: dynamic, semantic, gaussian splatting, ar, efficient, quality enhancement, compression  
- **[LL-GaussianMap: Zero-shot Low-Light Image Enhancement via 2D Gaussian Splatting Guided Gain Maps](https://arxiv.org/abs/2601.15766v2)**  
  Authors: Yuhan Chen, Ying Fang, Guofa Li, Wenxuan Yu, Yicui Shi, Jingrui Zhang, Kefei Qian, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15766v2.pdf)  
  Keywords: lighting, ar, gaussian splatting, efficient, high-fidelity  
- **[SplatBus: A Gaussian Splatting Viewer Framework via GPU Interprocess Communication](https://arxiv.org/abs/2601.15431v1)**  
  Authors: Yinghan Xu, Théo Morales, John Dingliana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15431v1.pdf)  
  Keywords: lighting, high-fidelity, robotics, autonomous driving, gaussian splatting, ar, real-time rendering, 3d gaussian  
- **[One-Shot Refiner: Boosting Feed-forward Novel View Synthesis via One-Step Diffusion](https://arxiv.org/abs/2601.14161v1)**  
  Authors: Yitong Dong, Qi Zhang, Minchao Jiang, Zhiqiang Wu, Qingnan Fan, Ying Feng, Huaqi Zhang, Hujun Bao, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.14161v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, gaussian splatting  
- **[ParkingTwin: Training-Free Streaming 3D Reconstruction for Parking-Lot Digital Twins](https://arxiv.org/abs/2601.13706v1)**  
  Authors: Xinhao Liu, Yu Wang, Xiansheng Guo, Gordon Owusu Boateng, Yu Cao, Haonan Si, Xingchen Guo, Nirwan Ansari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.13706v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mihoutao-liu.github.io/ParkingTwin/)  
  Keywords: lighting, high-fidelity, illumination, neural rendering, dynamic, semantic, gaussian splatting, ar, lightweight, mapping, face, 3d gaussian, geometry, 3d reconstruction  

### Ray Tracing

- **[Hybrid Foveated Path Tracing with Peripheral Gaussians for Immersive Anatomy](https://arxiv.org/abs/2601.22026v1)**  
  Authors: Constantin Kleinbeck, Luisa Theelke, Hannah Schieber, Ulrich Eck, Rüdiger von Eisenhart-Rothe, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22026v1.pdf)  
  Keywords: medical, path tracing, gaussian splatting, ar, head, lightweight, vr, understanding  
- **[GRTX: Efficient Ray Tracing for 3D Gaussian-Based Rendering](https://arxiv.org/abs/2601.20429v1)**  
  Authors: Junseo Lee, Sangyun Jeon, Jungi Lee, Junyong Park, Jaewoong Sim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20429v1.pdf)  
  Keywords: acceleration, gaussian splatting, ar, efficient, head, ray tracing, 3d gaussian  
- **[ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2601.00939v1)**  
  Authors: Feng Luo, Hongbo Pan, Xiang Yang, Baoyu Jiang, Fengqing Liu, Tao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00939v1.pdf)  
  Keywords: shadow, illumination, gaussian splatting, sparse-view, ar, efficient, efficient rendering, 3d gaussian, ray marching, 3d reconstruction  
- **[Geometric-Photometric Event-based 3D Gaussian Ray Tracing](https://arxiv.org/abs/2512.18640v1)**  
  Authors: Kai Kohyama, Yoshimitsu Aoki, Guillermo Gallego, Shintaro Shiba  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18640v1.pdf)  
  Keywords: motion, gaussian splatting, ar, ray tracing, understanding, fast, 3d gaussian, geometry, 3d reconstruction  
- **[MatSpray: Fusing 2D Material World Knowledge on 3D Geometry](https://arxiv.org/abs/2512.18314v1)**  
  Authors: Philipp Langsteiner, Jan-Niklas Dihlmann, Hendrik P. A. Lensch  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18314v1.pdf)  
  Keywords: lighting, relightable, gaussian splatting, ar, relighting, ray tracing, geometry, 3d reconstruction  
- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: gaussian splatting, ar, ray tracing, face, fast, 3d gaussian, nerf  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: high-fidelity, compact, gaussian splatting, ar, real-time rendering, ray tracing, 3d gaussian, fast  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, reflection, ray tracing, high-fidelity, geometry, 3d reconstruction  
- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: illumination, gaussian splatting, ar, reflection, ray tracing, geometry  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: gaussian splatting, ar, efficient, 3d gaussian, ray marching, geometry  

### Relighting

*Showing the latest 50 out of 125 papers*

- **[ThermoSplat: Cross-Modal 3D Gaussian Splatting with Feature Modulation and Geometry Decoupling](https://arxiv.org/abs/2601.15897v1)**  
  Authors: Zhaoqi Su, Shihai Chen, Xinyan Lin, Liqin Huang, Zhipeng Su, Xiaoqiang Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15897v1.pdf)  
  Keywords: lighting, dynamic, semantic, gaussian splatting, ar, 3d gaussian, geometry  
- **[LL-GaussianMap: Zero-shot Low-Light Image Enhancement via 2D Gaussian Splatting Guided Gain Maps](https://arxiv.org/abs/2601.15766v2)**  
  Authors: Yuhan Chen, Ying Fang, Guofa Li, Wenxuan Yu, Yicui Shi, Jingrui Zhang, Kefei Qian, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15766v2.pdf)  
  Keywords: lighting, ar, gaussian splatting, efficient, high-fidelity  
- **[SplatBus: A Gaussian Splatting Viewer Framework via GPU Interprocess Communication](https://arxiv.org/abs/2601.15431v1)**  
  Authors: Yinghan Xu, Théo Morales, John Dingliana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15431v1.pdf)  
  Keywords: lighting, high-fidelity, robotics, autonomous driving, gaussian splatting, ar, real-time rendering, 3d gaussian  
- **[LuxRemix: Lighting Decomposition and Remixing for Indoor Scenes](https://arxiv.org/abs/2601.15283v1)**  
  Authors: Ruofan Liang, Norman Müller, Ethan Weber, Duncan Zauss, Nandita Vijaykumar, Peter Kontschieder, Christian Richardt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15283v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://luxremix.github.io.)  
  Keywords: lighting, illumination, relightable, gaussian splatting, ar, relighting, 3d gaussian  
- **[POTR: Post-Training 3DGS Compression](https://arxiv.org/abs/2601.14821v1)**  
  Authors: Bert Ramlot, Martijn Courteaux, Peter Lambert, Glenn Van Wallendael  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.14821v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, efficient, fast, 3d gaussian, nerf, compression  
- **[ParkingTwin: Training-Free Streaming 3D Reconstruction for Parking-Lot Digital Twins](https://arxiv.org/abs/2601.13706v1)**  
  Authors: Xinhao Liu, Yu Wang, Xiansheng Guo, Gordon Owusu Boateng, Yu Cao, Haonan Si, Xingchen Guo, Nirwan Ansari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.13706v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mihoutao-liu.github.io/ParkingTwin/)  
  Keywords: lighting, high-fidelity, illumination, neural rendering, dynamic, semantic, gaussian splatting, ar, lightweight, mapping, face, 3d gaussian, geometry, 3d reconstruction  
- **[Active Semantic Mapping of Horticultural Environments Using Gaussian Splatting](https://arxiv.org/abs/2601.12122v1)**  
  Authors: Jose Cuaran, Naveen K. Upalapati, Girish Chowdhary  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12122v1.pdf)  
  Keywords: lighting, high-fidelity, robotics, semantic, gaussian splatting, ar, efficient, segmentation, mapping, 3d gaussian, 3d reconstruction  
- **[studentSplat: Your Student Model Learns Single-view 3D Gaussian Splatting](https://arxiv.org/abs/2601.11772v1)**  
  Authors: Yimu Pan, Hongda Mao, Qingshuang Chen, Yelin Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.11772v1.pdf)  
  Keywords: lighting, ar, gaussian splatting, understanding, 3d gaussian  
- **[GaussianFluent: Gaussian Simulation for Dynamic Scenes with Mixed Materials](https://arxiv.org/abs/2601.09265v1)**  
  Authors: Bei Huang, Yixin Chen, Ruijie Lu, Gang Zeng, Hongbin Zha, Yuru Pei, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.09265v1.pdf)  
  Keywords: lighting, high-fidelity, robotics, dynamic, gaussian splatting, ar, real-time rendering, vr, 3d gaussian  
- **[RelightAnyone: A Generalized Relightable 3D Gaussian Head Model](https://arxiv.org/abs/2601.03357v1)**  
  Authors: Yingyan Xu, Pramod Rao, Sebastian Weiss, Gaspard Zoss, Markus Gross, Christian Theobalt, Marc Habermann, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03357v1.pdf)  
  Keywords: lighting, illumination, relightable, gaussian splatting, ar, head, high quality, mapping, relighting, 3d gaussian, avatar  

### SLAM

*Showing the latest 50 out of 153 papers*

- **[Structured Image-based Coding for Efficient Gaussian Splatting Compression](https://arxiv.org/abs/2601.14510v2)**  
  Authors: Pedro Martin, Antonio Rodrigues, Joao Ascenso, Maria Paula Queluz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.14510v2.pdf)  
  Keywords: gaussian splatting, ar, efficient, real-time rendering, mapping, nerf, compression  
- **[ParkingTwin: Training-Free Streaming 3D Reconstruction for Parking-Lot Digital Twins](https://arxiv.org/abs/2601.13706v1)**  
  Authors: Xinhao Liu, Yu Wang, Xiansheng Guo, Gordon Owusu Boateng, Yu Cao, Haonan Si, Xingchen Guo, Nirwan Ansari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.13706v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mihoutao-liu.github.io/ParkingTwin/)  
  Keywords: lighting, high-fidelity, illumination, neural rendering, dynamic, semantic, gaussian splatting, ar, lightweight, mapping, face, 3d gaussian, geometry, 3d reconstruction  
- **[Active Semantic Mapping of Horticultural Environments Using Gaussian Splatting](https://arxiv.org/abs/2601.12122v1)**  
  Authors: Jose Cuaran, Naveen K. Upalapati, Girish Chowdhary  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12122v1.pdf)  
  Keywords: lighting, high-fidelity, robotics, semantic, gaussian splatting, ar, efficient, segmentation, mapping, 3d gaussian, 3d reconstruction  
- **[Variable Basis Mapping for Real-Time Volumetric Visualization](https://arxiv.org/abs/2601.09417v1)**  
  Authors: Qibiao Li, Yuxuan Wang, Youcheng Cai, Huangsheng Du, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.09417v1.pdf)  
  Keywords: compact, gaussian splatting, ar, efficient, lightweight, mapping, 3d gaussian  
- **[FeatureSLAM: Feature-enriched 3D gaussian splatting SLAM in real time](https://arxiv.org/abs/2601.05738v1)**  
  Authors: Christopher Thirgood, Oscar Mendez, Erin Ling, Jon Storey, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05738v1.pdf)  
  Keywords: tracking, slam, semantic, gaussian splatting, ar, efficient, segmentation, mapping, 3d gaussian  
- **[MOSAIC-GS: Monocular Scene Reconstruction via Advanced Initialization for Complex Dynamic Environments](https://arxiv.org/abs/2601.05368v1)**  
  Authors: Svitlana Morkva, Maximum Wilder-Smith, Michael Oechsle, Alessio Tonioni, Marco Hutter, Vaishakh Patil  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05368v1.pdf)  
  Keywords: tracking, compact, motion, dynamic, deformation, gaussian splatting, ar, efficient, real-time rendering, segmentation, high-fidelity, geometry, fast  
- **[G2P: Gaussian-to-Point Attribute Alignment for Boundary-Aware 3D Semantic Segmentation](https://arxiv.org/abs/2601.03510v1)**  
  Authors: Hojun Song, Chae-yeong Song, Jeong-hun Hong, Chaewon Moon, Dong-hwi Kim, Gahyeon Kim, Soo Ye Kim, Yiyi Liao, Jaehyup Lee, Sang-hyo Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03510v1.pdf)  
  Keywords: semantic, gaussian splatting, ar, localization, segmentation, understanding, 3d gaussian, geometry  
- **[RelightAnyone: A Generalized Relightable 3D Gaussian Head Model](https://arxiv.org/abs/2601.03357v1)**  
  Authors: Yingyan Xu, Pramod Rao, Sebastian Weiss, Gaspard Zoss, Markus Gross, Christian Theobalt, Marc Habermann, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03357v1.pdf)  
  Keywords: lighting, illumination, relightable, gaussian splatting, ar, head, high quality, mapping, relighting, 3d gaussian, avatar  
- **[InpaintHuman: Reconstructing Occluded Humans with Multi-Scale UV Mapping and Identity-Preserving Diffusion Inpainting](https://arxiv.org/abs/2601.02098v1)**  
  Authors: Jinlong Fan, Shanshan Zhao, Liang Zheng, Jing Zhang, Yuxiang Yang, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02098v1.pdf)  
  Keywords: human, high-fidelity, motion, semantic, gaussian splatting, ar, mapping, 3d gaussian, geometry, avatar  
- **[Animated 3DGS Avatars in Diverse Scenes with Consistent Lighting and Shadows](https://arxiv.org/abs/2601.01660v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Jian Wang, Gerard Pons-Moll, Bing Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.01660v1.pdf)  
  Keywords: lighting, shadow, illumination, dynamic, gaussian splatting, ar, mapping, relighting, 3d gaussian, fast, avatar  

### Scene Understanding

*Showing the latest 50 out of 217 papers*

- **[Hybrid Foveated Path Tracing with Peripheral Gaussians for Immersive Anatomy](https://arxiv.org/abs/2601.22026v1)**  
  Authors: Constantin Kleinbeck, Luisa Theelke, Hannah Schieber, Ulrich Eck, Rüdiger von Eisenhart-Rothe, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22026v1.pdf)  
  Keywords: medical, path tracing, gaussian splatting, ar, head, lightweight, vr, understanding  
- **[TIGaussian: Disentangle Gaussians for Spatial-Awared Text-Image-3D Alignment](https://arxiv.org/abs/2601.19247v1)**  
  Authors: Jiarun Liu, Qifeng Chen, Yiru Zhao, Minghua Liu, Baorui Ma, Sheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19247v1.pdf)  
  Keywords: compact, ar, gaussian splatting, 3d gaussian, recognition  
- **[Bridging Visual and Wireless Sensing: A Unified Radiation Field for 3D Radio Map Construction](https://arxiv.org/abs/2601.19216v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Zehong Lin, Chenghong Bian, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19216v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, understanding, 3d gaussian, geometry, nerf  
- **[ExoGS: A 4D Real-to-Sim-to-Real Framework for Scalable Manipulation Data Collection](https://arxiv.org/abs/2601.18629v1)**  
  Authors: Yiming Wang, Ruogu Zhang, Minyang Li, Hao Shi, Junbo Wang, Deyi Li, Jieji Ren, Wenhai Liu, Weiming Wang, Hao-Shu Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18629v1.pdf)  
  Keywords: human, dynamic, semantic, gaussian splatting, 4d, ar, efficient, lightweight, 3d gaussian, geometry  
- **[A Step to Decouple Optimization in 3DGS](https://arxiv.org/abs/2601.16736v2)**  
  Authors: Renjie Ding, Yaonan Wang, Min Liu, Jialin Zhu, Jiazheng Wang, Jiahao Zhao, Wenting Shen, Feixiang He, Xiang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16736v2.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, understanding  
- **[EVolSplat4D: Efficient Volume-based Gaussian Splatting for 4D Urban Scene Synthesis](https://arxiv.org/abs/2601.15951v1)**  
  Authors: Sheng Miao, Sijin Li, Pan Wang, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15951v1.pdf)  
  Keywords: motion, dynamic, autonomous driving, semantic, gaussian splatting, 4d, ar, efficient, 3d gaussian, geometry, urban scene  
- **[ThermoSplat: Cross-Modal 3D Gaussian Splatting with Feature Modulation and Geometry Decoupling](https://arxiv.org/abs/2601.15897v1)**  
  Authors: Zhaoqi Su, Shihai Chen, Xinyan Lin, Liqin Huang, Zhipeng Su, Xiaoqiang Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15897v1.pdf)  
  Keywords: lighting, dynamic, semantic, gaussian splatting, ar, 3d gaussian, geometry  
- **[LL-GaussianImage: Efficient Image Representation for Zero-shot Low-Light Enhancement with 2D Gaussian Splatting](https://arxiv.org/abs/2601.15772v1)**  
  Authors: Yuhan Chen, Wenxuan Yu, Guofa Li, Yijun Xu, Ying Fang, Yicui Shi, Long Cao, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15772v1.pdf)  
  Keywords: dynamic, semantic, gaussian splatting, ar, efficient, quality enhancement, compression  
- **[ParkingTwin: Training-Free Streaming 3D Reconstruction for Parking-Lot Digital Twins](https://arxiv.org/abs/2601.13706v1)**  
  Authors: Xinhao Liu, Yu Wang, Xiansheng Guo, Gordon Owusu Boateng, Yu Cao, Haonan Si, Xingchen Guo, Nirwan Ansari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.13706v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mihoutao-liu.github.io/ParkingTwin/)  
  Keywords: lighting, high-fidelity, illumination, neural rendering, dynamic, semantic, gaussian splatting, ar, lightweight, mapping, face, 3d gaussian, geometry, 3d reconstruction  
- **[CSGaussian: Progressive Rate-Distortion Compression and Segmentation for 3D Gaussian Splatting](https://arxiv.org/abs/2601.12814v1)**  
  Authors: Yu-Jen Tseng, Chia-Hao Kao, Jing-Zhong Chen, Alessandro Gnutti, Shao-Yuan Lo, Yen-Yu Lin, Wen-Hsiao Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12814v1.pdf)  
  Keywords: semantic, gaussian splatting, ar, efficient, real-time rendering, lightweight, segmentation, understanding, 3d gaussian, compression  



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