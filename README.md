# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-03-11 00:49:26

## Categories

- [3DGS Surveys](#3dgs-surveys) (23 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (399 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1405 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (474 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (522 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (98 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (466 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (75 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (533 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (228 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (33 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (156 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (213 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (245 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: 3d reconstruction, compression, ar, nerf, efficient, gaussian splatting, survey, 3d gaussian, real-time rendering  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: deformation, 4d, lighting, motion, ar, nerf, gaussian splatting, survey, dynamic  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, ar, gaussian splatting, survey, 3d gaussian  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: slam, dynamic, lighting, ar, outdoor, reflection, survey, tracking, geometry, localization, face, mapping, 3d gaussian  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: recognition, illumination, ar, gaussian splatting, survey, 3d gaussian  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: 3d reconstruction, robotics, high-fidelity, lighting, ar, nerf, compact, gaussian splatting, survey, geometry, autonomous driving, dynamic, semantic  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: understanding, robotics, ar, nerf, gaussian splatting, survey, 3d gaussian, real-time rendering  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: high-fidelity, lighting, ar, nerf, gaussian splatting, survey, 3d gaussian  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: 3d reconstruction, robotics, ar, nerf, gaussian splatting, survey, autonomous driving, vr, 3d gaussian  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: survey, 3d gaussian, ar  

### Acceleration

*Showing the latest 50 out of 399 papers*

- **[D2GV: Deformable 2D Gaussian Splatting for Video Representation in 400FPS](https://arxiv.org/abs/2503.05600v1)**  
  Authors: Mufan Liu, Qi Yang, Miaoran Zhao, He Huang, Le Yang, Zhu Li, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05600v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Evan-sudo/D2GV?style=social)](https://github.com/Evan-sudo/D2GV)  
  Keywords: compression, ar, efficient, compact, gaussian splatting, fast  
- **[CoMoGaussian: Continuous Motion-Aware Gaussian Splatting from Motion-Blurred Images](https://arxiv.org/abs/2503.05332v1)**  
  Authors: Jungho Lee, Donghyeong Kim, Dogyoon Lee, Suhwan Cho, Minhyeok Lee, Wonjoon Lee, Taeoh Kim, Dongyoon Wee, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05332v1.pdf)  
  Keywords: motion, ar, gaussian splatting, body, 3d gaussian, real-time rendering  
- **[SeeLe: A Unified Acceleration Framework for Real-Time Gaussian Splatting](https://arxiv.org/abs/2503.05168v1)**  
  Authors: Xiaotong Huang, He Zhu, Zihan Liu, Weikai Lin, Xiaohong Liu, Zhezhi He, Jingwen Leng, Minyi Guo, Yu Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05168v1.pdf)  
  Keywords: ar, acceleration, 3d gaussian, gaussian splatting  
- **[EvolvingGS: High-Fidelity Streamable Volumetric Video via Evolving 3D Gaussian Representation](https://arxiv.org/abs/2503.05162v1)**  
  Authors: Chao Zhang, Yifeng Zhou, Shuheng Wang, Wenfa Li, Degang Wang, Yi Xu, Shaohui Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05162v1.pdf)  
  Keywords: dynamic, compression, high-fidelity, motion, ar, efficient, gaussian splatting, human, fast, 3d gaussian, high quality  
- **[GaussianVideo: Efficient Video Representation and Compression by Gaussian Splatting](https://arxiv.org/abs/2503.04333v1)**  
  Authors: Inseo Lee, Youngyoon Choi, Joonseok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04333v1.pdf)  
  Keywords: compression, ar, efficient, gaussian splatting, fast, dynamic, lightweight  
- **[Surgical Gaussian Surfels: Highly Accurate Real-time Surgical Scene Rendering](https://arxiv.org/abs/2503.04079v1)**  
  Authors: Idris O. Sunmola, Zhenjun Zhao, Samuel Schmidgall, Yumeng Wang, Paul Maria Scheikl, Axel Krieger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04079v1.pdf) | [![GitHub](https://img.shields.io/github/stars/aloma85/SurgicalGaussianSurfels?style=social)](https://github.com/aloma85/SurgicalGaussianSurfels)  
  Keywords: deformation, motion, ar, nerf, efficient, geometry, face, 3d gaussian, real-time rendering, lightweight  
- **[Beyond Existance: Fulfill 3D Reconstructed Scenes with Pseudo Details](https://arxiv.org/abs/2503.04037v1)**  
  Authors: Yifei Gao, Jun Huang, Lei Wang, Ruiting Dai, Jun Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04037v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, fast, 3d gaussian  
- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: dynamic, high-fidelity, ar, nerf, gaussian splatting, human, fast, geometry, 3d gaussian, avatar, real-time rendering  
- **[OpenGS-SLAM: Open-Set Dense Semantic SLAM with 3D Gaussian Splatting for Object-Level Scene Understanding](https://arxiv.org/abs/2503.01646v1)**  
  Authors: Dianyi Yang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01646v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://young-bit.github.io/opengs-github.github.io/.)  
  Keywords: slam, understanding, ar, gaussian splatting, segmentation, tracking, fast, mapping, 3d gaussian, semantic  
- **[Evolving High-Quality Rendering and Reconstruction in a Unified Framework with Contribution-Adaptive Regularization](https://arxiv.org/abs/2503.00881v1)**  
  Authors: You Shen, Zhipeng Zhang, Xinyang Li, Yansong Qu, Yu Lin, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00881v1.pdf)  
  Keywords: ar, compact, gaussian splatting, geometry, fast, face, 3d gaussian  

### Applications

*Showing the latest 50 out of 1405 papers*

- **[D2GV: Deformable 2D Gaussian Splatting for Video Representation in 400FPS](https://arxiv.org/abs/2503.05600v1)**  
  Authors: Mufan Liu, Qi Yang, Miaoran Zhao, He Huang, Le Yang, Zhu Li, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05600v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Evan-sudo/D2GV?style=social)](https://github.com/Evan-sudo/D2GV)  
  Keywords: compression, ar, efficient, compact, gaussian splatting, fast  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v1)**  
  Authors: Jiahui Fan, Fujun Luan, Miloš Hašan, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v1.pdf)  
  Keywords: relighting, lightweight, motion, lighting, ar, gaussian splatting, human, 3d gaussian, high quality, relightable  
- **[LiDAR-enhanced 3D Gaussian Splatting Mapping](https://arxiv.org/abs/2503.05425v1)**  
  Authors: Jian Shen, Huai Yu, Ji Wu, Wen Yang, Gui-Song Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05425v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, tracking, geometry, mapping, dynamic  
- **[Self-Modeling Robots by Photographing](https://arxiv.org/abs/2503.05398v1)**  
  Authors: Kejun Hu, Peng Yu, Ning Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05398v1.pdf)  
  Keywords: deformation, motion, ar, gaussian splatting, human, 3d gaussian  
- **[CoMoGaussian: Continuous Motion-Aware Gaussian Splatting from Motion-Blurred Images](https://arxiv.org/abs/2503.05332v1)**  
  Authors: Jungho Lee, Donghyeong Kim, Dogyoon Lee, Suhwan Cho, Minhyeok Lee, Wonjoon Lee, Taeoh Kim, Dongyoon Wee, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05332v1.pdf)  
  Keywords: motion, ar, gaussian splatting, body, 3d gaussian, real-time rendering  
- **[STGA: Selective-Training Gaussian Head Avatars](https://arxiv.org/abs/2503.05196v1)**  
  Authors: Hanzhi Guo, Yixiao Chen, Dongye Xiaonuo, Zeyu Tian, Dongdong Weng, Le Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05196v1.pdf)  
  Keywords: head, ar, 3d gaussian, dynamic, avatar, animation  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: ar, efficient, compact, human, tracking, geometry, dynamic, semantic  
- **[MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions](https://arxiv.org/abs/2503.05182v1)**  
  Authors: Qingyuan Zhou, Yuehu Gong, Weidong Yang, Jiaze Li, Yeqi Luo, Baixin Xu, Shuhao Li, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05182v1.pdf)  
  Keywords: 3d reconstruction, high-fidelity, illumination, ar, gaussian splatting, geometry, face, 3d gaussian  
- **[SplatPose: Geometry-Aware 6-DoF Pose Estimation from Single RGB Image via 3D Gaussian Splatting](https://arxiv.org/abs/2503.05174v1)**  
  Authors: Linqi Yang, Xiongwei Zhao, Qihao Sun, Ke Wang, Ao Chen, Peng Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05174v1.pdf)  
  Keywords: robotics, ar, gaussian splatting, geometry, 3d gaussian  
- **[SeeLe: A Unified Acceleration Framework for Real-Time Gaussian Splatting](https://arxiv.org/abs/2503.05168v1)**  
  Authors: Xiaotong Huang, He Zhu, Zihan Liu, Weikai Lin, Xiaohong Liu, Zhezhi He, Jingwen Leng, Minyi Guo, Yu Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05168v1.pdf)  
  Keywords: ar, acceleration, 3d gaussian, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 474 papers*

- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v1)**  
  Authors: Jiahui Fan, Fujun Luan, Miloš Hašan, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v1.pdf)  
  Keywords: relighting, lightweight, motion, lighting, ar, gaussian splatting, human, 3d gaussian, high quality, relightable  
- **[Self-Modeling Robots by Photographing](https://arxiv.org/abs/2503.05398v1)**  
  Authors: Kejun Hu, Peng Yu, Ning Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05398v1.pdf)  
  Keywords: deformation, motion, ar, gaussian splatting, human, 3d gaussian  
- **[CoMoGaussian: Continuous Motion-Aware Gaussian Splatting from Motion-Blurred Images](https://arxiv.org/abs/2503.05332v1)**  
  Authors: Jungho Lee, Donghyeong Kim, Dogyoon Lee, Suhwan Cho, Minhyeok Lee, Wonjoon Lee, Taeoh Kim, Dongyoon Wee, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05332v1.pdf)  
  Keywords: motion, ar, gaussian splatting, body, 3d gaussian, real-time rendering  
- **[STGA: Selective-Training Gaussian Head Avatars](https://arxiv.org/abs/2503.05196v1)**  
  Authors: Hanzhi Guo, Yixiao Chen, Dongye Xiaonuo, Zeyu Tian, Dongdong Weng, Le Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05196v1.pdf)  
  Keywords: head, ar, 3d gaussian, dynamic, avatar, animation  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: ar, efficient, compact, human, tracking, geometry, dynamic, semantic  
- **[MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions](https://arxiv.org/abs/2503.05182v1)**  
  Authors: Qingyuan Zhou, Yuehu Gong, Weidong Yang, Jiaze Li, Yeqi Luo, Baixin Xu, Shuhao Li, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05182v1.pdf)  
  Keywords: 3d reconstruction, high-fidelity, illumination, ar, gaussian splatting, geometry, face, 3d gaussian  
- **[EvolvingGS: High-Fidelity Streamable Volumetric Video via Evolving 3D Gaussian Representation](https://arxiv.org/abs/2503.05162v1)**  
  Authors: Chao Zhang, Yifeng Zhou, Shuheng Wang, Wenfa Li, Degang Wang, Yi Xu, Shaohui Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05162v1.pdf)  
  Keywords: dynamic, compression, high-fidelity, motion, ar, efficient, gaussian splatting, human, fast, 3d gaussian, high quality  
- **[GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting](https://arxiv.org/abs/2503.05152v1)**  
  Authors: Kohei Honda, Takeshi Ishita, Yasuhiro Yoshimura, Ryo Yonitani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05152v1.pdf)  
  Keywords: head, ar, gaussian splatting, localization, 3d gaussian  
- **[Surgical Gaussian Surfels: Highly Accurate Real-time Surgical Scene Rendering](https://arxiv.org/abs/2503.04079v1)**  
  Authors: Idris O. Sunmola, Zhenjun Zhao, Samuel Schmidgall, Yumeng Wang, Paul Maria Scheikl, Axel Krieger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04079v1.pdf) | [![GitHub](https://img.shields.io/github/stars/aloma85/SurgicalGaussianSurfels?style=social)](https://github.com/aloma85/SurgicalGaussianSurfels)  
  Keywords: deformation, motion, ar, nerf, efficient, geometry, face, 3d gaussian, real-time rendering, lightweight  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: ar, efficient, nerf, gaussian splatting, human, neural rendering, few-shot, semantic  

### Dynamic Scene

*Showing the latest 50 out of 522 papers*

- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v1)**  
  Authors: Jiahui Fan, Fujun Luan, Miloš Hašan, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v1.pdf)  
  Keywords: relighting, lightweight, motion, lighting, ar, gaussian splatting, human, 3d gaussian, high quality, relightable  
- **[LiDAR-enhanced 3D Gaussian Splatting Mapping](https://arxiv.org/abs/2503.05425v1)**  
  Authors: Jian Shen, Huai Yu, Ji Wu, Wen Yang, Gui-Song Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05425v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, tracking, geometry, mapping, dynamic  
- **[Self-Modeling Robots by Photographing](https://arxiv.org/abs/2503.05398v1)**  
  Authors: Kejun Hu, Peng Yu, Ning Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05398v1.pdf)  
  Keywords: deformation, motion, ar, gaussian splatting, human, 3d gaussian  
- **[CoMoGaussian: Continuous Motion-Aware Gaussian Splatting from Motion-Blurred Images](https://arxiv.org/abs/2503.05332v1)**  
  Authors: Jungho Lee, Donghyeong Kim, Dogyoon Lee, Suhwan Cho, Minhyeok Lee, Wonjoon Lee, Taeoh Kim, Dongyoon Wee, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05332v1.pdf)  
  Keywords: motion, ar, gaussian splatting, body, 3d gaussian, real-time rendering  
- **[STGA: Selective-Training Gaussian Head Avatars](https://arxiv.org/abs/2503.05196v1)**  
  Authors: Hanzhi Guo, Yixiao Chen, Dongye Xiaonuo, Zeyu Tian, Dongdong Weng, Le Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05196v1.pdf)  
  Keywords: head, ar, 3d gaussian, dynamic, avatar, animation  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: ar, efficient, compact, human, tracking, geometry, dynamic, semantic  
- **[EvolvingGS: High-Fidelity Streamable Volumetric Video via Evolving 3D Gaussian Representation](https://arxiv.org/abs/2503.05162v1)**  
  Authors: Chao Zhang, Yifeng Zhou, Shuheng Wang, Wenfa Li, Degang Wang, Yi Xu, Shaohui Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05162v1.pdf)  
  Keywords: dynamic, compression, high-fidelity, motion, ar, efficient, gaussian splatting, human, fast, 3d gaussian, high quality  
- **[GaussianVideo: Efficient Video Representation and Compression by Gaussian Splatting](https://arxiv.org/abs/2503.04333v1)**  
  Authors: Inseo Lee, Youngyoon Choi, Joonseok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04333v1.pdf)  
  Keywords: compression, ar, efficient, gaussian splatting, fast, dynamic, lightweight  
- **[Surgical Gaussian Surfels: Highly Accurate Real-time Surgical Scene Rendering](https://arxiv.org/abs/2503.04079v1)**  
  Authors: Idris O. Sunmola, Zhenjun Zhao, Samuel Schmidgall, Yumeng Wang, Paul Maria Scheikl, Axel Krieger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04079v1.pdf) | [![GitHub](https://img.shields.io/github/stars/aloma85/SurgicalGaussianSurfels?style=social)](https://github.com/aloma85/SurgicalGaussianSurfels)  
  Keywords: deformation, motion, ar, nerf, efficient, geometry, face, 3d gaussian, real-time rendering, lightweight  
- **[GaussianGraph: 3D Gaussian-based Scene Graph Generation for Open-world Scene Understanding](https://arxiv.org/abs/2503.04034v1)**  
  Authors: Xihan Wang, Dianyi Yang, Yu Gao, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04034v1.pdf)  
  Keywords: compression, understanding, ar, 3d gaussian, gaussian splatting, segmentation, dynamic, semantic  

### Few-shot

*Showing the latest 50 out of 98 papers*

- **[GaussianCAD: Robust Self-Supervised CAD Reconstruction from Three Orthographic Views Using 3D Gaussian Splatting](https://arxiv.org/abs/2503.05161v1)**  
  Authors: Zheng Zhou, Zhe Li, Bo Yu, Lina Hu, Liang Dong, Zijian Yang, Xiaoli Liu, Ning Xu, Ziwei Wang, Yonghao Dang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05161v1.pdf)  
  Keywords: 3d reconstruction, ar, sparse-view, gaussian splatting, 3d gaussian  
- **[S2Gaussian: Sparse-View Super-Resolution 3D Gaussian Splatting](https://arxiv.org/abs/2503.04314v1)**  
  Authors: Yecong Wan, Mingwen Shao, Yuanshuo Cheng, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04314v1.pdf)  
  Keywords: sparse view, ar, sparse-view, gaussian splatting, geometry, 3d gaussian  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: ar, efficient, nerf, gaussian splatting, human, neural rendering, few-shot, semantic  
- **[Seeing A 3D World in A Grain of Sand](https://arxiv.org/abs/2503.00260v1)**  
  Authors: Yufan Zhang, Yu Ji, Yu Guo, Jinwei Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00260v1.pdf)  
  Keywords: sparse view, 3d reconstruction, ar, gaussian splatting, face, 3d gaussian  
- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: sparse view, 3d reconstruction, high-fidelity, ar, efficient, gaussian splatting, 3d gaussian  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: slam, ar, nerf, sparse-view, gaussian splatting, tracking, geometry, mapping, real-time rendering  
- **[DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform](https://arxiv.org/abs/2501.12637v2)**  
  Authors: Hung Nguyen, Blark Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12637v2.pdf)  
  Keywords: head, ar, nerf, fast, few-shot  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: 4d, ar, sparse-view, gaussian splatting, 3d gaussian, semantic  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: 3d reconstruction, ar, nerf, sparse-view, gaussian splatting, efficient, 3d gaussian  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: sparse view, lighting, ar, medical, nerf, gaussian splatting, human, face, dynamic  

### Geometry Reconstruction

*Showing the latest 50 out of 466 papers*

- **[LiDAR-enhanced 3D Gaussian Splatting Mapping](https://arxiv.org/abs/2503.05425v1)**  
  Authors: Jian Shen, Huai Yu, Ji Wu, Wen Yang, Gui-Song Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05425v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, tracking, geometry, mapping, dynamic  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: ar, efficient, compact, human, tracking, geometry, dynamic, semantic  
- **[MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions](https://arxiv.org/abs/2503.05182v1)**  
  Authors: Qingyuan Zhou, Yuehu Gong, Weidong Yang, Jiaze Li, Yeqi Luo, Baixin Xu, Shuhao Li, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05182v1.pdf)  
  Keywords: 3d reconstruction, high-fidelity, illumination, ar, gaussian splatting, geometry, face, 3d gaussian  
- **[SplatPose: Geometry-Aware 6-DoF Pose Estimation from Single RGB Image via 3D Gaussian Splatting](https://arxiv.org/abs/2503.05174v1)**  
  Authors: Linqi Yang, Xiongwei Zhao, Qihao Sun, Ke Wang, Ao Chen, Peng Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05174v1.pdf)  
  Keywords: robotics, ar, gaussian splatting, geometry, 3d gaussian  
- **[GaussianCAD: Robust Self-Supervised CAD Reconstruction from Three Orthographic Views Using 3D Gaussian Splatting](https://arxiv.org/abs/2503.05161v1)**  
  Authors: Zheng Zhou, Zhe Li, Bo Yu, Lina Hu, Liang Dong, Zijian Yang, Xiaoli Liu, Ning Xu, Ziwei Wang, Yonghao Dang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05161v1.pdf)  
  Keywords: 3d reconstruction, ar, sparse-view, gaussian splatting, 3d gaussian  
- **[S2Gaussian: Sparse-View Super-Resolution 3D Gaussian Splatting](https://arxiv.org/abs/2503.04314v1)**  
  Authors: Yecong Wan, Mingwen Shao, Yuanshuo Cheng, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04314v1.pdf)  
  Keywords: sparse view, ar, sparse-view, gaussian splatting, geometry, 3d gaussian  
- **[Instrument-Splatting: Controllable Photorealistic Reconstruction of Surgical Instruments Using Gaussian Splatting](https://arxiv.org/abs/2503.04082v1)**  
  Authors: Shuojue Yang, Zijian Wu, Mingxuan Hong, Qian Li, Daiyun Shen, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04082v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, tracking, geometry, 3d gaussian, semantic  
- **[Surgical Gaussian Surfels: Highly Accurate Real-time Surgical Scene Rendering](https://arxiv.org/abs/2503.04079v1)**  
  Authors: Idris O. Sunmola, Zhenjun Zhao, Samuel Schmidgall, Yumeng Wang, Paul Maria Scheikl, Axel Krieger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04079v1.pdf) | [![GitHub](https://img.shields.io/github/stars/aloma85/SurgicalGaussianSurfels?style=social)](https://github.com/aloma85/SurgicalGaussianSurfels)  
  Keywords: deformation, motion, ar, nerf, efficient, geometry, face, 3d gaussian, real-time rendering, lightweight  
- **[Beyond Existance: Fulfill 3D Reconstructed Scenes with Pseudo Details](https://arxiv.org/abs/2503.04037v1)**  
  Authors: Yifei Gao, Jun Huang, Lei Wang, Ruiting Dai, Jun Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04037v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, fast, 3d gaussian  
- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115v1)**  
  Authors: Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03115v1.pdf)  
  Keywords: 3d reconstruction, 4d, ar, efficient, gaussian splatting, face, dynamic  

### Large Scene

*Showing the latest 50 out of 75 papers*

- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: ar, outdoor, gaussian splatting, semantic  
- **[OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation](https://arxiv.org/abs/2502.18041v4)**  
  Authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.18041v4.pdf)  
  Keywords: ar, outdoor, gaussian splatting, segmentation, 3d gaussian, semantic  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: slam, high-fidelity, ar, outdoor, gaussian splatting, tracking, geometry, mapping, 3d gaussian  
- **[RadSplatter: Extending 3D Gaussian Splatting to Radio Frequencies for Wireless Radiomap Extrapolation](https://arxiv.org/abs/2502.12686v1)**  
  Authors: Yiheng Wang, Ye Xue, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.12686v1.pdf)  
  Keywords: ar, efficient, outdoor, gaussian splatting, autonomous driving, 3d gaussian  
- **[GS-GVINS: A Tightly-integrated GNSS-Visual-Inertial Navigation System Augmented by 3D Gaussian Splatting](https://arxiv.org/abs/2502.10975v1)**  
  Authors: Zelin Zhou, Saurav Uprety, Shichuang Nie, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10975v1.pdf)  
  Keywords: slam, motion, ar, 3d gaussian, outdoor, gaussian splatting, tracking, dynamic  
- **[PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression](https://arxiv.org/abs/2502.04843v2)**  
  Authors: Feifei Li, Qi Song, Chi Zhang, Hui Shuai, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04843v2.pdf)  
  Keywords: ar, nerf, outdoor, gaussian splatting  
- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: ar, efficient, outdoor, gaussian splatting, 3d gaussian  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: slam, ar, nerf, gaussian splatting, outdoor, large scene, geometry, localization, mapping, dynamic  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: understanding, motion, ar, 3d gaussian, outdoor, dynamic, real-time rendering  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: slam, ar, nerf, efficient, outdoor, gaussian splatting, neural rendering, mapping, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 533 papers*

- **[D2GV: Deformable 2D Gaussian Splatting for Video Representation in 400FPS](https://arxiv.org/abs/2503.05600v1)**  
  Authors: Mufan Liu, Qi Yang, Miaoran Zhao, He Huang, Le Yang, Zhu Li, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05600v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Evan-sudo/D2GV?style=social)](https://github.com/Evan-sudo/D2GV)  
  Keywords: compression, ar, efficient, compact, gaussian splatting, fast  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v1)**  
  Authors: Jiahui Fan, Fujun Luan, Miloš Hašan, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v1.pdf)  
  Keywords: relighting, lightweight, motion, lighting, ar, gaussian splatting, human, 3d gaussian, high quality, relightable  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: ar, efficient, compact, human, tracking, geometry, dynamic, semantic  
- **[EvolvingGS: High-Fidelity Streamable Volumetric Video via Evolving 3D Gaussian Representation](https://arxiv.org/abs/2503.05162v1)**  
  Authors: Chao Zhang, Yifeng Zhou, Shuheng Wang, Wenfa Li, Degang Wang, Yi Xu, Shaohui Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05162v1.pdf)  
  Keywords: dynamic, compression, high-fidelity, motion, ar, efficient, gaussian splatting, human, fast, 3d gaussian, high quality  
- **[GaussianVideo: Efficient Video Representation and Compression by Gaussian Splatting](https://arxiv.org/abs/2503.04333v1)**  
  Authors: Inseo Lee, Youngyoon Choi, Joonseok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04333v1.pdf)  
  Keywords: compression, ar, efficient, gaussian splatting, fast, dynamic, lightweight  
- **[Surgical Gaussian Surfels: Highly Accurate Real-time Surgical Scene Rendering](https://arxiv.org/abs/2503.04079v1)**  
  Authors: Idris O. Sunmola, Zhenjun Zhao, Samuel Schmidgall, Yumeng Wang, Paul Maria Scheikl, Axel Krieger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04079v1.pdf) | [![GitHub](https://img.shields.io/github/stars/aloma85/SurgicalGaussianSurfels?style=social)](https://github.com/aloma85/SurgicalGaussianSurfels)  
  Keywords: deformation, motion, ar, nerf, efficient, geometry, face, 3d gaussian, real-time rendering, lightweight  
- **[GaussianGraph: 3D Gaussian-based Scene Graph Generation for Open-world Scene Understanding](https://arxiv.org/abs/2503.04034v1)**  
  Authors: Xihan Wang, Dianyi Yang, Yu Gao, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04034v1.pdf)  
  Keywords: compression, understanding, ar, 3d gaussian, gaussian splatting, segmentation, dynamic, semantic  
- **[GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2503.03984v1)**  
  Authors: Qianzhong Chen, Jiankai Sun, Naixiang Gao, JunEn Low, Timothy Chen, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03984v1.pdf)  
  Keywords: high-fidelity, ar, 3d gaussian, efficient, gaussian splatting, dynamic  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: ar, efficient, nerf, gaussian splatting, human, neural rendering, few-shot, semantic  
- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115v1)**  
  Authors: Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03115v1.pdf)  
  Keywords: 3d reconstruction, 4d, ar, efficient, gaussian splatting, face, dynamic  

### Quality Enhancement

*Showing the latest 50 out of 228 papers*

- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v1)**  
  Authors: Jiahui Fan, Fujun Luan, Miloš Hašan, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v1.pdf)  
  Keywords: relighting, lightweight, motion, lighting, ar, gaussian splatting, human, 3d gaussian, high quality, relightable  
- **[MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions](https://arxiv.org/abs/2503.05182v1)**  
  Authors: Qingyuan Zhou, Yuehu Gong, Weidong Yang, Jiaze Li, Yeqi Luo, Baixin Xu, Shuhao Li, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05182v1.pdf)  
  Keywords: 3d reconstruction, high-fidelity, illumination, ar, gaussian splatting, geometry, face, 3d gaussian  
- **[EvolvingGS: High-Fidelity Streamable Volumetric Video via Evolving 3D Gaussian Representation](https://arxiv.org/abs/2503.05162v1)**  
  Authors: Chao Zhang, Yifeng Zhou, Shuheng Wang, Wenfa Li, Degang Wang, Yi Xu, Shaohui Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05162v1.pdf)  
  Keywords: dynamic, compression, high-fidelity, motion, ar, efficient, gaussian splatting, human, fast, 3d gaussian, high quality  
- **[GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2503.03984v1)**  
  Authors: Qianzhong Chen, Jiankai Sun, Naixiang Gao, JunEn Low, Timothy Chen, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03984v1.pdf)  
  Keywords: high-fidelity, ar, 3d gaussian, efficient, gaussian splatting, dynamic  
- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: dynamic, high-fidelity, ar, nerf, gaussian splatting, human, fast, geometry, 3d gaussian, avatar, real-time rendering  
- **[DQO-MAP: Dual Quadrics Multi-Object mapping with Gaussian Splatting](https://arxiv.org/abs/2503.02223v1)**  
  Authors: Haoyuan Li, Ziqin Ye, Yue Hao, Weiyang Lin, Chao Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LiHaoy-ux/DQO-MAP?style=social)](https://github.com/LiHaoy-ux/DQO-MAP)  
  Keywords: slam, high-fidelity, ar, gaussian splatting, mapping, 3d gaussian  
- **[FGS-SLAM: Fourier-based Gaussian Splatting for Real-time SLAM with Sparse and Dense Map Fusion](https://arxiv.org/abs/2503.01109v1)**  
  Authors: Yansong Xu, Junlin Li, Wei Zhang, Siyu Chen, Shengyong Zhang, Yuquan Leng, Weijia Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01109v1.pdf)  
  Keywords: slam, high-fidelity, ar, efficient, gaussian splatting, tracking, localization, mapping, 3d gaussian  
- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: sparse view, 3d reconstruction, high-fidelity, ar, efficient, gaussian splatting, 3d gaussian  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: slam, high-fidelity, ar, outdoor, gaussian splatting, tracking, geometry, mapping, 3d gaussian  
- **[DynamicGSG: Dynamic 3D Gaussian Scene Graphs for Environment Adaptation](https://arxiv.org/abs/2502.15309v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Zhuo Yang, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15309v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GeLuzhou/Dynamic-GSG?style=social)](https://github.com/GeLuzhou/Dynamic-GSG)  
  Keywords: high-fidelity, ar, 3d gaussian, gaussian splatting, human, segmentation, dynamic, semantic  

### Ray Tracing

- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: ray tracing, 4d, lighting, ar, efficient, tracking, geometry, face, dynamic, real-time rendering, relightable  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: ray tracing, lighting, shadow, gaussian splatting, reflection, face  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, ar, gaussian splatting, survey, 3d gaussian  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: ray tracing, ar, efficient, light transport, acceleration, gaussian splatting, reflection  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: ray tracing, ar, shadow, gaussian splatting, reflection, 3d gaussian  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: relighting, ray tracing, lighting, ar, efficient, gaussian splatting, reflection  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: ray tracing, high-fidelity, lighting, ar, efficient, gaussian splatting, reflection, 3d gaussian, real-time rendering  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: global illumination, illumination, ar, nerf, efficient, gaussian splatting, fast, geometry, face, mapping  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v2)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v2.pdf)  
  Keywords: ray tracing, ar, efficient, gaussian splatting, 3d gaussian  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: ar, 3d gaussian, ray tracing, gaussian splatting  

### Relighting

*Showing the latest 50 out of 156 papers*

- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v1)**  
  Authors: Jiahui Fan, Fujun Luan, Miloš Hašan, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v1.pdf)  
  Keywords: relighting, lightweight, motion, lighting, ar, gaussian splatting, human, 3d gaussian, high quality, relightable  
