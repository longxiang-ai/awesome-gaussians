# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-04-09 00:52:05

## Categories

- [3DGS Surveys](#3dgs-surveys) (26 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (461 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1620 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (545 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (614 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (114 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (521 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (89 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (614 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (262 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (37 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (176 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (242 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (283 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: gaussian splatting, 3d reconstruction, survey, dynamic, lighting, ar, motion, 3d gaussian, fast  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, survey, dynamic, ar, 3d gaussian  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: ar, survey, semantic, geometry  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, 3d reconstruction, survey, compression, nerf, ar, 3d gaussian, efficient  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: deformation, gaussian splatting, survey, dynamic, nerf, lighting, ar, motion, 4d  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, survey, ray tracing, ar, 3d gaussian  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: mapping, geometry, survey, slam, dynamic, lighting, tracking, outdoor, localization, face, ar  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: recognition, gaussian splatting, survey, illumination, ar, 3d gaussian  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: gaussian splatting, geometry, 3d reconstruction, survey, dynamic, nerf, compact, lighting, semantic, high-fidelity, robotics, ar, autonomous driving  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: real-time rendering, gaussian splatting, survey, robotics, nerf, ar, understanding, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 461 papers*

- **[Let it Snow! Animating Static Gaussian Scenes With Dynamic Weather Effects](https://arxiv.org/abs/2504.05296v1)**  
  Authors: Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05296v1.pdf)  
  Keywords: gaussian splatting, dynamic, ar, motion, 3d gaussian, fast  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: gaussian splatting, acceleration, dynamic, compact, ray marching, ar, animation, 3d gaussian, efficient  
- **[Compressing 3D Gaussian Splatting by Noise-Substituted Vector Quantization](https://arxiv.org/abs/2504.03059v1)**  
  Authors: Haishan Wang, Mohammad Hassan Vali, Arno Solin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03059v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, compression, ar, 3d gaussian, fast, efficient  
- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: gaussian splatting, mapping, slam, dynamic, tracking, ar, localization, face, 3d gaussian, fast  
- **[WorldPrompter: Traversable Text-to-Scene Generation](https://arxiv.org/abs/2504.02045v1)**  
  Authors: Zhaoyang Zhang, Yannick Hold-Geoffroy, Miloš Hašan, Chen Ziwen, Fujun Luan, Julie Dorsey, Yiwei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02045v1.pdf)  
  Keywords: ar, fast  
- **[Toward Real-world BEV Perception: Depth Uncertainty Estimation via Gaussian Splatting](https://arxiv.org/abs/2504.01957v2)**  
  Authors: Shu-Wei Lu, Yi-Hsuan Tsai, Yi-Ting Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01957v2.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, autonomous driving, fast  
- **[BOGausS: Better Optimized Gaussian Splatting](https://arxiv.org/abs/2504.01844v1)**  
  Authors: Stéphane Pateux, Matthieu Gendrin, Luce Morin, Théo Ladune, Xiaoran Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01844v1.pdf)  
  Keywords: gaussian splatting, nerf, ar, high-fidelity, 3d gaussian, fast, efficient  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, mapping, nerf, lighting, ar, 3d gaussian  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: real-time rendering, gaussian splatting, global illumination, ray tracing, illumination, lighting, ar, face, 3d gaussian, efficient  
- **[DropGaussian: Structural Regularization for Sparse-view Gaussian Splatting](https://arxiv.org/abs/2504.00773v1)**  
  Authors: Hyunwoo Park, Gun Ryu, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DCVL-3D/DropGaussian?style=social)](https://github.com/DCVL-3D/DropGaussian)  
  Keywords: gaussian splatting, sparse-view, ar, face, 3d gaussian, fast  

### Applications

*Showing the latest 50 out of 1620 papers*

- **[Let it Snow! Animating Static Gaussian Scenes With Dynamic Weather Effects](https://arxiv.org/abs/2504.05296v1)**  
  Authors: Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05296v1.pdf)  
  Keywords: gaussian splatting, dynamic, ar, motion, 3d gaussian, fast  
- **[PanoDreamer: Consistent Text to 360-Degree Scene Generation](https://arxiv.org/abs/2504.05152v1)**  
  Authors: Zhexiao Xiong, Zhang Chen, Zhong Li, Yi Xu, Nathan Jacobs  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05152v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: gaussian splatting, acceleration, dynamic, compact, ray marching, ar, animation, 3d gaussian, efficient  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: 4d, gaussian splatting, mapping, slam, dynamic, tracking, ar, high-fidelity, localization, 3d gaussian  
- **[DeclutterNeRF: Generative-Free 3D Scene Recovery for Occlusion Removal](https://arxiv.org/abs/2504.04679v1)**  
  Authors: Wanzhou Liu, Zhexiao Xiong, Xinyu Li, Nathan Jacobs  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04679v1.pdf)  
  Keywords: gaussian splatting, nerf, ar, motion, 3d gaussian  
- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, segmentation, dynamic, ar, face, human, efficient  
- **[Targetless LiDAR-Camera Calibration with Anchored 3D Gaussians](https://arxiv.org/abs/2504.04597v1)**  
  Authors: Haebeom Jung, Namtae Kim, Jungwoo Kim, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04597v1.pdf)  
  Keywords: ar, 3d gaussian, autonomous driving, geometry  
- **[Thermoxels: a voxel-based method to generate simulation-ready 3D thermal models](https://arxiv.org/abs/2504.04448v1)**  
  Authors: Etienne Chassaing, Florent Forest, Olga Fink, Malcolm Mielle  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04448v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d reconstruction, nerf, ar, face  
- **[3R-GS: Best Practice in Optimizing Camera Poses Along with 3DGS](https://arxiv.org/abs/2504.04294v1)**  
  Authors: Zhisheng Huang, Peng Wang, Jingdong Zhang, Yuan Liu, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04294v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zsh523.github.io/3R-GS/)  
  Keywords: gaussian splatting, neural rendering, ar, motion, face, 3d gaussian, efficient  
- **[Interpretable Single-View 3D Gaussian Splatting using Unsupervised Hierarchical Disentangled Representation Learning](https://arxiv.org/abs/2504.04190v1)**  
  Authors: Yuyang Zhang, Baao Xie, Hu Zhu, Qi Wang, Huanting Guo, Xin Jin, Wenjun Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04190v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d reconstruction, semantic, ar, understanding, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 545 papers*

- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, segmentation, dynamic, ar, face, human, efficient  
- **[Thermoxels: a voxel-based method to generate simulation-ready 3D thermal models](https://arxiv.org/abs/2504.04448v1)**  
  Authors: Etienne Chassaing, Florent Forest, Olga Fink, Malcolm Mielle  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04448v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d reconstruction, nerf, ar, face  
- **[3R-GS: Best Practice in Optimizing Camera Poses Along with 3DGS](https://arxiv.org/abs/2504.04294v1)**  
  Authors: Zhisheng Huang, Peng Wang, Jingdong Zhang, Yuan Liu, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04294v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zsh523.github.io/3R-GS/)  
  Keywords: gaussian splatting, neural rendering, ar, motion, face, 3d gaussian, efficient  
- **[HumanDreamer-X: Photorealistic Single-image Human Avatars Reconstruction via Gaussian Restoration](https://arxiv.org/abs/2504.03536v1)**  
  Authors: Boyuan Wang, Runqi Ouyang, Xiaofeng Wang, Zheng Zhu, Guosheng Zhao, Chaojun Ni, Guan Huang, Lihong Liu, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03536v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d reconstruction, avatar, ar, animation, human, 3d gaussian  
- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: gaussian splatting, mapping, slam, dynamic, tracking, ar, localization, face, 3d gaussian, fast  
- **[ConsDreamer: Advancing Multi-View Consistency for Zero-Shot Text-to-3D Generation](https://arxiv.org/abs/2504.02316v1)**  
  Authors: Yuan Zhou, Shilong Jin, Litao Hua, Wanjun Lv, Haoran Duan, Jungong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02316v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, face, ar  
- **[UAVTwin: Neural Digital Twins for UAVs using Gaussian Splatting](https://arxiv.org/abs/2504.02158v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02158v1.pdf)  
  Keywords: gaussian splatting, neural rendering, high quality, dynamic, ar, high-fidelity, motion, human, 3d gaussian  
- **[RealityAvatar: Towards Realistic Loose Clothing Modeling in Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2504.01559v1)**  
  Authors: Yahui Li, Zhi Zeng, Liming Pang, Guixuan Zhang, Shuwu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01559v1.pdf)  
  Keywords: deformation, gaussian splatting, avatar, dynamic, nerf, ar, high-fidelity, motion, human, 3d gaussian, efficient  
- **[High-fidelity 3D Object Generation from Single Image with RGBN-Volume Gaussian Reconstruction Model](https://arxiv.org/abs/2504.01512v1)**  
  Authors: Yiyang Shen, Kun Zhou, He Wang, Yin Yang, Tianjia Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01512v1.pdf)  
  Keywords: gaussian splatting, ar, high-fidelity, face, 3d gaussian  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: real-time rendering, gaussian splatting, global illumination, ray tracing, illumination, lighting, ar, face, 3d gaussian, efficient  

### Dynamic Scene

*Showing the latest 50 out of 614 papers*

- **[Let it Snow! Animating Static Gaussian Scenes With Dynamic Weather Effects](https://arxiv.org/abs/2504.05296v1)**  
  Authors: Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05296v1.pdf)  
  Keywords: gaussian splatting, dynamic, ar, motion, 3d gaussian, fast  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: gaussian splatting, acceleration, dynamic, compact, ray marching, ar, animation, 3d gaussian, efficient  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: 4d, gaussian splatting, mapping, slam, dynamic, tracking, ar, high-fidelity, localization, 3d gaussian  
- **[DeclutterNeRF: Generative-Free 3D Scene Recovery for Occlusion Removal](https://arxiv.org/abs/2504.04679v1)**  
  Authors: Wanzhou Liu, Zhexiao Xiong, Xinyu Li, Nathan Jacobs  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04679v1.pdf)  
  Keywords: gaussian splatting, nerf, ar, motion, 3d gaussian  
- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, segmentation, dynamic, ar, face, human, efficient  
- **[3R-GS: Best Practice in Optimizing Camera Poses Along with 3DGS](https://arxiv.org/abs/2504.04294v1)**  
  Authors: Zhisheng Huang, Peng Wang, Jingdong Zhang, Yuan Liu, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04294v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zsh523.github.io/3R-GS/)  
  Keywords: gaussian splatting, neural rendering, ar, motion, face, 3d gaussian, efficient  
- **[WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2504.03886v1)**  
  Authors: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys, Songyou Peng, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03886v1.pdf)  
  Keywords: gaussian splatting, mapping, slam, dynamic, tracking, ar, efficient  
- **[HumanDreamer-X: Photorealistic Single-image Human Avatars Reconstruction via Gaussian Restoration](https://arxiv.org/abs/2504.03536v1)**  
  Authors: Boyuan Wang, Runqi Ouyang, Xiaofeng Wang, Zheng Zhu, Guosheng Zhao, Chaojun Ni, Guan Huang, Lihong Liu, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03536v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d reconstruction, avatar, ar, animation, human, 3d gaussian  
- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: gaussian splatting, mapping, slam, dynamic, tracking, ar, localization, face, 3d gaussian, fast  
- **[UAVTwin: Neural Digital Twins for UAVs using Gaussian Splatting](https://arxiv.org/abs/2504.02158v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02158v1.pdf)  
  Keywords: gaussian splatting, neural rendering, high quality, dynamic, ar, high-fidelity, motion, human, 3d gaussian  

### Few-shot

*Showing the latest 50 out of 114 papers*

- **[DropGaussian: Structural Regularization for Sparse-view Gaussian Splatting](https://arxiv.org/abs/2504.00773v1)**  
  Authors: Hyunwoo Park, Gun Ryu, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DCVL-3D/DropGaussian?style=social)](https://github.com/DCVL-3D/DropGaussian)  
  Keywords: gaussian splatting, sparse-view, ar, face, 3d gaussian, fast  
- **[Coca-Splat: Collaborative Optimization for Camera Parameters and 3D Gaussians](https://arxiv.org/abs/2504.00639v1)**  
  Authors: Jiamin Wu, Hongyang Li, Xiaoke Jiang, Yuan Yao, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00639v1.pdf)  
  Keywords: 3d gaussian, sparse view, ar  
- **[Distilling Multi-view Diffusion Models into 3D Generators](https://arxiv.org/abs/2504.00457v3)**  
  Authors: Hao Qin, Luyuan Chen, Ming Kong, Mengxu Lu, Qiang Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00457v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://qinbaigao.github.io/DD3G_project/)  
  Keywords: gaussian splatting, sparse-view, ar, 3d gaussian, efficient  
- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: gaussian splatting, geometry, 3d reconstruction, sparse-view, neural rendering, ar, face  
- **[FreeSplat++: Generalizable 3D Gaussian Splatting for Efficient Indoor Scene Reconstruction](https://arxiv.org/abs/2503.22986v1)**  
  Authors: Yunsong Wang, Tianxin Huang, Hanlin Chen, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22986v1.pdf)  
  Keywords: sparse view, gaussian splatting, ar, 3d gaussian, efficient  
- **[CoMapGS: Covisibility Map-based Gaussian Splatting for Sparse Novel View Synthesis](https://arxiv.org/abs/2503.20998v1)**  
  Authors: Youngkyoon Jang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20998v1.pdf)  
  Keywords: ar, few-shot, gaussian splatting, nerf  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: gaussian splatting, sparse-view, illumination, ar, outdoor, 3d gaussian  
- **[NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting](https://arxiv.org/abs/2503.18794v1)**  
  Authors: Yulong Zheng, Zicheng Jiang, Shengfeng He, Yandu Sun, Junyu Dong, Huaidong Zhang, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18794v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://usmizuki.github.io/NexusGS/.)  
  Keywords: sparse view, gaussian splatting, geometry, few-shot, sparse-view, nerf, ar, 3d gaussian  
- **[SplatVoxel: History-Aware Novel View Streaming without Temporal Training](https://arxiv.org/abs/2503.14698v1)**  
  Authors: Yiming Wang, Lucy Chai, Xuan Luo, Michael Niemeyer, Manuel Lagunas, Stephen Lombardi, Siyu Tang, Tiancheng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14698v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://19reborn.github.io/SplatVoxel/)  
  Keywords: gaussian splatting, sparse-view, tracking, ar, motion, efficient  
- **[RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2503.14198v1)**  
  Authors: Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14198v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iSEE-Laboratory/RoGSplat?style=social)](https://github.com/iSEE-Laboratory/RoGSplat)  
  Keywords: sparse view, gaussian splatting, geometry, body, ar, high-fidelity, human, 3d gaussian  

### Geometry Reconstruction

*Showing the latest 50 out of 521 papers*

- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, segmentation, dynamic, ar, face, human, efficient  
- **[Targetless LiDAR-Camera Calibration with Anchored 3D Gaussians](https://arxiv.org/abs/2504.04597v1)**  
  Authors: Haebeom Jung, Namtae Kim, Jungwoo Kim, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04597v1.pdf)  
  Keywords: ar, 3d gaussian, autonomous driving, geometry  
- **[Thermoxels: a voxel-based method to generate simulation-ready 3D thermal models](https://arxiv.org/abs/2504.04448v1)**  
  Authors: Etienne Chassaing, Florent Forest, Olga Fink, Malcolm Mielle  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04448v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d reconstruction, nerf, ar, face  
- **[Interpretable Single-View 3D Gaussian Splatting using Unsupervised Hierarchical Disentangled Representation Learning](https://arxiv.org/abs/2504.04190v1)**  
  Authors: Yuyang Zhang, Baao Xie, Hu Zhu, Qi Wang, Huanting Guo, Xin Jin, Wenjun Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04190v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d reconstruction, semantic, ar, understanding, 3d gaussian  
- **[HumanDreamer-X: Photorealistic Single-image Human Avatars Reconstruction via Gaussian Restoration](https://arxiv.org/abs/2504.03536v1)**  
  Authors: Boyuan Wang, Runqi Ouyang, Xiaofeng Wang, Zheng Zhu, Guosheng Zhao, Chaojun Ni, Guan Huang, Lihong Liu, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03536v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d reconstruction, avatar, ar, animation, human, 3d gaussian  
- **[Compressing 3D Gaussian Splatting by Noise-Substituted Vector Quantization](https://arxiv.org/abs/2504.03059v1)**  
  Authors: Haishan Wang, Mohammad Hassan Vali, Arno Solin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03059v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, compression, ar, 3d gaussian, fast, efficient  
- **[Diffusion-Guided Gaussian Splatting for Large-Scale Unconstrained 3D Reconstruction and Novel View Synthesis](https://arxiv.org/abs/2504.01960v1)**  
  Authors: Niluthpol Chowdhury Mithun, Tuan Pham, Qiao Wang, Ben Southall, Kshitij Minhas, Bogdan Matei, Stephan Mandt, Supun Samarasekera, Rakesh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01960v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, dynamic, nerf, ar, 3d gaussian  
- **[FlowR: Flowing from Sparse to Dense 3D Reconstructions](https://arxiv.org/abs/2504.01647v1)**  
  Authors: Tobias Fischer, Samuel Rota Bulò, Yung-Hsu Yang, Nikhil Varma Keetha, Lorenzo Porzi, Norman Müller, Katja Schwarz, Jonathon Luiten, Marc Pollefeys, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01647v1.pdf)  
  Keywords: vr, gaussian splatting, 3d reconstruction, ar, 3d gaussian  
- **[ADGaussian: Generalizable Gaussian Splatting for Autonomous Driving with Multi-modal Inputs](https://arxiv.org/abs/2504.00437v1)**  
  Authors: Qi Song, Chenghong Li, Haotong Lin, Sida Peng, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00437v1.pdf)  
  Keywords: gaussian splatting, geometry, ar, autonomous driving, efficient  
- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: gaussian splatting, geometry, 3d reconstruction, sparse-view, neural rendering, ar, face  

### Large Scene

*Showing the latest 50 out of 89 papers*

- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v1)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v1.pdf)  
  Keywords: gaussian splatting, reflection, nerf, ar, outdoor, motion  
- **[UnIRe: Unsupervised Instance Decomposition for Dynamic Urban Scene Reconstruction](https://arxiv.org/abs/2504.00763v1)**  
  Authors: Yunxuan Mao, Rong Xiong, Yue Wang, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00763v1.pdf)  
  Keywords: 4d, gaussian splatting, dynamic, ar, 3d gaussian, autonomous driving, urban scene  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: gaussian splatting, geometry, reflection, dynamic, nerf, ar, high-fidelity, outdoor, fast, efficient  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: gaussian splatting, geometry, dynamic, ar, motion, urban scene  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, nerf, ar, 3d gaussian, autonomous driving, urban scene, fast, efficient  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: gaussian splatting, sparse-view, illumination, ar, outdoor, 3d gaussian  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: gaussian splatting, ar, outdoor, localization, efficient  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: real-time rendering, gaussian splatting, geometry, ar, outdoor, 3d gaussian, fast, efficient  
- **[PanopticSplatting: End-to-End Panoptic Gaussian Splatting](https://arxiv.org/abs/2503.18073v1)**  
  Authors: Yuxuan Xie, Xuan Yu, Changjian Jiang, Sitong Mao, Shunbo Zhou, Rui Fan, Rong Xiong, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18073v1.pdf)  
  Keywords: gaussian splatting, segmentation, nerf, ar, understanding, large scene  
- **[GaussianFocus: Constrained Attention Focus for 3D Gaussian Splatting](https://arxiv.org/abs/2503.17798v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17798v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, neural rendering, ar, large scene, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 614 papers*

- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: gaussian splatting, acceleration, dynamic, compact, ray marching, ar, animation, 3d gaussian, efficient  
- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, segmentation, dynamic, ar, face, human, efficient  
- **[3R-GS: Best Practice in Optimizing Camera Poses Along with 3DGS](https://arxiv.org/abs/2504.04294v1)**  
  Authors: Zhisheng Huang, Peng Wang, Jingdong Zhang, Yuan Liu, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04294v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zsh523.github.io/3R-GS/)  
  Keywords: gaussian splatting, neural rendering, ar, motion, face, 3d gaussian, efficient  
- **[WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2504.03886v1)**  
  Authors: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys, Songyou Peng, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03886v1.pdf)  
  Keywords: gaussian splatting, mapping, slam, dynamic, tracking, ar, efficient  
- **[Compressing 3D Gaussian Splatting by Noise-Substituted Vector Quantization](https://arxiv.org/abs/2504.03059v1)**  
  Authors: Haishan Wang, Mohammad Hassan Vali, Arno Solin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03059v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, compression, ar, 3d gaussian, fast, efficient  
- **[BOGausS: Better Optimized Gaussian Splatting](https://arxiv.org/abs/2504.01844v1)**  
  Authors: Stéphane Pateux, Matthieu Gendrin, Luce Morin, Théo Ladune, Xiaoran Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01844v1.pdf)  
  Keywords: gaussian splatting, nerf, ar, high-fidelity, 3d gaussian, fast, efficient  
- **[RealityAvatar: Towards Realistic Loose Clothing Modeling in Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2504.01559v1)**  
  Authors: Yahui Li, Zhi Zeng, Liming Pang, Guixuan Zhang, Shuwu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01559v1.pdf)  
  Keywords: deformation, gaussian splatting, avatar, dynamic, nerf, ar, high-fidelity, motion, human, 3d gaussian, efficient  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: real-time rendering, gaussian splatting, global illumination, ray tracing, illumination, lighting, ar, face, 3d gaussian, efficient  
- **[Distilling Multi-view Diffusion Models into 3D Generators](https://arxiv.org/abs/2504.00457v3)**  
  Authors: Hao Qin, Luyuan Chen, Ming Kong, Mengxu Lu, Qiang Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00457v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://qinbaigao.github.io/DD3G_project/)  
  Keywords: gaussian splatting, sparse-view, ar, 3d gaussian, efficient  
- **[ADGaussian: Generalizable Gaussian Splatting for Autonomous Driving with Multi-modal Inputs](https://arxiv.org/abs/2504.00437v1)**  
  Authors: Qi Song, Chenghong Li, Haotong Lin, Sida Peng, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00437v1.pdf)  
  Keywords: gaussian splatting, geometry, ar, autonomous driving, efficient  

### Quality Enhancement

*Showing the latest 50 out of 262 papers*

- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: 4d, gaussian splatting, mapping, slam, dynamic, tracking, ar, high-fidelity, localization, 3d gaussian  
- **[UAVTwin: Neural Digital Twins for UAVs using Gaussian Splatting](https://arxiv.org/abs/2504.02158v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02158v1.pdf)  
  Keywords: gaussian splatting, neural rendering, high quality, dynamic, ar, high-fidelity, motion, human, 3d gaussian  
- **[BOGausS: Better Optimized Gaussian Splatting](https://arxiv.org/abs/2504.01844v1)**  
  Authors: Stéphane Pateux, Matthieu Gendrin, Luce Morin, Théo Ladune, Xiaoran Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01844v1.pdf)  
  Keywords: gaussian splatting, nerf, ar, high-fidelity, 3d gaussian, fast, efficient  
- **[RealityAvatar: Towards Realistic Loose Clothing Modeling in Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2504.01559v1)**  
  Authors: Yahui Li, Zhi Zeng, Liming Pang, Guixuan Zhang, Shuwu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01559v1.pdf)  
  Keywords: deformation, gaussian splatting, avatar, dynamic, nerf, ar, high-fidelity, motion, human, 3d gaussian, efficient  
- **[High-fidelity 3D Object Generation from Single Image with RGBN-Volume Gaussian Reconstruction Model](https://arxiv.org/abs/2504.01512v1)**  
  Authors: Yiyang Shen, Kun Zhou, He Wang, Yin Yang, Tianjia Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01512v1.pdf)  
  Keywords: gaussian splatting, ar, high-fidelity, face, 3d gaussian  
- **[ExScene: Free-View 3D Scene Reconstruction with Gaussian Splatting from a Single Image](https://arxiv.org/abs/2503.23881v1)**  
  Authors: Tianyi Gong, Boyan Li, Yifei Zhong, Fangxin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23881v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, ar  
- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: deformation, gaussian splatting, dynamic, ar, high-fidelity, motion, face, 4d  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: gaussian splatting, geometry, reflection, dynamic, nerf, ar, high-fidelity, outdoor, fast, efficient  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: mapping, slam, dynamic, semantic, robotics, ar, high-fidelity, localization, 3d gaussian  
- **[LLGS: Unsupervised Gaussian Splatting for Image Enhancement and Reconstruction in Pure Dark Environment](https://arxiv.org/abs/2503.18640v1)**  
  Authors: Haoran Wang, Jingwei Huang, Lu Yang, Tianchen Deng, Gaojing Zhang, Mingrui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18640v1.pdf)  
  Keywords: gaussian splatting, robotics, ar, high-fidelity, 3d gaussian  

### Ray Tracing

- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: gaussian splatting, acceleration, dynamic, compact, ray marching, ar, animation, 3d gaussian, efficient  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: real-time rendering, gaussian splatting, global illumination, ray tracing, illumination, lighting, ar, face, 3d gaussian, efficient  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: real-time rendering, global illumination, illumination, dynamic, lighting, face, 3d gaussian, fast, light transport  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: shadow, gaussian splatting, reflection, ray tracing, neural rendering, ar, 3d gaussian, fast  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, real-time rendering, geometry, ray tracing, dynamic, lighting, tracking, ar, face, relightable, efficient  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: shadow, gaussian splatting, reflection, ray tracing, lighting, face  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, survey, ray tracing, ar, 3d gaussian  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: gaussian splatting, reflection, efficient, ray tracing, acceleration, ar, light transport  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: shadow, gaussian splatting, reflection, ray tracing, ar, 3d gaussian  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v2)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v2.pdf)  
  Keywords: gaussian splatting, reflection, efficient, ray tracing, lighting, ar, relighting  

### Relighting

*Showing the latest 50 out of 176 papers*

- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v1)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v1.pdf)  
  Keywords: gaussian splatting, reflection, nerf, ar, outdoor, motion  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, mapping, nerf, lighting, ar, 3d gaussian  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: real-time rendering, gaussian splatting, global illumination, ray tracing, illumination, lighting, ar, face, 3d gaussian, efficient  
- **[LITA-GS: Illumination-Agnostic Novel View Synthesis via Reference-Free 3D Gaussian Splatting and Physical Priors](https://arxiv.org/abs/2504.00219v1)**  
  Authors: Han Zhou, Wei Dong, Jun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00219v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LowLevelAI/LITA-GS?style=social)](https://github.com/LowLevelAI/LITA-GS)  
  Keywords: gaussian splatting, illumination, nerf, lighting, ar, motion, 3d gaussian, fast  
- **[Learning 3D-Gaussian Simulators from RGB Videos](https://arxiv.org/abs/2503.24009v1)**  
  Authors: Mikel Zhobro, Andreas René Geist, Georg Martius  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24009v1.pdf)  
  Keywords: gaussian splatting, body, dynamic, lighting, ar, 3d gaussian  
- **[TranSplat: Lighting-Consistent Cross-Scene Object Transfer with 3D Gaussian Splatting](https://arxiv.org/abs/2503.22676v1)**  
  Authors: Boyang, Yu, Yanlin Jin, Ashok Veeraraghavan, Akshat Dave, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22676v1.pdf)  
  Keywords: gaussian splatting, segmentation, lighting, ar, 3d gaussian, relighting  
- **[Follow Your Motion: A Generic Temporal Consistency Portrait Editing Framework with Trajectory Guidance](https://arxiv.org/abs/2503.22225v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22225v1.pdf)  
  Keywords: gaussian splatting, avatar, efficient, dynamic, lighting, ar, head, motion, face, 3d gaussian, relighting  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: gaussian splatting, geometry, reflection, dynamic, nerf, ar, high-fidelity, outdoor, fast, efficient  
- **[PGC: Physics-Based Gaussian Cloth from a Single Pose](https://arxiv.org/abs/2503.20779v1)**  
  Authors: Michelle Guo, Matt Jen-Yuan Chiang, Igor Santesteban, Nikolaos Sarafianos, Hsiao-yu Chen, Oshri Halimi, Aljaž Božič, Shunsuke Saito, Jiajun Wu, C. Karen Liu, Tuur Stuyck, Egor Larionov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys-gaussian-cloth.github.io)  
  Keywords: body, lighting, ar, face, 3d gaussian, relighting  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, survey, dynamic, lighting, ar, motion, 3d gaussian, fast  

### SLAM

*Showing the latest 50 out of 242 papers*

- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: 4d, gaussian splatting, mapping, slam, dynamic, tracking, ar, high-fidelity, localization, 3d gaussian  
- **[WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2504.03886v1)**  
  Authors: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys, Songyou Peng, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03886v1.pdf)  
  Keywords: gaussian splatting, mapping, slam, dynamic, tracking, ar, efficient  
- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: gaussian splatting, mapping, slam, dynamic, tracking, ar, localization, face, 3d gaussian, fast  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, mapping, nerf, lighting, ar, 3d gaussian  
- **[Visual Acoustic Fields](https://arxiv.org/abs/2503.24270v2)**  
  Authors: Yuelei Li, Hyunjin Kim, Fangneng Zhan, Ri-Zhao Qiu, Mazeyu Ji, Xiaojun Shan, Xueyan Zou, Paul Liang, Hanspeter Pfister, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24270v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuelei0428.github.io/projects/Visual-Acoustic-Fields/.)  
  Keywords: gaussian splatting, ar, localization, human, 3d gaussian  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: gaussian splatting, segmentation, semantic, robotics, ar, understanding, localization, 3d gaussian  
- **[VizFlyt: Perception-centric Pedagogical Framework For Autonomous Aerial Robots](https://arxiv.org/abs/2503.22876v2)**  
  Authors: Kushagra Srivastava, Rutwik Kulkarni, Manoj Velmurugan, Nitin J. Sanket  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22876v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pear.wpi.edu/research/vizflyt.html)  
  Keywords: gaussian splatting, robotics, ar, localization, 3d gaussian, efficient  
- **[Time-resolved dynamic CBCT reconstruction using prior-model-free spatiotemporal Gaussian representation (PMF-STGR)](https://arxiv.org/abs/2503.22139v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22139v1.pdf)  
  Keywords: deformation, dynamic, ar, localization, motion, 3d gaussian, fast, efficient  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: mapping, slam, dynamic, semantic, robotics, ar, high-fidelity, localization, 3d gaussian  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: 4d, deformation, gaussian splatting, 3d reconstruction, tracking, ar, face, 3d gaussian  

### Scene Understanding

*Showing the latest 50 out of 283 papers*

- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, segmentation, dynamic, ar, face, human, efficient  
- **[Interpretable Single-View 3D Gaussian Splatting using Unsupervised Hierarchical Disentangled Representation Learning](https://arxiv.org/abs/2504.04190v1)**  
  Authors: Yuyang Zhang, Baao Xie, Hu Zhu, Qi Wang, Huanting Guo, Xin Jin, Wenjun Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04190v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d reconstruction, semantic, ar, understanding, 3d gaussian  
- **[Scene4U: Hierarchical Layered 3D Scene Reconstruction from Single Panoramic Image for Your Immerse Exploration](https://arxiv.org/abs/2504.00387v1)**  
  Authors: Zilong Huang, Jun He, Junyan Ye, Lihan Jiang, Weijia Li, Yiping Chen, Ting Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00387v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LongHZ140516/Scene4U?style=social)](https://github.com/LongHZ140516/Scene4U)  
  Keywords: gaussian splatting, segmentation, semantic, dynamic, ar, 3d gaussian, fast  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: gaussian splatting, segmentation, semantic, robotics, ar, understanding, localization, 3d gaussian  
- **[TranSplat: Lighting-Consistent Cross-Scene Object Transfer with 3D Gaussian Splatting](https://arxiv.org/abs/2503.22676v1)**  
  Authors: Boyang, Yu, Yanlin Jin, Ashok Veeraraghavan, Akshat Dave, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22676v1.pdf)  
  Keywords: gaussian splatting, segmentation, lighting, ar, 3d gaussian, relighting  
- **[ABC-GS: Alignment-Based Controllable Style Transfer for 3D Gaussian Splatting](https://arxiv.org/abs/2503.22218v1)**  
  Authors: Wenjie Liu, Zhongliang Liu, Xiaoyan Yang, Man Sha, Yang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22218v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vpx-ecnu.github.io/ABC-GS-website.)  
  Keywords: gaussian splatting, segmentation, nerf, ar, 3d gaussian  
- **[Segment then Splat: A Unified Approach for 3D Open-Vocabulary Segmentation based on Gaussian Splatting](https://arxiv.org/abs/2503.22204v1)**  
  Authors: Yiren Lu, Yunlai Zhou, Yiran Qiao, Chaoda Song, Tuo Liang, Jing Ma, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22204v1.pdf)  
  Keywords: gaussian splatting, segmentation, robotics, dynamic, ar, motion  
- **[Semantic Consistent Language Gaussian Splatting for Point-Level Open-vocabulary Querying](https://arxiv.org/abs/2503.21767v1)**  
  Authors: Hairong Yin, Huangying Zhan, Yi Xu, Raymond A. Yeh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21767v1.pdf)  
  Keywords: gaussian splatting, segmentation, semantic, ar, 3d gaussian  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: mapping, slam, dynamic, semantic, robotics, ar, high-fidelity, localization, 3d gaussian  
- **[Feature4X: Bridging Any Monocular Video to 4D Agentic AI with Versatile Gaussian Feature Fields](https://arxiv.org/abs/2503.20776v2)**  
  Authors: Shijie Zhou, Hui Ren, Yijia Weng, Shuwang Zhang, Zhen Wang, Dejia Xu, Zhiwen Fan, Suya You, Zhangyang Wang, Leonidas Guibas, Achuta Kadambi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20776v2.pdf)  
  Keywords: gaussian splatting, segmentation, semantic, dynamic, ar, 4d  



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