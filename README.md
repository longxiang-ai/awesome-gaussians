# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-04-05 01:23:50

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

- [3DGS Surveys](#3dgs-surveys) (5 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (118 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (499 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (157 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (202 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (32 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (207 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (19 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (218 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (130 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (22 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (73 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (75 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (133 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Nevis Digital Twin: Photogrammetry and Immersive Visualization of Historical Sites](https://arxiv.org/abs/2603.20560v1)**  
  Authors: Alex Apffel, Huy Tran, Vuthea Chheang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20560v1.pdf)  
  Keywords: vr, gaussian splatting, ar, 3d gaussian, survey  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: mapping, gaussian splatting, ar, 3d gaussian, survey, ray tracing  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: dynamic, mapping, tracking, survey, localization, gaussian splatting, ar, 3d gaussian, efficient, motion, face, slam  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: robotics, gaussian splatting, ar, 3d gaussian, survey  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v3)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v3.pdf)  
  Keywords: gaussian splatting, ar, nerf, 3d gaussian, efficient, survey, geometry  

### Acceleration

*Showing the latest 50 out of 118 papers*

- **[GEMM-GS: Accelerating 3D Gaussian Splatting on Tensor Cores with GEMM-Compatible Blending](https://arxiv.org/abs/2604.02120v1)**  
  Authors: Haomin Li, Bowen Zhu, Fangxin Liu, Zongwu Wang, Xinran Liang, Li Jiang, Haibing Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02120v1.pdf) | [![GitHub](https://img.shields.io/github/stars/shieldforever/GEMM-GS?style=social)](https://github.com/shieldforever/GEMM-GS)  
  Keywords: nerf, gaussian splatting, 3d gaussian, acceleration  
- **[GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2604.01884v1)**  
  Authors: Xianben Yang, Tao Wang, Yuxuan Li, Yi Jin, Haibin Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01884v1.pdf)  
  Keywords: real-time rendering, dynamic, compact, gaussian splatting, ar, 3d gaussian  
- **[FaCT-GS: Fast and Scalable CT Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2604.01844v1)**  
  Authors: Pawel Tomasz Pieta, Rasmus Juul Pedersen, Sina Borgi, Jakob Sauer Jørgensen, Jens Wenzel Andreasen, Vedrana Andersen Dahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01844v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PaPieta/fact-gs?style=social)](https://github.com/PaPieta/fact-gs)  
  Keywords: fast, gaussian splatting, ar  
- **[Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty-aware Differentiable Optimization](https://arxiv.org/abs/2604.01030v1)**  
  Authors: Yueh-Cheng Liu, Jozef Hladký, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01030v1.pdf)  
  Keywords: fast, gaussian splatting, ar, 3d gaussian, sparse-view  
- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394v1)**  
  Authors: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29394v1.pdf)  
  Keywords: fast, gaussian splatting, ar, 3d gaussian, 3d reconstruction, sparse-view  
- **[LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2603.28431v3)**  
  Authors: Xuan Deng, Xiandong Meng, Hengyu Man, Qiang Zhu, Tiange Zhang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28431v3.pdf)  
  Keywords: real-time rendering, high-fidelity, compression, compact, gaussian splatting, ar, nerf, lightweight, 3d gaussian, head, geometry  
- **[ObjectMorpher: 3D-Aware Image Editing via Deformable 3DGS Models](https://arxiv.org/abs/2603.28152v1)**  
  Authors: Yuhuan Xie, Aoxuan Pan, Yi-Hua Huang, Chirui Chang, Peng Dai, Xin Yu, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28152v1.pdf)  
  Keywords: fast, gaussian splatting, lighting, ar, 3d gaussian, deformation, geometry  
- **[Physically Inspired Gaussian Splatting for HDR Novel View Synthesis](https://arxiv.org/abs/2603.28020v1)**  
  Authors: Huimin Zeng, Yue Bai, Hailing Wang, Yun Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huimin-zeng.github.io/PhysHDR-GS)  
  Keywords: real-time rendering, dynamic, illumination, gaussian splatting, ar  
