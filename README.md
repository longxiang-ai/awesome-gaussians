# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-04-02 01:18:12

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
- [Acceleration](#acceleration) (120 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (500 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (156 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (203 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (33 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (207 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (18 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (219 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (132 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (24 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (75 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (77 papers) - Papers about SLAM using Gaussian Splatting
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
  Keywords: vr, survey, 3d gaussian, ar, gaussian splatting  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: mapping, survey, ray tracing, 3d gaussian, ar, gaussian splatting  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: efficient, mapping, face, tracking, survey, localization, 3d gaussian, slam, ar, motion, gaussian splatting, dynamic  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: robotics, survey, 3d gaussian, ar, gaussian splatting  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v3)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v3.pdf)  
  Keywords: efficient, survey, geometry, 3d gaussian, ar, nerf, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 120 papers*

- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394v1)**  
  Authors: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29394v1.pdf)  
  Keywords: fast, 3d reconstruction, 3d gaussian, ar, gaussian splatting, sparse-view  
- **[LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2603.28431v2)**  
  Authors: Xuan Deng, Xiandong Meng, Hengyu Man, Qiang Zhu, Tiange Zhang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28431v2.pdf)  
  Keywords: real-time rendering, compact, compression, high-fidelity, lightweight, geometry, 3d gaussian, ar, head, gaussian splatting  
- **[ObjectMorpher: 3D-Aware Image Editing via Deformable 3DGS Models](https://arxiv.org/abs/2603.28152v1)**  
  Authors: Yuhuan Xie, Aoxuan Pan, Yi-Hua Huang, Chirui Chang, Peng Dai, Xin Yu, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28152v1.pdf)  
  Keywords: fast, deformation, lighting, geometry, 3d gaussian, ar, gaussian splatting  
- **[Physically Inspired Gaussian Splatting for HDR Novel View Synthesis](https://arxiv.org/abs/2603.28020v1)**  
  Authors: Huimin Zeng, Yue Bai, Hailing Wang, Yun Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huimin-zeng.github.io/PhysHDR-GS)  
  Keywords: real-time rendering, illumination, ar, gaussian splatting, dynamic  
- **[DiffSoup: Direct Differentiable Rasterization of Triangle Soup for Extreme Radiance Field Simplification](https://arxiv.org/abs/2603.27151v1)**  
  Authors: Kenji Tojo, Bernd Bickel, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27151v1.pdf) | [![GitHub](https://img.shields.io/github/stars/kenji-tojo/diffsoup?style=social)](https://github.com/kenji-tojo/diffsoup)  
  Keywords: real-time rendering, 3d gaussian, ar, efficient, gaussian splatting  
- **[ViewSplat: View-Adaptive Dynamic Gaussian Splatting for Feed-Forward Synthesis](https://arxiv.org/abs/2603.25265v1)**  
  Authors: Moonyeon Jeong, Seunggi Min, Suhyeon Lee, Hongje Seong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25265v1.pdf)  
  Keywords: real-time rendering, fast, high-fidelity, dynamic, 3d gaussian, ar, gaussian splatting  
- **[MoRGS: Efficient Per-Gaussian Motion Reasoning for Streamable Dynamic 3D Scenes](https://arxiv.org/abs/2603.25042v1)**  
  Authors: Wonjoon Lee, Sungmin Woo, Donghyeong Kim, Jungho Lee, Sangheon Park, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25042v1.pdf)  
  Keywords: real-time rendering, efficient, fast, 4d, lightweight, 3d gaussian, ar, motion, gaussian splatting, dynamic  
- **[Confidence-Based Mesh Extraction from 3D Gaussians](https://arxiv.org/abs/2603.24725v1)**  
  Authors: Lukas Radl, Felix Windisch, Andreas Kurz, Thomas Köhler, Michael Steiner, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24725v1.pdf)  
  Keywords: efficient, fast, face, 3d gaussian, ar, gaussian splatting, dynamic  
- **[Accurate Point Measurement in 3DGS -- A New Alternative to Traditional Stereoscopic-View Based Measurements](https://arxiv.org/abs/2603.24716v1)**  
  Authors: Deyan Deng, Rongjun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24716v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/3dgs_measurement_tool?style=social)](https://github.com/GDAOSU/3dgs_measurement_tool)  
  Keywords: real-time rendering, ar, 3d gaussian, gaussian splatting  
- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686v1)**  
  Authors: Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23686v1.pdf)  
  Keywords: fast, 3d reconstruction, face, high-fidelity, 3d gaussian, ar, efficient, gaussian splatting  

### Applications

*Showing the latest 50 out of 500 papers*

- **[DLWM: Dual Latent World Models enable Holistic Gaussian-centric Pre-training in Autonomous Driving](https://arxiv.org/abs/2604.00969v1)**  
  Authors: Yiyao Zhu, Ying Xue, Haiming Zhang, Guangfeng Jiang, Wending Zhou, Xu Yan, Jiantao Gao, Yingjie Cai, Bingbing Liu, Zhen Li, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00969v1.pdf)  
  Keywords: 4d, semantic, 3d gaussian, autonomous driving, ar, motion  
- **[Autoregressive Appearance Prediction for 3D Gaussian Avatars](https://arxiv.org/abs/2604.00928v1)**  
  Authors: Michael Steiner, Zhang Chen, Alexander Richard, Vasu Agrawal, Markus Steinberger, Michael Zollhöfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00928v1.pdf)  
  Keywords: compact, high-fidelity, avatar, 3d gaussian, ar, motion, gaussian splatting, dynamic, human  
