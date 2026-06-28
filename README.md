# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-06-28 02:30:30

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
- [Avatar Generation](#avatar-generation) (171 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (184 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (45 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (209 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (19 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (189 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (119 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (11 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (53 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (73 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (113 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: neural rendering, motion, compact, 4d, medical, autonomous driving, ar, 3d gaussian, vr, 3d reconstruction, survey, gaussian splatting, recognition  
- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137v1)**  
  Authors: Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00137v1.pdf)  
  Keywords: ar, animation, mapping, geometry, survey, gaussian splatting  
- **[ReefMapGS: Enabling Large-Scale Underwater Reconstruction by Closing the Loop Between Multimodal SLAM and Gaussian Splatting](https://arxiv.org/abs/2604.11992v1)**  
  Authors: Daniel Yang, Jungseok Hong, John J. Leonard, Yogesh Girdhar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11992v1.pdf)  
  Keywords: motion, tracking, ar, efficient, 3d gaussian, 3d reconstruction, slam, geometry, survey, gaussian splatting  
- **[A Survey of Spatial Memory Representations for Efficient Robot Navigation](https://arxiv.org/abs/2604.16482v1)**  
  Authors: Ma. Madecheen S. Pangaliman, Steven S. Sison, Erwin P. Quilloy, Rowel Atienza  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.16482v1.pdf)  
  Keywords: ar, efficient, semantic, slam, survey  

### Acceleration

*Showing the latest 50 out of 83 papers*

- **[Vis4GS: A Visual Analytic Tool for 3D Gaussian Splatting Reconstruction](https://arxiv.org/abs/2606.26985v1)**  
  Authors: Kai-Yuan Lin, Aryabima Mandala Putra, Jui-Chi Lee, Shih-Hsuan Hung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26985v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, understanding, fast, ar, gaussian splatting  
- **[FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation](https://arxiv.org/abs/2606.24876v1)**  
  Authors: Orest Kupyn, Goutam Bhat, Philipp Henzler, Fabian Manhardt, Christian Rupprecht, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24876v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://flat-splat.github.io)  
  Keywords: real-time rendering, lightweight, face, 3d gaussian, ar  
- **[ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos](https://arxiv.org/abs/2606.24628v1)**  
  Authors: Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, Hermann Blum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24628v1.pdf)  
  Keywords: motion, tracking, real-time rendering, 3d gaussian, ar, gaussian splatting, human  
- **[Open-Vocabulary BEV Segmentation with 3D-Aware Geometric Constraints](https://arxiv.org/abs/2606.24353v1)**  
  Authors: Hojun Choi, Seulbin Hwang, Dae Jung Kim, Kisung Kim, Hyunjung Shim, Jinhan Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24353v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hchoi256.github.io/projects/ovbevseg)  
  Keywords: autonomous driving, efficient, semantic, segmentation, fast, geometry, ar, gaussian splatting  
- **[3DCarGen: Scalable 3D Car Generation via 3D-consistent Multi-view Synthesis](https://arxiv.org/abs/2606.24257v1)**  
  Authors: Hongli Xiao, Youjian Zhang, Yaohui Jin, Xiaoguang Ren, Wenjing Yang, Long Lan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24257v1.pdf)  
  Keywords: autonomous driving, 3d gaussian, fast, ar, gaussian splatting  
- **[Deep Learning Approaches for 3D Medical Scene Completion: From Geometric Modeling to Generative Paradigms](https://arxiv.org/abs/2606.24180v1)**  
  Authors: Afifa Khaled, Said Jadid Abdulkadir, Majdy Mohamed Eltayeb Eltahir  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24180v1.pdf)  
  Keywords: medical, real-time rendering, semantic, 3d gaussian, robotics, ar, gaussian splatting  
- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031v1)**  
  Authors: Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23031v1.pdf)  
  Keywords: urban scene, efficient, high-fidelity, 3d gaussian, dynamic, large scene, fast, geometry, ar, gaussian splatting  
- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091v1)**  
  Authors: Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22091v1.pdf)  
  Keywords: sparse-view, head, ar, lightweight, high-fidelity, 3d gaussian, mapping, robotics, fast, geometry, slam, gaussian splatting  
- **[ACE-GS: Acing the Trade-off with Accurate, Compact and Efficient 3D Gaussian Splatting](https://arxiv.org/abs/2606.21244v1)**  
  Authors: Jijian Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21244v1.pdf)  
  Keywords: compact, real-time rendering, efficient, high-fidelity, 3d gaussian, acceleration, fast, ar, gaussian splatting  
- **[Hand-4DGS: Feed-Forward 3D Gaussian Splatting for 4D Hand Reconstruction from Egocentric Videos](https://arxiv.org/abs/2606.19156v1)**  
  Authors: Jeongmin Bae, Seoha Kim, Marc Pollefeys, Mahdi Rad, Youngjung Uh, Taein Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.19156v1.pdf)  
  Keywords: head, motion, 4d, 3d gaussian, body, vr, dynamic, fast, ar, gaussian splatting, human  

### Applications

*Showing the latest 50 out of 498 papers*

