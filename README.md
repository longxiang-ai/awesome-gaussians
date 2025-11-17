# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-11-17 00:55:24

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
- [Dynamic Scene](#dynamic-scene) (398 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (74 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (325 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (75 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (404 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (182 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (15 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (119 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (139 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (199 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: semantic, survey, high-fidelity, robotics, ar, gaussian splatting, 3d gaussian, mapping, slam, efficient, localization  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: survey, geometry, ar, gaussian splatting, 3d gaussian, fast, motion, 4d, nerf  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: survey, efficient rendering, face, gaussian splatting, lighting, ar, 3d gaussian, real-time rendering, avatar, efficient, 3d reconstruction, animation  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: lightweight, survey, efficient, ar, gaussian splatting, nerf, understanding, human  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: survey, efficient, ar, gaussian splatting, 3d gaussian, fast, slam, neural rendering, nerf, understanding  
- **[A-TDOM: Active TDOM via On-the-Fly 3DGS](https://arxiv.org/abs/2509.12759v2)**  
  Authors: Yiwei Xu, Xiang Wang, Yifei Yu, Wentian Gan, Luca Morelli, Giulio Perda, Xiongwu Xiao, Zongqian Zhan, Xin Wang, Fabio Remondino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.12759v2.pdf)  
  Keywords: ar, face, survey  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: semantic, compact, survey, high-fidelity, segmentation, gaussian splatting, lighting, ar, 3d gaussian, nerf, understanding  
- **[A Study of the Framework and Real-World Applications of Language Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: semantic, survey, efficient, robotics, ar, gaussian splatting, 3d gaussian, nerf, understanding  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: survey, robotics, ar, gaussian splatting, 3d gaussian, nerf, human  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: survey, geometry, robotics, sparse-view, gaussian splatting, ar, vr, 3d gaussian, motion, nerf, 3d reconstruction  

### Acceleration

*Showing the latest 50 out of 260 papers*

- **[YoNoSplat: You Only Need One Model for Feedforward 3D Gaussian Splatting](https://arxiv.org/abs/2511.07321v1)**  
  Authors: Botao Ye, Boqi Chen, Haofei Xu, Daniel Barath, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07321v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://botaoye.github.io/yonosplat/.)  
  Keywords: ar, gaussian splatting, 3d gaussian, fast  
- **[GFix: Perceptually Enhanced Gaussian Splatting Video Compression](https://arxiv.org/abs/2511.06953v1)**  
  Authors: Siyue Teng, Ge Gao, Duolikun Danier, Yuxuan Jiang, Fan Zhang, Thomas Davis, Zoe Liu, David Bull  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06953v1.pdf)  
  Keywords: compression, ar, gaussian splatting, quality enhancement, 3d gaussian, fast, efficient  
- **[ConeGS: Error-Guided Densification Using Pixel Cones for Improved Reconstruction with Fewer Primitives](https://arxiv.org/abs/2511.06810v1)**  
  Authors: Bartłomiej Baranowski, Stefano Esposito, Patricia Gschoßmann, Anpei Chen, Andreas Geiger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06810v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, 3d gaussian, fast, efficient  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: head, ar, gaussian splatting, large scene, 3d gaussian, fast  
- **[3D Gaussian Point Encoders](https://arxiv.org/abs/2511.04797v1)**  
  Authors: Jim James, Ben Wilson, Simon Lucey, James Hays  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04797v1.pdf)  
  Keywords: lightweight, recognition, efficient, geometry, ar, gaussian splatting, 3d gaussian, fast, nerf, 3d reconstruction  
- **[FastGS: Training 3D Gaussian Splatting in 100 Seconds](https://arxiv.org/abs/2511.04283v1)**  
  Authors: Shiwei Ren, Tianci Wen, Yongchun Fang, Biao Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04283v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fastgs.github.io/)  
  Keywords: head, efficient, sparse-view, gaussian splatting, face, ar, 3d gaussian, fast, dynamic, mapping, localization, nerf, acceleration  
- **[4D Neural Voxel Splatting: Dynamic Scene Rendering with Voxelized Guassian Splatting](https://arxiv.org/abs/2511.00560v1)**  
  Authors: Chun-Tin Wu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.00560v1.pdf)  
  Keywords: head, efficient rendering, efficient, ar, gaussian splatting, 3d gaussian, fast, real-time rendering, dynamic, 4d, deformation, compact  
- **[SAGS: Self-Adaptive Alias-Free Gaussian Splatting for Dynamic Surgical Endoscopic Reconstruction](https://arxiv.org/abs/2510.27318v1)**  
  Authors: Wenfeng Huang, Xiangyun Liao, Yinling Qian, Hao Liu, Yongming Yang, Wenjing Jia, Qiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.27318v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, fast, dynamic, deformation, 4d, nerf  
- **[Explicit Memory through Online 3D Gaussian Splatting Improves Class-Agnostic Video Segmentation](https://arxiv.org/abs/2510.23521v1)**  
  Authors: Anthony Opipari, Aravindhan K Krishnan, Shreekant Gayaka, Min Sun, Cheng-Hao Kuo, Arnie Sen, Odest Chadwicke Jenkins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23521v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://topipari.com/projects/FastSAM-Splat/)  
  Keywords: ar, segmentation, gaussian splatting, 3d gaussian, fast  
- **[DynamicTree: Interactive Real Tree Animation via Sparse Voxel Spectrum](https://arxiv.org/abs/2510.22213v1)**  
  Authors: Yaokun Li, Lihe Ding, Xiao Chen, Guang Tan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22213v1.pdf)  
  Keywords: semantic, face, gaussian splatting, ar, 3d gaussian, fast, dynamic, motion, 4d, compact, animation  

### Applications

*Showing the latest 50 out of 996 papers*

- **[Depth-Consistent 3D Gaussian Splatting via Physical Defocus Modeling and Multi-View Geometric Supervision](https://arxiv.org/abs/2511.10316v1)**  
  Authors: Yu Deng, Baozhu Zhao, Junyan Su, Xiaohan Zhang, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.10316v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian  
- **[TSPE-GS: Probabilistic Depth Extraction for Semi-Transparent Surface Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2511.09944v1)**  
  Authors: Zhiyuan Xu, Nan Min, Yuhang Guo, Tong Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09944v1.pdf)  
  Keywords: head, geometry, face, gaussian splatting, ar, 3d gaussian  
- **[AHA! Animating Human Avatars in Diverse Scenes with Gaussian Splatting](https://arxiv.org/abs/2511.09827v1)**  
  Authors: Aymen Mir, Jian Wang, Riza Alp Guler, Chuan Guo, Gerard Pons-Moll, Bing Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09827v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, motion, 3d gaussian, human, avatar, animation  
- **[A Shared-Autonomy Construction Robotic System for Overhead Works](https://arxiv.org/abs/2511.09695v1)**  
  Authors: David Minkwan Kim, K. M. Brian Lee, Yong Hyeok Seo, Nikola Raicevic, Runfa Blark Li, Kehan Long, Chan Seon Yoon, Dong Min Kang, Byeong Jo Lim, Young Pyoung Kim, Nikolay Atanasov, Truong Nguyen, Se Woong Jun, Young Wook Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09695v1.pdf)  
  Keywords: head, ar, gaussian splatting, motion, dynamic, 3d reconstruction  
- **[OUGS: Active View Selection via Object-aware Uncertainty Estimation in 3DGS](https://arxiv.org/abs/2511.09397v1)**  
  Authors: Haiyi Li, Qi Chen, Denis Kalkofen, Hsiang-Ting Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09397v1.pdf)  
  Keywords: semantic, high-fidelity, segmentation, gaussian splatting, ar, 3d gaussian, efficient  
- **[SkelSplat: Robust Multi-view 3D Human Pose Estimation with Differentiable Gaussian Rendering](https://arxiv.org/abs/2511.08294v1)**  
  Authors: Laura Bragagnolo, Leonardo Barcellona, Stefano Ghidoni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.08294v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://skelsplat.github.io.)  
  Keywords: ar, gaussian splatting, human, 3d gaussian  
- **[Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric](https://arxiv.org/abs/2511.08032v1)**  
  Authors: Zhaolin Wan, Yining Diao, Jingqi Xu, Hao Wang, Zhiyang Li, Xiaopeng Fan, Wangmeng Zuo, Debin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.08032v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, lighting, 3d gaussian  
- **[UltraGS: Gaussian Splatting for Ultrasound Novel View Synthesis](https://arxiv.org/abs/2511.07743v1)**  
  Authors: Yuezhe Yang, Wenjie Cai, Dexin Yang, Yufang Dong, Xingbo Dong, Zhe Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07743v1.pdf)  
  Keywords: reflection, lightweight, gaussian splatting, ar  
- **[YoNoSplat: You Only Need One Model for Feedforward 3D Gaussian Splatting](https://arxiv.org/abs/2511.07321v1)**  
  Authors: Botao Ye, Boqi Chen, Haofei Xu, Daniel Barath, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07321v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://botaoye.github.io/yonosplat/.)  
  Keywords: ar, gaussian splatting, 3d gaussian, fast  
- **[4DSTR: Advancing Generative 4D Gaussians with Spatial-Temporal Rectification for High-Quality and Consistent 4D Generation](https://arxiv.org/abs/2511.07241v1)**  
  Authors: Mengmeng Liu, Jiuming Liu, Yunpeng Zhang, Jiangtao Li, Michael Ying Yang, Francesco Nex, Hao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07241v1.pdf)  
  Keywords: ar, 4d, gaussian splatting, dynamic  

### Avatar Generation

*Showing the latest 50 out of 340 papers*

- **[TSPE-GS: Probabilistic Depth Extraction for Semi-Transparent Surface Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2511.09944v1)**  
  Authors: Zhiyuan Xu, Nan Min, Yuhang Guo, Tong Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09944v1.pdf)  
  Keywords: head, geometry, face, gaussian splatting, ar, 3d gaussian  
- **[AHA! Animating Human Avatars in Diverse Scenes with Gaussian Splatting](https://arxiv.org/abs/2511.09827v1)**  
  Authors: Aymen Mir, Jian Wang, Riza Alp Guler, Chuan Guo, Gerard Pons-Moll, Bing Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09827v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, motion, 3d gaussian, human, avatar, animation  
- **[A Shared-Autonomy Construction Robotic System for Overhead Works](https://arxiv.org/abs/2511.09695v1)**  
  Authors: David Minkwan Kim, K. M. Brian Lee, Yong Hyeok Seo, Nikola Raicevic, Runfa Blark Li, Kehan Long, Chan Seon Yoon, Dong Min Kang, Byeong Jo Lim, Young Pyoung Kim, Nikolay Atanasov, Truong Nguyen, Se Woong Jun, Young Wook Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09695v1.pdf)  
  Keywords: head, ar, gaussian splatting, motion, dynamic, 3d reconstruction  
- **[SkelSplat: Robust Multi-view 3D Human Pose Estimation with Differentiable Gaussian Rendering](https://arxiv.org/abs/2511.08294v1)**  
  Authors: Laura Bragagnolo, Leonardo Barcellona, Stefano Ghidoni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.08294v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://skelsplat.github.io.)  
  Keywords: ar, gaussian splatting, human, 3d gaussian  
- **[MUGSQA: Novel Multi-Uncertainty-Based Gaussian Splatting Quality Assessment Method, Dataset, and Benchmarks](https://arxiv.org/abs/2511.06830v1)**  
  Authors: Tianang Chen, Jian Jin, Shilv Cai, Zhuangzi Li, Weisi Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06830v1.pdf)  
  Keywords: ar, gaussian splatting, human  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: autonomous driving, ar, gaussian splatting, dynamic, 4d, human, urban scene  
- **[StreamSTGS: Streaming Spatial and Temporal Gaussian Grids for Real-Time Free-Viewpoint Video](https://arxiv.org/abs/2511.06046v1)**  
  Authors: Zhihui Ke, Yuyang Liu, Xiaobo Zhou, Tie Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06046v1.pdf)  
  Keywords: compression, face, gaussian splatting, ar, motion, 3d gaussian, deformation, dynamic  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: head, ar, gaussian splatting, large scene, 3d gaussian, fast  
- **[Real-to-Sim Robot Policy Evaluation with Gaussian Splatting Simulation of Soft-Body Interactions](https://arxiv.org/abs/2511.04665v2)**  
  Authors: Kaifeng Zhang, Shuo Sha, Hanxiao Jiang, Matthew Loper, Hyunjong Song, Guangyan Cai, Zhuo Xu, Xiaochen Hu, Changxi Zheng, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04665v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2sim-eval.github.io/)  
  Keywords: body, ar, gaussian splatting, 3d gaussian  
- **[FastGS: Training 3D Gaussian Splatting in 100 Seconds](https://arxiv.org/abs/2511.04283v1)**  
  Authors: Shiwei Ren, Tianci Wen, Yongchun Fang, Biao Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04283v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fastgs.github.io/)  
  Keywords: head, efficient, sparse-view, gaussian splatting, face, ar, 3d gaussian, fast, dynamic, mapping, localization, nerf, acceleration  

### Dynamic Scene

*Showing the latest 50 out of 398 papers*

- **[AHA! Animating Human Avatars in Diverse Scenes with Gaussian Splatting](https://arxiv.org/abs/2511.09827v1)**  
  Authors: Aymen Mir, Jian Wang, Riza Alp Guler, Chuan Guo, Gerard Pons-Moll, Bing Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09827v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, motion, 3d gaussian, human, avatar, animation  
- **[A Shared-Autonomy Construction Robotic System for Overhead Works](https://arxiv.org/abs/2511.09695v1)**  
  Authors: David Minkwan Kim, K. M. Brian Lee, Yong Hyeok Seo, Nikola Raicevic, Runfa Blark Li, Kehan Long, Chan Seon Yoon, Dong Min Kang, Byeong Jo Lim, Young Pyoung Kim, Nikolay Atanasov, Truong Nguyen, Se Woong Jun, Young Wook Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09695v1.pdf)  
  Keywords: head, ar, gaussian splatting, motion, dynamic, 3d reconstruction  
- **[4DSTR: Advancing Generative 4D Gaussians with Spatial-Temporal Rectification for High-Quality and Consistent 4D Generation](https://arxiv.org/abs/2511.07241v1)**  
  Authors: Mengmeng Liu, Jiuming Liu, Yunpeng Zhang, Jiangtao Li, Michael Ying Yang, Francesco Nex, Hao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07241v1.pdf)  
  Keywords: ar, 4d, gaussian splatting, dynamic  
- **[Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction](https://arxiv.org/abs/2511.07122v1)**  
  Authors: Changyue Shi, Chuxiao Yang, Xinyuan Hu, Minghao Chen, Wenwen Pan, Yan Yang, Jiajun Ding, Zhou Yu, Jun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07122v1.pdf)  
  Keywords: ar, gaussian splatting, deformation, dynamic, 4d, few-shot, nerf  
- **[Rethinking Rainy 3D Scene Reconstruction via Perspective Transforming and Brightness Tuning](https://arxiv.org/abs/2511.06734v1)**  
  Authors: Qianfeng Yang, Xiang Chen, Pengpeng Li, Qiyuan Guan, Guiyue Jin, Jiyu Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06734v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, vr, 3d gaussian, dynamic  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: autonomous driving, ar, gaussian splatting, dynamic, 4d, human, urban scene  
- **[Physics-Informed Deformable Gaussian Splatting: Towards Unified Constitutive Laws for Time-Evolving Material Field](https://arxiv.org/abs/2511.06299v2)**  
  Authors: Haoqin Hong, Ding Fan, Fubin Dou, Zhi-Li Zhou, Haoran Sun, Congcong Zhu, Jingrun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06299v2.pdf)  
  Keywords: geometry, ar, gaussian splatting, 3d gaussian, motion, dynamic, 4d, efficient  
- **[StreamSTGS: Streaming Spatial and Temporal Gaussian Grids for Real-Time Free-Viewpoint Video](https://arxiv.org/abs/2511.06046v1)**  
  Authors: Zhihui Ke, Yuyang Liu, Xiaobo Zhou, Tie Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06046v1.pdf)  
  Keywords: compression, face, gaussian splatting, ar, motion, 3d gaussian, deformation, dynamic  
- **[4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes from Monocular Videos](https://arxiv.org/abs/2511.05229v1)**  
  Authors: Mengqi Guo, Bo Xu, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.05229v1.pdf)  
  Keywords: efficient, geometry, segmentation, gaussian splatting, ar, 3d gaussian, motion, dynamic, deformation, 4d, neural rendering, nerf  
- **[Splatography: Sparse multi-view dynamic Gaussian Splatting for filmmaking challenges](https://arxiv.org/abs/2511.05152v1)**  
  Authors: Adrian Azzarelli, Nantheera Anantrasirichai, David R Bull  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.05152v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://interims-git.github.io/)  
  Keywords: ar, deformation, gaussian splatting, dynamic  

### Few-shot

*Showing the latest 50 out of 74 papers*

- **[Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction](https://arxiv.org/abs/2511.07122v1)**  
  Authors: Changyue Shi, Chuxiao Yang, Xinyuan Hu, Minghao Chen, Wenwen Pan, Yan Yang, Jiajun Ding, Zhou Yu, Jun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07122v1.pdf)  
  Keywords: ar, gaussian splatting, deformation, dynamic, 4d, few-shot, nerf  
- **[FastGS: Training 3D Gaussian Splatting in 100 Seconds](https://arxiv.org/abs/2511.04283v1)**  
  Authors: Shiwei Ren, Tianci Wen, Yongchun Fang, Biao Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04283v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fastgs.github.io/)  
  Keywords: head, efficient, sparse-view, gaussian splatting, face, ar, 3d gaussian, fast, dynamic, mapping, localization, nerf, acceleration  
- **[DentalSplat: Dental Occlusion Novel View Synthesis from Sparse Intra-Oral Photographs](https://arxiv.org/abs/2511.03099v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Sihao Li, Ji Jiang, Youpeng Yang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.03099v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, sparse view, 3d reconstruction  
- **[Initialize to Generalize: A Stronger Initialization Pipeline for Sparse-View 3DGS](https://arxiv.org/abs/2510.17479v1)**  
  Authors: Feng Zhou, Wenkai Guo, Pu Cao, Zhicheng Zhang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.17479v1.pdf)  
  Keywords: sparse-view, gaussian splatting, ar, motion, 3d gaussian, sparse view, nerf  
- **[Opacity-Gradient Driven Density Control for Compact and Efficient Few-Shot 3D Gaussian Splatting](https://arxiv.org/abs/2510.10257v1)**  
  Authors: Abdelrhman Elrawy, Emad A. Mohammed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10257v1.pdf)  
  Keywords: lightweight, efficient, ar, gaussian splatting, 3d gaussian, nerf, few-shot, compact  
- **[Gesplat: Robust Pose-Free 3D Reconstruction via Geometry-Guided Gaussian Splatting](https://arxiv.org/abs/2510.10097v2)**  
  Authors: Jiahui Lu, Haihong Xiao, Xueyan Zhao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10097v2.pdf)  
  Keywords: geometry, sparse-view, gaussian splatting, ar, 3d gaussian, nerf, 3d reconstruction  
- **[LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates](https://arxiv.org/abs/2510.09881v1)**  
  Authors: Minkwan Kim, Seungmin Lee, Junho Kim, Young Min Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09881v1.pdf)  
  Keywords: sparse-view, gaussian splatting, face, ar, fast, sparse view, few-shot, efficient  
- **[D$^2$GS: Depth-and-Density Guided Gaussian Splatting for Stable and Accurate Sparse-View Reconstruction](https://arxiv.org/abs/2510.08566v1)**  
  Authors: Meixi Song, Xin Lin, Dizhe Zhang, Haodong Li, Xiangtai Li, Bo Du, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08566v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insta360-research-team.github.io/DDGS-website/.)  
  Keywords: high-fidelity, sparse-view, gaussian splatting, ar, 3d gaussian, sparse view  
- **[FSFSplatter: Build Surface and Novel Views with Sparse-Views within 2min](https://arxiv.org/abs/2510.02691v2)**  
  Authors: Yibin Zhao, Yihan Pan, Jun Nan, Liwei Chen, Jianjun Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02691v2.pdf)  
  Keywords: head, geometry, sparse-view, gaussian splatting, face, ar, fast  
- **[HART: Human Aligned Reconstruction Transformer](https://arxiv.org/abs/2509.26621v1)**  
  Authors: Xiyi Chen, Shaofei Wang, Marko Mihajlovic, Taewon Kang, Sergey Prokudin, Ming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.26621v1.pdf)  
  Keywords: geometry, sparse-view, ar, body, human  

### Geometry Reconstruction

*Showing the latest 50 out of 325 papers*

- **[TSPE-GS: Probabilistic Depth Extraction for Semi-Transparent Surface Reconstruction via 3D Gaussian Splatting](https://arxiv.org/abs/2511.09944v1)**  
  Authors: Zhiyuan Xu, Nan Min, Yuhang Guo, Tong Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09944v1.pdf)  
  Keywords: head, geometry, face, gaussian splatting, ar, 3d gaussian  
- **[AHA! Animating Human Avatars in Diverse Scenes with Gaussian Splatting](https://arxiv.org/abs/2511.09827v1)**  
  Authors: Aymen Mir, Jian Wang, Riza Alp Guler, Chuan Guo, Gerard Pons-Moll, Bing Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09827v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, motion, 3d gaussian, human, avatar, animation  
- **[A Shared-Autonomy Construction Robotic System for Overhead Works](https://arxiv.org/abs/2511.09695v1)**  
  Authors: David Minkwan Kim, K. M. Brian Lee, Yong Hyeok Seo, Nikola Raicevic, Runfa Blark Li, Kehan Long, Chan Seon Yoon, Dong Min Kang, Byeong Jo Lim, Young Pyoung Kim, Nikolay Atanasov, Truong Nguyen, Se Woong Jun, Young Wook Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09695v1.pdf)  
  Keywords: head, ar, gaussian splatting, motion, dynamic, 3d reconstruction  
- **[ConeGS: Error-Guided Densification Using Pixel Cones for Improved Reconstruction with Fewer Primitives](https://arxiv.org/abs/2511.06810v1)**  
  Authors: Bartłomiej Baranowski, Stefano Esposito, Patricia Gschoßmann, Anpei Chen, Andreas Geiger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06810v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, 3d gaussian, fast, efficient  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: outdoor, high-fidelity, geometry, ar, gaussian splatting, 3d gaussian  
- **[Physics-Informed Deformable Gaussian Splatting: Towards Unified Constitutive Laws for Time-Evolving Material Field](https://arxiv.org/abs/2511.06299v2)**  
  Authors: Haoqin Hong, Ding Fan, Fubin Dou, Zhi-Li Zhou, Haoran Sun, Congcong Zhu, Jingrun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06299v2.pdf)  
  Keywords: geometry, ar, gaussian splatting, 3d gaussian, motion, dynamic, 4d, efficient  
- **[4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes from Monocular Videos](https://arxiv.org/abs/2511.05229v1)**  
  Authors: Mengqi Guo, Bo Xu, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.05229v1.pdf)  
  Keywords: efficient, geometry, segmentation, gaussian splatting, ar, 3d gaussian, motion, dynamic, deformation, 4d, neural rendering, nerf  
- **[3D Gaussian Point Encoders](https://arxiv.org/abs/2511.04797v1)**  
  Authors: Jim James, Ben Wilson, Simon Lucey, James Hays  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04797v1.pdf)  
  Keywords: lightweight, recognition, efficient, geometry, ar, gaussian splatting, 3d gaussian, fast, nerf, 3d reconstruction  
- **[CaRF: Enhancing Multi-View Consistency in Referring 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/2511.03992v1)**  
  Authors: Yuwen Tao, Kanglei Zhou, Xin Tan, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.03992v1.pdf)  
  Keywords: geometry, segmentation, gaussian splatting, ar, vr, 3d gaussian, understanding  
- **[DentalSplat: Dental Occlusion Novel View Synthesis from Sparse Intra-Oral Photographs](https://arxiv.org/abs/2511.03099v1)**  
  Authors: Yiyi Miao, Taoyu Wu, Tong Chen, Sihao Li, Ji Jiang, Youpeng Yang, Angelos Stefanidis, Limin Yu, Jionglong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.03099v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, sparse view, 3d reconstruction  

### Large Scene

*Showing the latest 50 out of 75 papers*

- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: outdoor, high-fidelity, geometry, ar, gaussian splatting, 3d gaussian  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: autonomous driving, ar, gaussian splatting, dynamic, 4d, human, urban scene  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: head, ar, gaussian splatting, large scene, 3d gaussian, fast  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: outdoor, geometry, ar, gaussian splatting, motion, 3d gaussian, mapping, slam, understanding  
- **[D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction](https://arxiv.org/abs/2510.25173v2)**  
  Authors: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25173v2.pdf)  
  Keywords: geometry, autonomous driving, ar, gaussian splatting, urban scene  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: semantic, face, gaussian splatting, ar, urban scene, 3d reconstruction  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/2510.22669v1)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22669v1.pdf)  
  Keywords: outdoor, high-fidelity, segmentation, gaussian splatting, ar, 3d gaussian, dynamic, mapping, slam, human  
- **[Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering](https://arxiv.org/abs/2510.13381v1)**  
  Authors: Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13381v1.pdf)  
  Keywords: tracking, segmentation, gaussian splatting, ar, motion, 3d gaussian, deformation, dynamic, urban scene  
- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: semantic, autonomous driving, face, gaussian splatting, ar, dynamic, urban scene, 3d reconstruction  
- **[Two-Stage Gaussian Splatting Optimization for Outdoor Scene Reconstruction](https://arxiv.org/abs/2510.09489v1)**  
  Authors: Deborah Pintani, Ariel Caputo, Noah Lewis, Marc Stamminger, Fabio Pellacini, Andrea Giachetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09489v1.pdf)  
  Keywords: outdoor, ar, gaussian splatting, motion, illumination  

### Model Compression

*Showing the latest 50 out of 404 papers*

- **[OUGS: Active View Selection via Object-aware Uncertainty Estimation in 3DGS](https://arxiv.org/abs/2511.09397v1)**  
  Authors: Haiyi Li, Qi Chen, Denis Kalkofen, Hsiang-Ting Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09397v1.pdf)  
  Keywords: semantic, high-fidelity, segmentation, gaussian splatting, ar, 3d gaussian, efficient  
- **[UltraGS: Gaussian Splatting for Ultrasound Novel View Synthesis](https://arxiv.org/abs/2511.07743v1)**  
  Authors: Yuezhe Yang, Wenjie Cai, Dexin Yang, Yufang Dong, Xingbo Dong, Zhe Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07743v1.pdf)  
  Keywords: reflection, lightweight, gaussian splatting, ar  
- **[GFix: Perceptually Enhanced Gaussian Splatting Video Compression](https://arxiv.org/abs/2511.06953v1)**  
  Authors: Siyue Teng, Ge Gao, Duolikun Danier, Yuxuan Jiang, Fan Zhang, Thomas Davis, Zoe Liu, David Bull  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06953v1.pdf)  
  Keywords: compression, ar, gaussian splatting, quality enhancement, 3d gaussian, fast, efficient  
- **[ConeGS: Error-Guided Densification Using Pixel Cones for Improved Reconstruction with Fewer Primitives](https://arxiv.org/abs/2511.06810v1)**  
  Authors: Bartłomiej Baranowski, Stefano Esposito, Patricia Gschoßmann, Anpei Chen, Andreas Geiger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06810v1.pdf)  
  Keywords: geometry, ar, gaussian splatting, 3d gaussian, fast, efficient  
- **[Inpaint360GS: Efficient Object-Aware 3D Inpainting via Gaussian Splatting for 360° Scenes](https://arxiv.org/abs/2511.06457v1)**  
  Authors: Shaoxiang Wang, Shihong Zhang, Christen Millerdurai, Rüdiger Westermann, Didier Stricker, Alain Pagani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06457v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dfki-av.github.io/inpaint360gs/)  
  Keywords: high-fidelity, segmentation, gaussian splatting, ar, 3d gaussian, nerf, efficient  
- **[Physics-Informed Deformable Gaussian Splatting: Towards Unified Constitutive Laws for Time-Evolving Material Field](https://arxiv.org/abs/2511.06299v2)**  
  Authors: Haoqin Hong, Ding Fan, Fubin Dou, Zhi-Li Zhou, Haoran Sun, Congcong Zhu, Jingrun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06299v2.pdf)  
  Keywords: geometry, ar, gaussian splatting, 3d gaussian, motion, dynamic, 4d, efficient  
- **[StreamSTGS: Streaming Spatial and Temporal Gaussian Grids for Real-Time Free-Viewpoint Video](https://arxiv.org/abs/2511.06046v1)**  
  Authors: Zhihui Ke, Yuyang Liu, Xiaobo Zhou, Tie Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06046v1.pdf)  
  Keywords: compression, face, gaussian splatting, ar, motion, 3d gaussian, deformation, dynamic  
- **[4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes from Monocular Videos](https://arxiv.org/abs/2511.05229v1)**  
  Authors: Mengqi Guo, Bo Xu, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.05229v1.pdf)  
  Keywords: efficient, geometry, segmentation, gaussian splatting, ar, 3d gaussian, motion, dynamic, deformation, 4d, neural rendering, nerf  
- **[Efficient representation of 3D spatial data for defense-related applications](https://arxiv.org/abs/2511.05109v1)**  
  Authors: Benjamin Kahl, Marcus Hebel, Michael Arens  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.05109v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, 3d gaussian, nerf, efficient  
- **[Channel Knowledge Map Construction: Recent Advances and Open Challenges](https://arxiv.org/abs/2511.04944v1)**  
  Authors: Zixiang Ren, Juncong Zhou, Jie Xu, Ling Qiu, Yong Zeng, Han Hu, Juyong Zhang, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04944v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, lighting, efficient  

### Quality Enhancement

*Showing the latest 50 out of 182 papers*

- **[OUGS: Active View Selection via Object-aware Uncertainty Estimation in 3DGS](https://arxiv.org/abs/2511.09397v1)**  
  Authors: Haiyi Li, Qi Chen, Denis Kalkofen, Hsiang-Ting Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09397v1.pdf)  
  Keywords: semantic, high-fidelity, segmentation, gaussian splatting, ar, 3d gaussian, efficient  
- **[Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric](https://arxiv.org/abs/2511.08032v1)**  
  Authors: Zhaolin Wan, Yining Diao, Jingqi Xu, Hao Wang, Zhiyang Li, Xiaopeng Fan, Wangmeng Zuo, Debin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.08032v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, lighting, 3d gaussian  
- **[GFix: Perceptually Enhanced Gaussian Splatting Video Compression](https://arxiv.org/abs/2511.06953v1)**  
  Authors: Siyue Teng, Ge Gao, Duolikun Danier, Yuxuan Jiang, Fan Zhang, Thomas Davis, Zoe Liu, David Bull  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06953v1.pdf)  
  Keywords: compression, ar, gaussian splatting, quality enhancement, 3d gaussian, fast, efficient  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: outdoor, high-fidelity, geometry, ar, gaussian splatting, 3d gaussian  
- **[Rethinking Rainy 3D Scene Reconstruction via Perspective Transforming and Brightness Tuning](https://arxiv.org/abs/2511.06734v1)**  
  Authors: Qianfeng Yang, Xiang Chen, Pengpeng Li, Qiyuan Guan, Guiyue Jin, Jiyu Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06734v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, vr, 3d gaussian, dynamic  
- **[Inpaint360GS: Efficient Object-Aware 3D Inpainting via Gaussian Splatting for 360° Scenes](https://arxiv.org/abs/2511.06457v1)**  
  Authors: Shaoxiang Wang, Shihong Zhang, Christen Millerdurai, Rüdiger Westermann, Didier Stricker, Alain Pagani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06457v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dfki-av.github.io/inpaint360gs/)  
  Keywords: high-fidelity, segmentation, gaussian splatting, ar, 3d gaussian, nerf, efficient  
- **[Efficient representation of 3D spatial data for defense-related applications](https://arxiv.org/abs/2511.05109v1)**  
  Authors: Benjamin Kahl, Marcus Hebel, Michael Arens  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.05109v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, 3d gaussian, nerf, efficient  
- **[Channel Knowledge Map Construction: Recent Advances and Open Challenges](https://arxiv.org/abs/2511.04944v1)**  
  Authors: Zixiang Ren, Juncong Zhou, Jie Xu, Ling Qiu, Yong Zeng, Han Hu, Juyong Zhang, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04944v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, lighting, efficient  
- **[Object-Centric 3D Gaussian Splatting for Strawberry Plant Reconstruction and Phenotyping](https://arxiv.org/abs/2511.02207v1)**  
  Authors: Jiajia Li, Keyi Zhu, Qianwen Zhang, Dong Chen, Qi Sun, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.02207v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, 3d gaussian, dynamic, neural rendering, nerf, 3d reconstruction  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: semantic, survey, high-fidelity, robotics, ar, gaussian splatting, 3d gaussian, mapping, slam, efficient, localization  

### Ray Tracing

- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: geometry, reflection, ar, gaussian splatting, ray tracing, illumination  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: geometry, ar, gaussian splatting, ray marching, 3d gaussian, efficient  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: shadow, light transport, face, gaussian splatting, lighting, ar, real-time rendering, relightable, ray tracing, efficient  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: relighting, global illumination, light transport, geometry, reflection, ar, gaussian splatting, lighting, illumination, efficient  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v2)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v2.pdf)  
  Keywords: ar, gaussian splatting, fast, dynamic, 4d, ray tracing  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: relighting, high-fidelity, geometry, reflection, face, gaussian splatting, lighting, ar, 3d gaussian, ray tracing, illumination, nerf  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: relighting, shadow, global illumination, outdoor, face, gaussian splatting, lighting, ar, 3d gaussian, dynamic, relightable, illumination  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: face, gaussian splatting, lighting, ar, 3d gaussian, dynamic, path tracing  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relighting, efficient rendering, geometry, face, gaussian splatting, ray marching, lighting, 3d gaussian, ar, relightable, efficient  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, real-time rendering, ray tracing, efficient  

### Relighting

*Showing the latest 50 out of 119 papers*

- **[Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric](https://arxiv.org/abs/2511.08032v1)**  
  Authors: Zhaolin Wan, Yining Diao, Jingqi Xu, Hao Wang, Zhiyang Li, Xiaopeng Fan, Wangmeng Zuo, Debin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.08032v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, lighting, 3d gaussian  
- **[UltraGS: Gaussian Splatting for Ultrasound Novel View Synthesis](https://arxiv.org/abs/2511.07743v1)**  
  Authors: Yuezhe Yang, Wenjie Cai, Dexin Yang, Yufang Dong, Xingbo Dong, Zhe Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.07743v1.pdf)  
  Keywords: reflection, lightweight, gaussian splatting, ar  
- **[Channel Knowledge Map Construction: Recent Advances and Open Challenges](https://arxiv.org/abs/2511.04944v1)**  
  Authors: Zixiang Ren, Juncong Zhou, Jie Xu, Ling Qiu, Yong Zeng, Han Hu, Juyong Zhang, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04944v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, lighting, efficient  
- **[RoGER-SLAM: A Robust Gaussian Splatting SLAM System for Noisy and Low-light Environment Resilience](https://arxiv.org/abs/2510.22600v1)**  
  Authors: Huilin Yin, Zhaolin Yang, Linchuan Zhang, Gerhard Rigoll, Johannes Betz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22600v1.pdf)  
  Keywords: semantic, tracking, high-fidelity, ar, gaussian splatting, 3d gaussian, mapping, slam, illumination, localization  
- **[Dino-Diffusion Modular Designs Bridge the Cross-Domain Gap in Autonomous Parking](https://arxiv.org/abs/2510.20335v1)**  
  Authors: Zixuan Wu, Hengyuan Zhang, Ting-Hsuan Chen, Yuliang Guo, David Paz, Xinyu Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.20335v1.pdf)  
  Keywords: ar, gaussian splatting, lighting, motion, 3d gaussian  
- **[Moving Light Adaptive Colonoscopy Reconstruction via Illumination-Attenuation-Aware 3D Gaussian Splatting](https://arxiv.org/abs/2510.18739v1)**  
  Authors: Hao Wang, Ying Zhou, Haoyu Zhao, Rui Wang, Qiang Hu, Xing Zhang, Qiang Li, Zhiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18739v1.pdf)  
  Keywords: tracking, geometry, ar, gaussian splatting, 3d gaussian, dynamic, illumination, 3d reconstruction  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: survey, efficient rendering, face, gaussian splatting, lighting, ar, 3d gaussian, real-time rendering, avatar, efficient, 3d reconstruction, animation  
- **[2DGS-R: Revisiting the Normal Consistency Regularization in 2D Gaussian Splatting](https://arxiv.org/abs/2510.16837v1)**  
  Authors: Haofan Ren, Qingsong Yan, Ming Lu, Rongfeng Lu, Zunjie Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16837v1.pdf)  
  Keywords: head, high-fidelity, face, gaussian splatting, lighting, ar, 3d gaussian  
- **[GauSSmart: Enhanced 3D Reconstruction through 2D Foundation Models and Geometric Filtering](https://arxiv.org/abs/2510.14270v3)**  
  Authors: Alexander Valverde, Brian Xu, Yuyin Zhou, Meng Xu, Hongyun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14270v3.pdf)  
  Keywords: semantic, segmentation, gaussian splatting, lighting, ar, 3d gaussian, nerf, 3d reconstruction  
- **[Virtually Being: Customizing Camera-Controllable Video Diffusion Models with Multi-View Performance Captures](https://arxiv.org/abs/2510.14179v1)**  
  Authors: Yuancheng Xu, Wenqi Xian, Li Ma, Julien Philip, Ahmet Levent Taşel, Yiwei Zhao, Ryan Burgert, Mingming He, Oliver Hermann, Oliver Pilarski, Rahul Garg, Paul Debevec, Ning Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14179v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eyeline-labs.github.io/Virtually-Being.)  
  Keywords: relighting, ar, gaussian splatting, lighting, motion, 4d, efficient  

### SLAM

*Showing the latest 50 out of 139 papers*

- **[FastGS: Training 3D Gaussian Splatting in 100 Seconds](https://arxiv.org/abs/2511.04283v1)**  
  Authors: Shiwei Ren, Tianci Wen, Yongchun Fang, Biao Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04283v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fastgs.github.io/)  
  Keywords: head, efficient, sparse-view, gaussian splatting, face, ar, 3d gaussian, fast, dynamic, mapping, localization, nerf, acceleration  
- **[WildfireX-SLAM: A Large-scale Low-altitude RGB-D Dataset for Wildfire SLAM and Beyond](https://arxiv.org/abs/2510.27133v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.27133v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhicongsun.github.io/wildfirexslam.)  
  Keywords: ar, gaussian splatting, 3d gaussian, mapping, slam, localization  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: outdoor, geometry, ar, gaussian splatting, motion, 3d gaussian, mapping, slam, understanding  
- **[LagMemo: Language 3D Gaussian Splatting Memory for Multi-modal Open-vocabulary Multi-goal Visual Navigation](https://arxiv.org/abs/2510.24118v1)**  
  Authors: Haotian Zhou, Xiaole Wang, He Li, Fusheng Sun, Shengyu Guo, Guolei Qi, Jianghuan Xu, Huijing Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.24118v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weekgoodday.github.io/lagmemo)  
  Keywords: ar, gaussian splatting, 3d gaussian, dynamic, localization  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: semantic, survey, high-fidelity, robotics, ar, gaussian splatting, 3d gaussian, mapping, slam, efficient, localization  
- **[LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering](https://arxiv.org/abs/2510.22669v1)**  
  Authors: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22669v1.pdf)  
  Keywords: outdoor, high-fidelity, segmentation, gaussian splatting, ar, 3d gaussian, dynamic, mapping, slam, human  
- **[RoGER-SLAM: A Robust Gaussian Splatting SLAM System for Noisy and Low-light Environment Resilience](https://arxiv.org/abs/2510.22600v1)**  
  Authors: Huilin Yin, Zhaolin Yang, Linchuan Zhang, Gerhard Rigoll, Johannes Betz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.22600v1.pdf)  
  Keywords: semantic, tracking, high-fidelity, ar, gaussian splatting, 3d gaussian, mapping, slam, illumination, localization  
- **[COS3D: Collaborative Open-Vocabulary 3D Segmentation](https://arxiv.org/abs/2510.20238v1)**  
  Authors: Runsong Zhu, Ka-Hei Hui, Zhengzhe Liu, Qianyi Wu, Weiliang Tang, Shi Qiu, Pheng-Ann Heng, Chi-Wing Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.20238v1.pdf)  
  Keywords: robotics, segmentation, ar, mapping, efficient, understanding  
- **[Moving Light Adaptive Colonoscopy Reconstruction via Illumination-Attenuation-Aware 3D Gaussian Splatting](https://arxiv.org/abs/2510.18739v1)**  
  Authors: Hao Wang, Ying Zhou, Haoyu Zhao, Rui Wang, Qiang Hu, Xing Zhang, Qiang Li, Zhiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18739v1.pdf)  
  Keywords: tracking, geometry, ar, gaussian splatting, 3d gaussian, dynamic, illumination, 3d reconstruction  
- **[REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting](https://arxiv.org/abs/2510.16410v1)**  
  Authors: Changyue Shi, Minghao Chen, Yiping Mao, Chuxiao Yang, Xinyuan Hu, Jiajun Ding, Zhou Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16410v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ChangyueShi.github.io/REALM.)  
  Keywords: robotics, segmentation, gaussian splatting, ar, 3d gaussian, human, understanding, localization  

### Scene Understanding

*Showing the latest 50 out of 199 papers*

- **[OUGS: Active View Selection via Object-aware Uncertainty Estimation in 3DGS](https://arxiv.org/abs/2511.09397v1)**  
  Authors: Haiyi Li, Qi Chen, Denis Kalkofen, Hsiang-Ting Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.09397v1.pdf)  
  Keywords: semantic, high-fidelity, segmentation, gaussian splatting, ar, 3d gaussian, efficient  
- **[Inpaint360GS: Efficient Object-Aware 3D Inpainting via Gaussian Splatting for 360° Scenes](https://arxiv.org/abs/2511.06457v1)**  
  Authors: Shaoxiang Wang, Shihong Zhang, Christen Millerdurai, Rüdiger Westermann, Didier Stricker, Alain Pagani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06457v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dfki-av.github.io/inpaint360gs/)  
  Keywords: high-fidelity, segmentation, gaussian splatting, ar, 3d gaussian, nerf, efficient  
- **[4D3R: Motion-Aware Neural Reconstruction and Rendering of Dynamic Scenes from Monocular Videos](https://arxiv.org/abs/2511.05229v1)**  
  Authors: Mengqi Guo, Bo Xu, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.05229v1.pdf)  
  Keywords: efficient, geometry, segmentation, gaussian splatting, ar, 3d gaussian, motion, dynamic, deformation, 4d, neural rendering, nerf  
- **[3D Gaussian Point Encoders](https://arxiv.org/abs/2511.04797v1)**  
  Authors: Jim James, Ben Wilson, Simon Lucey, James Hays  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04797v1.pdf)  
  Keywords: lightweight, recognition, efficient, geometry, ar, gaussian splatting, 3d gaussian, fast, nerf, 3d reconstruction  
- **[CaRF: Enhancing Multi-View Consistency in Referring 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/2511.03992v1)**  
  Authors: Yuwen Tao, Kanglei Zhou, Xin Tan, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.03992v1.pdf)  
  Keywords: geometry, segmentation, gaussian splatting, ar, vr, 3d gaussian, understanding  
- **[PercHead: Perceptual Head Model for Single-Image 3D Head Reconstruction & Editing](https://arxiv.org/abs/2511.02777v1)**  
  Authors: Antonio Oroz, Matthias Nießner, Tobias Kirschstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.02777v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://antoniooroz.github.io/PercHead)  
  Keywords: semantic, lightweight, head, geometry, segmentation, gaussian splatting, ar  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: outdoor, geometry, ar, gaussian splatting, motion, 3d gaussian, mapping, slam, understanding  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: semantic, face, gaussian splatting, ar, urban scene, 3d reconstruction  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: semantic, survey, high-fidelity, robotics, ar, gaussian splatting, 3d gaussian, mapping, slam, efficient, localization  
- **[PlanarGS: High-Fidelity Indoor 3D Gaussian Splatting Guided by Vision-Language Planar Priors](https://arxiv.org/abs/2510.23930v1)**  
  Authors: Xirui Jin, Renbiao Jin, Boying Li, Danping Zou, Wenxian Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://planargs.github.io)  
  Keywords: high-fidelity, geometry, face, gaussian splatting, segmentation, ar, 3d gaussian, efficient  



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