- **[MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions](https://arxiv.org/abs/2503.05182v1)**  
  Authors: Qingyuan Zhou, Yuehu Gong, Weidong Yang, Jiaze Li, Yeqi Luo, Baixin Xu, Shuhao Li, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05182v1.pdf)  
  Keywords: 3d reconstruction, high-fidelity, illumination, ar, gaussian splatting, geometry, face, 3d gaussian  
- **[EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering](https://arxiv.org/abs/2502.20669v1)**  
  Authors: John J. Han, Jie Ying Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20669v1.pdf)  
  Keywords: 3d reconstruction, lighting, ar, medical, gaussian splatting, geometry, face, 3d gaussian  
- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941v1)**  
  Authors: Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16941v1.pdf)  
  Keywords: 4d, lighting, ar, efficient, nerf  
- **[RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection](https://arxiv.org/abs/2502.13071v1)**  
  Authors: Jingtong Yue, Zhiwei Lin, Xin Lin, Xiaoyu Zhou, Xiangtai Li, Lu Qi, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13071v1.pdf)  
  Keywords: lighting, face, 3d gaussian, ar  
- **[OMG: Opacity Matters in Material Modeling with Gaussian Splatting](https://arxiv.org/abs/2502.10988v2)**  
  Authors: Silong Yong, Venkata Nagarjun Pudureddiyur Manivannan, Bernhard Kerbl, Zifu Wan, Simon Stepputtis, Katia Sycara, Yaqi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10988v2.pdf)  
  Keywords: lighting, ar, gaussian splatting, neural rendering, geometry, 3d gaussian, real-time rendering  
