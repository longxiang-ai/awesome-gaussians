# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2024-12-10 00:52:15

## Categories

- [3DGS Surveys](#3dgs-surveys) (19 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (322 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1090 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (369 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (395 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (73 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (365 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (61 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (391 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (181 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (25 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (122 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (158 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (185 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: 3d gaussian, illumination, ar, gaussian splatting, recognition, survey  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: autonomous driving, high-fidelity, semantic, ar, lighting, 3d reconstruction, gaussian splatting, geometry, dynamic, nerf, survey, robotics, compact  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v1)**  
  Authors: Siting Zhu, Guangming Wang, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, nerf, survey, robotics, real-time rendering, understanding  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, lighting, gaussian splatting, nerf, survey  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v1)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, ar, 3d reconstruction, gaussian splatting, nerf, survey, robotics, vr  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: 3d gaussian, survey, ar  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v1)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v1.pdf)  
  Keywords: 3d gaussian, efficient, ar, gaussian splatting, survey, real-time rendering, understanding  
- **[Survey on Fundamental Deep Learning 3D Reconstruction Techniques](https://arxiv.org/abs/2407.08137v1)**  
  Authors: Yonge Bai, LikHang Wong, TszYin Twan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.08137v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, 3d reconstruction, gaussian splatting, nerf, survey  
- **[Panopticon: a telescope for our times](https://arxiv.org/abs/2407.05103v2)**  
  Authors: Will Saunders, Timothy Chin, Michael Goodwin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05103v2.pdf)  
  Keywords: survey, ar  
- **[3DGS.zip: A survey on 3D Gaussian Splatting Compression Methods](https://arxiv.org/abs/2407.09510v4)**  
  Authors: Milena T. Bagdasarian, Paul Knoll, Yi-Hsin Li, Florian Barthel, Anna Hilsmann, Peter Eisert, Wieland Morgenstern  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.09510v4.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://w-m.github.io/3dgs-compression-survey/)  
  Keywords: 3d gaussian, efficient, ar, compression, head, gaussian splatting, survey, compact  

### Acceleration

*Showing the latest 50 out of 322 papers*

- **[Pushing Rendering Boundaries: Hard Gaussian Splatting](https://arxiv.org/abs/2412.04826v1)**  
  Authors: Qingshan Xu, Jiequan Cui, Xuanyu Yi, Yuxuan Wang, Yuan Zhou, Yew-Soon Ong, Hanwang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04826v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, 3d gaussian, ar  
- **[Turbo3D: Ultra-fast Text-to-3D Generation](https://arxiv.org/abs/2412.04470v1)**  
  Authors: Hanzhe Hu, Tianwei Yin, Fujun Luan, Yiwei Hu, Hao Tan, Zexiang Xu, Sai Bi, Shubham Tulsiani, Kai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04470v1.pdf)  
  Keywords: gaussian splatting, fast, efficient, ar  
- **[QUEEN: QUantized Efficient ENcoding of Dynamic Gaussians for Streaming Free-viewpoint Videos](https://arxiv.org/abs/2412.04469v1)**  
  Authors: Sharath Girish, Tianye Li, Amrita Mazumdar, Abhinav Shrivastava, David Luebke, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/queen)  
  Keywords: fast, 3d gaussian, efficient, ar, high quality, dynamic, gaussian splatting  
- **[Monocular Dynamic Gaussian Splatting is Fast and Brittle but Smooth Motion Helps](https://arxiv.org/abs/2412.04457v1)**  
  Authors: Yiqing Liang, Mikhail Okunev, Mikaela Angelina Uy, Runfeng Li, Leonidas Guibas, James Tompkin, Adam W. Harley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04457v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lynl7130.github.io/MonoDyGauBench.github.io/)  
  Keywords: fast, ar, motion, dynamic, gaussian splatting  
- **[InfiniCube: Unbounded and Controllable Dynamic 3D Driving Scene Generation with World-Guided Video Models](https://arxiv.org/abs/2412.03934v1)**  
  Authors: Yifan Lu, Xuanchi Ren, Jiawei Yang, Tianchang Shen, Zhangjie Wu, Jun Gao, Yue Wang, Siheng Chen, Mike Chen, Sanja Fidler, Jiahui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03934v1.pdf)  
  Keywords: 3d gaussian, fast, ar, dynamic  
- **[DGNS: Deformable Gaussian Splatting and Dynamic Neural Surface for Monocular Dynamic 3D Reconstruction](https://arxiv.org/abs/2412.03910v1)**  
  Authors: Xuesong Li, Jinguang Tong, Jie Hong, Vivien Rolland, Lars Petersson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03910v1.pdf)  
  Keywords: fast, ar, geometry, gaussian splatting, dynamic, 3d reconstruction, face  
- **[Splats in Splats: Embedding Invisible 3D Watermark within Gaussian Splatting](https://arxiv.org/abs/2412.03121v1)**  
  Authors: Yijia Guo, Wenkai Huang, Yang Li, Gaolei Li, Hang Zhang, Liwen Hu, Jianhua Li, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03121v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://water-gs.github.io.)  
  Keywords: fast, 3d gaussian, efficient, mapping, ar, 3d reconstruction, gaussian splatting  
- **[Gaussian Splatting Under Attack: Investigating Adversarial Noise in 3D Objects](https://arxiv.org/abs/2412.02803v1)**  
  Authors: Abdurrahman Zeybey, Mehmet Ergezer, Tommy Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02803v1.pdf)  
  Keywords: fast, 3d gaussian, autonomous driving, ar, gaussian splatting, human, robotics  
- **[AniGS: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction](https://arxiv.org/abs/2412.02684v1)**  
  Authors: Lingteng Qiu, Shenhao Zhu, Qi Zuo, Xiaodong Gu, Yuan Dong, Junfei Zhang, Chao Xu, Zhe Li, Weihao Yuan, Liefeng Bo, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02684v1.pdf)  
  Keywords: efficient, ar, 3d reconstruction, gaussian splatting, animation, human, avatar, real-time rendering, 4d  
- **[SparseGrasp: Robotic Grasping via 3D Semantic Gaussian Splatting from Sparse Multi-View RGB Images](https://arxiv.org/abs/2412.02140v1)**  
  Authors: Junqiu Yu, Xinlin Ren, Yongchong Gu, Haitao Lin, Tianyu Wang, Yi Zhu, Hang Xu, Yu-Gang Jiang, Xiangyang Xue, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02140v1.pdf)  
  Keywords: fast, 3d gaussian, efficient, semantic, ar, gaussian splatting, human, sparse-view  

### Applications

*Showing the latest 50 out of 1090 papers*

- **[Extrapolated Urban View Synthesis Benchmark](https://arxiv.org/abs/2412.05256v1)**  
  Authors: Xiangyu Han, Zhen Jia, Boyi Li, Yan Wang, Boris Ivanovic, Yurong You, Lingjie Liu, Yue Wang, Marco Pavone, Chen Feng, Yiming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05256v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, geometry, gaussian splatting, robotics  
- **[MixedGaussianAvatar: Realistically and Geometrically Accurate Head Avatar via Mixed 2D-3D Gaussian Splatting](https://arxiv.org/abs/2412.04955v1)**  
  Authors: Peng Chen, Xiaobao Wei, Qingpo Wuwu, Xinyi Wang, Xingyu Xiao, Ming Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04955v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ChenVoid/MGA?style=social)](https://github.com/ChenVoid/MGA/)  
  Keywords: 3d gaussian, high-fidelity, ar, head, face, gaussian splatting, nerf, avatar  
- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: 3d gaussian, ar, head, large scene, dynamic, gaussian splatting  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v1.pdf)  
  Keywords: 3d gaussian, efficient, ar, gaussian splatting, ray tracing  
- **[Pushing Rendering Boundaries: Hard Gaussian Splatting](https://arxiv.org/abs/2412.04826v1)**  
  Authors: Qingshan Xu, Jiequan Cui, Xuanyu Yi, Yuxuan Wang, Yuan Zhou, Yew-Soon Ong, Hanwang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04826v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, 3d gaussian, ar  
- **[Turbo3D: Ultra-fast Text-to-3D Generation](https://arxiv.org/abs/2412.04470v1)**  
  Authors: Hanzhe Hu, Tianwei Yin, Fujun Luan, Yiwei Hu, Hao Tan, Zexiang Xu, Sai Bi, Shubham Tulsiani, Kai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04470v1.pdf)  
  Keywords: gaussian splatting, fast, efficient, ar  
- **[QUEEN: QUantized Efficient ENcoding of Dynamic Gaussians for Streaming Free-viewpoint Videos](https://arxiv.org/abs/2412.04469v1)**  
  Authors: Sharath Girish, Tianye Li, Amrita Mazumdar, Abhinav Shrivastava, David Luebke, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/queen)  
  Keywords: fast, 3d gaussian, efficient, ar, high quality, dynamic, gaussian splatting  
- **[Sparse Voxels Rasterization: Real-time High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2412.04459v1)**  
  Authors: Cheng Sun, Jaesung Choe, Charles Loop, Wei-Chiu Ma, Yu-Chiang Frank Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04459v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, efficient, ar, dynamic, gaussian splatting, 4d  
- **[Monocular Dynamic Gaussian Splatting is Fast and Brittle but Smooth Motion Helps](https://arxiv.org/abs/2412.04457v1)**  
  Authors: Yiqing Liang, Mikhail Okunev, Mikaela Angelina Uy, Runfeng Li, Leonidas Guibas, James Tompkin, Adam W. Harley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04457v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lynl7130.github.io/MonoDyGauBench.github.io/)  
  Keywords: fast, ar, motion, dynamic, gaussian splatting  
- **[PBDyG: Position Based Dynamic Gaussians for Motion-Aware Clothed Human Avatars](https://arxiv.org/abs/2412.04433v1)**  
  Authors: Shota Sasaki, Jane Wu, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04433v1.pdf)  
  Keywords: 3d gaussian, ar, motion, dynamic, gaussian splatting, body, human, deformation, avatar  

### Avatar Generation

*Showing the latest 50 out of 369 papers*

- **[MixedGaussianAvatar: Realistically and Geometrically Accurate Head Avatar via Mixed 2D-3D Gaussian Splatting](https://arxiv.org/abs/2412.04955v1)**  
  Authors: Peng Chen, Xiaobao Wei, Qingpo Wuwu, Xinyi Wang, Xingyu Xiao, Ming Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04955v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ChenVoid/MGA?style=social)](https://github.com/ChenVoid/MGA/)  
  Keywords: 3d gaussian, high-fidelity, ar, head, face, gaussian splatting, nerf, avatar  
- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: 3d gaussian, ar, head, large scene, dynamic, gaussian splatting  
- **[PBDyG: Position Based Dynamic Gaussians for Motion-Aware Clothed Human Avatars](https://arxiv.org/abs/2412.04433v1)**  
  Authors: Shota Sasaki, Jane Wu, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04433v1.pdf)  
  Keywords: 3d gaussian, ar, motion, dynamic, gaussian splatting, body, human, deformation, avatar  
- **[EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding](https://arxiv.org/abs/2412.04380v2)**  
  Authors: Yuqi Wu, Wenzhao Zheng, Sicheng Zuo, Yuanhui Huang, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04380v2.pdf) | [![GitHub](https://img.shields.io/github/stars/YkiWu/EmbodiedOcc?style=social)](https://github.com/YkiWu/EmbodiedOcc)  
  Keywords: 3d gaussian, semantic, efficient, ar, human, understanding  
- **[DGNS: Deformable Gaussian Splatting and Dynamic Neural Surface for Monocular Dynamic 3D Reconstruction](https://arxiv.org/abs/2412.03910v1)**  
  Authors: Xuesong Li, Jinguang Tong, Jie Hong, Vivien Rolland, Lars Petersson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03910v1.pdf)  
  Keywords: fast, ar, geometry, gaussian splatting, dynamic, 3d reconstruction, face  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: semantic, ar, dynamic, gaussian splatting, face, urban scene, deformation, 4d  
- **[2DGS-Room: Seed-Guided 2D Gaussian Splatting with Geometric Constrains for High-Fidelity Indoor Scene Reconstruction](https://arxiv.org/abs/2412.03428v1)**  
  Authors: Wanting Zhang, Haodong Xiang, Zhichao Liao, Xiansong Lai, Xinghui Li, Long Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03428v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, face, gaussian splatting, dynamic  
- **[Volumetrically Consistent 3D Gaussian Rasterization](https://arxiv.org/abs/2412.03378v1)**  
  Authors: Chinmay Talegaonkar, Yash Belhe, Ravi Ramamoorthi, Nicholas Antipa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03378v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, face  
- **[Gaussian Splatting Under Attack: Investigating Adversarial Noise in 3D Objects](https://arxiv.org/abs/2412.02803v1)**  
  Authors: Abdurrahman Zeybey, Mehmet Ergezer, Tommy Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02803v1.pdf)  
  Keywords: fast, 3d gaussian, autonomous driving, ar, gaussian splatting, human, robotics  
- **[AniGS: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction](https://arxiv.org/abs/2412.02684v1)**  
  Authors: Lingteng Qiu, Shenhao Zhu, Qi Zuo, Xiaodong Gu, Yuan Dong, Junfei Zhang, Chao Xu, Zhe Li, Weihao Yuan, Liefeng Bo, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02684v1.pdf)  
  Keywords: efficient, ar, 3d reconstruction, gaussian splatting, animation, human, avatar, real-time rendering, 4d  

### Dynamic Scene

*Showing the latest 50 out of 395 papers*

- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: 3d gaussian, ar, head, large scene, dynamic, gaussian splatting  
- **[QUEEN: QUantized Efficient ENcoding of Dynamic Gaussians for Streaming Free-viewpoint Videos](https://arxiv.org/abs/2412.04469v1)**  
  Authors: Sharath Girish, Tianye Li, Amrita Mazumdar, Abhinav Shrivastava, David Luebke, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/queen)  
  Keywords: fast, 3d gaussian, efficient, ar, high quality, dynamic, gaussian splatting  
- **[Sparse Voxels Rasterization: Real-time High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2412.04459v1)**  
  Authors: Cheng Sun, Jaesung Choe, Charles Loop, Wei-Chiu Ma, Yu-Chiang Frank Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04459v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, efficient, ar, dynamic, gaussian splatting, 4d  
- **[Monocular Dynamic Gaussian Splatting is Fast and Brittle but Smooth Motion Helps](https://arxiv.org/abs/2412.04457v1)**  
  Authors: Yiqing Liang, Mikhail Okunev, Mikaela Angelina Uy, Runfeng Li, Leonidas Guibas, James Tompkin, Adam W. Harley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04457v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lynl7130.github.io/MonoDyGauBench.github.io/)  
  Keywords: fast, ar, motion, dynamic, gaussian splatting  
- **[PBDyG: Position Based Dynamic Gaussians for Motion-Aware Clothed Human Avatars](https://arxiv.org/abs/2412.04433v1)**  
  Authors: Shota Sasaki, Jane Wu, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04433v1.pdf)  
  Keywords: 3d gaussian, ar, motion, dynamic, gaussian splatting, body, human, deformation, avatar  
- **[InfiniCube: Unbounded and Controllable Dynamic 3D Driving Scene Generation with World-Guided Video Models](https://arxiv.org/abs/2412.03934v1)**  
  Authors: Yifan Lu, Xuanchi Ren, Jiawei Yang, Tianchang Shen, Zhangjie Wu, Jun Gao, Yue Wang, Siheng Chen, Mike Chen, Sanja Fidler, Jiahui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03934v1.pdf)  
  Keywords: 3d gaussian, fast, ar, dynamic  
- **[DGNS: Deformable Gaussian Splatting and Dynamic Neural Surface for Monocular Dynamic 3D Reconstruction](https://arxiv.org/abs/2412.03910v1)**  
  Authors: Xuesong Li, Jinguang Tong, Jie Hong, Vivien Rolland, Lars Petersson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03910v1.pdf)  
  Keywords: fast, ar, geometry, gaussian splatting, dynamic, 3d reconstruction, face  
- **[Feed-Forward Bullet-Time Reconstruction of Dynamic Scenes from Monocular Videos](https://arxiv.org/abs/2412.03526v1)**  
  Authors: Hanxue Liang, Jiawei Ren, Ashkan Mirzaei, Antonio Torralba, Ziwei Liu, Igor Gilitschenski, Sanja Fidler, Cengiz Oztireli, Huan Ling, Zan Gojcic, Jiahui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03526v1.pdf)  
  Keywords: 3d gaussian, ar, motion, dynamic, gaussian splatting  
- **[Dense Scene Reconstruction from Light-Field Images Affected by Rolling Shutter](https://arxiv.org/abs/2412.03518v1)**  
  Authors: Hermes McGriff, Renato Martins, Nicolas Andreff, Cedric Demonceaux  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03518v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ICB-Vision-AI/DenseRSLF?style=social)](https://github.com/ICB-Vision-AI/DenseRSLF)  
  Keywords: ar, motion, deformation  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: semantic, ar, dynamic, gaussian splatting, face, urban scene, deformation, 4d  

### Few-shot

*Showing the latest 50 out of 73 papers*

- **[SparseLGS: Sparse View Language Embedded Gaussian Splatting](https://arxiv.org/abs/2412.02245v2)**  
  Authors: Jun Hu, Zhang Chen, Zhong Li, Yi Xu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02245v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ustc3dv.github.io/SparseLGS)  
  Keywords: semantic, ar, sparse view, gaussian splatting, understanding  
- **[How to Use Diffusion Priors under Sparse Views?](https://arxiv.org/abs/2412.02225v1)**  
  Authors: Qisen Wang, Yifan Zhao, Jiawei Ma, Jia Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02225v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iCVTEAM/IPSM?style=social)](https://github.com/iCVTEAM/IPSM)  
  Keywords: 3d gaussian, semantic, ar, sparse view, geometry, gaussian splatting, 3d reconstruction, sparse-view  
- **[SparseGrasp: Robotic Grasping via 3D Semantic Gaussian Splatting from Sparse Multi-View RGB Images](https://arxiv.org/abs/2412.02140v1)**  
  Authors: Junqiu Yu, Xinlin Ren, Yongchong Gu, Haitao Lin, Tianyu Wang, Yi Zhu, Hang Xu, Yu-Gang Jiang, Xiangyang Xue, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02140v1.pdf)  
  Keywords: fast, 3d gaussian, efficient, semantic, ar, gaussian splatting, human, sparse-view  
- **[DynSUP: Dynamic Gaussian Splatting from An Unposed Image Pair](https://arxiv.org/abs/2412.00851v1)**  
  Authors: Weihang Li, Weirong Chen, Shenhan Qian, Jiajie Chen, Daniel Cremers, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00851v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://colin-de.github.io/DynSUP/.)  
  Keywords: 3d gaussian, high-fidelity, ar, sparse view, motion, dynamic, gaussian splatting  
- **[FlashSLAM: Accelerated RGB-D SLAM for Real-Time 3D Scene Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2412.00682v1)**  
  Authors: Phu Pham, Damon Conover, Aniket Bera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00682v1.pdf)  
  Keywords: fast, 3d gaussian, efficient, slam, ar, sparse view, 3d reconstruction, gaussian splatting, tracking  
- **[NovelGS: Consistent Novel-view Denoising via Large Gaussian Reconstruction Model](https://arxiv.org/abs/2411.16779v1)**  
  Authors: Jinpeng Liu, Jiale Xu, Weihao Cheng, Yiming Gao, Xintao Wang, Ying Shan, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16779v1.pdf)  
  Keywords: fast, 3d gaussian, ar, gaussian splatting, sparse-view  
- **[GPS-Gaussian+: Generalizable Pixel-wise 3D Gaussian Splatting for Real-Time Human-Scene Rendering from Sparse Views](https://arxiv.org/abs/2411.11363v1)**  
  Authors: Boyao Zhou, Shunyuan Zheng, Hanzhang Tu, Ruizhi Shao, Boning Liu, Shengping Zhang, Liqiang Nie, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.11363v1.pdf)  
  Keywords: 3d gaussian, ar, sparse view, geometry, gaussian splatting, human, sparse-view, real-time rendering  
- **[SPARS3R: Semantic Prior Alignment and Regularization for Sparse 3D Reconstruction](https://arxiv.org/abs/2411.12592v1)**  
  Authors: Yutao Tang, Yuxiang Guo, Deming Li, Cheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12592v1.pdf)  
  Keywords: semantic, ar, motion, 3d reconstruction, sparse-view  
- **[4D Gaussian Splatting in the Wild with Uncertainty-Aware Regularization](https://arxiv.org/abs/2411.08879v1)**  
  Authors: Mijeong Kim, Jongwoo Lim, Bohyung Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.08879v1.pdf)  
  Keywords: fast, ar, few-shot, motion, dynamic, gaussian splatting, 4d  
- **[SplatFormer: Point Transformer for Robust 3D Gaussian Splatting](https://arxiv.org/abs/2411.06390v2)**  
  Authors: Yutong Chen, Marko Mihajlovic, Xiyi Chen, Yiming Wang, Sergey Prokudin, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.06390v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, sparse view, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 365 papers*

- **[Extrapolated Urban View Synthesis Benchmark](https://arxiv.org/abs/2412.05256v1)**  
  Authors: Xiangyu Han, Zhen Jia, Boyi Li, Yan Wang, Boris Ivanovic, Yurong You, Lingjie Liu, Yue Wang, Marco Pavone, Chen Feng, Yiming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05256v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, geometry, gaussian splatting, robotics  
- **[DGNS: Deformable Gaussian Splatting and Dynamic Neural Surface for Monocular Dynamic 3D Reconstruction](https://arxiv.org/abs/2412.03910v1)**  
  Authors: Xuesong Li, Jinguang Tong, Jie Hong, Vivien Rolland, Lars Petersson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03910v1.pdf)  
  Keywords: fast, ar, geometry, gaussian splatting, dynamic, 3d reconstruction, face  
- **[Splats in Splats: Embedding Invisible 3D Watermark within Gaussian Splatting](https://arxiv.org/abs/2412.03121v1)**  
  Authors: Yijia Guo, Wenkai Huang, Yang Li, Gaolei Li, Hang Zhang, Liwen Hu, Jianhua Li, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03121v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://water-gs.github.io.)  
  Keywords: fast, 3d gaussian, efficient, mapping, ar, 3d reconstruction, gaussian splatting  
- **[RoDyGS: Robust Dynamic Gaussian Splatting for Casual Videos](https://arxiv.org/abs/2412.03077v1)**  
  Authors: Yoonwoo Jeong, Junmyeong Lee, Hoseung Choi, Minsu Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03077v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rodygs.github.io/.)  
  Keywords: high-fidelity, ar, motion, dynamic, gaussian splatting, geometry  
- **[AniGS: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction](https://arxiv.org/abs/2412.02684v1)**  
  Authors: Lingteng Qiu, Shenhao Zhu, Qi Zuo, Xiaodong Gu, Yuan Dong, Junfei Zhang, Chao Xu, Zhe Li, Weihao Yuan, Liefeng Bo, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02684v1.pdf)  
  Keywords: efficient, ar, 3d reconstruction, gaussian splatting, animation, human, avatar, real-time rendering, 4d  
- **[Realistic Surgical Simulation from Monocular Videos](https://arxiv.org/abs/2412.02359v1)**  
  Authors: Kailing Wang, Chen Yang, Keyang Zhao, Xiaokang Yang, Wei Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02359v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://namaenashibot.github.io/SurgiSim/.)  
  Keywords: 3d gaussian, high-fidelity, ar, motion, dynamic, geometry, deformation  
- **[GSGTrack: Gaussian Splatting-Guided Object Pose Tracking from RGB Videos](https://arxiv.org/abs/2412.02267v1)**  
  Authors: Zhiyuan Chen, Fan Lu, Guo Yu, Bin Li, Sanqing Qu, Yuan Huang, Changhong Fu, Guang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02267v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting, tracking  
- **[Multi-robot autonomous 3D reconstruction using Gaussian splatting with Semantic guidance](https://arxiv.org/abs/2412.02249v1)**  
  Authors: Jing Zeng, Qi Ye, Tianle Liu, Yang Xu, Jin Li, Jinming Xu, Liang Li, Jiming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02249v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, high quality, face, gaussian splatting, 3d reconstruction, segmentation  
- **[How to Use Diffusion Priors under Sparse Views?](https://arxiv.org/abs/2412.02225v1)**  
  Authors: Qisen Wang, Yifan Zhao, Jiawei Ma, Jia Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02225v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iCVTEAM/IPSM?style=social)](https://github.com/iCVTEAM/IPSM)  
  Keywords: 3d gaussian, semantic, ar, sparse view, geometry, gaussian splatting, 3d reconstruction, sparse-view  
- **[Gaussian Object Carver: Object-Compositional Gaussian Splatting with surfaces completion](https://arxiv.org/abs/2412.02075v1)**  
  Authors: Liu Liu, Xinjie Wang, Jiaxiong Qiu, Tianwei Lin, Xiaolin Zhou, Zhizhong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02075v1.pdf)  
  Keywords: 3d gaussian, efficient, ar, face, gaussian splatting, geometry, vr  

### Large Scene

*Showing the latest 50 out of 61 papers*

- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: 3d gaussian, ar, head, large scene, dynamic, gaussian splatting  
- **[HybridGS: Decoupling Transients and Statics with 2D and 3D Gaussian Splatting](https://arxiv.org/abs/2412.03844v1)**  
  Authors: Jingyu Lin, Jiaqi Gu, Lubin Fan, Bojian Wu, Yujing Lou, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03844v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, outdoor, ar  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: semantic, ar, dynamic, gaussian splatting, face, urban scene, deformation, 4d  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: slam, mapping, outdoor, ar, lighting, localization, dynamic, gaussian splatting, nerf, tracking, understanding  
- **[Horizon-GS: Unified 3D Gaussian Splatting for Large-Scale Aerial-to-Ground Scenes](https://arxiv.org/abs/2412.01745v1)**  
  Authors: Lihan Jiang, Kerui Ren, Mulin Yu, Linning Xu, Junting Dong, Tao Lu, Feng Zhao, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01745v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, gaussian splatting, urban scene  
- **[Tortho-Gaussian: Splatting True Digital Orthophoto Maps](https://arxiv.org/abs/2411.19594v1)**  
  Authors: Xin Wang, Wendi Zhang, Hong Xie, Haibin Ai, Qiangqiang Yuan, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19594v1.pdf)  
  Keywords: 3d gaussian, ar, face, gaussian splatting, urban scene  
- **[UrbanCAD: Towards Highly Controllable and Photorealistic 3D Vehicles for Urban Scene Simulation](https://arxiv.org/abs/2411.19292v1)**  
  Authors: Yichong Lu, Yichi Cai, Shangzhan Zhang, Hongyu Zhou, Haoji Hu, Huimin Yu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19292v1.pdf)  
  Keywords: autonomous driving, high-fidelity, ar, relighting, lighting, urban scene  
- **[Unleashing the Power of Data Synthesis in Visual Localization](https://arxiv.org/abs/2412.00138v1)**  
  Authors: Sihang Li, Siqi Tan, Bowen Chang, Jing Zhang, Chen Feng, Yiming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ai4ce.github.io/RAP/)  
  Keywords: 3d gaussian, fast, outdoor, ar, localization, dynamic, robotics  
- **[UniGaussian: Driving Scene Reconstruction from Multiple Camera Models via Unified Gaussian Representations](https://arxiv.org/abs/2411.15355v1)**  
  Authors: Yuan Ren, Guile Wu, Runhao Li, Zheyuan Yang, Yibo Liu, Xingxin Chen, Tongtong Cao, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15355v1.pdf)  
  Keywords: 3d gaussian, fast, semantic, autonomous driving, ar, gaussian splatting, urban scene, real-time rendering, understanding  
- **[LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments](https://arxiv.org/abs/2411.12185v1)**  
  Authors: Renxiang Xiao, Wei Liu, Yushuai Chen, Liang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12185v1.pdf)  
  Keywords: fast, 3d gaussian, semantic, slam, mapping, outdoor, ar, localization, gaussian splatting, segmentation, tracking  

### Model Compression

*Showing the latest 50 out of 391 papers*

- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v1.pdf)  
  Keywords: 3d gaussian, efficient, ar, gaussian splatting, ray tracing  
- **[Turbo3D: Ultra-fast Text-to-3D Generation](https://arxiv.org/abs/2412.04470v1)**  
  Authors: Hanzhe Hu, Tianwei Yin, Fujun Luan, Yiwei Hu, Hao Tan, Zexiang Xu, Sai Bi, Shubham Tulsiani, Kai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04470v1.pdf)  
  Keywords: gaussian splatting, fast, efficient, ar  
- **[QUEEN: QUantized Efficient ENcoding of Dynamic Gaussians for Streaming Free-viewpoint Videos](https://arxiv.org/abs/2412.04469v1)**  
  Authors: Sharath Girish, Tianye Li, Amrita Mazumdar, Abhinav Shrivastava, David Luebke, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/queen)  
  Keywords: fast, 3d gaussian, efficient, ar, high quality, dynamic, gaussian splatting  
- **[Sparse Voxels Rasterization: Real-time High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2412.04459v1)**  
  Authors: Cheng Sun, Jaesung Choe, Charles Loop, Wei-Chiu Ma, Yu-Chiang Frank Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04459v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, efficient, ar, dynamic, gaussian splatting, 4d  
- **[EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding](https://arxiv.org/abs/2412.04380v2)**  
  Authors: Yuqi Wu, Wenzhao Zheng, Sicheng Zuo, Yuanhui Huang, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04380v2.pdf) | [![GitHub](https://img.shields.io/github/stars/YkiWu/EmbodiedOcc?style=social)](https://github.com/YkiWu/EmbodiedOcc)  
  Keywords: 3d gaussian, semantic, efficient, ar, human, understanding  
- **[Splats in Splats: Embedding Invisible 3D Watermark within Gaussian Splatting](https://arxiv.org/abs/2412.03121v1)**  
  Authors: Yijia Guo, Wenkai Huang, Yang Li, Gaolei Li, Hang Zhang, Liwen Hu, Jianhua Li, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03121v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://water-gs.github.io.)  
  Keywords: fast, 3d gaussian, efficient, mapping, ar, 3d reconstruction, gaussian splatting  
- **[AniGS: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction](https://arxiv.org/abs/2412.02684v1)**  
  Authors: Lingteng Qiu, Shenhao Zhu, Qi Zuo, Xiaodong Gu, Yuan Dong, Junfei Zhang, Chao Xu, Zhe Li, Weihao Yuan, Liefeng Bo, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02684v1.pdf)  
  Keywords: efficient, ar, 3d reconstruction, gaussian splatting, animation, human, avatar, real-time rendering, 4d  
- **[RelayGS: Reconstructing Dynamic Scenes with Large-Scale and Complex Motions via Relay Gaussians](https://arxiv.org/abs/2412.02493v1)**  
  Authors: Qiankun Gao, Yanmin Wu, Chengxiang Wen, Jiarui Meng, Luyang Tang, Jie Chen, Ronggang Wang, Jian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02493v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gqk/RelayGS?style=social)](https://github.com/gqk/RelayGS)  
  Keywords: 3d gaussian, ar, motion, dynamic, gaussian splatting, compact, 4d  
- **[TimeWalker: Personalized Neural Space for Lifelong Head Avatars](https://arxiv.org/abs/2412.02421v1)**  
  Authors: Dongwei Pan, Yang Li, Hongsheng Li, Kwan-Yee Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02421v1.pdf)  
  Keywords: ar, head, motion, dynamic, gaussian splatting, animation, human, deformation, avatar, compact  
- **[SparseGrasp: Robotic Grasping via 3D Semantic Gaussian Splatting from Sparse Multi-View RGB Images](https://arxiv.org/abs/2412.02140v1)**  
  Authors: Junqiu Yu, Xinlin Ren, Yongchong Gu, Haitao Lin, Tianyu Wang, Yi Zhu, Hang Xu, Yu-Gang Jiang, Xiangyang Xue, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02140v1.pdf)  
  Keywords: fast, 3d gaussian, efficient, semantic, ar, gaussian splatting, human, sparse-view  

### Quality Enhancement

*Showing the latest 50 out of 181 papers*

- **[MixedGaussianAvatar: Realistically and Geometrically Accurate Head Avatar via Mixed 2D-3D Gaussian Splatting](https://arxiv.org/abs/2412.04955v1)**  
  Authors: Peng Chen, Xiaobao Wei, Qingpo Wuwu, Xinyi Wang, Xingyu Xiao, Ming Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04955v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ChenVoid/MGA?style=social)](https://github.com/ChenVoid/MGA/)  
  Keywords: 3d gaussian, high-fidelity, ar, head, face, gaussian splatting, nerf, avatar  
- **[QUEEN: QUantized Efficient ENcoding of Dynamic Gaussians for Streaming Free-viewpoint Videos](https://arxiv.org/abs/2412.04469v1)**  
  Authors: Sharath Girish, Tianye Li, Amrita Mazumdar, Abhinav Shrivastava, David Luebke, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/queen)  
  Keywords: fast, 3d gaussian, efficient, ar, high quality, dynamic, gaussian splatting  
- **[Sparse Voxels Rasterization: Real-time High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2412.04459v1)**  
  Authors: Cheng Sun, Jaesung Choe, Charles Loop, Wei-Chiu Ma, Yu-Chiang Frank Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04459v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, efficient, ar, dynamic, gaussian splatting, 4d  
- **[2DGS-Room: Seed-Guided 2D Gaussian Splatting with Geometric Constrains for High-Fidelity Indoor Scene Reconstruction](https://arxiv.org/abs/2412.03428v1)**  
  Authors: Wanting Zhang, Haodong Xiang, Zhichao Liao, Xiansong Lai, Xinghui Li, Long Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03428v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, face, gaussian splatting, dynamic  
- **[RoDyGS: Robust Dynamic Gaussian Splatting for Casual Videos](https://arxiv.org/abs/2412.03077v1)**  
  Authors: Yoonwoo Jeong, Junmyeong Lee, Hoseung Choi, Minsu Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03077v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rodygs.github.io/.)  
  Keywords: high-fidelity, ar, motion, dynamic, gaussian splatting, geometry  
- **[Realistic Surgical Simulation from Monocular Videos](https://arxiv.org/abs/2412.02359v1)**  
  Authors: Kailing Wang, Chen Yang, Keyang Zhao, Xiaokang Yang, Wei Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02359v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://namaenashibot.github.io/SurgiSim/.)  
  Keywords: 3d gaussian, high-fidelity, ar, motion, dynamic, geometry, deformation  
- **[Multi-robot autonomous 3D reconstruction using Gaussian splatting with Semantic guidance](https://arxiv.org/abs/2412.02249v1)**  
  Authors: Jing Zeng, Qi Ye, Tianle Liu, Yang Xu, Jin Li, Jinming Xu, Liang Li, Jiming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02249v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, high quality, face, gaussian splatting, 3d reconstruction, segmentation  
- **[HDGS: Textured 2D Gaussian Splatting for Enhanced Scene Rendering](https://arxiv.org/abs/2412.01823v1)**  
  Authors: Yunzhou Song, Heguang Lin, Jiahui Lei, Lingjie Liu, Kostas Daniilidis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01823v1.pdf)  
  Keywords: high-fidelity, ar, neural rendering, face, gaussian splatting, geometry  
- **[Horizon-GS: Unified 3D Gaussian Splatting for Large-Scale Aerial-to-Ground Scenes](https://arxiv.org/abs/2412.01745v1)**  
  Authors: Lihan Jiang, Kerui Ren, Mulin Yu, Linning Xu, Junting Dong, Tao Lu, Feng Zhao, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01745v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, gaussian splatting, urban scene  
- **[Driving Scene Synthesis on Free-form Trajectories with Generative Prior](https://arxiv.org/abs/2412.01717v1)**  
  Authors: Zeyu Yang, Zijie Pan, Yuankun Yang, Xiatian Zhu, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01717v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, ar, face  

### Ray Tracing

- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v1.pdf)  
  Keywords: 3d gaussian, efficient, ar, gaussian splatting, ray tracing  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v1)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, ray tracing  
- **[URAvatar: Universal Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2410.24223v1)**  
  Authors: Junxuan Li, Chen Cao, Gabriel Schwartz, Rawal Khirodkar, Christian Richardt, Tomas Simon, Yaser Sheikh, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24223v1.pdf)  
  Keywords: 3d gaussian, efficient, illumination, global illumination, ar, head, light transport, human, avatar, relightable, real-time rendering  
- **[Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization](https://arxiv.org/abs/2410.16978v1)**  
  Authors: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, Ralf Gutjahr, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16978v1.pdf)  
  Keywords: efficient, ar, head, medical, path tracing, gaussian splatting, understanding, vr  
- **[GS^3: Efficient Relighting with Triple Gaussian Splatting](https://arxiv.org/abs/2410.11419v1)**  
  Authors: Zoubin Bi, Yixin Zeng, Chong Zeng, Fan Pei, Xiang Feng, Kun Zhou, Hongzhi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11419v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://GSrelight.github.io/.)  
  Keywords: efficient, illumination, global illumination, ar, relighting, lighting, geometry, gaussian splatting, shadow  
- **[RGM: Reconstructing High-fidelity 3D Car Assets with Relightable 3D-GS Generative Model from a Single Image](https://arxiv.org/abs/2410.08181v1)**  
  Authors: Xiaoxue Chen, Jv Zheng, Hao Huang, Haoran Xu, Weihao Gu, Kangliang Chen, He xiang, Huan-ang Gao, Hao Zhao, Guyue Zhou, Yaqin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08181v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, autonomous driving, global illumination, illumination, ar, relighting, lighting, geometry, nerf, relightable  
- **[6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering](https://arxiv.org/abs/2410.04974v2)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04974v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/6dgs/)  
  Keywords: 3d gaussian, ar, high quality, gaussian splatting, nerf, real-time rendering, ray tracing  
- **[GI-GS: Global Illumination Decomposition on Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2410.02619v1)**  
  Authors: Hongze Chen, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.02619v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, efficient, global illumination, illumination, ar, relighting, lighting, lightweight, path tracing, geometry, gaussian splatting, shadow  
- **[EVER: Exact Volumetric Ellipsoid Rendering for Real-time View Synthesis](https://arxiv.org/abs/2410.01804v5)**  
  Authors: Alexander Mai, Peter Hedman, George Kopanas, Dor Verbin, David Futschik, Qiangeng Xu, Falko Kuester, Jonathan T. Barron, Yinda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.01804v5.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, nerf, ray tracing  
- **[SpikeGS: Learning 3D Gaussian Fields from Continuous Spike Stream](https://arxiv.org/abs/2409.15176v5)**  
  Authors: Jinze Yu, Xin Peng, Zhengda Lu, Laurent Kneip, Yiqun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.15176v5.pdf) | [![GitHub](https://img.shields.io/github/stars/520jz/SpikeGS?style=social)](https://github.com/520jz/SpikeGS)  
  Keywords: 3d gaussian, illumination, ar, lighting, dynamic, real-time rendering, ray marching  

### Relighting

*Showing the latest 50 out of 122 papers*

- **[Extrapolated Urban View Synthesis Benchmark](https://arxiv.org/abs/2412.05256v1)**  
  Authors: Xiangyu Han, Zhen Jia, Boyi Li, Yan Wang, Boris Ivanovic, Yurong You, Lingjie Liu, Yue Wang, Marco Pavone, Chen Feng, Yiming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05256v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, geometry, gaussian splatting, robotics  
- **[Multi-View Pose-Agnostic Change Localization with Zero Labels](https://arxiv.org/abs/2412.03911v1)**  
  Authors: Chamuditha Jayanga Galappaththige, Jason Lai, Lloyd Windrim, Donald Dansereau, Niko Suenderhauf, Dimity Miller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03911v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, localization, gaussian splatting  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: slam, mapping, outdoor, ar, lighting, localization, dynamic, gaussian splatting, nerf, tracking, understanding  
- **[HUGSIM: A Real-Time, Photo-Realistic and Closed-Loop Simulator for Autonomous Driving](https://arxiv.org/abs/2412.01718v1)**  
  Authors: Hongyu Zhou, Longzhong Lin, Jiabao Wang, Yichong Lu, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01718v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, ar, lighting, dynamic, gaussian splatting  
- **[Ref-GS: Directional Factorization for 2D Gaussian Splatting](https://arxiv.org/abs/2412.00905v1)**  
  Authors: Youjia Zhang, Anpei Chen, Yumin Wan, Zikai Song, Junqing Yu, Yawei Luo, Wei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00905v1.pdf)  
  Keywords: efficient, ar, lighting, head, face, gaussian splatting, geometry  
- **[A Lesson in Splats: Teacher-Guided Diffusion for 3D Gaussian Splats Generation with 2D Supervision](https://arxiv.org/abs/2412.00623v1)**  
  Authors: Chensheng Peng, Ido Sobol, Masayoshi Tomizuka, Kurt Keutzer, Chenfeng Xu, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00623v1.pdf)  
  Keywords: 3d gaussian, lighting, ar  
- **[UrbanCAD: Towards Highly Controllable and Photorealistic 3D Vehicles for Urban Scene Simulation](https://arxiv.org/abs/2411.19292v1)**  
  Authors: Yichong Lu, Yichi Cai, Shangzhan Zhang, Hongyu Zhou, Haoji Hu, Huimin Yu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19292v1.pdf)  
  Keywords: autonomous driving, high-fidelity, ar, relighting, lighting, urban scene  
- **[InstanceGaussian: Appearance-Semantic Joint Gaussian Representation for 3D Instance-Level Perception](https://arxiv.org/abs/2411.19235v1)**  
  Authors: Haijie Li, Yanmin Wu, Jiarui Meng, Qiankun Gao, Zhiyao Zhang, Ronggang Wang, Jian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19235v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lhj-git.github.io/InstanceGaussian/)  
  Keywords: 3d gaussian, semantic, efficient, autonomous driving, ar, lighting, gaussian splatting, segmentation, robotics, understanding  
- **[SuperGaussians: Enhancing Gaussian Splatting Using Primitives with Spatially Varying Colors](https://arxiv.org/abs/2411.18966v1)**  
  Authors: Rui Xu, Wenyue Chen, Jiepeng Wang, Yuan Liu, Peng Wang, Lin Gao, Shiqing Xin, Taku Komura, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18966v1.pdf)  
  Keywords: ar, lighting, geometry, gaussian splatting, compact  
- **[NexusSplats: Efficient 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2411.14514v4)**  
  Authors: Yuzhou Tang, Dejun Xu, Yongjie Hou, Zhenzhong Wang, Min Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.14514v4.pdf)  
  Keywords: 3d gaussian, efficient, mapping, ar, lighting, gaussian splatting  

### SLAM

*Showing the latest 50 out of 158 papers*

- **[Multi-View Pose-Agnostic Change Localization with Zero Labels](https://arxiv.org/abs/2412.03911v1)**  
  Authors: Chamuditha Jayanga Galappaththige, Jason Lai, Lloyd Windrim, Donald Dansereau, Niko Suenderhauf, Dimity Miller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03911v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, localization, gaussian splatting  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: slam, mapping, outdoor, ar, lighting, localization, dynamic, gaussian splatting, nerf, tracking, understanding  
- **[Splats in Splats: Embedding Invisible 3D Watermark within Gaussian Splatting](https://arxiv.org/abs/2412.03121v1)**  
  Authors: Yijia Guo, Wenkai Huang, Yang Li, Gaolei Li, Hang Zhang, Liwen Hu, Jianhua Li, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03121v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://water-gs.github.io.)  
  Keywords: fast, 3d gaussian, efficient, mapping, ar, 3d reconstruction, gaussian splatting  
- **[Towards Rich Emotions in 3D Avatars: A Text-to-3D Avatar Generation Benchmark](https://arxiv.org/abs/2412.02508v1)**  
  Authors: Haidong Xu, Meishan Zhang, Hao Ju, Zhedong Zheng, Hongyuan Zhu, Erik Cambria, Min Zhang, Hao Fei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02508v1.pdf)  
  Keywords: 3d gaussian, mapping, ar, motion, dynamic, human, avatar  
- **[GSGTrack: Gaussian Splatting-Guided Object Pose Tracking from RGB Videos](https://arxiv.org/abs/2412.02267v1)**  
  Authors: Zhiyuan Chen, Fan Lu, Guo Yu, Bin Li, Sanqing Qu, Yuan Huang, Changhong Fu, Guang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02267v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting, tracking  
- **[CTRL-D: Controllable Dynamic 3D Scene Editing with Personalized 2D Diffusion](https://arxiv.org/abs/2412.01792v1)**  
  Authors: Kai He, Chin-Hsuan Wu, Igor Gilitschenski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01792v1.pdf)  
  Keywords: 3d gaussian, ar, dynamic, gaussian splatting, tracking  
- **[6DOPE-GS: Online 6D Object Pose Estimation using Gaussian Splatting](https://arxiv.org/abs/2412.01543v1)**  
  Authors: Yufeng Jin, Vignesh Prasad, Snehal Jauhri, Mathias Franzius, Georgia Chalvatzaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01543v1.pdf)  
  Keywords: fast, autonomous driving, efficient, ar, dynamic, gaussian splatting, tracking, robotics  
- **[RGBDS-SLAM: A RGB-D Semantic Dense SLAM Based on 3D Multi Level Pyramid Gaussian Splatting](https://arxiv.org/abs/2412.01217v2)**  
  Authors: Zhenzhong Cao, Chenyang Zhao, Qianyi Zhang, Jinzheng Guang, Yinuo Song Jingtai Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01217v2.pdf) | [![GitHub](https://img.shields.io/github/stars/zhenzhongcao/RGBDS-SLAM?style=social)](https://github.com/zhenzhongcao/RGBDS-SLAM)  
  Keywords: 3d gaussian, semantic, slam, ar, gaussian splatting  
- **[FlashSLAM: Accelerated RGB-D SLAM for Real-Time 3D Scene Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2412.00682v1)**  
  Authors: Phu Pham, Damon Conover, Aniket Bera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00682v1.pdf)  
  Keywords: fast, 3d gaussian, efficient, slam, ar, sparse view, 3d reconstruction, gaussian splatting, tracking  
- **[LineGS : 3D Line Segment Representation on 3D Gaussian Splatting](https://arxiv.org/abs/2412.00477v1)**  
  Authors: Chenggang Yang, Yuang Shi, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00477v1.pdf)  
  Keywords: 3d gaussian, efficient, mapping, ar, localization, geometry, gaussian splatting, 3d reconstruction, face  

### Scene Understanding

*Showing the latest 50 out of 185 papers*

- **[EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding](https://arxiv.org/abs/2412.04380v2)**  
  Authors: Yuqi Wu, Wenzhao Zheng, Sicheng Zuo, Yuanhui Huang, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04380v2.pdf) | [![GitHub](https://img.shields.io/github/stars/YkiWu/EmbodiedOcc?style=social)](https://github.com/YkiWu/EmbodiedOcc)  
  Keywords: 3d gaussian, semantic, efficient, ar, human, understanding  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: semantic, ar, dynamic, gaussian splatting, face, urban scene, deformation, 4d  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: slam, mapping, outdoor, ar, lighting, localization, dynamic, gaussian splatting, nerf, tracking, understanding  
- **[Multi-robot autonomous 3D reconstruction using Gaussian splatting with Semantic guidance](https://arxiv.org/abs/2412.02249v1)**  
  Authors: Jing Zeng, Qi Ye, Tianle Liu, Yang Xu, Jin Li, Jinming Xu, Liang Li, Jiming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02249v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, high quality, face, gaussian splatting, 3d reconstruction, segmentation  
- **[SparseLGS: Sparse View Language Embedded Gaussian Splatting](https://arxiv.org/abs/2412.02245v2)**  
  Authors: Jun Hu, Zhang Chen, Zhong Li, Yi Xu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02245v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ustc3dv.github.io/SparseLGS)  
  Keywords: semantic, ar, sparse view, gaussian splatting, understanding  
- **[How to Use Diffusion Priors under Sparse Views?](https://arxiv.org/abs/2412.02225v1)**  
  Authors: Qisen Wang, Yifan Zhao, Jiawei Ma, Jia Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02225v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iCVTEAM/IPSM?style=social)](https://github.com/iCVTEAM/IPSM)  
  Keywords: 3d gaussian, semantic, ar, sparse view, geometry, gaussian splatting, 3d reconstruction, sparse-view  
- **[SparseGrasp: Robotic Grasping via 3D Semantic Gaussian Splatting from Sparse Multi-View RGB Images](https://arxiv.org/abs/2412.02140v1)**  
  Authors: Junqiu Yu, Xinlin Ren, Yongchong Gu, Haitao Lin, Tianyu Wang, Yi Zhu, Hang Xu, Yu-Gang Jiang, Xiangyang Xue, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02140v1.pdf)  
  Keywords: fast, 3d gaussian, efficient, semantic, ar, gaussian splatting, human, sparse-view  
- **[Planar Gaussian Splatting](https://arxiv.org/abs/2412.01931v1)**  
  Authors: Farhad G. Zanjani, Hong Cai, Hanno Ackermann, Leila Mirvakhabova, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01931v1.pdf)  
  Keywords: fast, ar, neural rendering, face, gaussian splatting, geometry, segmentation  
- **[Occam's LGS: A Simple Approach for Language Gaussian Splatting](https://arxiv.org/abs/2412.01807v1)**  
  Authors: Jiahuan Cheng, Jan-Nico Zaech, Luc Van Gool, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01807v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insait-institute.github.io/OccamLGS/)  
  Keywords: 3d gaussian, semantic, efficient, ar, compression, 3d reconstruction, gaussian splatting, understanding  
- **[3DSceneEditor: Controllable 3D Scene Editing with Gaussian Splatting](https://arxiv.org/abs/2412.01583v1)**  
  Authors: Ziyang Yan, Lei Li, Yihua Shao, Siyu Chen, Wuzong Kai, Jenq-Neng Hwang, Hao Zhao, Fabio Remondino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01583v1.pdf)  
  Keywords: semantic, efficient, ar, gaussian splatting, segmentation  



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