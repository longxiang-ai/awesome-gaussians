# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-01-19 00:49:10

## Categories

- [3DGS Surveys](#3dgs-surveys) (20 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (359 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1240 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (412 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (461 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (89 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (411 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (68 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (457 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (202 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (28 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (136 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (181 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (216 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: 3d gaussian, outdoor, tracking, geometry, survey, face, slam, lighting, dynamic, mapping, ar, reflection, localization  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: 3d gaussian, illumination, survey, recognition, ar, gaussian splatting  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: autonomous driving, geometry, compact, 3d reconstruction, high-fidelity, nerf, semantic, survey, lighting, dynamic, ar, gaussian splatting, robotics  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: 3d gaussian, real-time rendering, nerf, understanding, survey, ar, gaussian splatting, robotics  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, nerf, survey, lighting, ar, gaussian splatting  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: 3d gaussian, vr, autonomous driving, 3d reconstruction, nerf, survey, ar, gaussian splatting, robotics  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: 3d gaussian, survey, ar  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v2)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v2.pdf)  
  Keywords: 3d gaussian, efficient, real-time rendering, understanding, survey, ar, gaussian splatting  
- **[Survey on Fundamental Deep Learning 3D Reconstruction Techniques](https://arxiv.org/abs/2407.08137v1)**  
  Authors: Yonge Bai, LikHang Wong, TszYin Twan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.08137v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, nerf, survey, lighting, ar, gaussian splatting  
- **[Panopticon: a telescope for our times](https://arxiv.org/abs/2407.05103v2)**  
  Authors: Will Saunders, Timothy Chin, Michael Goodwin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05103v2.pdf)  
  Keywords: survey, ar  

### Acceleration

*Showing the latest 50 out of 359 papers*

- **[Object-Centric 2D Gaussian Splatting: Background Removal and Occlusion-Aware Pruning for Compact Object Models](https://arxiv.org/abs/2501.08174v1)**  
  Authors: Marcel Rogge, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08174v1.pdf)  
  Keywords: compact, fast, ar, gaussian splatting  
- **[ActiveGAMER: Active GAussian Mapping through Efficient Rendering](https://arxiv.org/abs/2501.06897v1)**  
  Authors: Liyan Chen, Huangying Zhan, Kevin Chen, Xiangyu Xu, Qingan Yan, Changjiang Cai, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06897v1.pdf)  
  Keywords: 3d gaussian, efficient, efficient rendering, nerf, dynamic, mapping, ar, gaussian splatting  
- **[MapGS: Generalizable Pretraining and Data Augmentation for Online Mapping via Novel View Synthesis](https://arxiv.org/abs/2501.06660v1)**  
  Authors: Hengyuan Zhang, David Paz, Yuliang Guo, Xinyu Huang, Henrik I. Christensen, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06660v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://henryzhangzhy.github.io/mapgs.)  
  Keywords: efficient, fast, mapping, ar, gaussian splatting  
- **[Locality-aware Gaussian Compression for Fast and High-quality Rendering](https://arxiv.org/abs/2501.05757v1)**  
  Authors: Seungjoo Shin, Jaesik Park, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.05757v1.pdf)  
  Keywords: 3d gaussian, compact, fast, compression, ar, gaussian splatting  
- **[FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency](https://arxiv.org/abs/2501.04628v1)**  
  Authors: Han Huang, Yulun Wu, Chao Deng, Ge Gao, Ming Gu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04628v1.pdf)  
  Keywords: sparse-view, fast, face, sparse view, ar, gaussian splatting  
- **[CrossView-GS: Cross-view Gaussian Splatting For Large-scale Scene Reconstruction](https://arxiv.org/abs/2501.01695v1)**  
  Authors: Chenhao Zhang, Yuanping Cao, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01695v1.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, gaussian splatting  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: 3d gaussian, motion, outdoor, real-time rendering, understanding, dynamic, ar  
- **[PanoSLAM: Panoptic 3D Scene Reconstruction via Gaussian SLAM](https://arxiv.org/abs/2501.00352v1)**  
  Authors: Runnan Chen, Zhaoqing Wang, Jiepeng Wang, Yuexin Ma, Mingming Gong, Wenping Wang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00352v1.pdf) | [![GitHub](https://img.shields.io/github/stars/runnanchen/PanoSLAM?style=social)](https://github.com/runnanchen/PanoSLAM)  
  Keywords: 3d gaussian, efficient, tracking, efficient rendering, 3d reconstruction, semantic, understanding, slam, segmentation, mapping, ar, gaussian splatting, localization, robotics  
- **[KeyGS: A Keyframe-Centric Gaussian Splatting Method for Monocular Image Sequences](https://arxiv.org/abs/2412.20767v1)**  
  Authors: Keng-Wei Chang, Zi-Ming Wang, Shang-Hong Lai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20767v1.pdf)  
  Keywords: 3d gaussian, motion, efficient, real-time rendering, ar, gaussian splatting  
- **[4D Gaussian Splatting: Modeling Dynamic Scenes with Native 4D Primitives](https://arxiv.org/abs/2412.20720v1)**  
  Authors: Zeyu Yang, Zijie Pan, Xiatian Zhu, Li Zhang, Yu-Gang Jiang, Philip H. S. Torr  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20720v1.pdf)  
  Keywords: motion, vr, geometry, 4d, compact, real-time rendering, understanding, dynamic, ar, gaussian splatting  

### Applications

*Showing the latest 50 out of 1240 papers*

- **[Creating Virtual Environments with 3D Gaussian Splatting: A Comparative Study](https://arxiv.org/abs/2501.09302v1)**  
  Authors: Shi Qiu, Binzhu Xie, Qixuan Liu, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.09302v1.pdf)  
  Keywords: 3d gaussian, efficient, ar, gaussian splatting  
- **[CityLoc: 6 DoF Localization of Text Descriptions in Large-Scale Scenes with Gaussian Representation](https://arxiv.org/abs/2501.08982v1)**  
  Authors: Qi Ma, Runyi Yang, Bin Ren, Ender Konukoglu, Luc Van Gool, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08982v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, localization  
- **[GS-LIVO: Real-Time LiDAR, Inertial, and Visual Multi-sensor Fused Odometry with Gaussian Mapping](https://arxiv.org/abs/2501.08672v1)**  
  Authors: Sheng Hong, Chunran Zheng, Yishu Shen, Changze Li, Fu Zhang, Tong Qin, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08672v1.pdf)  
  Keywords: 3d gaussian, motion, slam, face, mapping, ar, gaussian splatting, localization  
- **[3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering](https://arxiv.org/abs/2501.08370v1)**  
  Authors: Meenakshi Krishnan, Liam Fowl, Ramani Duraiswami  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08370v1.pdf)  
  Keywords: 3d gaussian, efficient, vr, geometry, nerf, face, animation, ar, gaussian splatting  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: outdoor, geometry, large scene, nerf, slam, dynamic, mapping, ar, gaussian splatting, localization  
- **[Object-Centric 2D Gaussian Splatting: Background Removal and Occlusion-Aware Pruning for Compact Object Models](https://arxiv.org/abs/2501.08174v1)**  
  Authors: Marcel Rogge, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08174v1.pdf)  
  Keywords: compact, fast, ar, gaussian splatting  
- **[UnCommon Objects in 3D](https://arxiv.org/abs/2501.07574v1)**  
  Authors: Xingchen Liu, Piyush Tayal, Jianyuan Wang, Jesus Zarzar, Tom Monnier, Konstantinos Tertikas, Jiali Duan, Antoine Toisoul, Jason Y. Zhang, Natalia Neverova, Andrea Vedaldi, Roman Shapovalov, David Novotny  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07574v1.pdf)  
  Keywords: 3d gaussian, ar  
- **[3DGS-to-PC: Convert a 3D Gaussian Splatting Scene into a Dense Point Cloud or Mesh](https://arxiv.org/abs/2501.07478v1)**  
  Authors: Lewis A G Stuart, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07478v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, face, ar, gaussian splatting  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: medical, nerf, face, dynamic, lighting, sparse view, human, ar, gaussian splatting  
- **[RMAvatar: Photorealistic Human Avatar Reconstruction from Monocular Video Based on Rectified Mesh-embedded Gaussians](https://arxiv.org/abs/2501.07104v1)**  
  Authors: Sen Peng, Weixing Xie, Zilong Wang, Xiaohu Guo, Zhonggui Chen, Baorong Yang, Xiao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07104v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rm-avatar.github.io.)  
  Keywords: motion, deformation, geometry, face, avatar, human, ar, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 412 papers*

- **[GS-LIVO: Real-Time LiDAR, Inertial, and Visual Multi-sensor Fused Odometry with Gaussian Mapping](https://arxiv.org/abs/2501.08672v1)**  
  Authors: Sheng Hong, Chunran Zheng, Yishu Shen, Changze Li, Fu Zhang, Tong Qin, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08672v1.pdf)  
  Keywords: 3d gaussian, motion, slam, face, mapping, ar, gaussian splatting, localization  
- **[3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering](https://arxiv.org/abs/2501.08370v1)**  
  Authors: Meenakshi Krishnan, Liam Fowl, Ramani Duraiswami  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08370v1.pdf)  
  Keywords: 3d gaussian, efficient, vr, geometry, nerf, face, animation, ar, gaussian splatting  
- **[3DGS-to-PC: Convert a 3D Gaussian Splatting Scene into a Dense Point Cloud or Mesh](https://arxiv.org/abs/2501.07478v1)**  
  Authors: Lewis A G Stuart, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07478v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, face, ar, gaussian splatting  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: medical, nerf, face, dynamic, lighting, sparse view, human, ar, gaussian splatting  
- **[RMAvatar: Photorealistic Human Avatar Reconstruction from Monocular Video Based on Rectified Mesh-embedded Gaussians](https://arxiv.org/abs/2501.07104v1)**  
  Authors: Sen Peng, Weixing Xie, Zilong Wang, Xiaohu Guo, Zhonggui Chen, Baorong Yang, Xiao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07104v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rm-avatar.github.io.)  
  Keywords: motion, deformation, geometry, face, avatar, human, ar, gaussian splatting  
- **[Synthetic Prior for Few-Shot Drivable Head Avatar Inversion](https://arxiv.org/abs/2501.06903v1)**  
  Authors: Wojciech Zielonka, Stephan J. Garbin, Alexandros Lattas, George Kopanas, Paulo Gotardo, Thabo Beeler, Justus Thies, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06903v1.pdf)  
  Keywords: 3d gaussian, few-shot, avatar, ar, head, gaussian splatting  
- **[NVS-SQA: Exploring Self-Supervised Quality Representation Learning for Neurally Synthesized Scenes without References](https://arxiv.org/abs/2501.06488v1)**  
  Authors: Qiang Qu, Yiran Shen, Xiaoming Chen, Yuk Ying Chung, Weidong Cai, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06488v1.pdf)  
  Keywords: 3d gaussian, nerf, sparse view, human, ar, gaussian splatting  
- **[Arc2Avatar: Generating Expressive 3D Avatars from a Single Image via ID Guidance](https://arxiv.org/abs/2501.05379v2)**  
  Authors: Dimitrios Gerogiannis, Foivos Paraperas Papantoniou, Rolandos Alexandros Potamias, Alexandros Lattas, Stefanos Zafeiriou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.05379v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://arc2avatar.github.io)  
  Keywords: 3d gaussian, efficient, face, avatar, ar, human, head, gaussian splatting  
- **[GaussianVideo: Efficient Video Representation via Hierarchical Gaussian Splatting](https://arxiv.org/abs/2501.04782v1)**  
  Authors: Andrew Bond, Jui-Hsien Wang, Long Mai, Erkut Erdem, Aykut Erdem  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04782v1.pdf)  
  Keywords: 3d gaussian, motion, efficient, face, compression, dynamic, ar, gaussian splatting  
- **[FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency](https://arxiv.org/abs/2501.04628v1)**  
  Authors: Han Huang, Yulun Wu, Chao Deng, Ge Gao, Ming Gu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04628v1.pdf)  
  Keywords: sparse-view, fast, face, sparse view, ar, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 461 papers*

- **[GS-LIVO: Real-Time LiDAR, Inertial, and Visual Multi-sensor Fused Odometry with Gaussian Mapping](https://arxiv.org/abs/2501.08672v1)**  
  Authors: Sheng Hong, Chunran Zheng, Yishu Shen, Changze Li, Fu Zhang, Tong Qin, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08672v1.pdf)  
  Keywords: 3d gaussian, motion, slam, face, mapping, ar, gaussian splatting, localization  
- **[3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering](https://arxiv.org/abs/2501.08370v1)**  
  Authors: Meenakshi Krishnan, Liam Fowl, Ramani Duraiswami  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08370v1.pdf)  
  Keywords: 3d gaussian, efficient, vr, geometry, nerf, face, animation, ar, gaussian splatting  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: outdoor, geometry, large scene, nerf, slam, dynamic, mapping, ar, gaussian splatting, localization  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: medical, nerf, face, dynamic, lighting, sparse view, human, ar, gaussian splatting  
- **[RMAvatar: Photorealistic Human Avatar Reconstruction from Monocular Video Based on Rectified Mesh-embedded Gaussians](https://arxiv.org/abs/2501.07104v1)**  
  Authors: Sen Peng, Weixing Xie, Zilong Wang, Xiaohu Guo, Zhonggui Chen, Baorong Yang, Xiao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07104v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rm-avatar.github.io.)  
  Keywords: motion, deformation, geometry, face, avatar, human, ar, gaussian splatting  
- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: 3d gaussian, motion, efficient, geometry, 3d reconstruction, high-fidelity, nerf, slam, dynamic, mapping, ar, gaussian splatting  
- **[CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications](https://arxiv.org/abs/2501.06927v1)**  
  Authors: Xinyi Zheng, Steve Zhang, Weizhe Lin, Aaron Zhang, Walterio W. Mayol-Cuevas, Junxiao Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06927v1.pdf)  
  Keywords: motion, 3d reconstruction, nerf, slam, segmentation, ar, gaussian splatting  
- **[ActiveGAMER: Active GAussian Mapping through Efficient Rendering](https://arxiv.org/abs/2501.06897v1)**  
  Authors: Liyan Chen, Huangying Zhan, Kevin Chen, Xiangyu Xu, Qingan Yan, Changjiang Cai, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06897v1.pdf)  
  Keywords: 3d gaussian, efficient, efficient rendering, nerf, dynamic, mapping, ar, gaussian splatting  
- **[F3D-Gaus: Feed-forward 3D-aware Generation on ImageNet with Cycle-Consistent Gaussian Splatting](https://arxiv.org/abs/2501.06714v1)**  
  Authors: Yuxin Wang, Qianyi Wu, Dan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06714v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, dynamic  
- **[Scaffold-SLAM: Structured 3D Gaussians for Simultaneous Localization and Photorealistic Mapping](https://arxiv.org/abs/2501.05242v1)**  
  Authors: Wen Tianci, Liu Zhiang, Lu Biao, Fang Yongchun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.05242v1.pdf)  
  Keywords: 3d gaussian, motion, slam, mapping, ar, gaussian splatting, localization  

### Few-shot

*Showing the latest 50 out of 89 papers*

- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: medical, nerf, face, dynamic, lighting, sparse view, human, ar, gaussian splatting  
- **[Synthetic Prior for Few-Shot Drivable Head Avatar Inversion](https://arxiv.org/abs/2501.06903v1)**  
  Authors: Wojciech Zielonka, Stephan J. Garbin, Alexandros Lattas, George Kopanas, Paulo Gotardo, Thabo Beeler, Justus Thies, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06903v1.pdf)  
  Keywords: 3d gaussian, few-shot, avatar, ar, head, gaussian splatting  
- **[NVS-SQA: Exploring Self-Supervised Quality Representation Learning for Neurally Synthesized Scenes without References](https://arxiv.org/abs/2501.06488v1)**  
  Authors: Qiang Qu, Yiran Shen, Xiaoming Chen, Yuk Ying Chung, Weidong Cai, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06488v1.pdf)  
  Keywords: 3d gaussian, nerf, sparse view, human, ar, gaussian splatting  
- **[FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency](https://arxiv.org/abs/2501.04628v1)**  
  Authors: Han Huang, Yulun Wu, Chao Deng, Ge Gao, Ming Gu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04628v1.pdf)  
  Keywords: sparse-view, fast, face, sparse view, ar, gaussian splatting  
- **[Dust to Tower: Coarse-to-Fine Photo-Realistic Scene Reconstruction from Sparse Uncalibrated Images](https://arxiv.org/abs/2412.19518v1)**  
  Authors: Xudong Cai, Yongcai Wang, Zhaoxin Fan, Deng Haoran, Shuo Wang, Wanting Li, Deying Li, Lun Luo, Minhang Wang, Jintao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19518v1.pdf)  
  Keywords: 3d gaussian, sparse-view, efficient, fast, ar, gaussian splatting  
- **[CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting](https://arxiv.org/abs/2412.19142v1)**  
  Authors: Siyu Jiao, Haoye Dong, Yuyang Yin, Zequn Jie, Yinlong Qian, Yao Zhao, Humphrey Shi, Yunchao Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19142v1.pdf)  
  Keywords: 3d gaussian, efficient, few-shot, ar, gaussian splatting  
- **[SolidGS: Consolidating Gaussian Surfel Splatting for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2412.15400v1)**  
  Authors: Zhuowen Shen, Yuan Liu, Zhang Chen, Zhong Li, Jiepeng Wang, Yongqing Liang, Zhengming Yu, Jingdong Zhang, Yi Xu, Scott Schaefer, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15400v1.pdf)  
  Keywords: sparse-view, geometry, face, sparse view, ar, gaussian splatting  
- **[Improving Geometry in Sparse-View 3DGS via Reprojection-based DoF Separation](https://arxiv.org/abs/2412.14568v1)**  
  Authors: Yongsung Kim, Minjun Park, Jooyoung Choi, Sungroh Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.14568v1.pdf)  
  Keywords: 3d gaussian, sparse-view, geometry, 3d reconstruction, ar, gaussian splatting  
- **[Real-time Free-view Human Rendering from Sparse-view RGB Videos using Double Unprojected Textures](https://arxiv.org/abs/2412.13183v1)**  
  Authors: Guoxing Sun, Rishabh Dabral, Heming Zhu, Pascal Fua, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13183v1.pdf)  
  Keywords: sparse-view, deformation, geometry, body, human, ar  
- **[4DRGS: 4D Radiative Gaussian Splatting for Efficient 3D Vessel Reconstruction from Sparse-View Dynamic DSA Images](https://arxiv.org/abs/2412.12919v1)**  
  Authors: Zhentao Liu, Ruyi Zha, Huangxuan Zhao, Hongdong Li, Zhiming Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12919v1.pdf)  
  Keywords: sparse-view, efficient, geometry, 4d, compact, medical, fast, dynamic, ar, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 411 papers*

- **[3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering](https://arxiv.org/abs/2501.08370v1)**  
  Authors: Meenakshi Krishnan, Liam Fowl, Ramani Duraiswami  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08370v1.pdf)  
  Keywords: 3d gaussian, efficient, vr, geometry, nerf, face, animation, ar, gaussian splatting  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: outdoor, geometry, large scene, nerf, slam, dynamic, mapping, ar, gaussian splatting, localization  
- **[3DGS-to-PC: Convert a 3D Gaussian Splatting Scene into a Dense Point Cloud or Mesh](https://arxiv.org/abs/2501.07478v1)**  
  Authors: Lewis A G Stuart, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07478v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, face, ar, gaussian splatting  
- **[RMAvatar: Photorealistic Human Avatar Reconstruction from Monocular Video Based on Rectified Mesh-embedded Gaussians](https://arxiv.org/abs/2501.07104v1)**  
  Authors: Sen Peng, Weixing Xie, Zilong Wang, Xiaohu Guo, Zhonggui Chen, Baorong Yang, Xiao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07104v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rm-avatar.github.io.)  
  Keywords: motion, deformation, geometry, face, avatar, human, ar, gaussian splatting  
- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: 3d gaussian, motion, efficient, geometry, 3d reconstruction, high-fidelity, nerf, slam, dynamic, mapping, ar, gaussian splatting  
- **[CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications](https://arxiv.org/abs/2501.06927v1)**  
  Authors: Xinyi Zheng, Steve Zhang, Weizhe Lin, Aaron Zhang, Walterio W. Mayol-Cuevas, Junxiao Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06927v1.pdf)  
  Keywords: motion, 3d reconstruction, nerf, slam, segmentation, ar, gaussian splatting  
- **[F3D-Gaus: Feed-forward 3D-aware Generation on ImageNet with Cycle-Consistent Gaussian Splatting](https://arxiv.org/abs/2501.06714v1)**  
  Authors: Yuxin Wang, Qianyi Wu, Dan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06714v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, dynamic  
- **[ConcealGS: Concealing Invisible Copyright Information in 3D Gaussian Splatting](https://arxiv.org/abs/2501.03605v1)**  
  Authors: Yifeng Yang, Hengyu Liu, Chenxin Li, Yining Sun, Wuyang Li, Yifan Liu, Yiyang Lin, Yixuan Yuan, Nanyang Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.03605v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, nerf, ar, gaussian splatting  
- **[Gaussian Building Mesh (GBM): Extract a Building's 3D Mesh with Google Earth and Gaussian Splatting](https://arxiv.org/abs/2501.00625v2)**  
  Authors: Kyle Gao, Liangzhi Li, Hongjie He, Dening Lu, Linlin Xu, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00625v2.pdf)  
  Keywords: geometry, ar, segmentation, gaussian splatting  
- **[DreamDrive: Generative 4D Scene Modeling from Street View Images](https://arxiv.org/abs/2501.00601v2)**  
  Authors: Jiageng Mao, Boyi Li, Boris Ivanovic, Yuxiao Chen, Yan Wang, Yurong You, Chaowei Xiao, Danfei Xu, Marco Pavone, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00601v2.pdf)  
  Keywords: autonomous driving, neural rendering, 4d, geometry, dynamic, ar, gaussian splatting  

### Large Scene

*Showing the latest 50 out of 68 papers*

- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: outdoor, geometry, large scene, nerf, slam, dynamic, mapping, ar, gaussian splatting, localization  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: 3d gaussian, motion, outdoor, real-time rendering, understanding, dynamic, ar  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: 3d gaussian, efficient, outdoor, neural rendering, nerf, slam, mapping, ar, gaussian splatting  
- **[WeatherGS: 3D Scene Reconstruction in Adverse Weather Conditions via Gaussian Splatting](https://arxiv.org/abs/2412.18862v2)**  
  Authors: Chenghao Qian, Yuhu Guo, Wenjing Li, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.18862v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/weather-gs.)  
  Keywords: 3d gaussian, outdoor, 3d reconstruction, ar, gaussian splatting  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: 3d gaussian, large scene, fast, high-fidelity, nerf, face, compression, ar, gaussian splatting  
- **[LiHi-GS: LiDAR-Supervised Gaussian Splatting for Highway Driving Scene Reconstruction](https://arxiv.org/abs/2412.15447v2)**  
  Authors: Pou-Chun Kung, Xianling Zhang, Katherine A. Skinner, Nikita Jaipuria  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15447v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/lihi_gs)  
  Keywords: 3d gaussian, autonomous driving, fast, nerf, dynamic, urban scene, ar, gaussian splatting  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: 3d gaussian, outdoor, tracking, geometry, survey, face, slam, lighting, dynamic, mapping, ar, reflection, localization  
- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: 3d gaussian, large scene, dynamic, ar, head, gaussian splatting  
- **[HybridGS: Decoupling Transients and Statics with 2D and 3D Gaussian Splatting](https://arxiv.org/abs/2412.03844v2)**  
  Authors: Jingyu Lin, Jiaqi Gu, Lubin Fan, Bojian Wu, Yujing Lou, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03844v2.pdf)  
  Keywords: 3d gaussian, outdoor, ar, gaussian splatting  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: deformation, 4d, semantic, face, dynamic, urban scene, ar, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 457 papers*

- **[Creating Virtual Environments with 3D Gaussian Splatting: A Comparative Study](https://arxiv.org/abs/2501.09302v1)**  
  Authors: Shi Qiu, Binzhu Xie, Qixuan Liu, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.09302v1.pdf)  
  Keywords: 3d gaussian, efficient, ar, gaussian splatting  
- **[3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering](https://arxiv.org/abs/2501.08370v1)**  
  Authors: Meenakshi Krishnan, Liam Fowl, Ramani Duraiswami  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08370v1.pdf)  
  Keywords: 3d gaussian, efficient, vr, geometry, nerf, face, animation, ar, gaussian splatting  
- **[Object-Centric 2D Gaussian Splatting: Background Removal and Occlusion-Aware Pruning for Compact Object Models](https://arxiv.org/abs/2501.08174v1)**  
  Authors: Marcel Rogge, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08174v1.pdf)  
  Keywords: compact, fast, ar, gaussian splatting  
- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: 3d gaussian, motion, efficient, geometry, 3d reconstruction, high-fidelity, nerf, slam, dynamic, mapping, ar, gaussian splatting  
- **[ActiveGAMER: Active GAussian Mapping through Efficient Rendering](https://arxiv.org/abs/2501.06897v1)**  
  Authors: Liyan Chen, Huangying Zhan, Kevin Chen, Xiangyu Xu, Qingan Yan, Changjiang Cai, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06897v1.pdf)  
  Keywords: 3d gaussian, efficient, efficient rendering, nerf, dynamic, mapping, ar, gaussian splatting  
- **[Generalized and Efficient 2D Gaussian Splatting for Arbitrary-scale Super-Resolution](https://arxiv.org/abs/2501.06838v2)**  
  Authors: Du Chen, Liyi Chen, Zhengqiang Zhang, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06838v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mt-cly.github.io/GSASR.github.io/}.)  
  Keywords: efficient, ar, gaussian splatting  
- **[MapGS: Generalizable Pretraining and Data Augmentation for Online Mapping via Novel View Synthesis](https://arxiv.org/abs/2501.06660v1)**  
  Authors: Hengyuan Zhang, David Paz, Yuliang Guo, Xinyu Huang, Henrik I. Christensen, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06660v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://henryzhangzhy.github.io/mapgs.)  
  Keywords: efficient, fast, mapping, ar, gaussian splatting  
- **[Locality-aware Gaussian Compression for Fast and High-quality Rendering](https://arxiv.org/abs/2501.05757v1)**  
  Authors: Seungjoo Shin, Jaesik Park, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.05757v1.pdf)  
  Keywords: 3d gaussian, compact, fast, compression, ar, gaussian splatting  
- **[Zero-1-to-G: Taming Pretrained 2D Diffusion Model for Direct 3D Generation](https://arxiv.org/abs/2501.05427v1)**  
  Authors: Xuyi Meng, Chen Wang, Jiahui Lei, Kostas Daniilidis, Jiatao Gu, Lingjie Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.05427v1.pdf)  
  Keywords: efficient, ar  
- **[Arc2Avatar: Generating Expressive 3D Avatars from a Single Image via ID Guidance](https://arxiv.org/abs/2501.05379v2)**  
  Authors: Dimitrios Gerogiannis, Foivos Paraperas Papantoniou, Rolandos Alexandros Potamias, Alexandros Lattas, Stefanos Zafeiriou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.05379v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://arc2avatar.github.io)  
  Keywords: 3d gaussian, efficient, face, avatar, ar, human, head, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 202 papers*

- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: 3d gaussian, motion, efficient, geometry, 3d reconstruction, high-fidelity, nerf, slam, dynamic, mapping, ar, gaussian splatting  
- **[Gaussian Masked Autoencoders](https://arxiv.org/abs/2501.03229v1)**  
  Authors: Jathushan Rajasegaran, Xinlei Chen, Rulilong Li, Christoph Feichtenhofer, Jitendra Malik, Shiry Ginosar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.03229v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://brjathu.github.io/gmae)  
  Keywords: 3d gaussian, high-fidelity, semantic, understanding, segmentation, ar, gaussian splatting  
- **[Deformable Gaussian Splatting for Efficient and High-Fidelity Reconstruction of Surgical Scenes](https://arxiv.org/abs/2501.01101v1)**  
  Authors: Jiwei Shan, Zeyu Cai, Cheng-Tai Hsieh, Shing Shin Cheng, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01101v1.pdf)  
  Keywords: 3d gaussian, motion, efficient, deformation, high-fidelity, dynamic, ar, gaussian splatting  
- **[ActiveGS: Active Scene Reconstruction using Gaussian Splatting](https://arxiv.org/abs/2412.17769v1)**  
  Authors: Liren Jin, Xingguang Zhong, Yue Pan, Jens Behley, Cyrill Stachniss, Marija Popović  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17769v1.pdf)  
  Keywords: robotics, ar, gaussian splatting, high-fidelity  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: 3d gaussian, large scene, fast, high-fidelity, nerf, face, compression, ar, gaussian splatting  
- **[SqueezeMe: Efficient Gaussian Avatars for VR](https://arxiv.org/abs/2412.15171v2)**  
  Authors: Shunsuke Saito, Stanislav Pidhorskyi, Igor Santesteban, Forrest Iandola, Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Frank Yu, Emanuel Garbin, Tomas Simon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15171v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://forresti.github.io/squeezeme.)  
  Keywords: motion, efficient, vr, high quality, avatar, ar, human, head, gaussian splatting  
- **[HyperGS: Hyperspectral 3D Gaussian Splatting](https://arxiv.org/abs/2412.12849v1)**  
  Authors: Christopher Thirgood, Oscar Mendez, Erin Chao Ling, Jon Storey, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12849v1.pdf)  
  Keywords: 3d gaussian, 4d, high-fidelity, ar, gaussian splatting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: 3d gaussian, reflection, efficient, real-time rendering, high-fidelity, ray tracing, lighting, ar, gaussian splatting  
- **[Deformable Radial Kernel Splatting](https://arxiv.org/abs/2412.11752v1)**  
  Authors: Yi-Hua Huang, Ming-Xian Lin, Yang-Tian Sun, Ziyi Yang, Xiaoyang Lyu, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11752v1.pdf)  
  Keywords: efficient, geometry, high-fidelity, ar, gaussian splatting  
- **[SweepEvGS: Event-Based 3D Gaussian Splatting for Macro and Micro Radiance Field Rendering from a Single Sweep](https://arxiv.org/abs/2412.11579v1)**  
  Authors: Jingqian Wu, Shuo Zhu, Chutian Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11579v1.pdf)  
  Keywords: 3d gaussian, motion, efficient, high-fidelity, dynamic, lighting, ar, gaussian splatting  

### Ray Tracing

- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: relighting, efficient, ray tracing, lighting, gaussian splatting, ar, reflection  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: 3d gaussian, reflection, efficient, real-time rendering, high-fidelity, ray tracing, lighting, ar, gaussian splatting  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: illumination, efficient, global illumination, geometry, fast, nerf, face, mapping, ar, gaussian splatting  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v1.pdf)  
  Keywords: 3d gaussian, efficient, ray tracing, ar, gaussian splatting  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: 3d gaussian, ar, gaussian splatting, ray tracing  
- **[URAvatar: Universal Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2410.24223v1)**  
  Authors: Junxuan Li, Chen Cao, Gabriel Schwartz, Rawal Khirodkar, Christian Richardt, Tomas Simon, Yaser Sheikh, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24223v1.pdf)  
  Keywords: 3d gaussian, illumination, global illumination, relightable, efficient, real-time rendering, avatar, ar, human, head, light transport  
- **[Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization](https://arxiv.org/abs/2410.16978v1)**  
  Authors: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, Ralf Gutjahr, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16978v1.pdf)  
  Keywords: efficient, vr, path tracing, medical, understanding, ar, head, gaussian splatting  
- **[GS^3: Efficient Relighting with Triple Gaussian Splatting](https://arxiv.org/abs/2410.11419v1)**  
  Authors: Zoubin Bi, Yixin Zeng, Chong Zeng, Fan Pei, Xiang Feng, Kun Zhou, Hongzhi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11419v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://GSrelight.github.io/.)  
  Keywords: illumination, relighting, global illumination, efficient, shadow, geometry, lighting, ar, gaussian splatting  
- **[RGM: Reconstructing High-fidelity 3D Car Assets with Relightable 3D-GS Generative Model from a Single Image](https://arxiv.org/abs/2410.08181v1)**  
  Authors: Xiaoxue Chen, Jv Zheng, Hao Huang, Haoran Xu, Weihao Gu, Kangliang Chen, He xiang, Huan-ang Gao, Hao Zhao, Guyue Zhou, Yaqin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08181v1.pdf)  
  Keywords: 3d gaussian, relighting, global illumination, relightable, illumination, autonomous driving, geometry, high-fidelity, nerf, lighting, ar  
- **[6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering](https://arxiv.org/abs/2410.04974v2)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04974v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/6dgs/)  
  Keywords: 3d gaussian, real-time rendering, high quality, nerf, ray tracing, ar, gaussian splatting  

### Relighting

*Showing the latest 50 out of 136 papers*

- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: medical, nerf, face, dynamic, lighting, sparse view, human, ar, gaussian splatting  
- **[Reflective Gaussian Splatting](https://arxiv.org/abs/2412.19282v1)**  
  Authors: Yuxuan Yao, Zixuan Zeng, Chun Gu, Xiatian Zhu, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19282v1.pdf)  
  Keywords: relighting, geometry, nerf, lighting, gaussian splatting, ar, reflection  
- **[Generating Editable Head Avatars with 3D Gaussian GANs](https://arxiv.org/abs/2412.19149v1)**  
  Authors: Guohao Li, Hongyu Yang, Yifang Men, Di Huang, Weixin Li, Ruijie Yang, Yunhong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19149v1.pdf) | [![GitHub](https://img.shields.io/github/stars/liguohao96/EGG3D?style=social)](https://github.com/liguohao96/EGG3D)  
  Keywords: 3d gaussian, illumination, deformation, nerf, face, avatar, ar, animation, head, gaussian splatting  
- **[FaceLift: Single Image to 3D Head with View Generation and GS-LRM](https://arxiv.org/abs/2412.17812v1)**  
  Authors: Weijie Lyu, Yi Zhou, Ming-Hsuan Yang, Zhixin Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17812v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weijielyu.github.io/FaceLift.)  
  Keywords: 4d, face, lighting, ar, human, animation, head  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: relighting, efficient, ray tracing, lighting, gaussian splatting, ar, reflection  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: 3d gaussian, outdoor, tracking, geometry, survey, face, slam, lighting, dynamic, mapping, ar, reflection, localization  
- **[EOGS: Gaussian Splatting for Earth Observation](https://arxiv.org/abs/2412.13047v1)**  
  Authors: Luca Savant Aira, Gabriele Facciolo, Thibaud Ehret  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13047v1.pdf)  
  Keywords: ar, gaussian splatting, shadow, nerf  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: 3d gaussian, reflection, efficient, real-time rendering, high-fidelity, ray tracing, lighting, ar, gaussian splatting  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: illumination, efficient, global illumination, geometry, fast, nerf, face, mapping, ar, gaussian splatting  
- **[SweepEvGS: Event-Based 3D Gaussian Splatting for Macro and Micro Radiance Field Rendering from a Single Sweep](https://arxiv.org/abs/2412.11579v1)**  
  Authors: Jingqian Wu, Shuo Zhu, Chutian Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11579v1.pdf)  
  Keywords: 3d gaussian, motion, efficient, high-fidelity, dynamic, lighting, ar, gaussian splatting  

### SLAM

*Showing the latest 50 out of 181 papers*

- **[CityLoc: 6 DoF Localization of Text Descriptions in Large-Scale Scenes with Gaussian Representation](https://arxiv.org/abs/2501.08982v1)**  
  Authors: Qi Ma, Runyi Yang, Bin Ren, Ender Konukoglu, Luc Van Gool, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08982v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, localization  
- **[GS-LIVO: Real-Time LiDAR, Inertial, and Visual Multi-sensor Fused Odometry with Gaussian Mapping](https://arxiv.org/abs/2501.08672v1)**  
  Authors: Sheng Hong, Chunran Zheng, Yishu Shen, Changze Li, Fu Zhang, Tong Qin, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08672v1.pdf)  
  Keywords: 3d gaussian, motion, slam, face, mapping, ar, gaussian splatting, localization  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: outdoor, geometry, large scene, nerf, slam, dynamic, mapping, ar, gaussian splatting, localization  
- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: 3d gaussian, motion, efficient, geometry, 3d reconstruction, high-fidelity, nerf, slam, dynamic, mapping, ar, gaussian splatting  
- **[CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications](https://arxiv.org/abs/2501.06927v1)**  
  Authors: Xinyi Zheng, Steve Zhang, Weizhe Lin, Aaron Zhang, Walterio W. Mayol-Cuevas, Junxiao Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06927v1.pdf)  
  Keywords: motion, 3d reconstruction, nerf, slam, segmentation, ar, gaussian splatting  
- **[ActiveGAMER: Active GAussian Mapping through Efficient Rendering](https://arxiv.org/abs/2501.06897v1)**  
  Authors: Liyan Chen, Huangying Zhan, Kevin Chen, Xiangyu Xu, Qingan Yan, Changjiang Cai, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06897v1.pdf)  
  Keywords: 3d gaussian, efficient, efficient rendering, nerf, dynamic, mapping, ar, gaussian splatting  
- **[MapGS: Generalizable Pretraining and Data Augmentation for Online Mapping via Novel View Synthesis](https://arxiv.org/abs/2501.06660v1)**  
  Authors: Hengyuan Zhang, David Paz, Yuliang Guo, Xinyu Huang, Henrik I. Christensen, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06660v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://henryzhangzhy.github.io/mapgs.)  
  Keywords: efficient, fast, mapping, ar, gaussian splatting  
- **[Scaffold-SLAM: Structured 3D Gaussians for Simultaneous Localization and Photorealistic Mapping](https://arxiv.org/abs/2501.05242v1)**  
  Authors: Wen Tianci, Liu Zhiang, Lu Biao, Fang Yongchun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.05242v1.pdf)  
  Keywords: 3d gaussian, motion, slam, mapping, ar, gaussian splatting, localization  
- **[GS-DiT: Advancing Video Generation with Pseudo 4D Gaussian Fields through Efficient Dense 3D Point Tracking](https://arxiv.org/abs/2501.02690v1)**  
  Authors: Weikang Bian, Zhaoyang Huang, Xiaoyu Shi, Yijin Li, Fu-Yun Wang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.02690v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wkbian.github.io/Projects/GS-DiT/.)  
  Keywords: motion, efficient, tracking, 4d, dynamic, ar, gaussian splatting  
- **[PanoSLAM: Panoptic 3D Scene Reconstruction via Gaussian SLAM](https://arxiv.org/abs/2501.00352v1)**  
  Authors: Runnan Chen, Zhaoqing Wang, Jiepeng Wang, Yuexin Ma, Mingming Gong, Wenping Wang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00352v1.pdf) | [![GitHub](https://img.shields.io/github/stars/runnanchen/PanoSLAM?style=social)](https://github.com/runnanchen/PanoSLAM)  
  Keywords: 3d gaussian, efficient, tracking, efficient rendering, 3d reconstruction, semantic, understanding, slam, segmentation, mapping, ar, gaussian splatting, localization, robotics  

### Scene Understanding

*Showing the latest 50 out of 216 papers*

- **[CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications](https://arxiv.org/abs/2501.06927v1)**  
  Authors: Xinyi Zheng, Steve Zhang, Weizhe Lin, Aaron Zhang, Walterio W. Mayol-Cuevas, Junxiao Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06927v1.pdf)  
  Keywords: motion, 3d reconstruction, nerf, slam, segmentation, ar, gaussian splatting  
- **[Gaussian Masked Autoencoders](https://arxiv.org/abs/2501.03229v1)**  
  Authors: Jathushan Rajasegaran, Xinlei Chen, Rulilong Li, Christoph Feichtenhofer, Jitendra Malik, Shiry Ginosar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.03229v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://brjathu.github.io/gmae)  
  Keywords: 3d gaussian, high-fidelity, semantic, understanding, segmentation, ar, gaussian splatting  
- **[HOGSA: Bimanual Hand-Object Interaction Understanding with 3D Gaussian Splatting Based Data Augmentation](https://arxiv.org/abs/2501.02845v1)**  
  Authors: Wentian Qu, Jiahe Li, Jian Cheng, Jian Shi, Chenyu Meng, Cuixia Ma, Hongan Wang, Xiaoming Deng, Yinda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.02845v1.pdf)  
  Keywords: 3d gaussian, motion, understanding, ar, gaussian splatting, robotics  
- **[PG-SAG: Parallel Gaussian Splatting for Fine-Grained Large-Scale Urban Buildings Reconstruction via Semantic-Aware Grouping](https://arxiv.org/abs/2501.01677v1)**  
  Authors: Tengfei Wang, Xin Wang, Yongmao Hou, Yiwei Xu, Wendi Zhang, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01677v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TFWang-9527/PG-SAG?style=social)](https://github.com/TFWang-9527/PG-SAG)  
  Keywords: 3d gaussian, semantic, face, ar, gaussian splatting  
- **[Leverage Cross-Attention for End-to-End Open-Vocabulary Panoptic Reconstruction](https://arxiv.org/abs/2501.01119v1)**  
  Authors: Xuan Yu, Yuxuan Xie, Yili Liu, Haojian Lu, Rong Xiong, Yiyi Liao, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01119v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuxuan1206.github.io/panopticrecon_pp/)  
  Keywords: 3d gaussian, semantic, understanding, segmentation, dynamic, ar, head, robotics  
- **[Gaussian Building Mesh (GBM): Extract a Building's 3D Mesh with Google Earth and Gaussian Splatting](https://arxiv.org/abs/2501.00625v2)**  
  Authors: Kyle Gao, Liangzhi Li, Hongjie He, Dening Lu, Linlin Xu, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00625v2.pdf)  
  Keywords: geometry, ar, segmentation, gaussian splatting  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: 3d gaussian, motion, outdoor, real-time rendering, understanding, dynamic, ar  
- **[PanoSLAM: Panoptic 3D Scene Reconstruction via Gaussian SLAM](https://arxiv.org/abs/2501.00352v1)**  
  Authors: Runnan Chen, Zhaoqing Wang, Jiepeng Wang, Yuexin Ma, Mingming Gong, Wenping Wang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00352v1.pdf) | [![GitHub](https://img.shields.io/github/stars/runnanchen/PanoSLAM?style=social)](https://github.com/runnanchen/PanoSLAM)  
  Keywords: 3d gaussian, efficient, tracking, efficient rendering, 3d reconstruction, semantic, understanding, slam, segmentation, mapping, ar, gaussian splatting, localization, robotics  
- **[OVGaussian: Generalizable 3D Gaussian Segmentation with Open Vocabularies](https://arxiv.org/abs/2501.00326v1)**  
  Authors: Runnan Chen, Xiangyu Sun, Zhaoqing Wang, Youquan Liu, Jiepeng Wang, Lingdong Kong, Jiankang Deng, Mingming Gong, Liang Pan, Wenping Wang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00326v1.pdf) | [![GitHub](https://img.shields.io/github/stars/runnanchen/OVGaussian?style=social)](https://github.com/runnanchen/OVGaussian)  
  Keywords: 3d gaussian, semantic, understanding, segmentation, ar  
- **[4D Gaussian Splatting: Modeling Dynamic Scenes with Native 4D Primitives](https://arxiv.org/abs/2412.20720v1)**  
  Authors: Zeyu Yang, Zijie Pan, Xiatian Zhu, Li Zhang, Yu-Gang Jiang, Philip H. S. Torr  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20720v1.pdf)  
  Keywords: motion, vr, geometry, 4d, compact, real-time rendering, understanding, dynamic, ar, gaussian splatting  



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