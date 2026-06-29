# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-06-29 02:31:17

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
- [Dynamic Scene](#dynamic-scene) (183 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (46 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (211 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (19 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (190 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (120 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (11 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (53 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (73 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (114 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: medical, 3d reconstruction, 3d gaussian, ar, motion, compact, gaussian splatting, recognition, survey, 4d, autonomous driving, neural rendering, vr  
- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137v1)**  
  Authors: Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00137v1.pdf)  
  Keywords: ar, gaussian splatting, geometry, survey, animation, mapping  
- **[ReefMapGS: Enabling Large-Scale Underwater Reconstruction by Closing the Loop Between Multimodal SLAM and Gaussian Splatting](https://arxiv.org/abs/2604.11992v1)**  
  Authors: Daniel Yang, Jungseok Hong, John J. Leonard, Yogesh Girdhar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11992v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, motion, tracking, gaussian splatting, geometry, survey, 3d reconstruction, slam  
- **[A Survey of Spatial Memory Representations for Efficient Robot Navigation](https://arxiv.org/abs/2604.16482v1)**  
  Authors: Ma. Madecheen S. Pangaliman, Steven S. Sison, Erwin P. Quilloy, Rowel Atienza  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.16482v1.pdf)  
  Keywords: efficient, semantic, ar, survey, slam  

### Acceleration

*Showing the latest 50 out of 83 papers*

- **[Vis4GS: A Visual Analytic Tool for 3D Gaussian Splatting Reconstruction](https://arxiv.org/abs/2606.26985v1)**  
  Authors: Kai-Yuan Lin, Aryabima Mandala Putra, Jui-Chi Lee, Shih-Hsuan Hung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26985v1.pdf)  
  Keywords: understanding, 3d gaussian, real-time rendering, ar, fast, gaussian splatting  
- **[FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation](https://arxiv.org/abs/2606.24876v1)**  
  Authors: Orest Kupyn, Goutam Bhat, Philipp Henzler, Fabian Manhardt, Christian Rupprecht, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24876v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://flat-splat.github.io)  
  Keywords: face, 3d gaussian, real-time rendering, ar, lightweight  
- **[ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos](https://arxiv.org/abs/2606.24628v1)**  
  Authors: Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, Hermann Blum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24628v1.pdf)  
  Keywords: 3d gaussian, human, real-time rendering, ar, motion, tracking, gaussian splatting  
- **[Open-Vocabulary BEV Segmentation with 3D-Aware Geometric Constraints](https://arxiv.org/abs/2606.24353v1)**  
  Authors: Hojun Choi, Seulbin Hwang, Dae Jung Kim, Kisung Kim, Hyunjung Shim, Jinhan Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24353v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hchoi256.github.io/projects/ovbevseg)  
  Keywords: efficient, semantic, ar, fast, gaussian splatting, geometry, segmentation, autonomous driving  
- **[3DCarGen: Scalable 3D Car Generation via 3D-consistent Multi-view Synthesis](https://arxiv.org/abs/2606.24257v1)**  
  Authors: Hongli Xiao, Youjian Zhang, Yaohui Jin, Xiaoguang Ren, Wenjing Yang, Long Lan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24257v1.pdf)  
  Keywords: 3d gaussian, ar, fast, gaussian splatting, autonomous driving  
- **[Deep Learning Approaches for 3D Medical Scene Completion: From Geometric Modeling to Generative Paradigms](https://arxiv.org/abs/2606.24180v1)**  
  Authors: Afifa Khaled, Said Jadid Abdulkadir, Majdy Mohamed Eltayeb Eltahir  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24180v1.pdf)  
  Keywords: medical, 3d gaussian, semantic, real-time rendering, ar, robotics, gaussian splatting  
- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031v1)**  
  Authors: Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23031v1.pdf)  
  Keywords: large scene, efficient, urban scene, 3d gaussian, ar, fast, high-fidelity, dynamic, gaussian splatting, geometry  
- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091v1)**  
  Authors: Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22091v1.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, fast, robotics, high-fidelity, lightweight, gaussian splatting, geometry, head, slam, mapping  
- **[ACE-GS: Acing the Trade-off with Accurate, Compact and Efficient 3D Gaussian Splatting](https://arxiv.org/abs/2606.21244v1)**  
  Authors: Jijian Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21244v1.pdf)  
  Keywords: efficient, 3d gaussian, real-time rendering, ar, fast, high-fidelity, compact, gaussian splatting, acceleration  
- **[Hand-4DGS: Feed-Forward 3D Gaussian Splatting for 4D Hand Reconstruction from Egocentric Videos](https://arxiv.org/abs/2606.19156v1)**  
  Authors: Jeongmin Bae, Seoha Kim, Marc Pollefeys, Mahdi Rad, Youngjung Uh, Taein Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.19156v1.pdf)  
  Keywords: 3d gaussian, human, ar, fast, dynamic, motion, gaussian splatting, body, 4d, head, vr  

### Applications

*Showing the latest 50 out of 498 papers*

