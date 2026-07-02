# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-07-02 02:11:05

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
- [Acceleration](#acceleration) (92 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (500 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (182 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (186 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (45 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (214 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (21 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (191 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (118 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (14 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (57 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (76 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (118 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Recent Advances and Trends in Learning-based 3D Representations](https://arxiv.org/abs/2606.04871v1)**  
  Authors: Adrien Schockaert, Hamid Laga, Hazem Wannous, Vincent Magnier, Guillaume Dufaye, Jean-françois Witz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.04871v1.pdf)  
  Keywords: survey, neural rendering, 4d, compact, 3d reconstruction, motion, recognition, medical, gaussian splatting, vr, autonomous driving, 3d gaussian, ar  
- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137v1)**  
  Authors: Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00137v1.pdf)  
  Keywords: survey, mapping, gaussian splatting, animation, geometry, ar  
- **[ReefMapGS: Enabling Large-Scale Underwater Reconstruction by Closing the Loop Between Multimodal SLAM and Gaussian Splatting](https://arxiv.org/abs/2604.11992v1)**  
  Authors: Daniel Yang, Jungseok Hong, John J. Leonard, Yogesh Girdhar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11992v1.pdf)  
  Keywords: slam, tracking, survey, efficient, 3d reconstruction, motion, gaussian splatting, geometry, 3d gaussian, ar  
- **[A Survey of Spatial Memory Representations for Efficient Robot Navigation](https://arxiv.org/abs/2604.16482v1)**  
  Authors: Ma. Madecheen S. Pangaliman, Steven S. Sison, Erwin P. Quilloy, Rowel Atienza  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.16482v1.pdf)  
  Keywords: slam, survey, semantic, efficient, ar  

### Acceleration

*Showing the latest 50 out of 92 papers*

- **[FastBridge: Closing the Model-Based Realization Gap in Safety Filters on 3D Gaussian Splatting for Fast Quadrotor Flight](https://arxiv.org/abs/2607.01200v1)**  
  Authors: Tscholl Dario, Nakka Yashwanth Kumar, Gunter Brian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01200v1.pdf)  
  Keywords: acceleration, gaussian splatting, geometry, dynamic, 3d gaussian, fast, ar  
- **[Relation-Centric Open-Vocabulary 3D Gaussian Segmentation](https://arxiv.org/abs/2607.01140v1)**  
  Authors: Eunsung Cha, Hyunjoon Lee, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01140v1.pdf)  
  Keywords: efficient, understanding, segmentation, 3d gaussian, fast, ar  
- **[GaussianEmoTalker: Real-Time Emotional Talking Head Synthesis with Audio-Driven and Blendshape-Based 3D Gaussian Splatting](https://arxiv.org/abs/2607.00959v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Yixuan Dong, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00959v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://njust-yang.github.io/GaussianEmoTalker.github.io)  
  Keywords: head, real-time rendering, avatar, motion, gaussian splatting, animation, high-fidelity, deformation, 3d gaussian, ar  
- **[Improving Sparse-View 3DGS Generalization via Flat Minima Optimization](https://arxiv.org/abs/2607.00885v1)**  
  Authors: Kangmin Seo, Sangeek Hyun, MinKyu Lee, Jae-Pil Heo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00885v1.pdf)  
  Keywords: real-time rendering, neural rendering, efficient, nerf, ar, gaussian splatting, sparse-view, dynamic, 3d gaussian, fast, lightweight  
- **[GADA: Geometry-Aware Deformable Aggregation for Image-Based Gaussian Splatting](https://arxiv.org/abs/2607.00595v1)**  
  Authors: Siwoo Lim, Sunjae Yoon, Gwanhyeong Koo, Chang D. Yoo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00595v1.pdf)  
  Keywords: geometry, gaussian splatting, fast, ar  
- **[DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918v1)**  
  Authors: Junzhe Jiang, Zipei Ma, Zijie Pan, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31918v1.pdf)  
  Keywords: real-time rendering, lighting, autonomous driving, 3d gaussian, ar  
- **[AugSplat: Radiance Field-Informed Gaussian Splatting for Sparse-View Settings](https://arxiv.org/abs/2606.31556v1)**  
  Authors: Lorenzo Lazzaroni, Riccardo Bollati, Daniel Barath, Michael Niemeyer, Keisuke Tateno  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31556v1.pdf)  
  Keywords: real-time rendering, nerf, sparse-view, gaussian splatting, geometry, ar  
- **[Learning Video Dynamics with Predictive Differentiable Rendering](https://arxiv.org/abs/2606.31050v1)**  
  Authors: Yujin Tang, Tian Zhou, Xin Lin, Cheng Tan, Yifan Hu, Rong Jin, SouYoung Jin, Liang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31050v1.pdf)  
  Keywords: head, 3d reconstruction, human, ar, gaussian splatting, high-fidelity, dynamic, 3d gaussian, fast, lightweight  
- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869v1)**  
  Authors: Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30869v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gray)  
  Keywords: ray tracing, gaussian splatting, 3d gaussian, fast, ar  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: real-time rendering, reflection, geometry, ray tracing, efficient, gaussian splatting, path tracing, 3d gaussian, fast, ar  

### Applications

*Showing the latest 50 out of 500 papers*

- **[World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video](https://arxiv.org/abs/2607.01202v1)**  
  Authors: Liyuan Zhu, Shengyu Huang, Amrita Mazumdar, Tianye Li, Zan Gojcic, Gordon Wetzstein, Iro Armeni, Shalini De Mello, Alex Trevithick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01202v1.pdf)  
  Keywords: 4d, motion, geometry, dynamic, 3d gaussian, ar  
- **[FastBridge: Closing the Model-Based Realization Gap in Safety Filters on 3D Gaussian Splatting for Fast Quadrotor Flight](https://arxiv.org/abs/2607.01200v1)**  
  Authors: Tscholl Dario, Nakka Yashwanth Kumar, Gunter Brian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01200v1.pdf)  
  Keywords: acceleration, gaussian splatting, geometry, dynamic, 3d gaussian, fast, ar  
