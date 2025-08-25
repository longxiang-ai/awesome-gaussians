# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-08-25 00:54:50

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

- [3DGS Surveys](#3dgs-surveys) (20 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (263 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (322 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (391 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (74 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (310 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (73 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (406 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (161 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (18 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (114 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (151 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (196 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, compact, nerf, high-fidelity, ar, lighting, segmentation, survey, semantic  
- **[A Study of the Framework and Real-World Applications of Language
  Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: efficient, gaussian splatting, robotics, understanding, 3d gaussian, nerf, ar, survey, semantic  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned
  and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: gaussian splatting, robotics, 3d gaussian, nerf, human, ar, survey  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: gaussian splatting, robotics, sparse-view, vr, 3d gaussian, motion, nerf, geometry, 3d reconstruction, ar, survey  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v2)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v2.pdf)  
  Keywords: gaussian splatting, slam, robotics, dynamic, vr, 3d gaussian, nerf, human, 3d reconstruction, lighting, ar, fast, survey  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: efficient, gaussian splatting, dynamic, 3d gaussian, nerf, high-fidelity, ar, face, autonomous driving, outdoor, survey  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: gaussian splatting, robotics, vr, 3d gaussian, nerf, neural rendering, high-fidelity, 3d reconstruction, ar, autonomous driving, survey  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: efficient, gaussian splatting, understanding, 3d gaussian, neural rendering, high-fidelity, 3d reconstruction, ar, segmentation, outdoor, survey, semantic  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: efficient, gaussian splatting, slam, mapping, 3d gaussian, localization, nerf, ar, segmentation, survey, semantic  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to
  Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: gaussian splatting, dynamic, understanding, 3d gaussian, motion, body, ar, 4d, survey  

### Acceleration

*Showing the latest 50 out of 263 papers*

