# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-08-30 02:20:55

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

- [3DGS Surveys](#3dgs-surveys) (5 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (93 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (171 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (204 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (40 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (229 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (21 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (197 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (103 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (15 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (49 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (83 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (116 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: illumination, gaussian splatting, ar, motion, survey, geometry, 3d reconstruction  
- **[UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys](https://arxiv.org/abs/2608.06404v1)**  
  Authors: Junxiong Zhou, Xuechen Li, Chonghao Qiu, Lang Qiao, Xiaowei Jia, Qi Yang, Chishan Zhang, Leikun Yin, Nanshan You, Vipin Kumar, David Mulla, Ce Yang, Zhenong Jin, Licheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06404v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://link-dev.github.io/UAV3DCrop)  
  Keywords: gaussian splatting, 3d gaussian, dynamic, ar, nerf, survey, geometry, 3d reconstruction  
- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: localization, efficient, tracking, mapping, 3d gaussian, dynamic, ar, survey, slam, high-fidelity  
- **[Recent Advances and Trends in Learning-based 3D Representations](https://arxiv.org/abs/2606.04871v1)**  
  Authors: Adrien Schockaert, Hamid Laga, Hazem Wannous, Vincent Magnier, Guillaume Dufaye, Jean-françois Witz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.04871v1.pdf)  
  Keywords: vr, medical, compact, gaussian splatting, 3d gaussian, recognition, motion, ar, survey, autonomous driving, 4d, 3d reconstruction, neural rendering  
- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137v1)**  
  Authors: Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00137v1.pdf)  
  Keywords: mapping, gaussian splatting, ar, survey, geometry, animation  

### Acceleration

*Showing the latest 50 out of 93 papers*

- **[GaussianWAM: Distilling Geometry and Semantics from 3D Gaussian Fields into World-Action Models](https://arxiv.org/abs/2608.24714v1)**  
  Authors: Zijian Zhang, Yuqing Jiang, Weitao Zhou, Minglei Li, Jinhao Zhang, Yao Mu, Xiaofan Li, Hao Zhao, Haibao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24714v1.pdf)  
  Keywords: head, fast, 3d gaussian, dynamic, semantic, ar, geometry  
- **[Fast and Compact 3D Gaussian Splatting with Polarized Opacity Prior](https://arxiv.org/abs/2608.22344v1)**  
  Authors: Zi-Ming Wang, Kai-Wen Duan, Kowei Huang, Akihiro Sugimoto, Shang-Hong Lai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22344v1.pdf)  
  Keywords: efficient, compact, fast, gaussian splatting, 3d gaussian, ar  
- **[Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)**  
  Authors: Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/vorotracing)  
  Keywords: real-time rendering, face, ray tracing, compact, fast, gaussian splatting, 3d gaussian, ar, motion, nerf  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: shadow, reflection, efficient, ray tracing, mapping, compact, fast, gaussian splatting, 3d gaussian, ar, nerf  
- **[RoofGS: Roofline-Guided End-to-End Acceleration of 3D Gaussian Splatting](https://arxiv.org/abs/2608.15785v1)**  
  Authors: Yang Luo, Yan Gong, Yongsheng Gao, Jie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.15785v1.pdf)  
  Keywords: acceleration, compact, fast, gaussian splatting, 3d gaussian, ar  
- **[GaussMemory: Task-Driven 3D Gaussian Scene Memory for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2608.14986v1)**  
  Authors: Zhiqiang Hu, Shouren Huang, Masatoshi Ishikawa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.14986v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, fast  
- **[GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting](https://arxiv.org/abs/2608.10938v2)**  
  Authors: Huaiyuan Weng, Chul Min Yeum, Su-Min Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10938v2.pdf)  
  Keywords: localization, outdoor, fast, gaussian splatting, 3d gaussian, ar, geometry  
- **[Compact Feed-Forward 3D Gaussians via Saliency-Guided Primitive Merging](https://arxiv.org/abs/2608.10712v2)**  
  Authors: Tim-Felix Fassch, Jochen Kall, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10712v2.pdf)  
  Keywords: efficient, compact, fast, gaussian splatting, 3d gaussian, ar, segmentation  
