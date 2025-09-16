# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-09-16 00:48:44

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

- [3DGS Surveys](#3dgs-surveys) (20 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (261 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (994 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (324 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (385 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (70 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (310 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (73 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (414 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (165 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (18 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (114 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (150 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (194 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: survey, lighting, compact, ar, nerf, understanding, segmentation, high-fidelity, gaussian splatting, 3d gaussian, semantic  
- **[A Study of the Framework and Real-World Applications of Language
  Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: survey, ar, nerf, understanding, efficient, robotics, gaussian splatting, 3d gaussian, semantic  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned
  and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: survey, ar, nerf, human, robotics, gaussian splatting, 3d gaussian  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: survey, ar, nerf, 3d reconstruction, geometry, sparse-view, vr, robotics, gaussian splatting, motion, 3d gaussian  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v2)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v2.pdf)  
  Keywords: survey, lighting, ar, nerf, 3d reconstruction, dynamic, human, slam, fast, vr, robotics, gaussian splatting, 3d gaussian  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: survey, outdoor, face, ar, nerf, dynamic, efficient, high-fidelity, gaussian splatting, 3d gaussian, autonomous driving  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: survey, ar, nerf, 3d reconstruction, vr, neural rendering, high-fidelity, robotics, gaussian splatting, 3d gaussian, autonomous driving  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: survey, outdoor, ar, understanding, 3d reconstruction, segmentation, efficient, neural rendering, high-fidelity, gaussian splatting, 3d gaussian, semantic  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: survey, ar, nerf, slam, segmentation, efficient, localization, gaussian splatting, mapping, 3d gaussian, semantic  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to
  Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: survey, ar, dynamic, gaussian splatting, body, motion, 4d, 3d gaussian, understanding  

### Acceleration

*Showing the latest 50 out of 261 papers*

- **[CoRe-GS: Coarse-to-Refined Gaussian Splatting with Semantic Object Focus](https://arxiv.org/abs/2509.04859v1)**  
  Authors: Hannah Schieber, Dominik Frischmann, Simon Boche, Victor Schaack, Angela Schoellig, Stefan Leutenegger, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.04859v1.pdf)  
  Keywords: outdoor, ar, 3d reconstruction, segmentation, fast, efficient, robotics, gaussian splatting, 3d gaussian, semantic  
- **[ContraGS: Codebook-Condensed and Trainable Gaussian Splatting for Fast,
  Memory-Efficient Reconstruction](https://arxiv.org/abs/2509.03775v1)**  
  Authors: Sankeerth Durvasula, Sharanshangar Muhunthan, Zain Moustafa, Richard Chen, Ruofan Liang, Yushi Guan, Nilesh Ahuja, Nilesh Jain, Selvakumar Panneer, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.03775v1.pdf)  
  Keywords: compact, ar, fast, efficient, gaussian splatting, high quality, real-time rendering, 3d gaussian  
- **[GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned
  Residuals](https://arxiv.org/abs/2509.02141v1)**  
  Authors: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.02141v1.pdf)  
  Keywords: face, animation, ar, geometry, fast, lightweight, vr, high-fidelity, gaussian splatting, real-time rendering, head, deformation  
- **[GaussianGAN: Real-Time Photorealistic controllable Human Avatars](https://arxiv.org/abs/2509.01681v1)**  
  Authors: Mohamed Ilyes Lakhal, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01681v1.pdf)  
  Keywords: face, ar, human, segmentation, fast, avatar, neural rendering, gaussian splatting, 4d, semantic  
- **[Towards Integrating Multi-Spectral Imaging with Gaussian Splatting](https://arxiv.org/abs/2509.00989v1)**  
  Authors: Josef Grün, Lukas Meyer, Maximilian Weiherer, Bernhard Egger, Marc Stamminger, Linus Franke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00989v1.pdf)  
  Keywords: compact, ar, 3d reconstruction, geometry, fast, high-fidelity, gaussian splatting, 3d gaussian  
- **[AGS: Accelerating 3D Gaussian Splatting SLAM via CODEC-Assisted Frame
  Covisibility Detection](https://arxiv.org/abs/2509.00433v1)**  
  Authors: Houshu He, Naifeng Jing, Li Jiang, Xiaoyao Liang, Zhuoran Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00433v1.pdf)  
  Keywords: ar, slam, efficient, localization, acceleration, gaussian splatting, tracking, mapping, 3d gaussian  
- **[Scale-GS: Efficient Scalable Gaussian Splatting via Redundancy-filtering
  Training on Streaming Content](https://arxiv.org/abs/2508.21444v1)**  
  Authors: Jiayu Yang, Weijian Su, Songqian Zhang, Yuqi Han, Jinli Suo, Qiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.21444v1.pdf)  
  Keywords: ar, dynamic, deformation, efficient, high-fidelity, gaussian splatting, motion, real-time rendering, head, 3d gaussian  
- **[MAPo : Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for
  High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2508.19786v1)**  
  Authors: Han Jiao, Jiakai Sun, Yexing Xu, Lei Zhao, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19786v1.pdf)  
  Keywords: ar, dynamic, fast, deformation, high-fidelity, gaussian splatting, motion, 3d gaussian  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: face, animation, ar, fast, avatar, high-fidelity, tracking, gaussian splatting, head, 3d gaussian  
- **[LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation](https://arxiv.org/abs/2508.19699v1)**  
  Authors: Yupeng Zhang, Dezhi Zheng, Ping Lu, Han Zhang, Lei Wang, Liping xiang, Cheng Luo, Kaijun Deng, Xiaowen Fu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19699v1.pdf)  
  Keywords: ar, understanding, segmentation, efficient rendering, efficient, high-fidelity, gaussian splatting, 3d gaussian, semantic  

### Applications

*Showing the latest 50 out of 994 papers*

- **[On the Geometric Accuracy of Implicit and Primitive-based
  Representations Derived from View Rendering Constraints](https://arxiv.org/abs/2509.10241v1)**  
  Authors: Elias De Smijter, Renaud Detry, Christophe De Vleeschouwer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10241v1.pdf)  
  Keywords: lighting, compact, ar, geometry, robotics, gaussian splatting  
