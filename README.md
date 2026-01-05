# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-01-05 01:03:47

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
- [Acceleration](#acceleration) (252 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (344 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (400 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (80 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (351 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (70 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (404 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (198 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (19 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (127 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (144 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (207 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197v1)**  
  Authors: Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07197v1.pdf)  
  Keywords: survey, compression, high-fidelity, gaussian splatting, 3d gaussian, dynamic, 4d, efficient, ar, compact, 3d reconstruction  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v1)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v1.pdf)  
  Keywords: survey, robotics, slam, gaussian splatting, 3d gaussian, mapping, understanding, nerf, ar, localization, semantic  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: survey, robotics, high-fidelity, slam, gaussian splatting, 3d gaussian, mapping, efficient, ar, localization, semantic  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: survey, gaussian splatting, 3d gaussian, motion, 4d, geometry, nerf, ar, fast  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: survey, real-time rendering, lighting, gaussian splatting, 3d gaussian, animation, efficient, face, ar, efficient rendering, avatar, 3d reconstruction  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: survey, human, gaussian splatting, efficient, understanding, nerf, ar, lightweight  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: survey, slam, gaussian splatting, 3d gaussian, neural rendering, efficient, understanding, nerf, ar, fast  
- **[A-TDOM: Active TDOM via On-the-Fly 3DGS](https://arxiv.org/abs/2509.12759v3)**  
  Authors: Yiwei Xu, Xiang Wang, Yifei Yu, Wentian Gan, Luca Morelli, Giulio Perda, Xin Wang, Zongqian Zhan, Fabio Remondino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.12759v3.pdf)  
  Keywords: survey, gaussian splatting, 3d gaussian, face, ar  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: survey, high-fidelity, lighting, gaussian splatting, 3d gaussian, understanding, nerf, ar, compact, segmentation, semantic  
