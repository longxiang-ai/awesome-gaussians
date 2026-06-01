# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-06-01 02:39:34

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
- [Acceleration](#acceleration) (88 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (170 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (181 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (44 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (210 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (20 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (197 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (120 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (12 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (58 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (80 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (121 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: efficient, motion, survey, 3d reconstruction, geometry, tracking, ar, 3d gaussian, slam, gaussian splatting  
- **[A Survey of Spatial Memory Representations for Efficient Robot Navigation](https://arxiv.org/abs/2604.16482v1)**  
  Authors: Ma. Madecheen S. Pangaliman, Steven S. Sison, Erwin P. Quilloy, Rowel Atienza  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.16482v1.pdf)  
  Keywords: efficient, survey, semantic, ar, slam  
- **[Nevis Digital Twin: Photogrammetry and Immersive Visualization of Historical Sites](https://arxiv.org/abs/2603.20560v1)**  
  Authors: Alex Apffel, Huy Tran, Vuthea Chheang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20560v1.pdf)  
  Keywords: vr, survey, ar, 3d gaussian, gaussian splatting  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awareness](https://arxiv.org/abs/2603.17499v6)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v6.pdf) | [![GitHub](https://img.shields.io/github/stars/UNIC-Lab/Awesome-Radio-Map-Categorized?style=social)](https://github.com/UNIC-Lab/Awesome-Radio-Map-Categorized)  
  Keywords: survey, ray tracing, ar, mapping, 3d gaussian, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 88 papers*

- **[Supercharging Thermal Gaussian Splatting with Depth Estimation](https://arxiv.org/abs/2605.30328v1)**  
  Authors: Manoj Biswanath, Chenxin Cai, Hannah Schieber, Daniel Roth, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30328v1.pdf)  
  Keywords: efficient, fast, 3d reconstruction, ar, 3d gaussian, robotics, autonomous driving, gaussian splatting  
- **[Smaller and Faster 3DGS via Post-Training Dictionary Learning](https://arxiv.org/abs/2605.30396v1)**  
  Authors: Jiarong Gong, Jonas Unger, Ehsan Miandji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30396v1.pdf)  
  Keywords: fast, real-time rendering, compression, ar, 3d gaussian, gaussian splatting  
- **[Eulerian Gaussian Splatting using Hashed Probability Pyramids](https://arxiv.org/abs/2605.29136v1)**  
  Authors: Mia Gaia Polansky, George Kopanas, Stephan Garbin, Todd Zickler, Dor Verbin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29136v1.pdf)  
  Keywords: efficient, fast, ar, 3d gaussian, nerf, gaussian splatting  
- **[Gaussian-Voxel Duet: A Dual-Scaffolding Hybrid Representation for Fast and Accurate Monocular Surface Reconstruction](https://arxiv.org/abs/2605.26616v1)**  
  Authors: Zhenhua Du, Zhen Tan, Haoyu Zhang, Dewen Hu, Shuaifeng Zhi, Peidong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26616v1.pdf) | [![GitHub](https://img.shields.io/github/stars/duzh11/VoxelGS?style=social)](https://github.com/duzh11/VoxelGS)  
  Keywords: face, fast, real-time rendering, 3d reconstruction, geometry, ar, 3d gaussian, gaussian splatting, high-fidelity  
- **[F-RNG: Feed-Forward Relightable Neural Gaussians](https://arxiv.org/abs/2605.25975v2)**  
  Authors: Guangming Fu, Jiahui Fan, Jian Yang, Miloš Hašan, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25975v2.pdf)  
  Keywords: fast, lighting, illumination, geometry, ar, relighting, relightable, 3d gaussian, gaussian splatting, sparse-view, high-fidelity  
- **[ArtSplat: Feed-Forward Articulated 3D Gaussian Splatting from Sparse Multi-State Uncalibrated Views](https://arxiv.org/abs/2605.24304v1)**  
  Authors: Inseo Lee, Yoonji Kim, Eugene Sohn, Jiwoong Lee, Jungmin You, Joonseok Lee, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.24304v1.pdf)  
  Keywords: fast, motion, geometry, ar, 3d gaussian, nerf, gaussian splatting, sparse-view  
- **[No Pose, No Problem in 4D: Feed-Forward Dynamic Gaussians from Unposed Multi-View Videos](https://arxiv.org/abs/2605.22190v1)**  
  Authors: Matteo Balice, Yanik Kunzi, Chenyangguang Zhang, Matteo Matteucci, Marc Pollefeys, Sungwhan Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.22190v1.pdf)  
  Keywords: fast, motion, geometry, dynamic, ar, 3d gaussian, gaussian splatting, 4d  
- **[TWINGS: Thin Plate Splines Warp-aligned Initialization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2605.22069v2)**  
  Authors: Hyeseong Kim, Geonhui Son, Deukhee Lee, Dosik Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.22069v2.pdf)  
  Keywords: fast, ar, 3d gaussian, nerf, gaussian splatting, sparse-view, deformation  
- **[ForeSplat: Optimization-Aware Foresight for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2605.22020v2)**  
  Authors: Yuke Li, Weihang Liu, Cheng Zhang, Yuefeng Zhang, Jiadi Cui, Zixuan Wang, Junran Ding, Haoyu Wu, Yujiao Shi, Jingyi Yu, Xin Lou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.22020v2.pdf)  
  Keywords: fast, head, 3d reconstruction, ar, 3d gaussian, compact, lightweight, gaussian splatting, high-fidelity  
- **[Transcoding a 3D Gaussian Splatting Model from a Plenoptic Point Cloud or Mesh without the Original Multi-view Images](https://arxiv.org/abs/2605.21051v1)**  
  Authors: Maja Krivokuća, Riad Bendouro, Neus Sabater  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.21051v1.pdf)  
  Keywords: face, fast, ar, 3d gaussian, gaussian splatting  

### Applications

*Showing the latest 50 out of 498 papers*

- **[Learning Global Motion with Compact Gaussians for Feed-Forward 4D Reconstruction](https://arxiv.org/abs/2605.31595v1)**  
  Authors: Mungyeom Kim, Minkyeong Jeon, Honggyu An, Jaewoo Jung, Hyuna Ko, Jisang Han, Hyeonseo Yu, Donghwan Shin, Sunghwan Hong, Takuya Narihira, Kazumi Fukuda, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31595v1.pdf)  
  Keywords: motion, dynamic, ar, 3d gaussian, understanding, compact, tracking, 4d  
- **[Feature-Optimized Vision for Adaptive 3D Scene Reconstruction](https://arxiv.org/abs/2605.31534v1)**  
  Authors: Eric Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31534v1.pdf)  
  Keywords: ar, 3d reconstruction  
- **[VolFill: Single-View Amodal 3D Scene Reconstruction with Volumetric Flow Matching](https://arxiv.org/abs/2605.31466v1)**  
  Authors: Tuan Duc Ngo, Chuang Gan, Evangelos Kalogerakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31466v1.pdf)  
  Keywords: face, geometry, ar, understanding, compact  
- **[Triangle Splatting SLAM](https://arxiv.org/abs/2605.31419v1)**  
  Authors: Nicholas Fry, Eric Dexheimer, Kirill Mazur, Paul H. J. Kelly, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31419v1.pdf)  
  Keywords: geometry, tracking, ar, mapping, 3d gaussian, slam, gaussian splatting, deformation  
- **[LiftNav: Path Planning via Semantic Lifting in TSDF-Guided Gaussian Splatting](https://arxiv.org/abs/2605.31376v1)**  
  Authors: Hannah Schieber, Dominik Frischmann, Victor Schaack, Angela P. Schoellig, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31376v1.pdf)  
  Keywords: semantic, geometry, ar, understanding, gaussian splatting  
- **[Benchmarking Single-Step Inpainting Methods for Multi-Object 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2605.30987v1)**  
  Authors: Finn Dröge, Cecilia Curreli, Abhishek Saroha, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30987v1.pdf)  
  Keywords: face, ar, gaussian splatting, 3d gaussian  
