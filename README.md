# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-08-05 01:00:52

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

- [3DGS Surveys](#3dgs-surveys) (4 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (47 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (212 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (68 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (98 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (12 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (72 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (18 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (83 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (42 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (4 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (31 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (44 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (53 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: robotics, geometry, ar, survey, 3d reconstruction, motion, vr, 3d gaussian, nerf, sparse-view, gaussian splatting  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v2)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v2.pdf)  
  Keywords: lighting, robotics, human, ar, survey, 3d reconstruction, vr, 3d gaussian, dynamic, nerf, fast, slam, gaussian splatting  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: face, ar, survey, autonomous driving, outdoor, 3d gaussian, dynamic, nerf, gaussian splatting, efficient, high-fidelity  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: robotics, ar, survey, 3d reconstruction, autonomous driving, vr, 3d gaussian, nerf, neural rendering, gaussian splatting, high-fidelity  

### Acceleration

- **[Enhanced Velocity Field Modeling for Gaussian Video Reconstruction](https://arxiv.org/abs/2507.23704v1)**  
  Authors: Zhenyang Li, Xiaoyang Bai, Tongchen Zhang, Pengfei Shen, Weiwei Xu, Yifan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23704v1.pdf)  
  Keywords: real-time rendering, ar, motion, vr, 3d gaussian, dynamic, deformation, gaussian splatting, high-fidelity  
- **[Stereo 3D Gaussian Splatting SLAM for Outdoor Urban Scenes](https://arxiv.org/abs/2507.23677v1)**  
  Authors: Xiaohan Li, Ziren Gong, Fabio Tosi, Matteo Poggi, Stefano Mattoccia, Dong Liu, Jun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23677v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, mapping, fast, slam, gaussian splatting, urban scene, tracking, high-fidelity  
- **[iLRM: An Iterative Large 3D Reconstruction Model](https://arxiv.org/abs/2507.23277v1)**  
  Authors: Gyeongjin Kang, Seungtae Nam, Xiangyu Sun, Sameh Khamis, Abdelrahman Mohamed, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23277v1.pdf)  
  Keywords: ar, 3d reconstruction, compact, 3d gaussian, fast, gaussian splatting, efficient, high-fidelity  
- **[No Redundancy, No Stall: Lightweight Streaming 3D Gaussian Splatting for
  Real-time Rendering](https://arxiv.org/abs/2507.21572v2)**  
  Authors: Linye Wei, Jiajun Tang, Fan Fei, Boxin Shi, Runsheng Wang, Meng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.21572v2.pdf)  
  Keywords: lightweight, face, real-time rendering, ar, autonomous driving, 3d gaussian, mapping, gaussian splatting, efficient  
- **[Automated 3D-GS Registration and Fusion via Skeleton Alignment and
  Gaussian-Adaptive Features](https://arxiv.org/abs/2507.20480v1)**  
  Authors: Shiyang Liu, Dianyi Yang, Yu Gao, Bohan Ren, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20480v1.pdf)  
  Keywords: lighting, real-time rendering, ar, 3d gaussian, gaussian splatting  
- **[Decomposing Densification in Gaussian Splatting for Faster 3D Scene
  Reconstruction](https://arxiv.org/abs/2507.20239v1)**  
  Authors: Binxiao Huang, Zhengwu Liu, Ngai Wong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20239v1.pdf)  
  Keywords: ar, 3d gaussian, dynamic, nerf, fast, gaussian splatting, efficient  
- **[Fast Learning of Non-Cooperative Spacecraft 3D Models through Primitive
  Initialization](https://arxiv.org/abs/2507.19459v1)**  
  Authors: Pol Francesch Huc, Emily Bates, Simone D'Amico  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19459v1.pdf)  
  Keywords: ar, 3d gaussian, nerf, fast, gaussian splatting, high-fidelity  
- **[3DGauCIM: Accelerating Static/Dynamic 3D Gaussian Splatting via Digital
  CIM for High Frame Rate Real-Time Edge Rendering](https://arxiv.org/abs/2507.19133v1)**  
  Authors: Wei-Hsing Huang, Cheng-Jhih Shih, Jian-Wei Su, Samuel Wade Wang, Vaidehi Garg, Yuyao Kong, Jen-Chun Tien, Nealson Li, Arijit Raychowdhury, Meng-Fan Chang, Yingyan, Lin, Shimeng Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19133v1.pdf)  
  Keywords: head, real-time rendering, ar, vr, 3d gaussian, dynamic, gaussian splatting, face  
- **[SaLF: Sparse Local Fields for Multi-Sensor Rendering in Real-Time](https://arxiv.org/abs/2507.18713v1)**  
  Authors: Yun Chen, Matthew Haines, Jingkang Wang, Krzysztof Baron-Lis, Sivabalan Manivasagam, Ze Yang, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18713v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://waabi.ai/salf/)  
  Keywords: ar, large scene, 3d gaussian, nerf, fast, gaussian splatting, high-fidelity  
- **[StreamME: Simplify 3D Gaussian Avatar within Live Stream](https://arxiv.org/abs/2507.17029v1)**  
  Authors: Luchuan Song, Yang Zhou, Zhan Xu, Yi Zhou, Deepali Aneja, Chenliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.17029v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://songluchuan.github.io/StreamME/.)  
  Keywords: lighting, head, geometry, ar, vr, 3d gaussian, fast, avatar, animation, gaussian splatting, relighting, face  

### Applications

*Showing the latest 50 out of 212 papers*

- **[Omni-Scan: Creating Visually-Accurate Digital Twin Object Models Using a
  Bimanual Robot with Handover and Gaussian Splat Merging](https://arxiv.org/abs/2508.00354v1)**  
  Authors: Tianshuang Qiu, Zehan Ma, Karim El-Refai, Hiya Shah, Chung Min Kim, Justin Kerr, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.00354v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://berkeleyautomation.github.io/omni-scan/)  
  Keywords: ar, face, 3d gaussian  
- **[PointGauss: Point Cloud-Guided Multi-Object Segmentation for Gaussian
  Splatting](https://arxiv.org/abs/2508.00259v1)**  
  Authors: Wentao Sun, Hanqing Xu, Quanyun Wu, Dedong Zhang, Yiping Chen, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.00259v1.pdf)  
  Keywords: segmentation, efficient, ar, gaussian splatting  
- **[Gaussian Variation Field Diffusion for High-fidelity Video-to-4D
  Synthesis](https://arxiv.org/abs/2507.23785v1)**  
  Authors: Bowen Zhang, Sicheng Xu, Chuxin Wang, Jiaolong Yang, Feng Zhao, Dong Chen, Baining Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23785v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gvfdiffusion.github.io/.)  
  Keywords: 4d, ar, motion, compact, dynamic, animation, efficient, high-fidelity  
- **[SeqAffordSplat: Scene-level Sequential Affordance Reasoning on 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.23772v1)**  
  Authors: Di Li, Jie Feng, Jiahao Chen, Weisheng Dong, Guanbin Li, Yuhui Zheng, Mingtao Feng, Guangming Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23772v1.pdf)  
  Keywords: geometry, human, ar, understanding, 3d gaussian, semantic, segmentation, gaussian splatting  
- **[Enhanced Velocity Field Modeling for Gaussian Video Reconstruction](https://arxiv.org/abs/2507.23704v1)**  
  Authors: Zhenyang Li, Xiaoyang Bai, Tongchen Zhang, Pengfei Shen, Weiwei Xu, Yifan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23704v1.pdf)  
  Keywords: real-time rendering, ar, motion, vr, 3d gaussian, dynamic, deformation, gaussian splatting, high-fidelity  
- **[I2V-GS: Infrastructure-to-Vehicle View Transformation with Gaussian
  Splatting for Autonomous Driving Data Generation](https://arxiv.org/abs/2507.23683v1)**  
  Authors: Jialei Chen, Wuhao Xu, Sipeng He, Baoru Huang, Dongchun Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23683v1.pdf)  
  Keywords: lighting, ar, 3d reconstruction, autonomous driving, gaussian splatting, efficient  
- **[Stereo 3D Gaussian Splatting SLAM for Outdoor Urban Scenes](https://arxiv.org/abs/2507.23677v1)**  
  Authors: Xiaohan Li, Ziren Gong, Fabio Tosi, Matteo Poggi, Stefano Mattoccia, Dong Liu, Jun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23677v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, mapping, fast, slam, gaussian splatting, urban scene, tracking, high-fidelity  
- **[Gaussian Splatting Feature Fields for Privacy-Preserving Visual
  Localization](https://arxiv.org/abs/2507.23569v1)**  
  Authors: Maxime Pietrantoni, Gabriela Csurka, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23569v1.pdf)  
  Keywords: localization, geometry, ar, 3d gaussian, gaussian splatting, segmentation  
- **[NeRF Is a Valuable Assistant for 3D Gaussian Splatting](https://arxiv.org/abs/2507.23374v1)**  
  Authors: Shuangkang Fang, I-Chao Shen, Takeo Igarashi, Yufeng Wang, ZeSheng Wang, Yi Yang, Wenrui Ding, Shuchang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23374v1.pdf)  
  Keywords: ar, 3d gaussian, nerf, gaussian splatting, efficient  
- **[MagicRoad: Semantic-Aware 3D Road Surface Reconstruction via Obstacle
  Inpainting](https://arxiv.org/abs/2507.23340v1)**  
  Authors: Xingyue Peng, Yuandong Lyu, Lang Zhang, Jian Zhu, Songtao Wang, Jiaxin Deng, Songxin Lu, Weiliang Ma, Dangen She, Peng Jia, XianPeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23340v1.pdf)  
  Keywords: lighting, segmentation, face, ar, autonomous driving, 3d gaussian, dynamic, mapping, semantic, gaussian splatting, efficient  

### Avatar Generation

*Showing the latest 50 out of 68 papers*

- **[Omni-Scan: Creating Visually-Accurate Digital Twin Object Models Using a
  Bimanual Robot with Handover and Gaussian Splat Merging](https://arxiv.org/abs/2508.00354v1)**  
  Authors: Tianshuang Qiu, Zehan Ma, Karim El-Refai, Hiya Shah, Chung Min Kim, Justin Kerr, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.00354v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://berkeleyautomation.github.io/omni-scan/)  
  Keywords: ar, face, 3d gaussian  
- **[SeqAffordSplat: Scene-level Sequential Affordance Reasoning on 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.23772v1)**  
  Authors: Di Li, Jie Feng, Jiahao Chen, Weisheng Dong, Guanbin Li, Yuhui Zheng, Mingtao Feng, Guangming Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23772v1.pdf)  
  Keywords: geometry, human, ar, understanding, 3d gaussian, semantic, segmentation, gaussian splatting  
- **[MagicRoad: Semantic-Aware 3D Road Surface Reconstruction via Obstacle
  Inpainting](https://arxiv.org/abs/2507.23340v1)**  
  Authors: Xingyue Peng, Yuandong Lyu, Lang Zhang, Jian Zhu, Songtao Wang, Jiaxin Deng, Songxin Lu, Weiliang Ma, Dangen She, Peng Jia, XianPeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23340v1.pdf)  
  Keywords: lighting, segmentation, face, ar, autonomous driving, 3d gaussian, dynamic, mapping, semantic, gaussian splatting, efficient  
- **[No Redundancy, No Stall: Lightweight Streaming 3D Gaussian Splatting for
  Real-time Rendering](https://arxiv.org/abs/2507.21572v2)**  
  Authors: Linye Wei, Jiajun Tang, Fan Fei, Boxin Shi, Runsheng Wang, Meng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.21572v2.pdf)  
  Keywords: lightweight, face, real-time rendering, ar, autonomous driving, 3d gaussian, mapping, gaussian splatting, efficient  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: lighting, global illumination, relightable, ar, shadow, outdoor, 3d gaussian, dynamic, gaussian splatting, relighting, face, illumination  
- **[Neural Shell Texture Splatting: More Details and Fewer Primitives](https://arxiv.org/abs/2507.20200v1)**  
  Authors: Xin Zhang, Anpei Chen, Jincheng Xiong, Pinxuan Dai, Yujun Shen, Weiwei Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20200v1.pdf)  
  Keywords: face, geometry, ar, gaussian splatting, efficient  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: lighting, face, ar, 3d gaussian, dynamic, gaussian splatting, path tracing  
- **[3DGauCIM: Accelerating Static/Dynamic 3D Gaussian Splatting via Digital
  CIM for High Frame Rate Real-Time Edge Rendering](https://arxiv.org/abs/2507.19133v1)**  
  Authors: Wei-Hsing Huang, Cheng-Jhih Shih, Jian-Wei Su, Samuel Wade Wang, Vaidehi Garg, Yuyao Kong, Jen-Chun Tien, Nealson Li, Arijit Raychowdhury, Meng-Fan Chang, Yingyan, Lin, Shimeng Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19133v1.pdf)  
  Keywords: head, real-time rendering, ar, vr, 3d gaussian, dynamic, gaussian splatting, face  
- **[Gaussian Set Surface Reconstruction through Per-Gaussian Optimization](https://arxiv.org/abs/2507.18923v1)**  
  Authors: Zhentao Huang, Di Wu, Zhenbang He, Minglun Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18923v1.pdf)  
  Keywords: face, geometry, ar, 3d gaussian, gaussian splatting, efficient  
- **[G2S-ICP SLAM: Geometry-aware Gaussian Splatting ICP SLAM](https://arxiv.org/abs/2507.18344v1)**  
  Authors: Gyuhyeon Pak, Hae Min Cho, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18344v1.pdf)  
  Keywords: localization, geometry, ar, 3d reconstruction, slam, gaussian splatting, face, tracking, high-fidelity  

### Dynamic Scene

*Showing the latest 50 out of 98 papers*

- **[Gaussian Variation Field Diffusion for High-fidelity Video-to-4D
  Synthesis](https://arxiv.org/abs/2507.23785v1)**  
  Authors: Bowen Zhang, Sicheng Xu, Chuxin Wang, Jiaolong Yang, Feng Zhao, Dong Chen, Baining Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23785v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gvfdiffusion.github.io/.)  
  Keywords: 4d, ar, motion, compact, dynamic, animation, efficient, high-fidelity  
- **[Enhanced Velocity Field Modeling for Gaussian Video Reconstruction](https://arxiv.org/abs/2507.23704v1)**  
  Authors: Zhenyang Li, Xiaoyang Bai, Tongchen Zhang, Pengfei Shen, Weiwei Xu, Yifan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23704v1.pdf)  
  Keywords: real-time rendering, ar, motion, vr, 3d gaussian, dynamic, deformation, gaussian splatting, high-fidelity  
- **[MagicRoad: Semantic-Aware 3D Road Surface Reconstruction via Obstacle
  Inpainting](https://arxiv.org/abs/2507.23340v1)**  
  Authors: Xingyue Peng, Yuandong Lyu, Lang Zhang, Jian Zhu, Songtao Wang, Jiaxin Deng, Songxin Lu, Weiliang Ma, Dangen She, Peng Jia, XianPeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23340v1.pdf)  
  Keywords: lighting, segmentation, face, ar, autonomous driving, 3d gaussian, dynamic, mapping, semantic, gaussian splatting, efficient  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: lighting, global illumination, relightable, ar, shadow, outdoor, 3d gaussian, dynamic, gaussian splatting, relighting, face, illumination  
- **[From Gallery to Wrist: Realistic 3D Bracelet Insertion in Videos](https://arxiv.org/abs/2507.20331v2)**  
  Authors: Chenjian Gao, Lihe Ding, Rui Han, Zhanpeng Huang, Zibin Wang, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20331v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cjeen.github.io/BraceletPaper/)  
  Keywords: lighting, ar, motion, 3d gaussian, dynamic, gaussian splatting, illumination  
- **[Decomposing Densification in Gaussian Splatting for Faster 3D Scene
  Reconstruction](https://arxiv.org/abs/2507.20239v1)**  
  Authors: Binxiao Huang, Zhengwu Liu, Ngai Wong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20239v1.pdf)  
  Keywords: ar, 3d gaussian, dynamic, nerf, fast, gaussian splatting, efficient  
- **[RaGS: Unleashing 3D Gaussian Splatting from 4D Radar and Monocular Cues
  for 3D Object Detection](https://arxiv.org/abs/2507.19856v2)**  
  Authors: Xiaokai Bai, Chenxu Zhou, Lianqing Zheng, Si-Yuan Cao, Jianan Liu, Xiaohan Zhang, Zhengzhuang Zhang, Hui-liang Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19856v2.pdf)  
  Keywords: localization, geometry, 4d, ar, understanding, autonomous driving, 3d gaussian, dynamic, semantic, gaussian splatting, efficient  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: lighting, face, ar, 3d gaussian, dynamic, gaussian splatting, path tracing  
- **[DASH: 4D Hash Encoding with Self-Supervised Decomposition for Real-Time
  Dynamic Scene Rendering](https://arxiv.org/abs/2507.19141v2)**  
  Authors: Jie Chen, Zhangchi Hu, Peixi Wu, Huyue Zhu, Hebei Li, Xiaoyan Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19141v2.pdf)  
  Keywords: 4d, ar, dynamic, deformation, gaussian splatting  
- **[3DGauCIM: Accelerating Static/Dynamic 3D Gaussian Splatting via Digital
  CIM for High Frame Rate Real-Time Edge Rendering](https://arxiv.org/abs/2507.19133v1)**  
  Authors: Wei-Hsing Huang, Cheng-Jhih Shih, Jian-Wei Su, Samuel Wade Wang, Vaidehi Garg, Yuyao Kong, Jen-Chun Tien, Nealson Li, Arijit Raychowdhury, Meng-Fan Chang, Yingyan, Lin, Shimeng Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19133v1.pdf)  
  Keywords: head, real-time rendering, ar, vr, 3d gaussian, dynamic, gaussian splatting, face  

### Few-shot

- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: robotics, geometry, ar, survey, 3d reconstruction, motion, vr, 3d gaussian, nerf, sparse-view, gaussian splatting  
- **[DWTGS: Rethinking Frequency Regularization for Sparse-view 3D Gaussian
  Splatting](https://arxiv.org/abs/2507.15690v1)**  
  Authors: Hung Nguyen, Runfa Li, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15690v1.pdf)  
  Keywords: 3d gaussian, ar, sparse-view, gaussian splatting  
- **[SurfaceSplat: Connecting Surface Reconstruction and Gaussian Splatting](https://arxiv.org/abs/2507.15602v2)**  
  Authors: Zihui Gao, Jia-Wang Bian, Guosheng Lin, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15602v2.pdf)  
  Keywords: geometry, ar, 3d gaussian, sparse-view, gaussian splatting, face  
- **[DCHM: Depth-Consistent Human Modeling for Multiview Detection](https://arxiv.org/abs/2507.14505v1)**  
  Authors: Jiahao Ma, Tianyu Wang, Miaomiao Liu, David Ahmedt-Aristizabal, Chuong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14505v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiahao-ma.github.io/DCHM/}{project)  
  Keywords: localization, human, ar, sparse-view, gaussian splatting, segmentation  
- **[BRUM: Robust 3D Vehicle Reconstruction from 360 Sparse Images](https://arxiv.org/abs/2507.12095v1)**  
  Authors: Davide Di Nucci, Matteo Tomei, Guido Borghi, Luca Ciuffreda, Roberto Vezzani, Rita Cucchiara  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.12095v1.pdf)  
  Keywords: ar, motion, 3d reconstruction, sparse-view, gaussian splatting  
- **[TRAN-D: 2D Gaussian Splatting-based Sparse-view Transparent Object Depth
  Reconstruction via Physics Simulation for Scene Update](https://arxiv.org/abs/2507.11069v2)**  
  Authors: Jeongyun Kim, Seunghoon Jeong, Giseop Kim, Myung-Hwan Jeon, Eunji Jun, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.11069v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jeongyun0609.github.io/TRAN-D/.)  
  Keywords: reflection, geometry, ar, sparse view, understanding, dynamic, sparse-view, gaussian splatting, face  
- **[Learning human-to-robot handovers through 3D scene reconstruction](https://arxiv.org/abs/2507.08726v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08726v1.pdf)  
  Keywords: human, ar, sparse-view, gaussian splatting  
- **[RegGS: Unposed Sparse Views Gaussian Splatting with 3DGS Registration](https://arxiv.org/abs/2507.08136v2)**  
  Authors: Chong Cheng, Yu Hu, Sicheng Yu, Beizhen Zhao, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.08136v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/reggs/.)  
  Keywords: geometry, ar, sparse view, 3d gaussian, gaussian splatting, efficient  
- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from
  RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: ar, motion, dynamic, sparse-view, gaussian splatting  
- **[PointGS: Point Attention-Aware Sparse View Synthesis with Gaussian
  Splatting](https://arxiv.org/abs/2506.10335v1)**  
  Authors: Lintao Xiang, Hongpei Zheng, Yating Huang, Qijun Yang, Hujun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.10335v1.pdf)  
  Keywords: few-shot, lightweight, ar, sparse view, 3d gaussian, nerf, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 72 papers*

- **[SeqAffordSplat: Scene-level Sequential Affordance Reasoning on 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.23772v1)**  
  Authors: Di Li, Jie Feng, Jiahao Chen, Weisheng Dong, Guanbin Li, Yuhui Zheng, Mingtao Feng, Guangming Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23772v1.pdf)  
  Keywords: geometry, human, ar, understanding, 3d gaussian, semantic, segmentation, gaussian splatting  
- **[I2V-GS: Infrastructure-to-Vehicle View Transformation with Gaussian
  Splatting for Autonomous Driving Data Generation](https://arxiv.org/abs/2507.23683v1)**  
  Authors: Jialei Chen, Wuhao Xu, Sipeng He, Baoru Huang, Dongchun Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23683v1.pdf)  
  Keywords: lighting, ar, 3d reconstruction, autonomous driving, gaussian splatting, efficient  
- **[Gaussian Splatting Feature Fields for Privacy-Preserving Visual
  Localization](https://arxiv.org/abs/2507.23569v1)**  
  Authors: Maxime Pietrantoni, Gabriela Csurka, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23569v1.pdf)  
  Keywords: localization, geometry, ar, 3d gaussian, gaussian splatting, segmentation  
- **[iLRM: An Iterative Large 3D Reconstruction Model](https://arxiv.org/abs/2507.23277v1)**  
  Authors: Gyeongjin Kang, Seungtae Nam, Xiangyu Sun, Sameh Khamis, Abdelrahman Mohamed, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23277v1.pdf)  
  Keywords: ar, 3d reconstruction, compact, 3d gaussian, fast, gaussian splatting, efficient, high-fidelity  
- **[DISCOVERSE: Efficient Robot Simulation in Complex High-Fidelity
  Environments](https://arxiv.org/abs/2507.21981v1)**  
  Authors: Yufei Jia, Guangyu Wang, Yuhang Dong, Junzhe Wu, Yupei Zeng, Haonan Lin, Zifan Wang, Haizhou Ge, Weibin Gu, Kairui Ding, Zike Yan, Yunjie Cheng, Yue Li, Ziming Wang, Chuxuan Li, Wei Sui, Lu Shi, Guanzhong Tian, Ruqi Huang, Guyue Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.21981v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://air-discoverse.github.io/.)  
  Keywords: geometry, ar, gaussian splatting, efficient, high-fidelity  
- **[Neural Shell Texture Splatting: More Details and Fewer Primitives](https://arxiv.org/abs/2507.20200v1)**  
  Authors: Xin Zhang, Anpei Chen, Jincheng Xiong, Pinxuan Dai, Yujun Shen, Weiwei Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20200v1.pdf)  
  Keywords: face, geometry, ar, gaussian splatting, efficient  
- **[RaGS: Unleashing 3D Gaussian Splatting from 4D Radar and Monocular Cues
  for 3D Object Detection](https://arxiv.org/abs/2507.19856v2)**  
  Authors: Xiaokai Bai, Chenxu Zhou, Lianqing Zheng, Si-Yuan Cao, Jianan Liu, Xiaohan Zhang, Zhengzhuang Zhang, Hui-liang Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19856v2.pdf)  
  Keywords: localization, geometry, 4d, ar, understanding, autonomous driving, 3d gaussian, dynamic, semantic, gaussian splatting, efficient  
- **[Taking Language Embedded 3D Gaussian Splatting into the Wild](https://arxiv.org/abs/2507.19830v1)**  
  Authors: Yuze Wang, Yue Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19830v1.pdf)  
  Keywords: ar, 3d reconstruction, understanding, 3d gaussian, gaussian splatting, segmentation, recognition  
- **[Gaussian Set Surface Reconstruction through Per-Gaussian Optimization](https://arxiv.org/abs/2507.18923v1)**  
  Authors: Zhentao Huang, Di Wu, Zhenbang He, Minglun Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18923v1.pdf)  
  Keywords: face, geometry, ar, 3d gaussian, gaussian splatting, efficient  
- **[Unposed 3DGS Reconstruction with Probabilistic Procrustes Mapping](https://arxiv.org/abs/2507.18541v1)**  
  Authors: Chong Cheng, Zijian Wang, Sicheng Yu, Yu Hu, Nanjie Yao, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18541v1.pdf)  
  Keywords: geometry, ar, outdoor, 3d gaussian, mapping, gaussian splatting  

### Large Scene

- **[Stereo 3D Gaussian Splatting SLAM for Outdoor Urban Scenes](https://arxiv.org/abs/2507.23677v1)**  
  Authors: Xiaohan Li, Ziren Gong, Fabio Tosi, Matteo Poggi, Stefano Mattoccia, Dong Liu, Jun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23677v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, mapping, fast, slam, gaussian splatting, urban scene, tracking, high-fidelity  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: lighting, global illumination, relightable, ar, shadow, outdoor, 3d gaussian, dynamic, gaussian splatting, relighting, face, illumination  
- **[SaLF: Sparse Local Fields for Multi-Sensor Rendering in Real-Time](https://arxiv.org/abs/2507.18713v1)**  
  Authors: Yun Chen, Matthew Haines, Jingkang Wang, Krzysztof Baron-Lis, Sivabalan Manivasagam, Ze Yang, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18713v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://waabi.ai/salf/)  
  Keywords: ar, large scene, 3d gaussian, nerf, fast, gaussian splatting, high-fidelity  
- **[Unposed 3DGS Reconstruction with Probabilistic Procrustes Mapping](https://arxiv.org/abs/2507.18541v1)**  
  Authors: Chong Cheng, Zijian Wang, Sicheng Yu, Yu Hu, Nanjie Yao, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18541v1.pdf)  
  Keywords: geometry, ar, outdoor, 3d gaussian, mapping, gaussian splatting  
- **[MUVOD: A Novel Multi-view Video Object Segmentation Dataset and A
  Benchmark for 3D Segmentation](https://arxiv.org/abs/2507.07519v1)**  
  Authors: Bangning Wei, Joshua Maraval, Meriem Outtas, Kidiyo Kpalma, Nicolas Ramin, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07519v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://volumetric-repository.labs.b-com.com/#/muvod.)  
  Keywords: 4d, ar, motion, understanding, outdoor, 3d gaussian, dynamic, nerf, gaussian splatting, segmentation  
- **[3DGS_LSR:Large_Scale Relocation for Autonomous Driving Based on 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.05661v1)**  
  Authors: Haitao Lu, Haijier Chen, Haoze Liu, Shoujian Zhang, Bo Xu, Ziao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.05661v1.pdf)  
  Keywords: localization, ar, autonomous driving, outdoor, 3d gaussian, mapping, gaussian splatting  
- **[ArmGS: Composite Gaussian Appearance Refinement for Modeling Dynamic
  Urban Environments](https://arxiv.org/abs/2507.03886v1)**  
  Authors: Guile Wu, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.03886v1.pdf)  
  Keywords: real-time rendering, ar, autonomous driving, 3d gaussian, dynamic, gaussian splatting, urban scene, high-fidelity  
- **[Outdoor Monocular SLAM with Global Scale-Consistent 3D Gaussian
  Pointmaps](https://arxiv.org/abs/2507.03737v2)**  
  Authors: Chong Cheng, Sicheng Yu, Zijian Wang, Yifan Zhou, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.03737v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/S3PO-GS/.)  
  Keywords: ar, outdoor, 3d gaussian, dynamic, slam, mapping, gaussian splatting, tracking, high-fidelity  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: lighting, geometry, ar, outdoor, 3d gaussian, dynamic, slam, mapping, tracking, gaussian splatting, illumination, high-fidelity  
- **[BézierGS: Dynamic Urban Scene Reconstruction with Bézier Curve
  Gaussian Splatting](https://arxiv.org/abs/2506.22099v3)**  
  Authors: Zipei Ma, Junzhe Jiang, Yurui Chen, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22099v3.pdf)  
  Keywords: ar, motion, autonomous driving, dynamic, gaussian splatting, urban scene  

### Model Compression

*Showing the latest 50 out of 83 papers*

- **[PointGauss: Point Cloud-Guided Multi-Object Segmentation for Gaussian
  Splatting](https://arxiv.org/abs/2508.00259v1)**  
  Authors: Wentao Sun, Hanqing Xu, Quanyun Wu, Dedong Zhang, Yiping Chen, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.00259v1.pdf)  
  Keywords: segmentation, efficient, ar, gaussian splatting  
- **[Gaussian Variation Field Diffusion for High-fidelity Video-to-4D
  Synthesis](https://arxiv.org/abs/2507.23785v1)**  
  Authors: Bowen Zhang, Sicheng Xu, Chuxin Wang, Jiaolong Yang, Feng Zhao, Dong Chen, Baining Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23785v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gvfdiffusion.github.io/.)  
  Keywords: 4d, ar, motion, compact, dynamic, animation, efficient, high-fidelity  
- **[I2V-GS: Infrastructure-to-Vehicle View Transformation with Gaussian
  Splatting for Autonomous Driving Data Generation](https://arxiv.org/abs/2507.23683v1)**  
  Authors: Jialei Chen, Wuhao Xu, Sipeng He, Baoru Huang, Dongchun Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23683v1.pdf)  
  Keywords: lighting, ar, 3d reconstruction, autonomous driving, gaussian splatting, efficient  
- **[NeRF Is a Valuable Assistant for 3D Gaussian Splatting](https://arxiv.org/abs/2507.23374v1)**  
  Authors: Shuangkang Fang, I-Chao Shen, Takeo Igarashi, Yufeng Wang, ZeSheng Wang, Yi Yang, Wenrui Ding, Shuchang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23374v1.pdf)  
  Keywords: ar, 3d gaussian, nerf, gaussian splatting, efficient  
- **[MagicRoad: Semantic-Aware 3D Road Surface Reconstruction via Obstacle
  Inpainting](https://arxiv.org/abs/2507.23340v1)**  
  Authors: Xingyue Peng, Yuandong Lyu, Lang Zhang, Jian Zhu, Songtao Wang, Jiaxin Deng, Songxin Lu, Weiliang Ma, Dangen She, Peng Jia, XianPeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23340v1.pdf)  
  Keywords: lighting, segmentation, face, ar, autonomous driving, 3d gaussian, dynamic, mapping, semantic, gaussian splatting, efficient  
- **[iLRM: An Iterative Large 3D Reconstruction Model](https://arxiv.org/abs/2507.23277v1)**  
  Authors: Gyeongjin Kang, Seungtae Nam, Xiangyu Sun, Sameh Khamis, Abdelrahman Mohamed, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23277v1.pdf)  
  Keywords: ar, 3d reconstruction, compact, 3d gaussian, fast, gaussian splatting, efficient, high-fidelity  
- **[GSFusion:Globally Optimized LiDAR-Inertial-Visual Mapping for Gaussian
  Splatting](https://arxiv.org/abs/2507.23273v1)**  
  Authors: Jaeseok Park, Chanoh Park, Minsu Kim, Soohwan Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23273v1.pdf)  
  Keywords: ar, 3d gaussian, mapping, slam, gaussian splatting, efficient, illumination  
- **[DISCOVERSE: Efficient Robot Simulation in Complex High-Fidelity
  Environments](https://arxiv.org/abs/2507.21981v1)**  
  Authors: Yufei Jia, Guangyu Wang, Yuhang Dong, Junzhe Wu, Yupei Zeng, Haonan Lin, Zifan Wang, Haizhou Ge, Weibin Gu, Kairui Ding, Zike Yan, Yunjie Cheng, Yue Li, Ziming Wang, Chuxuan Li, Wei Sui, Lu Shi, Guanzhong Tian, Ruqi Huang, Guyue Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.21981v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://air-discoverse.github.io/.)  
  Keywords: geometry, ar, gaussian splatting, efficient, high-fidelity  
- **[No Redundancy, No Stall: Lightweight Streaming 3D Gaussian Splatting for
  Real-time Rendering](https://arxiv.org/abs/2507.21572v2)**  
  Authors: Linye Wei, Jiajun Tang, Fan Fei, Boxin Shi, Runsheng Wang, Meng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.21572v2.pdf)  
  Keywords: lightweight, face, real-time rendering, ar, autonomous driving, 3d gaussian, mapping, gaussian splatting, efficient  
- **[Decomposing Densification in Gaussian Splatting for Faster 3D Scene
  Reconstruction](https://arxiv.org/abs/2507.20239v1)**  
  Authors: Binxiao Huang, Zhengwu Liu, Ngai Wong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20239v1.pdf)  
  Keywords: ar, 3d gaussian, dynamic, nerf, fast, gaussian splatting, efficient  

### Quality Enhancement

- **[Gaussian Variation Field Diffusion for High-fidelity Video-to-4D
  Synthesis](https://arxiv.org/abs/2507.23785v1)**  
  Authors: Bowen Zhang, Sicheng Xu, Chuxin Wang, Jiaolong Yang, Feng Zhao, Dong Chen, Baining Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23785v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gvfdiffusion.github.io/.)  
  Keywords: 4d, ar, motion, compact, dynamic, animation, efficient, high-fidelity  
- **[Enhanced Velocity Field Modeling for Gaussian Video Reconstruction](https://arxiv.org/abs/2507.23704v1)**  
  Authors: Zhenyang Li, Xiaoyang Bai, Tongchen Zhang, Pengfei Shen, Weiwei Xu, Yifan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23704v1.pdf)  
  Keywords: real-time rendering, ar, motion, vr, 3d gaussian, dynamic, deformation, gaussian splatting, high-fidelity  
- **[Stereo 3D Gaussian Splatting SLAM for Outdoor Urban Scenes](https://arxiv.org/abs/2507.23677v1)**  
  Authors: Xiaohan Li, Ziren Gong, Fabio Tosi, Matteo Poggi, Stefano Mattoccia, Dong Liu, Jun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23677v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, mapping, fast, slam, gaussian splatting, urban scene, tracking, high-fidelity  
- **[iLRM: An Iterative Large 3D Reconstruction Model](https://arxiv.org/abs/2507.23277v1)**  
  Authors: Gyeongjin Kang, Seungtae Nam, Xiangyu Sun, Sameh Khamis, Abdelrahman Mohamed, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23277v1.pdf)  
  Keywords: ar, 3d reconstruction, compact, 3d gaussian, fast, gaussian splatting, efficient, high-fidelity  
- **[DISCOVERSE: Efficient Robot Simulation in Complex High-Fidelity
  Environments](https://arxiv.org/abs/2507.21981v1)**  
  Authors: Yufei Jia, Guangyu Wang, Yuhang Dong, Junzhe Wu, Yupei Zeng, Haonan Lin, Zifan Wang, Haizhou Ge, Weibin Gu, Kairui Ding, Zike Yan, Yunjie Cheng, Yue Li, Ziming Wang, Chuxuan Li, Wei Sui, Lu Shi, Guanzhong Tian, Ruqi Huang, Guyue Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.21981v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://air-discoverse.github.io/.)  
  Keywords: geometry, ar, gaussian splatting, efficient, high-fidelity  
- **[MultiEditor: Controllable Multimodal Object Editing for Driving
  Scenarios Using 3D Gaussian Splatting Priors](https://arxiv.org/abs/2507.21872v3)**  
  Authors: Shouyi Lu, Zihan Lin, Chao Lu, Huanran Wang, Guirong Zhuo, Lianqing Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.21872v3.pdf)  
  Keywords: ar, autonomous driving, 3d gaussian, semantic, high-fidelity, gaussian splatting  
- **[Fast Learning of Non-Cooperative Spacecraft 3D Models through Primitive
  Initialization](https://arxiv.org/abs/2507.19459v1)**  
  Authors: Pol Francesch Huc, Emily Bates, Simone D'Amico  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19459v1.pdf)  
  Keywords: ar, 3d gaussian, nerf, fast, gaussian splatting, high-fidelity  
- **[SaLF: Sparse Local Fields for Multi-Sensor Rendering in Real-Time](https://arxiv.org/abs/2507.18713v1)**  
  Authors: Yun Chen, Matthew Haines, Jingkang Wang, Krzysztof Baron-Lis, Sivabalan Manivasagam, Ze Yang, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18713v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://waabi.ai/salf/)  
  Keywords: ar, large scene, 3d gaussian, nerf, fast, gaussian splatting, high-fidelity  
- **[MVG4D: Image Matrix-Based Multi-View and Motion Generation for 4D
  Content Creation from a Single Image](https://arxiv.org/abs/2507.18371v2)**  
  Authors: DongFu Yin, Xiaotian Chen, Fei Richard Yu, Xuanchen Li, Xinhao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18371v2.pdf)  
  Keywords: lightweight, 4d, ar, motion, vr, 3d gaussian, dynamic, deformation, gaussian splatting, efficient, high-fidelity  
- **[G2S-ICP SLAM: Geometry-aware Gaussian Splatting ICP SLAM](https://arxiv.org/abs/2507.18344v1)**  
  Authors: Gyuhyeon Pak, Hae Min Cho, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18344v1.pdf)  
  Keywords: localization, geometry, ar, 3d reconstruction, slam, gaussian splatting, face, tracking, high-fidelity  

### Ray Tracing

- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: lighting, global illumination, relightable, ar, shadow, outdoor, 3d gaussian, dynamic, gaussian splatting, relighting, face, illumination  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: lighting, face, ar, 3d gaussian, dynamic, gaussian splatting, path tracing  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: lighting, relightable, face, geometry, ar, ray marching, 3d gaussian, efficient rendering, relighting, efficient, gaussian splatting  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: real-time rendering, ar, gaussian splatting, ray tracing, efficient, high-fidelity  

### Relighting

- **[I2V-GS: Infrastructure-to-Vehicle View Transformation with Gaussian
  Splatting for Autonomous Driving Data Generation](https://arxiv.org/abs/2507.23683v1)**  
  Authors: Jialei Chen, Wuhao Xu, Sipeng He, Baoru Huang, Dongchun Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23683v1.pdf)  
  Keywords: lighting, ar, 3d reconstruction, autonomous driving, gaussian splatting, efficient  
- **[MagicRoad: Semantic-Aware 3D Road Surface Reconstruction via Obstacle
  Inpainting](https://arxiv.org/abs/2507.23340v1)**  
  Authors: Xingyue Peng, Yuandong Lyu, Lang Zhang, Jian Zhu, Songtao Wang, Jiaxin Deng, Songxin Lu, Weiliang Ma, Dangen She, Peng Jia, XianPeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23340v1.pdf)  
  Keywords: lighting, segmentation, face, ar, autonomous driving, 3d gaussian, dynamic, mapping, semantic, gaussian splatting, efficient  
- **[GSFusion:Globally Optimized LiDAR-Inertial-Visual Mapping for Gaussian
  Splatting](https://arxiv.org/abs/2507.23273v1)**  
  Authors: Jaeseok Park, Chanoh Park, Minsu Kim, Soohwan Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23273v1.pdf)  
  Keywords: ar, 3d gaussian, mapping, slam, gaussian splatting, efficient, illumination  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: lighting, global illumination, relightable, ar, shadow, outdoor, 3d gaussian, dynamic, gaussian splatting, relighting, face, illumination  
- **[Automated 3D-GS Registration and Fusion via Skeleton Alignment and
  Gaussian-Adaptive Features](https://arxiv.org/abs/2507.20480v1)**  
  Authors: Shiyang Liu, Dianyi Yang, Yu Gao, Bohan Ren, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20480v1.pdf)  
  Keywords: lighting, real-time rendering, ar, 3d gaussian, gaussian splatting  
- **[From Gallery to Wrist: Realistic 3D Bracelet Insertion in Videos](https://arxiv.org/abs/2507.20331v2)**  
  Authors: Chenjian Gao, Lihe Ding, Rui Han, Zhanpeng Huang, Zibin Wang, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20331v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cjeen.github.io/BraceletPaper/)  
  Keywords: lighting, ar, motion, 3d gaussian, dynamic, gaussian splatting, illumination  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: lighting, face, ar, 3d gaussian, dynamic, gaussian splatting, path tracing  
- **[PS-GS: Gaussian Splatting for Multi-View Photometric Stereo](https://arxiv.org/abs/2507.18231v1)**  
  Authors: Yixiao Chen, Bin Liang, Hanzhi Guo, Yongqing Cheng, Jiayi Zhao, Dongdong Weng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18231v1.pdf)  
  Keywords: lighting, geometry, ar, 3d reconstruction, gaussian splatting, relighting, efficient, illumination  
- **[StreamME: Simplify 3D Gaussian Avatar within Live Stream](https://arxiv.org/abs/2507.17029v1)**  
  Authors: Luchuan Song, Yang Zhou, Zhan Xu, Yi Zhou, Deepali Aneja, Chenliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.17029v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://songluchuan.github.io/StreamME/.)  
  Keywords: lighting, head, geometry, ar, vr, 3d gaussian, fast, avatar, animation, gaussian splatting, relighting, face  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: lighting, relightable, face, geometry, ar, ray marching, 3d gaussian, efficient rendering, relighting, efficient, gaussian splatting  

### SLAM

- **[Stereo 3D Gaussian Splatting SLAM for Outdoor Urban Scenes](https://arxiv.org/abs/2507.23677v1)**  
  Authors: Xiaohan Li, Ziren Gong, Fabio Tosi, Matteo Poggi, Stefano Mattoccia, Dong Liu, Jun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23677v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, mapping, fast, slam, gaussian splatting, urban scene, tracking, high-fidelity  
- **[Gaussian Splatting Feature Fields for Privacy-Preserving Visual
  Localization](https://arxiv.org/abs/2507.23569v1)**  
  Authors: Maxime Pietrantoni, Gabriela Csurka, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23569v1.pdf)  
  Keywords: localization, geometry, ar, 3d gaussian, gaussian splatting, segmentation  
- **[MagicRoad: Semantic-Aware 3D Road Surface Reconstruction via Obstacle
  Inpainting](https://arxiv.org/abs/2507.23340v1)**  
  Authors: Xingyue Peng, Yuandong Lyu, Lang Zhang, Jian Zhu, Songtao Wang, Jiaxin Deng, Songxin Lu, Weiliang Ma, Dangen She, Peng Jia, XianPeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23340v1.pdf)  
  Keywords: lighting, segmentation, face, ar, autonomous driving, 3d gaussian, dynamic, mapping, semantic, gaussian splatting, efficient  
- **[GSFusion:Globally Optimized LiDAR-Inertial-Visual Mapping for Gaussian
  Splatting](https://arxiv.org/abs/2507.23273v1)**  
  Authors: Jaeseok Park, Chanoh Park, Minsu Kim, Soohwan Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23273v1.pdf)  
  Keywords: ar, 3d gaussian, mapping, slam, gaussian splatting, efficient, illumination  
- **[No Redundancy, No Stall: Lightweight Streaming 3D Gaussian Splatting for
  Real-time Rendering](https://arxiv.org/abs/2507.21572v2)**  
  Authors: Linye Wei, Jiajun Tang, Fan Fei, Boxin Shi, Runsheng Wang, Meng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.21572v2.pdf)  
  Keywords: lightweight, face, real-time rendering, ar, autonomous driving, 3d gaussian, mapping, gaussian splatting, efficient  
- **[RaGS: Unleashing 3D Gaussian Splatting from 4D Radar and Monocular Cues
  for 3D Object Detection](https://arxiv.org/abs/2507.19856v2)**  
  Authors: Xiaokai Bai, Chenxu Zhou, Lianqing Zheng, Si-Yuan Cao, Jianan Liu, Xiaohan Zhang, Zhengzhuang Zhang, Hui-liang Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19856v2.pdf)  
  Keywords: localization, geometry, 4d, ar, understanding, autonomous driving, 3d gaussian, dynamic, semantic, gaussian splatting, efficient  
- **[DINO-SLAM: DINO-informed RGB-D SLAM for Neural Implicit and Explicit
  Representations](https://arxiv.org/abs/2507.19474v1)**  
  Authors: Ziren Gong, Xiaohan Li, Fabio Tosi, Youmin Zhang, Stefano Mattoccia, Jun Wu, Matteo Poggi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19474v1.pdf)  
  Keywords: ar, 3d gaussian, nerf, slam, gaussian splatting  
- **[Unposed 3DGS Reconstruction with Probabilistic Procrustes Mapping](https://arxiv.org/abs/2507.18541v1)**  
  Authors: Chong Cheng, Zijian Wang, Sicheng Yu, Yu Hu, Nanjie Yao, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18541v1.pdf)  
  Keywords: geometry, ar, outdoor, 3d gaussian, mapping, gaussian splatting  
- **[CRUISE: Cooperative Reconstruction and Editing in V2X Scenarios using
  Gaussian Splatting](https://arxiv.org/abs/2507.18473v1)**  
  Authors: Haoran Xu, Saining Zhang, Peishuo Li, Baijun Ye, Xiaoxue Chen, Huan-ang Gao, Jv Zheng, Xiaowei Song, Ziqiao Peng, Run Miao, Jinrang Jia, Yifeng Shi, Guangqi Yi, Hang Zhao, Hao Tang, Hongyang Li, Kaicheng Yu, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18473v1.pdf)  
  Keywords: ar, autonomous driving, dynamic, gaussian splatting, tracking  
- **[G2S-ICP SLAM: Geometry-aware Gaussian Splatting ICP SLAM](https://arxiv.org/abs/2507.18344v1)**  
  Authors: Gyuhyeon Pak, Hae Min Cho, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18344v1.pdf)  
  Keywords: localization, geometry, ar, 3d reconstruction, slam, gaussian splatting, face, tracking, high-fidelity  

### Scene Understanding

*Showing the latest 50 out of 53 papers*

- **[PointGauss: Point Cloud-Guided Multi-Object Segmentation for Gaussian
  Splatting](https://arxiv.org/abs/2508.00259v1)**  
  Authors: Wentao Sun, Hanqing Xu, Quanyun Wu, Dedong Zhang, Yiping Chen, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.00259v1.pdf)  
  Keywords: segmentation, efficient, ar, gaussian splatting  
- **[SeqAffordSplat: Scene-level Sequential Affordance Reasoning on 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.23772v1)**  
  Authors: Di Li, Jie Feng, Jiahao Chen, Weisheng Dong, Guanbin Li, Yuhui Zheng, Mingtao Feng, Guangming Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23772v1.pdf)  
  Keywords: geometry, human, ar, understanding, 3d gaussian, semantic, segmentation, gaussian splatting  
- **[Gaussian Splatting Feature Fields for Privacy-Preserving Visual
  Localization](https://arxiv.org/abs/2507.23569v1)**  
  Authors: Maxime Pietrantoni, Gabriela Csurka, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23569v1.pdf)  
  Keywords: localization, geometry, ar, 3d gaussian, gaussian splatting, segmentation  
- **[MagicRoad: Semantic-Aware 3D Road Surface Reconstruction via Obstacle
  Inpainting](https://arxiv.org/abs/2507.23340v1)**  
  Authors: Xingyue Peng, Yuandong Lyu, Lang Zhang, Jian Zhu, Songtao Wang, Jiaxin Deng, Songxin Lu, Weiliang Ma, Dangen She, Peng Jia, XianPeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23340v1.pdf)  
  Keywords: lighting, segmentation, face, ar, autonomous driving, 3d gaussian, dynamic, mapping, semantic, gaussian splatting, efficient  
- **[MultiEditor: Controllable Multimodal Object Editing for Driving
  Scenarios Using 3D Gaussian Splatting Priors](https://arxiv.org/abs/2507.21872v3)**  
  Authors: Shouyi Lu, Zihan Lin, Chao Lu, Huanran Wang, Guirong Zhuo, Lianqing Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.21872v3.pdf)  
  Keywords: ar, autonomous driving, 3d gaussian, semantic, high-fidelity, gaussian splatting  
- **[RaGS: Unleashing 3D Gaussian Splatting from 4D Radar and Monocular Cues
  for 3D Object Detection](https://arxiv.org/abs/2507.19856v2)**  
  Authors: Xiaokai Bai, Chenxu Zhou, Lianqing Zheng, Si-Yuan Cao, Jianan Liu, Xiaohan Zhang, Zhengzhuang Zhang, Hui-liang Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19856v2.pdf)  
  Keywords: localization, geometry, 4d, ar, understanding, autonomous driving, 3d gaussian, dynamic, semantic, gaussian splatting, efficient  
- **[Taking Language Embedded 3D Gaussian Splatting into the Wild](https://arxiv.org/abs/2507.19830v1)**  
  Authors: Yuze Wang, Yue Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19830v1.pdf)  
  Keywords: ar, 3d reconstruction, understanding, 3d gaussian, gaussian splatting, segmentation, recognition  
- **[EarthCrafter: Scalable 3D Earth Generation via Dual-Sparse Latent
  Diffusion](https://arxiv.org/abs/2507.16535v2)**  
  Authors: Shang Liu, Chenjie Cao, Chaohui Yu, Wen Qian, Jing Wang, Fan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16535v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://whiteinblue.github.io/earthcrafter/)  
  Keywords: face, geometry, ar, compact, semantic, segmentation  
- **[Hi^2-GSLoc: Dual-Hierarchical Gaussian-Specific Visual Relocalization
  for Remote Sensing](https://arxiv.org/abs/2507.15683v1)**  
  Authors: Boni Hu, Zhenyu Xia, Lin Chen, Pengcheng Han, Shuhui Bu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15683v1.pdf)  
  Keywords: localization, geometry, ar, motion, compact, 3d gaussian, dynamic, semantic, gaussian splatting, face  
- **[ObjectGS: Object-aware Scene Reconstruction and Scene Understanding via
  Gaussian Splatting](https://arxiv.org/abs/2507.15454v1)**  
  Authors: Ruijie Zhu, Mulin Yu, Linning Xu, Lihan Jiang, Yixuan Li, Tianzhu Zhang, Jiangmiao Pang, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15454v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ruijiezhu94.github.io/ObjectGS_page)  
  Keywords: ar, understanding, 3d gaussian, dynamic, semantic, segmentation, high-fidelity, gaussian splatting  



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