# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-03-07 00:48:57

## Categories

- [3DGS Surveys](#3dgs-surveys) (23 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (392 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1382 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (464 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (510 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (95 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (457 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (75 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (524 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (223 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (33 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (154 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (208 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (240 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: nerf, survey, real-time rendering, compression, 3d reconstruction, ar, efficient, gaussian splatting, 3d gaussian  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: nerf, survey, lighting, dynamic, 4d, motion, ar, deformation, gaussian splatting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, ar, gaussian splatting, ray tracing, 3d gaussian  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: survey, face, lighting, tracking, outdoor, ar, geometry, reflection, mapping, slam, dynamic, 3d gaussian, localization  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: survey, illumination, ar, recognition, gaussian splatting, 3d gaussian  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: nerf, survey, lighting, robotics, 3d reconstruction, dynamic, semantic, ar, geometry, autonomous driving, gaussian splatting, compact, high-fidelity  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: nerf, survey, real-time rendering, robotics, understanding, ar, gaussian splatting, 3d gaussian  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: nerf, survey, lighting, ar, gaussian splatting, 3d gaussian, high-fidelity  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: nerf, survey, robotics, 3d reconstruction, ar, autonomous driving, gaussian splatting, 3d gaussian, vr  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: ar, survey, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 392 papers*

- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: human, nerf, real-time rendering, fast, dynamic, ar, geometry, avatar, gaussian splatting, 3d gaussian, high-fidelity  
- **[OpenGS-SLAM: Open-Set Dense Semantic SLAM with 3D Gaussian Splatting for Object-Level Scene Understanding](https://arxiv.org/abs/2503.01646v1)**  
  Authors: Dianyi Yang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01646v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://young-bit.github.io/opengs-github.github.io/.)  
  Keywords: segmentation, tracking, fast, understanding, ar, mapping, slam, gaussian splatting, 3d gaussian, semantic  
- **[Evolving High-Quality Rendering and Reconstruction in a Unified Framework with Contribution-Adaptive Regularization](https://arxiv.org/abs/2503.00881v1)**  
  Authors: You Shen, Zhipeng Zhang, Xinyang Li, Yansong Qu, Yu Lin, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00881v1.pdf)  
  Keywords: face, 3d gaussian, fast, ar, geometry, gaussian splatting, compact  
- **[InsTaG: Learning Personalized 3D Talking Head from Few-Second Video](https://arxiv.org/abs/2502.20387v1)**  
  Authors: Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Jun Zhou, Lin Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20387v1.pdf)  
  Keywords: head, fast, motion, ar, lightweight, dynamic  
- **[Does 3D Gaussian Splatting Need Accurate Volumetric Rendering?](https://arxiv.org/abs/2502.19318v1)**  
  Authors: Adam Celarek, George Kopanas, George Drettakis, Michael Wimmer, Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19318v1.pdf)  
  Keywords: nerf, fast, ar, efficient, gaussian splatting, 3d gaussian  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: nerf, survey, real-time rendering, compression, 3d reconstruction, ar, efficient, gaussian splatting, 3d gaussian  
- **[GaussianFlowOcc: Sparse and Weakly Supervised Occupancy Estimation using Gaussian Splatting and Temporal Flow](https://arxiv.org/abs/2502.17288v2)**  
  Authors: Simon Boeder, Fabian Gigengack, Benjamin Risse  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17288v2.pdf)  
  Keywords: fast, dynamic, ar, efficient, autonomous driving, gaussian splatting, 3d gaussian  
- **[GS-TransUNet: Integrated 2D Gaussian Splatting and Transformer UNet for Accurate Skin Lesion Analysis](https://arxiv.org/abs/2502.16748v1)**  
  Authors: Anand Kumar, Kavinder Roghit Kanthen, Josna John  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16748v1.pdf)  
  Keywords: segmentation, fast, ar, efficient, medical, gaussian splatting  
- **[GS-QA: Comprehensive Quality Assessment Benchmark for Gaussian Splatting View Synthesis](https://arxiv.org/abs/2502.13196v1)**  
  Authors: Pedro Martin, António Rodrigues, João Ascenso, Maria Paula Queluz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13196v1.pdf)  
  Keywords: human, nerf, fast, ar, geometry, gaussian splatting, 3d gaussian  
- **[GaussianMotion: End-to-End Learning of Animatable Gaussian Avatars with Pose Guidance from Text](https://arxiv.org/abs/2502.11642v1)**  
  Authors: Gyumin Shim, Sangmin Lee, Jaegul Choo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.11642v1.pdf)  
  Keywords: human, face, motion, ar, efficient, avatar, efficient rendering, gaussian splatting, 3d gaussian  

### Applications

*Showing the latest 50 out of 1382 papers*

- **[Direct Sparse Odometry with Continuous 3D Gaussian Maps for Indoor Environments](https://arxiv.org/abs/2503.03373v1)**  
  Authors: Jie Deng, Fengtian Lang, Zikang Yuan, Xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03373v1.pdf)  
  Keywords: tracking, robotics, ar, 3d gaussian, localization  
- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115v1)**  
  Authors: Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03115v1.pdf)  
  Keywords: face, 3d reconstruction, dynamic, 4d, ar, efficient, gaussian splatting  
- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: human, nerf, real-time rendering, fast, dynamic, ar, geometry, avatar, gaussian splatting, 3d gaussian, high-fidelity  
- **[DQO-MAP: Dual Quadrics Multi-Object mapping with Gaussian Splatting](https://arxiv.org/abs/2503.02223v1)**  
  Authors: Haoyuan Li, Ziqin Ye, Yue Hao, Weiyang Lin, Chao Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LiHaoy-ux/DQO-MAP?style=social)](https://github.com/LiHaoy-ux/DQO-MAP)  
  Keywords: ar, mapping, slam, gaussian splatting, 3d gaussian, high-fidelity  
- **[Morpheus: Text-Driven 3D Gaussian Splat Shape and Color Stylization](https://arxiv.org/abs/2503.02009v1)**  
  Authors: Jamie Wynn, Zawar Qureshi, Jakub Powierza, Jamie Watson, Mohamed Sayed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02009v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry  
- **[Difix3D+: Improving 3D Reconstructions with Single-Step Diffusion Models](https://arxiv.org/abs/2503.01774v1)**  
  Authors: Jay Zhangjie Wu, Yuxuan Zhang, Haithem Turki, Xuanchi Ren, Jun Gao, Mike Zheng Shou, Sanja Fidler, Zan Gojcic, Huan Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01774v1.pdf)  
  Keywords: nerf, 3d reconstruction, ar, gaussian splatting, 3d gaussian  
- **[OpenGS-SLAM: Open-Set Dense Semantic SLAM with 3D Gaussian Splatting for Object-Level Scene Understanding](https://arxiv.org/abs/2503.01646v1)**  
  Authors: Dianyi Yang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01646v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://young-bit.github.io/opengs-github.github.io/.)  
  Keywords: segmentation, tracking, fast, understanding, ar, mapping, slam, gaussian splatting, 3d gaussian, semantic  
- **[Vid2Avatar-Pro: Authentic Avatar from Videos in the Wild via Universal Prior](https://arxiv.org/abs/2503.01610v1)**  
  Authors: Chen Guo, Junxuan Li, Yash Kant, Yaser Sheikh, Shunsuke Saito, Chen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01610v1.pdf)  
  Keywords: human, motion, ar, avatar, 3d gaussian, animation  
- **[LiteGS: A High-Performance Modular Framework for Gaussian Splatting Training](https://arxiv.org/abs/2503.01199v1)**  
  Authors: Kaimin Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01199v1.pdf)  
  Keywords: nerf, face, head, ar, gaussian splatting  
- **[FGS-SLAM: Fourier-based Gaussian Splatting for Real-time SLAM with Sparse and Dense Map Fusion](https://arxiv.org/abs/2503.01109v1)**  
  Authors: Yansong Xu, Junlin Li, Wei Zhang, Siyu Chen, Shengyong Zhang, Yuquan Leng, Weijia Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01109v1.pdf)  
  Keywords: tracking, ar, efficient, mapping, slam, gaussian splatting, 3d gaussian, high-fidelity, localization  

### Avatar Generation

*Showing the latest 50 out of 464 papers*

- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115v1)**  
  Authors: Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03115v1.pdf)  
  Keywords: face, 3d reconstruction, dynamic, 4d, ar, efficient, gaussian splatting  
- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: human, nerf, real-time rendering, fast, dynamic, ar, geometry, avatar, gaussian splatting, 3d gaussian, high-fidelity  
- **[Vid2Avatar-Pro: Authentic Avatar from Videos in the Wild via Universal Prior](https://arxiv.org/abs/2503.01610v1)**  
  Authors: Chen Guo, Junxuan Li, Yash Kant, Yaser Sheikh, Shunsuke Saito, Chen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01610v1.pdf)  
  Keywords: human, motion, ar, avatar, 3d gaussian, animation  
- **[LiteGS: A High-Performance Modular Framework for Gaussian Splatting Training](https://arxiv.org/abs/2503.01199v1)**  
  Authors: Kaimin Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01199v1.pdf)  
  Keywords: nerf, face, head, ar, gaussian splatting  
- **[Evolving High-Quality Rendering and Reconstruction in a Unified Framework with Contribution-Adaptive Regularization](https://arxiv.org/abs/2503.00881v1)**  
  Authors: You Shen, Zhipeng Zhang, Xinyang Li, Yansong Qu, Yu Lin, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00881v1.pdf)  
  Keywords: face, 3d gaussian, fast, ar, geometry, gaussian splatting, compact  
- **[Vid2Fluid: 3D Dynamic Fluid Assets from Single-View Videos with Generative Gaussian Splatting](https://arxiv.org/abs/2503.00868v1)**  
  Authors: Zhiwei Zhao, Alan Zhao, Minchen Li, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00868v1.pdf)  
  Keywords: face, dynamic, ar, geometry, gaussian splatting, 3d gaussian  
- **[PSRGS:Progressive Spectral Residual of 3D Gaussian for High-Frequency Recovery](https://arxiv.org/abs/2503.00848v1)**  
  Authors: BoCheng Li, WenJuan Zhang, Bing Zhang, YiLing Yao, YaNing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00848v1.pdf)  
  Keywords: face, motion, ar, geometry, gaussian splatting, 3d gaussian  
- **[GaussianSeal: Rooting Adaptive Watermarks for 3D Gaussian Generation Model](https://arxiv.org/abs/2503.00531v1)**  
  Authors: Runyi Li, Xuanyu Zhang, Chuhan Tong, Zhipei Xu, Jian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00531v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, head  
- **[Seeing A 3D World in A Grain of Sand](https://arxiv.org/abs/2503.00260v1)**  
  Authors: Yufan Zhang, Yu Ji, Yu Guo, Jinwei Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00260v1.pdf)  
  Keywords: face, sparse view, 3d reconstruction, ar, gaussian splatting, 3d gaussian  
- **[EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering](https://arxiv.org/abs/2502.20669v1)**  
  Authors: John J. Han, Jie Ying Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20669v1.pdf)  
  Keywords: face, lighting, 3d reconstruction, ar, medical, geometry, gaussian splatting, 3d gaussian  

### Dynamic Scene

*Showing the latest 50 out of 510 papers*

- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115v1)**  
  Authors: Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03115v1.pdf)  
  Keywords: face, 3d reconstruction, dynamic, 4d, ar, efficient, gaussian splatting  
- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: human, nerf, real-time rendering, fast, dynamic, ar, geometry, avatar, gaussian splatting, 3d gaussian, high-fidelity  
- **[Vid2Avatar-Pro: Authentic Avatar from Videos in the Wild via Universal Prior](https://arxiv.org/abs/2503.01610v1)**  
  Authors: Chen Guo, Junxuan Li, Yash Kant, Yaser Sheikh, Shunsuke Saito, Chen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01610v1.pdf)  
  Keywords: human, motion, ar, avatar, 3d gaussian, animation  
- **[Vid2Fluid: 3D Dynamic Fluid Assets from Single-View Videos with Generative Gaussian Splatting](https://arxiv.org/abs/2503.00868v1)**  
  Authors: Zhiwei Zhao, Alan Zhao, Minchen Li, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00868v1.pdf)  
  Keywords: face, dynamic, ar, geometry, gaussian splatting, 3d gaussian  
- **[PSRGS:Progressive Spectral Residual of 3D Gaussian for High-Frequency Recovery](https://arxiv.org/abs/2503.00848v1)**  
  Authors: BoCheng Li, WenJuan Zhang, Bing Zhang, YiLing Yao, YaNing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00848v1.pdf)  
  Keywords: face, motion, ar, geometry, gaussian splatting, 3d gaussian  
- **[Scalable Real2Sim: Physics-Aware Asset Generation Via Robotic Pick-and-Place Setups](https://arxiv.org/abs/2503.00370v1)**  
  Authors: Nicholas Pfaff, Evelyn Fu, Jeremy Binagia, Phillip Isola, Russ Tedrake  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00370v1.pdf)  
  Keywords: nerf, dynamic, ar, efficient, geometry, gaussian splatting  
- **[Abstract Rendering: Computing All that is Seen in Gaussian Splat Scenes](https://arxiv.org/abs/2503.00308v2)**  
  Authors: Yangge Li, Chenxi Ji, Xiangru Zhong, Huan Zhang, Sayan Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00308v2.pdf)  
  Keywords: motion, ar, efficient, robotics  
- **[InsTaG: Learning Personalized 3D Talking Head from Few-Second Video](https://arxiv.org/abs/2502.20387v1)**  
  Authors: Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Jun Zhou, Lin Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20387v1.pdf)  
  Keywords: head, fast, motion, ar, lightweight, dynamic  
- **[Efficient Gaussian Splatting for Monocular Dynamic Scene Rendering via Sparse Time-Variant Attribute Modeling](https://arxiv.org/abs/2502.20378v1)**  
  Authors: Hanyang Kong, Xingyi Yang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20378v1.pdf)  
  Keywords: dynamic, motion, ar, efficient, gaussian splatting  
- **[Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting](https://arxiv.org/abs/2502.19459v1)**  
  Authors: Yu Liu, Baoxiong Jia, Ruijie Lu, Junfeng Ni, Song-Chun Zhu, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19459v1.pdf)  
  Keywords: dynamic, ar, efficient, gaussian splatting, 3d gaussian  

### Few-shot

*Showing the latest 50 out of 95 papers*

- **[Seeing A 3D World in A Grain of Sand](https://arxiv.org/abs/2503.00260v1)**  
  Authors: Yufan Zhang, Yu Ji, Yu Guo, Jinwei Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00260v1.pdf)  
  Keywords: face, sparse view, 3d reconstruction, ar, gaussian splatting, 3d gaussian  
- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: sparse view, 3d reconstruction, ar, efficient, gaussian splatting, 3d gaussian, high-fidelity  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: nerf, real-time rendering, tracking, sparse-view, ar, geometry, mapping, slam, gaussian splatting  
- **[DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform](https://arxiv.org/abs/2501.12637v2)**  
  Authors: Hung Nguyen, Blark Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12637v2.pdf)  
  Keywords: nerf, head, fast, ar, few-shot  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: sparse-view, 4d, ar, gaussian splatting, 3d gaussian, semantic  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: nerf, sparse-view, 3d reconstruction, ar, efficient, gaussian splatting, 3d gaussian  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: human, nerf, face, lighting, sparse view, dynamic, ar, medical, gaussian splatting  
- **[Synthetic Prior for Few-Shot Drivable Head Avatar Inversion](https://arxiv.org/abs/2501.06903v1)**  
  Authors: Wojciech Zielonka, Stephan J. Garbin, Alexandros Lattas, George Kopanas, Paulo Gotardo, Thabo Beeler, Justus Thies, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06903v1.pdf)  
  Keywords: head, ar, few-shot, avatar, gaussian splatting, 3d gaussian  
- **[NVS-SQA: Exploring Self-Supervised Quality Representation Learning for Neurally Synthesized Scenes without References](https://arxiv.org/abs/2501.06488v1)**  
  Authors: Qiang Qu, Yiran Shen, Xiaoming Chen, Yuk Ying Chung, Weidong Cai, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06488v1.pdf)  
  Keywords: human, nerf, sparse view, ar, gaussian splatting, 3d gaussian  
- **[FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency](https://arxiv.org/abs/2501.04628v1)**  
  Authors: Han Huang, Yulun Wu, Chao Deng, Ge Gao, Ming Gu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04628v1.pdf)  
  Keywords: face, sparse view, sparse-view, fast, ar, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 457 papers*

- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115v1)**  
  Authors: Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03115v1.pdf)  
  Keywords: face, 3d reconstruction, dynamic, 4d, ar, efficient, gaussian splatting  
- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: human, nerf, real-time rendering, fast, dynamic, ar, geometry, avatar, gaussian splatting, 3d gaussian, high-fidelity  
- **[Morpheus: Text-Driven 3D Gaussian Splat Shape and Color Stylization](https://arxiv.org/abs/2503.02009v1)**  
  Authors: Jamie Wynn, Zawar Qureshi, Jakub Powierza, Jamie Watson, Mohamed Sayed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02009v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry  
- **[Difix3D+: Improving 3D Reconstructions with Single-Step Diffusion Models](https://arxiv.org/abs/2503.01774v1)**  
  Authors: Jay Zhangjie Wu, Yuxuan Zhang, Haithem Turki, Xuanchi Ren, Jun Gao, Mike Zheng Shou, Sanja Fidler, Zan Gojcic, Huan Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01774v1.pdf)  
  Keywords: nerf, 3d reconstruction, ar, gaussian splatting, 3d gaussian  
- **[Evolving High-Quality Rendering and Reconstruction in a Unified Framework with Contribution-Adaptive Regularization](https://arxiv.org/abs/2503.00881v1)**  
  Authors: You Shen, Zhipeng Zhang, Xinyang Li, Yansong Qu, Yu Lin, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00881v1.pdf)  
  Keywords: face, 3d gaussian, fast, ar, geometry, gaussian splatting, compact  
- **[Vid2Fluid: 3D Dynamic Fluid Assets from Single-View Videos with Generative Gaussian Splatting](https://arxiv.org/abs/2503.00868v1)**  
  Authors: Zhiwei Zhao, Alan Zhao, Minchen Li, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00868v1.pdf)  
  Keywords: face, dynamic, ar, geometry, gaussian splatting, 3d gaussian  
- **[PSRGS:Progressive Spectral Residual of 3D Gaussian for High-Frequency Recovery](https://arxiv.org/abs/2503.00848v1)**  
  Authors: BoCheng Li, WenJuan Zhang, Bing Zhang, YiLing Yao, YaNing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00848v1.pdf)  
  Keywords: face, motion, ar, geometry, gaussian splatting, 3d gaussian  
- **[DoF-Gaussian: Controllable Depth-of-Field for 3D Gaussian Splatting](https://arxiv.org/abs/2503.00746v1)**  
  Authors: Liao Shen, Tianqi Liu, Huiqiang Sun, Jiaqi Li, Zhiguo Cao, Wei Li, Chen Change Loy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00746v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dof-gaussian.github.io.)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry  
- **[Enhancing Monocular 3D Scene Completion with Diffusion Model](https://arxiv.org/abs/2503.00726v1)**  
  Authors: Changlin Song, Jiaqi Wang, Liyun Zhu, He Weng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00726v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CharlieSong1999/FlashDreamer?style=social)](https://github.com/CharlieSong1999/FlashDreamer)  
  Keywords: robotics, 3d reconstruction, ar, autonomous driving, gaussian splatting, 3d gaussian  
- **[Scalable Real2Sim: Physics-Aware Asset Generation Via Robotic Pick-and-Place Setups](https://arxiv.org/abs/2503.00370v1)**  
  Authors: Nicholas Pfaff, Evelyn Fu, Jeremy Binagia, Phillip Isola, Russ Tedrake  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00370v1.pdf)  
  Keywords: nerf, dynamic, ar, efficient, geometry, gaussian splatting  

### Large Scene

*Showing the latest 50 out of 75 papers*

- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: ar, gaussian splatting, outdoor, semantic  
- **[OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation](https://arxiv.org/abs/2502.18041v3)**  
  Authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.18041v3.pdf)  
  Keywords: segmentation, outdoor, ar, gaussian splatting, 3d gaussian, semantic  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: tracking, outdoor, ar, geometry, mapping, slam, gaussian splatting, 3d gaussian, high-fidelity  
- **[RadSplatter: Extending 3D Gaussian Splatting to Radio Frequencies for Wireless Radiomap Extrapolation](https://arxiv.org/abs/2502.12686v1)**  
  Authors: Yiheng Wang, Ye Xue, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.12686v1.pdf)  
  Keywords: outdoor, ar, efficient, autonomous driving, gaussian splatting, 3d gaussian  
- **[GS-GVINS: A Tightly-integrated GNSS-Visual-Inertial Navigation System Augmented by 3D Gaussian Splatting](https://arxiv.org/abs/2502.10975v1)**  
  Authors: Zelin Zhou, Saurav Uprety, Shichuang Nie, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10975v1.pdf)  
  Keywords: tracking, dynamic, outdoor, motion, ar, slam, gaussian splatting, 3d gaussian  
- **[PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression](https://arxiv.org/abs/2502.04843v2)**  
  Authors: Feifei Li, Qi Song, Chi Zhang, Hui Shuai, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04843v2.pdf)  
  Keywords: ar, gaussian splatting, nerf, outdoor  
- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: outdoor, ar, efficient, gaussian splatting, 3d gaussian  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: nerf, large scene, dynamic, outdoor, ar, geometry, mapping, slam, gaussian splatting, localization  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: real-time rendering, understanding, outdoor, motion, ar, dynamic, 3d gaussian  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: nerf, outdoor, ar, efficient, neural rendering, mapping, slam, gaussian splatting, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 524 papers*

- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115v1)**  
  Authors: Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03115v1.pdf)  
  Keywords: face, 3d reconstruction, dynamic, 4d, ar, efficient, gaussian splatting  
