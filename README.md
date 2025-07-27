# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-07-27 01:04:06

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

- [3DGS Surveys](#3dgs-surveys) (19 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (272 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (330 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (400 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (72 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (322 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (63 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (398 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (163 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (17 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (112 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (158 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (189 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: survey, ar, 3d gaussian, geometry, motion, sparse-view, robotics, vr, 3d reconstruction, nerf, gaussian splatting  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v1)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v1.pdf)  
  Keywords: survey, ar, 3d gaussian, lighting, human, robotics, vr, 3d reconstruction, nerf, dynamic, gaussian splatting, slam, fast  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: survey, ar, 3d gaussian, face, outdoor, efficient, high-fidelity, nerf, dynamic, gaussian splatting, autonomous driving  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: survey, ar, 3d gaussian, neural rendering, robotics, vr, 3d reconstruction, high-fidelity, nerf, gaussian splatting, autonomous driving  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: survey, ar, 3d gaussian, neural rendering, outdoor, efficient, understanding, 3d reconstruction, high-fidelity, gaussian splatting, semantic, segmentation  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: survey, ar, 3d gaussian, efficient, mapping, nerf, gaussian splatting, slam, localization, semantic, segmentation  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to
  Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: survey, ar, 3d gaussian, motion, 4d, understanding, body, dynamic, gaussian splatting  
- **[A Survey of 3D Reconstruction with Event Cameras](https://arxiv.org/abs/2505.08438v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v2.pdf)  
  Keywords: survey, ar, 3d gaussian, neural rendering, geometry, motion, robotics, illumination, 3d reconstruction, nerf, dynamic, gaussian splatting, autonomous driving  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: survey, ar, efficient, 3d reconstruction, gaussian splatting, fast  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: survey, 3d gaussian, lighting, 3d reconstruction, ar  

### Acceleration

*Showing the latest 50 out of 272 papers*

- **[StreamME: Simplify 3D Gaussian Avatar within Live Stream](https://arxiv.org/abs/2507.17029v1)**  
  Authors: Luchuan Song, Yang Zhou, Zhan Xu, Yi Zhou, Deepali Aneja, Chenliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.17029v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://songluchuan.github.io/StreamME/.)  
  Keywords: avatar, ar, 3d gaussian, animation, face, lighting, geometry, vr, relighting, gaussian splatting, fast, head  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: ar, 3d gaussian, face, ray marching, lighting, geometry, relightable, efficient, relighting, gaussian splatting, efficient rendering  
- **[GCC: A 3DGS Inference Architecture with Gaussian-Wise and Cross-Stage
  Conditional Processing](https://arxiv.org/abs/2507.15300v2)**  
  Authors: Minnan Pei, Gang Li, Junwen Si, Zeyu Zhu, Zitao Mo, Peisong Wang, Zhuoran Song, Xiaoyao Liang, Jian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15300v2.pdf)  
  Keywords: ar, 3d gaussian, neural rendering, compact, efficient, high-fidelity, dynamic, gaussian splatting, fast, head  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v1)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v1.pdf)  
  Keywords: survey, ar, 3d gaussian, lighting, human, robotics, vr, 3d reconstruction, nerf, dynamic, gaussian splatting, slam, fast  
- **[Neural-GASh: A CGA-based neural radiance prediction pipeline for
  real-time shading](https://arxiv.org/abs/2507.13917v1)**  
  Authors: Efstratios Geronikolakis, Manos Kamarianakis, Antonis Protopsaltis, George Papagiannakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13917v1.pdf)  
  Keywords: 3d gaussian, light transport, efficient, vr, dynamic, ar, fast  
- **[TexGS-VolVis: Expressive Scene Editing for Volume Visualization via
  Textured Gaussian Splatting](https://arxiv.org/abs/2507.13586v1)**  
  Authors: Kaiyuan Tang, Kuangshi Ai, Jun Han, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13586v1.pdf)  
  Keywords: ar, 3d gaussian, lighting, geometry, segmentation, gaussian splatting, real-time rendering  
- **[ScaffoldAvatar: High-Fidelity Gaussian Avatars with Patch Expressions](https://arxiv.org/abs/2507.10542v1)**  
  Authors: Shivangi Aneja, Sebastian Weiss, Irene Baeza, Prashanth Chandran, Gaspard Zoss, Matthias Nießner, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.10542v1.pdf)  
  Keywords: avatar, ar, 3d gaussian, face, motion, human, high-fidelity, dynamic, gaussian splatting, fast, head  
- **[Enhancing non-Rigid 3D Model Deformations Using Mesh-based Gaussian
  Splatting](https://arxiv.org/abs/2507.07000v1)**  
  Authors: Wijayathunga W. M. R. D. B  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07000v1.pdf)  
  Keywords: ar, 3d gaussian, animation, face, deformation, gaussian splatting, fast  
- **[FlexGaussian: Flexible and Cost-Effective Training-Free Compression for
  3D Gaussian Splatting](https://arxiv.org/abs/2507.06671v1)**  
  Authors: Boyuan Tian, Qizhe Gao, Siran Xianyu, Xiaotong Cui, Minjia Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.06671v1.pdf)  
  Keywords: ar, 3d gaussian, compression, gaussian splatting, fast  
- **[LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+
  FPS](https://arxiv.org/abs/2507.07136v1)**  
  Authors: Wanhua Li, Yujie Zhao, Minghan Qin, Yang Liu, Yuanhao Cai, Chuang Gan, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07136v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://langsplat-v2.github.io.)  
  Keywords: ar, efficient, high quality, gaussian splatting, fast, semantic  

### Applications

*Showing the latest 50 out of 995 papers*

- **[Unposed 3DGS Reconstruction with Probabilistic Procrustes Mapping](https://arxiv.org/abs/2507.18541v1)**  
  Authors: Chong Cheng, Zijian Wang, Sicheng Yu, Yu Hu, Nanjie Yao, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18541v1.pdf)  
  Keywords: ar, 3d gaussian, outdoor, geometry, mapping, gaussian splatting  
- **[CRUISE: Cooperative Reconstruction and Editing in V2X Scenarios using
  Gaussian Splatting](https://arxiv.org/abs/2507.18473v1)**  
  Authors: Haoran Xu, Saining Zhang, Peishuo Li, Baijun Ye, Xiaoxue Chen, Huan-ang Gao, Jv Zheng, Xiaowei Song, Ziqiao Peng, Run Miao, Jinrang Jia, Yifeng Shi, Guangqi Yi, Hang Zhao, Hao Tang, Hongyang Li, Kaicheng Yu, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18473v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, autonomous driving, tracking  
- **[MVG4D: Image Matrix-Based Multi-View and Motion Generation for 4D
  Content Creation from a Single Image](https://arxiv.org/abs/2507.18371v1)**  
  Authors: Xiaotian Chen, DongFu Yin, Fei Richard Yu, Xuanchen Li, Xinhao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18371v1.pdf)  
  Keywords: ar, 3d gaussian, motion, deformation, efficient, 4d, lightweight, vr, high-fidelity, dynamic, gaussian splatting  
- **[G2S-ICP SLAM: Geometry-aware Gaussian Splatting ICP SLAM](https://arxiv.org/abs/2507.18344v1)**  
  Authors: Gyuhyeon Pak, Hae Min Cho, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18344v1.pdf)  
  Keywords: ar, face, geometry, high-fidelity, 3d reconstruction, gaussian splatting, slam, localization, tracking  
- **[PS-GS: Gaussian Splatting for Multi-View Photometric Stereo](https://arxiv.org/abs/2507.18231v1)**  
  Authors: Yixiao Chen, Bin Liang, Hanzhi Guo, Yongqing Cheng, Jiayi Zhao, Dongdong Weng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18231v1.pdf)  
  Keywords: ar, lighting, geometry, efficient, illumination, 3d reconstruction, relighting, gaussian splatting  
- **[GeoAvatar: Adaptive Geometrical Gaussian Splatting for 3D Head Avatar](https://arxiv.org/abs/2507.18155v1)**  
  Authors: SeungJun Moon, Hah Min Lew, Seungeun Lee, Ji-Su Kang, Gyeong-Moon Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18155v1.pdf)  
  Keywords: avatar, ar, animation, face, motion, deformation, dynamic, gaussian splatting, head  
- **[High-fidelity 3D Gaussian Inpainting: preserving multi-view consistency
  and photorealistic details](https://arxiv.org/abs/2507.18023v1)**  
  Authors: Jun Zhou, Dinghao Li, Nannan Li, Mingjie Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18023v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, 3d reconstruction, nerf, gaussian splatting, localization  
- **[Temporal Smoothness-Aware Rate-Distortion Optimized 4D Gaussian
  Splatting](https://arxiv.org/abs/2507.17336v1)**  
  Authors: Hyeongmin Lee, Kyungjune Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.17336v1.pdf)  
  Keywords: ar, 3d gaussian, motion, efficient, 4d, compression, high-fidelity, dynamic, gaussian splatting  
- **[StreamME: Simplify 3D Gaussian Avatar within Live Stream](https://arxiv.org/abs/2507.17029v1)**  
  Authors: Luchuan Song, Yang Zhou, Zhan Xu, Yi Zhou, Deepali Aneja, Chenliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.17029v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://songluchuan.github.io/StreamME/.)  
  Keywords: avatar, ar, 3d gaussian, animation, face, lighting, geometry, vr, relighting, gaussian splatting, fast, head  
- **[EarthCrafter: Scalable 3D Earth Generation via Dual-Sparse Latent
  Diffusion](https://arxiv.org/abs/2507.16535v2)**  
  Authors: Shang Liu, Chenjie Cao, Chaohui Yu, Wen Qian, Jing Wang, Fan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16535v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://whiteinblue.github.io/earthcrafter/)  
  Keywords: face, geometry, compact, ar, semantic, segmentation  

### Avatar Generation

*Showing the latest 50 out of 330 papers*

- **[G2S-ICP SLAM: Geometry-aware Gaussian Splatting ICP SLAM](https://arxiv.org/abs/2507.18344v1)**  
  Authors: Gyuhyeon Pak, Hae Min Cho, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18344v1.pdf)  
  Keywords: ar, face, geometry, high-fidelity, 3d reconstruction, gaussian splatting, slam, localization, tracking  
- **[GeoAvatar: Adaptive Geometrical Gaussian Splatting for 3D Head Avatar](https://arxiv.org/abs/2507.18155v1)**  
  Authors: SeungJun Moon, Hah Min Lew, Seungeun Lee, Ji-Su Kang, Gyeong-Moon Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18155v1.pdf)  
  Keywords: avatar, ar, animation, face, motion, deformation, dynamic, gaussian splatting, head  
- **[StreamME: Simplify 3D Gaussian Avatar within Live Stream](https://arxiv.org/abs/2507.17029v1)**  
  Authors: Luchuan Song, Yang Zhou, Zhan Xu, Yi Zhou, Deepali Aneja, Chenliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.17029v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://songluchuan.github.io/StreamME/.)  
  Keywords: avatar, ar, 3d gaussian, animation, face, lighting, geometry, vr, relighting, gaussian splatting, fast, head  
- **[EarthCrafter: Scalable 3D Earth Generation via Dual-Sparse Latent
  Diffusion](https://arxiv.org/abs/2507.16535v2)**  
  Authors: Shang Liu, Chenjie Cao, Chaohui Yu, Wen Qian, Jing Wang, Fan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16535v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://whiteinblue.github.io/earthcrafter/)  
  Keywords: face, geometry, compact, ar, semantic, segmentation  
- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: ar, 3d gaussian, face, motion, geometry, compact, dynamic, gaussian splatting, localization, semantic  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: ar, 3d gaussian, face, ray marching, lighting, geometry, relightable, efficient, relighting, gaussian splatting, efficient rendering  
- **[SurfaceSplat: Connecting Surface Reconstruction and Gaussian Splatting](https://arxiv.org/abs/2507.15602v1)**  
  Authors: Zihui Gao, Jia-Wang Bian, Guosheng Lin, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15602v1.pdf)  
  Keywords: ar, 3d gaussian, face, geometry, sparse-view, gaussian splatting  
- **[GCC: A 3DGS Inference Architecture with Gaussian-Wise and Cross-Stage
  Conditional Processing](https://arxiv.org/abs/2507.15300v2)**  
  Authors: Minnan Pei, Gang Li, Junwen Si, Zeyu Zhu, Zitao Mo, Peisong Wang, Zhuoran Song, Xiaoyao Liang, Jian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15300v2.pdf)  
  Keywords: ar, 3d gaussian, neural rendering, compact, efficient, high-fidelity, dynamic, gaussian splatting, fast, head  
- **[Stereo-GS: Multi-View Stereo Vision Model for Generalizable 3D Gaussian
  Splatting Reconstruction](https://arxiv.org/abs/2507.14921v1)**  
  Authors: Xiufeng Huang, Ka Chun Cheung, Runmin Cong, Simon See, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14921v1.pdf)  
  Keywords: ar, 3d gaussian, geometry, efficient, 3d reconstruction, gaussian splatting, head  
- **[DCHM: Depth-Consistent Human Modeling for Multiview Detection](https://arxiv.org/abs/2507.14505v1)**  
  Authors: Jiahao Ma, Tianyu Wang, Miaomiao Liu, David Ahmedt-Aristizabal, Chuong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14505v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiahao-ma.github.io/DCHM/}{project)  
  Keywords: ar, human, sparse-view, gaussian splatting, localization, segmentation  

### Dynamic Scene

*Showing the latest 50 out of 400 papers*

- **[CRUISE: Cooperative Reconstruction and Editing in V2X Scenarios using
  Gaussian Splatting](https://arxiv.org/abs/2507.18473v1)**  
  Authors: Haoran Xu, Saining Zhang, Peishuo Li, Baijun Ye, Xiaoxue Chen, Huan-ang Gao, Jv Zheng, Xiaowei Song, Ziqiao Peng, Run Miao, Jinrang Jia, Yifeng Shi, Guangqi Yi, Hang Zhao, Hao Tang, Hongyang Li, Kaicheng Yu, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18473v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, autonomous driving, tracking  
- **[MVG4D: Image Matrix-Based Multi-View and Motion Generation for 4D
  Content Creation from a Single Image](https://arxiv.org/abs/2507.18371v1)**  
  Authors: Xiaotian Chen, DongFu Yin, Fei Richard Yu, Xuanchen Li, Xinhao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18371v1.pdf)  
  Keywords: ar, 3d gaussian, motion, deformation, efficient, 4d, lightweight, vr, high-fidelity, dynamic, gaussian splatting  
- **[GeoAvatar: Adaptive Geometrical Gaussian Splatting for 3D Head Avatar](https://arxiv.org/abs/2507.18155v1)**  
  Authors: SeungJun Moon, Hah Min Lew, Seungeun Lee, Ji-Su Kang, Gyeong-Moon Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18155v1.pdf)  
  Keywords: avatar, ar, animation, face, motion, deformation, dynamic, gaussian splatting, head  
- **[Temporal Smoothness-Aware Rate-Distortion Optimized 4D Gaussian
  Splatting](https://arxiv.org/abs/2507.17336v1)**  
  Authors: Hyeongmin Lee, Kyungjune Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.17336v1.pdf)  
  Keywords: ar, 3d gaussian, motion, efficient, 4d, compression, high-fidelity, dynamic, gaussian splatting  
- **[StreamME: Simplify 3D Gaussian Avatar within Live Stream](https://arxiv.org/abs/2507.17029v1)**  
  Authors: Luchuan Song, Yang Zhou, Zhan Xu, Yi Zhou, Deepali Aneja, Chenliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.17029v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://songluchuan.github.io/StreamME/.)  
  Keywords: avatar, ar, 3d gaussian, animation, face, lighting, geometry, vr, relighting, gaussian splatting, fast, head  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: survey, ar, 3d gaussian, geometry, motion, sparse-view, robotics, vr, 3d reconstruction, nerf, gaussian splatting  
- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: ar, 3d gaussian, face, motion, geometry, compact, dynamic, gaussian splatting, localization, semantic  
- **[ObjectGS: Object-aware Scene Reconstruction and Scene Understanding via
  Gaussian Splatting](https://arxiv.org/abs/2507.15454v1)**  
  Authors: Ruijie Zhu, Mulin Yu, Linning Xu, Lihan Jiang, Yixuan Li, Tianzhu Zhang, Jiangmiao Pang, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15454v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ruijiezhu94.github.io/ObjectGS_page)  
  Keywords: ar, 3d gaussian, understanding, high-fidelity, dynamic, gaussian splatting, semantic, segmentation  
- **[GCC: A 3DGS Inference Architecture with Gaussian-Wise and Cross-Stage
  Conditional Processing](https://arxiv.org/abs/2507.15300v2)**  
  Authors: Minnan Pei, Gang Li, Junwen Si, Zeyu Zhu, Zitao Mo, Peisong Wang, Zhuoran Song, Xiaoyao Liang, Jian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15300v2.pdf)  
  Keywords: ar, 3d gaussian, neural rendering, compact, efficient, high-fidelity, dynamic, gaussian splatting, fast, head  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v1)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v1.pdf)  
  Keywords: survey, ar, 3d gaussian, lighting, human, robotics, vr, 3d reconstruction, nerf, dynamic, gaussian splatting, slam, fast  

### Few-shot

*Showing the latest 50 out of 72 papers*

- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: survey, ar, 3d gaussian, geometry, motion, sparse-view, robotics, vr, 3d reconstruction, nerf, gaussian splatting  
- **[DWTGS: Rethinking Frequency Regularization for Sparse-view 3D Gaussian
  Splatting](https://arxiv.org/abs/2507.15690v1)**  
  Authors: Hung Nguyen, Runfa Li, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15690v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, sparse-view  
- **[SurfaceSplat: Connecting Surface Reconstruction and Gaussian Splatting](https://arxiv.org/abs/2507.15602v1)**  
  Authors: Zihui Gao, Jia-Wang Bian, Guosheng Lin, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15602v1.pdf)  
  Keywords: ar, 3d gaussian, face, geometry, sparse-view, gaussian splatting  
- **[DCHM: Depth-Consistent Human Modeling for Multiview Detection](https://arxiv.org/abs/2507.14505v1)**  
  Authors: Jiahao Ma, Tianyu Wang, Miaomiao Liu, David Ahmedt-Aristizabal, Chuong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14505v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiahao-ma.github.io/DCHM/}{project)  
  Keywords: ar, human, sparse-view, gaussian splatting, localization, segmentation  
- **[BRUM: Robust 3D Vehicle Reconstruction from 360 Sparse Images](https://arxiv.org/abs/2507.12095v1)**  
  Authors: Davide Di Nucci, Matteo Tomei, Guido Borghi, Luca Ciuffreda, Roberto Vezzani, Rita Cucchiara  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12095v1.pdf)  
  Keywords: ar, motion, sparse-view, 3d reconstruction, gaussian splatting  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: ar, sparse view, face, geometry, sparse-view, understanding, reflection, dynamic, gaussian splatting  
- **[Learning human-to-robot handovers through 3D scene reconstruction](https://arxiv.org/abs/2507.08726v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08726v1.pdf)  
  Keywords: gaussian splatting, ar, human, sparse-view  
- **[RegGS: Unposed Sparse Views Gaussian Splatting with 3DGS Registration](https://arxiv.org/abs/2507.08136v2)**  
  Authors: Chong Cheng, Yu Hu, Sicheng Yu, Beizhen Zhao, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08136v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/reggs/.)  
  Keywords: ar, 3d gaussian, sparse view, geometry, efficient, gaussian splatting  
- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from
  RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: ar, motion, sparse-view, dynamic, gaussian splatting  
- **[PointGS: Point Attention-Aware Sparse View Synthesis with Gaussian
  Splatting](https://arxiv.org/abs/2506.10335v1)**  
  Authors: Lintao Xiang, Hongpei Zheng, Yating Huang, Qijun Yang, Hujun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.10335v1.pdf)  
  Keywords: ar, 3d gaussian, sparse view, few-shot, lightweight, nerf, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 322 papers*

- **[Unposed 3DGS Reconstruction with Probabilistic Procrustes Mapping](https://arxiv.org/abs/2507.18541v1)**  
  Authors: Chong Cheng, Zijian Wang, Sicheng Yu, Yu Hu, Nanjie Yao, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18541v1.pdf)  
  Keywords: ar, 3d gaussian, outdoor, geometry, mapping, gaussian splatting  
- **[G2S-ICP SLAM: Geometry-aware Gaussian Splatting ICP SLAM](https://arxiv.org/abs/2507.18344v1)**  
  Authors: Gyuhyeon Pak, Hae Min Cho, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18344v1.pdf)  
  Keywords: ar, face, geometry, high-fidelity, 3d reconstruction, gaussian splatting, slam, localization, tracking  
- **[PS-GS: Gaussian Splatting for Multi-View Photometric Stereo](https://arxiv.org/abs/2507.18231v1)**  
  Authors: Yixiao Chen, Bin Liang, Hanzhi Guo, Yongqing Cheng, Jiayi Zhao, Dongdong Weng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18231v1.pdf)  
  Keywords: ar, lighting, geometry, efficient, illumination, 3d reconstruction, relighting, gaussian splatting  
- **[High-fidelity 3D Gaussian Inpainting: preserving multi-view consistency
  and photorealistic details](https://arxiv.org/abs/2507.18023v1)**  
  Authors: Jun Zhou, Dinghao Li, Nannan Li, Mingjie Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18023v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, 3d reconstruction, nerf, gaussian splatting, localization  
- **[StreamME: Simplify 3D Gaussian Avatar within Live Stream](https://arxiv.org/abs/2507.17029v1)**  
  Authors: Luchuan Song, Yang Zhou, Zhan Xu, Yi Zhou, Deepali Aneja, Chenliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.17029v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://songluchuan.github.io/StreamME/.)  
  Keywords: avatar, ar, 3d gaussian, animation, face, lighting, geometry, vr, relighting, gaussian splatting, fast, head  
- **[EarthCrafter: Scalable 3D Earth Generation via Dual-Sparse Latent
  Diffusion](https://arxiv.org/abs/2507.16535v2)**  
  Authors: Shang Liu, Chenjie Cao, Chaohui Yu, Wen Qian, Jing Wang, Fan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16535v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://whiteinblue.github.io/earthcrafter/)  
  Keywords: face, geometry, compact, ar, semantic, segmentation  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: survey, ar, 3d gaussian, geometry, motion, sparse-view, robotics, vr, 3d reconstruction, nerf, gaussian splatting  
- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: ar, 3d gaussian, face, motion, geometry, compact, dynamic, gaussian splatting, localization, semantic  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: ar, 3d gaussian, face, ray marching, lighting, geometry, relightable, efficient, relighting, gaussian splatting, efficient rendering  
- **[SurfaceSplat: Connecting Surface Reconstruction and Gaussian Splatting](https://arxiv.org/abs/2507.15602v1)**  
  Authors: Zihui Gao, Jia-Wang Bian, Guosheng Lin, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15602v1.pdf)  
  Keywords: ar, 3d gaussian, face, geometry, sparse-view, gaussian splatting  

### Large Scene

*Showing the latest 50 out of 63 papers*

- **[Unposed 3DGS Reconstruction with Probabilistic Procrustes Mapping](https://arxiv.org/abs/2507.18541v1)**  
  Authors: Chong Cheng, Zijian Wang, Sicheng Yu, Yu Hu, Nanjie Yao, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18541v1.pdf)  
  Keywords: ar, 3d gaussian, outdoor, geometry, mapping, gaussian splatting  
- **[MUVOD: A Novel Multi-view Video Object Segmentation Dataset and A
  Benchmark for 3D Segmentation](https://arxiv.org/abs/2507.07519v1)**  
  Authors: Bangning Wei, Joshua Maraval, Meriem Outtas, Kidiyo Kpalma, Nicolas Ramin, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07519v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://volumetric-repository.labs.b-com.com/#/muvod.)  
  Keywords: ar, 3d gaussian, outdoor, motion, 4d, understanding, nerf, dynamic, gaussian splatting, segmentation  
- **[3DGS_LSR:Large_Scale Relocation for Autonomous Driving Based on 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.05661v1)**  
  Authors: Haitao Lu, Haijier Chen, Haoze Liu, Shoujian Zhang, Bo Xu, Ziao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05661v1.pdf)  
  Keywords: ar, 3d gaussian, outdoor, mapping, gaussian splatting, autonomous driving, localization  
- **[ArmGS: Composite Gaussian Appearance Refinement for Modeling Dynamic
  Urban Environments](https://arxiv.org/abs/2507.03886v1)**  
  Authors: Guile Wu, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.03886v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, autonomous driving, dynamic, gaussian splatting, urban scene, real-time rendering  
- **[Outdoor Monocular SLAM with Global Scale-Consistent 3D Gaussian
  Pointmaps](https://arxiv.org/abs/2507.03737v2)**  
  Authors: Chong Cheng, Sicheng Yu, Zijian Wang, Yifan Zhou, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.03737v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/S3PO-GS/.)  
  Keywords: ar, 3d gaussian, outdoor, mapping, high-fidelity, dynamic, gaussian splatting, slam, tracking  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: ar, 3d gaussian, outdoor, lighting, geometry, mapping, illumination, high-fidelity, dynamic, gaussian splatting, slam, tracking  
- **[BézierGS: Dynamic Urban Scene Reconstruction with Bézier Curve
  Gaussian Splatting](https://arxiv.org/abs/2506.22099v3)**  
  Authors: Zipei Ma, Junzhe Jiang, Yurui Chen, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22099v3.pdf)  
  Keywords: ar, motion, urban scene, dynamic, gaussian splatting, autonomous driving  
- **[ICP-3DGS: SfM-free 3D Gaussian Splatting for Large-scale Unbounded
  Scenes](https://arxiv.org/abs/2506.21629v1)**  
  Authors: Chenhao Zhang, Yezhi Shen, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21629v1.pdf)  
  Keywords: ar, 3d gaussian, neural rendering, outdoor, motion, nerf, gaussian splatting  
- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: ar, 3d gaussian, outdoor, gaussian splatting, slam, tracking  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: survey, ar, 3d gaussian, face, outdoor, efficient, high-fidelity, nerf, dynamic, gaussian splatting, autonomous driving  

### Model Compression

*Showing the latest 50 out of 398 papers*

- **[MVG4D: Image Matrix-Based Multi-View and Motion Generation for 4D
  Content Creation from a Single Image](https://arxiv.org/abs/2507.18371v1)**  
  Authors: Xiaotian Chen, DongFu Yin, Fei Richard Yu, Xuanchen Li, Xinhao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18371v1.pdf)  
  Keywords: ar, 3d gaussian, motion, deformation, efficient, 4d, lightweight, vr, high-fidelity, dynamic, gaussian splatting  
- **[PS-GS: Gaussian Splatting for Multi-View Photometric Stereo](https://arxiv.org/abs/2507.18231v1)**  
  Authors: Yixiao Chen, Bin Liang, Hanzhi Guo, Yongqing Cheng, Jiayi Zhao, Dongdong Weng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18231v1.pdf)  
  Keywords: ar, lighting, geometry, efficient, illumination, 3d reconstruction, relighting, gaussian splatting  
- **[Temporal Smoothness-Aware Rate-Distortion Optimized 4D Gaussian
  Splatting](https://arxiv.org/abs/2507.17336v1)**  
  Authors: Hyeongmin Lee, Kyungjune Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.17336v1.pdf)  
  Keywords: ar, 3d gaussian, motion, efficient, 4d, compression, high-fidelity, dynamic, gaussian splatting  
- **[EarthCrafter: Scalable 3D Earth Generation via Dual-Sparse Latent
  Diffusion](https://arxiv.org/abs/2507.16535v2)**  
  Authors: Shang Liu, Chenjie Cao, Chaohui Yu, Wen Qian, Jing Wang, Fan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16535v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://whiteinblue.github.io/earthcrafter/)  
  Keywords: face, geometry, compact, ar, semantic, segmentation  
- **[LongSplat: Online Generalizable 3D Gaussian Splatting from Long Sequence
  Images](https://arxiv.org/abs/2507.16144v1)**  
  Authors: Guichen Huang, Ruoyu Wang, Xiangjun Gao, Che Sun, Yuwei Wu, Shenghua Gao, Yunde Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16144v1.pdf)  
  Keywords: ar, 3d gaussian, compact, efficient, compression, high-fidelity, gaussian splatting  
- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: ar, 3d gaussian, face, motion, geometry, compact, dynamic, gaussian splatting, localization, semantic  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: ar, 3d gaussian, face, ray marching, lighting, geometry, relightable, efficient, relighting, gaussian splatting, efficient rendering  
- **[GCC: A 3DGS Inference Architecture with Gaussian-Wise and Cross-Stage
  Conditional Processing](https://arxiv.org/abs/2507.15300v2)**  
  Authors: Minnan Pei, Gang Li, Junwen Si, Zeyu Zhu, Zitao Mo, Peisong Wang, Zhuoran Song, Xiaoyao Liang, Jian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15300v2.pdf)  
  Keywords: ar, 3d gaussian, neural rendering, compact, efficient, high-fidelity, dynamic, gaussian splatting, fast, head  
- **[Stereo-GS: Multi-View Stereo Vision Model for Generalizable 3D Gaussian
  Splatting Reconstruction](https://arxiv.org/abs/2507.14921v1)**  
  Authors: Xiufeng Huang, Ka Chun Cheung, Runmin Cong, Simon See, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14921v1.pdf)  
  Keywords: ar, 3d gaussian, geometry, efficient, 3d reconstruction, gaussian splatting, head  
- **[Adaptive 3D Gaussian Splatting Video Streaming](https://arxiv.org/abs/2507.14432v1)**  
  Authors: Han Gong, Qiyue Li, Zhi Liu, Hao Zhou, Peng Yuan Zhou, Zhu Li, Jie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14432v1.pdf)  
  Keywords: ar, 3d gaussian, deformation, efficient, compression, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 163 papers*

- **[MVG4D: Image Matrix-Based Multi-View and Motion Generation for 4D
  Content Creation from a Single Image](https://arxiv.org/abs/2507.18371v1)**  
  Authors: Xiaotian Chen, DongFu Yin, Fei Richard Yu, Xuanchen Li, Xinhao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18371v1.pdf)  
  Keywords: ar, 3d gaussian, motion, deformation, efficient, 4d, lightweight, vr, high-fidelity, dynamic, gaussian splatting  
- **[G2S-ICP SLAM: Geometry-aware Gaussian Splatting ICP SLAM](https://arxiv.org/abs/2507.18344v1)**  
  Authors: Gyuhyeon Pak, Hae Min Cho, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18344v1.pdf)  
  Keywords: ar, face, geometry, high-fidelity, 3d reconstruction, gaussian splatting, slam, localization, tracking  
- **[High-fidelity 3D Gaussian Inpainting: preserving multi-view consistency
  and photorealistic details](https://arxiv.org/abs/2507.18023v1)**  
  Authors: Jun Zhou, Dinghao Li, Nannan Li, Mingjie Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18023v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, 3d reconstruction, nerf, gaussian splatting, localization  
- **[Temporal Smoothness-Aware Rate-Distortion Optimized 4D Gaussian
  Splatting](https://arxiv.org/abs/2507.17336v1)**  
  Authors: Hyeongmin Lee, Kyungjune Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.17336v1.pdf)  
  Keywords: ar, 3d gaussian, motion, efficient, 4d, compression, high-fidelity, dynamic, gaussian splatting  
- **[LongSplat: Online Generalizable 3D Gaussian Splatting from Long Sequence
  Images](https://arxiv.org/abs/2507.16144v1)**  
  Authors: Guichen Huang, Ruoyu Wang, Xiangjun Gao, Che Sun, Yuwei Wu, Shenghua Gao, Yunde Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16144v1.pdf)  
  Keywords: ar, 3d gaussian, compact, efficient, compression, high-fidelity, gaussian splatting  
- **[ObjectGS: Object-aware Scene Reconstruction and Scene Understanding via
  Gaussian Splatting](https://arxiv.org/abs/2507.15454v1)**  
  Authors: Ruijie Zhu, Mulin Yu, Linning Xu, Lihan Jiang, Yixuan Li, Tianzhu Zhang, Jiangmiao Pang, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15454v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ruijiezhu94.github.io/ObjectGS_page)  
  Keywords: ar, 3d gaussian, understanding, high-fidelity, dynamic, gaussian splatting, semantic, segmentation  
- **[GCC: A 3DGS Inference Architecture with Gaussian-Wise and Cross-Stage
  Conditional Processing](https://arxiv.org/abs/2507.15300v2)**  
  Authors: Minnan Pei, Gang Li, Junwen Si, Zeyu Zhu, Zitao Mo, Peisong Wang, Zhuoran Song, Xiaoyao Liang, Jian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15300v2.pdf)  
  Keywords: ar, 3d gaussian, neural rendering, compact, efficient, high-fidelity, dynamic, gaussian splatting, fast, head  
- **[A Mixed-Primitive-based Gaussian Splatting Method for Surface
  Reconstruction](https://arxiv.org/abs/2507.11321v1)**  
  Authors: Haoxuan Qu, Yujun Cai, Hossein Rahmani, Ajay Kumar, Junsong Yuan, Jun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11321v1.pdf)  
  Keywords: gaussian splatting, ar, face, high quality  
- **[ScaffoldAvatar: High-Fidelity Gaussian Avatars with Patch Expressions](https://arxiv.org/abs/2507.10542v1)**  
  Authors: Shivangi Aneja, Sebastian Weiss, Irene Baeza, Prashanth Chandran, Gaspard Zoss, Matthias Nießner, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.10542v1.pdf)  
  Keywords: avatar, ar, 3d gaussian, face, motion, human, high-fidelity, dynamic, gaussian splatting, fast, head  
- **[LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+
  FPS](https://arxiv.org/abs/2507.07136v1)**  
  Authors: Wanhua Li, Yujie Zhao, Minghan Qin, Yang Liu, Yuanhao Cai, Chuang Gan, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07136v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://langsplat-v2.github.io.)  
  Keywords: ar, efficient, high quality, gaussian splatting, fast, semantic  

### Ray Tracing

- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: ar, 3d gaussian, face, ray marching, lighting, geometry, relightable, efficient, relighting, gaussian splatting, efficient rendering  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: ar, efficient, high-fidelity, ray tracing, gaussian splatting, real-time rendering  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: avatar, ar, lighting, geometry, relightable, ray tracing, human, shadow, relighting, gaussian splatting, fast  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: ar, 3d gaussian, lighting, acceleration, efficient, relighting, ray tracing, gaussian splatting, efficient rendering  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: ar, 3d gaussian, animation, ray marching, acceleration, compact, efficient, dynamic, gaussian splatting  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: ar, 3d gaussian, face, lighting, efficient, illumination, global illumination, ray tracing, gaussian splatting, real-time rendering  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: ar, 3d gaussian, neural rendering, reflection, shadow, ray tracing, gaussian splatting, fast  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: face, lighting, reflection, shadow, ray tracing, gaussian splatting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation
  Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, ar, 3d gaussian, ray tracing, gaussian splatting  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: ar, light transport, acceleration, efficient, reflection, ray tracing, gaussian splatting  

### Relighting

*Showing the latest 50 out of 112 papers*

- **[PS-GS: Gaussian Splatting for Multi-View Photometric Stereo](https://arxiv.org/abs/2507.18231v1)**  
  Authors: Yixiao Chen, Bin Liang, Hanzhi Guo, Yongqing Cheng, Jiayi Zhao, Dongdong Weng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18231v1.pdf)  
  Keywords: ar, lighting, geometry, efficient, illumination, 3d reconstruction, relighting, gaussian splatting  
- **[StreamME: Simplify 3D Gaussian Avatar within Live Stream](https://arxiv.org/abs/2507.17029v1)**  
  Authors: Luchuan Song, Yang Zhou, Zhan Xu, Yi Zhou, Deepali Aneja, Chenliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.17029v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://songluchuan.github.io/StreamME/.)  
  Keywords: avatar, ar, 3d gaussian, animation, face, lighting, geometry, vr, relighting, gaussian splatting, fast, head  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: ar, 3d gaussian, face, ray marching, lighting, geometry, relightable, efficient, relighting, gaussian splatting, efficient rendering  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v1)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v1.pdf)  
  Keywords: survey, ar, 3d gaussian, lighting, human, robotics, vr, 3d reconstruction, nerf, dynamic, gaussian splatting, slam, fast  
- **[Neural-GASh: A CGA-based neural radiance prediction pipeline for
  real-time shading](https://arxiv.org/abs/2507.13917v1)**  
  Authors: Efstratios Geronikolakis, Manos Kamarianakis, Antonis Protopsaltis, George Papagiannakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13917v1.pdf)  
  Keywords: 3d gaussian, light transport, efficient, vr, dynamic, ar, fast  
- **[TexGS-VolVis: Expressive Scene Editing for Volume Visualization via
  Textured Gaussian Splatting](https://arxiv.org/abs/2507.13586v1)**  
  Authors: Kaiyuan Tang, Kuangshi Ai, Jun Han, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13586v1.pdf)  
  Keywords: ar, 3d gaussian, lighting, geometry, segmentation, gaussian splatting, real-time rendering  
- **[Wavelet-GS: 3D Gaussian Splatting with Wavelet Decomposition](https://arxiv.org/abs/2507.12498v2)**  
  Authors: Beizhen Zhao, Yifan Zhou, Sicheng Yu, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12498v2.pdf)  
  Keywords: ar, 3d gaussian, face, lighting, gaussian splatting  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: ar, sparse view, face, geometry, sparse-view, understanding, reflection, dynamic, gaussian splatting  
- **[RTR-GS: 3D Gaussian Splatting for Inverse Rendering with Radiance
  Transfer and Reflection](https://arxiv.org/abs/2507.07733v1)**  
  Authors: Yongyang Zhou, Fang-Lue Zhang, Zichen Wang, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07733v1.pdf)  
  Keywords: ar, 3d gaussian, lighting, efficient, reflection, relighting, gaussian splatting  
- **[Seg-Wild: Interactive Segmentation based on 3D Gaussian Splatting for
  Unconstrained Image Collections](https://arxiv.org/abs/2507.07395v1)**  
  Authors: Yongtang Bao, Chengjie Tang, Yuze Wang, Haojie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07395v1.pdf)  
  Keywords: ar, 3d gaussian, lighting, gaussian splatting, segmentation  

### SLAM

*Showing the latest 50 out of 158 papers*

- **[Unposed 3DGS Reconstruction with Probabilistic Procrustes Mapping](https://arxiv.org/abs/2507.18541v1)**  
  Authors: Chong Cheng, Zijian Wang, Sicheng Yu, Yu Hu, Nanjie Yao, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18541v1.pdf)  
  Keywords: ar, 3d gaussian, outdoor, geometry, mapping, gaussian splatting  
- **[CRUISE: Cooperative Reconstruction and Editing in V2X Scenarios using
  Gaussian Splatting](https://arxiv.org/abs/2507.18473v1)**  
  Authors: Haoran Xu, Saining Zhang, Peishuo Li, Baijun Ye, Xiaoxue Chen, Huan-ang Gao, Jv Zheng, Xiaowei Song, Ziqiao Peng, Run Miao, Jinrang Jia, Yifeng Shi, Guangqi Yi, Hang Zhao, Hao Tang, Hongyang Li, Kaicheng Yu, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18473v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, autonomous driving, tracking  
- **[G2S-ICP SLAM: Geometry-aware Gaussian Splatting ICP SLAM](https://arxiv.org/abs/2507.18344v1)**  
  Authors: Gyuhyeon Pak, Hae Min Cho, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18344v1.pdf)  
  Keywords: ar, face, geometry, high-fidelity, 3d reconstruction, gaussian splatting, slam, localization, tracking  
- **[High-fidelity 3D Gaussian Inpainting: preserving multi-view consistency
  and photorealistic details](https://arxiv.org/abs/2507.18023v1)**  
  Authors: Jun Zhou, Dinghao Li, Nannan Li, Mingjie Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18023v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, 3d reconstruction, nerf, gaussian splatting, localization  
- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: ar, 3d gaussian, face, motion, geometry, compact, dynamic, gaussian splatting, localization, semantic  
- **[DCHM: Depth-Consistent Human Modeling for Multiview Detection](https://arxiv.org/abs/2507.14505v1)**  
  Authors: Jiahao Ma, Tianyu Wang, Miaomiao Liu, David Ahmedt-Aristizabal, Chuong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14505v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiahao-ma.github.io/DCHM/}{project)  
  Keywords: ar, human, sparse-view, gaussian splatting, localization, segmentation  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v1)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v1.pdf)  
  Keywords: survey, ar, 3d gaussian, lighting, human, robotics, vr, 3d reconstruction, nerf, dynamic, gaussian splatting, slam, fast  
- **[VolSegGS: Segmentation and Tracking in Dynamic Volumetric Scenes via
  Deformable 3D Gaussians](https://arxiv.org/abs/2507.12667v1)**  
  Authors: Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12667v1.pdf)  
  Keywords: ar, 3d gaussian, deformation, dynamic, gaussian splatting, tracking, segmentation  
- **[SGLoc: Semantic Localization System for Camera Pose Estimation from 3D
  Gaussian Splatting Representation](https://arxiv.org/abs/2507.12027v1)**  
  Authors: Beining Xu, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12027v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, localization, semantic  
- **[Robust 3D-Masked Part-level Editing in 3D Gaussian Splatting with
  Regularized Score Distillation Sampling](https://arxiv.org/abs/2507.11061v2)**  
  Authors: Hayeon Kim, Ji Ha Jang, Se Young Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11061v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://janeyeon.github.io/romap.)  
  Keywords: ar, 3d gaussian, geometry, efficient, gaussian splatting, slam, segmentation  

### Scene Understanding

*Showing the latest 50 out of 189 papers*

- **[EarthCrafter: Scalable 3D Earth Generation via Dual-Sparse Latent
  Diffusion](https://arxiv.org/abs/2507.16535v2)**  
  Authors: Shang Liu, Chenjie Cao, Chaohui Yu, Wen Qian, Jing Wang, Fan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16535v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://whiteinblue.github.io/earthcrafter/)  
  Keywords: face, geometry, compact, ar, semantic, segmentation  
- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: ar, 3d gaussian, face, motion, geometry, compact, dynamic, gaussian splatting, localization, semantic  
- **[ObjectGS: Object-aware Scene Reconstruction and Scene Understanding via
  Gaussian Splatting](https://arxiv.org/abs/2507.15454v1)**  
  Authors: Ruijie Zhu, Mulin Yu, Linning Xu, Lihan Jiang, Yixuan Li, Tianzhu Zhang, Jiangmiao Pang, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15454v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ruijiezhu94.github.io/ObjectGS_page)  
  Keywords: ar, 3d gaussian, understanding, high-fidelity, dynamic, gaussian splatting, semantic, segmentation  
- **[DCHM: Depth-Consistent Human Modeling for Multiview Detection](https://arxiv.org/abs/2507.14505v1)**  
  Authors: Jiahao Ma, Tianyu Wang, Miaomiao Liu, David Ahmedt-Aristizabal, Chuong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14505v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiahao-ma.github.io/DCHM/}{project)  
  Keywords: ar, human, sparse-view, gaussian splatting, localization, segmentation  
- **[PCR-GS: COLMAP-Free 3D Gaussian Splatting via Pose Co-Regularizations](https://arxiv.org/abs/2507.13891v2)**  
  Authors: Yu Wei, Jiahui Zhang, Xiaoqin Zhang, Ling Shao, Shijian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13891v2.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, semantic  
- **[TexGS-VolVis: Expressive Scene Editing for Volume Visualization via
  Textured Gaussian Splatting](https://arxiv.org/abs/2507.13586v1)**  
  Authors: Kaiyuan Tang, Kuangshi Ai, Jun Han, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.13586v1.pdf)  
  Keywords: ar, 3d gaussian, lighting, geometry, segmentation, gaussian splatting, real-time rendering  
- **[VolSegGS: Segmentation and Tracking in Dynamic Volumetric Scenes via
  Deformable 3D Gaussians](https://arxiv.org/abs/2507.12667v1)**  
  Authors: Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12667v1.pdf)  
  Keywords: ar, 3d gaussian, deformation, dynamic, gaussian splatting, tracking, segmentation  
- **[SGLoc: Semantic Localization System for Camera Pose Estimation from 3D
  Gaussian Splatting Representation](https://arxiv.org/abs/2507.12027v1)**  
  Authors: Beining Xu, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12027v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, localization, semantic  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: ar, sparse view, face, geometry, sparse-view, understanding, reflection, dynamic, gaussian splatting  
- **[Robust 3D-Masked Part-level Editing in 3D Gaussian Splatting with
  Regularized Score Distillation Sampling](https://arxiv.org/abs/2507.11061v2)**  
  Authors: Hayeon Kim, Ji Ha Jang, Se Young Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11061v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://janeyeon.github.io/romap.)  
  Keywords: ar, 3d gaussian, geometry, efficient, gaussian splatting, slam, segmentation  



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