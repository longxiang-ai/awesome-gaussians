# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-01-25 00:43:30

## Categories

- [3DGS Surveys](#3dgs-surveys) (20 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (362 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1256 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (418 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (467 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (91 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (415 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (69 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (466 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (204 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (28 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (136 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (184 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (218 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: 3d gaussian, face, dynamic, slam, localization, ar, lighting, reflection, mapping, tracking, outdoor, geometry, survey  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: 3d gaussian, illumination, gaussian splatting, ar, recognition, survey  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: high-fidelity, robotics, compact, nerf, gaussian splatting, 3d reconstruction, dynamic, autonomous driving, lighting, ar, semantic, geometry, survey  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: 3d gaussian, robotics, understanding, nerf, gaussian splatting, ar, real-time rendering, survey  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, nerf, gaussian splatting, ar, lighting, survey  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: 3d gaussian, robotics, vr, nerf, gaussian splatting, 3d reconstruction, ar, autonomous driving, survey  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: 3d gaussian, ar, survey  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v2)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v2.pdf)  
  Keywords: 3d gaussian, understanding, gaussian splatting, ar, real-time rendering, efficient, survey  
- **[Survey on Fundamental Deep Learning 3D Reconstruction Techniques](https://arxiv.org/abs/2407.08137v1)**  
  Authors: Yonge Bai, LikHang Wong, TszYin Twan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.08137v1.pdf)  
  Keywords: 3d gaussian, nerf, gaussian splatting, 3d reconstruction, ar, lighting, survey  
- **[Panopticon: a telescope for our times](https://arxiv.org/abs/2407.05103v2)**  
  Authors: Will Saunders, Timothy Chin, Michael Goodwin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05103v2.pdf)  
  Keywords: ar, survey  

### Acceleration

*Showing the latest 50 out of 362 papers*

- **[Deblur-Avatar: Animatable Avatars from Motion-Blurred Monocular Videos](https://arxiv.org/abs/2501.13335v1)**  
  Authors: Xianrui Luo, Juewen Peng, Zhongang Cai, Lei Yang, Fan Yang, Zhiguo Cao, Guosheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13335v1.pdf)  
  Keywords: 3d gaussian, human, high-fidelity, dynamic, gaussian splatting, motion, body, ar, avatar, real-time rendering  
- **[DARB-Splatting: Generalizing Splatting with Decaying Anisotropic Radial Basis Functions](https://arxiv.org/abs/2501.12369v1)**  
  Authors: Vishagar Arunan, Saeedha Nazar, Hashiru Pramuditha, Vinasirajan Viruthshaan, Sameera Ramasinghe, Simon Lucey, Ranga Rodrigo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12369v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, 3d reconstruction, ar, efficient  
- **[Decoupling Appearance Variations with 3D Consistent Features in Gaussian Splatting](https://arxiv.org/abs/2501.10788v1)**  
  Authors: Jiaqi Lin, Zhihao Li, Binxiao Huang, Xiao Tang, Jianzhuang Liu, Shiyong Liu, Xiaofei Wu, Fenglong Song, Wenming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10788v1.pdf)  
  Keywords: gaussian splatting, ar, head, real-time rendering, efficient  
- **[Object-Centric 2D Gaussian Splatting: Background Removal and Occlusion-Aware Pruning for Compact Object Models](https://arxiv.org/abs/2501.08174v1)**  
  Authors: Marcel Rogge, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08174v1.pdf)  
  Keywords: compact, gaussian splatting, ar, fast  
- **[ActiveGAMER: Active GAussian Mapping through Efficient Rendering](https://arxiv.org/abs/2501.06897v1)**  
  Authors: Liyan Chen, Huangying Zhan, Kevin Chen, Xiangyu Xu, Qingan Yan, Changjiang Cai, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06897v1.pdf)  
  Keywords: 3d gaussian, efficient rendering, dynamic, gaussian splatting, nerf, ar, mapping, efficient  
- **[MapGS: Generalizable Pretraining and Data Augmentation for Online Mapping via Novel View Synthesis](https://arxiv.org/abs/2501.06660v1)**  
  Authors: Hengyuan Zhang, David Paz, Yuliang Guo, Xinyu Huang, Henrik I. Christensen, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06660v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://henryzhangzhy.github.io/mapgs.)  
  Keywords: fast, gaussian splatting, ar, mapping, efficient  
- **[Locality-aware Gaussian Compression for Fast and High-quality Rendering](https://arxiv.org/abs/2501.05757v1)**  
  Authors: Seungjoo Shin, Jaesik Park, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.05757v1.pdf)  
  Keywords: 3d gaussian, compression, fast, compact, gaussian splatting, ar  
- **[FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency](https://arxiv.org/abs/2501.04628v1)**  
  Authors: Han Huang, Yulun Wu, Chao Deng, Ge Gao, Ming Gu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04628v1.pdf)  
  Keywords: face, fast, gaussian splatting, ar, sparse-view, sparse view  
- **[CrossView-GS: Cross-view Gaussian Splatting For Large-scale Scene Reconstruction](https://arxiv.org/abs/2501.01695v1)**  
  Authors: Chenhao Zhang, Yuanping Cao, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01695v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, real-time rendering, ar  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: 3d gaussian, understanding, dynamic, motion, ar, real-time rendering, outdoor  

### Applications

*Showing the latest 50 out of 1256 papers*

- **[GoDe: Gaussians on Demand for Progressive Level of Detail and Scalable Compression](https://arxiv.org/abs/2501.13558v1)**  
  Authors: Francesco Di Sario, Riccardo Renzulli, Marco Grangetto, Akihiro Sugimoto, Enzo Tartaglione  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13558v1.pdf)  
  Keywords: 3d gaussian, compression, vr, gaussian splatting, ar  
- **[MultiDreamer3D: Multi-concept 3D Customization with Concept-Aware Diffusion Guidance](https://arxiv.org/abs/2501.13449v1)**  
  Authors: Wooseok Song, Seunggyu Chang, Jaejun Yoo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13449v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar  
- **[GeomGS: LiDAR-Guided Geometry-Aware Gaussian Splatting for Robot Localization](https://arxiv.org/abs/2501.13417v1)**  
  Authors: Jaewon Lee, Mangyu Kong, Minseong Park, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13417v1.pdf)  
  Keywords: 3d gaussian, robotics, understanding, gaussian splatting, autonomous driving, ar, mapping, geometry, localization  
- **[VIGS SLAM: IMU-based Large-Scale 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2501.13402v1)**  
  Authors: Gyuhyeon Pak, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13402v1.pdf)  
  Keywords: 3d gaussian, slam, gaussian splatting, nerf, ar, mapping, tracking  
- **[Deblur-Avatar: Animatable Avatars from Motion-Blurred Monocular Videos](https://arxiv.org/abs/2501.13335v1)**  
  Authors: Xianrui Luo, Juewen Peng, Zhongang Cai, Lei Yang, Fan Yang, Zhiguo Cao, Guosheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13335v1.pdf)  
  Keywords: 3d gaussian, human, high-fidelity, dynamic, gaussian splatting, motion, body, ar, avatar, real-time rendering  
- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, outdoor, efficient  
- **[DARB-Splatting: Generalizing Splatting with Decaying Anisotropic Radial Basis Functions](https://arxiv.org/abs/2501.12369v1)**  
  Authors: Vishagar Arunan, Saeedha Nazar, Hashiru Pramuditha, Vinasirajan Viruthshaan, Sameera Ramasinghe, Simon Lucey, Ranga Rodrigo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12369v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, 3d reconstruction, ar, efficient  
- **[HAC++: Towards 100X Compression of 3D Gaussian Splatting](https://arxiv.org/abs/2501.12255v2)**  
  Authors: Yihang Chen, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12255v2.pdf) | [![GitHub](https://img.shields.io/github/stars/YihangChen-ee/HAC-plus?style=social)](https://github.com/YihangChen-ee/HAC-plus)  
  Keywords: 3d gaussian, compression, compact, gaussian splatting, ar  
- **[GSVC: Efficient Video Representation and Compression Through 2D Gaussian Splatting](https://arxiv.org/abs/2501.12060v2)**  
  Authors: Longan Wang, Yuang Shi, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12060v2.pdf)  
  Keywords: 3d gaussian, compression, dynamic, gaussian splatting, motion, ar, efficient  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: 3d gaussian, 4d, gaussian splatting, ar, sparse-view, semantic  

### Avatar Generation

*Showing the latest 50 out of 418 papers*

- **[Deblur-Avatar: Animatable Avatars from Motion-Blurred Monocular Videos](https://arxiv.org/abs/2501.13335v1)**  
  Authors: Xianrui Luo, Juewen Peng, Zhongang Cai, Lei Yang, Fan Yang, Zhiguo Cao, Guosheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13335v1.pdf)  
  Keywords: 3d gaussian, human, high-fidelity, dynamic, gaussian splatting, motion, body, ar, avatar, real-time rendering  
- **[Car-GS: Addressing Reflective and Transparent Surface Challenges in 3D Car Reconstruction](https://arxiv.org/abs/2501.11020v1)**  
  Authors: Congcong Li, Jin Wang, Xiaomeng Wang, Xingchen Zhou, Wei Wu, Yuzhi Zhang, Tongyi Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lcc815.github.io/Car-GS.)  
  Keywords: face, geometry, ar, reflection, autonomous driving  
- **[Decoupling Appearance Variations with 3D Consistent Features in Gaussian Splatting](https://arxiv.org/abs/2501.10788v1)**  
  Authors: Jiaqi Lin, Zhihao Li, Binxiao Huang, Xiao Tang, Jianzhuang Liu, Shiyong Liu, Xiaofei Wu, Fenglong Song, Wenming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10788v1.pdf)  
  Keywords: gaussian splatting, ar, head, real-time rendering, efficient  
- **[GSTAR: Gaussian Surface Tracking and Reconstruction](https://arxiv.org/abs/2501.10283v2)**  
  Authors: Chengwei Zheng, Lixin Xue, Juan Zarate, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10283v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/GSTAR/.)  
  Keywords: 3d gaussian, face, dynamic, gaussian splatting, ar, tracking, efficient  
- **[GaussianAvatar-Editor: Photorealistic Animatable Gaussian Head Avatar Editor](https://arxiv.org/abs/2501.09978v1)**  
  Authors: Xiangyue Liu, Kunming Luo, Heng Li, Qi Zhang, Yuan Liu, Li Yi, Ping Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.09978v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiangyueliu.github.io/GaussianAvatar-Editor/).)  
  Keywords: 3d gaussian, 4d, motion, ar, head, avatar, animation  
- **[BloomScene: Lightweight Structured 3D Gaussian Splatting for Crossmodal Scene Generation](https://arxiv.org/abs/2501.10462v1)**  
  Authors: Xiaolu Hou, Mingcheng Li, Dingkang Yang, Jiawei Chen, Ziyun Qian, Xiao Zhao, Yue Jiang, Jinjie Wei, Qingyao Xu, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10462v1.pdf)  
  Keywords: lightweight, 3d gaussian, compression, gaussian splatting, ar, head  
- **[GS-LIVO: Real-Time LiDAR, Inertial, and Visual Multi-sensor Fused Odometry with Gaussian Mapping](https://arxiv.org/abs/2501.08672v1)**  
  Authors: Sheng Hong, Chunran Zheng, Yishu Shen, Changze Li, Fu Zhang, Tong Qin, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08672v1.pdf)  
  Keywords: 3d gaussian, face, slam, gaussian splatting, motion, ar, mapping, localization  
- **[3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering](https://arxiv.org/abs/2501.08370v1)**  
  Authors: Meenakshi Krishnan, Liam Fowl, Ramani Duraiswami  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08370v1.pdf)  
  Keywords: 3d gaussian, face, vr, nerf, gaussian splatting, ar, animation, geometry, efficient  
- **[3DGS-to-PC: Convert a 3D Gaussian Splatting Scene into a Dense Point Cloud or Mesh](https://arxiv.org/abs/2501.07478v1)**  
  Authors: Lewis A G Stuart, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07478v1.pdf)  
  Keywords: 3d gaussian, face, gaussian splatting, 3d reconstruction, ar  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: human, face, dynamic, nerf, gaussian splatting, medical, ar, lighting, sparse view  

### Dynamic Scene

*Showing the latest 50 out of 467 papers*

- **[Deblur-Avatar: Animatable Avatars from Motion-Blurred Monocular Videos](https://arxiv.org/abs/2501.13335v1)**  
  Authors: Xianrui Luo, Juewen Peng, Zhongang Cai, Lei Yang, Fan Yang, Zhiguo Cao, Guosheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13335v1.pdf)  
  Keywords: 3d gaussian, human, high-fidelity, dynamic, gaussian splatting, motion, body, ar, avatar, real-time rendering  
- **[GSVC: Efficient Video Representation and Compression Through 2D Gaussian Splatting](https://arxiv.org/abs/2501.12060v2)**  
  Authors: Longan Wang, Yuang Shi, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12060v2.pdf)  
  Keywords: 3d gaussian, compression, dynamic, gaussian splatting, motion, ar, efficient  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: 3d gaussian, 4d, gaussian splatting, ar, sparse-view, semantic  
- **[GSTAR: Gaussian Surface Tracking and Reconstruction](https://arxiv.org/abs/2501.10283v2)**  
  Authors: Chengwei Zheng, Lixin Xue, Juan Zarate, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10283v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/GSTAR/.)  
  Keywords: 3d gaussian, face, dynamic, gaussian splatting, ar, tracking, efficient  
- **[GaussianAvatar-Editor: Photorealistic Animatable Gaussian Head Avatar Editor](https://arxiv.org/abs/2501.09978v1)**  
  Authors: Xiangyue Liu, Kunming Luo, Heng Li, Qi Zhang, Yuan Liu, Li Yi, Ping Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.09978v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiangyueliu.github.io/GaussianAvatar-Editor/).)  
  Keywords: 3d gaussian, 4d, motion, ar, head, avatar, animation  
- **[GS-LIVO: Real-Time LiDAR, Inertial, and Visual Multi-sensor Fused Odometry with Gaussian Mapping](https://arxiv.org/abs/2501.08672v1)**  
  Authors: Sheng Hong, Chunran Zheng, Yishu Shen, Changze Li, Fu Zhang, Tong Qin, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08672v1.pdf)  
  Keywords: 3d gaussian, face, slam, gaussian splatting, motion, ar, mapping, localization  
- **[3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering](https://arxiv.org/abs/2501.08370v1)**  
  Authors: Meenakshi Krishnan, Liam Fowl, Ramani Duraiswami  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08370v1.pdf)  
  Keywords: 3d gaussian, face, vr, nerf, gaussian splatting, ar, animation, geometry, efficient  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: large scene, dynamic, nerf, gaussian splatting, slam, ar, mapping, outdoor, geometry, localization  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: human, face, dynamic, nerf, gaussian splatting, medical, ar, lighting, sparse view  
- **[RMAvatar: Photorealistic Human Avatar Reconstruction from Monocular Video Based on Rectified Mesh-embedded Gaussians](https://arxiv.org/abs/2501.07104v1)**  
  Authors: Sen Peng, Weixing Xie, Zilong Wang, Xiaohu Guo, Zhonggui Chen, Baorong Yang, Xiao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07104v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rm-avatar.github.io.)  
  Keywords: human, face, gaussian splatting, motion, ar, avatar, deformation, geometry  

### Few-shot

*Showing the latest 50 out of 91 papers*

- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: 3d gaussian, 4d, gaussian splatting, ar, sparse-view, semantic  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: 3d gaussian, nerf, gaussian splatting, 3d reconstruction, ar, sparse-view, efficient  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: human, face, dynamic, nerf, gaussian splatting, medical, ar, lighting, sparse view  
- **[Synthetic Prior for Few-Shot Drivable Head Avatar Inversion](https://arxiv.org/abs/2501.06903v1)**  
  Authors: Wojciech Zielonka, Stephan J. Garbin, Alexandros Lattas, George Kopanas, Paulo Gotardo, Thabo Beeler, Justus Thies, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06903v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, few-shot, ar, head, avatar  
- **[NVS-SQA: Exploring Self-Supervised Quality Representation Learning for Neurally Synthesized Scenes without References](https://arxiv.org/abs/2501.06488v1)**  
  Authors: Qiang Qu, Yiran Shen, Xiaoming Chen, Yuk Ying Chung, Weidong Cai, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06488v1.pdf)  
  Keywords: 3d gaussian, human, nerf, gaussian splatting, ar, sparse view  
- **[FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency](https://arxiv.org/abs/2501.04628v1)**  
  Authors: Han Huang, Yulun Wu, Chao Deng, Ge Gao, Ming Gu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04628v1.pdf)  
  Keywords: face, fast, gaussian splatting, ar, sparse-view, sparse view  
- **[Dust to Tower: Coarse-to-Fine Photo-Realistic Scene Reconstruction from Sparse Uncalibrated Images](https://arxiv.org/abs/2412.19518v1)**  
  Authors: Xudong Cai, Yongcai Wang, Zhaoxin Fan, Deng Haoran, Shuo Wang, Wanting Li, Deying Li, Lun Luo, Minhang Wang, Jintao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19518v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, ar, sparse-view, efficient  
- **[CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting](https://arxiv.org/abs/2412.19142v1)**  
  Authors: Siyu Jiao, Haoye Dong, Yuyang Yin, Zequn Jie, Yinlong Qian, Yao Zhao, Humphrey Shi, Yunchao Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19142v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, few-shot, efficient  
- **[SolidGS: Consolidating Gaussian Surfel Splatting for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2412.15400v1)**  
  Authors: Zhuowen Shen, Yuan Liu, Zhang Chen, Zhong Li, Jiepeng Wang, Yongqing Liang, Zhengming Yu, Jingdong Zhang, Yi Xu, Scott Schaefer, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15400v1.pdf)  
  Keywords: face, gaussian splatting, ar, sparse-view, sparse view, geometry  
- **[Improving Geometry in Sparse-View 3DGS via Reprojection-based DoF Separation](https://arxiv.org/abs/2412.14568v1)**  
  Authors: Yongsung Kim, Minjun Park, Jooyoung Choi, Sungroh Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.14568v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, 3d reconstruction, ar, sparse-view, geometry  

### Geometry Reconstruction

*Showing the latest 50 out of 415 papers*

- **[GeomGS: LiDAR-Guided Geometry-Aware Gaussian Splatting for Robot Localization](https://arxiv.org/abs/2501.13417v1)**  
  Authors: Jaewon Lee, Mangyu Kong, Minseong Park, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13417v1.pdf)  
  Keywords: 3d gaussian, robotics, understanding, gaussian splatting, autonomous driving, ar, mapping, geometry, localization  
- **[DARB-Splatting: Generalizing Splatting with Decaying Anisotropic Radial Basis Functions](https://arxiv.org/abs/2501.12369v1)**  
  Authors: Vishagar Arunan, Saeedha Nazar, Hashiru Pramuditha, Vinasirajan Viruthshaan, Sameera Ramasinghe, Simon Lucey, Ranga Rodrigo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12369v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, 3d reconstruction, ar, efficient  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: 3d gaussian, nerf, gaussian splatting, 3d reconstruction, ar, sparse-view, efficient  
- **[Car-GS: Addressing Reflective and Transparent Surface Challenges in 3D Car Reconstruction](https://arxiv.org/abs/2501.11020v1)**  
  Authors: Congcong Li, Jin Wang, Xiaomeng Wang, Xingchen Zhou, Wei Wu, Yuzhi Zhang, Tongyi Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lcc815.github.io/Car-GS.)  
  Keywords: face, geometry, ar, reflection, autonomous driving  
- **[3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering](https://arxiv.org/abs/2501.08370v1)**  
  Authors: Meenakshi Krishnan, Liam Fowl, Ramani Duraiswami  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08370v1.pdf)  
  Keywords: 3d gaussian, face, vr, nerf, gaussian splatting, ar, animation, geometry, efficient  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: large scene, dynamic, nerf, gaussian splatting, slam, ar, mapping, outdoor, geometry, localization  
- **[3DGS-to-PC: Convert a 3D Gaussian Splatting Scene into a Dense Point Cloud or Mesh](https://arxiv.org/abs/2501.07478v1)**  
  Authors: Lewis A G Stuart, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07478v1.pdf)  
  Keywords: 3d gaussian, face, gaussian splatting, 3d reconstruction, ar  
- **[RMAvatar: Photorealistic Human Avatar Reconstruction from Monocular Video Based on Rectified Mesh-embedded Gaussians](https://arxiv.org/abs/2501.07104v1)**  
  Authors: Sen Peng, Weixing Xie, Zilong Wang, Xiaohu Guo, Zhonggui Chen, Baorong Yang, Xiao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07104v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rm-avatar.github.io.)  
  Keywords: human, face, gaussian splatting, motion, ar, avatar, deformation, geometry  
- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: 3d gaussian, high-fidelity, nerf, gaussian splatting, 3d reconstruction, dynamic, motion, slam, ar, mapping, geometry, efficient  
- **[CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications](https://arxiv.org/abs/2501.06927v1)**  
  Authors: Xinyi Zheng, Steve Zhang, Weizhe Lin, Aaron Zhang, Walterio W. Mayol-Cuevas, Junxiao Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06927v1.pdf)  
  Keywords: nerf, gaussian splatting, 3d reconstruction, motion, segmentation, slam, ar  

### Large Scene

*Showing the latest 50 out of 69 papers*

- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, outdoor, efficient  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: large scene, dynamic, nerf, gaussian splatting, slam, ar, mapping, outdoor, geometry, localization  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: 3d gaussian, understanding, dynamic, motion, ar, real-time rendering, outdoor  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: 3d gaussian, nerf, gaussian splatting, slam, ar, neural rendering, mapping, outdoor, efficient  
- **[WeatherGS: 3D Scene Reconstruction in Adverse Weather Conditions via Gaussian Splatting](https://arxiv.org/abs/2412.18862v2)**  
  Authors: Chenghao Qian, Yuhu Guo, Wenjing Li, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.18862v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/weather-gs.)  
  Keywords: 3d gaussian, gaussian splatting, 3d reconstruction, ar, outdoor  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: 3d gaussian, compression, high-fidelity, face, fast, large scene, nerf, gaussian splatting, ar  
- **[LiHi-GS: LiDAR-Supervised Gaussian Splatting for Highway Driving Scene Reconstruction](https://arxiv.org/abs/2412.15447v2)**  
  Authors: Pou-Chun Kung, Xianling Zhang, Katherine A. Skinner, Nikita Jaipuria  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15447v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/lihi_gs)  
  Keywords: 3d gaussian, urban scene, fast, dynamic, gaussian splatting, nerf, ar, autonomous driving  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: 3d gaussian, face, dynamic, slam, localization, ar, lighting, reflection, mapping, tracking, outdoor, geometry, survey  
- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: 3d gaussian, large scene, dynamic, gaussian splatting, ar, head  
- **[HybridGS: Decoupling Transients and Statics with 2D and 3D Gaussian Splatting](https://arxiv.org/abs/2412.03844v2)**  
  Authors: Jingyu Lin, Jiaqi Gu, Lubin Fan, Bojian Wu, Yujing Lou, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03844v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, outdoor, ar  

### Model Compression

*Showing the latest 50 out of 466 papers*

- **[GoDe: Gaussians on Demand for Progressive Level of Detail and Scalable Compression](https://arxiv.org/abs/2501.13558v1)**  
  Authors: Francesco Di Sario, Riccardo Renzulli, Marco Grangetto, Akihiro Sugimoto, Enzo Tartaglione  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13558v1.pdf)  
  Keywords: 3d gaussian, compression, vr, gaussian splatting, ar  
- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, outdoor, efficient  
- **[DARB-Splatting: Generalizing Splatting with Decaying Anisotropic Radial Basis Functions](https://arxiv.org/abs/2501.12369v1)**  
  Authors: Vishagar Arunan, Saeedha Nazar, Hashiru Pramuditha, Vinasirajan Viruthshaan, Sameera Ramasinghe, Simon Lucey, Ranga Rodrigo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12369v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, 3d reconstruction, ar, efficient  
- **[HAC++: Towards 100X Compression of 3D Gaussian Splatting](https://arxiv.org/abs/2501.12255v2)**  
  Authors: Yihang Chen, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12255v2.pdf) | [![GitHub](https://img.shields.io/github/stars/YihangChen-ee/HAC-plus?style=social)](https://github.com/YihangChen-ee/HAC-plus)  
  Keywords: 3d gaussian, compression, compact, gaussian splatting, ar  
- **[GSVC: Efficient Video Representation and Compression Through 2D Gaussian Splatting](https://arxiv.org/abs/2501.12060v2)**  
  Authors: Longan Wang, Yuang Shi, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12060v2.pdf)  
  Keywords: 3d gaussian, compression, dynamic, gaussian splatting, motion, ar, efficient  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: 3d gaussian, nerf, gaussian splatting, 3d reconstruction, ar, sparse-view, efficient  
- **[Decoupling Appearance Variations with 3D Consistent Features in Gaussian Splatting](https://arxiv.org/abs/2501.10788v1)**  
  Authors: Jiaqi Lin, Zhihao Li, Binxiao Huang, Xiao Tang, Jianzhuang Liu, Shiyong Liu, Xiaofei Wu, Fenglong Song, Wenming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10788v1.pdf)  
  Keywords: gaussian splatting, ar, head, real-time rendering, efficient  
- **[GSTAR: Gaussian Surface Tracking and Reconstruction](https://arxiv.org/abs/2501.10283v2)**  
  Authors: Chengwei Zheng, Lixin Xue, Juan Zarate, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10283v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/GSTAR/.)  
  Keywords: 3d gaussian, face, dynamic, gaussian splatting, ar, tracking, efficient  
- **[Creating Virtual Environments with 3D Gaussian Splatting: A Comparative Study](https://arxiv.org/abs/2501.09302v1)**  
  Authors: Shi Qiu, Binzhu Xie, Qixuan Liu, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.09302v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, efficient  
- **[BloomScene: Lightweight Structured 3D Gaussian Splatting for Crossmodal Scene Generation](https://arxiv.org/abs/2501.10462v1)**  
  Authors: Xiaolu Hou, Mingcheng Li, Dingkang Yang, Jiawei Chen, Ziyun Qian, Xiao Zhao, Yue Jiang, Jinjie Wei, Qingyao Xu, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10462v1.pdf)  
  Keywords: lightweight, 3d gaussian, compression, gaussian splatting, ar, head  

### Quality Enhancement

*Showing the latest 50 out of 204 papers*

- **[Deblur-Avatar: Animatable Avatars from Motion-Blurred Monocular Videos](https://arxiv.org/abs/2501.13335v1)**  
  Authors: Xianrui Luo, Juewen Peng, Zhongang Cai, Lei Yang, Fan Yang, Zhiguo Cao, Guosheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13335v1.pdf)  
  Keywords: 3d gaussian, human, high-fidelity, dynamic, gaussian splatting, motion, body, ar, avatar, real-time rendering  
- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: 3d gaussian, high-fidelity, nerf, gaussian splatting, 3d reconstruction, dynamic, motion, slam, ar, mapping, geometry, efficient  
- **[Gaussian Masked Autoencoders](https://arxiv.org/abs/2501.03229v1)**  
  Authors: Jathushan Rajasegaran, Xinlei Chen, Rulilong Li, Christoph Feichtenhofer, Jitendra Malik, Shiry Ginosar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.03229v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://brjathu.github.io/gmae)  
  Keywords: 3d gaussian, high-fidelity, understanding, gaussian splatting, segmentation, ar, semantic  
- **[Deformable Gaussian Splatting for Efficient and High-Fidelity Reconstruction of Surgical Scenes](https://arxiv.org/abs/2501.01101v1)**  
  Authors: Jiwei Shan, Zeyu Cai, Cheng-Tai Hsieh, Shing Shin Cheng, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01101v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, dynamic, gaussian splatting, motion, ar, deformation, efficient  
- **[ActiveGS: Active Scene Reconstruction using Gaussian Splatting](https://arxiv.org/abs/2412.17769v1)**  
  Authors: Liren Jin, Xingguang Zhong, Yue Pan, Jens Behley, Cyrill Stachniss, Marija Popović  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17769v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, robotics, ar  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: 3d gaussian, compression, high-fidelity, face, fast, large scene, nerf, gaussian splatting, ar  
- **[SqueezeMe: Efficient Gaussian Avatars for VR](https://arxiv.org/abs/2412.15171v2)**  
  Authors: Shunsuke Saito, Stanislav Pidhorskyi, Igor Santesteban, Forrest Iandola, Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Frank Yu, Emanuel Garbin, Tomas Simon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15171v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://forresti.github.io/squeezeme.)  
  Keywords: human, vr, gaussian splatting, high quality, motion, ar, head, avatar, efficient  
- **[HyperGS: Hyperspectral 3D Gaussian Splatting](https://arxiv.org/abs/2412.12849v1)**  
  Authors: Christopher Thirgood, Oscar Mendez, Erin Chao Ling, Jon Storey, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12849v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, 4d, gaussian splatting, ar  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, ar, lighting, ray tracing, real-time rendering, reflection, efficient  
- **[Deformable Radial Kernel Splatting](https://arxiv.org/abs/2412.11752v1)**  
  Authors: Yi-Hua Huang, Ming-Xian Lin, Yang-Tian Sun, Ziyi Yang, Xiaoyang Lyu, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11752v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, geometry, efficient  

### Ray Tracing

- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: gaussian splatting, ar, lighting, ray tracing, reflection, relighting, efficient  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, ar, lighting, ray tracing, real-time rendering, reflection, efficient  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: illumination, face, fast, nerf, gaussian splatting, ar, mapping, global illumination, geometry, efficient  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, ray tracing, efficient  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: ray tracing, 3d gaussian, gaussian splatting, ar  
- **[URAvatar: Universal Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2410.24223v1)**  
  Authors: Junxuan Li, Chen Cao, Gabriel Schwartz, Rawal Khirodkar, Christian Richardt, Tomas Simon, Yaser Sheikh, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24223v1.pdf)  
  Keywords: relightable, 3d gaussian, light transport, illumination, human, ar, head, avatar, real-time rendering, global illumination, efficient  
- **[Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization](https://arxiv.org/abs/2410.16978v1)**  
  Authors: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, Ralf Gutjahr, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16978v1.pdf)  
  Keywords: vr, understanding, path tracing, gaussian splatting, medical, ar, head, efficient  
- **[GS^3: Efficient Relighting with Triple Gaussian Splatting](https://arxiv.org/abs/2410.11419v1)**  
  Authors: Zoubin Bi, Yixin Zeng, Chong Zeng, Fan Pei, Xiang Feng, Kun Zhou, Hongzhi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11419v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://GSrelight.github.io/.)  
  Keywords: illumination, shadow, gaussian splatting, ar, lighting, global illumination, relighting, geometry, efficient  
- **[RGM: Reconstructing High-fidelity 3D Car Assets with Relightable 3D-GS Generative Model from a Single Image](https://arxiv.org/abs/2410.08181v1)**  
  Authors: Xiaoxue Chen, Jv Zheng, Hao Huang, Haoran Xu, Weihao Gu, Kangliang Chen, He xiang, Huan-ang Gao, Hao Zhao, Guyue Zhou, Yaqin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08181v1.pdf)  
  Keywords: relightable, 3d gaussian, high-fidelity, illumination, nerf, autonomous driving, ar, lighting, global illumination, relighting, geometry  
- **[6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering](https://arxiv.org/abs/2410.04974v2)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04974v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/6dgs/)  
  Keywords: 3d gaussian, nerf, gaussian splatting, high quality, ar, ray tracing, real-time rendering  

### Relighting

*Showing the latest 50 out of 136 papers*

- **[Car-GS: Addressing Reflective and Transparent Surface Challenges in 3D Car Reconstruction](https://arxiv.org/abs/2501.11020v1)**  
  Authors: Congcong Li, Jin Wang, Xiaomeng Wang, Xingchen Zhou, Wei Wu, Yuzhi Zhang, Tongyi Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lcc815.github.io/Car-GS.)  
  Keywords: face, geometry, ar, reflection, autonomous driving  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: human, face, dynamic, nerf, gaussian splatting, medical, ar, lighting, sparse view  
- **[Reflective Gaussian Splatting](https://arxiv.org/abs/2412.19282v1)**  
  Authors: Yuxuan Yao, Zixuan Zeng, Chun Gu, Xiatian Zhu, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19282v1.pdf)  
  Keywords: nerf, gaussian splatting, ar, lighting, reflection, relighting, geometry  
- **[Generating Editable Head Avatars with 3D Gaussian GANs](https://arxiv.org/abs/2412.19149v1)**  
  Authors: Guohao Li, Hongyu Yang, Yifang Men, Di Huang, Weixin Li, Ruijie Yang, Yunhong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19149v1.pdf) | [![GitHub](https://img.shields.io/github/stars/liguohao96/EGG3D?style=social)](https://github.com/liguohao96/EGG3D)  
  Keywords: 3d gaussian, illumination, face, nerf, gaussian splatting, ar, head, avatar, animation, deformation  
- **[FaceLift: Single Image to 3D Head with View Generation and GS-LRM](https://arxiv.org/abs/2412.17812v1)**  
  Authors: Weijie Lyu, Yi Zhou, Ming-Hsuan Yang, Zhixin Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17812v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weijielyu.github.io/FaceLift.)  
  Keywords: human, face, 4d, ar, lighting, head, animation  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: gaussian splatting, ar, lighting, ray tracing, reflection, relighting, efficient  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: 3d gaussian, face, dynamic, slam, localization, ar, lighting, reflection, mapping, tracking, outdoor, geometry, survey  
- **[EOGS: Gaussian Splatting for Earth Observation](https://arxiv.org/abs/2412.13047v1)**  
  Authors: Luca Savant Aira, Gabriele Facciolo, Thibaud Ehret  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13047v1.pdf)  
  Keywords: shadow, nerf, gaussian splatting, ar  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, ar, lighting, ray tracing, real-time rendering, reflection, efficient  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: illumination, face, fast, nerf, gaussian splatting, ar, mapping, global illumination, geometry, efficient  

### SLAM

*Showing the latest 50 out of 184 papers*

- **[GeomGS: LiDAR-Guided Geometry-Aware Gaussian Splatting for Robot Localization](https://arxiv.org/abs/2501.13417v1)**  
  Authors: Jaewon Lee, Mangyu Kong, Minseong Park, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13417v1.pdf)  
  Keywords: 3d gaussian, robotics, understanding, gaussian splatting, autonomous driving, ar, mapping, geometry, localization  
- **[VIGS SLAM: IMU-based Large-Scale 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2501.13402v1)**  
  Authors: Gyuhyeon Pak, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13402v1.pdf)  
  Keywords: 3d gaussian, slam, gaussian splatting, nerf, ar, mapping, tracking  
- **[GSTAR: Gaussian Surface Tracking and Reconstruction](https://arxiv.org/abs/2501.10283v2)**  
  Authors: Chengwei Zheng, Lixin Xue, Juan Zarate, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10283v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/GSTAR/.)  
  Keywords: 3d gaussian, face, dynamic, gaussian splatting, ar, tracking, efficient  
- **[CityLoc: 6 DoF Localization of Text Descriptions in Large-Scale Scenes with Gaussian Representation](https://arxiv.org/abs/2501.08982v1)**  
  Authors: Qi Ma, Runyi Yang, Bin Ren, Ender Konukoglu, Luc Van Gool, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08982v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, localization  
- **[GS-LIVO: Real-Time LiDAR, Inertial, and Visual Multi-sensor Fused Odometry with Gaussian Mapping](https://arxiv.org/abs/2501.08672v1)**  
  Authors: Sheng Hong, Chunran Zheng, Yishu Shen, Changze Li, Fu Zhang, Tong Qin, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08672v1.pdf)  
  Keywords: 3d gaussian, face, slam, gaussian splatting, motion, ar, mapping, localization  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: large scene, dynamic, nerf, gaussian splatting, slam, ar, mapping, outdoor, geometry, localization  
- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: 3d gaussian, high-fidelity, nerf, gaussian splatting, 3d reconstruction, dynamic, motion, slam, ar, mapping, geometry, efficient  
- **[CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications](https://arxiv.org/abs/2501.06927v1)**  
  Authors: Xinyi Zheng, Steve Zhang, Weizhe Lin, Aaron Zhang, Walterio W. Mayol-Cuevas, Junxiao Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06927v1.pdf)  
  Keywords: nerf, gaussian splatting, 3d reconstruction, motion, segmentation, slam, ar  
- **[ActiveGAMER: Active GAussian Mapping through Efficient Rendering](https://arxiv.org/abs/2501.06897v1)**  
  Authors: Liyan Chen, Huangying Zhan, Kevin Chen, Xiangyu Xu, Qingan Yan, Changjiang Cai, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06897v1.pdf)  
  Keywords: 3d gaussian, efficient rendering, dynamic, gaussian splatting, nerf, ar, mapping, efficient  
- **[MapGS: Generalizable Pretraining and Data Augmentation for Online Mapping via Novel View Synthesis](https://arxiv.org/abs/2501.06660v1)**  
  Authors: Hengyuan Zhang, David Paz, Yuliang Guo, Xinyu Huang, Henrik I. Christensen, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06660v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://henryzhangzhy.github.io/mapgs.)  
  Keywords: fast, gaussian splatting, ar, mapping, efficient  

### Scene Understanding

*Showing the latest 50 out of 218 papers*

- **[GeomGS: LiDAR-Guided Geometry-Aware Gaussian Splatting for Robot Localization](https://arxiv.org/abs/2501.13417v1)**  
  Authors: Jaewon Lee, Mangyu Kong, Minseong Park, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13417v1.pdf)  
  Keywords: 3d gaussian, robotics, understanding, gaussian splatting, autonomous driving, ar, mapping, geometry, localization  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: 3d gaussian, 4d, gaussian splatting, ar, sparse-view, semantic  
- **[CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications](https://arxiv.org/abs/2501.06927v1)**  
  Authors: Xinyi Zheng, Steve Zhang, Weizhe Lin, Aaron Zhang, Walterio W. Mayol-Cuevas, Junxiao Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06927v1.pdf)  
  Keywords: nerf, gaussian splatting, 3d reconstruction, motion, segmentation, slam, ar  
- **[Gaussian Masked Autoencoders](https://arxiv.org/abs/2501.03229v1)**  
  Authors: Jathushan Rajasegaran, Xinlei Chen, Rulilong Li, Christoph Feichtenhofer, Jitendra Malik, Shiry Ginosar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.03229v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://brjathu.github.io/gmae)  
  Keywords: 3d gaussian, high-fidelity, understanding, gaussian splatting, segmentation, ar, semantic  
- **[HOGSA: Bimanual Hand-Object Interaction Understanding with 3D Gaussian Splatting Based Data Augmentation](https://arxiv.org/abs/2501.02845v1)**  
  Authors: Wentian Qu, Jiahe Li, Jian Cheng, Jian Shi, Chenyu Meng, Cuixia Ma, Hongan Wang, Xiaoming Deng, Yinda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.02845v1.pdf)  
  Keywords: 3d gaussian, robotics, understanding, gaussian splatting, motion, ar  
- **[PG-SAG: Parallel Gaussian Splatting for Fine-Grained Large-Scale Urban Buildings Reconstruction via Semantic-Aware Grouping](https://arxiv.org/abs/2501.01677v1)**  
  Authors: Tengfei Wang, Xin Wang, Yongmao Hou, Yiwei Xu, Wendi Zhang, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01677v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TFWang-9527/PG-SAG?style=social)](https://github.com/TFWang-9527/PG-SAG)  
  Keywords: 3d gaussian, face, gaussian splatting, ar, semantic  
- **[Leverage Cross-Attention for End-to-End Open-Vocabulary Panoptic Reconstruction](https://arxiv.org/abs/2501.01119v1)**  
  Authors: Xuan Yu, Yuxuan Xie, Yili Liu, Haojian Lu, Rong Xiong, Yiyi Liao, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01119v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuxuan1206.github.io/panopticrecon_pp/)  
  Keywords: 3d gaussian, robotics, understanding, dynamic, segmentation, ar, head, semantic  
- **[Gaussian Building Mesh (GBM): Extract a Building's 3D Mesh with Google Earth and Gaussian Splatting](https://arxiv.org/abs/2501.00625v2)**  
  Authors: Kyle Gao, Liangzhi Li, Hongjie He, Dening Lu, Linlin Xu, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00625v2.pdf)  
  Keywords: gaussian splatting, segmentation, geometry, ar  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: 3d gaussian, understanding, dynamic, motion, ar, real-time rendering, outdoor  
- **[PanoSLAM: Panoptic 3D Scene Reconstruction via Gaussian SLAM](https://arxiv.org/abs/2501.00352v1)**  
  Authors: Runnan Chen, Zhaoqing Wang, Jiepeng Wang, Yuexin Ma, Mingming Gong, Wenping Wang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00352v1.pdf) | [![GitHub](https://img.shields.io/github/stars/runnanchen/PanoSLAM?style=social)](https://github.com/runnanchen/PanoSLAM)  
  Keywords: 3d gaussian, robotics, understanding, efficient rendering, slam, gaussian splatting, 3d reconstruction, segmentation, ar, mapping, tracking, semantic, efficient, localization  



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