- **[Efficient Compression of Structured and Unstructured Volumes via Learned 3D Gaussian Representation](https://arxiv.org/abs/2607.01164v1)**  
  Authors: Landon Dyken, Sharmistha Chakrabarti, Nathan Debardeleben, Steve Petruzza, Qi Wu, Will Usher, Sidharth Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01164v1.pdf)  
  Keywords: compression, efficient, geometry, 3d gaussian, ar  
- **[Relation-Centric Open-Vocabulary 3D Gaussian Segmentation](https://arxiv.org/abs/2607.01140v1)**  
  Authors: Eunsung Cha, Hyunjoon Lee, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01140v1.pdf)  
  Keywords: efficient, understanding, segmentation, 3d gaussian, fast, ar  
- **[GaussianEmoTalker: Real-Time Emotional Talking Head Synthesis with Audio-Driven and Blendshape-Based 3D Gaussian Splatting](https://arxiv.org/abs/2607.00959v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Yixuan Dong, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00959v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://njust-yang.github.io/GaussianEmoTalker.github.io)  
  Keywords: head, real-time rendering, avatar, motion, gaussian splatting, animation, high-fidelity, deformation, 3d gaussian, ar  
- **[DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors](https://arxiv.org/abs/2607.00889v1)**  
  Authors: Seok-Young Kim, Abdelrahman Elskhawy, Taewook Ha, Dooyoung Kim, Eunjae Shin, Benjamin Busam, Woontack Woo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00889v1.pdf)  
  Keywords: 3d gaussian, ar, semantic  
- **[Improving Sparse-View 3DGS Generalization via Flat Minima Optimization](https://arxiv.org/abs/2607.00885v1)**  
  Authors: Kangmin Seo, Sangeek Hyun, MinKyu Lee, Jae-Pil Heo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00885v1.pdf)  
  Keywords: real-time rendering, neural rendering, efficient, nerf, ar, gaussian splatting, sparse-view, dynamic, 3d gaussian, fast, lightweight  
- **[Pano2World: End-to-End 3D Generation via Unified Multi-View Sequences](https://arxiv.org/abs/2607.00832v1)**  
  Authors: Zhenjia Li, Jinrang Jia, Yifeng Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00832v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, semantic  
- **[GaussianFusion: Unified 3D Gaussian Representation for Multi-Modal Fusion Perception](https://arxiv.org/abs/2607.00746v1)**  
  Authors: Xiao Zhao, Chang Liu, Mingxu Zhu, Zheyuan Zhang, Linna Song, Qingliang Luo, Chufan Guo, Kuifeng Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00746v1.pdf)  
  Keywords: 3d gaussian, ar, semantic  
- **[Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673v1)**  
  Authors: Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu, Krishna Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00673v1.pdf)  
  Keywords: outdoor, deformation, 3d gaussian, human, ar  

### Avatar Generation

*Showing the latest 50 out of 182 papers*

- **[GaussianEmoTalker: Real-Time Emotional Talking Head Synthesis with Audio-Driven and Blendshape-Based 3D Gaussian Splatting](https://arxiv.org/abs/2607.00959v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Yixuan Dong, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00959v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://njust-yang.github.io/GaussianEmoTalker.github.io)  
  Keywords: head, real-time rendering, avatar, motion, gaussian splatting, animation, high-fidelity, deformation, 3d gaussian, ar  
- **[Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673v1)**  
  Authors: Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu, Krishna Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00673v1.pdf)  
  Keywords: outdoor, deformation, 3d gaussian, human, ar  
- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: compact, ar, gaussian splatting, geometry, ray casting, human  
- **[LUNA: Learning Universal 3D Human Animation Beyond Skinning](https://arxiv.org/abs/2606.31981v1)**  
  Authors: Peng Li, Rawal Khirodkar, Junxuan Li, Yuan Dong, Chen Cao, Yuan Liu, Wenhan Luo, Yike Guo, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31981v1.pdf)  
  Keywords: avatar, ar, motion, body, animation, deformation, dynamic, 3d gaussian, human  
- **[Practical High-Fidelity Novel-View Synthesis of Mounted Lepidoptera](https://arxiv.org/abs/2606.31679v1)**  
  Authors: Kristof Overdulve, Lode Jorissen, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31679v1.pdf)  
  Keywords: face, body, gaussian splatting, high-fidelity, segmentation, 3d gaussian, ar  
- **[Intrinsic decomposition and editing of 3D Gaussian splats](https://arxiv.org/abs/2606.31637v1)**  
  Authors: Alexandre Lanvin, Jeffrey Hu, Simon Lucas, Adrien Bousseau, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31637v1.pdf)  
  Keywords: lighting, face, gaussian splatting, 3d gaussian, ar  
- **[Learning Video Dynamics with Predictive Differentiable Rendering](https://arxiv.org/abs/2606.31050v1)**  
  Authors: Yujin Tang, Tian Zhou, Xin Lin, Cheng Tan, Yifan Hu, Rong Jin, SouYoung Jin, Liang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31050v1.pdf)  
  Keywords: head, 3d reconstruction, human, ar, gaussian splatting, high-fidelity, dynamic, 3d gaussian, fast, lightweight  
- **[VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes](https://arxiv.org/abs/2606.30645v1)**  
  Authors: Yen-Jen Wang, Jiaman Li, Sirui Chen, Takara E. Truong, Pei Xu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, Karen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30645v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vision-language-kinematics.github.io)  
  Keywords: mapping, ar, motion, body, gaussian splatting, 3d gaussian, human  
- **[StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors](https://arxiv.org/abs/2606.30545v1)**  
  Authors: Wenhao Yuan, Yiyuan Ge, Deli Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30545v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://stringerywh00.github.io/StereoGS_project_page)  
  Keywords: head, nerf, face, sparse-view, gaussian splatting, geometry, dynamic, 3d gaussian, ar  
- **[Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes](https://arxiv.org/abs/2606.30436v1)**  
  Authors: Sicheng Yu, Dongxu Shen, Beizhen Zhao, Guanzhi Ding, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30436v1.pdf)  
  Keywords: slam, head, tracking, mapping, outdoor, efficient, motion, gaussian splatting, high-fidelity, dynamic, 3d gaussian, ar  

### Dynamic Scene

*Showing the latest 50 out of 186 papers*

- **[World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video](https://arxiv.org/abs/2607.01202v1)**  
  Authors: Liyuan Zhu, Shengyu Huang, Amrita Mazumdar, Tianye Li, Zan Gojcic, Gordon Wetzstein, Iro Armeni, Shalini De Mello, Alex Trevithick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01202v1.pdf)  
  Keywords: 4d, motion, geometry, dynamic, 3d gaussian, ar  
- **[FastBridge: Closing the Model-Based Realization Gap in Safety Filters on 3D Gaussian Splatting for Fast Quadrotor Flight](https://arxiv.org/abs/2607.01200v1)**  
  Authors: Tscholl Dario, Nakka Yashwanth Kumar, Gunter Brian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01200v1.pdf)  
  Keywords: acceleration, gaussian splatting, geometry, dynamic, 3d gaussian, fast, ar  
- **[GaussianEmoTalker: Real-Time Emotional Talking Head Synthesis with Audio-Driven and Blendshape-Based 3D Gaussian Splatting](https://arxiv.org/abs/2607.00959v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Yixuan Dong, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00959v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://njust-yang.github.io/GaussianEmoTalker.github.io)  
  Keywords: head, real-time rendering, avatar, motion, gaussian splatting, animation, high-fidelity, deformation, 3d gaussian, ar  
- **[Improving Sparse-View 3DGS Generalization via Flat Minima Optimization](https://arxiv.org/abs/2607.00885v1)**  
  Authors: Kangmin Seo, Sangeek Hyun, MinKyu Lee, Jae-Pil Heo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00885v1.pdf)  
  Keywords: real-time rendering, neural rendering, efficient, nerf, ar, gaussian splatting, sparse-view, dynamic, 3d gaussian, fast, lightweight  
- **[Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673v1)**  
  Authors: Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu, Krishna Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00673v1.pdf)  
  Keywords: outdoor, deformation, 3d gaussian, human, ar  
- **[CORGI: Consistency-Aware 3D Dog Reconstruction from a Single Image in the Wild](https://arxiv.org/abs/2607.00321v1)**  
  Authors: Yuxiao Wu, Weile Li, Boyi Zhu, Yumeng Liu, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00321v1.pdf)  
  Keywords: deformation, high-fidelity, ar  
- **[Progressive Pose-Guided 4D Animal Reconstruction from Monocular Video](https://arxiv.org/abs/2607.00157v1)**  
  Authors: Siyuan Li, Weiying Chen, Yilin Wang, Xinxin Zuo, Xingyu Li, Li Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00157v1.pdf)  
  Keywords: 4d, gaussian splatting, deformation, high-fidelity, 3d gaussian, ar  
- **[LUNA: Learning Universal 3D Human Animation Beyond Skinning](https://arxiv.org/abs/2606.31981v1)**  
  Authors: Peng Li, Rawal Khirodkar, Junxuan Li, Yuan Dong, Chen Cao, Yuan Liu, Wenhan Luo, Yike Guo, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31981v1.pdf)  
  Keywords: avatar, ar, motion, body, animation, deformation, dynamic, 3d gaussian, human  
- **[Learning Video Dynamics with Predictive Differentiable Rendering](https://arxiv.org/abs/2606.31050v1)**  
  Authors: Yujin Tang, Tian Zhou, Xin Lin, Cheng Tan, Yifan Hu, Rong Jin, SouYoung Jin, Liang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31050v1.pdf)  
  Keywords: head, 3d reconstruction, human, ar, gaussian splatting, high-fidelity, dynamic, 3d gaussian, fast, lightweight  
- **[VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes](https://arxiv.org/abs/2606.30645v1)**  
  Authors: Yen-Jen Wang, Jiaman Li, Sirui Chen, Takara E. Truong, Pei Xu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, Karen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30645v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vision-language-kinematics.github.io)  
  Keywords: mapping, ar, motion, body, gaussian splatting, 3d gaussian, human  

### Few-shot

- **[Improving Sparse-View 3DGS Generalization via Flat Minima Optimization](https://arxiv.org/abs/2607.00885v1)**  
  Authors: Kangmin Seo, Sangeek Hyun, MinKyu Lee, Jae-Pil Heo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00885v1.pdf)  
  Keywords: real-time rendering, neural rendering, efficient, nerf, ar, gaussian splatting, sparse-view, dynamic, 3d gaussian, fast, lightweight  
- **[AugSplat: Radiance Field-Informed Gaussian Splatting for Sparse-View Settings](https://arxiv.org/abs/2606.31556v1)**  
  Authors: Lorenzo Lazzaroni, Riccardo Bollati, Daniel Barath, Michael Niemeyer, Keisuke Tateno  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31556v1.pdf)  
  Keywords: real-time rendering, nerf, sparse-view, gaussian splatting, geometry, ar  
- **[StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors](https://arxiv.org/abs/2606.30545v1)**  
  Authors: Wenhao Yuan, Yiyuan Ge, Deli Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30545v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://stringerywh00.github.io/StereoGS_project_page)  
  Keywords: head, nerf, face, sparse-view, gaussian splatting, geometry, dynamic, 3d gaussian, ar  
- **[HiReFF: High-Resolution Feedforward Human Reconstruction from Uncalibrated Sparse-View Video](https://arxiv.org/abs/2606.29333v1)**  
  Authors: Yiming Jiang, Hanzhang Tu, Wenfeng Song, Siyou Lin, Liang An, Shuai Li, Aimin Hao, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29333v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://iridescentjiang.github.io/HiReFF)  
  Keywords: head, efficient, ar, vr, sparse-view, 3d gaussian, human  
- **[Occlusion-Robust Multi-Object Decoupling for Physics-Based Robotic Interaction](https://arxiv.org/abs/2606.29303v2)**  
  Authors: Xin Dong, Lihan Zhang, Tianru Dai, Wenfeng Deng, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29303v2.pdf)  
  Keywords: 3d reconstruction, sparse-view, gaussian splatting, segmentation, geometry, dynamic, 3d gaussian, ar  
- **[StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views](https://arxiv.org/abs/2606.28321v1)**  
  Authors: Jia-Chen Zhao, Beiqi Chen, Xinyang Chen, Guangcong Wang, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.28321v1.pdf) | [![GitHub](https://img.shields.io/github/stars/J-C-Zhao/StructSplat?style=social)](https://github.com/J-C-Zhao/StructSplat) | [![Project](https://img.shields.io/badge/-Project-blue)](https://structsplat.github.io)  
  Keywords: semantic, gaussian splatting, sparse view, geometry, 3d gaussian, ar  
- **[Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography](https://arxiv.org/abs/2606.22525v1)**  
  Authors: Yikuang Yuluo, Ao Wang, Shen Kuan, Yujie Liu, Wang Liao, Ying Chen, Shuangyang Zhong, Yixing Huang, Fuquan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22525v1.pdf)  
  Keywords: efficient, sparse-view, gaussian splatting, deformation, geometry, 3d gaussian, ar  
- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091v1)**  
  Authors: Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22091v1.pdf)  
  Keywords: slam, head, mapping, robotics, ar, sparse-view, gaussian splatting, high-fidelity, geometry, 3d gaussian, fast, lightweight  
- **[From Uncertainty to Stability and Fidelity: Guiding Sparse-View 3D Gaussian Splatting with Fisher Information](https://arxiv.org/abs/2606.20842v1)**  
  Authors: Junbao Zhou, Qingshan Xu, Yuan Zhou, Xiaolong Shen, Beier Zhu, Kesen Zhao, Yiming Zeng, Chen Bai, Cheng Lu, Hanwang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.20842v1.pdf)  
  Keywords: sparse-view, gaussian splatting, 3d gaussian, ar  
- **[VisDom: Sparse Novel View Synthesis with Visible Domain Constraint](https://arxiv.org/abs/2606.20531v1)**  
  Authors: Mariia Gladkova*, Tarun Yenamandra*, Edmond Boyer, Robert Maier, Tony Tung, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.20531v1.pdf)  
  Keywords: nerf, sparse-view, gaussian splatting, geometry, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 214 papers*

- **[World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video](https://arxiv.org/abs/2607.01202v1)**  
  Authors: Liyuan Zhu, Shengyu Huang, Amrita Mazumdar, Tianye Li, Zan Gojcic, Gordon Wetzstein, Iro Armeni, Shalini De Mello, Alex Trevithick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01202v1.pdf)  
  Keywords: 4d, motion, geometry, dynamic, 3d gaussian, ar  
- **[FastBridge: Closing the Model-Based Realization Gap in Safety Filters on 3D Gaussian Splatting for Fast Quadrotor Flight](https://arxiv.org/abs/2607.01200v1)**  
  Authors: Tscholl Dario, Nakka Yashwanth Kumar, Gunter Brian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01200v1.pdf)  
  Keywords: acceleration, gaussian splatting, geometry, dynamic, 3d gaussian, fast, ar  
- **[Efficient Compression of Structured and Unstructured Volumes via Learned 3D Gaussian Representation](https://arxiv.org/abs/2607.01164v1)**  
  Authors: Landon Dyken, Sharmistha Chakrabarti, Nathan Debardeleben, Steve Petruzza, Qi Wu, Will Usher, Sidharth Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01164v1.pdf)  
  Keywords: compression, efficient, geometry, 3d gaussian, ar  
- **[Pano2World: End-to-End 3D Generation via Unified Multi-View Sequences](https://arxiv.org/abs/2607.00832v1)**  
  Authors: Zhenjia Li, Jinrang Jia, Yifeng Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00832v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, semantic  
- **[GADA: Geometry-Aware Deformable Aggregation for Image-Based Gaussian Splatting](https://arxiv.org/abs/2607.00595v1)**  
  Authors: Siwoo Lim, Sunjae Yoon, Gwanhyeong Koo, Chang D. Yoo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00595v1.pdf)  
  Keywords: geometry, gaussian splatting, fast, ar  
- **[NoPA: Non-Parametric Online 3D Scene Graph Generation](https://arxiv.org/abs/2607.00529v1)**  
  Authors: Qi Xun Yeo, Seungjun Lee, Yan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00529v1.pdf)  
  Keywords: mapping, lightweight, geometry, 3d gaussian, ar  
- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: compact, ar, gaussian splatting, geometry, ray casting, human  
- **[AugSplat: Radiance Field-Informed Gaussian Splatting for Sparse-View Settings](https://arxiv.org/abs/2606.31556v1)**  
  Authors: Lorenzo Lazzaroni, Riccardo Bollati, Daniel Barath, Michael Niemeyer, Keisuke Tateno  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31556v1.pdf)  
  Keywords: real-time rendering, nerf, sparse-view, gaussian splatting, geometry, ar  
- **[Learning Video Dynamics with Predictive Differentiable Rendering](https://arxiv.org/abs/2606.31050v1)**  
  Authors: Yujin Tang, Tian Zhou, Xin Lin, Cheng Tan, Yifan Hu, Rong Jin, SouYoung Jin, Liang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31050v1.pdf)  
  Keywords: head, 3d reconstruction, human, ar, gaussian splatting, high-fidelity, dynamic, 3d gaussian, fast, lightweight  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: real-time rendering, reflection, geometry, ray tracing, efficient, gaussian splatting, path tracing, 3d gaussian, fast, ar  

### Large Scene

- **[Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673v1)**  
  Authors: Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu, Krishna Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00673v1.pdf)  
  Keywords: outdoor, deformation, 3d gaussian, human, ar  
- **[GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping](https://arxiv.org/abs/2606.30809v1)**  
  Authors: Annika Thomas, Mason Peterson, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30809v1.pdf)  
  Keywords: mapping, outdoor, gaussian splatting, geometry, 3d gaussian, ar  
- **[Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes](https://arxiv.org/abs/2606.30436v1)**  
  Authors: Sicheng Yu, Dongxu Shen, Beizhen Zhao, Guanzhi Ding, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30436v1.pdf)  
  Keywords: slam, head, tracking, mapping, outdoor, efficient, motion, gaussian splatting, high-fidelity, dynamic, 3d gaussian, ar  
- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)**  
  Authors: Leshu Li, Jie Peng, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/UMN-ZhaoLab/Pocket-SLAM.git?style=social)](https://github.com/UMN-ZhaoLab/Pocket-SLAM.git)  
  Keywords: slam, mapping, outdoor, efficient, face, gaussian splatting, autonomous driving, geometry, 3d gaussian, localization, ar  
- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031v1)**  
  Authors: Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23031v1.pdf)  
  Keywords: efficient, large scene, urban scene, gaussian splatting, high-fidelity, geometry, dynamic, 3d gaussian, fast, ar  