- **[DSD-GS: Dynamic-Static Decomposition of Gaussian Splatting for Efficient and High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.30863v1)**  
  Authors: Youngtae Han, Sung-hwan Han, Youngmin Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30863v1.pdf)  
  Keywords: efficient, dynamic, ar, robotics, gaussian splatting, high-fidelity  
- **[Robust Dreamer: Deviation-Aware Latent Gaussian Memory for Action-Controlled AR Video Generation](https://arxiv.org/abs/2605.30855v1)**  
  Authors: Hanlin Chen, Jiaxin Wei, Xibin Song, Yifu Wang, Steve Wang, Hongdong Li, Pan Ji, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30855v1.pdf)  
  Keywords: ar, gaussian splatting, dynamic, geometry  
- **[Uncertainty-driven 3D Gaussian Splatting Active Mapping via Anisotropic Visibility Field](https://arxiv.org/abs/2605.30342v1)**  
  Authors: Shangjie Xue, Jesse Dill, Dhruv Ahuja, Frank Dellaert, Panagiotis Tsiotras, Danfei Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30342v1.pdf)  
  Keywords: efficient, ar, mapping, 3d gaussian, gaussian splatting  
- **[Supercharging Thermal Gaussian Splatting with Depth Estimation](https://arxiv.org/abs/2605.30328v1)**  
  Authors: Manoj Biswanath, Chenxin Cai, Hannah Schieber, Daniel Roth, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30328v1.pdf)  
  Keywords: efficient, fast, 3d reconstruction, ar, 3d gaussian, robotics, autonomous driving, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 170 papers*

- **[VolFill: Single-View Amodal 3D Scene Reconstruction with Volumetric Flow Matching](https://arxiv.org/abs/2605.31466v1)**  
  Authors: Tuan Duc Ngo, Chuang Gan, Evangelos Kalogerakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31466v1.pdf)  
  Keywords: face, geometry, ar, understanding, compact  
- **[Benchmarking Single-Step Inpainting Methods for Multi-Object 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2605.30987v1)**  
  Authors: Finn Dröge, Cecilia Curreli, Abhishek Saroha, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30987v1.pdf)  
  Keywords: face, ar, gaussian splatting, 3d gaussian  
- **[City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.30310v1)**  
  Authors: Sayan Paul, Sourav Ghosh, Siddharth Katageri, Soumyadip Maity, Sanjana Sinha, Brojeshwar Bhowmick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30310v1.pdf)  
  Keywords: face, large scene, urban scene, 3d reconstruction, geometry, ar, nerf, gaussian splatting, high-fidelity  
