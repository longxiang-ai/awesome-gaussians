# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-07-07 00:59:53

## 📰 Latest Updates

🔧 **[2025-06-26] HTTP 301 Redirect Issue Completely Resolved!** 
- Implemented multi-layer fallback strategy to thoroughly solve network compatibility issues

🔧 **[2025-06-26] Configurable Search Keywords Feature Added!**
- You can now customize search keywords by modifying `data/search_config.json`
- Support for different search scopes: abstract-only, title-only, or both
- Flexible keyword configuration for targeted paper collection

- View detailed updates: [News.md](News.md) 📋

---

## Categories

- [3DGS Surveys](#3dgs-surveys) (19 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (278 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (331 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (395 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (72 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (315 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (61 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (392 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (159 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (16 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (107 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (156 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (184 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: outdoor, nerf, efficient, dynamic, ar, high-fidelity, gaussian splatting, 3d gaussian, face, autonomous driving, survey  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: robotics, nerf, 3d reconstruction, ar, neural rendering, gaussian splatting, high-fidelity, vr, 3d gaussian, autonomous driving, survey  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: outdoor, efficient, semantic, understanding, 3d reconstruction, ar, neural rendering, gaussian splatting, high-fidelity, segmentation, 3d gaussian, survey  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: nerf, efficient, semantic, mapping, slam, ar, gaussian splatting, segmentation, 3d gaussian, localization, survey  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to
  Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: body, understanding, dynamic, 4d, motion, ar, gaussian splatting, 3d gaussian, survey  
- **[A Survey of 3D Reconstruction with Event Cameras](https://arxiv.org/abs/2505.08438v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v2.pdf)  
  Keywords: robotics, nerf, illumination, dynamic, 3d reconstruction, motion, ar, neural rendering, gaussian splatting, geometry, 3d gaussian, autonomous driving, survey  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: efficient, 3d reconstruction, ar, gaussian splatting, survey, fast  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d reconstruction, ar, lighting, 3d gaussian, survey  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From
  Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting
  (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf)  
  Keywords: sparse view, outdoor, nerf, understanding, 3d reconstruction, ar, geometry, gaussian splatting, 3d gaussian, face, survey  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf)  
  Keywords: robotics, semantic, lighting, ar, gaussian splatting, segmentation, 3d gaussian, survey  

### Acceleration

*Showing the latest 50 out of 278 papers*

- **[HyperGaussians: High-Dimensional Gaussian Splatting for High-Fidelity
  Animatable Face Avatars](https://arxiv.org/abs/2507.02803v1)**  
  Authors: Gent Serifi, Marcel C. Bühler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02803v1.pdf)  
  Keywords: reflection, lighting, high-fidelity, gaussian splatting, avatar, ar, 3d gaussian, face, deformation, fast  
- **[A LoD of Gaussians: Unified Training and Rendering for Ultra-Large Scale
  Reconstruction with External Memory](https://arxiv.org/abs/2507.01110v1)**  
  Authors: Felix Windisch, Lukas Radl, Thomas Köhler, Michael Steiner, Dieter Schmalstieg, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01110v1.pdf)  
  Keywords: efficient, dynamic, lightweight, ar, vr, gaussian splatting, real-time rendering  
- **[GaussianVLM: Scene-centric 3D Vision-Language Models using
  Language-aligned Gaussian Splats for Embodied Reasoning and Beyond](https://arxiv.org/abs/2507.00886v1)**  
  Authors: Anna-Maria Halacheva, Jan-Nico Zaech, Xi Wang, Danda Pani Paudel, Luc Van Gool  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00886v1.pdf)  
  Keywords: compact, understanding, ar, gaussian splatting, 3d gaussian, fast  
- **[GDGS: 3D Gaussian Splatting Via Geometry-Guided Initialization And
  Dynamic Density Control](https://arxiv.org/abs/2507.00363v1)**  
  Authors: Xingjun Wang, Lianlei Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00363v1.pdf)  
  Keywords: dynamic, ar, high-fidelity, gaussian splatting, geometry, 3d gaussian, face, real-time rendering, fast  
- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: efficient, ar, geometry, gaussian splatting, 3d gaussian, face, animation, fast  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: efficient rendering, nerf, efficient, 3d reconstruction, motion, ar, gaussian splatting, 3d gaussian, face  
- **[Confident Splatting: Confidence-Based Compression of 3D Gaussian
  Splatting via Learnable Beta Distributions](https://arxiv.org/abs/2506.22973v1)**  
  Authors: AmirHossein Naghi Razlighi, Elaheh Badali Golezani, Shohreh Kasaei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22973v1.pdf)  
  Keywords: head, compression, ar, gaussian splatting, 3d gaussian, real-time rendering  
- **[VoteSplat: Hough Voting Gaussian Splatting for 3D Scene Understanding](https://arxiv.org/abs/2506.22799v1)**  
  Authors: Minchao Jiang, Shunyu Jia, Jiaming Gu, Xiaoyuan Lu, Guangming Zhu, Anqi Dong, Liang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sy-ja.github.io/votesplat/)  
  Keywords: semantic, understanding, ar, gaussian splatting, segmentation, 3d gaussian, localization, real-time rendering  
- **[Geometry and Perception Guided Gaussians for Multiview-consistent 3D
  Generation from a Single Image](https://arxiv.org/abs/2506.21152v1)**  
  Authors: Pufan Li, Bi'an Du, Wei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21152v1.pdf)  
  Keywords: 3d reconstruction, ar, geometry, gaussian splatting, 3d gaussian, fast  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: ray tracing, efficient, ar, high-fidelity, gaussian splatting, real-time rendering  

### Applications

*Showing the latest 50 out of 995 papers*

- **[HyperGaussians: High-Dimensional Gaussian Splatting for High-Fidelity
  Animatable Face Avatars](https://arxiv.org/abs/2507.02803v1)**  
  Authors: Gent Serifi, Marcel C. Bühler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02803v1.pdf)  
  Keywords: reflection, lighting, high-fidelity, gaussian splatting, avatar, ar, 3d gaussian, face, deformation, fast  
- **[ArtGS:3D Gaussian Splatting for Interactive Visual-Physical Modeling and
  Manipulation of Articulated Objects](https://arxiv.org/abs/2507.02600v1)**  
  Authors: Qiaojun Yu, Xibin Yuan, Yu jiang, Junting Chen, Dongzhe Zheng, Ce Hao, Yang You, Yixing Chen, Yao Mu, Liu Liu, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02600v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sites.google.com/view/artgs/home)  
  Keywords: robotics, efficient, semantic, understanding, dynamic, motion, ar, gaussian splatting, 3d gaussian  
- **[LocalDyGS: Multi-view Global Dynamic Scene Modeling via Adaptive Local
  Implicit Feature Decoupling](https://arxiv.org/abs/2507.02363v1)**  
  Authors: Jiahao Wu, Rui Peng, Jianbo Jiao, Jiayu Yang, Luyang Tang, Kaiqiang Xiong, Jie Liang, Jinbo Yan, Runling Liu, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02363v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wujh2001.github.io/LocalDyGS/.)  
  Keywords: dynamic, motion, ar, gaussian splatting, 3d gaussian  
- **[Gbake: Baking 3D Gaussian Splats into Reflection Probes](https://arxiv.org/abs/2507.02257v1)**  
  Authors: Stephen Pasch, Joel K. Salzman, Changxi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02257v1.pdf)  
  Keywords: reflection, mapping, lighting, geometry, gaussian splatting, ar, 3d gaussian  
- **[3D Gaussian Splatting Driven Multi-View Robust Physical Adversarial
  Camouflage Generation](https://arxiv.org/abs/2507.01367v1)**  
  Authors: Tianrui Lou, Xiaojun Jia, Siyuan Liang, Jiawei Liang, Ming Zhang, Yanjun Xiao, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01367v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, autonomous driving  
- **[VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online
  Semantic Gaussian Splatting](https://arxiv.org/abs/2507.01125v1)**  
  Authors: Keiko Nagami, Timothy Chen, Javier Yu, Ola Shorinwa, Maximilian Adang, Carlyn Dougherty, Eric Cristofalo, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01125v1.pdf)  
  Keywords: efficient, semantic, ar, gaussian splatting, 3d gaussian  
- **[A LoD of Gaussians: Unified Training and Rendering for Ultra-Large Scale
  Reconstruction with External Memory](https://arxiv.org/abs/2507.01110v1)**  
  Authors: Felix Windisch, Lukas Radl, Thomas Köhler, Michael Steiner, Dieter Schmalstieg, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01110v1.pdf)  
  Keywords: efficient, dynamic, lightweight, ar, vr, gaussian splatting, real-time rendering  
- **[Masks make discriminative models great again!](https://arxiv.org/abs/2507.00916v1)**  
  Authors: Tianshi Cao, Marie-Julie Rakotosaona, Ben Poole, Federico Tombari, Michael Niemeyer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00916v1.pdf)  
  Keywords: ar, 3d gaussian, face  
- **[GaussianVLM: Scene-centric 3D Vision-Language Models using
  Language-aligned Gaussian Splats for Embodied Reasoning and Beyond](https://arxiv.org/abs/2507.00886v1)**  
  Authors: Anna-Maria Halacheva, Jan-Nico Zaech, Xi Wang, Danda Pani Paudel, Luc Van Gool  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00886v1.pdf)  
  Keywords: compact, understanding, ar, gaussian splatting, 3d gaussian, fast  
- **[LOD-GS: Level-of-Detail-Sensitive 3D Gaussian Splatting for Detail
  Conserved Anti-Aliasing](https://arxiv.org/abs/2507.00554v1)**  
  Authors: Zhenya Yang, Bingchen Gong, Kai Chen, Qi Dou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00554v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, ar  

### Avatar Generation

*Showing the latest 50 out of 331 papers*

- **[HyperGaussians: High-Dimensional Gaussian Splatting for High-Fidelity
  Animatable Face Avatars](https://arxiv.org/abs/2507.02803v1)**  
  Authors: Gent Serifi, Marcel C. Bühler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02803v1.pdf)  
  Keywords: reflection, lighting, high-fidelity, gaussian splatting, avatar, ar, 3d gaussian, face, deformation, fast  
- **[Masks make discriminative models great again!](https://arxiv.org/abs/2507.00916v1)**  
  Authors: Tianshi Cao, Marie-Julie Rakotosaona, Ben Poole, Federico Tombari, Michael Niemeyer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00916v1.pdf)  
  Keywords: ar, 3d gaussian, face  
- **[GDGS: 3D Gaussian Splatting Via Geometry-Guided Initialization And
  Dynamic Density Control](https://arxiv.org/abs/2507.00363v1)**  
  Authors: Xingjun Wang, Lianlei Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00363v1.pdf)  
  Keywords: dynamic, ar, high-fidelity, gaussian splatting, geometry, 3d gaussian, face, real-time rendering, fast  
- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: efficient, ar, geometry, gaussian splatting, 3d gaussian, face, animation, fast  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: efficient rendering, nerf, efficient, 3d reconstruction, motion, ar, gaussian splatting, 3d gaussian, face  
- **[Confident Splatting: Confidence-Based Compression of 3D Gaussian
  Splatting via Learnable Beta Distributions](https://arxiv.org/abs/2506.22973v1)**  
  Authors: AmirHossein Naghi Razlighi, Elaheh Badali Golezani, Shohreh Kasaei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22973v1.pdf)  
  Keywords: head, compression, ar, gaussian splatting, 3d gaussian, real-time rendering  
- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: efficient, mapping, dynamic, motion, 3d reconstruction, slam, ar, gaussian splatting, 3d gaussian, face, localization  
- **[CL-Splats: Continual Learning of Gaussian Splatting with Local
  Optimization](https://arxiv.org/abs/2506.21117v1)**  
  Authors: Jan Ackermann, Jonas Kulhanek, Shengqu Cai, Haofei Xu, Marc Pollefeys, Gordon Wetzstein, Leonidas Guibas, Songyou Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21117v1.pdf)  
  Keywords: head, robotics, efficient, dynamic, ar, gaussian splatting, segmentation  
- **[3DGH: 3D Head Generation with Composable Hair and Face](https://arxiv.org/abs/2506.20875v1)**  
  Authors: Chengan He, Junxuan Li, Tobias Kirschstein, Artem Sevastopolsky, Shunsuke Saito, Qingyang Tan, Javier Romero, Chen Cao, Holly Rushmeier, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20875v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://c-he.github.io/projects/3dgh/.)  
  Keywords: head, human, ar, geometry, gaussian splatting, 3d gaussian, face  
- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: body, understanding, dynamic, motion, ar, gaussian splatting, deformation  

### Dynamic Scene

*Showing the latest 50 out of 395 papers*

- **[HyperGaussians: High-Dimensional Gaussian Splatting for High-Fidelity
  Animatable Face Avatars](https://arxiv.org/abs/2507.02803v1)**  
  Authors: Gent Serifi, Marcel C. Bühler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02803v1.pdf)  
  Keywords: reflection, lighting, high-fidelity, gaussian splatting, avatar, ar, 3d gaussian, face, deformation, fast  
- **[ArtGS:3D Gaussian Splatting for Interactive Visual-Physical Modeling and
  Manipulation of Articulated Objects](https://arxiv.org/abs/2507.02600v1)**  
  Authors: Qiaojun Yu, Xibin Yuan, Yu jiang, Junting Chen, Dongzhe Zheng, Ce Hao, Yang You, Yixing Chen, Yao Mu, Liu Liu, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02600v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sites.google.com/view/artgs/home)  
  Keywords: robotics, efficient, semantic, understanding, dynamic, motion, ar, gaussian splatting, 3d gaussian  
- **[LocalDyGS: Multi-view Global Dynamic Scene Modeling via Adaptive Local
  Implicit Feature Decoupling](https://arxiv.org/abs/2507.02363v1)**  
  Authors: Jiahao Wu, Rui Peng, Jianbo Jiao, Jiayu Yang, Luyang Tang, Kaiqiang Xiong, Jie Liang, Jinbo Yan, Runling Liu, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02363v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wujh2001.github.io/LocalDyGS/.)  
  Keywords: dynamic, motion, ar, gaussian splatting, 3d gaussian  
- **[A LoD of Gaussians: Unified Training and Rendering for Ultra-Large Scale
  Reconstruction with External Memory](https://arxiv.org/abs/2507.01110v1)**  
  Authors: Felix Windisch, Lukas Radl, Thomas Köhler, Michael Steiner, Dieter Schmalstieg, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01110v1.pdf)  
  Keywords: efficient, dynamic, lightweight, ar, vr, gaussian splatting, real-time rendering  
- **[LOD-GS: Level-of-Detail-Sensitive 3D Gaussian Splatting for Detail
  Conserved Anti-Aliasing](https://arxiv.org/abs/2507.00554v1)**  
  Authors: Zhenya Yang, Bingchen Gong, Kai Chen, Qi Dou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00554v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, ar  
- **[GDGS: 3D Gaussian Splatting Via Geometry-Guided Initialization And
  Dynamic Density Control](https://arxiv.org/abs/2507.00363v1)**  
  Authors: Xingjun Wang, Lianlei Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00363v1.pdf)  
  Keywords: dynamic, ar, high-fidelity, gaussian splatting, geometry, 3d gaussian, face, real-time rendering, fast  
- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: efficient, ar, geometry, gaussian splatting, 3d gaussian, face, animation, fast  
- **[GaVS: 3D-Grounded Video Stabilization via Temporally-Consistent Local
  Reconstruction and Rendering](https://arxiv.org/abs/2506.23957v1)**  
  Authors: Zinuo You, Stamatios Georgoulis, Anpei Chen, Siyu Tang, Dengxin Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23957v1.pdf)  
  Keywords: dynamic, motion, ar, geometry, gaussian splatting  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: efficient rendering, nerf, efficient, 3d reconstruction, motion, ar, gaussian splatting, 3d gaussian, face  
- **[Instant GaussianImage: A Generalizable and Self-Adaptive Image
  Representation via 2D Gaussian Splatting](https://arxiv.org/abs/2506.23479v1)**  
  Authors: Zhaojie Zeng, Yuesong Wang, Chao Yang, Tao Guan, Lili Ju  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23479v1.pdf)  
  Keywords: gaussian splatting, dynamic, ar  

### Few-shot

*Showing the latest 50 out of 72 papers*

- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from
  RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: dynamic, motion, ar, gaussian splatting, sparse-view  
- **[PointGS: Point Attention-Aware Sparse View Synthesis with Gaussian
  Splatting](https://arxiv.org/abs/2506.10335v1)**  
  Authors: Lintao Xiang, Hongpei Zheng, Yating Huang, Qijun Yang, Hujun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.10335v1.pdf)  
  Keywords: sparse view, few-shot, nerf, lightweight, ar, gaussian splatting, 3d gaussian  
- **[UniForward: Unified 3D Scene and Semantic Field Reconstruction via
  Feed-Forward Gaussian Splatting from Only Sparse-View Images](https://arxiv.org/abs/2506.09378v1)**  
  Authors: Qijian Tian, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09378v1.pdf)  
  Keywords: semantic, understanding, ar, gaussian splatting, segmentation, 3d gaussian, sparse-view  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline
  Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: sparse view, ar, high-fidelity, gaussian splatting, 3d gaussian  
- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade
  Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: nerf, efficient, ar, geometry, gaussian splatting, 3d gaussian, sparse-view  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, face, sparse-view  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian
  Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: motion, 3d reconstruction, ar, gaussian splatting, face, sparse-view, fast  
- **[Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse
  Views by Jointly Training Hemisphere Sampled Synthetic Images](https://arxiv.org/abs/2505.19264v1)**  
  Authors: Guangan Chen, Anh Minh Truong, Hanhe Lin, Michiel Vlaminck, Wilfried Philips, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19264v1.pdf)  
  Keywords: sparse view, motion, ar, gaussian splatting, 3d gaussian, sparse-view  
- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane
  Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: head, compact, efficient, dynamic, 4d, 3d reconstruction, motion, ar, gaussian splatting, sparse-view, deformation  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater
  Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: robotics, ar, high-fidelity, gaussian splatting, 3d gaussian, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 315 papers*

- **[Gbake: Baking 3D Gaussian Splats into Reflection Probes](https://arxiv.org/abs/2507.02257v1)**  
  Authors: Stephen Pasch, Joel K. Salzman, Changxi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02257v1.pdf)  
  Keywords: reflection, mapping, lighting, geometry, gaussian splatting, ar, 3d gaussian  
- **[GDGS: 3D Gaussian Splatting Via Geometry-Guided Initialization And
  Dynamic Density Control](https://arxiv.org/abs/2507.00363v1)**  
  Authors: Xingjun Wang, Lianlei Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00363v1.pdf)  
  Keywords: dynamic, ar, high-fidelity, gaussian splatting, geometry, 3d gaussian, face, real-time rendering, fast  
- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: efficient, ar, geometry, gaussian splatting, 3d gaussian, face, animation, fast  
- **[GaVS: 3D-Grounded Video Stabilization via Temporally-Consistent Local
  Reconstruction and Rendering](https://arxiv.org/abs/2506.23957v1)**  
  Authors: Zinuo You, Stamatios Georgoulis, Anpei Chen, Siyu Tang, Dengxin Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23957v1.pdf)  
  Keywords: dynamic, motion, ar, geometry, gaussian splatting  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: efficient rendering, nerf, efficient, 3d reconstruction, motion, ar, gaussian splatting, 3d gaussian, face  
- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: semantic, understanding, 3d reconstruction, lighting, ar, gaussian splatting, segmentation, tracking, deformation  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: outdoor, illumination, mapping, dynamic, slam, lighting, high-fidelity, gaussian splatting, geometry, tracking, ar, 3d gaussian  
- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: efficient, mapping, dynamic, motion, 3d reconstruction, slam, ar, gaussian splatting, 3d gaussian, face, localization  
- **[Geometry and Perception Guided Gaussians for Multiview-consistent 3D
  Generation from a Single Image](https://arxiv.org/abs/2506.21152v1)**  
  Authors: Pufan Li, Bi'an Du, Wei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21152v1.pdf)  
  Keywords: 3d reconstruction, ar, geometry, gaussian splatting, 3d gaussian, fast  
- **[DBMovi-GS: Dynamic View Synthesis from Blurry Monocular Video via
  Sparse-Controlled Gaussian Splatting](https://arxiv.org/abs/2506.20998v1)**  
  Authors: Yeon-Ji Song, Jaein Kim, Byung-Ju Kim, Byoung-Tak Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20998v1.pdf)  
  Keywords: dynamic, motion, ar, geometry, gaussian splatting, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 61 papers*

- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: outdoor, illumination, mapping, dynamic, slam, lighting, high-fidelity, gaussian splatting, geometry, tracking, ar, 3d gaussian  
- **[BézierGS: Dynamic Urban Scene Reconstruction with Bézier Curve
  Gaussian Splatting](https://arxiv.org/abs/2506.22099v2)**  
  Authors: Zipei Ma, Junzhe Jiang, Yurui Chen, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22099v2.pdf)  
  Keywords: urban scene, dynamic, motion, ar, gaussian splatting, autonomous driving  
- **[ICP-3DGS: SfM-free 3D Gaussian Splatting for Large-scale Unbounded
  Scenes](https://arxiv.org/abs/2506.21629v1)**  
  Authors: Chenhao Zhang, Yezhi Shen, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21629v1.pdf)  
  Keywords: outdoor, nerf, motion, ar, neural rendering, gaussian splatting, 3d gaussian  
- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: outdoor, slam, ar, gaussian splatting, tracking, 3d gaussian  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: outdoor, nerf, efficient, dynamic, ar, high-fidelity, gaussian splatting, 3d gaussian, face, autonomous driving, survey  
- **[Multiview Geometric Regularization of Gaussian Splatting for Accurate
  Radiance Fields](https://arxiv.org/abs/2506.13508v1)**  
  Authors: Jungeon Kim, Geonsoo Park, Seungyong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13508v1.pdf)  
  Keywords: outdoor, ar, geometry, gaussian splatting, 3d gaussian  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language
  Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: outdoor, efficient, semantic, understanding, ar, geometry, gaussian splatting, segmentation, 3d gaussian, fast  
- **[TraGraph-GS: Trajectory Graph-based Gaussian Splatting for Arbitrary
  Large-Scale Scene Rendering](https://arxiv.org/abs/2506.08704v1)**  
  Authors: Xiaohan Zhang, Sitong Wang, Yushen Yan, Yi Yang, Mingda Xu, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08704v1.pdf)  
  Keywords: gaussian splatting, large scene, ar  
- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from
  Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: efficient, motion, slam, ar, gaussian splatting, 3d gaussian, large scene, fast  
- **[Photoreal Scene Reconstruction from an Egocentric Device](https://arxiv.org/abs/2506.04444v1)**  
  Authors: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04444v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.projectaria.com/photoreal-reconstruction/)  
  Keywords: outdoor, dynamic, ar, lighting, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 392 papers*

- **[ArtGS:3D Gaussian Splatting for Interactive Visual-Physical Modeling and
  Manipulation of Articulated Objects](https://arxiv.org/abs/2507.02600v1)**  
  Authors: Qiaojun Yu, Xibin Yuan, Yu jiang, Junting Chen, Dongzhe Zheng, Ce Hao, Yang You, Yixing Chen, Yao Mu, Liu Liu, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02600v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sites.google.com/view/artgs/home)  
  Keywords: robotics, efficient, semantic, understanding, dynamic, motion, ar, gaussian splatting, 3d gaussian  
- **[VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online
  Semantic Gaussian Splatting](https://arxiv.org/abs/2507.01125v1)**  
  Authors: Keiko Nagami, Timothy Chen, Javier Yu, Ola Shorinwa, Maximilian Adang, Carlyn Dougherty, Eric Cristofalo, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01125v1.pdf)  
  Keywords: efficient, semantic, ar, gaussian splatting, 3d gaussian  
- **[A LoD of Gaussians: Unified Training and Rendering for Ultra-Large Scale
  Reconstruction with External Memory](https://arxiv.org/abs/2507.01110v1)**  
  Authors: Felix Windisch, Lukas Radl, Thomas Köhler, Michael Steiner, Dieter Schmalstieg, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01110v1.pdf)  
  Keywords: efficient, dynamic, lightweight, ar, vr, gaussian splatting, real-time rendering  
- **[GaussianVLM: Scene-centric 3D Vision-Language Models using
  Language-aligned Gaussian Splats for Embodied Reasoning and Beyond](https://arxiv.org/abs/2507.00886v1)**  
  Authors: Anna-Maria Halacheva, Jan-Nico Zaech, Xi Wang, Danda Pani Paudel, Luc Van Gool  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00886v1.pdf)  
  Keywords: compact, understanding, ar, gaussian splatting, 3d gaussian, fast  
- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: efficient, ar, geometry, gaussian splatting, 3d gaussian, face, animation, fast  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: efficient rendering, nerf, efficient, 3d reconstruction, motion, ar, gaussian splatting, 3d gaussian, face  
- **[From Coarse to Fine: Learnable Discrete Wavelet Transforms for Efficient
  3D Gaussian Splatting](https://arxiv.org/abs/2506.23042v1)**  
  Authors: Hung Nguyen, An Le, Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23042v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, efficient  
- **[Confident Splatting: Confidence-Based Compression of 3D Gaussian
  Splatting via Learnable Beta Distributions](https://arxiv.org/abs/2506.22973v1)**  
  Authors: AmirHossein Naghi Razlighi, Elaheh Badali Golezani, Shohreh Kasaei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22973v1.pdf)  
  Keywords: head, compression, ar, gaussian splatting, 3d gaussian, real-time rendering  
- **[DIGS: Dynamic CBCT Reconstruction using Deformation-Informed 4D Gaussian
  Splatting and a Low-Rank Free-Form Deformation Model](https://arxiv.org/abs/2506.22280v1)**  
  Authors: Yuliang Huang, Imraj Singh, Thomas Joyce, Kris Thielemans, Jamie R. McClelland  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22280v1.pdf)  
  Keywords: efficient, dynamic, 4d, motion, ar, gaussian splatting, deformation  
- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: efficient, mapping, dynamic, motion, 3d reconstruction, slam, ar, gaussian splatting, 3d gaussian, face, localization  

### Quality Enhancement

*Showing the latest 50 out of 159 papers*

- **[HyperGaussians: High-Dimensional Gaussian Splatting for High-Fidelity
  Animatable Face Avatars](https://arxiv.org/abs/2507.02803v1)**  
  Authors: Gent Serifi, Marcel C. Bühler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02803v1.pdf)  
  Keywords: reflection, lighting, high-fidelity, gaussian splatting, avatar, ar, 3d gaussian, face, deformation, fast  
- **[GDGS: 3D Gaussian Splatting Via Geometry-Guided Initialization And
  Dynamic Density Control](https://arxiv.org/abs/2507.00363v1)**  
  Authors: Xingjun Wang, Lianlei Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00363v1.pdf)  
  Keywords: dynamic, ar, high-fidelity, gaussian splatting, geometry, 3d gaussian, face, real-time rendering, fast  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: outdoor, illumination, mapping, dynamic, slam, lighting, high-fidelity, gaussian splatting, geometry, tracking, ar, 3d gaussian  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: ray tracing, efficient, ar, high-fidelity, gaussian splatting, real-time rendering  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: outdoor, nerf, efficient, dynamic, ar, high-fidelity, gaussian splatting, 3d gaussian, face, autonomous driving, survey  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: robotics, nerf, 3d reconstruction, ar, neural rendering, gaussian splatting, high-fidelity, vr, 3d gaussian, autonomous driving, survey  
- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads
  Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: head, efficient, dynamic, ar, high-fidelity, gaussian splatting, face  
- **[PF-LHM: 3D Animatable Avatar Reconstruction from Pose-free Articulated
  Human Images](https://arxiv.org/abs/2506.13766v1)**  
  Authors: Lingteng Qiu, Peihao Li, Qi Zuo, Xiaodong Gu, Yuan Dong, Weihao Yuan, Siyu Zhu, Xiaoguang Han, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13766v1.pdf)  
  Keywords: efficient, human, avatar, geometry, high-fidelity, ar, 3d gaussian  
- **[GaussianVAE: Adaptive Learning Dynamics of 3D Gaussians for
  High-Fidelity Super-Resolution](https://arxiv.org/abs/2506.07897v1)**  
  Authors: Shuja Khalid, Mohamed Ibrahim, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07897v1.pdf)  
  Keywords: dynamic, lightweight, ar, high-fidelity, gaussian splatting, 3d gaussian  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline
  Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: sparse view, ar, high-fidelity, gaussian splatting, 3d gaussian  

### Ray Tracing

- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: ray tracing, efficient, ar, high-fidelity, gaussian splatting, real-time rendering  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: ray tracing, relighting, human, shadow, lighting, geometry, gaussian splatting, avatar, relightable, ar, fast  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: efficient rendering, ray tracing, relighting, efficient, lighting, ar, gaussian splatting, 3d gaussian, acceleration  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: ray marching, compact, efficient, dynamic, ar, gaussian splatting, 3d gaussian, animation, acceleration  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: ray tracing, efficient, illumination, lighting, ar, gaussian splatting, real-time rendering, 3d gaussian, face, global illumination  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: ray tracing, reflection, shadow, ar, neural rendering, gaussian splatting, 3d gaussian, fast  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: ray tracing, reflection, shadow, lighting, gaussian splatting, face  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation
  Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, ar, gaussian splatting, 3d gaussian, survey  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: ray tracing, light transport, reflection, efficient, ar, gaussian splatting, acceleration  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: ray tracing, reflection, shadow, ar, gaussian splatting, 3d gaussian  

### Relighting

*Showing the latest 50 out of 107 papers*

- **[HyperGaussians: High-Dimensional Gaussian Splatting for High-Fidelity
  Animatable Face Avatars](https://arxiv.org/abs/2507.02803v1)**  
  Authors: Gent Serifi, Marcel C. Bühler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02803v1.pdf)  
  Keywords: reflection, lighting, high-fidelity, gaussian splatting, avatar, ar, 3d gaussian, face, deformation, fast  
- **[Gbake: Baking 3D Gaussian Splats into Reflection Probes](https://arxiv.org/abs/2507.02257v1)**  
  Authors: Stephen Pasch, Joel K. Salzman, Changxi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02257v1.pdf)  
  Keywords: reflection, mapping, lighting, geometry, gaussian splatting, ar, 3d gaussian  
- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: semantic, understanding, 3d reconstruction, lighting, ar, gaussian splatting, segmentation, tracking, deformation  
- **[Endo-4DGX: Robust Endoscopic Scene Reconstruction and Illumination
  Correction with Gaussian Splatting](https://arxiv.org/abs/2506.23308v1)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Yanheng Li, Tong Chen, Jie Wang, Jinlin Wu, Zhen Lei, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23308v1.pdf)  
  Keywords: illumination, dynamic, 4d, lighting, ar, gaussian splatting, 3d gaussian  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: outdoor, illumination, mapping, dynamic, slam, lighting, high-fidelity, gaussian splatting, geometry, tracking, ar, 3d gaussian  
- **[MADrive: Memory-Augmented Driving Scene Modeling](https://arxiv.org/abs/2506.21520v1)**  
  Authors: Polina Karpikova, Daniil Selikhanovych, Kirill Struminsky, Ruslan Musaev, Maria Golitsyna, Dmitry Baranchuk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21520v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yandex-research.github.io/madrive/)  
  Keywords: relighting, lighting, ar, gaussian splatting, 3d gaussian, autonomous driving  
- **[Micro-macro Gaussian Splatting with Enhanced Scalability for
  Unconstrained Scene Reconstruction](https://arxiv.org/abs/2506.13516v1)**  
  Authors: Yihui Li, Chengxin Lv, Hongyu Yang, Di Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13516v1.pdf)  
  Keywords: illumination, 3d reconstruction, motion, ar, gaussian splatting  
- **[GS-2DGS: Geometrically Supervised 2DGS for Reflective Object
  Reconstruction](https://arxiv.org/abs/2506.13110v1)**  
  Authors: Jinguang Tong, Xuesong li, Fahira Afzal Maken, Sundaram Muthu, Lars Petersson, Chuong Nguyen, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13110v1.pdf)  
  Keywords: relighting, lighting, ar, gaussian splatting, 3d gaussian, face, real-time rendering, fast  
- **[Efficient multi-view training for 3D Gaussian Splatting](https://arxiv.org/abs/2506.12727v2)**  
  Authors: Minhyuk Choi, Injae Kim, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12727v2.pdf)  
  Keywords: head, nerf, efficient, lighting, ar, gaussian splatting, 3d gaussian  
- **[R3D2: Realistic 3D Asset Insertion via Diffusion for Autonomous Driving
  Simulation](https://arxiv.org/abs/2506.07826v1)**  
  Authors: William Ljungbergh, Bernardo Taveira, Wenzhao Zheng, Adam Tonderski, Chensheng Peng, Fredrik Kahl, Christoffer Petersson, Michael Felsberg, Kurt Keutzer, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07826v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/R3D2/.)  
  Keywords: illumination, shadow, dynamic, lightweight, lighting, neural rendering, gaussian splatting, ar, 3d gaussian, autonomous driving  

### SLAM

*Showing the latest 50 out of 156 papers*

- **[Gbake: Baking 3D Gaussian Splats into Reflection Probes](https://arxiv.org/abs/2507.02257v1)**  
  Authors: Stephen Pasch, Joel K. Salzman, Changxi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02257v1.pdf)  
  Keywords: reflection, mapping, lighting, geometry, gaussian splatting, ar, 3d gaussian  
- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: semantic, understanding, 3d reconstruction, lighting, ar, gaussian splatting, segmentation, tracking, deformation  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: outdoor, illumination, mapping, dynamic, slam, lighting, high-fidelity, gaussian splatting, geometry, tracking, ar, 3d gaussian  
- **[VoteSplat: Hough Voting Gaussian Splatting for 3D Scene Understanding](https://arxiv.org/abs/2506.22799v1)**  
  Authors: Minchao Jiang, Shunyu Jia, Jiaming Gu, Xiaoyuan Lu, Guangming Zhu, Anqi Dong, Liang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sy-ja.github.io/votesplat/)  
  Keywords: semantic, understanding, ar, gaussian splatting, segmentation, 3d gaussian, localization, real-time rendering  
- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: efficient, mapping, dynamic, motion, 3d reconstruction, slam, ar, gaussian splatting, 3d gaussian, face, localization  
- **[SAR-GS: 3D Gaussian Splatting for Synthetic Aperture Radar Target
  Reconstruction](https://arxiv.org/abs/2506.21633v1)**  
  Authors: Aobo Li, Zhengxin Lei, Jiangtao Wei, Feng Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21633v1.pdf)  
  Keywords: mapping, 3d reconstruction, ar, gaussian splatting, 3d gaussian  
- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: outdoor, slam, ar, gaussian splatting, tracking, 3d gaussian  
- **[RA-NeRF: Robust Neural Radiance Field Reconstruction with Accurate
  Camera Pose Estimation under Complex Trajectories](https://arxiv.org/abs/2506.15242v2)**  
  Authors: Qingsong Yan, Qiang Wang, Kaiyong Zhao, Jie Chen, Bo Li, Xiaowen Chu, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15242v2.pdf)  
  Keywords: nerf, 3d reconstruction, slam, ar, gaussian splatting, 3d gaussian, localization  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty
  Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: head, nerf, efficient, mapping, 3d reconstruction, lightweight, ar, neural rendering, gaussian splatting, 3d gaussian  
- **[TextureSplat: Per-Primitive Texture Mapping for Reflective Gaussian
  Splatting](https://arxiv.org/abs/2506.13348v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13348v1.pdf)  
  Keywords: gaussian splatting, ar, mapping, face  

### Scene Understanding

*Showing the latest 50 out of 184 papers*

- **[ArtGS:3D Gaussian Splatting for Interactive Visual-Physical Modeling and
  Manipulation of Articulated Objects](https://arxiv.org/abs/2507.02600v1)**  
  Authors: Qiaojun Yu, Xibin Yuan, Yu jiang, Junting Chen, Dongzhe Zheng, Ce Hao, Yang You, Yixing Chen, Yao Mu, Liu Liu, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.02600v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sites.google.com/view/artgs/home)  
  Keywords: robotics, efficient, semantic, understanding, dynamic, motion, ar, gaussian splatting, 3d gaussian  
- **[VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online
  Semantic Gaussian Splatting](https://arxiv.org/abs/2507.01125v1)**  
  Authors: Keiko Nagami, Timothy Chen, Javier Yu, Ola Shorinwa, Maximilian Adang, Carlyn Dougherty, Eric Cristofalo, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01125v1.pdf)  
  Keywords: efficient, semantic, ar, gaussian splatting, 3d gaussian  
- **[GaussianVLM: Scene-centric 3D Vision-Language Models using
  Language-aligned Gaussian Splats for Embodied Reasoning and Beyond](https://arxiv.org/abs/2507.00886v1)**  
  Authors: Anna-Maria Halacheva, Jan-Nico Zaech, Xi Wang, Danda Pani Paudel, Luc Van Gool  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00886v1.pdf)  
  Keywords: compact, understanding, ar, gaussian splatting, 3d gaussian, fast  
- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: semantic, understanding, 3d reconstruction, lighting, ar, gaussian splatting, segmentation, tracking, deformation  
- **[VoteSplat: Hough Voting Gaussian Splatting for 3D Scene Understanding](https://arxiv.org/abs/2506.22799v1)**  
  Authors: Minchao Jiang, Shunyu Jia, Jiaming Gu, Xiaoyuan Lu, Guangming Zhu, Anqi Dong, Liang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sy-ja.github.io/votesplat/)  
  Keywords: semantic, understanding, ar, gaussian splatting, segmentation, 3d gaussian, localization, real-time rendering  
- **[RoboPearls: Editable Video Simulation for Robot Manipulation](https://arxiv.org/abs/2506.22756v1)**  
  Authors: Tao Tang, Likui Zhang, Youpeng Wen, Kaidong Zhang, Jia-Wang Bian, xia zhou, Tianyi Yan, Kun Zhan, Peng Jia, Hefeng Wu, Liang Lin, Xiaodan Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22756v1.pdf)  
  Keywords: semantic, 4d, ar, gaussian splatting, 3d gaussian  
- **[CL-Splats: Continual Learning of Gaussian Splatting with Local
  Optimization](https://arxiv.org/abs/2506.21117v1)**  
  Authors: Jan Ackermann, Jonas Kulhanek, Shengqu Cai, Haofei Xu, Marc Pollefeys, Gordon Wetzstein, Leonidas Guibas, Songyou Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21117v1.pdf)  
  Keywords: head, robotics, efficient, dynamic, ar, gaussian splatting, segmentation  
- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: body, understanding, dynamic, motion, ar, gaussian splatting, deformation  
- **[3D Arena: An Open Platform for Generative 3D Evaluation](https://arxiv.org/abs/2506.18787v1)**  
  Authors: Dylan Ebert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18787v1.pdf)  
  Keywords: human, ar, understanding  
- **[Reconstructing Tornadoes in 3D with Gaussian Splatting](https://arxiv.org/abs/2506.18677v1)**  
  Authors: Adam Yang, Nadula Kadawedduwa, Tianfu Wang, Maria Molina, Christopher Metzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18677v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, understanding  



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

## 📋 Project Features

### 🛠️ Core Features
- **Configurable Search System**: Customize search keywords through `data/search_config.json` for targeted paper collection
- **Automated Paper Collection**: Daily automatic crawling of latest Gaussian Splatting related papers
- **Intelligent Classification System**: Automatically categorize papers into different topics (Acceleration, Applications, Dynamic Scenes, etc.)
- **Flexible Search Scopes**: Support for abstract-only, title-only, or combined searches
- **Cross-Platform Compatibility**: Support for Windows/Linux/macOS with automatic environment detection

### 🛠️ Technical Features
- **Robust Error Handling**: Multi-layer retry and fallback strategies ensure stable operation
- **GitHub Actions Integration**: Automated CI/CD workflows
- **Real-time Update Mechanism**: Daily automatic paper data updates
- **Detailed Logging**: Comprehensive logging for debugging and monitoring

### 📚 Documentation System
- **User Guides**: Detailed configuration and usage instructions
- **Update Logs**: [News.md](News.md) - Records all important updates
- **Validation Reports**: Automated testing and validation results

## 🚀 Quick Start

### Customize Search Keywords
Edit `data/search_config.json` to target specific research areas:

```json
{
  "search_config": {
    "both_abstract_and_title": [
      "gaussian splatting",
      "3d gaussian",
      "neural rendering"
    ],
    "abstract_only": [
      "volumetric rendering",
      "point cloud reconstruction"
    ],
    "title_only": [
      "real-time rendering",
      "3D reconstruction"
    ]
  }
}
```

### Run the Crawler
```bash
# Basic usage
python scripts/arxiv_crawler.py

# Custom number of papers
python scripts/arxiv_crawler.py --max-results 200

# Validate configuration
python scripts/validate_search_config.py
```

## Contribution Guidelines
Feel free to submit Pull Requests to improve this list! Please follow these formats:
- Paper entry format: `**[Paper Title](link)** - Brief description`
- Project entry format: `[Project Name](link) - Project description`

## License
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) 