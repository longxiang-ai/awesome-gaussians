# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-09-16 02:17:23

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
- [Avatar Generation](#avatar-generation) (166 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (198 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (43 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (218 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (24 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (195 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (95 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (9 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (51 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (85 papers) - Papers about SLAM using Gaussian Splatting
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
  Keywords: 3d reconstruction, motion, ar, illumination, survey, gaussian splatting, geometry  
- **[UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys](https://arxiv.org/abs/2608.06404v1)**  
  Authors: Junxiong Zhou, Xuechen Li, Chonghao Qiu, Lang Qiao, Xiaowei Jia, Qi Yang, Chishan Zhang, Leikun Yin, Nanshan You, Vipin Kumar, David Mulla, Ce Yang, Zhenong Jin, Licheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06404v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://link-dev.github.io/UAV3DCrop)  
  Keywords: 3d reconstruction, ar, dynamic, geometry, gaussian splatting, 3d gaussian, nerf, survey  
- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: slam, ar, tracking, localization, dynamic, high-fidelity, efficient, survey, 3d gaussian, mapping  

### Acceleration

*Showing the latest 50 out of 95 papers*

- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: slam, motion, ar, robotics, tracking, localization, dynamic, lighting, gaussian splatting, 3d gaussian, fast, mapping, geometry  
- **[DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230v1)**  
  Authors: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17230v1.pdf)  
  Keywords: 3d reconstruction, motion, ar, compact, dynamic, high-fidelity, efficient, 3d gaussian, fast  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: 4d, human, outdoor, illumination, ar, dynamic, gaussian splatting, fast  
- **[CGGT: Curve-Grounded Geometry Transformer for 3D Parametric Curve Reconstruction](https://arxiv.org/abs/2609.14521v1)**  
  Authors: Zhirui Gao, Renjiao Yi, Yunfan Ye, Ruizhen Hu, Chenyang Zhu, Wei Chen, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14521v1.pdf)  
  Keywords: ar, compact, sparse-view, geometry, fast, nerf  
- **[Deformable 2D Gaussian Splatting for Efficient 4K Video Compression](https://arxiv.org/abs/2609.14129v1)**  
  Authors: Chenhao Zhang, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14129v1.pdf)  
  Keywords: gaussian splatting, lightweight, ar, high-fidelity, efficient, deformation, compression, fast  
- **[3D Point Splatting for mmWave Radar Novel View Synthesis](https://arxiv.org/abs/2609.11894v1)**  
  Authors: Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.11894v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, fast, nerf  
- **[FIRE3D: Feed-forward Interactive 3D Scene Reconstruction Within A Minute](https://arxiv.org/abs/2609.08848v1)**  
  Authors: Hongchi Xia, Tianhang Cheng, Wei-Chiu Ma, Shenlong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08848v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiahongchi.github.io/Fire3D)  
  Keywords: geometry, fast, ar  
- **[CVT-GS: Learning to Simplify 3D Gaussian Splatting with Centroidal Voronoi Tessellation](https://arxiv.org/abs/2609.08730v1)**  
  Authors: Bingxian Li, Yilong Li, Jingliang Peng, Peng-Shuai Wang, Fei Zhu, Guozheng Li, Chi Harold Liu, Guoping Wang, Bo Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08730v1.pdf)  
  Keywords: lightweight, head, ar, high-fidelity, gaussian splatting, 3d gaussian, fast, geometry  
- **[GSComplete: Gaussian Splat Completion with 2D Diffusion Priors](https://arxiv.org/abs/2609.08449v1)**  
  Authors: Elias Brugger, Philipp Erler, Stefan Ohrhallinger, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08449v1.pdf)  
  Keywords: high-fidelity, fast, ar  
- **[LightSplat: Real-Time High-Fidelity 3D Gaussian SLAM with Loop Closure](https://arxiv.org/abs/2609.07274v1)**  
  Authors: Junze Bao, Ye Gao, Yiming Huang, Xiaolong Yu, Chen Dong, Qing Gao, Wei Wang, Jinhu Lü  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07274v1.pdf)  
  Keywords: slam, motion, ar, tracking, high-fidelity, efficient, gaussian splatting, 3d gaussian, fast  

### Applications

*Showing the latest 50 out of 498 papers*

- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: slam, motion, ar, robotics, tracking, localization, dynamic, lighting, gaussian splatting, 3d gaussian, fast, mapping, geometry  
- **[DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230v1)**  
  Authors: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17230v1.pdf)  
  Keywords: 3d reconstruction, motion, ar, compact, dynamic, high-fidelity, efficient, 3d gaussian, fast  
- **[BRAVE-6D: Benchmark for Robotic Active Vision in 6DOF Pose Estimation](https://arxiv.org/abs/2609.17106v1)**  
  Authors: Philipp Ausserlechner, Bernhard Neuberger, Alessandro Scherl, Michael Schebek, Stefan Thalhammer, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17106v1.pdf)  
  Keywords: robotics, ar  
- **[Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement](https://arxiv.org/abs/2609.17039v1)**  
  Authors: Yuetong Wang, Jinsheng Quan, Yi Yang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17039v1.pdf)  
  Keywords: motion, ar, sparse-view, gaussian splatting, 3d gaussian, geometry  
- **[HLC-GS: Risk-Map-Guided Height-Layer Consistency Gaussian Splatting for DSM Reconstruction from Optical Satellite Imagery](https://arxiv.org/abs/2609.16772v1)**  
  Authors: Jie Yang, Yingdong Pi, Qiyan Luo, Xiaoyu Wang, Lekang Wen, Mi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16772v1.pdf)  
  Keywords: ar, face, efficient, gaussian splatting, 3d gaussian  
- **[The Neverwhere Visual Parkour Benchmark Suite](https://arxiv.org/abs/2609.16443v1)**  
  Authors: Ziyu Chen, Henghui Bao, Haoran Chang, Alan Yu, Ran Choi, Kai McClennen, Gio Huh, Kevin Yang, Ri-Zhao Qiu, Yajvan Ravan, John J. Leonard, Xiaolong Wang, Phillip Isola, Ge Yang, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16443v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziyc.github.io/neverwhere-bench)  
  Keywords: motion, ar, outdoor, gaussian splatting, 3d gaussian  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: 4d, human, outdoor, illumination, ar, dynamic, gaussian splatting, fast  
- **[SceneBench: A Hierarchical Benchmark for Vision-Language Understanding of 3D Scenes](https://arxiv.org/abs/2609.16233v1)**  
  Authors: Anubhav Khanal, Prabigya Acharya, Roshni Poudel, Sujan Kapali, Bigyan Bhatta, Pramish Paudel, Francois Rameau, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16233v1.pdf)  
  Keywords: semantic, human, ar, recognition, understanding, gaussian splatting, geometry  
- **[SparseTalk - Sparsifying 3D Gaussian Language Fields for Efficient 3D Visual Question Answering](https://arxiv.org/abs/2609.15137v1)**  
  Authors: Davit Soselia, Joseph JaJa, Amitabh Varshney  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15137v1.pdf)  
  Keywords: semantic, 3d gaussian, efficient, ar  
- **[Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras](https://arxiv.org/abs/2609.15032v1)**  
  Authors: Hanzhang Tu, Zhanfeng Liao, Wei Min, Jiajun Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15032v1.pdf)  
  Keywords: lightweight, human, motion, ar, dynamic, efficient, geometry, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 166 papers*

- **[HLC-GS: Risk-Map-Guided Height-Layer Consistency Gaussian Splatting for DSM Reconstruction from Optical Satellite Imagery](https://arxiv.org/abs/2609.16772v1)**  
  Authors: Jie Yang, Yingdong Pi, Qiyan Luo, Xiaoyu Wang, Lekang Wen, Mi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16772v1.pdf)  
  Keywords: ar, face, efficient, gaussian splatting, 3d gaussian  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: 4d, human, outdoor, illumination, ar, dynamic, gaussian splatting, fast  
- **[SceneBench: A Hierarchical Benchmark for Vision-Language Understanding of 3D Scenes](https://arxiv.org/abs/2609.16233v1)**  
  Authors: Anubhav Khanal, Prabigya Acharya, Roshni Poudel, Sujan Kapali, Bigyan Bhatta, Pramish Paudel, Francois Rameau, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16233v1.pdf)  
  Keywords: semantic, human, ar, recognition, understanding, gaussian splatting, geometry  
- **[Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras](https://arxiv.org/abs/2609.15032v1)**  
  Authors: Hanzhang Tu, Zhanfeng Liao, Wei Min, Jiajun Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15032v1.pdf)  
  Keywords: lightweight, human, motion, ar, dynamic, efficient, geometry, 3d gaussian  
- **[LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2609.10095v1)**  
  Authors: Donghun Ryu, Minhyeok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.10095v1.pdf)  
  Keywords: head, outdoor, ar, compact, gaussian splatting, 3d gaussian, nerf  
