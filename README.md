# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-06-16 02:44:45

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
- [Acceleration](#acceleration) (83 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (172 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (188 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (45 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (211 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (19 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (194 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (117 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (14 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (59 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (75 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (112 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: compact, autonomous driving, neural rendering, ar, vr, medical, recognition, motion, gaussian splatting, 3d reconstruction, 4d, survey, 3d gaussian  
- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137v1)**  
  Authors: Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00137v1.pdf)  
  Keywords: ar, geometry, animation, mapping, gaussian splatting, survey  
- **[ReefMapGS: Enabling Large-Scale Underwater Reconstruction by Closing the Loop Between Multimodal SLAM and Gaussian Splatting](https://arxiv.org/abs/2604.11992v1)**  
  Authors: Daniel Yang, Jungseok Hong, John J. Leonard, Yogesh Girdhar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11992v1.pdf)  
  Keywords: efficient, ar, geometry, tracking, motion, slam, gaussian splatting, 3d reconstruction, survey, 3d gaussian  
- **[A Survey of Spatial Memory Representations for Efficient Robot Navigation](https://arxiv.org/abs/2604.16482v1)**  
  Authors: Ma. Madecheen S. Pangaliman, Steven S. Sison, Erwin P. Quilloy, Rowel Atienza  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.16482v1.pdf)  
  Keywords: efficient, ar, semantic, slam, survey  

### Acceleration

*Showing the latest 50 out of 83 papers*

- **[TurboGS: Accelerating 3D Gaussian Splatting via Error-Guided Sparse Pixel Sampling and Optimization](https://arxiv.org/abs/2606.15924v1)**  
  Authors: Zheng Dong, Daifei Qiu, Pinxuan Dai, Ke Xu, Jiamin Xu, Lili He, Rynson W. H. Lau, Weiwei Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.15924v1.pdf)  
  Keywords: acceleration, fast, ar, dynamic, gaussian splatting, high-fidelity, 3d gaussian  
- **[Seeing What Matters: Perceptual Wrapper with Common Randomness for 3D Gaussian Splatting](https://arxiv.org/abs/2606.11782v1)**  
  Authors: He-Bi Yang, Jing-Zhong Chen, Yen-Kuan Ho, Sang NguyenQuang, Fan-Yi Hsu, Yun-Yu Lee, Jui-Chiu Chiang, Wen-Hsiao Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11782v1.pdf)  
  Keywords: ar, lightweight, real-time rendering, gaussian splatting, 3d gaussian  
- **[XPR: An Extensible Cross-Platform Point-Based Differentiable Renderer](https://arxiv.org/abs/2606.11529v1)**  
  Authors: Steve Rhyner, Sankeerth Durvasula, Aleksandr Kovalev, Hansel Jia, Adrian Zhao, Mrutunjayya Mrutunjayya, Nilesh Ahuja, Selvakumar Panneer, Christina Giannoula, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11529v1.pdf)  
  Keywords: 3d reconstruction, face, ar, fast  
- **[Leveraging NeRF-Rendered Images for 3D Gaussian Splatting](https://arxiv.org/abs/2606.09034v1)**  
  Authors: Mizuki Morikawa, Yuta Shimizu, Chunyu Li, Yusuke Monno, Masatoshi Okutomi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09034v1.pdf)  
  Keywords: ar, fast, nerf, gaussian splatting, 3d gaussian  
- **[LEGS: Laplacian-Enhanced Gaussian Splatting with a Nonlinear Weighted Loss](https://arxiv.org/abs/2606.07932v1)**  
  Authors: Yongfei Guo, Qizhou Huo, Xuan Sun, Yuanhao Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.07932v1.pdf)  
  Keywords: efficient, ar, fast, vr, nerf, gaussian splatting, 3d gaussian  
- **[GS-NFS: Bandwidth-adaptive Streaming of Dynamic Gaussian Splats and Point Clouds](https://arxiv.org/abs/2606.05650v1)**  
  Authors: Rajrup Ghosh, Haodong Wang, Haoran Hong, Eduardo Pavez, Amartya Chaudhuri, Weiwu Pang, Harsha V. Madhyastha, Antonio Ortega, Ramesh Govindan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.05650v1.pdf)  
  Keywords: efficient, acceleration, fast, ar, dynamic, compression, gaussian splatting, 3d gaussian  
- **[MLP Splatting: Object-Centric Neural Fields](https://arxiv.org/abs/2606.03877v1)**  
  Authors: Shinjeong Kim, Yuzhou Cheng, Xin Kong, Paul H. J. Kelly, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.03877v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shinjeongkim.com/mlp-splatting)  
  Keywords: efficient, compact, understanding, fast, ar, semantic, segmentation, gaussian splatting, 3d gaussian  
- **[VEDAL: Variational Error-Driven Asynchronous Learning for 3D Gaussian Splatting Pruning](https://arxiv.org/abs/2606.02346v1)**  
  Authors: Aoduo Li, Jiancheng Li, Huan Ye, Hongjian Xu, Shiting Wu, Xiujun Zhang, Zimeng Li, Xuhang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.02346v1.pdf)  
  Keywords: ar, head, nerf, compression, real-time rendering, gaussian splatting, 3d gaussian  
- **[WebSpline: Structure-Informed Splines for Real-Time 3D Gaussians from Monocular Videos](https://arxiv.org/abs/2606.02096v1)**  
  Authors: Jongmin Park, Jeonghwan Yun, Minh-Quan Viet Bui, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.02096v1.pdf)  
  Keywords: ar, fast, dynamic, motion, high-fidelity, 3d gaussian  
- **[Fast and Lightweight Novel View Synthesis with Differentiable Multiplane Image](https://arxiv.org/abs/2606.02068v1)**  
  Authors: Kaidi Zhang, Guanxu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.02068v1.pdf)  
  Keywords: efficient, compact, ar, fast, sparse-view, nerf, lightweight, gaussian splatting, 3d gaussian  

### Applications

*Showing the latest 50 out of 498 papers*

- **[MVM-IOD: An Industrial Object-Centric Benchmark Dataset for the Evaluation of 3D Reconstruction Methods](https://arxiv.org/abs/2606.16638v1)**  
  Authors: Robert Langendörfer, Markus Hillemann, Markus Ulrich  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16638v1.pdf)  
  Keywords: ar, geometry, motion, gaussian splatting, 3d reconstruction  
- **[Local-GS: Accelerating 3D Gaussian Splatting via Tile-Local Warp Coherence](https://arxiv.org/abs/2606.16566v1)**  
  Authors: Yang Luo, Yan Gong, Yongsheng Gao, Jie Zhao, Xinyu Zhang, Huaping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16566v1.pdf)  
  Keywords: ar, geometry, gaussian splatting, 3d gaussian  