- **[SplatFill: 3D Scene Inpainting via Depth-Guided Gaussian Splatting](https://arxiv.org/abs/2509.07809v1)**  
  Authors: Mahtab Dahaghin, Milind G. Padalkar, Matteo Toso, Alessio Del Bue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07809v1.pdf)  
  Keywords: ar, nerf, geometry, gaussian splatting, 3d gaussian  
- **[DiGS: Accurate and Complete Surface Reconstruction from 3D Gaussians via
  Direct SDF Learning](https://arxiv.org/abs/2509.07493v1)**  
  Authors: Wenzhi Guo, Bing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07493v1.pdf)  
  Keywords: face, ar, nerf, geometry, gaussian splatting, 3d gaussian  
- **[DreamLifting: A Plug-in Module Lifting MV Diffusion Models for 3D Asset
  Generation](https://arxiv.org/abs/2509.07435v1)**  
  Authors: Ze-Xin Yin, Jiaxiong Qiu, Liu Liu, Xinjie Wang, Wei Sui, Zhizhong Su, Jian Yang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07435v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zx-yin.github.io/dreamlifting/.)  
  Keywords: ar, geometry, efficient, lightweight, gaussian splatting, relightable  
- **[VIM-GS: Visual-Inertial Monocular Gaussian Splatting via Object-level
  Guidance in Large Scenes](https://arxiv.org/abs/2509.06685v3)**  
  Authors: Shengkai Zhang, Yuhe Liu, Guanjun Wu, Jianhua He, Xinggang Wang, Mozi Chen, Kezhong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06685v3.pdf)  
  Keywords: ar, dynamic, large scene, gaussian splatting, motion  
- **[Real-time Photorealistic Mapping for Situational Awareness in Robot
  Teleoperation](https://arxiv.org/abs/2509.06433v1)**  
  Authors: Ian Page, Pierre Susbielle, Olivier Aycard, Pierre-Brice Wieber  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06433v1.pdf)  
  Keywords: ar, slam, efficient, gaussian splatting, mapping, understanding  
- **[3DOF+Quantization: 3DGS quantization for large scenes with limited
  Degrees of Freedom](https://arxiv.org/abs/2509.06400v1)**  
  Authors: Matthieu Gendrin, Stéphane Pateux, Théo Ladune  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06400v1.pdf)  
  Keywords: ar, large scene, 3d gaussian, gaussian splatting  
- **[MEGS$^{2}$: Memory-Efficient Gaussian Splatting via Spherical Gaussians
  and Unified Pruning](https://arxiv.org/abs/2509.07021v1)**  
  Authors: Jiarui Chen, Yikeng Chen, Yingshuang Zou, Ye Huang, Peng Wang, Yuan Liu, Yujing Sun, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07021v1.pdf)  
  Keywords: compression, ar, efficient, lightweight, vr, gaussian splatting, 3d gaussian  
- **[Toward Distributed 3D Gaussian Splatting for High-Resolution Isosurface
  Visualization](https://arxiv.org/abs/2509.05216v1)**  
  Authors: Mengjiao Han, Andres Sewell, Joseph Insley, Janet Knowles, Victor A. Mateevitsi, Michael E. Papka, Steve Petruzza, Silvio Rizzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.05216v1.pdf)  
  Keywords: face, ar, high-fidelity, gaussian splatting, 3d gaussian  
- **[GeoSplat: A Deep Dive into Geometry-Constrained Gaussian Splatting](https://arxiv.org/abs/2509.05075v1)**  
  Authors: Yangming Li, Chaoyu Liu, Lihao Liu, Simon Masnou, Carola-Bibian Schönlieb  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.05075v1.pdf)  
  Keywords: face, ar, geometry, dynamic, efficient, gaussian splatting, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 324 papers*

- **[HairGS: Hair Strand Reconstruction based on 3D Gaussian Splatting](https://arxiv.org/abs/2509.07774v1)**  
  Authors: Yimin Pan, Matthias Nießner, Tobias Kirschstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07774v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimin-pan.github.io/hair-gs/)  
  Keywords: human, geometry, efficient, gaussian splatting, 3d gaussian  
- **[DiGS: Accurate and Complete Surface Reconstruction from 3D Gaussians via
  Direct SDF Learning](https://arxiv.org/abs/2509.07493v1)**  
  Authors: Wenzhi Guo, Bing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07493v1.pdf)  
  Keywords: face, ar, nerf, geometry, gaussian splatting, 3d gaussian  
- **[Toward Distributed 3D Gaussian Splatting for High-Resolution Isosurface
  Visualization](https://arxiv.org/abs/2509.05216v1)**  
  Authors: Mengjiao Han, Andres Sewell, Joseph Insley, Janet Knowles, Victor A. Mateevitsi, Michael E. Papka, Steve Petruzza, Silvio Rizzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.05216v1.pdf)  
  Keywords: face, ar, high-fidelity, gaussian splatting, 3d gaussian  
- **[GeoSplat: A Deep Dive into Geometry-Constrained Gaussian Splatting](https://arxiv.org/abs/2509.05075v1)**  
  Authors: Yangming Li, Chaoyu Liu, Lihao Liu, Simon Masnou, Carola-Bibian Schönlieb  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.05075v1.pdf)  
  Keywords: face, ar, geometry, dynamic, efficient, gaussian splatting, 3d gaussian  
- **[GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned
  Residuals](https://arxiv.org/abs/2509.02141v1)**  
  Authors: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.02141v1.pdf)  
  Keywords: face, animation, ar, geometry, fast, lightweight, vr, high-fidelity, gaussian splatting, real-time rendering, head, deformation  
- **[2D Gaussian Splatting with Semantic Alignment for Image Inpainting](https://arxiv.org/abs/2509.01964v1)**  
  Authors: Hongyu Li, Chaofeng Chen, Xiaoming Li, Guangming Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01964v1.pdf)  
  Keywords: ar, efficient, gaussian splatting, head, semantic  
