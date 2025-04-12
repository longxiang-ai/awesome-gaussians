# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-04-12 00:51:15

## Categories

- [3DGS Surveys](#3dgs-surveys) (26 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (467 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1637 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (553 papers) - Papers about human avatar generation
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
  Keywords: lighting, fast, gaussian splatting, 3d reconstruction, motion, ar, 3d gaussian, dynamic, survey  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, real-time rendering, dynamic, survey  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: semantic, ar, survey, geometry  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: compression, gaussian splatting, efficient, 3d reconstruction, ar, 3d gaussian, real-time rendering, nerf, survey  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: lighting, 4d, gaussian splatting, motion, ar, dynamic, deformation, nerf, survey  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, gaussian splatting, ar, 3d gaussian, survey  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: localization, lighting, mapping, survey, face, tracking, slam, geometry, ar, dynamic, outdoor  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: recognition, illumination, gaussian splatting, ar, 3d gaussian, survey  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: semantic, lighting, autonomous driving, nerf, gaussian splatting, 3d reconstruction, geometry, ar, robotics, compact, dynamic, high-fidelity, survey  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: robotics, understanding, gaussian splatting, ar, 3d gaussian, real-time rendering, nerf, survey  

### Acceleration

*Showing the latest 50 out of 467 papers*

- **[View-Dependent Uncertainty Estimation of 3D Gaussian Splatting](https://arxiv.org/abs/2504.07370v1)**  
  Authors: Chenyu Han, Corentin Dumery  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07370v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, fast  
- **[SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2504.06815v1)**  
  Authors: Hanxiao Sun, YuPeng Gao, Jin Xie, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06815v1.pdf)  
  Keywords: lighting, relighting, illumination, gaussian splatting, ar, 3d gaussian, real-time rendering, nerf  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: fast, gaussian splatting, efficient, 3d reconstruction, ar, robotics, dynamic  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: lighting, relighting, ray tracing, ar, gaussian splatting, efficient, efficient rendering, 3d gaussian, acceleration  
- **[Micro-splatting: Maximizing Isotropic Constraints for Refined Optimization in 3D Gaussian Splatting](https://arxiv.org/abs/2504.05740v1)**  
  Authors: Jee Won Lee, Hansol Lim, Sooyeun Yang, Jongseong Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05740v1.pdf)  
  Keywords: compact, gaussian splatting, 3d reconstruction, ar, 3d gaussian, real-time rendering, dynamic  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: head, ar, efficient, high quality, efficient rendering, 3d gaussian  
- **[Let it Snow! Animating Static Gaussian Scenes With Dynamic Weather Effects](https://arxiv.org/abs/2504.05296v1)**  
  Authors: Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05296v1.pdf)  
  Keywords: fast, gaussian splatting, motion, ar, 3d gaussian, dynamic  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: ray marching, dynamic, animation, gaussian splatting, efficient, ar, 3d gaussian, compact, acceleration  
- **[Compressing 3D Gaussian Splatting by Noise-Substituted Vector Quantization](https://arxiv.org/abs/2504.03059v2)**  
  Authors: Haishan Wang, Mohammad Hassan Vali, Arno Solin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03059v2.pdf)  
  Keywords: fast, compression, gaussian splatting, efficient, 3d reconstruction, ar, 3d gaussian  
- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: localization, mapping, fast, face, tracking, gaussian splatting, slam, ar, 3d gaussian, dynamic  

### Applications

*Showing the latest 50 out of 1637 papers*

- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: shadow, avatar, head, face, vr, gaussian splatting, body, geometry, ar, 3d gaussian, dynamic, human, high-fidelity  
- **[View-Dependent Uncertainty Estimation of 3D Gaussian Splatting](https://arxiv.org/abs/2504.07370v1)**  
  Authors: Chenyu Han, Corentin Dumery  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07370v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, fast  
- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: mapping, deformation, ar, 3d gaussian, human  
- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: segmentation, head, understanding, gaussian splatting, 3d reconstruction, ar, 3d gaussian, nerf  
- **[IAAO: Interactive Affordance Learning for Articulated Objects in 3D Environments](https://arxiv.org/abs/2504.06827v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06827v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, understanding  
- **[SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2504.06815v1)**  
  Authors: Hanxiao Sun, YuPeng Gao, Jin Xie, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06815v1.pdf)  
  Keywords: lighting, relighting, illumination, gaussian splatting, ar, 3d gaussian, real-time rendering, nerf  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: fast, gaussian splatting, efficient, 3d reconstruction, ar, robotics, dynamic  
- **[Collision avoidance from monocular vision trained with novel view synthesis](https://arxiv.org/abs/2504.06651v1)**  
  Authors: Valentin Tordjman--Levavasseur, Stéphane Caron  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06651v1.pdf)  
  Keywords: ar, gaussian splatting, motion  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: lighting, relighting, ray tracing, ar, gaussian splatting, efficient, efficient rendering, 3d gaussian, acceleration  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: avatar, head, body, sparse-view, ar, 3d gaussian, human  

### Avatar Generation

*Showing the latest 50 out of 553 papers*

- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: shadow, avatar, head, face, vr, gaussian splatting, body, geometry, ar, 3d gaussian, dynamic, human, high-fidelity  
- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: mapping, deformation, ar, 3d gaussian, human  
- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: segmentation, head, understanding, gaussian splatting, 3d reconstruction, ar, 3d gaussian, nerf  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: avatar, head, body, sparse-view, ar, 3d gaussian, human  
- **[SE4Lip: Speech-Lip Encoder for Talking Head Synthesis to Solve Phoneme-Viseme Alignment Ambiguity](https://arxiv.org/abs/2504.05803v1)**  
  Authors: Yihuan Huang, Jiajun Liu, Yanzhen Ren, Wuyang Liu, Juhua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05803v1.pdf)  
  Keywords: ar, head, nerf  
- **[View-Dependent Deformation Fields for 2D Editing of 3D Models](https://arxiv.org/abs/2504.05544v1)**  
  Authors: Martin El Mqirmi, Noam Aigerman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05544v1.pdf)  
  Keywords: human, 3d gaussian, deformation, ar  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: head, ar, efficient, high quality, efficient rendering, 3d gaussian  
- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: segmentation, face, gaussian splatting, efficient, 3d reconstruction, ar, dynamic, human  
- **[Thermoxels: a voxel-based method to generate simulation-ready 3D thermal models](https://arxiv.org/abs/2504.04448v1)**  
  Authors: Etienne Chassaing, Florent Forest, Olga Fink, Malcolm Mielle  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04448v1.pdf)  
  Keywords: face, gaussian splatting, 3d reconstruction, geometry, ar, nerf  
- **[3R-GS: Best Practice in Optimizing Camera Poses Along with 3DGS](https://arxiv.org/abs/2504.04294v1)**  
  Authors: Zhisheng Huang, Peng Wang, Jingdong Zhang, Yuan Liu, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04294v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zsh523.github.io/3R-GS/)  
  Keywords: face, gaussian splatting, efficient, motion, ar, 3d gaussian, neural rendering  

### Dynamic Scene

*Showing the latest 50 out of 622 papers*

- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: shadow, avatar, head, face, vr, gaussian splatting, body, geometry, ar, 3d gaussian, dynamic, human, high-fidelity  
- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: mapping, deformation, ar, 3d gaussian, human  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: fast, gaussian splatting, efficient, 3d reconstruction, ar, robotics, dynamic  
- **[Collision avoidance from monocular vision trained with novel view synthesis](https://arxiv.org/abs/2504.06651v1)**  
  Authors: Valentin Tordjman--Levavasseur, Stéphane Caron  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06651v1.pdf)  
  Keywords: ar, gaussian splatting, motion  
- **[HiMoR: Monocular Deformable Gaussian Reconstruction with Hierarchical Motion Representation](https://arxiv.org/abs/2504.06210v1)**  
  Authors: Yiming Liang, Tianhan Xu, Yuta Kikuchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06210v1.pdf)  
  Keywords: 3d reconstruction, motion, ar, 3d gaussian, dynamic, deformation  
- **[Micro-splatting: Maximizing Isotropic Constraints for Refined Optimization in 3D Gaussian Splatting](https://arxiv.org/abs/2504.05740v1)**  
  Authors: Jee Won Lee, Hansol Lim, Sooyeun Yang, Jongseong Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05740v1.pdf)  
  Keywords: compact, gaussian splatting, 3d reconstruction, ar, 3d gaussian, real-time rendering, dynamic  
- **[View-Dependent Deformation Fields for 2D Editing of 3D Models](https://arxiv.org/abs/2504.05544v1)**  
  Authors: Martin El Mqirmi, Noam Aigerman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05544v1.pdf)  
  Keywords: human, 3d gaussian, deformation, ar  
- **[Let it Snow! Animating Static Gaussian Scenes With Dynamic Weather Effects](https://arxiv.org/abs/2504.05296v1)**  
  Authors: Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05296v1.pdf)  
  Keywords: fast, gaussian splatting, motion, ar, 3d gaussian, dynamic  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: ray marching, dynamic, animation, gaussian splatting, efficient, ar, 3d gaussian, compact, acceleration  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: localization, dynamic, mapping, tracking, gaussian splatting, slam, ar, 3d gaussian, 4d, high-fidelity  

### Few-shot

*Showing the latest 50 out of 115 papers*

- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: avatar, head, body, sparse-view, ar, 3d gaussian, human  
- **[DropGaussian: Structural Regularization for Sparse-view Gaussian Splatting](https://arxiv.org/abs/2504.00773v1)**  
  Authors: Hyunwoo Park, Gun Ryu, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DCVL-3D/DropGaussian?style=social)](https://github.com/DCVL-3D/DropGaussian)  
  Keywords: fast, face, gaussian splatting, sparse-view, ar, 3d gaussian  
- **[Coca-Splat: Collaborative Optimization for Camera Parameters and 3D Gaussians](https://arxiv.org/abs/2504.00639v1)**  
  Authors: Jiamin Wu, Hongyang Li, Xiaoke Jiang, Yuan Yao, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00639v1.pdf)  
  Keywords: ar, 3d gaussian, sparse view  
- **[Distilling Multi-view Diffusion Models into 3D Generators](https://arxiv.org/abs/2504.00457v3)**  
  Authors: Hao Qin, Luyuan Chen, Ming Kong, Mengxu Lu, Qiang Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00457v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://qinbaigao.github.io/DD3G_project/)  
  Keywords: gaussian splatting, efficient, sparse-view, ar, 3d gaussian  
- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: face, gaussian splatting, sparse-view, 3d reconstruction, ar, neural rendering, geometry  
- **[FreeSplat++: Generalizable 3D Gaussian Splatting for Efficient Indoor Scene Reconstruction](https://arxiv.org/abs/2503.22986v1)**  
  Authors: Yunsong Wang, Tianxin Huang, Hanlin Chen, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22986v1.pdf)  
  Keywords: sparse view, gaussian splatting, efficient, ar, 3d gaussian  
- **[CoMapGS: Covisibility Map-based Gaussian Splatting for Sparse Novel View Synthesis](https://arxiv.org/abs/2503.20998v1)**  
  Authors: Youngkyoon Jang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20998v1.pdf)  
  Keywords: few-shot, gaussian splatting, nerf, ar  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: illumination, gaussian splatting, sparse-view, ar, 3d gaussian, outdoor  
- **[NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting](https://arxiv.org/abs/2503.18794v1)**  
  Authors: Yulong Zheng, Zicheng Jiang, Shengfeng He, Yandu Sun, Junyu Dong, Huaidong Zhang, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18794v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://usmizuki.github.io/NexusGS/.)  
  Keywords: ar, sparse view, gaussian splatting, sparse-view, geometry, few-shot, 3d gaussian, nerf  
- **[SplatVoxel: History-Aware Novel View Streaming without Temporal Training](https://arxiv.org/abs/2503.14698v1)**  
  Authors: Yiming Wang, Lucy Chai, Xuan Luo, Michael Niemeyer, Manuel Lagunas, Stephen Lombardi, Siyu Tang, Tiancheng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14698v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://19reborn.github.io/SplatVoxel/)  
  Keywords: tracking, gaussian splatting, efficient, sparse-view, motion, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 526 papers*

- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: shadow, avatar, head, face, vr, gaussian splatting, body, geometry, ar, 3d gaussian, dynamic, human, high-fidelity  
- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: segmentation, head, understanding, gaussian splatting, 3d reconstruction, ar, 3d gaussian, nerf  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: fast, gaussian splatting, efficient, 3d reconstruction, ar, robotics, dynamic  
- **[HiMoR: Monocular Deformable Gaussian Reconstruction with Hierarchical Motion Representation](https://arxiv.org/abs/2504.06210v1)**  
  Authors: Yiming Liang, Tianhan Xu, Yuta Kikuchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06210v1.pdf)  
  Keywords: 3d reconstruction, motion, ar, 3d gaussian, dynamic, deformation  
- **[Micro-splatting: Maximizing Isotropic Constraints for Refined Optimization in 3D Gaussian Splatting](https://arxiv.org/abs/2504.05740v1)**  
  Authors: Jee Won Lee, Hansol Lim, Sooyeun Yang, Jongseong Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05740v1.pdf)  
  Keywords: compact, gaussian splatting, 3d reconstruction, ar, 3d gaussian, real-time rendering, dynamic  
- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: segmentation, face, gaussian splatting, efficient, 3d reconstruction, ar, dynamic, human  
- **[Targetless LiDAR-Camera Calibration with Anchored 3D Gaussians](https://arxiv.org/abs/2504.04597v1)**  
  Authors: Haebeom Jung, Namtae Kim, Jungwoo Kim, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04597v1.pdf)  
  Keywords: ar, 3d gaussian, autonomous driving, geometry  
- **[Thermoxels: a voxel-based method to generate simulation-ready 3D thermal models](https://arxiv.org/abs/2504.04448v1)**  
  Authors: Etienne Chassaing, Florent Forest, Olga Fink, Malcolm Mielle  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04448v1.pdf)  
  Keywords: face, gaussian splatting, 3d reconstruction, geometry, ar, nerf  
- **[Interpretable Single-View 3D Gaussian Splatting using Unsupervised Hierarchical Disentangled Representation Learning](https://arxiv.org/abs/2504.04190v1)**  
  Authors: Yuyang Zhang, Baao Xie, Hu Zhu, Qi Wang, Huanting Guo, Xin Jin, Wenjun Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04190v1.pdf)  
  Keywords: semantic, understanding, gaussian splatting, 3d reconstruction, geometry, ar, 3d gaussian  
- **[HumanDreamer-X: Photorealistic Single-image Human Avatars Reconstruction via Gaussian Restoration](https://arxiv.org/abs/2504.03536v1)**  
  Authors: Boyuan Wang, Runqi Ouyang, Xiaofeng Wang, Zheng Zhu, Guosheng Zhao, Chaojun Ni, Guan Huang, Lihong Liu, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03536v1.pdf)  
  Keywords: avatar, animation, gaussian splatting, 3d reconstruction, geometry, ar, 3d gaussian, human  

### Large Scene

*Showing the latest 50 out of 89 papers*

- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: gaussian splatting, motion, ar, reflection, nerf, outdoor  
- **[UnIRe: Unsupervised Instance Decomposition for Dynamic Urban Scene Reconstruction](https://arxiv.org/abs/2504.00763v1)**  
  Authors: Yunxuan Mao, Rong Xiong, Yue Wang, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00763v1.pdf)  
  Keywords: dynamic, autonomous driving, urban scene, gaussian splatting, ar, 3d gaussian, 4d  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: fast, nerf, gaussian splatting, efficient, geometry, ar, reflection, dynamic, high-fidelity, outdoor  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: urban scene, gaussian splatting, motion, geometry, ar, dynamic  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: autonomous driving, fast, urban scene, gaussian splatting, efficient, ar, 3d gaussian, real-time rendering, nerf  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: illumination, gaussian splatting, sparse-view, ar, 3d gaussian, outdoor  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: localization, gaussian splatting, efficient, ar, outdoor  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: fast, gaussian splatting, efficient, geometry, ar, 3d gaussian, real-time rendering, outdoor  
- **[PanopticSplatting: End-to-End Panoptic Gaussian Splatting](https://arxiv.org/abs/2503.18073v1)**  
  Authors: Yuxuan Xie, Xuan Yu, Changjian Jiang, Sitong Mao, Shunbo Zhou, Rui Fan, Rong Xiong, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18073v1.pdf)  
  Keywords: segmentation, understanding, gaussian splatting, large scene, ar, nerf  
- **[GaussianFocus: Constrained Attention Focus for 3D Gaussian Splatting](https://arxiv.org/abs/2503.17798v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17798v1.pdf)  
  Keywords: gaussian splatting, large scene, 3d reconstruction, ar, 3d gaussian, neural rendering  

### Model Compression

*Showing the latest 50 out of 619 papers*

- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: fast, gaussian splatting, efficient, 3d reconstruction, ar, robotics, dynamic  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: lighting, relighting, ray tracing, ar, gaussian splatting, efficient, efficient rendering, 3d gaussian, acceleration  
- **[econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians](https://arxiv.org/abs/2504.06003v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06003v1.pdf)  
  Keywords: semantic, segmentation, efficient, ar  
- **[Micro-splatting: Maximizing Isotropic Constraints for Refined Optimization in 3D Gaussian Splatting](https://arxiv.org/abs/2504.05740v1)**  
  Authors: Jee Won Lee, Hansol Lim, Sooyeun Yang, Jongseong Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05740v1.pdf)  
  Keywords: compact, gaussian splatting, 3d reconstruction, ar, 3d gaussian, real-time rendering, dynamic  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: head, ar, efficient, high quality, efficient rendering, 3d gaussian  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: ray marching, dynamic, animation, gaussian splatting, efficient, ar, 3d gaussian, compact, acceleration  
- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: segmentation, face, gaussian splatting, efficient, 3d reconstruction, ar, dynamic, human  
- **[3R-GS: Best Practice in Optimizing Camera Poses Along with 3DGS](https://arxiv.org/abs/2504.04294v1)**  
  Authors: Zhisheng Huang, Peng Wang, Jingdong Zhang, Yuan Liu, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04294v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zsh523.github.io/3R-GS/)  
  Keywords: face, gaussian splatting, efficient, motion, ar, 3d gaussian, neural rendering  
- **[WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2504.03886v1)**  
  Authors: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys, Songyou Peng, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03886v1.pdf)  
  Keywords: mapping, tracking, gaussian splatting, slam, efficient, ar, dynamic  
- **[Compressing 3D Gaussian Splatting by Noise-Substituted Vector Quantization](https://arxiv.org/abs/2504.03059v2)**  
  Authors: Haishan Wang, Mohammad Hassan Vali, Arno Solin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03059v2.pdf)  
  Keywords: fast, compression, gaussian splatting, efficient, 3d reconstruction, ar, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 264 papers*

- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: shadow, avatar, head, face, vr, gaussian splatting, body, geometry, ar, 3d gaussian, dynamic, human, high-fidelity  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: head, ar, efficient, high quality, efficient rendering, 3d gaussian  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: localization, dynamic, mapping, tracking, gaussian splatting, slam, ar, 3d gaussian, 4d, high-fidelity  
- **[UAVTwin: Neural Digital Twins for UAVs using Gaussian Splatting](https://arxiv.org/abs/2504.02158v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02158v1.pdf)  
  Keywords: dynamic, gaussian splatting, high quality, motion, ar, 3d gaussian, neural rendering, human, high-fidelity  
- **[BOGausS: Better Optimized Gaussian Splatting](https://arxiv.org/abs/2504.01844v1)**  
  Authors: Stéphane Pateux, Matthieu Gendrin, Luce Morin, Théo Ladune, Xiaoran Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01844v1.pdf)  
  Keywords: fast, nerf, gaussian splatting, efficient, ar, 3d gaussian, high-fidelity  
- **[RealityAvatar: Towards Realistic Loose Clothing Modeling in Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2504.01559v1)**  
  Authors: Yahui Li, Zhi Zeng, Liming Pang, Guixuan Zhang, Shuwu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01559v1.pdf)  
  Keywords: avatar, nerf, ar, gaussian splatting, efficient, motion, human, 3d gaussian, dynamic, deformation, high-fidelity  
- **[High-fidelity 3D Object Generation from Single Image with RGBN-Volume Gaussian Reconstruction Model](https://arxiv.org/abs/2504.01512v1)**  
  Authors: Yiyang Shen, Kun Zhou, He Wang, Yin Yang, Tianjia Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01512v1.pdf)  
  Keywords: face, gaussian splatting, ar, 3d gaussian, high-fidelity  
- **[ExScene: Free-View 3D Scene Reconstruction with Gaussian Splatting from a Single Image](https://arxiv.org/abs/2503.23881v1)**  
  Authors: Tianyi Gong, Boyan Li, Yifei Zhong, Fangxin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23881v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, high-fidelity  
- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: dynamic, face, gaussian splatting, motion, ar, 4d, deformation, high-fidelity  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: fast, nerf, gaussian splatting, efficient, geometry, ar, reflection, dynamic, high-fidelity, outdoor  

### Ray Tracing

- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: lighting, relighting, ray tracing, ar, gaussian splatting, efficient, efficient rendering, 3d gaussian, acceleration  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: ray marching, dynamic, animation, gaussian splatting, efficient, ar, 3d gaussian, compact, acceleration  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: lighting, face, ray tracing, illumination, gaussian splatting, efficient, global illumination, ar, 3d gaussian, real-time rendering  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: lighting, fast, light transport, face, illumination, global illumination, 3d gaussian, real-time rendering, dynamic  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: shadow, fast, ray tracing, reflection, gaussian splatting, ar, 3d gaussian, neural rendering  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: lighting, relightable, face, ray tracing, tracking, 4d, efficient, geometry, ar, real-time rendering, dynamic  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: shadow, lighting, face, ray tracing, gaussian splatting, reflection  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, gaussian splatting, ar, 3d gaussian, survey  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: light transport, ray tracing, gaussian splatting, efficient, ar, reflection, acceleration  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: shadow, ray tracing, reflection, gaussian splatting, ar, 3d gaussian  

### Relighting

*Showing the latest 50 out of 180 papers*

- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: shadow, avatar, head, face, vr, gaussian splatting, body, geometry, ar, 3d gaussian, dynamic, human, high-fidelity  
- **[SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2504.06815v1)**  
  Authors: Hanxiao Sun, YuPeng Gao, Jin Xie, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06815v1.pdf)  
  Keywords: lighting, relighting, illumination, gaussian splatting, ar, 3d gaussian, real-time rendering, nerf  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: lighting, relighting, ray tracing, ar, gaussian splatting, efficient, efficient rendering, 3d gaussian, acceleration  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: gaussian splatting, motion, ar, reflection, nerf, outdoor  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: lighting, mapping, gaussian splatting, ar, 3d gaussian, real-time rendering, nerf  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: lighting, face, ray tracing, illumination, gaussian splatting, efficient, global illumination, ar, 3d gaussian, real-time rendering  
- **[LITA-GS: Illumination-Agnostic Novel View Synthesis via Reference-Free 3D Gaussian Splatting and Physical Priors](https://arxiv.org/abs/2504.00219v1)**  
  Authors: Han Zhou, Wei Dong, Jun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00219v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LowLevelAI/LITA-GS?style=social)](https://github.com/LowLevelAI/LITA-GS)  
  Keywords: lighting, fast, illumination, gaussian splatting, motion, ar, 3d gaussian, nerf  
- **[Learning 3D-Gaussian Simulators from RGB Videos](https://arxiv.org/abs/2503.24009v1)**  
  Authors: Mikel Zhobro, Andreas René Geist, Georg Martius  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24009v1.pdf)  
  Keywords: lighting, gaussian splatting, body, ar, 3d gaussian, dynamic  
- **[TranSplat: Lighting-Consistent Cross-Scene Object Transfer with 3D Gaussian Splatting](https://arxiv.org/abs/2503.22676v1)**  
  Authors: Boyang, Yu, Yanlin Jin, Ashok Veeraraghavan, Akshat Dave, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22676v1.pdf)  
  Keywords: lighting, segmentation, relighting, gaussian splatting, ar, 3d gaussian  
- **[Follow Your Motion: A Generic Temporal Consistency Portrait Editing Framework with Trajectory Guidance](https://arxiv.org/abs/2503.22225v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22225v1.pdf)  
  Keywords: lighting, avatar, relighting, head, face, gaussian splatting, efficient, motion, ar, 3d gaussian, dynamic  

### SLAM

*Showing the latest 50 out of 243 papers*

- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: mapping, deformation, ar, 3d gaussian, human  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: localization, dynamic, mapping, tracking, gaussian splatting, slam, ar, 3d gaussian, 4d, high-fidelity  
- **[WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2504.03886v1)**  
  Authors: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys, Songyou Peng, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03886v1.pdf)  
  Keywords: mapping, tracking, gaussian splatting, slam, efficient, ar, dynamic  
- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: localization, mapping, fast, face, tracking, gaussian splatting, slam, ar, 3d gaussian, dynamic  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: lighting, mapping, gaussian splatting, ar, 3d gaussian, real-time rendering, nerf  
- **[Visual Acoustic Fields](https://arxiv.org/abs/2503.24270v2)**  
  Authors: Yuelei Li, Hyunjin Kim, Fangneng Zhan, Ri-Zhao Qiu, Mazeyu Ji, Xiaojun Shan, Xueyan Zou, Paul Liang, Hanspeter Pfister, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24270v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuelei0428.github.io/projects/Visual-Acoustic-Fields/.)  
  Keywords: localization, gaussian splatting, ar, 3d gaussian, human  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: semantic, localization, segmentation, understanding, gaussian splatting, ar, 3d gaussian, robotics  
- **[VizFlyt: Perception-centric Pedagogical Framework For Autonomous Aerial Robots](https://arxiv.org/abs/2503.22876v2)**  
  Authors: Kushagra Srivastava, Rutwik Kulkarni, Manoj Velmurugan, Nitin J. Sanket  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22876v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pear.wpi.edu/research/vizflyt.html)  
  Keywords: localization, gaussian splatting, efficient, ar, 3d gaussian, robotics  
- **[Time-resolved dynamic CBCT reconstruction using prior-model-free spatiotemporal Gaussian representation (PMF-STGR)](https://arxiv.org/abs/2503.22139v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22139v1.pdf)  
  Keywords: localization, fast, efficient, motion, ar, 3d gaussian, dynamic, deformation  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: semantic, localization, mapping, slam, ar, 3d gaussian, dynamic, high-fidelity, robotics  

### Scene Understanding

*Showing the latest 50 out of 286 papers*

- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: segmentation, head, understanding, gaussian splatting, 3d reconstruction, ar, 3d gaussian, nerf  
- **[IAAO: Interactive Affordance Learning for Articulated Objects in 3D Environments](https://arxiv.org/abs/2504.06827v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06827v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, understanding  
- **[econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians](https://arxiv.org/abs/2504.06003v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06003v1.pdf)  
  Keywords: semantic, segmentation, efficient, ar  
- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: segmentation, face, gaussian splatting, efficient, 3d reconstruction, ar, dynamic, human  
- **[Interpretable Single-View 3D Gaussian Splatting using Unsupervised Hierarchical Disentangled Representation Learning](https://arxiv.org/abs/2504.04190v1)**  
  Authors: Yuyang Zhang, Baao Xie, Hu Zhu, Qi Wang, Huanting Guo, Xin Jin, Wenjun Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04190v1.pdf)  
  Keywords: semantic, understanding, gaussian splatting, 3d reconstruction, geometry, ar, 3d gaussian  
- **[Scene4U: Hierarchical Layered 3D Scene Reconstruction from Single Panoramic Image for Your Immerse Exploration](https://arxiv.org/abs/2504.00387v1)**  
  Authors: Zilong Huang, Jun He, Junyan Ye, Lihan Jiang, Weijia Li, Yiping Chen, Ting Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00387v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LongHZ140516/Scene4U?style=social)](https://github.com/LongHZ140516/Scene4U)  
  Keywords: semantic, fast, segmentation, gaussian splatting, ar, 3d gaussian, dynamic  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: semantic, localization, segmentation, understanding, gaussian splatting, ar, 3d gaussian, robotics  
- **[TranSplat: Lighting-Consistent Cross-Scene Object Transfer with 3D Gaussian Splatting](https://arxiv.org/abs/2503.22676v1)**  
  Authors: Boyang, Yu, Yanlin Jin, Ashok Veeraraghavan, Akshat Dave, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22676v1.pdf)  
  Keywords: lighting, segmentation, relighting, gaussian splatting, ar, 3d gaussian  
- **[ABC-GS: Alignment-Based Controllable Style Transfer for 3D Gaussian Splatting](https://arxiv.org/abs/2503.22218v1)**  
  Authors: Wenjie Liu, Zhongliang Liu, Xiaoyan Yang, Man Sha, Yang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22218v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vpx-ecnu.github.io/ABC-GS-website.)  
  Keywords: segmentation, gaussian splatting, ar, 3d gaussian, nerf  
- **[Segment then Splat: A Unified Approach for 3D Open-Vocabulary Segmentation based on Gaussian Splatting](https://arxiv.org/abs/2503.22204v1)**  
  Authors: Yiren Lu, Yunlai Zhou, Yiran Qiao, Chaoda Song, Tuo Liang, Jing Ma, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22204v1.pdf)  
  Keywords: segmentation, gaussian splatting, motion, ar, robotics, dynamic  



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