- **[RouteBridge: Reliability-Routed Bidirectional Distillation Between Neural Radiance Fields and 3D Gaussian Splatting](https://arxiv.org/abs/2609.09606v1)**  
  Authors: YuanHang Wang, Xin Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.09606v1.pdf)  
  Keywords: ar, face, gaussian splatting, 3d gaussian, nerf  
- **[CVT-GS: Learning to Simplify 3D Gaussian Splatting with Centroidal Voronoi Tessellation](https://arxiv.org/abs/2609.08730v1)**  
  Authors: Bingxian Li, Yilong Li, Jingliang Peng, Peng-Shuai Wang, Fei Zhu, Guozheng Li, Chi Harold Liu, Guoping Wang, Bo Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08730v1.pdf)  
  Keywords: lightweight, head, ar, high-fidelity, gaussian splatting, 3d gaussian, fast, geometry  
- **[Heat Kernel Textures: the Geodesic Gaussians That Do Not Splat](https://arxiv.org/abs/2609.07557v1)**  
  Authors: Simone Foti, Caner Korkmaz, Stefanos Zafeiriou, Tolga Birdal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07557v1.pdf)  
  Keywords: ar, face, gaussian splatting, 3d gaussian, mapping, geometry  
- **[From Explicit References to Scene Manifolds: Distributional Fidelity and Realism for Radiance Field Quality Assessment](https://arxiv.org/abs/2609.07346v1)**  
  Authors: Saeed Mahmoudpour, Gi-Mun Um, Hyon-Gon Choo, Peter Schelkens  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07346v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gitlab.com/saeedmp/scoda)  
  Keywords: gaussian splatting, lightweight, human, semantic, ar, compression, 3d gaussian, nerf  
- **[ADELE - Adaptive Delaunay Grids for High-Fidelity Mesh-Native Reconstruction](https://arxiv.org/abs/2609.06723v1)**  
  Authors: Johannes Weidenfeller, Shaofei Wang, Philipp Fürnstahl, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06723v1.pdf)  
  Keywords: ar, face, high-fidelity, geometry, nerf  

### Dynamic Scene

*Showing the latest 50 out of 198 papers*

- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: slam, motion, ar, robotics, tracking, localization, dynamic, lighting, gaussian splatting, 3d gaussian, fast, mapping, geometry  
- **[DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230v1)**  
  Authors: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17230v1.pdf)  
  Keywords: 3d reconstruction, motion, ar, compact, dynamic, high-fidelity, efficient, 3d gaussian, fast  
- **[Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement](https://arxiv.org/abs/2609.17039v1)**  
  Authors: Yuetong Wang, Jinsheng Quan, Yi Yang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17039v1.pdf)  
  Keywords: motion, ar, sparse-view, gaussian splatting, 3d gaussian, geometry  
- **[The Neverwhere Visual Parkour Benchmark Suite](https://arxiv.org/abs/2609.16443v1)**  
  Authors: Ziyu Chen, Henghui Bao, Haoran Chang, Alan Yu, Ran Choi, Kai McClennen, Gio Huh, Kevin Yang, Ri-Zhao Qiu, Yajvan Ravan, John J. Leonard, Xiaolong Wang, Phillip Isola, Ge Yang, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16443v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziyc.github.io/neverwhere-bench)  
  Keywords: motion, ar, outdoor, gaussian splatting, 3d gaussian  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: 4d, human, outdoor, illumination, ar, dynamic, gaussian splatting, fast  
- **[Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras](https://arxiv.org/abs/2609.15032v1)**  
  Authors: Hanzhang Tu, Zhanfeng Liao, Wei Min, Jiajun Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15032v1.pdf)  
  Keywords: lightweight, human, motion, ar, dynamic, efficient, geometry, 3d gaussian  
- **[SCOUT-SLAM: Structurally-Coupled Dual Uncertainty-Aware 3DGS SLAM in the Wild](https://arxiv.org/abs/2609.14634v1)**  
  Authors: Kumaran Karthik, Pramat Shastri Jois, Suresh Sundaram  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14634v1.pdf)  
  Keywords: slam, motion, ar, tracking, dynamic, gaussian splatting, 3d gaussian, localization  
- **[Deformable 2D Gaussian Splatting for Efficient 4K Video Compression](https://arxiv.org/abs/2609.14129v1)**  
  Authors: Chenhao Zhang, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14129v1.pdf)  
  Keywords: gaussian splatting, lightweight, ar, high-fidelity, efficient, deformation, compression, fast  
- **[SkyAnchor: Updating Metric-scale Aerial 3D Gaussian Scenes from Unposed Ground-View Sequences](https://arxiv.org/abs/2609.13903v1)**  
  Authors: Zhuoxiao Li, Xinyi Liu, Taoyu Wu, Yinrui Ren, Tongyan Hua, Ou Jing, Shuai Zhang, Dongli Wu, Rongjun Qin, Ge Lin Kan, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.13903v1.pdf)  
  Keywords: lightweight, motion, ar, gaussian splatting, 3d gaussian, localization  
- **[NOVA-GS: Noise-Aware View-Consistent Gaussian Splatting for Low-Light Novel View Synthesis](https://arxiv.org/abs/2609.12682v1)**  
  Authors: Shaurya Pavan A, Vemunuri Divya Madhuri, Yash Pradeep Gawande, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.12682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shaurya2524.github.io/nova-gs)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, geometry  

### Few-shot

- **[Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement](https://arxiv.org/abs/2609.17039v1)**  
  Authors: Yuetong Wang, Jinsheng Quan, Yi Yang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17039v1.pdf)  
  Keywords: motion, ar, sparse-view, gaussian splatting, 3d gaussian, geometry  
- **[CGGT: Curve-Grounded Geometry Transformer for 3D Parametric Curve Reconstruction](https://arxiv.org/abs/2609.14521v1)**  
  Authors: Zhirui Gao, Renjiao Yi, Yunfan Ye, Ruizhen Hu, Chenyang Zhu, Wei Chen, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14521v1.pdf)  
  Keywords: ar, compact, sparse-view, geometry, fast, nerf  
- **[VS-Splat: Voxel-Selective feed-forward Gaussian Splatting for end-to-end 3D object reconstruction from sparse-views](https://arxiv.org/abs/2609.12343v1)**  
  Authors: Yunsu Jeong, Hyuk Heo, Youngsang Kwak, Jaehwa Kwak, Il Yong Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.12343v1.pdf)  
  Keywords: gaussian splatting, sparse-view, ar  
