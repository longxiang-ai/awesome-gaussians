# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-09-06 00:47:52

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
- [Avatar Generation](#avatar-generation) (325 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (390 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (70 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (307 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (72 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (411 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (166 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (18 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (113 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (151 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (194 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: high-fidelity, semantic, gaussian splatting, understanding, compact, segmentation, nerf, lighting, 3d gaussian, survey, ar  
- **[A Study of the Framework and Real-World Applications of Language
  Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: semantic, gaussian splatting, understanding, efficient, nerf, 3d gaussian, robotics, survey, ar  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned
  and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: human, gaussian splatting, nerf, 3d gaussian, robotics, survey, ar  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: sparse-view, gaussian splatting, geometry, nerf, 3d reconstruction, motion, vr, 3d gaussian, robotics, survey, ar  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v2)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v2.pdf)  
  Keywords: human, gaussian splatting, slam, nerf, 3d reconstruction, lighting, dynamic, vr, 3d gaussian, robotics, survey, fast, ar  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: autonomous driving, high-fidelity, gaussian splatting, efficient, nerf, dynamic, 3d gaussian, face, survey, outdoor, ar  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: autonomous driving, high-fidelity, gaussian splatting, neural rendering, nerf, 3d reconstruction, vr, 3d gaussian, robotics, survey, ar  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: high-fidelity, semantic, gaussian splatting, understanding, neural rendering, efficient, segmentation, 3d reconstruction, 3d gaussian, survey, outdoor, ar  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: semantic, gaussian splatting, slam, ar, efficient, segmentation, nerf, 3d gaussian, survey, localization, mapping  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to
  Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: gaussian splatting, understanding, body, dynamic, motion, 3d gaussian, 4d, survey, ar  

### Acceleration

*Showing the latest 50 out of 264 papers*

