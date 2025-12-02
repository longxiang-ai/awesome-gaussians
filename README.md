# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-12-02 00:55:33

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
- [Acceleration](#acceleration) (253 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (996 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (337 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (395 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (78 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (332 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (77 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (402 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (188 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (15 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (119 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (139 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (200 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: high-fidelity, ar, mapping, robotics, localization, survey, efficient, gaussian splatting, slam, semantic, 3d gaussian  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: fast, ar, motion, geometry, 4d, survey, gaussian splatting, nerf, 3d gaussian  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: real-time rendering, efficient rendering, lighting, face, ar, avatar, animation, survey, efficient, gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: ar, lightweight, survey, understanding, efficient, gaussian splatting, nerf, human  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: fast, ar, survey, neural rendering, efficient, understanding, gaussian splatting, slam, nerf, 3d gaussian  
- **[A-TDOM: Active TDOM via On-the-Fly 3DGS](https://arxiv.org/abs/2509.12759v2)**  
  Authors: Yiwei Xu, Xiang Wang, Yifei Yu, Wentian Gan, Luca Morelli, Giulio Perda, Xiongwu Xiao, Zongqian Zhan, Xin Wang, Fabio Remondino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.12759v2.pdf)  
  Keywords: survey, face, ar  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: high-fidelity, ar, lighting, semantic, survey, understanding, compact, gaussian splatting, nerf, segmentation, 3d gaussian  
- **[A Study of the Framework and Real-World Applications of Language Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: ar, robotics, semantic, survey, understanding, efficient, gaussian splatting, nerf, 3d gaussian  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: ar, robotics, survey, gaussian splatting, nerf, human, 3d gaussian  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: ar, vr, motion, sparse-view, geometry, robotics, survey, gaussian splatting, nerf, 3d gaussian, 3d reconstruction  

### Acceleration

*Showing the latest 50 out of 253 papers*

- **[DiskChunGS: Large-Scale 3D Gaussian SLAM Through Chunk-Based Memory Management](https://arxiv.org/abs/2511.23030v1)**  
  Authors: Casimir Feldmann, Maximum Wilder-Smith, Vaishakh Patil, Michael Oechsle, Michael Niemeyer, Keisuke Tateno, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23030v1.pdf)  
  Keywords: real-time rendering, face, ar, slam, gaussian splatting, 3d gaussian  
- **[DenoiseGS: Gaussian Reconstruction Model for Burst Denoising](https://arxiv.org/abs/2511.22939v1)**  
  Authors: Yongsen Cheng, Yuanhao Cai, Yulun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22939v1.pdf)  
  Keywords: fast, ar, motion, geometry, gaussian splatting, nerf, 3d gaussian  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: fast, ar, geometry, gaussian splatting, outdoor, semantic  
- **[Alias-free 4D Gaussian Splatting](https://arxiv.org/abs/2511.18367v1)**  
  Authors: Zilong Chen, Huan-ang Gao, Delin Qu, Haohan Chi, Hao Tang, Kai Zhang, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18367v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4d-alias-free.github.io/4D-Alias-free/)  
  Keywords: real-time rendering, ar, dynamic, 4d, gaussian splatting  
- **[PEGS: Physics-Event Enhanced Large Spatiotemporal Motion Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2511.17116v1)**  
  Authors: Yijun Xu, Jingrui Zhang, Hongyi Liu, Yuhan Chen, Yuanyang Wang, Qingyao Guo, Dingwen Wang, Lei Yu, Chu He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17116v1.pdf)  
  Keywords: fast, ar, motion, dynamic, gaussian splatting, acceleration, 3d gaussian  
- **[One Walk is All You Need: Data-Efficient 3D RF Scene Reconstruction with Human Movements](https://arxiv.org/abs/2511.16966v1)**  
  Authors: Yiheng Bian, Zechen Li, Lanqing Yang, Hao Pan, Yezhou Wang, Longyuan Ge, Jeffery Wu, Ruiheng Liu, Yongjian Fu, Yichao chen, Guangtao xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16966v1.pdf)  
  Keywords: fast, high-fidelity, ar, mapping, motion, geometry, dynamic, efficient, gaussian splatting, human, 3d gaussian  
- **[Vorion: A RISC-V GPU with Hardware-Accelerated 3D Gaussian Rendering and Training](https://arxiv.org/abs/2511.16831v1)**  
  Authors: Yipeng Wang, Mengtian Yang, Chieh-pu Lo, Jaydeep P. Kulkarni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16831v1.pdf)  
  Keywords: real-time rendering, ar, 4d, neural rendering, gaussian splatting, 3d gaussian  
- **[Optimizing 3D Gaussian Splattering for Mobile GPUs](https://arxiv.org/abs/2511.16298v1)**  
  Authors: Md Musfiqur Rahman Sanim, Zhihao Shu, Bahram Afsharmanesh, AmirAli Mirian, Jiexiong Guan, Wei Niu, Bin Ren, Gagan Agrawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16298v1.pdf)  
  Keywords: fast, ar, mapping, efficient, gaussian splatting, 3d gaussian  
- **[Gaussian Blending: Rethinking Alpha Blending in 3D Gaussian Splatting](https://arxiv.org/abs/2511.15102v1)**  
  Authors: Junseo Koo, Jinseo Jeong, Gunhee Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.15102v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, gaussian splatting, ar  
- **[IBGS: Image-Based Gaussian Splatting](https://arxiv.org/abs/2511.14357v1)**  
  Authors: Hoang Chuong Nguyen, Wei Mao, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14357v1.pdf)  
  Keywords: fast, face, ar, head, efficient, gaussian splatting, 3d gaussian  

### Applications

*Showing the latest 50 out of 996 papers*

- **[FACT-GS: Frequency-Aligned Complexity-Aware Texture Reparameterization for 2D Gaussian Splatting](https://arxiv.org/abs/2511.23292v1)**  
  Authors: Tianhao Xie, Linlian Jiang, Xinxin Zuo, Yang Wang, Tiberiu Popa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23292v1.pdf)  
  Keywords: efficient, deformation, gaussian splatting, ar  
- **[Geometry-Consistent 4D Gaussian Splatting for Sparse-Input Dynamic View Synthesis](https://arxiv.org/abs/2511.23044v1)**  
  Authors: Yiwei Li, Jiannong Cao, Penghui Ruan, Divya Saxena, Songye Zhu, Yinfeng Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23044v1.pdf)  
  Keywords: ar, geometry, dynamic, 4d, gaussian splatting  
- **[DiskChunGS: Large-Scale 3D Gaussian SLAM Through Chunk-Based Memory Management](https://arxiv.org/abs/2511.23030v1)**  
  Authors: Casimir Feldmann, Maximum Wilder-Smith, Vaishakh Patil, Michael Oechsle, Michael Niemeyer, Keisuke Tateno, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23030v1.pdf)  
  Keywords: real-time rendering, face, ar, slam, gaussian splatting, 3d gaussian  
- **[MrGS: Multi-modal Radiance Fields with 3D Gaussian Splatting for RGB-Thermal Novel View Synthesis](https://arxiv.org/abs/2511.22997v1)**  
  Authors: Minseong Kweon, Janghyun Kim, Ukcheol Shin, Jinsun Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22997v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, nerf, 3d gaussian  
- **[DenoiseGS: Gaussian Reconstruction Model for Burst Denoising](https://arxiv.org/abs/2511.22939v1)**  
  Authors: Yongsen Cheng, Yuanhao Cai, Yulun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22939v1.pdf)  
  Keywords: fast, ar, motion, geometry, gaussian splatting, nerf, 3d gaussian  
- **[GSpaRC: Gaussian Splatting for Real-time Reconstruction of RF Channels](https://arxiv.org/abs/2511.22793v1)**  
  Authors: Bhavya Sai Nukapotula, Rishabh Tripathi, Seth Pregler, Dileep Kalathil, Srinivas Shakkottai, Theodore S. Rappaport  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22793v1.pdf)  
  Keywords: face, ar, lightweight, head, compact, gaussian splatting, 3d gaussian  
- **[Splat-SAP: Feed-Forward Gaussian Splatting for Human-Centered Scene with Scale-Aware Point Map Reconstruction](https://arxiv.org/abs/2511.22704v1)**  
  Authors: Boyao Zhou, Shunyuan Zheng, Zhanfeng Liao, Zihan Ma, Hanzhang Tu, Boning Liu, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22704v1.pdf)  
  Keywords: geometry, human, ar, gaussian splatting  
- **[Can Protective Watermarking Safeguard the Copyright of 3D Gaussian Splatting?](https://arxiv.org/abs/2511.22262v1)**  
  Authors: Wenkai Huang, Yijia Guo, Gaolei Li, Lei Ma, Hang Zhang, Liwen Hu, Jiazheng Wang, Jianhua Li, Tiejun Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22262v1.pdf)  
  Keywords: high-fidelity, ar, 4d, gaussian splatting, 3d gaussian  
- **[IE-SRGS: An Internal-External Knowledge Fusion Framework for High-Fidelity 3D Gaussian Splatting Super-Resolution](https://arxiv.org/abs/2511.22233v1)**  
  Authors: Xiang Feng, Tieshi Zhong, Shuo Chang, Weiliu Wang, Chengkai Wang, Yifei Chen, Yuhe Wang, Zhenzhong Kuang, Xuefei Yin, Yanming Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22233v1.pdf)  
  Keywords: high-fidelity, ar, geometry, gaussian splatting, 3d gaussian  
- **[3D-Consistent Multi-View Editing by Diffusion Guidance](https://arxiv.org/abs/2511.22228v1)**  
  Authors: Josef Bengtson, David Nilsson, Dong In Lee, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22228v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3d-consistent-editing.github.io/)  
  Keywords: ar, nerf  

### Avatar Generation

*Showing the latest 50 out of 337 papers*

- **[DiskChunGS: Large-Scale 3D Gaussian SLAM Through Chunk-Based Memory Management](https://arxiv.org/abs/2511.23030v1)**  
  Authors: Casimir Feldmann, Maximum Wilder-Smith, Vaishakh Patil, Michael Oechsle, Michael Niemeyer, Keisuke Tateno, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23030v1.pdf)  
  Keywords: real-time rendering, face, ar, slam, gaussian splatting, 3d gaussian  
- **[GSpaRC: Gaussian Splatting for Real-time Reconstruction of RF Channels](https://arxiv.org/abs/2511.22793v1)**  
  Authors: Bhavya Sai Nukapotula, Rishabh Tripathi, Seth Pregler, Dileep Kalathil, Srinivas Shakkottai, Theodore S. Rappaport  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22793v1.pdf)  
  Keywords: face, ar, lightweight, head, compact, gaussian splatting, 3d gaussian  
- **[Splat-SAP: Feed-Forward Gaussian Splatting for Human-Centered Scene with Scale-Aware Point Map Reconstruction](https://arxiv.org/abs/2511.22704v1)**  
  Authors: Boyao Zhou, Shunyuan Zheng, Zhanfeng Liao, Zihan Ma, Hanzhang Tu, Boning Liu, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22704v1.pdf)  
  Keywords: geometry, human, ar, gaussian splatting  
- **[Resolution Where It Counts: Hash-based GPU-Accelerated 3D Reconstruction via Variance-Adaptive Voxel Grids](https://arxiv.org/abs/2511.21459v1)**  
  Authors: Lorenzo De Rebotti, Emanuele Giacomini, Giorgio Grisetti, Luca Di Giammarino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21459v1.pdf)  
  Keywords: face, ar, dynamic, head, efficient, gaussian splatting, 3d reconstruction  
- **[Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v2)**  
  Authors: Andy Huynh, João Malheiro Silva, Holger Caesar, Tong Duy Son  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20348v2.pdf)  
  Keywords: face, ar, geometry, gaussian splatting, semantic, 3d gaussian, 3d reconstruction  
- **[STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction](https://arxiv.org/abs/2511.19854v2)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Zidu Wang, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19854v2.pdf)  
  Keywords: high-fidelity, ar, deformation, motion, dynamic, avatar, head, gaussian splatting, 3d gaussian  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: high-fidelity, ar, motion, dynamic, autonomous driving, gaussian splatting, human, 3d gaussian, tracking  
- **[Proxy-Free Gaussian Splats Deformation with Splat-Based Surface Estimation](https://arxiv.org/abs/2511.19542v1)**  
  Authors: Jaeyeong Kim, Seungwoo Yoo, Minhyuk Sung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19542v1.pdf)  
  Keywords: ar, face, deformation, head, nerf  
- **[AEGIS: Preserving privacy of 3D Facial Avatars with Adversarial Perturbations](https://arxiv.org/abs/2511.17747v1)**  
  Authors: Dawid Wolkiewicz, Anastasiya Pechko, Przemysław Spurek, Piotr Syga  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17747v1.pdf)  
  Keywords: face, ar, motion, geometry, dynamic, avatar, efficient, gaussian splatting, 3d gaussian  
- **[Towards Generative Design Using Optimal Transport for Shape Exploration and Solution Field Interpolation](https://arxiv.org/abs/2511.17111v1)**  
  Authors: Sergio Torregrosa, David Munoz, Hector Navarro, Charbel Farhat, Francisco Chinesta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17111v1.pdf)  
  Keywords: efficient, gaussian splatting, face, ar  

### Dynamic Scene

*Showing the latest 50 out of 395 papers*

- **[FACT-GS: Frequency-Aligned Complexity-Aware Texture Reparameterization for 2D Gaussian Splatting](https://arxiv.org/abs/2511.23292v1)**  
  Authors: Tianhao Xie, Linlian Jiang, Xinxin Zuo, Yang Wang, Tiberiu Popa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23292v1.pdf)  
  Keywords: efficient, deformation, gaussian splatting, ar  
- **[Geometry-Consistent 4D Gaussian Splatting for Sparse-Input Dynamic View Synthesis](https://arxiv.org/abs/2511.23044v1)**  
  Authors: Yiwei Li, Jiannong Cao, Penghui Ruan, Divya Saxena, Songye Zhu, Yinfeng Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23044v1.pdf)  
  Keywords: ar, geometry, dynamic, 4d, gaussian splatting  
- **[DenoiseGS: Gaussian Reconstruction Model for Burst Denoising](https://arxiv.org/abs/2511.22939v1)**  
  Authors: Yongsen Cheng, Yuanhao Cai, Yulun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22939v1.pdf)  
  Keywords: fast, ar, motion, geometry, gaussian splatting, nerf, 3d gaussian  
- **[Can Protective Watermarking Safeguard the Copyright of 3D Gaussian Splatting?](https://arxiv.org/abs/2511.22262v1)**  
  Authors: Wenkai Huang, Yijia Guo, Gaolei Li, Lei Ma, Hang Zhang, Liwen Hu, Jiazheng Wang, Jianhua Li, Tiejun Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22262v1.pdf)  
  Keywords: high-fidelity, ar, 4d, gaussian splatting, 3d gaussian  
- **[EAST: Environment-Aware Stylized Transition Along the Reality-Virtuality Continuum](https://arxiv.org/abs/2511.22056v1)**  
  Authors: Fengze Li, Jieming Ma, Kan Liu, Xiaohan Zhang, Yangle Liu, Yue Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22056v1.pdf)  
  Keywords: ar, vr, motion, gaussian splatting, 3d gaussian  
- **[Resolution Where It Counts: Hash-based GPU-Accelerated 3D Reconstruction via Variance-Adaptive Voxel Grids](https://arxiv.org/abs/2511.21459v1)**  
  Authors: Lorenzo De Rebotti, Emanuele Giacomini, Giorgio Grisetti, Luca Di Giammarino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21459v1.pdf)  
  Keywords: face, ar, dynamic, head, efficient, gaussian splatting, 3d reconstruction  
- **[Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes](https://arxiv.org/abs/2511.21367v1)**  
  Authors: Yangle Liu, Fengze Li, Kan Liu, Jieming Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21367v1.pdf)  
  Keywords: ar, motion, geometry, dynamic, lightweight, reflection, 4d, gaussian splatting, nerf  
- **[GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861v1)**  
  Authors: GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu, Kerui Li, Mengyuan Xu, Qiuping Deng, Siting Wang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yankai Wang, Yu Cao, Yifan Chang, Yuan Xu, Yun Ye, Yang Wang, Yukun Zhou, Zhengyuan Zhang, Zhehao Dong, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19861v1.pdf)  
  Keywords: ar, motion, efficient, gaussian splatting, semantic, 3d gaussian  
- **[STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction](https://arxiv.org/abs/2511.19854v2)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Zidu Wang, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19854v2.pdf)  
  Keywords: high-fidelity, ar, deformation, motion, dynamic, avatar, head, gaussian splatting, 3d gaussian  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: high-fidelity, ar, motion, dynamic, autonomous driving, gaussian splatting, human, 3d gaussian, tracking  

### Few-shot

*Showing the latest 50 out of 78 papers*

- **[Observer Actor: Active Vision Imitation Learning with Sparse View Gaussian Splatting](https://arxiv.org/abs/2511.18140v1)**  
  Authors: Yilong Wang, Cheng Qian, Ruomeng Fan, Edward Johns  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18140v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://obact.github.io.)  
  Keywords: ar, dynamic, sparse view, gaussian splatting, 3d gaussian  
- **[Frequency-Adaptive Sharpness Regularization for Improving 3D Gaussian Splatting Generalization](https://arxiv.org/abs/2511.17918v1)**  
  Authors: Youngsik Yun, Dongjun Gu, Youngjung Uh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bbangsik13.github.io/FASR.)  
  Keywords: 3d gaussian, few-shot, gaussian splatting, ar  
- **[SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting](https://arxiv.org/abs/2511.17092v2)**  
  Authors: Di Wu, Liu Liu, Xueyu Yuan, Qiaojun Yu, Wenxiao Chen, Ruilong Yan, Yiming Tang, Liangtu Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17092v2.pdf)  
  Keywords: few-shot, face, ar, sparse-view, sparse view, gaussian splatting, segmentation, 3d gaussian, 3d reconstruction  
- **[CuriGS: Curriculum-Guided Gaussian Splatting for Sparse View Synthesis](https://arxiv.org/abs/2511.16030v1)**  
  Authors: Zijian Wu, Mingfeng Jiang, Zidian Lin, Ying Song, Hanjie Ma, Qun Wu, Dongping Zhang, Guiyang Pu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16030v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zijian1026.github.io/CuriGS/)  
  Keywords: high-fidelity, ar, sparse-view, sparse view, efficient, gaussian splatting, 3d gaussian, 3d reconstruction  
- **[SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2511.14633v1)**  
  Authors: Meiying Gu, Jiawei Zhang, Jiahe Li, Xiaohan Yu, Haonan Luo, Jin Zheng, Xiao Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14633v1.pdf)  
  Keywords: face, ar, sparse-view, geometry, efficient, gaussian splatting, nerf, 3d gaussian  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: high-fidelity, face, ar, sparse-view, geometry, compact, gaussian splatting, illumination, 3d gaussian, 3d reconstruction  
- **[RoboTidy : A 3D Gaussian Splatting Household Tidying Benchmark for Embodied Navigation and Action](https://arxiv.org/abs/2511.14161v2)**  
  Authors: Xiaoquan Sun, Ruijian Zhang, Kang Pang, Bingchen Miao, Yuxiang Tan, Zhen Yang, Ming Li, Jiayu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14161v2.pdf)  
  Keywords: 3d gaussian, few-shot, gaussian splatting, ar  
- **[SplatSearch: Instance Image Goal Navigation for Mobile Robots using 3D Gaussian Splatting and Diffusion Models](https://arxiv.org/abs/2511.12972v1)**  
  Authors: Siddarth Narasimhan, Matthew Lisondra, Haitong Wang, Goldie Nejat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12972v1.pdf)  
  Keywords: ar, sparse-view, gaussian splatting, semantic, 3d gaussian  
- **[RealisticDreamer: Guidance Score Distillation for Few-shot Gaussian Splatting](https://arxiv.org/abs/2511.11213v1)**  
  Authors: Ruocheng Wu, Haolan He, Yufei Wang, Zhihao Li, Bihan Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.11213v1.pdf)  
  Keywords: few-shot, real-time rendering, ar, motion, geometry, gaussian splatting, semantic, 3d gaussian  
- **[Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction](https://arxiv.org/abs/2511.07122v1)**  
  Authors: Changyue Shi, Chuxiao Yang, Xinyuan Hu, Minghao Chen, Wenwen Pan, Yan Yang, Jiajun Ding, Zhou Yu, Jun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07122v1.pdf)  
  Keywords: few-shot, ar, deformation, dynamic, 4d, gaussian splatting, nerf  

### Geometry Reconstruction

*Showing the latest 50 out of 332 papers*

- **[Geometry-Consistent 4D Gaussian Splatting for Sparse-Input Dynamic View Synthesis](https://arxiv.org/abs/2511.23044v1)**  
  Authors: Yiwei Li, Jiannong Cao, Penghui Ruan, Divya Saxena, Songye Zhu, Yinfeng Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23044v1.pdf)  
  Keywords: ar, geometry, dynamic, 4d, gaussian splatting  
- **[DenoiseGS: Gaussian Reconstruction Model for Burst Denoising](https://arxiv.org/abs/2511.22939v1)**  
  Authors: Yongsen Cheng, Yuanhao Cai, Yulun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22939v1.pdf)  
  Keywords: fast, ar, motion, geometry, gaussian splatting, nerf, 3d gaussian  
- **[Splat-SAP: Feed-Forward Gaussian Splatting for Human-Centered Scene with Scale-Aware Point Map Reconstruction](https://arxiv.org/abs/2511.22704v1)**  
  Authors: Boyao Zhou, Shunyuan Zheng, Zhanfeng Liao, Zihan Ma, Hanzhang Tu, Boning Liu, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22704v1.pdf)  
  Keywords: geometry, human, ar, gaussian splatting  
- **[IE-SRGS: An Internal-External Knowledge Fusion Framework for High-Fidelity 3D Gaussian Splatting Super-Resolution](https://arxiv.org/abs/2511.22233v1)**  
  Authors: Xiang Feng, Tieshi Zhong, Shuo Chang, Weiliu Wang, Chengkai Wang, Yifei Chen, Yuhe Wang, Zhenzhong Kuang, Xuefei Yin, Yanming Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22233v1.pdf)  
  Keywords: high-fidelity, ar, geometry, gaussian splatting, 3d gaussian  
- **[RemedyGS: Defend 3D Gaussian Splatting against Computation Cost Attacks](https://arxiv.org/abs/2511.22147v1)**  
  Authors: Yanping Li, Zhening Liu, Zijian Li, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22147v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, 3d reconstruction  
- **[Resolution Where It Counts: Hash-based GPU-Accelerated 3D Reconstruction via Variance-Adaptive Voxel Grids](https://arxiv.org/abs/2511.21459v1)**  
  Authors: Lorenzo De Rebotti, Emanuele Giacomini, Giorgio Grisetti, Luca Di Giammarino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21459v1.pdf)  
  Keywords: face, ar, dynamic, head, efficient, gaussian splatting, 3d reconstruction  
- **[Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes](https://arxiv.org/abs/2511.21367v1)**  
  Authors: Yangle Liu, Fengze Li, Kan Liu, Jieming Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21367v1.pdf)  
  Keywords: ar, motion, geometry, dynamic, lightweight, reflection, 4d, gaussian splatting, nerf  
- **[Unlocking Zero-shot Potential of Semi-dense Image Matching via Gaussian Splatting](https://arxiv.org/abs/2511.21265v1)**  
  Authors: Juncheng Chen, Chao Xu, Yanjun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21265v1.pdf)  
  Keywords: high-fidelity, ar, geometry, gaussian splatting, 3d gaussian  
- **[Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v2)**  
  Authors: Andy Huynh, João Malheiro Silva, Holger Caesar, Tong Duy Son  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20348v2.pdf)  
  Keywords: face, ar, geometry, gaussian splatting, semantic, 3d gaussian, 3d reconstruction  
- **[MetroGS: Efficient and Stable Reconstruction of Geometrically Accurate High-Fidelity Large-Scale Scenes](https://arxiv.org/abs/2511.19172v1)**  
  Authors: Kehua Chen, Tianlu Mao, Zhuxin Ma, Hao Jiang, Zehao Li, Zihan Liu, Shuqi Gao, Honglong Zhao, Feng Dai, Yucheng Zhang, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19172v1.pdf)  
  Keywords: high-fidelity, ar, geometry, efficient, gaussian splatting, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 77 papers*

- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: ar, geometry, understanding, gaussian splatting, outdoor, 3d gaussian, 3d reconstruction  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: fast, ar, geometry, gaussian splatting, outdoor, semantic  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: high-fidelity, face, lighting, ar, relighting, geometry, efficient, gaussian splatting, outdoor, semantic, illumination, segmentation  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: high-fidelity, ar, geometry, gaussian splatting, outdoor, 3d gaussian  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: human, ar, dynamic, autonomous driving, 4d, gaussian splatting, urban scene  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: fast, ar, head, gaussian splatting, large scene, 3d gaussian  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: ar, mapping, motion, geometry, understanding, gaussian splatting, outdoor, slam, 3d gaussian  
- **[D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction](https://arxiv.org/abs/2510.25173v2)**  
  Authors: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25173v2.pdf)  
  Keywords: ar, geometry, autonomous driving, gaussian splatting, urban scene  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: face, ar, gaussian splatting, semantic, urban scene, 3d reconstruction  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/2510.22669v1)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22669v1.pdf)  
  Keywords: high-fidelity, ar, mapping, dynamic, gaussian splatting, outdoor, slam, human, segmentation, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 402 papers*

- **[FACT-GS: Frequency-Aligned Complexity-Aware Texture Reparameterization for 2D Gaussian Splatting](https://arxiv.org/abs/2511.23292v1)**  
  Authors: Tianhao Xie, Linlian Jiang, Xinxin Zuo, Yang Wang, Tiberiu Popa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23292v1.pdf)  
  Keywords: efficient, deformation, gaussian splatting, ar  
- **[GSpaRC: Gaussian Splatting for Real-time Reconstruction of RF Channels](https://arxiv.org/abs/2511.22793v1)**  
  Authors: Bhavya Sai Nukapotula, Rishabh Tripathi, Seth Pregler, Dileep Kalathil, Srinivas Shakkottai, Theodore S. Rappaport  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22793v1.pdf)  
  Keywords: face, ar, lightweight, head, compact, gaussian splatting, 3d gaussian  
- **[Resolution Where It Counts: Hash-based GPU-Accelerated 3D Reconstruction via Variance-Adaptive Voxel Grids](https://arxiv.org/abs/2511.21459v1)**  
  Authors: Lorenzo De Rebotti, Emanuele Giacomini, Giorgio Grisetti, Luca Di Giammarino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21459v1.pdf)  
  Keywords: face, ar, dynamic, head, efficient, gaussian splatting, 3d reconstruction  
- **[Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes](https://arxiv.org/abs/2511.21367v1)**  
  Authors: Yangle Liu, Fengze Li, Kan Liu, Jieming Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21367v1.pdf)  
  Keywords: ar, motion, geometry, dynamic, lightweight, reflection, 4d, gaussian splatting, nerf  
- **[GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861v1)**  
  Authors: GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu, Kerui Li, Mengyuan Xu, Qiuping Deng, Siting Wang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yankai Wang, Yu Cao, Yifan Chang, Yuan Xu, Yun Ye, Yang Wang, Yukun Zhou, Zhengyuan Zhang, Zhehao Dong, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19861v1.pdf)  
  Keywords: ar, motion, efficient, gaussian splatting, semantic, 3d gaussian  