- **[Shape-guided Gaussian Splatting for Sparse-View X-ray 3D Reconstruction](https://arxiv.org/abs/2609.10376v1)**  
  Authors: Pranav Poudel, Florence Dell'Aniello Picard, Nairouz Shehata, Frédéric Lavoie, Herve Lombaert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.10376v1.pdf) | [![GitHub](https://img.shields.io/github/stars/polyshape-lab/ShapeGuidedGaussian?style=social)](https://github.com/polyshape-lab/ShapeGuidedGaussian)  
  Keywords: 3d reconstruction, ar, sparse-view, gaussian splatting, 3d gaussian, geometry  
- **[TV-SGS: Gaussian Splatting with Geometric Information Propagation via Tensor Voting under sparse views](https://arxiv.org/abs/2609.07734v1)**  
  Authors: Harish N Sathishchandra, Philippos Mordohai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07734v1.pdf)  
  Keywords: gaussian splatting, ar, sparse view, geometry  
- **[UniFusion: Sparse-View 4D Reconstruction via Unified Spatio-temporal Depth Alignment](https://arxiv.org/abs/2609.05888v1)**  
  Authors: Yongzhe Lyu, Shaofei Wang, Yixin Chen, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05888v1.pdf)  
  Keywords: 4d, human, ar, segmentation, tracking, dynamic, sparse-view, gaussian splatting, fast, geometry  
- **[Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations](https://arxiv.org/abs/2609.03657v1)**  
  Authors: Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03657v1.pdf)  
  Keywords: lightweight, ar, robotics, sparse-view, gaussian splatting, 3d gaussian, nerf  
- **[RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation](https://arxiv.org/abs/2609.02847v2)**  
  Authors: Xiaolei Lang, Ze Kang, Zehao Huang, Naiyan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02847v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jerry-locker.github.io/roge)  
  Keywords: 3d gaussian, sparse view, ar  
- **[GSPotential: Camera Potential Field for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2608.29346v1)**  
  Authors: Zeyuan An, Yanghang Xiao, Zhiying Leng, Yijun Feng, Xiaohui Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.29346v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, sparse-view, ar  
- **[PAGS: Autofocusing Photoacoustic Tomography via Speed-of-Sound-Adaptive Gaussian Splatting](https://arxiv.org/abs/2608.25472v1)**  
  Authors: Jiarui Ge, Jintao Ma, Bangxu Fan, Jinyan Zhang, Xiaokang Yang, Shuai Na, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25472v1.pdf)  
  Keywords: ar, compact, efficient, sparse-view, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 218 papers*

- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: slam, motion, ar, robotics, tracking, localization, dynamic, lighting, gaussian splatting, 3d gaussian, fast, mapping, geometry  
- **[DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230v1)**  
  Authors: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17230v1.pdf)  
  Keywords: 3d reconstruction, motion, ar, compact, dynamic, high-fidelity, efficient, 3d gaussian, fast  
- **[Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement](https://arxiv.org/abs/2609.17039v1)**  
  Authors: Yuetong Wang, Jinsheng Quan, Yi Yang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17039v1.pdf)  
  Keywords: motion, ar, sparse-view, gaussian splatting, 3d gaussian, geometry  
- **[SceneBench: A Hierarchical Benchmark for Vision-Language Understanding of 3D Scenes](https://arxiv.org/abs/2609.16233v1)**  
  Authors: Anubhav Khanal, Prabigya Acharya, Roshni Poudel, Sujan Kapali, Bigyan Bhatta, Pramish Paudel, Francois Rameau, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16233v1.pdf)  
  Keywords: semantic, human, ar, recognition, understanding, gaussian splatting, geometry  
- **[Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras](https://arxiv.org/abs/2609.15032v1)**  
  Authors: Hanzhang Tu, Zhanfeng Liao, Wei Min, Jiajun Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15032v1.pdf)  
  Keywords: lightweight, human, motion, ar, dynamic, efficient, geometry, 3d gaussian  
- **[What Makes a 3D Scene Editable? A Factorized Benchmark of Fidelity, Locality, Consistency, and Preservation](https://arxiv.org/abs/2609.14899v1)**  
  Authors: Sariah Patro, Arjun Mehra, Nikhil Bhatia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14899v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, 3d gaussian, nerf, geometry  
- **[CGGT: Curve-Grounded Geometry Transformer for 3D Parametric Curve Reconstruction](https://arxiv.org/abs/2609.14521v1)**  
  Authors: Zhirui Gao, Renjiao Yi, Yunfan Ye, Ruizhen Hu, Chenyang Zhu, Wei Chen, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14521v1.pdf)  
  Keywords: ar, compact, sparse-view, geometry, fast, nerf  
- **[NOVA-GS: Noise-Aware View-Consistent Gaussian Splatting for Low-Light Novel View Synthesis](https://arxiv.org/abs/2609.12682v1)**  
  Authors: Shaurya Pavan A, Vemunuri Divya Madhuri, Yash Pradeep Gawande, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.12682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shaurya2524.github.io/nova-gs)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, geometry  
- **[RIDE: Relocalization-Informed Depth Estimation with 3D Gaussian Splatting](https://arxiv.org/abs/2609.11079v1)**  
  Authors: Jiarong Lian, Zhe Xiao, Zhaoyang Zhang, Wei Li, Ruizhi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.11079v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, localization, geometry  
- **[Shape-guided Gaussian Splatting for Sparse-View X-ray 3D Reconstruction](https://arxiv.org/abs/2609.10376v1)**  
  Authors: Pranav Poudel, Florence Dell'Aniello Picard, Nairouz Shehata, Frédéric Lavoie, Herve Lombaert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.10376v1.pdf) | [![GitHub](https://img.shields.io/github/stars/polyshape-lab/ShapeGuidedGaussian?style=social)](https://github.com/polyshape-lab/ShapeGuidedGaussian)  
  Keywords: 3d reconstruction, ar, sparse-view, gaussian splatting, 3d gaussian, geometry  

### Large Scene

- **[The Neverwhere Visual Parkour Benchmark Suite](https://arxiv.org/abs/2609.16443v1)**  
  Authors: Ziyu Chen, Henghui Bao, Haoran Chang, Alan Yu, Ran Choi, Kai McClennen, Gio Huh, Kevin Yang, Ri-Zhao Qiu, Yajvan Ravan, John J. Leonard, Xiaolong Wang, Phillip Isola, Ge Yang, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16443v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziyc.github.io/neverwhere-bench)  
  Keywords: motion, ar, outdoor, gaussian splatting, 3d gaussian  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: 4d, human, outdoor, illumination, ar, dynamic, gaussian splatting, fast  
- **[3D Point Splatting for mmWave Radar Novel View Synthesis](https://arxiv.org/abs/2609.11894v1)**  
  Authors: Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.11894v1.pdf)  
  Keywords: ar, outdoor, 3d gaussian, fast, nerf  
- **[LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2609.10095v1)**  
  Authors: Donghun Ryu, Minhyeok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.10095v1.pdf)  
  Keywords: head, outdoor, ar, compact, gaussian splatting, 3d gaussian, nerf  
- **[WorldSculpt: Generating Compositional Worlds from Grounded Videos](https://arxiv.org/abs/2609.05416v2)**  
  Authors: Muyao Niu, Jixuan He, Ruihan Yu, Lian Fu, Yonghao Yu, Zheng-Hui Huang, Yifan Zhan, Fengbo Lan, Yongtao Ge, Yinqiang Zheng, Kaipeng Zhang, Zhixiang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05416v2.pdf)  
  Keywords: ar, vr, robotics, large scene, geometry  
- **[M$^3$ISR: A Multi-Modal Multi-View Benchmark for 3D/4D Gaussian Splatting and Feedforward Compression](https://arxiv.org/abs/2608.22465v1)**  
  Authors: Xinhui Liu, Lei Liu, Zhenghao Chen, Lebin Zhou, Wei Wang, Wei Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22465v1.pdf)  
  Keywords: 4d, semantic, motion, outdoor, ar, segmentation, dynamic, compression, high-fidelity, gaussian splatting, geometry  
- **[CoMVS-GS: Collaborative Multi-View Stereo and 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2608.18413v1)**  
  Authors: Shihan Chen, Junjing Zhang, Qingsong Yan, Haibing Liu, Haofan Ren, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.18413v1.pdf)  
  Keywords: motion, outdoor, ar, compact, face, efficient, gaussian splatting, 3d gaussian, geometry  
- **[GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting](https://arxiv.org/abs/2608.10938v2)**  
  Authors: Huaiyuan Weng, Chul Min Yeum, Su-Min Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10938v2.pdf)  
  Keywords: outdoor, ar, gaussian splatting, 3d gaussian, fast, localization, geometry  
- **[OutLangSplat: 3D Language Gaussian Splatting for UAV Outdoor Scenes](https://arxiv.org/abs/2608.04560v1)**  
  Authors: Xia Yan, He Wu, Yanghui Xu, Zizhao Wu, Jiazhou Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04560v1.pdf)  
  Keywords: semantic, outdoor, ar, segmentation, efficient, understanding, gaussian splatting, 3d gaussian, localization  
- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: slam, lightweight, outdoor, ar, tracking, localization, gaussian splatting, 3d gaussian, mapping, geometry  

### Model Compression

*Showing the latest 50 out of 195 papers*

- **[DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230v1)**  
  Authors: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17230v1.pdf)  
  Keywords: 3d reconstruction, motion, ar, compact, dynamic, high-fidelity, efficient, 3d gaussian, fast  
