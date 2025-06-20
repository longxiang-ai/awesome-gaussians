# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-06-20 00:56:00

## Categories

- [3DGS Surveys](#3dgs-surveys) (35 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (548 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1948 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (654 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (738 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (139 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (636 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (113 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (758 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (311 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (41 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (216 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (296 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (359 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: ar, survey, neural rendering, segmentation, semantic, understanding, 3d reconstruction, outdoor, efficient, gaussian splatting, 3d gaussian, high-fidelity  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: ar, survey, segmentation, semantic, mapping, efficient, slam, localization, nerf, gaussian splatting, 3d gaussian  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: ar, survey, body, understanding, motion, dynamic, gaussian splatting, 3d gaussian, 4d  
- **[A Survey of 3D Reconstruction with Event Cameras](https://arxiv.org/abs/2505.08438v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v2.pdf)  
  Keywords: ar, survey, neural rendering, geometry, robotics, motion, 3d reconstruction, dynamic, autonomous driving, nerf, gaussian splatting, 3d gaussian, illumination  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: ar, survey, 3d reconstruction, efficient, fast, gaussian splatting  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: ar, survey, semantic, robotics, autonomous driving, nerf, 3d gaussian  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: ar, survey, 3d reconstruction, lighting, 3d gaussian  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: face, ar, survey, geometry, understanding, 3d reconstruction, outdoor, nerf, gaussian splatting, 3d gaussian, sparse view  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: ar, survey, segmentation, semantic, robotics, lighting, gaussian splatting, 3d gaussian  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v3)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v3.pdf)  
  Keywords: ar, survey, motion, 3d reconstruction, dynamic, fast, lighting, gaussian splatting, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 548 papers*

