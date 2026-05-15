# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-05-15 02:07:40

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

- [3DGS Surveys](#3dgs-surveys) (4 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (101 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (168 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (186 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (48 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (219 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (18 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (200 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (115 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (14 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (64 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (81 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (120 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[ReefMapGS: Enabling Large-Scale Underwater Reconstruction by Closing the Loop Between Multimodal SLAM and Gaussian Splatting](https://arxiv.org/abs/2604.11992v1)**  
  Authors: Daniel Yang, Jungseok Hong, John J. Leonard, Yogesh Girdhar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11992v1.pdf)  
  Keywords: ar, geometry, motion, 3d gaussian, gaussian splatting, efficient, tracking, survey, 3d reconstruction, slam  
- **[A Survey of Spatial Memory Representations for Efficient Robot Navigation](https://arxiv.org/abs/2604.16482v1)**  
  Authors: Ma. Madecheen S. Pangaliman, Steven S. Sison, Erwin P. Quilloy, Rowel Atienza  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.16482v1.pdf)  
  Keywords: ar, semantic, efficient, survey, slam  
- **[Nevis Digital Twin: Photogrammetry and Immersive Visualization of Historical Sites](https://arxiv.org/abs/2603.20560v1)**  
  Authors: Alex Apffel, Huy Tran, Vuthea Chheang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20560v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, vr, survey  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awareness](https://arxiv.org/abs/2603.17499v6)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v6.pdf) | [![GitHub](https://img.shields.io/github/stars/UNIC-Lab/Awesome-Radio-Map-Categorized?style=social)](https://github.com/UNIC-Lab/Awesome-Radio-Map-Categorized)  
  Keywords: ar, mapping, 3d gaussian, gaussian splatting, ray tracing, survey  

### Acceleration

*Showing the latest 50 out of 101 papers*

- **[BlitzGS: City-Scale Gaussian Splatting at Lightning Speed](https://arxiv.org/abs/2605.13794v1)**  
  Authors: Zhongtao Wang, Huishan Au, Yilong Li, Mai Su, Haojie Jin, Yisong Chen, Meng Gai, Fei Zhu, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13794v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AkierRaee/BlitzGS?style=social)](https://github.com/AkierRaee/BlitzGS)  
  Keywords: fast, ar, gaussian splatting  
- **[Sparse Code Uplifting for Efficient 3D Language Gaussian Splatting](https://arxiv.org/abs/2605.13600v1)**  
  Authors: Lovre Antonio Budimir, Yushi Guan, Steve Ryhner, Sven Lončarić, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13600v1.pdf)  
  Keywords: fast, ar, semantic, 3d gaussian, gaussian splatting, efficient, understanding, compact  
- **[Z-Order Transformer for Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2605.13465v1)**  
  Authors: Can Wang, Lei Liu, Wei Jiang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13465v1.pdf)  
  Keywords: fast, ar, semantic, 3d gaussian, gaussian splatting, efficient  
- **[PointForward: Feedforward Driving Reconstruction through Point-Aligned Representations](https://arxiv.org/abs/2605.11594v1)**  
  Authors: Cheng Chi, Xianqi Wang, Hongcheng Luo, Mingfei Tu, Gangwei Xu, Zehan Zhang, Bing Wang, Guang Chen, Hangjun Ye, Sida Peng, Xin Yang, Haiyang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11594v1.pdf)  
  Keywords: fast, high-fidelity, ar, motion, 3d gaussian, gaussian splatting, dynamic, autonomous driving  
- **[3DGS$^3$: Joint Super Sampling and Frame Interpolation for Real-Time Large-Scale 3DGS Rendering](https://arxiv.org/abs/2605.11489v1)**  
  Authors: Yibo Zhao, Fan Gao, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11489v1.pdf)  
  Keywords: high-fidelity, ar, acceleration, lightweight, 3d gaussian, gaussian splatting, efficient, face, compact  
- **[PG-3DGS: Optimizing 3D Gaussian Splatting to Satisfy Physics Objectives](https://arxiv.org/abs/2605.11266v1)**  
  Authors: Zachary Lee, Maxwell Jacobson, Yexiang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11266v1.pdf)  
  Keywords: fast, high-fidelity, ar, 3d gaussian, gaussian splatting, dynamic, understanding  
- **[PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.10307v1)**  
  Authors: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10307v1.pdf)  
  Keywords: fast, high-fidelity, 4d, ar, motion, gaussian splatting, deformation, dynamic, tracking, segmentation, robotics  
- **[CAGS: Color-Adaptive Volumetric Video Streaming with Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2605.09279v1)**  
  Authors: Daheng Yin, Yili Jin, Jianxin Shi, Isaac Ding, Miao Zhang, Fangxin Wang, Zhaowu Huang, Cong Zhang, Jiangchuan Liu, Fang Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.09279v1.pdf)  
  Keywords: fast, ar, 3d gaussian, gaussian splatting, compression, dynamic, face  
- **[AdpSplit: Error-Driven Adaptive Splitting for Faster Geometry Discovery in 3D Gaussian Splatting](https://arxiv.org/abs/2605.06876v1)**  
  Authors: Yongjae Lee, Jingxing Li, Abhay Kumar Yadav, Rama Chellappa, Deliang Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.06876v1.pdf)  
  Keywords: fast, ar, geometry, 3d gaussian, gaussian splatting, efficient, nerf, acceleration  
- **[ULF-Loc: Unbiased Landmark Feature for Robust Visual Localization with 3D Gaussian Splatting](https://arxiv.org/abs/2605.04730v1)**  
  Authors: Yingdong Gu, Shaocheng Yan, Zhenjun Zhao, Yuan Kou, Jianxin Luo, Pengcheng Shi, Jiayuan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04730v1.pdf)  
  Keywords: localization, ar, geometry, efficient rendering, 3d gaussian, gaussian splatting, efficient  

### Applications

*Showing the latest 50 out of 498 papers*