- **[Image-Conditioned 3D Gaussian Splat Quantization](https://arxiv.org/abs/2508.15372v1)**  
  Authors: Xinshuang Liu, Runfa Blark Li, Keito Suzuki, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15372v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, 3d gaussian, head, compression, ar  
- **[EAvatar: Expression-Aware Head Avatar Reconstruction with Generative
  Geometry Priors](https://arxiv.org/abs/2508.13537v1)**  
  Authors: Shikun Zhang, Cunjian Chen, Yiqun Wang, Qiuhong Ke, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13537v1.pdf)  
  Keywords: gaussian splatting, avatar, deformation, real-time rendering, vr, 3d gaussian, geometry, high-fidelity, head, ar, face  
- **[Improving Densification in 3D Gaussian Splatting for High-Fidelity
  Rendering](https://arxiv.org/abs/2508.12313v1)**  
  Authors: Xiaobin Deng, Changyu Diao, Min Li, Ruohan Yu, Duanqing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12313v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, 3d gaussian, high-fidelity, head, ar  
- **[Multi-Sample Anti-Aliasing and Constrained Optimization for 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.10507v1)**  
  Authors: Zheng Zhou, Jia-Chen Zhang, Yu-Jie Xiong, Chun-Ming Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.10507v1.pdf)  
  Keywords: gaussian splatting, dynamic, real-time rendering, 3d gaussian, ar  
- **[EntropyGS: An Efficient Entropy Coding on 3D Gaussian Splatting](https://arxiv.org/abs/2508.10227v1)**  
  Authors: Yuning Huang, Jiahao Pang, Fengqing Zhu, Dong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.10227v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, compression, ar, fast  
- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event
  Cameras](https://arxiv.org/abs/2508.09912v1)**  
  Authors: Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09912v1.pdf)  
  Keywords: gaussian splatting, dynamic, motion, high-fidelity, ar, lighting, 4d, fast  
- **[SAGOnline: Segment Any Gaussians Online](https://arxiv.org/abs/2508.08219v1)**  
  Authors: Wentao Sun, Quanyun Wu, Hanqing Xu, Kyle Gao, Zhengsen Xu, Yiping Chen, Dedong Zhang, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08219v1.pdf)  
  Keywords: efficient, gaussian splatting, understanding, real-time rendering, vr, 3d gaussian, nerf, lightweight, ar, segmentation, tracking  
- **[DIP-GS: Deep Image Prior For Gaussian Splatting Sparse View Recovery](https://arxiv.org/abs/2508.07372v1)**  
  Authors: Rajaei Khatib, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07372v1.pdf)  
  Keywords: gaussian splatting, sparse-view, real-time rendering, 3d gaussian, sparse view, ar  
- **[ExploreGS: Explorable 3D Scene Reconstruction with Virtual Camera
  Samplings and Diffusion Priors](https://arxiv.org/abs/2508.06014v1)**  
  Authors: Minsu Kim, Subin Jeon, In Cho, Mijin Yoo, Seon Joo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06014v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://exploregs.github.io)  
  Keywords: 3d gaussian, gaussian splatting, ar, real-time rendering  
- **[Optimization-Free Style Transfer for 3D Gaussian Splats](https://arxiv.org/abs/2508.05813v1)**  
  Authors: Raphael Du Sablon, David Hart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05813v1.pdf)  
  Keywords: 3d gaussian, fast, ar, face  

### Applications

*Showing the latest 50 out of 995 papers*

- **[Enhancing Novel View Synthesis from extremely sparse views with SfM-free
  3D Gaussian Splatting Framework](https://arxiv.org/abs/2508.15457v1)**  
  Authors: Zongqi He, Hanmin Li, Kin-Chung Chan, Yushen Zuo, Hao Xie, Zhe Xiao, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15457v1.pdf)  
  Keywords: gaussian splatting, sparse-view, 3d gaussian, motion, geometry, sparse view, ar  
- **[DriveSplat: Decoupled Driving Scene Reconstruction with
  Geometry-enhanced Partitioned Neural Gaussians](https://arxiv.org/abs/2508.15376v1)**  
  Authors: Cong Wang, Xianda Guo, Wenbo Xu, Wei Tian, Ruiqi Song, Chenming Zhang, Lingxi Li, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15376v1.pdf)  
  Keywords: gaussian splatting, dynamic, deformation, 3d gaussian, motion, geometry, ar  
- **[Image-Conditioned 3D Gaussian Splat Quantization](https://arxiv.org/abs/2508.15372v1)**  
  Authors: Xinshuang Liu, Runfa Blark Li, Keito Suzuki, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15372v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, 3d gaussian, head, compression, ar  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v1)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, sparse view, lighting, face, autonomous driving, ar, outdoor, relighting  
- **[Zero-shot Volumetric CT Super-Resolution using 3D Gaussian Splatting
  with Upsampled 2D X-ray Projection Priors](https://arxiv.org/abs/2508.15151v1)**  
  Authors: Jeonghyun Noh, Hyun-Jic Oh, Byungju Chae, Won-Ki Jeong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15151v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar  
- **[GSFix3D: Diffusion-Guided Repair of Novel Views in Gaussian Splatting](https://arxiv.org/abs/2508.14717v1)**  
  Authors: Jiaxin Wei, Stefan Leutenegger, Simon Schaefer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14717v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsfix3d.github.io.)  
  Keywords: 3d gaussian, ar, gaussian splatting, 3d reconstruction  
- **[GeMS: Efficient Gaussian Splatting for Extreme Motion Blur](https://arxiv.org/abs/2508.14682v1)**  
  Authors: Gopi Raju Matta, Trisha Reddypalli, Vemunuri Divya Madhuri, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14682v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, motion, ar  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, geometry, high-fidelity, ray tracing, lighting, face, ar, illumination, reflection, relighting  
- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, compact, motion, geometry, 3d reconstruction, ar, tracking  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, outdoor, 3d reconstruction, lighting, ar, illumination  

### Avatar Generation

*Showing the latest 50 out of 322 papers*

- **[Image-Conditioned 3D Gaussian Splat Quantization](https://arxiv.org/abs/2508.15372v1)**  
  Authors: Xinshuang Liu, Runfa Blark Li, Keito Suzuki, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15372v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, 3d gaussian, head, compression, ar  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v1)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, sparse view, lighting, face, autonomous driving, ar, outdoor, relighting  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, geometry, high-fidelity, ray tracing, lighting, face, ar, illumination, reflection, relighting  
- **[PhysGM: Large Physical Gaussian Model for Feed-Forward 4D Synthesis](https://arxiv.org/abs/2508.13911v1)**  
  Authors: Chunji Lv, Zequn Chen, Donglin Di, Weinan Zhang, Hao Li, Wei Chen, Changsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13911v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hihixiaolv.github.io/PhysGM.github.io/)  
  Keywords: gaussian splatting, 3d gaussian, motion, high-fidelity, ar, face, 4d  
- **[EAvatar: Expression-Aware Head Avatar Reconstruction with Generative
  Geometry Priors](https://arxiv.org/abs/2508.13537v1)**  
  Authors: Shikun Zhang, Cunjian Chen, Yiqun Wang, Qiuhong Ke, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13537v1.pdf)  
  Keywords: gaussian splatting, avatar, deformation, real-time rendering, vr, 3d gaussian, geometry, high-fidelity, head, ar, face  
- **[InnerGS: Internal Scenes Rendering via Factorized 3D Gaussian Splatting](https://arxiv.org/abs/2508.13287v1)**  
  Authors: Shuxin Liang, Yihan Xiao, Wenlu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13287v1.pdf)  
  Keywords: efficient, gaussian splatting, understanding, 3d gaussian, ar, face  
- **[IntelliCap: Intelligent Guidance for Consistent View Sampling](https://arxiv.org/abs/2508.13043v1)**  
  Authors: Ayaka Yasunaga, Hideo Saito, Dieter Schmalstieg, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13043v1.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, human, ar, segmentation, semantic  
- **[Improving Densification in 3D Gaussian Splatting for High-Fidelity
  Rendering](https://arxiv.org/abs/2508.12313v1)**  
  Authors: Xiaobin Deng, Changyu Diao, Min Li, Ruohan Yu, Duanqing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12313v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, 3d gaussian, high-fidelity, head, ar  
- **[Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.11431v1)**  
  Authors: Simona Kocour, Assia Benbihi, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11431v1.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, geometry, 3d reconstruction, ar, face, outdoor, semantic  
- **[HumanGenesis: Agent-Based Geometric and Generative Modeling for
  Synthetic Human Dynamics](https://arxiv.org/abs/2508.09858v1)**  
  Authors: Weiqi Li, Zehao Zhang, Liang Lin, Guangrun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09858v1.pdf)  
  Keywords: gaussian splatting, dynamic, deformation, 3d gaussian, motion, human, ar, face, 4d, reflection  

### Dynamic Scene

*Showing the latest 50 out of 391 papers*

- **[Enhancing Novel View Synthesis from extremely sparse views with SfM-free
  3D Gaussian Splatting Framework](https://arxiv.org/abs/2508.15457v1)**  
  Authors: Zongqi He, Hanmin Li, Kin-Chung Chan, Yushen Zuo, Hao Xie, Zhe Xiao, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15457v1.pdf)  
  Keywords: gaussian splatting, sparse-view, 3d gaussian, motion, geometry, sparse view, ar  
- **[DriveSplat: Decoupled Driving Scene Reconstruction with
  Geometry-enhanced Partitioned Neural Gaussians](https://arxiv.org/abs/2508.15376v1)**  
  Authors: Cong Wang, Xianda Guo, Wenbo Xu, Wei Tian, Ruiqi Song, Chenming Zhang, Lingxi Li, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15376v1.pdf)  
  Keywords: gaussian splatting, dynamic, deformation, 3d gaussian, motion, geometry, ar  
- **[GeMS: Efficient Gaussian Splatting for Extreme Motion Blur](https://arxiv.org/abs/2508.14682v1)**  
  Authors: Gopi Raju Matta, Trisha Reddypalli, Vemunuri Divya Madhuri, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14682v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, motion, ar  
- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, compact, motion, geometry, 3d reconstruction, ar, tracking  
- **[LongSplat: Robust Unposed 3D Gaussian Splatting for Casual Long Videos](https://arxiv.org/abs/2508.14041v1)**  
  Authors: Chin-Yang Lin, Cheng Sun, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14041v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://linjohnss.github.io/longsplat/)  
  Keywords: efficient, gaussian splatting, 3d gaussian, motion, geometry, ar  
- **[PhysGM: Large Physical Gaussian Model for Feed-Forward 4D Synthesis](https://arxiv.org/abs/2508.13911v1)**  
  Authors: Chunji Lv, Zequn Chen, Donglin Di, Weinan Zhang, Hao Li, Wei Chen, Changsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13911v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hihixiaolv.github.io/PhysGM.github.io/)  
  Keywords: gaussian splatting, 3d gaussian, motion, high-fidelity, ar, face, 4d  
- **[EAvatar: Expression-Aware Head Avatar Reconstruction with Generative
  Geometry Priors](https://arxiv.org/abs/2508.13537v1)**  
  Authors: Shikun Zhang, Cunjian Chen, Yiqun Wang, Qiuhong Ke, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13537v1.pdf)  
  Keywords: gaussian splatting, avatar, deformation, real-time rendering, vr, 3d gaussian, geometry, high-fidelity, head, ar, face  
- **[TiP4GEN: Text to Immersive Panorama 4D Scene Generation](https://arxiv.org/abs/2508.12415v2)**  
  Authors: Ke Xing, Hanwen Liang, Dejia Xu, Yuyang Yin, Konstantinos N. Plataniotis, Yao Zhao, Yunchao Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12415v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ke-xing.github.io/TiP4GEN/.)  
  Keywords: gaussian splatting, dynamic, vr, 3d gaussian, motion, geometry, ar, 4d  
- **[InstDrive: Instance-Aware 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2508.12015v1)**  
  Authors: Hongyuan Liu, Haochen Yu, Jianfei Jiang, Qiankun Liu, Jiansheng Chen, Huimin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12015v1.pdf)  
  Keywords: gaussian splatting, dynamic, understanding, 3d gaussian, lightweight, autonomous driving, ar, segmentation, outdoor  
- **[Versatile Video Tokenization with Generative 2D Gaussian Splatting](https://arxiv.org/abs/2508.11183v1)**  
  Authors: Zhenghao Chen, Zicong Chen, Lei Liu, Yiming Wu, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11183v1.pdf)  
  Keywords: gaussian splatting, dynamic, compact, recognition, compression, ar  

### Few-shot

*Showing the latest 50 out of 74 papers*

- **[Enhancing Novel View Synthesis from extremely sparse views with SfM-free
  3D Gaussian Splatting Framework](https://arxiv.org/abs/2508.15457v1)**  
  Authors: Zongqi He, Hanmin Li, Kin-Chung Chan, Yushen Zuo, Hao Xie, Zhe Xiao, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15457v1.pdf)  
  Keywords: gaussian splatting, sparse-view, 3d gaussian, motion, geometry, sparse view, ar  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v1)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, sparse view, lighting, face, autonomous driving, ar, outdoor, relighting  
- **[Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.12720v1)**  
  Authors: Kangjie Chen, Yingji Zhong, Zhihao Li, Jiaqi Lin, Youyu Chen, Minghan Qin, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12720v1.pdf)  
  Keywords: gaussian splatting, sparse-view, understanding, 3d gaussian, lightweight, ar  
- **[Toward Human-Robot Teaming: Learning Handover Behaviors from 3D Scenes](https://arxiv.org/abs/2508.09855v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09855v1.pdf)  
  Keywords: human, gaussian splatting, sparse-view, ar  
- **[GSFixer: Improving 3D Gaussian Splatting with Reference-Guided Video
  Diffusion Priors](https://arxiv.org/abs/2508.09667v1)**  
  Authors: Xingyilang Yin, Qi Zhang, Jiahao Chang, Ying Feng, Qingnan Fan, Xi Yang, Chi-Man Pun, Huaqi Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09667v1.pdf)  
  Keywords: gaussian splatting, sparse-view, 3d gaussian, geometry, sparse view, 3d reconstruction, ar, semantic  
- **[SkySplat: Generalizable 3D Gaussian Splatting from Multi-Temporal Sparse
  Satellite Images](https://arxiv.org/abs/2508.09479v1)**  
  Authors: Xuejun Huang, Xinyi Liu, Yi Wan, Zhi Zheng, Bin Zhang, Mingtao Xiong, Yingying Pei, Yongjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09479v1.pdf)  
  Keywords: efficient, gaussian splatting, sparse-view, 3d gaussian, ar  
- **[DIP-GS: Deep Image Prior For Gaussian Splatting Sparse View Recovery](https://arxiv.org/abs/2508.07372v1)**  
  Authors: Rajaei Khatib, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07372v1.pdf)  
  Keywords: gaussian splatting, sparse-view, real-time rendering, 3d gaussian, sparse view, ar  
- **[UGOD: Uncertainty-Guided Differentiable Opacity and Soft Dropout for
  Enhanced Sparse-View 3DGS](https://arxiv.org/abs/2508.04968v1)**  
  Authors: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Liangxiu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04968v1.pdf)  
  Keywords: gaussian splatting, sparse-view, 3d gaussian, nerf, ar  
- **[DET-GS: Depth- and Edge-Aware Regularization for High-Fidelity 3D
  Gaussian Splatting](https://arxiv.org/abs/2508.04099v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04099v1.pdf)  
  Keywords: efficient, gaussian splatting, sparse-view, 3d gaussian, high-fidelity, ar, semantic  
- **[GR-Gaussian: Graph-Based Radiative Gaussian Splatting for Sparse-View CT
  Reconstruction](https://arxiv.org/abs/2508.02408v2)**  
  Authors: Yikuang Yuluo, Yue Ma, Kuan Shen, Tongtong Jin, Wang Liao, Yangpu Ma, Fuquan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.02408v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, sparse-view, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 310 papers*

- **[Enhancing Novel View Synthesis from extremely sparse views with SfM-free
  3D Gaussian Splatting Framework](https://arxiv.org/abs/2508.15457v1)**  
  Authors: Zongqi He, Hanmin Li, Kin-Chung Chan, Yushen Zuo, Hao Xie, Zhe Xiao, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15457v1.pdf)  
  Keywords: gaussian splatting, sparse-view, 3d gaussian, motion, geometry, sparse view, ar  
- **[DriveSplat: Decoupled Driving Scene Reconstruction with
  Geometry-enhanced Partitioned Neural Gaussians](https://arxiv.org/abs/2508.15376v1)**  
  Authors: Cong Wang, Xianda Guo, Wenbo Xu, Wei Tian, Ruiqi Song, Chenming Zhang, Lingxi Li, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15376v1.pdf)  
  Keywords: gaussian splatting, dynamic, deformation, 3d gaussian, motion, geometry, ar  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v1)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, sparse view, lighting, face, autonomous driving, ar, outdoor, relighting  
- **[GSFix3D: Diffusion-Guided Repair of Novel Views in Gaussian Splatting](https://arxiv.org/abs/2508.14717v1)**  
  Authors: Jiaxin Wei, Stefan Leutenegger, Simon Schaefer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14717v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsfix3d.github.io.)  
  Keywords: 3d gaussian, ar, gaussian splatting, 3d reconstruction  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, geometry, high-fidelity, ray tracing, lighting, face, ar, illumination, reflection, relighting  
- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, compact, motion, geometry, 3d reconstruction, ar, tracking  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, outdoor, 3d reconstruction, lighting, ar, illumination  
- **[LongSplat: Robust Unposed 3D Gaussian Splatting for Casual Long Videos](https://arxiv.org/abs/2508.14041v1)**  
  Authors: Chin-Yang Lin, Cheng Sun, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14041v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://linjohnss.github.io/longsplat/)  
  Keywords: efficient, gaussian splatting, 3d gaussian, motion, geometry, ar  
- **[EAvatar: Expression-Aware Head Avatar Reconstruction with Generative
  Geometry Priors](https://arxiv.org/abs/2508.13537v1)**  
  Authors: Shikun Zhang, Cunjian Chen, Yiqun Wang, Qiuhong Ke, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13537v1.pdf)  
  Keywords: gaussian splatting, avatar, deformation, real-time rendering, vr, 3d gaussian, geometry, high-fidelity, head, ar, face  
- **[TiP4GEN: Text to Immersive Panorama 4D Scene Generation](https://arxiv.org/abs/2508.12415v2)**  
  Authors: Ke Xing, Hanwen Liang, Dejia Xu, Yuyang Yin, Konstantinos N. Plataniotis, Yao Zhao, Yunchao Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12415v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ke-xing.github.io/TiP4GEN/.)  
  Keywords: gaussian splatting, dynamic, vr, 3d gaussian, motion, geometry, ar, 4d  

### Large Scene

*Showing the latest 50 out of 73 papers*

- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v1)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, sparse view, lighting, face, autonomous driving, ar, outdoor, relighting  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, outdoor, 3d reconstruction, lighting, ar, illumination  
- **[Online 3D Gaussian Splatting Modeling with Novel View Selection](https://arxiv.org/abs/2508.14014v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14014v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, ar, outdoor  
- **[InstDrive: Instance-Aware 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2508.12015v1)**  
  Authors: Hongyuan Liu, Haochen Yu, Jianfei Jiang, Qiankun Liu, Jiansheng Chen, Huimin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12015v1.pdf)  
  Keywords: gaussian splatting, dynamic, understanding, 3d gaussian, lightweight, autonomous driving, ar, segmentation, outdoor  
- **[Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.11431v1)**  
  Authors: Simona Kocour, Assia Benbihi, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11431v1.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, geometry, 3d reconstruction, ar, face, outdoor, semantic  
- **[Multi-view Normal and Distance Guidance Gaussian Splatting for Surface
  Reconstruction](https://arxiv.org/abs/2508.07701v2)**  
  Authors: Bo Jia, Yanan Guo, Ying Chang, Benkui Zhang, Ying Xie, Kangning Du, Lin Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07701v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, ar, face, outdoor  
- **[GS4Buildings: Prior-Guided Gaussian Splatting for 3D Building
  Reconstruction](https://arxiv.org/abs/2508.07355v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07355v1.pdf)  
  Keywords: efficient, gaussian splatting, compact, motion, geometry, 3d reconstruction, ar, face, urban scene, semantic  
- **[Evaluating Fisheye-Compatible 3D Gaussian Splatting Methods on Real
  Images Beyond 180 Degree Field of View](https://arxiv.org/abs/2508.06968v1)**  
  Authors: Ulas Gunes, Matias Turkulainen, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06968v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, 3d reconstruction, outdoor  
- **[Neural Gaussian Radio Fields for Channel Estimation](https://arxiv.org/abs/2508.11668v1)**  
  Authors: Muhammad Umer, Muhammad Ahmed Mohsin, Ahsan Bilal, John M. Cioffi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11668v1.pdf)  
  Keywords: efficient, gaussian splatting, dynamic, 3d gaussian, nerf, head, ar, outdoor  
- **[MuGS: Multi-Baseline Generalizable Gaussian Splatting Reconstruction](https://arxiv.org/abs/2508.04297v1)**  
  Authors: Yaopeng Lou, Liao Shen, Tianqi Liu, Jiaqi Li, Zihao Huang, Huiqiang Sun, Zhiguo Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04297v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, geometry, ar, outdoor  

### Model Compression

*Showing the latest 50 out of 406 papers*

- **[Image-Conditioned 3D Gaussian Splat Quantization](https://arxiv.org/abs/2508.15372v1)**  
  Authors: Xinshuang Liu, Runfa Blark Li, Keito Suzuki, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15372v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, 3d gaussian, head, compression, ar  
- **[GeMS: Efficient Gaussian Splatting for Extreme Motion Blur](https://arxiv.org/abs/2508.14682v1)**  
  Authors: Gopi Raju Matta, Trisha Reddypalli, Vemunuri Divya Madhuri, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14682v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, motion, ar  
- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, compact, motion, geometry, 3d reconstruction, ar, tracking  
- **[LongSplat: Robust Unposed 3D Gaussian Splatting for Casual Long Videos](https://arxiv.org/abs/2508.14041v1)**  
  Authors: Chin-Yang Lin, Cheng Sun, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14041v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://linjohnss.github.io/longsplat/)  
  Keywords: efficient, gaussian splatting, 3d gaussian, motion, geometry, ar  
- **[Distilled-3DGS:Distilled 3D Gaussian Splatting](https://arxiv.org/abs/2508.14037v1)**  
  Authors: Lintao Xiang, Xinkai Chen, Jianhuang Lai, Guangcong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14037v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://distilled3dgs.github.io)  
  Keywords: gaussian splatting, 3d gaussian, lightweight, high-fidelity, ar  
- **[InnerGS: Internal Scenes Rendering via Factorized 3D Gaussian Splatting](https://arxiv.org/abs/2508.13287v1)**  
  Authors: Shuxin Liang, Yihan Xiao, Wenlu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13287v1.pdf)  
  Keywords: efficient, gaussian splatting, understanding, 3d gaussian, ar, face  
- **[Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.12720v1)**  
  Authors: Kangjie Chen, Yingji Zhong, Zhihao Li, Jiaqi Lin, Youyu Chen, Minghan Qin, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12720v1.pdf)  
  Keywords: gaussian splatting, sparse-view, understanding, 3d gaussian, lightweight, ar  
- **[InstDrive: Instance-Aware 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2508.12015v1)**  
  Authors: Hongyuan Liu, Haochen Yu, Jianfei Jiang, Qiankun Liu, Jiansheng Chen, Huimin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12015v1.pdf)  
  Keywords: gaussian splatting, dynamic, understanding, 3d gaussian, lightweight, autonomous driving, ar, segmentation, outdoor  
- **[ComplicitSplat: Downstream Models are Vulnerable to Blackbox Attacks by
  3D Gaussian Splat Camouflages](https://arxiv.org/abs/2508.11854v1)**  
  Authors: Matthew Hull, Haoyang Yang, Pratham Mehta, Mansi Phute, Aeree Cho, Haorang Wang, Matthew Lau, Wenke Lee, Wilian Lunardi, Martin Andreoni, Polo Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11854v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, ar  
- **[Versatile Video Tokenization with Generative 2D Gaussian Splatting](https://arxiv.org/abs/2508.11183v1)**  
  Authors: Zhenghao Chen, Zicong Chen, Lei Liu, Yiming Wu, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11183v1.pdf)  
  Keywords: gaussian splatting, dynamic, compact, recognition, compression, ar  

### Quality Enhancement

*Showing the latest 50 out of 161 papers*

- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, geometry, high-fidelity, ray tracing, lighting, face, ar, illumination, reflection, relighting  
- **[Distilled-3DGS:Distilled 3D Gaussian Splatting](https://arxiv.org/abs/2508.14037v1)**  
  Authors: Lintao Xiang, Xinkai Chen, Jianhuang Lai, Guangcong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14037v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://distilled3dgs.github.io)  
  Keywords: gaussian splatting, 3d gaussian, lightweight, high-fidelity, ar  
- **[PhysGM: Large Physical Gaussian Model for Feed-Forward 4D Synthesis](https://arxiv.org/abs/2508.13911v1)**  
  Authors: Chunji Lv, Zequn Chen, Donglin Di, Weinan Zhang, Hao Li, Wei Chen, Changsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13911v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hihixiaolv.github.io/PhysGM.github.io/)  
  Keywords: gaussian splatting, 3d gaussian, motion, high-fidelity, ar, face, 4d  
- **[EAvatar: Expression-Aware Head Avatar Reconstruction with Generative
  Geometry Priors](https://arxiv.org/abs/2508.13537v1)**  
  Authors: Shikun Zhang, Cunjian Chen, Yiqun Wang, Qiuhong Ke, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13537v1.pdf)  
  Keywords: gaussian splatting, avatar, deformation, real-time rendering, vr, 3d gaussian, geometry, high-fidelity, head, ar, face  
- **[Improving Densification in 3D Gaussian Splatting for High-Fidelity
  Rendering](https://arxiv.org/abs/2508.12313v1)**  
  Authors: Xiaobin Deng, Changyu Diao, Min Li, Ruohan Yu, Duanqing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12313v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, 3d gaussian, high-fidelity, head, ar  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, compact, nerf, high-fidelity, ar, lighting, segmentation, survey, semantic  
- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event
  Cameras](https://arxiv.org/abs/2508.09912v1)**  
  Authors: Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09912v1.pdf)  
  Keywords: gaussian splatting, dynamic, motion, high-fidelity, ar, lighting, 4d, fast  
- **[EGS-SLAM: RGB-D Gaussian Splatting SLAM with Events](https://arxiv.org/abs/2508.07003v1)**  
  Authors: Siyu Chen, Shenghai Yuan, Thien-Minh Nguyen, Zhuyu Huang, Chenyang Shi, Jin Jing, Lihua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07003v1.pdf)  
  Keywords: gaussian splatting, slam, mapping, dynamic, 3d gaussian, motion, high-fidelity, 3d reconstruction, ar, tracking  
- **[GAP: Gaussianize Any Point Clouds with Text Guidance](https://arxiv.org/abs/2508.05631v1)**  
  Authors: Weiqi Zhang, Junsheng Zhou, Haotian Geng, Wenyuan Zhang, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05631v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weiqi-zhang.github.io/GAP.)  
  Keywords: gaussian splatting, 3d gaussian, high-fidelity, ar, face, fast  
- **[3DGabSplat: 3D Gabor Splatting for Frequency-adaptive Radiance Field
  Rendering](https://arxiv.org/abs/2508.05343v1)**  
  Authors: Junyu Zhou, Yuyang Huang, Wenrui Dai, Junni Zou, Ziyang Zheng, Nuowen Kan, Chenglin Li, Hongkai Xiong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05343v1.pdf)  
  Keywords: efficient, gaussian splatting, real-time rendering, 3d gaussian, high-fidelity, head, ar  

### Ray Tracing

- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, geometry, high-fidelity, ray tracing, lighting, face, ar, illumination, reflection, relighting  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: gaussian splatting, shadow, dynamic, 3d gaussian, global illumination, outdoor, relightable, ar, lighting, face, illumination, relighting  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: gaussian splatting, dynamic, path tracing, 3d gaussian, ar, lighting, face  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: efficient, gaussian splatting, efficient rendering, 3d gaussian, geometry, relightable, ar, lighting, face, ray marching, relighting  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: efficient, gaussian splatting, real-time rendering, high-fidelity, ray tracing, ar  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v2)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v2.pdf)  
  Keywords: gaussian splatting, avatar, shadow, geometry, human, relightable, ray tracing, lighting, ar, fast, relighting  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: efficient, gaussian splatting, efficient rendering, 3d gaussian, ray tracing, lighting, ar, acceleration, relighting  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: efficient, gaussian splatting, animation, dynamic, 3d gaussian, compact, ar, acceleration, ray marching  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: efficient, gaussian splatting, real-time rendering, 3d gaussian, global illumination, ray tracing, lighting, face, ar, illumination  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: gaussian splatting, shadow, 3d gaussian, neural rendering, ray tracing, ar, fast, reflection  

### Relighting

*Showing the latest 50 out of 114 papers*

- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v1)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, sparse view, lighting, face, autonomous driving, ar, outdoor, relighting  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, geometry, high-fidelity, ray tracing, lighting, face, ar, illumination, reflection, relighting  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, outdoor, 3d reconstruction, lighting, ar, illumination  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, compact, nerf, high-fidelity, ar, lighting, segmentation, survey, semantic  
- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event
  Cameras](https://arxiv.org/abs/2508.09912v1)**  
  Authors: Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09912v1.pdf)  
  Keywords: gaussian splatting, dynamic, motion, high-fidelity, ar, lighting, 4d, fast  
- **[HumanGenesis: Agent-Based Geometric and Generative Modeling for
  Synthetic Human Dynamics](https://arxiv.org/abs/2508.09858v1)**  
  Authors: Weiqi Li, Zehao Zhang, Liang Lin, Guangrun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09858v1.pdf)  
  Keywords: gaussian splatting, dynamic, deformation, 3d gaussian, motion, human, ar, face, 4d, reflection  
- **[Vision-Only Gaussian Splatting for Collaborative Semantic Occupancy
  Prediction](https://arxiv.org/abs/2508.10936v1)**  
  Authors: Cheng Chen, Hao Huang, Saurabh Bagchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.10936v1.pdf)  
  Keywords: gaussian splatting, geometry, ar, lighting, semantic  
- **[Touch-Augmented Gaussian Splatting for Enhanced 3D Scene Reconstruction](https://arxiv.org/abs/2508.07717v1)**  
  Authors: Yuchen Gao, Xiao Xu, Eckehard Steinbach, Daniel E. Lucani, Qi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07717v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, ar, lighting, face  
- **[UW-3DGS: Underwater 3D Reconstruction with Physics-Aware Gaussian
  Splatting](https://arxiv.org/abs/2508.06169v1)**  
  Authors: Wenpeng Xing, Jie Chen, Zaifeng Yang, Changting Lin, Jianfeng Dong, Chaochao Chen, Xun Zhou, Meng Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06169v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, geometry, 3d reconstruction, light transport, face, ar  
- **[A 3DGS-Diffusion Self-Supervised Framework for Normal Estimation from a
  Single Image](https://arxiv.org/abs/2508.05950v1)**  
  Authors: Yanxing Liang, Yinghui Wang, Jinlong Yang, Wei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05950v1.pdf)  
  Keywords: gaussian splatting, mapping, 3d gaussian, light transport, ar, face  

### SLAM

*Showing the latest 50 out of 151 papers*

- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, compact, motion, geometry, 3d reconstruction, ar, tracking  
- **[Online 3D Gaussian Splatting Modeling with Novel View Selection](https://arxiv.org/abs/2508.14014v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14014v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, ar, outdoor  
- **[SAGOnline: Segment Any Gaussians Online](https://arxiv.org/abs/2508.08219v1)**  
  Authors: Wentao Sun, Quanyun Wu, Hanqing Xu, Kyle Gao, Zhengsen Xu, Yiping Chen, Dedong Zhang, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08219v1.pdf)  
  Keywords: efficient, gaussian splatting, understanding, real-time rendering, vr, 3d gaussian, nerf, lightweight, ar, segmentation, tracking  
- **[NeeCo: Image Synthesis of Novel Instrument States Based on Dynamic and
  Deformable 3D Gaussian Reconstruction](https://arxiv.org/abs/2508.07897v1)**  
  Authors: Tianle Zeng, Junlei Hu, Gerardo Loza Galindo, Sharib Ali, Duygu Sarikaya, Pietro Valdastri, Dominic Jones  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07897v1.pdf)  
  Keywords: gaussian splatting, dynamic, deformation, 3d gaussian, motion, medical, ar, localization, tracking  
- **[EGS-SLAM: RGB-D Gaussian Splatting SLAM with Events](https://arxiv.org/abs/2508.07003v1)**  
  Authors: Siyu Chen, Shenghai Yuan, Thien-Minh Nguyen, Zhuyu Huang, Chenyang Shi, Jin Jing, Lihua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07003v1.pdf)  
  Keywords: gaussian splatting, slam, mapping, dynamic, 3d gaussian, motion, high-fidelity, 3d reconstruction, ar, tracking  
- **[A 3DGS-Diffusion Self-Supervised Framework for Normal Estimation from a
  Single Image](https://arxiv.org/abs/2508.05950v1)**  
  Authors: Yanxing Liang, Yinghui Wang, Jinlong Yang, Wei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05950v1.pdf)  
  Keywords: gaussian splatting, mapping, 3d gaussian, light transport, ar, face  
- **[Stereo 3D Gaussian Splatting SLAM for Outdoor Urban Scenes](https://arxiv.org/abs/2507.23677v1)**  
  Authors: Xiaohan Li, Ziren Gong, Fabio Tosi, Matteo Poggi, Stefano Mattoccia, Dong Liu, Jun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23677v1.pdf)  
  Keywords: gaussian splatting, slam, mapping, 3d gaussian, outdoor, high-fidelity, ar, urban scene, fast, tracking  
- **[Gaussian Splatting Feature Fields for Privacy-Preserving Visual
  Localization](https://arxiv.org/abs/2507.23569v1)**  
  Authors: Maxime Pietrantoni, Gabriela Csurka, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23569v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, ar, segmentation, localization  
- **[MagicRoad: Semantic-Aware 3D Road Surface Reconstruction via Obstacle
  Inpainting](https://arxiv.org/abs/2507.23340v1)**  
  Authors: Xingyue Peng, Yuandong Lyu, Lang Zhang, Jian Zhu, Songtao Wang, Jiaxin Deng, Songxin Lu, Weiliang Ma, Dangen She, Peng Jia, XianPeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23340v1.pdf)  
  Keywords: efficient, gaussian splatting, mapping, dynamic, 3d gaussian, autonomous driving, ar, lighting, face, segmentation, semantic  
- **[GSFusion:Globally Optimized LiDAR-Inertial-Visual Mapping for Gaussian
  Splatting](https://arxiv.org/abs/2507.23273v1)**  
  Authors: Jaeseok Park, Chanoh Park, Minsu Kim, Soohwan Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23273v1.pdf)  
  Keywords: efficient, gaussian splatting, slam, mapping, 3d gaussian, ar, illumination  

### Scene Understanding

*Showing the latest 50 out of 196 papers*

- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, outdoor, 3d reconstruction, lighting, ar, illumination  
- **[GALA: Guided Attention with Language Alignment for Open Vocabulary
  Gaussian Splatting](https://arxiv.org/abs/2508.14278v2)**  
  Authors: Elena Alegret, Kunyi Li, Sen Wang, Siyun Liang, Michael Niemeyer, Stefano Gasperini, Nassir Navab, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14278v2.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, ar, semantic  
- **[InnerGS: Internal Scenes Rendering via Factorized 3D Gaussian Splatting](https://arxiv.org/abs/2508.13287v1)**  
  Authors: Shuxin Liang, Yihan Xiao, Wenlu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13287v1.pdf)  
  Keywords: efficient, gaussian splatting, understanding, 3d gaussian, ar, face  
- **[IntelliCap: Intelligent Guidance for Consistent View Sampling](https://arxiv.org/abs/2508.13043v1)**  
  Authors: Ayaka Yasunaga, Hideo Saito, Dieter Schmalstieg, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13043v1.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, human, ar, segmentation, semantic  
- **[Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.12720v1)**  
  Authors: Kangjie Chen, Yingji Zhong, Zhihao Li, Jiaqi Lin, Youyu Chen, Minghan Qin, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12720v1.pdf)  
  Keywords: gaussian splatting, sparse-view, understanding, 3d gaussian, lightweight, ar  
- **[InstDrive: Instance-Aware 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2508.12015v1)**  
  Authors: Hongyuan Liu, Haochen Yu, Jianfei Jiang, Qiankun Liu, Jiansheng Chen, Huimin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12015v1.pdf)  
  Keywords: gaussian splatting, dynamic, understanding, 3d gaussian, lightweight, autonomous driving, ar, segmentation, outdoor  
- **[Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.11431v1)**  
  Authors: Simona Kocour, Assia Benbihi, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11431v1.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, geometry, 3d reconstruction, ar, face, outdoor, semantic  
- **[Versatile Video Tokenization with Generative 2D Gaussian Splatting](https://arxiv.org/abs/2508.11183v1)**  
  Authors: Zhenghao Chen, Zicong Chen, Lei Liu, Yiming Wu, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11183v1.pdf)  
  Keywords: gaussian splatting, dynamic, compact, recognition, compression, ar  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, compact, nerf, high-fidelity, ar, lighting, segmentation, survey, semantic  
- **[GSFixer: Improving 3D Gaussian Splatting with Reference-Guided Video
  Diffusion Priors](https://arxiv.org/abs/2508.09667v1)**  
  Authors: Xingyilang Yin, Qi Zhang, Jiahao Chang, Ying Feng, Qingnan Fan, Xi Yang, Chi-Man Pun, Huaqi Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09667v1.pdf)  
  Keywords: gaussian splatting, sparse-view, 3d gaussian, geometry, sparse view, 3d reconstruction, ar, semantic  



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