- **[RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos](https://arxiv.org/abs/2606.16278v1)**  
  Authors: Zhenhua Wu, Yun Pang, Mingkun Chang, Yuwei Ning, Liangzhi Wang, Yi Xiao, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16278v1.pdf)  
  Keywords: illumination, autonomous driving, ar, semantic, lightweight, gaussian splatting, 3d gaussian  
- **[PolyMerge: Compressing 3D Gaussian Splats with Polytope Coverings for Provably Safe Resource-Constrained Navigation](https://arxiv.org/abs/2606.16232v1)**  
  Authors: Jihoon Hong, Chih-Yuan Chiu, Sara Fridovich-Keil, Glen Chou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://athlon76.github.io/PolyMerge-website)  
  Keywords: ar, lightweight, motion, gaussian splatting, 3d gaussian  
- **[Fi-Gaussian: Frequency-Aware Implicit Gaussian Splatting for Single Image Dehazing](https://arxiv.org/abs/2606.16168v1)**  
  Authors: Yuhan Chen, Ying Fang, Guofa Li, Wenxuan Yu, Yicui Shi, Kunyang Huang, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16168v1.pdf)  
  Keywords: ar, gaussian splatting  
- **[Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation](https://arxiv.org/abs/2606.16163v1)**  
  Authors: Yuhan Chen, Wenxuan Yu, Guofa Li, Kunyang Huang, Ying Fang, Yicui Shi, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16163v1.pdf)  
  Keywords: efficient, ar, lighting, dynamic, gaussian splatting  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: illumination, ar, global illumination, gaussian splatting, high-fidelity  
- **[TurboGS: Accelerating 3D Gaussian Splatting via Error-Guided Sparse Pixel Sampling and Optimization](https://arxiv.org/abs/2606.15924v1)**  
  Authors: Zheng Dong, Daifei Qiu, Pinxuan Dai, Ke Xu, Jiamin Xu, Lili He, Rynson W. H. Lau, Weiwei Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.15924v1.pdf)  
  Keywords: acceleration, fast, ar, dynamic, gaussian splatting, high-fidelity, 3d gaussian  
- **[EmoZone-Talker: Regional Semantic Control of Audio-Driven 3DGS Talking Heads via Facial Action Units](https://arxiv.org/abs/2606.15848v1)**  
  Authors: Tingting Chen, Shaojun Wang, Huaye Zhang, Diqiong Jiang, Chenglizhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.15848v1.pdf)  
  Keywords: face, ar, head, animation, semantic, dynamic, motion, gaussian splatting, deformation, high-fidelity, 3d gaussian  
- **[SpatialAvatar-0: High-Quality 4D Head Avatar with Multi-Stage Reconstruction](https://arxiv.org/abs/2606.15659v1)**  
  Authors: Yiran Wang, Zeyu Zhang, Yuanming Li, Ziming Wang, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.15659v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://spatialwalk.github.io/SpatialAvatar-0)  
  Keywords: ar, avatar, vr, head, gaussian splatting, human, 4d, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 172 papers*

- **[EmoZone-Talker: Regional Semantic Control of Audio-Driven 3DGS Talking Heads via Facial Action Units](https://arxiv.org/abs/2606.15848v1)**  
  Authors: Tingting Chen, Shaojun Wang, Huaye Zhang, Diqiong Jiang, Chenglizhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.15848v1.pdf)  
  Keywords: face, ar, head, animation, semantic, dynamic, motion, gaussian splatting, deformation, high-fidelity, 3d gaussian  
- **[SpatialAvatar-0: High-Quality 4D Head Avatar with Multi-Stage Reconstruction](https://arxiv.org/abs/2606.15659v1)**  
  Authors: Yiran Wang, Zeyu Zhang, Yuanming Li, Ziming Wang, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.15659v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://spatialwalk.github.io/SpatialAvatar-0)  
  Keywords: ar, avatar, vr, head, gaussian splatting, human, 4d, 3d gaussian  
- **[SplatlessDF: Continuous Distance Field Mapping with Non-Splatting Gaussians](https://arxiv.org/abs/2606.13990v1)**  
  Authors: Monisha Mushtary Uttsha, Lan Wu, Teresa Vidal-Calleja  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.13990v1.pdf)  
  Keywords: efficient, face, ar, geometry, mapping, gaussian splatting  
- **[Flex4DHuman: Flexible Multi-view Video Diffusion for 4D Human Reconstruction](https://arxiv.org/abs/2606.13655v2)**  
  Authors: Jen-Hao Cheng, Yipeng Wang, Hao Zhang, Gengshan Yang, Jenq-Neng Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.13655v2.pdf)  
  Keywords: ar, geometry, vr, dynamic, gaussian splatting, human, 4d  
- **[XPR: An Extensible Cross-Platform Point-Based Differentiable Renderer](https://arxiv.org/abs/2606.11529v1)**  
  Authors: Steve Rhyner, Sankeerth Durvasula, Aleksandr Kovalev, Hansel Jia, Adrian Zhao, Mrutunjayya Mrutunjayya, Nilesh Ahuja, Selvakumar Panneer, Christina Giannoula, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11529v1.pdf)  
  Keywords: 3d reconstruction, face, ar, fast  
- **[REFINE: Super-efficient 3D Gaussian Splatting Pruning via Rendering-Free Primitive Importance](https://arxiv.org/abs/2606.09074v1)**  
  Authors: Zhang Chen, Shuai Wan, Mengting Yu, Fuzheng Yang, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09074v1.pdf)  
  Keywords: efficient, ar, geometry, head, gaussian splatting, high-fidelity, 3d gaussian  
- **[Wispy to Voluminous: Prior-free Multi-view Capture of Strand-level Facial Hair](https://arxiv.org/abs/2606.08041v1)**  
  Authors: Jaeseong Lee, Giljoo Nam, Adrian Jarabo, Carlos Aliaga  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.08041v1.pdf)  
  Keywords: face, ar, geometry, avatar, head, animation, high-fidelity, 3d gaussian  
- **[RigPAPR: Rig-Based Animation of Static Neural Point Clouds from a Fixed-Viewpoint Video](https://arxiv.org/abs/2606.06685v1)**  
  Authors: Shichong Peng, Yanshu Zhang, Ke Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.06685v1.pdf)  
  Keywords: animation, face, ar  
- **[Self-Learning Expression Deformations for Data-Efficient Gaussian Avatars](https://arxiv.org/abs/2606.05912v1)**  
  Authors: Jiahao Yang, Xiaohang Yang, Qing Wang, Yilan Dong, Gregory Slabaugh, Shanxin Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.05912v1.pdf)  
  Keywords: efficient, compact, face, ar, avatar, head, animation, dynamic, deformation, high-fidelity, 3d gaussian  
- **[Geometry Gaussians: Decoupling Appearance and Geometry in Gaussian Splatting](https://arxiv.org/abs/2606.05124v1)**  
  Authors: Hongyu Zhou, Zorah Lähner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.05124v1.pdf)  
  Keywords: face, ar, geometry, gaussian splatting, 3d gaussian  

### Dynamic Scene

*Showing the latest 50 out of 188 papers*

- **[MVM-IOD: An Industrial Object-Centric Benchmark Dataset for the Evaluation of 3D Reconstruction Methods](https://arxiv.org/abs/2606.16638v1)**  
  Authors: Robert Langendörfer, Markus Hillemann, Markus Ulrich  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16638v1.pdf)  
  Keywords: ar, geometry, motion, gaussian splatting, 3d reconstruction  
- **[PolyMerge: Compressing 3D Gaussian Splats with Polytope Coverings for Provably Safe Resource-Constrained Navigation](https://arxiv.org/abs/2606.16232v1)**  
  Authors: Jihoon Hong, Chih-Yuan Chiu, Sara Fridovich-Keil, Glen Chou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://athlon76.github.io/PolyMerge-website)  
  Keywords: ar, lightweight, motion, gaussian splatting, 3d gaussian  
- **[Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation](https://arxiv.org/abs/2606.16163v1)**  
  Authors: Yuhan Chen, Wenxuan Yu, Guofa Li, Kunyang Huang, Ying Fang, Yicui Shi, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16163v1.pdf)  
  Keywords: efficient, ar, lighting, dynamic, gaussian splatting  
- **[TurboGS: Accelerating 3D Gaussian Splatting via Error-Guided Sparse Pixel Sampling and Optimization](https://arxiv.org/abs/2606.15924v1)**  
  Authors: Zheng Dong, Daifei Qiu, Pinxuan Dai, Ke Xu, Jiamin Xu, Lili He, Rynson W. H. Lau, Weiwei Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.15924v1.pdf)  
  Keywords: acceleration, fast, ar, dynamic, gaussian splatting, high-fidelity, 3d gaussian  
- **[EmoZone-Talker: Regional Semantic Control of Audio-Driven 3DGS Talking Heads via Facial Action Units](https://arxiv.org/abs/2606.15848v1)**  
  Authors: Tingting Chen, Shaojun Wang, Huaye Zhang, Diqiong Jiang, Chenglizhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.15848v1.pdf)  
  Keywords: face, ar, head, animation, semantic, dynamic, motion, gaussian splatting, deformation, high-fidelity, 3d gaussian  
- **[SpatialAvatar-0: High-Quality 4D Head Avatar with Multi-Stage Reconstruction](https://arxiv.org/abs/2606.15659v1)**  
  Authors: Yiran Wang, Zeyu Zhang, Yuanming Li, Ziming Wang, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.15659v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://spatialwalk.github.io/SpatialAvatar-0)  
  Keywords: ar, avatar, vr, head, gaussian splatting, human, 4d, 3d gaussian  
- **[MooMIns -- Monocular 3D Reconstruction and Object Pose Estimation from Multiple Instances](https://arxiv.org/abs/2606.14389v1)**  
  Authors: Robert Langendörfer, Markus Hillemann, Markus Ulrich  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.14389v1.pdf)  
  Keywords: ar, geometry, segmentation, motion, gaussian splatting, 3d reconstruction  
- **[Flex4DHuman: Flexible Multi-view Video Diffusion for 4D Human Reconstruction](https://arxiv.org/abs/2606.13655v2)**  
  Authors: Jen-Hao Cheng, Yipeng Wang, Hao Zhang, Gengshan Yang, Jenq-Neng Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.13655v2.pdf)  
  Keywords: ar, geometry, vr, dynamic, gaussian splatting, human, 4d  
- **[MoVerse: Real-Time Video World Modeling with Panoramic Gaussian Scaffold](https://arxiv.org/abs/2606.13376v1)**  
  Authors: Yang Zhou, Ziheng Wang, Yuqin Lu, Haofeng Liu, Jun Liang, Shengfeng He, Jing Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.13376v1.pdf)  
  Keywords: ar, geometry, motion, high-fidelity, 3d gaussian  
- **[Scene-Adaptive Nonlinear Tone Curves for Pseudo Ground-Truth Generation in Low-Light 3D Gaussian Splatting](https://arxiv.org/abs/2606.11841v1)**  
  Authors: Mingzhe Lyu, Jinqiang Cui, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11841v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lvmingzhe/adaptiveToneCurve?style=social)](https://github.com/lvmingzhe/adaptiveToneCurve)  
  Keywords: ar, dynamic, mapping, gaussian splatting, 3d reconstruction, 3d gaussian  

### Few-shot

- **[KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis](https://arxiv.org/abs/2606.03120v1)**  
  Authors: Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.03120v1.pdf)  
  Keywords: efficient, ar, sparse-view, nerf, gaussian splatting, outdoor, high-fidelity, 3d gaussian  
- **[BEAST3D: Animal behavioral analysis and neural encoding from multi-view video via Gaussian splatting](https://arxiv.org/abs/2606.02937v1)**  
  Authors: Yanchen Wang, Lenny Aharon, Wangshu Zhu, Kyle Daruwalla, Linghua Zhang, Jiaru Zou, Selmaan Chettih, Helen Hou, Liam Paninski, Matthew R Whiteway  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.02937v1.pdf)  
  Keywords: ar, geometry, sparse-view, gaussian splatting, 3d reconstruction, 3d gaussian  
- **[Fast and Lightweight Novel View Synthesis with Differentiable Multiplane Image](https://arxiv.org/abs/2606.02068v1)**  
  Authors: Kaidi Zhang, Guanxu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.02068v1.pdf)  
  Keywords: efficient, compact, ar, fast, sparse-view, nerf, lightweight, gaussian splatting, 3d gaussian  
- **[DeblurNVS: Geometric Latent Diffusion for Novel View Synthesis from Sparse Motion-Blurred Images](https://arxiv.org/abs/2606.01315v1)**  
  Authors: Changyue Shi, Wangbo Yu, Chaoran Feng, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.01315v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PKU-YuanGroup/DeblurNVS?style=social)](https://github.com/PKU-YuanGroup/DeblurNVS)  
  Keywords: efficient, ar, sparse-view, nerf, motion, gaussian splatting, high-fidelity, 3d gaussian  
- **[TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction](https://arxiv.org/abs/2605.26115v1)**  
  Authors: Weijie Wang, Zimu Li, Jinchuan Shi, Zeyu Zhang, Botao Ye, Marc Pollefeys, Donny Y. Chen, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26115v1.pdf)  
  Keywords: face, ar, geometry, head, sparse-view, 3d reconstruction  
- **[F-RNG: Feed-Forward Relightable Neural Gaussians](https://arxiv.org/abs/2605.25975v2)**  
  Authors: Guangming Fu, Jiahui Fan, Jian Yang, Miloš Hašan, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25975v2.pdf)  
  Keywords: illumination, ar, fast, geometry, sparse-view, lighting, gaussian splatting, relighting, high-fidelity, relightable, 3d gaussian  
- **[ArtSplat: Feed-Forward Articulated 3D Gaussian Splatting from Sparse Multi-State Uncalibrated Views](https://arxiv.org/abs/2605.24304v1)**  
  Authors: Inseo Lee, Yoonji Kim, Eugene Sohn, Jiwoong Lee, Jungmin You, Joonseok Lee, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.24304v1.pdf)  
  Keywords: ar, geometry, fast, sparse-view, nerf, motion, gaussian splatting, 3d gaussian  
- **[TWINGS: Thin Plate Splines Warp-aligned Initialization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2605.22069v2)**  
  Authors: Hyeseong Kim, Geonhui Son, Deukhee Lee, Dosik Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.22069v2.pdf)  
  Keywords: ar, fast, sparse-view, nerf, gaussian splatting, deformation, 3d gaussian  
- **[P2GS: Physical Prior-guided Gaussian Splatting for Photometrically Consistent Urban Reconstruction](https://arxiv.org/abs/2605.16925v1)**  
  Authors: Kota Shimomura, Hidehisa Arai, Tsubasa Takahashi, Takayoshi Yamashita, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.16925v1.pdf)  
  Keywords: illumination, autonomous driving, fast, ar, lighting, sparse view, dynamic, mapping, gaussian splatting, outdoor, high-fidelity, 3d gaussian  
- **[FFAvatar: Few-Shot, Feed-Forward, and Generalizable Avatar Reconstruction](https://arxiv.org/abs/2605.15320v1)**  
  Authors: Thuan Hoang Nguyen, Jiahao Luo, Yinyu Nie, Hao Li, Gordon Guocheng Qian, Jian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15320v1.pdf)  
  Keywords: ar, avatar, head, animation, few-shot, high-fidelity, 3d gaussian  

### Geometry Reconstruction

*Showing the latest 50 out of 211 papers*

- **[MVM-IOD: An Industrial Object-Centric Benchmark Dataset for the Evaluation of 3D Reconstruction Methods](https://arxiv.org/abs/2606.16638v1)**  
  Authors: Robert Langendörfer, Markus Hillemann, Markus Ulrich  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16638v1.pdf)  
  Keywords: ar, geometry, motion, gaussian splatting, 3d reconstruction  
- **[Local-GS: Accelerating 3D Gaussian Splatting via Tile-Local Warp Coherence](https://arxiv.org/abs/2606.16566v1)**  
  Authors: Yang Luo, Yan Gong, Yongsheng Gao, Jie Zhao, Xinyu Zhang, Huaping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16566v1.pdf)  
  Keywords: ar, geometry, gaussian splatting, 3d gaussian  
- **[MooMIns -- Monocular 3D Reconstruction and Object Pose Estimation from Multiple Instances](https://arxiv.org/abs/2606.14389v1)**  
  Authors: Robert Langendörfer, Markus Hillemann, Markus Ulrich  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.14389v1.pdf)  
  Keywords: ar, geometry, segmentation, motion, gaussian splatting, 3d reconstruction  
- **[SplatlessDF: Continuous Distance Field Mapping with Non-Splatting Gaussians](https://arxiv.org/abs/2606.13990v1)**  
  Authors: Monisha Mushtary Uttsha, Lan Wu, Teresa Vidal-Calleja  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.13990v1.pdf)  
  Keywords: efficient, face, ar, geometry, mapping, gaussian splatting  
- **[Flex4DHuman: Flexible Multi-view Video Diffusion for 4D Human Reconstruction](https://arxiv.org/abs/2606.13655v2)**  
  Authors: Jen-Hao Cheng, Yipeng Wang, Hao Zhang, Gengshan Yang, Jenq-Neng Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.13655v2.pdf)  
  Keywords: ar, geometry, vr, dynamic, gaussian splatting, human, 4d  
- **[MoVerse: Real-Time Video World Modeling with Panoramic Gaussian Scaffold](https://arxiv.org/abs/2606.13376v1)**  
  Authors: Yang Zhou, Ziheng Wang, Yuqin Lu, Haofeng Liu, Jun Liang, Shengfeng He, Jing Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.13376v1.pdf)  
  Keywords: ar, geometry, motion, high-fidelity, 3d gaussian  
- **[Scene-Adaptive Nonlinear Tone Curves for Pseudo Ground-Truth Generation in Low-Light 3D Gaussian Splatting](https://arxiv.org/abs/2606.11841v1)**  
  Authors: Mingzhe Lyu, Jinqiang Cui, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11841v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lvmingzhe/adaptiveToneCurve?style=social)](https://github.com/lvmingzhe/adaptiveToneCurve)  
  Keywords: ar, dynamic, mapping, gaussian splatting, 3d reconstruction, 3d gaussian  
- **[XPR: An Extensible Cross-Platform Point-Based Differentiable Renderer](https://arxiv.org/abs/2606.11529v1)**  
  Authors: Steve Rhyner, Sankeerth Durvasula, Aleksandr Kovalev, Hansel Jia, Adrian Zhao, Mrutunjayya Mrutunjayya, Nilesh Ahuja, Selvakumar Panneer, Christina Giannoula, Nandita Vijaykumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11529v1.pdf)  
  Keywords: 3d reconstruction, face, ar, fast  
- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314v1)**  
  Authors: Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11314v1.pdf)  
  Keywords: ar, neural rendering, geometry, lighting, lightweight, light transport, dynamic, ray tracing, motion, relighting, 3d reconstruction, 3d gaussian  
- **[WorldOlympiad: Can Your World Model Survive a Triathlon?](https://arxiv.org/abs/2606.11129v1)**  
  Authors: Yuke Zhao, Wangbo Zhao, Weijie Wang, Zeyu Zhang, Dakai An, Akide Liu, Yinghao Yu, Jiasheng Tang, Fan Wang, Wei Wang, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11129v1.pdf)  
  Keywords: ar, geometry, semantic, segmentation, robotics, dynamic, motion, gaussian splatting  

### Large Scene

- **[KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis](https://arxiv.org/abs/2606.03120v1)**  
  Authors: Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.03120v1.pdf)  
  Keywords: efficient, ar, sparse-view, nerf, gaussian splatting, outdoor, high-fidelity, 3d gaussian  
- **[City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.30310v1)**  
  Authors: Sayan Paul, Sourav Ghosh, Siddharth Katageri, Soumyadip Maity, Sanjana Sinha, Brojeshwar Bhowmick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30310v1.pdf)  
  Keywords: face, ar, geometry, urban scene, nerf, large scene, gaussian splatting, 3d reconstruction, high-fidelity  
- **[GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction](https://arxiv.org/abs/2605.23888v1)**  
  Authors: Katharina Schmid, Nicolas von Lützow, Jozef Hladký, Angela Dai, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.23888v1.pdf)  
  Keywords: geometry, large scene, ar, high-fidelity  
- **[Diffusion-guided Generalizable Enhancer for Urban Scene Reconstruction](https://arxiv.org/abs/2605.22420v1)**  
  Authors: Henry Che, Jingkang Wang, Yun Chen, Ze Yang, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.22420v1.pdf)  
  Keywords: efficient, autonomous driving, neural rendering, ar, urban scene, high-fidelity, 3d gaussian  
- **[Feed-Forward Gaussian Splatting from Sparse Aerial Views](https://arxiv.org/abs/2605.19949v1)**  
  Authors: Dongli Wu, Zhuoxiao Li, Tongyan Hua, Yinrui Ren, Xiaobao Wei, Rongjun Qin, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.19949v1.pdf)  
  Keywords: ar, geometry, urban scene, gaussian splatting, 3d gaussian  
- **[Cross-View Splatter: Feed-Forward View Synthesis with Georeferenced Images](https://arxiv.org/abs/2605.19656v1)**  
  Authors: Matias Turkulainen, Akshay Krishnan, Filippo Aleotti, Mohamed Sayed, Guillermo Garcia-Hernando, Juho Kannala, Arno Solin, Gabriel Brostow, Daniyar Turmukhambetov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.19656v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nianticspatial.github.io/cross-view-splatter)  
  Keywords: outdoor, mapping, ar  
- **[P2GS: Physical Prior-guided Gaussian Splatting for Photometrically Consistent Urban Reconstruction](https://arxiv.org/abs/2605.16925v1)**  
  Authors: Kota Shimomura, Hidehisa Arai, Tsubasa Takahashi, Takayoshi Yamashita, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.16925v1.pdf)  
  Keywords: illumination, autonomous driving, fast, ar, lighting, sparse view, dynamic, mapping, gaussian splatting, outdoor, high-fidelity, 3d gaussian  
- **[PropSplat: Map-Free RF Field Reconstruction via 3D Gaussian Propagation Splatting](https://arxiv.org/abs/2605.08035v1)**  
  Authors: William Bjorndahl, Maninder Pal Singh, Farhad Nouri, Joseph Camp  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.08035v1.pdf)  
  Keywords: ar, nerf, localization, outdoor, 3d gaussian  
- **[FieryGS: In-the-Wild Fire Synthesis with Physics-Integrated Gaussian Splatting](https://arxiv.org/abs/2605.00177v1)**  
  Authors: Qianfan Shen, Ningxiao Tao, Qiyu Dai, Tianle Chen, Minghan Qin, Yongjie Zhang, Mengyu Chu, Wenzheng Chen, Baoquan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/FieryGS)  
  Keywords: efficient, face, ar, geometry, dynamic, gaussian splatting, outdoor, high-fidelity, 3d gaussian  
- **[Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193v1)**  
  Authors: Vinayak Gupta, Chih-Hao Lin, Shenlong Wang, Anand Bhattad, Jia-Bin Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28193v1.pdf)  
  Keywords: illumination, ar, sparse-view, lighting, sparse view, semantic, segmentation, dynamic, outdoor, 3d reconstruction, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 194 papers*