- **[Point-Cloud-Assistant Localized Statistical Channel Prediction by Tangent Gaussian Splatting](https://arxiv.org/abs/2606.18734v1)**  
  Authors: Ye Xue, Yiheng Wang, Xinhua Shao, Qi Yan, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.18734v1.pdf)  
  Keywords: outdoor, efficient, gaussian splatting, geometry, 3d gaussian, fast, ar  
- **[MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization](https://arxiv.org/abs/2606.17935v1)**  
  Authors: Guo Pu, Yixuan Han, Haofeng Li, Yao Zhang, Hui Zhou, Zhouhui Lian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17935v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TrickyGo/MoonSplat?style=social)](https://github.com/TrickyGo/MoonSplat)  
  Keywords: real-time rendering, tracking, outdoor, efficient, robotics, 3d reconstruction, gaussian splatting, vr, 3d gaussian, ar  
- **[KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis](https://arxiv.org/abs/2606.03120v1)**  
  Authors: Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.03120v1.pdf)  
  Keywords: outdoor, efficient, nerf, gaussian splatting, high-fidelity, sparse-view, 3d gaussian, ar  
- **[City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.30310v1)**  
  Authors: Sayan Paul, Sourav Ghosh, Siddharth Katageri, Soumyadip Maity, Sanjana Sinha, Brojeshwar Bhowmick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30310v1.pdf)  
  Keywords: 3d reconstruction, large scene, nerf, face, urban scene, gaussian splatting, high-fidelity, geometry, ar  