- **[StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views](https://arxiv.org/abs/2606.28321v1)**  
  Authors: Jia-Chen Zhao, Beiqi Chen, Xinyang Chen, Guangcong Wang, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.28321v1.pdf) | [![GitHub](https://img.shields.io/github/stars/J-C-Zhao/StructSplat?style=social)](https://github.com/J-C-Zhao/StructSplat) | [![Project](https://img.shields.io/badge/-Project-blue)](https://structsplat.github.io)  
  Keywords: sparse view, 3d gaussian, semantic, ar, gaussian splatting, geometry  
- **[CoIn: Comprehensive 2D-3D Inpainting with Gaussian Splatting Guidance](https://arxiv.org/abs/2606.27584v1)**  
  Authors: Hana Kim, Minje Kim, Tae-Kyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27584v1.pdf)  
  Keywords: gaussian splatting, efficient, ar, segmentation  
- **[Structured-Li-GS: Structured 3D Gaussians Splatting with LiDAR Incorporation and Spatial Constraints](https://arxiv.org/abs/2606.27509v1)**  
  Authors: Huaiyuan Weng, Huibin Li, Chul Min Yeum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27509v1.pdf)  
  Keywords: face, 3d gaussian, ar, high-fidelity, lightweight, gaussian splatting, geometry, 3d reconstruction, slam  
- **[SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223v1)**  
  Authors: Jiyong Kim, Shuang Song, Ronjgun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/SatSplatDiff?style=social)](https://github.com/GDAOSU/SatSplatDiff)  
  Keywords: shadow, face, ar, high-fidelity, gaussian splatting, geometry, 3d reconstruction  
- **[PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views](https://arxiv.org/abs/2606.27071v1)**  
  Authors: Zhisong Xu, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27071v1.pdf)  
  Keywords: ar, motion, geometry, 3d reconstruction, slam  
- **[Vis4GS: A Visual Analytic Tool for 3D Gaussian Splatting Reconstruction](https://arxiv.org/abs/2606.26985v1)**  
  Authors: Kai-Yuan Lin, Aryabima Mandala Putra, Jui-Chi Lee, Shih-Hsuan Hung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26985v1.pdf)  
  Keywords: understanding, 3d gaussian, real-time rendering, ar, fast, gaussian splatting  
- **[Capacity-Controlled Multi-View Stylization of 3D Gaussian Splatting](https://arxiv.org/abs/2606.26754v1)**  
  Authors: Zhihao Wen, Yixin Yang, Bojian Wu, Yang Zhou, Dani Lischinski, Daniel Cohen-Or, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26754v1.pdf)  
  Keywords: efficient, 3d gaussian, semantic, ar, gaussian splatting  
- **[Rendering Novel Views of MRI Using 3D Gaussian Splatting](https://arxiv.org/abs/2606.26236v1)**  
  Authors: Robin Y. Park, Mark C. Eid, Rhydian Windsor, Amir Jamaludin, Ana I. L. Namburete, João F. Henriques, Andrew Zisserman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26236v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian  
- **[TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy](https://arxiv.org/abs/2606.26092v1)**  
  Authors: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26092v1.pdf)  
  Keywords: localization, human, ar, avatar, dynamic, motion, high-fidelity, deformation, 4d  
- **[From Sparse and Imperfect 2D Anchors to Consistent 3D Gaussian Street Scenes: Support-Aware Appearance](https://arxiv.org/abs/2606.26007v1)**  
  Authors: Long Cao, Zhongquan Wang, Jie Li, Yuhan Chen, Kefei Qian, Xiangfei Huang, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26007v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Cagares/Baking-for-3D-Gaussian?style=social)](https://github.com/Cagares/Baking-for-3D-Gaussian)  
  Keywords: efficient, geometry, ar, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 172 papers*

- **[Structured-Li-GS: Structured 3D Gaussians Splatting with LiDAR Incorporation and Spatial Constraints](https://arxiv.org/abs/2606.27509v1)**  
  Authors: Huaiyuan Weng, Huibin Li, Chul Min Yeum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27509v1.pdf)  
  Keywords: face, 3d gaussian, ar, high-fidelity, lightweight, gaussian splatting, geometry, 3d reconstruction, slam  
- **[SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223v1)**  
  Authors: Jiyong Kim, Shuang Song, Ronjgun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/SatSplatDiff?style=social)](https://github.com/GDAOSU/SatSplatDiff)  
  Keywords: shadow, face, ar, high-fidelity, gaussian splatting, geometry, 3d reconstruction  
- **[TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy](https://arxiv.org/abs/2606.26092v1)**  
  Authors: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26092v1.pdf)  
  Keywords: localization, human, ar, avatar, dynamic, motion, high-fidelity, deformation, 4d  
- **[FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation](https://arxiv.org/abs/2606.24876v1)**  
  Authors: Orest Kupyn, Goutam Bhat, Philipp Henzler, Fabian Manhardt, Christian Rupprecht, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24876v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://flat-splat.github.io)  
  Keywords: face, 3d gaussian, real-time rendering, ar, lightweight  
- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)**  
  Authors: Leshu Li, Jie Peng, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/UMN-ZhaoLab/Pocket-SLAM.git?style=social)](https://github.com/UMN-ZhaoLab/Pocket-SLAM.git)  
  Keywords: efficient, face, 3d gaussian, localization, ar, gaussian splatting, geometry, autonomous driving, slam, outdoor, mapping  
- **[ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos](https://arxiv.org/abs/2606.24628v1)**  
  Authors: Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, Hermann Blum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24628v1.pdf)  
  Keywords: 3d gaussian, human, real-time rendering, ar, motion, tracking, gaussian splatting  
- **[FiCA: Feed-forward instant Gaussian Codec Avatars from a Single Portrait Image](https://arxiv.org/abs/2606.24232v1)**  
  Authors: Kim Youwang, Zhengyu Yang, Liuhao Ge, Yu Rong, Timur Bagautdinov, Su Zhaoen, Nir Sopher, Jovan Popović, Teng Deng, Tae-Hyun Oh, Chen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24232v1.pdf)  
  Keywords: 3d gaussian, human, ar, avatar, geometry, head, mapping  
- **[Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild](https://arxiv.org/abs/2606.23688v1)**  
  Authors: Yehonathan Litman, Xiaoxuan Ma, Manan Shah, Nicolas Ugrinovic, Kris Kitani, Fernando De la Torre, Shubham Tulsiani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23688v1.pdf)  
  Keywords: face, 3d gaussian, ar, dynamic, motion, gaussian splatting, geometry, deformation, 4d, 3d reconstruction  
- **[Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation](https://arxiv.org/abs/2606.22197v1)**  
  Authors: Rui Wang, Quentin Lohmeyer, Siyu Tang, Mirko Meboldt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22197v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://batfacewayne.github.io/Multi4D.io)  
  Keywords: face, 3d gaussian, semantic, ar, dynamic, high-fidelity, gaussian splatting, motion, geometry, deformation, compact, 4d, segmentation, head  
- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091v1)**  
  Authors: Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22091v1.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, fast, robotics, high-fidelity, lightweight, gaussian splatting, geometry, head, slam, mapping  

### Dynamic Scene

*Showing the latest 50 out of 183 papers*

- **[PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views](https://arxiv.org/abs/2606.27071v1)**  
  Authors: Zhisong Xu, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27071v1.pdf)  
  Keywords: ar, motion, geometry, 3d reconstruction, slam  
- **[TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy](https://arxiv.org/abs/2606.26092v1)**  
  Authors: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26092v1.pdf)  
  Keywords: localization, human, ar, avatar, dynamic, motion, high-fidelity, deformation, 4d  
- **[OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis](https://arxiv.org/abs/2606.24799v1)**  
  Authors: Chenrui Fan, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24799v1.pdf)  
  Keywords: high quality, 3d gaussian, ar, motion, gaussian splatting, 3d reconstruction  
- **[ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos](https://arxiv.org/abs/2606.24628v1)**  
  Authors: Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, Hermann Blum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24628v1.pdf)  
  Keywords: 3d gaussian, human, real-time rendering, ar, motion, tracking, gaussian splatting  
- **[SignNet-1M: Large-Scale Multilingual Sign Language Video Dataset with Downstream Benchmarks](https://arxiv.org/abs/2606.24361v1)**  
  Authors: Zhewen He, Junyi Hu, Haomian Huang, Zhenhua Li, Yu-Shen Liu, Yi Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24361v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://signnet.chatsign.ai)  
  Keywords: 3d gaussian, ar, compression, recognition, motion, gaussian splatting  
- **[Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild](https://arxiv.org/abs/2606.23688v1)**  
  Authors: Yehonathan Litman, Xiaoxuan Ma, Manan Shah, Nicolas Ugrinovic, Kris Kitani, Fernando De la Torre, Shubham Tulsiani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23688v1.pdf)  
  Keywords: face, 3d gaussian, ar, dynamic, motion, gaussian splatting, geometry, deformation, 4d, 3d reconstruction  
- **[MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing](https://arxiv.org/abs/2606.23455v1)**  
  Authors: Zesong Yang, Yuanhang Lei, Liyuan Cui, Yihang Chen, Jiaer Huang, Boming Zhao, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23455v1.pdf)  
  Keywords: 3d gaussian, ar, dynamic, high-fidelity, gaussian splatting, deformation, animation, neural rendering  
- **[Temporally Aware Densification for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2606.23212v1)**  
  Authors: Vikram Sandu, Mayurdeep Pathak, Rajiv Soundararajan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23212v1.pdf)  
  Keywords: 3d gaussian, ar, motion, dynamic, gaussian splatting, deformation  
- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031v1)**  
  Authors: Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23031v1.pdf)  
  Keywords: large scene, efficient, urban scene, 3d gaussian, ar, fast, high-fidelity, dynamic, gaussian splatting, geometry  
