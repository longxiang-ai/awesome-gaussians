# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-03-31 01:21:12

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
- [Avatar Generation](#avatar-generation) (157 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (203 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (33 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (208 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (16 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (218 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (128 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (21 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (74 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (75 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (132 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: 3d gaussian, ar, gaussian splatting, survey, vr  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v4)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v4.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, survey, ray tracing, mapping  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: dynamic, 3d gaussian, efficient, localization, ar, gaussian splatting, face, survey, tracking, mapping, motion, slam  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: 3d gaussian, robotics, ar, gaussian splatting, survey  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v3)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v3.pdf)  
  Keywords: efficient, 3d gaussian, ar, gaussian splatting, survey, geometry, nerf  
- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197v1)**  
  Authors: Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07197v1.pdf)  
  Keywords: compression, 3d reconstruction, 3d gaussian, dynamic, high-fidelity, efficient, 4d, ar, gaussian splatting, survey, compact  

### Acceleration

*Showing the latest 50 out of 118 papers*

- **[DiffSoup: Direct Differentiable Rasterization of Triangle Soup for Extreme Radiance Field Simplification](https://arxiv.org/abs/2603.27151v1)**  
  Authors: Kenji Tojo, Bernd Bickel, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27151v1.pdf) | [![GitHub](https://img.shields.io/github/stars/kenji-tojo/diffsoup?style=social)](https://github.com/kenji-tojo/diffsoup)  
  Keywords: efficient, 3d gaussian, ar, gaussian splatting, real-time rendering  
- **[ViewSplat: View-Adaptive Dynamic Gaussian Splatting for Feed-Forward Synthesis](https://arxiv.org/abs/2603.25265v1)**  
  Authors: Moonyeon Jeong, Seunggi Min, Suhyeon Lee, Hongje Seong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25265v1.pdf)  
  Keywords: dynamic, 3d gaussian, high-fidelity, fast, ar, gaussian splatting, real-time rendering  
- **[MoRGS: Efficient Per-Gaussian Motion Reasoning for Streamable Dynamic 3D Scenes](https://arxiv.org/abs/2603.25042v1)**  
  Authors: Wonjoon Lee, Sungmin Woo, Donghyeong Kim, Jungho Lee, Sangheon Park, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25042v1.pdf)  
  Keywords: lightweight, dynamic, 3d gaussian, efficient, fast, 4d, ar, gaussian splatting, motion, real-time rendering  
- **[Confidence-Based Mesh Extraction from 3D Gaussians](https://arxiv.org/abs/2603.24725v1)**  
  Authors: Lukas Radl, Felix Windisch, Andreas Kurz, Thomas Köhler, Michael Steiner, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24725v1.pdf)  
  Keywords: efficient, dynamic, 3d gaussian, fast, ar, gaussian splatting, face  
- **[Accurate Point Measurement in 3DGS -- A New Alternative to Traditional Stereoscopic-View Based Measurements](https://arxiv.org/abs/2603.24716v1)**  
  Authors: Deyan Deng, Rongjun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24716v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/3dgs_measurement_tool?style=social)](https://github.com/GDAOSU/3dgs_measurement_tool)  
  Keywords: ar, gaussian splatting, real-time rendering, 3d gaussian  
- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, efficient, high-fidelity, fast, ar, gaussian splatting, face  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: head, efficient, animation, 3d gaussian, high-fidelity, fast, ar, avatar, face, geometry  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: 3d gaussian, path tracing, ar, face, geometry, real-time rendering  
- **[Fast undersampled dynamic MRI reconstruction using explicit representation learning with Gaussian splatting](https://arxiv.org/abs/2603.21980v1)**  
  Authors: M. L. Terpstra, C. A. T. van den Berg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21980v1.pdf)  
  Keywords: efficient, dynamic, fast, ar, gaussian splatting, motion  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: efficient, 3d gaussian, high-fidelity, fast, ar, gaussian splatting, face, ray tracing, geometry, real-time rendering, nerf  

### Applications

*Showing the latest 50 out of 500 papers*

- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516v1)**  
  Authors: Jiahao Niu, Rongjia Zheng, Wenju Xu, WeiShi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27516v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GrumpySloths/SGS_Intrinsic.github.io?style=social)](https://github.com/GrumpySloths/SGS_Intrinsic.github.io)  
  Keywords: sparse view, 3d gaussian, sparse-view, illumination, semantic, ar, gaussian splatting, shadow, geometry  
- **[From None to All: Self-Supervised 3D Reconstruction via Novel View Synthesis](https://arxiv.org/abs/2603.27455v1)**  
  Authors: Ranran Huang, Weixun Luo, Ye Mao, Krystian Mikolajczyk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27455v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ranrhuang.github.io/nas3r)  
  Keywords: ar, 3d reconstruction, 3d gaussian, geometry  
- **[NimbusGS: Unified 3D Scene Reconstruction under Hybrid Weather](https://arxiv.org/abs/2603.27228v1)**  
  Authors: Yanying Li, Jinyang Li, Shengfeng He, Yangyang Xu, Junyu Dong, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27228v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lyy-ovo/NimbusGS?style=social)](https://github.com/lyy-ovo/NimbusGS)  
  Keywords: ar, dynamic, 3d gaussian, geometry  
- **[DiffSoup: Direct Differentiable Rasterization of Triangle Soup for Extreme Radiance Field Simplification](https://arxiv.org/abs/2603.27151v1)**  
  Authors: Kenji Tojo, Bernd Bickel, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27151v1.pdf) | [![GitHub](https://img.shields.io/github/stars/kenji-tojo/diffsoup?style=social)](https://github.com/kenji-tojo/diffsoup)  
  Keywords: efficient, 3d gaussian, ar, gaussian splatting, real-time rendering  
- **[Detailed Geometry and Appearance from Opportunistic Motion](https://arxiv.org/abs/2603.26665v1)**  
  Authors: Ryosuke Hirai, Kohei Yamashita, Antoine Guédon, Ryo Kawahara, Vincent Lepetit, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26665v1.pdf)  
  Keywords: sparse view, illumination, ar, gaussian splatting, geometry, motion  
- **[GaussianGPT: Towards Autoregressive 3D Gaussian Scene Generation](https://arxiv.org/abs/2603.26661v1)**  
  Authors: Nicolas von Lützow, Barbara Rössle, Katharina Schmid, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26661v1.pdf)  
  Keywords: ar, 3d gaussian, neural rendering  
- **[Drive-Through 3D Vehicle Exterior Reconstruction via Dynamic-Scene SfM and Distortion-Aware Gaussian Splatting](https://arxiv.org/abs/2603.26638v1)**  
  Authors: Nitin Kulkarni, Akhil Devarashetti, Charlie Cluss, Livio Forte, Philip Schneider, Chunming Qiao, Alina Vereshchaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26638v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, dynamic, high-fidelity, segmentation, semantic, ar, gaussian splatting, face, geometry, motion  
- **[Scene Grounding In the Wild](https://arxiv.org/abs/2603.26584v1)**  
  Authors: Tamir Cohen, Leo Segre, Shay Shomer-Chai, Shai Avidan, Hadar Averbuch-Elor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26584v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, semantic, ar, gaussian splatting, geometry  
- **[GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport](https://arxiv.org/abs/2603.26181v1)**  
  Authors: Youngju Na, Jaeseong Yun, Soohyun Ryu, Hyunsu Kim, Sung-Eui Yoon, Suyong Yeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26181v1.pdf)  
  Keywords: 3d gaussian, localization, relighting, ar, gaussian splatting, face, geometry, lighting  
- **[R-PGA: Robust Physical Adversarial Camouflage Generation via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2603.26067v1)**  
  Authors: Tianrui Lou, Siyuan Liang, Jiawei Liang, Yuze Gao, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26067v1.pdf)  
  Keywords: relightable, dynamic, 3d gaussian, autonomous driving, illumination, ar, gaussian splatting, lighting, mapping  

### Avatar Generation

*Showing the latest 50 out of 157 papers*

- **[Drive-Through 3D Vehicle Exterior Reconstruction via Dynamic-Scene SfM and Distortion-Aware Gaussian Splatting](https://arxiv.org/abs/2603.26638v1)**  
  Authors: Nitin Kulkarni, Akhil Devarashetti, Charlie Cluss, Livio Forte, Philip Schneider, Chunming Qiao, Alina Vereshchaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26638v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, dynamic, high-fidelity, segmentation, semantic, ar, gaussian splatting, face, geometry, motion  
- **[GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport](https://arxiv.org/abs/2603.26181v1)**  
  Authors: Youngju Na, Jaeseong Yun, Soohyun Ryu, Hyunsu Kim, Sung-Eui Yoon, Suyong Yeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26181v1.pdf)  
  Keywords: 3d gaussian, localization, relighting, ar, gaussian splatting, face, geometry, lighting  
- **[arg-VU: Affordance Reasoning with Physics-Aware 3D Geometry for Visual Understanding in Robotic Surgery](https://arxiv.org/abs/2603.26814v1)**  
  Authors: Nan Xiao, Yunxin Fan, Farong Wang, Fei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26814v1.pdf)  
  Keywords: dynamic, 3d gaussian, robotics, understanding, ar, gaussian splatting, deformation, face, tracking, geometry, motion  
- **[Confidence-Based Mesh Extraction from 3D Gaussians](https://arxiv.org/abs/2603.24725v1)**  
  Authors: Lukas Radl, Felix Windisch, Andreas Kurz, Thomas Köhler, Michael Steiner, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24725v1.pdf)  
  Keywords: efficient, dynamic, 3d gaussian, fast, ar, gaussian splatting, face  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: head, efficient, 3d gaussian, neural rendering, ar, gaussian splatting, face, large scene  
- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, efficient, high-fidelity, fast, ar, gaussian splatting, face  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: head, efficient, animation, 3d gaussian, high-fidelity, fast, ar, avatar, face, geometry  
- **[GSwap: Realistic Head Swapping with Dynamic Neural Gaussian Field](https://arxiv.org/abs/2603.23168v1)**  
  Authors: Jingtao Zhou, Xuan Gao, Dongyu Liu, Junhui Hou, Yudong Guo, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23168v1.pdf)  
  Keywords: head, dynamic, 3d gaussian, efficient, high-fidelity, body, ar, face, motion  
- **[UniQueR: Unified Query-based Feedforward 3D Reconstruction](https://arxiv.org/abs/2603.22851v1)**  
  Authors: Chensheng Peng, Quentin Herau, Jiezhi Yang, Yichen Xie, Yihan Hu, Wenzhao Zheng, Matthew Strong, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22851v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, efficient, ar, face, geometry, compact, vr, nerf  
- **[FullCircle: Effortless 3D Reconstruction from Casual 360$^\circ$ Captures](https://arxiv.org/abs/2603.22572v1)**  
  Authors: Yalda Foroutan, Ipek Oztas, Daniel Rebain, Aysegul Dundar, Kwang Moo Yi, Lily Goli, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22572v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://theialab.github.io/fullcircle)  
  Keywords: ar, human, 3d reconstruction  

### Dynamic Scene

*Showing the latest 50 out of 203 papers*

- **[NimbusGS: Unified 3D Scene Reconstruction under Hybrid Weather](https://arxiv.org/abs/2603.27228v1)**  
  Authors: Yanying Li, Jinyang Li, Shengfeng He, Yangyang Xu, Junyu Dong, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27228v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lyy-ovo/NimbusGS?style=social)](https://github.com/lyy-ovo/NimbusGS)  
  Keywords: ar, dynamic, 3d gaussian, geometry  
- **[Detailed Geometry and Appearance from Opportunistic Motion](https://arxiv.org/abs/2603.26665v1)**  
  Authors: Ryosuke Hirai, Kohei Yamashita, Antoine Guédon, Ryo Kawahara, Vincent Lepetit, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26665v1.pdf)  
  Keywords: sparse view, illumination, ar, gaussian splatting, geometry, motion  
- **[Drive-Through 3D Vehicle Exterior Reconstruction via Dynamic-Scene SfM and Distortion-Aware Gaussian Splatting](https://arxiv.org/abs/2603.26638v1)**  
  Authors: Nitin Kulkarni, Akhil Devarashetti, Charlie Cluss, Livio Forte, Philip Schneider, Chunming Qiao, Alina Vereshchaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26638v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, dynamic, high-fidelity, segmentation, semantic, ar, gaussian splatting, face, geometry, motion  
- **[R-PGA: Robust Physical Adversarial Camouflage Generation via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2603.26067v1)**  
  Authors: Tianrui Lou, Siyuan Liang, Jiawei Liang, Yuze Gao, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26067v1.pdf)  
  Keywords: relightable, dynamic, 3d gaussian, autonomous driving, illumination, ar, gaussian splatting, lighting, mapping  
- **[arg-VU: Affordance Reasoning with Physics-Aware 3D Geometry for Visual Understanding in Robotic Surgery](https://arxiv.org/abs/2603.26814v1)**  
  Authors: Nan Xiao, Yunxin Fan, Farong Wang, Fei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26814v1.pdf)  
  Keywords: dynamic, 3d gaussian, robotics, understanding, ar, gaussian splatting, deformation, face, tracking, geometry, motion  
- **[Unblur-SLAM: Dense Neural SLAM for Blurry Inputs](https://arxiv.org/abs/2603.26810v1)**  
  Authors: Qi Zhang, Denis Rozumny, Francesco Girlanda, Sezer Karaoglu, Marc Pollefeys, Theo Gevers, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26810v1.pdf)  
  Keywords: 3d reconstruction, ar, mapping, tracking, geometry, motion, slam  
- **[ViewSplat: View-Adaptive Dynamic Gaussian Splatting for Feed-Forward Synthesis](https://arxiv.org/abs/2603.25265v1)**  
  Authors: Moonyeon Jeong, Seunggi Min, Suhyeon Lee, Hongje Seong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25265v1.pdf)  
  Keywords: dynamic, 3d gaussian, high-fidelity, fast, ar, gaussian splatting, real-time rendering  
- **[Learning Explicit Continuous Motion Representation for Dynamic Gaussian Splatting from Monocular Videos](https://arxiv.org/abs/2603.25058v1)**  
  Authors: Xuankai Zhang, Junjin Xiao, Shangwei Huang, Wei-shi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25058v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hhhddddddd/se3bsplinegs?style=social)](https://github.com/hhhddddddd/se3bsplinegs)  
  Keywords: dynamic, ar, gaussian splatting, motion, compact, deformation  
- **[MoRGS: Efficient Per-Gaussian Motion Reasoning for Streamable Dynamic 3D Scenes](https://arxiv.org/abs/2603.25042v1)**  
  Authors: Wonjoon Lee, Sungmin Woo, Donghyeong Kim, Jungho Lee, Sangheon Park, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25042v1.pdf)  
  Keywords: lightweight, dynamic, 3d gaussian, efficient, fast, 4d, ar, gaussian splatting, motion, real-time rendering  
- **[$π$, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation](https://arxiv.org/abs/2603.25038v1)**  
  Authors: Johnathan Tucker, Denis Liu, Aiden Swann, Allen Ren, Javier Yu, Jiankai Sun, Brandon Kim, Lachlain McGranahan, Quan Vuong, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25038v1.pdf)  
  Keywords: ar, gaussian splatting, dynamic  

### Few-shot

- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516v1)**  
  Authors: Jiahao Niu, Rongjia Zheng, Wenju Xu, WeiShi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27516v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GrumpySloths/SGS_Intrinsic.github.io?style=social)](https://github.com/GrumpySloths/SGS_Intrinsic.github.io)  
  Keywords: sparse view, 3d gaussian, sparse-view, illumination, semantic, ar, gaussian splatting, shadow, geometry  
- **[Detailed Geometry and Appearance from Opportunistic Motion](https://arxiv.org/abs/2603.26665v1)**  
  Authors: Ryosuke Hirai, Kohei Yamashita, Antoine Guédon, Ryo Kawahara, Vincent Lepetit, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26665v1.pdf)  
  Keywords: sparse view, illumination, ar, gaussian splatting, geometry, motion  
- **[AirSplat: Alignment and Rating for Robust Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.25129v1)**  
  Authors: Minh-Quan Viet Bui, Jaeho Moon, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25129v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, sparse-view, ar, gaussian splatting, geometry  
- **[EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](https://arxiv.org/abs/2603.21332v2)**  
  Authors: Haolan Xu, Keli Cheng, Lei Wang, Ning Bi, Xiaoming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21332v2.pdf)  
  Keywords: head, 3d gaussian, ar, gaussian splatting, motion, few-shot, face, lighting, nerf  
- **[UniSem: Generalizable Semantic 3D Reconstruction from Sparse Unposed Images](https://arxiv.org/abs/2603.17519v1)**  
  Authors: Guibiao Liao, Qian Ren, Kaimin Liao, Hua Wang, Zhi Chen, Luchao Wang, Yaohua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17519v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, segmentation, sparse-view, semantic, ar, gaussian splatting, geometry  
- **[S2D: Sparse to Dense Lifting for 3D Reconstruction with Minimal Inputs](https://arxiv.org/abs/2603.10893v1)**  
  Authors: Yuzhou Ji, Qijian Tian, He Zhu, Xiaoqi Jiang, Guangzhi Cao, Lizhuang Ma, Yuan Xie, Xin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10893v1.pdf)  
  Keywords: sparse view, 3d reconstruction, 3d gaussian, efficient, high-fidelity, understanding, ar, gaussian splatting  
- **[Active View Selection with Perturbed Gaussian Ensemble for Tomographic Reconstruction](https://arxiv.org/abs/2603.06852v1)**  
  Authors: Yulun Wu, Ruyi Zha, Wei Cao, Yingying Li, Yuanhao Cai, Yaoyao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06852v1.pdf)  
  Keywords: 3d gaussian, sparse-view, fast, ar, gaussian splatting  
- **[CylinderSplat: 3D Gaussian Splatting with Cylindrical Triplanes for Panoramic Novel View Synthesis](https://arxiv.org/abs/2603.05882v1)**  
  Authors: Qiwei Wang, Xianghui Ze, Jingyi Yu, Yujiao Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05882v1.pdf)  
  Keywords: 3d gaussian, sparse-view, ar, gaussian splatting, geometry  
- **[DSA-SRGS: Super-Resolution Gaussian Splatting for Dynamic Sparse-View DSA Reconstruction](https://arxiv.org/abs/2603.04770v1)**  
  Authors: Shiyu Zhang, Zhicong Wu, Huangxuan Zhao, Zhentao Liu, Lei Chen, Yong Luo, Lefei Zhang, Zhiming Cui, Ziwen Ke, Bo Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04770v1.pdf)  
  Keywords: dynamic, sparse-view, 4d, ar, gaussian splatting  
- **[Intrinsic Geometry-Appearance Consistency Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2603.02893v1)**  
  Authors: Kaiqiang Xiong, Rui Peng, Jiahao Wu, Zhanke Wang, Jie Liang, Xiaoyun Zheng, Feng Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02893v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, sparse-view, human, ar, gaussian splatting, geometry  

### Geometry Reconstruction

*Showing the latest 50 out of 208 papers*

- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516v1)**  
  Authors: Jiahao Niu, Rongjia Zheng, Wenju Xu, WeiShi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27516v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GrumpySloths/SGS_Intrinsic.github.io?style=social)](https://github.com/GrumpySloths/SGS_Intrinsic.github.io)  
  Keywords: sparse view, 3d gaussian, sparse-view, illumination, semantic, ar, gaussian splatting, shadow, geometry  
- **[From None to All: Self-Supervised 3D Reconstruction via Novel View Synthesis](https://arxiv.org/abs/2603.27455v1)**  
  Authors: Ranran Huang, Weixun Luo, Ye Mao, Krystian Mikolajczyk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27455v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ranrhuang.github.io/nas3r)  
  Keywords: ar, 3d reconstruction, 3d gaussian, geometry  
- **[NimbusGS: Unified 3D Scene Reconstruction under Hybrid Weather](https://arxiv.org/abs/2603.27228v1)**  
  Authors: Yanying Li, Jinyang Li, Shengfeng He, Yangyang Xu, Junyu Dong, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27228v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lyy-ovo/NimbusGS?style=social)](https://github.com/lyy-ovo/NimbusGS)  
  Keywords: ar, dynamic, 3d gaussian, geometry  
- **[Detailed Geometry and Appearance from Opportunistic Motion](https://arxiv.org/abs/2603.26665v1)**  
  Authors: Ryosuke Hirai, Kohei Yamashita, Antoine Guédon, Ryo Kawahara, Vincent Lepetit, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26665v1.pdf)  
  Keywords: sparse view, illumination, ar, gaussian splatting, geometry, motion  
- **[Drive-Through 3D Vehicle Exterior Reconstruction via Dynamic-Scene SfM and Distortion-Aware Gaussian Splatting](https://arxiv.org/abs/2603.26638v1)**  
  Authors: Nitin Kulkarni, Akhil Devarashetti, Charlie Cluss, Livio Forte, Philip Schneider, Chunming Qiao, Alina Vereshchaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26638v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, dynamic, high-fidelity, segmentation, semantic, ar, gaussian splatting, face, geometry, motion  
- **[Scene Grounding In the Wild](https://arxiv.org/abs/2603.26584v1)**  
  Authors: Tamir Cohen, Leo Segre, Shay Shomer-Chai, Shai Avidan, Hadar Averbuch-Elor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26584v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, semantic, ar, gaussian splatting, geometry  
- **[GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport](https://arxiv.org/abs/2603.26181v1)**  
  Authors: Youngju Na, Jaeseong Yun, Soohyun Ryu, Hyunsu Kim, Sung-Eui Yoon, Suyong Yeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26181v1.pdf)  
  Keywords: 3d gaussian, localization, relighting, ar, gaussian splatting, face, geometry, lighting  
- **[arg-VU: Affordance Reasoning with Physics-Aware 3D Geometry for Visual Understanding in Robotic Surgery](https://arxiv.org/abs/2603.26814v1)**  
  Authors: Nan Xiao, Yunxin Fan, Farong Wang, Fei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26814v1.pdf)  
  Keywords: dynamic, 3d gaussian, robotics, understanding, ar, gaussian splatting, deformation, face, tracking, geometry, motion  
- **[Unblur-SLAM: Dense Neural SLAM for Blurry Inputs](https://arxiv.org/abs/2603.26810v1)**  
  Authors: Qi Zhang, Denis Rozumny, Francesco Girlanda, Sezer Karaoglu, Marc Pollefeys, Theo Gevers, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26810v1.pdf)  
  Keywords: 3d reconstruction, ar, mapping, tracking, geometry, motion, slam  
- **[AirSplat: Alignment and Rating for Robust Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.25129v1)**  
  Authors: Minh-Quan Viet Bui, Jaeho Moon, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25129v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, sparse-view, ar, gaussian splatting, geometry  

### Large Scene

- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: head, efficient, 3d gaussian, neural rendering, ar, gaussian splatting, face, large scene  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: head, dynamic, outdoor, efficient, ar, gaussian splatting, tracking, slam  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: outdoor, 3d gaussian, localization, ar, gaussian splatting, geometry  
- **[EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.06216v1)**  
  Authors: Miriam Jäger, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06216v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, ar, gaussian splatting, face, geometry, urban scene  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: relightable, 3d reconstruction, 3d gaussian, outdoor, reflection, illumination, fast, relighting, ar, gaussian splatting, lighting, nerf  
- **[Interactive Augmented Reality-enabled Outdoor Scene Visualization For Enhanced Real-time Disaster Response](https://arxiv.org/abs/2602.21874v1)**  
  Authors: Dimitrios Apostolakis, Georgios Angelidis, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21874v1.pdf)  
  Keywords: lightweight, outdoor, 3d gaussian, semantic, fast, ar, gaussian splatting, face, lighting  
- **[Large-scale Photorealistic Outdoor 3D Scene Reconstruction from UAV Imagery Using Gaussian Splatting Techniques](https://arxiv.org/abs/2602.20342v1)**  
  Authors: Christos Maikos, Georgios Angelidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20342v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, outdoor, high-fidelity, efficient, neural rendering, ar, gaussian splatting, vr, nerf  
- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: head, outdoor, 3d gaussian, localization, semantic, ar, gaussian splatting, geometry, lighting, mapping  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: autonomous driving, 3d gaussian, outdoor, global illumination, illumination, ar, gaussian splatting, lighting, real-time rendering, nerf  
- **[Zero-Shot UAV Navigation in Forests via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2602.07101v2)**  
  Authors: Zinan Lv, Yeqian Qian, Chen Sang, Hao Liu, Danping Zou, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07101v2.pdf)  
  Keywords: lightweight, relightable, dynamic, 3d gaussian, outdoor, high-fidelity, illumination, ar, gaussian splatting, geometry, lighting  

### Model Compression

*Showing the latest 50 out of 218 papers*

- **[DiffSoup: Direct Differentiable Rasterization of Triangle Soup for Extreme Radiance Field Simplification](https://arxiv.org/abs/2603.27151v1)**  
  Authors: Kenji Tojo, Bernd Bickel, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27151v1.pdf) | [![GitHub](https://img.shields.io/github/stars/kenji-tojo/diffsoup?style=social)](https://github.com/kenji-tojo/diffsoup)  
  Keywords: efficient, 3d gaussian, ar, gaussian splatting, real-time rendering  
- **[Less Gaussians, Texture More: 4K Feed-Forward Textured Splatting](https://arxiv.org/abs/2603.25745v1)**  
  Authors: Yixing Lao, Xuyang Bai, Xiaoyang Wu, Nuoyuan Yan, Zixin Luo, Tian Fang, Jean-Daniel Nahmias, Yanghai Tsin, Shiwei Li, Hengshuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25745v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yxlao.github.io/lgtm)  
  Keywords: 3d gaussian, high-fidelity, ar, gaussian splatting, compact  
- **[Learning Explicit Continuous Motion Representation for Dynamic Gaussian Splatting from Monocular Videos](https://arxiv.org/abs/2603.25058v1)**  
  Authors: Xuankai Zhang, Junjin Xiao, Shangwei Huang, Wei-shi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25058v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hhhddddddd/se3bsplinegs?style=social)](https://github.com/hhhddddddd/se3bsplinegs)  
  Keywords: dynamic, ar, gaussian splatting, motion, compact, deformation  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v2)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v2.pdf)  
  Keywords: efficient, 3d reconstruction, 3d gaussian, ar, gaussian splatting, geometry  
- **[MoRGS: Efficient Per-Gaussian Motion Reasoning for Streamable Dynamic 3D Scenes](https://arxiv.org/abs/2603.25042v1)**  
  Authors: Wonjoon Lee, Sungmin Woo, Donghyeong Kim, Jungho Lee, Sangheon Park, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25042v1.pdf)  
  Keywords: lightweight, dynamic, 3d gaussian, efficient, fast, 4d, ar, gaussian splatting, motion, real-time rendering  
- **[Confidence-Based Mesh Extraction from 3D Gaussians](https://arxiv.org/abs/2603.24725v1)**  
  Authors: Lukas Radl, Felix Windisch, Andreas Kurz, Thomas Köhler, Michael Steiner, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24725v1.pdf)  
  Keywords: efficient, dynamic, 3d gaussian, fast, ar, gaussian splatting, face  
- **[SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision](https://arxiv.org/abs/2603.24036v1)**  
  Authors: Avigail Cohen Rimon, Amir Mann, Mirela Ben Chen, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24036v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, tracking, compact, deformation  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: head, efficient, 3d gaussian, neural rendering, ar, gaussian splatting, face, large scene  
- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, efficient, high-fidelity, fast, ar, gaussian splatting, face  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: head, efficient, animation, 3d gaussian, high-fidelity, fast, ar, avatar, face, geometry  

### Quality Enhancement

*Showing the latest 50 out of 128 papers*

- **[Drive-Through 3D Vehicle Exterior Reconstruction via Dynamic-Scene SfM and Distortion-Aware Gaussian Splatting](https://arxiv.org/abs/2603.26638v1)**  
  Authors: Nitin Kulkarni, Akhil Devarashetti, Charlie Cluss, Livio Forte, Philip Schneider, Chunming Qiao, Alina Vereshchaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26638v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, dynamic, high-fidelity, segmentation, semantic, ar, gaussian splatting, face, geometry, motion  
- **[Less Gaussians, Texture More: 4K Feed-Forward Textured Splatting](https://arxiv.org/abs/2603.25745v1)**  
  Authors: Yixing Lao, Xuyang Bai, Xiaoyang Wu, Nuoyuan Yan, Zixin Luo, Tian Fang, Jean-Daniel Nahmias, Yanghai Tsin, Shiwei Li, Hengshuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25745v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yxlao.github.io/lgtm)  
  Keywords: 3d gaussian, high-fidelity, ar, gaussian splatting, compact  
- **[ViewSplat: View-Adaptive Dynamic Gaussian Splatting for Feed-Forward Synthesis](https://arxiv.org/abs/2603.25265v1)**  
  Authors: Moonyeon Jeong, Seunggi Min, Suhyeon Lee, Hongje Seong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25265v1.pdf)  
  Keywords: dynamic, 3d gaussian, high-fidelity, fast, ar, gaussian splatting, real-time rendering  
- **[AirSplat: Alignment and Rating for Robust Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.25129v1)**  
  Authors: Minh-Quan Viet Bui, Jaeho Moon, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25129v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, sparse-view, ar, gaussian splatting, geometry  
- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, efficient, high-fidelity, fast, ar, gaussian splatting, face  
- **[FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures](https://arxiv.org/abs/2603.23345v1)**  
  Authors: Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen, Chengfei Lv, Fan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23345v1.pdf)  
  Keywords: head, efficient, animation, 3d gaussian, high-fidelity, fast, ar, avatar, face, geometry  
- **[GSwap: Realistic Head Swapping with Dynamic Neural Gaussian Field](https://arxiv.org/abs/2603.23168v1)**  
  Authors: Jingtao Zhou, Xuan Gao, Dongyu Liu, Junhui Hou, Yudong Guo, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23168v1.pdf)  
  Keywords: head, dynamic, 3d gaussian, efficient, high-fidelity, body, ar, face, motion  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: efficient, 3d gaussian, high-fidelity, fast, ar, gaussian splatting, face, ray tracing, geometry, real-time rendering, nerf  
- **[Training-Free Instance-Aware 3D Scene Reconstruction and Diffusion-Based View Synthesis from Sparse Images](https://arxiv.org/abs/2603.21166v1)**  
  Authors: Jiatong Xia, Lingqiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21166v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiatongxia.github.io/TID3R)  
  Keywords: efficient, high-fidelity, segmentation, understanding, ar, geometry  
- **[2Xplat: Two Experts Are Better Than One Generalist](https://arxiv.org/abs/2603.21064v2)**  
  Authors: Hwasik Jeong, Seungryong Lee, Gyeongjin Kang, Seungkwon Yang, Xiangyu Sun, Seungtae Nam, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21064v2.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, gaussian splatting, geometry  

### Ray Tracing

- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: relightable, 3d gaussian, reflection, ar, gaussian splatting, ray tracing, shadow, mapping  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: 3d gaussian, path tracing, ar, face, geometry, real-time rendering  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: efficient, 3d gaussian, high-fidelity, fast, ar, gaussian splatting, face, ray tracing, geometry, real-time rendering, nerf  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v4)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v4.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, survey, ray tracing, mapping  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: efficient, ray marching, 3d gaussian, high-fidelity, ar, gaussian splatting, real-time rendering  
- **[Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction](https://arxiv.org/abs/2603.08503v1)**  
  Authors: Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08503v1.pdf) | [![GitHub](https://img.shields.io/github/stars/1170632760/Spherical-GOF?style=social)](https://github.com/1170632760/Spherical-GOF)  
  Keywords: ray casting, 3d gaussian, efficient, robotics, fast, ar, gaussian splatting, geometry  
- **[Ref-DGS: Reflective Dual Gaussian Splatting](https://arxiv.org/abs/2603.07664v2)**  
  Authors: Ningjing Fan, Yiqun Wang, Dongming Yan, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07664v2.pdf)  
  Keywords: lightweight, efficient, reflection, fast, ar, gaussian splatting, face, ray tracing, geometry  
- **[Radiometrically Consistent Gaussian Surfels for Inverse Rendering](https://arxiv.org/abs/2603.01491v1)**  
  Authors: Kyu Beom Han, Jaeyoon Kim, Woo Jae Kim, Jinhwan Seo, Sung-eui Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01491v1.pdf)  
  Keywords: efficient, reflection, illumination, relighting, ar, gaussian splatting, ray tracing, lighting, global illumination  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: autonomous driving, 3d gaussian, outdoor, global illumination, illumination, ar, gaussian splatting, lighting, real-time rendering, nerf  
- **[Rotated Lights for Consistent and Efficient 2D Gaussians Inverse Rendering](https://arxiv.org/abs/2602.08724v1)**  
  Authors: Geng Lin, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08724v1.pdf)  
  Keywords: efficient, illumination, relighting, ar, gaussian splatting, shadow, geometry, lighting, global illumination  

### Relighting

*Showing the latest 50 out of 74 papers*

- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516v1)**  
  Authors: Jiahao Niu, Rongjia Zheng, Wenju Xu, WeiShi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27516v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GrumpySloths/SGS_Intrinsic.github.io?style=social)](https://github.com/GrumpySloths/SGS_Intrinsic.github.io)  
  Keywords: sparse view, 3d gaussian, sparse-view, illumination, semantic, ar, gaussian splatting, shadow, geometry  
- **[Detailed Geometry and Appearance from Opportunistic Motion](https://arxiv.org/abs/2603.26665v1)**  
  Authors: Ryosuke Hirai, Kohei Yamashita, Antoine Guédon, Ryo Kawahara, Vincent Lepetit, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26665v1.pdf)  
  Keywords: sparse view, illumination, ar, gaussian splatting, geometry, motion  
- **[GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport](https://arxiv.org/abs/2603.26181v1)**  
  Authors: Youngju Na, Jaeseong Yun, Soohyun Ryu, Hyunsu Kim, Sung-Eui Yoon, Suyong Yeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26181v1.pdf)  
  Keywords: 3d gaussian, localization, relighting, ar, gaussian splatting, face, geometry, lighting  
- **[R-PGA: Robust Physical Adversarial Camouflage Generation via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2603.26067v1)**  
  Authors: Tianrui Lou, Siyuan Liang, Jiawei Liang, Yuze Gao, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26067v1.pdf)  
  Keywords: relightable, dynamic, 3d gaussian, autonomous driving, illumination, ar, gaussian splatting, lighting, mapping  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: relightable, 3d gaussian, reflection, ar, gaussian splatting, ray tracing, shadow, mapping  
- **[PhotoAgent: A Robotic Photographer with Spatial and Aesthetic Understanding](https://arxiv.org/abs/2603.22796v1)**  
  Authors: Lirong Che, Zhenfeng Gan, Yanbo Chen, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22796v1.pdf)  
  Keywords: 3d gaussian, understanding, reflection, semantic, ar, gaussian splatting  
- **[EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](https://arxiv.org/abs/2603.21332v2)**  
  Authors: Haolan Xu, Keli Cheng, Lei Wang, Ning Bi, Xiaoming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21332v2.pdf)  
  Keywords: head, 3d gaussian, ar, gaussian splatting, motion, few-shot, face, lighting, nerf  
- **[TRGS-SLAM: IMU-Aided Gaussian Splatting SLAM for Blurry, Rolling Shutter, and Noisy Thermal Images](https://arxiv.org/abs/2603.20443v1)**  
  Authors: Spencer Carmichael, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20443v1.pdf)  
  Keywords: dynamic, 3d gaussian, robotics, localization, illumination, fast, ar, gaussian splatting, tracking, mapping, motion, slam  
- **[HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks](https://arxiv.org/abs/2603.19822v1)**  
  Authors: Jingyu Guo, Ziye Chen, Ziwen Li, Zhengqing Gao, Jiaxin Huang, Hanlue Zhang, Fengming Huang, Yu Yao, Tongliang Liu, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19822v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, gaussian splatting, geometry, lighting  
- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: 3d gaussian, segmentation, understanding, semantic, ar, gaussian splatting, face, lighting, mapping, slam  

### SLAM

*Showing the latest 50 out of 75 papers*

- **[GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport](https://arxiv.org/abs/2603.26181v1)**  
  Authors: Youngju Na, Jaeseong Yun, Soohyun Ryu, Hyunsu Kim, Sung-Eui Yoon, Suyong Yeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26181v1.pdf)  
  Keywords: 3d gaussian, localization, relighting, ar, gaussian splatting, face, geometry, lighting  
- **[R-PGA: Robust Physical Adversarial Camouflage Generation via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2603.26067v1)**  
  Authors: Tianrui Lou, Siyuan Liang, Jiawei Liang, Yuze Gao, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26067v1.pdf)  
  Keywords: relightable, dynamic, 3d gaussian, autonomous driving, illumination, ar, gaussian splatting, lighting, mapping  
- **[arg-VU: Affordance Reasoning with Physics-Aware 3D Geometry for Visual Understanding in Robotic Surgery](https://arxiv.org/abs/2603.26814v1)**  
  Authors: Nan Xiao, Yunxin Fan, Farong Wang, Fei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26814v1.pdf)  
  Keywords: dynamic, 3d gaussian, robotics, understanding, ar, gaussian splatting, deformation, face, tracking, geometry, motion  
- **[Unblur-SLAM: Dense Neural SLAM for Blurry Inputs](https://arxiv.org/abs/2603.26810v1)**  
  Authors: Qi Zhang, Denis Rozumny, Francesco Girlanda, Sezer Karaoglu, Marc Pollefeys, Theo Gevers, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26810v1.pdf)  
  Keywords: 3d reconstruction, ar, mapping, tracking, geometry, motion, slam  
- **[SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision](https://arxiv.org/abs/2603.24036v1)**  
  Authors: Avigail Cohen Rimon, Amir Mann, Mirela Ben Chen, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24036v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, tracking, compact, deformation  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: relightable, 3d gaussian, reflection, ar, gaussian splatting, ray tracing, shadow, mapping  
- **[Instrument-Splatting++: Towards Controllable Surgical Instrument Digital Twin Using Gaussian Splatting](https://arxiv.org/abs/2603.22792v2)**  
  Authors: Shuojue Yang, Zijian Wu, Chengjiaao Liao, Qian Li, Daiyun Shen, Chang Han Low, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22792v2.pdf)  
  Keywords: 3d gaussian, semantic, ar, gaussian splatting, tracking, geometry  
- **[FreeArtGS: Articulated Gaussian Splatting Under Free-moving Scenario](https://arxiv.org/abs/2603.22102v1)**  
  Authors: Hang Dai, Hongwei Fan, Han Zhang, Duojin Wu, Jiyao Zhang, Hao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22102v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://freeartgs.github.io)  
  Keywords: robotics, segmentation, ar, gaussian splatting, tracking, geometry, motion  
- **[SGAD-SLAM: Splatting Gaussians at Adjusted Depth for Better Radiance Fields in RGBD SLAM](https://arxiv.org/abs/2603.21055v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21055v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/SGAD-SLAM-Project)  
  Keywords: 3d gaussian, ar, gaussian splatting, tracking, mapping, slam  
- **[Glove2Hand: Synthesizing Natural Hand-Object Interaction from Multi-Modal Sensing Gloves](https://arxiv.org/abs/2603.20850v1)**  
  Authors: Xinyu Zhang, Ziyi Kou, Chuan Qin, Mia Huang, Ergys Ristani, Ankit Kumar, Lele Chen, Kun He, Abdeslam Boularias, Li Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20850v1.pdf)  
  Keywords: dynamic, 3d gaussian, robotics, understanding, ar, deformation, tracking, vr, motion  

### Scene Understanding

*Showing the latest 50 out of 132 papers*

- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516v1)**  
  Authors: Jiahao Niu, Rongjia Zheng, Wenju Xu, WeiShi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27516v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GrumpySloths/SGS_Intrinsic.github.io?style=social)](https://github.com/GrumpySloths/SGS_Intrinsic.github.io)  
  Keywords: sparse view, 3d gaussian, sparse-view, illumination, semantic, ar, gaussian splatting, shadow, geometry  
- **[Drive-Through 3D Vehicle Exterior Reconstruction via Dynamic-Scene SfM and Distortion-Aware Gaussian Splatting](https://arxiv.org/abs/2603.26638v1)**  
  Authors: Nitin Kulkarni, Akhil Devarashetti, Charlie Cluss, Livio Forte, Philip Schneider, Chunming Qiao, Alina Vereshchaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26638v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, dynamic, high-fidelity, segmentation, semantic, ar, gaussian splatting, face, geometry, motion  
- **[Scene Grounding In the Wild](https://arxiv.org/abs/2603.26584v1)**  
  Authors: Tamir Cohen, Leo Segre, Shay Shomer-Chai, Shai Avidan, Hadar Averbuch-Elor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26584v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, semantic, ar, gaussian splatting, geometry  
- **[arg-VU: Affordance Reasoning with Physics-Aware 3D Geometry for Visual Understanding in Robotic Surgery](https://arxiv.org/abs/2603.26814v1)**  
  Authors: Nan Xiao, Yunxin Fan, Farong Wang, Fei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26814v1.pdf)  
  Keywords: dynamic, 3d gaussian, robotics, understanding, ar, gaussian splatting, deformation, face, tracking, geometry, motion  
- **[Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction](https://arxiv.org/abs/2603.22852v1)**  
  Authors: Chengxin Lv, Yihui Li, Hongyu Yang, YunHong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22852v1.pdf)  
  Keywords: efficient, 3d gaussian, autonomous driving, semantic, ar, geometry, compact  
- **[PhotoAgent: A Robotic Photographer with Spatial and Aesthetic Understanding](https://arxiv.org/abs/2603.22796v1)**  
  Authors: Lirong Che, Zhenfeng Gan, Yanbo Chen, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22796v1.pdf)  
  Keywords: 3d gaussian, understanding, reflection, semantic, ar, gaussian splatting  
- **[Instrument-Splatting++: Towards Controllable Surgical Instrument Digital Twin Using Gaussian Splatting](https://arxiv.org/abs/2603.22792v2)**  
  Authors: Shuojue Yang, Zijian Wu, Chengjiaao Liao, Qian Li, Daiyun Shen, Chang Han Low, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22792v2.pdf)  
  Keywords: 3d gaussian, semantic, ar, gaussian splatting, tracking, geometry  
- **[FreeArtGS: Articulated Gaussian Splatting Under Free-moving Scenario](https://arxiv.org/abs/2603.22102v1)**  
  Authors: Hang Dai, Hongwei Fan, Han Zhang, Duojin Wu, Jiyao Zhang, Hao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22102v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://freeartgs.github.io)  
  Keywords: robotics, segmentation, ar, gaussian splatting, tracking, geometry, motion  
- **[Training-Free Instance-Aware 3D Scene Reconstruction and Diffusion-Based View Synthesis from Sparse Images](https://arxiv.org/abs/2603.21166v1)**  
  Authors: Jiatong Xia, Lingqiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21166v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiatongxia.github.io/TID3R)  
  Keywords: efficient, high-fidelity, segmentation, understanding, ar, geometry  
- **[Glove2Hand: Synthesizing Natural Hand-Object Interaction from Multi-Modal Sensing Gloves](https://arxiv.org/abs/2603.20850v1)**  
  Authors: Xinyu Zhang, Ziyi Kou, Chuan Qin, Mia Huang, Ergys Ristani, Ankit Kumar, Lele Chen, Kun He, Abdeslam Boularias, Li Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20850v1.pdf)  
  Keywords: dynamic, 3d gaussian, robotics, understanding, ar, deformation, tracking, vr, motion  



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