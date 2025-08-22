# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-08-22 00:52:36

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
- [Acceleration](#acceleration) (264 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (321 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (391 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (72 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (311 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (72 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (405 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (162 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (19 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (113 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (152 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (199 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v1)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v1.pdf)  
  Keywords: gaussian splatting, semantic, lighting, nerf, 3d gaussian, segmentation, understanding, ar, high-fidelity, survey, compact  
- **[A Study of the Framework and Real-World Applications of Language
  Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: gaussian splatting, semantic, nerf, 3d gaussian, survey, robotics, ar, efficient, understanding  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned
  and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: gaussian splatting, nerf, 3d gaussian, robotics, ar, human, survey  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, nerf, 3d gaussian, geometry, sparse-view, robotics, ar, survey, vr, motion  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v2)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v2.pdf)  
  Keywords: slam, gaussian splatting, 3d reconstruction, lighting, dynamic, nerf, 3d gaussian, robotics, ar, fast, human, survey, vr  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: gaussian splatting, dynamic, nerf, 3d gaussian, autonomous driving, outdoor, high-fidelity, ar, survey, efficient, face  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: gaussian splatting, neural rendering, 3d reconstruction, nerf, 3d gaussian, autonomous driving, robotics, high-fidelity, ar, survey, vr  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: gaussian splatting, neural rendering, semantic, 3d reconstruction, 3d gaussian, segmentation, outdoor, high-fidelity, ar, survey, efficient, understanding  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: slam, gaussian splatting, semantic, nerf, 3d gaussian, survey, segmentation, mapping, ar, efficient, localization  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to
  Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: gaussian splatting, 4d, dynamic, 3d gaussian, understanding, ar, body, survey, motion  

### Acceleration

*Showing the latest 50 out of 264 papers*

- **[EAvatar: Expression-Aware Head Avatar Reconstruction with Generative
  Geometry Priors](https://arxiv.org/abs/2508.13537v1)**  
  Authors: Shikun Zhang, Cunjian Chen, Yiqun Wang, Qiuhong Ke, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13537v1.pdf)  
  Keywords: gaussian splatting, avatar, 3d gaussian, real-time rendering, geometry, head, ar, high-fidelity, vr, face, deformation  
- **[Improving Densification in 3D Gaussian Splatting for High-Fidelity
  Rendering](https://arxiv.org/abs/2508.12313v1)**  
  Authors: Xiaobin Deng, Changyu Diao, Min Li, Ruohan Yu, Duanqing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12313v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, head, ar, high-fidelity  
- **[Multi-Sample Anti-Aliasing and Constrained Optimization for 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.10507v1)**  
  Authors: Zheng Zhou, Jia-Chen Zhang, Yu-Jie Xiong, Chun-Ming Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.10507v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, real-time rendering, ar  
- **[EntropyGS: An Efficient Entropy Coding on 3D Gaussian Splatting](https://arxiv.org/abs/2508.10227v1)**  
  Authors: Yuning Huang, Jiahao Pang, Fengqing Zhu, Dong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.10227v1.pdf)  
  Keywords: gaussian splatting, compression, 3d gaussian, ar, fast, efficient  
- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event
  Cameras](https://arxiv.org/abs/2508.09912v1)**  
  Authors: Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09912v1.pdf)  
  Keywords: gaussian splatting, 4d, lighting, dynamic, ar, high-fidelity, fast, motion  
- **[SAGOnline: Segment Any Gaussians Online](https://arxiv.org/abs/2508.08219v1)**  
  Authors: Wentao Sun, Quanyun Wu, Hanqing Xu, Kyle Gao, Zhengsen Xu, Yiping Chen, Dedong Zhang, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08219v1.pdf)  
  Keywords: gaussian splatting, nerf, 3d gaussian, real-time rendering, tracking, segmentation, ar, efficient, lightweight, vr, understanding  
