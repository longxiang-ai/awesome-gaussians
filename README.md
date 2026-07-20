# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-07-20 01:58:36

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

- [3DGS Surveys](#3dgs-surveys) (3 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (96 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (173 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (184 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (44 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (215 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (22 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (185 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (119 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (14 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (54 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (75 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (117 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: 3d gaussian, mapping, slam, dynamic, localization, high-fidelity, tracking, survey, ar, efficient  
- **[Recent Advances and Trends in Learning-based 3D Representations](https://arxiv.org/abs/2606.04871v1)**  
  Authors: Adrien Schockaert, Hamid Laga, Hazem Wannous, Vincent Magnier, Guillaume Dufaye, Jean-françois Witz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.04871v1.pdf)  
  Keywords: 3d gaussian, medical, motion, autonomous driving, vr, neural rendering, gaussian splatting, 3d reconstruction, compact, 4d, recognition, survey, ar  
- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137v1)**  
  Authors: Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00137v1.pdf)  
  Keywords: mapping, geometry, gaussian splatting, animation, survey, ar  

### Acceleration

*Showing the latest 50 out of 96 papers*

- **[JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting](https://arxiv.org/abs/2607.14990v1)**  
  Authors: Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14990v1.pdf)  
  Keywords: 3d gaussian, face, geometry, real-time rendering, motion, fast, gaussian splatting, ar  
- **[Compression of 3D Gaussian Splatting Data Using GPU-friendly Graphics Texture Coding](https://arxiv.org/abs/2607.14513v1)**  
  Authors: Amir Said, Randall Rauwendaal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14513v1.pdf)  
  Keywords: 3d gaussian, acceleration, gaussian splatting, compression, ar, efficient  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, motion, fast, slam, gaussian splatting, large scene, recognition, ar, efficient  
- **[G$^2$SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction](https://arxiv.org/abs/2607.14470v1)**  
  Authors: Dasong Gao, Vivienne Sze, Sertac Karaman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14470v1.pdf)  
  Keywords: 3d gaussian, face, ar, geometry, fast, gaussian splatting, high-fidelity, lightweight, efficient  
- **[Bake It Till You Make It: Ultrafast Spatial Texture-Atlas Splatting](https://arxiv.org/abs/2607.13808v1)**  
  Authors: Neel Kelkar, Simon Niedermayr, Kaloian Petkov, Klaus Engel, Rüdiger Westermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13808v1.pdf)  
  Keywords: 3d gaussian, mapping, geometry, fast, gaussian splatting, compact, ar, efficient  
- **[Calibrated Closed-Form Uncertainty for Radiative Gaussian Splatting in Sparse-View CT](https://arxiv.org/abs/2607.13682v1)**  
  Authors: Chulin Zhao, Yiran Xu, Shu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13682v1.pdf)  
  Keywords: sparse-view, gaussian splatting, fast, ar  