- **[FGS-SLAM: Fourier-based Gaussian Splatting for Real-time SLAM with Sparse and Dense Map Fusion](https://arxiv.org/abs/2503.01109v1)**  
  Authors: Yansong Xu, Junlin Li, Wei Zhang, Siyu Chen, Shengyong Zhang, Yuquan Leng, Weijia Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01109v1.pdf)  
  Keywords: tracking, ar, efficient, mapping, slam, gaussian splatting, 3d gaussian, high-fidelity, localization  
- **[Evolving High-Quality Rendering and Reconstruction in a Unified Framework with Contribution-Adaptive Regularization](https://arxiv.org/abs/2503.00881v1)**  
  Authors: You Shen, Zhipeng Zhang, Xinyang Li, Yansong Qu, Yu Lin, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00881v1.pdf)  
  Keywords: face, 3d gaussian, fast, ar, geometry, gaussian splatting, compact  
- **[Scalable Real2Sim: Physics-Aware Asset Generation Via Robotic Pick-and-Place Setups](https://arxiv.org/abs/2503.00370v1)**  
  Authors: Nicholas Pfaff, Evelyn Fu, Jeremy Binagia, Phillip Isola, Russ Tedrake  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00370v1.pdf)  
  Keywords: nerf, dynamic, ar, efficient, geometry, gaussian splatting  
- **[CAT-3DGS: A Context-Adaptive Triplane Approach to Rate-Distortion-Optimized 3DGS Compression](https://arxiv.org/abs/2503.00357v1)**  
  Authors: Yu-Ting Zhan, Cheng-Yuan Ho, Hebi Yang, Yi-Hsin Chen, Jui Chiu Chiang, Yu-Lun Liu, Wen-Hsiao Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00357v1.pdf)  
  Keywords: ar, gaussian splatting, compression, 3d gaussian  
- **[Abstract Rendering: Computing All that is Seen in Gaussian Splat Scenes](https://arxiv.org/abs/2503.00308v2)**  
  Authors: Yangge Li, Chenxi Ji, Xiangru Zhong, Huan Zhang, Sayan Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00308v2.pdf)  
  Keywords: motion, ar, efficient, robotics  
- **[FlexDrive: Toward Trajectory Flexibility in Driving Scene Reconstruction and Rendering](https://arxiv.org/abs/2502.21093v2)**  
  Authors: Jingqiu Zhou, Lue Fan, Linjiang Huang, Xiaoyu Shi, Si Liu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.21093v2.pdf)  
  Keywords: ar, gaussian splatting, compact, 3d gaussian  
- **[InsTaG: Learning Personalized 3D Talking Head from Few-Second Video](https://arxiv.org/abs/2502.20387v1)**  
  Authors: Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Jun Zhou, Lin Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20387v1.pdf)  
  Keywords: head, fast, motion, ar, lightweight, dynamic  
