# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-09-17 02:21:52

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

- [3DGS Surveys](#3dgs-surveys) (3 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (95 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (168 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (198 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (45 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (219 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (24 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (193 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (95 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (9 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (49 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (85 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (111 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: geometry, 3d reconstruction, motion, gaussian splatting, ar, illumination, survey  
- **[UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys](https://arxiv.org/abs/2608.06404v1)**  
  Authors: Junxiong Zhou, Xuechen Li, Chonghao Qiu, Lang Qiao, Xiaowei Jia, Qi Yang, Chishan Zhang, Leikun Yin, Nanshan You, Vipin Kumar, David Mulla, Ce Yang, Zhenong Jin, Licheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06404v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://link-dev.github.io/UAV3DCrop)  
  Keywords: 3d reconstruction, 3d gaussian, dynamic, nerf, gaussian splatting, ar, geometry, survey  
- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: localization, mapping, high-fidelity, 3d gaussian, efficient, tracking, dynamic, ar, slam, survey  

### Acceleration

*Showing the latest 50 out of 95 papers*

- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: localization, mapping, robotics, slam, 3d gaussian, motion, lighting, fast, tracking, dynamic, ar, geometry, gaussian splatting  
- **[DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230v1)**  
  Authors: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17230v1.pdf)  
  Keywords: high-fidelity, 3d reconstruction, compact, 3d gaussian, motion, fast, efficient, dynamic, ar  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: human, outdoor, fast, dynamic, ar, illumination, 4d, gaussian splatting  
- **[CGGT: Curve-Grounded Geometry Transformer for 3D Parametric Curve Reconstruction](https://arxiv.org/abs/2609.14521v1)**  
  Authors: Zhirui Gao, Renjiao Yi, Yunfan Ye, Ruizhen Hu, Chenyang Zhu, Wei Chen, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14521v1.pdf)  
  Keywords: compact, sparse-view, fast, nerf, geometry, ar  
- **[Deformable 2D Gaussian Splatting for Efficient 4K Video Compression](https://arxiv.org/abs/2609.14129v1)**  
  Authors: Chenhao Zhang, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14129v1.pdf)  
  Keywords: high-fidelity, lightweight, fast, efficient, deformation, ar, compression, gaussian splatting  
- **[3D Point Splatting for mmWave Radar Novel View Synthesis](https://arxiv.org/abs/2609.11894v1)**  
  Authors: Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.11894v1.pdf)  
  Keywords: 3d gaussian, outdoor, fast, nerf, ar  
- **[FIRE3D: Feed-forward Interactive 3D Scene Reconstruction Within A Minute](https://arxiv.org/abs/2609.08848v1)**  
  Authors: Hongchi Xia, Tianhang Cheng, Wei-Chiu Ma, Shenlong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08848v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiahongchi.github.io/Fire3D)  
  Keywords: fast, geometry, ar  
- **[CVT-GS: Learning to Simplify 3D Gaussian Splatting with Centroidal Voronoi Tessellation](https://arxiv.org/abs/2609.08730v1)**  
  Authors: Bingxian Li, Yilong Li, Jingliang Peng, Peng-Shuai Wang, Fei Zhu, Guozheng Li, Chi Harold Liu, Guoping Wang, Bo Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08730v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, fast, head, ar, geometry, lightweight, gaussian splatting  
- **[GSComplete: Gaussian Splat Completion with 2D Diffusion Priors](https://arxiv.org/abs/2609.08449v1)**  
  Authors: Elias Brugger, Philipp Erler, Stefan Ohrhallinger, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08449v1.pdf)  
  Keywords: fast, ar, high-fidelity  
- **[LightSplat: Real-Time High-Fidelity 3D Gaussian SLAM with Loop Closure](https://arxiv.org/abs/2609.07274v1)**  
  Authors: Junze Bao, Ye Gao, Yiming Huang, Xiaolong Yu, Chen Dong, Qing Gao, Wei Wang, Jinhu Lü  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07274v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, motion, fast, efficient, tracking, ar, slam, gaussian splatting  

### Applications

*Showing the latest 50 out of 498 papers*

- **[NormLift: From Lifted Features To Semantic Reliability In 3D Gaussian Splatting](https://arxiv.org/abs/2609.18898v1)**  
  Authors: Yihan Zang, Da Li, Dominik Engel, Shinkyu Park, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18898v1.pdf)  
  Keywords: segmentation, 3d gaussian, efficient, semantic, ar, understanding, gaussian splatting  
- **[Geometry beneath the Waves: Dense Priors for Sparse-View Underwater 3D Gaussian Splatting](https://arxiv.org/abs/2609.18737v1)**  
  Authors: Harvey Caldeira, Haoran Wang, Guoxi Huang, Shaoyu Cai, Rachel Fu, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18737v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, sparse-view, ar, geometry, gaussian splatting  
- **[MoQSplat: Adaptive Progressive Streaming of 3D Gaussian Splatting via MoQ](https://arxiv.org/abs/2609.18624v1)**  
  Authors: Emanuele Artioli, Mohammadreza Ghafari, Md Tariqul Islam, Farzad Tashtarian, Christian Rothenberg, Christian Timmerer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18624v1.pdf) | [![GitHub](https://img.shields.io/github/stars/emanuele-artioli/MoQSplat?style=social)](https://github.com/emanuele-artioli/MoQSplat)  
  Keywords: semantic, 3d gaussian, head, dynamic, ar, gaussian splatting  
- **[CADSplat: Sparse-View 3D Gaussian Splatting Aided by CAD Models for Robust, Photorealistic Digital-Twin Reconstruction](https://arxiv.org/abs/2609.18473v1)**  
  Authors: Kristof Overdulve, Lode Jorissen, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18473v1.pdf)  
  Keywords: 3d gaussian, deformation, few-shot, face, sparse-view, ar, gaussian splatting  
- **[Wind on Trees: Testing Physical Grounding in Dynamic 4D Gaussian Splatting](https://arxiv.org/abs/2609.17810v1)**  
  Authors: Weiying Chen, Edmond Lou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17810v1.pdf)  
  Keywords: motion, dynamic, deformation, ar, geometry, 4d, gaussian splatting  
- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: localization, mapping, robotics, slam, 3d gaussian, motion, lighting, fast, tracking, dynamic, ar, geometry, gaussian splatting  
- **[DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230v1)**  
  Authors: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17230v1.pdf)  
  Keywords: high-fidelity, 3d reconstruction, compact, 3d gaussian, motion, fast, efficient, dynamic, ar  
- **[BRAVE-6D: Benchmark for Robotic Active Vision in 6DOF Pose Estimation](https://arxiv.org/abs/2609.17106v1)**  
  Authors: Philipp Ausserlechner, Bernhard Neuberger, Alessandro Scherl, Michael Schebek, Stefan Thalhammer, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17106v1.pdf)  
  Keywords: robotics, ar  
- **[Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement](https://arxiv.org/abs/2609.17039v1)**  
  Authors: Yuetong Wang, Jinsheng Quan, Yi Yang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17039v1.pdf)  
  Keywords: 3d gaussian, motion, sparse-view, ar, geometry, gaussian splatting  
- **[HLC-GS: Risk-Map-Guided Height-Layer Consistency Gaussian Splatting for DSM Reconstruction from Optical Satellite Imagery](https://arxiv.org/abs/2609.16772v1)**  
  Authors: Jie Yang, Yingdong Pi, Qiyan Luo, Xiaoyu Wang, Lekang Wen, Mi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16772v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, face, ar  

### Avatar Generation

*Showing the latest 50 out of 168 papers*

- **[MoQSplat: Adaptive Progressive Streaming of 3D Gaussian Splatting via MoQ](https://arxiv.org/abs/2609.18624v1)**  
  Authors: Emanuele Artioli, Mohammadreza Ghafari, Md Tariqul Islam, Farzad Tashtarian, Christian Rothenberg, Christian Timmerer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18624v1.pdf) | [![GitHub](https://img.shields.io/github/stars/emanuele-artioli/MoQSplat?style=social)](https://github.com/emanuele-artioli/MoQSplat)  
  Keywords: semantic, 3d gaussian, head, dynamic, ar, gaussian splatting  
- **[CADSplat: Sparse-View 3D Gaussian Splatting Aided by CAD Models for Robust, Photorealistic Digital-Twin Reconstruction](https://arxiv.org/abs/2609.18473v1)**  
  Authors: Kristof Overdulve, Lode Jorissen, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18473v1.pdf)  
  Keywords: 3d gaussian, deformation, few-shot, face, sparse-view, ar, gaussian splatting  
- **[HLC-GS: Risk-Map-Guided Height-Layer Consistency Gaussian Splatting for DSM Reconstruction from Optical Satellite Imagery](https://arxiv.org/abs/2609.16772v1)**  
  Authors: Jie Yang, Yingdong Pi, Qiyan Luo, Xiaoyu Wang, Lekang Wen, Mi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16772v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, face, ar  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: human, outdoor, fast, dynamic, ar, illumination, 4d, gaussian splatting  
- **[SceneBench: A Hierarchical Benchmark for Vision-Language Understanding of 3D Scenes](https://arxiv.org/abs/2609.16233v1)**  
  Authors: Anubhav Khanal, Prabigya Acharya, Roshni Poudel, Sujan Kapali, Bigyan Bhatta, Pramish Paudel, Francois Rameau, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16233v1.pdf)  
  Keywords: human, recognition, semantic, ar, geometry, understanding, gaussian splatting  
- **[Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras](https://arxiv.org/abs/2609.15032v1)**  
  Authors: Hanzhang Tu, Zhanfeng Liao, Wei Min, Jiajun Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15032v1.pdf)  
  Keywords: human, 3d gaussian, motion, efficient, dynamic, geometry, lightweight, ar  
- **[LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2609.10095v1)**  
  Authors: Donghun Ryu, Minhyeok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.10095v1.pdf)  
  Keywords: compact, 3d gaussian, outdoor, head, nerf, ar, gaussian splatting  
- **[RouteBridge: Reliability-Routed Bidirectional Distillation Between Neural Radiance Fields and 3D Gaussian Splatting](https://arxiv.org/abs/2609.09606v1)**  
  Authors: YuanHang Wang, Xin Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.09606v1.pdf)  
  Keywords: 3d gaussian, nerf, gaussian splatting, face, ar  
- **[CVT-GS: Learning to Simplify 3D Gaussian Splatting with Centroidal Voronoi Tessellation](https://arxiv.org/abs/2609.08730v1)**  
  Authors: Bingxian Li, Yilong Li, Jingliang Peng, Peng-Shuai Wang, Fei Zhu, Guozheng Li, Chi Harold Liu, Guoping Wang, Bo Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08730v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, fast, head, ar, geometry, lightweight, gaussian splatting  
- **[Heat Kernel Textures: the Geodesic Gaussians That Do Not Splat](https://arxiv.org/abs/2609.07557v1)**  
  Authors: Simone Foti, Caner Korkmaz, Stefanos Zafeiriou, Tolga Birdal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07557v1.pdf)  
  Keywords: mapping, 3d gaussian, face, geometry, ar, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 198 papers*

- **[MoQSplat: Adaptive Progressive Streaming of 3D Gaussian Splatting via MoQ](https://arxiv.org/abs/2609.18624v1)**  
  Authors: Emanuele Artioli, Mohammadreza Ghafari, Md Tariqul Islam, Farzad Tashtarian, Christian Rothenberg, Christian Timmerer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18624v1.pdf) | [![GitHub](https://img.shields.io/github/stars/emanuele-artioli/MoQSplat?style=social)](https://github.com/emanuele-artioli/MoQSplat)  
  Keywords: semantic, 3d gaussian, head, dynamic, ar, gaussian splatting  
- **[CADSplat: Sparse-View 3D Gaussian Splatting Aided by CAD Models for Robust, Photorealistic Digital-Twin Reconstruction](https://arxiv.org/abs/2609.18473v1)**  
  Authors: Kristof Overdulve, Lode Jorissen, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18473v1.pdf)  
  Keywords: 3d gaussian, deformation, few-shot, face, sparse-view, ar, gaussian splatting  
- **[Wind on Trees: Testing Physical Grounding in Dynamic 4D Gaussian Splatting](https://arxiv.org/abs/2609.17810v1)**  
  Authors: Weiying Chen, Edmond Lou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17810v1.pdf)  
  Keywords: motion, dynamic, deformation, ar, geometry, 4d, gaussian splatting  
- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: localization, mapping, robotics, slam, 3d gaussian, motion, lighting, fast, tracking, dynamic, ar, geometry, gaussian splatting  
- **[DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230v1)**  
  Authors: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17230v1.pdf)  
  Keywords: high-fidelity, 3d reconstruction, compact, 3d gaussian, motion, fast, efficient, dynamic, ar  
- **[Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement](https://arxiv.org/abs/2609.17039v1)**  
  Authors: Yuetong Wang, Jinsheng Quan, Yi Yang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17039v1.pdf)  
  Keywords: 3d gaussian, motion, sparse-view, ar, geometry, gaussian splatting  
- **[The Neverwhere Visual Parkour Benchmark Suite](https://arxiv.org/abs/2609.16443v1)**  
  Authors: Ziyu Chen, Henghui Bao, Haoran Chang, Alan Yu, Ran Choi, Kai McClennen, Gio Huh, Kevin Yang, Ri-Zhao Qiu, Yajvan Ravan, John J. Leonard, Xiaolong Wang, Phillip Isola, Ge Yang, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16443v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziyc.github.io/neverwhere-bench)  
  Keywords: 3d gaussian, motion, outdoor, gaussian splatting, ar  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: human, outdoor, fast, dynamic, ar, illumination, 4d, gaussian splatting  
- **[Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras](https://arxiv.org/abs/2609.15032v1)**  
  Authors: Hanzhang Tu, Zhanfeng Liao, Wei Min, Jiajun Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15032v1.pdf)  
  Keywords: human, 3d gaussian, motion, efficient, dynamic, geometry, lightweight, ar  
- **[SCOUT-SLAM: Structurally-Coupled Dual Uncertainty-Aware 3DGS SLAM in the Wild](https://arxiv.org/abs/2609.14634v1)**  
  Authors: Kumaran Karthik, Pramat Shastri Jois, Suresh Sundaram  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14634v1.pdf)  
  Keywords: localization, 3d gaussian, motion, tracking, dynamic, ar, slam, gaussian splatting  

### Few-shot

- **[Geometry beneath the Waves: Dense Priors for Sparse-View Underwater 3D Gaussian Splatting](https://arxiv.org/abs/2609.18737v1)**  
  Authors: Harvey Caldeira, Haoran Wang, Guoxi Huang, Shaoyu Cai, Rachel Fu, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18737v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, sparse-view, ar, geometry, gaussian splatting  
- **[CADSplat: Sparse-View 3D Gaussian Splatting Aided by CAD Models for Robust, Photorealistic Digital-Twin Reconstruction](https://arxiv.org/abs/2609.18473v1)**  
  Authors: Kristof Overdulve, Lode Jorissen, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18473v1.pdf)  
  Keywords: 3d gaussian, deformation, few-shot, face, sparse-view, ar, gaussian splatting  
- **[Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement](https://arxiv.org/abs/2609.17039v1)**  
  Authors: Yuetong Wang, Jinsheng Quan, Yi Yang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17039v1.pdf)  
  Keywords: 3d gaussian, motion, sparse-view, ar, geometry, gaussian splatting  
- **[CGGT: Curve-Grounded Geometry Transformer for 3D Parametric Curve Reconstruction](https://arxiv.org/abs/2609.14521v1)**  
  Authors: Zhirui Gao, Renjiao Yi, Yunfan Ye, Ruizhen Hu, Chenyang Zhu, Wei Chen, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14521v1.pdf)  
  Keywords: compact, sparse-view, fast, nerf, geometry, ar  
- **[VS-Splat: Voxel-Selective feed-forward Gaussian Splatting for end-to-end 3D object reconstruction from sparse-views](https://arxiv.org/abs/2609.12343v1)**  
  Authors: Yunsu Jeong, Hyuk Heo, Youngsang Kwak, Jaehwa Kwak, Il Yong Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.12343v1.pdf)  
  Keywords: ar, sparse-view, gaussian splatting  
- **[Shape-guided Gaussian Splatting for Sparse-View X-ray 3D Reconstruction](https://arxiv.org/abs/2609.10376v1)**  
  Authors: Pranav Poudel, Florence Dell'Aniello Picard, Nairouz Shehata, Frédéric Lavoie, Herve Lombaert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.10376v1.pdf) | [![GitHub](https://img.shields.io/github/stars/polyshape-lab/ShapeGuidedGaussian?style=social)](https://github.com/polyshape-lab/ShapeGuidedGaussian)  
  Keywords: 3d reconstruction, 3d gaussian, sparse-view, ar, geometry, gaussian splatting  
- **[TV-SGS: Gaussian Splatting with Geometric Information Propagation via Tensor Voting under sparse views](https://arxiv.org/abs/2609.07734v1)**  
  Authors: Harish N Sathishchandra, Philippos Mordohai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07734v1.pdf)  
  Keywords: sparse view, ar, geometry, gaussian splatting  
- **[UniFusion: Sparse-View 4D Reconstruction via Unified Spatio-temporal Depth Alignment](https://arxiv.org/abs/2609.05888v1)**  
  Authors: Yongzhe Lyu, Shaofei Wang, Yixin Chen, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05888v1.pdf)  
  Keywords: segmentation, human, sparse-view, fast, tracking, dynamic, ar, geometry, 4d, gaussian splatting  
- **[Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations](https://arxiv.org/abs/2609.03657v1)**  
  Authors: Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03657v1.pdf)  
  Keywords: robotics, 3d gaussian, nerf, ar, sparse-view, lightweight, gaussian splatting  
- **[RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation](https://arxiv.org/abs/2609.02847v2)**  
  Authors: Xiaolei Lang, Ze Kang, Zehao Huang, Naiyan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02847v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jerry-locker.github.io/roge)  
  Keywords: sparse view, 3d gaussian, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 219 papers*

- **[Geometry beneath the Waves: Dense Priors for Sparse-View Underwater 3D Gaussian Splatting](https://arxiv.org/abs/2609.18737v1)**  
  Authors: Harvey Caldeira, Haoran Wang, Guoxi Huang, Shaoyu Cai, Rachel Fu, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18737v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, sparse-view, ar, geometry, gaussian splatting  
- **[Wind on Trees: Testing Physical Grounding in Dynamic 4D Gaussian Splatting](https://arxiv.org/abs/2609.17810v1)**  
  Authors: Weiying Chen, Edmond Lou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17810v1.pdf)  
  Keywords: motion, dynamic, deformation, ar, geometry, 4d, gaussian splatting  
- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: localization, mapping, robotics, slam, 3d gaussian, motion, lighting, fast, tracking, dynamic, ar, geometry, gaussian splatting  
- **[DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230v1)**  
  Authors: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17230v1.pdf)  
  Keywords: high-fidelity, 3d reconstruction, compact, 3d gaussian, motion, fast, efficient, dynamic, ar  
- **[Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement](https://arxiv.org/abs/2609.17039v1)**  
  Authors: Yuetong Wang, Jinsheng Quan, Yi Yang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17039v1.pdf)  
  Keywords: 3d gaussian, motion, sparse-view, ar, geometry, gaussian splatting  
- **[SceneBench: A Hierarchical Benchmark for Vision-Language Understanding of 3D Scenes](https://arxiv.org/abs/2609.16233v1)**  
  Authors: Anubhav Khanal, Prabigya Acharya, Roshni Poudel, Sujan Kapali, Bigyan Bhatta, Pramish Paudel, Francois Rameau, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16233v1.pdf)  
  Keywords: human, recognition, semantic, ar, geometry, understanding, gaussian splatting  
- **[Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras](https://arxiv.org/abs/2609.15032v1)**  
  Authors: Hanzhang Tu, Zhanfeng Liao, Wei Min, Jiajun Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15032v1.pdf)  
  Keywords: human, 3d gaussian, motion, efficient, dynamic, geometry, lightweight, ar  
- **[What Makes a 3D Scene Editable? A Factorized Benchmark of Fidelity, Locality, Consistency, and Preservation](https://arxiv.org/abs/2609.14899v1)**  
  Authors: Sariah Patro, Arjun Mehra, Nikhil Bhatia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14899v1.pdf)  
  Keywords: 3d gaussian, nerf, semantic, ar, geometry, gaussian splatting  
- **[CGGT: Curve-Grounded Geometry Transformer for 3D Parametric Curve Reconstruction](https://arxiv.org/abs/2609.14521v1)**  
  Authors: Zhirui Gao, Renjiao Yi, Yunfan Ye, Ruizhen Hu, Chenyang Zhu, Wei Chen, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14521v1.pdf)  
  Keywords: compact, sparse-view, fast, nerf, geometry, ar  
- **[NOVA-GS: Noise-Aware View-Consistent Gaussian Splatting for Low-Light Novel View Synthesis](https://arxiv.org/abs/2609.12682v1)**  
  Authors: Shaurya Pavan A, Vemunuri Divya Madhuri, Yash Pradeep Gawande, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.12682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shaurya2524.github.io/nova-gs)  
  Keywords: 3d gaussian, motion, gaussian splatting, geometry, ar  

### Large Scene

- **[The Neverwhere Visual Parkour Benchmark Suite](https://arxiv.org/abs/2609.16443v1)**  
  Authors: Ziyu Chen, Henghui Bao, Haoran Chang, Alan Yu, Ran Choi, Kai McClennen, Gio Huh, Kevin Yang, Ri-Zhao Qiu, Yajvan Ravan, John J. Leonard, Xiaolong Wang, Phillip Isola, Ge Yang, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16443v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziyc.github.io/neverwhere-bench)  
  Keywords: 3d gaussian, motion, outdoor, gaussian splatting, ar  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: human, outdoor, fast, dynamic, ar, illumination, 4d, gaussian splatting  
- **[3D Point Splatting for mmWave Radar Novel View Synthesis](https://arxiv.org/abs/2609.11894v1)**  
  Authors: Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.11894v1.pdf)  
  Keywords: 3d gaussian, outdoor, fast, nerf, ar  
- **[LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2609.10095v1)**  
  Authors: Donghun Ryu, Minhyeok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.10095v1.pdf)  
  Keywords: compact, 3d gaussian, outdoor, head, nerf, ar, gaussian splatting  
- **[WorldSculpt: Generating Compositional Worlds from Grounded Videos](https://arxiv.org/abs/2609.05416v2)**  
  Authors: Muyao Niu, Jixuan He, Ruihan Yu, Lian Fu, Yonghao Yu, Zheng-Hui Huang, Yifan Zhan, Fengbo Lan, Yongtao Ge, Yinqiang Zheng, Kaipeng Zhang, Zhixiang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05416v2.pdf)  
  Keywords: robotics, large scene, vr, geometry, ar  
- **[M$^3$ISR: A Multi-Modal Multi-View Benchmark for 3D/4D Gaussian Splatting and Feedforward Compression](https://arxiv.org/abs/2608.22465v1)**  
  Authors: Xinhui Liu, Lei Liu, Zhenghao Chen, Lebin Zhou, Wei Wang, Wei Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22465v1.pdf)  
  Keywords: segmentation, high-fidelity, semantic, motion, outdoor, dynamic, ar, geometry, 4d, compression, gaussian splatting  
- **[CoMVS-GS: Collaborative Multi-View Stereo and 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2608.18413v1)**  
  Authors: Shihan Chen, Junjing Zhang, Qingsong Yan, Haibing Liu, Haofan Ren, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.18413v1.pdf)  
  Keywords: compact, 3d gaussian, motion, outdoor, efficient, face, geometry, ar, gaussian splatting  
- **[GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting](https://arxiv.org/abs/2608.10938v2)**  
  Authors: Huaiyuan Weng, Chul Min Yeum, Su-Min Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10938v2.pdf)  
  Keywords: localization, 3d gaussian, outdoor, fast, ar, geometry, gaussian splatting  
- **[OutLangSplat: 3D Language Gaussian Splatting for UAV Outdoor Scenes](https://arxiv.org/abs/2608.04560v1)**  
  Authors: Xia Yan, He Wu, Yanghui Xu, Zizhao Wu, Jiazhou Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04560v1.pdf)  
  Keywords: localization, segmentation, 3d gaussian, outdoor, efficient, semantic, ar, understanding, gaussian splatting  
- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: localization, mapping, slam, 3d gaussian, outdoor, tracking, ar, geometry, lightweight, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 193 papers*

- **[NormLift: From Lifted Features To Semantic Reliability In 3D Gaussian Splatting](https://arxiv.org/abs/2609.18898v1)**  
  Authors: Yihan Zang, Da Li, Dominik Engel, Shinkyu Park, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18898v1.pdf)  
  Keywords: segmentation, 3d gaussian, efficient, semantic, ar, understanding, gaussian splatting  
- **[DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230v1)**  
  Authors: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17230v1.pdf)  
  Keywords: high-fidelity, 3d reconstruction, compact, 3d gaussian, motion, fast, efficient, dynamic, ar  
- **[HLC-GS: Risk-Map-Guided Height-Layer Consistency Gaussian Splatting for DSM Reconstruction from Optical Satellite Imagery](https://arxiv.org/abs/2609.16772v1)**  
  Authors: Jie Yang, Yingdong Pi, Qiyan Luo, Xiaoyu Wang, Lekang Wen, Mi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16772v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, face, ar  
- **[SparseTalk - Sparsifying 3D Gaussian Language Fields for Efficient 3D Visual Question Answering](https://arxiv.org/abs/2609.15137v1)**  
  Authors: Davit Soselia, Joseph JaJa, Amitabh Varshney  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15137v1.pdf)  
  Keywords: semantic, 3d gaussian, efficient, ar  
- **[Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras](https://arxiv.org/abs/2609.15032v1)**  
  Authors: Hanzhang Tu, Zhanfeng Liao, Wei Min, Jiajun Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15032v1.pdf)  
  Keywords: human, 3d gaussian, motion, efficient, dynamic, geometry, lightweight, ar  
- **[CGGT: Curve-Grounded Geometry Transformer for 3D Parametric Curve Reconstruction](https://arxiv.org/abs/2609.14521v1)**  
  Authors: Zhirui Gao, Renjiao Yi, Yunfan Ye, Ruizhen Hu, Chenyang Zhu, Wei Chen, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14521v1.pdf)  
  Keywords: compact, sparse-view, fast, nerf, geometry, ar  
- **[Deformable 2D Gaussian Splatting for Efficient 4K Video Compression](https://arxiv.org/abs/2609.14129v1)**  
  Authors: Chenhao Zhang, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14129v1.pdf)  
  Keywords: high-fidelity, lightweight, fast, efficient, deformation, ar, compression, gaussian splatting  
- **[SkyAnchor: Updating Metric-scale Aerial 3D Gaussian Scenes from Unposed Ground-View Sequences](https://arxiv.org/abs/2609.13903v1)**  
  Authors: Zhuoxiao Li, Xinyi Liu, Taoyu Wu, Yinrui Ren, Tongyan Hua, Ou Jing, Shuai Zhang, Dongli Wu, Rongjun Qin, Ge Lin Kan, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.13903v1.pdf)  
  Keywords: localization, 3d gaussian, motion, ar, lightweight, gaussian splatting  
- **[Is Gaussian Splatting Becoming Neural Again? A Taxonomy and Controlled Study of Learned Parameterization](https://arxiv.org/abs/2609.12395v1)**  
  Authors: YuanHang Wang, Xin Cao, Yi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.12395v1.pdf)  
  Keywords: nerf, ar, efficient, gaussian splatting  
- **[Hologram Representation via Quadratic Phase Gaussian Splatting](https://arxiv.org/abs/2609.11434v1)**  
  Authors: Haolong Wang, Yicheng Zhan, Kaan Akşit, Simeng Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.11434v1.pdf)  
  Keywords: ar, lightweight, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 95 papers*

- **[DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230v1)**  
  Authors: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17230v1.pdf)  
  Keywords: high-fidelity, 3d reconstruction, compact, 3d gaussian, motion, fast, efficient, dynamic, ar  
- **[Deformable 2D Gaussian Splatting for Efficient 4K Video Compression](https://arxiv.org/abs/2609.14129v1)**  
  Authors: Chenhao Zhang, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14129v1.pdf)  
  Keywords: high-fidelity, lightweight, fast, efficient, deformation, ar, compression, gaussian splatting  
- **[Leveraging Visual and Geometric Priors for Metric-scale and Complete Vehicle Gaussian Reconstruction from Limited Views](https://arxiv.org/abs/2609.08841v1)**  
  Authors: Jinyu Miao, Jiusi Li, Yifei He, Miao Long, Kun Jiang, Mengmeng Yang, Diange Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08841v1.pdf)  
  Keywords: 3d gaussian, ar, high-fidelity  
- **[CVT-GS: Learning to Simplify 3D Gaussian Splatting with Centroidal Voronoi Tessellation](https://arxiv.org/abs/2609.08730v1)**  
  Authors: Bingxian Li, Yilong Li, Jingliang Peng, Peng-Shuai Wang, Fei Zhu, Guozheng Li, Chi Harold Liu, Guoping Wang, Bo Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08730v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, fast, head, ar, geometry, lightweight, gaussian splatting  
- **[GSComplete: Gaussian Splat Completion with 2D Diffusion Priors](https://arxiv.org/abs/2609.08449v1)**  
  Authors: Elias Brugger, Philipp Erler, Stefan Ohrhallinger, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08449v1.pdf)  
  Keywords: fast, ar, high-fidelity  
- **[LightSplat: Real-Time High-Fidelity 3D Gaussian SLAM with Loop Closure](https://arxiv.org/abs/2609.07274v1)**  
  Authors: Junze Bao, Ye Gao, Yiming Huang, Xiaolong Yu, Chen Dong, Qing Gao, Wei Wang, Jinhu Lü  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07274v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, motion, fast, efficient, tracking, ar, slam, gaussian splatting  
- **[Generalizable 6D Pose Estimation of Textureless Objects with Planar-based Gaussian Splatting](https://arxiv.org/abs/2609.07231v1)**  
  Authors: Jie Lu, Hengtan Zhang, Li Gong, Pengpeng Wang, Xianjia Yu, Jinxiang Deng, Tomi Westerlund, Zhongxue Gan, Lirong Zheng, Zhuo Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07231v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, gaussian splatting, geometry, ar  
- **[MedGSSR: Generalizable Medical Image Super-Resolution 3D Reconstruction via Hierarchical Feed-forward Gaussian Splatting](https://arxiv.org/abs/2609.06874v1)**  
  Authors: Chengkai Wang, Luoyu Hong, Yiting Zhao, Jiamin Wang, Xiang Feng, Feiwei Qin, Zhenzhong Kuang, Xuefei Yin, Ali Bashashati, Yanming Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://william2ai.github.io/medgssr)  
  Keywords: medical, high-fidelity, 3d reconstruction, 3d gaussian, fast, ar, gaussian splatting  
- **[ADELE - Adaptive Delaunay Grids for High-Fidelity Mesh-Native Reconstruction](https://arxiv.org/abs/2609.06723v1)**  
  Authors: Johannes Weidenfeller, Shaofei Wang, Philipp Fürnstahl, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06723v1.pdf)  
  Keywords: high-fidelity, nerf, face, geometry, ar  
- **[InceptionGS: Generative Bootstrapping for Large-Scale Gaussian Splatting under Unstructured View Sampling](https://arxiv.org/abs/2609.02747v1)**  
  Authors: Tianheng Lu, Guangyu Wang, Ruqi Huang, Lu Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02747v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting  

### Ray Tracing

- **[Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)**  
  Authors: Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/vorotracing)  
  Keywords: face, real-time rendering, compact, 3d gaussian, motion, fast, nerf, ray tracing, ar, gaussian splatting  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: shadow, mapping, compact, 3d gaussian, fast, reflection, efficient, nerf, ray tracing, ar, gaussian splatting  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: relighting, face, lighting, reflection, efficient, ray tracing, illumination, ar, gaussian splatting  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: face, high-fidelity, human, 3d gaussian, motion, reflection, dynamic, ray tracing, geometry, ar, gaussian splatting  
- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: ray casting, compact, human, ar, geometry, gaussian splatting  
- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869v1)**  
  Authors: Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30869v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gray)  
  Keywords: 3d gaussian, fast, gaussian splatting, ray tracing, ar  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: real-time rendering, 3d gaussian, fast, reflection, path tracing, efficient, ray tracing, geometry, ar, gaussian splatting  
- **[RenderFormer++: Scalable and Physics-Informed Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v2)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v2.pdf)  
  Keywords: neural rendering, compact, light transport, illumination, global illumination, ar  
- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: geometry, 3d reconstruction, 3d gaussian, efficient, ar, illumination, global illumination, gaussian splatting  

### Relighting

- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: localization, mapping, robotics, slam, 3d gaussian, motion, lighting, fast, tracking, dynamic, ar, geometry, gaussian splatting  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: human, outdoor, fast, dynamic, ar, illumination, 4d, gaussian splatting  
- **[RenderFormer-V2: Neural Rendering with Heterogeneous Scene Primitives](https://arxiv.org/abs/2609.05738v1)**  
  Authors: Chong Zeng, Yue Dong, Pieter Peers, Lvmin Zhang, Maneesh Agrawala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05738v1.pdf)  
  Keywords: neural rendering, lighting, light transport, face, ar  
- **[Where Appearance Fails, Geometry Recognizes: A CAD-Free 3D Shape Prior That Complements Vision Foundation Models](https://arxiv.org/abs/2609.04381v1)**  
  Authors: Chenxi Tao, Seung-Kyum Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04381v1.pdf)  
  Keywords: robotics, geometry, 3d gaussian, lighting, ar, recognition, gaussian splatting  
- **[Sparse auto-regressive modeling for scene generation from multi-view images](https://arxiv.org/abs/2609.03931v1)**  
  Authors: Thomas Lucas, Maxime Pietrantoni, Philippe Weinzaepfel, Wonjune Cho, Bardienus Pieter Duisterhof, Vincent Leroy, Jerome Revaud  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03931v1.pdf)  
  Keywords: compact, 3d gaussian, lighting, efficient, ar, gaussian splatting  
- **[LightBridge: Feed-Forward Generative Relighting for 3D Gaussian Splatting](https://arxiv.org/abs/2609.02543v1)**  
  Authors: Hezhi Cao, Panhao Cheng, huangsheng du, Qibiao Li, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02543v1.pdf)  
  Keywords: relighting, 3d gaussian, lighting, efficient, ar, illumination, gaussian splatting  
- **[Inverse Rendering for Modeling with Line Primitives](https://arxiv.org/abs/2609.00625v1)**  
  Authors: Kenji Tojo, Ariel Shamir, Nobuyuki Umetani, Bernd Bickel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00625v1.pdf)  
  Keywords: 3d gaussian, reflection, efficient, face, geometry, ar  
- **[ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos](https://arxiv.org/abs/2608.28570v1)**  
  Authors: Seungyeon Kim, Noémie Jaquier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.28570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chainsplat.github.io)  
  Keywords: high-fidelity, compact, lighting, dynamic, ar, geometry, gaussian splatting  
- **[WilLaGS: Latent-Conditional 3D Appearance Fields for Robust Gaussian Splatting In-the-Wild](https://arxiv.org/abs/2608.28240v1)**  
  Authors: Yuhao Bai, Qianqiu Tan, Lilong Chen, Huanhuan Lv, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.28240v1.pdf)  
  Keywords: real-time rendering, high-fidelity, 3d gaussian, dynamic, ar, illumination, gaussian splatting  
- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: geometry, 3d reconstruction, motion, gaussian splatting, ar, illumination, survey  

### SLAM

*Showing the latest 50 out of 85 papers*

- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: localization, mapping, robotics, slam, 3d gaussian, motion, lighting, fast, tracking, dynamic, ar, geometry, gaussian splatting  
- **[SCOUT-SLAM: Structurally-Coupled Dual Uncertainty-Aware 3DGS SLAM in the Wild](https://arxiv.org/abs/2609.14634v1)**  
  Authors: Kumaran Karthik, Pramat Shastri Jois, Suresh Sundaram  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14634v1.pdf)  
  Keywords: localization, 3d gaussian, motion, tracking, dynamic, ar, slam, gaussian splatting  
- **[SkyAnchor: Updating Metric-scale Aerial 3D Gaussian Scenes from Unposed Ground-View Sequences](https://arxiv.org/abs/2609.13903v1)**  
  Authors: Zhuoxiao Li, Xinyi Liu, Taoyu Wu, Yinrui Ren, Tongyan Hua, Ou Jing, Shuai Zhang, Dongli Wu, Rongjun Qin, Ge Lin Kan, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.13903v1.pdf)  
  Keywords: localization, 3d gaussian, motion, ar, lightweight, gaussian splatting  
- **[RIDE: Relocalization-Informed Depth Estimation with 3D Gaussian Splatting](https://arxiv.org/abs/2609.11079v1)**  
  Authors: Jiarong Lian, Zhe Xiao, Zhaoyang Zhang, Wei Li, Ruizhi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.11079v1.pdf)  
  Keywords: localization, 3d gaussian, gaussian splatting, geometry, ar  
- **[Heat Kernel Textures: the Geodesic Gaussians That Do Not Splat](https://arxiv.org/abs/2609.07557v1)**  
  Authors: Simone Foti, Caner Korkmaz, Stefanos Zafeiriou, Tolga Birdal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07557v1.pdf)  
  Keywords: mapping, 3d gaussian, face, geometry, ar, gaussian splatting  
- **[LightSplat: Real-Time High-Fidelity 3D Gaussian SLAM with Loop Closure](https://arxiv.org/abs/2609.07274v1)**  
  Authors: Junze Bao, Ye Gao, Yiming Huang, Xiaolong Yu, Chen Dong, Qing Gao, Wei Wang, Jinhu Lü  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07274v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, motion, fast, efficient, tracking, ar, slam, gaussian splatting  
- **[UniFusion: Sparse-View 4D Reconstruction via Unified Spatio-temporal Depth Alignment](https://arxiv.org/abs/2609.05888v1)**  
  Authors: Yongzhe Lyu, Shaofei Wang, Yixin Chen, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05888v1.pdf)  
  Keywords: segmentation, human, sparse-view, fast, tracking, dynamic, ar, geometry, 4d, gaussian splatting  
- **[STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction](https://arxiv.org/abs/2609.03447v1)**  
  Authors: Bocheng Li, Wenjuan Zhang, Jie Pan. Dongxu Han, Xuesong Ma, Yiling Yao, Yaning Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03447v1.pdf)  
  Keywords: mapping, 3d gaussian, face, geometry, ar, gaussian splatting  
- **[PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations](https://arxiv.org/abs/2609.03341v1)**  
  Authors: Yanshu Zhang, George Shramko, Pratul P. Srinivasan, Ke Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03341v1.pdf)  
  Keywords: mapping, 3d gaussian, deformation, ar, geometry, gaussian splatting  
- **[Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations](https://arxiv.org/abs/2609.02664v1)**  
  Authors: Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02664v1.pdf)  
  Keywords: localization, segmentation, semantic, nerf, dynamic, 4d, understanding, ar  

### Scene Understanding

*Showing the latest 50 out of 111 papers*

- **[NormLift: From Lifted Features To Semantic Reliability In 3D Gaussian Splatting](https://arxiv.org/abs/2609.18898v1)**  
  Authors: Yihan Zang, Da Li, Dominik Engel, Shinkyu Park, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18898v1.pdf)  
  Keywords: segmentation, 3d gaussian, efficient, semantic, ar, understanding, gaussian splatting  
- **[MoQSplat: Adaptive Progressive Streaming of 3D Gaussian Splatting via MoQ](https://arxiv.org/abs/2609.18624v1)**  
  Authors: Emanuele Artioli, Mohammadreza Ghafari, Md Tariqul Islam, Farzad Tashtarian, Christian Rothenberg, Christian Timmerer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18624v1.pdf) | [![GitHub](https://img.shields.io/github/stars/emanuele-artioli/MoQSplat?style=social)](https://github.com/emanuele-artioli/MoQSplat)  
  Keywords: semantic, 3d gaussian, head, dynamic, ar, gaussian splatting  
- **[SceneBench: A Hierarchical Benchmark for Vision-Language Understanding of 3D Scenes](https://arxiv.org/abs/2609.16233v1)**  
  Authors: Anubhav Khanal, Prabigya Acharya, Roshni Poudel, Sujan Kapali, Bigyan Bhatta, Pramish Paudel, Francois Rameau, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16233v1.pdf)  
  Keywords: human, recognition, semantic, ar, geometry, understanding, gaussian splatting  
- **[SparseTalk - Sparsifying 3D Gaussian Language Fields for Efficient 3D Visual Question Answering](https://arxiv.org/abs/2609.15137v1)**  
  Authors: Davit Soselia, Joseph JaJa, Amitabh Varshney  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15137v1.pdf)  
  Keywords: semantic, 3d gaussian, efficient, ar  
- **[What Makes a 3D Scene Editable? A Factorized Benchmark of Fidelity, Locality, Consistency, and Preservation](https://arxiv.org/abs/2609.14899v1)**  
  Authors: Sariah Patro, Arjun Mehra, Nikhil Bhatia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14899v1.pdf)  
  Keywords: 3d gaussian, nerf, semantic, ar, geometry, gaussian splatting  
- **[From Explicit References to Scene Manifolds: Distributional Fidelity and Realism for Radiance Field Quality Assessment](https://arxiv.org/abs/2609.07346v1)**  
  Authors: Saeed Mahmoudpour, Gi-Mun Um, Hyon-Gon Choo, Peter Schelkens  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07346v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gitlab.com/saeedmp/scoda)  
  Keywords: compression, human, 3d gaussian, nerf, semantic, ar, lightweight, gaussian splatting  
- **[PhysMAS: Physics-Grounded Multi-Agent Synthesis of Compositional 4D Gaussians](https://arxiv.org/abs/2609.07174v1)**  
  Authors: Jiang Qin, Chunji Lv, Yangguang Wei, Yang Gao, Ming Liu, Lizhong Ding, Ye Yuan, Yinjie Lei, Changsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07174v1.pdf)  
  Keywords: semantic, 3d gaussian, motion, efficient, dynamic, 4d, ar  
- **[UniFusion: Sparse-View 4D Reconstruction via Unified Spatio-temporal Depth Alignment](https://arxiv.org/abs/2609.05888v1)**  
  Authors: Yongzhe Lyu, Shaofei Wang, Yixin Chen, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05888v1.pdf)  
  Keywords: segmentation, human, sparse-view, fast, tracking, dynamic, ar, geometry, 4d, gaussian splatting  
- **[An overview of 3D Vision-Language Models](https://arxiv.org/abs/2609.05583v1)**  
  Authors: Márcus Lobo, Vitor Matias, Afonso Paiva, Jeová Farias, Tiago Novello, Moacir Ponti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05583v1.pdf)  
  Keywords: segmentation, robotics, 3d gaussian, ar, recognition, gaussian splatting  
- **[NavArena: Automated Construction of Goal-Oriented Navigation Benchmarks from 3D Gaussian Splatting Reconstructions](https://arxiv.org/abs/2609.04602v1)**  
  Authors: Junhui Wang, Wei Yang, Xinyao Li, Ningjing Fan, Yuehao Yin, Xuecheng Chen, Chao Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04602v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, gaussian splatting  



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
