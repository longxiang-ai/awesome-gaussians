# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2024-12-12 00:51:09

## Categories

- [3DGS Surveys](#3dgs-surveys) (19 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (329 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1107 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (371 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (402 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (76 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (369 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (61 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (401 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (188 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (25 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (122 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (158 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (186 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: illumination, survey, recognition, gaussian splatting, 3d gaussian, ar  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: lighting, dynamic, survey, compact, geometry, semantic, high-fidelity, gaussian splatting, robotics, nerf, autonomous driving, ar, 3d reconstruction  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v1)**  
  Authors: Siting Zhu, Guangming Wang, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v1.pdf)  
  Keywords: survey, real-time rendering, gaussian splatting, 3d gaussian, robotics, nerf, understanding, ar  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: lighting, survey, high-fidelity, gaussian splatting, 3d gaussian, nerf, ar  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: vr, survey, gaussian splatting, 3d gaussian, robotics, nerf, autonomous driving, ar, 3d reconstruction  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: survey, ar, 3d gaussian  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v1)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v1.pdf)  
  Keywords: survey, real-time rendering, efficient, gaussian splatting, 3d gaussian, understanding, ar  
- **[Survey on Fundamental Deep Learning 3D Reconstruction Techniques](https://arxiv.org/abs/2407.08137v1)**  
  Authors: Yonge Bai, LikHang Wong, TszYin Twan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.08137v1.pdf)  
  Keywords: lighting, survey, gaussian splatting, 3d gaussian, nerf, ar, 3d reconstruction  
- **[Panopticon: a telescope for our times](https://arxiv.org/abs/2407.05103v2)**  
  Authors: Will Saunders, Timothy Chin, Michael Goodwin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05103v2.pdf)  
  Keywords: survey, ar  
- **[3DGS.zip: A survey on 3D Gaussian Splatting Compression Methods](https://arxiv.org/abs/2407.09510v4)**  
  Authors: Milena T. Bagdasarian, Paul Knoll, Yi-Hsin Li, Florian Barthel, Anna Hilsmann, Peter Eisert, Wieland Morgenstern  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.09510v4.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://w-m.github.io/3dgs-compression-survey/)  
  Keywords: head, survey, compact, compression, efficient, gaussian splatting, 3d gaussian, ar  

### Acceleration

*Showing the latest 50 out of 329 papers*

- **[Faster and Better 3D Splatting via Group Training](https://arxiv.org/abs/2412.07608v1)**  
  Authors: Chengbo Wang, Guozheng Ma, Yifei Xue, Yizhen Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07608v1.pdf)  
  Keywords: head, high-fidelity, gaussian splatting, 3d gaussian, fast, ar  
- **[EventSplat: 3D Gaussian Splatting from Moving Event Cameras for Real-time Rendering](https://arxiv.org/abs/2412.07293v1)**  
  Authors: Toshiya Yura, Ashkan Mirzaei, Igor Gilitschenski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07293v1.pdf)  
  Keywords: high quality, dynamic, real-time rendering, motion, gaussian splatting, 3d gaussian, nerf, fast  
- **[MV-DUSt3R+: Single-Stage Scene Reconstruction from Sparse Views In 2 Seconds](https://arxiv.org/abs/2412.06974v1)**  
  Authors: Zhenggang Tang, Yuchen Fan, Dilin Wang, Hongyu Xu, Rakesh Ranjan, Alexander Schwing, Zhicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06974v1.pdf)  
  Keywords: sparse view, head, gaussian splatting, fast, ar  
- **[4D Gaussian Splatting with Scale-aware Residual Field and Adaptive Optimization for Real-time Rendering of Temporally Complex Dynamic Scenes](https://arxiv.org/abs/2412.06299v1)**  
  Authors: Jinbo Yan, Rui Peng, Luyang Tang, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06299v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yjb6.github.io/SaRO-GS.github.io.)  
  Keywords: dynamic, real-time rendering, motion, gaussian splatting, 3d gaussian, 4d, ar  
- **[Splatter-360: Generalizable 360$^{\circ}$ Gaussian Splatting for Wide-baseline Panoramic Images](https://arxiv.org/abs/2412.06250v1)**  
  Authors: Zheng Chen, Chenming Wu, Zhelun Shen, Chen Zhao, Weicai Ye, Haocheng Feng, Errui Ding, Song-Hai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06250v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3d-aigc.github.io/Splatter-360/}.)  
  Keywords: vr, real-time rendering, geometry, gaussian splatting, 3d gaussian, nerf, ar  
- **[WATER-GS: Toward Copyright Protection for 3D Gaussian Splatting via Universal Watermarking](https://arxiv.org/abs/2412.05695v1)**  
  Authors: Yuqi Tan, Xiang Liu, Shuzhao Xie, Bin Chen, Shu-Tao Xia, Zhi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05695v1.pdf)  
  Keywords: real-time rendering, compression, gaussian splatting, 3d gaussian, nerf, ar  
- **[Template-free Articulated Gaussian Splatting for Real-time Reposable Dynamic View Synthesis](https://arxiv.org/abs/2412.05570v1)**  
  Authors: Diwen Wan, Yuxiang Wang, Ruijie Lu, Gang Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05570v1.pdf)  
  Keywords: dynamic, real-time rendering, gaussian splatting, 3d gaussian, ar  
- **[Pushing Rendering Boundaries: Hard Gaussian Splatting](https://arxiv.org/abs/2412.04826v1)**  
  Authors: Qingshan Xu, Jiequan Cui, Xuanyu Yi, Yuxuan Wang, Yuan Zhou, Yew-Soon Ong, Hanwang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04826v1.pdf)  
  Keywords: ar, gaussian splatting, real-time rendering, 3d gaussian  
- **[Turbo3D: Ultra-fast Text-to-3D Generation](https://arxiv.org/abs/2412.04470v1)**  
  Authors: Hanzhe Hu, Tianwei Yin, Fujun Luan, Yiwei Hu, Hao Tan, Zexiang Xu, Sai Bi, Shubham Tulsiani, Kai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04470v1.pdf)  
  Keywords: efficient, fast, ar, gaussian splatting  
- **[QUEEN: QUantized Efficient ENcoding of Dynamic Gaussians for Streaming Free-viewpoint Videos](https://arxiv.org/abs/2412.04469v1)**  
  Authors: Sharath Girish, Tianye Li, Amrita Mazumdar, Abhinav Shrivastava, David Luebke, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/queen)  
  Keywords: high quality, dynamic, efficient, gaussian splatting, 3d gaussian, fast, ar  

### Applications

*Showing the latest 50 out of 1107 papers*

