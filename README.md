# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-02-10 01:23:02

## 📰 Latest Updates

🚀 **[2026-02] Major Feature Update — v2.0**
- **Unified CLI**: Single entry point `python main.py` with subcommands: `init`, `search`, `suggest`, `export-bib`, `readme`
- **Interactive Configuration Wizard**: Run `python main.py init` to set up keywords, domains, time range, and API keys step-by-step
- **Custom Time Range Filtering**: Support relative periods (`6m`, `1y`, `2y`) and absolute date ranges (`2024-01-01` to `2025-06-01`)
- **Smart Link Extraction**: Automatically extracts and classifies GitHub, project page, dataset, video, demo, and HuggingFace links from paper abstracts
- **BibTeX Export**: Fetch BibTeX from arXiv and export to `.bib` files with category/date filters
- **LLM Keyword Suggestion**: Paste a few paper titles or arXiv IDs, and an LLM automatically generates optimized search keywords
- **arXiv Domain Filtering**: Restrict searches to specific arXiv categories (e.g., `cs.CV`, `cs.GR`)

🔧 **[2025-06-26] HTTP 301 Redirect Issue Completely Resolved!** 
- Implemented multi-layer fallback strategy to thoroughly solve network compatibility issues

🔧 **[2025-06-26] Configurable Search Keywords Feature Added!**
- You can now customize search keywords by modifying `data/search_config.json`

- View detailed updates: [News.md](News.md) 📋

---

## Categories

- [3DGS Surveys](#3dgs-surveys) (8 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (104 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (499 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (173 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (210 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (33 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (190 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (19 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (205 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (125 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (12 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (68 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (73 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (119 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: mapping, dynamic, ar, efficient, tracking, face, survey, motion, 3d gaussian, slam, gaussian splatting, localization  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: ar, robotics, survey, 3d gaussian, gaussian splatting  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v2)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v2.pdf)  
  Keywords: ar, efficient, nerf, geometry, survey, 3d gaussian, gaussian splatting  
- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197v1)**  
  Authors: Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07197v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, efficient, survey, 3d reconstruction, 3d gaussian, compression, compact, gaussian splatting  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v2)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v2.pdf)  
  Keywords: localization, ar, robotics, nerf, survey, slam, mapping, 3d gaussian, understanding, gaussian splatting, semantic  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: high-fidelity, localization, ar, efficient, robotics, survey, mapping, 3d gaussian, slam, gaussian splatting, semantic  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI)  
  Keywords: ar, 4d, nerf, geometry, survey, motion, 3d gaussian, fast, gaussian splatting  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: ar, animation, efficient, lighting, efficient rendering, face, survey, 3d reconstruction, real-time rendering, avatar, 3d gaussian, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 104 papers*