- **[3D Skew-Normal Splatting](https://arxiv.org/abs/2605.15010v1)**  
  Authors: Xiangru Wu, Ke Fan, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15010v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, efficient, face, compact  
- **[Denoising-GS: Gaussian Splatting with Spatial-aware Denoising](https://arxiv.org/abs/2605.14880v1)**  
  Authors: Qingyuan Zhou, Xinyi Liu, Weidong Yang, Ning Wang, Shuquan Ye, Ben Fei, Ying He, Wanli Ouyang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14880v1.pdf)  
  Keywords: high-fidelity, ar, motion, 3d gaussian, gaussian splatting, compact  
- **[Efficient Dense Matching for Enhanced Gaussian Splatting Using AV1 Motion Vectors](https://arxiv.org/abs/2605.14629v1)**  
  Authors: Julien Zouein, Vibhoothi Vibhoothi, François Pitié, Anil Kokaram  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14629v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sigmedia.tv/AV1-3DGS.github.io)  
  Keywords: ar, motion, 3d gaussian, gaussian splatting, head, efficient, nerf  
- **[Towards Accurate Single Panoramic 3D Detection: A Semantic Gaussian Centric Approach](https://arxiv.org/abs/2605.14601v1)**  
  Authors: Kanglin Ning, Yiran Zhao, Wenrui Li, Shaoru Sun, Xingtao Wang, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14601v1.pdf)  
  Keywords: ar, mapping, semantic, head, 3d gaussian, understanding  
- **[PanoPlane: Plane-Aware Panoramic Completion for Sparse-View Indoor 3D Gaussian Splatting](https://arxiv.org/abs/2605.14135v1)**  
  Authors: Adil Qureshi, Dongki Jung, Jaehoon Choi, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14135v1.pdf)  
  Keywords: high-fidelity, ar, geometry, sparse-view, 3d gaussian, gaussian splatting, face  
- **[BlitzGS: City-Scale Gaussian Splatting at Lightning Speed](https://arxiv.org/abs/2605.13794v1)**  
  Authors: Zhongtao Wang, Huishan Au, Yilong Li, Mai Su, Haojie Jin, Yisong Chen, Meng Gai, Fei Zhu, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13794v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AkierRaee/BlitzGS?style=social)](https://github.com/AkierRaee/BlitzGS)  
  Keywords: fast, ar, gaussian splatting  
- **[Sparse Code Uplifting for Efficient 3D Language Gaussian Splatting](https://arxiv.org/abs/2605.13600v1)**  
  Authors: Lovre Antonio Budimir, Yushi Guan, Steve Ryhner, Sven Lončarić, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13600v1.pdf)  
  Keywords: fast, ar, semantic, 3d gaussian, gaussian splatting, efficient, understanding, compact  
- **[Real2Sim: A Physics-driven and Editable Gaussian Splatting Framework for Autonomous Driving Scenes](https://arxiv.org/abs/2605.13591v1)**  
  Authors: Kaicong Huang, Talha Azfar, Weisong Shi, Ruimin Ke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13591v1.pdf)  
  Keywords: high-fidelity, 4d, ar, gaussian splatting, dynamic, autonomous driving, tracking  
- **[Z-Order Transformer for Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2605.13465v1)**  
  Authors: Can Wang, Lei Liu, Wei Jiang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13465v1.pdf)  
  Keywords: fast, ar, semantic, 3d gaussian, gaussian splatting, efficient  