- **[Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography](https://arxiv.org/abs/2606.22525v1)**  
  Authors: Yikuang Yuluo, Ao Wang, Shen Kuan, Yujie Liu, Wang Liao, Ying Chen, Shuangyang Zhong, Yixing Huang, Fuquan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22525v1.pdf)  
  Keywords: sparse-view, efficient, 3d gaussian, ar, gaussian splatting, geometry, deformation  

### Few-shot

- **[StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views](https://arxiv.org/abs/2606.28321v1)**  
  Authors: Jia-Chen Zhao, Beiqi Chen, Xinyang Chen, Guangcong Wang, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.28321v1.pdf) | [![GitHub](https://img.shields.io/github/stars/J-C-Zhao/StructSplat?style=social)](https://github.com/J-C-Zhao/StructSplat) | [![Project](https://img.shields.io/badge/-Project-blue)](https://structsplat.github.io)  
  Keywords: sparse view, 3d gaussian, semantic, ar, gaussian splatting, geometry  
- **[Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography](https://arxiv.org/abs/2606.22525v1)**  
  Authors: Yikuang Yuluo, Ao Wang, Shen Kuan, Yujie Liu, Wang Liao, Ying Chen, Shuangyang Zhong, Yixing Huang, Fuquan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22525v1.pdf)  
  Keywords: sparse-view, efficient, 3d gaussian, ar, gaussian splatting, geometry, deformation  
- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091v1)**  
  Authors: Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22091v1.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, fast, robotics, high-fidelity, lightweight, gaussian splatting, geometry, head, slam, mapping  
- **[From Uncertainty to Stability and Fidelity: Guiding Sparse-View 3D Gaussian Splatting with Fisher Information](https://arxiv.org/abs/2606.20842v1)**  
  Authors: Junbao Zhou, Qingshan Xu, Yuan Zhou, Xiaolong Shen, Beier Zhu, Kesen Zhao, Yiming Zeng, Chen Bai, Cheng Lu, Hanwang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.20842v1.pdf)  
  Keywords: gaussian splatting, sparse-view, ar, 3d gaussian  
- **[VisDom: Sparse Novel View Synthesis with Visible Domain Constraint](https://arxiv.org/abs/2606.20531v1)**  
  Authors: Mariia Gladkova*, Tarun Yenamandra*, Edmond Boyer, Robert Maier, Tony Tung, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.20531v1.pdf)  
  Keywords: sparse-view, ar, nerf, gaussian splatting, geometry  
- **[FlowObject: Flow Steering for Bridging Generative Priors and Reconstruction Fidelity](https://arxiv.org/abs/2606.19019v1)**  
  Authors: Yuchen Rao, Xuqian Ren, Yinyu Nie, Sayan Deb Sarkar, Biao Zhang, Vincent Lepetit, Friedrich Fraundorfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.19019v1.pdf)  
  Keywords: sparse-view, face, 3d gaussian, ar, gaussian splatting, geometry, 3d reconstruction  
- **[KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis](https://arxiv.org/abs/2606.03120v1)**  
  Authors: Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.03120v1.pdf)  
  Keywords: sparse-view, efficient, 3d gaussian, ar, high-fidelity, nerf, gaussian splatting, outdoor  
- **[BEAST3D: Animal behavioral analysis and neural encoding from multi-view video via Gaussian splatting](https://arxiv.org/abs/2606.02937v1)**  
  Authors: Yanchen Wang, Lenny Aharon, Wangshu Zhu, Kyle Daruwalla, Linghua Zhang, Jiaru Zou, Selmaan Chettih, Helen Hou, Liam Paninski, Matthew R Whiteway  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.02937v1.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, gaussian splatting, geometry, 3d reconstruction  
- **[Fast and Lightweight Novel View Synthesis with Differentiable Multiplane Image](https://arxiv.org/abs/2606.02068v1)**  
  Authors: Kaidi Zhang, Guanxu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.02068v1.pdf)  
  Keywords: sparse-view, efficient, 3d gaussian, ar, fast, lightweight, nerf, gaussian splatting, compact  
- **[DeblurNVS: Geometric Latent Diffusion for Novel View Synthesis from Sparse Motion-Blurred Images](https://arxiv.org/abs/2606.01315v1)**  
  Authors: Changyue Shi, Wangbo Yu, Chaoran Feng, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.01315v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PKU-YuanGroup/DeblurNVS?style=social)](https://github.com/PKU-YuanGroup/DeblurNVS)  
  Keywords: sparse-view, efficient, 3d gaussian, ar, motion, nerf, gaussian splatting, high-fidelity  

### Geometry Reconstruction

*Showing the latest 50 out of 211 papers*

- **[StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views](https://arxiv.org/abs/2606.28321v1)**  
  Authors: Jia-Chen Zhao, Beiqi Chen, Xinyang Chen, Guangcong Wang, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.28321v1.pdf) | [![GitHub](https://img.shields.io/github/stars/J-C-Zhao/StructSplat?style=social)](https://github.com/J-C-Zhao/StructSplat) | [![Project](https://img.shields.io/badge/-Project-blue)](https://structsplat.github.io)  
  Keywords: sparse view, 3d gaussian, semantic, ar, gaussian splatting, geometry  
- **[Structured-Li-GS: Structured 3D Gaussians Splatting with LiDAR Incorporation and Spatial Constraints](https://arxiv.org/abs/2606.27509v1)**  
  Authors: Huaiyuan Weng, Huibin Li, Chul Min Yeum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27509v1.pdf)  
  Keywords: face, 3d gaussian, ar, high-fidelity, lightweight, gaussian splatting, geometry, 3d reconstruction, slam  
- **[SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223v1)**  
  Authors: Jiyong Kim, Shuang Song, Ronjgun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/SatSplatDiff?style=social)](https://github.com/GDAOSU/SatSplatDiff)  
  Keywords: shadow, face, ar, high-fidelity, gaussian splatting, geometry, 3d reconstruction  
- **[PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views](https://arxiv.org/abs/2606.27071v1)**  
  Authors: Zhisong Xu, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27071v1.pdf)  
  Keywords: ar, motion, geometry, 3d reconstruction, slam  
- **[From Sparse and Imperfect 2D Anchors to Consistent 3D Gaussian Street Scenes: Support-Aware Appearance](https://arxiv.org/abs/2606.26007v1)**  
  Authors: Long Cao, Zhongquan Wang, Jie Li, Yuhan Chen, Kefei Qian, Xiangfei Huang, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26007v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Cagares/Baking-for-3D-Gaussian?style=social)](https://github.com/Cagares/Baking-for-3D-Gaussian)  
  Keywords: efficient, geometry, ar, 3d gaussian  
- **[FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation](https://arxiv.org/abs/2606.24874v1)**  
  Authors: Haorui Ji, Weizhe Liu, Hongdong Li, Hengkai Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24874v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, high-fidelity, gaussian splatting, geometry  
- **[OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis](https://arxiv.org/abs/2606.24799v1)**  
  Authors: Chenrui Fan, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24799v1.pdf)  
  Keywords: high quality, 3d gaussian, ar, motion, gaussian splatting, 3d reconstruction  
- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)**  
  Authors: Leshu Li, Jie Peng, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/UMN-ZhaoLab/Pocket-SLAM.git?style=social)](https://github.com/UMN-ZhaoLab/Pocket-SLAM.git)  
  Keywords: efficient, face, 3d gaussian, localization, ar, gaussian splatting, geometry, autonomous driving, slam, outdoor, mapping  
- **[Open-Vocabulary BEV Segmentation with 3D-Aware Geometric Constraints](https://arxiv.org/abs/2606.24353v1)**  
  Authors: Hojun Choi, Seulbin Hwang, Dae Jung Kim, Kisung Kim, Hyunjung Shim, Jinhan Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24353v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hchoi256.github.io/projects/ovbevseg)  
  Keywords: efficient, semantic, ar, fast, gaussian splatting, geometry, segmentation, autonomous driving  
- **[MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301v1)**  
  Authors: Hongli Xiao, Youjian Zhang, Yucai Bai, Chaoyue Wang, Yaohui Jin, Xiaoguang Ren, Wenjing Yang, Long Lan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24301v1.pdf) | [![GitHub](https://img.shields.io/github/stars/HongliXiao/MM-TRELLIS?style=social)](https://github.com/HongliXiao/MM-TRELLIS)  
  Keywords: 3d gaussian, ar, high-fidelity, gaussian splatting, geometry, autonomous driving, neural rendering  

### Large Scene

- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)**  
  Authors: Leshu Li, Jie Peng, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/UMN-ZhaoLab/Pocket-SLAM.git?style=social)](https://github.com/UMN-ZhaoLab/Pocket-SLAM.git)  
  Keywords: efficient, face, 3d gaussian, localization, ar, gaussian splatting, geometry, autonomous driving, slam, outdoor, mapping  
- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031v1)**  
  Authors: Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23031v1.pdf)  
  Keywords: large scene, efficient, urban scene, 3d gaussian, ar, fast, high-fidelity, dynamic, gaussian splatting, geometry  