- **[SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223v1)**  
  Authors: Jiyong Kim, Shuang Song, Ronjgun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/SatSplatDiff?style=social)](https://github.com/GDAOSU/SatSplatDiff)  
  Keywords: face, high-fidelity, 3d reconstruction, geometry, ar, gaussian splatting, shadow  
- **[PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views](https://arxiv.org/abs/2606.27071v1)**  
  Authors: Zhisong Xu, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27071v1.pdf)  
  Keywords: motion, geometry, 3d reconstruction, slam, ar  
- **[Vis4GS: A Visual Analytic Tool for 3D Gaussian Splatting Reconstruction](https://arxiv.org/abs/2606.26985v1)**  
  Authors: Kai-Yuan Lin, Aryabima Mandala Putra, Jui-Chi Lee, Shih-Hsuan Hung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26985v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, understanding, fast, ar, gaussian splatting  
- **[Capacity-Controlled Multi-View Stylization of 3D Gaussian Splatting](https://arxiv.org/abs/2606.26754v1)**  
  Authors: Zhihao Wen, Yixin Yang, Bojian Wu, Yang Zhou, Dani Lischinski, Daniel Cohen-Or, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26754v1.pdf)  
  Keywords: efficient, semantic, 3d gaussian, ar, gaussian splatting  
- **[Rendering Novel Views of MRI Using 3D Gaussian Splatting](https://arxiv.org/abs/2606.26236v1)**  
  Authors: Robin Y. Park, Mark C. Eid, Rhydian Windsor, Amir Jamaludin, Ana I. L. Namburete, João F. Henriques, Andrew Zisserman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26236v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian  
- **[TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy](https://arxiv.org/abs/2606.26092v1)**  
  Authors: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26092v1.pdf)  
  Keywords: localization, motion, 4d, high-fidelity, avatar, dynamic, ar, human, deformation  
- **[From Sparse and Imperfect 2D Anchors to Consistent 3D Gaussian Street Scenes: Support-Aware Appearance](https://arxiv.org/abs/2606.26007v1)**  
  Authors: Long Cao, Zhongquan Wang, Jie Li, Yuhan Chen, Kefei Qian, Xiangfei Huang, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26007v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Cagares/Baking-for-3D-Gaussian?style=social)](https://github.com/Cagares/Baking-for-3D-Gaussian)  
  Keywords: ar, efficient, 3d gaussian, geometry  
- **[Gastroendoscopy View Synthesis: A New Real Dataset and Evaluation](https://arxiv.org/abs/2606.25427v1)**  
  Authors: Masaki Minai, Yusuke Monno, Masatoshi Okutomi, Sho Suzuki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.25427v1.pdf)  
  Keywords: ar, gaussian splatting, nerf, 3d gaussian  
- **[FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation](https://arxiv.org/abs/2606.24876v1)**  
  Authors: Orest Kupyn, Goutam Bhat, Philipp Henzler, Fabian Manhardt, Christian Rupprecht, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24876v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://flat-splat.github.io)  
  Keywords: real-time rendering, lightweight, face, 3d gaussian, ar  
- **[FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation](https://arxiv.org/abs/2606.24874v1)**  
  Authors: Haorui Ji, Weizhe Liu, Hongdong Li, Hengkai Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24874v1.pdf)  
  Keywords: semantic, high-fidelity, 3d gaussian, geometry, ar, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 171 papers*

- **[SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223v1)**  
  Authors: Jiyong Kim, Shuang Song, Ronjgun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/SatSplatDiff?style=social)](https://github.com/GDAOSU/SatSplatDiff)  
  Keywords: face, high-fidelity, 3d reconstruction, geometry, ar, gaussian splatting, shadow  
- **[TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy](https://arxiv.org/abs/2606.26092v1)**  
  Authors: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26092v1.pdf)  
  Keywords: localization, motion, 4d, high-fidelity, avatar, dynamic, ar, human, deformation  
- **[FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation](https://arxiv.org/abs/2606.24876v1)**  
  Authors: Orest Kupyn, Goutam Bhat, Philipp Henzler, Fabian Manhardt, Christian Rupprecht, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24876v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://flat-splat.github.io)  
  Keywords: real-time rendering, lightweight, face, 3d gaussian, ar  
- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)**  
  Authors: Leshu Li, Jie Peng, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/UMN-ZhaoLab/Pocket-SLAM.git?style=social)](https://github.com/UMN-ZhaoLab/Pocket-SLAM.git)  
  Keywords: localization, autonomous driving, face, efficient, 3d gaussian, mapping, slam, geometry, ar, gaussian splatting, outdoor  
- **[ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos](https://arxiv.org/abs/2606.24628v1)**  
  Authors: Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, Hermann Blum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24628v1.pdf)  
  Keywords: motion, tracking, real-time rendering, 3d gaussian, ar, gaussian splatting, human  
- **[FiCA: Feed-forward instant Gaussian Codec Avatars from a Single Portrait Image](https://arxiv.org/abs/2606.24232v1)**  
  Authors: Kim Youwang, Zhengyu Yang, Liuhao Ge, Yu Rong, Timur Bagautdinov, Su Zhaoen, Nir Sopher, Jovan Popović, Teng Deng, Tae-Hyun Oh, Chen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24232v1.pdf)  
  Keywords: head, 3d gaussian, avatar, geometry, ar, mapping, human  
- **[Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild](https://arxiv.org/abs/2606.23688v1)**  
  Authors: Yehonathan Litman, Xiaoxuan Ma, Manan Shah, Nicolas Ugrinovic, Kris Kitani, Fernando De la Torre, Shubham Tulsiani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23688v1.pdf)  
  Keywords: motion, 4d, face, 3d gaussian, 3d reconstruction, dynamic, geometry, ar, gaussian splatting, deformation  
- **[Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation](https://arxiv.org/abs/2606.22197v1)**  
  Authors: Rui Wang, Quentin Lohmeyer, Siyu Tang, Mirko Meboldt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22197v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://batfacewayne.github.io/Multi4D.io)  
  Keywords: head, motion, compact, 4d, face, semantic, high-fidelity, 3d gaussian, segmentation, dynamic, geometry, ar, gaussian splatting, deformation  
- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091v1)**  
  Authors: Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22091v1.pdf)  
  Keywords: sparse-view, head, ar, lightweight, high-fidelity, 3d gaussian, mapping, robotics, fast, geometry, slam, gaussian splatting  
- **[$φ$-Scene: Physically Grounded Image-to-3D Scene Reconstruction](https://arxiv.org/abs/2606.21596v1)**  
  Authors: Haodong Li, Lulu Shao, Haolin Lu, Yu Fu, Yen-Ru Chen, Seemandhar Jain, Manmohan Chandraker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21596v1.pdf)  
  Keywords: high-fidelity, body, robotics, dynamic, ar, human  

### Dynamic Scene

*Showing the latest 50 out of 184 papers*

- **[PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views](https://arxiv.org/abs/2606.27071v1)**  
  Authors: Zhisong Xu, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27071v1.pdf)  
  Keywords: motion, geometry, 3d reconstruction, slam, ar  
- **[TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy](https://arxiv.org/abs/2606.26092v1)**  
  Authors: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26092v1.pdf)  
  Keywords: localization, motion, 4d, high-fidelity, avatar, dynamic, ar, human, deformation  
- **[OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis](https://arxiv.org/abs/2606.24799v1)**  
  Authors: Chenrui Fan, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24799v1.pdf)  
  Keywords: motion, 3d gaussian, high quality, 3d reconstruction, ar, gaussian splatting  
- **[ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos](https://arxiv.org/abs/2606.24628v1)**  
  Authors: Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, Hermann Blum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24628v1.pdf)  
  Keywords: motion, tracking, real-time rendering, 3d gaussian, ar, gaussian splatting, human  
- **[SignNet-1M: Large-Scale Multilingual Sign Language Video Dataset with Downstream Benchmarks](https://arxiv.org/abs/2606.24361v1)**  
  Authors: Zhewen He, Junyi Hu, Haomian Huang, Zhenhua Li, Yu-Shen Liu, Yi Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24361v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://signnet.chatsign.ai)  
  Keywords: motion, 3d gaussian, ar, gaussian splatting, recognition, compression  
- **[Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild](https://arxiv.org/abs/2606.23688v1)**  
  Authors: Yehonathan Litman, Xiaoxuan Ma, Manan Shah, Nicolas Ugrinovic, Kris Kitani, Fernando De la Torre, Shubham Tulsiani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23688v1.pdf)  
  Keywords: motion, 4d, face, 3d gaussian, 3d reconstruction, dynamic, geometry, ar, gaussian splatting, deformation  
- **[MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing](https://arxiv.org/abs/2606.23455v1)**  
  Authors: Zesong Yang, Yuanhang Lei, Liyuan Cui, Yihang Chen, Jiaer Huang, Boming Zhao, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23455v1.pdf)  
  Keywords: neural rendering, animation, high-fidelity, 3d gaussian, dynamic, ar, gaussian splatting, deformation  
- **[Temporally Aware Densification for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2606.23212v1)**  
  Authors: Vikram Sandu, Mayurdeep Pathak, Rajiv Soundararajan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23212v1.pdf)  
  Keywords: motion, 3d gaussian, dynamic, ar, gaussian splatting, deformation  
- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031v1)**  
  Authors: Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23031v1.pdf)  
  Keywords: urban scene, efficient, high-fidelity, 3d gaussian, dynamic, large scene, fast, geometry, ar, gaussian splatting  
