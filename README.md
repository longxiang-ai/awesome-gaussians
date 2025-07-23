# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-07-23 00:59:04

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

- [3DGS Surveys](#3dgs-surveys) (18 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (276 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (330 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (400 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (72 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (319 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (62 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (395 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (161 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (17 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (112 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (156 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (191 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v1)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, survey, lighting, ar, slam, robotics, vr, nerf, dynamic, 3d gaussian, human, fast  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: autonomous driving, gaussian splatting, face, survey, ar, efficient, high-fidelity, nerf, dynamic, 3d gaussian, outdoor  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: autonomous driving, 3d reconstruction, gaussian splatting, survey, ar, neural rendering, robotics, high-fidelity, nerf, vr, 3d gaussian  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: understanding, 3d reconstruction, gaussian splatting, survey, ar, neural rendering, efficient, segmentation, high-fidelity, 3d gaussian, semantic, outdoor  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: localization, gaussian splatting, survey, ar, efficient, slam, segmentation, nerf, 3d gaussian, semantic, mapping  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to
  Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: motion, understanding, gaussian splatting, survey, 4d, ar, body, dynamic, 3d gaussian  
- **[A Survey of 3D Reconstruction with Event Cameras](https://arxiv.org/abs/2505.08438v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v2.pdf)  
  Keywords: illumination, motion, 3d reconstruction, autonomous driving, gaussian splatting, survey, geometry, ar, neural rendering, robotics, nerf, dynamic, 3d gaussian  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, survey, ar, efficient, fast  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d reconstruction, survey, lighting, ar, 3d gaussian  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From
  Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting
  (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf)  
  Keywords: understanding, 3d reconstruction, gaussian splatting, face, survey, geometry, ar, nerf, 3d gaussian, outdoor, sparse view  

### Acceleration

*Showing the latest 50 out of 276 papers*

- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relighting, gaussian splatting, face, lighting, geometry, ar, efficient, efficient rendering, ray marching, 3d gaussian, relightable  
- **[GCC: A 3DGS Inference Architecture with Gaussian-Wise and Cross-Stage
  Conditional Processing](https://arxiv.org/abs/2507.15300v2)**  
  Authors: Minnan Pei, Gang Li, Junwen Si, Zeyu Zhu, Zitao Mo, Peisong Wang, Zhuoran Song, Xiaoyao Liang, Jian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15300v2.pdf)  
  Keywords: gaussian splatting, ar, neural rendering, efficient, head, compact, high-fidelity, dynamic, 3d gaussian, fast  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v1)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, survey, lighting, ar, slam, robotics, vr, nerf, dynamic, 3d gaussian, human, fast  
- **[Neural-GASh: A CGA-based neural radiance prediction pipeline for
  real-time shading](https://arxiv.org/abs/2507.13917v1)**  
  Authors: Efstratios Geronikolakis, Manos Kamarianakis, Antonis Protopsaltis, George Papagiannakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13917v1.pdf)  
  Keywords: light transport, ar, efficient, vr, dynamic, 3d gaussian, fast  
- **[TexGS-VolVis: Expressive Scene Editing for Volume Visualization via
  Textured Gaussian Splatting](https://arxiv.org/abs/2507.13586v1)**  
  Authors: Kaiyuan Tang, Kuangshi Ai, Jun Han, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13586v1.pdf)  
  Keywords: gaussian splatting, lighting, geometry, ar, segmentation, 3d gaussian, real-time rendering  
- **[ScaffoldAvatar: High-Fidelity Gaussian Avatars with Patch Expressions](https://arxiv.org/abs/2507.10542v1)**  
  Authors: Shivangi Aneja, Sebastian Weiss, Irene Baeza, Prashanth Chandran, Gaspard Zoss, Matthias Nießner, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.10542v1.pdf)  
  Keywords: motion, gaussian splatting, face, ar, head, avatar, high-fidelity, dynamic, 3d gaussian, human, fast  
- **[Enhancing non-Rigid 3D Model Deformations Using Mesh-based Gaussian
  Splatting](https://arxiv.org/abs/2507.07000v1)**  
  Authors: Wijayathunga W. M. R. D. B  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07000v1.pdf)  
  Keywords: gaussian splatting, face, ar, animation, deformation, 3d gaussian, fast  
- **[FlexGaussian: Flexible and Cost-Effective Training-Free Compression for
  3D Gaussian Splatting](https://arxiv.org/abs/2507.06671v1)**  
  Authors: Boyuan Tian, Qizhe Gao, Siran Xianyu, Xiaotong Cui, Minjia Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06671v1.pdf)  
  Keywords: gaussian splatting, ar, compression, 3d gaussian, fast  
- **[LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+
  FPS](https://arxiv.org/abs/2507.07136v1)**  
  Authors: Wanhua Li, Yujie Zhao, Minghan Qin, Yang Liu, Yuanhao Cai, Chuang Gan, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07136v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://langsplat-v2.github.io.)  
  Keywords: gaussian splatting, ar, efficient, high quality, semantic, fast  
- **[A3FR: Agile 3D Gaussian Splatting with Incremental Gaze Tracked Foveated
  Rendering in Virtual Reality](https://arxiv.org/abs/2507.04147v1)**  
  Authors: Shuo Xin, Haiyu Wang, Sai Qian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.04147v1.pdf)  
  Keywords: tracking, gaussian splatting, face, ar, neural rendering, efficient, head, efficient rendering, vr, dynamic, 3d gaussian, human  

### Applications

*Showing the latest 50 out of 995 papers*

- **[Appearance Harmonization via Bilateral Grid Prediction with Transformers
  for 3DGS](https://arxiv.org/abs/2507.15748v1)**  
  Authors: Jisu Shin, Richard Shaw, Seunghyun Shin, Anton Pelykh, Zhensong Zhang, Hae-Gon Jeon, Eduardo Perez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15748v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian  
- **[DWTGS: Rethinking Frequency Regularization for Sparse-view 3D Gaussian
  Splatting](https://arxiv.org/abs/2507.15690v1)**  
  Authors: Hung Nguyen, Runfa Li, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15690v1.pdf)  
  Keywords: sparse-view, ar, gaussian splatting, 3d gaussian  
- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: localization, motion, gaussian splatting, face, geometry, ar, compact, dynamic, 3d gaussian, semantic  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relighting, gaussian splatting, face, lighting, geometry, ar, efficient, efficient rendering, ray marching, 3d gaussian, relightable  
- **[SurfaceSplat: Connecting Surface Reconstruction and Gaussian Splatting](https://arxiv.org/abs/2507.15602v1)**  
  Authors: Zihui Gao, Jia-Wang Bian, Guosheng Lin, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15602v1.pdf)  
  Keywords: sparse-view, gaussian splatting, face, geometry, ar, 3d gaussian  
- **[ObjectGS: Object-aware Scene Reconstruction and Scene Understanding via
  Gaussian Splatting](https://arxiv.org/abs/2507.15454v1)**  
  Authors: Ruijie Zhu, Mulin Yu, Linning Xu, Lihan Jiang, Yixuan Li, Tianzhu Zhang, Jiangmiao Pang, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15454v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ruijiezhu94.github.io/ObjectGS_page)  
  Keywords: understanding, gaussian splatting, ar, segmentation, high-fidelity, dynamic, 3d gaussian, semantic  
- **[GCC: A 3DGS Inference Architecture with Gaussian-Wise and Cross-Stage
  Conditional Processing](https://arxiv.org/abs/2507.15300v2)**  
  Authors: Minnan Pei, Gang Li, Junwen Si, Zeyu Zhu, Zitao Mo, Peisong Wang, Zhuoran Song, Xiaoyao Liang, Jian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15300v2.pdf)  
  Keywords: gaussian splatting, ar, neural rendering, efficient, head, compact, high-fidelity, dynamic, 3d gaussian, fast  
- **[Stereo-GS: Multi-View Stereo Vision Model for Generalizable 3D Gaussian
  Splatting Reconstruction](https://arxiv.org/abs/2507.14921v1)**  
  Authors: Xiufeng Huang, Ka Chun Cheung, Runmin Cong, Simon See, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14921v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, geometry, ar, efficient, head, 3d gaussian  
- **[DCHM: Depth-Consistent Human Modeling for Multiview Detection](https://arxiv.org/abs/2507.14505v1)**  
  Authors: Jiahao Ma, Tianyu Wang, Miaomiao Liu, David Ahmedt-Aristizabal, Chuong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14505v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiahao-ma.github.io/DCHM/}{project)  
  Keywords: sparse-view, localization, gaussian splatting, ar, segmentation, human  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v1)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, survey, lighting, ar, slam, robotics, vr, nerf, dynamic, 3d gaussian, human, fast  

### Avatar Generation

*Showing the latest 50 out of 330 papers*

- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: localization, motion, gaussian splatting, face, geometry, ar, compact, dynamic, 3d gaussian, semantic  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relighting, gaussian splatting, face, lighting, geometry, ar, efficient, efficient rendering, ray marching, 3d gaussian, relightable  
- **[SurfaceSplat: Connecting Surface Reconstruction and Gaussian Splatting](https://arxiv.org/abs/2507.15602v1)**  
  Authors: Zihui Gao, Jia-Wang Bian, Guosheng Lin, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15602v1.pdf)  
  Keywords: sparse-view, gaussian splatting, face, geometry, ar, 3d gaussian  
- **[GCC: A 3DGS Inference Architecture with Gaussian-Wise and Cross-Stage
  Conditional Processing](https://arxiv.org/abs/2507.15300v2)**  
  Authors: Minnan Pei, Gang Li, Junwen Si, Zeyu Zhu, Zitao Mo, Peisong Wang, Zhuoran Song, Xiaoyao Liang, Jian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15300v2.pdf)  
  Keywords: gaussian splatting, ar, neural rendering, efficient, head, compact, high-fidelity, dynamic, 3d gaussian, fast  
- **[Stereo-GS: Multi-View Stereo Vision Model for Generalizable 3D Gaussian
  Splatting Reconstruction](https://arxiv.org/abs/2507.14921v1)**  
  Authors: Xiufeng Huang, Ka Chun Cheung, Runmin Cong, Simon See, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14921v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, geometry, ar, efficient, head, 3d gaussian  
- **[DCHM: Depth-Consistent Human Modeling for Multiview Detection](https://arxiv.org/abs/2507.14505v1)**  
  Authors: Jiahao Ma, Tianyu Wang, Miaomiao Liu, David Ahmedt-Aristizabal, Chuong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14505v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiahao-ma.github.io/DCHM/}{project)  
  Keywords: sparse-view, localization, gaussian splatting, ar, segmentation, human  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v1)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, survey, lighting, ar, slam, robotics, vr, nerf, dynamic, 3d gaussian, human, fast  
- **[Dark-EvGS: Event Camera as an Eye for Radiance Field in the Dark](https://arxiv.org/abs/2507.11931v1)**  
  Authors: Jingqian Wu, Peiqi Duan, Zongqiang Wang, Changwei Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11931v1.pdf)  
  Keywords: motion, gaussian splatting, face, ar, dynamic, 3d gaussian  
- **[Wavelet-GS: 3D Gaussian Splatting with Wavelet Decomposition](https://arxiv.org/abs/2507.12498v2)**  
  Authors: Beizhen Zhao, Yifan Zhou, Sicheng Yu, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12498v2.pdf)  
  Keywords: gaussian splatting, face, lighting, ar, 3d gaussian  
- **[A Mixed-Primitive-based Gaussian Splatting Method for Surface
  Reconstruction](https://arxiv.org/abs/2507.11321v1)**  
  Authors: Haoxuan Qu, Yujun Cai, Hossein Rahmani, Ajay Kumar, Junsong Yuan, Jun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11321v1.pdf)  
  Keywords: ar, high quality, gaussian splatting, face  

### Dynamic Scene

*Showing the latest 50 out of 400 papers*

- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: localization, motion, gaussian splatting, face, geometry, ar, compact, dynamic, 3d gaussian, semantic  
- **[ObjectGS: Object-aware Scene Reconstruction and Scene Understanding via
  Gaussian Splatting](https://arxiv.org/abs/2507.15454v1)**  
  Authors: Ruijie Zhu, Mulin Yu, Linning Xu, Lihan Jiang, Yixuan Li, Tianzhu Zhang, Jiangmiao Pang, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15454v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ruijiezhu94.github.io/ObjectGS_page)  
  Keywords: understanding, gaussian splatting, ar, segmentation, high-fidelity, dynamic, 3d gaussian, semantic  
- **[GCC: A 3DGS Inference Architecture with Gaussian-Wise and Cross-Stage
  Conditional Processing](https://arxiv.org/abs/2507.15300v2)**  
  Authors: Minnan Pei, Gang Li, Junwen Si, Zeyu Zhu, Zitao Mo, Peisong Wang, Zhuoran Song, Xiaoyao Liang, Jian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15300v2.pdf)  
  Keywords: gaussian splatting, ar, neural rendering, efficient, head, compact, high-fidelity, dynamic, 3d gaussian, fast  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v1)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, survey, lighting, ar, slam, robotics, vr, nerf, dynamic, 3d gaussian, human, fast  
- **[Adaptive 3D Gaussian Splatting Video Streaming: Visual Saliency-Aware
  Tiling and Meta-Learning-Based Bitrate Adaptation](https://arxiv.org/abs/2507.14454v1)**  
  Authors: Han Gong, Qiyue Li, Jie Li, Zhi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14454v1.pdf)  
  Keywords: deformation, ar, gaussian splatting, 3d gaussian  
- **[Adaptive 3D Gaussian Splatting Video Streaming](https://arxiv.org/abs/2507.14432v1)**  
  Authors: Han Gong, Qiyue Li, Zhi Liu, Hao Zhou, Peng Yuan Zhou, Zhu Li, Jie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14432v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, deformation, compression, 3d gaussian  
- **[Neural-GASh: A CGA-based neural radiance prediction pipeline for
  real-time shading](https://arxiv.org/abs/2507.13917v1)**  
  Authors: Efstratios Geronikolakis, Manos Kamarianakis, Antonis Protopsaltis, George Papagiannakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13917v1.pdf)  
  Keywords: light transport, ar, efficient, vr, dynamic, 3d gaussian, fast  
- **[VolSegGS: Segmentation and Tracking in Dynamic Volumetric Scenes via
  Deformable 3D Gaussians](https://arxiv.org/abs/2507.12667v1)**  
  Authors: Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12667v1.pdf)  
  Keywords: tracking, gaussian splatting, ar, segmentation, dynamic, deformation, 3d gaussian  
- **[BRUM: Robust 3D Vehicle Reconstruction from 360 Sparse Images](https://arxiv.org/abs/2507.12095v1)**  
  Authors: Davide Di Nucci, Matteo Tomei, Guido Borghi, Luca Ciuffreda, Roberto Vezzani, Rita Cucchiara  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12095v1.pdf)  
  Keywords: sparse-view, motion, 3d reconstruction, gaussian splatting, ar  
- **[Dark-EvGS: Event Camera as an Eye for Radiance Field in the Dark](https://arxiv.org/abs/2507.11931v1)**  
  Authors: Jingqian Wu, Peiqi Duan, Zongqiang Wang, Changwei Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11931v1.pdf)  
  Keywords: motion, gaussian splatting, face, ar, dynamic, 3d gaussian  

### Few-shot

*Showing the latest 50 out of 72 papers*

- **[DWTGS: Rethinking Frequency Regularization for Sparse-view 3D Gaussian
  Splatting](https://arxiv.org/abs/2507.15690v1)**  
  Authors: Hung Nguyen, Runfa Li, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15690v1.pdf)  
  Keywords: sparse-view, ar, gaussian splatting, 3d gaussian  
- **[SurfaceSplat: Connecting Surface Reconstruction and Gaussian Splatting](https://arxiv.org/abs/2507.15602v1)**  
  Authors: Zihui Gao, Jia-Wang Bian, Guosheng Lin, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15602v1.pdf)  
  Keywords: sparse-view, gaussian splatting, face, geometry, ar, 3d gaussian  
- **[DCHM: Depth-Consistent Human Modeling for Multiview Detection](https://arxiv.org/abs/2507.14505v1)**  
  Authors: Jiahao Ma, Tianyu Wang, Miaomiao Liu, David Ahmedt-Aristizabal, Chuong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14505v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiahao-ma.github.io/DCHM/}{project)  
  Keywords: sparse-view, localization, gaussian splatting, ar, segmentation, human  
- **[BRUM: Robust 3D Vehicle Reconstruction from 360 Sparse Images](https://arxiv.org/abs/2507.12095v1)**  
  Authors: Davide Di Nucci, Matteo Tomei, Guido Borghi, Luca Ciuffreda, Roberto Vezzani, Rita Cucchiara  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12095v1.pdf)  
  Keywords: sparse-view, motion, 3d reconstruction, gaussian splatting, ar  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: sparse-view, understanding, gaussian splatting, face, reflection, geometry, ar, dynamic, sparse view  
- **[Learning human-to-robot handovers through 3D scene reconstruction](https://arxiv.org/abs/2507.08726v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08726v1.pdf)  
  Keywords: sparse-view, ar, human, gaussian splatting  
- **[RegGS: Unposed Sparse Views Gaussian Splatting with 3DGS Registration](https://arxiv.org/abs/2507.08136v2)**  
  Authors: Chong Cheng, Yu Hu, Sicheng Yu, Beizhen Zhao, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08136v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/reggs/.)  
  Keywords: gaussian splatting, geometry, ar, efficient, 3d gaussian, sparse view  
- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from
  RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: sparse-view, motion, gaussian splatting, ar, dynamic  
- **[PointGS: Point Attention-Aware Sparse View Synthesis with Gaussian
  Splatting](https://arxiv.org/abs/2506.10335v1)**  
  Authors: Lintao Xiang, Hongpei Zheng, Yating Huang, Qijun Yang, Hujun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.10335v1.pdf)  
  Keywords: gaussian splatting, lightweight, ar, nerf, few-shot, 3d gaussian, sparse view  
- **[UniForward: Unified 3D Scene and Semantic Field Reconstruction via
  Feed-Forward Gaussian Splatting from Only Sparse-View Images](https://arxiv.org/abs/2506.09378v1)**  
  Authors: Qijian Tian, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09378v1.pdf)  
  Keywords: sparse-view, understanding, gaussian splatting, ar, segmentation, 3d gaussian, semantic  

### Geometry Reconstruction

*Showing the latest 50 out of 319 papers*

- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: localization, motion, gaussian splatting, face, geometry, ar, compact, dynamic, 3d gaussian, semantic  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relighting, gaussian splatting, face, lighting, geometry, ar, efficient, efficient rendering, ray marching, 3d gaussian, relightable  
- **[SurfaceSplat: Connecting Surface Reconstruction and Gaussian Splatting](https://arxiv.org/abs/2507.15602v1)**  
  Authors: Zihui Gao, Jia-Wang Bian, Guosheng Lin, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15602v1.pdf)  
  Keywords: sparse-view, gaussian splatting, face, geometry, ar, 3d gaussian  
- **[Stereo-GS: Multi-View Stereo Vision Model for Generalizable 3D Gaussian
  Splatting Reconstruction](https://arxiv.org/abs/2507.14921v1)**  
  Authors: Xiufeng Huang, Ka Chun Cheung, Runmin Cong, Simon See, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14921v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, geometry, ar, efficient, head, 3d gaussian  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v1)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, survey, lighting, ar, slam, robotics, vr, nerf, dynamic, 3d gaussian, human, fast  
- **[TexGS-VolVis: Expressive Scene Editing for Volume Visualization via
  Textured Gaussian Splatting](https://arxiv.org/abs/2507.13586v1)**  
  Authors: Kaiyuan Tang, Kuangshi Ai, Jun Han, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13586v1.pdf)  
  Keywords: gaussian splatting, lighting, geometry, ar, segmentation, 3d gaussian, real-time rendering  
- **[BRUM: Robust 3D Vehicle Reconstruction from 360 Sparse Images](https://arxiv.org/abs/2507.12095v1)**  
  Authors: Davide Di Nucci, Matteo Tomei, Guido Borghi, Luca Ciuffreda, Roberto Vezzani, Rita Cucchiara  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12095v1.pdf)  
  Keywords: sparse-view, motion, 3d reconstruction, gaussian splatting, ar  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: sparse-view, understanding, gaussian splatting, face, reflection, geometry, ar, dynamic, sparse view  
- **[Robust 3D-Masked Part-level Editing in 3D Gaussian Splatting with
  Regularized Score Distillation Sampling](https://arxiv.org/abs/2507.11061v2)**  
  Authors: Hayeon Kim, Ji Ha Jang, Se Young Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11061v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://janeyeon.github.io/romap.)  
  Keywords: gaussian splatting, geometry, ar, efficient, slam, segmentation, 3d gaussian  
- **[3DGAA: Realistic and Robust 3D Gaussian-based Adversarial Attack for
  Autonomous Driving](https://arxiv.org/abs/2507.09993v2)**  
  Authors: Yixun Zhang, Lizhi Wang, Junjun Zhao, Wending Zhao, Feng Zhou, Yonghao Dang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.09993v2.pdf)  
  Keywords: autonomous driving, gaussian splatting, geometry, ar, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 62 papers*

- **[MUVOD: A Novel Multi-view Video Object Segmentation Dataset and A
  Benchmark for 3D Segmentation](https://arxiv.org/abs/2507.07519v1)**  
  Authors: Bangning Wei, Joshua Maraval, Meriem Outtas, Kidiyo Kpalma, Nicolas Ramin, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07519v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://volumetric-repository.labs.b-com.com/#/muvod.)  
  Keywords: motion, understanding, gaussian splatting, 4d, ar, segmentation, dynamic, nerf, 3d gaussian, outdoor  
- **[3DGS_LSR:Large_Scale Relocation for Autonomous Driving Based on 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.05661v1)**  
  Authors: Haitao Lu, Haijier Chen, Haoze Liu, Shoujian Zhang, Bo Xu, Ziao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05661v1.pdf)  
  Keywords: localization, autonomous driving, gaussian splatting, ar, outdoor, 3d gaussian, mapping  
- **[ArmGS: Composite Gaussian Appearance Refinement for Modeling Dynamic
  Urban Environments](https://arxiv.org/abs/2507.03886v1)**  
  Authors: Guile Wu, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.03886v1.pdf)  
  Keywords: autonomous driving, gaussian splatting, urban scene, ar, high-fidelity, dynamic, 3d gaussian, real-time rendering  
- **[Outdoor Monocular SLAM with Global Scale-Consistent 3D Gaussian
  Pointmaps](https://arxiv.org/abs/2507.03737v1)**  
  Authors: Chong Cheng, Sicheng Yu, Zijian Wang, Yifan Zhou, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.03737v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/S3PO-GS/.)  
  Keywords: mapping, tracking, gaussian splatting, ar, slam, high-fidelity, dynamic, 3d gaussian, outdoor  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: illumination, mapping, tracking, gaussian splatting, lighting, geometry, ar, slam, high-fidelity, dynamic, 3d gaussian, outdoor  
- **[BézierGS: Dynamic Urban Scene Reconstruction with Bézier Curve
  Gaussian Splatting](https://arxiv.org/abs/2506.22099v3)**  
  Authors: Zipei Ma, Junzhe Jiang, Yurui Chen, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22099v3.pdf)  
  Keywords: motion, autonomous driving, gaussian splatting, urban scene, ar, dynamic  
- **[ICP-3DGS: SfM-free 3D Gaussian Splatting for Large-scale Unbounded
  Scenes](https://arxiv.org/abs/2506.21629v1)**  
  Authors: Chenhao Zhang, Yezhi Shen, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21629v1.pdf)  
  Keywords: motion, gaussian splatting, ar, neural rendering, nerf, 3d gaussian, outdoor  
- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: tracking, gaussian splatting, ar, slam, 3d gaussian, outdoor  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: autonomous driving, gaussian splatting, face, survey, ar, efficient, high-fidelity, nerf, dynamic, 3d gaussian, outdoor  
- **[Multiview Geometric Regularization of Gaussian Splatting for Accurate
  Radiance Fields](https://arxiv.org/abs/2506.13508v1)**  
  Authors: Jungeon Kim, Geonsoo Park, Seungyong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13508v1.pdf)  
  Keywords: gaussian splatting, geometry, ar, 3d gaussian, outdoor  

### Model Compression

*Showing the latest 50 out of 395 papers*

- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: localization, motion, gaussian splatting, face, geometry, ar, compact, dynamic, 3d gaussian, semantic  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relighting, gaussian splatting, face, lighting, geometry, ar, efficient, efficient rendering, ray marching, 3d gaussian, relightable  
- **[GCC: A 3DGS Inference Architecture with Gaussian-Wise and Cross-Stage
  Conditional Processing](https://arxiv.org/abs/2507.15300v2)**  
  Authors: Minnan Pei, Gang Li, Junwen Si, Zeyu Zhu, Zitao Mo, Peisong Wang, Zhuoran Song, Xiaoyao Liang, Jian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15300v2.pdf)  
  Keywords: gaussian splatting, ar, neural rendering, efficient, head, compact, high-fidelity, dynamic, 3d gaussian, fast  
- **[Stereo-GS: Multi-View Stereo Vision Model for Generalizable 3D Gaussian
  Splatting Reconstruction](https://arxiv.org/abs/2507.14921v1)**  
  Authors: Xiufeng Huang, Ka Chun Cheung, Runmin Cong, Simon See, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14921v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, geometry, ar, efficient, head, 3d gaussian  
- **[Adaptive 3D Gaussian Splatting Video Streaming](https://arxiv.org/abs/2507.14432v1)**  
  Authors: Han Gong, Qiyue Li, Zhi Liu, Hao Zhou, Peng Yuan Zhou, Zhu Li, Jie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14432v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, deformation, compression, 3d gaussian  
- **[Neural-GASh: A CGA-based neural radiance prediction pipeline for
  real-time shading](https://arxiv.org/abs/2507.13917v1)**  
  Authors: Efstratios Geronikolakis, Manos Kamarianakis, Antonis Protopsaltis, George Papagiannakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13917v1.pdf)  
  Keywords: light transport, ar, efficient, vr, dynamic, 3d gaussian, fast  
- **[Robust 3D-Masked Part-level Editing in 3D Gaussian Splatting with
  Regularized Score Distillation Sampling](https://arxiv.org/abs/2507.11061v2)**  
  Authors: Hayeon Kim, Ji Ha Jang, Se Young Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11061v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://janeyeon.github.io/romap.)  
  Keywords: gaussian splatting, geometry, ar, efficient, slam, segmentation, 3d gaussian  
- **[RegGS: Unposed Sparse Views Gaussian Splatting with 3DGS Registration](https://arxiv.org/abs/2507.08136v2)**  
  Authors: Chong Cheng, Yu Hu, Sicheng Yu, Beizhen Zhao, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08136v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/reggs/.)  
  Keywords: gaussian splatting, geometry, ar, efficient, 3d gaussian, sparse view  
- **[RTR-GS: 3D Gaussian Splatting for Inverse Rendering with Radiance
  Transfer and Reflection](https://arxiv.org/abs/2507.07733v1)**  
  Authors: Yongyang Zhou, Fang-Lue Zhang, Zichen Wang, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07733v1.pdf)  
  Keywords: relighting, gaussian splatting, lighting, reflection, ar, efficient, 3d gaussian  
- **[SD-GS: Structured Deformable 3D Gaussians for Efficient Dynamic Scene
  Reconstruction](https://arxiv.org/abs/2507.07465v1)**  
  Authors: Wei Yao, Shuzhao Xie, Letian Li, Weixiang Zhang, Zhixin Lai, Shiqi Dai, Ke Zhang, Zhi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07465v1.pdf)  
  Keywords: motion, gaussian splatting, 4d, ar, efficient, compact, dynamic, deformation, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 161 papers*

- **[ObjectGS: Object-aware Scene Reconstruction and Scene Understanding via
  Gaussian Splatting](https://arxiv.org/abs/2507.15454v1)**  
  Authors: Ruijie Zhu, Mulin Yu, Linning Xu, Lihan Jiang, Yixuan Li, Tianzhu Zhang, Jiangmiao Pang, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15454v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ruijiezhu94.github.io/ObjectGS_page)  
  Keywords: understanding, gaussian splatting, ar, segmentation, high-fidelity, dynamic, 3d gaussian, semantic  
- **[GCC: A 3DGS Inference Architecture with Gaussian-Wise and Cross-Stage
  Conditional Processing](https://arxiv.org/abs/2507.15300v2)**  
  Authors: Minnan Pei, Gang Li, Junwen Si, Zeyu Zhu, Zitao Mo, Peisong Wang, Zhuoran Song, Xiaoyao Liang, Jian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15300v2.pdf)  
  Keywords: gaussian splatting, ar, neural rendering, efficient, head, compact, high-fidelity, dynamic, 3d gaussian, fast  
- **[A Mixed-Primitive-based Gaussian Splatting Method for Surface
  Reconstruction](https://arxiv.org/abs/2507.11321v1)**  
  Authors: Haoxuan Qu, Yujun Cai, Hossein Rahmani, Ajay Kumar, Junsong Yuan, Jun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11321v1.pdf)  
  Keywords: ar, high quality, gaussian splatting, face  
- **[ScaffoldAvatar: High-Fidelity Gaussian Avatars with Patch Expressions](https://arxiv.org/abs/2507.10542v1)**  
  Authors: Shivangi Aneja, Sebastian Weiss, Irene Baeza, Prashanth Chandran, Gaspard Zoss, Matthias Nießner, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.10542v1.pdf)  
  Keywords: motion, gaussian splatting, face, ar, head, avatar, high-fidelity, dynamic, 3d gaussian, human, fast  
- **[LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+
  FPS](https://arxiv.org/abs/2507.07136v1)**  
  Authors: Wanhua Li, Yujie Zhao, Minghan Qin, Yang Liu, Yuanhao Cai, Chuang Gan, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07136v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://langsplat-v2.github.io.)  
  Keywords: gaussian splatting, ar, efficient, high quality, semantic, fast  
- **[LighthouseGS: Indoor Structure-aware 3D Gaussian Splatting for
  Panorama-Style Mobile Captures](https://arxiv.org/abs/2507.06109v1)**  
  Authors: Seungoh Han, Jaehoon Jang, Hyunsu Kim, Jaeheung Surh, Junhyung Kwak, Hyowon Ha, Kyungdon Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06109v1.pdf)  
  Keywords: motion, gaussian splatting, geometry, ar, high-fidelity, 3d gaussian  
- **[VisualSpeaker: Visually-Guided 3D Avatar Lip Synthesis](https://arxiv.org/abs/2507.06060v2)**  
  Authors: Alexandre Symeonidis-Herzig, Özge Mercanoğlu Sincan, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06060v2.pdf)  
  Keywords: gaussian splatting, ar, animation, avatar, high-fidelity, recognition, 3d gaussian, human  
- **[D-FCGS: Feedforward Compression of Dynamic Gaussian Splatting for
  Free-Viewpoint Videos](https://arxiv.org/abs/2507.05859v1)**  
  Authors: Wenkang Zhang, Yan Zhao, Qiang Wang, Li Song, Zhengxue Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05859v1.pdf)  
  Keywords: motion, gaussian splatting, ar, efficient, high-fidelity, dynamic, compression, 3d gaussian  
- **[DreamArt: Generating Interactable Articulated Objects from a Single
  Image](https://arxiv.org/abs/2507.05763v1)**  
  Authors: Ruijie Lu, Yu Liu, Jiaxiang Tang, Junfeng Ni, Yuxiang Wang, Diwen Wan, Gang Zeng, Yixin Chen, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05763v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dream-art-0.github.io/DreamArt/.)  
  Keywords: motion, gaussian splatting, face, geometry, ar, segmentation, high-fidelity, nerf, vr  
- **[SegmentDreamer: Towards High-fidelity Text-to-3D Synthesis with
  Segmented Consistency Trajectory Distillation](https://arxiv.org/abs/2507.05256v1)**  
  Authors: Jiahao Zhu, Zixuan Chen, Guangcong Wang, Xiaohua Xie, Yi Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05256v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, 3d gaussian  

### Ray Tracing

- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relighting, gaussian splatting, face, lighting, geometry, ar, efficient, efficient rendering, ray marching, 3d gaussian, relightable  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, high-fidelity, ray tracing, real-time rendering  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: relighting, gaussian splatting, lighting, shadow, geometry, ar, avatar, human, ray tracing, fast, relightable  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: relighting, gaussian splatting, acceleration, lighting, ar, efficient, efficient rendering, 3d gaussian, ray tracing  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: gaussian splatting, acceleration, ar, efficient, animation, compact, dynamic, ray marching, 3d gaussian  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: illumination, gaussian splatting, global illumination, lighting, face, ar, efficient, 3d gaussian, ray tracing, real-time rendering  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: gaussian splatting, reflection, ar, neural rendering, 3d gaussian, ray tracing, fast, shadow  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: gaussian splatting, face, lighting, reflection, ray tracing, shadow  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation
  Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, survey, ar, 3d gaussian, ray tracing  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: light transport, gaussian splatting, acceleration, reflection, ar, efficient, ray tracing  

### Relighting

*Showing the latest 50 out of 112 papers*

- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relighting, gaussian splatting, face, lighting, geometry, ar, efficient, efficient rendering, ray marching, 3d gaussian, relightable  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v1)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, survey, lighting, ar, slam, robotics, vr, nerf, dynamic, 3d gaussian, human, fast  
- **[Neural-GASh: A CGA-based neural radiance prediction pipeline for
  real-time shading](https://arxiv.org/abs/2507.13917v1)**  
  Authors: Efstratios Geronikolakis, Manos Kamarianakis, Antonis Protopsaltis, George Papagiannakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13917v1.pdf)  
  Keywords: light transport, ar, efficient, vr, dynamic, 3d gaussian, fast  
- **[TexGS-VolVis: Expressive Scene Editing for Volume Visualization via
  Textured Gaussian Splatting](https://arxiv.org/abs/2507.13586v1)**  
  Authors: Kaiyuan Tang, Kuangshi Ai, Jun Han, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13586v1.pdf)  
  Keywords: gaussian splatting, lighting, geometry, ar, segmentation, 3d gaussian, real-time rendering  
- **[Wavelet-GS: 3D Gaussian Splatting with Wavelet Decomposition](https://arxiv.org/abs/2507.12498v2)**  
  Authors: Beizhen Zhao, Yifan Zhou, Sicheng Yu, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12498v2.pdf)  
  Keywords: gaussian splatting, face, lighting, ar, 3d gaussian  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: sparse-view, understanding, gaussian splatting, face, reflection, geometry, ar, dynamic, sparse view  
- **[RTR-GS: 3D Gaussian Splatting for Inverse Rendering with Radiance
  Transfer and Reflection](https://arxiv.org/abs/2507.07733v1)**  
  Authors: Yongyang Zhou, Fang-Lue Zhang, Zichen Wang, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07733v1.pdf)  
  Keywords: relighting, gaussian splatting, lighting, reflection, ar, efficient, 3d gaussian  
- **[Seg-Wild: Interactive Segmentation based on 3D Gaussian Splatting for
  Unconstrained Image Collections](https://arxiv.org/abs/2507.07395v1)**  
  Authors: Yongtang Bao, Chengjie Tang, Yuze Wang, Haojie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07395v1.pdf)  
  Keywords: gaussian splatting, lighting, ar, segmentation, 3d gaussian  
- **[Reflections Unlock: Geometry-Aware Reflection Disentanglement in 3D
  Gaussian Splatting for Photorealistic Scenes Rendering](https://arxiv.org/abs/2507.06103v1)**  
  Authors: Jiayi Song, Zihan Ye, Qingyuan Zhou, Weidong Yang, Ben Fei, Jingyi Xu, Ying He, Wanli Ouyang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06103v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ref-unlock.github.io/.)  
  Keywords: gaussian splatting, face, reflection, geometry, ar, efficient, nerf, 3d gaussian  
- **[HyperGaussians: High-Dimensional Gaussian Splatting for High-Fidelity
  Animatable Face Avatars](https://arxiv.org/abs/2507.02803v2)**  
  Authors: Gent Serifi, Marcel C. Bühler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02803v2.pdf)  
  Keywords: gaussian splatting, face, lighting, reflection, ar, avatar, high-fidelity, deformation, 3d gaussian, fast  

### SLAM

*Showing the latest 50 out of 156 papers*

- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: localization, motion, gaussian splatting, face, geometry, ar, compact, dynamic, 3d gaussian, semantic  
- **[DCHM: Depth-Consistent Human Modeling for Multiview Detection](https://arxiv.org/abs/2507.14505v1)**  
  Authors: Jiahao Ma, Tianyu Wang, Miaomiao Liu, David Ahmedt-Aristizabal, Chuong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14505v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiahao-ma.github.io/DCHM/}{project)  
  Keywords: sparse-view, localization, gaussian splatting, ar, segmentation, human  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v1)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, survey, lighting, ar, slam, robotics, vr, nerf, dynamic, 3d gaussian, human, fast  
- **[VolSegGS: Segmentation and Tracking in Dynamic Volumetric Scenes via
  Deformable 3D Gaussians](https://arxiv.org/abs/2507.12667v1)**  
  Authors: Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12667v1.pdf)  
  Keywords: tracking, gaussian splatting, ar, segmentation, dynamic, deformation, 3d gaussian  
- **[SGLoc: Semantic Localization System for Camera Pose Estimation from 3D
  Gaussian Splatting Representation](https://arxiv.org/abs/2507.12027v1)**  
  Authors: Beining Xu, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12027v1.pdf)  
  Keywords: localization, gaussian splatting, ar, 3d gaussian, semantic  
- **[Robust 3D-Masked Part-level Editing in 3D Gaussian Splatting with
  Regularized Score Distillation Sampling](https://arxiv.org/abs/2507.11061v2)**  
  Authors: Hayeon Kim, Ji Ha Jang, Se Young Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11061v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://janeyeon.github.io/romap.)  
  Keywords: gaussian splatting, geometry, ar, efficient, slam, segmentation, 3d gaussian  
- **[3DGS_LSR:Large_Scale Relocation for Autonomous Driving Based on 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.05661v1)**  
  Authors: Haitao Lu, Haijier Chen, Haoze Liu, Shoujian Zhang, Bo Xu, Ziao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05661v1.pdf)  
  Keywords: localization, autonomous driving, gaussian splatting, ar, outdoor, 3d gaussian, mapping  
- **[Mastering Regional 3DGS: Locating, Initializing, and Editing with
  Diverse 2D Priors](https://arxiv.org/abs/2507.05426v1)**  
  Authors: Lanqing Guo, Yufei Wang, Hezhen Hu, Yan Zheng, Yeying Jin, Siyu Huang, Zhangyang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05426v1.pdf)  
  Keywords: localization, gaussian splatting, ar, efficient, 3d gaussian, semantic  
- **[A3FR: Agile 3D Gaussian Splatting with Incremental Gaze Tracked Foveated
  Rendering in Virtual Reality](https://arxiv.org/abs/2507.04147v1)**  
  Authors: Shuo Xin, Haiyu Wang, Sai Qian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.04147v1.pdf)  
  Keywords: tracking, gaussian splatting, face, ar, neural rendering, efficient, head, efficient rendering, vr, dynamic, 3d gaussian, human  
- **[Gaussian-LIC2: LiDAR-Inertial-Camera Gaussian Splatting SLAM](https://arxiv.org/abs/2507.04004v2)**  
  Authors: Xiaolei Lang, Jiajun Lv, Kai Tang, Laijian Li, Jianxin Huang, Lina Liu, Yong Liu, Xingxing Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.04004v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xingxingzuo.github.io/gaussian_lic2.)  
  Keywords: lightweight, gaussian splatting, ar, slam, 3d gaussian, fast  

### Scene Understanding

*Showing the latest 50 out of 191 papers*

- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: localization, motion, gaussian splatting, face, geometry, ar, compact, dynamic, 3d gaussian, semantic  
- **[ObjectGS: Object-aware Scene Reconstruction and Scene Understanding via
  Gaussian Splatting](https://arxiv.org/abs/2507.15454v1)**  
  Authors: Ruijie Zhu, Mulin Yu, Linning Xu, Lihan Jiang, Yixuan Li, Tianzhu Zhang, Jiangmiao Pang, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15454v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ruijiezhu94.github.io/ObjectGS_page)  
  Keywords: understanding, gaussian splatting, ar, segmentation, high-fidelity, dynamic, 3d gaussian, semantic  
- **[DCHM: Depth-Consistent Human Modeling for Multiview Detection](https://arxiv.org/abs/2507.14505v1)**  
  Authors: Jiahao Ma, Tianyu Wang, Miaomiao Liu, David Ahmedt-Aristizabal, Chuong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14505v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiahao-ma.github.io/DCHM/}{project)  
  Keywords: sparse-view, localization, gaussian splatting, ar, segmentation, human  
- **[PCR-GS: COLMAP-Free 3D Gaussian Splatting via Pose Co-Regularizations](https://arxiv.org/abs/2507.13891v2)**  
  Authors: Yu Wei, Jiahui Zhang, Xiaoqin Zhang, Ling Shao, Shijian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13891v2.pdf)  
  Keywords: semantic, ar, gaussian splatting, 3d gaussian  
- **[TexGS-VolVis: Expressive Scene Editing for Volume Visualization via
  Textured Gaussian Splatting](https://arxiv.org/abs/2507.13586v1)**  
  Authors: Kaiyuan Tang, Kuangshi Ai, Jun Han, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13586v1.pdf)  
  Keywords: gaussian splatting, lighting, geometry, ar, segmentation, 3d gaussian, real-time rendering  
- **[VolSegGS: Segmentation and Tracking in Dynamic Volumetric Scenes via
  Deformable 3D Gaussians](https://arxiv.org/abs/2507.12667v1)**  
  Authors: Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12667v1.pdf)  
  Keywords: tracking, gaussian splatting, ar, segmentation, dynamic, deformation, 3d gaussian  
- **[SGLoc: Semantic Localization System for Camera Pose Estimation from 3D
  Gaussian Splatting Representation](https://arxiv.org/abs/2507.12027v1)**  
  Authors: Beining Xu, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12027v1.pdf)  
  Keywords: localization, gaussian splatting, ar, 3d gaussian, semantic  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: sparse-view, understanding, gaussian splatting, face, reflection, geometry, ar, dynamic, sparse view  
- **[Robust 3D-Masked Part-level Editing in 3D Gaussian Splatting with
  Regularized Score Distillation Sampling](https://arxiv.org/abs/2507.11061v2)**  
  Authors: Hayeon Kim, Ji Ha Jang, Se Young Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11061v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://janeyeon.github.io/romap.)  
  Keywords: gaussian splatting, geometry, ar, efficient, slam, segmentation, 3d gaussian  
- **[MUVOD: A Novel Multi-view Video Object Segmentation Dataset and A
  Benchmark for 3D Segmentation](https://arxiv.org/abs/2507.07519v1)**  
  Authors: Bangning Wei, Joshua Maraval, Meriem Outtas, Kidiyo Kpalma, Nicolas Ramin, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07519v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://volumetric-repository.labs.b-com.com/#/muvod.)  
  Keywords: motion, understanding, gaussian splatting, 4d, ar, segmentation, dynamic, nerf, 3d gaussian, outdoor  



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