- **[Point-Cloud-Assistant Localized Statistical Channel Prediction by Tangent Gaussian Splatting](https://arxiv.org/abs/2606.18734v1)**  
  Authors: Ye Xue, Yiheng Wang, Xinhua Shao, Qi Yan, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.18734v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, fast, gaussian splatting, geometry, outdoor  
- **[MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization](https://arxiv.org/abs/2606.17935v1)**  
  Authors: Guo Pu, Yixuan Han, Haofeng Li, Yao Zhang, Hui Zhou, Zhouhui Lian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17935v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TrickyGo/MoonSplat?style=social)](https://github.com/TrickyGo/MoonSplat)  
  Keywords: efficient, 3d gaussian, real-time rendering, ar, robotics, tracking, gaussian splatting, 3d reconstruction, outdoor, vr  
- **[KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis](https://arxiv.org/abs/2606.03120v1)**  
  Authors: Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.03120v1.pdf)  
  Keywords: sparse-view, efficient, 3d gaussian, ar, high-fidelity, nerf, gaussian splatting, outdoor  
- **[City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.30310v1)**  
  Authors: Sayan Paul, Sourav Ghosh, Siddharth Katageri, Soumyadip Maity, Sanjana Sinha, Brojeshwar Bhowmick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30310v1.pdf)  
  Keywords: large scene, urban scene, face, ar, high-fidelity, nerf, gaussian splatting, geometry, 3d reconstruction  