- **[E-3DGS: Event-Based Novel View Rendering of Large-Scale Scenes Using 3D Gaussian Splatting](https://arxiv.org/abs/2502.10827v1)**  
  Authors: Sohaib Zahid, Viktor Rudnev, Eddy Ilg, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10827v1.pdf)  
  Keywords: dynamic, motion, lighting, ar, nerf, gaussian splatting, fast, 3d gaussian  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: ray tracing, 4d, lighting, ar, efficient, tracking, geometry, face, dynamic, real-time rendering, relightable  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: ray tracing, lighting, shadow, gaussian splatting, reflection, face  
- **[TranSplat: Surface Embedding-guided 3D Gaussian Splatting for Transparent Object Manipulation](https://arxiv.org/abs/2502.07840v1)**  
  Authors: Jeongyun Kim, Jeongho Noh, Dong-Guw Lee, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07840v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://github.)  
  Keywords: robotics, lighting, ar, gaussian splatting, face, 3d gaussian  

### SLAM

*Showing the latest 50 out of 213 papers*

- **[LiDAR-enhanced 3D Gaussian Splatting Mapping](https://arxiv.org/abs/2503.05425v1)**  
  Authors: Jian Shen, Huai Yu, Ji Wu, Wen Yang, Gui-Song Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05425v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, tracking, geometry, mapping, dynamic  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: ar, efficient, compact, human, tracking, geometry, dynamic, semantic  
- **[GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting](https://arxiv.org/abs/2503.05152v1)**  
  Authors: Kohei Honda, Takeshi Ishita, Yasuhiro Yoshimura, Ryo Yonitani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05152v1.pdf)  
  Keywords: head, ar, gaussian splatting, localization, 3d gaussian  
- **[Instrument-Splatting: Controllable Photorealistic Reconstruction of Surgical Instruments Using Gaussian Splatting](https://arxiv.org/abs/2503.04082v1)**  
  Authors: Shuojue Yang, Zijian Wu, Mingxuan Hong, Qian Li, Daiyun Shen, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04082v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, tracking, geometry, 3d gaussian, semantic  
- **[Direct Sparse Odometry with Continuous 3D Gaussian Maps for Indoor Environments](https://arxiv.org/abs/2503.03373v1)**  
  Authors: Jie Deng, Fengtian Lang, Zikang Yuan, Xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03373v1.pdf)  
  Keywords: robotics, ar, tracking, localization, 3d gaussian  
- **[DQO-MAP: Dual Quadrics Multi-Object mapping with Gaussian Splatting](https://arxiv.org/abs/2503.02223v1)**  
  Authors: Haoyuan Li, Ziqin Ye, Yue Hao, Weiyang Lin, Chao Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LiHaoy-ux/DQO-MAP?style=social)](https://github.com/LiHaoy-ux/DQO-MAP)  
  Keywords: slam, high-fidelity, ar, gaussian splatting, mapping, 3d gaussian  
- **[OpenGS-SLAM: Open-Set Dense Semantic SLAM with 3D Gaussian Splatting for Object-Level Scene Understanding](https://arxiv.org/abs/2503.01646v1)**  
  Authors: Dianyi Yang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01646v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://young-bit.github.io/opengs-github.github.io/.)  
  Keywords: slam, understanding, ar, gaussian splatting, segmentation, tracking, fast, mapping, 3d gaussian, semantic  
- **[FGS-SLAM: Fourier-based Gaussian Splatting for Real-time SLAM with Sparse and Dense Map Fusion](https://arxiv.org/abs/2503.01109v1)**  
  Authors: Yansong Xu, Junlin Li, Wei Zhang, Siyu Chen, Shengyong Zhang, Yuquan Leng, Weijia Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01109v1.pdf)  
  Keywords: slam, high-fidelity, ar, efficient, gaussian splatting, tracking, localization, mapping, 3d gaussian  
- **[Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration](https://arxiv.org/abs/2502.16652v1)**  
  Authors: Kim Jun-Seong, GeonU Kim, Kim Yu-Ji, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16652v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drsplat.github.io/)  
  Keywords: understanding, ar, compact, gaussian splatting, segmentation, localization, 3d gaussian, semantic  
- **[Dragen3D: Multiview Geometry Consistent 3D Gaussian Generation with Drag-Based Control](https://arxiv.org/abs/2502.16475v1)**  
  Authors: Jinbo Yan, Alan Zhao, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16475v1.pdf)  
  Keywords: ar, efficient, gaussian splatting, geometry, face, mapping, 3d gaussian  

### Scene Understanding

*Showing the latest 50 out of 245 papers*

- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: ar, efficient, compact, human, tracking, geometry, dynamic, semantic  
- **[Manboformer: Learning Gaussian Representations via Spatial-temporal Attention Mechanism](https://arxiv.org/abs/2503.04863v1)**  
  Authors: Ziyue Zhao, Qining Qi, Jianfa Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04863v1.pdf)  
  Keywords: autonomous driving, 3d gaussian, ar, semantic  
- **[Instrument-Splatting: Controllable Photorealistic Reconstruction of Surgical Instruments Using Gaussian Splatting](https://arxiv.org/abs/2503.04082v1)**  
  Authors: Shuojue Yang, Zijian Wu, Mingxuan Hong, Qian Li, Daiyun Shen, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04082v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, tracking, geometry, 3d gaussian, semantic  
- **[GaussianGraph: 3D Gaussian-based Scene Graph Generation for Open-world Scene Understanding](https://arxiv.org/abs/2503.04034v1)**  
  Authors: Xihan Wang, Dianyi Yang, Yu Gao, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04034v1.pdf)  
  Keywords: compression, understanding, ar, 3d gaussian, gaussian splatting, segmentation, dynamic, semantic  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: ar, efficient, nerf, gaussian splatting, human, neural rendering, few-shot, semantic  
- **[OpenGS-SLAM: Open-Set Dense Semantic SLAM with 3D Gaussian Splatting for Object-Level Scene Understanding](https://arxiv.org/abs/2503.01646v1)**  
  Authors: Dianyi Yang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01646v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://young-bit.github.io/opengs-github.github.io/.)  
  Keywords: slam, understanding, ar, gaussian splatting, segmentation, tracking, fast, mapping, 3d gaussian, semantic  
- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: ar, outdoor, gaussian splatting, semantic  
- **[Open-Vocabulary Semantic Part Segmentation of 3D Human](https://arxiv.org/abs/2502.19782v1)**  
  Authors: Keito Suzuki, Bang Du, Girish Krishnan, Kunyao Chen, Runfa Blark Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19782v1.pdf)  
  Keywords: ar, gaussian splatting, human, segmentation, vr, 3d gaussian, semantic  
- **[OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation](https://arxiv.org/abs/2502.18041v4)**  
  Authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.18041v4.pdf)  
  Keywords: ar, outdoor, gaussian splatting, segmentation, 3d gaussian, semantic  
- **[UniGS: Unified Language-Image-3D Pretraining with Gaussian Splatting](https://arxiv.org/abs/2502.17860v2)**  
  Authors: Haoyuan Li, Yanpeng Zhou, Tao Tang, Jifei Song, Yihan Zeng, Michael Kampffmeyer, Hang Xu, Xiaodan Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17860v2.pdf)  
  Keywords: ar, 3d gaussian, understanding, gaussian splatting  



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