- **[GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction](https://arxiv.org/abs/2605.23888v1)**  
  Authors: Katharina Schmid, Nicolas von Lützow, Jozef Hladký, Angela Dai, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.23888v1.pdf)  
  Keywords: geometry, large scene, high-fidelity, ar  

### Model Compression

*Showing the latest 50 out of 191 papers*

- **[Efficient Compression of Structured and Unstructured Volumes via Learned 3D Gaussian Representation](https://arxiv.org/abs/2607.01164v1)**  
  Authors: Landon Dyken, Sharmistha Chakrabarti, Nathan Debardeleben, Steve Petruzza, Qi Wu, Will Usher, Sidharth Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01164v1.pdf)  
  Keywords: compression, efficient, geometry, 3d gaussian, ar  
- **[Relation-Centric Open-Vocabulary 3D Gaussian Segmentation](https://arxiv.org/abs/2607.01140v1)**  
  Authors: Eunsung Cha, Hyunjoon Lee, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01140v1.pdf)  
  Keywords: efficient, understanding, segmentation, 3d gaussian, fast, ar  
- **[Improving Sparse-View 3DGS Generalization via Flat Minima Optimization](https://arxiv.org/abs/2607.00885v1)**  
  Authors: Kangmin Seo, Sangeek Hyun, MinKyu Lee, Jae-Pil Heo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00885v1.pdf)  
  Keywords: real-time rendering, neural rendering, efficient, nerf, ar, gaussian splatting, sparse-view, dynamic, 3d gaussian, fast, lightweight  