- **[SpeedyGS: Content-Aware 3D Gaussian Splatting Compression via Two-Stage Optimization](https://arxiv.org/abs/2607.12656v1)**  
  Authors: Junteng Zhang, Tong Chen, Yuxin Zhao, Yibo Shi, Jing Wang, Zhan Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12656v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, head, fast, gaussian splatting, compression, compact, lightweight, efficient  
- **[Implicit 4D Gaussian Splatting for Fast Motion with Large Inter-Frame Displacements](https://arxiv.org/abs/2607.12362v1)**  
  Authors: Seung-gyeom Kim, Areum Kim, Yongjae Yoo, Sukmin Yun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12362v1.pdf)  
  Keywords: ar, head, motion, fast, gaussian splatting, 4d, lightweight  
- **[HyperGS: Fast and Generalizable Gaussian Video Representation](https://arxiv.org/abs/2607.11500v1)**  
  Authors: Fatimah Zohra, Chen Zhao, Shuming Liu, Yahya Al Malallah, Bernard Ghanem  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11500v1.pdf)  
  Keywords: dynamic, gaussian splatting, fast, ar  
- **[Grassmannian Splatting I: Moving rank-2 Spacetime Surfels for Dynamic Scene Rendering](https://arxiv.org/abs/2607.10489v1)**  
  Authors: Aaron Maurice Berman, Shantanu Dave  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.10489v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PaulCelanCoding/grassmannian-splatting?style=social)](https://github.com/PaulCelanCoding/grassmannian-splatting)  
  Keywords: face, deformation, motion, fast, nerf, gaussian splatting, dynamic, 4d, ar  

### Applications

*Showing the latest 50 out of 498 papers*

- **[Rendering 3D Gaussians on a Graph Processor](https://arxiv.org/abs/2607.15951v1)**  
  Authors: Nicholas Fry, Ignacio Alzugaray, Mark Pupilli, Paul H. J. Kelly, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15951v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nmjfry.github.io/ipu-3dgs)  
  Keywords: 3d gaussian, ar, efficient  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: human, 3d gaussian, face, ray tracing, geometry, motion, reflection, gaussian splatting, dynamic, high-fidelity, ar  
- **[ImprovedVBGS: Real-time Continual Variational Bayes Gaussian Splatting](https://arxiv.org/abs/2607.15542v1)**  
  Authors: Damani Mguni-Coker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15542v1.pdf)  
  Keywords: nerf, gaussian splatting, dynamic, ar, robotics  
- **[E3DGS: Unified Geometric-Photometric Equivariance for 3D Gaussian Splatting via Color-as-Geometry Embedding](https://arxiv.org/abs/2607.15536v1)**  
  Authors: Chankyo Kim, Maani Ghaffari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15536v1.pdf)  
  Keywords: 3d gaussian, geometry, body, gaussian splatting, ar, efficient  
- **[RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping](https://arxiv.org/abs/2607.15048v1)**  
  Authors: Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15048v1.pdf)  
  Keywords: face, 3d gaussian, semantic, mapping, autonomous driving, compact, ar, efficient  
- **[AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight](https://arxiv.org/abs/2607.14997v1)**  
  Authors: Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14997v1.pdf)  
  Keywords: 3d gaussian, semantic, motion, gaussian splatting, dynamic, tracking, ar  
- **[JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting](https://arxiv.org/abs/2607.14990v1)**  
  Authors: Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14990v1.pdf)  
  Keywords: 3d gaussian, face, geometry, real-time rendering, motion, fast, gaussian splatting, ar  
- **[Compression of 3D Gaussian Splatting Data Using GPU-friendly Graphics Texture Coding](https://arxiv.org/abs/2607.14513v1)**  
  Authors: Amir Said, Randall Rauwendaal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14513v1.pdf)  
  Keywords: 3d gaussian, acceleration, gaussian splatting, compression, ar, efficient  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, motion, fast, slam, gaussian splatting, large scene, recognition, ar, efficient  
- **[G$^2$SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction](https://arxiv.org/abs/2607.14470v1)**  
  Authors: Dasong Gao, Vivienne Sze, Sertac Karaman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14470v1.pdf)  
  Keywords: 3d gaussian, face, ar, geometry, fast, gaussian splatting, high-fidelity, lightweight, efficient  

### Avatar Generation

*Showing the latest 50 out of 173 papers*

- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: human, 3d gaussian, face, ray tracing, geometry, motion, reflection, gaussian splatting, dynamic, high-fidelity, ar  
- **[E3DGS: Unified Geometric-Photometric Equivariance for 3D Gaussian Splatting via Color-as-Geometry Embedding](https://arxiv.org/abs/2607.15536v1)**  
  Authors: Chankyo Kim, Maani Ghaffari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15536v1.pdf)  
  Keywords: 3d gaussian, geometry, body, gaussian splatting, ar, efficient  
- **[RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping](https://arxiv.org/abs/2607.15048v1)**  
  Authors: Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15048v1.pdf)  
  Keywords: face, 3d gaussian, semantic, mapping, autonomous driving, compact, ar, efficient  
- **[JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting](https://arxiv.org/abs/2607.14990v1)**  
  Authors: Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14990v1.pdf)  
  Keywords: 3d gaussian, face, geometry, real-time rendering, motion, fast, gaussian splatting, ar  
- **[G$^2$SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction](https://arxiv.org/abs/2607.14470v1)**  
  Authors: Dasong Gao, Vivienne Sze, Sertac Karaman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14470v1.pdf)  
  Keywords: 3d gaussian, face, ar, geometry, fast, gaussian splatting, high-fidelity, lightweight, efficient  
- **[T3HG-Editor: Text-driven 3D Human Garment Editing with Body Priors Embedded in SMPL-X](https://arxiv.org/abs/2607.13654v1)**  
  Authors: Shaoru Sun, Xingtao Wang, Zihan Ma, Wenrui Li, Jiantao Zhou, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13654v1.pdf)  
  Keywords: human, 3d gaussian, face, semantic, geometry, body, high-fidelity, ar  
- **[Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation](https://arxiv.org/abs/2607.13154v2)**  
  Authors: Lingxiao Guo, Huanyu Li, Guanya Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13154v2.pdf)  
  Keywords: human, body, motion, gaussian splatting, ar  
- **[SpeedyGS: Content-Aware 3D Gaussian Splatting Compression via Two-Stage Optimization](https://arxiv.org/abs/2607.12656v1)**  
  Authors: Junteng Zhang, Tong Chen, Yuxin Zhao, Yibo Shi, Jing Wang, Zhan Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12656v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, head, fast, gaussian splatting, compression, compact, lightweight, efficient  
- **[Implicit 4D Gaussian Splatting for Fast Motion with Large Inter-Frame Displacements](https://arxiv.org/abs/2607.12362v1)**  
  Authors: Seung-gyeom Kim, Areum Kim, Yongjae Yoo, Sukmin Yun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12362v1.pdf)  
  Keywords: ar, head, motion, fast, gaussian splatting, 4d, lightweight  
- **[VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation](https://arxiv.org/abs/2607.12356v2)**  
  Authors: Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao, Yan Wu, Wei-Yun Yau, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12356v2.pdf)  
  Keywords: human, 3d gaussian, semantic, mapping, geometry, compact, ar  

### Dynamic Scene

*Showing the latest 50 out of 184 papers*

- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: human, 3d gaussian, face, ray tracing, geometry, motion, reflection, gaussian splatting, dynamic, high-fidelity, ar  
- **[ImprovedVBGS: Real-time Continual Variational Bayes Gaussian Splatting](https://arxiv.org/abs/2607.15542v1)**  
  Authors: Damani Mguni-Coker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15542v1.pdf)  
  Keywords: nerf, gaussian splatting, dynamic, ar, robotics  
- **[AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight](https://arxiv.org/abs/2607.14997v1)**  
  Authors: Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14997v1.pdf)  
  Keywords: 3d gaussian, semantic, motion, gaussian splatting, dynamic, tracking, ar  
- **[JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting](https://arxiv.org/abs/2607.14990v1)**  
  Authors: Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14990v1.pdf)  
  Keywords: 3d gaussian, face, geometry, real-time rendering, motion, fast, gaussian splatting, ar  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, motion, fast, slam, gaussian splatting, large scene, recognition, ar, efficient  
- **[Instant NuRec: Feed-Forward 3D Gaussian Reconstruction for Driving Scene Simulation](https://arxiv.org/abs/2607.14203v1)**  
  Authors: NVIDIA, :, Jiahui Huang, Jiawei Ren, Michal Tyszkiewicz, Bjoern Haefner, Michael Shelley, Xin Kang, Seung Wook Kim, Ning Xu, Qi Wu, Janick Martinez Esturo, Shengyu Huang, Nick Schneider, Laura Leal-Taixe, Zan Gojcic, Sanja Fidler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14203v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, gaussian splatting, dynamic, ar  
- **[Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](https://arxiv.org/abs/2607.13451v1)**  
  Authors: Shivansh Patel, Kaifeng Zhang, Sanjay Pokkali, Svetlana Lazebnik, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13451v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, dynamic, ar  
- **[Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation](https://arxiv.org/abs/2607.13154v2)**  
  Authors: Lingxiao Guo, Huanyu Li, Guanya Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13154v2.pdf)  
  Keywords: human, body, motion, gaussian splatting, ar  
- **[Implicit 4D Gaussian Splatting for Fast Motion with Large Inter-Frame Displacements](https://arxiv.org/abs/2607.12362v1)**  
  Authors: Seung-gyeom Kim, Areum Kim, Yongjae Yoo, Sukmin Yun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12362v1.pdf)  
  Keywords: ar, head, motion, fast, gaussian splatting, 4d, lightweight  
- **[HyperGS: Fast and Generalizable Gaussian Video Representation](https://arxiv.org/abs/2607.11500v1)**  
  Authors: Fatimah Zohra, Chen Zhao, Shuming Liu, Yahya Al Malallah, Bernard Ghanem  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11500v1.pdf)  
  Keywords: dynamic, gaussian splatting, fast, ar  

### Few-shot

- **[Calibrated Closed-Form Uncertainty for Radiative Gaussian Splatting in Sparse-View CT](https://arxiv.org/abs/2607.13682v1)**  
  Authors: Chulin Zhao, Yiran Xu, Shu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13682v1.pdf)  
  Keywords: sparse-view, gaussian splatting, fast, ar  
- **[MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction](https://arxiv.org/abs/2607.10792v1)**  
  Authors: Jinqian Yang, Yichen Wu, Wanhua Li, Haokun Lin, Renzhen Wang, Xiangchu Feng, Xixi Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.10792v1.pdf)  
  Keywords: 3d gaussian, sparse-view, semantic, geometry, neural rendering, gaussian splatting, high-fidelity, ar  
- **[Rendering-Aware Bayesian 3D Gaussian Splatting with Native Uncertainty and Adaptive Complexity Control](https://arxiv.org/abs/2607.05522v1)**  
  Authors: Gaoxiang Jia, Vikram Appia, Junzhou Huang, Xinlei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05522v1.pdf)  
  Keywords: 3d gaussian, geometry, gaussian splatting, sparse view, ar  
- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771v1)**  
  Authors: Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03771v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/VOP-GS)  
  Keywords: 3d gaussian, face, ar, geometry, gaussian splatting, large scene, sparse view, efficient  
- **[Sparse-View Surface Reconstruction using Gaussian Splatting through High-Confidence Depth Propagation with Normal Priors](https://arxiv.org/abs/2607.03765v1)**  
  Authors: Liang Han, Bangcai Wei, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03765v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/DP-GS)  
  Keywords: 3d gaussian, sparse-view, face, ar, geometry, gaussian splatting, 3d reconstruction, high-fidelity, sparse view  
- **[Fast 3D Foundation Model Initialized Gaussian Splatting](https://arxiv.org/abs/2607.03209v1)**  
  Authors: Anurag Dalal, Daniel Hagen, Kjell G. Robbersmyr, Kristian Muri Knausgård  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03209v1.pdf)  
  Keywords: 3d gaussian, sparse-view, motion, vr, fast, nerf, gaussian splatting, ar, robotics  
- **[Improving Sparse-View 3DGS Generalization via Flat Minima Optimization](https://arxiv.org/abs/2607.00885v1)**  
  Authors: Kangmin Seo, Sangeek Hyun, MinKyu Lee, Jae-Pil Heo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00885v1.pdf)  
  Keywords: 3d gaussian, sparse-view, ar, real-time rendering, fast, nerf, neural rendering, gaussian splatting, dynamic, lightweight, efficient  
- **[AugSplat: Radiance Field-Informed Gaussian Splatting for Sparse-View Settings](https://arxiv.org/abs/2606.31556v1)**  
  Authors: Lorenzo Lazzaroni, Riccardo Bollati, Daniel Barath, Michael Niemeyer, Keisuke Tateno  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31556v1.pdf)  
  Keywords: sparse-view, geometry, real-time rendering, nerf, gaussian splatting, ar  
- **[StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors](https://arxiv.org/abs/2606.30545v2)**  
  Authors: Wenhao Yuan, Yiyuan Ge, Deli Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30545v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://stringerywh00.github.io/StereoGS_project_page)  
  Keywords: 3d gaussian, sparse-view, face, geometry, head, nerf, gaussian splatting, dynamic, ar  
- **[HiReFF: High-Resolution Feedforward Human Reconstruction from Uncalibrated Sparse-View Video](https://arxiv.org/abs/2606.29333v1)**  
  Authors: Yiming Jiang, Hanzhang Tu, Wenfeng Song, Siyou Lin, Liang An, Shuai Li, Aimin Hao, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29333v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://iridescentjiang.github.io/HiReFF)  
  Keywords: human, 3d gaussian, sparse-view, head, vr, ar, efficient  

### Geometry Reconstruction

*Showing the latest 50 out of 215 papers*

- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: human, 3d gaussian, face, ray tracing, geometry, motion, reflection, gaussian splatting, dynamic, high-fidelity, ar  
- **[E3DGS: Unified Geometric-Photometric Equivariance for 3D Gaussian Splatting via Color-as-Geometry Embedding](https://arxiv.org/abs/2607.15536v1)**  
  Authors: Chankyo Kim, Maani Ghaffari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15536v1.pdf)  
  Keywords: 3d gaussian, geometry, body, gaussian splatting, ar, efficient  
- **[JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting](https://arxiv.org/abs/2607.14990v1)**  
  Authors: Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14990v1.pdf)  
  Keywords: 3d gaussian, face, geometry, real-time rendering, motion, fast, gaussian splatting, ar  
- **[G$^2$SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction](https://arxiv.org/abs/2607.14470v1)**  
  Authors: Dasong Gao, Vivienne Sze, Sertac Karaman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14470v1.pdf)  
  Keywords: 3d gaussian, face, ar, geometry, fast, gaussian splatting, high-fidelity, lightweight, efficient  
- **[Bake It Till You Make It: Ultrafast Spatial Texture-Atlas Splatting](https://arxiv.org/abs/2607.13808v1)**  
  Authors: Neel Kelkar, Simon Niedermayr, Kaloian Petkov, Klaus Engel, Rüdiger Westermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13808v1.pdf)  
  Keywords: 3d gaussian, mapping, geometry, fast, gaussian splatting, compact, ar, efficient  
- **[T3HG-Editor: Text-driven 3D Human Garment Editing with Body Priors Embedded in SMPL-X](https://arxiv.org/abs/2607.13654v1)**  
  Authors: Shaoru Sun, Xingtao Wang, Zihan Ma, Wenrui Li, Jiantao Zhou, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13654v1.pdf)  
  Keywords: human, 3d gaussian, face, semantic, geometry, body, high-fidelity, ar  
- **[COLMAR: Cooperative View Policy Learning for Multi-Agent Active 3D Reconstruction](https://arxiv.org/abs/2607.13524v1)**  
  Authors: Phu Pham, Damon Conover, Aniket Bera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13524v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, 3d reconstruction, high-fidelity, ar  
- **[SpeedyGS: Content-Aware 3D Gaussian Splatting Compression via Two-Stage Optimization](https://arxiv.org/abs/2607.12656v1)**  
  Authors: Junteng Zhang, Tong Chen, Yuxin Zhao, Yibo Shi, Jing Wang, Zhan Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12656v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, head, fast, gaussian splatting, compression, compact, lightweight, efficient  
- **[GeoFovea-GS: Geometry-Aware Cross-Layer Gaussian Splatting for Wireless Aerial VR](https://arxiv.org/abs/2607.12641v1)**  
  Authors: Zeyi Ren, Wencheng Yan, Jiawen Zhang, Jintao Yan, Sheng Zhou, Zhisheng Niu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12641v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, vr, gaussian splatting, compact, lightweight, efficient  
- **[VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation](https://arxiv.org/abs/2607.12356v2)**  
  Authors: Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao, Yan Wu, Wei-Yun Yau, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12356v2.pdf)  
  Keywords: human, 3d gaussian, semantic, mapping, geometry, compact, ar  

### Large Scene

- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, motion, fast, slam, gaussian splatting, large scene, recognition, ar, efficient  
- **[GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors](https://arxiv.org/abs/2607.11184v1)**  
  Authors: Ruilan Gao, Letian Jin, Yu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11184v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rlgao.github.io/geogs_slam)  
  Keywords: 3d gaussian, mapping, geometry, slam, outdoor, gaussian splatting, tracking, ar  
- **[Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction](https://arxiv.org/abs/2607.08769v1)**  
  Authors: Weijian Chen, Weibo Yao, Yuhang Zhang, Xiaolin Tang, Guo Wang, Weijun Zhang, Xitong Gao, Yihao Chen, Hongde Qin, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08769v1.pdf)  
  Keywords: 3d gaussian, geometry, outdoor, gaussian splatting, ar  
- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771v1)**  
  Authors: Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03771v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/VOP-GS)  
  Keywords: 3d gaussian, face, ar, geometry, gaussian splatting, large scene, sparse view, efficient  
- **[Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673v1)**  
  Authors: Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu, Krishna Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00673v1.pdf)  
  Keywords: human, 3d gaussian, deformation, outdoor, ar  
- **[GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping](https://arxiv.org/abs/2606.30809v1)**  
  Authors: Annika Thomas, Mason Peterson, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30809v1.pdf)  
  Keywords: 3d gaussian, mapping, geometry, outdoor, gaussian splatting, ar  
- **[Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes](https://arxiv.org/abs/2606.30436v1)**  
  Authors: Sicheng Yu, Dongxu Shen, Beizhen Zhao, Guanzhi Ding, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30436v1.pdf)  
  Keywords: 3d gaussian, mapping, head, motion, slam, outdoor, gaussian splatting, dynamic, high-fidelity, tracking, ar, efficient  
- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)**  
  Authors: Leshu Li, Jie Peng, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/UMN-ZhaoLab/Pocket-SLAM.git?style=social)](https://github.com/UMN-ZhaoLab/Pocket-SLAM.git)  
  Keywords: 3d gaussian, face, mapping, geometry, autonomous driving, slam, outdoor, gaussian splatting, localization, ar, efficient  
- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031v1)**  
  Authors: Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23031v1.pdf)  
  Keywords: 3d gaussian, geometry, efficient, fast, gaussian splatting, dynamic, large scene, high-fidelity, ar, urban scene  
