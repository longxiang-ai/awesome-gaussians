# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-03-09 00:42:20

## Categories

- [3DGS Surveys](#3dgs-surveys) (23 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (395 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1390 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (466 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (514 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (97 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (461 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (75 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (529 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (224 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (33 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (154 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (209 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (243 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: compression, gaussian splatting, 3d reconstruction, real-time rendering, survey, nerf, ar, 3d gaussian, efficient  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: gaussian splatting, 4d, motion, dynamic, lighting, survey, nerf, ar, deformation  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, ray tracing, survey, ar, 3d gaussian  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: tracking, geometry, reflection, dynamic, localization, lighting, survey, face, outdoor, slam, mapping, ar, 3d gaussian  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: gaussian splatting, illumination, survey, ar, 3d gaussian, recognition  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: gaussian splatting, autonomous driving, 3d reconstruction, robotics, geometry, compact, dynamic, lighting, survey, nerf, ar, semantic, high-fidelity  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: gaussian splatting, robotics, real-time rendering, survey, nerf, ar, 3d gaussian, understanding  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: gaussian splatting, lighting, survey, nerf, ar, 3d gaussian, high-fidelity  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: gaussian splatting, vr, autonomous driving, 3d reconstruction, robotics, survey, nerf, ar, 3d gaussian  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: 3d gaussian, survey, ar  

### Acceleration

*Showing the latest 50 out of 395 papers*

- **[GaussianVideo: Efficient Video Representation and Compression by Gaussian Splatting](https://arxiv.org/abs/2503.04333v1)**  
  Authors: Inseo Lee, Youngyoon Choi, Joonseok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04333v1.pdf)  
  Keywords: compression, gaussian splatting, dynamic, lightweight, ar, fast, efficient  
- **[Surgical Gaussian Surfels: Highly Accurate Real-time Surgical Scene Rendering](https://arxiv.org/abs/2503.04079v1)**  
  Authors: Idris O. Sunmola, Zhenjun Zhao, Samuel Schmidgall, Yumeng Wang, Paul Maria Scheikl, Axel Krieger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04079v1.pdf) | [![GitHub](https://img.shields.io/github/stars/aloma85/SurgicalGaussianSurfels?style=social)](https://github.com/aloma85/SurgicalGaussianSurfels)  
  Keywords: real-time rendering, geometry, motion, lightweight, face, nerf, ar, efficient, 3d gaussian, deformation  
- **[Beyond Existance: Fulfill 3D Reconstructed Scenes with Pseudo Details](https://arxiv.org/abs/2503.04037v1)**  
  Authors: Yifei Gao, Jun Huang, Lei Wang, Ruiting Dai, Jun Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04037v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, ar, fast, 3d gaussian  
- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: gaussian splatting, avatar, human, real-time rendering, geometry, dynamic, nerf, fast, ar, 3d gaussian, high-fidelity  
- **[OpenGS-SLAM: Open-Set Dense Semantic SLAM with 3D Gaussian Splatting for Object-Level Scene Understanding](https://arxiv.org/abs/2503.01646v1)**  
  Authors: Dianyi Yang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01646v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://young-bit.github.io/opengs-github.github.io/.)  
  Keywords: gaussian splatting, tracking, slam, fast, segmentation, mapping, ar, 3d gaussian, semantic, understanding  
- **[Evolving High-Quality Rendering and Reconstruction in a Unified Framework with Contribution-Adaptive Regularization](https://arxiv.org/abs/2503.00881v1)**  
  Authors: You Shen, Zhipeng Zhang, Xinyang Li, Yansong Qu, Yu Lin, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00881v1.pdf)  
  Keywords: gaussian splatting, geometry, compact, face, ar, fast, 3d gaussian  
- **[InsTaG: Learning Personalized 3D Talking Head from Few-Second Video](https://arxiv.org/abs/2502.20387v1)**  
  Authors: Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Jun Zhou, Lin Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20387v1.pdf)  
  Keywords: head, motion, dynamic, lightweight, ar, fast  
- **[Does 3D Gaussian Splatting Need Accurate Volumetric Rendering?](https://arxiv.org/abs/2502.19318v1)**  
  Authors: Adam Celarek, George Kopanas, George Drettakis, Michael Wimmer, Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19318v1.pdf)  
  Keywords: gaussian splatting, nerf, fast, ar, 3d gaussian, efficient  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: compression, gaussian splatting, 3d reconstruction, real-time rendering, survey, nerf, ar, 3d gaussian, efficient  
- **[GaussianFlowOcc: Sparse and Weakly Supervised Occupancy Estimation using Gaussian Splatting and Temporal Flow](https://arxiv.org/abs/2502.17288v2)**  
  Authors: Simon Boeder, Fabian Gigengack, Benjamin Risse  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17288v2.pdf)  
  Keywords: gaussian splatting, autonomous driving, dynamic, ar, fast, 3d gaussian, efficient  

### Applications

*Showing the latest 50 out of 1390 papers*

- **[GaussianVideo: Efficient Video Representation and Compression by Gaussian Splatting](https://arxiv.org/abs/2503.04333v1)**  
  Authors: Inseo Lee, Youngyoon Choi, Joonseok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04333v1.pdf)  
  Keywords: compression, gaussian splatting, dynamic, lightweight, ar, fast, efficient  
- **[S2Gaussian: Sparse-View Super-Resolution 3D Gaussian Splatting](https://arxiv.org/abs/2503.04314v1)**  
  Authors: Yecong Wan, Mingwen Shao, Yuanshuo Cheng, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04314v1.pdf)  
  Keywords: gaussian splatting, geometry, sparse view, ar, sparse-view, 3d gaussian  
- **[Instrument-Splatting: Controllable Photorealistic Reconstruction of Surgical Instruments Using Gaussian Splatting](https://arxiv.org/abs/2503.04082v1)**  
  Authors: Shuojue Yang, Zijian Wu, Mingxuan Hong, Qian Li, Daiyun Shen, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04082v1.pdf)  
  Keywords: gaussian splatting, tracking, 3d reconstruction, geometry, ar, 3d gaussian, semantic  
- **[Surgical Gaussian Surfels: Highly Accurate Real-time Surgical Scene Rendering](https://arxiv.org/abs/2503.04079v1)**  
  Authors: Idris O. Sunmola, Zhenjun Zhao, Samuel Schmidgall, Yumeng Wang, Paul Maria Scheikl, Axel Krieger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04079v1.pdf) | [![GitHub](https://img.shields.io/github/stars/aloma85/SurgicalGaussianSurfels?style=social)](https://github.com/aloma85/SurgicalGaussianSurfels)  
  Keywords: real-time rendering, geometry, motion, lightweight, face, nerf, ar, efficient, 3d gaussian, deformation  
- **[Beyond Existance: Fulfill 3D Reconstructed Scenes with Pseudo Details](https://arxiv.org/abs/2503.04037v1)**  
  Authors: Yifei Gao, Jun Huang, Lei Wang, Ruiting Dai, Jun Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04037v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, ar, fast, 3d gaussian  
- **[GaussianGraph: 3D Gaussian-based Scene Graph Generation for Open-world Scene Understanding](https://arxiv.org/abs/2503.04034v1)**  
  Authors: Xihan Wang, Dianyi Yang, Yu Gao, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04034v1.pdf)  
  Keywords: compression, gaussian splatting, dynamic, ar, segmentation, 3d gaussian, semantic, understanding  
- **[GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2503.03984v1)**  
  Authors: Qianzhong Chen, Jiankai Sun, Naixiang Gao, JunEn Low, Timothy Chen, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03984v1.pdf)  
  Keywords: gaussian splatting, dynamic, ar, 3d gaussian, efficient, high-fidelity  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: gaussian splatting, human, neural rendering, few-shot, semantic, nerf, ar, efficient  
- **[Direct Sparse Odometry with Continuous 3D Gaussian Maps for Indoor Environments](https://arxiv.org/abs/2503.03373v1)**  
  Authors: Jie Deng, Fengtian Lang, Zikang Yuan, Xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03373v1.pdf)  
  Keywords: tracking, robotics, localization, ar, 3d gaussian  
- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115v1)**  
  Authors: Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03115v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 4d, dynamic, face, ar, efficient  

### Avatar Generation

*Showing the latest 50 out of 466 papers*

- **[Surgical Gaussian Surfels: Highly Accurate Real-time Surgical Scene Rendering](https://arxiv.org/abs/2503.04079v1)**  
  Authors: Idris O. Sunmola, Zhenjun Zhao, Samuel Schmidgall, Yumeng Wang, Paul Maria Scheikl, Axel Krieger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04079v1.pdf) | [![GitHub](https://img.shields.io/github/stars/aloma85/SurgicalGaussianSurfels?style=social)](https://github.com/aloma85/SurgicalGaussianSurfels)  
  Keywords: real-time rendering, geometry, motion, lightweight, face, nerf, ar, efficient, 3d gaussian, deformation  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: gaussian splatting, human, neural rendering, few-shot, semantic, nerf, ar, efficient  
- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115v1)**  
  Authors: Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03115v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 4d, dynamic, face, ar, efficient  
- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: gaussian splatting, avatar, human, real-time rendering, geometry, dynamic, nerf, fast, ar, 3d gaussian, high-fidelity  
- **[Vid2Avatar-Pro: Authentic Avatar from Videos in the Wild via Universal Prior](https://arxiv.org/abs/2503.01610v1)**  
  Authors: Chen Guo, Junxuan Li, Yash Kant, Yaser Sheikh, Shunsuke Saito, Chen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01610v1.pdf)  
  Keywords: avatar, human, motion, ar, 3d gaussian, animation  
- **[LiteGS: A High-Performance Modular Framework for Gaussian Splatting Training](https://arxiv.org/abs/2503.01199v1)**  
  Authors: Kaimin Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01199v1.pdf)  
  Keywords: gaussian splatting, head, face, ar, nerf  
- **[Evolving High-Quality Rendering and Reconstruction in a Unified Framework with Contribution-Adaptive Regularization](https://arxiv.org/abs/2503.00881v1)**  
  Authors: You Shen, Zhipeng Zhang, Xinyang Li, Yansong Qu, Yu Lin, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00881v1.pdf)  
  Keywords: gaussian splatting, geometry, compact, face, ar, fast, 3d gaussian  
- **[Vid2Fluid: 3D Dynamic Fluid Assets from Single-View Videos with Generative Gaussian Splatting](https://arxiv.org/abs/2503.00868v1)**  
  Authors: Zhiwei Zhao, Alan Zhao, Minchen Li, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00868v1.pdf)  
  Keywords: gaussian splatting, geometry, dynamic, face, ar, 3d gaussian  
- **[PSRGS:Progressive Spectral Residual of 3D Gaussian for High-Frequency Recovery](https://arxiv.org/abs/2503.00848v1)**  
  Authors: BoCheng Li, WenJuan Zhang, Bing Zhang, YiLing Yao, YaNing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00848v1.pdf)  
  Keywords: gaussian splatting, motion, geometry, face, ar, 3d gaussian  
- **[GaussianSeal: Rooting Adaptive Watermarks for 3D Gaussian Generation Model](https://arxiv.org/abs/2503.00531v1)**  
  Authors: Runyi Li, Xuanyu Zhang, Chuhan Tong, Zhipei Xu, Jian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00531v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, head  

### Dynamic Scene

*Showing the latest 50 out of 514 papers*

- **[GaussianVideo: Efficient Video Representation and Compression by Gaussian Splatting](https://arxiv.org/abs/2503.04333v1)**  
  Authors: Inseo Lee, Youngyoon Choi, Joonseok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04333v1.pdf)  
  Keywords: compression, gaussian splatting, dynamic, lightweight, ar, fast, efficient  
- **[Surgical Gaussian Surfels: Highly Accurate Real-time Surgical Scene Rendering](https://arxiv.org/abs/2503.04079v1)**  
  Authors: Idris O. Sunmola, Zhenjun Zhao, Samuel Schmidgall, Yumeng Wang, Paul Maria Scheikl, Axel Krieger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04079v1.pdf) | [![GitHub](https://img.shields.io/github/stars/aloma85/SurgicalGaussianSurfels?style=social)](https://github.com/aloma85/SurgicalGaussianSurfels)  
  Keywords: real-time rendering, geometry, motion, lightweight, face, nerf, ar, efficient, 3d gaussian, deformation  
- **[GaussianGraph: 3D Gaussian-based Scene Graph Generation for Open-world Scene Understanding](https://arxiv.org/abs/2503.04034v1)**  
  Authors: Xihan Wang, Dianyi Yang, Yu Gao, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04034v1.pdf)  
  Keywords: compression, gaussian splatting, dynamic, ar, segmentation, 3d gaussian, semantic, understanding  
- **[GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2503.03984v1)**  
  Authors: Qianzhong Chen, Jiankai Sun, Naixiang Gao, JunEn Low, Timothy Chen, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03984v1.pdf)  
  Keywords: gaussian splatting, dynamic, ar, 3d gaussian, efficient, high-fidelity  
- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115v1)**  
  Authors: Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03115v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 4d, dynamic, face, ar, efficient  
- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: gaussian splatting, avatar, human, real-time rendering, geometry, dynamic, nerf, fast, ar, 3d gaussian, high-fidelity  
- **[Vid2Avatar-Pro: Authentic Avatar from Videos in the Wild via Universal Prior](https://arxiv.org/abs/2503.01610v1)**  
  Authors: Chen Guo, Junxuan Li, Yash Kant, Yaser Sheikh, Shunsuke Saito, Chen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01610v1.pdf)  
  Keywords: avatar, human, motion, ar, 3d gaussian, animation  
- **[Vid2Fluid: 3D Dynamic Fluid Assets from Single-View Videos with Generative Gaussian Splatting](https://arxiv.org/abs/2503.00868v1)**  
  Authors: Zhiwei Zhao, Alan Zhao, Minchen Li, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00868v1.pdf)  
  Keywords: gaussian splatting, geometry, dynamic, face, ar, 3d gaussian  
- **[PSRGS:Progressive Spectral Residual of 3D Gaussian for High-Frequency Recovery](https://arxiv.org/abs/2503.00848v1)**  
  Authors: BoCheng Li, WenJuan Zhang, Bing Zhang, YiLing Yao, YaNing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00848v1.pdf)  
  Keywords: gaussian splatting, motion, geometry, face, ar, 3d gaussian  
- **[Scalable Real2Sim: Physics-Aware Asset Generation Via Robotic Pick-and-Place Setups](https://arxiv.org/abs/2503.00370v1)**  
  Authors: Nicholas Pfaff, Evelyn Fu, Jeremy Binagia, Phillip Isola, Russ Tedrake  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00370v1.pdf)  
  Keywords: gaussian splatting, geometry, dynamic, nerf, ar, efficient  

### Few-shot

*Showing the latest 50 out of 97 papers*

- **[S2Gaussian: Sparse-View Super-Resolution 3D Gaussian Splatting](https://arxiv.org/abs/2503.04314v1)**  
  Authors: Yecong Wan, Mingwen Shao, Yuanshuo Cheng, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04314v1.pdf)  
  Keywords: gaussian splatting, geometry, sparse view, ar, sparse-view, 3d gaussian  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: gaussian splatting, human, neural rendering, few-shot, semantic, nerf, ar, efficient  
- **[Seeing A 3D World in A Grain of Sand](https://arxiv.org/abs/2503.00260v1)**  
  Authors: Yufan Zhang, Yu Ji, Yu Guo, Jinwei Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00260v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, sparse view, face, ar, 3d gaussian  
- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: gaussian splatting, 3d reconstruction, sparse view, ar, 3d gaussian, efficient, high-fidelity  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: gaussian splatting, tracking, real-time rendering, geometry, nerf, slam, mapping, ar, sparse-view  
- **[DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform](https://arxiv.org/abs/2501.12637v2)**  
  Authors: Hung Nguyen, Blark Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12637v2.pdf)  
  Keywords: head, few-shot, ar, nerf, fast  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: gaussian splatting, 4d, ar, sparse-view, 3d gaussian, semantic  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, nerf, ar, sparse-view, 3d gaussian, efficient  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: gaussian splatting, human, sparse view, dynamic, lighting, face, nerf, medical, ar  
- **[Synthetic Prior for Few-Shot Drivable Head Avatar Inversion](https://arxiv.org/abs/2501.06903v1)**  
  Authors: Wojciech Zielonka, Stephan J. Garbin, Alexandros Lattas, George Kopanas, Paulo Gotardo, Thabo Beeler, Justus Thies, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06903v1.pdf)  
  Keywords: gaussian splatting, head, avatar, few-shot, ar, 3d gaussian  

### Geometry Reconstruction

*Showing the latest 50 out of 461 papers*

- **[S2Gaussian: Sparse-View Super-Resolution 3D Gaussian Splatting](https://arxiv.org/abs/2503.04314v1)**  
  Authors: Yecong Wan, Mingwen Shao, Yuanshuo Cheng, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04314v1.pdf)  
  Keywords: gaussian splatting, geometry, sparse view, ar, sparse-view, 3d gaussian  
- **[Instrument-Splatting: Controllable Photorealistic Reconstruction of Surgical Instruments Using Gaussian Splatting](https://arxiv.org/abs/2503.04082v1)**  
  Authors: Shuojue Yang, Zijian Wu, Mingxuan Hong, Qian Li, Daiyun Shen, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04082v1.pdf)  
  Keywords: gaussian splatting, tracking, 3d reconstruction, geometry, ar, 3d gaussian, semantic  
- **[Surgical Gaussian Surfels: Highly Accurate Real-time Surgical Scene Rendering](https://arxiv.org/abs/2503.04079v1)**  
  Authors: Idris O. Sunmola, Zhenjun Zhao, Samuel Schmidgall, Yumeng Wang, Paul Maria Scheikl, Axel Krieger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04079v1.pdf) | [![GitHub](https://img.shields.io/github/stars/aloma85/SurgicalGaussianSurfels?style=social)](https://github.com/aloma85/SurgicalGaussianSurfels)  
  Keywords: real-time rendering, geometry, motion, lightweight, face, nerf, ar, efficient, 3d gaussian, deformation  
- **[Beyond Existance: Fulfill 3D Reconstructed Scenes with Pseudo Details](https://arxiv.org/abs/2503.04037v1)**  
  Authors: Yifei Gao, Jun Huang, Lei Wang, Ruiting Dai, Jun Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04037v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, ar, fast, 3d gaussian  
- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115v1)**  
  Authors: Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03115v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 4d, dynamic, face, ar, efficient  
- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: gaussian splatting, avatar, human, real-time rendering, geometry, dynamic, nerf, fast, ar, 3d gaussian, high-fidelity  
- **[Morpheus: Text-Driven 3D Gaussian Splat Shape and Color Stylization](https://arxiv.org/abs/2503.02009v1)**  
  Authors: Jamie Wynn, Zawar Qureshi, Jakub Powierza, Jamie Watson, Mohamed Sayed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02009v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, geometry  
- **[Difix3D+: Improving 3D Reconstructions with Single-Step Diffusion Models](https://arxiv.org/abs/2503.01774v1)**  
  Authors: Jay Zhangjie Wu, Yuxuan Zhang, Haithem Turki, Xuanchi Ren, Jun Gao, Mike Zheng Shou, Sanja Fidler, Zan Gojcic, Huan Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01774v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, ar, nerf, 3d gaussian  
- **[Evolving High-Quality Rendering and Reconstruction in a Unified Framework with Contribution-Adaptive Regularization](https://arxiv.org/abs/2503.00881v1)**  
  Authors: You Shen, Zhipeng Zhang, Xinyang Li, Yansong Qu, Yu Lin, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00881v1.pdf)  
  Keywords: gaussian splatting, geometry, compact, face, ar, fast, 3d gaussian  
- **[Vid2Fluid: 3D Dynamic Fluid Assets from Single-View Videos with Generative Gaussian Splatting](https://arxiv.org/abs/2503.00868v1)**  
  Authors: Zhiwei Zhao, Alan Zhao, Minchen Li, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00868v1.pdf)  
  Keywords: gaussian splatting, geometry, dynamic, face, ar, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 75 papers*

- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: gaussian splatting, ar, semantic, outdoor  
- **[OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation](https://arxiv.org/abs/2502.18041v3)**  
  Authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.18041v3.pdf)  
  Keywords: gaussian splatting, ar, outdoor, segmentation, 3d gaussian, semantic  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: gaussian splatting, tracking, geometry, slam, outdoor, mapping, ar, 3d gaussian, high-fidelity  
- **[RadSplatter: Extending 3D Gaussian Splatting to Radio Frequencies for Wireless Radiomap Extrapolation](https://arxiv.org/abs/2502.12686v1)**  
  Authors: Yiheng Wang, Ye Xue, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.12686v1.pdf)  
  Keywords: gaussian splatting, autonomous driving, ar, outdoor, 3d gaussian, efficient  
- **[GS-GVINS: A Tightly-integrated GNSS-Visual-Inertial Navigation System Augmented by 3D Gaussian Splatting](https://arxiv.org/abs/2502.10975v1)**  
  Authors: Zelin Zhou, Saurav Uprety, Shichuang Nie, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10975v1.pdf)  
  Keywords: gaussian splatting, tracking, motion, dynamic, slam, outdoor, ar, 3d gaussian  
- **[PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression](https://arxiv.org/abs/2502.04843v2)**  
  Authors: Feifei Li, Qi Song, Chi Zhang, Hui Shuai, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04843v2.pdf)  
  Keywords: gaussian splatting, ar, nerf, outdoor  
- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: gaussian splatting, ar, outdoor, 3d gaussian, efficient  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: gaussian splatting, geometry, dynamic, localization, nerf, outdoor, slam, mapping, ar, large scene  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: real-time rendering, motion, dynamic, ar, outdoor, 3d gaussian, understanding  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: gaussian splatting, neural rendering, nerf, outdoor, slam, mapping, ar, 3d gaussian, efficient  

### Model Compression

*Showing the latest 50 out of 529 papers*

- **[GaussianVideo: Efficient Video Representation and Compression by Gaussian Splatting](https://arxiv.org/abs/2503.04333v1)**  
  Authors: Inseo Lee, Youngyoon Choi, Joonseok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04333v1.pdf)  
  Keywords: compression, gaussian splatting, dynamic, lightweight, ar, fast, efficient  
- **[Surgical Gaussian Surfels: Highly Accurate Real-time Surgical Scene Rendering](https://arxiv.org/abs/2503.04079v1)**  
  Authors: Idris O. Sunmola, Zhenjun Zhao, Samuel Schmidgall, Yumeng Wang, Paul Maria Scheikl, Axel Krieger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04079v1.pdf) | [![GitHub](https://img.shields.io/github/stars/aloma85/SurgicalGaussianSurfels?style=social)](https://github.com/aloma85/SurgicalGaussianSurfels)  
  Keywords: real-time rendering, geometry, motion, lightweight, face, nerf, ar, efficient, 3d gaussian, deformation  
- **[GaussianGraph: 3D Gaussian-based Scene Graph Generation for Open-world Scene Understanding](https://arxiv.org/abs/2503.04034v1)**  
  Authors: Xihan Wang, Dianyi Yang, Yu Gao, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04034v1.pdf)  
  Keywords: compression, gaussian splatting, dynamic, ar, segmentation, 3d gaussian, semantic, understanding  
- **[GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2503.03984v1)**  
  Authors: Qianzhong Chen, Jiankai Sun, Naixiang Gao, JunEn Low, Timothy Chen, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03984v1.pdf)  
  Keywords: gaussian splatting, dynamic, ar, 3d gaussian, efficient, high-fidelity  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: gaussian splatting, human, neural rendering, few-shot, semantic, nerf, ar, efficient  
- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115v1)**  
  Authors: Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03115v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 4d, dynamic, face, ar, efficient  
- **[FGS-SLAM: Fourier-based Gaussian Splatting for Real-time SLAM with Sparse and Dense Map Fusion](https://arxiv.org/abs/2503.01109v1)**  
  Authors: Yansong Xu, Junlin Li, Wei Zhang, Siyu Chen, Shengyong Zhang, Yuquan Leng, Weijia Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01109v1.pdf)  
  Keywords: gaussian splatting, tracking, localization, slam, mapping, ar, 3d gaussian, efficient, high-fidelity  
- **[Evolving High-Quality Rendering and Reconstruction in a Unified Framework with Contribution-Adaptive Regularization](https://arxiv.org/abs/2503.00881v1)**  
  Authors: You Shen, Zhipeng Zhang, Xinyang Li, Yansong Qu, Yu Lin, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00881v1.pdf)  
  Keywords: gaussian splatting, geometry, compact, face, ar, fast, 3d gaussian  
- **[Scalable Real2Sim: Physics-Aware Asset Generation Via Robotic Pick-and-Place Setups](https://arxiv.org/abs/2503.00370v1)**  
  Authors: Nicholas Pfaff, Evelyn Fu, Jeremy Binagia, Phillip Isola, Russ Tedrake  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00370v1.pdf)  
  Keywords: gaussian splatting, geometry, dynamic, nerf, ar, efficient  
- **[CAT-3DGS: A Context-Adaptive Triplane Approach to Rate-Distortion-Optimized 3DGS Compression](https://arxiv.org/abs/2503.00357v1)**  
  Authors: Yu-Ting Zhan, Cheng-Yuan Ho, Hebi Yang, Yi-Hsin Chen, Jui Chiu Chiang, Yu-Lun Liu, Wen-Hsiao Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00357v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, compression  

### Quality Enhancement

*Showing the latest 50 out of 224 papers*

- **[GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2503.03984v1)**  
  Authors: Qianzhong Chen, Jiankai Sun, Naixiang Gao, JunEn Low, Timothy Chen, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03984v1.pdf)  
  Keywords: gaussian splatting, dynamic, ar, 3d gaussian, efficient, high-fidelity  
- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: gaussian splatting, avatar, human, real-time rendering, geometry, dynamic, nerf, fast, ar, 3d gaussian, high-fidelity  
- **[DQO-MAP: Dual Quadrics Multi-Object mapping with Gaussian Splatting](https://arxiv.org/abs/2503.02223v1)**  
  Authors: Haoyuan Li, Ziqin Ye, Yue Hao, Weiyang Lin, Chao Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LiHaoy-ux/DQO-MAP?style=social)](https://github.com/LiHaoy-ux/DQO-MAP)  
  Keywords: gaussian splatting, slam, mapping, ar, 3d gaussian, high-fidelity  
- **[FGS-SLAM: Fourier-based Gaussian Splatting for Real-time SLAM with Sparse and Dense Map Fusion](https://arxiv.org/abs/2503.01109v1)**  
  Authors: Yansong Xu, Junlin Li, Wei Zhang, Siyu Chen, Shengyong Zhang, Yuquan Leng, Weijia Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01109v1.pdf)  
  Keywords: gaussian splatting, tracking, localization, slam, mapping, ar, 3d gaussian, efficient, high-fidelity  
- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: gaussian splatting, 3d reconstruction, sparse view, ar, 3d gaussian, efficient, high-fidelity  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: gaussian splatting, tracking, geometry, slam, outdoor, mapping, ar, 3d gaussian, high-fidelity  
- **[DynamicGSG: Dynamic 3D Gaussian Scene Graphs for Environment Adaptation](https://arxiv.org/abs/2502.15309v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Zhuo Yang, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15309v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GeLuzhou/Dynamic-GSG?style=social)](https://github.com/GeLuzhou/Dynamic-GSG)  
  Keywords: gaussian splatting, human, dynamic, ar, segmentation, 3d gaussian, semantic, high-fidelity  
- **[GS-Cache: A GS-Cache Inference Framework for Large-scale Gaussian Splatting Models](https://arxiv.org/abs/2502.14938v1)**  
  Authors: Miao Tao, Yuanzhen Zhou, Haoran Xu, Zeyu He, Zhenyu Yang, Yuchang Zhang, Zhongling Su, Linning Xu, Zhenxiang Ma, Rong Fu, Hengjie Li, Xingcheng Zhang, Jidong Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14938v1.pdf)  
  Keywords: gaussian splatting, vr, neural rendering, face, ar, 3d gaussian, efficient, high-fidelity  
- **[SIREN: Semantic, Initialization-Free Registration of Multi-Robot Gaussian Splatting Maps](https://arxiv.org/abs/2502.06519v1)**  
  Authors: Ola Shorinwa, Jiankai Sun, Mac Schwager, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.06519v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, semantic, high-fidelity  
- **[PINGS: Gaussian Splatting Meets Distance Fields within a Point-Based Implicit Neural Map](https://arxiv.org/abs/2502.05752v1)**  
  Authors: Yue Pan, Xingguang Zhong, Liren Jin, Louis Wiesmann, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05752v1.pdf)  
  Keywords: gaussian splatting, high quality, compact, slam, mapping, ar, high-fidelity  

### Ray Tracing

- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: tracking, relightable, real-time rendering, ray tracing, geometry, dynamic, 4d, lighting, face, ar, efficient  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: gaussian splatting, shadow, ray tracing, reflection, lighting, face  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, ray tracing, survey, ar, 3d gaussian  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: gaussian splatting, ray tracing, reflection, light transport, ar, acceleration, efficient  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: gaussian splatting, shadow, ray tracing, reflection, ar, 3d gaussian  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: gaussian splatting, ray tracing, reflection, lighting, ar, efficient, relighting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, ray tracing, reflection, lighting, ar, 3d gaussian, efficient, high-fidelity  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: gaussian splatting, global illumination, geometry, illumination, face, nerf, fast, mapping, ar, efficient  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v2)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v2.pdf)  
  Keywords: gaussian splatting, ray tracing, ar, 3d gaussian, efficient  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: 3d gaussian, gaussian splatting, ar, ray tracing  

### Relighting

*Showing the latest 50 out of 154 papers*

- **[EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering](https://arxiv.org/abs/2502.20669v1)**  
  Authors: John J. Han, Jie Ying Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20669v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, geometry, lighting, face, medical, ar, 3d gaussian  
- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941v1)**  
  Authors: Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16941v1.pdf)  
  Keywords: 4d, lighting, ar, nerf, efficient  
- **[RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection](https://arxiv.org/abs/2502.13071v1)**  
  Authors: Jingtong Yue, Zhiwei Lin, Xin Lin, Xiaoyu Zhou, Xiangtai Li, Lu Qi, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13071v1.pdf)  
  Keywords: 3d gaussian, lighting, ar, face  
- **[OMG: Opacity Matters in Material Modeling with Gaussian Splatting](https://arxiv.org/abs/2502.10988v2)**  
  Authors: Silong Yong, Venkata Nagarjun Pudureddiyur Manivannan, Bernhard Kerbl, Zifu Wan, Simon Stepputtis, Katia Sycara, Yaqi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10988v2.pdf)  
  Keywords: gaussian splatting, neural rendering, real-time rendering, geometry, lighting, ar, 3d gaussian  
- **[E-3DGS: Event-Based Novel View Rendering of Large-Scale Scenes Using 3D Gaussian Splatting](https://arxiv.org/abs/2502.10827v1)**  
  Authors: Sohaib Zahid, Viktor Rudnev, Eddy Ilg, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10827v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, lighting, nerf, fast, ar, 3d gaussian  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: tracking, relightable, real-time rendering, ray tracing, geometry, dynamic, 4d, lighting, face, ar, efficient  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: gaussian splatting, shadow, ray tracing, reflection, lighting, face  
- **[TranSplat: Surface Embedding-guided 3D Gaussian Splatting for Transparent Object Manipulation](https://arxiv.org/abs/2502.07840v1)**  
  Authors: Jeongyun Kim, Jeongho Noh, Dong-Guw Lee, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07840v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://github.)  
  Keywords: gaussian splatting, robotics, lighting, face, ar, 3d gaussian  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: gaussian splatting, 4d, motion, dynamic, lighting, survey, nerf, ar, deformation  
- **[GaussRender: Learning 3D Occupancy with Gaussian Rendering](https://arxiv.org/abs/2502.05040v1)**  
  Authors: Loick Chambon, Eloi Zablocki, Alexandre Boulch, Mickael Chen, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05040v1.pdf) | [![GitHub](https://img.shields.io/github/stars/valeoai/GaussRender?style=social)](https://github.com/valeoai/GaussRender)  
  Keywords: gaussian splatting, geometry, lighting, ar, efficient, semantic, understanding  

### SLAM

*Showing the latest 50 out of 209 papers*

- **[Instrument-Splatting: Controllable Photorealistic Reconstruction of Surgical Instruments Using Gaussian Splatting](https://arxiv.org/abs/2503.04082v1)**  
  Authors: Shuojue Yang, Zijian Wu, Mingxuan Hong, Qian Li, Daiyun Shen, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04082v1.pdf)  
  Keywords: gaussian splatting, tracking, 3d reconstruction, geometry, ar, 3d gaussian, semantic  
- **[Direct Sparse Odometry with Continuous 3D Gaussian Maps for Indoor Environments](https://arxiv.org/abs/2503.03373v1)**  
  Authors: Jie Deng, Fengtian Lang, Zikang Yuan, Xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03373v1.pdf)  
  Keywords: tracking, robotics, localization, ar, 3d gaussian  
- **[DQO-MAP: Dual Quadrics Multi-Object mapping with Gaussian Splatting](https://arxiv.org/abs/2503.02223v1)**  
  Authors: Haoyuan Li, Ziqin Ye, Yue Hao, Weiyang Lin, Chao Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LiHaoy-ux/DQO-MAP?style=social)](https://github.com/LiHaoy-ux/DQO-MAP)  
  Keywords: gaussian splatting, slam, mapping, ar, 3d gaussian, high-fidelity  
- **[OpenGS-SLAM: Open-Set Dense Semantic SLAM with 3D Gaussian Splatting for Object-Level Scene Understanding](https://arxiv.org/abs/2503.01646v1)**  
  Authors: Dianyi Yang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01646v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://young-bit.github.io/opengs-github.github.io/.)  
  Keywords: gaussian splatting, tracking, slam, fast, segmentation, mapping, ar, 3d gaussian, semantic, understanding  
- **[FGS-SLAM: Fourier-based Gaussian Splatting for Real-time SLAM with Sparse and Dense Map Fusion](https://arxiv.org/abs/2503.01109v1)**  
  Authors: Yansong Xu, Junlin Li, Wei Zhang, Siyu Chen, Shengyong Zhang, Yuquan Leng, Weijia Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01109v1.pdf)  
  Keywords: gaussian splatting, tracking, localization, slam, mapping, ar, 3d gaussian, efficient, high-fidelity  
- **[Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration](https://arxiv.org/abs/2502.16652v1)**  
  Authors: Kim Jun-Seong, GeonU Kim, Kim Yu-Ji, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16652v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drsplat.github.io/)  
  Keywords: gaussian splatting, compact, localization, ar, segmentation, 3d gaussian, semantic, understanding  
- **[Dragen3D: Multiview Geometry Consistent 3D Gaussian Generation with Drag-Based Control](https://arxiv.org/abs/2502.16475v1)**  
  Authors: Jinbo Yan, Alan Zhao, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16475v1.pdf)  
  Keywords: gaussian splatting, geometry, face, mapping, ar, 3d gaussian, efficient  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: gaussian splatting, tracking, geometry, slam, outdoor, mapping, ar, 3d gaussian, high-fidelity  
- **[Hier-SLAM++: Neuro-Symbolic Semantic SLAM with a Hierarchically Categorical Gaussian Splatting](https://arxiv.org/abs/2502.14931v1)**  
  Authors: Boying Li, Vuong Chi Hao, Peter J. Stuckey, Ian Reid, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14931v1.pdf)  
  Keywords: gaussian splatting, compact, nerf, slam, mapping, ar, 3d gaussian, semantic, understanding  
- **[3D Gaussian Splatting aided Localization for Large and Complex Indoor-Environments](https://arxiv.org/abs/2502.13803v1)**  
  Authors: Vincent Ress, Jonas Meyer, Wei Zhang, David Skuddis, Uwe Soergel, Norbert Haala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13803v1.pdf)  
  Keywords: gaussian splatting, geometry, localization, slam, ar, 3d gaussian  

### Scene Understanding

*Showing the latest 50 out of 243 papers*

- **[Instrument-Splatting: Controllable Photorealistic Reconstruction of Surgical Instruments Using Gaussian Splatting](https://arxiv.org/abs/2503.04082v1)**  
  Authors: Shuojue Yang, Zijian Wu, Mingxuan Hong, Qian Li, Daiyun Shen, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04082v1.pdf)  
  Keywords: gaussian splatting, tracking, 3d reconstruction, geometry, ar, 3d gaussian, semantic  
- **[GaussianGraph: 3D Gaussian-based Scene Graph Generation for Open-world Scene Understanding](https://arxiv.org/abs/2503.04034v1)**  
  Authors: Xihan Wang, Dianyi Yang, Yu Gao, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04034v1.pdf)  
  Keywords: compression, gaussian splatting, dynamic, ar, segmentation, 3d gaussian, semantic, understanding  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: gaussian splatting, human, neural rendering, few-shot, semantic, nerf, ar, efficient  
- **[OpenGS-SLAM: Open-Set Dense Semantic SLAM with 3D Gaussian Splatting for Object-Level Scene Understanding](https://arxiv.org/abs/2503.01646v1)**  
  Authors: Dianyi Yang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01646v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://young-bit.github.io/opengs-github.github.io/.)  
  Keywords: gaussian splatting, tracking, slam, fast, segmentation, mapping, ar, 3d gaussian, semantic, understanding  
- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: gaussian splatting, ar, semantic, outdoor  
- **[Open-Vocabulary Semantic Part Segmentation of 3D Human](https://arxiv.org/abs/2502.19782v1)**  
  Authors: Keito Suzuki, Bang Du, Girish Krishnan, Kunyao Chen, Runfa Blark Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19782v1.pdf)  
  Keywords: gaussian splatting, human, vr, ar, segmentation, 3d gaussian, semantic  
- **[OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation](https://arxiv.org/abs/2502.18041v3)**  
  Authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.18041v3.pdf)  
  Keywords: gaussian splatting, ar, outdoor, segmentation, 3d gaussian, semantic  
- **[UniGS: Unified Language-Image-3D Pretraining with Gaussian Splatting](https://arxiv.org/abs/2502.17860v2)**  
  Authors: Haoyuan Li, Yanpeng Zhou, Tao Tang, Jifei Song, Yihan Zeng, Michael Kampffmeyer, Hang Xu, Xiaodan Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17860v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, understanding  
- **[GS-TransUNet: Integrated 2D Gaussian Splatting and Transformer UNet for Accurate Skin Lesion Analysis](https://arxiv.org/abs/2502.16748v1)**  
  Authors: Anand Kumar, Kavinder Roghit Kanthen, Josna John  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16748v1.pdf)  
  Keywords: gaussian splatting, medical, ar, fast, segmentation, efficient  
- **[Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration](https://arxiv.org/abs/2502.16652v1)**  
  Authors: Kim Jun-Seong, GeonU Kim, Kim Yu-Ji, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16652v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drsplat.github.io/)  
  Keywords: gaussian splatting, compact, localization, ar, segmentation, 3d gaussian, semantic, understanding  



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