- **[GaussianGAN: Real-Time Photorealistic controllable Human Avatars](https://arxiv.org/abs/2509.01681v1)**  
  Authors: Mohamed Ilyes Lakhal, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01681v1.pdf)  
  Keywords: face, ar, human, segmentation, fast, avatar, neural rendering, gaussian splatting, 4d, semantic  
- **[Im2Haircut: Single-view Strand-based Hair Reconstruction for Human
  Avatars](https://arxiv.org/abs/2509.01469v1)**  
  Authors: Vanessa Sklyarova, Egor Zakharov, Malte Prinzler, Giorgio Becherini, Michael J. Black, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://im2haircut.is.tue.mpg.de.)  
  Keywords: human, geometry, ar, avatar  
- **[Complete Gaussian Splats from a Single Image with Denoising Diffusion
  Models](https://arxiv.org/abs/2508.21542v1)**  
  Authors: Ziwei Liao, Mohamed Sayed, Steven L. Waslander, Sara Vicente, Daniyar Turmukhambetov, Michael Firman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.21542v1.pdf)  
  Keywords: ar, face, gaussian splatting  
- **[Scale-GS: Efficient Scalable Gaussian Splatting via Redundancy-filtering
  Training on Streaming Content](https://arxiv.org/abs/2508.21444v1)**  
  Authors: Jiayu Yang, Weijian Su, Songqian Zhang, Yuqi Han, Jinli Suo, Qiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.21444v1.pdf)  
  Keywords: ar, dynamic, deformation, efficient, high-fidelity, gaussian splatting, motion, real-time rendering, head, 3d gaussian  

### Dynamic Scene

*Showing the latest 50 out of 385 papers*

- **[VIM-GS: Visual-Inertial Monocular Gaussian Splatting via Object-level
  Guidance in Large Scenes](https://arxiv.org/abs/2509.06685v3)**  
  Authors: Shengkai Zhang, Yuhe Liu, Guanjun Wu, Jianhua He, Xinggang Wang, Mozi Chen, Kezhong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06685v3.pdf)  
  Keywords: ar, dynamic, large scene, gaussian splatting, motion  
- **[GeoSplat: A Deep Dive into Geometry-Constrained Gaussian Splatting](https://arxiv.org/abs/2509.05075v1)**  
  Authors: Yangming Li, Chaoyu Liu, Lihao Liu, Simon Masnou, Carola-Bibian Schönlieb  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.05075v1.pdf)  
  Keywords: face, ar, geometry, dynamic, efficient, gaussian splatting, 3d gaussian  
- **[GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned
  Residuals](https://arxiv.org/abs/2509.02141v1)**  
  Authors: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.02141v1.pdf)  
  Keywords: face, animation, ar, geometry, fast, lightweight, vr, high-fidelity, gaussian splatting, real-time rendering, head, deformation  
- **[GaussianGAN: Real-Time Photorealistic controllable Human Avatars](https://arxiv.org/abs/2509.01681v1)**  
  Authors: Mohamed Ilyes Lakhal, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01681v1.pdf)  
  Keywords: face, ar, human, segmentation, fast, avatar, neural rendering, gaussian splatting, 4d, semantic  
- **[DyPho-SLAM : Real-time Photorealistic SLAM in Dynamic Environments](https://arxiv.org/abs/2509.00741v1)**  
  Authors: Yi Liu, Keyu Fan, Bin Lan, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00741v1.pdf)  
  Keywords: ar, slam, dynamic, efficient, high-fidelity, localization, tracking, gaussian splatting, mapping  
- **[Scale-GS: Efficient Scalable Gaussian Splatting via Redundancy-filtering
  Training on Streaming Content](https://arxiv.org/abs/2508.21444v1)**  
  Authors: Jiayu Yang, Weijian Su, Songqian Zhang, Yuqi Han, Jinli Suo, Qiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.21444v1.pdf)  
  Keywords: ar, dynamic, deformation, efficient, high-fidelity, gaussian splatting, motion, real-time rendering, head, 3d gaussian  
- **[AvatarBack: Back-Head Generation for Complete 3D Avatars from Front-View
  Images](https://arxiv.org/abs/2508.20623v1)**  
  Authors: Shiqi Xin, Xiaolin Zhang, Yanbin Liu, Peng Zhang, Caifeng Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20623v1.pdf)  
  Keywords: ar, avatar, gaussian splatting, motion, head, 3d gaussian  
- **[MAPo : Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for
  High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2508.19786v1)**  
  Authors: Han Jiao, Jiakai Sun, Yexing Xu, Lei Zhao, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19786v1.pdf)  
  Keywords: ar, dynamic, fast, deformation, high-fidelity, gaussian splatting, motion, 3d gaussian  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: face, animation, ar, fast, avatar, high-fidelity, tracking, gaussian splatting, head, 3d gaussian  
- **[Style4D-Bench: A Benchmark Suite for 4D Stylization](https://arxiv.org/abs/2508.19243v1)**  
  Authors: Beiqi Chen, Shuai Shao, Haitang Feng, Jianhuang Lai, Jianlou Si, Guangcong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19243v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://becky-catherine.github.io/Style4D)  
  Keywords: ar, geometry, dynamic, lightweight, gaussian splatting, motion, 4d  

### Few-shot

*Showing the latest 50 out of 70 papers*

- **[${C}^{3}$-GS: Learning Context-aware, Cross-dimension, Cross-scale
  Feature for Generalizable Gaussian Splatting](https://arxiv.org/abs/2508.20754v1)**  
  Authors: Yuxi Hu, Jun Zhang, Kuangyi Chen, Zhe Zhang, Friedrich Fraundorfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20754v1.pdf)  
  Keywords: ar, geometry, sparse view, lightweight, gaussian splatting  
- **[MeshSplat: Generalizable Sparse-View Surface Reconstruction via Gaussian
  Splatting](https://arxiv.org/abs/2508.17811v1)**  
  Authors: Hanzhi Chang, Ruijie Zhu, Wenjie Chang, Mulin Yu, Yanzhe Liang, Jiahao Lu, Zhuoyuan Li, Tianzhu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17811v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanzhichang.github.io/meshsplat_web)  
  Keywords: face, ar, geometry, sparse-view, gaussian splatting  
- **[Enhancing Novel View Synthesis from extremely sparse views with SfM-free
  3D Gaussian Splatting Framework](https://arxiv.org/abs/2508.15457v1)**  
  Authors: Zongqi He, Hanmin Li, Kin-Chung Chan, Yushen Zuo, Hao Xie, Zhe Xiao, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15457v1.pdf)  
  Keywords: ar, geometry, sparse view, sparse-view, gaussian splatting, motion, 3d gaussian  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v2)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v2.pdf)  
  Keywords: face, lighting, outdoor, relighting, ar, geometry, sparse view, gaussian splatting, 3d gaussian, autonomous driving  
