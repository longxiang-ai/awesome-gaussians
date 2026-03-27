# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-03-27 01:19:31

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
- [Acceleration](#acceleration) (118 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (500 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (159 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (204 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (31 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (204 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (16 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (220 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (130 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (21 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (71 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (72 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (131 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: 3d gaussian, vr, gaussian splatting, survey, ar  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v3)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v3.pdf)  
  Keywords: 3d gaussian, ray tracing, gaussian splatting, survey, mapping, ar  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: face, 3d gaussian, dynamic, efficient, localization, slam, tracking, gaussian splatting, survey, mapping, ar, motion  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, survey, ar, robotics  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v3)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v3.pdf)  
  Keywords: 3d gaussian, efficient, nerf, geometry, gaussian splatting, survey, ar  
- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197v1)**  
  Authors: Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07197v1.pdf)  
  Keywords: high-fidelity, compression, 3d gaussian, dynamic, efficient, 3d reconstruction, compact, survey, gaussian splatting, ar, 4d  

### Acceleration

*Showing the latest 50 out of 118 papers*

- **[ViewSplat: View-Adaptive Dynamic Gaussian Splatting for Feed-Forward Synthesis](https://arxiv.org/abs/2603.25265v1)**  
  Authors: Moonyeon Jeong, Seunggi Min, Suhyeon Lee, Hongje Seong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25265v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, dynamic, gaussian splatting, fast, ar, real-time rendering  
- **[MoRGS: Efficient Per-Gaussian Motion Reasoning for Streamable Dynamic 3D Scenes](https://arxiv.org/abs/2603.25042v1)**  
  Authors: Wonjoon Lee, Sungmin Woo, Donghyeong Kim, Jungho Lee, Sangheon Park, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25042v1.pdf)  
  Keywords: 3d gaussian, dynamic, efficient, gaussian splatting, fast, lightweight, ar, real-time rendering, motion, 4d  
- **[Confidence-Based Mesh Extraction from 3D Gaussians](https://arxiv.org/abs/2603.24725v1)**  
  Authors: Lukas Radl, Felix Windisch, Andreas Kurz, Thomas Köhler, Michael Steiner, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24725v1.pdf)  
  Keywords: face, efficient, 3d gaussian, dynamic, gaussian splatting, fast, ar  
- **[Accurate Point Measurement in 3DGS -- A New Alternative to Traditional Stereoscopic-View Based Measurements](https://arxiv.org/abs/2603.24716v1)**  
  Authors: Deyan Deng, Rongjun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24716v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/3dgs_measurement_tool?style=social)](https://github.com/GDAOSU/3dgs_measurement_tool)  
  Keywords: 3d gaussian, gaussian splatting, ar, real-time rendering  
- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, 3d reconstruction, gaussian splatting, fast, ar  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, geometry, head, fast, avatar, ar, animation  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: face, 3d gaussian, geometry, path tracing, ar, real-time rendering  
- **[Fast undersampled dynamic MRI reconstruction using explicit representation learning with Gaussian splatting](https://arxiv.org/abs/2603.21980v1)**  
  Authors: M. L. Terpstra, C. A. T. van den Berg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21980v1.pdf)  
  Keywords: efficient, dynamic, gaussian splatting, fast, ar, motion  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, nerf, geometry, gaussian splatting, ray tracing, fast, ar, real-time rendering  
- **[F4Splat: Feed-Forward Predictive Densification for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.21304v2)**  
  Authors: Injae Kim, Chaehyeon Kim, Minseong Bae, Minseok Joo, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21304v2.pdf)  
  Keywords: 3d gaussian, compact, gaussian splatting, ar, real-time rendering  

### Applications

*Showing the latest 50 out of 500 papers*

- **[ViewSplat: View-Adaptive Dynamic Gaussian Splatting for Feed-Forward Synthesis](https://arxiv.org/abs/2603.25265v1)**  
  Authors: Moonyeon Jeong, Seunggi Min, Suhyeon Lee, Hongje Seong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25265v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, dynamic, gaussian splatting, fast, ar, real-time rendering  
- **[AirSplat: Alignment and Rating for Robust Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.25129v1)**  
  Authors: Minh-Quan Viet Bui, Jaeho Moon, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25129v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, geometry, gaussian splatting, ar, sparse-view  
- **[Learning Explicit Continuous Motion Representation for Dynamic Gaussian Splatting from Monocular Videos](https://arxiv.org/abs/2603.25058v1)**  
  Authors: Xuankai Zhang, Junjin Xiao, Shangwei Huang, Wei-shi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25058v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hhhddddddd/se3bsplinegs?style=social)](https://github.com/hhhddddddd/se3bsplinegs)  
  Keywords: dynamic, compact, gaussian splatting, ar, motion, deformation  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v1)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v1.pdf)  
  Keywords: efficient, 3d gaussian, 3d reconstruction, geometry, gaussian splatting, ar  