- **[DensifyBeforehand: LiDAR-assisted Content-aware Densification for Efficient and Quality 3D Gaussian Splatting](https://arxiv.org/abs/2511.19294v1)**  
  Authors: Phurtivilai Patt, Leyang Huang, Yinqiang Zhang, Yang Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19294v1.pdf)  
  Keywords: ar, efficient, gaussian splatting, semantic, 3d gaussian  
- **[NVGS: Neural Visibility for Occlusion Culling in 3D Gaussian Splatting](https://arxiv.org/abs/2511.19202v1)**  
  Authors: Brent Zoomers, Florian Hahlbohm, Joni Vanherck, Lode Jorissen, Marcus Magnor, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19202v1.pdf)  
  Keywords: ar, vr, efficient, gaussian splatting, 3d gaussian  
- **[MetroGS: Efficient and Stable Reconstruction of Geometrically Accurate High-Fidelity Large-Scale Scenes](https://arxiv.org/abs/2511.19172v1)**  
  Authors: Kehua Chen, Tianlu Mao, Zhuxin Ma, Hao Jiang, Zehao Li, Zihan Liu, Shuqi Gao, Honglong Zhao, Feng Dai, Yucheng Zhang, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19172v1.pdf)  
  Keywords: high-fidelity, ar, geometry, efficient, gaussian splatting, 3d gaussian  