- **[Point-Cloud-Assistant Localized Statistical Channel Prediction by Tangent Gaussian Splatting](https://arxiv.org/abs/2606.18734v1)**  
  Authors: Ye Xue, Yiheng Wang, Xinhua Shao, Qi Yan, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.18734v1.pdf)  
  Keywords: 3d gaussian, geometry, fast, outdoor, gaussian splatting, ar, efficient  

### Model Compression

*Showing the latest 50 out of 185 papers*

- **[Rendering 3D Gaussians on a Graph Processor](https://arxiv.org/abs/2607.15951v1)**  
  Authors: Nicholas Fry, Ignacio Alzugaray, Mark Pupilli, Paul H. J. Kelly, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15951v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nmjfry.github.io/ipu-3dgs)  
  Keywords: 3d gaussian, ar, efficient  
- **[E3DGS: Unified Geometric-Photometric Equivariance for 3D Gaussian Splatting via Color-as-Geometry Embedding](https://arxiv.org/abs/2607.15536v1)**  
  Authors: Chankyo Kim, Maani Ghaffari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15536v1.pdf)  
  Keywords: 3d gaussian, geometry, body, gaussian splatting, ar, efficient  
- **[RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping](https://arxiv.org/abs/2607.15048v1)**  
  Authors: Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15048v1.pdf)  
  Keywords: face, 3d gaussian, semantic, mapping, autonomous driving, compact, ar, efficient  
