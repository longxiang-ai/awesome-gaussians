# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-08-30 00:47:30

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
- [Acceleration](#acceleration) (260 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (324 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (391 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (73 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (309 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (73 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (407 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (163 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (18 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (114 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (151 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (195 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: understanding, high-fidelity, nerf, semantic, compact, segmentation, lighting, gaussian splatting, survey, ar, 3d gaussian  
- **[A Study of the Framework and Real-World Applications of Language
  Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: understanding, robotics, nerf, semantic, gaussian splatting, survey, ar, efficient, 3d gaussian  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned
  and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: robotics, nerf, gaussian splatting, survey, ar, human, 3d gaussian  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: geometry, robotics, sparse-view, nerf, motion, gaussian splatting, survey, vr, ar, 3d reconstruction, 3d gaussian  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v2)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v2.pdf)  
  Keywords: fast, robotics, nerf, lighting, gaussian splatting, survey, dynamic, slam, vr, ar, human, 3d reconstruction, 3d gaussian  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: autonomous driving, high-fidelity, nerf, face, outdoor, gaussian splatting, survey, dynamic, ar, efficient, 3d gaussian  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: autonomous driving, robotics, high-fidelity, nerf, gaussian splatting, survey, vr, ar, 3d gaussian, 3d reconstruction, neural rendering  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: understanding, high-fidelity, semantic, segmentation, outdoor, gaussian splatting, survey, ar, 3d gaussian, 3d reconstruction, efficient, neural rendering  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: localization, nerf, semantic, mapping, segmentation, gaussian splatting, survey, slam, ar, efficient, 3d gaussian  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to
  Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: 4d, body, understanding, motion, gaussian splatting, survey, dynamic, ar, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 260 papers*

- **[MAPo : Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for
  High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2508.19786v1)**  
  Authors: Han Jiao, Jiakai Sun, Yexing Xu, Lei Zhao, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19786v1.pdf)  
  Keywords: high-fidelity, motion, deformation, gaussian splatting, dynamic, ar, 3d gaussian, fast  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: animation, high-fidelity, head, face, avatar, tracking, gaussian splatting, ar, 3d gaussian, fast  
- **[LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation](https://arxiv.org/abs/2508.19699v1)**  
  Authors: Yupeng Zhang, Dezhi Zheng, Ping Lu, Han Zhang, Lei Wang, Liping xiang, Cheng Luo, Kaijun Deng, Xiaowen Fu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19699v1.pdf)  
  Keywords: efficient rendering, understanding, high-fidelity, semantic, segmentation, gaussian splatting, ar, efficient, 3d gaussian  
- **[ColorGS: High-fidelity Surgical Scene Reconstruction with Colored
  Gaussian Splatting](https://arxiv.org/abs/2508.18696v1)**  
  Authors: Qun Ji, Peng Li, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18696v1.pdf)  
  Keywords: high-fidelity, nerf, motion, deformation, lighting, gaussian splatting, dynamic, vr, ar, 3d gaussian, efficient, real-time rendering  
- **[FastAvatar: Instant 3D Gaussian Splatting for Faces from Single
  Unconstrained Poses](https://arxiv.org/abs/2508.18389v1)**  
  Authors: Hao Liang, Zhixuan Ge, Ashish Tiwari, Soumendu Majee, G. M. Dilshan Godaliyadda, Ashok Veeraraghavan, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18389v1.pdf)  
  Keywords: face, avatar, gaussian splatting, ar, 3d gaussian, fast  
- **[Arbitrary-Scale 3D Gaussian Super-Resolution](https://arxiv.org/abs/2508.16467v1)**  
  Authors: Huimin Zeng, Yue Bai, Yun Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.16467v1.pdf)  
  Keywords: ar, gaussian splatting, real-time rendering, 3d gaussian  
- **[Image-Conditioned 3D Gaussian Splat Quantization](https://arxiv.org/abs/2508.15372v1)**  
  Authors: Xinshuang Liu, Runfa Blark Li, Keito Suzuki, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15372v1.pdf)  
  Keywords: head, gaussian splatting, ar, compression, 3d gaussian, real-time rendering  
- **[Pixie: Fast and Generalizable Supervised Learning of 3D Physics from
  Pixels](https://arxiv.org/abs/2508.17437v2)**  
  Authors: Long Le, Ryan Lucas, Chen Wang, Chuhao Chen, Dinesh Jayaraman, Eric Eaton, Lingjie Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17437v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pixie-3d.github.io/)  
  Keywords: ar, gaussian splatting, human, fast  
- **[EAvatar: Expression-Aware Head Avatar Reconstruction with Generative
  Geometry Priors](https://arxiv.org/abs/2508.13537v1)**  
  Authors: Shikun Zhang, Cunjian Chen, Yiqun Wang, Qiuhong Ke, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13537v1.pdf)  
  Keywords: geometry, high-fidelity, head, face, avatar, deformation, gaussian splatting, vr, ar, 3d gaussian, real-time rendering  
- **[Improving Densification in 3D Gaussian Splatting for High-Fidelity
  Rendering](https://arxiv.org/abs/2508.12313v1)**  
  Authors: Xiaobin Deng, Changyu Diao, Min Li, Ruohan Yu, Duanqing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12313v1.pdf)  
  Keywords: high-fidelity, head, gaussian splatting, ar, 3d gaussian, real-time rendering  

### Applications

*Showing the latest 50 out of 995 papers*

- **[${C}^{3}$-GS: Learning Context-aware, Cross-dimension, Cross-scale
  Feature for Generalizable Gaussian Splatting](https://arxiv.org/abs/2508.20754v1)**  
  Authors: Yuxi Hu, Jun Zhang, Kuangyi Chen, Zhe Zhang, Friedrich Fraundorfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20754v1.pdf)  
  Keywords: geometry, sparse view, lightweight, gaussian splatting, ar  
