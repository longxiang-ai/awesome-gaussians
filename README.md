# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-04-17 00:52:25

## Categories

- [3DGS Surveys](#3dgs-surveys) (26 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (474 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1659 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (557 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (627 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (116 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (534 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (90 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (628 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (269 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (39 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (186 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (244 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (293 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: survey, 3d gaussian, dynamic, motion, 3d reconstruction, ar, lighting, fast, gaussian splatting  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: real-time rendering, survey, 3d gaussian, dynamic, ar, gaussian splatting  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: semantic, survey, ar, geometry  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: nerf, real-time rendering, efficient, 3d gaussian, survey, ar, 3d reconstruction, compression, gaussian splatting  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: nerf, 4d, deformation, survey, dynamic, motion, ar, lighting, gaussian splatting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, 3d gaussian, ar, ray tracing, gaussian splatting  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: tracking, outdoor, survey, dynamic, ar, geometry, mapping, lighting, localization, face, slam  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: recognition, survey, 3d gaussian, ar, illumination, gaussian splatting  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: nerf, semantic, robotics, autonomous driving, survey, dynamic, ar, 3d reconstruction, geometry, lighting, compact, high-fidelity, gaussian splatting  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: nerf, real-time rendering, robotics, survey, 3d gaussian, ar, understanding, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 474 papers*

- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: real-time rendering, efficient, human, 3d gaussian, recognition, ar, lighting, high-fidelity, gaussian splatting, head  
- **[3D Gabor Splatting: Reconstruction of High-frequency Surface Texture using Gabor Noise](https://arxiv.org/abs/2504.11003v1)**  
  Authors: Haato Watanabe, Kenji Tojo, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11003v1.pdf)  
  Keywords: lightweight, 3d gaussian, ar, fast, face, gaussian splatting  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: shadow, human, relighting, ar, ray tracing, geometry, lighting, fast, avatar, relightable, gaussian splatting  
- **[LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2504.10331v2)**  
  Authors: Hao Sun, Fenggen Yu, Huiyao Xu, Tao Zhang, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10331v2.pdf)  
  Keywords: nerf, real-time rendering, 3d gaussian, dynamic, ar, 3d reconstruction, illumination, fast, gaussian splatting  
- **[GaussVideoDreamer: 3D Scene Generation with Video Diffusion and Inconsistency-Aware Gaussian Splatting](https://arxiv.org/abs/2504.10001v3)**  
  Authors: Junlin Hao, Peiheng Wang, Haoyang Wang, Xinggong Zhang, Zongming Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10001v3.pdf)  
  Keywords: 3d gaussian, ar, geometry, fast, gaussian splatting  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: nerf, efficient, dynamic, ar, acceleration, high-fidelity, gaussian splatting  
- **[FMLGS: Fast Multilevel Language Embedded Gaussians for Part-level Interactive Agents](https://arxiv.org/abs/2504.08581v1)**  
  Authors: Xin Tan, Yuzhou Ji, He Zhu, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08581v1.pdf)  
  Keywords: semantic, efficient, 3d gaussian, ar, fast, face, understanding, gaussian splatting  
- **[View-Dependent Uncertainty Estimation of 3D Gaussian Splatting](https://arxiv.org/abs/2504.07370v1)**  
  Authors: Chenyu Han, Corentin Dumery  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07370v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, fast  
- **[SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2504.06815v1)**  
  Authors: Hanxiao Sun, YuPeng Gao, Jin Xie, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06815v1.pdf)  
  Keywords: nerf, real-time rendering, relighting, 3d gaussian, ar, illumination, lighting, gaussian splatting  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: robotics, efficient, dynamic, ar, 3d reconstruction, fast, gaussian splatting  

### Applications

*Showing the latest 50 out of 1659 papers*

- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: real-time rendering, efficient, human, 3d gaussian, recognition, ar, lighting, high-fidelity, gaussian splatting, head  
- **[Easy3D: A Simple Yet Effective Method for 3D Interactive Segmentation](https://arxiv.org/abs/2504.11024v1)**  
  Authors: Andrea Simonelli, Norman Müller, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11024v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://simonelli-andrea.github.io/easy3d.)  
  Keywords: lightweight, efficient, segmentation, ar, 3d reconstruction, gaussian splatting  
- **[3D Gabor Splatting: Reconstruction of High-frequency Surface Texture using Gabor Noise](https://arxiv.org/abs/2504.11003v1)**  
  Authors: Haato Watanabe, Kenji Tojo, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11003v1.pdf)  
  Keywords: lightweight, 3d gaussian, ar, fast, face, gaussian splatting  
- **[GaSLight: Gaussian Splats for Spatially-Varying Lighting in HDR](https://arxiv.org/abs/2504.10809v1)**  
  Authors: Christophe Bolduc, Yannick Hold-Geoffroy, Zhixin Shu, Jean-François Lalonde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10809v1.pdf)  
  Keywords: ar, lighting, dynamic  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: shadow, human, relighting, ar, ray tracing, geometry, lighting, fast, avatar, relightable, gaussian splatting  
- **[LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2504.10331v2)**  
  Authors: Hao Sun, Fenggen Yu, Huiyao Xu, Tao Zhang, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10331v2.pdf)  
  Keywords: nerf, real-time rendering, 3d gaussian, dynamic, ar, 3d reconstruction, illumination, fast, gaussian splatting  
- **[ESCT3D: Efficient and Selectively Controllable Text-Driven 3D Content Generation with Gaussian Splatting](https://arxiv.org/abs/2504.10316v1)**  
  Authors: Huiqi Wu, Jianbo Mei, Yingjie Huang, Yining Xu, Jingjiao You, Yilong Liu, Li Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10316v1.pdf)  
  Keywords: efficient, gaussian splatting, ar  
- **[EBAD-Gaussian: Event-driven Bundle Adjusted Deblur Gaussian Splatting](https://arxiv.org/abs/2504.10012v1)**  
  Authors: Yufei Deng, Yuanjian Wang, Rong Xiao, Chenwei Tang, Jizhe Zhou, Jiahao Fan, Deng Xiong, Jiancheng Lv, Huajin Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10012v1.pdf)  
  Keywords: 3d gaussian, ar, dynamic, motion, gaussian splatting  
- **[GaussVideoDreamer: 3D Scene Generation with Video Diffusion and Inconsistency-Aware Gaussian Splatting](https://arxiv.org/abs/2504.10001v3)**  
  Authors: Junlin Hao, Peiheng Wang, Haoyang Wang, Xinggong Zhang, Zongming Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10001v3.pdf)  
  Keywords: 3d gaussian, ar, geometry, fast, gaussian splatting  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: nerf, efficient, dynamic, ar, acceleration, high-fidelity, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 557 papers*

- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: real-time rendering, efficient, human, 3d gaussian, recognition, ar, lighting, high-fidelity, gaussian splatting, head  
- **[3D Gabor Splatting: Reconstruction of High-frequency Surface Texture using Gabor Noise](https://arxiv.org/abs/2504.11003v1)**  
  Authors: Haato Watanabe, Kenji Tojo, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11003v1.pdf)  
  Keywords: lightweight, 3d gaussian, ar, fast, face, gaussian splatting  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: shadow, human, relighting, ar, ray tracing, geometry, lighting, fast, avatar, relightable, gaussian splatting  
