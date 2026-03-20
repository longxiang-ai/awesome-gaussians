# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-03-20 01:11:30

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
- [Acceleration](#acceleration) (115 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (499 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (168 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (207 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (32 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (202 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (16 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (212 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (131 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (19 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (71 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (78 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (133 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v1)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v1.pdf)  
  Keywords: ar, 3d gaussian, mapping, ray tracing, gaussian splatting, survey  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: slam, ar, face, 3d gaussian, tracking, localization, motion, mapping, dynamic, gaussian splatting, survey, efficient  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: ar, 3d gaussian, robotics, gaussian splatting, survey  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v3)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v3.pdf)  
  Keywords: ar, 3d gaussian, geometry, nerf, gaussian splatting, survey, efficient  
- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197v1)**  
  Authors: Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07197v1.pdf)  
  Keywords: ar, 3d gaussian, compression, dynamic, 4d, compact, 3d reconstruction, gaussian splatting, high-fidelity, survey, efficient  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v2)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v2.pdf)  
  Keywords: semantic, slam, ar, 3d gaussian, localization, mapping, nerf, robotics, understanding, gaussian splatting, survey  

### Acceleration

*Showing the latest 50 out of 115 papers*

- **[Adaptive Anchor Policies for Efficient 4D Gaussian Streaming](https://arxiv.org/abs/2603.17227v1)**  
  Authors: Ashim Dahal, Rabab Abdelfattah, Nick Rahimi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17227v1.pdf)  
  Keywords: ar, dynamic, 4d, real-time rendering, gaussian splatting, fast, efficient  
- **[Feed-forward Gaussian Registration for Head Avatar Creation and Editing](https://arxiv.org/abs/2603.15811v1)**  
  Authors: Malte Prinzler, Paulo Gotardo, Siyu Tang, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15811v1.pdf)  
  Keywords: semantic, ar, tracking, head, avatar, fast, geometry  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: ar, 3d gaussian, ray marching, real-time rendering, gaussian splatting, high-fidelity, efficient  
- **[E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction](https://arxiv.org/abs/2603.14684v1)**  
  Authors: Yunsoo Kim, Changki Sung, Dasol Hong, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14684v1.pdf)  
  Keywords: ar, 3d gaussian, tracking, motion, lighting, dynamic, nerf, 3d reconstruction, gaussian splatting, fast  