- **[Compact Keyframe-Optimized Multi-Agent Gaussian Splatting SLAM](https://arxiv.org/abs/2604.00804v1)**  
  Authors: Monica M. Q. Li, Pierre-Yves Lajoie, Jialiang Liu, Giovanni Beltrame  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00804v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lemonci/coko-slam?style=social)](https://github.com/lemonci/coko-slam)  
  Keywords: compact, mapping, lightweight, localization, 3d gaussian, slam, ar, efficient, gaussian splatting  
- **[DirectFisheye-GS: Enabling Native Fisheye Input in Gaussian Splatting with Cross-View Joint Optimization](https://arxiv.org/abs/2604.00648v1)**  
  Authors: Zhengxian Yang, Fei Xie, Xutao Xue, Rui Zhang, Taicheng Huang, Yang Liu, Mengqi Ji, Tao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00648v1.pdf)  
  Keywords: vr, high-fidelity, 3d gaussian, ar, efficient, gaussian splatting  
- **[TRiGS: Temporal Rigid-Body Motion for Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2604.00538v1)**  
  Authors: Suwoong Yeom, Joonsik Nam, Seunggyu Choi, Lucas Yunkyu Lee, Sangmin Kim, Jaesik Park, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong, Sukju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00538v1.pdf)  
  Keywords: 4d, motion, ar, body, gaussian splatting, dynamic  
- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: face, reflection, ray tracing, ar, gaussian splatting  
- **[ARGS: Auto-Regressive Gaussian Splatting via Parallel Progressive Next-Scale Prediction](https://arxiv.org/abs/2604.00494v1)**  
  Authors: Quanyuan Ruan, Kewei Shi, Jiabao Lei, Xifeng Gao, Xiaoguang Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00494v1.pdf)  
  Keywords: ar, gaussian splatting  
- **[GRVS: a Generalizable and Recurrent Approach to Monocular Dynamic View Synthesis](https://arxiv.org/abs/2603.29734v1)**  
  Authors: Thomas Tanay, Mohammed Brahimi, Michal Nazarczuk, Qingwen Zhang, Sibi Catley-Chandar, Arthur Moreau, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29734v1.pdf)  
  Keywords: efficient, 4d, mapping, ar, motion, gaussian splatting, dynamic  
- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394v1)**  
  Authors: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29394v1.pdf)  
  Keywords: fast, 3d reconstruction, 3d gaussian, ar, gaussian splatting, sparse-view  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, understanding, high-fidelity, dynamic, geometry, neural rendering, ar, shadow, large scene, motion, efficient, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 156 papers*

- **[Autoregressive Appearance Prediction for 3D Gaussian Avatars](https://arxiv.org/abs/2604.00928v1)**  
  Authors: Michael Steiner, Zhang Chen, Alexander Richard, Vasu Agrawal, Markus Steinberger, Michael Zollhöfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00928v1.pdf)  
  Keywords: compact, high-fidelity, avatar, 3d gaussian, ar, motion, gaussian splatting, dynamic, human  
- **[TRiGS: Temporal Rigid-Body Motion for Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2604.00538v1)**  
  Authors: Suwoong Yeom, Joonsik Nam, Seunggyu Choi, Lucas Yunkyu Lee, Sangmin Kim, Jaesik Park, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong, Sukju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00538v1.pdf)  
  Keywords: 4d, motion, ar, body, gaussian splatting, dynamic  
- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: face, reflection, ray tracing, ar, gaussian splatting  
- **[LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2603.28431v2)**  
  Authors: Xuan Deng, Xiandong Meng, Hengyu Man, Qiang Zhu, Tiange Zhang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28431v2.pdf)  
  Keywords: real-time rendering, compact, compression, high-fidelity, lightweight, geometry, 3d gaussian, ar, head, gaussian splatting  
- **[\textit{4DSurf}: High-Fidelity Dynamic Scene Surface Reconstruction](https://arxiv.org/abs/2603.28064v1)**  
  Authors: Renjie Wu, Hongdong Li, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28064v1.pdf)  
  Keywords: 4d, deformation, face, high-fidelity, geometry, ar, motion, gaussian splatting, dynamic, sparse-view  
- **[DipGuava: Disentangling Personalized Gaussian Features for 3D Head Avatars from Monocular Video](https://arxiv.org/abs/2603.28003v1)**  
  Authors: Jeonghaeng Lee, Seok Keun Choi, Zhixuan Li, Weisi Lin, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28003v1.pdf)  
  Keywords: deformation, semantic, geometry, avatar, 3d gaussian, ar, head, dynamic  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: mapping, face, semantic, ray tracing, localization, 3d gaussian, slam, ar, tracking, efficient, gaussian splatting  
- **[Drive-Through 3D Vehicle Exterior Reconstruction via Dynamic-Scene SfM and Distortion-Aware Gaussian Splatting](https://arxiv.org/abs/2603.26638v1)**  
  Authors: Nitin Kulkarni, Akhil Devarashetti, Charlie Cluss, Livio Forte, Philip Schneider, Chunming Qiao, Alina Vereshchaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26638v1.pdf)  
  Keywords: 3d reconstruction, face, segmentation, high-fidelity, dynamic, semantic, geometry, 3d gaussian, ar, motion, gaussian splatting  
- **[GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport](https://arxiv.org/abs/2603.26181v1)**  
  Authors: Youngju Na, Jaeseong Yun, Soohyun Ryu, Hyunsu Kim, Sung-Eui Yoon, Suyong Yeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26181v1.pdf)  
  Keywords: face, lighting, localization, geometry, 3d gaussian, ar, gaussian splatting, relighting  
