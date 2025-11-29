# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-11-29 00:52:33

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

- [3DGS Surveys](#3dgs-surveys) (22 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (253 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (996 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (338 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (397 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (79 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (328 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (77 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (408 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (185 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (15 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (120 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (140 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (202 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: robotics, semantic, ar, slam, gaussian splatting, localization, efficient, 3d gaussian, survey, mapping, high-fidelity  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: ar, gaussian splatting, motion, 4d, nerf, 3d gaussian, fast, survey, geometry  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: real-time rendering, ar, animation, gaussian splatting, 3d reconstruction, lighting, efficient, 3d gaussian, avatar, survey, efficient rendering, face  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: ar, gaussian splatting, efficient, understanding, nerf, human, survey, lightweight  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: ar, slam, gaussian splatting, efficient, understanding, nerf, 3d gaussian, fast, survey, neural rendering  
- **[A-TDOM: Active TDOM via On-the-Fly 3DGS](https://arxiv.org/abs/2509.12759v2)**  
  Authors: Yiwei Xu, Xiang Wang, Yifei Yu, Wentian Gan, Luca Morelli, Giulio Perda, Xiongwu Xiao, Zongqian Zhan, Xin Wang, Fabio Remondino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.12759v2.pdf)  
  Keywords: ar, face, survey  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: compact, semantic, ar, gaussian splatting, lighting, segmentation, understanding, nerf, 3d gaussian, survey, high-fidelity  
- **[A Study of the Framework and Real-World Applications of Language Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: robotics, semantic, ar, gaussian splatting, efficient, understanding, nerf, 3d gaussian, survey  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: robotics, ar, gaussian splatting, nerf, 3d gaussian, human, survey  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: robotics, ar, gaussian splatting, 3d reconstruction, motion, nerf, 3d gaussian, survey, geometry, vr, sparse-view  

### Acceleration

*Showing the latest 50 out of 253 papers*

- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: semantic, ar, outdoor, gaussian splatting, fast, geometry  
- **[Alias-free 4D Gaussian Splatting](https://arxiv.org/abs/2511.18367v1)**  
  Authors: Zilong Chen, Huan-ang Gao, Delin Qu, Haohan Chi, Hao Tang, Kai Zhang, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18367v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4d-alias-free.github.io/4D-Alias-free/)  
  Keywords: real-time rendering, ar, gaussian splatting, 4d, dynamic  
- **[PEGS: Physics-Event Enhanced Large Spatiotemporal Motion Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2511.17116v1)**  
  Authors: Yijun Xu, Jingrui Zhang, Hongyi Liu, Yuhan Chen, Yuanyang Wang, Qingyao Guo, Dingwen Wang, Lei Yu, Chu He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17116v1.pdf)  
  Keywords: ar, gaussian splatting, motion, fast, dynamic, 3d gaussian, acceleration  
- **[One Walk is All You Need: Data-Efficient 3D RF Scene Reconstruction with Human Movements](https://arxiv.org/abs/2511.16966v1)**  
  Authors: Yiheng Bian, Zechen Li, Lanqing Yang, Hao Pan, Yezhou Wang, Longyuan Ge, Jeffery Wu, Ruiheng Liu, Yongjian Fu, Yichao chen, Guangtao xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16966v1.pdf)  
  Keywords: ar, gaussian splatting, motion, efficient, fast, 3d gaussian, dynamic, human, geometry, mapping, high-fidelity  
- **[Vorion: A RISC-V GPU with Hardware-Accelerated 3D Gaussian Rendering and Training](https://arxiv.org/abs/2511.16831v1)**  
  Authors: Yipeng Wang, Mengtian Yang, Chieh-pu Lo, Jaydeep P. Kulkarni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16831v1.pdf)  
  Keywords: real-time rendering, ar, gaussian splatting, 4d, 3d gaussian, neural rendering  
- **[Optimizing 3D Gaussian Splattering for Mobile GPUs](https://arxiv.org/abs/2511.16298v1)**  
  Authors: Md Musfiqur Rahman Sanim, Zhihao Shu, Bahram Afsharmanesh, AmirAli Mirian, Jiexiong Guan, Wei Niu, Bin Ren, Gagan Agrawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16298v1.pdf)  
  Keywords: ar, gaussian splatting, efficient, fast, 3d gaussian, mapping  
- **[Gaussian Blending: Rethinking Alpha Blending in 3D Gaussian Splatting](https://arxiv.org/abs/2511.15102v1)**  
  Authors: Junseo Koo, Jinseo Jeong, Gunhee Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.15102v1.pdf)  
  Keywords: real-time rendering, ar, 3d gaussian, gaussian splatting  
- **[IBGS: Image-Based Gaussian Splatting](https://arxiv.org/abs/2511.14357v1)**  
  Authors: Hoang Chuong Nguyen, Wei Mao, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14357v1.pdf)  
  Keywords: ar, gaussian splatting, head, efficient, fast, 3d gaussian, face  
- **[SF-Recon: Simplification-Free Lightweight Building Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2511.13278v2)**  
  Authors: Zihan Li, Tengfei Wang, Wentian Gan, Hao Zhan, Xin Wang, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13278v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lzh282140127-cell.github.io/SF-Recon-project/)  
  Keywords: ar, gaussian splatting, fast, 3d gaussian, geometry, face, lightweight  