- **[AvatarBack: Back-Head Generation for Complete 3D Avatars from Front-View
  Images](https://arxiv.org/abs/2508.20623v1)**  
  Authors: Shiqi Xin, Xiaolin Zhang, Yanbin Liu, Peng Zhang, Caifeng Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20623v1.pdf)  
  Keywords: head, motion, avatar, gaussian splatting, ar, 3d gaussian  
- **[Realistic and Controllable 3D Gaussian-Guided Object Editing for Driving
  Video Generation](https://arxiv.org/abs/2508.20471v1)**  
  Authors: Jiusi Li, Jackson Jiang, Jinyu Miao, Miao Long, Tuopu Wen, Peijin Jia, Shengxiang Liu, Chunlei Yu, Maolin Liu, Yuzhan Cai, Kun Jiang, Mengmeng Yang, Diange Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20471v1.pdf)  
  Keywords: autonomous driving, ar, gaussian splatting, 3d gaussian  
- **[Seam360GS: Seamless 360° Gaussian Splatting from Real-World
  Omnidirectional Images](https://arxiv.org/abs/2508.20080v1)**  
  Authors: Changha Shin, Woong Oh Cho, Seon Joo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20080v1.pdf)  
  Keywords: ar, gaussian splatting, robotics, 3d gaussian  
- **[MAPo : Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for
  High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2508.19786v1)**  
  Authors: Han Jiao, Jiakai Sun, Yexing Xu, Lei Zhao, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19786v1.pdf)  
  Keywords: high-fidelity, motion, deformation, gaussian splatting, dynamic, ar, 3d gaussian, fast  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: animation, high-fidelity, head, face, avatar, tracking, gaussian splatting, ar, 3d gaussian, fast  
- **[LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation](https://arxiv.org/abs/2508.19699v1)**  
  Authors: Yupeng Zhang, Dezhi Zheng, Ping Lu, Han Zhang, Lei Wang, Liping xiang, Cheng Luo, Kaijun Deng, Xiaowen Fu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19699v1.pdf)  
  Keywords: efficient rendering, understanding, high-fidelity, semantic, segmentation, gaussian splatting, ar, efficient, 3d gaussian  
- **[Style4D-Bench: A Benchmark Suite for 4D Stylization](https://arxiv.org/abs/2508.19243v1)**  
  Authors: Beiqi Chen, Shuai Shao, Haitang Feng, Jianhuang Lai, Jianlou Si, Guangcong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19243v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://becky-catherine.github.io/Style4D)  
  Keywords: geometry, 4d, motion, lightweight, gaussian splatting, dynamic, ar  
- **[PseudoMapTrainer: Learning Online Mapping without HD Maps](https://arxiv.org/abs/2508.18788v1)**  
  Authors: Christian Löwens, Thorben Funke, Jingchao Xie, Alexandru Paul Condurache  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18788v1.pdf)  
  Keywords: semantic, face, mapping, segmentation, gaussian splatting, ar  
- **[ColorGS: High-fidelity Surgical Scene Reconstruction with Colored
  Gaussian Splatting](https://arxiv.org/abs/2508.18696v1)**  
  Authors: Qun Ji, Peng Li, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18696v1.pdf)  
  Keywords: high-fidelity, nerf, motion, deformation, lighting, gaussian splatting, dynamic, vr, ar, 3d gaussian, efficient, real-time rendering  

### Avatar Generation

*Showing the latest 50 out of 324 papers*

- **[AvatarBack: Back-Head Generation for Complete 3D Avatars from Front-View
  Images](https://arxiv.org/abs/2508.20623v1)**  
  Authors: Shiqi Xin, Xiaolin Zhang, Yanbin Liu, Peng Zhang, Caifeng Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20623v1.pdf)  
  Keywords: head, motion, avatar, gaussian splatting, ar, 3d gaussian  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: animation, high-fidelity, head, face, avatar, tracking, gaussian splatting, ar, 3d gaussian, fast  
- **[PseudoMapTrainer: Learning Online Mapping without HD Maps](https://arxiv.org/abs/2508.18788v1)**  
  Authors: Christian Löwens, Thorben Funke, Jingchao Xie, Alexandru Paul Condurache  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18788v1.pdf)  
  Keywords: semantic, face, mapping, segmentation, gaussian splatting, ar  
- **[FastAvatar: Instant 3D Gaussian Splatting for Faces from Single
  Unconstrained Poses](https://arxiv.org/abs/2508.18389v1)**  
  Authors: Hao Liang, Zhixuan Ge, Ashish Tiwari, Soumendu Majee, G. M. Dilshan Godaliyadda, Ashok Veeraraghavan, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18389v1.pdf)  
  Keywords: face, avatar, gaussian splatting, ar, 3d gaussian, fast  
- **[MeshSplat: Generalizable Sparse-View Surface Reconstruction via Gaussian
  Splatting](https://arxiv.org/abs/2508.17811v1)**  
  Authors: Hanzhi Chang, Ruijie Zhu, Wenjie Chang, Mulin Yu, Yanzhe Liang, Jiahao Lu, Zhuoyuan Li, Tianzhu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17811v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanzhichang.github.io/meshsplat_web)  
  Keywords: geometry, sparse-view, face, gaussian splatting, ar  
- **[Generating Human-AI Collaborative Design Sequence for 3D Assets via
  Differentiable Operation Graph](https://arxiv.org/abs/2508.17645v2)**  
  Authors: Xiaoyang Huang, Bingbing Ni, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17645v2.pdf)  
  Keywords: nerf, compact, gaussian splatting, ar, human  
- **[IDU: Incremental Dynamic Update of Existing 3D Virtual Environments with
  New Imagery Data](https://arxiv.org/abs/2508.17579v1)**  
  Authors: Meida Chen, Luis Leal, Yue Hu, Rong Liu, Butian Xiong, Andrew Feng, Jiuyi Xu, Yangming Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17579v1.pdf)  
  Keywords: gaussian splatting, dynamic, ar, human, 3d reconstruction, efficient, 3d gaussian  
- **[Image-Conditioned 3D Gaussian Splat Quantization](https://arxiv.org/abs/2508.15372v1)**  
  Authors: Xinshuang Liu, Runfa Blark Li, Keito Suzuki, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15372v1.pdf)  
  Keywords: head, gaussian splatting, ar, compression, 3d gaussian, real-time rendering  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v2)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v2.pdf)  
  Keywords: autonomous driving, geometry, sparse view, face, lighting, gaussian splatting, outdoor, relighting, ar, 3d gaussian  