- **[arg-VU: Affordance Reasoning with Physics-Aware 3D Geometry for Visual Understanding in Robotic Surgery](https://arxiv.org/abs/2603.26814v1)**  
  Authors: Nan Xiao, Yunxin Fan, Farong Wang, Fei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26814v1.pdf)  
  Keywords: deformation, understanding, robotics, face, tracking, geometry, 3d gaussian, ar, motion, gaussian splatting, dynamic  

### Dynamic Scene

*Showing the latest 50 out of 203 papers*

- **[DLWM: Dual Latent World Models enable Holistic Gaussian-centric Pre-training in Autonomous Driving](https://arxiv.org/abs/2604.00969v1)**  
  Authors: Yiyao Zhu, Ying Xue, Haiming Zhang, Guangfeng Jiang, Wending Zhou, Xu Yan, Jiantao Gao, Yingjie Cai, Bingbing Liu, Zhen Li, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00969v1.pdf)  
  Keywords: 4d, semantic, 3d gaussian, autonomous driving, ar, motion  
- **[Autoregressive Appearance Prediction for 3D Gaussian Avatars](https://arxiv.org/abs/2604.00928v1)**  
  Authors: Michael Steiner, Zhang Chen, Alexander Richard, Vasu Agrawal, Markus Steinberger, Michael Zollhöfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00928v1.pdf)  
  Keywords: compact, high-fidelity, avatar, 3d gaussian, ar, motion, gaussian splatting, dynamic, human  
- **[TRiGS: Temporal Rigid-Body Motion for Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2604.00538v1)**  
  Authors: Suwoong Yeom, Joonsik Nam, Seunggyu Choi, Lucas Yunkyu Lee, Sangmin Kim, Jaesik Park, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong, Sukju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00538v1.pdf)  
  Keywords: 4d, motion, ar, body, gaussian splatting, dynamic  
- **[GRVS: a Generalizable and Recurrent Approach to Monocular Dynamic View Synthesis](https://arxiv.org/abs/2603.29734v1)**  
  Authors: Thomas Tanay, Mohammed Brahimi, Michal Nazarczuk, Qingwen Zhang, Sibi Catley-Chandar, Arthur Moreau, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29734v1.pdf)  
  Keywords: efficient, 4d, mapping, ar, motion, gaussian splatting, dynamic  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, understanding, high-fidelity, dynamic, geometry, neural rendering, ar, shadow, large scene, motion, efficient, gaussian splatting  
- **[ObjectMorpher: 3D-Aware Image Editing via Deformable 3DGS Models](https://arxiv.org/abs/2603.28152v1)**  
  Authors: Yuhuan Xie, Aoxuan Pan, Yi-Hua Huang, Chirui Chang, Peng Dai, Xin Yu, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28152v1.pdf)  
  Keywords: fast, deformation, lighting, geometry, 3d gaussian, ar, gaussian splatting  
- **[\textit{4DSurf}: High-Fidelity Dynamic Scene Surface Reconstruction](https://arxiv.org/abs/2603.28064v1)**  
  Authors: Renjie Wu, Hongdong Li, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28064v1.pdf)  
  Keywords: 4d, deformation, face, high-fidelity, geometry, ar, motion, gaussian splatting, dynamic, sparse-view  
- **[Physically Inspired Gaussian Splatting for HDR Novel View Synthesis](https://arxiv.org/abs/2603.28020v1)**  
  Authors: Huimin Zeng, Yue Bai, Hailing Wang, Yun Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huimin-zeng.github.io/PhysHDR-GS)  
  Keywords: real-time rendering, illumination, ar, gaussian splatting, dynamic  
- **[DipGuava: Disentangling Personalized Gaussian Features for 3D Head Avatars from Monocular Video](https://arxiv.org/abs/2603.28003v1)**  
  Authors: Jeonghaeng Lee, Seok Keun Choi, Zhixuan Li, Weisi Lin, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28003v1.pdf)  
  Keywords: deformation, semantic, geometry, avatar, 3d gaussian, ar, head, dynamic  
- **[NimbusGS: Unified 3D Scene Reconstruction under Hybrid Weather](https://arxiv.org/abs/2603.27228v1)**  
  Authors: Yanying Li, Jinyang Li, Shengfeng He, Yangyang Xu, Junyu Dong, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27228v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lyy-ovo/NimbusGS?style=social)](https://github.com/lyy-ovo/NimbusGS)  
  Keywords: geometry, ar, 3d gaussian, dynamic  

### Few-shot

- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394v1)**  
  Authors: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29394v1.pdf)  
  Keywords: fast, 3d reconstruction, 3d gaussian, ar, gaussian splatting, sparse-view  
- **[\textit{4DSurf}: High-Fidelity Dynamic Scene Surface Reconstruction](https://arxiv.org/abs/2603.28064v1)**  
  Authors: Renjie Wu, Hongdong Li, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28064v1.pdf)  
  Keywords: 4d, deformation, face, high-fidelity, geometry, ar, motion, gaussian splatting, dynamic, sparse-view  
- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516v2)**  
  Authors: Jiahao Niu, Rongjia Zheng, Wenju Xu, Wei-Shi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27516v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GrumpySloths/SGS_Intrinsic.github.io?style=social)](https://github.com/GrumpySloths/SGS_Intrinsic.github.io)  
  Keywords: semantic, sparse-view, illumination, geometry, 3d gaussian, ar, shadow, gaussian splatting, sparse view  
- **[Detailed Geometry and Appearance from Opportunistic Motion](https://arxiv.org/abs/2603.26665v1)**  
  Authors: Ryosuke Hirai, Kohei Yamashita, Antoine Guédon, Ryo Kawahara, Vincent Lepetit, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26665v1.pdf)  
  Keywords: illumination, geometry, ar, motion, gaussian splatting, sparse view  
- **[AirSplat: Alignment and Rating for Robust Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2603.25129v1)**  
  Authors: Minh-Quan Viet Bui, Jaeho Moon, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25129v1.pdf)  
  Keywords: high-fidelity, geometry, 3d gaussian, ar, gaussian splatting, sparse-view  
- **[EmoTaG: Emotion-Aware Talking Head Synthesis on Gaussian Splatting with Few-Shot Personalization](https://arxiv.org/abs/2603.21332v2)**  
  Authors: Haolan Xu, Keli Cheng, Lei Wang, Ning Bi, Xiaoming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21332v2.pdf)  
  Keywords: few-shot, face, lighting, 3d gaussian, ar, motion, head, nerf, gaussian splatting  
- **[UniSem: Generalizable Semantic 3D Reconstruction from Sparse Unposed Images](https://arxiv.org/abs/2603.17519v1)**  
  Authors: Guibiao Liao, Qian Ren, Kaimin Liao, Hua Wang, Zhi Chen, Luchao Wang, Yaohua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17519v1.pdf)  
  Keywords: 3d reconstruction, segmentation, semantic, geometry, 3d gaussian, ar, gaussian splatting, sparse-view  
- **[S2D: Sparse to Dense Lifting for 3D Reconstruction with Minimal Inputs](https://arxiv.org/abs/2603.10893v1)**  
  Authors: Yuzhou Ji, Qijian Tian, He Zhu, Xiaoqi Jiang, Guangzhi Cao, Lizhuang Ma, Yuan Xie, Xin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10893v1.pdf)  
  Keywords: 3d reconstruction, understanding, high-fidelity, 3d gaussian, ar, efficient, gaussian splatting, sparse view  
- **[Active View Selection with Perturbed Gaussian Ensemble for Tomographic Reconstruction](https://arxiv.org/abs/2603.06852v1)**  
  Authors: Yulun Wu, Ruyi Zha, Wei Cao, Yingying Li, Yuanhao Cai, Yaoyao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06852v1.pdf)  
  Keywords: fast, 3d gaussian, ar, gaussian splatting, sparse-view  
- **[CylinderSplat: 3D Gaussian Splatting with Cylindrical Triplanes for Panoramic Novel View Synthesis](https://arxiv.org/abs/2603.05882v1)**  
  Authors: Qiwei Wang, Xianghui Ze, Jingyi Yu, Yujiao Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05882v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, gaussian splatting, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 207 papers*

- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394v1)**  
  Authors: Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29394v1.pdf)  
  Keywords: fast, 3d reconstruction, 3d gaussian, ar, gaussian splatting, sparse-view  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, understanding, high-fidelity, dynamic, geometry, neural rendering, ar, shadow, large scene, motion, efficient, gaussian splatting  
- **[LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting](https://arxiv.org/abs/2603.29209v1)**  
  Authors: Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29209v1.pdf)  
  Keywords: vr, high-fidelity, lighting, illumination, geometry, 3d gaussian, ar, shadow, efficient, gaussian splatting  
- **[LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2603.28431v2)**  
  Authors: Xuan Deng, Xiandong Meng, Hengyu Man, Qiang Zhu, Tiange Zhang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28431v2.pdf)  
  Keywords: real-time rendering, compact, compression, high-fidelity, lightweight, geometry, 3d gaussian, ar, head, gaussian splatting  
- **[ObjectMorpher: 3D-Aware Image Editing via Deformable 3DGS Models](https://arxiv.org/abs/2603.28152v1)**  
  Authors: Yuhuan Xie, Aoxuan Pan, Yi-Hua Huang, Chirui Chang, Peng Dai, Xin Yu, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28152v1.pdf)  
  Keywords: fast, deformation, lighting, geometry, 3d gaussian, ar, gaussian splatting  
- **[\textit{4DSurf}: High-Fidelity Dynamic Scene Surface Reconstruction](https://arxiv.org/abs/2603.28064v1)**  
  Authors: Renjie Wu, Hongdong Li, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28064v1.pdf)  
  Keywords: 4d, deformation, face, high-fidelity, geometry, ar, motion, gaussian splatting, dynamic, sparse-view  
- **[DipGuava: Disentangling Personalized Gaussian Features for 3D Head Avatars from Monocular Video](https://arxiv.org/abs/2603.28003v1)**  
  Authors: Jeonghaeng Lee, Seok Keun Choi, Zhixuan Li, Weisi Lin, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28003v1.pdf)  
  Keywords: deformation, semantic, geometry, avatar, 3d gaussian, ar, head, dynamic  
- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516v2)**  
  Authors: Jiahao Niu, Rongjia Zheng, Wenju Xu, Wei-Shi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27516v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GrumpySloths/SGS_Intrinsic.github.io?style=social)](https://github.com/GrumpySloths/SGS_Intrinsic.github.io)  
  Keywords: semantic, sparse-view, illumination, geometry, 3d gaussian, ar, shadow, gaussian splatting, sparse view  
- **[From None to All: Self-Supervised 3D Reconstruction via Novel View Synthesis](https://arxiv.org/abs/2603.27455v1)**  
  Authors: Ranran Huang, Weixun Luo, Ye Mao, Krystian Mikolajczyk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27455v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ranrhuang.github.io/nas3r)  
  Keywords: geometry, 3d gaussian, ar, 3d reconstruction  
- **[NimbusGS: Unified 3D Scene Reconstruction under Hybrid Weather](https://arxiv.org/abs/2603.27228v1)**  
  Authors: Yanying Li, Jinyang Li, Shengfeng He, Yangyang Xu, Junyu Dong, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27228v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lyy-ovo/NimbusGS?style=social)](https://github.com/lyy-ovo/NimbusGS)  
  Keywords: geometry, ar, 3d gaussian, dynamic  

### Large Scene

- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, understanding, high-fidelity, dynamic, geometry, neural rendering, ar, shadow, large scene, motion, efficient, gaussian splatting  
- **[Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting](https://arxiv.org/abs/2603.29185v1)**  
  Authors: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29185v1.pdf)  
  Keywords: localization, outdoor, ar, efficient, gaussian splatting  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: face, neural rendering, 3d gaussian, ar, large scene, head, efficient, gaussian splatting  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: outdoor, slam, gaussian splatting, ar, tracking, head, efficient, dynamic  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: localization, geometry, outdoor, 3d gaussian, ar, gaussian splatting  
- **[EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.06216v1)**  
  Authors: Miriam Jäger, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06216v1.pdf)  
  Keywords: urban scene, 3d reconstruction, face, geometry, 3d gaussian, ar, gaussian splatting  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: fast, 3d reconstruction, relightable, relighting, reflection, lighting, outdoor, illumination, 3d gaussian, ar, nerf, gaussian splatting  
- **[Interactive Augmented Reality-enabled Outdoor Scene Visualization For Enhanced Real-time Disaster Response](https://arxiv.org/abs/2602.21874v1)**  
  Authors: Dimitrios Apostolakis, Georgios Angelidis, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21874v1.pdf)  
  Keywords: fast, face, lighting, lightweight, semantic, outdoor, 3d gaussian, ar, gaussian splatting  
- **[Large-scale Photorealistic Outdoor 3D Scene Reconstruction from UAV Imagery Using Gaussian Splatting Techniques](https://arxiv.org/abs/2602.20342v1)**  
  Authors: Christos Maikos, Georgios Angelidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20342v1.pdf)  
  Keywords: efficient, 3d reconstruction, vr, high-fidelity, outdoor, neural rendering, 3d gaussian, ar, nerf, gaussian splatting  
- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: mapping, lighting, semantic, outdoor, geometry, localization, 3d gaussian, ar, head, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 219 papers*

- **[Autoregressive Appearance Prediction for 3D Gaussian Avatars](https://arxiv.org/abs/2604.00928v1)**  
  Authors: Michael Steiner, Zhang Chen, Alexander Richard, Vasu Agrawal, Markus Steinberger, Michael Zollhöfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00928v1.pdf)  
  Keywords: compact, high-fidelity, avatar, 3d gaussian, ar, motion, gaussian splatting, dynamic, human  
