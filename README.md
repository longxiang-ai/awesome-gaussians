# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-06-30 00:59:04

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
- [Acceleration](#acceleration) (276 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (335 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (383 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (75 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (314 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (58 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (392 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (162 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (18 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (107 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (157 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (182 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: face, 3d gaussian, high-fidelity, gaussian splatting, dynamic, efficient, outdoor, nerf, autonomous driving, survey, ar  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, autonomous driving, 3d reconstruction, robotics, vr, nerf, neural rendering, survey, ar  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: segmentation, 3d gaussian, high-fidelity, gaussian splatting, 3d reconstruction, efficient, understanding, outdoor, semantic, neural rendering, survey, ar  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: segmentation, localization, 3d gaussian, gaussian splatting, efficient, slam, mapping, nerf, semantic, survey, ar  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to
  Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, 4d, understanding, motion, dynamic, body, survey, ar  
- **[A Survey of 3D Reconstruction with Event Cameras](https://arxiv.org/abs/2505.08438v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v2.pdf)  
  Keywords: illumination, geometry, 3d gaussian, gaussian splatting, dynamic, autonomous driving, 3d reconstruction, robotics, motion, nerf, neural rendering, survey, ar  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: gaussian splatting, efficient, 3d reconstruction, fast, survey, ar  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, lighting, survey, ar  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From
  Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting
  (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf)  
  Keywords: geometry, 3d gaussian, face, gaussian splatting, 3d reconstruction, understanding, outdoor, nerf, sparse view, survey, ar  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf)  
  Keywords: segmentation, 3d gaussian, gaussian splatting, robotics, ar, lighting, survey, semantic  

### Acceleration

*Showing the latest 50 out of 276 papers*

- **[Geometry and Perception Guided Gaussians for Multiview-consistent 3D
  Generation from a Single Image](https://arxiv.org/abs/2506.21152v1)**  
  Authors: Pufan Li, Bi'an Du, Wei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21152v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, 3d reconstruction, fast, ar  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: real-time rendering, high-fidelity, gaussian splatting, efficient, ray tracing, ar  
- **[Virtual Memory for 3D Gaussian Splatting](https://arxiv.org/abs/2506.19415v1)**  
  Authors: Jonathan Haberl, Philipp Fleck, Clemens Arth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19415v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, gaussian splatting, efficient, dynamic, ar  
- **[3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D
  Gaussian-Splatting](https://arxiv.org/abs/2506.14642v1)**  
  Authors: Yuke Xing, Jiarui Wang, Peizhi Niu, Wenjie Huang, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14642v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, compression, gaussian splatting, human, ar  
- **[GS-2DGS: Geometrically Supervised 2DGS for Reflective Object
  Reconstruction](https://arxiv.org/abs/2506.13110v1)**  
  Authors: Jinguang Tong, Xuesong li, Fahira Afzal Maken, Sundaram Muthu, Lars Petersson, Chuong Nguyen, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13110v1.pdf)  
  Keywords: real-time rendering, relighting, 3d gaussian, gaussian splatting, fast, face, lighting, ar  
- **[Rasterizing Wireless Radiance Field via Deformable 2D Gaussian Splatting](https://arxiv.org/abs/2506.12787v2)**  
  Authors: Mufan Liu, Cixiao Zhang, Qi Yang, Yujie Cao, Yiling Xu, Yin Xu, Shu Sun, Mingzeng Dai, Yunfeng Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12787v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://evan-sudo.github.io/swiftwrf/.)  
  Keywords: localization, lightweight, gaussian splatting, fast, compact, deformation, nerf, ar  
- **[HAIF-GS: Hierarchical and Induced Flow-Guided Gaussian Splatting for
  Dynamic Scene](https://arxiv.org/abs/2506.09518v1)**  
  Authors: Jianing Chen, Zehao Li, Yujun Cai, Hao Jiang, Chengxuan Qian, Juyuan Kang, Shuqin Gao, Honglong Zhao, Tianlu Mao, Yucheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09518v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, gaussian splatting, efficient, motion, deformation, dynamic, ar  
- **[ODG: Occupancy Prediction Using Dual Gaussians](https://arxiv.org/abs/2506.09417v2)**  
  Authors: Yunxiao Shi, Yinhao Zhu, Shizhong Han, Jisoo Jeong, Amin Ansari, Hong Cai, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09417v2.pdf)  
  Keywords: real-time rendering, geometry, 3d gaussian, gaussian splatting, dynamic, semantic, autonomous driving, ar  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language
  Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: segmentation, geometry, 3d gaussian, gaussian splatting, fast, efficient, understanding, outdoor, semantic, ar  
- **[Speedy Deformable 3D Gaussian Splatting: Fast Rendering and Compression
  of Dynamic Scenes](https://arxiv.org/abs/2506.07917v1)**  
  Authors: Allen Tu, Haiyang Ying, Alex Hanson, Yonghan Lee, Tom Goldstein, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07917v1.pdf)  
  Keywords: 3d gaussian, compression, gaussian splatting, dynamic, fast, 4d, vr, motion, deformation, nerf, ar  

### Applications

*Showing the latest 50 out of 995 papers*

- **[MADrive: Memory-Augmented Driving Scene Modeling](https://arxiv.org/abs/2506.21520v1)**  
  Authors: Polina Karpikova, Daniil Selikhanovych, Kirill Struminsky, Ruslan Musaev, Maria Golitsyna, Dmitry Baranchuk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21520v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yandex-research.github.io/madrive/)  
  Keywords: relighting, 3d gaussian, gaussian splatting, lighting, autonomous driving, ar  
- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, face, 3d gaussian, gaussian splatting, 3d reconstruction, efficient, slam, motion, mapping, dynamic, ar  
- **[Geometry and Perception Guided Gaussians for Multiview-consistent 3D
  Generation from a Single Image](https://arxiv.org/abs/2506.21152v1)**  
  Authors: Pufan Li, Bi'an Du, Wei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21152v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, 3d reconstruction, fast, ar  
- **[CL-Splats: Continual Learning of Gaussian Splatting with Local
  Optimization](https://arxiv.org/abs/2506.21117v1)**  
  Authors: Jan Ackermann, Jonas Kulhanek, Shengqu Cai, Haofei Xu, Marc Pollefeys, Gordon Wetzstein, Leonidas Guibas, Songyou Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21117v1.pdf)  
  Keywords: segmentation, gaussian splatting, efficient, robotics, ar, dynamic, head  
- **[User-in-the-Loop View Sampling with Error Peaking Visualization](https://arxiv.org/abs/2506.21009v1)**  
  Authors: Ayaka Yasunaga, Hideo Saito, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21009v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar  
- **[DBMovi-GS: Dynamic View Synthesis from Blurry Monocular Video via
  Sparse-Controlled Gaussian Splatting](https://arxiv.org/abs/2506.20998v1)**  
  Authors: Yeon-Ji Song, Jaein Kim, Byung-Ju Kim, Byoung-Tak Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20998v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, motion, dynamic, ar  
- **[3DGH: 3D Head Generation with Composable Hair and Face](https://arxiv.org/abs/2506.20875v1)**  
  Authors: Chengan He, Junxuan Li, Tobias Kirschstein, Artem Sevastopolsky, Shunsuke Saito, Qingyang Tan, Javier Romero, Chen Cao, Holly Rushmeier, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20875v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://c-he.github.io/projects/3dgh/.)  
  Keywords: geometry, 3d gaussian, gaussian splatting, human, ar, face, head  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: real-time rendering, high-fidelity, gaussian splatting, efficient, ray tracing, ar  
- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: gaussian splatting, understanding, motion, deformation, dynamic, body, ar  
- **[Virtual Memory for 3D Gaussian Splatting](https://arxiv.org/abs/2506.19415v1)**  
  Authors: Jonathan Haberl, Philipp Fleck, Clemens Arth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19415v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, gaussian splatting, efficient, dynamic, ar  

### Avatar Generation

*Showing the latest 50 out of 335 papers*

- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, face, 3d gaussian, gaussian splatting, 3d reconstruction, efficient, slam, motion, mapping, dynamic, ar  
- **[CL-Splats: Continual Learning of Gaussian Splatting with Local
  Optimization](https://arxiv.org/abs/2506.21117v1)**  
  Authors: Jan Ackermann, Jonas Kulhanek, Shengqu Cai, Haofei Xu, Marc Pollefeys, Gordon Wetzstein, Leonidas Guibas, Songyou Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21117v1.pdf)  
  Keywords: segmentation, gaussian splatting, efficient, robotics, ar, dynamic, head  
- **[3DGH: 3D Head Generation with Composable Hair and Face](https://arxiv.org/abs/2506.20875v1)**  
  Authors: Chengan He, Junxuan Li, Tobias Kirschstein, Artem Sevastopolsky, Shunsuke Saito, Qingyang Tan, Javier Romero, Chen Cao, Holly Rushmeier, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20875v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://c-he.github.io/projects/3dgh/.)  
  Keywords: geometry, 3d gaussian, gaussian splatting, human, ar, face, head  
- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: gaussian splatting, understanding, motion, deformation, dynamic, body, ar  
- **[HoliGS: Holistic Gaussian Splatting for Embodied View Synthesis](https://arxiv.org/abs/2506.19291v1)**  
  Authors: Xiaoyuan Wang, Yizhou Zhao, Botao Ye, Xiaojun Shan, Weijie Lyu, Lu Qi, Kelvin C. K. Chan, Yinxiao Li, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19291v1.pdf)  
  Keywords: gaussian splatting, dynamic, 4d, ar, deformation, nerf, head  
- **[3D Arena: An Open Platform for Generative 3D Evaluation](https://arxiv.org/abs/2506.18787v1)**  
  Authors: Dylan Ebert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18787v1.pdf)  
  Keywords: understanding, human, ar  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: face, 3d gaussian, high-fidelity, gaussian splatting, dynamic, efficient, outdoor, nerf, autonomous driving, survey, ar  
- **[Information-computation trade-offs in non-linear transforms](https://arxiv.org/abs/2506.15948v1)**  
  Authors: Connor Ding, Abhiram Rao Gorle, Jiwon Jeong, Naomi Sagan, Tsachy Weissman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15948v1.pdf)  
  Keywords: compression, gaussian splatting, efficient, compact, human, dynamic, ar  
- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads
  Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: face, high-fidelity, gaussian splatting, efficient, ar, dynamic, head  
- **[3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D
  Gaussian-Splatting](https://arxiv.org/abs/2506.14642v1)**  
  Authors: Yuke Xing, Jiarui Wang, Peizhi Niu, Wenjie Huang, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14642v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, compression, gaussian splatting, human, ar  

### Dynamic Scene

*Showing the latest 50 out of 383 papers*

- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, face, 3d gaussian, gaussian splatting, 3d reconstruction, efficient, slam, motion, mapping, dynamic, ar  
- **[CL-Splats: Continual Learning of Gaussian Splatting with Local
  Optimization](https://arxiv.org/abs/2506.21117v1)**  
  Authors: Jan Ackermann, Jonas Kulhanek, Shengqu Cai, Haofei Xu, Marc Pollefeys, Gordon Wetzstein, Leonidas Guibas, Songyou Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21117v1.pdf)  
  Keywords: segmentation, gaussian splatting, efficient, robotics, ar, dynamic, head  
- **[DBMovi-GS: Dynamic View Synthesis from Blurry Monocular Video via
  Sparse-Controlled Gaussian Splatting](https://arxiv.org/abs/2506.20998v1)**  
  Authors: Yeon-Ji Song, Jaein Kim, Byung-Ju Kim, Byoung-Tak Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20998v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, motion, dynamic, ar  
- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: gaussian splatting, understanding, motion, deformation, dynamic, body, ar  
- **[Virtual Memory for 3D Gaussian Splatting](https://arxiv.org/abs/2506.19415v1)**  
  Authors: Jonathan Haberl, Philipp Fleck, Clemens Arth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19415v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, gaussian splatting, efficient, dynamic, ar  
- **[HoliGS: Holistic Gaussian Splatting for Embodied View Synthesis](https://arxiv.org/abs/2506.19291v1)**  
  Authors: Xiaoyuan Wang, Yizhou Zhao, Botao Ye, Xiaojun Shan, Weijie Lyu, Lu Qi, Kelvin C. K. Chan, Yinxiao Li, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19291v1.pdf)  
  Keywords: gaussian splatting, dynamic, 4d, ar, deformation, nerf, head  
- **[ViDAR: Video Diffusion-Aware 4D Reconstruction From Monocular Inputs](https://arxiv.org/abs/2506.18792v1)**  
  Authors: Michal Nazarczuk, Sibi Catley-Chandar, Thomas Tanay, Zhensong Zhang, Gregory Slabaugh, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18792v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vidar-4d.github.io)  
  Keywords: geometry, gaussian splatting, 4d, motion, dynamic, ar  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: face, 3d gaussian, high-fidelity, gaussian splatting, dynamic, efficient, outdoor, nerf, autonomous driving, survey, ar  
- **[Information-computation trade-offs in non-linear transforms](https://arxiv.org/abs/2506.15948v1)**  
  Authors: Connor Ding, Abhiram Rao Gorle, Jiwon Jeong, Naomi Sagan, Tsachy Weissman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15948v1.pdf)  
  Keywords: compression, gaussian splatting, efficient, compact, human, dynamic, ar  
- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from
  RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: gaussian splatting, sparse-view, motion, dynamic, ar  

### Few-shot

*Showing the latest 50 out of 75 papers*

- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from
  RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: gaussian splatting, sparse-view, motion, dynamic, ar  
- **[PointGS: Point Attention-Aware Sparse View Synthesis with Gaussian
  Splatting](https://arxiv.org/abs/2506.10335v1)**  
  Authors: Lintao Xiang, Hongpei Zheng, Yating Huang, Qijun Yang, Hujun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.10335v1.pdf)  
  Keywords: lightweight, 3d gaussian, gaussian splatting, few-shot, nerf, sparse view, ar  
- **[UniForward: Unified 3D Scene and Semantic Field Reconstruction via
  Feed-Forward Gaussian Splatting from Only Sparse-View Images](https://arxiv.org/abs/2506.09378v1)**  
  Authors: Qijian Tian, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09378v1.pdf)  
  Keywords: segmentation, 3d gaussian, gaussian splatting, sparse-view, understanding, semantic, ar  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline
  Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, sparse view, ar  
- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade
  Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, sparse-view, efficient, nerf, ar  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, sparse-view, motion, face, ar  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian
  Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: gaussian splatting, sparse-view, 3d reconstruction, fast, motion, face, ar  
- **[Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse
  Views by Jointly Training Hemisphere Sampled Synthetic Images](https://arxiv.org/abs/2505.19264v1)**  
  Authors: Guangan Chen, Anh Minh Truong, Hanhe Lin, Michiel Vlaminck, Wilfried Philips, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19264v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, sparse-view, motion, sparse view, ar  
- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane
  Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: ar, gaussian splatting, sparse-view, 3d reconstruction, compact, efficient, 4d, motion, deformation, dynamic, head  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater
  Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, sparse-view, robotics, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 314 papers*

- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, face, 3d gaussian, gaussian splatting, 3d reconstruction, efficient, slam, motion, mapping, dynamic, ar  
- **[Geometry and Perception Guided Gaussians for Multiview-consistent 3D
  Generation from a Single Image](https://arxiv.org/abs/2506.21152v1)**  
  Authors: Pufan Li, Bi'an Du, Wei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21152v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, 3d reconstruction, fast, ar  
- **[DBMovi-GS: Dynamic View Synthesis from Blurry Monocular Video via
  Sparse-Controlled Gaussian Splatting](https://arxiv.org/abs/2506.20998v1)**  
  Authors: Yeon-Ji Song, Jaein Kim, Byung-Ju Kim, Byoung-Tak Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20998v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, motion, dynamic, ar  
- **[3DGH: 3D Head Generation with Composable Hair and Face](https://arxiv.org/abs/2506.20875v1)**  
  Authors: Chengan He, Junxuan Li, Tobias Kirschstein, Artem Sevastopolsky, Shunsuke Saito, Qingyang Tan, Javier Romero, Chen Cao, Holly Rushmeier, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20875v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://c-he.github.io/projects/3dgh/.)  
  Keywords: geometry, 3d gaussian, gaussian splatting, human, ar, face, head  
- **[ViDAR: Video Diffusion-Aware 4D Reconstruction From Monocular Inputs](https://arxiv.org/abs/2506.18792v1)**  
  Authors: Michal Nazarczuk, Sibi Catley-Chandar, Thomas Tanay, Zhensong Zhang, Gregory Slabaugh, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18792v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vidar-4d.github.io)  
  Keywords: geometry, gaussian splatting, 4d, motion, dynamic, ar  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, autonomous driving, 3d reconstruction, robotics, vr, nerf, neural rendering, survey, ar  
- **[RA-NeRF: Robust Neural Radiance Field Reconstruction with Accurate
  Camera Pose Estimation under Complex Trajectories](https://arxiv.org/abs/2506.15242v2)**  
  Authors: Qingsong Yan, Qiang Wang, Kaiyong Zhao, Jie Chen, Bo Li, Xiaowen Chu, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15242v2.pdf)  
  Keywords: localization, 3d gaussian, gaussian splatting, 3d reconstruction, slam, nerf, ar  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty
  Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: lightweight, 3d gaussian, gaussian splatting, 3d reconstruction, efficient, ar, mapping, nerf, neural rendering, head  
- **[HRGS: Hierarchical Gaussian Splatting for Memory-Efficient
  High-Resolution 3D Reconstruction](https://arxiv.org/abs/2506.14229v1)**  
  Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Juan Zhang, Tongfei Chen, Shuo Yang, Shuwei Shao, Wenhao Dong, Baochang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14229v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, 3d reconstruction, efficient, face, ar  
- **[GAF: Gaussian Action Field as a Dynamic World Model for Robotic
  Manipulation](https://arxiv.org/abs/2506.14135v2)**  
  Authors: Ying Chai, Litao Deng, Ruizhi Shao, Jiajun Zhang, Liangjun Xing, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14135v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://chaiying1.github.io/GAF.github.io/project_page/)  
  Keywords: geometry, 3d gaussian, gaussian splatting, 4d, motion, dynamic, ar  

### Large Scene

*Showing the latest 50 out of 58 papers*

- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, slam, outdoor, tracking, ar  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: face, 3d gaussian, high-fidelity, gaussian splatting, dynamic, efficient, outdoor, nerf, autonomous driving, survey, ar  
- **[Multiview Geometric Regularization of Gaussian Splatting for Accurate
  Radiance Fields](https://arxiv.org/abs/2506.13508v1)**  
  Authors: Jungeon Kim, Geonsoo Park, Seungyong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13508v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, outdoor, ar  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language
  Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: segmentation, geometry, 3d gaussian, gaussian splatting, fast, efficient, understanding, outdoor, semantic, ar  
- **[TraGraph-GS: Trajectory Graph-based Gaussian Splatting for Arbitrary
  Large-Scale Scene Rendering](https://arxiv.org/abs/2506.08704v1)**  
  Authors: Xiaohan Zhang, Sitong Wang, Yushen Yan, Yi Yang, Mingda Xu, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08704v1.pdf)  
  Keywords: gaussian splatting, large scene, ar  
- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from
  Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: 3d gaussian, large scene, gaussian splatting, fast, efficient, slam, motion, ar  
- **[Photoreal Scene Reconstruction from an Egocentric Device](https://arxiv.org/abs/2506.04444v1)**  
  Authors: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04444v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.projectaria.com/photoreal-reconstruction/)  
  Keywords: gaussian splatting, outdoor, dynamic, lighting, ar  
- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient
  Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, gaussian splatting, dynamic, efficient, outdoor, ar, nerf, head  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings
  and Residual Gaussians](https://arxiv.org/abs/2505.21041v3)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v3.pdf)  
  Keywords: lightweight, real-time rendering, geometry, 3d gaussian, urban scene, gaussian splatting, compact, efficient, ar  
- **[VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale
  Scenes](https://arxiv.org/abs/2505.18992v1)**  
  Authors: Tianchen Deng, Wenhua Wu, Junjie He, Yue Pan, Xirui Jiang, Shenghai Yuan, Danwei Wang, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18992v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, compact, slam, outdoor, mapping, tracking, ar  

### Model Compression

*Showing the latest 50 out of 392 papers*

- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, face, 3d gaussian, gaussian splatting, 3d reconstruction, efficient, slam, motion, mapping, dynamic, ar  
- **[CL-Splats: Continual Learning of Gaussian Splatting with Local
  Optimization](https://arxiv.org/abs/2506.21117v1)**  
  Authors: Jan Ackermann, Jonas Kulhanek, Shengqu Cai, Haofei Xu, Marc Pollefeys, Gordon Wetzstein, Leonidas Guibas, Songyou Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21117v1.pdf)  
  Keywords: segmentation, gaussian splatting, efficient, robotics, ar, dynamic, head  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: real-time rendering, high-fidelity, gaussian splatting, efficient, ray tracing, ar  
- **[Virtual Memory for 3D Gaussian Splatting](https://arxiv.org/abs/2506.19415v1)**  
  Authors: Jonathan Haberl, Philipp Fleck, Clemens Arth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19415v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, gaussian splatting, efficient, dynamic, ar  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: face, 3d gaussian, high-fidelity, gaussian splatting, dynamic, efficient, outdoor, nerf, autonomous driving, survey, ar  
- **[Information-computation trade-offs in non-linear transforms](https://arxiv.org/abs/2506.15948v1)**  
  Authors: Connor Ding, Abhiram Rao Gorle, Jiwon Jeong, Naomi Sagan, Tsachy Weissman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15948v1.pdf)  
  Keywords: compression, gaussian splatting, efficient, compact, human, dynamic, ar  
- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads
  Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: face, high-fidelity, gaussian splatting, efficient, ar, dynamic, head  
- **[3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D
  Gaussian-Splatting](https://arxiv.org/abs/2506.14642v1)**  
  Authors: Yuke Xing, Jiarui Wang, Peizhi Niu, Wenjie Huang, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14642v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, compression, gaussian splatting, human, ar  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty
  Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: lightweight, 3d gaussian, gaussian splatting, 3d reconstruction, efficient, ar, mapping, nerf, neural rendering, head  
- **[HRGS: Hierarchical Gaussian Splatting for Memory-Efficient
  High-Resolution 3D Reconstruction](https://arxiv.org/abs/2506.14229v1)**  
  Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Juan Zhang, Tongfei Chen, Shuo Yang, Shuwei Shao, Wenhao Dong, Baochang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14229v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, 3d reconstruction, efficient, face, ar  

### Quality Enhancement

*Showing the latest 50 out of 162 papers*

- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: real-time rendering, high-fidelity, gaussian splatting, efficient, ray tracing, ar  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: face, 3d gaussian, high-fidelity, gaussian splatting, dynamic, efficient, outdoor, nerf, autonomous driving, survey, ar  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, autonomous driving, 3d reconstruction, robotics, vr, nerf, neural rendering, survey, ar  
- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads
  Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: face, high-fidelity, gaussian splatting, efficient, ar, dynamic, head  
- **[PF-LHM: 3D Animatable Avatar Reconstruction from Pose-free Articulated
  Human Images](https://arxiv.org/abs/2506.13766v1)**  
  Authors: Lingteng Qiu, Peihao Li, Qi Zuo, Xiaodong Gu, Yuan Dong, Weihao Yuan, Siyu Zhu, Xiaoguang Han, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13766v1.pdf)  
  Keywords: geometry, 3d gaussian, high-fidelity, efficient, human, avatar, ar  
- **[GaussianVAE: Adaptive Learning Dynamics of 3D Gaussians for
  High-Fidelity Super-Resolution](https://arxiv.org/abs/2506.07897v1)**  
  Authors: Shuja Khalid, Mohamed Ibrahim, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07897v1.pdf)  
  Keywords: lightweight, 3d gaussian, high-fidelity, gaussian splatting, dynamic, ar  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline
  Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, sparse view, ar  
- **[Parametric Gaussian Human Model: Generalizable Prior for Efficient and
  Realistic Human Avatar Modeling](https://arxiv.org/abs/2506.06645v1)**  
  Authors: Cheng Peng, Jingxiang Sun, Yushuo Chen, Zhaoqi Su, Zhuo Su, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06645v1.pdf)  
  Keywords: geometry, 3d gaussian, high-fidelity, ar, gaussian splatting, fast, compact, efficient, human, avatar, face, head  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for
  Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: geometry, 3d gaussian, high-fidelity, gaussian splatting, 3d reconstruction, efficient, motion, lighting, ar  
- **[ODE-GS: Latent ODEs for Dynamic Scene Extrapolation with 3D Gaussian
  Splatting](https://arxiv.org/abs/2506.05480v1)**  
  Authors: Daniel Wang, Patrick Rim, Tian Tian, Alex Wong, Ganesh Sundaramoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05480v1.pdf)  
  Keywords: lightweight, 3d gaussian, high-fidelity, gaussian splatting, dynamic, deformation, nerf, neural rendering, ar  

### Ray Tracing

- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: real-time rendering, high-fidelity, gaussian splatting, efficient, ray tracing, ar  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: relighting, geometry, gaussian splatting, relightable, fast, human, ray tracing, avatar, shadow, lighting, ar  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: relighting, 3d gaussian, gaussian splatting, efficient, efficient rendering, ray tracing, acceleration, lighting, ar  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, dynamic, animation, ray marching, compact, efficient, acceleration, ar  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: global illumination, real-time rendering, illumination, 3d gaussian, gaussian splatting, efficient, ray tracing, face, lighting, ar  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: reflection, 3d gaussian, gaussian splatting, fast, ray tracing, shadow, neural rendering, ar  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: reflection, face, gaussian splatting, ray tracing, shadow, lighting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation
  Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ray tracing, survey, ar  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: reflection, gaussian splatting, efficient, ray tracing, light transport, acceleration, ar  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: reflection, 3d gaussian, gaussian splatting, ray tracing, shadow, ar  

### Relighting

*Showing the latest 50 out of 107 papers*

- **[MADrive: Memory-Augmented Driving Scene Modeling](https://arxiv.org/abs/2506.21520v1)**  
  Authors: Polina Karpikova, Daniil Selikhanovych, Kirill Struminsky, Ruslan Musaev, Maria Golitsyna, Dmitry Baranchuk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21520v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yandex-research.github.io/madrive/)  
  Keywords: relighting, 3d gaussian, gaussian splatting, lighting, autonomous driving, ar  
- **[Micro-macro Gaussian Splatting with Enhanced Scalability for
  Unconstrained Scene Reconstruction](https://arxiv.org/abs/2506.13516v1)**  
  Authors: Yihui Li, Chengxin Lv, Hongyu Yang, Di Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13516v1.pdf)  
  Keywords: illumination, gaussian splatting, 3d reconstruction, motion, ar  
- **[GS-2DGS: Geometrically Supervised 2DGS for Reflective Object
  Reconstruction](https://arxiv.org/abs/2506.13110v1)**  
  Authors: Jinguang Tong, Xuesong li, Fahira Afzal Maken, Sundaram Muthu, Lars Petersson, Chuong Nguyen, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13110v1.pdf)  
  Keywords: real-time rendering, relighting, 3d gaussian, gaussian splatting, fast, face, lighting, ar  
- **[Efficient multi-view training for 3D Gaussian Splatting](https://arxiv.org/abs/2506.12727v2)**  
  Authors: Minhyuk Choi, Injae Kim, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12727v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, efficient, ar, nerf, lighting, head  
- **[R3D2: Realistic 3D Asset Insertion via Diffusion for Autonomous Driving
  Simulation](https://arxiv.org/abs/2506.07826v1)**  
  Authors: William Ljungbergh, Bernardo Taveira, Wenzhao Zheng, Adam Tonderski, Chensheng Peng, Fredrik Kahl, Christoffer Petersson, Michael Felsberg, Kurt Keutzer, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07826v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/R3D2/.)  
  Keywords: lightweight, illumination, 3d gaussian, gaussian splatting, dynamic, autonomous driving, shadow, lighting, neural rendering, ar  
- **[SPC to 3D: Novel View Synthesis from Binary SPC via I2I translation](https://arxiv.org/abs/2506.06890v1)**  
  Authors: Sumit Sharma, Gopi Raju Matta, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06890v1.pdf)  
  Keywords: illumination, gaussian splatting, 3d reconstruction, nerf, ar  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for
  Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: geometry, 3d gaussian, high-fidelity, gaussian splatting, 3d reconstruction, efficient, motion, lighting, ar  
- **[Photoreal Scene Reconstruction from an Egocentric Device](https://arxiv.org/abs/2506.04444v1)**  
  Authors: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04444v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.projectaria.com/photoreal-reconstruction/)  
  Keywords: gaussian splatting, outdoor, dynamic, lighting, ar  
- **[Robust Neural Rendering in the Wild with Asymmetric Dual 3D Gaussian
  Splatting](https://arxiv.org/abs/2506.03538v1)**  
  Authors: Chengqi Li, Zhihao Shi, Yangdi Lu, Wenbo He, Xiangyu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03538v1.pdf)  
  Keywords: lightweight, geometry, 3d gaussian, gaussian splatting, 3d reconstruction, dynamic, lighting, neural rendering, ar  
- **[RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis
  and 3D Reconstruction of Autonomous Driving Scenes](https://arxiv.org/abs/2506.01379v1)**  
  Authors: Pou-Chun Kung, Skanda Harisha, Ram Vasudevan, Aline Eid, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01379v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/radarsplat.)  
  Keywords: reflection, high-fidelity, gaussian splatting, 3d reconstruction, autonomous driving, ar  

### SLAM

*Showing the latest 50 out of 157 papers*

- **[EndoFlow-SLAM: Real-Time Endoscopic SLAM with Flow-Constrained Gaussian
  Splatting](https://arxiv.org/abs/2506.21420v1)**  
  Authors: Taoyu Wu, Yiyi Miao, Zhuoxiao Li, Haocheng Zhao, Kang Dang, Jionglong Su, Limin Yu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21420v1.pdf)  
  Keywords: localization, face, 3d gaussian, gaussian splatting, 3d reconstruction, efficient, slam, motion, mapping, dynamic, ar  
- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, slam, outdoor, tracking, ar  
- **[RA-NeRF: Robust Neural Radiance Field Reconstruction with Accurate
  Camera Pose Estimation under Complex Trajectories](https://arxiv.org/abs/2506.15242v2)**  
  Authors: Qingsong Yan, Qiang Wang, Kaiyong Zhao, Jie Chen, Bo Li, Xiaowen Chu, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15242v2.pdf)  
  Keywords: localization, 3d gaussian, gaussian splatting, 3d reconstruction, slam, nerf, ar  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty
  Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: lightweight, 3d gaussian, gaussian splatting, 3d reconstruction, efficient, ar, mapping, nerf, neural rendering, head  
- **[TextureSplat: Per-Primitive Texture Mapping for Reflective Gaussian
  Splatting](https://arxiv.org/abs/2506.13348v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13348v1.pdf)  
  Keywords: mapping, gaussian splatting, face, ar  
- **[Rasterizing Wireless Radiance Field via Deformable 2D Gaussian Splatting](https://arxiv.org/abs/2506.12787v2)**  
  Authors: Mufan Liu, Cixiao Zhang, Qi Yang, Yujie Cao, Yiling Xu, Yin Xu, Shu Sun, Mingzeng Dai, Yunfeng Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12787v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://evan-sudo.github.io/swiftwrf/.)  
  Keywords: localization, lightweight, gaussian splatting, fast, compact, deformation, nerf, ar  
- **[Anti-Aliased 2D Gaussian Splatting](https://arxiv.org/abs/2506.11252v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.11252v1.pdf)  
  Keywords: gaussian splatting, efficient, mapping, face, ar  
- **[DGS-LRM: Real-Time Deformable 3D Gaussian Reconstruction From Monocular
  Videos](https://arxiv.org/abs/2506.09997v1)**  
  Authors: Chieh Hubert Lin, Zhaoyang Lv, Songyin Wu, Zhen Xu, Thu Nguyen-Phuoc, Hung-Yu Tseng, Julian Straub, Numair Khan, Lei Xiao, Ming-Hsuan Yang, Yuheng Ren, Richard Newcombe, Zhao Dong, Zhengqin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09997v1.pdf)  
  Keywords: 3d gaussian, motion, deformation, dynamic, tracking, ar  
- **[PIG: Physically-based Multi-Material Interaction with 3D Gaussians](https://arxiv.org/abs/2506.07657v1)**  
  Authors: Zeyu Xiao, Zhenyi Wu, Mingyang Sun, Qipeng Yan, Yufan Guo, Zhuoer Liang, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07657v1.pdf)  
  Keywords: segmentation, 3d gaussian, gaussian splatting, fast, mapping, deformation, dynamic, ar  
- **[Gaussian Mapping for Evolving Scenes](https://arxiv.org/abs/2506.06909v1)**  
  Authors: Vladimir Yugay, Thies Kersten, Luca Carlone, Theo Gevers, Martin R. Oswald, Lukas Schmid  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06909v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, robotics, motion, mapping, dynamic, semantic, autonomous driving, ar  

### Scene Understanding

*Showing the latest 50 out of 182 papers*

- **[CL-Splats: Continual Learning of Gaussian Splatting with Local
  Optimization](https://arxiv.org/abs/2506.21117v1)**  
  Authors: Jan Ackermann, Jonas Kulhanek, Shengqu Cai, Haofei Xu, Marc Pollefeys, Gordon Wetzstein, Leonidas Guibas, Songyou Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.21117v1.pdf)  
  Keywords: segmentation, gaussian splatting, efficient, robotics, ar, dynamic, head  
- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: gaussian splatting, understanding, motion, deformation, dynamic, body, ar  
- **[3D Arena: An Open Platform for Generative 3D Evaluation](https://arxiv.org/abs/2506.18787v1)**  
  Authors: Dylan Ebert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18787v1.pdf)  
  Keywords: understanding, human, ar  
- **[Reconstructing Tornadoes in 3D with Gaussian Splatting](https://arxiv.org/abs/2506.18677v1)**  
  Authors: Adam Yang, Nadula Kadawedduwa, Tianfu Wang, Maria Molina, Christopher Metzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18677v1.pdf)  
  Keywords: understanding, gaussian splatting, 3d gaussian, ar  
- **[SPLATART: Articulated Gaussian Splatting with Estimated Object Structure](https://arxiv.org/abs/2506.12184v1)**  
  Authors: Stanley Lewis, Vishal Chandra, Tom Gao, Odest Chadwicke Jenkins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12184v1.pdf)  
  Keywords: segmentation, geometry, gaussian splatting, robotics, ar  
- **[ODG: Occupancy Prediction Using Dual Gaussians](https://arxiv.org/abs/2506.09417v2)**  
  Authors: Yunxiao Shi, Yinhao Zhu, Shizhong Han, Jisoo Jeong, Amin Ansari, Hong Cai, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09417v2.pdf)  
  Keywords: real-time rendering, geometry, 3d gaussian, gaussian splatting, dynamic, semantic, autonomous driving, ar  
- **[UniForward: Unified 3D Scene and Semantic Field Reconstruction via
  Feed-Forward Gaussian Splatting from Only Sparse-View Images](https://arxiv.org/abs/2506.09378v1)**  
  Authors: Qijian Tian, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09378v1.pdf)  
  Keywords: segmentation, 3d gaussian, gaussian splatting, sparse-view, understanding, semantic, ar  
- **[Gaussian2Scene: 3D Scene Representation Learning via Self-supervised
  Learning with 3D Gaussian Splatting](https://arxiv.org/abs/2506.08777v2)**  
  Authors: Keyi Liu, Weidong Yang, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08777v2.pdf)  
  Keywords: understanding, gaussian splatting, 3d gaussian, ar  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language
  Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: segmentation, geometry, 3d gaussian, gaussian splatting, fast, efficient, understanding, outdoor, semantic, ar  
- **[OpenSplat3D: Open-Vocabulary 3D Instance Segmentation using Gaussian
  Splatting](https://arxiv.org/abs/2506.07697v1)**  
  Authors: Jens Piekenbrinck, Christian Schmidt, Alexander Hermans, Narunas Vaskevicius, Timm Linder, Bastian Leibe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07697v1.pdf)  
  Keywords: segmentation, 3d gaussian, gaussian splatting, understanding, semantic, ar  



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