# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-12-09 00:55:47

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
- [Avatar Generation](#avatar-generation) (340 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (402 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (80 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (341 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (76 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (400 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (191 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (14 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (119 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (143 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (207 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v1)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v1.pdf)  
  Keywords: survey, mapping, localization, 3d gaussian, understanding, semantic, ar, nerf, gaussian splatting, slam, robotics  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: survey, mapping, localization, 3d gaussian, efficient, semantic, high-fidelity, ar, gaussian splatting, slam, robotics  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: motion, survey, 4d, 3d gaussian, fast, ar, nerf, geometry, gaussian splatting  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: survey, avatar, efficient rendering, 3d gaussian, face, efficient, animation, 3d reconstruction, ar, real-time rendering, gaussian splatting, lighting  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: survey, lightweight, efficient, understanding, human, ar, nerf, gaussian splatting  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: survey, 3d gaussian, efficient, understanding, fast, neural rendering, nerf, ar, gaussian splatting, slam  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: segmentation, survey, 3d gaussian, understanding, semantic, high-fidelity, ar, nerf, gaussian splatting, lighting, compact  
- **[A Study of the Framework and Real-World Applications of Language Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: survey, 3d gaussian, efficient, understanding, semantic, ar, nerf, gaussian splatting, robotics  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: survey, 3d gaussian, human, ar, nerf, gaussian splatting, robotics  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: motion, sparse-view, survey, 3d gaussian, 3d reconstruction, vr, ar, nerf, geometry, gaussian splatting, robotics  

### Acceleration

*Showing the latest 50 out of 252 papers*

- **[EGGS: Exchangeable 2D/3D Gaussian Splatting for Geometry-Appearance Balanced Novel View Synthesis](https://arxiv.org/abs/2512.02932v1)**  
  Authors: Yancheng Zhang, Guangyu Sun, Chen Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02932v1.pdf)  
  Keywords: dynamic, 3d gaussian, efficient, vr, ar, real-time rendering, geometry, gaussian splatting, autonomous driving  
- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: reflection, efficient rendering, 3d gaussian, face, efficient, high-fidelity, real-time rendering, nerf, ar, geometry, gaussian splatting  
- **[Content-Aware Texturing for Gaussian Splatting](https://arxiv.org/abs/2512.02621v1)**  
  Authors: Panagiotis Papantonakis, Georgios Kopanas, Fredo Durand, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02621v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gs-texturing/)  
  Keywords: 3d reconstruction, ar, real-time rendering, geometry, gaussian splatting, mapping  
- **[G-SHARP: Gaussian Surgical Hardware Accelerated Real-time Pipeline](https://arxiv.org/abs/2512.02482v1)**  
  Authors: Vishwesh Nath, Javier G. Tejero, Ruilong Li, Filippo Filicori, Mahdi Azizian, Sean D. Huver  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02482v1.pdf)  
  Keywords: nerf, fast, high-fidelity, deformation, ar, gaussian splatting  
- **[Asset-Driven Sematic Reconstruction of Dynamic Scene with Multi-Human-Object Interactions](https://arxiv.org/abs/2512.00547v1)**  
  Authors: Sandika Biswas, Qianyi Wu, Biplab Banerjee, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00547v1.pdf)  
  Keywords: motion, dynamic, 3d gaussian, face, semantic, fast, high-fidelity, deformation, human, geometry, gaussian splatting, mapping, ar, vr  
- **[SplatFont3D: Structure-Aware Text-to-3D Artistic Font Generation with Part-Level Style Control](https://arxiv.org/abs/2512.00413v1)**  
  Authors: Ji Gan, Lingxu Chen, Jiaxu Leng, Xinbo Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00413v1.pdf)  
  Keywords: dynamic, 3d gaussian, semantic, fast, human, nerf, ar, gaussian splatting, animation  
- **[DiskChunGS: Large-Scale 3D Gaussian SLAM Through Chunk-Based Memory Management](https://arxiv.org/abs/2511.23030v1)**  
  Authors: Casimir Feldmann, Maximum Wilder-Smith, Vaishakh Patil, Michael Oechsle, Michael Niemeyer, Keisuke Tateno, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23030v1.pdf)  
  Keywords: 3d gaussian, face, ar, real-time rendering, gaussian splatting, slam  
- **[DenoiseGS: Gaussian Reconstruction Model for Burst Denoising](https://arxiv.org/abs/2511.22939v2)**  
  Authors: Yongsen Cheng, Yuanhao Cai, Yulun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22939v2.pdf)  
  Keywords: motion, 3d gaussian, fast, ar, nerf, geometry, gaussian splatting  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: semantic, outdoor, fast, ar, geometry, gaussian splatting  
- **[Alias-free 4D Gaussian Splatting](https://arxiv.org/abs/2511.18367v1)**  
  Authors: Zilong Chen, Huan-ang Gao, Delin Qu, Haohan Chi, Hao Tang, Kai Zhang, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18367v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4d-alias-free.github.io/4D-Alias-free/)  
  Keywords: 4d, dynamic, ar, real-time rendering, gaussian splatting  

### Applications

*Showing the latest 50 out of 995 papers*

- **[TED-4DGS: Temporally Activated and Embedding-based Deformation for 4DGS Compression](https://arxiv.org/abs/2512.05446v1)**  
  Authors: Cheng-Yuan Ho, He-Bi Yang, Jui-Chiu Chiang, Yu-Lun Liu, Wen-Hsiao Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05446v1.pdf)  
  Keywords: 4d, dynamic, compression, lightweight, 3d gaussian, efficient, deformation, ar, gaussian splatting, compact  
- **[SplatPainter: Interactive Authoring of 3D Gaussians from 2D Edits via Test-Time Training](https://arxiv.org/abs/2512.05354v1)**  
  Authors: Yang Zheng, Hao Tan, Kai Zhang, Peng Wang, Leonidas Guibas, Gordon Wetzstein, Wang Yifan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05354v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, gaussian splatting, compact  
- **[Splannequin: Freezing Monocular Mannequin-Challenge Footage with Dual-Detection Splatting](https://arxiv.org/abs/2512.05113v1)**  
  Authors: Hao-Jen Chien, Yi-Chuan Huang, Chung-Ho Wu, Wei-Lun Chao, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05113v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chien90190.github.io/splannequin/)  
  Keywords: motion, dynamic, high-fidelity, ar, gaussian splatting, head  
- **[4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer](https://arxiv.org/abs/2512.05060v1)**  
  Authors: Xianfeng Wu, Yajing Bai, Minghan Li, Xianzu Wu, Xueqi Zhao, Zhongyuan Lai, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05060v1.pdf)  
  Keywords: dynamic, 4d, understanding, semantic, ar, nerf, geometry, gaussian splatting  
- **[RobustSplat++: Decoupling Densification, Dynamics, and Illumination for In-the-Wild 3DGS](https://arxiv.org/abs/2512.04815v1)**  
  Authors: Chuanyu Fu, Guanying Chen, Yuqi Zhang, Kunbin Yao, Yuan Xiong, Chuan Huang, Shuguang Cui, Yasuyuki Matsushita, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04815v1.pdf)  
  Keywords: dynamic, 3d gaussian, semantic, ar, illumination, gaussian splatting  
- **[Bridging Simulation and Reality: Cross-Domain Transfer with Semantic 2D Gaussian Splatting](https://arxiv.org/abs/2512.04731v1)**  
  Authors: Jian Tang, Pu Pang, Haowen Sun, Chengzhong Ma, Xingyu Chen, Hua Huang, Xuguang Lan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04731v1.pdf)  
  Keywords: gaussian splatting, semantic, ar  
- **[Gaussian Entropy Fields: Driving Adaptive Sparsity in 3D Gaussian Optimization](https://arxiv.org/abs/2512.04542v1)**  
  Authors: Hong Kuang, Jianchen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04542v1.pdf)  
  Keywords: 3d gaussian, face, ar, nerf, geometry, gaussian splatting  
- **[SyncTrack4D: Cross-Video Motion Alignment and Video Synchronization for Multi-Video 4D Gaussian Splatting](https://arxiv.org/abs/2512.04315v1)**  
  Authors: Yonghan Lee, Tsung-Wei Huang, Shiv Gehlot, Jaehoon Choi, Guan-Ming Su, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04315v1.pdf)  
  Keywords: motion, dynamic, 4d, high-fidelity, ar, nerf, geometry, gaussian splatting  
- **[Mind-to-Face: Neural-Driven Photorealistic Avatar Synthesis via EEG Decoding](https://arxiv.org/abs/2512.04313v1)**  
  Authors: Haolin Xiong, Tianwen Fu, Pratusha Bhuvana Prasad, Yunxuan Cai, Haiwei Chen, Wenbin Teng, Hanyuan Xiao, Yajie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04313v1.pdf)  
  Keywords: motion, dynamic, avatar, 3d gaussian, face, high-fidelity, ar, geometry, gaussian splatting  
- **[C3G: Learning Compact 3D Representations with 2K Gaussians](https://arxiv.org/abs/2512.04021v1)**  
  Authors: Honggyu An, Jaewoo Jung, Mungyeom Kim, Sunghwan Hong, Chaehyun Kim, Kazumi Fukuda, Minkyeong Jeon, Jisang Han, Takuya Narihira, Hyuna Ko, Junsu Kim, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04021v1.pdf)  
  Keywords: segmentation, 3d gaussian, efficient, compact, understanding, ar, gaussian splatting, head, sparse view  

### Avatar Generation

*Showing the latest 50 out of 340 papers*

- **[Splannequin: Freezing Monocular Mannequin-Challenge Footage with Dual-Detection Splatting](https://arxiv.org/abs/2512.05113v1)**  
  Authors: Hao-Jen Chien, Yi-Chuan Huang, Chung-Ho Wu, Wei-Lun Chao, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05113v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chien90190.github.io/splannequin/)  
  Keywords: motion, dynamic, high-fidelity, ar, gaussian splatting, head  
- **[Gaussian Entropy Fields: Driving Adaptive Sparsity in 3D Gaussian Optimization](https://arxiv.org/abs/2512.04542v1)**  
  Authors: Hong Kuang, Jianchen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04542v1.pdf)  
  Keywords: 3d gaussian, face, ar, nerf, geometry, gaussian splatting  
- **[Mind-to-Face: Neural-Driven Photorealistic Avatar Synthesis via EEG Decoding](https://arxiv.org/abs/2512.04313v1)**  
  Authors: Haolin Xiong, Tianwen Fu, Pratusha Bhuvana Prasad, Yunxuan Cai, Haiwei Chen, Wenbin Teng, Hanyuan Xiao, Yajie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04313v1.pdf)  
  Keywords: motion, dynamic, avatar, 3d gaussian, face, high-fidelity, ar, geometry, gaussian splatting  
- **[C3G: Learning Compact 3D Representations with 2K Gaussians](https://arxiv.org/abs/2512.04021v1)**  
  Authors: Honggyu An, Jaewoo Jung, Mungyeom Kim, Sunghwan Hong, Chaehyun Kim, Kazumi Fukuda, Minkyeong Jeon, Jisang Han, Takuya Narihira, Hyuna Ko, Junsu Kim, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04021v1.pdf)  
  Keywords: segmentation, 3d gaussian, efficient, compact, understanding, ar, gaussian splatting, head, sparse view  
- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: reflection, efficient rendering, 3d gaussian, face, efficient, high-fidelity, real-time rendering, nerf, ar, geometry, gaussian splatting  
- **[PoreTrack3D: A Benchmark for Dynamic 3D Gaussian Splatting in Pore-Scale Facial Trajectory Tracking](https://arxiv.org/abs/2512.02648v1)**  
  Authors: Dong Li, Jiahao Xiong, Yingda Huang, Le Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02648v1.pdf)  
  Keywords: motion, dynamic, 3d gaussian, face, 3d reconstruction, high-fidelity, ar, gaussian splatting, tracking  
- **[ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation](https://arxiv.org/abs/2512.02013v1)**  
  Authors: Chenyang Gu, Jiaming Liu, Hao Chen, Runzhong Huang, Qingpo Wuwu, Zhuoyang Liu, Xiaoqi Li, Ying Li, Renrui Zhang, Peng Jia, Pheng-Ann Heng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02013v1.pdf)  
  Keywords: 3d gaussian, face, understanding, high-fidelity, ar, gaussian splatting  
- **[TagSplat: Topology-Aware Gaussian Splatting for Dynamic Mesh Modeling and Tracking](https://arxiv.org/abs/2512.01329v1)**  
  Authors: Hanzhi Guo, Dongdong Weng, Mo Su, Yixiao Chen, Xiaonuo Dongye, Chenyu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01329v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haza628.github.io/tagSplat/)  
  Keywords: 4d, dynamic, face, ar, gaussian splatting, animation, tracking  
- **[EGG-Fusion: Efficient 3D Reconstruction with Geometry-aware Gaussian Surfel on the Fly](https://arxiv.org/abs/2512.01296v1)**  
  Authors: Xiaokun Pan, Zhenzhe Li, Zhichao Ye, Hongjia Zhai, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/eggfusion/)  
  Keywords: mapping, 3d gaussian, face, efficient, 3d reconstruction, ar, nerf, geometry, gaussian splatting, slam, tracking  
- **[Binary-Gaussian: Compact and Progressive Representation for 3D Gaussian Segmentation](https://arxiv.org/abs/2512.00944v1)**  
  Authors: An Yang, Chenyu Liu, Jun Du, Jianqing Gao, Jia Pan, Jinshui Hu, Baocai Yin, Bing Yin, Cong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00944v1.pdf)  
  Keywords: segmentation, mapping, 3d gaussian, efficient, semantic, ar, gaussian splatting, head, compact  

### Dynamic Scene

*Showing the latest 50 out of 402 papers*

- **[TED-4DGS: Temporally Activated and Embedding-based Deformation for 4DGS Compression](https://arxiv.org/abs/2512.05446v1)**  
  Authors: Cheng-Yuan Ho, He-Bi Yang, Jui-Chiu Chiang, Yu-Lun Liu, Wen-Hsiao Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05446v1.pdf)  
  Keywords: 4d, dynamic, compression, lightweight, 3d gaussian, efficient, deformation, ar, gaussian splatting, compact  
- **[Splannequin: Freezing Monocular Mannequin-Challenge Footage with Dual-Detection Splatting](https://arxiv.org/abs/2512.05113v1)**  
  Authors: Hao-Jen Chien, Yi-Chuan Huang, Chung-Ho Wu, Wei-Lun Chao, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05113v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chien90190.github.io/splannequin/)  
  Keywords: motion, dynamic, high-fidelity, ar, gaussian splatting, head  
- **[4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer](https://arxiv.org/abs/2512.05060v1)**  
  Authors: Xianfeng Wu, Yajing Bai, Minghan Li, Xianzu Wu, Xueqi Zhao, Zhongyuan Lai, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05060v1.pdf)  
  Keywords: dynamic, 4d, understanding, semantic, ar, nerf, geometry, gaussian splatting  
- **[RobustSplat++: Decoupling Densification, Dynamics, and Illumination for In-the-Wild 3DGS](https://arxiv.org/abs/2512.04815v1)**  
  Authors: Chuanyu Fu, Guanying Chen, Yuqi Zhang, Kunbin Yao, Yuan Xiong, Chuan Huang, Shuguang Cui, Yasuyuki Matsushita, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04815v1.pdf)  
  Keywords: dynamic, 3d gaussian, semantic, ar, illumination, gaussian splatting  
- **[SyncTrack4D: Cross-Video Motion Alignment and Video Synchronization for Multi-Video 4D Gaussian Splatting](https://arxiv.org/abs/2512.04315v1)**  
  Authors: Yonghan Lee, Tsung-Wei Huang, Shiv Gehlot, Jaehoon Choi, Guan-Ming Su, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04315v1.pdf)  
  Keywords: motion, dynamic, 4d, high-fidelity, ar, nerf, geometry, gaussian splatting  
- **[Mind-to-Face: Neural-Driven Photorealistic Avatar Synthesis via EEG Decoding](https://arxiv.org/abs/2512.04313v1)**  
  Authors: Haolin Xiong, Tianwen Fu, Pratusha Bhuvana Prasad, Yunxuan Cai, Haiwei Chen, Wenbin Teng, Hanyuan Xiao, Yajie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04313v1.pdf)  
  Keywords: motion, dynamic, avatar, 3d gaussian, face, high-fidelity, ar, geometry, gaussian splatting  
- **[Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding](https://arxiv.org/abs/2512.03601v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion4d-web/.)  
  Keywords: segmentation, motion, 4d, dynamic, understanding, semantic, ar, geometry, gaussian splatting, tracking  
- **[Flux4D: Flow-based Unsupervised 4D Reconstruction](https://arxiv.org/abs/2512.03210v1)**  
  Authors: Jingkang Wang, Henry Che, Yun Chen, Ze Yang, Lily Goli, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03210v1.pdf)  
  Keywords: motion, 4d, dynamic, 3d gaussian, efficient, outdoor, ar, nerf, gaussian splatting, robotics  
- **[EGGS: Exchangeable 2D/3D Gaussian Splatting for Geometry-Appearance Balanced Novel View Synthesis](https://arxiv.org/abs/2512.02932v1)**  
  Authors: Yancheng Zhang, Guangyu Sun, Chen Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02932v1.pdf)  
  Keywords: dynamic, 3d gaussian, efficient, vr, ar, real-time rendering, geometry, gaussian splatting, autonomous driving  
- **[PoreTrack3D: A Benchmark for Dynamic 3D Gaussian Splatting in Pore-Scale Facial Trajectory Tracking](https://arxiv.org/abs/2512.02648v1)**  
  Authors: Dong Li, Jiahao Xiong, Yingda Huang, Le Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02648v1.pdf)  
  Keywords: motion, dynamic, 3d gaussian, face, 3d reconstruction, high-fidelity, ar, gaussian splatting, tracking  

### Few-shot

*Showing the latest 50 out of 80 papers*

- **[C3G: Learning Compact 3D Representations with 2K Gaussians](https://arxiv.org/abs/2512.04021v1)**  
  Authors: Honggyu An, Jaewoo Jung, Mungyeom Kim, Sunghwan Hong, Chaehyun Kim, Kazumi Fukuda, Minkyeong Jeon, Jisang Han, Takuya Narihira, Hyuna Ko, Junsu Kim, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04021v1.pdf)  
  Keywords: segmentation, 3d gaussian, efficient, compact, understanding, ar, gaussian splatting, head, sparse view  
- **[Cross-Temporal 3D Gaussian Splatting for Sparse-View Guided Scene Update](https://arxiv.org/abs/2512.00534v1)**  
  Authors: Zeyuan An, Yanghang Xiao, Zhiying Leng, Frederick W. B. Li, Xiaohui Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00534v1.pdf)  
  Keywords: sparse-view, 3d gaussian, efficient, ar, gaussian splatting, sparse view  
- **[Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views](https://arxiv.org/abs/2512.00255v1)**  
  Authors: Kunwar Maheep Singh, Jianchun Chen, Vladislav Golyanik, Stephan J. Garbin, Thabo Beeler, Rishabh Dabral, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/RHC/)  
  Keywords: motion, sparse-view, dynamic, illumination, 3d gaussian, efficient, body, human, ar, relighting, geometry, lighting, sparse view, relightable, tracking  
- **[Observer Actor: Active Vision Imitation Learning with Sparse View Gaussian Splatting](https://arxiv.org/abs/2511.18140v1)**  
  Authors: Yilong Wang, Cheng Qian, Ruomeng Fan, Edward Johns  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18140v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://obact.github.io.)  
  Keywords: dynamic, 3d gaussian, ar, gaussian splatting, sparse view  
- **[Frequency-Adaptive Sharpness Regularization for Improving 3D Gaussian Splatting Generalization](https://arxiv.org/abs/2511.17918v1)**  
  Authors: Youngsik Yun, Dongjun Gu, Youngjung Uh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bbangsik13.github.io/FASR.)  
  Keywords: few-shot, gaussian splatting, 3d gaussian, ar  
- **[SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting](https://arxiv.org/abs/2511.17092v2)**  
  Authors: Di Wu, Liu Liu, Xueyu Yuan, Qiaojun Yu, Wenxiao Chen, Ruilong Yan, Yiming Tang, Liangtu Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17092v2.pdf)  
  Keywords: segmentation, sparse-view, 3d gaussian, face, 3d reconstruction, ar, few-shot, gaussian splatting, sparse view  
- **[CuriGS: Curriculum-Guided Gaussian Splatting for Sparse View Synthesis](https://arxiv.org/abs/2511.16030v1)**  
  Authors: Zijian Wu, Mingfeng Jiang, Zidian Lin, Ying Song, Hanjie Ma, Qun Wu, Dongping Zhang, Guiyang Pu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16030v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zijian1026.github.io/CuriGS/)  
  Keywords: sparse-view, 3d gaussian, efficient, 3d reconstruction, high-fidelity, ar, gaussian splatting, sparse view  
- **[SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2511.14633v1)**  
  Authors: Meiying Gu, Jiawei Zhang, Jiahe Li, Xiaohan Yu, Haonan Luo, Jin Zheng, Xiao Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14633v1.pdf)  
  Keywords: sparse-view, 3d gaussian, face, efficient, ar, nerf, geometry, gaussian splatting  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: sparse-view, 3d gaussian, face, 3d reconstruction, high-fidelity, ar, illumination, geometry, gaussian splatting, compact  
- **[RoboTidy : A 3D Gaussian Splatting Household Tidying Benchmark for Embodied Navigation and Action](https://arxiv.org/abs/2511.14161v2)**  
  Authors: Xiaoquan Sun, Ruijian Zhang, Kang Pang, Bingchen Miao, Yuxiang Tan, Zhen Yang, Ming Li, Jiayu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14161v2.pdf)  
  Keywords: few-shot, gaussian splatting, 3d gaussian, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 341 papers*

- **[4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer](https://arxiv.org/abs/2512.05060v1)**  
  Authors: Xianfeng Wu, Yajing Bai, Minghan Li, Xianzu Wu, Xueqi Zhao, Zhongyuan Lai, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05060v1.pdf)  
  Keywords: dynamic, 4d, understanding, semantic, ar, nerf, geometry, gaussian splatting  
- **[Gaussian Entropy Fields: Driving Adaptive Sparsity in 3D Gaussian Optimization](https://arxiv.org/abs/2512.04542v1)**  
  Authors: Hong Kuang, Jianchen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04542v1.pdf)  
  Keywords: 3d gaussian, face, ar, nerf, geometry, gaussian splatting  
- **[SyncTrack4D: Cross-Video Motion Alignment and Video Synchronization for Multi-Video 4D Gaussian Splatting](https://arxiv.org/abs/2512.04315v1)**  
  Authors: Yonghan Lee, Tsung-Wei Huang, Shiv Gehlot, Jaehoon Choi, Guan-Ming Su, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04315v1.pdf)  
  Keywords: motion, dynamic, 4d, high-fidelity, ar, nerf, geometry, gaussian splatting  
- **[Mind-to-Face: Neural-Driven Photorealistic Avatar Synthesis via EEG Decoding](https://arxiv.org/abs/2512.04313v1)**  
  Authors: Haolin Xiong, Tianwen Fu, Pratusha Bhuvana Prasad, Yunxuan Cai, Haiwei Chen, Wenbin Teng, Hanyuan Xiao, Yajie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04313v1.pdf)  
  Keywords: motion, dynamic, avatar, 3d gaussian, face, high-fidelity, ar, geometry, gaussian splatting  
- **[Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding](https://arxiv.org/abs/2512.03601v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion4d-web/.)  
  Keywords: segmentation, motion, 4d, dynamic, understanding, semantic, ar, geometry, gaussian splatting, tracking  
- **[EGGS: Exchangeable 2D/3D Gaussian Splatting for Geometry-Appearance Balanced Novel View Synthesis](https://arxiv.org/abs/2512.02932v1)**  
  Authors: Yancheng Zhang, Guangyu Sun, Chen Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02932v1.pdf)  
  Keywords: dynamic, 3d gaussian, efficient, vr, ar, real-time rendering, geometry, gaussian splatting, autonomous driving  
- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: reflection, efficient rendering, 3d gaussian, face, efficient, high-fidelity, real-time rendering, nerf, ar, geometry, gaussian splatting  
- **[PoreTrack3D: A Benchmark for Dynamic 3D Gaussian Splatting in Pore-Scale Facial Trajectory Tracking](https://arxiv.org/abs/2512.02648v1)**  
  Authors: Dong Li, Jiahao Xiong, Yingda Huang, Le Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02648v1.pdf)  
  Keywords: motion, dynamic, 3d gaussian, face, 3d reconstruction, high-fidelity, ar, gaussian splatting, tracking  
- **[Content-Aware Texturing for Gaussian Splatting](https://arxiv.org/abs/2512.02621v1)**  
  Authors: Panagiotis Papantonakis, Georgios Kopanas, Fredo Durand, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02621v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gs-texturing/)  
  Keywords: 3d reconstruction, ar, real-time rendering, geometry, gaussian splatting, mapping  
- **[SplatSuRe: Selective Super-Resolution for Multi-view Consistent 3D Gaussian Splatting](https://arxiv.org/abs/2512.02172v1)**  
  Authors: Pranav Asthana, Alex Hanson, Allen Tu, Tom Goldstein, Matthias Zwicker, Amitabh Varshney  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02172v1.pdf)  
  Keywords: 3d gaussian, ar, nerf, geometry, gaussian splatting  

### Large Scene

*Showing the latest 50 out of 76 papers*

- **[Flux4D: Flow-based Unsupervised 4D Reconstruction](https://arxiv.org/abs/2512.03210v1)**  
  Authors: Jingkang Wang, Henry Che, Yun Chen, Ze Yang, Lily Goli, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03210v1.pdf)  
  Keywords: motion, 4d, dynamic, 3d gaussian, efficient, outdoor, ar, nerf, gaussian splatting, robotics  
- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: 3d gaussian, understanding, 3d reconstruction, outdoor, ar, geometry, gaussian splatting  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: semantic, outdoor, fast, ar, geometry, gaussian splatting  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: segmentation, illumination, face, efficient, outdoor, semantic, high-fidelity, ar, relighting, geometry, gaussian splatting, lighting  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: 3d gaussian, outdoor, high-fidelity, ar, geometry, gaussian splatting  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: urban scene, 4d, dynamic, human, ar, gaussian splatting, autonomous driving  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: 3d gaussian, large scene, fast, ar, gaussian splatting, head  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: motion, mapping, 3d gaussian, understanding, outdoor, ar, geometry, gaussian splatting, slam  
- **[D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction](https://arxiv.org/abs/2510.25173v2)**  
  Authors: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25173v2.pdf)  
  Keywords: urban scene, ar, geometry, gaussian splatting, autonomous driving  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: urban scene, face, 3d reconstruction, semantic, ar, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 400 papers*

- **[TED-4DGS: Temporally Activated and Embedding-based Deformation for 4DGS Compression](https://arxiv.org/abs/2512.05446v1)**  
  Authors: Cheng-Yuan Ho, He-Bi Yang, Jui-Chiu Chiang, Yu-Lun Liu, Wen-Hsiao Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05446v1.pdf)  
  Keywords: 4d, dynamic, compression, lightweight, 3d gaussian, efficient, deformation, ar, gaussian splatting, compact  
- **[SplatPainter: Interactive Authoring of 3D Gaussians from 2D Edits via Test-Time Training](https://arxiv.org/abs/2512.05354v1)**  
  Authors: Yang Zheng, Hao Tan, Kai Zhang, Peng Wang, Leonidas Guibas, Gordon Wetzstein, Wang Yifan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05354v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, gaussian splatting, compact  
- **[C3G: Learning Compact 3D Representations with 2K Gaussians](https://arxiv.org/abs/2512.04021v1)**  
  Authors: Honggyu An, Jaewoo Jung, Mungyeom Kim, Sunghwan Hong, Chaehyun Kim, Kazumi Fukuda, Minkyeong Jeon, Jisang Han, Takuya Narihira, Hyuna Ko, Junsu Kim, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04021v1.pdf)  
  Keywords: segmentation, 3d gaussian, efficient, compact, understanding, ar, gaussian splatting, head, sparse view  
- **[Flux4D: Flow-based Unsupervised 4D Reconstruction](https://arxiv.org/abs/2512.03210v1)**  
  Authors: Jingkang Wang, Henry Che, Yun Chen, Ze Yang, Lily Goli, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03210v1.pdf)  
  Keywords: motion, 4d, dynamic, 3d gaussian, efficient, outdoor, ar, nerf, gaussian splatting, robotics  
- **[EGGS: Exchangeable 2D/3D Gaussian Splatting for Geometry-Appearance Balanced Novel View Synthesis](https://arxiv.org/abs/2512.02932v1)**  
  Authors: Yancheng Zhang, Guangyu Sun, Chen Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02932v1.pdf)  
  Keywords: dynamic, 3d gaussian, efficient, vr, ar, real-time rendering, geometry, gaussian splatting, autonomous driving  
- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: reflection, efficient rendering, 3d gaussian, face, efficient, high-fidelity, real-time rendering, nerf, ar, geometry, gaussian splatting  
- **[EGG-Fusion: Efficient 3D Reconstruction with Geometry-aware Gaussian Surfel on the Fly](https://arxiv.org/abs/2512.01296v1)**  
  Authors: Xiaokun Pan, Zhenzhe Li, Zhichao Ye, Hongjia Zhai, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/eggfusion/)  
  Keywords: mapping, 3d gaussian, face, efficient, 3d reconstruction, ar, nerf, geometry, gaussian splatting, slam, tracking  
- **[LISA-3D: Lifting Language-Image Segmentation to 3D via Multi-View Consistency](https://arxiv.org/abs/2512.01008v1)**  
  Authors: Zhongbin Guo, Jiahe Liu, Wenyu Gao, Yushan Li, Chengzhi Li, Ping Jian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01008v1.pdf)  
  Keywords: segmentation, efficient, 3d reconstruction, ar, geometry  
- **[Binary-Gaussian: Compact and Progressive Representation for 3D Gaussian Segmentation](https://arxiv.org/abs/2512.00944v1)**  
  Authors: An Yang, Chenyu Liu, Jun Du, Jianqing Gao, Jia Pan, Jinshui Hu, Baocai Yin, Bing Yin, Cong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00944v1.pdf)  
  Keywords: segmentation, mapping, 3d gaussian, efficient, semantic, ar, gaussian splatting, head, compact  
- **[Feed-Forward 3D Gaussian Splatting Compression with Long-Context Modeling](https://arxiv.org/abs/2512.00877v1)**  
  Authors: Zhening Liu, Rui Song, Yushi Huang, Yingdong Hu, Xinjie Zhang, Jiawei Shao, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00877v1.pdf)  
  Keywords: compression, 3d gaussian, ar, gaussian splatting, compact  

### Quality Enhancement

*Showing the latest 50 out of 191 papers*

- **[SplatPainter: Interactive Authoring of 3D Gaussians from 2D Edits via Test-Time Training](https://arxiv.org/abs/2512.05354v1)**  
  Authors: Yang Zheng, Hao Tan, Kai Zhang, Peng Wang, Leonidas Guibas, Gordon Wetzstein, Wang Yifan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05354v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, gaussian splatting, compact  
- **[Splannequin: Freezing Monocular Mannequin-Challenge Footage with Dual-Detection Splatting](https://arxiv.org/abs/2512.05113v1)**  
  Authors: Hao-Jen Chien, Yi-Chuan Huang, Chung-Ho Wu, Wei-Lun Chao, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05113v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chien90190.github.io/splannequin/)  
  Keywords: motion, dynamic, high-fidelity, ar, gaussian splatting, head  
- **[SyncTrack4D: Cross-Video Motion Alignment and Video Synchronization for Multi-Video 4D Gaussian Splatting](https://arxiv.org/abs/2512.04315v1)**  
  Authors: Yonghan Lee, Tsung-Wei Huang, Shiv Gehlot, Jaehoon Choi, Guan-Ming Su, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04315v1.pdf)  
  Keywords: motion, dynamic, 4d, high-fidelity, ar, nerf, geometry, gaussian splatting  
- **[Mind-to-Face: Neural-Driven Photorealistic Avatar Synthesis via EEG Decoding](https://arxiv.org/abs/2512.04313v1)**  
  Authors: Haolin Xiong, Tianwen Fu, Pratusha Bhuvana Prasad, Yunxuan Cai, Haiwei Chen, Wenbin Teng, Hanyuan Xiao, Yajie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04313v1.pdf)  
  Keywords: motion, dynamic, avatar, 3d gaussian, face, high-fidelity, ar, geometry, gaussian splatting  
- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: reflection, efficient rendering, 3d gaussian, face, efficient, high-fidelity, real-time rendering, nerf, ar, geometry, gaussian splatting  
- **[PoreTrack3D: A Benchmark for Dynamic 3D Gaussian Splatting in Pore-Scale Facial Trajectory Tracking](https://arxiv.org/abs/2512.02648v1)**  
  Authors: Dong Li, Jiahao Xiong, Yingda Huang, Le Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02648v1.pdf)  
  Keywords: motion, dynamic, 3d gaussian, face, 3d reconstruction, high-fidelity, ar, gaussian splatting, tracking  
- **[G-SHARP: Gaussian Surgical Hardware Accelerated Real-time Pipeline](https://arxiv.org/abs/2512.02482v1)**  
  Authors: Vishwesh Nath, Javier G. Tejero, Ruilong Li, Filippo Filicori, Mahdi Azizian, Sean D. Huver  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02482v1.pdf)  
  Keywords: nerf, fast, high-fidelity, deformation, ar, gaussian splatting  
- **[VIGS-SLAM: Visual Inertial Gaussian Splatting SLAM](https://arxiv.org/abs/2512.02293v1)**  
  Authors: Zihan Zhu, Wei Zhang, Norbert Haala, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02293v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vigs-slam.github.io)  
  Keywords: motion, mapping, 3d gaussian, high-fidelity, ar, gaussian splatting, slam, tracking  
- **[ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation](https://arxiv.org/abs/2512.02013v1)**  
  Authors: Chenyang Gu, Jiaming Liu, Hao Chen, Runzhong Huang, Qingpo Wuwu, Zhuoyang Liu, Xiaoqi Li, Ying Li, Renrui Zhang, Peng Jia, Pheng-Ann Heng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02013v1.pdf)  
  Keywords: 3d gaussian, face, understanding, high-fidelity, ar, gaussian splatting  
- **[Asset-Driven Sematic Reconstruction of Dynamic Scene with Multi-Human-Object Interactions](https://arxiv.org/abs/2512.00547v1)**  
  Authors: Sandika Biswas, Qianyi Wu, Biplab Banerjee, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00547v1.pdf)  
  Keywords: motion, dynamic, 3d gaussian, face, semantic, fast, high-fidelity, deformation, human, geometry, gaussian splatting, mapping, ar, vr  

### Ray Tracing

- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: ray tracing, ar, reflection, illumination, geometry, gaussian splatting  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: 3d gaussian, efficient, ray marching, ar, geometry, gaussian splatting  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: ray tracing, light transport, face, efficient, shadow, ar, real-time rendering, gaussian splatting, lighting, relightable  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: light transport, illumination, global illumination, efficient, ar, reflection, relighting, geometry, gaussian splatting, lighting  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v2)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v2.pdf)  
  Keywords: ray tracing, 4d, dynamic, fast, ar, gaussian splatting  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: ray tracing, reflection, 3d gaussian, illumination, face, high-fidelity, ar, nerf, relighting, geometry, gaussian splatting, lighting  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: dynamic, global illumination, 3d gaussian, illumination, face, shadow, outdoor, ar, relighting, gaussian splatting, lighting, relightable  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: path tracing, dynamic, 3d gaussian, face, ar, gaussian splatting, lighting  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: efficient rendering, 3d gaussian, face, ray marching, efficient, ar, relighting, geometry, gaussian splatting, lighting, relightable  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: ray tracing, efficient, high-fidelity, ar, real-time rendering, gaussian splatting  

### Relighting

*Showing the latest 50 out of 119 papers*

- **[RobustSplat++: Decoupling Densification, Dynamics, and Illumination for In-the-Wild 3DGS](https://arxiv.org/abs/2512.04815v1)**  
  Authors: Chuanyu Fu, Guanying Chen, Yuqi Zhang, Kunbin Yao, Yuan Xiong, Chuan Huang, Shuguang Cui, Yasuyuki Matsushita, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04815v1.pdf)  
  Keywords: dynamic, 3d gaussian, semantic, ar, illumination, gaussian splatting  
- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: reflection, efficient rendering, 3d gaussian, face, efficient, high-fidelity, real-time rendering, nerf, ar, geometry, gaussian splatting  
- **[Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views](https://arxiv.org/abs/2512.00255v1)**  
  Authors: Kunwar Maheep Singh, Jianchun Chen, Vladislav Golyanik, Stephan J. Garbin, Thabo Beeler, Rishabh Dabral, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/RHC/)  
  Keywords: motion, sparse-view, dynamic, illumination, 3d gaussian, efficient, body, human, ar, relighting, geometry, lighting, sparse view, relightable, tracking  
- **[Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes](https://arxiv.org/abs/2511.21367v1)**  
  Authors: Yangle Liu, Fengze Li, Kan Liu, Jieming Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21367v1.pdf)  
  Keywords: motion, dynamic, nerf, 4d, lightweight, ar, reflection, geometry, gaussian splatting  
- **[CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation](https://arxiv.org/abs/2511.17904v1)**  
  Authors: Yuhang Ming, Chenxin Fang, Xingyuan Yu, Fan Zhang, Weichen Dai, Wanzeng Kong, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17904v1.pdf)  
  Keywords: dynamic, understanding, semantic, ar, geometry, gaussian splatting, lighting, compact  
- **[Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction](https://arxiv.org/abs/2511.14540v1)**  
  Authors: Hao Tian, Chenyangguang Zhang, Rui Liu, Wen Shen, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14540v1.pdf)  
  Keywords: motion, dynamic, 4d, 3d gaussian, deformation, ar, geometry, gaussian splatting, lighting  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: sparse-view, 3d gaussian, face, 3d reconstruction, high-fidelity, ar, illumination, geometry, gaussian splatting, compact  
- **[iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion](https://arxiv.org/abs/2511.14149v1)**  
  Authors: Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14149v1.pdf)  
  Keywords: head, 3d gaussian, ar, nerf, gaussian splatting, lighting, slam, robotics, tracking  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: segmentation, illumination, face, efficient, outdoor, semantic, high-fidelity, ar, relighting, geometry, gaussian splatting, lighting  
- **[Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis](https://arxiv.org/abs/2511.13011v1)**  
  Authors: Qingsen Ma, Chen Zou, Dianyun Wang, Jia Wang, Liuyu Xiang, Zhaofeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13011v1.pdf)  
  Keywords: dynamic, 3d gaussian, face, 3d reconstruction, ar, illumination, geometry, gaussian splatting  

### SLAM

*Showing the latest 50 out of 143 papers*

- **[Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding](https://arxiv.org/abs/2512.03601v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion4d-web/.)  
  Keywords: segmentation, motion, 4d, dynamic, understanding, semantic, ar, geometry, gaussian splatting, tracking  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v1)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v1.pdf)  
  Keywords: survey, mapping, localization, 3d gaussian, understanding, semantic, ar, nerf, gaussian splatting, slam, robotics  
- **[PoreTrack3D: A Benchmark for Dynamic 3D Gaussian Splatting in Pore-Scale Facial Trajectory Tracking](https://arxiv.org/abs/2512.02648v1)**  
  Authors: Dong Li, Jiahao Xiong, Yingda Huang, Le Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02648v1.pdf)  
  Keywords: motion, dynamic, 3d gaussian, face, 3d reconstruction, high-fidelity, ar, gaussian splatting, tracking  
- **[Content-Aware Texturing for Gaussian Splatting](https://arxiv.org/abs/2512.02621v1)**  
  Authors: Panagiotis Papantonakis, Georgios Kopanas, Fredo Durand, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02621v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gs-texturing/)  
  Keywords: 3d reconstruction, ar, real-time rendering, geometry, gaussian splatting, mapping  
- **[VIGS-SLAM: Visual Inertial Gaussian Splatting SLAM](https://arxiv.org/abs/2512.02293v1)**  
  Authors: Zihan Zhu, Wei Zhang, Norbert Haala, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02293v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vigs-slam.github.io)  
  Keywords: motion, mapping, 3d gaussian, high-fidelity, ar, gaussian splatting, slam, tracking  
- **[TagSplat: Topology-Aware Gaussian Splatting for Dynamic Mesh Modeling and Tracking](https://arxiv.org/abs/2512.01329v1)**  
  Authors: Hanzhi Guo, Dongdong Weng, Mo Su, Yixiao Chen, Xiaonuo Dongye, Chenyu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01329v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haza628.github.io/tagSplat/)  
  Keywords: 4d, dynamic, face, ar, gaussian splatting, animation, tracking  
- **[EGG-Fusion: Efficient 3D Reconstruction with Geometry-aware Gaussian Surfel on the Fly](https://arxiv.org/abs/2512.01296v1)**  
  Authors: Xiaokun Pan, Zhenzhe Li, Zhichao Ye, Hongjia Zhai, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/eggfusion/)  
  Keywords: mapping, 3d gaussian, face, efficient, 3d reconstruction, ar, nerf, geometry, gaussian splatting, slam, tracking  
- **[Binary-Gaussian: Compact and Progressive Representation for 3D Gaussian Segmentation](https://arxiv.org/abs/2512.00944v1)**  
  Authors: An Yang, Chenyu Liu, Jun Du, Jianqing Gao, Jia Pan, Jinshui Hu, Baocai Yin, Bing Yin, Cong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00944v1.pdf)  
  Keywords: segmentation, mapping, 3d gaussian, efficient, semantic, ar, gaussian splatting, head, compact  
- **[Asset-Driven Sematic Reconstruction of Dynamic Scene with Multi-Human-Object Interactions](https://arxiv.org/abs/2512.00547v1)**  
  Authors: Sandika Biswas, Qianyi Wu, Biplab Banerjee, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00547v1.pdf)  
  Keywords: motion, dynamic, 3d gaussian, face, semantic, fast, high-fidelity, deformation, human, geometry, gaussian splatting, mapping, ar, vr  
- **[Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views](https://arxiv.org/abs/2512.00255v1)**  
  Authors: Kunwar Maheep Singh, Jianchun Chen, Vladislav Golyanik, Stephan J. Garbin, Thabo Beeler, Rishabh Dabral, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/RHC/)  
  Keywords: motion, sparse-view, dynamic, illumination, 3d gaussian, efficient, body, human, ar, relighting, geometry, lighting, sparse view, relightable, tracking  

### Scene Understanding

*Showing the latest 50 out of 207 papers*

- **[4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer](https://arxiv.org/abs/2512.05060v1)**  
  Authors: Xianfeng Wu, Yajing Bai, Minghan Li, Xianzu Wu, Xueqi Zhao, Zhongyuan Lai, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05060v1.pdf)  
  Keywords: dynamic, 4d, understanding, semantic, ar, nerf, geometry, gaussian splatting  
- **[RobustSplat++: Decoupling Densification, Dynamics, and Illumination for In-the-Wild 3DGS](https://arxiv.org/abs/2512.04815v1)**  
  Authors: Chuanyu Fu, Guanying Chen, Yuqi Zhang, Kunbin Yao, Yuan Xiong, Chuan Huang, Shuguang Cui, Yasuyuki Matsushita, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04815v1.pdf)  
  Keywords: dynamic, 3d gaussian, semantic, ar, illumination, gaussian splatting  
- **[Bridging Simulation and Reality: Cross-Domain Transfer with Semantic 2D Gaussian Splatting](https://arxiv.org/abs/2512.04731v1)**  
  Authors: Jian Tang, Pu Pang, Haowen Sun, Chengzhong Ma, Xingyu Chen, Hua Huang, Xuguang Lan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04731v1.pdf)  
  Keywords: gaussian splatting, semantic, ar  
- **[C3G: Learning Compact 3D Representations with 2K Gaussians](https://arxiv.org/abs/2512.04021v1)**  
  Authors: Honggyu An, Jaewoo Jung, Mungyeom Kim, Sunghwan Hong, Chaehyun Kim, Kazumi Fukuda, Minkyeong Jeon, Jisang Han, Takuya Narihira, Hyuna Ko, Junsu Kim, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04021v1.pdf)  
  Keywords: segmentation, 3d gaussian, efficient, compact, understanding, ar, gaussian splatting, head, sparse view  
- **[Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding](https://arxiv.org/abs/2512.03601v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion4d-web/.)  
  Keywords: segmentation, motion, 4d, dynamic, understanding, semantic, ar, geometry, gaussian splatting, tracking  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v1)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v1.pdf)  
  Keywords: survey, mapping, localization, 3d gaussian, understanding, semantic, ar, nerf, gaussian splatting, slam, robotics  
- **[ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation](https://arxiv.org/abs/2512.02013v1)**  
  Authors: Chenyang Gu, Jiaming Liu, Hao Chen, Runzhong Huang, Qingpo Wuwu, Zhuoyang Liu, Xiaoqi Li, Ying Li, Renrui Zhang, Peng Jia, Pheng-Ann Heng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02013v1.pdf)  
  Keywords: 3d gaussian, face, understanding, high-fidelity, ar, gaussian splatting  
- **[LISA-3D: Lifting Language-Image Segmentation to 3D via Multi-View Consistency](https://arxiv.org/abs/2512.01008v1)**  
  Authors: Zhongbin Guo, Jiahe Liu, Wenyu Gao, Yushan Li, Chengzhi Li, Ping Jian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.01008v1.pdf)  
  Keywords: segmentation, efficient, 3d reconstruction, ar, geometry  
- **[Binary-Gaussian: Compact and Progressive Representation for 3D Gaussian Segmentation](https://arxiv.org/abs/2512.00944v1)**  
  Authors: An Yang, Chenyu Liu, Jun Du, Jianqing Gao, Jia Pan, Jinshui Hu, Baocai Yin, Bing Yin, Cong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00944v1.pdf)  
  Keywords: segmentation, mapping, 3d gaussian, efficient, semantic, ar, gaussian splatting, head, compact  
- **[Smol-GS: Compact Representations for Abstract 3D Gaussian Splatting](https://arxiv.org/abs/2512.00850v1)**  
  Authors: Haishan Wang, Mohammad Hassan Vali, Arno Solin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00850v1.pdf)  
  Keywords: compression, 3d gaussian, efficient, understanding, semantic, ar, gaussian splatting, compact  



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