- **[RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos](https://arxiv.org/abs/2606.16278v1)**  
  Authors: Zhenhua Wu, Yun Pang, Mingkun Chang, Yuwei Ning, Liangzhi Wang, Yi Xiao, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16278v1.pdf)  
  Keywords: illumination, autonomous driving, ar, semantic, lightweight, gaussian splatting, 3d gaussian  
- **[PolyMerge: Compressing 3D Gaussian Splats with Polytope Coverings for Provably Safe Resource-Constrained Navigation](https://arxiv.org/abs/2606.16232v1)**  
  Authors: Jihoon Hong, Chih-Yuan Chiu, Sara Fridovich-Keil, Glen Chou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://athlon76.github.io/PolyMerge-website)  
  Keywords: ar, lightweight, motion, gaussian splatting, 3d gaussian  
- **[Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation](https://arxiv.org/abs/2606.16163v1)**  
  Authors: Yuhan Chen, Wenxuan Yu, Guofa Li, Kunyang Huang, Ying Fang, Yicui Shi, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16163v1.pdf)  
  Keywords: efficient, ar, lighting, dynamic, gaussian splatting  
- **[SplatlessDF: Continuous Distance Field Mapping with Non-Splatting Gaussians](https://arxiv.org/abs/2606.13990v1)**  
  Authors: Monisha Mushtary Uttsha, Lan Wu, Teresa Vidal-Calleja  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.13990v1.pdf)  
  Keywords: efficient, face, ar, geometry, mapping, gaussian splatting  
- **[Seeing What Matters: Perceptual Wrapper with Common Randomness for 3D Gaussian Splatting](https://arxiv.org/abs/2606.11782v1)**  
  Authors: He-Bi Yang, Jing-Zhong Chen, Yen-Kuan Ho, Sang NguyenQuang, Fan-Yi Hsu, Yun-Yu Lee, Jui-Chiu Chiang, Wen-Hsiao Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11782v1.pdf)  
  Keywords: ar, lightweight, real-time rendering, gaussian splatting, 3d gaussian  
- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314v1)**  
  Authors: Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11314v1.pdf)  
  Keywords: ar, neural rendering, geometry, lighting, lightweight, light transport, dynamic, ray tracing, motion, relighting, 3d reconstruction, 3d gaussian  
