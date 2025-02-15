# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-02-15 00:45:16

## Categories

- [3DGS Surveys](#3dgs-surveys) (22 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (378 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1316 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (438 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (489 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (93 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (433 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (70 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (492 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (213 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (33 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (148 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (196 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (229 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: 4d, ar, dynamic, motion, deformation, survey, lighting, gaussian splatting, nerf  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ar, survey, 3d gaussian, gaussian splatting, ray tracing  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: mapping, geometry, reflection, ar, dynamic, localization, tracking, survey, face, lighting, slam, 3d gaussian, outdoor  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: ar, recognition, survey, gaussian splatting, 3d gaussian, illumination  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: robotics, autonomous driving, geometry, ar, dynamic, compact, survey, semantic, lighting, high-fidelity, gaussian splatting, nerf, 3d reconstruction  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: robotics, ar, survey, real-time rendering, understanding, 3d gaussian, gaussian splatting, nerf  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: ar, survey, lighting, high-fidelity, 3d gaussian, gaussian splatting, nerf  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: robotics, autonomous driving, vr, ar, survey, 3d gaussian, gaussian splatting, nerf, 3d reconstruction  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: ar, 3d gaussian, survey  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v2)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v2.pdf)  
  Keywords: ar, survey, gaussian splatting, real-time rendering, understanding, 3d gaussian, efficient  

### Acceleration

*Showing the latest 50 out of 378 papers*

- **[Self-Calibrating Gaussian Splatting for Large Field of View Reconstruction](https://arxiv.org/abs/2502.09563v1)**  
  Authors: Youming Deng, Wenqi Xian, Guandao Yang, Leonidas Guibas, Gordon Wetzstein, Steve Marschner, Paul Debevec  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09563v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, fast, efficient  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: mapping, geometry, ar, tracking, real-time rendering, sparse-view, slam, gaussian splatting, nerf  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, geometry, ar, relightable, dynamic, tracking, real-time rendering, face, lighting, efficient, ray tracing  
- **[Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors](https://arxiv.org/abs/2502.07615v1)**  
  Authors: Lin-Zhuo Chen, Kangjie Liu, Youtian Lin, Siyu Zhu, Zhihao Li, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07615v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/fds)  
  Keywords: geometry, 3d gaussian, ar, fast, gaussian splatting  
- **[SC-OmniGS: Self-Calibrating Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2502.04734v1)**  
  Authors: Huajian Huang, Yingshu Chen, Longwei Li, Hui Cheng, Tristan Braud, Yajie Zhao, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04734v1.pdf)  
  Keywords: 3d gaussian, ar, fast, gaussian splatting, 3d reconstruction  
- **[High-Speed Dynamic 3D Imaging with Sensor Fusion Splatting](https://arxiv.org/abs/2502.04630v1)**  
  Authors: Zihao Zou, Ziyuan Qu, Xi Peng, Vivek Boominathan, Adithya Pediredla, Praneeth Chakravarthula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04630v1.pdf)  
  Keywords: robotics, efficient, geometry, 3d gaussian, ar, dynamic, motion, deformation, fast, gaussian splatting  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: efficient, acceleration, ar, light transport, reflection, gaussian splatting, ray tracing  
- **[Lifting by Gaussians: A Simple, Fast and Flexible Method for 3D Instance Segmentation](https://arxiv.org/abs/2502.00173v1)**  
  Authors: Rohan Chacko, Nicolai Haeni, Eldar Khaliullin, Lin Sun, Douglas Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00173v1.pdf)  
  Keywords: segmentation, 3d gaussian, ar, semantic, fast, efficient  
- **[Advancing Dense Endoscopic Reconstruction with Gaussian Splatting-driven Surface Normal-aware Tracking and Mapping](https://arxiv.org/abs/2501.19319v1)**  
  Authors: Yiming Huang, Beilei Cui, Long Bai, Zhen Chen, Jinlin Wu, Zhen Li, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19319v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lastbasket/Endo-2DTAM?style=social)](https://github.com/lastbasket/Endo-2DTAM)  
  Keywords: mapping, 3d gaussian, ar, localization, tracking, real-time rendering, gaussian splatting, face, slam, fast, efficient  
- **[JGHand: Joint-Driven Animatable Hand Avater via 3D Gaussian Splatting](https://arxiv.org/abs/2501.19088v1)**  
  Authors: Zhoutao Sun, Xukun Shen, Yong Hu, Yuyou Zhong, Xueyang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19088v1.pdf)  
  Keywords: shadow, face, ar, deformation, real-time rendering, high-fidelity, human, neural rendering, 3d gaussian, gaussian splatting  

### Applications

*Showing the latest 50 out of 1316 papers*

- **[Self-Calibrating Gaussian Splatting for Large Field of View Reconstruction](https://arxiv.org/abs/2502.09563v1)**  
  Authors: Youming Deng, Wenqi Xian, Guandao Yang, Leonidas Guibas, Gordon Wetzstein, Steve Marschner, Paul Debevec  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09563v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, fast, efficient  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: mapping, geometry, ar, tracking, real-time rendering, sparse-view, slam, gaussian splatting, nerf  
- **[BevSplat: Resolving Height Ambiguity via Feature-Based Gaussian Primitives for Weakly-Supervised Cross-View Localization](https://arxiv.org/abs/2502.09080v1)**  
  Authors: Qiwei Wang, Shaoxun Wu, Yujiao Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09080v1.pdf)  
  Keywords: ar, 3d gaussian, semantic, localization  
- **[Large Images are Gaussians: High-Quality Large Image Representation with Levels of 2D Gaussian Splatting](https://arxiv.org/abs/2502.09039v1)**  
  Authors: Lingting Zhu, Guying Lin, Jinnan Chen, Xinjie Zhang, Zhenchao Jin, Zhao Wang, Lequan Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09039v1.pdf) | [![GitHub](https://img.shields.io/github/stars/HKU-MedAI/LIG?style=social)](https://github.com/HKU-MedAI/LIG)  
  Keywords: ar, gaussian splatting, 3d reconstruction  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, geometry, ar, relightable, dynamic, tracking, real-time rendering, face, lighting, efficient, ray tracing  
- **[Interactive Holographic Visualization for 3D Facial Avatar](https://arxiv.org/abs/2502.08085v1)**  
  Authors: Tri Tung Nguyen Nguyen, Fujii Yasuyuki, Dinh Tuan Tran, Joo-Ho Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08085v1.pdf)  
  Keywords: ar, dynamic, medical, recognition, human, gaussian splatting, 3d gaussian, efficient, avatar  
- **[Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors](https://arxiv.org/abs/2502.07615v1)**  
  Authors: Lin-Zhuo Chen, Kangjie Liu, Youtian Lin, Siyu Zhu, Zhihao Li, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07615v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/fds)  
  Keywords: geometry, 3d gaussian, ar, fast, gaussian splatting  
- **[The establishment of static digital humans and the integration with spinal models](https://arxiv.org/abs/2502.07844v1)**  
  Authors: Fujiao Ju, Yuxuan Wang, Shuo Wang, Chengyin Wang, Yinbo Chen, Jianfeng Li, Mingjie Dong, Bin Fang, Qianyu Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07844v1.pdf)  
  Keywords: ar, dynamic, motion, body, human, 3d gaussian  
- **[TranSplat: Surface Embedding-guided 3D Gaussian Splatting for Transparent Object Manipulation](https://arxiv.org/abs/2502.07840v1)**  
  Authors: Jeongyun Kim, Jeongho Noh, Dong-Guw Lee, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07840v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://github.)  
  Keywords: robotics, ar, face, lighting, 3d gaussian, gaussian splatting  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: 4d, ar, dynamic, motion, deformation, survey, lighting, gaussian splatting, nerf  

### Avatar Generation

*Showing the latest 50 out of 438 papers*

- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, geometry, ar, relightable, dynamic, tracking, real-time rendering, face, lighting, efficient, ray tracing  
- **[Interactive Holographic Visualization for 3D Facial Avatar](https://arxiv.org/abs/2502.08085v1)**  
  Authors: Tri Tung Nguyen Nguyen, Fujii Yasuyuki, Dinh Tuan Tran, Joo-Ho Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08085v1.pdf)  
  Keywords: ar, dynamic, medical, recognition, human, gaussian splatting, 3d gaussian, efficient, avatar  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: face, lighting, shadow, reflection, gaussian splatting, ray tracing  
- **[The establishment of static digital humans and the integration with spinal models](https://arxiv.org/abs/2502.07844v1)**  
  Authors: Fujiao Ju, Yuxuan Wang, Shuo Wang, Chengyin Wang, Yinbo Chen, Jianfeng Li, Mingjie Dong, Bin Fang, Qianyu Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07844v1.pdf)  
  Keywords: ar, dynamic, motion, body, human, 3d gaussian  
- **[TranSplat: Surface Embedding-guided 3D Gaussian Splatting for Transparent Object Manipulation](https://arxiv.org/abs/2502.07840v1)**  
  Authors: Jeongyun Kim, Jeongho Noh, Dong-Guw Lee, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07840v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://github.)  
  Keywords: robotics, ar, face, lighting, 3d gaussian, gaussian splatting  
- **[GARAD-SLAM: 3D GAussian splatting for Real-time Anti Dynamic SLAM](https://arxiv.org/abs/2502.03228v1)**  
  Authors: Mingrui Li, Weijian Chen, Na Cheng, Jingyuan Xu, Dong Li, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.03228v1.pdf)  
  Keywords: mapping, segmentation, ar, dynamic, tracking, face, high-fidelity, 3d gaussian, gaussian splatting, slam  
- **[LAYOUTDREAMER: Physics-guided Layout for Text-to-3D Compositional Scene Generation](https://arxiv.org/abs/2502.01949v1)**  
  Authors: Yang Zhou, Zongjin He, Qixuan Li, Chao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01949v1.pdf)  
  Keywords: ar, dynamic, semantic, face, 3d gaussian, gaussian splatting  
- **[EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](https://arxiv.org/abs/2502.00654v1)**  
  Authors: Junuk Cha, Seongro Yoon, Valeriya Strizhkova, Francois Bremond, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00654v1.pdf)  
  Keywords: head, ar, motion, face, high-fidelity, 3d gaussian, gaussian splatting  
- **[Advancing Dense Endoscopic Reconstruction with Gaussian Splatting-driven Surface Normal-aware Tracking and Mapping](https://arxiv.org/abs/2501.19319v1)**  
  Authors: Yiming Huang, Beilei Cui, Long Bai, Zhen Chen, Jinlin Wu, Zhen Li, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19319v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lastbasket/Endo-2DTAM?style=social)](https://github.com/lastbasket/Endo-2DTAM)  
  Keywords: mapping, 3d gaussian, ar, localization, tracking, real-time rendering, gaussian splatting, face, slam, fast, efficient  
- **[JGHand: Joint-Driven Animatable Hand Avater via 3D Gaussian Splatting](https://arxiv.org/abs/2501.19088v1)**  
  Authors: Zhoutao Sun, Xukun Shen, Yong Hu, Yuyou Zhong, Xueyang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19088v1.pdf)  
  Keywords: shadow, face, ar, deformation, real-time rendering, high-fidelity, human, neural rendering, 3d gaussian, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 489 papers*

- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, geometry, ar, relightable, dynamic, tracking, real-time rendering, face, lighting, efficient, ray tracing  
- **[Interactive Holographic Visualization for 3D Facial Avatar](https://arxiv.org/abs/2502.08085v1)**  
  Authors: Tri Tung Nguyen Nguyen, Fujii Yasuyuki, Dinh Tuan Tran, Joo-Ho Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08085v1.pdf)  
  Keywords: ar, dynamic, medical, recognition, human, gaussian splatting, 3d gaussian, efficient, avatar  
- **[The establishment of static digital humans and the integration with spinal models](https://arxiv.org/abs/2502.07844v1)**  
  Authors: Fujiao Ju, Yuxuan Wang, Shuo Wang, Chengyin Wang, Yinbo Chen, Jianfeng Li, Mingjie Dong, Bin Fang, Qianyu Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07844v1.pdf)  
  Keywords: ar, dynamic, motion, body, human, 3d gaussian  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: 4d, ar, dynamic, motion, deformation, survey, lighting, gaussian splatting, nerf  
- **[High-Speed Dynamic 3D Imaging with Sensor Fusion Splatting](https://arxiv.org/abs/2502.04630v1)**  
  Authors: Zihao Zou, Ziyuan Qu, Xi Peng, Vivek Boominathan, Adithya Pediredla, Praneeth Chakravarthula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04630v1.pdf)  
  Keywords: robotics, efficient, geometry, 3d gaussian, ar, dynamic, motion, deformation, fast, gaussian splatting  
- **[Seeing World Dynamics in a Nutshell](https://arxiv.org/abs/2502.03465v1)**  
  Authors: Qiuhong Shen, Xuanyu Yi, Mingbao Lin, Hanwang Zhang, Shuicheng Yan, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.03465v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Nut-World/NutWorld?style=social)](https://github.com/Nut-World/NutWorld)  
  Keywords: ar, dynamic, motion, high-fidelity, 3d gaussian, efficient  
- **[GARAD-SLAM: 3D GAussian splatting for Real-time Anti Dynamic SLAM](https://arxiv.org/abs/2502.03228v1)**  
  Authors: Mingrui Li, Weijian Chen, Na Cheng, Jingyuan Xu, Dong Li, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.03228v1.pdf)  
  Keywords: mapping, segmentation, ar, dynamic, tracking, face, high-fidelity, 3d gaussian, gaussian splatting, slam  
- **[GP-GS: Gaussian Processes for Enhanced Gaussian Splatting](https://arxiv.org/abs/2502.02283v2)**  
  Authors: Zhihao Guo, Jingxuan Su, Shenglin Wang, Jinlong Fan, Jing Zhang, Liangxiu Han, Peng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.02283v2.pdf)  
  Keywords: efficient, ar, dynamic, motion, 3d gaussian, gaussian splatting, 3d reconstruction  
- **[Efficient Dynamic Scene Editing via 4D Gaussian-based Static-Dynamic Separation](https://arxiv.org/abs/2502.02091v1)**  
  Authors: JooHyun Kwon, Hanbyel Cho, Junmo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.02091v1.pdf)  
  Keywords: 4d, ar, dynamic, deformation, 3d gaussian, efficient  
- **[LAYOUTDREAMER: Physics-guided Layout for Text-to-3D Compositional Scene Generation](https://arxiv.org/abs/2502.01949v1)**  
  Authors: Yang Zhou, Zongjin He, Qixuan Li, Chao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01949v1.pdf)  
  Keywords: ar, dynamic, semantic, face, 3d gaussian, gaussian splatting  

### Few-shot

*Showing the latest 50 out of 93 papers*

- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: mapping, geometry, ar, tracking, real-time rendering, sparse-view, slam, gaussian splatting, nerf  
- **[DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform](https://arxiv.org/abs/2501.12637v2)**  
  Authors: Hung Nguyen, Blark Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12637v2.pdf)  
  Keywords: head, ar, few-shot, fast, nerf  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: 4d, ar, sparse-view, semantic, 3d gaussian, gaussian splatting  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: efficient, ar, sparse-view, 3d gaussian, gaussian splatting, nerf, 3d reconstruction  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: ar, dynamic, medical, sparse view, human, face, lighting, gaussian splatting, nerf  
- **[Synthetic Prior for Few-Shot Drivable Head Avatar Inversion](https://arxiv.org/abs/2501.06903v1)**  
  Authors: Wojciech Zielonka, Stephan J. Garbin, Alexandros Lattas, George Kopanas, Paulo Gotardo, Thabo Beeler, Justus Thies, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06903v1.pdf)  
  Keywords: head, ar, few-shot, 3d gaussian, gaussian splatting, avatar  
- **[NVS-SQA: Exploring Self-Supervised Quality Representation Learning for Neurally Synthesized Scenes without References](https://arxiv.org/abs/2501.06488v1)**  
  Authors: Qiang Qu, Yiran Shen, Xiaoming Chen, Yuk Ying Chung, Weidong Cai, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06488v1.pdf)  
  Keywords: ar, sparse view, human, 3d gaussian, gaussian splatting, nerf  
- **[FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency](https://arxiv.org/abs/2501.04628v1)**  
  Authors: Han Huang, Yulun Wu, Chao Deng, Ge Gao, Ming Gu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04628v1.pdf)  
  Keywords: ar, sparse view, sparse-view, face, fast, gaussian splatting  
- **[Dust to Tower: Coarse-to-Fine Photo-Realistic Scene Reconstruction from Sparse Uncalibrated Images](https://arxiv.org/abs/2412.19518v1)**  
  Authors: Xudong Cai, Yongcai Wang, Zhaoxin Fan, Deng Haoran, Shuo Wang, Wanting Li, Deying Li, Lun Luo, Minhang Wang, Jintao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19518v1.pdf)  
  Keywords: 3d gaussian, ar, sparse-view, gaussian splatting, fast, efficient  
- **[CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting](https://arxiv.org/abs/2412.19142v1)**  
  Authors: Siyu Jiao, Haoye Dong, Yuyang Yin, Zequn Jie, Yinlong Qian, Yao Zhao, Humphrey Shi, Yunchao Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19142v1.pdf)  
  Keywords: ar, few-shot, gaussian splatting, 3d gaussian, efficient  

### Geometry Reconstruction

*Showing the latest 50 out of 433 papers*

- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: mapping, geometry, ar, tracking, real-time rendering, sparse-view, slam, gaussian splatting, nerf  
- **[Large Images are Gaussians: High-Quality Large Image Representation with Levels of 2D Gaussian Splatting](https://arxiv.org/abs/2502.09039v1)**  
  Authors: Lingting Zhu, Guying Lin, Jinnan Chen, Xinjie Zhang, Zhenchao Jin, Zhao Wang, Lequan Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09039v1.pdf) | [![GitHub](https://img.shields.io/github/stars/HKU-MedAI/LIG?style=social)](https://github.com/HKU-MedAI/LIG)  
  Keywords: ar, gaussian splatting, 3d reconstruction  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, geometry, ar, relightable, dynamic, tracking, real-time rendering, face, lighting, efficient, ray tracing  
- **[Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors](https://arxiv.org/abs/2502.07615v1)**  
  Authors: Lin-Zhuo Chen, Kangjie Liu, Youtian Lin, Siyu Zhu, Zhihao Li, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07615v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/fds)  
  Keywords: geometry, 3d gaussian, ar, fast, gaussian splatting  
- **[GaussRender: Learning 3D Occupancy with Gaussian Rendering](https://arxiv.org/abs/2502.05040v1)**  
  Authors: Loick Chambon, Eloi Zablocki, Alexandre Boulch, Mickael Chen, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05040v1.pdf) | [![GitHub](https://img.shields.io/github/stars/valeoai/GaussRender?style=social)](https://github.com/valeoai/GaussRender)  
  Keywords: understanding, geometry, ar, gaussian splatting, semantic, lighting, efficient  
- **[OccGS: Zero-shot 3D Occupancy Reconstruction with Semantic and Geometric-Aware Gaussian Splatting](https://arxiv.org/abs/2502.04981v1)**  
  Authors: Xiaoyu Zhou, Jingqi Wang, Yongtao Wang, Yufei Wei, Nan Dong, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04981v1.pdf)  
  Keywords: ar, gaussian splatting, geometry, semantic  
- **[SC-OmniGS: Self-Calibrating Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2502.04734v1)**  
  Authors: Huajian Huang, Yingshu Chen, Longwei Li, Hui Cheng, Tristan Braud, Yajie Zhao, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04734v1.pdf)  
  Keywords: 3d gaussian, ar, fast, gaussian splatting, 3d reconstruction  
- **[High-Speed Dynamic 3D Imaging with Sensor Fusion Splatting](https://arxiv.org/abs/2502.04630v1)**  
  Authors: Zihao Zou, Ziyuan Qu, Xi Peng, Vivek Boominathan, Adithya Pediredla, Praneeth Chakravarthula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04630v1.pdf)  
  Keywords: robotics, efficient, geometry, 3d gaussian, ar, dynamic, motion, deformation, fast, gaussian splatting  
- **[GP-GS: Gaussian Processes for Enhanced Gaussian Splatting](https://arxiv.org/abs/2502.02283v2)**  
  Authors: Zhihao Guo, Jingxuan Su, Shenglin Wang, Jinlong Fan, Jing Zhang, Liangxiu Han, Peng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.02283v2.pdf)  
  Keywords: efficient, ar, dynamic, motion, 3d gaussian, gaussian splatting, 3d reconstruction  
- **[VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion](https://arxiv.org/abs/2502.01536v1)**  
  Authors: Shaoting Zhu, Linzhan Mou, Derun Li, Baijun Ye, Runhan Huang, Hang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01536v1.pdf)  
  Keywords: geometry, vr, ar, motion, tracking, lighting, 3d gaussian, gaussian splatting  

### Large Scene

*Showing the latest 50 out of 70 papers*

- **[PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression](https://arxiv.org/abs/2502.04843v2)**  
  Authors: Feifei Li, Qi Song, Chi Zhang, Hui Shuai, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04843v2.pdf)  
  Keywords: ar, outdoor, gaussian splatting, nerf  
- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, efficient, outdoor  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: mapping, geometry, ar, dynamic, large scene, localization, slam, outdoor, gaussian splatting, nerf  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: ar, dynamic, motion, real-time rendering, understanding, 3d gaussian, outdoor  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: mapping, efficient, slam, ar, neural rendering, 3d gaussian, gaussian splatting, nerf, outdoor  
- **[WeatherGS: 3D Scene Reconstruction in Adverse Weather Conditions via Gaussian Splatting](https://arxiv.org/abs/2412.18862v3)**  
  Authors: Chenghao Qian, Yuhu Guo, Wenjing Li, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.18862v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/weather-gs.)  
  Keywords: 3d reconstruction, ar, 3d gaussian, gaussian splatting, outdoor  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: 3d gaussian, ar, large scene, face, high-fidelity, fast, gaussian splatting, nerf, compression  
- **[LiHi-GS: LiDAR-Supervised Gaussian Splatting for Highway Driving Scene Reconstruction](https://arxiv.org/abs/2412.15447v2)**  
  Authors: Pou-Chun Kung, Xianling Zhang, Katherine A. Skinner, Nikita Jaipuria  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15447v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/lihi_gs)  
  Keywords: autonomous driving, 3d gaussian, ar, dynamic, urban scene, fast, gaussian splatting, nerf  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: mapping, geometry, reflection, ar, dynamic, localization, tracking, survey, face, lighting, slam, 3d gaussian, outdoor  
- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: head, ar, dynamic, large scene, 3d gaussian, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 492 papers*

- **[Self-Calibrating Gaussian Splatting for Large Field of View Reconstruction](https://arxiv.org/abs/2502.09563v1)**  
  Authors: Youming Deng, Wenqi Xian, Guandao Yang, Leonidas Guibas, Gordon Wetzstein, Steve Marschner, Paul Debevec  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09563v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, fast, efficient  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, geometry, ar, relightable, dynamic, tracking, real-time rendering, face, lighting, efficient, ray tracing  
- **[Interactive Holographic Visualization for 3D Facial Avatar](https://arxiv.org/abs/2502.08085v1)**  
  Authors: Tri Tung Nguyen Nguyen, Fujii Yasuyuki, Dinh Tuan Tran, Joo-Ho Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08085v1.pdf)  
  Keywords: ar, dynamic, medical, recognition, human, gaussian splatting, 3d gaussian, efficient, avatar  
- **[PINGS: Gaussian Splatting Meets Distance Fields within a Point-Based Implicit Neural Map](https://arxiv.org/abs/2502.05752v1)**  
  Authors: Yue Pan, Xingguang Zhong, Liren Jin, Louis Wiesmann, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05752v1.pdf)  
  Keywords: mapping, high quality, ar, compact, high-fidelity, gaussian splatting, slam  
- **[Vision-in-the-loop Simulation for Deep Monocular Pose Estimation of UAV in Ocean Environment](https://arxiv.org/abs/2502.05409v1)**  
  Authors: Maneesha Wickramasuriya, Beomyeol Yu, Taeyoung Lee, Murray Snyder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05409v1.pdf)  
  Keywords: ar, lightweight, gaussian splatting  
- **[GaussRender: Learning 3D Occupancy with Gaussian Rendering](https://arxiv.org/abs/2502.05040v1)**  
  Authors: Loick Chambon, Eloi Zablocki, Alexandre Boulch, Mickael Chen, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05040v1.pdf) | [![GitHub](https://img.shields.io/github/stars/valeoai/GaussRender?style=social)](https://github.com/valeoai/GaussRender)  
  Keywords: understanding, geometry, ar, gaussian splatting, semantic, lighting, efficient  
- **[High-Speed Dynamic 3D Imaging with Sensor Fusion Splatting](https://arxiv.org/abs/2502.04630v1)**  
  Authors: Zihao Zou, Ziyuan Qu, Xi Peng, Vivek Boominathan, Adithya Pediredla, Praneeth Chakravarthula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04630v1.pdf)  
  Keywords: robotics, efficient, geometry, 3d gaussian, ar, dynamic, motion, deformation, fast, gaussian splatting  
- **[Seeing World Dynamics in a Nutshell](https://arxiv.org/abs/2502.03465v1)**  
  Authors: Qiuhong Shen, Xuanyu Yi, Mingbao Lin, Hanwang Zhang, Shuicheng Yan, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.03465v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Nut-World/NutWorld?style=social)](https://github.com/Nut-World/NutWorld)  
  Keywords: ar, dynamic, motion, high-fidelity, 3d gaussian, efficient  
- **[GP-GS: Gaussian Processes for Enhanced Gaussian Splatting](https://arxiv.org/abs/2502.02283v2)**  
  Authors: Zhihao Guo, Jingxuan Su, Shenglin Wang, Jinlong Fan, Jing Zhang, Liangxiu Han, Peng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.02283v2.pdf)  
  Keywords: efficient, ar, dynamic, motion, 3d gaussian, gaussian splatting, 3d reconstruction  
- **[Efficient Dynamic Scene Editing via 4D Gaussian-based Static-Dynamic Separation](https://arxiv.org/abs/2502.02091v1)**  
  Authors: JooHyun Kwon, Hanbyel Cho, Junmo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.02091v1.pdf)  
  Keywords: 4d, ar, dynamic, deformation, 3d gaussian, efficient  

### Quality Enhancement

*Showing the latest 50 out of 213 papers*

- **[SIREN: Semantic, Initialization-Free Registration of Multi-Robot Gaussian Splatting Maps](https://arxiv.org/abs/2502.06519v1)**  
  Authors: Ola Shorinwa, Jiankai Sun, Mac Schwager, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.06519v1.pdf)  
  Keywords: ar, semantic, high-fidelity, 3d gaussian, gaussian splatting  
- **[PINGS: Gaussian Splatting Meets Distance Fields within a Point-Based Implicit Neural Map](https://arxiv.org/abs/2502.05752v1)**  
  Authors: Yue Pan, Xingguang Zhong, Liren Jin, Louis Wiesmann, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05752v1.pdf)  
  Keywords: mapping, high quality, ar, compact, high-fidelity, gaussian splatting, slam  
- **[Seeing World Dynamics in a Nutshell](https://arxiv.org/abs/2502.03465v1)**  
  Authors: Qiuhong Shen, Xuanyu Yi, Mingbao Lin, Hanwang Zhang, Shuicheng Yan, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.03465v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Nut-World/NutWorld?style=social)](https://github.com/Nut-World/NutWorld)  
  Keywords: ar, dynamic, motion, high-fidelity, 3d gaussian, efficient  
- **[GARAD-SLAM: 3D GAussian splatting for Real-time Anti Dynamic SLAM](https://arxiv.org/abs/2502.03228v1)**  
  Authors: Mingrui Li, Weijian Chen, Na Cheng, Jingyuan Xu, Dong Li, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.03228v1.pdf)  
  Keywords: mapping, segmentation, ar, dynamic, tracking, face, high-fidelity, 3d gaussian, gaussian splatting, slam  
- **[EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](https://arxiv.org/abs/2502.00654v1)**  
  Authors: Junuk Cha, Seongro Yoon, Valeriya Strizhkova, Francois Bremond, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00654v1.pdf)  
  Keywords: head, ar, motion, face, high-fidelity, 3d gaussian, gaussian splatting  
- **[JGHand: Joint-Driven Animatable Hand Avater via 3D Gaussian Splatting](https://arxiv.org/abs/2501.19088v1)**  
  Authors: Zhoutao Sun, Xukun Shen, Yong Hu, Yuyou Zhong, Xueyang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19088v1.pdf)  
  Keywords: shadow, face, ar, deformation, real-time rendering, high-fidelity, human, neural rendering, 3d gaussian, gaussian splatting  
- **[StructuredField: Unifying Structured Geometry and Radiance Field](https://arxiv.org/abs/2501.18152v1)**  
  Authors: Kaiwen Song, Jinkai Cui, Zherui Qiu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18152v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, deformation, high-fidelity, fast  
- **[Towards Better Robustness: Progressively Joint Pose-3DGS Learning for Arbitrarily Long Videos](https://arxiv.org/abs/2501.15096v1)**  
  Authors: Zhen-Hui Dong, Sheng Ye, Yu-Hui Wen, Nannan Li, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15096v1.pdf)  
  Keywords: ar, motion, tracking, face, high-fidelity, 3d gaussian, gaussian splatting  
- **[Trick-GS: A Balanced Bag of Tricks for Efficient Gaussian Splatting](https://arxiv.org/abs/2501.14534v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Mateusz Nowak, Mehmet Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.14534v1.pdf)  
  Keywords: high quality, ar, gaussian splatting, fast, efficient, 3d reconstruction  
- **[Deblur-Avatar: Animatable Avatars from Motion-Blurred Monocular Videos](https://arxiv.org/abs/2501.13335v1)**  
  Authors: Xianrui Luo, Juewen Peng, Zhongang Cai, Lei Yang, Fan Yang, Zhiguo Cao, Guosheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13335v1.pdf)  
  Keywords: ar, dynamic, motion, body, real-time rendering, human, high-fidelity, 3d gaussian, gaussian splatting, avatar  

### Ray Tracing

- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, geometry, ar, relightable, dynamic, tracking, real-time rendering, face, lighting, efficient, ray tracing  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: face, lighting, shadow, reflection, gaussian splatting, ray tracing  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ar, survey, 3d gaussian, gaussian splatting, ray tracing  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: efficient, acceleration, ar, light transport, reflection, gaussian splatting, ray tracing  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: reflection, ar, shadow, 3d gaussian, gaussian splatting, ray tracing  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: relighting, efficient, ar, lighting, reflection, gaussian splatting, ray tracing  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: efficient, reflection, ar, real-time rendering, lighting, high-fidelity, 3d gaussian, gaussian splatting, ray tracing  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: mapping, efficient, global illumination, geometry, ar, gaussian splatting, face, fast, illumination, nerf  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, efficient, ray tracing  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: ar, 3d gaussian, gaussian splatting, ray tracing  

### Relighting

*Showing the latest 50 out of 148 papers*

- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, geometry, ar, relightable, dynamic, tracking, real-time rendering, face, lighting, efficient, ray tracing  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: face, lighting, shadow, reflection, gaussian splatting, ray tracing  
- **[TranSplat: Surface Embedding-guided 3D Gaussian Splatting for Transparent Object Manipulation](https://arxiv.org/abs/2502.07840v1)**  
  Authors: Jeongyun Kim, Jeongho Noh, Dong-Guw Lee, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07840v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://github.)  
  Keywords: robotics, ar, face, lighting, 3d gaussian, gaussian splatting  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: 4d, ar, dynamic, motion, deformation, survey, lighting, gaussian splatting, nerf  
- **[GaussRender: Learning 3D Occupancy with Gaussian Rendering](https://arxiv.org/abs/2502.05040v1)**  
  Authors: Loick Chambon, Eloi Zablocki, Alexandre Boulch, Mickael Chen, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05040v1.pdf) | [![GitHub](https://img.shields.io/github/stars/valeoai/GaussRender?style=social)](https://github.com/valeoai/GaussRender)  
  Keywords: understanding, geometry, ar, gaussian splatting, semantic, lighting, efficient  
- **[VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion](https://arxiv.org/abs/2502.01536v1)**  
  Authors: Shaoting Zhu, Linzhan Mou, Derun Li, Baijun Ye, Runhan Huang, Hang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01536v1.pdf)  
  Keywords: geometry, vr, ar, motion, tracking, lighting, 3d gaussian, gaussian splatting  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: efficient, acceleration, ar, light transport, reflection, gaussian splatting, ray tracing  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: reflection, ar, shadow, 3d gaussian, gaussian splatting, ray tracing  
- **[JGHand: Joint-Driven Animatable Hand Avater via 3D Gaussian Splatting](https://arxiv.org/abs/2501.19088v1)**  
  Authors: Zhoutao Sun, Xukun Shen, Yong Hu, Yuyou Zhong, Xueyang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19088v1.pdf)  
  Keywords: shadow, face, ar, deformation, real-time rendering, high-fidelity, human, neural rendering, 3d gaussian, gaussian splatting  
- **[VoD-3DGS: View-opacity-Dependent 3D Gaussian Splatting](https://arxiv.org/abs/2501.17978v2)**  
  Authors: Mateusz Nowak, Wojciech Jarosz, Peter Chin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.17978v2.pdf)  
  Keywords: reflection, ar, face, 3d gaussian, gaussian splatting, nerf  

### SLAM

*Showing the latest 50 out of 196 papers*

- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: mapping, geometry, ar, tracking, real-time rendering, sparse-view, slam, gaussian splatting, nerf  
- **[BevSplat: Resolving Height Ambiguity via Feature-Based Gaussian Primitives for Weakly-Supervised Cross-View Localization](https://arxiv.org/abs/2502.09080v1)**  
  Authors: Qiwei Wang, Shaoxun Wu, Yujiao Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09080v1.pdf)  
  Keywords: ar, 3d gaussian, semantic, localization  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, geometry, ar, relightable, dynamic, tracking, real-time rendering, face, lighting, efficient, ray tracing  
- **[Digital Twin Buildings: 3D Modeling, GIS Integration, and Visual Descriptions Using Gaussian Splatting, ChatGPT/Deepseek, and Google Maps Platform](https://arxiv.org/abs/2502.05769v2)**  
  Authors: Kyle Gao, Dening Lu, Liangzhi Li, Nan Chen, Hongjie He, Linlin Xu, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05769v2.pdf)  
  Keywords: ar, mapping, gaussian splatting  
- **[PINGS: Gaussian Splatting Meets Distance Fields within a Point-Based Implicit Neural Map](https://arxiv.org/abs/2502.05752v1)**  
  Authors: Yue Pan, Xingguang Zhong, Liren Jin, Louis Wiesmann, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05752v1.pdf)  
  Keywords: mapping, high quality, ar, compact, high-fidelity, gaussian splatting, slam  
- **[GARAD-SLAM: 3D GAussian splatting for Real-time Anti Dynamic SLAM](https://arxiv.org/abs/2502.03228v1)**  
  Authors: Mingrui Li, Weijian Chen, Na Cheng, Jingyuan Xu, Dong Li, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.03228v1.pdf)  
  Keywords: mapping, segmentation, ar, dynamic, tracking, face, high-fidelity, 3d gaussian, gaussian splatting, slam  
- **[UVGS: Reimagining Unstructured 3D Gaussian Splatting using UV Mapping](https://arxiv.org/abs/2502.01846v2)**  
  Authors: Aashish Rai, Dilin Wang, Mihir Jain, Nikolaos Sarafianos, Kefan Chen, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01846v2.pdf)  
  Keywords: ar, mapping, 3d gaussian, gaussian splatting  
- **[VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion](https://arxiv.org/abs/2502.01536v1)**  
  Authors: Shaoting Zhu, Linzhan Mou, Derun Li, Baijun Ye, Runhan Huang, Hang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01536v1.pdf)  
  Keywords: geometry, vr, ar, motion, tracking, lighting, 3d gaussian, gaussian splatting  
- **[Advancing Dense Endoscopic Reconstruction with Gaussian Splatting-driven Surface Normal-aware Tracking and Mapping](https://arxiv.org/abs/2501.19319v1)**  
  Authors: Yiming Huang, Beilei Cui, Long Bai, Zhen Chen, Jinlin Wu, Zhen Li, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19319v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lastbasket/Endo-2DTAM?style=social)](https://github.com/lastbasket/Endo-2DTAM)  
  Keywords: mapping, 3d gaussian, ar, localization, tracking, real-time rendering, gaussian splatting, face, slam, fast, efficient  
- **[Towards Better Robustness: Progressively Joint Pose-3DGS Learning for Arbitrarily Long Videos](https://arxiv.org/abs/2501.15096v1)**  
  Authors: Zhen-Hui Dong, Sheng Ye, Yu-Hui Wen, Nannan Li, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15096v1.pdf)  
  Keywords: ar, motion, tracking, face, high-fidelity, 3d gaussian, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 229 papers*

- **[BevSplat: Resolving Height Ambiguity via Feature-Based Gaussian Primitives for Weakly-Supervised Cross-View Localization](https://arxiv.org/abs/2502.09080v1)**  
  Authors: Qiwei Wang, Shaoxun Wu, Yujiao Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09080v1.pdf)  
  Keywords: ar, 3d gaussian, semantic, localization  
- **[Interactive Holographic Visualization for 3D Facial Avatar](https://arxiv.org/abs/2502.08085v1)**  
  Authors: Tri Tung Nguyen Nguyen, Fujii Yasuyuki, Dinh Tuan Tran, Joo-Ho Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08085v1.pdf)  
  Keywords: ar, dynamic, medical, recognition, human, gaussian splatting, 3d gaussian, efficient, avatar  
- **[SIREN: Semantic, Initialization-Free Registration of Multi-Robot Gaussian Splatting Maps](https://arxiv.org/abs/2502.06519v1)**  
  Authors: Ola Shorinwa, Jiankai Sun, Mac Schwager, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.06519v1.pdf)  
  Keywords: ar, semantic, high-fidelity, 3d gaussian, gaussian splatting  
- **[GaussRender: Learning 3D Occupancy with Gaussian Rendering](https://arxiv.org/abs/2502.05040v1)**  
  Authors: Loick Chambon, Eloi Zablocki, Alexandre Boulch, Mickael Chen, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05040v1.pdf) | [![GitHub](https://img.shields.io/github/stars/valeoai/GaussRender?style=social)](https://github.com/valeoai/GaussRender)  
  Keywords: understanding, geometry, ar, gaussian splatting, semantic, lighting, efficient  
- **[OccGS: Zero-shot 3D Occupancy Reconstruction with Semantic and Geometric-Aware Gaussian Splatting](https://arxiv.org/abs/2502.04981v1)**  
  Authors: Xiaoyu Zhou, Jingqi Wang, Yongtao Wang, Yufei Wei, Nan Dong, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04981v1.pdf)  
  Keywords: ar, gaussian splatting, geometry, semantic  
- **[GARAD-SLAM: 3D GAussian splatting for Real-time Anti Dynamic SLAM](https://arxiv.org/abs/2502.03228v1)**  
  Authors: Mingrui Li, Weijian Chen, Na Cheng, Jingyuan Xu, Dong Li, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.03228v1.pdf)  
  Keywords: mapping, segmentation, ar, dynamic, tracking, face, high-fidelity, 3d gaussian, gaussian splatting, slam  
- **[LAYOUTDREAMER: Physics-guided Layout for Text-to-3D Compositional Scene Generation](https://arxiv.org/abs/2502.01949v1)**  
  Authors: Yang Zhou, Zongjin He, Qixuan Li, Chao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01949v1.pdf)  
  Keywords: ar, dynamic, semantic, face, 3d gaussian, gaussian splatting  
- **[Lifting by Gaussians: A Simple, Fast and Flexible Method for 3D Instance Segmentation](https://arxiv.org/abs/2502.00173v1)**  
  Authors: Rohan Chacko, Nicolai Haeni, Eldar Khaliullin, Lin Sun, Douglas Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00173v1.pdf)  
  Keywords: segmentation, 3d gaussian, ar, semantic, fast, efficient  
- **[3D Reconstruction of Shoes for Augmented Reality](https://arxiv.org/abs/2501.18643v1)**  
  Authors: Pratik Shrestha, Sujan Kapali, Swikar Gautam, Vishal Pokharel, Santosh Giri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.18643v1.pdf)  
  Keywords: segmentation, ar, 3d gaussian, gaussian splatting, 3d reconstruction  
- **[GaussianToken: An Effective Image Tokenizer with 2D Gaussian Splatting](https://arxiv.org/abs/2501.15619v1)**  
  Authors: Jiajun Dong, Chengkun Wang, Wenzhao Zheng, Lei Chen, Jiwen Lu, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.15619v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ChrisDong-THU/GaussianToken?style=social)](https://github.com/ChrisDong-THU/GaussianToken)  
  Keywords: understanding, efficient, gaussian splatting, ar  



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