- **[3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D Gaussian-Splatting](https://arxiv.org/abs/2506.14642v1)**  
  Authors: Yuke Xing, Jiarui Wang, Peizhi Niu, Wenjie Huang, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14642v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YukeXing/3DGS-IEval-15K?style=social)](https://github.com/YukeXing/3DGS-IEval-15K)  
  Keywords: ar, human, real-time rendering, compression, gaussian splatting, 3d gaussian  
- **[ImmerseGen: Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://arxiv.org/abs/2506.14315v2)**  
  Authors: Jinyan Yuan, Bangbang Yang, Keke Wang, Panwang Pan, Lin Ma, Xuehai Zhang, Xiao Liu, Zhaopeng Cui, Yuewen Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14315v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://immersegen.github.io.)  
  Keywords: lightweight, ar, geometry, head, semantic, dynamic, vr, real-time rendering, compact, 3d gaussian  
- **[GS-2DGS: Geometrically Supervised 2DGS for Reflective Object Reconstruction](https://arxiv.org/abs/2506.13110v1)**  
  Authors: Jinguang Tong, Xuesong li, Fahira Afzal Maken, Sundaram Muthu, Lars Petersson, Chuong Nguyen, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13110v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hirotong/GS2DGS?style=social)](https://github.com/hirotong/GS2DGS)  
  Keywords: ar, relighting, lighting, fast, real-time rendering, gaussian splatting, 3d gaussian, face  
- **[Rasterizing Wireless Radiance Field via Deformable 2D Gaussian Splatting](https://arxiv.org/abs/2506.12787v2)**  
  Authors: Mufan Liu, Cixiao Zhang, Qi Yang, Yujie Cao, Yiling Xu, Yin Xu, Shu Sun, Mingzeng Dai, Yunfeng Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12787v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://evan-sudo.github.io/swiftwrf/.)  
  Keywords: lightweight, ar, compact, deformation, localization, fast, nerf, gaussian splatting  
- **[HAIF-GS: Hierarchical and Induced Flow-Guided Gaussian Splatting for Dynamic Scene](https://arxiv.org/abs/2506.09518v1)**  
  Authors: Jianing Chen, Zehao Li, Yujun Cai, Hao Jiang, Chengxuan Qian, Juyuan Kang, Shuqin Gao, Honglong Zhao, Tianlu Mao, Yucheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09518v1.pdf)  
  Keywords: ar, motion, efficient, dynamic, deformation, real-time rendering, gaussian splatting, 3d gaussian  
- **[ODG: Occupancy Prediction Using Dual Gaussians](https://arxiv.org/abs/2506.09417v2)**  
  Authors: Yunxiao Shi, Yinhao Zhu, Shizhong Han, Jisoo Jeong, Amin Ansari, Hong Cai, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09417v2.pdf)  
  Keywords: ar, geometry, semantic, dynamic, autonomous driving, real-time rendering, gaussian splatting, 3d gaussian  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: ar, geometry, segmentation, semantic, understanding, efficient, outdoor, fast, gaussian splatting, 3d gaussian  
- **[4DGT: Learning a 4D Gaussian Transformer Using Real-World Monocular Videos](https://arxiv.org/abs/2506.08015v1)**  
  Authors: Zhen Xu, Zhengqin Li, Zhao Dong, Xiaowei Zhou, Richard Newcombe, Zhaoyang Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08015v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dgt.github.io)  
  Keywords: ar, efficient, dynamic, efficient rendering, 4d  
- **[Speedy Deformable 3D Gaussian Splatting: Fast Rendering and Compression of Dynamic Scenes](https://arxiv.org/abs/2506.07917v1)**  
  Authors: Allen Tu, Haiyang Ying, Alex Hanson, Yonghan Lee, Tom Goldstein, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07917v1.pdf)  
  Keywords: ar, motion, dynamic, deformation, vr, fast, nerf, compression, gaussian splatting, 3d gaussian, 4d  
- **[PIG: Physically-based Multi-Material Interaction with 3D Gaussians](https://arxiv.org/abs/2506.07657v1)**  
  Authors: Zeyu Xiao, Zhenyi Wu, Mingyang Sun, Qipeng Yan, Yufan Guo, Zhuoer Liang, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07657v1.pdf)  
  Keywords: ar, segmentation, mapping, dynamic, deformation, fast, gaussian splatting, 3d gaussian  

### Applications

*Showing the latest 50 out of 1948 papers*

- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: ar, sparse-view, motion, dynamic, gaussian splatting  
- **[RA-NeRF: Robust Neural Radiance Field Reconstruction with Accurate Camera Pose Estimation under Complex Trajectories](https://arxiv.org/abs/2506.15242v1)**  
  Authors: Qingsong Yan, Qiang Wang, Kaiyong Zhao, Jie Chen, Bo Li, Xiaowen Chu, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15242v1.pdf)  
  Keywords: ar, 3d reconstruction, slam, localization, nerf, gaussian splatting, 3d gaussian  
- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: ar, head, efficient, dynamic, gaussian splatting, face, high-fidelity  
- **[3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D Gaussian-Splatting](https://arxiv.org/abs/2506.14642v1)**  
  Authors: Yuke Xing, Jiarui Wang, Peizhi Niu, Wenjie Huang, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14642v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YukeXing/3DGS-IEval-15K?style=social)](https://github.com/YukeXing/3DGS-IEval-15K)  
  Keywords: ar, human, real-time rendering, compression, gaussian splatting, 3d gaussian  
- **[ImmerseGen: Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://arxiv.org/abs/2506.14315v2)**  
  Authors: Jinyan Yuan, Bangbang Yang, Keke Wang, Panwang Pan, Lin Ma, Xuehai Zhang, Xiao Liu, Zhaopeng Cui, Yuewen Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14315v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://immersegen.github.io.)  
  Keywords: lightweight, ar, geometry, head, semantic, dynamic, vr, real-time rendering, compact, 3d gaussian  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: lightweight, ar, neural rendering, head, mapping, 3d reconstruction, efficient, nerf, gaussian splatting, 3d gaussian  
- **[HRGS: Hierarchical Gaussian Splatting for Memory-Efficient High-Resolution 3D Reconstruction](https://arxiv.org/abs/2506.14229v1)**  
  Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Juan Zhang, Tongfei Chen, Shuo Yang, Shuwei Shao, Wenhao Dong, Baochang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14229v1.pdf)  
  Keywords: ar, 3d reconstruction, efficient, gaussian splatting, 3d gaussian, face  
- **[GAF: Gaussian Action Field as a Dvnamic World Model for Robotic Mlanipulation](https://arxiv.org/abs/2506.14135v1)**  
  Authors: Ying Chai, Litao Deng, Ruizhi Shao, Jiajun Zhang, Liangjun Xing, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14135v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://chaiying1.github.io/GAF.github.io/project_page/)  
  Keywords: ar, geometry, motion, dynamic, gaussian splatting, 3d gaussian, 4d  
- **[GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2506.14009v1)**  
  Authors: Qianzhong Chen, Naixiang Gao, Suning Huang, JunEn Low, Timothy Chen, Jiankai Sun, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14009v1.pdf)  
  Keywords: lightweight, ar, head, compact, efficient, dynamic, gaussian splatting, 3d gaussian  
- **[PF-LHM: 3D Animatable Avatar Reconstruction from Pose-free Articulated Human Images](https://arxiv.org/abs/2506.13766v1)**  
  Authors: Lingteng Qiu, Peihao Li, Qi Zuo, Xiaodong Gu, Yuan Dong, Weihao Yuan, Siyu Zhu, Xiaoguang Han, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13766v1.pdf)  
  Keywords: ar, avatar, geometry, human, efficient, 3d gaussian, high-fidelity  

### Avatar Generation

*Showing the latest 50 out of 654 papers*

- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: ar, head, efficient, dynamic, gaussian splatting, face, high-fidelity  
- **[3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D Gaussian-Splatting](https://arxiv.org/abs/2506.14642v1)**  
  Authors: Yuke Xing, Jiarui Wang, Peizhi Niu, Wenjie Huang, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14642v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YukeXing/3DGS-IEval-15K?style=social)](https://github.com/YukeXing/3DGS-IEval-15K)  
  Keywords: ar, human, real-time rendering, compression, gaussian splatting, 3d gaussian  
- **[ImmerseGen: Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://arxiv.org/abs/2506.14315v2)**  
  Authors: Jinyan Yuan, Bangbang Yang, Keke Wang, Panwang Pan, Lin Ma, Xuehai Zhang, Xiao Liu, Zhaopeng Cui, Yuewen Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14315v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://immersegen.github.io.)  
  Keywords: lightweight, ar, geometry, head, semantic, dynamic, vr, real-time rendering, compact, 3d gaussian  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: lightweight, ar, neural rendering, head, mapping, 3d reconstruction, efficient, nerf, gaussian splatting, 3d gaussian  
- **[HRGS: Hierarchical Gaussian Splatting for Memory-Efficient High-Resolution 3D Reconstruction](https://arxiv.org/abs/2506.14229v1)**  
  Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Juan Zhang, Tongfei Chen, Shuo Yang, Shuwei Shao, Wenhao Dong, Baochang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14229v1.pdf)  
  Keywords: ar, 3d reconstruction, efficient, gaussian splatting, 3d gaussian, face  
- **[GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2506.14009v1)**  
  Authors: Qianzhong Chen, Naixiang Gao, Suning Huang, JunEn Low, Timothy Chen, Jiankai Sun, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14009v1.pdf)  
  Keywords: lightweight, ar, head, compact, efficient, dynamic, gaussian splatting, 3d gaussian  
- **[PF-LHM: 3D Animatable Avatar Reconstruction from Pose-free Articulated Human Images](https://arxiv.org/abs/2506.13766v1)**  
  Authors: Lingteng Qiu, Peihao Li, Qi Zuo, Xiaodong Gu, Yuan Dong, Weihao Yuan, Siyu Zhu, Xiaoguang Han, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13766v1.pdf)  
  Keywords: ar, avatar, geometry, human, efficient, 3d gaussian, high-fidelity  
- **[TextureSplat: Per-Primitive Texture Mapping for Reflective Gaussian Splatting](https://arxiv.org/abs/2506.13348v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13348v1.pdf)  
  Keywords: ar, gaussian splatting, face, mapping  
- **[GS-2DGS: Geometrically Supervised 2DGS for Reflective Object Reconstruction](https://arxiv.org/abs/2506.13110v1)**  
  Authors: Jinguang Tong, Xuesong li, Fahira Afzal Maken, Sundaram Muthu, Lars Petersson, Chuong Nguyen, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13110v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hirotong/GS2DGS?style=social)](https://github.com/hirotong/GS2DGS)  
  Keywords: ar, relighting, lighting, fast, real-time rendering, gaussian splatting, 3d gaussian, face  
- **[Efficient multi-view training for 3D Gaussian Splatting](https://arxiv.org/abs/2506.12727v2)**  
  Authors: Minhyuk Choi, Injae Kim, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12727v2.pdf)  
  Keywords: ar, head, efficient, lighting, nerf, gaussian splatting, 3d gaussian  

### Dynamic Scene

*Showing the latest 50 out of 738 papers*

- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: ar, sparse-view, motion, dynamic, gaussian splatting  
- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: ar, head, efficient, dynamic, gaussian splatting, face, high-fidelity  
- **[ImmerseGen: Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://arxiv.org/abs/2506.14315v2)**  
  Authors: Jinyan Yuan, Bangbang Yang, Keke Wang, Panwang Pan, Lin Ma, Xuehai Zhang, Xiao Liu, Zhaopeng Cui, Yuewen Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14315v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://immersegen.github.io.)  
  Keywords: lightweight, ar, geometry, head, semantic, dynamic, vr, real-time rendering, compact, 3d gaussian  
- **[GAF: Gaussian Action Field as a Dvnamic World Model for Robotic Mlanipulation](https://arxiv.org/abs/2506.14135v1)**  
  Authors: Ying Chai, Litao Deng, Ruizhi Shao, Jiajun Zhang, Liangjun Xing, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14135v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://chaiying1.github.io/GAF.github.io/project_page/)  
  Keywords: ar, geometry, motion, dynamic, gaussian splatting, 3d gaussian, 4d  
- **[GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2506.14009v1)**  
  Authors: Qianzhong Chen, Naixiang Gao, Suning Huang, JunEn Low, Timothy Chen, Jiankai Sun, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14009v1.pdf)  
  Keywords: lightweight, ar, head, compact, efficient, dynamic, gaussian splatting, 3d gaussian  
- **[Micro-macro Gaussian Splatting with Enhanced Scalability for Unconstrained Scene Reconstruction](https://arxiv.org/abs/2506.13516v1)**  
  Authors: Yihui Li, Chengxin Lv, Hongyu Yang, Di Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13516v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Kidleyh/SMW-GS?style=social)](https://github.com/Kidleyh/SMW-GS)  
  Keywords: ar, motion, 3d reconstruction, gaussian splatting, illumination  
- **[Metropolis-Hastings Sampling for 3D Gaussian Reconstruction](https://arxiv.org/abs/2506.12945v1)**  
  Authors: Hyunjin Kim, Haebeom Jung, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12945v1.pdf)  
  Keywords: ar, dynamic, nerf, gaussian splatting, 3d gaussian  
- **[Rasterizing Wireless Radiance Field via Deformable 2D Gaussian Splatting](https://arxiv.org/abs/2506.12787v2)**  
  Authors: Mufan Liu, Cixiao Zhang, Qi Yang, Yujie Cao, Yiling Xu, Yin Xu, Shu Sun, Mingzeng Dai, Yunfeng Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12787v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://evan-sudo.github.io/swiftwrf/.)  
  Keywords: lightweight, ar, compact, deformation, localization, fast, nerf, gaussian splatting  
- **[Generative 4D Scene Gaussian Splatting with Object View-Synthesis Priors](https://arxiv.org/abs/2506.12716v1)**  
  Authors: Wen-Hsuan Chu, Lei Ke, Jianmeng Liu, Mingxiao Huo, Pavel Tokmakov, Katerina Fragkiadaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12716v1.pdf)  
  Keywords: ar, human, dynamic, gaussian splatting, 3d gaussian, 4d  
- **[GraphGSOcc: Semantic and Geometric Graph Transformer for 3D Gaussian Splating-based Occupancy Prediction](https://arxiv.org/abs/2506.14825v1)**  
  Authors: Ke Song, Yunhe Wu, Chunchit Siu, Huiyuan Xiong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14825v1.pdf)  
  Keywords: ar, semantic, dynamic, autonomous driving, compact, 3d gaussian  

### Few-shot

*Showing the latest 50 out of 139 papers*

- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: ar, sparse-view, motion, dynamic, gaussian splatting  
- **[PointGS: Point Attention-Aware Sparse View Synthesis with Gaussian Splatting](https://arxiv.org/abs/2506.10335v1)**  
  Authors: Lintao Xiang, Hongpei Zheng, Yating Huang, Qijun Yang, Hujun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.10335v1.pdf)  
  Keywords: few-shot, lightweight, ar, nerf, gaussian splatting, 3d gaussian, sparse view  
- **[SemanticSplat: Feed-Forward 3D Scene Understanding with Language-Aware Gaussian Fields](https://arxiv.org/abs/2506.09565v2)**  
  Authors: Qijing Li, Jingxiang Sun, Liang An, Zhaoqi Su, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09565v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://semanticsplat.github.io.)  
  Keywords: ar, geometry, segmentation, semantic, sparse-view, understanding, 3d reconstruction, 3d gaussian  
- **[Synthetic Human Action Video Data Generation with Pose Transfer](https://arxiv.org/abs/2506.09411v1)**  
  Authors: Vaclav Knapp, Matyas Bohacek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09411v1.pdf)  
  Keywords: ar, avatar, human, motion, understanding, autonomous driving, recognition, 3d gaussian, few-shot  
- **[UniForward: Unified 3D Scene and Semantic Field Reconstruction via Feed-Forward Gaussian Splatting from Only Sparse-View Images](https://arxiv.org/abs/2506.09378v1)**  
  Authors: Qijian Tian, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09378v1.pdf)  
  Keywords: ar, segmentation, semantic, sparse-view, understanding, gaussian splatting, 3d gaussian  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, sparse view, high-fidelity  
- **[JointSplat: Probabilistic Joint Flow-Depth Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2506.03872v1)**  
  Authors: Yang Xiao, Guoan Xu, Qiang Wu, Wenjing Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03872v1.pdf)  
  Keywords: face, ar, sparse-view, 3d reconstruction, efficient, gaussian splatting, 3d gaussian, sparse view, high-fidelity  
- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: ar, geometry, sparse-view, efficient, nerf, gaussian splatting, 3d gaussian  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: ar, sparse-view, motion, gaussian splatting, 3d gaussian, face  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: ar, sparse-view, motion, 3d reconstruction, fast, gaussian splatting, face  

### Geometry Reconstruction

*Showing the latest 50 out of 636 papers*

- **[RA-NeRF: Robust Neural Radiance Field Reconstruction with Accurate Camera Pose Estimation under Complex Trajectories](https://arxiv.org/abs/2506.15242v1)**  
  Authors: Qingsong Yan, Qiang Wang, Kaiyong Zhao, Jie Chen, Bo Li, Xiaowen Chu, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15242v1.pdf)  
  Keywords: ar, 3d reconstruction, slam, localization, nerf, gaussian splatting, 3d gaussian  
- **[ImmerseGen: Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://arxiv.org/abs/2506.14315v2)**  
  Authors: Jinyan Yuan, Bangbang Yang, Keke Wang, Panwang Pan, Lin Ma, Xuehai Zhang, Xiao Liu, Zhaopeng Cui, Yuewen Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14315v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://immersegen.github.io.)  
  Keywords: lightweight, ar, geometry, head, semantic, dynamic, vr, real-time rendering, compact, 3d gaussian  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: lightweight, ar, neural rendering, head, mapping, 3d reconstruction, efficient, nerf, gaussian splatting, 3d gaussian  
- **[HRGS: Hierarchical Gaussian Splatting for Memory-Efficient High-Resolution 3D Reconstruction](https://arxiv.org/abs/2506.14229v1)**  
  Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Juan Zhang, Tongfei Chen, Shuo Yang, Shuwei Shao, Wenhao Dong, Baochang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14229v1.pdf)  
  Keywords: ar, 3d reconstruction, efficient, gaussian splatting, 3d gaussian, face  
- **[GAF: Gaussian Action Field as a Dvnamic World Model for Robotic Mlanipulation](https://arxiv.org/abs/2506.14135v1)**  
  Authors: Ying Chai, Litao Deng, Ruizhi Shao, Jiajun Zhang, Liangjun Xing, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14135v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://chaiying1.github.io/GAF.github.io/project_page/)  
  Keywords: ar, geometry, motion, dynamic, gaussian splatting, 3d gaussian, 4d  
- **[PF-LHM: 3D Animatable Avatar Reconstruction from Pose-free Articulated Human Images](https://arxiv.org/abs/2506.13766v1)**  
  Authors: Lingteng Qiu, Peihao Li, Qi Zuo, Xiaodong Gu, Yuan Dong, Weihao Yuan, Siyu Zhu, Xiaoguang Han, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13766v1.pdf)  
  Keywords: ar, avatar, geometry, human, efficient, 3d gaussian, high-fidelity  
- **[Micro-macro Gaussian Splatting with Enhanced Scalability for Unconstrained Scene Reconstruction](https://arxiv.org/abs/2506.13516v1)**  
  Authors: Yihui Li, Chengxin Lv, Hongyu Yang, Di Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13516v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Kidleyh/SMW-GS?style=social)](https://github.com/Kidleyh/SMW-GS)  
  Keywords: ar, motion, 3d reconstruction, gaussian splatting, illumination  
- **[Multiview Geometric Regularization of Gaussian Splatting for Accurate Radiance Fields](https://arxiv.org/abs/2506.13508v1)**  
  Authors: Jungeon Kim, Geonsoo Park, Seungyong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13508v1.pdf)  
  Keywords: ar, geometry, outdoor, gaussian splatting, 3d gaussian  
- **[SPLATART: Articulated Gaussian Splatting with Estimated Object Structure](https://arxiv.org/abs/2506.12184v1)**  
  Authors: Stanley Lewis, Vishal Chandra, Tom Gao, Odest Chadwicke Jenkins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12184v1.pdf)  
  Keywords: ar, geometry, segmentation, robotics, gaussian splatting  
- **[The Less You Depend, The More You Learn: Synthesizing Novel Views from Sparse, Unposed Images without Any 3D Knowledge](https://arxiv.org/abs/2506.09885v1)**  
  Authors: Haoru Wang, Kai Ye, Yangyan Li, Wenzheng Chen, Baoquan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09885v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/Less3Depend/)  
  Keywords: geometry, nerf, ar  

### Large Scene

*Showing the latest 50 out of 113 papers*

- **[Multiview Geometric Regularization of Gaussian Splatting for Accurate Radiance Fields](https://arxiv.org/abs/2506.13508v1)**  
  Authors: Jungeon Kim, Geonsoo Park, Seungyong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13508v1.pdf)  
  Keywords: ar, geometry, outdoor, gaussian splatting, 3d gaussian  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: ar, geometry, segmentation, semantic, understanding, efficient, outdoor, fast, gaussian splatting, 3d gaussian  
- **[TraGraph-GS: Trajectory Graph-based Gaussian Splatting for Arbitrary Large-Scale Scene Rendering](https://arxiv.org/abs/2506.08704v1)**  
  Authors: Xiaohan Zhang, Sitong Wang, Yushen Yan, Yi Yang, Mingda Xu, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08704v1.pdf)  
  Keywords: large scene, gaussian splatting, ar  
- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: ar, large scene, motion, efficient, slam, fast, gaussian splatting, 3d gaussian  
- **[Photoreal Scene Reconstruction from an Egocentric Device](https://arxiv.org/abs/2506.04444v1)**  
  Authors: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04444v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.projectaria.com/photoreal-reconstruction/)  
  Keywords: ar, dynamic, outdoor, lighting, gaussian splatting  
- **[VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians](https://arxiv.org/abs/2506.02741v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02741v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/VTGaussian-SLAM-Project)  
  Keywords: ar, geometry, large scene, mapping, tracking, efficient, slam, localization, 3d gaussian  
- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: ar, head, efficient, dynamic, outdoor, efficient rendering, real-time rendering, nerf, gaussian splatting, 3d gaussian  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v3)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v3.pdf)  
  Keywords: lightweight, urban scene, ar, geometry, compact, efficient, real-time rendering, gaussian splatting, 3d gaussian  
- **[HaloGS: Loose Coupling of Compact Geometry and Gaussian Splats for 3D Scenes](https://arxiv.org/abs/2505.20267v1)**  
  Authors: Changjian Jiang, Kerui Ren, Linning Xu, Jiong Chen, Jiangmiao Pang, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20267v1.pdf)  
  Keywords: lightweight, ar, geometry, 3d reconstruction, outdoor, compact  
- **[VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale Scenes](https://arxiv.org/abs/2505.18992v1)**  
  Authors: Tianchen Deng, Wenhua Wu, Junjie He, Yue Pan, Xirui Jiang, Shenghai Yuan, Danwei Wang, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18992v1.pdf) | [![GitHub](https://img.shields.io/github/stars/dtc111111/vpgs-slam?style=social)](https://github.com/dtc111111/vpgs-slam)  
  Keywords: ar, mapping, compact, tracking, slam, outdoor, gaussian splatting, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 758 papers*

- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: ar, head, efficient, dynamic, gaussian splatting, face, high-fidelity  
- **[3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D Gaussian-Splatting](https://arxiv.org/abs/2506.14642v1)**  
  Authors: Yuke Xing, Jiarui Wang, Peizhi Niu, Wenjie Huang, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14642v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YukeXing/3DGS-IEval-15K?style=social)](https://github.com/YukeXing/3DGS-IEval-15K)  
  Keywords: ar, human, real-time rendering, compression, gaussian splatting, 3d gaussian  
- **[ImmerseGen: Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://arxiv.org/abs/2506.14315v2)**  
  Authors: Jinyan Yuan, Bangbang Yang, Keke Wang, Panwang Pan, Lin Ma, Xuehai Zhang, Xiao Liu, Zhaopeng Cui, Yuewen Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14315v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://immersegen.github.io.)  
  Keywords: lightweight, ar, geometry, head, semantic, dynamic, vr, real-time rendering, compact, 3d gaussian  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: lightweight, ar, neural rendering, head, mapping, 3d reconstruction, efficient, nerf, gaussian splatting, 3d gaussian  
- **[HRGS: Hierarchical Gaussian Splatting for Memory-Efficient High-Resolution 3D Reconstruction](https://arxiv.org/abs/2506.14229v1)**  
  Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Juan Zhang, Tongfei Chen, Shuo Yang, Shuwei Shao, Wenhao Dong, Baochang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14229v1.pdf)  
  Keywords: ar, 3d reconstruction, efficient, gaussian splatting, 3d gaussian, face  
- **[GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2506.14009v1)**  
  Authors: Qianzhong Chen, Naixiang Gao, Suning Huang, JunEn Low, Timothy Chen, Jiankai Sun, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14009v1.pdf)  
  Keywords: lightweight, ar, head, compact, efficient, dynamic, gaussian splatting, 3d gaussian  
- **[PF-LHM: 3D Animatable Avatar Reconstruction from Pose-free Articulated Human Images](https://arxiv.org/abs/2506.13766v1)**  
  Authors: Lingteng Qiu, Peihao Li, Qi Zuo, Xiaodong Gu, Yuan Dong, Weihao Yuan, Siyu Zhu, Xiaoguang Han, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13766v1.pdf)  
  Keywords: ar, avatar, geometry, human, efficient, 3d gaussian, high-fidelity  
- **[X-Scene: Large-Scale Driving Scene Generation with High Fidelity and Flexible Controllability](https://arxiv.org/abs/2506.13558v1)**  
  Authors: Yu Yang, Alan Liang, Jianbiao Mei, Yukai Ma, Yong Liu, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13558v1.pdf)  
  Keywords: ar, efficient, autonomous driving, semantic  
- **[Rasterizing Wireless Radiance Field via Deformable 2D Gaussian Splatting](https://arxiv.org/abs/2506.12787v2)**  
  Authors: Mufan Liu, Cixiao Zhang, Qi Yang, Yujie Cao, Yiling Xu, Yin Xu, Shu Sun, Mingzeng Dai, Yunfeng Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12787v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://evan-sudo.github.io/swiftwrf/.)  
  Keywords: lightweight, ar, compact, deformation, localization, fast, nerf, gaussian splatting  
- **[Efficient multi-view training for 3D Gaussian Splatting](https://arxiv.org/abs/2506.12727v2)**  
  Authors: Minhyuk Choi, Injae Kim, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12727v2.pdf)  
  Keywords: ar, head, efficient, lighting, nerf, gaussian splatting, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 311 papers*

- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: ar, head, efficient, dynamic, gaussian splatting, face, high-fidelity  
- **[PF-LHM: 3D Animatable Avatar Reconstruction from Pose-free Articulated Human Images](https://arxiv.org/abs/2506.13766v1)**  
  Authors: Lingteng Qiu, Peihao Li, Qi Zuo, Xiaodong Gu, Yuan Dong, Weihao Yuan, Siyu Zhu, Xiaoguang Han, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13766v1.pdf)  
  Keywords: ar, avatar, geometry, human, efficient, 3d gaussian, high-fidelity  
- **[GaussianVAE: Adaptive Learning Dynamics of 3D Gaussians for High-Fidelity Super-Resolution](https://arxiv.org/abs/2506.07897v1)**  
  Authors: Shuja Khalid, Mohamed Ibrahim, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07897v1.pdf)  
  Keywords: lightweight, ar, dynamic, gaussian splatting, 3d gaussian, high-fidelity  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, sparse view, high-fidelity  
- **[Parametric Gaussian Human Model: Generalizable Prior for Efficient and Realistic Human Avatar Modeling](https://arxiv.org/abs/2506.06645v1)**  
  Authors: Cheng Peng, Jingxiang Sun, Yushuo Chen, Zhaoqi Su, Zhuo Su, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06645v1.pdf)  
  Keywords: ar, avatar, geometry, head, human, compact, efficient, fast, gaussian splatting, 3d gaussian, face, high-fidelity  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: ar, geometry, motion, 3d reconstruction, efficient, lighting, gaussian splatting, 3d gaussian, high-fidelity  
- **[ODE-GS: Latent ODEs for Dynamic Scene Extrapolation with 3D Gaussian Splatting](https://arxiv.org/abs/2506.05480v1)**  
  Authors: Daniel Wang, Patrick Rim, Tian Tian, Alex Wong, Ganesh Sundaramoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05480v1.pdf)  
  Keywords: lightweight, ar, neural rendering, dynamic, deformation, nerf, gaussian splatting, 3d gaussian, high-fidelity  
- **[DSG-World: Learning a 3D Gaussian World Model from Dual State Videos](https://arxiv.org/abs/2506.05217v1)**  
  Authors: Wenhao Hu, Xuexiang Wen, Xi Li, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05217v1.pdf)  
  Keywords: ar, segmentation, semantic, robotics, 3d reconstruction, efficient, lighting, 3d gaussian, high-fidelity  
- **[Generating Synthetic Stereo Datasets using 3D Gaussian Splatting and Expert Knowledge Transfer](https://arxiv.org/abs/2506.04908v1)**  
  Authors: Filip Slezak, Magnus K. Gjerde, Joakim B. Haurum, Ivan Nikolov, Morten S. Laursen, Thomas B. Moeslund  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04908v1.pdf)  
  Keywords: ar, geometry, efficient, fast, nerf, gaussian splatting, 3d gaussian, high-fidelity  
- **[Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations](https://arxiv.org/abs/2506.04789v1)**  
  Authors: Gaia Di Lorenzo, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04789v1.pdf)  
  Keywords: ar, geometry, semantic, understanding, robotics, localization, gaussian splatting, 3d gaussian, high-fidelity  

### Ray Tracing

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: face, relightable, ar, neural rendering, relighting, geometry, human, 3d gaussian, shadow, lighting, gaussian splatting, ray tracing, illumination, high-fidelity  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: relightable, ar, avatar, shadow, geometry, relighting, human, fast, lighting, gaussian splatting, ray tracing  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: ar, gaussian splatting, relighting, efficient, efficient rendering, 3d gaussian, lighting, acceleration, ray tracing  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: ar, gaussian splatting, compact, animation, efficient, dynamic, 3d gaussian, acceleration, ray marching  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: face, ar, gaussian splatting, ray tracing, lighting, efficient, real-time rendering, global illumination, 3d gaussian, illumination  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: face, light transport, lighting, dynamic, fast, real-time rendering, global illumination, 3d gaussian, illumination  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: ar, shadow, neural rendering, reflection, 3d gaussian, fast, gaussian splatting, ray tracing  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: relightable, ar, geometry, tracking, efficient, dynamic, real-time rendering, lighting, ray tracing, 4d, face  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: reflection, shadow, lighting, gaussian splatting, ray tracing, face  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ar, survey, 3d gaussian, gaussian splatting, ray tracing  

### Relighting

*Showing the latest 50 out of 216 papers*

- **[Micro-macro Gaussian Splatting with Enhanced Scalability for Unconstrained Scene Reconstruction](https://arxiv.org/abs/2506.13516v1)**  
  Authors: Yihui Li, Chengxin Lv, Hongyu Yang, Di Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13516v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Kidleyh/SMW-GS?style=social)](https://github.com/Kidleyh/SMW-GS)  
  Keywords: ar, motion, 3d reconstruction, gaussian splatting, illumination  
- **[GS-2DGS: Geometrically Supervised 2DGS for Reflective Object Reconstruction](https://arxiv.org/abs/2506.13110v1)**  
  Authors: Jinguang Tong, Xuesong li, Fahira Afzal Maken, Sundaram Muthu, Lars Petersson, Chuong Nguyen, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13110v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hirotong/GS2DGS?style=social)](https://github.com/hirotong/GS2DGS)  
  Keywords: ar, relighting, lighting, fast, real-time rendering, gaussian splatting, 3d gaussian, face  
- **[Efficient multi-view training for 3D Gaussian Splatting](https://arxiv.org/abs/2506.12727v2)**  
  Authors: Minhyuk Choi, Injae Kim, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12727v2.pdf)  
  Keywords: ar, head, efficient, lighting, nerf, gaussian splatting, 3d gaussian  
- **[R3D2: Realistic 3D Asset Insertion via Diffusion for Autonomous Driving Simulation](https://arxiv.org/abs/2506.07826v1)**  
  Authors: William Ljungbergh, Bernardo Taveira, Wenzhao Zheng, Adam Tonderski, Chensheng Peng, Fredrik Kahl, Christoffer Petersson, Michael Felsberg, Kurt Keutzer, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07826v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/R3D2/.)  
  Keywords: lightweight, ar, neural rendering, dynamic, autonomous driving, shadow, lighting, gaussian splatting, 3d gaussian, illumination  
- **[SPC to 3D: Novel View Synthesis from Binary SPC via I2I translation](https://arxiv.org/abs/2506.06890v1)**  
  Authors: Sumit Sharma, Gopi Raju Matta, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06890v1.pdf)  
  Keywords: ar, 3d reconstruction, nerf, gaussian splatting, illumination  
- **[BecomingLit: Relightable Gaussian Avatars with Hybrid Neural Shading](https://arxiv.org/abs/2506.06271v1)**  
  Authors: Jonathan Schmidt, Simon Giebenhain, Matthias Niessner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06271v1.pdf)  
  Keywords: face, relightable, ar, avatar, relighting, head, dynamic, lighting, 3d gaussian, illumination  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: ar, geometry, motion, 3d reconstruction, efficient, lighting, gaussian splatting, 3d gaussian, high-fidelity  
- **[DSG-World: Learning a 3D Gaussian World Model from Dual State Videos](https://arxiv.org/abs/2506.05217v1)**  
  Authors: Wenhao Hu, Xuexiang Wen, Xi Li, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05217v1.pdf)  
  Keywords: ar, segmentation, semantic, robotics, 3d reconstruction, efficient, lighting, 3d gaussian, high-fidelity  
- **[Photoreal Scene Reconstruction from an Egocentric Device](https://arxiv.org/abs/2506.04444v1)**  
  Authors: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04444v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.projectaria.com/photoreal-reconstruction/)  
  Keywords: ar, dynamic, outdoor, lighting, gaussian splatting  
- **[Robust Neural Rendering in the Wild with Asymmetric Dual 3D Gaussian Splatting](https://arxiv.org/abs/2506.03538v1)**  
  Authors: Chengqi Li, Zhihao Shi, Yangdi Lu, Wenbo He, Xiangyu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03538v1.pdf)  
  Keywords: lightweight, ar, neural rendering, geometry, 3d reconstruction, dynamic, lighting, gaussian splatting, 3d gaussian  

### SLAM

*Showing the latest 50 out of 296 papers*

- **[RA-NeRF: Robust Neural Radiance Field Reconstruction with Accurate Camera Pose Estimation under Complex Trajectories](https://arxiv.org/abs/2506.15242v1)**  
  Authors: Qingsong Yan, Qiang Wang, Kaiyong Zhao, Jie Chen, Bo Li, Xiaowen Chu, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15242v1.pdf)  
  Keywords: ar, 3d reconstruction, slam, localization, nerf, gaussian splatting, 3d gaussian  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: lightweight, ar, neural rendering, head, mapping, 3d reconstruction, efficient, nerf, gaussian splatting, 3d gaussian  
- **[TextureSplat: Per-Primitive Texture Mapping for Reflective Gaussian Splatting](https://arxiv.org/abs/2506.13348v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13348v1.pdf)  
  Keywords: ar, gaussian splatting, face, mapping  
- **[Rasterizing Wireless Radiance Field via Deformable 2D Gaussian Splatting](https://arxiv.org/abs/2506.12787v2)**  
  Authors: Mufan Liu, Cixiao Zhang, Qi Yang, Yujie Cao, Yiling Xu, Yin Xu, Shu Sun, Mingzeng Dai, Yunfeng Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12787v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://evan-sudo.github.io/swiftwrf/.)  
  Keywords: lightweight, ar, compact, deformation, localization, fast, nerf, gaussian splatting  
- **[Anti-Aliased 2D Gaussian Splatting](https://arxiv.org/abs/2506.11252v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.11252v1.pdf)  
  Keywords: ar, mapping, efficient, gaussian splatting, face  
- **[DGS-LRM: Real-Time Deformable 3D Gaussian Reconstruction From Monocular Videos](https://arxiv.org/abs/2506.09997v1)**  
  Authors: Chieh Hubert Lin, Zhaoyang Lv, Songyin Wu, Zhen Xu, Thu Nguyen-Phuoc, Hung-Yu Tseng, Julian Straub, Numair Khan, Lei Xiao, Ming-Hsuan Yang, Yuheng Ren, Richard Newcombe, Zhao Dong, Zhengqin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09997v1.pdf)  
  Keywords: ar, tracking, motion, dynamic, deformation, 3d gaussian  
- **[PIG: Physically-based Multi-Material Interaction with 3D Gaussians](https://arxiv.org/abs/2506.07657v1)**  
  Authors: Zeyu Xiao, Zhenyi Wu, Mingyang Sun, Qipeng Yan, Yufan Guo, Zhuoer Liang, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07657v1.pdf)  
  Keywords: ar, segmentation, mapping, dynamic, deformation, fast, gaussian splatting, 3d gaussian  
- **[Gaussian Mapping for Evolving Scenes](https://arxiv.org/abs/2506.06909v1)**  
  Authors: Vladimir Yugay, Thies Kersten, Luca Carlone, Theo Gevers, Martin R. Oswald, Lukas Schmid  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06909v1.pdf)  
  Keywords: ar, semantic, mapping, motion, robotics, dynamic, autonomous driving, gaussian splatting, 3d gaussian  
- **[Hi-LSplat: Hierarchical 3D Language Gaussian Splatting](https://arxiv.org/abs/2506.06822v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06822v1.pdf)  
  Keywords: ar, segmentation, semantic, understanding, localization, gaussian splatting  
- **[GS4: Generalizable Sparse Splatting Semantic SLAM](https://arxiv.org/abs/2506.06517v1)**  
  Authors: Mingqi Jiang, Chanho Kim, Chen Ziwen, Li Fuxin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06517v1.pdf)  
  Keywords: ar, segmentation, semantic, mapping, tracking, slam, localization, recognition, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 359 papers*

- **[ImmerseGen: Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://arxiv.org/abs/2506.14315v2)**  
  Authors: Jinyan Yuan, Bangbang Yang, Keke Wang, Panwang Pan, Lin Ma, Xuehai Zhang, Xiao Liu, Zhaopeng Cui, Yuewen Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14315v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://immersegen.github.io.)  
  Keywords: lightweight, ar, geometry, head, semantic, dynamic, vr, real-time rendering, compact, 3d gaussian  
- **[X-Scene: Large-Scale Driving Scene Generation with High Fidelity and Flexible Controllability](https://arxiv.org/abs/2506.13558v1)**  
  Authors: Yu Yang, Alan Liang, Jianbiao Mei, Yukai Ma, Yong Liu, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13558v1.pdf)  
  Keywords: ar, efficient, autonomous driving, semantic  
- **[SPLATART: Articulated Gaussian Splatting with Estimated Object Structure](https://arxiv.org/abs/2506.12184v1)**  
  Authors: Stanley Lewis, Vishal Chandra, Tom Gao, Odest Chadwicke Jenkins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12184v1.pdf)  
  Keywords: ar, geometry, segmentation, robotics, gaussian splatting  
- **[GraphGSOcc: Semantic and Geometric Graph Transformer for 3D Gaussian Splating-based Occupancy Prediction](https://arxiv.org/abs/2506.14825v1)**  
  Authors: Ke Song, Yunhe Wu, Chunchit Siu, Huiyuan Xiong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14825v1.pdf)  
  Keywords: ar, semantic, dynamic, autonomous driving, compact, 3d gaussian  
- **[Self-Supervised Multi-Part Articulated Objects Modeling via Deformable Gaussian Splatting and Progressive Primitive Segmentation](https://arxiv.org/abs/2506.09663v1)**  
  Authors: Haowen Wang, Xiaoping Yuan, Zhao Jin, Zhen Zhao, Zhengping Che, Yousong Xue, Jin Tian, Yakun Huang, Jian Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09663v1.pdf)  
  Keywords: ar, geometry, segmentation, human, motion, compact, deformation, gaussian splatting, 3d gaussian  
- **[SemanticSplat: Feed-Forward 3D Scene Understanding with Language-Aware Gaussian Fields](https://arxiv.org/abs/2506.09565v2)**  
  Authors: Qijing Li, Jingxiang Sun, Liang An, Zhaoqi Su, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09565v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://semanticsplat.github.io.)  
  Keywords: ar, geometry, segmentation, semantic, sparse-view, understanding, 3d reconstruction, 3d gaussian  
- **[ODG: Occupancy Prediction Using Dual Gaussians](https://arxiv.org/abs/2506.09417v2)**  
  Authors: Yunxiao Shi, Yinhao Zhu, Shizhong Han, Jisoo Jeong, Amin Ansari, Hong Cai, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09417v2.pdf)  
  Keywords: ar, geometry, semantic, dynamic, autonomous driving, real-time rendering, gaussian splatting, 3d gaussian  
- **[Synthetic Human Action Video Data Generation with Pose Transfer](https://arxiv.org/abs/2506.09411v1)**  
  Authors: Vaclav Knapp, Matyas Bohacek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09411v1.pdf)  
  Keywords: ar, avatar, human, motion, understanding, autonomous driving, recognition, 3d gaussian, few-shot  
- **[UniForward: Unified 3D Scene and Semantic Field Reconstruction via Feed-Forward Gaussian Splatting from Only Sparse-View Images](https://arxiv.org/abs/2506.09378v1)**  
  Authors: Qijian Tian, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09378v1.pdf)  
  Keywords: ar, segmentation, semantic, sparse-view, understanding, gaussian splatting, 3d gaussian  
- **[Gaussian2Scene: 3D Scene Representation Learning via Self-supervised Learning with 3D Gaussian Splatting](https://arxiv.org/abs/2506.08777v2)**  
  Authors: Keyi Liu, Weidong Yang, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08777v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, understanding  



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

## Contribution Guidelines
Feel free to submit Pull Requests to improve this list! Please follow these formats:
- Paper entry format: `**[Paper Title](link)** - Brief description`
- Project entry format: `[Project Name](link) - Project description`

## License
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) 