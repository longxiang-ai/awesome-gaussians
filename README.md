# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-07-02 00:55:50

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
- [Acceleration](#acceleration) (275 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (333 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (390 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (74 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (315 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (61 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (392 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (160 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (18 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (108 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (155 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (181 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: outdoor, gaussian splatting, survey, efficient, autonomous driving, ar, face, dynamic, nerf, high-fidelity, 3d gaussian  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: robotics, gaussian splatting, 3d reconstruction, high-fidelity, neural rendering, survey, autonomous driving, ar, vr, nerf, 3d gaussian  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: outdoor, gaussian splatting, semantic, 3d reconstruction, segmentation, survey, neural rendering, efficient, understanding, ar, high-fidelity, 3d gaussian  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: localization, gaussian splatting, semantic, segmentation, slam, survey, efficient, ar, mapping, nerf, 3d gaussian  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to
  Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: gaussian splatting, body, motion, survey, understanding, ar, 4d, dynamic, 3d gaussian  
- **[A Survey of 3D Reconstruction with Event Cameras](https://arxiv.org/abs/2505.08438v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v2.pdf)  
  Keywords: robotics, gaussian splatting, illumination, 3d reconstruction, motion, neural rendering, survey, autonomous driving, geometry, ar, dynamic, nerf, 3d gaussian  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, survey, efficient, ar, fast  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: lighting, 3d reconstruction, survey, ar, 3d gaussian  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From
  Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting
  (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf)  
  Keywords: outdoor, gaussian splatting, 3d reconstruction, survey, sparse view, understanding, geometry, ar, face, nerf, 3d gaussian  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf)  
  Keywords: robotics, gaussian splatting, semantic, lighting, segmentation, survey, ar, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 275 papers*

- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, geometry, ar, face, fast, animation  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: gaussian splatting, efficient rendering, 3d reconstruction, motion, efficient, ar, face, nerf, 3d gaussian  
- **[Confident Splatting: Confidence-Based Compression of 3D Gaussian
  Splatting via Learnable Beta Distributions](https://arxiv.org/abs/2506.22973v1)**  
  Authors: AmirHossein Naghi Razlighi, Elaheh Badali Golezani, Shohreh Kasaei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22973v1.pdf)  
  Keywords: gaussian splatting, head, compression, ar, real-time rendering, 3d gaussian  
- **[VoteSplat: Hough Voting Gaussian Splatting for 3D Scene Understanding](https://arxiv.org/abs/2506.22799v1)**  
  Authors: Minchao Jiang, Shunyu Jia, Jiaming Gu, Xiaoyuan Lu, Guangming Zhu, Anqi Dong, Liang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sy-ja.github.io/votesplat/)  
  Keywords: localization, gaussian splatting, semantic, segmentation, understanding, ar, real-time rendering, 3d gaussian  
- **[Geometry and Perception Guided Gaussians for Multiview-consistent 3D
  Generation from a Single Image](https://arxiv.org/abs/2506.21152v1)**  
  Authors: Pufan Li, Bi'an Du, Wei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21152v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, geometry, ar, fast, 3d gaussian  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: gaussian splatting, ray tracing, efficient, ar, real-time rendering, high-fidelity  
- **[Virtual Memory for 3D Gaussian Splatting](https://arxiv.org/abs/2506.19415v1)**  
  Authors: Jonathan Haberl, Philipp Fleck, Clemens Arth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19415v1.pdf)  
  Keywords: gaussian splatting, efficient, ar, real-time rendering, dynamic, 3d gaussian  
- **[3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D
  Gaussian-Splatting](https://arxiv.org/abs/2506.14642v1)**  
  Authors: Yuke Xing, Jiarui Wang, Peizhi Niu, Wenjie Huang, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14642v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, compression, ar, real-time rendering, human  
- **[GS-2DGS: Geometrically Supervised 2DGS for Reflective Object
  Reconstruction](https://arxiv.org/abs/2506.13110v1)**  
  Authors: Jinguang Tong, Xuesong li, Fahira Afzal Maken, Sundaram Muthu, Lars Petersson, Chuong Nguyen, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13110v1.pdf)  
  Keywords: gaussian splatting, lighting, relighting, ar, real-time rendering, face, fast, 3d gaussian  
- **[Rasterizing Wireless Radiance Field via Deformable 2D Gaussian Splatting](https://arxiv.org/abs/2506.12787v2)**  
  Authors: Mufan Liu, Cixiao Zhang, Qi Yang, Yujie Cao, Yiling Xu, Yin Xu, Shu Sun, Mingzeng Dai, Yunfeng Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12787v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://evan-sudo.github.io/swiftwrf/.)  
  Keywords: localization, gaussian splatting, lightweight, deformation, ar, nerf, fast, compact  

### Applications

*Showing the latest 50 out of 995 papers*

- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, geometry, ar, face, fast, animation  
- **[GaVS: 3D-Grounded Video Stabilization via Temporally-Consistent Local
  Reconstruction and Rendering](https://arxiv.org/abs/2506.23957v1)**  
  Authors: Zinuo You, Stamatios Georgoulis, Anpei Chen, Siyu Tang, Dengxin Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23957v1.pdf)  
  Keywords: gaussian splatting, motion, geometry, ar, dynamic  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: gaussian splatting, efficient rendering, 3d reconstruction, motion, efficient, ar, face, nerf, 3d gaussian  
- **[Instant GaussianImage: A Generalizable and Self-Adaptive Image
  Representation via 2D Gaussian Splatting](https://arxiv.org/abs/2506.23479v1)**  
  Authors: Zhaojie Zeng, Yuesong Wang, Chao Yang, Tao Guan, Lili Ju  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23479v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar  
- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: tracking, gaussian splatting, semantic, lighting, 3d reconstruction, segmentation, deformation, understanding, ar  
- **[Endo-4DGX: Robust Endoscopic Scene Reconstruction and Illumination
  Correction with Gaussian Splatting](https://arxiv.org/abs/2506.23308v1)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Yanheng Li, Tong Chen, Jie Wang, Jinlin Wu, Zhen Lei, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23308v1.pdf)  
  Keywords: gaussian splatting, illumination, lighting, ar, 4d, dynamic, 3d gaussian  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: tracking, outdoor, gaussian splatting, illumination, lighting, slam, geometry, ar, dynamic, mapping, high-fidelity, 3d gaussian  
- **[STD-GS: Exploring Frame-Event Interaction for
  SpatioTemporal-Disentangled Gaussian Splatting to Reconstruct High-Dynamic
  Scene](https://arxiv.org/abs/2506.23157v1)**  
  Authors: Hanyu Zhou, Haonan Wang, Haoyue Liu, Yuxing Duan, Luxin Yan, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23157v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, motion  
- **[From Coarse to Fine: Learnable Discrete Wavelet Transforms for Efficient
  3D Gaussian Splatting](https://arxiv.org/abs/2506.23042v1)**  
  Authors: Hung Nguyen, An Le, Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23042v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, 3d gaussian  
- **[Confident Splatting: Confidence-Based Compression of 3D Gaussian
  Splatting via Learnable Beta Distributions](https://arxiv.org/abs/2506.22973v1)**  
  Authors: AmirHossein Naghi Razlighi, Elaheh Badali Golezani, Shohreh Kasaei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22973v1.pdf)  
  Keywords: gaussian splatting, head, compression, ar, real-time rendering, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 333 papers*

- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, geometry, ar, face, fast, animation  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: gaussian splatting, efficient rendering, 3d reconstruction, motion, efficient, ar, face, nerf, 3d gaussian  
- **[Confident Splatting: Confidence-Based Compression of 3D Gaussian
  Splatting via Learnable Beta Distributions](https://arxiv.org/abs/2506.22973v1)**  
  Authors: AmirHossein Naghi Razlighi, Elaheh Badali Golezani, Shohreh Kasaei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22973v1.pdf)  
  Keywords: gaussian splatting, head, compression, ar, real-time rendering, 3d gaussian  
- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, gaussian splatting, 3d reconstruction, slam, motion, efficient, ar, face, dynamic, mapping, 3d gaussian  
- **[CL-Splats: Continual Learning of Gaussian Splatting with Local
  Optimization](https://arxiv.org/abs/2506.21117v1)**  
  Authors: Jan Ackermann, Jonas Kulhanek, Shengqu Cai, Haofei Xu, Marc Pollefeys, Gordon Wetzstein, Leonidas Guibas, Songyou Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21117v1.pdf)  
  Keywords: robotics, gaussian splatting, segmentation, head, efficient, ar, dynamic  
- **[3DGH: 3D Head Generation with Composable Hair and Face](https://arxiv.org/abs/2506.20875v1)**  
  Authors: Chengan He, Junxuan Li, Tobias Kirschstein, Artem Sevastopolsky, Shunsuke Saito, Qingyang Tan, Javier Romero, Chen Cao, Holly Rushmeier, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20875v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://c-he.github.io/projects/3dgh/.)  
  Keywords: gaussian splatting, 3d gaussian, head, geometry, ar, face, human  
- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: gaussian splatting, body, motion, deformation, understanding, ar, dynamic  
- **[HoliGS: Holistic Gaussian Splatting for Embodied View Synthesis](https://arxiv.org/abs/2506.19291v1)**  
  Authors: Xiaoyuan Wang, Yizhou Zhao, Botao Ye, Xiaojun Shan, Weijie Lyu, Lu Qi, Kelvin C. K. Chan, Yinxiao Li, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19291v1.pdf)  
  Keywords: gaussian splatting, head, deformation, ar, 4d, dynamic, nerf  
- **[3D Arena: An Open Platform for Generative 3D Evaluation](https://arxiv.org/abs/2506.18787v1)**  
  Authors: Dylan Ebert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18787v1.pdf)  
  Keywords: understanding, ar, human  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: outdoor, gaussian splatting, survey, efficient, autonomous driving, ar, face, dynamic, nerf, high-fidelity, 3d gaussian  

### Dynamic Scene

*Showing the latest 50 out of 390 papers*

- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, geometry, ar, face, fast, animation  
- **[GaVS: 3D-Grounded Video Stabilization via Temporally-Consistent Local
  Reconstruction and Rendering](https://arxiv.org/abs/2506.23957v1)**  
  Authors: Zinuo You, Stamatios Georgoulis, Anpei Chen, Siyu Tang, Dengxin Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23957v1.pdf)  
  Keywords: gaussian splatting, motion, geometry, ar, dynamic  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: gaussian splatting, efficient rendering, 3d reconstruction, motion, efficient, ar, face, nerf, 3d gaussian  
- **[Instant GaussianImage: A Generalizable and Self-Adaptive Image
  Representation via 2D Gaussian Splatting](https://arxiv.org/abs/2506.23479v1)**  
  Authors: Zhaojie Zeng, Yuesong Wang, Chao Yang, Tao Guan, Lili Ju  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23479v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar  
- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: tracking, gaussian splatting, semantic, lighting, 3d reconstruction, segmentation, deformation, understanding, ar  
- **[Endo-4DGX: Robust Endoscopic Scene Reconstruction and Illumination
  Correction with Gaussian Splatting](https://arxiv.org/abs/2506.23308v1)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Yanheng Li, Tong Chen, Jie Wang, Jinlin Wu, Zhen Lei, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23308v1.pdf)  
  Keywords: gaussian splatting, illumination, lighting, ar, 4d, dynamic, 3d gaussian  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: tracking, outdoor, gaussian splatting, illumination, lighting, slam, geometry, ar, dynamic, mapping, high-fidelity, 3d gaussian  
- **[STD-GS: Exploring Frame-Event Interaction for
  SpatioTemporal-Disentangled Gaussian Splatting to Reconstruct High-Dynamic
  Scene](https://arxiv.org/abs/2506.23157v1)**  
  Authors: Hanyu Zhou, Haonan Wang, Haoyue Liu, Yuxing Duan, Luxin Yan, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23157v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, motion  
- **[RoboPearls: Editable Video Simulation for Robot Manipulation](https://arxiv.org/abs/2506.22756v1)**  
  Authors: Tao Tang, Likui Zhang, Youpeng Wen, Kaidong Zhang, Jia-Wang Bian, xia zhou, Tianyi Yan, Kun Zhan, Peng Jia, Hefeng Wu, Liang Lin, Xiaodan Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22756v1.pdf)  
  Keywords: gaussian splatting, semantic, ar, 4d, 3d gaussian  
- **[DIGS: Dynamic CBCT Reconstruction using Deformation-Informed 4D Gaussian
  Splatting and a Low-Rank Free-Form Deformation Model](https://arxiv.org/abs/2506.22280v1)**  
  Authors: Yuliang Huang, Imraj Singh, Thomas Joyce, Kris Thielemans, Jamie R. McClelland  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22280v1.pdf)  
  Keywords: gaussian splatting, motion, deformation, efficient, ar, 4d, dynamic  

### Few-shot

*Showing the latest 50 out of 74 papers*

- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from
  RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: gaussian splatting, motion, ar, sparse-view, dynamic  
- **[PointGS: Point Attention-Aware Sparse View Synthesis with Gaussian
  Splatting](https://arxiv.org/abs/2506.10335v1)**  
  Authors: Lintao Xiang, Hongpei Zheng, Yating Huang, Qijun Yang, Hujun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.10335v1.pdf)  
  Keywords: few-shot, gaussian splatting, 3d gaussian, lightweight, ar, nerf, sparse view  
- **[UniForward: Unified 3D Scene and Semantic Field Reconstruction via
  Feed-Forward Gaussian Splatting from Only Sparse-View Images](https://arxiv.org/abs/2506.09378v1)**  
  Authors: Qijian Tian, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09378v1.pdf)  
  Keywords: gaussian splatting, semantic, segmentation, understanding, ar, sparse-view, 3d gaussian  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline
  Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, high-fidelity, sparse view  
- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade
  Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: gaussian splatting, efficient, geometry, ar, sparse-view, nerf, 3d gaussian  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: gaussian splatting, motion, ar, sparse-view, face, 3d gaussian  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian
  Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: gaussian splatting, 3d reconstruction, motion, ar, sparse-view, fast, face  
- **[Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse
  Views by Jointly Training Hemisphere Sampled Synthetic Images](https://arxiv.org/abs/2505.19264v1)**  
  Authors: Guangan Chen, Anh Minh Truong, Hanhe Lin, Michiel Vlaminck, Wilfried Philips, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19264v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, motion, ar, sparse-view, sparse view  
- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane
  Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, head, motion, deformation, efficient, ar, 4d, sparse-view, dynamic, compact  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater
  Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: robotics, gaussian splatting, ar, sparse-view, high-fidelity, 3d gaussian  

### Geometry Reconstruction

*Showing the latest 50 out of 315 papers*

- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, geometry, ar, face, fast, animation  
- **[GaVS: 3D-Grounded Video Stabilization via Temporally-Consistent Local
  Reconstruction and Rendering](https://arxiv.org/abs/2506.23957v1)**  
  Authors: Zinuo You, Stamatios Georgoulis, Anpei Chen, Siyu Tang, Dengxin Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23957v1.pdf)  
  Keywords: gaussian splatting, motion, geometry, ar, dynamic  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: gaussian splatting, efficient rendering, 3d reconstruction, motion, efficient, ar, face, nerf, 3d gaussian  
- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: tracking, gaussian splatting, semantic, lighting, 3d reconstruction, segmentation, deformation, understanding, ar  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: tracking, outdoor, gaussian splatting, illumination, lighting, slam, geometry, ar, dynamic, mapping, high-fidelity, 3d gaussian  
- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, gaussian splatting, 3d reconstruction, slam, motion, efficient, ar, face, dynamic, mapping, 3d gaussian  
- **[Geometry and Perception Guided Gaussians for Multiview-consistent 3D
  Generation from a Single Image](https://arxiv.org/abs/2506.21152v1)**  
  Authors: Pufan Li, Bi'an Du, Wei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21152v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, geometry, ar, fast, 3d gaussian  
- **[DBMovi-GS: Dynamic View Synthesis from Blurry Monocular Video via
  Sparse-Controlled Gaussian Splatting](https://arxiv.org/abs/2506.20998v1)**  
  Authors: Yeon-Ji Song, Jaein Kim, Byung-Ju Kim, Byoung-Tak Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20998v1.pdf)  
  Keywords: gaussian splatting, motion, geometry, ar, dynamic, 3d gaussian  
- **[3DGH: 3D Head Generation with Composable Hair and Face](https://arxiv.org/abs/2506.20875v1)**  
  Authors: Chengan He, Junxuan Li, Tobias Kirschstein, Artem Sevastopolsky, Shunsuke Saito, Qingyang Tan, Javier Romero, Chen Cao, Holly Rushmeier, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20875v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://c-he.github.io/projects/3dgh/.)  
  Keywords: gaussian splatting, 3d gaussian, head, geometry, ar, face, human  
- **[SAR-GS: 3D Gaussian Splatting for Synthetic Aperture Radar Target
  Reconstruction](https://arxiv.org/abs/2506.21633v1)**  
  Authors: Aobo Li, Zhengxin Lei, Jiangtao Wei, Feng Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21633v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, ar, mapping, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 61 papers*

- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: tracking, outdoor, gaussian splatting, illumination, lighting, slam, geometry, ar, dynamic, mapping, high-fidelity, 3d gaussian  
- **[BézierGS: Dynamic Urban Scene Reconstruction with Bézier Curve
  Gaussian Splatting](https://arxiv.org/abs/2506.22099v2)**  
  Authors: Zipei Ma, Junzhe Jiang, Yurui Chen, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22099v2.pdf)  
  Keywords: gaussian splatting, urban scene, motion, autonomous driving, ar, dynamic  
- **[ICP-3DGS: SfM-free 3D Gaussian Splatting for Large-scale Unbounded
  Scenes](https://arxiv.org/abs/2506.21629v1)**  
  Authors: Chenhao Zhang, Yezhi Shen, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21629v1.pdf)  
  Keywords: outdoor, gaussian splatting, motion, neural rendering, ar, nerf, 3d gaussian  
- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: tracking, outdoor, gaussian splatting, slam, ar, 3d gaussian  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: outdoor, gaussian splatting, survey, efficient, autonomous driving, ar, face, dynamic, nerf, high-fidelity, 3d gaussian  
- **[Multiview Geometric Regularization of Gaussian Splatting for Accurate
  Radiance Fields](https://arxiv.org/abs/2506.13508v1)**  
  Authors: Jungeon Kim, Geonsoo Park, Seungyong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13508v1.pdf)  
  Keywords: outdoor, gaussian splatting, geometry, ar, 3d gaussian  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language
  Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: outdoor, gaussian splatting, semantic, segmentation, efficient, understanding, geometry, ar, fast, 3d gaussian  
- **[TraGraph-GS: Trajectory Graph-based Gaussian Splatting for Arbitrary
  Large-Scale Scene Rendering](https://arxiv.org/abs/2506.08704v1)**  
  Authors: Xiaohan Zhang, Sitong Wang, Yushen Yan, Yi Yang, Mingda Xu, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08704v1.pdf)  
  Keywords: gaussian splatting, ar, large scene  
- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from
  Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: gaussian splatting, slam, motion, efficient, ar, large scene, fast, 3d gaussian  
- **[Photoreal Scene Reconstruction from an Egocentric Device](https://arxiv.org/abs/2506.04444v1)**  
  Authors: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04444v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.projectaria.com/photoreal-reconstruction/)  
  Keywords: outdoor, gaussian splatting, lighting, ar, dynamic  

### Model Compression

*Showing the latest 50 out of 392 papers*

- **[MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient
  Surface Reconstruction](https://arxiv.org/abs/2506.24096v1)**  
  Authors: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.24096v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, geometry, ar, face, fast, animation  
- **[AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via
  Structural Attention](https://arxiv.org/abs/2506.23611v1)**  
  Authors: Ziao Liu, Zhenjia Li, Yifeng Shi, Xiangang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23611v1.pdf)  
  Keywords: gaussian splatting, efficient rendering, 3d reconstruction, motion, efficient, ar, face, nerf, 3d gaussian  
- **[From Coarse to Fine: Learnable Discrete Wavelet Transforms for Efficient
  3D Gaussian Splatting](https://arxiv.org/abs/2506.23042v1)**  
  Authors: Hung Nguyen, An Le, Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23042v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, 3d gaussian  
- **[Confident Splatting: Confidence-Based Compression of 3D Gaussian
  Splatting via Learnable Beta Distributions](https://arxiv.org/abs/2506.22973v1)**  
  Authors: AmirHossein Naghi Razlighi, Elaheh Badali Golezani, Shohreh Kasaei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22973v1.pdf)  
  Keywords: gaussian splatting, head, compression, ar, real-time rendering, 3d gaussian  
- **[DIGS: Dynamic CBCT Reconstruction using Deformation-Informed 4D Gaussian
  Splatting and a Low-Rank Free-Form Deformation Model](https://arxiv.org/abs/2506.22280v1)**  
  Authors: Yuliang Huang, Imraj Singh, Thomas Joyce, Kris Thielemans, Jamie R. McClelland  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22280v1.pdf)  
  Keywords: gaussian splatting, motion, deformation, efficient, ar, 4d, dynamic  
- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, gaussian splatting, 3d reconstruction, slam, motion, efficient, ar, face, dynamic, mapping, 3d gaussian  
- **[CL-Splats: Continual Learning of Gaussian Splatting with Local
  Optimization](https://arxiv.org/abs/2506.21117v1)**  
  Authors: Jan Ackermann, Jonas Kulhanek, Shengqu Cai, Haofei Xu, Marc Pollefeys, Gordon Wetzstein, Leonidas Guibas, Songyou Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21117v1.pdf)  
  Keywords: robotics, gaussian splatting, segmentation, head, efficient, ar, dynamic  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: gaussian splatting, ray tracing, efficient, ar, real-time rendering, high-fidelity  
- **[Virtual Memory for 3D Gaussian Splatting](https://arxiv.org/abs/2506.19415v1)**  
  Authors: Jonathan Haberl, Philipp Fleck, Clemens Arth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19415v1.pdf)  
  Keywords: gaussian splatting, efficient, ar, real-time rendering, dynamic, 3d gaussian  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: outdoor, gaussian splatting, survey, efficient, autonomous driving, ar, face, dynamic, nerf, high-fidelity, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 160 papers*

- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: tracking, outdoor, gaussian splatting, illumination, lighting, slam, geometry, ar, dynamic, mapping, high-fidelity, 3d gaussian  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: gaussian splatting, ray tracing, efficient, ar, real-time rendering, high-fidelity  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: outdoor, gaussian splatting, survey, efficient, autonomous driving, ar, face, dynamic, nerf, high-fidelity, 3d gaussian  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: robotics, gaussian splatting, 3d reconstruction, high-fidelity, neural rendering, survey, autonomous driving, ar, vr, nerf, 3d gaussian  
- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads
  Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: gaussian splatting, head, efficient, ar, face, dynamic, high-fidelity  
- **[PF-LHM: 3D Animatable Avatar Reconstruction from Pose-free Articulated
  Human Images](https://arxiv.org/abs/2506.13766v1)**  
  Authors: Lingteng Qiu, Peihao Li, Qi Zuo, Xiaodong Gu, Yuan Dong, Weihao Yuan, Siyu Zhu, Xiaoguang Han, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13766v1.pdf)  
  Keywords: avatar, efficient, geometry, ar, human, high-fidelity, 3d gaussian  
- **[GaussianVAE: Adaptive Learning Dynamics of 3D Gaussians for
  High-Fidelity Super-Resolution](https://arxiv.org/abs/2506.07897v1)**  
  Authors: Shuja Khalid, Mohamed Ibrahim, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07897v1.pdf)  
  Keywords: gaussian splatting, lightweight, ar, dynamic, high-fidelity, 3d gaussian  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline
  Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, high-fidelity, sparse view  
- **[Parametric Gaussian Human Model: Generalizable Prior for Efficient and
  Realistic Human Avatar Modeling](https://arxiv.org/abs/2506.06645v1)**  
  Authors: Cheng Peng, Jingxiang Sun, Yushuo Chen, Zhaoqi Su, Zhuo Su, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06645v1.pdf)  
  Keywords: gaussian splatting, avatar, head, high-fidelity, efficient, geometry, ar, human, face, fast, compact, 3d gaussian  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for
  Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: gaussian splatting, lighting, 3d reconstruction, motion, efficient, geometry, ar, high-fidelity, 3d gaussian  

### Ray Tracing

- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: gaussian splatting, ray tracing, efficient, ar, real-time rendering, high-fidelity  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: gaussian splatting, avatar, lighting, ray tracing, shadow, relighting, geometry, relightable, ar, fast, human  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: acceleration, gaussian splatting, lighting, ray tracing, efficient rendering, efficient, relighting, ar, 3d gaussian  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: acceleration, animation, ray marching, gaussian splatting, efficient, ar, dynamic, compact, 3d gaussian  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: gaussian splatting, illumination, lighting, ray tracing, global illumination, efficient, ar, real-time rendering, face, 3d gaussian  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: gaussian splatting, ray tracing, neural rendering, shadow, reflection, ar, fast, 3d gaussian  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: gaussian splatting, lighting, ray tracing, reflection, shadow, face  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation
  Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, ray tracing, survey, ar, 3d gaussian  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: acceleration, gaussian splatting, ray tracing, reflection, light transport, efficient, ar  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: gaussian splatting, ray tracing, shadow, reflection, ar, 3d gaussian  

### Relighting

*Showing the latest 50 out of 108 papers*

- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: tracking, gaussian splatting, semantic, lighting, 3d reconstruction, segmentation, deformation, understanding, ar  
- **[Endo-4DGX: Robust Endoscopic Scene Reconstruction and Illumination
  Correction with Gaussian Splatting](https://arxiv.org/abs/2506.23308v1)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Yanheng Li, Tong Chen, Jie Wang, Jinlin Wu, Zhen Lei, Hongbin Liu, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23308v1.pdf)  
  Keywords: gaussian splatting, illumination, lighting, ar, 4d, dynamic, 3d gaussian  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: tracking, outdoor, gaussian splatting, illumination, lighting, slam, geometry, ar, dynamic, mapping, high-fidelity, 3d gaussian  
- **[MADrive: Memory-Augmented Driving Scene Modeling](https://arxiv.org/abs/2506.21520v1)**  
  Authors: Polina Karpikova, Daniil Selikhanovych, Kirill Struminsky, Ruslan Musaev, Maria Golitsyna, Dmitry Baranchuk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21520v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yandex-research.github.io/madrive/)  
  Keywords: gaussian splatting, lighting, relighting, autonomous driving, ar, 3d gaussian  
- **[Micro-macro Gaussian Splatting with Enhanced Scalability for
  Unconstrained Scene Reconstruction](https://arxiv.org/abs/2506.13516v1)**  
  Authors: Yihui Li, Chengxin Lv, Hongyu Yang, Di Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13516v1.pdf)  
  Keywords: gaussian splatting, illumination, 3d reconstruction, motion, ar  
- **[GS-2DGS: Geometrically Supervised 2DGS for Reflective Object
  Reconstruction](https://arxiv.org/abs/2506.13110v1)**  
  Authors: Jinguang Tong, Xuesong li, Fahira Afzal Maken, Sundaram Muthu, Lars Petersson, Chuong Nguyen, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13110v1.pdf)  
  Keywords: gaussian splatting, lighting, relighting, ar, real-time rendering, face, fast, 3d gaussian  
- **[Efficient multi-view training for 3D Gaussian Splatting](https://arxiv.org/abs/2506.12727v2)**  
  Authors: Minhyuk Choi, Injae Kim, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12727v2.pdf)  
  Keywords: gaussian splatting, lighting, head, efficient, ar, nerf, 3d gaussian  
- **[R3D2: Realistic 3D Asset Insertion via Diffusion for Autonomous Driving
  Simulation](https://arxiv.org/abs/2506.07826v1)**  
  Authors: William Ljungbergh, Bernardo Taveira, Wenzhao Zheng, Adam Tonderski, Chensheng Peng, Fredrik Kahl, Christoffer Petersson, Michael Felsberg, Kurt Keutzer, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07826v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/R3D2/.)  
  Keywords: gaussian splatting, illumination, lighting, lightweight, neural rendering, shadow, autonomous driving, ar, dynamic, 3d gaussian  
- **[SPC to 3D: Novel View Synthesis from Binary SPC via I2I translation](https://arxiv.org/abs/2506.06890v1)**  
  Authors: Sumit Sharma, Gopi Raju Matta, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06890v1.pdf)  
  Keywords: gaussian splatting, illumination, 3d reconstruction, ar, nerf  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for
  Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: gaussian splatting, lighting, 3d reconstruction, motion, efficient, geometry, ar, high-fidelity, 3d gaussian  

### SLAM

*Showing the latest 50 out of 155 papers*

- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: tracking, gaussian splatting, semantic, lighting, 3d reconstruction, segmentation, deformation, understanding, ar  
- **[TVG-SLAM: Robust Gaussian Splatting SLAM with Tri-view Geometric
  Constraints](https://arxiv.org/abs/2506.23207v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Lei Feng, Yangbing Ge, Shuaifeng Zhi, Jiaxiong Liu, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23207v1.pdf)  
  Keywords: tracking, outdoor, gaussian splatting, illumination, lighting, slam, geometry, ar, dynamic, mapping, high-fidelity, 3d gaussian  
- **[VoteSplat: Hough Voting Gaussian Splatting for 3D Scene Understanding](https://arxiv.org/abs/2506.22799v1)**  
  Authors: Minchao Jiang, Shunyu Jia, Jiaming Gu, Xiaoyuan Lu, Guangming Zhu, Anqi Dong, Liang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sy-ja.github.io/votesplat/)  
  Keywords: localization, gaussian splatting, semantic, segmentation, understanding, ar, real-time rendering, 3d gaussian  
- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, gaussian splatting, 3d reconstruction, slam, motion, efficient, ar, face, dynamic, mapping, 3d gaussian  
- **[SAR-GS: 3D Gaussian Splatting for Synthetic Aperture Radar Target
  Reconstruction](https://arxiv.org/abs/2506.21633v1)**  
  Authors: Aobo Li, Zhengxin Lei, Jiangtao Wei, Feng Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21633v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, ar, mapping, 3d gaussian  
- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: tracking, outdoor, gaussian splatting, slam, ar, 3d gaussian  
- **[RA-NeRF: Robust Neural Radiance Field Reconstruction with Accurate
  Camera Pose Estimation under Complex Trajectories](https://arxiv.org/abs/2506.15242v2)**  
  Authors: Qingsong Yan, Qiang Wang, Kaiyong Zhao, Jie Chen, Bo Li, Xiaowen Chu, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15242v2.pdf)  
  Keywords: localization, gaussian splatting, 3d reconstruction, slam, ar, nerf, 3d gaussian  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty
  Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, lightweight, head, neural rendering, efficient, ar, mapping, nerf, 3d gaussian  
- **[TextureSplat: Per-Primitive Texture Mapping for Reflective Gaussian
  Splatting](https://arxiv.org/abs/2506.13348v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13348v1.pdf)  
  Keywords: face, mapping, gaussian splatting, ar  
- **[Rasterizing Wireless Radiance Field via Deformable 2D Gaussian Splatting](https://arxiv.org/abs/2506.12787v2)**  
  Authors: Mufan Liu, Cixiao Zhang, Qi Yang, Yujie Cao, Yiling Xu, Yin Xu, Shu Sun, Mingzeng Dai, Yunfeng Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12787v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://evan-sudo.github.io/swiftwrf/.)  
  Keywords: localization, gaussian splatting, lightweight, deformation, ar, nerf, fast, compact  

### Scene Understanding

*Showing the latest 50 out of 181 papers*

- **[SurgTPGS: Semantic 3D Surgical Scene Understanding with Text Promptable
  Gaussian Splatting](https://arxiv.org/abs/2506.23309v2)**  
  Authors: Yiming Huang, Long Bai, Beilei Cui, Kun Yuan, Guankun Wang, Mobarak I. Hoque, Nicolas Padoy, Nassir Navab, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.23309v2.pdf)  
  Keywords: tracking, gaussian splatting, semantic, lighting, 3d reconstruction, segmentation, deformation, understanding, ar  
- **[VoteSplat: Hough Voting Gaussian Splatting for 3D Scene Understanding](https://arxiv.org/abs/2506.22799v1)**  
  Authors: Minchao Jiang, Shunyu Jia, Jiaming Gu, Xiaoyuan Lu, Guangming Zhu, Anqi Dong, Liang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sy-ja.github.io/votesplat/)  
  Keywords: localization, gaussian splatting, semantic, segmentation, understanding, ar, real-time rendering, 3d gaussian  
- **[RoboPearls: Editable Video Simulation for Robot Manipulation](https://arxiv.org/abs/2506.22756v1)**  
  Authors: Tao Tang, Likui Zhang, Youpeng Wen, Kaidong Zhang, Jia-Wang Bian, xia zhou, Tianyi Yan, Kun Zhan, Peng Jia, Hefeng Wu, Liang Lin, Xiaodan Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.22756v1.pdf)  
  Keywords: gaussian splatting, semantic, ar, 4d, 3d gaussian  
- **[CL-Splats: Continual Learning of Gaussian Splatting with Local
  Optimization](https://arxiv.org/abs/2506.21117v1)**  
  Authors: Jan Ackermann, Jonas Kulhanek, Shengqu Cai, Haofei Xu, Marc Pollefeys, Gordon Wetzstein, Leonidas Guibas, Songyou Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21117v1.pdf)  
  Keywords: robotics, gaussian splatting, segmentation, head, efficient, ar, dynamic  
- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: gaussian splatting, body, motion, deformation, understanding, ar, dynamic  
- **[3D Arena: An Open Platform for Generative 3D Evaluation](https://arxiv.org/abs/2506.18787v1)**  
  Authors: Dylan Ebert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18787v1.pdf)  
  Keywords: understanding, ar, human  
- **[Reconstructing Tornadoes in 3D with Gaussian Splatting](https://arxiv.org/abs/2506.18677v1)**  
  Authors: Adam Yang, Nadula Kadawedduwa, Tianfu Wang, Maria Molina, Christopher Metzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18677v1.pdf)  
  Keywords: understanding, gaussian splatting, ar, 3d gaussian  
- **[SPLATART: Articulated Gaussian Splatting with Estimated Object Structure](https://arxiv.org/abs/2506.12184v1)**  
  Authors: Stanley Lewis, Vishal Chandra, Tom Gao, Odest Chadwicke Jenkins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12184v1.pdf)  
  Keywords: robotics, gaussian splatting, segmentation, geometry, ar  
- **[ODG: Occupancy Prediction Using Dual Gaussians](https://arxiv.org/abs/2506.09417v2)**  
  Authors: Yunxiao Shi, Yinhao Zhu, Shizhong Han, Jisoo Jeong, Amin Ansari, Hong Cai, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09417v2.pdf)  
  Keywords: gaussian splatting, semantic, autonomous driving, geometry, ar, real-time rendering, dynamic, 3d gaussian  
- **[UniForward: Unified 3D Scene and Semantic Field Reconstruction via
  Feed-Forward Gaussian Splatting from Only Sparse-View Images](https://arxiv.org/abs/2506.09378v1)**  
  Authors: Qijian Tian, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09378v1.pdf)  
  Keywords: gaussian splatting, semantic, segmentation, understanding, ar, sparse-view, 3d gaussian  



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