- **[DiffSoup: Direct Differentiable Rasterization of Triangle Soup for Extreme Radiance Field Simplification](https://arxiv.org/abs/2603.27151v1)**  
  Authors: Kenji Tojo, Bernd Bickel, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27151v1.pdf) | [![GitHub](https://img.shields.io/github/stars/kenji-tojo/diffsoup?style=social)](https://github.com/kenji-tojo/diffsoup)  
  Keywords: real-time rendering, gaussian splatting, ar, 3d gaussian, efficient  
- **[ViewSplat: View-Adaptive Dynamic Gaussian Splatting for Feed-Forward Synthesis](https://arxiv.org/abs/2603.25265v1)**  
  Authors: Moonyeon Jeong, Seunggi Min, Suhyeon Lee, Hongje Seong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25265v1.pdf)  
  Keywords: real-time rendering, dynamic, high-fidelity, fast, gaussian splatting, ar, 3d gaussian  

### Applications

*Showing the latest 50 out of 499 papers*

- **[ProDiG: Progressive Diffusion-Guided Gaussian Splatting for Aerial to Ground Reconstruction](https://arxiv.org/abs/2604.02003v1)**  
  Authors: Sirshapan Mitra, Yogesh S. Rawat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02003v1.pdf)  
  Keywords: dynamic, gaussian splatting, geometry, ar  
- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, segmentation, lightweight, 3d gaussian, motion, deformation, head  
- **[GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2604.01884v1)**  
  Authors: Xianben Yang, Tao Wang, Yuxuan Li, Yi Jin, Haibin Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01884v1.pdf)  
  Keywords: real-time rendering, dynamic, compact, gaussian splatting, ar, 3d gaussian  
- **[A3R: Agentic Affordance Reasoning via Cross-Dimensional Evidence in 3D Gaussian Scenes](https://arxiv.org/abs/2604.01882v1)**  
  Authors: Di Li, Jie Feng, Guanbin Li, Ronghua Shang, Yuhui Zheng, Weisheng Dong, Guangming Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01882v1.pdf)  
  Keywords: semantic, 3d gaussian, ar  
- **[FaCT-GS: Fast and Scalable CT Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2604.01844v1)**  
  Authors: Pawel Tomasz Pieta, Rasmus Juul Pedersen, Sina Borgi, Jakob Sauer Jørgensen, Jens Wenzel Andreasen, Vedrana Andersen Dahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01844v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PaPieta/fact-gs?style=social)](https://github.com/PaPieta/fact-gs)  
  Keywords: fast, gaussian splatting, ar  
- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, understanding, segmentation, semantic, human, motion, face, tracking, geometry  
- **[F3DGS: Federated 3D Gaussian Splatting for Decentralized Multi-Agent World Modeling](https://arxiv.org/abs/2604.01605v1)**  
  Authors: Morui Zhu, Mohammad Dehghani Tezerjani, Mátyás Szántó, Márton Vaitkus, Song Fu, Qing Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01605v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, efficient, 3d reconstruction, head  
- **[Satellite-Free Training for Drone-View Geo-Localization](https://arxiv.org/abs/2604.01581v1)**  
  Authors: Tao Liu, Yingzhi Zhang, Kan Ren, Xiaoqi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01581v1.pdf)  
  Keywords: localization, gaussian splatting, ar, lightweight, 3d gaussian, geometry  
- **[ColorGradedGaussians: Palette-Based Color Grading for 3D Gaussian Splatting via View-Space Sparse Decomposition](https://arxiv.org/abs/2604.01551v1)**  
  Authors: Cheng-Kang Ted Chao, Yotam Gingold  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01551v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar  
- **[Better Rigs, Not Bigger Networks: A Body Model Ablation for Gaussian Avatars](https://arxiv.org/abs/2604.01447v1)**  
  Authors: Derek Austin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01447v1.pdf)  
  Keywords: gaussian splatting, body, avatar, ar, human, 3d gaussian, deformation  

### Avatar Generation

*Showing the latest 50 out of 157 papers*

- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, segmentation, lightweight, 3d gaussian, motion, deformation, head  
- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, understanding, segmentation, semantic, human, motion, face, tracking, geometry  
- **[F3DGS: Federated 3D Gaussian Splatting for Decentralized Multi-Agent World Modeling](https://arxiv.org/abs/2604.01605v1)**  
  Authors: Morui Zhu, Mohammad Dehghani Tezerjani, Mátyás Szántó, Márton Vaitkus, Song Fu, Qing Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01605v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, efficient, 3d reconstruction, head  
- **[Better Rigs, Not Bigger Networks: A Body Model Ablation for Gaussian Avatars](https://arxiv.org/abs/2604.01447v1)**  
  Authors: Derek Austin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01447v1.pdf)  
  Keywords: gaussian splatting, body, avatar, ar, human, 3d gaussian, deformation  
- **[LESV: Language Embedded Sparse Voxel Fusion for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2604.01388v1)**  
  Authors: Fusang Wang, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Fabien Moutarde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01388v1.pdf)  
  Keywords: gaussian splatting, vr, ar, understanding, semantic, 3d gaussian, head, geometry  
- **[Autoregressive Appearance Prediction for 3D Gaussian Avatars](https://arxiv.org/abs/2604.00928v1)**  
  Authors: Michael Steiner, Zhang Chen, Alexander Richard, Vasu Agrawal, Markus Steinberger, Michael Zollhöfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00928v1.pdf)  
  Keywords: dynamic, high-fidelity, compact, gaussian splatting, avatar, ar, 3d gaussian, human, motion  
- **[TRiGS: Temporal Rigid-Body Motion for Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2604.00538v1)**  
  Authors: Suwoong Yeom, Joonsik Nam, Seunggyu Choi, Lucas Yunkyu Lee, Sangmin Kim, Jaesik Park, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong, Sukju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00538v1.pdf)  
  Keywords: 4d, dynamic, body, gaussian splatting, ar, motion  
- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: gaussian splatting, reflection, ar, face, ray tracing  
- **[LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2603.28431v3)**  
  Authors: Xuan Deng, Xiandong Meng, Hengyu Man, Qiang Zhu, Tiange Zhang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28431v3.pdf)  
  Keywords: real-time rendering, high-fidelity, compression, compact, gaussian splatting, ar, nerf, lightweight, 3d gaussian, head, geometry  
- **[\textit{4DSurf}: High-Fidelity Dynamic Scene Surface Reconstruction](https://arxiv.org/abs/2603.28064v1)**  
  Authors: Renjie Wu, Hongdong Li, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28064v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, sparse-view, motion, deformation, face, geometry  

### Dynamic Scene

*Showing the latest 50 out of 202 papers*

- **[ProDiG: Progressive Diffusion-Guided Gaussian Splatting for Aerial to Ground Reconstruction](https://arxiv.org/abs/2604.02003v1)**  
  Authors: Sirshapan Mitra, Yogesh S. Rawat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02003v1.pdf)  
  Keywords: dynamic, gaussian splatting, geometry, ar  
- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, segmentation, lightweight, 3d gaussian, motion, deformation, head  
- **[GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2604.01884v1)**  
  Authors: Xianben Yang, Tao Wang, Yuxuan Li, Yi Jin, Haibin Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01884v1.pdf)  
  Keywords: real-time rendering, dynamic, compact, gaussian splatting, ar, 3d gaussian  
- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, understanding, segmentation, semantic, human, motion, face, tracking, geometry  
- **[Better Rigs, Not Bigger Networks: A Body Model Ablation for Gaussian Avatars](https://arxiv.org/abs/2604.01447v1)**  
  Authors: Derek Austin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01447v1.pdf)  
  Keywords: gaussian splatting, body, avatar, ar, human, 3d gaussian, deformation  
- **[DLWM: Dual Latent World Models enable Holistic Gaussian-centric Pre-training in Autonomous Driving](https://arxiv.org/abs/2604.00969v1)**  
  Authors: Yiyao Zhu, Ying Xue, Haiming Zhang, Guangfeng Jiang, Wending Zhou, Xu Yan, Jiantao Gao, Yingjie Cai, Bingbing Liu, Zhen Li, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00969v1.pdf)  
  Keywords: 4d, ar, semantic, 3d gaussian, motion, autonomous driving  
- **[Autoregressive Appearance Prediction for 3D Gaussian Avatars](https://arxiv.org/abs/2604.00928v1)**  
  Authors: Michael Steiner, Zhang Chen, Alexander Richard, Vasu Agrawal, Markus Steinberger, Michael Zollhöfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00928v1.pdf)  
  Keywords: dynamic, high-fidelity, compact, gaussian splatting, avatar, ar, 3d gaussian, human, motion  
- **[TRiGS: Temporal Rigid-Body Motion for Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2604.00538v1)**  
  Authors: Suwoong Yeom, Joonsik Nam, Seunggyu Choi, Lucas Yunkyu Lee, Sangmin Kim, Jaesik Park, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong, Sukju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00538v1.pdf)  
  Keywords: 4d, dynamic, body, gaussian splatting, ar, motion  