- **[Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.12720v2)**  
  Authors: Kangjie Chen, Yingji Zhong, Zhihao Li, Jiaqi Lin, Youyu Chen, Minghan Qin, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12720v2.pdf)  
  Keywords: ar, sparse-view, lightweight, gaussian splatting, 3d gaussian, understanding  
- **[Toward Human-Robot Teaming: Learning Handover Behaviors from 3D Scenes](https://arxiv.org/abs/2508.09855v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09855v1.pdf)  
  Keywords: human, ar, sparse-view, gaussian splatting  
- **[GSFixer: Improving 3D Gaussian Splatting with Reference-Guided Video
  Diffusion Priors](https://arxiv.org/abs/2508.09667v1)**  
  Authors: Xingyilang Yin, Qi Zhang, Jiahao Chang, Ying Feng, Qingnan Fan, Xi Yang, Chi-Man Pun, Huaqi Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09667v1.pdf)  
  Keywords: ar, 3d reconstruction, sparse view, geometry, sparse-view, gaussian splatting, 3d gaussian, semantic  
- **[SkySplat: Generalizable 3D Gaussian Splatting from Multi-Temporal Sparse
  Satellite Images](https://arxiv.org/abs/2508.09479v1)**  
  Authors: Xuejun Huang, Xinyi Liu, Yi Wan, Zhi Zheng, Bin Zhang, Mingtao Xiong, Yingying Pei, Yongjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09479v1.pdf)  
  Keywords: ar, sparse-view, efficient, gaussian splatting, 3d gaussian  
- **[DIP-GS: Deep Image Prior For Gaussian Splatting Sparse View Recovery](https://arxiv.org/abs/2508.07372v1)**  
  Authors: Rajaei Khatib, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07372v1.pdf)  
  Keywords: ar, sparse view, sparse-view, gaussian splatting, real-time rendering, 3d gaussian  
- **[UGOD: Uncertainty-Guided Differentiable Opacity and Soft Dropout for
  Enhanced Sparse-View 3DGS](https://arxiv.org/abs/2508.04968v1)**  
  Authors: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Liangxiu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04968v1.pdf)  
  Keywords: ar, nerf, sparse-view, gaussian splatting, 3d gaussian  

### Geometry Reconstruction

*Showing the latest 50 out of 310 papers*

- **[On the Geometric Accuracy of Implicit and Primitive-based
  Representations Derived from View Rendering Constraints](https://arxiv.org/abs/2509.10241v1)**  
  Authors: Elias De Smijter, Renaud Detry, Christophe De Vleeschouwer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10241v1.pdf)  
  Keywords: lighting, compact, ar, geometry, robotics, gaussian splatting  
- **[SplatFill: 3D Scene Inpainting via Depth-Guided Gaussian Splatting](https://arxiv.org/abs/2509.07809v1)**  
  Authors: Mahtab Dahaghin, Milind G. Padalkar, Matteo Toso, Alessio Del Bue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07809v1.pdf)  
  Keywords: ar, nerf, geometry, gaussian splatting, 3d gaussian  
- **[HairGS: Hair Strand Reconstruction based on 3D Gaussian Splatting](https://arxiv.org/abs/2509.07774v1)**  
  Authors: Yimin Pan, Matthias Nießner, Tobias Kirschstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07774v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimin-pan.github.io/hair-gs/)  
  Keywords: human, geometry, efficient, gaussian splatting, 3d gaussian  
- **[DiGS: Accurate and Complete Surface Reconstruction from 3D Gaussians via
  Direct SDF Learning](https://arxiv.org/abs/2509.07493v1)**  
  Authors: Wenzhi Guo, Bing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07493v1.pdf)  
  Keywords: face, ar, nerf, geometry, gaussian splatting, 3d gaussian  
- **[DreamLifting: A Plug-in Module Lifting MV Diffusion Models for 3D Asset
  Generation](https://arxiv.org/abs/2509.07435v1)**  
  Authors: Ze-Xin Yin, Jiaxiong Qiu, Liu Liu, Xinjie Wang, Wei Sui, Zhizhong Su, Jian Yang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07435v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zx-yin.github.io/dreamlifting/.)  
  Keywords: ar, geometry, efficient, lightweight, gaussian splatting, relightable  
- **[GeoSplat: A Deep Dive into Geometry-Constrained Gaussian Splatting](https://arxiv.org/abs/2509.05075v1)**  
  Authors: Yangming Li, Chaoyu Liu, Lihao Liu, Simon Masnou, Carola-Bibian Schönlieb  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.05075v1.pdf)  
  Keywords: face, ar, geometry, dynamic, efficient, gaussian splatting, 3d gaussian  
- **[CoRe-GS: Coarse-to-Refined Gaussian Splatting with Semantic Object Focus](https://arxiv.org/abs/2509.04859v1)**  
  Authors: Hannah Schieber, Dominik Frischmann, Simon Boche, Victor Schaack, Angela Schoellig, Stefan Leutenegger, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.04859v1.pdf)  
  Keywords: outdoor, ar, 3d reconstruction, segmentation, fast, efficient, robotics, gaussian splatting, 3d gaussian, semantic  
- **[GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned
  Residuals](https://arxiv.org/abs/2509.02141v1)**  
  Authors: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.02141v1.pdf)  
  Keywords: face, animation, ar, geometry, fast, lightweight, vr, high-fidelity, gaussian splatting, real-time rendering, head, deformation  
- **[Im2Haircut: Single-view Strand-based Hair Reconstruction for Human
  Avatars](https://arxiv.org/abs/2509.01469v1)**  
  Authors: Vanessa Sklyarova, Egor Zakharov, Malte Prinzler, Giorgio Becherini, Michael J. Black, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://im2haircut.is.tue.mpg.de.)  
  Keywords: human, geometry, ar, avatar  
- **[Towards Integrating Multi-Spectral Imaging with Gaussian Splatting](https://arxiv.org/abs/2509.00989v1)**  
  Authors: Josef Grün, Lukas Meyer, Maximilian Weiherer, Bernhard Egger, Marc Stamminger, Linus Franke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00989v1.pdf)  
  Keywords: compact, ar, 3d reconstruction, geometry, fast, high-fidelity, gaussian splatting, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 73 papers*

- **[VIM-GS: Visual-Inertial Monocular Gaussian Splatting via Object-level
  Guidance in Large Scenes](https://arxiv.org/abs/2509.06685v3)**  
  Authors: Shengkai Zhang, Yuhe Liu, Guanjun Wu, Jianhua He, Xinggang Wang, Mozi Chen, Kezhong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06685v3.pdf)  
  Keywords: ar, dynamic, large scene, gaussian splatting, motion  
- **[3DOF+Quantization: 3DGS quantization for large scenes with limited
  Degrees of Freedom](https://arxiv.org/abs/2509.06400v1)**  
  Authors: Matthieu Gendrin, Stéphane Pateux, Théo Ladune  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06400v1.pdf)  
  Keywords: ar, large scene, 3d gaussian, gaussian splatting  
- **[CoRe-GS: Coarse-to-Refined Gaussian Splatting with Semantic Object Focus](https://arxiv.org/abs/2509.04859v1)**  
  Authors: Hannah Schieber, Dominik Frischmann, Simon Boche, Victor Schaack, Angela Schoellig, Stefan Leutenegger, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.04859v1.pdf)  
  Keywords: outdoor, ar, 3d reconstruction, segmentation, fast, efficient, robotics, gaussian splatting, 3d gaussian, semantic  
- **[GSVisLoc: Generalizable Visual Localization for Gaussian Splatting Scene
  Representations](https://arxiv.org/abs/2508.18242v1)**  
  Authors: Fadi Khatib, Dror Moran, Guy Trostianetsky, Yoni Kasten, Meirav Galun, Ronen Basri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18242v1.pdf)  
  Keywords: outdoor, ar, localization, gaussian splatting, 3d gaussian  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v2)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v2.pdf)  
  Keywords: face, lighting, outdoor, relighting, ar, geometry, sparse view, gaussian splatting, 3d gaussian, autonomous driving  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: lighting, outdoor, ar, understanding, 3d reconstruction, gaussian splatting, 3d gaussian, illumination  