- **[Compression of 3D Gaussian Splatting Data Using GPU-friendly Graphics Texture Coding](https://arxiv.org/abs/2607.14513v1)**  
  Authors: Amir Said, Randall Rauwendaal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14513v1.pdf)  
  Keywords: 3d gaussian, acceleration, gaussian splatting, compression, ar, efficient  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, motion, fast, slam, gaussian splatting, large scene, recognition, ar, efficient  
- **[G$^2$SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction](https://arxiv.org/abs/2607.14470v1)**  
  Authors: Dasong Gao, Vivienne Sze, Sertac Karaman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14470v1.pdf)  
  Keywords: 3d gaussian, face, ar, geometry, fast, gaussian splatting, high-fidelity, lightweight, efficient  
- **[Bake It Till You Make It: Ultrafast Spatial Texture-Atlas Splatting](https://arxiv.org/abs/2607.13808v1)**  
  Authors: Neel Kelkar, Simon Niedermayr, Kaloian Petkov, Klaus Engel, Rüdiger Westermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13808v1.pdf)  
  Keywords: 3d gaussian, mapping, geometry, fast, gaussian splatting, compact, ar, efficient  
- **[SpeedyGS: Content-Aware 3D Gaussian Splatting Compression via Two-Stage Optimization](https://arxiv.org/abs/2607.12656v1)**  
  Authors: Junteng Zhang, Tong Chen, Yuxin Zhao, Yibo Shi, Jing Wang, Zhan Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12656v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, head, fast, gaussian splatting, compression, compact, lightweight, efficient  
- **[GeoFovea-GS: Geometry-Aware Cross-Layer Gaussian Splatting for Wireless Aerial VR](https://arxiv.org/abs/2607.12641v1)**  
  Authors: Zeyi Ren, Wencheng Yan, Jiawen Zhang, Jintao Yan, Sheng Zhou, Zhisheng Niu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12641v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, vr, gaussian splatting, compact, lightweight, efficient  
- **[Implicit 4D Gaussian Splatting for Fast Motion with Large Inter-Frame Displacements](https://arxiv.org/abs/2607.12362v1)**  
  Authors: Seung-gyeom Kim, Areum Kim, Yongjae Yoo, Sukmin Yun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12362v1.pdf)  
  Keywords: ar, head, motion, fast, gaussian splatting, 4d, lightweight  

### Quality Enhancement

*Showing the latest 50 out of 119 papers*

- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: human, 3d gaussian, face, ray tracing, geometry, motion, reflection, gaussian splatting, dynamic, high-fidelity, ar  
- **[G$^2$SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction](https://arxiv.org/abs/2607.14470v1)**  
  Authors: Dasong Gao, Vivienne Sze, Sertac Karaman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14470v1.pdf)  
  Keywords: 3d gaussian, face, ar, geometry, fast, gaussian splatting, high-fidelity, lightweight, efficient  
- **[T3HG-Editor: Text-driven 3D Human Garment Editing with Body Priors Embedded in SMPL-X](https://arxiv.org/abs/2607.13654v1)**  
  Authors: Shaoru Sun, Xingtao Wang, Zihan Ma, Wenrui Li, Jiantao Zhou, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13654v1.pdf)  
  Keywords: human, 3d gaussian, face, semantic, geometry, body, high-fidelity, ar  
- **[COLMAR: Cooperative View Policy Learning for Multi-Agent Active 3D Reconstruction](https://arxiv.org/abs/2607.13524v1)**  
  Authors: Phu Pham, Damon Conover, Aniket Bera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13524v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, 3d reconstruction, high-fidelity, ar  
- **[ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space](https://arxiv.org/abs/2607.11673v2)**  
  Authors: Mingchao Sun, Luyang Tang, Yu Liu, Xu Yan, Zhan Li, Yunwei Zhang, Fei Yu, Zengye Ge, Yumin Liu, Jiacheng Zhang, Yongchang Zhang, Jiawei Zhang, Zhicheng Liu, Zhongxu Sun, Tianjian Ouyang, Wenzheng Chen, Shixing Yang, Nianfei Fan, Guodong Sun, Huan Li, Zheng Zhou, Yongze Li, Yingliang Peng, Mengmeng Du, Yuan Liu, Haozhe Shi, Chunnuo Gong, Chengzhen Yu, Chunxue Jia, Yang Liu, Shiying Zeng, Junnan Lai, Hang Zhang, Ning Guo, Baoquan Chen, Mu Xu, Hongyu Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11673v2.pdf)  
  Keywords: 3d gaussian, geometry, gaussian splatting, high-fidelity, compact, ar, efficient  
- **[MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction](https://arxiv.org/abs/2607.10792v1)**  
  Authors: Jinqian Yang, Yichen Wu, Wanhua Li, Haokun Lin, Renzhen Wang, Xiangchu Feng, Xixi Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.10792v1.pdf)  
  Keywords: 3d gaussian, sparse-view, semantic, geometry, neural rendering, gaussian splatting, high-fidelity, ar  
- **[Incremental Online Scene Reconstruction by 3D Gaussian Triangulation](https://arxiv.org/abs/2607.10690v1)**  
  Authors: Yanjin Zhu, Shaofan Liu, Jianke Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.10690v1.pdf)  
  Keywords: 3d gaussian, face, head, gaussian splatting, dynamic, high-fidelity, efficient  
- **[EscFOA: Enhancing Spatial Learning for Visually Impaired Learners via Generative Spatial Audio in 360-Degree Educational Environments](https://arxiv.org/abs/2607.07015v1)**  
  Authors: Ziyu Luo, Xiaowei Dai, Siying Zhu, Xiaoming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07015v1.pdf)  
  Keywords: 3d gaussian, geometry, gaussian splatting, high-fidelity, ar  
- **[RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation](https://arxiv.org/abs/2607.06699v1)**  
  Authors: Shujie Zhang, Jingkun Yi, Weipeng Zhong, Zirui Zhou, Yangkun Zhu, Hanqing Wang, Xudong Xu, Weinan Zhang, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06699v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, gaussian splatting, ar  
- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: 3d gaussian, mapping, slam, dynamic, localization, high-fidelity, tracking, survey, ar, efficient  

### Ray Tracing

- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: human, 3d gaussian, face, ray tracing, geometry, motion, reflection, gaussian splatting, dynamic, high-fidelity, ar  
- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: human, ray casting, geometry, gaussian splatting, compact, ar  
- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869v1)**  
  Authors: Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30869v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gray)  
  Keywords: 3d gaussian, ray tracing, fast, gaussian splatting, ar  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: 3d gaussian, path tracing, ray tracing, real-time rendering, geometry, fast, reflection, gaussian splatting, ar, efficient  
- **[RenderFormer++: Scalable and Physically Grounded Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v1)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jinyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v1.pdf)  
  Keywords: illumination, global illumination, neural rendering, light transport, compact, ar  
- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: illumination, 3d gaussian, geometry, global illumination, gaussian splatting, 3d reconstruction, ar, efficient  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: illumination, global illumination, gaussian splatting, high-fidelity, ar  
- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314v1)**  
  Authors: Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11314v1.pdf)  
  Keywords: 3d gaussian, ar, ray tracing, geometry, motion, neural rendering, relighting, 3d reconstruction, lighting, dynamic, light transport, lightweight  