- **[PhyGenHOI: Physically-Aware 4D Generation of Dynamic Human-Object Interactions](https://arxiv.org/abs/2605.30268v1)**  
  Authors: Omer Benishu, Gal Fiebelman, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30268v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://omerbenishu.github.io/PhyGenHOI)  
  Keywords: motion, semantic, dynamic, human, ar, 3d gaussian, 4d  
- **[Comparative evaluation of photogrammetric reconstruction methods and 3D Gaussian Splatting for road surface roughness analysis](https://arxiv.org/abs/2605.29452v1)**  
  Authors: Marouane Elmegdar, Teng Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29452v1.pdf)  
  Keywords: face, 3d reconstruction, geometry, segmentation, ar, 3d gaussian, gaussian splatting  
- **[Gaussian-Voxel Duet: A Dual-Scaffolding Hybrid Representation for Fast and Accurate Monocular Surface Reconstruction](https://arxiv.org/abs/2605.26616v1)**  
  Authors: Zhenhua Du, Zhen Tan, Haoyu Zhang, Dewen Hu, Shuaifeng Zhi, Peidong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26616v1.pdf) | [![GitHub](https://img.shields.io/github/stars/duzh11/VoxelGS?style=social)](https://github.com/duzh11/VoxelGS)  
  Keywords: face, fast, real-time rendering, 3d reconstruction, geometry, ar, 3d gaussian, gaussian splatting, high-fidelity  
- **[TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction](https://arxiv.org/abs/2605.26115v1)**  
  Authors: Weijie Wang, Zimu Li, Jinchuan Shi, Zeyu Zhang, Botao Ye, Marc Pollefeys, Donny Y. Chen, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26115v1.pdf)  
  Keywords: face, head, 3d reconstruction, geometry, ar, sparse-view  
- **[R5DGS: Semantic-Aware 4D Gaussian Splatting with Rigid Body Constraints for Efficient Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.25909v1)**  
  Authors: Denis Gridusov, Maxim Popov, Sergey Kolyubin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25909v1.pdf)  
  Keywords: efficient, motion, vr, semantic, head, body, dynamic, ar, robotics, compact, gaussian splatting, 4d  
- **[SplitAvatar: One-shot Head Avatar with Autoregressive Gaussian Splitting](https://arxiv.org/abs/2605.25751v1)**  
  Authors: Hongzhe Liao, Chuhua Xian, Hongmin Cai, Haiyang Liu, Fa-Ting Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25751v1.pdf)  
  Keywords: efficient, head, avatar, dynamic, human, ar, 3d gaussian, gaussian splatting  
- **[Multi-view Consistent 3D Gaussian Head Avatars 'without' Multi-view Generation](https://arxiv.org/abs/2605.25220v1)**  
  Authors: Aviral Chharia, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/MVCHead)  
  Keywords: face, vr, head, avatar, human, ar, 3d gaussian, high-fidelity  

### Dynamic Scene

*Showing the latest 50 out of 181 papers*

- **[Learning Global Motion with Compact Gaussians for Feed-Forward 4D Reconstruction](https://arxiv.org/abs/2605.31595v1)**  
  Authors: Mungyeom Kim, Minkyeong Jeon, Honggyu An, Jaewoo Jung, Hyuna Ko, Jisang Han, Hyeonseo Yu, Donghwan Shin, Sunghwan Hong, Takuya Narihira, Kazumi Fukuda, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31595v1.pdf)  
  Keywords: motion, dynamic, ar, 3d gaussian, understanding, compact, tracking, 4d  
- **[Triangle Splatting SLAM](https://arxiv.org/abs/2605.31419v1)**  
  Authors: Nicholas Fry, Eric Dexheimer, Kirill Mazur, Paul H. J. Kelly, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31419v1.pdf)  
  Keywords: geometry, tracking, ar, mapping, 3d gaussian, slam, gaussian splatting, deformation  
- **[DSD-GS: Dynamic-Static Decomposition of Gaussian Splatting for Efficient and High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.30863v1)**  
  Authors: Youngtae Han, Sung-hwan Han, Youngmin Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30863v1.pdf)  
  Keywords: efficient, dynamic, ar, robotics, gaussian splatting, high-fidelity  
- **[Robust Dreamer: Deviation-Aware Latent Gaussian Memory for Action-Controlled AR Video Generation](https://arxiv.org/abs/2605.30855v1)**  
  Authors: Hanlin Chen, Jiaxin Wei, Xibin Song, Yifu Wang, Steve Wang, Hongdong Li, Pan Ji, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30855v1.pdf)  
  Keywords: ar, gaussian splatting, dynamic, geometry  
- **[PhyGenHOI: Physically-Aware 4D Generation of Dynamic Human-Object Interactions](https://arxiv.org/abs/2605.30268v1)**  
  Authors: Omer Benishu, Gal Fiebelman, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30268v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://omerbenishu.github.io/PhyGenHOI)  
  Keywords: motion, semantic, dynamic, human, ar, 3d gaussian, 4d  
- **[FRUC: Feedforward Dynamic Scene Reconstruction from Uncalibrated Collaborative Driving Views](https://arxiv.org/abs/2605.29997v1)**  
  Authors: Yihang Tao, Yu Guo, Zhengru Fang, Haonan An, Yuguang Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29997v1.pdf)  
  Keywords: efficient, geometry, dynamic, ar, 3d gaussian, gaussian splatting  
- **[DGSG-Mind: Dynamic 3D Gaussian Scene Graphs for Long-Term Scene Understanding and Grounding](https://arxiv.org/abs/2605.29879v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Jinyan Liu, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29879v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://icr-lab.github.io/DGSG-Mind)  
  Keywords: semantic, dynamic, segmentation, geometry, mapping, localization, ar, 3d gaussian, understanding  
- **[EMAG: Differentiable 4D Gaussian Mixture Splatting for EEG Spatial Super-Resolution](https://arxiv.org/abs/2605.29731v1)**  
  Authors: Alex Lazarovich, Ofir Itzhak Shahar, Gur Elkin, Ohad Ben-Shahar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29731v1.pdf)  
  Keywords: localization, ar, 4d  
- **[FreeForm: Reduced-Order Deformable Simulation from Particle-Based Skinning Eigenmodes](https://arxiv.org/abs/2605.29318v1)**  
  Authors: Donglai Xiang, Vismay Modi, Rishit Dagli, Ty Trusty, Gilles Daviet, Anka He Chen, Nicholas Sharp, David I. W. Levin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29318v1.pdf)  
  Keywords: ar, dynamic, geometry  
- **[R5DGS: Semantic-Aware 4D Gaussian Splatting with Rigid Body Constraints for Efficient Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.25909v1)**  
  Authors: Denis Gridusov, Maxim Popov, Sergey Kolyubin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25909v1.pdf)  
  Keywords: efficient, motion, vr, semantic, head, body, dynamic, ar, robotics, compact, gaussian splatting, 4d  

### Few-shot

- **[TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction](https://arxiv.org/abs/2605.26115v1)**  
  Authors: Weijie Wang, Zimu Li, Jinchuan Shi, Zeyu Zhang, Botao Ye, Marc Pollefeys, Donny Y. Chen, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26115v1.pdf)  
  Keywords: face, head, 3d reconstruction, geometry, ar, sparse-view  
- **[F-RNG: Feed-Forward Relightable Neural Gaussians](https://arxiv.org/abs/2605.25975v2)**  
  Authors: Guangming Fu, Jiahui Fan, Jian Yang, Miloš Hašan, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25975v2.pdf)  
  Keywords: fast, lighting, illumination, geometry, ar, relighting, relightable, 3d gaussian, gaussian splatting, sparse-view, high-fidelity  
- **[ArtSplat: Feed-Forward Articulated 3D Gaussian Splatting from Sparse Multi-State Uncalibrated Views](https://arxiv.org/abs/2605.24304v1)**  
  Authors: Inseo Lee, Yoonji Kim, Eugene Sohn, Jiwoong Lee, Jungmin You, Joonseok Lee, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.24304v1.pdf)  
  Keywords: fast, motion, geometry, ar, 3d gaussian, nerf, gaussian splatting, sparse-view  
- **[TWINGS: Thin Plate Splines Warp-aligned Initialization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2605.22069v2)**  
  Authors: Hyeseong Kim, Geonhui Son, Deukhee Lee, Dosik Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.22069v2.pdf)  
  Keywords: fast, ar, 3d gaussian, nerf, gaussian splatting, sparse-view, deformation  
- **[P2GS: Physical Prior-guided Gaussian Splatting for Photometrically Consistent Urban Reconstruction](https://arxiv.org/abs/2605.16925v1)**  
  Authors: Kota Shimomura, Hidehisa Arai, Tsubasa Takahashi, Takayoshi Yamashita, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.16925v1.pdf)  
  Keywords: fast, lighting, illumination, dynamic, outdoor, ar, mapping, 3d gaussian, autonomous driving, sparse view, gaussian splatting, high-fidelity  
- **[FFAvatar: Few-Shot, Feed-Forward, and Generalizable Avatar Reconstruction](https://arxiv.org/abs/2605.15320v1)**  
  Authors: Thuan Hoang Nguyen, Jiahao Luo, Yinyu Nie, Hao Li, Gordon Guocheng Qian, Jian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15320v1.pdf)  
  Keywords: head, avatar, animation, ar, 3d gaussian, few-shot, high-fidelity  
- **[PanoPlane: Plane-Aware Panoramic Completion for Sparse-View Indoor 3D Gaussian Splatting](https://arxiv.org/abs/2605.14135v1)**  
  Authors: Adil Qureshi, Dongki Jung, Jaehoon Choi, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14135v1.pdf)  
  Keywords: face, geometry, ar, 3d gaussian, gaussian splatting, sparse-view, high-fidelity  
- **[GeoQuery: Geometry-Query Diffusion for Sparse-View Reconstruction](https://arxiv.org/abs/2605.12399v1)**  
  Authors: Xiao Cao, Yuze Li, Youmin Zhang, Jiayu Song, Cheng Yan, Wen Li, Lixin Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12399v1.pdf)  
  Keywords: 3d reconstruction, geometry, ar, 3d gaussian, gaussian splatting, sparse-view  
- **[PairDropGS: Paired Dropout-Induced Consistency Regularization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2605.12072v2)**  
  Authors: Hantang Li, Qiang Zhu, Xiandong Meng, Xingtao Wang, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12072v2.pdf)  
  Keywords: geometry, ar, 3d gaussian, gaussian splatting, sparse-view  
