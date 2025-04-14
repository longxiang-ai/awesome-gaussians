# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-04-14 00:54:57

## Categories

- [3DGS Surveys](#3dgs-surveys) (26 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (467 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1637 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (552 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (622 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (115 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (526 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (89 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (619 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (264 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (38 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (180 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (243 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (286 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: ar, lighting, dynamic, gaussian splatting, motion, 3d gaussian, fast, survey, 3d reconstruction  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: real-time rendering, dynamic, gaussian splatting, 3d gaussian, survey, ar  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: semantic, geometry, survey, ar  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: real-time rendering, compression, nerf, efficient, ar, gaussian splatting, 3d gaussian, survey, 3d reconstruction  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: 4d, nerf, lighting, dynamic, gaussian splatting, motion, deformation, survey, ar  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, gaussian splatting, 3d gaussian, survey, ar  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: outdoor, slam, survey, localization, tracking, geometry, dynamic, mapping, face, lighting, ar  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: recognition, gaussian splatting, 3d gaussian, illumination, survey, ar  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: robotics, autonomous driving, compact, nerf, ar, lighting, semantic, geometry, dynamic, gaussian splatting, high-fidelity, survey, 3d reconstruction  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: robotics, understanding, real-time rendering, nerf, gaussian splatting, 3d gaussian, survey, ar  

### Acceleration

*Showing the latest 50 out of 467 papers*

- **[View-Dependent Uncertainty Estimation of 3D Gaussian Splatting](https://arxiv.org/abs/2504.07370v1)**  
  Authors: Chenyu Han, Corentin Dumery  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07370v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, ar  
- **[SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2504.06815v1)**  
  Authors: Hanxiao Sun, YuPeng Gao, Jin Xie, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06815v1.pdf)  
  Keywords: relighting, real-time rendering, nerf, gaussian splatting, 3d gaussian, illumination, lighting, ar  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: robotics, efficient, ar, dynamic, gaussian splatting, fast, 3d reconstruction  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: efficient rendering, relighting, ray tracing, efficient, gaussian splatting, 3d gaussian, acceleration, lighting, ar  
- **[Micro-splatting: Maximizing Isotropic Constraints for Refined Optimization in 3D Gaussian Splatting](https://arxiv.org/abs/2504.05740v1)**  
  Authors: Jee Won Lee, Hansol Lim, Sooyeun Yang, Jongseong Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05740v1.pdf)  
  Keywords: real-time rendering, compact, ar, dynamic, gaussian splatting, 3d gaussian, 3d reconstruction  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: efficient rendering, efficient, ar, 3d gaussian, high quality, head  
- **[Let it Snow! Animating Static Gaussian Scenes With Dynamic Weather Effects](https://arxiv.org/abs/2504.05296v1)**  
  Authors: Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05296v1.pdf)  
  Keywords: dynamic, motion, gaussian splatting, 3d gaussian, fast, ar  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: compact, efficient, dynamic, gaussian splatting, animation, ray marching, 3d gaussian, acceleration, ar  
- **[Compressing 3D Gaussian Splatting by Noise-Substituted Vector Quantization](https://arxiv.org/abs/2504.03059v2)**  
  Authors: Haishan Wang, Mohammad Hassan Vali, Arno Solin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03059v2.pdf)  
  Keywords: compression, efficient, ar, gaussian splatting, 3d gaussian, fast, 3d reconstruction  
- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: slam, localization, tracking, dynamic, gaussian splatting, fast, mapping, 3d gaussian, face, ar  

### Applications

*Showing the latest 50 out of 1637 papers*

- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: avatar, ar, vr, shadow, human, geometry, dynamic, gaussian splatting, body, 3d gaussian, face, high-fidelity, head  
- **[View-Dependent Uncertainty Estimation of 3D Gaussian Splatting](https://arxiv.org/abs/2504.07370v1)**  
  Authors: Chenyu Han, Corentin Dumery  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07370v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, ar  
- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: human, mapping, 3d gaussian, deformation, ar  
- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: understanding, 3d reconstruction, nerf, ar, segmentation, gaussian splatting, 3d gaussian, head  
- **[IAAO: Interactive Affordance Learning for Articulated Objects in 3D Environments](https://arxiv.org/abs/2504.06827v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06827v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, understanding  
- **[SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2504.06815v1)**  
  Authors: Hanxiao Sun, YuPeng Gao, Jin Xie, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06815v1.pdf)  
  Keywords: relighting, real-time rendering, nerf, gaussian splatting, 3d gaussian, illumination, lighting, ar  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: robotics, efficient, ar, dynamic, gaussian splatting, fast, 3d reconstruction  
- **[Collision avoidance from monocular vision trained with novel view synthesis](https://arxiv.org/abs/2504.06651v1)**  
  Authors: Valentin Tordjman--Levavasseur, Stéphane Caron  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06651v1.pdf)  
  Keywords: motion, gaussian splatting, ar  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: efficient rendering, relighting, ray tracing, efficient, gaussian splatting, 3d gaussian, acceleration, lighting, ar  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: avatar, ar, human, sparse-view, body, 3d gaussian, head  

### Avatar Generation

*Showing the latest 50 out of 552 papers*

- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: avatar, ar, vr, shadow, human, geometry, dynamic, gaussian splatting, body, 3d gaussian, face, high-fidelity, head  
- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: human, mapping, 3d gaussian, deformation, ar  
- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: understanding, 3d reconstruction, nerf, ar, segmentation, gaussian splatting, 3d gaussian, head  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: avatar, ar, human, sparse-view, body, 3d gaussian, head  
- **[SE4Lip: Speech-Lip Encoder for Talking Head Synthesis to Solve Phoneme-Viseme Alignment Ambiguity](https://arxiv.org/abs/2504.05803v1)**  
  Authors: Yihuan Huang, Jiajun Liu, Yanzhen Ren, Wuyang Liu, Juhua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05803v1.pdf)  
  Keywords: nerf, ar, head  
- **[View-Dependent Deformation Fields for 2D Editing of 3D Models](https://arxiv.org/abs/2504.05544v1)**  
  Authors: Martin El Mqirmi, Noam Aigerman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05544v1.pdf)  
  Keywords: human, 3d gaussian, deformation, ar  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: efficient rendering, efficient, ar, 3d gaussian, high quality, head  
- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: efficient, ar, human, segmentation, dynamic, gaussian splatting, face, 3d reconstruction  
- **[Thermoxels: a voxel-based method to generate simulation-ready 3D thermal models](https://arxiv.org/abs/2504.04448v1)**  
  Authors: Etienne Chassaing, Florent Forest, Olga Fink, Malcolm Mielle  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04448v1.pdf)  
  Keywords: nerf, ar, geometry, gaussian splatting, face, 3d reconstruction  
- **[3R-GS: Best Practice in Optimizing Camera Poses Along with 3DGS](https://arxiv.org/abs/2504.04294v1)**  
  Authors: Zhisheng Huang, Peng Wang, Jingdong Zhang, Yuan Liu, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04294v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zsh523.github.io/3R-GS/)  
  Keywords: neural rendering, efficient, motion, gaussian splatting, 3d gaussian, face, ar  

### Dynamic Scene

*Showing the latest 50 out of 622 papers*

- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: avatar, ar, vr, shadow, human, geometry, dynamic, gaussian splatting, body, 3d gaussian, face, high-fidelity, head  
- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: human, mapping, 3d gaussian, deformation, ar  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: robotics, efficient, ar, dynamic, gaussian splatting, fast, 3d reconstruction  
- **[Collision avoidance from monocular vision trained with novel view synthesis](https://arxiv.org/abs/2504.06651v1)**  
  Authors: Valentin Tordjman--Levavasseur, Stéphane Caron  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06651v1.pdf)  
  Keywords: motion, gaussian splatting, ar  
- **[HiMoR: Monocular Deformable Gaussian Reconstruction with Hierarchical Motion Representation](https://arxiv.org/abs/2504.06210v1)**  
  Authors: Yiming Liang, Tianhan Xu, Yuta Kikuchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06210v1.pdf)  
  Keywords: ar, dynamic, motion, 3d gaussian, deformation, 3d reconstruction  
- **[Micro-splatting: Maximizing Isotropic Constraints for Refined Optimization in 3D Gaussian Splatting](https://arxiv.org/abs/2504.05740v1)**  
  Authors: Jee Won Lee, Hansol Lim, Sooyeun Yang, Jongseong Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05740v1.pdf)  
  Keywords: real-time rendering, compact, ar, dynamic, gaussian splatting, 3d gaussian, 3d reconstruction  
- **[View-Dependent Deformation Fields for 2D Editing of 3D Models](https://arxiv.org/abs/2504.05544v1)**  
  Authors: Martin El Mqirmi, Noam Aigerman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05544v1.pdf)  
  Keywords: human, 3d gaussian, deformation, ar  
- **[Let it Snow! Animating Static Gaussian Scenes With Dynamic Weather Effects](https://arxiv.org/abs/2504.05296v1)**  
  Authors: Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05296v1.pdf)  
  Keywords: dynamic, motion, gaussian splatting, 3d gaussian, fast, ar  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: compact, efficient, dynamic, gaussian splatting, animation, ray marching, 3d gaussian, acceleration, ar  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: 4d, slam, localization, tracking, dynamic, gaussian splatting, mapping, 3d gaussian, high-fidelity, ar  

### Few-shot

*Showing the latest 50 out of 115 papers*

- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: avatar, ar, human, sparse-view, body, 3d gaussian, head  
- **[DropGaussian: Structural Regularization for Sparse-view Gaussian Splatting](https://arxiv.org/abs/2504.00773v1)**  
  Authors: Hyunwoo Park, Gun Ryu, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DCVL-3D/DropGaussian?style=social)](https://github.com/DCVL-3D/DropGaussian)  
  Keywords: gaussian splatting, sparse-view, fast, 3d gaussian, face, ar  
- **[Coca-Splat: Collaborative Optimization for Camera Parameters and 3D Gaussians](https://arxiv.org/abs/2504.00639v1)**  
  Authors: Jiamin Wu, Hongyang Li, Xiaoke Jiang, Yuan Yao, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00639v1.pdf)  
  Keywords: sparse view, 3d gaussian, ar  
- **[Distilling Multi-view Diffusion Models into 3D Generators](https://arxiv.org/abs/2504.00457v3)**  
  Authors: Hao Qin, Luyuan Chen, Ming Kong, Mengxu Lu, Qiang Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00457v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://qinbaigao.github.io/DD3G_project/)  
  Keywords: efficient, gaussian splatting, sparse-view, 3d gaussian, ar  
- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: neural rendering, ar, geometry, gaussian splatting, sparse-view, face, 3d reconstruction  
- **[FreeSplat++: Generalizable 3D Gaussian Splatting for Efficient Indoor Scene Reconstruction](https://arxiv.org/abs/2503.22986v1)**  
  Authors: Yunsong Wang, Tianxin Huang, Hanlin Chen, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22986v1.pdf)  
  Keywords: sparse view, efficient, gaussian splatting, 3d gaussian, ar  
- **[CoMapGS: Covisibility Map-based Gaussian Splatting for Sparse Novel View Synthesis](https://arxiv.org/abs/2503.20998v1)**  
  Authors: Youngkyoon Jang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20998v1.pdf)  
  Keywords: nerf, few-shot, gaussian splatting, ar  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: outdoor, gaussian splatting, sparse-view, 3d gaussian, illumination, ar  
- **[NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting](https://arxiv.org/abs/2503.18794v1)**  
  Authors: Yulong Zheng, Zicheng Jiang, Shengfeng He, Yandu Sun, Junyu Dong, Huaidong Zhang, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18794v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://usmizuki.github.io/NexusGS/.)  
  Keywords: sparse view, nerf, geometry, few-shot, gaussian splatting, sparse-view, 3d gaussian, ar  
- **[SplatVoxel: History-Aware Novel View Streaming without Temporal Training](https://arxiv.org/abs/2503.14698v1)**  
  Authors: Yiming Wang, Lucy Chai, Xuan Luo, Michael Niemeyer, Manuel Lagunas, Stephen Lombardi, Siyu Tang, Tiancheng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14698v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://19reborn.github.io/SplatVoxel/)  
  Keywords: efficient, tracking, motion, gaussian splatting, sparse-view, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 526 papers*

- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: avatar, ar, vr, shadow, human, geometry, dynamic, gaussian splatting, body, 3d gaussian, face, high-fidelity, head  
- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: understanding, 3d reconstruction, nerf, ar, segmentation, gaussian splatting, 3d gaussian, head  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: robotics, efficient, ar, dynamic, gaussian splatting, fast, 3d reconstruction  
- **[HiMoR: Monocular Deformable Gaussian Reconstruction with Hierarchical Motion Representation](https://arxiv.org/abs/2504.06210v1)**  
  Authors: Yiming Liang, Tianhan Xu, Yuta Kikuchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06210v1.pdf)  
  Keywords: ar, dynamic, motion, 3d gaussian, deformation, 3d reconstruction  
- **[Micro-splatting: Maximizing Isotropic Constraints for Refined Optimization in 3D Gaussian Splatting](https://arxiv.org/abs/2504.05740v1)**  
  Authors: Jee Won Lee, Hansol Lim, Sooyeun Yang, Jongseong Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05740v1.pdf)  
  Keywords: real-time rendering, compact, ar, dynamic, gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: efficient, ar, human, segmentation, dynamic, gaussian splatting, face, 3d reconstruction  
- **[Targetless LiDAR-Camera Calibration with Anchored 3D Gaussians](https://arxiv.org/abs/2504.04597v1)**  
  Authors: Haebeom Jung, Namtae Kim, Jungwoo Kim, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04597v1.pdf)  
  Keywords: geometry, 3d gaussian, autonomous driving, ar  
- **[Thermoxels: a voxel-based method to generate simulation-ready 3D thermal models](https://arxiv.org/abs/2504.04448v1)**  
  Authors: Etienne Chassaing, Florent Forest, Olga Fink, Malcolm Mielle  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04448v1.pdf)  
  Keywords: nerf, ar, geometry, gaussian splatting, face, 3d reconstruction  
- **[Interpretable Single-View 3D Gaussian Splatting using Unsupervised Hierarchical Disentangled Representation Learning](https://arxiv.org/abs/2504.04190v1)**  
  Authors: Yuyang Zhang, Baao Xie, Hu Zhu, Qi Wang, Huanting Guo, Xin Jin, Wenjun Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04190v1.pdf)  
  Keywords: understanding, ar, geometry, gaussian splatting, 3d gaussian, semantic, 3d reconstruction  
- **[HumanDreamer-X: Photorealistic Single-image Human Avatars Reconstruction via Gaussian Restoration](https://arxiv.org/abs/2504.03536v1)**  
  Authors: Boyuan Wang, Runqi Ouyang, Xiaofeng Wang, Zheng Zhu, Guosheng Zhao, Chaojun Ni, Guan Huang, Lihong Liu, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03536v1.pdf)  
  Keywords: avatar, ar, human, geometry, gaussian splatting, animation, 3d gaussian, 3d reconstruction  

### Large Scene

*Showing the latest 50 out of 89 papers*

- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: reflection, nerf, outdoor, motion, gaussian splatting, ar  
- **[UnIRe: Unsupervised Instance Decomposition for Dynamic Urban Scene Reconstruction](https://arxiv.org/abs/2504.00763v1)**  
  Authors: Yunxuan Mao, Rong Xiong, Yue Wang, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00763v1.pdf)  
  Keywords: 4d, urban scene, dynamic, gaussian splatting, 3d gaussian, autonomous driving, ar  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: reflection, nerf, efficient, outdoor, geometry, dynamic, gaussian splatting, fast, high-fidelity, ar  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: urban scene, geometry, dynamic, motion, gaussian splatting, ar  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: real-time rendering, nerf, urban scene, efficient, gaussian splatting, 3d gaussian, fast, autonomous driving, ar  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: outdoor, gaussian splatting, sparse-view, 3d gaussian, illumination, ar  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: efficient, outdoor, localization, gaussian splatting, ar  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: real-time rendering, efficient, outdoor, geometry, gaussian splatting, 3d gaussian, fast, ar  
- **[PanopticSplatting: End-to-End Panoptic Gaussian Splatting](https://arxiv.org/abs/2503.18073v1)**  
  Authors: Yuxuan Xie, Xuan Yu, Changjian Jiang, Sitong Mao, Shunbo Zhou, Rui Fan, Rong Xiong, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18073v1.pdf)  
  Keywords: understanding, nerf, segmentation, gaussian splatting, large scene, ar  
- **[GaussianFocus: Constrained Attention Focus for 3D Gaussian Splatting](https://arxiv.org/abs/2503.17798v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17798v1.pdf)  
  Keywords: neural rendering, ar, gaussian splatting, 3d gaussian, large scene, 3d reconstruction  

### Model Compression

*Showing the latest 50 out of 619 papers*

- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: robotics, efficient, ar, dynamic, gaussian splatting, fast, 3d reconstruction  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: efficient rendering, relighting, ray tracing, efficient, gaussian splatting, 3d gaussian, acceleration, lighting, ar  
- **[econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians](https://arxiv.org/abs/2504.06003v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06003v1.pdf)  
  Keywords: segmentation, efficient, semantic, ar  
- **[Micro-splatting: Maximizing Isotropic Constraints for Refined Optimization in 3D Gaussian Splatting](https://arxiv.org/abs/2504.05740v1)**  
  Authors: Jee Won Lee, Hansol Lim, Sooyeun Yang, Jongseong Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05740v1.pdf)  
  Keywords: real-time rendering, compact, ar, dynamic, gaussian splatting, 3d gaussian, 3d reconstruction  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: efficient rendering, efficient, ar, 3d gaussian, high quality, head  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: compact, efficient, dynamic, gaussian splatting, animation, ray marching, 3d gaussian, acceleration, ar  
- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: efficient, ar, human, segmentation, dynamic, gaussian splatting, face, 3d reconstruction  
- **[3R-GS: Best Practice in Optimizing Camera Poses Along with 3DGS](https://arxiv.org/abs/2504.04294v1)**  
  Authors: Zhisheng Huang, Peng Wang, Jingdong Zhang, Yuan Liu, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04294v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zsh523.github.io/3R-GS/)  
  Keywords: neural rendering, efficient, motion, gaussian splatting, 3d gaussian, face, ar  
- **[WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2504.03886v1)**  
  Authors: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys, Songyou Peng, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03886v1.pdf)  
  Keywords: efficient, slam, tracking, dynamic, gaussian splatting, mapping, ar  
- **[Compressing 3D Gaussian Splatting by Noise-Substituted Vector Quantization](https://arxiv.org/abs/2504.03059v2)**  
  Authors: Haishan Wang, Mohammad Hassan Vali, Arno Solin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03059v2.pdf)  
  Keywords: compression, efficient, ar, gaussian splatting, 3d gaussian, fast, 3d reconstruction  

### Quality Enhancement

*Showing the latest 50 out of 264 papers*

- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: avatar, ar, vr, shadow, human, geometry, dynamic, gaussian splatting, body, 3d gaussian, face, high-fidelity, head  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: efficient rendering, efficient, ar, 3d gaussian, high quality, head  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: 4d, slam, localization, tracking, dynamic, gaussian splatting, mapping, 3d gaussian, high-fidelity, ar  
- **[UAVTwin: Neural Digital Twins for UAVs using Gaussian Splatting](https://arxiv.org/abs/2504.02158v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02158v1.pdf)  
  Keywords: neural rendering, human, dynamic, gaussian splatting, motion, 3d gaussian, high-fidelity, high quality, ar  
- **[BOGausS: Better Optimized Gaussian Splatting](https://arxiv.org/abs/2504.01844v1)**  
  Authors: Stéphane Pateux, Matthieu Gendrin, Luce Morin, Théo Ladune, Xiaoran Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01844v1.pdf)  
  Keywords: nerf, efficient, gaussian splatting, 3d gaussian, fast, high-fidelity, ar  
- **[RealityAvatar: Towards Realistic Loose Clothing Modeling in Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2504.01559v1)**  
  Authors: Yahui Li, Zhi Zeng, Liming Pang, Guixuan Zhang, Shuwu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01559v1.pdf)  
  Keywords: nerf, efficient, avatar, human, dynamic, gaussian splatting, motion, 3d gaussian, deformation, high-fidelity, ar  
- **[High-fidelity 3D Object Generation from Single Image with RGBN-Volume Gaussian Reconstruction Model](https://arxiv.org/abs/2504.01512v1)**  
  Authors: Yiyang Shen, Kun Zhou, He Wang, Yin Yang, Tianjia Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01512v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, face, high-fidelity, ar  
- **[ExScene: Free-View 3D Scene Reconstruction with Gaussian Splatting from a Single Image](https://arxiv.org/abs/2503.23881v1)**  
  Authors: Tianyi Gong, Boyan Li, Yifei Zhong, Fangxin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23881v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, ar  
- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: 4d, face, dynamic, motion, gaussian splatting, deformation, high-fidelity, ar  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: reflection, nerf, efficient, outdoor, geometry, dynamic, gaussian splatting, fast, high-fidelity, ar  

### Ray Tracing

- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: efficient rendering, relighting, ray tracing, efficient, gaussian splatting, 3d gaussian, acceleration, lighting, ar  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: compact, efficient, dynamic, gaussian splatting, animation, ray marching, 3d gaussian, acceleration, ar  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: real-time rendering, ray tracing, efficient, global illumination, gaussian splatting, 3d gaussian, face, illumination, lighting, ar  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: real-time rendering, light transport, face, global illumination, dynamic, 3d gaussian, fast, illumination, lighting  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: neural rendering, ray tracing, reflection, shadow, gaussian splatting, 3d gaussian, fast, ar  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: real-time rendering, 4d, relightable, ray tracing, efficient, tracking, geometry, dynamic, face, lighting, ar  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: ray tracing, reflection, shadow, gaussian splatting, face, lighting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, gaussian splatting, 3d gaussian, survey, ar  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: light transport, ray tracing, reflection, efficient, gaussian splatting, acceleration, ar  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: ray tracing, reflection, shadow, gaussian splatting, 3d gaussian, ar  

### Relighting

*Showing the latest 50 out of 180 papers*

- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: avatar, ar, vr, shadow, human, geometry, dynamic, gaussian splatting, body, 3d gaussian, face, high-fidelity, head  
- **[SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2504.06815v1)**  
  Authors: Hanxiao Sun, YuPeng Gao, Jin Xie, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06815v1.pdf)  
  Keywords: relighting, real-time rendering, nerf, gaussian splatting, 3d gaussian, illumination, lighting, ar  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: efficient rendering, relighting, ray tracing, efficient, gaussian splatting, 3d gaussian, acceleration, lighting, ar  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: reflection, nerf, outdoor, motion, gaussian splatting, ar  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: real-time rendering, nerf, gaussian splatting, mapping, 3d gaussian, lighting, ar  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: real-time rendering, ray tracing, efficient, global illumination, gaussian splatting, 3d gaussian, face, illumination, lighting, ar  
- **[LITA-GS: Illumination-Agnostic Novel View Synthesis via Reference-Free 3D Gaussian Splatting and Physical Priors](https://arxiv.org/abs/2504.00219v1)**  
  Authors: Han Zhou, Wei Dong, Jun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00219v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LowLevelAI/LITA-GS?style=social)](https://github.com/LowLevelAI/LITA-GS)  
  Keywords: nerf, gaussian splatting, motion, 3d gaussian, fast, illumination, lighting, ar  
- **[Learning 3D-Gaussian Simulators from RGB Videos](https://arxiv.org/abs/2503.24009v1)**  
  Authors: Mikel Zhobro, Andreas René Geist, Georg Martius  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24009v1.pdf)  
  Keywords: dynamic, gaussian splatting, body, 3d gaussian, lighting, ar  
- **[TranSplat: Lighting-Consistent Cross-Scene Object Transfer with 3D Gaussian Splatting](https://arxiv.org/abs/2503.22676v1)**  
  Authors: Boyang, Yu, Yanlin Jin, Ashok Veeraraghavan, Akshat Dave, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22676v1.pdf)  
  Keywords: relighting, segmentation, gaussian splatting, 3d gaussian, lighting, ar  
- **[Follow Your Motion: A Generic Temporal Consistency Portrait Editing Framework with Trajectory Guidance](https://arxiv.org/abs/2503.22225v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22225v1.pdf)  
  Keywords: relighting, efficient, avatar, ar, dynamic, gaussian splatting, motion, 3d gaussian, face, lighting, head  

### SLAM

*Showing the latest 50 out of 243 papers*

- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: human, mapping, 3d gaussian, deformation, ar  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: 4d, slam, localization, tracking, dynamic, gaussian splatting, mapping, 3d gaussian, high-fidelity, ar  
- **[WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2504.03886v1)**  
  Authors: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys, Songyou Peng, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03886v1.pdf)  
  Keywords: efficient, slam, tracking, dynamic, gaussian splatting, mapping, ar  
- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: slam, localization, tracking, dynamic, gaussian splatting, fast, mapping, 3d gaussian, face, ar  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: real-time rendering, nerf, gaussian splatting, mapping, 3d gaussian, lighting, ar  
- **[Visual Acoustic Fields](https://arxiv.org/abs/2503.24270v2)**  
  Authors: Yuelei Li, Hyunjin Kim, Fangneng Zhan, Ri-Zhao Qiu, Mazeyu Ji, Xiaojun Shan, Xueyan Zou, Paul Liang, Hanspeter Pfister, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24270v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuelei0428.github.io/projects/Visual-Acoustic-Fields/.)  
  Keywords: localization, human, gaussian splatting, 3d gaussian, ar  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: robotics, understanding, localization, segmentation, gaussian splatting, 3d gaussian, semantic, ar  
- **[VizFlyt: Perception-centric Pedagogical Framework For Autonomous Aerial Robots](https://arxiv.org/abs/2503.22876v2)**  
  Authors: Kushagra Srivastava, Rutwik Kulkarni, Manoj Velmurugan, Nitin J. Sanket  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22876v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pear.wpi.edu/research/vizflyt.html)  
  Keywords: robotics, efficient, localization, gaussian splatting, 3d gaussian, ar  
- **[Time-resolved dynamic CBCT reconstruction using prior-model-free spatiotemporal Gaussian representation (PMF-STGR)](https://arxiv.org/abs/2503.22139v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22139v1.pdf)  
  Keywords: efficient, localization, dynamic, motion, fast, 3d gaussian, deformation, ar  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: robotics, slam, localization, dynamic, mapping, 3d gaussian, high-fidelity, semantic, ar  

### Scene Understanding

*Showing the latest 50 out of 286 papers*

- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: understanding, 3d reconstruction, nerf, ar, segmentation, gaussian splatting, 3d gaussian, head  
- **[IAAO: Interactive Affordance Learning for Articulated Objects in 3D Environments](https://arxiv.org/abs/2504.06827v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06827v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, understanding  
- **[econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians](https://arxiv.org/abs/2504.06003v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06003v1.pdf)  
  Keywords: segmentation, efficient, semantic, ar  
- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: efficient, ar, human, segmentation, dynamic, gaussian splatting, face, 3d reconstruction  
- **[Interpretable Single-View 3D Gaussian Splatting using Unsupervised Hierarchical Disentangled Representation Learning](https://arxiv.org/abs/2504.04190v1)**  
  Authors: Yuyang Zhang, Baao Xie, Hu Zhu, Qi Wang, Huanting Guo, Xin Jin, Wenjun Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04190v1.pdf)  
  Keywords: understanding, ar, geometry, gaussian splatting, 3d gaussian, semantic, 3d reconstruction  
- **[Scene4U: Hierarchical Layered 3D Scene Reconstruction from Single Panoramic Image for Your Immerse Exploration](https://arxiv.org/abs/2504.00387v1)**  
  Authors: Zilong Huang, Jun He, Junyan Ye, Lihan Jiang, Weijia Li, Yiping Chen, Ting Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00387v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LongHZ140516/Scene4U?style=social)](https://github.com/LongHZ140516/Scene4U)  
  Keywords: segmentation, dynamic, gaussian splatting, 3d gaussian, fast, semantic, ar  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: robotics, understanding, localization, segmentation, gaussian splatting, 3d gaussian, semantic, ar  
- **[TranSplat: Lighting-Consistent Cross-Scene Object Transfer with 3D Gaussian Splatting](https://arxiv.org/abs/2503.22676v1)**  
  Authors: Boyang, Yu, Yanlin Jin, Ashok Veeraraghavan, Akshat Dave, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22676v1.pdf)  
  Keywords: relighting, segmentation, gaussian splatting, 3d gaussian, lighting, ar  
- **[ABC-GS: Alignment-Based Controllable Style Transfer for 3D Gaussian Splatting](https://arxiv.org/abs/2503.22218v1)**  
  Authors: Wenjie Liu, Zhongliang Liu, Xiaoyan Yang, Man Sha, Yang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22218v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vpx-ecnu.github.io/ABC-GS-website.)  
  Keywords: nerf, segmentation, gaussian splatting, 3d gaussian, ar  
- **[Segment then Splat: A Unified Approach for 3D Open-Vocabulary Segmentation based on Gaussian Splatting](https://arxiv.org/abs/2503.22204v1)**  
  Authors: Yiren Lu, Yunlai Zhou, Yiran Qiao, Chaoda Song, Tuo Liang, Jing Ma, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22204v1.pdf)  
  Keywords: robotics, segmentation, dynamic, motion, gaussian splatting, ar  



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