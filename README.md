# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-09-07 01:49:05

## 📰 Latest Updates

🔧 **[2026-08-08] Resilient arXiv Updates**
- Switched the crawler to the official HTTPS export API endpoint
- Added bounded retries for rate limits, server errors, and network timeouts
- Temporary arXiv outages now preserve existing data and finish scheduled runs with a warning
- Added atomic, non-empty JSON writes and fallback to the latest valid data when generating README

📚 **[2026-08-08] Community Paper Added**
- Added the HDR Gaussian Splatting paper suggested in [Issue #3](https://github.com/longxiang-ai/awesome-gaussians/issues/3)

🚀 **[2026-02] Major Feature Update — v2.0**
- **Unified CLI**: Single entry point `python main.py` with subcommands: `init`, `search`, `suggest`, `export-bib`, `readme`
- **Interactive Configuration Wizard**: Run `python main.py init` to set up keywords, domains, time range, and API keys step-by-step
- **Custom Time Range Filtering**: Support relative periods (`6m`, `1y`, `2y`) and absolute date ranges (`2024-01-01` to `2025-06-01`)
- **Smart Link Extraction**: Automatically extracts and classifies GitHub, project page, dataset, video, demo, and HuggingFace links from paper abstracts
- **BibTeX Export**: Fetch BibTeX from arXiv and export to `.bib` files with category/date filters
- **LLM Keyword Suggestion**: Paste a few paper titles or arXiv IDs, and an LLM automatically generates optimized search keywords
- **arXiv Domain Filtering**: Restrict searches to specific arXiv categories (e.g., `cs.CV`, `cs.GR`)

🔧 **[2025-06-26] Configurable Search Keywords Added**
- You can now customize search keywords by modifying `data/search_config.json`

- View detailed updates: [News.md](News.md) 📋

---

## Categories

- [3DGS Surveys](#3dgs-surveys) (4 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (91 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (169 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (207 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (40 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (219 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (20 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (196 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (100 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (12 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (53 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (83 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (109 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: geometry, survey, ar, gaussian splatting, illumination, motion, 3d reconstruction  
- **[UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys](https://arxiv.org/abs/2608.06404v1)**  
  Authors: Junxiong Zhou, Xuechen Li, Chonghao Qiu, Lang Qiao, Xiaowei Jia, Qi Yang, Chishan Zhang, Leikun Yin, Nanshan You, Vipin Kumar, David Mulla, Ce Yang, Zhenong Jin, Licheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06404v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://link-dev.github.io/UAV3DCrop)  
  Keywords: geometry, dynamic, survey, 3d gaussian, ar, gaussian splatting, nerf, 3d reconstruction  
- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: tracking, dynamic, survey, 3d gaussian, mapping, ar, high-fidelity, slam, localization, efficient  
- **[Recent Advances and Trends in Learning-based 3D Representations](https://arxiv.org/abs/2606.04871v1)**  
  Authors: Adrien Schockaert, Hamid Laga, Hazem Wannous, Vincent Magnier, Guillaume Dufaye, Jean-françois Witz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.04871v1.pdf)  
  Keywords: 4d, medical, recognition, survey, autonomous driving, 3d gaussian, ar, compact, vr, gaussian splatting, neural rendering, motion, 3d reconstruction  

### Acceleration

*Showing the latest 50 out of 91 papers*

- **[GradRig: Differentiable Weights for Skinned Gaussian Splat Deformation](https://arxiv.org/abs/2609.05127v1)**  
  Authors: Nina Vesseron, Élie Michel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05127v1.pdf)  
  Keywords: real-time rendering, deformation, dynamic, 3d gaussian, ar  
- **[TileGS: Tile-Local Depth Binning for Gaussian Splatting Rasterization](https://arxiv.org/abs/2609.03613v1)**  
  Authors: Wei Tan, Matias Turkulainen, Lauri Ilola, Hamed Rezazadegan Tavakoli, Juho Kannala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03613v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, fast, gaussian splatting  
- **[Laplacian Frequency Hierarchies for Efficient 3D Gaussian Splatting Training](https://arxiv.org/abs/2609.03334v1)**  
  Authors: Yixiong Yang, Sisheng Zhang, Qingsong Yan, Shaohuai Shi, Qiang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03334v1.pdf)  
  Keywords: acceleration, 3d gaussian, fast, ar, head, gaussian splatting, efficient  
- **[Diffusion-Encoding Gaussian Field for Joint k-q dMRI Reconstruction](https://arxiv.org/abs/2609.02288v1)**  
  Authors: Zhibo Chen, Yajuan Huang, Yu Guan, Qiuyun Fan, Dong Liang, Qiegen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02288v1.pdf)  
  Keywords: 3d gaussian, acceleration, ar  
- **[CC-4DGS: Computational Deformation and Point-Cloud Compression for Storage-Efficient Dynamic Gaussian Splatting](https://arxiv.org/abs/2609.02184v1)**  
  Authors: Kyungdae Park, Chae Eun Rhee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02184v1.pdf)  
  Keywords: real-time rendering, 4d, deformation, dynamic, compression, ar, compact, gaussian splatting, efficient  
- **[Amortized Anchor Refinement for Deployable Continuous-Time 4D Gaussian Reconstruction](https://arxiv.org/abs/2608.30218v1)**  
  Authors: Jingong Chen, Qingwen Zhang, Sanghyeon Jun, Chulwoo Pack, Kyle Gao, Kwanghee Won  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.30218v1.pdf)  
  Keywords: fast, 4d, head, ar  
- **[WilLaGS: Latent-Conditional 3D Appearance Fields for Robust Gaussian Splatting In-the-Wild](https://arxiv.org/abs/2608.28240v1)**  
  Authors: Yuhao Bai, Qianqiu Tan, Lilong Chen, Huanhuan Lv, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.28240v1.pdf)  
  Keywords: real-time rendering, dynamic, 3d gaussian, ar, high-fidelity, gaussian splatting, illumination  
- **[GaussianWAM: Distilling Geometry and Semantics from 3D Gaussian Fields into World-Action Models](https://arxiv.org/abs/2608.24714v1)**  
  Authors: Zijian Zhang, Yuqing Jiang, Weitao Zhou, Minglei Li, Jinhao Zhang, Yao Mu, Xiaofan Li, Hao Zhao, Haibao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24714v1.pdf)  
  Keywords: geometry, dynamic, semantic, 3d gaussian, fast, ar, head  
- **[Fast and Compact 3D Gaussian Splatting with Polarized Opacity Prior](https://arxiv.org/abs/2608.22344v1)**  
  Authors: Zi-Ming Wang, Kai-Wen Duan, Kowei Huang, Akihiro Sugimoto, Shang-Hong Lai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22344v1.pdf)  
  Keywords: 3d gaussian, fast, compact, ar, gaussian splatting, efficient  
- **[Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)**  
  Authors: Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/vorotracing)  
  Keywords: real-time rendering, motion, face, 3d gaussian, fast, compact, ar, gaussian splatting, nerf, ray tracing  

### Applications

*Showing the latest 50 out of 498 papers*

- **[Compact Neural Appearance Models for Efficient Gaussian Splatting](https://arxiv.org/abs/2609.05255v1)**  
  Authors: Florian Hahlbohm, Jorge Condor, Linus Franke, Martin Eisemann, Marcus Magnor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05255v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, compact, gaussian splatting, efficient  
- **[GradRig: Differentiable Weights for Skinned Gaussian Splat Deformation](https://arxiv.org/abs/2609.05127v1)**  
  Authors: Nina Vesseron, Élie Michel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05127v1.pdf)  
  Keywords: real-time rendering, deformation, dynamic, 3d gaussian, ar  
- **[NavArena: Automated Construction of Goal-Oriented Navigation Benchmarks from 3D Gaussian Splatting Reconstructions](https://arxiv.org/abs/2609.04602v1)**  
  Authors: Junhui Wang, Wei Yang, Xinyao Li, Ningjing Fan, Yuehao Yin, Xuecheng Chen, Chao Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04602v1.pdf)  
  Keywords: 3d gaussian, ar, semantic, gaussian splatting  
- **[Where Appearance Fails, Geometry Recognizes: A CAD-Free 3D Shape Prior That Complements Vision Foundation Models](https://arxiv.org/abs/2609.04381v1)**  
  Authors: Chenxi Tao, Seung-Kyum Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04381v1.pdf)  
  Keywords: geometry, recognition, 3d gaussian, ar, gaussian splatting, lighting, robotics  
- **[Sparse auto-regressive modeling for scene generation from multi-view images](https://arxiv.org/abs/2609.03931v1)**  
  Authors: Thomas Lucas, Maxime Pietrantoni, Philippe Weinzaepfel, Wonjune Cho, Bardienus Pieter Duisterhof, Vincent Leroy, Jerome Revaud  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03931v1.pdf)  
  Keywords: 3d gaussian, ar, compact, gaussian splatting, lighting, efficient  
- **[Reparametrizing 3D Gaussian Splatting for Real-Time Palette-based Color and Luminance Editing](https://arxiv.org/abs/2609.03897v1)**  
  Authors: Cheng-Kang Ted Chao, Yotam Gingold  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03897v1.pdf)  
  Keywords: 3d gaussian, ar, efficient, gaussian splatting  
- **[Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations](https://arxiv.org/abs/2609.03657v1)**  
  Authors: Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03657v1.pdf)  
  Keywords: lightweight, sparse-view, 3d gaussian, ar, gaussian splatting, nerf, robotics  
- **[TileGS: Tile-Local Depth Binning for Gaussian Splatting Rasterization](https://arxiv.org/abs/2609.03613v1)**  
  Authors: Wei Tan, Matias Turkulainen, Lauri Ilola, Hamed Rezazadegan Tavakoli, Juho Kannala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03613v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, fast, gaussian splatting  
- **[TruncGradGS: Improved 3D Gaussian Splatting via Truncated Gradient Updates](https://arxiv.org/abs/2609.03534v1)**  
  Authors: Theo Morales, Nhat-Quynh Le-Pham, Robin Atkins, Binh-Son Hua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03534v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, ar  
- **[STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction](https://arxiv.org/abs/2609.03447v1)**  
  Authors: Bocheng Li, Wenjuan Zhang, Jie Pan. Dongxu Han, Xuesong Ma, Yiling Yao, Yaning Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03447v1.pdf)  
  Keywords: geometry, face, 3d gaussian, mapping, ar, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 169 papers*

- **[STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction](https://arxiv.org/abs/2609.03447v1)**  
  Authors: Bocheng Li, Wenjuan Zhang, Jie Pan. Dongxu Han, Xuesong Ma, Yiling Yao, Yaning Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03447v1.pdf)  
  Keywords: geometry, face, 3d gaussian, mapping, ar, gaussian splatting  
- **[Laplacian Frequency Hierarchies for Efficient 3D Gaussian Splatting Training](https://arxiv.org/abs/2609.03334v1)**  
  Authors: Yixiong Yang, Sisheng Zhang, Qingsong Yan, Shaohuai Shi, Qiang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03334v1.pdf)  
  Keywords: acceleration, 3d gaussian, fast, ar, head, gaussian splatting, efficient  
- **[Atlas: Algorithm-Hardware Co-Design for On-Device City-Scale 3D Gaussian Splatting in VR](https://arxiv.org/abs/2609.02352v1)**  
  Authors: He Zhu, Zheng Liu, Xingyang Li, Anbang Wu, Zihan Liu, Ruyang Li, Hui Wei, Yaqian Zhao, Jingwen Leng, Minyi Guo, Yu Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02352v1.pdf)  
  Keywords: dynamic, 3d gaussian, ar, vr, head, gaussian splatting  
- **[MeshSplatBench: A Unified Benchmark for Triangle-Based Neural Rendering](https://arxiv.org/abs/2609.01306v1)**  
  Authors: Kaixuan Zhang, Minxian Li, Mingwu Ren, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.01306v1.pdf)  
  Keywords: neural rendering, ar, semantic, face  
- **[Inverse Rendering for Modeling with Line Primitives](https://arxiv.org/abs/2609.00625v1)**  
  Authors: Kenji Tojo, Ariel Shamir, Nobuyuki Umetani, Bernd Bickel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00625v1.pdf)  
  Keywords: geometry, reflection, face, 3d gaussian, ar, efficient  
- **[DSG: Dynamic 3D Scene Graph Construction for Embodied Agents in Changing Indoor Environments](https://arxiv.org/abs/2609.00619v1)**  
  Authors: Ming Liao, Chao Ye, Jianing Fei, Weiyang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00619v1.pdf)  
  Keywords: dynamic, semantic, 3d gaussian, ar, human  
- **[BRF-GS: Hyperspectral Bidirectional Reflectance Factor Modeling and Image Generation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2608.31159v1)**  
  Authors: Yiling Yao, Wenjuan Zhang, Bowen Wang, Bocheng Li, Wentao Song, Bing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.31159v1.pdf)  
  Keywords: geometry, face, 3d gaussian, ar, gaussian splatting, efficient  
- **[VCAR: Training-Free 3DGS Segmentation via View Completeness and Axis-Aware Boundary Refinement](https://arxiv.org/abs/2608.30870v1)**  
  Authors: Kun Cao, Di Wang, Haibin Zhu, Haozhi Huang, Xu Wang, Zheng Shi, Guanghua Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.30870v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DDKK0526/VCAR?style=social)](https://github.com/DDKK0526/VCAR)  
  Keywords: semantic, segmentation, compression, 3d gaussian, ar, head, gaussian splatting, understanding  
- **[Amortized Anchor Refinement for Deployable Continuous-Time 4D Gaussian Reconstruction](https://arxiv.org/abs/2608.30218v1)**  
  Authors: Jingong Chen, Qingwen Zhang, Sanghyeon Jun, Chulwoo Pack, Kyle Gao, Kwanghee Won  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.30218v1.pdf)  
  Keywords: fast, 4d, head, ar  
- **[When 3D Gaussian Splatting Recovers Real Surfaces](https://arxiv.org/abs/2608.30054v1)**  
  Authors: Songhe Wang, David Johnathan Miller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.30054v1.pdf)  
  Keywords: geometry, face, 3d gaussian, ar, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 207 papers*

- **[GradRig: Differentiable Weights for Skinned Gaussian Splat Deformation](https://arxiv.org/abs/2609.05127v1)**  
  Authors: Nina Vesseron, Élie Michel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05127v1.pdf)  
  Keywords: real-time rendering, deformation, dynamic, 3d gaussian, ar  
- **[TruncGradGS: Improved 3D Gaussian Splatting via Truncated Gradient Updates](https://arxiv.org/abs/2609.03534v1)**  
  Authors: Theo Morales, Nhat-Quynh Le-Pham, Robin Atkins, Binh-Son Hua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03534v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, ar  
- **[PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations](https://arxiv.org/abs/2609.03341v1)**  
  Authors: Yanshu Zhang, George Shramko, Pratul P. Srinivasan, Ke Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03341v1.pdf)  
  Keywords: deformation, geometry, 3d gaussian, mapping, ar, gaussian splatting  
- **[Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations](https://arxiv.org/abs/2609.02664v1)**  
  Authors: Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02664v1.pdf)  
  Keywords: 4d, dynamic, semantic, segmentation, ar, nerf, localization, understanding  
- **[Atlas: Algorithm-Hardware Co-Design for On-Device City-Scale 3D Gaussian Splatting in VR](https://arxiv.org/abs/2609.02352v1)**  
  Authors: He Zhu, Zheng Liu, Xingyang Li, Anbang Wu, Zihan Liu, Ruyang Li, Hui Wei, Yaqian Zhao, Jingwen Leng, Minyi Guo, Yu Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02352v1.pdf)  
  Keywords: dynamic, 3d gaussian, ar, vr, head, gaussian splatting  
- **[CC-4DGS: Computational Deformation and Point-Cloud Compression for Storage-Efficient Dynamic Gaussian Splatting](https://arxiv.org/abs/2609.02184v1)**  
  Authors: Kyungdae Park, Chae Eun Rhee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02184v1.pdf)  
  Keywords: real-time rendering, 4d, deformation, dynamic, compression, ar, compact, gaussian splatting, efficient  
- **[VirSqueezer: Generating Realistic Deformations and Squeezing Dynamics in VR from Fine-Grained Squeezing Controls](https://arxiv.org/abs/2609.01698v1)**  
  Authors: Qian Zhang, Xiaoming Chen, Xiaorui Ma, Haisheng Li, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.01698v1.pdf)  
  Keywords: deformation, dynamic, 3d gaussian, ar, vr, gaussian splatting  
- **[EvoGS: Modeling Deformation Evolution for Dynamic Gaussian Splatting](https://arxiv.org/abs/2609.00994v1)**  
  Authors: Wei Dong, Shahram Shirani, Jun Chen, Han Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00994v1.pdf)  
  Keywords: deformation, dynamic, 3d gaussian, ar, gaussian splatting, motion  
- **[DSG: Dynamic 3D Scene Graph Construction for Embodied Agents in Changing Indoor Environments](https://arxiv.org/abs/2609.00619v1)**  
  Authors: Ming Liao, Chao Ye, Jianing Fei, Weiyang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00619v1.pdf)  
  Keywords: dynamic, semantic, 3d gaussian, ar, human  
- **[SMG: Semantic Motion Graph for Monocular Dynamic Gaussian Splatting](https://arxiv.org/abs/2608.31023v1)**  
  Authors: Haozheng Yu, Xinyu Yang, Rundong Luo, Jennifer J. Sun, Bharath Hariharan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.31023v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://smg-gaussian.github.io)  
  Keywords: dynamic, semantic, ar, gaussian splatting, motion  

### Few-shot

- **[Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations](https://arxiv.org/abs/2609.03657v1)**  
  Authors: Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03657v1.pdf)  
  Keywords: lightweight, sparse-view, 3d gaussian, ar, gaussian splatting, nerf, robotics  
- **[RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation](https://arxiv.org/abs/2609.02847v2)**  
  Authors: Xiaolei Lang, Ze Kang, Zehao Huang, Naiyan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02847v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jerry-locker.github.io/roge)  
  Keywords: 3d gaussian, sparse view, ar  
- **[GSPotential: Camera Potential Field for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2608.29346v1)**  
  Authors: Zeyuan An, Yanghang Xiao, Zhiying Leng, Yijun Feng, Xiaohui Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.29346v1.pdf)  
  Keywords: 3d gaussian, ar, sparse-view, gaussian splatting  
- **[PAGS: Autofocusing Photoacoustic Tomography via Speed-of-Sound-Adaptive Gaussian Splatting](https://arxiv.org/abs/2608.25472v1)**  
  Authors: Jiarui Ge, Jintao Ma, Bangxu Fan, Jinyan Zhang, Xiaokang Yang, Shuai Na, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25472v1.pdf)  
  Keywords: sparse-view, ar, compact, gaussian splatting, efficient  
- **[Seeing the Unseen: Semantic-in-Gaussian for Sparse-View 3D Generalization](https://arxiv.org/abs/2608.22740v1)**  
  Authors: Zeyang Bai, Yunpeng Wang, Yunbiao Wang, Jun Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22740v1.pdf)  
  Keywords: sparse-view, semantic, face, 3d gaussian, ar, compact, gaussian splatting, efficient  
- **[GaussVid: Sparse-View Gaussian Splatting with 3D-Aware Video Diffusion Priors](https://arxiv.org/abs/2608.21849v1)**  
  Authors: Xinhui Liu, Can Wang, Wei Jiang, Wei Wang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21849v1.pdf)  
  Keywords: sparse-view, geometry, 3d gaussian, ar, gaussian splatting, sparse view  
- **[Sparse Light Field Sampling Improves Casual 3D and 4D Reconstruction](https://arxiv.org/abs/2608.20602v1)**  
  Authors: Shamus Li, Ruiming Cao, Laura Waller, Kristina Monakhova, Sara Fridovich-Keil  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20602v1.pdf)  
  Keywords: 4d, geometry, dynamic, sparse-view, ar, few-shot, motion  
- **[Point-Based 3D Reconstruction from Sparse Views under Known Illumination](https://arxiv.org/abs/2608.20000v1)**  
  Authors: Magnus Kaufmann Gjerde, Joakim Bruslund Haurum, Jeppe Revall Frisvad, Markus Worchel, J. Andreas Bærentzen, Thomas B. Moeslund  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20000v1.pdf)  
  Keywords: geometry, face, ar, compact, light transport, gaussian splatting, illumination, sparse view, 3d reconstruction  
- **[TR-GS: High-Fidelity Sparse-View CT Volumetric Rendering via t-Distribution Gaussian Splatting and Ray-Confidence Modeling](https://arxiv.org/abs/2608.16042v1)**  
  Authors: Zedong Xiao, Yiren Wang, Zhou Liu, Xiaolin Liu, Zhangji Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16042v1.pdf)  
  Keywords: medical, sparse-view, 3d gaussian, ar, high-fidelity, gaussian splatting, sparse view, efficient  
- **[Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting](https://arxiv.org/abs/2608.10756v1)**  
  Authors: Huosen Ou, Dongni Song, Yuncong Wang, Tao Zhou, Yiding Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10756v1.pdf)  
  Keywords: semantic, face, 3d gaussian, ar, few-shot, gaussian splatting, localization  

### Geometry Reconstruction

*Showing the latest 50 out of 219 papers*

- **[Compact Neural Appearance Models for Efficient Gaussian Splatting](https://arxiv.org/abs/2609.05255v1)**  
  Authors: Florian Hahlbohm, Jorge Condor, Linus Franke, Martin Eisemann, Marcus Magnor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05255v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, compact, gaussian splatting, efficient  
- **[Where Appearance Fails, Geometry Recognizes: A CAD-Free 3D Shape Prior That Complements Vision Foundation Models](https://arxiv.org/abs/2609.04381v1)**  
  Authors: Chenxi Tao, Seung-Kyum Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04381v1.pdf)  
  Keywords: geometry, recognition, 3d gaussian, ar, gaussian splatting, lighting, robotics  
- **[TileGS: Tile-Local Depth Binning for Gaussian Splatting Rasterization](https://arxiv.org/abs/2609.03613v1)**  
  Authors: Wei Tan, Matias Turkulainen, Lauri Ilola, Hamed Rezazadegan Tavakoli, Juho Kannala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03613v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, fast, gaussian splatting  
- **[STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction](https://arxiv.org/abs/2609.03447v1)**  
  Authors: Bocheng Li, Wenjuan Zhang, Jie Pan. Dongxu Han, Xuesong Ma, Yiling Yao, Yaning Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03447v1.pdf)  
  Keywords: geometry, face, 3d gaussian, mapping, ar, gaussian splatting  
- **[PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations](https://arxiv.org/abs/2609.03341v1)**  
  Authors: Yanshu Zhang, George Shramko, Pratul P. Srinivasan, Ke Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03341v1.pdf)  
  Keywords: deformation, geometry, 3d gaussian, mapping, ar, gaussian splatting  
- **[AnyGS2Mesh: Feed-Forward Mesh Reconstruction from 3D Gaussian Splatting with Arbitrary-Resolution Views](https://arxiv.org/abs/2609.03304v1)**  
  Authors: Yuxuan Song, Fan Gao, Yibo Zhao, Jiarui Wen, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03304v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, gaussian splatting, efficient  
- **[DualDiff3D: Dual Structure-Appearance Diffusion Priors for Reliability-Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2609.01516v1)**  
  Authors: Qian Wang, Yu Wang, Weiqi Li, Xinhua Cheng, Xiandong Meng, Ronggang Wang, Jian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.01516v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Akaneqwq/DualDiff3D?style=social)](https://github.com/Akaneqwq/DualDiff3D)  
  Keywords: 3d gaussian, ar, gaussian splatting, 3d reconstruction  
- **[Inverse Rendering for Modeling with Line Primitives](https://arxiv.org/abs/2609.00625v1)**  
  Authors: Kenji Tojo, Ariel Shamir, Nobuyuki Umetani, Bernd Bickel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00625v1.pdf)  
  Keywords: geometry, reflection, face, 3d gaussian, ar, efficient  
- **[BRF-GS: Hyperspectral Bidirectional Reflectance Factor Modeling and Image Generation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2608.31159v1)**  
  Authors: Yiling Yao, Wenjuan Zhang, Bowen Wang, Bocheng Li, Wentao Song, Bing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.31159v1.pdf)  
  Keywords: geometry, face, 3d gaussian, ar, gaussian splatting, efficient  
- **[When 3D Gaussian Splatting Recovers Real Surfaces](https://arxiv.org/abs/2608.30054v1)**  
  Authors: Songhe Wang, David Johnathan Miller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.30054v1.pdf)  
  Keywords: geometry, face, 3d gaussian, ar, gaussian splatting  

### Large Scene

- **[M$^3$ISR: A Multi-Modal Multi-View Benchmark for 3D/4D Gaussian Splatting and Feedforward Compression](https://arxiv.org/abs/2608.22465v1)**  
  Authors: Xinhui Liu, Lei Liu, Zhenghao Chen, Lebin Zhou, Wei Wang, Wei Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22465v1.pdf)  
  Keywords: 4d, geometry, dynamic, semantic, segmentation, compression, outdoor, ar, high-fidelity, gaussian splatting, motion  
- **[CoMVS-GS: Collaborative Multi-View Stereo and 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2608.18413v1)**  
  Authors: Shihan Chen, Junjing Zhang, Qingsong Yan, Haibing Liu, Haofan Ren, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.18413v1.pdf)  
  Keywords: geometry, face, 3d gaussian, outdoor, compact, ar, gaussian splatting, motion, efficient  
- **[GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting](https://arxiv.org/abs/2608.10938v2)**  
  Authors: Huaiyuan Weng, Chul Min Yeum, Su-Min Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10938v2.pdf)  
  Keywords: geometry, 3d gaussian, fast, outdoor, ar, gaussian splatting, localization  
- **[OutLangSplat: 3D Language Gaussian Splatting for UAV Outdoor Scenes](https://arxiv.org/abs/2608.04560v1)**  
  Authors: Xia Yan, He Wu, Yanghui Xu, Zizhao Wu, Jiazhou Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04560v1.pdf)  
  Keywords: semantic, segmentation, 3d gaussian, outdoor, ar, gaussian splatting, localization, efficient, understanding  
- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: tracking, lightweight, geometry, 3d gaussian, outdoor, mapping, ar, gaussian splatting, slam, localization  
- **[Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering](https://arxiv.org/abs/2607.19893v1)**  
  Authors: Zhenxiang Ma, Zeyu He, Yuanzhen Zhou, Zhenyu Yang, Yuchang Zhang, Miao Tao, Rong Fu, Jidong Zhai, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19893v1.pdf)  
  Keywords: neural rendering, ar, large scene, head  
- **[AniGS: Bridging Rendering and Diffusion Prior for 3D Scene Animation](https://arxiv.org/abs/2607.18539v1)**  
  Authors: Yen-Chi Cheng, Chen Gao, Chuhan Chen, Tuotuo Li, Rajvi Shah, Ayush Saraf, Changil Kim, Liangyan Gui, Alexander Schwing, Johannes Kopf, Hung-Yu Tseng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18539v1.pdf)  
  Keywords: deformation, dynamic, 3d gaussian, outdoor, ar, gaussian splatting, motion, animation  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: tracking, geometry, dynamic, 3d gaussian, outdoor, mapping, ar, vr, illumination, motion  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: real-time rendering, large scene, recognition, 3d gaussian, fast, ar, gaussian splatting, slam, motion, efficient  
- **[GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors](https://arxiv.org/abs/2607.11184v1)**  
  Authors: Ruilan Gao, Letian Jin, Yu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11184v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rlgao.github.io/geogs_slam)  
  Keywords: tracking, geometry, 3d gaussian, outdoor, mapping, ar, gaussian splatting, slam  

### Model Compression

*Showing the latest 50 out of 196 papers*

- **[Compact Neural Appearance Models for Efficient Gaussian Splatting](https://arxiv.org/abs/2609.05255v1)**  
  Authors: Florian Hahlbohm, Jorge Condor, Linus Franke, Martin Eisemann, Marcus Magnor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05255v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, compact, gaussian splatting, efficient  
- **[Sparse auto-regressive modeling for scene generation from multi-view images](https://arxiv.org/abs/2609.03931v1)**  
  Authors: Thomas Lucas, Maxime Pietrantoni, Philippe Weinzaepfel, Wonjune Cho, Bardienus Pieter Duisterhof, Vincent Leroy, Jerome Revaud  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03931v1.pdf)  
  Keywords: 3d gaussian, ar, compact, gaussian splatting, lighting, efficient  
- **[Reparametrizing 3D Gaussian Splatting for Real-Time Palette-based Color and Luminance Editing](https://arxiv.org/abs/2609.03897v1)**  
  Authors: Cheng-Kang Ted Chao, Yotam Gingold  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03897v1.pdf)  
  Keywords: 3d gaussian, ar, efficient, gaussian splatting  
- **[Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations](https://arxiv.org/abs/2609.03657v1)**  
  Authors: Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03657v1.pdf)  
  Keywords: lightweight, sparse-view, 3d gaussian, ar, gaussian splatting, nerf, robotics  
- **[Laplacian Frequency Hierarchies for Efficient 3D Gaussian Splatting Training](https://arxiv.org/abs/2609.03334v1)**  
  Authors: Yixiong Yang, Sisheng Zhang, Qingsong Yan, Shaohuai Shi, Qiang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03334v1.pdf)  
  Keywords: acceleration, 3d gaussian, fast, ar, head, gaussian splatting, efficient  
- **[AnyGS2Mesh: Feed-Forward Mesh Reconstruction from 3D Gaussian Splatting with Arbitrary-Resolution Views](https://arxiv.org/abs/2609.03304v1)**  
  Authors: Yuxuan Song, Fan Gao, Yibo Zhao, Jiarui Wen, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03304v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, gaussian splatting, efficient  
- **[LightBridge: Feed-Forward Generative Relighting for 3D Gaussian Splatting](https://arxiv.org/abs/2609.02543v1)**  
  Authors: Hezhi Cao, Panhao Cheng, huangsheng du, Qibiao Li, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02543v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, illumination, lighting, relighting, efficient  
- **[CC-4DGS: Computational Deformation and Point-Cloud Compression for Storage-Efficient Dynamic Gaussian Splatting](https://arxiv.org/abs/2609.02184v1)**  
  Authors: Kyungdae Park, Chae Eun Rhee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02184v1.pdf)  
  Keywords: real-time rendering, 4d, deformation, dynamic, compression, ar, compact, gaussian splatting, efficient  
- **[Inverse Rendering for Modeling with Line Primitives](https://arxiv.org/abs/2609.00625v1)**  
  Authors: Kenji Tojo, Ariel Shamir, Nobuyuki Umetani, Bernd Bickel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00625v1.pdf)  
  Keywords: geometry, reflection, face, 3d gaussian, ar, efficient  
- **[BRF-GS: Hyperspectral Bidirectional Reflectance Factor Modeling and Image Generation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2608.31159v1)**  
  Authors: Yiling Yao, Wenjuan Zhang, Bowen Wang, Bocheng Li, Wentao Song, Bing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.31159v1.pdf)  
  Keywords: geometry, face, 3d gaussian, ar, gaussian splatting, efficient  

### Quality Enhancement

*Showing the latest 50 out of 100 papers*

- **[InceptionGS: Generative Bootstrapping for Large-Scale Gaussian Splatting under Unstructured View Sampling](https://arxiv.org/abs/2609.02747v1)**  
  Authors: Tianheng Lu, Guangyu Wang, Ruqi Huang, Lu Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02747v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting  
- **[As-Rigid-As-Possible Deformation of Gaussian Radiance Fields](https://arxiv.org/abs/2608.29538v1)**  
  Authors: Xinhao Tong, Tianjia Shao, Yanlin Weng, Yin Yang, Kun Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.29538v1.pdf)  
  Keywords: deformation, high quality, 3d gaussian, ar, gaussian splatting  
- **[ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos](https://arxiv.org/abs/2608.28570v1)**  
  Authors: Seungyeon Kim, Noémie Jaquier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.28570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chainsplat.github.io)  
  Keywords: geometry, dynamic, ar, compact, high-fidelity, gaussian splatting, lighting  
- **[WilLaGS: Latent-Conditional 3D Appearance Fields for Robust Gaussian Splatting In-the-Wild](https://arxiv.org/abs/2608.28240v1)**  
  Authors: Yuhao Bai, Qianqiu Tan, Lilong Chen, Huanhuan Lv, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.28240v1.pdf)  
  Keywords: real-time rendering, dynamic, 3d gaussian, ar, high-fidelity, gaussian splatting, illumination  
- **[Comparative Evaluation of 3D Reconstruction Methods for Immersive Visualization of Laboratory Objects](https://arxiv.org/abs/2608.27301v1)**  
  Authors: Brian De La Cruz, Aaron Y. Zhao, Maitrey Gramopadhye, Sawyer J. Lazar, Xianming Tan, Daniel Szafir, David S. Lawrence  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.27301v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, nerf, 3d reconstruction  
- **[SACHA: Semantic-Aware Compression for 3D Gaussian Head Avatars](https://arxiv.org/abs/2608.23133v1)**  
  Authors: Zihan Zhang, Shanzhi Yin, Xinju Wu, Bolin Chen, Ru-Ling Liao, Jie Chen, Shiqi Wang, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23133v1.pdf)  
  Keywords: dynamic, semantic, compression, 3d gaussian, ar, compact, high-fidelity, head, avatar, motion, efficient  
- **[AquaFlow: A Monocular Gaussian Splatting SLAM for Underwater Streaming Reconstruction](https://arxiv.org/abs/2608.22906v1)**  
  Authors: Yingxiang Xu, Kerui Ren, Wenqi Guo, Changjian Jiang, Tao Lu, Linning Xu, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22906v1.pdf)  
  Keywords: tracking, geometry, 3d gaussian, mapping, ar, high-fidelity, gaussian splatting, slam, localization, efficient  
- **[NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction](https://arxiv.org/abs/2608.22888v2)**  
  Authors: Xiaopeng Guo, Wai Chung Tse, Yipeng Zhu, Hanwen Zhang, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22888v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nemosplat.hkustvgd.com)  
  Keywords: 4d, tracking, dynamic, semantic, 3d gaussian, ar, high-fidelity, gaussian splatting, motion  
- **[M$^3$ISR: A Multi-Modal Multi-View Benchmark for 3D/4D Gaussian Splatting and Feedforward Compression](https://arxiv.org/abs/2608.22465v1)**  
  Authors: Xinhui Liu, Lei Liu, Zhenghao Chen, Lebin Zhou, Wei Wang, Wei Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22465v1.pdf)  
  Keywords: 4d, geometry, dynamic, semantic, segmentation, compression, outdoor, ar, high-fidelity, gaussian splatting, motion  
- **[In-Situ Reconstruction of the International Space Station Using 3D Gaussian Splatting and Astrobee](https://arxiv.org/abs/2608.21685v1)**  
  Authors: Hudson Kim, Ryan Soussan, Brian Coltin, Jordan Kam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21685v1.pdf)  
  Keywords: 3d gaussian, mapping, ar, high-fidelity, gaussian splatting, human, nerf, 3d reconstruction  

### Ray Tracing

- **[Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)**  
  Authors: Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/vorotracing)  
  Keywords: real-time rendering, motion, face, 3d gaussian, fast, compact, ar, gaussian splatting, nerf, ray tracing  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: reflection, shadow, 3d gaussian, fast, compact, mapping, ar, gaussian splatting, nerf, ray tracing, efficient  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: reflection, face, ar, gaussian splatting, illumination, lighting, ray tracing, relighting, efficient  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: motion, geometry, dynamic, reflection, face, 3d gaussian, ar, high-fidelity, gaussian splatting, human, ray tracing  
- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: geometry, ar, compact, human, gaussian splatting, ray casting  
- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869v1)**  
  Authors: Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30869v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gray)  
  Keywords: 3d gaussian, fast, ar, gaussian splatting, ray tracing  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: real-time rendering, geometry, reflection, 3d gaussian, fast, path tracing, ar, gaussian splatting, ray tracing, efficient  
- **[RenderFormer++: Scalable and Physics-Informed Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v2)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v2.pdf)  
  Keywords: ar, compact, light transport, illumination, neural rendering, global illumination  
- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: geometry, 3d gaussian, ar, gaussian splatting, illumination, global illumination, efficient, 3d reconstruction  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, illumination, global illumination  

### Relighting

*Showing the latest 50 out of 53 papers*

- **[Where Appearance Fails, Geometry Recognizes: A CAD-Free 3D Shape Prior That Complements Vision Foundation Models](https://arxiv.org/abs/2609.04381v1)**  
  Authors: Chenxi Tao, Seung-Kyum Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04381v1.pdf)  
  Keywords: geometry, recognition, 3d gaussian, ar, gaussian splatting, lighting, robotics  
- **[Sparse auto-regressive modeling for scene generation from multi-view images](https://arxiv.org/abs/2609.03931v1)**  
  Authors: Thomas Lucas, Maxime Pietrantoni, Philippe Weinzaepfel, Wonjune Cho, Bardienus Pieter Duisterhof, Vincent Leroy, Jerome Revaud  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03931v1.pdf)  
  Keywords: 3d gaussian, ar, compact, gaussian splatting, lighting, efficient  
- **[LightBridge: Feed-Forward Generative Relighting for 3D Gaussian Splatting](https://arxiv.org/abs/2609.02543v1)**  
  Authors: Hezhi Cao, Panhao Cheng, huangsheng du, Qibiao Li, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02543v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, illumination, lighting, relighting, efficient  
- **[Inverse Rendering for Modeling with Line Primitives](https://arxiv.org/abs/2609.00625v1)**  
  Authors: Kenji Tojo, Ariel Shamir, Nobuyuki Umetani, Bernd Bickel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00625v1.pdf)  
  Keywords: geometry, reflection, face, 3d gaussian, ar, efficient  
- **[ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos](https://arxiv.org/abs/2608.28570v1)**  
  Authors: Seungyeon Kim, Noémie Jaquier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.28570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chainsplat.github.io)  
  Keywords: geometry, dynamic, ar, compact, high-fidelity, gaussian splatting, lighting  
- **[WilLaGS: Latent-Conditional 3D Appearance Fields for Robust Gaussian Splatting In-the-Wild](https://arxiv.org/abs/2608.28240v1)**  
  Authors: Yuhao Bai, Qianqiu Tan, Lilong Chen, Huanhuan Lv, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.28240v1.pdf)  
  Keywords: real-time rendering, dynamic, 3d gaussian, ar, high-fidelity, gaussian splatting, illumination  
- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: geometry, survey, ar, gaussian splatting, illumination, motion, 3d reconstruction  
- **[Point-Based 3D Reconstruction from Sparse Views under Known Illumination](https://arxiv.org/abs/2608.20000v1)**  
  Authors: Magnus Kaufmann Gjerde, Joakim Bruslund Haurum, Jeppe Revall Frisvad, Markus Worchel, J. Andreas Bærentzen, Thomas B. Moeslund  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20000v1.pdf)  
  Keywords: geometry, face, ar, compact, light transport, gaussian splatting, illumination, sparse view, 3d reconstruction  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: reflection, shadow, 3d gaussian, fast, compact, mapping, ar, gaussian splatting, nerf, ray tracing, efficient  
- **[Geometry-Aware Online Mapping for 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2608.14902v1)**  
  Authors: Thai Luu, Quan Tran, Hieu Phan, Tuan Dang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.14902v1.pdf)  
  Keywords: tracking, geometry, 3d gaussian, mapping, localization, ar, head, gaussian splatting, slam, lighting, efficient  

### SLAM

*Showing the latest 50 out of 83 papers*

- **[STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction](https://arxiv.org/abs/2609.03447v1)**  
  Authors: Bocheng Li, Wenjuan Zhang, Jie Pan. Dongxu Han, Xuesong Ma, Yiling Yao, Yaning Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03447v1.pdf)  
  Keywords: geometry, face, 3d gaussian, mapping, ar, gaussian splatting  
- **[PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations](https://arxiv.org/abs/2609.03341v1)**  
  Authors: Yanshu Zhang, George Shramko, Pratul P. Srinivasan, Ke Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03341v1.pdf)  
  Keywords: deformation, geometry, 3d gaussian, mapping, ar, gaussian splatting  
- **[Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations](https://arxiv.org/abs/2609.02664v1)**  
  Authors: Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02664v1.pdf)  
  Keywords: 4d, dynamic, semantic, segmentation, ar, nerf, localization, understanding  
- **[ATGS: Anchored Temporal Gaussian Splatting for Long Volumetric Video Representation](https://arxiv.org/abs/2608.30184v1)**  
  Authors: Jiahao Wu, Jie Liang, Die Hu, Jiayu Yang, Kaiqiang Xiong, Xiang Li, Xiaoyun Zheng, Chao Wang, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.30184v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WuJH2001/ATGS?style=social)](https://github.com/WuJH2001/ATGS)  
  Keywords: tracking, dynamic, ar, compact, gaussian splatting, motion  
- **[Ground-to-Satellite Localization in Unconstrained Image Collections for 3D Scene Reconstruction](https://arxiv.org/abs/2608.29211v1)**  
  Authors: Angel Daruna, Ben Southall, Niluthpol Chowdhury Mithun, Kshitij Minhas, Nicholas Meegan, Qiao Wang, Bogdan Matei, Supun Samarasekera, Rakesh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.29211v1.pdf)  
  Keywords: ar, localization, motion  
- **[SGRNet: Spatially Guided Radiology Network for Structured Radiological Reporting of Head and Neck Cancer](https://arxiv.org/abs/2608.29153v1)**  
  Authors: Ayush Gupta, Vinkle Srivastav, Prateek Upadhya, Amit Gupta, Krithika Rangarajan, Nicolas Padoy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.29153v1.pdf)  
  Keywords: dynamic, segmentation, 3d gaussian, ar, head, localization  
- **[RoSe-SLAM: Robust Semantic-Aware Gaussian Splatting SLAM from Dynamic Monocular Videos](https://arxiv.org/abs/2608.29003v1)**  
  Authors: Wenting Wang, Jiaxin Guo, Wenzhen Dong, Yun-Hui Liu, Charlie C. L. Wang, Yeung Yam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.29003v1.pdf)  
  Keywords: tracking, geometry, dynamic, semantic, mapping, ar, gaussian splatting, slam, motion, understanding  
- **[CGS-SLAM: Collaborative Gaussian Splatting based SLAM for Multi-Agent Reconstruction](https://arxiv.org/abs/2608.26868v1)**  
  Authors: Jean-Daniel de Ambrogi, Aladine Chetouani, Vincent Nguyen, Aurélien Chateigner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26868v1.pdf)  
  Keywords: tracking, dynamic, mapping, ar, gaussian splatting, slam, motion  
- **[Cross-Platform Benchmark of Neural 3D Reconstruction for Autonomous Laboratory Robots](https://arxiv.org/abs/2608.26383v1)**  
  Authors: Yongho Kim, Mengjiao Han, Victor Mateevitsi, Silvio Rizzi, Michael E. Papka, Nicola Ferrier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26383v1.pdf)  
  Keywords: tracking, lightweight, geometry, 3d gaussian, ar, gaussian splatting, nerf, 3d reconstruction  
- **[AquaFlow: A Monocular Gaussian Splatting SLAM for Underwater Streaming Reconstruction](https://arxiv.org/abs/2608.22906v1)**  
  Authors: Yingxiang Xu, Kerui Ren, Wenqi Guo, Changjian Jiang, Tao Lu, Linning Xu, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22906v1.pdf)  
  Keywords: tracking, geometry, 3d gaussian, mapping, ar, high-fidelity, gaussian splatting, slam, localization, efficient  

### Scene Understanding

*Showing the latest 50 out of 109 papers*

- **[NavArena: Automated Construction of Goal-Oriented Navigation Benchmarks from 3D Gaussian Splatting Reconstructions](https://arxiv.org/abs/2609.04602v1)**  
  Authors: Junhui Wang, Wei Yang, Xinyao Li, Ningjing Fan, Yuehao Yin, Xuecheng Chen, Chao Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04602v1.pdf)  
  Keywords: 3d gaussian, ar, semantic, gaussian splatting  
- **[Where Appearance Fails, Geometry Recognizes: A CAD-Free 3D Shape Prior That Complements Vision Foundation Models](https://arxiv.org/abs/2609.04381v1)**  
  Authors: Chenxi Tao, Seung-Kyum Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04381v1.pdf)  
  Keywords: geometry, recognition, 3d gaussian, ar, gaussian splatting, lighting, robotics  
- **[Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations](https://arxiv.org/abs/2609.02664v1)**  
  Authors: Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02664v1.pdf)  
  Keywords: 4d, dynamic, semantic, segmentation, ar, nerf, localization, understanding  
- **[MeshSplatBench: A Unified Benchmark for Triangle-Based Neural Rendering](https://arxiv.org/abs/2609.01306v1)**  
  Authors: Kaixuan Zhang, Minxian Li, Mingwu Ren, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.01306v1.pdf)  
  Keywords: neural rendering, ar, semantic, face  
- **[DSG: Dynamic 3D Scene Graph Construction for Embodied Agents in Changing Indoor Environments](https://arxiv.org/abs/2609.00619v1)**  
  Authors: Ming Liao, Chao Ye, Jianing Fei, Weiyang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00619v1.pdf)  
  Keywords: dynamic, semantic, 3d gaussian, ar, human  
- **[SMG: Semantic Motion Graph for Monocular Dynamic Gaussian Splatting](https://arxiv.org/abs/2608.31023v1)**  
  Authors: Haozheng Yu, Xinyu Yang, Rundong Luo, Jennifer J. Sun, Bharath Hariharan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.31023v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://smg-gaussian.github.io)  
  Keywords: dynamic, semantic, ar, gaussian splatting, motion  
- **[VCAR: Training-Free 3DGS Segmentation via View Completeness and Axis-Aware Boundary Refinement](https://arxiv.org/abs/2608.30870v1)**  
  Authors: Kun Cao, Di Wang, Haibin Zhu, Haozhi Huang, Xu Wang, Zheng Shi, Guanghua Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.30870v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DDKK0526/VCAR?style=social)](https://github.com/DDKK0526/VCAR)  
  Keywords: semantic, segmentation, compression, 3d gaussian, ar, head, gaussian splatting, understanding  
- **[SGRNet: Spatially Guided Radiology Network for Structured Radiological Reporting of Head and Neck Cancer](https://arxiv.org/abs/2608.29153v1)**  
  Authors: Ayush Gupta, Vinkle Srivastav, Prateek Upadhya, Amit Gupta, Krithika Rangarajan, Nicolas Padoy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.29153v1.pdf)  
  Keywords: dynamic, segmentation, 3d gaussian, ar, head, localization  
- **[RoSe-SLAM: Robust Semantic-Aware Gaussian Splatting SLAM from Dynamic Monocular Videos](https://arxiv.org/abs/2608.29003v1)**  
  Authors: Wenting Wang, Jiaxin Guo, Wenzhen Dong, Yun-Hui Liu, Charlie C. L. Wang, Yeung Yam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.29003v1.pdf)  
  Keywords: tracking, geometry, dynamic, semantic, mapping, ar, gaussian splatting, slam, motion, understanding  
- **[CoGeo-GS: Concept-Driven and Geometry-Aware Multi-Object Removal in 3D Scenes](https://arxiv.org/abs/2608.26656v1)**  
  Authors: Yuanxiang Ni, Xianliang Huang, Chenhang Ma, Chen Xiao, Yuewen Ma, Ruxin Wang, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26656v1.pdf)  
  Keywords: geometry, semantic, 3d gaussian, ar, gaussian splatting  



## Classic Papers
- **[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)** (SIGGRAPH 2023)  
  Authors: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis  
  Code: 🔗 [GitHub](https://github.com/graphdeco-inria/gaussian-splatting)  
  Keywords: Real-time Rendering, Neural Rendering, Point-based Graphics

- **[A Study on the Use of High Dynamic Range Imaging for Gaussian Splatting Methods: Are 8 Bits Enough?](https://doi.org/10.2312/stag.20241341)** (STAG 2024)  
  Authors: Valentina Piras, Amedeo F. Bonatti, Carmelo De Maria, Paolo Cignoni, Francesco Banterle  
  Paper: 📄 [PDF](https://iris.cnr.it/bitstream/20.500.14243/513755/3/Piras-Cignoni-Banterle_STAG20241341.pdf)  
  Keywords: High Dynamic Range, HDR, Tone Mapping, 3D Gaussian Splatting, Neural Radiance Fields

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