- **[GASP: Gaussian Avatars with Synthetic Priors](https://arxiv.org/abs/2412.07739v1)**  
  Authors: Jack Saunders, Charlie Hewitt, Yanan Jian, Marek Kowalski, Tadas Baltrusaitis, Yiye Chen, Darren Cosker, Virginia Estellers, Nicholas Gyde, Vinay P. Namboodiri, Benjamin E Lundell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07739v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://microsoft.github.io/GASP/))  
  Keywords: high quality, gaussian splatting, ar, avatar  
- **[Proc-GS: Procedural Building Generation for City Assembly with 3D Gaussians](https://arxiv.org/abs/2412.07660v1)**  
  Authors: Yixuan Li, Xingjian Ran, Linning Xu, Tao Lu, Mulin Yu, Zhenzhi Wang, Yuanbo Xiangli, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07660v1.pdf)  
  Keywords: efficient, high-fidelity, gaussian splatting, 3d gaussian, ar  
- **[Faster and Better 3D Splatting via Group Training](https://arxiv.org/abs/2412.07608v1)**  
  Authors: Chengbo Wang, Guozheng Ma, Yifei Xue, Yizhen Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07608v1.pdf)  
  Keywords: head, high-fidelity, gaussian splatting, 3d gaussian, fast, ar  
- **[ResGS: Residual Densification of 3D Gaussian for Efficient Detail Recovery](https://arxiv.org/abs/2412.07494v1)**  
  Authors: Yanzhe Lyu, Kai Cheng, Xin Kang, Xuejin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07494v1.pdf)  
  Keywords: geometry, efficient, gaussian splatting, 3d gaussian, ar  
- **[MV-DUSt3R+: Single-Stage Scene Reconstruction from Sparse Views In 2 Seconds](https://arxiv.org/abs/2412.06974v1)**  
  Authors: Zhenggang Tang, Yuchen Fan, Dilin Wang, Hongyu Xu, Rakesh Ranjan, Alexander Schwing, Zhicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06974v1.pdf)  
  Keywords: sparse view, head, gaussian splatting, fast, ar  
- **[Deblur4DGS: 4D Gaussian Splatting from Blurry Monocular Video](https://arxiv.org/abs/2412.06424v1)**  
  Authors: Renlong Wu, Zhilu Zhang, Mingyang Chen, Xiaopeng Fan, Zifei Yan, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06424v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ZcsrenlongZ/Deblur4DGS?style=social)](https://github.com/ZcsrenlongZ/Deblur4DGS)  
  Keywords: dynamic, motion, gaussian splatting, 3d gaussian, nerf, 4d, ar  
- **[4D Gaussian Splatting with Scale-aware Residual Field and Adaptive Optimization for Real-time Rendering of Temporally Complex Dynamic Scenes](https://arxiv.org/abs/2412.06299v1)**  
  Authors: Jinbo Yan, Rui Peng, Luyang Tang, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06299v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yjb6.github.io/SaRO-GS.github.io.)  
  Keywords: dynamic, real-time rendering, motion, gaussian splatting, 3d gaussian, 4d, ar  
- **[Advancing Extended Reality with 3D Gaussian Splatting: Innovations and Prospects](https://arxiv.org/abs/2412.06257v1)**  
  Authors: Shi Qiu, Binzhu Xie, Qixuan Liu, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06257v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian  
- **[Splatter-360: Generalizable 360$^{\circ}$ Gaussian Splatting for Wide-baseline Panoramic Images](https://arxiv.org/abs/2412.06250v1)**  
  Authors: Zheng Chen, Chenming Wu, Zhelun Shen, Chen Zhao, Weicai Ye, Haocheng Feng, Errui Ding, Song-Hai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06250v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3d-aigc.github.io/Splatter-360/}.)  
  Keywords: vr, real-time rendering, geometry, gaussian splatting, 3d gaussian, nerf, ar  
- **[Generative Densification: Learning to Densify Gaussians for High-Fidelity Generalizable 3D Reconstruction](https://arxiv.org/abs/2412.06234v1)**  
  Authors: Seungtae Nam, Xiangyu Sun, Gyeongjin Kang, Younggeun Lee, Seungjun Oh, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06234v1.pdf)  
  Keywords: sparse-view, efficient, high-fidelity, gaussian splatting, 3d gaussian, ar, 3d reconstruction  

### Avatar Generation

*Showing the latest 50 out of 371 papers*

- **[GASP: Gaussian Avatars with Synthetic Priors](https://arxiv.org/abs/2412.07739v1)**  
  Authors: Jack Saunders, Charlie Hewitt, Yanan Jian, Marek Kowalski, Tadas Baltrusaitis, Yiye Chen, Darren Cosker, Virginia Estellers, Nicholas Gyde, Vinay P. Namboodiri, Benjamin E Lundell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07739v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://microsoft.github.io/GASP/))  
  Keywords: high quality, gaussian splatting, ar, avatar  
- **[Faster and Better 3D Splatting via Group Training](https://arxiv.org/abs/2412.07608v1)**  
  Authors: Chengbo Wang, Guozheng Ma, Yifei Xue, Yizhen Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07608v1.pdf)  
  Keywords: head, high-fidelity, gaussian splatting, 3d gaussian, fast, ar  
- **[MV-DUSt3R+: Single-Stage Scene Reconstruction from Sparse Views In 2 Seconds](https://arxiv.org/abs/2412.06974v1)**  
  Authors: Zhenggang Tang, Yuchen Fan, Dilin Wang, Hongyu Xu, Rakesh Ranjan, Alexander Schwing, Zhicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06974v1.pdf)  
  Keywords: sparse view, head, gaussian splatting, fast, ar  
- **[MixedGaussianAvatar: Realistically and Geometrically Accurate Head Avatar via Mixed 2D-3D Gaussian Splatting](https://arxiv.org/abs/2412.04955v1)**  
  Authors: Peng Chen, Xiaobao Wei, Qingpo Wuwu, Xinyi Wang, Xingyu Xiao, Ming Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04955v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ChenVoid/MGA?style=social)](https://github.com/ChenVoid/MGA/)  
  Keywords: head, face, high-fidelity, gaussian splatting, 3d gaussian, nerf, ar, avatar  
- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: dynamic, head, gaussian splatting, 3d gaussian, large scene, ar  
- **[PBDyG: Position Based Dynamic Gaussians for Motion-Aware Clothed Human Avatars](https://arxiv.org/abs/2412.04433v2)**  
  Authors: Shota Sasaki, Jane Wu, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04433v2.pdf)  
  Keywords: deformation, dynamic, body, human, motion, gaussian splatting, 3d gaussian, ar, avatar  
- **[EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding](https://arxiv.org/abs/2412.04380v2)**  
  Authors: Yuqi Wu, Wenzhao Zheng, Sicheng Zuo, Yuanhui Huang, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04380v2.pdf) | [![GitHub](https://img.shields.io/github/stars/YkiWu/EmbodiedOcc?style=social)](https://github.com/YkiWu/EmbodiedOcc)  
  Keywords: human, semantic, efficient, 3d gaussian, understanding, ar  
- **[DGNS: Deformable Gaussian Splatting and Dynamic Neural Surface for Monocular Dynamic 3D Reconstruction](https://arxiv.org/abs/2412.03910v1)**  
  Authors: Xuesong Li, Jinguang Tong, Jie Hong, Vivien Rolland, Lars Petersson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03910v1.pdf)  
  Keywords: dynamic, geometry, face, gaussian splatting, fast, ar, 3d reconstruction  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: deformation, dynamic, semantic, face, gaussian splatting, urban scene, 4d, ar  
- **[2DGS-Room: Seed-Guided 2D Gaussian Splatting with Geometric Constrains for High-Fidelity Indoor Scene Reconstruction](https://arxiv.org/abs/2412.03428v1)**  
  Authors: Wanting Zhang, Haodong Xiang, Zhichao Liao, Xiansong Lai, Xinghui Li, Long Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03428v1.pdf)  
  Keywords: dynamic, face, high-fidelity, gaussian splatting, 3d gaussian, ar  

### Dynamic Scene

*Showing the latest 50 out of 402 papers*

- **[EventSplat: 3D Gaussian Splatting from Moving Event Cameras for Real-time Rendering](https://arxiv.org/abs/2412.07293v1)**  
  Authors: Toshiya Yura, Ashkan Mirzaei, Igor Gilitschenski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07293v1.pdf)  
  Keywords: high quality, dynamic, real-time rendering, motion, gaussian splatting, 3d gaussian, nerf, fast  
- **[Deblur4DGS: 4D Gaussian Splatting from Blurry Monocular Video](https://arxiv.org/abs/2412.06424v1)**  
  Authors: Renlong Wu, Zhilu Zhang, Mingyang Chen, Xiaopeng Fan, Zifei Yan, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06424v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ZcsrenlongZ/Deblur4DGS?style=social)](https://github.com/ZcsrenlongZ/Deblur4DGS)  
  Keywords: dynamic, motion, gaussian splatting, 3d gaussian, nerf, 4d, ar  
- **[4D Gaussian Splatting with Scale-aware Residual Field and Adaptive Optimization for Real-time Rendering of Temporally Complex Dynamic Scenes](https://arxiv.org/abs/2412.06299v1)**  
  Authors: Jinbo Yan, Rui Peng, Luyang Tang, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06299v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yjb6.github.io/SaRO-GS.github.io.)  
  Keywords: dynamic, real-time rendering, motion, gaussian splatting, 3d gaussian, 4d, ar  
- **[SizeGS: Size-aware Compression of 3D Gaussians with Hierarchical Mixed Precision Quantization](https://arxiv.org/abs/2412.05808v1)**  
  Authors: Shuzhao Xie, Jiahang Liu, Weixiang Zhang, Shijia Ge, Sicheng Pan, Chen Tang, Yunpeng Bai, Zhi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05808v1.pdf)  
  Keywords: dynamic, compression, efficient, 3d gaussian, ar  
- **[Temporally Compressed 3D Gaussian Splatting for Dynamic Scenes](https://arxiv.org/abs/2412.05700v1)**  
  Authors: Saqib Javed, Ahmad Jarrar Khan, Corentin Dumery, Chen Zhao, Mathieu Salzmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05700v1.pdf)  
  Keywords: dynamic, vr, compression, high-fidelity, motion, gaussian splatting, lightweight, 3d gaussian, 4d, ar  
- **[Template-free Articulated Gaussian Splatting for Real-time Reposable Dynamic View Synthesis](https://arxiv.org/abs/2412.05570v1)**  
  Authors: Diwen Wan, Yuxiang Wang, Ruijie Lu, Gang Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05570v1.pdf)  
  Keywords: dynamic, real-time rendering, gaussian splatting, 3d gaussian, ar  
- **[Text-to-3D Gaussian Splatting with Physics-Grounded Motion Generation](https://arxiv.org/abs/2412.05560v1)**  
  Authors: Wenqing Wang, Yun Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05560v1.pdf)  
  Keywords: deformation, efficient, high-fidelity, motion, gaussian splatting, 3d gaussian, ar  
- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: dynamic, head, gaussian splatting, 3d gaussian, large scene, ar  
- **[QUEEN: QUantized Efficient ENcoding of Dynamic Gaussians for Streaming Free-viewpoint Videos](https://arxiv.org/abs/2412.04469v1)**  
  Authors: Sharath Girish, Tianye Li, Amrita Mazumdar, Abhinav Shrivastava, David Luebke, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/queen)  
  Keywords: high quality, dynamic, efficient, gaussian splatting, 3d gaussian, fast, ar  
- **[Sparse Voxels Rasterization: Real-time High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2412.04459v1)**  
  Authors: Cheng Sun, Jaesung Choe, Charles Loop, Wei-Chiu Ma, Yu-Chiang Frank Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04459v1.pdf)  
  Keywords: dynamic, efficient, high-fidelity, gaussian splatting, 3d gaussian, 4d, ar  

### Few-shot

*Showing the latest 50 out of 76 papers*

- **[MV-DUSt3R+: Single-Stage Scene Reconstruction from Sparse Views In 2 Seconds](https://arxiv.org/abs/2412.06974v1)**  
  Authors: Zhenggang Tang, Yuchen Fan, Dilin Wang, Hongyu Xu, Rakesh Ranjan, Alexander Schwing, Zhicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06974v1.pdf)  
  Keywords: sparse view, head, gaussian splatting, fast, ar  
- **[Generative Densification: Learning to Densify Gaussians for High-Fidelity Generalizable 3D Reconstruction](https://arxiv.org/abs/2412.06234v1)**  
  Authors: Seungtae Nam, Xiangyu Sun, Gyeongjin Kang, Younggeun Lee, Seungjun Oh, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06234v1.pdf)  
  Keywords: sparse-view, efficient, high-fidelity, gaussian splatting, 3d gaussian, ar, 3d reconstruction  
- **[GBR: Generative Bundle Refinement for High-fidelity Gaussian Splatting and Meshing](https://arxiv.org/abs/2412.05908v1)**  
  Authors: Jianing Zhang, Yuchao Zheng, Ziwei Li, Qionghai Dai, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05908v1.pdf)  
  Keywords: sparse-view, geometry, efficient, high-fidelity, gaussian splatting, ar  
- **[SparseLGS: Sparse View Language Embedded Gaussian Splatting](https://arxiv.org/abs/2412.02245v2)**  
  Authors: Jun Hu, Zhang Chen, Zhong Li, Yi Xu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02245v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ustc3dv.github.io/SparseLGS)  
  Keywords: sparse view, semantic, gaussian splatting, understanding, ar  
- **[How to Use Diffusion Priors under Sparse Views?](https://arxiv.org/abs/2412.02225v1)**  
  Authors: Qisen Wang, Yifan Zhao, Jiawei Ma, Jia Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02225v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iCVTEAM/IPSM?style=social)](https://github.com/iCVTEAM/IPSM)  
  Keywords: sparse-view, sparse view, geometry, semantic, gaussian splatting, 3d gaussian, ar, 3d reconstruction  
- **[SparseGrasp: Robotic Grasping via 3D Semantic Gaussian Splatting from Sparse Multi-View RGB Images](https://arxiv.org/abs/2412.02140v1)**  
  Authors: Junqiu Yu, Xinlin Ren, Yongchong Gu, Haitao Lin, Tianyu Wang, Yi Zhu, Hang Xu, Yu-Gang Jiang, Xiangyang Xue, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02140v1.pdf)  
  Keywords: sparse-view, human, semantic, efficient, gaussian splatting, 3d gaussian, fast, ar  
- **[DynSUP: Dynamic Gaussian Splatting from An Unposed Image Pair](https://arxiv.org/abs/2412.00851v1)**  
  Authors: Weihang Li, Weirong Chen, Shenhan Qian, Jiajie Chen, Daniel Cremers, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00851v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://colin-de.github.io/DynSUP/.)  
  Keywords: dynamic, sparse view, high-fidelity, motion, gaussian splatting, 3d gaussian, ar  
- **[FlashSLAM: Accelerated RGB-D SLAM for Real-Time 3D Scene Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2412.00682v1)**  
  Authors: Phu Pham, Damon Conover, Aniket Bera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00682v1.pdf)  
  Keywords: slam, sparse view, efficient, gaussian splatting, tracking, 3d gaussian, fast, ar, 3d reconstruction  
- **[NovelGS: Consistent Novel-view Denoising via Large Gaussian Reconstruction Model](https://arxiv.org/abs/2411.16779v1)**  
  Authors: Jinpeng Liu, Jiale Xu, Weihao Cheng, Yiming Gao, Xintao Wang, Ying Shan, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16779v1.pdf)  
  Keywords: sparse-view, gaussian splatting, 3d gaussian, fast, ar  
- **[GPS-Gaussian+: Generalizable Pixel-wise 3D Gaussian Splatting for Real-Time Human-Scene Rendering from Sparse Views](https://arxiv.org/abs/2411.11363v1)**  
  Authors: Boyao Zhou, Shunyuan Zheng, Hanzhang Tu, Ruizhi Shao, Boning Liu, Shengping Zhang, Liqiang Nie, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.11363v1.pdf)  
  Keywords: sparse-view, sparse view, human, real-time rendering, geometry, gaussian splatting, 3d gaussian, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 369 papers*

- **[ResGS: Residual Densification of 3D Gaussian for Efficient Detail Recovery](https://arxiv.org/abs/2412.07494v1)**  
  Authors: Yanzhe Lyu, Kai Cheng, Xin Kang, Xuejin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07494v1.pdf)  
  Keywords: geometry, efficient, gaussian splatting, 3d gaussian, ar  
- **[Splatter-360: Generalizable 360$^{\circ}$ Gaussian Splatting for Wide-baseline Panoramic Images](https://arxiv.org/abs/2412.06250v1)**  
  Authors: Zheng Chen, Chenming Wu, Zhelun Shen, Chen Zhao, Weicai Ye, Haocheng Feng, Errui Ding, Song-Hai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06250v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3d-aigc.github.io/Splatter-360/}.)  
  Keywords: vr, real-time rendering, geometry, gaussian splatting, 3d gaussian, nerf, ar  
- **[Generative Densification: Learning to Densify Gaussians for High-Fidelity Generalizable 3D Reconstruction](https://arxiv.org/abs/2412.06234v1)**  
  Authors: Seungtae Nam, Xiangyu Sun, Gyeongjin Kang, Younggeun Lee, Seungjun Oh, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06234v1.pdf)  
  Keywords: sparse-view, efficient, high-fidelity, gaussian splatting, 3d gaussian, ar, 3d reconstruction  
- **[GBR: Generative Bundle Refinement for High-fidelity Gaussian Splatting and Meshing](https://arxiv.org/abs/2412.05908v1)**  
  Authors: Jianing Zhang, Yuchao Zheng, Ziwei Li, Qionghai Dai, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05908v1.pdf)  
  Keywords: sparse-view, geometry, efficient, high-fidelity, gaussian splatting, ar  
- **[Extrapolated Urban View Synthesis Benchmark](https://arxiv.org/abs/2412.05256v2)**  
  Authors: Xiangyu Han, Zhen Jia, Boyi Li, Yan Wang, Boris Ivanovic, Yurong You, Lingjie Liu, Yue Wang, Marco Pavone, Chen Feng, Yiming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05256v2.pdf)  
  Keywords: lighting, geometry, gaussian splatting, robotics, 3d gaussian, ar  
- **[DGNS: Deformable Gaussian Splatting and Dynamic Neural Surface for Monocular Dynamic 3D Reconstruction](https://arxiv.org/abs/2412.03910v1)**  
  Authors: Xuesong Li, Jinguang Tong, Jie Hong, Vivien Rolland, Lars Petersson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03910v1.pdf)  
  Keywords: dynamic, geometry, face, gaussian splatting, fast, ar, 3d reconstruction  
- **[Splats in Splats: Embedding Invisible 3D Watermark within Gaussian Splatting](https://arxiv.org/abs/2412.03121v1)**  
  Authors: Yijia Guo, Wenkai Huang, Yang Li, Gaolei Li, Hang Zhang, Liwen Hu, Jianhua Li, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03121v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://water-gs.github.io.)  
  Keywords: efficient, gaussian splatting, 3d gaussian, fast, ar, 3d reconstruction, mapping  
- **[RoDyGS: Robust Dynamic Gaussian Splatting for Casual Videos](https://arxiv.org/abs/2412.03077v1)**  
  Authors: Yoonwoo Jeong, Junmyeong Lee, Hoseung Choi, Minsu Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03077v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rodygs.github.io/.)  
  Keywords: dynamic, geometry, high-fidelity, motion, gaussian splatting, ar  
- **[AniGS: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction](https://arxiv.org/abs/2412.02684v1)**  
  Authors: Lingteng Qiu, Shenhao Zhu, Qi Zuo, Xiaodong Gu, Yuan Dong, Junfei Zhang, Chao Xu, Zhe Li, Weihao Yuan, Liefeng Bo, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02684v1.pdf)  
  Keywords: ar, human, real-time rendering, animation, efficient, gaussian splatting, 4d, avatar, 3d reconstruction  
- **[Realistic Surgical Simulation from Monocular Videos](https://arxiv.org/abs/2412.02359v1)**  
  Authors: Kailing Wang, Chen Yang, Keyang Zhao, Xiaokang Yang, Wei Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02359v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://namaenashibot.github.io/SurgiSim/.)  
  Keywords: deformation, dynamic, geometry, high-fidelity, motion, 3d gaussian, ar  

### Large Scene

*Showing the latest 50 out of 61 papers*

- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: dynamic, head, gaussian splatting, 3d gaussian, large scene, ar  
- **[HybridGS: Decoupling Transients and Statics with 2D and 3D Gaussian Splatting](https://arxiv.org/abs/2412.03844v2)**  
  Authors: Jingyu Lin, Jiaqi Gu, Lubin Fan, Bojian Wu, Yujing Lou, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03844v2.pdf)  
  Keywords: outdoor, ar, gaussian splatting, 3d gaussian  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: deformation, dynamic, semantic, face, gaussian splatting, urban scene, 4d, ar  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: lighting, slam, dynamic, outdoor, localization, gaussian splatting, tracking, nerf, understanding, ar, mapping  
- **[Horizon-GS: Unified 3D Gaussian Splatting for Large-Scale Aerial-to-Ground Scenes](https://arxiv.org/abs/2412.01745v1)**  
  Authors: Lihan Jiang, Kerui Ren, Mulin Yu, Linning Xu, Junting Dong, Tao Lu, Feng Zhao, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01745v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, urban scene, 3d gaussian, ar  
- **[Tortho-Gaussian: Splatting True Digital Orthophoto Maps](https://arxiv.org/abs/2411.19594v1)**  
  Authors: Xin Wang, Wendi Zhang, Hong Xie, Haibin Ai, Qiangqiang Yuan, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19594v1.pdf)  
  Keywords: face, gaussian splatting, urban scene, 3d gaussian, ar  
- **[UrbanCAD: Towards Highly Controllable and Photorealistic 3D Vehicles for Urban Scene Simulation](https://arxiv.org/abs/2411.19292v1)**  
  Authors: Yichong Lu, Yichi Cai, Shangzhan Zhang, Hongyu Zhou, Haoji Hu, Huimin Yu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19292v1.pdf)  
  Keywords: lighting, relighting, high-fidelity, urban scene, autonomous driving, ar  
- **[Unleashing the Power of Data Synthesis in Visual Localization](https://arxiv.org/abs/2412.00138v1)**  
  Authors: Sihang Li, Siqi Tan, Bowen Chang, Jing Zhang, Chen Feng, Yiming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ai4ce.github.io/RAP/)  
  Keywords: dynamic, outdoor, localization, 3d gaussian, robotics, fast, ar  
- **[UniGaussian: Driving Scene Reconstruction from Multiple Camera Models via Unified Gaussian Representations](https://arxiv.org/abs/2411.15355v1)**  
  Authors: Yuan Ren, Guile Wu, Runhao Li, Zheyuan Yang, Yibo Liu, Xingxin Chen, Tongtong Cao, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15355v1.pdf)  
  Keywords: real-time rendering, semantic, autonomous driving, gaussian splatting, urban scene, 3d gaussian, fast, understanding, ar  
- **[LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments](https://arxiv.org/abs/2411.12185v1)**  
  Authors: Renxiang Xiao, Wei Liu, Yushuai Chen, Liang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12185v1.pdf)  
  Keywords: slam, outdoor, localization, segmentation, semantic, gaussian splatting, tracking, 3d gaussian, fast, ar, mapping  

### Model Compression

*Showing the latest 50 out of 401 papers*

- **[Proc-GS: Procedural Building Generation for City Assembly with 3D Gaussians](https://arxiv.org/abs/2412.07660v1)**  
  Authors: Yixuan Li, Xingjian Ran, Linning Xu, Tao Lu, Mulin Yu, Zhenzhi Wang, Yuanbo Xiangli, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07660v1.pdf)  
  Keywords: efficient, high-fidelity, gaussian splatting, 3d gaussian, ar  
- **[ResGS: Residual Densification of 3D Gaussian for Efficient Detail Recovery](https://arxiv.org/abs/2412.07494v1)**  
  Authors: Yanzhe Lyu, Kai Cheng, Xin Kang, Xuejin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07494v1.pdf)  
  Keywords: geometry, efficient, gaussian splatting, 3d gaussian, ar  
- **[Generative Densification: Learning to Densify Gaussians for High-Fidelity Generalizable 3D Reconstruction](https://arxiv.org/abs/2412.06234v1)**  
  Authors: Seungtae Nam, Xiangyu Sun, Gyeongjin Kang, Younggeun Lee, Seungjun Oh, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06234v1.pdf)  
  Keywords: sparse-view, efficient, high-fidelity, gaussian splatting, 3d gaussian, ar, 3d reconstruction  
- **[Efficient Semantic Splatting for Remote Sensing Multi-view Segmentation](https://arxiv.org/abs/2412.05969v1)**  
  Authors: Zipeng Qi, Hao Chen, Haotian Zhang, Zhengxia Zou, Zhenwei Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05969v1.pdf)  
  Keywords: segmentation, semantic, efficient, gaussian splatting, ar  
- **[GBR: Generative Bundle Refinement for High-fidelity Gaussian Splatting and Meshing](https://arxiv.org/abs/2412.05908v1)**  
  Authors: Jianing Zhang, Yuchao Zheng, Ziwei Li, Qionghai Dai, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05908v1.pdf)  
  Keywords: sparse-view, geometry, efficient, high-fidelity, gaussian splatting, ar  
- **[SizeGS: Size-aware Compression of 3D Gaussians with Hierarchical Mixed Precision Quantization](https://arxiv.org/abs/2412.05808v1)**  
  Authors: Shuzhao Xie, Jiahang Liu, Weixiang Zhang, Shijia Ge, Sicheng Pan, Chen Tang, Yunpeng Bai, Zhi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05808v1.pdf)  
  Keywords: dynamic, compression, efficient, 3d gaussian, ar  
- **[Temporally Compressed 3D Gaussian Splatting for Dynamic Scenes](https://arxiv.org/abs/2412.05700v1)**  
  Authors: Saqib Javed, Ahmad Jarrar Khan, Corentin Dumery, Chen Zhao, Mathieu Salzmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05700v1.pdf)  
  Keywords: dynamic, vr, compression, high-fidelity, motion, gaussian splatting, lightweight, 3d gaussian, 4d, ar  
- **[WATER-GS: Toward Copyright Protection for 3D Gaussian Splatting via Universal Watermarking](https://arxiv.org/abs/2412.05695v1)**  
  Authors: Yuqi Tan, Xiang Liu, Shuzhao Xie, Bin Chen, Shu-Tao Xia, Zhi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05695v1.pdf)  
  Keywords: real-time rendering, compression, gaussian splatting, 3d gaussian, nerf, ar  
- **[Text-to-3D Gaussian Splatting with Physics-Grounded Motion Generation](https://arxiv.org/abs/2412.05560v1)**  
  Authors: Wenqing Wang, Yun Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05560v1.pdf)  
  Keywords: deformation, efficient, high-fidelity, motion, gaussian splatting, 3d gaussian, ar  
- **[Radiant: Large-scale 3D Gaussian Rendering based on Hierarchical Framework](https://arxiv.org/abs/2412.05546v1)**  
  Authors: Haosong Peng, Tianyu Qi, Yufeng Zhan, Hao Li, Yalun Dai, Yuanqing Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05546v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 188 papers*

- **[GASP: Gaussian Avatars with Synthetic Priors](https://arxiv.org/abs/2412.07739v1)**  
  Authors: Jack Saunders, Charlie Hewitt, Yanan Jian, Marek Kowalski, Tadas Baltrusaitis, Yiye Chen, Darren Cosker, Virginia Estellers, Nicholas Gyde, Vinay P. Namboodiri, Benjamin E Lundell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07739v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://microsoft.github.io/GASP/))  
  Keywords: high quality, gaussian splatting, ar, avatar  
- **[Proc-GS: Procedural Building Generation for City Assembly with 3D Gaussians](https://arxiv.org/abs/2412.07660v1)**  
  Authors: Yixuan Li, Xingjian Ran, Linning Xu, Tao Lu, Mulin Yu, Zhenzhi Wang, Yuanbo Xiangli, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07660v1.pdf)  
  Keywords: efficient, high-fidelity, gaussian splatting, 3d gaussian, ar  
- **[Faster and Better 3D Splatting via Group Training](https://arxiv.org/abs/2412.07608v1)**  
  Authors: Chengbo Wang, Guozheng Ma, Yifei Xue, Yizhen Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07608v1.pdf)  
  Keywords: head, high-fidelity, gaussian splatting, 3d gaussian, fast, ar  
- **[EventSplat: 3D Gaussian Splatting from Moving Event Cameras for Real-time Rendering](https://arxiv.org/abs/2412.07293v1)**  
  Authors: Toshiya Yura, Ashkan Mirzaei, Igor Gilitschenski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07293v1.pdf)  
  Keywords: high quality, dynamic, real-time rendering, motion, gaussian splatting, 3d gaussian, nerf, fast  
- **[Generative Densification: Learning to Densify Gaussians for High-Fidelity Generalizable 3D Reconstruction](https://arxiv.org/abs/2412.06234v1)**  
  Authors: Seungtae Nam, Xiangyu Sun, Gyeongjin Kang, Younggeun Lee, Seungjun Oh, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06234v1.pdf)  
  Keywords: sparse-view, efficient, high-fidelity, gaussian splatting, 3d gaussian, ar, 3d reconstruction  
- **[GBR: Generative Bundle Refinement for High-fidelity Gaussian Splatting and Meshing](https://arxiv.org/abs/2412.05908v1)**  
  Authors: Jianing Zhang, Yuchao Zheng, Ziwei Li, Qionghai Dai, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05908v1.pdf)  
  Keywords: sparse-view, geometry, efficient, high-fidelity, gaussian splatting, ar  
- **[Temporally Compressed 3D Gaussian Splatting for Dynamic Scenes](https://arxiv.org/abs/2412.05700v1)**  
  Authors: Saqib Javed, Ahmad Jarrar Khan, Corentin Dumery, Chen Zhao, Mathieu Salzmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05700v1.pdf)  
  Keywords: dynamic, vr, compression, high-fidelity, motion, gaussian splatting, lightweight, 3d gaussian, 4d, ar  
- **[Text-to-3D Gaussian Splatting with Physics-Grounded Motion Generation](https://arxiv.org/abs/2412.05560v1)**  
  Authors: Wenqing Wang, Yun Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05560v1.pdf)  
  Keywords: deformation, efficient, high-fidelity, motion, gaussian splatting, 3d gaussian, ar  
- **[MixedGaussianAvatar: Realistically and Geometrically Accurate Head Avatar via Mixed 2D-3D Gaussian Splatting](https://arxiv.org/abs/2412.04955v1)**  
  Authors: Peng Chen, Xiaobao Wei, Qingpo Wuwu, Xinyi Wang, Xingyu Xiao, Ming Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04955v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ChenVoid/MGA?style=social)](https://github.com/ChenVoid/MGA/)  
  Keywords: head, face, high-fidelity, gaussian splatting, 3d gaussian, nerf, ar, avatar  
- **[QUEEN: QUantized Efficient ENcoding of Dynamic Gaussians for Streaming Free-viewpoint Videos](https://arxiv.org/abs/2412.04469v1)**  
  Authors: Sharath Girish, Tianye Li, Amrita Mazumdar, Abhinav Shrivastava, David Luebke, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/queen)  
  Keywords: high quality, dynamic, efficient, gaussian splatting, 3d gaussian, fast, ar  

### Ray Tracing

- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v1.pdf)  
  Keywords: ray tracing, efficient, gaussian splatting, 3d gaussian, ar  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v1)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v1.pdf)  
  Keywords: ray tracing, ar, gaussian splatting, 3d gaussian  
- **[URAvatar: Universal Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2410.24223v1)**  
  Authors: Junxuan Li, Chen Cao, Gabriel Schwartz, Rawal Khirodkar, Christian Richardt, Tomas Simon, Yaser Sheikh, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24223v1.pdf)  
  Keywords: light transport, global illumination, illumination, head, human, real-time rendering, efficient, 3d gaussian, ar, avatar, relightable  
- **[Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization](https://arxiv.org/abs/2410.16978v1)**  
  Authors: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, Ralf Gutjahr, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16978v1.pdf)  
  Keywords: path tracing, head, vr, efficient, medical, gaussian splatting, understanding, ar  
- **[GS^3: Efficient Relighting with Triple Gaussian Splatting](https://arxiv.org/abs/2410.11419v1)**  
  Authors: Zoubin Bi, Yixin Zeng, Chong Zeng, Fan Pei, Xiang Feng, Kun Zhou, Hongzhi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11419v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://GSrelight.github.io/.)  
  Keywords: lighting, global illumination, illumination, relighting, geometry, efficient, gaussian splatting, shadow, ar  
- **[RGM: Reconstructing High-fidelity 3D Car Assets with Relightable 3D-GS Generative Model from a Single Image](https://arxiv.org/abs/2410.08181v1)**  
  Authors: Xiaoxue Chen, Jv Zheng, Hao Huang, Haoran Xu, Weihao Gu, Kangliang Chen, He xiang, Huan-ang Gao, Hao Zhao, Guyue Zhou, Yaqin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08181v1.pdf)  
  Keywords: lighting, global illumination, illumination, relighting, geometry, high-fidelity, 3d gaussian, nerf, autonomous driving, ar, relightable  
- **[6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering](https://arxiv.org/abs/2410.04974v2)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04974v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/6dgs/)  
  Keywords: high quality, ray tracing, real-time rendering, gaussian splatting, 3d gaussian, nerf, ar  
- **[GI-GS: Global Illumination Decomposition on Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2410.02619v1)**  
  Authors: Hongze Chen, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.02619v1.pdf)  
  Keywords: path tracing, global illumination, illumination, lighting, relighting, geometry, efficient, high-fidelity, gaussian splatting, lightweight, 3d gaussian, shadow, ar  
- **[EVER: Exact Volumetric Ellipsoid Rendering for Real-time View Synthesis](https://arxiv.org/abs/2410.01804v5)**  
  Authors: Alexander Mai, Peter Hedman, George Kopanas, Dor Verbin, David Futschik, Qiangeng Xu, Falko Kuester, Jonathan T. Barron, Yinda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.01804v5.pdf)  
  Keywords: ray tracing, gaussian splatting, 3d gaussian, nerf, ar  
- **[SpikeGS: Learning 3D Gaussian Fields from Continuous Spike Stream](https://arxiv.org/abs/2409.15176v5)**  
  Authors: Jinze Yu, Xin Peng, Zhengda Lu, Laurent Kneip, Yiqun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.15176v5.pdf) | [![GitHub](https://img.shields.io/github/stars/520jz/SpikeGS?style=social)](https://github.com/520jz/SpikeGS)  
  Keywords: lighting, illumination, dynamic, real-time rendering, ray marching, 3d gaussian, ar  

### Relighting

*Showing the latest 50 out of 122 papers*

- **[Extrapolated Urban View Synthesis Benchmark](https://arxiv.org/abs/2412.05256v2)**  
  Authors: Xiangyu Han, Zhen Jia, Boyi Li, Yan Wang, Boris Ivanovic, Yurong You, Lingjie Liu, Yue Wang, Marco Pavone, Chen Feng, Yiming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05256v2.pdf)  
  Keywords: lighting, geometry, gaussian splatting, robotics, 3d gaussian, ar  
- **[Multi-View Pose-Agnostic Change Localization with Zero Labels](https://arxiv.org/abs/2412.03911v1)**  
  Authors: Chamuditha Jayanga Galappaththige, Jason Lai, Lloyd Windrim, Donald Dansereau, Niko Suenderhauf, Dimity Miller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03911v1.pdf)  
  Keywords: lighting, localization, gaussian splatting, 3d gaussian, ar  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: lighting, slam, dynamic, outdoor, localization, gaussian splatting, tracking, nerf, understanding, ar, mapping  
- **[HUGSIM: A Real-Time, Photo-Realistic and Closed-Loop Simulator for Autonomous Driving](https://arxiv.org/abs/2412.01718v1)**  
  Authors: Hongyu Zhou, Longzhong Lin, Jiabao Wang, Yichong Lu, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01718v1.pdf)  
  Keywords: lighting, dynamic, gaussian splatting, 3d gaussian, autonomous driving, ar  
- **[Ref-GS: Directional Factorization for 2D Gaussian Splatting](https://arxiv.org/abs/2412.00905v1)**  
  Authors: Youjia Zhang, Anpei Chen, Yumin Wan, Zikai Song, Junqing Yu, Yawei Luo, Wei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00905v1.pdf)  
  Keywords: lighting, head, geometry, efficient, face, gaussian splatting, ar  
- **[A Lesson in Splats: Teacher-Guided Diffusion for 3D Gaussian Splats Generation with 2D Supervision](https://arxiv.org/abs/2412.00623v2)**  
  Authors: Chensheng Peng, Ido Sobol, Masayoshi Tomizuka, Kurt Keutzer, Chenfeng Xu, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00623v2.pdf)  
  Keywords: lighting, ar, 3d gaussian  
- **[UrbanCAD: Towards Highly Controllable and Photorealistic 3D Vehicles for Urban Scene Simulation](https://arxiv.org/abs/2411.19292v1)**  
  Authors: Yichong Lu, Yichi Cai, Shangzhan Zhang, Hongyu Zhou, Haoji Hu, Huimin Yu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19292v1.pdf)  
  Keywords: lighting, relighting, high-fidelity, urban scene, autonomous driving, ar  
- **[InstanceGaussian: Appearance-Semantic Joint Gaussian Representation for 3D Instance-Level Perception](https://arxiv.org/abs/2411.19235v1)**  
  Authors: Haijie Li, Yanmin Wu, Jiarui Meng, Qiankun Gao, Zhiyao Zhang, Ronggang Wang, Jian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19235v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lhj-git.github.io/InstanceGaussian/)  
  Keywords: lighting, segmentation, semantic, efficient, gaussian splatting, 3d gaussian, robotics, autonomous driving, understanding, ar  
- **[SuperGaussians: Enhancing Gaussian Splatting Using Primitives with Spatially Varying Colors](https://arxiv.org/abs/2411.18966v1)**  
  Authors: Rui Xu, Wenyue Chen, Jiepeng Wang, Yuan Liu, Peng Wang, Lin Gao, Shiqing Xin, Taku Komura, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18966v1.pdf)  
  Keywords: lighting, compact, geometry, gaussian splatting, ar  
- **[NexusSplats: Efficient 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2411.14514v4)**  
  Authors: Yuzhou Tang, Dejun Xu, Yongjie Hou, Zhenzhong Wang, Min Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.14514v4.pdf)  
  Keywords: lighting, efficient, gaussian splatting, 3d gaussian, ar, mapping  

### SLAM

*Showing the latest 50 out of 158 papers*

- **[Multi-View Pose-Agnostic Change Localization with Zero Labels](https://arxiv.org/abs/2412.03911v1)**  
  Authors: Chamuditha Jayanga Galappaththige, Jason Lai, Lloyd Windrim, Donald Dansereau, Niko Suenderhauf, Dimity Miller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03911v1.pdf)  
  Keywords: lighting, localization, gaussian splatting, 3d gaussian, ar  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: lighting, slam, dynamic, outdoor, localization, gaussian splatting, tracking, nerf, understanding, ar, mapping  
- **[Splats in Splats: Embedding Invisible 3D Watermark within Gaussian Splatting](https://arxiv.org/abs/2412.03121v1)**  
  Authors: Yijia Guo, Wenkai Huang, Yang Li, Gaolei Li, Hang Zhang, Liwen Hu, Jianhua Li, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03121v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://water-gs.github.io.)  
  Keywords: efficient, gaussian splatting, 3d gaussian, fast, ar, 3d reconstruction, mapping  
- **[Towards Rich Emotions in 3D Avatars: A Text-to-3D Avatar Generation Benchmark](https://arxiv.org/abs/2412.02508v1)**  
  Authors: Haidong Xu, Meishan Zhang, Hao Ju, Zhedong Zheng, Hongyuan Zhu, Erik Cambria, Min Zhang, Hao Fei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02508v1.pdf)  
  Keywords: dynamic, human, motion, 3d gaussian, ar, avatar, mapping  
- **[GSGTrack: Gaussian Splatting-Guided Object Pose Tracking from RGB Videos](https://arxiv.org/abs/2412.02267v1)**  
  Authors: Zhiyuan Chen, Fan Lu, Guo Yu, Bin Li, Sanqing Qu, Yuan Huang, Changhong Fu, Guang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02267v1.pdf)  
  Keywords: geometry, gaussian splatting, tracking, 3d gaussian, ar  
- **[CTRL-D: Controllable Dynamic 3D Scene Editing with Personalized 2D Diffusion](https://arxiv.org/abs/2412.01792v1)**  
  Authors: Kai He, Chin-Hsuan Wu, Igor Gilitschenski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01792v1.pdf)  
  Keywords: dynamic, gaussian splatting, tracking, 3d gaussian, ar  
- **[6DOPE-GS: Online 6D Object Pose Estimation using Gaussian Splatting](https://arxiv.org/abs/2412.01543v1)**  
  Authors: Yufeng Jin, Vignesh Prasad, Snehal Jauhri, Mathias Franzius, Georgia Chalvatzaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01543v1.pdf)  
  Keywords: dynamic, efficient, gaussian splatting, tracking, robotics, fast, autonomous driving, ar  
- **[RGBDS-SLAM: A RGB-D Semantic Dense SLAM Based on 3D Multi Level Pyramid Gaussian Splatting](https://arxiv.org/abs/2412.01217v2)**  
  Authors: Zhenzhong Cao, Chenyang Zhao, Qianyi Zhang, Jinzheng Guang, Yinuo Song Jingtai Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01217v2.pdf) | [![GitHub](https://img.shields.io/github/stars/zhenzhongcao/RGBDS-SLAM?style=social)](https://github.com/zhenzhongcao/RGBDS-SLAM)  
  Keywords: slam, semantic, gaussian splatting, 3d gaussian, ar  
- **[FlashSLAM: Accelerated RGB-D SLAM for Real-Time 3D Scene Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2412.00682v1)**  
  Authors: Phu Pham, Damon Conover, Aniket Bera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00682v1.pdf)  
  Keywords: slam, sparse view, efficient, gaussian splatting, tracking, 3d gaussian, fast, ar, 3d reconstruction  
- **[LineGS : 3D Line Segment Representation on 3D Gaussian Splatting](https://arxiv.org/abs/2412.00477v1)**  
  Authors: Chenggang Yang, Yuang Shi, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00477v1.pdf)  
  Keywords: localization, geometry, efficient, face, gaussian splatting, 3d gaussian, ar, 3d reconstruction, mapping  

### Scene Understanding

*Showing the latest 50 out of 186 papers*

- **[Efficient Semantic Splatting for Remote Sensing Multi-view Segmentation](https://arxiv.org/abs/2412.05969v1)**  
  Authors: Zipeng Qi, Hao Chen, Haotian Zhang, Zhengxia Zou, Zhenwei Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05969v1.pdf)  
  Keywords: segmentation, semantic, efficient, gaussian splatting, ar  
- **[EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding](https://arxiv.org/abs/2412.04380v2)**  
  Authors: Yuqi Wu, Wenzhao Zheng, Sicheng Zuo, Yuanhui Huang, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04380v2.pdf) | [![GitHub](https://img.shields.io/github/stars/YkiWu/EmbodiedOcc?style=social)](https://github.com/YkiWu/EmbodiedOcc)  
  Keywords: human, semantic, efficient, 3d gaussian, understanding, ar  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: deformation, dynamic, semantic, face, gaussian splatting, urban scene, 4d, ar  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: lighting, slam, dynamic, outdoor, localization, gaussian splatting, tracking, nerf, understanding, ar, mapping  
- **[Multi-robot autonomous 3D reconstruction using Gaussian splatting with Semantic guidance](https://arxiv.org/abs/2412.02249v1)**  
  Authors: Jing Zeng, Qi Ye, Tianle Liu, Yang Xu, Jin Li, Jinming Xu, Liang Li, Jiming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02249v1.pdf)  
  Keywords: high quality, segmentation, semantic, face, gaussian splatting, 3d gaussian, ar, 3d reconstruction  
- **[SparseLGS: Sparse View Language Embedded Gaussian Splatting](https://arxiv.org/abs/2412.02245v2)**  
  Authors: Jun Hu, Zhang Chen, Zhong Li, Yi Xu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02245v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ustc3dv.github.io/SparseLGS)  
  Keywords: sparse view, semantic, gaussian splatting, understanding, ar  
- **[How to Use Diffusion Priors under Sparse Views?](https://arxiv.org/abs/2412.02225v1)**  
  Authors: Qisen Wang, Yifan Zhao, Jiawei Ma, Jia Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02225v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iCVTEAM/IPSM?style=social)](https://github.com/iCVTEAM/IPSM)  
  Keywords: sparse-view, sparse view, geometry, semantic, gaussian splatting, 3d gaussian, ar, 3d reconstruction  
- **[SparseGrasp: Robotic Grasping via 3D Semantic Gaussian Splatting from Sparse Multi-View RGB Images](https://arxiv.org/abs/2412.02140v1)**  
  Authors: Junqiu Yu, Xinlin Ren, Yongchong Gu, Haitao Lin, Tianyu Wang, Yi Zhu, Hang Xu, Yu-Gang Jiang, Xiangyang Xue, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02140v1.pdf)  
  Keywords: sparse-view, human, semantic, efficient, gaussian splatting, 3d gaussian, fast, ar  
- **[Planar Gaussian Splatting](https://arxiv.org/abs/2412.01931v1)**  
  Authors: Farhad G. Zanjani, Hong Cai, Hanno Ackermann, Leila Mirvakhabova, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01931v1.pdf)  
  Keywords: geometry, segmentation, face, gaussian splatting, neural rendering, fast, ar  
- **[Occam's LGS: A Simple Approach for Language Gaussian Splatting](https://arxiv.org/abs/2412.01807v1)**  
  Authors: Jiahuan Cheng, Jan-Nico Zaech, Luc Van Gool, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01807v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insait-institute.github.io/OccamLGS/)  
  Keywords: compression, semantic, efficient, gaussian splatting, 3d gaussian, understanding, ar, 3d reconstruction  



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