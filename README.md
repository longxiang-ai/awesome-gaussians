# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-02-20 01:09:26

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

- [3DGS Surveys](#3dgs-surveys) (6 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (105 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (499 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (172 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (214 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (33 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (192 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (22 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (210 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (129 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (14 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (65 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (77 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (124 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: face, localization, survey, 3d gaussian, dynamic, motion, gaussian splatting, ar, mapping, efficient, tracking, slam  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: robotics, survey, 3d gaussian, gaussian splatting, ar  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v2)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v2.pdf)  
  Keywords: nerf, survey, 3d gaussian, geometry, gaussian splatting, ar, efficient  
- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197v1)**  
  Authors: Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07197v1.pdf)  
  Keywords: high-fidelity, 4d, survey, 3d gaussian, compact, dynamic, gaussian splatting, ar, compression, 3d reconstruction, efficient  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v2)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v2.pdf)  
  Keywords: understanding, semantic, localization, nerf, robotics, survey, 3d gaussian, gaussian splatting, ar, mapping, slam  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: semantic, localization, high-fidelity, robotics, survey, 3d gaussian, gaussian splatting, ar, mapping, efficient, slam  

### Acceleration

*Showing the latest 50 out of 105 papers*

- **[Semantic-Guided 3D Gaussian Splatting for Transient Object Removal](https://arxiv.org/abs/2602.15516v1)**  
  Authors: Aditi Prabakaran, Priyesh Shukla  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15516v1.pdf)  
  Keywords: head, semantic, nerf, 3d gaussian, real-time rendering, motion, gaussian splatting, ar  
- **[Time-Archival Camera Virtualization for Sports and Visual Performances](https://arxiv.org/abs/2602.15181v1)**  
  Authors: Yunxiao Zhang, William Stone, Suryansh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15181v1.pdf)  
  Keywords: 4d, 3d gaussian, dynamic, neural rendering, fast, motion, gaussian splatting, ar, efficient, tracking  
