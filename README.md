# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-07-26 01:48:08

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
- [Acceleration](#acceleration) (97 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (172 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (185 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (39 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (212 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (26 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (185 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (119 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (13 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (53 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (76 papers) - Papers about SLAM using Gaussian Splatting
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
  Keywords: efficient, ar, high-fidelity, mapping, 3d gaussian, tracking, slam, dynamic, survey, localization  
- **[Recent Advances and Trends in Learning-based 3D Representations](https://arxiv.org/abs/2606.04871v1)**  
  Authors: Adrien Schockaert, Hamid Laga, Hazem Wannous, Vincent Magnier, Guillaume Dufaye, Jean-françois Witz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.04871v1.pdf)  
  Keywords: compact, recognition, gaussian splatting, 3d reconstruction, ar, neural rendering, motion, 3d gaussian, 4d, medical, survey, autonomous driving, vr  
- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137v1)**  
  Authors: Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00137v1.pdf)  
  Keywords: geometry, gaussian splatting, ar, animation, mapping, survey  

### Acceleration

*Showing the latest 50 out of 97 papers*

- **[Construction and Dynamic Update of Channel Gain Maps via 3D Gaussian Splatting](https://arxiv.org/abs/2607.21099v1)**  
  Authors: Yilong Chen, Yuan Guo, Juncong Zhou, Jie Xu, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21099v1.pdf)  
  Keywords: compact, efficient, geometry, fast, gaussian splatting, ar, 3d gaussian, dynamic  
- **[QIRF Quantum-Inspired Non-Orthogonal Function-Space Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2607.18067v1)**  
  Authors: Shizeng Jiang, Hao Zhang, Xuerui Ma, Ying Hu, Tao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18067v1.pdf)  
  Keywords: real-time rendering, nerf, gaussian splatting, ar, 3d gaussian, compression  