- **[HLC-GS: Risk-Map-Guided Height-Layer Consistency Gaussian Splatting for DSM Reconstruction from Optical Satellite Imagery](https://arxiv.org/abs/2609.16772v1)**  
  Authors: Jie Yang, Yingdong Pi, Qiyan Luo, Xiaoyu Wang, Lekang Wen, Mi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16772v1.pdf)  
  Keywords: ar, face, efficient, gaussian splatting, 3d gaussian  
- **[SparseTalk - Sparsifying 3D Gaussian Language Fields for Efficient 3D Visual Question Answering](https://arxiv.org/abs/2609.15137v1)**  
  Authors: Davit Soselia, Joseph JaJa, Amitabh Varshney  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15137v1.pdf)  
  Keywords: semantic, 3d gaussian, efficient, ar  
- **[Tele360: Real-Time Feed-Forward Human Reconstruction from Sparse Unposed Cameras](https://arxiv.org/abs/2609.15032v1)**  
  Authors: Hanzhang Tu, Zhanfeng Liao, Wei Min, Jiajun Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15032v1.pdf)  
  Keywords: lightweight, human, motion, ar, dynamic, efficient, geometry, 3d gaussian  
- **[CGGT: Curve-Grounded Geometry Transformer for 3D Parametric Curve Reconstruction](https://arxiv.org/abs/2609.14521v1)**  
  Authors: Zhirui Gao, Renjiao Yi, Yunfan Ye, Ruizhen Hu, Chenyang Zhu, Wei Chen, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14521v1.pdf)  
  Keywords: ar, compact, sparse-view, geometry, fast, nerf  
- **[Deformable 2D Gaussian Splatting for Efficient 4K Video Compression](https://arxiv.org/abs/2609.14129v1)**  
  Authors: Chenhao Zhang, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14129v1.pdf)  
  Keywords: gaussian splatting, lightweight, ar, high-fidelity, efficient, deformation, compression, fast  
- **[SkyAnchor: Updating Metric-scale Aerial 3D Gaussian Scenes from Unposed Ground-View Sequences](https://arxiv.org/abs/2609.13903v1)**  
  Authors: Zhuoxiao Li, Xinyi Liu, Taoyu Wu, Yinrui Ren, Tongyan Hua, Ou Jing, Shuai Zhang, Dongli Wu, Rongjun Qin, Ge Lin Kan, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.13903v1.pdf)  
  Keywords: lightweight, motion, ar, gaussian splatting, 3d gaussian, localization  
- **[Is Gaussian Splatting Becoming Neural Again? A Taxonomy and Controlled Study of Learned Parameterization](https://arxiv.org/abs/2609.12395v1)**  
  Authors: YuanHang Wang, Xin Cao, Yi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.12395v1.pdf)  
  Keywords: gaussian splatting, efficient, nerf, ar  
