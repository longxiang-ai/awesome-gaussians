# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-04-16 00:53:09

## Categories

- [3DGS Surveys](#3dgs-surveys) (26 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (472 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1655 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (555 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (626 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (116 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (533 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (90 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (625 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (268 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (39 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (184 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (244 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (291 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: motion, survey, 3d reconstruction, fast, gaussian splatting, dynamic, ar, lighting, 3d gaussian  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: survey, gaussian splatting, real-time rendering, dynamic, ar, 3d gaussian  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: survey, geometry, semantic, ar  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: survey, 3d reconstruction, compression, gaussian splatting, efficient, real-time rendering, nerf, ar, 3d gaussian  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: motion, survey, gaussian splatting, dynamic, nerf, ar, deformation, lighting, 4d  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, gaussian splatting, ar, 3d gaussian, ray tracing  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: survey, slam, geometry, face, tracking, mapping, localization, dynamic, outdoor, ar, lighting  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: survey, gaussian splatting, recognition, illumination, ar, 3d gaussian  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: ar, survey, 3d reconstruction, semantic, geometry, high-fidelity, gaussian splatting, autonomous driving, robotics, dynamic, nerf, compact, lighting  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: survey, understanding, gaussian splatting, real-time rendering, robotics, nerf, ar, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 472 papers*

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: human, relighting, geometry, fast, gaussian splatting, avatar, shadow, ar, lighting, ray tracing, relightable  
- **[LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2504.10331v1)**  
  Authors: Hao Sun, Fenggen Yu, Huiyao Xu, Tao Zhang, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10331v1.pdf)  
  Keywords: 3d reconstruction, fast, gaussian splatting, real-time rendering, illumination, dynamic, nerf, ar, 3d gaussian  
- **[GaussVideoDreamer: 3D Scene Generation with Video Diffusion and Inconsistency-Aware Gaussian Splatting](https://arxiv.org/abs/2504.10001v2)**  
  Authors: Junlin Hao, Peiheng Wang, Haoyang Wang, Xinggong Zhang, Zongming Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10001v2.pdf)  
  Keywords: geometry, fast, gaussian splatting, ar, 3d gaussian  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, efficient, dynamic, nerf, ar, acceleration  
- **[FMLGS: Fast Multilevel Language Embedded Gaussians for Part-level Interactive Agents](https://arxiv.org/abs/2504.08581v1)**  
  Authors: Xin Tan, Yuzhou Ji, He Zhu, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08581v1.pdf)  
  Keywords: understanding, semantic, face, fast, efficient, gaussian splatting, ar, 3d gaussian  
- **[View-Dependent Uncertainty Estimation of 3D Gaussian Splatting](https://arxiv.org/abs/2504.07370v1)**  
  Authors: Chenyu Han, Corentin Dumery  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07370v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, ar  
- **[SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2504.06815v1)**  
  Authors: Hanxiao Sun, YuPeng Gao, Jin Xie, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06815v1.pdf)  
  Keywords: relighting, gaussian splatting, real-time rendering, illumination, nerf, ar, lighting, 3d gaussian  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: 3d reconstruction, fast, efficient, gaussian splatting, robotics, dynamic, ar  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: relighting, gaussian splatting, lighting, efficient, ar, efficient rendering, 3d gaussian, acceleration, ray tracing  
- **[Micro-splatting: Maximizing Isotropic Constraints for Refined Optimization in 3D Gaussian Splatting](https://arxiv.org/abs/2504.05740v1)**  
  Authors: Jee Won Lee, Hansol Lim, Sooyeun Yang, Jongseong Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05740v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, real-time rendering, dynamic, compact, ar, 3d gaussian  

### Applications

*Showing the latest 50 out of 1655 papers*

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: human, relighting, geometry, fast, gaussian splatting, avatar, shadow, ar, lighting, ray tracing, relightable  
- **[LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2504.10331v1)**  
  Authors: Hao Sun, Fenggen Yu, Huiyao Xu, Tao Zhang, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10331v1.pdf)  
  Keywords: 3d reconstruction, fast, gaussian splatting, real-time rendering, illumination, dynamic, nerf, ar, 3d gaussian  