- **[NoPA: Non-Parametric Online 3D Scene Graph Generation](https://arxiv.org/abs/2607.00529v1)**  
  Authors: Qi Xun Yeo, Seungjun Lee, Yan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00529v1.pdf)  
  Keywords: mapping, lightweight, geometry, 3d gaussian, ar  
- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: compact, ar, gaussian splatting, geometry, ray casting, human  
- **[Learning Video Dynamics with Predictive Differentiable Rendering](https://arxiv.org/abs/2606.31050v1)**  
  Authors: Yujin Tang, Tian Zhou, Xin Lin, Cheng Tan, Yifan Hu, Rong Jin, SouYoung Jin, Liang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31050v1.pdf)  
  Keywords: head, 3d reconstruction, human, ar, gaussian splatting, high-fidelity, dynamic, 3d gaussian, fast, lightweight  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: real-time rendering, reflection, geometry, ray tracing, efficient, gaussian splatting, path tracing, 3d gaussian, fast, ar  
- **[Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes](https://arxiv.org/abs/2606.30436v1)**  
  Authors: Sicheng Yu, Dongxu Shen, Beizhen Zhao, Guanzhi Ding, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30436v1.pdf)  
  Keywords: slam, head, tracking, mapping, outdoor, efficient, motion, gaussian splatting, high-fidelity, dynamic, 3d gaussian, ar  
- **[RenderFormer++: Scalable and Physically Grounded Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v1)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jinyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v1.pdf)  
  Keywords: illumination, neural rendering, global illumination, compact, light transport, ar  