- **[Hologram Representation via Quadratic Phase Gaussian Splatting](https://arxiv.org/abs/2609.11434v1)**  
  Authors: Haolong Wang, Yicheng Zhan, Kaan Akşit, Simeng Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.11434v1.pdf)  
  Keywords: gaussian splatting, lightweight, ar  
- **[LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2609.10095v1)**  
  Authors: Donghun Ryu, Minhyeok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.10095v1.pdf)  
  Keywords: head, outdoor, ar, compact, gaussian splatting, 3d gaussian, nerf  

### Quality Enhancement

*Showing the latest 50 out of 95 papers*

- **[DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230v1)**  
  Authors: Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17230v1.pdf)  
  Keywords: 3d reconstruction, motion, ar, compact, dynamic, high-fidelity, efficient, 3d gaussian, fast  
- **[Deformable 2D Gaussian Splatting for Efficient 4K Video Compression](https://arxiv.org/abs/2609.14129v1)**  
  Authors: Chenhao Zhang, Fengqing Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14129v1.pdf)  
  Keywords: gaussian splatting, lightweight, ar, high-fidelity, efficient, deformation, compression, fast  
- **[Leveraging Visual and Geometric Priors for Metric-scale and Complete Vehicle Gaussian Reconstruction from Limited Views](https://arxiv.org/abs/2609.08841v1)**  
  Authors: Jinyu Miao, Jiusi Li, Yifei He, Miao Long, Kun Jiang, Mengmeng Yang, Diange Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08841v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, ar  
- **[CVT-GS: Learning to Simplify 3D Gaussian Splatting with Centroidal Voronoi Tessellation](https://arxiv.org/abs/2609.08730v1)**  
  Authors: Bingxian Li, Yilong Li, Jingliang Peng, Peng-Shuai Wang, Fei Zhu, Guozheng Li, Chi Harold Liu, Guoping Wang, Bo Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08730v1.pdf)  
  Keywords: lightweight, head, ar, high-fidelity, gaussian splatting, 3d gaussian, fast, geometry  
- **[GSComplete: Gaussian Splat Completion with 2D Diffusion Priors](https://arxiv.org/abs/2609.08449v1)**  
  Authors: Elias Brugger, Philipp Erler, Stefan Ohrhallinger, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08449v1.pdf)  
  Keywords: high-fidelity, fast, ar  
- **[LightSplat: Real-Time High-Fidelity 3D Gaussian SLAM with Loop Closure](https://arxiv.org/abs/2609.07274v1)**  
  Authors: Junze Bao, Ye Gao, Yiming Huang, Xiaolong Yu, Chen Dong, Qing Gao, Wei Wang, Jinhu Lü  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07274v1.pdf)  
  Keywords: slam, motion, ar, tracking, high-fidelity, efficient, gaussian splatting, 3d gaussian, fast  
- **[Generalizable 6D Pose Estimation of Textureless Objects with Planar-based Gaussian Splatting](https://arxiv.org/abs/2609.07231v1)**  
  Authors: Jie Lu, Hengtan Zhang, Li Gong, Pengpeng Wang, Xianjia Yu, Jinxiang Deng, Tomi Westerlund, Zhongxue Gan, Lirong Zheng, Zhuo Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07231v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, 3d gaussian, geometry  
- **[MedGSSR: Generalizable Medical Image Super-Resolution 3D Reconstruction via Hierarchical Feed-forward Gaussian Splatting](https://arxiv.org/abs/2609.06874v1)**  
  Authors: Chengkai Wang, Luoyu Hong, Yiting Zhao, Jiamin Wang, Xiang Feng, Feiwei Qin, Zhenzhong Kuang, Xuefei Yin, Ali Bashashati, Yanming Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://william2ai.github.io/medgssr)  
  Keywords: 3d reconstruction, medical, ar, high-fidelity, gaussian splatting, 3d gaussian, fast  
- **[ADELE - Adaptive Delaunay Grids for High-Fidelity Mesh-Native Reconstruction](https://arxiv.org/abs/2609.06723v1)**  
  Authors: Johannes Weidenfeller, Shaofei Wang, Philipp Fürnstahl, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06723v1.pdf)  
  Keywords: ar, face, high-fidelity, geometry, nerf  
- **[InceptionGS: Generative Bootstrapping for Large-Scale Gaussian Splatting under Unstructured View Sampling](https://arxiv.org/abs/2609.02747v1)**  
  Authors: Tianheng Lu, Guangyu Wang, Ruqi Huang, Lu Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02747v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, ar  

### Ray Tracing

- **[Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)**  
  Authors: Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/vorotracing)  
  Keywords: motion, ar, ray tracing, real-time rendering, compact, face, gaussian splatting, 3d gaussian, fast, nerf  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: shadow, ar, ray tracing, mapping, compact, efficient, gaussian splatting, 3d gaussian, reflection, fast, nerf  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: ar, illumination, ray tracing, face, relighting, efficient, lighting, gaussian splatting, reflection  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: human, motion, ar, ray tracing, face, dynamic, high-fidelity, gaussian splatting, 3d gaussian, reflection, geometry  
- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: ray casting, human, ar, compact, gaussian splatting, geometry  
- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869v1)**  
  Authors: Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30869v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gray)  
  Keywords: ar, ray tracing, gaussian splatting, 3d gaussian, fast  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: ar, ray tracing, real-time rendering, path tracing, efficient, gaussian splatting, 3d gaussian, reflection, fast, geometry  
- **[RenderFormer++: Scalable and Physics-Informed Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v2)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v2.pdf)  
  Keywords: ar, illumination, compact, light transport, global illumination, neural rendering  
- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: 3d reconstruction, ar, illumination, efficient, global illumination, gaussian splatting, 3d gaussian, geometry  

### Relighting

*Showing the latest 50 out of 51 papers*

- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: slam, motion, ar, robotics, tracking, localization, dynamic, lighting, gaussian splatting, 3d gaussian, fast, mapping, geometry  
- **[Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310v1)**  
  Authors: Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle, Albert Mosella-Montoro, Jose Ribeiro-Gomes, Francisco Vicente Carrasco, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16310v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humansensinglab.github.io/monaco4d)  
  Keywords: 4d, human, outdoor, illumination, ar, dynamic, gaussian splatting, fast  
- **[RenderFormer-V2: Neural Rendering with Heterogeneous Scene Primitives](https://arxiv.org/abs/2609.05738v1)**  
  Authors: Chong Zeng, Yue Dong, Pieter Peers, Lvmin Zhang, Maneesh Agrawala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05738v1.pdf)  
  Keywords: ar, face, light transport, lighting, neural rendering  
- **[Where Appearance Fails, Geometry Recognizes: A CAD-Free 3D Shape Prior That Complements Vision Foundation Models](https://arxiv.org/abs/2609.04381v1)**  
  Authors: Chenxi Tao, Seung-Kyum Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04381v1.pdf)  
  Keywords: ar, robotics, recognition, lighting, gaussian splatting, 3d gaussian, geometry  
- **[Sparse auto-regressive modeling for scene generation from multi-view images](https://arxiv.org/abs/2609.03931v1)**  
  Authors: Thomas Lucas, Maxime Pietrantoni, Philippe Weinzaepfel, Wonjune Cho, Bardienus Pieter Duisterhof, Vincent Leroy, Jerome Revaud  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03931v1.pdf)  
  Keywords: ar, compact, efficient, lighting, gaussian splatting, 3d gaussian  
- **[LightBridge: Feed-Forward Generative Relighting for 3D Gaussian Splatting](https://arxiv.org/abs/2609.02543v1)**  
  Authors: Hezhi Cao, Panhao Cheng, huangsheng du, Qibiao Li, Youcheng Cai, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02543v1.pdf)  
  Keywords: ar, illumination, relighting, efficient, lighting, gaussian splatting, 3d gaussian  
- **[Inverse Rendering for Modeling with Line Primitives](https://arxiv.org/abs/2609.00625v1)**  
  Authors: Kenji Tojo, Ariel Shamir, Nobuyuki Umetani, Bernd Bickel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00625v1.pdf)  
  Keywords: ar, face, efficient, geometry, 3d gaussian, reflection  
- **[ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos](https://arxiv.org/abs/2608.28570v1)**  
  Authors: Seungyeon Kim, Noémie Jaquier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.28570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chainsplat.github.io)  
  Keywords: ar, compact, dynamic, high-fidelity, lighting, gaussian splatting, geometry  
- **[WilLaGS: Latent-Conditional 3D Appearance Fields for Robust Gaussian Splatting In-the-Wild](https://arxiv.org/abs/2608.28240v1)**  
  Authors: Yuhao Bai, Qianqiu Tan, Lilong Chen, Huanhuan Lv, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.28240v1.pdf)  
  Keywords: ar, illumination, real-time rendering, dynamic, high-fidelity, gaussian splatting, 3d gaussian  
- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: 3d reconstruction, motion, ar, illumination, survey, gaussian splatting, geometry  

### SLAM

*Showing the latest 50 out of 85 papers*

- **[PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387v1)**  
  Authors: Yongqi Mao, Hao Shi, Yufan Zhang, Zhonghua Yi, Xiangfei Guo, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17387v1.pdf)  
  Keywords: slam, motion, ar, robotics, tracking, localization, dynamic, lighting, gaussian splatting, 3d gaussian, fast, mapping, geometry  
- **[SCOUT-SLAM: Structurally-Coupled Dual Uncertainty-Aware 3DGS SLAM in the Wild](https://arxiv.org/abs/2609.14634v1)**  
  Authors: Kumaran Karthik, Pramat Shastri Jois, Suresh Sundaram  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14634v1.pdf)  
  Keywords: slam, motion, ar, tracking, dynamic, gaussian splatting, 3d gaussian, localization  
- **[SkyAnchor: Updating Metric-scale Aerial 3D Gaussian Scenes from Unposed Ground-View Sequences](https://arxiv.org/abs/2609.13903v1)**  
  Authors: Zhuoxiao Li, Xinyi Liu, Taoyu Wu, Yinrui Ren, Tongyan Hua, Ou Jing, Shuai Zhang, Dongli Wu, Rongjun Qin, Ge Lin Kan, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.13903v1.pdf)  
  Keywords: lightweight, motion, ar, gaussian splatting, 3d gaussian, localization  