- **[Locality-Aware Density Control for Efficient Gaussian-based Image Representation](https://arxiv.org/abs/2607.17896v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Xiandong Meng, Shuai Liu, Chao Li, Fanyang Meng, Youneng Bao, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17896v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ChenJiaCong-1005/LocoADC?style=social)](https://github.com/ChenJiaCong-1005/LocoADC)  
  Keywords: fast, gaussian splatting, ar, efficient  
- **[CaT-GS: Efficient 3DGS Rendering for Large Scale Scenes via Inter-frame Caching and Tile Scheduling](https://arxiv.org/abs/2607.17842v1)**  
  Authors: Tingjia Zhang, Bo Chen, Shengzhong Liu, Fan Wu, Guihai Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17842v1.pdf)  
  Keywords: real-time rendering, efficient, gaussian splatting, ar, high-fidelity, neural rendering, 3d gaussian  
- **[Points as Tori: Fast Pointwise Signed Distance for Point Clouds](https://arxiv.org/abs/2607.16946v1)**  
  Authors: Nicole Feng, Ioannis Gkioulekas, Keenan Crane  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16946v1.pdf)  
  Keywords: ar, fast, 3d gaussian, face  
- **[Splat-based 3D Scene Reconstruction with Extreme Motion-blur](https://arxiv.org/abs/2607.16926v1)**  
  Authors: Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16926v1.pdf) | [![GitHub](https://img.shields.io/github/stars/KAIST-VCLAB/gs-extreme-motion-blur?style=social)](https://github.com/KAIST-VCLAB/gs-extreme-motion-blur)  
  Keywords: robotics, geometry, fast, gaussian splatting, 3d reconstruction, ar, lighting, illumination, motion, 3d gaussian, mapping  
- **[JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting](https://arxiv.org/abs/2607.14990v1)**  
  Authors: Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14990v1.pdf)  
  Keywords: real-time rendering, geometry, fast, gaussian splatting, ar, motion, 3d gaussian, face  
- **[Compression of 3D Gaussian Splatting Data Using GPU-friendly Graphics Texture Coding](https://arxiv.org/abs/2607.14513v1)**  
  Authors: Amir Said, Randall Rauwendaal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14513v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, acceleration, 3d gaussian, compression  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: real-time rendering, efficient, recognition, fast, gaussian splatting, ar, large scene, motion, 3d gaussian, slam  
- **[G$^2$SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction](https://arxiv.org/abs/2607.14470v1)**  
  Authors: Dasong Gao, Vivienne Sze, Sertac Karaman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14470v1.pdf)  
  Keywords: efficient, geometry, fast, gaussian splatting, ar, lightweight, high-fidelity, 3d gaussian, face  

### Applications

*Showing the latest 50 out of 498 papers*

- **[Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window](https://arxiv.org/abs/2607.21471v1)**  
  Authors: Yukun Shi, Minglun Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21471v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ricky-S/futuresurf?style=social)](https://github.com/Ricky-S/futuresurf)  
  Keywords: geometry, deformation, ar, motion, dynamic, face  
- **[GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis](https://arxiv.org/abs/2607.21448v1)**  
  Authors: Jiahao He, Yihua Shao, Zhengkai Zhao, Pan Gao, Fei Ma, Jingcai Guo, Hao Tang, Nicu Sebe, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21448v1.pdf)  
  Keywords: compact, efficient, gaussian splatting, deformation, ar, motion, 3d gaussian, dynamic  
- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: geometry, gaussian splatting, outdoor, lightweight, ar, mapping, 3d gaussian, tracking, slam, localization  
- **[Construction and Dynamic Update of Channel Gain Maps via 3D Gaussian Splatting](https://arxiv.org/abs/2607.21099v1)**  
  Authors: Yilong Chen, Yuan Guo, Juncong Zhou, Jie Xu, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21099v1.pdf)  
  Keywords: compact, efficient, geometry, fast, gaussian splatting, ar, 3d gaussian, dynamic  
- **[SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization](https://arxiv.org/abs/2607.20813v1)**  
  Authors: Jiun Lee, Jaekwang Kim, Sangmin Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20813v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, high-fidelity, face  
- **[3D-GIMP: When 3D Gaussian Inpainting Meets PatchMatch](https://arxiv.org/abs/2607.20789v1)**  
  Authors: Xuening Tian, Dieter Schmalstieg, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20789v1.pdf)  
  Keywords: gaussian splatting, ar, 3d reconstruction, high-fidelity, 3d gaussian  
- **[RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring](https://arxiv.org/abs/2607.20628v1)**  
  Authors: Renbiao Jin, Mingxin Yang, Yutian Chen, Junhao Zhuang, Xin Cai, Mulin Yu, Linning Xu, Wenxian Yu, Danping Zou, Shi Guo, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20628v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rbjin.github.io/RealVDeblur)  
  Keywords: efficient, gaussian splatting, 3d reconstruction, ar, motion, 3d gaussian, semantic, compression  
- **[ATSplat: Compact Feed-forward 3D Gaussian Splatting with Adaptive Token Expansion](https://arxiv.org/abs/2607.20417v1)**  
  Authors: Cho In, Jeonghwan Cho, Mijin Yoo, Gim Hee Lee, Seon Joo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20417v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, compact  
- **[MR-Compare: A Mixed-Reality Framework for Spatially Grounded Visual Comparison of 3D Gaussian Splatting and Mesh Reconstructions with the Physical Environment](https://arxiv.org/abs/2607.20325v1)**  
  Authors: Changrui Zhu, Ernst Kruijff, Pengju Zhang, Simon Julier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20325v1.pdf) | [![GitHub](https://img.shields.io/github/stars/changruizhu96/MR-Compare?style=social)](https://github.com/changruizhu96/MR-Compare)  
  Keywords: ar, gaussian splatting, 3d gaussian  
- **[Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering](https://arxiv.org/abs/2607.19893v1)**  
  Authors: Zhenxiang Ma, Zeyu He, Yuanzhen Zhou, Zhenyu Yang, Yuchang Zhang, Miao Tao, Rong Fu, Jidong Zhai, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19893v1.pdf)  
  Keywords: ar, head, large scene, neural rendering  

### Avatar Generation

*Showing the latest 50 out of 172 papers*

- **[Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window](https://arxiv.org/abs/2607.21471v1)**  
  Authors: Yukun Shi, Minglun Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21471v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ricky-S/futuresurf?style=social)](https://github.com/Ricky-S/futuresurf)  
  Keywords: geometry, deformation, ar, motion, dynamic, face  
- **[SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization](https://arxiv.org/abs/2607.20813v1)**  
  Authors: Jiun Lee, Jaekwang Kim, Sangmin Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20813v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, high-fidelity, face  
- **[Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering](https://arxiv.org/abs/2607.19893v1)**  
  Authors: Zhenxiang Ma, Zeyu He, Yuanzhen Zhou, Zhenyu Yang, Yuchang Zhang, Miao Tao, Rong Fu, Jidong Zhai, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19893v1.pdf)  
  Keywords: ar, head, large scene, neural rendering  
- **[FlexiAvatar: Unified 3D Gaussian Human Avatars Under Arbitrary Body Visibility](https://arxiv.org/abs/2607.19100v1)**  
  Authors: Yihalem Yimolal Tiruneh, Muhammad Salman Ali, Uyoung Jeong, Muneeb A. Khan, MD Khalequzzaman Chowdhury Sayem, Allanur Bayramgeldiyev, Binod Bhattarai, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19100v1.pdf)  
  Keywords: human, body, gaussian splatting, ar, neural rendering, 3d gaussian, head, tracking, avatar, vr  
- **[ZeroSplat: Generalized Referring Segmentation in 3D Gaussian Splatting](https://arxiv.org/abs/2607.18801v1)**  
  Authors: Jiayu Ding, Meilu Song, Xiaoyi Zhang, Hongbo Jin, Yichen Jin, Xiangtian Si  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18801v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://inkmind-ai.github.io/ZeroSplat)  
  Keywords: understanding, segmentation, gaussian splatting, ar, 3d gaussian, head, dynamic, semantic  
- **[FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System](https://arxiv.org/abs/2607.17803v1)**  
  Authors: Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17803v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CPREgroup/FF-ProCams?style=social)](https://github.com/CPREgroup/FF-ProCams)  
  Keywords: relightable, gaussian splatting, 3d reconstruction, lightweight, ar, high-fidelity, illumination, 3d gaussian, head, mapping, face  
- **[FillGauss: Fine-Grained Filling-Aware Impact Sound Generation for 3D Gaussian Splatting](https://arxiv.org/abs/2607.17773v1)**  
  Authors: Chen Yang, Ganye Wen, Bin Huang, Jiayi Lyu, Zehai Niu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17773v1.pdf)  
  Keywords: geometry, gaussian splatting, ar, high-fidelity, 3d gaussian, face  
- **[RayOcc: Occlusion-Aware Ray Occupancy Estimation via Gaussian Mixture Intensity](https://arxiv.org/abs/2607.17660v1)**  
  Authors: Junho Kim, Seongwon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17660v1.pdf)  
  Keywords: ar, 3d gaussian, face, semantic  
- **[GEAR: Reconstruction of Classical Paintings via Geometry Grounding and Appearance Restitution](https://arxiv.org/abs/2607.17519v1)**  
  Authors: Qinyu Zhang, Xinda Liu, Yunchen Li, Yunzhuo Liu, Chenxi Hu, Kang Li, Guohua Geng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17519v1.pdf)  
  Keywords: geometry, human, 3d reconstruction, ar, lighting, illumination, 3d gaussian  
- **[Points as Tori: Fast Pointwise Signed Distance for Point Clouds](https://arxiv.org/abs/2607.16946v1)**  
  Authors: Nicole Feng, Ioannis Gkioulekas, Keenan Crane  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16946v1.pdf)  
  Keywords: ar, fast, 3d gaussian, face  

### Dynamic Scene

*Showing the latest 50 out of 185 papers*

- **[Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window](https://arxiv.org/abs/2607.21471v1)**  
  Authors: Yukun Shi, Minglun Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21471v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ricky-S/futuresurf?style=social)](https://github.com/Ricky-S/futuresurf)  
  Keywords: geometry, deformation, ar, motion, dynamic, face  
- **[GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis](https://arxiv.org/abs/2607.21448v1)**  
  Authors: Jiahao He, Yihua Shao, Zhengkai Zhao, Pan Gao, Fei Ma, Jingcai Guo, Hao Tang, Nicu Sebe, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21448v1.pdf)  
  Keywords: compact, efficient, gaussian splatting, deformation, ar, motion, 3d gaussian, dynamic  
- **[Construction and Dynamic Update of Channel Gain Maps via 3D Gaussian Splatting](https://arxiv.org/abs/2607.21099v1)**  
  Authors: Yilong Chen, Yuan Guo, Juncong Zhou, Jie Xu, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21099v1.pdf)  
  Keywords: compact, efficient, geometry, fast, gaussian splatting, ar, 3d gaussian, dynamic  
- **[RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring](https://arxiv.org/abs/2607.20628v1)**  
  Authors: Renbiao Jin, Mingxin Yang, Yutian Chen, Junhao Zhuang, Xin Cai, Mulin Yu, Linning Xu, Wenxian Yu, Danping Zou, Shi Guo, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20628v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rbjin.github.io/RealVDeblur)  
  Keywords: efficient, gaussian splatting, 3d reconstruction, ar, motion, 3d gaussian, semantic, compression  
- **[ZeroSplat: Generalized Referring Segmentation in 3D Gaussian Splatting](https://arxiv.org/abs/2607.18801v1)**  
  Authors: Jiayu Ding, Meilu Song, Xiaoyi Zhang, Hongbo Jin, Yichen Jin, Xiangtian Si  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18801v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://inkmind-ai.github.io/ZeroSplat)  
  Keywords: understanding, segmentation, gaussian splatting, ar, 3d gaussian, head, dynamic, semantic  
- **[AniGS: Bridging Rendering and Diffusion Prior for 3D Scene Animation](https://arxiv.org/abs/2607.18539v1)**  
  Authors: Yen-Chi Cheng, Chen Gao, Chuhan Chen, Tuotuo Li, Rajvi Shah, Ayush Saraf, Changil Kim, Liangyan Gui, Alexander Schwing, Johannes Kopf, Hung-Yu Tseng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18539v1.pdf)  
  Keywords: gaussian splatting, deformation, outdoor, ar, animation, motion, 3d gaussian, dynamic  
- **[ECoNGS: Efficient Compressive Neural Gaussian Splats for Volume Visualization](https://arxiv.org/abs/2607.18466v1)**  
  Authors: Kaiyuan Tang, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18466v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/ECoNGS?style=social)](https://github.com/TouKaienn/ECoNGS)  
  Keywords: compact, efficient, gaussian splatting, ar, lightweight, lighting, dynamic, vr  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: geometry, outdoor, ar, illumination, motion, 3d gaussian, tracking, mapping, dynamic, vr  
- **[Splat-based 3D Scene Reconstruction with Extreme Motion-blur](https://arxiv.org/abs/2607.16926v1)**  
  Authors: Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16926v1.pdf) | [![GitHub](https://img.shields.io/github/stars/KAIST-VCLAB/gs-extreme-motion-blur?style=social)](https://github.com/KAIST-VCLAB/gs-extreme-motion-blur)  
  Keywords: robotics, geometry, fast, gaussian splatting, 3d reconstruction, ar, lighting, illumination, motion, 3d gaussian, mapping  
- **[SPARE-GS: Structural Parsimony and Resource Efficiency for 3D Gaussian Splatting](https://arxiv.org/abs/2607.16624v1)**  
  Authors: Zhang Chen, Shuai Wan, Fuzheng Yang, Jiazhi Xia, Weiyao Lin, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16624v1.pdf)  
  Keywords: compact, gaussian splatting, ar, high-fidelity, 3d gaussian, dynamic, compression  

### Few-shot

- **[Calibrated Closed-Form Uncertainty for Radiative Gaussian Splatting in Sparse-View CT](https://arxiv.org/abs/2607.13682v1)**  
  Authors: Chulin Zhao, Yiran Xu, Shu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13682v1.pdf)  
  Keywords: ar, fast, gaussian splatting, sparse-view  
- **[MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction](https://arxiv.org/abs/2607.10792v1)**  
  Authors: Jinqian Yang, Yichen Wu, Wanhua Li, Haokun Lin, Renzhen Wang, Xiangchu Feng, Xixi Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.10792v1.pdf)  
  Keywords: sparse-view, geometry, gaussian splatting, ar, high-fidelity, neural rendering, 3d gaussian, semantic  
- **[Rendering-Aware Bayesian 3D Gaussian Splatting with Native Uncertainty and Adaptive Complexity Control](https://arxiv.org/abs/2607.05522v1)**  
  Authors: Gaoxiang Jia, Vikram Appia, Junzhou Huang, Xinlei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05522v1.pdf)  
  Keywords: geometry, gaussian splatting, ar, 3d gaussian, sparse view  
- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771v1)**  
  Authors: Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03771v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/VOP-GS)  
  Keywords: efficient, geometry, gaussian splatting, ar, large scene, 3d gaussian, face, sparse view  
- **[Sparse-View Surface Reconstruction using Gaussian Splatting through High-Confidence Depth Propagation with Normal Priors](https://arxiv.org/abs/2607.03765v1)**  
  Authors: Liang Han, Bangcai Wei, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03765v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/DP-GS)  
  Keywords: sparse-view, geometry, gaussian splatting, 3d reconstruction, ar, high-fidelity, 3d gaussian, face, sparse view  
- **[Fast 3D Foundation Model Initialized Gaussian Splatting](https://arxiv.org/abs/2607.03209v1)**  
  Authors: Anurag Dalal, Daniel Hagen, Kjell G. Robbersmyr, Kristian Muri Knausgård  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03209v1.pdf)  
  Keywords: sparse-view, nerf, robotics, fast, gaussian splatting, ar, motion, 3d gaussian, vr  
- **[Improving Sparse-View 3DGS Generalization via Flat Minima Optimization](https://arxiv.org/abs/2607.00885v1)**  
  Authors: Kangmin Seo, Sangeek Hyun, MinKyu Lee, Jae-Pil Heo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00885v1.pdf)  
  Keywords: real-time rendering, sparse-view, nerf, efficient, fast, gaussian splatting, ar, lightweight, neural rendering, 3d gaussian, dynamic  
- **[AugSplat: Radiance Field-Informed Gaussian Splatting for Sparse-View Settings](https://arxiv.org/abs/2606.31556v1)**  
  Authors: Lorenzo Lazzaroni, Riccardo Bollati, Daniel Barath, Michael Niemeyer, Keisuke Tateno  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31556v1.pdf)  
  Keywords: real-time rendering, sparse-view, nerf, geometry, gaussian splatting, ar  
- **[StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors](https://arxiv.org/abs/2606.30545v2)**  
  Authors: Wenhao Yuan, Yiyuan Ge, Deli Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30545v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://stringerywh00.github.io/StereoGS_project_page)  
  Keywords: sparse-view, nerf, geometry, gaussian splatting, ar, 3d gaussian, head, dynamic, face  
- **[HiReFF: High-Resolution Feedforward Human Reconstruction from Uncalibrated Sparse-View Video](https://arxiv.org/abs/2606.29333v1)**  
  Authors: Yiming Jiang, Hanzhang Tu, Wenfeng Song, Siyou Lin, Liang An, Shuai Li, Aimin Hao, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29333v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://iridescentjiang.github.io/HiReFF)  
  Keywords: sparse-view, efficient, human, ar, 3d gaussian, head, vr  

### Geometry Reconstruction

*Showing the latest 50 out of 212 papers*

- **[Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window](https://arxiv.org/abs/2607.21471v1)**  
  Authors: Yukun Shi, Minglun Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21471v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ricky-S/futuresurf?style=social)](https://github.com/Ricky-S/futuresurf)  
  Keywords: geometry, deformation, ar, motion, dynamic, face  
- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: geometry, gaussian splatting, outdoor, lightweight, ar, mapping, 3d gaussian, tracking, slam, localization  
- **[Construction and Dynamic Update of Channel Gain Maps via 3D Gaussian Splatting](https://arxiv.org/abs/2607.21099v1)**  
  Authors: Yilong Chen, Yuan Guo, Juncong Zhou, Jie Xu, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21099v1.pdf)  
  Keywords: compact, efficient, geometry, fast, gaussian splatting, ar, 3d gaussian, dynamic  
- **[3D-GIMP: When 3D Gaussian Inpainting Meets PatchMatch](https://arxiv.org/abs/2607.20789v1)**  
  Authors: Xuening Tian, Dieter Schmalstieg, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20789v1.pdf)  
  Keywords: gaussian splatting, ar, 3d reconstruction, high-fidelity, 3d gaussian  
- **[RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring](https://arxiv.org/abs/2607.20628v1)**  
  Authors: Renbiao Jin, Mingxin Yang, Yutian Chen, Junhao Zhuang, Xin Cai, Mulin Yu, Linning Xu, Wenxian Yu, Danping Zou, Shi Guo, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20628v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rbjin.github.io/RealVDeblur)  
  Keywords: efficient, gaussian splatting, 3d reconstruction, ar, motion, 3d gaussian, semantic, compression  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: geometry, outdoor, ar, illumination, motion, 3d gaussian, tracking, mapping, dynamic, vr  
- **[FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System](https://arxiv.org/abs/2607.17803v1)**  
  Authors: Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17803v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CPREgroup/FF-ProCams?style=social)](https://github.com/CPREgroup/FF-ProCams)  
  Keywords: relightable, gaussian splatting, 3d reconstruction, lightweight, ar, high-fidelity, illumination, 3d gaussian, head, mapping, face  
- **[FillGauss: Fine-Grained Filling-Aware Impact Sound Generation for 3D Gaussian Splatting](https://arxiv.org/abs/2607.17773v1)**  
  Authors: Chen Yang, Ganye Wen, Bin Huang, Jiayi Lyu, Zehai Niu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17773v1.pdf)  
  Keywords: geometry, gaussian splatting, ar, high-fidelity, 3d gaussian, face  
- **[GEAR: Reconstruction of Classical Paintings via Geometry Grounding and Appearance Restitution](https://arxiv.org/abs/2607.17519v1)**  
  Authors: Qinyu Zhang, Xinda Liu, Yunchen Li, Yunzhuo Liu, Chenxi Hu, Kang Li, Guohua Geng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17519v1.pdf)  
  Keywords: geometry, human, 3d reconstruction, ar, lighting, illumination, 3d gaussian  
- **[Splat-based 3D Scene Reconstruction with Extreme Motion-blur](https://arxiv.org/abs/2607.16926v1)**  
  Authors: Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16926v1.pdf) | [![GitHub](https://img.shields.io/github/stars/KAIST-VCLAB/gs-extreme-motion-blur?style=social)](https://github.com/KAIST-VCLAB/gs-extreme-motion-blur)  
  Keywords: robotics, geometry, fast, gaussian splatting, 3d reconstruction, ar, lighting, illumination, motion, 3d gaussian, mapping  

### Large Scene

- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: geometry, gaussian splatting, outdoor, lightweight, ar, mapping, 3d gaussian, tracking, slam, localization  
- **[Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering](https://arxiv.org/abs/2607.19893v1)**  
  Authors: Zhenxiang Ma, Zeyu He, Yuanzhen Zhou, Zhenyu Yang, Yuchang Zhang, Miao Tao, Rong Fu, Jidong Zhai, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19893v1.pdf)  
  Keywords: ar, head, large scene, neural rendering  
- **[AniGS: Bridging Rendering and Diffusion Prior for 3D Scene Animation](https://arxiv.org/abs/2607.18539v1)**  
  Authors: Yen-Chi Cheng, Chen Gao, Chuhan Chen, Tuotuo Li, Rajvi Shah, Ayush Saraf, Changil Kim, Liangyan Gui, Alexander Schwing, Johannes Kopf, Hung-Yu Tseng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18539v1.pdf)  
  Keywords: gaussian splatting, deformation, outdoor, ar, animation, motion, 3d gaussian, dynamic  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: geometry, outdoor, ar, illumination, motion, 3d gaussian, tracking, mapping, dynamic, vr  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: real-time rendering, efficient, recognition, fast, gaussian splatting, ar, large scene, motion, 3d gaussian, slam  
- **[GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors](https://arxiv.org/abs/2607.11184v1)**  
  Authors: Ruilan Gao, Letian Jin, Yu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11184v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rlgao.github.io/geogs_slam)  
  Keywords: geometry, gaussian splatting, outdoor, ar, mapping, 3d gaussian, tracking, slam  
- **[Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction](https://arxiv.org/abs/2607.08769v1)**  
  Authors: Weijian Chen, Weibo Yao, Yuhang Zhang, Xiaolin Tang, Guo Wang, Weijun Zhang, Xitong Gao, Yihao Chen, Hongde Qin, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08769v1.pdf)  
  Keywords: geometry, gaussian splatting, ar, outdoor, 3d gaussian  
- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771v1)**  
  Authors: Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03771v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/VOP-GS)  
  Keywords: efficient, geometry, gaussian splatting, ar, large scene, 3d gaussian, face, sparse view  
- **[Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673v1)**  
  Authors: Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu, Krishna Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00673v1.pdf)  
  Keywords: human, deformation, ar, outdoor, 3d gaussian  
- **[GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping](https://arxiv.org/abs/2606.30809v1)**  
  Authors: Annika Thomas, Mason Peterson, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30809v1.pdf)  
  Keywords: geometry, gaussian splatting, outdoor, ar, 3d gaussian, mapping  

### Model Compression

*Showing the latest 50 out of 185 papers*

- **[GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis](https://arxiv.org/abs/2607.21448v1)**  
  Authors: Jiahao He, Yihua Shao, Zhengkai Zhao, Pan Gao, Fei Ma, Jingcai Guo, Hao Tang, Nicu Sebe, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21448v1.pdf)  
  Keywords: compact, efficient, gaussian splatting, deformation, ar, motion, 3d gaussian, dynamic  
- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: geometry, gaussian splatting, outdoor, lightweight, ar, mapping, 3d gaussian, tracking, slam, localization  
- **[Construction and Dynamic Update of Channel Gain Maps via 3D Gaussian Splatting](https://arxiv.org/abs/2607.21099v1)**  
  Authors: Yilong Chen, Yuan Guo, Juncong Zhou, Jie Xu, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21099v1.pdf)  
  Keywords: compact, efficient, geometry, fast, gaussian splatting, ar, 3d gaussian, dynamic  
- **[SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization](https://arxiv.org/abs/2607.20813v1)**  
  Authors: Jiun Lee, Jaekwang Kim, Sangmin Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20813v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, high-fidelity, face  
- **[RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring](https://arxiv.org/abs/2607.20628v1)**  
  Authors: Renbiao Jin, Mingxin Yang, Yutian Chen, Junhao Zhuang, Xin Cai, Mulin Yu, Linning Xu, Wenxian Yu, Danping Zou, Shi Guo, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20628v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rbjin.github.io/RealVDeblur)  
  Keywords: efficient, gaussian splatting, 3d reconstruction, ar, motion, 3d gaussian, semantic, compression  
- **[ATSplat: Compact Feed-forward 3D Gaussian Splatting with Adaptive Token Expansion](https://arxiv.org/abs/2607.20417v1)**  
  Authors: Cho In, Jeonghwan Cho, Mijin Yoo, Gim Hee Lee, Seon Joo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20417v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, compact  
- **[Look Before You Edit: Attention-Guided Camera Placement and Multi-View Alignment for 3D Gaussian Splatting Editing](https://arxiv.org/abs/2607.19777v1)**  
  Authors: Jaeyeon Park, Taeho Kang, Youngki Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19777v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, compact  
- **[ECoNGS: Efficient Compressive Neural Gaussian Splats for Volume Visualization](https://arxiv.org/abs/2607.18466v1)**  
  Authors: Kaiyuan Tang, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18466v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/ECoNGS?style=social)](https://github.com/TouKaienn/ECoNGS)  
  Keywords: compact, efficient, gaussian splatting, ar, lightweight, lighting, dynamic, vr  
- **[QIRF Quantum-Inspired Non-Orthogonal Function-Space Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2607.18067v1)**  
  Authors: Shizeng Jiang, Hao Zhang, Xuerui Ma, Ying Hu, Tao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18067v1.pdf)  
  Keywords: real-time rendering, nerf, gaussian splatting, ar, 3d gaussian, compression  
- **[Packet-Loss Robust 3D Gaussian Compression via Atomic Packaging and GNN-based Error Concealment](https://arxiv.org/abs/2607.17916v1)**  
  Authors: Yuxuan Tao, Xuerui Ma, Hao Zhang, Chunhua Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17916v1.pdf)  
  Keywords: nerf, gaussian splatting, ar, lightweight, high-fidelity, neural rendering, 3d gaussian, compression  

### Quality Enhancement

*Showing the latest 50 out of 119 papers*

- **[SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization](https://arxiv.org/abs/2607.20813v1)**  
  Authors: Jiun Lee, Jaekwang Kim, Sangmin Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20813v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, high-fidelity, face  
- **[3D-GIMP: When 3D Gaussian Inpainting Meets PatchMatch](https://arxiv.org/abs/2607.20789v1)**  
  Authors: Xuening Tian, Dieter Schmalstieg, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20789v1.pdf)  
  Keywords: gaussian splatting, ar, 3d reconstruction, high-fidelity, 3d gaussian  
- **[Exploration Matters for Escaping the Blur Trap in 3D Gaussian Splatting](https://arxiv.org/abs/2607.17965v1)**  
  Authors: Chengbo Wang, Guozheng Ma, Jinhong Wu, Tie Ji, Yizhen Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17965v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chengbo-wang.github.io/ExploreGS)  
  Keywords: ar, gaussian splatting, 3d gaussian, high-fidelity  
- **[Packet-Loss Robust 3D Gaussian Compression via Atomic Packaging and GNN-based Error Concealment](https://arxiv.org/abs/2607.17916v1)**  
  Authors: Yuxuan Tao, Xuerui Ma, Hao Zhang, Chunhua Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17916v1.pdf)  
  Keywords: nerf, gaussian splatting, ar, lightweight, high-fidelity, neural rendering, 3d gaussian, compression  
- **[CaT-GS: Efficient 3DGS Rendering for Large Scale Scenes via Inter-frame Caching and Tile Scheduling](https://arxiv.org/abs/2607.17842v1)**  
  Authors: Tingjia Zhang, Bo Chen, Shengzhong Liu, Fan Wu, Guihai Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17842v1.pdf)  
  Keywords: real-time rendering, efficient, gaussian splatting, ar, high-fidelity, neural rendering, 3d gaussian  
- **[FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System](https://arxiv.org/abs/2607.17803v1)**  
  Authors: Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17803v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CPREgroup/FF-ProCams?style=social)](https://github.com/CPREgroup/FF-ProCams)  
  Keywords: relightable, gaussian splatting, 3d reconstruction, lightweight, ar, high-fidelity, illumination, 3d gaussian, head, mapping, face  
- **[FillGauss: Fine-Grained Filling-Aware Impact Sound Generation for 3D Gaussian Splatting](https://arxiv.org/abs/2607.17773v1)**  
  Authors: Chen Yang, Ganye Wen, Bin Huang, Jiayi Lyu, Zehai Niu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17773v1.pdf)  
  Keywords: geometry, gaussian splatting, ar, high-fidelity, 3d gaussian, face  
- **[SPARE-GS: Structural Parsimony and Resource Efficiency for 3D Gaussian Splatting](https://arxiv.org/abs/2607.16624v1)**  
  Authors: Zhang Chen, Shuai Wan, Fuzheng Yang, Jiazhi Xia, Weiyao Lin, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16624v1.pdf)  
  Keywords: compact, gaussian splatting, ar, high-fidelity, 3d gaussian, dynamic, compression  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: geometry, human, gaussian splatting, ar, high-fidelity, reflection, motion, 3d gaussian, ray tracing, dynamic, face  
- **[G$^2$SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction](https://arxiv.org/abs/2607.14470v1)**  
  Authors: Dasong Gao, Vivienne Sze, Sertac Karaman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14470v1.pdf)  
  Keywords: efficient, geometry, fast, gaussian splatting, ar, lightweight, high-fidelity, 3d gaussian, face  

### Ray Tracing

- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: geometry, human, gaussian splatting, ar, high-fidelity, reflection, motion, 3d gaussian, ray tracing, dynamic, face  
- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: compact, geometry, ray casting, human, gaussian splatting, ar  
- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869v1)**  
  Authors: Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30869v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gray)  
  Keywords: fast, gaussian splatting, ar, 3d gaussian, ray tracing  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: real-time rendering, efficient, geometry, fast, gaussian splatting, ar, path tracing, reflection, 3d gaussian, ray tracing  
- **[RenderFormer++: Scalable and Physically Grounded Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v1)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jinyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v1.pdf)  
  Keywords: compact, ar, light transport, neural rendering, illumination, global illumination  
- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: efficient, geometry, gaussian splatting, 3d reconstruction, ar, illumination, 3d gaussian, global illumination  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: gaussian splatting, ar, high-fidelity, illumination, global illumination  
- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314v1)**  
  Authors: Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11314v1.pdf)  
  Keywords: geometry, 3d reconstruction, relighting, light transport, lightweight, neural rendering, lighting, ar, motion, 3d gaussian, ray tracing, dynamic  
- **[PTIR-GS: Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606v3)**  
  Authors: Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09606v3.pdf)  
  Keywords: shadow, compact, relighting, light transport, ar, path tracing, lighting, illumination, reflection, 3d gaussian, ray tracing, global illumination  
- **[RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation](https://arxiv.org/abs/2606.01261v1)**  
  Authors: Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.01261v1.pdf)  
  Keywords: efficient, geometry, segmentation, gaussian splatting, ar, reflection, 3d gaussian, ray tracing, semantic  

### Relighting

*Showing the latest 50 out of 53 papers*

- **[ECoNGS: Efficient Compressive Neural Gaussian Splats for Volume Visualization](https://arxiv.org/abs/2607.18466v1)**  
  Authors: Kaiyuan Tang, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18466v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/ECoNGS?style=social)](https://github.com/TouKaienn/ECoNGS)  
  Keywords: compact, efficient, gaussian splatting, ar, lightweight, lighting, dynamic, vr  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: geometry, outdoor, ar, illumination, motion, 3d gaussian, tracking, mapping, dynamic, vr  
- **[FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System](https://arxiv.org/abs/2607.17803v1)**  
  Authors: Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17803v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CPREgroup/FF-ProCams?style=social)](https://github.com/CPREgroup/FF-ProCams)  
  Keywords: relightable, gaussian splatting, 3d reconstruction, lightweight, ar, high-fidelity, illumination, 3d gaussian, head, mapping, face  
- **[GEAR: Reconstruction of Classical Paintings via Geometry Grounding and Appearance Restitution](https://arxiv.org/abs/2607.17519v1)**  
  Authors: Qinyu Zhang, Xinda Liu, Yunchen Li, Yunzhuo Liu, Chenxi Hu, Kang Li, Guohua Geng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17519v1.pdf)  
  Keywords: geometry, human, 3d reconstruction, ar, lighting, illumination, 3d gaussian  
- **[Splat-based 3D Scene Reconstruction with Extreme Motion-blur](https://arxiv.org/abs/2607.16926v1)**  
  Authors: Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16926v1.pdf) | [![GitHub](https://img.shields.io/github/stars/KAIST-VCLAB/gs-extreme-motion-blur?style=social)](https://github.com/KAIST-VCLAB/gs-extreme-motion-blur)  
  Keywords: robotics, geometry, fast, gaussian splatting, 3d reconstruction, ar, lighting, illumination, motion, 3d gaussian, mapping  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: geometry, human, gaussian splatting, ar, high-fidelity, reflection, motion, 3d gaussian, ray tracing, dynamic, face  
- **[GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM](https://arxiv.org/abs/2607.07452v1)**  
  Authors: Lipu Zhou, Yaoyun Kang, Junxiang Pang, Shengkai Sun, Tingting Bao, Kehan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07452v1.pdf)  
  Keywords: robotics, geometry, gaussian splatting, 3d reconstruction, ar, mapping, illumination, slam  
- **[PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution](https://arxiv.org/abs/2607.06238v1)**  
  Authors: Lihua Wei, Huatong Gao, Jia Gong, Zhiyu Tan, Hao Li, Jun Liu, Zhihua Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06238v1.pdf)  
  Keywords: gaussian splatting, ar, lighting, mapping, dynamic  
- **[WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images](https://arxiv.org/abs/2607.05347v1)**  
  Authors: Xiyu Zhang, Jingyu Zhuang, Hongjia Zhai, Zizheng Yan, Jinwei Chen, Guofeng Zhang, Qingnan Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05347v1.pdf)  
  Keywords: efficient, geometry, gaussian splatting, 3d reconstruction, ar, illumination, 3d gaussian, face  
- **[InvSplat: Inverse Feed-Forward Scene Splatting](https://arxiv.org/abs/2607.02301v1)**  
  Authors: Polina Karpikova, Wenjing Bian, Haofei Xu, Hendrik Lensch, Andreas Geiger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.02301v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://poliik.github.io/invsplat)  
  Keywords: geometry, 3d reconstruction, relighting, ar, lighting, 3d gaussian  

### SLAM

*Showing the latest 50 out of 76 papers*

- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: geometry, gaussian splatting, outdoor, lightweight, ar, mapping, 3d gaussian, tracking, slam, localization  
- **[FlexiAvatar: Unified 3D Gaussian Human Avatars Under Arbitrary Body Visibility](https://arxiv.org/abs/2607.19100v1)**  
  Authors: Yihalem Yimolal Tiruneh, Muhammad Salman Ali, Uyoung Jeong, Muneeb A. Khan, MD Khalequzzaman Chowdhury Sayem, Allanur Bayramgeldiyev, Binod Bhattarai, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19100v1.pdf)  
  Keywords: human, body, gaussian splatting, ar, neural rendering, 3d gaussian, head, tracking, avatar, vr  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: geometry, outdoor, ar, illumination, motion, 3d gaussian, tracking, mapping, dynamic, vr  
- **[FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System](https://arxiv.org/abs/2607.17803v1)**  
  Authors: Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17803v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CPREgroup/FF-ProCams?style=social)](https://github.com/CPREgroup/FF-ProCams)  
  Keywords: relightable, gaussian splatting, 3d reconstruction, lightweight, ar, high-fidelity, illumination, 3d gaussian, head, mapping, face  
- **[Splat-based 3D Scene Reconstruction with Extreme Motion-blur](https://arxiv.org/abs/2607.16926v1)**  
  Authors: Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16926v1.pdf) | [![GitHub](https://img.shields.io/github/stars/KAIST-VCLAB/gs-extreme-motion-blur?style=social)](https://github.com/KAIST-VCLAB/gs-extreme-motion-blur)  
  Keywords: robotics, geometry, fast, gaussian splatting, 3d reconstruction, ar, lighting, illumination, motion, 3d gaussian, mapping  
- **[RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping](https://arxiv.org/abs/2607.15048v1)**  
  Authors: Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15048v1.pdf)  
  Keywords: compact, efficient, autonomous driving, ar, 3d gaussian, mapping, face, semantic  
- **[AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight](https://arxiv.org/abs/2607.14997v1)**  
  Authors: Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14997v1.pdf)  
  Keywords: gaussian splatting, ar, motion, 3d gaussian, tracking, dynamic, semantic  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: real-time rendering, efficient, recognition, fast, gaussian splatting, ar, large scene, motion, 3d gaussian, slam  
- **[Bake It Till You Make It: Ultrafast Spatial Texture-Atlas Splatting](https://arxiv.org/abs/2607.13808v1)**  
  Authors: Neel Kelkar, Simon Niedermayr, Kaloian Petkov, Klaus Engel, Rüdiger Westermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13808v1.pdf)  
  Keywords: compact, efficient, geometry, fast, gaussian splatting, ar, 3d gaussian, mapping  
- **[VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation](https://arxiv.org/abs/2607.12356v2)**  
  Authors: Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao, Yan Wu, Wei-Yun Yau, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12356v2.pdf)  
  Keywords: compact, geometry, human, ar, 3d gaussian, mapping, semantic  

### Scene Understanding

*Showing the latest 50 out of 117 papers*

- **[RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring](https://arxiv.org/abs/2607.20628v1)**  
  Authors: Renbiao Jin, Mingxin Yang, Yutian Chen, Junhao Zhuang, Xin Cai, Mulin Yu, Linning Xu, Wenxian Yu, Danping Zou, Shi Guo, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20628v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rbjin.github.io/RealVDeblur)  
  Keywords: efficient, gaussian splatting, 3d reconstruction, ar, motion, 3d gaussian, semantic, compression  
- **[ZeroSplat: Generalized Referring Segmentation in 3D Gaussian Splatting](https://arxiv.org/abs/2607.18801v1)**  
  Authors: Jiayu Ding, Meilu Song, Xiaoyi Zhang, Hongbo Jin, Yichen Jin, Xiangtian Si  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18801v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://inkmind-ai.github.io/ZeroSplat)  
  Keywords: understanding, segmentation, gaussian splatting, ar, 3d gaussian, head, dynamic, semantic  
- **[RayOcc: Occlusion-Aware Ray Occupancy Estimation via Gaussian Mixture Intensity](https://arxiv.org/abs/2607.17660v1)**  
  Authors: Junho Kim, Seongwon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17660v1.pdf)  
  Keywords: ar, 3d gaussian, face, semantic  
- **[TopoGS: Planar Reconstruction via Topology-aware 3D Gaussian Splatting](https://arxiv.org/abs/2607.16838v1)**  
  Authors: Shanshan Pan, Jiale Chen, Yilin Liu, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16838v1.pdf)  
  Keywords: compact, geometry, segmentation, gaussian splatting, 3d reconstruction, ar, 3d gaussian  
- **[RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping](https://arxiv.org/abs/2607.15048v1)**  
  Authors: Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15048v1.pdf)  
  Keywords: compact, efficient, autonomous driving, ar, 3d gaussian, mapping, face, semantic  
- **[AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight](https://arxiv.org/abs/2607.14997v1)**  
  Authors: Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14997v1.pdf)  
  Keywords: gaussian splatting, ar, motion, 3d gaussian, tracking, dynamic, semantic  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: real-time rendering, efficient, recognition, fast, gaussian splatting, ar, large scene, motion, 3d gaussian, slam  
- **[T3HG-Editor: Text-driven 3D Human Garment Editing with Body Priors Embedded in SMPL-X](https://arxiv.org/abs/2607.13654v1)**  
  Authors: Shaoru Sun, Xingtao Wang, Zihan Ma, Wenrui Li, Jiantao Zhou, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13654v1.pdf)  
  Keywords: geometry, human, body, ar, high-fidelity, 3d gaussian, face, semantic  
- **[SaaF: Scene-Specific Ambiguity-Aware 3D Language Fields towards Interactive Real-World Object Retrieval](https://arxiv.org/abs/2607.16309v1)**  
  Authors: Yuga Yano, Daiju Kanaoka, Hakaru Tamukoh, Yasutomo Kawanishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16309v1.pdf)  
  Keywords: understanding, gaussian splatting, ar, semantic, compression  
- **[VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation](https://arxiv.org/abs/2607.12356v2)**  
  Authors: Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao, Yan Wu, Wei-Yun Yau, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12356v2.pdf)  
  Keywords: compact, geometry, human, ar, 3d gaussian, mapping, semantic  



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