- **[ESCT3D: Efficient and Selectively Controllable Text-Driven 3D Content Generation with Gaussian Splatting](https://arxiv.org/abs/2504.10316v1)**  
  Authors: Huiqi Wu, Jianbo Mei, Yingjie Huang, Yining Xu, Jingjiao You, Yilong Liu, Li Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10316v1.pdf)  
  Keywords: efficient, gaussian splatting, ar  
- **[EBAD-Gaussian: Event-driven Bundle Adjusted Deblur Gaussian Splatting](https://arxiv.org/abs/2504.10012v1)**  
  Authors: Yufei Deng, Yuanjian Wang, Rong Xiao, Chenwei Tang, Jizhe Zhou, Jiahao Fan, Deng Xiong, Jiancheng Lv, Huajin Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10012v1.pdf)  
  Keywords: motion, gaussian splatting, dynamic, ar, 3d gaussian  
- **[GaussVideoDreamer: 3D Scene Generation with Video Diffusion and Inconsistency-Aware Gaussian Splatting](https://arxiv.org/abs/2504.10001v2)**  
  Authors: Junlin Hao, Peiheng Wang, Haoyang Wang, Xinggong Zhang, Zongming Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10001v2.pdf)  
  Keywords: geometry, fast, gaussian splatting, ar, 3d gaussian  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, efficient, dynamic, nerf, ar, acceleration  
- **[TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting](https://arxiv.org/abs/2504.09588v1)**  
  Authors: Zhicong Wu, Hongbin Xu, Gang Xu, Ping Nie, Zhixin Yan, Jinkai Zheng, Liangqiong Qu, Ming Li, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09588v1.pdf)  
  Keywords: segmentation, 3d reconstruction, understanding, semantic, gaussian splatting, high-fidelity, ar, 3d gaussian  
- **[DropoutGS: Dropping Out Gaussians for Better Sparse-view Rendering](https://arxiv.org/abs/2504.09491v1)**  
  Authors: Yexing Xu, Longguang Wang, Minglin Chen, Sheng Ao, Li Li, Yulan Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuyx55.github.io/DropoutGS/.)  
  Keywords: sparse-view, sparse view, gaussian splatting, ar, 3d gaussian  
- **[A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds](https://arxiv.org/abs/2504.09129v1)**  
  Authors: Jizong Peng, Tze Ho Elden Tse, Kai Xu, Wenchao Gao, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09129v1.pdf)  
  Keywords: motion, 3d reconstruction, geometry, gaussian splatting, high-fidelity, ar, 3d gaussian  
- **[BIGS: Bimanual Category-agnostic Interaction Reconstruction from Monocular Videos via 3D Gaussian Splatting](https://arxiv.org/abs/2504.09097v1)**  
  Authors: Jeongwan On, Kyeonghwan Gwak, Gunyoung Kang, Junuk Cha, Soohyun Hwang, Hyein Hwang, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09097v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar  

### Avatar Generation

*Showing the latest 50 out of 555 papers*

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: human, relighting, geometry, fast, gaussian splatting, avatar, shadow, ar, lighting, ray tracing, relightable  
- **[You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting](https://arxiv.org/abs/2504.09062v1)**  
  Authors: Zhijie Shen, Chunyu Lin, Shujuan Huang, Lang Nie, Kang Liao, Yao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09062v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhijieshen-bjtu/TPGS?style=social)](https://github.com/zhijieshen-bjtu/TPGS)  
  Keywords: 3d reconstruction, face, gaussian splatting, outdoor, ar, 3d gaussian  
- **[FMLGS: Fast Multilevel Language Embedded Gaussians for Part-level Interactive Agents](https://arxiv.org/abs/2504.08581v1)**  
  Authors: Xin Tan, Yuzhou Ji, He Zhu, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08581v1.pdf)  
  Keywords: understanding, semantic, face, fast, efficient, gaussian splatting, ar, 3d gaussian  
- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: ar, human, body, vr, geometry, face, gaussian splatting, high-fidelity, shadow, dynamic, head, 3d gaussian, avatar  
- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: human, mapping, ar, deformation, 3d gaussian  
- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: ar, segmentation, 3d reconstruction, understanding, gaussian splatting, nerf, head, 3d gaussian  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: ar, human, body, sparse-view, head, 3d gaussian, avatar  
- **[SE4Lip: Speech-Lip Encoder for Talking Head Synthesis to Solve Phoneme-Viseme Alignment Ambiguity](https://arxiv.org/abs/2504.05803v1)**  
  Authors: Yihuan Huang, Jiajun Liu, Yanzhen Ren, Wuyang Liu, Juhua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05803v1.pdf)  
  Keywords: ar, nerf, head  
- **[View-Dependent Deformation Fields for 2D Editing of 3D Models](https://arxiv.org/abs/2504.05544v1)**  
  Authors: Martin El Mqirmi, Noam Aigerman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05544v1.pdf)  
  Keywords: deformation, human, 3d gaussian, ar  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: ar, high quality, efficient, head, efficient rendering, 3d gaussian  

### Dynamic Scene

*Showing the latest 50 out of 626 papers*

- **[LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2504.10331v1)**  
  Authors: Hao Sun, Fenggen Yu, Huiyao Xu, Tao Zhang, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10331v1.pdf)  
  Keywords: 3d reconstruction, fast, gaussian splatting, real-time rendering, illumination, dynamic, nerf, ar, 3d gaussian  