- **[GRVS: a Generalizable and Recurrent Approach to Monocular Dynamic View Synthesis](https://arxiv.org/abs/2603.29734v1)**  
  Authors: Thomas Tanay, Mohammed Brahimi, Michal Nazarczuk, Qingwen Zhang, Sibi Catley-Chandar, Arthur Moreau, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29734v1.pdf)  
  Keywords: 4d, dynamic, mapping, gaussian splatting, ar, efficient, motion  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, dynamic, high-fidelity, large scene, shadow, neural rendering, gaussian splatting, ar, understanding, efficient, motion, geometry  

### Few-shot

- **[TRACE: High-Fidelity 3D Scene Editing via Tangible Reconstruction and Geometry-Aligned Contextual Video Masking](https://arxiv.org/abs/2604.01207v1)**  
  Authors: Jiyuan Hu, Zechuan Zhang, Zongxin Yang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01207v1.pdf)  
  Keywords: high-fidelity, ar, geometry, sparse-view  
- **[Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty-aware Differentiable Optimization](https://arxiv.org/abs/2604.01030v1)**  
  Authors: Yueh-Cheng Liu, Jozef Hladký, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01030v1.pdf)  
  Keywords: fast, gaussian splatting, ar, 3d gaussian, sparse-view  
- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394v1)**  
  Authors: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29394v1.pdf)  
  Keywords: fast, gaussian splatting, ar, 3d gaussian, 3d reconstruction, sparse-view  