- **[RIDE: Relocalization-Informed Depth Estimation with 3D Gaussian Splatting](https://arxiv.org/abs/2609.11079v1)**  
  Authors: Jiarong Lian, Zhe Xiao, Zhaoyang Zhang, Wei Li, Ruizhi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.11079v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, localization, geometry  
- **[Heat Kernel Textures: the Geodesic Gaussians That Do Not Splat](https://arxiv.org/abs/2609.07557v1)**  
  Authors: Simone Foti, Caner Korkmaz, Stefanos Zafeiriou, Tolga Birdal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07557v1.pdf)  
  Keywords: ar, face, gaussian splatting, 3d gaussian, mapping, geometry  
- **[LightSplat: Real-Time High-Fidelity 3D Gaussian SLAM with Loop Closure](https://arxiv.org/abs/2609.07274v1)**  
  Authors: Junze Bao, Ye Gao, Yiming Huang, Xiaolong Yu, Chen Dong, Qing Gao, Wei Wang, Jinhu Lü  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07274v1.pdf)  
  Keywords: slam, motion, ar, tracking, high-fidelity, efficient, gaussian splatting, 3d gaussian, fast  
- **[UniFusion: Sparse-View 4D Reconstruction via Unified Spatio-temporal Depth Alignment](https://arxiv.org/abs/2609.05888v1)**  
  Authors: Yongzhe Lyu, Shaofei Wang, Yixin Chen, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05888v1.pdf)  
  Keywords: 4d, human, ar, segmentation, tracking, dynamic, sparse-view, gaussian splatting, fast, geometry  
- **[STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction](https://arxiv.org/abs/2609.03447v1)**  
  Authors: Bocheng Li, Wenjuan Zhang, Jie Pan. Dongxu Han, Xuesong Ma, Yiling Yao, Yaning Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03447v1.pdf)  
  Keywords: ar, face, gaussian splatting, 3d gaussian, mapping, geometry  
- **[PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations](https://arxiv.org/abs/2609.03341v1)**  
  Authors: Yanshu Zhang, George Shramko, Pratul P. Srinivasan, Ke Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03341v1.pdf)  
  Keywords: ar, deformation, gaussian splatting, 3d gaussian, mapping, geometry  
- **[Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations](https://arxiv.org/abs/2609.02664v1)**  
  Authors: Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02664v1.pdf)  
  Keywords: 4d, semantic, ar, segmentation, localization, dynamic, understanding, nerf  

### Scene Understanding

*Showing the latest 50 out of 109 papers*

- **[SceneBench: A Hierarchical Benchmark for Vision-Language Understanding of 3D Scenes](https://arxiv.org/abs/2609.16233v1)**  
  Authors: Anubhav Khanal, Prabigya Acharya, Roshni Poudel, Sujan Kapali, Bigyan Bhatta, Pramish Paudel, Francois Rameau, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16233v1.pdf)  
  Keywords: semantic, human, ar, recognition, understanding, gaussian splatting, geometry  
- **[SparseTalk - Sparsifying 3D Gaussian Language Fields for Efficient 3D Visual Question Answering](https://arxiv.org/abs/2609.15137v1)**  
  Authors: Davit Soselia, Joseph JaJa, Amitabh Varshney  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15137v1.pdf)  
  Keywords: semantic, 3d gaussian, efficient, ar  
- **[What Makes a 3D Scene Editable? A Factorized Benchmark of Fidelity, Locality, Consistency, and Preservation](https://arxiv.org/abs/2609.14899v1)**  
  Authors: Sariah Patro, Arjun Mehra, Nikhil Bhatia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14899v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, 3d gaussian, nerf, geometry  
- **[From Explicit References to Scene Manifolds: Distributional Fidelity and Realism for Radiance Field Quality Assessment](https://arxiv.org/abs/2609.07346v1)**  
  Authors: Saeed Mahmoudpour, Gi-Mun Um, Hyon-Gon Choo, Peter Schelkens  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07346v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gitlab.com/saeedmp/scoda)  
  Keywords: gaussian splatting, lightweight, human, semantic, ar, compression, 3d gaussian, nerf  
- **[PhysMAS: Physics-Grounded Multi-Agent Synthesis of Compositional 4D Gaussians](https://arxiv.org/abs/2609.07174v1)**  
  Authors: Jiang Qin, Chunji Lv, Yangguang Wei, Yang Gao, Ming Liu, Lizhong Ding, Ye Yuan, Yinjie Lei, Changsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07174v1.pdf)  
  Keywords: 4d, semantic, motion, ar, dynamic, efficient, 3d gaussian  
- **[UniFusion: Sparse-View 4D Reconstruction via Unified Spatio-temporal Depth Alignment](https://arxiv.org/abs/2609.05888v1)**  
  Authors: Yongzhe Lyu, Shaofei Wang, Yixin Chen, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05888v1.pdf)  
  Keywords: 4d, human, ar, segmentation, tracking, dynamic, sparse-view, gaussian splatting, fast, geometry  
- **[An overview of 3D Vision-Language Models](https://arxiv.org/abs/2609.05583v1)**  
  Authors: Márcus Lobo, Vitor Matias, Afonso Paiva, Jeová Farias, Tiago Novello, Moacir Ponti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05583v1.pdf)  
  Keywords: ar, robotics, segmentation, recognition, gaussian splatting, 3d gaussian  
- **[NavArena: Automated Construction of Goal-Oriented Navigation Benchmarks from 3D Gaussian Splatting Reconstructions](https://arxiv.org/abs/2609.04602v1)**  
  Authors: Junhui Wang, Wei Yang, Xinyao Li, Ningjing Fan, Yuehao Yin, Xuecheng Chen, Chao Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04602v1.pdf)  
  Keywords: semantic, gaussian splatting, 3d gaussian, ar  
- **[Where Appearance Fails, Geometry Recognizes: A CAD-Free 3D Shape Prior That Complements Vision Foundation Models](https://arxiv.org/abs/2609.04381v1)**  
  Authors: Chenxi Tao, Seung-Kyum Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04381v1.pdf)  
  Keywords: ar, robotics, recognition, lighting, gaussian splatting, 3d gaussian, geometry  
- **[Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations](https://arxiv.org/abs/2609.02664v1)**  
  Authors: Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02664v1.pdf)  
  Keywords: 4d, semantic, ar, segmentation, localization, dynamic, understanding, nerf  



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