- **[You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting](https://arxiv.org/abs/2504.09062v1)**  
  Authors: Zhijie Shen, Chunyu Lin, Shujuan Huang, Lang Nie, Kang Liao, Yao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09062v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhijieshen-bjtu/TPGS?style=social)](https://github.com/zhijieshen-bjtu/TPGS)  
  Keywords: outdoor, 3d gaussian, ar, 3d reconstruction, face, gaussian splatting  
- **[FMLGS: Fast Multilevel Language Embedded Gaussians for Part-level Interactive Agents](https://arxiv.org/abs/2504.08581v1)**  
  Authors: Xin Tan, Yuzhou Ji, He Zhu, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08581v1.pdf)  
  Keywords: semantic, efficient, 3d gaussian, ar, fast, face, understanding, gaussian splatting  
- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: shadow, human, body, 3d gaussian, vr, dynamic, ar, geometry, face, avatar, high-fidelity, gaussian splatting, head  
- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: deformation, human, 3d gaussian, ar, mapping  
- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: nerf, 3d gaussian, segmentation, ar, 3d reconstruction, understanding, gaussian splatting, head  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: human, body, 3d gaussian, ar, avatar, sparse-view, head  
- **[SE4Lip: Speech-Lip Encoder for Talking Head Synthesis to Solve Phoneme-Viseme Alignment Ambiguity](https://arxiv.org/abs/2504.05803v1)**  
  Authors: Yihuan Huang, Jiajun Liu, Yanzhen Ren, Wuyang Liu, Juhua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05803v1.pdf)  
  Keywords: nerf, head, ar  

### Dynamic Scene

*Showing the latest 50 out of 627 papers*

- **[GaSLight: Gaussian Splats for Spatially-Varying Lighting in HDR](https://arxiv.org/abs/2504.10809v1)**  
  Authors: Christophe Bolduc, Yannick Hold-Geoffroy, Zhixin Shu, Jean-François Lalonde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10809v1.pdf)  
  Keywords: ar, lighting, dynamic  
- **[LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2504.10331v2)**  
  Authors: Hao Sun, Fenggen Yu, Huiyao Xu, Tao Zhang, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10331v2.pdf)  
  Keywords: nerf, real-time rendering, 3d gaussian, dynamic, ar, 3d reconstruction, illumination, fast, gaussian splatting  
- **[EBAD-Gaussian: Event-driven Bundle Adjusted Deblur Gaussian Splatting](https://arxiv.org/abs/2504.10012v1)**  
  Authors: Yufei Deng, Yuanjian Wang, Rong Xiao, Chenwei Tang, Jizhe Zhou, Jiahao Fan, Deng Xiong, Jiancheng Lv, Huajin Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10012v1.pdf)  
  Keywords: 3d gaussian, ar, dynamic, motion, gaussian splatting  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: nerf, efficient, dynamic, ar, acceleration, high-fidelity, gaussian splatting  
- **[A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds](https://arxiv.org/abs/2504.09129v1)**  
  Authors: Jizong Peng, Tze Ho Elden Tse, Kai Xu, Wenchao Gao, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09129v1.pdf)  
  Keywords: 3d gaussian, ar, motion, 3d reconstruction, geometry, high-fidelity, gaussian splatting  