- **[Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography](https://arxiv.org/abs/2606.22525v1)**  
  Authors: Yikuang Yuluo, Ao Wang, Shen Kuan, Yujie Liu, Wang Liao, Ying Chen, Shuangyang Zhong, Yixing Huang, Fuquan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22525v1.pdf)  
  Keywords: sparse-view, efficient, 3d gaussian, geometry, ar, gaussian splatting, deformation  

### Few-shot

- **[Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography](https://arxiv.org/abs/2606.22525v1)**  
  Authors: Yikuang Yuluo, Ao Wang, Shen Kuan, Yujie Liu, Wang Liao, Ying Chen, Shuangyang Zhong, Yixing Huang, Fuquan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22525v1.pdf)  
  Keywords: sparse-view, efficient, 3d gaussian, geometry, ar, gaussian splatting, deformation  
- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091v1)**  
  Authors: Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22091v1.pdf)  
  Keywords: sparse-view, head, ar, lightweight, high-fidelity, 3d gaussian, mapping, robotics, fast, geometry, slam, gaussian splatting  
- **[From Uncertainty to Stability and Fidelity: Guiding Sparse-View 3D Gaussian Splatting with Fisher Information](https://arxiv.org/abs/2606.20842v1)**  
  Authors: Junbao Zhou, Qingshan Xu, Yuan Zhou, Xiaolong Shen, Beier Zhu, Kesen Zhao, Yiming Zeng, Chen Bai, Cheng Lu, Hanwang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.20842v1.pdf)  
  Keywords: sparse-view, gaussian splatting, 3d gaussian, ar  
- **[VisDom: Sparse Novel View Synthesis with Visible Domain Constraint](https://arxiv.org/abs/2606.20531v1)**  
  Authors: Mariia Gladkova*, Tarun Yenamandra*, Edmond Boyer, Robert Maier, Tony Tung, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.20531v1.pdf)  
  Keywords: sparse-view, nerf, geometry, ar, gaussian splatting  
- **[FlowObject: Flow Steering for Bridging Generative Priors and Reconstruction Fidelity](https://arxiv.org/abs/2606.19019v1)**  
  Authors: Yuchen Rao, Xuqian Ren, Yinyu Nie, Sayan Deb Sarkar, Biao Zhang, Vincent Lepetit, Friedrich Fraundorfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.19019v1.pdf)  
  Keywords: sparse-view, face, 3d gaussian, 3d reconstruction, geometry, ar, gaussian splatting  
- **[KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis](https://arxiv.org/abs/2606.03120v1)**  
  Authors: Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.03120v1.pdf)  
  Keywords: sparse-view, efficient, nerf, high-fidelity, 3d gaussian, ar, gaussian splatting, outdoor  
- **[BEAST3D: Animal behavioral analysis and neural encoding from multi-view video via Gaussian splatting](https://arxiv.org/abs/2606.02937v1)**  
  Authors: Yanchen Wang, Lenny Aharon, Wangshu Zhu, Kyle Daruwalla, Linghua Zhang, Jiaru Zou, Selmaan Chettih, Helen Hou, Liam Paninski, Matthew R Whiteway  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.02937v1.pdf)  
  Keywords: sparse-view, 3d gaussian, 3d reconstruction, geometry, ar, gaussian splatting  