- **[PTIR-GS: Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606v3)**  
  Authors: Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09606v3.pdf)  
  Keywords: illumination, 3d gaussian, path tracing, ray tracing, reflection, global illumination, relighting, lighting, light transport, compact, ar, shadow  
- **[RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation](https://arxiv.org/abs/2606.01261v1)**  
  Authors: Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.01261v1.pdf)  
  Keywords: 3d gaussian, semantic, ray tracing, geometry, reflection, gaussian splatting, segmentation, ar, efficient  

### Relighting

*Showing the latest 50 out of 54 papers*

- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: human, 3d gaussian, face, ray tracing, geometry, motion, reflection, gaussian splatting, dynamic, high-fidelity, ar  
- **[GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM](https://arxiv.org/abs/2607.07452v1)**  
  Authors: Lipu Zhou, Yaoyun Kang, Junxiang Pang, Shengkai Sun, Tingting Bao, Kehan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07452v1.pdf)  
  Keywords: illumination, mapping, geometry, slam, gaussian splatting, 3d reconstruction, ar, robotics  
- **[PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution](https://arxiv.org/abs/2607.06238v1)**  
  Authors: Lihua Wei, Huatong Gao, Jia Gong, Zhiyu Tan, Hao Li, Jun Liu, Zhihua Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06238v1.pdf)  
  Keywords: mapping, gaussian splatting, dynamic, lighting, ar  