- **[FastPano3D: Feed-Forward Indoor Panoramic 3D Reconstruction from a Single Image](https://arxiv.org/abs/2606.30352v1)**  
  Authors: Jianqiang Li, Liumei Zhang, Wenjia Guo, Tianlong Feng, Yongzhi Liao, Di Lu, Hanchi Ren, Jingjing Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30352v1.pdf)  
  Keywords: efficient, 3d reconstruction, nerf, ar, gaussian splatting, high-fidelity, 3d gaussian, fast, lightweight  

### Quality Enhancement

*Showing the latest 50 out of 118 papers*

- **[GaussianEmoTalker: Real-Time Emotional Talking Head Synthesis with Audio-Driven and Blendshape-Based 3D Gaussian Splatting](https://arxiv.org/abs/2607.00959v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Yixuan Dong, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00959v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://njust-yang.github.io/GaussianEmoTalker.github.io)  
  Keywords: head, real-time rendering, avatar, motion, gaussian splatting, animation, high-fidelity, deformation, 3d gaussian, ar  
- **[CORGI: Consistency-Aware 3D Dog Reconstruction from a Single Image in the Wild](https://arxiv.org/abs/2607.00321v1)**  
  Authors: Yuxiao Wu, Weile Li, Boyi Zhu, Yumeng Liu, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00321v1.pdf)  
  Keywords: deformation, high-fidelity, ar  
- **[Progressive Pose-Guided 4D Animal Reconstruction from Monocular Video](https://arxiv.org/abs/2607.00157v1)**  
  Authors: Siyuan Li, Weiying Chen, Yilin Wang, Xinxin Zuo, Xingyu Li, Li Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00157v1.pdf)  
  Keywords: 4d, gaussian splatting, deformation, high-fidelity, 3d gaussian, ar  
- **[Practical High-Fidelity Novel-View Synthesis of Mounted Lepidoptera](https://arxiv.org/abs/2606.31679v1)**  
  Authors: Kristof Overdulve, Lode Jorissen, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31679v1.pdf)  
  Keywords: face, body, gaussian splatting, high-fidelity, segmentation, 3d gaussian, ar  
- **[Learning Video Dynamics with Predictive Differentiable Rendering](https://arxiv.org/abs/2606.31050v1)**  
  Authors: Yujin Tang, Tian Zhou, Xin Lin, Cheng Tan, Yifan Hu, Rong Jin, SouYoung Jin, Liang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31050v1.pdf)  
  Keywords: head, 3d reconstruction, human, ar, gaussian splatting, high-fidelity, dynamic, 3d gaussian, fast, lightweight  
- **[Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes](https://arxiv.org/abs/2606.30436v1)**  
  Authors: Sicheng Yu, Dongxu Shen, Beizhen Zhao, Guanzhi Ding, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30436v1.pdf)  
  Keywords: slam, head, tracking, mapping, outdoor, efficient, motion, gaussian splatting, high-fidelity, dynamic, 3d gaussian, ar  
- **[FastPano3D: Feed-Forward Indoor Panoramic 3D Reconstruction from a Single Image](https://arxiv.org/abs/2606.30352v1)**  
  Authors: Jianqiang Li, Liumei Zhang, Wenjia Guo, Tianlong Feng, Yongzhi Liao, Di Lu, Hanchi Ren, Jingjing Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30352v1.pdf)  
  Keywords: efficient, 3d reconstruction, nerf, ar, gaussian splatting, high-fidelity, 3d gaussian, fast, lightweight  
- **[FFAvatar: Feed-Forward 4D Head Avatar Reconstruction from Sparse Portrait Images](https://arxiv.org/abs/2606.30347v1)**  
  Authors: Jianjiang Yao, Ke Xian, Renxiang Dai, Robert Caiming Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30347v1.pdf)  
  Keywords: head, avatar, 4d, efficient, motion, high-fidelity, deformation, dynamic, 3d gaussian, fast, ar  
- **[Monte Carlo Energy Aggregation for Mobile 3D Gaussian Splatting](https://arxiv.org/abs/2606.30017v1)**  
  Authors: Xiaobiao Du, YuAn Wang, Hao Li, Bosheng Wang, Xun Sun, Xin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30017v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiaobiaodu.github.io/flux-gs-project)  
  Keywords: compression, head, lighting, compact, gaussian splatting, high-fidelity, 3d gaussian, ar  
- **[MyGO-Splat: Multi-Objective Closed-Loop Geometric Feedback for RGB-Only Gaussian SLAM](https://arxiv.org/abs/2606.29738v1)**  
  Authors: Fan Zhu, Ziyu Chen, Zhenjun Zhao, Zhisong Xu, Hui Zhu, Mingrui Li, Chunmao Jiang, Javier Civera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29738v1.pdf)  
  Keywords: slam, tracking, mapping, face, gaussian splatting, high-fidelity, geometry, 3d gaussian, localization, ar  

### Ray Tracing

- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: compact, ar, gaussian splatting, geometry, ray casting, human  
- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869v1)**  
  Authors: Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30869v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gray)  
  Keywords: ray tracing, gaussian splatting, 3d gaussian, fast, ar  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: real-time rendering, reflection, geometry, ray tracing, efficient, gaussian splatting, path tracing, 3d gaussian, fast, ar  
- **[RenderFormer++: Scalable and Physically Grounded Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v1)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jinyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v1.pdf)  
  Keywords: illumination, neural rendering, global illumination, compact, light transport, ar  
- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: illumination, global illumination, efficient, 3d reconstruction, gaussian splatting, geometry, 3d gaussian, ar  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: illumination, global illumination, gaussian splatting, high-fidelity, ar  
- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314v1)**  
  Authors: Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11314v1.pdf)  
  Keywords: lighting, neural rendering, ray tracing, relighting, 3d reconstruction, ar, motion, light transport, geometry, dynamic, 3d gaussian, lightweight  