- **[Fast and Lightweight Novel View Synthesis with Differentiable Multiplane Image](https://arxiv.org/abs/2606.02068v1)**  
  Authors: Kaidi Zhang, Guanxu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.02068v1.pdf)  
  Keywords: sparse-view, compact, lightweight, efficient, nerf, 3d gaussian, fast, ar, gaussian splatting  
- **[DeblurNVS: Geometric Latent Diffusion for Novel View Synthesis from Sparse Motion-Blurred Images](https://arxiv.org/abs/2606.01315v1)**  
  Authors: Changyue Shi, Wangbo Yu, Chaoran Feng, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.01315v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PKU-YuanGroup/DeblurNVS?style=social)](https://github.com/PKU-YuanGroup/DeblurNVS)  
  Keywords: sparse-view, motion, efficient, nerf, high-fidelity, 3d gaussian, ar, gaussian splatting  
- **[TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction](https://arxiv.org/abs/2605.26115v1)**  
  Authors: Weijie Wang, Zimu Li, Jinchuan Shi, Zeyu Zhang, Botao Ye, Marc Pollefeys, Donny Y. Chen, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26115v1.pdf)  
  Keywords: sparse-view, head, face, 3d reconstruction, geometry, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 209 papers*

- **[SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223v1)**  
  Authors: Jiyong Kim, Shuang Song, Ronjgun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/SatSplatDiff?style=social)](https://github.com/GDAOSU/SatSplatDiff)  
  Keywords: face, high-fidelity, 3d reconstruction, geometry, ar, gaussian splatting, shadow  
- **[PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views](https://arxiv.org/abs/2606.27071v1)**  
  Authors: Zhisong Xu, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27071v1.pdf)  
  Keywords: motion, geometry, 3d reconstruction, slam, ar  
- **[From Sparse and Imperfect 2D Anchors to Consistent 3D Gaussian Street Scenes: Support-Aware Appearance](https://arxiv.org/abs/2606.26007v1)**  
  Authors: Long Cao, Zhongquan Wang, Jie Li, Yuhan Chen, Kefei Qian, Xiangfei Huang, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26007v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Cagares/Baking-for-3D-Gaussian?style=social)](https://github.com/Cagares/Baking-for-3D-Gaussian)  
  Keywords: ar, efficient, 3d gaussian, geometry  
- **[FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation](https://arxiv.org/abs/2606.24874v1)**  
  Authors: Haorui Ji, Weizhe Liu, Hongdong Li, Hengkai Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24874v1.pdf)  
  Keywords: semantic, high-fidelity, 3d gaussian, geometry, ar, gaussian splatting  
- **[OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis](https://arxiv.org/abs/2606.24799v1)**  
  Authors: Chenrui Fan, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24799v1.pdf)  
  Keywords: motion, 3d gaussian, high quality, 3d reconstruction, ar, gaussian splatting  
- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)**  
  Authors: Leshu Li, Jie Peng, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/UMN-ZhaoLab/Pocket-SLAM.git?style=social)](https://github.com/UMN-ZhaoLab/Pocket-SLAM.git)  
  Keywords: localization, autonomous driving, face, efficient, 3d gaussian, mapping, slam, geometry, ar, gaussian splatting, outdoor  
- **[Open-Vocabulary BEV Segmentation with 3D-Aware Geometric Constraints](https://arxiv.org/abs/2606.24353v1)**  
  Authors: Hojun Choi, Seulbin Hwang, Dae Jung Kim, Kisung Kim, Hyunjung Shim, Jinhan Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24353v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hchoi256.github.io/projects/ovbevseg)  
  Keywords: autonomous driving, efficient, semantic, segmentation, fast, geometry, ar, gaussian splatting  
- **[MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301v1)**  
  Authors: Hongli Xiao, Youjian Zhang, Yucai Bai, Chaoyue Wang, Yaohui Jin, Xiaoguang Ren, Wenjing Yang, Long Lan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24301v1.pdf) | [![GitHub](https://img.shields.io/github/stars/HongliXiao/MM-TRELLIS?style=social)](https://github.com/HongliXiao/MM-TRELLIS)  
  Keywords: neural rendering, autonomous driving, high-fidelity, 3d gaussian, geometry, ar, gaussian splatting  
- **[FiCA: Feed-forward instant Gaussian Codec Avatars from a Single Portrait Image](https://arxiv.org/abs/2606.24232v1)**  
  Authors: Kim Youwang, Zhengyu Yang, Liuhao Ge, Yu Rong, Timur Bagautdinov, Su Zhaoen, Nir Sopher, Jovan Popović, Teng Deng, Tae-Hyun Oh, Chen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24232v1.pdf)  
  Keywords: head, 3d gaussian, avatar, geometry, ar, mapping, human  
- **[Geometry-Aware Style Transfer in 3D Gaussian Splatting](https://arxiv.org/abs/2606.24144v1)**  
  Authors: Min Hyeok Bang, Jun Hyeong Kim, Seung-Wook Kim, Se-Ho Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24144v1.pdf) | [![GitHub](https://img.shields.io/github/stars/oweixx/gast?style=social)](https://github.com/oweixx/gast)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry  

### Large Scene

- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)**  
  Authors: Leshu Li, Jie Peng, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/UMN-ZhaoLab/Pocket-SLAM.git?style=social)](https://github.com/UMN-ZhaoLab/Pocket-SLAM.git)  
  Keywords: localization, autonomous driving, face, efficient, 3d gaussian, mapping, slam, geometry, ar, gaussian splatting, outdoor  
- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031v1)**  
  Authors: Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23031v1.pdf)  
  Keywords: urban scene, efficient, high-fidelity, 3d gaussian, dynamic, large scene, fast, geometry, ar, gaussian splatting  