- **[Pixie: Fast and Generalizable Supervised Learning of 3D Physics from
  Pixels](https://arxiv.org/abs/2508.17437v2)**  
  Authors: Long Le, Ryan Lucas, Chen Wang, Chuhao Chen, Dinesh Jayaraman, Eric Eaton, Lingjie Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17437v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pixie-3d.github.io/)  
  Keywords: ar, gaussian splatting, human, fast  

### Dynamic Scene

*Showing the latest 50 out of 391 papers*

- **[AvatarBack: Back-Head Generation for Complete 3D Avatars from Front-View
  Images](https://arxiv.org/abs/2508.20623v1)**  
  Authors: Shiqi Xin, Xiaolin Zhang, Yanbin Liu, Peng Zhang, Caifeng Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20623v1.pdf)  
  Keywords: head, motion, avatar, gaussian splatting, ar, 3d gaussian  
- **[MAPo : Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for
  High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2508.19786v1)**  
  Authors: Han Jiao, Jiakai Sun, Yexing Xu, Lei Zhao, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19786v1.pdf)  
  Keywords: high-fidelity, motion, deformation, gaussian splatting, dynamic, ar, 3d gaussian, fast  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: animation, high-fidelity, head, face, avatar, tracking, gaussian splatting, ar, 3d gaussian, fast  
- **[Style4D-Bench: A Benchmark Suite for 4D Stylization](https://arxiv.org/abs/2508.19243v1)**  
  Authors: Beiqi Chen, Shuai Shao, Haitang Feng, Jianhuang Lai, Jianlou Si, Guangcong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19243v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://becky-catherine.github.io/Style4D)  
  Keywords: geometry, 4d, motion, lightweight, gaussian splatting, dynamic, ar  
- **[ColorGS: High-fidelity Surgical Scene Reconstruction with Colored
  Gaussian Splatting](https://arxiv.org/abs/2508.18696v1)**  
  Authors: Qun Ji, Peng Li, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18696v1.pdf)  
  Keywords: high-fidelity, nerf, motion, deformation, lighting, gaussian splatting, dynamic, vr, ar, 3d gaussian, efficient, real-time rendering  
- **[IDU: Incremental Dynamic Update of Existing 3D Virtual Environments with
  New Imagery Data](https://arxiv.org/abs/2508.17579v1)**  
  Authors: Meida Chen, Luis Leal, Yue Hu, Rong Liu, Butian Xiong, Andrew Feng, Jiuyi Xu, Yangming Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17579v1.pdf)  
  Keywords: gaussian splatting, dynamic, ar, human, 3d reconstruction, efficient, 3d gaussian  
- **[Enhancing Novel View Synthesis from extremely sparse views with SfM-free
  3D Gaussian Splatting Framework](https://arxiv.org/abs/2508.15457v1)**  
  Authors: Zongqi He, Hanmin Li, Kin-Chung Chan, Yushen Zuo, Hao Xie, Zhe Xiao, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15457v1.pdf)  
  Keywords: geometry, sparse view, sparse-view, motion, gaussian splatting, ar, 3d gaussian  
- **[DriveSplat: Decoupled Driving Scene Reconstruction with
  Geometry-enhanced Partitioned Neural Gaussians](https://arxiv.org/abs/2508.15376v2)**  
  Authors: Cong Wang, Xianda Guo, Wenbo Xu, Wei Tian, Ruiqi Song, Chenming Zhang, Lingxi Li, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15376v2.pdf)  
  Keywords: geometry, motion, deformation, gaussian splatting, dynamic, ar, 3d gaussian  
- **[GeMS: Efficient Gaussian Splatting for Extreme Motion Blur](https://arxiv.org/abs/2508.14682v1)**  
  Authors: Gopi Raju Matta, Trisha Reddypalli, Vemunuri Divya Madhuri, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14682v1.pdf)  
  Keywords: motion, gaussian splatting, ar, efficient, 3d gaussian  
- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: geometry, motion, compact, tracking, gaussian splatting, ar, 3d reconstruction, efficient, 3d gaussian  

### Few-shot

*Showing the latest 50 out of 73 papers*

- **[${C}^{3}$-GS: Learning Context-aware, Cross-dimension, Cross-scale
  Feature for Generalizable Gaussian Splatting](https://arxiv.org/abs/2508.20754v1)**  
  Authors: Yuxi Hu, Jun Zhang, Kuangyi Chen, Zhe Zhang, Friedrich Fraundorfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20754v1.pdf)  
  Keywords: geometry, sparse view, lightweight, gaussian splatting, ar  
- **[MeshSplat: Generalizable Sparse-View Surface Reconstruction via Gaussian
  Splatting](https://arxiv.org/abs/2508.17811v1)**  
  Authors: Hanzhi Chang, Ruijie Zhu, Wenjie Chang, Mulin Yu, Yanzhe Liang, Jiahao Lu, Zhuoyuan Li, Tianzhu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17811v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanzhichang.github.io/meshsplat_web)  
  Keywords: geometry, sparse-view, face, gaussian splatting, ar  
- **[Enhancing Novel View Synthesis from extremely sparse views with SfM-free
  3D Gaussian Splatting Framework](https://arxiv.org/abs/2508.15457v1)**  
  Authors: Zongqi He, Hanmin Li, Kin-Chung Chan, Yushen Zuo, Hao Xie, Zhe Xiao, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15457v1.pdf)  
  Keywords: geometry, sparse view, sparse-view, motion, gaussian splatting, ar, 3d gaussian  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v2)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v2.pdf)  
  Keywords: autonomous driving, geometry, sparse view, face, lighting, gaussian splatting, outdoor, relighting, ar, 3d gaussian  