- **[Online 3D Gaussian Splatting Modeling with Novel View Selection](https://arxiv.org/abs/2508.14014v2)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14014v2.pdf)  
  Keywords: outdoor, ar, slam, gaussian splatting, 3d gaussian  
- **[InstDrive: Instance-Aware 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2508.12015v1)**  
  Authors: Hongyuan Liu, Haochen Yu, Jianfei Jiang, Qiankun Liu, Jiansheng Chen, Huimin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12015v1.pdf)  
  Keywords: outdoor, ar, dynamic, segmentation, lightweight, autonomous driving, gaussian splatting, 3d gaussian, understanding  
- **[Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.11431v1)**  
  Authors: Simona Kocour, Assia Benbihi, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11431v1.pdf)  
  Keywords: face, outdoor, ar, understanding, 3d reconstruction, geometry, gaussian splatting, 3d gaussian, semantic  
- **[Multi-view Normal and Distance Guidance Gaussian Splatting for Surface
  Reconstruction](https://arxiv.org/abs/2508.07701v2)**  
  Authors: Bo Jia, Yanan Guo, Ying Chang, Benkui Zhang, Ying Xie, Kangning Du, Lin Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07701v2.pdf)  
  Keywords: face, outdoor, ar, geometry, gaussian splatting, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 414 papers*

- **[On the Geometric Accuracy of Implicit and Primitive-based
  Representations Derived from View Rendering Constraints](https://arxiv.org/abs/2509.10241v1)**  
  Authors: Elias De Smijter, Renaud Detry, Christophe De Vleeschouwer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10241v1.pdf)  
  Keywords: lighting, compact, ar, geometry, robotics, gaussian splatting  
- **[HairGS: Hair Strand Reconstruction based on 3D Gaussian Splatting](https://arxiv.org/abs/2509.07774v1)**  
  Authors: Yimin Pan, Matthias Nießner, Tobias Kirschstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07774v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimin-pan.github.io/hair-gs/)  
  Keywords: human, geometry, efficient, gaussian splatting, 3d gaussian  
- **[DreamLifting: A Plug-in Module Lifting MV Diffusion Models for 3D Asset
  Generation](https://arxiv.org/abs/2509.07435v1)**  
  Authors: Ze-Xin Yin, Jiaxiong Qiu, Liu Liu, Xinjie Wang, Wei Sui, Zhizhong Su, Jian Yang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07435v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zx-yin.github.io/dreamlifting/.)  
  Keywords: ar, geometry, efficient, lightweight, gaussian splatting, relightable  
- **[Real-time Photorealistic Mapping for Situational Awareness in Robot
  Teleoperation](https://arxiv.org/abs/2509.06433v1)**  
  Authors: Ian Page, Pierre Susbielle, Olivier Aycard, Pierre-Brice Wieber  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06433v1.pdf)  
  Keywords: ar, slam, efficient, gaussian splatting, mapping, understanding  