- **[Point-Cloud-Assistant Localized Statistical Channel Prediction by Tangent Gaussian Splatting](https://arxiv.org/abs/2606.18734v1)**  
  Authors: Ye Xue, Yiheng Wang, Xinhua Shao, Qi Yan, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.18734v1.pdf)  
  Keywords: efficient, 3d gaussian, fast, geometry, ar, gaussian splatting, outdoor  
- **[MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization](https://arxiv.org/abs/2606.17935v1)**  
  Authors: Guo Pu, Yixuan Han, Haofeng Li, Yao Zhang, Hui Zhou, Zhouhui Lian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17935v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TrickyGo/MoonSplat?style=social)](https://github.com/TrickyGo/MoonSplat)  
  Keywords: tracking, real-time rendering, efficient, 3d gaussian, vr, 3d reconstruction, robotics, ar, gaussian splatting, outdoor  
- **[KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis](https://arxiv.org/abs/2606.03120v1)**  
  Authors: Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.03120v1.pdf)  
  Keywords: sparse-view, efficient, nerf, high-fidelity, 3d gaussian, ar, gaussian splatting, outdoor  
- **[City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.30310v1)**  
  Authors: Sayan Paul, Sourav Ghosh, Siddharth Katageri, Soumyadip Maity, Sanjana Sinha, Brojeshwar Bhowmick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.30310v1.pdf)  
  Keywords: urban scene, face, nerf, high-fidelity, 3d reconstruction, large scene, geometry, ar, gaussian splatting  
- **[GenRecon: Bridging Generative Priors for Multi-View 3D Scene Reconstruction](https://arxiv.org/abs/2605.23888v1)**  
  Authors: Katharina Schmid, Nicolas von Lützow, Jozef Hladký, Angela Dai, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.23888v1.pdf)  
  Keywords: ar, large scene, high-fidelity, geometry  
- **[Diffusion-guided Generalizable Enhancer for Urban Scene Reconstruction](https://arxiv.org/abs/2605.22420v1)**  
  Authors: Henry Che, Jingkang Wang, Yun Chen, Ze Yang, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.22420v1.pdf)  
  Keywords: neural rendering, autonomous driving, urban scene, efficient, high-fidelity, 3d gaussian, ar  
- **[Feed-Forward Gaussian Splatting from Sparse Aerial Views](https://arxiv.org/abs/2605.19949v1)**  
  Authors: Dongli Wu, Zhuoxiao Li, Tongyan Hua, Yinrui Ren, Xiaobao Wei, Rongjun Qin, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.19949v1.pdf)  
  Keywords: urban scene, 3d gaussian, geometry, ar, gaussian splatting  
- **[Cross-View Splatter: Feed-Forward View Synthesis with Georeferenced Images](https://arxiv.org/abs/2605.19656v1)**  
  Authors: Matias Turkulainen, Akshay Krishnan, Filippo Aleotti, Mohamed Sayed, Guillermo Garcia-Hernando, Juho Kannala, Arno Solin, Gabriel Brostow, Daniyar Turmukhambetov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.19656v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nianticspatial.github.io/cross-view-splatter)  
  Keywords: ar, mapping, outdoor  

### Model Compression

*Showing the latest 50 out of 189 papers*

- **[Capacity-Controlled Multi-View Stylization of 3D Gaussian Splatting](https://arxiv.org/abs/2606.26754v1)**  
  Authors: Zhihao Wen, Yixin Yang, Bojian Wu, Yang Zhou, Dani Lischinski, Daniel Cohen-Or, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26754v1.pdf)  
  Keywords: efficient, semantic, 3d gaussian, ar, gaussian splatting  
- **[From Sparse and Imperfect 2D Anchors to Consistent 3D Gaussian Street Scenes: Support-Aware Appearance](https://arxiv.org/abs/2606.26007v1)**  
  Authors: Long Cao, Zhongquan Wang, Jie Li, Yuhan Chen, Kefei Qian, Xiangfei Huang, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26007v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Cagares/Baking-for-3D-Gaussian?style=social)](https://github.com/Cagares/Baking-for-3D-Gaussian)  
  Keywords: ar, efficient, 3d gaussian, geometry  
- **[FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation](https://arxiv.org/abs/2606.24876v1)**  
  Authors: Orest Kupyn, Goutam Bhat, Philipp Henzler, Fabian Manhardt, Christian Rupprecht, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24876v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://flat-splat.github.io)  
  Keywords: real-time rendering, lightweight, face, 3d gaussian, ar  
- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)**  
  Authors: Leshu Li, Jie Peng, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/UMN-ZhaoLab/Pocket-SLAM.git?style=social)](https://github.com/UMN-ZhaoLab/Pocket-SLAM.git)  
  Keywords: localization, autonomous driving, face, efficient, 3d gaussian, mapping, slam, geometry, ar, gaussian splatting, outdoor  
- **[SignNet-1M: Large-Scale Multilingual Sign Language Video Dataset with Downstream Benchmarks](https://arxiv.org/abs/2606.24361v1)**  
  Authors: Zhewen He, Junyi Hu, Haomian Huang, Zhenhua Li, Yu-Shen Liu, Yi Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24361v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://signnet.chatsign.ai)  
  Keywords: motion, 3d gaussian, ar, gaussian splatting, recognition, compression  
- **[Open-Vocabulary BEV Segmentation with 3D-Aware Geometric Constraints](https://arxiv.org/abs/2606.24353v1)**  
  Authors: Hojun Choi, Seulbin Hwang, Dae Jung Kim, Kisung Kim, Hyunjung Shim, Jinhan Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24353v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hchoi256.github.io/projects/ovbevseg)  
  Keywords: autonomous driving, efficient, semantic, segmentation, fast, geometry, ar, gaussian splatting  
- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031v1)**  
  Authors: Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23031v1.pdf)  
  Keywords: urban scene, efficient, high-fidelity, 3d gaussian, dynamic, large scene, fast, geometry, ar, gaussian splatting  