- **[ERF-GS: Reconstructing Fast Motion from Disjoint Event-RGB Viewpoints](https://arxiv.org/abs/2608.08531v1)**  
  Authors: Xiaoyang Bai, Zhenyang Li, Weiwei Xu, Edmund Y. Lam, Yifan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.08531v1.pdf) | [![GitHub](https://img.shields.io/github/stars/andrewbxy/ERF-GS?style=social)](https://github.com/andrewbxy/ERF-GS)  
  Keywords: fast, gaussian splatting, dynamic, 3d gaussian, motion, nerf, ar, 4d  
- **[Confidence matters: Leveraging Multi-view Geometric Priors for GS-based Reconstruction](https://arxiv.org/abs/2608.06117v1)**  
  Authors: Hongyu Zhou, Zorah Lähner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06117v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, 3d gaussian, ar, motion, geometry  

### Applications

*Showing the latest 50 out of 498 papers*

- **[KnockGS:interaction-Grounded Calibrationof Physical Gaussian Representations](https://arxiv.org/abs/2608.27365v1)**  
  Authors: Chenchen Ge, Hanwen Shen, Bowen Jing, Jiyuan Cai, Xiaofeng Wang, Hongsen Lei, Weitao Zhou, Dandan Zhang, Haibao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.27365v1.pdf)  
  Keywords: 3d gaussian, dynamic, ar  
- **[Comparative Evaluation of 3D Reconstruction Methods for Immersive Visualization of Laboratory Objects](https://arxiv.org/abs/2608.27301v1)**  
  Authors: Brian De La Cruz, Aaron Y. Zhao, Maitrey Gramopadhye, Sawyer J. Lazar, Xianming Tan, Daniel Szafir, David S. Lawrence  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.27301v1.pdf)  
  Keywords: gaussian splatting, ar, nerf, 3d reconstruction, high-fidelity  
- **[Per-View Gaussian Predictions Enable Training-Free Distractor Filtering in Feed-Forward 3DGS](https://arxiv.org/abs/2608.26951v1)**  
  Authors: Kangmin Seo, Jae-Pil Heo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26951v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, 3d reconstruction  
- **[KISS-GS: 3D Gaussian Splatting Compression Kept Simple](https://arxiv.org/abs/2608.26948v1)**  
  Authors: Wieland Morgenstern, Friedrich Elias Branschke, Florian Fleischmann, Adrian Szatmari, Paul Schlack, Florian Barthel, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26948v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fraunhoferhhi.github.io/KISS-GS)  
  Keywords: compact, gaussian splatting, ar, 3d gaussian, compression  
- **[CGS-SLAM: Collaborative Gaussian Splatting based SLAM for Multi-Agent Reconstruction](https://arxiv.org/abs/2608.26868v1)**  
  Authors: Jean-Daniel de Ambrogi, Aladine Chetouani, Vincent Nguyen, Aurélien Chateigner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26868v1.pdf)  
  Keywords: tracking, mapping, gaussian splatting, dynamic, ar, motion, slam  
- **[CoGeo-GS: Concept-Driven and Geometry-Aware Multi-Object Removal in 3D Scenes](https://arxiv.org/abs/2608.26656v1)**  
  Authors: Yuanxiang Ni, Xianliang Huang, Chenhang Ma, Chen Xiao, Yuewen Ma, Ruxin Wang, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26656v1.pdf)  
  Keywords: gaussian splatting, semantic, 3d gaussian, ar, geometry  
- **[Cross-Platform Benchmark of Neural 3D Reconstruction for Autonomous Laboratory Robots](https://arxiv.org/abs/2608.26383v1)**  
  Authors: Yongho Kim, Mengjiao Han, Victor Mateevitsi, Silvio Rizzi, Michael E. Papka, Nicola Ferrier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26383v1.pdf)  
  Keywords: tracking, lightweight, gaussian splatting, 3d gaussian, ar, nerf, geometry, 3d reconstruction  
- **[4DGS-WAM: Bridging Past and Future with an Object-Centric World Action Model based on 4D Gaussian Splatting](https://arxiv.org/abs/2608.25956v1)**  
  Authors: Yueen Ma, Zenglin Xu, Irwin King  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25956v1.pdf)  
  Keywords: gaussian splatting, dynamic, 4d, ar  
- **[GaussianDream++: Efficient 3D Gaussian World Modeling for Robotic Manipulation](https://arxiv.org/abs/2608.25659v1)**  
  Authors: Yuqing Jiang, Zijian Zhang, Weitao Zhou, Jiawei Wang, Junjie He, Lei Yang, Haifang Qing, Si Liu, Ding Zhao, Ping Luo, Haibao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25659v1.pdf)  
  Keywords: efficient, head, compact, 3d gaussian, dynamic, ar, motion, geometry  
- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: illumination, gaussian splatting, ar, motion, survey, geometry, 3d reconstruction  

### Avatar Generation

*Showing the latest 50 out of 171 papers*

- **[GaussianDream++: Efficient 3D Gaussian World Modeling for Robotic Manipulation](https://arxiv.org/abs/2608.25659v1)**  
  Authors: Yuqing Jiang, Zijian Zhang, Weitao Zhou, Jiawei Wang, Junjie He, Lei Yang, Haifang Qing, Si Liu, Ding Zhao, Ping Luo, Haibao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25659v1.pdf)  
  Keywords: efficient, head, compact, 3d gaussian, dynamic, ar, motion, geometry  
- **[GaussianWAM: Distilling Geometry and Semantics from 3D Gaussian Fields into World-Action Models](https://arxiv.org/abs/2608.24714v1)**  
  Authors: Zijian Zhang, Yuqing Jiang, Weitao Zhou, Minglei Li, Jinhao Zhang, Yao Mu, Xiaofan Li, Hao Zhao, Haibao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24714v1.pdf)  
  Keywords: head, fast, 3d gaussian, dynamic, semantic, ar, geometry  
- **[GaussVLA: Geometry-Aware Spatial Reasoning for Vision-Language-Action Model](https://arxiv.org/abs/2608.24959v1)**  
  Authors: Md Selim Sarowar, Md Tanvir Islam, Sungho Kim, Sangtae Ahn  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24959v1.pdf)  
  Keywords: efficient, face, compact, 3d gaussian, semantic, ar, geometry  
- **[Physics-Integrated Operator Learning via Gaussian Splatting Representations](https://arxiv.org/abs/2608.24049v1)**  
  Authors: Jihao Zhang, Junyi Guo, Jian-Xun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24049v1.pdf)  
  Keywords: efficient, face, gaussian splatting, ar, dynamic  
- **[Source-Face Authenticity Detection for 3D Gaussian Heads Reconstructed from a Single Portrait: A Benchmark and Dedicated Detector](https://arxiv.org/abs/2608.23984v1)**  
  Authors: Yujie Gao, Zijian Yu, Yan Hong, Jun Lan, Jianfu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23984v1.pdf)  
  Keywords: ar, 3d gaussian, head, face  
- **[Photorealistic Novel View Synthesis of Human Faces using Next-Scale Transformers](https://arxiv.org/abs/2608.23410v1)**  
  Authors: Federico Stella, Fei Jiang, Zhongshi Jiang, Zohar Barzelay, Emanuel Garbin, Amin Jourabloo, Liuhao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23410v1.pdf)  
  Keywords: 3d gaussian, ar, face, human  
- **[Learning Spherical Occupancy Profiles for Multi-View 3D Reconstruction and Generation](https://arxiv.org/abs/2608.23206v2)**  
  Authors: YiHsuan Tsai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23206v2.pdf)  
  Keywords: face, head, compact, 3d gaussian, ar, 3d reconstruction  
- **[SACHA: Semantic-Aware Compression for 3D Gaussian Head Avatars](https://arxiv.org/abs/2608.23133v1)**  
  Authors: Zihan Zhang, Shanzhi Yin, Xinju Wu, Bolin Chen, Ru-Ling Liao, Jie Chen, Shiqi Wang, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23133v1.pdf)  
  Keywords: efficient, head, compact, 3d gaussian, dynamic, compression, motion, semantic, ar, avatar, high-fidelity  
- **[Seeing the Unseen: Semantic-in-Gaussian for Sparse-View 3D Generalization](https://arxiv.org/abs/2608.22740v1)**  
  Authors: Zeyang Bai, Yunpeng Wang, Yunbiao Wang, Jun Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22740v1.pdf)  
  Keywords: efficient, face, compact, gaussian splatting, 3d gaussian, semantic, sparse-view, ar  
- **[In-Situ Reconstruction of the International Space Station Using 3D Gaussian Splatting and Astrobee](https://arxiv.org/abs/2608.21685v1)**  
  Authors: Hudson Kim, Ryan Soussan, Brian Coltin, Jordan Kam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21685v1.pdf)  
  Keywords: human, mapping, gaussian splatting, 3d gaussian, ar, nerf, 3d reconstruction, high-fidelity  

### Dynamic Scene

*Showing the latest 50 out of 204 papers*

- **[KnockGS:interaction-Grounded Calibrationof Physical Gaussian Representations](https://arxiv.org/abs/2608.27365v1)**  
  Authors: Chenchen Ge, Hanwen Shen, Bowen Jing, Jiyuan Cai, Xiaofeng Wang, Hongsen Lei, Weitao Zhou, Dandan Zhang, Haibao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.27365v1.pdf)  
  Keywords: 3d gaussian, dynamic, ar  
- **[CGS-SLAM: Collaborative Gaussian Splatting based SLAM for Multi-Agent Reconstruction](https://arxiv.org/abs/2608.26868v1)**  
  Authors: Jean-Daniel de Ambrogi, Aladine Chetouani, Vincent Nguyen, Aurélien Chateigner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26868v1.pdf)  
  Keywords: tracking, mapping, gaussian splatting, dynamic, ar, motion, slam  
- **[4DGS-WAM: Bridging Past and Future with an Object-Centric World Action Model based on 4D Gaussian Splatting](https://arxiv.org/abs/2608.25956v1)**  
  Authors: Yueen Ma, Zenglin Xu, Irwin King  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25956v1.pdf)  
  Keywords: gaussian splatting, dynamic, 4d, ar  
- **[GaussianDream++: Efficient 3D Gaussian World Modeling for Robotic Manipulation](https://arxiv.org/abs/2608.25659v1)**  
  Authors: Yuqing Jiang, Zijian Zhang, Weitao Zhou, Jiawei Wang, Junjie He, Lei Yang, Haifang Qing, Si Liu, Ding Zhao, Ping Luo, Haibao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25659v1.pdf)  
  Keywords: efficient, head, compact, 3d gaussian, dynamic, ar, motion, geometry  
- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: illumination, gaussian splatting, ar, motion, survey, geometry, 3d reconstruction  
- **[GaussianWAM: Distilling Geometry and Semantics from 3D Gaussian Fields into World-Action Models](https://arxiv.org/abs/2608.24714v1)**  
  Authors: Zijian Zhang, Yuqing Jiang, Weitao Zhou, Minglei Li, Jinhao Zhang, Yao Mu, Xiaofan Li, Hao Zhao, Haibao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24714v1.pdf)  
  Keywords: head, fast, 3d gaussian, dynamic, semantic, ar, geometry  
- **[Physics-Integrated Operator Learning via Gaussian Splatting Representations](https://arxiv.org/abs/2608.24049v1)**  
  Authors: Jihao Zhang, Junyi Guo, Jian-Xun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24049v1.pdf)  
  Keywords: efficient, face, gaussian splatting, ar, dynamic  
- **[FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors](https://arxiv.org/abs/2608.23549v1)**  
  Authors: Khiem Vuong, Deva Ramanan, Srinivasa Narasimhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23549v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, motion, nerf  
- **[SACHA: Semantic-Aware Compression for 3D Gaussian Head Avatars](https://arxiv.org/abs/2608.23133v1)**  
  Authors: Zihan Zhang, Shanzhi Yin, Xinju Wu, Bolin Chen, Ru-Ling Liao, Jie Chen, Shiqi Wang, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23133v1.pdf)  
  Keywords: efficient, head, compact, 3d gaussian, dynamic, compression, motion, semantic, ar, avatar, high-fidelity  
- **[NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction](https://arxiv.org/abs/2608.22888v2)**  
  Authors: Xiaopeng Guo, Wai Chung Tse, Yipeng Zhu, Hanwen Zhang, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22888v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nemosplat.hkustvgd.com)  
  Keywords: tracking, gaussian splatting, dynamic, 3d gaussian, motion, semantic, ar, 4d, high-fidelity  

### Few-shot

- **[PAGS: Autofocusing Photoacoustic Tomography via Speed-of-Sound-Adaptive Gaussian Splatting](https://arxiv.org/abs/2608.25472v1)**  
  Authors: Jiarui Ge, Jintao Ma, Bangxu Fan, Jinyan Zhang, Xiaokang Yang, Shuai Na, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25472v1.pdf)  
  Keywords: efficient, compact, gaussian splatting, ar, sparse-view  
- **[Seeing the Unseen: Semantic-in-Gaussian for Sparse-View 3D Generalization](https://arxiv.org/abs/2608.22740v1)**  
  Authors: Zeyang Bai, Yunpeng Wang, Yunbiao Wang, Jun Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22740v1.pdf)  
  Keywords: efficient, face, compact, gaussian splatting, 3d gaussian, semantic, sparse-view, ar  
- **[GaussVid: Sparse-View Gaussian Splatting with 3D-Aware Video Diffusion Priors](https://arxiv.org/abs/2608.21849v1)**  
  Authors: Xinhui Liu, Can Wang, Wei Jiang, Wei Wang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21849v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, sparse-view, sparse view, geometry  
- **[Sparse Light Field Sampling Improves Casual 3D and 4D Reconstruction](https://arxiv.org/abs/2608.20602v1)**  
  Authors: Shamus Li, Ruiming Cao, Laura Waller, Kristina Monakhova, Sara Fridovich-Keil  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20602v1.pdf)  
  Keywords: few-shot, dynamic, ar, motion, sparse-view, geometry, 4d  
- **[Point-Based 3D Reconstruction from Sparse Views under Known Illumination](https://arxiv.org/abs/2608.20000v1)**  
  Authors: Magnus Kaufmann Gjerde, Joakim Bruslund Haurum, Jeppe Revall Frisvad, Markus Worchel, J. Andreas Bærentzen, Thomas B. Moeslund  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20000v1.pdf)  
  Keywords: illumination, face, compact, gaussian splatting, ar, light transport, sparse view, geometry, 3d reconstruction  
- **[TR-GS: High-Fidelity Sparse-View CT Volumetric Rendering via t-Distribution Gaussian Splatting and Ray-Confidence Modeling](https://arxiv.org/abs/2608.16042v1)**  
  Authors: Zedong Xiao, Yiren Wang, Zhou Liu, Xiaolin Liu, Zhangji Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16042v1.pdf)  
  Keywords: efficient, medical, gaussian splatting, 3d gaussian, ar, sparse-view, sparse view, high-fidelity  
- **[Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting](https://arxiv.org/abs/2608.10756v1)**  
  Authors: Huosen Ou, Dongni Song, Yuncong Wang, Tao Zhou, Yiding Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10756v1.pdf)  
  Keywords: localization, face, few-shot, gaussian splatting, semantic, 3d gaussian, ar  
- **[CasDeblurGS: Cascaded 2D-to-3D Multi-View Consistency for 3D Gaussian Splatting from Two Blurry Images](https://arxiv.org/abs/2608.10345v1)**  
  Authors: Haeyun Choi, Minhyuk Jang, I-Gil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10345v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, motion, nerf, sparse-view, neural rendering  
- **[TRACE-GS: On-Policy Trajectory Distillation with Privileged Geometric Conditioning for Sparse-View 3DGS Restoration](https://arxiv.org/abs/2608.10286v1)**  
  Authors: Linlian Jiang, Yuchen Xi, Sadman Rakib Pinon, Ruigang Yang, Yang Wang, Xinxin Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10286v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, sparse-view, geometry  
- **[Scenix: Sparse-View 3D Scene Reconstruction via Executable Scene Programs](https://arxiv.org/abs/2608.07012v1)**  
  Authors: Kai Li, Lutao Jiang, Zhenyang Li, Jiayu Dong, Jierui Zhang, Yingda Yin, Runze Zhang, Kai Yan, Xiaoyang Huang, Keyang Luo, Xin Wang, Xiangyu Zhao, Weikai Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07012v1.pdf)  
  Keywords: sparse view, ar, sparse-view, human  

### Geometry Reconstruction

*Showing the latest 50 out of 229 papers*

- **[Comparative Evaluation of 3D Reconstruction Methods for Immersive Visualization of Laboratory Objects](https://arxiv.org/abs/2608.27301v1)**  
  Authors: Brian De La Cruz, Aaron Y. Zhao, Maitrey Gramopadhye, Sawyer J. Lazar, Xianming Tan, Daniel Szafir, David S. Lawrence  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.27301v1.pdf)  
  Keywords: gaussian splatting, ar, nerf, 3d reconstruction, high-fidelity  
- **[Per-View Gaussian Predictions Enable Training-Free Distractor Filtering in Feed-Forward 3DGS](https://arxiv.org/abs/2608.26951v1)**  
  Authors: Kangmin Seo, Jae-Pil Heo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26951v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, 3d reconstruction  
- **[CoGeo-GS: Concept-Driven and Geometry-Aware Multi-Object Removal in 3D Scenes](https://arxiv.org/abs/2608.26656v1)**  
  Authors: Yuanxiang Ni, Xianliang Huang, Chenhang Ma, Chen Xiao, Yuewen Ma, Ruxin Wang, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26656v1.pdf)  
  Keywords: gaussian splatting, semantic, 3d gaussian, ar, geometry  
- **[Cross-Platform Benchmark of Neural 3D Reconstruction for Autonomous Laboratory Robots](https://arxiv.org/abs/2608.26383v1)**  
  Authors: Yongho Kim, Mengjiao Han, Victor Mateevitsi, Silvio Rizzi, Michael E. Papka, Nicola Ferrier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26383v1.pdf)  
  Keywords: tracking, lightweight, gaussian splatting, 3d gaussian, ar, nerf, geometry, 3d reconstruction  
- **[GaussianDream++: Efficient 3D Gaussian World Modeling for Robotic Manipulation](https://arxiv.org/abs/2608.25659v1)**  
  Authors: Yuqing Jiang, Zijian Zhang, Weitao Zhou, Jiawei Wang, Junjie He, Lei Yang, Haifang Qing, Si Liu, Ding Zhao, Ping Luo, Haibao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25659v1.pdf)  
  Keywords: efficient, head, compact, 3d gaussian, dynamic, ar, motion, geometry  
- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: illumination, gaussian splatting, ar, motion, survey, geometry, 3d reconstruction  
- **[PIVOT: A Multi-Trajectory Dataset and Testbed for Pose, Intrinsics, and Novel Viewpoint Evaluation in Real-World 3D Reconstruction](https://arxiv.org/abs/2608.25401v1)**  
  Authors: Mary Raymond  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25401v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, nerf, 3d reconstruction  
- **[GaussianWAM: Distilling Geometry and Semantics from 3D Gaussian Fields into World-Action Models](https://arxiv.org/abs/2608.24714v1)**  
  Authors: Zijian Zhang, Yuqing Jiang, Weitao Zhou, Minglei Li, Jinhao Zhang, Yao Mu, Xiaofan Li, Hao Zhao, Haibao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24714v1.pdf)  
  Keywords: head, fast, 3d gaussian, dynamic, semantic, ar, geometry  
- **[GaussVLA: Geometry-Aware Spatial Reasoning for Vision-Language-Action Model](https://arxiv.org/abs/2608.24959v1)**  
  Authors: Md Selim Sarowar, Md Tanvir Islam, Sungho Kim, Sangtae Ahn  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24959v1.pdf)  
  Keywords: efficient, face, compact, 3d gaussian, semantic, ar, geometry  
- **[Learning Spherical Occupancy Profiles for Multi-View 3D Reconstruction and Generation](https://arxiv.org/abs/2608.23206v2)**  
  Authors: YiHsuan Tsai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23206v2.pdf)  
  Keywords: face, head, compact, 3d gaussian, ar, 3d reconstruction  

### Large Scene

- **[M$^3$ISR: A Multi-Modal Multi-View Benchmark for 3D/4D Gaussian Splatting and Feedforward Compression](https://arxiv.org/abs/2608.22465v1)**  
  Authors: Xinhui Liu, Lei Liu, Zhenghao Chen, Lebin Zhou, Wei Wang, Wei Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22465v1.pdf)  
  Keywords: outdoor, gaussian splatting, dynamic, compression, motion, semantic, ar, geometry, 4d, high-fidelity, segmentation  
- **[CoMVS-GS: Collaborative Multi-View Stereo and 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2608.18413v1)**  
  Authors: Shihan Chen, Junjing Zhang, Qingsong Yan, Haibing Liu, Haofan Ren, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.18413v1.pdf)  
  Keywords: efficient, face, outdoor, compact, gaussian splatting, 3d gaussian, ar, motion, geometry  
- **[GS-CPE: Unified 6-Degree-of-Freedom Camera Pose Estimation via 3D Gaussian Splatting](https://arxiv.org/abs/2608.10938v2)**  
  Authors: Huaiyuan Weng, Chul Min Yeum, Su-Min Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10938v2.pdf)  
  Keywords: localization, outdoor, fast, gaussian splatting, 3d gaussian, ar, geometry  
- **[OutLangSplat: 3D Language Gaussian Splatting for UAV Outdoor Scenes](https://arxiv.org/abs/2608.04560v1)**  
  Authors: Xia Yan, He Wu, Yanghui Xu, Zizhao Wu, Jiazhou Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04560v1.pdf)  
  Keywords: localization, efficient, outdoor, gaussian splatting, semantic, 3d gaussian, ar, understanding, segmentation  
- **[GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition](https://arxiv.org/abs/2607.21416v1)**  
  Authors: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.21416v1.pdf)  
  Keywords: localization, tracking, outdoor, mapping, lightweight, gaussian splatting, 3d gaussian, ar, geometry, slam  
- **[Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering](https://arxiv.org/abs/2607.19893v1)**  
  Authors: Zhenxiang Ma, Zeyu He, Yuanzhen Zhou, Zhenyu Yang, Yuchang Zhang, Miao Tao, Rong Fu, Jidong Zhai, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19893v1.pdf)  
  Keywords: head, large scene, ar, neural rendering  
- **[AniGS: Bridging Rendering and Diffusion Prior for 3D Scene Animation](https://arxiv.org/abs/2607.18539v1)**  
  Authors: Yen-Chi Cheng, Chen Gao, Chuhan Chen, Tuotuo Li, Rajvi Shah, Ayush Saraf, Changil Kim, Liangyan Gui, Alexander Schwing, Johannes Kopf, Hung-Yu Tseng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18539v1.pdf)  
  Keywords: deformation, outdoor, gaussian splatting, dynamic, 3d gaussian, motion, ar, animation  
- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956v1)**  
  Authors: Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.17956v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view)  
  Keywords: illumination, vr, tracking, outdoor, mapping, 3d gaussian, dynamic, ar, motion, geometry  
- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481v1)**  
  Authors: Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14481v1.pdf)  
  Keywords: real-time rendering, efficient, fast, gaussian splatting, 3d gaussian, large scene, motion, recognition, ar, slam  
- **[GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors](https://arxiv.org/abs/2607.11184v1)**  
  Authors: Ruilan Gao, Letian Jin, Yu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11184v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rlgao.github.io/geogs_slam)  
  Keywords: tracking, outdoor, mapping, gaussian splatting, 3d gaussian, ar, geometry, slam  

### Model Compression

*Showing the latest 50 out of 197 papers*

- **[KISS-GS: 3D Gaussian Splatting Compression Kept Simple](https://arxiv.org/abs/2608.26948v1)**  
  Authors: Wieland Morgenstern, Friedrich Elias Branschke, Florian Fleischmann, Adrian Szatmari, Paul Schlack, Florian Barthel, Peter Eisert, Anna Hilsmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26948v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fraunhoferhhi.github.io/KISS-GS)  
  Keywords: compact, gaussian splatting, ar, 3d gaussian, compression  
- **[Cross-Platform Benchmark of Neural 3D Reconstruction for Autonomous Laboratory Robots](https://arxiv.org/abs/2608.26383v1)**  
  Authors: Yongho Kim, Mengjiao Han, Victor Mateevitsi, Silvio Rizzi, Michael E. Papka, Nicola Ferrier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26383v1.pdf)  
  Keywords: tracking, lightweight, gaussian splatting, 3d gaussian, ar, nerf, geometry, 3d reconstruction  
- **[GaussianDream++: Efficient 3D Gaussian World Modeling for Robotic Manipulation](https://arxiv.org/abs/2608.25659v1)**  
  Authors: Yuqing Jiang, Zijian Zhang, Weitao Zhou, Jiawei Wang, Junjie He, Lei Yang, Haifang Qing, Si Liu, Ding Zhao, Ping Luo, Haibao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25659v1.pdf)  
  Keywords: efficient, head, compact, 3d gaussian, dynamic, ar, motion, geometry  
- **[PAGS: Autofocusing Photoacoustic Tomography via Speed-of-Sound-Adaptive Gaussian Splatting](https://arxiv.org/abs/2608.25472v1)**  
  Authors: Jiarui Ge, Jintao Ma, Bangxu Fan, Jinyan Zhang, Xiaokang Yang, Shuai Na, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25472v1.pdf)  
  Keywords: efficient, compact, gaussian splatting, ar, sparse-view  
- **[GaussVLA: Geometry-Aware Spatial Reasoning for Vision-Language-Action Model](https://arxiv.org/abs/2608.24959v1)**  
  Authors: Md Selim Sarowar, Md Tanvir Islam, Sungho Kim, Sangtae Ahn  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24959v1.pdf)  
  Keywords: efficient, face, compact, 3d gaussian, semantic, ar, geometry  
- **[Physics-Integrated Operator Learning via Gaussian Splatting Representations](https://arxiv.org/abs/2608.24049v1)**  
  Authors: Jihao Zhang, Junyi Guo, Jian-Xun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24049v1.pdf)  
  Keywords: efficient, face, gaussian splatting, ar, dynamic  
- **[FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors](https://arxiv.org/abs/2608.23549v1)**  
  Authors: Khiem Vuong, Deva Ramanan, Srinivasa Narasimhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23549v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, motion, nerf  
- **[Learning Spherical Occupancy Profiles for Multi-View 3D Reconstruction and Generation](https://arxiv.org/abs/2608.23206v2)**  
  Authors: YiHsuan Tsai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23206v2.pdf)  
  Keywords: face, head, compact, 3d gaussian, ar, 3d reconstruction  
- **[SACHA: Semantic-Aware Compression for 3D Gaussian Head Avatars](https://arxiv.org/abs/2608.23133v1)**  
  Authors: Zihan Zhang, Shanzhi Yin, Xinju Wu, Bolin Chen, Ru-Ling Liao, Jie Chen, Shiqi Wang, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23133v1.pdf)  
  Keywords: efficient, head, compact, 3d gaussian, dynamic, compression, motion, semantic, ar, avatar, high-fidelity  
- **[AquaFlow: A Monocular Gaussian Splatting SLAM for Underwater Streaming Reconstruction](https://arxiv.org/abs/2608.22906v1)**  
  Authors: Yingxiang Xu, Kerui Ren, Wenqi Guo, Changjian Jiang, Tao Lu, Linning Xu, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22906v1.pdf)  
  Keywords: localization, efficient, tracking, mapping, gaussian splatting, 3d gaussian, ar, geometry, slam, high-fidelity  

### Quality Enhancement

*Showing the latest 50 out of 103 papers*

- **[Comparative Evaluation of 3D Reconstruction Methods for Immersive Visualization of Laboratory Objects](https://arxiv.org/abs/2608.27301v1)**  
  Authors: Brian De La Cruz, Aaron Y. Zhao, Maitrey Gramopadhye, Sawyer J. Lazar, Xianming Tan, Daniel Szafir, David S. Lawrence  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.27301v1.pdf)  
  Keywords: gaussian splatting, ar, nerf, 3d reconstruction, high-fidelity  
- **[SACHA: Semantic-Aware Compression for 3D Gaussian Head Avatars](https://arxiv.org/abs/2608.23133v1)**  
  Authors: Zihan Zhang, Shanzhi Yin, Xinju Wu, Bolin Chen, Ru-Ling Liao, Jie Chen, Shiqi Wang, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23133v1.pdf)  
  Keywords: efficient, head, compact, 3d gaussian, dynamic, compression, motion, semantic, ar, avatar, high-fidelity  
- **[AquaFlow: A Monocular Gaussian Splatting SLAM for Underwater Streaming Reconstruction](https://arxiv.org/abs/2608.22906v1)**  
  Authors: Yingxiang Xu, Kerui Ren, Wenqi Guo, Changjian Jiang, Tao Lu, Linning Xu, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22906v1.pdf)  
  Keywords: localization, efficient, tracking, mapping, gaussian splatting, 3d gaussian, ar, geometry, slam, high-fidelity  
- **[NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction](https://arxiv.org/abs/2608.22888v2)**  
  Authors: Xiaopeng Guo, Wai Chung Tse, Yipeng Zhu, Hanwen Zhang, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22888v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nemosplat.hkustvgd.com)  
  Keywords: tracking, gaussian splatting, dynamic, 3d gaussian, motion, semantic, ar, 4d, high-fidelity  
- **[M$^3$ISR: A Multi-Modal Multi-View Benchmark for 3D/4D Gaussian Splatting and Feedforward Compression](https://arxiv.org/abs/2608.22465v1)**  
  Authors: Xinhui Liu, Lei Liu, Zhenghao Chen, Lebin Zhou, Wei Wang, Wei Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22465v1.pdf)  
  Keywords: outdoor, gaussian splatting, dynamic, compression, motion, semantic, ar, geometry, 4d, high-fidelity, segmentation  
- **[In-Situ Reconstruction of the International Space Station Using 3D Gaussian Splatting and Astrobee](https://arxiv.org/abs/2608.21685v1)**  
  Authors: Hudson Kim, Ryan Soussan, Brian Coltin, Jordan Kam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21685v1.pdf)  
  Keywords: human, mapping, gaussian splatting, 3d gaussian, ar, nerf, 3d reconstruction, high-fidelity  
- **[TopoSurfel: Closing the Loop between Gaussian Surfels and Meshes for Surface Reconstruction](https://arxiv.org/abs/2608.20687v1)**  
  Authors: Chuanjin Fan, Wenjie Chang, Bohao Liao, Yujia Chen, Wenfei Yang, Tianzhu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20687v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Fan-Treasure/TopoSurfel?style=social)](https://github.com/Fan-Treasure/TopoSurfel)  
  Keywords: face, gaussian splatting, dynamic, 3d gaussian, ar, geometry, high-fidelity  
- **[DesignAgent3D: Interactive 3D Scene Editing via Designer-like Multimodal Reasoning](https://arxiv.org/abs/2608.21438v1)**  
  Authors: Xiujin Liu, Tianyu Yang, Yilun Zhao, Xiangliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21438v1.pdf)  
  Keywords: localization, face, tracking, gaussian splatting, 3d gaussian, semantic, ar, nerf, high-fidelity  
- **[TR-GS: High-Fidelity Sparse-View CT Volumetric Rendering via t-Distribution Gaussian Splatting and Ray-Confidence Modeling](https://arxiv.org/abs/2608.16042v1)**  
  Authors: Zedong Xiao, Yiren Wang, Zhou Liu, Xiaolin Liu, Zhangji Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16042v1.pdf)  
  Keywords: efficient, medical, gaussian splatting, 3d gaussian, ar, sparse-view, sparse view, high-fidelity  
- **[HiCo-GS: Hierarchical Context Aggregation and Geometric Consistency for Octree Gaussian Splatting](https://arxiv.org/abs/2608.14136v1)**  
  Authors: Wei Zhang, Shengkai Yu, Shiqiang Gong, Qi Zhang, Qiang Li, Qi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.14136v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WZ-CS/HiCo-GS?style=social)](https://github.com/WZ-CS/HiCo-GS)  
  Keywords: head, lightweight, gaussian splatting, ar, geometry, high-fidelity  

### Ray Tracing

- **[Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)**  
  Authors: Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/vorotracing)  
  Keywords: real-time rendering, face, ray tracing, compact, fast, gaussian splatting, 3d gaussian, ar, motion, nerf  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: shadow, reflection, efficient, ray tracing, mapping, compact, fast, gaussian splatting, 3d gaussian, ar, nerf  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: illumination, reflection, efficient, face, ray tracing, lighting, gaussian splatting, ar, relighting  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: reflection, face, human, ray tracing, gaussian splatting, 3d gaussian, dynamic, motion, ar, geometry, high-fidelity  
- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: human, compact, ray casting, gaussian splatting, ar, geometry  
- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869v1)**  
  Authors: Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30869v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gray)  
  Keywords: ray tracing, fast, gaussian splatting, ar, 3d gaussian  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: reflection, real-time rendering, efficient, ray tracing, fast, gaussian splatting, 3d gaussian, path tracing, ar, geometry  
- **[RenderFormer++: Scalable and Physics-Informed Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v2)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v2.pdf)  
  Keywords: illumination, compact, global illumination, ar, light transport, neural rendering  
- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: illumination, efficient, global illumination, gaussian splatting, 3d gaussian, ar, geometry, 3d reconstruction  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: illumination, global illumination, gaussian splatting, ar, high-fidelity  

### Relighting

- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: illumination, gaussian splatting, ar, motion, survey, geometry, 3d reconstruction  
- **[Point-Based 3D Reconstruction from Sparse Views under Known Illumination](https://arxiv.org/abs/2608.20000v1)**  
  Authors: Magnus Kaufmann Gjerde, Joakim Bruslund Haurum, Jeppe Revall Frisvad, Markus Worchel, J. Andreas Bærentzen, Thomas B. Moeslund  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20000v1.pdf)  
  Keywords: illumination, face, compact, gaussian splatting, ar, light transport, sparse view, geometry, 3d reconstruction  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: shadow, reflection, efficient, ray tracing, mapping, compact, fast, gaussian splatting, 3d gaussian, ar, nerf  
- **[Geometry-Aware Online Mapping for 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2608.14902v1)**  
  Authors: Thai Luu, Quan Tran, Hieu Phan, Tuan Dang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.14902v1.pdf)  
  Keywords: localization, efficient, tracking, mapping, lighting, head, gaussian splatting, 3d gaussian, ar, geometry, slam  
- **[SpotlessGS: Relightable 3D Gaussian Splatting under Dynamic Illumination for Robotic Perception](https://arxiv.org/abs/2608.14713v1)**  
  Authors: Liang Hong, Jiaxin Wei, Simon Schaefer, Stefan Leutenegger, Jaehyung Jung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.14713v1.pdf)  
  Keywords: illumination, relightable, lighting, gaussian splatting, 3d gaussian, dynamic, ar, 3d reconstruction  
- **[AdvTiles: Physical Adversarial Camouflage Clothing against Person Detectors via Learnable Tiles](https://arxiv.org/abs/2608.06801v1)**  
  Authors: Jinlei Wang, Jiahuan Long, Mingkai Sun, Yafei Guo, Yuanhao Huang, Ming Wang, Junqi Wu, Jiacheng Hou, Hongbo Chen, Xingxing Wei, Tingsong Jiang, Wen Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06801v1.pdf)  
  Keywords: illumination, gaussian splatting, ar, 3d gaussian, body  
- **[DerainSplat: Feed-Forward Clean 3D Gaussian Splatting from Sparse Rainy Views](https://arxiv.org/abs/2608.02191v1)**  
  Authors: Fuzhen Jiang, Changyue Shi, Chuxiao Yang, Xinyuan Hu, Wenjie Ye, Minghao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02191v1.pdf)  
  Keywords: illumination, gaussian splatting, 3d gaussian, ar, nerf, geometry, autonomous driving  
- **[DecoupleGS: Interactive 3D Gaussian Splatting for End-to-End Autonomous Driving Testing](https://arxiv.org/abs/2608.01761v1)**  
  Authors: Siying Li, Ying Ni, Jie Sun, Jian Sun, Haotian Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01761v1.pdf)  
  Keywords: illumination, lighting, gaussian splatting, 3d gaussian, dynamic, compression, semantic, ar, relighting, autonomous driving, high-fidelity, neural rendering  
- **[Endo-NeRF++: Uncertainty-Aware Neural Rendering with Multi-Resolution Hash Encoding for Dynamic Surgical Scene Reconstruction](https://arxiv.org/abs/2607.27825v3)**  
  Authors: Gousia Habib, Laura Ruotsalainen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.27825v3.pdf)  
  Keywords: reflection, deformation, dynamic, ar, nerf, neural rendering  
- **[PanoLess: Environment Reconstruction from Partial Reflective Views](https://arxiv.org/abs/2607.25362v1)**  
  Authors: Ahitagni Das, Ashok Veeraraghavan, Vivek Boominathan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25362v1.pdf)  
  Keywords: illumination, reflection, face, ar, high-fidelity  

### SLAM

*Showing the latest 50 out of 83 papers*

- **[CGS-SLAM: Collaborative Gaussian Splatting based SLAM for Multi-Agent Reconstruction](https://arxiv.org/abs/2608.26868v1)**  
  Authors: Jean-Daniel de Ambrogi, Aladine Chetouani, Vincent Nguyen, Aurélien Chateigner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26868v1.pdf)  
  Keywords: tracking, mapping, gaussian splatting, dynamic, ar, motion, slam  
- **[Cross-Platform Benchmark of Neural 3D Reconstruction for Autonomous Laboratory Robots](https://arxiv.org/abs/2608.26383v1)**  
  Authors: Yongho Kim, Mengjiao Han, Victor Mateevitsi, Silvio Rizzi, Michael E. Papka, Nicola Ferrier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26383v1.pdf)  
  Keywords: tracking, lightweight, gaussian splatting, 3d gaussian, ar, nerf, geometry, 3d reconstruction  
- **[AquaFlow: A Monocular Gaussian Splatting SLAM for Underwater Streaming Reconstruction](https://arxiv.org/abs/2608.22906v1)**  
  Authors: Yingxiang Xu, Kerui Ren, Wenqi Guo, Changjian Jiang, Tao Lu, Linning Xu, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22906v1.pdf)  
  Keywords: localization, efficient, tracking, mapping, gaussian splatting, 3d gaussian, ar, geometry, slam, high-fidelity  
- **[NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction](https://arxiv.org/abs/2608.22888v2)**  
  Authors: Xiaopeng Guo, Wai Chung Tse, Yipeng Zhu, Hanwen Zhang, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22888v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nemosplat.hkustvgd.com)  
  Keywords: tracking, gaussian splatting, dynamic, 3d gaussian, motion, semantic, ar, 4d, high-fidelity  
- **[In-Situ Reconstruction of the International Space Station Using 3D Gaussian Splatting and Astrobee](https://arxiv.org/abs/2608.21685v1)**  
  Authors: Hudson Kim, Ryan Soussan, Brian Coltin, Jordan Kam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21685v1.pdf)  
  Keywords: human, mapping, gaussian splatting, 3d gaussian, ar, nerf, 3d reconstruction, high-fidelity  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: shadow, reflection, efficient, ray tracing, mapping, compact, fast, gaussian splatting, 3d gaussian, ar, nerf  
- **[DesignAgent3D: Interactive 3D Scene Editing via Designer-like Multimodal Reasoning](https://arxiv.org/abs/2608.21438v1)**  
  Authors: Xiujin Liu, Tianyu Yang, Yilun Zhao, Xiangliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21438v1.pdf)  
  Keywords: localization, face, tracking, gaussian splatting, 3d gaussian, semantic, ar, nerf, high-fidelity  
- **[MotionGS-SLAM: Event-Modulated Gaussian Splatting for Motion-Blur Robust SLAM](https://arxiv.org/abs/2608.15024v1)**  
  Authors: Zhiqiang Hu, Shouren Huang, Masatoshi Ishikawa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.15024v1.pdf)  
  Keywords: gaussian splatting, dynamic, ar, motion, geometry, slam  
- **[Geometry-Aware Online Mapping for 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2608.14902v1)**  
  Authors: Thai Luu, Quan Tran, Hieu Phan, Tuan Dang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.14902v1.pdf)  
  Keywords: localization, efficient, tracking, mapping, lighting, head, gaussian splatting, 3d gaussian, ar, geometry, slam  