- **[MoRGS: Efficient Per-Gaussian Motion Reasoning for Streamable Dynamic 3D Scenes](https://arxiv.org/abs/2603.25042v1)**  
  Authors: Wonjoon Lee, Sungmin Woo, Donghyeong Kim, Jungho Lee, Sangheon Park, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25042v1.pdf)  
  Keywords: 3d gaussian, dynamic, efficient, gaussian splatting, fast, lightweight, ar, real-time rendering, motion, 4d  
- **[$π$, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation](https://arxiv.org/abs/2603.25038v1)**  
  Authors: Johnathan Tucker, Denis Liu, Aiden Swann, Allen Ren, Javier Yu, Jiankai Sun, Brandon Kim, Lachlain McGranahan, Quan Vuong, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25038v1.pdf)  
  Keywords: gaussian splatting, ar, dynamic  
- **[Relaxed Rigidity with Ray-based Grouping for Dynamic Gaussian Splatting](https://arxiv.org/abs/2603.24994v1)**  
  Authors: Junoh Leea, Junmyeong Lee, Yeon-Ji Song, Inhwan Bae, Jisu Shin, Hae-Gon Jeon, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24994v1.pdf)  
  Keywords: 3d gaussian, dynamic, geometry, gaussian splatting, ar, motion, 4d  
- **[Confidence-Based Mesh Extraction from 3D Gaussians](https://arxiv.org/abs/2603.24725v1)**  
  Authors: Lukas Radl, Felix Windisch, Andreas Kurz, Thomas Köhler, Michael Steiner, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24725v1.pdf)  
  Keywords: face, efficient, 3d gaussian, dynamic, gaussian splatting, fast, ar  
