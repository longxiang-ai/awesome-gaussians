# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2024-12-20 00:46:04

## Categories

- [3DGS Surveys](#3dgs-surveys) (20 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (342 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1150 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (385 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (419 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (81 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (389 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (62 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (420 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (196 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (27 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (129 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (169 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (200 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: ar, survey, slam, outdoor, dynamic, face, tracking, lighting, mapping, geometry, 3d gaussian, localization, reflection  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: ar, survey, illumination, 3d gaussian, recognition, gaussian splatting  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: ar, survey, high-fidelity, nerf, compact, dynamic, autonomous driving, 3d reconstruction, lighting, semantic, geometry, robotics, gaussian splatting  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v1)**  
  Authors: Siting Zhu, Guangming Wang, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v1.pdf)  
  Keywords: ar, real-time rendering, survey, nerf, understanding, 3d gaussian, robotics, gaussian splatting  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: ar, survey, high-fidelity, nerf, lighting, 3d gaussian, gaussian splatting  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: ar, survey, nerf, autonomous driving, vr, 3d reconstruction, 3d gaussian, robotics, gaussian splatting  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: ar, survey, 3d gaussian  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v2)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v2.pdf)  
  Keywords: ar, real-time rendering, survey, understanding, efficient, 3d gaussian, gaussian splatting  
- **[Survey on Fundamental Deep Learning 3D Reconstruction Techniques](https://arxiv.org/abs/2407.08137v1)**  
  Authors: Yonge Bai, LikHang Wong, TszYin Twan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.08137v1.pdf)  
  Keywords: ar, survey, nerf, 3d reconstruction, lighting, 3d gaussian, gaussian splatting  
- **[Panopticon: a telescope for our times](https://arxiv.org/abs/2407.05103v2)**  
  Authors: Will Saunders, Timothy Chin, Michael Goodwin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05103v2.pdf)  
  Keywords: ar, survey  

### Acceleration

*Showing the latest 50 out of 342 papers*

- **[GAGS: Granularity-Aware Feature Distillation for Language Gaussian Splatting](https://arxiv.org/abs/2412.13654v1)**  
  Authors: Yuning Peng, Haiping Wang, Yuan Liu, Chenglu Wen, Zhen Dong, Bisheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13654v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pz0826.github.io/GAGS-Webpage/)  
  Keywords: ar, understanding, semantic, segmentation, fast, 3d gaussian, gaussian splatting  
- **[Turbo-GS: Accelerating 3D Gaussian Fitting for High-Quality Radiance Fields](https://arxiv.org/abs/2412.13547v1)**  
  Authors: Tao Lu, Ankit Dhiman, R Srinath, Emre Arslan, Angela Xing, Yuanbo Xiangli, R Venkatesh Babu, Srinath Sridhar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13547v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ivl.cs.brown.edu/research/turbo-gs.)  
  Keywords: ar, 3d reconstruction, fast, 3d gaussian, robotics, gaussian splatting  
- **[4DRGS: 4D Radiative Gaussian Splatting for Efficient 3D Vessel Reconstruction from Sparse-View Dynamic DSA Images](https://arxiv.org/abs/2412.12919v1)**  
  Authors: Zhentao Liu, Ruyi Zha, Huangxuan Zhao, Hongdong Li, Zhiming Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12919v1.pdf)  
  Keywords: ar, medical, sparse-view, compact, dynamic, 4d, efficient, fast, geometry, gaussian splatting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: ar, real-time rendering, high-fidelity, ray tracing, efficient, lighting, 3d gaussian, reflection, gaussian splatting  