- **[ContraGS: Codebook-Condensed and Trainable Gaussian Splatting for Fast,
  Memory-Efficient Reconstruction](https://arxiv.org/abs/2509.03775v1)**  
  Authors: Sankeerth Durvasula, Sharanshangar Muhunthan, Zain Moustafa, Richard Chen, Ruofan Liang, Yushi Guan, Nilesh Ahuja, Nilesh Jain, Selvakumar Panneer, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.03775v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, compact, high quality, efficient, 3d gaussian, fast, ar  
- **[GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned
  Residuals](https://arxiv.org/abs/2509.02141v1)**  
  Authors: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.02141v1.pdf)  
  Keywords: high-fidelity, real-time rendering, gaussian splatting, lightweight, deformation, geometry, face, head, vr, animation, fast, ar  
- **[GaussianGAN: Real-Time Photorealistic controllable Human Avatars](https://arxiv.org/abs/2509.01681v1)**  
  Authors: Mohamed Ilyes Lakhal, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01681v1.pdf)  
  Keywords: semantic, human, gaussian splatting, avatar, neural rendering, segmentation, face, 4d, fast, ar  
- **[Towards Integrating Multi-Spectral Imaging with Gaussian Splatting](https://arxiv.org/abs/2509.00989v1)**  
  Authors: Josef Grün, Lukas Meyer, Maximilian Weiherer, Bernhard Egger, Marc Stamminger, Linus Franke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00989v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, compact, geometry, 3d reconstruction, 3d gaussian, fast, ar  
- **[AGS: Accelerating 3D Gaussian Splatting SLAM via CODEC-Assisted Frame
  Covisibility Detection](https://arxiv.org/abs/2509.00433v1)**  
  Authors: Houshu He, Naifeng Jing, Li Jiang, Xiaoyao Liang, Zhuoran Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00433v1.pdf)  
  Keywords: slam, gaussian splatting, ar, acceleration, tracking, efficient, 3d gaussian, localization, mapping  
- **[Scale-GS: Efficient Scalable Gaussian Splatting via Redundancy-filtering
  Training on Streaming Content](https://arxiv.org/abs/2508.21444v1)**  
  Authors: Jiayu Yang, Weijian Su, Songqian Zhang, Yuqi Han, Jinli Suo, Qiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.21444v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, efficient, dynamic, head, motion, 3d gaussian, real-time rendering, ar  
- **[MAPo : Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for
  High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2508.19786v1)**  
  Authors: Han Jiao, Jiakai Sun, Yexing Xu, Lei Zhao, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19786v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, dynamic, motion, 3d gaussian, fast, ar  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, avatar, tracking, face, head, 3d gaussian, animation, fast, ar  
- **[LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation](https://arxiv.org/abs/2508.19699v1)**  
  Authors: Yupeng Zhang, Dezhi Zheng, Ping Lu, Han Zhang, Lei Wang, Liping xiang, Cheng Luo, Kaijun Deng, Xiaowen Fu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19699v1.pdf)  
  Keywords: high-fidelity, semantic, efficient rendering, gaussian splatting, understanding, efficient, segmentation, 3d gaussian, ar  
- **[ColorGS: High-fidelity Surgical Scene Reconstruction with Colored
  Gaussian Splatting](https://arxiv.org/abs/2508.18696v1)**  
  Authors: Qun Ji, Peng Li, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18696v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, efficient, nerf, lighting, dynamic, motion, vr, 3d gaussian, real-time rendering, ar  

### Applications

*Showing the latest 50 out of 995 papers*

- **[SSGaussian: Semantic-Aware and Structure-Preserving 3D Style Transfer](https://arxiv.org/abs/2509.04379v1)**  
  Authors: Jimin Xu, Bosheng Qin, Tao Jin, Zhou Zhao, Zhenhui Ye, Jun Yu, Fei Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.04379v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jm-xu.github.io/SSGaussian)  
  Keywords: ar, 3d gaussian, semantic, gaussian splatting  
- **[ContraGS: Codebook-Condensed and Trainable Gaussian Splatting for Fast,
  Memory-Efficient Reconstruction](https://arxiv.org/abs/2509.03775v1)**  
  Authors: Sankeerth Durvasula, Sharanshangar Muhunthan, Zain Moustafa, Richard Chen, Ruofan Liang, Yushi Guan, Nilesh Ahuja, Nilesh Jain, Selvakumar Panneer, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.03775v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, compact, high quality, efficient, 3d gaussian, fast, ar  
- **[GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned
  Residuals](https://arxiv.org/abs/2509.02141v1)**  
  Authors: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.02141v1.pdf)  
  Keywords: high-fidelity, real-time rendering, gaussian splatting, lightweight, deformation, geometry, face, head, vr, animation, fast, ar  
- **[2D Gaussian Splatting with Semantic Alignment for Image Inpainting](https://arxiv.org/abs/2509.01964v1)**  
  Authors: Hongyu Li, Chaofeng Chen, Xiaoming Li, Guangming Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01964v1.pdf)  
  Keywords: semantic, gaussian splatting, efficient, head, ar  
- **[GaussianGAN: Real-Time Photorealistic controllable Human Avatars](https://arxiv.org/abs/2509.01681v1)**  
  Authors: Mohamed Ilyes Lakhal, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01681v1.pdf)  
  Keywords: semantic, human, gaussian splatting, avatar, neural rendering, segmentation, face, 4d, fast, ar  
- **[Im2Haircut: Single-view Strand-based Hair Reconstruction for Human
  Avatars](https://arxiv.org/abs/2509.01469v1)**  
  Authors: Vanessa Sklyarova, Egor Zakharov, Malte Prinzler, Giorgio Becherini, Michael J. Black, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://im2haircut.is.tue.mpg.de.)  
  Keywords: avatar, ar, human, geometry  
- **[Towards Integrating Multi-Spectral Imaging with Gaussian Splatting](https://arxiv.org/abs/2509.00989v1)**  
  Authors: Josef Grün, Lukas Meyer, Maximilian Weiherer, Bernhard Egger, Marc Stamminger, Linus Franke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00989v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, compact, geometry, 3d reconstruction, 3d gaussian, fast, ar  
- **[GS-TG: 3D Gaussian Splatting Accelerator with Tile Grouping for Reducing
  Redundant Sorting while Preserving Rasterization Efficiency](https://arxiv.org/abs/2509.00911v2)**  
  Authors: Joongho Jo, Jongsun Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00911v2.pdf)  
  Keywords: gaussian splatting, efficient, nerf, 3d gaussian, ar  
- **[SWAGSplatting: Semantic-guided Water-scene Augmented Gaussian Splatting](https://arxiv.org/abs/2509.00800v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00800v1.pdf)  
  Keywords: high-fidelity, semantic, gaussian splatting, understanding, nerf, 3d reconstruction, 3d gaussian, ar  
- **[MarkSplatter: Generalizable Watermarking for 3D Gaussian Splatting Model
  via Splatter Image Structure](https://arxiv.org/abs/2509.00757v1)**  
  Authors: Xiufeng Huang, Ziyuan Luo, Qi Song, Ruofei Wang, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00757v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kevinhuangxf.github.io/marksplatter.)  
  Keywords: gaussian splatting, efficient, segmentation, 3d gaussian, ar  

### Avatar Generation

*Showing the latest 50 out of 325 papers*

- **[GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned
  Residuals](https://arxiv.org/abs/2509.02141v1)**  
  Authors: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.02141v1.pdf)  
  Keywords: high-fidelity, real-time rendering, gaussian splatting, lightweight, deformation, geometry, face, head, vr, animation, fast, ar  
- **[2D Gaussian Splatting with Semantic Alignment for Image Inpainting](https://arxiv.org/abs/2509.01964v1)**  
  Authors: Hongyu Li, Chaofeng Chen, Xiaoming Li, Guangming Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01964v1.pdf)  
  Keywords: semantic, gaussian splatting, efficient, head, ar  
- **[GaussianGAN: Real-Time Photorealistic controllable Human Avatars](https://arxiv.org/abs/2509.01681v1)**  
  Authors: Mohamed Ilyes Lakhal, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01681v1.pdf)  
  Keywords: semantic, human, gaussian splatting, avatar, neural rendering, segmentation, face, 4d, fast, ar  
- **[Im2Haircut: Single-view Strand-based Hair Reconstruction for Human
  Avatars](https://arxiv.org/abs/2509.01469v1)**  
  Authors: Vanessa Sklyarova, Egor Zakharov, Malte Prinzler, Giorgio Becherini, Michael J. Black, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://im2haircut.is.tue.mpg.de.)  
  Keywords: avatar, ar, human, geometry  
- **[Complete Gaussian Splats from a Single Image with Denoising Diffusion
  Models](https://arxiv.org/abs/2508.21542v1)**  
  Authors: Ziwei Liao, Mohamed Sayed, Steven L. Waslander, Sara Vicente, Daniyar Turmukhambetov, Michael Firman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.21542v1.pdf)  
  Keywords: ar, face, gaussian splatting  
- **[Scale-GS: Efficient Scalable Gaussian Splatting via Redundancy-filtering
  Training on Streaming Content](https://arxiv.org/abs/2508.21444v1)**  
  Authors: Jiayu Yang, Weijian Su, Songqian Zhang, Yuqi Han, Jinli Suo, Qiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.21444v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, efficient, dynamic, head, motion, 3d gaussian, real-time rendering, ar  
- **[ARGS: Advanced Regularization on Aligning Gaussians over the Surface](https://arxiv.org/abs/2508.21344v1)**  
  Authors: Jeong Uk Lee, Sung Hee Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.21344v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d gaussian, face, ar  
- **[AvatarBack: Back-Head Generation for Complete 3D Avatars from Front-View
  Images](https://arxiv.org/abs/2508.20623v1)**  
  Authors: Shiqi Xin, Xiaolin Zhang, Yanbin Liu, Peng Zhang, Caifeng Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20623v1.pdf)  
  Keywords: gaussian splatting, avatar, head, motion, 3d gaussian, ar  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, avatar, tracking, face, head, 3d gaussian, animation, fast, ar  
- **[PseudoMapTrainer: Learning Online Mapping without HD Maps](https://arxiv.org/abs/2508.18788v1)**  
  Authors: Christian Löwens, Thorben Funke, Jingchao Xie, Alexandru Paul Condurache  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18788v1.pdf)  
  Keywords: semantic, gaussian splatting, ar, segmentation, face, mapping  

### Dynamic Scene

*Showing the latest 50 out of 390 papers*

- **[GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned
  Residuals](https://arxiv.org/abs/2509.02141v1)**  
  Authors: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.02141v1.pdf)  
  Keywords: high-fidelity, real-time rendering, gaussian splatting, lightweight, deformation, geometry, face, head, vr, animation, fast, ar  
- **[GaussianGAN: Real-Time Photorealistic controllable Human Avatars](https://arxiv.org/abs/2509.01681v1)**  
  Authors: Mohamed Ilyes Lakhal, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01681v1.pdf)  
  Keywords: semantic, human, gaussian splatting, avatar, neural rendering, segmentation, face, 4d, fast, ar  
- **[DyPho-SLAM : Real-time Photorealistic SLAM in Dynamic Environments](https://arxiv.org/abs/2509.00741v1)**  
  Authors: Yi Liu, Keyu Fan, Bin Lan, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00741v1.pdf)  
  Keywords: high-fidelity, slam, gaussian splatting, ar, tracking, efficient, dynamic, localization, mapping  
- **[Scale-GS: Efficient Scalable Gaussian Splatting via Redundancy-filtering
  Training on Streaming Content](https://arxiv.org/abs/2508.21444v1)**  
  Authors: Jiayu Yang, Weijian Su, Songqian Zhang, Yuqi Han, Jinli Suo, Qiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.21444v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, efficient, dynamic, head, motion, 3d gaussian, real-time rendering, ar  
- **[AvatarBack: Back-Head Generation for Complete 3D Avatars from Front-View
  Images](https://arxiv.org/abs/2508.20623v1)**  
  Authors: Shiqi Xin, Xiaolin Zhang, Yanbin Liu, Peng Zhang, Caifeng Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20623v1.pdf)  
  Keywords: gaussian splatting, avatar, head, motion, 3d gaussian, ar  
- **[MAPo : Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for
  High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2508.19786v1)**  
  Authors: Han Jiao, Jiakai Sun, Yexing Xu, Lei Zhao, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19786v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, dynamic, motion, 3d gaussian, fast, ar  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, avatar, tracking, face, head, 3d gaussian, animation, fast, ar  
- **[Style4D-Bench: A Benchmark Suite for 4D Stylization](https://arxiv.org/abs/2508.19243v1)**  
  Authors: Beiqi Chen, Shuai Shao, Haitang Feng, Jianhuang Lai, Jianlou Si, Guangcong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19243v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://becky-catherine.github.io/Style4D)  
  Keywords: gaussian splatting, lightweight, geometry, dynamic, motion, 4d, ar  
- **[ColorGS: High-fidelity Surgical Scene Reconstruction with Colored
  Gaussian Splatting](https://arxiv.org/abs/2508.18696v1)**  
  Authors: Qun Ji, Peng Li, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18696v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, efficient, nerf, lighting, dynamic, motion, vr, 3d gaussian, real-time rendering, ar  
- **[IDU: Incremental Dynamic Update of Existing 3D Virtual Environments with
  New Imagery Data](https://arxiv.org/abs/2508.17579v1)**  
  Authors: Meida Chen, Luis Leal, Yue Hu, Rong Liu, Butian Xiong, Andrew Feng, Jiuyi Xu, Yangming Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17579v1.pdf)  
  Keywords: human, gaussian splatting, efficient, 3d reconstruction, dynamic, 3d gaussian, ar  

### Few-shot

*Showing the latest 50 out of 70 papers*

- **[${C}^{3}$-GS: Learning Context-aware, Cross-dimension, Cross-scale
  Feature for Generalizable Gaussian Splatting](https://arxiv.org/abs/2508.20754v1)**  
  Authors: Yuxi Hu, Jun Zhang, Kuangyi Chen, Zhe Zhang, Friedrich Fraundorfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20754v1.pdf)  
  Keywords: lightweight, gaussian splatting, geometry, sparse view, ar  
- **[MeshSplat: Generalizable Sparse-View Surface Reconstruction via Gaussian
  Splatting](https://arxiv.org/abs/2508.17811v1)**  
  Authors: Hanzhi Chang, Ruijie Zhu, Wenjie Chang, Mulin Yu, Yanzhe Liang, Jiahao Lu, Zhuoyuan Li, Tianzhu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17811v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanzhichang.github.io/meshsplat_web)  
  Keywords: sparse-view, gaussian splatting, geometry, face, ar  
- **[Enhancing Novel View Synthesis from extremely sparse views with SfM-free
  3D Gaussian Splatting Framework](https://arxiv.org/abs/2508.15457v1)**  
  Authors: Zongqi He, Hanmin Li, Kin-Chung Chan, Yushen Zuo, Hao Xie, Zhe Xiao, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15457v1.pdf)  
  Keywords: sparse-view, gaussian splatting, geometry, motion, 3d gaussian, sparse view, ar  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v2)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v2.pdf)  
  Keywords: autonomous driving, relighting, gaussian splatting, geometry, lighting, 3d gaussian, face, sparse view, outdoor, ar  
- **[Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.12720v2)**  
  Authors: Kangjie Chen, Yingji Zhong, Zhihao Li, Jiaqi Lin, Youyu Chen, Minghan Qin, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12720v2.pdf)  
  Keywords: sparse-view, lightweight, gaussian splatting, understanding, 3d gaussian, ar  
- **[Toward Human-Robot Teaming: Learning Handover Behaviors from 3D Scenes](https://arxiv.org/abs/2508.09855v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09855v1.pdf)  
  Keywords: sparse-view, ar, human, gaussian splatting  
- **[GSFixer: Improving 3D Gaussian Splatting with Reference-Guided Video
  Diffusion Priors](https://arxiv.org/abs/2508.09667v1)**  
  Authors: Xingyilang Yin, Qi Zhang, Jiahao Chang, Ying Feng, Qingnan Fan, Xi Yang, Chi-Man Pun, Huaqi Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09667v1.pdf)  
  Keywords: sparse-view, semantic, gaussian splatting, geometry, 3d reconstruction, 3d gaussian, sparse view, ar  
- **[SkySplat: Generalizable 3D Gaussian Splatting from Multi-Temporal Sparse
  Satellite Images](https://arxiv.org/abs/2508.09479v1)**  
  Authors: Xuejun Huang, Xinyi Liu, Yi Wan, Zhi Zheng, Bin Zhang, Mingtao Xiong, Yingying Pei, Yongjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09479v1.pdf)  
  Keywords: sparse-view, gaussian splatting, efficient, 3d gaussian, ar  
- **[DIP-GS: Deep Image Prior For Gaussian Splatting Sparse View Recovery](https://arxiv.org/abs/2508.07372v1)**  
  Authors: Rajaei Khatib, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07372v1.pdf)  
  Keywords: sparse-view, gaussian splatting, 3d gaussian, sparse view, real-time rendering, ar  
- **[UGOD: Uncertainty-Guided Differentiable Opacity and Soft Dropout for
  Enhanced Sparse-View 3DGS](https://arxiv.org/abs/2508.04968v1)**  
  Authors: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Liangxiu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04968v1.pdf)  
  Keywords: sparse-view, gaussian splatting, nerf, 3d gaussian, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 307 papers*

- **[GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned
  Residuals](https://arxiv.org/abs/2509.02141v1)**  
  Authors: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.02141v1.pdf)  
  Keywords: high-fidelity, real-time rendering, gaussian splatting, lightweight, deformation, geometry, face, head, vr, animation, fast, ar  
- **[Im2Haircut: Single-view Strand-based Hair Reconstruction for Human
  Avatars](https://arxiv.org/abs/2509.01469v1)**  
  Authors: Vanessa Sklyarova, Egor Zakharov, Malte Prinzler, Giorgio Becherini, Michael J. Black, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://im2haircut.is.tue.mpg.de.)  
  Keywords: avatar, ar, human, geometry  
- **[Towards Integrating Multi-Spectral Imaging with Gaussian Splatting](https://arxiv.org/abs/2509.00989v1)**  
  Authors: Josef Grün, Lukas Meyer, Maximilian Weiherer, Bernhard Egger, Marc Stamminger, Linus Franke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00989v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, compact, geometry, 3d reconstruction, 3d gaussian, fast, ar  
- **[SWAGSplatting: Semantic-guided Water-scene Augmented Gaussian Splatting](https://arxiv.org/abs/2509.00800v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00800v1.pdf)  
  Keywords: high-fidelity, semantic, gaussian splatting, understanding, nerf, 3d reconstruction, 3d gaussian, ar  
- **[ARGS: Advanced Regularization on Aligning Gaussians over the Surface](https://arxiv.org/abs/2508.21344v1)**  
  Authors: Jeong Uk Lee, Sung Hee Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.21344v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d gaussian, face, ar  
- **[${C}^{3}$-GS: Learning Context-aware, Cross-dimension, Cross-scale
  Feature for Generalizable Gaussian Splatting](https://arxiv.org/abs/2508.20754v1)**  
  Authors: Yuxi Hu, Jun Zhang, Kuangyi Chen, Zhe Zhang, Friedrich Fraundorfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20754v1.pdf)  
  Keywords: lightweight, gaussian splatting, geometry, sparse view, ar  
- **[Style4D-Bench: A Benchmark Suite for 4D Stylization](https://arxiv.org/abs/2508.19243v1)**  
  Authors: Beiqi Chen, Shuai Shao, Haitang Feng, Jianhuang Lai, Jianlou Si, Guangcong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19243v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://becky-catherine.github.io/Style4D)  
  Keywords: gaussian splatting, lightweight, geometry, dynamic, motion, 4d, ar  
- **[Camera Pose Refinement via 3D Gaussian Splatting](https://arxiv.org/abs/2508.17876v1)**  
  Authors: Lulu Hao, Lipu Zhou, Zhenzhong Wei, Xu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17876v1.pdf)  
  Keywords: lightweight, gaussian splatting, geometry, 3d gaussian, ar  
- **[MeshSplat: Generalizable Sparse-View Surface Reconstruction via Gaussian
  Splatting](https://arxiv.org/abs/2508.17811v1)**  
  Authors: Hanzhi Chang, Ruijie Zhu, Wenjie Chang, Mulin Yu, Yanzhe Liang, Jiahao Lu, Zhuoyuan Li, Tianzhu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17811v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanzhichang.github.io/meshsplat_web)  
  Keywords: sparse-view, gaussian splatting, geometry, face, ar  
- **[IDU: Incremental Dynamic Update of Existing 3D Virtual Environments with
  New Imagery Data](https://arxiv.org/abs/2508.17579v1)**  
  Authors: Meida Chen, Luis Leal, Yue Hu, Rong Liu, Butian Xiong, Andrew Feng, Jiuyi Xu, Yangming Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17579v1.pdf)  
  Keywords: human, gaussian splatting, efficient, 3d reconstruction, dynamic, 3d gaussian, ar  

### Large Scene

*Showing the latest 50 out of 72 papers*

- **[GSVisLoc: Generalizable Visual Localization for Gaussian Splatting Scene
  Representations](https://arxiv.org/abs/2508.18242v1)**  
  Authors: Fadi Khatib, Dror Moran, Guy Trostianetsky, Yoni Kasten, Meirav Galun, Ronen Basri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18242v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, localization, outdoor, ar  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v2)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v2.pdf)  
  Keywords: autonomous driving, relighting, gaussian splatting, geometry, lighting, 3d gaussian, face, sparse view, outdoor, ar  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: gaussian splatting, understanding, illumination, 3d reconstruction, lighting, 3d gaussian, outdoor, ar  
- **[Online 3D Gaussian Splatting Modeling with Novel View Selection](https://arxiv.org/abs/2508.14014v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14014v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, outdoor, ar  
- **[InstDrive: Instance-Aware 3D Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2508.12015v1)**  
  Authors: Hongyuan Liu, Haochen Yu, Jianfei Jiang, Qiankun Liu, Jiansheng Chen, Huimin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.12015v1.pdf)  
  Keywords: lightweight, gaussian splatting, understanding, segmentation, dynamic, 3d gaussian, autonomous driving, outdoor, ar  
- **[Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian
  Splatting](https://arxiv.org/abs/2508.11431v1)**  
  Authors: Simona Kocour, Assia Benbihi, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11431v1.pdf)  
  Keywords: semantic, gaussian splatting, understanding, geometry, 3d reconstruction, 3d gaussian, face, outdoor, ar  
- **[Multi-view Normal and Distance Guidance Gaussian Splatting for Surface
  Reconstruction](https://arxiv.org/abs/2508.07701v2)**  
  Authors: Bo Jia, Yanan Guo, Ying Chang, Benkui Zhang, Ying Xie, Kangning Du, Lin Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07701v2.pdf)  
  Keywords: gaussian splatting, geometry, 3d gaussian, face, outdoor, ar  
- **[GS4Buildings: Prior-Guided Gaussian Splatting for 3D Building
  Reconstruction](https://arxiv.org/abs/2508.07355v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07355v1.pdf)  
  Keywords: semantic, gaussian splatting, compact, geometry, efficient, urban scene, 3d reconstruction, motion, face, ar  
- **[Evaluating Fisheye-Compatible 3D Gaussian Splatting Methods on Real
  Images Beyond 180 Degree Field of View](https://arxiv.org/abs/2508.06968v1)**  
  Authors: Ulas Gunes, Matias Turkulainen, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06968v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, 3d gaussian, outdoor, ar  
- **[Neural Gaussian Radio Fields for Channel Estimation](https://arxiv.org/abs/2508.11668v1)**  
  Authors: Muhammad Umer, Muhammad Ahmed Mohsin, Ahsan Bilal, John M. Cioffi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.11668v1.pdf)  
  Keywords: gaussian splatting, efficient, nerf, dynamic, head, 3d gaussian, outdoor, ar  

### Model Compression

*Showing the latest 50 out of 411 papers*

- **[ContraGS: Codebook-Condensed and Trainable Gaussian Splatting for Fast,
  Memory-Efficient Reconstruction](https://arxiv.org/abs/2509.03775v1)**  
  Authors: Sankeerth Durvasula, Sharanshangar Muhunthan, Zain Moustafa, Richard Chen, Ruofan Liang, Yushi Guan, Nilesh Ahuja, Nilesh Jain, Selvakumar Panneer, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.03775v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, compact, high quality, efficient, 3d gaussian, fast, ar  
- **[GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned
  Residuals](https://arxiv.org/abs/2509.02141v1)**  
  Authors: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.02141v1.pdf)  
  Keywords: high-fidelity, real-time rendering, gaussian splatting, lightweight, deformation, geometry, face, head, vr, animation, fast, ar  
- **[2D Gaussian Splatting with Semantic Alignment for Image Inpainting](https://arxiv.org/abs/2509.01964v1)**  
  Authors: Hongyu Li, Chaofeng Chen, Xiaoming Li, Guangming Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01964v1.pdf)  
  Keywords: semantic, gaussian splatting, efficient, head, ar  
- **[Towards Integrating Multi-Spectral Imaging with Gaussian Splatting](https://arxiv.org/abs/2509.00989v1)**  
  Authors: Josef Grün, Lukas Meyer, Maximilian Weiherer, Bernhard Egger, Marc Stamminger, Linus Franke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00989v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, compact, geometry, 3d reconstruction, 3d gaussian, fast, ar  
- **[GS-TG: 3D Gaussian Splatting Accelerator with Tile Grouping for Reducing
  Redundant Sorting while Preserving Rasterization Efficiency](https://arxiv.org/abs/2509.00911v2)**  
  Authors: Joongho Jo, Jongsun Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00911v2.pdf)  
  Keywords: gaussian splatting, efficient, nerf, 3d gaussian, ar  
- **[MarkSplatter: Generalizable Watermarking for 3D Gaussian Splatting Model
  via Splatter Image Structure](https://arxiv.org/abs/2509.00757v1)**  
  Authors: Xiufeng Huang, Ziyuan Luo, Qi Song, Ruofei Wang, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00757v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kevinhuangxf.github.io/marksplatter.)  
  Keywords: gaussian splatting, efficient, segmentation, 3d gaussian, ar  
- **[DyPho-SLAM : Real-time Photorealistic SLAM in Dynamic Environments](https://arxiv.org/abs/2509.00741v1)**  
  Authors: Yi Liu, Keyu Fan, Bin Lan, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00741v1.pdf)  
  Keywords: high-fidelity, slam, gaussian splatting, ar, tracking, efficient, dynamic, localization, mapping  
- **[AGS: Accelerating 3D Gaussian Splatting SLAM via CODEC-Assisted Frame
  Covisibility Detection](https://arxiv.org/abs/2509.00433v1)**  
  Authors: Houshu He, Naifeng Jing, Li Jiang, Xiaoyao Liang, Zhuoran Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00433v1.pdf)  
  Keywords: slam, gaussian splatting, ar, acceleration, tracking, efficient, 3d gaussian, localization, mapping  
- **[Scale-GS: Efficient Scalable Gaussian Splatting via Redundancy-filtering
  Training on Streaming Content](https://arxiv.org/abs/2508.21444v1)**  
  Authors: Jiayu Yang, Weijian Su, Songqian Zhang, Yuqi Han, Jinli Suo, Qiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.21444v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, efficient, dynamic, head, motion, 3d gaussian, real-time rendering, ar  
- **[${C}^{3}$-GS: Learning Context-aware, Cross-dimension, Cross-scale
  Feature for Generalizable Gaussian Splatting](https://arxiv.org/abs/2508.20754v1)**  
  Authors: Yuxi Hu, Jun Zhang, Kuangyi Chen, Zhe Zhang, Friedrich Fraundorfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20754v1.pdf)  
  Keywords: lightweight, gaussian splatting, geometry, sparse view, ar  

### Quality Enhancement

*Showing the latest 50 out of 166 papers*

- **[ContraGS: Codebook-Condensed and Trainable Gaussian Splatting for Fast,
  Memory-Efficient Reconstruction](https://arxiv.org/abs/2509.03775v1)**  
  Authors: Sankeerth Durvasula, Sharanshangar Muhunthan, Zain Moustafa, Richard Chen, Ruofan Liang, Yushi Guan, Nilesh Ahuja, Nilesh Jain, Selvakumar Panneer, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.03775v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, compact, high quality, efficient, 3d gaussian, fast, ar  
- **[GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned
  Residuals](https://arxiv.org/abs/2509.02141v1)**  
  Authors: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.02141v1.pdf)  
  Keywords: high-fidelity, real-time rendering, gaussian splatting, lightweight, deformation, geometry, face, head, vr, animation, fast, ar  
- **[Towards Integrating Multi-Spectral Imaging with Gaussian Splatting](https://arxiv.org/abs/2509.00989v1)**  
  Authors: Josef Grün, Lukas Meyer, Maximilian Weiherer, Bernhard Egger, Marc Stamminger, Linus Franke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00989v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, compact, geometry, 3d reconstruction, 3d gaussian, fast, ar  
- **[SWAGSplatting: Semantic-guided Water-scene Augmented Gaussian Splatting](https://arxiv.org/abs/2509.00800v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00800v1.pdf)  
  Keywords: high-fidelity, semantic, gaussian splatting, understanding, nerf, 3d reconstruction, 3d gaussian, ar  
- **[DyPho-SLAM : Real-time Photorealistic SLAM in Dynamic Environments](https://arxiv.org/abs/2509.00741v1)**  
  Authors: Yi Liu, Keyu Fan, Bin Lan, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00741v1.pdf)  
  Keywords: high-fidelity, slam, gaussian splatting, ar, tracking, efficient, dynamic, localization, mapping  
- **[Scale-GS: Efficient Scalable Gaussian Splatting via Redundancy-filtering
  Training on Streaming Content](https://arxiv.org/abs/2508.21444v1)**  
  Authors: Jiayu Yang, Weijian Su, Songqian Zhang, Yuqi Han, Jinli Suo, Qiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.21444v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, efficient, dynamic, head, motion, 3d gaussian, real-time rendering, ar  
- **[MAPo : Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for
  High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2508.19786v1)**  
  Authors: Han Jiao, Jiakai Sun, Yexing Xu, Lei Zhao, Wei Xing, Huaizhong Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19786v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, dynamic, motion, 3d gaussian, fast, ar  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, avatar, tracking, face, head, 3d gaussian, animation, fast, ar  
- **[LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation](https://arxiv.org/abs/2508.19699v1)**  
  Authors: Yupeng Zhang, Dezhi Zheng, Ping Lu, Han Zhang, Lei Wang, Liping xiang, Cheng Luo, Kaijun Deng, Xiaowen Fu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19699v1.pdf)  
  Keywords: high-fidelity, semantic, efficient rendering, gaussian splatting, understanding, efficient, segmentation, 3d gaussian, ar  
- **[ColorGS: High-fidelity Surgical Scene Reconstruction with Colored
  Gaussian Splatting](https://arxiv.org/abs/2508.18696v1)**  
  Authors: Qun Ji, Peng Li, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18696v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, efficient, nerf, lighting, dynamic, motion, vr, 3d gaussian, real-time rendering, ar  

### Ray Tracing

- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: relighting, high-fidelity, gaussian splatting, ray tracing, geometry, nerf, illumination, lighting, 3d gaussian, face, reflection, ar  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: relighting, relightable, gaussian splatting, global illumination, illumination, lighting, dynamic, 3d gaussian, face, shadow, outdoor, ar  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: path tracing, gaussian splatting, lighting, dynamic, 3d gaussian, face, ar  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relighting, relightable, efficient rendering, gaussian splatting, ray marching, geometry, efficient, lighting, 3d gaussian, face, ar  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ray tracing, efficient, real-time rendering, ar  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v2)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v2.pdf)  
  Keywords: relighting, human, relightable, gaussian splatting, ray tracing, avatar, geometry, lighting, shadow, fast, ar  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: relighting, efficient rendering, ray tracing, gaussian splatting, acceleration, efficient, lighting, 3d gaussian, ar  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: gaussian splatting, compact, acceleration, ray marching, efficient, dynamic, 3d gaussian, animation, ar  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: gaussian splatting, ray tracing, efficient, global illumination, illumination, lighting, 3d gaussian, face, real-time rendering, ar  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: gaussian splatting, ray tracing, neural rendering, reflection, 3d gaussian, shadow, fast, ar  

### Relighting

*Showing the latest 50 out of 113 papers*

- **[ColorGS: High-fidelity Surgical Scene Reconstruction with Colored
  Gaussian Splatting](https://arxiv.org/abs/2508.18696v1)**  
  Authors: Qun Ji, Peng Li, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18696v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, efficient, nerf, lighting, dynamic, motion, vr, 3d gaussian, real-time rendering, ar  
- **[Fiducial Marker Splatting for High-Fidelity Robotics Simulations](https://arxiv.org/abs/2508.17012v1)**  
  Authors: Diram Tabaa, Gianni Di Caro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17012v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, neural rendering, efficient, lighting, robotics, localization, ar  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v2)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v2.pdf)  
  Keywords: autonomous driving, relighting, gaussian splatting, geometry, lighting, 3d gaussian, face, sparse view, outdoor, ar  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: relighting, high-fidelity, gaussian splatting, ray tracing, geometry, nerf, illumination, lighting, 3d gaussian, face, reflection, ar  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: gaussian splatting, understanding, illumination, 3d reconstruction, lighting, 3d gaussian, outdoor, ar  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: high-fidelity, semantic, gaussian splatting, understanding, compact, segmentation, nerf, lighting, 3d gaussian, survey, ar  
- **[HumanGenesis: Agent-Based Geometric and Generative Modeling for
  Synthetic Human Dynamics](https://arxiv.org/abs/2508.09858v1)**  
  Authors: Weiqi Li, Zehao Zhang, Liang Lin, Guangrun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09858v1.pdf)  
  Keywords: human, gaussian splatting, deformation, face, dynamic, motion, 3d gaussian, 4d, reflection, ar  
- **[Vision-Only Gaussian Splatting for Collaborative Semantic Occupancy
  Prediction](https://arxiv.org/abs/2508.10936v1)**  
  Authors: Cheng Chen, Hao Huang, Saurabh Bagchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.10936v1.pdf)  
  Keywords: semantic, gaussian splatting, geometry, lighting, ar  
- **[Touch-Augmented Gaussian Splatting for Enhanced 3D Scene Reconstruction](https://arxiv.org/abs/2508.07717v1)**  
  Authors: Yuchen Gao, Xiao Xu, Eckehard Steinbach, Daniel E. Lucani, Qi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07717v1.pdf)  
  Keywords: gaussian splatting, geometry, lighting, 3d gaussian, face, ar  
- **[UW-3DGS: Underwater 3D Reconstruction with Physics-Aware Gaussian
  Splatting](https://arxiv.org/abs/2508.06169v1)**  
  Authors: Wenpeng Xing, Jie Chen, Zaifeng Yang, Changting Lin, Jianfeng Dong, Chaochao Chen, Xun Zhou, Meng Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06169v1.pdf)  
  Keywords: light transport, gaussian splatting, geometry, nerf, 3d reconstruction, 3d gaussian, face, ar  

### SLAM

*Showing the latest 50 out of 151 papers*

- **[DyPho-SLAM : Real-time Photorealistic SLAM in Dynamic Environments](https://arxiv.org/abs/2509.00741v1)**  
  Authors: Yi Liu, Keyu Fan, Bin Lan, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00741v1.pdf)  
  Keywords: high-fidelity, slam, gaussian splatting, ar, tracking, efficient, dynamic, localization, mapping  
- **[AGS: Accelerating 3D Gaussian Splatting SLAM via CODEC-Assisted Frame
  Covisibility Detection](https://arxiv.org/abs/2509.00433v1)**  
  Authors: Houshu He, Naifeng Jing, Li Jiang, Xiaoyao Liang, Zhuoran Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00433v1.pdf)  
  Keywords: slam, gaussian splatting, ar, acceleration, tracking, efficient, 3d gaussian, localization, mapping  
- **[FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction
  with Large Gaussian Reconstruction Transformers](https://arxiv.org/abs/2508.19754v1)**  
  Authors: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19754v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, avatar, tracking, face, head, 3d gaussian, animation, fast, ar  
- **[PseudoMapTrainer: Learning Online Mapping without HD Maps](https://arxiv.org/abs/2508.18788v1)**  
  Authors: Christian Löwens, Thorben Funke, Jingchao Xie, Alexandru Paul Condurache  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18788v1.pdf)  
  Keywords: semantic, gaussian splatting, ar, segmentation, face, mapping  
- **[GSVisLoc: Generalizable Visual Localization for Gaussian Splatting Scene
  Representations](https://arxiv.org/abs/2508.18242v1)**  
  Authors: Fadi Khatib, Dror Moran, Guy Trostianetsky, Yoni Kasten, Meirav Galun, Ronen Basri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18242v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, localization, outdoor, ar  
- **[Fiducial Marker Splatting for High-Fidelity Robotics Simulations](https://arxiv.org/abs/2508.17012v1)**  
  Authors: Diram Tabaa, Gianni Di Caro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17012v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, neural rendering, efficient, lighting, robotics, localization, ar  
- **[From Slices to Structures: Unsupervised 3D Reconstruction of Female
  Pelvic Anatomy from Freehand Transvaginal Ultrasound](https://arxiv.org/abs/2508.14552v1)**  
  Authors: Max Krähenmann, Sergio Tascon-Morales, Fabian Laumer, Julia E. Vogt, Ece Ozkan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14552v1.pdf)  
  Keywords: gaussian splatting, compact, tracking, geometry, efficient, 3d reconstruction, motion, 3d gaussian, ar  
- **[Online 3D Gaussian Splatting Modeling with Novel View Selection](https://arxiv.org/abs/2508.14014v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14014v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, outdoor, ar  
- **[SAGOnline: Segment Any Gaussians Online](https://arxiv.org/abs/2508.08219v1)**  
  Authors: Wentao Sun, Quanyun Wu, Hanqing Xu, Kyle Gao, Zhengsen Xu, Yiping Chen, Dedong Zhang, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08219v1.pdf)  
  Keywords: gaussian splatting, lightweight, understanding, tracking, efficient, segmentation, nerf, vr, 3d gaussian, real-time rendering, ar  
- **[NeeCo: Image Synthesis of Novel Instrument States Based on Dynamic and
  Deformable 3D Gaussian Reconstruction](https://arxiv.org/abs/2508.07897v1)**  
  Authors: Tianle Zeng, Junlei Hu, Gerardo Loza Galindo, Sharib Ali, Duygu Sarikaya, Pietro Valdastri, Dominic Jones  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07897v1.pdf)  
  Keywords: gaussian splatting, deformation, tracking, medical, dynamic, motion, 3d gaussian, localization, ar  

### Scene Understanding

*Showing the latest 50 out of 194 papers*

- **[SSGaussian: Semantic-Aware and Structure-Preserving 3D Style Transfer](https://arxiv.org/abs/2509.04379v1)**  
  Authors: Jimin Xu, Bosheng Qin, Tao Jin, Zhou Zhao, Zhenhui Ye, Jun Yu, Fei Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.04379v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jm-xu.github.io/SSGaussian)  
  Keywords: ar, 3d gaussian, semantic, gaussian splatting  
- **[2D Gaussian Splatting with Semantic Alignment for Image Inpainting](https://arxiv.org/abs/2509.01964v1)**  
  Authors: Hongyu Li, Chaofeng Chen, Xiaoming Li, Guangming Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01964v1.pdf)  
  Keywords: semantic, gaussian splatting, efficient, head, ar  
- **[GaussianGAN: Real-Time Photorealistic controllable Human Avatars](https://arxiv.org/abs/2509.01681v1)**  
  Authors: Mohamed Ilyes Lakhal, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.01681v1.pdf)  
  Keywords: semantic, human, gaussian splatting, avatar, neural rendering, segmentation, face, 4d, fast, ar  
- **[SWAGSplatting: Semantic-guided Water-scene Augmented Gaussian Splatting](https://arxiv.org/abs/2509.00800v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00800v1.pdf)  
  Keywords: high-fidelity, semantic, gaussian splatting, understanding, nerf, 3d reconstruction, 3d gaussian, ar  
- **[MarkSplatter: Generalizable Watermarking for 3D Gaussian Splatting Model
  via Splatter Image Structure](https://arxiv.org/abs/2509.00757v1)**  
  Authors: Xiufeng Huang, Ziyuan Luo, Qi Song, Ruofei Wang, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00757v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kevinhuangxf.github.io/marksplatter.)  
  Keywords: gaussian splatting, efficient, segmentation, 3d gaussian, ar  
- **[LabelGS: Label-Aware 3D Gaussian Splatting for 3D Scene Segmentation](https://arxiv.org/abs/2508.19699v1)**  
  Authors: Yupeng Zhang, Dezhi Zheng, Ping Lu, Han Zhang, Lei Wang, Liping xiang, Cheng Luo, Kaijun Deng, Xiaowen Fu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.19699v1.pdf)  
  Keywords: high-fidelity, semantic, efficient rendering, gaussian splatting, understanding, efficient, segmentation, 3d gaussian, ar  
- **[PseudoMapTrainer: Learning Online Mapping without HD Maps](https://arxiv.org/abs/2508.18788v1)**  
  Authors: Christian Löwens, Thorben Funke, Jingchao Xie, Alexandru Paul Condurache  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18788v1.pdf)  
  Keywords: semantic, gaussian splatting, ar, segmentation, face, mapping  
- **[GWM: Towards Scalable Gaussian World Models for Robotic Manipulation](https://arxiv.org/abs/2508.17600v1)**  
  Authors: Guanxing Lu, Baoxiong Jia, Puhao Li, Yixin Chen, Ziwei Wang, Yansong Tang, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.17600v1.pdf)  
  Keywords: ar, understanding, gaussian splatting  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: gaussian splatting, understanding, illumination, 3d reconstruction, lighting, 3d gaussian, outdoor, ar  
- **[GALA: Guided Attention with Language Alignment for Open Vocabulary
  Gaussian Splatting](https://arxiv.org/abs/2508.14278v2)**  
  Authors: Elena Alegret, Kunyi Li, Sen Wang, Siyun Liang, Michael Niemeyer, Stefano Gasperini, Nassir Navab, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14278v2.pdf)  
  Keywords: semantic, gaussian splatting, understanding, 3d gaussian, ar  



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