- **[VidSplat: Gaussian Splatting Reconstruction with Geometry-Guided Video Diffusion Priors](https://arxiv.org/abs/2605.11424v1)**  
  Authors: Jimin Tang, Wenyuan Zhang, Junsheng Zhou, Zian Huang, Kanle Shi, Shenkun Xu, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11424v1.pdf)  
  Keywords: face, geometry, ar, gaussian splatting, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 210 papers*

- **[Feature-Optimized Vision for Adaptive 3D Scene Reconstruction](https://arxiv.org/abs/2605.31534v1)**  
  Authors: Eric Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31534v1.pdf)  
  Keywords: ar, 3d reconstruction  
- **[VolFill: Single-View Amodal 3D Scene Reconstruction with Volumetric Flow Matching](https://arxiv.org/abs/2605.31466v1)**  
  Authors: Tuan Duc Ngo, Chuang Gan, Evangelos Kalogerakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31466v1.pdf)  
  Keywords: face, geometry, ar, understanding, compact  
- **[Triangle Splatting SLAM](https://arxiv.org/abs/2605.31419v1)**  
  Authors: Nicholas Fry, Eric Dexheimer, Kirill Mazur, Paul H. J. Kelly, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31419v1.pdf)  
  Keywords: geometry, tracking, ar, mapping, 3d gaussian, slam, gaussian splatting, deformation  
- **[LiftNav: Path Planning via Semantic Lifting in TSDF-Guided Gaussian Splatting](https://arxiv.org/abs/2605.31376v1)**  
  Authors: Hannah Schieber, Dominik Frischmann, Victor Schaack, Angela P. Schoellig, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31376v1.pdf)  
  Keywords: semantic, geometry, ar, understanding, gaussian splatting  
- **[Robust Dreamer: Deviation-Aware Latent Gaussian Memory for Action-Controlled AR Video Generation](https://arxiv.org/abs/2605.30855v1)**  
  Authors: Hanlin Chen, Jiaxin Wei, Xibin Song, Yifu Wang, Steve Wang, Hongdong Li, Pan Ji, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30855v1.pdf)  
  Keywords: ar, gaussian splatting, dynamic, geometry  
- **[Supercharging Thermal Gaussian Splatting with Depth Estimation](https://arxiv.org/abs/2605.30328v1)**  
  Authors: Manoj Biswanath, Chenxin Cai, Hannah Schieber, Daniel Roth, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30328v1.pdf)  
  Keywords: efficient, fast, 3d reconstruction, ar, 3d gaussian, robotics, autonomous driving, gaussian splatting  
- **[MonoPhysics: Estimating Geometry, Appearance, and Physical Parameters from Monocular Videos](https://arxiv.org/abs/2605.30320v1)**  
  Authors: Daniel Rho, Jun Myeong Choi, Matthew Thornton, Biswadip Dey, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30320v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://daniel03c1.github.io/MonoPhysics)  
  Keywords: ar, geometry, gaussian splatting, 3d gaussian  
- **[City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.30310v1)**  
  Authors: Sayan Paul, Sourav Ghosh, Siddharth Katageri, Soumyadip Maity, Sanjana Sinha, Brojeshwar Bhowmick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30310v1.pdf)  
  Keywords: face, large scene, urban scene, 3d reconstruction, geometry, ar, nerf, gaussian splatting, high-fidelity  
- **[FRUC: Feedforward Dynamic Scene Reconstruction from Uncalibrated Collaborative Driving Views](https://arxiv.org/abs/2605.29997v1)**  
  Authors: Yihang Tao, Yu Guo, Zhengru Fang, Haonan An, Yuguang Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29997v1.pdf)  
  Keywords: efficient, geometry, dynamic, ar, 3d gaussian, gaussian splatting  
- **[DGSG-Mind: Dynamic 3D Gaussian Scene Graphs for Long-Term Scene Understanding and Grounding](https://arxiv.org/abs/2605.29879v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Jinyan Liu, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29879v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://icr-lab.github.io/DGSG-Mind)  
  Keywords: semantic, dynamic, segmentation, geometry, mapping, localization, ar, 3d gaussian, understanding  

### Large Scene

- **[City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.30310v1)**  
  Authors: Sayan Paul, Sourav Ghosh, Siddharth Katageri, Soumyadip Maity, Sanjana Sinha, Brojeshwar Bhowmick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30310v1.pdf)  
  Keywords: face, large scene, urban scene, 3d reconstruction, geometry, ar, nerf, gaussian splatting, high-fidelity  
- **[GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction](https://arxiv.org/abs/2605.23888v1)**  
  Authors: Katharina Schmid, Nicolas von Lützow, Jozef Hladký, Angela Dai, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.23888v1.pdf)  
  Keywords: large scene, ar, geometry, high-fidelity  
- **[Diffusion-guided Generalizable Enhancer for Urban Scene Reconstruction](https://arxiv.org/abs/2605.22420v1)**  
  Authors: Henry Che, Jingkang Wang, Yun Chen, Ze Yang, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.22420v1.pdf)  
  Keywords: efficient, urban scene, neural rendering, ar, 3d gaussian, autonomous driving, high-fidelity  
