# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-gaussians/)**: an interactive paper map, monthly trends, topic network and co-author network of every tracked paper.

> Last Update: 2026-11-25 06:01:45

## 📰 Latest Updates

🗺️ **[2026-09-30] Paper Atlas on GitHub Pages**
- New [interactive site](https://longxiang-ai.github.io/awesome-gaussians/) built from all daily snapshots, rebuilt after every update

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

- [3DGS Surveys](#3dgs-surveys) (5 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (87 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (500 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (156 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (167 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (30 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (207 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (31 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (183 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (49 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (5 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (49 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (71 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (89 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Urban State Representation for Autonomous Mobility: A Survey of Multimodal Perception, Architectures, Datasets, and Benchmarks](https://arxiv.org/abs/2611.28129v1)**  
  Authors: Binay Kumar Singh, Niels Da Vitoria Lobo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.28129v1.pdf) | [![GitHub](https://img.shields.io/github/stars/binayksingh/Awesome-Urban-State-Representation?style=social)](https://github.com/binayksingh/Awesome-Urban-State-Representation)  
  Keywords: autonomous driving, 3d gaussian, survey, head, ar  
- **[Spectro-Spatial Survey Fusion](https://arxiv.org/abs/2611.21798v1)**  
  Authors: Georgios N. Vassilakis, Miles Cranmer, Vasily Belokurov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.21798v1.pdf)  
  Keywords: gaussian splatting, survey, face, ar  
- **[Gaussian Splatting for Real-Time Scene Reconstruction: Methods, Systems, and Trade-offs](https://arxiv.org/abs/2610.17513v1)**  
  Authors: Ashim Dahal, Rabab Abdelfattah, Nick Rahimi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17513v1.pdf)  
  Keywords: sparse-view, gaussian splatting, tracking, localization, 3d gaussian, real-time rendering, mapping, ar, dynamic, survey, slam, compression  
- **[OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones](https://arxiv.org/abs/2609.24253v1)**  
  Authors: Zhongrui You, Zhen Li, Junli Liu, Zhigang Wang, Bin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24253v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://openflyscan.github.io)  
  Keywords: face, gaussian splatting, 3d gaussian, survey, high-fidelity, ar  
- **[Quality Assessment of 3D Gaussian Splatting: Distortions, Benchmarks, and Open Challenges](https://arxiv.org/abs/2609.23027v1)**  
  Authors: Shuai Liu, Binqiang Liu, Qingyu Mao, Jiacong Chen, Yongsheng Liang, Youneng Bao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23027v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, survey, compression  

### Acceleration

*Showing the latest 50 out of 87 papers*

- **[AnyPrune: Optimization-Free Pruning for Any Feedforward 3D Gaussian Splatting Pipeline](https://arxiv.org/abs/2611.32735v1)**  
  Authors: Nicola Leonetti, Federico Stella, Aoxiang Fan, Saqib Javed, Pascal Fua, Luigi Di Stefano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32735v1.pdf)  
  Keywords: gaussian splatting, ar, fast, 3d gaussian  
- **[Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation](https://arxiv.org/abs/2611.32718v1)**  
  Authors: Itai Mizlish, Boaz Ben-Moshe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32718v1.pdf) | [![GitHub](https://img.shields.io/github/stars/itaim18/DANIEL?style=social)](https://github.com/itaim18/DANIEL)  
  Keywords: fast, mapping, ar, slam, outdoor  
- **[SplatTok: Data-Driven Compression of 3D Gaussian Splats with Scene-Level Tokens](https://arxiv.org/abs/2611.32202v1)**  
  Authors: Sai Karthikey Pentapati, Shashank Nelamangala Sridhara, Birendra Kathariya, Peng Yin, Guandao Yang, Alan C. Bovik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32202v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, compact, compression, ar  
- **[HiGS: A Hierarchical Architecture for Fast Differentiable 3D Gaussian Splatting](https://arxiv.org/abs/2611.31918v1)**  
  Authors: Dawid Pająk, Martin Bisson, Rodolfo Lima, François Trudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31918v1.pdf)  
  Keywords: gaussian splatting, ar, fast, 3d gaussian  
- **[WildAnySplat: Feed-Forward 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2611.31023v1)**  
  Authors: Richard Shaw, Arthur Moreau, Athanasios Papaioannou, Thomas Tanay, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31023v1.pdf)  
  Keywords: gaussian splatting, illumination, fast, 3d gaussian, head, ar  
- **[PennyGS: Full Resolution 3DGS Training in Minutes on Consumer GPUs](https://arxiv.org/abs/2611.27525v1)**  
  Authors: Nicholas Jing Shou Nge, Yuang Shi, Geraldine Morin, Simone Gasparini, Anand Bhojan, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.27525v1.pdf)  
  Keywords: nerf, gaussian splatting, fast, 3d gaussian, ar  
- **[PRIO: Pre-trained Representation for Interactive Objects in 4D Worlds](https://arxiv.org/abs/2611.25500v1)**  
  Authors: Shixun Huang, Lifu Wei, Yue Chang, Chen Geng, Heng Zhang, Jinhyung Ahn, Caoliwen Wang, Siyuan Chen, Donglai Xiang, Jiajun Wu, Peter Yichen Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.25500v1.pdf)  
  Keywords: geometry, motion, 4d, fast, 3d gaussian, dynamic, ar  
- **[Facet-SLAM: Real-Time Triangle Splatting SLAM](https://arxiv.org/abs/2611.23935v1)**  
  Authors: Edward Beng Wai Tan, Siew-Kei Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.23935v1.pdf) | [![GitHub](https://img.shields.io/github/stars/edward62740/Facet-SLAM?style=social)](https://github.com/edward62740/Facet-SLAM)  
  Keywords: face, geometry, tracking, gaussian splatting, localization, fast, 3d gaussian, slam, ar  
- **[OCLDA-GS: Object-Centric Local Deformation-Aware Gaussian Streaming](https://arxiv.org/abs/2611.23416v1)**  
  Authors: Ashim Dahal, Nikesh Subedi, Rabab Abdelfattah, Nick Rahimi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.23416v1.pdf)  
  Keywords: motion, gaussian splatting, efficient, fast, 3d gaussian, dynamic, deformation, ar  
- **[DOOM-GS: Dynamic Out-of-core Optimization for Massive Gaussian Splatting](https://arxiv.org/abs/2611.22805v1)**  
  Authors: Doğa Yılmaz, Jialin Zhu, Binglun Wang, He Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.22805v1.pdf)  
  Keywords: gaussian splatting, fast, dynamic, high quality, ar  

### Applications

*Showing the latest 50 out of 500 papers*

- **[Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](https://arxiv.org/abs/2611.33145v1)**  
  Authors: Zehan Zheng, Yanyuan Chen, Deming Li, Yutao Tang, Jianwen Xie, Alan Yuille, Jieneng Chen, Cheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33145v1.pdf)  
  Keywords: gaussian splatting, localization, 3d gaussian, semantic, ar, outdoor  
- **[First-Hit Photoconsistency for Neural Surface Reconstruction](https://arxiv.org/abs/2611.32998v1)**  
  Authors: Gabriel Lenain, Edmond Boyer, Jean Ponce  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32998v1.pdf)  
  Keywords: face, geometry, gaussian splatting, efficient, ar  
- **[AnyPrune: Optimization-Free Pruning for Any Feedforward 3D Gaussian Splatting Pipeline](https://arxiv.org/abs/2611.32735v1)**  
  Authors: Nicola Leonetti, Federico Stella, Aoxiang Fan, Saqib Javed, Pascal Fua, Luigi Di Stefano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32735v1.pdf)  
  Keywords: gaussian splatting, ar, fast, 3d gaussian  
- **[Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation](https://arxiv.org/abs/2611.32718v1)**  
  Authors: Itai Mizlish, Boaz Ben-Moshe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32718v1.pdf) | [![GitHub](https://img.shields.io/github/stars/itaim18/DANIEL?style=social)](https://github.com/itaim18/DANIEL)  
  Keywords: fast, mapping, ar, slam, outdoor  
- **[Completion-Aware Compression for Progressive 3D Gaussian Splatting](https://arxiv.org/abs/2611.32628v1)**  
  Authors: Reagan Koo, Yeong-Gyu Kim, Eun-Seok Ryu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32628v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, large scene, 3d gaussian, compact, ar, compression  
- **[NRG-Twins: Pixel-Level Ground Truth for Rigidity Violations in Generated Videos](https://arxiv.org/abs/2611.32431v1)**  
  Authors: Chenrui Fan, Qiyang Hu, Luca Scharr, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32431v1.pdf)  
  Keywords: 3d reconstruction, ar, motion, segmentation  
- **[GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM](https://arxiv.org/abs/2611.32335v1)**  
  Authors: Weicong Zhang, Yuan Huang, Yu Zheng, Lin Chenxiao, Yingying Li, Lilong Fan, Liangdong Zhuang, Yufan Chen, Ruiping Liu, Junwei Zheng, Jiaming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32335v1.pdf)  
  Keywords: face, geometry, tracking, gaussian splatting, mapping, dynamic, slam, ar  
- **[ST-SfM: Spatio-Temporal Structure-from-Motion for Initialising 4D Gaussian Splatting](https://arxiv.org/abs/2611.32231v1)**  
  Authors: Harshit, Sami Brandt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32231v1.pdf)  
  Keywords: motion, gaussian splatting, 4d, dynamic, ar  
- **[SplatTok: Data-Driven Compression of 3D Gaussian Splats with Scene-Level Tokens](https://arxiv.org/abs/2611.32202v1)**  
  Authors: Sai Karthikey Pentapati, Shashank Nelamangala Sridhara, Birendra Kathariya, Peng Yin, Guandao Yang, Alan C. Bovik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32202v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, compact, compression, ar  
- **[View Management with Gaussian Placement and Opacity Regularization for Online 3DGS](https://arxiv.org/abs/2611.32025v1)**  
  Authors: Dong Hwi Kim, Park Sangwon, Chaehyeon Song, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32025v1.pdf)  
  Keywords: face, geometry, gaussian splatting, localization, 3d gaussian, mapping, slam, ar  

### Avatar Generation

*Showing the latest 50 out of 156 papers*

- **[First-Hit Photoconsistency for Neural Surface Reconstruction](https://arxiv.org/abs/2611.32998v1)**  
  Authors: Gabriel Lenain, Edmond Boyer, Jean Ponce  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32998v1.pdf)  
  Keywords: face, geometry, gaussian splatting, efficient, ar  
- **[GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM](https://arxiv.org/abs/2611.32335v1)**  
  Authors: Weicong Zhang, Yuan Huang, Yu Zheng, Lin Chenxiao, Yingying Li, Lilong Fan, Liangdong Zhuang, Yufan Chen, Ruiping Liu, Junwei Zheng, Jiaming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32335v1.pdf)  
  Keywords: face, geometry, tracking, gaussian splatting, mapping, dynamic, slam, ar  
- **[View Management with Gaussian Placement and Opacity Regularization for Online 3DGS](https://arxiv.org/abs/2611.32025v1)**  
  Authors: Dong Hwi Kim, Park Sangwon, Chaehyeon Song, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32025v1.pdf)  
  Keywords: face, geometry, gaussian splatting, localization, 3d gaussian, mapping, slam, ar  
- **[BendGS: Observation-Conditioned Gaussian Self-Modeling for Continuum Robots](https://arxiv.org/abs/2611.31844v1)**  
  Authors: Jeong Woon Lee, Doungjun Kim, Namho Kim, Seungheon Chae, Jongwoo Kim, Hyoseok Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31844v1.pdf)  
  Keywords: geometry, 3d gaussian, body, deformation, ar  
- **[HoloSplat: Real-Time Token Streaming for Feed-Forward Human Reconstruction](https://arxiv.org/abs/2611.31140v1)**  
  Authors: Chaofan Li, Qihan Ding, Shihan Wang, Zhehao Shen, Boyu Shen, Quanyu Chen, Haoyu Wu, Lan Xu, Xin Lou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31140v1.pdf)  
  Keywords: lightweight, geometry, human, 3d gaussian, ar, head, compression  
- **[WildAnySplat: Feed-Forward 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2611.31023v1)**  
  Authors: Richard Shaw, Arthur Moreau, Athanasios Papaioannou, Thomas Tanay, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31023v1.pdf)  
  Keywords: gaussian splatting, illumination, fast, 3d gaussian, head, ar  
- **[NNS-GS: Non-Local Neural Scattering for Relightable Gaussian Splatting](https://arxiv.org/abs/2611.30351v1)**  
  Authors: Shiyu Liang, Yang Gao, Lili Wang, Aimin Hao, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.30351v1.pdf)  
  Keywords: geometry, face, gaussian splatting, relightable, illumination, lighting, shadow, reflection, ar  
- **[Complementary Geometry in Gaussian Splatting](https://arxiv.org/abs/2611.29236v1)**  
  Authors: Mingle Jiang, Jikui Zhou, Chenghan Lyu, Rui Xu, Yunke Wang, Chang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.29236v1.pdf)  
  Keywords: face, geometry, gaussian splatting, dynamic, ar  
- **[VeilGS: Solving Darkness as a Veil of 2D Basis Maps over Retinex 3DGS](https://arxiv.org/abs/2611.27719v1)**  
  Authors: Mohab Kishawy, Chengzhou Tang, Shahram Shirani, Jun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.27719v1.pdf)  
  Keywords: face, gaussian splatting, efficient, 3d reconstruction, illumination, 3d gaussian, ar  
- **[CryoGaussian: Heterogeneous Cryo-EM Reconstruction Made Explicit with Gaussian Splatting](https://arxiv.org/abs/2611.26128v2)**  
  Authors: Ziwen Wang, Jiajun Fan, Chaoran Cheng, Ruihan Guo, Yanru Qu, Juexiao Zhou, Ge Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.26128v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/ZiwenWang28/CryoGaussian.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/ZiwenWang28/CryoGaussian)  
  Keywords: gaussian splatting, face, motion, ar  

### Dynamic Scene

*Showing the latest 50 out of 167 papers*

- **[NRG-Twins: Pixel-Level Ground Truth for Rigidity Violations in Generated Videos](https://arxiv.org/abs/2611.32431v1)**  
  Authors: Chenrui Fan, Qiyang Hu, Luca Scharr, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32431v1.pdf)  
  Keywords: 3d reconstruction, ar, motion, segmentation  
- **[GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM](https://arxiv.org/abs/2611.32335v1)**  
  Authors: Weicong Zhang, Yuan Huang, Yu Zheng, Lin Chenxiao, Yingying Li, Lilong Fan, Liangdong Zhuang, Yufan Chen, Ruiping Liu, Junwei Zheng, Jiaming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32335v1.pdf)  
  Keywords: face, geometry, tracking, gaussian splatting, mapping, dynamic, slam, ar  
- **[ST-SfM: Spatio-Temporal Structure-from-Motion for Initialising 4D Gaussian Splatting](https://arxiv.org/abs/2611.32231v1)**  
  Authors: Harshit, Sami Brandt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32231v1.pdf)  
  Keywords: motion, gaussian splatting, 4d, dynamic, ar  
- **[BendGS: Observation-Conditioned Gaussian Self-Modeling for Continuum Robots](https://arxiv.org/abs/2611.31844v1)**  
  Authors: Jeong Woon Lee, Doungjun Kim, Namho Kim, Seungheon Chae, Jongwoo Kim, Hyoseok Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31844v1.pdf)  
  Keywords: geometry, 3d gaussian, body, deformation, ar  
- **[InterGS+: Inter-Frame Gaussian Splatting Compression with Geometry-Aware Transformer Prediction and Adaptive Residual Coding](https://arxiv.org/abs/2611.31482v1)**  
  Authors: Muhammad Talha, Zhu Li, Joel Jung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31482v1.pdf)  
  Keywords: lightweight, geometry, gaussian splatting, efficient, 3d gaussian, ar, dynamic, compression  
- **[Tornado4D: Physics-Guided 4D Gaussian Reconstruction of a Laboratory Tornado from Sparse One-Sided Videos](https://arxiv.org/abs/2611.31435v1)**  
  Authors: Yucheng Zhu, Maria J. Molina, Christopher Metzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31435v1.pdf)  
  Keywords: geometry, motion, 3d reconstruction, 4d, understanding, ar  
- **[GSDet: Gaussian Splatting for Oriented Object Detection](https://arxiv.org/abs/2611.30602v1)**  
  Authors: Zeyu Ding, Jiaqi Zhao, Yong Zhou, Wen-liang Du, Hancheng Zhu, Rui Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.30602v1.pdf)  
  Keywords: gaussian splatting, ar, dynamic, 3d gaussian  
- **[JEPA-Shield: Safe Diffusion Planning with Latent World Models via Conformal Shielding](https://arxiv.org/abs/2611.29609v1)**  
  Authors: Taekyung Kim, Ege Yuceel, Steven Hong, Georgios Fainekos, Dimitra Panagou, Bardh Hoxha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.29609v1.pdf)  
  Keywords: geometry, motion, ar  
- **[Complementary Geometry in Gaussian Splatting](https://arxiv.org/abs/2611.29236v1)**  
  Authors: Mingle Jiang, Jikui Zhou, Chenghan Lyu, Rui Xu, Yunke Wang, Chang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.29236v1.pdf)  
  Keywords: face, geometry, gaussian splatting, dynamic, ar  
- **[ArgsWorld: Unifying 3DGS Scene Reconstruction, Generation and Extrapolation with Autoregressive Diffusion Transformer](https://arxiv.org/abs/2611.28792v1)**  
  Authors: Weiming Chen, Shuaiyan Liu, Xinyu Shao, Zhewen Chen, Tian Guan, Yonghong He, Xitong Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.28792v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://m4a1tastegood.github.io/ArgsWorld)  
  Keywords: gaussian splatting, 3d gaussian, dynamic, robotics, ar  

### Few-shot

- **[Enhancing Sparse-View Gaussian Splatting with Feed-Forward Priors via Spectral Fusion and Distillation](https://arxiv.org/abs/2611.31428v1)**  
  Authors: Weikai Lin, Jun Dai, Sheng Zhao, Junjie Zhao, Yuhao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31428v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://linwk20.github.io/spectral-fusion-gs)  
  Keywords: gaussian splatting, ar, sparse-view  
- **[Not All Directions Are Flat: Decomposed-Gradient Flatness for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2611.28802v1)**  
  Authors: Ungbae Yoon, Kwanyoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.28802v1.pdf)  
  Keywords: sparse-view, gaussian splatting, 3d gaussian, sparse view, robotics, ar  
- **[Stage-wise Lineage-aware Dropout for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2611.17752v1)**  
  Authors: Yan Xing, Zhi Chen, Fanglue Zhang, Junhong Zhao, Bing Xue, Mengjie Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.17752v1.pdf)  
  Keywords: nerf, geometry, sparse-view, gaussian splatting, 3d gaussian, ar  
- **[ThermalSplat: Generalizable Pose-Free Gaussian Splatting for Sparse-View Thermal 3D Reconstruction](https://arxiv.org/abs/2611.15435v1)**  
  Authors: Prasanna S, Gopi Raju Matta, Divya Madhuri Vemunuri, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.15435v1.pdf)  
  Keywords: sparse-view, gaussian splatting, efficient, 3d reconstruction, ar  
- **[A Reproducible Reconstruction and Evaluation Framework for Photorealistic Lunar Analog Scene Reconstruction Toward Digital Twins](https://arxiv.org/abs/2611.00870v1)**  
  Authors: Antar Mazumder, Ryan Hartzell, Luke Boyd, Alexander Robinson, Neha Sharma, Chance Carnival, Frances Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00870v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rose-lab-admin.github.io/rose-lunar-dt-rec)  
  Keywords: geometry, motion, gaussian splatting, human, 3d gaussian, sparse view, ar  
- **[P^2-Gaussian: Prior-Driven and Projection-Guided Gaussian Splatting for Sparse-View Cone-Beam CT Reconstruction](https://arxiv.org/abs/2610.39359v1)**  
  Authors: Jinqiu Xia, Jianhui Ma, Bin Ouyang, Xiaoyan Huang, Yuan Xu, Zun Piao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39359v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ballbo5354/P-2-Gaussian?style=social)](https://github.com/Ballbo5354/P-2-Gaussian)  
  Keywords: sparse-view, gaussian splatting, 3d gaussian, compact, ar  
- **[DUET4D: Self-Corrective Coupled Guidance for Sparse-View 4D Reconstruction](https://arxiv.org/abs/2610.35002v1)**  
  Authors: Beizhen Zhao, Nanjie Yao, Boyi Fu, Qingsong Yan, Haofan Ren, Kaiyong Zhao, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35002v1.pdf)  
  Keywords: gaussian splatting, 4d, ar, sparse-view  
- **[PixGR: Pixel-Space Generative Decoding for Fast Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2610.31908v1)**  
  Authors: Ranran Huang, Wenjing Bian, Weixun Luo, Ye Mao, Krystian Mikolajczyk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.31908v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ranrhuang.github.io/pixgr)  
  Keywords: lightweight, sparse-view, 3d reconstruction, efficient, fast, 3d gaussian, ar, compression  
- **[Rethinking Sparse-View 3D Gaussian Splatting: A Few-Shot Learning Perspective on Overfitting Prevention](https://arxiv.org/abs/2610.25887v1)**  
  Authors: Lejia Ye, Bin Wu, Jingjing Gao, Yiyang Wu, Xiaohu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25887v1.pdf)  
  Keywords: geometry, motion, sparse-view, gaussian splatting, vr, 3d gaussian, few-shot, dynamic, ar  
- **[Holi-Spatial 360: Generative Reconstruction from Sparse Panoramas for Spatial Rendering and Intelligence](https://arxiv.org/abs/2610.19502v1)**  
  Authors: Yuanyuan Gao, Zhirui Liu, Yuning Gong, Yifei Liu, Yifan Zhan, Kuixuan Jiao, Xiaolong Zhou, Yifan Yang, Hongjie Zhang, Xue Yang, Dan Xu, Zhihang Zhong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19502v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, semantic, sparse view, understanding, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 207 papers*

- **[First-Hit Photoconsistency for Neural Surface Reconstruction](https://arxiv.org/abs/2611.32998v1)**  
  Authors: Gabriel Lenain, Edmond Boyer, Jean Ponce  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32998v1.pdf)  
  Keywords: face, geometry, gaussian splatting, efficient, ar  
- **[Completion-Aware Compression for Progressive 3D Gaussian Splatting](https://arxiv.org/abs/2611.32628v1)**  
  Authors: Reagan Koo, Yeong-Gyu Kim, Eun-Seok Ryu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32628v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, large scene, 3d gaussian, compact, ar, compression  
- **[NRG-Twins: Pixel-Level Ground Truth for Rigidity Violations in Generated Videos](https://arxiv.org/abs/2611.32431v1)**  
  Authors: Chenrui Fan, Qiyang Hu, Luca Scharr, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32431v1.pdf)  
  Keywords: 3d reconstruction, ar, motion, segmentation  
- **[GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM](https://arxiv.org/abs/2611.32335v1)**  
  Authors: Weicong Zhang, Yuan Huang, Yu Zheng, Lin Chenxiao, Yingying Li, Lilong Fan, Liangdong Zhuang, Yufan Chen, Ruiping Liu, Junwei Zheng, Jiaming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32335v1.pdf)  
  Keywords: face, geometry, tracking, gaussian splatting, mapping, dynamic, slam, ar  
- **[View Management with Gaussian Placement and Opacity Regularization for Online 3DGS](https://arxiv.org/abs/2611.32025v1)**  
  Authors: Dong Hwi Kim, Park Sangwon, Chaehyeon Song, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32025v1.pdf)  
  Keywords: face, geometry, gaussian splatting, localization, 3d gaussian, mapping, slam, ar  
- **[BendGS: Observation-Conditioned Gaussian Self-Modeling for Continuum Robots](https://arxiv.org/abs/2611.31844v1)**  
  Authors: Jeong Woon Lee, Doungjun Kim, Namho Kim, Seungheon Chae, Jongwoo Kim, Hyoseok Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31844v1.pdf)  
  Keywords: geometry, 3d gaussian, body, deformation, ar  
- **[InterGS+: Inter-Frame Gaussian Splatting Compression with Geometry-Aware Transformer Prediction and Adaptive Residual Coding](https://arxiv.org/abs/2611.31482v1)**  
  Authors: Muhammad Talha, Zhu Li, Joel Jung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31482v1.pdf)  
  Keywords: lightweight, geometry, gaussian splatting, efficient, 3d gaussian, ar, dynamic, compression  
- **[Tornado4D: Physics-Guided 4D Gaussian Reconstruction of a Laboratory Tornado from Sparse One-Sided Videos](https://arxiv.org/abs/2611.31435v1)**  
  Authors: Yucheng Zhu, Maria J. Molina, Christopher Metzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31435v1.pdf)  
  Keywords: geometry, motion, 3d reconstruction, 4d, understanding, ar  
- **[HoloSplat: Real-Time Token Streaming for Feed-Forward Human Reconstruction](https://arxiv.org/abs/2611.31140v1)**  
  Authors: Chaofan Li, Qihan Ding, Shihan Wang, Zhehao Shen, Boyu Shen, Quanyu Chen, Haoyu Wu, Lan Xu, Xin Lou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31140v1.pdf)  
  Keywords: lightweight, geometry, human, 3d gaussian, ar, head, compression  
- **[NNS-GS: Non-Local Neural Scattering for Relightable Gaussian Splatting](https://arxiv.org/abs/2611.30351v1)**  
  Authors: Shiyu Liang, Yang Gao, Lili Wang, Aimin Hao, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.30351v1.pdf)  
  Keywords: geometry, face, gaussian splatting, relightable, illumination, lighting, shadow, reflection, ar  

### Large Scene

- **[Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](https://arxiv.org/abs/2611.33145v1)**  
  Authors: Zehan Zheng, Yanyuan Chen, Deming Li, Yutao Tang, Jianwen Xie, Alan Yuille, Jieneng Chen, Cheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33145v1.pdf)  
  Keywords: gaussian splatting, localization, 3d gaussian, semantic, ar, outdoor  
- **[Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation](https://arxiv.org/abs/2611.32718v1)**  
  Authors: Itai Mizlish, Boaz Ben-Moshe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32718v1.pdf) | [![GitHub](https://img.shields.io/github/stars/itaim18/DANIEL?style=social)](https://github.com/itaim18/DANIEL)  
  Keywords: fast, mapping, ar, slam, outdoor  
- **[Completion-Aware Compression for Progressive 3D Gaussian Splatting](https://arxiv.org/abs/2611.32628v1)**  
  Authors: Reagan Koo, Yeong-Gyu Kim, Eun-Seok Ryu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32628v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, large scene, 3d gaussian, compact, ar, compression  
- **[Mitigating SM-Level Load Imbalance in 3D Gaussian Splatting on GPUs](https://arxiv.org/abs/2611.12319v1)**  
  Authors: Junha Ryu, Hoi-Jun Yoo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.12319v1.pdf)  
  Keywords: lightweight, autonomous driving, gaussian splatting, urban scene, 3d gaussian, real-time rendering, ar  
- **[PLS-GS: Probabilistic Lidar Scaffolds for Compact, Surface-Aligned Gaussian Splatting](https://arxiv.org/abs/2611.10699v1)**  
  Authors: Krishnan Harikumar, Alejandro Fontan, Thierry Peynot, Emili Hernández, Niko Sünderhauf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.10699v1.pdf) | [![GitHub](https://img.shields.io/github/stars/k-harikumar/PLS-GS?style=social)](https://github.com/k-harikumar/PLS-GS)  
  Keywords: face, gaussian splatting, fast, 3d gaussian, mapping, compact, ar, robotics, outdoor  
- **[IGSW: Multi-Weather Urban Scene Reconstruction with Intrinsic-Decoupled Gaussian Splatting](https://arxiv.org/abs/2611.04374v1)**  
  Authors: Zhongquan Wang, Long Cao, Peijia Xie, Senlei Ma, Jie Li, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04374v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://akaxi6.github.io/IGSW)  
  Keywords: autonomous driving, gaussian splatting, 4d, urban scene, illumination, semantic, dynamic, high-fidelity, ar  
- **[DomeGS: Perceptually Consistent Background Completion for Unbounded 3D Gaussian Splatting in Virtual Reality](https://arxiv.org/abs/2610.37172v1)**  
  Authors: Anastasiya Pechko, Agata Szymańska, Piotr Borycki, Joanna Szelewska, Michał Mnich, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37172v1.pdf)  
  Keywords: geometry, gaussian splatting, vr, 3d gaussian, ar, high-fidelity, outdoor  
- **[D4GS: Efficient Gaussian Splatting SLAM with Depth Priors](https://arxiv.org/abs/2610.36853v2)**  
  Authors: Da Li, Yihan Zang, Ivan Viola, Zeyu Wang, Dominik Engel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36853v2.pdf)  
  Keywords: tracking, gaussian splatting, efficient, fast, ar, slam, outdoor  
- **[SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation](https://arxiv.org/abs/2610.36312v1)**  
  Authors: Ziang Guo, Didar Seyidov, Yixiao Zhou, Xuefeng Zhang, Ali Alridha Abdulkarim, Chen Min, Zufeng Zhang, Dzmitry Tsetserukou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36312v1.pdf)  
  Keywords: geometry, motion, tracking, gaussian splatting, 3d gaussian, mapping, ar, slam, outdoor  
- **[BoundedGS: Memory-Efficient High-Resolution Training for 3D Gaussian Splatting](https://arxiv.org/abs/2610.34233v1)**  
  Authors: Xiaobin Deng, Changyu Diao, Min Li, Duanqing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34233v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiaobin2001.github.io/BoundedGS-Web)  
  Keywords: gaussian splatting, efficient, 3d gaussian, compact, ar, outdoor  

### Model Compression

*Showing the latest 50 out of 183 papers*

- **[First-Hit Photoconsistency for Neural Surface Reconstruction](https://arxiv.org/abs/2611.32998v1)**  
  Authors: Gabriel Lenain, Edmond Boyer, Jean Ponce  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32998v1.pdf)  
  Keywords: face, geometry, gaussian splatting, efficient, ar  
- **[Completion-Aware Compression for Progressive 3D Gaussian Splatting](https://arxiv.org/abs/2611.32628v1)**  
  Authors: Reagan Koo, Yeong-Gyu Kim, Eun-Seok Ryu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32628v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, large scene, 3d gaussian, compact, ar, compression  
- **[SplatTok: Data-Driven Compression of 3D Gaussian Splats with Scene-Level Tokens](https://arxiv.org/abs/2611.32202v1)**  
  Authors: Sai Karthikey Pentapati, Shashank Nelamangala Sridhara, Birendra Kathariya, Peng Yin, Guandao Yang, Alan C. Bovik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32202v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, compact, compression, ar  
- **[InterGS+: Inter-Frame Gaussian Splatting Compression with Geometry-Aware Transformer Prediction and Adaptive Residual Coding](https://arxiv.org/abs/2611.31482v1)**  
  Authors: Muhammad Talha, Zhu Li, Joel Jung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31482v1.pdf)  
  Keywords: lightweight, geometry, gaussian splatting, efficient, 3d gaussian, ar, dynamic, compression  
- **[HoloSplat: Real-Time Token Streaming for Feed-Forward Human Reconstruction](https://arxiv.org/abs/2611.31140v1)**  
  Authors: Chaofan Li, Qihan Ding, Shihan Wang, Zhehao Shen, Boyu Shen, Quanyu Chen, Haoyu Wu, Lan Xu, Xin Lou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31140v1.pdf)  
  Keywords: lightweight, geometry, human, 3d gaussian, ar, head, compression  
- **[SemGuard: Semantics-Decoupled Watermarking for Gaussian Splatting](https://arxiv.org/abs/2611.28636v1)**  
  Authors: Yingying Shi, Zhong Zhou, Bin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.28636v1.pdf)  
  Keywords: gaussian splatting, efficient, semantic, dynamic, high-fidelity, ar  
- **[VeilGS: Solving Darkness as a Veil of 2D Basis Maps over Retinex 3DGS](https://arxiv.org/abs/2611.27719v1)**  
  Authors: Mohab Kishawy, Chengzhou Tang, Shahram Shirani, Jun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.27719v1.pdf)  
  Keywords: face, gaussian splatting, efficient, 3d reconstruction, illumination, 3d gaussian, ar  
- **[BladeR: Scalable, Shape-Guided 3D Reconstruction of Wind Turbine Blades from UAV Imagery](https://arxiv.org/abs/2611.27407v1)**  
  Authors: Jonathan Sterckx, Michiel Vlaminck, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.27407v1.pdf)  
  Keywords: gaussian splatting, efficient, 3d reconstruction, localization, lighting, ar  
- **[AGSR: Aperture-Guided Super-Resolution for Gaussian Splatting](https://arxiv.org/abs/2611.25934v1)**  
  Authors: Ayman Alkhateeb, Hadi Amirpour, Christian Timmerer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.25934v1.pdf)  
  Keywords: nerf, lightweight, gaussian splatting, 3d gaussian, ar  
- **[Multi-View Relighting with Mergeable Radiance Fields](https://arxiv.org/abs/2611.25523v1)**  
  Authors: Yinan Wang, Rohan Kadkol, Hyunjin Yoo, Jean-François Lalonde, James J. Clark  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.25523v1.pdf)  
  Keywords: nerf, geometry, gaussian splatting, efficient, lighting, 3d gaussian, ar, light transport, relighting  

### Quality Enhancement

- **[SemGuard: Semantics-Decoupled Watermarking for Gaussian Splatting](https://arxiv.org/abs/2611.28636v1)**  
  Authors: Yingying Shi, Zhong Zhou, Bin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.28636v1.pdf)  
  Keywords: gaussian splatting, efficient, semantic, dynamic, high-fidelity, ar  
- **[DOOM-GS: Dynamic Out-of-core Optimization for Massive Gaussian Splatting](https://arxiv.org/abs/2611.22805v1)**  
  Authors: Doğa Yılmaz, Jialin Zhu, Binglun Wang, He Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.22805v1.pdf)  
  Keywords: gaussian splatting, fast, dynamic, high quality, ar  
- **[RF3DGS: Reflection-Free 3D Gaussian Splatting with Self-Priors](https://arxiv.org/abs/2611.13772v2)**  
  Authors: Qiang Wen, Guotao Meng, Junhong Ruan, Hongyu Liu, Chenyang Lei, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.13772v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, reflection, high-fidelity, ar  
- **[Plant Orbiter: 3D Plant Reconstruction and Generation with Video Diffusion Orbit Cameras and 3D Gaussian Splatting](https://arxiv.org/abs/2611.12739v1)**  
  Authors: Zane K. J. Hartley, Yong En Kok, Lewis A. G. Stuart, Andrew P. French, Michael P. Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.12739v1.pdf)  
  Keywords: gaussian splatting, ar, high quality, 3d gaussian  
- **[URL-Sim: Unified and Regulated LiDAR Simulation for High-Fidelity Reconstruction of Dynamic Driving Scenes](https://arxiv.org/abs/2611.12932v1)**  
  Authors: Kefei Qian, Xipeng Feng, Jie Li, Long Cao, Yuhan Chen, Xiangfei Huang, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.12932v1.pdf)  
  Keywords: nerf, autonomous driving, geometry, gaussian splatting, 3d gaussian, dynamic, high-fidelity, ar  
- **[Perception Over Geometry: Rethinking Gaussian Allocation in Mesh-based Splatting](https://arxiv.org/abs/2611.07979v1)**  
  Authors: Yuting Wang, Yang Zhao, Shanding Diao, Penglin Wang, Yuan Chen, Wei Jia, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07979v1.pdf)  
  Keywords: geometry, face, gaussian splatting, 3d gaussian, compact, high quality, deformation, ar  
- **[Wide View Synthesis from Overlapping Perspective Cameras in Autonomous Driving](https://arxiv.org/abs/2611.07081v1)**  
  Authors: Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07081v1.pdf)  
  Keywords: autonomous driving, geometry, gaussian splatting, 3d gaussian, high-fidelity, ar  
- **[IGSW: Multi-Weather Urban Scene Reconstruction with Intrinsic-Decoupled Gaussian Splatting](https://arxiv.org/abs/2611.04374v1)**  
  Authors: Zhongquan Wang, Long Cao, Peijia Xie, Senlei Ma, Jie Li, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04374v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://akaxi6.github.io/IGSW)  
  Keywords: autonomous driving, gaussian splatting, 4d, urban scene, illumination, semantic, dynamic, high-fidelity, ar  
- **[EndoS3:Endoscopic Semantic Splatting SLAM](https://arxiv.org/abs/2611.04358v1)**  
  Authors: Mona Sheikh Zeinoddin, Benjamin Wright, Zafer Tandogdu, Greg Shaw, Evangelos Mazomenos, Danail Stoyanov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04358v1.pdf)  
  Keywords: motion, tracking, gaussian splatting, mapping, semantic, dynamic, understanding, deformation, high-fidelity, slam, ar  
- **[SettleSplat: Monocular Gaussian Mapping under In-View Scene Changes](https://arxiv.org/abs/2611.04195v1)**  
  Authors: Anh Thuan Tran, Xiyun Song, Yubin Zhou, Heather Yu, Jana Kosecka, Liang Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04195v1.pdf)  
  Keywords: fast, 3d gaussian, mapping, dynamic, high-fidelity, robotics, ar  

### Ray Tracing

- **[Neural Render Proxies for Interactive and Differentiable Lighting](https://arxiv.org/abs/2611.17185v1)**  
  Authors: Sergio Sancho, Alexander Rath, Marco Manzi, Pascal Chang, Amit H. Bermano, Derek Nowrouzezahrai, Markus Gross, Marios Papas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.17185v1.pdf)  
  Keywords: lightweight, path tracing, efficient, illumination, global illumination, fast, lighting, ar, animation, light transport, relighting  
- **[FastGRT: Accelerating Training of 3D Gaussian Ray Tracing](https://arxiv.org/abs/2611.11586v1)**  
  Authors: Meet Banthia, Xiaoteng Liu, Hexu Zhao, Aurojit Panda, Jinyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.11586v1.pdf)  
  Keywords: gaussian splatting, ray tracing, fast, 3d gaussian, ar  
- **[GraftRay: Physically Based Mesh Insertion into Gaussian Splatting Scenes via Path Tracing](https://arxiv.org/abs/2610.37036v3)**  
  Authors: Jinxin Ai, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37036v3.pdf)  
  Keywords: path tracing, gaussian splatting, shadow, lighting, 3d gaussian, reflection, ar  
- **[Spatial MIMO Channel Rendering: A 3D Gaussian Splatting Approach](https://arxiv.org/abs/2610.36880v1)**  
  Authors: Juntaek Han, Geonha Kim, Chaozheng Wen, Ahmed Alkhateeb, Jun Zhang, Jeonghun Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36880v1.pdf)  
  Keywords: gaussian splatting, ray tracing, fast, 3d gaussian, head, ar  
- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: gaussian splatting, efficient, ray tracing, lighting, 3d gaussian, head, ar  

### Relighting

- **[WildAnySplat: Feed-Forward 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2611.31023v1)**  
  Authors: Richard Shaw, Arthur Moreau, Athanasios Papaioannou, Thomas Tanay, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31023v1.pdf)  
  Keywords: gaussian splatting, illumination, fast, 3d gaussian, head, ar  
- **[NNS-GS: Non-Local Neural Scattering for Relightable Gaussian Splatting](https://arxiv.org/abs/2611.30351v1)**  
  Authors: Shiyu Liang, Yang Gao, Lili Wang, Aimin Hao, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.30351v1.pdf)  
  Keywords: geometry, face, gaussian splatting, relightable, illumination, lighting, shadow, reflection, ar  
- **[VeilGS: Solving Darkness as a Veil of 2D Basis Maps over Retinex 3DGS](https://arxiv.org/abs/2611.27719v1)**  
  Authors: Mohab Kishawy, Chengzhou Tang, Shahram Shirani, Jun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.27719v1.pdf)  
  Keywords: face, gaussian splatting, efficient, 3d reconstruction, illumination, 3d gaussian, ar  
- **[BladeR: Scalable, Shape-Guided 3D Reconstruction of Wind Turbine Blades from UAV Imagery](https://arxiv.org/abs/2611.27407v1)**  
  Authors: Jonathan Sterckx, Michiel Vlaminck, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.27407v1.pdf)  
  Keywords: gaussian splatting, efficient, 3d reconstruction, localization, lighting, ar  
- **[Multi-View Relighting with Mergeable Radiance Fields](https://arxiv.org/abs/2611.25523v1)**  
  Authors: Yinan Wang, Rohan Kadkol, Hyunjin Yoo, Jean-François Lalonde, James J. Clark  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.25523v1.pdf)  
  Keywords: nerf, geometry, gaussian splatting, efficient, lighting, 3d gaussian, ar, light transport, relighting  
- **[VideoRNG: Relightable Neural Gaussians from Generative Video Models](https://arxiv.org/abs/2611.25338v1)**  
  Authors: Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Ravi Ramamoorthi, Zahra Montazeri, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.25338v1.pdf)  
  Keywords: geometry, face, relightable, illumination, compact, light transport, ar  
- **[Beyond Appearance: Evidence-Guided Programmatic 3D Scene Reconstruction with Agentic Lighting Reasoning](https://arxiv.org/abs/2611.24565v1)**  
  Authors: Zeting Luo, Yifan Li, Shuai Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.24565v1.pdf)  
  Keywords: geometry, illumination, shadow, lighting, reflection, ar, relighting  
- **[Neural Render Proxies for Interactive and Differentiable Lighting](https://arxiv.org/abs/2611.17185v1)**  
  Authors: Sergio Sancho, Alexander Rath, Marco Manzi, Pascal Chang, Amit H. Bermano, Derek Nowrouzezahrai, Markus Gross, Marios Papas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.17185v1.pdf)  
  Keywords: lightweight, path tracing, efficient, illumination, global illumination, fast, lighting, ar, animation, light transport, relighting  
- **[Reconstruct What You Can: Distractor-free 4D Gaussian Splatting](https://arxiv.org/abs/2611.16259v1)**  
  Authors: Joel Julin, Liuyue Xie, Ananya Bal, Mose Sakashita, Koichiro Niinuma, Laszlo A. Jeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.16259v1.pdf)  
  Keywords: geometry, motion, gaussian splatting, 4d, shadow, dynamic, deformation, ar  
- **[FastWild-GS: Minutes-Scale In-the-Wild Gaussian Splatting via Compact Per-Image Appearance Adaptation](https://arxiv.org/abs/2611.13808v1)**  
  Authors: Donghun Ryu, Seokhyun Kim, Minhyeok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.13808v1.pdf)  
  Keywords: nerf, gaussian splatting, illumination, fast, compact, ar  

### SLAM

*Showing the latest 50 out of 71 papers*

- **[Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](https://arxiv.org/abs/2611.33145v1)**  
  Authors: Zehan Zheng, Yanyuan Chen, Deming Li, Yutao Tang, Jianwen Xie, Alan Yuille, Jieneng Chen, Cheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33145v1.pdf)  
  Keywords: gaussian splatting, localization, 3d gaussian, semantic, ar, outdoor  
- **[Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation](https://arxiv.org/abs/2611.32718v1)**  
  Authors: Itai Mizlish, Boaz Ben-Moshe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32718v1.pdf) | [![GitHub](https://img.shields.io/github/stars/itaim18/DANIEL?style=social)](https://github.com/itaim18/DANIEL)  
  Keywords: fast, mapping, ar, slam, outdoor  
- **[GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM](https://arxiv.org/abs/2611.32335v1)**  
  Authors: Weicong Zhang, Yuan Huang, Yu Zheng, Lin Chenxiao, Yingying Li, Lilong Fan, Liangdong Zhuang, Yufan Chen, Ruiping Liu, Junwei Zheng, Jiaming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32335v1.pdf)  
  Keywords: face, geometry, tracking, gaussian splatting, mapping, dynamic, slam, ar  
- **[View Management with Gaussian Placement and Opacity Regularization for Online 3DGS](https://arxiv.org/abs/2611.32025v1)**  
  Authors: Dong Hwi Kim, Park Sangwon, Chaehyeon Song, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32025v1.pdf)  
  Keywords: face, geometry, gaussian splatting, localization, 3d gaussian, mapping, slam, ar  
- **[BladeR: Scalable, Shape-Guided 3D Reconstruction of Wind Turbine Blades from UAV Imagery](https://arxiv.org/abs/2611.27407v1)**  
  Authors: Jonathan Sterckx, Michiel Vlaminck, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.27407v1.pdf)  
  Keywords: gaussian splatting, efficient, 3d reconstruction, localization, lighting, ar  
- **[Facet-SLAM: Real-Time Triangle Splatting SLAM](https://arxiv.org/abs/2611.23935v1)**  
  Authors: Edward Beng Wai Tan, Siew-Kei Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.23935v1.pdf) | [![GitHub](https://img.shields.io/github/stars/edward62740/Facet-SLAM?style=social)](https://github.com/edward62740/Facet-SLAM)  
  Keywords: face, geometry, tracking, gaussian splatting, localization, fast, 3d gaussian, slam, ar  
- **[ReTouchGS: Ultralight Render-free Aesthetic Color Enhancement and Transfer for 3D Gaussian Splatting](https://arxiv.org/abs/2611.23054v1)**  
  Authors: Chuanzhi Xu, Boyu Wei, Chengkun Yue, Xuanhua Yin, Yiyang Li, Haodong Chen, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.23054v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d gaussian, mapping, ar  
- **[CoSphere-SLAM: Multi-Agent Panoramic Gaussian Splatting SLAM with Spherical Loop Closure](https://arxiv.org/abs/2611.22235v2)**  
  Authors: Qi Shao, Zhihao Cao, Shuhao Zhai, Taoyu Wu, Zhuoxiao Li, Anh Nguyen, Long Hu, Xianzhi Li, Hong Liang, Liang Li, Baoru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.22235v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cosphere-slam.github.io)  
  Keywords: face, gaussian splatting, fast, mapping, head, slam, ar  
- **[QuantileGS: Quantile-Based Conformal Bounds on RGB Rendering Errors for Novel View Synthesis with 3D Gaussian Splatting](https://arxiv.org/abs/2611.21253v1)**  
  Authors: Haiyang Xu, Ziye Zhang, Bin Pan, Xia Xu, Zhenwei Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.21253v1.pdf)  
  Keywords: nerf, gaussian splatting, localization, 3d gaussian, mapping, ar  
- **[Prepare Lighter and Faster for Open-Vocabulary Queries: A Query-Wise 3D Segmenter for Gaussian Splatting](https://arxiv.org/abs/2611.19429v1)**  
  Authors: Nhat-Quynh Le-Pham, Khoi Nguyen, Binh-Son Hua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.19429v1.pdf)  
  Keywords: lightweight, gaussian splatting, efficient, localization, fast, 3d gaussian, segmentation, semantic, understanding, ar  

### Scene Understanding

*Showing the latest 50 out of 89 papers*

- **[Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild](https://arxiv.org/abs/2611.33145v1)**  
  Authors: Zehan Zheng, Yanyuan Chen, Deming Li, Yutao Tang, Jianwen Xie, Alan Yuille, Jieneng Chen, Cheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.33145v1.pdf)  
  Keywords: gaussian splatting, localization, 3d gaussian, semantic, ar, outdoor  
- **[NRG-Twins: Pixel-Level Ground Truth for Rigidity Violations in Generated Videos](https://arxiv.org/abs/2611.32431v1)**  
  Authors: Chenrui Fan, Qiyang Hu, Luca Scharr, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.32431v1.pdf)  
  Keywords: 3d reconstruction, ar, motion, segmentation  
- **[Tornado4D: Physics-Guided 4D Gaussian Reconstruction of a Laboratory Tornado from Sparse One-Sided Videos](https://arxiv.org/abs/2611.31435v1)**  
  Authors: Yucheng Zhu, Maria J. Molina, Christopher Metzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.31435v1.pdf)  
  Keywords: geometry, motion, 3d reconstruction, 4d, understanding, ar  
- **[SemGuard: Semantics-Decoupled Watermarking for Gaussian Splatting](https://arxiv.org/abs/2611.28636v1)**  
  Authors: Yingying Shi, Zhong Zhou, Bin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.28636v1.pdf)  
  Keywords: gaussian splatting, efficient, semantic, dynamic, high-fidelity, ar  
- **[A Hierarchical Onboard Vision-Language-Navigation Framework for Aerial Robots in Complex Environments](https://arxiv.org/abs/2611.23930v1)**  
  Authors: Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Zhaoqi Wang, Yuxin Fan, Wenjun Li, Kenghou Hoi, Zhichao Han, Xin Zhou, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wyz000.github.io/VLN-AR)  
  Keywords: lightweight, gaussian splatting, 3d gaussian, semantic, dynamic, ar  
- **[GaussianMamba: Geometric and Relational State Space Scanning of 3D Gaussian Primitives](https://arxiv.org/abs/2611.22742v1)**  
  Authors: A. Enes Doruk, Ozgur Erkent  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.22742v1.pdf)  
  Keywords: geometry, efficient, 3d gaussian, semantic, ar  
- **[The Mask Is Not the Object: Volumetric Supervision for 3D Gaussian Segmentation](https://arxiv.org/abs/2611.21383v1)**  
  Authors: Jeonghwan Cho, Minsu Kim, Junyoung Hong, Seon Joo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.21383v1.pdf)  
  Keywords: gaussian splatting, segmentation, ar, 3d gaussian  
- **[InterRSGaussian: Interactive Multi-view Instance Segmentation for 3D Remote Sensing Scenes](https://arxiv.org/abs/2611.20425v1)**  
  Authors: Zipeng Qi, Zhengxia Zou, Zhenwei Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.20425v1.pdf)  
  Keywords: segmentation, ar, understanding, 3d gaussian  
- **[SemLite-GS: Semantic-Selective Parallel Gaussian Splatting for Lightweight Building Reconstruction from UAV Oblique Imagery](https://arxiv.org/abs/2611.19773v1)**  
  Authors: Tengfei Wang, Xin Wang, Zihan Li, Quanjian Ji, Yifei Yu, Dong Lin, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.19773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRIS-LAB-whu/SemLite-GS?style=social)](https://github.com/IRIS-LAB-whu/SemLite-GS)  
  Keywords: lightweight, gaussian splatting, efficient, 3d gaussian, semantic, ar  
- **[Prepare Lighter and Faster for Open-Vocabulary Queries: A Query-Wise 3D Segmenter for Gaussian Splatting](https://arxiv.org/abs/2611.19429v1)**  
  Authors: Nhat-Quynh Le-Pham, Khoi Nguyen, Binh-Son Hua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.19429v1.pdf)  
  Keywords: lightweight, gaussian splatting, efficient, localization, fast, 3d gaussian, segmentation, semantic, understanding, ar  



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