- **[Neural Texture Splatting: Expressive 3D Gaussian Splatting for View Synthesis, Geometry, and Dynamic Reconstruction](https://arxiv.org/abs/2511.18873v1)**  
  Authors: Yiming Wang, Shaofei Wang, Marko Mihajlovic, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18873v1.pdf)  
  Keywords: ar, geometry, dynamic, 4d, efficient, gaussian splatting, 3d gaussian  
- **[Splatonic: Architecture Support for 3D Gaussian Splatting SLAM via Sparse Processing](https://arxiv.org/abs/2511.18755v2)**  
  Authors: Xiaotong Huang, He Zhu, Tianrui Ma, Yuxiang Xiong, Fangxin Liu, Zhezhi He, Yiming Gan, Zihan Liu, Jingwen Leng, Yu Feng, Minyi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18755v2.pdf)  
  Keywords: high-fidelity, ar, efficient, slam, gaussian splatting, 3d gaussian, tracking  

### Quality Enhancement

*Showing the latest 50 out of 188 papers*

- **[MrGS: Multi-modal Radiance Fields with 3D Gaussian Splatting for RGB-Thermal Novel View Synthesis](https://arxiv.org/abs/2511.22997v1)**  
  Authors: Minseong Kweon, Janghyun Kim, Ukcheol Shin, Jinsun Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22997v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, nerf, 3d gaussian  
- **[Can Protective Watermarking Safeguard the Copyright of 3D Gaussian Splatting?](https://arxiv.org/abs/2511.22262v1)**  
  Authors: Wenkai Huang, Yijia Guo, Gaolei Li, Lei Ma, Hang Zhang, Liwen Hu, Jiazheng Wang, Jianhua Li, Tiejun Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22262v1.pdf)  
  Keywords: high-fidelity, ar, 4d, gaussian splatting, 3d gaussian  
- **[IE-SRGS: An Internal-External Knowledge Fusion Framework for High-Fidelity 3D Gaussian Splatting Super-Resolution](https://arxiv.org/abs/2511.22233v1)**  
  Authors: Xiang Feng, Tieshi Zhong, Shuo Chang, Weiliu Wang, Chengkai Wang, Yifei Chen, Yuhe Wang, Zhenzhong Kuang, Xuefei Yin, Yanming Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.22233v1.pdf)  
  Keywords: high-fidelity, ar, geometry, gaussian splatting, 3d gaussian  
- **[Unlocking Zero-shot Potential of Semi-dense Image Matching via Gaussian Splatting](https://arxiv.org/abs/2511.21265v1)**  
  Authors: Juncheng Chen, Chao Xu, Yanjun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21265v1.pdf)  
  Keywords: high-fidelity, ar, geometry, gaussian splatting, 3d gaussian  
- **[STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction](https://arxiv.org/abs/2511.19854v2)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Zidu Wang, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19854v2.pdf)  
  Keywords: high-fidelity, ar, deformation, motion, dynamic, avatar, head, gaussian splatting, 3d gaussian  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: high-fidelity, ar, motion, dynamic, autonomous driving, gaussian splatting, human, 3d gaussian, tracking  
- **[MetroGS: Efficient and Stable Reconstruction of Geometrically Accurate High-Fidelity Large-Scale Scenes](https://arxiv.org/abs/2511.19172v1)**  
  Authors: Kehua Chen, Tianlu Mao, Zhuxin Ma, Hao Jiang, Zehao Li, Zihan Liu, Shuqi Gao, Honglong Zhao, Feng Dai, Yucheng Zhang, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19172v1.pdf)  
  Keywords: high-fidelity, ar, geometry, efficient, gaussian splatting, 3d gaussian  
- **[Splatonic: Architecture Support for 3D Gaussian Splatting SLAM via Sparse Processing](https://arxiv.org/abs/2511.18755v2)**  
  Authors: Xiaotong Huang, He Zhu, Tianrui Ma, Yuxiang Xiong, Fangxin Liu, Zhezhi He, Yiming Gan, Zihan Liu, Jingwen Leng, Yu Feng, Minyi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18755v2.pdf)  
  Keywords: high-fidelity, ar, efficient, slam, gaussian splatting, 3d gaussian, tracking  
- **[Novel View Synthesis from A Few Glimpses via Test-Time Natural Video Completion](https://arxiv.org/abs/2511.17932v1)**  
  Authors: Yan Xu, Yixing Wang, Stella X. Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17932v1.pdf)  
  Keywords: high-fidelity, ar, geometry, gaussian splatting, nerf, 3d gaussian  
- **[One Walk is All You Need: Data-Efficient 3D RF Scene Reconstruction with Human Movements](https://arxiv.org/abs/2511.16966v1)**  
  Authors: Yiheng Bian, Zechen Li, Lanqing Yang, Hao Pan, Yezhou Wang, Longyuan Ge, Jeffery Wu, Ruiheng Liu, Yongjian Fu, Yichao chen, Guangtao xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16966v1.pdf)  
  Keywords: fast, high-fidelity, ar, mapping, motion, geometry, dynamic, efficient, gaussian splatting, human, 3d gaussian  

### Ray Tracing

- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: ar, geometry, ray tracing, reflection, gaussian splatting, illumination  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: ar, geometry, efficient, ray marching, gaussian splatting, 3d gaussian  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: real-time rendering, lighting, face, ar, light transport, ray tracing, efficient, gaussian splatting, shadow, relightable  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: ar, lighting, relighting, light transport, geometry, reflection, efficient, gaussian splatting, global illumination, illumination  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v2)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v2.pdf)  
  Keywords: fast, ar, dynamic, ray tracing, 4d, gaussian splatting  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: high-fidelity, face, lighting, ar, relighting, geometry, ray tracing, reflection, gaussian splatting, nerf, illumination, 3d gaussian  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: face, lighting, ar, relighting, dynamic, gaussian splatting, shadow, global illumination, outdoor, illumination, 3d gaussian, relightable  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: face, lighting, ar, path tracing, dynamic, gaussian splatting, 3d gaussian  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: face, efficient rendering, lighting, relighting, ar, geometry, efficient, ray marching, gaussian splatting, 3d gaussian, relightable  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: high-fidelity, real-time rendering, ar, ray tracing, efficient, gaussian splatting  