- **[\textit{4DSurf}: High-Fidelity Dynamic Scene Surface Reconstruction](https://arxiv.org/abs/2603.28064v1)**  
  Authors: Renjie Wu, Hongdong Li, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28064v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, sparse-view, motion, deformation, face, geometry  
- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516v2)**  
  Authors: Jiahao Niu, Rongjia Zheng, Wenju Xu, Wei-Shi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27516v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GrumpySloths/SGS_Intrinsic.github.io?style=social)](https://github.com/GrumpySloths/SGS_Intrinsic.github.io)  
  Keywords: illumination, shadow, gaussian splatting, sparse view, ar, sparse-view, semantic, 3d gaussian, geometry  
- **[Detailed Geometry and Appearance from Opportunistic Motion](https://arxiv.org/abs/2603.26665v1)**  
  Authors: Ryosuke Hirai, Kohei Yamashita, Antoine Guédon, Ryo Kawahara, Vincent Lepetit, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26665v1.pdf)  
  Keywords: illumination, gaussian splatting, sparse view, ar, motion, geometry  
- **[AirSplat: Alignment and Rating for Robust Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.25129v1)**  
  Authors: Minh-Quan Viet Bui, Jaeho Moon, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25129v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, sparse-view, 3d gaussian, geometry  
- **[EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](https://arxiv.org/abs/2603.21332v2)**  
  Authors: Haolan Xu, Keli Cheng, Lei Wang, Ning Bi, Xiaoming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21332v2.pdf)  
  Keywords: gaussian splatting, lighting, ar, nerf, 3d gaussian, motion, face, head, few-shot  
- **[UniSem: Generalizable Semantic 3D Reconstruction from Sparse Unposed Images](https://arxiv.org/abs/2603.17519v1)**  
  Authors: Guibiao Liao, Qian Ren, Kaimin Liao, Hua Wang, Zhi Chen, Luchao Wang, Yaohua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17519v1.pdf)  
  Keywords: gaussian splatting, ar, sparse-view, segmentation, semantic, 3d gaussian, 3d reconstruction, geometry  
- **[S2D: Sparse to Dense Lifting for 3D Reconstruction with Minimal Inputs](https://arxiv.org/abs/2603.10893v1)**  
  Authors: Yuzhou Ji, Qijian Tian, He Zhu, Xiaoqi Jiang, Guangzhi Cao, Lizhuang Ma, Yuan Xie, Xin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10893v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, sparse view, ar, understanding, 3d gaussian, efficient, 3d reconstruction  

### Geometry Reconstruction

*Showing the latest 50 out of 207 papers*

- **[ProDiG: Progressive Diffusion-Guided Gaussian Splatting for Aerial to Ground Reconstruction](https://arxiv.org/abs/2604.02003v1)**  
  Authors: Sirshapan Mitra, Yogesh S. Rawat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02003v1.pdf)  
  Keywords: dynamic, gaussian splatting, geometry, ar  
- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, understanding, segmentation, semantic, human, motion, face, tracking, geometry  
- **[F3DGS: Federated 3D Gaussian Splatting for Decentralized Multi-Agent World Modeling](https://arxiv.org/abs/2604.01605v1)**  
  Authors: Morui Zhu, Mohammad Dehghani Tezerjani, Mátyás Szántó, Márton Vaitkus, Song Fu, Qing Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01605v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, efficient, 3d reconstruction, head  
- **[Satellite-Free Training for Drone-View Geo-Localization](https://arxiv.org/abs/2604.01581v1)**  
  Authors: Tao Liu, Yingzhi Zhang, Kan Ren, Xiaoqi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01581v1.pdf)  
  Keywords: localization, gaussian splatting, ar, lightweight, 3d gaussian, geometry  
- **[LESV: Language Embedded Sparse Voxel Fusion for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2604.01388v1)**  
  Authors: Fusang Wang, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Fabien Moutarde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01388v1.pdf)  
  Keywords: gaussian splatting, vr, ar, understanding, semantic, 3d gaussian, head, geometry  
- **[TRACE: High-Fidelity 3D Scene Editing via Tangible Reconstruction and Geometry-Aligned Contextual Video Masking](https://arxiv.org/abs/2604.01207v1)**  
  Authors: Jiyuan Hu, Zechuan Zhang, Zongxin Yang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01207v1.pdf)  
  Keywords: high-fidelity, ar, geometry, sparse-view  
- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394v1)**  
  Authors: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29394v1.pdf)  
  Keywords: fast, gaussian splatting, ar, 3d gaussian, 3d reconstruction, sparse-view  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, dynamic, high-fidelity, large scene, shadow, neural rendering, gaussian splatting, ar, understanding, efficient, motion, geometry  
- **[LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting](https://arxiv.org/abs/2603.29209v1)**  
  Authors: Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29209v1.pdf)  
  Keywords: high-fidelity, illumination, shadow, gaussian splatting, vr, lighting, ar, 3d gaussian, efficient, geometry  
- **[LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2603.28431v3)**  
  Authors: Xuan Deng, Xiandong Meng, Hengyu Man, Qiang Zhu, Tiange Zhang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28431v3.pdf)  
  Keywords: real-time rendering, high-fidelity, compression, compact, gaussian splatting, ar, nerf, lightweight, 3d gaussian, head, geometry  