- **[Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction For 3D-Aware Distillation](https://arxiv.org/abs/2602.06032v1)**  
  Authors: David Shavin, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06032v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://davidshavin4.github.io/Splat-and-Distill)  
  Keywords: dynamic, ar, face, 3d reconstruction, segmentation, 3d gaussian, fast, semantic  
- **[PoseGaussian: Pose-Driven Novel View Synthesis for Robust 3D Human Reconstruction](https://arxiv.org/abs/2602.05190v1)**  
  Authors: Ju Shen, Chen Chen, Tam V. Nguyen, Vijayan K. Asari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05190v1.pdf)  
  Keywords: high-fidelity, human, body, dynamic, ar, real-time rendering, motion, gaussian splatting  
- **[QuantumGS: Quantum Encoding Framework for Gaussian Splatting](https://arxiv.org/abs/2602.05047v1)**  
  Authors: Grzegorz Wilczyński, Rafał Tobiasz, Paweł Gora, Marcin Mazur, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05047v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/QuantumGS?style=social)](https://github.com/gwilczynski95/QuantumGS)  
  Keywords: ar, neural rendering, reflection, geometry, real-time rendering, 3d gaussian, gaussian splatting  
- **[JOintGS: Joint Optimization of Cameras, Bodies and 3D Gaussians for In-the-Wild Monocular Reconstruction](https://arxiv.org/abs/2602.04317v1)**  
  Authors: Zihan Lou, Jinlong Fan, Sihan Ma, Yuxiang Yang, Jing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04317v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MiliLab/JOintGS?style=social)](https://github.com/MiliLab/JOintGS)  
  Keywords: high-fidelity, human, body, dynamic, ar, illumination, real-time rendering, avatar, deformation, 3d gaussian  
- **[Pi-GS: Sparse-View Gaussian Splatting with Dense π^3 Initialization](https://arxiv.org/abs/2602.03327v1)**  
  Authors: Manuel Hofer, Markus Steinberger, Thomas Köhler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03327v1.pdf)  
  Keywords: ar, nerf, sparse-view, real-time rendering, motion, 3d gaussian, gaussian splatting  
- **[SharpTimeGS: Sharp and Stable Dynamic Gaussian Splatting via Lifespan Modulation](https://arxiv.org/abs/2602.02989v2)**  
  Authors: Zhanfeng Liao, Jiajun Zhang, Hanzhang Tu, Zhixi Wang, Yunqi Gao, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02989v2.pdf)  
  Keywords: dynamic, ar, 4d, real-time rendering, motion, compact, gaussian splatting  
- **[UrbanGS: A Scalable and Efficient Architecture for Geometrically Accurate Large-Scene Reconstruction](https://arxiv.org/abs/2602.02089v1)**  
  Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Xiuping Liang, Tongfei Chen, Shuwei Shao, Linlin Yang, Huobin Tan, Baochang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02089v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, efficient, real-time rendering, 3d gaussian, gaussian splatting  
- **[FastPhysGS: Accelerating Physics-based Dynamic 3DGS Simulation via Interior Completion and Adaptive Optimization](https://arxiv.org/abs/2602.01723v1)**  
  Authors: Yikun Ma, Yiqing Li, Jingwen Ye, Zhongkai Wu, Weidong Zhang, Lin Gao, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01723v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, efficient, face, motion, 3d gaussian, fast, gaussian splatting  
- **[Split&Splat: Zero-Shot Panoptic Segmentation via Explicit Instance Modeling and 3D Gaussian Splatting](https://arxiv.org/abs/2602.03809v1)**  
  Authors: Leonardo Monchieri, Elena Camuffo, Francesco Barbato, Pietro Zanuttigh, Simone Milani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03809v1.pdf)  
  Keywords: ar, segmentation, 3d gaussian, fast, gaussian splatting, semantic  
- **[PLANING: A Loosely Coupled Triangle-Gaussian Framework for Streaming 3D Reconstruction](https://arxiv.org/abs/2601.22046v2)**  
  Authors: Changjian Jiang, Kerui Ren, Xudong Li, Kaiwen Song, Linning Xu, Tao Lu, Junting Dong, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22046v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://city-super.github.io/PLANING)  
  Keywords: ar, efficient, geometry, 3d reconstruction, fast, gaussian splatting  

### Applications

*Showing the latest 50 out of 499 papers*

- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2602.06846v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06846v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, vr, reflection, geometry, head, motion, 3d gaussian, gaussian splatting, semantic  
- **[GaussianPOP: Principled Simplification Framework for Compact 3D Gaussian Splatting via Error Quantification](https://arxiv.org/abs/2602.06830v1)**  
  Authors: Soonbin Lee, Yeong-Gyu Kim, Simon Sasse, Tomas M. Borges, Yago Sanchez, Eun-Seok Ryu, Thomas Schierl, Cornelius Hellge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06830v1.pdf)  
  Keywords: ar, efficient, 3d gaussian, compact, gaussian splatting  
- **[TFusionOcc: Student's t-Distribution Based Object-Centric Multi-Sensor Fusion Framework for 3D Occupancy Prediction](https://arxiv.org/abs/2602.06400v1)**  
  Authors: Zhenxing Ming, Julie Stephany Berrio, Mao Shan, Stewart Worrall  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06400v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DanielMing123/TFusionOcc?style=social)](https://github.com/DanielMing123/TFusionOcc)  
  Keywords: efficient, 3d gaussian, ar, semantic  
- **[Uncertainty-Aware 4D Gaussian Splatting for Monocular Occluded Human Rendering](https://arxiv.org/abs/2602.06343v1)**  
  Authors: Weiquan Wang, Feifei Shao, Lin Li, Zhen Wang, Jun Xiao, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06343v1.pdf)  
  Keywords: high-fidelity, human, dynamic, ar, 4d, motion, deformation, gaussian splatting  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, animation, geometry, face, 3d reconstruction, avatar, head, motion, 3d gaussian, gaussian splatting  
- **[Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction For 3D-Aware Distillation](https://arxiv.org/abs/2602.06032v1)**  
  Authors: David Shavin, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06032v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://davidshavin4.github.io/Splat-and-Distill)  
  Keywords: dynamic, ar, face, 3d reconstruction, segmentation, 3d gaussian, fast, semantic  
- **[NVS-HO: A Benchmark for Novel View Synthesis of Handheld Objects](https://arxiv.org/abs/2602.05822v1)**  
  Authors: Musawar Ali, Manuel Carranza-García, Nicola Fioraio, Samuele Salti, Luigi Di Stefano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05822v1.pdf)  
  Keywords: lighting, nerf, ar, gaussian splatting  
- **[Unified Sensor Simulation for Autonomous Driving](https://arxiv.org/abs/2602.05617v1)**  
  Authors: Nikolay Patakin, Arsenii Shirokov, Anton Konushin, Dmitry Senushkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05617v1.pdf) | [![GitHub](https://img.shields.io/github/stars/whesense/XSIM?style=social)](https://github.com/whesense/XSIM)  
  Keywords: ar, dynamic, geometry, autonomous driving, 3d gaussian  
- **[PoseGaussian: Pose-Driven Novel View Synthesis for Robust 3D Human Reconstruction](https://arxiv.org/abs/2602.05190v1)**  
  Authors: Ju Shen, Chen Chen, Tam V. Nguyen, Vijayan K. Asari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05190v1.pdf)  
  Keywords: high-fidelity, human, body, dynamic, ar, real-time rendering, motion, gaussian splatting  
- **[QuantumGS: Quantum Encoding Framework for Gaussian Splatting](https://arxiv.org/abs/2602.05047v1)**  
  Authors: Grzegorz Wilczyński, Rafał Tobiasz, Paweł Gora, Marcin Mazur, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05047v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/QuantumGS?style=social)](https://github.com/gwilczynski95/QuantumGS)  
  Keywords: ar, neural rendering, reflection, geometry, real-time rendering, 3d gaussian, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 173 papers*

- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2602.06846v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06846v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, vr, reflection, geometry, head, motion, 3d gaussian, gaussian splatting, semantic  
- **[Uncertainty-Aware 4D Gaussian Splatting for Monocular Occluded Human Rendering](https://arxiv.org/abs/2602.06343v1)**  
  Authors: Weiquan Wang, Feifei Shao, Lin Li, Zhen Wang, Jun Xiao, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06343v1.pdf)  
  Keywords: high-fidelity, human, dynamic, ar, 4d, motion, deformation, gaussian splatting  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, animation, geometry, face, 3d reconstruction, avatar, head, motion, 3d gaussian, gaussian splatting  
- **[Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction For 3D-Aware Distillation](https://arxiv.org/abs/2602.06032v1)**  
  Authors: David Shavin, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06032v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://davidshavin4.github.io/Splat-and-Distill)  
  Keywords: dynamic, ar, face, 3d reconstruction, segmentation, 3d gaussian, fast, semantic  
- **[PoseGaussian: Pose-Driven Novel View Synthesis for Robust 3D Human Reconstruction](https://arxiv.org/abs/2602.05190v1)**  
  Authors: Ju Shen, Chen Chen, Tam V. Nguyen, Vijayan K. Asari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05190v1.pdf)  
  Keywords: high-fidelity, human, body, dynamic, ar, real-time rendering, motion, gaussian splatting  
- **[JOintGS: Joint Optimization of Cameras, Bodies and 3D Gaussians for In-the-Wild Monocular Reconstruction](https://arxiv.org/abs/2602.04317v1)**  
  Authors: Zihan Lou, Jinlong Fan, Sihan Ma, Yuxiang Yang, Jing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04317v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MiliLab/JOintGS?style=social)](https://github.com/MiliLab/JOintGS)  
  Keywords: high-fidelity, human, body, dynamic, ar, illumination, real-time rendering, avatar, deformation, 3d gaussian  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: mapping, dynamic, ar, efficient, tracking, face, survey, motion, 3d gaussian, slam, gaussian splatting, localization  
- **[SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-body Manipulation](https://arxiv.org/abs/2602.02402v1)**  
  Authors: Mu Huang, Hui Wang, Kerui Ren, Linning Xu, Yunsong Zhou, Mulin Yu, Bo Dai, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02402v1.pdf)  
  Keywords: body, 3d gaussian, ar, dynamic  
- **[SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors](https://arxiv.org/abs/2602.02000v2)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Ning Cao, Gang Chen, Zhengxue Cheng, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02000v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hebing-sjtu.github.io/SurfSplat-website)  
  Keywords: high-fidelity, ar, geometry, face, 3d reconstruction, 3d gaussian, gaussian splatting  
- **[OFERA: Blendshape-driven 3D Gaussian Control for Occluded Facial Expression to Realistic Avatars in VR](https://arxiv.org/abs/2602.01748v1)**  
  Authors: Seokhwan Yang, Boram Yoon, Seoyoung Kang, Hail Song, Woontack Woo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01748v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ysshwan147.github.io/projects/ofera)  
  Keywords: mapping, ar, vr, head, avatar, 3d gaussian  

### Dynamic Scene

*Showing the latest 50 out of 210 papers*

- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2602.06846v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06846v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, vr, reflection, geometry, head, motion, 3d gaussian, gaussian splatting, semantic  
- **[Uncertainty-Aware 4D Gaussian Splatting for Monocular Occluded Human Rendering](https://arxiv.org/abs/2602.06343v1)**  
  Authors: Weiquan Wang, Feifei Shao, Lin Li, Zhen Wang, Jun Xiao, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06343v1.pdf)  
  Keywords: high-fidelity, human, dynamic, ar, 4d, motion, deformation, gaussian splatting  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, animation, geometry, face, 3d reconstruction, avatar, head, motion, 3d gaussian, gaussian splatting  
- **[Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction For 3D-Aware Distillation](https://arxiv.org/abs/2602.06032v1)**  
  Authors: David Shavin, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06032v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://davidshavin4.github.io/Splat-and-Distill)  
  Keywords: dynamic, ar, face, 3d reconstruction, segmentation, 3d gaussian, fast, semantic  
- **[Unified Sensor Simulation for Autonomous Driving](https://arxiv.org/abs/2602.05617v1)**  
  Authors: Nikolay Patakin, Arsenii Shirokov, Anton Konushin, Dmitry Senushkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05617v1.pdf) | [![GitHub](https://img.shields.io/github/stars/whesense/XSIM?style=social)](https://github.com/whesense/XSIM)  
  Keywords: ar, dynamic, geometry, autonomous driving, 3d gaussian  
- **[PoseGaussian: Pose-Driven Novel View Synthesis for Robust 3D Human Reconstruction](https://arxiv.org/abs/2602.05190v1)**  
  Authors: Ju Shen, Chen Chen, Tam V. Nguyen, Vijayan K. Asari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05190v1.pdf)  
  Keywords: high-fidelity, human, body, dynamic, ar, real-time rendering, motion, gaussian splatting  
- **[JOintGS: Joint Optimization of Cameras, Bodies and 3D Gaussians for In-the-Wild Monocular Reconstruction](https://arxiv.org/abs/2602.04317v1)**  
  Authors: Zihan Lou, Jinlong Fan, Sihan Ma, Yuxiang Yang, Jing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04317v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MiliLab/JOintGS?style=social)](https://github.com/MiliLab/JOintGS)  
  Keywords: high-fidelity, human, body, dynamic, ar, illumination, real-time rendering, avatar, deformation, 3d gaussian  
- **[SkeletonGaussian: Editable 4D Generation through Gaussian Skeletonization](https://arxiv.org/abs/2602.04271v1)**  
  Authors: Lifan Wu, Ruijie Zhu, Yubo Ai, Tianzhu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04271v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wusar.github.io/projects/skeletongaussian)  
  Keywords: dynamic, ar, 4d, motion, deformation, 3d gaussian  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: mapping, dynamic, ar, efficient, tracking, face, survey, motion, 3d gaussian, slam, gaussian splatting, localization  
- **[Constrained Dynamic Gaussian Splatting](https://arxiv.org/abs/2602.03538v1)**  
  Authors: Zihan Zheng, Zhenglong Wu, Xuanxuan Wang, Houqiang Zhong, Xiaoyun Zhang, Qiang Hu, Guangtao Zhai, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03538v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, motion, compression, gaussian splatting  

### Few-shot

- **[Pi-GS: Sparse-View Gaussian Splatting with Dense π^3 Initialization](https://arxiv.org/abs/2602.03327v1)**  
  Authors: Manuel Hofer, Markus Steinberger, Thomas Köhler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03327v1.pdf)  
  Keywords: ar, nerf, sparse-view, real-time rendering, motion, 3d gaussian, gaussian splatting  
- **[LoD-Structured 3D Gaussian Splatting for Streaming Video Reconstruction](https://arxiv.org/abs/2601.18475v1)**  
  Authors: Xinhui Liu, Can Wang, Lei Liu, Zhenghao Chen, Wei Jiang, Wei Wang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18475v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, efficient, sparse-view, motion, 3d gaussian, gaussian splatting  
- **[LGDWT-GS: Local and Global Discrete Wavelet-Regularized 3D Gaussian Splatting for Sparse-View Scene Reconstruction](https://arxiv.org/abs/2601.17185v1)**  
  Authors: Shima Salehi, Atharva Agashe, Andrew J. McFarland, Joshua Peeples  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17185v1.pdf)  
  Keywords: few-shot, ar, geometry, sparse-view, 3d reconstruction, 3d gaussian, gaussian splatting  
- **[FastGHA: Generalized Few-Shot 3D Gaussian Head Avatars with Real-Time Animation](https://arxiv.org/abs/2601.13837v2)**  
  Authors: Xinya Ji, Sebastian Weiss, Manuel Kansy, Jacek Naruniec, Xun Cao, Barbara Solenthaler, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.13837v2.pdf)  
  Keywords: few-shot, dynamic, lightweight, animation, efficient, ar, geometry, avatar, head, deformation, 3d gaussian, fast  
- **[SA-ResGS: Self-Augmented Residual 3D Gaussian Splatting for Next Best View Selection](https://arxiv.org/abs/2601.03024v2)**  
  Authors: Kim Jun-Seong, Tae-Hyun Oh, Eduardo Pérez-Pellitero, Youngkyoon Jang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03024v2.pdf)  
  Keywords: ar, efficient, sparse-view, 3d gaussian, gaussian splatting  
- **[360-GeoGS: Geometrically Consistent Feed-Forward 3D Gaussian Splatting Reconstruction for 360 Images](https://arxiv.org/abs/2601.02102v1)**  
  Authors: Jiaqi Yao, Zhongmiao Yan, Jingyi Xu, Songpengcheng Xia, Yan Xiang, Ling Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02102v1.pdf)  
  Keywords: ar, efficient, robotics, neural rendering, efficient rendering, face, 3d reconstruction, sparse view, 3d gaussian, gaussian splatting  
- **[ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2601.00939v1)**  
  Authors: Feng Luo, Hongbo Pan, Xiang Yang, Baoyu Jiang, Fengqing Liu, Tao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00939v1.pdf)  
  Keywords: ray marching, ar, efficient, efficient rendering, illumination, sparse-view, 3d reconstruction, 3d gaussian, shadow, gaussian splatting  
- **[SV-GS: Sparse View 4D Reconstruction with Skeleton-Driven Gaussian Splatting](https://arxiv.org/abs/2601.00285v1)**  
  Authors: Jun-Jee Chao, Volkan Isler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00285v1.pdf)  
  Keywords: dynamic, ar, 4d, sparse view, motion, deformation, gaussian splatting  
- **[3D Scene Change Modeling With Consistent Multi-View Aggregation](https://arxiv.org/abs/2512.22830v1)**  
  Authors: Zirui Zhou, Junfeng Ni, Shujie Zhang, Yixin Chen, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22830v1.pdf)  
  Keywords: sparse-view, ar, dynamic  
- **[SplatBright: Generalizable Low-Light Scene Reconstruction from Sparse Views via Physically-Guided Gaussian Enhancement](https://arxiv.org/abs/2512.18655v1)**  
  Authors: Yue Wen, Liang Song, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18655v1.pdf)  
  Keywords: ar, lighting, geometry, illumination, 3d reconstruction, sparse view, 3d gaussian  

### Geometry Reconstruction

*Showing the latest 50 out of 190 papers*

- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2602.06846v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06846v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, vr, reflection, geometry, head, motion, 3d gaussian, gaussian splatting, semantic  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, animation, geometry, face, 3d reconstruction, avatar, head, motion, 3d gaussian, gaussian splatting  
- **[Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction For 3D-Aware Distillation](https://arxiv.org/abs/2602.06032v1)**  
  Authors: David Shavin, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06032v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://davidshavin4.github.io/Splat-and-Distill)  
  Keywords: dynamic, ar, face, 3d reconstruction, segmentation, 3d gaussian, fast, semantic  
- **[Unified Sensor Simulation for Autonomous Driving](https://arxiv.org/abs/2602.05617v1)**  
  Authors: Nikolay Patakin, Arsenii Shirokov, Anton Konushin, Dmitry Senushkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05617v1.pdf) | [![GitHub](https://img.shields.io/github/stars/whesense/XSIM?style=social)](https://github.com/whesense/XSIM)  
  Keywords: ar, dynamic, geometry, autonomous driving, 3d gaussian  
- **[QuantumGS: Quantum Encoding Framework for Gaussian Splatting](https://arxiv.org/abs/2602.05047v1)**  
  Authors: Grzegorz Wilczyński, Rafał Tobiasz, Paweł Gora, Marcin Mazur, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05047v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/QuantumGS?style=social)](https://github.com/gwilczynski95/QuantumGS)  
  Keywords: ar, neural rendering, reflection, geometry, real-time rendering, 3d gaussian, gaussian splatting  
- **[AnyStyle: Single-Pass Multimodal Stylization for 3D Gaussian Splatting](https://arxiv.org/abs/2602.04043v1)**  
  Authors: Joanna Kaleta, Bartosz Świrta, Kacper Kania, Przemysław Spurek, Marek Kowalski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04043v1.pdf) | [![GitHub](https://img.shields.io/github/stars/joaxkal/AnyStyle?style=social)](https://github.com/joaxkal/AnyStyle)  
  Keywords: 3d gaussian, ar, 3d reconstruction, gaussian splatting  
- **[WebSplatter: Enabling Cross-Device Efficient Gaussian Splatting in Web Browsers via WebGPU](https://arxiv.org/abs/2602.03207v1)**  
  Authors: Yudong Han, Chao Xu, Xiaodan Ye, Weichen Bi, Zilong Dong, Yun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03207v1.pdf)  
  Keywords: dynamic, ar, efficient, geometry, gaussian splatting  
- **[SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors](https://arxiv.org/abs/2602.02000v2)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Ning Cao, Gang Chen, Zhengxue Cheng, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02000v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hebing-sjtu.github.io/SurfSplat-website)  
  Keywords: high-fidelity, ar, geometry, face, 3d reconstruction, 3d gaussian, gaussian splatting  
- **[CloDS: Visual-Only Unsupervised Cloth Dynamics Learning in Unknown Conditions](https://arxiv.org/abs/2602.01844v1)**  
  Authors: Yuliang Zhan, Jian Li, Wenbing Huang, Wenbing Huang, Yang Liu, Hao Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01844v1.pdf) | [![GitHub](https://img.shields.io/github/stars/whynot-zyl/CloDS?style=social)](https://github.com/whynot-zyl/CloDS)  
  Keywords: mapping, dynamic, ar, geometry, deformation, gaussian splatting  
- **[MarkCleaner: High-Fidelity Watermark Removal via Imperceptible Micro-Geometric Perturbation](https://arxiv.org/abs/2602.01513v1)**  
  Authors: Xiaoxi Kong, Jieyu Yuan, Pengdi Chen, Yuanlin Zhang, Chongyi Li, Bin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01513v1.pdf)  
  Keywords: high-fidelity, ar, efficient, geometry, gaussian splatting, semantic  

### Large Scene

- **[3DGS$^2$-TR: Scalable Second-Order Trust-Region Method for 3D Gaussian Splatting](https://arxiv.org/abs/2602.00395v1)**  
  Authors: Roger Hsiao, Yuchen Fang, Xiangru Huang, Ruilong Li, Hesam Rabeti, Zan Gojcic, Javad Lavaei, James Demmel, Sophia Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00395v1.pdf)  
  Keywords: large scene, ar, efficient, head, 3d gaussian, gaussian splatting  
- **[EVolSplat4D: Efficient Volume-based Gaussian Splatting for 4D Urban Scene Synthesis](https://arxiv.org/abs/2601.15951v1)**  
  Authors: Sheng Miao, Sijin Li, Pan Wang, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15951v1.pdf)  
  Keywords: dynamic, ar, 4d, efficient, geometry, urban scene, autonomous driving, motion, 3d gaussian, gaussian splatting, semantic  
- **[ScenDi: 3D-to-2D Scene Diffusion Cascades for Urban Generation](https://arxiv.org/abs/2601.15221v1)**  
  Authors: Hanlei Guo, Jiahao Shao, Xinya Chen, Xiyang Tan, Sheng Miao, Yujun Shen, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15221v1.pdf)  
  Keywords: 3d gaussian, ar, urban scene  
- **[Clean-GS: Semantic Mask-Guided Pruning for 3D Gaussian Splatting](https://arxiv.org/abs/2601.00913v1)**  
  Authors: Subhankar Mishra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00913v1.pdf) | [![GitHub](https://img.shields.io/github/stars/smlab-niser/clean-gs?style=social)](https://github.com/smlab-niser/clean-gs)  
  Keywords: ar, vr, segmentation, outdoor, 3d gaussian, compression, gaussian splatting, semantic  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: ar, efficient, geometry, illumination, urban scene, face, 3d reconstruction, 3d gaussian, gaussian splatting  
- **[Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries](https://arxiv.org/abs/2512.13796v1)**  
  Authors: Victor Rong, Jan Held, Victor Chu, Daniel Rebain, Marc Van Droogenbroeck, Kiriakos N. Kutulakos, Andrea Tagliasacchi, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13796v1.pdf)  
  Keywords: ar, compact, geometry, outdoor, 3d gaussian, fast, gaussian splatting  
- **[Flux4D: Flow-based Unsupervised 4D Reconstruction](https://arxiv.org/abs/2512.03210v1)**  
  Authors: Jingkang Wang, Henry Che, Yun Chen, Ze Yang, Lily Goli, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03210v1.pdf)  
  Keywords: dynamic, ar, 4d, efficient, robotics, nerf, motion, outdoor, 3d gaussian, gaussian splatting  
- **[Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI](https://arxiv.org/abs/2511.20620v1)**  
  Authors: Xinhao Liu, Jiaqi Li, Youming Deng, Ruxin Chen, Yingjia Zhang, Yifei Ma, Li Guo, Yiming Li, Jing Zhang, Chen Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.20620v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ai4ce.github.io/wanderland)  
  Keywords: high-fidelity, ar, urban scene, geometry, 3d reconstruction, outdoor  
- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs)  
  Keywords: ar, geometry, 3d reconstruction, outdoor, 3d gaussian, understanding, gaussian splatting  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: ar, geometry, outdoor, fast, gaussian splatting, semantic  

### Model Compression

*Showing the latest 50 out of 205 papers*

- **[GaussianPOP: Principled Simplification Framework for Compact 3D Gaussian Splatting via Error Quantification](https://arxiv.org/abs/2602.06830v1)**  
  Authors: Soonbin Lee, Yeong-Gyu Kim, Simon Sasse, Tomas M. Borges, Yago Sanchez, Eun-Seok Ryu, Thomas Schierl, Cornelius Hellge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06830v1.pdf)  
  Keywords: ar, efficient, 3d gaussian, compact, gaussian splatting  
- **[TFusionOcc: Student's t-Distribution Based Object-Centric Multi-Sensor Fusion Framework for 3D Occupancy Prediction](https://arxiv.org/abs/2602.06400v1)**  
  Authors: Zhenxing Ming, Julie Stephany Berrio, Mao Shan, Stewart Worrall  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06400v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DanielMing123/TFusionOcc?style=social)](https://github.com/DanielMing123/TFusionOcc)  
  Keywords: efficient, 3d gaussian, ar, semantic  
- **[Nix and Fix: Targeting 1000x Compression of 3D Gaussian Splatting with Diffusion Models](https://arxiv.org/abs/2602.04549v1)**  
  Authors: Cem Eteke, Enzo Tartaglione  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04549v1.pdf)  
  Keywords: 3d gaussian, ar, compression, gaussian splatting  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: mapping, dynamic, ar, efficient, tracking, face, survey, motion, 3d gaussian, slam, gaussian splatting, localization  
- **[Constrained Dynamic Gaussian Splatting](https://arxiv.org/abs/2602.03538v1)**  
  Authors: Zihan Zheng, Zhenglong Wu, Xuanxuan Wang, Houqiang Zhong, Xiaoyun Zhang, Qiang Hu, Guangtao Zhai, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03538v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, motion, compression, gaussian splatting  
- **[WebSplatter: Enabling Cross-Device Efficient Gaussian Splatting in Web Browsers via WebGPU](https://arxiv.org/abs/2602.03207v1)**  
  Authors: Yudong Han, Chao Xu, Xiaodan Ye, Weichen Bi, Zilong Dong, Yun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03207v1.pdf)  
  Keywords: dynamic, ar, efficient, geometry, gaussian splatting  
- **[SharpTimeGS: Sharp and Stable Dynamic Gaussian Splatting via Lifespan Modulation](https://arxiv.org/abs/2602.02989v2)**  
  Authors: Zhanfeng Liao, Jiajun Zhang, Hanzhang Tu, Zhixi Wang, Yunqi Gao, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02989v2.pdf)  
  Keywords: dynamic, ar, 4d, real-time rendering, motion, compact, gaussian splatting  
- **[UrbanGS: A Scalable and Efficient Architecture for Geometrically Accurate Large-Scene Reconstruction](https://arxiv.org/abs/2602.02089v1)**  
  Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Xiuping Liang, Tongfei Chen, Shuwei Shao, Linlin Yang, Huobin Tan, Baochang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02089v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, efficient, real-time rendering, 3d gaussian, gaussian splatting  
- **[FastPhysGS: Accelerating Physics-based Dynamic 3DGS Simulation via Interior Completion and Adaptive Optimization](https://arxiv.org/abs/2602.01723v1)**  
  Authors: Yikun Ma, Yiqing Li, Jingwen Ye, Zhongkai Wu, Weidong Zhang, Lin Gao, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01723v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, efficient, face, motion, 3d gaussian, fast, gaussian splatting  
- **[MarkCleaner: High-Fidelity Watermark Removal via Imperceptible Micro-Geometric Perturbation](https://arxiv.org/abs/2602.01513v1)**  
  Authors: Xiaoxi Kong, Jieyu Yuan, Pengdi Chen, Yuanlin Zhang, Chongyi Li, Bin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01513v1.pdf)  
  Keywords: high-fidelity, ar, efficient, geometry, gaussian splatting, semantic  

### Quality Enhancement

*Showing the latest 50 out of 125 papers*

- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2602.06846v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06846v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, vr, reflection, geometry, head, motion, 3d gaussian, gaussian splatting, semantic  
- **[Uncertainty-Aware 4D Gaussian Splatting for Monocular Occluded Human Rendering](https://arxiv.org/abs/2602.06343v1)**  
  Authors: Weiquan Wang, Feifei Shao, Lin Li, Zhen Wang, Jun Xiao, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06343v1.pdf)  
  Keywords: high-fidelity, human, dynamic, ar, 4d, motion, deformation, gaussian splatting  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, animation, geometry, face, 3d reconstruction, avatar, head, motion, 3d gaussian, gaussian splatting  
- **[PoseGaussian: Pose-Driven Novel View Synthesis for Robust 3D Human Reconstruction](https://arxiv.org/abs/2602.05190v1)**  
  Authors: Ju Shen, Chen Chen, Tam V. Nguyen, Vijayan K. Asari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05190v1.pdf)  
  Keywords: high-fidelity, human, body, dynamic, ar, real-time rendering, motion, gaussian splatting  
- **[VecSet-Edit: Unleashing Pre-trained LRM for Mesh Editing from Single Image](https://arxiv.org/abs/2602.04349v1)**  
  Authors: Teng-Fang Hsiao, Bo-Kai Ruan, Yu-Lun Liu, Hong-Han Shuai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04349v1.pdf) | [![GitHub](https://img.shields.io/github/stars/BlueDyee/VecSet-Edit?style=social)](https://github.com/BlueDyee/VecSet-Edit)  
  Keywords: high-fidelity, 3d gaussian, ar, gaussian splatting  
- **[JOintGS: Joint Optimization of Cameras, Bodies and 3D Gaussians for In-the-Wild Monocular Reconstruction](https://arxiv.org/abs/2602.04317v1)**  
  Authors: Zihan Lou, Jinlong Fan, Sihan Ma, Yuxiang Yang, Jing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04317v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MiliLab/JOintGS?style=social)](https://github.com/MiliLab/JOintGS)  
  Keywords: high-fidelity, human, body, dynamic, ar, illumination, real-time rendering, avatar, deformation, 3d gaussian  
- **[Constrained Dynamic Gaussian Splatting](https://arxiv.org/abs/2602.03538v1)**  
  Authors: Zihan Zheng, Zhenglong Wu, Xuanxuan Wang, Houqiang Zhong, Xiaoyun Zhang, Qiang Hu, Guangtao Zhai, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03538v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, motion, compression, gaussian splatting  
- **[UrbanGS: A Scalable and Efficient Architecture for Geometrically Accurate Large-Scene Reconstruction](https://arxiv.org/abs/2602.02089v1)**  
  Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Xiuping Liang, Tongfei Chen, Shuwei Shao, Linlin Yang, Huobin Tan, Baochang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02089v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, efficient, real-time rendering, 3d gaussian, gaussian splatting  
- **[SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors](https://arxiv.org/abs/2602.02000v2)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Ning Cao, Gang Chen, Zhengxue Cheng, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02000v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hebing-sjtu.github.io/SurfSplat-website)  
  Keywords: high-fidelity, ar, geometry, face, 3d reconstruction, 3d gaussian, gaussian splatting  
- **[FastPhysGS: Accelerating Physics-based Dynamic 3DGS Simulation via Interior Completion and Adaptive Optimization](https://arxiv.org/abs/2602.01723v1)**  
  Authors: Yikun Ma, Yiqing Li, Jingwen Ye, Zhongkai Wu, Weidong Zhang, Lin Gao, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01723v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, efficient, face, motion, 3d gaussian, fast, gaussian splatting  

### Ray Tracing

- **[Radioactive 3D Gaussian Ray Tracing for Tomographic Reconstruction](https://arxiv.org/abs/2602.01057v1)**  
  Authors: Ling Chen, Bao Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01057v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, ray tracing  
- **[EAG-PT: Emission-Aware Gaussians and Path Tracing for Indoor Scene Reconstruction and Editing](https://arxiv.org/abs/2601.23065v1)**  
  Authors: Xijie Yang, Mulin Yu, Changjian Jiang, Kerui Ren, Tao Lu, Jiangmiao Pang, Dahua Lin, Bo Dai, Linning Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.23065v1.pdf)  
  Keywords: ar, light transport, efficient, nerf, geometry, illumination, path tracing  
- **[Hybrid Foveated Path Tracing with Peripheral Gaussians for Immersive Anatomy](https://arxiv.org/abs/2601.22026v1)**  
  Authors: Constantin Kleinbeck, Luisa Theelke, Hannah Schieber, Ulrich Eck, Rüdiger von Eisenhart-Rothe, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22026v1.pdf)  
  Keywords: medical, ar, lightweight, vr, path tracing, head, understanding, gaussian splatting  
- **[GRTX: Efficient Ray Tracing for 3D Gaussian-Based Rendering](https://arxiv.org/abs/2601.20429v1)**  
  Authors: Junseo Lee, Sangyun Jeon, Jungi Lee, Junyong Park, Jaewoong Sim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20429v1.pdf)  
  Keywords: ar, efficient, acceleration, head, ray tracing, 3d gaussian, gaussian splatting  
- **[ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2601.00939v1)**  
  Authors: Feng Luo, Hongbo Pan, Xiang Yang, Baoyu Jiang, Fengqing Liu, Tao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00939v1.pdf)  
  Keywords: ray marching, ar, efficient, efficient rendering, illumination, sparse-view, 3d reconstruction, 3d gaussian, shadow, gaussian splatting  
- **[Geometric-Photometric Event-based 3D Gaussian Ray Tracing](https://arxiv.org/abs/2512.18640v1)**  
  Authors: Kai Kohyama, Yoshimitsu Aoki, Guillermo Gallego, Shintaro Shiba  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18640v1.pdf)  
  Keywords: ar, geometry, understanding, 3d reconstruction, ray tracing, motion, 3d gaussian, fast, gaussian splatting  
- **[MatSpray: Fusing 2D Material World Knowledge on 3D Geometry](https://arxiv.org/abs/2512.18314v1)**  
  Authors: Philipp Langsteiner, Jan-Niklas Dihlmann, Hendrik P. A. Lensch  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18314v1.pdf)  
  Keywords: relightable, ar, lighting, geometry, relighting, 3d reconstruction, ray tracing, gaussian splatting  
- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: ar, nerf, face, ray tracing, 3d gaussian, fast, gaussian splatting  
- **[From Particles to Fields: Reframing Photon Mapping with Continuous Gaussian Photon Fields](https://arxiv.org/abs/2512.12459v1)**  
  Authors: Jiachen Tao, Benjamin Planche, Van Nguyen Nguyen, Junyi Wu, Yuchun Liu, Haoxuan Wang, Zhongpai Gao, Gengyu Zhang, Meng Zheng, Feiran Wang, Anwesa Choudhuri, Zhenghao Zhao, Weitai Kang, Terrence Chen, Yan Yan, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.12459v1.pdf)  
  Keywords: ar, light transport, global illumination, efficient, illumination, mapping, 3d gaussian  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: high-fidelity, ar, compact, real-time rendering, ray tracing, 3d gaussian, fast, gaussian splatting  

### Relighting

*Showing the latest 50 out of 68 papers*

- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2602.06846v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06846v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, vr, reflection, geometry, head, motion, 3d gaussian, gaussian splatting, semantic  
- **[NVS-HO: A Benchmark for Novel View Synthesis of Handheld Objects](https://arxiv.org/abs/2602.05822v1)**  
  Authors: Musawar Ali, Manuel Carranza-García, Nicola Fioraio, Samuele Salti, Luigi Di Stefano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05822v1.pdf)  
  Keywords: lighting, nerf, ar, gaussian splatting  
- **[QuantumGS: Quantum Encoding Framework for Gaussian Splatting](https://arxiv.org/abs/2602.05047v1)**  
  Authors: Grzegorz Wilczyński, Rafał Tobiasz, Paweł Gora, Marcin Mazur, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05047v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/QuantumGS?style=social)](https://github.com/gwilczynski95/QuantumGS)  
  Keywords: ar, neural rendering, reflection, geometry, real-time rendering, 3d gaussian, gaussian splatting  
- **[JOintGS: Joint Optimization of Cameras, Bodies and 3D Gaussians for In-the-Wild Monocular Reconstruction](https://arxiv.org/abs/2602.04317v1)**  
  Authors: Zihan Lou, Jinlong Fan, Sihan Ma, Yuxiang Yang, Jing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04317v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MiliLab/JOintGS?style=social)](https://github.com/MiliLab/JOintGS)  
  Keywords: high-fidelity, human, body, dynamic, ar, illumination, real-time rendering, avatar, deformation, 3d gaussian  
- **[Position: 3D Gaussian Splatting Watermarking Should Be Scenario-Driven and Threat-Model Explicit](https://arxiv.org/abs/2602.02602v1)**  
  Authors: Yangfan Deng, Anirudh Nakra, Min Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02602v1.pdf)  
  Keywords: high-fidelity, ar, lighting, 3d gaussian, gaussian splatting  
- **[EAG-PT: Emission-Aware Gaussians and Path Tracing for Indoor Scene Reconstruction and Editing](https://arxiv.org/abs/2601.23065v1)**  
  Authors: Xijie Yang, Mulin Yu, Changjian Jiang, Kerui Ren, Tao Lu, Jiangmiao Pang, Dahua Lin, Bo Dai, Linning Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.23065v1.pdf)  
  Keywords: ar, light transport, efficient, nerf, geometry, illumination, path tracing  
- **[Diachronic Stereo Matching for Multi-Date Satellite Imagery](https://arxiv.org/abs/2601.22808v1)**  
  Authors: Elías Masquil, Luca Savant Aira, Roger Marí, Thibaud Ehret, Pablo Musé, Gabriele Facciolo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22808v1.pdf)  
  Keywords: ar, nerf, geometry, illumination, 3d reconstruction, shadow  
- **[Mirage2Matter: A Physically Grounded Gaussian World Model from Video](https://arxiv.org/abs/2602.00096v1)**  
  Authors: Zhengqing Gao, Ziwen Li, Xin Wang, Jiaxin Huang, Zhenyang Ren, Mingkai Shao, Hanlue Zhang, Tianyu Huang, Yongkang Cheng, Yandong Guo, Runqi Lin, Yuanyuan Wang, Tongliang Liu, Kun Zhang, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00096v1.pdf)  
  Keywords: high-fidelity, ar, efficient, lighting, geometry, 3d gaussian, gaussian splatting  
- **[ThermoSplat: Cross-Modal 3D Gaussian Splatting with Feature Modulation and Geometry Decoupling](https://arxiv.org/abs/2601.15897v1)**  
  Authors: Zhaoqi Su, Shihai Chen, Xinyan Lin, Liqin Huang, Zhipeng Su, Xiaoqiang Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15897v1.pdf)  
  Keywords: dynamic, ar, lighting, geometry, 3d gaussian, gaussian splatting, semantic  
- **[LL-GaussianMap: Zero-shot Low-Light Image Enhancement via 2D Gaussian Splatting Guided Gain Maps](https://arxiv.org/abs/2601.15766v2)**  
  Authors: Yuhan Chen, Ying Fang, Guofa Li, Wenxuan Yu, Yicui Shi, Jingrui Zhang, Kefei Qian, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15766v2.pdf)  
  Keywords: high-fidelity, ar, efficient, lighting, gaussian splatting  

### SLAM

*Showing the latest 50 out of 73 papers*

- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: mapping, dynamic, ar, efficient, tracking, face, survey, motion, 3d gaussian, slam, gaussian splatting, localization  
- **[CloDS: Visual-Only Unsupervised Cloth Dynamics Learning in Unknown Conditions](https://arxiv.org/abs/2602.01844v1)**  
  Authors: Yuliang Zhan, Jian Li, Wenbing Huang, Wenbing Huang, Yang Liu, Hao Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01844v1.pdf) | [![GitHub](https://img.shields.io/github/stars/whynot-zyl/CloDS?style=social)](https://github.com/whynot-zyl/CloDS)  
  Keywords: mapping, dynamic, ar, geometry, deformation, gaussian splatting  
- **[OFERA: Blendshape-driven 3D Gaussian Control for Occluded Facial Expression to Realistic Avatars in VR](https://arxiv.org/abs/2602.01748v1)**  
  Authors: Seokhwan Yang, Boram Yoon, Seoyoung Kang, Hail Song, Woontack Woo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01748v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ysshwan147.github.io/projects/ofera)  
  Keywords: mapping, ar, vr, head, avatar, 3d gaussian  
- **[VRGaussianAvatar: Integrating 3D Gaussian Avatars into VR](https://arxiv.org/abs/2602.01674v1)**  
  Authors: Hail Song, Boram Yoon, Seokhwan Yang, Seoyoung Kang, Hyunjeong Kim, Henning Metzmacher, Woontack Woo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01674v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vrgaussianavatar.github.io)  
  Keywords: body, ar, vr, tracking, head, avatar, 3d gaussian, gaussian splatting  
- **[Synthetic-to-Real Domain Bridging for Single-View 3D Reconstruction of Ships for Maritime Monitoring](https://arxiv.org/abs/2601.21786v1)**  
  Authors: Borja Carrillo-Perez, Felix Sattler, Angel Bueno Rodriguez, Maurice Stephan, Sarah Barnes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.21786v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dlr-mi.github.io/ship3d-demo/.) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://dlr-mi.github.io/ship3d-demo)  
  Keywords: ar, efficient, segmentation, 3d reconstruction, mapping, 3d gaussian  
- **[Fast Converging 3D Gaussian Splatting for 1-Minute Reconstruction](https://arxiv.org/abs/2601.19489v2)**  
  Authors: Ziyu Zhang, Tianle Liu, Diantao Tu, Shuhan Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19489v2.pdf)  
  Keywords: high-fidelity, fast, ar, head, 3d gaussian, compact, gaussian splatting, slam  
- **[Structured Image-based Coding for Efficient Gaussian Splatting Compression](https://arxiv.org/abs/2601.14510v2)**  
  Authors: Pedro Martin, Antonio Rodrigues, Joao Ascenso, Maria Paula Queluz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.14510v2.pdf)  
  Keywords: ar, efficient, nerf, real-time rendering, mapping, compression, gaussian splatting  
- **[ParkingTwin: Training-Free Streaming 3D Reconstruction for Parking-Lot Digital Twins](https://arxiv.org/abs/2601.13706v1)**  
  Authors: Xinhao Liu, Yu Wang, Xiansheng Guo, Gordon Owusu Boateng, Yu Cao, Haonan Si, Xingchen Guo, Nirwan Ansari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.13706v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mihoutao-liu.github.io/ParkingTwin)  
  Keywords: high-fidelity, dynamic, lightweight, ar, neural rendering, lighting, geometry, illumination, face, 3d reconstruction, mapping, 3d gaussian, gaussian splatting, semantic  
- **[Active Semantic Mapping of Horticultural Environments Using Gaussian Splatting](https://arxiv.org/abs/2601.12122v1)**  
  Authors: Jose Cuaran, Naveen K. Upalapati, Girish Chowdhary  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12122v1.pdf)  
  Keywords: high-fidelity, ar, efficient, robotics, lighting, 3d reconstruction, segmentation, mapping, 3d gaussian, gaussian splatting, semantic  
- **[Variable Basis Mapping for Real-Time Volumetric Visualization](https://arxiv.org/abs/2601.09417v1)**  
  Authors: Qibiao Li, Yuxuan Wang, Youcheng Cai, Huangsheng Du, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.09417v1.pdf)  
  Keywords: ar, lightweight, efficient, mapping, 3d gaussian, compact, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 119 papers*

- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2602.06846v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06846v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, 4d, vr, reflection, geometry, head, motion, 3d gaussian, gaussian splatting, semantic  
- **[TFusionOcc: Student's t-Distribution Based Object-Centric Multi-Sensor Fusion Framework for 3D Occupancy Prediction](https://arxiv.org/abs/2602.06400v1)**  
  Authors: Zhenxing Ming, Julie Stephany Berrio, Mao Shan, Stewart Worrall  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06400v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DanielMing123/TFusionOcc?style=social)](https://github.com/DanielMing123/TFusionOcc)  
  Keywords: efficient, 3d gaussian, ar, semantic  
- **[Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction For 3D-Aware Distillation](https://arxiv.org/abs/2602.06032v1)**  
  Authors: David Shavin, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06032v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://davidshavin4.github.io/Splat-and-Distill)  
  Keywords: dynamic, ar, face, 3d reconstruction, segmentation, 3d gaussian, fast, semantic  
- **[Seeing Through Clutter: Structured 3D Scene Reconstruction via Iterative Object Removal](https://arxiv.org/abs/2602.04053v1)**  
  Authors: Rio Aguina-Kang, Kevin James Blackburn-Matzen, Thibault Groueix, Vladimir Kim, Matheus Gadelha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04053v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rioak.github.io/seeingthroughclutter)  
  Keywords: segmentation, ar, semantic  
- **[MarkCleaner: High-Fidelity Watermark Removal via Imperceptible Micro-Geometric Perturbation](https://arxiv.org/abs/2602.01513v1)**  
  Authors: Xiaoxi Kong, Jieyu Yuan, Pengdi Chen, Yuanlin Zhang, Chongyi Li, Bin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01513v1.pdf)  
  Keywords: high-fidelity, ar, efficient, geometry, gaussian splatting, semantic  
- **[Split&Splat: Zero-Shot Panoptic Segmentation via Explicit Instance Modeling and 3D Gaussian Splatting](https://arxiv.org/abs/2602.03809v1)**  
  Authors: Leonardo Monchieri, Elena Camuffo, Francesco Barbato, Pietro Zanuttigh, Simone Milani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03809v1.pdf)  
  Keywords: ar, segmentation, 3d gaussian, fast, gaussian splatting, semantic  
- **[PSGS: Text-driven Panorama Sliding Scene Generation via Gaussian Splatting](https://arxiv.org/abs/2602.00463v1)**  
  Authors: Xin Zhang, Shen Chen, Jiale Zhou, Lei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00463v1.pdf)  
  Keywords: high-fidelity, ar, vr, 3d gaussian, gaussian splatting, semantic  
- **[Learning Geometrically-Grounded 3D Visual Representations for View-Generalizable Robotic Manipulation](https://arxiv.org/abs/2601.22988v1)**  
  Authors: Di Zhang, Weicheng Duan, Dasen Gu, Hongye Lu, Hai Zhang, Hang Yu, Junqiao Zhao, Guang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22988v1.pdf)  
  Keywords: ar, understanding, gaussian splatting  
- **[GaussianOcc3D: A Gaussian-Based Adaptive Multi-modal 3D Occupancy Prediction](https://arxiv.org/abs/2601.22729v1)**  
  Authors: A. Enes Doruk, Hasan F. Ates  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22729v1.pdf)  
  Keywords: ar, efficient, geometry, face, autonomous driving, head, 3d gaussian, understanding, semantic  
- **[Hybrid Foveated Path Tracing with Peripheral Gaussians for Immersive Anatomy](https://arxiv.org/abs/2601.22026v1)**  
  Authors: Constantin Kleinbeck, Luisa Theelke, Hannah Schieber, Ulrich Eck, Rüdiger von Eisenhart-Rothe, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22026v1.pdf)  
  Keywords: medical, ar, lightweight, vr, path tracing, head, understanding, gaussian splatting  



## Classic Papers
- **[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)** (SIGGRAPH 2023)  
  Authors: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis  
  Code: 🔗 [GitHub](https://github.com/graphdeco-inria/gaussian-splatting)  
  Keywords: Real-time Rendering, Neural Rendering, Point-based Graphics

- **[Instruct-4DGS: Efficient Dynamic Scene Editing via 4D Gaussian-based Static-Dynamic Separation](https://hanbyelcho.info/instruct-4dgs/)** (CVPR 2025)  
  Authors: Hanbyel Cho, Juhyeon Kwon, et al.  
  Paper: 📄 [arXiv](https://arxiv.org/abs/2502.02091)  
  Code: 🔗 [GitHub](https://github.com/juhyeon-kwon/efficient_4d_gaussian_editing)  
  Keywords: Dynamic Scene Editing, 4D Gaussian Splatting, Static-Dynamic Separation

## Open Source Projects
- [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) - Original implementation of 3D Gaussian Splatting
- [taichi-3d-gaussian-splatting](https://github.com/wanmeihuali/taichi-3d-gaussian-splatting) - 3D Gaussian Splatting implemented in Taichi

## Applications
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering Demo](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) - Online Demo

## Tutorials & Blogs
- [Introduction to 3D Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting) - Official Tutorial

## 📋 Project Features

### 🛠️ Core Features
- **Unified CLI** (`main.py`): Single entry point with `init`, `search`, `suggest`, `export-bib`, `readme` subcommands
- **Interactive Config Wizard**: Guided setup for keywords, domains, time range, and API keys via `python main.py init`
- **Custom Search Keywords**: Configure keywords for title, abstract, or both; with arXiv domain filtering (`cs.CV`, `cs.GR`, etc.)
- **Time Range Filtering**: Relative periods (`30d`, `6m`, `1y`, `2y`) or absolute date ranges (`YYYY-MM-DD` to `YYYY-MM-DD`)
- **Smart Link Extraction**: Auto-classifies URLs from abstracts into GitHub, project page, dataset, video, demo, HuggingFace links
- **BibTeX Export**: Fetch BibTeX from arXiv official API; export to `.bib` files with category and date filters
- **LLM Keyword Suggestion**: Input paper titles or arXiv IDs to auto-generate optimized search keywords via OpenAI-compatible API
- **Automated Paper Collection**: Daily automatic crawling with GitHub Actions
- **Intelligent Classification**: Auto-categorize papers into 14+ topics (Acceleration, Dynamic Scenes, SLAM, etc.)

### 🛠️ Technical Features
- **Robust Error Handling**: Multi-layer retry and fallback strategies ensure stable operation
- **GitHub Actions Integration**: Automated CI/CD workflows for daily updates
- **Multi-type Link Badges**: README entries display PDF, GitHub (with stars), Project, Dataset, Video, Demo, HuggingFace, and Citation badges
- **Detailed Logging**: Comprehensive logging for debugging and monitoring
- **Cross-Platform**: Support for Windows/Linux/macOS

### 📚 Data Output
- **Paper JSON files** (`data/papers_YYYY-MM-DD.json`): Full paper metadata with title, authors, abstract, links, keywords, BibTeX
- **BibTeX files** (`output/*.bib`): Ready-to-use bibliography files for LaTeX
- **Auto-generated README**: Categorized and formatted paper listings

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Interactive Setup (Recommended)

```bash
python main.py init
```

This wizard walks you through:
- Setting search keywords (for title, abstract, or both)
- Selecting arXiv domains (e.g., `cs.CV`, `cs.GR`, `cs.AI`)
- Configuring time range (relative like `6m`/`1y`, or absolute dates)
- Setting max results
- Optionally configuring an OpenAI-compatible API key for keyword suggestion

### 3. Search Papers

```bash
# Search with settings from user_config.json
python main.py search

# Override: fetch 200 papers from the last 6 months, include BibTeX
python main.py search --max-results 200 --recent 6m --bibtex

# Search with absolute date range
python main.py search --date-from 2024-01-01 --date-to 2025-01-01

# Include citation counts from Semantic Scholar
python main.py search --citations
```

### 4. Export BibTeX

```bash
# Export all papers from the latest data file
python main.py export-bib --output output/references.bib

# Export only "Dynamic Scene" papers
python main.py export-bib --category "Dynamic Scene" --output output/dynamic.bib

# Export papers from a specific date range
python main.py export-bib --date-from 2024-06-01 --date-to 2025-01-01 --output output/recent.bib
```

### 5. LLM Keyword Suggestion

```bash
# Generate keywords from paper titles
python main.py suggest --titles "3D Gaussian Splatting for Real-Time Rendering" "Dynamic 3D Gaussians"

# Generate from arXiv IDs (auto-fetches titles)
python main.py suggest --arxiv-ids 2308.04079 2311.12897

# Auto-write suggested keywords to config
python main.py suggest --titles "NeRF" "Gaussian Splatting" --apply

# Use a custom API endpoint (e.g., DeepSeek)
python main.py suggest --titles "Paper Title" --base-url https://api.deepseek.com/v1 --api-key sk-xxx --model deepseek-chat
```

### 6. Generate README

```bash
# Basic README
python main.py readme

# Include latest papers section and abstracts
python main.py readme --show-latest --show-abstracts
```

### Configuration File

All settings are stored in `data/user_config.json`:

```json
{
  "search": {
    "keywords": {
      "both_abstract_and_title": ["gaussian splatting", "3d gaussian"],
      "abstract_only": ["neural radiance field gaussian"],
      "title_only": ["3D scene reconstruction"]
    },
    "domains": ["cs.CV", "cs.GR"],
    "time_range": {
      "mode": "relative",
      "relative": "1y"
    },
    "max_results": 500
  },
  "api_keys": {
    "openai_api_key": "",
    "openai_base_url": "https://api.openai.com/v1",
    "openai_model": "gpt-4o-mini"
  }
}
```

## Contribution Guidelines
Feel free to submit Pull Requests to improve this list! Please follow these formats:
- Paper entry format: `**[Paper Title](link)** - Brief description`
- Project entry format: `[Project Name](link) - Project description`

## License
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) 