- **[GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction](https://arxiv.org/abs/2605.23888v1)**  
  Authors: Katharina Schmid, Nicolas von Lützow, Jozef Hladký, Angela Dai, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.23888v1.pdf)  
  Keywords: large scene, geometry, ar, high-fidelity  
- **[Diffusion-guided Generalizable Enhancer for Urban Scene Reconstruction](https://arxiv.org/abs/2605.22420v1)**  
  Authors: Henry Che, Jingkang Wang, Yun Chen, Ze Yang, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.22420v1.pdf)  
  Keywords: efficient, urban scene, 3d gaussian, ar, high-fidelity, autonomous driving, neural rendering  
- **[Feed-Forward Gaussian Splatting from Sparse Aerial Views](https://arxiv.org/abs/2605.19949v1)**  
  Authors: Dongli Wu, Zhuoxiao Li, Tongyan Hua, Yinrui Ren, Xiaobao Wei, Rongjun Qin, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.19949v1.pdf)  
  Keywords: urban scene, 3d gaussian, ar, gaussian splatting, geometry  
- **[Cross-View Splatter: Feed-Forward View Synthesis with Georeferenced Images](https://arxiv.org/abs/2605.19656v1)**  
  Authors: Matias Turkulainen, Akshay Krishnan, Filippo Aleotti, Mohamed Sayed, Guillermo Garcia-Hernando, Juho Kannala, Arno Solin, Gabriel Brostow, Daniyar Turmukhambetov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.19656v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nianticspatial.github.io/cross-view-splatter)  
  Keywords: mapping, ar, outdoor  

### Model Compression

*Showing the latest 50 out of 190 papers*

- **[CoIn: Comprehensive 2D-3D Inpainting with Gaussian Splatting Guidance](https://arxiv.org/abs/2606.27584v1)**  
  Authors: Hana Kim, Minje Kim, Tae-Kyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27584v1.pdf)  
  Keywords: gaussian splatting, efficient, ar, segmentation  
- **[Structured-Li-GS: Structured 3D Gaussians Splatting with LiDAR Incorporation and Spatial Constraints](https://arxiv.org/abs/2606.27509v1)**  
  Authors: Huaiyuan Weng, Huibin Li, Chul Min Yeum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27509v1.pdf)  
  Keywords: face, 3d gaussian, ar, high-fidelity, lightweight, gaussian splatting, geometry, 3d reconstruction, slam  
- **[Capacity-Controlled Multi-View Stylization of 3D Gaussian Splatting](https://arxiv.org/abs/2606.26754v1)**  
  Authors: Zhihao Wen, Yixin Yang, Bojian Wu, Yang Zhou, Dani Lischinski, Daniel Cohen-Or, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26754v1.pdf)  
  Keywords: efficient, 3d gaussian, semantic, ar, gaussian splatting  
- **[From Sparse and Imperfect 2D Anchors to Consistent 3D Gaussian Street Scenes: Support-Aware Appearance](https://arxiv.org/abs/2606.26007v1)**  
  Authors: Long Cao, Zhongquan Wang, Jie Li, Yuhan Chen, Kefei Qian, Xiangfei Huang, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26007v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Cagares/Baking-for-3D-Gaussian?style=social)](https://github.com/Cagares/Baking-for-3D-Gaussian)  
  Keywords: efficient, geometry, ar, 3d gaussian  
- **[FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation](https://arxiv.org/abs/2606.24876v1)**  
  Authors: Orest Kupyn, Goutam Bhat, Philipp Henzler, Fabian Manhardt, Christian Rupprecht, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24876v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://flat-splat.github.io)  
  Keywords: face, 3d gaussian, real-time rendering, ar, lightweight  
- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)**  
  Authors: Leshu Li, Jie Peng, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/UMN-ZhaoLab/Pocket-SLAM.git?style=social)](https://github.com/UMN-ZhaoLab/Pocket-SLAM.git)  
  Keywords: efficient, face, 3d gaussian, localization, ar, gaussian splatting, geometry, autonomous driving, slam, outdoor, mapping  
- **[SignNet-1M: Large-Scale Multilingual Sign Language Video Dataset with Downstream Benchmarks](https://arxiv.org/abs/2606.24361v1)**  
  Authors: Zhewen He, Junyi Hu, Haomian Huang, Zhenhua Li, Yu-Shen Liu, Yi Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24361v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://signnet.chatsign.ai)  
  Keywords: 3d gaussian, ar, compression, recognition, motion, gaussian splatting  
- **[Open-Vocabulary BEV Segmentation with 3D-Aware Geometric Constraints](https://arxiv.org/abs/2606.24353v1)**  
  Authors: Hojun Choi, Seulbin Hwang, Dae Jung Kim, Kisung Kim, Hyunjung Shim, Jinhan Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24353v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hchoi256.github.io/projects/ovbevseg)  
  Keywords: efficient, semantic, ar, fast, gaussian splatting, geometry, segmentation, autonomous driving  
- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031v1)**  
  Authors: Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23031v1.pdf)  
  Keywords: large scene, efficient, urban scene, 3d gaussian, ar, fast, high-fidelity, dynamic, gaussian splatting, geometry  