- **[PanSplat: 4K Panorama Synthesis with Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2412.12096v1)**  
  Authors: Cheng Zhang, Haofei Xu, Qianyi Wu, Camilo Cruz Gambardella, Dinh Phung, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12096v1.pdf) | [![GitHub](https://img.shields.io/github/stars/chengzhag/PanSplat?style=social)](https://github.com/chengzhag/PanSplat)  
  Keywords: ar, autonomous driving, vr, efficient, 3d gaussian, fast, head, robotics, gaussian splatting  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: ar, nerf, face, efficient, mapping, fast, global illumination, illumination, geometry, gaussian splatting  
- **[SuperGSeg: Open-Vocabulary 3D Segmentation with Structured Super-Gaussians](https://arxiv.org/abs/2412.10231v1)**  
  Authors: Siyun Liang, Sen Wang, Kunyi Li, Michael Niemeyer, Stefano Gasperini, Nassir Navab, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10231v1.pdf)  
  Keywords: ar, real-time rendering, understanding, efficient, semantic, segmentation, 3d gaussian, localization, gaussian splatting  
- **[SplineGS: Robust Motion-Adaptive Spline for Real-Time Dynamic 3D Gaussians from Monocular Video](https://arxiv.org/abs/2412.09982v2)**  
  Authors: Jongmin Park, Minh-Quan Viet Bui, Juan Luis Gonzalez Bello, Jaeho Moon, Jihyong Oh, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09982v2.pdf)  
  Keywords: ar, motion, dynamic, deformation, fast, 3d gaussian, gaussian splatting  
- **[SLGaussian: Fast Language Gaussian Splatting in Sparse Views](https://arxiv.org/abs/2412.08331v1)**  
  Authors: Kangjie Chen, BingQuan Dai, Minghan Qin, Dongbin Zhang, Peihao Li, Yingshuang Zou, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08331v1.pdf)  
  Keywords: ar, sparse view, understanding, efficient, tracking, vr, semantic, segmentation, fast, localization, robotics, gaussian splatting  
- **[ProGDF: Progressive Gaussian Differential Field for Controllable and Flexible 3D Editing](https://arxiv.org/abs/2412.08152v1)**  
  Authors: Yian Zhao, Wanshi Xu, Yang Wu, Weiheng Huang, Zhongqian Sun, Wei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08152v1.pdf)  
  Keywords: ar, face, efficient, efficient rendering, lightweight, gaussian splatting  

### Applications

*Showing the latest 50 out of 1150 papers*

- **[GraphAvatar: Compact Head Avatars with GNN-Generated 3D Gaussians](https://arxiv.org/abs/2412.13983v1)**  
  Authors: Xiaobao Wei, Peng Chen, Ming Lu, Hui Chen, Feng Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13983v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ucwxb/GraphAvatar?style=social)](https://github.com/ucwxb/GraphAvatar)  
  Keywords: ar, nerf, avatar, compact, head, face, tracking, 3d gaussian, gaussian splatting  
- **[GAGS: Granularity-Aware Feature Distillation for Language Gaussian Splatting](https://arxiv.org/abs/2412.13654v1)**  
  Authors: Yuning Peng, Haiping Wang, Yuan Liu, Chenglu Wen, Zhen Dong, Bisheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13654v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pz0826.github.io/GAGS-Webpage/)  
  Keywords: ar, understanding, semantic, segmentation, fast, 3d gaussian, gaussian splatting  
- **[4D Radar-Inertial Odometry based on Gaussian Modeling and Multi-Hypothesis Scan Matching](https://arxiv.org/abs/2412.13639v1)**  
  Authors: Fernando Amodeo, Luis Merino, Fernando Caballero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13639v1.pdf)  
  Keywords: ar, slam, 4d, 3d gaussian, gaussian splatting  
- **[Turbo-GS: Accelerating 3D Gaussian Fitting for High-Quality Radiance Fields](https://arxiv.org/abs/2412.13547v1)**  
  Authors: Tao Lu, Ankit Dhiman, R Srinath, Emre Arslan, Angela Xing, Yuanbo Xiangli, R Venkatesh Babu, Srinath Sridhar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13547v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ivl.cs.brown.edu/research/turbo-gs.)  
  Keywords: ar, 3d reconstruction, fast, 3d gaussian, robotics, gaussian splatting  
- **[Vivar: A Generative AR System for Intuitive Multi-Modal Sensor Data Presentation](https://arxiv.org/abs/2412.13509v1)**  
  Authors: Yunqi Guo, Kaiyuan Hou, Heming Fu, Hongkai Chen, Zhenyu Yan, Guoliang Xing, Xiaofan Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13509v1.pdf)  
  Keywords: ar, dynamic, understanding, semantic, 3d gaussian, gaussian splatting  
- **[GaussTR: Foundation Model-Aligned Gaussian Transformer for Self-Supervised 3D Spatial Understanding](https://arxiv.org/abs/2412.13193v1)**  
  Authors: Haoyi Jiang, Liu Liu, Tianheng Cheng, Xinjie Wang, Tianwei Lin, Zhizhong Su, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13193v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hustvl/GaussTR?style=social)](https://github.com/hustvl/GaussTR)  
  Keywords: ar, autonomous driving, understanding, semantic, 3d gaussian  
- **[Real-time Free-view Human Rendering from Sparse-view RGB Videos using Double Unprojected Textures](https://arxiv.org/abs/2412.13183v1)**  
  Authors: Guoxing Sun, Rishabh Dabral, Heming Zhu, Pascal Fua, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13183v1.pdf)  
  Keywords: ar, sparse-view, human, body, deformation, geometry  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: ar, survey, slam, outdoor, dynamic, face, tracking, lighting, mapping, geometry, 3d gaussian, localization, reflection  
- **[EOGS: Gaussian Splatting for Earth Observation](https://arxiv.org/abs/2412.13047v1)**  
  Authors: Luca Savant Aira, Gabriele Facciolo, Thibaud Ehret  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13047v1.pdf)  
  Keywords: ar, shadow, nerf, gaussian splatting  
- **[4DRGS: 4D Radiative Gaussian Splatting for Efficient 3D Vessel Reconstruction from Sparse-View Dynamic DSA Images](https://arxiv.org/abs/2412.12919v1)**  
  Authors: Zhentao Liu, Ruyi Zha, Huangxuan Zhao, Hongdong Li, Zhiming Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12919v1.pdf)  
  Keywords: ar, medical, sparse-view, compact, dynamic, 4d, efficient, fast, geometry, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 385 papers*

- **[GraphAvatar: Compact Head Avatars with GNN-Generated 3D Gaussians](https://arxiv.org/abs/2412.13983v1)**  
  Authors: Xiaobao Wei, Peng Chen, Ming Lu, Hui Chen, Feng Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13983v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ucwxb/GraphAvatar?style=social)](https://github.com/ucwxb/GraphAvatar)  
  Keywords: ar, nerf, avatar, compact, head, face, tracking, 3d gaussian, gaussian splatting  
- **[Real-time Free-view Human Rendering from Sparse-view RGB Videos using Double Unprojected Textures](https://arxiv.org/abs/2412.13183v1)**  
  Authors: Guoxing Sun, Rishabh Dabral, Heming Zhu, Pascal Fua, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13183v1.pdf)  
  Keywords: ar, sparse-view, human, body, deformation, geometry  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: ar, survey, slam, outdoor, dynamic, face, tracking, lighting, mapping, geometry, 3d gaussian, localization, reflection  
- **[Gaussian Billboards: Expressive 2D Gaussian Splatting with Textures](https://arxiv.org/abs/2412.12734v1)**  
  Authors: Sebastian Weiss, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12734v1.pdf)  
  Keywords: ar, face, mapping, geometry, gaussian splatting  
- **[PanSplat: 4K Panorama Synthesis with Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2412.12096v1)**  
  Authors: Cheng Zhang, Haofei Xu, Qianyi Wu, Camilo Cruz Gambardella, Dinh Phung, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12096v1.pdf) | [![GitHub](https://img.shields.io/github/stars/chengzhag/PanSplat?style=social)](https://github.com/chengzhag/PanSplat)  
  Keywords: ar, autonomous driving, vr, efficient, 3d gaussian, fast, head, robotics, gaussian splatting  
- **[Wonderland: Navigating 3D Scenes from a Single Image](https://arxiv.org/abs/2412.12091v1)**  
  Authors: Hanwen Liang, Junli Cao, Vidit Goel, Guocheng Qian, Sergei Korolev, Demetri Terzopoulos, Konstantinos N. Plataniotis, Sergey Tulyakov, Jian Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12091v1.pdf)  
  Keywords: ar, face, efficient, 3d reconstruction, 3d gaussian, gaussian splatting  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: ar, nerf, face, efficient, mapping, fast, global illumination, illumination, geometry, gaussian splatting  
- **[GAF: Gaussian Avatar Reconstruction from Monocular Videos via Multi-view Diffusion](https://arxiv.org/abs/2412.10209v1)**  
  Authors: Jiapeng Tang, Davide Davoli, Tobias Kirschstein, Liam Schoneveld, Matthias Niessner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10209v1.pdf)  
  Keywords: ar, avatar, head, 3d gaussian, gaussian splatting  
- **[RP-SLAM: Real-time Photorealistic SLAM with Efficient 3D Gaussian Splatting](https://arxiv.org/abs/2412.09868v1)**  
  Authors: Lizhi Bai, Chunqi Tian, Jun Yang, Siyu Zhang, Masanori Suganuma, Takayuki Okatani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09868v1.pdf)  
  Keywords: ar, slam, compact, dynamic, face, efficient, mapping, 3d gaussian, gaussian splatting  
- **[LiftImage3D: Lifting Any Single Image to 3D Gaussians with Video Generation Priors](https://arxiv.org/abs/2412.09597v1)**  
  Authors: Yabo Chen, Chen Yang, Jiemin Fang, Xiaopeng Zhang, Lingxi Xie, Wei Shen, Wenrui Dai, Hongkai Xiong, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09597v1.pdf)  
  Keywords: ar, motion, face, 3d reconstruction, 3d gaussian, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 419 papers*

- **[4D Radar-Inertial Odometry based on Gaussian Modeling and Multi-Hypothesis Scan Matching](https://arxiv.org/abs/2412.13639v1)**  
  Authors: Fernando Amodeo, Luis Merino, Fernando Caballero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13639v1.pdf)  
  Keywords: ar, slam, 4d, 3d gaussian, gaussian splatting  
- **[Vivar: A Generative AR System for Intuitive Multi-Modal Sensor Data Presentation](https://arxiv.org/abs/2412.13509v1)**  
  Authors: Yunqi Guo, Kaiyuan Hou, Heming Fu, Hongkai Chen, Zhenyu Yan, Guoliang Xing, Xiaofan Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13509v1.pdf)  
  Keywords: ar, dynamic, understanding, semantic, 3d gaussian, gaussian splatting  
- **[Real-time Free-view Human Rendering from Sparse-view RGB Videos using Double Unprojected Textures](https://arxiv.org/abs/2412.13183v1)**  
  Authors: Guoxing Sun, Rishabh Dabral, Heming Zhu, Pascal Fua, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13183v1.pdf)  
  Keywords: ar, sparse-view, human, body, deformation, geometry  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: ar, survey, slam, outdoor, dynamic, face, tracking, lighting, mapping, geometry, 3d gaussian, localization, reflection  
- **[4DRGS: 4D Radiative Gaussian Splatting for Efficient 3D Vessel Reconstruction from Sparse-View Dynamic DSA Images](https://arxiv.org/abs/2412.12919v1)**  
  Authors: Zhentao Liu, Ruyi Zha, Huangxuan Zhao, Hongdong Li, Zhiming Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12919v1.pdf)  
  Keywords: ar, medical, sparse-view, compact, dynamic, 4d, efficient, fast, geometry, gaussian splatting  
- **[HyperGS: Hyperspectral 3D Gaussian Splatting](https://arxiv.org/abs/2412.12849v1)**  
  Authors: Christopher Thirgood, Oscar Mendez, Erin Chao Ling, Jon Storey, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12849v1.pdf)  
  Keywords: ar, high-fidelity, 4d, 3d gaussian, gaussian splatting  
- **[SweepEvGS: Event-Based 3D Gaussian Splatting for Macro and Micro Radiance Field Rendering from a Single Sweep](https://arxiv.org/abs/2412.11579v1)**  
  Authors: Jingqian Wu, Shuo Zhu, Chutian Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11579v1.pdf)  
  Keywords: ar, high-fidelity, motion, dynamic, efficient, lighting, 3d gaussian, gaussian splatting  
- **[GaussianProperty: Integrating Physical Properties to 3D Gaussians with LMMs](https://arxiv.org/abs/2412.11258v1)**  
  Authors: Xinli Xu, Wenhang Ge, Dicong Qiu, ZhiFei Chen, Dongyu Yan, Zhuoyun Liu, Haoyu Zhao, Hanfeng Zhao, Shunsi Zhang, Junwei Liang, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11258v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://Gaussian-Property.github.io}{this)  
  Keywords: ar, dynamic, understanding, lighting, segmentation, 3d gaussian, recognition, robotics  
- **[GaussianWorld: Gaussian World Model for Streaming 3D Occupancy Prediction](https://arxiv.org/abs/2412.10373v1)**  
  Authors: Sicheng Zuo, Wenzhao Zheng, Yuanhui Huang, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10373v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zuosc19/GaussianWorld?style=social)](https://github.com/zuosc19/GaussianWorld)  
  Keywords: ar, motion, dynamic, autonomous driving, 4d, 3d gaussian  
- **[GaussianAD: Gaussian-Centric End-to-End Autonomous Driving](https://arxiv.org/abs/2412.10371v1)**  
  Authors: Wenzhao Zheng, Junjie Wu, Yao Zheng, Sicheng Zuo, Zixun Xie, Longchao Yang, Yong Pan, Zhihui Hao, Peng Jia, Xianpeng Lang, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10371v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wzzheng/GaussianAD?style=social)](https://github.com/wzzheng/GaussianAD)  
  Keywords: ar, motion, dynamic, autonomous driving, efficient, 4d, semantic, 3d gaussian  

### Few-shot

*Showing the latest 50 out of 81 papers*

- **[Real-time Free-view Human Rendering from Sparse-view RGB Videos using Double Unprojected Textures](https://arxiv.org/abs/2412.13183v1)**  
  Authors: Guoxing Sun, Rishabh Dabral, Heming Zhu, Pascal Fua, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13183v1.pdf)  
  Keywords: ar, sparse-view, human, body, deformation, geometry  
- **[4DRGS: 4D Radiative Gaussian Splatting for Efficient 3D Vessel Reconstruction from Sparse-View Dynamic DSA Images](https://arxiv.org/abs/2412.12919v1)**  
  Authors: Zhentao Liu, Ruyi Zha, Huangxuan Zhao, Hongdong Li, Zhiming Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12919v1.pdf)  
  Keywords: ar, medical, sparse-view, compact, dynamic, 4d, efficient, fast, geometry, gaussian splatting  
- **[TSGaussian: Semantic and Depth-Guided Target-Specific Gaussian Splatting from Sparse Views](https://arxiv.org/abs/2412.10051v1)**  
  Authors: Liang Zhao, Zehan Bao, Yi Xie, Hong Chen, Yaohui Chen, Weifu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10051v1.pdf) | [![GitHub](https://img.shields.io/github/stars/leon2000-ai/TSGaussian?style=social)](https://github.com/leon2000-ai/TSGaussian)  
  Keywords: ar, sparse view, compact, semantic, segmentation, geometry, 3d gaussian, gaussian splatting  
- **[FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction](https://arxiv.org/abs/2412.09573v1)**  
  Authors: Jiale Xu, Shenghua Gao, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09573v1.pdf)  
  Keywords: ar, high-fidelity, sparse-view, 3d reconstruction, 3d gaussian, gaussian splatting  
- **[SLGaussian: Fast Language Gaussian Splatting in Sparse Views](https://arxiv.org/abs/2412.08331v1)**  
  Authors: Kangjie Chen, BingQuan Dai, Minghan Qin, Dongbin Zhang, Peihao Li, Yingshuang Zou, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08331v1.pdf)  
  Keywords: ar, sparse view, understanding, efficient, tracking, vr, semantic, segmentation, fast, localization, robotics, gaussian splatting  
- **[MV-DUSt3R+: Single-Stage Scene Reconstruction from Sparse Views In 2 Seconds](https://arxiv.org/abs/2412.06974v1)**  
  Authors: Zhenggang Tang, Yuchen Fan, Dilin Wang, Hongyu Xu, Rakesh Ranjan, Alexander Schwing, Zhicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06974v1.pdf)  
  Keywords: ar, sparse view, fast, head, gaussian splatting  
- **[Generative Densification: Learning to Densify Gaussians for High-Fidelity Generalizable 3D Reconstruction](https://arxiv.org/abs/2412.06234v2)**  
  Authors: Seungtae Nam, Xiangyu Sun, Gyeongjin Kang, Younggeun Lee, Seungjun Oh, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06234v2.pdf)  
  Keywords: ar, high-fidelity, sparse-view, 3d reconstruction, efficient, 3d gaussian, gaussian splatting  
- **[GBR: Generative Bundle Refinement for High-fidelity Gaussian Splatting and Meshing](https://arxiv.org/abs/2412.05908v1)**  
  Authors: Jianing Zhang, Yuchao Zheng, Ziwei Li, Qionghai Dai, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05908v1.pdf)  
  Keywords: ar, high-fidelity, sparse-view, efficient, geometry, gaussian splatting  
- **[SparseLGS: Sparse View Language Embedded Gaussian Splatting](https://arxiv.org/abs/2412.02245v2)**  
  Authors: Jun Hu, Zhang Chen, Zhong Li, Yi Xu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02245v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ustc3dv.github.io/SparseLGS)  
  Keywords: ar, sparse view, understanding, semantic, gaussian splatting  
- **[How to Use Diffusion Priors under Sparse Views?](https://arxiv.org/abs/2412.02225v1)**  
  Authors: Qisen Wang, Yifan Zhao, Jiawei Ma, Jia Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02225v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iCVTEAM/IPSM?style=social)](https://github.com/iCVTEAM/IPSM)  
  Keywords: ar, sparse view, sparse-view, 3d reconstruction, semantic, geometry, 3d gaussian, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 389 papers*

- **[Turbo-GS: Accelerating 3D Gaussian Fitting for High-Quality Radiance Fields](https://arxiv.org/abs/2412.13547v1)**  
  Authors: Tao Lu, Ankit Dhiman, R Srinath, Emre Arslan, Angela Xing, Yuanbo Xiangli, R Venkatesh Babu, Srinath Sridhar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13547v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ivl.cs.brown.edu/research/turbo-gs.)  
  Keywords: ar, 3d reconstruction, fast, 3d gaussian, robotics, gaussian splatting  
- **[Real-time Free-view Human Rendering from Sparse-view RGB Videos using Double Unprojected Textures](https://arxiv.org/abs/2412.13183v1)**  
  Authors: Guoxing Sun, Rishabh Dabral, Heming Zhu, Pascal Fua, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13183v1.pdf)  
  Keywords: ar, sparse-view, human, body, deformation, geometry  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: ar, survey, slam, outdoor, dynamic, face, tracking, lighting, mapping, geometry, 3d gaussian, localization, reflection  
- **[4DRGS: 4D Radiative Gaussian Splatting for Efficient 3D Vessel Reconstruction from Sparse-View Dynamic DSA Images](https://arxiv.org/abs/2412.12919v1)**  
  Authors: Zhentao Liu, Ruyi Zha, Huangxuan Zhao, Hongdong Li, Zhiming Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12919v1.pdf)  
  Keywords: ar, medical, sparse-view, compact, dynamic, 4d, efficient, fast, geometry, gaussian splatting  
- **[Gaussian Billboards: Expressive 2D Gaussian Splatting with Textures](https://arxiv.org/abs/2412.12734v1)**  
  Authors: Sebastian Weiss, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12734v1.pdf)  
  Keywords: ar, face, mapping, geometry, gaussian splatting  
- **[Wonderland: Navigating 3D Scenes from a Single Image](https://arxiv.org/abs/2412.12091v1)**  
  Authors: Hanwen Liang, Junli Cao, Vidit Goel, Guocheng Qian, Sergei Korolev, Demetri Terzopoulos, Konstantinos N. Plataniotis, Sergey Tulyakov, Jian Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12091v1.pdf)  
  Keywords: ar, face, efficient, 3d reconstruction, 3d gaussian, gaussian splatting  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: ar, nerf, face, efficient, mapping, fast, global illumination, illumination, geometry, gaussian splatting  
- **[Deformable Radial Kernel Splatting](https://arxiv.org/abs/2412.11752v1)**  
  Authors: Yi-Hua Huang, Ming-Xian Lin, Yang-Tian Sun, Ziyi Yang, Xiaoyang Lyu, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11752v1.pdf)  
  Keywords: ar, high-fidelity, efficient, geometry, gaussian splatting  
- **[DCSEG: Decoupled 3D Open-Set Segmentation using Gaussian Splatting](https://arxiv.org/abs/2412.10972v1)**  
  Authors: Luis Wiedmann, Luca Wiehe, David Rozenberszki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10972v1.pdf)  
  Keywords: ar, efficient, 3d reconstruction, semantic, segmentation, 3d gaussian, robotics, gaussian splatting  
- **[TSGaussian: Semantic and Depth-Guided Target-Specific Gaussian Splatting from Sparse Views](https://arxiv.org/abs/2412.10051v1)**  
  Authors: Liang Zhao, Zehan Bao, Yi Xie, Hong Chen, Yaohui Chen, Weifu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10051v1.pdf) | [![GitHub](https://img.shields.io/github/stars/leon2000-ai/TSGaussian?style=social)](https://github.com/leon2000-ai/TSGaussian)  
  Keywords: ar, sparse view, compact, semantic, segmentation, geometry, 3d gaussian, gaussian splatting  

### Large Scene

*Showing the latest 50 out of 62 papers*

- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: ar, survey, slam, outdoor, dynamic, face, tracking, lighting, mapping, geometry, 3d gaussian, localization, reflection  
- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: ar, dynamic, 3d gaussian, large scene, head, gaussian splatting  
- **[HybridGS: Decoupling Transients and Statics with 2D and 3D Gaussian Splatting](https://arxiv.org/abs/2412.03844v2)**  
  Authors: Jingyu Lin, Jiaqi Gu, Lubin Fan, Bojian Wu, Yujing Lou, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03844v2.pdf)  
  Keywords: outdoor, ar, 3d gaussian, gaussian splatting  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: ar, dynamic, face, 4d, deformation, semantic, urban scene, gaussian splatting  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: ar, slam, nerf, outdoor, dynamic, understanding, tracking, lighting, mapping, localization, gaussian splatting  
- **[Horizon-GS: Unified 3D Gaussian Splatting for Large-Scale Aerial-to-Ground Scenes](https://arxiv.org/abs/2412.01745v1)**  
  Authors: Lihan Jiang, Kerui Ren, Mulin Yu, Linning Xu, Junting Dong, Tao Lu, Feng Zhao, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01745v1.pdf)  
  Keywords: ar, high-fidelity, urban scene, 3d gaussian, gaussian splatting  
- **[Tortho-Gaussian: Splatting True Digital Orthophoto Maps](https://arxiv.org/abs/2411.19594v1)**  
  Authors: Xin Wang, Wendi Zhang, Hong Xie, Haibin Ai, Qiangqiang Yuan, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19594v1.pdf)  
  Keywords: ar, face, urban scene, 3d gaussian, gaussian splatting  
- **[UrbanCAD: Towards Highly Controllable and Photorealistic 3D Vehicles for Urban Scene Simulation](https://arxiv.org/abs/2411.19292v1)**  
  Authors: Yichong Lu, Yichi Cai, Shangzhan Zhang, Hongyu Zhou, Haoji Hu, Huimin Yu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19292v1.pdf)  
  Keywords: ar, high-fidelity, relighting, autonomous driving, lighting, urban scene  
- **[Unleashing the Power of Data Synthesis in Visual Localization](https://arxiv.org/abs/2412.00138v1)**  
  Authors: Sihang Li, Siqi Tan, Bowen Chang, Jing Zhang, Chen Feng, Yiming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ai4ce.github.io/RAP/)  
  Keywords: ar, outdoor, dynamic, fast, 3d gaussian, localization, robotics  
- **[UniGaussian: Driving Scene Reconstruction from Multiple Camera Models via Unified Gaussian Representations](https://arxiv.org/abs/2411.15355v1)**  
  Authors: Yuan Ren, Guile Wu, Runhao Li, Zheyuan Yang, Yibo Liu, Xingxin Chen, Tongtong Cao, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15355v1.pdf)  
  Keywords: ar, real-time rendering, autonomous driving, understanding, semantic, fast, urban scene, 3d gaussian, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 420 papers*

- **[GraphAvatar: Compact Head Avatars with GNN-Generated 3D Gaussians](https://arxiv.org/abs/2412.13983v1)**  
  Authors: Xiaobao Wei, Peng Chen, Ming Lu, Hui Chen, Feng Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13983v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ucwxb/GraphAvatar?style=social)](https://github.com/ucwxb/GraphAvatar)  
  Keywords: ar, nerf, avatar, compact, head, face, tracking, 3d gaussian, gaussian splatting  
- **[4DRGS: 4D Radiative Gaussian Splatting for Efficient 3D Vessel Reconstruction from Sparse-View Dynamic DSA Images](https://arxiv.org/abs/2412.12919v1)**  
  Authors: Zhentao Liu, Ruyi Zha, Huangxuan Zhao, Hongdong Li, Zhiming Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12919v1.pdf)  
  Keywords: ar, medical, sparse-view, compact, dynamic, 4d, efficient, fast, geometry, gaussian splatting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: ar, real-time rendering, high-fidelity, ray tracing, efficient, lighting, 3d gaussian, reflection, gaussian splatting  
- **[PanSplat: 4K Panorama Synthesis with Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2412.12096v1)**  
  Authors: Cheng Zhang, Haofei Xu, Qianyi Wu, Camilo Cruz Gambardella, Dinh Phung, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12096v1.pdf) | [![GitHub](https://img.shields.io/github/stars/chengzhag/PanSplat?style=social)](https://github.com/chengzhag/PanSplat)  
  Keywords: ar, autonomous driving, vr, efficient, 3d gaussian, fast, head, robotics, gaussian splatting  
- **[Wonderland: Navigating 3D Scenes from a Single Image](https://arxiv.org/abs/2412.12091v1)**  
  Authors: Hanwen Liang, Junli Cao, Vidit Goel, Guocheng Qian, Sergei Korolev, Demetri Terzopoulos, Konstantinos N. Plataniotis, Sergey Tulyakov, Jian Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12091v1.pdf)  
  Keywords: ar, face, efficient, 3d reconstruction, 3d gaussian, gaussian splatting  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: ar, nerf, face, efficient, mapping, fast, global illumination, illumination, geometry, gaussian splatting  
- **[Deformable Radial Kernel Splatting](https://arxiv.org/abs/2412.11752v1)**  
  Authors: Yi-Hua Huang, Ming-Xian Lin, Yang-Tian Sun, Ziyi Yang, Xiaoyang Lyu, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11752v1.pdf)  
  Keywords: ar, high-fidelity, efficient, geometry, gaussian splatting  
- **[SweepEvGS: Event-Based 3D Gaussian Splatting for Macro and Micro Radiance Field Rendering from a Single Sweep](https://arxiv.org/abs/2412.11579v1)**  
  Authors: Jingqian Wu, Shuo Zhu, Chutian Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11579v1.pdf)  
  Keywords: ar, high-fidelity, motion, dynamic, efficient, lighting, 3d gaussian, gaussian splatting  
- **[EditSplat: Multi-View Fusion and Attention-Guided Optimization for View-Consistent 3D Scene Editing with 3D Gaussian Splatting](https://arxiv.org/abs/2412.11520v1)**  
  Authors: Dong In Lee, Hyeongcheol Park, Jiyoung Seo, Eunbyung Park, Hyunje Park, Ha Dam Baek, Shin Sangheon, Sangmin kim, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11520v1.pdf)  
  Keywords: ar, vr, efficient, semantic, 3d gaussian, gaussian splatting  
- **[DCSEG: Decoupled 3D Open-Set Segmentation using Gaussian Splatting](https://arxiv.org/abs/2412.10972v1)**  
  Authors: Luis Wiedmann, Luca Wiehe, David Rozenberszki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10972v1.pdf)  
  Keywords: ar, efficient, 3d reconstruction, semantic, segmentation, 3d gaussian, robotics, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 196 papers*

- **[HyperGS: Hyperspectral 3D Gaussian Splatting](https://arxiv.org/abs/2412.12849v1)**  
  Authors: Christopher Thirgood, Oscar Mendez, Erin Chao Ling, Jon Storey, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12849v1.pdf)  
  Keywords: ar, high-fidelity, 4d, 3d gaussian, gaussian splatting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: ar, real-time rendering, high-fidelity, ray tracing, efficient, lighting, 3d gaussian, reflection, gaussian splatting  
- **[Deformable Radial Kernel Splatting](https://arxiv.org/abs/2412.11752v1)**  
  Authors: Yi-Hua Huang, Ming-Xian Lin, Yang-Tian Sun, Ziyi Yang, Xiaoyang Lyu, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11752v1.pdf)  
  Keywords: ar, high-fidelity, efficient, geometry, gaussian splatting  
- **[SweepEvGS: Event-Based 3D Gaussian Splatting for Macro and Micro Radiance Field Rendering from a Single Sweep](https://arxiv.org/abs/2412.11579v1)**  
  Authors: Jingqian Wu, Shuo Zhu, Chutian Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11579v1.pdf)  
  Keywords: ar, high-fidelity, motion, dynamic, efficient, lighting, 3d gaussian, gaussian splatting  
- **[MAC-Ego3D: Multi-Agent Gaussian Consensus for Real-Time Collaborative Ego-Motion and Photorealistic 3D Reconstruction](https://arxiv.org/abs/2412.09723v1)**  
  Authors: Xiaohao Xu, Feng Xue, Shibo Zhao, Yike Pan, Sebastian Scherer, Xiaonan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09723v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Xiaohao-Xu/MAC-Ego3D?style=social)](https://github.com/Xiaohao-Xu/MAC-Ego3D)  
  Keywords: ar, high-fidelity, motion, efficient, mapping, 3d reconstruction, localization  
- **[FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction](https://arxiv.org/abs/2412.09573v1)**  
  Authors: Jiale Xu, Shenghua Gao, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09573v1.pdf)  
  Keywords: ar, high-fidelity, sparse-view, 3d reconstruction, 3d gaussian, gaussian splatting  
- **[PointTalk: Audio-Driven Dynamic Lip Point Cloud for 3D Gaussian-based Talking Head Synthesis](https://arxiv.org/abs/2412.08504v1)**  
  Authors: Yifan Xie, Tao Feng, Xin Zhang, Xiangyang Luo, Zixuan Guo, Weijiang Yu, Heng Chang, Fei Ma, Fei Richard Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08504v1.pdf)  
  Keywords: ar, high-fidelity, head, human, dynamic, understanding, 3d gaussian  
- **[DSplats: 3D Generation by Denoising Splats-Based Multiview Diffusion Models](https://arxiv.org/abs/2412.09648v1)**  
  Authors: Kevin Miao, Harsh Agrawal, Qihang Zhang, Federico Semeraro, Marco Cavallo, Jiatao Gu, Alexander Toshev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09648v1.pdf)  
  Keywords: high-fidelity, ar, 3d gaussian, 3d reconstruction  
- **[GASP: Gaussian Avatars with Synthetic Priors](https://arxiv.org/abs/2412.07739v1)**  
  Authors: Jack Saunders, Charlie Hewitt, Yanan Jian, Marek Kowalski, Tadas Baltrusaitis, Yiye Chen, Darren Cosker, Virginia Estellers, Nicholas Gyde, Vinay P. Namboodiri, Benjamin E Lundell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07739v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://microsoft.github.io/GASP/))  
  Keywords: avatar, ar, high quality, gaussian splatting  
- **[Proc-GS: Procedural Building Generation for City Assembly with 3D Gaussians](https://arxiv.org/abs/2412.07660v1)**  
  Authors: Yixuan Li, Xingjian Ran, Linning Xu, Tao Lu, Mulin Yu, Zhenzhi Wang, Yuanbo Xiangli, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.07660v1.pdf)  
  Keywords: ar, high-fidelity, efficient, 3d gaussian, gaussian splatting  

### Ray Tracing

- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: ar, real-time rendering, high-fidelity, ray tracing, efficient, lighting, 3d gaussian, reflection, gaussian splatting  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: ar, nerf, face, efficient, mapping, fast, global illumination, illumination, geometry, gaussian splatting  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v1.pdf)  
  Keywords: ar, ray tracing, efficient, 3d gaussian, gaussian splatting  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v1)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v1.pdf)  
  Keywords: ray tracing, ar, 3d gaussian, gaussian splatting  
- **[URAvatar: Universal Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2410.24223v1)**  
  Authors: Junxuan Li, Chen Cao, Gabriel Schwartz, Rawal Khirodkar, Christian Richardt, Tomas Simon, Yaser Sheikh, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24223v1.pdf)  
  Keywords: ar, real-time rendering, light transport, avatar, human, head, efficient, global illumination, illumination, 3d gaussian, relightable  
- **[Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization](https://arxiv.org/abs/2410.16978v1)**  
  Authors: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, Ralf Gutjahr, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16978v1.pdf)  
  Keywords: ar, medical, path tracing, understanding, efficient, vr, head, gaussian splatting  
- **[GS^3: Efficient Relighting with Triple Gaussian Splatting](https://arxiv.org/abs/2410.11419v1)**  
  Authors: Zoubin Bi, Yixin Zeng, Chong Zeng, Fan Pei, Xiang Feng, Kun Zhou, Hongzhi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11419v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://GSrelight.github.io/.)  
  Keywords: ar, relighting, shadow, efficient, lighting, global illumination, illumination, geometry, gaussian splatting  
- **[RGM: Reconstructing High-fidelity 3D Car Assets with Relightable 3D-GS Generative Model from a Single Image](https://arxiv.org/abs/2410.08181v1)**  
  Authors: Xiaoxue Chen, Jv Zheng, Hao Huang, Haoran Xu, Weihao Gu, Kangliang Chen, He xiang, Huan-ang Gao, Hao Zhao, Guyue Zhou, Yaqin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08181v1.pdf)  
  Keywords: ar, high-fidelity, nerf, relighting, autonomous driving, lighting, global illumination, illumination, geometry, 3d gaussian, relightable  
- **[6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering](https://arxiv.org/abs/2410.04974v2)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04974v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/6dgs/)  
  Keywords: ar, real-time rendering, nerf, high quality, ray tracing, 3d gaussian, gaussian splatting  
- **[GI-GS: Global Illumination Decomposition on Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2410.02619v1)**  
  Authors: Hongze Chen, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.02619v1.pdf)  
  Keywords: ar, high-fidelity, path tracing, relighting, shadow, efficient, lighting, global illumination, illumination, geometry, 3d gaussian, lightweight, gaussian splatting  

### Relighting

*Showing the latest 50 out of 129 papers*

- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: ar, survey, slam, outdoor, dynamic, face, tracking, lighting, mapping, geometry, 3d gaussian, localization, reflection  
- **[EOGS: Gaussian Splatting for Earth Observation](https://arxiv.org/abs/2412.13047v1)**  
  Authors: Luca Savant Aira, Gabriele Facciolo, Thibaud Ehret  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13047v1.pdf)  
  Keywords: ar, shadow, nerf, gaussian splatting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: ar, real-time rendering, high-fidelity, ray tracing, efficient, lighting, 3d gaussian, reflection, gaussian splatting  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: ar, nerf, face, efficient, mapping, fast, global illumination, illumination, geometry, gaussian splatting  
- **[SweepEvGS: Event-Based 3D Gaussian Splatting for Macro and Micro Radiance Field Rendering from a Single Sweep](https://arxiv.org/abs/2412.11579v1)**  
  Authors: Jingqian Wu, Shuo Zhu, Chutian Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11579v1.pdf)  
  Keywords: ar, high-fidelity, motion, dynamic, efficient, lighting, 3d gaussian, gaussian splatting  
- **[GaussianProperty: Integrating Physical Properties to 3D Gaussians with LMMs](https://arxiv.org/abs/2412.11258v1)**  
  Authors: Xinli Xu, Wenhang Ge, Dicong Qiu, ZhiFei Chen, Dongyu Yan, Zhuoyun Liu, Haoyu Zhao, Hanfeng Zhao, Shunsi Zhang, Junwei Liang, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11258v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://Gaussian-Property.github.io}{this)  
  Keywords: ar, dynamic, understanding, lighting, segmentation, 3d gaussian, recognition, robotics  
- **[PBR-NeRF: Inverse Rendering with Physics-Based Neural Fields](https://arxiv.org/abs/2412.09680v1)**  
  Authors: Sean Wu, Shamik Basu, Tim Broedermann, Luc Van Gool, Christos Sakaridis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09680v1.pdf) | [![GitHub](https://img.shields.io/github/stars/s3anwu/pbrnerf?style=social)](https://github.com/s3anwu/pbrnerf)  
  Keywords: ar, nerf, 3d reconstruction, neural rendering, illumination, geometry, 3d gaussian, gaussian splatting  
- **[Extrapolated Urban View Synthesis Benchmark](https://arxiv.org/abs/2412.05256v2)**  
  Authors: Xiangyu Han, Zhen Jia, Boyi Li, Yan Wang, Boris Ivanovic, Yurong You, Lingjie Liu, Yue Wang, Marco Pavone, Chen Feng, Yiming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.05256v2.pdf)  
  Keywords: ar, lighting, geometry, 3d gaussian, robotics, gaussian splatting  
- **[Multi-View Pose-Agnostic Change Localization with Zero Labels](https://arxiv.org/abs/2412.03911v1)**  
  Authors: Chamuditha Jayanga Galappaththige, Jason Lai, Lloyd Windrim, Donald Dansereau, Niko Suenderhauf, Dimity Miller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03911v1.pdf)  
  Keywords: ar, lighting, 3d gaussian, localization, gaussian splatting  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: ar, slam, nerf, outdoor, dynamic, understanding, tracking, lighting, mapping, localization, gaussian splatting  

### SLAM

*Showing the latest 50 out of 169 papers*

- **[GraphAvatar: Compact Head Avatars with GNN-Generated 3D Gaussians](https://arxiv.org/abs/2412.13983v1)**  
  Authors: Xiaobao Wei, Peng Chen, Ming Lu, Hui Chen, Feng Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13983v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ucwxb/GraphAvatar?style=social)](https://github.com/ucwxb/GraphAvatar)  
  Keywords: ar, nerf, avatar, compact, head, face, tracking, 3d gaussian, gaussian splatting  
- **[4D Radar-Inertial Odometry based on Gaussian Modeling and Multi-Hypothesis Scan Matching](https://arxiv.org/abs/2412.13639v1)**  
  Authors: Fernando Amodeo, Luis Merino, Fernando Caballero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13639v1.pdf)  
  Keywords: ar, slam, 4d, 3d gaussian, gaussian splatting  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: ar, survey, slam, outdoor, dynamic, face, tracking, lighting, mapping, geometry, 3d gaussian, localization, reflection  
- **[Gaussian Billboards: Expressive 2D Gaussian Splatting with Textures](https://arxiv.org/abs/2412.12734v1)**  
  Authors: Sebastian Weiss, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12734v1.pdf)  
  Keywords: ar, face, mapping, geometry, gaussian splatting  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: ar, nerf, face, efficient, mapping, fast, global illumination, illumination, geometry, gaussian splatting  
- **[SuperGSeg: Open-Vocabulary 3D Segmentation with Structured Super-Gaussians](https://arxiv.org/abs/2412.10231v1)**  
  Authors: Siyun Liang, Sen Wang, Kunyi Li, Michael Niemeyer, Stefano Gasperini, Nassir Navab, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10231v1.pdf)  
  Keywords: ar, real-time rendering, understanding, efficient, semantic, segmentation, 3d gaussian, localization, gaussian splatting  
- **[RP-SLAM: Real-time Photorealistic SLAM with Efficient 3D Gaussian Splatting](https://arxiv.org/abs/2412.09868v1)**  
  Authors: Lizhi Bai, Chunqi Tian, Jun Yang, Siyu Zhang, Masanori Suganuma, Takayuki Okatani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09868v1.pdf)  
  Keywords: ar, slam, compact, dynamic, face, efficient, mapping, 3d gaussian, gaussian splatting  
- **[MAC-Ego3D: Multi-Agent Gaussian Consensus for Real-Time Collaborative Ego-Motion and Photorealistic 3D Reconstruction](https://arxiv.org/abs/2412.09723v1)**  
  Authors: Xiaohao Xu, Feng Xue, Shibo Zhao, Yike Pan, Sebastian Scherer, Xiaonan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09723v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Xiaohao-Xu/MAC-Ego3D?style=social)](https://github.com/Xiaohao-Xu/MAC-Ego3D)  
  Keywords: ar, high-fidelity, motion, efficient, mapping, 3d reconstruction, localization  
- **[Feat2GS: Probing Visual Foundation Models with Gaussian Splatting](https://arxiv.org/abs/2412.09606v1)**  
  Authors: Yue Chen, Xingyu Chen, Anpei Chen, Gerard Pons-Moll, Yuliang Xiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09606v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fanegg.github.io/Feat2GS/.)  
  Keywords: ar, tracking, geometry, 3d gaussian, gaussian splatting  
- **[GEAL: Generalizable 3D Affordance Learning with Cross-Modal Consistency](https://arxiv.org/abs/2412.09511v1)**  
  Authors: Dongyue Lu, Lingdong Kong, Tianxin Huang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09511v1.pdf)  
  Keywords: ar, human, mapping, semantic, robotics, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 200 papers*

- **[GAGS: Granularity-Aware Feature Distillation for Language Gaussian Splatting](https://arxiv.org/abs/2412.13654v1)**  
  Authors: Yuning Peng, Haiping Wang, Yuan Liu, Chenglu Wen, Zhen Dong, Bisheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13654v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pz0826.github.io/GAGS-Webpage/)  
  Keywords: ar, understanding, semantic, segmentation, fast, 3d gaussian, gaussian splatting  
- **[Vivar: A Generative AR System for Intuitive Multi-Modal Sensor Data Presentation](https://arxiv.org/abs/2412.13509v1)**  
  Authors: Yunqi Guo, Kaiyuan Hou, Heming Fu, Hongkai Chen, Zhenyu Yan, Guoliang Xing, Xiaofan Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13509v1.pdf)  
  Keywords: ar, dynamic, understanding, semantic, 3d gaussian, gaussian splatting  
- **[GaussTR: Foundation Model-Aligned Gaussian Transformer for Self-Supervised 3D Spatial Understanding](https://arxiv.org/abs/2412.13193v1)**  
  Authors: Haoyi Jiang, Liu Liu, Tianheng Cheng, Xinjie Wang, Tianwei Lin, Zhizhong Su, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13193v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hustvl/GaussTR?style=social)](https://github.com/hustvl/GaussTR)  
  Keywords: ar, autonomous driving, understanding, semantic, 3d gaussian  
- **[CATSplat: Context-Aware Transformer with Spatial Guidance for Generalizable 3D Gaussian Splatting from A Single-View Image](https://arxiv.org/abs/2412.12906v1)**  
  Authors: Wonseok Roh, Hwanhee Jung, Jong Wook Kim, Seunggwan Lee, Innfarn Yoo, Andreas Lugmayr, Seunggeun Chi, Karthik Ramani, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12906v1.pdf)  
  Keywords: ar, 3d gaussian, understanding, gaussian splatting  
- **[EditSplat: Multi-View Fusion and Attention-Guided Optimization for View-Consistent 3D Scene Editing with 3D Gaussian Splatting](https://arxiv.org/abs/2412.11520v1)**  
  Authors: Dong In Lee, Hyeongcheol Park, Jiyoung Seo, Eunbyung Park, Hyunje Park, Ha Dam Baek, Shin Sangheon, Sangmin kim, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11520v1.pdf)  
  Keywords: ar, vr, efficient, semantic, 3d gaussian, gaussian splatting  
- **[GaussianProperty: Integrating Physical Properties to 3D Gaussians with LMMs](https://arxiv.org/abs/2412.11258v1)**  
  Authors: Xinli Xu, Wenhang Ge, Dicong Qiu, ZhiFei Chen, Dongyu Yan, Zhuoyun Liu, Haoyu Zhao, Hanfeng Zhao, Shunsi Zhang, Junwei Liang, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11258v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://Gaussian-Property.github.io}{this)  
  Keywords: ar, dynamic, understanding, lighting, segmentation, 3d gaussian, recognition, robotics  
- **[DCSEG: Decoupled 3D Open-Set Segmentation using Gaussian Splatting](https://arxiv.org/abs/2412.10972v1)**  
  Authors: Luis Wiedmann, Luca Wiehe, David Rozenberszki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10972v1.pdf)  
  Keywords: ar, efficient, 3d reconstruction, semantic, segmentation, 3d gaussian, robotics, gaussian splatting  
- **[GaussianAD: Gaussian-Centric End-to-End Autonomous Driving](https://arxiv.org/abs/2412.10371v1)**  
  Authors: Wenzhao Zheng, Junjie Wu, Yao Zheng, Sicheng Zuo, Zixun Xie, Longchao Yang, Yong Pan, Zhihui Hao, Peng Jia, Xianpeng Lang, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10371v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wzzheng/GaussianAD?style=social)](https://github.com/wzzheng/GaussianAD)  
  Keywords: ar, motion, dynamic, autonomous driving, efficient, 4d, semantic, 3d gaussian  
- **[SuperGSeg: Open-Vocabulary 3D Segmentation with Structured Super-Gaussians](https://arxiv.org/abs/2412.10231v1)**  
  Authors: Siyun Liang, Sen Wang, Kunyi Li, Michael Niemeyer, Stefano Gasperini, Nassir Navab, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10231v1.pdf)  
  Keywords: ar, real-time rendering, understanding, efficient, semantic, segmentation, 3d gaussian, localization, gaussian splatting  
- **[TSGaussian: Semantic and Depth-Guided Target-Specific Gaussian Splatting from Sparse Views](https://arxiv.org/abs/2412.10051v1)**  
  Authors: Liang Zhao, Zehan Bao, Yi Xie, Hong Chen, Yaohui Chen, Weifu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10051v1.pdf) | [![GitHub](https://img.shields.io/github/stars/leon2000-ai/TSGaussian?style=social)](https://github.com/leon2000-ai/TSGaussian)  
  Keywords: ar, sparse view, compact, semantic, segmentation, geometry, 3d gaussian, gaussian splatting  



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