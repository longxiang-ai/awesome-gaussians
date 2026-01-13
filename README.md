# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-01-13 00:55:08

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
- [Acceleration](#acceleration) (250 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (345 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (400 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (81 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (357 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (69 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (410 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (202 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (19 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (126 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (149 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (215 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: dynamic, efficient, 3d reconstruction, 3d gaussian, ar, compact, high-fidelity, 4d, compression, survey, gaussian splatting  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v1)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v1.pdf)  
  Keywords: understanding, mapping, ar, 3d gaussian, robotics, localization, semantic, survey, nerf, gaussian splatting, slam  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, high-fidelity, robotics, localization, semantic, survey, mapping, gaussian splatting, slam  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: ar, 3d gaussian, fast, 4d, geometry, motion, survey, nerf, gaussian splatting  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: efficient, real-time rendering, 3d reconstruction, 3d gaussian, ar, efficient rendering, avatar, animation, face, survey, lighting, gaussian splatting  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: understanding, human, efficient, ar, lightweight, survey, nerf, gaussian splatting  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: understanding, efficient, ar, 3d gaussian, fast, neural rendering, survey, nerf, gaussian splatting, slam  
- **[A-TDOM: Active TDOM via On-the-Fly 3DGS](https://arxiv.org/abs/2509.12759v3)**  
  Authors: Yiwei Xu, Xiang Wang, Yifei Yu, Wentian Gan, Luca Morelli, Giulio Perda, Xin Wang, Zongqian Zhan, Fabio Remondino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.12759v3.pdf)  
  Keywords: ar, 3d gaussian, face, survey, gaussian splatting  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977v3)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v3.pdf)  
  Keywords: understanding, efficient, ar, 3d gaussian, segmentation, compact, high-fidelity, semantic, survey, nerf, lighting, gaussian splatting  