- **[Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography](https://arxiv.org/abs/2606.22525v1)**  
  Authors: Yikuang Yuluo, Ao Wang, Shen Kuan, Yujie Liu, Wang Liao, Ying Chen, Shuangyang Zhong, Yixing Huang, Fuquan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22525v1.pdf)  
  Keywords: sparse-view, efficient, 3d gaussian, ar, gaussian splatting, geometry, deformation  

### Quality Enhancement

*Showing the latest 50 out of 120 papers*

- **[Structured-Li-GS: Structured 3D Gaussians Splatting with LiDAR Incorporation and Spatial Constraints](https://arxiv.org/abs/2606.27509v1)**  
  Authors: Huaiyuan Weng, Huibin Li, Chul Min Yeum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27509v1.pdf)  
  Keywords: face, 3d gaussian, ar, high-fidelity, lightweight, gaussian splatting, geometry, 3d reconstruction, slam  
- **[SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223v1)**  
  Authors: Jiyong Kim, Shuang Song, Ronjgun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/SatSplatDiff?style=social)](https://github.com/GDAOSU/SatSplatDiff)  
  Keywords: shadow, face, ar, high-fidelity, gaussian splatting, geometry, 3d reconstruction  
- **[TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy](https://arxiv.org/abs/2606.26092v1)**  
  Authors: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26092v1.pdf)  
  Keywords: localization, human, ar, avatar, dynamic, motion, high-fidelity, deformation, 4d  
- **[FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation](https://arxiv.org/abs/2606.24874v1)**  
  Authors: Haorui Ji, Weizhe Liu, Hongdong Li, Hengkai Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24874v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, high-fidelity, gaussian splatting, geometry  
- **[OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis](https://arxiv.org/abs/2606.24799v1)**  
  Authors: Chenrui Fan, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24799v1.pdf)  
  Keywords: high quality, 3d gaussian, ar, motion, gaussian splatting, 3d reconstruction  
- **[MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301v1)**  
  Authors: Hongli Xiao, Youjian Zhang, Yucai Bai, Chaoyue Wang, Yaohui Jin, Xiaoguang Ren, Wenjing Yang, Long Lan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24301v1.pdf) | [![GitHub](https://img.shields.io/github/stars/HongliXiao/MM-TRELLIS?style=social)](https://github.com/HongliXiao/MM-TRELLIS)  
  Keywords: 3d gaussian, ar, high-fidelity, gaussian splatting, geometry, autonomous driving, neural rendering  
- **[MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing](https://arxiv.org/abs/2606.23455v1)**  
  Authors: Zesong Yang, Yuanhang Lei, Liyuan Cui, Yihang Chen, Jiaer Huang, Boming Zhao, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23455v1.pdf)  
  Keywords: 3d gaussian, ar, dynamic, high-fidelity, gaussian splatting, deformation, animation, neural rendering  
- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031v1)**  
  Authors: Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23031v1.pdf)  
  Keywords: large scene, efficient, urban scene, 3d gaussian, ar, fast, high-fidelity, dynamic, gaussian splatting, geometry  
- **[Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation](https://arxiv.org/abs/2606.22197v1)**  
  Authors: Rui Wang, Quentin Lohmeyer, Siyu Tang, Mirko Meboldt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22197v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://batfacewayne.github.io/Multi4D.io)  
  Keywords: face, 3d gaussian, semantic, ar, dynamic, high-fidelity, gaussian splatting, motion, geometry, deformation, compact, 4d, segmentation, head  
- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091v1)**  
  Authors: Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22091v1.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, fast, robotics, high-fidelity, lightweight, gaussian splatting, geometry, head, slam, mapping  

### Ray Tracing

- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, gaussian splatting, global illumination, illumination, geometry, 3d reconstruction  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, global illumination, illumination  
- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314v1)**  
  Authors: Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11314v1.pdf)  
  Keywords: relighting, 3d reconstruction, 3d gaussian, ar, light transport, dynamic, motion, lightweight, geometry, lighting, neural rendering, ray tracing  
- **[Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606v1)**  
  Authors: Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09606v1.pdf)  
  Keywords: shadow, relighting, path tracing, 3d gaussian, ar, light transport, compact, global illumination, illumination, lighting, ray tracing, reflection  
- **[RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation](https://arxiv.org/abs/2606.01261v1)**  
  Authors: Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.01261v1.pdf)  
  Keywords: efficient, 3d gaussian, semantic, ar, gaussian splatting, geometry, segmentation, ray tracing, reflection  
