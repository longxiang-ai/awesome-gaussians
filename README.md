# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-11-27 00:53:25

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

- [3DGS Surveys](#3dgs-surveys) (23 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (255 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (996 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (338 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (397 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (79 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (326 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (77 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (406 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (184 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (15 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (119 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (140 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (203 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: robotics, 3d gaussian, slam, localization, semantic, gaussian splatting, high-fidelity, ar, survey, efficient, mapping  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: 3d gaussian, motion, geometry, nerf, fast, gaussian splatting, ar, 4d, survey  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: efficient rendering, 3d gaussian, face, animation, gaussian splatting, ar, survey, lighting, efficient, real-time rendering, avatar, 3d reconstruction  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: human, nerf, gaussian splatting, ar, understanding, survey, lightweight, efficient  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: 3d gaussian, neural rendering, slam, nerf, gaussian splatting, fast, ar, understanding, survey, efficient  
- **[A-TDOM: Active TDOM via On-the-Fly 3DGS](https://arxiv.org/abs/2509.12759v2)**  
  Authors: Yiwei Xu, Xiang Wang, Yifei Yu, Wentian Gan, Luca Morelli, Giulio Perda, Xiongwu Xiao, Zongqian Zhan, Xin Wang, Fabio Remondino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.12759v2.pdf)  
  Keywords: face, ar, survey  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: segmentation, 3d gaussian, nerf, semantic, gaussian splatting, high-fidelity, ar, compact, understanding, survey, lighting  
- **[A Study of the Framework and Real-World Applications of Language Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: robotics, 3d gaussian, nerf, semantic, gaussian splatting, ar, understanding, survey, efficient  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: robotics, 3d gaussian, human, nerf, gaussian splatting, ar, survey  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: robotics, 3d gaussian, motion, geometry, nerf, sparse-view, vr, gaussian splatting, ar, survey, 3d reconstruction  

### Acceleration

*Showing the latest 50 out of 255 papers*

- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: geometry, outdoor, semantic, fast, gaussian splatting, ar  
- **[Alias-free 4D Gaussian Splatting](https://arxiv.org/abs/2511.18367v1)**  
  Authors: Zilong Chen, Huan-ang Gao, Delin Qu, Haohan Chi, Hao Tang, Kai Zhang, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18367v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4d-alias-free.github.io/4D-Alias-free/)  
  Keywords: gaussian splatting, 4d, ar, dynamic, real-time rendering  
- **[PEGS: Physics-Event Enhanced Large Spatiotemporal Motion Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2511.17116v1)**  
  Authors: Yijun Xu, Jingrui Zhang, Hongyi Liu, Yuhan Chen, Yuanyang Wang, Qingyao Guo, Dingwen Wang, Lei Yu, Chu He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17116v1.pdf)  
  Keywords: 3d gaussian, motion, fast, gaussian splatting, ar, acceleration, dynamic  
- **[One Walk is All You Need: Data-Efficient 3D RF Scene Reconstruction with Human Movements](https://arxiv.org/abs/2511.16966v1)**  
  Authors: Yiheng Bian, Zechen Li, Lanqing Yang, Hao Pan, Yezhou Wang, Longyuan Ge, Jeffery Wu, Ruiheng Liu, Yongjian Fu, Yichao chen, Guangtao xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16966v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, human, fast, gaussian splatting, high-fidelity, ar, dynamic, efficient, mapping  
- **[Vorion: A RISC-V GPU with Hardware-Accelerated 3D Gaussian Rendering and Training](https://arxiv.org/abs/2511.16831v1)**  
  Authors: Yipeng Wang, Mengtian Yang, Chieh-pu Lo, Jaydeep P. Kulkarni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16831v1.pdf)  
  Keywords: 3d gaussian, neural rendering, gaussian splatting, 4d, ar, real-time rendering  
- **[Optimizing 3D Gaussian Splattering for Mobile GPUs](https://arxiv.org/abs/2511.16298v1)**  
  Authors: Md Musfiqur Rahman Sanim, Zhihao Shu, Bahram Afsharmanesh, AmirAli Mirian, Jiexiong Guan, Wei Niu, Bin Ren, Gagan Agrawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16298v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, ar, efficient, mapping  
- **[Gaussian Blending: Rethinking Alpha Blending in 3D Gaussian Splatting](https://arxiv.org/abs/2511.15102v1)**  
  Authors: Junseo Koo, Jinseo Jeong, Gunhee Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.15102v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, ar  
- **[IBGS: Image-Based Gaussian Splatting](https://arxiv.org/abs/2511.14357v1)**  
  Authors: Hoang Chuong Nguyen, Wei Mao, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14357v1.pdf)  
  Keywords: 3d gaussian, face, fast, gaussian splatting, ar, efficient, head  
- **[SF-Recon: Simplification-Free Lightweight Building Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2511.13278v2)**  
  Authors: Zihan Li, Tengfei Wang, Wentian Gan, Hao Zhan, Xin Wang, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13278v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lzh282140127-cell.github.io/SF-Recon-project/)  
  Keywords: 3d gaussian, geometry, face, fast, gaussian splatting, ar, lightweight  
- **[Neo: Real-Time On-Device 3D Gaussian Splatting with Reuse-and-Update Sorting Acceleration](https://arxiv.org/abs/2511.12930v1)**  
  Authors: Changhun Oh, Seongryong Oh, Jinwoo Hwang, Yoonsung Kim, Hardik Sharma, Jongse Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12930v1.pdf)  
  Keywords: tracking, 3d gaussian, vr, gaussian splatting, ar, acceleration, efficient  

### Applications

*Showing the latest 50 out of 996 papers*

- **[GS-Checker: Tampering Localization for 3D Gaussian Splatting](https://arxiv.org/abs/2511.20354v1)**  
  Authors: Haoliang Han, Ziyuan Luo, Jun Qi, Anderson Rocha, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20354v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, localization, ar  
- **[Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v1)**  
  Authors: João Malheiro Silva, Andy Huynh, Tong Duy Son, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20348v1.pdf)  
  Keywords: 3d gaussian, geometry, face, semantic, gaussian splatting, ar, 3d reconstruction  
- **[GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861v1)**  
  Authors: GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu, Kerui Li, Mengyuan Xu, Qiuping Deng, Siting Wang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yankai Wang, Yu Cao, Yifan Chang, Yuan Xu, Yun Ye, Yang Wang, Yukun Zhou, Zhengyuan Zhang, Zhehao Dong, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19861v1.pdf)  
  Keywords: 3d gaussian, motion, semantic, gaussian splatting, ar, efficient  
- **[STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction](https://arxiv.org/abs/2511.19854v1)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Zidu Wang, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19854v1.pdf)  
  Keywords: 3d gaussian, motion, gaussian splatting, high-fidelity, ar, deformation, dynamic, head, avatar  
- **[DensifyBeforehand: LiDAR-assisted Content-aware Densification for Efficient and Quality 3D Gaussian Splatting](https://arxiv.org/abs/2511.19294v1)**  
  Authors: Phurtivilai Patt, Leyang Huang, Yinqiang Zhang, Yang Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19294v1.pdf)  
  Keywords: 3d gaussian, semantic, gaussian splatting, ar, efficient  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: 3d gaussian, tracking, motion, human, gaussian splatting, high-fidelity, ar, dynamic, autonomous driving  
- **[NVGS: Neural Visibility for Occlusion Culling in 3D Gaussian Splatting](https://arxiv.org/abs/2511.19202v1)**  
  Authors: Brent Zoomers, Florian Hahlbohm, Joni Vanherck, Lode Jorissen, Marcus Magnor, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19202v1.pdf)  
  Keywords: 3d gaussian, vr, gaussian splatting, ar, efficient  
- **[MetroGS: Efficient and Stable Reconstruction of Geometrically Accurate High-Fidelity Large-Scale Scenes](https://arxiv.org/abs/2511.19172v1)**  
  Authors: Kehua Chen, Tianlu Mao, Zhuxin Ma, Hao Jiang, Zehao Li, Zihan Liu, Shuqi Gao, Honglong Zhao, Feng Dai, Yucheng Zhang, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19172v1.pdf)  
  Keywords: 3d gaussian, geometry, gaussian splatting, high-fidelity, ar, efficient  
- **[Proxy-Free Gaussian Splats Deformation with Splat-Based Surface Estimation](https://arxiv.org/abs/2511.19542v1)**  
  Authors: Jaeyeong Kim, Seungwoo Yoo, Minhyuk Sung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19542v1.pdf)  
  Keywords: face, nerf, ar, deformation, head  
- **[Neural Texture Splatting: Expressive 3D Gaussian Splatting for View Synthesis, Geometry, and Dynamic Reconstruction](https://arxiv.org/abs/2511.18873v1)**  
  Authors: Yiming Wang, Shaofei Wang, Marko Mihajlovic, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18873v1.pdf)  
  Keywords: 3d gaussian, geometry, gaussian splatting, 4d, ar, dynamic, efficient  

### Avatar Generation

*Showing the latest 50 out of 338 papers*

- **[Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v1)**  
  Authors: João Malheiro Silva, Andy Huynh, Tong Duy Son, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20348v1.pdf)  
  Keywords: 3d gaussian, geometry, face, semantic, gaussian splatting, ar, 3d reconstruction  
- **[STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction](https://arxiv.org/abs/2511.19854v1)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Zidu Wang, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19854v1.pdf)  
  Keywords: 3d gaussian, motion, gaussian splatting, high-fidelity, ar, deformation, dynamic, head, avatar  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: 3d gaussian, tracking, motion, human, gaussian splatting, high-fidelity, ar, dynamic, autonomous driving  
- **[Proxy-Free Gaussian Splats Deformation with Splat-Based Surface Estimation](https://arxiv.org/abs/2511.19542v1)**  
  Authors: Jaeyeong Kim, Seungwoo Yoo, Minhyuk Sung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19542v1.pdf)  
  Keywords: face, nerf, ar, deformation, head  
- **[AEGIS: Preserving privacy of 3D Facial Avatars with Adversarial Perturbations](https://arxiv.org/abs/2511.17747v1)**  
  Authors: Dawid Wolkiewicz, Anastasiya Pechko, Przemysław Spurek, Piotr Syga  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17747v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, face, gaussian splatting, ar, dynamic, efficient, avatar  
- **[Towards Generative Design Using Optimal Transport for Shape Exploration and Solution Field Interpolation](https://arxiv.org/abs/2511.17111v1)**  
  Authors: Sergio Torregrosa, David Munoz, Hector Navarro, Charbel Farhat, Francisco Chinesta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17111v1.pdf)  
  Keywords: face, efficient, gaussian splatting, ar  
- **[SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting](https://arxiv.org/abs/2511.17092v2)**  
  Authors: Di Wu, Liu Liu, Xueyu Yuan, Qiaojun Yu, Wenxiao Chen, Ruilong Yan, Yiming Tang, Liangtu Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17092v2.pdf)  
  Keywords: segmentation, 3d gaussian, sparse-view, face, gaussian splatting, ar, sparse view, few-shot, 3d reconstruction  
- **[REArtGS++: Generalizable Articulation Reconstruction with Temporal Geometry Constraint via Planar Gaussian Splatting](https://arxiv.org/abs/2511.17059v2)**  
  Authors: Di Wu, Liu Liu, Anran Huang, Yuyan Liu, Qiaojun Yu, Shaofan Liu, Liangtu Song, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17059v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sites.google.com/view/reartgs2/home.)  
  Keywords: motion, geometry, face, gaussian splatting, ar  
- **[PhysMorph-GS: Differentiable Shape Morphing via Joint Optimization of Physics and Rendering Objectives](https://arxiv.org/abs/2511.16988v1)**  
  Authors: Chang-Yong Song, David Hyde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16988v1.pdf)  
  Keywords: 3d gaussian, face, gaussian splatting, compact, ar, deformation, mapping  
- **[One Walk is All You Need: Data-Efficient 3D RF Scene Reconstruction with Human Movements](https://arxiv.org/abs/2511.16966v1)**  
  Authors: Yiheng Bian, Zechen Li, Lanqing Yang, Hao Pan, Yezhou Wang, Longyuan Ge, Jeffery Wu, Ruiheng Liu, Yongjian Fu, Yichao chen, Guangtao xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16966v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, human, fast, gaussian splatting, high-fidelity, ar, dynamic, efficient, mapping  

### Dynamic Scene

*Showing the latest 50 out of 397 papers*

- **[GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861v1)**  
  Authors: GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu, Kerui Li, Mengyuan Xu, Qiuping Deng, Siting Wang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yankai Wang, Yu Cao, Yifan Chang, Yuan Xu, Yun Ye, Yang Wang, Yukun Zhou, Zhengyuan Zhang, Zhehao Dong, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19861v1.pdf)  
  Keywords: 3d gaussian, motion, semantic, gaussian splatting, ar, efficient  
- **[STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction](https://arxiv.org/abs/2511.19854v1)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Zidu Wang, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19854v1.pdf)  
  Keywords: 3d gaussian, motion, gaussian splatting, high-fidelity, ar, deformation, dynamic, head, avatar  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: 3d gaussian, tracking, motion, human, gaussian splatting, high-fidelity, ar, dynamic, autonomous driving  
- **[Proxy-Free Gaussian Splats Deformation with Splat-Based Surface Estimation](https://arxiv.org/abs/2511.19542v1)**  
  Authors: Jaeyeong Kim, Seungwoo Yoo, Minhyuk Sung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19542v1.pdf)  
  Keywords: face, nerf, ar, deformation, head  
- **[Neural Texture Splatting: Expressive 3D Gaussian Splatting for View Synthesis, Geometry, and Dynamic Reconstruction](https://arxiv.org/abs/2511.18873v1)**  
  Authors: Yiming Wang, Shaofei Wang, Marko Mihajlovic, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18873v1.pdf)  
  Keywords: 3d gaussian, geometry, gaussian splatting, 4d, ar, dynamic, efficient  
- **[Alias-free 4D Gaussian Splatting](https://arxiv.org/abs/2511.18367v1)**  
  Authors: Zilong Chen, Huan-ang Gao, Delin Qu, Haohan Chi, Hao Tang, Kai Zhang, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18367v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4d-alias-free.github.io/4D-Alias-free/)  
  Keywords: gaussian splatting, 4d, ar, dynamic, real-time rendering  
- **[Observer Actor: Active Vision Imitation Learning with Sparse View Gaussian Splatting](https://arxiv.org/abs/2511.18140v1)**  
  Authors: Yilong Wang, Cheng Qian, Ruomeng Fan, Edward Johns  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18140v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://obact.github.io.)  
  Keywords: 3d gaussian, sparse view, gaussian splatting, ar, dynamic  
- **[CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation](https://arxiv.org/abs/2511.17904v1)**  
  Authors: Yuhang Ming, Chenxin Fang, Xingyuan Yu, Fan Zhang, Weichen Dai, Wanzeng Kong, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17904v1.pdf)  
  Keywords: geometry, semantic, gaussian splatting, compact, understanding, ar, lighting, dynamic  
- **[AEGIS: Preserving privacy of 3D Facial Avatars with Adversarial Perturbations](https://arxiv.org/abs/2511.17747v1)**  
  Authors: Dawid Wolkiewicz, Anastasiya Pechko, Przemysław Spurek, Piotr Syga  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17747v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, face, gaussian splatting, ar, dynamic, efficient, avatar  
- **[PEGS: Physics-Event Enhanced Large Spatiotemporal Motion Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2511.17116v1)**  
  Authors: Yijun Xu, Jingrui Zhang, Hongyi Liu, Yuhan Chen, Yuanyang Wang, Qingyao Guo, Dingwen Wang, Lei Yu, Chu He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17116v1.pdf)  
  Keywords: 3d gaussian, motion, fast, gaussian splatting, ar, acceleration, dynamic  

### Few-shot

*Showing the latest 50 out of 79 papers*

- **[Observer Actor: Active Vision Imitation Learning with Sparse View Gaussian Splatting](https://arxiv.org/abs/2511.18140v1)**  
  Authors: Yilong Wang, Cheng Qian, Ruomeng Fan, Edward Johns  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18140v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://obact.github.io.)  
  Keywords: 3d gaussian, sparse view, gaussian splatting, ar, dynamic  
- **[Frequency-Adaptive Sharpness Regularization for Improving 3D Gaussian Splatting Generalization](https://arxiv.org/abs/2511.17918v1)**  
  Authors: Youngsik Yun, Dongjun Gu, Youngjung Uh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bbangsik13.github.io/FASR.)  
  Keywords: few-shot, gaussian splatting, 3d gaussian, ar  
- **[SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting](https://arxiv.org/abs/2511.17092v2)**  
  Authors: Di Wu, Liu Liu, Xueyu Yuan, Qiaojun Yu, Wenxiao Chen, Ruilong Yan, Yiming Tang, Liangtu Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17092v2.pdf)  
  Keywords: segmentation, 3d gaussian, sparse-view, face, gaussian splatting, ar, sparse view, few-shot, 3d reconstruction  
- **[CuriGS: Curriculum-Guided Gaussian Splatting for Sparse View Synthesis](https://arxiv.org/abs/2511.16030v1)**  
  Authors: Zijian Wu, Mingfeng Jiang, Zidian Lin, Ying Song, Hanjie Ma, Qun Wu, Dongping Zhang, Guiyang Pu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16030v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zijian1026.github.io/CuriGS/)  
  Keywords: 3d gaussian, sparse-view, gaussian splatting, high-fidelity, ar, sparse view, efficient, 3d reconstruction  
- **[SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2511.14633v1)**  
  Authors: Meiying Gu, Jiawei Zhang, Jiahe Li, Xiaohan Yu, Haonan Luo, Jin Zheng, Xiao Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14633v1.pdf)  
  Keywords: 3d gaussian, geometry, nerf, sparse-view, face, gaussian splatting, ar, efficient  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: 3d gaussian, geometry, sparse-view, face, gaussian splatting, illumination, high-fidelity, compact, ar, 3d reconstruction  
- **[RoboTidy : A 3D Gaussian Splatting Household Tidying Benchmark for Embodied Navigation and Action](https://arxiv.org/abs/2511.14161v2)**  
  Authors: Xiaoquan Sun, Ruijian Zhang, Kang Pang, Bingchen Miao, Yuxiang Tan, Zhen Yang, Ming Li, Jiayu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14161v2.pdf)  
  Keywords: few-shot, gaussian splatting, 3d gaussian, ar  
- **[SplatSearch: Instance Image Goal Navigation for Mobile Robots using 3D Gaussian Splatting and Diffusion Models](https://arxiv.org/abs/2511.12972v1)**  
  Authors: Siddarth Narasimhan, Matthew Lisondra, Haitong Wang, Goldie Nejat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12972v1.pdf)  
  Keywords: 3d gaussian, sparse-view, semantic, gaussian splatting, ar  
- **[RealisticDreamer: Guidance Score Distillation for Few-shot Gaussian Splatting](https://arxiv.org/abs/2511.11213v1)**  
  Authors: Ruocheng Wu, Haolan He, Yufei Wang, Zhihao Li, Bihan Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.11213v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, semantic, gaussian splatting, ar, few-shot, real-time rendering  
- **[Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction](https://arxiv.org/abs/2511.07122v1)**  
  Authors: Changyue Shi, Chuxiao Yang, Xinyuan Hu, Minghao Chen, Wenwen Pan, Yan Yang, Jiajun Ding, Zhou Yu, Jun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07122v1.pdf)  
  Keywords: nerf, gaussian splatting, 4d, ar, deformation, dynamic, few-shot  

### Geometry Reconstruction

*Showing the latest 50 out of 326 papers*

- **[Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v1)**  
  Authors: João Malheiro Silva, Andy Huynh, Tong Duy Son, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20348v1.pdf)  
  Keywords: 3d gaussian, geometry, face, semantic, gaussian splatting, ar, 3d reconstruction  
- **[MetroGS: Efficient and Stable Reconstruction of Geometrically Accurate High-Fidelity Large-Scale Scenes](https://arxiv.org/abs/2511.19172v1)**  
  Authors: Kehua Chen, Tianlu Mao, Zhuxin Ma, Hao Jiang, Zehao Li, Zihan Liu, Shuqi Gao, Honglong Zhao, Feng Dai, Yucheng Zhang, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19172v1.pdf)  
  Keywords: 3d gaussian, geometry, gaussian splatting, high-fidelity, ar, efficient  
- **[Neural Texture Splatting: Expressive 3D Gaussian Splatting for View Synthesis, Geometry, and Dynamic Reconstruction](https://arxiv.org/abs/2511.18873v1)**  
  Authors: Yiming Wang, Shaofei Wang, Marko Mihajlovic, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18873v1.pdf)  
  Keywords: 3d gaussian, geometry, gaussian splatting, 4d, ar, dynamic, efficient  
- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: 3d gaussian, geometry, outdoor, gaussian splatting, understanding, ar, 3d reconstruction  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: geometry, outdoor, semantic, fast, gaussian splatting, ar  
- **[SegSplat: Feed-forward Gaussian Splatting and Open-Set Semantic Segmentation](https://arxiv.org/abs/2511.18386v1)**  
  Authors: Peter Siegel, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18386v1.pdf)  
  Keywords: segmentation, 3d gaussian, semantic, gaussian splatting, compact, understanding, ar, efficient, 3d reconstruction  
- **[Novel View Synthesis from A Few Glimpses via Test-Time Natural Video Completion](https://arxiv.org/abs/2511.17932v1)**  
  Authors: Yan Xu, Yixing Wang, Stella X. Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17932v1.pdf)  
  Keywords: 3d gaussian, geometry, nerf, gaussian splatting, high-fidelity, ar  
- **[CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation](https://arxiv.org/abs/2511.17904v1)**  
  Authors: Yuhang Ming, Chenxin Fang, Xingyuan Yu, Fan Zhang, Weichen Dai, Wanzeng Kong, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17904v1.pdf)  
  Keywords: geometry, semantic, gaussian splatting, compact, understanding, ar, lighting, dynamic  
- **[AEGIS: Preserving privacy of 3D Facial Avatars with Adversarial Perturbations](https://arxiv.org/abs/2511.17747v1)**  
  Authors: Dawid Wolkiewicz, Anastasiya Pechko, Przemysław Spurek, Piotr Syga  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17747v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, face, gaussian splatting, ar, dynamic, efficient, avatar  
- **[SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting](https://arxiv.org/abs/2511.17092v2)**  
  Authors: Di Wu, Liu Liu, Xueyu Yuan, Qiaojun Yu, Wenxiao Chen, Ruilong Yan, Yiming Tang, Liangtu Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17092v2.pdf)  
  Keywords: segmentation, 3d gaussian, sparse-view, face, gaussian splatting, ar, sparse view, few-shot, 3d reconstruction  

### Large Scene

*Showing the latest 50 out of 77 papers*

- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: 3d gaussian, geometry, outdoor, gaussian splatting, understanding, ar, 3d reconstruction  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: geometry, outdoor, semantic, fast, gaussian splatting, ar  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: segmentation, geometry, face, outdoor, relighting, gaussian splatting, illumination, high-fidelity, semantic, ar, lighting, efficient  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: 3d gaussian, geometry, outdoor, gaussian splatting, high-fidelity, ar  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: human, gaussian splatting, 4d, urban scene, ar, dynamic, autonomous driving  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, ar, large scene, head  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, outdoor, gaussian splatting, ar, understanding, slam, mapping  
- **[D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction](https://arxiv.org/abs/2510.25173v2)**  
  Authors: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25173v2.pdf)  
  Keywords: geometry, gaussian splatting, urban scene, ar, autonomous driving  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: face, semantic, gaussian splatting, urban scene, ar, 3d reconstruction  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/2510.22669v1)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22669v1.pdf)  
  Keywords: segmentation, 3d gaussian, human, outdoor, gaussian splatting, high-fidelity, ar, slam, dynamic, mapping  

### Model Compression

*Showing the latest 50 out of 406 papers*

- **[GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861v1)**  
  Authors: GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu, Kerui Li, Mengyuan Xu, Qiuping Deng, Siting Wang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yankai Wang, Yu Cao, Yifan Chang, Yuan Xu, Yun Ye, Yang Wang, Yukun Zhou, Zhengyuan Zhang, Zhehao Dong, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19861v1.pdf)  
  Keywords: 3d gaussian, motion, semantic, gaussian splatting, ar, efficient  
- **[DensifyBeforehand: LiDAR-assisted Content-aware Densification for Efficient and Quality 3D Gaussian Splatting](https://arxiv.org/abs/2511.19294v1)**  
  Authors: Phurtivilai Patt, Leyang Huang, Yinqiang Zhang, Yang Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19294v1.pdf)  
  Keywords: 3d gaussian, semantic, gaussian splatting, ar, efficient  
- **[NVGS: Neural Visibility for Occlusion Culling in 3D Gaussian Splatting](https://arxiv.org/abs/2511.19202v1)**  
  Authors: Brent Zoomers, Florian Hahlbohm, Joni Vanherck, Lode Jorissen, Marcus Magnor, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19202v1.pdf)  
  Keywords: 3d gaussian, vr, gaussian splatting, ar, efficient  
- **[MetroGS: Efficient and Stable Reconstruction of Geometrically Accurate High-Fidelity Large-Scale Scenes](https://arxiv.org/abs/2511.19172v1)**  
  Authors: Kehua Chen, Tianlu Mao, Zhuxin Ma, Hao Jiang, Zehao Li, Zihan Liu, Shuqi Gao, Honglong Zhao, Feng Dai, Yucheng Zhang, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19172v1.pdf)  
  Keywords: 3d gaussian, geometry, gaussian splatting, high-fidelity, ar, efficient  
- **[Neural Texture Splatting: Expressive 3D Gaussian Splatting for View Synthesis, Geometry, and Dynamic Reconstruction](https://arxiv.org/abs/2511.18873v1)**  
  Authors: Yiming Wang, Shaofei Wang, Marko Mihajlovic, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18873v1.pdf)  
  Keywords: 3d gaussian, geometry, gaussian splatting, 4d, ar, dynamic, efficient  
- **[Splatonic: Architecture Support for 3D Gaussian Splatting SLAM via Sparse Processing](https://arxiv.org/abs/2511.18755v1)**  
  Authors: Xiaotong Huang, He Zhu, Tianrui Ma, Yuxiang Xiong, Fangxin Liu, Zhezhi He, Yiming Gan, Zihan Liu, Jingwen Leng, Yu Feng, Minyi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18755v1.pdf)  
  Keywords: 3d gaussian, tracking, gaussian splatting, high-fidelity, ar, slam, efficient  
- **[SegSplat: Feed-forward Gaussian Splatting and Open-Set Semantic Segmentation](https://arxiv.org/abs/2511.18386v1)**  
  Authors: Peter Siegel, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18386v1.pdf)  
  Keywords: segmentation, 3d gaussian, semantic, gaussian splatting, compact, understanding, ar, efficient, 3d reconstruction  
- **[CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation](https://arxiv.org/abs/2511.17904v1)**  
  Authors: Yuhang Ming, Chenxin Fang, Xingyuan Yu, Fan Zhang, Weichen Dai, Wanzeng Kong, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17904v1.pdf)  
  Keywords: geometry, semantic, gaussian splatting, compact, understanding, ar, lighting, dynamic  
- **[AEGIS: Preserving privacy of 3D Facial Avatars with Adversarial Perturbations](https://arxiv.org/abs/2511.17747v1)**  
  Authors: Dawid Wolkiewicz, Anastasiya Pechko, Przemysław Spurek, Piotr Syga  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17747v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, face, gaussian splatting, ar, dynamic, efficient, avatar  
- **[Towards Generative Design Using Optimal Transport for Shape Exploration and Solution Field Interpolation](https://arxiv.org/abs/2511.17111v1)**  
  Authors: Sergio Torregrosa, David Munoz, Hector Navarro, Charbel Farhat, Francisco Chinesta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17111v1.pdf)  
  Keywords: face, efficient, gaussian splatting, ar  

### Quality Enhancement

*Showing the latest 50 out of 184 papers*

- **[STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction](https://arxiv.org/abs/2511.19854v1)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Zidu Wang, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19854v1.pdf)  
  Keywords: 3d gaussian, motion, gaussian splatting, high-fidelity, ar, deformation, dynamic, head, avatar  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: 3d gaussian, tracking, motion, human, gaussian splatting, high-fidelity, ar, dynamic, autonomous driving  
- **[MetroGS: Efficient and Stable Reconstruction of Geometrically Accurate High-Fidelity Large-Scale Scenes](https://arxiv.org/abs/2511.19172v1)**  
  Authors: Kehua Chen, Tianlu Mao, Zhuxin Ma, Hao Jiang, Zehao Li, Zihan Liu, Shuqi Gao, Honglong Zhao, Feng Dai, Yucheng Zhang, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19172v1.pdf)  
  Keywords: 3d gaussian, geometry, gaussian splatting, high-fidelity, ar, efficient  
- **[Splatonic: Architecture Support for 3D Gaussian Splatting SLAM via Sparse Processing](https://arxiv.org/abs/2511.18755v1)**  
  Authors: Xiaotong Huang, He Zhu, Tianrui Ma, Yuxiang Xiong, Fangxin Liu, Zhezhi He, Yiming Gan, Zihan Liu, Jingwen Leng, Yu Feng, Minyi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18755v1.pdf)  
  Keywords: 3d gaussian, tracking, gaussian splatting, high-fidelity, ar, slam, efficient  
- **[Novel View Synthesis from A Few Glimpses via Test-Time Natural Video Completion](https://arxiv.org/abs/2511.17932v1)**  
  Authors: Yan Xu, Yixing Wang, Stella X. Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17932v1.pdf)  
  Keywords: 3d gaussian, geometry, nerf, gaussian splatting, high-fidelity, ar  
- **[One Walk is All You Need: Data-Efficient 3D RF Scene Reconstruction with Human Movements](https://arxiv.org/abs/2511.16966v1)**  
  Authors: Yiheng Bian, Zechen Li, Lanqing Yang, Hao Pan, Yezhou Wang, Longyuan Ge, Jeffery Wu, Ruiheng Liu, Yongjian Fu, Yichao chen, Guangtao xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16966v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, human, fast, gaussian splatting, high-fidelity, ar, dynamic, efficient, mapping  
- **[CuriGS: Curriculum-Guided Gaussian Splatting for Sparse View Synthesis](https://arxiv.org/abs/2511.16030v1)**  
  Authors: Zijian Wu, Mingfeng Jiang, Zidian Lin, Ying Song, Hanjie Ma, Qun Wu, Dongping Zhang, Guiyang Pu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16030v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zijian1026.github.io/CuriGS/)  
  Keywords: 3d gaussian, sparse-view, gaussian splatting, high-fidelity, ar, sparse view, efficient, 3d reconstruction  
- **[Silhouette-to-Contour Registration: Aligning Intraoral Scan Models with Cephalometric Radiographs](https://arxiv.org/abs/2511.14343v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Ji Jiang, Tong Chen, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14343v1.pdf)  
  Keywords: geometry, face, gaussian splatting, high-fidelity, ar  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: 3d gaussian, geometry, sparse-view, face, gaussian splatting, illumination, high-fidelity, compact, ar, 3d reconstruction  
- **[GEN3D: Generating Domain-Free 3D Scenes from a Single Image](https://arxiv.org/abs/2511.14291v1)**  
  Authors: Yuxin Zhang, Ziyu Lu, Hongbo Duan, Keyu Fan, Pengting Luo, Peiyu Zhuang, Mengyu Yang, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14291v1.pdf)  
  Keywords: ar, gaussian splatting, high-fidelity, 3d reconstruction  

### Ray Tracing

- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: geometry, gaussian splatting, illumination, reflection, ar, ray tracing  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: 3d gaussian, ray marching, geometry, gaussian splatting, ar, efficient  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: relightable, light transport, face, gaussian splatting, ray tracing, shadow, ar, lighting, efficient, real-time rendering  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: light transport, geometry, relighting, gaussian splatting, illumination, reflection, global illumination, ar, lighting, efficient  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v2)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v2.pdf)  
  Keywords: fast, gaussian splatting, 4d, ar, dynamic, ray tracing  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: 3d gaussian, geometry, nerf, face, relighting, gaussian splatting, illumination, high-fidelity, reflection, ar, lighting, ray tracing  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: 3d gaussian, relightable, face, outdoor, relighting, gaussian splatting, illumination, global illumination, shadow, ar, lighting, dynamic  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: 3d gaussian, face, path tracing, gaussian splatting, lighting, ar, dynamic  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: efficient rendering, 3d gaussian, relightable, ray marching, geometry, face, relighting, gaussian splatting, ar, lighting, efficient  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, ray tracing, ar, efficient, real-time rendering  

### Relighting

*Showing the latest 50 out of 119 papers*

- **[CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation](https://arxiv.org/abs/2511.17904v1)**  
  Authors: Yuhang Ming, Chenxin Fang, Xingyuan Yu, Fan Zhang, Weichen Dai, Wanzeng Kong, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17904v1.pdf)  
  Keywords: geometry, semantic, gaussian splatting, compact, understanding, ar, lighting, dynamic  
- **[Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction](https://arxiv.org/abs/2511.14540v1)**  
  Authors: Hao Tian, Chenyangguang Zhang, Rui Liu, Wen Shen, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14540v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, gaussian splatting, 4d, ar, deformation, lighting, dynamic  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: 3d gaussian, geometry, sparse-view, face, gaussian splatting, illumination, high-fidelity, compact, ar, 3d reconstruction  
- **[iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion](https://arxiv.org/abs/2511.14149v1)**  
  Authors: Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14149v1.pdf)  
  Keywords: robotics, 3d gaussian, tracking, nerf, gaussian splatting, ar, slam, lighting, head  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: segmentation, geometry, face, outdoor, relighting, gaussian splatting, illumination, high-fidelity, semantic, ar, lighting, efficient  
- **[Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis](https://arxiv.org/abs/2511.13011v1)**  
  Authors: Qingsen Ma, Chen Zou, Dianyun Wang, Jia Wang, Liuyu Xiang, Zhaofeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13011v1.pdf)  
  Keywords: 3d gaussian, geometry, face, gaussian splatting, illumination, ar, dynamic, 3d reconstruction  
- **[Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric](https://arxiv.org/abs/2511.08032v1)**  
  Authors: Zhaolin Wan, Yining Diao, Jingqi Xu, Hao Wang, Zhiyang Li, Xiaopeng Fan, Wangmeng Zuo, Debin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.08032v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, ar, lighting  
- **[UltraGS: Gaussian Splatting for Ultrasound Novel View Synthesis](https://arxiv.org/abs/2511.07743v1)**  
  Authors: Yuezhe Yang, Wenjie Cai, Dexin Yang, Yufang Dong, Xingbo Dong, Zhe Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07743v1.pdf)  
  Keywords: lightweight, gaussian splatting, reflection, ar  
- **[Channel Knowledge Map Construction: Recent Advances and Open Challenges](https://arxiv.org/abs/2511.04944v1)**  
  Authors: Zixiang Ren, Juncong Zhou, Jie Xu, Ling Qiu, Yong Zeng, Han Hu, Juyong Zhang, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04944v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, ar, lighting, efficient  
- **[RoGER-SLAM: A Robust Gaussian Splatting SLAM System for Noisy and Low-light Environment Resilience](https://arxiv.org/abs/2510.22600v1)**  
  Authors: Huilin Yin, Zhaolin Yang, Linchuan Zhang, Gerhard Rigoll, Johannes Betz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22600v1.pdf)  
  Keywords: 3d gaussian, tracking, localization, semantic, gaussian splatting, illumination, high-fidelity, ar, slam, mapping  

### SLAM

*Showing the latest 50 out of 140 papers*

- **[GS-Checker: Tampering Localization for 3D Gaussian Splatting](https://arxiv.org/abs/2511.20354v1)**  
  Authors: Haoliang Han, Ziyuan Luo, Jun Qi, Anderson Rocha, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20354v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, localization, ar  
- **[IDSplat: Instance-Decomposed 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2511.19235v1)**  
  Authors: Carl Lindström, Mahan Rafidashti, Maryam Fatemi, Lars Hammarstrand, Martin R. Oswald, Lennart Svensson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19235v1.pdf)  
  Keywords: 3d gaussian, tracking, motion, human, gaussian splatting, high-fidelity, ar, dynamic, autonomous driving  
- **[Splatonic: Architecture Support for 3D Gaussian Splatting SLAM via Sparse Processing](https://arxiv.org/abs/2511.18755v1)**  
  Authors: Xiaotong Huang, He Zhu, Tianrui Ma, Yuxiang Xiong, Fangxin Liu, Zhezhi He, Yiming Gan, Zihan Liu, Jingwen Leng, Yu Feng, Minyi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18755v1.pdf)  
  Keywords: 3d gaussian, tracking, gaussian splatting, high-fidelity, ar, slam, efficient  
- **[PhysMorph-GS: Differentiable Shape Morphing via Joint Optimization of Physics and Rendering Objectives](https://arxiv.org/abs/2511.16988v1)**  
  Authors: Chang-Yong Song, David Hyde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16988v1.pdf)  
  Keywords: 3d gaussian, face, gaussian splatting, compact, ar, deformation, mapping  
- **[One Walk is All You Need: Data-Efficient 3D RF Scene Reconstruction with Human Movements](https://arxiv.org/abs/2511.16966v1)**  
  Authors: Yiheng Bian, Zechen Li, Lanqing Yang, Hao Pan, Yezhou Wang, Longyuan Ge, Jeffery Wu, Ruiheng Liu, Yongjian Fu, Yichao chen, Guangtao xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16966v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, human, fast, gaussian splatting, high-fidelity, ar, dynamic, efficient, mapping  
- **[Optimizing 3D Gaussian Splattering for Mobile GPUs](https://arxiv.org/abs/2511.16298v1)**  
  Authors: Md Musfiqur Rahman Sanim, Zhihao Shu, Bahram Afsharmanesh, AmirAli Mirian, Jiexiong Guan, Wei Niu, Bin Ren, Gagan Agrawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16298v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, ar, efficient, mapping  
- **[LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM](https://arxiv.org/abs/2511.16144v1)**  
  Authors: Sibaek Lee, Seongbo Ha, Kyeongsu Kang, Joonyeol Choi, Seungjun Tak, Hyeonwoo Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16144v1.pdf)  
  Keywords: 3d gaussian, tracking, localization, semantic, gaussian splatting, ar, compact, understanding, slam, head, mapping  
- **[Clustered Error Correction with Grouped 4D Gaussian Splatting](https://arxiv.org/abs/2511.16112v1)**  
  Authors: Taeho Kang, Jaeyeon Park, Kyungjin Lee, Youngki Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16112v1.pdf)  
  Keywords: gaussian splatting, 4d, ar, dynamic, mapping  
- **[iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion](https://arxiv.org/abs/2511.14149v1)**  
  Authors: Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14149v1.pdf)  
  Keywords: robotics, 3d gaussian, tracking, nerf, gaussian splatting, ar, slam, lighting, head  
- **[GUIDE: Gaussian Unified Instance Detection for Enhanced Obstacle Perception in Autonomous Driving](https://arxiv.org/abs/2511.12941v1)**  
  Authors: Chunyong Hu, Qi Luo, Jianyun Xu, Song Wang, Qiang Li, Sheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12941v1.pdf)  
  Keywords: tracking, 3d gaussian, autonomous driving, ar  

### Scene Understanding

*Showing the latest 50 out of 203 papers*

- **[Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348v1)**  
  Authors: João Malheiro Silva, Andy Huynh, Tong Duy Son, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20348v1.pdf)  
  Keywords: 3d gaussian, geometry, face, semantic, gaussian splatting, ar, 3d reconstruction  
- **[GigaWorld-0: World Models as Data Engine to Empower Embodied AI](https://arxiv.org/abs/2511.19861v1)**  
  Authors: GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu, Kerui Li, Mengyuan Xu, Qiuping Deng, Siting Wang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yankai Wang, Yu Cao, Yifan Chang, Yuan Xu, Yun Ye, Yang Wang, Yukun Zhou, Zhengyuan Zhang, Zhehao Dong, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19861v1.pdf)  
  Keywords: 3d gaussian, motion, semantic, gaussian splatting, ar, efficient  
- **[DensifyBeforehand: LiDAR-assisted Content-aware Densification for Efficient and Quality 3D Gaussian Splatting](https://arxiv.org/abs/2511.19294v1)**  
  Authors: Phurtivilai Patt, Leyang Huang, Yinqiang Zhang, Yang Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.19294v1.pdf)  
  Keywords: 3d gaussian, semantic, gaussian splatting, ar, efficient  
- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: 3d gaussian, geometry, outdoor, gaussian splatting, understanding, ar, 3d reconstruction  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: geometry, outdoor, semantic, fast, gaussian splatting, ar  
- **[SegSplat: Feed-forward Gaussian Splatting and Open-Set Semantic Segmentation](https://arxiv.org/abs/2511.18386v1)**  
  Authors: Peter Siegel, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18386v1.pdf)  
  Keywords: segmentation, 3d gaussian, semantic, gaussian splatting, compact, understanding, ar, efficient, 3d reconstruction  
- **[CUS-GS: A Compact Unified Structured Gaussian Splatting Framework for Multimodal Scene Representation](https://arxiv.org/abs/2511.17904v1)**  
  Authors: Yuhang Ming, Chenxin Fang, Xingyuan Yu, Fan Zhang, Weichen Dai, Wanzeng Kong, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17904v1.pdf)  
  Keywords: geometry, semantic, gaussian splatting, compact, understanding, ar, lighting, dynamic  
- **[FisheyeGaussianLift: BEV Feature Lifting for Surround-View Fisheye Camera Perception](https://arxiv.org/abs/2511.17210v1)**  
  Authors: Shubham Sonarghare, Prasad Deshpande, Ciaran Hogan, Deepika-Rani Kaliappan-Mahalingam, Ganesh Sistu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17210v1.pdf)  
  Keywords: semantic, segmentation, 3d gaussian, ar  
- **[SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting](https://arxiv.org/abs/2511.17092v2)**  
  Authors: Di Wu, Liu Liu, Xueyu Yuan, Qiaojun Yu, Wenxiao Chen, Ruilong Yan, Yiming Tang, Liangtu Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17092v2.pdf)  
  Keywords: segmentation, 3d gaussian, sparse-view, face, gaussian splatting, ar, sparse view, few-shot, 3d reconstruction  
- **[Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling](https://arxiv.org/abs/2511.16301v2)**  
  Authors: Minseok Seo, Mark Hamilton, Changick Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.16301v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seominseok0429.github.io/Upsample-Anything/}{https://seominseok0429.github.io/Upsample-Anything/})  
  Keywords: segmentation, semantic, gaussian splatting, ar, lightweight  



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