- **[A Study of the Framework and Real-World Applications of Language Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: survey, robotics, gaussian splatting, 3d gaussian, efficient, understanding, nerf, ar, semantic  

### Acceleration

*Showing the latest 50 out of 252 papers*

- **[Contour Information Aware 2D Gaussian Splatting for Image Representation](https://arxiv.org/abs/2512.23255v1)**  
  Authors: Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai, Zheming Fan, Ryo Ishimoto, Kakeru Sugimoto, Ruri Imichi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23255v1.pdf)  
  Keywords: compression, gaussian splatting, efficient, ar, compact, segmentation, lightweight, fast  
- **[AirGS: Real-Time 4D Gaussian Streaming for Free-Viewpoint Video Experiences](https://arxiv.org/abs/2512.20943v1)**  
  Authors: Zhe Wang, Jinghang Li, Yifei Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20943v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, 4d, dynamic, efficient, head, ar, lightweight, fast  
- **[Quantile Rendering: Efficiently Embedding High-dimensional Feature on 3D Gaussian Splatting](https://arxiv.org/abs/2512.20927v1)**  
  Authors: Yoonwoo Jeong, Cheng Sun, Frank Wang, Minsu Cho, Jaesung Choe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20927v1.pdf)  
  Keywords: compression, real-time rendering, gaussian splatting, 3d gaussian, efficient, ar, segmentation  
- **[Nebula: Enable City-Scale 3D Gaussian Splatting in Virtual Reality via Collaborative Rendering and Accelerated Stereo Rasterization](https://arxiv.org/abs/2512.20495v1)**  
  Authors: He Zhu, Zheng Liu, Xingyang Li, Anbang Wu, Jieru Zhao, Fangxin Liu, Yiming Gan, Jingwen Leng, Yu Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20495v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, motion, ar, vr, acceleration  
- **[4D Gaussian Splatting as a Learned Dynamical System](https://arxiv.org/abs/2512.19648v1)**  
  Authors: Arnold Caleb Asiimwe, Carl Vondrick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19648v1.pdf)  
  Keywords: deformation, real-time rendering, gaussian splatting, motion, 4d, dynamic, efficient, ar  
- **[Geometric-Photometric Event-based 3D Gaussian Ray Tracing](https://arxiv.org/abs/2512.18640v1)**  
  Authors: Kai Kohyama, Yoshimitsu Aoki, Guillermo Gallego, Shintaro Shiba  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18640v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, motion, understanding, ray tracing, geometry, ar, fast, 3d reconstruction  
- **[Voxel-GS: Quantized Scaffold Gaussian Splatting Compression with Run-Length Coding](https://arxiv.org/abs/2512.17528v1)**  
  Authors: Chunyang Fu, Xiangrui Liu, Shiqi Wang, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17528v1.pdf)  
  Keywords: compression, high-fidelity, gaussian splatting, ar, compact, lightweight, fast  
- **[Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation](https://arxiv.org/abs/2512.16893v1)**  
  Authors: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16893v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/instant4d)  
  Keywords: gaussian splatting, animation, motion, 4d, efficient, face, head, ar, lightweight, avatar, fast  
- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, face, ray tracing, nerf, ar, fast  
- **[Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering](https://arxiv.org/abs/2512.15711v1)**  
  Authors: Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Tomas Simon, Forrest Iandola, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15711v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, face, head, ar, efficient rendering, avatar  

### Applications

*Showing the latest 50 out of 995 papers*

- **[PhysTalk: Language-driven Real-time Physics in 3D Gaussian Scenes](https://arxiv.org/abs/2512.24986v1)**  
  Authors: Luca Collorone, Mert Kiray, Indro Spinelli, Fabio Galasso, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24986v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, animation, 4d, dynamic, face, ar, lightweight  
- **[UniC-Lift: Unified 3D Instance Segmentation via Contrastive Learning](https://arxiv.org/abs/2512.24763v1)**  
  Authors: Ankit Dhiman, Srinath R, Jaswanth Reddy, Lokesh R Boregowda, Venkatesh Babu Radhakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24763v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, understanding, nerf, ar, segmentation, semantic  
- **[Splatwizard: A Benchmark Toolkit for 3D Gaussian Splatting Compression](https://arxiv.org/abs/2512.24742v1)**  
  Authors: Xiang Liu, Yimin Zhou, Jinxiang Wang, Yujun Huang, Shuzhao Xie, Shiyu Qin, Mingyao Hong, Jiawei Li, Yaowei Wang, Zhi Wang, Shu-Tao Xia, Bin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24742v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, compression  
- **[Structure-Guided Allocation of 2D Gaussians for Image Representation and Compression](https://arxiv.org/abs/2512.24018v1)**  
  Authors: Huanxiong Liang, Yunuo Chen, Yicheng Pan, Sixian Wang, Jincheng Dai, Guo Lu, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24018v1.pdf)  
  Keywords: compression, gaussian splatting, geometry, ar, compact, semantic  
- **[Improved 3D Gaussian Splatting of Unknown Spacecraft Structure Using Space Environment Illumination Knowledge](https://arxiv.org/abs/2512.23998v1)**  
  Authors: Tae Ha Park, Simone D'Amico  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23998v1.pdf)  
  Keywords: lighting, gaussian splatting, 3d gaussian, illumination, dynamic, geometry, ar, shadow  
- **[Contour Information Aware 2D Gaussian Splatting for Image Representation](https://arxiv.org/abs/2512.23255v1)**  
  Authors: Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai, Zheming Fan, Ryo Ishimoto, Kakeru Sugimoto, Ruri Imichi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23255v1.pdf)  
  Keywords: compression, gaussian splatting, efficient, ar, compact, segmentation, lightweight, fast  
- **[GVSynergy-Det: Synergistic Gaussian-Voxel Representations for Multi-View 3D Object Detection](https://arxiv.org/abs/2512.23176v1)**  
  Authors: Yi Zhang, Yi Wang, Lei Yao, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23176v1.pdf)  
  Keywords: gaussian splatting, face, geometry, ar, localization  
- **[Differentiable Physics-Driven Human Representation for Millimeter-Wave Based Pose Estimation](https://arxiv.org/abs/2512.23054v2)**  
  Authors: Shuntian Zheng, Guangming Wang, Jiaqi Li, Minzhe Ni, Yu Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23054v2.pdf)  
  Keywords: human, gaussian splatting, motion, face, ar  
- **[Hash Grid Feature Pruning](https://arxiv.org/abs/2512.22882v1)**  
  Authors: Yangzhi Ma, Bojun Liu, Jie Li, Li Li, Dong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22882v1.pdf)  
  Keywords: gaussian splatting, head, ar  
- **[SCPainter: A Unified Framework for Realistic 3D Asset Insertion and Novel View Synthesis](https://arxiv.org/abs/2512.22706v1)**  
  Authors: Paul Dobre, Jackson Cooper, Xin Wang, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22706v1.pdf)  
  Keywords: lighting, high quality, 3d gaussian, dynamic, ar, shadow, autonomous driving  

### Avatar Generation

*Showing the latest 50 out of 344 papers*

- **[PhysTalk: Language-driven Real-time Physics in 3D Gaussian Scenes](https://arxiv.org/abs/2512.24986v1)**  
  Authors: Luca Collorone, Mert Kiray, Indro Spinelli, Fabio Galasso, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24986v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, animation, 4d, dynamic, face, ar, lightweight  
- **[GVSynergy-Det: Synergistic Gaussian-Voxel Representations for Multi-View 3D Object Detection](https://arxiv.org/abs/2512.23176v1)**  
  Authors: Yi Zhang, Yi Wang, Lei Yao, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23176v1.pdf)  
  Keywords: gaussian splatting, face, geometry, ar, localization  
- **[Differentiable Physics-Driven Human Representation for Millimeter-Wave Based Pose Estimation](https://arxiv.org/abs/2512.23054v2)**  
  Authors: Shuntian Zheng, Guangming Wang, Jiaqi Li, Minzhe Ni, Yu Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23054v2.pdf)  
  Keywords: human, gaussian splatting, motion, face, ar  
- **[Hash Grid Feature Pruning](https://arxiv.org/abs/2512.22882v1)**  
  Authors: Yangzhi Ma, Bojun Liu, Jie Li, Li Li, Dong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22882v1.pdf)  
  Keywords: gaussian splatting, head, ar  
- **[AirGS: Real-Time 4D Gaussian Streaming for Free-Viewpoint Video Experiences](https://arxiv.org/abs/2512.20943v1)**  
  Authors: Zhe Wang, Jinghang Li, Yifei Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20943v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, 4d, dynamic, efficient, head, ar, lightweight, fast  
- **[Dreamcrafter: Immersive Editing of 3D Radiance Fields Through Flexible, Generative Inputs and Outputs](https://arxiv.org/abs/2512.20129v2)**  
  Authors: Cyrus Vachha, Yixiao Kang, Zach Dive, Ashwat Chidambaram, Anik Gupta, Eunice Jun, Bjoern Hartmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20129v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, face, ar, nerf, vr  
- **[Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation](https://arxiv.org/abs/2512.16893v1)**  
  Authors: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16893v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/instant4d)  
  Keywords: gaussian splatting, animation, motion, 4d, efficient, face, head, ar, lightweight, avatar, fast  
- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, face, ray tracing, nerf, ar, fast  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: human, high-fidelity, lighting, gaussian splatting, relightable, face, geometry, nerf, ar, segmentation, semantic  
- **[Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering](https://arxiv.org/abs/2512.15711v1)**  
  Authors: Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Tomas Simon, Forrest Iandola, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15711v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, face, head, ar, efficient rendering, avatar  

### Dynamic Scene

*Showing the latest 50 out of 400 papers*

- **[PhysTalk: Language-driven Real-time Physics in 3D Gaussian Scenes](https://arxiv.org/abs/2512.24986v1)**  
  Authors: Luca Collorone, Mert Kiray, Indro Spinelli, Fabio Galasso, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24986v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, animation, 4d, dynamic, face, ar, lightweight  
- **[Improved 3D Gaussian Splatting of Unknown Spacecraft Structure Using Space Environment Illumination Knowledge](https://arxiv.org/abs/2512.23998v1)**  
  Authors: Tae Ha Park, Simone D'Amico  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23998v1.pdf)  
  Keywords: lighting, gaussian splatting, 3d gaussian, illumination, dynamic, geometry, ar, shadow  
- **[Differentiable Physics-Driven Human Representation for Millimeter-Wave Based Pose Estimation](https://arxiv.org/abs/2512.23054v2)**  
  Authors: Shuntian Zheng, Guangming Wang, Jiaqi Li, Minzhe Ni, Yu Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23054v2.pdf)  
  Keywords: human, gaussian splatting, motion, face, ar  
- **[SCPainter: A Unified Framework for Realistic 3D Asset Insertion and Novel View Synthesis](https://arxiv.org/abs/2512.22706v1)**  
  Authors: Paul Dobre, Jackson Cooper, Xin Wang, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22706v1.pdf)  
  Keywords: lighting, high quality, 3d gaussian, dynamic, ar, shadow, autonomous driving  
- **[Tracking by Predicting 3-D Gaussians Over Time](https://arxiv.org/abs/2512.22489v2)**  
  Authors: Tanish Baranwal, Himanshu Gaurav Singh, Jathushan Rajasegaran, Jitendra Malik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22489v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://videogmae.org/)  
  Keywords: tracking, mapping, dynamic, ar  
- **[AirGS: Real-Time 4D Gaussian Streaming for Free-Viewpoint Video Experiences](https://arxiv.org/abs/2512.20943v1)**  
  Authors: Zhe Wang, Jinghang Li, Yifei Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20943v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, 4d, dynamic, efficient, head, ar, lightweight, fast  
- **[Nebula: Enable City-Scale 3D Gaussian Splatting in Virtual Reality via Collaborative Rendering and Accelerated Stereo Rasterization](https://arxiv.org/abs/2512.20495v1)**  
  Authors: He Zhu, Zheng Liu, Xingyang Li, Anbang Wu, Jieru Zhao, Fangxin Liu, Yiming Gan, Jingwen Leng, Yu Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20495v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, motion, ar, vr, acceleration  
- **[WorldWarp: Propagating 3D Geometry with Asynchronous Video Diffusion](https://arxiv.org/abs/2512.19678v1)**  
  Authors: Hanyang Kong, Xingyi Yang, Xiaoxu Zheng, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19678v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hyokong.github.io/worldwarp-page/}{https://hyokong.github.io/worldwarp-page/}.)  
  Keywords: gaussian splatting, geometry, ar, dynamic  
- **[4D Gaussian Splatting as a Learned Dynamical System](https://arxiv.org/abs/2512.19648v1)**  
  Authors: Arnold Caleb Asiimwe, Carl Vondrick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19648v1.pdf)  
  Keywords: deformation, real-time rendering, gaussian splatting, motion, 4d, dynamic, efficient, ar  
- **[Geometric-Photometric Event-based 3D Gaussian Ray Tracing](https://arxiv.org/abs/2512.18640v1)**  
  Authors: Kai Kohyama, Yoshimitsu Aoki, Guillermo Gallego, Shintaro Shiba  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18640v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, motion, understanding, ray tracing, geometry, ar, fast, 3d reconstruction  

### Few-shot

*Showing the latest 50 out of 80 papers*

- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v2)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, motion, ar, sparse view, 3d reconstruction  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: light transport, lighting, gaussian splatting, relighting, geometry, ar, segmentation, sparse-view  
- **[Splatent: Splatting Diffusion Latents for Novel View Synthesis](https://arxiv.org/abs/2512.09923v1)**  
  Authors: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09923v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, face, ar, efficient rendering, sparse-view, 3d reconstruction  
- **[Tessellation GS: Neural Mesh Gaussians for Robust Monocular Reconstruction of Dynamic Objects](https://arxiv.org/abs/2512.07381v1)**  
  Authors: Shuohan Tao, Boyao Zhou, Hanzhang Tu, Yuwang Wang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07381v1.pdf)  
  Keywords: deformation, gaussian splatting, 3d gaussian, dynamic, face, ar, sparse-view  
- **[MuSASplat: Efficient Sparse-View 3D Gaussian Splats via Lightweight Multi-Scale Adaptation](https://arxiv.org/abs/2512.07165v1)**  
  Authors: Muyu Xu, Fangneng Zhan, Xiaoqin Zhang, Ling Shao, Shijian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07165v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, head, ar, lightweight, sparse-view  
- **[C3G: Learning Compact 3D Representations with 2K Gaussians](https://arxiv.org/abs/2512.04021v1)**  
  Authors: Honggyu An, Jaewoo Jung, Mungyeom Kim, Sunghwan Hong, Chaehyun Kim, Kazumi Fukuda, Minkyeong Jeon, Jisang Han, Takuya Narihira, Hyuna Ko, Junsu Kim, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04021v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, understanding, head, ar, sparse view, compact, segmentation  
- **[Cross-Temporal 3D Gaussian Splatting for Sparse-View Guided Scene Update](https://arxiv.org/abs/2512.00534v1)**  
  Authors: Zeyuan An, Yanghang Xiao, Zhiying Leng, Frederick W. B. Li, Xiaohui Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00534v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, ar, sparse view, sparse-view  
- **[Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views](https://arxiv.org/abs/2512.00255v1)**  
  Authors: Kunwar Maheep Singh, Jianchun Chen, Vladislav Golyanik, Stephan J. Garbin, Thabo Beeler, Rishabh Dabral, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/RHC/)  
  Keywords: human, tracking, lighting, relightable, 3d gaussian, illumination, relighting, motion, dynamic, efficient, body, geometry, ar, sparse view, sparse-view  
- **[Observer Actor: Active Vision Imitation Learning with Sparse View Gaussian Splatting](https://arxiv.org/abs/2511.18140v1)**  
  Authors: Yilong Wang, Cheng Qian, Ruomeng Fan, Edward Johns  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18140v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://obact.github.io.)  
  Keywords: gaussian splatting, 3d gaussian, dynamic, ar, sparse view  
- **[Frequency-Adaptive Sharpness Regularization for Improving 3D Gaussian Splatting Generalization](https://arxiv.org/abs/2511.17918v1)**  
  Authors: Youngsik Yun, Dongjun Gu, Youngjung Uh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bbangsik13.github.io/FASR.)  
  Keywords: gaussian splatting, 3d gaussian, few-shot, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 351 papers*

- **[Structure-Guided Allocation of 2D Gaussians for Image Representation and Compression](https://arxiv.org/abs/2512.24018v1)**  
  Authors: Huanxiong Liang, Yunuo Chen, Yicheng Pan, Sixian Wang, Jincheng Dai, Guo Lu, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24018v1.pdf)  
  Keywords: compression, gaussian splatting, geometry, ar, compact, semantic  
- **[Improved 3D Gaussian Splatting of Unknown Spacecraft Structure Using Space Environment Illumination Knowledge](https://arxiv.org/abs/2512.23998v1)**  
  Authors: Tae Ha Park, Simone D'Amico  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23998v1.pdf)  
  Keywords: lighting, gaussian splatting, 3d gaussian, illumination, dynamic, geometry, ar, shadow  
- **[GVSynergy-Det: Synergistic Gaussian-Voxel Representations for Multi-View 3D Object Detection](https://arxiv.org/abs/2512.23176v1)**  
  Authors: Yi Zhang, Yi Wang, Lei Yao, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23176v1.pdf)  
  Keywords: gaussian splatting, face, geometry, ar, localization  
- **[Enhancing annotations for 5D apple pose estimation through 3D Gaussian Splatting (3DGS)](https://arxiv.org/abs/2512.20148v1)**  
  Authors: Robert van de Ven, Trim Bresilla, Bram Nelissen, Ard Nieuwenhuizen, Eldert J. van Henten, Gert Kootstra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20148v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, 3d reconstruction  
- **[WorldWarp: Propagating 3D Geometry with Asynchronous Video Diffusion](https://arxiv.org/abs/2512.19678v1)**  
  Authors: Hanyang Kong, Xingyi Yang, Xiaoxu Zheng, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19678v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hyokong.github.io/worldwarp-page/}{https://hyokong.github.io/worldwarp-page/}.)  
  Keywords: gaussian splatting, geometry, ar, dynamic  
- **[Geometric-Photometric Event-based 3D Gaussian Ray Tracing](https://arxiv.org/abs/2512.18640v1)**  
  Authors: Kai Kohyama, Yoshimitsu Aoki, Guillermo Gallego, Shintaro Shiba  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18640v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, motion, understanding, ray tracing, geometry, ar, fast, 3d reconstruction  
- **[MatSpray: Fusing 2D Material World Knowledge on 3D Geometry](https://arxiv.org/abs/2512.18314v1)**  
  Authors: Philipp Langsteiner, Jan-Niklas Dihlmann, Hendrik P. A. Lensch  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18314v1.pdf)  
  Keywords: lighting, gaussian splatting, relightable, relighting, ray tracing, geometry, ar, 3d reconstruction  
- **[G3Splat: Geometrically Consistent Generalizable Gaussian Splatting](https://arxiv.org/abs/2512.17547v1)**  
  Authors: Mehdi Hosseinzadeh, Shin-Fang Chng, Yi Xu, Simon Lucey, Ian Reid, Ravi Garg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17547v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://m80hz.github.io/g3splat/).)  
  Keywords: gaussian splatting, 3d gaussian, geometry, ar  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: human, high-fidelity, lighting, gaussian splatting, relightable, face, geometry, nerf, ar, segmentation, semantic  
- **[Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2512.15508v1)**  
  Authors: Arthur Moreau, Richard Shaw, Michal Nazarczuk, Jisu Shin, Thomas Tanay, Zhensong Zhang, Songcen Xu, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15508v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, ar, 3d reconstruction  

### Large Scene

*Showing the latest 50 out of 70 papers*

- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, illumination, efficient, face, geometry, ar, urban scene, 3d reconstruction  
- **[Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries](https://arxiv.org/abs/2512.13796v1)**  
  Authors: Victor Rong, Jan Held, Victor Chu, Daniel Rebain, Marc Van Droogenbroeck, Kiriakos N. Kutulakos, Andrea Tagliasacchi, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13796v1.pdf)  
  Keywords: outdoor, gaussian splatting, 3d gaussian, geometry, ar, compact, fast  
- **[Flux4D: Flow-based Unsupervised 4D Reconstruction](https://arxiv.org/abs/2512.03210v1)**  
  Authors: Jingkang Wang, Henry Che, Yun Chen, Ze Yang, Lily Goli, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03210v1.pdf)  
  Keywords: robotics, outdoor, gaussian splatting, 3d gaussian, motion, 4d, dynamic, efficient, nerf, ar  
- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: outdoor, gaussian splatting, 3d gaussian, understanding, geometry, ar, 3d reconstruction  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: outdoor, gaussian splatting, geometry, ar, fast, semantic  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: high-fidelity, lighting, outdoor, gaussian splatting, illumination, relighting, efficient, face, geometry, ar, segmentation, semantic  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: high-fidelity, outdoor, gaussian splatting, 3d gaussian, geometry, ar  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: human, gaussian splatting, 4d, dynamic, ar, autonomous driving, urban scene  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: large scene, gaussian splatting, 3d gaussian, head, ar, fast  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: outdoor, slam, gaussian splatting, 3d gaussian, motion, mapping, understanding, geometry, ar  

### Model Compression

*Showing the latest 50 out of 404 papers*

- **[PhysTalk: Language-driven Real-time Physics in 3D Gaussian Scenes](https://arxiv.org/abs/2512.24986v1)**  
  Authors: Luca Collorone, Mert Kiray, Indro Spinelli, Fabio Galasso, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24986v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, animation, 4d, dynamic, face, ar, lightweight  
- **[UniC-Lift: Unified 3D Instance Segmentation via Contrastive Learning](https://arxiv.org/abs/2512.24763v1)**  
  Authors: Ankit Dhiman, Srinath R, Jaswanth Reddy, Lokesh R Boregowda, Venkatesh Babu Radhakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24763v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, understanding, nerf, ar, segmentation, semantic  
- **[Splatwizard: A Benchmark Toolkit for 3D Gaussian Splatting Compression](https://arxiv.org/abs/2512.24742v1)**  
  Authors: Xiang Liu, Yimin Zhou, Jinxiang Wang, Yujun Huang, Shuzhao Xie, Shiyu Qin, Mingyao Hong, Jiawei Li, Yaowei Wang, Zhi Wang, Shu-Tao Xia, Bin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24742v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, compression  
- **[Structure-Guided Allocation of 2D Gaussians for Image Representation and Compression](https://arxiv.org/abs/2512.24018v1)**  
  Authors: Huanxiong Liang, Yunuo Chen, Yicheng Pan, Sixian Wang, Jincheng Dai, Guo Lu, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24018v1.pdf)  
  Keywords: compression, gaussian splatting, geometry, ar, compact, semantic  
- **[Contour Information Aware 2D Gaussian Splatting for Image Representation](https://arxiv.org/abs/2512.23255v1)**  
  Authors: Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai, Zheming Fan, Ryo Ishimoto, Kakeru Sugimoto, Ruri Imichi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23255v1.pdf)  
  Keywords: compression, gaussian splatting, efficient, ar, compact, segmentation, lightweight, fast  
- **[AirGS: Real-Time 4D Gaussian Streaming for Free-Viewpoint Video Experiences](https://arxiv.org/abs/2512.20943v1)**  
  Authors: Zhe Wang, Jinghang Li, Yifei Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20943v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, 4d, dynamic, efficient, head, ar, lightweight, fast  
- **[Quantile Rendering: Efficiently Embedding High-dimensional Feature on 3D Gaussian Splatting](https://arxiv.org/abs/2512.20927v1)**  
  Authors: Yoonwoo Jeong, Cheng Sun, Frank Wang, Minsu Cho, Jaesung Choe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20927v1.pdf)  
  Keywords: compression, real-time rendering, gaussian splatting, 3d gaussian, efficient, ar, segmentation  
- **[SmartSplat: Feature-Smart Gaussians for Scalable Compression of Ultra-High-Resolution Images](https://arxiv.org/abs/2512.20377v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20377v1.pdf)  
  Keywords: compression, gaussian splatting, 3d gaussian, efficient, ar  
- **[4D Gaussian Splatting as a Learned Dynamical System](https://arxiv.org/abs/2512.19648v1)**  
  Authors: Arnold Caleb Asiimwe, Carl Vondrick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19648v1.pdf)  
  Keywords: deformation, real-time rendering, gaussian splatting, motion, 4d, dynamic, efficient, ar  
- **[GaussianImage++: Boosted Image Representation and Compression with 2D Gaussian Splatting](https://arxiv.org/abs/2512.19108v2)**  
  Authors: Tiantian Li, Xinjie Zhang, Xingtong Ge, Tongda Xu, Dailan He, Jun Zhang, Yan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19108v2.pdf)  
  Keywords: gaussian splatting, ar, efficient, compression  

### Quality Enhancement

*Showing the latest 50 out of 198 papers*

- **[SCPainter: A Unified Framework for Realistic 3D Asset Insertion and Novel View Synthesis](https://arxiv.org/abs/2512.22706v1)**  
  Authors: Paul Dobre, Jackson Cooper, Xin Wang, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22706v1.pdf)  
  Keywords: lighting, high quality, 3d gaussian, dynamic, ar, shadow, autonomous driving  
- **[Nebula: Enable City-Scale 3D Gaussian Splatting in Virtual Reality via Collaborative Rendering and Accelerated Stereo Rasterization](https://arxiv.org/abs/2512.20495v1)**  
  Authors: He Zhu, Zheng Liu, Xingyang Li, Anbang Wu, Jieru Zhao, Fangxin Liu, Yiming Gan, Jingwen Leng, Yu Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20495v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, motion, ar, vr, acceleration  
- **[Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding](https://arxiv.org/abs/2512.17817v2)**  
  Authors: Yue Li, Qi Ma, Runyi Yang, Mengjiao Ma, Bin Ren, Nikola Popovic, Nicu Sebe, Theo Gevers, Luc Van Gool, Danda Pani Paudel, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17817v2.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, efficient, ar, segmentation, semantic  
- **[Voxel-GS: Quantized Scaffold Gaussian Splatting Compression with Run-Length Coding](https://arxiv.org/abs/2512.17528v1)**  
  Authors: Chunyang Fu, Xiangrui Liu, Shiqi Wang, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17528v1.pdf)  
  Keywords: compression, high-fidelity, gaussian splatting, ar, compact, lightweight, fast  
- **[Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation](https://arxiv.org/abs/2512.17349v1)**  
  Authors: Xijie Huang, Jinhan Li, Tianyue Wu, Xin Zhou, Zhichao Han, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17349v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, illumination, ar  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: human, high-fidelity, lighting, gaussian splatting, relightable, face, geometry, nerf, ar, segmentation, semantic  
- **[VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments](https://arxiv.org/abs/2512.15258v2)**  
  Authors: Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Yuxin Fan, Wenjun Li, Zhichao Han, Xin Zhou, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15258v2.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, efficient, ar, lightweight, fast  
- **[GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants](https://arxiv.org/abs/2512.14087v1)**  
  Authors: Yang Yang, Risa Shinoda, Hiroaki Santo, Fumio Okura  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14087v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, geometry, ar, 3d reconstruction  
- **[ASAP-Textured Gaussians: Enhancing Textured Gaussians with Adaptive Sampling and Anisotropic Parameterization](https://arxiv.org/abs/2512.14039v1)**  
  Authors: Meng Wei, Cheng Zhang, Jianmin Zheng, Hamid Rezatofighi, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14039v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, efficient, ar  
- **[Fast 2DGS: Efficient Image Representation with Deep Gaussian Prior](https://arxiv.org/abs/2512.12774v1)**  
  Authors: Hao Wang, Ashish Bastola, Chaoyi Zhou, Wenhui Zhu, Xiwen Chen, Xuanzhao Dong, Siyu Huang, Abolfazl Razi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.12774v1.pdf)  
  Keywords: real-time rendering, high-fidelity, gaussian splatting, efficient, ar, lightweight, fast  

### Ray Tracing

- **[Geometric-Photometric Event-based 3D Gaussian Ray Tracing](https://arxiv.org/abs/2512.18640v1)**  
  Authors: Kai Kohyama, Yoshimitsu Aoki, Guillermo Gallego, Shintaro Shiba  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18640v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, motion, understanding, ray tracing, geometry, ar, fast, 3d reconstruction  
- **[MatSpray: Fusing 2D Material World Knowledge on 3D Geometry](https://arxiv.org/abs/2512.18314v1)**  
  Authors: Philipp Langsteiner, Jan-Niklas Dihlmann, Hendrik P. A. Lensch  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18314v1.pdf)  
  Keywords: lighting, gaussian splatting, relightable, relighting, ray tracing, geometry, ar, 3d reconstruction  
- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, face, ray tracing, nerf, ar, fast  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: real-time rendering, high-fidelity, gaussian splatting, 3d gaussian, ray tracing, ar, compact, fast  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: reflection, high-fidelity, gaussian splatting, dynamic, ray tracing, geometry, ar, 3d reconstruction  
- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: reflection, gaussian splatting, illumination, ray tracing, geometry, ar  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: gaussian splatting, 3d gaussian, efficient, geometry, ar, ray marching  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: real-time rendering, light transport, lighting, gaussian splatting, relightable, efficient, face, ray tracing, ar, shadow  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: reflection, light transport, lighting, gaussian splatting, illumination, relighting, efficient, geometry, ar, global illumination  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v2)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v2.pdf)  
  Keywords: gaussian splatting, 4d, dynamic, ray tracing, ar, fast  

### Relighting

*Showing the latest 50 out of 127 papers*

- **[Improved 3D Gaussian Splatting of Unknown Spacecraft Structure Using Space Environment Illumination Knowledge](https://arxiv.org/abs/2512.23998v1)**  
  Authors: Tae Ha Park, Simone D'Amico  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23998v1.pdf)  
  Keywords: lighting, gaussian splatting, 3d gaussian, illumination, dynamic, geometry, ar, shadow  
- **[SCPainter: A Unified Framework for Realistic 3D Asset Insertion and Novel View Synthesis](https://arxiv.org/abs/2512.22706v1)**  
  Authors: Paul Dobre, Jackson Cooper, Xin Wang, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22706v1.pdf)  
  Keywords: lighting, high quality, 3d gaussian, dynamic, ar, shadow, autonomous driving  
- **[MatSpray: Fusing 2D Material World Knowledge on 3D Geometry](https://arxiv.org/abs/2512.18314v1)**  
  Authors: Philipp Langsteiner, Jan-Niklas Dihlmann, Hendrik P. A. Lensch  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18314v1.pdf)  
  Keywords: lighting, gaussian splatting, relightable, relighting, ray tracing, geometry, ar, 3d reconstruction  
- **[Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation](https://arxiv.org/abs/2512.17349v1)**  
  Authors: Xijie Huang, Jinhan Li, Tianyue Wu, Xin Zhou, Zhichao Han, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17349v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, illumination, ar  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: human, high-fidelity, lighting, gaussian splatting, relightable, face, geometry, nerf, ar, segmentation, semantic  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, illumination, efficient, face, geometry, ar, urban scene, 3d reconstruction  
- **[Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere](https://arxiv.org/abs/2512.14180v1)**  
  Authors: Francesco Di Sario, Daniel Rebain, Dor Verbin, Marco Grangetto, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14180v1.pdf)  
  Keywords: reflection, gaussian splatting, 3d gaussian, efficient, ar  
- **[Computer vision training dataset generation for robotic environments using Gaussian splatting](https://arxiv.org/abs/2512.13411v1)**  
  Authors: Patryk Niżeniec, Marcin Iwanowski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13411v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, ar, segmentation, shadow  
- **[Light Field Based 6DoF Tracking of Previously Unobserved Objects](https://arxiv.org/abs/2512.13007v1)**  
  Authors: Nikolai Goncharov, James L. Gray, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13007v1.pdf)  
  Keywords: reflection, robotics, tracking, ar, autonomous driving, semantic  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: reflection, high-fidelity, gaussian splatting, dynamic, ray tracing, geometry, ar, 3d reconstruction  

### SLAM

*Showing the latest 50 out of 144 papers*

- **[GVSynergy-Det: Synergistic Gaussian-Voxel Representations for Multi-View 3D Object Detection](https://arxiv.org/abs/2512.23176v1)**  
  Authors: Yi Zhang, Yi Wang, Lei Yao, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23176v1.pdf)  
  Keywords: gaussian splatting, face, geometry, ar, localization  
- **[Tracking by Predicting 3-D Gaussians Over Time](https://arxiv.org/abs/2512.22489v2)**  
  Authors: Tanish Baranwal, Himanshu Gaurav Singh, Jathushan Rajasegaran, Jitendra Malik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22489v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://videogmae.org/)  
  Keywords: tracking, mapping, dynamic, ar  
- **[Light Field Based 6DoF Tracking of Previously Unobserved Objects](https://arxiv.org/abs/2512.13007v1)**  
  Authors: Nikolai Goncharov, James L. Gray, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13007v1.pdf)  
  Keywords: reflection, robotics, tracking, ar, autonomous driving, semantic  
- **[GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](https://arxiv.org/abs/2512.10939v1)**  
  Authors: Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10939v1.pdf)  
  Keywords: tracking, gaussian splatting, mapping, head, ar, avatar, fast  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: deformation, high-fidelity, gaussian splatting, mapping, face, ar  
- **[Neural Hamiltonian Deformation Fields for Dynamic Scene Rendering](https://arxiv.org/abs/2512.10424v1)**  
  Authors: Hai-Long Qin, Sixian Wang, Guo Lu, Jincheng Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10424v1.pdf)  
  Keywords: deformation, gaussian splatting, motion, mapping, dynamic, ar  
- **[YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos](https://arxiv.org/abs/2512.09903v1)**  
  Authors: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09903v1.pdf)  
  Keywords: human, gaussian splatting, 3d gaussian, mapping, recognition, ar, compact, localization  
- **[GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars](https://arxiv.org/abs/2512.09162v1)**  
  Authors: Kelian Baert, Mae Younes, Francois Bourel, Marc Christie, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09162v1.pdf)  
  Keywords: lighting, gaussian splatting, relightable, relighting, mapping, efficient, head, geometry, ar, avatar  
- **[OpenMonoGS-SLAM: Monocular Gaussian Splatting SLAM with Open-set Semantics](https://arxiv.org/abs/2512.08625v1)**  
  Authors: Jisang Yoo, Gyeongjin Kang, Hyun-kyu Ko, Hyeonwoo Yu, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08625v1.pdf)  
  Keywords: robotics, tracking, slam, gaussian splatting, 3d gaussian, mapping, understanding, geometry, ar, vr, segmentation, localization, semantic  
- **[Tracking-Guided 4D Generation: Foundation-Tracker Motion Priors for 3D Model Animation](https://arxiv.org/abs/2512.06158v1)**  
  Authors: Su Sun, Cheng Zhao, Himangi Mittal, Gaurav Mittal, Rohith Kukkala, Yingjie Victor Chen, Mei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.06158v1.pdf)  
  Keywords: tracking, gaussian splatting, animation, motion, 4d, dynamic, ar  

### Scene Understanding

*Showing the latest 50 out of 207 papers*

- **[UniC-Lift: Unified 3D Instance Segmentation via Contrastive Learning](https://arxiv.org/abs/2512.24763v1)**  
  Authors: Ankit Dhiman, Srinath R, Jaswanth Reddy, Lokesh R Boregowda, Venkatesh Babu Radhakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24763v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, understanding, nerf, ar, segmentation, semantic  
- **[Structure-Guided Allocation of 2D Gaussians for Image Representation and Compression](https://arxiv.org/abs/2512.24018v1)**  
  Authors: Huanxiong Liang, Yunuo Chen, Yicheng Pan, Sixian Wang, Jincheng Dai, Guo Lu, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24018v1.pdf)  
  Keywords: compression, gaussian splatting, geometry, ar, compact, semantic  
- **[Contour Information Aware 2D Gaussian Splatting for Image Representation](https://arxiv.org/abs/2512.23255v1)**  
  Authors: Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai, Zheming Fan, Ryo Ishimoto, Kakeru Sugimoto, Ruri Imichi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23255v1.pdf)  
  Keywords: compression, gaussian splatting, efficient, ar, compact, segmentation, lightweight, fast  
- **[Quantile Rendering: Efficiently Embedding High-dimensional Feature on 3D Gaussian Splatting](https://arxiv.org/abs/2512.20927v1)**  
  Authors: Yoonwoo Jeong, Cheng Sun, Frank Wang, Minsu Cho, Jaesung Choe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20927v1.pdf)  
  Keywords: compression, real-time rendering, gaussian splatting, 3d gaussian, efficient, ar, segmentation  
- **[Geometric-Photometric Event-based 3D Gaussian Ray Tracing](https://arxiv.org/abs/2512.18640v1)**  
  Authors: Kai Kohyama, Yoshimitsu Aoki, Guillermo Gallego, Shintaro Shiba  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18640v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, motion, understanding, ray tracing, geometry, ar, fast, 3d reconstruction  
- **[Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding](https://arxiv.org/abs/2512.17817v2)**  
  Authors: Yue Li, Qi Ma, Runyi Yang, Mengjiao Ma, Bin Ren, Nikola Popovic, Nicu Sebe, Theo Gevers, Luc Van Gool, Danda Pani Paudel, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17817v2.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, efficient, ar, segmentation, semantic  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: human, high-fidelity, lighting, gaussian splatting, relightable, face, geometry, nerf, ar, segmentation, semantic  
- **[Computer vision training dataset generation for robotic environments using Gaussian splatting](https://arxiv.org/abs/2512.13411v1)**  
  Authors: Patryk Niżeniec, Marcin Iwanowski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13411v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, ar, segmentation, shadow  
- **[Light Field Based 6DoF Tracking of Previously Unobserved Objects](https://arxiv.org/abs/2512.13007v1)**  
  Authors: Nikolai Goncharov, James L. Gray, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13007v1.pdf)  
  Keywords: reflection, robotics, tracking, ar, autonomous driving, semantic  
- **[Prior-Enhanced Gaussian Splatting for Dynamic Scene Reconstruction from Casual Video](https://arxiv.org/abs/2512.11356v1)**  
  Authors: Meng-Li Shih, Ying-Huan Chen, Yu-Lun Liu, Brian Curless  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11356v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, geometry, ar, segmentation  



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