- **[Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography](https://arxiv.org/abs/2606.22525v1)**  
  Authors: Yikuang Yuluo, Ao Wang, Shen Kuan, Yujie Liu, Wang Liao, Ying Chen, Shuangyang Zhong, Yixing Huang, Fuquan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22525v1.pdf)  
  Keywords: sparse-view, efficient, 3d gaussian, geometry, ar, gaussian splatting, deformation  
- **[Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation](https://arxiv.org/abs/2606.22197v1)**  
  Authors: Rui Wang, Quentin Lohmeyer, Siyu Tang, Mirko Meboldt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22197v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://batfacewayne.github.io/Multi4D.io)  
  Keywords: head, motion, compact, 4d, face, semantic, high-fidelity, 3d gaussian, segmentation, dynamic, geometry, ar, gaussian splatting, deformation  
- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091v1)**  
  Authors: Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22091v1.pdf)  
  Keywords: sparse-view, head, ar, lightweight, high-fidelity, 3d gaussian, mapping, robotics, fast, geometry, slam, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 119 papers*

- **[SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223v1)**  
  Authors: Jiyong Kim, Shuang Song, Ronjgun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/SatSplatDiff?style=social)](https://github.com/GDAOSU/SatSplatDiff)  
  Keywords: face, high-fidelity, 3d reconstruction, geometry, ar, gaussian splatting, shadow  
- **[TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy](https://arxiv.org/abs/2606.26092v1)**  
  Authors: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26092v1.pdf)  
  Keywords: localization, motion, 4d, high-fidelity, avatar, dynamic, ar, human, deformation  
- **[FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation](https://arxiv.org/abs/2606.24874v1)**  
  Authors: Haorui Ji, Weizhe Liu, Hongdong Li, Hengkai Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24874v1.pdf)  
  Keywords: semantic, high-fidelity, 3d gaussian, geometry, ar, gaussian splatting  
- **[OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis](https://arxiv.org/abs/2606.24799v1)**  
  Authors: Chenrui Fan, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24799v1.pdf)  
  Keywords: motion, 3d gaussian, high quality, 3d reconstruction, ar, gaussian splatting  
- **[MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301v1)**  
  Authors: Hongli Xiao, Youjian Zhang, Yucai Bai, Chaoyue Wang, Yaohui Jin, Xiaoguang Ren, Wenjing Yang, Long Lan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24301v1.pdf) | [![GitHub](https://img.shields.io/github/stars/HongliXiao/MM-TRELLIS?style=social)](https://github.com/HongliXiao/MM-TRELLIS)  
  Keywords: neural rendering, autonomous driving, high-fidelity, 3d gaussian, geometry, ar, gaussian splatting  
- **[MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing](https://arxiv.org/abs/2606.23455v1)**  
  Authors: Zesong Yang, Yuanhang Lei, Liyuan Cui, Yihang Chen, Jiaer Huang, Boming Zhao, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23455v1.pdf)  
  Keywords: neural rendering, animation, high-fidelity, 3d gaussian, dynamic, ar, gaussian splatting, deformation  
- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031v1)**  
  Authors: Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23031v1.pdf)  
  Keywords: urban scene, efficient, high-fidelity, 3d gaussian, dynamic, large scene, fast, geometry, ar, gaussian splatting  
- **[Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation](https://arxiv.org/abs/2606.22197v1)**  
  Authors: Rui Wang, Quentin Lohmeyer, Siyu Tang, Mirko Meboldt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22197v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://batfacewayne.github.io/Multi4D.io)  
  Keywords: head, motion, compact, 4d, face, semantic, high-fidelity, 3d gaussian, segmentation, dynamic, geometry, ar, gaussian splatting, deformation  
- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091v1)**  
  Authors: Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22091v1.pdf)  
  Keywords: sparse-view, head, ar, lightweight, high-fidelity, 3d gaussian, mapping, robotics, fast, geometry, slam, gaussian splatting  
- **[$φ$-Scene: Physically Grounded Image-to-3D Scene Reconstruction](https://arxiv.org/abs/2606.21596v1)**  
  Authors: Haodong Li, Lulu Shao, Haolin Lu, Yu Fu, Yen-Ru Chen, Seemandhar Jain, Manmohan Chandraker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21596v1.pdf)  
  Keywords: high-fidelity, body, robotics, dynamic, ar, human  

### Ray Tracing

- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: efficient, illumination, 3d gaussian, 3d reconstruction, global illumination, geometry, ar, gaussian splatting  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: illumination, high-fidelity, global illumination, ar, gaussian splatting  
- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314v1)**  
  Authors: Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11314v1.pdf)  
  Keywords: neural rendering, motion, relighting, lightweight, 3d gaussian, 3d reconstruction, lighting, dynamic, ray tracing, light transport, geometry, ar  
- **[Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606v1)**  
  Authors: Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09606v1.pdf)  
  Keywords: compact, relighting, illumination, 3d gaussian, lighting, ray tracing, light transport, global illumination, ar, reflection, shadow, path tracing  
- **[RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation](https://arxiv.org/abs/2606.01261v1)**  
  Authors: Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.01261v1.pdf)  
  Keywords: efficient, semantic, 3d gaussian, segmentation, ray tracing, geometry, ar, gaussian splatting, reflection  