### Large Scene

- **[Neural Harmonic Textures for High-Quality Primitive Based Neural Reconstruction](https://arxiv.org/abs/2604.01204v1)**  
  Authors: Jorge Condor, Nicolas Moenne-Loccoz, Merlin Nimier-David, Piotr Didyk, Zan Gojcic, Qi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01204v1.pdf)  
  Keywords: large scene, gaussian splatting, ar, semantic, 3d gaussian  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, dynamic, high-fidelity, large scene, shadow, neural rendering, gaussian splatting, ar, understanding, efficient, motion, geometry  
- **[Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting](https://arxiv.org/abs/2603.29185v1)**  
  Authors: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29185v1.pdf)  
  Keywords: localization, outdoor, gaussian splatting, ar, efficient  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: large scene, neural rendering, gaussian splatting, ar, 3d gaussian, efficient, face, head  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: dynamic, tracking, outdoor, gaussian splatting, ar, slam, efficient, head  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: localization, outdoor, gaussian splatting, ar, 3d gaussian, geometry  
- **[EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.06216v1)**  
  Authors: Miriam Jäger, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06216v1.pdf)  
  Keywords: urban scene, face, gaussian splatting, ar, 3d gaussian, 3d reconstruction, geometry  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: relighting, relightable, illumination, fast, outdoor, gaussian splatting, reflection, lighting, ar, nerf, 3d gaussian, 3d reconstruction  
- **[Interactive Augmented Reality-enabled Outdoor Scene Visualization For Enhanced Real-time Disaster Response](https://arxiv.org/abs/2602.21874v1)**  
  Authors: Dimitrios Apostolakis, Georgios Angelidis, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21874v1.pdf)  
  Keywords: fast, outdoor, gaussian splatting, lighting, ar, lightweight, semantic, 3d gaussian, face  
- **[Large-scale Photorealistic Outdoor 3D Scene Reconstruction from UAV Imagery Using Gaussian Splatting Techniques](https://arxiv.org/abs/2602.20342v1)**  
  Authors: Christos Maikos, Georgios Angelidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20342v1.pdf)  
  Keywords: high-fidelity, outdoor, neural rendering, gaussian splatting, vr, ar, nerf, 3d gaussian, efficient, 3d reconstruction  

### Model Compression

*Showing the latest 50 out of 218 papers*

- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, segmentation, lightweight, 3d gaussian, motion, deformation, head  
- **[GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2604.01884v1)**  
  Authors: Xianben Yang, Tao Wang, Yuxuan Li, Yi Jin, Haibin Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01884v1.pdf)  
  Keywords: real-time rendering, dynamic, compact, gaussian splatting, ar, 3d gaussian  