- **[A Study of the Framework and Real-World Applications of Language Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: understanding, efficient, ar, 3d gaussian, robotics, semantic, survey, nerf, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 250 papers*

- **[MOSAIC-GS: Monocular Scene Reconstruction via Advanced Initialization for Complex Dynamic Environments](https://arxiv.org/abs/2601.05368v1)**  
  Authors: Svitlana Morkva, Maximum Wilder-Smith, Michael Oechsle, Alessio Tonioni, Marco Hutter, Vaishakh Patil  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05368v1.pdf)  
  Keywords: dynamic, real-time rendering, efficient, ar, fast, compact, high-fidelity, deformation, geometry, motion, tracking, segmentation, gaussian splatting  
- **[ProFuse: Efficient Cross-View Context Fusion for Open-Vocabulary 3D Gaussian Splatting](https://arxiv.org/abs/2601.04754v1)**  
  Authors: Yen-Jen Chiou, Wei-Tse Cheng, Yuan-Fu Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.04754v1.pdf)  
  Keywords: understanding, efficient, ar, 3d gaussian, fast, geometry, head, semantic, gaussian splatting  
- **[A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2601.03200v1)**  
  Authors: Ziyang Sun, Lingfan Bao, Tianhu Peng, Jingcheng Sun, Chengxu Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03200v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, fast, high-fidelity, geometry, motion, semantic, gaussian splatting  
- **[HeadLighter: Disentangling Illumination in Generative 3D Gaussian Heads via Lightstage Captures](https://arxiv.org/abs/2601.02103v1)**  
  Authors: Yating Wang, Yuan Sun, Xuan Wang, Ran Yi, Boyao Zhou, Yipengjing Sun, Hongyu Liu, Yinuo Wang, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02103v1.pdf)  
  Keywords: illumination, ar, real-time rendering, 3d gaussian, head, relighting, lighting, gaussian splatting  
- **[360-GeoGS: Geometrically Consistent Feed-Forward 3D Gaussian Splatting Reconstruction for 360 Images](https://arxiv.org/abs/2601.02102v1)**  
  Authors: Jiaqi Yao, Zhongmiao Yan, Jingyi Xu, Songpengcheng Xia, Yan Xiang, Ling Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02102v1.pdf)  
  Keywords: efficient, ar, 3d reconstruction, 3d gaussian, efficient rendering, face, robotics, sparse view, neural rendering, gaussian splatting  
- **[Animated 3DGS Avatars in Diverse Scenes with Consistent Lighting and Shadows](https://arxiv.org/abs/2601.01660v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Jian Wang, Gerard Pons-Moll, Bing Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.01660v1.pdf)  
  Keywords: illumination, dynamic, ar, 3d gaussian, fast, avatar, shadow, relighting, mapping, lighting, gaussian splatting  
- **[ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2601.00939v1)**  
  Authors: Feng Luo, Hongbo Pan, Xiang Yang, Baoyu Jiang, Fengqing Liu, Tao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00939v1.pdf)  
  Keywords: illumination, efficient, ar, 3d reconstruction, 3d gaussian, efficient rendering, shadow, ray marching, gaussian splatting, sparse-view  
- **[Contour Information Aware 2D Gaussian Splatting for Image Representation](https://arxiv.org/abs/2512.23255v1)**  
  Authors: Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai, Zheming Fan, Ryo Ishimoto, Kakeru Sugimoto, Ruri Imichi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23255v1.pdf)  
  Keywords: efficient, ar, fast, compact, lightweight, compression, segmentation, gaussian splatting  
- **[AirGS: Real-Time 4D Gaussian Streaming for Free-Viewpoint Video Experiences](https://arxiv.org/abs/2512.20943v1)**  
  Authors: Zhe Wang, Jinghang Li, Yifei Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20943v1.pdf)  
  Keywords: dynamic, efficient, ar, 3d gaussian, fast, lightweight, 4d, head, gaussian splatting  
- **[Quantile Rendering: Efficiently Embedding High-dimensional Feature on 3D Gaussian Splatting](https://arxiv.org/abs/2512.20927v1)**  
  Authors: Yoonwoo Jeong, Cheng Sun, Frank Wang, Minsu Cho, Jaesung Choe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20927v1.pdf)  
  Keywords: efficient, real-time rendering, ar, 3d gaussian, compression, segmentation, gaussian splatting  

### Applications

*Showing the latest 50 out of 995 papers*

- **[FeatureSLAM: Feature-enriched 3D gaussian splatting SLAM in real time](https://arxiv.org/abs/2601.05738v1)**  
  Authors: Christopher Thirgood, Oscar Mendez, Erin Ling, Jon Storey, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05738v1.pdf)  
  Keywords: mapping, efficient, ar, tracking, 3d gaussian, semantic, segmentation, gaussian splatting, slam  
- **[GaussianSwap: Animatable Video Face Swapping with 3D Gaussian Splatting](https://arxiv.org/abs/2601.05511v1)**  
  Authors: Xuan Cheng, Jiahao Rao, Chengyang Li, Wenhao Wang, Weilin Chen, Lvqing Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05511v1.pdf)  
  Keywords: recognition, dynamic, ar, 3d gaussian, avatar, high-fidelity, animation, face, segmentation, gaussian splatting  
- **[MOSAIC-GS: Monocular Scene Reconstruction via Advanced Initialization for Complex Dynamic Environments](https://arxiv.org/abs/2601.05368v1)**  
  Authors: Svitlana Morkva, Maximum Wilder-Smith, Michael Oechsle, Alessio Tonioni, Marco Hutter, Vaishakh Patil  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05368v1.pdf)  
  Keywords: dynamic, real-time rendering, efficient, ar, fast, compact, high-fidelity, deformation, geometry, motion, tracking, segmentation, gaussian splatting  
- **[OceanSplat: Object-aware Gaussian Splatting with Trinocular View Consistency for Underwater Scene Reconstruction](https://arxiv.org/abs/2601.04984v1)**  
  Authors: Minseong Kweon, Jinsun Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.04984v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, geometry  
- **[ProFuse: Efficient Cross-View Context Fusion for Open-Vocabulary 3D Gaussian Splatting](https://arxiv.org/abs/2601.04754v1)**  
  Authors: Yen-Jen Chiou, Wei-Tse Cheng, Yuan-Fu Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.04754v1.pdf)  
  Keywords: understanding, efficient, ar, 3d gaussian, fast, geometry, head, semantic, gaussian splatting  
- **[SCAR-GS: Spatial Context Attention for Residuals in Progressive Gaussian Splatting](https://arxiv.org/abs/2601.04348v1)**  
  Authors: Diego Revilla, Pooja Suresh, Anand Bhojan, Ooi Wei Tsang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.04348v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, compression, gaussian splatting  
- **[IDESplat: Iterative Depth Probability Estimation for Generalizable 3D Gaussian Splatting](https://arxiv.org/abs/2601.03824v1)**  
  Authors: Wei Long, Haifeng Wu, Shiyin Jiang, Jinhua Zhang, Xinchun Ji, Shuhang Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03824v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting  
- **[G2P: Gaussian-to-Point Attribute Alignment for Boundary-Aware 3D Semantic Segmentation](https://arxiv.org/abs/2601.03510v1)**  
  Authors: Hojun Song, Chae-yeong Song, Jeong-hun Hong, Chaewon Moon, Dong-hwi Kim, Gahyeon Kim, Soo Ye Kim, Yiyi Liao, Jaehyup Lee, Sang-hyo Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03510v1.pdf)  
  Keywords: understanding, ar, 3d gaussian, geometry, localization, semantic, segmentation, gaussian splatting  
- **[RelightAnyone: A Generalized Relightable 3D Gaussian Head Model](https://arxiv.org/abs/2601.03357v1)**  
  Authors: Yingyan Xu, Pramod Rao, Sebastian Weiss, Gaspard Zoss, Markus Gross, Christian Theobalt, Marc Habermann, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03357v1.pdf)  
  Keywords: illumination, ar, 3d gaussian, relightable, avatar, high quality, head, relighting, mapping, lighting, gaussian splatting  
- **[A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2601.03200v1)**  
  Authors: Ziyang Sun, Lingfan Bao, Tianhu Peng, Jingcheng Sun, Chengxu Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03200v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, fast, high-fidelity, geometry, motion, semantic, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 345 papers*

- **[GaussianSwap: Animatable Video Face Swapping with 3D Gaussian Splatting](https://arxiv.org/abs/2601.05511v1)**  
  Authors: Xuan Cheng, Jiahao Rao, Chengyang Li, Wenhao Wang, Weilin Chen, Lvqing Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05511v1.pdf)  
  Keywords: recognition, dynamic, ar, 3d gaussian, avatar, high-fidelity, animation, face, segmentation, gaussian splatting  
- **[ProFuse: Efficient Cross-View Context Fusion for Open-Vocabulary 3D Gaussian Splatting](https://arxiv.org/abs/2601.04754v1)**  
  Authors: Yen-Jen Chiou, Wei-Tse Cheng, Yuan-Fu Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.04754v1.pdf)  
  Keywords: understanding, efficient, ar, 3d gaussian, fast, geometry, head, semantic, gaussian splatting  
- **[RelightAnyone: A Generalized Relightable 3D Gaussian Head Model](https://arxiv.org/abs/2601.03357v1)**  
  Authors: Yingyan Xu, Pramod Rao, Sebastian Weiss, Gaspard Zoss, Markus Gross, Christian Theobalt, Marc Habermann, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03357v1.pdf)  
  Keywords: illumination, ar, 3d gaussian, relightable, avatar, high quality, head, relighting, mapping, lighting, gaussian splatting  
- **[CaricatureGS: Exaggerating 3D Gaussian Splatting Faces With Gaussian Curvature](https://arxiv.org/abs/2601.03319v1)**  
  Authors: Eldad Matmon, Amit Bracha, Noam Rotstein, Ron Kimmel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03319v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, avatar, deformation, face, geometry, gaussian splatting  
- **[HeadLighter: Disentangling Illumination in Generative 3D Gaussian Heads via Lightstage Captures](https://arxiv.org/abs/2601.02103v1)**  
  Authors: Yating Wang, Yuan Sun, Xuan Wang, Ran Yi, Boyao Zhou, Yipengjing Sun, Hongyu Liu, Yinuo Wang, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02103v1.pdf)  
  Keywords: illumination, ar, real-time rendering, 3d gaussian, head, relighting, lighting, gaussian splatting  
- **[360-GeoGS: Geometrically Consistent Feed-Forward 3D Gaussian Splatting Reconstruction for 360 Images](https://arxiv.org/abs/2601.02102v1)**  
  Authors: Jiaqi Yao, Zhongmiao Yan, Jingyi Xu, Songpengcheng Xia, Yan Xiang, Ling Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02102v1.pdf)  
  Keywords: efficient, ar, 3d reconstruction, 3d gaussian, efficient rendering, face, robotics, sparse view, neural rendering, gaussian splatting  
- **[InpaintHuman: Reconstructing Occluded Humans with Multi-Scale UV Mapping and Identity-Preserving Diffusion Inpainting](https://arxiv.org/abs/2601.02098v1)**  
  Authors: Jinlong Fan, Shanshan Zhao, Liang Zheng, Jing Zhang, Yuxiang Yang, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02098v1.pdf)  
  Keywords: human, ar, 3d gaussian, avatar, high-fidelity, geometry, motion, semantic, mapping, gaussian splatting  
- **[ESGaussianFace: Emotional and Stylized Audio-Driven Facial Animation via 3D Gaussian Splatting](https://arxiv.org/abs/2601.01847v1)**  
  Authors: Chuhang Ma, Shuai Tan, Ye Pan, Jiaolong Yang, Xin Tong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.01847v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, high quality, deformation, animation, face, head, motion, gaussian splatting  
- **[Animated 3DGS Avatars in Diverse Scenes with Consistent Lighting and Shadows](https://arxiv.org/abs/2601.01660v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Jian Wang, Gerard Pons-Moll, Bing Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.01660v1.pdf)  
  Keywords: illumination, dynamic, ar, 3d gaussian, fast, avatar, shadow, relighting, mapping, lighting, gaussian splatting  
- **[PhysTalk: Language-driven Real-time Physics in 3D Gaussian Scenes](https://arxiv.org/abs/2512.24986v1)**  
  Authors: Luca Collorone, Mert Kiray, Indro Spinelli, Fabio Galasso, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24986v1.pdf)  
  Keywords: dynamic, ar, 3d gaussian, lightweight, 4d, animation, face, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 400 papers*

- **[GaussianSwap: Animatable Video Face Swapping with 3D Gaussian Splatting](https://arxiv.org/abs/2601.05511v1)**  
  Authors: Xuan Cheng, Jiahao Rao, Chengyang Li, Wenhao Wang, Weilin Chen, Lvqing Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05511v1.pdf)  
  Keywords: recognition, dynamic, ar, 3d gaussian, avatar, high-fidelity, animation, face, segmentation, gaussian splatting  
- **[MOSAIC-GS: Monocular Scene Reconstruction via Advanced Initialization for Complex Dynamic Environments](https://arxiv.org/abs/2601.05368v1)**  
  Authors: Svitlana Morkva, Maximum Wilder-Smith, Michael Oechsle, Alessio Tonioni, Marco Hutter, Vaishakh Patil  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05368v1.pdf)  
  Keywords: dynamic, real-time rendering, efficient, ar, fast, compact, high-fidelity, deformation, geometry, motion, tracking, segmentation, gaussian splatting  
- **[A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2601.03200v1)**  
  Authors: Ziyang Sun, Lingfan Bao, Tianhu Peng, Jingcheng Sun, Chengxu Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03200v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, fast, high-fidelity, geometry, motion, semantic, gaussian splatting  
- **[CaricatureGS: Exaggerating 3D Gaussian Splatting Faces With Gaussian Curvature](https://arxiv.org/abs/2601.03319v1)**  
  Authors: Eldad Matmon, Amit Bracha, Noam Rotstein, Ron Kimmel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03319v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, avatar, deformation, face, geometry, gaussian splatting  
- **[CAMO: Category-Agnostic 3D Motion Transfer from Monocular 2D Videos](https://arxiv.org/abs/2601.02716v1)**  
  Authors: Taeyeon Kim, Youngju Na, Jumin Lee, Minhyuk Sung, Sung-Eui Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02716v1.pdf)  
  Keywords: ar, 3d gaussian, motion, semantic, gaussian splatting  
- **[InpaintHuman: Reconstructing Occluded Humans with Multi-Scale UV Mapping and Identity-Preserving Diffusion Inpainting](https://arxiv.org/abs/2601.02098v1)**  
  Authors: Jinlong Fan, Shanshan Zhao, Liang Zheng, Jing Zhang, Yuxiang Yang, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02098v1.pdf)  
  Keywords: human, ar, 3d gaussian, avatar, high-fidelity, geometry, motion, semantic, mapping, gaussian splatting  
- **[SketchRodGS: Sketch-based Extraction of Slender Geometries for Animating Gaussian Splatting Scenes](https://arxiv.org/abs/2601.02072v1)**  
  Authors: Haato Watanabe, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02072v1.pdf)  
  Keywords: ar, dynamic, efficient, gaussian splatting  
- **[ESGaussianFace: Emotional and Stylized Audio-Driven Facial Animation via 3D Gaussian Splatting](https://arxiv.org/abs/2601.01847v1)**  
  Authors: Chuhang Ma, Shuai Tan, Ye Pan, Jiaolong Yang, Xin Tong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.01847v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, high quality, deformation, animation, face, head, motion, gaussian splatting  
- **[Animated 3DGS Avatars in Diverse Scenes with Consistent Lighting and Shadows](https://arxiv.org/abs/2601.01660v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Jian Wang, Gerard Pons-Moll, Bing Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.01660v1.pdf)  
  Keywords: illumination, dynamic, ar, 3d gaussian, fast, avatar, shadow, relighting, mapping, lighting, gaussian splatting  
- **[PhysTalk: Language-driven Real-time Physics in 3D Gaussian Scenes](https://arxiv.org/abs/2512.24986v1)**  
  Authors: Luca Collorone, Mert Kiray, Indro Spinelli, Fabio Galasso, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24986v1.pdf)  
  Keywords: dynamic, ar, 3d gaussian, lightweight, 4d, animation, face, gaussian splatting  

### Few-shot

*Showing the latest 50 out of 81 papers*

- **[SA-ResGS: Self-Augmented Residual 3D Gaussian Splatting for Next Best View Selection](https://arxiv.org/abs/2601.03024v1)**  
  Authors: Kim Jun-Seong, Tae-Hyun Oh, Eduardo Pérez-Pellitero, Youngkyoon Jang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03024v1.pdf)  
  Keywords: ar, efficient, 3d gaussian, gaussian splatting, sparse-view  
- **[360-GeoGS: Geometrically Consistent Feed-Forward 3D Gaussian Splatting Reconstruction for 360 Images](https://arxiv.org/abs/2601.02102v1)**  
  Authors: Jiaqi Yao, Zhongmiao Yan, Jingyi Xu, Songpengcheng Xia, Yan Xiang, Ling Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02102v1.pdf)  
  Keywords: efficient, ar, 3d reconstruction, 3d gaussian, efficient rendering, face, robotics, sparse view, neural rendering, gaussian splatting  
- **[ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2601.00939v1)**  
  Authors: Feng Luo, Hongbo Pan, Xiang Yang, Baoyu Jiang, Fengqing Liu, Tao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00939v1.pdf)  
  Keywords: illumination, efficient, ar, 3d reconstruction, 3d gaussian, efficient rendering, shadow, ray marching, gaussian splatting, sparse-view  
- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v2)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: ar, sparse view, 3d reconstruction, 3d gaussian, high-fidelity, motion, gaussian splatting  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: ar, sparse-view, geometry, relighting, segmentation, lighting, gaussian splatting, light transport  
- **[Splatent: Splatting Diffusion Latents for Novel View Synthesis](https://arxiv.org/abs/2512.09923v1)**  
  Authors: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09923v1.pdf)  
  Keywords: efficient, ar, 3d reconstruction, 3d gaussian, efficient rendering, face, gaussian splatting, sparse-view  
- **[Tessellation GS: Neural Mesh Gaussians for Robust Monocular Reconstruction of Dynamic Objects](https://arxiv.org/abs/2512.07381v1)**  
  Authors: Shuohan Tao, Boyao Zhou, Hanzhang Tu, Yuwang Wang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07381v1.pdf)  
  Keywords: dynamic, ar, 3d gaussian, deformation, face, gaussian splatting, sparse-view  
- **[MuSASplat: Efficient Sparse-View 3D Gaussian Splats via Lightweight Multi-Scale Adaptation](https://arxiv.org/abs/2512.07165v1)**  
  Authors: Muyu Xu, Fangneng Zhan, Xiaoqin Zhang, Ling Shao, Shijian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07165v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, lightweight, head, gaussian splatting, sparse-view  
- **[C3G: Learning Compact 3D Representations with 2K Gaussians](https://arxiv.org/abs/2512.04021v1)**  
  Authors: Honggyu An, Jaewoo Jung, Mungyeom Kim, Sunghwan Hong, Chaehyun Kim, Kazumi Fukuda, Minkyeong Jeon, Jisang Han, Takuya Narihira, Hyuna Ko, Junsu Kim, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04021v1.pdf)  
  Keywords: understanding, efficient, ar, 3d gaussian, compact, head, gaussian splatting, segmentation, sparse view  
- **[Cross-Temporal 3D Gaussian Splatting for Sparse-View Guided Scene Update](https://arxiv.org/abs/2512.00534v1)**  
  Authors: Zeyuan An, Yanghang Xiao, Zhiying Leng, Frederick W. B. Li, Xiaohui Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00534v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, gaussian splatting, sparse view, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 357 papers*

- **[MOSAIC-GS: Monocular Scene Reconstruction via Advanced Initialization for Complex Dynamic Environments](https://arxiv.org/abs/2601.05368v1)**  
  Authors: Svitlana Morkva, Maximum Wilder-Smith, Michael Oechsle, Alessio Tonioni, Marco Hutter, Vaishakh Patil  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05368v1.pdf)  
  Keywords: dynamic, real-time rendering, efficient, ar, fast, compact, high-fidelity, deformation, geometry, motion, tracking, segmentation, gaussian splatting  
- **[OceanSplat: Object-aware Gaussian Splatting with Trinocular View Consistency for Underwater Scene Reconstruction](https://arxiv.org/abs/2601.04984v1)**  
  Authors: Minseong Kweon, Jinsun Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.04984v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, geometry  
- **[ProFuse: Efficient Cross-View Context Fusion for Open-Vocabulary 3D Gaussian Splatting](https://arxiv.org/abs/2601.04754v1)**  
  Authors: Yen-Jen Chiou, Wei-Tse Cheng, Yuan-Fu Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.04754v1.pdf)  
  Keywords: understanding, efficient, ar, 3d gaussian, fast, geometry, head, semantic, gaussian splatting  
- **[G2P: Gaussian-to-Point Attribute Alignment for Boundary-Aware 3D Semantic Segmentation](https://arxiv.org/abs/2601.03510v1)**  
  Authors: Hojun Song, Chae-yeong Song, Jeong-hun Hong, Chaewon Moon, Dong-hwi Kim, Gahyeon Kim, Soo Ye Kim, Yiyi Liao, Jaehyup Lee, Sang-hyo Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03510v1.pdf)  
  Keywords: understanding, ar, 3d gaussian, geometry, localization, semantic, segmentation, gaussian splatting  
- **[A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2601.03200v1)**  
  Authors: Ziyang Sun, Lingfan Bao, Tianhu Peng, Jingcheng Sun, Chengxu Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03200v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, fast, high-fidelity, geometry, motion, semantic, gaussian splatting  
- **[CaricatureGS: Exaggerating 3D Gaussian Splatting Faces With Gaussian Curvature](https://arxiv.org/abs/2601.03319v1)**  
  Authors: Eldad Matmon, Amit Bracha, Noam Rotstein, Ron Kimmel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03319v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, avatar, deformation, face, geometry, gaussian splatting  
- **[360-GeoGS: Geometrically Consistent Feed-Forward 3D Gaussian Splatting Reconstruction for 360 Images](https://arxiv.org/abs/2601.02102v1)**  
  Authors: Jiaqi Yao, Zhongmiao Yan, Jingyi Xu, Songpengcheng Xia, Yan Xiang, Ling Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02102v1.pdf)  
  Keywords: efficient, ar, 3d reconstruction, 3d gaussian, efficient rendering, face, robotics, sparse view, neural rendering, gaussian splatting  
- **[InpaintHuman: Reconstructing Occluded Humans with Multi-Scale UV Mapping and Identity-Preserving Diffusion Inpainting](https://arxiv.org/abs/2601.02098v1)**  
  Authors: Jinlong Fan, Shanshan Zhao, Liang Zheng, Jing Zhang, Yuxiang Yang, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02098v1.pdf)  
  Keywords: human, ar, 3d gaussian, avatar, high-fidelity, geometry, motion, semantic, mapping, gaussian splatting  
- **[ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2601.00939v1)**  
  Authors: Feng Luo, Hongbo Pan, Xiang Yang, Baoyu Jiang, Fengqing Liu, Tao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00939v1.pdf)  
  Keywords: illumination, efficient, ar, 3d reconstruction, 3d gaussian, efficient rendering, shadow, ray marching, gaussian splatting, sparse-view  
- **[ParkGaussian: Surround-view 3D Gaussian Splatting for Autonomous Parking](https://arxiv.org/abs/2601.01386v1)**  
  Authors: Xiaobao Wei, Zhangjie Ye, Yuxiang Gu, Zunjie Zhu, Yunfei Guo, Yingying Shen, Shan Zhao, Ming Lu, Haiyang Sun, Bing Wang, Guang Chen, Rongfeng Lu, Hangjun Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.01386v1.pdf)  
  Keywords: ar, 3d reconstruction, 3d gaussian, autonomous driving, geometry, localization, mapping, gaussian splatting  

### Large Scene

*Showing the latest 50 out of 69 papers*

- **[Clean-GS: Semantic Mask-Guided Pruning for 3D Gaussian Splatting](https://arxiv.org/abs/2601.00913v1)**  
  Authors: Subhankar Mishra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00913v1.pdf)  
  Keywords: ar, vr, 3d gaussian, outdoor, compression, semantic, segmentation, gaussian splatting  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: illumination, efficient, ar, 3d reconstruction, 3d gaussian, urban scene, face, geometry, gaussian splatting  
- **[Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries](https://arxiv.org/abs/2512.13796v1)**  
  Authors: Victor Rong, Jan Held, Victor Chu, Daniel Rebain, Marc Van Droogenbroeck, Kiriakos N. Kutulakos, Andrea Tagliasacchi, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13796v1.pdf)  
  Keywords: ar, 3d gaussian, fast, compact, outdoor, geometry, gaussian splatting  
- **[Flux4D: Flow-based Unsupervised 4D Reconstruction](https://arxiv.org/abs/2512.03210v1)**  
  Authors: Jingkang Wang, Henry Che, Yun Chen, Ze Yang, Lily Goli, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03210v1.pdf)  
  Keywords: dynamic, efficient, ar, 3d gaussian, outdoor, 4d, robotics, motion, nerf, gaussian splatting  
- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: understanding, ar, 3d reconstruction, 3d gaussian, outdoor, geometry, gaussian splatting  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: ar, fast, outdoor, geometry, semantic, gaussian splatting  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: illumination, efficient, ar, high-fidelity, outdoor, face, geometry, semantic, relighting, segmentation, lighting, gaussian splatting  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: ar, 3d gaussian, outdoor, high-fidelity, geometry, gaussian splatting  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: human, dynamic, ar, autonomous driving, 4d, urban scene, gaussian splatting  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: ar, 3d gaussian, large scene, fast, head, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 410 papers*

- **[FeatureSLAM: Feature-enriched 3D gaussian splatting SLAM in real time](https://arxiv.org/abs/2601.05738v1)**  
  Authors: Christopher Thirgood, Oscar Mendez, Erin Ling, Jon Storey, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05738v1.pdf)  
  Keywords: mapping, efficient, ar, tracking, 3d gaussian, semantic, segmentation, gaussian splatting, slam  
- **[MOSAIC-GS: Monocular Scene Reconstruction via Advanced Initialization for Complex Dynamic Environments](https://arxiv.org/abs/2601.05368v1)**  
  Authors: Svitlana Morkva, Maximum Wilder-Smith, Michael Oechsle, Alessio Tonioni, Marco Hutter, Vaishakh Patil  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05368v1.pdf)  
  Keywords: dynamic, real-time rendering, efficient, ar, fast, compact, high-fidelity, deformation, geometry, motion, tracking, segmentation, gaussian splatting  
- **[ProFuse: Efficient Cross-View Context Fusion for Open-Vocabulary 3D Gaussian Splatting](https://arxiv.org/abs/2601.04754v1)**  
  Authors: Yen-Jen Chiou, Wei-Tse Cheng, Yuan-Fu Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.04754v1.pdf)  
  Keywords: understanding, efficient, ar, 3d gaussian, fast, geometry, head, semantic, gaussian splatting  
- **[SCAR-GS: Spatial Context Attention for Residuals in Progressive Gaussian Splatting](https://arxiv.org/abs/2601.04348v1)**  
  Authors: Diego Revilla, Pooja Suresh, Anand Bhojan, Ooi Wei Tsang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.04348v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, compression, gaussian splatting  
- **[A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2601.03200v1)**  
  Authors: Ziyang Sun, Lingfan Bao, Tianhu Peng, Jingcheng Sun, Chengxu Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03200v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, fast, high-fidelity, geometry, motion, semantic, gaussian splatting  
- **[SA-ResGS: Self-Augmented Residual 3D Gaussian Splatting for Next Best View Selection](https://arxiv.org/abs/2601.03024v1)**  
  Authors: Kim Jun-Seong, Tae-Hyun Oh, Eduardo Pérez-Pellitero, Youngkyoon Jang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03024v1.pdf)  
  Keywords: ar, efficient, 3d gaussian, gaussian splatting, sparse-view  
- **[CaricatureGS: Exaggerating 3D Gaussian Splatting Faces With Gaussian Curvature](https://arxiv.org/abs/2601.03319v1)**  
  Authors: Eldad Matmon, Amit Bracha, Noam Rotstein, Ron Kimmel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03319v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, avatar, deformation, face, geometry, gaussian splatting  
- **[360-GeoGS: Geometrically Consistent Feed-Forward 3D Gaussian Splatting Reconstruction for 360 Images](https://arxiv.org/abs/2601.02102v1)**  
  Authors: Jiaqi Yao, Zhongmiao Yan, Jingyi Xu, Songpengcheng Xia, Yan Xiang, Ling Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02102v1.pdf)  
  Keywords: efficient, ar, 3d reconstruction, 3d gaussian, efficient rendering, face, robotics, sparse view, neural rendering, gaussian splatting  
- **[SketchRodGS: Sketch-based Extraction of Slender Geometries for Animating Gaussian Splatting Scenes](https://arxiv.org/abs/2601.02072v1)**  
  Authors: Haato Watanabe, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02072v1.pdf)  
  Keywords: ar, dynamic, efficient, gaussian splatting  
- **[ESGaussianFace: Emotional and Stylized Audio-Driven Facial Animation via 3D Gaussian Splatting](https://arxiv.org/abs/2601.01847v1)**  
  Authors: Chuhang Ma, Shuai Tan, Ye Pan, Jiaolong Yang, Xin Tong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.01847v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, high quality, deformation, animation, face, head, motion, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 202 papers*

- **[GaussianSwap: Animatable Video Face Swapping with 3D Gaussian Splatting](https://arxiv.org/abs/2601.05511v1)**  
  Authors: Xuan Cheng, Jiahao Rao, Chengyang Li, Wenhao Wang, Weilin Chen, Lvqing Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05511v1.pdf)  
  Keywords: recognition, dynamic, ar, 3d gaussian, avatar, high-fidelity, animation, face, segmentation, gaussian splatting  
- **[MOSAIC-GS: Monocular Scene Reconstruction via Advanced Initialization for Complex Dynamic Environments](https://arxiv.org/abs/2601.05368v1)**  
  Authors: Svitlana Morkva, Maximum Wilder-Smith, Michael Oechsle, Alessio Tonioni, Marco Hutter, Vaishakh Patil  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05368v1.pdf)  
  Keywords: dynamic, real-time rendering, efficient, ar, fast, compact, high-fidelity, deformation, geometry, motion, tracking, segmentation, gaussian splatting  
- **[SCAR-GS: Spatial Context Attention for Residuals in Progressive Gaussian Splatting](https://arxiv.org/abs/2601.04348v1)**  
  Authors: Diego Revilla, Pooja Suresh, Anand Bhojan, Ooi Wei Tsang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.04348v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, compression, gaussian splatting  
- **[RelightAnyone: A Generalized Relightable 3D Gaussian Head Model](https://arxiv.org/abs/2601.03357v1)**  
  Authors: Yingyan Xu, Pramod Rao, Sebastian Weiss, Gaspard Zoss, Markus Gross, Christian Theobalt, Marc Habermann, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03357v1.pdf)  
  Keywords: illumination, ar, 3d gaussian, relightable, avatar, high quality, head, relighting, mapping, lighting, gaussian splatting  
- **[A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2601.03200v1)**  
  Authors: Ziyang Sun, Lingfan Bao, Tianhu Peng, Jingcheng Sun, Chengxu Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03200v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, fast, high-fidelity, geometry, motion, semantic, gaussian splatting  
- **[InpaintHuman: Reconstructing Occluded Humans with Multi-Scale UV Mapping and Identity-Preserving Diffusion Inpainting](https://arxiv.org/abs/2601.02098v1)**  
  Authors: Jinlong Fan, Shanshan Zhao, Liang Zheng, Jing Zhang, Yuxiang Yang, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02098v1.pdf)  
  Keywords: human, ar, 3d gaussian, avatar, high-fidelity, geometry, motion, semantic, mapping, gaussian splatting  
- **[ESGaussianFace: Emotional and Stylized Audio-Driven Facial Animation via 3D Gaussian Splatting](https://arxiv.org/abs/2601.01847v1)**  
  Authors: Chuhang Ma, Shuai Tan, Ye Pan, Jiaolong Yang, Xin Tong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.01847v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, high quality, deformation, animation, face, head, motion, gaussian splatting  
- **[SCPainter: A Unified Framework for Realistic 3D Asset Insertion and Novel View Synthesis](https://arxiv.org/abs/2512.22706v1)**  
  Authors: Paul Dobre, Jackson Cooper, Xin Wang, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22706v1.pdf)  
  Keywords: dynamic, ar, 3d gaussian, high quality, autonomous driving, shadow, lighting  
- **[Nebula: Enable City-Scale 3D Gaussian Splatting in Virtual Reality via Collaborative Rendering and Accelerated Stereo Rasterization](https://arxiv.org/abs/2512.20495v1)**  
  Authors: He Zhu, Zheng Liu, Xingyang Li, Anbang Wu, Jieru Zhao, Fangxin Liu, Yiming Gan, Jingwen Leng, Yu Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.20495v1.pdf)  
  Keywords: ar, vr, 3d gaussian, high-fidelity, acceleration, motion, gaussian splatting  
- **[Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding](https://arxiv.org/abs/2512.17817v2)**  
  Authors: Yue Li, Qi Ma, Runyi Yang, Mengjiao Ma, Bin Ren, Nikola Popovic, Nicu Sebe, Theo Gevers, Luc Van Gool, Danda Pani Paudel, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17817v2.pdf)  
  Keywords: efficient, ar, 3d gaussian, high-fidelity, semantic, segmentation, gaussian splatting  

### Ray Tracing

- **[ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2601.00939v1)**  
  Authors: Feng Luo, Hongbo Pan, Xiang Yang, Baoyu Jiang, Fengqing Liu, Tao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00939v1.pdf)  
  Keywords: illumination, efficient, ar, 3d reconstruction, 3d gaussian, efficient rendering, shadow, ray marching, gaussian splatting, sparse-view  
- **[Geometric-Photometric Event-based 3D Gaussian Ray Tracing](https://arxiv.org/abs/2512.18640v1)**  
  Authors: Kai Kohyama, Yoshimitsu Aoki, Guillermo Gallego, Shintaro Shiba  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18640v1.pdf)  
  Keywords: understanding, ar, 3d reconstruction, 3d gaussian, fast, ray tracing, geometry, motion, gaussian splatting  
- **[MatSpray: Fusing 2D Material World Knowledge on 3D Geometry](https://arxiv.org/abs/2512.18314v1)**  
  Authors: Philipp Langsteiner, Jan-Niklas Dihlmann, Hendrik P. A. Lensch  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18314v1.pdf)  
  Keywords: ar, 3d reconstruction, relightable, ray tracing, geometry, relighting, lighting, gaussian splatting  
- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: ar, 3d gaussian, fast, ray tracing, face, nerf, gaussian splatting  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: ar, real-time rendering, 3d gaussian, fast, compact, high-fidelity, ray tracing, gaussian splatting  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: dynamic, ar, reflection, 3d reconstruction, high-fidelity, ray tracing, geometry, gaussian splatting  
- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: illumination, ar, reflection, ray tracing, geometry, gaussian splatting  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: efficient, ar, 3d gaussian, ray marching, geometry, gaussian splatting  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: efficient, real-time rendering, ar, relightable, shadow, ray tracing, face, lighting, gaussian splatting, light transport  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: illumination, efficient, ar, reflection, lighting, geometry, relighting, global illumination, gaussian splatting, light transport  

### Relighting

*Showing the latest 50 out of 126 papers*

- **[RelightAnyone: A Generalized Relightable 3D Gaussian Head Model](https://arxiv.org/abs/2601.03357v1)**  
  Authors: Yingyan Xu, Pramod Rao, Sebastian Weiss, Gaspard Zoss, Markus Gross, Christian Theobalt, Marc Habermann, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03357v1.pdf)  
  Keywords: illumination, ar, 3d gaussian, relightable, avatar, high quality, head, relighting, mapping, lighting, gaussian splatting  
- **[HeadLighter: Disentangling Illumination in Generative 3D Gaussian Heads via Lightstage Captures](https://arxiv.org/abs/2601.02103v1)**  
  Authors: Yating Wang, Yuan Sun, Xuan Wang, Ran Yi, Boyao Zhou, Yipengjing Sun, Hongyu Liu, Yinuo Wang, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02103v1.pdf)  
  Keywords: illumination, ar, real-time rendering, 3d gaussian, head, relighting, lighting, gaussian splatting  
- **[Animated 3DGS Avatars in Diverse Scenes with Consistent Lighting and Shadows](https://arxiv.org/abs/2601.01660v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Jian Wang, Gerard Pons-Moll, Bing Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.01660v1.pdf)  
  Keywords: illumination, dynamic, ar, 3d gaussian, fast, avatar, shadow, relighting, mapping, lighting, gaussian splatting  
- **[ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2601.00939v1)**  
  Authors: Feng Luo, Hongbo Pan, Xiang Yang, Baoyu Jiang, Fengqing Liu, Tao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00939v1.pdf)  
  Keywords: illumination, efficient, ar, 3d reconstruction, 3d gaussian, efficient rendering, shadow, ray marching, gaussian splatting, sparse-view  
- **[Improved 3D Gaussian Splatting of Unknown Spacecraft Structure Using Space Environment Illumination Knowledge](https://arxiv.org/abs/2512.23998v1)**  
  Authors: Tae Ha Park, Simone D'Amico  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23998v1.pdf)  
  Keywords: illumination, dynamic, ar, 3d gaussian, shadow, geometry, lighting, gaussian splatting  
- **[SCPainter: A Unified Framework for Realistic 3D Asset Insertion and Novel View Synthesis](https://arxiv.org/abs/2512.22706v1)**  
  Authors: Paul Dobre, Jackson Cooper, Xin Wang, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22706v1.pdf)  
  Keywords: dynamic, ar, 3d gaussian, high quality, autonomous driving, shadow, lighting  
- **[MatSpray: Fusing 2D Material World Knowledge on 3D Geometry](https://arxiv.org/abs/2512.18314v1)**  
  Authors: Philipp Langsteiner, Jan-Niklas Dihlmann, Hendrik P. A. Lensch  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18314v1.pdf)  
  Keywords: ar, 3d reconstruction, relightable, ray tracing, geometry, relighting, lighting, gaussian splatting  
- **[Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation](https://arxiv.org/abs/2512.17349v1)**  
  Authors: Xijie Huang, Jinhan Li, Tianyue Wu, Xin Zhou, Zhichao Han, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17349v1.pdf)  
  Keywords: illumination, ar, 3d gaussian, high-fidelity, gaussian splatting  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: human, ar, segmentation, relightable, high-fidelity, face, geometry, semantic, nerf, lighting, gaussian splatting  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: illumination, efficient, ar, 3d reconstruction, 3d gaussian, urban scene, face, geometry, gaussian splatting  

### SLAM

*Showing the latest 50 out of 149 papers*

- **[FeatureSLAM: Feature-enriched 3D gaussian splatting SLAM in real time](https://arxiv.org/abs/2601.05738v1)**  
  Authors: Christopher Thirgood, Oscar Mendez, Erin Ling, Jon Storey, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05738v1.pdf)  
  Keywords: mapping, efficient, ar, tracking, 3d gaussian, semantic, segmentation, gaussian splatting, slam  
- **[MOSAIC-GS: Monocular Scene Reconstruction via Advanced Initialization for Complex Dynamic Environments](https://arxiv.org/abs/2601.05368v1)**  
  Authors: Svitlana Morkva, Maximum Wilder-Smith, Michael Oechsle, Alessio Tonioni, Marco Hutter, Vaishakh Patil  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05368v1.pdf)  
  Keywords: dynamic, real-time rendering, efficient, ar, fast, compact, high-fidelity, deformation, geometry, motion, tracking, segmentation, gaussian splatting  
- **[G2P: Gaussian-to-Point Attribute Alignment for Boundary-Aware 3D Semantic Segmentation](https://arxiv.org/abs/2601.03510v1)**  
  Authors: Hojun Song, Chae-yeong Song, Jeong-hun Hong, Chaewon Moon, Dong-hwi Kim, Gahyeon Kim, Soo Ye Kim, Yiyi Liao, Jaehyup Lee, Sang-hyo Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03510v1.pdf)  
  Keywords: understanding, ar, 3d gaussian, geometry, localization, semantic, segmentation, gaussian splatting  
- **[RelightAnyone: A Generalized Relightable 3D Gaussian Head Model](https://arxiv.org/abs/2601.03357v1)**  
  Authors: Yingyan Xu, Pramod Rao, Sebastian Weiss, Gaspard Zoss, Markus Gross, Christian Theobalt, Marc Habermann, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03357v1.pdf)  
  Keywords: illumination, ar, 3d gaussian, relightable, avatar, high quality, head, relighting, mapping, lighting, gaussian splatting  
- **[InpaintHuman: Reconstructing Occluded Humans with Multi-Scale UV Mapping and Identity-Preserving Diffusion Inpainting](https://arxiv.org/abs/2601.02098v1)**  
  Authors: Jinlong Fan, Shanshan Zhao, Liang Zheng, Jing Zhang, Yuxiang Yang, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02098v1.pdf)  
  Keywords: human, ar, 3d gaussian, avatar, high-fidelity, geometry, motion, semantic, mapping, gaussian splatting  
- **[Animated 3DGS Avatars in Diverse Scenes with Consistent Lighting and Shadows](https://arxiv.org/abs/2601.01660v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Jian Wang, Gerard Pons-Moll, Bing Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.01660v1.pdf)  
  Keywords: illumination, dynamic, ar, 3d gaussian, fast, avatar, shadow, relighting, mapping, lighting, gaussian splatting  
- **[ParkGaussian: Surround-view 3D Gaussian Splatting for Autonomous Parking](https://arxiv.org/abs/2601.01386v1)**  
  Authors: Xiaobao Wei, Zhangjie Ye, Yuxiang Gu, Zunjie Zhu, Yunfei Guo, Yingying Shen, Shan Zhao, Ming Lu, Haiyang Sun, Bing Wang, Guang Chen, Rongfeng Lu, Hangjun Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.01386v1.pdf)  
  Keywords: ar, 3d reconstruction, 3d gaussian, autonomous driving, geometry, localization, mapping, gaussian splatting  
- **[GVSynergy-Det: Synergistic Gaussian-Voxel Representations for Multi-View 3D Object Detection](https://arxiv.org/abs/2512.23176v1)**  
  Authors: Yi Zhang, Yi Wang, Lei Yao, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23176v1.pdf)  
  Keywords: ar, face, geometry, localization, gaussian splatting  
- **[RGS-SLAM: Robust Gaussian Splatting SLAM with One-Shot Dense Initialization](https://arxiv.org/abs/2601.00705v1)**  
  Authors: Wei-Tse Cheng, Yen-Jen Chiou, Yuan-Fu Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00705v1.pdf)  
  Keywords: ar, geometry, localization, mapping, gaussian splatting, slam  
- **[Tracking by Predicting 3-D Gaussians Over Time](https://arxiv.org/abs/2512.22489v2)**  
  Authors: Tanish Baranwal, Himanshu Gaurav Singh, Jathushan Rajasegaran, Jitendra Malik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22489v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://videogmae.org/)  
  Keywords: ar, tracking, dynamic, mapping  

### Scene Understanding

*Showing the latest 50 out of 215 papers*

- **[FeatureSLAM: Feature-enriched 3D gaussian splatting SLAM in real time](https://arxiv.org/abs/2601.05738v1)**  
  Authors: Christopher Thirgood, Oscar Mendez, Erin Ling, Jon Storey, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05738v1.pdf)  
  Keywords: mapping, efficient, ar, tracking, 3d gaussian, semantic, segmentation, gaussian splatting, slam  
- **[GaussianSwap: Animatable Video Face Swapping with 3D Gaussian Splatting](https://arxiv.org/abs/2601.05511v1)**  
  Authors: Xuan Cheng, Jiahao Rao, Chengyang Li, Wenhao Wang, Weilin Chen, Lvqing Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05511v1.pdf)  
  Keywords: recognition, dynamic, ar, 3d gaussian, avatar, high-fidelity, animation, face, segmentation, gaussian splatting  
- **[MOSAIC-GS: Monocular Scene Reconstruction via Advanced Initialization for Complex Dynamic Environments](https://arxiv.org/abs/2601.05368v1)**  
  Authors: Svitlana Morkva, Maximum Wilder-Smith, Michael Oechsle, Alessio Tonioni, Marco Hutter, Vaishakh Patil  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05368v1.pdf)  
  Keywords: dynamic, real-time rendering, efficient, ar, fast, compact, high-fidelity, deformation, geometry, motion, tracking, segmentation, gaussian splatting  
- **[ProFuse: Efficient Cross-View Context Fusion for Open-Vocabulary 3D Gaussian Splatting](https://arxiv.org/abs/2601.04754v1)**  
  Authors: Yen-Jen Chiou, Wei-Tse Cheng, Yuan-Fu Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.04754v1.pdf)  
  Keywords: understanding, efficient, ar, 3d gaussian, fast, geometry, head, semantic, gaussian splatting  
- **[G2P: Gaussian-to-Point Attribute Alignment for Boundary-Aware 3D Semantic Segmentation](https://arxiv.org/abs/2601.03510v1)**  
  Authors: Hojun Song, Chae-yeong Song, Jeong-hun Hong, Chaewon Moon, Dong-hwi Kim, Gahyeon Kim, Soo Ye Kim, Yiyi Liao, Jaehyup Lee, Sang-hyo Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03510v1.pdf)  
  Keywords: understanding, ar, 3d gaussian, geometry, localization, semantic, segmentation, gaussian splatting  
- **[A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2601.03200v1)**  
  Authors: Ziyang Sun, Lingfan Bao, Tianhu Peng, Jingcheng Sun, Chengxu Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03200v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, fast, high-fidelity, geometry, motion, semantic, gaussian splatting  
- **[CAMO: Category-Agnostic 3D Motion Transfer from Monocular 2D Videos](https://arxiv.org/abs/2601.02716v1)**  
  Authors: Taeyeon Kim, Youngju Na, Jumin Lee, Minhyuk Sung, Sung-Eui Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02716v1.pdf)  
  Keywords: ar, 3d gaussian, motion, semantic, gaussian splatting  
- **[InpaintHuman: Reconstructing Occluded Humans with Multi-Scale UV Mapping and Identity-Preserving Diffusion Inpainting](https://arxiv.org/abs/2601.02098v1)**  
  Authors: Jinlong Fan, Shanshan Zhao, Liang Zheng, Jing Zhang, Yuxiang Yang, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02098v1.pdf)  
  Keywords: human, ar, 3d gaussian, avatar, high-fidelity, geometry, motion, semantic, mapping, gaussian splatting  
- **[Clean-GS: Semantic Mask-Guided Pruning for 3D Gaussian Splatting](https://arxiv.org/abs/2601.00913v1)**  
  Authors: Subhankar Mishra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00913v1.pdf)  
  Keywords: ar, vr, 3d gaussian, outdoor, compression, semantic, segmentation, gaussian splatting  
- **[UniC-Lift: Unified 3D Instance Segmentation via Contrastive Learning](https://arxiv.org/abs/2512.24763v1)**  
  Authors: Ankit Dhiman, Srinath R, Jaswanth Reddy, Lokesh R Boregowda, Venkatesh Babu Radhakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.24763v1.pdf)  
  Keywords: understanding, efficient, ar, 3d gaussian, segmentation, semantic, nerf, gaussian splatting  



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