- **[Compact Keyframe-Optimized Multi-Agent Gaussian Splatting SLAM](https://arxiv.org/abs/2604.00804v1)**  
  Authors: Monica M. Q. Li, Pierre-Yves Lajoie, Jialiang Liu, Giovanni Beltrame  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00804v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lemonci/coko-slam?style=social)](https://github.com/lemonci/coko-slam)  
  Keywords: compact, mapping, lightweight, localization, 3d gaussian, slam, ar, efficient, gaussian splatting  
- **[DirectFisheye-GS: Enabling Native Fisheye Input in Gaussian Splatting with Cross-View Joint Optimization](https://arxiv.org/abs/2604.00648v1)**  
  Authors: Zhengxian Yang, Fei Xie, Xutao Xue, Rui Zhang, Taicheng Huang, Yang Liu, Mengqi Ji, Tao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00648v1.pdf)  
  Keywords: vr, high-fidelity, 3d gaussian, ar, efficient, gaussian splatting  
- **[GRVS: a Generalizable and Recurrent Approach to Monocular Dynamic View Synthesis](https://arxiv.org/abs/2603.29734v1)**  
  Authors: Thomas Tanay, Mohammed Brahimi, Michal Nazarczuk, Qingwen Zhang, Sibi Catley-Chandar, Arthur Moreau, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29734v1.pdf)  
  Keywords: efficient, 4d, mapping, ar, motion, gaussian splatting, dynamic  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, understanding, high-fidelity, dynamic, geometry, neural rendering, ar, shadow, large scene, motion, efficient, gaussian splatting  
- **[LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting](https://arxiv.org/abs/2603.29209v1)**  
  Authors: Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29209v1.pdf)  
  Keywords: vr, high-fidelity, lighting, illumination, geometry, 3d gaussian, ar, shadow, efficient, gaussian splatting  
- **[Efficient Camera Pose Augmentation for View Generalization in Robotic Policy Learning](https://arxiv.org/abs/2603.29192v1)**  
  Authors: Sen Wang, Huaiyi Dong, Jingyi Tian, Jiayi Li, Zhuo Yang, Tongtong Cao, Anlin Chen, Shuang Wu, Le Wang, Sanping Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29192v1.pdf)  
  Keywords: mapping, high-fidelity, 3d gaussian, ar, efficient, gaussian splatting  
- **[Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting](https://arxiv.org/abs/2603.29185v1)**  
  Authors: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29185v1.pdf)  
  Keywords: localization, outdoor, ar, efficient, gaussian splatting  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: reflection, 3d gaussian, ar, ray casting, efficient  
- **[Gleanmer: A 6 mW SoC for Real-Time 3D Gaussian Occupancy Mapping](https://arxiv.org/abs/2603.29005v1)**  
  Authors: Zih-Sing Fu, Peter Zhi Xuan Li, Sertac Karaman, Vivienne Sze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29005v1.pdf)  
  Keywords: compact, mapping, vr, high-fidelity, 3d gaussian, ar, efficient  

### Quality Enhancement

*Showing the latest 50 out of 132 papers*

- **[Autoregressive Appearance Prediction for 3D Gaussian Avatars](https://arxiv.org/abs/2604.00928v1)**  
  Authors: Michael Steiner, Zhang Chen, Alexander Richard, Vasu Agrawal, Markus Steinberger, Michael Zollhöfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00928v1.pdf)  
  Keywords: compact, high-fidelity, avatar, 3d gaussian, ar, motion, gaussian splatting, dynamic, human  
- **[DirectFisheye-GS: Enabling Native Fisheye Input in Gaussian Splatting with Cross-View Joint Optimization](https://arxiv.org/abs/2604.00648v1)**  
  Authors: Zhengxian Yang, Fei Xie, Xutao Xue, Rui Zhang, Taicheng Huang, Yang Liu, Mengqi Ji, Tao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00648v1.pdf)  
  Keywords: vr, high-fidelity, 3d gaussian, ar, efficient, gaussian splatting  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, understanding, high-fidelity, dynamic, geometry, neural rendering, ar, shadow, large scene, motion, efficient, gaussian splatting  
- **[LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting](https://arxiv.org/abs/2603.29209v1)**  
  Authors: Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29209v1.pdf)  
  Keywords: vr, high-fidelity, lighting, illumination, geometry, 3d gaussian, ar, shadow, efficient, gaussian splatting  
- **[Efficient Camera Pose Augmentation for View Generalization in Robotic Policy Learning](https://arxiv.org/abs/2603.29192v1)**  
  Authors: Sen Wang, Huaiyi Dong, Jingyi Tian, Jiayi Li, Zhuo Yang, Tongtong Cao, Anlin Chen, Shuang Wu, Le Wang, Sanping Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29192v1.pdf)  
  Keywords: mapping, high-fidelity, 3d gaussian, ar, efficient, gaussian splatting  
- **[Gleanmer: A 6 mW SoC for Real-Time 3D Gaussian Occupancy Mapping](https://arxiv.org/abs/2603.29005v1)**  
  Authors: Zih-Sing Fu, Peter Zhi Xuan Li, Sertac Karaman, Vivienne Sze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29005v1.pdf)  
  Keywords: compact, mapping, vr, high-fidelity, 3d gaussian, ar, efficient  
- **[LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2603.28431v2)**  
  Authors: Xuan Deng, Xiandong Meng, Hengyu Man, Qiang Zhu, Tiange Zhang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28431v2.pdf)  
  Keywords: real-time rendering, compact, compression, high-fidelity, lightweight, geometry, 3d gaussian, ar, head, gaussian splatting  
- **[\textit{4DSurf}: High-Fidelity Dynamic Scene Surface Reconstruction](https://arxiv.org/abs/2603.28064v1)**  
  Authors: Renjie Wu, Hongdong Li, Jose M. Alvarez, Miaomiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28064v1.pdf)  
  Keywords: 4d, deformation, face, high-fidelity, geometry, ar, motion, gaussian splatting, dynamic, sparse-view  
- **[Drive-Through 3D Vehicle Exterior Reconstruction via Dynamic-Scene SfM and Distortion-Aware Gaussian Splatting](https://arxiv.org/abs/2603.26638v1)**  
  Authors: Nitin Kulkarni, Akhil Devarashetti, Charlie Cluss, Livio Forte, Philip Schneider, Chunming Qiao, Alina Vereshchaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26638v1.pdf)  
  Keywords: 3d reconstruction, face, segmentation, high-fidelity, dynamic, semantic, geometry, 3d gaussian, ar, motion, gaussian splatting  
- **[Less Gaussians, Texture More: 4K Feed-Forward Textured Splatting](https://arxiv.org/abs/2603.25745v1)**  
  Authors: Yixing Lao, Xuyang Bai, Xiaoyang Wu, Nuoyuan Yan, Zixin Luo, Tian Fang, Jean-Daniel Nahmias, Yanghai Tsin, Shiwei Li, Hengshuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25745v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yxlao.github.io/lgtm)  
  Keywords: compact, high-fidelity, 3d gaussian, ar, gaussian splatting  

### Ray Tracing

- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: face, reflection, ray tracing, ar, gaussian splatting  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: reflection, 3d gaussian, ar, ray casting, efficient  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: mapping, face, semantic, ray tracing, localization, 3d gaussian, slam, ar, tracking, efficient, gaussian splatting  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: mapping, relightable, reflection, ray tracing, 3d gaussian, ar, shadow, gaussian splatting  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: real-time rendering, face, geometry, 3d gaussian, ar, path tracing  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: real-time rendering, efficient, fast, face, high-fidelity, ray tracing, geometry, 3d gaussian, ar, nerf, gaussian splatting  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: mapping, survey, ray tracing, 3d gaussian, ar, gaussian splatting  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: real-time rendering, ray marching, high-fidelity, 3d gaussian, ar, efficient, gaussian splatting  
- **[Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction](https://arxiv.org/abs/2603.08503v1)**  
  Authors: Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08503v1.pdf) | [![GitHub](https://img.shields.io/github/stars/1170632760/Spherical-GOF?style=social)](https://github.com/1170632760/Spherical-GOF)  
  Keywords: fast, robotics, geometry, 3d gaussian, ar, ray casting, efficient, gaussian splatting  
- **[Ref-DGS: Reflective Dual Gaussian Splatting](https://arxiv.org/abs/2603.07664v2)**  
  Authors: Ningjing Fan, Yiqun Wang, Dongming Yan, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07664v2.pdf)  
  Keywords: fast, face, reflection, lightweight, ray tracing, geometry, ar, efficient, gaussian splatting  

### Relighting

*Showing the latest 50 out of 75 papers*

- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: face, reflection, ray tracing, ar, gaussian splatting  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, understanding, high-fidelity, dynamic, geometry, neural rendering, ar, shadow, large scene, motion, efficient, gaussian splatting  
- **[LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting](https://arxiv.org/abs/2603.29209v1)**  
  Authors: Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29209v1.pdf)  
  Keywords: vr, high-fidelity, lighting, illumination, geometry, 3d gaussian, ar, shadow, efficient, gaussian splatting  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: reflection, 3d gaussian, ar, ray casting, efficient  
- **[ObjectMorpher: 3D-Aware Image Editing via Deformable 3DGS Models](https://arxiv.org/abs/2603.28152v1)**  
  Authors: Yuhuan Xie, Aoxuan Pan, Yi-Hua Huang, Chirui Chang, Peng Dai, Xin Yu, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28152v1.pdf)  
  Keywords: fast, deformation, lighting, geometry, 3d gaussian, ar, gaussian splatting  
- **[Physically Inspired Gaussian Splatting for HDR Novel View Synthesis](https://arxiv.org/abs/2603.28020v1)**  
  Authors: Huimin Zeng, Yue Bai, Hailing Wang, Yun Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28020v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huimin-zeng.github.io/PhysHDR-GS)  
  Keywords: real-time rendering, illumination, ar, gaussian splatting, dynamic  
- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516v2)**  
  Authors: Jiahao Niu, Rongjia Zheng, Wenju Xu, Wei-Shi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27516v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GrumpySloths/SGS_Intrinsic.github.io?style=social)](https://github.com/GrumpySloths/SGS_Intrinsic.github.io)  
  Keywords: semantic, sparse-view, illumination, geometry, 3d gaussian, ar, shadow, gaussian splatting, sparse view  
- **[Detailed Geometry and Appearance from Opportunistic Motion](https://arxiv.org/abs/2603.26665v1)**  
  Authors: Ryosuke Hirai, Kohei Yamashita, Antoine Guédon, Ryo Kawahara, Vincent Lepetit, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26665v1.pdf)  
  Keywords: illumination, geometry, ar, motion, gaussian splatting, sparse view  
- **[GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport](https://arxiv.org/abs/2603.26181v1)**  
  Authors: Youngju Na, Jaeseong Yun, Soohyun Ryu, Hyunsu Kim, Sung-Eui Yoon, Suyong Yeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26181v1.pdf)  
  Keywords: face, lighting, localization, geometry, 3d gaussian, ar, gaussian splatting, relighting  
- **[R-PGA: Robust Physical Adversarial Camouflage Generation via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2603.26067v1)**  
  Authors: Tianrui Lou, Siyuan Liang, Jiawei Liang, Yuze Gao, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26067v1.pdf)  
  Keywords: mapping, relightable, lighting, dynamic, illumination, 3d gaussian, autonomous driving, ar, gaussian splatting  

### SLAM

*Showing the latest 50 out of 77 papers*

- **[Compact Keyframe-Optimized Multi-Agent Gaussian Splatting SLAM](https://arxiv.org/abs/2604.00804v1)**  
  Authors: Monica M. Q. Li, Pierre-Yves Lajoie, Jialiang Liu, Giovanni Beltrame  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00804v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lemonci/coko-slam?style=social)](https://github.com/lemonci/coko-slam)  
  Keywords: compact, mapping, lightweight, localization, 3d gaussian, slam, ar, efficient, gaussian splatting  
- **[GRVS: a Generalizable and Recurrent Approach to Monocular Dynamic View Synthesis](https://arxiv.org/abs/2603.29734v1)**  
  Authors: Thomas Tanay, Mohammed Brahimi, Michal Nazarczuk, Qingwen Zhang, Sibi Catley-Chandar, Arthur Moreau, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29734v1.pdf)  
  Keywords: efficient, 4d, mapping, ar, motion, gaussian splatting, dynamic  
- **[Efficient Camera Pose Augmentation for View Generalization in Robotic Policy Learning](https://arxiv.org/abs/2603.29192v1)**  
  Authors: Sen Wang, Huaiyi Dong, Jingyi Tian, Jiayi Li, Zhuo Yang, Tongtong Cao, Anlin Chen, Shuang Wu, Le Wang, Sanping Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29192v1.pdf)  
  Keywords: mapping, high-fidelity, 3d gaussian, ar, efficient, gaussian splatting  
- **[Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting](https://arxiv.org/abs/2603.29185v1)**  
  Authors: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29185v1.pdf)  
  Keywords: localization, outdoor, ar, efficient, gaussian splatting  
- **[Gleanmer: A 6 mW SoC for Real-Time 3D Gaussian Occupancy Mapping](https://arxiv.org/abs/2603.29005v1)**  
  Authors: Zih-Sing Fu, Peter Zhi Xuan Li, Sertac Karaman, Vivienne Sze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29005v1.pdf)  
  Keywords: compact, mapping, vr, high-fidelity, 3d gaussian, ar, efficient  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: mapping, face, semantic, ray tracing, localization, 3d gaussian, slam, ar, tracking, efficient, gaussian splatting  
- **[GLINT: Modeling Scene-Scale Transparency via Gaussian Radiance Transport](https://arxiv.org/abs/2603.26181v1)**  
  Authors: Youngju Na, Jaeseong Yun, Soohyun Ryu, Hyunsu Kim, Sung-Eui Yoon, Suyong Yeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26181v1.pdf)  
  Keywords: face, lighting, localization, geometry, 3d gaussian, ar, gaussian splatting, relighting  
- **[R-PGA: Robust Physical Adversarial Camouflage Generation via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2603.26067v1)**  
  Authors: Tianrui Lou, Siyuan Liang, Jiawei Liang, Yuze Gao, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26067v1.pdf)  
  Keywords: mapping, relightable, lighting, dynamic, illumination, 3d gaussian, autonomous driving, ar, gaussian splatting  
