# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-gaussians/)**: an interactive paper map, monthly trends, topic network and co-author network of every tracked paper.

> Last Update: 2026-10-11 02:50:22

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
- [Acceleration](#acceleration) (81 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (500 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (170 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (192 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (39 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (210 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (25 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (205 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (71 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (4 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (40 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (76 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (98 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[GS-Pool: Object-Level Change Detection in 3D Gaussian Splatting](https://arxiv.org/abs/2610.06688v1)**  
  Authors: Boaz Keren-Gil, James Gain, Patrick Marais  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.06688v1.pdf)  
  Keywords: gaussian splatting, survey, ar, geometry, 3d gaussian  
- **[OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones](https://arxiv.org/abs/2609.24253v1)**  
  Authors: Zhongrui You, Zhen Li, Junli Liu, Zhigang Wang, Bin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24253v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://openflyscan.github.io)  
  Keywords: gaussian splatting, survey, ar, 3d gaussian, high-fidelity, face  
- **[Quality Assessment of 3D Gaussian Splatting: Distortions, Benchmarks, and Open Challenges](https://arxiv.org/abs/2609.23027v1)**  
  Authors: Shuai Liu, Binqiang Liu, Qingyu Mao, Jiacong Chen, Yongsheng Liang, Youneng Bao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23027v1.pdf)  
  Keywords: gaussian splatting, survey, ar, 3d gaussian, compression  
- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: gaussian splatting, survey, ar, geometry, 3d reconstruction, motion, illumination  
- **[UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys](https://arxiv.org/abs/2608.06404v1)**  
  Authors: Junxiong Zhou, Xuechen Li, Chonghao Qiu, Lang Qiao, Xiaowei Jia, Qi Yang, Chishan Zhang, Leikun Yin, Nanshan You, Vipin Kumar, David Mulla, Ce Yang, Zhenong Jin, Licheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06404v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://link-dev.github.io/UAV3DCrop)  
  Keywords: gaussian splatting, survey, ar, geometry, dynamic, nerf, 3d gaussian, 3d reconstruction  

### Acceleration

*Showing the latest 50 out of 81 papers*

- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, geometry, dynamic, real-time rendering, 3d gaussian, face, illumination  
- **[Efficient 3D Gaussian Head Avatars for Edge Devices](https://arxiv.org/abs/2610.09821v1)**  
  Authors: Umar Farooq, Jean-Yves Guillemaut, Adrian Hilton, Marco Volino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09821v1.pdf)  
  Keywords: ar, efficient rendering, 3d gaussian, compression, efficient, head, avatar  
- **[LoCoSplat: Real-Time Feed-Forward 3D Gaussian Splatting with Minimal 3D Reasoning](https://arxiv.org/abs/2610.04351v1)**  
  Authors: Sinan Wang, Jinjin He, Yuchen Sun, Duowen Chen, Shenyifan Lu, Bo Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04351v1.pdf)  
  Keywords: gaussian splatting, ar, dynamic, 3d gaussian, fast  
- **[Budgeted-GS: Real-Time Large-Scale Gaussian Splatting via Factoring LOD](https://arxiv.org/abs/2610.03162v1)**  
  Authors: Haipeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03162v1.pdf)  
  Keywords: gaussian splatting, ar, high quality, 3d gaussian, real-time rendering  
- **[FactorSplat: Appearance-Controllable Gaussian Proxies for Medical Volume Rendering](https://arxiv.org/abs/2610.02382v1)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/FactorSplat)  
  Keywords: gaussian splatting, ar, geometry, fast, medical  
- **[One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time Avatars](https://arxiv.org/abs/2610.02207v1)**  
  Authors: Ramazan Fazylov, Stamatis Lefkimmiatis, Ivan Laptev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02207v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ramazan793.github.io/gala)  
  Keywords: ar, dynamic, 3d gaussian, animation, efficient, fast, avatar  
- **[Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation](https://arxiv.org/abs/2610.01114v1)**  
  Authors: Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01114v1.pdf)  
  Keywords: deformation, gaussian splatting, ar, efficient, fast, motion  
- **[Dirichlet Splatting: Differentiable Rendering for Wave-Based Inverse Problems](https://arxiv.org/abs/2610.00618v1)**  
  Authors: Xingyu Chen, Wuqiong Zhao, Xinyu Zhang, Tzu-Mao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00618v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, fast  
- **[EffGS: Efficient and High-Fidelity Gaussian Splatting](https://arxiv.org/abs/2609.39553v1)**  
  Authors: Changbai Li, Shuo Yang, Yichen Yang, Shuwei Shao, Huobin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39553v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, high-fidelity, compact, acceleration, efficient  
- **[RLX: A Unified Multi-Backend Tensor Compiler and Distributed Runtime in Rust](https://arxiv.org/abs/2609.37916v1)**  
  Authors: Eugene Hauptmann, Nataliya Kosmyna  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37916v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, fast  

### Applications

*Showing the latest 50 out of 500 papers*

- **[OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs](https://arxiv.org/abs/2610.12461v1)**  
  Authors: You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12461v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ouroworld.userwei.com)  
  Keywords: deformation, gaussian splatting, ar, dynamic, 3d gaussian, motion, 4d, illumination  
- **[LVS: Local View Synthesis from Relative Camera Pose by Reusing Previous Views](https://arxiv.org/abs/2610.12127v1)**  
  Authors: Qizhou Huo, Xuan Sun, Yongfei Guo, Zhipeng Wang, Yuanhao Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12127v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, 3d gaussian, motion  
- **[2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map](https://arxiv.org/abs/2610.11752v1)**  
  Authors: Jiwon Park, Dong-Uk Seo, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11752v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://2dgs-planner.github.io)  
  Keywords: gaussian splatting, ar, geometry, efficient, face  
- **[CoCam4D: Geometry-Aware Cooperative 4D Perception for Camera-Only Autonomous Driving](https://arxiv.org/abs/2610.11577v1)**  
  Authors: Soham Pahari, Sudip Das, Arindam Das, Ujjwal Bhattacharya  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11577v1.pdf)  
  Keywords: ar, dynamic, geometry, autonomous driving, 3d gaussian, compact, efficient, 4d  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, geometry, dynamic, real-time rendering, 3d gaussian, face, illumination  
- **[OX-NeRF: 3D X-ray Tomography Reconstruction from Sparse Views Using Implicit Neural Representation](https://arxiv.org/abs/2610.11547v1)**  
  Authors: Thomas Welsch, Min-Hsin Tu, David J. Chapman, Daniel E. Eakins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11547v1.pdf)  
  Keywords: gaussian splatting, ar, nerf, sparse view, 3d reconstruction  
- **[FlyMark: Training-Free Invisible Watermarking of 3D Gaussian Splatting via a Fruit Fly Connectome](https://arxiv.org/abs/2610.11364v1)**  
  Authors: Ziyuan Luo, Haoliang Li, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11364v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, geometry  
- **[3DTexMOR: 3D Gaussian Multi-Object Removal via Texture-Space Inpainting](https://arxiv.org/abs/2610.11198v1)**  
  Authors: Kunxin Guang, Yonghao Zhao, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11198v1.pdf)  
  Keywords: ar, geometry, reflection, nerf, 3d gaussian  
- **[MATE4D: Matrix-Guided Editable 4D Generation from a Single Image](https://arxiv.org/abs/2610.11181v1)**  
  Authors: Xiaotian Chen, Dongfu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11181v1.pdf)  
  Keywords: deformation, lightweight, ar, vr, dynamic, geometry, 3d gaussian, motion, 4d  
- **[Rendering-Free Lookahead for Question-Guided Active Vision](https://arxiv.org/abs/2610.11039v1)**  
  Authors: Koya Sakamoto, Daichi Azuma, Shuhei Kurita, Naoya Chiba, Yusuke Iwasawa, Yutaka Matsuo, Taiki Miyanishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11039v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, motion, head  

### Avatar Generation

*Showing the latest 50 out of 170 papers*

- **[2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map](https://arxiv.org/abs/2610.11752v1)**  
  Authors: Jiwon Park, Dong-Uk Seo, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11752v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://2dgs-planner.github.io)  
  Keywords: gaussian splatting, ar, geometry, efficient, face  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, geometry, dynamic, real-time rendering, 3d gaussian, face, illumination  
- **[Rendering-Free Lookahead for Question-Guided Active Vision](https://arxiv.org/abs/2610.11039v1)**  
  Authors: Koya Sakamoto, Daichi Azuma, Shuhei Kurita, Naoya Chiba, Yusuke Iwasawa, Yutaka Matsuo, Taiki Miyanishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11039v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, motion, head  
- **[PCAsplat: Gaussian Splatting with Local PCA Regularization](https://arxiv.org/abs/2610.11011v1)**  
  Authors: Vitor Matias, Filipe Nascimento, Kiyohiro Nakayama, João Paulo Lima, Márcus Lobo, Gordon Wetzstein, Leonidas Guibas, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11011v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, nerf, segmentation, face, 3d reconstruction  
- **[DeltaSplat: Iterative Gaussian Refinement for Pose-Free Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2610.09853v1)**  
  Authors: Chanung Park, Seunghyeon Song, Joo Chan Lee, Eunbyung Park, Jong Hwan Ko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09853v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, 3d gaussian, efficient, head  
- **[Efficient 3D Gaussian Head Avatars for Edge Devices](https://arxiv.org/abs/2610.09821v1)**  
  Authors: Umar Farooq, Jean-Yves Guillemaut, Adrian Hilton, Marco Volino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09821v1.pdf)  
  Keywords: ar, efficient rendering, 3d gaussian, compression, efficient, head, avatar  
- **[S2Tok: Streaming 3D Gaussian Reconstruction with Persistent Spatial Tokens](https://arxiv.org/abs/2610.08978v1)**  
  Authors: Fang Li, Jiraphon Yenphraphai, Quentin Herau, Depu Meng, Yihan Hu, Tianshuo Xu, Narendra Ahuja, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.08978v1.pdf)  
  Keywords: ar, 3d gaussian, compact, 3d reconstruction, head  
- **[DensiTok: Making Feed-Forward 3D Gaussian Splatting See More Views Than It Is Given](https://arxiv.org/abs/2610.07958v1)**  
  Authors: Minhyeok Lee, Jungho Lee, Minseok Kang, Heeseung Choi, Ig-Jae Kim, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07958v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, 3d gaussian, compact, sparse-view, head  
- **[MoonGS: High-quality Representation of the Lunar Surface via Gaussian Splatting Using Robust Depth Features from Image Pairs](https://arxiv.org/abs/2610.07110v1)**  
  Authors: Yun Jiang, Bo Zheng, Yingying Zhang, Xueming Xiao, Tao Hu, Hutao Cui, Zhiguo Meng, Ke Gao, Yang Gao, Meibao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07110v1.pdf) | [![GitHub](https://img.shields.io/github/stars/InRobots/MoonBlender?style=social)](https://github.com/InRobots/MoonBlender)  
  Keywords: gaussian splatting, ar, nerf, 3d gaussian, face, 3d reconstruction, head, semantic  
- **[MaRO-GS: Mask-Robust Object-Centric Gaussian Splatting from Inconsistent Multi-view Masks](https://arxiv.org/abs/2610.06472v1)**  
  Authors: Eunji Kim, Gahyeon Kim, Gianella Cravioto, Dong-hun Lee, Chaewon Moon, Chae-yeong Song, Sang-hyo Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.06472v1.pdf)  
  Keywords: gaussian splatting, ar, head, segmentation  

### Dynamic Scene

*Showing the latest 50 out of 192 papers*

- **[OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs](https://arxiv.org/abs/2610.12461v1)**  
  Authors: You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12461v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ouroworld.userwei.com)  
  Keywords: deformation, gaussian splatting, ar, dynamic, 3d gaussian, motion, 4d, illumination  
- **[LVS: Local View Synthesis from Relative Camera Pose by Reusing Previous Views](https://arxiv.org/abs/2610.12127v1)**  
  Authors: Qizhou Huo, Xuan Sun, Yongfei Guo, Zhipeng Wang, Yuanhao Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12127v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, 3d gaussian, motion  
- **[CoCam4D: Geometry-Aware Cooperative 4D Perception for Camera-Only Autonomous Driving](https://arxiv.org/abs/2610.11577v1)**  
  Authors: Soham Pahari, Sudip Das, Arindam Das, Ujjwal Bhattacharya  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11577v1.pdf)  
  Keywords: ar, dynamic, geometry, autonomous driving, 3d gaussian, compact, efficient, 4d  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, geometry, dynamic, real-time rendering, 3d gaussian, face, illumination  
- **[MATE4D: Matrix-Guided Editable 4D Generation from a Single Image](https://arxiv.org/abs/2610.11181v1)**  
  Authors: Xiaotian Chen, Dongfu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11181v1.pdf)  
  Keywords: deformation, lightweight, ar, vr, dynamic, geometry, 3d gaussian, motion, 4d  
- **[Rendering-Free Lookahead for Question-Guided Active Vision](https://arxiv.org/abs/2610.11039v1)**  
  Authors: Koya Sakamoto, Daichi Azuma, Shuhei Kurita, Naoya Chiba, Yusuke Iwasawa, Yutaka Matsuo, Taiki Miyanishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11039v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, motion, head  
- **[DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video](https://arxiv.org/abs/2610.09720v1)**  
  Authors: Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09720v1.pdf)  
  Keywords: ar, dynamic, geometry, high-fidelity, efficient, 4d, outdoor  
- **[LighTROcc: Lightweight 4D Occupancy Forecasting via Instance-Centric 3D Gaussians](https://arxiv.org/abs/2610.09444v1)**  
  Authors: Hwanhee Jung, SeungHyeon Kim, Inkyu Koo, Qixing Huang, Sang Ho Yoon, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09444v1.pdf)  
  Keywords: lightweight, ar, geometry, autonomous driving, 3d gaussian, compact, 4d  
- **[Controllable and Photorealistic Pedestrian Risky Motion Generation for End-to-End Driving Safety Evaluation](https://arxiv.org/abs/2610.06171v1)**  
  Authors: Siyuan Liu, Miao Li, Haibao Yu, Haohong Lin, Qing Zhou, Bingbing Nie, Ding Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.06171v1.pdf)  
  Keywords: human, gaussian splatting, ar, autonomous driving, 3d gaussian, motion, avatar  
- **[Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting](https://arxiv.org/abs/2610.05289v1)**  
  Authors: Xiaobiao Du, Beixi Hao, Zhen Fang, Tianqing Zhu, Richard Hartley, Xin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05289v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiaobiaodu.github.io/mobile-4dgs-project)  
  Keywords: deformation, gaussian splatting, lightweight, ar, dynamic, 3d gaussian, high-fidelity, compact, motion, 4d, head  

### Few-shot

- **[OX-NeRF: 3D X-ray Tomography Reconstruction from Sparse Views Using Implicit Neural Representation](https://arxiv.org/abs/2610.11547v1)**  
  Authors: Thomas Welsch, Min-Hsin Tu, David J. Chapman, Daniel E. Eakins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11547v1.pdf)  
  Keywords: gaussian splatting, ar, nerf, sparse view, 3d reconstruction  
- **[DensiTok: Making Feed-Forward 3D Gaussian Splatting See More Views Than It Is Given](https://arxiv.org/abs/2610.07958v1)**  
  Authors: Minhyeok Lee, Jungho Lee, Minseok Kang, Heeseung Choi, Ig-Jae Kim, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07958v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, 3d gaussian, compact, sparse-view, head  
- **[Sparse-View 4D Gaussian Splatting via Spatiotemporal Priors and Generative Assistance](https://arxiv.org/abs/2610.04606v2)**  
  Authors: Shengqi Wang, Zhengxian Yang, Kaiwen Tian, Yang Liu, Bowen Liu, Hua Du, Taicheng Huang, Jiamin Wu, Tao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04606v2.pdf)  
  Keywords: gaussian splatting, ar, dynamic, geometry, sparse view, sparse-view, motion, 4d  
- **[Sparse-GS2Mesh: 3D Gaussian Splatting Guided by Novel Stereo Views and 2DGS for Sparse View Surface Reconstruction](https://arxiv.org/abs/2610.04203v2)**  
  Authors: Younghyun Noh, Minje Kim, Tae-Kyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04203v2.pdf)  
  Keywords: gaussian splatting, ar, geometry, 3d gaussian, sparse view, sparse-view, efficient, face  
- **[UGOD: Uncertainty-Guided Opacity and Dropout for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.39089v1)**  
  Authors: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Chenghao Qian, Ziyang Wang, Xinqi Fan, Liangxiu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39089v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, nerf, 3d gaussian, compact, sparse-view, head  
- **[Remote Sensing Sparse-View 3D Gaussian Splatting via Depth Image-Based Rendering](https://arxiv.org/abs/2609.35612v1)**  
  Authors: Jiaming Kang, Zhengxia Zou, Zhenwei Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35612v1.pdf) | [![GitHub](https://img.shields.io/github/stars/kanehub/DIBR-GS?style=social)](https://github.com/kanehub/DIBR-GS)  
  Keywords: gaussian splatting, ar, nerf, 3d gaussian, sparse-view, face  
- **[GAPS: Generative Active Pseudo-view Selection for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.23436v2)**  
  Authors: Hongfei Zhu, Haochen Deng, Sitao Zhang, Ling Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23436v2.pdf)  
  Keywords: gaussian splatting, ar, geometry, real-time rendering, 3d gaussian, nerf, sparse-view  
- **[D3GS: Depth, DINO, and RGB Diffusion Co-Guided 3D Gaussian Splatting for Sparse-View Reconstruction](https://arxiv.org/abs/2609.22941v1)**  
  Authors: Yunqi Gao, Zhanfeng Liao, Hanzhang Tu, Zhaoqi Su, Guoqing Zheng, Songtao Wang, Hongwen Zhang, Zhou Xue, Leyuan Liu, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.22941v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, nerf, 3d gaussian, sparse-view  
- **[LINGO: Latent Initialization and Gradient Optimization for Sparse-view X-ray Novel View Synthesis and CT Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2609.22849v1)**  
  Authors: Lifeng Xing, Dequan Jin, Kunpeng Bu, Peigeng He, Shihui Ying  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.22849v1.pdf)  
  Keywords: gaussian splatting, ar, dynamic, 3d gaussian, sparse-view  
- **[4DGS-Fixer: Generative Sparse-View 4D Gaussian Splatting with Iterative Refinement Guided by Video Diffusion Priors](https://arxiv.org/abs/2609.21176v3)**  
  Authors: Haitao Huang, Shenghao Zhao, Boyuan Tian, Shin-Fang Chng, Songlin Yang, Sheila Lim, Huangying Zhan, Yi Xu, Anyi Rao, Frank Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21176v3.pdf)  
  Keywords: gaussian splatting, ar, large scene, dynamic, sparse-view, 4d  

### Geometry Reconstruction

*Showing the latest 50 out of 210 papers*

- **[2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map](https://arxiv.org/abs/2610.11752v1)**  
  Authors: Jiwon Park, Dong-Uk Seo, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11752v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://2dgs-planner.github.io)  
  Keywords: gaussian splatting, ar, geometry, efficient, face  
- **[CoCam4D: Geometry-Aware Cooperative 4D Perception for Camera-Only Autonomous Driving](https://arxiv.org/abs/2610.11577v1)**  
  Authors: Soham Pahari, Sudip Das, Arindam Das, Ujjwal Bhattacharya  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11577v1.pdf)  
  Keywords: ar, dynamic, geometry, autonomous driving, 3d gaussian, compact, efficient, 4d  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, geometry, dynamic, real-time rendering, 3d gaussian, face, illumination  
- **[OX-NeRF: 3D X-ray Tomography Reconstruction from Sparse Views Using Implicit Neural Representation](https://arxiv.org/abs/2610.11547v1)**  
  Authors: Thomas Welsch, Min-Hsin Tu, David J. Chapman, Daniel E. Eakins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11547v1.pdf)  
  Keywords: gaussian splatting, ar, nerf, sparse view, 3d reconstruction  
- **[FlyMark: Training-Free Invisible Watermarking of 3D Gaussian Splatting via a Fruit Fly Connectome](https://arxiv.org/abs/2610.11364v1)**  
  Authors: Ziyuan Luo, Haoliang Li, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11364v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, geometry  
- **[3DTexMOR: 3D Gaussian Multi-Object Removal via Texture-Space Inpainting](https://arxiv.org/abs/2610.11198v1)**  
  Authors: Kunxin Guang, Yonghao Zhao, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11198v1.pdf)  
  Keywords: ar, geometry, reflection, nerf, 3d gaussian  
- **[MATE4D: Matrix-Guided Editable 4D Generation from a Single Image](https://arxiv.org/abs/2610.11181v1)**  
  Authors: Xiaotian Chen, Dongfu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11181v1.pdf)  
  Keywords: deformation, lightweight, ar, vr, dynamic, geometry, 3d gaussian, motion, 4d  
- **[PCAsplat: Gaussian Splatting with Local PCA Regularization](https://arxiv.org/abs/2610.11011v1)**  
  Authors: Vitor Matias, Filipe Nascimento, Kiyohiro Nakayama, João Paulo Lima, Márcus Lobo, Gordon Wetzstein, Leonidas Guibas, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11011v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, nerf, segmentation, face, 3d reconstruction  
- **[DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video](https://arxiv.org/abs/2610.09720v1)**  
  Authors: Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09720v1.pdf)  
  Keywords: ar, dynamic, geometry, high-fidelity, efficient, 4d, outdoor  
- **[Gaussian Material Fields for Volumetric Multi-Energy CT Decomposition](https://arxiv.org/abs/2610.09492v1)**  
  Authors: Jian Lin, Jiancheng Fang, Hongming Shan, Shaoyu Wang, Yang Chen, Qiegen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09492v1.pdf)  
  Keywords: ar, 3d gaussian, geometry, efficient  

### Large Scene

- **[DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video](https://arxiv.org/abs/2610.09720v1)**  
  Authors: Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09720v1.pdf)  
  Keywords: ar, dynamic, geometry, high-fidelity, efficient, 4d, outdoor  
- **[LEGO-Anything: Coding Agents for 3D Scene Reconstruction](https://arxiv.org/abs/2609.36380v1)**  
  Authors: Xirui Li, Peng Shi, Mingwen Dong, Sheng Zhang, Zhuoyan Xu, Dongkyu Lee, Shuaichen Chang, Yi Xiang, Lin Pan, Jiarong Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36380v1.pdf)  
  Keywords: ar, outdoor, geometry, face  
- **[Federated 3D Gaussian Splatting for Large-Scale Scene Reconstruction at Wireless Edge](https://arxiv.org/abs/2609.32177v1)**  
  Authors: Guanlin Wu, Chao Hu, Pu Chen, Juyong Zhang, Han Hu, Shuguang Cui, Jie Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32177v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, large scene, 3d gaussian, efficient, face  
- **[ChronoFuseGS: Multi-Temporal Gaussian Fusion with Per-Splat Persistence and Change Visualization](https://arxiv.org/abs/2609.31339v1)**  
  Authors: Tobias Batik, Diana Marin, Peter Kán, Hannes Kaufmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31339v1.pdf)  
  Keywords: gaussian splatting, ar, outdoor  
- **[OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning](https://arxiv.org/abs/2609.29985v1)**  
  Authors: Haoran Wang, Shaoyu Cai, Adrian Azzarelli, Zhuodong Jiang, Guoxi Huang, Eng Tat Khoo, Brett Seymour, Fan Zhang, David Bull, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29985v1.pdf)  
  Keywords: gaussian splatting, ar, large scene, real-time rendering, 3d gaussian, nerf, compact, efficient, 3d reconstruction, fast  
- **[Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models](https://arxiv.org/abs/2609.26007v1)**  
  Authors: Yuhang Zhang, Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Weiying Wang, Steven Yang, Qingsong Yan, Chao Yan, Mir Feroskhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26007v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, motion, outdoor  
- **[Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking](https://arxiv.org/abs/2609.25746v1)**  
  Authors: Edward Beng Wai Tan, Siew-Kei Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25746v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, 3d gaussian, face, slam, tracking, outdoor  
- **[Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene Reconstruction](https://arxiv.org/abs/2609.23796v2)**  
  Authors: Yang-Tian Sun, Tianjia Liu, Zehuan Huang, Yi-Hua Huang, Xiaoyang Lyu, Ziyi Yang, Zi-Xin Zou, Yuan-Chen Guo, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23796v2.pdf)  
  Keywords: ar, geometry, high-fidelity, face, outdoor  
- **[Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization](https://arxiv.org/abs/2609.21347v1)**  
  Authors: Xiangfei Guo, Hao Shi, Yufan Zhang, Zhonghua Yi, Yongqi Mao, Xiaoting Yin, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21347v1.pdf) | [![GitHub](https://img.shields.io/github/stars/guoxf304/CubeSplat?style=social)](https://github.com/guoxf304/CubeSplat)  
  Keywords: gaussian splatting, ar, mapping, 3d gaussian, high-fidelity, face, slam, tracking, outdoor  
- **[4DGS-Fixer: Generative Sparse-View 4D Gaussian Splatting with Iterative Refinement Guided by Video Diffusion Priors](https://arxiv.org/abs/2609.21176v3)**  
  Authors: Haitao Huang, Shenghao Zhao, Boyuan Tian, Shin-Fang Chng, Songlin Yang, Sheila Lim, Huangying Zhan, Yi Xu, Anyi Rao, Frank Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21176v3.pdf)  
  Keywords: gaussian splatting, ar, large scene, dynamic, sparse-view, 4d  

### Model Compression

*Showing the latest 50 out of 205 papers*

- **[LVS: Local View Synthesis from Relative Camera Pose by Reusing Previous Views](https://arxiv.org/abs/2610.12127v1)**  
  Authors: Qizhou Huo, Xuan Sun, Yongfei Guo, Zhipeng Wang, Yuanhao Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12127v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, 3d gaussian, motion  
- **[2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map](https://arxiv.org/abs/2610.11752v1)**  
  Authors: Jiwon Park, Dong-Uk Seo, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11752v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://2dgs-planner.github.io)  
  Keywords: gaussian splatting, ar, geometry, efficient, face  
- **[CoCam4D: Geometry-Aware Cooperative 4D Perception for Camera-Only Autonomous Driving](https://arxiv.org/abs/2610.11577v1)**  
  Authors: Soham Pahari, Sudip Das, Arindam Das, Ujjwal Bhattacharya  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11577v1.pdf)  
  Keywords: ar, dynamic, geometry, autonomous driving, 3d gaussian, compact, efficient, 4d  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, geometry, dynamic, real-time rendering, 3d gaussian, face, illumination  
- **[MATE4D: Matrix-Guided Editable 4D Generation from a Single Image](https://arxiv.org/abs/2610.11181v1)**  
  Authors: Xiaotian Chen, Dongfu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11181v1.pdf)  
  Keywords: deformation, lightweight, ar, vr, dynamic, geometry, 3d gaussian, motion, 4d  
- **[DeltaSplat: Iterative Gaussian Refinement for Pose-Free Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2610.09853v1)**  
  Authors: Chanung Park, Seunghyeon Song, Joo Chan Lee, Eunbyung Park, Jong Hwan Ko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09853v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, 3d gaussian, efficient, head  
- **[Efficient 3D Gaussian Head Avatars for Edge Devices](https://arxiv.org/abs/2610.09821v1)**  
  Authors: Umar Farooq, Jean-Yves Guillemaut, Adrian Hilton, Marco Volino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09821v1.pdf)  
  Keywords: ar, efficient rendering, 3d gaussian, compression, efficient, head, avatar  
- **[DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video](https://arxiv.org/abs/2610.09720v1)**  
  Authors: Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09720v1.pdf)  
  Keywords: ar, dynamic, geometry, high-fidelity, efficient, 4d, outdoor  
- **[Gaussian Material Fields for Volumetric Multi-Energy CT Decomposition](https://arxiv.org/abs/2610.09492v1)**  
  Authors: Jian Lin, Jiancheng Fang, Hongming Shan, Shaoyu Wang, Yang Chen, Qiegen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09492v1.pdf)  
  Keywords: ar, 3d gaussian, geometry, efficient  
- **[LighTROcc: Lightweight 4D Occupancy Forecasting via Instance-Centric 3D Gaussians](https://arxiv.org/abs/2610.09444v1)**  
  Authors: Hwanhee Jung, SeungHyeon Kim, Inkyu Koo, Qixing Huang, Sang Ho Yoon, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09444v1.pdf)  
  Keywords: lightweight, ar, geometry, autonomous driving, 3d gaussian, compact, 4d  

### Quality Enhancement

*Showing the latest 50 out of 71 papers*

- **[DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video](https://arxiv.org/abs/2610.09720v1)**  
  Authors: Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09720v1.pdf)  
  Keywords: ar, dynamic, geometry, high-fidelity, efficient, 4d, outdoor  
- **[OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception](https://arxiv.org/abs/2610.07569v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07569v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/OpenSplatGraph)  
  Keywords: lightweight, gaussian splatting, ar, geometry, robotics, 3d gaussian, high-fidelity, efficient, understanding, mapping, semantic  
- **[SteadySplats: Resampling of Low-Variance Gaussians for High-Fidelity Stochastic Rendering](https://arxiv.org/abs/2610.05576v2)**  
  Authors: Felix Windisch, Thomas Köhler, Lukas Radl, Chris Wyman, Georgios Kopanas, Bernhard Kerbl, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05576v2.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, high-fidelity, efficient  
- **[Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting](https://arxiv.org/abs/2610.05289v1)**  
  Authors: Xiaobiao Du, Beixi Hao, Zhen Fang, Tianqing Zhu, Richard Hartley, Xin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05289v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiaobiaodu.github.io/mobile-4dgs-project)  
  Keywords: deformation, gaussian splatting, lightweight, ar, dynamic, 3d gaussian, high-fidelity, compact, motion, 4d, head  
- **[Return-to-Home Feasible Micro-Aerial Vehicle Exploration for 3D Gaussian Splatting Reconstruction](https://arxiv.org/abs/2610.04013v1)**  
  Authors: Prajit Krisshnakumar, Fan Yang, Koichiro Niinuma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04013v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, geometry, 3d gaussian, high-fidelity, 3d reconstruction, head  
- **[ManifoldSplat: Language-Guided Semantic Shape Editing of 3D Gaussian Head Avatars](https://arxiv.org/abs/2610.03599v1)**  
  Authors: Antonio Canela, Jordi Sànchez-Riera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03599v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://a-canela.github.io/manifoldsplat)  
  Keywords: gaussian splatting, ar, geometry, 3d gaussian, high-fidelity, animation, head, avatar, semantic  
- **[Budgeted-GS: Real-Time Large-Scale Gaussian Splatting via Factoring LOD](https://arxiv.org/abs/2610.03162v1)**  
  Authors: Haipeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03162v1.pdf)  
  Keywords: gaussian splatting, ar, high quality, 3d gaussian, real-time rendering  
- **[SCION: Scene Composition with Instanced Neural Primitives](https://arxiv.org/abs/2610.02322v2)**  
  Authors: William Koch, Amogh Joshi, Cyrus Vachha, Cheng Zheng, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02322v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://light.princeton.edu/SCION)  
  Keywords: human, lightweight, gaussian splatting, ar, high quality, 3d gaussian, animation, compact, compression  
- **[EffGS: Efficient and High-Fidelity Gaussian Splatting](https://arxiv.org/abs/2609.39553v1)**  
  Authors: Changbai Li, Shuo Yang, Yichen Yang, Shuwei Shao, Huobin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39553v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, high-fidelity, compact, acceleration, efficient  
- **[Gaussian Stippling: Efficient Sorting-Free 3D Gaussian Rendering through Hybrid Sampling and Spatiotemporal Reconstruction](https://arxiv.org/abs/2609.38488v1)**  
  Authors: Zijian Huang, Suiliang Mai, Chuankun Zheng, Yuan Meng, Yuchi Huo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38488v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, 3d gaussian, high-fidelity, efficient  

### Ray Tracing

- **[Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)**  
  Authors: Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/vorotracing)  
  Keywords: gaussian splatting, ar, real-time rendering, 3d gaussian, nerf, ray tracing, compact, fast, face, motion  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: gaussian splatting, ar, shadow, nerf, 3d gaussian, ray tracing, reflection, compact, efficient, fast, mapping  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, reflection, ray tracing, efficient, face, illumination, relighting  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: human, gaussian splatting, ar, geometry, dynamic, reflection, 3d gaussian, high-fidelity, ray tracing, face, motion  

### Relighting

- **[OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs](https://arxiv.org/abs/2610.12461v1)**  
  Authors: You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12461v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ouroworld.userwei.com)  
  Keywords: deformation, gaussian splatting, ar, dynamic, 3d gaussian, motion, 4d, illumination  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, geometry, dynamic, real-time rendering, 3d gaussian, face, illumination  
- **[3DTexMOR: 3D Gaussian Multi-Object Removal via Texture-Space Inpainting](https://arxiv.org/abs/2610.11198v1)**  
  Authors: Kunxin Guang, Yonghao Zhao, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11198v1.pdf)  
  Keywords: ar, geometry, reflection, nerf, 3d gaussian  
- **[Casual Flash Lighting for Gaussian Splat Inverse Rendering](https://arxiv.org/abs/2610.06035v1)**  
  Authors: Jiamin Xu, Dongheng Wei, Jiarong Zhao, Qi Wang, James Tompkin, Weiwei Xu, Gang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.06035v1.pdf)  
  Keywords: lighting, ar, geometry, illumination, relighting  
- **[VolS-GS: Relightable Gaussian Splatting with Volumetric Subsurface Scattering](https://arxiv.org/abs/2610.04007v2)**  
  Authors: Junyeong Ahn, Jaegul Choo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04007v2.pdf)  
  Keywords: lighting, relighting, gaussian splatting, ar, shadow, efficient, face, relightable  
- **[EvenSplat: Coupled 2D-3D Decomposition for Gaussian Splatting under Exposure and Illumination Variation](https://arxiv.org/abs/2610.01876v1)**  
  Authors: Tongyu Wu, Jacob Edwards, Ziteng Cui, Caigui Jiang, Cheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01876v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, geometry, shadow, 3d gaussian, face, illumination  
- **[EndoPrior-GS: Dynamic Endoscopic Reconstruction with a Joint Texture Prior](https://arxiv.org/abs/2609.37874v1)**  
  Authors: Jiaqi Huang, Shidong Wang, Tong Xin, Kabita Adhikari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiaqi-huang-77.github.io/EndoPrior-GS)  
  Keywords: gaussian splatting, ar, geometry, dynamic, real-time rendering, 3d gaussian, nerf, illumination  
- **[CollisionSplatting: Collision-Aware Motion Planning in 3DGS Scenes with Image-Conditioned Objectives and Adjustable Conservatism](https://arxiv.org/abs/2609.35619v1)**  
  Authors: R. Khorrambakht, Joaquim Ortiz-Haro, Stephan Weiss, Ludovic Righetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35619v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, vr, 3d gaussian, motion  
- **[PePESeg3D: Perception Prior Enhances Multi-Scale Segmentation for 3D Gaussian Splatting](https://arxiv.org/abs/2609.28645v1)**  
  Authors: Sungjae Choi, Seunghee Koh, Junmo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28645v1.pdf) | [![GitHub](https://img.shields.io/github/stars/BeCow5X5/PePESeg3D?style=social)](https://github.com/BeCow5X5/PePESeg3D)  
  Keywords: lighting, gaussian splatting, ar, geometry, nerf, 3d gaussian, segmentation, semantic  
- **[Relightable 3D Avatar Reconstruction with Semantic-Adaptive Motion-Illumination Responses](https://arxiv.org/abs/2609.24158v1)**  
  Authors: Jiankuo Zhao, Xiangyu Zhu, Jijie Li, Baiqin Wang, Shukai Chen, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24158v1.pdf)  
  Keywords: lighting, relighting, avatar, lightweight, ar, 3d gaussian, animation, compact, motion, head, illumination, relightable, semantic  

### SLAM

*Showing the latest 50 out of 76 papers*

- **[OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception](https://arxiv.org/abs/2610.07569v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07569v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/OpenSplatGraph)  
  Keywords: lightweight, gaussian splatting, ar, geometry, robotics, 3d gaussian, high-fidelity, efficient, understanding, mapping, semantic  
- **[SURGE: Sonar-fUsed Reconstruction and localization via image-gated Graph Estimation](https://arxiv.org/abs/2610.07472v1)**  
  Authors: Mohammed Ibrahim M, Vallabh Deogaonkar, Trung Dong, Jane Shin, Abhilash Somayajula, Xiaomin Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07472v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, compact, localization, understanding  
- **[FOCUS: Fine-Grained Open-Vocabulary Change Detection for Uncertainty-Aware Semi-Static Scenes](https://arxiv.org/abs/2610.05639v1)**  
  Authors: Can Xu, Mingfeng Yuan, Mahan Mohammadi, Steven L. Waslander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05639v1.pdf)  
  Keywords: ar, geometry, 3d gaussian, mapping, semantic  
- **[CellSplat4D: PSF-Aware 4D Gaussian Splatting for Sparse Robotic Live-Cell Imaging](https://arxiv.org/abs/2610.04199v1)**  
  Authors: Yingda Tao, Guoyu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04199v1.pdf)  
  Keywords: gaussian splatting, ar, motion, 4d, tracking  
- **[VoxelSynth3D: Interpretable Volumetric Image-Domain Metal Artifact Reduction with a Paired Synthetic CLINIC-Metal Benchmark](https://arxiv.org/abs/2610.01512v1)**  
  Authors: Amritesh Banerjee, Abdul Basit, Renil Renji Joseph, Nouhaila Innan, Muhammad Shafique  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01512v1.pdf)  
  Keywords: localization, 3d gaussian, ar, face  
- **[Lens Flare Removal and Reconstruction](https://arxiv.org/abs/2609.39527v1)**  
  Authors: Tarun Yenamandra, Jonathon Luiten, Daniel Cremers, Nathan Matsuda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39527v1.pdf)  
  Keywords: gaussian splatting, ar, localization  
- **[DispFlow-GS: Displacement Flow Supervision with Motion Disentangling for Monocular Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2609.36940v1)**  
  Authors: Thai Duy Nguyen, Haitian Zhang, Addison Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36940v1.pdf)  
  Keywords: deformation, gaussian splatting, ar, dynamic, geometry, 3d gaussian, localization, motion  
- **[EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation](https://arxiv.org/abs/2609.34853v1)**  
  Authors: Sungho Moon, Kota Shimomura, Junwoo Park, Wonhyeok Choi, Seunghun Lee, Takayoshi Yamashita, Sunghoon Im  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34853v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, compact, segmentation, localization, understanding  
- **[Reliability-Regulated Trajectory Optimization for Progressive COLMAP-Free 3D Gaussian Splatting](https://arxiv.org/abs/2609.30865v1)**  
  Authors: Zijian Wu, Jinliang Wang, Zidian Lin, Ying Song, Ziqian Lu, Hanjie Ma, Zhen Ye, Mingfeng Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30865v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Zijian1026/RRTO-CF3DGS?style=social)](https://github.com/Zijian1026/RRTO-CF3DGS)  
  Keywords: gaussian splatting, ar, dynamic, 3d gaussian, motion, tracking  
- **[SplatLabel: Pseudo-Labelling through 4D Gaussian Splatting](https://arxiv.org/abs/2609.29836v1)**  
  Authors: Nitya Nanvani, Andras Palffy, Holger Caesar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29836v1.pdf)  
  Keywords: gaussian splatting, ar, dynamic, geometry, segmentation, 4d, tracking, semantic  

### Scene Understanding

*Showing the latest 50 out of 98 papers*

- **[PCAsplat: Gaussian Splatting with Local PCA Regularization](https://arxiv.org/abs/2610.11011v1)**  
  Authors: Vitor Matias, Filipe Nascimento, Kiyohiro Nakayama, João Paulo Lima, Márcus Lobo, Gordon Wetzstein, Leonidas Guibas, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11011v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, nerf, segmentation, face, 3d reconstruction  
- **[Post-Training Semantic Lifting for 3D Gaussian Splatting: Separating Detector, Lifting and Representation Error](https://arxiv.org/abs/2610.08756v1)**  
  Authors: Iván Verdugo Guerra, Ezequiel López Rubio, Jorge García González  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.08756v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, semantic  
- **[View Matters: Keyframe-Guided Text-Driven 3D Gaussian Editing](https://arxiv.org/abs/2610.08179v1)**  
  Authors: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Xuanyu Wang, Feng Lei, Sha Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.08179v1.pdf)  
  Keywords: ar, 3d gaussian, semantic  
- **[OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception](https://arxiv.org/abs/2610.07569v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07569v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/OpenSplatGraph)  
  Keywords: lightweight, gaussian splatting, ar, geometry, robotics, 3d gaussian, high-fidelity, efficient, understanding, mapping, semantic  
- **[SURGE: Sonar-fUsed Reconstruction and localization via image-gated Graph Estimation](https://arxiv.org/abs/2610.07472v1)**  
  Authors: Mohammed Ibrahim M, Vallabh Deogaonkar, Trung Dong, Jane Shin, Abhilash Somayajula, Xiaomin Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07472v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, compact, localization, understanding  
- **[MoonGS: High-quality Representation of the Lunar Surface via Gaussian Splatting Using Robust Depth Features from Image Pairs](https://arxiv.org/abs/2610.07110v1)**  
  Authors: Yun Jiang, Bo Zheng, Yingying Zhang, Xueming Xiao, Tao Hu, Hutao Cui, Zhiguo Meng, Ke Gao, Yang Gao, Meibao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07110v1.pdf) | [![GitHub](https://img.shields.io/github/stars/InRobots/MoonBlender?style=social)](https://github.com/InRobots/MoonBlender)  
  Keywords: gaussian splatting, ar, nerf, 3d gaussian, face, 3d reconstruction, head, semantic  
- **[MaRO-GS: Mask-Robust Object-Centric Gaussian Splatting from Inconsistent Multi-view Masks](https://arxiv.org/abs/2610.06472v1)**  
  Authors: Eunji Kim, Gahyeon Kim, Gianella Cravioto, Dong-hun Lee, Chaewon Moon, Chae-yeong Song, Sang-hyo Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.06472v1.pdf)  
  Keywords: gaussian splatting, ar, head, segmentation  
- **[FOCUS: Fine-Grained Open-Vocabulary Change Detection for Uncertainty-Aware Semi-Static Scenes](https://arxiv.org/abs/2610.05639v1)**  
  Authors: Can Xu, Mingfeng Yuan, Mahan Mohammadi, Steven L. Waslander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05639v1.pdf)  
  Keywords: ar, geometry, 3d gaussian, mapping, semantic  
- **[GS-Codec: A Gaussian-Splatting Bottleneck for Neural Audio Coding](https://arxiv.org/abs/2610.04651v1)**  
  Authors: Ron Aluf, Alon Canfi, Eliya Nachmani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04651v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ronaluf.github.io/gs-codec)  
  Keywords: lightweight, gaussian splatting, ar, compact, semantic  
- **[ManifoldSplat: Language-Guided Semantic Shape Editing of 3D Gaussian Head Avatars](https://arxiv.org/abs/2610.03599v1)**  
  Authors: Antonio Canela, Jordi Sànchez-Riera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03599v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://a-canela.github.io/manifoldsplat)  
  Keywords: gaussian splatting, ar, geometry, 3d gaussian, high-fidelity, animation, head, avatar, semantic  



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