- **[RoSplat: Robust Feed-Forward Pixel-wise Gaussian Splatting for Varying Input Views and High-Resolution Rendering](https://arxiv.org/abs/2605.13093v1)**  
  Authors: Hoang Chuong Nguyen, Renjie Wu, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13093v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 168 papers*

- **[3D Skew-Normal Splatting](https://arxiv.org/abs/2605.15010v1)**  
  Authors: Xiangru Wu, Ke Fan, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15010v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, efficient, face, compact  
- **[Efficient Dense Matching for Enhanced Gaussian Splatting Using AV1 Motion Vectors](https://arxiv.org/abs/2605.14629v1)**  
  Authors: Julien Zouein, Vibhoothi Vibhoothi, François Pitié, Anil Kokaram  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14629v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sigmedia.tv/AV1-3DGS.github.io)  
  Keywords: ar, motion, 3d gaussian, gaussian splatting, head, efficient, nerf  
- **[Towards Accurate Single Panoramic 3D Detection: A Semantic Gaussian Centric Approach](https://arxiv.org/abs/2605.14601v1)**  
  Authors: Kanglin Ning, Yiran Zhao, Wenrui Li, Shaoru Sun, Xingtao Wang, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14601v1.pdf)  
  Keywords: ar, mapping, semantic, head, 3d gaussian, understanding  
- **[PanoPlane: Plane-Aware Panoramic Completion for Sparse-View Indoor 3D Gaussian Splatting](https://arxiv.org/abs/2605.14135v1)**  
  Authors: Adil Qureshi, Dongki Jung, Jaehoon Choi, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14135v1.pdf)  
  Keywords: high-fidelity, ar, geometry, sparse-view, 3d gaussian, gaussian splatting, face  
- **[Revisiting Photometric Ambiguity for Accurate Gaussian-Splatting Surface Reconstruction](https://arxiv.org/abs/2605.12494v1)**  
  Authors: Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Xiaohan Yu, Lin Gu, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12494v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fictionarry.github.io/AmbiSuR-Proj)  
  Keywords: ar, geometry, gaussian splatting, 3d reconstruction, face  
- **[3D Gaussian Splatting for Efficient Retrospective Dynamic Scene Novel View Synthesis with a Standardized Benchmark](https://arxiv.org/abs/2605.12437v1)**  
  Authors: Yunxiao Zhang, Suryansh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12437v1.pdf)  
  Keywords: ar, motion, 3d gaussian, gaussian splatting, deformation, dynamic, efficient, nerf, body  
- **[PointGS: Semantic-Consistent Unsupervised 3D Point Cloud Segmentation with 3D Gaussian Splatting](https://arxiv.org/abs/2605.11520v1)**  
  Authors: Yixiao Song, Qingyong Li, Wen Wang, Zhicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11520v1.pdf)  
  Keywords: ar, semantic, 3d gaussian, gaussian splatting, autonomous driving, segmentation, face  
- **[3DGS$^3$: Joint Super Sampling and Frame Interpolation for Real-Time Large-Scale 3DGS Rendering](https://arxiv.org/abs/2605.11489v1)**  
  Authors: Yibo Zhao, Fan Gao, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11489v1.pdf)  
  Keywords: high-fidelity, ar, acceleration, lightweight, 3d gaussian, gaussian splatting, efficient, face, compact  
- **[VidSplat: Gaussian Splatting Reconstruction with Geometry-Guided Video Diffusion Priors](https://arxiv.org/abs/2605.11424v1)**  
  Authors: Jimin Tang, Wenyuan Zhang, Junsheng Zhou, Zian Huang, Kanle Shi, Shenkun Xu, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11424v1.pdf)  
  Keywords: ar, geometry, sparse-view, gaussian splatting, face  
- **[Forecast-aware Gaussian Splatting for Predictive 3D Representation in Language-Guided Pick-and-Place Manipulation](https://arxiv.org/abs/2605.11144v1)**  
  Authors: Kaixin Jia, Jiacheng Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11144v1.pdf)  
  Keywords: ar, human, semantic, gaussian splatting, understanding  

### Dynamic Scene

*Showing the latest 50 out of 186 papers*

- **[Denoising-GS: Gaussian Splatting with Spatial-aware Denoising](https://arxiv.org/abs/2605.14880v1)**  
  Authors: Qingyuan Zhou, Xinyi Liu, Weidong Yang, Ning Wang, Shuquan Ye, Ben Fei, Ying He, Wanli Ouyang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14880v1.pdf)  
  Keywords: high-fidelity, ar, motion, 3d gaussian, gaussian splatting, compact  
- **[Efficient Dense Matching for Enhanced Gaussian Splatting Using AV1 Motion Vectors](https://arxiv.org/abs/2605.14629v1)**  
  Authors: Julien Zouein, Vibhoothi Vibhoothi, François Pitié, Anil Kokaram  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14629v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sigmedia.tv/AV1-3DGS.github.io)  
  Keywords: ar, motion, 3d gaussian, gaussian splatting, head, efficient, nerf  
- **[Real2Sim: A Physics-driven and Editable Gaussian Splatting Framework for Autonomous Driving Scenes](https://arxiv.org/abs/2605.13591v1)**  
  Authors: Kaicong Huang, Talha Azfar, Weisong Shi, Ruimin Ke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13591v1.pdf)  
  Keywords: high-fidelity, 4d, ar, gaussian splatting, dynamic, autonomous driving, tracking  
- **[3D Gaussian Splatting for Efficient Retrospective Dynamic Scene Novel View Synthesis with a Standardized Benchmark](https://arxiv.org/abs/2605.12437v1)**  
  Authors: Yunxiao Zhang, Suryansh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12437v1.pdf)  
  Keywords: ar, motion, 3d gaussian, gaussian splatting, deformation, dynamic, efficient, nerf, body  
- **[PointForward: Feedforward Driving Reconstruction through Point-Aligned Representations](https://arxiv.org/abs/2605.11594v1)**  
  Authors: Cheng Chi, Xianqi Wang, Hongcheng Luo, Mingfei Tu, Gangwei Xu, Zehan Zhang, Bing Wang, Guang Chen, Hangjun Ye, Sida Peng, Xin Yang, Haiyang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11594v1.pdf)  
  Keywords: fast, high-fidelity, ar, motion, 3d gaussian, gaussian splatting, dynamic, autonomous driving  
- **[PD-4DGS:Progressive Decomposition of 4D Gaussian Splatting for Bandwidth-Adaptive Dynamic Scene Streaming](https://arxiv.org/abs/2605.11427v1)**  
  Authors: Jiachen Li, Guangzhi Han, Jin Wan, Delong Han, Yuan Gao, Min Li, Mingle Zhou, Gang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11427v1.pdf)  
  Keywords: 4d, ar, motion, gaussian splatting, compression, deformation, dynamic  
- **[PG-3DGS: Optimizing 3D Gaussian Splatting to Satisfy Physics Objectives](https://arxiv.org/abs/2605.11266v1)**  
  Authors: Zachary Lee, Maxwell Jacobson, Yexiang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11266v1.pdf)  
  Keywords: fast, high-fidelity, ar, 3d gaussian, gaussian splatting, dynamic, understanding  
- **[DySurface: Consistent 4D Surface Reconstruction via Bridging Explicit Gaussians and Implicit Functions](https://arxiv.org/abs/2605.10360v2)**  
  Authors: Minje Kim, Younghyun Noh, Jaesoon Kim, Tae-Kyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10360v2.pdf)  
  Keywords: 4d, ar, 3d gaussian, gaussian splatting, deformation, dynamic, nerf, face  
- **[PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.10307v1)**  
  Authors: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10307v1.pdf)  
  Keywords: fast, high-fidelity, 4d, ar, motion, gaussian splatting, deformation, dynamic, tracking, segmentation, robotics  
- **[SDTalk: Structured Facial Priors and Dual-Branch Motion Fields for Generalizable Gaussian Talking Head Synthesis](https://arxiv.org/abs/2605.09956v1)**  
  Authors: Peng Jia, Zhen Xiao, Jia Li, Xueliang Liu, Zhenzhen Hu, Lingyun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.09956v1.pdf)  
  Keywords: ar, motion, 3d gaussian, gaussian splatting, head, dynamic  

### Few-shot

- **[PanoPlane: Plane-Aware Panoramic Completion for Sparse-View Indoor 3D Gaussian Splatting](https://arxiv.org/abs/2605.14135v1)**  
  Authors: Adil Qureshi, Dongki Jung, Jaehoon Choi, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14135v1.pdf)  
  Keywords: high-fidelity, ar, geometry, sparse-view, 3d gaussian, gaussian splatting, face  
- **[GeoQuery: Geometry-Query Diffusion for Sparse-View Reconstruction](https://arxiv.org/abs/2605.12399v1)**  
  Authors: Xiao Cao, Yuze Li, Youmin Zhang, Jiayu Song, Cheng Yan, Wen Li, Lixin Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12399v1.pdf)  
  Keywords: ar, geometry, sparse-view, 3d gaussian, gaussian splatting, 3d reconstruction  
- **[PairDropGS: Paired Dropout-Induced Consistency Regularization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2605.12072v2)**  
  Authors: Hantang Li, Qiang Zhu, Xiandong Meng, Xingtao Wang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12072v2.pdf)  
  Keywords: ar, geometry, sparse-view, 3d gaussian, gaussian splatting  
- **[VidSplat: Gaussian Splatting Reconstruction with Geometry-Guided Video Diffusion Priors](https://arxiv.org/abs/2605.11424v1)**  
  Authors: Jimin Tang, Wenyuan Zhang, Junsheng Zhou, Zian Huang, Kanle Shi, Shenkun Xu, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11424v1.pdf)  
  Keywords: ar, geometry, sparse-view, gaussian splatting, face  
- **[ConFixGS: Learning to Fix Feedforward 3D Gaussian Splatting with Confidence-Aware Diffusion Priors in Driving Scenes](https://arxiv.org/abs/2605.09688v1)**  
  Authors: Rui Song, Tianhui Cai, Markus Gross, Xingcheng Zhou, Zewei Zhou, Zhiyu Huang, Olaf Wysocki, Jiaqi Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.09688v1.pdf)  
  Keywords: 3d gaussian, sparse-view, ar, gaussian splatting  