### Relighting

*Showing the latest 50 out of 119 papers*

- **[Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes](https://arxiv.org/abs/2511.21367v1)**  
  Authors: Yangle Liu, Fengze Li, Kan Liu, Jieming Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21367v1.pdf)  
  Keywords: ar, motion, geometry, dynamic, lightweight, reflection, 4d, gaussian splatting, nerf  
- **[CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation](https://arxiv.org/abs/2511.17904v1)**  
  Authors: Yuhang Ming, Chenxin Fang, Xingyuan Yu, Fan Zhang, Weichen Dai, Wanzeng Kong, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17904v1.pdf)  
  Keywords: ar, lighting, geometry, dynamic, understanding, compact, gaussian splatting, semantic  
- **[Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction](https://arxiv.org/abs/2511.14540v1)**  
  Authors: Hao Tian, Chenyangguang Zhang, Rui Liu, Wen Shen, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14540v1.pdf)  
  Keywords: ar, lighting, deformation, motion, geometry, dynamic, 4d, gaussian splatting, 3d gaussian  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: high-fidelity, face, ar, sparse-view, geometry, compact, gaussian splatting, illumination, 3d gaussian, 3d reconstruction  
- **[iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion](https://arxiv.org/abs/2511.14149v1)**  
  Authors: Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14149v1.pdf)  
  Keywords: ar, lighting, robotics, head, gaussian splatting, slam, nerf, 3d gaussian, tracking  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: high-fidelity, face, lighting, ar, relighting, geometry, efficient, gaussian splatting, outdoor, semantic, illumination, segmentation  