- **[F3DGS: Federated 3D Gaussian Splatting for Decentralized Multi-Agent World Modeling](https://arxiv.org/abs/2604.01605v1)**  
  Authors: Morui Zhu, Mohammad Dehghani Tezerjani, Mátyás Szántó, Márton Vaitkus, Song Fu, Qing Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01605v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, efficient, 3d reconstruction, head  
- **[Satellite-Free Training for Drone-View Geo-Localization](https://arxiv.org/abs/2604.01581v1)**  
  Authors: Tao Liu, Yingzhi Zhang, Kan Ren, Xiaoqi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01581v1.pdf)  
  Keywords: localization, gaussian splatting, ar, lightweight, 3d gaussian, geometry  
- **[Autoregressive Appearance Prediction for 3D Gaussian Avatars](https://arxiv.org/abs/2604.00928v1)**  
  Authors: Michael Steiner, Zhang Chen, Alexander Richard, Vasu Agrawal, Markus Steinberger, Michael Zollhöfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00928v1.pdf)  
  Keywords: dynamic, high-fidelity, compact, gaussian splatting, avatar, ar, 3d gaussian, human, motion  
- **[Compact Keyframe-Optimized Multi-Agent Gaussian Splatting SLAM](https://arxiv.org/abs/2604.00804v1)**  
  Authors: Monica M. Q. Li, Pierre-Yves Lajoie, Jialiang Liu, Giovanni Beltrame  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00804v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lemonci/coko-slam?style=social)](https://github.com/lemonci/coko-slam)  
  Keywords: mapping, compact, gaussian splatting, localization, ar, lightweight, 3d gaussian, efficient, slam  
- **[DirectFisheye-GS: Enabling Native Fisheye Input in Gaussian Splatting with Cross-View Joint Optimization](https://arxiv.org/abs/2604.00648v1)**  
  Authors: Zhengxian Yang, Fei Xie, Xutao Xue, Rui Zhang, Taicheng Huang, Yang Liu, Mengqi Ji, Tao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00648v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, vr, ar, 3d gaussian, efficient  
- **[GRVS: a Generalizable and Recurrent Approach to Monocular Dynamic View Synthesis](https://arxiv.org/abs/2603.29734v1)**  
  Authors: Thomas Tanay, Mohammed Brahimi, Michal Nazarczuk, Qingwen Zhang, Sibi Catley-Chandar, Arthur Moreau, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29734v1.pdf)  
  Keywords: 4d, dynamic, mapping, gaussian splatting, ar, efficient, motion  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, dynamic, high-fidelity, large scene, shadow, neural rendering, gaussian splatting, ar, understanding, efficient, motion, geometry  
- **[LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting](https://arxiv.org/abs/2603.29209v1)**  
  Authors: Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29209v1.pdf)  
  Keywords: high-fidelity, illumination, shadow, gaussian splatting, vr, lighting, ar, 3d gaussian, efficient, geometry  

### Quality Enhancement

*Showing the latest 50 out of 130 papers*

- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, segmentation, lightweight, 3d gaussian, motion, deformation, head  
- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, understanding, segmentation, semantic, human, motion, face, tracking, geometry  
- **[TRACE: High-Fidelity 3D Scene Editing via Tangible Reconstruction and Geometry-Aligned Contextual Video Masking](https://arxiv.org/abs/2604.01207v1)**  
  Authors: Jiyuan Hu, Zechuan Zhang, Zongxin Yang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01207v1.pdf)  
  Keywords: high-fidelity, ar, geometry, sparse-view  
- **[Autoregressive Appearance Prediction for 3D Gaussian Avatars](https://arxiv.org/abs/2604.00928v1)**  
  Authors: Michael Steiner, Zhang Chen, Alexander Richard, Vasu Agrawal, Markus Steinberger, Michael Zollhöfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00928v1.pdf)  
  Keywords: dynamic, high-fidelity, compact, gaussian splatting, avatar, ar, 3d gaussian, human, motion  
- **[DirectFisheye-GS: Enabling Native Fisheye Input in Gaussian Splatting with Cross-View Joint Optimization](https://arxiv.org/abs/2604.00648v1)**  
  Authors: Zhengxian Yang, Fei Xie, Xutao Xue, Rui Zhang, Taicheng Huang, Yang Liu, Mengqi Ji, Tao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00648v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, vr, ar, 3d gaussian, efficient  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, dynamic, high-fidelity, large scene, shadow, neural rendering, gaussian splatting, ar, understanding, efficient, motion, geometry  
- **[LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting](https://arxiv.org/abs/2603.29209v1)**  
  Authors: Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29209v1.pdf)  
  Keywords: high-fidelity, illumination, shadow, gaussian splatting, vr, lighting, ar, 3d gaussian, efficient, geometry  
- **[Efficient Camera Pose Augmentation for View Generalization in Robotic Policy Learning](https://arxiv.org/abs/2603.29192v1)**  
  Authors: Sen Wang, Huaiyi Dong, Jingyi Tian, Jiayi Li, Zhuo Yang, Tongtong Cao, Anlin Chen, Shuang Wu, Le Wang, Sanping Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29192v1.pdf)  
  Keywords: high-fidelity, mapping, gaussian splatting, ar, 3d gaussian, efficient  
- **[Gleanmer: A 6 mW SoC for Real-Time 3D Gaussian Occupancy Mapping](https://arxiv.org/abs/2603.29005v1)**  
  Authors: Zih-Sing Fu, Peter Zhi Xuan Li, Sertac Karaman, Vivienne Sze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29005v1.pdf)  
  Keywords: high-fidelity, mapping, compact, vr, ar, 3d gaussian, efficient  
- **[LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2603.28431v3)**  
  Authors: Xuan Deng, Xiandong Meng, Hengyu Man, Qiang Zhu, Tiange Zhang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28431v3.pdf)  
  Keywords: real-time rendering, high-fidelity, compression, compact, gaussian splatting, ar, nerf, lightweight, 3d gaussian, head, geometry  

### Ray Tracing

- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: gaussian splatting, reflection, ar, face, ray tracing  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: reflection, ar, 3d gaussian, efficient, ray casting  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: mapping, tracking, localization, gaussian splatting, ar, semantic, 3d gaussian, efficient, face, slam, ray tracing  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: relightable, mapping, shadow, gaussian splatting, reflection, ar, 3d gaussian, ray tracing  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: real-time rendering, path tracing, ar, 3d gaussian, face, geometry  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: real-time rendering, high-fidelity, fast, gaussian splatting, ar, nerf, 3d gaussian, efficient, face, ray tracing, geometry  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: mapping, gaussian splatting, ar, 3d gaussian, survey, ray tracing  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: real-time rendering, high-fidelity, ray marching, gaussian splatting, ar, 3d gaussian, efficient  
- **[Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction](https://arxiv.org/abs/2603.08503v1)**  
  Authors: Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08503v1.pdf) | [![GitHub](https://img.shields.io/github/stars/1170632760/Spherical-GOF?style=social)](https://github.com/1170632760/Spherical-GOF)  
  Keywords: robotics, fast, gaussian splatting, ar, 3d gaussian, ray casting, efficient, geometry  
- **[Ref-DGS: Reflective Dual Gaussian Splatting](https://arxiv.org/abs/2603.07664v2)**  
  Authors: Ningjing Fan, Yiqun Wang, Dongming Yan, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07664v2.pdf)  
  Keywords: fast, gaussian splatting, reflection, ar, lightweight, efficient, face, ray tracing, geometry  

### Relighting

*Showing the latest 50 out of 73 papers*

- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: gaussian splatting, reflection, ar, face, ray tracing  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, dynamic, high-fidelity, large scene, shadow, neural rendering, gaussian splatting, ar, understanding, efficient, motion, geometry  
- **[LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting](https://arxiv.org/abs/2603.29209v1)**  
  Authors: Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29209v1.pdf)  
  Keywords: high-fidelity, illumination, shadow, gaussian splatting, vr, lighting, ar, 3d gaussian, efficient, geometry  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: reflection, ar, 3d gaussian, efficient, ray casting  
- **[ObjectMorpher: 3D-Aware Image Editing via Deformable 3DGS Models](https://arxiv.org/abs/2603.28152v1)**  
  Authors: Yuhuan Xie, Aoxuan Pan, Yi-Hua Huang, Chirui Chang, Peng Dai, Xin Yu, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28152v1.pdf)  
  Keywords: fast, gaussian splatting, lighting, ar, 3d gaussian, deformation, geometry  
- **[Physically Inspired Gaussian Splatting for HDR Novel View Synthesis](https://arxiv.org/abs/2603.28020v1)**  
  Authors: Huimin Zeng, Yue Bai, Hailing Wang, Yun Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huimin-zeng.github.io/PhysHDR-GS)  
  Keywords: real-time rendering, dynamic, illumination, gaussian splatting, ar  
- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516v2)**  
  Authors: Jiahao Niu, Rongjia Zheng, Wenju Xu, Wei-Shi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27516v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GrumpySloths/SGS_Intrinsic.github.io?style=social)](https://github.com/GrumpySloths/SGS_Intrinsic.github.io)  
  Keywords: illumination, shadow, gaussian splatting, sparse view, ar, sparse-view, semantic, 3d gaussian, geometry  
- **[Detailed Geometry and Appearance from Opportunistic Motion](https://arxiv.org/abs/2603.26665v1)**  
  Authors: Ryosuke Hirai, Kohei Yamashita, Antoine Guédon, Ryo Kawahara, Vincent Lepetit, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26665v1.pdf)  
  Keywords: illumination, gaussian splatting, sparse view, ar, motion, geometry  
- **[GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport](https://arxiv.org/abs/2603.26181v1)**  
  Authors: Youngju Na, Jaeseong Yun, Soohyun Ryu, Hyunsu Kim, Sung-Eui Yoon, Suyong Yeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26181v1.pdf)  
  Keywords: relighting, localization, gaussian splatting, lighting, ar, 3d gaussian, face, geometry  
- **[R-PGA: Robust Physical Adversarial Camouflage Generation via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2603.26067v1)**  
  Authors: Tianrui Lou, Siyuan Liang, Jiawei Liang, Yuze Gao, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26067v1.pdf)  
  Keywords: dynamic, relightable, mapping, illumination, gaussian splatting, lighting, ar, 3d gaussian, autonomous driving  

### SLAM

*Showing the latest 50 out of 75 papers*

- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, understanding, segmentation, semantic, human, motion, face, tracking, geometry  
- **[Satellite-Free Training for Drone-View Geo-Localization](https://arxiv.org/abs/2604.01581v1)**  
  Authors: Tao Liu, Yingzhi Zhang, Kan Ren, Xiaoqi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01581v1.pdf)  
  Keywords: localization, gaussian splatting, ar, lightweight, 3d gaussian, geometry  
- **[Compact Keyframe-Optimized Multi-Agent Gaussian Splatting SLAM](https://arxiv.org/abs/2604.00804v1)**  
  Authors: Monica M. Q. Li, Pierre-Yves Lajoie, Jialiang Liu, Giovanni Beltrame  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00804v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lemonci/coko-slam?style=social)](https://github.com/lemonci/coko-slam)  
  Keywords: mapping, compact, gaussian splatting, localization, ar, lightweight, 3d gaussian, efficient, slam  
- **[GRVS: a Generalizable and Recurrent Approach to Monocular Dynamic View Synthesis](https://arxiv.org/abs/2603.29734v1)**  
  Authors: Thomas Tanay, Mohammed Brahimi, Michal Nazarczuk, Qingwen Zhang, Sibi Catley-Chandar, Arthur Moreau, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29734v1.pdf)  
  Keywords: 4d, dynamic, mapping, gaussian splatting, ar, efficient, motion  
- **[Efficient Camera Pose Augmentation for View Generalization in Robotic Policy Learning](https://arxiv.org/abs/2603.29192v1)**  
  Authors: Sen Wang, Huaiyi Dong, Jingyi Tian, Jiayi Li, Zhuo Yang, Tongtong Cao, Anlin Chen, Shuang Wu, Le Wang, Sanping Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29192v1.pdf)  
  Keywords: high-fidelity, mapping, gaussian splatting, ar, 3d gaussian, efficient  
- **[Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting](https://arxiv.org/abs/2603.29185v1)**  
  Authors: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29185v1.pdf)  
  Keywords: localization, outdoor, gaussian splatting, ar, efficient  
- **[Gleanmer: A 6 mW SoC for Real-Time 3D Gaussian Occupancy Mapping](https://arxiv.org/abs/2603.29005v1)**  
  Authors: Zih-Sing Fu, Peter Zhi Xuan Li, Sertac Karaman, Vivienne Sze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29005v1.pdf)  
  Keywords: high-fidelity, mapping, compact, vr, ar, 3d gaussian, efficient  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: mapping, tracking, localization, gaussian splatting, ar, semantic, 3d gaussian, efficient, face, slam, ray tracing  
- **[GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport](https://arxiv.org/abs/2603.26181v1)**  
  Authors: Youngju Na, Jaeseong Yun, Soohyun Ryu, Hyunsu Kim, Sung-Eui Yoon, Suyong Yeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26181v1.pdf)  
  Keywords: relighting, localization, gaussian splatting, lighting, ar, 3d gaussian, face, geometry  
- **[R-PGA: Robust Physical Adversarial Camouflage Generation via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2603.26067v1)**  
  Authors: Tianrui Lou, Siyuan Liang, Jiawei Liang, Yuze Gao, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26067v1.pdf)  
  Keywords: dynamic, relightable, mapping, illumination, gaussian splatting, lighting, ar, 3d gaussian, autonomous driving  