- **[Feed-Forward Gaussian Splatting from Sparse Aerial Views](https://arxiv.org/abs/2605.19949v1)**  
  Authors: Dongli Wu, Zhuoxiao Li, Tongyan Hua, Yinrui Ren, Xiaobao Wei, Rongjun Qin, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.19949v1.pdf)  
  Keywords: urban scene, geometry, ar, 3d gaussian, gaussian splatting  
- **[Cross-View Splatter: Feed-Forward View Synthesis with Georeferenced Images](https://arxiv.org/abs/2605.19656v1)**  
  Authors: Matias Turkulainen, Akshay Krishnan, Filippo Aleotti, Mohamed Sayed, Guillermo Garcia-Hernando, Juho Kannala, Arno Solin, Gabriel Brostow, Daniyar Turmukhambetov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.19656v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nianticspatial.github.io/cross-view-splatter)  
  Keywords: ar, mapping, outdoor  
- **[P2GS: Physical Prior-guided Gaussian Splatting for Photometrically Consistent Urban Reconstruction](https://arxiv.org/abs/2605.16925v1)**  
  Authors: Kota Shimomura, Hidehisa Arai, Tsubasa Takahashi, Takayoshi Yamashita, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.16925v1.pdf)  
  Keywords: fast, lighting, illumination, dynamic, outdoor, ar, mapping, 3d gaussian, autonomous driving, sparse view, gaussian splatting, high-fidelity  
- **[PropSplat: Map-Free RF Field Reconstruction via 3D Gaussian Propagation Splatting](https://arxiv.org/abs/2605.08035v1)**  
  Authors: William Bjorndahl, Maninder Pal Singh, Farhad Nouri, Joseph Camp  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.08035v1.pdf)  
  Keywords: outdoor, localization, ar, 3d gaussian, nerf  
- **[FieryGS: In-the-Wild Fire Synthesis with Physics-Integrated Gaussian Splatting](https://arxiv.org/abs/2605.00177v1)**  
  Authors: Qianfan Shen, Ningxiao Tao, Qiyu Dai, Tianle Chen, Minghan Qin, Yongjie Zhang, Mengyu Chu, Wenzheng Chen, Baoquan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/FieryGS)  
  Keywords: efficient, face, geometry, dynamic, outdoor, ar, 3d gaussian, gaussian splatting, high-fidelity  
- **[Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193v1)**  
  Authors: Vinayak Gupta, Chih-Hao Lin, Shenlong Wang, Anand Bhattad, Jia-Bin Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28193v1.pdf)  
  Keywords: semantic, lighting, illumination, 3d reconstruction, dynamic, outdoor, segmentation, ar, 3d gaussian, sparse view, sparse-view  
- **[EnerGS: Energy-Based Gaussian Splatting with Partial Geometric Priors](https://arxiv.org/abs/2604.26238v1)**  
  Authors: Rui Song, Tianhui Cai, Markus Gross, Yun Zhang, Walter Zimmer, Zhiyu Huang, Olaf Wysocki, Jiaqi Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26238v1.pdf)  
  Keywords: outdoor, geometry, ar, 3d gaussian, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 197 papers*

- **[Learning Global Motion with Compact Gaussians for Feed-Forward 4D Reconstruction](https://arxiv.org/abs/2605.31595v1)**  
  Authors: Mungyeom Kim, Minkyeong Jeon, Honggyu An, Jaewoo Jung, Hyuna Ko, Jisang Han, Hyeonseo Yu, Donghwan Shin, Sunghwan Hong, Takuya Narihira, Kazumi Fukuda, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31595v1.pdf)  
  Keywords: motion, dynamic, ar, 3d gaussian, understanding, compact, tracking, 4d  
- **[VolFill: Single-View Amodal 3D Scene Reconstruction with Volumetric Flow Matching](https://arxiv.org/abs/2605.31466v1)**  
  Authors: Tuan Duc Ngo, Chuang Gan, Evangelos Kalogerakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31466v1.pdf)  
  Keywords: face, geometry, ar, understanding, compact  
- **[DSD-GS: Dynamic-Static Decomposition of Gaussian Splatting for Efficient and High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.30863v1)**  
  Authors: Youngtae Han, Sung-hwan Han, Youngmin Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30863v1.pdf)  
  Keywords: efficient, dynamic, ar, robotics, gaussian splatting, high-fidelity  
- **[Uncertainty-driven 3D Gaussian Splatting Active Mapping via Anisotropic Visibility Field](https://arxiv.org/abs/2605.30342v1)**  
  Authors: Shangjie Xue, Jesse Dill, Dhruv Ahuja, Frank Dellaert, Panagiotis Tsiotras, Danfei Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30342v1.pdf)  
  Keywords: efficient, ar, mapping, 3d gaussian, gaussian splatting  
- **[Supercharging Thermal Gaussian Splatting with Depth Estimation](https://arxiv.org/abs/2605.30328v1)**  
  Authors: Manoj Biswanath, Chenxin Cai, Hannah Schieber, Daniel Roth, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30328v1.pdf)  
  Keywords: efficient, fast, 3d reconstruction, ar, 3d gaussian, robotics, autonomous driving, gaussian splatting  
- **[FRUC: Feedforward Dynamic Scene Reconstruction from Uncalibrated Collaborative Driving Views](https://arxiv.org/abs/2605.29997v1)**  
  Authors: Yihang Tao, Yu Guo, Zhengru Fang, Haonan An, Yuguang Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29997v1.pdf)  
  Keywords: efficient, geometry, dynamic, ar, 3d gaussian, gaussian splatting  
- **[Smaller and Faster 3DGS via Post-Training Dictionary Learning](https://arxiv.org/abs/2605.30396v1)**  
  Authors: Jiarong Gong, Jonas Unger, Ehsan Miandji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30396v1.pdf)  
  Keywords: fast, real-time rendering, compression, ar, 3d gaussian, gaussian splatting  
- **[BitC-3DGS: High-Capacity 3D Gaussian Splatting Watermarking via Bit Compression](https://arxiv.org/abs/2605.29583v1)**  
  Authors: Yuquan Bi, Baosheng Yu, Yingke Lei, Jianwei Yang, Hongsong Wang, Jie Gui, Yuan Yan Tang, James Tin-Yau Kwok  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29583v1.pdf)  
  Keywords: semantic, compression, ar, 3d gaussian, gaussian splatting  