- **[Directed Distance Fields for Constant-Time Ray Queries on Gaussian Splatting](https://arxiv.org/abs/2606.00817v1)**  
  Authors: Subhankar MIshra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00817v1.pdf) | [![GitHub](https://img.shields.io/github/stars/smlab-niser/ddf-gs?style=social)](https://github.com/smlab-niser/ddf-gs)  
  Keywords: shadow, face, 3d gaussian, ar, fast, gaussian splatting, global illumination, illumination  
- **[Underwater360: Reconstructing Underwater Scenes from Panoramic Images with Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2605.26447v1)**  
  Authors: Jiangbei Hu, Weichao Song, Shibo Yu, Mohan Wang, Zihan Yi, Rui Wu, Mingkang Xiang, Na Lei, Shengfa Wang, Zhongxuan Luo, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26447v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SwcK423/Underwater360?style=social)](https://github.com/SwcK423/Underwater360)  
  Keywords: gaussian splatting, ar, ray casting, 3d gaussian  
- **[Differentiable Ray Tracing with Gaussians for Unified Radio Propagation Simulation and View Synthesis](https://arxiv.org/abs/2605.07781v1)**  
  Authors: Niklas Vaara, Lam Huynh, Pekka Sangi, Miguel Bordallo López, Janne Heikkilä  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.07781v1.pdf)  
  Keywords: 3d gaussian, ar, high-fidelity, gaussian splatting, geometry, ray tracing  
- **[Power Foam: Unifying Real-Time Differentiable Ray Tracing and Rasterization](https://arxiv.org/abs/2604.24994v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Dor Verbin, Kwang Moo Yi, Anish Prabhu, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24994v1.pdf)  
  Keywords: efficient, face, ar, geometry, ray tracing  
- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138v1)**  
  Authors: Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/viserdex)  
  Keywords: efficient, 3d gaussian, semantic, ar, robotics, dynamic, tracking, gaussian splatting, lighting, ray tracing  

### Relighting

*Showing the latest 50 out of 53 papers*

- **[SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223v1)**  
  Authors: Jiyong Kim, Shuang Song, Ronjgun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/SatSplatDiff?style=social)](https://github.com/GDAOSU/SatSplatDiff)  
  Keywords: shadow, face, ar, high-fidelity, gaussian splatting, geometry, 3d reconstruction  
- **[Lighting-Consistent Object Transfer Across Radiance Fields](https://arxiv.org/abs/2606.22481v1)**  
  Authors: Nicolás Violante, George Kopanas, Linus Franke, Julien Philip, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22481v1.pdf)  
  Keywords: gaussian splatting, ar, lighting, 3d gaussian  
- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, gaussian splatting, global illumination, illumination, geometry, 3d reconstruction  
- **[LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping](https://arxiv.org/abs/2606.20424v1)**  
  Authors: Shikuan Shi, Chunran Zheng, Jiaming Xu, Tianyong Ye, Tao Yu, Yukang Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.20424v1.pdf)  
  Keywords: face, ar, gaussian splatting, illumination, geometry, lighting, neural rendering, mapping  
- **[AIGS-Net: Compact Illumination Field Modeling via 2D Gaussian Splatting for Fast Low-Light Image Enhancement](https://arxiv.org/abs/2606.17998v1)**  
  Authors: Yuhan Chen, Kunyang Huang, Fuchen Li, Zhuohan Qin, Guofa Li, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17998v1.pdf)  
  Keywords: efficient, face, ar, fast, dynamic, compact, gaussian splatting, illumination, lightweight, mapping  
- **[Gaussian Light Field Splatting: A Physical Prior-Driven Vision Transformer for Unsupervised Low-Light Image Enhancement](https://arxiv.org/abs/2606.17985v1)**  
  Authors: Yuhan Chen, Wenxuan Yu, Guofa Li, Fuchen Li, Kunyang Huang, Yicui Shi, Ying Fang, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17985v1.pdf)  
  Keywords: gaussian splatting, illumination, ar  
- **[RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos](https://arxiv.org/abs/2606.16278v1)**  
  Authors: Zhenhua Wu, Yun Pang, Mingkun Chang, Yuwei Ning, Liangzhi Wang, Yi Xiao, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16278v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, lightweight, gaussian splatting, illumination, autonomous driving  
- **[Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation](https://arxiv.org/abs/2606.16163v1)**  
  Authors: Yuhan Chen, Wenxuan Yu, Guofa Li, Kunyang Huang, Ying Fang, Yicui Shi, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16163v1.pdf)  
  Keywords: efficient, ar, dynamic, gaussian splatting, lighting  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, global illumination, illumination  
- **[Wild3R: Feed-Forward 3D Gaussian Splatting from Unconstrained Sparse Photo Collection](https://arxiv.org/abs/2606.11894v2)**  
  Authors: Yuto Furutani, Takashi Otonari, Kaede Shiohara, Toshihiko Yamasaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11894v2.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, illumination, lighting  

### SLAM

*Showing the latest 50 out of 73 papers*

- **[Structured-Li-GS: Structured 3D Gaussians Splatting with LiDAR Incorporation and Spatial Constraints](https://arxiv.org/abs/2606.27509v1)**  
  Authors: Huaiyuan Weng, Huibin Li, Chul Min Yeum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27509v1.pdf)  
  Keywords: face, 3d gaussian, ar, high-fidelity, lightweight, gaussian splatting, geometry, 3d reconstruction, slam  
- **[PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views](https://arxiv.org/abs/2606.27071v1)**  
  Authors: Zhisong Xu, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27071v1.pdf)  
  Keywords: ar, motion, geometry, 3d reconstruction, slam  
- **[TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy](https://arxiv.org/abs/2606.26092v1)**  
  Authors: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26092v1.pdf)  
  Keywords: localization, human, ar, avatar, dynamic, motion, high-fidelity, deformation, 4d  
- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)**  
  Authors: Leshu Li, Jie Peng, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/UMN-ZhaoLab/Pocket-SLAM.git?style=social)](https://github.com/UMN-ZhaoLab/Pocket-SLAM.git)  
  Keywords: efficient, face, 3d gaussian, localization, ar, gaussian splatting, geometry, autonomous driving, slam, outdoor, mapping  
- **[ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos](https://arxiv.org/abs/2606.24628v1)**  
  Authors: Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, Hermann Blum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24628v1.pdf)  
  Keywords: 3d gaussian, human, real-time rendering, ar, motion, tracking, gaussian splatting  
- **[FiCA: Feed-forward instant Gaussian Codec Avatars from a Single Portrait Image](https://arxiv.org/abs/2606.24232v1)**  
  Authors: Kim Youwang, Zhengyu Yang, Liuhao Ge, Yu Rong, Timur Bagautdinov, Su Zhaoen, Nir Sopher, Jovan Popović, Teng Deng, Tae-Hyun Oh, Chen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24232v1.pdf)  
  Keywords: 3d gaussian, human, ar, avatar, geometry, head, mapping  
- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091v1)**  
  Authors: Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22091v1.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, fast, robotics, high-fidelity, lightweight, gaussian splatting, geometry, head, slam, mapping  