- **[DIP-GS: Deep Image Prior For Gaussian Splatting Sparse View Recovery](https://arxiv.org/abs/2508.07372v1)**  
  Authors: Rajaei Khatib, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07372v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, sparse-view, ar, sparse view  
- **[ExploreGS: Explorable 3D Scene Reconstruction with Virtual Camera
  Samplings and Diffusion Priors](https://arxiv.org/abs/2508.06014v1)**  
  Authors: Minsu Kim, Subin Jeon, In Cho, Mijin Yoo, Seon Joo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06014v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://exploregs.github.io)  
  Keywords: gaussian splatting, ar, 3d gaussian, real-time rendering  
- **[Optimization-Free Style Transfer for 3D Gaussian Splats](https://arxiv.org/abs/2508.05813v1)**  
  Authors: Raphael Du Sablon, David Hart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05813v1.pdf)  
  Keywords: ar, 3d gaussian, face, fast  
- **[GAP: Gaussianize Any Point Clouds with Text Guidance](https://arxiv.org/abs/2508.05631v1)**  
  Authors: Weiqi Zhang, Junsheng Zhou, Haotian Geng, Wenyuan Zhang, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05631v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weiqi-zhang.github.io/GAP.)  
  Keywords: gaussian splatting, 3d gaussian, ar, high-fidelity, fast, face  

### Applications

*Showing the latest 50 out of 995 papers*

- **[GSFix3D: Diffusion-Guided Repair of Novel Views in Gaussian Splatting](https://arxiv.org/abs/2508.14717v1)**  
  Authors: Jiaxin Wei, Stefan Leutenegger, Simon Schaefer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14717v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsfix3d.github.io.)  
  Keywords: 3d reconstruction, gaussian splatting, ar, 3d gaussian  
- **[GeMS: Efficient Gaussian Splatting for Extreme Motion Blur](https://arxiv.org/abs/2508.14682v1)**  
  Authors: Gopi Raju Matta, Trisha Reddypalli, Vemunuri Divya Madhuri, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14682v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, motion  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: gaussian splatting, relighting, illumination, lighting, nerf, 3d gaussian, geometry, ar, ray tracing, high-fidelity, reflection, face  
- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, tracking, geometry, ar, compact, efficient, motion  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: gaussian splatting, illumination, lighting, 3d reconstruction, 3d gaussian, outdoor, ar, understanding  
- **[GALA: Guided Attention with Language Alignment for Open Vocabulary
  Gaussian Splatting](https://arxiv.org/abs/2508.14278v2)**  
  Authors: Elena Alegret, Kunyi Li, Sen Wang, Siyun Liang, Michael Niemeyer, Stefano Gasperini, Nassir Navab, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14278v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, semantic, understanding  
- **[LongSplat: Robust Unposed 3D Gaussian Splatting for Casual Long Videos](https://arxiv.org/abs/2508.14041v1)**  
  Authors: Chin-Yang Lin, Cheng Sun, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14041v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://linjohnss.github.io/longsplat/)  
  Keywords: gaussian splatting, 3d gaussian, geometry, ar, efficient, motion  
- **[Distilled-3DGS:Distilled 3D Gaussian Splatting](https://arxiv.org/abs/2508.14037v1)**  
  Authors: Lintao Xiang, Xinkai Chen, Jianhuang Lai, Guangcong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14037v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://distilled3dgs.github.io)  
  Keywords: gaussian splatting, 3d gaussian, ar, high-fidelity, lightweight  
- **[Online 3D Gaussian Splatting Modeling with Novel View Selection](https://arxiv.org/abs/2508.14014v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14014v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, ar, outdoor  
- **[PhysGM: Large Physical Gaussian Model for Feed-Forward 4D Synthesis](https://arxiv.org/abs/2508.13911v1)**  
  Authors: Chunji Lv, Zequn Chen, Donglin Di, Weinan Zhang, Hao Li, Wei Chen, Changsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13911v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hihixiaolv.github.io/PhysGM.github.io/)  
  Keywords: gaussian splatting, 4d, 3d gaussian, ar, high-fidelity, face, motion  

### Avatar Generation

*Showing the latest 50 out of 321 papers*

- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: gaussian splatting, relighting, illumination, lighting, nerf, 3d gaussian, geometry, ar, ray tracing, high-fidelity, reflection, face  
- **[PhysGM: Large Physical Gaussian Model for Feed-Forward 4D Synthesis](https://arxiv.org/abs/2508.13911v1)**  
  Authors: Chunji Lv, Zequn Chen, Donglin Di, Weinan Zhang, Hao Li, Wei Chen, Changsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13911v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hihixiaolv.github.io/PhysGM.github.io/)  
  Keywords: gaussian splatting, 4d, 3d gaussian, ar, high-fidelity, face, motion  
- **[EAvatar: Expression-Aware Head Avatar Reconstruction with Generative
  Geometry Priors](https://arxiv.org/abs/2508.13537v1)**  
  Authors: Shikun Zhang, Cunjian Chen, Yiqun Wang, Qiuhong Ke, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13537v1.pdf)  
  Keywords: gaussian splatting, avatar, 3d gaussian, real-time rendering, geometry, head, ar, high-fidelity, vr, face, deformation  
- **[InnerGS: Internal Scenes Rendering via Factorized 3D Gaussian Splatting](https://arxiv.org/abs/2508.13287v1)**  
  Authors: Shuxin Liang, Yihan Xiao, Wenlu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13287v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, face, understanding  
- **[IntelliCap: Intelligent Guidance for Consistent View Sampling](https://arxiv.org/abs/2508.13043v1)**  
  Authors: Ayaka Yasunaga, Hideo Saito, Dieter Schmalstieg, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13043v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, segmentation, ar, human, semantic, understanding  
- **[Improving Densification in 3D Gaussian Splatting for High-Fidelity
  Rendering](https://arxiv.org/abs/2508.12313v1)**  
  Authors: Xiaobin Deng, Changyu Diao, Min Li, Ruohan Yu, Duanqing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12313v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, head, ar, high-fidelity  
- **[Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.11431v1)**  
  Authors: Simona Kocour, Assia Benbihi, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11431v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, geometry, outdoor, ar, semantic, face, understanding  
- **[HumanGenesis: Agent-Based Geometric and Generative Modeling for
  Synthetic Human Dynamics](https://arxiv.org/abs/2508.09858v1)**  
  Authors: Weiqi Li, Zehao Zhang, Liang Lin, Guangrun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09858v1.pdf)  
  Keywords: gaussian splatting, 4d, deformation, dynamic, 3d gaussian, ar, reflection, human, face, motion  
- **[Toward Human-Robot Teaming: Learning Handover Behaviors from 3D Scenes](https://arxiv.org/abs/2508.09855v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09855v1.pdf)  
  Keywords: sparse-view, gaussian splatting, human, ar  
- **[Gradient-Direction-Aware Density Control for 3D Gaussian Splatting](https://arxiv.org/abs/2508.09239v1)**  
  Authors: Zheng Zhou, Yu-Jie Xiong, Chun-Ming Xia, Jia-Chen Zhang, Hong-Jian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09239v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, head, ar, compact  

### Dynamic Scene

*Showing the latest 50 out of 391 papers*

- **[GeMS: Efficient Gaussian Splatting for Extreme Motion Blur](https://arxiv.org/abs/2508.14682v1)**  
  Authors: Gopi Raju Matta, Trisha Reddypalli, Vemunuri Divya Madhuri, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14682v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, motion  
- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, tracking, geometry, ar, compact, efficient, motion  
- **[LongSplat: Robust Unposed 3D Gaussian Splatting for Casual Long Videos](https://arxiv.org/abs/2508.14041v1)**  
  Authors: Chin-Yang Lin, Cheng Sun, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14041v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://linjohnss.github.io/longsplat/)  
  Keywords: gaussian splatting, 3d gaussian, geometry, ar, efficient, motion  
- **[PhysGM: Large Physical Gaussian Model for Feed-Forward 4D Synthesis](https://arxiv.org/abs/2508.13911v1)**  
  Authors: Chunji Lv, Zequn Chen, Donglin Di, Weinan Zhang, Hao Li, Wei Chen, Changsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13911v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hihixiaolv.github.io/PhysGM.github.io/)  
  Keywords: gaussian splatting, 4d, 3d gaussian, ar, high-fidelity, face, motion  
- **[EAvatar: Expression-Aware Head Avatar Reconstruction with Generative
  Geometry Priors](https://arxiv.org/abs/2508.13537v1)**  
  Authors: Shikun Zhang, Cunjian Chen, Yiqun Wang, Qiuhong Ke, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13537v1.pdf)  
  Keywords: gaussian splatting, avatar, 3d gaussian, real-time rendering, geometry, head, ar, high-fidelity, vr, face, deformation  
- **[TiP4GEN: Text to Immersive Panorama 4D Scene Generation](https://arxiv.org/abs/2508.12415v2)**  
  Authors: Ke Xing, Hanwen Liang, Dejia Xu, Yuyang Yin, Konstantinos N. Plataniotis, Yao Zhao, Yunchao Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12415v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ke-xing.github.io/TiP4GEN/.)  
  Keywords: gaussian splatting, 4d, dynamic, 3d gaussian, geometry, ar, vr, motion  
- **[InstDrive: Instance-Aware 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2508.12015v1)**  
  Authors: Hongyuan Liu, Haochen Yu, Jianfei Jiang, Qiankun Liu, Jiansheng Chen, Huimin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12015v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, autonomous driving, segmentation, outdoor, ar, lightweight, understanding  
- **[Versatile Video Tokenization with Generative 2D Gaussian Splatting](https://arxiv.org/abs/2508.11183v1)**  
  Authors: Zhenghao Chen, Zicong Chen, Lei Liu, Yiming Wu, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11183v1.pdf)  
  Keywords: gaussian splatting, compression, dynamic, recognition, ar, compact  
- **[Multi-Sample Anti-Aliasing and Constrained Optimization for 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.10507v1)**  
  Authors: Zheng Zhou, Jia-Chen Zhang, Yu-Jie Xiong, Chun-Ming Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.10507v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, real-time rendering, ar  
- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event
  Cameras](https://arxiv.org/abs/2508.09912v1)**  
  Authors: Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09912v1.pdf)  
  Keywords: gaussian splatting, 4d, lighting, dynamic, ar, high-fidelity, fast, motion  

### Few-shot

*Showing the latest 50 out of 72 papers*

- **[Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.12720v1)**  
  Authors: Kangjie Chen, Yingji Zhong, Zhihao Li, Jiaqi Lin, Youyu Chen, Minghan Qin, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12720v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, sparse-view, ar, lightweight, understanding  
- **[Toward Human-Robot Teaming: Learning Handover Behaviors from 3D Scenes](https://arxiv.org/abs/2508.09855v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09855v1.pdf)  
  Keywords: sparse-view, gaussian splatting, human, ar  
- **[GSFixer: Improving 3D Gaussian Splatting with Reference-Guided Video
  Diffusion Priors](https://arxiv.org/abs/2508.09667v1)**  
  Authors: Xingyilang Yin, Qi Zhang, Jiahao Chang, Ying Feng, Qingnan Fan, Xi Yang, Chi-Man Pun, Huaqi Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09667v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, geometry, sparse-view, ar, semantic, sparse view  
- **[SkySplat: Generalizable 3D Gaussian Splatting from Multi-Temporal Sparse
  Satellite Images](https://arxiv.org/abs/2508.09479v1)**  
  Authors: Xuejun Huang, Xinyi Liu, Yi Wan, Zhi Zheng, Bin Zhang, Mingtao Xiong, Yingying Pei, Yongjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09479v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, sparse-view, ar, efficient  
- **[DIP-GS: Deep Image Prior For Gaussian Splatting Sparse View Recovery](https://arxiv.org/abs/2508.07372v1)**  
  Authors: Rajaei Khatib, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07372v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, sparse-view, ar, sparse view  
- **[UGOD: Uncertainty-Guided Differentiable Opacity and Soft Dropout for
  Enhanced Sparse-View 3DGS](https://arxiv.org/abs/2508.04968v1)**  
  Authors: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Liangxiu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04968v1.pdf)  
  Keywords: gaussian splatting, nerf, 3d gaussian, sparse-view, ar  
- **[DET-GS: Depth- and Edge-Aware Regularization for High-Fidelity 3D
  Gaussian Splatting](https://arxiv.org/abs/2508.04099v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04099v1.pdf)  
  Keywords: gaussian splatting, semantic, 3d gaussian, sparse-view, ar, high-fidelity, efficient  
- **[GR-Gaussian: Graph-Based Radiative Gaussian Splatting for Sparse-View CT
  Reconstruction](https://arxiv.org/abs/2508.02408v2)**  
  Authors: Yikuang Yuluo, Yue Ma, Kuan Shen, Tongtong Jin, Wang Liao, Yangpu Ma, Fuquan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.02408v2.pdf)  
  Keywords: sparse-view, gaussian splatting, ar, 3d gaussian  
- **[No Pose at All: Self-Supervised Pose-Free 3D Gaussian Splatting from
  Sparse Views](https://arxiv.org/abs/2508.01171v1)**  
  Authors: Ranran Huang, Krystian Mikolajczyk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.01171v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ranrhuang.github.io/spfsplat/.)  
  Keywords: gaussian splatting, 3d gaussian, geometry, ar, efficient, sparse view  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, nerf, 3d gaussian, geometry, sparse-view, robotics, ar, survey, vr, motion  

### Geometry Reconstruction

*Showing the latest 50 out of 311 papers*

- **[GSFix3D: Diffusion-Guided Repair of Novel Views in Gaussian Splatting](https://arxiv.org/abs/2508.14717v1)**  
  Authors: Jiaxin Wei, Stefan Leutenegger, Simon Schaefer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14717v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsfix3d.github.io.)  
  Keywords: 3d reconstruction, gaussian splatting, ar, 3d gaussian  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: gaussian splatting, relighting, illumination, lighting, nerf, 3d gaussian, geometry, ar, ray tracing, high-fidelity, reflection, face  
- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, tracking, geometry, ar, compact, efficient, motion  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: gaussian splatting, illumination, lighting, 3d reconstruction, 3d gaussian, outdoor, ar, understanding  
- **[LongSplat: Robust Unposed 3D Gaussian Splatting for Casual Long Videos](https://arxiv.org/abs/2508.14041v1)**  
  Authors: Chin-Yang Lin, Cheng Sun, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14041v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://linjohnss.github.io/longsplat/)  
  Keywords: gaussian splatting, 3d gaussian, geometry, ar, efficient, motion  
- **[EAvatar: Expression-Aware Head Avatar Reconstruction with Generative
  Geometry Priors](https://arxiv.org/abs/2508.13537v1)**  
  Authors: Shikun Zhang, Cunjian Chen, Yiqun Wang, Qiuhong Ke, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13537v1.pdf)  
  Keywords: gaussian splatting, avatar, 3d gaussian, real-time rendering, geometry, head, ar, high-fidelity, vr, face, deformation  
- **[TiP4GEN: Text to Immersive Panorama 4D Scene Generation](https://arxiv.org/abs/2508.12415v2)**  
  Authors: Ke Xing, Hanwen Liang, Dejia Xu, Yuyang Yin, Konstantinos N. Plataniotis, Yao Zhao, Yunchao Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12415v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ke-xing.github.io/TiP4GEN/.)  
  Keywords: gaussian splatting, 4d, dynamic, 3d gaussian, geometry, ar, vr, motion  
- **[Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.11431v1)**  
  Authors: Simona Kocour, Assia Benbihi, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11431v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, geometry, outdoor, ar, semantic, face, understanding  
- **[GSFixer: Improving 3D Gaussian Splatting with Reference-Guided Video
  Diffusion Priors](https://arxiv.org/abs/2508.09667v1)**  
  Authors: Xingyilang Yin, Qi Zhang, Jiahao Chang, Ying Feng, Qingnan Fan, Xi Yang, Chi-Man Pun, Huaqi Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09667v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, geometry, sparse-view, ar, semantic, sparse view  
- **[Vision-Only Gaussian Splatting for Collaborative Semantic Occupancy
  Prediction](https://arxiv.org/abs/2508.10936v1)**  
  Authors: Cheng Chen, Hao Huang, Saurabh Bagchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.10936v1.pdf)  
  Keywords: gaussian splatting, lighting, geometry, ar, semantic  

### Large Scene

*Showing the latest 50 out of 72 papers*

- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: gaussian splatting, illumination, lighting, 3d reconstruction, 3d gaussian, outdoor, ar, understanding  
- **[Online 3D Gaussian Splatting Modeling with Novel View Selection](https://arxiv.org/abs/2508.14014v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14014v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, ar, outdoor  
- **[InstDrive: Instance-Aware 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2508.12015v1)**  
  Authors: Hongyuan Liu, Haochen Yu, Jianfei Jiang, Qiankun Liu, Jiansheng Chen, Huimin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12015v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, autonomous driving, segmentation, outdoor, ar, lightweight, understanding  
- **[Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.11431v1)**  
  Authors: Simona Kocour, Assia Benbihi, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11431v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, geometry, outdoor, ar, semantic, face, understanding  
- **[Multi-view Normal and Distance Guidance Gaussian Splatting for Surface
  Reconstruction](https://arxiv.org/abs/2508.07701v2)**  
  Authors: Bo Jia, Yanan Guo, Ying Chang, Benkui Zhang, Ying Xie, Kangning Du, Lin Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07701v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, outdoor, ar, face  
- **[GS4Buildings: Prior-Guided Gaussian Splatting for 3D Building
  Reconstruction](https://arxiv.org/abs/2508.07355v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07355v1.pdf)  
  Keywords: gaussian splatting, semantic, 3d reconstruction, urban scene, geometry, ar, compact, efficient, face, motion  
- **[Evaluating Fisheye-Compatible 3D Gaussian Splatting Methods on Real
  Images Beyond 180 Degree Field of View](https://arxiv.org/abs/2508.06968v1)**  
  Authors: Ulas Gunes, Matias Turkulainen, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06968v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, ar, outdoor  
- **[Neural Gaussian Radio Fields for Channel Estimation](https://arxiv.org/abs/2508.11668v1)**  
  Authors: Muhammad Umer, Muhammad Ahmed Mohsin, Ahsan Bilal, John M. Cioffi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11668v1.pdf)  
  Keywords: gaussian splatting, dynamic, nerf, 3d gaussian, head, outdoor, ar, efficient  
- **[MuGS: Multi-Baseline Generalizable Gaussian Splatting Reconstruction](https://arxiv.org/abs/2508.04297v1)**  
  Authors: Yaopeng Lou, Liao Shen, Tianqi Liu, Jiaqi Li, Zihao Huang, Huiqiang Sun, Zhiguo Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04297v1.pdf)  
  Keywords: gaussian splatting, nerf, 3d gaussian, geometry, outdoor, ar  
- **[VDEGaussian: Video Diffusion Enhanced 4D Gaussian Splatting for Dynamic
  Urban Scenes Modeling](https://arxiv.org/abs/2508.02129v1)**  
  Authors: Yuru Xiao, Zihan Lin, Chao Lu, Deming Zhai, Kui Jiang, Wenbo Zhao, Wei Zhang, Junjun Jiang, Huanran Wang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.02129v1.pdf)  
  Keywords: gaussian splatting, 4d, dynamic, urban scene, ar, high-fidelity, fast, face  

### Model Compression

*Showing the latest 50 out of 405 papers*

- **[GeMS: Efficient Gaussian Splatting for Extreme Motion Blur](https://arxiv.org/abs/2508.14682v1)**  
  Authors: Gopi Raju Matta, Trisha Reddypalli, Vemunuri Divya Madhuri, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14682v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, motion  
- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, tracking, geometry, ar, compact, efficient, motion  
- **[LongSplat: Robust Unposed 3D Gaussian Splatting for Casual Long Videos](https://arxiv.org/abs/2508.14041v1)**  
  Authors: Chin-Yang Lin, Cheng Sun, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14041v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://linjohnss.github.io/longsplat/)  
  Keywords: gaussian splatting, 3d gaussian, geometry, ar, efficient, motion  
- **[Distilled-3DGS:Distilled 3D Gaussian Splatting](https://arxiv.org/abs/2508.14037v1)**  
  Authors: Lintao Xiang, Xinkai Chen, Jianhuang Lai, Guangcong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14037v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://distilled3dgs.github.io)  
  Keywords: gaussian splatting, 3d gaussian, ar, high-fidelity, lightweight  
- **[InnerGS: Internal Scenes Rendering via Factorized 3D Gaussian Splatting](https://arxiv.org/abs/2508.13287v1)**  
  Authors: Shuxin Liang, Yihan Xiao, Wenlu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13287v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, face, understanding  
- **[Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.12720v1)**  
  Authors: Kangjie Chen, Yingji Zhong, Zhihao Li, Jiaqi Lin, Youyu Chen, Minghan Qin, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12720v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, sparse-view, ar, lightweight, understanding  
- **[InstDrive: Instance-Aware 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2508.12015v1)**  
  Authors: Hongyuan Liu, Haochen Yu, Jianfei Jiang, Qiankun Liu, Jiansheng Chen, Huimin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12015v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, autonomous driving, segmentation, outdoor, ar, lightweight, understanding  
- **[ComplicitSplat: Downstream Models are Vulnerable to Blackbox Attacks by
  3D Gaussian Splat Camouflages](https://arxiv.org/abs/2508.11854v1)**  
  Authors: Matthew Hull, Haoyang Yang, Pratham Mehta, Mansi Phute, Aeree Cho, Haorang Wang, Matthew Lau, Wenke Lee, Wilian Lunardi, Martin Andreoni, Polo Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11854v1.pdf)  
  Keywords: gaussian splatting, efficient, ar, 3d gaussian  
- **[Versatile Video Tokenization with Generative 2D Gaussian Splatting](https://arxiv.org/abs/2508.11183v1)**  
  Authors: Zhenghao Chen, Zicong Chen, Lei Liu, Yiming Wu, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11183v1.pdf)  
  Keywords: gaussian splatting, compression, dynamic, recognition, ar, compact  
- **[EntropyGS: An Efficient Entropy Coding on 3D Gaussian Splatting](https://arxiv.org/abs/2508.10227v1)**  
  Authors: Yuning Huang, Jiahao Pang, Fengqing Zhu, Dong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.10227v1.pdf)  
  Keywords: gaussian splatting, compression, 3d gaussian, ar, fast, efficient  

### Quality Enhancement

*Showing the latest 50 out of 162 papers*

- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: gaussian splatting, relighting, illumination, lighting, nerf, 3d gaussian, geometry, ar, ray tracing, high-fidelity, reflection, face  
- **[Distilled-3DGS:Distilled 3D Gaussian Splatting](https://arxiv.org/abs/2508.14037v1)**  
  Authors: Lintao Xiang, Xinkai Chen, Jianhuang Lai, Guangcong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14037v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://distilled3dgs.github.io)  
  Keywords: gaussian splatting, 3d gaussian, ar, high-fidelity, lightweight  
- **[PhysGM: Large Physical Gaussian Model for Feed-Forward 4D Synthesis](https://arxiv.org/abs/2508.13911v1)**  
  Authors: Chunji Lv, Zequn Chen, Donglin Di, Weinan Zhang, Hao Li, Wei Chen, Changsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13911v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hihixiaolv.github.io/PhysGM.github.io/)  
  Keywords: gaussian splatting, 4d, 3d gaussian, ar, high-fidelity, face, motion  
- **[EAvatar: Expression-Aware Head Avatar Reconstruction with Generative
  Geometry Priors](https://arxiv.org/abs/2508.13537v1)**  
  Authors: Shikun Zhang, Cunjian Chen, Yiqun Wang, Qiuhong Ke, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13537v1.pdf)  
  Keywords: gaussian splatting, avatar, 3d gaussian, real-time rendering, geometry, head, ar, high-fidelity, vr, face, deformation  
- **[Improving Densification in 3D Gaussian Splatting for High-Fidelity
  Rendering](https://arxiv.org/abs/2508.12313v1)**  
  Authors: Xiaobin Deng, Changyu Diao, Min Li, Ruohan Yu, Duanqing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12313v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, head, ar, high-fidelity  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v1)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v1.pdf)  
  Keywords: gaussian splatting, semantic, lighting, nerf, 3d gaussian, segmentation, understanding, ar, high-fidelity, survey, compact  
- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event
  Cameras](https://arxiv.org/abs/2508.09912v1)**  
  Authors: Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09912v1.pdf)  
  Keywords: gaussian splatting, 4d, lighting, dynamic, ar, high-fidelity, fast, motion  
- **[EGS-SLAM: RGB-D Gaussian Splatting SLAM with Events](https://arxiv.org/abs/2508.07003v1)**  
  Authors: Siyu Chen, Shenghai Yuan, Thien-Minh Nguyen, Zhuyu Huang, Chenyang Shi, Jin Jing, Lihua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07003v1.pdf)  
  Keywords: slam, gaussian splatting, 3d reconstruction, dynamic, 3d gaussian, tracking, mapping, ar, high-fidelity, motion  
- **[GAP: Gaussianize Any Point Clouds with Text Guidance](https://arxiv.org/abs/2508.05631v1)**  
  Authors: Weiqi Zhang, Junsheng Zhou, Haotian Geng, Wenyuan Zhang, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05631v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weiqi-zhang.github.io/GAP.)  
  Keywords: gaussian splatting, 3d gaussian, ar, high-fidelity, fast, face  
- **[3DGabSplat: 3D Gabor Splatting for Frequency-adaptive Radiance Field
  Rendering](https://arxiv.org/abs/2508.05343v1)**  
  Authors: Junyu Zhou, Yuyang Huang, Wenrui Dai, Junni Zou, Ziyang Zheng, Nuowen Kan, Chenglin Li, Hongkai Xiong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05343v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, head, ar, high-fidelity, efficient  

### Ray Tracing

- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: gaussian splatting, relighting, illumination, lighting, nerf, 3d gaussian, geometry, ar, ray tracing, high-fidelity, reflection, face  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: gaussian splatting, relighting, illumination, lighting, dynamic, global illumination, 3d gaussian, relightable, shadow, outdoor, ar, face  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: gaussian splatting, lighting, dynamic, 3d gaussian, ar, face, path tracing  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: gaussian splatting, efficient rendering, relighting, lighting, 3d gaussian, ray marching, geometry, relightable, ar, efficient, face  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, ar, ray tracing, high-fidelity, efficient  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v2)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v2.pdf)  
  Keywords: gaussian splatting, relighting, avatar, lighting, geometry, relightable, ray tracing, fast, shadow, ar, human  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: gaussian splatting, efficient rendering, relighting, lighting, 3d gaussian, ar, ray tracing, acceleration, efficient  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: gaussian splatting, animation, dynamic, 3d gaussian, ray marching, ar, acceleration, efficient, compact  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: gaussian splatting, illumination, lighting, global illumination, 3d gaussian, real-time rendering, ar, ray tracing, efficient, face  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: gaussian splatting, neural rendering, 3d gaussian, shadow, ray tracing, fast, reflection, ar  

### Relighting

*Showing the latest 50 out of 113 papers*

- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: gaussian splatting, relighting, illumination, lighting, nerf, 3d gaussian, geometry, ar, ray tracing, high-fidelity, reflection, face  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: gaussian splatting, illumination, lighting, 3d reconstruction, 3d gaussian, outdoor, ar, understanding  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v1)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v1.pdf)  
  Keywords: gaussian splatting, semantic, lighting, nerf, 3d gaussian, segmentation, understanding, ar, high-fidelity, survey, compact  
- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event
  Cameras](https://arxiv.org/abs/2508.09912v1)**  
  Authors: Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09912v1.pdf)  
  Keywords: gaussian splatting, 4d, lighting, dynamic, ar, high-fidelity, fast, motion  
- **[HumanGenesis: Agent-Based Geometric and Generative Modeling for
  Synthetic Human Dynamics](https://arxiv.org/abs/2508.09858v1)**  
  Authors: Weiqi Li, Zehao Zhang, Liang Lin, Guangrun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09858v1.pdf)  
  Keywords: gaussian splatting, 4d, deformation, dynamic, 3d gaussian, ar, reflection, human, face, motion  
- **[Vision-Only Gaussian Splatting for Collaborative Semantic Occupancy
  Prediction](https://arxiv.org/abs/2508.10936v1)**  
  Authors: Cheng Chen, Hao Huang, Saurabh Bagchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.10936v1.pdf)  
  Keywords: gaussian splatting, lighting, geometry, ar, semantic  
- **[Touch-Augmented Gaussian Splatting for Enhanced 3D Scene Reconstruction](https://arxiv.org/abs/2508.07717v1)**  
  Authors: Yuchen Gao, Xiao Xu, Eckehard Steinbach, Daniel E. Lucani, Qi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07717v1.pdf)  
  Keywords: gaussian splatting, lighting, 3d gaussian, geometry, ar, face  
- **[UW-3DGS: Underwater 3D Reconstruction with Physics-Aware Gaussian
  Splatting](https://arxiv.org/abs/2508.06169v1)**  
  Authors: Wenpeng Xing, Jie Chen, Zaifeng Yang, Changting Lin, Jianfeng Dong, Chaochao Chen, Xun Zhou, Meng Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06169v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, nerf, 3d gaussian, light transport, geometry, ar, face  
- **[A 3DGS-Diffusion Self-Supervised Framework for Normal Estimation from a
  Single Image](https://arxiv.org/abs/2508.05950v1)**  
  Authors: Yanxing Liang, Yinghui Wang, Jinlong Yang, Wei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05950v1.pdf)  
  Keywords: gaussian splatting, light transport, 3d gaussian, mapping, ar, face  
- **[OCSplats: Observation Completeness Quantification and Label Noise
  Separation in 3DGS](https://arxiv.org/abs/2508.01239v1)**  
  Authors: Han Ling, Xian Xu, Yinghui Sun, Quansen Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.01239v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, dynamic, 3d gaussian, shadow, ar, face  

### SLAM

*Showing the latest 50 out of 152 papers*

- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, tracking, geometry, ar, compact, efficient, motion  
- **[Online 3D Gaussian Splatting Modeling with Novel View Selection](https://arxiv.org/abs/2508.14014v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14014v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, ar, outdoor  
- **[SAGOnline: Segment Any Gaussians Online](https://arxiv.org/abs/2508.08219v1)**  
  Authors: Wentao Sun, Quanyun Wu, Hanqing Xu, Kyle Gao, Zhengsen Xu, Yiping Chen, Dedong Zhang, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08219v1.pdf)  
  Keywords: gaussian splatting, nerf, 3d gaussian, real-time rendering, tracking, segmentation, ar, efficient, lightweight, vr, understanding  
- **[NeeCo: Image Synthesis of Novel Instrument States Based on Dynamic and
  Deformable 3D Gaussian Reconstruction](https://arxiv.org/abs/2508.07897v1)**  
  Authors: Tianle Zeng, Junlei Hu, Gerardo Loza Galindo, Sharib Ali, Duygu Sarikaya, Pietro Valdastri, Dominic Jones  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07897v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, tracking, motion, ar, localization, medical, deformation  
- **[EGS-SLAM: RGB-D Gaussian Splatting SLAM with Events](https://arxiv.org/abs/2508.07003v1)**  
  Authors: Siyu Chen, Shenghai Yuan, Thien-Minh Nguyen, Zhuyu Huang, Chenyang Shi, Jin Jing, Lihua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07003v1.pdf)  
  Keywords: slam, gaussian splatting, 3d reconstruction, dynamic, 3d gaussian, tracking, mapping, ar, high-fidelity, motion  
- **[A 3DGS-Diffusion Self-Supervised Framework for Normal Estimation from a
  Single Image](https://arxiv.org/abs/2508.05950v1)**  
  Authors: Yanxing Liang, Yinghui Wang, Jinlong Yang, Wei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05950v1.pdf)  
  Keywords: gaussian splatting, light transport, 3d gaussian, mapping, ar, face  
- **[Stereo 3D Gaussian Splatting SLAM for Outdoor Urban Scenes](https://arxiv.org/abs/2507.23677v1)**  
  Authors: Xiaohan Li, Ziren Gong, Fabio Tosi, Matteo Poggi, Stefano Mattoccia, Dong Liu, Jun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23677v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, tracking, urban scene, mapping, outdoor, high-fidelity, fast, ar  
- **[Gaussian Splatting Feature Fields for Privacy-Preserving Visual
  Localization](https://arxiv.org/abs/2507.23569v1)**  
  Authors: Maxime Pietrantoni, Gabriela Csurka, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23569v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, segmentation, ar, localization  
- **[MagicRoad: Semantic-Aware 3D Road Surface Reconstruction via Obstacle
  Inpainting](https://arxiv.org/abs/2507.23340v1)**  
  Authors: Xingyue Peng, Yuandong Lyu, Lang Zhang, Jian Zhu, Songtao Wang, Jiaxin Deng, Songxin Lu, Weiliang Ma, Dangen She, Peng Jia, XianPeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23340v1.pdf)  
  Keywords: gaussian splatting, semantic, lighting, dynamic, 3d gaussian, autonomous driving, segmentation, mapping, ar, efficient, face  
- **[GSFusion:Globally Optimized LiDAR-Inertial-Visual Mapping for Gaussian
  Splatting](https://arxiv.org/abs/2507.23273v1)**  
  Authors: Jaeseok Park, Chanoh Park, Minsu Kim, Soohwan Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23273v1.pdf)  
  Keywords: slam, gaussian splatting, illumination, 3d gaussian, mapping, ar, efficient  

### Scene Understanding

*Showing the latest 50 out of 199 papers*

- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: gaussian splatting, illumination, lighting, 3d reconstruction, 3d gaussian, outdoor, ar, understanding  
- **[GALA: Guided Attention with Language Alignment for Open Vocabulary
  Gaussian Splatting](https://arxiv.org/abs/2508.14278v2)**  
  Authors: Elena Alegret, Kunyi Li, Sen Wang, Siyun Liang, Michael Niemeyer, Stefano Gasperini, Nassir Navab, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14278v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, semantic, understanding  
- **[InnerGS: Internal Scenes Rendering via Factorized 3D Gaussian Splatting](https://arxiv.org/abs/2508.13287v1)**  
  Authors: Shuxin Liang, Yihan Xiao, Wenlu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13287v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, face, understanding  
- **[IntelliCap: Intelligent Guidance for Consistent View Sampling](https://arxiv.org/abs/2508.13043v1)**  
  Authors: Ayaka Yasunaga, Hideo Saito, Dieter Schmalstieg, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13043v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, segmentation, ar, human, semantic, understanding  
- **[Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.12720v1)**  
  Authors: Kangjie Chen, Yingji Zhong, Zhihao Li, Jiaqi Lin, Youyu Chen, Minghan Qin, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12720v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, sparse-view, ar, lightweight, understanding  
- **[InstDrive: Instance-Aware 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2508.12015v1)**  
  Authors: Hongyuan Liu, Haochen Yu, Jianfei Jiang, Qiankun Liu, Jiansheng Chen, Huimin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12015v1.pdf)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, autonomous driving, segmentation, outdoor, ar, lightweight, understanding  
- **[Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.11431v1)**  
  Authors: Simona Kocour, Assia Benbihi, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11431v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, geometry, outdoor, ar, semantic, face, understanding  
- **[Versatile Video Tokenization with Generative 2D Gaussian Splatting](https://arxiv.org/abs/2508.11183v1)**  
  Authors: Zhenghao Chen, Zicong Chen, Lei Liu, Yiming Wu, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11183v1.pdf)  
  Keywords: gaussian splatting, compression, dynamic, recognition, ar, compact  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v1)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v1.pdf)  
  Keywords: gaussian splatting, semantic, lighting, nerf, 3d gaussian, segmentation, understanding, ar, high-fidelity, survey, compact  
- **[GSFixer: Improving 3D Gaussian Splatting with Reference-Guided Video
  Diffusion Priors](https://arxiv.org/abs/2508.09667v1)**  
  Authors: Xingyilang Yin, Qi Zhang, Jiahao Chang, Ying Feng, Qingnan Fan, Xi Yang, Chi-Man Pun, Huaqi Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09667v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, geometry, sparse-view, ar, semantic, sparse view  



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