- **[Scene Generation at Absolute Scale: Utilizing Semantic and Geometric Guidance From Text for Accurate and Interpretable 3D Indoor Scene Generation](https://arxiv.org/abs/2603.13910v1)**  
  Authors: Stefan Ainetter, Thomas Deixelberger, Edoardo A. Dominici, Philipp Drescher, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13910v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, gaussian splatting, fast  
- **[RetimeGS: Continuous-Time Reconstruction of 4D Gaussian Splatting](https://arxiv.org/abs/2603.13783v1)**  
  Authors: Xuezhen Wang, Li Ma, Yulin Shen, Zeyu Wang, Pedro V. Sander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13783v1.pdf)  
  Keywords: ar, 3d gaussian, motion, dynamic, 4d, deformation, gaussian splatting, fast  
- **[Mango-GS: Enhancing Spatio-Temporal Consistency in Dynamic Scenes Reconstruction using Multi-Frame Node-Guided 4D Gaussian Splatting](https://arxiv.org/abs/2603.11543v1)**  
  Authors: Tingxuan Huang, Haowei Zhu, Jun-hai Yong, Hao Pan, Bin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11543v1.pdf)  
  Keywords: semantic, ar, motion, dynamic, 4d, real-time rendering, deformation, gaussian splatting, high-fidelity  
- **[Mobile-GS: Real-time Gaussian Splatting for Mobile Devices](https://arxiv.org/abs/2603.11531v1)**  
  Authors: Xiaobiao Du, Yida Wang, Kun Zhan, Xin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11531v1.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, compact, gaussian splatting, geometry, efficient  
- **[PolGS++: Physically-Guided Polarimetric Gaussian Splatting for Fast Reflective Surface Reconstruction](https://arxiv.org/abs/2603.10801v1)**  
  Authors: Yufei Han, Chu Zhou, Youwei Lyu, Qi Chen, Si Li, Boxin Shi, Yunpeng Jia, Heng Guo, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10801v1.pdf)  
  Keywords: ar, face, 3d gaussian, gaussian splatting, fast, geometry, efficient  
- **[SignSparK: Efficient Multilingual Sign Language Production via Sparse Keyframe Learning](https://arxiv.org/abs/2603.10446v2)**  
  Authors: Jianhe Low, Alexandre Symeonidis-Herzig, Maksym Ivashechkin, Ozge Mercanoglu Sincan, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10446v2.pdf)  
  Keywords: ar, human, face, 3d gaussian, motion, avatar, gaussian splatting, high-fidelity, fast, segmentation, efficient  

### Applications

*Showing the latest 50 out of 499 papers*

- **[From ex(p) to poly: Gaussian Splatting with Polynomial Kernels](https://arxiv.org/abs/2603.18707v1)**  
  Authors: Joerg H. Mueller, Martin Winter, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18707v1.pdf)  
  Keywords: ar, gaussian splatting  
- **[OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2603.18510v1)**  
  Authors: Hongjia Zhai, Qi Zhang, Xiaokun Pan, Xiyu Zhang, Yitong Dong, Huaqi Zhang, Dan Xu, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18510v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, mapping, understanding, gaussian splatting, efficient  
- **[Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning](https://arxiv.org/abs/2603.18402v1)**  
  Authors: Yonghan Lee, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18402v1.pdf)  
  Keywords: ar, tracking, motion, dynamic, 4d, gaussian splatting, segmentation  
- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: semantic, slam, ar, face, 3d gaussian, lighting, mapping, understanding, gaussian splatting, segmentation  
- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: ar, human, 3d gaussian, head, avatar, gaussian splatting, body  
- **[CrowdGaussian: Reconstructing High-Fidelity 3D Gaussians for Human Crowd from a Single Image](https://arxiv.org/abs/2603.17779v1)**  
  Authors: Yizheng Song, Yiyu Zhuang, Qipeng Xu, Haixiang Wang, Jiahe Zhu, Jing Tian, Siyu Zhu, Hao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17779v1.pdf)  
  Keywords: ar, human, 3d gaussian, gaussian splatting, high-fidelity, geometry  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: ar, face, dynamic, 3d reconstruction, neural rendering, high-fidelity, geometry  
- **[ReLaGS: Relational Language Gaussian Splatting](https://arxiv.org/abs/2603.17605v1)**  
  Authors: Yaxu Xie, Abdalla Arafa, Alireza Javanmardi, Christen Millerdurai, Jia Cheng Hu, Shaoxiang Wang, Alain Pagani, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17605v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dfki-av.github.io/ReLaGS)  
  Keywords: semantic, ar, understanding, gaussian splatting, geometry, segmentation, efficient  
- **[UniSem: Generalizable Semantic 3D Reconstruction from Sparse Unposed Images](https://arxiv.org/abs/2603.17519v1)**  
  Authors: Guibiao Liao, Qian Ren, Kaimin Liao, Hua Wang, Zhi Chen, Luchao Wang, Yaohua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17519v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, 3d reconstruction, sparse-view, gaussian splatting, geometry, segmentation  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v1)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v1.pdf)  
  Keywords: ar, 3d gaussian, mapping, ray tracing, gaussian splatting, survey  

### Avatar Generation

*Showing the latest 50 out of 168 papers*

- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: semantic, slam, ar, face, 3d gaussian, lighting, mapping, understanding, gaussian splatting, segmentation  
- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: ar, human, 3d gaussian, head, avatar, gaussian splatting, body  
- **[CrowdGaussian: Reconstructing High-Fidelity 3D Gaussians for Human Crowd from a Single Image](https://arxiv.org/abs/2603.17779v1)**  
  Authors: Yizheng Song, Yiyu Zhuang, Qipeng Xu, Haixiang Wang, Jiahe Zhu, Jing Tian, Siyu Zhu, Hao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17779v1.pdf)  
  Keywords: ar, human, 3d gaussian, gaussian splatting, high-fidelity, geometry  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: ar, face, dynamic, 3d reconstruction, neural rendering, high-fidelity, geometry  
- **[SMAL-pets: SMAL Based Avatars of Pets from Single Image](https://arxiv.org/abs/2603.17131v1)**  
  Authors: Piotr Borycki, Joanna Waczyńska, Yizhe Zhu, Yongqiang Gao, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17131v1.pdf)  
  Keywords: ar, human, face, 3d gaussian, avatar, animation, gaussian splatting, high-fidelity  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: slam, outdoor, ar, tracking, head, dynamic, gaussian splatting, efficient  
- **[ProgressiveAvatars: Progressive Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2603.16447v1)**  
  Authors: Kaiwen Song, Jinkai Cui, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16447v1.pdf)  
  Keywords: ar, face, 3d gaussian, head, motion, avatar  
- **[Feed-forward Gaussian Registration for Head Avatar Creation and Editing](https://arxiv.org/abs/2603.15811v1)**  
  Authors: Malte Prinzler, Paulo Gotardo, Siyu Tang, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15811v1.pdf)  
  Keywords: semantic, ar, tracking, head, avatar, fast, geometry  