- **[Directed Distance Fields for Constant-Time Ray Queries on Gaussian Splatting](https://arxiv.org/abs/2606.00817v1)**  
  Authors: Subhankar MIshra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00817v1.pdf) | [![GitHub](https://img.shields.io/github/stars/smlab-niser/ddf-gs?style=social)](https://github.com/smlab-niser/ddf-gs)  
  Keywords: face, illumination, 3d gaussian, fast, global illumination, ar, gaussian splatting, shadow  
- **[Underwater360: Reconstructing Underwater Scenes from Panoramic Images with Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2605.26447v1)**  
  Authors: Jiangbei Hu, Weichao Song, Shibo Yu, Mohan Wang, Zihan Yi, Rui Wu, Mingkang Xiang, Na Lei, Shengfa Wang, Zhongxuan Luo, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.26447v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SwcK423/Underwater360?style=social)](https://github.com/SwcK423/Underwater360)  
  Keywords: ar, gaussian splatting, ray casting, 3d gaussian  
- **[Differentiable Ray Tracing with Gaussians for Unified Radio Propagation Simulation and View Synthesis](https://arxiv.org/abs/2605.07781v1)**  
  Authors: Niklas Vaara, Lam Huynh, Pekka Sangi, Miguel Bordallo López, Janne Heikkilä  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.07781v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, ray tracing, geometry, ar, gaussian splatting  
- **[Power Foam: Unifying Real-Time Differentiable Ray Tracing and Rasterization](https://arxiv.org/abs/2604.24994v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Dor Verbin, Kwang Moo Yi, Anish Prabhu, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24994v1.pdf)  
  Keywords: face, efficient, ray tracing, geometry, ar  
- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138v1)**  
  Authors: Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/viserdex)  
  Keywords: tracking, efficient, semantic, 3d gaussian, lighting, dynamic, robotics, ray tracing, ar, gaussian splatting  

### Relighting

*Showing the latest 50 out of 53 papers*

- **[SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223v1)**  
  Authors: Jiyong Kim, Shuang Song, Ronjgun Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GDAOSU/SatSplatDiff?style=social)](https://github.com/GDAOSU/SatSplatDiff)  
  Keywords: face, high-fidelity, 3d reconstruction, geometry, ar, gaussian splatting, shadow  
- **[Lighting-Consistent Object Transfer Across Radiance Fields](https://arxiv.org/abs/2606.22481v1)**  
  Authors: Nicolás Violante, George Kopanas, Linus Franke, Julien Philip, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22481v1.pdf)  
  Keywords: lighting, gaussian splatting, 3d gaussian, ar  
- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: efficient, illumination, 3d gaussian, 3d reconstruction, global illumination, geometry, ar, gaussian splatting  
- **[LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping](https://arxiv.org/abs/2606.20424v1)**  
  Authors: Shikuan Shi, Chunran Zheng, Jiaming Xu, Tianyong Ye, Tao Yu, Yukang Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.20424v1.pdf)  
  Keywords: neural rendering, face, illumination, lighting, mapping, geometry, ar, gaussian splatting  
- **[AIGS-Net: Compact Illumination Field Modeling via 2D Gaussian Splatting for Fast Low-Light Image Enhancement](https://arxiv.org/abs/2606.17998v1)**  
  Authors: Yuhan Chen, Kunyang Huang, Fuchen Li, Zhuohan Qin, Guofa Li, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17998v1.pdf)  
  Keywords: compact, lightweight, efficient, face, illumination, mapping, dynamic, fast, ar, gaussian splatting  
- **[Gaussian Light Field Splatting: A Physical Prior-Driven Vision Transformer for Unsupervised Low-Light Image Enhancement](https://arxiv.org/abs/2606.17985v1)**  
  Authors: Yuhan Chen, Wenxuan Yu, Guofa Li, Fuchen Li, Kunyang Huang, Yicui Shi, Ying Fang, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17985v1.pdf)  
  Keywords: ar, gaussian splatting, illumination  
- **[RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos](https://arxiv.org/abs/2606.16278v1)**  
  Authors: Zhenhua Wu, Yun Pang, Mingkun Chang, Yuwei Ning, Liangzhi Wang, Yi Xiao, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16278v1.pdf)  
  Keywords: autonomous driving, lightweight, semantic, illumination, 3d gaussian, ar, gaussian splatting  
- **[Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation](https://arxiv.org/abs/2606.16163v1)**  
  Authors: Yuhan Chen, Wenxuan Yu, Guofa Li, Kunyang Huang, Ying Fang, Yicui Shi, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16163v1.pdf)  
  Keywords: efficient, lighting, dynamic, ar, gaussian splatting  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: illumination, high-fidelity, global illumination, ar, gaussian splatting  
- **[Wild3R: Feed-Forward 3D Gaussian Splatting from Unconstrained Sparse Photo Collection](https://arxiv.org/abs/2606.11894v2)**  
  Authors: Yuto Furutani, Takashi Otonari, Kaede Shiohara, Toshihiko Yamasaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11894v2.pdf)  
  Keywords: illumination, 3d gaussian, lighting, ar, gaussian splatting  

### SLAM

*Showing the latest 50 out of 73 papers*

- **[PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views](https://arxiv.org/abs/2606.27071v1)**  
  Authors: Zhisong Xu, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27071v1.pdf)  
  Keywords: motion, geometry, 3d reconstruction, slam, ar  
- **[TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy](https://arxiv.org/abs/2606.26092v1)**  
  Authors: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26092v1.pdf)  
  Keywords: localization, motion, 4d, high-fidelity, avatar, dynamic, ar, human, deformation  
- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)**  
  Authors: Leshu Li, Jie Peng, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/UMN-ZhaoLab/Pocket-SLAM.git?style=social)](https://github.com/UMN-ZhaoLab/Pocket-SLAM.git)  
  Keywords: localization, autonomous driving, face, efficient, 3d gaussian, mapping, slam, geometry, ar, gaussian splatting, outdoor  
- **[ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos](https://arxiv.org/abs/2606.24628v1)**  
  Authors: Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, Hermann Blum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24628v1.pdf)  
  Keywords: motion, tracking, real-time rendering, 3d gaussian, ar, gaussian splatting, human  
- **[FiCA: Feed-forward instant Gaussian Codec Avatars from a Single Portrait Image](https://arxiv.org/abs/2606.24232v1)**  
  Authors: Kim Youwang, Zhengyu Yang, Liuhao Ge, Yu Rong, Timur Bagautdinov, Su Zhaoen, Nir Sopher, Jovan Popović, Teng Deng, Tae-Hyun Oh, Chen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24232v1.pdf)  
  Keywords: head, 3d gaussian, avatar, geometry, ar, mapping, human  
- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091v1)**  
  Authors: Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22091v1.pdf)  
  Keywords: sparse-view, head, ar, lightweight, high-fidelity, 3d gaussian, mapping, robotics, fast, geometry, slam, gaussian splatting  
