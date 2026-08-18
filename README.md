# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-08-18 00:37:17

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
- [Acceleration](#acceleration) (96 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (169 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (199 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (38 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (219 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (24 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (192 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (112 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (13 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (52 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (80 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (117 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys](https://arxiv.org/abs/2608.06404v1)**  
  Authors: Junxiong Zhou, Xuechen Li, Chonghao Qiu, Lang Qiao, Xiaowei Jia, Qi Yang, Chishan Zhang, Leikun Yin, Nanshan You, Vipin Kumar, David Mulla, Ce Yang, Zhenong Jin, Licheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06404v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://link-dev.github.io/UAV3DCrop)  
  Keywords: dynamic, 3d reconstruction, gaussian splatting, survey, 3d gaussian, nerf, geometry, ar  
- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: dynamic, efficient, high-fidelity, mapping, survey, ar, slam, tracking, 3d gaussian, localization  
- **[Recent Advances and Trends in Learning-based 3D Representations](https://arxiv.org/abs/2606.04871v1)**  
  Authors: Adrien Schockaert, Hamid Laga, Hazem Wannous, Vincent Magnier, Guillaume Dufaye, Jean-françois Witz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.04871v1.pdf)  
  Keywords: 4d, 3d reconstruction, medical, compact, gaussian splatting, survey, recognition, 3d gaussian, autonomous driving, motion, neural rendering, vr, ar  
- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137v1)**  
  Authors: Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00137v1.pdf)  
  Keywords: gaussian splatting, mapping, survey, animation, geometry, ar  

### Acceleration

*Showing the latest 50 out of 96 papers*

- **[GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting](https://arxiv.org/abs/2608.10938v1)**  
  Authors: Huaiyuan Weng, Chul Min Yeum, Su-Min Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10938v1.pdf)  
  Keywords: gaussian splatting, ar, outdoor, 3d gaussian, fast, geometry, localization  
- **[Compact Feed-Forward 3D Gaussians via Saliency-Guided Primitive Merging](https://arxiv.org/abs/2608.10712v1)**  
  Authors: Tim-Felix Fassch, Jochen Kall, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10712v1.pdf)  
  Keywords: efficient, compact, gaussian splatting, segmentation, 3d gaussian, fast, ar  
