# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-07-29 01:29:57

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
- [Avatar Generation](#avatar-generation) (177 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (188 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (38 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (211 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (25 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (186 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (122 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (14 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (56 papers) - Papers about relighting and illumination effects in Gaussian Splatting
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

- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: survey, dynamic, high-fidelity, efficient, 3d gaussian, ar, mapping, tracking, slam, localization  
- **[Recent Advances and Trends in Learning-based 3D Representations](https://arxiv.org/abs/2606.04871v1)**  
  Authors: Adrien Schockaert, Hamid Laga, Hazem Wannous, Vincent Magnier, Guillaume Dufaye, Jean-françois Witz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.04871v1.pdf)  
  Keywords: gaussian splatting, survey, motion, recognition, 4d, medical, autonomous driving, 3d gaussian, ar, vr, 3d reconstruction, compact, neural rendering  
- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137v1)**  
  Authors: Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00137v1.pdf)  
  Keywords: gaussian splatting, survey, geometry, ar, mapping, animation  

### Acceleration

*Showing the latest 50 out of 96 papers*

- **[Head Avatars with Dynamic Explicit Hair](https://arxiv.org/abs/2607.23861v1)**  
  Authors: Vanessa Sklyarova, Haonan Chen, Berna Kabadayi, Tobias Kirschstein, Zicong Fan, Xi Wang, Gerard Pons-Moll, Matthias Nießner, Marc Pollefeys, Michael J. Black, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.23861v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, human, 3d gaussian, deformation, acceleration, avatar, head, ar, tracking, face  
- **[3D Gaussian Splatting for Scientific Particle Data Compression and Rendering](https://arxiv.org/abs/2607.22956v1)**  
  Authors: Bo Jiang, Youyuan Liu, Taolue Yang, Sheng Di, Sian Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22956v1.pdf)  
  Keywords: gaussian splatting, fast, 3d gaussian, ar, compression, compact, lightweight  
- **[Construction and Dynamic Update of Channel Gain Maps via 3D Gaussian Splatting](https://arxiv.org/abs/2607.21099v1)**  
  Authors: Yilong Chen, Yuan Guo, Juncong Zhou, Jie Xu, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21099v1.pdf)  
  Keywords: gaussian splatting, dynamic, fast, geometry, efficient, 3d gaussian, ar, compact  
- **[QIRF Quantum-Inspired Non-Orthogonal Function-Space Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2607.18067v1)**  
  Authors: Shizeng Jiang, Hao Zhang, Xuerui Ma, Ying Hu, Tao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18067v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, compression, nerf, real-time rendering  
- **[Locality-Aware Density Control for Efficient Gaussian-based Image Representation](https://arxiv.org/abs/2607.17896v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Xiandong Meng, Shuai Liu, Chao Li, Fanyang Meng, Youneng Bao, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17896v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ChenJiaCong-1005/LocoADC?style=social)](https://github.com/ChenJiaCong-1005/LocoADC)  
  Keywords: gaussian splatting, ar, efficient, fast  
- **[CaT-GS: Efficient 3DGS Rendering for Large Scale Scenes via Inter-frame Caching and Tile Scheduling](https://arxiv.org/abs/2607.17842v1)**  
  Authors: Tingjia Zhang, Bo Chen, Shengzhong Liu, Fan Wu, Guihai Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17842v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, efficient, 3d gaussian, ar, real-time rendering, neural rendering  
- **[Points as Tori: Fast Pointwise Signed Distance for Point Clouds](https://arxiv.org/abs/2607.16946v1)**  
  Authors: Nicole Feng, Ioannis Gkioulekas, Keenan Crane  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16946v1.pdf)  
  Keywords: face, ar, 3d gaussian, fast  
- **[Splat-based 3D Scene Reconstruction with Extreme Motion-blur](https://arxiv.org/abs/2607.16926v1)**  
  Authors: Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16926v1.pdf) | [![GitHub](https://img.shields.io/github/stars/KAIST-VCLAB/gs-extreme-motion-blur?style=social)](https://github.com/KAIST-VCLAB/gs-extreme-motion-blur)  
  Keywords: gaussian splatting, illumination, motion, fast, lighting, geometry, 3d gaussian, ar, mapping, robotics, 3d reconstruction  
- **[JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting](https://arxiv.org/abs/2607.14990v1)**  
  Authors: Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14990v1.pdf)  
  Keywords: gaussian splatting, motion, fast, geometry, 3d gaussian, ar, real-time rendering, face  
- **[Compression of 3D Gaussian Splatting Data Using GPU-friendly Graphics Texture Coding](https://arxiv.org/abs/2607.14513v1)**  
  Authors: Amir Said, Randall Rauwendaal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14513v1.pdf)  
  Keywords: gaussian splatting, efficient, 3d gaussian, acceleration, ar, compression  

### Applications

*Showing the latest 50 out of 498 papers*

- **[CORF-GS: Real-Time Wireless Radiance Field Reconstruction via Coupled Optical-RF Gaussian Splatting](https://arxiv.org/abs/2607.25569v1)**  
  Authors: Jinya Zhang, Jiajia Guo, Chao-Kai Wen, Shi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25569v1.pdf)  
  Keywords: gaussian splatting, geometry, efficient, 3d gaussian, ar, face  
- **[PanoLess: Environment Reconstruction from Partial Reflective Views](https://arxiv.org/abs/2607.25362v1)**  
  Authors: Ahitagni Das, Ashok Veeraraghavan, Vivek Boominathan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25362v1.pdf)  
  Keywords: illumination, high-fidelity, ar, reflection, face  
- **[SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation](https://arxiv.org/abs/2607.25219v1)**  
  Authors: Weiqi Huang, Dianyi Yang, Jiaxin Li, Shuangyi Dong, Hao Xu, Zan Wang, Wei Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25219v1.pdf)  
  Keywords: gaussian splatting, motion, human, body, 3d gaussian, avatar, ar, semantic  
- **[GenSplatCodec: Feed-Forward Gaussian Splatting Compression via One-Step Diffusion](https://arxiv.org/abs/2607.24403v1)**  
  Authors: Qiang Hu, Zhenlong Wu, Lei Huang, Zihan Zheng, Xiaoyun Zhang, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24403v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, geometry, 3d gaussian, ar, compression, compact, lightweight  
- **[Head Avatars with Dynamic Explicit Hair](https://arxiv.org/abs/2607.23861v1)**  
  Authors: Vanessa Sklyarova, Haonan Chen, Berna Kabadayi, Tobias Kirschstein, Zicong Fan, Xi Wang, Gerard Pons-Moll, Matthias Nießner, Marc Pollefeys, Michael J. Black, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.23861v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, human, 3d gaussian, deformation, acceleration, avatar, head, ar, tracking, face  
- **[Fashion-3DLR: A Controllable 3D Garment Generation Using Pairwise Fashion Elements for Intelligent Design](https://arxiv.org/abs/2607.23189v1)**  
  Authors: Shenghao Yang, Hongtao Zhang, Yuhan Yi, Zhihao Tang, Zihao Cui, Lian Wen, Han Yan, Yuan Gao, Mingbo Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.23189v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d gaussian, ar, semantic  
- **[Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline](https://arxiv.org/abs/2607.22997v1)**  
  Authors: Qing Yang, Xun Wang, Ziguan Wang, Zhenjiang Li, Hongqiang Wang, Dongdong Weng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22997v1.pdf)  
  Keywords: gaussian splatting, motion, human, body, 3d gaussian, ar, semantic  
- **[3D Gaussian Splatting for Scientific Particle Data Compression and Rendering](https://arxiv.org/abs/2607.22956v1)**  
  Authors: Bo Jiang, Youyuan Liu, Taolue Yang, Sheng Di, Sian Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22956v1.pdf)  
  Keywords: gaussian splatting, fast, 3d gaussian, ar, compression, compact, lightweight  
- **[Meshless Domain Randomization via Explicit Parameter Perturbation of 3D Gaussian Splatting](https://arxiv.org/abs/2607.22890v1)**  
  Authors: Felipe Nunes Carbone de Carvalho, Joyce de Morais Souza, Alan de Aguiar, Charles Morphy D. Santos, João Paulo Gois  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22890v1.pdf)  
  Keywords: gaussian splatting, illumination, efficient, 3d gaussian, ar  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: gaussian splatting, illumination, lighting, efficient, ar, reflection, ray tracing, face, relighting  

### Avatar Generation

*Showing the latest 50 out of 177 papers*

- **[CORF-GS: Real-Time Wireless Radiance Field Reconstruction via Coupled Optical-RF Gaussian Splatting](https://arxiv.org/abs/2607.25569v1)**  
  Authors: Jinya Zhang, Jiajia Guo, Chao-Kai Wen, Shi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25569v1.pdf)  
  Keywords: gaussian splatting, geometry, efficient, 3d gaussian, ar, face  
- **[PanoLess: Environment Reconstruction from Partial Reflective Views](https://arxiv.org/abs/2607.25362v1)**  
  Authors: Ahitagni Das, Ashok Veeraraghavan, Vivek Boominathan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25362v1.pdf)  
  Keywords: illumination, high-fidelity, ar, reflection, face  
- **[SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation](https://arxiv.org/abs/2607.25219v1)**  
  Authors: Weiqi Huang, Dianyi Yang, Jiaxin Li, Shuangyi Dong, Hao Xu, Zan Wang, Wei Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25219v1.pdf)  
  Keywords: gaussian splatting, motion, human, body, 3d gaussian, avatar, ar, semantic  
- **[Head Avatars with Dynamic Explicit Hair](https://arxiv.org/abs/2607.23861v1)**  
  Authors: Vanessa Sklyarova, Haonan Chen, Berna Kabadayi, Tobias Kirschstein, Zicong Fan, Xi Wang, Gerard Pons-Moll, Matthias Nießner, Marc Pollefeys, Michael J. Black, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.23861v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, human, 3d gaussian, deformation, acceleration, avatar, head, ar, tracking, face  
- **[Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline](https://arxiv.org/abs/2607.22997v1)**  
  Authors: Qing Yang, Xun Wang, Ziguan Wang, Zhenjiang Li, Hongqiang Wang, Dongdong Weng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22997v1.pdf)  
  Keywords: gaussian splatting, motion, human, body, 3d gaussian, ar, semantic  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: gaussian splatting, illumination, lighting, efficient, ar, reflection, ray tracing, face, relighting  
- **[Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window](https://arxiv.org/abs/2607.21471v1)**  
  Authors: Yukun Shi, Minglun Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21471v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ricky-S/futuresurf?style=social)](https://github.com/Ricky-S/futuresurf)  
  Keywords: motion, dynamic, geometry, deformation, ar, face  
- **[SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization](https://arxiv.org/abs/2607.20813v1)**  
  Authors: Jiun Lee, Jaekwang Kim, Sangmin Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20813v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, efficient, ar, face  
- **[Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering](https://arxiv.org/abs/2607.19893v1)**  
  Authors: Zhenxiang Ma, Zeyu He, Yuanzhen Zhou, Zhenyu Yang, Yuchang Zhang, Miao Tao, Rong Fu, Jidong Zhai, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19893v1.pdf)  
  Keywords: neural rendering, head, large scene, ar  
- **[FlexiAvatar: Unified 3D Gaussian Human Avatars Under Arbitrary Body Visibility](https://arxiv.org/abs/2607.19100v1)**  
  Authors: Yihalem Yimolal Tiruneh, Muhammad Salman Ali, Uyoung Jeong, Muneeb A. Khan, MD Khalequzzaman Chowdhury Sayem, Allanur Bayramgeldiyev, Binod Bhattarai, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19100v1.pdf)  
  Keywords: gaussian splatting, body, human, 3d gaussian, head, avatar, ar, vr, tracking, neural rendering  

### Dynamic Scene

*Showing the latest 50 out of 188 papers*

- **[SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation](https://arxiv.org/abs/2607.25219v1)**  
  Authors: Weiqi Huang, Dianyi Yang, Jiaxin Li, Shuangyi Dong, Hao Xu, Zan Wang, Wei Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25219v1.pdf)  
  Keywords: gaussian splatting, motion, human, body, 3d gaussian, avatar, ar, semantic  
- **[Head Avatars with Dynamic Explicit Hair](https://arxiv.org/abs/2607.23861v1)**  
  Authors: Vanessa Sklyarova, Haonan Chen, Berna Kabadayi, Tobias Kirschstein, Zicong Fan, Xi Wang, Gerard Pons-Moll, Matthias Nießner, Marc Pollefeys, Michael J. Black, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.23861v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, human, 3d gaussian, deformation, acceleration, avatar, head, ar, tracking, face  
- **[Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline](https://arxiv.org/abs/2607.22997v1)**  
  Authors: Qing Yang, Xun Wang, Ziguan Wang, Zhenjiang Li, Hongqiang Wang, Dongdong Weng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22997v1.pdf)  
  Keywords: gaussian splatting, motion, human, body, 3d gaussian, ar, semantic  
- **[Visual Relocalization from Sparse Views in Aliased and Low-Texture Environments via Novel View Synthesis](https://arxiv.org/abs/2607.22147v1)**  
  Authors: Maria Peribañez, Javier Civera, Rudolph Triebel, Riccardo Giubilato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22147v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DLR-RM/multimodal-gsplat-relocalization?style=social)](https://github.com/DLR-RM/multimodal-gsplat-relocalization)  
  Keywords: gaussian splatting, illumination, motion, geometry, sparse view, 3d gaussian, ar, localization  
- **[Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window](https://arxiv.org/abs/2607.21471v1)**  
  Authors: Yukun Shi, Minglun Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21471v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ricky-S/futuresurf?style=social)](https://github.com/Ricky-S/futuresurf)  
  Keywords: motion, dynamic, geometry, deformation, ar, face  
- **[GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis](https://arxiv.org/abs/2607.21448v2)**  
  Authors: Jiahao He, Yihua Shao, Zhengkai Zhao, Pan Gao, Fei Ma, Jingcai Guo, Hao Tang, Nicu Sebe, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21448v2.pdf)  
  Keywords: gaussian splatting, motion, dynamic, efficient, 3d gaussian, deformation, ar, compact  
- **[Construction and Dynamic Update of Channel Gain Maps via 3D Gaussian Splatting](https://arxiv.org/abs/2607.21099v1)**  
  Authors: Yilong Chen, Yuan Guo, Juncong Zhou, Jie Xu, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21099v1.pdf)  
  Keywords: gaussian splatting, dynamic, fast, geometry, efficient, 3d gaussian, ar, compact  
- **[RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring](https://arxiv.org/abs/2607.20628v1)**  
  Authors: Renbiao Jin, Mingxin Yang, Yutian Chen, Junhao Zhuang, Xin Cai, Mulin Yu, Linning Xu, Wenxian Yu, Danping Zou, Shi Guo, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20628v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rbjin.github.io/RealVDeblur)  
  Keywords: gaussian splatting, motion, efficient, 3d gaussian, ar, compression, 3d reconstruction, semantic  
- **[TOM-GS: Editable Video Representation via Temporal Opacity Modulation of Static 3D Gaussians](https://arxiv.org/abs/2607.22717v1)**  
  Authors: Marek Lisowski, Łukasz Smoliński, Kornel Howil, Piotr Biliński, Marcin Mazur, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22717v1.pdf)  
  Keywords: gaussian splatting, dynamic, geometry, 3d gaussian, deformation, ar  
- **[ZeroSplat: Generalized Referring Segmentation in 3D Gaussian Splatting](https://arxiv.org/abs/2607.18801v1)**  
  Authors: Jiayu Ding, Meilu Song, Xiaoyi Zhang, Hongbo Jin, Yichen Jin, Xiangtian Si  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18801v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://inkmind-ai.github.io/ZeroSplat)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, segmentation, head, ar, understanding, semantic  

### Few-shot

- **[Visual Relocalization from Sparse Views in Aliased and Low-Texture Environments via Novel View Synthesis](https://arxiv.org/abs/2607.22147v1)**  
  Authors: Maria Peribañez, Javier Civera, Rudolph Triebel, Riccardo Giubilato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22147v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DLR-RM/multimodal-gsplat-relocalization?style=social)](https://github.com/DLR-RM/multimodal-gsplat-relocalization)  
  Keywords: gaussian splatting, illumination, motion, geometry, sparse view, 3d gaussian, ar, localization  
- **[Calibrated Closed-Form Uncertainty for Radiative Gaussian Splatting in Sparse-View CT](https://arxiv.org/abs/2607.13682v1)**  
  Authors: Chulin Zhao, Yiran Xu, Shu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13682v1.pdf)  
  Keywords: gaussian splatting, ar, sparse-view, fast  
- **[MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction](https://arxiv.org/abs/2607.10792v1)**  
  Authors: Jinqian Yang, Yichen Wu, Wanhua Li, Haokun Lin, Renzhen Wang, Xiangchu Feng, Xixi Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.10792v1.pdf)  
  Keywords: gaussian splatting, sparse-view, high-fidelity, geometry, 3d gaussian, ar, neural rendering, semantic  
- **[Rendering-Aware Bayesian 3D Gaussian Splatting with Native Uncertainty and Adaptive Complexity Control](https://arxiv.org/abs/2607.05522v1)**  
  Authors: Gaoxiang Jia, Vikram Appia, Junzhou Huang, Xinlei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05522v1.pdf)  
  Keywords: gaussian splatting, geometry, sparse view, 3d gaussian, ar  
- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771v1)**  
  Authors: Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03771v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/VOP-GS)  
  Keywords: gaussian splatting, geometry, sparse view, efficient, 3d gaussian, large scene, ar, face  
- **[Sparse-View Surface Reconstruction using Gaussian Splatting through High-Confidence Depth Propagation with Normal Priors](https://arxiv.org/abs/2607.03765v1)**  
  Authors: Liang Han, Bangcai Wei, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03765v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/DP-GS)  
  Keywords: gaussian splatting, sparse-view, high-fidelity, geometry, sparse view, 3d gaussian, ar, 3d reconstruction, face  
- **[Fast 3D Foundation Model Initialized Gaussian Splatting](https://arxiv.org/abs/2607.03209v1)**  
  Authors: Anurag Dalal, Daniel Hagen, Kjell G. Robbersmyr, Kristian Muri Knausgård  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03209v1.pdf)  
  Keywords: gaussian splatting, sparse-view, motion, fast, 3d gaussian, ar, vr, robotics, nerf  
- **[Improving Sparse-View 3DGS Generalization via Flat Minima Optimization](https://arxiv.org/abs/2607.00885v1)**  
  Authors: Kangmin Seo, Sangeek Hyun, MinKyu Lee, Jae-Pil Heo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00885v1.pdf)  
  Keywords: gaussian splatting, sparse-view, dynamic, fast, efficient, 3d gaussian, ar, nerf, real-time rendering, neural rendering, lightweight  
- **[AugSplat: Radiance Field-Informed Gaussian Splatting for Sparse-View Settings](https://arxiv.org/abs/2606.31556v1)**  
  Authors: Lorenzo Lazzaroni, Riccardo Bollati, Daniel Barath, Michael Niemeyer, Keisuke Tateno  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31556v1.pdf)  
  Keywords: gaussian splatting, sparse-view, geometry, ar, nerf, real-time rendering  
- **[StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors](https://arxiv.org/abs/2606.30545v2)**  
  Authors: Wenhao Yuan, Yiyuan Ge, Deli Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30545v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://stringerywh00.github.io/StereoGS_project_page)  
  Keywords: gaussian splatting, sparse-view, dynamic, geometry, 3d gaussian, head, ar, nerf, face  

### Geometry Reconstruction

*Showing the latest 50 out of 211 papers*

- **[CORF-GS: Real-Time Wireless Radiance Field Reconstruction via Coupled Optical-RF Gaussian Splatting](https://arxiv.org/abs/2607.25569v1)**  
  Authors: Jinya Zhang, Jiajia Guo, Chao-Kai Wen, Shi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25569v1.pdf)  
  Keywords: gaussian splatting, geometry, efficient, 3d gaussian, ar, face  
- **[GenSplatCodec: Feed-Forward Gaussian Splatting Compression via One-Step Diffusion](https://arxiv.org/abs/2607.24403v1)**  
  Authors: Qiang Hu, Zhenlong Wu, Lei Huang, Zihan Zheng, Xiaoyun Zhang, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24403v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, geometry, 3d gaussian, ar, compression, compact, lightweight  
- **[Fashion-3DLR: A Controllable 3D Garment Generation Using Pairwise Fashion Elements for Intelligent Design](https://arxiv.org/abs/2607.23189v1)**  
  Authors: Shenghao Yang, Hongtao Zhang, Yuhan Yi, Zhihao Tang, Zihao Cui, Lian Wen, Han Yan, Yuan Gao, Mingbo Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.23189v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d gaussian, ar, semantic  
- **[Visual Relocalization from Sparse Views in Aliased and Low-Texture Environments via Novel View Synthesis](https://arxiv.org/abs/2607.22147v1)**  
  Authors: Maria Peribañez, Javier Civera, Rudolph Triebel, Riccardo Giubilato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22147v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DLR-RM/multimodal-gsplat-relocalization?style=social)](https://github.com/DLR-RM/multimodal-gsplat-relocalization)  
  Keywords: gaussian splatting, illumination, motion, geometry, sparse view, 3d gaussian, ar, localization  
- **[Learning Adaptive Semantic Gaussian Allocation for 3D Occupancy](https://arxiv.org/abs/2607.21896v1)**  
  Authors: Kanglin Ning, Yiran Zhao, Wenrui Li, Houde Quan, Qifan Li, Xingtao Wang, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21896v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, compact, semantic  
- **[Future Rendering $\neq$ Future Surface: A Benchmark and Dataset for Dynamic Surface Reconstruction Beyond the Observed Window](https://arxiv.org/abs/2607.21471v1)**  
  Authors: Yukun Shi, Minglun Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21471v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ricky-S/futuresurf?style=social)](https://github.com/Ricky-S/futuresurf)  
  Keywords: motion, dynamic, geometry, deformation, ar, face  
- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: gaussian splatting, outdoor, geometry, 3d gaussian, ar, mapping, tracking, slam, localization, lightweight  
- **[Construction and Dynamic Update of Channel Gain Maps via 3D Gaussian Splatting](https://arxiv.org/abs/2607.21099v1)**  
  Authors: Yilong Chen, Yuan Guo, Juncong Zhou, Jie Xu, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21099v1.pdf)  
  Keywords: gaussian splatting, dynamic, fast, geometry, efficient, 3d gaussian, ar, compact  
- **[3D-GIMP: When 3D Gaussian Inpainting Meets PatchMatch](https://arxiv.org/abs/2607.20789v1)**  
  Authors: Xuening Tian, Dieter Schmalstieg, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20789v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, 3d gaussian, ar, 3d reconstruction  
- **[RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring](https://arxiv.org/abs/2607.20628v1)**  
  Authors: Renbiao Jin, Mingxin Yang, Yutian Chen, Junhao Zhuang, Xin Cai, Mulin Yu, Linning Xu, Wenxian Yu, Danping Zou, Shi Guo, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20628v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rbjin.github.io/RealVDeblur)  
  Keywords: gaussian splatting, motion, efficient, 3d gaussian, ar, compression, 3d reconstruction, semantic  

### Large Scene

- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: gaussian splatting, outdoor, geometry, 3d gaussian, ar, mapping, tracking, slam, localization, lightweight  
- **[Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering](https://arxiv.org/abs/2607.19893v1)**  
  Authors: Zhenxiang Ma, Zeyu He, Yuanzhen Zhou, Zhenyu Yang, Yuchang Zhang, Miao Tao, Rong Fu, Jidong Zhai, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19893v1.pdf)  
  Keywords: neural rendering, head, large scene, ar  
- **[AniGS: Bridging Rendering and Diffusion Prior for 3D Scene Animation](https://arxiv.org/abs/2607.18539v1)**  
  Authors: Yen-Chi Cheng, Chen Gao, Chuhan Chen, Tuotuo Li, Rajvi Shah, Ayush Saraf, Changil Kim, Liangyan Gui, Alexander Schwing, Johannes Kopf, Hung-Yu Tseng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18539v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, outdoor, 3d gaussian, deformation, ar, animation  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: illumination, dynamic, motion, outdoor, geometry, 3d gaussian, ar, mapping, vr, tracking  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: gaussian splatting, recognition, motion, fast, efficient, 3d gaussian, large scene, ar, slam, real-time rendering  
- **[GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors](https://arxiv.org/abs/2607.11184v1)**  
  Authors: Ruilan Gao, Letian Jin, Yu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11184v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rlgao.github.io/geogs_slam)  
  Keywords: gaussian splatting, outdoor, geometry, 3d gaussian, ar, mapping, tracking, slam  
- **[Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction](https://arxiv.org/abs/2607.08769v1)**  
  Authors: Weijian Chen, Weibo Yao, Yuhang Zhang, Xiaolin Tang, Guo Wang, Weijun Zhang, Xitong Gao, Yihao Chen, Hongde Qin, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08769v1.pdf)  
  Keywords: gaussian splatting, outdoor, geometry, 3d gaussian, ar  
- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771v1)**  
  Authors: Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03771v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/VOP-GS)  
  Keywords: gaussian splatting, geometry, sparse view, efficient, 3d gaussian, large scene, ar, face  
- **[Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673v1)**  
  Authors: Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu, Krishna Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00673v1.pdf)  
  Keywords: human, outdoor, 3d gaussian, deformation, ar  
- **[GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping](https://arxiv.org/abs/2606.30809v1)**  
  Authors: Annika Thomas, Mason Peterson, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30809v1.pdf)  
  Keywords: gaussian splatting, outdoor, geometry, 3d gaussian, ar, mapping  

### Model Compression

*Showing the latest 50 out of 186 papers*

- **[CORF-GS: Real-Time Wireless Radiance Field Reconstruction via Coupled Optical-RF Gaussian Splatting](https://arxiv.org/abs/2607.25569v1)**  
  Authors: Jinya Zhang, Jiajia Guo, Chao-Kai Wen, Shi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25569v1.pdf)  
  Keywords: gaussian splatting, geometry, efficient, 3d gaussian, ar, face  
- **[GenSplatCodec: Feed-Forward Gaussian Splatting Compression via One-Step Diffusion](https://arxiv.org/abs/2607.24403v1)**  
  Authors: Qiang Hu, Zhenlong Wu, Lei Huang, Zihan Zheng, Xiaoyun Zhang, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24403v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, geometry, 3d gaussian, ar, compression, compact, lightweight  
- **[3D Gaussian Splatting for Scientific Particle Data Compression and Rendering](https://arxiv.org/abs/2607.22956v1)**  
  Authors: Bo Jiang, Youyuan Liu, Taolue Yang, Sheng Di, Sian Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22956v1.pdf)  
  Keywords: gaussian splatting, fast, 3d gaussian, ar, compression, compact, lightweight  
- **[Meshless Domain Randomization via Explicit Parameter Perturbation of 3D Gaussian Splatting](https://arxiv.org/abs/2607.22890v1)**  
  Authors: Felipe Nunes Carbone de Carvalho, Joyce de Morais Souza, Alan de Aguiar, Charles Morphy D. Santos, João Paulo Gois  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22890v1.pdf)  
  Keywords: gaussian splatting, illumination, efficient, 3d gaussian, ar  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: gaussian splatting, illumination, lighting, efficient, ar, reflection, ray tracing, face, relighting  
- **[Learning Adaptive Semantic Gaussian Allocation for 3D Occupancy](https://arxiv.org/abs/2607.21896v1)**  
  Authors: Kanglin Ning, Yiran Zhao, Wenrui Li, Houde Quan, Qifan Li, Xingtao Wang, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21896v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, compact, semantic  
- **[GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel View Synthesis](https://arxiv.org/abs/2607.21448v2)**  
  Authors: Jiahao He, Yihua Shao, Zhengkai Zhao, Pan Gao, Fei Ma, Jingcai Guo, Hao Tang, Nicu Sebe, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21448v2.pdf)  
  Keywords: gaussian splatting, motion, dynamic, efficient, 3d gaussian, deformation, ar, compact  
- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: gaussian splatting, outdoor, geometry, 3d gaussian, ar, mapping, tracking, slam, localization, lightweight  
- **[Construction and Dynamic Update of Channel Gain Maps via 3D Gaussian Splatting](https://arxiv.org/abs/2607.21099v1)**  
  Authors: Yilong Chen, Yuan Guo, Juncong Zhou, Jie Xu, Rui Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21099v1.pdf)  
  Keywords: gaussian splatting, dynamic, fast, geometry, efficient, 3d gaussian, ar, compact  
- **[SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization](https://arxiv.org/abs/2607.20813v1)**  
  Authors: Jiun Lee, Jaekwang Kim, Sangmin Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20813v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, efficient, ar, face  

### Quality Enhancement

*Showing the latest 50 out of 122 papers*

- **[PanoLess: Environment Reconstruction from Partial Reflective Views](https://arxiv.org/abs/2607.25362v1)**  
  Authors: Ahitagni Das, Ashok Veeraraghavan, Vivek Boominathan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25362v1.pdf)  
  Keywords: illumination, high-fidelity, ar, reflection, face  
- **[GenSplatCodec: Feed-Forward Gaussian Splatting Compression via One-Step Diffusion](https://arxiv.org/abs/2607.24403v1)**  
  Authors: Qiang Hu, Zhenlong Wu, Lei Huang, Zihan Zheng, Xiaoyun Zhang, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24403v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, geometry, 3d gaussian, ar, compression, compact, lightweight  
- **[SubSplat: High-Resolution Pixel-aligned 3DGS via Sub-pixel Gaussian Reparameterization](https://arxiv.org/abs/2607.20813v1)**  
  Authors: Jiun Lee, Jaekwang Kim, Sangmin Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20813v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, efficient, ar, face  
- **[3D-GIMP: When 3D Gaussian Inpainting Meets PatchMatch](https://arxiv.org/abs/2607.20789v1)**  
  Authors: Xuening Tian, Dieter Schmalstieg, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20789v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, 3d gaussian, ar, 3d reconstruction  
- **[Exploration Matters for Escaping the Blur Trap in 3D Gaussian Splatting](https://arxiv.org/abs/2607.17965v1)**  
  Authors: Chengbo Wang, Guozheng Ma, Jinhong Wu, Tie Ji, Yizhen Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17965v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chengbo-wang.github.io/ExploreGS)  
  Keywords: gaussian splatting, 3d gaussian, high-fidelity, ar  
- **[Packet-Loss Robust 3D Gaussian Compression via Atomic Packaging and GNN-based Error Concealment](https://arxiv.org/abs/2607.17916v1)**  
  Authors: Yuxuan Tao, Xuerui Ma, Hao Zhang, Chunhua Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17916v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, 3d gaussian, ar, compression, nerf, neural rendering, lightweight  
- **[CaT-GS: Efficient 3DGS Rendering for Large Scale Scenes via Inter-frame Caching and Tile Scheduling](https://arxiv.org/abs/2607.17842v1)**  
  Authors: Tingjia Zhang, Bo Chen, Shengzhong Liu, Fan Wu, Guihai Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17842v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, efficient, 3d gaussian, ar, real-time rendering, neural rendering  
- **[FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System](https://arxiv.org/abs/2607.17803v1)**  
  Authors: Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17803v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CPREgroup/FF-ProCams?style=social)](https://github.com/CPREgroup/FF-ProCams)  
  Keywords: gaussian splatting, illumination, high-fidelity, relightable, 3d gaussian, head, ar, mapping, 3d reconstruction, face, lightweight  
- **[FillGauss: Fine-Grained Filling-Aware Impact Sound Generation for 3D Gaussian Splatting](https://arxiv.org/abs/2607.17773v1)**  
  Authors: Chen Yang, Ganye Wen, Bin Huang, Jiayi Lyu, Zehai Niu, Linlin Shen, Jinbao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17773v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, geometry, 3d gaussian, ar, face  
- **[SPARE-GS: Structural Parsimony and Resource Efficiency for 3D Gaussian Splatting](https://arxiv.org/abs/2607.16624v1)**  
  Authors: Zhang Chen, Shuai Wan, Fuzheng Yang, Jiazhi Xia, Weiyao Lin, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16624v1.pdf)  
  Keywords: gaussian splatting, dynamic, high-fidelity, 3d gaussian, ar, compression, compact  

### Ray Tracing

- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: gaussian splatting, illumination, lighting, efficient, ar, reflection, ray tracing, face, relighting  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, human, high-fidelity, geometry, 3d gaussian, ar, reflection, ray tracing, face  
- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: gaussian splatting, human, geometry, ar, ray casting, compact  
- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869v1)**  
  Authors: Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30869v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gray)  
  Keywords: gaussian splatting, fast, 3d gaussian, ar, ray tracing  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: gaussian splatting, fast, geometry, efficient, 3d gaussian, ar, path tracing, reflection, ray tracing, real-time rendering  
- **[RenderFormer++: Scalable and Physically Grounded Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v1)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jinyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v1.pdf)  
  Keywords: illumination, global illumination, ar, light transport, compact, neural rendering  
- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: gaussian splatting, illumination, global illumination, geometry, efficient, 3d gaussian, ar, 3d reconstruction  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: gaussian splatting, illumination, global illumination, high-fidelity, ar  
- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314v1)**  
  Authors: Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11314v1.pdf)  
  Keywords: motion, dynamic, geometry, lighting, 3d gaussian, ar, ray tracing, 3d reconstruction, neural rendering, relighting, light transport, lightweight  
- **[PTIR-GS: Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606v3)**  
  Authors: Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09606v3.pdf)  
  Keywords: illumination, global illumination, lighting, 3d gaussian, ar, path tracing, reflection, ray tracing, light transport, compact, relighting, shadow  

### Relighting

*Showing the latest 50 out of 56 papers*

- **[PanoLess: Environment Reconstruction from Partial Reflective Views](https://arxiv.org/abs/2607.25362v1)**  
  Authors: Ahitagni Das, Ashok Veeraraghavan, Vivek Boominathan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25362v1.pdf)  
  Keywords: illumination, high-fidelity, ar, reflection, face  
- **[Meshless Domain Randomization via Explicit Parameter Perturbation of 3D Gaussian Splatting](https://arxiv.org/abs/2607.22890v1)**  
  Authors: Felipe Nunes Carbone de Carvalho, Joyce de Morais Souza, Alan de Aguiar, Charles Morphy D. Santos, João Paulo Gois  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22890v1.pdf)  
  Keywords: gaussian splatting, illumination, efficient, 3d gaussian, ar  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: gaussian splatting, illumination, lighting, efficient, ar, reflection, ray tracing, face, relighting  
- **[Visual Relocalization from Sparse Views in Aliased and Low-Texture Environments via Novel View Synthesis](https://arxiv.org/abs/2607.22147v1)**  
  Authors: Maria Peribañez, Javier Civera, Rudolph Triebel, Riccardo Giubilato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22147v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DLR-RM/multimodal-gsplat-relocalization?style=social)](https://github.com/DLR-RM/multimodal-gsplat-relocalization)  
  Keywords: gaussian splatting, illumination, motion, geometry, sparse view, 3d gaussian, ar, localization  
- **[ECoNGS: Efficient Compressive Neural Gaussian Splats for Volume Visualization](https://arxiv.org/abs/2607.18466v1)**  
  Authors: Kaiyuan Tang, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18466v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/ECoNGS?style=social)](https://github.com/TouKaienn/ECoNGS)  
  Keywords: gaussian splatting, dynamic, lighting, efficient, ar, vr, compact, lightweight  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: illumination, dynamic, motion, outdoor, geometry, 3d gaussian, ar, mapping, vr, tracking  
- **[FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System](https://arxiv.org/abs/2607.17803v1)**  
  Authors: Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17803v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CPREgroup/FF-ProCams?style=social)](https://github.com/CPREgroup/FF-ProCams)  
  Keywords: gaussian splatting, illumination, high-fidelity, relightable, 3d gaussian, head, ar, mapping, 3d reconstruction, face, lightweight  
- **[GEAR: Reconstruction of Classical Paintings via Geometry Grounding and Appearance Restitution](https://arxiv.org/abs/2607.17519v2)**  
  Authors: Qinyu Zhang, Xinda Liu, Yunchen Li, Yunzhuo Liu, Chenxi Hu, Kang Li, Guohua Geng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17519v2.pdf)  
  Keywords: illumination, human, geometry, lighting, 3d gaussian, ar, 3d reconstruction  
- **[Splat-based 3D Scene Reconstruction with Extreme Motion-blur](https://arxiv.org/abs/2607.16926v1)**  
  Authors: Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16926v1.pdf) | [![GitHub](https://img.shields.io/github/stars/KAIST-VCLAB/gs-extreme-motion-blur?style=social)](https://github.com/KAIST-VCLAB/gs-extreme-motion-blur)  
  Keywords: gaussian splatting, illumination, motion, fast, lighting, geometry, 3d gaussian, ar, mapping, robotics, 3d reconstruction  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, human, high-fidelity, geometry, 3d gaussian, ar, reflection, ray tracing, face  

### SLAM

*Showing the latest 50 out of 76 papers*

- **[Head Avatars with Dynamic Explicit Hair](https://arxiv.org/abs/2607.23861v1)**  
  Authors: Vanessa Sklyarova, Haonan Chen, Berna Kabadayi, Tobias Kirschstein, Zicong Fan, Xi Wang, Gerard Pons-Moll, Matthias Nießner, Marc Pollefeys, Michael J. Black, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.23861v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, human, 3d gaussian, deformation, acceleration, avatar, head, ar, tracking, face  
- **[Visual Relocalization from Sparse Views in Aliased and Low-Texture Environments via Novel View Synthesis](https://arxiv.org/abs/2607.22147v1)**  
  Authors: Maria Peribañez, Javier Civera, Rudolph Triebel, Riccardo Giubilato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22147v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DLR-RM/multimodal-gsplat-relocalization?style=social)](https://github.com/DLR-RM/multimodal-gsplat-relocalization)  
  Keywords: gaussian splatting, illumination, motion, geometry, sparse view, 3d gaussian, ar, localization  
- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: gaussian splatting, outdoor, geometry, 3d gaussian, ar, mapping, tracking, slam, localization, lightweight  
- **[FlexiAvatar: Unified 3D Gaussian Human Avatars Under Arbitrary Body Visibility](https://arxiv.org/abs/2607.19100v1)**  
  Authors: Yihalem Yimolal Tiruneh, Muhammad Salman Ali, Uyoung Jeong, Muneeb A. Khan, MD Khalequzzaman Chowdhury Sayem, Allanur Bayramgeldiyev, Binod Bhattarai, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19100v1.pdf)  
  Keywords: gaussian splatting, body, human, 3d gaussian, head, avatar, ar, vr, tracking, neural rendering  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: illumination, dynamic, motion, outdoor, geometry, 3d gaussian, ar, mapping, vr, tracking  
- **[FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System](https://arxiv.org/abs/2607.17803v1)**  
  Authors: Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17803v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CPREgroup/FF-ProCams?style=social)](https://github.com/CPREgroup/FF-ProCams)  
  Keywords: gaussian splatting, illumination, high-fidelity, relightable, 3d gaussian, head, ar, mapping, 3d reconstruction, face, lightweight  
- **[Splat-based 3D Scene Reconstruction with Extreme Motion-blur](https://arxiv.org/abs/2607.16926v1)**  
  Authors: Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16926v1.pdf) | [![GitHub](https://img.shields.io/github/stars/KAIST-VCLAB/gs-extreme-motion-blur?style=social)](https://github.com/KAIST-VCLAB/gs-extreme-motion-blur)  
  Keywords: gaussian splatting, illumination, motion, fast, lighting, geometry, 3d gaussian, ar, mapping, robotics, 3d reconstruction  
- **[RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping](https://arxiv.org/abs/2607.15048v1)**  
  Authors: Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15048v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, mapping, autonomous driving, compact, face, semantic  
- **[AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight](https://arxiv.org/abs/2607.14997v1)**  
  Authors: Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14997v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, 3d gaussian, ar, tracking, semantic  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: gaussian splatting, recognition, motion, fast, efficient, 3d gaussian, large scene, ar, slam, real-time rendering  

### Scene Understanding

*Showing the latest 50 out of 118 papers*

- **[SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation](https://arxiv.org/abs/2607.25219v1)**  
  Authors: Weiqi Huang, Dianyi Yang, Jiaxin Li, Shuangyi Dong, Hao Xu, Zan Wang, Wei Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25219v1.pdf)  
  Keywords: gaussian splatting, motion, human, body, 3d gaussian, avatar, ar, semantic  
- **[Fashion-3DLR: A Controllable 3D Garment Generation Using Pairwise Fashion Elements for Intelligent Design](https://arxiv.org/abs/2607.23189v1)**  
  Authors: Shenghao Yang, Hongtao Zhang, Yuhan Yi, Zhihao Tang, Zihao Cui, Lian Wen, Han Yan, Yuan Gao, Mingbo Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.23189v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d gaussian, ar, semantic  
- **[Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline](https://arxiv.org/abs/2607.22997v1)**  
  Authors: Qing Yang, Xun Wang, Ziguan Wang, Zhenjiang Li, Hongqiang Wang, Dongdong Weng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22997v1.pdf)  
  Keywords: gaussian splatting, motion, human, body, 3d gaussian, ar, semantic  
- **[Learning Adaptive Semantic Gaussian Allocation for 3D Occupancy](https://arxiv.org/abs/2607.21896v1)**  
  Authors: Kanglin Ning, Yiran Zhao, Wenrui Li, Houde Quan, Qifan Li, Xingtao Wang, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21896v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, compact, semantic  
- **[RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring](https://arxiv.org/abs/2607.20628v1)**  
  Authors: Renbiao Jin, Mingxin Yang, Yutian Chen, Junhao Zhuang, Xin Cai, Mulin Yu, Linning Xu, Wenxian Yu, Danping Zou, Shi Guo, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.20628v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rbjin.github.io/RealVDeblur)  
  Keywords: gaussian splatting, motion, efficient, 3d gaussian, ar, compression, 3d reconstruction, semantic  
- **[ZeroSplat: Generalized Referring Segmentation in 3D Gaussian Splatting](https://arxiv.org/abs/2607.18801v1)**  
  Authors: Jiayu Ding, Meilu Song, Xiaoyi Zhang, Hongbo Jin, Yichen Jin, Xiangtian Si  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18801v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://inkmind-ai.github.io/ZeroSplat)  
  Keywords: gaussian splatting, dynamic, 3d gaussian, segmentation, head, ar, understanding, semantic  
- **[RayOcc: Occlusion-Aware Ray Occupancy Estimation via Gaussian Mixture Intensity](https://arxiv.org/abs/2607.17660v1)**  
  Authors: Junho Kim, Seongwon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17660v1.pdf)  
  Keywords: face, 3d gaussian, semantic, ar  
- **[TopoGS: Planar Reconstruction via Topology-aware 3D Gaussian Splatting](https://arxiv.org/abs/2607.16838v1)**  
  Authors: Shanshan Pan, Jiale Chen, Yilin Liu, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.16838v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d gaussian, segmentation, ar, 3d reconstruction, compact  
- **[RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping](https://arxiv.org/abs/2607.15048v1)**  
  Authors: Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15048v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, mapping, autonomous driving, compact, face, semantic  
- **[AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight](https://arxiv.org/abs/2607.14997v1)**  
  Authors: Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14997v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, 3d gaussian, ar, tracking, semantic  



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