- **[WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images](https://arxiv.org/abs/2607.05347v1)**  
  Authors: Xiyu Zhang, Jingyu Zhuang, Hongjia Zhai, Zizheng Yan, Jinwei Chen, Guofeng Zhang, Qingnan Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05347v1.pdf)  
  Keywords: illumination, 3d gaussian, face, geometry, gaussian splatting, 3d reconstruction, ar, efficient  
- **[InvSplat: Inverse Feed-Forward Scene Splatting](https://arxiv.org/abs/2607.02301v1)**  
  Authors: Polina Karpikova, Wenjing Bian, Haofei Xu, Hendrik Lensch, Andreas Geiger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.02301v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://poliik.github.io/invsplat)  
  Keywords: 3d gaussian, geometry, relighting, 3d reconstruction, lighting, ar  
- **[DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918v2)**  
  Authors: Junzhe Jiang, Zipei Ma, Zijie Pan, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31918v2.pdf)  
  Keywords: 3d gaussian, real-time rendering, autonomous driving, lighting, ar  
- **[Intrinsic decomposition and editing of 3D Gaussian splats](https://arxiv.org/abs/2606.31637v1)**  
  Authors: Alexandre Lanvin, Jeffrey Hu, Simon Lucas, Adrien Bousseau, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31637v1.pdf)  
  Keywords: face, 3d gaussian, gaussian splatting, lighting, ar  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: 3d gaussian, path tracing, ray tracing, real-time rendering, geometry, fast, reflection, gaussian splatting, ar, efficient  