- **[Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis](https://arxiv.org/abs/2511.13011v1)**  
  Authors: Qingsen Ma, Chen Zou, Dianyun Wang, Jia Wang, Liuyu Xiang, Zhaofeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13011v1.pdf)  
  Keywords: face, ar, geometry, dynamic, gaussian splatting, illumination, 3d gaussian, 3d reconstruction  
- **[Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric](https://arxiv.org/abs/2511.08032v1)**  
  Authors: Zhaolin Wan, Yining Diao, Jingqi Xu, Hao Wang, Zhiyang Li, Xiaopeng Fan, Wangmeng Zuo, Debin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.08032v1.pdf)  
  Keywords: high-fidelity, ar, lighting, gaussian splatting, 3d gaussian  
- **[UltraGS: Gaussian Splatting for Ultrasound Novel View Synthesis](https://arxiv.org/abs/2511.07743v1)**  
  Authors: Yuezhe Yang, Wenjie Cai, Dexin Yang, Yufang Dong, Xingbo Dong, Zhe Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07743v1.pdf)  
  Keywords: lightweight, ar, gaussian splatting, reflection  
- **[Channel Knowledge Map Construction: Recent Advances and Open Challenges](https://arxiv.org/abs/2511.04944v1)**  
  Authors: Zixiang Ren, Juncong Zhou, Jie Xu, Ling Qiu, Yong Zeng, Han Hu, Juyong Zhang, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04944v1.pdf)  
  Keywords: high-fidelity, ar, lighting, efficient, gaussian splatting  