- **[MEGS$^{2}$: Memory-Efficient Gaussian Splatting via Spherical Gaussians
  and Unified Pruning](https://arxiv.org/abs/2509.07021v1)**  
  Authors: Jiarui Chen, Yikeng Chen, Yingshuang Zou, Ye Huang, Peng Wang, Yuan Liu, Yujing Sun, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07021v1.pdf)  
  Keywords: compression, ar, efficient, lightweight, vr, gaussian splatting, 3d gaussian  
- **[GeoSplat: A Deep Dive into Geometry-Constrained Gaussian Splatting](https://arxiv.org/abs/2509.05075v1)**  
  Authors: Yangming Li, Chaoyu Liu, Lihao Liu, Simon Masnou, Carola-Bibian Schönlieb  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.05075v1.pdf)  
  Keywords: face, ar, geometry, dynamic, efficient, gaussian splatting, 3d gaussian  
- **[CoRe-GS: Coarse-to-Refined Gaussian Splatting with Semantic Object Focus](https://arxiv.org/abs/2509.04859v1)**  
  Authors: Hannah Schieber, Dominik Frischmann, Simon Boche, Victor Schaack, Angela Schoellig, Stefan Leutenegger, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.04859v1.pdf)  
  Keywords: outdoor, ar, 3d reconstruction, segmentation, fast, efficient, robotics, gaussian splatting, 3d gaussian, semantic  
- **[ContraGS: Codebook-Condensed and Trainable Gaussian Splatting for Fast,
  Memory-Efficient Reconstruction](https://arxiv.org/abs/2509.03775v1)**  
  Authors: Sankeerth Durvasula, Sharanshangar Muhunthan, Zain Moustafa, Richard Chen, Ruofan Liang, Yushi Guan, Nilesh Ahuja, Nilesh Jain, Selvakumar Panneer, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.03775v1.pdf)  
  Keywords: compact, ar, fast, efficient, gaussian splatting, high quality, real-time rendering, 3d gaussian  
- **[GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned
  Residuals](https://arxiv.org/abs/2509.02141v1)**  
  Authors: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.02141v1.pdf)  
  Keywords: face, animation, ar, geometry, fast, lightweight, vr, high-fidelity, gaussian splatting, real-time rendering, head, deformation  
- **[2D Gaussian Splatting with Semantic Alignment for Image Inpainting](https://arxiv.org/abs/2509.01964v1)**  
  Authors: Hongyu Li, Chaofeng Chen, Xiaoming Li, Guangming Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01964v1.pdf)  
  Keywords: ar, efficient, gaussian splatting, head, semantic  

### Quality Enhancement

*Showing the latest 50 out of 165 papers*

- **[Toward Distributed 3D Gaussian Splatting for High-Resolution Isosurface
  Visualization](https://arxiv.org/abs/2509.05216v1)**  
  Authors: Mengjiao Han, Andres Sewell, Joseph Insley, Janet Knowles, Victor A. Mateevitsi, Michael E. Papka, Steve Petruzza, Silvio Rizzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.05216v1.pdf)  
  Keywords: face, ar, high-fidelity, gaussian splatting, 3d gaussian  
- **[ContraGS: Codebook-Condensed and Trainable Gaussian Splatting for Fast,
  Memory-Efficient Reconstruction](https://arxiv.org/abs/2509.03775v1)**  
  Authors: Sankeerth Durvasula, Sharanshangar Muhunthan, Zain Moustafa, Richard Chen, Ruofan Liang, Yushi Guan, Nilesh Ahuja, Nilesh Jain, Selvakumar Panneer, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.03775v1.pdf)  
  Keywords: compact, ar, fast, efficient, gaussian splatting, high quality, real-time rendering, 3d gaussian  
- **[GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned
  Residuals](https://arxiv.org/abs/2509.02141v1)**  
  Authors: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.02141v1.pdf)  
  Keywords: face, animation, ar, geometry, fast, lightweight, vr, high-fidelity, gaussian splatting, real-time rendering, head, deformation  
- **[Towards Integrating Multi-Spectral Imaging with Gaussian Splatting](https://arxiv.org/abs/2509.00989v1)**  
  Authors: Josef Grün, Lukas Meyer, Maximilian Weiherer, Bernhard Egger, Marc Stamminger, Linus Franke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00989v1.pdf)  
  Keywords: compact, ar, 3d reconstruction, geometry, fast, high-fidelity, gaussian splatting, 3d gaussian  
- **[SWAGSplatting: Semantic-guided Water-scene Augmented Gaussian Splatting](https://arxiv.org/abs/2509.00800v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00800v1.pdf)  
  Keywords: ar, nerf, 3d reconstruction, understanding, high-fidelity, gaussian splatting, 3d gaussian, semantic  
- **[DyPho-SLAM : Real-time Photorealistic SLAM in Dynamic Environments](https://arxiv.org/abs/2509.00741v1)**  
  Authors: Yi Liu, Keyu Fan, Bin Lan, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00741v1.pdf)  
  Keywords: ar, slam, dynamic, efficient, high-fidelity, localization, tracking, gaussian splatting, mapping  
- **[Scale-GS: Efficient Scalable Gaussian Splatting via Redundancy-filtering
  Training on Streaming Content](https://arxiv.org/abs/2508.21444v1)**  
  Authors: Jiayu Yang, Weijian Su, Songqian Zhang, Yuqi Han, Jinli Suo, Qiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.21444v1.pdf)  
  Keywords: ar, dynamic, deformation, efficient, high-fidelity, gaussian splatting, motion, real-time rendering, head, 3d gaussian  
- **[MAPo : Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for
  High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2508.19786v1)**  
  Authors: Han Jiao, Jiakai Sun, Yexing Xu, Lei Zhao, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19786v1.pdf)  
  Keywords: ar, dynamic, fast, deformation, high-fidelity, gaussian splatting, motion, 3d gaussian  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: face, animation, ar, fast, avatar, high-fidelity, tracking, gaussian splatting, head, 3d gaussian  