- **[ERF-GS: Reconstructing Fast Motion from Disjoint Event-RGB Viewpoints](https://arxiv.org/abs/2608.08531v1)**  
  Authors: Xiaoyang Bai, Zhenyang Li, Weiwei Xu, Edmund Y. Lam, Yifan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.08531v1.pdf) | [![GitHub](https://img.shields.io/github/stars/andrewbxy/ERF-GS?style=social)](https://github.com/andrewbxy/ERF-GS)  
  Keywords: dynamic, 4d, gaussian splatting, 3d gaussian, nerf, fast, motion, ar  
- **[Confidence matters: Leveraging Multi-view Geometric Priors for GS-based Reconstruction](https://arxiv.org/abs/2608.06117v1)**  
  Authors: Hongyu Zhou, Zorah Lähner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06117v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, motion, geometry, ar  
- **[ESVR: 3D Ellipsoid-based Sparse Volume Rendering via Structure-aware Primitive Learning and Per-primitive Ray Sampling](https://arxiv.org/abs/2608.05564v1)**  
  Authors: Suemin Jeon, Youjin Kim, Jungwoo Park, Kyungryun Lee, Won-Ki Jeong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05564v1.pdf)  
  Keywords: efficient, high-fidelity, compact, gaussian splatting, mapping, 3d gaussian, fast, real-time rendering, compression, vr, ar  
- **[Revisiting Pose Sensitivity in Splat-based Computed Tomography under Sparse-view Reconstruction](https://arxiv.org/abs/2608.04752v1)**  
  Authors: Kiseok Choi, Hyeongjun Cho, Inchul Kim, Min H. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04752v1.pdf)  
  Keywords: sparse-view, ar, 3d gaussian, fast, geometry, lightweight  
- **[PD-GS: Phoneme-Driven 3DGS for Audio-Driven Talking Heads](https://arxiv.org/abs/2608.05218v1)**  
  Authors: Ao Fu, Yi Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05218v1.pdf)  
  Keywords: dynamic, avatar, gaussian splatting, 3d gaussian, fast, motion, geometry, ar, head  
- **[FAST-GS: Frequency Aware Space-time Gaussian Splatting for Photorealistic Dynamic Novel View Synthesis](https://arxiv.org/abs/2608.01958v2)**  
  Authors: Zhengyang Zhang, Ziyu Lu, PengCheng Li, Hongbo Duan, Yi Liu, Pengting Luo, Peiyu Zhuang, Xinghui Li, Shaohua Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01958v2.pdf)  
  Keywords: dynamic, 3d reconstruction, 4d, efficient, gaussian splatting, fast, real-time rendering, motion, ar  
- **[G-Skin: Learning to Bind 3D Gaussians with Generative Visual Priors](https://arxiv.org/abs/2608.01726v1)**  
  Authors: Yuxin Yao, Kendong Liu, Shiqi Zhou, Jiazhi Xia, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01726v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yaoyx689.github.io/GSkin.html)  
  Keywords: efficient, high-fidelity, face, gaussian splatting, efficient rendering, 3d gaussian, motion, animation, geometry, ar  
- **[D^2-4DGS: Dual-Depth Guided Sparse-Camera 4D Gaussian Splatting](https://arxiv.org/abs/2608.01588v1)**  
  Authors: Jijian Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01588v1.pdf)  
  Keywords: dynamic, 4d, efficient, gaussian splatting, sparse-view, real-time rendering, geometry, ar  

### Applications

*Showing the latest 50 out of 498 papers*

- **[HiCo-GS: Hierarchical Context Aggregation and Geometric Consistency for Octree Gaussian Splatting](https://arxiv.org/abs/2608.14136v1)**  
  Authors: Wei Zhang, Shengkai Yu, Shiqiang Gong, Qi Zhang, Qiang Li, Qi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.14136v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WZ-CS/HiCo-GS?style=social)](https://github.com/WZ-CS/HiCo-GS)  
  Keywords: high-fidelity, gaussian splatting, ar, geometry, lightweight, head  
- **[GS$^{2}$CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via Large Vision Model Priors](https://arxiv.org/abs/2608.13502v1)**  
  Authors: Yanming Yang, Chenxi Song, Ping Wang, Xin Yuan, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13502v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, motion, ar  
- **[Splat-based Metal Artifact Reduction in Cone-Beam CT via Polychromatic Modeling](https://arxiv.org/abs/2608.13159v1)**  
  Authors: Kiseok Choi, Inchul Kim, Jaemin Cho, Hyeongjun Cho, Min H. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13159v1.pdf)  
  Keywords: efficient, high-fidelity, ar, gaussian splatting  
- **[ProbSplat: Efficient Probabilistic Hardware for Gaussian Splatting in 3D Scene Reconstruction](https://arxiv.org/abs/2608.13143v1)**  
  Authors: Siddarth Gottumukkula, M P Samartha, Vedant Pahariya, Priyanshi Jain, Amit Ranjan Trivedi, Priyesh Shukla  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13143v1.pdf)  
  Keywords: efficient, gaussian splatting, robotics, vr, ar  
- **[HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments](https://arxiv.org/abs/2608.12860v1)**  
  Authors: Quan-Dung Pham, Anh Dao, The-Anh Nguyen, Minh Nguyen-Dinh, Phuong Nam Dang, Tri Pham, Hung Tran, Bach Dao, Tuyen P. Le, Truong Nguyen, Quan Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.12860v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humanoid-vln.github.io)  
  Keywords: dynamic, body, human, gaussian splatting, 3d gaussian, motion, ar  
- **[LocusGS: Spatially Grounded Tokens for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2608.12825v1)**  
  Authors: Wenyu Li, Sidun Liu, Tongrui Hu, Peng Qiao, Yong Dou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.12825v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://leo-frank.github.io/LocusGS_viewer)  
  Keywords: 3d gaussian, ar, gaussian splatting  
- **[Seed2GS: Camera-Free, Training-Free Object Extraction from 3D Gaussian Scenes via a Single Reference-View Grounding](https://arxiv.org/abs/2608.11928v1)**  
  Authors: Zongjian Ding, Yudong Gao, Jiale Liu, Xinglin Yu, Junxing Ren, Dong Wei, Yajing Chen, Shan Huang, Mingjun Cheng, Min Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.11928v1.pdf)  
  Keywords: 3d gaussian, ar, tracking, gaussian splatting  
- **[CausalSplat: Towards Comprehensive Hierarchical Reasoning in 3D Gaussian Splatting](https://arxiv.org/abs/2608.11150v2)**  
  Authors: Jiayu Ding, Meilu Song, Yun Chen, Wei Gao, Ge Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.11150v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiayuding031020.github.io/CausalSplat)  
  Keywords: understanding, gaussian splatting, segmentation, 3d gaussian, ar  
- **[WildFireGS: Physics-Based Wildfire Simulation in Large-Scale Semantics-Enriched Gaussian Splatting Forest Scenes](https://arxiv.org/abs/2608.11100v1)**  
  Authors: Nienke Driessen, Joris Rijsdijk, Sören Pirk, Wojtek Palubicki, Dominik L. Michels, Michael Weinmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.11100v1.pdf)  
  Keywords: dynamic, gaussian splatting, 3d gaussian, semantic, ar  
- **[Learning Gaussian Structure: Intervention-Guided Density Control for Feed-Forward Driving Reconstruction](https://arxiv.org/abs/2608.11077v1)**  
  Authors: Hang Li, Jiahe Li, Meiying Gu, Jin Zheng, Lina Yu, Xiao Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.11077v1.pdf)  
  Keywords: efficient, compact, ar  

### Avatar Generation

*Showing the latest 50 out of 169 papers*

- **[HiCo-GS: Hierarchical Context Aggregation and Geometric Consistency for Octree Gaussian Splatting](https://arxiv.org/abs/2608.14136v1)**  
  Authors: Wei Zhang, Shengkai Yu, Shiqiang Gong, Qi Zhang, Qiang Li, Qi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.14136v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WZ-CS/HiCo-GS?style=social)](https://github.com/WZ-CS/HiCo-GS)  
  Keywords: high-fidelity, gaussian splatting, ar, geometry, lightweight, head  
- **[HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments](https://arxiv.org/abs/2608.12860v1)**  
  Authors: Quan-Dung Pham, Anh Dao, The-Anh Nguyen, Minh Nguyen-Dinh, Phuong Nam Dang, Tri Pham, Hung Tran, Bach Dao, Tuyen P. Le, Truong Nguyen, Quan Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.12860v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humanoid-vln.github.io)  
  Keywords: dynamic, body, human, gaussian splatting, 3d gaussian, motion, ar  
- **[Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting](https://arxiv.org/abs/2608.10756v1)**  
  Authors: Huosen Ou, Dongni Song, Yuncong Wang, Tao Zhou, Yiding Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10756v1.pdf)  
  Keywords: face, gaussian splatting, ar, 3d gaussian, semantic, few-shot, localization  
- **[Visual Geometry Foundation-Aware Gaussians for Single-Frame Surround-View Driving Reconstruction](https://arxiv.org/abs/2608.10682v1)**  
  Authors: Junhong Lin, Jinlong Wang, Xianda Guo, Yanlun Peng, Wei Zheng, Guoqing Liu, Hanli Wang, Tiesong Zhao, Wei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10682v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, geometry, ar  
- **[Gaussian Sculpting: End-to-End Controllable Surface Reconstruction via Field Optimization](https://arxiv.org/abs/2608.10602v1)**  
  Authors: Ke Jiaxin, Juncheng Liu, Yi Wang, Zhouhui Lian, Bin Liu, Shengfa Wang, Xiangjia He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10602v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, geometry, ar  
- **[EvTrajGS: Accurate and Efficient 3D Gaussian Splatting from Unposed Event Streams](https://arxiv.org/abs/2608.08585v1)**  
  Authors: Zixuan Chen, Jiakai Zhang, Junhao Dong, Guangcong Wang, Jianhuang Lai, Yew-Soon Ong, Xiaohua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.08585v1.pdf)  
  Keywords: dynamic, 3d reconstruction, efficient, gaussian splatting, mapping, slam, tracking, 3d gaussian, motion, ar, head  
- **[XClipGS: Exact Half-Space Clipping for Medical Volume Gaussian Splatting](https://arxiv.org/abs/2608.07760v1)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Chaoyi Zhou, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07760v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/XClipGS)  
  Keywords: medical, face, ar, gaussian splatting  
- **[Scenix: Sparse-View 3D Scene Reconstruction via Executable Scene Programs](https://arxiv.org/abs/2608.07012v1)**  
  Authors: Kai Li, Lutao Jiang, Zhenyang Li, Jiayu Dong, Jierui Zhang, Yingda Yin, Runze Zhang, Kai Yan, Xiaoyang Huang, Keyang Luo, Xin Wang, Xiangyu Zhao, Weikai Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07012v1.pdf)  
  Keywords: sparse-view, sparse view, ar, human  
- **[AdvTiles: Physical Adversarial Camouflage Clothing against Person Detectors via Learnable Tiles](https://arxiv.org/abs/2608.06801v1)**  
  Authors: Jinlei Wang, Jiahuan Long, Mingkai Sun, Yafei Guo, Yuanhao Huang, Ming Wang, Junqi Wu, Jiacheng Hou, Hongbo Chen, Xingxing Wei, Tingsong Jiang, Wen Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06801v1.pdf)  
  Keywords: body, gaussian splatting, 3d gaussian, illumination, ar  
- **[GSBF: Gaussian Splatting for Environment-Aware Beamforming](https://arxiv.org/abs/2608.05896v1)**  
  Authors: Yijie Bian, Wei Guo, Zixin Wang, Shenghui Song, Jun Zhang, Khaled B. Letaief  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05896v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, ar, head  

### Dynamic Scene

*Showing the latest 50 out of 199 papers*

- **[GS$^{2}$CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via Large Vision Model Priors](https://arxiv.org/abs/2608.13502v1)**  
  Authors: Yanming Yang, Chenxi Song, Ping Wang, Xin Yuan, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13502v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, motion, ar  
- **[HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments](https://arxiv.org/abs/2608.12860v1)**  
  Authors: Quan-Dung Pham, Anh Dao, The-Anh Nguyen, Minh Nguyen-Dinh, Phuong Nam Dang, Tri Pham, Hung Tran, Bach Dao, Tuyen P. Le, Truong Nguyen, Quan Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.12860v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://humanoid-vln.github.io)  
  Keywords: dynamic, body, human, gaussian splatting, 3d gaussian, motion, ar  
- **[WildFireGS: Physics-Based Wildfire Simulation in Large-Scale Semantics-Enriched Gaussian Splatting Forest Scenes](https://arxiv.org/abs/2608.11100v1)**  
  Authors: Nienke Driessen, Joris Rijsdijk, Sören Pirk, Wojtek Palubicki, Dominik L. Michels, Michael Weinmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.11100v1.pdf)  
  Keywords: dynamic, gaussian splatting, 3d gaussian, semantic, ar  
- **[CasDeblurGS: Cascaded 2D-to-3D Multi-View Consistency for 3D Gaussian Splatting from Two Blurry Images](https://arxiv.org/abs/2608.10345v1)**  
  Authors: Haeyun Choi, Minhyuk Jang, I-Gil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10345v1.pdf)  
  Keywords: gaussian splatting, sparse-view, 3d gaussian, nerf, motion, neural rendering, ar  
- **[HandSplatter: Automated Digital Goniometry from Neural Rendering](https://arxiv.org/abs/2608.09735v1)**  
  Authors: Emmett Chen, Neal Chen, Xiang Li, Quanzheng Li, Siyeop Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.09735v1.pdf)  
  Keywords: ar, motion, neural rendering  
- **[EvTrajGS: Accurate and Efficient 3D Gaussian Splatting from Unposed Event Streams](https://arxiv.org/abs/2608.08585v1)**  
  Authors: Zixuan Chen, Jiakai Zhang, Junhao Dong, Guangcong Wang, Jianhuang Lai, Yew-Soon Ong, Xiaohua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.08585v1.pdf)  
  Keywords: dynamic, 3d reconstruction, efficient, gaussian splatting, mapping, slam, tracking, 3d gaussian, motion, ar, head  
- **[ERF-GS: Reconstructing Fast Motion from Disjoint Event-RGB Viewpoints](https://arxiv.org/abs/2608.08531v1)**  
  Authors: Xiaoyang Bai, Zhenyang Li, Weiwei Xu, Edmund Y. Lam, Yifan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.08531v1.pdf) | [![GitHub](https://img.shields.io/github/stars/andrewbxy/ERF-GS?style=social)](https://github.com/andrewbxy/ERF-GS)  
  Keywords: dynamic, 4d, gaussian splatting, 3d gaussian, nerf, fast, motion, ar  
- **[Confidence matters: Leveraging Multi-view Geometric Priors for GS-based Reconstruction](https://arxiv.org/abs/2608.06117v1)**  
  Authors: Hongyu Zhou, Zorah Lähner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06117v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, motion, geometry, ar  
- **[NewtonGS: Physics-Structured Object-Level Neural Newtonian Dynamics for Gaussian Scene Animation](https://arxiv.org/abs/2608.07598v1)**  
  Authors: Lianlei Shan, Feiyang Ye, Yan Chen, Yong Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07598v1.pdf)  
  Keywords: dynamic, compact, 3d gaussian, motion, animation, deformation, ar  
- **[RORA: Realistic Object Reconstruction with Articulation](https://arxiv.org/abs/2608.04842v1)**  
  Authors: Hyesung Lee, Youngseon Lee, Kyutae Lee, Dongjun Lee, Yongseok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04842v1.pdf)  
  Keywords: dynamic, efficient, gaussian splatting, human, segmentation, tracking, 3d gaussian, nerf, motion, geometry, ar  

### Few-shot

- **[Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting](https://arxiv.org/abs/2608.10756v1)**  
  Authors: Huosen Ou, Dongni Song, Yuncong Wang, Tao Zhou, Yiding Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10756v1.pdf)  
  Keywords: face, gaussian splatting, ar, 3d gaussian, semantic, few-shot, localization  
- **[CasDeblurGS: Cascaded 2D-to-3D Multi-View Consistency for 3D Gaussian Splatting from Two Blurry Images](https://arxiv.org/abs/2608.10345v1)**  
  Authors: Haeyun Choi, Minhyuk Jang, I-Gil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10345v1.pdf)  
  Keywords: gaussian splatting, sparse-view, 3d gaussian, nerf, motion, neural rendering, ar  
- **[TRACE-GS: On-Policy Trajectory Distillation with Privileged Geometric Conditioning for Sparse-View 3DGS Restoration](https://arxiv.org/abs/2608.10286v1)**  
  Authors: Linlian Jiang, Yuchen Xi, Sadman Rakib Pinon, Ruigang Yang, Yang Wang, Xinxin Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10286v1.pdf)  
  Keywords: gaussian splatting, sparse-view, 3d gaussian, geometry, ar  
- **[Scenix: Sparse-View 3D Scene Reconstruction via Executable Scene Programs](https://arxiv.org/abs/2608.07012v1)**  
  Authors: Kai Li, Lutao Jiang, Zhenyang Li, Jiayu Dong, Jierui Zhang, Yingda Yin, Runze Zhang, Kai Yan, Xiaoyang Huang, Keyang Luo, Xin Wang, Xiangyu Zhao, Weikai Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07012v1.pdf)  
  Keywords: sparse-view, sparse view, ar, human  
- **[Objects as Audio-Visual Modal Sound Fields](https://arxiv.org/abs/2608.05145v2)**  
  Authors: Zisen Shao, Zihao Wei, Derong Jin, Ruohan Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05145v2.pdf)  
  Keywords: 3d reconstruction, compact, gaussian splatting, ar, 3d gaussian, few-shot, geometry, localization  
- **[Revisiting Pose Sensitivity in Splat-based Computed Tomography under Sparse-view Reconstruction](https://arxiv.org/abs/2608.04752v1)**  
  Authors: Kiseok Choi, Hyeongjun Cho, Inchul Kim, Min H. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04752v1.pdf)  
  Keywords: sparse-view, ar, 3d gaussian, fast, geometry, lightweight  
- **[CLEAR: Conflict-aware Learning via Evidence-guided Adaptive Routing for Unified Sparse-View 3D Gaussian Super-Resolution](https://arxiv.org/abs/2608.02206v1)**  
  Authors: Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02206v1.pdf)  
  Keywords: 3d gaussian, sparse-view, ar, gaussian splatting  
- **[D^2-4DGS: Dual-Depth Guided Sparse-Camera 4D Gaussian Splatting](https://arxiv.org/abs/2608.01588v1)**  
  Authors: Jijian Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01588v1.pdf)  
  Keywords: dynamic, 4d, efficient, gaussian splatting, sparse-view, real-time rendering, geometry, ar  
- **[GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian Splatting with Graph Optimization](https://arxiv.org/abs/2608.01492v1)**  
  Authors: Baihan Yang, Tiexin Li, Yuheng Liu, Xin Lin, Xinke Li, Xiaohui Xie, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01492v1.pdf)  
  Keywords: human, gaussian splatting, ar, 3d gaussian, sparse view, lightweight, head  
- **[Manifold-GS: Certified Hybrid Assets via Varifold-Conservative Gaussian Splatting](https://arxiv.org/abs/2608.00214v1)**  
  Authors: Boyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00214v1.pdf)  
  Keywords: face, gaussian splatting, sparse-view, 3d gaussian, geometry, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 219 papers*

- **[HiCo-GS: Hierarchical Context Aggregation and Geometric Consistency for Octree Gaussian Splatting](https://arxiv.org/abs/2608.14136v1)**  
  Authors: Wei Zhang, Shengkai Yu, Shiqiang Gong, Qi Zhang, Qiang Li, Qi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.14136v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WZ-CS/HiCo-GS?style=social)](https://github.com/WZ-CS/HiCo-GS)  
  Keywords: high-fidelity, gaussian splatting, ar, geometry, lightweight, head  
- **[GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting](https://arxiv.org/abs/2608.10938v1)**  
  Authors: Huaiyuan Weng, Chul Min Yeum, Su-Min Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10938v1.pdf)  
  Keywords: gaussian splatting, ar, outdoor, 3d gaussian, fast, geometry, localization  
- **[Visual Geometry Foundation-Aware Gaussians for Single-Frame Surround-View Driving Reconstruction](https://arxiv.org/abs/2608.10682v1)**  
  Authors: Junhong Lin, Jinlong Wang, Xianda Guo, Yanlun Peng, Wei Zheng, Guoqing Liu, Hanli Wang, Tiesong Zhao, Wei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10682v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, geometry, ar  
- **[Gaussian Sculpting: End-to-End Controllable Surface Reconstruction via Field Optimization](https://arxiv.org/abs/2608.10602v1)**  
  Authors: Ke Jiaxin, Juncheng Liu, Yi Wang, Zhouhui Lian, Bin Liu, Shengfa Wang, Xiangjia He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10602v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, geometry, ar  
- **[TRACE-GS: On-Policy Trajectory Distillation with Privileged Geometric Conditioning for Sparse-View 3DGS Restoration](https://arxiv.org/abs/2608.10286v1)**  
  Authors: Linlian Jiang, Yuchen Xi, Sadman Rakib Pinon, Ruigang Yang, Yang Wang, Xinxin Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10286v1.pdf)  
  Keywords: gaussian splatting, sparse-view, 3d gaussian, geometry, ar  
- **[EndoMD-SLAM: Endoscopic Gaussian Splatting SLAM under Optical Degradation with Memory and Static-Transient Decomposition](https://arxiv.org/abs/2608.08949v1)**  
  Authors: Nuo Chen, Kangqi Ni, Lulin Liu, Joga Ivatury, Ying Ding, Farshid Alambeigi, Tianlong Chen, Zhiwen Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.08949v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, mapping, ar, slam, tracking, geometry, localization  
- **[EvTrajGS: Accurate and Efficient 3D Gaussian Splatting from Unposed Event Streams](https://arxiv.org/abs/2608.08585v1)**  
  Authors: Zixuan Chen, Jiakai Zhang, Junhao Dong, Guangcong Wang, Jianhuang Lai, Yew-Soon Ong, Xiaohua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.08585v1.pdf)  
  Keywords: dynamic, 3d reconstruction, efficient, gaussian splatting, mapping, slam, tracking, 3d gaussian, motion, ar, head  
- **[FlexSplat: Flexible Feed-Forward 3D Gaussian Splatting without Point Cloud Correspondence](https://arxiv.org/abs/2608.07937v1)**  
  Authors: Amir Sabbaghziarani, Hanting Ye, Maria Gorlatova, Yi Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07937v1.pdf)  
  Keywords: compact, gaussian splatting, 3d gaussian, geometry, ar  
- **[InstanceSplat: Instance-Aware Feed-Forward 3D Gaussian Splatting for Scene Understanding](https://arxiv.org/abs/2608.07144v1)**  
  Authors: Minchao Jiang, Xiaoxuan Ma, Shunyu Jia, Haoru Wang, Zhang Liang, Wentao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07144v1.pdf)  
  Keywords: 3d reconstruction, efficient, understanding, gaussian splatting, segmentation, 3d gaussian, semantic, geometry, ar  
- **[Confidence matters: Leveraging Multi-view Geometric Priors for GS-based Reconstruction](https://arxiv.org/abs/2608.06117v1)**  
  Authors: Hongyu Zhou, Zorah Lähner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06117v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, motion, geometry, ar  

### Large Scene

- **[GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting](https://arxiv.org/abs/2608.10938v1)**  
  Authors: Huaiyuan Weng, Chul Min Yeum, Su-Min Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10938v1.pdf)  
  Keywords: gaussian splatting, ar, outdoor, 3d gaussian, fast, geometry, localization  
- **[OutLangSplat: 3D Language Gaussian Splatting for UAV Outdoor Scenes](https://arxiv.org/abs/2608.04560v1)**  
  Authors: Xia Yan, He Wu, Yanghui Xu, Zizhao Wu, Jiazhou Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04560v1.pdf)  
  Keywords: efficient, understanding, gaussian splatting, ar, outdoor, segmentation, 3d gaussian, semantic, localization  
- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: gaussian splatting, mapping, localization, ar, outdoor, slam, tracking, 3d gaussian, geometry, lightweight  
- **[Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering](https://arxiv.org/abs/2607.19893v1)**  
  Authors: Zhenxiang Ma, Zeyu He, Yuanzhen Zhou, Zhenyu Yang, Yuchang Zhang, Miao Tao, Rong Fu, Jidong Zhai, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19893v1.pdf)  
  Keywords: head, ar, neural rendering, large scene  
- **[AniGS: Bridging Rendering and Diffusion Prior for 3D Scene Animation](https://arxiv.org/abs/2607.18539v1)**  
  Authors: Yen-Chi Cheng, Chen Gao, Chuhan Chen, Tuotuo Li, Rajvi Shah, Ayush Saraf, Changil Kim, Liangyan Gui, Alexander Schwing, Johannes Kopf, Hung-Yu Tseng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18539v1.pdf)  
  Keywords: dynamic, gaussian splatting, outdoor, 3d gaussian, motion, animation, deformation, ar  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: dynamic, mapping, outdoor, tracking, 3d gaussian, motion, geometry, illumination, ar, vr  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: efficient, gaussian splatting, slam, large scene, 3d gaussian, recognition, fast, real-time rendering, motion, ar  
- **[GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors](https://arxiv.org/abs/2607.11184v1)**  
  Authors: Ruilan Gao, Letian Jin, Yu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11184v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rlgao.github.io/geogs_slam)  
  Keywords: gaussian splatting, mapping, outdoor, slam, tracking, 3d gaussian, geometry, ar  
- **[Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction](https://arxiv.org/abs/2607.08769v1)**  
  Authors: Weijian Chen, Weibo Yao, Yuhang Zhang, Xiaolin Tang, Guo Wang, Weijun Zhang, Xitong Gao, Yihao Chen, Hongde Qin, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08769v1.pdf)  
  Keywords: gaussian splatting, outdoor, 3d gaussian, geometry, ar  
- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771v1)**  
  Authors: Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03771v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/VOP-GS)  
  Keywords: efficient, face, gaussian splatting, large scene, 3d gaussian, geometry, sparse view, ar  

### Model Compression

*Showing the latest 50 out of 192 papers*

- **[HiCo-GS: Hierarchical Context Aggregation and Geometric Consistency for Octree Gaussian Splatting](https://arxiv.org/abs/2608.14136v1)**  
  Authors: Wei Zhang, Shengkai Yu, Shiqiang Gong, Qi Zhang, Qiang Li, Qi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.14136v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WZ-CS/HiCo-GS?style=social)](https://github.com/WZ-CS/HiCo-GS)  
  Keywords: high-fidelity, gaussian splatting, ar, geometry, lightweight, head  
- **[GS$^{2}$CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via Large Vision Model Priors](https://arxiv.org/abs/2608.13502v1)**  
  Authors: Yanming Yang, Chenxi Song, Ping Wang, Xin Yuan, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13502v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, motion, ar  
- **[Splat-based Metal Artifact Reduction in Cone-Beam CT via Polychromatic Modeling](https://arxiv.org/abs/2608.13159v1)**  
  Authors: Kiseok Choi, Inchul Kim, Jaemin Cho, Hyeongjun Cho, Min H. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13159v1.pdf)  
  Keywords: efficient, high-fidelity, ar, gaussian splatting  
- **[ProbSplat: Efficient Probabilistic Hardware for Gaussian Splatting in 3D Scene Reconstruction](https://arxiv.org/abs/2608.13143v1)**  
  Authors: Siddarth Gottumukkula, M P Samartha, Vedant Pahariya, Priyanshi Jain, Amit Ranjan Trivedi, Priyesh Shukla  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13143v1.pdf)  
  Keywords: efficient, gaussian splatting, robotics, vr, ar  
- **[Learning Gaussian Structure: Intervention-Guided Density Control for Feed-Forward Driving Reconstruction](https://arxiv.org/abs/2608.11077v1)**  
  Authors: Hang Li, Jiahe Li, Meiying Gu, Jin Zheng, Lina Yu, Xiao Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.11077v1.pdf)  
  Keywords: efficient, compact, ar  
- **[Compact Feed-Forward 3D Gaussians via Saliency-Guided Primitive Merging](https://arxiv.org/abs/2608.10712v1)**  
  Authors: Tim-Felix Fassch, Jochen Kall, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10712v1.pdf)  
  Keywords: efficient, compact, gaussian splatting, segmentation, 3d gaussian, fast, ar  
- **[JSGS: JPEG State-Guided Supervision for 3D Gaussian Splatting from Mixed-Quality Views](https://arxiv.org/abs/2608.08659v1)**  
  Authors: Jinhua Cui, Anhong Wang, Kai Hu, Donghan Bu, Peihao Li, Tammam Tillo, Hao Jing, Shiao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.08659v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Jayden-Cui/JSGS?style=social)](https://github.com/Jayden-Cui/JSGS)  
  Keywords: 3d gaussian, compression, ar, gaussian splatting  
- **[EvTrajGS: Accurate and Efficient 3D Gaussian Splatting from Unposed Event Streams](https://arxiv.org/abs/2608.08585v1)**  
  Authors: Zixuan Chen, Jiakai Zhang, Junhao Dong, Guangcong Wang, Jianhuang Lai, Yew-Soon Ong, Xiaohua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.08585v1.pdf)  
  Keywords: dynamic, 3d reconstruction, efficient, gaussian splatting, mapping, slam, tracking, 3d gaussian, motion, ar, head  
- **[FlexSplat: Flexible Feed-Forward 3D Gaussian Splatting without Point Cloud Correspondence](https://arxiv.org/abs/2608.07937v1)**  
  Authors: Amir Sabbaghziarani, Hanting Ye, Maria Gorlatova, Yi Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07937v1.pdf)  
  Keywords: compact, gaussian splatting, 3d gaussian, geometry, ar  
- **[InstanceSplat: Instance-Aware Feed-Forward 3D Gaussian Splatting for Scene Understanding](https://arxiv.org/abs/2608.07144v1)**  
  Authors: Minchao Jiang, Xiaoxuan Ma, Shunyu Jia, Haoru Wang, Zhang Liang, Wentao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07144v1.pdf)  
  Keywords: 3d reconstruction, efficient, understanding, gaussian splatting, segmentation, 3d gaussian, semantic, geometry, ar  

### Quality Enhancement

*Showing the latest 50 out of 112 papers*

- **[HiCo-GS: Hierarchical Context Aggregation and Geometric Consistency for Octree Gaussian Splatting](https://arxiv.org/abs/2608.14136v1)**  
  Authors: Wei Zhang, Shengkai Yu, Shiqiang Gong, Qi Zhang, Qiang Li, Qi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.14136v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WZ-CS/HiCo-GS?style=social)](https://github.com/WZ-CS/HiCo-GS)  
  Keywords: high-fidelity, gaussian splatting, ar, geometry, lightweight, head  
- **[Splat-based Metal Artifact Reduction in Cone-Beam CT via Polychromatic Modeling](https://arxiv.org/abs/2608.13159v1)**  
  Authors: Kiseok Choi, Inchul Kim, Jaemin Cho, Hyeongjun Cho, Min H. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13159v1.pdf)  
  Keywords: efficient, high-fidelity, ar, gaussian splatting  
- **[ESVR: 3D Ellipsoid-based Sparse Volume Rendering via Structure-aware Primitive Learning and Per-primitive Ray Sampling](https://arxiv.org/abs/2608.05564v1)**  
  Authors: Suemin Jeon, Youjin Kim, Jungwoo Park, Kyungryun Lee, Won-Ki Jeong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05564v1.pdf)  
  Keywords: efficient, high-fidelity, compact, gaussian splatting, mapping, 3d gaussian, fast, real-time rendering, compression, vr, ar  
- **[Multi-View Face and Gesture Animation with Dynamic Gaussians](https://arxiv.org/abs/2608.04722v1)**  
  Authors: Alireza Javanmardi, Vippin Kumar Jeetmal, Christen Millerdurai, Alain Pagani, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04722v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dfki-av.github.io/MVFGA)  
  Keywords: dynamic, high-fidelity, face, avatar, body, human, 3d gaussian, motion, animation, ar, head  
- **[UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models](https://arxiv.org/abs/2608.04701v1)**  
  Authors: Haiyang Zhou, Wangbo Yu, Chaoran Feng, Xunyu Zhou, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04701v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, 3d gaussian, nerf, motion, ar  
- **[ACA-GS: Adaptive-Capacity Anchored Gaussian Splatting for Compact Dynamic Radiance Fields](https://arxiv.org/abs/2608.04581v1)**  
  Authors: Seunghyeon Song, Joo Chan Lee, Chanung Park, Jun Young Jeong, Minseo Lee, Eunbyung Park, Jong Hwan Ko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04581v1.pdf)  
  Keywords: dynamic, 4d, high-fidelity, compact, gaussian splatting, ar, motion, compression, lightweight  
- **[3D Gaussian Splatting and Mesh-Based Digital Twins: An Exploratory Study for Virtual Reality Tourism](https://arxiv.org/abs/2608.01969v1)**  
  Authors: Maximilian Warsinke, Francesco Vona, Abm Tariqul Islam, Tanja Kojić, Jan-Niklas Voigt-Antons, Sebastian Möller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01969v1.pdf)  
  Keywords: understanding, high-fidelity, gaussian splatting, 3d gaussian, motion, vr, ar  
- **[DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing](https://arxiv.org/abs/2608.01761v1)**  
  Authors: Siying Li, Ying Ni, Jie Sun, Jian Sun, Haotian Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01761v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, relighting, 3d gaussian, lighting, semantic, autonomous driving, neural rendering, compression, illumination, ar  
- **[G-Skin: Learning to Bind 3D Gaussians with Generative Visual Priors](https://arxiv.org/abs/2608.01726v1)**  
  Authors: Yuxin Yao, Kendong Liu, Shiqi Zhou, Jiazhi Xia, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01726v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yaoyx689.github.io/GSkin.html)  
  Keywords: efficient, high-fidelity, face, gaussian splatting, efficient rendering, 3d gaussian, motion, animation, geometry, ar  
- **[QuerySplat: Decoupling Geometry and Appearance Representations in 3DGS Prediction](https://arxiv.org/abs/2608.01186v1)**  
  Authors: Yinglong Li, Donghui Shen, Xiaoyu Zhang, Zhichao Ye, Hongyu Wu, Aimin Hao, Guofeng Zhang, Haomin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01186v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://inspatio.github.io/querysplat)  
  Keywords: 3d reconstruction, efficient, high-fidelity, understanding, gaussian splatting, 3d gaussian, geometry, ar  

### Ray Tracing

- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: efficient, face, ray tracing, relighting, gaussian splatting, reflection, lighting, illumination, ar  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: dynamic, high-fidelity, face, ray tracing, gaussian splatting, human, reflection, 3d gaussian, motion, geometry, ar  
- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: compact, ray casting, human, gaussian splatting, geometry, ar  
- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869v1)**  
  Authors: Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30869v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gray)  
  Keywords: ray tracing, gaussian splatting, 3d gaussian, fast, ar  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: efficient, ray tracing, gaussian splatting, reflection, path tracing, 3d gaussian, fast, real-time rendering, geometry, ar  
- **[RenderFormer++: Scalable and Physics-Informed Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v2)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v2.pdf)  
  Keywords: compact, global illumination, neural rendering, illumination, ar, light transport  
- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: 3d reconstruction, efficient, gaussian splatting, 3d gaussian, global illumination, geometry, illumination, ar  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, global illumination, illumination, ar  
- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314v1)**  
  Authors: Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11314v1.pdf)  
  Keywords: dynamic, 3d reconstruction, ray tracing, relighting, ar, 3d gaussian, lighting, motion, neural rendering, geometry, lightweight, light transport  
- **[PTIR-GS: Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606v3)**  
  Authors: Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09606v3.pdf)  
  Keywords: compact, shadow, ray tracing, relighting, reflection, path tracing, 3d gaussian, lighting, global illumination, illumination, ar, light transport  

### Relighting

*Showing the latest 50 out of 52 papers*

- **[AdvTiles: Physical Adversarial Camouflage Clothing against Person Detectors via Learnable Tiles](https://arxiv.org/abs/2608.06801v1)**  
  Authors: Jinlei Wang, Jiahuan Long, Mingkai Sun, Yafei Guo, Yuanhao Huang, Ming Wang, Junqi Wu, Jiacheng Hou, Hongbo Chen, Xingxing Wei, Tingsong Jiang, Wen Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06801v1.pdf)  
  Keywords: body, gaussian splatting, 3d gaussian, illumination, ar  
- **[DerainSplat: Feed-Forward Clean 3D Gaussian Splatting from Sparse Rainy Views](https://arxiv.org/abs/2608.02191v1)**  
  Authors: Fuzhen Jiang, Changyue Shi, Chuxiao Yang, Xinyuan Hu, Wenjie Ye, Minghao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02191v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, autonomous driving, geometry, illumination, ar  
- **[DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing](https://arxiv.org/abs/2608.01761v1)**  
  Authors: Siying Li, Ying Ni, Jie Sun, Jian Sun, Haotian Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01761v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, relighting, 3d gaussian, lighting, semantic, autonomous driving, neural rendering, compression, illumination, ar  
- **[Endo-NeRF++: Uncertainty-Aware Neural Rendering with Multi-Resolution Hash Encoding for Dynamic Surgical Scene Reconstruction](https://arxiv.org/abs/2607.27825v3)**  
  Authors: Gousia Habib, Laura Ruotsalainen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.27825v3.pdf)  
  Keywords: dynamic, reflection, nerf, neural rendering, deformation, ar  
- **[PanoLess: Environment Reconstruction from Partial Reflective Views](https://arxiv.org/abs/2607.25362v1)**  
  Authors: Ahitagni Das, Ashok Veeraraghavan, Vivek Boominathan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25362v1.pdf)  
  Keywords: high-fidelity, face, reflection, illumination, ar  
- **[Meshless Domain Randomization via Explicit Parameter Perturbation of 3D Gaussian Splatting](https://arxiv.org/abs/2607.22890v1)**  
  Authors: Felipe Nunes Carbone de Carvalho, Joyce de Morais Souza, Alan de Aguiar, Charles Morphy D. Santos, João Paulo Gois  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22890v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, illumination, ar  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: efficient, face, ray tracing, relighting, gaussian splatting, reflection, lighting, illumination, ar  
- **[Visual Relocalization from Sparse Views in Aliased and Low-Texture Environments via Novel View Synthesis](https://arxiv.org/abs/2607.22147v1)**  
  Authors: Maria Peribañez, Javier Civera, Rudolph Triebel, Riccardo Giubilato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22147v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DLR-RM/multimodal-gsplat-relocalization?style=social)](https://github.com/DLR-RM/multimodal-gsplat-relocalization)  
  Keywords: gaussian splatting, ar, 3d gaussian, motion, sparse view, geometry, illumination, localization  
- **[ECoNGS: Efficient Compressive Neural Gaussian Splats for Volume Visualization](https://arxiv.org/abs/2607.18466v1)**  
  Authors: Kaiyuan Tang, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18466v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/ECoNGS?style=social)](https://github.com/TouKaienn/ECoNGS)  
  Keywords: dynamic, efficient, compact, gaussian splatting, ar, lighting, vr, lightweight  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: dynamic, mapping, outdoor, tracking, 3d gaussian, motion, geometry, illumination, ar, vr  

### SLAM

*Showing the latest 50 out of 80 papers*

- **[Seed2GS: Camera-Free, Training-Free Object Extraction from 3D Gaussian Scenes via a Single Reference-View Grounding](https://arxiv.org/abs/2608.11928v1)**  
  Authors: Zongjian Ding, Yudong Gao, Jiale Liu, Xinglin Yu, Junxing Ren, Dong Wei, Yajing Chen, Shan Huang, Mingjun Cheng, Min Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.11928v1.pdf)  
  Keywords: 3d gaussian, ar, tracking, gaussian splatting  
- **[GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting](https://arxiv.org/abs/2608.10938v1)**  
  Authors: Huaiyuan Weng, Chul Min Yeum, Su-Min Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10938v1.pdf)  
  Keywords: gaussian splatting, ar, outdoor, 3d gaussian, fast, geometry, localization  
- **[Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting](https://arxiv.org/abs/2608.10756v1)**  
  Authors: Huosen Ou, Dongni Song, Yuncong Wang, Tao Zhou, Yiding Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10756v1.pdf)  
  Keywords: face, gaussian splatting, ar, 3d gaussian, semantic, few-shot, localization  
- **[EndoMD-SLAM: Endoscopic Gaussian Splatting SLAM under Optical Degradation with Memory and Static-Transient Decomposition](https://arxiv.org/abs/2608.08949v1)**  
  Authors: Nuo Chen, Kangqi Ni, Lulin Liu, Joga Ivatury, Ying Ding, Farshid Alambeigi, Tianlong Chen, Zhiwen Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.08949v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, mapping, ar, slam, tracking, geometry, localization  
- **[EvTrajGS: Accurate and Efficient 3D Gaussian Splatting from Unposed Event Streams](https://arxiv.org/abs/2608.08585v1)**  
  Authors: Zixuan Chen, Jiakai Zhang, Junhao Dong, Guangcong Wang, Jianhuang Lai, Yew-Soon Ong, Xiaohua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.08585v1.pdf)  
  Keywords: dynamic, 3d reconstruction, efficient, gaussian splatting, mapping, slam, tracking, 3d gaussian, motion, ar, head  
- **[ESVR: 3D Ellipsoid-based Sparse Volume Rendering via Structure-aware Primitive Learning and Per-primitive Ray Sampling](https://arxiv.org/abs/2608.05564v1)**  
  Authors: Suemin Jeon, Youjin Kim, Jungwoo Park, Kyungryun Lee, Won-Ki Jeong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05564v1.pdf)  
  Keywords: efficient, high-fidelity, compact, gaussian splatting, mapping, 3d gaussian, fast, real-time rendering, compression, vr, ar  
- **[Objects as Audio-Visual Modal Sound Fields](https://arxiv.org/abs/2608.05145v2)**  
  Authors: Zisen Shao, Zihao Wei, Derong Jin, Ruohan Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05145v2.pdf)  
  Keywords: 3d reconstruction, compact, gaussian splatting, ar, 3d gaussian, few-shot, geometry, localization  
- **[RORA: Realistic Object Reconstruction with Articulation](https://arxiv.org/abs/2608.04842v1)**  
  Authors: Hyesung Lee, Youngseon Lee, Kyutae Lee, Dongjun Lee, Yongseok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04842v1.pdf)  
  Keywords: dynamic, efficient, gaussian splatting, human, segmentation, tracking, 3d gaussian, nerf, motion, geometry, ar  
- **[OutLangSplat: 3D Language Gaussian Splatting for UAV Outdoor Scenes](https://arxiv.org/abs/2608.04560v1)**  
  Authors: Xia Yan, He Wu, Yanghui Xu, Zizhao Wu, Jiazhou Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04560v1.pdf)  
  Keywords: efficient, understanding, gaussian splatting, ar, outdoor, segmentation, 3d gaussian, semantic, localization  
- **[TRACE: Ergodic Trajectory Optimization for Active Scene Reconstruction](https://arxiv.org/abs/2608.02304v3)**  
  Authors: Ziyue Zheng, Linli Shi, Bingkun He, Wen Jiang, Ziyun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02304v3.pdf) | [![GitHub](https://img.shields.io/github/stars/spikelab-jhu/trace-active-reconstruction?style=social)](https://github.com/spikelab-jhu/trace-active-reconstruction)  
  Keywords: mapping, efficient, ar  

### Scene Understanding

*Showing the latest 50 out of 117 papers*

- **[CausalSplat: Towards Comprehensive Hierarchical Reasoning in 3D Gaussian Splatting](https://arxiv.org/abs/2608.11150v2)**  
  Authors: Jiayu Ding, Meilu Song, Yun Chen, Wei Gao, Ge Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.11150v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiayuding031020.github.io/CausalSplat)  
  Keywords: understanding, gaussian splatting, segmentation, 3d gaussian, ar  
- **[WildFireGS: Physics-Based Wildfire Simulation in Large-Scale Semantics-Enriched Gaussian Splatting Forest Scenes](https://arxiv.org/abs/2608.11100v1)**  
  Authors: Nienke Driessen, Joris Rijsdijk, Sören Pirk, Wojtek Palubicki, Dominik L. Michels, Michael Weinmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.11100v1.pdf)  
  Keywords: dynamic, gaussian splatting, 3d gaussian, semantic, ar  
- **[Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting](https://arxiv.org/abs/2608.10756v1)**  
  Authors: Huosen Ou, Dongni Song, Yuncong Wang, Tao Zhou, Yiding Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10756v1.pdf)  
  Keywords: face, gaussian splatting, ar, 3d gaussian, semantic, few-shot, localization  
- **[Compact Feed-Forward 3D Gaussians via Saliency-Guided Primitive Merging](https://arxiv.org/abs/2608.10712v1)**  
  Authors: Tim-Felix Fassch, Jochen Kall, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10712v1.pdf)  
  Keywords: efficient, compact, gaussian splatting, segmentation, 3d gaussian, fast, ar  
- **[LEGO: Leveled Language Gaussian Splatting](https://arxiv.org/abs/2608.10057v1)**  
  Authors: Yuning Peng, Haiping Wang, Yuan Liu, Yipeng Lu, Zhen Dong, Bisheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10057v1.pdf)  
  Keywords: understanding, gaussian splatting, segmentation, recognition, semantic, ar  
- **[InstanceSplat: Instance-Aware Feed-Forward 3D Gaussian Splatting for Scene Understanding](https://arxiv.org/abs/2608.07144v1)**  
  Authors: Minchao Jiang, Xiaoxuan Ma, Shunyu Jia, Haoru Wang, Zhang Liang, Wentao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07144v1.pdf)  
  Keywords: 3d reconstruction, efficient, understanding, gaussian splatting, segmentation, 3d gaussian, semantic, geometry, ar  
- **[CDSeg: A Renderable Gaussian Carrier for Image-to-3D Label Transfer](https://arxiv.org/abs/2608.05482v1)**  
  Authors: Wentao Sun, Yiping Chen, Zhengsen Xu, Jonathan Li, John S. Zelek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05482v1.pdf)  
  Keywords: face, gaussian splatting, segmentation, semantic, ar  
- **[RORA: Realistic Object Reconstruction with Articulation](https://arxiv.org/abs/2608.04842v1)**  
  Authors: Hyesung Lee, Youngseon Lee, Kyutae Lee, Dongjun Lee, Yongseok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04842v1.pdf)  
  Keywords: dynamic, efficient, gaussian splatting, human, segmentation, tracking, 3d gaussian, nerf, motion, geometry, ar  
- **[EmpaAva: An Open-source Agentic 3D-Avatar Empathetic Live Chatbot](https://arxiv.org/abs/2608.04709v1)**  
  Authors: Jie Yang, Wenhao Xu, Shuhui Lin, Hao Fei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04709v1.pdf)  
  Keywords: understanding, face, avatar, human, 3d gaussian, motion, ar  
- **[OutLangSplat: 3D Language Gaussian Splatting for UAV Outdoor Scenes](https://arxiv.org/abs/2608.04560v1)**  
  Authors: Xia Yan, He Wu, Yanghui Xu, Zizhao Wu, Jiazhou Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04560v1.pdf)  
  Keywords: efficient, understanding, gaussian splatting, ar, outdoor, segmentation, 3d gaussian, semantic, localization  



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