### SLAM

*Showing the latest 50 out of 139 papers*

- **[DiskChunGS: Large-Scale 3D Gaussian SLAM Through Chunk-Based Memory Management](https://arxiv.org/abs/2511.23030v1)**  
  Authors: Casimir Feldmann, Maximum Wilder-Smith, Vaishakh Patil, Michael Oechsle, Michael Niemeyer, Keisuke Tateno, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.23030v1.pdf)  
  Keywords: real-time rendering, face, ar, slam, gaussian splatting, 3d gaussian  
- **[GS-Checker: Tampering Localization for 3D Gaussian Splatting](https://arxiv.org/abs/2511.20354v1)**  
  Authors: Haoliang Han, Ziyuan Luo, Jun Qi, Anderson Rocha, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20354v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, localization  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: high-fidelity, ar, motion, dynamic, autonomous driving, gaussian splatting, human, 3d gaussian, tracking  
- **[Splatonic: Architecture Support for 3D Gaussian Splatting SLAM via Sparse Processing](https://arxiv.org/abs/2511.18755v2)**  
  Authors: Xiaotong Huang, He Zhu, Tianrui Ma, Yuxiang Xiong, Fangxin Liu, Zhezhi He, Yiming Gan, Zihan Liu, Jingwen Leng, Yu Feng, Minyi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18755v2.pdf)  
  Keywords: high-fidelity, ar, efficient, slam, gaussian splatting, 3d gaussian, tracking  
- **[PhysMorph-GS: Differentiable Shape Morphing via Joint Optimization of Physics and Rendering Objectives](https://arxiv.org/abs/2511.16988v1)**  
  Authors: Chang-Yong Song, David Hyde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16988v1.pdf)  
  Keywords: face, deformation, mapping, ar, compact, gaussian splatting, 3d gaussian  
- **[One Walk is All You Need: Data-Efficient 3D RF Scene Reconstruction with Human Movements](https://arxiv.org/abs/2511.16966v1)**  
  Authors: Yiheng Bian, Zechen Li, Lanqing Yang, Hao Pan, Yezhou Wang, Longyuan Ge, Jeffery Wu, Ruiheng Liu, Yongjian Fu, Yichao chen, Guangtao xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16966v1.pdf)  
  Keywords: fast, high-fidelity, ar, mapping, motion, geometry, dynamic, efficient, gaussian splatting, human, 3d gaussian  
- **[Optimizing 3D Gaussian Splattering for Mobile GPUs](https://arxiv.org/abs/2511.16298v1)**  
  Authors: Md Musfiqur Rahman Sanim, Zhihao Shu, Bahram Afsharmanesh, AmirAli Mirian, Jiexiong Guan, Wei Niu, Bin Ren, Gagan Agrawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16298v1.pdf)  
  Keywords: fast, ar, mapping, efficient, gaussian splatting, 3d gaussian  
- **[LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM](https://arxiv.org/abs/2511.16144v1)**  
  Authors: Sibaek Lee, Seongbo Ha, Kyeongsu Kang, Joonyeol Choi, Seungjun Tak, Hyeonwoo Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16144v1.pdf)  
  Keywords: ar, mapping, head, localization, understanding, compact, gaussian splatting, slam, semantic, 3d gaussian, tracking  
- **[Clustered Error Correction with Grouped 4D Gaussian Splatting](https://arxiv.org/abs/2511.16112v1)**  
  Authors: Taeho Kang, Jaeyeon Park, Kyungjin Lee, Youngki Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16112v1.pdf)  
  Keywords: ar, mapping, dynamic, 4d, gaussian splatting  
- **[iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion](https://arxiv.org/abs/2511.14149v1)**  
  Authors: Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14149v1.pdf)  
  Keywords: ar, lighting, robotics, head, gaussian splatting, slam, nerf, 3d gaussian, tracking  

### Scene Understanding

*Showing the latest 50 out of 200 papers*

- **[Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v2)**  
  Authors: Andy Huynh, João Malheiro Silva, Holger Caesar, Tong Duy Son  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20348v2.pdf)  
  Keywords: face, ar, geometry, gaussian splatting, semantic, 3d gaussian, 3d reconstruction  