- **[Eulerian Gaussian Splatting using Hashed Probability Pyramids](https://arxiv.org/abs/2605.29136v1)**  
  Authors: Mia Gaia Polansky, George Kopanas, Stephan Garbin, Todd Zickler, Dor Verbin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29136v1.pdf)  
  Keywords: efficient, fast, ar, 3d gaussian, nerf, gaussian splatting  
- **[GScomp-QA: A Subjective Dataset for Quality Assessment of Compressed Gaussian Splatting](https://arxiv.org/abs/2605.26880v1)**  
  Authors: Pedro Martin, António Rodrigues, João Ascenso, Maria Paula Queluz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26880v1.pdf)  
  Keywords: efficient, compression, 3d reconstruction, ar, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 120 papers*

- **[DSD-GS: Dynamic-Static Decomposition of Gaussian Splatting for Efficient and High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.30863v1)**  
  Authors: Youngtae Han, Sung-hwan Han, Youngmin Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30863v1.pdf)  
  Keywords: efficient, dynamic, ar, robotics, gaussian splatting, high-fidelity  
- **[City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.30310v1)**  
  Authors: Sayan Paul, Sourav Ghosh, Siddharth Katageri, Soumyadip Maity, Sanjana Sinha, Brojeshwar Bhowmick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30310v1.pdf)  
  Keywords: face, large scene, urban scene, 3d reconstruction, geometry, ar, nerf, gaussian splatting, high-fidelity  