- **[Efficient Gaussian Splatting for Monocular Dynamic Scene Rendering via Sparse Time-Variant Attribute Modeling](https://arxiv.org/abs/2502.20378v1)**  
  Authors: Hanyang Kong, Xingyi Yang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20378v1.pdf)  
  Keywords: dynamic, motion, ar, efficient, gaussian splatting  
- **[Does 3D Gaussian Splatting Need Accurate Volumetric Rendering?](https://arxiv.org/abs/2502.19318v1)**  
  Authors: Adam Celarek, George Kopanas, George Drettakis, Michael Wimmer, Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19318v1.pdf)  
  Keywords: nerf, fast, ar, efficient, gaussian splatting, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 223 papers*

- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: human, nerf, real-time rendering, fast, dynamic, ar, geometry, avatar, gaussian splatting, 3d gaussian, high-fidelity  
- **[DQO-MAP: Dual Quadrics Multi-Object mapping with Gaussian Splatting](https://arxiv.org/abs/2503.02223v1)**  
  Authors: Haoyuan Li, Ziqin Ye, Yue Hao, Weiyang Lin, Chao Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LiHaoy-ux/DQO-MAP?style=social)](https://github.com/LiHaoy-ux/DQO-MAP)  
  Keywords: ar, mapping, slam, gaussian splatting, 3d gaussian, high-fidelity  
- **[FGS-SLAM: Fourier-based Gaussian Splatting for Real-time SLAM with Sparse and Dense Map Fusion](https://arxiv.org/abs/2503.01109v1)**  
  Authors: Yansong Xu, Junlin Li, Wei Zhang, Siyu Chen, Shengyong Zhang, Yuquan Leng, Weijia Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01109v1.pdf)  
  Keywords: tracking, ar, efficient, mapping, slam, gaussian splatting, 3d gaussian, high-fidelity, localization  
- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: sparse view, 3d reconstruction, ar, efficient, gaussian splatting, 3d gaussian, high-fidelity  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: tracking, outdoor, ar, geometry, mapping, slam, gaussian splatting, 3d gaussian, high-fidelity  
- **[DynamicGSG: Dynamic 3D Gaussian Scene Graphs for Environment Adaptation](https://arxiv.org/abs/2502.15309v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Zhuo Yang, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15309v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GeLuzhou/Dynamic-GSG?style=social)](https://github.com/GeLuzhou/Dynamic-GSG)  
  Keywords: human, segmentation, dynamic, semantic, ar, gaussian splatting, 3d gaussian, high-fidelity  
- **[GS-Cache: A GS-Cache Inference Framework for Large-scale Gaussian Splatting Models](https://arxiv.org/abs/2502.14938v1)**  
  Authors: Miao Tao, Yuanzhen Zhou, Haoran Xu, Zeyu He, Zhenyu Yang, Yuchang Zhang, Zhongling Su, Linning Xu, Zhenxiang Ma, Rong Fu, Hengjie Li, Xingcheng Zhang, Jidong Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14938v1.pdf)  
  Keywords: face, vr, ar, efficient, neural rendering, gaussian splatting, 3d gaussian, high-fidelity  
- **[SIREN: Semantic, Initialization-Free Registration of Multi-Robot Gaussian Splatting Maps](https://arxiv.org/abs/2502.06519v1)**  
  Authors: Ola Shorinwa, Jiankai Sun, Mac Schwager, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.06519v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, 3d gaussian, semantic  
- **[PINGS: Gaussian Splatting Meets Distance Fields within a Point-Based Implicit Neural Map](https://arxiv.org/abs/2502.05752v1)**  
  Authors: Yue Pan, Xingguang Zhong, Liren Jin, Louis Wiesmann, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05752v1.pdf)  
  Keywords: ar, mapping, slam, gaussian splatting, compact, high-fidelity, high quality  
- **[Seeing World Dynamics in a Nutshell](https://arxiv.org/abs/2502.03465v1)**  
  Authors: Qiuhong Shen, Xuanyu Yi, Mingbao Lin, Hanwang Zhang, Shuicheng Yan, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.03465v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Nut-World/NutWorld?style=social)](https://github.com/Nut-World/NutWorld)  
  Keywords: motion, ar, efficient, dynamic, 3d gaussian, high-fidelity  

### Ray Tracing

- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: face, real-time rendering, lighting, tracking, relightable, 4d, ar, efficient, geometry, dynamic, ray tracing  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: face, lighting, shadow, reflection, gaussian splatting, ray tracing  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, ar, gaussian splatting, ray tracing, 3d gaussian  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: acceleration, ar, efficient, reflection, light transport, gaussian splatting, ray tracing  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: shadow, ar, reflection, gaussian splatting, ray tracing, 3d gaussian  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: lighting, relighting, ar, efficient, reflection, gaussian splatting, ray tracing  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: real-time rendering, lighting, ar, efficient, reflection, gaussian splatting, ray tracing, 3d gaussian, high-fidelity  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: nerf, face, fast, illumination, ar, efficient, geometry, mapping, global illumination, gaussian splatting  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v2)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v2.pdf)  
  Keywords: ar, efficient, gaussian splatting, ray tracing, 3d gaussian  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: ar, gaussian splatting, ray tracing, 3d gaussian  

### Relighting

*Showing the latest 50 out of 154 papers*

- **[EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering](https://arxiv.org/abs/2502.20669v1)**  
  Authors: John J. Han, Jie Ying Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20669v1.pdf)  
  Keywords: face, lighting, 3d reconstruction, ar, medical, geometry, gaussian splatting, 3d gaussian  
- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941v1)**  
  Authors: Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16941v1.pdf)  
  Keywords: nerf, lighting, 4d, ar, efficient  