- **[GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861v1)**  
  Authors: GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu, Kerui Li, Mengyuan Xu, Qiuping Deng, Siting Wang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yankai Wang, Yu Cao, Yifan Chang, Yuan Xu, Yun Ye, Yang Wang, Yukun Zhou, Zhengyuan Zhang, Zhehao Dong, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19861v1.pdf)  
  Keywords: ar, motion, efficient, gaussian splatting, semantic, 3d gaussian  
- **[DensifyBeforehand: LiDAR-assisted Content-aware Densification for Efficient and Quality 3D Gaussian Splatting](https://arxiv.org/abs/2511.19294v1)**  
  Authors: Phurtivilai Patt, Leyang Huang, Yinqiang Zhang, Yang Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19294v1.pdf)  
  Keywords: ar, efficient, gaussian splatting, semantic, 3d gaussian  
- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: ar, geometry, understanding, gaussian splatting, outdoor, 3d gaussian, 3d reconstruction  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: fast, ar, geometry, gaussian splatting, outdoor, semantic  
- **[SegSplat: Feed-forward Gaussian Splatting and Open-Set Semantic Segmentation](https://arxiv.org/abs/2511.18386v1)**  
  Authors: Peter Siegel, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18386v1.pdf)  
  Keywords: ar, understanding, efficient, compact, gaussian splatting, semantic, segmentation, 3d gaussian, 3d reconstruction  
