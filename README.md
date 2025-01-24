# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-01-24 00:45:14

## Categories

- [3DGS Surveys](#3dgs-surveys) (20 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (361 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1251 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (417 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (466 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (91 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (414 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (69 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (465 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (203 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (28 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (136 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (182 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (217 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: outdoor, geometry, ar, localization, survey, tracking, mapping, slam, reflection, dynamic, face, 3d gaussian, lighting  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: recognition, illumination, ar, survey, gaussian splatting, 3d gaussian  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: high-fidelity, geometry, 3d reconstruction, ar, autonomous driving, survey, gaussian splatting, semantic, compact, nerf, dynamic, robotics, lighting  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: understanding, ar, survey, gaussian splatting, real-time rendering, nerf, robotics, 3d gaussian  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: high-fidelity, lighting, ar, survey, gaussian splatting, nerf, 3d gaussian  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: 3d reconstruction, ar, autonomous driving, survey, gaussian splatting, nerf, robotics, vr, 3d gaussian  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: survey, 3d gaussian, ar  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v2)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v2.pdf)  
  Keywords: understanding, ar, survey, gaussian splatting, real-time rendering, efficient, 3d gaussian  
- **[Survey on Fundamental Deep Learning 3D Reconstruction Techniques](https://arxiv.org/abs/2407.08137v1)**  
  Authors: Yonge Bai, LikHang Wong, TszYin Twan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.08137v1.pdf)  
  Keywords: lighting, 3d reconstruction, ar, survey, gaussian splatting, nerf, 3d gaussian  
- **[Panopticon: a telescope for our times](https://arxiv.org/abs/2407.05103v2)**  
  Authors: Will Saunders, Timothy Chin, Michael Goodwin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05103v2.pdf)  
  Keywords: survey, ar  

### Acceleration

*Showing the latest 50 out of 361 papers*

- **[DARB-Splatting: Generalizing Splatting with Decaying Anisotropic Radial Basis Functions](https://arxiv.org/abs/2501.12369v1)**  
  Authors: Vishagar Arunan, Saeedha Nazar, Hashiru Pramuditha, Vinasirajan Viruthshaan, Sameera Ramasinghe, Simon Lucey, Ranga Rodrigo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12369v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, fast, efficient, 3d gaussian  
- **[Decoupling Appearance Variations with 3D Consistent Features in Gaussian Splatting](https://arxiv.org/abs/2501.10788v1)**  
  Authors: Jiaqi Lin, Zhihao Li, Binxiao Huang, Xiao Tang, Jianzhuang Liu, Shiyong Liu, Xiaofei Wu, Fenglong Song, Wenming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10788v1.pdf)  
  Keywords: head, ar, gaussian splatting, real-time rendering, efficient  
- **[Object-Centric 2D Gaussian Splatting: Background Removal and Occlusion-Aware Pruning for Compact Object Models](https://arxiv.org/abs/2501.08174v1)**  
  Authors: Marcel Rogge, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08174v1.pdf)  
  Keywords: gaussian splatting, ar, fast, compact  
- **[ActiveGAMER: Active GAussian Mapping through Efficient Rendering](https://arxiv.org/abs/2501.06897v1)**  
  Authors: Liyan Chen, Huangying Zhan, Kevin Chen, Xiangyu Xu, Qingan Yan, Changjiang Cai, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06897v1.pdf)  
  Keywords: efficient rendering, ar, gaussian splatting, mapping, nerf, dynamic, efficient, 3d gaussian  
- **[MapGS: Generalizable Pretraining and Data Augmentation for Online Mapping via Novel View Synthesis](https://arxiv.org/abs/2501.06660v1)**  
  Authors: Hengyuan Zhang, David Paz, Yuliang Guo, Xinyu Huang, Henrik I. Christensen, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06660v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://henryzhangzhy.github.io/mapgs.)  
  Keywords: ar, gaussian splatting, fast, mapping, efficient  
- **[Locality-aware Gaussian Compression for Fast and High-quality Rendering](https://arxiv.org/abs/2501.05757v1)**  
  Authors: Seungjoo Shin, Jaesik Park, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.05757v1.pdf)  
  Keywords: ar, gaussian splatting, compression, fast, compact, 3d gaussian  
- **[FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency](https://arxiv.org/abs/2501.04628v1)**  
  Authors: Han Huang, Yulun Wu, Chao Deng, Ge Gao, Ming Gu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04628v1.pdf)  
  Keywords: ar, gaussian splatting, fast, sparse view, face, sparse-view  
- **[CrossView-GS: Cross-view Gaussian Splatting For Large-scale Scene Reconstruction](https://arxiv.org/abs/2501.01695v1)**  
  Authors: Chenhao Zhang, Yuanping Cao, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01695v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, 3d gaussian, ar  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: outdoor, understanding, ar, motion, real-time rendering, dynamic, 3d gaussian  
- **[PanoSLAM: Panoptic 3D Scene Reconstruction via Gaussian SLAM](https://arxiv.org/abs/2501.00352v1)**  
  Authors: Runnan Chen, Zhaoqing Wang, Jiepeng Wang, Yuexin Ma, Mingming Gong, Wenping Wang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00352v1.pdf) | [![GitHub](https://img.shields.io/github/stars/runnanchen/PanoSLAM?style=social)](https://github.com/runnanchen/PanoSLAM)  
  Keywords: understanding, efficient rendering, 3d reconstruction, ar, localization, gaussian splatting, semantic, tracking, mapping, slam, efficient, robotics, 3d gaussian, segmentation  

### Applications

*Showing the latest 50 out of 1251 papers*

- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: outdoor, ar, gaussian splatting, efficient, 3d gaussian  
- **[DARB-Splatting: Generalizing Splatting with Decaying Anisotropic Radial Basis Functions](https://arxiv.org/abs/2501.12369v1)**  
  Authors: Vishagar Arunan, Saeedha Nazar, Hashiru Pramuditha, Vinasirajan Viruthshaan, Sameera Ramasinghe, Simon Lucey, Ranga Rodrigo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12369v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, fast, efficient, 3d gaussian  
- **[HAC++: Towards 100X Compression of 3D Gaussian Splatting](https://arxiv.org/abs/2501.12255v2)**  
  Authors: Yihang Chen, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12255v2.pdf) | [![GitHub](https://img.shields.io/github/stars/YihangChen-ee/HAC-plus?style=social)](https://github.com/YihangChen-ee/HAC-plus)  
  Keywords: ar, gaussian splatting, compression, compact, 3d gaussian  
- **[GSVC: Efficient Video Representation and Compression Through 2D Gaussian Splatting](https://arxiv.org/abs/2501.12060v2)**  
  Authors: Longan Wang, Yuang Shi, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12060v2.pdf)  
  Keywords: ar, motion, gaussian splatting, compression, dynamic, efficient, 3d gaussian  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: ar, gaussian splatting, 4d, semantic, sparse-view, 3d gaussian  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, nerf, efficient, sparse-view, 3d gaussian  
- **[Car-GS: Addressing Reflective and Transparent Surface Challenges in 3D Car Reconstruction](https://arxiv.org/abs/2501.11020v1)**  
  Authors: Congcong Li, Jin Wang, Xiaomeng Wang, Xingchen Zhou, Wei Wu, Yuzhi Zhang, Tongyi Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lcc815.github.io/Car-GS.)  
  Keywords: geometry, ar, autonomous driving, reflection, face  
- **[Decoupling Appearance Variations with 3D Consistent Features in Gaussian Splatting](https://arxiv.org/abs/2501.10788v1)**  
  Authors: Jiaqi Lin, Zhihao Li, Binxiao Huang, Xiao Tang, Jianzhuang Liu, Shiyong Liu, Xiaofei Wu, Fenglong Song, Wenming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10788v1.pdf)  
  Keywords: head, ar, gaussian splatting, real-time rendering, efficient  
- **[GSTAR: Gaussian Surface Tracking and Reconstruction](https://arxiv.org/abs/2501.10283v2)**  
  Authors: Chengwei Zheng, Lixin Xue, Juan Zarate, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10283v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/GSTAR/.)  
  Keywords: ar, gaussian splatting, tracking, dynamic, efficient, face, 3d gaussian  
- **[GaussianAvatar-Editor: Photorealistic Animatable Gaussian Head Avatar Editor](https://arxiv.org/abs/2501.09978v1)**  
  Authors: Xiangyue Liu, Kunming Luo, Heng Li, Qi Zhang, Yuan Liu, Li Yi, Ping Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.09978v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiangyueliu.github.io/GaussianAvatar-Editor/).)  
  Keywords: head, avatar, ar, motion, 4d, animation, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 417 papers*

- **[Car-GS: Addressing Reflective and Transparent Surface Challenges in 3D Car Reconstruction](https://arxiv.org/abs/2501.11020v1)**  
  Authors: Congcong Li, Jin Wang, Xiaomeng Wang, Xingchen Zhou, Wei Wu, Yuzhi Zhang, Tongyi Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lcc815.github.io/Car-GS.)  
  Keywords: geometry, ar, autonomous driving, reflection, face  
- **[Decoupling Appearance Variations with 3D Consistent Features in Gaussian Splatting](https://arxiv.org/abs/2501.10788v1)**  
  Authors: Jiaqi Lin, Zhihao Li, Binxiao Huang, Xiao Tang, Jianzhuang Liu, Shiyong Liu, Xiaofei Wu, Fenglong Song, Wenming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10788v1.pdf)  
  Keywords: head, ar, gaussian splatting, real-time rendering, efficient  
- **[GSTAR: Gaussian Surface Tracking and Reconstruction](https://arxiv.org/abs/2501.10283v2)**  
  Authors: Chengwei Zheng, Lixin Xue, Juan Zarate, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10283v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/GSTAR/.)  
  Keywords: ar, gaussian splatting, tracking, dynamic, efficient, face, 3d gaussian  
- **[GaussianAvatar-Editor: Photorealistic Animatable Gaussian Head Avatar Editor](https://arxiv.org/abs/2501.09978v1)**  
  Authors: Xiangyue Liu, Kunming Luo, Heng Li, Qi Zhang, Yuan Liu, Li Yi, Ping Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.09978v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiangyueliu.github.io/GaussianAvatar-Editor/).)  
  Keywords: head, avatar, ar, motion, 4d, animation, 3d gaussian  
- **[BloomScene: Lightweight Structured 3D Gaussian Splatting for Crossmodal Scene Generation](https://arxiv.org/abs/2501.10462v1)**  
  Authors: Xiaolu Hou, Mingcheng Li, Dingkang Yang, Jiawei Chen, Ziyun Qian, Xiao Zhao, Yue Jiang, Jinjie Wei, Qingyao Xu, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10462v1.pdf)  
  Keywords: head, lightweight, ar, gaussian splatting, compression, 3d gaussian  
- **[GS-LIVO: Real-Time LiDAR, Inertial, and Visual Multi-sensor Fused Odometry with Gaussian Mapping](https://arxiv.org/abs/2501.08672v1)**  
  Authors: Sheng Hong, Chunran Zheng, Yishu Shen, Changze Li, Fu Zhang, Tong Qin, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08672v1.pdf)  
  Keywords: ar, motion, localization, gaussian splatting, mapping, slam, face, 3d gaussian  
- **[3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering](https://arxiv.org/abs/2501.08370v1)**  
  Authors: Meenakshi Krishnan, Liam Fowl, Ramani Duraiswami  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08370v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, animation, nerf, efficient, face, vr, 3d gaussian  
- **[3DGS-to-PC: Convert a 3D Gaussian Splatting Scene into a Dense Point Cloud or Mesh](https://arxiv.org/abs/2501.07478v1)**  
  Authors: Lewis A G Stuart, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07478v1.pdf)  
  Keywords: ar, 3d reconstruction, gaussian splatting, face, 3d gaussian  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: medical, ar, gaussian splatting, human, sparse view, nerf, dynamic, face, lighting  
- **[RMAvatar: Photorealistic Human Avatar Reconstruction from Monocular Video Based on Rectified Mesh-embedded Gaussians](https://arxiv.org/abs/2501.07104v1)**  
  Authors: Sen Peng, Weixing Xie, Zilong Wang, Xiaohu Guo, Zhonggui Chen, Baorong Yang, Xiao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07104v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rm-avatar.github.io.)  
  Keywords: geometry, avatar, ar, motion, gaussian splatting, deformation, human, face  

### Dynamic Scene

*Showing the latest 50 out of 466 papers*

- **[GSVC: Efficient Video Representation and Compression Through 2D Gaussian Splatting](https://arxiv.org/abs/2501.12060v2)**  
  Authors: Longan Wang, Yuang Shi, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12060v2.pdf)  
  Keywords: ar, motion, gaussian splatting, compression, dynamic, efficient, 3d gaussian  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: ar, gaussian splatting, 4d, semantic, sparse-view, 3d gaussian  
- **[GSTAR: Gaussian Surface Tracking and Reconstruction](https://arxiv.org/abs/2501.10283v2)**  
  Authors: Chengwei Zheng, Lixin Xue, Juan Zarate, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10283v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/GSTAR/.)  
  Keywords: ar, gaussian splatting, tracking, dynamic, efficient, face, 3d gaussian  
- **[GaussianAvatar-Editor: Photorealistic Animatable Gaussian Head Avatar Editor](https://arxiv.org/abs/2501.09978v1)**  
  Authors: Xiangyue Liu, Kunming Luo, Heng Li, Qi Zhang, Yuan Liu, Li Yi, Ping Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.09978v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiangyueliu.github.io/GaussianAvatar-Editor/).)  
  Keywords: head, avatar, ar, motion, 4d, animation, 3d gaussian  
- **[GS-LIVO: Real-Time LiDAR, Inertial, and Visual Multi-sensor Fused Odometry with Gaussian Mapping](https://arxiv.org/abs/2501.08672v1)**  
  Authors: Sheng Hong, Chunran Zheng, Yishu Shen, Changze Li, Fu Zhang, Tong Qin, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08672v1.pdf)  
  Keywords: ar, motion, localization, gaussian splatting, mapping, slam, face, 3d gaussian  
- **[3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering](https://arxiv.org/abs/2501.08370v1)**  
  Authors: Meenakshi Krishnan, Liam Fowl, Ramani Duraiswami  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08370v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, animation, nerf, efficient, face, vr, 3d gaussian  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: outdoor, geometry, ar, localization, gaussian splatting, mapping, slam, nerf, dynamic, large scene  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: medical, ar, gaussian splatting, human, sparse view, nerf, dynamic, face, lighting  
- **[RMAvatar: Photorealistic Human Avatar Reconstruction from Monocular Video Based on Rectified Mesh-embedded Gaussians](https://arxiv.org/abs/2501.07104v1)**  
  Authors: Sen Peng, Weixing Xie, Zilong Wang, Xiaohu Guo, Zhonggui Chen, Baorong Yang, Xiao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07104v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rm-avatar.github.io.)  
  Keywords: geometry, avatar, ar, motion, gaussian splatting, deformation, human, face  
- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: high-fidelity, geometry, 3d reconstruction, ar, motion, gaussian splatting, mapping, slam, nerf, dynamic, efficient, 3d gaussian  

### Few-shot

*Showing the latest 50 out of 91 papers*

- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: ar, gaussian splatting, 4d, semantic, sparse-view, 3d gaussian  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, nerf, efficient, sparse-view, 3d gaussian  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: medical, ar, gaussian splatting, human, sparse view, nerf, dynamic, face, lighting  
- **[Synthetic Prior for Few-Shot Drivable Head Avatar Inversion](https://arxiv.org/abs/2501.06903v1)**  
  Authors: Wojciech Zielonka, Stephan J. Garbin, Alexandros Lattas, George Kopanas, Paulo Gotardo, Thabo Beeler, Justus Thies, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06903v1.pdf)  
  Keywords: head, avatar, ar, gaussian splatting, few-shot, 3d gaussian  
- **[NVS-SQA: Exploring Self-Supervised Quality Representation Learning for Neurally Synthesized Scenes without References](https://arxiv.org/abs/2501.06488v1)**  
  Authors: Qiang Qu, Yiran Shen, Xiaoming Chen, Yuk Ying Chung, Weidong Cai, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06488v1.pdf)  
  Keywords: ar, gaussian splatting, human, sparse view, nerf, 3d gaussian  
- **[FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency](https://arxiv.org/abs/2501.04628v1)**  
  Authors: Han Huang, Yulun Wu, Chao Deng, Ge Gao, Ming Gu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04628v1.pdf)  
  Keywords: ar, gaussian splatting, fast, sparse view, face, sparse-view  
- **[Dust to Tower: Coarse-to-Fine Photo-Realistic Scene Reconstruction from Sparse Uncalibrated Images](https://arxiv.org/abs/2412.19518v1)**  
  Authors: Xudong Cai, Yongcai Wang, Zhaoxin Fan, Deng Haoran, Shuo Wang, Wanting Li, Deying Li, Lun Luo, Minhang Wang, Jintao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19518v1.pdf)  
  Keywords: ar, gaussian splatting, fast, efficient, sparse-view, 3d gaussian  
- **[CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting](https://arxiv.org/abs/2412.19142v1)**  
  Authors: Siyu Jiao, Haoye Dong, Yuyang Yin, Zequn Jie, Yinlong Qian, Yao Zhao, Humphrey Shi, Yunchao Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19142v1.pdf)  
  Keywords: ar, gaussian splatting, few-shot, efficient, 3d gaussian  
- **[SolidGS: Consolidating Gaussian Surfel Splatting for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2412.15400v1)**  
  Authors: Zhuowen Shen, Yuan Liu, Zhang Chen, Zhong Li, Jiepeng Wang, Yongqing Liang, Zhengming Yu, Jingdong Zhang, Yi Xu, Scott Schaefer, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15400v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, sparse view, face, sparse-view  
- **[Improving Geometry in Sparse-View 3DGS via Reprojection-based DoF Separation](https://arxiv.org/abs/2412.14568v1)**  
  Authors: Yongsung Kim, Minjun Park, Jooyoung Choi, Sungroh Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.14568v1.pdf)  
  Keywords: geometry, 3d reconstruction, ar, gaussian splatting, sparse-view, 3d gaussian  

### Geometry Reconstruction

*Showing the latest 50 out of 414 papers*

- **[DARB-Splatting: Generalizing Splatting with Decaying Anisotropic Radial Basis Functions](https://arxiv.org/abs/2501.12369v1)**  
  Authors: Vishagar Arunan, Saeedha Nazar, Hashiru Pramuditha, Vinasirajan Viruthshaan, Sameera Ramasinghe, Simon Lucey, Ranga Rodrigo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12369v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, fast, efficient, 3d gaussian  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, nerf, efficient, sparse-view, 3d gaussian  
- **[Car-GS: Addressing Reflective and Transparent Surface Challenges in 3D Car Reconstruction](https://arxiv.org/abs/2501.11020v1)**  
  Authors: Congcong Li, Jin Wang, Xiaomeng Wang, Xingchen Zhou, Wei Wu, Yuzhi Zhang, Tongyi Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lcc815.github.io/Car-GS.)  
  Keywords: geometry, ar, autonomous driving, reflection, face  
- **[3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering](https://arxiv.org/abs/2501.08370v1)**  
  Authors: Meenakshi Krishnan, Liam Fowl, Ramani Duraiswami  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08370v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, animation, nerf, efficient, face, vr, 3d gaussian  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: outdoor, geometry, ar, localization, gaussian splatting, mapping, slam, nerf, dynamic, large scene  
- **[3DGS-to-PC: Convert a 3D Gaussian Splatting Scene into a Dense Point Cloud or Mesh](https://arxiv.org/abs/2501.07478v1)**  
  Authors: Lewis A G Stuart, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07478v1.pdf)  
  Keywords: ar, 3d reconstruction, gaussian splatting, face, 3d gaussian  
- **[RMAvatar: Photorealistic Human Avatar Reconstruction from Monocular Video Based on Rectified Mesh-embedded Gaussians](https://arxiv.org/abs/2501.07104v1)**  
  Authors: Sen Peng, Weixing Xie, Zilong Wang, Xiaohu Guo, Zhonggui Chen, Baorong Yang, Xiao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07104v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rm-avatar.github.io.)  
  Keywords: geometry, avatar, ar, motion, gaussian splatting, deformation, human, face  
- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: high-fidelity, geometry, 3d reconstruction, ar, motion, gaussian splatting, mapping, slam, nerf, dynamic, efficient, 3d gaussian  
- **[CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications](https://arxiv.org/abs/2501.06927v1)**  
  Authors: Xinyi Zheng, Steve Zhang, Weizhe Lin, Aaron Zhang, Walterio W. Mayol-Cuevas, Junxiao Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06927v1.pdf)  
  Keywords: 3d reconstruction, ar, motion, gaussian splatting, slam, nerf, segmentation  
- **[F3D-Gaus: Feed-forward 3D-aware Generation on ImageNet with Cycle-Consistent Gaussian Splatting](https://arxiv.org/abs/2501.06714v2)**  
  Authors: Yuxin Wang, Qianyi Wu, Dan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06714v2.pdf)  
  Keywords: geometry, gaussian splatting, ar, dynamic  

### Large Scene

*Showing the latest 50 out of 69 papers*

- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: outdoor, ar, gaussian splatting, efficient, 3d gaussian  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: outdoor, geometry, ar, localization, gaussian splatting, mapping, slam, nerf, dynamic, large scene  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: outdoor, understanding, ar, motion, real-time rendering, dynamic, 3d gaussian  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: outdoor, ar, gaussian splatting, mapping, slam, nerf, efficient, 3d gaussian, neural rendering  
- **[WeatherGS: 3D Scene Reconstruction in Adverse Weather Conditions via Gaussian Splatting](https://arxiv.org/abs/2412.18862v2)**  
  Authors: Chenghao Qian, Yuhu Guo, Wenjing Li, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.18862v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/weather-gs.)  
  Keywords: outdoor, ar, 3d reconstruction, gaussian splatting, 3d gaussian  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: high-fidelity, ar, gaussian splatting, compression, fast, nerf, large scene, face, 3d gaussian  
- **[LiHi-GS: LiDAR-Supervised Gaussian Splatting for Highway Driving Scene Reconstruction](https://arxiv.org/abs/2412.15447v2)**  
  Authors: Pou-Chun Kung, Xianling Zhang, Katherine A. Skinner, Nikita Jaipuria  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15447v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/lihi_gs)  
  Keywords: ar, autonomous driving, gaussian splatting, fast, nerf, dynamic, urban scene, 3d gaussian  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: outdoor, geometry, ar, localization, survey, tracking, mapping, slam, reflection, dynamic, face, 3d gaussian, lighting  
- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: head, ar, gaussian splatting, dynamic, large scene, 3d gaussian  
- **[HybridGS: Decoupling Transients and Statics with 2D and 3D Gaussian Splatting](https://arxiv.org/abs/2412.03844v2)**  
  Authors: Jingyu Lin, Jiaqi Gu, Lubin Fan, Bojian Wu, Yujing Lou, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03844v2.pdf)  
  Keywords: outdoor, gaussian splatting, 3d gaussian, ar  

### Model Compression

*Showing the latest 50 out of 465 papers*

- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: outdoor, ar, gaussian splatting, efficient, 3d gaussian  
- **[DARB-Splatting: Generalizing Splatting with Decaying Anisotropic Radial Basis Functions](https://arxiv.org/abs/2501.12369v1)**  
  Authors: Vishagar Arunan, Saeedha Nazar, Hashiru Pramuditha, Vinasirajan Viruthshaan, Sameera Ramasinghe, Simon Lucey, Ranga Rodrigo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12369v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, fast, efficient, 3d gaussian  
- **[HAC++: Towards 100X Compression of 3D Gaussian Splatting](https://arxiv.org/abs/2501.12255v2)**  
  Authors: Yihang Chen, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12255v2.pdf) | [![GitHub](https://img.shields.io/github/stars/YihangChen-ee/HAC-plus?style=social)](https://github.com/YihangChen-ee/HAC-plus)  
  Keywords: ar, gaussian splatting, compression, compact, 3d gaussian  
- **[GSVC: Efficient Video Representation and Compression Through 2D Gaussian Splatting](https://arxiv.org/abs/2501.12060v2)**  
  Authors: Longan Wang, Yuang Shi, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12060v2.pdf)  
  Keywords: ar, motion, gaussian splatting, compression, dynamic, efficient, 3d gaussian  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, nerf, efficient, sparse-view, 3d gaussian  
- **[Decoupling Appearance Variations with 3D Consistent Features in Gaussian Splatting](https://arxiv.org/abs/2501.10788v1)**  
  Authors: Jiaqi Lin, Zhihao Li, Binxiao Huang, Xiao Tang, Jianzhuang Liu, Shiyong Liu, Xiaofei Wu, Fenglong Song, Wenming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10788v1.pdf)  
  Keywords: head, ar, gaussian splatting, real-time rendering, efficient  
- **[GSTAR: Gaussian Surface Tracking and Reconstruction](https://arxiv.org/abs/2501.10283v2)**  
  Authors: Chengwei Zheng, Lixin Xue, Juan Zarate, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10283v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/GSTAR/.)  
  Keywords: ar, gaussian splatting, tracking, dynamic, efficient, face, 3d gaussian  
- **[Creating Virtual Environments with 3D Gaussian Splatting: A Comparative Study](https://arxiv.org/abs/2501.09302v1)**  
  Authors: Shi Qiu, Binzhu Xie, Qixuan Liu, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.09302v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, ar  
- **[BloomScene: Lightweight Structured 3D Gaussian Splatting for Crossmodal Scene Generation](https://arxiv.org/abs/2501.10462v1)**  
  Authors: Xiaolu Hou, Mingcheng Li, Dingkang Yang, Jiawei Chen, Ziyun Qian, Xiao Zhao, Yue Jiang, Jinjie Wei, Qingyao Xu, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10462v1.pdf)  
  Keywords: head, lightweight, ar, gaussian splatting, compression, 3d gaussian  
- **[3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering](https://arxiv.org/abs/2501.08370v1)**  
  Authors: Meenakshi Krishnan, Liam Fowl, Ramani Duraiswami  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08370v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, animation, nerf, efficient, face, vr, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 203 papers*

- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: high-fidelity, geometry, 3d reconstruction, ar, motion, gaussian splatting, mapping, slam, nerf, dynamic, efficient, 3d gaussian  
- **[Gaussian Masked Autoencoders](https://arxiv.org/abs/2501.03229v1)**  
  Authors: Jathushan Rajasegaran, Xinlei Chen, Rulilong Li, Christoph Feichtenhofer, Jitendra Malik, Shiry Ginosar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.03229v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://brjathu.github.io/gmae)  
  Keywords: high-fidelity, understanding, ar, gaussian splatting, semantic, 3d gaussian, segmentation  
- **[Deformable Gaussian Splatting for Efficient and High-Fidelity Reconstruction of Surgical Scenes](https://arxiv.org/abs/2501.01101v1)**  
  Authors: Jiwei Shan, Zeyu Cai, Cheng-Tai Hsieh, Shing Shin Cheng, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01101v1.pdf)  
  Keywords: high-fidelity, ar, motion, gaussian splatting, deformation, dynamic, efficient, 3d gaussian  
- **[ActiveGS: Active Scene Reconstruction using Gaussian Splatting](https://arxiv.org/abs/2412.17769v1)**  
  Authors: Liren Jin, Xingguang Zhong, Yue Pan, Jens Behley, Cyrill Stachniss, Marija Popović  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17769v1.pdf)  
  Keywords: high-fidelity, robotics, gaussian splatting, ar  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: high-fidelity, ar, gaussian splatting, compression, fast, nerf, large scene, face, 3d gaussian  
- **[SqueezeMe: Efficient Gaussian Avatars for VR](https://arxiv.org/abs/2412.15171v2)**  
  Authors: Shunsuke Saito, Stanislav Pidhorskyi, Igor Santesteban, Forrest Iandola, Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Frank Yu, Emanuel Garbin, Tomas Simon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15171v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://forresti.github.io/squeezeme.)  
  Keywords: head, avatar, ar, motion, gaussian splatting, human, efficient, high quality, vr  
- **[HyperGS: Hyperspectral 3D Gaussian Splatting](https://arxiv.org/abs/2412.12849v1)**  
  Authors: Christopher Thirgood, Oscar Mendez, Erin Chao Ling, Jon Storey, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12849v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, 4d, 3d gaussian  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: high-fidelity, ray tracing, lighting, ar, gaussian splatting, real-time rendering, reflection, efficient, 3d gaussian  
- **[Deformable Radial Kernel Splatting](https://arxiv.org/abs/2412.11752v1)**  
  Authors: Yi-Hua Huang, Ming-Xian Lin, Yang-Tian Sun, Ziyi Yang, Xiaoyang Lyu, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11752v1.pdf)  
  Keywords: high-fidelity, geometry, ar, gaussian splatting, efficient  
- **[SweepEvGS: Event-Based 3D Gaussian Splatting for Macro and Micro Radiance Field Rendering from a Single Sweep](https://arxiv.org/abs/2412.11579v1)**  
  Authors: Jingqian Wu, Shuo Zhu, Chutian Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11579v1.pdf)  
  Keywords: high-fidelity, ar, motion, gaussian splatting, dynamic, efficient, 3d gaussian, lighting  

### Ray Tracing

- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: ray tracing, ar, gaussian splatting, relighting, reflection, efficient, lighting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: high-fidelity, ray tracing, lighting, ar, gaussian splatting, real-time rendering, reflection, efficient, 3d gaussian  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: geometry, illumination, global illumination, ar, gaussian splatting, fast, mapping, nerf, efficient, face  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v1.pdf)  
  Keywords: ray tracing, ar, gaussian splatting, efficient, 3d gaussian  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: ray tracing, gaussian splatting, 3d gaussian, ar  
- **[URAvatar: Universal Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2410.24223v1)**  
  Authors: Junxuan Li, Chen Cao, Gabriel Schwartz, Rawal Khirodkar, Christian Richardt, Tomas Simon, Yaser Sheikh, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24223v1.pdf)  
  Keywords: head, avatar, illumination, global illumination, ar, human, real-time rendering, light transport, efficient, 3d gaussian, relightable  
- **[Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization](https://arxiv.org/abs/2410.16978v1)**  
  Authors: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, Ralf Gutjahr, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16978v1.pdf)  
  Keywords: understanding, head, medical, ar, gaussian splatting, path tracing, efficient, vr  
- **[GS^3: Efficient Relighting with Triple Gaussian Splatting](https://arxiv.org/abs/2410.11419v1)**  
  Authors: Zoubin Bi, Yixin Zeng, Chong Zeng, Fan Pei, Xiang Feng, Kun Zhou, Hongzhi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11419v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://GSrelight.github.io/.)  
  Keywords: shadow, geometry, illumination, global illumination, ar, gaussian splatting, relighting, efficient, lighting  
- **[RGM: Reconstructing High-fidelity 3D Car Assets with Relightable 3D-GS Generative Model from a Single Image](https://arxiv.org/abs/2410.08181v1)**  
  Authors: Xiaoxue Chen, Jv Zheng, Hao Huang, Haoran Xu, Weihao Gu, Kangliang Chen, He xiang, Huan-ang Gao, Hao Zhao, Guyue Zhou, Yaqin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08181v1.pdf)  
  Keywords: high-fidelity, relightable, geometry, lighting, illumination, global illumination, ar, autonomous driving, relighting, nerf, 3d gaussian  
- **[6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering](https://arxiv.org/abs/2410.04974v2)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04974v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/6dgs/)  
  Keywords: ray tracing, ar, gaussian splatting, real-time rendering, nerf, high quality, 3d gaussian  

### Relighting

*Showing the latest 50 out of 136 papers*

- **[Car-GS: Addressing Reflective and Transparent Surface Challenges in 3D Car Reconstruction](https://arxiv.org/abs/2501.11020v1)**  
  Authors: Congcong Li, Jin Wang, Xiaomeng Wang, Xingchen Zhou, Wei Wu, Yuzhi Zhang, Tongyi Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lcc815.github.io/Car-GS.)  
  Keywords: geometry, ar, autonomous driving, reflection, face  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: medical, ar, gaussian splatting, human, sparse view, nerf, dynamic, face, lighting  
- **[Reflective Gaussian Splatting](https://arxiv.org/abs/2412.19282v1)**  
  Authors: Yuxuan Yao, Zixuan Zeng, Chun Gu, Xiatian Zhu, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19282v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, relighting, nerf, reflection, lighting  
- **[Generating Editable Head Avatars with 3D Gaussian GANs](https://arxiv.org/abs/2412.19149v1)**  
  Authors: Guohao Li, Hongyu Yang, Yifang Men, Di Huang, Weixin Li, Ruijie Yang, Yunhong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19149v1.pdf) | [![GitHub](https://img.shields.io/github/stars/liguohao96/EGG3D?style=social)](https://github.com/liguohao96/EGG3D)  
  Keywords: head, avatar, illumination, ar, gaussian splatting, deformation, animation, nerf, face, 3d gaussian  
- **[FaceLift: Single Image to 3D Head with View Generation and GS-LRM](https://arxiv.org/abs/2412.17812v1)**  
  Authors: Weijie Lyu, Yi Zhou, Ming-Hsuan Yang, Zhixin Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17812v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weijielyu.github.io/FaceLift.)  
  Keywords: head, ar, 4d, human, animation, face, lighting  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: ray tracing, ar, gaussian splatting, relighting, reflection, efficient, lighting  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: outdoor, geometry, ar, localization, survey, tracking, mapping, slam, reflection, dynamic, face, 3d gaussian, lighting  
- **[EOGS: Gaussian Splatting for Earth Observation](https://arxiv.org/abs/2412.13047v1)**  
  Authors: Luca Savant Aira, Gabriele Facciolo, Thibaud Ehret  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13047v1.pdf)  
  Keywords: shadow, gaussian splatting, nerf, ar  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: high-fidelity, ray tracing, lighting, ar, gaussian splatting, real-time rendering, reflection, efficient, 3d gaussian  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: geometry, illumination, global illumination, ar, gaussian splatting, fast, mapping, nerf, efficient, face  

### SLAM

*Showing the latest 50 out of 182 papers*

- **[GSTAR: Gaussian Surface Tracking and Reconstruction](https://arxiv.org/abs/2501.10283v2)**  
  Authors: Chengwei Zheng, Lixin Xue, Juan Zarate, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10283v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/GSTAR/.)  
  Keywords: ar, gaussian splatting, tracking, dynamic, efficient, face, 3d gaussian  
- **[CityLoc: 6 DoF Localization of Text Descriptions in Large-Scale Scenes with Gaussian Representation](https://arxiv.org/abs/2501.08982v1)**  
  Authors: Qi Ma, Runyi Yang, Bin Ren, Ender Konukoglu, Luc Van Gool, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08982v1.pdf)  
  Keywords: localization, gaussian splatting, 3d gaussian, ar  
- **[GS-LIVO: Real-Time LiDAR, Inertial, and Visual Multi-sensor Fused Odometry with Gaussian Mapping](https://arxiv.org/abs/2501.08672v1)**  
  Authors: Sheng Hong, Chunran Zheng, Yishu Shen, Changze Li, Fu Zhang, Tong Qin, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08672v1.pdf)  
  Keywords: ar, motion, localization, gaussian splatting, mapping, slam, face, 3d gaussian  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: outdoor, geometry, ar, localization, gaussian splatting, mapping, slam, nerf, dynamic, large scene  
- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: high-fidelity, geometry, 3d reconstruction, ar, motion, gaussian splatting, mapping, slam, nerf, dynamic, efficient, 3d gaussian  
- **[CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications](https://arxiv.org/abs/2501.06927v1)**  
  Authors: Xinyi Zheng, Steve Zhang, Weizhe Lin, Aaron Zhang, Walterio W. Mayol-Cuevas, Junxiao Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06927v1.pdf)  
  Keywords: 3d reconstruction, ar, motion, gaussian splatting, slam, nerf, segmentation  
- **[ActiveGAMER: Active GAussian Mapping through Efficient Rendering](https://arxiv.org/abs/2501.06897v1)**  
  Authors: Liyan Chen, Huangying Zhan, Kevin Chen, Xiangyu Xu, Qingan Yan, Changjiang Cai, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06897v1.pdf)  
  Keywords: efficient rendering, ar, gaussian splatting, mapping, nerf, dynamic, efficient, 3d gaussian  
- **[MapGS: Generalizable Pretraining and Data Augmentation for Online Mapping via Novel View Synthesis](https://arxiv.org/abs/2501.06660v1)**  
  Authors: Hengyuan Zhang, David Paz, Yuliang Guo, Xinyu Huang, Henrik I. Christensen, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06660v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://henryzhangzhy.github.io/mapgs.)  
  Keywords: ar, gaussian splatting, fast, mapping, efficient  
- **[Scaffold-SLAM: Structured 3D Gaussians for Simultaneous Localization and Photorealistic Mapping](https://arxiv.org/abs/2501.05242v1)**  
  Authors: Wen Tianci, Liu Zhiang, Lu Biao, Fang Yongchun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.05242v1.pdf)  
  Keywords: ar, motion, localization, gaussian splatting, mapping, slam, 3d gaussian  
- **[GS-DiT: Advancing Video Generation with Pseudo 4D Gaussian Fields through Efficient Dense 3D Point Tracking](https://arxiv.org/abs/2501.02690v1)**  
  Authors: Weikang Bian, Zhaoyang Huang, Xiaoyu Shi, Yijin Li, Fu-Yun Wang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.02690v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wkbian.github.io/Projects/GS-DiT/.)  
  Keywords: ar, motion, gaussian splatting, 4d, tracking, dynamic, efficient  

### Scene Understanding

*Showing the latest 50 out of 217 papers*

- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: ar, gaussian splatting, 4d, semantic, sparse-view, 3d gaussian  
- **[CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications](https://arxiv.org/abs/2501.06927v1)**  
  Authors: Xinyi Zheng, Steve Zhang, Weizhe Lin, Aaron Zhang, Walterio W. Mayol-Cuevas, Junxiao Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06927v1.pdf)  
  Keywords: 3d reconstruction, ar, motion, gaussian splatting, slam, nerf, segmentation  
- **[Gaussian Masked Autoencoders](https://arxiv.org/abs/2501.03229v1)**  
  Authors: Jathushan Rajasegaran, Xinlei Chen, Rulilong Li, Christoph Feichtenhofer, Jitendra Malik, Shiry Ginosar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.03229v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://brjathu.github.io/gmae)  
  Keywords: high-fidelity, understanding, ar, gaussian splatting, semantic, 3d gaussian, segmentation  
- **[HOGSA: Bimanual Hand-Object Interaction Understanding with 3D Gaussian Splatting Based Data Augmentation](https://arxiv.org/abs/2501.02845v1)**  
  Authors: Wentian Qu, Jiahe Li, Jian Cheng, Jian Shi, Chenyu Meng, Cuixia Ma, Hongan Wang, Xiaoming Deng, Yinda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.02845v1.pdf)  
  Keywords: understanding, ar, motion, gaussian splatting, robotics, 3d gaussian  
- **[PG-SAG: Parallel Gaussian Splatting for Fine-Grained Large-Scale Urban Buildings Reconstruction via Semantic-Aware Grouping](https://arxiv.org/abs/2501.01677v1)**  
  Authors: Tengfei Wang, Xin Wang, Yongmao Hou, Yiwei Xu, Wendi Zhang, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01677v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TFWang-9527/PG-SAG?style=social)](https://github.com/TFWang-9527/PG-SAG)  
  Keywords: ar, gaussian splatting, semantic, face, 3d gaussian  
- **[Leverage Cross-Attention for End-to-End Open-Vocabulary Panoptic Reconstruction](https://arxiv.org/abs/2501.01119v1)**  
  Authors: Xuan Yu, Yuxuan Xie, Yili Liu, Haojian Lu, Rong Xiong, Yiyi Liao, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01119v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuxuan1206.github.io/panopticrecon_pp/)  
  Keywords: understanding, head, ar, semantic, dynamic, robotics, 3d gaussian, segmentation  
- **[Gaussian Building Mesh (GBM): Extract a Building's 3D Mesh with Google Earth and Gaussian Splatting](https://arxiv.org/abs/2501.00625v2)**  
  Authors: Kyle Gao, Liangzhi Li, Hongjie He, Dening Lu, Linlin Xu, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00625v2.pdf)  
  Keywords: geometry, gaussian splatting, segmentation, ar  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: outdoor, understanding, ar, motion, real-time rendering, dynamic, 3d gaussian  
- **[PanoSLAM: Panoptic 3D Scene Reconstruction via Gaussian SLAM](https://arxiv.org/abs/2501.00352v1)**  
  Authors: Runnan Chen, Zhaoqing Wang, Jiepeng Wang, Yuexin Ma, Mingming Gong, Wenping Wang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00352v1.pdf) | [![GitHub](https://img.shields.io/github/stars/runnanchen/PanoSLAM?style=social)](https://github.com/runnanchen/PanoSLAM)  
  Keywords: understanding, efficient rendering, 3d reconstruction, ar, localization, gaussian splatting, semantic, tracking, mapping, slam, efficient, robotics, 3d gaussian, segmentation  
- **[OVGaussian: Generalizable 3D Gaussian Segmentation with Open Vocabularies](https://arxiv.org/abs/2501.00326v1)**  
  Authors: Runnan Chen, Xiangyu Sun, Zhaoqing Wang, Youquan Liu, Jiepeng Wang, Lingdong Kong, Jiankang Deng, Mingming Gong, Liang Pan, Wenping Wang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00326v1.pdf) | [![GitHub](https://img.shields.io/github/stars/runnanchen/OVGaussian?style=social)](https://github.com/runnanchen/OVGaussian)  
  Keywords: understanding, ar, semantic, 3d gaussian, segmentation  



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