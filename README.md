# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-01-30 00:44:23

## Categories

- [3DGS Surveys](#3dgs-surveys) (20 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (365 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1269 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (422 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (473 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (91 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (419 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (69 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (474 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (206 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (28 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (137 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (187 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (220 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: reflection, slam, face, localization, dynamic, lighting, 3d gaussian, survey, mapping, ar, geometry, outdoor, tracking  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: illumination, recognition, gaussian splatting, 3d gaussian, survey, ar  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: semantic, geometry, autonomous driving, gaussian splatting, dynamic, robotics, lighting, survey, nerf, ar, compact, 3d reconstruction, high-fidelity  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: real-time rendering, gaussian splatting, robotics, understanding, 3d gaussian, survey, nerf, ar  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: gaussian splatting, lighting, 3d gaussian, survey, nerf, ar, high-fidelity  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: autonomous driving, gaussian splatting, robotics, 3d gaussian, vr, survey, nerf, ar, 3d reconstruction  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: 3d gaussian, survey, ar  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v2)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v2.pdf)  
  Keywords: real-time rendering, gaussian splatting, understanding, 3d gaussian, survey, ar, efficient  
- **[Survey on Fundamental Deep Learning 3D Reconstruction Techniques](https://arxiv.org/abs/2407.08137v1)**  
  Authors: Yonge Bai, LikHang Wong, TszYin Twan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.08137v1.pdf)  
  Keywords: gaussian splatting, lighting, 3d gaussian, survey, nerf, ar, 3d reconstruction  
- **[Panopticon: a telescope for our times](https://arxiv.org/abs/2407.05103v2)**  
  Authors: Will Saunders, Timothy Chin, Michael Goodwin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05103v2.pdf)  
  Keywords: survey, ar  

### Acceleration

*Showing the latest 50 out of 365 papers*

- **[Evaluating CrowdSplat: Perceived Level of Detail for Gaussian Crowds](https://arxiv.org/abs/2501.17085v1)**  
  Authors: Xiaohan Sun, Yinghan Xu, John Dingliana, Carol O'Sullivan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17085v1.pdf)  
  Keywords: avatar, gaussian splatting, 3d gaussian, vr, motion, efficient rendering, ar, efficient  
- **[Trick-GS: A Balanced Bag of Tricks for Efficient Gaussian Splatting](https://arxiv.org/abs/2501.14534v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Mateusz Nowak, Mehmet Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14534v1.pdf)  
  Keywords: efficient, fast, high quality, gaussian splatting, ar, 3d reconstruction  
- **[Deblur-Avatar: Animatable Avatars from Motion-Blurred Monocular Videos](https://arxiv.org/abs/2501.13335v1)**  
  Authors: Xianrui Luo, Juewen Peng, Zhongang Cai, Lei Yang, Fan Yang, Zhiguo Cao, Guosheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13335v1.pdf)  
  Keywords: real-time rendering, human, avatar, gaussian splatting, dynamic, 3d gaussian, body, motion, ar, high-fidelity  
- **[3DGS$^2$: Near Second-order Converging 3D Gaussian Splatting](https://arxiv.org/abs/2501.13975v2)**  
  Authors: Lei Lan, Tianjia Shao, Zixuan Lu, Yu Zhang, Chenfanfu Jiang, Yin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13975v2.pdf)  
  Keywords: efficient, fast, gaussian splatting, 3d gaussian, ar, 3d reconstruction, acceleration  
- **[DARB-Splatting: Generalizing Splatting with Decaying Anisotropic Radial Basis Functions](https://arxiv.org/abs/2501.12369v1)**  
  Authors: Vishagar Arunan, Saeedha Nazar, Hashiru Pramuditha, Vinasirajan Viruthshaan, Sameera Ramasinghe, Simon Lucey, Ranga Rodrigo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12369v1.pdf)  
  Keywords: efficient, fast, gaussian splatting, 3d gaussian, ar, 3d reconstruction  
- **[Decoupling Appearance Variations with 3D Consistent Features in Gaussian Splatting](https://arxiv.org/abs/2501.10788v1)**  
  Authors: Jiaqi Lin, Zhihao Li, Binxiao Huang, Xiao Tang, Jianzhuang Liu, Shiyong Liu, Xiaofei Wu, Fenglong Song, Wenming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10788v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, head, ar, efficient  
- **[Object-Centric 2D Gaussian Splatting: Background Removal and Occlusion-Aware Pruning for Compact Object Models](https://arxiv.org/abs/2501.08174v1)**  
  Authors: Marcel Rogge, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08174v1.pdf)  
  Keywords: compact, fast, gaussian splatting, ar  
- **[ActiveGAMER: Active GAussian Mapping through Efficient Rendering](https://arxiv.org/abs/2501.06897v1)**  
  Authors: Liyan Chen, Huangying Zhan, Kevin Chen, Xiangyu Xu, Qingan Yan, Changjiang Cai, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06897v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, efficient rendering, nerf, ar, efficient, mapping  
- **[MapGS: Generalizable Pretraining and Data Augmentation for Online Mapping via Novel View Synthesis](https://arxiv.org/abs/2501.06660v1)**  
  Authors: Hengyuan Zhang, David Paz, Yuliang Guo, Xinyu Huang, Henrik I. Christensen, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06660v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://henryzhangzhy.github.io/mapgs.)  
  Keywords: fast, gaussian splatting, ar, efficient, mapping  
- **[Locality-aware Gaussian Compression for Fast and High-quality Rendering](https://arxiv.org/abs/2501.05757v1)**  
  Authors: Seungjoo Shin, Jaesik Park, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.05757v1.pdf)  
  Keywords: fast, gaussian splatting, 3d gaussian, compression, ar, compact  

### Applications

*Showing the latest 50 out of 1269 papers*

- **[Evaluating CrowdSplat: Perceived Level of Detail for Gaussian Crowds](https://arxiv.org/abs/2501.17085v1)**  
  Authors: Xiaohan Sun, Yinghan Xu, John Dingliana, Carol O'Sullivan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17085v1.pdf)  
  Keywords: avatar, gaussian splatting, 3d gaussian, vr, motion, efficient rendering, ar, efficient  
- **[DiffSplat: Repurposing Image Diffusion Models for Scalable Gaussian Splat Generation](https://arxiv.org/abs/2501.16764v1)**  
  Authors: Chenguo Lin, Panwang Pan, Bangbang Yang, Zeming Li, Yadong Mu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.16764v1.pdf)  
  Keywords: 3d gaussian, ar, lightweight  
- **[LinPrim: Linear Primitives for Differentiable Volumetric Rendering](https://arxiv.org/abs/2501.16312v2)**  
  Authors: Nicolas von Lützow, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.16312v2.pdf)  
  Keywords: face, head, 3d gaussian, nerf, ar, efficient, geometry  
- **[GaussianToken: An Effective Image Tokenizer with 2D Gaussian Splatting](https://arxiv.org/abs/2501.15619v1)**  
  Authors: Jiajun Dong, Chengkun Wang, Wenzhao Zheng, Lei Chen, Jiwen Lu, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15619v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ChrisDong-THU/GaussianToken?style=social)](https://github.com/ChrisDong-THU/GaussianToken)  
  Keywords: efficient, gaussian splatting, ar, understanding  
- **[Towards Better Robustness: Progressively Joint Pose-3DGS Learning for Arbitrarily Long Videos](https://arxiv.org/abs/2501.15096v1)**  
  Authors: Zhen-Hui Dong, Sheng Ye, Yu-Hui Wen, Nannan Li, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15096v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, motion, ar, tracking, high-fidelity  
- **[HuGDiffusion: Generalizable Single-Image Human Rendering via 3D Gaussian Diffusion](https://arxiv.org/abs/2501.15008v1)**  
  Authors: Yingzhi Tang, Qijian Zhang, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15008v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, human, ar  
- **[Trick-GS: A Balanced Bag of Tricks for Efficient Gaussian Splatting](https://arxiv.org/abs/2501.14534v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Mateusz Nowak, Mehmet Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14534v1.pdf)  
  Keywords: efficient, fast, high quality, gaussian splatting, ar, 3d reconstruction  
- **[Scalable Benchmarking and Robust Learning for Noise-Free Ego-Motion and 3D Reconstruction from Noisy Video](https://arxiv.org/abs/2501.14319v1)**  
  Authors: Xiaohao Xu, Tianyi Zhang, Shibo Zhao, Xiang Li, Sibo Wang, Yongqi Chen, Ye Li, Bhiksha Raj, Matthew Johnson-Roberson, Sebastian Scherer, Xiaonan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14319v1.pdf)  
  Keywords: illumination, gaussian splatting, dynamic, lighting, motion, ar, 3d reconstruction  
- **[Dense-SfM: Structure from Motion with Dense Consistent Matching](https://arxiv.org/abs/2501.14277v1)**  
  Authors: JongMin Lee, Sungjoo Yoo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14277v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, motion, ar  
- **[Micro-macro Wavelet-based Gaussian Splatting for 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2501.14231v1)**  
  Authors: Yihui Li, Chengxin Lv, Hongyu Yang, Di Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14231v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, ar  

### Avatar Generation

*Showing the latest 50 out of 422 papers*

- **[Evaluating CrowdSplat: Perceived Level of Detail for Gaussian Crowds](https://arxiv.org/abs/2501.17085v1)**  
  Authors: Xiaohan Sun, Yinghan Xu, John Dingliana, Carol O'Sullivan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17085v1.pdf)  
  Keywords: avatar, gaussian splatting, 3d gaussian, vr, motion, efficient rendering, ar, efficient  
- **[LinPrim: Linear Primitives for Differentiable Volumetric Rendering](https://arxiv.org/abs/2501.16312v2)**  
  Authors: Nicolas von Lützow, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.16312v2.pdf)  
  Keywords: face, head, 3d gaussian, nerf, ar, efficient, geometry  
- **[Towards Better Robustness: Progressively Joint Pose-3DGS Learning for Arbitrarily Long Videos](https://arxiv.org/abs/2501.15096v1)**  
  Authors: Zhen-Hui Dong, Sheng Ye, Yu-Hui Wen, Nannan Li, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15096v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, motion, ar, tracking, high-fidelity  
- **[HuGDiffusion: Generalizable Single-Image Human Rendering via 3D Gaussian Diffusion](https://arxiv.org/abs/2501.15008v1)**  
  Authors: Yingzhi Tang, Qijian Zhang, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15008v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, human, ar  
- **[Deblur-Avatar: Animatable Avatars from Motion-Blurred Monocular Videos](https://arxiv.org/abs/2501.13335v1)**  
  Authors: Xianrui Luo, Juewen Peng, Zhongang Cai, Lei Yang, Fan Yang, Zhiguo Cao, Guosheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13335v1.pdf)  
  Keywords: real-time rendering, human, avatar, gaussian splatting, dynamic, 3d gaussian, body, motion, ar, high-fidelity  
- **[Car-GS: Addressing Reflective and Transparent Surface Challenges in 3D Car Reconstruction](https://arxiv.org/abs/2501.11020v1)**  
  Authors: Congcong Li, Jin Wang, Xiaomeng Wang, Xingchen Zhou, Wei Wu, Yuzhi Zhang, Tongyi Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lcc815.github.io/Car-GS.)  
  Keywords: reflection, autonomous driving, face, ar, geometry  
- **[Decoupling Appearance Variations with 3D Consistent Features in Gaussian Splatting](https://arxiv.org/abs/2501.10788v1)**  
  Authors: Jiaqi Lin, Zhihao Li, Binxiao Huang, Xiao Tang, Jianzhuang Liu, Shiyong Liu, Xiaofei Wu, Fenglong Song, Wenming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10788v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, head, ar, efficient  
- **[GSTAR: Gaussian Surface Tracking and Reconstruction](https://arxiv.org/abs/2501.10283v2)**  
  Authors: Chengwei Zheng, Lixin Xue, Juan Zarate, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10283v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/GSTAR/.)  
  Keywords: gaussian splatting, face, dynamic, 3d gaussian, ar, efficient, tracking  
- **[GaussianAvatar-Editor: Photorealistic Animatable Gaussian Head Avatar Editor](https://arxiv.org/abs/2501.09978v1)**  
  Authors: Xiangyue Liu, Kunming Luo, Heng Li, Qi Zhang, Yuan Liu, Li Yi, Ping Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.09978v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiangyueliu.github.io/GaussianAvatar-Editor/).)  
  Keywords: avatar, animation, head, 4d, 3d gaussian, motion, ar  
- **[BloomScene: Lightweight Structured 3D Gaussian Splatting for Crossmodal Scene Generation](https://arxiv.org/abs/2501.10462v1)**  
  Authors: Xiaolu Hou, Mingcheng Li, Dingkang Yang, Jiawei Chen, Ziyun Qian, Xiao Zhao, Yue Jiang, Jinjie Wei, Qingyao Xu, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10462v1.pdf)  
  Keywords: lightweight, gaussian splatting, head, 3d gaussian, compression, ar  

### Dynamic Scene

*Showing the latest 50 out of 473 papers*

- **[Evaluating CrowdSplat: Perceived Level of Detail for Gaussian Crowds](https://arxiv.org/abs/2501.17085v1)**  
  Authors: Xiaohan Sun, Yinghan Xu, John Dingliana, Carol O'Sullivan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17085v1.pdf)  
  Keywords: avatar, gaussian splatting, 3d gaussian, vr, motion, efficient rendering, ar, efficient  
- **[Towards Better Robustness: Progressively Joint Pose-3DGS Learning for Arbitrarily Long Videos](https://arxiv.org/abs/2501.15096v1)**  
  Authors: Zhen-Hui Dong, Sheng Ye, Yu-Hui Wen, Nannan Li, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15096v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, motion, ar, tracking, high-fidelity  
- **[Scalable Benchmarking and Robust Learning for Noise-Free Ego-Motion and 3D Reconstruction from Noisy Video](https://arxiv.org/abs/2501.14319v1)**  
  Authors: Xiaohao Xu, Tianyi Zhang, Shibo Zhao, Xiang Li, Sibo Wang, Yongqi Chen, Ye Li, Bhiksha Raj, Matthew Johnson-Roberson, Sebastian Scherer, Xiaonan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14319v1.pdf)  
  Keywords: illumination, gaussian splatting, dynamic, lighting, motion, ar, 3d reconstruction  
- **[Dense-SfM: Structure from Motion with Dense Consistent Matching](https://arxiv.org/abs/2501.14277v1)**  
  Authors: JongMin Lee, Sungjoo Yoo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14277v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, motion, ar  
- **[Deblur-Avatar: Animatable Avatars from Motion-Blurred Monocular Videos](https://arxiv.org/abs/2501.13335v1)**  
  Authors: Xianrui Luo, Juewen Peng, Zhongang Cai, Lei Yang, Fan Yang, Zhiguo Cao, Guosheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13335v1.pdf)  
  Keywords: real-time rendering, human, avatar, gaussian splatting, dynamic, 3d gaussian, body, motion, ar, high-fidelity  
- **[GS-LiDAR: Generating Realistic LiDAR Point Clouds with Panoramic Gaussian Splatting](https://arxiv.org/abs/2501.13971v1)**  
  Authors: Junzhe Jiang, Chun Gu, Yurui Chen, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13971v1.pdf)  
  Keywords: autonomous driving, gaussian splatting, dynamic, nerf, ar, efficient  
- **[GSVC: Efficient Video Representation and Compression Through 2D Gaussian Splatting](https://arxiv.org/abs/2501.12060v2)**  
  Authors: Longan Wang, Yuang Shi, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12060v2.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, compression, motion, ar, efficient  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: semantic, sparse-view, gaussian splatting, 4d, 3d gaussian, ar  
- **[GSTAR: Gaussian Surface Tracking and Reconstruction](https://arxiv.org/abs/2501.10283v2)**  
  Authors: Chengwei Zheng, Lixin Xue, Juan Zarate, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10283v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/GSTAR/.)  
  Keywords: gaussian splatting, face, dynamic, 3d gaussian, ar, efficient, tracking  
- **[GaussianAvatar-Editor: Photorealistic Animatable Gaussian Head Avatar Editor](https://arxiv.org/abs/2501.09978v1)**  
  Authors: Xiangyue Liu, Kunming Luo, Heng Li, Qi Zhang, Yuan Liu, Li Yi, Ping Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.09978v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiangyueliu.github.io/GaussianAvatar-Editor/).)  
  Keywords: avatar, animation, head, 4d, 3d gaussian, motion, ar  

### Few-shot

*Showing the latest 50 out of 91 papers*

- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: semantic, sparse-view, gaussian splatting, 4d, 3d gaussian, ar  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: efficient, sparse-view, gaussian splatting, 3d gaussian, nerf, ar, 3d reconstruction  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: human, gaussian splatting, face, dynamic, lighting, nerf, ar, medical, sparse view  
- **[Synthetic Prior for Few-Shot Drivable Head Avatar Inversion](https://arxiv.org/abs/2501.06903v1)**  
  Authors: Wojciech Zielonka, Stephan J. Garbin, Alexandros Lattas, George Kopanas, Paulo Gotardo, Thabo Beeler, Justus Thies, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06903v1.pdf)  
  Keywords: avatar, gaussian splatting, few-shot, head, 3d gaussian, ar  
- **[NVS-SQA: Exploring Self-Supervised Quality Representation Learning for Neurally Synthesized Scenes without References](https://arxiv.org/abs/2501.06488v1)**  
  Authors: Qiang Qu, Yiran Shen, Xiaoming Chen, Yuk Ying Chung, Weidong Cai, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06488v1.pdf)  
  Keywords: human, gaussian splatting, 3d gaussian, nerf, ar, sparse view  
- **[FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency](https://arxiv.org/abs/2501.04628v1)**  
  Authors: Han Huang, Yulun Wu, Chao Deng, Ge Gao, Ming Gu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04628v1.pdf)  
  Keywords: fast, sparse-view, gaussian splatting, face, ar, sparse view  
- **[Dust to Tower: Coarse-to-Fine Photo-Realistic Scene Reconstruction from Sparse Uncalibrated Images](https://arxiv.org/abs/2412.19518v1)**  
  Authors: Xudong Cai, Yongcai Wang, Zhaoxin Fan, Deng Haoran, Shuo Wang, Wanting Li, Deying Li, Lun Luo, Minhang Wang, Jintao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19518v1.pdf)  
  Keywords: fast, sparse-view, gaussian splatting, 3d gaussian, ar, efficient  
- **[CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting](https://arxiv.org/abs/2412.19142v1)**  
  Authors: Siyu Jiao, Haoye Dong, Yuyang Yin, Zequn Jie, Yinlong Qian, Yao Zhao, Humphrey Shi, Yunchao Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19142v1.pdf)  
  Keywords: gaussian splatting, few-shot, 3d gaussian, ar, efficient  
- **[SolidGS: Consolidating Gaussian Surfel Splatting for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2412.15400v1)**  
  Authors: Zhuowen Shen, Yuan Liu, Zhang Chen, Zhong Li, Jiepeng Wang, Yongqing Liang, Zhengming Yu, Jingdong Zhang, Yi Xu, Scott Schaefer, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15400v1.pdf)  
  Keywords: sparse-view, gaussian splatting, face, ar, geometry, sparse view  
- **[Improving Geometry in Sparse-View 3DGS via Reprojection-based DoF Separation](https://arxiv.org/abs/2412.14568v1)**  
  Authors: Yongsung Kim, Minjun Park, Jooyoung Choi, Sungroh Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.14568v1.pdf)  
  Keywords: sparse-view, gaussian splatting, 3d gaussian, ar, 3d reconstruction, geometry  

### Geometry Reconstruction

*Showing the latest 50 out of 419 papers*

- **[LinPrim: Linear Primitives for Differentiable Volumetric Rendering](https://arxiv.org/abs/2501.16312v2)**  
  Authors: Nicolas von Lützow, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.16312v2.pdf)  
  Keywords: face, head, 3d gaussian, nerf, ar, efficient, geometry  
- **[Trick-GS: A Balanced Bag of Tricks for Efficient Gaussian Splatting](https://arxiv.org/abs/2501.14534v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Mateusz Nowak, Mehmet Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14534v1.pdf)  
  Keywords: efficient, fast, high quality, gaussian splatting, ar, 3d reconstruction  
- **[Scalable Benchmarking and Robust Learning for Noise-Free Ego-Motion and 3D Reconstruction from Noisy Video](https://arxiv.org/abs/2501.14319v1)**  
  Authors: Xiaohao Xu, Tianyi Zhang, Shibo Zhao, Xiang Li, Sibo Wang, Yongqi Chen, Ye Li, Bhiksha Raj, Matthew Johnson-Roberson, Sebastian Scherer, Xiaonan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14319v1.pdf)  
  Keywords: illumination, gaussian splatting, dynamic, lighting, motion, ar, 3d reconstruction  
- **[Dense-SfM: Structure from Motion with Dense Consistent Matching](https://arxiv.org/abs/2501.14277v1)**  
  Authors: JongMin Lee, Sungjoo Yoo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14277v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, motion, ar  
- **[Micro-macro Wavelet-based Gaussian Splatting for 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2501.14231v1)**  
  Authors: Yihui Li, Chengxin Lv, Hongyu Yang, Di Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14231v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, ar  
- **[GeomGS: LiDAR-Guided Geometry-Aware Gaussian Splatting for Robot Localization](https://arxiv.org/abs/2501.13417v1)**  
  Authors: Jaewon Lee, Mangyu Kong, Minseong Park, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13417v1.pdf)  
  Keywords: autonomous driving, gaussian splatting, localization, robotics, understanding, 3d gaussian, ar, geometry, mapping  
- **[3DGS$^2$: Near Second-order Converging 3D Gaussian Splatting](https://arxiv.org/abs/2501.13975v2)**  
  Authors: Lei Lan, Tianjia Shao, Zixuan Lu, Yu Zhang, Chenfanfu Jiang, Yin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13975v2.pdf)  
  Keywords: efficient, fast, gaussian splatting, 3d gaussian, ar, 3d reconstruction, acceleration  
- **[DARB-Splatting: Generalizing Splatting with Decaying Anisotropic Radial Basis Functions](https://arxiv.org/abs/2501.12369v1)**  
  Authors: Vishagar Arunan, Saeedha Nazar, Hashiru Pramuditha, Vinasirajan Viruthshaan, Sameera Ramasinghe, Simon Lucey, Ranga Rodrigo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12369v1.pdf)  
  Keywords: efficient, fast, gaussian splatting, 3d gaussian, ar, 3d reconstruction  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: efficient, sparse-view, gaussian splatting, 3d gaussian, nerf, ar, 3d reconstruction  
- **[Car-GS: Addressing Reflective and Transparent Surface Challenges in 3D Car Reconstruction](https://arxiv.org/abs/2501.11020v1)**  
  Authors: Congcong Li, Jin Wang, Xiaomeng Wang, Xingchen Zhou, Wei Wu, Yuzhi Zhang, Tongyi Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lcc815.github.io/Car-GS.)  
  Keywords: reflection, autonomous driving, face, ar, geometry  

### Large Scene

*Showing the latest 50 out of 69 papers*

- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, outdoor  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: slam, gaussian splatting, large scene, localization, dynamic, nerf, ar, geometry, outdoor, mapping  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: real-time rendering, dynamic, understanding, 3d gaussian, motion, ar, outdoor  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: neural rendering, slam, gaussian splatting, 3d gaussian, nerf, ar, efficient, outdoor, mapping  
- **[WeatherGS: 3D Scene Reconstruction in Adverse Weather Conditions via Gaussian Splatting](https://arxiv.org/abs/2412.18862v2)**  
  Authors: Chenghao Qian, Yuhu Guo, Wenjing Li, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.18862v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/weather-gs.)  
  Keywords: gaussian splatting, 3d gaussian, ar, 3d reconstruction, outdoor  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: fast, gaussian splatting, large scene, face, 3d gaussian, compression, nerf, ar, high-fidelity  
- **[LiHi-GS: LiDAR-Supervised Gaussian Splatting for Highway Driving Scene Reconstruction](https://arxiv.org/abs/2412.15447v2)**  
  Authors: Pou-Chun Kung, Xianling Zhang, Katherine A. Skinner, Nikita Jaipuria  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15447v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/lihi_gs)  
  Keywords: fast, urban scene, autonomous driving, gaussian splatting, dynamic, 3d gaussian, nerf, ar  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: reflection, slam, face, localization, dynamic, lighting, 3d gaussian, survey, mapping, ar, geometry, outdoor, tracking  
- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: gaussian splatting, large scene, dynamic, head, 3d gaussian, ar  
- **[HybridGS: Decoupling Transients and Statics with 2D and 3D Gaussian Splatting](https://arxiv.org/abs/2412.03844v2)**  
  Authors: Jingyu Lin, Jiaqi Gu, Lubin Fan, Bojian Wu, Yujing Lou, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03844v2.pdf)  
  Keywords: outdoor, 3d gaussian, gaussian splatting, ar  

### Model Compression

*Showing the latest 50 out of 474 papers*

- **[Evaluating CrowdSplat: Perceived Level of Detail for Gaussian Crowds](https://arxiv.org/abs/2501.17085v1)**  
  Authors: Xiaohan Sun, Yinghan Xu, John Dingliana, Carol O'Sullivan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17085v1.pdf)  
  Keywords: avatar, gaussian splatting, 3d gaussian, vr, motion, efficient rendering, ar, efficient  
- **[DiffSplat: Repurposing Image Diffusion Models for Scalable Gaussian Splat Generation](https://arxiv.org/abs/2501.16764v1)**  
  Authors: Chenguo Lin, Panwang Pan, Bangbang Yang, Zeming Li, Yadong Mu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.16764v1.pdf)  
  Keywords: 3d gaussian, ar, lightweight  
- **[LinPrim: Linear Primitives for Differentiable Volumetric Rendering](https://arxiv.org/abs/2501.16312v2)**  
  Authors: Nicolas von Lützow, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.16312v2.pdf)  
  Keywords: face, head, 3d gaussian, nerf, ar, efficient, geometry  
- **[GaussianToken: An Effective Image Tokenizer with 2D Gaussian Splatting](https://arxiv.org/abs/2501.15619v1)**  
  Authors: Jiajun Dong, Chengkun Wang, Wenzhao Zheng, Lei Chen, Jiwen Lu, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15619v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ChrisDong-THU/GaussianToken?style=social)](https://github.com/ChrisDong-THU/GaussianToken)  
  Keywords: efficient, gaussian splatting, ar, understanding  
- **[Trick-GS: A Balanced Bag of Tricks for Efficient Gaussian Splatting](https://arxiv.org/abs/2501.14534v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Mateusz Nowak, Mehmet Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14534v1.pdf)  
  Keywords: efficient, fast, high quality, gaussian splatting, ar, 3d reconstruction  
- **[HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting](https://arxiv.org/abs/2501.14147v1)**  
  Authors: Javier Yu, Timothy Chen, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14147v1.pdf)  
  Keywords: semantic, slam, gaussian splatting, 3d gaussian, ar, efficient  
- **[GoDe: Gaussians on Demand for Progressive Level of Detail and Scalable Compression](https://arxiv.org/abs/2501.13558v1)**  
  Authors: Francesco Di Sario, Riccardo Renzulli, Marco Grangetto, Akihiro Sugimoto, Enzo Tartaglione  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13558v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, vr, compression, ar  
- **[3DGS$^2$: Near Second-order Converging 3D Gaussian Splatting](https://arxiv.org/abs/2501.13975v2)**  
  Authors: Lei Lan, Tianjia Shao, Zixuan Lu, Yu Zhang, Chenfanfu Jiang, Yin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13975v2.pdf)  
  Keywords: efficient, fast, gaussian splatting, 3d gaussian, ar, 3d reconstruction, acceleration  
- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, outdoor  
- **[GS-LiDAR: Generating Realistic LiDAR Point Clouds with Panoramic Gaussian Splatting](https://arxiv.org/abs/2501.13971v1)**  
  Authors: Junzhe Jiang, Chun Gu, Yurui Chen, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13971v1.pdf)  
  Keywords: autonomous driving, gaussian splatting, dynamic, nerf, ar, efficient  

### Quality Enhancement

*Showing the latest 50 out of 206 papers*

- **[Towards Better Robustness: Progressively Joint Pose-3DGS Learning for Arbitrarily Long Videos](https://arxiv.org/abs/2501.15096v1)**  
  Authors: Zhen-Hui Dong, Sheng Ye, Yu-Hui Wen, Nannan Li, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15096v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, motion, ar, tracking, high-fidelity  
- **[Trick-GS: A Balanced Bag of Tricks for Efficient Gaussian Splatting](https://arxiv.org/abs/2501.14534v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Mateusz Nowak, Mehmet Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14534v1.pdf)  
  Keywords: efficient, fast, high quality, gaussian splatting, ar, 3d reconstruction  
- **[Deblur-Avatar: Animatable Avatars from Motion-Blurred Monocular Videos](https://arxiv.org/abs/2501.13335v1)**  
  Authors: Xianrui Luo, Juewen Peng, Zhongang Cai, Lei Yang, Fan Yang, Zhiguo Cao, Guosheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13335v1.pdf)  
  Keywords: real-time rendering, human, avatar, gaussian splatting, dynamic, 3d gaussian, body, motion, ar, high-fidelity  
- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: efficient, slam, geometry, gaussian splatting, dynamic, 3d gaussian, motion, nerf, mapping, ar, 3d reconstruction, high-fidelity  
- **[Gaussian Masked Autoencoders](https://arxiv.org/abs/2501.03229v1)**  
  Authors: Jathushan Rajasegaran, Xinlei Chen, Rulilong Li, Christoph Feichtenhofer, Jitendra Malik, Shiry Ginosar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.03229v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://brjathu.github.io/gmae)  
  Keywords: semantic, gaussian splatting, understanding, 3d gaussian, ar, high-fidelity, segmentation  
- **[Deformable Gaussian Splatting for Efficient and High-Fidelity Reconstruction of Surgical Scenes](https://arxiv.org/abs/2501.01101v1)**  
  Authors: Jiwei Shan, Zeyu Cai, Cheng-Tai Hsieh, Shing Shin Cheng, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01101v1.pdf)  
  Keywords: deformation, gaussian splatting, dynamic, 3d gaussian, motion, ar, efficient, high-fidelity  
- **[ActiveGS: Active Scene Reconstruction using Gaussian Splatting](https://arxiv.org/abs/2412.17769v1)**  
  Authors: Liren Jin, Xingguang Zhong, Yue Pan, Jens Behley, Cyrill Stachniss, Marija Popović  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17769v1.pdf)  
  Keywords: gaussian splatting, ar, robotics, high-fidelity  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: fast, gaussian splatting, large scene, face, 3d gaussian, compression, nerf, ar, high-fidelity  
- **[SqueezeMe: Efficient Gaussian Avatars for VR](https://arxiv.org/abs/2412.15171v2)**  
  Authors: Shunsuke Saito, Stanislav Pidhorskyi, Igor Santesteban, Forrest Iandola, Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Frank Yu, Emanuel Garbin, Tomas Simon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15171v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://forresti.github.io/squeezeme.)  
  Keywords: human, high quality, avatar, gaussian splatting, head, vr, motion, ar, efficient  
- **[HyperGS: Hyperspectral 3D Gaussian Splatting](https://arxiv.org/abs/2412.12849v1)**  
  Authors: Christopher Thirgood, Oscar Mendez, Erin Chao Ling, Jon Storey, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12849v1.pdf)  
  Keywords: gaussian splatting, 4d, 3d gaussian, ar, high-fidelity  

### Ray Tracing

- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: reflection, gaussian splatting, lighting, ray tracing, ar, efficient, relighting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: real-time rendering, reflection, gaussian splatting, lighting, ray tracing, 3d gaussian, ar, efficient, high-fidelity  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: efficient, fast, illumination, gaussian splatting, face, nerf, mapping, ar, global illumination, geometry  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v1.pdf)  
  Keywords: gaussian splatting, ray tracing, 3d gaussian, ar, efficient  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: 3d gaussian, gaussian splatting, ray tracing, ar  
- **[URAvatar: Universal Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2410.24223v1)**  
  Authors: Junxuan Li, Chen Cao, Gabriel Schwartz, Rawal Khirodkar, Christian Richardt, Tomas Simon, Yaser Sheikh, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24223v1.pdf)  
  Keywords: efficient, light transport, real-time rendering, human, illumination, avatar, head, relightable, 3d gaussian, ar, global illumination  
- **[Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization](https://arxiv.org/abs/2410.16978v1)**  
  Authors: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, Ralf Gutjahr, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16978v1.pdf)  
  Keywords: gaussian splatting, understanding, head, path tracing, vr, ar, efficient, medical  
- **[GS^3: Efficient Relighting with Triple Gaussian Splatting](https://arxiv.org/abs/2410.11419v1)**  
  Authors: Zoubin Bi, Yixin Zeng, Chong Zeng, Fan Pei, Xiang Feng, Kun Zhou, Hongzhi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11419v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://GSrelight.github.io/.)  
  Keywords: efficient, illumination, gaussian splatting, lighting, shadow, ar, global illumination, relighting, geometry  
- **[RGM: Reconstructing High-fidelity 3D Car Assets with Relightable 3D-GS Generative Model from a Single Image](https://arxiv.org/abs/2410.08181v1)**  
  Authors: Xiaoxue Chen, Jv Zheng, Hao Huang, Haoran Xu, Weihao Gu, Kangliang Chen, He xiang, Huan-ang Gao, Hao Zhao, Guyue Zhou, Yaqin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08181v1.pdf)  
  Keywords: illumination, geometry, autonomous driving, lighting, relightable, 3d gaussian, nerf, ar, global illumination, relighting, high-fidelity  
- **[6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering](https://arxiv.org/abs/2410.04974v2)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04974v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/6dgs/)  
  Keywords: real-time rendering, high quality, gaussian splatting, ray tracing, 3d gaussian, nerf, ar  

### Relighting

*Showing the latest 50 out of 137 papers*

- **[Scalable Benchmarking and Robust Learning for Noise-Free Ego-Motion and 3D Reconstruction from Noisy Video](https://arxiv.org/abs/2501.14319v1)**  
  Authors: Xiaohao Xu, Tianyi Zhang, Shibo Zhao, Xiang Li, Sibo Wang, Yongqi Chen, Ye Li, Bhiksha Raj, Matthew Johnson-Roberson, Sebastian Scherer, Xiaonan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14319v1.pdf)  
  Keywords: illumination, gaussian splatting, dynamic, lighting, motion, ar, 3d reconstruction  
- **[Car-GS: Addressing Reflective and Transparent Surface Challenges in 3D Car Reconstruction](https://arxiv.org/abs/2501.11020v1)**  
  Authors: Congcong Li, Jin Wang, Xiaomeng Wang, Xingchen Zhou, Wei Wu, Yuzhi Zhang, Tongyi Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lcc815.github.io/Car-GS.)  
  Keywords: reflection, autonomous driving, face, ar, geometry  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: human, gaussian splatting, face, dynamic, lighting, nerf, ar, medical, sparse view  
- **[Reflective Gaussian Splatting](https://arxiv.org/abs/2412.19282v1)**  
  Authors: Yuxuan Yao, Zixuan Zeng, Chun Gu, Xiatian Zhu, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19282v1.pdf)  
  Keywords: reflection, gaussian splatting, lighting, nerf, ar, geometry, relighting  
- **[Generating Editable Head Avatars with 3D Gaussian GANs](https://arxiv.org/abs/2412.19149v1)**  
  Authors: Guohao Li, Hongyu Yang, Yifang Men, Di Huang, Weixin Li, Ruijie Yang, Yunhong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19149v1.pdf) | [![GitHub](https://img.shields.io/github/stars/liguohao96/EGG3D?style=social)](https://github.com/liguohao96/EGG3D)  
  Keywords: deformation, illumination, avatar, gaussian splatting, animation, face, head, 3d gaussian, nerf, ar  
- **[FaceLift: Single Image to 3D Head with View Generation and GS-LRM](https://arxiv.org/abs/2412.17812v1)**  
  Authors: Weijie Lyu, Yi Zhou, Ming-Hsuan Yang, Zhixin Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17812v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weijielyu.github.io/FaceLift.)  
  Keywords: human, face, animation, lighting, head, 4d, ar  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: reflection, gaussian splatting, lighting, ray tracing, ar, efficient, relighting  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: reflection, slam, face, localization, dynamic, lighting, 3d gaussian, survey, mapping, ar, geometry, outdoor, tracking  
- **[EOGS: Gaussian Splatting for Earth Observation](https://arxiv.org/abs/2412.13047v1)**  
  Authors: Luca Savant Aira, Gabriele Facciolo, Thibaud Ehret  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13047v1.pdf)  
  Keywords: shadow, gaussian splatting, ar, nerf  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: real-time rendering, reflection, gaussian splatting, lighting, ray tracing, 3d gaussian, ar, efficient, high-fidelity  

### SLAM

*Showing the latest 50 out of 187 papers*

- **[Towards Better Robustness: Progressively Joint Pose-3DGS Learning for Arbitrarily Long Videos](https://arxiv.org/abs/2501.15096v1)**  
  Authors: Zhen-Hui Dong, Sheng Ye, Yu-Hui Wen, Nannan Li, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15096v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, motion, ar, tracking, high-fidelity  
- **[HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting](https://arxiv.org/abs/2501.14147v1)**  
  Authors: Javier Yu, Timothy Chen, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14147v1.pdf)  
  Keywords: semantic, slam, gaussian splatting, 3d gaussian, ar, efficient  
- **[GeomGS: LiDAR-Guided Geometry-Aware Gaussian Splatting for Robot Localization](https://arxiv.org/abs/2501.13417v1)**  
  Authors: Jaewon Lee, Mangyu Kong, Minseong Park, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13417v1.pdf)  
  Keywords: autonomous driving, gaussian splatting, localization, robotics, understanding, 3d gaussian, ar, geometry, mapping  
- **[VIGS SLAM: IMU-based Large-Scale 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2501.13402v1)**  
  Authors: Gyuhyeon Pak, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13402v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, nerf, ar, tracking, mapping  
- **[GSTAR: Gaussian Surface Tracking and Reconstruction](https://arxiv.org/abs/2501.10283v2)**  
  Authors: Chengwei Zheng, Lixin Xue, Juan Zarate, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10283v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/GSTAR/.)  
  Keywords: gaussian splatting, face, dynamic, 3d gaussian, ar, efficient, tracking  
- **[CityLoc: 6 DoF Localization of Text Descriptions in Large-Scale Scenes with Gaussian Representation](https://arxiv.org/abs/2501.08982v1)**  
  Authors: Qi Ma, Runyi Yang, Bin Ren, Ender Konukoglu, Luc Van Gool, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08982v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, localization, ar  
- **[GS-LIVO: Real-Time LiDAR, Inertial, and Visual Multi-sensor Fused Odometry with Gaussian Mapping](https://arxiv.org/abs/2501.08672v1)**  
  Authors: Sheng Hong, Chunran Zheng, Yishu Shen, Changze Li, Fu Zhang, Tong Qin, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08672v1.pdf)  
  Keywords: slam, gaussian splatting, face, localization, 3d gaussian, motion, ar, mapping  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: slam, gaussian splatting, large scene, localization, dynamic, nerf, ar, geometry, outdoor, mapping  
- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: efficient, slam, geometry, gaussian splatting, dynamic, 3d gaussian, motion, nerf, mapping, ar, 3d reconstruction, high-fidelity  
- **[CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications](https://arxiv.org/abs/2501.06927v1)**  
  Authors: Xinyi Zheng, Steve Zhang, Weizhe Lin, Aaron Zhang, Walterio W. Mayol-Cuevas, Junxiao Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06927v1.pdf)  
  Keywords: slam, gaussian splatting, motion, nerf, ar, 3d reconstruction, segmentation  

### Scene Understanding

*Showing the latest 50 out of 220 papers*

- **[GaussianToken: An Effective Image Tokenizer with 2D Gaussian Splatting](https://arxiv.org/abs/2501.15619v1)**  
  Authors: Jiajun Dong, Chengkun Wang, Wenzhao Zheng, Lei Chen, Jiwen Lu, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15619v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ChrisDong-THU/GaussianToken?style=social)](https://github.com/ChrisDong-THU/GaussianToken)  
  Keywords: efficient, gaussian splatting, ar, understanding  
- **[HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting](https://arxiv.org/abs/2501.14147v1)**  
  Authors: Javier Yu, Timothy Chen, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14147v1.pdf)  
  Keywords: semantic, slam, gaussian splatting, 3d gaussian, ar, efficient  
- **[GeomGS: LiDAR-Guided Geometry-Aware Gaussian Splatting for Robot Localization](https://arxiv.org/abs/2501.13417v1)**  
  Authors: Jaewon Lee, Mangyu Kong, Minseong Park, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13417v1.pdf)  
  Keywords: autonomous driving, gaussian splatting, localization, robotics, understanding, 3d gaussian, ar, geometry, mapping  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: semantic, sparse-view, gaussian splatting, 4d, 3d gaussian, ar  
- **[CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications](https://arxiv.org/abs/2501.06927v1)**  
  Authors: Xinyi Zheng, Steve Zhang, Weizhe Lin, Aaron Zhang, Walterio W. Mayol-Cuevas, Junxiao Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06927v1.pdf)  
  Keywords: slam, gaussian splatting, motion, nerf, ar, 3d reconstruction, segmentation  
- **[Gaussian Masked Autoencoders](https://arxiv.org/abs/2501.03229v1)**  
  Authors: Jathushan Rajasegaran, Xinlei Chen, Rulilong Li, Christoph Feichtenhofer, Jitendra Malik, Shiry Ginosar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.03229v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://brjathu.github.io/gmae)  
  Keywords: semantic, gaussian splatting, understanding, 3d gaussian, ar, high-fidelity, segmentation  
- **[HOGSA: Bimanual Hand-Object Interaction Understanding with 3D Gaussian Splatting Based Data Augmentation](https://arxiv.org/abs/2501.02845v1)**  
  Authors: Wentian Qu, Jiahe Li, Jian Cheng, Jian Shi, Chenyu Meng, Cuixia Ma, Hongan Wang, Xiaoming Deng, Yinda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.02845v1.pdf)  
  Keywords: gaussian splatting, robotics, understanding, 3d gaussian, motion, ar  
- **[PG-SAG: Parallel Gaussian Splatting for Fine-Grained Large-Scale Urban Buildings Reconstruction via Semantic-Aware Grouping](https://arxiv.org/abs/2501.01677v1)**  
  Authors: Tengfei Wang, Xin Wang, Yongmao Hou, Yiwei Xu, Wendi Zhang, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01677v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TFWang-9527/PG-SAG?style=social)](https://github.com/TFWang-9527/PG-SAG)  
  Keywords: semantic, gaussian splatting, face, 3d gaussian, ar  
- **[Leverage Cross-Attention for End-to-End Open-Vocabulary Panoptic Reconstruction](https://arxiv.org/abs/2501.01119v1)**  
  Authors: Xuan Yu, Yuxuan Xie, Yili Liu, Haojian Lu, Rong Xiong, Yiyi Liao, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01119v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuxuan1206.github.io/panopticrecon_pp/)  
  Keywords: semantic, dynamic, understanding, head, robotics, 3d gaussian, ar, segmentation  
- **[Gaussian Building Mesh (GBM): Extract a Building's 3D Mesh with Google Earth and Gaussian Splatting](https://arxiv.org/abs/2501.00625v2)**  
  Authors: Kyle Gao, Liangzhi Li, Hongjie He, Dening Lu, Linlin Xu, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00625v2.pdf)  
  Keywords: geometry, gaussian splatting, ar, segmentation  



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