- **[FrameTwin: Curve-Anchored Gaussian Alignment from Sparse Views for Adaptive Wireframe 3D Printing](https://arxiv.org/abs/2605.09362v1)**  
  Authors: Wenting Wang, Zhuo Huang, Kun Qian, Neelotpal Dutta, Yuhu Guo, Yingjun Tian, Yeung Yam, Charlie C. L. Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.09362v1.pdf)  
  Keywords: ar, geometry, sparse-view, deformation, sparse view, compact  
- **[SatSurfGS: Generalizable 2D Gaussian Splatting for Sparse-View Satellite Surface Reconstruction](https://arxiv.org/abs/2605.07181v1)**  
  Authors: Min Chen, Wei Guo, Bin Wang, Wen Li, Tong Fang, Jinbo Zhang, Junqi Zhao, Hong Kuang, Han Hu, Xuming Ge, Qing Zhu, Bo Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.07181v1.pdf)  
  Keywords: ar, sparse-view, 3d gaussian, gaussian splatting, face  
- **[Sparse-to-Complete: From Sparse Image Captures to Complete 3D Scenes](https://arxiv.org/abs/2605.05664v1)**  
  Authors: Yiyang Shen, Yin Yang, Kun Zhou, Tianjia Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.05664v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gapszju.github.io/S2C-3D)  
  Keywords: high-fidelity, ar, sparse-view, 3d gaussian, 3d reconstruction  
- **[Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193v1)**  
  Authors: Vinayak Gupta, Chih-Hao Lin, Shenlong Wang, Anand Bhattad, Jia-Bin Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28193v1.pdf)  
  Keywords: illumination, ar, segmentation, outdoor, sparse-view, semantic, 3d gaussian, dynamic, 3d reconstruction, sparse view, lighting  
- **[Residual Gaussian Splatting for Ultra Sparse-View CBCT Reconstruction](https://arxiv.org/abs/2604.27552v1)**  
  Authors: Jian Lin, Jiancheng Fang, Shaoyu Wang, Changan Lai, Yikun Zhang, Yang Chen, Qiegen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27552v1.pdf)  
  Keywords: neural rendering, ar, sparse-view, 3d gaussian, gaussian splatting, efficient  

### Geometry Reconstruction

*Showing the latest 50 out of 219 papers*

- **[PanoPlane: Plane-Aware Panoramic Completion for Sparse-View Indoor 3D Gaussian Splatting](https://arxiv.org/abs/2605.14135v1)**  
  Authors: Adil Qureshi, Dongki Jung, Jaehoon Choi, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14135v1.pdf)  
  Keywords: high-fidelity, ar, geometry, sparse-view, 3d gaussian, gaussian splatting, face  
- **[OCH3R: Object-Centric Holistic 3D Reconstruction](https://arxiv.org/abs/2605.13018v1)**  
  Authors: Yi Du, Yang You, Xiang Wan, Leonidas Guibas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13018v1.pdf)  
  Keywords: high-fidelity, ar, semantic, 3d gaussian, understanding, segmentation, 3d reconstruction  
- **[Revisiting Photometric Ambiguity for Accurate Gaussian-Splatting Surface Reconstruction](https://arxiv.org/abs/2605.12494v1)**  
  Authors: Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Xiaohan Yu, Lin Gu, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12494v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fictionarry.github.io/AmbiSuR-Proj)  
  Keywords: ar, geometry, gaussian splatting, 3d reconstruction, face  
- **[GeoQuery: Geometry-Query Diffusion for Sparse-View Reconstruction](https://arxiv.org/abs/2605.12399v1)**  
  Authors: Xiao Cao, Yuze Li, Youmin Zhang, Jiayu Song, Cheng Yan, Wen Li, Lixin Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12399v1.pdf)  
  Keywords: ar, geometry, sparse-view, 3d gaussian, gaussian splatting, 3d reconstruction  
- **[PairDropGS: Paired Dropout-Induced Consistency Regularization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2605.12072v2)**  
  Authors: Hantang Li, Qiang Zhu, Xiandong Meng, Xingtao Wang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12072v2.pdf)  
  Keywords: ar, geometry, sparse-view, 3d gaussian, gaussian splatting  