- **[Spectral GS-SLAM: Observability-Aware, Degeneracy-Robust Tracking for Real-Time 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2606.21258v1)**  
  Authors: Edward Beng Wai Tan, Siew-Kei Lam, Dongshuo Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21258v1.pdf)  
  Keywords: tracking, efficient, 3d gaussian, geometry, mapping, slam, ar, gaussian splatting  
- **[LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping](https://arxiv.org/abs/2606.20424v1)**  
  Authors: Shikuan Shi, Chunran Zheng, Jiaming Xu, Tianyong Ye, Tao Yu, Yukang Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.20424v1.pdf)  
  Keywords: neural rendering, face, illumination, lighting, mapping, geometry, ar, gaussian splatting  
- **[MMD-SLAM: Structure-Enhanced Multi-Meta Gaussian Distribution-Guided Visual SLAM](https://arxiv.org/abs/2606.19874v1)**  
  Authors: Fan Zhu, Ziyu Chen, Peichen Liu, Yifan Zhao, Zhisong Xu, Hui Zhu, Hongxing Zhou, Sixun Liu, Chunmao Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.19874v1.pdf)  
  Keywords: localization, tracking, high-fidelity, 3d gaussian, geometry, mapping, slam, ar, gaussian splatting  
- **[AIGS-Net: Compact Illumination Field Modeling via 2D Gaussian Splatting for Fast Low-Light Image Enhancement](https://arxiv.org/abs/2606.17998v1)**  
  Authors: Yuhan Chen, Kunyang Huang, Fuchen Li, Zhuohan Qin, Guofa Li, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17998v1.pdf)  
  Keywords: compact, lightweight, efficient, face, illumination, mapping, dynamic, fast, ar, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 113 papers*

- **[Vis4GS: A Visual Analytic Tool for 3D Gaussian Splatting Reconstruction](https://arxiv.org/abs/2606.26985v1)**  
  Authors: Kai-Yuan Lin, Aryabima Mandala Putra, Jui-Chi Lee, Shih-Hsuan Hung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26985v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, understanding, fast, ar, gaussian splatting  
- **[Capacity-Controlled Multi-View Stylization of 3D Gaussian Splatting](https://arxiv.org/abs/2606.26754v1)**  
  Authors: Zhihao Wen, Yixin Yang, Bojian Wu, Yang Zhou, Dani Lischinski, Daniel Cohen-Or, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26754v1.pdf)  
  Keywords: efficient, semantic, 3d gaussian, ar, gaussian splatting  
- **[FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation](https://arxiv.org/abs/2606.24874v1)**  
  Authors: Haorui Ji, Weizhe Liu, Hongdong Li, Hengkai Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24874v1.pdf)  
  Keywords: semantic, high-fidelity, 3d gaussian, geometry, ar, gaussian splatting  
- **[SignNet-1M: Large-Scale Multilingual Sign Language Video Dataset with Downstream Benchmarks](https://arxiv.org/abs/2606.24361v1)**  
  Authors: Zhewen He, Junyi Hu, Haomian Huang, Zhenhua Li, Yu-Shen Liu, Yi Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24361v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://signnet.chatsign.ai)  
  Keywords: motion, 3d gaussian, ar, gaussian splatting, recognition, compression  
- **[Open-Vocabulary BEV Segmentation with 3D-Aware Geometric Constraints](https://arxiv.org/abs/2606.24353v1)**  
  Authors: Hojun Choi, Seulbin Hwang, Dae Jung Kim, Kisung Kim, Hyunjung Shim, Jinhan Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24353v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hchoi256.github.io/projects/ovbevseg)  
  Keywords: autonomous driving, efficient, semantic, segmentation, fast, geometry, ar, gaussian splatting  
- **[Deep Learning Approaches for 3D Medical Scene Completion: From Geometric Modeling to Generative Paradigms](https://arxiv.org/abs/2606.24180v1)**  
  Authors: Afifa Khaled, Said Jadid Abdulkadir, Majdy Mohamed Eltayeb Eltahir  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24180v1.pdf)  
  Keywords: medical, real-time rendering, semantic, 3d gaussian, robotics, ar, gaussian splatting  
- **[Learning Stable Canonical Worlds for Novel View Synthesis and Beyond](https://arxiv.org/abs/2606.23027v2)**  
  Authors: Xiaoyu Xu, Jian Zou, Sheyang Tang, Zhihua Wang, Jing Liao, Kede Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23027v2.pdf)  
  Keywords: ar, gaussian splatting, semantic, segmentation  
- **[Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation](https://arxiv.org/abs/2606.22197v1)**  
  Authors: Rui Wang, Quentin Lohmeyer, Siyu Tang, Mirko Meboldt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22197v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://batfacewayne.github.io/Multi4D.io)  
  Keywords: head, motion, compact, 4d, face, semantic, high-fidelity, 3d gaussian, segmentation, dynamic, geometry, ar, gaussian splatting, deformation  
- **[LOGOS: LiDAR-Only Gaussian Elevation Splatting for Unified Tiny Obstacle Segmentation](https://arxiv.org/abs/2606.21527v1)**  
  Authors: Nan Ming, Yeqiang Qian, Chunxiang Wang, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21527v1.pdf)  
  Keywords: ar, gaussian splatting, face, segmentation  
- **[Building Drift: Documenting On-Site Construction Adaptations Across Material Lifecycles](https://arxiv.org/abs/2606.19609v1)**  
  Authors: Ritik Batra, Martin Tamke, Tom Svilans, Jan Hüls, Amritansh Kwatra, Steven J. Jackson, Thijs Roumen, Mette Ramsgaard Thomsen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.19609v1.pdf)  
  Keywords: ar, gaussian splatting, semantic, 3d gaussian  



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