- **[CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation](https://arxiv.org/abs/2511.17904v1)**  
  Authors: Yuhang Ming, Chenxin Fang, Xingyuan Yu, Fan Zhang, Weichen Dai, Wanzeng Kong, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17904v1.pdf)  
  Keywords: ar, lighting, geometry, dynamic, understanding, compact, gaussian splatting, semantic  
- **[FisheyeGaussianLift: BEV Feature Lifting for Surround-View Fisheye Camera Perception](https://arxiv.org/abs/2511.17210v1)**  
  Authors: Shubham Sonarghare, Prasad Deshpande, Ciaran Hogan, Deepika-Rani Kaliappan-Mahalingam, Ganesh Sistu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17210v1.pdf)  
  Keywords: segmentation, ar, 3d gaussian, semantic  
- **[SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting](https://arxiv.org/abs/2511.17092v2)**  
  Authors: Di Wu, Liu Liu, Xueyu Yuan, Qiaojun Yu, Wenxiao Chen, Ruilong Yan, Yiming Tang, Liangtu Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17092v2.pdf)  
  Keywords: few-shot, face, ar, sparse-view, sparse view, gaussian splatting, segmentation, 3d gaussian, 3d reconstruction  
- **[Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling](https://arxiv.org/abs/2511.16301v2)**  
  Authors: Minseok Seo, Mark Hamilton, Changick Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16301v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seominseok0429.github.io/Upsample-Anything/}{https://seominseok0429.github.io/Upsample-Anything/})  
  Keywords: ar, lightweight, gaussian splatting, semantic, segmentation  



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