- **[XFreq-GS: Cross-Frequency Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2605.11432v1)**  
  Authors: Sheng Wang, Hengtao He, Chaozheng Wen, Jingwen Tong, Xinyu Li, Xiao Li, Jun Zhang, Shi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11432v1.pdf) | [![GitHub](https://img.shields.io/github/stars/KINGAZ1019/XFreq-GS?style=social)](https://github.com/KINGAZ1019/XFreq-GS)  
  Keywords: high-fidelity, ar, geometry, 3d gaussian, gaussian splatting  
- **[VidSplat: Gaussian Splatting Reconstruction with Geometry-Guided Video Diffusion Priors](https://arxiv.org/abs/2605.11424v1)**  
  Authors: Jimin Tang, Wenyuan Zhang, Junsheng Zhou, Zian Huang, Kanle Shi, Shenkun Xu, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11424v1.pdf)  
  Keywords: ar, geometry, sparse-view, gaussian splatting, face  
- **[MAGS-SLAM: Monocular Multi-Agent Gaussian Splatting SLAM for Geometrically and Photometrically Consistent Reconstruction](https://arxiv.org/abs/2605.10760v1)**  
  Authors: Zhihao Cao, Qi Shao, Shuhao Zhai, Jing Zhang, Anh Nguyen, Baoru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10760v1.pdf)  
  Keywords: high-fidelity, ar, geometry, mapping, lightweight, 3d gaussian, gaussian splatting, slam, tracking, 3d reconstruction, compact  
- **[TransmissiveGS: Residual-Guided Disentangled Gaussian Splatting for Transmissive Scene Reconstruction and Rendering](https://arxiv.org/abs/2605.10705v1)**  
  Authors: Zhenyu Liang, Xiao Zhang, Tianchao Li, Jack C. P. Cheng, Chi-Keung Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10705v1.pdf)  
  Keywords: high-fidelity, ar, geometry, gaussian splatting, reflection, face  
- **[BEA-GS: BEyond RAdiance Supervision in 3DGS for Precise Object Extraction](https://arxiv.org/abs/2605.09662v1)**  
  Authors: Alessio Mazzucchelli, Maria Naranjo-Almeida, Jorge Bustos-Sanchez, Mariella Dimiccoli, Francesc Moreno-Noguer, Jordi Sanchez-Riera, Adrian Penate-Sanchez  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.09662v1.pdf)  
  Keywords: ar, geometry, semantic, gaussian splatting, segmentation  

### Large Scene

- **[PropSplat: Map-Free RF Field Reconstruction via 3D Gaussian Propagation Splatting](https://arxiv.org/abs/2605.08035v1)**  
  Authors: William Bjorndahl, Maninder Pal Singh, Farhad Nouri, Joseph Camp  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.08035v1.pdf)  
  Keywords: localization, ar, outdoor, 3d gaussian, nerf  
- **[FieryGS: In-the-Wild Fire Synthesis with Physics-Integrated Gaussian Splatting](https://arxiv.org/abs/2605.00177v1)**  
  Authors: Qianfan Shen, Ningxiao Tao, Qiyu Dai, Tianle Chen, Minghan Qin, Yongjie Zhang, Mengyu Chu, Wenzheng Chen, Baoquan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/FieryGS)  
  Keywords: high-fidelity, ar, geometry, outdoor, 3d gaussian, gaussian splatting, dynamic, efficient, face  
- **[Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193v1)**  
  Authors: Vinayak Gupta, Chih-Hao Lin, Shenlong Wang, Anand Bhattad, Jia-Bin Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28193v1.pdf)  
  Keywords: illumination, ar, segmentation, outdoor, sparse-view, semantic, 3d gaussian, dynamic, 3d reconstruction, sparse view, lighting  
- **[EnerGS: Energy-Based Gaussian Splatting with Partial Geometric Priors](https://arxiv.org/abs/2604.26238v1)**  
  Authors: Rui Song, Tianhui Cai, Markus Gross, Yun Zhang, Walter Zimmer, Zhiyu Huang, Olaf Wysocki, Jiaqi Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26238v1.pdf)  
  Keywords: ar, geometry, outdoor, 3d gaussian, gaussian splatting  
- **[DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis](https://arxiv.org/abs/2604.13416v1)**  
  Authors: Cheng-You Lu, Yi-Shan Hung, Wei-Ling Chi, Hao-Ping Wang, Charlie Li-Ting Tsai, Yu-Cheng Chang, Yu-Lun Liu, Thomas Do, Chin-Teng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13416v1.pdf)  
  Keywords: 3d gaussian, outdoor, gaussian splatting, ar  
- **[RMGS-SLAM: Real-time Multi-sensor Gaussian Splatting SLAM](https://arxiv.org/abs/2604.12942v2)**  
  Authors: Dongen Li, Yi Liu, Junqi Liu, Zewen Sun, Zefan Huang, Shuo Sun, Jiahui Liu, Chengran Yuan, Hongliang Guo, Francis E. H. Tay, Marcelo H. Ang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12942v2.pdf)  
  Keywords: localization, ar, mapping, outdoor, 3d gaussian, gaussian splatting, slam  
- **[GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors](https://arxiv.org/abs/2604.11401v1)**  
  Authors: Qilin Zhang, Jinyu Zhu, Olaf Wysocki, Benjamin Busam, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11401v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Jinyzzz/GS4City?style=social)](https://github.com/Jinyzzz/GS4City)  
  Keywords: ar, geometry, semantic, 3d gaussian, gaussian splatting, urban scene, understanding, segmentation, compact  
- **[Neural Harmonic Textures for High-Quality Primitive Based Neural Reconstruction](https://arxiv.org/abs/2604.01204v2)**  
  Authors: Jorge Condor, Nicolas Moenne-Loccoz, Merlin Nimier-David, Piotr Didyk, Zan Gojcic, Qi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01204v2.pdf)  
  Keywords: ar, semantic, 3d gaussian, gaussian splatting, large scene  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: high-fidelity, neural rendering, 4d, geometry, ar, motion, gaussian splatting, dynamic, efficient, large scene, understanding, shadow  
- **[Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting](https://arxiv.org/abs/2603.29185v1)**  
  Authors: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29185v1.pdf)  
  Keywords: localization, ar, outdoor, gaussian splatting, efficient  

### Model Compression

*Showing the latest 50 out of 200 papers*

- **[3D Skew-Normal Splatting](https://arxiv.org/abs/2605.15010v1)**  
  Authors: Xiangru Wu, Ke Fan, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15010v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, efficient, face, compact  
- **[Denoising-GS: Gaussian Splatting with Spatial-aware Denoising](https://arxiv.org/abs/2605.14880v1)**  
  Authors: Qingyuan Zhou, Xinyi Liu, Weidong Yang, Ning Wang, Shuquan Ye, Ben Fei, Ying He, Wanli Ouyang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14880v1.pdf)  
  Keywords: high-fidelity, ar, motion, 3d gaussian, gaussian splatting, compact  
- **[Efficient Dense Matching for Enhanced Gaussian Splatting Using AV1 Motion Vectors](https://arxiv.org/abs/2605.14629v1)**  
  Authors: Julien Zouein, Vibhoothi Vibhoothi, François Pitié, Anil Kokaram  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14629v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sigmedia.tv/AV1-3DGS.github.io)  
  Keywords: ar, motion, 3d gaussian, gaussian splatting, head, efficient, nerf  
- **[Sparse Code Uplifting for Efficient 3D Language Gaussian Splatting](https://arxiv.org/abs/2605.13600v1)**  
  Authors: Lovre Antonio Budimir, Yushi Guan, Steve Ryhner, Sven Lončarić, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13600v1.pdf)  
  Keywords: fast, ar, semantic, 3d gaussian, gaussian splatting, efficient, understanding, compact  
- **[Z-Order Transformer for Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2605.13465v1)**  
  Authors: Can Wang, Lei Liu, Wei Jiang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13465v1.pdf)  
  Keywords: fast, ar, semantic, 3d gaussian, gaussian splatting, efficient  
- **[RoSplat: Robust Feed-Forward Pixel-wise Gaussian Splatting for Varying Input Views and High-Resolution Rendering](https://arxiv.org/abs/2605.13093v1)**  
  Authors: Hoang Chuong Nguyen, Renjie Wu, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13093v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, gaussian splatting  
- **[3D Gaussian Splatting for Efficient Retrospective Dynamic Scene Novel View Synthesis with a Standardized Benchmark](https://arxiv.org/abs/2605.12437v1)**  
  Authors: Yunxiao Zhang, Suryansh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12437v1.pdf)  
  Keywords: ar, motion, 3d gaussian, gaussian splatting, deformation, dynamic, efficient, nerf, body  
- **[PoseCompass: Intelligent Synthetic Pose Selection for Visual Localization](https://arxiv.org/abs/2605.12144v1)**  
  Authors: Yanan Zhou, Zhaoyan Qian, Yanli Li, Nan Yang, Zhongliang Guo, Dong Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12144v1.pdf)  
  Keywords: localization, ar, lightweight, 3d gaussian, gaussian splatting  
- **[3DGS$^3$: Joint Super Sampling and Frame Interpolation for Real-Time Large-Scale 3DGS Rendering](https://arxiv.org/abs/2605.11489v1)**  
  Authors: Yibo Zhao, Fan Gao, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11489v1.pdf)  
  Keywords: high-fidelity, ar, acceleration, lightweight, 3d gaussian, gaussian splatting, efficient, face, compact  
- **[PD-4DGS:Progressive Decomposition of 4D Gaussian Splatting for Bandwidth-Adaptive Dynamic Scene Streaming](https://arxiv.org/abs/2605.11427v1)**  
  Authors: Jiachen Li, Guangzhi Han, Jin Wan, Delong Han, Yuan Gao, Min Li, Mingle Zhou, Gang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11427v1.pdf)  
  Keywords: 4d, ar, motion, gaussian splatting, compression, deformation, dynamic  

### Quality Enhancement

*Showing the latest 50 out of 115 papers*

- **[Denoising-GS: Gaussian Splatting with Spatial-aware Denoising](https://arxiv.org/abs/2605.14880v1)**  
  Authors: Qingyuan Zhou, Xinyi Liu, Weidong Yang, Ning Wang, Shuquan Ye, Ben Fei, Ying He, Wanli Ouyang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14880v1.pdf)  
  Keywords: high-fidelity, ar, motion, 3d gaussian, gaussian splatting, compact  
- **[PanoPlane: Plane-Aware Panoramic Completion for Sparse-View Indoor 3D Gaussian Splatting](https://arxiv.org/abs/2605.14135v1)**  
  Authors: Adil Qureshi, Dongki Jung, Jaehoon Choi, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14135v1.pdf)  
  Keywords: high-fidelity, ar, geometry, sparse-view, 3d gaussian, gaussian splatting, face  
- **[Real2Sim: A Physics-driven and Editable Gaussian Splatting Framework for Autonomous Driving Scenes](https://arxiv.org/abs/2605.13591v1)**  
  Authors: Kaicong Huang, Talha Azfar, Weisong Shi, Ruimin Ke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13591v1.pdf)  
  Keywords: high-fidelity, 4d, ar, gaussian splatting, dynamic, autonomous driving, tracking  
- **[OCH3R: Object-Centric Holistic 3D Reconstruction](https://arxiv.org/abs/2605.13018v1)**  
  Authors: Yi Du, Yang You, Xiang Wan, Leonidas Guibas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13018v1.pdf)  
  Keywords: high-fidelity, ar, semantic, 3d gaussian, understanding, segmentation, 3d reconstruction  
- **[PointForward: Feedforward Driving Reconstruction through Point-Aligned Representations](https://arxiv.org/abs/2605.11594v1)**  
  Authors: Cheng Chi, Xianqi Wang, Hongcheng Luo, Mingfei Tu, Gangwei Xu, Zehan Zhang, Bing Wang, Guang Chen, Hangjun Ye, Sida Peng, Xin Yang, Haiyang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11594v1.pdf)  
  Keywords: fast, high-fidelity, ar, motion, 3d gaussian, gaussian splatting, dynamic, autonomous driving  
- **[3DGS$^3$: Joint Super Sampling and Frame Interpolation for Real-Time Large-Scale 3DGS Rendering](https://arxiv.org/abs/2605.11489v1)**  
  Authors: Yibo Zhao, Fan Gao, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11489v1.pdf)  
  Keywords: high-fidelity, ar, acceleration, lightweight, 3d gaussian, gaussian splatting, efficient, face, compact  
- **[XFreq-GS: Cross-Frequency Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2605.11432v1)**  
  Authors: Sheng Wang, Hengtao He, Chaozheng Wen, Jingwen Tong, Xinyu Li, Xiao Li, Jun Zhang, Shi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11432v1.pdf) | [![GitHub](https://img.shields.io/github/stars/KINGAZ1019/XFreq-GS?style=social)](https://github.com/KINGAZ1019/XFreq-GS)  
  Keywords: high-fidelity, ar, geometry, 3d gaussian, gaussian splatting  
- **[PG-3DGS: Optimizing 3D Gaussian Splatting to Satisfy Physics Objectives](https://arxiv.org/abs/2605.11266v1)**  
  Authors: Zachary Lee, Maxwell Jacobson, Yexiang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11266v1.pdf)  
  Keywords: fast, high-fidelity, ar, 3d gaussian, gaussian splatting, dynamic, understanding  
- **[MAGS-SLAM: Monocular Multi-Agent Gaussian Splatting SLAM for Geometrically and Photometrically Consistent Reconstruction](https://arxiv.org/abs/2605.10760v1)**  
  Authors: Zhihao Cao, Qi Shao, Shuhao Zhai, Jing Zhang, Anh Nguyen, Baoru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10760v1.pdf)  
  Keywords: high-fidelity, ar, geometry, mapping, lightweight, 3d gaussian, gaussian splatting, slam, tracking, 3d reconstruction, compact  
- **[TransmissiveGS: Residual-Guided Disentangled Gaussian Splatting for Transmissive Scene Reconstruction and Rendering](https://arxiv.org/abs/2605.10705v1)**  
  Authors: Zhenyu Liang, Xiao Zhang, Tianchao Li, Jack C. P. Cheng, Chi-Keung Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10705v1.pdf)  
  Keywords: high-fidelity, ar, geometry, gaussian splatting, reflection, face  

### Ray Tracing

- **[Differentiable Ray Tracing with Gaussians for Unified Radio Propagation Simulation and View Synthesis](https://arxiv.org/abs/2605.07781v1)**  
  Authors: Niklas Vaara, Lam Huynh, Pekka Sangi, Miguel Bordallo López, Janne Heikkilä  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.07781v1.pdf)  
  Keywords: high-fidelity, ar, geometry, 3d gaussian, gaussian splatting, ray tracing  
- **[Power Foam: Unifying Real-Time Differentiable Ray Tracing and Rasterization](https://arxiv.org/abs/2604.24994v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Dor Verbin, Kwang Moo Yi, Anish Prabhu, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24994v1.pdf)  
  Keywords: ar, geometry, efficient, ray tracing, face  
- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138v1)**  
  Authors: Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/viserdex)  
  Keywords: ar, semantic, 3d gaussian, gaussian splatting, dynamic, efficient, tracking, ray tracing, robotics, lighting  
- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: ar, gaussian splatting, ray tracing, reflection, face  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, reflection, ray casting  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: localization, ar, mapping, semantic, 3d gaussian, gaussian splatting, efficient, tracking, ray tracing, face, slam  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: ar, mapping, 3d gaussian, gaussian splatting, ray tracing, reflection, shadow, relightable  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: ar, geometry, path tracing, 3d gaussian, real-time rendering, face  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: fast, high-fidelity, ar, geometry, 3d gaussian, gaussian splatting, efficient, ray tracing, real-time rendering, nerf, face  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awareness](https://arxiv.org/abs/2603.17499v6)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v6.pdf) | [![GitHub](https://img.shields.io/github/stars/UNIC-Lab/Awesome-Radio-Map-Categorized?style=social)](https://github.com/UNIC-Lab/Awesome-Radio-Map-Categorized)  
  Keywords: ar, mapping, 3d gaussian, gaussian splatting, ray tracing, survey  

### Relighting

*Showing the latest 50 out of 64 papers*

- **[HarmoGS: Robust 3D Gaussian Splatting in the Wild via Conflict-Aware Gradient Harmonization](https://arxiv.org/abs/2605.13073v1)**  
  Authors: Yulei Kang, Tianze Zhu, Jian-Fang Hu, Jianhuang Lai, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13073v1.pdf)  
  Keywords: illumination, ar, semantic, 3d gaussian, gaussian splatting  
- **[TransmissiveGS: Residual-Guided Disentangled Gaussian Splatting for Transmissive Scene Reconstruction and Rendering](https://arxiv.org/abs/2605.10705v1)**  
  Authors: Zhenyu Liang, Xiao Zhang, Tianchao Li, Jack C. P. Cheng, Chi-Keung Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10705v1.pdf)  
  Keywords: high-fidelity, ar, geometry, gaussian splatting, reflection, face  
- **[Relightable Gaussian Splatting for Virtual Production Using Image-Based Illumination](https://arxiv.org/abs/2605.09024v1)**  
  Authors: Adrian Azzarelli, Nantheera Anantrasirichai, James Pollock, David R. Bull  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.09024v1.pdf)  
  Keywords: illumination, ar, geometry, relighting, gaussian splatting, efficient, vr, light transport, 3d reconstruction, reflection, lighting, relightable  
- **[Uncovering and Shaping the Latent Representation of 3D Scene Topology in Vision-Language Models](https://arxiv.org/abs/2605.07148v1)**  
  Authors: Haoming Wang, Wei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.07148v1.pdf) | [![GitHub](https://img.shields.io/github/stars/pittisl/vlm-latent-shaping?style=social)](https://github.com/pittisl/vlm-latent-shaping)  
  Keywords: ar, human, semantic, 3d gaussian, understanding, shadow  
- **[3DSS: 3D Surface Splatting for Inverse Rendering](https://arxiv.org/abs/2605.05876v3)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.05876v3.pdf)  
  Keywords: illumination, ar, geometry, relighting, face, lighting  
- **[GOR-IS: 3D Gaussian Object Removal in the Intrinsic Space](https://arxiv.org/abs/2605.00498v1)**  
  Authors: Yonghao Zhao, Yupeng Gao, Jian Yang, Jin Xie, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00498v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://applezyh.github.io/GOR-IS-project-page/) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://applezyh.github.io/GOR-IS-project-page)  
  Keywords: ar, geometry, 3d gaussian, gaussian splatting, light transport, nerf, face, lighting  
- **[Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193v1)**  
  Authors: Vinayak Gupta, Chih-Hao Lin, Shenlong Wang, Anand Bhattad, Jia-Bin Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28193v1.pdf)  
  Keywords: illumination, ar, segmentation, outdoor, sparse-view, semantic, 3d gaussian, dynamic, 3d reconstruction, sparse view, lighting  
- **[Color-Encoded Illumination for High-Speed Volumetric Scene Reconstruction](https://arxiv.org/abs/2604.26920v1)**  
  Authors: David Novikov, Eilon Vaknin, Narek Tumanyan, Mark Sheinin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26920v1.pdf)  
  Keywords: illumination, ar, motion, gaussian splatting, dynamic  
- **[Light 'em Up: Enabling Few-Shot Low-Light 3D Gaussian Splatting with Multi-Scale Explicit Retinex Illumination Decoupling](https://arxiv.org/abs/2604.24053v1)**  
  Authors: YuHao Yin, Zongji Wang, Yuanben Zhang, Biqing Li, Jiesong Bai, Junyi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24053v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YhuoyuH/MERID-GS?style=social)](https://github.com/YhuoyuH/MERID-GS)  
  Keywords: illumination, ar, lightweight, few-shot, sparse-view, 3d gaussian, gaussian splatting, head, reflection  
- **[Bringing a Personal Point of View: Evaluating Dynamic 3D Gaussian Splatting for Egocentric Scene Reconstruction](https://arxiv.org/abs/2604.23803v1)**  
  Authors: Jan Warchocki, Xi Wang, Jonas Kulhanek, Jan van Gemert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23803v1.pdf)  
  Keywords: 4d, ar, human, motion, 3d gaussian, gaussian splatting, dynamic, efficient, 3d reconstruction, robotics, lighting  

### SLAM

*Showing the latest 50 out of 81 papers*

- **[Towards Accurate Single Panoramic 3D Detection: A Semantic Gaussian Centric Approach](https://arxiv.org/abs/2605.14601v1)**  
  Authors: Kanglin Ning, Yiran Zhao, Wenrui Li, Shaoru Sun, Xingtao Wang, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14601v1.pdf)  
  Keywords: ar, mapping, semantic, head, 3d gaussian, understanding  
- **[Real2Sim: A Physics-driven and Editable Gaussian Splatting Framework for Autonomous Driving Scenes](https://arxiv.org/abs/2605.13591v1)**  
  Authors: Kaicong Huang, Talha Azfar, Weisong Shi, Ruimin Ke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13591v1.pdf)  
  Keywords: high-fidelity, 4d, ar, gaussian splatting, dynamic, autonomous driving, tracking  
- **[PoseCompass: Intelligent Synthetic Pose Selection for Visual Localization](https://arxiv.org/abs/2605.12144v1)**  
  Authors: Yanan Zhou, Zhaoyan Qian, Yanli Li, Nan Yang, Zhongliang Guo, Dong Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12144v1.pdf)  
  Keywords: localization, ar, lightweight, 3d gaussian, gaussian splatting  
- **[MAGS-SLAM: Monocular Multi-Agent Gaussian Splatting SLAM for Geometrically and Photometrically Consistent Reconstruction](https://arxiv.org/abs/2605.10760v1)**  
  Authors: Zhihao Cao, Qi Shao, Shuhao Zhai, Jing Zhang, Anh Nguyen, Baoru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10760v1.pdf)  
  Keywords: high-fidelity, ar, geometry, mapping, lightweight, 3d gaussian, gaussian splatting, slam, tracking, 3d reconstruction, compact  
- **[PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.10307v1)**  
  Authors: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10307v1.pdf)  
  Keywords: fast, high-fidelity, 4d, ar, motion, gaussian splatting, deformation, dynamic, tracking, segmentation, robotics  
- **[PropSplat: Map-Free RF Field Reconstruction via 3D Gaussian Propagation Splatting](https://arxiv.org/abs/2605.08035v1)**  
  Authors: William Bjorndahl, Maninder Pal Singh, Farhad Nouri, Joseph Camp  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.08035v1.pdf)  
  Keywords: localization, ar, outdoor, 3d gaussian, nerf  
- **[Disambiguating 2D-3D Correspondences in Gaussian Splatting-based Feature Fields for Visual Localization](https://arxiv.org/abs/2605.07351v1)**  
  Authors: Miso Lee, Sangeek Hyun, Yerim Jeon, Jae-Pil Heo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.07351v1.pdf)  
  Keywords: localization, ar, mapping, gaussian splatting, efficient, compact  
- **[ULF-Loc: Unbiased Landmark Feature for Robust Visual Localization with 3D Gaussian Splatting](https://arxiv.org/abs/2605.04730v1)**  
  Authors: Yingdong Gu, Shaocheng Yan, Zhenjun Zhao, Yuan Kou, Jianxin Luo, Pengcheng Shi, Jiayuan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04730v1.pdf)  
  Keywords: localization, ar, geometry, efficient rendering, 3d gaussian, gaussian splatting, efficient  
- **[Velox: Learning Representations of 4D Geometry and Appearance](https://arxiv.org/abs/2605.04527v1)**  
  Authors: Anagh Malik, Dorian Chan, Xiaoming Zhao, David B. Lindell, Oncel Tuzel, Jen-Hao Rick Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04527v1.pdf)  
  Keywords: 4d, ar, geometry, 3d gaussian, dynamic, tracking, face  
- **[CoherentRaster: Efficient 3D Gaussian Splatting for Light Field Displays](https://arxiv.org/abs/2605.04509v1)**  
  Authors: Gyujin Sim, Seungjoo Shin, Hosung Jeon, Gwangsoon Lee, Hyon-Gon Choo, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04509v1.pdf)  
  Keywords: ar, mapping, 3d gaussian, gaussian splatting, head, efficient, real-time rendering, acceleration  

### Scene Understanding

*Showing the latest 50 out of 120 papers*

- **[Towards Accurate Single Panoramic 3D Detection: A Semantic Gaussian Centric Approach](https://arxiv.org/abs/2605.14601v1)**  
  Authors: Kanglin Ning, Yiran Zhao, Wenrui Li, Shaoru Sun, Xingtao Wang, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14601v1.pdf)  
  Keywords: ar, mapping, semantic, head, 3d gaussian, understanding  
- **[Sparse Code Uplifting for Efficient 3D Language Gaussian Splatting](https://arxiv.org/abs/2605.13600v1)**  
  Authors: Lovre Antonio Budimir, Yushi Guan, Steve Ryhner, Sven Lončarić, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13600v1.pdf)  
  Keywords: fast, ar, semantic, 3d gaussian, gaussian splatting, efficient, understanding, compact  
- **[Z-Order Transformer for Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2605.13465v1)**  
  Authors: Can Wang, Lei Liu, Wei Jiang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13465v1.pdf)  
  Keywords: fast, ar, semantic, 3d gaussian, gaussian splatting, efficient  
- **[HarmoGS: Robust 3D Gaussian Splatting in the Wild via Conflict-Aware Gradient Harmonization](https://arxiv.org/abs/2605.13073v1)**  
  Authors: Yulei Kang, Tianze Zhu, Jian-Fang Hu, Jianhuang Lai, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13073v1.pdf)  
  Keywords: illumination, ar, semantic, 3d gaussian, gaussian splatting  
- **[OCH3R: Object-Centric Holistic 3D Reconstruction](https://arxiv.org/abs/2605.13018v1)**  
  Authors: Yi Du, Yang You, Xiang Wan, Leonidas Guibas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13018v1.pdf)  
  Keywords: high-fidelity, ar, semantic, 3d gaussian, understanding, segmentation, 3d reconstruction  
- **[PointGS: Semantic-Consistent Unsupervised 3D Point Cloud Segmentation with 3D Gaussian Splatting](https://arxiv.org/abs/2605.11520v1)**  
  Authors: Yixiao Song, Qingyong Li, Wen Wang, Zhicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11520v1.pdf)  
  Keywords: ar, semantic, 3d gaussian, gaussian splatting, autonomous driving, segmentation, face  
- **[PG-3DGS: Optimizing 3D Gaussian Splatting to Satisfy Physics Objectives](https://arxiv.org/abs/2605.11266v1)**  
  Authors: Zachary Lee, Maxwell Jacobson, Yexiang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11266v1.pdf)  
  Keywords: fast, high-fidelity, ar, 3d gaussian, gaussian splatting, dynamic, understanding  
- **[Forecast-aware Gaussian Splatting for Predictive 3D Representation in Language-Guided Pick-and-Place Manipulation](https://arxiv.org/abs/2605.11144v1)**  
  Authors: Kaixin Jia, Jiacheng Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11144v1.pdf)  
  Keywords: ar, human, semantic, gaussian splatting, understanding  
- **[VEGA: Visual Encoder Grounding Alignment for Spatially-Aware Vision-Language-Action Models](https://arxiv.org/abs/2605.10485v1)**  
  Authors: Hao Wang, Xiaobao Wei, Jingyang He, Chengyu Bai, Chun-Kai Fan, Jiajun Cao, Jintao Chen, Ying Li, Shanyu Rong, Ming Lu, Xiaozhu Ju, Jian Tang, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10485v1.pdf)  
  Keywords: ar, lightweight, semantic, 3d gaussian, gaussian splatting, head  
- **[PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.10307v1)**  
  Authors: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10307v1.pdf)  
  Keywords: fast, high-fidelity, 4d, ar, motion, gaussian splatting, deformation, dynamic, tracking, segmentation, robotics  



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