- **[Spectral GS-SLAM: Observability-Aware, Degeneracy-Robust Tracking for Real-Time 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2606.21258v1)**  
  Authors: Edward Beng Wai Tan, Siew-Kei Lam, Dongshuo Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21258v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, tracking, gaussian splatting, geometry, slam, mapping  
- **[LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping](https://arxiv.org/abs/2606.20424v1)**  
  Authors: Shikuan Shi, Chunran Zheng, Jiaming Xu, Tianyong Ye, Tao Yu, Yukang Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.20424v1.pdf)  
  Keywords: face, ar, gaussian splatting, illumination, geometry, lighting, neural rendering, mapping  
- **[MMD-SLAM: Structure-Enhanced Multi-Meta Gaussian Distribution-Guided Visual SLAM](https://arxiv.org/abs/2606.19874v1)**  
  Authors: Fan Zhu, Ziyu Chen, Peichen Liu, Yifan Zhao, Zhisong Xu, Hui Zhu, Hongxing Zhou, Sixun Liu, Chunmao Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.19874v1.pdf)  
  Keywords: 3d gaussian, localization, ar, high-fidelity, tracking, gaussian splatting, geometry, slam, mapping  

### Scene Understanding

*Showing the latest 50 out of 114 papers*

- **[StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views](https://arxiv.org/abs/2606.28321v1)**  
  Authors: Jia-Chen Zhao, Beiqi Chen, Xinyang Chen, Guangcong Wang, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.28321v1.pdf) | [![GitHub](https://img.shields.io/github/stars/J-C-Zhao/StructSplat?style=social)](https://github.com/J-C-Zhao/StructSplat) | [![Project](https://img.shields.io/badge/-Project-blue)](https://structsplat.github.io)  
  Keywords: sparse view, 3d gaussian, semantic, ar, gaussian splatting, geometry  
- **[CoIn: Comprehensive 2D-3D Inpainting with Gaussian Splatting Guidance](https://arxiv.org/abs/2606.27584v1)**  
  Authors: Hana Kim, Minje Kim, Tae-Kyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27584v1.pdf)  
  Keywords: gaussian splatting, efficient, ar, segmentation  
- **[Vis4GS: A Visual Analytic Tool for 3D Gaussian Splatting Reconstruction](https://arxiv.org/abs/2606.26985v1)**  
  Authors: Kai-Yuan Lin, Aryabima Mandala Putra, Jui-Chi Lee, Shih-Hsuan Hung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26985v1.pdf)  
  Keywords: understanding, 3d gaussian, real-time rendering, ar, fast, gaussian splatting  
- **[Capacity-Controlled Multi-View Stylization of 3D Gaussian Splatting](https://arxiv.org/abs/2606.26754v1)**  
  Authors: Zhihao Wen, Yixin Yang, Bojian Wu, Yang Zhou, Dani Lischinski, Daniel Cohen-Or, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26754v1.pdf)  
  Keywords: efficient, 3d gaussian, semantic, ar, gaussian splatting  
- **[FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation](https://arxiv.org/abs/2606.24874v1)**  
  Authors: Haorui Ji, Weizhe Liu, Hongdong Li, Hengkai Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24874v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, high-fidelity, gaussian splatting, geometry  
- **[SignNet-1M: Large-Scale Multilingual Sign Language Video Dataset with Downstream Benchmarks](https://arxiv.org/abs/2606.24361v1)**  
  Authors: Zhewen He, Junyi Hu, Haomian Huang, Zhenhua Li, Yu-Shen Liu, Yi Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24361v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://signnet.chatsign.ai)  
  Keywords: 3d gaussian, ar, compression, recognition, motion, gaussian splatting  
- **[Open-Vocabulary BEV Segmentation with 3D-Aware Geometric Constraints](https://arxiv.org/abs/2606.24353v1)**  
  Authors: Hojun Choi, Seulbin Hwang, Dae Jung Kim, Kisung Kim, Hyunjung Shim, Jinhan Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24353v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hchoi256.github.io/projects/ovbevseg)  
  Keywords: efficient, semantic, ar, fast, gaussian splatting, geometry, segmentation, autonomous driving  
- **[Deep Learning Approaches for 3D Medical Scene Completion: From Geometric Modeling to Generative Paradigms](https://arxiv.org/abs/2606.24180v1)**  
  Authors: Afifa Khaled, Said Jadid Abdulkadir, Majdy Mohamed Eltayeb Eltahir  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24180v1.pdf)  
  Keywords: medical, 3d gaussian, semantic, real-time rendering, ar, robotics, gaussian splatting  
- **[Learning Stable Canonical Worlds for Novel View Synthesis and Beyond](https://arxiv.org/abs/2606.23027v2)**  
  Authors: Xiaoyu Xu, Jian Zou, Sheyang Tang, Zhihua Wang, Jing Liao, Kede Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23027v2.pdf)  
  Keywords: gaussian splatting, semantic, segmentation, ar  
- **[Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation](https://arxiv.org/abs/2606.22197v1)**  
  Authors: Rui Wang, Quentin Lohmeyer, Siyu Tang, Mirko Meboldt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22197v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://batfacewayne.github.io/Multi4D.io)  
  Keywords: face, 3d gaussian, semantic, ar, dynamic, high-fidelity, gaussian splatting, motion, geometry, deformation, compact, 4d, segmentation, head  



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