- **[Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606v1)**  
  Authors: Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09606v1.pdf)  
  Keywords: illumination, compact, ar, global illumination, lighting, light transport, path tracing, ray tracing, reflection, relighting, shadow, 3d gaussian  
- **[REFINE: Super-efficient 3D Gaussian Splatting Pruning via Rendering-Free Primitive Importance](https://arxiv.org/abs/2606.09074v1)**  
  Authors: Zhang Chen, Shuai Wan, Mengting Yu, Fuzheng Yang, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09074v1.pdf)  
  Keywords: efficient, ar, geometry, head, gaussian splatting, high-fidelity, 3d gaussian  
- **[MaterialClusterGS: Palette-Based Material Decomposition and Physically-Based Relighting with 2D Gaussian Splatting](https://arxiv.org/abs/2606.09018v1)**  
  Authors: Hao Zhang, Ang Li, Boyan Du, Junke Zhu, Fei Zhu, Meng Gai, Zhangjin Huang, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09018v1.pdf)  
  Keywords: illumination, compact, ar, lighting, gaussian splatting, relighting, shadow  
- **[LEGS: Laplacian-Enhanced Gaussian Splatting with a Nonlinear Weighted Loss](https://arxiv.org/abs/2606.07932v1)**  
  Authors: Yongfei Guo, Qizhou Huo, Xuan Sun, Yuanhao Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.07932v1.pdf)  
  Keywords: efficient, ar, fast, vr, nerf, gaussian splatting, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 117 papers*

- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: illumination, ar, global illumination, gaussian splatting, high-fidelity  
- **[TurboGS: Accelerating 3D Gaussian Splatting via Error-Guided Sparse Pixel Sampling and Optimization](https://arxiv.org/abs/2606.15924v1)**  
  Authors: Zheng Dong, Daifei Qiu, Pinxuan Dai, Ke Xu, Jiamin Xu, Lili He, Rynson W. H. Lau, Weiwei Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.15924v1.pdf)  
  Keywords: acceleration, fast, ar, dynamic, gaussian splatting, high-fidelity, 3d gaussian  
- **[EmoZone-Talker: Regional Semantic Control of Audio-Driven 3DGS Talking Heads via Facial Action Units](https://arxiv.org/abs/2606.15848v1)**  
  Authors: Tingting Chen, Shaojun Wang, Huaye Zhang, Diqiong Jiang, Chenglizhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.15848v1.pdf)  
  Keywords: face, ar, head, animation, semantic, dynamic, motion, gaussian splatting, deformation, high-fidelity, 3d gaussian  
- **[MoVerse: Real-Time Video World Modeling with Panoramic Gaussian Scaffold](https://arxiv.org/abs/2606.13376v1)**  
  Authors: Yang Zhou, Ziheng Wang, Yuqin Lu, Haofeng Liu, Jun Liang, Shengfeng He, Jing Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.13376v1.pdf)  
  Keywords: ar, geometry, motion, high-fidelity, 3d gaussian  