- **[Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.12720v2)**  
  Authors: Kangjie Chen, Yingji Zhong, Zhihao Li, Jiaqi Lin, Youyu Chen, Minghan Qin, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12720v2.pdf)  
  Keywords: understanding, sparse-view, lightweight, gaussian splatting, ar, 3d gaussian  
- **[Toward Human-Robot Teaming: Learning Handover Behaviors from 3D Scenes](https://arxiv.org/abs/2508.09855v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09855v1.pdf)  
  Keywords: gaussian splatting, human, sparse-view, ar  
- **[GSFixer: Improving 3D Gaussian Splatting with Reference-Guided Video
  Diffusion Priors](https://arxiv.org/abs/2508.09667v1)**  
  Authors: Xingyilang Yin, Qi Zhang, Jiahao Chang, Ying Feng, Qingnan Fan, Xi Yang, Chi-Man Pun, Huaqi Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09667v1.pdf)  
  Keywords: geometry, sparse view, sparse-view, semantic, gaussian splatting, ar, 3d reconstruction, 3d gaussian  
- **[SkySplat: Generalizable 3D Gaussian Splatting from Multi-Temporal Sparse
  Satellite Images](https://arxiv.org/abs/2508.09479v1)**  
  Authors: Xuejun Huang, Xinyi Liu, Yi Wan, Zhi Zheng, Bin Zhang, Mingtao Xiong, Yingying Pei, Yongjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09479v1.pdf)  
  Keywords: sparse-view, gaussian splatting, ar, efficient, 3d gaussian  
- **[DIP-GS: Deep Image Prior For Gaussian Splatting Sparse View Recovery](https://arxiv.org/abs/2508.07372v1)**  
  Authors: Rajaei Khatib, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07372v1.pdf)  
  Keywords: sparse view, sparse-view, gaussian splatting, ar, 3d gaussian, real-time rendering  
- **[UGOD: Uncertainty-Guided Differentiable Opacity and Soft Dropout for
  Enhanced Sparse-View 3DGS](https://arxiv.org/abs/2508.04968v1)**  
  Authors: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Liangxiu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04968v1.pdf)  
  Keywords: sparse-view, nerf, gaussian splatting, ar, 3d gaussian  

### Geometry Reconstruction

*Showing the latest 50 out of 309 papers*

- **[${C}^{3}$-GS: Learning Context-aware, Cross-dimension, Cross-scale
  Feature for Generalizable Gaussian Splatting](https://arxiv.org/abs/2508.20754v1)**  
  Authors: Yuxi Hu, Jun Zhang, Kuangyi Chen, Zhe Zhang, Friedrich Fraundorfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20754v1.pdf)  
  Keywords: geometry, sparse view, lightweight, gaussian splatting, ar  
- **[Style4D-Bench: A Benchmark Suite for 4D Stylization](https://arxiv.org/abs/2508.19243v1)**  
  Authors: Beiqi Chen, Shuai Shao, Haitang Feng, Jianhuang Lai, Jianlou Si, Guangcong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19243v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://becky-catherine.github.io/Style4D)  
  Keywords: geometry, 4d, motion, lightweight, gaussian splatting, dynamic, ar  
- **[Camera Pose Refinement via 3D Gaussian Splatting](https://arxiv.org/abs/2508.17876v1)**  
  Authors: Lulu Hao, Lipu Zhou, Zhenzhong Wei, Xu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17876v1.pdf)  
  Keywords: geometry, lightweight, gaussian splatting, ar, 3d gaussian  
- **[MeshSplat: Generalizable Sparse-View Surface Reconstruction via Gaussian
  Splatting](https://arxiv.org/abs/2508.17811v1)**  
  Authors: Hanzhi Chang, Ruijie Zhu, Wenjie Chang, Mulin Yu, Yanzhe Liang, Jiahao Lu, Zhuoyuan Li, Tianzhu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17811v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanzhichang.github.io/meshsplat_web)  
  Keywords: geometry, sparse-view, face, gaussian splatting, ar  
- **[IDU: Incremental Dynamic Update of Existing 3D Virtual Environments with
  New Imagery Data](https://arxiv.org/abs/2508.17579v1)**  
  Authors: Meida Chen, Luis Leal, Yue Hu, Rong Liu, Butian Xiong, Andrew Feng, Jiuyi Xu, Yangming Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17579v1.pdf)  
  Keywords: gaussian splatting, dynamic, ar, human, 3d reconstruction, efficient, 3d gaussian  
- **[UnPose: Uncertainty-Guided Diffusion Priors for Zero-Shot Pose
  Estimation](https://arxiv.org/abs/2508.15972v1)**  
  Authors: Zhaodong Jiang, Ashish Sinha, Tongtong Cao, Yuan Ren, Bingbing Liu, Binbin Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15972v1.pdf)  
  Keywords: geometry, robotics, gaussian splatting, ar, 3d reconstruction, 3d gaussian  
- **[Enhancing Novel View Synthesis from extremely sparse views with SfM-free
  3D Gaussian Splatting Framework](https://arxiv.org/abs/2508.15457v1)**  
  Authors: Zongqi He, Hanmin Li, Kin-Chung Chan, Yushen Zuo, Hao Xie, Zhe Xiao, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15457v1.pdf)  
  Keywords: geometry, sparse view, sparse-view, motion, gaussian splatting, ar, 3d gaussian  
- **[DriveSplat: Decoupled Driving Scene Reconstruction with
  Geometry-enhanced Partitioned Neural Gaussians](https://arxiv.org/abs/2508.15376v2)**  
  Authors: Cong Wang, Xianda Guo, Wenbo Xu, Wei Tian, Ruiqi Song, Chenming Zhang, Lingxi Li, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15376v2.pdf)  
  Keywords: geometry, motion, deformation, gaussian splatting, dynamic, ar, 3d gaussian  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v2)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v2.pdf)  
  Keywords: autonomous driving, geometry, sparse view, face, lighting, gaussian splatting, outdoor, relighting, ar, 3d gaussian  
