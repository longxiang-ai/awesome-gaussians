# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-07-21 01:01:52

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

- [3DGS Surveys](#3dgs-surveys) (2 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (21 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (100 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (37 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (53 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (5 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (33 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (10 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (35 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (19 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (1 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (14 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (19 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (22 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: 3d gaussian, face, survey, dynamic, autonomous driving, ar, outdoor, nerf, gaussian splatting, high-fidelity, efficient  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: 3d gaussian, robotics, 3d reconstruction, neural rendering, survey, autonomous driving, ar, nerf, gaussian splatting, high-fidelity, vr  

### Acceleration

- **[ScaffoldAvatar: High-Fidelity Gaussian Avatars with Patch Expressions](https://arxiv.org/abs/2507.10542v1)**  
  Authors: Shivangi Aneja, Sebastian Weiss, Irene Baeza, Prashanth Chandran, Gaspard Zoss, Matthias Nießner, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.10542v1.pdf)  
  Keywords: fast, 3d gaussian, human, face, avatar, dynamic, ar, head, gaussian splatting, high-fidelity, motion  
- **[Enhancing non-Rigid 3D Model Deformations Using Mesh-based Gaussian
  Splatting](https://arxiv.org/abs/2507.07000v1)**  
  Authors: Wijayathunga W. M. R. D. B  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07000v1.pdf)  
  Keywords: gaussian splatting, fast, 3d gaussian, face, ar, deformation, animation  
- **[FlexGaussian: Flexible and Cost-Effective Training-Free Compression for
  3D Gaussian Splatting](https://arxiv.org/abs/2507.06671v1)**  
  Authors: Boyuan Tian, Qizhe Gao, Siran Xianyu, Xiaotong Cui, Minjia Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06671v1.pdf)  
  Keywords: fast, 3d gaussian, ar, gaussian splatting, compression  
- **[LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+
  FPS](https://arxiv.org/abs/2507.07136v1)**  
  Authors: Wanhua Li, Yujie Zhao, Minghan Qin, Yang Liu, Yuanhao Cai, Chuang Gan, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07136v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://langsplat-v2.github.io.)  
  Keywords: fast, semantic, ar, high quality, gaussian splatting, efficient  
- **[A3FR: Agile 3D Gaussian Splatting with Incremental Gaze Tracked Foveated
  Rendering in Virtual Reality](https://arxiv.org/abs/2507.04147v1)**  
  Authors: Shuo Xin, Haiyu Wang, Sai Qian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.04147v1.pdf)  
  Keywords: human, 3d gaussian, tracking, vr, face, neural rendering, dynamic, efficient rendering, ar, head, gaussian splatting, efficient  
- **[Gaussian-LIC2: LiDAR-Inertial-Camera Gaussian Splatting SLAM](https://arxiv.org/abs/2507.04004v2)**  
  Authors: Xiaolei Lang, Jiajun Lv, Kai Tang, Laijian Li, Jianxin Huang, Lina Liu, Yong Liu, Xingxing Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.04004v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xingxingzuo.github.io/gaussian_lic2.)  
  Keywords: fast, 3d gaussian, slam, ar, lightweight, gaussian splatting  
- **[ArmGS: Composite Gaussian Appearance Refinement for Modeling Dynamic
  Urban Environments](https://arxiv.org/abs/2507.03886v1)**  
  Authors: Guile Wu, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.03886v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, urban scene, dynamic, autonomous driving, ar, gaussian splatting, high-fidelity  
- **[HyperGaussians: High-Dimensional Gaussian Splatting for High-Fidelity
  Animatable Face Avatars](https://arxiv.org/abs/2507.02803v2)**  
  Authors: Gent Serifi, Marcel C. Bühler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02803v2.pdf)  
  Keywords: fast, 3d gaussian, lighting, face, avatar, reflection, ar, deformation, gaussian splatting, high-fidelity  
- **[A LoD of Gaussians: Unified Training and Rendering for Ultra-Large Scale
  Reconstruction with External Memory](https://arxiv.org/abs/2507.01110v2)**  
  Authors: Felix Windisch, Lukas Radl, Thomas Köhler, Michael Steiner, Dieter Schmalstieg, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01110v2.pdf)  
  Keywords: real-time rendering, vr, dynamic, lightweight, ar, gaussian splatting, efficient  
- **[GaussianVLM: Scene-centric 3D Vision-Language Models using
  Language-aligned Gaussian Splats for Embodied Reasoning and Beyond](https://arxiv.org/abs/2507.00886v1)**  
  Authors: Anna-Maria Halacheva, Jan-Nico Zaech, Xi Wang, Danda Pani Paudel, Luc Van Gool  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00886v1.pdf)  
  Keywords: fast, 3d gaussian, understanding, compact, ar, gaussian splatting  

### Applications

*Showing the latest 50 out of 100 papers*

- **[VolSegGS: Segmentation and Tracking in Dynamic Volumetric Scenes via
  Deformable 3D Gaussians](https://arxiv.org/abs/2507.12667v1)**  
  Authors: Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12667v1.pdf)  
  Keywords: 3d gaussian, tracking, segmentation, dynamic, ar, deformation, gaussian splatting  
- **[BRUM: Robust 3D Vehicle Reconstruction from 360 Sparse Images](https://arxiv.org/abs/2507.12095v1)**  
  Authors: Davide Di Nucci, Matteo Tomei, Guido Borghi, Luca Ciuffreda, Roberto Vezzani, Rita Cucchiara  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12095v1.pdf)  
  Keywords: 3d reconstruction, ar, sparse-view, gaussian splatting, motion  
- **[SGLoc: Semantic Localization System for Camera Pose Estimation from 3D
  Gaussian Splatting Representation](https://arxiv.org/abs/2507.12027v1)**  
  Authors: Beining Xu, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12027v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, localization  
- **[Dark-EvGS: Event Camera as an Eye for Radiance Field in the Dark](https://arxiv.org/abs/2507.11931v1)**  
  Authors: Jingqian Wu, Peiqi Duan, Zongqiang Wang, Changwei Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11931v1.pdf)  
  Keywords: 3d gaussian, face, dynamic, ar, gaussian splatting, motion  
- **[Wavelet-GS: 3D Gaussian Splatting with Wavelet Decomposition](https://arxiv.org/abs/2507.12498v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Sicheng Yu, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12498v1.pdf)  
  Keywords: 3d gaussian, lighting, face, ar, gaussian splatting  
- **[A Mixed-Primitive-based Gaussian Splatting Method for Surface
  Reconstruction](https://arxiv.org/abs/2507.11321v1)**  
  Authors: Haoxuan Qu, Yujun Cai, Hossein Rahmani, Ajay Kumar, Junsong Yuan, Jun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11321v1.pdf)  
  Keywords: face, ar, gaussian splatting, high quality  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: sparse view, face, understanding, geometry, reflection, dynamic, sparse-view, ar, gaussian splatting  
- **[Robust 3D-Masked Part-level Editing in 3D Gaussian Splatting with
  Regularized Score Distillation Sampling](https://arxiv.org/abs/2507.11061v1)**  
  Authors: Hayeon Kim, Ji Ha Jang, Se Young Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11061v1.pdf)  
  Keywords: 3d gaussian, segmentation, geometry, slam, ar, gaussian splatting, efficient  
- **[ScaffoldAvatar: High-Fidelity Gaussian Avatars with Patch Expressions](https://arxiv.org/abs/2507.10542v1)**  
  Authors: Shivangi Aneja, Sebastian Weiss, Irene Baeza, Prashanth Chandran, Gaspard Zoss, Matthias Nießner, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.10542v1.pdf)  
  Keywords: fast, 3d gaussian, human, face, avatar, dynamic, ar, head, gaussian splatting, high-fidelity, motion  
- **[3DGAA: Realistic and Robust 3D Gaussian-based Adversarial Attack for
  Autonomous Driving](https://arxiv.org/abs/2507.09993v1)**  
  Authors: Yixun Zhang, Lizhi Wang, Junjun Zhao, Wending Zhao, Feng Zhou, Yonghao Dang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.09993v1.pdf)  
  Keywords: 3d gaussian, geometry, ar, autonomous driving, gaussian splatting  

### Avatar Generation

- **[Dark-EvGS: Event Camera as an Eye for Radiance Field in the Dark](https://arxiv.org/abs/2507.11931v1)**  
  Authors: Jingqian Wu, Peiqi Duan, Zongqiang Wang, Changwei Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11931v1.pdf)  
  Keywords: 3d gaussian, face, dynamic, ar, gaussian splatting, motion  
- **[Wavelet-GS: 3D Gaussian Splatting with Wavelet Decomposition](https://arxiv.org/abs/2507.12498v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Sicheng Yu, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12498v1.pdf)  
  Keywords: 3d gaussian, lighting, face, ar, gaussian splatting  
- **[A Mixed-Primitive-based Gaussian Splatting Method for Surface
  Reconstruction](https://arxiv.org/abs/2507.11321v1)**  
  Authors: Haoxuan Qu, Yujun Cai, Hossein Rahmani, Ajay Kumar, Junsong Yuan, Jun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11321v1.pdf)  
  Keywords: face, ar, gaussian splatting, high quality  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: sparse view, face, understanding, geometry, reflection, dynamic, sparse-view, ar, gaussian splatting  
- **[ScaffoldAvatar: High-Fidelity Gaussian Avatars with Patch Expressions](https://arxiv.org/abs/2507.10542v1)**  
  Authors: Shivangi Aneja, Sebastian Weiss, Irene Baeza, Prashanth Chandran, Gaspard Zoss, Matthias Nießner, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.10542v1.pdf)  
  Keywords: fast, 3d gaussian, human, face, avatar, dynamic, ar, head, gaussian splatting, high-fidelity, motion  
- **[Learning human-to-robot handovers through 3D scene reconstruction](https://arxiv.org/abs/2507.08726v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08726v1.pdf)  
  Keywords: human, ar, sparse-view, gaussian splatting  
- **[Temporally Consistent Amodal Completion for 3D Human-Object Interaction
  Reconstruction](https://arxiv.org/abs/2507.08137v1)**  
  Authors: Hyungjun Doh, Dong In Lee, Seunggeun Chi, Pin-Hao Huang, Kwonjoon Lee, Sangpil Kim, Karthik Ramani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08137v1.pdf)  
  Keywords: human, 3d gaussian, 3d reconstruction, dynamic, ar, gaussian splatting  
- **[Enhancing non-Rigid 3D Model Deformations Using Mesh-based Gaussian
  Splatting](https://arxiv.org/abs/2507.07000v1)**  
  Authors: Wijayathunga W. M. R. D. B  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07000v1.pdf)  
  Keywords: gaussian splatting, fast, 3d gaussian, face, ar, deformation, animation  
- **[Reflections Unlock: Geometry-Aware Reflection Disentanglement in 3D
  Gaussian Splatting for Photorealistic Scenes Rendering](https://arxiv.org/abs/2507.06103v1)**  
  Authors: Jiayi Song, Zihan Ye, Qingyuan Zhou, Weidong Yang, Ben Fei, Jingyi Xu, Ying He, Wanli Ouyang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06103v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ref-unlock.github.io/.)  
  Keywords: 3d gaussian, face, geometry, reflection, ar, nerf, gaussian splatting, efficient  
- **[VisualSpeaker: Visually-Guided 3D Avatar Lip Synthesis](https://arxiv.org/abs/2507.06060v1)**  
  Authors: Alexandre Symeonidis-Herzig, Özge Mercanoğlu Sincan, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06060v1.pdf)  
  Keywords: gaussian splatting, human, 3d gaussian, avatar, ar, recognition, animation, high-fidelity  

### Dynamic Scene

*Showing the latest 50 out of 53 papers*

- **[VolSegGS: Segmentation and Tracking in Dynamic Volumetric Scenes via
  Deformable 3D Gaussians](https://arxiv.org/abs/2507.12667v1)**  
  Authors: Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12667v1.pdf)  
  Keywords: 3d gaussian, tracking, segmentation, dynamic, ar, deformation, gaussian splatting  
- **[BRUM: Robust 3D Vehicle Reconstruction from 360 Sparse Images](https://arxiv.org/abs/2507.12095v1)**  
  Authors: Davide Di Nucci, Matteo Tomei, Guido Borghi, Luca Ciuffreda, Roberto Vezzani, Rita Cucchiara  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12095v1.pdf)  
  Keywords: 3d reconstruction, ar, sparse-view, gaussian splatting, motion  
- **[Dark-EvGS: Event Camera as an Eye for Radiance Field in the Dark](https://arxiv.org/abs/2507.11931v1)**  
  Authors: Jingqian Wu, Peiqi Duan, Zongqiang Wang, Changwei Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11931v1.pdf)  
  Keywords: 3d gaussian, face, dynamic, ar, gaussian splatting, motion  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: sparse view, face, understanding, geometry, reflection, dynamic, sparse-view, ar, gaussian splatting  
- **[ScaffoldAvatar: High-Fidelity Gaussian Avatars with Patch Expressions](https://arxiv.org/abs/2507.10542v1)**  
  Authors: Shivangi Aneja, Sebastian Weiss, Irene Baeza, Prashanth Chandran, Gaspard Zoss, Matthias Nießner, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.10542v1.pdf)  
  Keywords: fast, 3d gaussian, human, face, avatar, dynamic, ar, head, gaussian splatting, high-fidelity, motion  
- **[Temporally Consistent Amodal Completion for 3D Human-Object Interaction
  Reconstruction](https://arxiv.org/abs/2507.08137v1)**  
  Authors: Hyungjun Doh, Dong In Lee, Seunggeun Chi, Pin-Hao Huang, Kwonjoon Lee, Sangpil Kim, Karthik Ramani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08137v1.pdf)  
  Keywords: human, 3d gaussian, 3d reconstruction, dynamic, ar, gaussian splatting  
- **[MUVOD: A Novel Multi-view Video Object Segmentation Dataset and A
  Benchmark for 3D Segmentation](https://arxiv.org/abs/2507.07519v1)**  
  Authors: Bangning Wei, Joshua Maraval, Meriem Outtas, Kidiyo Kpalma, Nicolas Ramin, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07519v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://volumetric-repository.labs.b-com.com/#/muvod.)  
  Keywords: 3d gaussian, understanding, segmentation, nerf, dynamic, ar, outdoor, 4d, gaussian splatting, motion  
- **[SD-GS: Structured Deformable 3D Gaussians for Efficient Dynamic Scene
  Reconstruction](https://arxiv.org/abs/2507.07465v1)**  
  Authors: Wei Yao, Shuzhao Xie, Letian Li, Weixiang Zhang, Zhixin Lai, Shiqi Dai, Ke Zhang, Zhi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07465v1.pdf)  
  Keywords: 3d gaussian, compact, dynamic, ar, deformation, 4d, gaussian splatting, motion, efficient  
- **[Enhancing non-Rigid 3D Model Deformations Using Mesh-based Gaussian
  Splatting](https://arxiv.org/abs/2507.07000v1)**  
  Authors: Wijayathunga W. M. R. D. B  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07000v1.pdf)  
  Keywords: gaussian splatting, fast, 3d gaussian, face, ar, deformation, animation  
- **[ClipGS: Clippable Gaussian Splatting for Interactive Cinematic
  Visualization of Volumetric Medical Data](https://arxiv.org/abs/2507.06647v1)**  
  Authors: Chengkun Li, Yuqi Tong, Kai Chen, Zhenya Yang, Ruiyang Li, Shi Qiu, Jason Ying-Kuen Chan, Pheng-Ann Heng, Qi Dou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06647v1.pdf)  
  Keywords: medical, understanding, dynamic, ar, deformation, gaussian splatting  

### Few-shot

- **[BRUM: Robust 3D Vehicle Reconstruction from 360 Sparse Images](https://arxiv.org/abs/2507.12095v1)**  
  Authors: Davide Di Nucci, Matteo Tomei, Guido Borghi, Luca Ciuffreda, Roberto Vezzani, Rita Cucchiara  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12095v1.pdf)  
  Keywords: 3d reconstruction, ar, sparse-view, gaussian splatting, motion  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: sparse view, face, understanding, geometry, reflection, dynamic, sparse-view, ar, gaussian splatting  
- **[Learning human-to-robot handovers through 3D scene reconstruction](https://arxiv.org/abs/2507.08726v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08726v1.pdf)  
  Keywords: human, ar, sparse-view, gaussian splatting  
- **[RegGS: Unposed Sparse Views Gaussian Splatting with 3DGS Registration](https://arxiv.org/abs/2507.08136v1)**  
  Authors: Chong Cheng, Yu Hu, Sicheng Yu, Beizhen Zhao, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08136v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/reggs/.)  
  Keywords: 3d gaussian, sparse view, geometry, ar, gaussian splatting, efficient  
- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from
  RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: ar, sparse-view, dynamic, gaussian splatting, motion  

### Geometry Reconstruction

- **[BRUM: Robust 3D Vehicle Reconstruction from 360 Sparse Images](https://arxiv.org/abs/2507.12095v1)**  
  Authors: Davide Di Nucci, Matteo Tomei, Guido Borghi, Luca Ciuffreda, Roberto Vezzani, Rita Cucchiara  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12095v1.pdf)  
  Keywords: 3d reconstruction, ar, sparse-view, gaussian splatting, motion  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: sparse view, face, understanding, geometry, reflection, dynamic, sparse-view, ar, gaussian splatting  
- **[Robust 3D-Masked Part-level Editing in 3D Gaussian Splatting with
  Regularized Score Distillation Sampling](https://arxiv.org/abs/2507.11061v1)**  
  Authors: Hayeon Kim, Ji Ha Jang, Se Young Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11061v1.pdf)  
  Keywords: 3d gaussian, segmentation, geometry, slam, ar, gaussian splatting, efficient  
- **[3DGAA: Realistic and Robust 3D Gaussian-based Adversarial Attack for
  Autonomous Driving](https://arxiv.org/abs/2507.09993v1)**  
  Authors: Yixun Zhang, Lizhi Wang, Junjun Zhao, Wending Zhao, Feng Zhou, Yonghao Dang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.09993v1.pdf)  
  Keywords: 3d gaussian, geometry, ar, autonomous driving, gaussian splatting  
- **[RePaintGS: Reference-Guided Gaussian Splatting for Realistic and
  View-Consistent 3D Scene Inpainting](https://arxiv.org/abs/2507.08434v1)**  
  Authors: Ji Hyun Seo, Byounhyun Yoo, Gerard Jounghyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08434v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, gaussian splatting  
- **[Temporally Consistent Amodal Completion for 3D Human-Object Interaction
  Reconstruction](https://arxiv.org/abs/2507.08137v1)**  
  Authors: Hyungjun Doh, Dong In Lee, Seunggeun Chi, Pin-Hao Huang, Kwonjoon Lee, Sangpil Kim, Karthik Ramani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08137v1.pdf)  
  Keywords: human, 3d gaussian, 3d reconstruction, dynamic, ar, gaussian splatting  
- **[RegGS: Unposed Sparse Views Gaussian Splatting with 3DGS Registration](https://arxiv.org/abs/2507.08136v1)**  
  Authors: Chong Cheng, Yu Hu, Sicheng Yu, Beizhen Zhao, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08136v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/reggs/.)  
  Keywords: 3d gaussian, sparse view, geometry, ar, gaussian splatting, efficient  
- **[LighthouseGS: Indoor Structure-aware 3D Gaussian Splatting for
  Panorama-Style Mobile Captures](https://arxiv.org/abs/2507.06109v1)**  
  Authors: Seungoh Han, Jaehoon Jang, Hyunsu Kim, Jaeheung Surh, Junhyung Kwak, Hyowon Ha, Kyungdon Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06109v1.pdf)  
  Keywords: 3d gaussian, geometry, ar, gaussian splatting, high-fidelity, motion  
- **[Reflections Unlock: Geometry-Aware Reflection Disentanglement in 3D
  Gaussian Splatting for Photorealistic Scenes Rendering](https://arxiv.org/abs/2507.06103v1)**  
  Authors: Jiayi Song, Zihan Ye, Qingyuan Zhou, Weidong Yang, Ben Fei, Jingyi Xu, Ying He, Wanli Ouyang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06103v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ref-unlock.github.io/.)  
  Keywords: 3d gaussian, face, geometry, reflection, ar, nerf, gaussian splatting, efficient  
- **[DreamArt: Generating Interactable Articulated Objects from a Single
  Image](https://arxiv.org/abs/2507.05763v1)**  
  Authors: Ruijie Lu, Yu Liu, Jiaxiang Tang, Junfeng Ni, Yuxiang Wang, Diwen Wan, Gang Zeng, Yixin Chen, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05763v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dream-art-0.github.io/DreamArt/.)  
  Keywords: vr, face, geometry, segmentation, ar, nerf, gaussian splatting, high-fidelity, motion  

### Large Scene

- **[MUVOD: A Novel Multi-view Video Object Segmentation Dataset and A
  Benchmark for 3D Segmentation](https://arxiv.org/abs/2507.07519v1)**  
  Authors: Bangning Wei, Joshua Maraval, Meriem Outtas, Kidiyo Kpalma, Nicolas Ramin, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07519v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://volumetric-repository.labs.b-com.com/#/muvod.)  
  Keywords: 3d gaussian, understanding, segmentation, nerf, dynamic, ar, outdoor, 4d, gaussian splatting, motion  
- **[3DGS_LSR:Large_Scale Relocation for Autonomous Driving Based on 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.05661v1)**  
  Authors: Haitao Lu, Haijier Chen, Haoze Liu, Shoujian Zhang, Bo Xu, Ziao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05661v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, autonomous driving, ar, outdoor, localization, mapping  
- **[ArmGS: Composite Gaussian Appearance Refinement for Modeling Dynamic
  Urban Environments](https://arxiv.org/abs/2507.03886v1)**  
  Authors: Guile Wu, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.03886v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, urban scene, dynamic, autonomous driving, ar, gaussian splatting, high-fidelity  
- **[Outdoor Monocular SLAM with Global Scale-Consistent 3D Gaussian
  Pointmaps](https://arxiv.org/abs/2507.03737v1)**  
  Authors: Chong Cheng, Sicheng Yu, Zijian Wang, Yifan Zhou, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.03737v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/S3PO-GS/.)  
  Keywords: 3d gaussian, tracking, slam, dynamic, ar, outdoor, gaussian splatting, high-fidelity, mapping  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, lighting, tracking, geometry, slam, dynamic, ar, outdoor, illumination, high-fidelity, mapping  
- **[BézierGS: Dynamic Urban Scene Reconstruction with Bézier Curve
  Gaussian Splatting](https://arxiv.org/abs/2506.22099v3)**  
  Authors: Zipei Ma, Junzhe Jiang, Yurui Chen, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22099v3.pdf)  
  Keywords: urban scene, autonomous driving, dynamic, ar, gaussian splatting, motion  
- **[ICP-3DGS: SfM-free 3D Gaussian Splatting for Large-scale Unbounded
  Scenes](https://arxiv.org/abs/2506.21629v1)**  
  Authors: Chenhao Zhang, Yezhi Shen, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21629v1.pdf)  
  Keywords: 3d gaussian, neural rendering, ar, outdoor, nerf, gaussian splatting, motion  
- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: 3d gaussian, tracking, slam, ar, outdoor, gaussian splatting  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: 3d gaussian, face, survey, dynamic, autonomous driving, ar, outdoor, nerf, gaussian splatting, high-fidelity, efficient  
- **[Multiview Geometric Regularization of Gaussian Splatting for Accurate
  Radiance Fields](https://arxiv.org/abs/2506.13508v1)**  
  Authors: Jungeon Kim, Geonsoo Park, Seungyong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13508v1.pdf)  
  Keywords: 3d gaussian, geometry, ar, outdoor, gaussian splatting  

### Model Compression

- **[Robust 3D-Masked Part-level Editing in 3D Gaussian Splatting with
  Regularized Score Distillation Sampling](https://arxiv.org/abs/2507.11061v1)**  
  Authors: Hayeon Kim, Ji Ha Jang, Se Young Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11061v1.pdf)  
  Keywords: 3d gaussian, segmentation, geometry, slam, ar, gaussian splatting, efficient  
- **[RegGS: Unposed Sparse Views Gaussian Splatting with 3DGS Registration](https://arxiv.org/abs/2507.08136v1)**  
  Authors: Chong Cheng, Yu Hu, Sicheng Yu, Beizhen Zhao, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08136v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/reggs/.)  
  Keywords: 3d gaussian, sparse view, geometry, ar, gaussian splatting, efficient  
- **[RTR-GS: 3D Gaussian Splatting for Inverse Rendering with Radiance
  Transfer and Reflection](https://arxiv.org/abs/2507.07733v1)**  
  Authors: Yongyang Zhou, Fang-Lue Zhang, Zichen Wang, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07733v1.pdf)  
  Keywords: 3d gaussian, relighting, lighting, reflection, ar, gaussian splatting, efficient  
- **[SD-GS: Structured Deformable 3D Gaussians for Efficient Dynamic Scene
  Reconstruction](https://arxiv.org/abs/2507.07465v1)**  
  Authors: Wei Yao, Shuzhao Xie, Letian Li, Weixiang Zhang, Zhixin Lai, Shiqi Dai, Ke Zhang, Zhi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07465v1.pdf)  
  Keywords: 3d gaussian, compact, dynamic, ar, deformation, 4d, gaussian splatting, motion, efficient  
- **[FlexGaussian: Flexible and Cost-Effective Training-Free Compression for
  3D Gaussian Splatting](https://arxiv.org/abs/2507.06671v1)**  
  Authors: Boyuan Tian, Qizhe Gao, Siran Xianyu, Xiaotong Cui, Minjia Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06671v1.pdf)  
  Keywords: fast, 3d gaussian, ar, gaussian splatting, compression  
- **[LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+
  FPS](https://arxiv.org/abs/2507.07136v1)**  
  Authors: Wanhua Li, Yujie Zhao, Minghan Qin, Yang Liu, Yuanhao Cai, Chuang Gan, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07136v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://langsplat-v2.github.io.)  
  Keywords: fast, semantic, ar, high quality, gaussian splatting, efficient  
- **[Reflections Unlock: Geometry-Aware Reflection Disentanglement in 3D
  Gaussian Splatting for Photorealistic Scenes Rendering](https://arxiv.org/abs/2507.06103v1)**  
  Authors: Jiayi Song, Zihan Ye, Qingyuan Zhou, Weidong Yang, Ben Fei, Jingyi Xu, Ying He, Wanli Ouyang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06103v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ref-unlock.github.io/.)  
  Keywords: 3d gaussian, face, geometry, reflection, ar, nerf, gaussian splatting, efficient  
- **[D-FCGS: Feedforward Compression of Dynamic Gaussian Splatting for
  Free-Viewpoint Videos](https://arxiv.org/abs/2507.05859v1)**  
  Authors: Wenkang Zhang, Yan Zhao, Qiang Wang, Li Song, Zhengxue Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05859v1.pdf)  
  Keywords: 3d gaussian, dynamic, efficient, ar, compression, gaussian splatting, high-fidelity, motion  
- **[BayesSDF: Surface-Based Laplacian Uncertainty Estimation for 3D Geometry
  with Neural Signed Distance Fields](https://arxiv.org/abs/2507.06269v2)**  
  Authors: Rushil Desai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06269v2.pdf)  
  Keywords: 3d gaussian, face, geometry, ar, nerf, gaussian splatting, efficient  
- **[Mastering Regional 3DGS: Locating, Initializing, and Editing with
  Diverse 2D Priors](https://arxiv.org/abs/2507.05426v1)**  
  Authors: Lanqing Guo, Yufei Wang, Hezhen Hu, Yan Zheng, Yeying Jin, Siyu Huang, Zhangyang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05426v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, localization, efficient  

### Quality Enhancement

- **[A Mixed-Primitive-based Gaussian Splatting Method for Surface
  Reconstruction](https://arxiv.org/abs/2507.11321v1)**  
  Authors: Haoxuan Qu, Yujun Cai, Hossein Rahmani, Ajay Kumar, Junsong Yuan, Jun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11321v1.pdf)  
  Keywords: face, ar, gaussian splatting, high quality  
- **[ScaffoldAvatar: High-Fidelity Gaussian Avatars with Patch Expressions](https://arxiv.org/abs/2507.10542v1)**  
  Authors: Shivangi Aneja, Sebastian Weiss, Irene Baeza, Prashanth Chandran, Gaspard Zoss, Matthias Nießner, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.10542v1.pdf)  
  Keywords: fast, 3d gaussian, human, face, avatar, dynamic, ar, head, gaussian splatting, high-fidelity, motion  
- **[LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+
  FPS](https://arxiv.org/abs/2507.07136v1)**  
  Authors: Wanhua Li, Yujie Zhao, Minghan Qin, Yang Liu, Yuanhao Cai, Chuang Gan, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07136v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://langsplat-v2.github.io.)  
  Keywords: fast, semantic, ar, high quality, gaussian splatting, efficient  
- **[LighthouseGS: Indoor Structure-aware 3D Gaussian Splatting for
  Panorama-Style Mobile Captures](https://arxiv.org/abs/2507.06109v1)**  
  Authors: Seungoh Han, Jaehoon Jang, Hyunsu Kim, Jaeheung Surh, Junhyung Kwak, Hyowon Ha, Kyungdon Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06109v1.pdf)  
  Keywords: 3d gaussian, geometry, ar, gaussian splatting, high-fidelity, motion  
- **[VisualSpeaker: Visually-Guided 3D Avatar Lip Synthesis](https://arxiv.org/abs/2507.06060v1)**  
  Authors: Alexandre Symeonidis-Herzig, Özge Mercanoğlu Sincan, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06060v1.pdf)  
  Keywords: gaussian splatting, human, 3d gaussian, avatar, ar, recognition, animation, high-fidelity  
- **[D-FCGS: Feedforward Compression of Dynamic Gaussian Splatting for
  Free-Viewpoint Videos](https://arxiv.org/abs/2507.05859v1)**  
  Authors: Wenkang Zhang, Yan Zhao, Qiang Wang, Li Song, Zhengxue Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05859v1.pdf)  
  Keywords: 3d gaussian, dynamic, efficient, ar, compression, gaussian splatting, high-fidelity, motion  
- **[DreamArt: Generating Interactable Articulated Objects from a Single
  Image](https://arxiv.org/abs/2507.05763v1)**  
  Authors: Ruijie Lu, Yu Liu, Jiaxiang Tang, Junfeng Ni, Yuxiang Wang, Diwen Wan, Gang Zeng, Yixin Chen, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05763v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dream-art-0.github.io/DreamArt/.)  
  Keywords: vr, face, geometry, segmentation, ar, nerf, gaussian splatting, high-fidelity, motion  
- **[SegmentDreamer: Towards High-fidelity Text-to-3D Synthesis with
  Segmented Consistency Trajectory Distillation](https://arxiv.org/abs/2507.05256v1)**  
  Authors: Jiahao Zhu, Zixuan Chen, Guangcong Wang, Xiaohua Xie, Yi Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05256v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, high-fidelity  
- **[InterGSEdit: Interactive 3D Gaussian Splatting Editing with 3D
  Geometry-Consistent Attention Prior](https://arxiv.org/abs/2507.04961v1)**  
  Authors: Minghao Wen, Shengjie Wu, Kangkan Wang, Dong Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.04961v1.pdf)  
  Keywords: 3d gaussian, geometry, semantic, ar, deformation, gaussian splatting, high-fidelity  
- **[ArmGS: Composite Gaussian Appearance Refinement for Modeling Dynamic
  Urban Environments](https://arxiv.org/abs/2507.03886v1)**  
  Authors: Guile Wu, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.03886v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, urban scene, dynamic, autonomous driving, ar, gaussian splatting, high-fidelity  

### Ray Tracing

- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: real-time rendering, ray tracing, ar, gaussian splatting, high-fidelity, efficient  

### Relighting

- **[Wavelet-GS: 3D Gaussian Splatting with Wavelet Decomposition](https://arxiv.org/abs/2507.12498v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Sicheng Yu, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12498v1.pdf)  
  Keywords: 3d gaussian, lighting, face, ar, gaussian splatting  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: sparse view, face, understanding, geometry, reflection, dynamic, sparse-view, ar, gaussian splatting  
- **[RTR-GS: 3D Gaussian Splatting for Inverse Rendering with Radiance
  Transfer and Reflection](https://arxiv.org/abs/2507.07733v1)**  
  Authors: Yongyang Zhou, Fang-Lue Zhang, Zichen Wang, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07733v1.pdf)  
  Keywords: 3d gaussian, relighting, lighting, reflection, ar, gaussian splatting, efficient  
- **[Seg-Wild: Interactive Segmentation based on 3D Gaussian Splatting for
  Unconstrained Image Collections](https://arxiv.org/abs/2507.07395v1)**  
  Authors: Yongtang Bao, Chengjie Tang, Yuze Wang, Haojie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07395v1.pdf)  
  Keywords: 3d gaussian, lighting, segmentation, ar, gaussian splatting  
- **[Reflections Unlock: Geometry-Aware Reflection Disentanglement in 3D
  Gaussian Splatting for Photorealistic Scenes Rendering](https://arxiv.org/abs/2507.06103v1)**  
  Authors: Jiayi Song, Zihan Ye, Qingyuan Zhou, Weidong Yang, Ben Fei, Jingyi Xu, Ying He, Wanli Ouyang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06103v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ref-unlock.github.io/.)  
  Keywords: 3d gaussian, face, geometry, reflection, ar, nerf, gaussian splatting, efficient  
- **[HyperGaussians: High-Dimensional Gaussian Splatting for High-Fidelity
  Animatable Face Avatars](https://arxiv.org/abs/2507.02803v2)**  
  Authors: Gent Serifi, Marcel C. Bühler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02803v2.pdf)  
  Keywords: fast, 3d gaussian, lighting, face, avatar, reflection, ar, deformation, gaussian splatting, high-fidelity  
- **[Gbake: Baking 3D Gaussian Splats into Reflection Probes](https://arxiv.org/abs/2507.02257v1)**  
  Authors: Stephen Pasch, Joel K. Salzman, Changxi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02257v1.pdf)  
  Keywords: 3d gaussian, lighting, geometry, reflection, ar, gaussian splatting, mapping  
- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: lighting, tracking, 3d reconstruction, understanding, segmentation, semantic, ar, deformation, gaussian splatting  
- **[Endo-4DGX: Robust Endoscopic Scene Reconstruction and Illumination
  Correction with Gaussian Splatting](https://arxiv.org/abs/2506.23308v1)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Yanheng Li, Tong Chen, Jie Wang, Jinlin Wu, Zhen Lei, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23308v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, lighting, dynamic, ar, 4d, illumination  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, lighting, tracking, geometry, slam, dynamic, ar, outdoor, illumination, high-fidelity, mapping  

### SLAM

- **[VolSegGS: Segmentation and Tracking in Dynamic Volumetric Scenes via
  Deformable 3D Gaussians](https://arxiv.org/abs/2507.12667v1)**  
  Authors: Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12667v1.pdf)  
  Keywords: 3d gaussian, tracking, segmentation, dynamic, ar, deformation, gaussian splatting  
- **[SGLoc: Semantic Localization System for Camera Pose Estimation from 3D
  Gaussian Splatting Representation](https://arxiv.org/abs/2507.12027v1)**  
  Authors: Beining Xu, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12027v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, localization  
- **[Robust 3D-Masked Part-level Editing in 3D Gaussian Splatting with
  Regularized Score Distillation Sampling](https://arxiv.org/abs/2507.11061v1)**  
  Authors: Hayeon Kim, Ji Ha Jang, Se Young Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11061v1.pdf)  
  Keywords: 3d gaussian, segmentation, geometry, slam, ar, gaussian splatting, efficient  
- **[3DGS_LSR:Large_Scale Relocation for Autonomous Driving Based on 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.05661v1)**  
  Authors: Haitao Lu, Haijier Chen, Haoze Liu, Shoujian Zhang, Bo Xu, Ziao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05661v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, autonomous driving, ar, outdoor, localization, mapping  
- **[Mastering Regional 3DGS: Locating, Initializing, and Editing with
  Diverse 2D Priors](https://arxiv.org/abs/2507.05426v1)**  
  Authors: Lanqing Guo, Yufei Wang, Hezhen Hu, Yan Zheng, Yeying Jin, Siyu Huang, Zhangyang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05426v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, localization, efficient  
- **[A3FR: Agile 3D Gaussian Splatting with Incremental Gaze Tracked Foveated
  Rendering in Virtual Reality](https://arxiv.org/abs/2507.04147v1)**  
  Authors: Shuo Xin, Haiyu Wang, Sai Qian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.04147v1.pdf)  
  Keywords: human, 3d gaussian, tracking, vr, face, neural rendering, dynamic, efficient rendering, ar, head, gaussian splatting, efficient  
- **[Gaussian-LIC2: LiDAR-Inertial-Camera Gaussian Splatting SLAM](https://arxiv.org/abs/2507.04004v2)**  
  Authors: Xiaolei Lang, Jiajun Lv, Kai Tang, Laijian Li, Jianxin Huang, Lina Liu, Yong Liu, Xingxing Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.04004v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xingxingzuo.github.io/gaussian_lic2.)  
  Keywords: fast, 3d gaussian, slam, ar, lightweight, gaussian splatting  
- **[Outdoor Monocular SLAM with Global Scale-Consistent 3D Gaussian
  Pointmaps](https://arxiv.org/abs/2507.03737v1)**  
  Authors: Chong Cheng, Sicheng Yu, Zijian Wang, Yifan Zhou, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.03737v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/S3PO-GS/.)  
  Keywords: 3d gaussian, tracking, slam, dynamic, ar, outdoor, gaussian splatting, high-fidelity, mapping  
- **[Gbake: Baking 3D Gaussian Splats into Reflection Probes](https://arxiv.org/abs/2507.02257v1)**  
  Authors: Stephen Pasch, Joel K. Salzman, Changxi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02257v1.pdf)  
  Keywords: 3d gaussian, lighting, geometry, reflection, ar, gaussian splatting, mapping  
- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: lighting, tracking, 3d reconstruction, understanding, segmentation, semantic, ar, deformation, gaussian splatting  

### Scene Understanding

- **[VolSegGS: Segmentation and Tracking in Dynamic Volumetric Scenes via
  Deformable 3D Gaussians](https://arxiv.org/abs/2507.12667v1)**  
  Authors: Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12667v1.pdf)  
  Keywords: 3d gaussian, tracking, segmentation, dynamic, ar, deformation, gaussian splatting  
- **[SGLoc: Semantic Localization System for Camera Pose Estimation from 3D
  Gaussian Splatting Representation](https://arxiv.org/abs/2507.12027v1)**  
  Authors: Beining Xu, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12027v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, localization  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: sparse view, face, understanding, geometry, reflection, dynamic, sparse-view, ar, gaussian splatting  
- **[Robust 3D-Masked Part-level Editing in 3D Gaussian Splatting with
  Regularized Score Distillation Sampling](https://arxiv.org/abs/2507.11061v1)**  
  Authors: Hayeon Kim, Ji Ha Jang, Se Young Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11061v1.pdf)  
  Keywords: 3d gaussian, segmentation, geometry, slam, ar, gaussian splatting, efficient  
- **[MUVOD: A Novel Multi-view Video Object Segmentation Dataset and A
  Benchmark for 3D Segmentation](https://arxiv.org/abs/2507.07519v1)**  
  Authors: Bangning Wei, Joshua Maraval, Meriem Outtas, Kidiyo Kpalma, Nicolas Ramin, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07519v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://volumetric-repository.labs.b-com.com/#/muvod.)  
  Keywords: 3d gaussian, understanding, segmentation, nerf, dynamic, ar, outdoor, 4d, gaussian splatting, motion  
- **[Seg-Wild: Interactive Segmentation based on 3D Gaussian Splatting for
  Unconstrained Image Collections](https://arxiv.org/abs/2507.07395v1)**  
  Authors: Yongtang Bao, Chengjie Tang, Yuze Wang, Haojie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07395v1.pdf)  
  Keywords: 3d gaussian, lighting, segmentation, ar, gaussian splatting  
- **[ClipGS: Clippable Gaussian Splatting for Interactive Cinematic
  Visualization of Volumetric Medical Data](https://arxiv.org/abs/2507.06647v1)**  
  Authors: Chengkun Li, Yuqi Tong, Kai Chen, Zhenya Yang, Ruiyang Li, Shi Qiu, Jason Ying-Kuen Chan, Pheng-Ann Heng, Qi Dou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06647v1.pdf)  
  Keywords: medical, understanding, dynamic, ar, deformation, gaussian splatting  
- **[LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+
  FPS](https://arxiv.org/abs/2507.07136v1)**  
  Authors: Wanhua Li, Yujie Zhao, Minghan Qin, Yang Liu, Yuanhao Cai, Chuang Gan, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07136v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://langsplat-v2.github.io.)  
  Keywords: fast, semantic, ar, high quality, gaussian splatting, efficient  
- **[VisualSpeaker: Visually-Guided 3D Avatar Lip Synthesis](https://arxiv.org/abs/2507.06060v1)**  
  Authors: Alexandre Symeonidis-Herzig, Özge Mercanoğlu Sincan, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06060v1.pdf)  
  Keywords: gaussian splatting, human, 3d gaussian, avatar, ar, recognition, animation, high-fidelity  
- **[DreamArt: Generating Interactable Articulated Objects from a Single
  Image](https://arxiv.org/abs/2507.05763v1)**  
  Authors: Ruijie Lu, Yu Liu, Jiaxiang Tang, Junfeng Ni, Yuxiang Wang, Diwen Wan, Gang Zeng, Yixin Chen, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05763v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dream-art-0.github.io/DreamArt/.)  
  Keywords: vr, face, geometry, segmentation, ar, nerf, gaussian splatting, high-fidelity, motion  



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