- **[arg-VU: Affordance Reasoning with Physics-Aware 3D Geometry for Visual Understanding in Robotic Surgery](https://arxiv.org/abs/2603.26814v1)**  
  Authors: Nan Xiao, Yunxin Fan, Farong Wang, Fei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26814v1.pdf)  
  Keywords: deformation, understanding, robotics, face, tracking, geometry, 3d gaussian, ar, motion, gaussian splatting, dynamic  
- **[Unblur-SLAM: Dense Neural SLAM for Blurry Inputs](https://arxiv.org/abs/2603.26810v1)**  
  Authors: Qi Zhang, Denis Rozumny, Francesco Girlanda, Sezer Karaoglu, Marc Pollefeys, Theo Gevers, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26810v1.pdf)  
  Keywords: 3d reconstruction, mapping, motion, geometry, slam, ar, tracking  

### Scene Understanding

*Showing the latest 50 out of 131 papers*

- **[DLWM: Dual Latent World Models enable Holistic Gaussian-centric Pre-training in Autonomous Driving](https://arxiv.org/abs/2604.00969v1)**  
  Authors: Yiyao Zhu, Ying Xue, Haiming Zhang, Guangfeng Jiang, Wending Zhou, Xu Yan, Jiantao Gao, Yingjie Cai, Bingbing Liu, Zhen Li, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00969v1.pdf)  
  Keywords: 4d, semantic, 3d gaussian, autonomous driving, ar, motion  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: 4d, understanding, high-fidelity, dynamic, geometry, neural rendering, ar, shadow, large scene, motion, efficient, gaussian splatting  
- **[DipGuava: Disentangling Personalized Gaussian Features for 3D Head Avatars from Monocular Video](https://arxiv.org/abs/2603.28003v1)**  
  Authors: Jeonghaeng Lee, Seok Keun Choi, Zhixuan Li, Weisi Lin, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28003v1.pdf)  
  Keywords: deformation, semantic, geometry, avatar, 3d gaussian, ar, head, dynamic  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: mapping, face, semantic, ray tracing, localization, 3d gaussian, slam, ar, tracking, efficient, gaussian splatting  
- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516v2)**  
  Authors: Jiahao Niu, Rongjia Zheng, Wenju Xu, Wei-Shi Zheng, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27516v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GrumpySloths/SGS_Intrinsic.github.io?style=social)](https://github.com/GrumpySloths/SGS_Intrinsic.github.io)  
  Keywords: semantic, sparse-view, illumination, geometry, 3d gaussian, ar, shadow, gaussian splatting, sparse view  
- **[Drive-Through 3D Vehicle Exterior Reconstruction via Dynamic-Scene SfM and Distortion-Aware Gaussian Splatting](https://arxiv.org/abs/2603.26638v1)**  
  Authors: Nitin Kulkarni, Akhil Devarashetti, Charlie Cluss, Livio Forte, Philip Schneider, Chunming Qiao, Alina Vereshchaka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26638v1.pdf)  
  Keywords: 3d reconstruction, face, segmentation, high-fidelity, dynamic, semantic, geometry, 3d gaussian, ar, motion, gaussian splatting  
- **[Scene Grounding In the Wild](https://arxiv.org/abs/2603.26584v1)**  
  Authors: Tamir Cohen, Leo Segre, Shay Shomer-Chai, Shai Avidan, Hadar Averbuch-Elor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26584v1.pdf)  
  Keywords: 3d reconstruction, semantic, geometry, 3d gaussian, ar, gaussian splatting  
- **[arg-VU: Affordance Reasoning with Physics-Aware 3D Geometry for Visual Understanding in Robotic Surgery](https://arxiv.org/abs/2603.26814v1)**  
  Authors: Nan Xiao, Yunxin Fan, Farong Wang, Fei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26814v1.pdf)  
  Keywords: deformation, understanding, robotics, face, tracking, geometry, 3d gaussian, ar, motion, gaussian splatting, dynamic  
- **[Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction](https://arxiv.org/abs/2603.22852v1)**  
  Authors: Chengxin Lv, Yihui Li, Hongyu Yang, YunHong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22852v1.pdf)  
  Keywords: compact, semantic, geometry, 3d gaussian, autonomous driving, ar, efficient  
- **[PhotoAgent: A Robotic Photographer with Spatial and Aesthetic Understanding](https://arxiv.org/abs/2603.22796v1)**  
  Authors: Lirong Che, Zhenfeng Gan, Yanbo Chen, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22796v1.pdf)  
  Keywords: understanding, reflection, semantic, 3d gaussian, ar, gaussian splatting  



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