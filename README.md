# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-11-20 00:52:53

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
- [Acceleration](#acceleration) (260 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (996 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (340 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (396 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (76 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (321 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (76 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (403 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (184 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (15 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (123 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (139 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (198 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: semantic, slam, 3d gaussian, localization, robotics, survey, high-fidelity, ar, mapping, gaussian splatting, efficient  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: 3d gaussian, 4d, geometry, fast, survey, motion, ar, nerf, gaussian splatting  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: avatar, 3d reconstruction, animation, 3d gaussian, ar, survey, efficient rendering, lighting, real-time rendering, face, gaussian splatting, efficient  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: survey, understanding, human, ar, lightweight, nerf, gaussian splatting, efficient  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: slam, 3d gaussian, ar, fast, survey, understanding, neural rendering, nerf, gaussian splatting, efficient  
- **[A-TDOM: Active TDOM via On-the-Fly 3DGS](https://arxiv.org/abs/2509.12759v2)**  
  Authors: Yiwei Xu, Xiang Wang, Yifei Yu, Wentian Gan, Luca Morelli, Giulio Perda, Xiongwu Xiao, Zongqian Zhan, Xin Wang, Fabio Remondino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.12759v2.pdf)  
  Keywords: face, survey, ar  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: 3d gaussian, survey, high-fidelity, lighting, segmentation, understanding, ar, compact, nerf, gaussian splatting, semantic  
- **[A Study of the Framework and Real-World Applications of Language Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: semantic, 3d gaussian, robotics, survey, understanding, ar, nerf, gaussian splatting, efficient  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: 3d gaussian, robotics, survey, human, ar, nerf, gaussian splatting  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: 3d reconstruction, vr, 3d gaussian, geometry, robotics, survey, sparse-view, motion, ar, nerf, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 260 papers*

- **[IBGS: Image-Based Gaussian Splatting](https://arxiv.org/abs/2511.14357v1)**  
  Authors: Hoang Chuong Nguyen, Wei Mao, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14357v1.pdf)  
  Keywords: 3d gaussian, fast, ar, head, face, gaussian splatting, efficient  
- **[SF-Recon: Simplification-Free Lightweight Building Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2511.13278v1)**  
  Authors: Zihan Li, Tengfei Wang, Wentian Gan, Hao Zhan, Xin Wang, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13278v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lzh282140127-cell.github.io/SF-Recon-project/)  
  Keywords: 3d gaussian, geometry, fast, ar, lightweight, face, gaussian splatting  
- **[Neo: Real-Time On-Device 3D Gaussian Splatting with Reuse-and-Update Sorting Acceleration](https://arxiv.org/abs/2511.12930v1)**  
  Authors: Changhun Oh, Seongryong Oh, Jinwoo Hwang, Yoonsung Kim, Hardik Sharma, Jongse Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12930v1.pdf)  
  Keywords: vr, 3d gaussian, tracking, ar, acceleration, gaussian splatting, efficient  
- **[Changes in Real Time: Online Scene Change Detection with Multi-View Fusion](https://arxiv.org/abs/2511.12370v1)**  
  Authors: Chamuditha Jayanga Galappaththige, Jason Lai, Lloyd Windrim, Donald Dansereau, Niko Sünderhauf, Dimity Miller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12370v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, ar  
- **[RealisticDreamer: Guidance Score Distillation for Few-shot Gaussian Splatting](https://arxiv.org/abs/2511.11213v1)**  
  Authors: Ruocheng Wu, Haolan He, Yufei Wang, Zhihao Li, Bihan Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.11213v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, motion, real-time rendering, few-shot, gaussian splatting, semantic  
- **[YoNoSplat: You Only Need One Model for Feedforward 3D Gaussian Splatting](https://arxiv.org/abs/2511.07321v1)**  
  Authors: Botao Ye, Boqi Chen, Haofei Xu, Daniel Barath, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07321v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://botaoye.github.io/yonosplat/.)  
  Keywords: 3d gaussian, fast, gaussian splatting, ar  
- **[GFix: Perceptually Enhanced Gaussian Splatting Video Compression](https://arxiv.org/abs/2511.06953v1)**  
  Authors: Siyue Teng, Ge Gao, Duolikun Danier, Yuxuan Jiang, Fan Zhang, Thomas Davis, Zoe Liu, David Bull  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06953v1.pdf)  
  Keywords: compression, quality enhancement, 3d gaussian, fast, ar, gaussian splatting, efficient  
- **[ConeGS: Error-Guided Densification Using Pixel Cones for Improved Reconstruction with Fewer Primitives](https://arxiv.org/abs/2511.06810v1)**  
  Authors: Bartłomiej Baranowski, Stefano Esposito, Patricia Gschoßmann, Anpei Chen, Andreas Geiger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06810v1.pdf)  
  Keywords: 3d gaussian, geometry, fast, ar, gaussian splatting, efficient  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: 3d gaussian, fast, large scene, ar, head, gaussian splatting  
- **[3D Gaussian Point Encoders](https://arxiv.org/abs/2511.04797v1)**  
  Authors: Jim James, Ben Wilson, Simon Lucey, James Hays  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04797v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, fast, ar, lightweight, recognition, nerf, gaussian splatting, efficient  

### Applications

*Showing the latest 50 out of 996 papers*

- **[SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2511.14633v1)**  
  Authors: Meiying Gu, Jiawei Zhang, Jiahe Li, Xiaohan Yu, Haonan Luo, Jin Zheng, Xiao Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14633v1.pdf)  
  Keywords: 3d gaussian, geometry, sparse-view, ar, face, nerf, gaussian splatting, efficient  
- **[Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction](https://arxiv.org/abs/2511.14540v1)**  
  Authors: Hao Tian, Chenyangguang Zhang, Rui Liu, Wen Shen, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14540v1.pdf)  
  Keywords: 3d gaussian, 4d, geometry, dynamic, deformation, lighting, motion, ar, gaussian splatting  
- **[2D Gaussians Spatial Transport for Point-supervised Density Regression](https://arxiv.org/abs/2511.14477v1)**  
  Authors: Miao Shang, Xiaopeng Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14477v1.pdf)  
  Keywords: gaussian splatting, ar  
- **[IBGS: Image-Based Gaussian Splatting](https://arxiv.org/abs/2511.14357v1)**  
  Authors: Hoang Chuong Nguyen, Wei Mao, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14357v1.pdf)  
  Keywords: 3d gaussian, fast, ar, head, face, gaussian splatting, efficient  
- **[Silhouette-to-Contour Registration: Aligning Intraoral Scan Models with Cephalometric Radiographs](https://arxiv.org/abs/2511.14343v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Ji Jiang, Tong Chen, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14343v1.pdf)  
  Keywords: geometry, high-fidelity, ar, face, gaussian splatting  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, illumination, sparse-view, high-fidelity, ar, compact, face, gaussian splatting  
- **[GEN3D: Generating Domain-Free 3D Scenes from a Single Image](https://arxiv.org/abs/2511.14291v1)**  
  Authors: Yuxin Zhang, Ziyu Lu, Hongbo Duan, Keyu Fan, Pengting Luo, Peiyu Zhuang, Mengyu Yang, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14291v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d reconstruction, ar  
- **[Gaussian Splatting-based Low-Rank Tensor Representation for Multi-Dimensional Image Recovery](https://arxiv.org/abs/2511.14270v1)**  
  Authors: Yiming Zeng, Xi-Le Zhao, Wei-Hao Wu, Teng-Yu Ji, Chao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14270v1.pdf)  
  Keywords: compact, gaussian splatting, ar  
- **[RoboTidy : A 3D Gaussian Splatting Household Tidying Benchmark for Embodied Navigation and Action](https://arxiv.org/abs/2511.14161v1)**  
  Authors: Xiaoquan Sun, Ruijian Zhang, Kang Pang, Bingchen Miao, Yuxiang Tan, Zhen Yang, Ming Li, Jiayu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14161v1.pdf)  
  Keywords: 3d gaussian, few-shot, gaussian splatting, ar  
- **[iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion](https://arxiv.org/abs/2511.14149v1)**  
  Authors: Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14149v1.pdf)  
  Keywords: slam, 3d gaussian, robotics, tracking, lighting, ar, head, nerf, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 340 papers*

- **[SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2511.14633v1)**  
  Authors: Meiying Gu, Jiawei Zhang, Jiahe Li, Xiaohan Yu, Haonan Luo, Jin Zheng, Xiao Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14633v1.pdf)  
  Keywords: 3d gaussian, geometry, sparse-view, ar, face, nerf, gaussian splatting, efficient  
- **[IBGS: Image-Based Gaussian Splatting](https://arxiv.org/abs/2511.14357v1)**  
  Authors: Hoang Chuong Nguyen, Wei Mao, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14357v1.pdf)  
  Keywords: 3d gaussian, fast, ar, head, face, gaussian splatting, efficient  
- **[Silhouette-to-Contour Registration: Aligning Intraoral Scan Models with Cephalometric Radiographs](https://arxiv.org/abs/2511.14343v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Ji Jiang, Tong Chen, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14343v1.pdf)  
  Keywords: geometry, high-fidelity, ar, face, gaussian splatting  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, illumination, sparse-view, high-fidelity, ar, compact, face, gaussian splatting  
- **[iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion](https://arxiv.org/abs/2511.14149v1)**  
  Authors: Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14149v1.pdf)  
  Keywords: slam, 3d gaussian, robotics, tracking, lighting, ar, head, nerf, gaussian splatting  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: semantic, relighting, geometry, outdoor, illumination, lighting, high-fidelity, segmentation, ar, face, gaussian splatting, efficient  
- **[SF-Recon: Simplification-Free Lightweight Building Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2511.13278v1)**  
  Authors: Zihan Li, Tengfei Wang, Wentian Gan, Hao Zhan, Xin Wang, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13278v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lzh282140127-cell.github.io/SF-Recon-project/)  
  Keywords: 3d gaussian, geometry, fast, ar, lightweight, face, gaussian splatting  
- **[Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis](https://arxiv.org/abs/2511.13011v1)**  
  Authors: Qingsen Ma, Chen Zou, Dianyun Wang, Jia Wang, Liuyu Xiang, Zhaofeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13011v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, dynamic, illumination, ar, face, gaussian splatting  
- **[LiDAR-GS++:Improving LiDAR Gaussian Reconstruction via Diffusion Priors](https://arxiv.org/abs/2511.12304v1)**  
  Authors: Qifeng Chen, Jiarun Liu, Rengan Xie, Tao Tang, Sicong Du, Yiru Zhao, Yuchi Huo, Sheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12304v1.pdf)  
  Keywords: geometry, high-fidelity, ar, face, nerf, gaussian splatting  
- **[3D Gaussian and Diffusion-Based Gaze Redirection](https://arxiv.org/abs/2511.11231v1)**  
  Authors: Abiram Panchalingam, Indu Bodala, Stuart Middleton  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.11231v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, head, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 396 papers*

- **[Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction](https://arxiv.org/abs/2511.14540v1)**  
  Authors: Hao Tian, Chenyangguang Zhang, Rui Liu, Wen Shen, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14540v1.pdf)  
  Keywords: 3d gaussian, 4d, geometry, dynamic, deformation, lighting, motion, ar, gaussian splatting  
- **[Opt3DGS: Optimizing 3D Gaussian Splatting with Adaptive Exploration and Curvature-Aware Exploitation](https://arxiv.org/abs/2511.13571v1)**  
  Authors: Ziyang Huang, Jiagang Chen, Jin Liu, Shunping Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13571v1.pdf)  
  Keywords: 3d gaussian, dynamic, ar, gaussian splatting, efficient  
- **[Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis](https://arxiv.org/abs/2511.13011v1)**  
  Authors: Qingsen Ma, Chen Zou, Dianyun Wang, Jia Wang, Liuyu Xiang, Zhaofeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13011v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, dynamic, illumination, ar, face, gaussian splatting  
- **[Reconstructing 3D Scenes in Native High Dynamic Range](https://arxiv.org/abs/2511.12895v1)**  
  Authors: Kaixuan Zhang, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12895v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, dynamic, ar, mapping, gaussian splatting  
- **[RealisticDreamer: Guidance Score Distillation for Few-shot Gaussian Splatting](https://arxiv.org/abs/2511.11213v1)**  
  Authors: Ruocheng Wu, Haolan He, Yufei Wang, Zhihao Li, Bihan Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.11213v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, motion, real-time rendering, few-shot, gaussian splatting, semantic  
- **[Dynamic Gaussian Scene Reconstruction from Unsynchronized Videos](https://arxiv.org/abs/2511.11175v1)**  
  Authors: Zhixin Xu, Hengyu Zhou, Yuan Liu, Wenhan Xue, Hao Pan, Wenping Wang, Bin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.11175v1.pdf)  
  Keywords: 4d, dynamic, motion, ar, gaussian splatting  
- **[PINGS-X: Physics-Informed Normalized Gaussian Splatting with Axes Alignment for Efficient Super-Resolution of 4D Flow MRI](https://arxiv.org/abs/2511.11048v1)**  
  Authors: Sun Jo, Seok Young Hong, JinHyun Kim, Seungmin Kang, Ahjin Choi, Don-Gwan An, Simon Song, Je Hyeong Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.11048v1.pdf)  
  Keywords: 3d gaussian, 4d, dynamic, ar, gaussian splatting, efficient  
- **[AHA! Animating Human Avatars in Diverse Scenes with Gaussian Splatting](https://arxiv.org/abs/2511.09827v1)**  
  Authors: Aymen Mir, Jian Wang, Riza Alp Guler, Chuan Guo, Gerard Pons-Moll, Bing Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09827v1.pdf)  
  Keywords: animation, 3d gaussian, ar, geometry, motion, human, gaussian splatting, avatar  
- **[A Shared-Autonomy Construction Robotic System for Overhead Works](https://arxiv.org/abs/2511.09695v1)**  
  Authors: David Minkwan Kim, K. M. Brian Lee, Yong Hyeok Seo, Nikola Raicevic, Runfa Blark Li, Kehan Long, Chan Seon Yoon, Dong Min Kang, Byeong Jo Lim, Young Pyoung Kim, Nikolay Atanasov, Truong Nguyen, Se Woong Jun, Young Wook Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09695v1.pdf)  
  Keywords: 3d reconstruction, dynamic, motion, ar, head, gaussian splatting  
- **[4DSTR: Advancing Generative 4D Gaussians with Spatial-Temporal Rectification for High-Quality and Consistent 4D Generation](https://arxiv.org/abs/2511.07241v1)**  
  Authors: Mengmeng Liu, Jiuming Liu, Yunpeng Zhang, Jiangtao Li, Michael Ying Yang, Francesco Nex, Hao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07241v1.pdf)  
  Keywords: 4d, gaussian splatting, dynamic, ar  

### Few-shot

*Showing the latest 50 out of 76 papers*

- **[SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2511.14633v1)**  
  Authors: Meiying Gu, Jiawei Zhang, Jiahe Li, Xiaohan Yu, Haonan Luo, Jin Zheng, Xiao Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14633v1.pdf)  
  Keywords: 3d gaussian, geometry, sparse-view, ar, face, nerf, gaussian splatting, efficient  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, illumination, sparse-view, high-fidelity, ar, compact, face, gaussian splatting  
- **[RoboTidy : A 3D Gaussian Splatting Household Tidying Benchmark for Embodied Navigation and Action](https://arxiv.org/abs/2511.14161v1)**  
  Authors: Xiaoquan Sun, Ruijian Zhang, Kang Pang, Bingchen Miao, Yuxiang Tan, Zhen Yang, Ming Li, Jiayu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14161v1.pdf)  
  Keywords: 3d gaussian, few-shot, gaussian splatting, ar  
- **[SplatSearch: Instance Image Goal Navigation for Mobile Robots using 3D Gaussian Splatting and Diffusion Models](https://arxiv.org/abs/2511.12972v1)**  
  Authors: Siddarth Narasimhan, Matthew Lisondra, Haitong Wang, Goldie Nejat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12972v1.pdf)  
  Keywords: 3d gaussian, sparse-view, ar, gaussian splatting, semantic  
- **[RealisticDreamer: Guidance Score Distillation for Few-shot Gaussian Splatting](https://arxiv.org/abs/2511.11213v1)**  
  Authors: Ruocheng Wu, Haolan He, Yufei Wang, Zhihao Li, Bihan Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.11213v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, motion, real-time rendering, few-shot, gaussian splatting, semantic  
- **[Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction](https://arxiv.org/abs/2511.07122v1)**  
  Authors: Changyue Shi, Chuxiao Yang, Xinyuan Hu, Minghao Chen, Wenwen Pan, Yan Yang, Jiajun Ding, Zhou Yu, Jun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07122v1.pdf)  
  Keywords: 4d, dynamic, deformation, ar, few-shot, nerf, gaussian splatting  
- **[FastGS: Training 3D Gaussian Splatting in 100 Seconds](https://arxiv.org/abs/2511.04283v1)**  
  Authors: Shiwei Ren, Tianci Wen, Yongchun Fang, Biao Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04283v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fastgs.github.io/)  
  Keywords: mapping, 3d gaussian, localization, fast, dynamic, sparse-view, ar, acceleration, head, face, nerf, gaussian splatting, efficient  
- **[DentalSplat: Dental Occlusion Novel View Synthesis from Sparse Intra-Oral Photographs](https://arxiv.org/abs/2511.03099v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Sihao Li, Ji Jiang, Youpeng Yang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.03099v1.pdf)  
  Keywords: sparse view, 3d reconstruction, 3d gaussian, ar, gaussian splatting  
- **[Initialize to Generalize: A Stronger Initialization Pipeline for Sparse-View 3DGS](https://arxiv.org/abs/2510.17479v1)**  
  Authors: Feng Zhou, Wenkai Guo, Pu Cao, Zhicheng Zhang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.17479v1.pdf)  
  Keywords: sparse view, 3d gaussian, sparse-view, motion, ar, nerf, gaussian splatting  
- **[Opacity-Gradient Driven Density Control for Compact and Efficient Few-Shot 3D Gaussian Splatting](https://arxiv.org/abs/2510.10257v1)**  
  Authors: Abdelrhman Elrawy, Emad A. Mohammed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10257v1.pdf)  
  Keywords: lightweight, 3d gaussian, gaussian splatting, ar, compact, nerf, few-shot, efficient  

### Geometry Reconstruction

*Showing the latest 50 out of 321 papers*

- **[SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2511.14633v1)**  
  Authors: Meiying Gu, Jiawei Zhang, Jiahe Li, Xiaohan Yu, Haonan Luo, Jin Zheng, Xiao Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14633v1.pdf)  
  Keywords: 3d gaussian, geometry, sparse-view, ar, face, nerf, gaussian splatting, efficient  
- **[Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction](https://arxiv.org/abs/2511.14540v1)**  
  Authors: Hao Tian, Chenyangguang Zhang, Rui Liu, Wen Shen, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14540v1.pdf)  
  Keywords: 3d gaussian, 4d, geometry, dynamic, deformation, lighting, motion, ar, gaussian splatting  
- **[Silhouette-to-Contour Registration: Aligning Intraoral Scan Models with Cephalometric Radiographs](https://arxiv.org/abs/2511.14343v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Ji Jiang, Tong Chen, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14343v1.pdf)  
  Keywords: geometry, high-fidelity, ar, face, gaussian splatting  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, illumination, sparse-view, high-fidelity, ar, compact, face, gaussian splatting  
- **[GEN3D: Generating Domain-Free 3D Scenes from a Single Image](https://arxiv.org/abs/2511.14291v1)**  
  Authors: Yuxin Zhang, Ziyu Lu, Hongbo Duan, Keyu Fan, Pengting Luo, Peiyu Zhuang, Mengyu Yang, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14291v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d reconstruction, ar  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: semantic, relighting, geometry, outdoor, illumination, lighting, high-fidelity, segmentation, ar, face, gaussian splatting, efficient  
- **[SF-Recon: Simplification-Free Lightweight Building Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2511.13278v1)**  
  Authors: Zihan Li, Tengfei Wang, Wentian Gan, Hao Zhan, Xin Wang, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13278v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lzh282140127-cell.github.io/SF-Recon-project/)  
  Keywords: 3d gaussian, geometry, fast, ar, lightweight, face, gaussian splatting  
- **[Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis](https://arxiv.org/abs/2511.13011v1)**  
  Authors: Qingsen Ma, Chen Zou, Dianyun Wang, Jia Wang, Liuyu Xiang, Zhaofeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13011v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, dynamic, illumination, ar, face, gaussian splatting  
- **[Reconstructing 3D Scenes in Native High Dynamic Range](https://arxiv.org/abs/2511.12895v1)**  
  Authors: Kaixuan Zhang, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12895v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, dynamic, ar, mapping, gaussian splatting  
- **[LiDAR-GS++:Improving LiDAR Gaussian Reconstruction via Diffusion Priors](https://arxiv.org/abs/2511.12304v1)**  
  Authors: Qifeng Chen, Jiarun Liu, Rengan Xie, Tao Tang, Sicong Du, Yiru Zhao, Yuchi Huo, Sheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12304v1.pdf)  
  Keywords: geometry, high-fidelity, ar, face, nerf, gaussian splatting  

### Large Scene

*Showing the latest 50 out of 76 papers*

- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: semantic, relighting, geometry, outdoor, illumination, lighting, high-fidelity, segmentation, ar, face, gaussian splatting, efficient  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: 3d gaussian, geometry, outdoor, high-fidelity, ar, gaussian splatting  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: ar, 4d, dynamic, autonomous driving, urban scene, human, gaussian splatting  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: 3d gaussian, fast, large scene, ar, head, gaussian splatting  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: slam, 3d gaussian, geometry, outdoor, understanding, motion, ar, mapping, gaussian splatting  
- **[D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction](https://arxiv.org/abs/2510.25173v2)**  
  Authors: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25173v2.pdf)  
  Keywords: geometry, autonomous driving, urban scene, ar, gaussian splatting  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: 3d reconstruction, urban scene, ar, face, gaussian splatting, semantic  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/2510.22669v1)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22669v1.pdf)  
  Keywords: slam, 3d gaussian, outdoor, dynamic, high-fidelity, segmentation, human, ar, mapping, gaussian splatting  
- **[Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering](https://arxiv.org/abs/2510.13381v1)**  
  Authors: Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13381v1.pdf)  
  Keywords: 3d gaussian, ar, tracking, dynamic, deformation, segmentation, motion, urban scene, gaussian splatting  
- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: 3d reconstruction, dynamic, autonomous driving, urban scene, ar, face, gaussian splatting, semantic  

### Model Compression

*Showing the latest 50 out of 403 papers*

- **[SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2511.14633v1)**  
  Authors: Meiying Gu, Jiawei Zhang, Jiahe Li, Xiaohan Yu, Haonan Luo, Jin Zheng, Xiao Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14633v1.pdf)  
  Keywords: 3d gaussian, geometry, sparse-view, ar, face, nerf, gaussian splatting, efficient  
- **[IBGS: Image-Based Gaussian Splatting](https://arxiv.org/abs/2511.14357v1)**  
  Authors: Hoang Chuong Nguyen, Wei Mao, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14357v1.pdf)  
  Keywords: 3d gaussian, fast, ar, head, face, gaussian splatting, efficient  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, illumination, sparse-view, high-fidelity, ar, compact, face, gaussian splatting  
- **[Gaussian Splatting-based Low-Rank Tensor Representation for Multi-Dimensional Image Recovery](https://arxiv.org/abs/2511.14270v1)**  
  Authors: Yiming Zeng, Xi-Le Zhao, Wei-Hao Wu, Teng-Yu Ji, Chao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14270v1.pdf)  
  Keywords: compact, gaussian splatting, ar  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: semantic, relighting, geometry, outdoor, illumination, lighting, high-fidelity, segmentation, ar, face, gaussian splatting, efficient  
- **[Opt3DGS: Optimizing 3D Gaussian Splatting with Adaptive Exploration and Curvature-Aware Exploitation](https://arxiv.org/abs/2511.13571v1)**  
  Authors: Ziyang Huang, Jiagang Chen, Jin Liu, Shunping Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13571v1.pdf)  
  Keywords: 3d gaussian, dynamic, ar, gaussian splatting, efficient  
- **[SF-Recon: Simplification-Free Lightweight Building Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2511.13278v1)**  
  Authors: Zihan Li, Tengfei Wang, Wentian Gan, Hao Zhan, Xin Wang, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13278v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lzh282140127-cell.github.io/SF-Recon-project/)  
  Keywords: 3d gaussian, geometry, fast, ar, lightweight, face, gaussian splatting  
- **[SymGS : Leveraging Local Symmetries for 3D Gaussian Splatting Compression](https://arxiv.org/abs/2511.13264v1)**  
  Authors: Keshav Gupta, Akshat Sanghvi, Shreyas Reddy Palley, Astitva Srivastava, Charu Sharma, Avinash Sharma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13264v1.pdf)  
  Keywords: 3d gaussian, compression, gaussian splatting, ar  
- **[Neo: Real-Time On-Device 3D Gaussian Splatting with Reuse-and-Update Sorting Acceleration](https://arxiv.org/abs/2511.12930v1)**  
  Authors: Changhun Oh, Seongryong Oh, Jinwoo Hwang, Yoonsung Kim, Hardik Sharma, Jongse Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12930v1.pdf)  
  Keywords: vr, 3d gaussian, tracking, ar, acceleration, gaussian splatting, efficient  
- **[PINGS-X: Physics-Informed Normalized Gaussian Splatting with Axes Alignment for Efficient Super-Resolution of 4D Flow MRI](https://arxiv.org/abs/2511.11048v1)**  
  Authors: Sun Jo, Seok Young Hong, JinHyun Kim, Seungmin Kang, Ahjin Choi, Don-Gwan An, Simon Song, Je Hyeong Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.11048v1.pdf)  
  Keywords: 3d gaussian, 4d, dynamic, ar, gaussian splatting, efficient  

### Quality Enhancement

*Showing the latest 50 out of 184 papers*

- **[Silhouette-to-Contour Registration: Aligning Intraoral Scan Models with Cephalometric Radiographs](https://arxiv.org/abs/2511.14343v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Ji Jiang, Tong Chen, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14343v1.pdf)  
  Keywords: geometry, high-fidelity, ar, face, gaussian splatting  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, illumination, sparse-view, high-fidelity, ar, compact, face, gaussian splatting  
- **[GEN3D: Generating Domain-Free 3D Scenes from a Single Image](https://arxiv.org/abs/2511.14291v1)**  
  Authors: Yuxin Zhang, Ziyu Lu, Hongbo Duan, Keyu Fan, Pengting Luo, Peiyu Zhuang, Mengyu Yang, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14291v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d reconstruction, ar  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: semantic, relighting, geometry, outdoor, illumination, lighting, high-fidelity, segmentation, ar, face, gaussian splatting, efficient  
- **[LiDAR-GS++:Improving LiDAR Gaussian Reconstruction via Diffusion Priors](https://arxiv.org/abs/2511.12304v1)**  
  Authors: Qifeng Chen, Jiarun Liu, Rengan Xie, Tao Tang, Sicong Du, Yiru Zhao, Yuchi Huo, Sheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12304v1.pdf)  
  Keywords: geometry, high-fidelity, ar, face, nerf, gaussian splatting  
- **[3D Gaussian and Diffusion-Based Gaze Redirection](https://arxiv.org/abs/2511.11231v1)**  
  Authors: Abiram Panchalingam, Indu Bodala, Stuart Middleton  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.11231v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, head, gaussian splatting  
- **[OUGS: Active View Selection via Object-aware Uncertainty Estimation in 3DGS](https://arxiv.org/abs/2511.09397v1)**  
  Authors: Haiyi Li, Qi Chen, Denis Kalkofen, Hsiang-Ting Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09397v1.pdf)  
  Keywords: efficient, 3d gaussian, high-fidelity, segmentation, ar, gaussian splatting, semantic  
- **[Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric](https://arxiv.org/abs/2511.08032v1)**  
  Authors: Zhaolin Wan, Yining Diao, Jingqi Xu, Hao Wang, Zhiyang Li, Xiaopeng Fan, Wangmeng Zuo, Debin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.08032v1.pdf)  
  Keywords: 3d gaussian, lighting, high-fidelity, ar, gaussian splatting  
- **[GFix: Perceptually Enhanced Gaussian Splatting Video Compression](https://arxiv.org/abs/2511.06953v1)**  
  Authors: Siyue Teng, Ge Gao, Duolikun Danier, Yuxuan Jiang, Fan Zhang, Thomas Davis, Zoe Liu, David Bull  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06953v1.pdf)  
  Keywords: compression, quality enhancement, 3d gaussian, fast, ar, gaussian splatting, efficient  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: 3d gaussian, geometry, outdoor, high-fidelity, ar, gaussian splatting  

### Ray Tracing

- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: ray tracing, geometry, reflection, illumination, ar, gaussian splatting  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: 3d gaussian, geometry, ray marching, ar, gaussian splatting, efficient  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: ar, ray tracing, shadow, lighting, light transport, real-time rendering, relightable, face, gaussian splatting, efficient  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: efficient, relighting, geometry, reflection, illumination, lighting, light transport, ar, gaussian splatting, global illumination  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v2)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v2.pdf)  
  Keywords: ray tracing, 4d, fast, dynamic, ar, gaussian splatting  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: relighting, 3d gaussian, ray tracing, geometry, reflection, illumination, high-fidelity, lighting, ar, face, nerf, gaussian splatting  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: relighting, 3d gaussian, outdoor, dynamic, shadow, illumination, lighting, ar, relightable, face, gaussian splatting, global illumination  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: path tracing, 3d gaussian, dynamic, lighting, ar, face, gaussian splatting  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relighting, 3d gaussian, geometry, efficient rendering, lighting, ray marching, ar, relightable, face, gaussian splatting, efficient  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: ar, ray tracing, high-fidelity, real-time rendering, gaussian splatting, efficient  

### Relighting

*Showing the latest 50 out of 123 papers*

- **[Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction](https://arxiv.org/abs/2511.14540v1)**  
  Authors: Hao Tian, Chenyangguang Zhang, Rui Liu, Wen Shen, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14540v1.pdf)  
  Keywords: 3d gaussian, 4d, geometry, dynamic, deformation, lighting, motion, ar, gaussian splatting  
- **[Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs](https://arxiv.org/abs/2511.14315v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Ji Jiang, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14315v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, illumination, sparse-view, high-fidelity, ar, compact, face, gaussian splatting  
- **[iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion](https://arxiv.org/abs/2511.14149v1)**  
  Authors: Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14149v1.pdf)  
  Keywords: slam, 3d gaussian, robotics, tracking, lighting, ar, head, nerf, gaussian splatting  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: semantic, relighting, geometry, outdoor, illumination, lighting, high-fidelity, segmentation, ar, face, gaussian splatting, efficient  
- **[Beyond Darkness: Thermal-Supervised 3D Gaussian Splatting for Low-Light Novel View Synthesis](https://arxiv.org/abs/2511.13011v1)**  
  Authors: Qingsen Ma, Chen Zou, Dianyun Wang, Jia Wang, Liuyu Xiang, Zhaofeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13011v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, dynamic, illumination, ar, face, gaussian splatting  
- **[Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric](https://arxiv.org/abs/2511.08032v1)**  
  Authors: Zhaolin Wan, Yining Diao, Jingqi Xu, Hao Wang, Zhiyang Li, Xiaopeng Fan, Wangmeng Zuo, Debin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.08032v1.pdf)  
  Keywords: 3d gaussian, lighting, high-fidelity, ar, gaussian splatting  
- **[UltraGS: Gaussian Splatting for Ultrasound Novel View Synthesis](https://arxiv.org/abs/2511.07743v1)**  
  Authors: Yuezhe Yang, Wenjie Cai, Dexin Yang, Yufang Dong, Xingbo Dong, Zhe Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07743v1.pdf)  
  Keywords: lightweight, reflection, gaussian splatting, ar  
- **[Channel Knowledge Map Construction: Recent Advances and Open Challenges](https://arxiv.org/abs/2511.04944v1)**  
  Authors: Zixiang Ren, Juncong Zhou, Jie Xu, Ling Qiu, Yong Zeng, Han Hu, Juyong Zhang, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04944v1.pdf)  
  Keywords: lighting, high-fidelity, ar, gaussian splatting, efficient  
- **[RoGER-SLAM: A Robust Gaussian Splatting SLAM System for Noisy and Low-light Environment Resilience](https://arxiv.org/abs/2510.22600v1)**  
  Authors: Huilin Yin, Zhaolin Yang, Linchuan Zhang, Gerhard Rigoll, Johannes Betz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22600v1.pdf)  
  Keywords: slam, 3d gaussian, localization, tracking, illumination, high-fidelity, ar, mapping, gaussian splatting, semantic  
- **[Dino-Diffusion Modular Designs Bridge the Cross-Domain Gap in Autonomous Parking](https://arxiv.org/abs/2510.20335v1)**  
  Authors: Zixuan Wu, Hengyuan Zhang, Ting-Hsuan Chen, Yuliang Guo, David Paz, Xinyu Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.20335v1.pdf)  
  Keywords: 3d gaussian, lighting, motion, ar, gaussian splatting  

### SLAM

*Showing the latest 50 out of 139 papers*

- **[iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion](https://arxiv.org/abs/2511.14149v1)**  
  Authors: Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.14149v1.pdf)  
  Keywords: slam, 3d gaussian, robotics, tracking, lighting, ar, head, nerf, gaussian splatting  
- **[GUIDE: Gaussian Unified Instance Detection for Enhanced Obstacle Perception in Autonomous Driving](https://arxiv.org/abs/2511.12941v1)**  
  Authors: Chunyong Hu, Qi Luo, Jianyun Xu, Song Wang, Qiang Li, Sheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12941v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, tracking, ar  
- **[Neo: Real-Time On-Device 3D Gaussian Splatting with Reuse-and-Update Sorting Acceleration](https://arxiv.org/abs/2511.12930v1)**  
  Authors: Changhun Oh, Seongryong Oh, Jinwoo Hwang, Yoonsung Kim, Hardik Sharma, Jongse Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12930v1.pdf)  
  Keywords: vr, 3d gaussian, tracking, ar, acceleration, gaussian splatting, efficient  
- **[Reconstructing 3D Scenes in Native High Dynamic Range](https://arxiv.org/abs/2511.12895v1)**  
  Authors: Kaixuan Zhang, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12895v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, dynamic, ar, mapping, gaussian splatting  
- **[FastGS: Training 3D Gaussian Splatting in 100 Seconds](https://arxiv.org/abs/2511.04283v1)**  
  Authors: Shiwei Ren, Tianci Wen, Yongchun Fang, Biao Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04283v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fastgs.github.io/)  
  Keywords: mapping, 3d gaussian, localization, fast, dynamic, sparse-view, ar, acceleration, head, face, nerf, gaussian splatting, efficient  
- **[WildfireX-SLAM: A Large-scale Low-altitude RGB-D Dataset for Wildfire SLAM and Beyond](https://arxiv.org/abs/2510.27133v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.27133v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhicongsun.github.io/wildfirexslam.)  
  Keywords: slam, 3d gaussian, localization, ar, mapping, gaussian splatting  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: slam, 3d gaussian, geometry, outdoor, understanding, motion, ar, mapping, gaussian splatting  
- **[LagMemo: Language 3D Gaussian Splatting Memory for Multi-modal Open-vocabulary Multi-goal Visual Navigation](https://arxiv.org/abs/2510.24118v1)**  
  Authors: Haotian Zhou, Xiaole Wang, He Li, Fusheng Sun, Shengyu Guo, Guolei Qi, Jianghuan Xu, Huijing Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.24118v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weekgoodday.github.io/lagmemo)  
  Keywords: 3d gaussian, localization, dynamic, ar, gaussian splatting  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: semantic, slam, 3d gaussian, localization, robotics, survey, high-fidelity, ar, mapping, gaussian splatting, efficient  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/2510.22669v1)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22669v1.pdf)  
  Keywords: slam, 3d gaussian, outdoor, dynamic, high-fidelity, segmentation, human, ar, mapping, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 198 papers*

- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: semantic, relighting, geometry, outdoor, illumination, lighting, high-fidelity, segmentation, ar, face, gaussian splatting, efficient  
- **[SplatSearch: Instance Image Goal Navigation for Mobile Robots using 3D Gaussian Splatting and Diffusion Models](https://arxiv.org/abs/2511.12972v1)**  
  Authors: Siddarth Narasimhan, Matthew Lisondra, Haitong Wang, Goldie Nejat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.12972v1.pdf)  
  Keywords: 3d gaussian, sparse-view, ar, gaussian splatting, semantic  
- **[RealisticDreamer: Guidance Score Distillation for Few-shot Gaussian Splatting](https://arxiv.org/abs/2511.11213v1)**  
  Authors: Ruocheng Wu, Haolan He, Yufei Wang, Zhihao Li, Bihan Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.11213v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, motion, real-time rendering, few-shot, gaussian splatting, semantic  
- **[OUGS: Active View Selection via Object-aware Uncertainty Estimation in 3DGS](https://arxiv.org/abs/2511.09397v1)**  
  Authors: Haiyi Li, Qi Chen, Denis Kalkofen, Hsiang-Ting Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09397v1.pdf)  
  Keywords: efficient, 3d gaussian, high-fidelity, segmentation, ar, gaussian splatting, semantic  
- **[Inpaint360GS: Efficient Object-Aware 3D Inpainting via Gaussian Splatting for 360° Scenes](https://arxiv.org/abs/2511.06457v1)**  
  Authors: Shaoxiang Wang, Shihong Zhang, Christen Millerdurai, Rüdiger Westermann, Didier Stricker, Alain Pagani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06457v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dfki-av.github.io/inpaint360gs/)  
  Keywords: 3d gaussian, high-fidelity, segmentation, ar, nerf, gaussian splatting, efficient  
- **[4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes from Monocular Videos](https://arxiv.org/abs/2511.05229v1)**  
  Authors: Mengqi Guo, Bo Xu, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.05229v1.pdf)  
  Keywords: 3d gaussian, ar, 4d, geometry, dynamic, deformation, segmentation, motion, neural rendering, nerf, gaussian splatting, efficient  
- **[3D Gaussian Point Encoders](https://arxiv.org/abs/2511.04797v1)**  
  Authors: Jim James, Ben Wilson, Simon Lucey, James Hays  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04797v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, fast, ar, lightweight, recognition, nerf, gaussian splatting, efficient  
- **[CaRF: Enhancing Multi-View Consistency in Referring 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/2511.03992v1)**  
  Authors: Yuwen Tao, Kanglei Zhou, Xin Tan, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.03992v1.pdf)  
  Keywords: vr, 3d gaussian, geometry, segmentation, understanding, ar, gaussian splatting  
- **[PercHead: Perceptual Head Model for Single-Image 3D Head Reconstruction & Editing](https://arxiv.org/abs/2511.02777v1)**  
  Authors: Antonio Oroz, Matthias Nießner, Tobias Kirschstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.02777v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://antoniooroz.github.io/PercHead)  
  Keywords: geometry, segmentation, ar, lightweight, head, gaussian splatting, semantic  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: slam, 3d gaussian, geometry, outdoor, understanding, motion, ar, mapping, gaussian splatting  



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