- **[ManiSplat: Manipulation Trajectory Synthesis from Monocular Video via Decoupled 3D Gaussian Splatting](https://arxiv.org/abs/2606.10645v1)**  
  Authors: Wenhao Hu, Haonan Zhou, Liu Liu, Yun Du, Xinjie Wang, Ziang Li, Zhizhong Su, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.10645v1.pdf)  
  Keywords: ar, robotics, dynamic, motion, gaussian splatting, high-fidelity, 3d gaussian  
- **[GaussTrace: Provenance Analysis of 3D Gaussian Splatting Models with Evidence-based LLM Reasoning](https://arxiv.org/abs/2606.10612v1)**  
  Authors: Haoliang Han, Ziyuan Luo, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.10612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haolianghan.github.io/GaussTrace)  
  Keywords: ar, high-fidelity, gaussian splatting, 3d gaussian  
- **[ABot-Earth 0.5: Generative 3D Earth Model](https://arxiv.org/abs/2606.09967v1)**  
  Authors: Ming Qian, Tianjian Ouyang, Mingchao Sun, Zijian Wang, Jincheng Xiong, Jiarong Han, Yongchang Zhang, Jiawei Zhang, Xu Wang, Yu Liu, Luyang Tang, Fei Yu, Zengye Ge, Mengmeng Du, Yuan Liu, Nianfei Fan, Song Wang, Yingliang Peng, Chunxue Jia, Yang Liu, Shiying Zeng, Haozhe Shi, Junnan Lai, Hongyu Pan, Zheng Wu, Ning Guo, Mu Xu, Hang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09967v1.pdf)  
  Keywords: ar, geometry, gaussian splatting, 3d reconstruction, high-fidelity, 3d gaussian  
- **[REFINE: Super-efficient 3D Gaussian Splatting Pruning via Rendering-Free Primitive Importance](https://arxiv.org/abs/2606.09074v1)**  
  Authors: Zhang Chen, Shuai Wan, Mengting Yu, Fuzheng Yang, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09074v1.pdf)  
  Keywords: efficient, ar, geometry, head, gaussian splatting, high-fidelity, 3d gaussian  
- **[GraspFoM: Towards Reconstruction-Driven Robotic Grasping with 3D Foundation Priors](https://arxiv.org/abs/2606.08440v1)**  
  Authors: Dongli Wu, Xiaobao Wei, Hao Wang, Qiaochu Dong, Ying Li, Qingpo Wuwu, Ming Lu, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.08440v1.pdf)  
  Keywords: geometry, ar, high-fidelity  
- **[Wispy to Voluminous: Prior-free Multi-view Capture of Strand-level Facial Hair](https://arxiv.org/abs/2606.08041v1)**  
  Authors: Jaeseong Lee, Giljoo Nam, Adrian Jarabo, Carlos Aliaga  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.08041v1.pdf)  
  Keywords: face, ar, geometry, avatar, head, animation, high-fidelity, 3d gaussian  

### Ray Tracing

- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: illumination, ar, global illumination, gaussian splatting, high-fidelity  
- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314v1)**  
  Authors: Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11314v1.pdf)  
  Keywords: ar, neural rendering, geometry, lighting, lightweight, light transport, dynamic, ray tracing, motion, relighting, 3d reconstruction, 3d gaussian  
- **[Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606v1)**  
  Authors: Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09606v1.pdf)  
  Keywords: illumination, compact, ar, global illumination, lighting, light transport, path tracing, ray tracing, reflection, relighting, shadow, 3d gaussian  
- **[RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation](https://arxiv.org/abs/2606.01261v1)**  
  Authors: Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.01261v1.pdf)  
  Keywords: efficient, ar, geometry, semantic, segmentation, ray tracing, reflection, gaussian splatting, 3d gaussian  