- **[RenderFormer++: Scalable and Physically Grounded Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v1)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jinyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v1.pdf)  
  Keywords: illumination, global illumination, neural rendering, light transport, compact, ar  
- **[Monte Carlo Energy Aggregation for Mobile 3D Gaussian Splatting](https://arxiv.org/abs/2606.30017v1)**  
  Authors: Xiaobiao Du, YuAn Wang, Hao Li, Bosheng Wang, Xun Sun, Xin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30017v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiaobiaodu.github.io/flux-gs-project)  
  Keywords: 3d gaussian, head, gaussian splatting, lighting, compression, high-fidelity, compact, ar  

### SLAM

*Showing the latest 50 out of 75 papers*

- **[RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping](https://arxiv.org/abs/2607.15048v1)**  
  Authors: Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15048v1.pdf)  
  Keywords: face, 3d gaussian, semantic, mapping, autonomous driving, compact, ar, efficient  
- **[AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight](https://arxiv.org/abs/2607.14997v1)**  
  Authors: Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14997v1.pdf)  
  Keywords: 3d gaussian, semantic, motion, gaussian splatting, dynamic, tracking, ar  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, motion, fast, slam, gaussian splatting, large scene, recognition, ar, efficient  
- **[Bake It Till You Make It: Ultrafast Spatial Texture-Atlas Splatting](https://arxiv.org/abs/2607.13808v1)**  
  Authors: Neel Kelkar, Simon Niedermayr, Kaloian Petkov, Klaus Engel, Rüdiger Westermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13808v1.pdf)  
  Keywords: 3d gaussian, mapping, geometry, fast, gaussian splatting, compact, ar, efficient  
- **[VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation](https://arxiv.org/abs/2607.12356v2)**  
  Authors: Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao, Yan Wu, Wei-Yun Yau, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12356v2.pdf)  
  Keywords: human, 3d gaussian, semantic, mapping, geometry, compact, ar  
- **[GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors](https://arxiv.org/abs/2607.11184v1)**  
  Authors: Ruilan Gao, Letian Jin, Yu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11184v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rlgao.github.io/geogs_slam)  
  Keywords: 3d gaussian, mapping, geometry, slam, outdoor, gaussian splatting, tracking, ar  