- **[GSFix3D: Diffusion-Guided Repair of Novel Views in Gaussian Splatting](https://arxiv.org/abs/2508.14717v1)**  
  Authors: Jiaxin Wei, Stefan Leutenegger, Simon Schaefer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14717v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsfix3d.github.io.)  
  Keywords: ar, gaussian splatting, 3d reconstruction, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 73 papers*

- **[GSVisLoc: Generalizable Visual Localization for Gaussian Splatting Scene
  Representations](https://arxiv.org/abs/2508.18242v1)**  
  Authors: Fadi Khatib, Dror Moran, Guy Trostianetsky, Yoni Kasten, Meirav Galun, Ronen Basri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18242v1.pdf)  
  Keywords: outdoor, gaussian splatting, ar, 3d gaussian, localization  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v2)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v2.pdf)  
  Keywords: autonomous driving, geometry, sparse view, face, lighting, gaussian splatting, outdoor, relighting, ar, 3d gaussian  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: understanding, illumination, lighting, gaussian splatting, outdoor, ar, 3d reconstruction, 3d gaussian  
- **[Online 3D Gaussian Splatting Modeling with Novel View Selection](https://arxiv.org/abs/2508.14014v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14014v1.pdf)  
  Keywords: outdoor, gaussian splatting, slam, ar, 3d gaussian  
- **[InstDrive: Instance-Aware 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2508.12015v1)**  
  Authors: Hongyuan Liu, Haochen Yu, Jianfei Jiang, Qiankun Liu, Jiansheng Chen, Huimin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12015v1.pdf)  
  Keywords: autonomous driving, understanding, lightweight, segmentation, outdoor, gaussian splatting, dynamic, ar, 3d gaussian  
- **[Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.11431v1)**  
  Authors: Simona Kocour, Assia Benbihi, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11431v1.pdf)  
  Keywords: geometry, understanding, face, semantic, outdoor, gaussian splatting, ar, 3d reconstruction, 3d gaussian  
- **[Multi-view Normal and Distance Guidance Gaussian Splatting for Surface
  Reconstruction](https://arxiv.org/abs/2508.07701v2)**  
  Authors: Bo Jia, Yanan Guo, Ying Chang, Benkui Zhang, Ying Xie, Kangning Du, Lin Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07701v2.pdf)  
  Keywords: geometry, face, outdoor, gaussian splatting, ar, 3d gaussian  