- **[Directed Distance Fields for Constant-Time Ray Queries on Gaussian Splatting](https://arxiv.org/abs/2606.00817v1)**  
  Authors: Subhankar MIshra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00817v1.pdf) | [![GitHub](https://img.shields.io/github/stars/smlab-niser/ddf-gs?style=social)](https://github.com/smlab-niser/ddf-gs)  
  Keywords: illumination, face, ar, fast, global illumination, gaussian splatting, shadow, 3d gaussian  
- **[Underwater360: Reconstructing Underwater Scenes from Panoramic Images with Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2605.26447v1)**  
  Authors: Jiangbei Hu, Weichao Song, Shibo Yu, Mohan Wang, Zihan Yi, Rui Wu, Mingkang Xiang, Na Lei, Shengfa Wang, Zhongxuan Luo, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26447v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SwcK423/Underwater360?style=social)](https://github.com/SwcK423/Underwater360)  
  Keywords: ray casting, ar, gaussian splatting, 3d gaussian  
- **[Differentiable Ray Tracing with Gaussians for Unified Radio Propagation Simulation and View Synthesis](https://arxiv.org/abs/2605.07781v1)**  
  Authors: Niklas Vaara, Lam Huynh, Pekka Sangi, Miguel Bordallo López, Janne Heikkilä  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.07781v1.pdf)  
  Keywords: ar, geometry, ray tracing, gaussian splatting, high-fidelity, 3d gaussian  
- **[Power Foam: Unifying Real-Time Differentiable Ray Tracing and Rasterization](https://arxiv.org/abs/2604.24994v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Dor Verbin, Kwang Moo Yi, Anish Prabhu, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24994v1.pdf)  
  Keywords: efficient, face, ar, geometry, ray tracing  
- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138v1)**  
  Authors: Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/viserdex)  
  Keywords: efficient, ar, tracking, semantic, lighting, robotics, dynamic, ray tracing, gaussian splatting, 3d gaussian  
- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: face, ar, ray tracing, reflection, gaussian splatting  

### Relighting

*Showing the latest 50 out of 59 papers*

- **[RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos](https://arxiv.org/abs/2606.16278v1)**  
  Authors: Zhenhua Wu, Yun Pang, Mingkun Chang, Yuwei Ning, Liangzhi Wang, Yi Xiao, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16278v1.pdf)  
  Keywords: illumination, autonomous driving, ar, semantic, lightweight, gaussian splatting, 3d gaussian  
- **[Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation](https://arxiv.org/abs/2606.16163v1)**  
  Authors: Yuhan Chen, Wenxuan Yu, Guofa Li, Kunyang Huang, Ying Fang, Yicui Shi, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16163v1.pdf)  
  Keywords: efficient, ar, lighting, dynamic, gaussian splatting  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: illumination, ar, global illumination, gaussian splatting, high-fidelity  
- **[Wild3R: Feed-Forward 3D Gaussian Splatting from Unconstrained Sparse Photo Collection](https://arxiv.org/abs/2606.11894v2)**  
  Authors: Yuto Furutani, Takashi Otonari, Kaede Shiohara, Toshihiko Yamasaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11894v2.pdf)  
  Keywords: illumination, ar, lighting, gaussian splatting, 3d gaussian  
- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314v1)**  
  Authors: Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11314v1.pdf)  
  Keywords: ar, neural rendering, geometry, lighting, lightweight, light transport, dynamic, ray tracing, motion, relighting, 3d reconstruction, 3d gaussian  
- **[Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606v1)**  
  Authors: Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09606v1.pdf)  
  Keywords: illumination, compact, ar, global illumination, lighting, light transport, path tracing, ray tracing, reflection, relighting, shadow, 3d gaussian  
- **[MaterialClusterGS: Palette-Based Material Decomposition and Physically-Based Relighting with 2D Gaussian Splatting](https://arxiv.org/abs/2606.09018v1)**  
  Authors: Hao Zhang, Ang Li, Boyan Du, Junke Zhu, Fei Zhu, Meng Gai, Zhangjin Huang, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09018v1.pdf)  
  Keywords: illumination, compact, ar, lighting, gaussian splatting, relighting, shadow  
- **[RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation](https://arxiv.org/abs/2606.01261v1)**  
  Authors: Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.01261v1.pdf)  
  Keywords: efficient, ar, geometry, semantic, segmentation, ray tracing, reflection, gaussian splatting, 3d gaussian  
- **[Directed Distance Fields for Constant-Time Ray Queries on Gaussian Splatting](https://arxiv.org/abs/2606.00817v1)**  
  Authors: Subhankar MIshra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00817v1.pdf) | [![GitHub](https://img.shields.io/github/stars/smlab-niser/ddf-gs?style=social)](https://github.com/smlab-niser/ddf-gs)  
  Keywords: illumination, face, ar, fast, global illumination, gaussian splatting, shadow, 3d gaussian  
- **[F-RNG: Feed-Forward Relightable Neural Gaussians](https://arxiv.org/abs/2605.25975v2)**  
  Authors: Guangming Fu, Jiahui Fan, Jian Yang, Miloš Hašan, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25975v2.pdf)  
  Keywords: illumination, ar, fast, geometry, sparse-view, lighting, gaussian splatting, relighting, high-fidelity, relightable, 3d gaussian  

### SLAM

*Showing the latest 50 out of 75 papers*

- **[SplatlessDF: Continuous Distance Field Mapping with Non-Splatting Gaussians](https://arxiv.org/abs/2606.13990v1)**  
  Authors: Monisha Mushtary Uttsha, Lan Wu, Teresa Vidal-Calleja  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.13990v1.pdf)  
  Keywords: efficient, face, ar, geometry, mapping, gaussian splatting  
- **[Scene-Adaptive Nonlinear Tone Curves for Pseudo Ground-Truth Generation in Low-Light 3D Gaussian Splatting](https://arxiv.org/abs/2606.11841v1)**  
  Authors: Mingzhe Lyu, Jinqiang Cui, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11841v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lvmingzhe/adaptiveToneCurve?style=social)](https://github.com/lvmingzhe/adaptiveToneCurve)  
  Keywords: ar, dynamic, mapping, gaussian splatting, 3d reconstruction, 3d gaussian  
- **[Envision4D: Envisioning Visual Futures via Feed-forward 4D Gaussian Splatting for Autonomous Driving](https://arxiv.org/abs/2606.10656v1)**  
  Authors: Qi Song, Yifei He, Chi Zhang, Zheng Fu, Xuhe Zhao, Mengmeng Yang, Kun Jiang, Rui Huang, Diange Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.10656v1.pdf)  
  Keywords: autonomous driving, ar, dynamic, mapping, motion, gaussian splatting, 4d  
- **[QuadVerse: An Integrated Framework Aligning Visual-Physical Reality for Quadruped Simulation](https://arxiv.org/abs/2606.07118v2)**  
  Authors: Yuxiang Chen, Yuanhao Wang, Ziheng Zhang, Meng Zhang, Yu Liu, Yufei Jia, Tiancai Wang, Erjin Zhou, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.07118v2.pdf)  
  Keywords: ar, geometry, tracking, semantic, dynamic, motion, gaussian splatting, 3d gaussian  
- **[RPC-GS: Gaussian Splatting with native RPC Rendering for Satellite Imagery](https://arxiv.org/abs/2606.06690v1)**  
  Authors: Valentin Wagner, Sebastian Bullinger, Christoph Bodensteiner, Michael Arens  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.06690v1.pdf)  
  Keywords: mapping, ar, geometry, gaussian splatting  
- **[Multi-Agent Next-Best-View Optimization for Risk-Averse Planning](https://arxiv.org/abs/2606.04158v1)**  
  Authors: Amirhossein Mollaei Khass, Vivek Pandey, Guangyi Liu, Athanasios Cosse, Emrah Bayrak, Nader Motee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.04158v1.pdf)  
  Keywords: efficient, ar, head, mapping, gaussian splatting, 3d gaussian  
- **[Real-Time Physics Simulation with Dynamic Mesh-Gaussian Reconstructions](https://arxiv.org/abs/2606.00444v1)**  
  Authors: Adrian Ramlal, John S. Zelek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00444v1.pdf)  
  Keywords: efficient, ar, tracking, dynamic, gaussian splatting, 3d reconstruction  
- **[Learning Global Motion with Compact Gaussians for Feed-Forward 4D Reconstruction](https://arxiv.org/abs/2605.31595v1)**  
  Authors: Mungyeom Kim, Minkyeong Jeon, Honggyu An, Jaewoo Jung, Hyuna Ko, Jisang Han, Hyeonseo Yu, Donghwan Shin, Sunghwan Hong, Takuya Narihira, Kazumi Fukuda, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31595v1.pdf)  
  Keywords: compact, understanding, ar, tracking, dynamic, motion, 4d, 3d gaussian  
- **[Triangle Splatting SLAM](https://arxiv.org/abs/2605.31419v2)**  
  Authors: Nicholas Fry, Eric Dexheimer, Kirill Mazur, Paul H. J. Kelly, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31419v2.pdf)  
  Keywords: ar, geometry, tracking, mapping, slam, gaussian splatting, deformation, 3d gaussian  
- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137v1)**  
  Authors: Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00137v1.pdf)  
  Keywords: ar, geometry, animation, mapping, gaussian splatting, survey  

