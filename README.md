# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-gaussians/)**: an interactive paper map, monthly trends, topic network and co-author network of every tracked paper.

> Last Update: 2026-10-22 02:24:22

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

- [3DGS Surveys](#3dgs-surveys) (6 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (73 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (500 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (158 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (191 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (41 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (205 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (24 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (193 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (61 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (3 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (41 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (76 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (100 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Gaussian Splatting for Real-Time Scene Reconstruction: Methods, Systems, and Trade-offs](https://arxiv.org/abs/2610.17513v1)**  
  Authors: Ashim Dahal, Rabab Abdelfattah, Nick Rahimi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17513v1.pdf)  
  Keywords: 3d gaussian, ar, real-time rendering, sparse-view, compression, slam, localization, mapping, survey, tracking, gaussian splatting, dynamic  
- **[GS-Pool: Object-Level Change Detection in 3D Gaussian Splatting](https://arxiv.org/abs/2610.06688v1)**  
  Authors: Boaz Keren-Gil, James Gain, Patrick Marais  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.06688v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, survey, gaussian splatting  
- **[OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones](https://arxiv.org/abs/2609.24253v1)**  
  Authors: Zhongrui You, Zhen Li, Junli Liu, Zhigang Wang, Bin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24253v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://openflyscan.github.io)  
  Keywords: 3d gaussian, ar, high-fidelity, face, survey, gaussian splatting  
- **[Quality Assessment of 3D Gaussian Splatting: Distortions, Benchmarks, and Open Challenges](https://arxiv.org/abs/2609.23027v1)**  
  Authors: Shuai Liu, Binqiang Liu, Qingyu Mao, Jiacong Chen, Yongsheng Liang, Youneng Bao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23027v1.pdf)  
  Keywords: 3d gaussian, ar, compression, survey, gaussian splatting  
- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: ar, 3d reconstruction, motion, geometry, illumination, survey, gaussian splatting  
- **[UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys](https://arxiv.org/abs/2608.06404v1)**  
  Authors: Junxiong Zhou, Xuechen Li, Chonghao Qiu, Lang Qiao, Xiaowei Jia, Qi Yang, Chishan Zhang, Leikun Yin, Nanshan You, Vipin Kumar, David Mulla, Ce Yang, Zhenong Jin, Licheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06404v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://link-dev.github.io/UAV3DCrop)  
  Keywords: 3d gaussian, ar, 3d reconstruction, geometry, survey, nerf, gaussian splatting, dynamic  

### Acceleration

*Showing the latest 50 out of 73 papers*

- **[KoalaGS: Complexity-Aware Continuous Level of Detail for Gaussian Splatting](https://arxiv.org/abs/2610.28615v1)**  
  Authors: Radu Beche, Raoul de Charette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28615v1.pdf)  
  Keywords: 3d gaussian, fast, ar, gaussian splatting  
- **[Learning from Automatic 3D Gaussian Splatting Edits for Online Bayesian Scene Change Detection](https://arxiv.org/abs/2610.28490v1)**  
  Authors: Changrui Zhu, Simon Julier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28490v1.pdf)  
  Keywords: 3d gaussian, fast, ar, gaussian splatting  
- **[RLSplat: Resource-Linear Budget Control for Feed-forward 3D Gaussian Splatting](https://arxiv.org/abs/2610.27712v1)**  
  Authors: Injae Kim, Minseok Joo, Jihwan Park, Sehyung Kim, Minseong Bae, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.27712v1.pdf)  
  Keywords: 3d gaussian, ar, fast, efficient, gaussian splatting  
- **[Localization and Neural Splatting on the Edge: An FPGA Scene Memory for Robots](https://arxiv.org/abs/2610.25068v1)**  
  Authors: Que Haohua, Mingkai Liu, Handong Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25068v1.pdf)  
  Keywords: 3d gaussian, ar, fast, acceleration, localization, gaussian splatting  
- **[SwitchSplat: Learning Discrete Object States from Casually Captured Scenes](https://arxiv.org/abs/2610.24812v2)**  
  Authors: Yizheng Xie, Yalda Foroutan, George Shramko, Daniel Rebain, Shrisudhan Govindarajan, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24812v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://switchsplat.github.io)  
  Keywords: 3d gaussian, ar, high-fidelity, 3d reconstruction, geometry, 4d, fast, gaussian splatting, dynamic  
- **[RoMo-GS: Efficient Online 3D Gaussian Splatting for Robot Mapping via Exposure-Integrated Motion Blur](https://arxiv.org/abs/2610.24605v1)**  
  Authors: Sangwoo Jung, Di Deng, Jiahui Fu, Laura Herlant, Ayoung Kim, Yafei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24605v1.pdf)  
  Keywords: 3d gaussian, ar, motion, robotics, geometry, fast, mapping, efficient, gaussian splatting  
- **[EGGHead: Efficient Generalizable Gaussian Heads from a Single Image](https://arxiv.org/abs/2610.26898v1)**  
  Authors: Pilseo Park, Andrew Hou, Michel Sarkis, Ning Bi, Yiying Tong, Xiaoming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26898v1.pdf)  
  Keywords: ar, human, real-time rendering, face, semantic, efficient, nerf, head, gaussian splatting  
- **[Direct Conditional Parameterization for N-Dimensional Splatting](https://arxiv.org/abs/2610.22778v1)**  
  Authors: Zhongpai Gao, Benjamin Planche, Van Nguyen Nguyen, Meng Zheng, Anwesa Choudhuri, Arun Innanje, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22778v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/dgs)  
  Keywords: 3d gaussian, ar, fast, gaussian splatting, dynamic  
- **[Physical-Field-Bridged Material Parameter Inference from Multi-View Deformation Videos](https://arxiv.org/abs/2610.17591v1)**  
  Authors: Linrui Shou, Jie Li, Yu Liu, Tao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17591v1.pdf)  
  Keywords: motion, fast, ar, deformation  
- **[Gaussian Splatting for Real-Time Scene Reconstruction: Methods, Systems, and Trade-offs](https://arxiv.org/abs/2610.17513v1)**  
  Authors: Ashim Dahal, Rabab Abdelfattah, Nick Rahimi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17513v1.pdf)  
  Keywords: 3d gaussian, ar, real-time rendering, sparse-view, compression, slam, localization, mapping, survey, tracking, gaussian splatting, dynamic  

### Applications

*Showing the latest 50 out of 500 papers*

- **[ClunoGS: Compact Language 3D Gaussian Splatting via Unified Optimization](https://arxiv.org/abs/2610.30013v1)**  
  Authors: Jian Xu, Yi Li, Ying Huang, Siyi Wu, Bingzhe Li, Yuede Ji, Miao Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.30013v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, compression, compact, semantic, localization, segmentation, gaussian splatting  
- **[AirPlayground: Benchmarking Aerial Navigation across Diverse Reconstructed Environments](https://arxiv.org/abs/2610.29699v1)**  
  Authors: Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Mingsheng Li, Qingsong Yan, Chao Yan, Yuhang Zhang, Mir Feroskhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29699v1.pdf)  
  Keywords: 3d gaussian, ar, outdoor, geometry, gaussian splatting  
- **[AutoPhyX: Automatic Text-Condition Physics Property Generation](https://arxiv.org/abs/2610.29517v1)**  
  Authors: Bei Huang, Yixin Chen, Hongbin Zha, Yuru Pei, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29517v1.pdf)  
  Keywords: ar, high-fidelity, 4d, semantic, nerf, gaussian splatting, dynamic  
- **[AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2610.29374v1)**  
  Authors: Rodion Shkokov, Tatiana Zemskova, Dmitry Yudin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29374v1.pdf) | [![GitHub](https://img.shields.io/github/stars/OptimusFaber/AOV-GS?style=social)](https://github.com/OptimusFaber/AOV-GS)  
  Keywords: 3d gaussian, ar, human, geometry, lightweight, semantic, segmentation, mapping, gaussian splatting  
- **[Real2Sem2Real: 3D Semantic Augmentations for Robot Learning from a Single Human RGB Demonstration](https://arxiv.org/abs/2610.28880v1)**  
  Authors: Matthew Strong, Ankush K. Dhawan, Julien Poffet, Giuse Pham, Jinho So, Monroe Kennedy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28880v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2sem2real.github.io)  
  Keywords: ar, human, semantic  
- **[AEON: Unifying Video and 3D World Models](https://arxiv.org/abs/2610.28631v1)**  
  Authors: Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu, Junsheng Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28631v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weiqi-zhang.github.io/AEON)  
  Keywords: 4d, ar, gaussian splatting, dynamic  
- **[KoalaGS: Complexity-Aware Continuous Level of Detail for Gaussian Splatting](https://arxiv.org/abs/2610.28615v1)**  
  Authors: Radu Beche, Raoul de Charette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28615v1.pdf)  
  Keywords: 3d gaussian, fast, ar, gaussian splatting  
- **[SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images](https://arxiv.org/abs/2610.28585v1)**  
  Authors: Rundong Luo, Yunong Liu, Di Cao, Matthew Tancik, Shyamal Buch, Colton Stearns, Wenqi Xian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28585v1.pdf)  
  Keywords: ar, robotics, segmentation  
- **[CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding](https://arxiv.org/abs/2610.28530v1)**  
  Authors: Om Shivam Verma, Shaya Farahmand, Lingjun Zhao, Lu Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28530v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, geometry, compact, semantic, lighting  
- **[Learning from Automatic 3D Gaussian Splatting Edits for Online Bayesian Scene Change Detection](https://arxiv.org/abs/2610.28490v1)**  
  Authors: Changrui Zhu, Simon Julier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28490v1.pdf)  
  Keywords: 3d gaussian, fast, ar, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 158 papers*

- **[AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2610.29374v1)**  
  Authors: Rodion Shkokov, Tatiana Zemskova, Dmitry Yudin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29374v1.pdf) | [![GitHub](https://img.shields.io/github/stars/OptimusFaber/AOV-GS?style=social)](https://github.com/OptimusFaber/AOV-GS)  
  Keywords: 3d gaussian, ar, human, geometry, lightweight, semantic, segmentation, mapping, gaussian splatting  
- **[Real2Sem2Real: 3D Semantic Augmentations for Robot Learning from a Single Human RGB Demonstration](https://arxiv.org/abs/2610.28880v1)**  
  Authors: Matthew Strong, Ankush K. Dhawan, Julien Poffet, Giuse Pham, Jinho So, Monroe Kennedy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28880v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2sem2real.github.io)  
  Keywords: ar, human, semantic  
- **[World2HOSI: A Multi-Expert Harness for Long-Horizon Human-Object-Scene Interaction Generation](https://arxiv.org/abs/2610.27725v1)**  
  Authors: Jiushu Li, Haoran Wang, Yumeng Liu, Zhiyang Dou, Yuan Liu, Yuexin Ma, Cheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.27725v1.pdf)  
  Keywords: 3d gaussian, ar, human, animation, face, motion, gaussian splatting  
- **[SplatXR: A Toolkit for Multi-Layered Extended Reality via On-Headset 3D Gaussian Splatting](https://arxiv.org/abs/2610.26338v1)**  
  Authors: Cyrus Vachha, Mohamed Kari, Parastoo Abtahi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26338v1.pdf)  
  Keywords: 3d gaussian, ar, face, geometry, shadow, head, gaussian splatting  
- **[RxGS: Relightable Gaussian Stylization via BRDF Decomposition](https://arxiv.org/abs/2610.25681v1)**  
  Authors: Wanrong Hong, Liu Jiang, Mukesh Prasad, Jun Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25681v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, nerf, face, geometry, illumination, relightable, gaussian splatting  
- **[MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345v1)**  
  Authors: Yifei Wang, Wei Tian, Wenhua Bao, Jia Zhou, Hanshi Wang, Fudong Ge, Jianhua Wu, Shuai Yuan, Zhipeng Zhang, Xingliang Liu, Xianming Zeng, Jianyun Xu, Bingzhao Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25345v1.pdf)  
  Keywords: ar, face, geometry, illumination, gaussian splatting  
- **[Arbitrary-Scale Anisotropic 3D MRI Super-Resolution with Gaussian Prototypes](https://arxiv.org/abs/2610.24858v2)**  
  Authors: Aditya Rastogi, Ramon Leiser, Prateek Singh, Martha Foltyn-Dumitru, Martin Bendszus, Fabian Bamberg, Klaus Maier-Hein, Kai Schlamp, Alexander Radbruch, Gianluca Brugnara, Philipp Vollmuth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24858v2.pdf)  
  Keywords: 3d gaussian, ar, motion, geometry, segmentation, head  
- **[Directionally Factorized Illumination with Spherical Harmonic Rotation](https://arxiv.org/abs/2610.24811v1)**  
  Authors: Yimeng Dou, Adam M. Saunders, Andre T. S. Hucke, Michael E. Kim, Adam W. Anderson, Eric R. Tkaczyk, Bennett A. Landman, Daniel Moyer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24811v1.pdf)  
  Keywords: ar, gaussian splatting, face, geometry, illumination, neural rendering, nerf, medical, lighting  
- **[HumanSkill-4D: Training-Free Language Querying of Animatable Gaussian Avatars in Space and Time](https://arxiv.org/abs/2610.24452v2)**  
  Authors: Junsu Kim, Naeun Kim, Dongyoon Han, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24452v2.pdf)  
  Keywords: ar, human, motion, compact, 4d, semantic, avatar, segmentation, body, gaussian splatting  
- **[EGGHead: Efficient Generalizable Gaussian Heads from a Single Image](https://arxiv.org/abs/2610.26898v1)**  
  Authors: Pilseo Park, Andrew Hou, Michel Sarkis, Ning Bi, Yiying Tong, Xiaoming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26898v1.pdf)  
  Keywords: ar, human, real-time rendering, face, semantic, efficient, nerf, head, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 191 papers*

- **[AutoPhyX: Automatic Text-Condition Physics Property Generation](https://arxiv.org/abs/2610.29517v1)**  
  Authors: Bei Huang, Yixin Chen, Hongbin Zha, Yuru Pei, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29517v1.pdf)  
  Keywords: ar, high-fidelity, 4d, semantic, nerf, gaussian splatting, dynamic  
- **[AEON: Unifying Video and 3D World Models](https://arxiv.org/abs/2610.28631v1)**  
  Authors: Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu, Junsheng Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28631v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weiqi-zhang.github.io/AEON)  
  Keywords: 4d, ar, gaussian splatting, dynamic  
- **[SplatFlux: Feed-Forward 4D Gaussian Reconstruction and Generation from Video Latents](https://arxiv.org/abs/2610.28257v1)**  
  Authors: Runmin Zhang, Binglin Ren, Zhu Yu, Fudong Wang, Jiangke Lin, Yichun Shentu, Si-Yuan Cao, Yi Yuan, Hui-Liang Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28257v1.pdf)  
  Keywords: ar, motion, compact, 4d, dynamic  
- **[CrossFit-GS: Out-of-Fold Pose Estimation for COLMAP-Free 3D Gaussian Splatting](https://arxiv.org/abs/2610.28190v1)**  
  Authors: Zijian Wu, Jinliang Wang, Mingfeng Jiang, Zidian Lin, Ying Song, Ziqian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28190v1.pdf)  
  Keywords: 3d gaussian, ar, motion, gaussian splatting  
- **[World2HOSI: A Multi-Expert Harness for Long-Horizon Human-Object-Scene Interaction Generation](https://arxiv.org/abs/2610.27725v1)**  
  Authors: Jiushu Li, Haoran Wang, Yumeng Liu, Zhiyang Dou, Yuan Liu, Yuexin Ma, Cheng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.27725v1.pdf)  
  Keywords: 3d gaussian, ar, human, animation, face, motion, gaussian splatting  
- **[Drive2Gauss: FeedForward 4D Gaussian Reconstruction from Multimodal Generative Driving Videos](https://arxiv.org/abs/2610.26585v1)**  
  Authors: Tong Zhao, Zhiyuan Han, Lin Chen, Bowen Xie, Yunxi Qiao, Bohan Li, Weiqing Xiao, Gen Li, Shu Han, Xuyang Dai, Cheng Bi, Hao Zhao, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26585v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zttt04)  
  Keywords: 4d, ar, dynamic  
- **[PhysSkin++: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning](https://arxiv.org/abs/2610.26067v1)**  
  Authors: Yuanhang Lei, Baofei Liu, Xingxuan Li, Tao Cheng, Zixuan Wang, Boming Zhao, Yujun Shen, Siyuan Huang, Ruizhen Hu, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26067v1.pdf)  
  Keywords: 3d gaussian, ar, animation, compact, efficient, deformation, dynamic  
- **[Rethinking Sparse-View 3D Gaussian Splatting: A Few-Shot Learning Perspective on Overfitting Prevention](https://arxiv.org/abs/2610.25887v1)**  
  Authors: Lejia Ye, Bin Wu, Jingjing Gao, Yiyang Wu, Xiaohu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25887v1.pdf)  
  Keywords: 3d gaussian, ar, motion, sparse-view, few-shot, geometry, vr, gaussian splatting, dynamic  
- **[Arbitrary-Scale Anisotropic 3D MRI Super-Resolution with Gaussian Prototypes](https://arxiv.org/abs/2610.24858v2)**  
  Authors: Aditya Rastogi, Ramon Leiser, Prateek Singh, Martha Foltyn-Dumitru, Martin Bendszus, Fabian Bamberg, Klaus Maier-Hein, Kai Schlamp, Alexander Radbruch, Gianluca Brugnara, Philipp Vollmuth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24858v2.pdf)  
  Keywords: 3d gaussian, ar, motion, geometry, segmentation, head  
- **[SwitchSplat: Learning Discrete Object States from Casually Captured Scenes](https://arxiv.org/abs/2610.24812v2)**  
  Authors: Yizheng Xie, Yalda Foroutan, George Shramko, Daniel Rebain, Shrisudhan Govindarajan, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24812v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://switchsplat.github.io)  
  Keywords: 3d gaussian, ar, high-fidelity, 3d reconstruction, geometry, 4d, fast, gaussian splatting, dynamic  

### Few-shot

- **[Rethinking Sparse-View 3D Gaussian Splatting: A Few-Shot Learning Perspective on Overfitting Prevention](https://arxiv.org/abs/2610.25887v1)**  
  Authors: Lejia Ye, Bin Wu, Jingjing Gao, Yiyang Wu, Xiaohu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25887v1.pdf)  
  Keywords: 3d gaussian, ar, motion, sparse-view, few-shot, geometry, vr, gaussian splatting, dynamic  
- **[Holi-Spatial 360: Generative Reconstruction from Sparse Panoramas for Spatial Rendering and Intelligence](https://arxiv.org/abs/2610.19502v1)**  
  Authors: Yuanyuan Gao, Zhirui Liu, Yuning Gong, Yifei Liu, Yifan Zhan, Kuixuan Jiao, Xiaolong Zhou, Yifan Yang, Hongjie Zhang, Xue Yang, Dan Xu, Zhihang Zhong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19502v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, semantic, sparse view, gaussian splatting  
- **[Gaussian Splatting for Real-Time Scene Reconstruction: Methods, Systems, and Trade-offs](https://arxiv.org/abs/2610.17513v1)**  
  Authors: Ashim Dahal, Rabab Abdelfattah, Nick Rahimi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17513v1.pdf)  
  Keywords: 3d gaussian, ar, real-time rendering, sparse-view, compression, slam, localization, mapping, survey, tracking, gaussian splatting, dynamic  
- **[AD-GS: Anatomical Density-guided 3D Gaussian Splatting for Sparse-View Dental CBCT Reconstruction](https://arxiv.org/abs/2610.14963v1)**  
  Authors: Zonglin Li, Kexian Xie, Feiran Li, Chu Zhou, Yixing Huang, Ruiyang Chen, Zhanyu Ma, Heng Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.14963v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yulinjiaxue/AD-GS-BMVC2026?style=social)](https://github.com/yulinjiaxue/AD-GS-BMVC2026)  
  Keywords: 3d gaussian, ar, sparse-view, semantic, medical, gaussian splatting  
- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: 3d gaussian, ar, high-fidelity, face, geometry, compact, sparse view, gaussian splatting, dynamic  
- **[OX-NeRF: 3D X-ray Tomography Reconstruction from Sparse Views Using Implicit Neural Representation](https://arxiv.org/abs/2610.11547v1)**  
  Authors: Thomas Welsch, Min-Hsin Tu, David J. Chapman, Daniel E. Eakins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11547v1.pdf)  
  Keywords: ar, 3d reconstruction, sparse view, nerf, gaussian splatting  
- **[DensiTok: Making Feed-Forward 3D Gaussian Splatting See More Views Than It Is Given](https://arxiv.org/abs/2610.07958v1)**  
  Authors: Minhyeok Lee, Jungho Lee, Minseok Kang, Heeseung Choi, Ig-Jae Kim, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07958v1.pdf)  
  Keywords: 3d gaussian, ar, sparse-view, geometry, compact, head, gaussian splatting  
- **[Sparse-View 4D Gaussian Splatting via Spatiotemporal Priors and Generative Assistance](https://arxiv.org/abs/2610.04606v2)**  
  Authors: Shengqi Wang, Zhengxian Yang, Kaiwen Tian, Yang Liu, Bowen Liu, Hua Du, Taicheng Huang, Jiamin Wu, Tao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04606v2.pdf)  
  Keywords: ar, motion, sparse-view, geometry, 4d, sparse view, gaussian splatting, dynamic  
- **[Sparse-GS2Mesh: 3D Gaussian Splatting Guided by Novel Stereo Views and 2DGS for Sparse View Surface Reconstruction](https://arxiv.org/abs/2610.04203v3)**  
  Authors: Younghyun Noh, Minje Kim, Tae-Kyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04203v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yhnoh8623.github.io/projects/s-gs2mesh)  
  Keywords: 3d gaussian, ar, face, sparse-view, geometry, efficient, sparse view, gaussian splatting  
- **[UGOD: Uncertainty-Guided Opacity and Dropout for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.39089v1)**  
  Authors: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Chenghao Qian, Ziyang Wang, Xinqi Fan, Liangxiu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39089v1.pdf)  
  Keywords: 3d gaussian, ar, sparse-view, compact, lightweight, nerf, head, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 205 papers*

- **[AirPlayground: Benchmarking Aerial Navigation across Diverse Reconstructed Environments](https://arxiv.org/abs/2610.29699v1)**  
  Authors: Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Mingsheng Li, Qingsong Yan, Chao Yan, Yuhang Zhang, Mir Feroskhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29699v1.pdf)  
  Keywords: 3d gaussian, ar, outdoor, geometry, gaussian splatting  
- **[AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2610.29374v1)**  
  Authors: Rodion Shkokov, Tatiana Zemskova, Dmitry Yudin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29374v1.pdf) | [![GitHub](https://img.shields.io/github/stars/OptimusFaber/AOV-GS?style=social)](https://github.com/OptimusFaber/AOV-GS)  
  Keywords: 3d gaussian, ar, human, geometry, lightweight, semantic, segmentation, mapping, gaussian splatting  
- **[CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding](https://arxiv.org/abs/2610.28530v1)**  
  Authors: Om Shivam Verma, Shaya Farahmand, Lingjun Zhao, Lu Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28530v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, geometry, compact, semantic, lighting  
- **[PanoGraphGS: Unifying Panoptic Segmentation and Hierarchical 3D Scene Graphs with Gaussian Splatting](https://arxiv.org/abs/2610.27696v1)**  
  Authors: Jinghan Gao, Siyu Wang, Dongyu Feng, Yiyuan Pan, Rong Xiong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.27696v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gaojh0333/PanoGraphGS?style=social)](https://github.com/gaojh0333/PanoGraphGS)  
  Keywords: 3d gaussian, ar, understanding, geometry, semantic, segmentation, gaussian splatting  
- **[Counting Contributions, Not Views: Occlusion-Aware Densification for 3D Gaussian Splatting](https://arxiv.org/abs/2610.27108v1)**  
  Authors: Marcel Rogge, René Schuster, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.27108v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, large scene, gaussian splatting  
- **[Learning Geometry-Aware Planning Representations for Monocular Flight with Cross-Modal Supervision](https://arxiv.org/abs/2610.26508v1)**  
  Authors: Wencan Feng, Bailing Tian, Yulin Hui, Zhiyu Li, Junjie Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26508v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting  
- **[SplatXR: A Toolkit for Multi-Layered Extended Reality via On-Headset 3D Gaussian Splatting](https://arxiv.org/abs/2610.26338v1)**  
  Authors: Cyrus Vachha, Mohamed Kari, Parastoo Abtahi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26338v1.pdf)  
  Keywords: 3d gaussian, ar, face, geometry, shadow, head, gaussian splatting  
- **[Rethinking Sparse-View 3D Gaussian Splatting: A Few-Shot Learning Perspective on Overfitting Prevention](https://arxiv.org/abs/2610.25887v1)**  
  Authors: Lejia Ye, Bin Wu, Jingjing Gao, Yiyang Wu, Xiaohu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25887v1.pdf)  
  Keywords: 3d gaussian, ar, motion, sparse-view, few-shot, geometry, vr, gaussian splatting, dynamic  
- **[RxGS: Relightable Gaussian Stylization via BRDF Decomposition](https://arxiv.org/abs/2610.25681v1)**  
  Authors: Wanrong Hong, Liu Jiang, Mukesh Prasad, Jun Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25681v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, nerf, face, geometry, illumination, relightable, gaussian splatting  
- **[MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345v1)**  
  Authors: Yifei Wang, Wei Tian, Wenhua Bao, Jia Zhou, Hanshi Wang, Fudong Ge, Jianhua Wu, Shuai Yuan, Zhipeng Zhang, Xingliang Liu, Xianming Zeng, Jianyun Xu, Bingzhao Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25345v1.pdf)  
  Keywords: ar, face, geometry, illumination, gaussian splatting  

### Large Scene

- **[AirPlayground: Benchmarking Aerial Navigation across Diverse Reconstructed Environments](https://arxiv.org/abs/2610.29699v1)**  
  Authors: Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Mingsheng Li, Qingsong Yan, Chao Yan, Yuhang Zhang, Mir Feroskhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29699v1.pdf)  
  Keywords: 3d gaussian, ar, outdoor, geometry, gaussian splatting  
- **[Counting Contributions, Not Views: Occlusion-Aware Densification for 3D Gaussian Splatting](https://arxiv.org/abs/2610.27108v1)**  
  Authors: Marcel Rogge, René Schuster, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.27108v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, large scene, gaussian splatting  
- **[HyperLoop: Hyperspectral-Assisted Loop Closure Detection in 3D-SLAM for Planetary Exploration](https://arxiv.org/abs/2610.19742v1)**  
  Authors: Annie Bhalla, Dennis Rotondi, Riccardo Giubilato, Kai O. Arras, Wolfgang Stuerzl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19742v1.pdf)  
  Keywords: 3d gaussian, ar, outdoor, slam, mapping, illumination, gaussian splatting  
- **[I2O2I-Nav: A Benchmark with a Modular Agent for Long-Horizon Indoor-to-Outdoor-to-Indoor Navigation](https://arxiv.org/abs/2610.18307v1)**  
  Authors: Zhengjie Shu, Wanyu Li, Di Xiao, Lingxin Jiang, Lai Jiang, Kaidi Hu, Xincheng Tang, Wenkang Hu, Haoran Wang, Jinchuan Zhang, Chang Chen, Wei Li, Jia Pan, Ruigang Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.18307v1.pdf)  
  Keywords: ar, outdoor, geometry  
- **[3D Gaussian Splatting for Fine-grained Urban Scene Reconstruction via Semantic-guided Density Control and Loss Design](https://arxiv.org/abs/2610.16292v1)**  
  Authors: Yueling Liao, San Jiang, Xing Zhang, Zhongwen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16292v1.pdf)  
  Keywords: 3d gaussian, ar, high-fidelity, 3d reconstruction, urban scene, semantic, segmentation, gaussian splatting, dynamic  
- **[DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video](https://arxiv.org/abs/2610.09720v1)**  
  Authors: Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09720v1.pdf)  
  Keywords: ar, outdoor, high-fidelity, geometry, 4d, efficient, dynamic  
- **[LEGO-Anything: Coding Agents for 3D Scene Reconstruction](https://arxiv.org/abs/2609.36380v1)**  
  Authors: Xirui Li, Peng Shi, Mingwen Dong, Sheng Zhang, Zhuoyan Xu, Dongkyu Lee, Shuaichen Chang, Yi Xiang, Lin Pan, Jiarong Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36380v1.pdf)  
  Keywords: ar, outdoor, geometry, face  
- **[Federated 3D Gaussian Splatting for Large-Scale Scene Reconstruction at Wireless Edge](https://arxiv.org/abs/2609.32177v1)**  
  Authors: Guanlin Wu, Chao Hu, Pu Chen, Juyong Zhang, Han Hu, Shuguang Cui, Jie Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32177v1.pdf)  
  Keywords: 3d gaussian, ar, face, lightweight, efficient, large scene, gaussian splatting  
- **[ChronoFuseGS: Multi-Temporal Gaussian Fusion with Per-Splat Persistence and Change Visualization](https://arxiv.org/abs/2609.31339v1)**  
  Authors: Tobias Batik, Diana Marin, Peter Kán, Hannes Kaufmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31339v1.pdf)  
  Keywords: ar, outdoor, gaussian splatting  
- **[OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning](https://arxiv.org/abs/2609.29985v1)**  
  Authors: Haoran Wang, Shaoyu Cai, Adrian Azzarelli, Zhuodong Jiang, Guoxi Huang, Eng Tat Khoo, Brett Seymour, Fan Zhang, David Bull, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29985v1.pdf)  
  Keywords: 3d gaussian, ar, real-time rendering, 3d reconstruction, compact, fast, efficient, large scene, nerf, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 193 papers*

- **[ClunoGS: Compact Language 3D Gaussian Splatting via Unified Optimization](https://arxiv.org/abs/2610.30013v1)**  
  Authors: Jian Xu, Yi Li, Ying Huang, Siyi Wu, Bingzhe Li, Yuede Ji, Miao Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.30013v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, compression, compact, semantic, localization, segmentation, gaussian splatting  
- **[AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2610.29374v1)**  
  Authors: Rodion Shkokov, Tatiana Zemskova, Dmitry Yudin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29374v1.pdf) | [![GitHub](https://img.shields.io/github/stars/OptimusFaber/AOV-GS?style=social)](https://github.com/OptimusFaber/AOV-GS)  
  Keywords: 3d gaussian, ar, human, geometry, lightweight, semantic, segmentation, mapping, gaussian splatting  
- **[CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding](https://arxiv.org/abs/2610.28530v1)**  
  Authors: Om Shivam Verma, Shaya Farahmand, Lingjun Zhao, Lu Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28530v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, geometry, compact, semantic, lighting  
- **[SplatFlux: Feed-Forward 4D Gaussian Reconstruction and Generation from Video Latents](https://arxiv.org/abs/2610.28257v1)**  
  Authors: Runmin Zhang, Binglin Ren, Zhu Yu, Fudong Wang, Jiangke Lin, Yichun Shentu, Si-Yuan Cao, Yi Yuan, Hui-Liang Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28257v1.pdf)  
  Keywords: ar, motion, compact, 4d, dynamic  
- **[RLSplat: Resource-Linear Budget Control for Feed-forward 3D Gaussian Splatting](https://arxiv.org/abs/2610.27712v1)**  
  Authors: Injae Kim, Minseok Joo, Jihwan Park, Sehyung Kim, Minseong Bae, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.27712v1.pdf)  
  Keywords: 3d gaussian, ar, fast, efficient, gaussian splatting  
- **[PhysSkin++: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning](https://arxiv.org/abs/2610.26067v1)**  
  Authors: Yuanhang Lei, Baofei Liu, Xingxuan Li, Tao Cheng, Zixuan Wang, Boming Zhao, Yujun Shen, Siyuan Huang, Ruizhen Hu, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26067v1.pdf)  
  Keywords: 3d gaussian, ar, animation, compact, efficient, deformation, dynamic  
- **[FineSplat: Fine Patches, Local Groups, Detailed Splats](https://arxiv.org/abs/2610.25011v1)**  
  Authors: Hyebin Kim, Hwasik Jeong, Joonhyuk Park, Gyeongjin Kang, Jungwoo Kim, Younghyun Kim, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25011v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, compact, efficient, gaussian splatting  
- **[RoMo-GS: Efficient Online 3D Gaussian Splatting for Robot Mapping via Exposure-Integrated Motion Blur](https://arxiv.org/abs/2610.24605v1)**  
  Authors: Sangwoo Jung, Di Deng, Jiahui Fu, Laura Herlant, Ayoung Kim, Yafei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24605v1.pdf)  
  Keywords: 3d gaussian, ar, motion, robotics, geometry, fast, mapping, efficient, gaussian splatting  
- **[Codec-Compatible Learned Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2610.26920v1)**  
  Authors: Feiyang Yu, Qi Yang, Wenjie Huang, Yunfeng Guan, Yiling Xu, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26920v1.pdf)  
  Keywords: 3d gaussian, ar, compression, compact, lightweight, efficient, gaussian splatting  
- **[HumanSkill-4D: Training-Free Language Querying of Animatable Gaussian Avatars in Space and Time](https://arxiv.org/abs/2610.24452v2)**  
  Authors: Junsu Kim, Naeun Kim, Dongyoon Han, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24452v2.pdf)  
  Keywords: ar, human, motion, compact, 4d, semantic, avatar, segmentation, body, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 61 papers*

- **[AutoPhyX: Automatic Text-Condition Physics Property Generation](https://arxiv.org/abs/2610.29517v1)**  
  Authors: Bei Huang, Yixin Chen, Hongbin Zha, Yuru Pei, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29517v1.pdf)  
  Keywords: ar, high-fidelity, 4d, semantic, nerf, gaussian splatting, dynamic  
- **[GOFusion: Real-Time Gaussian-Occupancy Submap Fusion for Fisher-Informed Autonomous Robot Navigation](https://arxiv.org/abs/2610.25261v1)**  
  Authors: Boxin Bu, Simon Boche, Haoming Zhang, Jaehyung Jung, Jiaxin Wei, Hannah Schieber, Daniel Roth, Angela P. Schoellig, Stefan Leutenegger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25261v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Bennnoo/GOFusion?style=social)](https://github.com/Bennnoo/GOFusion) | [![Project](https://img.shields.io/badge/-Project-blue)](https://youtu.be/pLQKbxQvb6I.) | [![Video](https://img.shields.io/badge/-Video-red)](https://youtu.be/pLQKbxQvb6I)  
  Keywords: 3d gaussian, ar, high-fidelity, slam, mapping, gaussian splatting  
- **[SwitchSplat: Learning Discrete Object States from Casually Captured Scenes](https://arxiv.org/abs/2610.24812v2)**  
  Authors: Yizheng Xie, Yalda Foroutan, George Shramko, Daniel Rebain, Shrisudhan Govindarajan, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24812v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://switchsplat.github.io)  
  Keywords: 3d gaussian, ar, high-fidelity, 3d reconstruction, geometry, 4d, fast, gaussian splatting, dynamic  
- **[TriFold: Folding irregular 3D Gaussians into structured latents for 3D Scene Generation](https://arxiv.org/abs/2610.23050v2)**  
  Authors: Yun Wang, Chiyu Wang, Fan Jiang, Ziyu Zhu, Zhaoxu Sun, Guangchi Fang, Mu Xu, Dapeng Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.23050v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fantasy-amap.github.io/TriFold)  
  Keywords: 3d gaussian, ar, high-fidelity, geometry, compact  
- **[3D Gaussian Splatting for Fine-grained Urban Scene Reconstruction via Semantic-guided Density Control and Loss Design](https://arxiv.org/abs/2610.16292v1)**  
  Authors: Yueling Liao, San Jiang, Xing Zhang, Zhongwen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16292v1.pdf)  
  Keywords: 3d gaussian, ar, high-fidelity, 3d reconstruction, urban scene, semantic, segmentation, gaussian splatting, dynamic  
- **[Demiurge: Forging Navigable 4D Worlds via Autoregressive Video Rerendering](https://arxiv.org/abs/2610.14685v1)**  
  Authors: Hanxin Zhu, Jianqi Ma, Cong Wang, Zhihao Hu, Junyao Gao, Tianyu He, Junyan Lin, Jiayin Xiao, Jiateng Shou, Sen Liang, Weidong Zhang, Zhibo Chen, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.14685v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanxinzhu-lab.github.io/demiurge_project_page)  
  Keywords: 3d gaussian, ar, high-fidelity, motion, geometry, 4d, gaussian splatting, dynamic  
- **[TETRIS-4DGS: Efficient Post-Training Compression of 4D Gaussian Splatting](https://arxiv.org/abs/2610.14663v1)**  
  Authors: Chengzhen Wu, Kelei Liu, Sicheng Li, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.14663v1.pdf)  
  Keywords: ar, motion, compression, 4d, high quality, efficient, head, gaussian splatting, dynamic  
- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: 3d gaussian, ar, high-fidelity, face, geometry, compact, sparse view, gaussian splatting, dynamic  
- **[DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video](https://arxiv.org/abs/2610.09720v1)**  
  Authors: Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09720v1.pdf)  
  Keywords: ar, outdoor, high-fidelity, geometry, 4d, efficient, dynamic  
- **[OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception](https://arxiv.org/abs/2610.07569v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07569v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/OpenSplatGraph)  
  Keywords: 3d gaussian, ar, understanding, high-fidelity, robotics, geometry, lightweight, semantic, mapping, efficient, gaussian splatting  

### Ray Tracing

- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: 3d gaussian, ar, ray tracing, gaussian splatting, efficient, head, lighting  
- **[Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)**  
  Authors: Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/vorotracing)  
  Keywords: 3d gaussian, ar, real-time rendering, ray tracing, face, motion, compact, fast, nerf, gaussian splatting  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: 3d gaussian, ar, ray tracing, compact, shadow, reflection, fast, mapping, efficient, nerf, gaussian splatting  

### Relighting

- **[CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding](https://arxiv.org/abs/2610.28530v1)**  
  Authors: Om Shivam Verma, Shaya Farahmand, Lingjun Zhao, Lu Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28530v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, geometry, compact, semantic, lighting  
- **[SplatXR: A Toolkit for Multi-Layered Extended Reality via On-Headset 3D Gaussian Splatting](https://arxiv.org/abs/2610.26338v1)**  
  Authors: Cyrus Vachha, Mohamed Kari, Parastoo Abtahi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26338v1.pdf)  
  Keywords: 3d gaussian, ar, face, geometry, shadow, head, gaussian splatting  
- **[RxGS: Relightable Gaussian Stylization via BRDF Decomposition](https://arxiv.org/abs/2610.25681v1)**  
  Authors: Wanrong Hong, Liu Jiang, Mukesh Prasad, Jun Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25681v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, nerf, face, geometry, illumination, relightable, gaussian splatting  
- **[MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345v1)**  
  Authors: Yifei Wang, Wei Tian, Wenhua Bao, Jia Zhou, Hanshi Wang, Fudong Ge, Jianhua Wu, Shuai Yuan, Zhipeng Zhang, Xingliang Liu, Xianming Zeng, Jianyun Xu, Bingzhao Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25345v1.pdf)  
  Keywords: ar, face, geometry, illumination, gaussian splatting  
- **[Directionally Factorized Illumination with Spherical Harmonic Rotation](https://arxiv.org/abs/2610.24811v1)**  
  Authors: Yimeng Dou, Adam M. Saunders, Andre T. S. Hucke, Michael E. Kim, Adam W. Anderson, Eric R. Tkaczyk, Bennett A. Landman, Daniel Moyer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24811v1.pdf)  
  Keywords: ar, gaussian splatting, face, geometry, illumination, neural rendering, nerf, medical, lighting  
- **[Video Diffusion Avatars: Taming Video Diffusion Models into Controllable 3D Avatars](https://arxiv.org/abs/2610.23772v1)**  
  Authors: Simon Giebenhain, Tobias Kirschstein, Liam Schoneveld, Davide Davoli, Zhe Chen, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.23772v1.pdf)  
  Keywords: ar, face, motion, shadow, reflection, avatar, efficient, body, dynamic  
- **[Where Should the Gaussians Go? Reusable Label-Aware Allocation for Budget-Constrained Gaussian Splatting of Cinematic CT](https://arxiv.org/abs/2610.20397v1)**  
  Authors: Bowen Xiang, Dingjie Su, Jon S. Heiselman, Michael I. Miga  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20397v1.pdf)  
  Keywords: 3d gaussian, lighting, ar, gaussian splatting  
- **[VisibilitySplat: Ray-Traced Occlusion for Relighting with 3D Gaussian Splatting](https://arxiv.org/abs/2610.19847v1)**  
  Authors: Sven Kluge, Oliver Staadt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19847v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, face, illumination, relighting, nerf, gaussian splatting, dynamic  
- **[HyperLoop: Hyperspectral-Assisted Loop Closure Detection in 3D-SLAM for Planetary Exploration](https://arxiv.org/abs/2610.19742v1)**  
  Authors: Annie Bhalla, Dennis Rotondi, Riccardo Giubilato, Kai O. Arras, Wolfgang Stuerzl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19742v1.pdf)  
  Keywords: 3d gaussian, ar, outdoor, slam, mapping, illumination, gaussian splatting  
- **[YUBI-Real2Sim: 3DGS Scene Verification for Reliable Policy Evaluation](https://arxiv.org/abs/2610.17521v1)**  
  Authors: Hiroki Nishizawa, Takehiko Ohkawa, Nicola Scianca, Tatsuya Matsushima, Shigeo Morishima, Kei Ota  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17521v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yubi-real2sim.airoa.io)  
  Keywords: 3d gaussian, lighting, ar, gaussian splatting  

### SLAM

*Showing the latest 50 out of 76 papers*

- **[ClunoGS: Compact Language 3D Gaussian Splatting via Unified Optimization](https://arxiv.org/abs/2610.30013v1)**  
  Authors: Jian Xu, Yi Li, Ying Huang, Siyi Wu, Bingzhe Li, Yuede Ji, Miao Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.30013v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, compression, compact, semantic, localization, segmentation, gaussian splatting  
- **[AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2610.29374v1)**  
  Authors: Rodion Shkokov, Tatiana Zemskova, Dmitry Yudin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29374v1.pdf) | [![GitHub](https://img.shields.io/github/stars/OptimusFaber/AOV-GS?style=social)](https://github.com/OptimusFaber/AOV-GS)  
  Keywords: 3d gaussian, ar, human, geometry, lightweight, semantic, segmentation, mapping, gaussian splatting  
- **[GOFusion: Real-Time Gaussian-Occupancy Submap Fusion for Fisher-Informed Autonomous Robot Navigation](https://arxiv.org/abs/2610.25261v1)**  
  Authors: Boxin Bu, Simon Boche, Haoming Zhang, Jaehyung Jung, Jiaxin Wei, Hannah Schieber, Daniel Roth, Angela P. Schoellig, Stefan Leutenegger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25261v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Bennnoo/GOFusion?style=social)](https://github.com/Bennnoo/GOFusion) | [![Project](https://img.shields.io/badge/-Project-blue)](https://youtu.be/pLQKbxQvb6I.) | [![Video](https://img.shields.io/badge/-Video-red)](https://youtu.be/pLQKbxQvb6I)  
  Keywords: 3d gaussian, ar, high-fidelity, slam, mapping, gaussian splatting  
- **[Localization and Neural Splatting on the Edge: An FPGA Scene Memory for Robots](https://arxiv.org/abs/2610.25068v1)**  
  Authors: Que Haohua, Mingkai Liu, Handong Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25068v1.pdf)  
  Keywords: 3d gaussian, ar, fast, acceleration, localization, gaussian splatting  
- **[RoMo-GS: Efficient Online 3D Gaussian Splatting for Robot Mapping via Exposure-Integrated Motion Blur](https://arxiv.org/abs/2610.24605v1)**  
  Authors: Sangwoo Jung, Di Deng, Jiahui Fu, Laura Herlant, Ayoung Kim, Yafei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24605v1.pdf)  
  Keywords: 3d gaussian, ar, motion, robotics, geometry, fast, mapping, efficient, gaussian splatting  
- **[KFS$^4$LAM: Adaptive KeyFrame Selection with Structure-Aware Mapping for Endoscopic Gaussian Splatting SLAM](https://arxiv.org/abs/2610.22505v1)**  
  Authors: Xinwei Ju, Zhehua Mao, Tianyi Song, Danail Stoyanov, Sophia Bano, Francisco Vasconcelos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22505v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xinweiju.github.io/KFSLAM)  
  Keywords: ar, gaussian splatting, motion, slam, localization, mapping, deformation, dynamic  
- **[CF-Splat: Closed-Form Triangle Splatting with Mesh Priors](https://arxiv.org/abs/2610.22108v1)**  
  Authors: Yixin Fang, Liang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22108v1.pdf)  
  Keywords: mapping, ar, geometry, efficient  
- **[Compression of Uniformly Distributed Unit Quaternions](https://arxiv.org/abs/2610.22052v1)**  
  Authors: Carsten Faber, Bastian Kuth, Rinaldo Schuster, Daniel Pauls, Quirin Meyer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22052v1.pdf)  
  Keywords: ar, animation, compression, mapping, efficient, gaussian splatting  
- **[Training-Free Target-Aware Refinement of 3D Gaussian Language Map](https://arxiv.org/abs/2610.21619v1)**  
  Authors: Sibaek Lee, Kyeongsu Kang, Seongbo Ha, Yewon Jeon, Joonyeol Choi, Daegeol Ko, Jaehyuk Hur, Taemin Choi, Minsu Kim, Hyungjoo Ahn, Wonsok Yoo, Hyeonwoo Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.21619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lab-of-ai-and-robotics.github.io/target-aware-langmap)  
  Keywords: 3d gaussian, ar, robotics, localization, segmentation, efficient, gaussian splatting  
- **[HyperLoop: Hyperspectral-Assisted Loop Closure Detection in 3D-SLAM for Planetary Exploration](https://arxiv.org/abs/2610.19742v1)**  
  Authors: Annie Bhalla, Dennis Rotondi, Riccardo Giubilato, Kai O. Arras, Wolfgang Stuerzl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19742v1.pdf)  
  Keywords: 3d gaussian, ar, outdoor, slam, mapping, illumination, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 100 papers*

- **[ClunoGS: Compact Language 3D Gaussian Splatting via Unified Optimization](https://arxiv.org/abs/2610.30013v1)**  
  Authors: Jian Xu, Yi Li, Ying Huang, Siyi Wu, Bingzhe Li, Yuede Ji, Miao Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.30013v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, compression, compact, semantic, localization, segmentation, gaussian splatting  
- **[AutoPhyX: Automatic Text-Condition Physics Property Generation](https://arxiv.org/abs/2610.29517v1)**  
  Authors: Bei Huang, Yixin Chen, Hongbin Zha, Yuru Pei, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29517v1.pdf)  
  Keywords: ar, high-fidelity, 4d, semantic, nerf, gaussian splatting, dynamic  
- **[AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2610.29374v1)**  
  Authors: Rodion Shkokov, Tatiana Zemskova, Dmitry Yudin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29374v1.pdf) | [![GitHub](https://img.shields.io/github/stars/OptimusFaber/AOV-GS?style=social)](https://github.com/OptimusFaber/AOV-GS)  
  Keywords: 3d gaussian, ar, human, geometry, lightweight, semantic, segmentation, mapping, gaussian splatting  
- **[Real2Sem2Real: 3D Semantic Augmentations for Robot Learning from a Single Human RGB Demonstration](https://arxiv.org/abs/2610.28880v1)**  
  Authors: Matthew Strong, Ankush K. Dhawan, Julien Poffet, Giuse Pham, Jinho So, Monroe Kennedy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28880v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2sem2real.github.io)  
  Keywords: ar, human, semantic  
- **[SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images](https://arxiv.org/abs/2610.28585v1)**  
  Authors: Rundong Luo, Yunong Liu, Di Cao, Matthew Tancik, Shyamal Buch, Colton Stearns, Wenqi Xian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28585v1.pdf)  
  Keywords: ar, robotics, segmentation  
- **[CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding](https://arxiv.org/abs/2610.28530v1)**  
  Authors: Om Shivam Verma, Shaya Farahmand, Lingjun Zhao, Lu Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28530v1.pdf)  
  Keywords: 3d gaussian, ar, understanding, geometry, compact, semantic, lighting  
- **[OV-Foam: How 3D Representations Shape Semantic Feature Lifting](https://arxiv.org/abs/2610.28131v1)**  
  Authors: Yousef Rajeh, Alejandra Esparza Pelcastre, Ivan Viola, Dominik Engel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28131v1.pdf)  
  Keywords: 3d gaussian, ar, semantic, segmentation, gaussian splatting  
- **[PanoGraphGS: Unifying Panoptic Segmentation and Hierarchical 3D Scene Graphs with Gaussian Splatting](https://arxiv.org/abs/2610.27696v1)**  
  Authors: Jinghan Gao, Siyu Wang, Dongyu Feng, Yiyuan Pan, Rong Xiong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.27696v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gaojh0333/PanoGraphGS?style=social)](https://github.com/gaojh0333/PanoGraphGS)  
  Keywords: 3d gaussian, ar, understanding, geometry, semantic, segmentation, gaussian splatting  
- **[Arbitrary-Scale Anisotropic 3D MRI Super-Resolution with Gaussian Prototypes](https://arxiv.org/abs/2610.24858v2)**  
  Authors: Aditya Rastogi, Ramon Leiser, Prateek Singh, Martha Foltyn-Dumitru, Martin Bendszus, Fabian Bamberg, Klaus Maier-Hein, Kai Schlamp, Alexander Radbruch, Gianluca Brugnara, Philipp Vollmuth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24858v2.pdf)  
  Keywords: 3d gaussian, ar, motion, geometry, segmentation, head  
- **[HumanSkill-4D: Training-Free Language Querying of Animatable Gaussian Avatars in Space and Time](https://arxiv.org/abs/2610.24452v2)**  
  Authors: Junsu Kim, Naeun Kim, Dongyoon Han, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24452v2.pdf)  
  Keywords: ar, human, motion, compact, 4d, semantic, avatar, segmentation, body, gaussian splatting  



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