- **[Seed2GS: Camera-Free, Training-Free Object Extraction from 3D Gaussian Scenes via a Single Reference-View Grounding](https://arxiv.org/abs/2608.11928v1)**  
  Authors: Zongjian Ding, Yudong Gao, Jiale Liu, Xinglin Yu, Junxing Ren, Dong Wei, Yajing Chen, Shan Huang, Mingjun Cheng, Min Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.11928v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, tracking  

### Scene Understanding

*Showing the latest 50 out of 116 papers*

- **[CoGeo-GS: Concept-Driven and Geometry-Aware Multi-Object Removal in 3D Scenes](https://arxiv.org/abs/2608.26656v1)**  
  Authors: Yuanxiang Ni, Xianliang Huang, Chenhang Ma, Chen Xiao, Yuewen Ma, Ruxin Wang, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26656v1.pdf)  
  Keywords: gaussian splatting, semantic, 3d gaussian, ar, geometry  
- **[GaussianWAM: Distilling Geometry and Semantics from 3D Gaussian Fields into World-Action Models](https://arxiv.org/abs/2608.24714v1)**  
  Authors: Zijian Zhang, Yuqing Jiang, Weitao Zhou, Minglei Li, Jinhao Zhang, Yao Mu, Xiaofan Li, Hao Zhao, Haibao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24714v1.pdf)  
  Keywords: head, fast, 3d gaussian, dynamic, semantic, ar, geometry  
- **[GaussVLA: Geometry-Aware Spatial Reasoning for Vision-Language-Action Model](https://arxiv.org/abs/2608.24959v1)**  
  Authors: Md Selim Sarowar, Md Tanvir Islam, Sungho Kim, Sangtae Ahn  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24959v1.pdf)  
  Keywords: efficient, face, compact, 3d gaussian, semantic, ar, geometry  
- **[SACHA: Semantic-Aware Compression for 3D Gaussian Head Avatars](https://arxiv.org/abs/2608.23133v1)**  
  Authors: Zihan Zhang, Shanzhi Yin, Xinju Wu, Bolin Chen, Ru-Ling Liao, Jie Chen, Shiqi Wang, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23133v1.pdf)  
  Keywords: efficient, head, compact, 3d gaussian, dynamic, compression, motion, semantic, ar, avatar, high-fidelity  
- **[NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction](https://arxiv.org/abs/2608.22888v2)**  
  Authors: Xiaopeng Guo, Wai Chung Tse, Yipeng Zhu, Hanwen Zhang, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22888v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nemosplat.hkustvgd.com)  
  Keywords: tracking, gaussian splatting, dynamic, 3d gaussian, motion, semantic, ar, 4d, high-fidelity  
- **[Seeing the Unseen: Semantic-in-Gaussian for Sparse-View 3D Generalization](https://arxiv.org/abs/2608.22740v1)**  
  Authors: Zeyang Bai, Yunpeng Wang, Yunbiao Wang, Jun Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22740v1.pdf)  
  Keywords: efficient, face, compact, gaussian splatting, 3d gaussian, semantic, sparse-view, ar  
- **[M$^3$ISR: A Multi-Modal Multi-View Benchmark for 3D/4D Gaussian Splatting and Feedforward Compression](https://arxiv.org/abs/2608.22465v1)**  
  Authors: Xinhui Liu, Lei Liu, Zhenghao Chen, Lebin Zhou, Wei Wang, Wei Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22465v1.pdf)  
  Keywords: outdoor, gaussian splatting, dynamic, compression, motion, semantic, ar, geometry, 4d, high-fidelity, segmentation  
- **[DiGS-Avatar: Single-Image Animatable 3D Human Reconstruction via UV-Space Diffusion](https://arxiv.org/abs/2608.20759v1)**  
  Authors: Jiakun Li, Li Fang, Hao Zhu, Fei Hu, Long Ye, Yuan Zhang, Jinyao Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20759v1.pdf) | [![GitHub](https://img.shields.io/github/stars/KLMAV-CUC/DiGS-Avatar?style=social)](https://github.com/KLMAV-CUC/DiGS-Avatar)  
  Keywords: efficient, human, 3d gaussian, semantic, ar, avatar, 3d reconstruction  
- **[USR-Drive: Unified Driving Scene Representation via Joint Denoising of 3D Gaussians and Boxes](https://arxiv.org/abs/2608.19036v1)**  
  Authors: Li-Heng Chen, Haokai Pang, Chengye Su, Jiarun Liu, Qifeng Chen, Ziqian Ni, Jianxin Huang, Shi-Sheng Huang, Hongbo Fu, Sheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.19036v1.pdf)  
  Keywords: 3d gaussian, dynamic, ar, geometry, autonomous driving, understanding  
- **[GroupForward: Building Referable 3D Scenes via Instance-Grouped Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2608.17535v1)**  
  Authors: Qijian Tian, Zimeng Wu, Xuhong Wang, Lizhuang Ma, Xin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17535v1.pdf)  
  Keywords: efficient, compact, gaussian splatting, 3d gaussian, semantic, ar, geometry, understanding, segmentation  



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