### Scene Understanding

*Showing the latest 50 out of 133 papers*

- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, segmentation, lightweight, 3d gaussian, motion, deformation, head  
- **[A3R: Agentic Affordance Reasoning via Cross-Dimensional Evidence in 3D Gaussian Scenes](https://arxiv.org/abs/2604.01882v1)**  
  Authors: Di Li, Jie Feng, Guanbin Li, Ronghua Shang, Yuhui Zheng, Weisheng Dong, Guangming Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01882v1.pdf)  
  Keywords: semantic, 3d gaussian, ar  
- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678v1)**  
  Authors: Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01678v1.pdf)  
  Keywords: 4d, dynamic, high-fidelity, gaussian splatting, ar, understanding, segmentation, semantic, human, motion, face, tracking, geometry  
- **[LESV: Language Embedded Sparse Voxel Fusion for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2604.01388v1)**  
  Authors: Fusang Wang, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Fabien Moutarde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01388v1.pdf)  
  Keywords: gaussian splatting, vr, ar, understanding, semantic, 3d gaussian, head, geometry  
- **[Neural Harmonic Textures for High-Quality Primitive Based Neural Reconstruction](https://arxiv.org/abs/2604.01204v1)**  
  Authors: Jorge Condor, Nicolas Moenne-Loccoz, Merlin Nimier-David, Piotr Didyk, Zan Gojcic, Qi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01204v1.pdf)  
  Keywords: large scene, gaussian splatting, ar, semantic, 3d gaussian  