- **[RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection](https://arxiv.org/abs/2502.13071v1)**  
  Authors: Jingtong Yue, Zhiwei Lin, Xin Lin, Xiaoyu Zhou, Xiangtai Li, Lu Qi, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13071v1.pdf)  
  Keywords: ar, face, lighting, 3d gaussian  
- **[OMG: Opacity Matters in Material Modeling with Gaussian Splatting](https://arxiv.org/abs/2502.10988v2)**  
  Authors: Silong Yong, Venkata Nagarjun Pudureddiyur Manivannan, Bernhard Kerbl, Zifu Wan, Simon Stepputtis, Katia Sycara, Yaqi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10988v2.pdf)  
  Keywords: real-time rendering, lighting, ar, geometry, neural rendering, gaussian splatting, 3d gaussian  
- **[E-3DGS: Event-Based Novel View Rendering of Large-Scale Scenes Using 3D Gaussian Splatting](https://arxiv.org/abs/2502.10827v1)**  
  Authors: Sohaib Zahid, Viktor Rudnev, Eddy Ilg, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10827v1.pdf)  
  Keywords: nerf, lighting, fast, dynamic, motion, ar, gaussian splatting, 3d gaussian  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: face, real-time rendering, lighting, tracking, relightable, 4d, ar, efficient, geometry, dynamic, ray tracing  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: face, lighting, shadow, reflection, gaussian splatting, ray tracing  