- **[PTIR-GS: Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606v3)**  
  Authors: Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09606v3.pdf)  
  Keywords: illumination, reflection, lighting, ray tracing, relighting, global illumination, shadow, compact, light transport, path tracing, 3d gaussian, ar  
- **[RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation](https://arxiv.org/abs/2606.01261v1)**  
  Authors: Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.01261v1.pdf)  
  Keywords: reflection, ray tracing, efficient, semantic, gaussian splatting, segmentation, geometry, 3d gaussian, ar  
- **[Directed Distance Fields for Constant-Time Ray Queries on Gaussian Splatting](https://arxiv.org/abs/2606.00817v1)**  
  Authors: Subhankar MIshra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00817v1.pdf) | [![GitHub](https://img.shields.io/github/stars/smlab-niser/ddf-gs?style=social)](https://github.com/smlab-niser/ddf-gs)  
  Keywords: illumination, shadow, global illumination, face, gaussian splatting, 3d gaussian, fast, ar  

### Relighting

*Showing the latest 50 out of 57 papers*

- **[DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918v1)**  
  Authors: Junzhe Jiang, Zipei Ma, Zijie Pan, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31918v1.pdf)  
  Keywords: real-time rendering, lighting, autonomous driving, 3d gaussian, ar  
- **[Intrinsic decomposition and editing of 3D Gaussian splats](https://arxiv.org/abs/2606.31637v1)**  
  Authors: Alexandre Lanvin, Jeffrey Hu, Simon Lucas, Adrien Bousseau, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31637v1.pdf)  
  Keywords: lighting, face, gaussian splatting, 3d gaussian, ar  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: real-time rendering, reflection, geometry, ray tracing, efficient, gaussian splatting, path tracing, 3d gaussian, fast, ar  
- **[RenderFormer++: Scalable and Physically Grounded Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v1)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jinyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v1.pdf)  
  Keywords: illumination, neural rendering, global illumination, compact, light transport, ar  
- **[Monte Carlo Energy Aggregation for Mobile 3D Gaussian Splatting](https://arxiv.org/abs/2606.30017v1)**  
  Authors: Xiaobiao Du, YuAn Wang, Hao Li, Bosheng Wang, Xun Sun, Xin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30017v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiaobiaodu.github.io/flux-gs-project)  
  Keywords: compression, head, lighting, compact, gaussian splatting, high-fidelity, 3d gaussian, ar  
- **[Shell-Supervised Gaussian Splatting for Urban Real-to-Sim Reconstruction](https://arxiv.org/abs/2606.30014v1)**  
  Authors: Yuan Yang, Peijun Lu, Fangzhou Lu, Sai Fan, Siqi Yan, Chenyuan Zhang, Haobo Liang, Yichen Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30014v1.pdf)  
  Keywords: reflection, 3d reconstruction, face, ar, gaussian splatting, geometry, lightweight  
- **[DR-GS: Physically-Based Deformable and Relightable 2D Gaussians](https://arxiv.org/abs/2606.29379v1)**  
  Authors: Jiaxin Li, Tong Wu, Yi Wei, Tailin Wu, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29379v1.pdf)  
  Keywords: illumination, reflection, lighting, relighting, efficient, efficient rendering, face, gaussian splatting, vr, deformation, geometry, dynamic, relightable, ar  