- **[DLWM: Dual Latent World Models enable Holistic Gaussian-centric Pre-training in Autonomous Driving](https://arxiv.org/abs/2604.00969v1)**  
  Authors: Yiyao Zhu, Ying Xue, Haiming Zhang, Guangfeng Jiang, Wending Zhou, Xu Yan, Jiantao Gao, Yingjie Cai, Bingbing Liu, Zhen Li, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00969v1.pdf)  
  Keywords: 4d, ar, semantic, 3d gaussian, motion, autonomous driving  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, dynamic, high-fidelity, large scene, shadow, neural rendering, gaussian splatting, ar, understanding, efficient, motion, geometry  
- **[DipGuava: Disentangling Personalized Gaussian Features for 3D Head Avatars from Monocular Video](https://arxiv.org/abs/2603.28003v1)**  
  Authors: Jeonghaeng Lee, Seok Keun Choi, Zhixuan Li, Weisi Lin, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28003v1.pdf)  
  Keywords: dynamic, avatar, ar, semantic, 3d gaussian, deformation, head, geometry  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: mapping, tracking, localization, gaussian splatting, ar, semantic, 3d gaussian, efficient, face, slam, ray tracing  
- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516v2)**  
  Authors: Jiahao Niu, Rongjia Zheng, Wenju Xu, Wei-Shi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27516v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GrumpySloths/SGS_Intrinsic.github.io?style=social)](https://github.com/GrumpySloths/SGS_Intrinsic.github.io)  
  Keywords: illumination, shadow, gaussian splatting, sparse view, ar, sparse-view, semantic, 3d gaussian, geometry  



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