- **[KGS-GCN: Enhancing Sparse Skeleton Sensing via Kinematics-Driven Gaussian Splatting and Probabilistic Topology for Action Recognition](https://arxiv.org/abs/2603.16943v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Liping Zhang, Jie Li, Jiaxin Gao, Wenbo Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16943v1.pdf)  
  Keywords: semantic, ar, human, recognition, dynamic, gaussian splatting  
- **[Zero-Shot Reconstruction of Animatable 3D Avatars with Cloth Dynamics from a Single Image](https://arxiv.org/abs/2603.14772v1)**  
  Authors: Joohyun Kwon, Geonhee Sim, Gyeongsik Moon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14772v1.pdf)  
  Keywords: ar, human, 3d gaussian, motion, avatar, dynamic, animation, deformation, lightweight, efficient  

### Dynamic Scene

*Showing the latest 50 out of 207 papers*

- **[Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning](https://arxiv.org/abs/2603.18402v1)**  
  Authors: Yonghan Lee, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18402v1.pdf)  
  Keywords: ar, tracking, motion, dynamic, 4d, gaussian splatting, segmentation  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: ar, face, dynamic, 3d reconstruction, neural rendering, high-fidelity, geometry  
- **[Adaptive Anchor Policies for Efficient 4D Gaussian Streaming](https://arxiv.org/abs/2603.17227v1)**  
  Authors: Ashim Dahal, Rabab Abdelfattah, Nick Rahimi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17227v1.pdf)  
  Keywords: ar, dynamic, 4d, real-time rendering, gaussian splatting, fast, efficient  
- **[SMAL-pets: SMAL Based Avatars of Pets from Single Image](https://arxiv.org/abs/2603.17131v1)**  
  Authors: Piotr Borycki, Joanna Waczyńska, Yizhe Zhu, Yongqiang Gao, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17131v1.pdf)  
  Keywords: ar, human, face, 3d gaussian, avatar, animation, gaussian splatting, high-fidelity  
- **[MessyKitchens: Contact-rich object-level 3D scene reconstruction](https://arxiv.org/abs/2603.16868v1)**  
  Authors: Junaid Ahmed Ansari, Ran Ding, Fabio Pizzati, Ivan Laptev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16868v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://messykitchens.github.io)  
  Keywords: high-fidelity, ar, robotics, animation  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: slam, outdoor, ar, tracking, head, dynamic, gaussian splatting, efficient  
- **[ProgressiveAvatars: Progressive Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2603.16447v1)**  
  Authors: Kaiwen Song, Jinkai Cui, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16447v1.pdf)  
  Keywords: ar, face, 3d gaussian, head, motion, avatar  
- **[OGScene3D: Incremental Open-Vocabulary 3D Gaussian Scene Graph Mapping for Scene Understanding](https://arxiv.org/abs/2603.16301v2)**  
  Authors: Siting Zhu, Ziyun Lu, Guangming Wang, Chenguang Huang, Yongbo Chen, I-Ming Chen, Wolfram Burgard, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16301v2.pdf)  
  Keywords: semantic, ar, 3d gaussian, mapping, dynamic, understanding  
- **[KGS-GCN: Enhancing Sparse Skeleton Sensing via Kinematics-Driven Gaussian Splatting and Probabilistic Topology for Action Recognition](https://arxiv.org/abs/2603.16943v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Liping Zhang, Jie Li, Jiaxin Gao, Wenbo Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16943v1.pdf)  
  Keywords: semantic, ar, human, recognition, dynamic, gaussian splatting  
- **[Zero-Shot Reconstruction of Animatable 3D Avatars with Cloth Dynamics from a Single Image](https://arxiv.org/abs/2603.14772v1)**  
  Authors: Joohyun Kwon, Geonhee Sim, Gyeongsik Moon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14772v1.pdf)  
  Keywords: ar, human, 3d gaussian, motion, avatar, dynamic, animation, deformation, lightweight, efficient  

### Few-shot

- **[UniSem: Generalizable Semantic 3D Reconstruction from Sparse Unposed Images](https://arxiv.org/abs/2603.17519v1)**  
  Authors: Guibiao Liao, Qian Ren, Kaimin Liao, Hua Wang, Zhi Chen, Luchao Wang, Yaohua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17519v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, 3d reconstruction, sparse-view, gaussian splatting, geometry, segmentation  
- **[S2D: Sparse to Dense Lifting for 3D Reconstruction with Minimal Inputs](https://arxiv.org/abs/2603.10893v1)**  
  Authors: Yuzhou Ji, Qijian Tian, He Zhu, Xiaoqi Jiang, Guangzhi Cao, Lizhuang Ma, Yuan Xie, Xin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10893v1.pdf)  
  Keywords: ar, 3d gaussian, sparse view, 3d reconstruction, understanding, gaussian splatting, high-fidelity, efficient  
- **[Active View Selection with Perturbed Gaussian Ensemble for Tomographic Reconstruction](https://arxiv.org/abs/2603.06852v1)**  
  Authors: Yulun Wu, Ruyi Zha, Wei Cao, Yingying Li, Yuanhao Cai, Yaoyao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06852v1.pdf)  
  Keywords: ar, 3d gaussian, sparse-view, gaussian splatting, fast  
- **[CylinderSplat: 3D Gaussian Splatting with Cylindrical Triplanes for Panoramic Novel View Synthesis](https://arxiv.org/abs/2603.05882v1)**  
  Authors: Qiwei Wang, Xianghui Ze, Jingyi Yu, Yujiao Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05882v1.pdf)  
  Keywords: ar, 3d gaussian, sparse-view, gaussian splatting, geometry  
- **[DSA-SRGS: Super-Resolution Gaussian Splatting for Dynamic Sparse-View DSA Reconstruction](https://arxiv.org/abs/2603.04770v1)**  
  Authors: Shiyu Zhang, Zhicong Wu, Huangxuan Zhao, Zhentao Liu, Lei Chen, Yong Luo, Lefei Zhang, Zhiming Cui, Ziwen Ke, Bo Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04770v1.pdf)  
  Keywords: ar, dynamic, 4d, sparse-view, gaussian splatting  
- **[Intrinsic Geometry-Appearance Consistency Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2603.02893v1)**  
  Authors: Kaiqiang Xiong, Rui Peng, Jiahao Wu, Zhanke Wang, Jie Liang, Xiaoyun Zheng, Feng Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02893v1.pdf)  
  Keywords: ar, human, 3d gaussian, sparse-view, gaussian splatting, high-fidelity, geometry  
- **[Multimodal-Prior-Guided Importance Sampling for Hierarchical Gaussian Splatting in Sparse-View Novel View Synthesis](https://arxiv.org/abs/2603.02866v1)**  
  Authors: Kaiqiang Xiong, Zhanke Wang, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02866v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, sparse-view, gaussian splatting  
- **[SemGS: Feed-Forward Semantic 3D Gaussian Splatting from Sparse Views for Generalizable Scene Understanding](https://arxiv.org/abs/2603.02548v1)**  
  Authors: Sheng Ye, Zhen-Hui Dong, Ruoyu Fan, Tian Lv, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02548v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, understanding, gaussian splatting, sparse view  
- **[Sparse View Distractor-Free Gaussian Splatting](https://arxiv.org/abs/2603.01603v1)**  
  Authors: Yi Gu, Zhaorui Wang, Jiahang Cao, Jiaxu Wang, Mingle Zhao, Dongjun Ye, Renjing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01603v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, sparse-view, gaussian splatting, sparse view, fast, geometry, efficient  
- **[HeroGS: Hierarchical Guidance for Robust 3D Gaussian Splatting under Sparse Views](https://arxiv.org/abs/2603.01099v2)**  
  Authors: Jiashu Li, Xumeng Han, Zhaoyang Wei, Zipeng Wang, Kuiran Wang, Guorong Li, Zhenjun Han, Jianbin Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01099v2.pdf)  
  Keywords: ar, 3d gaussian, sparse view, sparse-view, gaussian splatting, high-fidelity, geometry  

### Geometry Reconstruction

*Showing the latest 50 out of 202 papers*

- **[CrowdGaussian: Reconstructing High-Fidelity 3D Gaussians for Human Crowd from a Single Image](https://arxiv.org/abs/2603.17779v1)**  
  Authors: Yizheng Song, Yiyu Zhuang, Qipeng Xu, Haixiang Wang, Jiahe Zhu, Jing Tian, Siyu Zhu, Hao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17779v1.pdf)  
  Keywords: ar, human, 3d gaussian, gaussian splatting, high-fidelity, geometry  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: ar, face, dynamic, 3d reconstruction, neural rendering, high-fidelity, geometry  
- **[ReLaGS: Relational Language Gaussian Splatting](https://arxiv.org/abs/2603.17605v1)**  
  Authors: Yaxu Xie, Abdalla Arafa, Alireza Javanmardi, Christen Millerdurai, Jia Cheng Hu, Shaoxiang Wang, Alain Pagani, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17605v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dfki-av.github.io/ReLaGS)  
  Keywords: semantic, ar, understanding, gaussian splatting, geometry, segmentation, efficient  
- **[UniSem: Generalizable Semantic 3D Reconstruction from Sparse Unposed Images](https://arxiv.org/abs/2603.17519v1)**  
  Authors: Guibiao Liao, Qian Ren, Kaimin Liao, Hua Wang, Zhi Chen, Luchao Wang, Yaohua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17519v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, 3d reconstruction, sparse-view, gaussian splatting, geometry, segmentation  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, localization, gaussian splatting, geometry  
- **[Leveling3D: Leveling Up 3D Reconstruction with Feed-Forward 3D Gaussian Splatting and Geometry-Aware Generation](https://arxiv.org/abs/2603.16211v1)**  
  Authors: Yiming Huang, Baixiang Huang, Beilei Cui, Chi Kit Ng, Long Bai, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16211v1.pdf)  
  Keywords: ar, 3d gaussian, 3d reconstruction, gaussian splatting, geometry, lightweight  
- **[Feed-forward Gaussian Registration for Head Avatar Creation and Editing](https://arxiv.org/abs/2603.15811v1)**  
  Authors: Malte Prinzler, Paulo Gotardo, Siyu Tang, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15811v1.pdf)  
  Keywords: semantic, ar, tracking, head, avatar, fast, geometry  
- **[GeoNVS: Geometry Grounded Video Diffusion for Novel View Synthesis](https://arxiv.org/abs/2603.14965v1)**  
  Authors: Minjun Kang, Inkyu Shin, Taeyeop Lee, Myungchul Kim, In So Kweon, Kuk-Jin Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14965v1.pdf)  
  Keywords: ar, geometry, 3d gaussian  
- **[E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction](https://arxiv.org/abs/2603.14684v1)**  
  Authors: Yunsoo Kim, Changki Sung, Dasol Hong, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14684v1.pdf)  
  Keywords: ar, 3d gaussian, tracking, motion, lighting, dynamic, nerf, 3d reconstruction, gaussian splatting, fast  
- **[Direct Object-Level Reconstruction via Probabilistic Gaussian Splatting](https://arxiv.org/abs/2603.14316v1)**  
  Authors: Shuai Guo, Ao Guo, Junchao Zhao, Qi Chen, Yuxiang Qi, Zechuan Li, Dong Chen, Tianjia Shao, Mingliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14316v1.pdf)  
  Keywords: ar, head, dynamic, 3d reconstruction, gaussian splatting, efficient  

### Large Scene

- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: slam, outdoor, ar, tracking, head, dynamic, gaussian splatting, efficient  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, localization, gaussian splatting, geometry  
- **[EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.06216v1)**  
  Authors: Miriam Jäger, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06216v1.pdf)  
  Keywords: ar, face, 3d gaussian, urban scene, 3d reconstruction, gaussian splatting, geometry  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, relighting, relightable, lighting, reflection, illumination, nerf, 3d reconstruction, gaussian splatting, fast  
- **[Interactive Augmented Reality-enabled Outdoor Scene Visualization For Enhanced Real-time Disaster Response](https://arxiv.org/abs/2602.21874v1)**  
  Authors: Dimitrios Apostolakis, Georgios Angelidis, Vasileios Argyriou, Panagiotis Sarigiannidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21874v1.pdf)  
  Keywords: semantic, ar, outdoor, face, 3d gaussian, lighting, gaussian splatting, fast, lightweight  
- **[Large-scale Photorealistic Outdoor 3D Scene Reconstruction from UAV Imagery Using Gaussian Splatting Techniques](https://arxiv.org/abs/2602.20342v1)**  
  Authors: Christos Maikos, Georgios Angelidis, Georgios Th. Papadopoulos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20342v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, vr, nerf, 3d reconstruction, neural rendering, gaussian splatting, high-fidelity, efficient  
- **[Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery](https://arxiv.org/abs/2602.14929v1)**  
  Authors: Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14929v1.pdf)  
  Keywords: semantic, ar, outdoor, 3d gaussian, head, localization, lighting, mapping, gaussian splatting, geometry  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, lighting, global illumination, real-time rendering, nerf, illumination, gaussian splatting, autonomous driving  
- **[Zero-Shot UAV Navigation in Forests via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2602.07101v2)**  
  Authors: Zinan Lv, Yeqian Qian, Chen Sang, Hao Liu, Danping Zou, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07101v2.pdf)  
  Keywords: ar, outdoor, 3d gaussian, relightable, lighting, dynamic, illumination, gaussian splatting, high-fidelity, geometry, lightweight  
- **[3DGS$^2$-TR: Scalable Second-Order Trust-Region Method for 3D Gaussian Splatting](https://arxiv.org/abs/2602.00395v1)**  
  Authors: Roger Hsiao, Yuchen Fang, Xiangru Huang, Ruilong Li, Hesam Rabeti, Zan Gojcic, Javad Lavaei, James Demmel, Sophia Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00395v1.pdf)  
  Keywords: ar, 3d gaussian, head, large scene, gaussian splatting, efficient  

### Model Compression

*Showing the latest 50 out of 212 papers*

- **[OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2603.18510v1)**  
  Authors: Hongjia Zhai, Qi Zhang, Xiaokun Pan, Xiyu Zhang, Yitong Dong, Huaqi Zhang, Dan Xu, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18510v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, mapping, understanding, gaussian splatting, efficient  
- **[ReLaGS: Relational Language Gaussian Splatting](https://arxiv.org/abs/2603.17605v1)**  
  Authors: Yaxu Xie, Abdalla Arafa, Alireza Javanmardi, Christen Millerdurai, Jia Cheng Hu, Shaoxiang Wang, Alain Pagani, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17605v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dfki-av.github.io/ReLaGS)  
  Keywords: semantic, ar, understanding, gaussian splatting, geometry, segmentation, efficient  
- **[Adaptive Anchor Policies for Efficient 4D Gaussian Streaming](https://arxiv.org/abs/2603.17227v1)**  
  Authors: Ashim Dahal, Rabab Abdelfattah, Nick Rahimi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17227v1.pdf)  
  Keywords: ar, dynamic, 4d, real-time rendering, gaussian splatting, fast, efficient  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: slam, outdoor, ar, tracking, head, dynamic, gaussian splatting, efficient  
- **[Leveling3D: Leveling Up 3D Reconstruction with Feed-Forward 3D Gaussian Splatting and Geometry-Aware Generation](https://arxiv.org/abs/2603.16211v1)**  
  Authors: Yiming Huang, Baixiang Huang, Beilei Cui, Chi Kit Ng, Long Bai, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16211v1.pdf)  
  Keywords: ar, 3d gaussian, 3d reconstruction, gaussian splatting, geometry, lightweight  
- **[NanoGS: Training-Free Gaussian Splat Simplification](https://arxiv.org/abs/2603.16103v1)**  
  Authors: Butian Xiong, Rong Liu, Tiantian Zhou, Meida Chen, Zhiwen Fan, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16103v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://saliteta.github.io/NanoGS)  
  Keywords: ar, 3d gaussian, compact, high-fidelity, compression, lightweight, efficient  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: ar, 3d gaussian, ray marching, real-time rendering, gaussian splatting, high-fidelity, efficient  
- **[Zero-Shot Reconstruction of Animatable 3D Avatars with Cloth Dynamics from a Single Image](https://arxiv.org/abs/2603.14772v1)**  
  Authors: Joohyun Kwon, Geonhee Sim, Gyeongsik Moon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14772v1.pdf)  
  Keywords: ar, human, 3d gaussian, motion, avatar, dynamic, animation, deformation, lightweight, efficient  
- **[LiDAR-EVS: Enhance Extrapolated View Synthesis for 3D Gaussian Splatting with Pseudo-LiDAR Supervision](https://arxiv.org/abs/2603.14763v1)**  
  Authors: Yiming Huang, Xin Kang, Sipeng Zhang, Hongliang Ren, Weihua Zhang, Junjie Lai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14763v1.pdf)  
  Keywords: ar, 3d gaussian, neural rendering, gaussian splatting, lightweight, autonomous driving  
- **[Direct Object-Level Reconstruction via Probabilistic Gaussian Splatting](https://arxiv.org/abs/2603.14316v1)**  
  Authors: Shuai Guo, Ao Guo, Junchao Zhao, Qi Chen, Yuxiang Qi, Zechuan Li, Dong Chen, Tianjia Shao, Mingliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14316v1.pdf)  
  Keywords: ar, head, dynamic, 3d reconstruction, gaussian splatting, efficient  

### Quality Enhancement

*Showing the latest 50 out of 131 papers*

- **[CrowdGaussian: Reconstructing High-Fidelity 3D Gaussians for Human Crowd from a Single Image](https://arxiv.org/abs/2603.17779v1)**  
  Authors: Yizheng Song, Yiyu Zhuang, Qipeng Xu, Haixiang Wang, Jiahe Zhu, Jing Tian, Siyu Zhu, Hao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17779v1.pdf)  
  Keywords: ar, human, 3d gaussian, gaussian splatting, high-fidelity, geometry  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: ar, face, dynamic, 3d reconstruction, neural rendering, high-fidelity, geometry  
- **[SMAL-pets: SMAL Based Avatars of Pets from Single Image](https://arxiv.org/abs/2603.17131v1)**  
  Authors: Piotr Borycki, Joanna Waczyńska, Yizhe Zhu, Yongqiang Gao, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17131v1.pdf)  
  Keywords: ar, human, face, 3d gaussian, avatar, animation, gaussian splatting, high-fidelity  
- **[MessyKitchens: Contact-rich object-level 3D scene reconstruction](https://arxiv.org/abs/2603.16868v1)**  
  Authors: Junaid Ahmed Ansari, Ran Ding, Fabio Pizzati, Ivan Laptev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16868v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://messykitchens.github.io)  
  Keywords: high-fidelity, ar, robotics, animation  
- **[NanoGS: Training-Free Gaussian Splat Simplification](https://arxiv.org/abs/2603.16103v1)**  
  Authors: Butian Xiong, Rong Liu, Tiantian Zhou, Meida Chen, Zhiwen Fan, Andrew Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16103v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://saliteta.github.io/NanoGS)  
  Keywords: ar, 3d gaussian, compact, high-fidelity, compression, lightweight, efficient  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: ar, 3d gaussian, ray marching, real-time rendering, gaussian splatting, high-fidelity, efficient  
- **[NavGSim: High-Fidelity Gaussian Splatting Simulator for Large-Scale Navigation](https://arxiv.org/abs/2603.15186v1)**  
  Authors: Jiahang Liu, Yuanxing Duan, Jiazhao Zhang, Minghan Li, Shaoan Wang, Zhizheng Zhang, He Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15186v1.pdf)  
  Keywords: ar, 3d gaussian, understanding, gaussian splatting, high-fidelity  
- **[PhyGaP: Physically-Grounded Gaussians with Polarization Cues](https://arxiv.org/abs/2603.14001v1)**  
  Authors: Jiale Wu, Xiaoyang Bai, Zongqi He, Weiwei Xu, Yifan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14001v1.pdf)  
  Keywords: ar, face, relighting, 3d gaussian, lighting, reflection, gaussian splatting, high-fidelity  
- **[Catalyst4D: High-Fidelity 3D-to-4D Scene Editing via Dynamic Propagation](https://arxiv.org/abs/2603.12766v1)**  
  Authors: Shifeng Chen, Yihui Li, Jun Liao, Hongyu Yang, Di Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12766v1.pdf)  
  Keywords: ar, motion, dynamic, 4d, nerf, deformation, high-fidelity  
- **[AstroSplat: Physics-Based Gaussian Splatting for Rendering and Reconstruction of Small Celestial Bodies](https://arxiv.org/abs/2603.11969v1)**  
  Authors: Jennifer Nolan, Travis Driver, John Christian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11969v1.pdf)  
  Keywords: ar, face, gaussian splatting, high-fidelity, body  

### Ray Tracing

- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v1)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v1.pdf)  
  Keywords: ar, 3d gaussian, mapping, ray tracing, gaussian splatting, survey  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: ar, 3d gaussian, ray marching, real-time rendering, gaussian splatting, high-fidelity, efficient  
- **[Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction](https://arxiv.org/abs/2603.08503v1)**  
  Authors: Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08503v1.pdf) | [![GitHub](https://img.shields.io/github/stars/1170632760/Spherical-GOF?style=social)](https://github.com/1170632760/Spherical-GOF)  
  Keywords: ar, 3d gaussian, ray casting, robotics, gaussian splatting, fast, geometry, efficient  
- **[Ref-DGS: Reflective Dual Gaussian Splatting](https://arxiv.org/abs/2603.07664v2)**  
  Authors: Ningjing Fan, Yiqun Wang, Dongming Yan, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07664v2.pdf)  
  Keywords: ar, face, reflection, ray tracing, gaussian splatting, fast, geometry, lightweight, efficient  
- **[Radiometrically Consistent Gaussian Surfels for Inverse Rendering](https://arxiv.org/abs/2603.01491v1)**  
  Authors: Kyu Beom Han, Jaeyoon Kim, Woo Jae Kim, Jinhwan Seo, Sung-eui Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01491v1.pdf)  
  Keywords: ar, relighting, lighting, global illumination, ray tracing, reflection, illumination, gaussian splatting, efficient  
- **[Nighttime Autonomous Driving Scene Reconstruction with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2602.13549v1)**  
  Authors: Tae-Kyeong Kim, Xingxin Chen, Guile Wu, Chengjie Huang, Dongfeng Bai, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13549v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, lighting, global illumination, real-time rendering, nerf, illumination, gaussian splatting, autonomous driving  
- **[Rotated Lights for Consistent and Efficient 2D Gaussians Inverse Rendering](https://arxiv.org/abs/2602.08724v1)**  
  Authors: Geng Lin, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08724v1.pdf)  
  Keywords: ar, relighting, lighting, global illumination, illumination, shadow, gaussian splatting, geometry, efficient  
- **[Radioactive 3D Gaussian Ray Tracing for Tomographic Reconstruction](https://arxiv.org/abs/2602.01057v1)**  
  Authors: Ling Chen, Bao Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01057v1.pdf)  
  Keywords: ar, ray tracing, 3d gaussian, gaussian splatting  
- **[EAG-PT: Emission-Aware Gaussians and Path Tracing for Indoor Scene Reconstruction and Editing](https://arxiv.org/abs/2601.23065v1)**  
  Authors: Xijie Yang, Mulin Yu, Changjian Jiang, Kerui Ren, Tao Lu, Jiangmiao Pang, Dahua Lin, Bo Dai, Linning Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.23065v1.pdf)  
  Keywords: ar, illumination, nerf, efficient, geometry, light transport, path tracing  
- **[Hybrid Foveated Path Tracing with Peripheral Gaussians for Immersive Anatomy](https://arxiv.org/abs/2601.22026v1)**  
  Authors: Constantin Kleinbeck, Luisa Theelke, Hannah Schieber, Ulrich Eck, Rüdiger von Eisenhart-Rothe, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22026v1.pdf)  
  Keywords: medical, ar, head, vr, understanding, gaussian splatting, lightweight, path tracing  

### Relighting

*Showing the latest 50 out of 71 papers*

- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: semantic, slam, ar, face, 3d gaussian, lighting, mapping, understanding, gaussian splatting, segmentation  
- **[E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction](https://arxiv.org/abs/2603.14684v1)**  
  Authors: Yunsoo Kim, Changki Sung, Dasol Hong, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14684v1.pdf)  
  Keywords: ar, 3d gaussian, tracking, motion, lighting, dynamic, nerf, 3d reconstruction, gaussian splatting, fast  
- **[PhyGaP: Physically-Grounded Gaussians with Polarization Cues](https://arxiv.org/abs/2603.14001v1)**  
  Authors: Jiale Wu, Xiaoyang Bai, Zongqi He, Weiwei Xu, Yifan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14001v1.pdf)  
  Keywords: ar, face, relighting, 3d gaussian, lighting, reflection, gaussian splatting, high-fidelity  
- **[LR-SGS: Robust LiDAR-Reflectance-Guided Salient Gaussian Splatting for Self-Driving Scene Reconstruction](https://arxiv.org/abs/2603.12647v1)**  
  Authors: Ziyu Chen, Fan Zhu, Hui Zhu, Deyi Kong, Xinkai Kuang, Yujia Zhang, Chunmao Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12647v1.pdf)  
  Keywords: ar, 3d gaussian, motion, lighting, gaussian splatting, efficient  
- **[InstantHDR: Single-forward Gaussian Splatting for High Dynamic Range 3D Reconstruction](https://arxiv.org/abs/2603.11298v2)**  
  Authors: Dingqiang Ye, Jiacong Xu, Jianglu Ping, Yuxiang Guo, Chao Fan, Vishal M. Patel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11298v2.pdf)  
  Keywords: ar, lighting, mapping, dynamic, 3d reconstruction, gaussian splatting, geometry  
- **[Ref-DGS: Reflective Dual Gaussian Splatting](https://arxiv.org/abs/2603.07664v2)**  
  Authors: Ningjing Fan, Yiqun Wang, Dongming Yan, Peter Wonka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07664v2.pdf)  
  Keywords: ar, face, reflection, ray tracing, gaussian splatting, fast, geometry, lightweight, efficient  
- **[3DGS-HPC: Distractor-free 3D Gaussian Splatting with Hybrid Patch-wise Classification](https://arxiv.org/abs/2603.07587v1)**  
  Authors: Jiahao Chen, Yipeng Qin, Ganlong Zhao, Xin Li, Wenping Wang, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07587v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, shadow, gaussian splatting  
- **[Spectral Probing of Feature Upsamplers in 2D-to-3D Scene Reconstruction](https://arxiv.org/abs/2603.05787v1)**  
  Authors: Ling Xiao, Yuliang Xiu, Yue Chen, Guoming Wang, Toshihiko Yamasaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05787v1.pdf)  
  Keywords: geometry, lighting, 3d reconstruction, ar  
- **[SSR-GS: Separating Specular Reflection in Gaussian Splatting for Glossy Surface Reconstruction](https://arxiv.org/abs/2603.05152v1)**  
  Authors: Ningjing Fan, Yiqun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05152v1.pdf)  
  Keywords: ar, face, 3d gaussian, reflection, illumination, gaussian splatting, geometry, efficient  
- **[R3GW: Relightable 3D Gaussians for Outdoor Scenes in the Wild](https://arxiv.org/abs/2603.02801v1)**  
  Authors: Margherita Lea Corona, Wieland Morgenstern, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02801v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, relighting, relightable, lighting, reflection, illumination, nerf, 3d reconstruction, gaussian splatting, fast  

### SLAM

*Showing the latest 50 out of 78 papers*

- **[OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2603.18510v1)**  
  Authors: Hongjia Zhai, Qi Zhang, Xiaokun Pan, Xiyu Zhang, Yitong Dong, Huaqi Zhang, Dan Xu, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18510v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, mapping, understanding, gaussian splatting, efficient  
- **[Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning](https://arxiv.org/abs/2603.18402v1)**  
  Authors: Yonghan Lee, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18402v1.pdf)  
  Keywords: ar, tracking, motion, dynamic, 4d, gaussian splatting, segmentation  
- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: semantic, slam, ar, face, 3d gaussian, lighting, mapping, understanding, gaussian splatting, segmentation  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v1)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v1.pdf)  
  Keywords: ar, 3d gaussian, mapping, ray tracing, gaussian splatting, survey  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: slam, outdoor, ar, tracking, head, dynamic, gaussian splatting, efficient  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, localization, gaussian splatting, geometry  
- **[OGScene3D: Incremental Open-Vocabulary 3D Gaussian Scene Graph Mapping for Scene Understanding](https://arxiv.org/abs/2603.16301v2)**  
  Authors: Siting Zhu, Ziyun Lu, Guangming Wang, Chenguang Huang, Yongbo Chen, I-Ming Chen, Wolfram Burgard, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16301v2.pdf)  
  Keywords: semantic, ar, 3d gaussian, mapping, dynamic, understanding  
- **[Feed-forward Gaussian Registration for Head Avatar Creation and Editing](https://arxiv.org/abs/2603.15811v1)**  
  Authors: Malte Prinzler, Paulo Gotardo, Siyu Tang, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15811v1.pdf)  
  Keywords: semantic, ar, tracking, head, avatar, fast, geometry  
- **[E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction](https://arxiv.org/abs/2603.14684v1)**  
  Authors: Yunsoo Kim, Changki Sung, Dasol Hong, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14684v1.pdf)  
  Keywords: ar, 3d gaussian, tracking, motion, lighting, dynamic, nerf, 3d reconstruction, gaussian splatting, fast  
- **[InstantHDR: Single-forward Gaussian Splatting for High Dynamic Range 3D Reconstruction](https://arxiv.org/abs/2603.11298v2)**  
  Authors: Dingqiang Ye, Jiacong Xu, Jianglu Ping, Yuxiang Guo, Chao Fan, Vishal M. Patel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11298v2.pdf)  
  Keywords: ar, lighting, mapping, dynamic, 3d reconstruction, gaussian splatting, geometry  

### Scene Understanding

*Showing the latest 50 out of 133 papers*

- **[OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2603.18510v1)**  
  Authors: Hongjia Zhai, Qi Zhang, Xiaokun Pan, Xiyu Zhang, Yitong Dong, Huaqi Zhang, Dan Xu, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18510v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, mapping, understanding, gaussian splatting, efficient  
- **[Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning](https://arxiv.org/abs/2603.18402v1)**  
  Authors: Yonghan Lee, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18402v1.pdf)  
  Keywords: ar, tracking, motion, dynamic, 4d, gaussian splatting, segmentation  
- **[Semantic Segmentation and Depth Estimation for Real-Time Lunar Surface Mapping Using 3D Gaussian Splatting](https://arxiv.org/abs/2603.18218v1)**  
  Authors: Guillem Casadesus Vila, Adam Dai, Grace Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18218v1.pdf)  
  Keywords: semantic, slam, ar, face, 3d gaussian, lighting, mapping, understanding, gaussian splatting, segmentation  
- **[ReLaGS: Relational Language Gaussian Splatting](https://arxiv.org/abs/2603.17605v1)**  
  Authors: Yaxu Xie, Abdalla Arafa, Alireza Javanmardi, Christen Millerdurai, Jia Cheng Hu, Shaoxiang Wang, Alain Pagani, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17605v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dfki-av.github.io/ReLaGS)  
  Keywords: semantic, ar, understanding, gaussian splatting, geometry, segmentation, efficient  
- **[UniSem: Generalizable Semantic 3D Reconstruction from Sparse Unposed Images](https://arxiv.org/abs/2603.17519v1)**  
  Authors: Guibiao Liao, Qian Ren, Kaimin Liao, Hua Wang, Zhi Chen, Luchao Wang, Yaohua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17519v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, 3d reconstruction, sparse-view, gaussian splatting, geometry, segmentation  
- **[OGScene3D: Incremental Open-Vocabulary 3D Gaussian Scene Graph Mapping for Scene Understanding](https://arxiv.org/abs/2603.16301v2)**  
  Authors: Siting Zhu, Ziyun Lu, Guangming Wang, Chenguang Huang, Yongbo Chen, I-Ming Chen, Wolfram Burgard, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16301v2.pdf)  
  Keywords: semantic, ar, 3d gaussian, mapping, dynamic, understanding  
- **[Feed-forward Gaussian Registration for Head Avatar Creation and Editing](https://arxiv.org/abs/2603.15811v1)**  
  Authors: Malte Prinzler, Paulo Gotardo, Siyu Tang, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15811v1.pdf)  
  Keywords: semantic, ar, tracking, head, avatar, fast, geometry  
- **[NavGSim: High-Fidelity Gaussian Splatting Simulator for Large-Scale Navigation](https://arxiv.org/abs/2603.15186v1)**  
  Authors: Jiahang Liu, Yuanxing Duan, Jiazhao Zhang, Minghan Li, Shaoan Wang, Zhizheng Zhang, He Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15186v1.pdf)  
  Keywords: ar, 3d gaussian, understanding, gaussian splatting, high-fidelity  
- **[KGS-GCN: Enhancing Sparse Skeleton Sensing via Kinematics-Driven Gaussian Splatting and Probabilistic Topology for Action Recognition](https://arxiv.org/abs/2603.16943v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Liping Zhang, Jie Li, Jiaxin Gao, Wenbo Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16943v1.pdf)  
  Keywords: semantic, ar, human, recognition, dynamic, gaussian splatting  
- **[In-Field 3D Wheat Head Instance Segmentation From TLS Point Clouds Using Deep Learning Without Manual Labels](https://arxiv.org/abs/2603.14309v1)**  
  Authors: Tomislav Medic, Liangliang Nan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14309v1.pdf)  
  Keywords: ar, 3d gaussian, head, gaussian splatting, segmentation  



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