- **[TranSplat: Surface Embedding-guided 3D Gaussian Splatting for Transparent Object Manipulation](https://arxiv.org/abs/2502.07840v1)**  
  Authors: Jeongyun Kim, Jeongho Noh, Dong-Guw Lee, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07840v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://github.)  
  Keywords: face, lighting, robotics, ar, gaussian splatting, 3d gaussian  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: nerf, survey, lighting, dynamic, 4d, motion, ar, deformation, gaussian splatting  
- **[GaussRender: Learning 3D Occupancy with Gaussian Rendering](https://arxiv.org/abs/2502.05040v1)**  
  Authors: Loick Chambon, Eloi Zablocki, Alexandre Boulch, Mickael Chen, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05040v1.pdf) | [![GitHub](https://img.shields.io/github/stars/valeoai/GaussRender?style=social)](https://github.com/valeoai/GaussRender)  
  Keywords: lighting, ar, efficient, geometry, gaussian splatting, understanding, semantic  

### SLAM

*Showing the latest 50 out of 208 papers*

- **[Direct Sparse Odometry with Continuous 3D Gaussian Maps for Indoor Environments](https://arxiv.org/abs/2503.03373v1)**  
  Authors: Jie Deng, Fengtian Lang, Zikang Yuan, Xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03373v1.pdf)  
  Keywords: tracking, robotics, ar, 3d gaussian, localization  
- **[DQO-MAP: Dual Quadrics Multi-Object mapping with Gaussian Splatting](https://arxiv.org/abs/2503.02223v1)**  
  Authors: Haoyuan Li, Ziqin Ye, Yue Hao, Weiyang Lin, Chao Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LiHaoy-ux/DQO-MAP?style=social)](https://github.com/LiHaoy-ux/DQO-MAP)  
  Keywords: ar, mapping, slam, gaussian splatting, 3d gaussian, high-fidelity  
- **[OpenGS-SLAM: Open-Set Dense Semantic SLAM with 3D Gaussian Splatting for Object-Level Scene Understanding](https://arxiv.org/abs/2503.01646v1)**  
  Authors: Dianyi Yang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01646v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://young-bit.github.io/opengs-github.github.io/.)  
  Keywords: segmentation, tracking, fast, understanding, ar, mapping, slam, gaussian splatting, 3d gaussian, semantic  
- **[FGS-SLAM: Fourier-based Gaussian Splatting for Real-time SLAM with Sparse and Dense Map Fusion](https://arxiv.org/abs/2503.01109v1)**  
  Authors: Yansong Xu, Junlin Li, Wei Zhang, Siyu Chen, Shengyong Zhang, Yuquan Leng, Weijia Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01109v1.pdf)  
  Keywords: tracking, ar, efficient, mapping, slam, gaussian splatting, 3d gaussian, high-fidelity, localization  
- **[Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration](https://arxiv.org/abs/2502.16652v1)**  
  Authors: Kim Jun-Seong, GeonU Kim, Kim Yu-Ji, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16652v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drsplat.github.io/)  
  Keywords: 3d gaussian, segmentation, understanding, ar, gaussian splatting, compact, semantic, localization  
- **[Dragen3D: Multiview Geometry Consistent 3D Gaussian Generation with Drag-Based Control](https://arxiv.org/abs/2502.16475v1)**  
  Authors: Jinbo Yan, Alan Zhao, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16475v1.pdf)  
  Keywords: face, ar, efficient, geometry, mapping, gaussian splatting, 3d gaussian  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: tracking, outdoor, ar, geometry, mapping, slam, gaussian splatting, 3d gaussian, high-fidelity  
- **[Hier-SLAM++: Neuro-Symbolic Semantic SLAM with a Hierarchically Categorical Gaussian Splatting](https://arxiv.org/abs/2502.14931v1)**  
  Authors: Boying Li, Vuong Chi Hao, Peter J. Stuckey, Ian Reid, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14931v1.pdf)  
  Keywords: nerf, 3d gaussian, understanding, ar, mapping, slam, gaussian splatting, compact, semantic  
- **[3D Gaussian Splatting aided Localization for Large and Complex Indoor-Environments](https://arxiv.org/abs/2502.13803v1)**  
  Authors: Vincent Ress, Jonas Meyer, Wei Zhang, David Skuddis, Uwe Soergel, Norbert Haala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13803v1.pdf)  
  Keywords: ar, geometry, slam, gaussian splatting, 3d gaussian, localization  
- **[High-Dynamic Radar Sequence Prediction for Weather Nowcasting Using Spatiotemporal Coherent Gaussian Representation](https://arxiv.org/abs/2502.14895v1)**  
  Authors: Ziye Wang, Yiran Qin, Lin Zeng, Ruimao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14895v1.pdf)  
  Keywords: tracking, dynamic, 4d, ar, efficient, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 240 papers*

- **[OpenGS-SLAM: Open-Set Dense Semantic SLAM with 3D Gaussian Splatting for Object-Level Scene Understanding](https://arxiv.org/abs/2503.01646v1)**  
  Authors: Dianyi Yang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01646v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://young-bit.github.io/opengs-github.github.io/.)  
  Keywords: segmentation, tracking, fast, understanding, ar, mapping, slam, gaussian splatting, 3d gaussian, semantic  
- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: ar, gaussian splatting, outdoor, semantic  
- **[Open-Vocabulary Semantic Part Segmentation of 3D Human](https://arxiv.org/abs/2502.19782v1)**  
  Authors: Keito Suzuki, Bang Du, Girish Krishnan, Kunyao Chen, Runfa Blark Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19782v1.pdf)  
  Keywords: human, segmentation, vr, ar, gaussian splatting, 3d gaussian, semantic  
- **[OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation](https://arxiv.org/abs/2502.18041v3)**  
  Authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.18041v3.pdf)  
  Keywords: segmentation, outdoor, ar, gaussian splatting, 3d gaussian, semantic  
- **[UniGS: Unified Language-Image-3D Pretraining with Gaussian Splatting](https://arxiv.org/abs/2502.17860v2)**  
  Authors: Haoyuan Li, Yanpeng Zhou, Tao Tang, Jifei Song, Yihan Zeng, Michael Kampffmeyer, Hang Xu, Xiaodan Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17860v2.pdf)  
  Keywords: ar, gaussian splatting, understanding, 3d gaussian  
- **[GS-TransUNet: Integrated 2D Gaussian Splatting and Transformer UNet for Accurate Skin Lesion Analysis](https://arxiv.org/abs/2502.16748v1)**  
  Authors: Anand Kumar, Kavinder Roghit Kanthen, Josna John  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16748v1.pdf)  
  Keywords: segmentation, fast, ar, efficient, medical, gaussian splatting  
- **[Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration](https://arxiv.org/abs/2502.16652v1)**  
  Authors: Kim Jun-Seong, GeonU Kim, Kim Yu-Ji, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16652v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drsplat.github.io/)  
  Keywords: 3d gaussian, segmentation, understanding, ar, gaussian splatting, compact, semantic, localization  
- **[Pointmap Association and Piecewise-Plane Constraint for Consistent and Compact 3D Gaussian Segmentation Field](https://arxiv.org/abs/2502.16303v1)**  
  Authors: Wenhao Hu, Wenhao Chai, Shengyu Hao, Xiaotong Cui, Xuexiang Wen, Jenq-Neng Hwang, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16303v1.pdf)  
  Keywords: 3d gaussian, segmentation, ar, compact, semantic  
- **[DynamicGSG: Dynamic 3D Gaussian Scene Graphs for Environment Adaptation](https://arxiv.org/abs/2502.15309v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Zhuo Yang, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15309v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GeLuzhou/Dynamic-GSG?style=social)](https://github.com/GeLuzhou/Dynamic-GSG)  
  Keywords: human, segmentation, dynamic, semantic, ar, gaussian splatting, 3d gaussian, high-fidelity  
- **[Hier-SLAM++: Neuro-Symbolic Semantic SLAM with a Hierarchically Categorical Gaussian Splatting](https://arxiv.org/abs/2502.14931v1)**  
  Authors: Boying Li, Vuong Chi Hao, Peter J. Stuckey, Ian Reid, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14931v1.pdf)  
  Keywords: nerf, 3d gaussian, understanding, ar, mapping, slam, gaussian splatting, compact, semantic  



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