- **[Accurate Point Measurement in 3DGS -- A New Alternative to Traditional Stereoscopic-View Based Measurements](https://arxiv.org/abs/2603.24716v1)**  
  Authors: Deyan Deng, Rongjun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24716v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/3dgs_measurement_tool?style=social)](https://github.com/GDAOSU/3dgs_measurement_tool)  
  Keywords: 3d gaussian, gaussian splatting, ar, real-time rendering  
- **[SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision](https://arxiv.org/abs/2603.24036v1)**  
  Authors: Avigail Cohen Rimon, Amir Mann, Mirela Ben Chen, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24036v1.pdf)  
  Keywords: 3d gaussian, compact, tracking, gaussian splatting, ar, deformation  

### Avatar Generation

*Showing the latest 50 out of 159 papers*

- **[Confidence-Based Mesh Extraction from 3D Gaussians](https://arxiv.org/abs/2603.24725v1)**  
  Authors: Lukas Radl, Felix Windisch, Andreas Kurz, Thomas Köhler, Michael Steiner, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24725v1.pdf)  
  Keywords: face, efficient, 3d gaussian, dynamic, gaussian splatting, fast, ar  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: face, efficient, 3d gaussian, large scene, head, gaussian splatting, neural rendering, ar  
- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, 3d reconstruction, gaussian splatting, fast, ar  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, geometry, head, fast, avatar, ar, animation  
- **[GSwap: Realistic Head Swapping with Dynamic Neural Gaussian Field](https://arxiv.org/abs/2603.23168v1)**  
  Authors: Jingtao Zhou, Xuan Gao, Dongyu Liu, Junhui Hou, Yudong Guo, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23168v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, dynamic, efficient, head, body, ar, motion  
- **[UniQueR: Unified Query-based Feedforward 3D Reconstruction](https://arxiv.org/abs/2603.22851v1)**  
  Authors: Chensheng Peng, Quentin Herau, Jiezhi Yang, Yichen Xie, Yihan Hu, Wenzhao Zheng, Matthew Strong, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22851v1.pdf)  
  Keywords: face, 3d gaussian, efficient, 3d reconstruction, vr, nerf, compact, geometry, ar  
- **[FullCircle: Effortless 3D Reconstruction from Casual 360$^\circ$ Captures](https://arxiv.org/abs/2603.22572v1)**  
  Authors: Yalda Foroutan, Ipek Oztas, Daniel Rebain, Aysegul Dundar, Kwang Moo Yi, Lily Goli, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22572v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://theialab.github.io/fullcircle)  
  Keywords: human, ar, 3d reconstruction  
- **[Drop-In Perceptual Optimization for 3D Gaussian Splatting](https://arxiv.org/abs/2603.23297v1)**  
  Authors: Ezgi Ozyilkan, Zhiqi Chen, Oren Rippel, Jona Ballé, Kedar Tatwawadi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23297v1.pdf)  
  Keywords: compression, 3d gaussian, gaussian splatting, ar, human  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: face, 3d gaussian, geometry, path tracing, ar, real-time rendering  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, nerf, geometry, gaussian splatting, ray tracing, fast, ar, real-time rendering  

### Dynamic Scene

*Showing the latest 50 out of 204 papers*

- **[ViewSplat: View-Adaptive Dynamic Gaussian Splatting for Feed-Forward Synthesis](https://arxiv.org/abs/2603.25265v1)**  
  Authors: Moonyeon Jeong, Seunggi Min, Suhyeon Lee, Hongje Seong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25265v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, dynamic, gaussian splatting, fast, ar, real-time rendering  
- **[Learning Explicit Continuous Motion Representation for Dynamic Gaussian Splatting from Monocular Videos](https://arxiv.org/abs/2603.25058v1)**  
  Authors: Xuankai Zhang, Junjin Xiao, Shangwei Huang, Wei-shi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25058v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hhhddddddd/se3bsplinegs?style=social)](https://github.com/hhhddddddd/se3bsplinegs)  
  Keywords: dynamic, compact, gaussian splatting, ar, motion, deformation  
- **[MoRGS: Efficient Per-Gaussian Motion Reasoning for Streamable Dynamic 3D Scenes](https://arxiv.org/abs/2603.25042v1)**  
  Authors: Wonjoon Lee, Sungmin Woo, Donghyeong Kim, Jungho Lee, Sangheon Park, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25042v1.pdf)  
  Keywords: 3d gaussian, dynamic, efficient, gaussian splatting, fast, lightweight, ar, real-time rendering, motion, 4d  
- **[$π$, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation](https://arxiv.org/abs/2603.25038v1)**  
  Authors: Johnathan Tucker, Denis Liu, Aiden Swann, Allen Ren, Javier Yu, Jiankai Sun, Brandon Kim, Lachlain McGranahan, Quan Vuong, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25038v1.pdf)  
  Keywords: gaussian splatting, ar, dynamic  
- **[Relaxed Rigidity with Ray-based Grouping for Dynamic Gaussian Splatting](https://arxiv.org/abs/2603.24994v1)**  
  Authors: Junoh Leea, Junmyeong Lee, Yeon-Ji Song, Inhwan Bae, Jisu Shin, Hae-Gon Jeon, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24994v1.pdf)  
  Keywords: 3d gaussian, dynamic, geometry, gaussian splatting, ar, motion, 4d  
- **[Confidence-Based Mesh Extraction from 3D Gaussians](https://arxiv.org/abs/2603.24725v1)**  
  Authors: Lukas Radl, Felix Windisch, Andreas Kurz, Thomas Köhler, Michael Steiner, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24725v1.pdf)  
  Keywords: face, efficient, 3d gaussian, dynamic, gaussian splatting, fast, ar  
- **[SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision](https://arxiv.org/abs/2603.24036v1)**  
  Authors: Avigail Cohen Rimon, Amir Mann, Mirela Ben Chen, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24036v1.pdf)  
  Keywords: 3d gaussian, compact, tracking, gaussian splatting, ar, deformation  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, geometry, head, fast, avatar, ar, animation  
- **[GTLR-GS: Geometry-Texture Aware LiDAR-Regularized 3D Gaussian Splatting for Realistic Scene Reconstruction](https://arxiv.org/abs/2603.23192v1)**  
  Authors: Yan Fang, Jianfei Ge, Jiangjian Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23192v1.pdf)  
  Keywords: 3d gaussian, dynamic, geometry, gaussian splatting, ar, motion  
- **[GSwap: Realistic Head Swapping with Dynamic Neural Gaussian Field](https://arxiv.org/abs/2603.23168v1)**  
  Authors: Jingtao Zhou, Xuan Gao, Dongyu Liu, Junhui Hou, Yudong Guo, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23168v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, dynamic, efficient, head, body, ar, motion  

### Few-shot

- **[AirSplat: Alignment and Rating for Robust Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.25129v1)**  
  Authors: Minh-Quan Viet Bui, Jaeho Moon, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25129v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, geometry, gaussian splatting, ar, sparse-view  
- **[EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](https://arxiv.org/abs/2603.21332v1)**  
  Authors: Haolan Xu, Keli Cheng, Lei Wang, Ning Bi, Xiaoming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21332v1.pdf)  
  Keywords: face, 3d gaussian, lighting, nerf, head, gaussian splatting, ar, few-shot, motion  
- **[UniSem: Generalizable Semantic 3D Reconstruction from Sparse Unposed Images](https://arxiv.org/abs/2603.17519v1)**  
  Authors: Guibiao Liao, Qian Ren, Kaimin Liao, Hua Wang, Zhi Chen, Luchao Wang, Yaohua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17519v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, geometry, gaussian splatting, semantic, ar, sparse-view, segmentation  
- **[S2D: Sparse to Dense Lifting for 3D Reconstruction with Minimal Inputs](https://arxiv.org/abs/2603.10893v1)**  
  Authors: Yuzhou Ji, Qijian Tian, He Zhu, Xiaoqi Jiang, Guangzhi Cao, Lizhuang Ma, Yuan Xie, Xin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10893v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, efficient, understanding, sparse view, 3d reconstruction, gaussian splatting, ar  
- **[Active View Selection with Perturbed Gaussian Ensemble for Tomographic Reconstruction](https://arxiv.org/abs/2603.06852v1)**  
  Authors: Yulun Wu, Ruyi Zha, Wei Cao, Yingying Li, Yuanhao Cai, Yaoyao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06852v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, fast, ar, sparse-view  
- **[CylinderSplat: 3D Gaussian Splatting with Cylindrical Triplanes for Panoramic Novel View Synthesis](https://arxiv.org/abs/2603.05882v1)**  
  Authors: Qiwei Wang, Xianghui Ze, Jingyi Yu, Yujiao Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05882v1.pdf)  
  Keywords: 3d gaussian, geometry, gaussian splatting, ar, sparse-view  
- **[DSA-SRGS: Super-Resolution Gaussian Splatting for Dynamic Sparse-View DSA Reconstruction](https://arxiv.org/abs/2603.04770v1)**  
  Authors: Shiyu Zhang, Zhicong Wu, Huangxuan Zhao, Zhentao Liu, Lei Chen, Yong Luo, Lefei Zhang, Zhiming Cui, Ziwen Ke, Bo Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04770v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, sparse-view, 4d  
- **[Intrinsic Geometry-Appearance Consistency Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2603.02893v1)**  
  Authors: Kaiqiang Xiong, Rui Peng, Jiahao Wu, Zhanke Wang, Jie Liang, Xiaoyun Zheng, Feng Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02893v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, human, geometry, gaussian splatting, ar, sparse-view  
- **[Multimodal-Prior-Guided Importance Sampling for Hierarchical Gaussian Splatting in Sparse-View Novel View Synthesis](https://arxiv.org/abs/2603.02866v1)**  
  Authors: Kaiqiang Xiong, Zhanke Wang, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02866v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, semantic, ar, sparse-view  
- **[SemGS: Feed-Forward Semantic 3D Gaussian Splatting from Sparse Views for Generalizable Scene Understanding](https://arxiv.org/abs/2603.02548v1)**  
  Authors: Sheng Ye, Zhen-Hui Dong, Ruoyu Fan, Tian Lv, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02548v1.pdf)  
  Keywords: 3d gaussian, understanding, sparse view, gaussian splatting, semantic, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 204 papers*

- **[AirSplat: Alignment and Rating for Robust Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.25129v1)**  
  Authors: Minh-Quan Viet Bui, Jaeho Moon, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25129v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, geometry, gaussian splatting, ar, sparse-view  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v1)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v1.pdf)  
  Keywords: efficient, 3d gaussian, 3d reconstruction, geometry, gaussian splatting, ar  
- **[Relaxed Rigidity with Ray-based Grouping for Dynamic Gaussian Splatting](https://arxiv.org/abs/2603.24994v1)**  
  Authors: Junoh Leea, Junmyeong Lee, Yeon-Ji Song, Inhwan Bae, Jisu Shin, Hae-Gon Jeon, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24994v1.pdf)  
  Keywords: 3d gaussian, dynamic, geometry, gaussian splatting, ar, motion, 4d  
- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, 3d reconstruction, gaussian splatting, fast, ar  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, geometry, head, fast, avatar, ar, animation  
- **[GTLR-GS: Geometry-Texture Aware LiDAR-Regularized 3D Gaussian Splatting for Realistic Scene Reconstruction](https://arxiv.org/abs/2603.23192v1)**  
  Authors: Yan Fang, Jianfei Ge, Jiangjian Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23192v1.pdf)  
  Keywords: 3d gaussian, dynamic, geometry, gaussian splatting, ar, motion  
- **[Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction](https://arxiv.org/abs/2603.22852v1)**  
  Authors: Chengxin Lv, Yihui Li, Hongyu Yang, YunHong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22852v1.pdf)  
  Keywords: 3d gaussian, efficient, compact, geometry, semantic, autonomous driving, ar  
- **[UniQueR: Unified Query-based Feedforward 3D Reconstruction](https://arxiv.org/abs/2603.22851v1)**  
  Authors: Chensheng Peng, Quentin Herau, Jiezhi Yang, Yichen Xie, Yihan Hu, Wenzhao Zheng, Matthew Strong, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22851v1.pdf)  
  Keywords: face, 3d gaussian, efficient, 3d reconstruction, vr, nerf, compact, geometry, ar  
- **[Instrument-Splatting++: Towards Controllable Surgical Instrument Digital Twin Using Gaussian Splatting](https://arxiv.org/abs/2603.22792v2)**  
  Authors: Shuojue Yang, Zijian Wu, Chengjiaao Liao, Qian Li, Daiyun Shen, Chang Han Low, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22792v2.pdf)  
  Keywords: 3d gaussian, geometry, tracking, gaussian splatting, semantic, ar  
- **[FullCircle: Effortless 3D Reconstruction from Casual 360$^\circ$ Captures](https://arxiv.org/abs/2603.22572v1)**  
  Authors: Yalda Foroutan, Ipek Oztas, Daniel Rebain, Aysegul Dundar, Kwang Moo Yi, Lily Goli, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22572v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://theialab.github.io/fullcircle)  
  Keywords: human, ar, 3d reconstruction  

### Large Scene

- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: face, efficient, 3d gaussian, large scene, head, gaussian splatting, neural rendering, ar  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: efficient, dynamic, slam, head, gaussian splatting, tracking, outdoor, ar  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: 3d gaussian, localization, geometry, gaussian splatting, outdoor, ar  
- **[EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.06216v1)**  
  Authors: Miriam Jäger, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06216v1.pdf)  
  Keywords: face, 3d gaussian, urban scene, 3d reconstruction, geometry, gaussian splatting, ar  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, lighting, nerf, illumination, reflection, gaussian splatting, relighting, outdoor, fast, relightable, ar  
- **[Interactive Augmented Reality-enabled Outdoor Scene Visualization For Enhanced Real-time Disaster Response](https://arxiv.org/abs/2602.21874v1)**  
  Authors: Dimitrios Apostolakis, Georgios Angelidis, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21874v1.pdf)  
  Keywords: face, 3d gaussian, lighting, gaussian splatting, outdoor, semantic, fast, ar, lightweight  
- **[Large-scale Photorealistic Outdoor 3D Scene Reconstruction from UAV Imagery Using Gaussian Splatting Techniques](https://arxiv.org/abs/2602.20342v1)**  
  Authors: Christos Maikos, Georgios Angelidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20342v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, efficient, 3d reconstruction, vr, nerf, gaussian splatting, neural rendering, outdoor, ar  
- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: 3d gaussian, lighting, localization, geometry, gaussian splatting, head, outdoor, semantic, mapping, ar  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: 3d gaussian, lighting, nerf, illumination, gaussian splatting, outdoor, global illumination, autonomous driving, real-time rendering, ar  
- **[Zero-Shot UAV Navigation in Forests via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2602.07101v2)**  
  Authors: Zinan Lv, Yeqian Qian, Chen Sang, Hao Liu, Danping Zou, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07101v2.pdf)  
  Keywords: high-fidelity, 3d gaussian, dynamic, lighting, illumination, geometry, gaussian splatting, outdoor, relightable, ar, lightweight  

### Model Compression

*Showing the latest 50 out of 220 papers*

- **[Learning Explicit Continuous Motion Representation for Dynamic Gaussian Splatting from Monocular Videos](https://arxiv.org/abs/2603.25058v1)**  
  Authors: Xuankai Zhang, Junjin Xiao, Shangwei Huang, Wei-shi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25058v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hhhddddddd/se3bsplinegs?style=social)](https://github.com/hhhddddddd/se3bsplinegs)  
  Keywords: dynamic, compact, gaussian splatting, ar, motion, deformation  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v1)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v1.pdf)  
  Keywords: efficient, 3d gaussian, 3d reconstruction, geometry, gaussian splatting, ar  
- **[MoRGS: Efficient Per-Gaussian Motion Reasoning for Streamable Dynamic 3D Scenes](https://arxiv.org/abs/2603.25042v1)**  
  Authors: Wonjoon Lee, Sungmin Woo, Donghyeong Kim, Jungho Lee, Sangheon Park, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25042v1.pdf)  
  Keywords: 3d gaussian, dynamic, efficient, gaussian splatting, fast, lightweight, ar, real-time rendering, motion, 4d  
- **[Confidence-Based Mesh Extraction from 3D Gaussians](https://arxiv.org/abs/2603.24725v1)**  
  Authors: Lukas Radl, Felix Windisch, Andreas Kurz, Thomas Köhler, Michael Steiner, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24725v1.pdf)  
  Keywords: face, efficient, 3d gaussian, dynamic, gaussian splatting, fast, ar  
- **[SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision](https://arxiv.org/abs/2603.24036v1)**  
  Authors: Avigail Cohen Rimon, Amir Mann, Mirela Ben Chen, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24036v1.pdf)  
  Keywords: 3d gaussian, compact, tracking, gaussian splatting, ar, deformation  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: face, efficient, 3d gaussian, large scene, head, gaussian splatting, neural rendering, ar  
- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, 3d reconstruction, gaussian splatting, fast, ar  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, geometry, head, fast, avatar, ar, animation  
- **[Pose-Free Omnidirectional Gaussian Splatting for 360-Degree Videos with Consistent Depth Priors](https://arxiv.org/abs/2603.23324v2)**  
  Authors: Chuanqing Zhuang, Xin Lu, Zehui Deng, Zhengda Lu, Yiqun Wang, Junqi Diao, Jun Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23324v2.pdf) | [![GitHub](https://img.shields.io/github/stars/zcq15/PFGS360?style=social)](https://github.com/zcq15/PFGS360)  
  Keywords: 3d gaussian, gaussian splatting, ar, efficient  
- **[GSwap: Realistic Head Swapping with Dynamic Neural Gaussian Field](https://arxiv.org/abs/2603.23168v1)**  
  Authors: Jingtao Zhou, Xuan Gao, Dongyu Liu, Junhui Hou, Yudong Guo, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23168v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, dynamic, efficient, head, body, ar, motion  

### Quality Enhancement

*Showing the latest 50 out of 130 papers*

- **[ViewSplat: View-Adaptive Dynamic Gaussian Splatting for Feed-Forward Synthesis](https://arxiv.org/abs/2603.25265v1)**  
  Authors: Moonyeon Jeong, Seunggi Min, Suhyeon Lee, Hongje Seong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25265v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, dynamic, gaussian splatting, fast, ar, real-time rendering  
- **[AirSplat: Alignment and Rating for Robust Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.25129v1)**  
  Authors: Minh-Quan Viet Bui, Jaeho Moon, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25129v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, geometry, gaussian splatting, ar, sparse-view  
- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, 3d reconstruction, gaussian splatting, fast, ar  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, geometry, head, fast, avatar, ar, animation  
- **[GSwap: Realistic Head Swapping with Dynamic Neural Gaussian Field](https://arxiv.org/abs/2603.23168v1)**  
  Authors: Jingtao Zhou, Xuan Gao, Dongyu Liu, Junhui Hou, Yudong Guo, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23168v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, dynamic, efficient, head, body, ar, motion  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, nerf, geometry, gaussian splatting, ray tracing, fast, ar, real-time rendering  
- **[Training-Free Instance-Aware 3D Scene Reconstruction and Diffusion-Based View Synthesis from Sparse Images](https://arxiv.org/abs/2603.21166v1)**  
  Authors: Jiatong Xia, Lingqiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21166v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiatongxia.github.io/TID3R)  
  Keywords: high-fidelity, efficient, understanding, geometry, ar, segmentation  
- **[2Xplat: Two Experts Are Better Than One Generalist](https://arxiv.org/abs/2603.21064v2)**  
  Authors: Hwasik Jeong, Seungryong Lee, Gyeongjin Kang, Seungkwon Yang, Xiangyu Sun, Seungtae Nam, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21064v2.pdf)  
  Keywords: high-fidelity, 3d gaussian, geometry, gaussian splatting, ar  
- **[Fourier Splatting: Generalized Fourier encoded primitives for scalable radiance fields](https://arxiv.org/abs/2603.19834v1)**  
  Authors: Mihnea-Bogdan Jurca, Bert Van hauwermeiren, Adrian Munteanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19834v1.pdf)  
  Keywords: high-fidelity, efficient, 3d gaussian, gaussian splatting, ar, real-time rendering  
- **[StreetForward: Perceiving Dynamic Street with Feedforward Causal Attention](https://arxiv.org/abs/2603.19552v1)**  
  Authors: Zhongrui Yu, Zhao Wang, Yijia Xie, Yida Wang, Xueyang Zhang, Yifei Zhan, Kun Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19552v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://streetforward.github.io)  
  Keywords: high-fidelity, 3d gaussian, dynamic, efficient, geometry, gaussian splatting, autonomous driving, ar, motion  

### Ray Tracing

- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: 3d gaussian, reflection, ray tracing, gaussian splatting, mapping, relightable, ar, shadow  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: face, 3d gaussian, geometry, path tracing, ar, real-time rendering  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: high-fidelity, face, 3d gaussian, efficient, nerf, geometry, gaussian splatting, ray tracing, fast, ar, real-time rendering  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v3)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v3.pdf)  
  Keywords: 3d gaussian, ray tracing, gaussian splatting, survey, mapping, ar  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: high-fidelity, 3d gaussian, efficient, ray marching, gaussian splatting, ar, real-time rendering  
- **[Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction](https://arxiv.org/abs/2603.08503v1)**  
  Authors: Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08503v1.pdf) | [![GitHub](https://img.shields.io/github/stars/1170632760/Spherical-GOF?style=social)](https://github.com/1170632760/Spherical-GOF)  
  Keywords: 3d gaussian, efficient, geometry, gaussian splatting, ray casting, fast, ar, robotics  
- **[Ref-DGS: Reflective Dual Gaussian Splatting](https://arxiv.org/abs/2603.07664v2)**  
  Authors: Ningjing Fan, Yiqun Wang, Dongming Yan, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07664v2.pdf)  
  Keywords: face, efficient, geometry, reflection, ray tracing, gaussian splatting, fast, ar, lightweight  
- **[Radiometrically Consistent Gaussian Surfels for Inverse Rendering](https://arxiv.org/abs/2603.01491v1)**  
  Authors: Kyu Beom Han, Jaeyoon Kim, Woo Jae Kim, Jinhwan Seo, Sung-eui Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01491v1.pdf)  
  Keywords: efficient, lighting, illumination, reflection, ray tracing, gaussian splatting, relighting, global illumination, ar  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: 3d gaussian, lighting, nerf, illumination, gaussian splatting, outdoor, global illumination, autonomous driving, real-time rendering, ar  
- **[Rotated Lights for Consistent and Efficient 2D Gaussians Inverse Rendering](https://arxiv.org/abs/2602.08724v1)**  
  Authors: Geng Lin, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08724v1.pdf)  
  Keywords: efficient, lighting, illumination, geometry, gaussian splatting, relighting, global illumination, ar, shadow  

### Relighting

*Showing the latest 50 out of 71 papers*

- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: 3d gaussian, reflection, ray tracing, gaussian splatting, mapping, relightable, ar, shadow  
- **[PhotoAgent: A Robotic Photographer with Spatial and Aesthetic Understanding](https://arxiv.org/abs/2603.22796v1)**  
  Authors: Lirong Che, Zhenfeng Gan, Yanbo Chen, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22796v1.pdf)  
  Keywords: 3d gaussian, understanding, reflection, gaussian splatting, semantic, ar  
- **[EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](https://arxiv.org/abs/2603.21332v1)**  
  Authors: Haolan Xu, Keli Cheng, Lei Wang, Ning Bi, Xiaoming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21332v1.pdf)  
  Keywords: face, 3d gaussian, lighting, nerf, head, gaussian splatting, ar, few-shot, motion  
- **[TRGS-SLAM: IMU-Aided Gaussian Splatting SLAM for Blurry, Rolling Shutter, and Noisy Thermal Images](https://arxiv.org/abs/2603.20443v1)**  
  Authors: Spencer Carmichael, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20443v1.pdf)  
  Keywords: 3d gaussian, dynamic, localization, illumination, slam, gaussian splatting, tracking, mapping, fast, ar, motion, robotics  
- **[HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks](https://arxiv.org/abs/2603.19822v1)**  
  Authors: Jingyu Guo, Ziye Chen, Ziwen Li, Zhengqing Gao, Jiaxin Huang, Hanlue Zhang, Fengming Huang, Yu Yao, Tongliang Liu, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19822v1.pdf)  
  Keywords: 3d gaussian, lighting, geometry, gaussian splatting, semantic, ar  
- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: face, 3d gaussian, understanding, lighting, slam, gaussian splatting, semantic, mapping, ar, segmentation  
- **[E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction](https://arxiv.org/abs/2603.14684v1)**  
  Authors: Yunsoo Kim, Changki Sung, Dasol Hong, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14684v1.pdf)  
  Keywords: 3d gaussian, dynamic, 3d reconstruction, lighting, nerf, tracking, gaussian splatting, fast, ar, motion  
- **[PhyGaP: Physically-Grounded Gaussians with Polarization Cues](https://arxiv.org/abs/2603.14001v1)**  
  Authors: Jiale Wu, Xiaoyang Bai, Zongqi He, Weiwei Xu, Yifan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14001v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, lighting, reflection, gaussian splatting, relighting, ar  
- **[LR-SGS: Robust LiDAR-Reflectance-Guided Salient Gaussian Splatting for Self-Driving Scene Reconstruction](https://arxiv.org/abs/2603.12647v1)**  
  Authors: Ziyu Chen, Fan Zhu, Hui Zhu, Deyi Kong, Xinkai Kuang, Yujia Zhang, Chunmao Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12647v1.pdf)  
  Keywords: 3d gaussian, efficient, lighting, gaussian splatting, ar, motion  
- **[InstantHDR: Single-forward Gaussian Splatting for High Dynamic Range 3D Reconstruction](https://arxiv.org/abs/2603.11298v2)**  
  Authors: Dingqiang Ye, Jiacong Xu, Jianglu Ping, Yuxiang Guo, Chao Fan, Vishal M. Patel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11298v2.pdf)  
  Keywords: dynamic, 3d reconstruction, lighting, geometry, gaussian splatting, mapping, ar  

### SLAM

*Showing the latest 50 out of 72 papers*

- **[SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision](https://arxiv.org/abs/2603.24036v1)**  
  Authors: Avigail Cohen Rimon, Amir Mann, Mirela Ben Chen, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24036v1.pdf)  
  Keywords: 3d gaussian, compact, tracking, gaussian splatting, ar, deformation  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: 3d gaussian, reflection, ray tracing, gaussian splatting, mapping, relightable, ar, shadow  
- **[Instrument-Splatting++: Towards Controllable Surgical Instrument Digital Twin Using Gaussian Splatting](https://arxiv.org/abs/2603.22792v2)**  
  Authors: Shuojue Yang, Zijian Wu, Chengjiaao Liao, Qian Li, Daiyun Shen, Chang Han Low, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22792v2.pdf)  
  Keywords: 3d gaussian, geometry, tracking, gaussian splatting, semantic, ar  
- **[FreeArtGS: Articulated Gaussian Splatting Under Free-moving Scenario](https://arxiv.org/abs/2603.22102v1)**  
  Authors: Hang Dai, Hongwei Fan, Han Zhang, Duojin Wu, Jiyao Zhang, Hao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22102v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://freeartgs.github.io)  
  Keywords: tracking, geometry, gaussian splatting, ar, motion, segmentation, robotics  
- **[SGAD-SLAM: Splatting Gaussians at Adjusted Depth for Better Radiance Fields in RGBD SLAM](https://arxiv.org/abs/2603.21055v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21055v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/SGAD-SLAM-Project)  
  Keywords: 3d gaussian, slam, tracking, gaussian splatting, mapping, ar  
- **[Glove2Hand: Synthesizing Natural Hand-Object Interaction from Multi-Modal Sensing Gloves](https://arxiv.org/abs/2603.20850v1)**  
  Authors: Xinyu Zhang, Ziyi Kou, Chuan Qin, Mia Huang, Ergys Ristani, Ankit Kumar, Lele Chen, Kun He, Abdeslam Boularias, Li Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20850v1.pdf)  
  Keywords: 3d gaussian, dynamic, understanding, vr, tracking, ar, motion, deformation, robotics  
- **[TRGS-SLAM: IMU-Aided Gaussian Splatting SLAM for Blurry, Rolling Shutter, and Noisy Thermal Images](https://arxiv.org/abs/2603.20443v1)**  
  Authors: Spencer Carmichael, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20443v1.pdf)  
  Keywords: 3d gaussian, dynamic, localization, illumination, slam, gaussian splatting, tracking, mapping, fast, ar, motion, robotics  
- **[OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2603.18510v1)**  
  Authors: Hongjia Zhai, Qi Zhang, Xiaokun Pan, Xiyu Zhang, Yitong Dong, Huaqi Zhang, Dan Xu, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18510v1.pdf)  
  Keywords: 3d gaussian, efficient, understanding, gaussian splatting, semantic, mapping, ar  
- **[Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning](https://arxiv.org/abs/2603.18402v1)**  
  Authors: Yonghan Lee, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18402v1.pdf)  
  Keywords: dynamic, tracking, gaussian splatting, ar, motion, 4d, segmentation  
- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: face, 3d gaussian, understanding, lighting, slam, gaussian splatting, semantic, mapping, ar, segmentation  

### Scene Understanding

*Showing the latest 50 out of 131 papers*

- **[Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction](https://arxiv.org/abs/2603.22852v1)**  
  Authors: Chengxin Lv, Yihui Li, Hongyu Yang, YunHong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22852v1.pdf)  
  Keywords: 3d gaussian, efficient, compact, geometry, semantic, autonomous driving, ar  
- **[PhotoAgent: A Robotic Photographer with Spatial and Aesthetic Understanding](https://arxiv.org/abs/2603.22796v1)**  
  Authors: Lirong Che, Zhenfeng Gan, Yanbo Chen, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22796v1.pdf)  
  Keywords: 3d gaussian, understanding, reflection, gaussian splatting, semantic, ar  
- **[Instrument-Splatting++: Towards Controllable Surgical Instrument Digital Twin Using Gaussian Splatting](https://arxiv.org/abs/2603.22792v2)**  
  Authors: Shuojue Yang, Zijian Wu, Chengjiaao Liao, Qian Li, Daiyun Shen, Chang Han Low, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22792v2.pdf)  
  Keywords: 3d gaussian, geometry, tracking, gaussian splatting, semantic, ar  
- **[FreeArtGS: Articulated Gaussian Splatting Under Free-moving Scenario](https://arxiv.org/abs/2603.22102v1)**  
  Authors: Hang Dai, Hongwei Fan, Han Zhang, Duojin Wu, Jiyao Zhang, Hao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22102v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://freeartgs.github.io)  
  Keywords: tracking, geometry, gaussian splatting, ar, motion, segmentation, robotics  
- **[Training-Free Instance-Aware 3D Scene Reconstruction and Diffusion-Based View Synthesis from Sparse Images](https://arxiv.org/abs/2603.21166v1)**  
  Authors: Jiatong Xia, Lingqiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21166v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiatongxia.github.io/TID3R)  
  Keywords: high-fidelity, efficient, understanding, geometry, ar, segmentation  
- **[Glove2Hand: Synthesizing Natural Hand-Object Interaction from Multi-Modal Sensing Gloves](https://arxiv.org/abs/2603.20850v1)**  
  Authors: Xinyu Zhang, Ziyi Kou, Chuan Qin, Mia Huang, Ergys Ristani, Ankit Kumar, Lele Chen, Kun He, Abdeslam Boularias, Li Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20850v1.pdf)  
  Keywords: 3d gaussian, dynamic, understanding, vr, tracking, ar, motion, deformation, robotics  
- **[HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks](https://arxiv.org/abs/2603.19822v1)**  
  Authors: Jingyu Guo, Ziye Chen, Ziwen Li, Zhengqing Gao, Jiaxin Huang, Hanlue Zhang, Fengming Huang, Yu Yao, Tongliang Liu, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19822v1.pdf)  
  Keywords: 3d gaussian, lighting, geometry, gaussian splatting, semantic, ar  
- **[Reconstruction Matters: Learning Geometry-Aligned BEV Representation through 3D Gaussian Splatting](https://arxiv.org/abs/2603.19193v1)**  
  Authors: Yiren Lu, Xin Ye, Burhaneddin Yaman, Jingru Luo, Zhexiao Xiong, Liu Ren, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19193v1.pdf)  
  Keywords: 3d gaussian, understanding, 3d reconstruction, geometry, gaussian splatting, semantic, autonomous driving, ar, motion, segmentation  
- **[GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning](https://arxiv.org/abs/2603.19137v1)**  
  Authors: Yiren Lu, Yi Du, Disheng Liu, Yunlai Zhou, Chen Wang, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19137v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, geometry, gaussian splatting, semantic, ar  
- **[GHOST: Fast Category-agnostic Hand-Object Interaction Reconstruction from RGB Videos using Gaussian Splatting](https://arxiv.org/abs/2603.18912v1)**  
  Authors: Ahmed Tawfik Aboukhadra, Marcel Rogge, Nadia Robertini, Abdalla Arafa, Jameel Malik, Ahmed Elhayek, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18912v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ATAboukhadra/GHOST?style=social)](https://github.com/ATAboukhadra/GHOST)  
  Keywords: efficient, dynamic, understanding, 3d reconstruction, vr, gaussian splatting, fast, ar, robotics  



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