- **[RAGA: Real Time Ray Traced Gaussian Shadow Casting for 3DGS Avatar-Scene Interaction](https://arxiv.org/abs/2606.29329v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Jian Wang, Peter Wonka, Bing Zhou, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29329v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/raga)  
  Keywords: shadow, avatar, gaussian splatting, deformation, 3d gaussian, ar  
- **[RefGlass-GS: A UAV-Enabled Fusion Framework for Photorealistic, Semantic and Interactive Digitization of Reflective Glass Facades via Gaussian Splatting](https://arxiv.org/abs/2606.28826v1)**  
  Authors: Zhenyu Liang, Xiao Zhang, Boyu Wang, Zhaolun Liang, Ang Li, Jeff Chak Fu Chan, Mingzhu Wang, Jack C. P. Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.28826v1.pdf)  
  Keywords: reflection, semantic, gaussian splatting, segmentation, ar  
- **[AEGIR: Modeling Area Emitters for Indoor Inverse Rendering using Gaussian Splatting](https://arxiv.org/abs/2606.28635v2)**  
  Authors: Mohamed Shawky Sabae, Philipp Langsteiner, Jan-Niklas Dihlmann, Hendrik Lensch  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.28635v2.pdf)  
  Keywords: illumination, lighting, shadow, relighting, efficient, face, light transport, gaussian splatting, geometry, relightable, ar  

### SLAM

*Showing the latest 50 out of 76 papers*

- **[NoPA: Non-Parametric Online 3D Scene Graph Generation](https://arxiv.org/abs/2607.00529v1)**  
  Authors: Qi Xun Yeo, Seungjun Lee, Yan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00529v1.pdf)  
  Keywords: mapping, lightweight, geometry, 3d gaussian, ar  
- **[GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping](https://arxiv.org/abs/2606.30809v1)**  
  Authors: Annika Thomas, Mason Peterson, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30809v1.pdf)  
  Keywords: mapping, outdoor, gaussian splatting, geometry, 3d gaussian, ar  
- **[VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes](https://arxiv.org/abs/2606.30645v1)**  
  Authors: Yen-Jen Wang, Jiaman Li, Sirui Chen, Takara E. Truong, Pei Xu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, Karen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30645v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vision-language-kinematics.github.io)  
  Keywords: mapping, ar, motion, body, gaussian splatting, 3d gaussian, human  
- **[Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes](https://arxiv.org/abs/2606.30436v1)**  
  Authors: Sicheng Yu, Dongxu Shen, Beizhen Zhao, Guanzhi Ding, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30436v1.pdf)  
  Keywords: slam, head, tracking, mapping, outdoor, efficient, motion, gaussian splatting, high-fidelity, dynamic, 3d gaussian, ar  
- **[FalconTrack: Photorealistic Auto-Labeled Perception and Physics-Aware Vision-Based Aerial Tracking](https://arxiv.org/abs/2606.29783v1)**  
  Authors: Yan Miao, Karteek Gandiboyina, Noah Giles, Hideki Okamoto, Bardh Hoxha, Georgios Fainekos, Sayan Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29783v1.pdf)  
  Keywords: head, tracking, gaussian splatting, dynamic, fast, ar  
- **[Graph-GSReg: Leveraging 3D Scene Graphs for Gaussian Splatting Registration](https://arxiv.org/abs/2606.29782v1)**  
  Authors: Jaewon Lee, Mangyu Kong, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29782v1.pdf)  
  Keywords: mapping, semantic, understanding, gaussian splatting, 3d gaussian, ar  
- **[MyGO-Splat: Multi-Objective Closed-Loop Geometric Feedback for RGB-Only Gaussian SLAM](https://arxiv.org/abs/2606.29738v1)**  
  Authors: Fan Zhu, Ziyu Chen, Zhenjun Zhao, Zhisong Xu, Hui Zhu, Mingrui Li, Chunmao Jiang, Javier Civera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29738v1.pdf)  
  Keywords: slam, tracking, mapping, face, gaussian splatting, high-fidelity, geometry, 3d gaussian, localization, ar  
- **[VCS-SLAM: Geometry-Validated Semantic Evidence Fusion for 3D Gaussian SLAM](https://arxiv.org/abs/2606.29494v1)**  
  Authors: Raman Jha, Shuaihang Yuan, Yi Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29494v1.pdf)  
  Keywords: slam, tracking, mapping, semantic, face, geometry, 3d gaussian, ar  
- **[MoPe: Motion Permanence for Robust Monocular Gaussian Mapping in Dynamic Environments](https://arxiv.org/abs/2606.29237v1)**  
  Authors: Qixin Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29237v1.pdf)  
  Keywords: slam, tracking, mapping, ar, motion, gaussian splatting, high-fidelity, geometry, dynamic, localization, human  
- **[Articulating then Matching: Zero-Shot Shape Matching for Uncurated Data](https://arxiv.org/abs/2606.29167v1)**  
  Authors: Qilong Liu, Qinfeng Xiao, Chenyuan Yi, Liying Zhang, Kit-lun Yick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29167v1.pdf)  
  Keywords: 3d gaussian, mapping, ar  

### Scene Understanding

*Showing the latest 50 out of 118 papers*

- **[Relation-Centric Open-Vocabulary 3D Gaussian Segmentation](https://arxiv.org/abs/2607.01140v1)**  
  Authors: Eunsung Cha, Hyunjoon Lee, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01140v1.pdf)  
  Keywords: efficient, understanding, segmentation, 3d gaussian, fast, ar  
- **[DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors](https://arxiv.org/abs/2607.00889v1)**  
  Authors: Seok-Young Kim, Abdelrahman Elskhawy, Taewook Ha, Dooyoung Kim, Eunjae Shin, Benjamin Busam, Woontack Woo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00889v1.pdf)  
  Keywords: 3d gaussian, ar, semantic  
- **[Pano2World: End-to-End 3D Generation via Unified Multi-View Sequences](https://arxiv.org/abs/2607.00832v1)**  
  Authors: Zhenjia Li, Jinrang Jia, Yifeng Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00832v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, semantic  
- **[GaussianFusion: Unified 3D Gaussian Representation for Multi-Modal Fusion Perception](https://arxiv.org/abs/2607.00746v1)**  
  Authors: Xiao Zhao, Chang Liu, Mingxu Zhu, Zheyuan Zhang, Linna Song, Qingliang Luo, Chufan Guo, Kuifeng Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00746v1.pdf)  
  Keywords: 3d gaussian, ar, semantic  
- **[Practical High-Fidelity Novel-View Synthesis of Mounted Lepidoptera](https://arxiv.org/abs/2606.31679v1)**  
  Authors: Kristof Overdulve, Lode Jorissen, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31679v1.pdf)  
  Keywords: face, body, gaussian splatting, high-fidelity, segmentation, 3d gaussian, ar  
- **[Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors](https://arxiv.org/abs/2606.30638v1)**  
  Authors: Jameel Hassan, Yasiru Ranasinghe, Vishal Patel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30638v1.pdf)  
  Keywords: semantic, understanding, gaussian splatting, segmentation, 3d gaussian, ar  
- **[Graph-GSReg: Leveraging 3D Scene Graphs for Gaussian Splatting Registration](https://arxiv.org/abs/2606.29782v1)**  
  Authors: Jaewon Lee, Mangyu Kong, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29782v1.pdf)  
  Keywords: mapping, semantic, understanding, gaussian splatting, 3d gaussian, ar  
- **[Scenes as Objects, Not Primitives: Instance-Structured 3D Tokenization from Unposed Views](https://arxiv.org/abs/2606.29513v1)**  
  Authors: Mijin Yoo, In Cho, Subin Jeon, Jiwoo Lee, Eunbyung Park, Seon Joo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29513v1.pdf)  
  Keywords: efficient, compact, face, segmentation, geometry, 3d gaussian, ar  
- **[Rectifying Mask via Entropy for Distractor-Free 3DGS in Ambiguous Scenarios](https://arxiv.org/abs/2606.29496v1)**  
  Authors: Wongi Park, Jiyeon Lim, Minjae Lee, Myeongseok Nam, Seongjun Choi, Jungwoo Kim, Soomok Lee, William J. Beksi, SangHyun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29496v1.pdf)  
  Keywords: ar, semantic  
- **[VCS-SLAM: Geometry-Validated Semantic Evidence Fusion for 3D Gaussian SLAM](https://arxiv.org/abs/2606.29494v1)**  
  Authors: Raman Jha, Shuaihang Yuan, Yi Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29494v1.pdf)  
  Keywords: slam, tracking, mapping, semantic, face, geometry, 3d gaussian, ar  



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