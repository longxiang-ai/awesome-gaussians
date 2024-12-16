# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2024-12-16 00:53:34

## Categories

- [3DGS Surveys](#3dgs-surveys) (19 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (332 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1120 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (377 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (407 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (78 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (375 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (61 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (406 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (190 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (25 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (122 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (161 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (190 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: recognition, 3d gaussian, ar, illumination, survey, gaussian splatting  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: robotics, nerf, lighting, compact, semantic, ar, survey, gaussian splatting, geometry, dynamic, 3d reconstruction, autonomous driving, high-fidelity  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v1)**  
  Authors: Siting Zhu, Guangming Wang, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v1.pdf)  
  Keywords: 3d gaussian, robotics, nerf, ar, survey, gaussian splatting, understanding, real-time rendering  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: 3d gaussian, nerf, lighting, ar, survey, gaussian splatting, high-fidelity  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: 3d gaussian, robotics, nerf, ar, survey, gaussian splatting, 3d reconstruction, vr, autonomous driving  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: 3d gaussian, ar, survey  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v1)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v1.pdf)  
  Keywords: 3d gaussian, ar, efficient, survey, gaussian splatting, understanding, real-time rendering  
- **[Survey on Fundamental Deep Learning 3D Reconstruction Techniques](https://arxiv.org/abs/2407.08137v1)**  
  Authors: Yonge Bai, LikHang Wong, TszYin Twan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.08137v1.pdf)  
  Keywords: 3d gaussian, nerf, ar, survey, gaussian splatting, 3d reconstruction, lighting  
- **[Panopticon: a telescope for our times](https://arxiv.org/abs/2407.05103v2)**  
  Authors: Will Saunders, Timothy Chin, Michael Goodwin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05103v2.pdf)  
  Keywords: ar, survey  