- **[GS4Buildings: Prior-Guided Gaussian Splatting for 3D Building
  Reconstruction](https://arxiv.org/abs/2508.07355v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07355v1.pdf)  
  Keywords: geometry, urban scene, motion, face, semantic, compact, gaussian splatting, ar, 3d reconstruction, efficient  
- **[Evaluating Fisheye-Compatible 3D Gaussian Splatting Methods on Real
  Images Beyond 180 Degree Field of View](https://arxiv.org/abs/2508.06968v1)**  
  Authors: Ulas Gunes, Matias Turkulainen, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06968v1.pdf)  
  Keywords: outdoor, gaussian splatting, ar, 3d reconstruction, 3d gaussian  
- **[Neural Gaussian Radio Fields for Channel Estimation](https://arxiv.org/abs/2508.11668v1)**  
  Authors: Muhammad Umer, Muhammad Ahmed Mohsin, Ahsan Bilal, John M. Cioffi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11668v1.pdf)  
  Keywords: nerf, head, outdoor, gaussian splatting, dynamic, ar, efficient, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 407 papers*

- **[${C}^{3}$-GS: Learning Context-aware, Cross-dimension, Cross-scale
  Feature for Generalizable Gaussian Splatting](https://arxiv.org/abs/2508.20754v1)**  
  Authors: Yuxi Hu, Jun Zhang, Kuangyi Chen, Zhe Zhang, Friedrich Fraundorfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20754v1.pdf)  
  Keywords: geometry, sparse view, lightweight, gaussian splatting, ar  
- **[LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation](https://arxiv.org/abs/2508.19699v1)**  
  Authors: Yupeng Zhang, Dezhi Zheng, Ping Lu, Han Zhang, Lei Wang, Liping xiang, Cheng Luo, Kaijun Deng, Xiaowen Fu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19699v1.pdf)  
  Keywords: efficient rendering, understanding, high-fidelity, semantic, segmentation, gaussian splatting, ar, efficient, 3d gaussian  
- **[Style4D-Bench: A Benchmark Suite for 4D Stylization](https://arxiv.org/abs/2508.19243v1)**  
  Authors: Beiqi Chen, Shuai Shao, Haitang Feng, Jianhuang Lai, Jianlou Si, Guangcong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19243v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://becky-catherine.github.io/Style4D)  
  Keywords: geometry, 4d, motion, lightweight, gaussian splatting, dynamic, ar  
- **[ColorGS: High-fidelity Surgical Scene Reconstruction with Colored
  Gaussian Splatting](https://arxiv.org/abs/2508.18696v1)**  
  Authors: Qun Ji, Peng Li, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18696v1.pdf)  
  Keywords: high-fidelity, nerf, motion, deformation, lighting, gaussian splatting, dynamic, vr, ar, 3d gaussian, efficient, real-time rendering  
- **[Real-time 3D Visualization of Radiance Fields on Light Field Displays](https://arxiv.org/abs/2508.18540v1)**  
  Authors: Jonghyun Kim, Cheng Sun, Michael Stengel, Matthew Chan, Andrew Russell, Jaehyun Jung, Wil Braithwaite, Shalini De Mello, David Luebke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18540v1.pdf)  
  Keywords: high-fidelity, nerf, gaussian splatting, ar, efficient, 3d gaussian  
- **[Camera Pose Refinement via 3D Gaussian Splatting](https://arxiv.org/abs/2508.17876v1)**  
  Authors: Lulu Hao, Lipu Zhou, Zhenzhong Wei, Xu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17876v1.pdf)  
  Keywords: geometry, lightweight, gaussian splatting, ar, 3d gaussian  
- **[Generating Human-AI Collaborative Design Sequence for 3D Assets via
  Differentiable Operation Graph](https://arxiv.org/abs/2508.17645v2)**  
  Authors: Xiaoyang Huang, Bingbing Ni, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17645v2.pdf)  
  Keywords: nerf, compact, gaussian splatting, ar, human  
- **[IDU: Incremental Dynamic Update of Existing 3D Virtual Environments with
  New Imagery Data](https://arxiv.org/abs/2508.17579v1)**  
  Authors: Meida Chen, Luis Leal, Yue Hu, Rong Liu, Butian Xiong, Andrew Feng, Jiuyi Xu, Yangming Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17579v1.pdf)  
  Keywords: gaussian splatting, dynamic, ar, human, 3d reconstruction, efficient, 3d gaussian  
- **[Fiducial Marker Splatting for High-Fidelity Robotics Simulations](https://arxiv.org/abs/2508.17012v1)**  
  Authors: Diram Tabaa, Gianni Di Caro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17012v1.pdf)  
  Keywords: localization, robotics, high-fidelity, lighting, gaussian splatting, ar, efficient, neural rendering  
- **[Image-Conditioned 3D Gaussian Splat Quantization](https://arxiv.org/abs/2508.15372v1)**  
  Authors: Xinshuang Liu, Runfa Blark Li, Keito Suzuki, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15372v1.pdf)  
  Keywords: head, gaussian splatting, ar, compression, 3d gaussian, real-time rendering  

### Quality Enhancement

*Showing the latest 50 out of 163 papers*

- **[MAPo : Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for
  High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2508.19786v1)**  
  Authors: Han Jiao, Jiakai Sun, Yexing Xu, Lei Zhao, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19786v1.pdf)  
  Keywords: high-fidelity, motion, deformation, gaussian splatting, dynamic, ar, 3d gaussian, fast  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: animation, high-fidelity, head, face, avatar, tracking, gaussian splatting, ar, 3d gaussian, fast  
- **[LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation](https://arxiv.org/abs/2508.19699v1)**  
  Authors: Yupeng Zhang, Dezhi Zheng, Ping Lu, Han Zhang, Lei Wang, Liping xiang, Cheng Luo, Kaijun Deng, Xiaowen Fu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19699v1.pdf)  
  Keywords: efficient rendering, understanding, high-fidelity, semantic, segmentation, gaussian splatting, ar, efficient, 3d gaussian  
- **[ColorGS: High-fidelity Surgical Scene Reconstruction with Colored
  Gaussian Splatting](https://arxiv.org/abs/2508.18696v1)**  
  Authors: Qun Ji, Peng Li, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18696v1.pdf)  
  Keywords: high-fidelity, nerf, motion, deformation, lighting, gaussian splatting, dynamic, vr, ar, 3d gaussian, efficient, real-time rendering  
- **[Real-time 3D Visualization of Radiance Fields on Light Field Displays](https://arxiv.org/abs/2508.18540v1)**  
  Authors: Jonghyun Kim, Cheng Sun, Michael Stengel, Matthew Chan, Andrew Russell, Jaehyun Jung, Wil Braithwaite, Shalini De Mello, David Luebke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18540v1.pdf)  
  Keywords: high-fidelity, nerf, gaussian splatting, ar, efficient, 3d gaussian  
- **[Fiducial Marker Splatting for High-Fidelity Robotics Simulations](https://arxiv.org/abs/2508.17012v1)**  
  Authors: Diram Tabaa, Gianni Di Caro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17012v1.pdf)  
  Keywords: localization, robotics, high-fidelity, lighting, gaussian splatting, ar, efficient, neural rendering  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: geometry, high-fidelity, nerf, face, ray tracing, illumination, lighting, gaussian splatting, reflection, relighting, ar, 3d gaussian  
- **[Distilled-3DGS:Distilled 3D Gaussian Splatting](https://arxiv.org/abs/2508.14037v1)**  
  Authors: Lintao Xiang, Xinkai Chen, Jianhuang Lai, Guangcong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14037v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://distilled3dgs.github.io)  
  Keywords: high-fidelity, lightweight, gaussian splatting, ar, 3d gaussian  
- **[PhysGM: Large Physical Gaussian Model for Feed-Forward 4D Synthesis](https://arxiv.org/abs/2508.13911v1)**  
  Authors: Chunji Lv, Zequn Chen, Donglin Di, Weinan Zhang, Hao Li, Wei Chen, Changsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13911v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hihixiaolv.github.io/PhysGM.github.io/)  
  Keywords: 4d, high-fidelity, motion, face, gaussian splatting, ar, 3d gaussian  
- **[EAvatar: Expression-Aware Head Avatar Reconstruction with Generative
  Geometry Priors](https://arxiv.org/abs/2508.13537v1)**  
  Authors: Shikun Zhang, Cunjian Chen, Yiqun Wang, Qiuhong Ke, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13537v1.pdf)  
  Keywords: geometry, high-fidelity, head, face, avatar, deformation, gaussian splatting, vr, ar, 3d gaussian, real-time rendering  

### Ray Tracing

- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: geometry, high-fidelity, nerf, face, ray tracing, illumination, lighting, gaussian splatting, reflection, relighting, ar, 3d gaussian  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: shadow, face, relightable, illumination, global illumination, gaussian splatting, lighting, dynamic, outdoor, relighting, ar, 3d gaussian  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: face, lighting, gaussian splatting, dynamic, path tracing, ar, 3d gaussian  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: efficient rendering, geometry, face, ray marching, relightable, lighting, gaussian splatting, relighting, ar, efficient, 3d gaussian  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: high-fidelity, ray tracing, gaussian splatting, ar, efficient, real-time rendering  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v2)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v2.pdf)  
  Keywords: shadow, geometry, relightable, ray tracing, avatar, lighting, gaussian splatting, relighting, ar, human, fast  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: efficient rendering, ray tracing, lighting, gaussian splatting, acceleration, relighting, ar, efficient, 3d gaussian  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: animation, ray marching, compact, gaussian splatting, acceleration, dynamic, ar, efficient, 3d gaussian  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: face, ray tracing, illumination, global illumination, gaussian splatting, lighting, ar, 3d gaussian, efficient, real-time rendering  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: shadow, fast, ray tracing, reflection, gaussian splatting, ar, 3d gaussian, neural rendering  

