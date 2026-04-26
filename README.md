# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-04-26 01:45:19

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
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (164 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (198 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (39 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (215 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (19 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (199 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (122 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (18 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (66 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (80 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (122 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: gaussian splatting, efficient, geometry, tracking, 3d gaussian, slam, survey, 3d reconstruction, motion, ar  
- **[A Survey of Spatial Memory Representations for Efficient Robot Navigation](https://arxiv.org/abs/2604.16482v1)**  
  Authors: Ma. Madecheen S. Pangaliman, Steven S. Sison, Erwin P. Quilloy, Rowel Atienza  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.16482v1.pdf)  
  Keywords: efficient, semantic, slam, survey, ar  
- **[Nevis Digital Twin: Photogrammetry and Immersive Visualization of Historical Sites](https://arxiv.org/abs/2603.20560v1)**  
  Authors: Alex Apffel, Huy Tran, Vuthea Chheang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20560v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, vr, survey, ar  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ray tracing, mapping, survey, ar  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: gaussian splatting, efficient, tracking, face, 3d gaussian, slam, survey, mapping, motion, ar, localization, dynamic  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: robotics, gaussian splatting, 3d gaussian, survey, ar  

### Acceleration

*Showing the latest 50 out of 105 papers*

- **[WildSplatter: Feed-forward 3D Gaussian Splatting with Appearance Control from Unconstrained Images](https://arxiv.org/abs/2604.21182v1)**  
  Authors: Yuki Fujimura, Takahiro Kushida, Kazuya Kitano, Takuya Funatomi, Yasuhiro Mukaigawa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21182v1.pdf)  
  Keywords: illumination, gaussian splatting, lighting, 3d gaussian, real-time rendering, ar  
- **[GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds](https://arxiv.org/abs/2604.20155v1)**  
  Authors: Ao Gao, Jingyu Gong, Xin Tan, Zhizhong Zhang, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20155v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, ar, sparse-view  
- **[SketchFaceGS: Real-Time Sketch-Driven Face Editing and Generation with Gaussian Splatting](https://arxiv.org/abs/2604.19202v1)**  
  Authors: Bo Li, Jiahao Kang, Yubo Ma, Feng-Lin Liu, Bin Liu, Fang-Lue Zhang, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19202v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, face, 3d gaussian, real-time rendering, ar, head, fast  
- **[High-Fidelity 3D Gaussian Human Reconstruction via Region-Aware Initialization and Geometric Priors](https://arxiv.org/abs/2604.21714v1)**  
  Authors: Yang Liu, Zhiyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21714v1.pdf)  
  Keywords: deformation, gaussian splatting, high-fidelity, efficient, geometry, human, face, efficient rendering, 3d gaussian, real-time rendering, motion, ar, dynamic  
- **[GeGS-PCR: Effective and Robust 3D Point Cloud Registration with Two-Stage Color-Enhanced Geometric-3DGS Fusion](https://arxiv.org/abs/2604.17721v1)**  
  Authors: Jiayi Tian, Haiduo Huang, Tian Xia, Wenzhe Zhao, Pengju Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17721v1.pdf)  
  Keywords: ar, fast  
- **[Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction](https://arxiv.org/abs/2604.15941v1)**  
  Authors: Haato Watanabe, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15941v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, nerf, lightweight, 3d reconstruction, real-time rendering, ar, fast  
- **[CLOTH-HUGS: Cloth Aware Human Gaussian Splatting](https://arxiv.org/abs/2604.15875v1)**  
  Authors: Sadia Mubashshira, Nazanin Amini, Kevin Desai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15875v1.pdf)  
  Keywords: deformation, gaussian splatting, human, neural rendering, body, real-time rendering, ar, dynamic  
- **[Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2604.15862v1)**  
  Authors: Yijia Guo, Wenkai Huang, Tong Hu, Gaolei Li, Yang Li, Yuxin Hong, Liwen Hu, Xitong Ling, Jianhua Li, Shengbo Chen, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15862v1.pdf)  
  Keywords: gaussian splatting, efficient, 3d gaussian, 3d reconstruction, mapping, 4d, ar, fast, dynamic  
- **[GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens](https://arxiv.org/abs/2604.15284v2)**  
  Authors: Roni Itkin, Noam Issachar, Yehonatan Keypur, Xingyu Chen, Anpei Chen, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15284v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://r-itk.github.io/globalsplat)  
  Keywords: gaussian splatting, efficient, geometry, 3d gaussian, compact, ar, fast  
- **[Rethinking Image-to-3D Generation with Sparse Queries: Efficiency, Capacity, and Input-View Bias](https://arxiv.org/abs/2604.13905v1)**  
  Authors: Zhiyuan Xu, Jiuming Liu, Yuxin Chen, Masayoshi Tomizuka, Chenfeng Xu, Chensheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13905v1.pdf)  
  Keywords: efficient, geometry, 3d gaussian, compact, ar, fast  

### Applications

*Showing the latest 50 out of 498 papers*

- **[DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures](https://arxiv.org/abs/2604.21631v1)**  
  Authors: Xu Wang, Zhiru Wang, Shiyun Xie, Chengwei Pan, Yisong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21631v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, nerf, lightweight, ar  
- **[DiffNR: Diffusion-Enhanced Neural Representation Optimization for Sparse-View 3D Tomographic Reconstruction](https://arxiv.org/abs/2604.21518v1)**  
  Authors: Shiyan Su, Ruyi Zha, Danli Shi, Hongdong Li, Xuelian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21518v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, sparse-view  
- **[You Only Gaussian Once: Controllable 3D Gaussian Splatting for Ultra-Densely Sampled Scenes](https://arxiv.org/abs/2604.21400v1)**  
  Authors: Jinrang Jia, Zhenjia Li, Yifeng Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21400v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jjrcn.github.io/YOGO)  
  Keywords: gaussian splatting, high-fidelity, neural rendering, 3d gaussian, ar  
- **[WildSplatter: Feed-forward 3D Gaussian Splatting with Appearance Control from Unconstrained Images](https://arxiv.org/abs/2604.21182v1)**  
  Authors: Yuki Fujimura, Takahiro Kushida, Kazuya Kitano, Takuya Funatomi, Yasuhiro Mukaigawa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21182v1.pdf)  
  Keywords: illumination, gaussian splatting, lighting, 3d gaussian, real-time rendering, ar  
- **[GeoRect4D: Geometry-Compatible Generative Rectification for Dynamic Sparse-View 3D Reconstruction](https://arxiv.org/abs/2604.20784v1)**  
  Authors: Zhenlong Wu, Zihan Zheng, Xuanxuan Wang, Qianhe Wang, Hua Yang, Xiaoyun Zhang, Qiang Hu, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20784v1.pdf)  
  Keywords: high-fidelity, geometry, 3d reconstruction, 4d, ar, sparse-view, dynamic  
- **[GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds](https://arxiv.org/abs/2604.20155v1)**  
  Authors: Ao Gao, Jingyu Gong, Xin Tan, Zhizhong Zhang, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20155v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, ar, sparse-view  
- **[FurnSet: Exploiting Repeats for 3D Scene Reconstruction](https://arxiv.org/abs/2604.20093v1)**  
  Authors: Paul Dobre, Xin Wang, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20093v1.pdf)  
  Keywords: ar, lighting, geometry  
- **[Gaussians on a Diet: High-Quality Memory-Bounded 3D Gaussian Splatting Training](https://arxiv.org/abs/2604.20046v1)**  
  Authors: Yangming Zhang, Jian Xu, Kunxiong Zhu, Wei Niu, Miao Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20046v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, ar, dynamic  
- **[FluSplat: Sparse-View 3D Editing without Test-Time Optimization](https://arxiv.org/abs/2604.20038v1)**  
  Authors: Haitao Huang, Shin-Fang Chng, Huangying Zhan, Qingan Yan, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20038v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, sparse view, 3d reconstruction, ar, sparse-view  
- **[TransSplat: Unbalanced Semantic Transport for Language-Driven 3DGS Editing](https://arxiv.org/abs/2604.19571v1)**  
  Authors: Yanhui Chen, Jiahong Li, Jingchao Wang, Junyi Lin, Zixin Zeng, Yang Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19571v1.pdf)  
  Keywords: gaussian splatting, semantic, 3d gaussian, vr, ar  

### Avatar Generation

*Showing the latest 50 out of 164 papers*

- **[DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures](https://arxiv.org/abs/2604.21631v1)**  
  Authors: Xu Wang, Zhiru Wang, Shiyun Xie, Chengwei Pan, Yisong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21631v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, nerf, lightweight, ar  
- **[SketchFaceGS: Real-Time Sketch-Driven Face Editing and Generation with Gaussian Splatting](https://arxiv.org/abs/2604.19202v1)**  
  Authors: Bo Li, Jiahao Kang, Yubo Ma, Feng-Lin Liu, Bin Liu, Fang-Lue Zhang, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19202v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, face, 3d gaussian, real-time rendering, ar, head, fast  
- **[High-Fidelity 3D Gaussian Human Reconstruction via Region-Aware Initialization and Geometric Priors](https://arxiv.org/abs/2604.21714v1)**  
  Authors: Yang Liu, Zhiyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21714v1.pdf)  
  Keywords: deformation, gaussian splatting, high-fidelity, efficient, geometry, human, face, efficient rendering, 3d gaussian, real-time rendering, motion, ar, dynamic  
- **[A Comparative Evaluation of Geometric Accuracy in NeRF and Gaussian Splatting](https://arxiv.org/abs/2604.18205v1)**  
  Authors: Mikolaj Zielinski, Eryk Vykysaly, Bartlomiej Biesiada, Jan Baturo, Mateusz Capala, Dominik Belter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18205v1.pdf)  
  Keywords: robotics, gaussian splatting, geometry, neural rendering, face, nerf, ar  
- **[E3VS-Bench: A Benchmark for Viewpoint-Dependent Active Perception in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2604.17969v2)**  
  Authors: Koya Sakamoto, Taiki Miyanishi, Daichi Azuma, Shuhei Kurita, Shu Morikuni, Naoya Chiba, Motoaki Kawanabe, Yusuke Iwasawa, Yutaka Matsuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17969v2.pdf)  
  Keywords: gaussian splatting, lighting, high-fidelity, human, 3d gaussian, motion, ar  
- **[D-Prism: Differentiable Primitives for Structured Dynamic Modeling](https://arxiv.org/abs/2604.17082v1)**  
  Authors: Xingyuan Yu, Yijin Li, Chong Zeng, Yuhang Ming, Hujun Bao, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17082v1.pdf)  
  Keywords: deformation, high-fidelity, geometry, tracking, face, motion, ar, dynamic  
- **[Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction](https://arxiv.org/abs/2604.15941v1)**  
  Authors: Haato Watanabe, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15941v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, nerf, lightweight, 3d reconstruction, real-time rendering, ar, fast  
- **[CLOTH-HUGS: Cloth Aware Human Gaussian Splatting](https://arxiv.org/abs/2604.15875v1)**  
  Authors: Sadia Mubashshira, Nazanin Amini, Kevin Desai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15875v1.pdf)  
  Keywords: deformation, gaussian splatting, human, neural rendering, body, real-time rendering, ar, dynamic  
- **[One-shot Compositional 3D Head Avatars with Deformable Hair](https://arxiv.org/abs/2604.14782v1)**  
  Authors: Yuan Sun, Xuan Wang, WeiLi Zhang, Wenxuan Zhang, Yu Guo, Fei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14782v1.pdf)  
  Keywords: deformation, avatar, gaussian splatting, geometry, face, semantic, 3d gaussian, animation, motion, ar, head, dynamic  
- **[Any3DAvatar: Fast and High-Quality Full-Head 3D Avatar Reconstruction from Single Portrait Image](https://arxiv.org/abs/2604.13856v1)**  
  Authors: Yujie Gao, Yao Xiao, Xiangnan Zhu, Ya Li, Yiyi Zhang, Liqing Zhang, Jianfu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13856v1.pdf)  
  Keywords: avatar, high-fidelity, geometry, face, 3d gaussian, ar, head, fast  

### Dynamic Scene

*Showing the latest 50 out of 198 papers*

- **[GeoRect4D: Geometry-Compatible Generative Rectification for Dynamic Sparse-View 3D Reconstruction](https://arxiv.org/abs/2604.20784v1)**  
  Authors: Zhenlong Wu, Zihan Zheng, Xuanxuan Wang, Qianhe Wang, Hua Yang, Xiaoyun Zhang, Qiang Hu, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20784v1.pdf)  
  Keywords: high-fidelity, geometry, 3d reconstruction, 4d, ar, sparse-view, dynamic  
- **[Gaussians on a Diet: High-Quality Memory-Bounded 3D Gaussian Splatting Training](https://arxiv.org/abs/2604.20046v1)**  
  Authors: Yangming Zhang, Jian Xu, Kunxiong Zhu, Wei Niu, Miao Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20046v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, ar, dynamic  
- **[An Object-Centered Data Acquisition Method for 3D Gaussian Splatting using Mobile Phones](https://arxiv.org/abs/2604.19216v1)**  
  Authors: Yuezhe Zhang, Luqian Bai, Mengting Yu, Lei Wei, Shuai Wan, Yifan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19216v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, ar  
- **[BALTIC: A Benchmark and Cross-Domain Strategy for 3D Reconstruction Across Air and Underwater Domains Under Varying Illumination](https://arxiv.org/abs/2604.19133v1)**  
  Authors: Michele Grimaldi, David Nakath, Oscar Pizarro, Jonatan Scharff Willners, Ignacio Carlucho, Yvan R. Petillot  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19133v1.pdf)  
  Keywords: illumination, gaussian splatting, lighting, geometry, 3d gaussian, 3d reconstruction, motion, ar  
- **[High-Fidelity 3D Gaussian Human Reconstruction via Region-Aware Initialization and Geometric Priors](https://arxiv.org/abs/2604.21714v1)**  
  Authors: Yang Liu, Zhiyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21714v1.pdf)  
  Keywords: deformation, gaussian splatting, high-fidelity, efficient, geometry, human, face, efficient rendering, 3d gaussian, real-time rendering, motion, ar, dynamic  
- **[GS-STVSR: Ultra-Efficient Continuous Spatio-Temporal Video Super-Resolution via 2D Gaussian Splatting](https://arxiv.org/abs/2604.18047v1)**  
  Authors: Mingyu Shi, Xin Di, Long Peng, Boxiang Cao, Anran Wu, Zhanfeng Feng, Jiaming Guo, Renjing Pei, Xueyang Fu, Yang Cao, Zhengjun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18047v1.pdf)  
  Keywords: efficient, gaussian splatting, lightweight, mapping, motion, ar  
- **[E3VS-Bench: A Benchmark for Viewpoint-Dependent Active Perception in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2604.17969v2)**  
  Authors: Koya Sakamoto, Taiki Miyanishi, Daichi Azuma, Shuhei Kurita, Shu Morikuni, Naoya Chiba, Motoaki Kawanabe, Yusuke Iwasawa, Yutaka Matsuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17969v2.pdf)  
  Keywords: gaussian splatting, lighting, high-fidelity, human, 3d gaussian, motion, ar  
- **[D-Prism: Differentiable Primitives for Structured Dynamic Modeling](https://arxiv.org/abs/2604.17082v1)**  
  Authors: Xingyuan Yu, Yijin Li, Chong Zeng, Yuhang Ming, Hujun Bao, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17082v1.pdf)  
  Keywords: deformation, high-fidelity, geometry, tracking, face, motion, ar, dynamic  
- **[Incoherent Deformation, Not Capacity: Diagnosing and Mitigating Overfitting in Dynamic Gaussian Splatting](https://arxiv.org/abs/2604.16747v1)**  
  Authors: Ahmad Droby  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.16747v1.pdf)  
  Keywords: deformation, gaussian splatting, 3d gaussian, nerf, ar, dynamic  
- **[CLOTH-HUGS: Cloth Aware Human Gaussian Splatting](https://arxiv.org/abs/2604.15875v1)**  
  Authors: Sadia Mubashshira, Nazanin Amini, Kevin Desai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15875v1.pdf)  
  Keywords: deformation, gaussian splatting, human, neural rendering, body, real-time rendering, ar, dynamic  

### Few-shot

- **[DiffNR: Diffusion-Enhanced Neural Representation Optimization for Sparse-View 3D Tomographic Reconstruction](https://arxiv.org/abs/2604.21518v1)**  
  Authors: Shiyan Su, Ruyi Zha, Danli Shi, Hongdong Li, Xuelian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21518v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, sparse-view  
- **[GeoRect4D: Geometry-Compatible Generative Rectification for Dynamic Sparse-View 3D Reconstruction](https://arxiv.org/abs/2604.20784v1)**  
  Authors: Zhenlong Wu, Zihan Zheng, Xuanxuan Wang, Qianhe Wang, Hua Yang, Xiaoyun Zhang, Qiang Hu, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20784v1.pdf)  
  Keywords: high-fidelity, geometry, 3d reconstruction, 4d, ar, sparse-view, dynamic  
- **[GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds](https://arxiv.org/abs/2604.20155v1)**  
  Authors: Ao Gao, Jingyu Gong, Xin Tan, Zhizhong Zhang, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20155v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, ar, sparse-view  
- **[FluSplat: Sparse-View 3D Editing without Test-Time Optimization](https://arxiv.org/abs/2604.20038v1)**  
  Authors: Haitao Huang, Shin-Fang Chng, Huangying Zhan, Qingan Yan, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20038v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, sparse view, 3d reconstruction, ar, sparse-view  
- **[Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation](https://arxiv.org/abs/2604.18468v1)**  
  Authors: Tianshi Cao, Jiawei Ren, Yuxuan Zhang, Jaewoo Seo, Jiahui Huang, Shikhar Solanki, Haotian Zhang, Mingfei Guo, Haithem Turki, Muxingzi Li, Yue Zhu, Sipeng Zhang, Zan Gojcic, Sanja Fidler, Kangxue Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18468v1.pdf)  
  Keywords: geometry, 3d gaussian, autonomous driving, ar, sparse-view  
- **[RobotPan: A 360$^\circ$ Surround-View Robotic Vision System for Embodied Perception](https://arxiv.org/abs/2604.13476v1)**  
  Authors: Jiahao Ma, Qiang Zhang, Peiran Liu, Zeran Su, Pihai Sun, Gang Han, Wen Zhao, Wei Cui, Zhang Zhang, Zhiyuan Xu, Renjing Xu, Jian Tang, Miaomiao Liu, Yijie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13476v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotpan.github.io)  
  Keywords: robotics, human, face, 3d gaussian, 3d reconstruction, real-time rendering, motion, compact, ar, head, sparse-view, dynamic  
- **[3DRealHead: Few-Shot Detailed Head Avatar](https://arxiv.org/abs/2604.13171v1)**  
  Authors: Jalees Nehvi, Timo Bolkart, Thabo Beeler, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13171v1.pdf)  
  Keywords: avatar, human, few-shot, face, 3d gaussian, ar, head  
- **[ArtifactWorld: Scaling 3D Gaussian Splatting Artifact Restoration via Video Generation Models](https://arxiv.org/abs/2604.12251v1)**  
  Authors: Xinliang Wang, Yifeng Shi, Zhenyu Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12251v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, 3d gaussian, 3d reconstruction, real-time rendering, ar, sparse-view  
- **[Learning 3D Representations for Spatial Intelligence from Unposed Multi-View Images](https://arxiv.org/abs/2604.10573v1)**  
  Authors: Bo Zhou, Qiuxia Lai, Zeren Sun, Xiangbo Shu, Yazhou Yao, Wenguan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10573v1.pdf)  
  Keywords: gaussian splatting, geometry, semantic, understanding, ar, head, sparse-view  
- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370v1)**  
  Authors: Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08370v1.pdf)  
  Keywords: efficient, gaussian splatting, geometry, face, 3d gaussian, ar, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 215 papers*

- **[GeoRect4D: Geometry-Compatible Generative Rectification for Dynamic Sparse-View 3D Reconstruction](https://arxiv.org/abs/2604.20784v1)**  
  Authors: Zhenlong Wu, Zihan Zheng, Xuanxuan Wang, Qianhe Wang, Hua Yang, Xiaoyun Zhang, Qiang Hu, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20784v1.pdf)  
  Keywords: high-fidelity, geometry, 3d reconstruction, 4d, ar, sparse-view, dynamic  
- **[FurnSet: Exploiting Repeats for 3D Scene Reconstruction](https://arxiv.org/abs/2604.20093v1)**  
  Authors: Paul Dobre, Xin Wang, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20093v1.pdf)  
  Keywords: ar, lighting, geometry  
- **[FluSplat: Sparse-View 3D Editing without Test-Time Optimization](https://arxiv.org/abs/2604.20038v1)**  
  Authors: Haitao Huang, Shin-Fang Chng, Huangying Zhan, Qingan Yan, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20038v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, sparse view, 3d reconstruction, ar, sparse-view  
- **[BALTIC: A Benchmark and Cross-Domain Strategy for 3D Reconstruction Across Air and Underwater Domains Under Varying Illumination](https://arxiv.org/abs/2604.19133v1)**  
  Authors: Michele Grimaldi, David Nakath, Oscar Pizarro, Jonatan Scharff Willners, Ignacio Carlucho, Yvan R. Petillot  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19133v1.pdf)  
  Keywords: illumination, gaussian splatting, lighting, geometry, 3d gaussian, 3d reconstruction, motion, ar  
- **[High-Fidelity 3D Gaussian Human Reconstruction via Region-Aware Initialization and Geometric Priors](https://arxiv.org/abs/2604.21714v1)**  
  Authors: Yang Liu, Zhiyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21714v1.pdf)  
  Keywords: deformation, gaussian splatting, high-fidelity, efficient, geometry, human, face, efficient rendering, 3d gaussian, real-time rendering, motion, ar, dynamic  
- **[Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation](https://arxiv.org/abs/2604.18468v1)**  
  Authors: Tianshi Cao, Jiawei Ren, Yuxuan Zhang, Jaewoo Seo, Jiahui Huang, Shikhar Solanki, Haotian Zhang, Mingfei Guo, Haithem Turki, Muxingzi Li, Yue Zhu, Sipeng Zhang, Zan Gojcic, Sanja Fidler, Kangxue Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18468v1.pdf)  
  Keywords: geometry, 3d gaussian, autonomous driving, ar, sparse-view  
- **[A Comparative Evaluation of Geometric Accuracy in NeRF and Gaussian Splatting](https://arxiv.org/abs/2604.18205v1)**  
  Authors: Mikolaj Zielinski, Eryk Vykysaly, Bartlomiej Biesiada, Jan Baturo, Mateusz Capala, Dominik Belter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18205v1.pdf)  
  Keywords: robotics, gaussian splatting, geometry, neural rendering, face, nerf, ar  
- **[D-Prism: Differentiable Primitives for Structured Dynamic Modeling](https://arxiv.org/abs/2604.17082v1)**  
  Authors: Xingyuan Yu, Yijin Li, Chong Zeng, Yuhang Ming, Hujun Bao, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17082v1.pdf)  
  Keywords: deformation, high-fidelity, geometry, tracking, face, motion, ar, dynamic  
- **[Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction](https://arxiv.org/abs/2604.15941v1)**  
  Authors: Haato Watanabe, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15941v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, nerf, lightweight, 3d reconstruction, real-time rendering, ar, fast  
- **[Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2604.15862v1)**  
  Authors: Yijia Guo, Wenkai Huang, Tong Hu, Gaolei Li, Yang Li, Yuxin Hong, Liwen Hu, Xitong Ling, Jianhua Li, Shengbo Chen, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15862v1.pdf)  
  Keywords: gaussian splatting, efficient, 3d gaussian, 3d reconstruction, mapping, 4d, ar, fast, dynamic  

### Large Scene

- **[DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis](https://arxiv.org/abs/2604.13416v1)**  
  Authors: Cheng-You Lu, Yi-Shan Hung, Wei-Ling Chi, Hao-Ping Wang, Charlie Li-Ting Tsai, Yu-Cheng Chang, Yu-Lun Liu, Thomas Do, Chin-Teng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13416v1.pdf)  
  Keywords: outdoor, 3d gaussian, gaussian splatting, ar  
- **[RMGS-SLAM: Real-time Multi-sensor Gaussian Splatting SLAM](https://arxiv.org/abs/2604.12942v2)**  
  Authors: Dongen Li, Yi Liu, Junqi Liu, Zewen Sun, Zefan Huang, Shuo Sun, Jiahui Liu, Chengran Yuan, Hongliang Guo, Francis E. H. Tay, Marcelo H. Ang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12942v2.pdf)  
  Keywords: outdoor, gaussian splatting, 3d gaussian, slam, mapping, ar, localization  
- **[GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors](https://arxiv.org/abs/2604.11401v1)**  
  Authors: Qilin Zhang, Jinyu Zhu, Olaf Wysocki, Benjamin Busam, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11401v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Jinyzzz/GS4City?style=social)](https://github.com/Jinyzzz/GS4City)  
  Keywords: segmentation, gaussian splatting, geometry, urban scene, 3d gaussian, semantic, understanding, compact, ar  
- **[Neural Harmonic Textures for High-Quality Primitive Based Neural Reconstruction](https://arxiv.org/abs/2604.01204v2)**  
  Authors: Jorge Condor, Nicolas Moenne-Loccoz, Merlin Nimier-David, Piotr Didyk, Zan Gojcic, Qi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01204v2.pdf)  
  Keywords: gaussian splatting, large scene, semantic, 3d gaussian, ar  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: gaussian splatting, high-fidelity, efficient, geometry, neural rendering, large scene, shadow, understanding, motion, 4d, ar, dynamic  
- **[Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting](https://arxiv.org/abs/2603.29185v1)**  
  Authors: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29185v1.pdf)  
  Keywords: outdoor, efficient, gaussian splatting, ar, localization  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: efficient, gaussian splatting, neural rendering, large scene, face, 3d gaussian, ar, head  
- **[MAGICIAN: Efficient Long-Term Planning with Imagined Gaussians for Active Mapping](https://arxiv.org/abs/2603.22650v2)**  
  Authors: Shiyao Li, Antoine Guédon, Shizhe Chen, Vincent Lepetit  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22650v2.pdf)  
  Keywords: outdoor, gaussian splatting, lighting, efficient, face, 3d gaussian, mapping, ar, fast  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: outdoor, efficient, gaussian splatting, tracking, slam, ar, head, dynamic  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: outdoor, gaussian splatting, geometry, 3d gaussian, ar, localization  

### Model Compression

*Showing the latest 50 out of 199 papers*

- **[DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures](https://arxiv.org/abs/2604.21631v1)**  
  Authors: Xu Wang, Zhiru Wang, Shiyun Xie, Chengwei Pan, Yisong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21631v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, nerf, lightweight, ar  
- **[DiffNR: Diffusion-Enhanced Neural Representation Optimization for Sparse-View 3D Tomographic Reconstruction](https://arxiv.org/abs/2604.21518v1)**  
  Authors: Shiyan Su, Ruyi Zha, Danli Shi, Hongdong Li, Xuelian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21518v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, sparse-view  
- **[Gaussians on a Diet: High-Quality Memory-Bounded 3D Gaussian Splatting Training](https://arxiv.org/abs/2604.20046v1)**  
  Authors: Yangming Zhang, Jian Xu, Kunxiong Zhu, Wei Niu, Miao Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20046v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, ar, dynamic  
- **[OT-UVGS: Revisiting UV Mapping for Gaussian Splatting as a Capacity Allocation Problem](https://arxiv.org/abs/2604.19127v1)**  
  Authors: Byunghyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19127v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, lightweight, mapping, compact, ar  
- **[AdaGScale: Viewpoint-Adaptive Gaussian Scaling in 3D Gaussian Splatting to Reduce Gaussian-Tile Pairs](https://arxiv.org/abs/2604.18980v1)**  
  Authors: Joongho Jo, Hyerin Lim, Hanjun Choi, Jongsun Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18980v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, ar  
- **[High-Fidelity 3D Gaussian Human Reconstruction via Region-Aware Initialization and Geometric Priors](https://arxiv.org/abs/2604.21714v1)**  
  Authors: Yang Liu, Zhiyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21714v1.pdf)  
  Keywords: deformation, gaussian splatting, high-fidelity, efficient, geometry, human, face, efficient rendering, 3d gaussian, real-time rendering, motion, ar, dynamic  
- **[GS-STVSR: Ultra-Efficient Continuous Spatio-Temporal Video Super-Resolution via 2D Gaussian Splatting](https://arxiv.org/abs/2604.18047v1)**  
  Authors: Mingyu Shi, Xin Di, Long Peng, Boxiang Cao, Anran Wu, Zhanfeng Feng, Jiaming Guo, Renjing Pei, Xueyang Fu, Yang Cao, Zhengjun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18047v1.pdf)  
  Keywords: efficient, gaussian splatting, lightweight, mapping, motion, ar  
- **[Instant Colorization of Gaussian Splats](https://arxiv.org/abs/2604.17155v1)**  
  Authors: Daniel Lieber, Alexander Mock, Nils Wandel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17155v1.pdf)  
  Keywords: segmentation, efficient, gaussian splatting, lighting, semantic, 3d gaussian, mapping, relighting, ar  
- **[LAGS: Low-Altitude Gaussian Splatting with Groupwise Heterogeneous Graph Learning](https://arxiv.org/abs/2604.16910v1)**  
  Authors: Yikun Wang, Yujie Wan, Wei Zuo, Shuai Wang, Yik-Chung Wu, Chengzhong Xu, Huseyin Arslan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.16910v1.pdf)  
  Keywords: ar, efficient, gaussian splatting  
- **[Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction](https://arxiv.org/abs/2604.15941v1)**  
  Authors: Haato Watanabe, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15941v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, nerf, lightweight, 3d reconstruction, real-time rendering, ar, fast  

### Quality Enhancement

*Showing the latest 50 out of 122 papers*

- **[You Only Gaussian Once: Controllable 3D Gaussian Splatting for Ultra-Densely Sampled Scenes](https://arxiv.org/abs/2604.21400v1)**  
  Authors: Jinrang Jia, Zhenjia Li, Yifeng Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21400v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jjrcn.github.io/YOGO)  
  Keywords: gaussian splatting, high-fidelity, neural rendering, 3d gaussian, ar  
- **[GeoRect4D: Geometry-Compatible Generative Rectification for Dynamic Sparse-View 3D Reconstruction](https://arxiv.org/abs/2604.20784v1)**  
  Authors: Zhenlong Wu, Zihan Zheng, Xuanxuan Wang, Qianhe Wang, Hua Yang, Xiaoyun Zhang, Qiang Hu, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20784v1.pdf)  
  Keywords: high-fidelity, geometry, 3d reconstruction, 4d, ar, sparse-view, dynamic  
- **[SketchFaceGS: Real-Time Sketch-Driven Face Editing and Generation with Gaussian Splatting](https://arxiv.org/abs/2604.19202v1)**  
  Authors: Bo Li, Jiahao Kang, Yubo Ma, Feng-Lin Liu, Bin Liu, Fang-Lue Zhang, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19202v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, face, 3d gaussian, real-time rendering, ar, head, fast  
- **[High-Fidelity 3D Gaussian Human Reconstruction via Region-Aware Initialization and Geometric Priors](https://arxiv.org/abs/2604.21714v1)**  
  Authors: Yang Liu, Zhiyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21714v1.pdf)  
  Keywords: deformation, gaussian splatting, high-fidelity, efficient, geometry, human, face, efficient rendering, 3d gaussian, real-time rendering, motion, ar, dynamic  
- **[E3VS-Bench: A Benchmark for Viewpoint-Dependent Active Perception in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2604.17969v2)**  
  Authors: Koya Sakamoto, Taiki Miyanishi, Daichi Azuma, Shuhei Kurita, Shu Morikuni, Naoya Chiba, Motoaki Kawanabe, Yusuke Iwasawa, Yutaka Matsuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17969v2.pdf)  
  Keywords: gaussian splatting, lighting, high-fidelity, human, 3d gaussian, motion, ar  
- **[D-Prism: Differentiable Primitives for Structured Dynamic Modeling](https://arxiv.org/abs/2604.17082v1)**  
  Authors: Xingyuan Yu, Yijin Li, Chong Zeng, Yuhang Ming, Hujun Bao, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17082v1.pdf)  
  Keywords: deformation, high-fidelity, geometry, tracking, face, motion, ar, dynamic  
- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268v1)**  
  Authors: Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14268v1.pdf)  
  Keywords: efficient, lighting, gaussian splatting, high-fidelity, 3d gaussian, understanding, ar  
- **[Any3DAvatar: Fast and High-Quality Full-Head 3D Avatar Reconstruction from Single Portrait Image](https://arxiv.org/abs/2604.13856v1)**  
  Authors: Yujie Gao, Yao Xiao, Xiangnan Zhu, Ya Li, Yiyi Zhang, Liqing Zhang, Jianfu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13856v1.pdf)  
  Keywords: avatar, high-fidelity, geometry, face, 3d gaussian, ar, head, fast  
- **[GGD-SLAM: Monocular 3DGS SLAM Powered by Generalizable Motion Model for Dynamic Environments](https://arxiv.org/abs/2604.12837v1)**  
  Authors: Yi Liu, Haoxuan Xu, Hongbo Duan, Keyu Fan, Zhengyang Zhang, Peiyu Zhuang, Pengting Luo, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12837v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, semantic, 3d gaussian, slam, mapping, motion, ar, localization, dynamic  
- **[Habitat-GS: A High-Fidelity Navigation Simulator with Dynamic Gaussian Splatting](https://arxiv.org/abs/2604.12626v1)**  
  Authors: Ziyuan Xia, Jingyi Xu, Chong Cui, Yuanhong Yu, Jiazhao Zhang, Qingsong Yan, Tao Ni, Junbo Chen, Xiaowei Zhou, Hujun Bao, Ruizhen Hu, Sida Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12626v1.pdf)  
  Keywords: avatar, gaussian splatting, high-fidelity, human, 3d gaussian, ar, dynamic  

### Ray Tracing

- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138v1)**  
  Authors: Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/viserdex)  
  Keywords: robotics, gaussian splatting, lighting, efficient, tracking, semantic, 3d gaussian, ray tracing, ar, dynamic  
- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: gaussian splatting, face, reflection, ray tracing, ar  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: efficient, 3d gaussian, reflection, ray casting, ar  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: efficient, gaussian splatting, tracking, face, semantic, 3d gaussian, ray tracing, slam, mapping, ar, localization  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, shadow, reflection, relightable, ray tracing, mapping, ar  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: path tracing, geometry, face, 3d gaussian, real-time rendering, ar  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: gaussian splatting, high-fidelity, efficient, geometry, face, 3d gaussian, nerf, ray tracing, real-time rendering, ar, fast  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ray tracing, mapping, survey, ar  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: gaussian splatting, high-fidelity, efficient, 3d gaussian, ray marching, real-time rendering, ar  
- **[Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction](https://arxiv.org/abs/2603.08503v1)**  
  Authors: Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08503v1.pdf) | [![GitHub](https://img.shields.io/github/stars/1170632760/Spherical-GOF?style=social)](https://github.com/1170632760/Spherical-GOF)  
  Keywords: robotics, gaussian splatting, efficient, geometry, 3d gaussian, ray casting, ar, fast  

### Relighting

*Showing the latest 50 out of 66 papers*

- **[WildSplatter: Feed-forward 3D Gaussian Splatting with Appearance Control from Unconstrained Images](https://arxiv.org/abs/2604.21182v1)**  
  Authors: Yuki Fujimura, Takahiro Kushida, Kazuya Kitano, Takuya Funatomi, Yasuhiro Mukaigawa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21182v1.pdf)  
  Keywords: illumination, gaussian splatting, lighting, 3d gaussian, real-time rendering, ar  
- **[FurnSet: Exploiting Repeats for 3D Scene Reconstruction](https://arxiv.org/abs/2604.20093v1)**  
  Authors: Paul Dobre, Xin Wang, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20093v1.pdf)  
  Keywords: ar, lighting, geometry  
- **[BALTIC: A Benchmark and Cross-Domain Strategy for 3D Reconstruction Across Air and Underwater Domains Under Varying Illumination](https://arxiv.org/abs/2604.19133v1)**  
  Authors: Michele Grimaldi, David Nakath, Oscar Pizarro, Jonatan Scharff Willners, Ignacio Carlucho, Yvan R. Petillot  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19133v1.pdf)  
  Keywords: illumination, gaussian splatting, lighting, geometry, 3d gaussian, 3d reconstruction, motion, ar  
- **[E3VS-Bench: A Benchmark for Viewpoint-Dependent Active Perception in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2604.17969v2)**  
  Authors: Koya Sakamoto, Taiki Miyanishi, Daichi Azuma, Shuhei Kurita, Shu Morikuni, Naoya Chiba, Motoaki Kawanabe, Yusuke Iwasawa, Yutaka Matsuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17969v2.pdf)  
  Keywords: gaussian splatting, lighting, high-fidelity, human, 3d gaussian, motion, ar  
- **[Instant Colorization of Gaussian Splats](https://arxiv.org/abs/2604.17155v1)**  
  Authors: Daniel Lieber, Alexander Mock, Nils Wandel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17155v1.pdf)  
  Keywords: segmentation, efficient, gaussian splatting, lighting, semantic, 3d gaussian, mapping, relighting, ar  
- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268v1)**  
  Authors: Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14268v1.pdf)  
  Keywords: efficient, lighting, gaussian splatting, high-fidelity, 3d gaussian, understanding, ar  
- **[RadarSplat-RIO: Indoor Radar-Inertial Odometry with Gaussian Splatting-Based Radar Bundle Adjustment](https://arxiv.org/abs/2604.13492v1)**  
  Authors: Pou-Chun Kung, Yuan Tian, Zhengqin Li, Yue Liu, Eric Whitmire, Wolf Kienzle, Hrvoje Benko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13492v1.pdf)  
  Keywords: gaussian splatting, lighting, geometry, recognition, slam, mapping, ar, localization  
- **[MSGS: Multispectral 3D Gaussian Splatting](https://arxiv.org/abs/2604.13340v1)**  
  Authors: Iris Zheng, Guojun Tang, Alexander Doronin, Paul Teal, Fang-Lue Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13340v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, reflection, compact, ar  
- **[SSD-GS: Scattering and Shadow Decomposition for Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2604.13333v1)**  
  Authors: Iris Zheng, Guojun Tang, Alexander Doronin, Paul Teal, Fang-Lue Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13333v1.pdf) | [![GitHub](https://img.shields.io/github/stars/irisfreesiri/SSD-GS?style=social)](https://github.com/irisfreesiri/SSD-GS)  
  Keywords: gaussian splatting, illumination, lighting, face, 3d gaussian, shadow, reflection, relightable, relighting, ar  
- **[AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation](https://arxiv.org/abs/2604.11674v1)**  
  Authors: Mingyang Li, Haofan Xu, Haowen Sun, Xinzhe Chen, Sihua Ren, Liqi Huang, Xinyang Sui, Chenyang Miao, Qiongjie Cui, Zeyang Liu, Xingyu Chen, Xuguang Lan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11674v1.pdf)  
  Keywords: ar, semantic, 3d gaussian, lighting  

### SLAM

*Showing the latest 50 out of 80 papers*

- **[OT-UVGS: Revisiting UV Mapping for Gaussian Splatting as a Capacity Allocation Problem](https://arxiv.org/abs/2604.19127v1)**  
  Authors: Byunghyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19127v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, lightweight, mapping, compact, ar  
- **[GS-STVSR: Ultra-Efficient Continuous Spatio-Temporal Video Super-Resolution via 2D Gaussian Splatting](https://arxiv.org/abs/2604.18047v1)**  
  Authors: Mingyu Shi, Xin Di, Long Peng, Boxiang Cao, Anran Wu, Zhanfeng Feng, Jiaming Guo, Renjing Pei, Xueyang Fu, Yang Cao, Zhengjun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18047v1.pdf)  
  Keywords: efficient, gaussian splatting, lightweight, mapping, motion, ar  
- **[Instant Colorization of Gaussian Splats](https://arxiv.org/abs/2604.17155v1)**  
  Authors: Daniel Lieber, Alexander Mock, Nils Wandel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17155v1.pdf)  
  Keywords: segmentation, efficient, gaussian splatting, lighting, semantic, 3d gaussian, mapping, relighting, ar  
- **[D-Prism: Differentiable Primitives for Structured Dynamic Modeling](https://arxiv.org/abs/2604.17082v1)**  
  Authors: Xingyuan Yu, Yijin Li, Chong Zeng, Yuhang Ming, Hujun Bao, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17082v1.pdf)  
  Keywords: deformation, high-fidelity, geometry, tracking, face, motion, ar, dynamic  
- **[Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2604.15862v1)**  
  Authors: Yijia Guo, Wenkai Huang, Tong Hu, Gaolei Li, Yang Li, Yuxin Hong, Liwen Hu, Xitong Ling, Jianhua Li, Shengbo Chen, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15862v1.pdf)  
  Keywords: gaussian splatting, efficient, 3d gaussian, 3d reconstruction, mapping, 4d, ar, fast, dynamic  
- **[GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow](https://arxiv.org/abs/2604.15612v1)**  
  Authors: Dong-Uk Seo, Jinwoo Jeon, Eungchang Mason Lee, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15612v1.pdf) | [![GitHub](https://img.shields.io/github/stars/url-kaist/gaussianflow-slam?style=social)](https://github.com/url-kaist/gaussianflow-slam)  
  Keywords: gaussian splatting, tracking, geometry, slam, mapping, motion, ar  
- **[RadarSplat-RIO: Indoor Radar-Inertial Odometry with Gaussian Splatting-Based Radar Bundle Adjustment](https://arxiv.org/abs/2604.13492v1)**  
  Authors: Pou-Chun Kung, Yuan Tian, Zhengqin Li, Yue Liu, Eric Whitmire, Wolf Kienzle, Hrvoje Benko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13492v1.pdf)  
  Keywords: gaussian splatting, lighting, geometry, recognition, slam, mapping, ar, localization  
- **[RMGS-SLAM: Real-time Multi-sensor Gaussian Splatting SLAM](https://arxiv.org/abs/2604.12942v2)**  
  Authors: Dongen Li, Yi Liu, Junqi Liu, Zewen Sun, Zefan Huang, Shuo Sun, Jiahui Liu, Chengran Yuan, Hongliang Guo, Francis E. H. Tay, Marcelo H. Ang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12942v2.pdf)  
  Keywords: outdoor, gaussian splatting, 3d gaussian, slam, mapping, ar, localization  
- **[GGD-SLAM: Monocular 3DGS SLAM Powered by Generalizable Motion Model for Dynamic Environments](https://arxiv.org/abs/2604.12837v1)**  
  Authors: Yi Liu, Haoxuan Xu, Hongbo Duan, Keyu Fan, Zhengyang Zhang, Peiyu Zhuang, Pengting Luo, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12837v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, semantic, 3d gaussian, slam, mapping, motion, ar, localization, dynamic  
- **[ReefMapGS: Enabling Large-Scale Underwater Reconstruction by Closing the Loop Between Multimodal SLAM and Gaussian Splatting](https://arxiv.org/abs/2604.11992v1)**  
  Authors: Daniel Yang, Jungseok Hong, John J. Leonard, Yogesh Girdhar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11992v1.pdf)  
  Keywords: gaussian splatting, efficient, geometry, tracking, 3d gaussian, slam, survey, 3d reconstruction, motion, ar  

### Scene Understanding

*Showing the latest 50 out of 122 papers*

- **[TransSplat: Unbalanced Semantic Transport for Language-Driven 3DGS Editing](https://arxiv.org/abs/2604.19571v1)**  
  Authors: Yanhui Chen, Jiahong Li, Jingchao Wang, Junyi Lin, Zixin Zeng, Yang Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19571v1.pdf)  
  Keywords: gaussian splatting, semantic, 3d gaussian, vr, ar  
- **[Instant Colorization of Gaussian Splats](https://arxiv.org/abs/2604.17155v1)**  
  Authors: Daniel Lieber, Alexander Mock, Nils Wandel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17155v1.pdf)  
  Keywords: segmentation, efficient, gaussian splatting, lighting, semantic, 3d gaussian, mapping, relighting, ar  
- **[One-shot Compositional 3D Head Avatars with Deformable Hair](https://arxiv.org/abs/2604.14782v1)**  
  Authors: Yuan Sun, Xuan Wang, WeiLi Zhang, Wenxuan Zhang, Yu Guo, Fei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14782v1.pdf)  
  Keywords: deformation, avatar, gaussian splatting, geometry, face, semantic, 3d gaussian, animation, motion, ar, head, dynamic  
- **[NG-GS: NeRF-Guided 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/2604.14706v1)**  
  Authors: Yi He, Tao Wang, Yi Jin, Congyan Lang, Yidong Li, Haibin Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14706v1.pdf) | [![GitHub](https://img.shields.io/github/stars/BJTU-KD3D/NG-GS?style=social)](https://github.com/BJTU-KD3D/NG-GS)  
  Keywords: segmentation, efficient, gaussian splatting, 3d gaussian, nerf, lightweight, ar  
- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268v1)**  
  Authors: Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14268v1.pdf)  
  Keywords: efficient, lighting, gaussian splatting, high-fidelity, 3d gaussian, understanding, ar  
- **[RadarSplat-RIO: Indoor Radar-Inertial Odometry with Gaussian Splatting-Based Radar Bundle Adjustment](https://arxiv.org/abs/2604.13492v1)**  
  Authors: Pou-Chun Kung, Yuan Tian, Zhengqin Li, Yue Liu, Eric Whitmire, Wolf Kienzle, Hrvoje Benko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13492v1.pdf)  
  Keywords: gaussian splatting, lighting, geometry, recognition, slam, mapping, ar, localization  
- **[GGD-SLAM: Monocular 3DGS SLAM Powered by Generalizable Motion Model for Dynamic Environments](https://arxiv.org/abs/2604.12837v1)**  
  Authors: Yi Liu, Haoxuan Xu, Hongbo Duan, Keyu Fan, Zhengyang Zhang, Peiyu Zhuang, Pengting Luo, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12837v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, semantic, 3d gaussian, slam, mapping, motion, ar, localization, dynamic  
- **[AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation](https://arxiv.org/abs/2604.11674v1)**  
  Authors: Mingyang Li, Haofan Xu, Haowen Sun, Xinzhe Chen, Sihua Ren, Liqi Huang, Xinyang Sui, Chenyang Miao, Qiongjie Cui, Zeyang Liu, Xingyu Chen, Xuguang Lan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11674v1.pdf)  
  Keywords: ar, semantic, 3d gaussian, lighting  
- **[GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors](https://arxiv.org/abs/2604.11401v1)**  
  Authors: Qilin Zhang, Jinyu Zhu, Olaf Wysocki, Benjamin Busam, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11401v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Jinyzzz/GS4City?style=social)](https://github.com/Jinyzzz/GS4City)  
  Keywords: segmentation, gaussian splatting, geometry, urban scene, 3d gaussian, semantic, understanding, compact, ar  
- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138v1)**  
  Authors: Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/viserdex)  
  Keywords: robotics, gaussian splatting, lighting, efficient, tracking, semantic, 3d gaussian, ray tracing, ar, dynamic  



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