- **[3DGS.zip: A survey on 3D Gaussian Splatting Compression Methods](https://arxiv.org/abs/2407.09510v4)**  
  Authors: Milena T. Bagdasarian, Paul Knoll, Yi-Hsin Li, Florian Barthel, Anna Hilsmann, Peter Eisert, Wieland Morgenstern  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.09510v4.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://w-m.github.io/3dgs-compression-survey/)  
  Keywords: 3d gaussian, ar, compact, compression, efficient, survey, gaussian splatting, head  

### Acceleration

*Showing the latest 50 out of 332 papers*

- **[SLGaussian: Fast Language Gaussian Splatting in Sparse Views](https://arxiv.org/abs/2412.08331v1)**  
  Authors: Kangjie Chen, BingQuan Dai, Minghan Qin, Dongbin Zhang, Peihao Li, Yingshuang Zou, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08331v1.pdf)  
  Keywords: sparse view, robotics, ar, semantic, localization, efficient, gaussian splatting, understanding, segmentation, tracking, fast, vr  
- **[ProGDF: Progressive Gaussian Differential Field for Controllable and Flexible 3D Editing](https://arxiv.org/abs/2412.08152v1)**  
  Authors: Yian Zhao, Wanshi Xu, Yang Wu, Weiheng Huang, Zhongqian Sun, Wei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08152v1.pdf)  
  Keywords: ar, lightweight, efficient, gaussian splatting, efficient rendering, face  
- **[Faster and Better 3D Splatting via Group Training](https://arxiv.org/abs/2412.07608v1)**  
  Authors: Chengbo Wang, Guozheng Ma, Yifei Xue, Yizhen Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07608v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, fast, head, high-fidelity  
- **[EventSplat: 3D Gaussian Splatting from Moving Event Cameras for Real-time Rendering](https://arxiv.org/abs/2412.07293v1)**  
  Authors: Toshiya Yura, Ashkan Mirzaei, Igor Gilitschenski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07293v1.pdf)  
  Keywords: 3d gaussian, nerf, motion, high quality, gaussian splatting, dynamic, real-time rendering, fast  
- **[MV-DUSt3R+: Single-Stage Scene Reconstruction from Sparse Views In 2 Seconds](https://arxiv.org/abs/2412.06974v1)**  
  Authors: Zhenggang Tang, Yuchen Fan, Dilin Wang, Hongyu Xu, Rakesh Ranjan, Alexander Schwing, Zhicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06974v1.pdf)  
  Keywords: sparse view, ar, gaussian splatting, fast, head  
- **[4D Gaussian Splatting with Scale-aware Residual Field and Adaptive Optimization for Real-time Rendering of Temporally Complex Dynamic Scenes](https://arxiv.org/abs/2412.06299v1)**  
  Authors: Jinbo Yan, Rui Peng, Luyang Tang, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06299v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yjb6.github.io/SaRO-GS.github.io.)  
  Keywords: 3d gaussian, 4d, motion, ar, gaussian splatting, dynamic, real-time rendering  
- **[Splatter-360: Generalizable 360$^{\circ}$ Gaussian Splatting for Wide-baseline Panoramic Images](https://arxiv.org/abs/2412.06250v1)**  
  Authors: Zheng Chen, Chenming Wu, Zhelun Shen, Chen Zhao, Weicai Ye, Haocheng Feng, Errui Ding, Song-Hai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06250v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3d-aigc.github.io/Splatter-360/}.)  
  Keywords: 3d gaussian, nerf, ar, geometry, gaussian splatting, real-time rendering, vr  
- **[WATER-GS: Toward Copyright Protection for 3D Gaussian Splatting via Universal Watermarking](https://arxiv.org/abs/2412.05695v1)**  
  Authors: Yuqi Tan, Xiang Liu, Shuzhao Xie, Bin Chen, Shu-Tao Xia, Zhi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05695v1.pdf)  
  Keywords: 3d gaussian, nerf, ar, compression, gaussian splatting, real-time rendering  
- **[Template-free Articulated Gaussian Splatting for Real-time Reposable Dynamic View Synthesis](https://arxiv.org/abs/2412.05570v1)**  
  Authors: Diwen Wan, Yuxiang Wang, Ruijie Lu, Gang Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05570v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, dynamic, real-time rendering  
- **[Pushing Rendering Boundaries: Hard Gaussian Splatting](https://arxiv.org/abs/2412.04826v1)**  
  Authors: Qingshan Xu, Jiequan Cui, Xuanyu Yi, Yuxuan Wang, Yuan Zhou, Yew-Soon Ong, Hanwang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04826v1.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, gaussian splatting  

### Applications

*Showing the latest 50 out of 1120 papers*

- **[Representing Long Volumetric Video with Temporal Gaussian Hierarchy](https://arxiv.org/abs/2412.09608v1)**  
  Authors: Zhen Xu, Yinghao Xu, Zhiyuan Yu, Sida Peng, Jiaming Sun, Hujun Bao, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09608v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/longvolcap.)  
  Keywords: ar, 4d, compact, efficient, dynamic  
- **[Feat2GS: Probing Visual Foundation Models with Gaussian Splatting](https://arxiv.org/abs/2412.09606v1)**  
  Authors: Yue Chen, Xingyu Chen, Anpei Chen, Gerard Pons-Moll, Yuliang Xiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09606v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fanegg.github.io/Feat2GS/.)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting, tracking  
- **[LiftImage3D: Lifting Any Single Image to 3D Gaussians with Video Generation Priors](https://arxiv.org/abs/2412.09597v1)**  
  Authors: Yabo Chen, Chen Yang, Jiemin Fang, Xiaopeng Zhang, Lingxi Xie, Wei Shen, Wenrui Dai, Hongkai Xiong, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09597v1.pdf)  
  Keywords: 3d gaussian, motion, ar, gaussian splatting, face, 3d reconstruction  
- **[FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction](https://arxiv.org/abs/2412.09573v1)**  
  Authors: Jiale Xu, Shenghua Gao, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09573v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, sparse-view, 3d reconstruction, high-fidelity  
- **[SimAvatar: Simulation-Ready Avatars with Layered Hair and Clothing](https://arxiv.org/abs/2412.09545v1)**  
  Authors: Xueting Li, Ye Yuan, Shalini De Mello, Gilles Daviet, Jonathan Leaf, Miles Macklin, Jan Kautz, Umar Iqbal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09545v1.pdf)  
  Keywords: 3d gaussian, motion, body, ar, geometry, avatar, human, dynamic  
- **[GEAL: Generalizable 3D Affordance Learning with Cross-Modal Consistency](https://arxiv.org/abs/2412.09511v1)**  
  Authors: Dongyue Lu, Lingdong Kong, Tianxin Huang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09511v1.pdf)  
  Keywords: robotics, ar, semantic, mapping, gaussian splatting, human  
- **[LIVE-GS: LLM Powers Interactive VR by Enhancing Gaussian Splatting](https://arxiv.org/abs/2412.09176v1)**  
  Authors: Haotian Mao, Zhuoxiong Xu, Siyue Wei, Yule Quan, Nianchen Deng, Xubo Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09176v1.pdf)  
  Keywords: 3d gaussian, body, ar, efficient, gaussian splatting, understanding, segmentation, vr  
- **[DrivingRecon: Large 4D Gaussian Reconstruction Model For Autonomous Driving](https://arxiv.org/abs/2412.09043v1)**  
  Authors: Hao Lu, Tianshuo Xu, Wenzhao Zheng, Yunpeng Zhang, Wei Zhan, Dalong Du, Masayoshi Tomizuka, Kurt Keutzer, Yingcong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09043v1.pdf) | [![GitHub](https://img.shields.io/github/stars/EnVision-Research/DriveRecon?style=social)](https://github.com/EnVision-Research/DriveRecon)  
  Keywords: motion, 4d, ar, geometry, dynamic, autonomous driving  
- **[PointTalk: Audio-Driven Dynamic Lip Point Cloud for 3D Gaussian-based Talking Head Synthesis](https://arxiv.org/abs/2412.08504v1)**  
  Authors: Yifan Xie, Tao Feng, Xin Zhang, Xiangyang Luo, Zixuan Guo, Weijiang Yu, Heng Chang, Fei Ma, Fei Richard Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08504v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, human, dynamic, head, high-fidelity  
- **[SLGaussian: Fast Language Gaussian Splatting in Sparse Views](https://arxiv.org/abs/2412.08331v1)**  
  Authors: Kangjie Chen, BingQuan Dai, Minghan Qin, Dongbin Zhang, Peihao Li, Yingshuang Zou, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08331v1.pdf)  
  Keywords: sparse view, robotics, ar, semantic, localization, efficient, gaussian splatting, understanding, segmentation, tracking, fast, vr  

### Avatar Generation

*Showing the latest 50 out of 377 papers*

- **[LiftImage3D: Lifting Any Single Image to 3D Gaussians with Video Generation Priors](https://arxiv.org/abs/2412.09597v1)**  
  Authors: Yabo Chen, Chen Yang, Jiemin Fang, Xiaopeng Zhang, Lingxi Xie, Wei Shen, Wenrui Dai, Hongkai Xiong, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09597v1.pdf)  
  Keywords: 3d gaussian, motion, ar, gaussian splatting, face, 3d reconstruction  
- **[SimAvatar: Simulation-Ready Avatars with Layered Hair and Clothing](https://arxiv.org/abs/2412.09545v1)**  
  Authors: Xueting Li, Ye Yuan, Shalini De Mello, Gilles Daviet, Jonathan Leaf, Miles Macklin, Jan Kautz, Umar Iqbal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09545v1.pdf)  
  Keywords: 3d gaussian, motion, body, ar, geometry, avatar, human, dynamic  
- **[GEAL: Generalizable 3D Affordance Learning with Cross-Modal Consistency](https://arxiv.org/abs/2412.09511v1)**  
  Authors: Dongyue Lu, Lingdong Kong, Tianxin Huang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09511v1.pdf)  
  Keywords: robotics, ar, semantic, mapping, gaussian splatting, human  
- **[LIVE-GS: LLM Powers Interactive VR by Enhancing Gaussian Splatting](https://arxiv.org/abs/2412.09176v1)**  
  Authors: Haotian Mao, Zhuoxiong Xu, Siyue Wei, Yule Quan, Nianchen Deng, Xubo Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09176v1.pdf)  
  Keywords: 3d gaussian, body, ar, efficient, gaussian splatting, understanding, segmentation, vr  
- **[PointTalk: Audio-Driven Dynamic Lip Point Cloud for 3D Gaussian-based Talking Head Synthesis](https://arxiv.org/abs/2412.08504v1)**  
  Authors: Yifan Xie, Tao Feng, Xin Zhang, Xiangyang Luo, Zixuan Guo, Weijiang Yu, Heng Chang, Fei Ma, Fei Richard Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08504v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, human, dynamic, head, high-fidelity  
- **[ProGDF: Progressive Gaussian Differential Field for Controllable and Flexible 3D Editing](https://arxiv.org/abs/2412.08152v1)**  
  Authors: Yian Zhao, Wanshi Xu, Yang Wu, Weiheng Huang, Zhongqian Sun, Wei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08152v1.pdf)  
  Keywords: ar, lightweight, efficient, gaussian splatting, efficient rendering, face  
- **[GASP: Gaussian Avatars with Synthetic Priors](https://arxiv.org/abs/2412.07739v1)**  
  Authors: Jack Saunders, Charlie Hewitt, Yanan Jian, Marek Kowalski, Tadas Baltrusaitis, Yiye Chen, Darren Cosker, Virginia Estellers, Nicholas Gyde, Vinay P. Namboodiri, Benjamin E Lundell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07739v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://microsoft.github.io/GASP/))  
  Keywords: high quality, avatar, ar, gaussian splatting  
- **[Faster and Better 3D Splatting via Group Training](https://arxiv.org/abs/2412.07608v1)**  
  Authors: Chengbo Wang, Guozheng Ma, Yifei Xue, Yizhen Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07608v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, fast, head, high-fidelity  
- **[MV-DUSt3R+: Single-Stage Scene Reconstruction from Sparse Views In 2 Seconds](https://arxiv.org/abs/2412.06974v1)**  
  Authors: Zhenggang Tang, Yuchen Fan, Dilin Wang, Hongyu Xu, Rakesh Ranjan, Alexander Schwing, Zhicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06974v1.pdf)  
  Keywords: sparse view, ar, gaussian splatting, fast, head  
- **[MixedGaussianAvatar: Realistically and Geometrically Accurate Head Avatar via Mixed 2D-3D Gaussian Splatting](https://arxiv.org/abs/2412.04955v2)**  
  Authors: Peng Chen, Xiaobao Wei, Qingpo Wuwu, Xinyi Wang, Xingyu Xiao, Ming Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04955v2.pdf) | [![GitHub](https://img.shields.io/github/stars/ChenVoid/MGA?style=social)](https://github.com/ChenVoid/MGA/)  
  Keywords: 3d gaussian, nerf, ar, gaussian splatting, avatar, face, head, high-fidelity  

### Dynamic Scene

*Showing the latest 50 out of 407 papers*

- **[Representing Long Volumetric Video with Temporal Gaussian Hierarchy](https://arxiv.org/abs/2412.09608v1)**  
  Authors: Zhen Xu, Yinghao Xu, Zhiyuan Yu, Sida Peng, Jiaming Sun, Hujun Bao, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09608v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/longvolcap.)  
  Keywords: ar, 4d, compact, efficient, dynamic  
- **[LiftImage3D: Lifting Any Single Image to 3D Gaussians with Video Generation Priors](https://arxiv.org/abs/2412.09597v1)**  
  Authors: Yabo Chen, Chen Yang, Jiemin Fang, Xiaopeng Zhang, Lingxi Xie, Wei Shen, Wenrui Dai, Hongkai Xiong, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09597v1.pdf)  
  Keywords: 3d gaussian, motion, ar, gaussian splatting, face, 3d reconstruction  
- **[SimAvatar: Simulation-Ready Avatars with Layered Hair and Clothing](https://arxiv.org/abs/2412.09545v1)**  
  Authors: Xueting Li, Ye Yuan, Shalini De Mello, Gilles Daviet, Jonathan Leaf, Miles Macklin, Jan Kautz, Umar Iqbal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09545v1.pdf)  
  Keywords: 3d gaussian, motion, body, ar, geometry, avatar, human, dynamic  
- **[DrivingRecon: Large 4D Gaussian Reconstruction Model For Autonomous Driving](https://arxiv.org/abs/2412.09043v1)**  
  Authors: Hao Lu, Tianshuo Xu, Wenzhao Zheng, Yunpeng Zhang, Wei Zhan, Dalong Du, Masayoshi Tomizuka, Kurt Keutzer, Yingcong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09043v1.pdf) | [![GitHub](https://img.shields.io/github/stars/EnVision-Research/DriveRecon?style=social)](https://github.com/EnVision-Research/DriveRecon)  
  Keywords: motion, 4d, ar, geometry, dynamic, autonomous driving  
- **[PointTalk: Audio-Driven Dynamic Lip Point Cloud for 3D Gaussian-based Talking Head Synthesis](https://arxiv.org/abs/2412.08504v1)**  
  Authors: Yifan Xie, Tao Feng, Xin Zhang, Xiangyang Luo, Zixuan Guo, Weijiang Yu, Heng Chang, Fei Ma, Fei Richard Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08504v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, human, dynamic, head, high-fidelity  
- **[EventSplat: 3D Gaussian Splatting from Moving Event Cameras for Real-time Rendering](https://arxiv.org/abs/2412.07293v1)**  
  Authors: Toshiya Yura, Ashkan Mirzaei, Igor Gilitschenski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07293v1.pdf)  
  Keywords: 3d gaussian, nerf, motion, high quality, gaussian splatting, dynamic, real-time rendering, fast  
- **[Deblur4DGS: 4D Gaussian Splatting from Blurry Monocular Video](https://arxiv.org/abs/2412.06424v1)**  
  Authors: Renlong Wu, Zhilu Zhang, Mingyang Chen, Xiaopeng Fan, Zifei Yan, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06424v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ZcsrenlongZ/Deblur4DGS?style=social)](https://github.com/ZcsrenlongZ/Deblur4DGS)  
  Keywords: 3d gaussian, 4d, nerf, motion, ar, gaussian splatting, dynamic  
- **[4D Gaussian Splatting with Scale-aware Residual Field and Adaptive Optimization for Real-time Rendering of Temporally Complex Dynamic Scenes](https://arxiv.org/abs/2412.06299v1)**  
  Authors: Jinbo Yan, Rui Peng, Luyang Tang, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06299v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yjb6.github.io/SaRO-GS.github.io.)  
  Keywords: 3d gaussian, 4d, motion, ar, gaussian splatting, dynamic, real-time rendering  
- **[SizeGS: Size-aware Compression of 3D Gaussians with Hierarchical Mixed Precision Quantization](https://arxiv.org/abs/2412.05808v1)**  
  Authors: Shuzhao Xie, Jiahang Liu, Weixiang Zhang, Shijia Ge, Sicheng Pan, Chen Tang, Yunpeng Bai, Zhi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05808v1.pdf)  
  Keywords: 3d gaussian, ar, compression, efficient, dynamic  
- **[Temporally Compressed 3D Gaussian Splatting for Dynamic Scenes](https://arxiv.org/abs/2412.05700v1)**  
  Authors: Saqib Javed, Ahmad Jarrar Khan, Corentin Dumery, Chen Zhao, Mathieu Salzmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05700v1.pdf)  
  Keywords: 3d gaussian, 4d, motion, ar, compression, lightweight, gaussian splatting, dynamic, vr, high-fidelity  

### Few-shot

*Showing the latest 50 out of 78 papers*

- **[FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction](https://arxiv.org/abs/2412.09573v1)**  
  Authors: Jiale Xu, Shenghua Gao, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09573v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, sparse-view, 3d reconstruction, high-fidelity  
- **[SLGaussian: Fast Language Gaussian Splatting in Sparse Views](https://arxiv.org/abs/2412.08331v1)**  
  Authors: Kangjie Chen, BingQuan Dai, Minghan Qin, Dongbin Zhang, Peihao Li, Yingshuang Zou, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08331v1.pdf)  
  Keywords: sparse view, robotics, ar, semantic, localization, efficient, gaussian splatting, understanding, segmentation, tracking, fast, vr  
- **[MV-DUSt3R+: Single-Stage Scene Reconstruction from Sparse Views In 2 Seconds](https://arxiv.org/abs/2412.06974v1)**  
  Authors: Zhenggang Tang, Yuchen Fan, Dilin Wang, Hongyu Xu, Rakesh Ranjan, Alexander Schwing, Zhicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06974v1.pdf)  
  Keywords: sparse view, ar, gaussian splatting, fast, head  
- **[Generative Densification: Learning to Densify Gaussians for High-Fidelity Generalizable 3D Reconstruction](https://arxiv.org/abs/2412.06234v2)**  
  Authors: Seungtae Nam, Xiangyu Sun, Gyeongjin Kang, Younggeun Lee, Seungjun Oh, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06234v2.pdf)  
  Keywords: 3d gaussian, ar, efficient, gaussian splatting, sparse-view, 3d reconstruction, high-fidelity  
- **[GBR: Generative Bundle Refinement for High-fidelity Gaussian Splatting and Meshing](https://arxiv.org/abs/2412.05908v1)**  
  Authors: Jianing Zhang, Yuchao Zheng, Ziwei Li, Qionghai Dai, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05908v1.pdf)  
  Keywords: ar, efficient, geometry, sparse-view, gaussian splatting, high-fidelity  
- **[SparseLGS: Sparse View Language Embedded Gaussian Splatting](https://arxiv.org/abs/2412.02245v2)**  
  Authors: Jun Hu, Zhang Chen, Zhong Li, Yi Xu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02245v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ustc3dv.github.io/SparseLGS)  
  Keywords: sparse view, ar, semantic, gaussian splatting, understanding  
- **[How to Use Diffusion Priors under Sparse Views?](https://arxiv.org/abs/2412.02225v1)**  
  Authors: Qisen Wang, Yifan Zhao, Jiawei Ma, Jia Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02225v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iCVTEAM/IPSM?style=social)](https://github.com/iCVTEAM/IPSM)  
  Keywords: sparse view, 3d gaussian, ar, semantic, geometry, gaussian splatting, sparse-view, 3d reconstruction  
- **[SparseGrasp: Robotic Grasping via 3D Semantic Gaussian Splatting from Sparse Multi-View RGB Images](https://arxiv.org/abs/2412.02140v1)**  
  Authors: Junqiu Yu, Xinlin Ren, Yongchong Gu, Haitao Lin, Tianyu Wang, Yi Zhu, Hang Xu, Yu-Gang Jiang, Xiangyang Xue, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02140v1.pdf)  
  Keywords: 3d gaussian, ar, semantic, efficient, gaussian splatting, sparse-view, human, fast  
- **[DynSUP: Dynamic Gaussian Splatting from An Unposed Image Pair](https://arxiv.org/abs/2412.00851v1)**  
  Authors: Weihang Li, Weirong Chen, Shenhan Qian, Jiajie Chen, Daniel Cremers, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00851v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://colin-de.github.io/DynSUP/.)  
  Keywords: sparse view, 3d gaussian, motion, ar, gaussian splatting, dynamic, high-fidelity  
- **[FlashSLAM: Accelerated RGB-D SLAM for Real-Time 3D Scene Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2412.00682v1)**  
  Authors: Phu Pham, Damon Conover, Aniket Bera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00682v1.pdf)  
  Keywords: sparse view, 3d gaussian, ar, slam, efficient, gaussian splatting, tracking, fast, 3d reconstruction  

### Geometry Reconstruction

*Showing the latest 50 out of 375 papers*

- **[Feat2GS: Probing Visual Foundation Models with Gaussian Splatting](https://arxiv.org/abs/2412.09606v1)**  
  Authors: Yue Chen, Xingyu Chen, Anpei Chen, Gerard Pons-Moll, Yuliang Xiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09606v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fanegg.github.io/Feat2GS/.)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting, tracking  
- **[LiftImage3D: Lifting Any Single Image to 3D Gaussians with Video Generation Priors](https://arxiv.org/abs/2412.09597v1)**  
  Authors: Yabo Chen, Chen Yang, Jiemin Fang, Xiaopeng Zhang, Lingxi Xie, Wei Shen, Wenrui Dai, Hongkai Xiong, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09597v1.pdf)  
  Keywords: 3d gaussian, motion, ar, gaussian splatting, face, 3d reconstruction  
- **[FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction](https://arxiv.org/abs/2412.09573v1)**  
  Authors: Jiale Xu, Shenghua Gao, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09573v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, sparse-view, 3d reconstruction, high-fidelity  
- **[SimAvatar: Simulation-Ready Avatars with Layered Hair and Clothing](https://arxiv.org/abs/2412.09545v1)**  
  Authors: Xueting Li, Ye Yuan, Shalini De Mello, Gilles Daviet, Jonathan Leaf, Miles Macklin, Jan Kautz, Umar Iqbal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09545v1.pdf)  
  Keywords: 3d gaussian, motion, body, ar, geometry, avatar, human, dynamic  
- **[DrivingRecon: Large 4D Gaussian Reconstruction Model For Autonomous Driving](https://arxiv.org/abs/2412.09043v1)**  
  Authors: Hao Lu, Tianshuo Xu, Wenzhao Zheng, Yunpeng Zhang, Wei Zhan, Dalong Du, Masayoshi Tomizuka, Kurt Keutzer, Yingcong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09043v1.pdf) | [![GitHub](https://img.shields.io/github/stars/EnVision-Research/DriveRecon?style=social)](https://github.com/EnVision-Research/DriveRecon)  
  Keywords: motion, 4d, ar, geometry, dynamic, autonomous driving  
- **[Diffusion-Based Attention Warping for Consistent 3D Scene Editing](https://arxiv.org/abs/2412.07984v1)**  
  Authors: Eyal Gomel, Lior Wolf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07984v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://attention-warp.github.io})  
  Keywords: geometry, ar, gaussian splatting  
- **[ResGS: Residual Densification of 3D Gaussian for Efficient Detail Recovery](https://arxiv.org/abs/2412.07494v1)**  
  Authors: Yanzhe Lyu, Kai Cheng, Xin Kang, Xuejin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07494v1.pdf)  
  Keywords: 3d gaussian, ar, efficient, geometry, gaussian splatting  
- **[Splatter-360: Generalizable 360$^{\circ}$ Gaussian Splatting for Wide-baseline Panoramic Images](https://arxiv.org/abs/2412.06250v1)**  
  Authors: Zheng Chen, Chenming Wu, Zhelun Shen, Chen Zhao, Weicai Ye, Haocheng Feng, Errui Ding, Song-Hai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06250v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3d-aigc.github.io/Splatter-360/}.)  
  Keywords: 3d gaussian, nerf, ar, geometry, gaussian splatting, real-time rendering, vr  
- **[Generative Densification: Learning to Densify Gaussians for High-Fidelity Generalizable 3D Reconstruction](https://arxiv.org/abs/2412.06234v2)**  
  Authors: Seungtae Nam, Xiangyu Sun, Gyeongjin Kang, Younggeun Lee, Seungjun Oh, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06234v2.pdf)  
  Keywords: 3d gaussian, ar, efficient, gaussian splatting, sparse-view, 3d reconstruction, high-fidelity  
- **[GBR: Generative Bundle Refinement for High-fidelity Gaussian Splatting and Meshing](https://arxiv.org/abs/2412.05908v1)**  
  Authors: Jianing Zhang, Yuchao Zheng, Ziwei Li, Qionghai Dai, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05908v1.pdf)  
  Keywords: ar, efficient, geometry, sparse-view, gaussian splatting, high-fidelity  

### Large Scene

*Showing the latest 50 out of 61 papers*

- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: 3d gaussian, ar, gaussian splatting, dynamic, large scene, head  
- **[HybridGS: Decoupling Transients and Statics with 2D and 3D Gaussian Splatting](https://arxiv.org/abs/2412.03844v2)**  
  Authors: Jingyu Lin, Jiaqi Gu, Lubin Fan, Bojian Wu, Yujing Lou, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03844v2.pdf)  
  Keywords: outdoor, 3d gaussian, ar, gaussian splatting  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: 4d, ar, semantic, gaussian splatting, dynamic, urban scene, deformation, face  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: nerf, ar, slam, mapping, localization, gaussian splatting, understanding, dynamic, tracking, outdoor, lighting  
- **[Horizon-GS: Unified 3D Gaussian Splatting for Large-Scale Aerial-to-Ground Scenes](https://arxiv.org/abs/2412.01745v1)**  
  Authors: Lihan Jiang, Kerui Ren, Mulin Yu, Linning Xu, Junting Dong, Tao Lu, Feng Zhao, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01745v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, urban scene, high-fidelity  
- **[Tortho-Gaussian: Splatting True Digital Orthophoto Maps](https://arxiv.org/abs/2411.19594v1)**  
  Authors: Xin Wang, Wendi Zhang, Hong Xie, Haibin Ai, Qiangqiang Yuan, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19594v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, face, urban scene  
- **[UrbanCAD: Towards Highly Controllable and Photorealistic 3D Vehicles for Urban Scene Simulation](https://arxiv.org/abs/2411.19292v1)**  
  Authors: Yichong Lu, Yichi Cai, Shangzhan Zhang, Hongyu Zhou, Haoji Hu, Huimin Yu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19292v1.pdf)  
  Keywords: relighting, lighting, ar, urban scene, autonomous driving, high-fidelity  
- **[Unleashing the Power of Data Synthesis in Visual Localization](https://arxiv.org/abs/2412.00138v1)**  
  Authors: Sihang Li, Siqi Tan, Bowen Chang, Jing Zhang, Chen Feng, Yiming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ai4ce.github.io/RAP/)  
  Keywords: 3d gaussian, robotics, ar, localization, dynamic, fast, outdoor  
- **[UniGaussian: Driving Scene Reconstruction from Multiple Camera Models via Unified Gaussian Representations](https://arxiv.org/abs/2411.15355v1)**  
  Authors: Yuan Ren, Guile Wu, Runhao Li, Zheyuan Yang, Yibo Liu, Xingxin Chen, Tongtong Cao, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15355v1.pdf)  
  Keywords: 3d gaussian, ar, semantic, gaussian splatting, understanding, urban scene, fast, real-time rendering, autonomous driving  
- **[LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments](https://arxiv.org/abs/2411.12185v1)**  
  Authors: Renxiang Xiao, Wei Liu, Yushuai Chen, Liang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12185v1.pdf)  
  Keywords: 3d gaussian, ar, semantic, slam, mapping, localization, gaussian splatting, segmentation, tracking, fast, outdoor  

### Model Compression

*Showing the latest 50 out of 406 papers*

- **[Representing Long Volumetric Video with Temporal Gaussian Hierarchy](https://arxiv.org/abs/2412.09608v1)**  
  Authors: Zhen Xu, Yinghao Xu, Zhiyuan Yu, Sida Peng, Jiaming Sun, Hujun Bao, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09608v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/longvolcap.)  
  Keywords: ar, 4d, compact, efficient, dynamic  
- **[LIVE-GS: LLM Powers Interactive VR by Enhancing Gaussian Splatting](https://arxiv.org/abs/2412.09176v1)**  
  Authors: Haotian Mao, Zhuoxiong Xu, Siyue Wei, Yule Quan, Nianchen Deng, Xubo Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09176v1.pdf)  
  Keywords: 3d gaussian, body, ar, efficient, gaussian splatting, understanding, segmentation, vr  
- **[SLGaussian: Fast Language Gaussian Splatting in Sparse Views](https://arxiv.org/abs/2412.08331v1)**  
  Authors: Kangjie Chen, BingQuan Dai, Minghan Qin, Dongbin Zhang, Peihao Li, Yingshuang Zou, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08331v1.pdf)  
  Keywords: sparse view, robotics, ar, semantic, localization, efficient, gaussian splatting, understanding, segmentation, tracking, fast, vr  
- **[ProGDF: Progressive Gaussian Differential Field for Controllable and Flexible 3D Editing](https://arxiv.org/abs/2412.08152v1)**  
  Authors: Yian Zhao, Wanshi Xu, Yang Wu, Weiheng Huang, Zhongqian Sun, Wei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08152v1.pdf)  
  Keywords: ar, lightweight, efficient, gaussian splatting, efficient rendering, face  
- **[Proc-GS: Procedural Building Generation for City Assembly with 3D Gaussians](https://arxiv.org/abs/2412.07660v1)**  
  Authors: Yixuan Li, Xingjian Ran, Linning Xu, Tao Lu, Mulin Yu, Zhenzhi Wang, Yuanbo Xiangli, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07660v1.pdf)  
  Keywords: 3d gaussian, ar, efficient, gaussian splatting, high-fidelity  
- **[ResGS: Residual Densification of 3D Gaussian for Efficient Detail Recovery](https://arxiv.org/abs/2412.07494v1)**  
  Authors: Yanzhe Lyu, Kai Cheng, Xin Kang, Xuejin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07494v1.pdf)  
  Keywords: 3d gaussian, ar, efficient, geometry, gaussian splatting  
- **[Generative Densification: Learning to Densify Gaussians for High-Fidelity Generalizable 3D Reconstruction](https://arxiv.org/abs/2412.06234v2)**  
  Authors: Seungtae Nam, Xiangyu Sun, Gyeongjin Kang, Younggeun Lee, Seungjun Oh, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06234v2.pdf)  
  Keywords: 3d gaussian, ar, efficient, gaussian splatting, sparse-view, 3d reconstruction, high-fidelity  
- **[Efficient Semantic Splatting for Remote Sensing Multi-view Segmentation](https://arxiv.org/abs/2412.05969v2)**  
  Authors: Zipeng Qi, Hao Chen, Haotian Zhang, Zhengxia Zou, Zhenwei Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05969v2.pdf)  
  Keywords: ar, semantic, efficient, gaussian splatting, segmentation  
- **[GBR: Generative Bundle Refinement for High-fidelity Gaussian Splatting and Meshing](https://arxiv.org/abs/2412.05908v1)**  
  Authors: Jianing Zhang, Yuchao Zheng, Ziwei Li, Qionghai Dai, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05908v1.pdf)  
  Keywords: ar, efficient, geometry, sparse-view, gaussian splatting, high-fidelity  
- **[SizeGS: Size-aware Compression of 3D Gaussians with Hierarchical Mixed Precision Quantization](https://arxiv.org/abs/2412.05808v1)**  
  Authors: Shuzhao Xie, Jiahang Liu, Weixiang Zhang, Shijia Ge, Sicheng Pan, Chen Tang, Yunpeng Bai, Zhi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05808v1.pdf)  
  Keywords: 3d gaussian, ar, compression, efficient, dynamic  

### Quality Enhancement

*Showing the latest 50 out of 190 papers*

- **[FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction](https://arxiv.org/abs/2412.09573v1)**  
  Authors: Jiale Xu, Shenghua Gao, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09573v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, sparse-view, 3d reconstruction, high-fidelity  
- **[PointTalk: Audio-Driven Dynamic Lip Point Cloud for 3D Gaussian-based Talking Head Synthesis](https://arxiv.org/abs/2412.08504v1)**  
  Authors: Yifan Xie, Tao Feng, Xin Zhang, Xiangyang Luo, Zixuan Guo, Weijiang Yu, Heng Chang, Fei Ma, Fei Richard Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08504v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, human, dynamic, head, high-fidelity  
- **[GASP: Gaussian Avatars with Synthetic Priors](https://arxiv.org/abs/2412.07739v1)**  
  Authors: Jack Saunders, Charlie Hewitt, Yanan Jian, Marek Kowalski, Tadas Baltrusaitis, Yiye Chen, Darren Cosker, Virginia Estellers, Nicholas Gyde, Vinay P. Namboodiri, Benjamin E Lundell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07739v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://microsoft.github.io/GASP/))  
  Keywords: high quality, avatar, ar, gaussian splatting  
- **[Proc-GS: Procedural Building Generation for City Assembly with 3D Gaussians](https://arxiv.org/abs/2412.07660v1)**  
  Authors: Yixuan Li, Xingjian Ran, Linning Xu, Tao Lu, Mulin Yu, Zhenzhi Wang, Yuanbo Xiangli, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07660v1.pdf)  
  Keywords: 3d gaussian, ar, efficient, gaussian splatting, high-fidelity  
- **[Faster and Better 3D Splatting via Group Training](https://arxiv.org/abs/2412.07608v1)**  
  Authors: Chengbo Wang, Guozheng Ma, Yifei Xue, Yizhen Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07608v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, fast, head, high-fidelity  
- **[EventSplat: 3D Gaussian Splatting from Moving Event Cameras for Real-time Rendering](https://arxiv.org/abs/2412.07293v1)**  
  Authors: Toshiya Yura, Ashkan Mirzaei, Igor Gilitschenski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07293v1.pdf)  
  Keywords: 3d gaussian, nerf, motion, high quality, gaussian splatting, dynamic, real-time rendering, fast  
- **[Generative Densification: Learning to Densify Gaussians for High-Fidelity Generalizable 3D Reconstruction](https://arxiv.org/abs/2412.06234v2)**  
  Authors: Seungtae Nam, Xiangyu Sun, Gyeongjin Kang, Younggeun Lee, Seungjun Oh, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06234v2.pdf)  
  Keywords: 3d gaussian, ar, efficient, gaussian splatting, sparse-view, 3d reconstruction, high-fidelity  
- **[GBR: Generative Bundle Refinement for High-fidelity Gaussian Splatting and Meshing](https://arxiv.org/abs/2412.05908v1)**  
  Authors: Jianing Zhang, Yuchao Zheng, Ziwei Li, Qionghai Dai, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05908v1.pdf)  
  Keywords: ar, efficient, geometry, sparse-view, gaussian splatting, high-fidelity  
- **[Temporally Compressed 3D Gaussian Splatting for Dynamic Scenes](https://arxiv.org/abs/2412.05700v1)**  
  Authors: Saqib Javed, Ahmad Jarrar Khan, Corentin Dumery, Chen Zhao, Mathieu Salzmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05700v1.pdf)  
  Keywords: 3d gaussian, 4d, motion, ar, compression, lightweight, gaussian splatting, dynamic, vr, high-fidelity  
- **[Text-to-3D Gaussian Splatting with Physics-Grounded Motion Generation](https://arxiv.org/abs/2412.05560v1)**  
  Authors: Wenqing Wang, Yun Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05560v1.pdf)  
  Keywords: 3d gaussian, motion, ar, efficient, gaussian splatting, deformation, high-fidelity  

### Ray Tracing

- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v1.pdf)  
  Keywords: 3d gaussian, ar, efficient, gaussian splatting, ray tracing  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v1)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v1.pdf)  
  Keywords: ray tracing, 3d gaussian, ar, gaussian splatting  
- **[URAvatar: Universal Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2410.24223v1)**  
  Authors: Junxuan Li, Chen Cao, Gabriel Schwartz, Rawal Khirodkar, Christian Richardt, Tomas Simon, Yaser Sheikh, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24223v1.pdf)  
  Keywords: 3d gaussian, light transport, ar, illumination, efficient, avatar, human, relightable, real-time rendering, head, global illumination  
- **[Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization](https://arxiv.org/abs/2410.16978v1)**  
  Authors: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, Ralf Gutjahr, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16978v1.pdf)  
  Keywords: medical, path tracing, ar, efficient, gaussian splatting, understanding, head, vr  
- **[GS^3: Efficient Relighting with Triple Gaussian Splatting](https://arxiv.org/abs/2410.11419v1)**  
  Authors: Zoubin Bi, Yixin Zeng, Chong Zeng, Fan Pei, Xiang Feng, Kun Zhou, Hongzhi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11419v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://GSrelight.github.io/.)  
  Keywords: relighting, lighting, ar, illumination, efficient, gaussian splatting, geometry, shadow, global illumination  
- **[RGM: Reconstructing High-fidelity 3D Car Assets with Relightable 3D-GS Generative Model from a Single Image](https://arxiv.org/abs/2410.08181v1)**  
  Authors: Xiaoxue Chen, Jv Zheng, Hao Huang, Haoran Xu, Weihao Gu, Kangliang Chen, He xiang, Huan-ang Gao, Hao Zhao, Guyue Zhou, Yaqin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08181v1.pdf)  
  Keywords: relighting, 3d gaussian, nerf, lighting, ar, high-fidelity, illumination, geometry, relightable, autonomous driving, global illumination  
- **[6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering](https://arxiv.org/abs/2410.04974v2)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04974v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/6dgs/)  
  Keywords: 3d gaussian, nerf, ar, high quality, gaussian splatting, ray tracing, real-time rendering  
- **[GI-GS: Global Illumination Decomposition on Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2410.02619v1)**  
  Authors: Hongze Chen, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.02619v1.pdf)  
  Keywords: relighting, 3d gaussian, path tracing, lighting, ar, high-fidelity, illumination, efficient, gaussian splatting, geometry, lightweight, shadow, global illumination  
- **[EVER: Exact Volumetric Ellipsoid Rendering for Real-time View Synthesis](https://arxiv.org/abs/2410.01804v5)**  
  Authors: Alexander Mai, Peter Hedman, George Kopanas, Dor Verbin, David Futschik, Qiangeng Xu, Falko Kuester, Jonathan T. Barron, Yinda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.01804v5.pdf)  
  Keywords: 3d gaussian, ar, nerf, gaussian splatting, ray tracing  
- **[SpikeGS: Learning 3D Gaussian Fields from Continuous Spike Stream](https://arxiv.org/abs/2409.15176v5)**  
  Authors: Jinze Yu, Xin Peng, Zhengda Lu, Laurent Kneip, Yiqun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.15176v5.pdf) | [![GitHub](https://img.shields.io/github/stars/520jz/SpikeGS?style=social)](https://github.com/520jz/SpikeGS)  
  Keywords: 3d gaussian, ar, illumination, dynamic, real-time rendering, lighting, ray marching  

### Relighting

*Showing the latest 50 out of 122 papers*

- **[Extrapolated Urban View Synthesis Benchmark](https://arxiv.org/abs/2412.05256v2)**  
  Authors: Xiangyu Han, Zhen Jia, Boyi Li, Yan Wang, Boris Ivanovic, Yurong You, Lingjie Liu, Yue Wang, Marco Pavone, Chen Feng, Yiming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05256v2.pdf)  
  Keywords: 3d gaussian, robotics, ar, geometry, gaussian splatting, lighting  
- **[Multi-View Pose-Agnostic Change Localization with Zero Labels](https://arxiv.org/abs/2412.03911v1)**  
  Authors: Chamuditha Jayanga Galappaththige, Jason Lai, Lloyd Windrim, Donald Dansereau, Niko Suenderhauf, Dimity Miller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03911v1.pdf)  
  Keywords: 3d gaussian, ar, localization, gaussian splatting, lighting  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: nerf, ar, slam, mapping, localization, gaussian splatting, understanding, dynamic, tracking, outdoor, lighting  
- **[HUGSIM: A Real-Time, Photo-Realistic and Closed-Loop Simulator for Autonomous Driving](https://arxiv.org/abs/2412.01718v1)**  
  Authors: Hongyu Zhou, Longzhong Lin, Jiabao Wang, Yichong Lu, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01718v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, dynamic, autonomous driving, lighting  
- **[Ref-GS: Directional Factorization for 2D Gaussian Splatting](https://arxiv.org/abs/2412.00905v1)**  
  Authors: Youjia Zhang, Anpei Chen, Yumin Wan, Zikai Song, Junqing Yu, Yawei Luo, Wei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00905v1.pdf)  
  Keywords: ar, efficient, geometry, gaussian splatting, face, head, lighting  
- **[A Lesson in Splats: Teacher-Guided Diffusion for 3D Gaussian Splats Generation with 2D Supervision](https://arxiv.org/abs/2412.00623v2)**  
  Authors: Chensheng Peng, Ido Sobol, Masayoshi Tomizuka, Kurt Keutzer, Chenfeng Xu, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00623v2.pdf)  
  Keywords: 3d gaussian, lighting, ar  
- **[UrbanCAD: Towards Highly Controllable and Photorealistic 3D Vehicles for Urban Scene Simulation](https://arxiv.org/abs/2411.19292v1)**  
  Authors: Yichong Lu, Yichi Cai, Shangzhan Zhang, Hongyu Zhou, Haoji Hu, Huimin Yu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19292v1.pdf)  
  Keywords: relighting, lighting, ar, urban scene, autonomous driving, high-fidelity  
- **[InstanceGaussian: Appearance-Semantic Joint Gaussian Representation for 3D Instance-Level Perception](https://arxiv.org/abs/2411.19235v1)**  
  Authors: Haijie Li, Yanmin Wu, Jiarui Meng, Qiankun Gao, Zhiyao Zhang, Ronggang Wang, Jian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19235v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lhj-git.github.io/InstanceGaussian/)  
  Keywords: 3d gaussian, robotics, ar, semantic, efficient, gaussian splatting, understanding, segmentation, autonomous driving, lighting  
- **[SuperGaussians: Enhancing Gaussian Splatting Using Primitives with Spatially Varying Colors](https://arxiv.org/abs/2411.18966v1)**  
  Authors: Rui Xu, Wenyue Chen, Jiepeng Wang, Yuan Liu, Peng Wang, Lin Gao, Shiqing Xin, Taku Komura, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18966v1.pdf)  
  Keywords: ar, compact, geometry, gaussian splatting, lighting  
- **[NexusSplats: Efficient 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2411.14514v4)**  
  Authors: Yuzhou Tang, Dejun Xu, Yongjie Hou, Zhenzhong Wang, Min Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.14514v4.pdf)  
  Keywords: 3d gaussian, ar, mapping, efficient, gaussian splatting, lighting  

### SLAM

*Showing the latest 50 out of 161 papers*

- **[Feat2GS: Probing Visual Foundation Models with Gaussian Splatting](https://arxiv.org/abs/2412.09606v1)**  
  Authors: Yue Chen, Xingyu Chen, Anpei Chen, Gerard Pons-Moll, Yuliang Xiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09606v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fanegg.github.io/Feat2GS/.)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting, tracking  
- **[GEAL: Generalizable 3D Affordance Learning with Cross-Modal Consistency](https://arxiv.org/abs/2412.09511v1)**  
  Authors: Dongyue Lu, Lingdong Kong, Tianxin Huang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09511v1.pdf)  
  Keywords: robotics, ar, semantic, mapping, gaussian splatting, human  
- **[SLGaussian: Fast Language Gaussian Splatting in Sparse Views](https://arxiv.org/abs/2412.08331v1)**  
  Authors: Kangjie Chen, BingQuan Dai, Minghan Qin, Dongbin Zhang, Peihao Li, Yingshuang Zou, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08331v1.pdf)  
  Keywords: sparse view, robotics, ar, semantic, localization, efficient, gaussian splatting, understanding, segmentation, tracking, fast, vr  
- **[Multi-View Pose-Agnostic Change Localization with Zero Labels](https://arxiv.org/abs/2412.03911v1)**  
  Authors: Chamuditha Jayanga Galappaththige, Jason Lai, Lloyd Windrim, Donald Dansereau, Niko Suenderhauf, Dimity Miller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03911v1.pdf)  
  Keywords: 3d gaussian, ar, localization, gaussian splatting, lighting  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: nerf, ar, slam, mapping, localization, gaussian splatting, understanding, dynamic, tracking, outdoor, lighting  
- **[Splats in Splats: Embedding Invisible 3D Watermark within Gaussian Splatting](https://arxiv.org/abs/2412.03121v1)**  
  Authors: Yijia Guo, Wenkai Huang, Yang Li, Gaolei Li, Hang Zhang, Liwen Hu, Jianhua Li, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03121v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://water-gs.github.io.)  
  Keywords: 3d gaussian, ar, mapping, efficient, gaussian splatting, fast, 3d reconstruction  
- **[Towards Rich Emotions in 3D Avatars: A Text-to-3D Avatar Generation Benchmark](https://arxiv.org/abs/2412.02508v1)**  
  Authors: Haidong Xu, Meishan Zhang, Hao Ju, Zhedong Zheng, Hongyuan Zhu, Erik Cambria, Min Zhang, Hao Fei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02508v1.pdf)  
  Keywords: 3d gaussian, motion, ar, mapping, human, avatar, dynamic  
- **[GSGTrack: Gaussian Splatting-Guided Object Pose Tracking from RGB Videos](https://arxiv.org/abs/2412.02267v1)**  
  Authors: Zhiyuan Chen, Fan Lu, Guo Yu, Bin Li, Sanqing Qu, Yuan Huang, Changhong Fu, Guang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02267v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting, tracking  
- **[CTRL-D: Controllable Dynamic 3D Scene Editing with Personalized 2D Diffusion](https://arxiv.org/abs/2412.01792v1)**  
  Authors: Kai He, Chin-Hsuan Wu, Igor Gilitschenski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01792v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, tracking, dynamic  
- **[6DOPE-GS: Online 6D Object Pose Estimation using Gaussian Splatting](https://arxiv.org/abs/2412.01543v1)**  
  Authors: Yufeng Jin, Vignesh Prasad, Snehal Jauhri, Mathias Franzius, Georgia Chalvatzaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01543v1.pdf)  
  Keywords: robotics, ar, efficient, gaussian splatting, tracking, dynamic, fast, autonomous driving  

### Scene Understanding

*Showing the latest 50 out of 190 papers*

- **[GEAL: Generalizable 3D Affordance Learning with Cross-Modal Consistency](https://arxiv.org/abs/2412.09511v1)**  
  Authors: Dongyue Lu, Lingdong Kong, Tianxin Huang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09511v1.pdf)  
  Keywords: robotics, ar, semantic, mapping, gaussian splatting, human  
- **[LIVE-GS: LLM Powers Interactive VR by Enhancing Gaussian Splatting](https://arxiv.org/abs/2412.09176v1)**  
  Authors: Haotian Mao, Zhuoxiong Xu, Siyue Wei, Yule Quan, Nianchen Deng, Xubo Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09176v1.pdf)  
  Keywords: 3d gaussian, body, ar, efficient, gaussian splatting, understanding, segmentation, vr  
- **[PointTalk: Audio-Driven Dynamic Lip Point Cloud for 3D Gaussian-based Talking Head Synthesis](https://arxiv.org/abs/2412.08504v1)**  
  Authors: Yifan Xie, Tao Feng, Xin Zhang, Xiangyang Luo, Zixuan Guo, Weijiang Yu, Heng Chang, Fei Ma, Fei Richard Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08504v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, human, dynamic, head, high-fidelity  
- **[SLGaussian: Fast Language Gaussian Splatting in Sparse Views](https://arxiv.org/abs/2412.08331v1)**  
  Authors: Kangjie Chen, BingQuan Dai, Minghan Qin, Dongbin Zhang, Peihao Li, Yingshuang Zou, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08331v1.pdf)  
  Keywords: sparse view, robotics, ar, semantic, localization, efficient, gaussian splatting, understanding, segmentation, tracking, fast, vr  
- **[Efficient Semantic Splatting for Remote Sensing Multi-view Segmentation](https://arxiv.org/abs/2412.05969v2)**  
  Authors: Zipeng Qi, Hao Chen, Haotian Zhang, Zhengxia Zou, Zhenwei Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05969v2.pdf)  
  Keywords: ar, semantic, efficient, gaussian splatting, segmentation  
- **[EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding](https://arxiv.org/abs/2412.04380v2)**  
  Authors: Yuqi Wu, Wenzhao Zheng, Sicheng Zuo, Yuanhui Huang, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04380v2.pdf) | [![GitHub](https://img.shields.io/github/stars/YkiWu/EmbodiedOcc?style=social)](https://github.com/YkiWu/EmbodiedOcc)  
  Keywords: 3d gaussian, ar, semantic, efficient, understanding, human  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: 4d, ar, semantic, gaussian splatting, dynamic, urban scene, deformation, face  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: nerf, ar, slam, mapping, localization, gaussian splatting, understanding, dynamic, tracking, outdoor, lighting  
- **[Multi-robot autonomous 3D reconstruction using Gaussian splatting with Semantic guidance](https://arxiv.org/abs/2412.02249v1)**  
  Authors: Jing Zeng, Qi Ye, Tianle Liu, Yang Xu, Jin Li, Jinming Xu, Liang Li, Jiming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02249v1.pdf)  
  Keywords: 3d gaussian, ar, high quality, semantic, gaussian splatting, segmentation, face, 3d reconstruction  
- **[SparseLGS: Sparse View Language Embedded Gaussian Splatting](https://arxiv.org/abs/2412.02245v2)**  
  Authors: Jun Hu, Zhang Chen, Zhong Li, Yi Xu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02245v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ustc3dv.github.io/SparseLGS)  
  Keywords: sparse view, ar, semantic, gaussian splatting, understanding  



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