- **[LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation](https://arxiv.org/abs/2508.19699v1)**  
  Authors: Yupeng Zhang, Dezhi Zheng, Ping Lu, Han Zhang, Lei Wang, Liping xiang, Cheng Luo, Kaijun Deng, Xiaowen Fu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19699v1.pdf)  
  Keywords: ar, understanding, segmentation, efficient rendering, efficient, high-fidelity, gaussian splatting, 3d gaussian, semantic  

### Ray Tracing

- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: face, lighting, relighting, ar, nerf, ray tracing, geometry, high-fidelity, gaussian splatting, reflection, 3d gaussian, illumination  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: face, global illumination, lighting, relighting, shadow, outdoor, ar, dynamic, gaussian splatting, relightable, 3d gaussian, illumination  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: face, lighting, ar, dynamic, gaussian splatting, path tracing, 3d gaussian  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: face, lighting, relighting, ar, geometry, efficient rendering, efficient, gaussian splatting, relightable, 3d gaussian, ray marching  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: ar, ray tracing, efficient, high-fidelity, gaussian splatting, real-time rendering  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v2)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v2.pdf)  
  Keywords: lighting, shadow, relighting, ar, ray tracing, geometry, human, fast, avatar, gaussian splatting, relightable  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: lighting, relighting, ar, ray tracing, efficient rendering, efficient, acceleration, gaussian splatting, 3d gaussian  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: animation, compact, ar, dynamic, efficient, acceleration, gaussian splatting, 3d gaussian, ray marching  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: face, global illumination, lighting, ar, ray tracing, efficient, gaussian splatting, real-time rendering, 3d gaussian, illumination  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: shadow, ar, ray tracing, fast, neural rendering, gaussian splatting, reflection, 3d gaussian  

### Relighting

*Showing the latest 50 out of 114 papers*

- **[On the Geometric Accuracy of Implicit and Primitive-based
  Representations Derived from View Rendering Constraints](https://arxiv.org/abs/2509.10241v1)**  
  Authors: Elias De Smijter, Renaud Detry, Christophe De Vleeschouwer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10241v1.pdf)  
  Keywords: lighting, compact, ar, geometry, robotics, gaussian splatting  
- **[DreamLifting: A Plug-in Module Lifting MV Diffusion Models for 3D Asset
  Generation](https://arxiv.org/abs/2509.07435v1)**  
  Authors: Ze-Xin Yin, Jiaxiong Qiu, Liu Liu, Xinjie Wang, Wei Sui, Zhizhong Su, Jian Yang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07435v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zx-yin.github.io/dreamlifting/.)  
  Keywords: ar, geometry, efficient, lightweight, gaussian splatting, relightable  
- **[ColorGS: High-fidelity Surgical Scene Reconstruction with Colored
  Gaussian Splatting](https://arxiv.org/abs/2508.18696v1)**  
  Authors: Qun Ji, Peng Li, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18696v1.pdf)  
  Keywords: lighting, ar, nerf, dynamic, deformation, efficient, vr, high-fidelity, gaussian splatting, motion, real-time rendering, 3d gaussian  
- **[Fiducial Marker Splatting for High-Fidelity Robotics Simulations](https://arxiv.org/abs/2508.17012v1)**  
  Authors: Diram Tabaa, Gianni Di Caro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17012v1.pdf)  
  Keywords: lighting, ar, efficient, neural rendering, high-fidelity, localization, robotics, gaussian splatting  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v2)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v2.pdf)  
  Keywords: face, lighting, outdoor, relighting, ar, geometry, sparse view, gaussian splatting, 3d gaussian, autonomous driving  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: face, lighting, relighting, ar, nerf, ray tracing, geometry, high-fidelity, gaussian splatting, reflection, 3d gaussian, illumination  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: lighting, outdoor, ar, understanding, 3d reconstruction, gaussian splatting, 3d gaussian, illumination  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: survey, lighting, compact, ar, nerf, understanding, segmentation, high-fidelity, gaussian splatting, 3d gaussian, semantic  
- **[HumanGenesis: Agent-Based Geometric and Generative Modeling for
  Synthetic Human Dynamics](https://arxiv.org/abs/2508.09858v1)**  
  Authors: Weiqi Li, Zehao Zhang, Liang Lin, Guangrun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09858v1.pdf)  
  Keywords: face, ar, human, dynamic, deformation, gaussian splatting, motion, 4d, reflection, 3d gaussian  
- **[Vision-Only Gaussian Splatting for Collaborative Semantic Occupancy
  Prediction](https://arxiv.org/abs/2508.10936v1)**  
  Authors: Cheng Chen, Hao Huang, Saurabh Bagchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.10936v1.pdf)  
  Keywords: lighting, ar, geometry, gaussian splatting, semantic  

### SLAM

*Showing the latest 50 out of 150 papers*

- **[Real-time Photorealistic Mapping for Situational Awareness in Robot
  Teleoperation](https://arxiv.org/abs/2509.06433v1)**  
  Authors: Ian Page, Pierre Susbielle, Olivier Aycard, Pierre-Brice Wieber  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06433v1.pdf)  
  Keywords: ar, slam, efficient, gaussian splatting, mapping, understanding  
- **[DyPho-SLAM : Real-time Photorealistic SLAM in Dynamic Environments](https://arxiv.org/abs/2509.00741v1)**  
  Authors: Yi Liu, Keyu Fan, Bin Lan, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00741v1.pdf)  
  Keywords: ar, slam, dynamic, efficient, high-fidelity, localization, tracking, gaussian splatting, mapping  
- **[AGS: Accelerating 3D Gaussian Splatting SLAM via CODEC-Assisted Frame
  Covisibility Detection](https://arxiv.org/abs/2509.00433v1)**  
  Authors: Houshu He, Naifeng Jing, Li Jiang, Xiaoyao Liang, Zhuoran Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00433v1.pdf)  
  Keywords: ar, slam, efficient, localization, acceleration, gaussian splatting, tracking, mapping, 3d gaussian  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: face, animation, ar, fast, avatar, high-fidelity, tracking, gaussian splatting, head, 3d gaussian  
