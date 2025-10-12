# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-10-12 00:52:31

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
- [Acceleration](#acceleration) (262 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (994 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (337 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (386 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (73 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (320 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (72 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (414 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (170 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (18 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (117 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (153 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (197 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, neural rendering, fast, efficient, ar, slam, nerf, understanding  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, lighting, segmentation, high-fidelity, ar, semantic, nerf, compact, understanding  
- **[A Study of the Framework and Real-World Applications of Language
  Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, efficient, ar, semantic, robotics, nerf, understanding  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned
  and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, ar, robotics, nerf, human  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, motion, ar, robotics, nerf, geometry, sparse-view, vr, 3d reconstruction  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v3)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Kaichen Zhou, Paul Pu Liang, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v3.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, lighting, fast, vr, ar, slam, dynamic, nerf, robotics, human, 3d reconstruction  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, high-fidelity, efficient, face, ar, autonomous driving, dynamic, nerf, outdoor  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, neural rendering, high-fidelity, ar, autonomous driving, robotics, nerf, vr, 3d reconstruction  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, neural rendering, segmentation, high-fidelity, efficient, ar, semantic, understanding, outdoor, 3d reconstruction  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, segmentation, efficient, localization, ar, semantic, slam, nerf, mapping  

### Acceleration

*Showing the latest 50 out of 262 papers*

- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: gaussian splatting, lighting, light transport, efficient, face, ray tracing, real-time rendering, ar, shadow, relightable  
- **[Capture and Interact: Rapid 3D Object Acquisition and Rendering with
  Gaussian Splatting in Unity](https://arxiv.org/abs/2510.06802v1)**  
  Authors: Islomjon Shukhratov, Sergey Gorinsky  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06802v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, real-time rendering, 3d reconstruction  
- **[RTGS: Real-Time 3D Gaussian Splatting SLAM via Multi-Level Redundancy
  Reduction](https://arxiv.org/abs/2510.06644v2)**  
  Authors: Leshu Li, Jiayin Qin, Jie Peng, Zishen Wan, Huaizhi Qu, Ye Han, Pingqing Zheng, Hongsen Zhang, Yu Cao, Tianlong Chen, Yang Katie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06644v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, localization, ar, slam, dynamic, acceleration, mapping  
- **[ArchitectHead: Continuous Level of Detail Control for 3D Gaussian Head
  Avatars](https://arxiv.org/abs/2510.05488v1)**  
  Authors: Peizhi Yan, Rabab Ward, Qiang Tang, Shan Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.05488v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, efficient, lightweight, ar, real-time rendering, dynamic, avatar  
- **[Optimized Minimal 4D Gaussian Splatting](https://arxiv.org/abs/2510.03857v1)**  
  Authors: Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee, Eunsoo Lee, Sangmin Kim, Seunghyeon Song, Joo Chan Lee, Jong Hwan Ko, Jaesik Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03857v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://minshirley.github.io/OMG4/.)  
  Keywords: compression, gaussian splatting, head, high-fidelity, face, motion, ar, real-time rendering, 4d, dynamic, compact  
- **[FSFSplatter: Build Surface and Novel Views with Sparse-Views within 3min](https://arxiv.org/abs/2510.02691v1)**  
  Authors: Yibin Zhao, Yihan Pan, Jun Nan, Jianjun Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02691v1.pdf)  
  Keywords: gaussian splatting, head, fast, face, ar, geometry, sparse-view  
- **[ROI-GS: Interest-based Local Quality 3D Gaussian Splatting](https://arxiv.org/abs/2510.01978v1)**  
  Authors: Quoc-Anh Bui, Gilles Rougeron, Géraldine Morin, Simone Gasparini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01978v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, fast, efficient, ar  
- **[LOBE-GS: Load-Balanced and Efficient 3D Gaussian Splatting for
  Large-Scale Scene Reconstruction](https://arxiv.org/abs/2510.01767v1)**  
  Authors: Sheng-Hsiang Hung, Ting-Yu Yen, Wei-Fang Sun, Simon See, Shih-Hsuan Hung, Hung-Kuo Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01767v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, high-fidelity, fast, efficient, lightweight, ar, outdoor  
- **[Universal Beta Splatting](https://arxiv.org/abs/2510.03312v1)**  
  Authors: Rong Liu, Zhongpai Gao, Benjamin Planche, Meida Chen, Van Nguyen Nguyen, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Yue Wang, Andrew Feng, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03312v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rongliu-leo.github.io/universal-beta-splatting/.)  
  Keywords: 3d gaussian, gaussian splatting, light transport, face, ar, real-time rendering, dynamic  
- **[LLM-Powered Code Analysis and Optimization for Gaussian Splatting
  Kernels](https://arxiv.org/abs/2509.25626v1)**  
  Authors: Yi Hu, Huiyang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25626v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, real-time rendering, nerf  

### Applications

*Showing the latest 50 out of 994 papers*

- **[ReSplat: Learning Recurrent Gaussian Splats](https://arxiv.org/abs/2510.08575v1)**  
  Authors: Haofei Xu, Daniel Barath, Andreas Geiger, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08575v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haofeixu.github.io/resplat/.)  
  Keywords: 3d gaussian, gaussian splatting, head, efficient, ar, compact  
- **[D$^2$GS: Depth-and-Density Guided Gaussian Splatting for Stable and
  Accurate Sparse-View Reconstruction](https://arxiv.org/abs/2510.08566v1)**  
  Authors: Meixi Song, Xin Lin, Dizhe Zhang, Haodong Li, Xiangtai Li, Bo Du, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08566v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insta360-research-team.github.io/DDGS-website/.)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, ar, sparse-view, sparse view  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: 3d gaussian, gaussian splatting, efficient, ray marching, ar, geometry  
- **[Efficient Label Refinement for Face Parsing Under Extreme Poses Using 3D
  Gaussian Splatting](https://arxiv.org/abs/2510.08096v1)**  
  Authors: Ankit Gahlawat, Anirban Mukherjee, Dinesh Babu Jayagopi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08096v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, head, efficient, face, ar, geometry, human  
- **[CVD-STORM: Cross-View Video Diffusion with Spatial-Temporal
  Reconstruction Model for Autonomous Driving](https://arxiv.org/abs/2510.07944v1)**  
  Authors: Tianrui Zhang, Yichen Liu, Zilin Guo, Yuxin Guo, Jingcheng Ni, Chenjing Ding, Dan Xu, Lewei Lu, Zehuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07944v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, ar, autonomous driving, 4d, dynamic, understanding  
- **[PrismGS: Physically-Grounded Anti-Aliasing for High-Fidelity Large-Scale
  3D Gaussian Splatting](https://arxiv.org/abs/2510.07830v1)**  
  Authors: Houqiang Zhong, Zhenglong Wu, Sihua Fu, Zihan Zheng, Xin Jin, Xiaoyun Zhang, Li Song, Qiang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07830v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, face, ar, compact, geometry  
- **[DEGS: Deformable Event-based 3D Gaussian Splatting from RGB and Event
  Stream](https://arxiv.org/abs/2510.07752v1)**  
  Authors: Junhao He, Jiaxu Wang, Jia Li, Mingyuan Sun, Qiang Zhang, Jiahang Cao, Ziyi Zhang, Yi Gu, Jingkai Sun, Renjing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07752v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, motion, ar, dynamic, geometry, deformation  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: gaussian splatting, lighting, light transport, efficient, face, ray tracing, real-time rendering, ar, shadow, relightable  
- **[Capture and Interact: Rapid 3D Object Acquisition and Rendering with
  Gaussian Splatting in Unity](https://arxiv.org/abs/2510.06802v1)**  
  Authors: Islomjon Shukhratov, Sergey Gorinsky  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06802v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, real-time rendering, 3d reconstruction  
- **[SCas4D: Structural Cascaded Optimization for Boosting Persistent 4D
  Novel View Synthesis](https://arxiv.org/abs/2510.06694v1)**  
  Authors: Jipeng Lyu, Jiahua Dong, Yu-Xiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06694v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, ar, 4d, dynamic, deformation, tracking  

### Avatar Generation

*Showing the latest 50 out of 337 papers*

- **[ReSplat: Learning Recurrent Gaussian Splats](https://arxiv.org/abs/2510.08575v1)**  
  Authors: Haofei Xu, Daniel Barath, Andreas Geiger, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08575v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haofeixu.github.io/resplat/.)  
  Keywords: 3d gaussian, gaussian splatting, head, efficient, ar, compact  
- **[Efficient Label Refinement for Face Parsing Under Extreme Poses Using 3D
  Gaussian Splatting](https://arxiv.org/abs/2510.08096v1)**  
  Authors: Ankit Gahlawat, Anirban Mukherjee, Dinesh Babu Jayagopi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08096v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, head, efficient, face, ar, geometry, human  
- **[PrismGS: Physically-Grounded Anti-Aliasing for High-Fidelity Large-Scale
  3D Gaussian Splatting](https://arxiv.org/abs/2510.07830v1)**  
  Authors: Houqiang Zhong, Zhenglong Wu, Sihua Fu, Zihan Zheng, Xin Jin, Xiaoyun Zhang, Li Song, Qiang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07830v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, face, ar, compact, geometry  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: gaussian splatting, lighting, light transport, efficient, face, ray tracing, real-time rendering, ar, shadow, relightable  
- **[Generating Surface for Text-to-3D using 2D Gaussian Splatting](https://arxiv.org/abs/2510.06967v1)**  
  Authors: Huanning Dong, Fan Li, Ping Kuang, Jianwen Min  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06967v1.pdf)  
  Keywords: high-fidelity, geometry, face, gaussian splatting  
- **[RTGS: Real-Time 3D Gaussian Splatting SLAM via Multi-Level Redundancy
  Reduction](https://arxiv.org/abs/2510.06644v2)**  
  Authors: Leshu Li, Jiayin Qin, Jie Peng, Zishen Wan, Huaizhi Qu, Ye Han, Pingqing Zheng, Hongsen Zhang, Yu Cao, Tianlong Chen, Yang Katie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06644v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, localization, ar, slam, dynamic, acceleration, mapping  
- **[ArchitectHead: Continuous Level of Detail Control for 3D Gaussian Head
  Avatars](https://arxiv.org/abs/2510.05488v1)**  
  Authors: Peizhi Yan, Rabab Ward, Qiang Tang, Shan Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.05488v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, efficient, lightweight, ar, real-time rendering, dynamic, avatar  
- **[Optimized Minimal 4D Gaussian Splatting](https://arxiv.org/abs/2510.03857v1)**  
  Authors: Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee, Eunsoo Lee, Sangmin Kim, Seunghyeon Song, Joo Chan Lee, Jong Hwan Ko, Jaesik Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03857v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://minshirley.github.io/OMG4/.)  
  Keywords: compression, gaussian splatting, head, high-fidelity, face, motion, ar, real-time rendering, 4d, dynamic, compact  
- **[SketchPlan: Diffusion Based Drone Planning From Human Sketches](https://arxiv.org/abs/2510.03545v1)**  
  Authors: Sixten Norelius, Aaron O. Feldman, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03545v1.pdf)  
  Keywords: human, 3d gaussian, gaussian splatting, ar  
- **[GS-Share: Enabling High-fidelity Map Sharing with Incremental Gaussian
  Splatting](https://arxiv.org/abs/2510.02884v1)**  
  Authors: Xinran Zhang, Hanqi Zhu, Yifan Duan, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02884v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, high-fidelity, ar, autonomous driving, compact, 3d reconstruction  

### Dynamic Scene

*Showing the latest 50 out of 386 papers*

- **[CVD-STORM: Cross-View Video Diffusion with Spatial-Temporal
  Reconstruction Model for Autonomous Driving](https://arxiv.org/abs/2510.07944v1)**  
  Authors: Tianrui Zhang, Yichen Liu, Zilin Guo, Yuxin Guo, Jingcheng Ni, Chenjing Ding, Dan Xu, Lewei Lu, Zehuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07944v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, ar, autonomous driving, 4d, dynamic, understanding  
- **[DEGS: Deformable Event-based 3D Gaussian Splatting from RGB and Event
  Stream](https://arxiv.org/abs/2510.07752v1)**  
  Authors: Junhao He, Jiaxu Wang, Jia Li, Mingyuan Sun, Qiang Zhang, Jiahang Cao, Ziyi Zhang, Yi Gu, Jingkai Sun, Renjing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07752v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, motion, ar, dynamic, geometry, deformation  
- **[SCas4D: Structural Cascaded Optimization for Boosting Persistent 4D
  Novel View Synthesis](https://arxiv.org/abs/2510.06694v1)**  
  Authors: Jipeng Lyu, Jiahua Dong, Yu-Xiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06694v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, ar, 4d, dynamic, deformation, tracking  
- **[RTGS: Real-Time 3D Gaussian Splatting SLAM via Multi-Level Redundancy
  Reduction](https://arxiv.org/abs/2510.06644v2)**  
  Authors: Leshu Li, Jiayin Qin, Jie Peng, Zishen Wan, Huaizhi Qu, Ye Han, Pingqing Zheng, Hongsen Zhang, Yu Cao, Tianlong Chen, Yang Katie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06644v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, localization, ar, slam, dynamic, acceleration, mapping  
- **[Active Next-Best-View Optimization for Risk-Averse Path Planning](https://arxiv.org/abs/2510.06481v1)**  
  Authors: Amirhossein Mollaei Khass, Guangyi Liu, Vivek Pandey, Wen Jiang, Boshu Lei, Kostas Daniilidis, Nader Motee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06481v1.pdf)  
  Keywords: efficient, motion, 3d gaussian, ar  
- **[ArchitectHead: Continuous Level of Detail Control for 3D Gaussian Head
  Avatars](https://arxiv.org/abs/2510.05488v1)**  
  Authors: Peizhi Yan, Rabab Ward, Qiang Tang, Shan Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.05488v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, efficient, lightweight, ar, real-time rendering, dynamic, avatar  
- **[Optimized Minimal 4D Gaussian Splatting](https://arxiv.org/abs/2510.03857v1)**  
  Authors: Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee, Eunsoo Lee, Sangmin Kim, Seunghyeon Song, Joo Chan Lee, Jong Hwan Ko, Jaesik Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03857v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://minshirley.github.io/OMG4/.)  
  Keywords: compression, gaussian splatting, head, high-fidelity, face, motion, ar, real-time rendering, 4d, dynamic, compact  
- **[SIMSplat: Predictive Driving Scene Editing with Language-aligned 4D
  Gaussian Splatting](https://arxiv.org/abs/2510.02469v1)**  
  Authors: Sung-Yeon Park, Adam Lee, Juanwu Lu, Can Cui, Luyang Jiang, Rohit Gupta, Kyungtae Han, Ahmadreza Moradipari, Ziran Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sungyeonparkk.github.io/simsplat/)  
  Keywords: gaussian splatting, efficient, motion, ar, 4d  
- **[Performance-Guided Refinement for Visual Aerial Navigation using
  Editable Gaussian Splatting in FalconGym 2.0](https://arxiv.org/abs/2510.02248v1)**  
  Authors: Yan Miao, Ege Yuceel, Georgios Fainekos, Bardh Hoxha, Hideki Okamoto, Sayan Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02248v1.pdf)  
  Keywords: geometry, dynamic, gaussian splatting, ar  
- **[Spec-Gloss Surfels and Normal-Diffuse Priors for Relightable Glossy
  Objects](https://arxiv.org/abs/2510.02069v1)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02069v1.pdf)  
  Keywords: illumination, gaussian splatting, lighting, neural rendering, face, ar, relighting, reflection, dynamic, geometry, relightable  

### Few-shot

*Showing the latest 50 out of 73 papers*

- **[D$^2$GS: Depth-and-Density Guided Gaussian Splatting for Stable and
  Accurate Sparse-View Reconstruction](https://arxiv.org/abs/2510.08566v1)**  
  Authors: Meixi Song, Xin Lin, Dizhe Zhang, Haodong Li, Xiangtai Li, Bo Du, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08566v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insta360-research-team.github.io/DDGS-website/.)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, ar, sparse-view, sparse view  
- **[FSFSplatter: Build Surface and Novel Views with Sparse-Views within 3min](https://arxiv.org/abs/2510.02691v1)**  
  Authors: Yibin Zhao, Yihan Pan, Jun Nan, Jianjun Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02691v1.pdf)  
  Keywords: gaussian splatting, head, fast, face, ar, geometry, sparse-view  
- **[HART: Human Aligned Reconstruction Transformer](https://arxiv.org/abs/2509.26621v1)**  
  Authors: Xiyi Chen, Shaofei Wang, Marko Mihajlovic, Taewon Kang, Sergey Prokudin, Ming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.26621v1.pdf)  
  Keywords: body, ar, geometry, sparse-view, human  
- **[GaussianLens: Localized High-Resolution Reconstruction via On-Demand
  Gaussian Densification](https://arxiv.org/abs/2509.25603v1)**  
  Authors: Yijia Weng, Zhicheng Wang, Songyou Peng, Saining Xie, Howard Zhou, Leonidas J. Guibas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25603v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, fast, ar, human, sparse view  
- **[HBSplat: Robust Sparse-View Gaussian Reconstruction with Hybrid-Loss
  Guided Depth and Bidirectional Warping](https://arxiv.org/abs/2509.24893v3)**  
  Authors: Yu Ma, Guoliang Wei, Haihong Xiao, Yue Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24893v3.pdf)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, ar, sparse-view, 3d reconstruction, sparse view  
- **[OracleGS: Grounding Generative Priors for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2509.23258v2)**  
  Authors: Atakan Topaloglu, Kunyi Li, Michael Niemeyer, Nassir Navab, A. Murat Tekalp, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23258v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, nerf, sparse-view, sparse view  
- **[WaveletGaussian: Wavelet-domain Diffusion for Sparse-view 3D Gaussian
  Object Reconstruction](https://arxiv.org/abs/2509.19073v1)**  
  Authors: Hung Nguyen, Runfa Li, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19073v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, efficient, lightweight, ar, nerf, sparse-view  
- **[FixingGS: Enhancing 3D Gaussian Splatting via Training-Free Score
  Distillation](https://arxiv.org/abs/2509.18759v1)**  
  Authors: Zhaorui Wang, Yi Gu, Deming Zhou, Renjing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18759v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, sparse-view, 3d reconstruction, sparse view  
- **[SPFSplatV2: Efficient Self-Supervised Pose-Free 3D Gaussian Splatting
  from Sparse Views](https://arxiv.org/abs/2509.17246v1)**  
  Authors: Ranran Huang, Krystian Mikolajczyk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.17246v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ranrhuang.github.io/spfsplatv2/.)  
  Keywords: 3d gaussian, gaussian splatting, efficient, ar, sparse view  
- **[MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2509.15548v3)**  
  Authors: Deming Li, Kaiwen Jiang, Yutao Tang, Ravi Ramamoorthi, Rama Chellappa, Cheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.15548v3.pdf)  
  Keywords: 3d gaussian, gaussian splatting, motion, ar, semantic, nerf, geometry, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 320 papers*

- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: 3d gaussian, gaussian splatting, efficient, ray marching, ar, geometry  
- **[Efficient Label Refinement for Face Parsing Under Extreme Poses Using 3D
  Gaussian Splatting](https://arxiv.org/abs/2510.08096v1)**  
  Authors: Ankit Gahlawat, Anirban Mukherjee, Dinesh Babu Jayagopi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08096v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, head, efficient, face, ar, geometry, human  
- **[PrismGS: Physically-Grounded Anti-Aliasing for High-Fidelity Large-Scale
  3D Gaussian Splatting](https://arxiv.org/abs/2510.07830v1)**  
  Authors: Houqiang Zhong, Zhenglong Wu, Sihua Fu, Zihan Zheng, Xin Jin, Xiaoyun Zhang, Li Song, Qiang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07830v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, face, ar, compact, geometry  
- **[DEGS: Deformable Event-based 3D Gaussian Splatting from RGB and Event
  Stream](https://arxiv.org/abs/2510.07752v1)**  
  Authors: Junhao He, Jiaxu Wang, Jia Li, Mingyuan Sun, Qiang Zhang, Jiahang Cao, Ziyi Zhang, Yi Gu, Jingkai Sun, Renjing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07752v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, motion, ar, dynamic, geometry, deformation  
- **[Generating Surface for Text-to-3D using 2D Gaussian Splatting](https://arxiv.org/abs/2510.06967v1)**  
  Authors: Huanning Dong, Fan Li, Ping Kuang, Jianwen Min  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06967v1.pdf)  
  Keywords: high-fidelity, geometry, face, gaussian splatting  
- **[Capture and Interact: Rapid 3D Object Acquisition and Rendering with
  Gaussian Splatting in Unity](https://arxiv.org/abs/2510.06802v1)**  
  Authors: Islomjon Shukhratov, Sergey Gorinsky  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06802v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, real-time rendering, 3d reconstruction  
- **[Geometry Meets Vision: Revisiting Pretrained Semantics in Distilled
  Fields](https://arxiv.org/abs/2510.03104v1)**  
  Authors: Zhiting Mei, Ola Shorinwa, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03104v1.pdf)  
  Keywords: gaussian splatting, localization, ar, semantic, geometry  
- **[GS-Share: Enabling High-fidelity Map Sharing with Incremental Gaussian
  Splatting](https://arxiv.org/abs/2510.02884v1)**  
  Authors: Xinran Zhang, Hanqi Zhu, Yifan Duan, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02884v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, high-fidelity, ar, autonomous driving, compact, 3d reconstruction  
- **[FSFSplatter: Build Surface and Novel Views with Sparse-Views within 3min](https://arxiv.org/abs/2510.02691v1)**  
  Authors: Yibin Zhao, Yihan Pan, Jun Nan, Jianjun Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02691v1.pdf)  
  Keywords: gaussian splatting, head, fast, face, ar, geometry, sparse-view  
- **[Performance-Guided Refinement for Visual Aerial Navigation using
  Editable Gaussian Splatting in FalconGym 2.0](https://arxiv.org/abs/2510.02248v1)**  
  Authors: Yan Miao, Ege Yuceel, Georgios Fainekos, Bardh Hoxha, Hideki Okamoto, Sayan Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02248v1.pdf)  
  Keywords: geometry, dynamic, gaussian splatting, ar  

### Large Scene

*Showing the latest 50 out of 72 papers*

- **[LOBE-GS: Load-Balanced and Efficient 3D Gaussian Splatting for
  Large-Scale Scene Reconstruction](https://arxiv.org/abs/2510.01767v1)**  
  Authors: Sheng-Hsiang Hung, Ting-Yu Yen, Wei-Fang Sun, Simon See, Shih-Hsuan Hung, Hung-Kuo Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01767v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, high-fidelity, fast, efficient, lightweight, ar, outdoor  
- **[LVT: Large-Scale Scene Reconstruction via Local View Transformers](https://arxiv.org/abs/2509.25001v1)**  
  Authors: Tooba Imtiaz, Lucy Chai, Kathryn Heal, Xuan Luo, Jungyeon Park, Jennifer Dy, John Flynn  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25001v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://toobaimt.github.io/lvt/.)  
  Keywords: large scene, ar, 3d gaussian  
- **[Aerial-Ground Image Feature Matching via 3D Gaussian Splatting-based
  Intermediate View Rendering](https://arxiv.org/abs/2509.19898v1)**  
  Authors: Jiangxue Yu, Hui Wang, San Jiang, Xing Zhang, Dejin Zhang, Qingquan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19898v1.pdf)  
  Keywords: large scene, 3d gaussian, gaussian splatting, motion, ar  
- **[FGGS-LiDAR: Ultra-Fast, GPU-Accelerated Simulation from General 3DGS
  Models to LiDAR](https://arxiv.org/abs/2509.17390v1)**  
  Authors: Junzhe Wu, Yufei Jia, Yiyi Yan, Zhixing Chen, Tiao Tan, Zifan Wang, Guangyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.17390v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, fast, ar, autonomous driving, robotics, outdoor  
- **[ROSGS: Relightable Outdoor Scenes With Gaussian Splatting](https://arxiv.org/abs/2509.11275v1)**  
  Authors: Lianjun Liao, Chunhui Zhang, Tong Wu, Henglei Lv, Bailin Deng, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.11275v1.pdf)  
  Keywords: illumination, 3d gaussian, gaussian splatting, lighting, head, efficient, ar, relighting, nerf, geometry, compact, efficient rendering, outdoor, relightable  
- **[VIM-GS: Visual-Inertial Monocular Gaussian Splatting via Object-level
  Guidance in Large Scenes](https://arxiv.org/abs/2509.06685v3)**  
  Authors: Shengkai Zhang, Yuhe Liu, Guanjun Wu, Jianhua He, Xinggang Wang, Mozi Chen, Kezhong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06685v3.pdf)  
  Keywords: large scene, gaussian splatting, motion, ar, dynamic  
- **[3DOF+Quantization: 3DGS quantization for large scenes with limited
  Degrees of Freedom](https://arxiv.org/abs/2509.06400v1)**  
  Authors: Matthieu Gendrin, Stéphane Pateux, Théo Ladune  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06400v1.pdf)  
  Keywords: large scene, 3d gaussian, gaussian splatting, ar  
- **[GSVisLoc: Generalizable Visual Localization for Gaussian Splatting Scene
  Representations](https://arxiv.org/abs/2508.18242v1)**  
  Authors: Fadi Khatib, Dror Moran, Guy Trostianetsky, Yoni Kasten, Meirav Galun, Ronen Basri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18242v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, localization, ar, outdoor  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v2)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v2.pdf)  
  Keywords: lighting, 3d gaussian, gaussian splatting, face, ar, autonomous driving, relighting, geometry, outdoor, sparse view  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: illumination, lighting, 3d gaussian, gaussian splatting, ar, understanding, outdoor, 3d reconstruction  

### Model Compression

*Showing the latest 50 out of 414 papers*

- **[ReSplat: Learning Recurrent Gaussian Splats](https://arxiv.org/abs/2510.08575v1)**  
  Authors: Haofei Xu, Daniel Barath, Andreas Geiger, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08575v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haofeixu.github.io/resplat/.)  
  Keywords: 3d gaussian, gaussian splatting, head, efficient, ar, compact  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: 3d gaussian, gaussian splatting, efficient, ray marching, ar, geometry  
- **[Efficient Label Refinement for Face Parsing Under Extreme Poses Using 3D
  Gaussian Splatting](https://arxiv.org/abs/2510.08096v1)**  
  Authors: Ankit Gahlawat, Anirban Mukherjee, Dinesh Babu Jayagopi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08096v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, head, efficient, face, ar, geometry, human  
- **[PrismGS: Physically-Grounded Anti-Aliasing for High-Fidelity Large-Scale
  3D Gaussian Splatting](https://arxiv.org/abs/2510.07830v1)**  
  Authors: Houqiang Zhong, Zhenglong Wu, Sihua Fu, Zihan Zheng, Xin Jin, Xiaoyun Zhang, Li Song, Qiang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07830v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, face, ar, compact, geometry  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: gaussian splatting, lighting, light transport, efficient, face, ray tracing, real-time rendering, ar, shadow, relightable  
- **[Active Next-Best-View Optimization for Risk-Averse Path Planning](https://arxiv.org/abs/2510.06481v1)**  
  Authors: Amirhossein Mollaei Khass, Guangyi Liu, Vivek Pandey, Wen Jiang, Boshu Lei, Kostas Daniilidis, Nader Motee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06481v1.pdf)  
  Keywords: efficient, motion, 3d gaussian, ar  
- **[ArchitectHead: Continuous Level of Detail Control for 3D Gaussian Head
  Avatars](https://arxiv.org/abs/2510.05488v1)**  
  Authors: Peizhi Yan, Rabab Ward, Qiang Tang, Shan Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.05488v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, efficient, lightweight, ar, real-time rendering, dynamic, avatar  
- **[Optimized Minimal 4D Gaussian Splatting](https://arxiv.org/abs/2510.03857v1)**  
  Authors: Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee, Eunsoo Lee, Sangmin Kim, Seunghyeon Song, Joo Chan Lee, Jong Hwan Ko, Jaesik Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03857v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://minshirley.github.io/OMG4/.)  
  Keywords: compression, gaussian splatting, head, high-fidelity, face, motion, ar, real-time rendering, 4d, dynamic, compact  
- **[GS-Share: Enabling High-fidelity Map Sharing with Incremental Gaussian
  Splatting](https://arxiv.org/abs/2510.02884v1)**  
  Authors: Xinran Zhang, Hanqi Zhu, Yifan Duan, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02884v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, high-fidelity, ar, autonomous driving, compact, 3d reconstruction  
- **[SIMSplat: Predictive Driving Scene Editing with Language-aligned 4D
  Gaussian Splatting](https://arxiv.org/abs/2510.02469v1)**  
  Authors: Sung-Yeon Park, Adam Lee, Juanwu Lu, Can Cui, Luyang Jiang, Rohit Gupta, Kyungtae Han, Ahmadreza Moradipari, Ziran Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sungyeonparkk.github.io/simsplat/)  
  Keywords: gaussian splatting, efficient, motion, ar, 4d  

### Quality Enhancement

*Showing the latest 50 out of 170 papers*

- **[D$^2$GS: Depth-and-Density Guided Gaussian Splatting for Stable and
  Accurate Sparse-View Reconstruction](https://arxiv.org/abs/2510.08566v1)**  
  Authors: Meixi Song, Xin Lin, Dizhe Zhang, Haodong Li, Xiangtai Li, Bo Du, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08566v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insta360-research-team.github.io/DDGS-website/.)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, ar, sparse-view, sparse view  
- **[CVD-STORM: Cross-View Video Diffusion with Spatial-Temporal
  Reconstruction Model for Autonomous Driving](https://arxiv.org/abs/2510.07944v1)**  
  Authors: Tianrui Zhang, Yichen Liu, Zilin Guo, Yuxin Guo, Jingcheng Ni, Chenjing Ding, Dan Xu, Lewei Lu, Zehuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07944v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, ar, autonomous driving, 4d, dynamic, understanding  
- **[PrismGS: Physically-Grounded Anti-Aliasing for High-Fidelity Large-Scale
  3D Gaussian Splatting](https://arxiv.org/abs/2510.07830v1)**  
  Authors: Houqiang Zhong, Zhenglong Wu, Sihua Fu, Zihan Zheng, Xin Jin, Xiaoyun Zhang, Li Song, Qiang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07830v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, face, ar, compact, geometry  
- **[Generating Surface for Text-to-3D using 2D Gaussian Splatting](https://arxiv.org/abs/2510.06967v1)**  
  Authors: Huanning Dong, Fan Li, Ping Kuang, Jianwen Min  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06967v1.pdf)  
  Keywords: high-fidelity, geometry, face, gaussian splatting  
- **[Optimized Minimal 4D Gaussian Splatting](https://arxiv.org/abs/2510.03857v1)**  
  Authors: Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee, Eunsoo Lee, Sangmin Kim, Seunghyeon Song, Joo Chan Lee, Jong Hwan Ko, Jaesik Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03857v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://minshirley.github.io/OMG4/.)  
  Keywords: compression, gaussian splatting, head, high-fidelity, face, motion, ar, real-time rendering, 4d, dynamic, compact  
- **[GS-Share: Enabling High-fidelity Map Sharing with Incremental Gaussian
  Splatting](https://arxiv.org/abs/2510.02884v1)**  
  Authors: Xinran Zhang, Hanqi Zhu, Yifan Duan, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02884v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, high-fidelity, ar, autonomous driving, compact, 3d reconstruction  
- **[GaussianMorphing: Mesh-Guided 3D Gaussians for Semantic-Aware Object
  Morphing](https://arxiv.org/abs/2510.02034v1)**  
  Authors: Mengtian Li, Yunshu Bai, Yimin Chu, Yijun Shen, Zhongmei Li, Weifeng Ge, Zhifeng Xie, Chaofeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02034v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://baiyunshu.github.io/GAUSSIANMORPHING.github.io/)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, ar, semantic, geometry, deformation, mapping  
- **[ROI-GS: Interest-based Local Quality 3D Gaussian Splatting](https://arxiv.org/abs/2510.01978v1)**  
  Authors: Quoc-Anh Bui, Gilles Rougeron, Géraldine Morin, Simone Gasparini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01978v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, fast, efficient, ar  
- **[LOBE-GS: Load-Balanced and Efficient 3D Gaussian Splatting for
  Large-Scale Scene Reconstruction](https://arxiv.org/abs/2510.01767v1)**  
  Authors: Sheng-Hsiang Hung, Ting-Yu Yen, Wei-Fang Sun, Simon See, Shih-Hsuan Hung, Hung-Kuo Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01767v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, high-fidelity, fast, efficient, lightweight, ar, outdoor  
- **[MPMAvatar: Learning 3D Gaussian Avatars with Accurate and Robust
  Physics-Based Dynamics](https://arxiv.org/abs/2510.01619v1)**  
  Authors: Changmin Lee, Jihyun Lee, Tae-Kyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://KAISTChangmin.github.io/MPMAvatar/)  
  Keywords: 3d gaussian, gaussian splatting, animation, high-fidelity, body, ar, human, dynamic, deformation, avatar, shadow  

### Ray Tracing

- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: 3d gaussian, gaussian splatting, efficient, ray marching, ar, geometry  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: gaussian splatting, lighting, light transport, efficient, face, ray tracing, real-time rendering, ar, shadow, relightable  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted
  Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: illumination, gaussian splatting, lighting, light transport, efficient, ar, relighting, reflection, geometry, global illumination  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing
  for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v1)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v1.pdf)  
  Keywords: gaussian splatting, fast, ar, ray tracing, 4d, dynamic  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: illumination, 3d gaussian, gaussian splatting, lighting, high-fidelity, face, ar, ray tracing, relighting, reflection, nerf, geometry  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: illumination, 3d gaussian, gaussian splatting, lighting, face, ar, relighting, dynamic, global illumination, shadow, outdoor, relightable  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: path tracing, 3d gaussian, gaussian splatting, lighting, face, ar, dynamic  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, lighting, efficient, ray marching, face, ar, relighting, geometry, efficient rendering, relightable  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, efficient, ar, ray tracing, real-time rendering  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v2)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v2.pdf)  
  Keywords: gaussian splatting, lighting, fast, ar, ray tracing, relighting, human, geometry, avatar, shadow, relightable  

### Relighting

*Showing the latest 50 out of 117 papers*

- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: gaussian splatting, lighting, light transport, efficient, face, ray tracing, real-time rendering, ar, shadow, relightable  
- **[Spec-Gloss Surfels and Normal-Diffuse Priors for Relightable Glossy
  Objects](https://arxiv.org/abs/2510.02069v1)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02069v1.pdf)  
  Keywords: illumination, gaussian splatting, lighting, neural rendering, face, ar, relighting, reflection, dynamic, geometry, relightable  
- **[MPMAvatar: Learning 3D Gaussian Avatars with Accurate and Robust
  Physics-Based Dynamics](https://arxiv.org/abs/2510.01619v1)**  
  Authors: Changmin Lee, Jihyun Lee, Tae-Kyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://KAISTChangmin.github.io/MPMAvatar/)  
  Keywords: 3d gaussian, gaussian splatting, animation, high-fidelity, body, ar, human, dynamic, deformation, avatar, shadow  
- **[Universal Beta Splatting](https://arxiv.org/abs/2510.03312v1)**  
  Authors: Rong Liu, Zhongpai Gao, Benjamin Planche, Meida Chen, Van Nguyen Nguyen, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Yue Wang, Andrew Feng, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03312v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rongliu-leo.github.io/universal-beta-splatting/.)  
  Keywords: 3d gaussian, gaussian splatting, light transport, face, ar, real-time rendering, dynamic  
- **[Large Material Gaussian Model for Relightable 3D Generation](https://arxiv.org/abs/2509.22112v1)**  
  Authors: Jingrui Ye, Lingting Zhu, Runze Zhang, Zeyu Hu, Yingda Yin, Lanjiong Li, Lequan Yu, Qingmin Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22112v1.pdf)  
  Keywords: lighting, 3d gaussian, gaussian splatting, efficient, ar, relighting, dynamic, relightable  
- **[Dynamic Novel View Synthesis in High Dynamic Range](https://arxiv.org/abs/2509.21853v2)**  
  Authors: Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.21853v2.pdf)  
  Keywords: lighting, gaussian splatting, ar, 4d, dynamic, mapping  
- **[Seeing Through Reflections: Advancing 3D Scene Reconstruction in
  Mirror-Containing Environments with Gaussian Splatting](https://arxiv.org/abs/2509.18956v1)**  
  Authors: Zijing Guo, Yunyang Zhao, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18956v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, face, ar, reflection, mapping, nerf, geometry, 3d reconstruction  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted
  Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: illumination, gaussian splatting, lighting, light transport, efficient, ar, relighting, reflection, geometry, global illumination  
- **[From Restoration to Reconstruction: Rethinking 3D Gaussian Splatting for
  Underwater Scenes](https://arxiv.org/abs/2509.17789v1)**  
  Authors: Guoxi Huang, Haoran Wang, Zipeng Qi, Wenjun Lu, David Bull, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.17789v1.pdf)  
  Keywords: illumination, 3d gaussian, gaussian splatting, lightweight, ar, nerf, 3d reconstruction  
- **[RadarGaussianDet3D: An Efficient and Effective Gaussian-based 3D
  Detector with 4D Automotive Radars](https://arxiv.org/abs/2509.16119v1)**  
  Authors: Weiyi Xiong, Bing Zhu, Tao Huang, Zewei Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.16119v1.pdf)  
  Keywords: lighting, 3d gaussian, gaussian splatting, fast, efficient, ar, autonomous driving, 4d  

### SLAM

*Showing the latest 50 out of 153 papers*

- **[SCas4D: Structural Cascaded Optimization for Boosting Persistent 4D
  Novel View Synthesis](https://arxiv.org/abs/2510.06694v1)**  
  Authors: Jipeng Lyu, Jiahua Dong, Yu-Xiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06694v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, ar, 4d, dynamic, deformation, tracking  
- **[RTGS: Real-Time 3D Gaussian Splatting SLAM via Multi-Level Redundancy
  Reduction](https://arxiv.org/abs/2510.06644v2)**  
  Authors: Leshu Li, Jiayin Qin, Jie Peng, Zishen Wan, Huaizhi Qu, Ye Han, Pingqing Zheng, Hongsen Zhang, Yu Cao, Tianlong Chen, Yang Katie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06644v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, head, localization, ar, slam, dynamic, acceleration, mapping  
- **[Geometry Meets Vision: Revisiting Pretrained Semantics in Distilled
  Fields](https://arxiv.org/abs/2510.03104v1)**  
  Authors: Zhiting Mei, Ola Shorinwa, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03104v1.pdf)  
  Keywords: gaussian splatting, localization, ar, semantic, geometry  
- **[GaussianMorphing: Mesh-Guided 3D Gaussians for Semantic-Aware Object
  Morphing](https://arxiv.org/abs/2510.02034v1)**  
  Authors: Mengtian Li, Yunshu Bai, Yimin Chu, Yijun Shen, Zhongmei Li, Weifeng Ge, Zhifeng Xie, Chaofeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02034v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://baiyunshu.github.io/GAUSSIANMORPHING.github.io/)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, ar, semantic, geometry, deformation, mapping  
- **[GreenhouseSplat: A Dataset of Photorealistic Greenhouse Simulations for
  Mobile Robotics](https://arxiv.org/abs/2510.01848v1)**  
  Authors: Diram Tabaa, Gianni Di Caro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01848v1.pdf)  
  Keywords: localization, robotics, gaussian splatting, ar  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, neural rendering, fast, efficient, ar, slam, nerf, understanding  
- **[Learning Unified Representation of 3D Gaussian Splatting](https://arxiv.org/abs/2509.22917v1)**  
  Authors: Yuelin Xin, Yuheng Liu, Xiaohui Xie, Xinke Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22917v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, efficient, ar, mapping, 3d reconstruction  
- **[Dynamic Novel View Synthesis in High Dynamic Range](https://arxiv.org/abs/2509.21853v2)**  
  Authors: Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.21853v2.pdf)  
  Keywords: lighting, gaussian splatting, ar, 4d, dynamic, mapping  
- **[Seeing Through Reflections: Advancing 3D Scene Reconstruction in
  Mirror-Containing Environments with Gaussian Splatting](https://arxiv.org/abs/2509.18956v1)**  
  Authors: Zijing Guo, Yunyang Zhao, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18956v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, face, ar, reflection, mapping, nerf, geometry, 3d reconstruction  
- **[ConfidentSplat: Confidence-Weighted Depth Fusion for Accurate 3D
  Gaussian Splatting SLAM](https://arxiv.org/abs/2509.16863v1)**  
  Authors: Amanuel T. Dufera, Yuan-Li Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.16863v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, efficient, ar, slam, dynamic, geometry  

### Scene Understanding

*Showing the latest 50 out of 197 papers*

- **[Efficient Label Refinement for Face Parsing Under Extreme Poses Using 3D
  Gaussian Splatting](https://arxiv.org/abs/2510.08096v1)**  
  Authors: Ankit Gahlawat, Anirban Mukherjee, Dinesh Babu Jayagopi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08096v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, head, efficient, face, ar, geometry, human  
- **[CVD-STORM: Cross-View Video Diffusion with Spatial-Temporal
  Reconstruction Model for Autonomous Driving](https://arxiv.org/abs/2510.07944v1)**  
  Authors: Tianrui Zhang, Yichen Liu, Zilin Guo, Yuxin Guo, Jingcheng Ni, Chenjing Ding, Dan Xu, Lewei Lu, Zehuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07944v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, ar, autonomous driving, 4d, dynamic, understanding  
- **[SCas4D: Structural Cascaded Optimization for Boosting Persistent 4D
  Novel View Synthesis](https://arxiv.org/abs/2510.06694v1)**  
  Authors: Jipeng Lyu, Jiahua Dong, Yu-Xiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06694v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, ar, 4d, dynamic, deformation, tracking  
- **[Geometry Meets Vision: Revisiting Pretrained Semantics in Distilled
  Fields](https://arxiv.org/abs/2510.03104v1)**  
  Authors: Zhiting Mei, Ola Shorinwa, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03104v1.pdf)  
  Keywords: gaussian splatting, localization, ar, semantic, geometry  
- **[GaussianMorphing: Mesh-Guided 3D Gaussians for Semantic-Aware Object
  Morphing](https://arxiv.org/abs/2510.02034v1)**  
  Authors: Mengtian Li, Yunshu Bai, Yimin Chu, Yijun Shen, Zhongmei Li, Weifeng Ge, Zhifeng Xie, Chaofeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02034v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://baiyunshu.github.io/GAUSSIANMORPHING.github.io/)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, ar, semantic, geometry, deformation, mapping  
- **[4DGS-Craft: Consistent and Interactive 4D Gaussian Splatting Editing](https://arxiv.org/abs/2510.01991v1)**  
  Authors: Lei Liu, Can Wang, Zhenghao Chen, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01991v1.pdf)  
  Keywords: gaussian splatting, face, ar, 4d, geometry, understanding  
- **[CrashSplat: 2D to 3D Vehicle Damage Segmentation in Gaussian Splatting](https://arxiv.org/abs/2509.23947v1)**  
  Authors: Dragoş-Andrei Chileban, Andrei-Ştefan Bulzan, Cosmin Cernǎzanu-Glǎvan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23947v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, fast, motion, ar, 3d reconstruction  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, neural rendering, fast, efficient, ar, slam, nerf, understanding  
- **[Vision-Language Alignment from Compressed Image Representations using 2D
  Gaussian Splatting](https://arxiv.org/abs/2509.22615v1)**  
  Authors: Yasmine Omri, Connor Ding, Tsachy Weissman, Thierry Tambe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22615v1.pdf)  
  Keywords: gaussian splatting, fast, efficient, lightweight, ar, semantic, compact  
- **[Polysemous Language Gaussian Splatting via Matching-based Mask Lifting](https://arxiv.org/abs/2509.22225v1)**  
  Authors: Jiayu Ding, Xinpeng Liu, Zhiyi Pan, Shiqiang Long, Ge Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22225v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, ar, semantic, understanding  



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