- **[In-2-4D: Inbetweening from Two Single-View Images to 4D Generation](https://arxiv.org/abs/2504.08366v1)**  
  Authors: Sauradip Nag, Daniel Cohen-Or, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08366v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://in-2-4d.github.io/)  
  Keywords: 4d, deformation, dynamic, motion, ar, gaussian splatting  
- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: shadow, human, body, 3d gaussian, vr, dynamic, ar, geometry, face, avatar, high-fidelity, gaussian splatting, head  
- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: deformation, human, 3d gaussian, ar, mapping  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: robotics, efficient, dynamic, ar, 3d reconstruction, fast, gaussian splatting  
- **[Collision avoidance from monocular vision trained with novel view synthesis](https://arxiv.org/abs/2504.06651v1)**  
  Authors: Valentin Tordjman--Levavasseur, Stéphane Caron  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06651v1.pdf)  
  Keywords: gaussian splatting, ar, motion  

### Few-shot

*Showing the latest 50 out of 116 papers*

- **[DropoutGS: Dropping Out Gaussians for Better Sparse-view Rendering](https://arxiv.org/abs/2504.09491v1)**  
  Authors: Yexing Xu, Longguang Wang, Minglin Chen, Sheng Ao, Li Li, Yulan Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuyx55.github.io/DropoutGS/.)  
  Keywords: 3d gaussian, ar, sparse view, sparse-view, gaussian splatting  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: human, body, 3d gaussian, ar, avatar, sparse-view, head  
- **[DropGaussian: Structural Regularization for Sparse-view Gaussian Splatting](https://arxiv.org/abs/2504.00773v1)**  
  Authors: Hyunwoo Park, Gun Ryu, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DCVL-3D/DropGaussian?style=social)](https://github.com/DCVL-3D/DropGaussian)  
  Keywords: 3d gaussian, ar, fast, face, sparse-view, gaussian splatting  
- **[Coca-Splat: Collaborative Optimization for Camera Parameters and 3D Gaussians](https://arxiv.org/abs/2504.00639v1)**  
  Authors: Jiamin Wu, Hongyang Li, Xiaoke Jiang, Yuan Yao, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00639v1.pdf)  
  Keywords: sparse view, 3d gaussian, ar  
- **[Distilling Multi-view Diffusion Models into 3D Generators](https://arxiv.org/abs/2504.00457v3)**  
  Authors: Hao Qin, Luyuan Chen, Ming Kong, Mengxu Lu, Qiang Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00457v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://qinbaigao.github.io/DD3G_project/)  
  Keywords: efficient, 3d gaussian, ar, sparse-view, gaussian splatting  
- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: neural rendering, ar, 3d reconstruction, geometry, face, sparse-view, gaussian splatting  
- **[FreeSplat++: Generalizable 3D Gaussian Splatting for Efficient Indoor Scene Reconstruction](https://arxiv.org/abs/2503.22986v1)**  
  Authors: Yunsong Wang, Tianxin Huang, Hanlin Chen, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22986v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, sparse view, gaussian splatting  
- **[CoMapGS: Covisibility Map-based Gaussian Splatting for Sparse Novel View Synthesis](https://arxiv.org/abs/2503.20998v1)**  
  Authors: Youngkyoon Jang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20998v1.pdf)  
  Keywords: nerf, few-shot, gaussian splatting, ar  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: outdoor, 3d gaussian, ar, illumination, sparse-view, gaussian splatting  
- **[NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting](https://arxiv.org/abs/2503.18794v1)**  
  Authors: Yulong Zheng, Zicheng Jiang, Shengfeng He, Yandu Sun, Junyu Dong, Huaidong Zhang, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18794v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://usmizuki.github.io/NexusGS/.)  
  Keywords: nerf, few-shot, 3d gaussian, ar, geometry, sparse view, sparse-view, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 534 papers*

- **[Easy3D: A Simple Yet Effective Method for 3D Interactive Segmentation](https://arxiv.org/abs/2504.11024v1)**  
  Authors: Andrea Simonelli, Norman Müller, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11024v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://simonelli-andrea.github.io/easy3d.)  
  Keywords: lightweight, efficient, segmentation, ar, 3d reconstruction, gaussian splatting  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: shadow, human, relighting, ar, ray tracing, geometry, lighting, fast, avatar, relightable, gaussian splatting  
- **[LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2504.10331v2)**  
  Authors: Hao Sun, Fenggen Yu, Huiyao Xu, Tao Zhang, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10331v2.pdf)  
  Keywords: nerf, real-time rendering, 3d gaussian, dynamic, ar, 3d reconstruction, illumination, fast, gaussian splatting  
- **[GaussVideoDreamer: 3D Scene Generation with Video Diffusion and Inconsistency-Aware Gaussian Splatting](https://arxiv.org/abs/2504.10001v3)**  
  Authors: Junlin Hao, Peiheng Wang, Haoyang Wang, Xinggong Zhang, Zongming Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10001v3.pdf)  
  Keywords: 3d gaussian, ar, geometry, fast, gaussian splatting  
- **[TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting](https://arxiv.org/abs/2504.09588v1)**  
  Authors: Zhicong Wu, Hongbin Xu, Gang Xu, Ping Nie, Zhixin Yan, Jinkai Zheng, Liangqiong Qu, Ming Li, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09588v1.pdf)  
  Keywords: semantic, 3d gaussian, segmentation, ar, 3d reconstruction, high-fidelity, understanding, gaussian splatting  
- **[A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds](https://arxiv.org/abs/2504.09129v1)**  
  Authors: Jizong Peng, Tze Ho Elden Tse, Kai Xu, Wenchao Gao, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09129v1.pdf)  
  Keywords: 3d gaussian, ar, motion, 3d reconstruction, geometry, high-fidelity, gaussian splatting  
- **[You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting](https://arxiv.org/abs/2504.09062v1)**  
  Authors: Zhijie Shen, Chunyu Lin, Shujuan Huang, Lang Nie, Kang Liao, Yao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09062v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhijieshen-bjtu/TPGS?style=social)](https://github.com/zhijieshen-bjtu/TPGS)  
  Keywords: outdoor, 3d gaussian, ar, 3d reconstruction, face, gaussian splatting  
- **[BlockGaussian: Efficient Large-Scale Scene Novel View Synthesis via Adaptive Block-Based Gaussian Splatting](https://arxiv.org/abs/2504.09048v2)**  
  Authors: Yongchang Wu, Zipeng Qi, Zhenwei Shi, Zhengxia Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09048v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunshineWYC/BlockGaussian?style=social)](https://github.com/SunshineWYC/BlockGaussian)  
  Keywords: efficient, vr, 3d gaussian, ar, geometry, gaussian splatting  
- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: shadow, human, body, 3d gaussian, vr, dynamic, ar, geometry, face, avatar, high-fidelity, gaussian splatting, head  
- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: nerf, 3d gaussian, segmentation, ar, 3d reconstruction, understanding, gaussian splatting, head  

### Large Scene

*Showing the latest 50 out of 90 papers*

- **[You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting](https://arxiv.org/abs/2504.09062v1)**  
  Authors: Zhijie Shen, Chunyu Lin, Shujuan Huang, Lang Nie, Kang Liao, Yao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09062v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhijieshen-bjtu/TPGS?style=social)](https://github.com/zhijieshen-bjtu/TPGS)  
  Keywords: outdoor, 3d gaussian, ar, 3d reconstruction, face, gaussian splatting  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: nerf, outdoor, ar, motion, gaussian splatting, reflection  
- **[UnIRe: Unsupervised Instance Decomposition for Dynamic Urban Scene Reconstruction](https://arxiv.org/abs/2504.00763v1)**  
  Authors: Yunxuan Mao, Rong Xiong, Yue Wang, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00763v1.pdf)  
  Keywords: 4d, urban scene, autonomous driving, 3d gaussian, dynamic, ar, gaussian splatting  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: nerf, outdoor, efficient, dynamic, ar, geometry, fast, high-fidelity, gaussian splatting, reflection  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: urban scene, dynamic, motion, ar, geometry, gaussian splatting  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: nerf, real-time rendering, urban scene, efficient, autonomous driving, 3d gaussian, ar, fast, gaussian splatting  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: outdoor, 3d gaussian, ar, illumination, sparse-view, gaussian splatting  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: outdoor, efficient, ar, localization, gaussian splatting  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: real-time rendering, outdoor, efficient, 3d gaussian, ar, geometry, fast, gaussian splatting  
- **[PanopticSplatting: End-to-End Panoptic Gaussian Splatting](https://arxiv.org/abs/2503.18073v1)**  
  Authors: Yuxuan Xie, Xuan Yu, Changjian Jiang, Sitong Mao, Shunbo Zhou, Rui Fan, Rong Xiong, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18073v1.pdf)  
  Keywords: nerf, segmentation, ar, large scene, understanding, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 628 papers*

- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: real-time rendering, efficient, human, 3d gaussian, recognition, ar, lighting, high-fidelity, gaussian splatting, head  
- **[Easy3D: A Simple Yet Effective Method for 3D Interactive Segmentation](https://arxiv.org/abs/2504.11024v1)**  
  Authors: Andrea Simonelli, Norman Müller, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11024v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://simonelli-andrea.github.io/easy3d.)  
  Keywords: lightweight, efficient, segmentation, ar, 3d reconstruction, gaussian splatting  
- **[3D Gabor Splatting: Reconstruction of High-frequency Surface Texture using Gabor Noise](https://arxiv.org/abs/2504.11003v1)**  
  Authors: Haato Watanabe, Kenji Tojo, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11003v1.pdf)  
  Keywords: lightweight, 3d gaussian, ar, fast, face, gaussian splatting  
- **[ESCT3D: Efficient and Selectively Controllable Text-Driven 3D Content Generation with Gaussian Splatting](https://arxiv.org/abs/2504.10316v1)**  
  Authors: Huiqi Wu, Jianbo Mei, Yingjie Huang, Yining Xu, Jingjiao You, Yilong Liu, Li Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10316v1.pdf)  
  Keywords: efficient, gaussian splatting, ar  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: nerf, efficient, dynamic, ar, acceleration, high-fidelity, gaussian splatting  
- **[BlockGaussian: Efficient Large-Scale Scene Novel View Synthesis via Adaptive Block-Based Gaussian Splatting](https://arxiv.org/abs/2504.09048v2)**  
  Authors: Yongchang Wu, Zipeng Qi, Zhenwei Shi, Zhengxia Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09048v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunshineWYC/BlockGaussian?style=social)](https://github.com/SunshineWYC/BlockGaussian)  
  Keywords: efficient, vr, 3d gaussian, ar, geometry, gaussian splatting  
- **[FMLGS: Fast Multilevel Language Embedded Gaussians for Part-level Interactive Agents](https://arxiv.org/abs/2504.08581v1)**  
  Authors: Xin Tan, Yuzhou Ji, He Zhu, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08581v1.pdf)  
  Keywords: semantic, efficient, 3d gaussian, ar, fast, face, understanding, gaussian splatting  
- **[GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction](https://arxiv.org/abs/2504.06716v1)**  
  Authors: Anil Armagan, Albert Saà-Garriga, Bruno Manganelli, Kyuwon Kim, M. Kerim Yucel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anilarmagan.github.io/SRUK-GSta.)  
  Keywords: robotics, efficient, dynamic, ar, 3d reconstruction, fast, gaussian splatting  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: efficient, 3d gaussian, efficient rendering, relighting, ar, ray tracing, acceleration, lighting, gaussian splatting  
- **[econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians](https://arxiv.org/abs/2504.06003v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06003v1.pdf)  
  Keywords: semantic, efficient, segmentation, ar  

### Quality Enhancement

*Showing the latest 50 out of 269 papers*

- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: real-time rendering, efficient, human, 3d gaussian, recognition, ar, lighting, high-fidelity, gaussian splatting, head  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: nerf, efficient, dynamic, ar, acceleration, high-fidelity, gaussian splatting  
- **[TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting](https://arxiv.org/abs/2504.09588v1)**  
  Authors: Zhicong Wu, Hongbin Xu, Gang Xu, Ping Nie, Zhixin Yan, Jinkai Zheng, Liangqiong Qu, Ming Li, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09588v1.pdf)  
  Keywords: semantic, 3d gaussian, segmentation, ar, 3d reconstruction, high-fidelity, understanding, gaussian splatting  
- **[A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds](https://arxiv.org/abs/2504.09129v1)**  
  Authors: Jizong Peng, Tze Ho Elden Tse, Kai Xu, Wenchao Gao, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09129v1.pdf)  
  Keywords: 3d gaussian, ar, motion, 3d reconstruction, geometry, high-fidelity, gaussian splatting  
- **[ContrastiveGaussian: High-Fidelity 3D Generation with Contrastive Learning and Gaussian Splatting](https://arxiv.org/abs/2504.08100v1)**  
  Authors: Junbang Liu, Enpei Huang, Dongxing Mao, Hui Zhang, Xinyuan Song, Yongxin Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08100v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar  
- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: shadow, human, body, 3d gaussian, vr, dynamic, ar, geometry, face, avatar, high-fidelity, gaussian splatting, head  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: high quality, efficient, 3d gaussian, efficient rendering, ar, head  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: 4d, 3d gaussian, dynamic, ar, localization, mapping, tracking, high-fidelity, gaussian splatting, slam  
- **[UAVTwin: Neural Digital Twins for UAVs using Gaussian Splatting](https://arxiv.org/abs/2504.02158v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02158v1.pdf)  
  Keywords: high quality, human, 3d gaussian, neural rendering, dynamic, motion, ar, high-fidelity, gaussian splatting  
- **[BOGausS: Better Optimized Gaussian Splatting](https://arxiv.org/abs/2504.01844v1)**  
  Authors: Stéphane Pateux, Matthieu Gendrin, Luce Morin, Théo Ladune, Xiaoran Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01844v1.pdf)  
  Keywords: nerf, efficient, 3d gaussian, ar, fast, high-fidelity, gaussian splatting  

### Ray Tracing

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: shadow, human, relighting, ar, ray tracing, geometry, lighting, fast, avatar, relightable, gaussian splatting  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: efficient, 3d gaussian, efficient rendering, relighting, ar, ray tracing, acceleration, lighting, gaussian splatting  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v1)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v1.pdf)  
  Keywords: efficient, 3d gaussian, dynamic, animation, ar, acceleration, compact, gaussian splatting, ray marching  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: real-time rendering, efficient, 3d gaussian, ar, ray tracing, global illumination, illumination, lighting, face, gaussian splatting  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: real-time rendering, light transport, 3d gaussian, dynamic, global illumination, illumination, lighting, fast, face  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: shadow, 3d gaussian, neural rendering, ar, ray tracing, fast, gaussian splatting, reflection  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, real-time rendering, efficient, dynamic, ar, ray tracing, geometry, lighting, face, relightable, tracking  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: shadow, ray tracing, lighting, face, gaussian splatting, reflection  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, 3d gaussian, ar, ray tracing, gaussian splatting  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: efficient, light transport, ar, ray tracing, acceleration, gaussian splatting, reflection  

### Relighting

*Showing the latest 50 out of 186 papers*

- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: real-time rendering, efficient, human, 3d gaussian, recognition, ar, lighting, high-fidelity, gaussian splatting, head  
- **[GaSLight: Gaussian Splats for Spatially-Varying Lighting in HDR](https://arxiv.org/abs/2504.10809v1)**  
  Authors: Christophe Bolduc, Yannick Hold-Geoffroy, Zhixin Shu, Jean-François Lalonde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10809v1.pdf)  
  Keywords: ar, lighting, dynamic  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: shadow, human, relighting, ar, ray tracing, geometry, lighting, fast, avatar, relightable, gaussian splatting  
- **[LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2504.10331v2)**  
  Authors: Hao Sun, Fenggen Yu, Huiyao Xu, Tao Zhang, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10331v2.pdf)  
  Keywords: nerf, real-time rendering, 3d gaussian, dynamic, ar, 3d reconstruction, illumination, fast, gaussian splatting  
- **[Cut-and-Splat: Leveraging Gaussian Splatting for Synthetic Data Generation](https://arxiv.org/abs/2504.08473v1)**  
  Authors: Bram Vanherle, Brent Zoomers, Jeroen Put, Frank Van Reeth, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08473v1.pdf)  
  Keywords: segmentation, gaussian splatting, lighting, ar  
- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: shadow, human, body, 3d gaussian, vr, dynamic, ar, geometry, face, avatar, high-fidelity, gaussian splatting, head  
- **[SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2504.06815v1)**  
  Authors: Hanxiao Sun, YuPeng Gao, Jin Xie, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06815v1.pdf)  
  Keywords: nerf, real-time rendering, relighting, 3d gaussian, ar, illumination, lighting, gaussian splatting  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: efficient, 3d gaussian, efficient rendering, relighting, ar, ray tracing, acceleration, lighting, gaussian splatting  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: nerf, outdoor, ar, motion, gaussian splatting, reflection  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: nerf, real-time rendering, 3d gaussian, ar, mapping, lighting, gaussian splatting  

### SLAM

*Showing the latest 50 out of 244 papers*

- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: deformation, human, 3d gaussian, ar, mapping  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: 4d, 3d gaussian, dynamic, ar, localization, mapping, tracking, high-fidelity, gaussian splatting, slam  
- **[WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2504.03886v1)**  
  Authors: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys, Songyou Peng, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03886v1.pdf)  
  Keywords: efficient, dynamic, ar, mapping, slam, gaussian splatting, tracking  
- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: tracking, 3d gaussian, dynamic, ar, localization, mapping, fast, face, gaussian splatting, slam  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: nerf, real-time rendering, 3d gaussian, ar, mapping, lighting, gaussian splatting  
- **[Visual Acoustic Fields](https://arxiv.org/abs/2503.24270v2)**  
  Authors: Yuelei Li, Hyunjin Kim, Fangneng Zhan, Ri-Zhao Qiu, Mazeyu Ji, Xiaojun Shan, Xueyan Zou, Paul Liang, Hanspeter Pfister, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24270v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuelei0428.github.io/projects/Visual-Acoustic-Fields/.)  
  Keywords: human, 3d gaussian, ar, localization, gaussian splatting  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: semantic, robotics, 3d gaussian, segmentation, ar, localization, understanding, gaussian splatting  
- **[VizFlyt: Perception-centric Pedagogical Framework For Autonomous Aerial Robots](https://arxiv.org/abs/2503.22876v2)**  
  Authors: Kushagra Srivastava, Rutwik Kulkarni, Manoj Velmurugan, Nitin J. Sanket  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22876v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pear.wpi.edu/research/vizflyt.html)  
  Keywords: robotics, efficient, 3d gaussian, ar, localization, gaussian splatting  
- **[Time-resolved dynamic CBCT reconstruction using prior-model-free spatiotemporal Gaussian representation (PMF-STGR)](https://arxiv.org/abs/2503.22139v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22139v1.pdf)  
  Keywords: deformation, efficient, 3d gaussian, dynamic, motion, ar, localization, fast  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: semantic, robotics, 3d gaussian, dynamic, ar, localization, mapping, high-fidelity, slam  

### Scene Understanding

*Showing the latest 50 out of 293 papers*

- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: real-time rendering, efficient, human, 3d gaussian, recognition, ar, lighting, high-fidelity, gaussian splatting, head  
- **[Easy3D: A Simple Yet Effective Method for 3D Interactive Segmentation](https://arxiv.org/abs/2504.11024v1)**  
  Authors: Andrea Simonelli, Norman Müller, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11024v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://simonelli-andrea.github.io/easy3d.)  
  Keywords: lightweight, efficient, segmentation, ar, 3d reconstruction, gaussian splatting  
- **[TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting](https://arxiv.org/abs/2504.09588v1)**  
  Authors: Zhicong Wu, Hongbin Xu, Gang Xu, Ping Nie, Zhixin Yan, Jinkai Zheng, Liangqiong Qu, Ming Li, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09588v1.pdf)  
  Keywords: semantic, 3d gaussian, segmentation, ar, 3d reconstruction, high-fidelity, understanding, gaussian splatting  
- **[FMLGS: Fast Multilevel Language Embedded Gaussians for Part-level Interactive Agents](https://arxiv.org/abs/2504.08581v1)**  
  Authors: Xin Tan, Yuzhou Ji, He Zhu, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08581v1.pdf)  
  Keywords: semantic, efficient, 3d gaussian, ar, fast, face, understanding, gaussian splatting  
- **[Cut-and-Splat: Leveraging Gaussian Splatting for Synthetic Data Generation](https://arxiv.org/abs/2504.08473v1)**  
  Authors: Bram Vanherle, Brent Zoomers, Jeroen Put, Frank Van Reeth, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08473v1.pdf)  
  Keywords: segmentation, gaussian splatting, lighting, ar  
- **[Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting](https://arxiv.org/abs/2504.06978v1)**  
  Authors: Daiwei Zhang, Joaquin Gajardo, Tomislav Medic, Isinsu Katircioglu, Mike Boss, Norbert Kirchgessner, Achim Walter, Lukas Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06978v1.pdf)  
  Keywords: nerf, 3d gaussian, segmentation, ar, 3d reconstruction, understanding, gaussian splatting, head  
- **[IAAO: Interactive Affordance Learning for Articulated Objects in 3D Environments](https://arxiv.org/abs/2504.06827v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06827v1.pdf)  
  Keywords: understanding, 3d gaussian, gaussian splatting, ar  
- **[econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians](https://arxiv.org/abs/2504.06003v1)**  
  Authors: Can Zhang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06003v1.pdf)  
  Keywords: semantic, efficient, segmentation, ar  
- **[Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning](https://arxiv.org/abs/2504.04612v1)**  
  Authors: Haonan Chen, Cheng Zhu, Yunzhu Li, Katherine Driggs-Campbell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04612v1.pdf)  
  Keywords: efficient, human, segmentation, dynamic, ar, 3d reconstruction, face, gaussian splatting  
- **[Interpretable Single-View 3D Gaussian Splatting using Unsupervised Hierarchical Disentangled Representation Learning](https://arxiv.org/abs/2504.04190v1)**  
  Authors: Yuyang Zhang, Baao Xie, Hu Zhu, Qi Wang, Huanting Guo, Xin Jin, Wenjun Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04190v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, 3d reconstruction, geometry, understanding, gaussian splatting  



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