- **[PseudoMapTrainer: Learning Online Mapping without HD Maps](https://arxiv.org/abs/2508.18788v1)**  
  Authors: Christian Löwens, Thorben Funke, Jingchao Xie, Alexandru Paul Condurache  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18788v1.pdf)  
  Keywords: face, ar, segmentation, gaussian splatting, mapping, semantic  
- **[GSVisLoc: Generalizable Visual Localization for Gaussian Splatting Scene
  Representations](https://arxiv.org/abs/2508.18242v1)**  
  Authors: Fadi Khatib, Dror Moran, Guy Trostianetsky, Yoni Kasten, Meirav Galun, Ronen Basri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18242v1.pdf)  
  Keywords: outdoor, ar, localization, gaussian splatting, 3d gaussian  
- **[Fiducial Marker Splatting for High-Fidelity Robotics Simulations](https://arxiv.org/abs/2508.17012v1)**  
  Authors: Diram Tabaa, Gianni Di Caro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17012v1.pdf)  
  Keywords: lighting, ar, efficient, neural rendering, high-fidelity, localization, robotics, gaussian splatting  
- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: compact, ar, 3d reconstruction, geometry, efficient, tracking, gaussian splatting, motion, 3d gaussian  
- **[Online 3D Gaussian Splatting Modeling with Novel View Selection](https://arxiv.org/abs/2508.14014v2)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14014v2.pdf)  
  Keywords: outdoor, ar, slam, gaussian splatting, 3d gaussian  
- **[SAGOnline: Segment Any Gaussians Online](https://arxiv.org/abs/2508.08219v1)**  
  Authors: Wentao Sun, Quanyun Wu, Hanqing Xu, Kyle Gao, Zhengsen Xu, Yiping Chen, Dedong Zhang, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08219v1.pdf)  
  Keywords: ar, nerf, segmentation, efficient, lightweight, vr, tracking, gaussian splatting, real-time rendering, 3d gaussian, understanding  

### Scene Understanding

*Showing the latest 50 out of 194 papers*

- **[Real-time Photorealistic Mapping for Situational Awareness in Robot
  Teleoperation](https://arxiv.org/abs/2509.06433v1)**  
  Authors: Ian Page, Pierre Susbielle, Olivier Aycard, Pierre-Brice Wieber  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06433v1.pdf)  
  Keywords: ar, slam, efficient, gaussian splatting, mapping, understanding  
- **[CoRe-GS: Coarse-to-Refined Gaussian Splatting with Semantic Object Focus](https://arxiv.org/abs/2509.04859v1)**  
  Authors: Hannah Schieber, Dominik Frischmann, Simon Boche, Victor Schaack, Angela Schoellig, Stefan Leutenegger, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.04859v1.pdf)  
  Keywords: outdoor, ar, 3d reconstruction, segmentation, fast, efficient, robotics, gaussian splatting, 3d gaussian, semantic  
- **[SSGaussian: Semantic-Aware and Structure-Preserving 3D Style Transfer](https://arxiv.org/abs/2509.04379v1)**  
  Authors: Jimin Xu, Bosheng Qin, Tao Jin, Zhou Zhao, Zhenhui Ye, Jun Yu, Fei Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.04379v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jm-xu.github.io/SSGaussian)  
  Keywords: ar, semantic, 3d gaussian, gaussian splatting  
- **[2D Gaussian Splatting with Semantic Alignment for Image Inpainting](https://arxiv.org/abs/2509.01964v1)**  
  Authors: Hongyu Li, Chaofeng Chen, Xiaoming Li, Guangming Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01964v1.pdf)  
  Keywords: ar, efficient, gaussian splatting, head, semantic  
- **[GaussianGAN: Real-Time Photorealistic controllable Human Avatars](https://arxiv.org/abs/2509.01681v1)**  
  Authors: Mohamed Ilyes Lakhal, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01681v1.pdf)  
  Keywords: face, ar, human, segmentation, fast, avatar, neural rendering, gaussian splatting, 4d, semantic  
- **[SWAGSplatting: Semantic-guided Water-scene Augmented Gaussian Splatting](https://arxiv.org/abs/2509.00800v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00800v1.pdf)  
  Keywords: ar, nerf, 3d reconstruction, understanding, high-fidelity, gaussian splatting, 3d gaussian, semantic  
- **[MarkSplatter: Generalizable Watermarking for 3D Gaussian Splatting Model
  via Splatter Image Structure](https://arxiv.org/abs/2509.00757v1)**  
  Authors: Xiufeng Huang, Ziyuan Luo, Qi Song, Ruofei Wang, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00757v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kevinhuangxf.github.io/marksplatter.)  
  Keywords: ar, segmentation, efficient, gaussian splatting, 3d gaussian  
- **[LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation](https://arxiv.org/abs/2508.19699v1)**  
  Authors: Yupeng Zhang, Dezhi Zheng, Ping Lu, Han Zhang, Lei Wang, Liping xiang, Cheng Luo, Kaijun Deng, Xiaowen Fu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19699v1.pdf)  
  Keywords: ar, understanding, segmentation, efficient rendering, efficient, high-fidelity, gaussian splatting, 3d gaussian, semantic  
- **[PseudoMapTrainer: Learning Online Mapping without HD Maps](https://arxiv.org/abs/2508.18788v1)**  
  Authors: Christian Löwens, Thorben Funke, Jingchao Xie, Alexandru Paul Condurache  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18788v1.pdf)  
  Keywords: face, ar, segmentation, gaussian splatting, mapping, semantic  
- **[GWM: Towards Scalable Gaussian World Models for Robotic Manipulation](https://arxiv.org/abs/2508.17600v1)**  
  Authors: Guanxing Lu, Baoxiong Jia, Puhao Li, Yixin Chen, Ziwei Wang, Yansong Tang, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17600v1.pdf)  
  Keywords: understanding, ar, gaussian splatting  



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