- **[Neo: Real-Time On-Device 3D Gaussian Splatting with Reuse-and-Update Sorting Acceleration](https://arxiv.org/abs/2511.12930v1)**  
  Authors: Changhun Oh, Seongryong Oh, Jinwoo Hwang, Yoonsung Kim, Hardik Sharma, Jongse Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12930v1.pdf)  
  Keywords: ar, gaussian splatting, efficient, 3d gaussian, acceleration, tracking, vr  

### Applications

*Showing the latest 50 out of 996 papers*

- **[Resolution Where It Counts: Hash-based GPU-Accelerated 3D Reconstruction via Variance-Adaptive Voxel Grids](https://arxiv.org/abs/2511.21459v1)**  
  Authors: Lorenzo De Rebotti, Emanuele Giacomini, Giorgio Grisetti, Luca Di Giammarino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21459v1.pdf)  
  Keywords: ar, gaussian splatting, 3d reconstruction, head, efficient, dynamic, face  
- **[Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes](https://arxiv.org/abs/2511.21367v1)**  
  Authors: Yangle Liu, Fengze Li, Kan Liu, Jieming Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21367v1.pdf)  
  Keywords: ar, gaussian splatting, motion, 4d, nerf, dynamic, geometry, lightweight, reflection  
- **[Unlocking Zero-shot Potential of Semi-dense Image Matching via Gaussian Splatting](https://arxiv.org/abs/2511.21265v1)**  
  Authors: Juncheng Chen, Chao Xu, Yanjun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21265v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry, high-fidelity  
- **[GS-Checker: Tampering Localization for 3D Gaussian Splatting](https://arxiv.org/abs/2511.20354v1)**  
  Authors: Haoliang Han, Ziyuan Luo, Jun Qi, Anderson Rocha, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20354v1.pdf)  
  Keywords: localization, ar, 3d gaussian, gaussian splatting  
- **[Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v1)**  
  Authors: João Malheiro Silva, Andy Huynh, Tong Duy Son, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20348v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, 3d reconstruction, 3d gaussian, geometry, face  
- **[GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861v1)**  
  Authors: GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu, Kerui Li, Mengyuan Xu, Qiuping Deng, Siting Wang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yankai Wang, Yu Cao, Yifan Chang, Yuan Xu, Yun Ye, Yang Wang, Yukun Zhou, Zhengyuan Zhang, Zhehao Dong, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19861v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, motion, efficient, 3d gaussian  
- **[STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction](https://arxiv.org/abs/2511.19854v1)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Zidu Wang, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19854v1.pdf)  
  Keywords: deformation, ar, gaussian splatting, motion, head, dynamic, 3d gaussian, avatar, high-fidelity  
- **[DensifyBeforehand: LiDAR-assisted Content-aware Densification for Efficient and Quality 3D Gaussian Splatting](https://arxiv.org/abs/2511.19294v1)**  
  Authors: Phurtivilai Patt, Leyang Huang, Yinqiang Zhang, Yang Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19294v1.pdf)  
  Keywords: ar, semantic, gaussian splatting, efficient, 3d gaussian  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: ar, gaussian splatting, motion, autonomous driving, dynamic, 3d gaussian, human, tracking, high-fidelity  
- **[NVGS: Neural Visibility for Occlusion Culling in 3D Gaussian Splatting](https://arxiv.org/abs/2511.19202v1)**  
  Authors: Brent Zoomers, Florian Hahlbohm, Joni Vanherck, Lode Jorissen, Marcus Magnor, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19202v1.pdf)  
  Keywords: ar, gaussian splatting, efficient, 3d gaussian, vr  

### Avatar Generation

*Showing the latest 50 out of 338 papers*

- **[Resolution Where It Counts: Hash-based GPU-Accelerated 3D Reconstruction via Variance-Adaptive Voxel Grids](https://arxiv.org/abs/2511.21459v1)**  
  Authors: Lorenzo De Rebotti, Emanuele Giacomini, Giorgio Grisetti, Luca Di Giammarino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21459v1.pdf)  
  Keywords: ar, gaussian splatting, 3d reconstruction, head, efficient, dynamic, face  
- **[Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v1)**  
  Authors: João Malheiro Silva, Andy Huynh, Tong Duy Son, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20348v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, 3d reconstruction, 3d gaussian, geometry, face  
- **[STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction](https://arxiv.org/abs/2511.19854v1)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Zidu Wang, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19854v1.pdf)  
  Keywords: deformation, ar, gaussian splatting, motion, head, dynamic, 3d gaussian, avatar, high-fidelity  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: ar, gaussian splatting, motion, autonomous driving, dynamic, 3d gaussian, human, tracking, high-fidelity  
- **[Proxy-Free Gaussian Splats Deformation with Splat-Based Surface Estimation](https://arxiv.org/abs/2511.19542v1)**  
  Authors: Jaeyeong Kim, Seungwoo Yoo, Minhyuk Sung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19542v1.pdf)  
  Keywords: deformation, ar, head, nerf, face  
- **[AEGIS: Preserving privacy of 3D Facial Avatars with Adversarial Perturbations](https://arxiv.org/abs/2511.17747v1)**  
  Authors: Dawid Wolkiewicz, Anastasiya Pechko, Przemysław Spurek, Piotr Syga  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17747v1.pdf)  
  Keywords: ar, gaussian splatting, motion, efficient, dynamic, 3d gaussian, avatar, geometry, face  
- **[Towards Generative Design Using Optimal Transport for Shape Exploration and Solution Field Interpolation](https://arxiv.org/abs/2511.17111v1)**  
  Authors: Sergio Torregrosa, David Munoz, Hector Navarro, Charbel Farhat, Francisco Chinesta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17111v1.pdf)  
  Keywords: ar, face, efficient, gaussian splatting  
- **[SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting](https://arxiv.org/abs/2511.17092v2)**  
  Authors: Di Wu, Liu Liu, Xueyu Yuan, Qiaojun Yu, Wenxiao Chen, Ruilong Yan, Yiming Tang, Liangtu Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17092v2.pdf)  
  Keywords: sparse view, ar, gaussian splatting, 3d reconstruction, segmentation, 3d gaussian, face, few-shot, sparse-view  
- **[REArtGS++: Generalizable Articulation Reconstruction with Temporal Geometry Constraint via Planar Gaussian Splatting](https://arxiv.org/abs/2511.17059v2)**  
  Authors: Di Wu, Liu Liu, Anran Huang, Yuyan Liu, Qiaojun Yu, Shaofan Liu, Liangtu Song, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17059v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sites.google.com/view/reartgs2/home.)  
  Keywords: ar, gaussian splatting, motion, geometry, face  
- **[PhysMorph-GS: Differentiable Shape Morphing via Joint Optimization of Physics and Rendering Objectives](https://arxiv.org/abs/2511.16988v1)**  
  Authors: Chang-Yong Song, David Hyde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16988v1.pdf)  
  Keywords: compact, deformation, ar, gaussian splatting, 3d gaussian, mapping, face  

### Dynamic Scene

*Showing the latest 50 out of 397 papers*

- **[Resolution Where It Counts: Hash-based GPU-Accelerated 3D Reconstruction via Variance-Adaptive Voxel Grids](https://arxiv.org/abs/2511.21459v1)**  
  Authors: Lorenzo De Rebotti, Emanuele Giacomini, Giorgio Grisetti, Luca Di Giammarino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21459v1.pdf)  
  Keywords: ar, gaussian splatting, 3d reconstruction, head, efficient, dynamic, face  
- **[Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes](https://arxiv.org/abs/2511.21367v1)**  
  Authors: Yangle Liu, Fengze Li, Kan Liu, Jieming Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21367v1.pdf)  
  Keywords: ar, gaussian splatting, motion, 4d, nerf, dynamic, geometry, lightweight, reflection  
- **[GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861v1)**  
  Authors: GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu, Kerui Li, Mengyuan Xu, Qiuping Deng, Siting Wang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yankai Wang, Yu Cao, Yifan Chang, Yuan Xu, Yun Ye, Yang Wang, Yukun Zhou, Zhengyuan Zhang, Zhehao Dong, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19861v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, motion, efficient, 3d gaussian  
- **[STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction](https://arxiv.org/abs/2511.19854v1)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Zidu Wang, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19854v1.pdf)  
  Keywords: deformation, ar, gaussian splatting, motion, head, dynamic, 3d gaussian, avatar, high-fidelity  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: ar, gaussian splatting, motion, autonomous driving, dynamic, 3d gaussian, human, tracking, high-fidelity  
- **[Proxy-Free Gaussian Splats Deformation with Splat-Based Surface Estimation](https://arxiv.org/abs/2511.19542v1)**  
  Authors: Jaeyeong Kim, Seungwoo Yoo, Minhyuk Sung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19542v1.pdf)  
  Keywords: deformation, ar, head, nerf, face  
- **[Neural Texture Splatting: Expressive 3D Gaussian Splatting for View Synthesis, Geometry, and Dynamic Reconstruction](https://arxiv.org/abs/2511.18873v1)**  
  Authors: Yiming Wang, Shaofei Wang, Marko Mihajlovic, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18873v1.pdf)  
  Keywords: ar, gaussian splatting, 4d, efficient, dynamic, 3d gaussian, geometry  
- **[Alias-free 4D Gaussian Splatting](https://arxiv.org/abs/2511.18367v1)**  
  Authors: Zilong Chen, Huan-ang Gao, Delin Qu, Haohan Chi, Hao Tang, Kai Zhang, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18367v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4d-alias-free.github.io/4D-Alias-free/)  
  Keywords: real-time rendering, ar, gaussian splatting, 4d, dynamic  
- **[Observer Actor: Active Vision Imitation Learning with Sparse View Gaussian Splatting](https://arxiv.org/abs/2511.18140v1)**  
  Authors: Yilong Wang, Cheng Qian, Ruomeng Fan, Edward Johns  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18140v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://obact.github.io.)  
  Keywords: sparse view, ar, gaussian splatting, dynamic, 3d gaussian  
- **[CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation](https://arxiv.org/abs/2511.17904v1)**  
  Authors: Yuhang Ming, Chenxin Fang, Xingyuan Yu, Fan Zhang, Weichen Dai, Wanzeng Kong, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17904v1.pdf)  
  Keywords: compact, semantic, ar, gaussian splatting, lighting, understanding, dynamic, geometry  

### Few-shot

*Showing the latest 50 out of 79 papers*

- **[Observer Actor: Active Vision Imitation Learning with Sparse View Gaussian Splatting](https://arxiv.org/abs/2511.18140v1)**  
  Authors: Yilong Wang, Cheng Qian, Ruomeng Fan, Edward Johns  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18140v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://obact.github.io.)  
  Keywords: sparse view, ar, gaussian splatting, dynamic, 3d gaussian  
- **[Frequency-Adaptive Sharpness Regularization for Improving 3D Gaussian Splatting Generalization](https://arxiv.org/abs/2511.17918v1)**  
  Authors: Youngsik Yun, Dongjun Gu, Youngjung Uh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bbangsik13.github.io/FASR.)  
  Keywords: ar, 3d gaussian, few-shot, gaussian splatting  
- **[SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting](https://arxiv.org/abs/2511.17092v2)**  
  Authors: Di Wu, Liu Liu, Xueyu Yuan, Qiaojun Yu, Wenxiao Chen, Ruilong Yan, Yiming Tang, Liangtu Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17092v2.pdf)  
  Keywords: sparse view, ar, gaussian splatting, 3d reconstruction, segmentation, 3d gaussian, face, few-shot, sparse-view  
- **[CuriGS: Curriculum-Guided Gaussian Splatting for Sparse View Synthesis](https://arxiv.org/abs/2511.16030v1)**  
  Authors: Zijian Wu, Mingfeng Jiang, Zidian Lin, Ying Song, Hanjie Ma, Qun Wu, Dongping Zhang, Guiyang Pu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16030v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zijian1026.github.io/CuriGS/)  
  Keywords: sparse view, ar, gaussian splatting, 3d reconstruction, efficient, 3d gaussian, high-fidelity, sparse-view  
- **[SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2511.14633v1)**  
  Authors: Meiying Gu, Jiawei Zhang, Jiahe Li, Xiaohan Yu, Haonan Luo, Jin Zheng, Xiao Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14633v1.pdf)  
  Keywords: ar, gaussian splatting, efficient, nerf, 3d gaussian, geometry, face, sparse-view  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: compact, illumination, ar, gaussian splatting, 3d reconstruction, 3d gaussian, geometry, face, high-fidelity, sparse-view  
- **[RoboTidy : A 3D Gaussian Splatting Household Tidying Benchmark for Embodied Navigation and Action](https://arxiv.org/abs/2511.14161v2)**  
  Authors: Xiaoquan Sun, Ruijian Zhang, Kang Pang, Bingchen Miao, Yuxiang Tan, Zhen Yang, Ming Li, Jiayu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14161v2.pdf)  
  Keywords: ar, 3d gaussian, few-shot, gaussian splatting  
- **[SplatSearch: Instance Image Goal Navigation for Mobile Robots using 3D Gaussian Splatting and Diffusion Models](https://arxiv.org/abs/2511.12972v1)**  
  Authors: Siddarth Narasimhan, Matthew Lisondra, Haitong Wang, Goldie Nejat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12972v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, 3d gaussian, sparse-view  
- **[RealisticDreamer: Guidance Score Distillation for Few-shot Gaussian Splatting](https://arxiv.org/abs/2511.11213v1)**  
  Authors: Ruocheng Wu, Haolan He, Yufei Wang, Zhihao Li, Bihan Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.11213v1.pdf)  
  Keywords: real-time rendering, semantic, ar, gaussian splatting, motion, 3d gaussian, geometry, few-shot  
- **[Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction](https://arxiv.org/abs/2511.07122v1)**  
  Authors: Changyue Shi, Chuxiao Yang, Xinyuan Hu, Minghao Chen, Wenwen Pan, Yan Yang, Jiajun Ding, Zhou Yu, Jun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07122v1.pdf)  
  Keywords: deformation, ar, gaussian splatting, 4d, nerf, dynamic, few-shot  

### Geometry Reconstruction

*Showing the latest 50 out of 328 papers*

- **[Resolution Where It Counts: Hash-based GPU-Accelerated 3D Reconstruction via Variance-Adaptive Voxel Grids](https://arxiv.org/abs/2511.21459v1)**  
  Authors: Lorenzo De Rebotti, Emanuele Giacomini, Giorgio Grisetti, Luca Di Giammarino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21459v1.pdf)  
  Keywords: ar, gaussian splatting, 3d reconstruction, head, efficient, dynamic, face  
- **[Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes](https://arxiv.org/abs/2511.21367v1)**  
  Authors: Yangle Liu, Fengze Li, Kan Liu, Jieming Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21367v1.pdf)  
  Keywords: ar, gaussian splatting, motion, 4d, nerf, dynamic, geometry, lightweight, reflection  
- **[Unlocking Zero-shot Potential of Semi-dense Image Matching via Gaussian Splatting](https://arxiv.org/abs/2511.21265v1)**  
  Authors: Juncheng Chen, Chao Xu, Yanjun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21265v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry, high-fidelity  
- **[Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v1)**  
  Authors: João Malheiro Silva, Andy Huynh, Tong Duy Son, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20348v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, 3d reconstruction, 3d gaussian, geometry, face  
- **[MetroGS: Efficient and Stable Reconstruction of Geometrically Accurate High-Fidelity Large-Scale Scenes](https://arxiv.org/abs/2511.19172v1)**  
  Authors: Kehua Chen, Tianlu Mao, Zhuxin Ma, Hao Jiang, Zehao Li, Zihan Liu, Shuqi Gao, Honglong Zhao, Feng Dai, Yucheng Zhang, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19172v1.pdf)  
  Keywords: ar, gaussian splatting, efficient, 3d gaussian, geometry, high-fidelity  
- **[Neural Texture Splatting: Expressive 3D Gaussian Splatting for View Synthesis, Geometry, and Dynamic Reconstruction](https://arxiv.org/abs/2511.18873v1)**  
  Authors: Yiming Wang, Shaofei Wang, Marko Mihajlovic, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18873v1.pdf)  
  Keywords: ar, gaussian splatting, 4d, efficient, dynamic, 3d gaussian, geometry  
- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: ar, outdoor, gaussian splatting, 3d reconstruction, understanding, 3d gaussian, geometry  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: semantic, ar, outdoor, gaussian splatting, fast, geometry  
- **[SegSplat: Feed-forward Gaussian Splatting and Open-Set Semantic Segmentation](https://arxiv.org/abs/2511.18386v1)**  
  Authors: Peter Siegel, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18386v1.pdf)  
  Keywords: compact, semantic, ar, gaussian splatting, 3d reconstruction, efficient, segmentation, understanding, 3d gaussian  
- **[Novel View Synthesis from A Few Glimpses via Test-Time Natural Video Completion](https://arxiv.org/abs/2511.17932v1)**  
  Authors: Yan Xu, Yixing Wang, Stella X. Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17932v1.pdf)  
  Keywords: ar, gaussian splatting, nerf, 3d gaussian, geometry, high-fidelity  

### Large Scene

*Showing the latest 50 out of 77 papers*

- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: ar, outdoor, gaussian splatting, 3d reconstruction, understanding, 3d gaussian, geometry  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: semantic, ar, outdoor, gaussian splatting, fast, geometry  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: illumination, semantic, ar, outdoor, gaussian splatting, lighting, efficient, segmentation, relighting, geometry, face, high-fidelity  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: ar, outdoor, gaussian splatting, 3d gaussian, geometry, high-fidelity  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: urban scene, ar, gaussian splatting, autonomous driving, 4d, dynamic, human  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: ar, large scene, gaussian splatting, head, fast, 3d gaussian  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: ar, outdoor, gaussian splatting, motion, slam, understanding, 3d gaussian, geometry, mapping  
- **[D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction](https://arxiv.org/abs/2510.25173v2)**  
  Authors: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25173v2.pdf)  
  Keywords: urban scene, ar, gaussian splatting, autonomous driving, geometry  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: urban scene, semantic, ar, gaussian splatting, 3d reconstruction, face  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/2510.22669v1)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22669v1.pdf)  
  Keywords: ar, outdoor, gaussian splatting, slam, segmentation, dynamic, 3d gaussian, human, mapping, high-fidelity  

### Model Compression

*Showing the latest 50 out of 408 papers*

- **[Resolution Where It Counts: Hash-based GPU-Accelerated 3D Reconstruction via Variance-Adaptive Voxel Grids](https://arxiv.org/abs/2511.21459v1)**  
  Authors: Lorenzo De Rebotti, Emanuele Giacomini, Giorgio Grisetti, Luca Di Giammarino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21459v1.pdf)  
  Keywords: ar, gaussian splatting, 3d reconstruction, head, efficient, dynamic, face  
- **[Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes](https://arxiv.org/abs/2511.21367v1)**  
  Authors: Yangle Liu, Fengze Li, Kan Liu, Jieming Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21367v1.pdf)  
  Keywords: ar, gaussian splatting, motion, 4d, nerf, dynamic, geometry, lightweight, reflection  
- **[GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861v1)**  
  Authors: GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu, Kerui Li, Mengyuan Xu, Qiuping Deng, Siting Wang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yankai Wang, Yu Cao, Yifan Chang, Yuan Xu, Yun Ye, Yang Wang, Yukun Zhou, Zhengyuan Zhang, Zhehao Dong, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19861v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, motion, efficient, 3d gaussian  
- **[DensifyBeforehand: LiDAR-assisted Content-aware Densification for Efficient and Quality 3D Gaussian Splatting](https://arxiv.org/abs/2511.19294v1)**  
  Authors: Phurtivilai Patt, Leyang Huang, Yinqiang Zhang, Yang Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19294v1.pdf)  
  Keywords: ar, semantic, gaussian splatting, efficient, 3d gaussian  
- **[NVGS: Neural Visibility for Occlusion Culling in 3D Gaussian Splatting](https://arxiv.org/abs/2511.19202v1)**  
  Authors: Brent Zoomers, Florian Hahlbohm, Joni Vanherck, Lode Jorissen, Marcus Magnor, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19202v1.pdf)  
  Keywords: ar, gaussian splatting, efficient, 3d gaussian, vr  
- **[MetroGS: Efficient and Stable Reconstruction of Geometrically Accurate High-Fidelity Large-Scale Scenes](https://arxiv.org/abs/2511.19172v1)**  
  Authors: Kehua Chen, Tianlu Mao, Zhuxin Ma, Hao Jiang, Zehao Li, Zihan Liu, Shuqi Gao, Honglong Zhao, Feng Dai, Yucheng Zhang, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19172v1.pdf)  
  Keywords: ar, gaussian splatting, efficient, 3d gaussian, geometry, high-fidelity  
- **[Neural Texture Splatting: Expressive 3D Gaussian Splatting for View Synthesis, Geometry, and Dynamic Reconstruction](https://arxiv.org/abs/2511.18873v1)**  
  Authors: Yiming Wang, Shaofei Wang, Marko Mihajlovic, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18873v1.pdf)  
  Keywords: ar, gaussian splatting, 4d, efficient, dynamic, 3d gaussian, geometry  
- **[Splatonic: Architecture Support for 3D Gaussian Splatting SLAM via Sparse Processing](https://arxiv.org/abs/2511.18755v1)**  
  Authors: Xiaotong Huang, He Zhu, Tianrui Ma, Yuxiang Xiong, Fangxin Liu, Zhezhi He, Yiming Gan, Zihan Liu, Jingwen Leng, Yu Feng, Minyi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18755v1.pdf)  
  Keywords: ar, slam, gaussian splatting, efficient, 3d gaussian, tracking, high-fidelity  
- **[SegSplat: Feed-forward Gaussian Splatting and Open-Set Semantic Segmentation](https://arxiv.org/abs/2511.18386v1)**  
  Authors: Peter Siegel, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18386v1.pdf)  
  Keywords: compact, semantic, ar, gaussian splatting, 3d reconstruction, efficient, segmentation, understanding, 3d gaussian  
- **[CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation](https://arxiv.org/abs/2511.17904v1)**  
  Authors: Yuhang Ming, Chenxin Fang, Xingyuan Yu, Fan Zhang, Weichen Dai, Wanzeng Kong, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17904v1.pdf)  
  Keywords: compact, semantic, ar, gaussian splatting, lighting, understanding, dynamic, geometry  

### Quality Enhancement

*Showing the latest 50 out of 185 papers*

- **[Unlocking Zero-shot Potential of Semi-dense Image Matching via Gaussian Splatting](https://arxiv.org/abs/2511.21265v1)**  
  Authors: Juncheng Chen, Chao Xu, Yanjun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21265v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry, high-fidelity  
- **[STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction](https://arxiv.org/abs/2511.19854v1)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Zidu Wang, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19854v1.pdf)  
  Keywords: deformation, ar, gaussian splatting, motion, head, dynamic, 3d gaussian, avatar, high-fidelity  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: ar, gaussian splatting, motion, autonomous driving, dynamic, 3d gaussian, human, tracking, high-fidelity  
- **[MetroGS: Efficient and Stable Reconstruction of Geometrically Accurate High-Fidelity Large-Scale Scenes](https://arxiv.org/abs/2511.19172v1)**  
  Authors: Kehua Chen, Tianlu Mao, Zhuxin Ma, Hao Jiang, Zehao Li, Zihan Liu, Shuqi Gao, Honglong Zhao, Feng Dai, Yucheng Zhang, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19172v1.pdf)  
  Keywords: ar, gaussian splatting, efficient, 3d gaussian, geometry, high-fidelity  
- **[Splatonic: Architecture Support for 3D Gaussian Splatting SLAM via Sparse Processing](https://arxiv.org/abs/2511.18755v1)**  
  Authors: Xiaotong Huang, He Zhu, Tianrui Ma, Yuxiang Xiong, Fangxin Liu, Zhezhi He, Yiming Gan, Zihan Liu, Jingwen Leng, Yu Feng, Minyi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18755v1.pdf)  
  Keywords: ar, slam, gaussian splatting, efficient, 3d gaussian, tracking, high-fidelity  
- **[Novel View Synthesis from A Few Glimpses via Test-Time Natural Video Completion](https://arxiv.org/abs/2511.17932v1)**  
  Authors: Yan Xu, Yixing Wang, Stella X. Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17932v1.pdf)  
  Keywords: ar, gaussian splatting, nerf, 3d gaussian, geometry, high-fidelity  
- **[One Walk is All You Need: Data-Efficient 3D RF Scene Reconstruction with Human Movements](https://arxiv.org/abs/2511.16966v1)**  
  Authors: Yiheng Bian, Zechen Li, Lanqing Yang, Hao Pan, Yezhou Wang, Longyuan Ge, Jeffery Wu, Ruiheng Liu, Yongjian Fu, Yichao chen, Guangtao xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16966v1.pdf)  
  Keywords: ar, gaussian splatting, motion, efficient, fast, 3d gaussian, dynamic, human, geometry, mapping, high-fidelity  
- **[CuriGS: Curriculum-Guided Gaussian Splatting for Sparse View Synthesis](https://arxiv.org/abs/2511.16030v1)**  
  Authors: Zijian Wu, Mingfeng Jiang, Zidian Lin, Ying Song, Hanjie Ma, Qun Wu, Dongping Zhang, Guiyang Pu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16030v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zijian1026.github.io/CuriGS/)  
  Keywords: sparse view, ar, gaussian splatting, 3d reconstruction, efficient, 3d gaussian, high-fidelity, sparse-view  
- **[Silhouette-to-Contour Registration: Aligning Intraoral Scan Models with Cephalometric Radiographs](https://arxiv.org/abs/2511.14343v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Ji Jiang, Tong Chen, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14343v1.pdf)  
  Keywords: ar, gaussian splatting, geometry, face, high-fidelity  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: compact, illumination, ar, gaussian splatting, 3d reconstruction, 3d gaussian, geometry, face, high-fidelity, sparse-view  

### Ray Tracing

- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: ray tracing, illumination, ar, gaussian splatting, geometry, reflection  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: ar, gaussian splatting, efficient, ray marching, 3d gaussian, geometry  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: real-time rendering, ray tracing, relightable, ar, gaussian splatting, lighting, efficient, light transport, face, shadow  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: illumination, ar, gaussian splatting, lighting, efficient, geometry, global illumination, relighting, reflection, light transport  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v2)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v2.pdf)  
  Keywords: ray tracing, ar, gaussian splatting, 4d, fast, dynamic  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: ray tracing, illumination, ar, gaussian splatting, lighting, geometry, nerf, 3d gaussian, relighting, reflection, face, high-fidelity  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: illumination, relightable, ar, outdoor, gaussian splatting, lighting, 3d gaussian, global illumination, dynamic, relighting, face, shadow  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: ar, gaussian splatting, lighting, path tracing, dynamic, 3d gaussian, face  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relightable, ar, gaussian splatting, lighting, efficient, ray marching, 3d gaussian, relighting, geometry, efficient rendering, face  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: real-time rendering, ray tracing, ar, gaussian splatting, efficient, high-fidelity  

### Relighting

*Showing the latest 50 out of 120 papers*

- **[Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes](https://arxiv.org/abs/2511.21367v1)**  
  Authors: Yangle Liu, Fengze Li, Kan Liu, Jieming Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.21367v1.pdf)  
  Keywords: ar, gaussian splatting, motion, 4d, nerf, dynamic, geometry, lightweight, reflection  
- **[CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation](https://arxiv.org/abs/2511.17904v1)**  
  Authors: Yuhang Ming, Chenxin Fang, Xingyuan Yu, Fan Zhang, Weichen Dai, Wanzeng Kong, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17904v1.pdf)  
  Keywords: compact, semantic, ar, gaussian splatting, lighting, understanding, dynamic, geometry  
- **[Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction](https://arxiv.org/abs/2511.14540v1)**  
  Authors: Hao Tian, Chenyangguang Zhang, Rui Liu, Wen Shen, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14540v1.pdf)  
  Keywords: deformation, ar, gaussian splatting, motion, lighting, 4d, dynamic, 3d gaussian, geometry  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: compact, illumination, ar, gaussian splatting, 3d reconstruction, 3d gaussian, geometry, face, high-fidelity, sparse-view  
- **[iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion](https://arxiv.org/abs/2511.14149v1)**  
  Authors: Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14149v1.pdf)  
  Keywords: robotics, ar, slam, gaussian splatting, lighting, head, nerf, 3d gaussian, tracking  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: illumination, semantic, ar, outdoor, gaussian splatting, lighting, efficient, segmentation, relighting, geometry, face, high-fidelity  
- **[Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis](https://arxiv.org/abs/2511.13011v1)**  
  Authors: Qingsen Ma, Chen Zou, Dianyun Wang, Jia Wang, Liuyu Xiang, Zhaofeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13011v1.pdf)  
  Keywords: illumination, ar, gaussian splatting, 3d reconstruction, 3d gaussian, dynamic, geometry, face  
- **[Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric](https://arxiv.org/abs/2511.08032v1)**  
  Authors: Zhaolin Wan, Yining Diao, Jingqi Xu, Hao Wang, Zhiyang Li, Xiaopeng Fan, Wangmeng Zuo, Debin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.08032v1.pdf)  
  Keywords: ar, gaussian splatting, lighting, 3d gaussian, high-fidelity  
- **[UltraGS: Gaussian Splatting for Ultrasound Novel View Synthesis](https://arxiv.org/abs/2511.07743v1)**  
  Authors: Yuezhe Yang, Wenjie Cai, Dexin Yang, Yufang Dong, Xingbo Dong, Zhe Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07743v1.pdf)  
  Keywords: ar, lightweight, gaussian splatting, reflection  
- **[Channel Knowledge Map Construction: Recent Advances and Open Challenges](https://arxiv.org/abs/2511.04944v1)**  
  Authors: Zixiang Ren, Juncong Zhou, Jie Xu, Ling Qiu, Yong Zeng, Han Hu, Juyong Zhang, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04944v1.pdf)  
  Keywords: ar, gaussian splatting, lighting, efficient, high-fidelity  

### SLAM

*Showing the latest 50 out of 140 papers*

- **[GS-Checker: Tampering Localization for 3D Gaussian Splatting](https://arxiv.org/abs/2511.20354v1)**  
  Authors: Haoliang Han, Ziyuan Luo, Jun Qi, Anderson Rocha, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20354v1.pdf)  
  Keywords: localization, ar, 3d gaussian, gaussian splatting  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: ar, gaussian splatting, motion, autonomous driving, dynamic, 3d gaussian, human, tracking, high-fidelity  
- **[Splatonic: Architecture Support for 3D Gaussian Splatting SLAM via Sparse Processing](https://arxiv.org/abs/2511.18755v1)**  
  Authors: Xiaotong Huang, He Zhu, Tianrui Ma, Yuxiang Xiong, Fangxin Liu, Zhezhi He, Yiming Gan, Zihan Liu, Jingwen Leng, Yu Feng, Minyi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18755v1.pdf)  
  Keywords: ar, slam, gaussian splatting, efficient, 3d gaussian, tracking, high-fidelity  
- **[PhysMorph-GS: Differentiable Shape Morphing via Joint Optimization of Physics and Rendering Objectives](https://arxiv.org/abs/2511.16988v1)**  
  Authors: Chang-Yong Song, David Hyde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16988v1.pdf)  
  Keywords: compact, deformation, ar, gaussian splatting, 3d gaussian, mapping, face  
- **[One Walk is All You Need: Data-Efficient 3D RF Scene Reconstruction with Human Movements](https://arxiv.org/abs/2511.16966v1)**  
  Authors: Yiheng Bian, Zechen Li, Lanqing Yang, Hao Pan, Yezhou Wang, Longyuan Ge, Jeffery Wu, Ruiheng Liu, Yongjian Fu, Yichao chen, Guangtao xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16966v1.pdf)  
  Keywords: ar, gaussian splatting, motion, efficient, fast, 3d gaussian, dynamic, human, geometry, mapping, high-fidelity  
- **[Optimizing 3D Gaussian Splattering for Mobile GPUs](https://arxiv.org/abs/2511.16298v1)**  
  Authors: Md Musfiqur Rahman Sanim, Zhihao Shu, Bahram Afsharmanesh, AmirAli Mirian, Jiexiong Guan, Wei Niu, Bin Ren, Gagan Agrawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16298v1.pdf)  
  Keywords: ar, gaussian splatting, efficient, fast, 3d gaussian, mapping  
- **[LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM](https://arxiv.org/abs/2511.16144v1)**  
  Authors: Sibaek Lee, Seongbo Ha, Kyeongsu Kang, Joonyeol Choi, Seungjun Tak, Hyeonwoo Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16144v1.pdf)  
  Keywords: compact, semantic, ar, slam, gaussian splatting, localization, head, understanding, 3d gaussian, tracking, mapping  
- **[Clustered Error Correction with Grouped 4D Gaussian Splatting](https://arxiv.org/abs/2511.16112v1)**  
  Authors: Taeho Kang, Jaeyeon Park, Kyungjin Lee, Youngki Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16112v1.pdf)  
  Keywords: ar, gaussian splatting, 4d, dynamic, mapping  
- **[iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion](https://arxiv.org/abs/2511.14149v1)**  
  Authors: Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14149v1.pdf)  
  Keywords: robotics, ar, slam, gaussian splatting, lighting, head, nerf, 3d gaussian, tracking  
- **[GUIDE: Gaussian Unified Instance Detection for Enhanced Obstacle Perception in Autonomous Driving](https://arxiv.org/abs/2511.12941v1)**  
  Authors: Chunyong Hu, Qi Luo, Jianyun Xu, Song Wang, Qiang Li, Sheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12941v1.pdf)  
  Keywords: ar, autonomous driving, 3d gaussian, tracking  

### Scene Understanding

*Showing the latest 50 out of 202 papers*

- **[Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v1)**  
  Authors: João Malheiro Silva, Andy Huynh, Tong Duy Son, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20348v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, 3d reconstruction, 3d gaussian, geometry, face  
- **[GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861v1)**  
  Authors: GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu, Kerui Li, Mengyuan Xu, Qiuping Deng, Siting Wang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yankai Wang, Yu Cao, Yifan Chang, Yuan Xu, Yun Ye, Yang Wang, Yukun Zhou, Zhengyuan Zhang, Zhehao Dong, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19861v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, motion, efficient, 3d gaussian  
- **[DensifyBeforehand: LiDAR-assisted Content-aware Densification for Efficient and Quality 3D Gaussian Splatting](https://arxiv.org/abs/2511.19294v1)**  
  Authors: Phurtivilai Patt, Leyang Huang, Yinqiang Zhang, Yang Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19294v1.pdf)  
  Keywords: ar, semantic, gaussian splatting, efficient, 3d gaussian  
- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: ar, outdoor, gaussian splatting, 3d reconstruction, understanding, 3d gaussian, geometry  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: semantic, ar, outdoor, gaussian splatting, fast, geometry  
- **[SegSplat: Feed-forward Gaussian Splatting and Open-Set Semantic Segmentation](https://arxiv.org/abs/2511.18386v1)**  
  Authors: Peter Siegel, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18386v1.pdf)  
  Keywords: compact, semantic, ar, gaussian splatting, 3d reconstruction, efficient, segmentation, understanding, 3d gaussian  
- **[CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation](https://arxiv.org/abs/2511.17904v1)**  
  Authors: Yuhang Ming, Chenxin Fang, Xingyuan Yu, Fan Zhang, Weichen Dai, Wanzeng Kong, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17904v1.pdf)  
  Keywords: compact, semantic, ar, gaussian splatting, lighting, understanding, dynamic, geometry  
- **[FisheyeGaussianLift: BEV Feature Lifting for Surround-View Fisheye Camera Perception](https://arxiv.org/abs/2511.17210v1)**  
  Authors: Shubham Sonarghare, Prasad Deshpande, Ciaran Hogan, Deepika-Rani Kaliappan-Mahalingam, Ganesh Sistu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17210v1.pdf)  
  Keywords: ar, 3d gaussian, segmentation, semantic  
- **[SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting](https://arxiv.org/abs/2511.17092v2)**  
  Authors: Di Wu, Liu Liu, Xueyu Yuan, Qiaojun Yu, Wenxiao Chen, Ruilong Yan, Yiming Tang, Liangtu Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17092v2.pdf)  
  Keywords: sparse view, ar, gaussian splatting, 3d reconstruction, segmentation, 3d gaussian, face, few-shot, sparse-view  
- **[Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling](https://arxiv.org/abs/2511.16301v2)**  
  Authors: Minseok Seo, Mark Hamilton, Changick Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16301v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seominseok0429.github.io/Upsample-Anything/}{https://seominseok0429.github.io/Upsample-Anything/})  
  Keywords: ar, semantic, gaussian splatting, segmentation, lightweight  



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