### Relighting

*Showing the latest 50 out of 114 papers*

- **[ColorGS: High-fidelity Surgical Scene Reconstruction with Colored
  Gaussian Splatting](https://arxiv.org/abs/2508.18696v1)**  
  Authors: Qun Ji, Peng Li, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18696v1.pdf)  
  Keywords: high-fidelity, nerf, motion, deformation, lighting, gaussian splatting, dynamic, vr, ar, 3d gaussian, efficient, real-time rendering  
- **[Fiducial Marker Splatting for High-Fidelity Robotics Simulations](https://arxiv.org/abs/2508.17012v1)**  
  Authors: Diram Tabaa, Gianni Di Caro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17012v1.pdf)  
  Keywords: localization, robotics, high-fidelity, lighting, gaussian splatting, ar, efficient, neural rendering  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v2)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v2.pdf)  
  Keywords: autonomous driving, geometry, sparse view, face, lighting, gaussian splatting, outdoor, relighting, ar, 3d gaussian  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: geometry, high-fidelity, nerf, face, ray tracing, illumination, lighting, gaussian splatting, reflection, relighting, ar, 3d gaussian  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: understanding, illumination, lighting, gaussian splatting, outdoor, ar, 3d reconstruction, 3d gaussian  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: understanding, high-fidelity, nerf, semantic, compact, segmentation, lighting, gaussian splatting, survey, ar, 3d gaussian  
- **[HumanGenesis: Agent-Based Geometric and Generative Modeling for
  Synthetic Human Dynamics](https://arxiv.org/abs/2508.09858v1)**  
  Authors: Weiqi Li, Zehao Zhang, Liang Lin, Guangrun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09858v1.pdf)  
  Keywords: 4d, motion, face, deformation, reflection, gaussian splatting, dynamic, ar, human, 3d gaussian  
- **[Vision-Only Gaussian Splatting for Collaborative Semantic Occupancy
  Prediction](https://arxiv.org/abs/2508.10936v1)**  
  Authors: Cheng Chen, Hao Huang, Saurabh Bagchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.10936v1.pdf)  
  Keywords: geometry, semantic, lighting, gaussian splatting, ar  
- **[Touch-Augmented Gaussian Splatting for Enhanced 3D Scene Reconstruction](https://arxiv.org/abs/2508.07717v1)**  
  Authors: Yuchen Gao, Xiao Xu, Eckehard Steinbach, Daniel E. Lucani, Qi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07717v1.pdf)  
  Keywords: geometry, face, lighting, gaussian splatting, ar, 3d gaussian  
- **[UW-3DGS: Underwater 3D Reconstruction with Physics-Aware Gaussian
  Splatting](https://arxiv.org/abs/2508.06169v1)**  
  Authors: Wenpeng Xing, Jie Chen, Zaifeng Yang, Changting Lin, Jianfeng Dong, Chaochao Chen, Xun Zhou, Meng Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06169v1.pdf)  
  Keywords: geometry, light transport, nerf, face, gaussian splatting, ar, 3d reconstruction, 3d gaussian  

### SLAM

*Showing the latest 50 out of 151 papers*

- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: animation, high-fidelity, head, face, avatar, tracking, gaussian splatting, ar, 3d gaussian, fast  
- **[PseudoMapTrainer: Learning Online Mapping without HD Maps](https://arxiv.org/abs/2508.18788v1)**  
  Authors: Christian Löwens, Thorben Funke, Jingchao Xie, Alexandru Paul Condurache  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18788v1.pdf)  
  Keywords: semantic, face, mapping, segmentation, gaussian splatting, ar  
- **[GSVisLoc: Generalizable Visual Localization for Gaussian Splatting Scene
  Representations](https://arxiv.org/abs/2508.18242v1)**  
  Authors: Fadi Khatib, Dror Moran, Guy Trostianetsky, Yoni Kasten, Meirav Galun, Ronen Basri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18242v1.pdf)  
  Keywords: outdoor, gaussian splatting, ar, 3d gaussian, localization  
- **[Fiducial Marker Splatting for High-Fidelity Robotics Simulations](https://arxiv.org/abs/2508.17012v1)**  
  Authors: Diram Tabaa, Gianni Di Caro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17012v1.pdf)  
  Keywords: localization, robotics, high-fidelity, lighting, gaussian splatting, ar, efficient, neural rendering  
- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: geometry, motion, compact, tracking, gaussian splatting, ar, 3d reconstruction, efficient, 3d gaussian  
- **[Online 3D Gaussian Splatting Modeling with Novel View Selection](https://arxiv.org/abs/2508.14014v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14014v1.pdf)  
  Keywords: outdoor, gaussian splatting, slam, ar, 3d gaussian  
- **[SAGOnline: Segment Any Gaussians Online](https://arxiv.org/abs/2508.08219v1)**  
  Authors: Wentao Sun, Quanyun Wu, Hanqing Xu, Kyle Gao, Zhengsen Xu, Yiping Chen, Dedong Zhang, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08219v1.pdf)  
  Keywords: understanding, nerf, lightweight, tracking, segmentation, gaussian splatting, vr, ar, 3d gaussian, efficient, real-time rendering  
- **[NeeCo: Image Synthesis of Novel Instrument States Based on Dynamic and
  Deformable 3D Gaussian Reconstruction](https://arxiv.org/abs/2508.07897v1)**  
  Authors: Tianle Zeng, Junlei Hu, Gerardo Loza Galindo, Sharib Ali, Duygu Sarikaya, Pietro Valdastri, Dominic Jones  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07897v1.pdf)  
  Keywords: localization, medical, motion, tracking, deformation, gaussian splatting, dynamic, ar, 3d gaussian  
- **[EGS-SLAM: RGB-D Gaussian Splatting SLAM with Events](https://arxiv.org/abs/2508.07003v1)**  
  Authors: Siyu Chen, Shenghai Yuan, Thien-Minh Nguyen, Zhuyu Huang, Chenyang Shi, Jin Jing, Lihua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07003v1.pdf)  
  Keywords: high-fidelity, motion, tracking, mapping, gaussian splatting, dynamic, slam, ar, 3d reconstruction, 3d gaussian  
- **[A 3DGS-Diffusion Self-Supervised Framework for Normal Estimation from a
  Single Image](https://arxiv.org/abs/2508.05950v1)**  
  Authors: Yanxing Liang, Yinghui Wang, Jinlong Yang, Wei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05950v1.pdf)  
  Keywords: light transport, face, mapping, gaussian splatting, ar, 3d gaussian  

### Scene Understanding

*Showing the latest 50 out of 195 papers*

- **[LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation](https://arxiv.org/abs/2508.19699v1)**  
  Authors: Yupeng Zhang, Dezhi Zheng, Ping Lu, Han Zhang, Lei Wang, Liping xiang, Cheng Luo, Kaijun Deng, Xiaowen Fu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19699v1.pdf)  
  Keywords: efficient rendering, understanding, high-fidelity, semantic, segmentation, gaussian splatting, ar, efficient, 3d gaussian  
- **[PseudoMapTrainer: Learning Online Mapping without HD Maps](https://arxiv.org/abs/2508.18788v1)**  
  Authors: Christian Löwens, Thorben Funke, Jingchao Xie, Alexandru Paul Condurache  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18788v1.pdf)  
  Keywords: semantic, face, mapping, segmentation, gaussian splatting, ar  
- **[GWM: Towards Scalable Gaussian World Models for Robotic Manipulation](https://arxiv.org/abs/2508.17600v1)**  
  Authors: Guanxing Lu, Baoxiong Jia, Puhao Li, Yixin Chen, Ziwei Wang, Yansong Tang, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17600v1.pdf)  
  Keywords: gaussian splatting, understanding, ar  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: understanding, illumination, lighting, gaussian splatting, outdoor, ar, 3d reconstruction, 3d gaussian  
- **[GALA: Guided Attention with Language Alignment for Open Vocabulary
  Gaussian Splatting](https://arxiv.org/abs/2508.14278v2)**  
  Authors: Elena Alegret, Kunyi Li, Sen Wang, Siyun Liang, Michael Niemeyer, Stefano Gasperini, Nassir Navab, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14278v2.pdf)  
  Keywords: understanding, semantic, gaussian splatting, ar, 3d gaussian  
- **[InnerGS: Internal Scenes Rendering via Factorized 3D Gaussian Splatting](https://arxiv.org/abs/2508.13287v1)**  
  Authors: Shuxin Liang, Yihan Xiao, Wenlu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13287v1.pdf)  
  Keywords: understanding, face, gaussian splatting, ar, efficient, 3d gaussian  
- **[IntelliCap: Intelligent Guidance for Consistent View Sampling](https://arxiv.org/abs/2508.13043v1)**  
  Authors: Ayaka Yasunaga, Hideo Saito, Dieter Schmalstieg, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.13043v1.pdf)  
  Keywords: understanding, semantic, segmentation, gaussian splatting, ar, human, 3d gaussian  
- **[Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.12720v2)**  
  Authors: Kangjie Chen, Yingji Zhong, Zhihao Li, Jiaqi Lin, Youyu Chen, Minghan Qin, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12720v2.pdf)  
  Keywords: understanding, sparse-view, lightweight, gaussian splatting, ar, 3d gaussian  
- **[InstDrive: Instance-Aware 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2508.12015v1)**  
  Authors: Hongyuan Liu, Haochen Yu, Jianfei Jiang, Qiankun Liu, Jiansheng Chen, Huimin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12015v1.pdf)  
  Keywords: autonomous driving, understanding, lightweight, segmentation, outdoor, gaussian splatting, dynamic, ar, 3d gaussian  
- **[Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.11431v1)**  
  Authors: Simona Kocour, Assia Benbihi, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11431v1.pdf)  
  Keywords: geometry, understanding, face, semantic, outdoor, gaussian splatting, ar, 3d reconstruction, 3d gaussian  



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