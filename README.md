# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-07-04 00:55:21

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
- [Acceleration](#acceleration) (277 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (331 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (392 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (73 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (315 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (61 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (393 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (159 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (17 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (107 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (155 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (183 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: efficient, autonomous driving, high-fidelity, dynamic, 3d gaussian, ar, outdoor, nerf, face, survey, gaussian splatting  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: autonomous driving, high-fidelity, 3d gaussian, ar, 3d reconstruction, nerf, survey, vr, neural rendering, robotics, gaussian splatting  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: efficient, semantic, high-fidelity, 3d gaussian, ar, outdoor, 3d reconstruction, segmentation, survey, neural rendering, understanding, gaussian splatting  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: localization, efficient, semantic, 3d gaussian, ar, segmentation, nerf, survey, slam, mapping, gaussian splatting  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to
  Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: 4d, dynamic, motion, 3d gaussian, body, ar, survey, understanding, gaussian splatting  
- **[A Survey of 3D Reconstruction with Event Cameras](https://arxiv.org/abs/2505.08438v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v2.pdf)  
  Keywords: autonomous driving, dynamic, motion, 3d gaussian, ar, 3d reconstruction, nerf, illumination, survey, neural rendering, geometry, robotics, gaussian splatting  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: efficient, fast, ar, 3d reconstruction, survey, gaussian splatting  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: lighting, 3d gaussian, ar, 3d reconstruction, survey  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From
  Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting
  (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf)  
  Keywords: 3d gaussian, ar, outdoor, 3d reconstruction, nerf, sparse view, survey, face, geometry, understanding, gaussian splatting  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf)  
  Keywords: semantic, lighting, 3d gaussian, ar, segmentation, survey, robotics, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 277 papers*

- **[A LoD of Gaussians: Unified Training and Rendering for Ultra-Large Scale
  Reconstruction with External Memory](https://arxiv.org/abs/2507.01110v1)**  
  Authors: Felix Windisch, Lukas Radl, Thomas Köhler, Michael Steiner, Dieter Schmalstieg, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01110v1.pdf)  
  Keywords: lightweight, efficient, dynamic, ar, real-time rendering, vr, gaussian splatting  
- **[GaussianVLM: Scene-centric 3D Vision-Language Models using
  Language-aligned Gaussian Splats for Embodied Reasoning and Beyond](https://arxiv.org/abs/2507.00886v1)**  
  Authors: Anna-Maria Halacheva, Jan-Nico Zaech, Xi Wang, Danda Pani Paudel, Luc Van Gool  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00886v1.pdf)  
  Keywords: fast, 3d gaussian, compact, ar, understanding, gaussian splatting  
- **[GDGS: 3D Gaussian Splatting Via Geometry-Guided Initialization And
  Dynamic Density Control](https://arxiv.org/abs/2507.00363v1)**  
  Authors: Xingjun Wang, Lianlei Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00363v1.pdf)  
  Keywords: fast, high-fidelity, dynamic, 3d gaussian, ar, real-time rendering, face, geometry, gaussian splatting  
- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: efficient, fast, 3d gaussian, ar, face, animation, geometry, gaussian splatting  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: efficient rendering, efficient, motion, 3d gaussian, ar, 3d reconstruction, nerf, face, gaussian splatting  
- **[Confident Splatting: Confidence-Based Compression of 3D Gaussian
  Splatting via Learnable Beta Distributions](https://arxiv.org/abs/2506.22973v1)**  
  Authors: AmirHossein Naghi Razlighi, Elaheh Badali Golezani, Shohreh Kasaei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22973v1.pdf)  
  Keywords: head, 3d gaussian, ar, real-time rendering, compression, gaussian splatting  
- **[VoteSplat: Hough Voting Gaussian Splatting for 3D Scene Understanding](https://arxiv.org/abs/2506.22799v1)**  
  Authors: Minchao Jiang, Shunyu Jia, Jiaming Gu, Xiaoyuan Lu, Guangming Zhu, Anqi Dong, Liang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sy-ja.github.io/votesplat/)  
  Keywords: localization, semantic, 3d gaussian, ar, segmentation, real-time rendering, understanding, gaussian splatting  
- **[Geometry and Perception Guided Gaussians for Multiview-consistent 3D
  Generation from a Single Image](https://arxiv.org/abs/2506.21152v1)**  
  Authors: Pufan Li, Bi'an Du, Wei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21152v1.pdf)  
  Keywords: fast, 3d gaussian, ar, 3d reconstruction, geometry, gaussian splatting  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: efficient, high-fidelity, ray tracing, ar, real-time rendering, gaussian splatting  
- **[Virtual Memory for 3D Gaussian Splatting](https://arxiv.org/abs/2506.19415v1)**  
  Authors: Jonathan Haberl, Philipp Fleck, Clemens Arth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19415v1.pdf)  
  Keywords: efficient, dynamic, 3d gaussian, ar, real-time rendering, gaussian splatting  

### Applications

*Showing the latest 50 out of 995 papers*

- **[3D Gaussian Splatting Driven Multi-View Robust Physical Adversarial
  Camouflage Generation](https://arxiv.org/abs/2507.01367v1)**  
  Authors: Tianrui Lou, Xiaojun Jia, Siyuan Liang, Jiawei Liang, Ming Zhang, Yanjun Xiao, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01367v1.pdf)  
  Keywords: ar, autonomous driving, 3d gaussian, gaussian splatting  
- **[VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online
  Semantic Gaussian Splatting](https://arxiv.org/abs/2507.01125v1)**  
  Authors: Keiko Nagami, Timothy Chen, Javier Yu, Ola Shorinwa, Maximilian Adang, Carlyn Dougherty, Eric Cristofalo, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01125v1.pdf)  
  Keywords: efficient, semantic, 3d gaussian, ar, gaussian splatting  
- **[A LoD of Gaussians: Unified Training and Rendering for Ultra-Large Scale
  Reconstruction with External Memory](https://arxiv.org/abs/2507.01110v1)**  
  Authors: Felix Windisch, Lukas Radl, Thomas Köhler, Michael Steiner, Dieter Schmalstieg, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01110v1.pdf)  
  Keywords: lightweight, efficient, dynamic, ar, real-time rendering, vr, gaussian splatting  
- **[Masks make discriminative models great again!](https://arxiv.org/abs/2507.00916v1)**  
  Authors: Tianshi Cao, Marie-Julie Rakotosaona, Ben Poole, Federico Tombari, Michael Niemeyer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00916v1.pdf)  
  Keywords: face, 3d gaussian, ar  
- **[GaussianVLM: Scene-centric 3D Vision-Language Models using
  Language-aligned Gaussian Splats for Embodied Reasoning and Beyond](https://arxiv.org/abs/2507.00886v1)**  
  Authors: Anna-Maria Halacheva, Jan-Nico Zaech, Xi Wang, Danda Pani Paudel, Luc Van Gool  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00886v1.pdf)  
  Keywords: fast, 3d gaussian, compact, ar, understanding, gaussian splatting  
- **[LOD-GS: Level-of-Detail-Sensitive 3D Gaussian Splatting for Detail
  Conserved Anti-Aliasing](https://arxiv.org/abs/2507.00554v1)**  
  Authors: Zhenya Yang, Bingchen Gong, Kai Chen, Qi Dou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00554v1.pdf)  
  Keywords: ar, dynamic, 3d gaussian, gaussian splatting  
- **[GDGS: 3D Gaussian Splatting Via Geometry-Guided Initialization And
  Dynamic Density Control](https://arxiv.org/abs/2507.00363v1)**  
  Authors: Xingjun Wang, Lianlei Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00363v1.pdf)  
  Keywords: fast, high-fidelity, dynamic, 3d gaussian, ar, real-time rendering, face, geometry, gaussian splatting  
- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: efficient, fast, 3d gaussian, ar, face, animation, geometry, gaussian splatting  
- **[GaVS: 3D-Grounded Video Stabilization via Temporally-Consistent Local
  Reconstruction and Rendering](https://arxiv.org/abs/2506.23957v1)**  
  Authors: Zinuo You, Stamatios Georgoulis, Anpei Chen, Siyu Tang, Dengxin Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23957v1.pdf)  
  Keywords: dynamic, motion, ar, geometry, gaussian splatting  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: efficient rendering, efficient, motion, 3d gaussian, ar, 3d reconstruction, nerf, face, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 331 papers*

- **[Masks make discriminative models great again!](https://arxiv.org/abs/2507.00916v1)**  
  Authors: Tianshi Cao, Marie-Julie Rakotosaona, Ben Poole, Federico Tombari, Michael Niemeyer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00916v1.pdf)  
  Keywords: face, 3d gaussian, ar  
- **[GDGS: 3D Gaussian Splatting Via Geometry-Guided Initialization And
  Dynamic Density Control](https://arxiv.org/abs/2507.00363v1)**  
  Authors: Xingjun Wang, Lianlei Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00363v1.pdf)  
  Keywords: fast, high-fidelity, dynamic, 3d gaussian, ar, real-time rendering, face, geometry, gaussian splatting  
- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: efficient, fast, 3d gaussian, ar, face, animation, geometry, gaussian splatting  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: efficient rendering, efficient, motion, 3d gaussian, ar, 3d reconstruction, nerf, face, gaussian splatting  
- **[Confident Splatting: Confidence-Based Compression of 3D Gaussian
  Splatting via Learnable Beta Distributions](https://arxiv.org/abs/2506.22973v1)**  
  Authors: AmirHossein Naghi Razlighi, Elaheh Badali Golezani, Shohreh Kasaei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22973v1.pdf)  
  Keywords: head, 3d gaussian, ar, real-time rendering, compression, gaussian splatting  
- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, efficient, dynamic, motion, 3d gaussian, ar, 3d reconstruction, face, slam, mapping, gaussian splatting  
- **[CL-Splats: Continual Learning of Gaussian Splatting with Local
  Optimization](https://arxiv.org/abs/2506.21117v1)**  
  Authors: Jan Ackermann, Jonas Kulhanek, Shengqu Cai, Haofei Xu, Marc Pollefeys, Gordon Wetzstein, Leonidas Guibas, Songyou Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21117v1.pdf)  
  Keywords: head, efficient, dynamic, ar, segmentation, robotics, gaussian splatting  
- **[3DGH: 3D Head Generation with Composable Hair and Face](https://arxiv.org/abs/2506.20875v1)**  
  Authors: Chengan He, Junxuan Li, Tobias Kirschstein, Artem Sevastopolsky, Shunsuke Saito, Qingyang Tan, Javier Romero, Chen Cao, Holly Rushmeier, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20875v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://c-he.github.io/projects/3dgh/.)  
  Keywords: head, 3d gaussian, ar, human, face, geometry, gaussian splatting  
- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: dynamic, motion, body, ar, deformation, understanding, gaussian splatting  
- **[HoliGS: Holistic Gaussian Splatting for Embodied View Synthesis](https://arxiv.org/abs/2506.19291v1)**  
  Authors: Xiaoyuan Wang, Yizhou Zhao, Botao Ye, Xiaojun Shan, Weijie Lyu, Lu Qi, Kelvin C. K. Chan, Yinxiao Li, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19291v1.pdf)  
  Keywords: head, 4d, dynamic, ar, nerf, deformation, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 392 papers*

- **[A LoD of Gaussians: Unified Training and Rendering for Ultra-Large Scale
  Reconstruction with External Memory](https://arxiv.org/abs/2507.01110v1)**  
  Authors: Felix Windisch, Lukas Radl, Thomas Köhler, Michael Steiner, Dieter Schmalstieg, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01110v1.pdf)  
  Keywords: lightweight, efficient, dynamic, ar, real-time rendering, vr, gaussian splatting  
- **[LOD-GS: Level-of-Detail-Sensitive 3D Gaussian Splatting for Detail
  Conserved Anti-Aliasing](https://arxiv.org/abs/2507.00554v1)**  
  Authors: Zhenya Yang, Bingchen Gong, Kai Chen, Qi Dou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00554v1.pdf)  
  Keywords: ar, dynamic, 3d gaussian, gaussian splatting  
- **[GDGS: 3D Gaussian Splatting Via Geometry-Guided Initialization And
  Dynamic Density Control](https://arxiv.org/abs/2507.00363v1)**  
  Authors: Xingjun Wang, Lianlei Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00363v1.pdf)  
  Keywords: fast, high-fidelity, dynamic, 3d gaussian, ar, real-time rendering, face, geometry, gaussian splatting  
- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: efficient, fast, 3d gaussian, ar, face, animation, geometry, gaussian splatting  
- **[GaVS: 3D-Grounded Video Stabilization via Temporally-Consistent Local
  Reconstruction and Rendering](https://arxiv.org/abs/2506.23957v1)**  
  Authors: Zinuo You, Stamatios Georgoulis, Anpei Chen, Siyu Tang, Dengxin Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23957v1.pdf)  
  Keywords: dynamic, motion, ar, geometry, gaussian splatting  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: efficient rendering, efficient, motion, 3d gaussian, ar, 3d reconstruction, nerf, face, gaussian splatting  
- **[Instant GaussianImage: A Generalizable and Self-Adaptive Image
  Representation via 2D Gaussian Splatting](https://arxiv.org/abs/2506.23479v1)**  
  Authors: Zhaojie Zeng, Yuesong Wang, Chao Yang, Tao Guan, Lili Ju  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23479v1.pdf)  
  Keywords: dynamic, ar, gaussian splatting  
- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: semantic, lighting, tracking, ar, segmentation, 3d reconstruction, deformation, understanding, gaussian splatting  
- **[Endo-4DGX: Robust Endoscopic Scene Reconstruction and Illumination
  Correction with Gaussian Splatting](https://arxiv.org/abs/2506.23308v1)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Yanheng Li, Tong Chen, Jie Wang, Jinlin Wu, Zhen Lei, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23308v1.pdf)  
  Keywords: 4d, lighting, dynamic, 3d gaussian, ar, illumination, gaussian splatting  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: tracking, high-fidelity, lighting, dynamic, 3d gaussian, ar, outdoor, illumination, geometry, slam, mapping, gaussian splatting  

### Few-shot

*Showing the latest 50 out of 73 papers*

- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from
  RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: sparse-view, dynamic, motion, ar, gaussian splatting  
- **[PointGS: Point Attention-Aware Sparse View Synthesis with Gaussian
  Splatting](https://arxiv.org/abs/2506.10335v1)**  
  Authors: Lintao Xiang, Hongpei Zheng, Yating Huang, Qijun Yang, Hujun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.10335v1.pdf)  
  Keywords: few-shot, lightweight, 3d gaussian, ar, nerf, sparse view, gaussian splatting  
- **[UniForward: Unified 3D Scene and Semantic Field Reconstruction via
  Feed-Forward Gaussian Splatting from Only Sparse-View Images](https://arxiv.org/abs/2506.09378v1)**  
  Authors: Qijian Tian, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09378v1.pdf)  
  Keywords: sparse-view, semantic, 3d gaussian, ar, segmentation, understanding, gaussian splatting  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline
  Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, ar, sparse view, gaussian splatting  
- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade
  Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: efficient, sparse-view, 3d gaussian, ar, nerf, geometry, gaussian splatting  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: sparse-view, motion, 3d gaussian, ar, face, gaussian splatting  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian
  Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: fast, sparse-view, motion, ar, 3d reconstruction, face, gaussian splatting  
- **[Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse
  Views by Jointly Training Hemisphere Sampled Synthetic Images](https://arxiv.org/abs/2505.19264v1)**  
  Authors: Guangan Chen, Anh Minh Truong, Hanhe Lin, Michiel Vlaminck, Wilfried Philips, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19264v1.pdf)  
  Keywords: sparse-view, motion, 3d gaussian, ar, sparse view, gaussian splatting  
- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane
  Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: head, 4d, efficient, sparse-view, dynamic, motion, compact, ar, 3d reconstruction, deformation, gaussian splatting  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater
  Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: sparse-view, high-fidelity, 3d gaussian, ar, robotics, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 315 papers*

- **[GDGS: 3D Gaussian Splatting Via Geometry-Guided Initialization And
  Dynamic Density Control](https://arxiv.org/abs/2507.00363v1)**  
  Authors: Xingjun Wang, Lianlei Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00363v1.pdf)  
  Keywords: fast, high-fidelity, dynamic, 3d gaussian, ar, real-time rendering, face, geometry, gaussian splatting  
- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: efficient, fast, 3d gaussian, ar, face, animation, geometry, gaussian splatting  
- **[GaVS: 3D-Grounded Video Stabilization via Temporally-Consistent Local
  Reconstruction and Rendering](https://arxiv.org/abs/2506.23957v1)**  
  Authors: Zinuo You, Stamatios Georgoulis, Anpei Chen, Siyu Tang, Dengxin Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23957v1.pdf)  
  Keywords: dynamic, motion, ar, geometry, gaussian splatting  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: efficient rendering, efficient, motion, 3d gaussian, ar, 3d reconstruction, nerf, face, gaussian splatting  
- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: semantic, lighting, tracking, ar, segmentation, 3d reconstruction, deformation, understanding, gaussian splatting  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: tracking, high-fidelity, lighting, dynamic, 3d gaussian, ar, outdoor, illumination, geometry, slam, mapping, gaussian splatting  
- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, efficient, dynamic, motion, 3d gaussian, ar, 3d reconstruction, face, slam, mapping, gaussian splatting  
- **[Geometry and Perception Guided Gaussians for Multiview-consistent 3D
  Generation from a Single Image](https://arxiv.org/abs/2506.21152v1)**  
  Authors: Pufan Li, Bi'an Du, Wei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21152v1.pdf)  
  Keywords: fast, 3d gaussian, ar, 3d reconstruction, geometry, gaussian splatting  
- **[DBMovi-GS: Dynamic View Synthesis from Blurry Monocular Video via
  Sparse-Controlled Gaussian Splatting](https://arxiv.org/abs/2506.20998v1)**  
  Authors: Yeon-Ji Song, Jaein Kim, Byung-Ju Kim, Byoung-Tak Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20998v1.pdf)  
  Keywords: dynamic, motion, 3d gaussian, ar, geometry, gaussian splatting  
- **[3DGH: 3D Head Generation with Composable Hair and Face](https://arxiv.org/abs/2506.20875v1)**  
  Authors: Chengan He, Junxuan Li, Tobias Kirschstein, Artem Sevastopolsky, Shunsuke Saito, Qingyang Tan, Javier Romero, Chen Cao, Holly Rushmeier, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20875v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://c-he.github.io/projects/3dgh/.)  
  Keywords: head, 3d gaussian, ar, human, face, geometry, gaussian splatting  

### Large Scene

*Showing the latest 50 out of 61 papers*

- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: tracking, high-fidelity, lighting, dynamic, 3d gaussian, ar, outdoor, illumination, geometry, slam, mapping, gaussian splatting  
- **[BézierGS: Dynamic Urban Scene Reconstruction with Bézier Curve
  Gaussian Splatting](https://arxiv.org/abs/2506.22099v2)**  
  Authors: Zipei Ma, Junzhe Jiang, Yurui Chen, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22099v2.pdf)  
  Keywords: autonomous driving, dynamic, motion, urban scene, ar, gaussian splatting  
- **[ICP-3DGS: SfM-free 3D Gaussian Splatting for Large-scale Unbounded
  Scenes](https://arxiv.org/abs/2506.21629v1)**  
  Authors: Chenhao Zhang, Yezhi Shen, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21629v1.pdf)  
  Keywords: motion, 3d gaussian, ar, outdoor, nerf, neural rendering, gaussian splatting  
- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: tracking, 3d gaussian, ar, outdoor, slam, gaussian splatting  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: efficient, autonomous driving, high-fidelity, dynamic, 3d gaussian, ar, outdoor, nerf, face, survey, gaussian splatting  
- **[Multiview Geometric Regularization of Gaussian Splatting for Accurate
  Radiance Fields](https://arxiv.org/abs/2506.13508v1)**  
  Authors: Jungeon Kim, Geonsoo Park, Seungyong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13508v1.pdf)  
  Keywords: 3d gaussian, ar, outdoor, geometry, gaussian splatting  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language
  Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: efficient, fast, semantic, 3d gaussian, ar, outdoor, segmentation, geometry, understanding, gaussian splatting  
- **[TraGraph-GS: Trajectory Graph-based Gaussian Splatting for Arbitrary
  Large-Scale Scene Rendering](https://arxiv.org/abs/2506.08704v1)**  
  Authors: Xiaohan Zhang, Sitong Wang, Yushen Yan, Yi Yang, Mingda Xu, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08704v1.pdf)  
  Keywords: large scene, ar, gaussian splatting  
- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from
  Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: efficient, fast, motion, 3d gaussian, ar, large scene, slam, gaussian splatting  
- **[Photoreal Scene Reconstruction from an Egocentric Device](https://arxiv.org/abs/2506.04444v1)**  
  Authors: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04444v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.projectaria.com/photoreal-reconstruction/)  
  Keywords: lighting, dynamic, ar, outdoor, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 393 papers*

- **[VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online
  Semantic Gaussian Splatting](https://arxiv.org/abs/2507.01125v1)**  
  Authors: Keiko Nagami, Timothy Chen, Javier Yu, Ola Shorinwa, Maximilian Adang, Carlyn Dougherty, Eric Cristofalo, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01125v1.pdf)  
  Keywords: efficient, semantic, 3d gaussian, ar, gaussian splatting  
- **[A LoD of Gaussians: Unified Training and Rendering for Ultra-Large Scale
  Reconstruction with External Memory](https://arxiv.org/abs/2507.01110v1)**  
  Authors: Felix Windisch, Lukas Radl, Thomas Köhler, Michael Steiner, Dieter Schmalstieg, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01110v1.pdf)  
  Keywords: lightweight, efficient, dynamic, ar, real-time rendering, vr, gaussian splatting  
- **[GaussianVLM: Scene-centric 3D Vision-Language Models using
  Language-aligned Gaussian Splats for Embodied Reasoning and Beyond](https://arxiv.org/abs/2507.00886v1)**  
  Authors: Anna-Maria Halacheva, Jan-Nico Zaech, Xi Wang, Danda Pani Paudel, Luc Van Gool  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00886v1.pdf)  
  Keywords: fast, 3d gaussian, compact, ar, understanding, gaussian splatting  
- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: efficient, fast, 3d gaussian, ar, face, animation, geometry, gaussian splatting  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: efficient rendering, efficient, motion, 3d gaussian, ar, 3d reconstruction, nerf, face, gaussian splatting  
- **[From Coarse to Fine: Learnable Discrete Wavelet Transforms for Efficient
  3D Gaussian Splatting](https://arxiv.org/abs/2506.23042v1)**  
  Authors: Hung Nguyen, An Le, Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23042v1.pdf)  
  Keywords: ar, efficient, 3d gaussian, gaussian splatting  
- **[Confident Splatting: Confidence-Based Compression of 3D Gaussian
  Splatting via Learnable Beta Distributions](https://arxiv.org/abs/2506.22973v1)**  
  Authors: AmirHossein Naghi Razlighi, Elaheh Badali Golezani, Shohreh Kasaei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22973v1.pdf)  
  Keywords: head, 3d gaussian, ar, real-time rendering, compression, gaussian splatting  
- **[DIGS: Dynamic CBCT Reconstruction using Deformation-Informed 4D Gaussian
  Splatting and a Low-Rank Free-Form Deformation Model](https://arxiv.org/abs/2506.22280v1)**  
  Authors: Yuliang Huang, Imraj Singh, Thomas Joyce, Kris Thielemans, Jamie R. McClelland  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22280v1.pdf)  
  Keywords: 4d, efficient, dynamic, motion, ar, deformation, gaussian splatting  
- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, efficient, dynamic, motion, 3d gaussian, ar, 3d reconstruction, face, slam, mapping, gaussian splatting  
- **[CL-Splats: Continual Learning of Gaussian Splatting with Local
  Optimization](https://arxiv.org/abs/2506.21117v1)**  
  Authors: Jan Ackermann, Jonas Kulhanek, Shengqu Cai, Haofei Xu, Marc Pollefeys, Gordon Wetzstein, Leonidas Guibas, Songyou Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21117v1.pdf)  
  Keywords: head, efficient, dynamic, ar, segmentation, robotics, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 159 papers*

- **[GDGS: 3D Gaussian Splatting Via Geometry-Guided Initialization And
  Dynamic Density Control](https://arxiv.org/abs/2507.00363v1)**  
  Authors: Xingjun Wang, Lianlei Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00363v1.pdf)  
  Keywords: fast, high-fidelity, dynamic, 3d gaussian, ar, real-time rendering, face, geometry, gaussian splatting  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: tracking, high-fidelity, lighting, dynamic, 3d gaussian, ar, outdoor, illumination, geometry, slam, mapping, gaussian splatting  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: efficient, high-fidelity, ray tracing, ar, real-time rendering, gaussian splatting  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: efficient, autonomous driving, high-fidelity, dynamic, 3d gaussian, ar, outdoor, nerf, face, survey, gaussian splatting  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: autonomous driving, high-fidelity, 3d gaussian, ar, 3d reconstruction, nerf, survey, vr, neural rendering, robotics, gaussian splatting  
- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads
  Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: head, efficient, high-fidelity, dynamic, ar, face, gaussian splatting  
- **[PF-LHM: 3D Animatable Avatar Reconstruction from Pose-free Articulated
  Human Images](https://arxiv.org/abs/2506.13766v1)**  
  Authors: Lingteng Qiu, Peihao Li, Qi Zuo, Xiaodong Gu, Yuan Dong, Weihao Yuan, Siyu Zhu, Xiaoguang Han, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13766v1.pdf)  
  Keywords: efficient, high-fidelity, 3d gaussian, ar, human, avatar, geometry  
- **[GaussianVAE: Adaptive Learning Dynamics of 3D Gaussians for
  High-Fidelity Super-Resolution](https://arxiv.org/abs/2506.07897v1)**  
  Authors: Shuja Khalid, Mohamed Ibrahim, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07897v1.pdf)  
  Keywords: lightweight, high-fidelity, dynamic, 3d gaussian, ar, gaussian splatting  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline
  Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, ar, sparse view, gaussian splatting  
- **[Parametric Gaussian Human Model: Generalizable Prior for Efficient and
  Realistic Human Avatar Modeling](https://arxiv.org/abs/2506.06645v1)**  
  Authors: Cheng Peng, Jingxiang Sun, Yushuo Chen, Zhaoqi Su, Zhuo Su, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06645v1.pdf)  
  Keywords: head, efficient, fast, high-fidelity, 3d gaussian, compact, ar, human, face, avatar, geometry, gaussian splatting  

### Ray Tracing

- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: efficient, high-fidelity, ray tracing, ar, real-time rendering, gaussian splatting  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: fast, shadow, lighting, ray tracing, geometry, ar, human, avatar, relighting, relightable, gaussian splatting  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: efficient rendering, efficient, acceleration, ray tracing, lighting, 3d gaussian, ar, relighting, gaussian splatting  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: efficient, ray marching, acceleration, dynamic, 3d gaussian, compact, ar, animation, gaussian splatting  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: efficient, global illumination, lighting, ray tracing, 3d gaussian, ar, real-time rendering, illumination, face, gaussian splatting  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: fast, shadow, ray tracing, 3d gaussian, ar, reflection, neural rendering, gaussian splatting  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: shadow, lighting, ray tracing, reflection, face, gaussian splatting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation
  Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, 3d gaussian, ar, survey, gaussian splatting  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: light transport, efficient, acceleration, ray tracing, ar, reflection, gaussian splatting  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: shadow, ray tracing, 3d gaussian, ar, reflection, gaussian splatting  

### Relighting

*Showing the latest 50 out of 107 papers*

- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: semantic, lighting, tracking, ar, segmentation, 3d reconstruction, deformation, understanding, gaussian splatting  
- **[Endo-4DGX: Robust Endoscopic Scene Reconstruction and Illumination
  Correction with Gaussian Splatting](https://arxiv.org/abs/2506.23308v1)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Yanheng Li, Tong Chen, Jie Wang, Jinlin Wu, Zhen Lei, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23308v1.pdf)  
  Keywords: 4d, lighting, dynamic, 3d gaussian, ar, illumination, gaussian splatting  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: tracking, high-fidelity, lighting, dynamic, 3d gaussian, ar, outdoor, illumination, geometry, slam, mapping, gaussian splatting  
- **[MADrive: Memory-Augmented Driving Scene Modeling](https://arxiv.org/abs/2506.21520v1)**  
  Authors: Polina Karpikova, Daniil Selikhanovych, Kirill Struminsky, Ruslan Musaev, Maria Golitsyna, Dmitry Baranchuk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21520v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yandex-research.github.io/madrive/)  
  Keywords: autonomous driving, lighting, 3d gaussian, ar, relighting, gaussian splatting  
- **[Micro-macro Gaussian Splatting with Enhanced Scalability for
  Unconstrained Scene Reconstruction](https://arxiv.org/abs/2506.13516v1)**  
  Authors: Yihui Li, Chengxin Lv, Hongyu Yang, Di Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13516v1.pdf)  
  Keywords: motion, ar, 3d reconstruction, illumination, gaussian splatting  
- **[GS-2DGS: Geometrically Supervised 2DGS for Reflective Object
  Reconstruction](https://arxiv.org/abs/2506.13110v1)**  
  Authors: Jinguang Tong, Xuesong li, Fahira Afzal Maken, Sundaram Muthu, Lars Petersson, Chuong Nguyen, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13110v1.pdf)  
  Keywords: fast, lighting, 3d gaussian, ar, real-time rendering, face, relighting, gaussian splatting  
- **[Efficient multi-view training for 3D Gaussian Splatting](https://arxiv.org/abs/2506.12727v2)**  
  Authors: Minhyuk Choi, Injae Kim, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12727v2.pdf)  
  Keywords: head, efficient, lighting, 3d gaussian, ar, nerf, gaussian splatting  
- **[R3D2: Realistic 3D Asset Insertion via Diffusion for Autonomous Driving
  Simulation](https://arxiv.org/abs/2506.07826v1)**  
  Authors: William Ljungbergh, Bernardo Taveira, Wenzhao Zheng, Adam Tonderski, Chensheng Peng, Fredrik Kahl, Christoffer Petersson, Michael Felsberg, Kurt Keutzer, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07826v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/R3D2/.)  
  Keywords: lightweight, autonomous driving, shadow, lighting, dynamic, 3d gaussian, ar, illumination, neural rendering, gaussian splatting  
- **[SPC to 3D: Novel View Synthesis from Binary SPC via I2I translation](https://arxiv.org/abs/2506.06890v1)**  
  Authors: Sumit Sharma, Gopi Raju Matta, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06890v1.pdf)  
  Keywords: ar, 3d reconstruction, nerf, illumination, gaussian splatting  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for
  Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: efficient, lighting, high-fidelity, motion, 3d gaussian, ar, 3d reconstruction, geometry, gaussian splatting  

### SLAM

*Showing the latest 50 out of 155 papers*

- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: semantic, lighting, tracking, ar, segmentation, 3d reconstruction, deformation, understanding, gaussian splatting  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: tracking, high-fidelity, lighting, dynamic, 3d gaussian, ar, outdoor, illumination, geometry, slam, mapping, gaussian splatting  
- **[VoteSplat: Hough Voting Gaussian Splatting for 3D Scene Understanding](https://arxiv.org/abs/2506.22799v1)**  
  Authors: Minchao Jiang, Shunyu Jia, Jiaming Gu, Xiaoyuan Lu, Guangming Zhu, Anqi Dong, Liang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sy-ja.github.io/votesplat/)  
  Keywords: localization, semantic, 3d gaussian, ar, segmentation, real-time rendering, understanding, gaussian splatting  
- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, efficient, dynamic, motion, 3d gaussian, ar, 3d reconstruction, face, slam, mapping, gaussian splatting  
- **[SAR-GS: 3D Gaussian Splatting for Synthetic Aperture Radar Target
  Reconstruction](https://arxiv.org/abs/2506.21633v1)**  
  Authors: Aobo Li, Zhengxin Lei, Jiangtao Wei, Feng Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21633v1.pdf)  
  Keywords: 3d gaussian, ar, 3d reconstruction, mapping, gaussian splatting  
- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: tracking, 3d gaussian, ar, outdoor, slam, gaussian splatting  
- **[RA-NeRF: Robust Neural Radiance Field Reconstruction with Accurate
  Camera Pose Estimation under Complex Trajectories](https://arxiv.org/abs/2506.15242v2)**  
  Authors: Qingsong Yan, Qiang Wang, Kaiyong Zhao, Jie Chen, Bo Li, Xiaowen Chu, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15242v2.pdf)  
  Keywords: localization, 3d gaussian, ar, 3d reconstruction, nerf, slam, gaussian splatting  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty
  Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: head, lightweight, efficient, 3d gaussian, ar, 3d reconstruction, nerf, neural rendering, mapping, gaussian splatting  
- **[TextureSplat: Per-Primitive Texture Mapping for Reflective Gaussian
  Splatting](https://arxiv.org/abs/2506.13348v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13348v1.pdf)  
  Keywords: face, mapping, ar, gaussian splatting  
- **[Rasterizing Wireless Radiance Field via Deformable 2D Gaussian Splatting](https://arxiv.org/abs/2506.12787v2)**  
  Authors: Mufan Liu, Cixiao Zhang, Qi Yang, Yujie Cao, Yiling Xu, Yin Xu, Shu Sun, Mingzeng Dai, Yunfeng Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12787v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://evan-sudo.github.io/swiftwrf/.)  
  Keywords: lightweight, localization, fast, compact, ar, nerf, deformation, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 183 papers*

- **[VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online
  Semantic Gaussian Splatting](https://arxiv.org/abs/2507.01125v1)**  
  Authors: Keiko Nagami, Timothy Chen, Javier Yu, Ola Shorinwa, Maximilian Adang, Carlyn Dougherty, Eric Cristofalo, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.01125v1.pdf)  
  Keywords: efficient, semantic, 3d gaussian, ar, gaussian splatting  
- **[GaussianVLM: Scene-centric 3D Vision-Language Models using
  Language-aligned Gaussian Splats for Embodied Reasoning and Beyond](https://arxiv.org/abs/2507.00886v1)**  
  Authors: Anna-Maria Halacheva, Jan-Nico Zaech, Xi Wang, Danda Pani Paudel, Luc Van Gool  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.00886v1.pdf)  
  Keywords: fast, 3d gaussian, compact, ar, understanding, gaussian splatting  
- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: semantic, lighting, tracking, ar, segmentation, 3d reconstruction, deformation, understanding, gaussian splatting  
- **[VoteSplat: Hough Voting Gaussian Splatting for 3D Scene Understanding](https://arxiv.org/abs/2506.22799v1)**  
  Authors: Minchao Jiang, Shunyu Jia, Jiaming Gu, Xiaoyuan Lu, Guangming Zhu, Anqi Dong, Liang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sy-ja.github.io/votesplat/)  
  Keywords: localization, semantic, 3d gaussian, ar, segmentation, real-time rendering, understanding, gaussian splatting  
- **[RoboPearls: Editable Video Simulation for Robot Manipulation](https://arxiv.org/abs/2506.22756v1)**  
  Authors: Tao Tang, Likui Zhang, Youpeng Wen, Kaidong Zhang, Jia-Wang Bian, xia zhou, Tianyi Yan, Kun Zhan, Peng Jia, Hefeng Wu, Liang Lin, Xiaodan Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22756v1.pdf)  
  Keywords: 4d, semantic, 3d gaussian, ar, gaussian splatting  
- **[CL-Splats: Continual Learning of Gaussian Splatting with Local
  Optimization](https://arxiv.org/abs/2506.21117v1)**  
  Authors: Jan Ackermann, Jonas Kulhanek, Shengqu Cai, Haofei Xu, Marc Pollefeys, Gordon Wetzstein, Leonidas Guibas, Songyou Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21117v1.pdf)  
  Keywords: head, efficient, dynamic, ar, segmentation, robotics, gaussian splatting  
- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: dynamic, motion, body, ar, deformation, understanding, gaussian splatting  
- **[3D Arena: An Open Platform for Generative 3D Evaluation](https://arxiv.org/abs/2506.18787v1)**  
  Authors: Dylan Ebert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18787v1.pdf)  
  Keywords: human, understanding, ar  
- **[Reconstructing Tornadoes in 3D with Gaussian Splatting](https://arxiv.org/abs/2506.18677v1)**  
  Authors: Adam Yang, Nadula Kadawedduwa, Tianfu Wang, Maria Molina, Christopher Metzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18677v1.pdf)  
  Keywords: understanding, ar, 3d gaussian, gaussian splatting  
- **[SPLATART: Articulated Gaussian Splatting with Estimated Object Structure](https://arxiv.org/abs/2506.12184v1)**  
  Authors: Stanley Lewis, Vishal Chandra, Tom Gao, Odest Chadwicke Jenkins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12184v1.pdf)  
  Keywords: ar, segmentation, geometry, robotics, gaussian splatting  



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