- **[Gaussian Mesh Renderer for Lightweight Differentiable Rendering](https://arxiv.org/abs/2602.14493v1)**  
  Authors: Xinpeng Liu, Fumio Okura  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14493v1.pdf) | [![GitHub](https://img.shields.io/github/stars/huntorochi/Gaussian-Mesh-Renderer?style=social)](https://github.com/huntorochi/Gaussian-Mesh-Renderer)  
  Keywords: face, high-fidelity, 3d gaussian, fast, lightweight, gaussian splatting, ar, efficient  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: nerf, 3d gaussian, illumination, real-time rendering, outdoor, gaussian splatting, ar, global illumination, autonomous driving, lighting  
- **[Faster-GS: Analyzing and Improving Gaussian Splatting Optimization](https://arxiv.org/abs/2602.09999v1)**  
  Authors: Florian Hahlbohm, Linus Franke, Martin Eisemann, Marcus Magnor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09999v1.pdf)  
  Keywords: 4d, 3d gaussian, fast, gaussian splatting, ar, efficient  
- **[ArtisanGS: Interactive Tools for Gaussian Splat Selection with AI and Human in the Loop](https://arxiv.org/abs/2602.10173v1)**  
  Authors: Clement Fuji Tsang, Anita Hu, Or Perel, Carsten Kolve, Maria Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10173v1.pdf)  
  Keywords: segmentation, 3d gaussian, fast, ar, human, animation  
- **[Toward Fine-Grained Facial Control in 3D Talking Head Generation](https://arxiv.org/abs/2602.09736v1)**  
  Authors: Shaoyang Xie, Xiaofeng Cong, Baosheng Yu, Zhipeng Gui, Jie Gui, Yuan Yan Tang, James Tin-Yau Kwok  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09736v1.pdf)  
  Keywords: head, high-fidelity, 3d gaussian, dynamic, real-time rendering, avatar, motion, gaussian splatting, ar  
- **[GaussianCaR: Gaussian Splatting for Efficient Camera-Radar Fusion](https://arxiv.org/abs/2602.08784v1)**  
  Authors: Santiago Montiel-Marín, Miguel Antunes-García, Fabio Sánchez-García, Angel Llamazares, Holger Caesar, Luis M. Bergasa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08784v1.pdf)  
  Keywords: segmentation, dynamic, fast, gaussian splatting, ar, mapping, efficient  
- **[Splat and Distill: Augmenting Teachers with Feed-Forward 3D Reconstruction For 3D-Aware Distillation](https://arxiv.org/abs/2602.06032v2)**  
  Authors: David Shavin, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06032v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://davidshavin4.github.io/Splat-and-Distill)  
  Keywords: segmentation, face, semantic, 3d gaussian, dynamic, fast, ar, 3d reconstruction  
- **[PoseGaussian: Pose-Driven Novel View Synthesis for Robust 3D Human Reconstruction](https://arxiv.org/abs/2602.05190v1)**  
  Authors: Ju Shen, Chen Chen, Tam V. Nguyen, Vijayan K. Asari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05190v1.pdf)  
  Keywords: high-fidelity, dynamic, real-time rendering, motion, gaussian splatting, ar, body, human  

### Applications

*Showing the latest 50 out of 499 papers*

- **[MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction](https://arxiv.org/abs/2602.15733v1)**  
  Authors: Qiang Zhang, Jiahao Ma, Peiran Liu, Shuai Shi, Zeran Su, Zifan Wang, Jingkai Sun, Wei Cui, Jialin Yu, Gang Han, Wen Zhao, Pihai Sun, Kangning Yin, Jiaxu Wang, Jiahang Cao, Lingfeng Zhang, Hao Cheng, Xiaoshuai Hao, Yiding Ji, Junwei Liang, Jian Tang, Renjing Xu, Yijie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15733v1.pdf)  
  Keywords: dynamic, geometry, motion, ar, human  
- **[Semantic-Guided 3D Gaussian Splatting for Transient Object Removal](https://arxiv.org/abs/2602.15516v1)**  
  Authors: Aditi Prabakaran, Priyesh Shukla  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15516v1.pdf)  
  Keywords: head, semantic, nerf, 3d gaussian, real-time rendering, motion, gaussian splatting, ar  
- **[DAV-GSWT: Diffusion-Active-View Sampling for Data-Efficient Gaussian Splatting Wang Tiles](https://arxiv.org/abs/2602.15355v1)**  
  Authors: Rong Fu, Jiekai Wu, Haiyun Wei, Yee Tan Jia, Wenxin Zhang, Yang Li, Xiaowen Ma, Wangyu Wu, Simon Fong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15355v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, neural rendering, gaussian splatting, ar, efficient  
- **[Time-Archival Camera Virtualization for Sports and Visual Performances](https://arxiv.org/abs/2602.15181v1)**  
  Authors: Yunxiao Zhang, William Stone, Suryansh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15181v1.pdf)  
  Keywords: 4d, 3d gaussian, dynamic, neural rendering, fast, motion, gaussian splatting, ar, efficient, tracking  
- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: head, semantic, localization, 3d gaussian, outdoor, geometry, gaussian splatting, ar, mapping, lighting  
- **[Gaussian Mesh Renderer for Lightweight Differentiable Rendering](https://arxiv.org/abs/2602.14493v1)**  
  Authors: Xinpeng Liu, Fumio Okura  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14493v1.pdf) | [![GitHub](https://img.shields.io/github/stars/huntorochi/Gaussian-Mesh-Renderer?style=social)](https://github.com/huntorochi/Gaussian-Mesh-Renderer)  
  Keywords: face, high-fidelity, 3d gaussian, fast, lightweight, gaussian splatting, ar, efficient  
- **[Learnable Multi-level Discrete Wavelet Transforms for 3D Gaussian Splatting Frequency Modulation](https://arxiv.org/abs/2602.14199v1)**  
  Authors: Hung Nguyen, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14199v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, 3d gaussian  
- **[High-fidelity 3D reconstruction for planetary exploration](https://arxiv.org/abs/2602.13909v1)**  
  Authors: Alfonso Martínez-Petersen, Levin Gerdes, David Rodríguez-Martínez, C. J. Pérez-del-Pulgar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13909v1.pdf)  
  Keywords: face, localization, nerf, high-fidelity, robotics, motion, gaussian splatting, ar, mapping, efficient, 3d reconstruction, slam  
- **[Gaussian Sequences with Multi-Scale Dynamics for 4D Reconstruction from Monocular Casual Videos](https://arxiv.org/abs/2602.13806v1)**  
  Authors: Can Li, Jie Gu, Jingmin Chen, Fangzhou Qiu, Lei Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13806v1.pdf)  
  Keywords: understanding, 4d, 3d gaussian, dynamic, motion, ar  
- **[Joint Orientation and Weight Optimization for Robust Watertight Surface Reconstruction via Dirichlet-Regularized Winding Fields](https://arxiv.org/abs/2602.13801v1)**  
  Authors: Jiaze Li, Daisheng Jin, Fei Hou, Junhui Hou, Zheng Liu, Shiqing Xin, Wenping Wang, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13801v1.pdf)  
  Keywords: face, 3d gaussian, gaussian splatting, ar, efficient  

### Avatar Generation

*Showing the latest 50 out of 172 papers*

- **[MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction](https://arxiv.org/abs/2602.15733v1)**  
  Authors: Qiang Zhang, Jiahao Ma, Peiran Liu, Shuai Shi, Zeran Su, Zifan Wang, Jingkai Sun, Wei Cui, Jialin Yu, Gang Han, Wen Zhao, Pihai Sun, Kangning Yin, Jiaxu Wang, Jiahang Cao, Lingfeng Zhang, Hao Cheng, Xiaoshuai Hao, Yiding Ji, Junwei Liang, Jian Tang, Renjing Xu, Yijie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15733v1.pdf)  
  Keywords: dynamic, geometry, motion, ar, human  
- **[Semantic-Guided 3D Gaussian Splatting for Transient Object Removal](https://arxiv.org/abs/2602.15516v1)**  
  Authors: Aditi Prabakaran, Priyesh Shukla  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15516v1.pdf)  
  Keywords: head, semantic, nerf, 3d gaussian, real-time rendering, motion, gaussian splatting, ar  
- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: head, semantic, localization, 3d gaussian, outdoor, geometry, gaussian splatting, ar, mapping, lighting  
- **[Gaussian Mesh Renderer for Lightweight Differentiable Rendering](https://arxiv.org/abs/2602.14493v1)**  
  Authors: Xinpeng Liu, Fumio Okura  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14493v1.pdf) | [![GitHub](https://img.shields.io/github/stars/huntorochi/Gaussian-Mesh-Renderer?style=social)](https://github.com/huntorochi/Gaussian-Mesh-Renderer)  
  Keywords: face, high-fidelity, 3d gaussian, fast, lightweight, gaussian splatting, ar, efficient  
- **[High-fidelity 3D reconstruction for planetary exploration](https://arxiv.org/abs/2602.13909v1)**  
  Authors: Alfonso Martínez-Petersen, Levin Gerdes, David Rodríguez-Martínez, C. J. Pérez-del-Pulgar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13909v1.pdf)  
  Keywords: face, localization, nerf, high-fidelity, robotics, motion, gaussian splatting, ar, mapping, efficient, 3d reconstruction, slam  
- **[Joint Orientation and Weight Optimization for Robust Watertight Surface Reconstruction via Dirichlet-Regularized Winding Fields](https://arxiv.org/abs/2602.13801v1)**  
  Authors: Jiaze Li, Daisheng Jin, Fei Hou, Junhui Hou, Zheng Liu, Shiqing Xin, Wenping Wang, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13801v1.pdf)  
  Keywords: face, 3d gaussian, gaussian splatting, ar, efficient  
- **[GSM-GS: Geometry-Constrained Single and Multi-view Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2602.12796v1)**  
  Authors: Xiao Ren, Yu Liu, Ning An, Jian Cheng, Xin Qiao, He Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12796v1.pdf)  
  Keywords: face, high-fidelity, 3d gaussian, dynamic, geometry, gaussian splatting, ar  
- **[GSO-SLAM: Bidirectionally Coupled Gaussian Splatting and Direct Visual Odometry](https://arxiv.org/abs/2602.11714v1)**  
  Authors: Jiung Yeon, Seongbo Ha, Hyeonwoo Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11714v1.pdf)  
  Keywords: head, gaussian splatting, ar, mapping, tracking, slam  
- **[OMEGA-Avatar: One-shot Modeling of 360° Gaussian Avatars](https://arxiv.org/abs/2602.11693v1)**  
  Authors: Zehao Xia, Yiqun Wang, Zhengda Lu, Kai Liu, Jun Xiao, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11693v1.pdf)  
  Keywords: head, deformation, semantic, high-fidelity, 3d gaussian, avatar, ar, mapping, animation  
- **[GR-Diffusion: 3D Gaussian Representation Meets Diffusion in Whole-Body PET Reconstruction](https://arxiv.org/abs/2602.11653v1)**  
  Authors: Mengxiao Geng, Zijie Chen, Ran Hong, Bingxuan Li, Qiegen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11653v1.pdf)  
  Keywords: ar, 3d gaussian, body, efficient  

### Dynamic Scene

*Showing the latest 50 out of 214 papers*

- **[MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction](https://arxiv.org/abs/2602.15733v1)**  
  Authors: Qiang Zhang, Jiahao Ma, Peiran Liu, Shuai Shi, Zeran Su, Zifan Wang, Jingkai Sun, Wei Cui, Jialin Yu, Gang Han, Wen Zhao, Pihai Sun, Kangning Yin, Jiaxu Wang, Jiahang Cao, Lingfeng Zhang, Hao Cheng, Xiaoshuai Hao, Yiding Ji, Junwei Liang, Jian Tang, Renjing Xu, Yijie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15733v1.pdf)  
  Keywords: dynamic, geometry, motion, ar, human  
- **[Semantic-Guided 3D Gaussian Splatting for Transient Object Removal](https://arxiv.org/abs/2602.15516v1)**  
  Authors: Aditi Prabakaran, Priyesh Shukla  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15516v1.pdf)  
  Keywords: head, semantic, nerf, 3d gaussian, real-time rendering, motion, gaussian splatting, ar  
- **[Time-Archival Camera Virtualization for Sports and Visual Performances](https://arxiv.org/abs/2602.15181v1)**  
  Authors: Yunxiao Zhang, William Stone, Suryansh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15181v1.pdf)  
  Keywords: 4d, 3d gaussian, dynamic, neural rendering, fast, motion, gaussian splatting, ar, efficient, tracking  
- **[High-fidelity 3D reconstruction for planetary exploration](https://arxiv.org/abs/2602.13909v1)**  
  Authors: Alfonso Martínez-Petersen, Levin Gerdes, David Rodríguez-Martínez, C. J. Pérez-del-Pulgar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13909v1.pdf)  
  Keywords: face, localization, nerf, high-fidelity, robotics, motion, gaussian splatting, ar, mapping, efficient, 3d reconstruction, slam  
- **[Gaussian Sequences with Multi-Scale Dynamics for 4D Reconstruction from Monocular Casual Videos](https://arxiv.org/abs/2602.13806v1)**  
  Authors: Can Li, Jie Gu, Jingmin Chen, Fangzhou Qiu, Lei Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13806v1.pdf)  
  Keywords: understanding, 4d, 3d gaussian, dynamic, motion, ar  
- **[FlowHOI: Flow-based Semantics-Grounded Generation of Hand-Object Interactions for Dexterous Robot Manipulation](https://arxiv.org/abs/2602.13444v1)**  
  Authors: Huajian Zeng, Lingyun Chen, Jiaqi Yang, Yuantai Zhang, Fan Shi, Peidong Liu, Xingxing Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13444v1.pdf)  
  Keywords: semantic, high-fidelity, 3d gaussian, compact, geometry, motion, gaussian splatting, recognition, ar  
- **[GSM-GS: Geometry-Constrained Single and Multi-view Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2602.12796v1)**  
  Authors: Xiao Ren, Yu Liu, Ning An, Jian Cheng, Xin Qiao, He Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12796v1.pdf)  
  Keywords: face, high-fidelity, 3d gaussian, dynamic, geometry, gaussian splatting, ar  
- **[TG-Field: Geometry-Aware Radiative Gaussian Fields for Tomographic Reconstruction](https://arxiv.org/abs/2602.11705v1)**  
  Authors: Yuxiang Zhong, Jun Wei, Chaoqi Chen, Senyou An, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11705v1.pdf)  
  Keywords: sparse-view, deformation, 3d gaussian, dynamic, geometry, motion, gaussian splatting, ar  
- **[OMEGA-Avatar: One-shot Modeling of 360° Gaussian Avatars](https://arxiv.org/abs/2602.11693v1)**  
  Authors: Zehao Xia, Yiqun Wang, Zhengda Lu, Kai Liu, Jun Xiao, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11693v1.pdf)  
  Keywords: head, deformation, semantic, high-fidelity, 3d gaussian, avatar, ar, mapping, animation  
- **[LeafFit: Plant Assets Creation from 3D Gaussian Splatting](https://arxiv.org/abs/2602.11577v1)**  
  Authors: Chang Luo, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11577v1.pdf)  
  Keywords: deformation, segmentation, 3d gaussian, gaussian splatting, ar, efficient  

### Few-shot

- **[TG-Field: Geometry-Aware Radiative Gaussian Fields for Tomographic Reconstruction](https://arxiv.org/abs/2602.11705v1)**  
  Authors: Yuxiang Zhong, Jun Wei, Chaoqi Chen, Senyou An, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11705v1.pdf)  
  Keywords: sparse-view, deformation, 3d gaussian, dynamic, geometry, motion, gaussian splatting, ar  
- **[Pi-GS: Sparse-View Gaussian Splatting with Dense π^3 Initialization](https://arxiv.org/abs/2602.03327v1)**  
  Authors: Manuel Hofer, Markus Steinberger, Thomas Köhler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03327v1.pdf)  
  Keywords: sparse-view, nerf, 3d gaussian, real-time rendering, motion, gaussian splatting, ar  
- **[LoD-Structured 3D Gaussian Splatting for Streaming Video Reconstruction](https://arxiv.org/abs/2601.18475v1)**  
  Authors: Xinhui Liu, Can Wang, Lei Liu, Zhenghao Chen, Wei Jiang, Wei Wang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18475v1.pdf)  
  Keywords: sparse-view, high-fidelity, 3d gaussian, dynamic, motion, gaussian splatting, ar, efficient  
- **[LGDWT-GS: Local and Global Discrete Wavelet-Regularized 3D Gaussian Splatting for Sparse-View Scene Reconstruction](https://arxiv.org/abs/2601.17185v1)**  
  Authors: Shima Salehi, Atharva Agashe, Andrew J. McFarland, Joshua Peeples  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17185v1.pdf)  
  Keywords: sparse-view, 3d gaussian, geometry, gaussian splatting, ar, few-shot, 3d reconstruction  
- **[FastGHA: Generalized Few-Shot 3D Gaussian Head Avatars with Real-Time Animation](https://arxiv.org/abs/2601.13837v2)**  
  Authors: Xinya Ji, Sebastian Weiss, Manuel Kansy, Jacek Naruniec, Xun Cao, Barbara Solenthaler, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.13837v2.pdf)  
  Keywords: head, deformation, 3d gaussian, dynamic, avatar, fast, geometry, lightweight, ar, efficient, few-shot, animation  
- **[SA-ResGS: Self-Augmented Residual 3D Gaussian Splatting for Next Best View Selection](https://arxiv.org/abs/2601.03024v2)**  
  Authors: Kim Jun-Seong, Tae-Hyun Oh, Eduardo Pérez-Pellitero, Youngkyoon Jang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.03024v2.pdf)  
  Keywords: sparse-view, 3d gaussian, gaussian splatting, ar, efficient  
- **[360-GeoGS: Geometrically Consistent Feed-Forward 3D Gaussian Splatting Reconstruction for 360 Images](https://arxiv.org/abs/2601.02102v1)**  
  Authors: Jiaqi Yao, Zhongmiao Yan, Jingyi Xu, Songpengcheng Xia, Yan Xiang, Ling Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.02102v1.pdf)  
  Keywords: efficient rendering, sparse view, face, robotics, 3d gaussian, neural rendering, gaussian splatting, ar, efficient, 3d reconstruction  
- **[ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2601.00939v1)**  
  Authors: Feng Luo, Hongbo Pan, Xiang Yang, Baoyu Jiang, Fengqing Liu, Tao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00939v1.pdf)  
  Keywords: sparse-view, efficient rendering, 3d gaussian, illumination, gaussian splatting, shadow, ar, efficient, 3d reconstruction, ray marching  
- **[SV-GS: Sparse View 4D Reconstruction with Skeleton-Driven Gaussian Splatting](https://arxiv.org/abs/2601.00285v1)**  
  Authors: Jun-Jee Chao, Volkan Isler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00285v1.pdf)  
  Keywords: deformation, sparse view, 4d, dynamic, motion, gaussian splatting, ar  
- **[3D Scene Change Modeling With Consistent Multi-View Aggregation](https://arxiv.org/abs/2512.22830v1)**  
  Authors: Zirui Zhou, Junfeng Ni, Shujie Zhang, Yixin Chen, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22830v1.pdf)  
  Keywords: sparse-view, ar, dynamic  

### Geometry Reconstruction

*Showing the latest 50 out of 192 papers*

- **[MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction](https://arxiv.org/abs/2602.15733v1)**  
  Authors: Qiang Zhang, Jiahao Ma, Peiran Liu, Shuai Shi, Zeran Su, Zifan Wang, Jingkai Sun, Wei Cui, Jialin Yu, Gang Han, Wen Zhao, Pihai Sun, Kangning Yin, Jiaxu Wang, Jiahang Cao, Lingfeng Zhang, Hao Cheng, Xiaoshuai Hao, Yiding Ji, Junwei Liang, Jian Tang, Renjing Xu, Yijie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15733v1.pdf)  
  Keywords: dynamic, geometry, motion, ar, human  
- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: head, semantic, localization, 3d gaussian, outdoor, geometry, gaussian splatting, ar, mapping, lighting  
- **[Learnable Multi-level Discrete Wavelet Transforms for 3D Gaussian Splatting Frequency Modulation](https://arxiv.org/abs/2602.14199v1)**  
  Authors: Hung Nguyen, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14199v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, 3d gaussian  
- **[High-fidelity 3D reconstruction for planetary exploration](https://arxiv.org/abs/2602.13909v1)**  
  Authors: Alfonso Martínez-Petersen, Levin Gerdes, David Rodríguez-Martínez, C. J. Pérez-del-Pulgar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13909v1.pdf)  
  Keywords: face, localization, nerf, high-fidelity, robotics, motion, gaussian splatting, ar, mapping, efficient, 3d reconstruction, slam  
- **[FlowHOI: Flow-based Semantics-Grounded Generation of Hand-Object Interactions for Dexterous Robot Manipulation](https://arxiv.org/abs/2602.13444v1)**  
  Authors: Huajian Zeng, Lingyun Chen, Jiaqi Yang, Yuantai Zhang, Fan Shi, Peidong Liu, Xingxing Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13444v1.pdf)  
  Keywords: semantic, high-fidelity, 3d gaussian, compact, geometry, motion, gaussian splatting, recognition, ar  
- **[GSM-GS: Geometry-Constrained Single and Multi-view Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2602.12796v1)**  
  Authors: Xiao Ren, Yu Liu, Ning An, Jian Cheng, Xin Qiao, He Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12796v1.pdf)  
  Keywords: face, high-fidelity, 3d gaussian, dynamic, geometry, gaussian splatting, ar  
- **[TG-Field: Geometry-Aware Radiative Gaussian Fields for Tomographic Reconstruction](https://arxiv.org/abs/2602.11705v1)**  
  Authors: Yuxiang Zhong, Jun Wei, Chaoqi Chen, Senyou An, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11705v1.pdf)  
  Keywords: sparse-view, deformation, 3d gaussian, dynamic, geometry, motion, gaussian splatting, ar  
- **[ERGO: Excess-Risk-Guided Optimization for High-Fidelity Monocular 3D Gaussian Splatting](https://arxiv.org/abs/2602.10278v1)**  
  Authors: Zehua Ma, Hanhui Li, Zhenyu Xie, Xiaonan Luo, Michael Kampffmeyer, Feng Gao, Xiaodan Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10278v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, dynamic, geometry, gaussian splatting, ar, 3d reconstruction  
- **[XSPLAIN: XAI-enabling Splat-based Prototype Learning for Attribute-aware INterpretability](https://arxiv.org/abs/2602.10239v1)**  
  Authors: Dominik Galus, Julia Farganus, Tymoteusz Zapala, Mikołaj Czachorowski, Piotr Borycki, Przemysław Spurek, Piotr Syga  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10239v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Solvro/ml-splat-xai?style=social)](https://github.com/Solvro/ml-splat-xai)  
  Keywords: high-fidelity, 3d gaussian, gaussian splatting, ar, 3d reconstruction, vr  
- **[CompSplat: Compression-aware 3D Gaussian Splatting for Real-world Video](https://arxiv.org/abs/2602.09816v1)**  
  Authors: Hojun Song, Heejung Choi, Aro Kim, Chae-yeong Song, Gahyeon Kim, Soo Ye Kim, Jaehyup Lee, Sang-hyo Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09816v1.pdf)  
  Keywords: 3d gaussian, geometry, gaussian splatting, ar, compression  

### Large Scene

- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: head, semantic, localization, 3d gaussian, outdoor, geometry, gaussian splatting, ar, mapping, lighting  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: nerf, 3d gaussian, illumination, real-time rendering, outdoor, gaussian splatting, ar, global illumination, autonomous driving, lighting  
- **[Zero-Shot UAV Navigation in Forests via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2602.07101v2)**  
  Authors: Zinan Lv, Yeqian Qian, Chen Sang, Hao Liu, Danping Zou, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07101v2.pdf)  
  Keywords: high-fidelity, relightable, 3d gaussian, illumination, dynamic, outdoor, geometry, lightweight, gaussian splatting, ar, lighting  
- **[3DGS$^2$-TR: Scalable Second-Order Trust-Region Method for 3D Gaussian Splatting](https://arxiv.org/abs/2602.00395v1)**  
  Authors: Roger Hsiao, Yuchen Fang, Xiangru Huang, Ruilong Li, Hesam Rabeti, Zan Gojcic, Javad Lavaei, James Demmel, Sophia Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00395v1.pdf)  
  Keywords: head, large scene, 3d gaussian, gaussian splatting, ar, efficient  
- **[EVolSplat4D: Efficient Volume-based Gaussian Splatting for 4D Urban Scene Synthesis](https://arxiv.org/abs/2601.15951v1)**  
  Authors: Sheng Miao, Sijin Li, Pan Wang, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15951v1.pdf)  
  Keywords: semantic, urban scene, 4d, 3d gaussian, dynamic, geometry, motion, gaussian splatting, ar, efficient, autonomous driving  
- **[ScenDi: 3D-to-2D Scene Diffusion Cascades for Urban Generation](https://arxiv.org/abs/2601.15221v1)**  
  Authors: Hanlei Guo, Jiahao Shao, Xinya Chen, Xiyang Tan, Sheng Miao, Yujun Shen, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15221v1.pdf)  
  Keywords: urban scene, ar, 3d gaussian  
- **[Clean-GS: Semantic Mask-Guided Pruning for 3D Gaussian Splatting](https://arxiv.org/abs/2601.00913v1)**  
  Authors: Subhankar Mishra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00913v1.pdf) | [![GitHub](https://img.shields.io/github/stars/smlab-niser/clean-gs?style=social)](https://github.com/smlab-niser/clean-gs)  
  Keywords: segmentation, semantic, 3d gaussian, outdoor, gaussian splatting, ar, compression, vr  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: face, urban scene, 3d gaussian, illumination, geometry, gaussian splatting, ar, efficient, 3d reconstruction  
- **[Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries](https://arxiv.org/abs/2512.13796v1)**  
  Authors: Victor Rong, Jan Held, Victor Chu, Daniel Rebain, Marc Van Droogenbroeck, Kiriakos N. Kutulakos, Andrea Tagliasacchi, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13796v1.pdf)  
  Keywords: 3d gaussian, outdoor, compact, fast, geometry, gaussian splatting, ar  
- **[Flux4D: Flow-based Unsupervised 4D Reconstruction](https://arxiv.org/abs/2512.03210v1)**  
  Authors: Jingkang Wang, Henry Che, Yun Chen, Ze Yang, Lily Goli, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03210v1.pdf)  
  Keywords: nerf, 4d, robotics, 3d gaussian, outdoor, dynamic, motion, gaussian splatting, ar, efficient  

### Model Compression

*Showing the latest 50 out of 210 papers*

- **[DAV-GSWT: Diffusion-Active-View Sampling for Data-Efficient Gaussian Splatting Wang Tiles](https://arxiv.org/abs/2602.15355v1)**  
  Authors: Rong Fu, Jiekai Wu, Haiyun Wei, Yee Tan Jia, Wenxin Zhang, Yang Li, Xiaowen Ma, Wangyu Wu, Simon Fong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15355v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, neural rendering, gaussian splatting, ar, efficient  
- **[Time-Archival Camera Virtualization for Sports and Visual Performances](https://arxiv.org/abs/2602.15181v1)**  
  Authors: Yunxiao Zhang, William Stone, Suryansh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15181v1.pdf)  
  Keywords: 4d, 3d gaussian, dynamic, neural rendering, fast, motion, gaussian splatting, ar, efficient, tracking  
- **[Gaussian Mesh Renderer for Lightweight Differentiable Rendering](https://arxiv.org/abs/2602.14493v1)**  
  Authors: Xinpeng Liu, Fumio Okura  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14493v1.pdf) | [![GitHub](https://img.shields.io/github/stars/huntorochi/Gaussian-Mesh-Renderer?style=social)](https://github.com/huntorochi/Gaussian-Mesh-Renderer)  
  Keywords: face, high-fidelity, 3d gaussian, fast, lightweight, gaussian splatting, ar, efficient  
- **[High-fidelity 3D reconstruction for planetary exploration](https://arxiv.org/abs/2602.13909v1)**  
  Authors: Alfonso Martínez-Petersen, Levin Gerdes, David Rodríguez-Martínez, C. J. Pérez-del-Pulgar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13909v1.pdf)  
  Keywords: face, localization, nerf, high-fidelity, robotics, motion, gaussian splatting, ar, mapping, efficient, 3d reconstruction, slam  
- **[Joint Orientation and Weight Optimization for Robust Watertight Surface Reconstruction via Dirichlet-Regularized Winding Fields](https://arxiv.org/abs/2602.13801v1)**  
  Authors: Jiaze Li, Daisheng Jin, Fei Hou, Junhui Hou, Zheng Liu, Shiqing Xin, Wenping Wang, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13801v1.pdf)  
  Keywords: face, 3d gaussian, gaussian splatting, ar, efficient  
- **[FlowHOI: Flow-based Semantics-Grounded Generation of Hand-Object Interactions for Dexterous Robot Manipulation](https://arxiv.org/abs/2602.13444v1)**  
  Authors: Huajian Zeng, Lingyun Chen, Jiaqi Yang, Yuantai Zhang, Fan Shi, Peidong Liu, Xingxing Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13444v1.pdf)  
  Keywords: semantic, high-fidelity, 3d gaussian, compact, geometry, motion, gaussian splatting, recognition, ar  
- **[LatentAM: Real-Time, Large-Scale Latent Gaussian Attention Mapping via Online Dictionary Learning](https://arxiv.org/abs/2602.12314v1)**  
  Authors: Junwoon Lee, Yulun Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12314v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://junwoonlee.github.io/projects/LatentAM)  
  Keywords: semantic, 3d gaussian, compact, gaussian splatting, ar, mapping, efficient  
- **[3DGSNav: Enhancing Vision-Language Model Reasoning for Object Navigation via Active 3D Gaussian Splatting](https://arxiv.org/abs/2602.12159v1)**  
  Authors: Wancai Zheng, Hao Chen, Xianlong Lu, Linlin Ou, Xinyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12159v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/3dgsnav.github.io)  
  Keywords: semantic, 3d gaussian, recognition, gaussian splatting, ar, efficient  
- **[GR-Diffusion: 3D Gaussian Representation Meets Diffusion in Whole-Body PET Reconstruction](https://arxiv.org/abs/2602.11653v1)**  
  Authors: Mengxiao Geng, Zijie Chen, Ran Hong, Bingxuan Li, Qiegen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11653v1.pdf)  
  Keywords: ar, 3d gaussian, body, efficient  
- **[Variation-aware Flexible 3D Gaussian Editing](https://arxiv.org/abs/2602.11638v2)**  
  Authors: Hao Qin, Yukai Sun, Meng Wang, Ming Kong, Mengxu Lu, Qiang Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11638v2.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, efficient  

### Quality Enhancement

*Showing the latest 50 out of 129 papers*

- **[DAV-GSWT: Diffusion-Active-View Sampling for Data-Efficient Gaussian Splatting Wang Tiles](https://arxiv.org/abs/2602.15355v1)**  
  Authors: Rong Fu, Jiekai Wu, Haiyun Wei, Yee Tan Jia, Wenxin Zhang, Yang Li, Xiaowen Ma, Wangyu Wu, Simon Fong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15355v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, neural rendering, gaussian splatting, ar, efficient  
- **[Gaussian Mesh Renderer for Lightweight Differentiable Rendering](https://arxiv.org/abs/2602.14493v1)**  
  Authors: Xinpeng Liu, Fumio Okura  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14493v1.pdf) | [![GitHub](https://img.shields.io/github/stars/huntorochi/Gaussian-Mesh-Renderer?style=social)](https://github.com/huntorochi/Gaussian-Mesh-Renderer)  
  Keywords: face, high-fidelity, 3d gaussian, fast, lightweight, gaussian splatting, ar, efficient  
- **[High-fidelity 3D reconstruction for planetary exploration](https://arxiv.org/abs/2602.13909v1)**  
  Authors: Alfonso Martínez-Petersen, Levin Gerdes, David Rodríguez-Martínez, C. J. Pérez-del-Pulgar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13909v1.pdf)  
  Keywords: face, localization, nerf, high-fidelity, robotics, motion, gaussian splatting, ar, mapping, efficient, 3d reconstruction, slam  
- **[FlowHOI: Flow-based Semantics-Grounded Generation of Hand-Object Interactions for Dexterous Robot Manipulation](https://arxiv.org/abs/2602.13444v1)**  
  Authors: Huajian Zeng, Lingyun Chen, Jiaqi Yang, Yuantai Zhang, Fan Shi, Peidong Liu, Xingxing Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13444v1.pdf)  
  Keywords: semantic, high-fidelity, 3d gaussian, compact, geometry, motion, gaussian splatting, recognition, ar  
- **[GSM-GS: Geometry-Constrained Single and Multi-view Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2602.12796v1)**  
  Authors: Xiao Ren, Yu Liu, Ning An, Jian Cheng, Xin Qiao, He Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12796v1.pdf)  
  Keywords: face, high-fidelity, 3d gaussian, dynamic, geometry, gaussian splatting, ar  
- **[OMEGA-Avatar: One-shot Modeling of 360° Gaussian Avatars](https://arxiv.org/abs/2602.11693v1)**  
  Authors: Zehao Xia, Yiqun Wang, Zhengda Lu, Kai Liu, Jun Xiao, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11693v1.pdf)  
  Keywords: head, deformation, semantic, high-fidelity, 3d gaussian, avatar, ar, mapping, animation  
- **[ERGO: Excess-Risk-Guided Optimization for High-Fidelity Monocular 3D Gaussian Splatting](https://arxiv.org/abs/2602.10278v1)**  
  Authors: Zehua Ma, Hanhui Li, Zhenyu Xie, Xiaonan Luo, Michael Kampffmeyer, Feng Gao, Xiaodan Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10278v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, dynamic, geometry, gaussian splatting, ar, 3d reconstruction  
- **[XSPLAIN: XAI-enabling Splat-based Prototype Learning for Attribute-aware INterpretability](https://arxiv.org/abs/2602.10239v1)**  
  Authors: Dominik Galus, Julia Farganus, Tymoteusz Zapala, Mikołaj Czachorowski, Piotr Borycki, Przemysław Spurek, Piotr Syga  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10239v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Solvro/ml-splat-xai?style=social)](https://github.com/Solvro/ml-splat-xai)  
  Keywords: high-fidelity, 3d gaussian, gaussian splatting, ar, 3d reconstruction, vr  
- **[Toward Fine-Grained Facial Control in 3D Talking Head Generation](https://arxiv.org/abs/2602.09736v1)**  
  Authors: Shaoyang Xie, Xiaofeng Cong, Baosheng Yu, Zhipeng Gui, Jie Gui, Yuan Yan Tang, James Tin-Yau Kwok  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09736v1.pdf)  
  Keywords: head, high-fidelity, 3d gaussian, dynamic, real-time rendering, avatar, motion, gaussian splatting, ar  
- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2602.06846v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06846v1.pdf)  
  Keywords: head, semantic, high-fidelity, 4d, reflection, 3d gaussian, dynamic, geometry, motion, gaussian splatting, ar, vr  

### Ray Tracing

- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: nerf, 3d gaussian, illumination, real-time rendering, outdoor, gaussian splatting, ar, global illumination, autonomous driving, lighting  
- **[Rotated Lights for Consistent and Efficient 2D Gaussians Inverse Rendering](https://arxiv.org/abs/2602.08724v1)**  
  Authors: Geng Lin, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08724v1.pdf)  
  Keywords: relighting, illumination, geometry, gaussian splatting, shadow, ar, efficient, global illumination, lighting  
- **[Radioactive 3D Gaussian Ray Tracing for Tomographic Reconstruction](https://arxiv.org/abs/2602.01057v1)**  
  Authors: Ling Chen, Bao Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01057v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, ray tracing  
- **[EAG-PT: Emission-Aware Gaussians and Path Tracing for Indoor Scene Reconstruction and Editing](https://arxiv.org/abs/2601.23065v1)**  
  Authors: Xijie Yang, Mulin Yu, Changjian Jiang, Kerui Ren, Tao Lu, Jiangmiao Pang, Dahua Lin, Bo Dai, Linning Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.23065v1.pdf)  
  Keywords: path tracing, nerf, illumination, geometry, ar, efficient, light transport  
- **[Hybrid Foveated Path Tracing with Peripheral Gaussians for Immersive Anatomy](https://arxiv.org/abs/2601.22026v1)**  
  Authors: Constantin Kleinbeck, Luisa Theelke, Hannah Schieber, Ulrich Eck, Rüdiger von Eisenhart-Rothe, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22026v1.pdf)  
  Keywords: head, understanding, path tracing, lightweight, gaussian splatting, ar, medical, vr  
- **[GRTX: Efficient Ray Tracing for 3D Gaussian-Based Rendering](https://arxiv.org/abs/2601.20429v1)**  
  Authors: Junseo Lee, Sangyun Jeon, Jungi Lee, Junyong Park, Jaewoong Sim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20429v1.pdf)  
  Keywords: head, acceleration, 3d gaussian, gaussian splatting, ar, efficient, ray tracing  
- **[ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2601.00939v1)**  
  Authors: Feng Luo, Hongbo Pan, Xiang Yang, Baoyu Jiang, Fengqing Liu, Tao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00939v1.pdf)  
  Keywords: sparse-view, efficient rendering, 3d gaussian, illumination, gaussian splatting, shadow, ar, efficient, 3d reconstruction, ray marching  
- **[Geometric-Photometric Event-based 3D Gaussian Ray Tracing](https://arxiv.org/abs/2512.18640v1)**  
  Authors: Kai Kohyama, Yoshimitsu Aoki, Guillermo Gallego, Shintaro Shiba  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18640v1.pdf)  
  Keywords: understanding, 3d gaussian, fast, geometry, gaussian splatting, motion, ar, 3d reconstruction, ray tracing  
- **[MatSpray: Fusing 2D Material World Knowledge on 3D Geometry](https://arxiv.org/abs/2512.18314v1)**  
  Authors: Philipp Langsteiner, Jan-Niklas Dihlmann, Hendrik P. A. Lensch  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.18314v1.pdf)  
  Keywords: relightable, geometry, gaussian splatting, ar, 3d reconstruction, lighting, ray tracing, relighting  
- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: face, nerf, 3d gaussian, fast, gaussian splatting, ar, ray tracing  

### Relighting

*Showing the latest 50 out of 65 papers*

- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: head, semantic, localization, 3d gaussian, outdoor, geometry, gaussian splatting, ar, mapping, lighting  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: nerf, 3d gaussian, illumination, real-time rendering, outdoor, gaussian splatting, ar, global illumination, autonomous driving, lighting  
- **[Rotated Lights for Consistent and Efficient 2D Gaussians Inverse Rendering](https://arxiv.org/abs/2602.08724v1)**  
  Authors: Geng Lin, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08724v1.pdf)  
  Keywords: relighting, illumination, geometry, gaussian splatting, shadow, ar, efficient, global illumination, lighting  
- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2602.06846v1)**  
  Authors: Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06846v1.pdf)  
  Keywords: head, semantic, high-fidelity, 4d, reflection, 3d gaussian, dynamic, geometry, motion, gaussian splatting, ar, vr  
- **[Zero-Shot UAV Navigation in Forests via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2602.07101v2)**  
  Authors: Zinan Lv, Yeqian Qian, Chen Sang, Hao Liu, Danping Zou, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07101v2.pdf)  
  Keywords: high-fidelity, relightable, 3d gaussian, illumination, dynamic, outdoor, geometry, lightweight, gaussian splatting, ar, lighting  
- **[NVS-HO: A Benchmark for Novel View Synthesis of Handheld Objects](https://arxiv.org/abs/2602.05822v1)**  
  Authors: Musawar Ali, Manuel Carranza-García, Nicola Fioraio, Samuele Salti, Luigi Di Stefano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05822v1.pdf)  
  Keywords: nerf, gaussian splatting, ar, lighting  
- **[QuantumGS: Quantum Encoding Framework for Gaussian Splatting](https://arxiv.org/abs/2602.05047v1)**  
  Authors: Grzegorz Wilczyński, Rafał Tobiasz, Paweł Gora, Marcin Mazur, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05047v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/QuantumGS?style=social)](https://github.com/gwilczynski95/QuantumGS)  
  Keywords: reflection, 3d gaussian, real-time rendering, neural rendering, geometry, gaussian splatting, ar  
- **[JOintGS: Joint Optimization of Cameras, Bodies and 3D Gaussians for In-the-Wild Monocular Reconstruction](https://arxiv.org/abs/2602.04317v1)**  
  Authors: Zihan Lou, Jinlong Fan, Sihan Ma, Yuxiang Yang, Jing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04317v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MiliLab/JOintGS?style=social)](https://github.com/MiliLab/JOintGS)  
  Keywords: deformation, high-fidelity, 3d gaussian, illumination, dynamic, real-time rendering, avatar, ar, body, human  
- **[Position: 3D Gaussian Splatting Watermarking Should Be Scenario-Driven and Threat-Model Explicit](https://arxiv.org/abs/2602.02602v1)**  
  Authors: Yangfan Deng, Anirudh Nakra, Min Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02602v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, gaussian splatting, ar, lighting  
- **[EAG-PT: Emission-Aware Gaussians and Path Tracing for Indoor Scene Reconstruction and Editing](https://arxiv.org/abs/2601.23065v1)**  
  Authors: Xijie Yang, Mulin Yu, Changjian Jiang, Kerui Ren, Tao Lu, Jiangmiao Pang, Dahua Lin, Bo Dai, Linning Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.23065v1.pdf)  
  Keywords: path tracing, nerf, illumination, geometry, ar, efficient, light transport  

### SLAM

*Showing the latest 50 out of 77 papers*

- **[Time-Archival Camera Virtualization for Sports and Visual Performances](https://arxiv.org/abs/2602.15181v1)**  
  Authors: Yunxiao Zhang, William Stone, Suryansh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15181v1.pdf)  
  Keywords: 4d, 3d gaussian, dynamic, neural rendering, fast, motion, gaussian splatting, ar, efficient, tracking  
- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: head, semantic, localization, 3d gaussian, outdoor, geometry, gaussian splatting, ar, mapping, lighting  
- **[High-fidelity 3D reconstruction for planetary exploration](https://arxiv.org/abs/2602.13909v1)**  
  Authors: Alfonso Martínez-Petersen, Levin Gerdes, David Rodríguez-Martínez, C. J. Pérez-del-Pulgar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13909v1.pdf)  
  Keywords: face, localization, nerf, high-fidelity, robotics, motion, gaussian splatting, ar, mapping, efficient, 3d reconstruction, slam  
- **[LatentAM: Real-Time, Large-Scale Latent Gaussian Attention Mapping via Online Dictionary Learning](https://arxiv.org/abs/2602.12314v1)**  
  Authors: Junwoon Lee, Yulun Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12314v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://junwoonlee.github.io/projects/LatentAM)  
  Keywords: semantic, 3d gaussian, compact, gaussian splatting, ar, mapping, efficient  
- **[GSO-SLAM: Bidirectionally Coupled Gaussian Splatting and Direct Visual Odometry](https://arxiv.org/abs/2602.11714v1)**  
  Authors: Jiung Yeon, Seongbo Ha, Hyeonwoo Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11714v1.pdf)  
  Keywords: head, gaussian splatting, ar, mapping, tracking, slam  
- **[OMEGA-Avatar: One-shot Modeling of 360° Gaussian Avatars](https://arxiv.org/abs/2602.11693v1)**  
  Authors: Zehao Xia, Yiqun Wang, Zhengda Lu, Kai Liu, Jun Xiao, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11693v1.pdf)  
  Keywords: head, deformation, semantic, high-fidelity, 3d gaussian, avatar, ar, mapping, animation  
- **[GaussianCaR: Gaussian Splatting for Efficient Camera-Radar Fusion](https://arxiv.org/abs/2602.08784v1)**  
  Authors: Santiago Montiel-Marín, Miguel Antunes-García, Fabio Sánchez-García, Angel Llamazares, Holger Caesar, Luis M. Bergasa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08784v1.pdf)  
  Keywords: segmentation, dynamic, fast, gaussian splatting, ar, mapping, efficient  
- **[Thermal odometry and dense mapping using learned odometry and Gaussian splatting](https://arxiv.org/abs/2602.07493v2)**  
  Authors: Tianhao Zhou, Yujia Chen, Zhihao Zhan, Yuhang Ming, Jianzhu Huai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07493v2.pdf)  
  Keywords: robotics, motion, gaussian splatting, ar, mapping, slam  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: face, localization, survey, 3d gaussian, dynamic, motion, gaussian splatting, ar, mapping, efficient, tracking, slam  
- **[CloDS: Visual-Only Unsupervised Cloth Dynamics Learning in Unknown Conditions](https://arxiv.org/abs/2602.01844v1)**  
  Authors: Yuliang Zhan, Jian Li, Wenbing Huang, Wenbing Huang, Yang Liu, Hao Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01844v1.pdf) | [![GitHub](https://img.shields.io/github/stars/whynot-zyl/CloDS?style=social)](https://github.com/whynot-zyl/CloDS)  
  Keywords: deformation, dynamic, geometry, gaussian splatting, ar, mapping  

### Scene Understanding

*Showing the latest 50 out of 124 papers*

- **[Semantic-Guided 3D Gaussian Splatting for Transient Object Removal](https://arxiv.org/abs/2602.15516v1)**  
  Authors: Aditi Prabakaran, Priyesh Shukla  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15516v1.pdf)  
  Keywords: head, semantic, nerf, 3d gaussian, real-time rendering, motion, gaussian splatting, ar  
- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: head, semantic, localization, 3d gaussian, outdoor, geometry, gaussian splatting, ar, mapping, lighting  
- **[Gaussian Sequences with Multi-Scale Dynamics for 4D Reconstruction from Monocular Casual Videos](https://arxiv.org/abs/2602.13806v1)**  
  Authors: Can Li, Jie Gu, Jingmin Chen, Fangzhou Qiu, Lei Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13806v1.pdf)  
  Keywords: understanding, 4d, 3d gaussian, dynamic, motion, ar  
- **[FlowHOI: Flow-based Semantics-Grounded Generation of Hand-Object Interactions for Dexterous Robot Manipulation](https://arxiv.org/abs/2602.13444v1)**  
  Authors: Huajian Zeng, Lingyun Chen, Jiaqi Yang, Yuantai Zhang, Fan Shi, Peidong Liu, Xingxing Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13444v1.pdf)  
  Keywords: semantic, high-fidelity, 3d gaussian, compact, geometry, motion, gaussian splatting, recognition, ar  
- **[LatentAM: Real-Time, Large-Scale Latent Gaussian Attention Mapping via Online Dictionary Learning](https://arxiv.org/abs/2602.12314v1)**  
  Authors: Junwoon Lee, Yulun Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12314v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://junwoonlee.github.io/projects/LatentAM)  
  Keywords: semantic, 3d gaussian, compact, gaussian splatting, ar, mapping, efficient  
- **[3DGSNav: Enhancing Vision-Language Model Reasoning for Object Navigation via Active 3D Gaussian Splatting](https://arxiv.org/abs/2602.12159v1)**  
  Authors: Wancai Zheng, Hao Chen, Xianlong Lu, Linlin Ou, Xinyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12159v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/3dgsnav.github.io)  
  Keywords: semantic, 3d gaussian, recognition, gaussian splatting, ar, efficient  
- **[OMEGA-Avatar: One-shot Modeling of 360° Gaussian Avatars](https://arxiv.org/abs/2602.11693v1)**  
  Authors: Zehao Xia, Yiqun Wang, Zhengda Lu, Kai Liu, Jun Xiao, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11693v1.pdf)  
  Keywords: head, deformation, semantic, high-fidelity, 3d gaussian, avatar, ar, mapping, animation  
- **[LeafFit: Plant Assets Creation from 3D Gaussian Splatting](https://arxiv.org/abs/2602.11577v1)**  
  Authors: Chang Luo, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11577v1.pdf)  
  Keywords: deformation, segmentation, 3d gaussian, gaussian splatting, ar, efficient  
- **[ArtisanGS: Interactive Tools for Gaussian Splat Selection with AI and Human in the Loop](https://arxiv.org/abs/2602.10173v1)**  
  Authors: Clement Fuji Tsang, Anita Hu, Or Perel, Carsten Kolve, Maria Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10173v1.pdf)  
  Keywords: segmentation, 3d gaussian, fast, ar, human, animation  
- **[GaussianCaR: Gaussian Splatting for Efficient Camera-Radar Fusion](https://arxiv.org/abs/2602.08784v1)**  
  Authors: Santiago Montiel-Marín, Miguel Antunes-García, Fabio Sánchez-García, Angel Llamazares, Holger Caesar, Luis M. Bergasa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08784v1.pdf)  
  Keywords: segmentation, dynamic, fast, gaussian splatting, ar, mapping, efficient  



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