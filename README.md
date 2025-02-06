# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-02-06 00:45:56

## Categories

- [3DGS Surveys](#3dgs-surveys) (21 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (372 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1293 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (431 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (482 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (92 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (425 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (69 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (482 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (209 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (31 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (143 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (190 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (223 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, survey, ar, ray tracing, gaussian splatting  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: lighting, outdoor, 3d gaussian, tracking, mapping, localization, survey, geometry, face, ar, dynamic, reflection, slam  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: 3d gaussian, survey, ar, recognition, illumination, gaussian splatting  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: lighting, 3d reconstruction, autonomous driving, high-fidelity, survey, geometry, semantic, nerf, robotics, compact, ar, dynamic, gaussian splatting  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: understanding, 3d gaussian, survey, robotics, nerf, real-time rendering, ar, gaussian splatting  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: lighting, 3d gaussian, high-fidelity, survey, nerf, ar, gaussian splatting  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, autonomous driving, vr, survey, robotics, nerf, ar, gaussian splatting  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: survey, ar, 3d gaussian  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v2)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v2.pdf)  
  Keywords: understanding, 3d gaussian, survey, efficient, real-time rendering, ar, gaussian splatting  
- **[Survey on Fundamental Deep Learning 3D Reconstruction Techniques](https://arxiv.org/abs/2407.08137v1)**  
  Authors: Yonge Bai, LikHang Wong, TszYin Twan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.08137v1.pdf)  
  Keywords: lighting, 3d reconstruction, 3d gaussian, survey, nerf, ar, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 372 papers*

- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: acceleration, efficient, ar, ray tracing, light transport, reflection, gaussian splatting  
- **[Lifting by Gaussians: A Simple, Fast and Flexible Method for 3D Instance Segmentation](https://arxiv.org/abs/2502.00173v1)**  
  Authors: Rohan Chacko, Nicolai Haeni, Eldar Khaliullin, Lin Sun, Douglas Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00173v1.pdf)  
  Keywords: fast, 3d gaussian, semantic, efficient, segmentation, ar  
- **[Advancing Dense Endoscopic Reconstruction with Gaussian Splatting-driven Surface Normal-aware Tracking and Mapping](https://arxiv.org/abs/2501.19319v1)**  
  Authors: Yiming Huang, Beilei Cui, Long Bai, Zhen Chen, Jinlin Wu, Zhen Li, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19319v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lastbasket/Endo-2DTAM?style=social)](https://github.com/lastbasket/Endo-2DTAM)  
  Keywords: fast, 3d gaussian, tracking, mapping, localization, efficient, face, real-time rendering, ar, slam, gaussian splatting  
- **[JGHand: Joint-Driven Animatable Hand Avater via 3D Gaussian Splatting](https://arxiv.org/abs/2501.19088v1)**  
  Authors: Zhoutao Sun, Xukun Shen, Yong Hu, Yuyou Zhong, Xueyang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19088v1.pdf)  
  Keywords: shadow, 3d gaussian, high-fidelity, deformation, face, neural rendering, real-time rendering, ar, gaussian splatting, human  
- **[StructuredField: Unifying Structured Geometry and Radiance Field](https://arxiv.org/abs/2501.18152v1)**  
  Authors: Kaiwen Song, Jinkai Cui, Zherui Qiu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18152v1.pdf)  
  Keywords: fast, 3d gaussian, high-fidelity, geometry, deformation, ar  
- **[Evaluating CrowdSplat: Perceived Level of Detail for Gaussian Crowds](https://arxiv.org/abs/2501.17085v1)**  
  Authors: Xiaohan Sun, Yinghan Xu, John Dingliana, Carol O'Sullivan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17085v1.pdf)  
  Keywords: motion, avatar, 3d gaussian, vr, efficient rendering, efficient, ar, gaussian splatting  
- **[Deformable Beta Splatting](https://arxiv.org/abs/2501.18630v1)**  
  Authors: Rong Liu, Dylan Sun, Meida Chen, Yue Wang, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18630v1.pdf)  
  Keywords: fast, lighting, 3d gaussian, geometry, compact, real-time rendering, ar, gaussian splatting  
- **[Trick-GS: A Balanced Bag of Tricks for Efficient Gaussian Splatting](https://arxiv.org/abs/2501.14534v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Mateusz Nowak, Mehmet Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14534v1.pdf)  
  Keywords: fast, 3d reconstruction, high quality, efficient, ar, gaussian splatting  
- **[Deblur-Avatar: Animatable Avatars from Motion-Blurred Monocular Videos](https://arxiv.org/abs/2501.13335v1)**  
  Authors: Xianrui Luo, Juewen Peng, Zhongang Cai, Lei Yang, Fan Yang, Zhiguo Cao, Guosheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13335v1.pdf)  
  Keywords: motion, avatar, 3d gaussian, high-fidelity, body, real-time rendering, ar, dynamic, gaussian splatting, human  
- **[3DGS$^2$: Near Second-order Converging 3D Gaussian Splatting](https://arxiv.org/abs/2501.13975v2)**  
  Authors: Lei Lan, Tianjia Shao, Zixuan Lu, Yu Zhang, Chenfanfu Jiang, Yin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13975v2.pdf)  
  Keywords: fast, 3d reconstruction, 3d gaussian, acceleration, efficient, ar, gaussian splatting  

### Applications

*Showing the latest 50 out of 1293 papers*

- **[GP-GS: Gaussian Processes for Enhanced Gaussian Splatting](https://arxiv.org/abs/2502.02283v1)**  
  Authors: Zhihao Guo, Jingxuan Su, Shenglin Wang, Jinlong Fan, Jing Zhang, Liangxiu Han, Peng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.02283v1.pdf)  
  Keywords: 3d reconstruction, motion, 3d gaussian, efficient, ar, dynamic, gaussian splatting  
- **[Efficient Dynamic Scene Editing via 4D Gaussian-based Static-Dynamic Separation](https://arxiv.org/abs/2502.02091v1)**  
  Authors: JooHyun Kwon, Hanbyel Cho, Junmo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.02091v1.pdf)  
  Keywords: 3d gaussian, 4d, deformation, efficient, ar, dynamic  
- **[LAYOUTDREAMER: Physics-guided Layout for Text-to-3D Compositional Scene Generation](https://arxiv.org/abs/2502.01949v1)**  
  Authors: Yang Zhou, Zongjin He, Qixuan Li, Chao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01949v1.pdf)  
  Keywords: 3d gaussian, semantic, face, ar, dynamic, gaussian splatting  
- **[UVGS: Reimagining Unstructured 3D Gaussian Splatting using UV Mapping](https://arxiv.org/abs/2502.01846v1)**  
  Authors: Aashish Rai, Dilin Wang, Mihir Jain, Nikolaos Sarafianos, Arthur Chen, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01846v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, mapping  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, survey, ar, ray tracing, gaussian splatting  
- **[VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion](https://arxiv.org/abs/2502.01536v1)**  
  Authors: Shaoting Zhu, Linzhan Mou, Derun Li, Baijun Ye, Runhan Huang, Hang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01536v1.pdf)  
  Keywords: lighting, motion, 3d gaussian, tracking, vr, geometry, ar, gaussian splatting  
- **[Transformers trained on proteins can learn to attend to Euclidean distance](https://arxiv.org/abs/2502.01533v1)**  
  Authors: Isaac Ellmen, Constantin Schneider, Matthew I. J. Raybould, Charlotte M. Deane  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01533v1.pdf)  
  Keywords: ar, 3d gaussian  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: acceleration, efficient, ar, ray tracing, light transport, reflection, gaussian splatting  
- **[PhiP-G: Physics-Guided Text-to-3D Compositional Scene Generation](https://arxiv.org/abs/2502.00708v1)**  
  Authors: Qixuan Li, Chao Wang, Zongjin He, Yan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00708v1.pdf)  
  Keywords: ar, 3d gaussian  
- **[EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](https://arxiv.org/abs/2502.00654v1)**  
  Authors: Junuk Cha, Seongro Yoon, Valeriya Strizhkova, Francois Bremond, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00654v1.pdf)  
  Keywords: motion, 3d gaussian, high-fidelity, face, head, ar, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 431 papers*

- **[LAYOUTDREAMER: Physics-guided Layout for Text-to-3D Compositional Scene Generation](https://arxiv.org/abs/2502.01949v1)**  
  Authors: Yang Zhou, Zongjin He, Qixuan Li, Chao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01949v1.pdf)  
  Keywords: 3d gaussian, semantic, face, ar, dynamic, gaussian splatting  
- **[EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](https://arxiv.org/abs/2502.00654v1)**  
  Authors: Junuk Cha, Seongro Yoon, Valeriya Strizhkova, Francois Bremond, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00654v1.pdf)  
  Keywords: motion, 3d gaussian, high-fidelity, face, head, ar, gaussian splatting  
- **[Advancing Dense Endoscopic Reconstruction with Gaussian Splatting-driven Surface Normal-aware Tracking and Mapping](https://arxiv.org/abs/2501.19319v1)**  
  Authors: Yiming Huang, Beilei Cui, Long Bai, Zhen Chen, Jinlin Wu, Zhen Li, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19319v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lastbasket/Endo-2DTAM?style=social)](https://github.com/lastbasket/Endo-2DTAM)  
  Keywords: fast, 3d gaussian, tracking, mapping, localization, efficient, face, real-time rendering, ar, slam, gaussian splatting  
- **[JGHand: Joint-Driven Animatable Hand Avater via 3D Gaussian Splatting](https://arxiv.org/abs/2501.19088v1)**  
  Authors: Zhoutao Sun, Xukun Shen, Yong Hu, Yuyou Zhong, Xueyang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19088v1.pdf)  
  Keywords: shadow, 3d gaussian, high-fidelity, deformation, face, neural rendering, real-time rendering, ar, gaussian splatting, human  
- **[Drag Your Gaussian: Effective Drag-Based Editing with Score Distillation for 3D Gaussian Splatting](https://arxiv.org/abs/2501.18672v1)**  
  Authors: Yansong Qu, Dian Chen, Xinyang Li, Xiaofan Li, Shengchuan Zhang, Liujuan Cao, Rongrong Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18672v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://quyans.github.io/Drag-Your-Gaussian.)  
  Keywords: head, gaussian splatting, ar, 3d gaussian  
- **[VoD-3DGS: View-opacity-Dependent 3D Gaussian Splatting](https://arxiv.org/abs/2501.17978v2)**  
  Authors: Mateusz Nowak, Wojciech Jarosz, Peter Chin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17978v2.pdf)  
  Keywords: 3d gaussian, nerf, face, ar, reflection, gaussian splatting  
- **[CrowdSplat: Exploring Gaussian Splatting For Crowd Rendering](https://arxiv.org/abs/2501.17792v1)**  
  Authors: Xiaohan Sun, Yinghan Xu, John Dingliana, Carol O'Sullivan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17792v1.pdf)  
  Keywords: avatar, 3d gaussian, ar, dynamic, gaussian splatting, human  
- **[FeatureGS: Eigenvalue-Feature Optimization in 3D Gaussian Splatting for Geometrically Accurate and Artifact-Reduced Reconstruction](https://arxiv.org/abs/2501.17655v1)**  
  Authors: Miriam Jäger, Markus Hillemann, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17655v1.pdf)  
  Keywords: 3d gaussian, efficient, face, ar, gaussian splatting  
- **[Evaluating CrowdSplat: Perceived Level of Detail for Gaussian Crowds](https://arxiv.org/abs/2501.17085v1)**  
  Authors: Xiaohan Sun, Yinghan Xu, John Dingliana, Carol O'Sullivan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17085v1.pdf)  
  Keywords: motion, avatar, 3d gaussian, vr, efficient rendering, efficient, ar, gaussian splatting  
- **[LinPrim: Linear Primitives for Differentiable Volumetric Rendering](https://arxiv.org/abs/2501.16312v2)**  
  Authors: Nicolas von Lützow, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.16312v2.pdf)  
  Keywords: 3d gaussian, geometry, nerf, efficient, face, head, ar  

### Dynamic Scene

*Showing the latest 50 out of 482 papers*

- **[GP-GS: Gaussian Processes for Enhanced Gaussian Splatting](https://arxiv.org/abs/2502.02283v1)**  
  Authors: Zhihao Guo, Jingxuan Su, Shenglin Wang, Jinlong Fan, Jing Zhang, Liangxiu Han, Peng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.02283v1.pdf)  
  Keywords: 3d reconstruction, motion, 3d gaussian, efficient, ar, dynamic, gaussian splatting  
- **[Efficient Dynamic Scene Editing via 4D Gaussian-based Static-Dynamic Separation](https://arxiv.org/abs/2502.02091v1)**  
  Authors: JooHyun Kwon, Hanbyel Cho, Junmo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.02091v1.pdf)  
  Keywords: 3d gaussian, 4d, deformation, efficient, ar, dynamic  
- **[LAYOUTDREAMER: Physics-guided Layout for Text-to-3D Compositional Scene Generation](https://arxiv.org/abs/2502.01949v1)**  
  Authors: Yang Zhou, Zongjin He, Qixuan Li, Chao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01949v1.pdf)  
  Keywords: 3d gaussian, semantic, face, ar, dynamic, gaussian splatting  
- **[VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion](https://arxiv.org/abs/2502.01536v1)**  
  Authors: Shaoting Zhu, Linzhan Mou, Derun Li, Baijun Ye, Runhan Huang, Hang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01536v1.pdf)  
  Keywords: lighting, motion, 3d gaussian, tracking, vr, geometry, ar, gaussian splatting  
- **[EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](https://arxiv.org/abs/2502.00654v1)**  
  Authors: Junuk Cha, Seongro Yoon, Valeriya Strizhkova, Francois Bremond, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00654v1.pdf)  
  Keywords: motion, 3d gaussian, high-fidelity, face, head, ar, gaussian splatting  
- **[JGHand: Joint-Driven Animatable Hand Avater via 3D Gaussian Splatting](https://arxiv.org/abs/2501.19088v1)**  
  Authors: Zhoutao Sun, Xukun Shen, Yong Hu, Yuyou Zhong, Xueyang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19088v1.pdf)  
  Keywords: shadow, 3d gaussian, high-fidelity, deformation, face, neural rendering, real-time rendering, ar, gaussian splatting, human  
- **[OmniPhysGS: 3D Constitutive Gaussians for General Physics-Based Dynamics Generation](https://arxiv.org/abs/2501.18982v1)**  
  Authors: Yuchen Lin, Chenguo Lin, Jianjin Xu, Yadong Mu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18982v1.pdf)  
  Keywords: animation, ar, dynamic, 3d gaussian  
- **[StructuredField: Unifying Structured Geometry and Radiance Field](https://arxiv.org/abs/2501.18152v1)**  
  Authors: Kaiwen Song, Jinkai Cui, Zherui Qiu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18152v1.pdf)  
  Keywords: fast, 3d gaussian, high-fidelity, geometry, deformation, ar  
- **[CrowdSplat: Exploring Gaussian Splatting For Crowd Rendering](https://arxiv.org/abs/2501.17792v1)**  
  Authors: Xiaohan Sun, Yinghan Xu, John Dingliana, Carol O'Sullivan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17792v1.pdf)  
  Keywords: avatar, 3d gaussian, ar, dynamic, gaussian splatting, human  
- **[Evaluating CrowdSplat: Perceived Level of Detail for Gaussian Crowds](https://arxiv.org/abs/2501.17085v1)**  
  Authors: Xiaohan Sun, Yinghan Xu, John Dingliana, Carol O'Sullivan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17085v1.pdf)  
  Keywords: motion, avatar, 3d gaussian, vr, efficient rendering, efficient, ar, gaussian splatting  

### Few-shot

*Showing the latest 50 out of 92 papers*

- **[DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform](https://arxiv.org/abs/2501.12637v2)**  
  Authors: Hung Nguyen, Blark Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12637v2.pdf)  
  Keywords: fast, few-shot, head, nerf, ar  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: 3d gaussian, 4d, semantic, ar, gaussian splatting, sparse-view  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, nerf, efficient, ar, gaussian splatting, sparse-view  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: lighting, sparse view, nerf, face, ar, dynamic, gaussian splatting, human, medical  
- **[Synthetic Prior for Few-Shot Drivable Head Avatar Inversion](https://arxiv.org/abs/2501.06903v1)**  
  Authors: Wojciech Zielonka, Stephan J. Garbin, Alexandros Lattas, George Kopanas, Paulo Gotardo, Thabo Beeler, Justus Thies, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06903v1.pdf)  
  Keywords: avatar, few-shot, 3d gaussian, head, ar, gaussian splatting  
- **[NVS-SQA: Exploring Self-Supervised Quality Representation Learning for Neurally Synthesized Scenes without References](https://arxiv.org/abs/2501.06488v1)**  
  Authors: Qiang Qu, Yiran Shen, Xiaoming Chen, Yuk Ying Chung, Weidong Cai, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06488v1.pdf)  
  Keywords: 3d gaussian, sparse view, nerf, ar, gaussian splatting, human  
- **[FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency](https://arxiv.org/abs/2501.04628v1)**  
  Authors: Han Huang, Yulun Wu, Chao Deng, Ge Gao, Ming Gu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04628v1.pdf)  
  Keywords: fast, sparse view, face, ar, gaussian splatting, sparse-view  
- **[Dust to Tower: Coarse-to-Fine Photo-Realistic Scene Reconstruction from Sparse Uncalibrated Images](https://arxiv.org/abs/2412.19518v1)**  
  Authors: Xudong Cai, Yongcai Wang, Zhaoxin Fan, Deng Haoran, Shuo Wang, Wanting Li, Deying Li, Lun Luo, Minhang Wang, Jintao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19518v1.pdf)  
  Keywords: fast, 3d gaussian, efficient, ar, gaussian splatting, sparse-view  
- **[CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting](https://arxiv.org/abs/2412.19142v1)**  
  Authors: Siyu Jiao, Haoye Dong, Yuyang Yin, Zequn Jie, Yinlong Qian, Yao Zhao, Humphrey Shi, Yunchao Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19142v1.pdf)  
  Keywords: few-shot, 3d gaussian, efficient, ar, gaussian splatting  
- **[SolidGS: Consolidating Gaussian Surfel Splatting for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2412.15400v1)**  
  Authors: Zhuowen Shen, Yuan Liu, Zhang Chen, Zhong Li, Jiepeng Wang, Yongqing Liang, Zhengming Yu, Jingdong Zhang, Yi Xu, Scott Schaefer, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15400v1.pdf)  
  Keywords: geometry, sparse view, face, ar, gaussian splatting, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 425 papers*

- **[GP-GS: Gaussian Processes for Enhanced Gaussian Splatting](https://arxiv.org/abs/2502.02283v1)**  
  Authors: Zhihao Guo, Jingxuan Su, Shenglin Wang, Jinlong Fan, Jing Zhang, Liangxiu Han, Peng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.02283v1.pdf)  
  Keywords: 3d reconstruction, motion, 3d gaussian, efficient, ar, dynamic, gaussian splatting  
- **[VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion](https://arxiv.org/abs/2502.01536v1)**  
  Authors: Shaoting Zhu, Linzhan Mou, Derun Li, Baijun Ye, Runhan Huang, Hang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01536v1.pdf)  
  Keywords: lighting, motion, 3d gaussian, tracking, vr, geometry, ar, gaussian splatting  
- **[Zero-Shot Novel View and Depth Synthesis with Multi-View Geometric Diffusion](https://arxiv.org/abs/2501.18804v1)**  
  Authors: Vitor Guizilini, Muhammad Zubair Irshad, Dian Chen, Greg Shakhnarovich, Rares Ambrus  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18804v1.pdf)  
  Keywords: geometry, ar, efficient, 3d gaussian  
- **[StructuredField: Unifying Structured Geometry and Radiance Field](https://arxiv.org/abs/2501.18152v1)**  
  Authors: Kaiwen Song, Jinkai Cui, Zherui Qiu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18152v1.pdf)  
  Keywords: fast, 3d gaussian, high-fidelity, geometry, deformation, ar  
- **[3D Reconstruction of Shoes for Augmented Reality](https://arxiv.org/abs/2501.18643v1)**  
  Authors: Pratik Shrestha, Sujan Kapali, Swikar Gautam, Vishal Pokharel, Santosh Giri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18643v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, segmentation, ar, gaussian splatting  
- **[Deformable Beta Splatting](https://arxiv.org/abs/2501.18630v1)**  
  Authors: Rong Liu, Dylan Sun, Meida Chen, Yue Wang, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18630v1.pdf)  
  Keywords: fast, lighting, 3d gaussian, geometry, compact, real-time rendering, ar, gaussian splatting  
- **[LinPrim: Linear Primitives for Differentiable Volumetric Rendering](https://arxiv.org/abs/2501.16312v2)**  
  Authors: Nicolas von Lützow, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.16312v2.pdf)  
  Keywords: 3d gaussian, geometry, nerf, efficient, face, head, ar  
- **[Trick-GS: A Balanced Bag of Tricks for Efficient Gaussian Splatting](https://arxiv.org/abs/2501.14534v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Mateusz Nowak, Mehmet Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14534v1.pdf)  
  Keywords: fast, 3d reconstruction, high quality, efficient, ar, gaussian splatting  
- **[Scalable Benchmarking and Robust Learning for Noise-Free Ego-Motion and 3D Reconstruction from Noisy Video](https://arxiv.org/abs/2501.14319v1)**  
  Authors: Xiaohao Xu, Tianyi Zhang, Shibo Zhao, Xiang Li, Sibo Wang, Yongqi Chen, Ye Li, Bhiksha Raj, Matthew Johnson-Roberson, Sebastian Scherer, Xiaonan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14319v1.pdf)  
  Keywords: lighting, 3d reconstruction, motion, ar, dynamic, illumination, gaussian splatting  
- **[Dense-SfM: Structure from Motion with Dense Consistent Matching](https://arxiv.org/abs/2501.14277v1)**  
  Authors: JongMin Lee, Sungjoo Yoo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14277v1.pdf)  
  Keywords: motion, 3d reconstruction, gaussian splatting, ar  

### Large Scene

*Showing the latest 50 out of 69 papers*

- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: outdoor, 3d gaussian, efficient, ar, gaussian splatting  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: outdoor, mapping, localization, geometry, nerf, ar, dynamic, large scene, slam, gaussian splatting  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: understanding, outdoor, motion, 3d gaussian, real-time rendering, ar, dynamic  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: outdoor, 3d gaussian, mapping, nerf, neural rendering, efficient, ar, slam, gaussian splatting  
- **[WeatherGS: 3D Scene Reconstruction in Adverse Weather Conditions via Gaussian Splatting](https://arxiv.org/abs/2412.18862v2)**  
  Authors: Chenghao Qian, Yuhu Guo, Wenjing Li, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.18862v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/weather-gs.)  
  Keywords: outdoor, 3d reconstruction, 3d gaussian, ar, gaussian splatting  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: fast, 3d gaussian, high-fidelity, nerf, face, ar, large scene, compression, gaussian splatting  
- **[LiHi-GS: LiDAR-Supervised Gaussian Splatting for Highway Driving Scene Reconstruction](https://arxiv.org/abs/2412.15447v2)**  
  Authors: Pou-Chun Kung, Xianling Zhang, Katherine A. Skinner, Nikita Jaipuria  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15447v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/lihi_gs)  
  Keywords: fast, 3d gaussian, autonomous driving, nerf, ar, dynamic, urban scene, gaussian splatting  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: lighting, outdoor, 3d gaussian, tracking, mapping, localization, survey, geometry, face, ar, dynamic, reflection, slam  
- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: 3d gaussian, head, ar, dynamic, large scene, gaussian splatting  
- **[HybridGS: Decoupling Transients and Statics with 2D and 3D Gaussian Splatting](https://arxiv.org/abs/2412.03844v2)**  
  Authors: Jingyu Lin, Jiaqi Gu, Lubin Fan, Bojian Wu, Yujing Lou, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03844v2.pdf)  
  Keywords: outdoor, gaussian splatting, ar, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 482 papers*

- **[GP-GS: Gaussian Processes for Enhanced Gaussian Splatting](https://arxiv.org/abs/2502.02283v1)**  
  Authors: Zhihao Guo, Jingxuan Su, Shenglin Wang, Jinlong Fan, Jing Zhang, Liangxiu Han, Peng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.02283v1.pdf)  
  Keywords: 3d reconstruction, motion, 3d gaussian, efficient, ar, dynamic, gaussian splatting  
- **[Efficient Dynamic Scene Editing via 4D Gaussian-based Static-Dynamic Separation](https://arxiv.org/abs/2502.02091v1)**  
  Authors: JooHyun Kwon, Hanbyel Cho, Junmo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.02091v1.pdf)  
  Keywords: 3d gaussian, 4d, deformation, efficient, ar, dynamic  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: acceleration, efficient, ar, ray tracing, light transport, reflection, gaussian splatting  
- **[Lifting by Gaussians: A Simple, Fast and Flexible Method for 3D Instance Segmentation](https://arxiv.org/abs/2502.00173v1)**  
  Authors: Rohan Chacko, Nicolai Haeni, Eldar Khaliullin, Lin Sun, Douglas Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00173v1.pdf)  
  Keywords: fast, 3d gaussian, semantic, efficient, segmentation, ar  
- **[Advancing Dense Endoscopic Reconstruction with Gaussian Splatting-driven Surface Normal-aware Tracking and Mapping](https://arxiv.org/abs/2501.19319v1)**  
  Authors: Yiming Huang, Beilei Cui, Long Bai, Zhen Chen, Jinlin Wu, Zhen Li, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19319v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lastbasket/Endo-2DTAM?style=social)](https://github.com/lastbasket/Endo-2DTAM)  
  Keywords: fast, 3d gaussian, tracking, mapping, localization, efficient, face, real-time rendering, ar, slam, gaussian splatting  
- **[Zero-Shot Novel View and Depth Synthesis with Multi-View Geometric Diffusion](https://arxiv.org/abs/2501.18804v1)**  
  Authors: Vitor Guizilini, Muhammad Zubair Irshad, Dian Chen, Greg Shakhnarovich, Rares Ambrus  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18804v1.pdf)  
  Keywords: geometry, ar, efficient, 3d gaussian  
- **[FeatureGS: Eigenvalue-Feature Optimization in 3D Gaussian Splatting for Geometrically Accurate and Artifact-Reduced Reconstruction](https://arxiv.org/abs/2501.17655v1)**  
  Authors: Miriam Jäger, Markus Hillemann, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17655v1.pdf)  
  Keywords: 3d gaussian, efficient, face, ar, gaussian splatting  
- **[Evaluating CrowdSplat: Perceived Level of Detail for Gaussian Crowds](https://arxiv.org/abs/2501.17085v1)**  
  Authors: Xiaohan Sun, Yinghan Xu, John Dingliana, Carol O'Sullivan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17085v1.pdf)  
  Keywords: motion, avatar, 3d gaussian, vr, efficient rendering, efficient, ar, gaussian splatting  
- **[DiffSplat: Repurposing Image Diffusion Models for Scalable Gaussian Splat Generation](https://arxiv.org/abs/2501.16764v1)**  
  Authors: Chenguo Lin, Panwang Pan, Bangbang Yang, Zeming Li, Yadong Mu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.16764v1.pdf)  
  Keywords: ar, 3d gaussian, lightweight  
- **[Deformable Beta Splatting](https://arxiv.org/abs/2501.18630v1)**  
  Authors: Rong Liu, Dylan Sun, Meida Chen, Yue Wang, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18630v1.pdf)  
  Keywords: fast, lighting, 3d gaussian, geometry, compact, real-time rendering, ar, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 209 papers*

- **[EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](https://arxiv.org/abs/2502.00654v1)**  
  Authors: Junuk Cha, Seongro Yoon, Valeriya Strizhkova, Francois Bremond, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00654v1.pdf)  
  Keywords: motion, 3d gaussian, high-fidelity, face, head, ar, gaussian splatting  
- **[JGHand: Joint-Driven Animatable Hand Avater via 3D Gaussian Splatting](https://arxiv.org/abs/2501.19088v1)**  
  Authors: Zhoutao Sun, Xukun Shen, Yong Hu, Yuyou Zhong, Xueyang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19088v1.pdf)  
  Keywords: shadow, 3d gaussian, high-fidelity, deformation, face, neural rendering, real-time rendering, ar, gaussian splatting, human  
- **[StructuredField: Unifying Structured Geometry and Radiance Field](https://arxiv.org/abs/2501.18152v1)**  
  Authors: Kaiwen Song, Jinkai Cui, Zherui Qiu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18152v1.pdf)  
  Keywords: fast, 3d gaussian, high-fidelity, geometry, deformation, ar  
- **[Towards Better Robustness: Progressively Joint Pose-3DGS Learning for Arbitrarily Long Videos](https://arxiv.org/abs/2501.15096v1)**  
  Authors: Zhen-Hui Dong, Sheng Ye, Yu-Hui Wen, Nannan Li, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15096v1.pdf)  
  Keywords: motion, 3d gaussian, tracking, high-fidelity, face, ar, gaussian splatting  
- **[Trick-GS: A Balanced Bag of Tricks for Efficient Gaussian Splatting](https://arxiv.org/abs/2501.14534v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Mateusz Nowak, Mehmet Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14534v1.pdf)  
  Keywords: fast, 3d reconstruction, high quality, efficient, ar, gaussian splatting  
- **[Deblur-Avatar: Animatable Avatars from Motion-Blurred Monocular Videos](https://arxiv.org/abs/2501.13335v1)**  
  Authors: Xianrui Luo, Juewen Peng, Zhongang Cai, Lei Yang, Fan Yang, Zhiguo Cao, Guosheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13335v1.pdf)  
  Keywords: motion, avatar, 3d gaussian, high-fidelity, body, real-time rendering, ar, dynamic, gaussian splatting, human  
- **[SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2501.07015v2)**  
  Authors: Yue Hu, Rong Liu, Meida Chen, Peter Beerel, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.07015v2.pdf)  
  Keywords: 3d reconstruction, motion, 3d gaussian, mapping, high-fidelity, geometry, nerf, efficient, ar, dynamic, slam, gaussian splatting  
- **[Gaussian Masked Autoencoders](https://arxiv.org/abs/2501.03229v1)**  
  Authors: Jathushan Rajasegaran, Xinlei Chen, Rulilong Li, Christoph Feichtenhofer, Jitendra Malik, Shiry Ginosar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.03229v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://brjathu.github.io/gmae)  
  Keywords: understanding, 3d gaussian, high-fidelity, semantic, segmentation, ar, gaussian splatting  
- **[Deformable Gaussian Splatting for Efficient and High-Fidelity Reconstruction of Surgical Scenes](https://arxiv.org/abs/2501.01101v1)**  
  Authors: Jiwei Shan, Zeyu Cai, Cheng-Tai Hsieh, Shing Shin Cheng, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.01101v1.pdf)  
  Keywords: motion, 3d gaussian, high-fidelity, deformation, efficient, ar, dynamic, gaussian splatting  
- **[ActiveGS: Active Scene Reconstruction using Gaussian Splatting](https://arxiv.org/abs/2412.17769v1)**  
  Authors: Liren Jin, Xingguang Zhong, Yue Pan, Jens Behley, Cyrill Stachniss, Marija Popović  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17769v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, robotics  

### Ray Tracing

- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, survey, ar, ray tracing, gaussian splatting  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: acceleration, efficient, ar, ray tracing, light transport, reflection, gaussian splatting  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: shadow, 3d gaussian, ar, ray tracing, reflection, gaussian splatting  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: lighting, efficient, relighting, ar, ray tracing, reflection, gaussian splatting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: lighting, 3d gaussian, high-fidelity, efficient, real-time rendering, ar, ray tracing, reflection, gaussian splatting  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: fast, mapping, geometry, nerf, efficient, face, global illumination, ar, illumination, gaussian splatting  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v1.pdf)  
  Keywords: 3d gaussian, efficient, ar, ray tracing, gaussian splatting  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: gaussian splatting, ar, ray tracing, 3d gaussian  
- **[URAvatar: Universal Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2410.24223v1)**  
  Authors: Junxuan Li, Chen Cao, Gabriel Schwartz, Rawal Khirodkar, Christian Richardt, Tomas Simon, Yaser Sheikh, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24223v1.pdf)  
  Keywords: avatar, relightable, 3d gaussian, efficient, head, real-time rendering, global illumination, ar, light transport, illumination, human  
- **[Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization](https://arxiv.org/abs/2410.16978v1)**  
  Authors: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, Ralf Gutjahr, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16978v1.pdf)  
  Keywords: understanding, vr, path tracing, head, efficient, ar, gaussian splatting, medical  

### Relighting

*Showing the latest 50 out of 143 papers*

- **[VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion](https://arxiv.org/abs/2502.01536v1)**  
  Authors: Shaoting Zhu, Linzhan Mou, Derun Li, Baijun Ye, Runhan Huang, Hang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01536v1.pdf)  
  Keywords: lighting, motion, 3d gaussian, tracking, vr, geometry, ar, gaussian splatting  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: acceleration, efficient, ar, ray tracing, light transport, reflection, gaussian splatting  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: shadow, 3d gaussian, ar, ray tracing, reflection, gaussian splatting  
- **[JGHand: Joint-Driven Animatable Hand Avater via 3D Gaussian Splatting](https://arxiv.org/abs/2501.19088v1)**  
  Authors: Zhoutao Sun, Xukun Shen, Yong Hu, Yuyou Zhong, Xueyang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19088v1.pdf)  
  Keywords: shadow, 3d gaussian, high-fidelity, deformation, face, neural rendering, real-time rendering, ar, gaussian splatting, human  
- **[VoD-3DGS: View-opacity-Dependent 3D Gaussian Splatting](https://arxiv.org/abs/2501.17978v2)**  
  Authors: Mateusz Nowak, Wojciech Jarosz, Peter Chin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17978v2.pdf)  
  Keywords: 3d gaussian, nerf, face, ar, reflection, gaussian splatting  
- **[Deformable Beta Splatting](https://arxiv.org/abs/2501.18630v1)**  
  Authors: Rong Liu, Dylan Sun, Meida Chen, Yue Wang, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18630v1.pdf)  
  Keywords: fast, lighting, 3d gaussian, geometry, compact, real-time rendering, ar, gaussian splatting  
- **[Scalable Benchmarking and Robust Learning for Noise-Free Ego-Motion and 3D Reconstruction from Noisy Video](https://arxiv.org/abs/2501.14319v1)**  
  Authors: Xiaohao Xu, Tianyi Zhang, Shibo Zhao, Xiang Li, Sibo Wang, Yongqi Chen, Ye Li, Bhiksha Raj, Matthew Johnson-Roberson, Sebastian Scherer, Xiaonan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14319v1.pdf)  
  Keywords: lighting, 3d reconstruction, motion, ar, dynamic, illumination, gaussian splatting  
- **[Car-GS: Addressing Reflective and Transparent Surface Challenges in 3D Car Reconstruction](https://arxiv.org/abs/2501.11020v1)**  
  Authors: Congcong Li, Jin Wang, Xiaomeng Wang, Xingchen Zhou, Wei Wu, Yuzhi Zhang, Tongyi Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lcc815.github.io/Car-GS.)  
  Keywords: autonomous driving, geometry, face, ar, reflection  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: lighting, sparse view, nerf, face, ar, dynamic, gaussian splatting, human, medical  
- **[Reflective Gaussian Splatting](https://arxiv.org/abs/2412.19282v2)**  
  Authors: Yuxuan Yao, Zixuan Zeng, Chun Gu, Xiatian Zhu, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19282v2.pdf)  
  Keywords: lighting, geometry, nerf, relighting, ar, reflection, gaussian splatting  

### SLAM

*Showing the latest 50 out of 190 papers*

- **[UVGS: Reimagining Unstructured 3D Gaussian Splatting using UV Mapping](https://arxiv.org/abs/2502.01846v1)**  
  Authors: Aashish Rai, Dilin Wang, Mihir Jain, Nikolaos Sarafianos, Arthur Chen, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01846v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, mapping  
- **[VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion](https://arxiv.org/abs/2502.01536v1)**  
  Authors: Shaoting Zhu, Linzhan Mou, Derun Li, Baijun Ye, Runhan Huang, Hang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01536v1.pdf)  
  Keywords: lighting, motion, 3d gaussian, tracking, vr, geometry, ar, gaussian splatting  
- **[Advancing Dense Endoscopic Reconstruction with Gaussian Splatting-driven Surface Normal-aware Tracking and Mapping](https://arxiv.org/abs/2501.19319v1)**  
  Authors: Yiming Huang, Beilei Cui, Long Bai, Zhen Chen, Jinlin Wu, Zhen Li, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19319v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lastbasket/Endo-2DTAM?style=social)](https://github.com/lastbasket/Endo-2DTAM)  
  Keywords: fast, 3d gaussian, tracking, mapping, localization, efficient, face, real-time rendering, ar, slam, gaussian splatting  
- **[Towards Better Robustness: Progressively Joint Pose-3DGS Learning for Arbitrarily Long Videos](https://arxiv.org/abs/2501.15096v1)**  
  Authors: Zhen-Hui Dong, Sheng Ye, Yu-Hui Wen, Nannan Li, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15096v1.pdf)  
  Keywords: motion, 3d gaussian, tracking, high-fidelity, face, ar, gaussian splatting  
- **[HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting](https://arxiv.org/abs/2501.14147v1)**  
  Authors: Javier Yu, Timothy Chen, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14147v1.pdf)  
  Keywords: 3d gaussian, semantic, efficient, ar, slam, gaussian splatting  
- **[GeomGS: LiDAR-Guided Geometry-Aware Gaussian Splatting for Robot Localization](https://arxiv.org/abs/2501.13417v1)**  
  Authors: Jaewon Lee, Mangyu Kong, Minseong Park, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13417v1.pdf)  
  Keywords: understanding, 3d gaussian, mapping, autonomous driving, localization, geometry, robotics, ar, gaussian splatting  
- **[VIGS SLAM: IMU-based Large-Scale 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2501.13402v1)**  
  Authors: Gyuhyeon Pak, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13402v1.pdf)  
  Keywords: 3d gaussian, tracking, mapping, nerf, ar, slam, gaussian splatting  
- **[GSTAR: Gaussian Surface Tracking and Reconstruction](https://arxiv.org/abs/2501.10283v2)**  
  Authors: Chengwei Zheng, Lixin Xue, Juan Zarate, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.10283v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/GSTAR/.)  
  Keywords: 3d gaussian, tracking, efficient, face, ar, dynamic, gaussian splatting  
- **[CityLoc: 6DoF Pose Distributional Localization for Text Descriptions in Large-Scale Scenes with Gaussian Representation](https://arxiv.org/abs/2501.08982v2)**  
  Authors: Qi Ma, Runyi Yang, Bin Ren, Nicu Sebe, Ender Konukoglu, Luc Van Gool, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08982v2.pdf)  
  Keywords: localization, gaussian splatting, ar, 3d gaussian  
- **[GS-LIVO: Real-Time LiDAR, Inertial, and Visual Multi-sensor Fused Odometry with Gaussian Mapping](https://arxiv.org/abs/2501.08672v1)**  
  Authors: Sheng Hong, Chunran Zheng, Yishu Shen, Changze Li, Fu Zhang, Tong Qin, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08672v1.pdf)  
  Keywords: motion, 3d gaussian, mapping, localization, face, ar, slam, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 223 papers*

- **[LAYOUTDREAMER: Physics-guided Layout for Text-to-3D Compositional Scene Generation](https://arxiv.org/abs/2502.01949v1)**  
  Authors: Yang Zhou, Zongjin He, Qixuan Li, Chao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01949v1.pdf)  
  Keywords: 3d gaussian, semantic, face, ar, dynamic, gaussian splatting  
- **[Lifting by Gaussians: A Simple, Fast and Flexible Method for 3D Instance Segmentation](https://arxiv.org/abs/2502.00173v1)**  
  Authors: Rohan Chacko, Nicolai Haeni, Eldar Khaliullin, Lin Sun, Douglas Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00173v1.pdf)  
  Keywords: fast, 3d gaussian, semantic, efficient, segmentation, ar  
- **[3D Reconstruction of Shoes for Augmented Reality](https://arxiv.org/abs/2501.18643v1)**  
  Authors: Pratik Shrestha, Sujan Kapali, Swikar Gautam, Vishal Pokharel, Santosh Giri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18643v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, segmentation, ar, gaussian splatting  
- **[GaussianToken: An Effective Image Tokenizer with 2D Gaussian Splatting](https://arxiv.org/abs/2501.15619v1)**  
  Authors: Jiajun Dong, Chengkun Wang, Wenzhao Zheng, Lei Chen, Jiwen Lu, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15619v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ChrisDong-THU/GaussianToken?style=social)](https://github.com/ChrisDong-THU/GaussianToken)  
  Keywords: understanding, gaussian splatting, ar, efficient  
- **[HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting](https://arxiv.org/abs/2501.14147v1)**  
  Authors: Javier Yu, Timothy Chen, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14147v1.pdf)  
  Keywords: 3d gaussian, semantic, efficient, ar, slam, gaussian splatting  
- **[GeomGS: LiDAR-Guided Geometry-Aware Gaussian Splatting for Robot Localization](https://arxiv.org/abs/2501.13417v1)**  
  Authors: Jaewon Lee, Mangyu Kong, Minseong Park, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13417v1.pdf)  
  Keywords: understanding, 3d gaussian, mapping, autonomous driving, localization, geometry, robotics, ar, gaussian splatting  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: 3d gaussian, 4d, semantic, ar, gaussian splatting, sparse-view  
- **[CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications](https://arxiv.org/abs/2501.06927v2)**  
  Authors: Xinyi Zheng, Steve Zhang, Weizhe Lin, Aaron Zhang, Walterio W. Mayol-Cuevas, Junxiao Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06927v2.pdf)  
  Keywords: 3d reconstruction, motion, nerf, segmentation, ar, slam, gaussian splatting  
- **[Gaussian Masked Autoencoders](https://arxiv.org/abs/2501.03229v1)**  
  Authors: Jathushan Rajasegaran, Xinlei Chen, Rulilong Li, Christoph Feichtenhofer, Jitendra Malik, Shiry Ginosar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.03229v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://brjathu.github.io/gmae)  
  Keywords: understanding, 3d gaussian, high-fidelity, semantic, segmentation, ar, gaussian splatting  
- **[HOGSA: Bimanual Hand-Object Interaction Understanding with 3D Gaussian Splatting Based Data Augmentation](https://arxiv.org/abs/2501.02845v1)**  
  Authors: Wentian Qu, Jiahe Li, Jian Cheng, Jian Shi, Chenyu Meng, Cuixia Ma, Hongan Wang, Xiaoming Deng, Yinda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.02845v1.pdf)  
  Keywords: understanding, motion, 3d gaussian, robotics, ar, gaussian splatting  



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