# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-12-04 00:55:31

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

- [3DGS Surveys](#3dgs-surveys) (22 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (252 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (339 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (397 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (80 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (339 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (76 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (406 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (188 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (14 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (118 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (143 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (203 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: high-fidelity, gaussian splatting, mapping, efficient, localization, ar, survey, slam, semantic, robotics, 3d gaussian  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: gaussian splatting, fast, ar, survey, 4d, motion, geometry, nerf, 3d gaussian  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: 3d reconstruction, animation, gaussian splatting, efficient, face, ar, survey, lighting, efficient rendering, real-time rendering, avatar, 3d gaussian  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: gaussian splatting, human, efficient, ar, survey, understanding, lightweight, nerf  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: gaussian splatting, fast, efficient, ar, survey, understanding, slam, nerf, neural rendering, 3d gaussian  
- **[A-TDOM: Active TDOM via On-the-Fly 3DGS](https://arxiv.org/abs/2509.12759v2)**  
  Authors: Yiwei Xu, Xiang Wang, Yifei Yu, Wentian Gan, Luca Morelli, Giulio Perda, Xiongwu Xiao, Zongqian Zhan, Xin Wang, Fabio Remondino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.12759v2.pdf)  
  Keywords: ar, face, survey  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: high-fidelity, gaussian splatting, segmentation, ar, survey, understanding, lighting, semantic, compact, nerf, 3d gaussian  
- **[A Study of the Framework and Real-World Applications of Language Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: gaussian splatting, efficient, ar, survey, understanding, semantic, robotics, nerf, 3d gaussian  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: gaussian splatting, human, ar, survey, robotics, nerf, 3d gaussian  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, ar, survey, sparse-view, vr, robotics, motion, geometry, nerf, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 252 papers*

- **[EGGS: Exchangeable 2D/3D Gaussian Splatting for Geometry-Appearance Balanced Novel View Synthesis](https://arxiv.org/abs/2512.02932v1)**  
  Authors: Yancheng Zhang, Guangyu Sun, Chen Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02932v1.pdf)  
  Keywords: dynamic, gaussian splatting, autonomous driving, efficient, ar, vr, geometry, real-time rendering, 3d gaussian  
- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: reflection, high-fidelity, gaussian splatting, efficient, face, ar, efficient rendering, geometry, real-time rendering, nerf, 3d gaussian  
- **[Content-Aware Texturing for Gaussian Splatting](https://arxiv.org/abs/2512.02621v1)**  
  Authors: Panagiotis Papantonakis, Georgios Kopanas, Fredo Durand, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02621v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gs-texturing/)  
  Keywords: 3d reconstruction, gaussian splatting, mapping, ar, geometry, real-time rendering  
- **[G-SHARP: Gaussian Surgical Hardware Accelerated Real-time Pipeline](https://arxiv.org/abs/2512.02482v1)**  
  Authors: Vishwesh Nath, Javier G. Tejero, Ruilong Li, Filippo Filicori, Mahdi Azizian, Sean D. Huver  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02482v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, fast, ar, deformation, nerf  
- **[Asset-Driven Sematic Reconstruction of Dynamic Scene with Multi-Human-Object Interactions](https://arxiv.org/abs/2512.00547v1)**  
  Authors: Sandika Biswas, Qianyi Wu, Biplab Banerjee, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00547v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, human, mapping, fast, ar, face, semantic, deformation, vr, motion, geometry, 3d gaussian  
- **[SplatFont3D: Structure-Aware Text-to-3D Artistic Font Generation with Part-Level Style Control](https://arxiv.org/abs/2512.00413v1)**  
  Authors: Ji Gan, Lingxu Chen, Jiaxu Leng, Xinbo Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00413v1.pdf)  
  Keywords: dynamic, gaussian splatting, animation, human, fast, ar, semantic, nerf, 3d gaussian  
- **[DiskChunGS: Large-Scale 3D Gaussian SLAM Through Chunk-Based Memory Management](https://arxiv.org/abs/2511.23030v1)**  
  Authors: Casimir Feldmann, Maximum Wilder-Smith, Vaishakh Patil, Michael Oechsle, Michael Niemeyer, Keisuke Tateno, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23030v1.pdf)  
  Keywords: gaussian splatting, ar, face, slam, real-time rendering, 3d gaussian  
- **[DenoiseGS: Gaussian Reconstruction Model for Burst Denoising](https://arxiv.org/abs/2511.22939v2)**  
  Authors: Yongsen Cheng, Yuanhao Cai, Yulun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22939v2.pdf)  
  Keywords: gaussian splatting, fast, ar, motion, geometry, nerf, 3d gaussian  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: gaussian splatting, fast, ar, semantic, geometry, outdoor  
- **[Alias-free 4D Gaussian Splatting](https://arxiv.org/abs/2511.18367v1)**  
  Authors: Zilong Chen, Huan-ang Gao, Delin Qu, Haohan Chi, Hao Tang, Kai Zhang, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18367v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4d-alias-free.github.io/4D-Alias-free/)  
  Keywords: dynamic, gaussian splatting, ar, 4d, real-time rendering  

### Applications

*Showing the latest 50 out of 995 papers*

- **[EGGS: Exchangeable 2D/3D Gaussian Splatting for Geometry-Appearance Balanced Novel View Synthesis](https://arxiv.org/abs/2512.02932v1)**  
  Authors: Yancheng Zhang, Guangyu Sun, Chen Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02932v1.pdf)  
  Keywords: dynamic, gaussian splatting, autonomous driving, efficient, ar, vr, geometry, real-time rendering, 3d gaussian  
- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: reflection, high-fidelity, gaussian splatting, efficient, face, ar, efficient rendering, geometry, real-time rendering, nerf, 3d gaussian  
- **[PoreTrack3D: A Benchmark for Dynamic 3D Gaussian Splatting in Pore-Scale Facial Trajectory Tracking](https://arxiv.org/abs/2512.02648v1)**  
  Authors: Dong Li, Jiahao Xiong, Yingda Huang, Le Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02648v1.pdf)  
  Keywords: 3d reconstruction, tracking, dynamic, high-fidelity, gaussian splatting, ar, face, motion, 3d gaussian  
- **[Content-Aware Texturing for Gaussian Splatting](https://arxiv.org/abs/2512.02621v1)**  
  Authors: Panagiotis Papantonakis, Georgios Kopanas, Fredo Durand, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02621v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gs-texturing/)  
  Keywords: 3d reconstruction, gaussian splatting, mapping, ar, geometry, real-time rendering  
- **[G-SHARP: Gaussian Surgical Hardware Accelerated Real-time Pipeline](https://arxiv.org/abs/2512.02482v1)**  
  Authors: Vishwesh Nath, Javier G. Tejero, Ruilong Li, Filippo Filicori, Mahdi Azizian, Sean D. Huver  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02482v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, fast, ar, deformation, nerf  
- **[VIGS-SLAM: Visual Inertial Gaussian Splatting SLAM](https://arxiv.org/abs/2512.02293v1)**  
  Authors: Zihan Zhu, Wei Zhang, Norbert Haala, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02293v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vigs-slam.github.io)  
  Keywords: tracking, high-fidelity, gaussian splatting, mapping, ar, slam, motion, 3d gaussian  
- **[SplatSuRe: Selective Super-Resolution for Multi-view Consistent 3D Gaussian Splatting](https://arxiv.org/abs/2512.02172v1)**  
  Authors: Pranav Asthana, Alex Hanson, Allen Tu, Tom Goldstein, Matthias Zwicker, Amitabh Varshney  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02172v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, nerf, 3d gaussian  
- **[ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation](https://arxiv.org/abs/2512.02013v1)**  
  Authors: Chenyang Gu, Jiaming Liu, Hao Chen, Runzhong Huang, Qingpo Wuwu, Zhuoyang Liu, Xiaoqi Li, Ying Li, Renrui Zhang, Peng Jia, Pheng-Ann Heng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02013v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, face, understanding, 3d gaussian  
- **[TagSplat: Topology-Aware Gaussian Splatting for Dynamic Mesh Modeling and Tracking](https://arxiv.org/abs/2512.01329v1)**  
  Authors: Hanzhi Guo, Dongdong Weng, Mo Su, Yixiao Chen, Xiaonuo Dongye, Chenyu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01329v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haza628.github.io/tagSplat/)  
  Keywords: tracking, dynamic, gaussian splatting, animation, ar, face, 4d  
- **[EGG-Fusion: Efficient 3D Reconstruction with Geometry-aware Gaussian Surfel on the Fly](https://arxiv.org/abs/2512.01296v1)**  
  Authors: Xiaokun Pan, Zhenzhe Li, Zhichao Ye, Hongjia Zhai, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/eggfusion/)  
  Keywords: 3d reconstruction, tracking, gaussian splatting, mapping, efficient, face, ar, slam, geometry, nerf, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 339 papers*

- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: reflection, high-fidelity, gaussian splatting, efficient, face, ar, efficient rendering, geometry, real-time rendering, nerf, 3d gaussian  
- **[PoreTrack3D: A Benchmark for Dynamic 3D Gaussian Splatting in Pore-Scale Facial Trajectory Tracking](https://arxiv.org/abs/2512.02648v1)**  
  Authors: Dong Li, Jiahao Xiong, Yingda Huang, Le Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02648v1.pdf)  
  Keywords: 3d reconstruction, tracking, dynamic, high-fidelity, gaussian splatting, ar, face, motion, 3d gaussian  
- **[ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation](https://arxiv.org/abs/2512.02013v1)**  
  Authors: Chenyang Gu, Jiaming Liu, Hao Chen, Runzhong Huang, Qingpo Wuwu, Zhuoyang Liu, Xiaoqi Li, Ying Li, Renrui Zhang, Peng Jia, Pheng-Ann Heng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02013v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, face, understanding, 3d gaussian  
- **[TagSplat: Topology-Aware Gaussian Splatting for Dynamic Mesh Modeling and Tracking](https://arxiv.org/abs/2512.01329v1)**  
  Authors: Hanzhi Guo, Dongdong Weng, Mo Su, Yixiao Chen, Xiaonuo Dongye, Chenyu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01329v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haza628.github.io/tagSplat/)  
  Keywords: tracking, dynamic, gaussian splatting, animation, ar, face, 4d  
- **[EGG-Fusion: Efficient 3D Reconstruction with Geometry-aware Gaussian Surfel on the Fly](https://arxiv.org/abs/2512.01296v1)**  
  Authors: Xiaokun Pan, Zhenzhe Li, Zhichao Ye, Hongjia Zhai, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/eggfusion/)  
  Keywords: 3d reconstruction, tracking, gaussian splatting, mapping, efficient, face, ar, slam, geometry, nerf, 3d gaussian  
- **[Binary-Gaussian: Compact and Progressive Representation for 3D Gaussian Segmentation](https://arxiv.org/abs/2512.00944v1)**  
  Authors: An Yang, Chenyu Liu, Jun Du, Jianqing Gao, Jia Pan, Jinshui Hu, Baocai Yin, Bing Yin, Cong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00944v1.pdf)  
  Keywords: gaussian splatting, mapping, efficient, segmentation, ar, head, semantic, compact, 3d gaussian  
- **[PolarGS: Polarimetric Cues for Ambiguity-Free Gaussian Splatting with Accurate Geometry Recovery](https://arxiv.org/abs/2512.00794v1)**  
  Authors: Bo Guo, Sijia Wen, Yifan Zhao, Jia Li, Zhiming Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00794v1.pdf)  
  Keywords: gaussian splatting, ar, face, geometry, 3d gaussian  
- **[Asset-Driven Sematic Reconstruction of Dynamic Scene with Multi-Human-Object Interactions](https://arxiv.org/abs/2512.00547v1)**  
  Authors: Sandika Biswas, Qianyi Wu, Biplab Banerjee, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00547v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, human, mapping, fast, ar, face, semantic, deformation, vr, motion, geometry, 3d gaussian  
- **[SplatFont3D: Structure-Aware Text-to-3D Artistic Font Generation with Part-Level Style Control](https://arxiv.org/abs/2512.00413v1)**  
  Authors: Ji Gan, Lingxu Chen, Jiaxu Leng, Xinbo Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00413v1.pdf)  
  Keywords: dynamic, gaussian splatting, animation, human, fast, ar, semantic, nerf, 3d gaussian  
- **[TGSFormer: Scalable Temporal Gaussian Splatting for Embodied Semantic Scene Completion](https://arxiv.org/abs/2512.00300v1)**  
  Authors: Rui Qian, Haozhi Cao, Tianchen Deng, Tianxin Hu, Weixiang Guo, Shenghai Yuan, Lihua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00300v1.pdf)  
  Keywords: gaussian splatting, ar, semantic, head, geometry, compact  

### Dynamic Scene

*Showing the latest 50 out of 397 papers*

- **[EGGS: Exchangeable 2D/3D Gaussian Splatting for Geometry-Appearance Balanced Novel View Synthesis](https://arxiv.org/abs/2512.02932v1)**  
  Authors: Yancheng Zhang, Guangyu Sun, Chen Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02932v1.pdf)  
  Keywords: dynamic, gaussian splatting, autonomous driving, efficient, ar, vr, geometry, real-time rendering, 3d gaussian  
- **[PoreTrack3D: A Benchmark for Dynamic 3D Gaussian Splatting in Pore-Scale Facial Trajectory Tracking](https://arxiv.org/abs/2512.02648v1)**  
  Authors: Dong Li, Jiahao Xiong, Yingda Huang, Le Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02648v1.pdf)  
  Keywords: 3d reconstruction, tracking, dynamic, high-fidelity, gaussian splatting, ar, face, motion, 3d gaussian  
- **[G-SHARP: Gaussian Surgical Hardware Accelerated Real-time Pipeline](https://arxiv.org/abs/2512.02482v1)**  
  Authors: Vishwesh Nath, Javier G. Tejero, Ruilong Li, Filippo Filicori, Mahdi Azizian, Sean D. Huver  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02482v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, fast, ar, deformation, nerf  
- **[VIGS-SLAM: Visual Inertial Gaussian Splatting SLAM](https://arxiv.org/abs/2512.02293v1)**  
  Authors: Zihan Zhu, Wei Zhang, Norbert Haala, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02293v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vigs-slam.github.io)  
  Keywords: tracking, high-fidelity, gaussian splatting, mapping, ar, slam, motion, 3d gaussian  
- **[TagSplat: Topology-Aware Gaussian Splatting for Dynamic Mesh Modeling and Tracking](https://arxiv.org/abs/2512.01329v1)**  
  Authors: Hanzhi Guo, Dongdong Weng, Mo Su, Yixiao Chen, Xiaonuo Dongye, Chenyu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01329v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haza628.github.io/tagSplat/)  
  Keywords: tracking, dynamic, gaussian splatting, animation, ar, face, 4d  
- **[Dynamic-eDiTor: Training-Free Text-Driven 4D Scene Editing with Multimodal Diffusion Transformer](https://arxiv.org/abs/2512.00677v1)**  
  Authors: Dong In Lee, Hyungjun Doh, Seunggeun Chi, Runlin Duan, Sangpil Kim, Karthik Ramani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00677v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://di-lee.github.io/dynamic-eDiTor/)  
  Keywords: dynamic, gaussian splatting, 4d, motion, nerf  
- **[Asset-Driven Sematic Reconstruction of Dynamic Scene with Multi-Human-Object Interactions](https://arxiv.org/abs/2512.00547v1)**  
  Authors: Sandika Biswas, Qianyi Wu, Biplab Banerjee, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00547v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, human, mapping, fast, ar, face, semantic, deformation, vr, motion, geometry, 3d gaussian  
- **[SplatFont3D: Structure-Aware Text-to-3D Artistic Font Generation with Part-Level Style Control](https://arxiv.org/abs/2512.00413v1)**  
  Authors: Ji Gan, Lingxu Chen, Jiaxu Leng, Xinbo Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00413v1.pdf)  
  Keywords: dynamic, gaussian splatting, animation, human, fast, ar, semantic, nerf, 3d gaussian  
- **[Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views](https://arxiv.org/abs/2512.00255v1)**  
  Authors: Kunwar Maheep Singh, Jianchun Chen, Vladislav Golyanik, Stephan J. Garbin, Thabo Beeler, Rishabh Dabral, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/RHC/)  
  Keywords: relightable, tracking, dynamic, sparse view, human, body, relighting, efficient, ar, sparse-view, lighting, illumination, motion, geometry, 3d gaussian  
- **[FACT-GS: Frequency-Aligned Complexity-Aware Texture Reparameterization for 2D Gaussian Splatting](https://arxiv.org/abs/2511.23292v1)**  
  Authors: Tianhao Xie, Linlian Jiang, Xinxin Zuo, Yang Wang, Tiberiu Popa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23292v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, deformation  

### Few-shot

*Showing the latest 50 out of 80 papers*

- **[Cross-Temporal 3D Gaussian Splatting for Sparse-View Guided Scene Update](https://arxiv.org/abs/2512.00534v1)**  
  Authors: Zeyuan An, Yanghang Xiao, Zhiying Leng, Frederick W. B. Li, Xiaohui Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00534v1.pdf)  
  Keywords: gaussian splatting, sparse view, efficient, ar, sparse-view, 3d gaussian  
- **[Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views](https://arxiv.org/abs/2512.00255v1)**  
  Authors: Kunwar Maheep Singh, Jianchun Chen, Vladislav Golyanik, Stephan J. Garbin, Thabo Beeler, Rishabh Dabral, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/RHC/)  
  Keywords: relightable, tracking, dynamic, sparse view, human, body, relighting, efficient, ar, sparse-view, lighting, illumination, motion, geometry, 3d gaussian  
- **[Observer Actor: Active Vision Imitation Learning with Sparse View Gaussian Splatting](https://arxiv.org/abs/2511.18140v1)**  
  Authors: Yilong Wang, Cheng Qian, Ruomeng Fan, Edward Johns  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18140v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://obact.github.io.)  
  Keywords: dynamic, gaussian splatting, sparse view, ar, 3d gaussian  
- **[Frequency-Adaptive Sharpness Regularization for Improving 3D Gaussian Splatting Generalization](https://arxiv.org/abs/2511.17918v1)**  
  Authors: Youngsik Yun, Dongjun Gu, Youngjung Uh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bbangsik13.github.io/FASR.)  
  Keywords: few-shot, ar, gaussian splatting, 3d gaussian  
- **[SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting](https://arxiv.org/abs/2511.17092v2)**  
  Authors: Di Wu, Liu Liu, Xueyu Yuan, Qiaojun Yu, Wenxiao Chen, Ruilong Yan, Yiming Tang, Liangtu Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17092v2.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, sparse view, segmentation, face, ar, sparse-view, few-shot, 3d gaussian  
- **[CuriGS: Curriculum-Guided Gaussian Splatting for Sparse View Synthesis](https://arxiv.org/abs/2511.16030v1)**  
  Authors: Zijian Wu, Mingfeng Jiang, Zidian Lin, Ying Song, Hanjie Ma, Qun Wu, Dongping Zhang, Guiyang Pu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16030v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zijian1026.github.io/CuriGS/)  
  Keywords: 3d reconstruction, high-fidelity, gaussian splatting, sparse view, efficient, ar, sparse-view, 3d gaussian  
- **[SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2511.14633v1)**  
  Authors: Meiying Gu, Jiawei Zhang, Jiahe Li, Xiaohan Yu, Haonan Luo, Jin Zheng, Xiao Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14633v1.pdf)  
  Keywords: gaussian splatting, efficient, face, ar, sparse-view, geometry, nerf, 3d gaussian  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: 3d reconstruction, high-fidelity, gaussian splatting, ar, face, sparse-view, illumination, geometry, compact, 3d gaussian  
- **[RoboTidy : A 3D Gaussian Splatting Household Tidying Benchmark for Embodied Navigation and Action](https://arxiv.org/abs/2511.14161v2)**  
  Authors: Xiaoquan Sun, Ruijian Zhang, Kang Pang, Bingchen Miao, Yuxiang Tan, Zhen Yang, Ming Li, Jiayu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14161v2.pdf)  
  Keywords: few-shot, ar, gaussian splatting, 3d gaussian  
- **[SplatSearch: Instance Image Goal Navigation for Mobile Robots using 3D Gaussian Splatting and Diffusion Models](https://arxiv.org/abs/2511.12972v1)**  
  Authors: Siddarth Narasimhan, Matthew Lisondra, Haitong Wang, Goldie Nejat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12972v1.pdf)  
  Keywords: gaussian splatting, ar, sparse-view, semantic, 3d gaussian  

### Geometry Reconstruction

*Showing the latest 50 out of 339 papers*

- **[EGGS: Exchangeable 2D/3D Gaussian Splatting for Geometry-Appearance Balanced Novel View Synthesis](https://arxiv.org/abs/2512.02932v1)**  
  Authors: Yancheng Zhang, Guangyu Sun, Chen Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02932v1.pdf)  
  Keywords: dynamic, gaussian splatting, autonomous driving, efficient, ar, vr, geometry, real-time rendering, 3d gaussian  
- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: reflection, high-fidelity, gaussian splatting, efficient, face, ar, efficient rendering, geometry, real-time rendering, nerf, 3d gaussian  
- **[PoreTrack3D: A Benchmark for Dynamic 3D Gaussian Splatting in Pore-Scale Facial Trajectory Tracking](https://arxiv.org/abs/2512.02648v1)**  
  Authors: Dong Li, Jiahao Xiong, Yingda Huang, Le Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02648v1.pdf)  
  Keywords: 3d reconstruction, tracking, dynamic, high-fidelity, gaussian splatting, ar, face, motion, 3d gaussian  
- **[Content-Aware Texturing for Gaussian Splatting](https://arxiv.org/abs/2512.02621v1)**  
  Authors: Panagiotis Papantonakis, Georgios Kopanas, Fredo Durand, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02621v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gs-texturing/)  
  Keywords: 3d reconstruction, gaussian splatting, mapping, ar, geometry, real-time rendering  
- **[SplatSuRe: Selective Super-Resolution for Multi-view Consistent 3D Gaussian Splatting](https://arxiv.org/abs/2512.02172v1)**  
  Authors: Pranav Asthana, Alex Hanson, Allen Tu, Tom Goldstein, Matthias Zwicker, Amitabh Varshney  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02172v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, nerf, 3d gaussian  
- **[EGG-Fusion: Efficient 3D Reconstruction with Geometry-aware Gaussian Surfel on the Fly](https://arxiv.org/abs/2512.01296v1)**  
  Authors: Xiaokun Pan, Zhenzhe Li, Zhichao Ye, Hongjia Zhai, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/eggfusion/)  
  Keywords: 3d reconstruction, tracking, gaussian splatting, mapping, efficient, face, ar, slam, geometry, nerf, 3d gaussian  
- **[LISA-3D: Lifting Language-Image Segmentation to 3D via Multi-View Consistency](https://arxiv.org/abs/2512.01008v1)**  
  Authors: Zhongbin Guo, Jiahe Liu, Wenyu Gao, Yushan Li, Chengzhi Li, Ping Jian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01008v1.pdf)  
  Keywords: 3d reconstruction, ar, efficient, segmentation, geometry  
- **[PolarGS: Polarimetric Cues for Ambiguity-Free Gaussian Splatting with Accurate Geometry Recovery](https://arxiv.org/abs/2512.00794v1)**  
  Authors: Bo Guo, Sijia Wen, Yifan Zhao, Jia Li, Zhiming Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00794v1.pdf)  
  Keywords: gaussian splatting, ar, face, geometry, 3d gaussian  
- **[Asset-Driven Sematic Reconstruction of Dynamic Scene with Multi-Human-Object Interactions](https://arxiv.org/abs/2512.00547v1)**  
  Authors: Sandika Biswas, Qianyi Wu, Biplab Banerjee, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00547v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, human, mapping, fast, ar, face, semantic, deformation, vr, motion, geometry, 3d gaussian  
- **[TGSFormer: Scalable Temporal Gaussian Splatting for Embodied Semantic Scene Completion](https://arxiv.org/abs/2512.00300v1)**  
  Authors: Rui Qian, Haozhi Cao, Tianchen Deng, Tianxin Hu, Weixiang Guo, Shenghai Yuan, Lihua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00300v1.pdf)  
  Keywords: gaussian splatting, ar, semantic, head, geometry, compact  

### Large Scene

*Showing the latest 50 out of 76 papers*

- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: 3d reconstruction, gaussian splatting, ar, understanding, geometry, outdoor, 3d gaussian  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: gaussian splatting, fast, ar, semantic, geometry, outdoor  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, relighting, efficient, face, segmentation, ar, lighting, semantic, illumination, geometry, outdoor  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, geometry, outdoor, 3d gaussian  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: urban scene, dynamic, gaussian splatting, human, autonomous driving, ar, 4d  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: gaussian splatting, fast, ar, head, large scene, 3d gaussian  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: gaussian splatting, mapping, ar, understanding, slam, motion, geometry, outdoor, 3d gaussian  
- **[D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction](https://arxiv.org/abs/2510.25173v2)**  
  Authors: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25173v2.pdf)  
  Keywords: urban scene, gaussian splatting, autonomous driving, ar, geometry  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: 3d reconstruction, urban scene, gaussian splatting, ar, face, semantic  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/2510.22669v1)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22669v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, human, mapping, segmentation, ar, slam, outdoor, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 406 papers*

- **[EGGS: Exchangeable 2D/3D Gaussian Splatting for Geometry-Appearance Balanced Novel View Synthesis](https://arxiv.org/abs/2512.02932v1)**  
  Authors: Yancheng Zhang, Guangyu Sun, Chen Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02932v1.pdf)  
  Keywords: dynamic, gaussian splatting, autonomous driving, efficient, ar, vr, geometry, real-time rendering, 3d gaussian  
- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: reflection, high-fidelity, gaussian splatting, efficient, face, ar, efficient rendering, geometry, real-time rendering, nerf, 3d gaussian  
- **[EGG-Fusion: Efficient 3D Reconstruction with Geometry-aware Gaussian Surfel on the Fly](https://arxiv.org/abs/2512.01296v1)**  
  Authors: Xiaokun Pan, Zhenzhe Li, Zhichao Ye, Hongjia Zhai, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/eggfusion/)  
  Keywords: 3d reconstruction, tracking, gaussian splatting, mapping, efficient, face, ar, slam, geometry, nerf, 3d gaussian  
- **[LISA-3D: Lifting Language-Image Segmentation to 3D via Multi-View Consistency](https://arxiv.org/abs/2512.01008v1)**  
  Authors: Zhongbin Guo, Jiahe Liu, Wenyu Gao, Yushan Li, Chengzhi Li, Ping Jian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01008v1.pdf)  
  Keywords: 3d reconstruction, ar, efficient, segmentation, geometry  
- **[Binary-Gaussian: Compact and Progressive Representation for 3D Gaussian Segmentation](https://arxiv.org/abs/2512.00944v1)**  
  Authors: An Yang, Chenyu Liu, Jun Du, Jianqing Gao, Jia Pan, Jinshui Hu, Baocai Yin, Bing Yin, Cong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00944v1.pdf)  
  Keywords: gaussian splatting, mapping, efficient, segmentation, ar, head, semantic, compact, 3d gaussian  
- **[Feed-Forward 3D Gaussian Splatting Compression with Long-Context Modeling](https://arxiv.org/abs/2512.00877v1)**  
  Authors: Zhening Liu, Rui Song, Yushi Huang, Yingdong Hu, Xinjie Zhang, Jiawei Shao, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00877v1.pdf)  
  Keywords: gaussian splatting, ar, compression, compact, 3d gaussian  
- **[Smol-GS: Compact Representations for Abstract 3D Gaussian Splatting](https://arxiv.org/abs/2512.00850v1)**  
  Authors: Haishan Wang, Mohammad Hassan Vali, Arno Solin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00850v1.pdf)  
  Keywords: gaussian splatting, efficient, compression, ar, understanding, semantic, compact, 3d gaussian  
- **[Cross-Temporal 3D Gaussian Splatting for Sparse-View Guided Scene Update](https://arxiv.org/abs/2512.00534v1)**  
  Authors: Zeyuan An, Yanghang Xiao, Zhiying Leng, Frederick W. B. Li, Xiaohui Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00534v1.pdf)  
  Keywords: gaussian splatting, sparse view, efficient, ar, sparse-view, 3d gaussian  
- **[TGSFormer: Scalable Temporal Gaussian Splatting for Embodied Semantic Scene Completion](https://arxiv.org/abs/2512.00300v1)**  
  Authors: Rui Qian, Haozhi Cao, Tianchen Deng, Tianxin Hu, Weixiang Guo, Shenghai Yuan, Lihua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00300v1.pdf)  
  Keywords: gaussian splatting, ar, semantic, head, geometry, compact  
- **[Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views](https://arxiv.org/abs/2512.00255v1)**  
  Authors: Kunwar Maheep Singh, Jianchun Chen, Vladislav Golyanik, Stephan J. Garbin, Thabo Beeler, Rishabh Dabral, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/RHC/)  
  Keywords: relightable, tracking, dynamic, sparse view, human, body, relighting, efficient, ar, sparse-view, lighting, illumination, motion, geometry, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 188 papers*

- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: reflection, high-fidelity, gaussian splatting, efficient, face, ar, efficient rendering, geometry, real-time rendering, nerf, 3d gaussian  
- **[PoreTrack3D: A Benchmark for Dynamic 3D Gaussian Splatting in Pore-Scale Facial Trajectory Tracking](https://arxiv.org/abs/2512.02648v1)**  
  Authors: Dong Li, Jiahao Xiong, Yingda Huang, Le Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02648v1.pdf)  
  Keywords: 3d reconstruction, tracking, dynamic, high-fidelity, gaussian splatting, ar, face, motion, 3d gaussian  
- **[G-SHARP: Gaussian Surgical Hardware Accelerated Real-time Pipeline](https://arxiv.org/abs/2512.02482v1)**  
  Authors: Vishwesh Nath, Javier G. Tejero, Ruilong Li, Filippo Filicori, Mahdi Azizian, Sean D. Huver  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02482v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, fast, ar, deformation, nerf  
- **[VIGS-SLAM: Visual Inertial Gaussian Splatting SLAM](https://arxiv.org/abs/2512.02293v1)**  
  Authors: Zihan Zhu, Wei Zhang, Norbert Haala, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02293v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vigs-slam.github.io)  
  Keywords: tracking, high-fidelity, gaussian splatting, mapping, ar, slam, motion, 3d gaussian  
- **[ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation](https://arxiv.org/abs/2512.02013v1)**  
  Authors: Chenyang Gu, Jiaming Liu, Hao Chen, Runzhong Huang, Qingpo Wuwu, Zhuoyang Liu, Xiaoqi Li, Ying Li, Renrui Zhang, Peng Jia, Pheng-Ann Heng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02013v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, face, understanding, 3d gaussian  
- **[Asset-Driven Sematic Reconstruction of Dynamic Scene with Multi-Human-Object Interactions](https://arxiv.org/abs/2512.00547v1)**  
  Authors: Sandika Biswas, Qianyi Wu, Biplab Banerjee, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00547v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, human, mapping, fast, ar, face, semantic, deformation, vr, motion, geometry, 3d gaussian  
- **[MrGS: Multi-modal Radiance Fields with 3D Gaussian Splatting for RGB-Thermal Novel View Synthesis](https://arxiv.org/abs/2511.22997v1)**  
  Authors: Minseong Kweon, Janghyun Kim, Ukcheol Shin, Jinsun Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22997v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, nerf, 3d gaussian  
- **[Can Protective Watermarking Safeguard the Copyright of 3D Gaussian Splatting?](https://arxiv.org/abs/2511.22262v1)**  
  Authors: Wenkai Huang, Yijia Guo, Gaolei Li, Lei Ma, Hang Zhang, Liwen Hu, Jiazheng Wang, Jianhua Li, Tiejun Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22262v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, 4d, 3d gaussian  
- **[IE-SRGS: An Internal-External Knowledge Fusion Framework for High-Fidelity 3D Gaussian Splatting Super-Resolution](https://arxiv.org/abs/2511.22233v1)**  
  Authors: Xiang Feng, Tieshi Zhong, Shuo Chang, Weiliu Wang, Chengkai Wang, Yifei Chen, Yuhe Wang, Zhenzhong Kuang, Xuefei Yin, Yanming Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22233v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, geometry, 3d gaussian  
- **[Unlocking Zero-shot Potential of Semi-dense Image Matching via Gaussian Splatting](https://arxiv.org/abs/2511.21265v1)**  
  Authors: Juncheng Chen, Chao Xu, Yanjun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21265v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, geometry, 3d gaussian  

### Ray Tracing

- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: reflection, gaussian splatting, ray tracing, ar, illumination, geometry  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: gaussian splatting, ray marching, efficient, ar, geometry, 3d gaussian  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: relightable, gaussian splatting, ray tracing, efficient, face, ar, light transport, lighting, shadow, real-time rendering  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: global illumination, reflection, gaussian splatting, relighting, efficient, ar, light transport, lighting, illumination, geometry  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v2)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v2.pdf)  
  Keywords: dynamic, gaussian splatting, ray tracing, fast, ar, 4d  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: reflection, high-fidelity, gaussian splatting, ray tracing, relighting, ar, face, lighting, illumination, geometry, nerf, 3d gaussian  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: global illumination, relightable, dynamic, gaussian splatting, relighting, ar, face, lighting, illumination, shadow, outdoor, 3d gaussian  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: dynamic, gaussian splatting, path tracing, ar, face, lighting, 3d gaussian  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relightable, gaussian splatting, ray marching, relighting, efficient, face, ar, lighting, efficient rendering, geometry, 3d gaussian  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ray tracing, efficient, ar, real-time rendering  

### Relighting

*Showing the latest 50 out of 118 papers*

- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: reflection, high-fidelity, gaussian splatting, efficient, face, ar, efficient rendering, geometry, real-time rendering, nerf, 3d gaussian  
- **[Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views](https://arxiv.org/abs/2512.00255v1)**  
  Authors: Kunwar Maheep Singh, Jianchun Chen, Vladislav Golyanik, Stephan J. Garbin, Thabo Beeler, Rishabh Dabral, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/RHC/)  
  Keywords: relightable, tracking, dynamic, sparse view, human, body, relighting, efficient, ar, sparse-view, lighting, illumination, motion, geometry, 3d gaussian  
- **[Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes](https://arxiv.org/abs/2511.21367v1)**  
  Authors: Yangle Liu, Fengze Li, Kan Liu, Jieming Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21367v1.pdf)  
  Keywords: reflection, dynamic, gaussian splatting, ar, lightweight, 4d, motion, geometry, nerf  
- **[CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation](https://arxiv.org/abs/2511.17904v1)**  
  Authors: Yuhang Ming, Chenxin Fang, Xingyuan Yu, Fan Zhang, Weichen Dai, Wanzeng Kong, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17904v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, understanding, lighting, semantic, geometry, compact  
- **[Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction](https://arxiv.org/abs/2511.14540v1)**  
  Authors: Hao Tian, Chenyangguang Zhang, Rui Liu, Wen Shen, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14540v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, lighting, 4d, deformation, motion, geometry, 3d gaussian  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: 3d reconstruction, high-fidelity, gaussian splatting, ar, face, sparse-view, illumination, geometry, compact, 3d gaussian  
- **[iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion](https://arxiv.org/abs/2511.14149v1)**  
  Authors: Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14149v1.pdf)  
  Keywords: tracking, gaussian splatting, ar, lighting, slam, head, robotics, nerf, 3d gaussian  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, relighting, efficient, face, segmentation, ar, lighting, semantic, illumination, geometry, outdoor  
- **[Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis](https://arxiv.org/abs/2511.13011v1)**  
  Authors: Qingsen Ma, Chen Zou, Dianyun Wang, Jia Wang, Liuyu Xiang, Zhaofeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13011v1.pdf)  
  Keywords: 3d reconstruction, dynamic, gaussian splatting, ar, face, illumination, geometry, 3d gaussian  
- **[Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric](https://arxiv.org/abs/2511.08032v1)**  
  Authors: Zhaolin Wan, Yining Diao, Jingqi Xu, Hao Wang, Zhiyang Li, Xiaopeng Fan, Wangmeng Zuo, Debin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.08032v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, lighting, 3d gaussian  

### SLAM

*Showing the latest 50 out of 143 papers*

- **[PoreTrack3D: A Benchmark for Dynamic 3D Gaussian Splatting in Pore-Scale Facial Trajectory Tracking](https://arxiv.org/abs/2512.02648v1)**  
  Authors: Dong Li, Jiahao Xiong, Yingda Huang, Le Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02648v1.pdf)  
  Keywords: 3d reconstruction, tracking, dynamic, high-fidelity, gaussian splatting, ar, face, motion, 3d gaussian  
- **[Content-Aware Texturing for Gaussian Splatting](https://arxiv.org/abs/2512.02621v1)**  
  Authors: Panagiotis Papantonakis, Georgios Kopanas, Fredo Durand, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02621v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gs-texturing/)  
  Keywords: 3d reconstruction, gaussian splatting, mapping, ar, geometry, real-time rendering  
- **[VIGS-SLAM: Visual Inertial Gaussian Splatting SLAM](https://arxiv.org/abs/2512.02293v1)**  
  Authors: Zihan Zhu, Wei Zhang, Norbert Haala, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02293v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vigs-slam.github.io)  
  Keywords: tracking, high-fidelity, gaussian splatting, mapping, ar, slam, motion, 3d gaussian  
- **[TagSplat: Topology-Aware Gaussian Splatting for Dynamic Mesh Modeling and Tracking](https://arxiv.org/abs/2512.01329v1)**  
  Authors: Hanzhi Guo, Dongdong Weng, Mo Su, Yixiao Chen, Xiaonuo Dongye, Chenyu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01329v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haza628.github.io/tagSplat/)  
  Keywords: tracking, dynamic, gaussian splatting, animation, ar, face, 4d  
- **[EGG-Fusion: Efficient 3D Reconstruction with Geometry-aware Gaussian Surfel on the Fly](https://arxiv.org/abs/2512.01296v1)**  
  Authors: Xiaokun Pan, Zhenzhe Li, Zhichao Ye, Hongjia Zhai, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/eggfusion/)  
  Keywords: 3d reconstruction, tracking, gaussian splatting, mapping, efficient, face, ar, slam, geometry, nerf, 3d gaussian  
- **[Binary-Gaussian: Compact and Progressive Representation for 3D Gaussian Segmentation](https://arxiv.org/abs/2512.00944v1)**  
  Authors: An Yang, Chenyu Liu, Jun Du, Jianqing Gao, Jia Pan, Jinshui Hu, Baocai Yin, Bing Yin, Cong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00944v1.pdf)  
  Keywords: gaussian splatting, mapping, efficient, segmentation, ar, head, semantic, compact, 3d gaussian  
- **[Asset-Driven Sematic Reconstruction of Dynamic Scene with Multi-Human-Object Interactions](https://arxiv.org/abs/2512.00547v1)**  
  Authors: Sandika Biswas, Qianyi Wu, Biplab Banerjee, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00547v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, human, mapping, fast, ar, face, semantic, deformation, vr, motion, geometry, 3d gaussian  
- **[Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views](https://arxiv.org/abs/2512.00255v1)**  
  Authors: Kunwar Maheep Singh, Jianchun Chen, Vladislav Golyanik, Stephan J. Garbin, Thabo Beeler, Rishabh Dabral, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/RHC/)  
  Keywords: relightable, tracking, dynamic, sparse view, human, body, relighting, efficient, ar, sparse-view, lighting, illumination, motion, geometry, 3d gaussian  
- **[DiskChunGS: Large-Scale 3D Gaussian SLAM Through Chunk-Based Memory Management](https://arxiv.org/abs/2511.23030v1)**  
  Authors: Casimir Feldmann, Maximum Wilder-Smith, Vaishakh Patil, Michael Oechsle, Michael Niemeyer, Keisuke Tateno, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23030v1.pdf)  
  Keywords: gaussian splatting, ar, face, slam, real-time rendering, 3d gaussian  
- **[GS-Checker: Tampering Localization for 3D Gaussian Splatting](https://arxiv.org/abs/2511.20354v1)**  
  Authors: Haoliang Han, Ziyuan Luo, Jun Qi, Anderson Rocha, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20354v1.pdf)  
  Keywords: ar, localization, gaussian splatting, 3d gaussian  

### Scene Understanding

*Showing the latest 50 out of 203 papers*

- **[ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation](https://arxiv.org/abs/2512.02013v1)**  
  Authors: Chenyang Gu, Jiaming Liu, Hao Chen, Runzhong Huang, Qingpo Wuwu, Zhuoyang Liu, Xiaoqi Li, Ying Li, Renrui Zhang, Peng Jia, Pheng-Ann Heng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02013v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, face, understanding, 3d gaussian  
- **[LISA-3D: Lifting Language-Image Segmentation to 3D via Multi-View Consistency](https://arxiv.org/abs/2512.01008v1)**  
  Authors: Zhongbin Guo, Jiahe Liu, Wenyu Gao, Yushan Li, Chengzhi Li, Ping Jian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01008v1.pdf)  
  Keywords: 3d reconstruction, ar, efficient, segmentation, geometry  
- **[Binary-Gaussian: Compact and Progressive Representation for 3D Gaussian Segmentation](https://arxiv.org/abs/2512.00944v1)**  
  Authors: An Yang, Chenyu Liu, Jun Du, Jianqing Gao, Jia Pan, Jinshui Hu, Baocai Yin, Bing Yin, Cong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00944v1.pdf)  
  Keywords: gaussian splatting, mapping, efficient, segmentation, ar, head, semantic, compact, 3d gaussian  
- **[Smol-GS: Compact Representations for Abstract 3D Gaussian Splatting](https://arxiv.org/abs/2512.00850v1)**  
  Authors: Haishan Wang, Mohammad Hassan Vali, Arno Solin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00850v1.pdf)  
  Keywords: gaussian splatting, efficient, compression, ar, understanding, semantic, compact, 3d gaussian  
- **[Asset-Driven Sematic Reconstruction of Dynamic Scene with Multi-Human-Object Interactions](https://arxiv.org/abs/2512.00547v1)**  
  Authors: Sandika Biswas, Qianyi Wu, Biplab Banerjee, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00547v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, human, mapping, fast, ar, face, semantic, deformation, vr, motion, geometry, 3d gaussian  
- **[SplatFont3D: Structure-Aware Text-to-3D Artistic Font Generation with Part-Level Style Control](https://arxiv.org/abs/2512.00413v1)**  
  Authors: Ji Gan, Lingxu Chen, Jiaxu Leng, Xinbo Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00413v1.pdf)  
  Keywords: dynamic, gaussian splatting, animation, human, fast, ar, semantic, nerf, 3d gaussian  
- **[TGSFormer: Scalable Temporal Gaussian Splatting for Embodied Semantic Scene Completion](https://arxiv.org/abs/2512.00300v1)**  
  Authors: Rui Qian, Haozhi Cao, Tianchen Deng, Tianxin Hu, Weixiang Guo, Shenghai Yuan, Lihua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00300v1.pdf)  
  Keywords: gaussian splatting, ar, semantic, head, geometry, compact  
- **[Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v2)**  
  Authors: Andy Huynh, João Malheiro Silva, Holger Caesar, Tong Duy Son  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20348v2.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, ar, face, semantic, geometry, 3d gaussian  
- **[GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861v2)**  
  Authors: GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu, Kerui Li, Mengyuan Xu, Qiuping Deng, Siting Wang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yankai Wang, Yu Cao, Yifan Chang, Yuan Xu, Yun Ye, Yang Wang, Yukun Zhou, Zhengyuan Zhang, Zhehao Dong, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19861v2.pdf)  
  Keywords: gaussian splatting, efficient, ar, semantic, motion, 3d gaussian  
- **[DensifyBeforehand: LiDAR-assisted Content-aware Densification for Efficient and Quality 3D Gaussian Splatting](https://arxiv.org/abs/2511.19294v1)**  
  Authors: Phurtivilai Patt, Leyang Huang, Yinqiang Zhang, Yang Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19294v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, semantic, 3d gaussian  



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