- **[EBAD-Gaussian: Event-driven Bundle Adjusted Deblur Gaussian Splatting](https://arxiv.org/abs/2504.10012v1)**  
  Authors: Yufei Deng, Yuanjian Wang, Rong Xiao, Chenwei Tang, Jizhe Zhou, Jiahao Fan, Deng Xiong, Jiancheng Lv, Huajin Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10012v1.pdf)  
  Keywords: motion, gaussian splatting, dynamic, ar, 3d gaussian  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, efficient, dynamic, nerf, ar, acceleration  
- **[A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds](https://arxiv.org/abs/2504.09129v1)**  
  Authors: Jizong Peng, Tze Ho Elden Tse, Kai Xu, Wenchao Gao, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09129v1.pdf)  
  Keywords: motion, 3d reconstruction, geometry, gaussian splatting, high-fidelity, ar, 3d gaussian  
- **[In-2-4D: Inbetweening from Two Single-View Images to 4D Generation](https://arxiv.org/abs/2504.08366v1)**  
  Authors: Sauradip Nag, Daniel Cohen-Or, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08366v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://in-2-4d.github.io/)  
  Keywords: motion, gaussian splatting, dynamic, ar, deformation, 4d  
- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: ar, human, body, vr, geometry, face, gaussian splatting, high-fidelity, shadow, dynamic, head, 3d gaussian, avatar  
- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: human, mapping, ar, deformation, 3d gaussian  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: 3d reconstruction, fast, efficient, gaussian splatting, robotics, dynamic, ar  
- **[Collision avoidance from monocular vision trained with novel view synthesis](https://arxiv.org/abs/2504.06651v1)**  
  Authors: Valentin Tordjman--Levavasseur, Stéphane Caron  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06651v1.pdf)  
  Keywords: motion, gaussian splatting, ar  
- **[HiMoR: Monocular Deformable Gaussian Reconstruction with Hierarchical Motion Representation](https://arxiv.org/abs/2504.06210v1)**  
  Authors: Yiming Liang, Tianhan Xu, Yuta Kikuchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06210v1.pdf)  
  Keywords: motion, 3d reconstruction, dynamic, ar, deformation, 3d gaussian  

### Few-shot

*Showing the latest 50 out of 116 papers*

- **[DropoutGS: Dropping Out Gaussians for Better Sparse-view Rendering](https://arxiv.org/abs/2504.09491v1)**  
  Authors: Yexing Xu, Longguang Wang, Minglin Chen, Sheng Ao, Li Li, Yulan Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuyx55.github.io/DropoutGS/.)  
  Keywords: sparse-view, sparse view, gaussian splatting, ar, 3d gaussian  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: ar, human, body, sparse-view, head, 3d gaussian, avatar  
- **[DropGaussian: Structural Regularization for Sparse-view Gaussian Splatting](https://arxiv.org/abs/2504.00773v1)**  
  Authors: Hyunwoo Park, Gun Ryu, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DCVL-3D/DropGaussian?style=social)](https://github.com/DCVL-3D/DropGaussian)  
  Keywords: sparse-view, face, fast, gaussian splatting, ar, 3d gaussian  
- **[Coca-Splat: Collaborative Optimization for Camera Parameters and 3D Gaussians](https://arxiv.org/abs/2504.00639v1)**  
  Authors: Jiamin Wu, Hongyang Li, Xiaoke Jiang, Yuan Yao, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00639v1.pdf)  
  Keywords: 3d gaussian, sparse view, ar  
- **[Distilling Multi-view Diffusion Models into 3D Generators](https://arxiv.org/abs/2504.00457v3)**  
  Authors: Hao Qin, Luyuan Chen, Ming Kong, Mengxu Lu, Qiang Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00457v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://qinbaigao.github.io/DD3G_project/)  
  Keywords: sparse-view, efficient, gaussian splatting, ar, 3d gaussian  
- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: 3d reconstruction, sparse-view, geometry, face, gaussian splatting, ar, neural rendering  
- **[FreeSplat++: Generalizable 3D Gaussian Splatting for Efficient Indoor Scene Reconstruction](https://arxiv.org/abs/2503.22986v1)**  
  Authors: Yunsong Wang, Tianxin Huang, Hanlin Chen, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22986v1.pdf)  
  Keywords: sparse view, efficient, gaussian splatting, ar, 3d gaussian  
- **[CoMapGS: Covisibility Map-based Gaussian Splatting for Sparse Novel View Synthesis](https://arxiv.org/abs/2503.20998v1)**  
  Authors: Youngkyoon Jang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20998v1.pdf)  
  Keywords: few-shot, gaussian splatting, nerf, ar  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: sparse-view, gaussian splatting, illumination, outdoor, ar, 3d gaussian  
- **[NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting](https://arxiv.org/abs/2503.18794v1)**  
  Authors: Yulong Zheng, Zicheng Jiang, Shengfeng He, Yandu Sun, Junyu Dong, Huaidong Zhang, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18794v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://usmizuki.github.io/NexusGS/.)  
  Keywords: sparse-view, geometry, sparse view, gaussian splatting, few-shot, nerf, ar, 3d gaussian  

### Geometry Reconstruction

*Showing the latest 50 out of 533 papers*

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: human, relighting, geometry, fast, gaussian splatting, avatar, shadow, ar, lighting, ray tracing, relightable  
- **[LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2504.10331v1)**  
  Authors: Hao Sun, Fenggen Yu, Huiyao Xu, Tao Zhang, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10331v1.pdf)  
  Keywords: 3d reconstruction, fast, gaussian splatting, real-time rendering, illumination, dynamic, nerf, ar, 3d gaussian  
- **[GaussVideoDreamer: 3D Scene Generation with Video Diffusion and Inconsistency-Aware Gaussian Splatting](https://arxiv.org/abs/2504.10001v2)**  
  Authors: Junlin Hao, Peiheng Wang, Haoyang Wang, Xinggong Zhang, Zongming Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10001v2.pdf)  
  Keywords: geometry, fast, gaussian splatting, ar, 3d gaussian  
- **[TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting](https://arxiv.org/abs/2504.09588v1)**  
  Authors: Zhicong Wu, Hongbin Xu, Gang Xu, Ping Nie, Zhixin Yan, Jinkai Zheng, Liangqiong Qu, Ming Li, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09588v1.pdf)  
  Keywords: segmentation, 3d reconstruction, understanding, semantic, gaussian splatting, high-fidelity, ar, 3d gaussian  
- **[A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds](https://arxiv.org/abs/2504.09129v1)**  
  Authors: Jizong Peng, Tze Ho Elden Tse, Kai Xu, Wenchao Gao, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09129v1.pdf)  
  Keywords: motion, 3d reconstruction, geometry, gaussian splatting, high-fidelity, ar, 3d gaussian  
- **[You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting](https://arxiv.org/abs/2504.09062v1)**  
  Authors: Zhijie Shen, Chunyu Lin, Shujuan Huang, Lang Nie, Kang Liao, Yao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09062v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhijieshen-bjtu/TPGS?style=social)](https://github.com/zhijieshen-bjtu/TPGS)  
  Keywords: 3d reconstruction, face, gaussian splatting, outdoor, ar, 3d gaussian  
- **[BlockGaussian: Efficient Large-Scale Scene Novel View Synthesis via Adaptive Block-Based Gaussian Splatting](https://arxiv.org/abs/2504.09048v2)**  
  Authors: Yongchang Wu, Zipeng Qi, Zhenwei Shi, Zhengxia Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09048v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunshineWYC/BlockGaussian?style=social)](https://github.com/SunshineWYC/BlockGaussian)  
  Keywords: vr, geometry, efficient, gaussian splatting, ar, 3d gaussian  
- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: ar, human, body, vr, geometry, face, gaussian splatting, high-fidelity, shadow, dynamic, head, 3d gaussian, avatar  
- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: ar, segmentation, 3d reconstruction, understanding, gaussian splatting, nerf, head, 3d gaussian  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: 3d reconstruction, fast, efficient, gaussian splatting, robotics, dynamic, ar  

### Large Scene

*Showing the latest 50 out of 90 papers*

- **[You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting](https://arxiv.org/abs/2504.09062v1)**  
  Authors: Zhijie Shen, Chunyu Lin, Shujuan Huang, Lang Nie, Kang Liao, Yao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09062v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhijieshen-bjtu/TPGS?style=social)](https://github.com/zhijieshen-bjtu/TPGS)  
  Keywords: 3d reconstruction, face, gaussian splatting, outdoor, ar, 3d gaussian  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: motion, ar, reflection, gaussian splatting, outdoor, nerf  
- **[UnIRe: Unsupervised Instance Decomposition for Dynamic Urban Scene Reconstruction](https://arxiv.org/abs/2504.00763v1)**  
  Authors: Yunxuan Mao, Rong Xiong, Yue Wang, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00763v1.pdf)  
  Keywords: gaussian splatting, autonomous driving, dynamic, ar, 3d gaussian, urban scene, 4d  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: ar, reflection, geometry, fast, high-fidelity, gaussian splatting, efficient, dynamic, nerf, outdoor  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: motion, geometry, gaussian splatting, dynamic, ar, urban scene  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: fast, gaussian splatting, efficient, autonomous driving, real-time rendering, nerf, ar, 3d gaussian, urban scene  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: sparse-view, gaussian splatting, illumination, outdoor, ar, 3d gaussian  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: efficient, gaussian splatting, localization, outdoor, ar  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: geometry, fast, gaussian splatting, efficient, real-time rendering, outdoor, ar, 3d gaussian  
- **[PanopticSplatting: End-to-End Panoptic Gaussian Splatting](https://arxiv.org/abs/2503.18073v1)**  
  Authors: Yuxuan Xie, Xuan Yu, Changjian Jiang, Sitong Mao, Shunbo Zhou, Rui Fan, Rong Xiong, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18073v1.pdf)  
  Keywords: segmentation, understanding, large scene, gaussian splatting, nerf, ar  

### Model Compression

*Showing the latest 50 out of 625 papers*

- **[ESCT3D: Efficient and Selectively Controllable Text-Driven 3D Content Generation with Gaussian Splatting](https://arxiv.org/abs/2504.10316v1)**  
  Authors: Huiqi Wu, Jianbo Mei, Yingjie Huang, Yining Xu, Jingjiao You, Yilong Liu, Li Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10316v1.pdf)  
  Keywords: efficient, gaussian splatting, ar  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, efficient, dynamic, nerf, ar, acceleration  
- **[BlockGaussian: Efficient Large-Scale Scene Novel View Synthesis via Adaptive Block-Based Gaussian Splatting](https://arxiv.org/abs/2504.09048v2)**  
  Authors: Yongchang Wu, Zipeng Qi, Zhenwei Shi, Zhengxia Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09048v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunshineWYC/BlockGaussian?style=social)](https://github.com/SunshineWYC/BlockGaussian)  
  Keywords: vr, geometry, efficient, gaussian splatting, ar, 3d gaussian  
- **[FMLGS: Fast Multilevel Language Embedded Gaussians for Part-level Interactive Agents](https://arxiv.org/abs/2504.08581v1)**  
  Authors: Xin Tan, Yuzhou Ji, He Zhu, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08581v1.pdf)  
  Keywords: understanding, semantic, face, fast, efficient, gaussian splatting, ar, 3d gaussian  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: 3d reconstruction, fast, efficient, gaussian splatting, robotics, dynamic, ar  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: relighting, gaussian splatting, lighting, efficient, ar, efficient rendering, 3d gaussian, acceleration, ray tracing  
- **[econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians](https://arxiv.org/abs/2504.06003v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06003v1.pdf)  
  Keywords: segmentation, efficient, semantic, ar  
- **[Micro-splatting: Maximizing Isotropic Constraints for Refined Optimization in 3D Gaussian Splatting](https://arxiv.org/abs/2504.05740v1)**  
  Authors: Jee Won Lee, Hansol Lim, Sooyeun Yang, Jongseong Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05740v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, real-time rendering, dynamic, compact, ar, 3d gaussian  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: ar, high quality, efficient, head, efficient rendering, 3d gaussian  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: gaussian splatting, efficient, ray marching, dynamic, compact, ar, acceleration, 3d gaussian, animation  

### Quality Enhancement

*Showing the latest 50 out of 268 papers*

- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, efficient, dynamic, nerf, ar, acceleration  
- **[TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting](https://arxiv.org/abs/2504.09588v1)**  
  Authors: Zhicong Wu, Hongbin Xu, Gang Xu, Ping Nie, Zhixin Yan, Jinkai Zheng, Liangqiong Qu, Ming Li, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09588v1.pdf)  
  Keywords: segmentation, 3d reconstruction, understanding, semantic, gaussian splatting, high-fidelity, ar, 3d gaussian  
- **[A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds](https://arxiv.org/abs/2504.09129v1)**  
  Authors: Jizong Peng, Tze Ho Elden Tse, Kai Xu, Wenchao Gao, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09129v1.pdf)  
  Keywords: motion, 3d reconstruction, geometry, gaussian splatting, high-fidelity, ar, 3d gaussian  
- **[ContrastiveGaussian: High-Fidelity 3D Generation with Contrastive Learning and Gaussian Splatting](https://arxiv.org/abs/2504.08100v1)**  
  Authors: Junbang Liu, Enpei Huang, Dongxing Mao, Hui Zhang, Xinyuan Song, Yongxin Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08100v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, ar  
- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: ar, human, body, vr, geometry, face, gaussian splatting, high-fidelity, shadow, dynamic, head, 3d gaussian, avatar  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: ar, high quality, efficient, head, efficient rendering, 3d gaussian  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: slam, gaussian splatting, high-fidelity, tracking, mapping, localization, dynamic, ar, 3d gaussian, 4d  
- **[UAVTwin: Neural Digital Twins for UAVs using Gaussian Splatting](https://arxiv.org/abs/2504.02158v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02158v1.pdf)  
  Keywords: motion, human, high quality, gaussian splatting, high-fidelity, dynamic, ar, 3d gaussian, neural rendering  
- **[BOGausS: Better Optimized Gaussian Splatting](https://arxiv.org/abs/2504.01844v1)**  
  Authors: Stéphane Pateux, Matthieu Gendrin, Luce Morin, Théo Ladune, Xiaoran Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01844v1.pdf)  
  Keywords: fast, high-fidelity, gaussian splatting, efficient, nerf, ar, 3d gaussian  
- **[RealityAvatar: Towards Realistic Loose Clothing Modeling in Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2504.01559v1)**  
  Authors: Yahui Li, Zhi Zeng, Liming Pang, Guixuan Zhang, Shuwu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01559v1.pdf)  
  Keywords: motion, human, high-fidelity, gaussian splatting, efficient, dynamic, nerf, ar, deformation, 3d gaussian, avatar  

### Ray Tracing

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: human, relighting, geometry, fast, gaussian splatting, avatar, shadow, ar, lighting, ray tracing, relightable  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: relighting, gaussian splatting, lighting, efficient, ar, efficient rendering, 3d gaussian, acceleration, ray tracing  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: gaussian splatting, efficient, ray marching, dynamic, compact, ar, acceleration, 3d gaussian, animation  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: face, gaussian splatting, efficient, real-time rendering, global illumination, illumination, ar, lighting, 3d gaussian, ray tracing  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: light transport, face, fast, real-time rendering, global illumination, illumination, dynamic, lighting, 3d gaussian  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: reflection, fast, gaussian splatting, shadow, ar, 3d gaussian, ray tracing, neural rendering  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: geometry, face, efficient, tracking, real-time rendering, dynamic, ar, lighting, ray tracing, relightable, 4d  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: reflection, face, gaussian splatting, ray tracing, shadow, lighting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, gaussian splatting, ar, 3d gaussian, ray tracing  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: light transport, reflection, gaussian splatting, efficient, ar, acceleration, ray tracing  

### Relighting

*Showing the latest 50 out of 184 papers*

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: human, relighting, geometry, fast, gaussian splatting, avatar, shadow, ar, lighting, ray tracing, relightable  
- **[LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2504.10331v1)**  
  Authors: Hao Sun, Fenggen Yu, Huiyao Xu, Tao Zhang, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10331v1.pdf)  
  Keywords: 3d reconstruction, fast, gaussian splatting, real-time rendering, illumination, dynamic, nerf, ar, 3d gaussian  
- **[Cut-and-Splat: Leveraging Gaussian Splatting for Synthetic Data Generation](https://arxiv.org/abs/2504.08473v1)**  
  Authors: Bram Vanherle, Brent Zoomers, Jeroen Put, Frank Van Reeth, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08473v1.pdf)  
  Keywords: segmentation, lighting, gaussian splatting, ar  
- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: ar, human, body, vr, geometry, face, gaussian splatting, high-fidelity, shadow, dynamic, head, 3d gaussian, avatar  
- **[SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2504.06815v1)**  
  Authors: Hanxiao Sun, YuPeng Gao, Jin Xie, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06815v1.pdf)  
  Keywords: relighting, gaussian splatting, real-time rendering, illumination, nerf, ar, lighting, 3d gaussian  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: relighting, gaussian splatting, lighting, efficient, ar, efficient rendering, 3d gaussian, acceleration, ray tracing  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: motion, ar, reflection, gaussian splatting, outdoor, nerf  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: gaussian splatting, mapping, real-time rendering, nerf, ar, 3d gaussian, lighting  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: face, gaussian splatting, efficient, real-time rendering, global illumination, illumination, ar, lighting, 3d gaussian, ray tracing  
- **[LITA-GS: Illumination-Agnostic Novel View Synthesis via Reference-Free 3D Gaussian Splatting and Physical Priors](https://arxiv.org/abs/2504.00219v1)**  
  Authors: Han Zhou, Wei Dong, Jun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00219v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LowLevelAI/LITA-GS?style=social)](https://github.com/LowLevelAI/LITA-GS)  
  Keywords: motion, fast, gaussian splatting, illumination, nerf, ar, lighting, 3d gaussian  

### SLAM

*Showing the latest 50 out of 244 papers*

- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: human, mapping, ar, deformation, 3d gaussian  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: slam, gaussian splatting, high-fidelity, tracking, mapping, localization, dynamic, ar, 3d gaussian, 4d  
- **[WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2504.03886v1)**  
  Authors: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys, Songyou Peng, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03886v1.pdf)  
  Keywords: slam, efficient, tracking, gaussian splatting, mapping, dynamic, ar  
- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: slam, face, fast, gaussian splatting, tracking, mapping, localization, dynamic, ar, 3d gaussian  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: gaussian splatting, mapping, real-time rendering, nerf, ar, 3d gaussian, lighting  
- **[Visual Acoustic Fields](https://arxiv.org/abs/2503.24270v2)**  
  Authors: Yuelei Li, Hyunjin Kim, Fangneng Zhan, Ri-Zhao Qiu, Mazeyu Ji, Xiaojun Shan, Xueyan Zou, Paul Liang, Hanspeter Pfister, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24270v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuelei0428.github.io/projects/Visual-Acoustic-Fields/.)  
  Keywords: human, gaussian splatting, localization, ar, 3d gaussian  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: segmentation, understanding, semantic, gaussian splatting, localization, robotics, ar, 3d gaussian  
- **[VizFlyt: Perception-centric Pedagogical Framework For Autonomous Aerial Robots](https://arxiv.org/abs/2503.22876v2)**  
  Authors: Kushagra Srivastava, Rutwik Kulkarni, Manoj Velmurugan, Nitin J. Sanket  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22876v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pear.wpi.edu/research/vizflyt.html)  
  Keywords: efficient, gaussian splatting, localization, robotics, ar, 3d gaussian  
- **[Time-resolved dynamic CBCT reconstruction using prior-model-free spatiotemporal Gaussian representation (PMF-STGR)](https://arxiv.org/abs/2503.22139v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22139v1.pdf)  
  Keywords: motion, fast, efficient, localization, dynamic, ar, deformation, 3d gaussian  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: slam, semantic, high-fidelity, mapping, localization, robotics, dynamic, ar, 3d gaussian  

### Scene Understanding

*Showing the latest 50 out of 291 papers*

- **[TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting](https://arxiv.org/abs/2504.09588v1)**  
  Authors: Zhicong Wu, Hongbin Xu, Gang Xu, Ping Nie, Zhixin Yan, Jinkai Zheng, Liangqiong Qu, Ming Li, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09588v1.pdf)  
  Keywords: segmentation, 3d reconstruction, understanding, semantic, gaussian splatting, high-fidelity, ar, 3d gaussian  
- **[FMLGS: Fast Multilevel Language Embedded Gaussians for Part-level Interactive Agents](https://arxiv.org/abs/2504.08581v1)**  
  Authors: Xin Tan, Yuzhou Ji, He Zhu, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08581v1.pdf)  
  Keywords: understanding, semantic, face, fast, efficient, gaussian splatting, ar, 3d gaussian  
- **[Cut-and-Splat: Leveraging Gaussian Splatting for Synthetic Data Generation](https://arxiv.org/abs/2504.08473v1)**  
  Authors: Bram Vanherle, Brent Zoomers, Jeroen Put, Frank Van Reeth, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08473v1.pdf)  
  Keywords: segmentation, lighting, gaussian splatting, ar  
- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: ar, segmentation, 3d reconstruction, understanding, gaussian splatting, nerf, head, 3d gaussian  
- **[IAAO: Interactive Affordance Learning for Articulated Objects in 3D Environments](https://arxiv.org/abs/2504.06827v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06827v1.pdf)  
  Keywords: 3d gaussian, understanding, gaussian splatting, ar  
- **[econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians](https://arxiv.org/abs/2504.06003v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06003v1.pdf)  
  Keywords: segmentation, efficient, semantic, ar  
- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: human, 3d reconstruction, segmentation, face, efficient, gaussian splatting, dynamic, ar  
- **[Interpretable Single-View 3D Gaussian Splatting using Unsupervised Hierarchical Disentangled Representation Learning](https://arxiv.org/abs/2504.04190v1)**  
  Authors: Yuyang Zhang, Baao Xie, Hu Zhu, Qi Wang, Huanting Guo, Xin Jin, Wenjun Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04190v1.pdf)  
  Keywords: 3d reconstruction, understanding, semantic, geometry, gaussian splatting, ar, 3d gaussian  
- **[Scene4U: Hierarchical Layered 3D Scene Reconstruction from Single Panoramic Image for Your Immerse Exploration](https://arxiv.org/abs/2504.00387v1)**  
  Authors: Zilong Huang, Jun He, Junyan Ye, Lihan Jiang, Weijia Li, Yiping Chen, Ting Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00387v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LongHZ140516/Scene4U?style=social)](https://github.com/LongHZ140516/Scene4U)  
  Keywords: segmentation, semantic, fast, gaussian splatting, dynamic, ar, 3d gaussian  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: segmentation, understanding, semantic, gaussian splatting, localization, robotics, ar, 3d gaussian  



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