- **[AnythingReality: Robust Online Gaussian Splatting SLAM for Open-Vocabulary VR Scene Exploration](https://arxiv.org/abs/2607.09260v1)**  
  Authors: Timofei Kozlov, Dmitrii Maliukov, Andrey Marchenko, Miguel Altamirano Cabrera, Dzmitry Tsetserukou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09260v1.pdf)  
  Keywords: 3d gaussian, semantic, vr, slam, gaussian splatting, recognition, ar  
- **[Track2Map: Online Deformable SLAM with Motion-Aware Pose Optimization in Robotic Surgery](https://arxiv.org/abs/2607.08408v1)**  
  Authors: Tianyi Song, Sierra Bonilla, Xinwei Ju, Evangelos Mazomenos, Danail Stoyanov, Adam Schmidt, Omid Mohareri, Sophia Bano, Francisco Vasconcelos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08408v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://track2map.github.io)  
  Keywords: 3d gaussian, mapping, deformation, motion, slam, gaussian splatting, 3d reconstruction, ar  
- **[GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM](https://arxiv.org/abs/2607.07452v1)**  
  Authors: Lipu Zhou, Yaoyun Kang, Junxiang Pang, Shengkai Sun, Tingting Bao, Kehan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07452v1.pdf)  
  Keywords: illumination, mapping, geometry, slam, gaussian splatting, 3d reconstruction, ar, robotics  
- **[PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution](https://arxiv.org/abs/2607.06238v1)**  
  Authors: Lihua Wei, Huatong Gao, Jia Gong, Zhiyu Tan, Hao Li, Jun Liu, Zhihua Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06238v1.pdf)  
  Keywords: mapping, gaussian splatting, dynamic, lighting, ar  

### Scene Understanding

*Showing the latest 50 out of 117 papers*

- **[RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping](https://arxiv.org/abs/2607.15048v1)**  
  Authors: Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15048v1.pdf)  
  Keywords: face, 3d gaussian, semantic, mapping, autonomous driving, compact, ar, efficient  
- **[AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight](https://arxiv.org/abs/2607.14997v1)**  
  Authors: Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14997v1.pdf)  
  Keywords: 3d gaussian, semantic, motion, gaussian splatting, dynamic, tracking, ar  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, motion, fast, slam, gaussian splatting, large scene, recognition, ar, efficient  
- **[T3HG-Editor: Text-driven 3D Human Garment Editing with Body Priors Embedded in SMPL-X](https://arxiv.org/abs/2607.13654v1)**  
  Authors: Shaoru Sun, Xingtao Wang, Zihan Ma, Wenrui Li, Jiantao Zhou, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13654v1.pdf)  
  Keywords: human, 3d gaussian, face, semantic, geometry, body, high-fidelity, ar  
- **[VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation](https://arxiv.org/abs/2607.12356v2)**  
  Authors: Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao, Yan Wu, Wei-Yun Yau, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12356v2.pdf)  
  Keywords: human, 3d gaussian, semantic, mapping, geometry, compact, ar  
- **[MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction](https://arxiv.org/abs/2607.10792v1)**  
  Authors: Jinqian Yang, Yichen Wu, Wanhua Li, Haokun Lin, Renzhen Wang, Xiangchu Feng, Xixi Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.10792v1.pdf)  
  Keywords: 3d gaussian, sparse-view, semantic, geometry, neural rendering, gaussian splatting, high-fidelity, ar  
- **[CoSAG: Compact Semantic Anchor Gaussians via Training-Free Rate-Distortion Coding](https://arxiv.org/abs/2607.10237v1)**  
  Authors: Yuang Jia, Jinlong Wang, Junhong Lin, Ruiting Dai, Wei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.10237v1.pdf)  
  Keywords: 3d gaussian, semantic, understanding, gaussian splatting, compact, ar  
- **[AnythingReality: Robust Online Gaussian Splatting SLAM for Open-Vocabulary VR Scene Exploration](https://arxiv.org/abs/2607.09260v1)**  
  Authors: Timofei Kozlov, Dmitrii Maliukov, Andrey Marchenko, Miguel Altamirano Cabrera, Dzmitry Tsetserukou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09260v1.pdf)  
  Keywords: 3d gaussian, semantic, vr, slam, gaussian splatting, recognition, ar  
- **[PUF: Plug-and-Play Uncertainty-Aware Fusion for Online 3D Scene Graph Generation](https://arxiv.org/abs/2607.07170v1)**  
  Authors: Yi Yang, Myrna Castillo, Bodo Rosenhahn, Michael Ying Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07170v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yyyyangyi/PUF?style=social)](https://github.com/yyyyangyi/PUF)  
  Keywords: 3d gaussian, semantic, ar, understanding  
- **[GaussFusion: Towards Multimodal 3D Gaussian Pretraining](https://arxiv.org/abs/2607.05906v1)**  
  Authors: Zhixuan You, Jihua Zhu, Yiding Sun, Zihao Guo, Haozhe Cheng, Dongxu Zhang, Lin Chen, Hainan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05906v1.pdf)  
  Keywords: 3d gaussian, semantic, geometry, gaussian splatting, ar  



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