### Scene Understanding

*Showing the latest 50 out of 112 papers*

- **[RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos](https://arxiv.org/abs/2606.16278v1)**  
  Authors: Zhenhua Wu, Yun Pang, Mingkun Chang, Yuwei Ning, Liangzhi Wang, Yi Xiao, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16278v1.pdf)  
  Keywords: illumination, autonomous driving, ar, semantic, lightweight, gaussian splatting, 3d gaussian  
- **[EmoZone-Talker: Regional Semantic Control of Audio-Driven 3DGS Talking Heads via Facial Action Units](https://arxiv.org/abs/2606.15848v1)**  
  Authors: Tingting Chen, Shaojun Wang, Huaye Zhang, Diqiong Jiang, Chenglizhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.15848v1.pdf)  
  Keywords: face, ar, head, animation, semantic, dynamic, motion, gaussian splatting, deformation, high-fidelity, 3d gaussian  
- **[MooMIns -- Monocular 3D Reconstruction and Object Pose Estimation from Multiple Instances](https://arxiv.org/abs/2606.14389v1)**  
  Authors: Robert Langendörfer, Markus Hillemann, Markus Ulrich  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.14389v1.pdf)  
  Keywords: ar, geometry, segmentation, motion, gaussian splatting, 3d reconstruction  
- **[WorldOlympiad: Can Your World Model Survive a Triathlon?](https://arxiv.org/abs/2606.11129v1)**  
  Authors: Yuke Zhao, Wangbo Zhao, Weijie Wang, Zeyu Zhang, Dakai An, Akide Liu, Yinghao Yu, Jiasheng Tang, Fan Wang, Wei Wang, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11129v1.pdf)  
  Keywords: ar, geometry, semantic, segmentation, robotics, dynamic, motion, gaussian splatting  
- **[QuadVerse: An Integrated Framework Aligning Visual-Physical Reality for Quadruped Simulation](https://arxiv.org/abs/2606.07118v2)**  
  Authors: Yuxiang Chen, Yuanhao Wang, Ziheng Zhang, Meng Zhang, Yu Liu, Yufei Jia, Tiancai Wang, Erjin Zhou, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.07118v2.pdf)  
  Keywords: ar, geometry, tracking, semantic, dynamic, motion, gaussian splatting, 3d gaussian  
- **[Recent Advances and Trends in Learning-based 3D Representations](https://arxiv.org/abs/2606.04871v1)**  
  Authors: Adrien Schockaert, Hamid Laga, Hazem Wannous, Vincent Magnier, Guillaume Dufaye, Jean-françois Witz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.04871v1.pdf)  
  Keywords: compact, autonomous driving, neural rendering, ar, vr, medical, recognition, motion, gaussian splatting, 3d reconstruction, 4d, survey, 3d gaussian  
- **[MLP Splatting: Object-Centric Neural Fields](https://arxiv.org/abs/2606.03877v1)**  
  Authors: Shinjeong Kim, Yuzhou Cheng, Xin Kong, Paul H. J. Kelly, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.03877v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shinjeongkim.com/mlp-splatting)  
  Keywords: efficient, compact, understanding, fast, ar, semantic, segmentation, gaussian splatting, 3d gaussian  
- **[UnsOcc: 3D Semantic Occupancy Prediction in Unstructured Scene via Rendering Fusion](https://arxiv.org/abs/2606.03581v1)**  
  Authors: Ye Wu, Ruiqi Song, Baiyong Ding, Nanxin Zeng, Junjie Cheng, Yunfeng Ai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.03581v1.pdf)  
  Keywords: ar, autonomous driving, semantic, segmentation, gaussian splatting  
- **[$\text{VG}^2$GT: Voxel-Gaussian Splatting Visual Geometry Grounded Transformer](https://arxiv.org/abs/2606.01573v2)**  
  Authors: Yibin Zhao, Yihan Pan, Jun Nan, Wenli Yang, Liwei Chen, Jianjun Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.01573v2.pdf)  
  Keywords: ar, geometry, gaussian splatting, 3d reconstruction, understanding  
- **[RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation](https://arxiv.org/abs/2606.01261v1)**  
  Authors: Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.01261v1.pdf)  
  Keywords: efficient, ar, geometry, semantic, segmentation, ray tracing, reflection, gaussian splatting, 3d gaussian  



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