- **[POINav: Benchmarking and Enhancing Final-Meters Arrival in Real-World Vision-Language Navigation](https://arxiv.org/abs/2605.28237v1)**  
  Authors: Ruiyan Gong, Meisheng Zhang, Yuxiang Zhao, Mingchao Sun, Yanfen Shen, Zedong Chu, Zhining Gu, Wei Guo, Xiaolong Cheng, Qiming Li, Kangning Niu, Yanqing Zhu, Xiaolong Wu, Tianlun Li, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.28237v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, 3d gaussian  
- **[Gaussian-Voxel Duet: A Dual-Scaffolding Hybrid Representation for Fast and Accurate Monocular Surface Reconstruction](https://arxiv.org/abs/2605.26616v1)**  
  Authors: Zhenhua Du, Zhen Tan, Haoyu Zhang, Dewen Hu, Shuaifeng Zhi, Peidong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26616v1.pdf) | [![GitHub](https://img.shields.io/github/stars/duzh11/VoxelGS?style=social)](https://github.com/duzh11/VoxelGS)  
  Keywords: face, fast, real-time rendering, 3d reconstruction, geometry, ar, 3d gaussian, gaussian splatting, high-fidelity  
- **[F-RNG: Feed-Forward Relightable Neural Gaussians](https://arxiv.org/abs/2605.25975v2)**  
  Authors: Guangming Fu, Jiahui Fan, Jian Yang, Miloš Hašan, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25975v2.pdf)  
  Keywords: fast, lighting, illumination, geometry, ar, relighting, relightable, 3d gaussian, gaussian splatting, sparse-view, high-fidelity  
- **[Depth Peeling for High-Fidelity Gaussian-Enhanced Surfel Rendering](https://arxiv.org/abs/2605.25345v1)**  
  Authors: Keyang Ye, Hongzhi Wu, Kun Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25345v1.pdf)  
  Keywords: ar, 3d gaussian, nerf, gaussian splatting, high-fidelity  
- **[Multi-view Consistent 3D Gaussian Head Avatars 'without' Multi-view Generation](https://arxiv.org/abs/2605.25220v1)**  
  Authors: Aviral Chharia, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/MVCHead)  
  Keywords: face, vr, head, avatar, human, ar, 3d gaussian, high-fidelity  
- **[ParkingWorld: End-to-End Autonomous Parking Reinforcement Learning from Corrective Experience in 3DGS Simulation](https://arxiv.org/abs/2605.25029v2)**  
  Authors: Zhengcheng Yu, Changze Li, Haoran Liu, Tong Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25029v2.pdf)  
  Keywords: efficient, face, head, human, ar, 3d gaussian, gaussian splatting, high-fidelity  
- **[GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction](https://arxiv.org/abs/2605.23888v1)**  
  Authors: Katharina Schmid, Nicolas von Lützow, Jozef Hladký, Angela Dai, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.23888v1.pdf)  
  Keywords: large scene, ar, geometry, high-fidelity  
- **[Sensor2Sensor: Cross-Embodiment Sensor Conversion for Autonomous Driving](https://arxiv.org/abs/2605.22809v2)**  
  Authors: Jiahao Wang, Bo Sun, Yijing Bai, Vincent Casser, Songyou Peng, Zehao Zhu, Meng-Li Shih, Xander Masotto, Shih-Yang Su, Kanaad V Parvate, Tiancheng Ge, Linn Bieske, Dragomir Anguelov, Mingxing Tan, Chiyu Max Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.22809v2.pdf)  
  Keywords: ar, high-fidelity, autonomous driving, gaussian splatting, 4d  

### Ray Tracing

- **[Underwater360: Reconstructing Underwater Scenes from Panoramic Images with Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2605.26447v1)**  
  Authors: Jiangbei Hu, Weichao Song, Shibo Yu, Mohan Wang, Zihan Yi, Rui Wu, Mingkang Xiang, Na Lei, Shengfa Wang, Zhongxuan Luo, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26447v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SwcK423/Underwater360?style=social)](https://github.com/SwcK423/Underwater360)  
  Keywords: ray casting, ar, gaussian splatting, 3d gaussian  
- **[Differentiable Ray Tracing with Gaussians for Unified Radio Propagation Simulation and View Synthesis](https://arxiv.org/abs/2605.07781v1)**  
  Authors: Niklas Vaara, Lam Huynh, Pekka Sangi, Miguel Bordallo López, Janne Heikkilä  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.07781v1.pdf)  
  Keywords: ray tracing, geometry, ar, 3d gaussian, gaussian splatting, high-fidelity  
- **[Power Foam: Unifying Real-Time Differentiable Ray Tracing and Rasterization](https://arxiv.org/abs/2604.24994v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Dor Verbin, Kwang Moo Yi, Anish Prabhu, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24994v1.pdf)  
  Keywords: efficient, face, ray tracing, geometry, ar  
- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138v1)**  
  Authors: Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/viserdex)  
  Keywords: efficient, semantic, lighting, ray tracing, dynamic, ar, 3d gaussian, robotics, tracking, gaussian splatting  
- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: face, reflection, ray tracing, ar, gaussian splatting  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: efficient, reflection, ray casting, ar, 3d gaussian  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: efficient, face, semantic, ray tracing, tracking, localization, mapping, ar, 3d gaussian, slam, gaussian splatting  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: reflection, ray tracing, ar, shadow, relightable, mapping, 3d gaussian, gaussian splatting  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: path tracing, face, real-time rendering, geometry, ar, 3d gaussian  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: efficient, fast, face, real-time rendering, ray tracing, geometry, ar, 3d gaussian, nerf, gaussian splatting, high-fidelity  

### Relighting

*Showing the latest 50 out of 58 papers*

- **[F-RNG: Feed-Forward Relightable Neural Gaussians](https://arxiv.org/abs/2605.25975v2)**  
  Authors: Guangming Fu, Jiahui Fan, Jian Yang, Miloš Hašan, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25975v2.pdf)  
  Keywords: fast, lighting, illumination, geometry, ar, relighting, relightable, 3d gaussian, gaussian splatting, sparse-view, high-fidelity  
- **[COSY: Compositional 3DGS Synthesis for Disentangled Human Head Editing](https://arxiv.org/abs/2605.24114v1)**  
  Authors: Florian Barthel, Shalini De Mello, Koki Nagano, Wieland Morgenstern, Anna Hilsmann, Peter Eisert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.24114v1.pdf)  
  Keywords: semantic, lighting, head, human, segmentation, ar, 3d gaussian, gaussian splatting  
- **[SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation](https://arxiv.org/abs/2605.22536v1)**  
  Authors: Xiaolong Zhou, Yifei Liu, Ziyang Gong, Jiarui Li, Qiyue Zhao, Muyao Niu, Yuanyuan Gao, Le Ma, Xue Yang, Hongjie Zhang, Zhihang Zhong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.22536v1.pdf)  
  Keywords: motion, lighting, compression, human, ar, 3d gaussian, understanding, gaussian splatting  
- **[Towards Physically Consistent 4D Scene Reconstruction for Closed-loop Autonomous Driving Simulation](https://arxiv.org/abs/2605.21032v1)**  
  Authors: Bowyn Tan, Yutong Xie, Bai Huang, Fan Luo, Xiao Li, Naizheng Wang, Yang Guan, Shengbo Eben Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.21032v1.pdf)  
  Keywords: dynamic, ar, shadow, high-fidelity, autonomous driving, 4d  
- **[A Geometric Algebra-Informed 3DGS Framework for Wireless Channel Prediction](https://arxiv.org/abs/2605.19065v2)**  
  Authors: Jingzhou Shen, Tianya Zhao, Xuyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.19065v2.pdf)  
  Keywords: reflection, ar, gaussian splatting, 3d gaussian  
- **[RT-Splatting: Joint Reflection-Transmission Modeling with Gaussian Splatting](https://arxiv.org/abs/2605.18263v1)**  
  Authors: Ji Shi, Xianghua Ying, Bowei Xing, Ruohao Guo, Wenzhen Yue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.18263v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sjj118.github.io/RT-Splatting)  
  Keywords: face, reflection, real-time rendering, ar, 3d gaussian, gaussian splatting, high-fidelity  
- **[A Single Atlas is All You Need: Decoder-Side Gaussian Splatting for Immersive Video](https://arxiv.org/abs/2605.17002v1)**  
  Authors: Dawid Mieloch, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.17002v1.pdf)  
  Keywords: reflection, compression, ar, 3d gaussian, gaussian splatting  
- **[P2GS: Physical Prior-guided Gaussian Splatting for Photometrically Consistent Urban Reconstruction](https://arxiv.org/abs/2605.16925v1)**  
  Authors: Kota Shimomura, Hidehisa Arai, Tsubasa Takahashi, Takayoshi Yamashita, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.16925v1.pdf)  
  Keywords: fast, lighting, illumination, dynamic, outdoor, ar, mapping, 3d gaussian, autonomous driving, sparse view, gaussian splatting, high-fidelity  
- **[3DEditSafe: Defending 3D Editing Pipelines from Unsafe Generation](https://arxiv.org/abs/2605.15398v1)**  
  Authors: Nicole Meng, Zheyuan Liu, Meng Jiang, Yingjie Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15398v1.pdf)  
  Keywords: semantic, lighting, ar, 3d gaussian, gaussian splatting, high-fidelity  
- **[HarmoGS: Robust 3D Gaussian Splatting in the Wild via Conflict-Aware Gradient Harmonization](https://arxiv.org/abs/2605.13073v2)**  
  Authors: Yulei Kang, Tianze Zhu, Jian-Fang Hu, Jianhuang Lai, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13073v2.pdf)  
  Keywords: semantic, illumination, ar, 3d gaussian, gaussian splatting  

### SLAM

*Showing the latest 50 out of 80 papers*

- **[Learning Global Motion with Compact Gaussians for Feed-Forward 4D Reconstruction](https://arxiv.org/abs/2605.31595v1)**  
  Authors: Mungyeom Kim, Minkyeong Jeon, Honggyu An, Jaewoo Jung, Hyuna Ko, Jisang Han, Hyeonseo Yu, Donghwan Shin, Sunghwan Hong, Takuya Narihira, Kazumi Fukuda, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31595v1.pdf)  
  Keywords: motion, dynamic, ar, 3d gaussian, understanding, compact, tracking, 4d  
- **[Triangle Splatting SLAM](https://arxiv.org/abs/2605.31419v1)**  
  Authors: Nicholas Fry, Eric Dexheimer, Kirill Mazur, Paul H. J. Kelly, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31419v1.pdf)  
  Keywords: geometry, tracking, ar, mapping, 3d gaussian, slam, gaussian splatting, deformation  
- **[Uncertainty-driven 3D Gaussian Splatting Active Mapping via Anisotropic Visibility Field](https://arxiv.org/abs/2605.30342v1)**  
  Authors: Shangjie Xue, Jesse Dill, Dhruv Ahuja, Frank Dellaert, Panagiotis Tsiotras, Danfei Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30342v1.pdf)  
  Keywords: efficient, ar, mapping, 3d gaussian, gaussian splatting  
- **[DGSG-Mind: Dynamic 3D Gaussian Scene Graphs for Long-Term Scene Understanding and Grounding](https://arxiv.org/abs/2605.29879v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Jinyan Liu, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29879v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://icr-lab.github.io/DGSG-Mind)  
  Keywords: semantic, dynamic, segmentation, geometry, mapping, localization, ar, 3d gaussian, understanding  
- **[EMAG: Differentiable 4D Gaussian Mixture Splatting for EEG Spatial Super-Resolution](https://arxiv.org/abs/2605.29731v1)**  
  Authors: Alex Lazarovich, Ofir Itzhak Shahar, Gur Elkin, Ohad Ben-Shahar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29731v1.pdf)  
  Keywords: localization, ar, 4d  
- **[Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments](https://arxiv.org/abs/2605.21935v1)**  
  Authors: Peifeng Jiang, Hong Liu, Jin Jin, Wenshuai Wang, Xia Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.21935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziya-jiang.github.io/MIF-homepage)  
  Keywords: motion, semantic, geometry, dynamic, human, mapping, ar, 3d gaussian, gaussian splatting  
- **[GLUT: 3D Gaussian Lookup Table for Continuous Color Transformation](https://arxiv.org/abs/2605.19889v1)**  
  Authors: Danna Xue, David Serrano-Lozano, Shaolin Su, Javier Vazquez-Corral  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.19889v1.pdf)  
  Keywords: efficient, ar, mapping, 3d gaussian, compact  
- **[Cross-View Splatter: Feed-Forward View Synthesis with Georeferenced Images](https://arxiv.org/abs/2605.19656v1)**  
  Authors: Matias Turkulainen, Akshay Krishnan, Filippo Aleotti, Mohamed Sayed, Guillermo Garcia-Hernando, Juho Kannala, Arno Solin, Gabriel Brostow, Daniyar Turmukhambetov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.19656v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nianticspatial.github.io/cross-view-splatter)  
  Keywords: ar, mapping, outdoor  
- **[Efficient Sparse-to-Dense Visual Localization via Compact Gaussian Scene Representation and Accelerated Dense Pose Estimation](https://arxiv.org/abs/2605.17777v1)**  
  Authors: Zizhuo Li, Songchu Deng, Linfeng Tang, Jiayi Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.17777v1.pdf)  
  Keywords: efficient, head, localization, ar, 3d gaussian, compact, gaussian splatting  
- **[P2GS: Physical Prior-guided Gaussian Splatting for Photometrically Consistent Urban Reconstruction](https://arxiv.org/abs/2605.16925v1)**  
  Authors: Kota Shimomura, Hidehisa Arai, Tsubasa Takahashi, Takayoshi Yamashita, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.16925v1.pdf)  
  Keywords: fast, lighting, illumination, dynamic, outdoor, ar, mapping, 3d gaussian, autonomous driving, sparse view, gaussian splatting, high-fidelity  

### Scene Understanding

*Showing the latest 50 out of 121 papers*

- **[Learning Global Motion with Compact Gaussians for Feed-Forward 4D Reconstruction](https://arxiv.org/abs/2605.31595v1)**  
  Authors: Mungyeom Kim, Minkyeong Jeon, Honggyu An, Jaewoo Jung, Hyuna Ko, Jisang Han, Hyeonseo Yu, Donghwan Shin, Sunghwan Hong, Takuya Narihira, Kazumi Fukuda, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31595v1.pdf)  
  Keywords: motion, dynamic, ar, 3d gaussian, understanding, compact, tracking, 4d  
- **[VolFill: Single-View Amodal 3D Scene Reconstruction with Volumetric Flow Matching](https://arxiv.org/abs/2605.31466v1)**  
  Authors: Tuan Duc Ngo, Chuang Gan, Evangelos Kalogerakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31466v1.pdf)  
  Keywords: face, geometry, ar, understanding, compact  
- **[LiftNav: Path Planning via Semantic Lifting in TSDF-Guided Gaussian Splatting](https://arxiv.org/abs/2605.31376v1)**  
  Authors: Hannah Schieber, Dominik Frischmann, Victor Schaack, Angela P. Schoellig, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.31376v1.pdf)  
  Keywords: semantic, geometry, ar, understanding, gaussian splatting  
- **[PhyGenHOI: Physically-Aware 4D Generation of Dynamic Human-Object Interactions](https://arxiv.org/abs/2605.30268v1)**  
  Authors: Omer Benishu, Gal Fiebelman, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30268v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://omerbenishu.github.io/PhyGenHOI)  
  Keywords: motion, semantic, dynamic, human, ar, 3d gaussian, 4d  
- **[DGSG-Mind: Dynamic 3D Gaussian Scene Graphs for Long-Term Scene Understanding and Grounding](https://arxiv.org/abs/2605.29879v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Jinyan Liu, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29879v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://icr-lab.github.io/DGSG-Mind)  
  Keywords: semantic, dynamic, segmentation, geometry, mapping, localization, ar, 3d gaussian, understanding  
- **[BitC-3DGS: High-Capacity 3D Gaussian Splatting Watermarking via Bit Compression](https://arxiv.org/abs/2605.29583v1)**  
  Authors: Yuquan Bi, Baosheng Yu, Yingke Lei, Jianwei Yang, Hongsong Wang, Jie Gui, Yuan Yan Tang, James Tin-Yau Kwok  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29583v1.pdf)  
  Keywords: semantic, compression, ar, 3d gaussian, gaussian splatting  
- **[Learning Representations from 3D Gaussian Splats](https://arxiv.org/abs/2605.29549v1)**  
  Authors: Julia Farganus, Krzysztof Żurawicki, Arkadiusz Gaweł, Weronika Jakubowska, Halina Kwaśnicka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29549v1.pdf)  
  Keywords: geometry, ar, 3d gaussian, understanding, gaussian splatting  
- **[Comparative evaluation of photogrammetric reconstruction methods and 3D Gaussian Splatting for road surface roughness analysis](https://arxiv.org/abs/2605.29452v1)**  
  Authors: Marouane Elmegdar, Teng Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.29452v1.pdf)  
  Keywords: face, 3d reconstruction, geometry, segmentation, ar, 3d gaussian, gaussian splatting  
- **[TrackRef3D: Multi-View Consistent Track-then-Label for Open-World Referring Segmentation in 3D Gaussian Splatting](https://arxiv.org/abs/2605.26576v1)**  
  Authors: Yuyang Tan, Renhe Zhang, Hang Zhang, Ao Li, Xin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26576v1.pdf)  
  Keywords: semantic, segmentation, ar, 3d gaussian, gaussian splatting  
- **[Uncertainty-Aware Gaussian Map for Vision-Language Navigation](https://arxiv.org/abs/2605.26503v1)**  
  Authors: Jianzhe Gao, Rui Liu, Yuxuan Xu, Tongtong Cao, Yingxue Zhang, Zhanguang Zhang, Sida Peng, Yi Yang, Wenguan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26503v1.pdf)  
  Keywords: ar, semantic, 3d gaussian  



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