# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-gaussians/)**: an interactive paper map, monthly trends, topic network and co-author network of every tracked paper.

> Last Update: 2026-10-12 03:13:29

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
- [Acceleration](#acceleration) (80 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (500 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (171 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (192 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (40 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (208 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (24 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (203 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (71 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (5 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (42 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (75 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (97 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: survey, geometry, 3d gaussian, gaussian splatting, ar  
- **[OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones](https://arxiv.org/abs/2609.24253v1)**  
  Authors: Zhongrui You, Zhen Li, Junli Liu, Zhigang Wang, Bin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24253v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://openflyscan.github.io)  
  Keywords: high-fidelity, survey, 3d gaussian, gaussian splatting, face, ar  
- **[Quality Assessment of 3D Gaussian Splatting: Distortions, Benchmarks, and Open Challenges](https://arxiv.org/abs/2609.23027v1)**  
  Authors: Shuai Liu, Binqiang Liu, Qingyu Mao, Jiacong Chen, Yongsheng Liang, Youneng Bao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23027v1.pdf)  
  Keywords: survey, 3d gaussian, compression, gaussian splatting, ar  
- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: motion, survey, geometry, illumination, gaussian splatting, 3d reconstruction, ar  
- **[UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys](https://arxiv.org/abs/2608.06404v1)**  
  Authors: Junxiong Zhou, Xuechen Li, Chonghao Qiu, Lang Qiao, Xiaowei Jia, Qi Yang, Chishan Zhang, Leikun Yin, Nanshan You, Vipin Kumar, David Mulla, Ce Yang, Zhenong Jin, Licheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06404v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://link-dev.github.io/UAV3DCrop)  
  Keywords: survey, geometry, 3d gaussian, dynamic, gaussian splatting, ar, 3d reconstruction, nerf  

### Acceleration

*Showing the latest 50 out of 80 papers*

- **[Make It Flow: Animating Water in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2610.13860v1)**  
  Authors: Kjell Keune, Florian Hahlbohm, Jannis Möller, Susana Castillo, Martin Eisemann, Marcus Magnor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13860v1.pdf)  
  Keywords: motion, real-time rendering, animation, 3d gaussian, dynamic, gaussian splatting, human, ar  
- **[NovaSplat: Model-Free 6D Object Pose Estimation via 3D Gaussian Splatting Onboarding and Refinement](https://arxiv.org/abs/2610.13309v1)**  
  Authors: Georgios Floros, Evangelos Sartinas, Orestis Vangelis, Maria Pateraki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13309v1.pdf) | [![GitHub](https://img.shields.io/github/stars/POSE-Lab/novasplat?style=social)](https://github.com/POSE-Lab/novasplat)  
  Keywords: fast, 3d gaussian, gaussian splatting, face, ar  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: real-time rendering, geometry, illumination, 3d gaussian, dynamic, gaussian splatting, lightweight, face, ar  
- **[Efficient 3D Gaussian Head Avatars for Edge Devices](https://arxiv.org/abs/2610.09821v1)**  
  Authors: Umar Farooq, Jean-Yves Guillemaut, Adrian Hilton, Marco Volino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09821v1.pdf)  
  Keywords: 3d gaussian, efficient rendering, compression, efficient, head, ar, avatar  
- **[LoCoSplat: Real-Time Feed-Forward 3D Gaussian Splatting with Minimal 3D Reasoning](https://arxiv.org/abs/2610.04351v1)**  
  Authors: Sinan Wang, Jinjin He, Yuchen Sun, Duowen Chen, Shenyifan Lu, Bo Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04351v1.pdf)  
  Keywords: fast, 3d gaussian, dynamic, gaussian splatting, ar  
- **[Budgeted-GS: Real-Time Large-Scale Gaussian Splatting via Factoring LOD](https://arxiv.org/abs/2610.03162v1)**  
  Authors: Haipeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03162v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, gaussian splatting, high quality, ar  
- **[FactorSplat: Appearance-Controllable Gaussian Proxies for Medical Volume Rendering](https://arxiv.org/abs/2610.02382v1)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/FactorSplat)  
  Keywords: fast, geometry, medical, gaussian splatting, ar  
- **[One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time Avatars](https://arxiv.org/abs/2610.02207v1)**  
  Authors: Ramazan Fazylov, Stamatis Lefkimmiatis, Ivan Laptev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02207v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ramazan793.github.io/gala)  
  Keywords: fast, animation, 3d gaussian, efficient, dynamic, ar, avatar  
- **[Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation](https://arxiv.org/abs/2610.01114v1)**  
  Authors: Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01114v1.pdf)  
  Keywords: fast, motion, efficient, gaussian splatting, ar, deformation  
- **[Dirichlet Splatting: Differentiable Rendering for Wave-Based Inverse Problems](https://arxiv.org/abs/2610.00618v1)**  
  Authors: Xingyu Chen, Wuqiong Zhao, Xinyu Zhang, Tzu-Mao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00618v1.pdf)  
  Keywords: fast, ar, gaussian splatting, 3d gaussian  

### Applications

*Showing the latest 50 out of 500 papers*

- **[Splat2Act: From Captured Scenes to Personalized VLA Manipulation](https://arxiv.org/abs/2610.13945v1)**  
  Authors: Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, Gunjan Chhablani, Muhammad Zubair Irshad, Zsolt Kira  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13945v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, human, tracking, ar  
- **[Make It Flow: Animating Water in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2610.13860v1)**  
  Authors: Kjell Keune, Florian Hahlbohm, Jannis Möller, Susana Castillo, Martin Eisemann, Marcus Magnor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13860v1.pdf)  
  Keywords: motion, real-time rendering, animation, 3d gaussian, dynamic, gaussian splatting, human, ar  
- **[SimVTA: Simulation-Grounded Video-Trajectory Alignment for Driving World Action Models](https://arxiv.org/abs/2610.13781v1)**  
  Authors: Changhui Jing, Haochen Tian, Hongchen Li, Tianyu Li, Caojun Wang, Zihao Zhang, Yanhao Liu, Chengen Xie, Bailin Li, Hao Zhao, Zhenjie Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13781v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian  
- **[Gaussian Splatting with Reflections Guided by What is Seen](https://arxiv.org/abs/2610.13757v1)**  
  Authors: Yiming Liang, Tianyu Xiao, Hiroshi Ishikawa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13757v1.pdf)  
  Keywords: reflection, 3d gaussian, gaussian splatting, nerf, ar  
- **[AutoBio+: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories](https://arxiv.org/abs/2610.13643v1)**  
  Authors: Xuanye Wu, Yue Shi, Yongcan Yang, Yiqun Wang, Zhaoqi Wan, Dayu Xia, Jiezhang Cao, Xiangfei Li, Yao Mu, Guangtao Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13643v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://autobio-plus.github.io/AutoBioPlus)  
  Keywords: efficient, dynamic, ar  
- **[Efficient Confidence-Aware Densification for 3DGS](https://arxiv.org/abs/2610.13541v1)**  
  Authors: Manuel Hofer, Thomas Köhler, Felix Windisch, Bernhard Kerbl, Markus Steinberger, Lukas Radl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13541v1.pdf)  
  Keywords: 3d gaussian, 4d, efficient, gaussian splatting, ar  
- **[SplatQ: Interaction-Aware Pruning of 3D Gaussian Splatting via Quadratic Selection](https://arxiv.org/abs/2610.13503v1)**  
  Authors: Hongbin Ye, Haixu Liu, Shenwei Kang, Wenxiu Wei, Tinglan Wang, Hongdong Zhu, Fan Tang, Qi Gao, Yin Ma, Kai Wen, Hai Wei, Nuo Qian, Wei-Shi Zheng, Shaobo Chen, Fa-Ting Hong, Jingke Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13503v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian  
- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: ray tracing, 3d gaussian, efficient, gaussian splatting, head, ar, lighting  
- **[ManeuverFlow: Maneuver Hypothesis Generation with Future Evidence for Trajectory Evaluation and Refinement in End-to-End Autonomous Driving](https://arxiv.org/abs/2610.13409v1)**  
  Authors: Yuhao Wei, Yong Chen, Chen Yang, Yingchen Wang, Delin Ouyang, Lingfeng Qi, Qi Lan, Zhanhua Zhang, Jie Li, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13409v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wyh-autonomy/maneuverflow?style=social)](https://github.com/wyh-autonomy/maneuverflow)  
  Keywords: autonomous driving, lightweight, ar  
- **[NovaSplat: Model-Free 6D Object Pose Estimation via 3D Gaussian Splatting Onboarding and Refinement](https://arxiv.org/abs/2610.13309v1)**  
  Authors: Georgios Floros, Evangelos Sartinas, Orestis Vangelis, Maria Pateraki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13309v1.pdf) | [![GitHub](https://img.shields.io/github/stars/POSE-Lab/novasplat?style=social)](https://github.com/POSE-Lab/novasplat)  
  Keywords: fast, 3d gaussian, gaussian splatting, face, ar  

### Avatar Generation

*Showing the latest 50 out of 171 papers*

- **[Splat2Act: From Captured Scenes to Personalized VLA Manipulation](https://arxiv.org/abs/2610.13945v1)**  
  Authors: Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, Gunjan Chhablani, Muhammad Zubair Irshad, Zsolt Kira  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13945v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, human, tracking, ar  
- **[Make It Flow: Animating Water in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2610.13860v1)**  
  Authors: Kjell Keune, Florian Hahlbohm, Jannis Möller, Susana Castillo, Martin Eisemann, Marcus Magnor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13860v1.pdf)  
  Keywords: motion, real-time rendering, animation, 3d gaussian, dynamic, gaussian splatting, human, ar  
- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: ray tracing, 3d gaussian, efficient, gaussian splatting, head, ar, lighting  
- **[NovaSplat: Model-Free 6D Object Pose Estimation via 3D Gaussian Splatting Onboarding and Refinement](https://arxiv.org/abs/2610.13309v1)**  
  Authors: Georgios Floros, Evangelos Sartinas, Orestis Vangelis, Maria Pateraki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13309v1.pdf) | [![GitHub](https://img.shields.io/github/stars/POSE-Lab/novasplat?style=social)](https://github.com/POSE-Lab/novasplat)  
  Keywords: fast, 3d gaussian, gaussian splatting, face, ar  
- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: high-fidelity, geometry, 3d gaussian, compact, sparse view, dynamic, gaussian splatting, face, ar  
- **[Measurable Semantic 3D Gaussian Splatting with Joint Region and Depth Supervision for Interactive Building Inspection](https://arxiv.org/abs/2610.13143v1)**  
  Authors: Yi Zhang, Tian Tan, Ray Kai Leung Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13143v1.pdf)  
  Keywords: geometry, 3d gaussian, semantic, gaussian splatting, face, 3d reconstruction, ar  
- **[Volume Rendering with Metric--Phase Fields for Thin Structures and Sign-Ambiguous Geometry](https://arxiv.org/abs/2610.13088v1)**  
  Authors: Junkai Deng, Jiayi Kong, Xuhui Chen, Guanli Hou, Fei Hou, Junhui Hou, Wenping Wang, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13088v1.pdf)  
  Keywords: face, geometry, ar  
- **[2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map](https://arxiv.org/abs/2610.11752v1)**  
  Authors: Jiwon Park, Dong-Uk Seo, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11752v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://2dgs-planner.github.io)  
  Keywords: geometry, efficient, gaussian splatting, face, ar  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: real-time rendering, geometry, illumination, 3d gaussian, dynamic, gaussian splatting, lightweight, face, ar  
- **[Rendering-Free Lookahead for Question-Guided Active Vision](https://arxiv.org/abs/2610.11039v1)**  
  Authors: Koya Sakamoto, Daichi Azuma, Shuhei Kurita, Naoya Chiba, Yusuke Iwasawa, Yutaka Matsuo, Taiki Miyanishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11039v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, head, ar  

### Dynamic Scene

*Showing the latest 50 out of 192 papers*

- **[Make It Flow: Animating Water in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2610.13860v1)**  
  Authors: Kjell Keune, Florian Hahlbohm, Jannis Möller, Susana Castillo, Martin Eisemann, Marcus Magnor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13860v1.pdf)  
  Keywords: motion, real-time rendering, animation, 3d gaussian, dynamic, gaussian splatting, human, ar  
- **[AutoBio+: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories](https://arxiv.org/abs/2610.13643v1)**  
  Authors: Xuanye Wu, Yue Shi, Yongcan Yang, Yiqun Wang, Zhaoqi Wan, Dayu Xia, Jiezhang Cao, Xiangfei Li, Yao Mu, Guangtao Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13643v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://autobio-plus.github.io/AutoBioPlus)  
  Keywords: efficient, dynamic, ar  
- **[Efficient Confidence-Aware Densification for 3DGS](https://arxiv.org/abs/2610.13541v1)**  
  Authors: Manuel Hofer, Thomas Köhler, Felix Windisch, Bernhard Kerbl, Markus Steinberger, Lukas Radl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13541v1.pdf)  
  Keywords: 3d gaussian, 4d, efficient, gaussian splatting, ar  
- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: high-fidelity, geometry, 3d gaussian, compact, sparse view, dynamic, gaussian splatting, face, ar  
- **[OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs](https://arxiv.org/abs/2610.12461v1)**  
  Authors: You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12461v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ouroworld.userwei.com)  
  Keywords: motion, illumination, 3d gaussian, 4d, dynamic, gaussian splatting, ar, deformation  
- **[LVS: Local View Synthesis from Relative Camera Pose by Reusing Previous Views](https://arxiv.org/abs/2610.12127v1)**  
  Authors: Qizhou Huo, Xuan Sun, Yongfei Guo, Zhipeng Wang, Yuanhao Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12127v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, lightweight, ar  
- **[CoCam4D: Geometry-Aware Cooperative 4D Perception for Camera-Only Autonomous Driving](https://arxiv.org/abs/2610.11577v1)**  
  Authors: Soham Pahari, Sudip Das, Arindam Das, Ujjwal Bhattacharya  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11577v1.pdf)  
  Keywords: geometry, compact, 3d gaussian, 4d, dynamic, efficient, autonomous driving, ar  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: real-time rendering, geometry, illumination, 3d gaussian, dynamic, gaussian splatting, lightweight, face, ar  
- **[MATE4D: Matrix-Guided Editable 4D Generation from a Single Image](https://arxiv.org/abs/2610.11181v1)**  
  Authors: Xiaotian Chen, Dongfu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11181v1.pdf)  
  Keywords: motion, geometry, 3d gaussian, 4d, dynamic, vr, lightweight, ar, deformation  
- **[Rendering-Free Lookahead for Question-Guided Active Vision](https://arxiv.org/abs/2610.11039v1)**  
  Authors: Koya Sakamoto, Daichi Azuma, Shuhei Kurita, Naoya Chiba, Yusuke Iwasawa, Yutaka Matsuo, Taiki Miyanishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11039v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, head, ar  

### Few-shot

- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: high-fidelity, geometry, 3d gaussian, compact, sparse view, dynamic, gaussian splatting, face, ar  
- **[OX-NeRF: 3D X-ray Tomography Reconstruction from Sparse Views Using Implicit Neural Representation](https://arxiv.org/abs/2610.11547v1)**  
  Authors: Thomas Welsch, Min-Hsin Tu, David J. Chapman, Daniel E. Eakins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11547v1.pdf)  
  Keywords: sparse view, gaussian splatting, 3d reconstruction, nerf, ar  
- **[DensiTok: Making Feed-Forward 3D Gaussian Splatting See More Views Than It Is Given](https://arxiv.org/abs/2610.07958v1)**  
  Authors: Minhyeok Lee, Jungho Lee, Minseok Kang, Heeseung Choi, Ig-Jae Kim, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07958v1.pdf)  
  Keywords: geometry, compact, 3d gaussian, sparse-view, gaussian splatting, head, ar  
- **[Sparse-View 4D Gaussian Splatting via Spatiotemporal Priors and Generative Assistance](https://arxiv.org/abs/2610.04606v2)**  
  Authors: Shengqi Wang, Zhengxian Yang, Kaiwen Tian, Yang Liu, Bowen Liu, Hua Du, Taicheng Huang, Jiamin Wu, Tao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04606v2.pdf)  
  Keywords: motion, geometry, sparse view, 4d, dynamic, sparse-view, gaussian splatting, ar  
- **[Sparse-GS2Mesh: 3D Gaussian Splatting Guided by Novel Stereo Views and 2DGS for Sparse View Surface Reconstruction](https://arxiv.org/abs/2610.04203v2)**  
  Authors: Younghyun Noh, Minje Kim, Tae-Kyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04203v2.pdf)  
  Keywords: geometry, 3d gaussian, sparse view, sparse-view, efficient, gaussian splatting, face, ar  
- **[UGOD: Uncertainty-Guided Opacity and Dropout for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.39089v1)**  
  Authors: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Chenghao Qian, Ziyang Wang, Xinqi Fan, Liangxiu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39089v1.pdf)  
  Keywords: compact, 3d gaussian, sparse-view, gaussian splatting, lightweight, head, ar, nerf  
- **[Remote Sensing Sparse-View 3D Gaussian Splatting via Depth Image-Based Rendering](https://arxiv.org/abs/2609.35612v1)**  
  Authors: Jiaming Kang, Zhengxia Zou, Zhenwei Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35612v1.pdf) | [![GitHub](https://img.shields.io/github/stars/kanehub/DIBR-GS?style=social)](https://github.com/kanehub/DIBR-GS)  
  Keywords: 3d gaussian, sparse-view, gaussian splatting, face, ar, nerf  
- **[GAPS: Generative Active Pseudo-view Selection for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.23436v2)**  
  Authors: Hongfei Zhu, Haochen Deng, Sitao Zhang, Ling Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23436v2.pdf)  
  Keywords: real-time rendering, geometry, 3d gaussian, sparse-view, gaussian splatting, ar, nerf  
- **[D3GS: Depth, DINO, and RGB Diffusion Co-Guided 3D Gaussian Splatting for Sparse-View Reconstruction](https://arxiv.org/abs/2609.22941v1)**  
  Authors: Yunqi Gao, Zhanfeng Liao, Hanzhang Tu, Zhaoqi Su, Guoqing Zheng, Songtao Wang, Hongwen Zhang, Zhou Xue, Leyuan Liu, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.22941v1.pdf)  
  Keywords: geometry, 3d gaussian, sparse-view, gaussian splatting, ar, nerf  
- **[LINGO: Latent Initialization and Gradient Optimization for Sparse-view X-ray Novel View Synthesis and CT Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2609.22849v1)**  
  Authors: Lifeng Xing, Dequan Jin, Kunpeng Bu, Peigeng He, Shihui Ying  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.22849v1.pdf)  
  Keywords: 3d gaussian, sparse-view, dynamic, gaussian splatting, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 208 papers*

- **[Splat2Act: From Captured Scenes to Personalized VLA Manipulation](https://arxiv.org/abs/2610.13945v1)**  
  Authors: Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, Gunjan Chhablani, Muhammad Zubair Irshad, Zsolt Kira  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13945v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, human, tracking, ar  
- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: high-fidelity, geometry, 3d gaussian, compact, sparse view, dynamic, gaussian splatting, face, ar  
- **[Measurable Semantic 3D Gaussian Splatting with Joint Region and Depth Supervision for Interactive Building Inspection](https://arxiv.org/abs/2610.13143v1)**  
  Authors: Yi Zhang, Tian Tan, Ray Kai Leung Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13143v1.pdf)  
  Keywords: geometry, 3d gaussian, semantic, gaussian splatting, face, 3d reconstruction, ar  
- **[Volume Rendering with Metric--Phase Fields for Thin Structures and Sign-Ambiguous Geometry](https://arxiv.org/abs/2610.13088v1)**  
  Authors: Junkai Deng, Jiayi Kong, Xuhui Chen, Guanli Hou, Fei Hou, Junhui Hou, Wenping Wang, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13088v1.pdf)  
  Keywords: face, geometry, ar  
- **[2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map](https://arxiv.org/abs/2610.11752v1)**  
  Authors: Jiwon Park, Dong-Uk Seo, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11752v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://2dgs-planner.github.io)  
  Keywords: geometry, efficient, gaussian splatting, face, ar  
- **[CoCam4D: Geometry-Aware Cooperative 4D Perception for Camera-Only Autonomous Driving](https://arxiv.org/abs/2610.11577v1)**  
  Authors: Soham Pahari, Sudip Das, Arindam Das, Ujjwal Bhattacharya  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11577v1.pdf)  
  Keywords: geometry, compact, 3d gaussian, 4d, dynamic, efficient, autonomous driving, ar  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: real-time rendering, geometry, illumination, 3d gaussian, dynamic, gaussian splatting, lightweight, face, ar  
- **[OX-NeRF: 3D X-ray Tomography Reconstruction from Sparse Views Using Implicit Neural Representation](https://arxiv.org/abs/2610.11547v1)**  
  Authors: Thomas Welsch, Min-Hsin Tu, David J. Chapman, Daniel E. Eakins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11547v1.pdf)  
  Keywords: sparse view, gaussian splatting, 3d reconstruction, nerf, ar  
- **[FlyMark: Training-Free Invisible Watermarking of 3D Gaussian Splatting via a Fruit Fly Connectome](https://arxiv.org/abs/2610.11364v1)**  
  Authors: Ziyuan Luo, Haoliang Li, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11364v1.pdf)  
  Keywords: ar, geometry, gaussian splatting, 3d gaussian  
- **[3DTexMOR: 3D Gaussian Multi-Object Removal via Texture-Space Inpainting](https://arxiv.org/abs/2610.11198v1)**  
  Authors: Kunxin Guang, Yonghao Zhao, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11198v1.pdf)  
  Keywords: reflection, geometry, 3d gaussian, nerf, ar  

### Large Scene

- **[DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video](https://arxiv.org/abs/2610.09720v1)**  
  Authors: Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09720v1.pdf)  
  Keywords: high-fidelity, geometry, 4d, dynamic, efficient, outdoor, ar  
- **[LEGO-Anything: Coding Agents for 3D Scene Reconstruction](https://arxiv.org/abs/2609.36380v1)**  
  Authors: Xirui Li, Peng Shi, Mingwen Dong, Sheng Zhang, Zhuoyan Xu, Dongkyu Lee, Shuaichen Chang, Yi Xiang, Lin Pan, Jiarong Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36380v1.pdf)  
  Keywords: face, geometry, ar, outdoor  
- **[Federated 3D Gaussian Splatting for Large-Scale Scene Reconstruction at Wireless Edge](https://arxiv.org/abs/2609.32177v1)**  
  Authors: Guanlin Wu, Chao Hu, Pu Chen, Juyong Zhang, Han Hu, Shuguang Cui, Jie Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32177v1.pdf)  
  Keywords: 3d gaussian, efficient, large scene, gaussian splatting, lightweight, face, ar  
- **[ChronoFuseGS: Multi-Temporal Gaussian Fusion with Per-Splat Persistence and Change Visualization](https://arxiv.org/abs/2609.31339v1)**  
  Authors: Tobias Batik, Diana Marin, Peter Kán, Hannes Kaufmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31339v1.pdf)  
  Keywords: ar, gaussian splatting, outdoor  
- **[OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning](https://arxiv.org/abs/2609.29985v1)**  
  Authors: Haoran Wang, Shaoyu Cai, Adrian Azzarelli, Zhuodong Jiang, Guoxi Huang, Eng Tat Khoo, Brett Seymour, Fan Zhang, David Bull, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29985v1.pdf)  
  Keywords: fast, real-time rendering, 3d gaussian, compact, efficient, large scene, gaussian splatting, ar, 3d reconstruction, nerf  
- **[Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models](https://arxiv.org/abs/2609.26007v1)**  
  Authors: Yuhang Zhang, Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Weiying Wang, Steven Yang, Qingsong Yan, Chao Yan, Mir Feroskhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26007v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, outdoor, ar  
- **[Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking](https://arxiv.org/abs/2609.25746v1)**  
  Authors: Edward Beng Wai Tan, Siew-Kei Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25746v1.pdf)  
  Keywords: geometry, slam, 3d gaussian, gaussian splatting, face, tracking, outdoor, ar  
- **[Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene Reconstruction](https://arxiv.org/abs/2609.23796v2)**  
  Authors: Yang-Tian Sun, Tianjia Liu, Zehuan Huang, Yi-Hua Huang, Xiaoyang Lyu, Ziyi Yang, Zi-Xin Zou, Yuan-Chen Guo, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23796v2.pdf)  
  Keywords: high-fidelity, geometry, face, outdoor, ar  
- **[Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization](https://arxiv.org/abs/2609.21347v1)**  
  Authors: Xiangfei Guo, Hao Shi, Yufan Zhang, Zhonghua Yi, Yongqi Mao, Xiaoting Yin, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21347v1.pdf) | [![GitHub](https://img.shields.io/github/stars/guoxf304/CubeSplat?style=social)](https://github.com/guoxf304/CubeSplat)  
  Keywords: high-fidelity, slam, 3d gaussian, gaussian splatting, face, tracking, outdoor, mapping, ar  
- **[4DGS-Fixer: Generative Sparse-View 4D Gaussian Splatting with Iterative Refinement Guided by Video Diffusion Priors](https://arxiv.org/abs/2609.21176v3)**  
  Authors: Haitao Huang, Shenghao Zhao, Boyuan Tian, Shin-Fang Chng, Songlin Yang, Sheila Lim, Huangying Zhan, Yi Xu, Anyi Rao, Frank Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21176v3.pdf)  
  Keywords: sparse-view, 4d, dynamic, large scene, gaussian splatting, ar  

### Model Compression

*Showing the latest 50 out of 203 papers*

- **[AutoBio+: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories](https://arxiv.org/abs/2610.13643v1)**  
  Authors: Xuanye Wu, Yue Shi, Yongcan Yang, Yiqun Wang, Zhaoqi Wan, Dayu Xia, Jiezhang Cao, Xiangfei Li, Yao Mu, Guangtao Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13643v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://autobio-plus.github.io/AutoBioPlus)  
  Keywords: efficient, dynamic, ar  
- **[Efficient Confidence-Aware Densification for 3DGS](https://arxiv.org/abs/2610.13541v1)**  
  Authors: Manuel Hofer, Thomas Köhler, Felix Windisch, Bernhard Kerbl, Markus Steinberger, Lukas Radl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13541v1.pdf)  
  Keywords: 3d gaussian, 4d, efficient, gaussian splatting, ar  
- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: ray tracing, 3d gaussian, efficient, gaussian splatting, head, ar, lighting  
- **[ManeuverFlow: Maneuver Hypothesis Generation with Future Evidence for Trajectory Evaluation and Refinement in End-to-End Autonomous Driving](https://arxiv.org/abs/2610.13409v1)**  
  Authors: Yuhao Wei, Yong Chen, Chen Yang, Yingchen Wang, Delin Ouyang, Lingfeng Qi, Qi Lan, Zhanhua Zhang, Jie Li, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13409v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wyh-autonomy/maneuverflow?style=social)](https://github.com/wyh-autonomy/maneuverflow)  
  Keywords: autonomous driving, lightweight, ar  
- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: high-fidelity, geometry, 3d gaussian, compact, sparse view, dynamic, gaussian splatting, face, ar  
- **[LVS: Local View Synthesis from Relative Camera Pose by Reusing Previous Views](https://arxiv.org/abs/2610.12127v1)**  
  Authors: Qizhou Huo, Xuan Sun, Yongfei Guo, Zhipeng Wang, Yuanhao Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12127v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, lightweight, ar  
- **[2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map](https://arxiv.org/abs/2610.11752v1)**  
  Authors: Jiwon Park, Dong-Uk Seo, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11752v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://2dgs-planner.github.io)  
  Keywords: geometry, efficient, gaussian splatting, face, ar  
- **[CoCam4D: Geometry-Aware Cooperative 4D Perception for Camera-Only Autonomous Driving](https://arxiv.org/abs/2610.11577v1)**  
  Authors: Soham Pahari, Sudip Das, Arindam Das, Ujjwal Bhattacharya  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11577v1.pdf)  
  Keywords: geometry, compact, 3d gaussian, 4d, dynamic, efficient, autonomous driving, ar  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: real-time rendering, geometry, illumination, 3d gaussian, dynamic, gaussian splatting, lightweight, face, ar  
- **[MATE4D: Matrix-Guided Editable 4D Generation from a Single Image](https://arxiv.org/abs/2610.11181v1)**  
  Authors: Xiaotian Chen, Dongfu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11181v1.pdf)  
  Keywords: motion, geometry, 3d gaussian, 4d, dynamic, vr, lightweight, ar, deformation  

### Quality Enhancement

*Showing the latest 50 out of 71 papers*

- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: high-fidelity, geometry, 3d gaussian, compact, sparse view, dynamic, gaussian splatting, face, ar  
- **[DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video](https://arxiv.org/abs/2610.09720v1)**  
  Authors: Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09720v1.pdf)  
  Keywords: high-fidelity, geometry, 4d, dynamic, efficient, outdoor, ar  
- **[OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception](https://arxiv.org/abs/2610.07569v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07569v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/OpenSplatGraph)  
  Keywords: high-fidelity, understanding, geometry, 3d gaussian, semantic, efficient, robotics, gaussian splatting, lightweight, mapping, ar  
- **[SteadySplats: Resampling of Low-Variance Gaussians for High-Fidelity Stochastic Rendering](https://arxiv.org/abs/2610.05576v2)**  
  Authors: Felix Windisch, Thomas Köhler, Lukas Radl, Chris Wyman, Georgios Kopanas, Bernhard Kerbl, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05576v2.pdf)  
  Keywords: high-fidelity, 3d gaussian, efficient, gaussian splatting, ar  
- **[Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting](https://arxiv.org/abs/2610.05289v1)**  
  Authors: Xiaobiao Du, Beixi Hao, Zhen Fang, Tianqing Zhu, Richard Hartley, Xin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05289v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiaobiaodu.github.io/mobile-4dgs-project)  
  Keywords: high-fidelity, motion, 3d gaussian, compact, 4d, dynamic, gaussian splatting, lightweight, head, ar, deformation  
- **[Return-to-Home Feasible Micro-Aerial Vehicle Exploration for 3D Gaussian Splatting Reconstruction](https://arxiv.org/abs/2610.04013v1)**  
  Authors: Prajit Krisshnakumar, Fan Yang, Koichiro Niinuma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04013v1.pdf)  
  Keywords: high-fidelity, geometry, 3d gaussian, gaussian splatting, lightweight, head, 3d reconstruction, ar  
- **[ManifoldSplat: Language-Guided Semantic Shape Editing of 3D Gaussian Head Avatars](https://arxiv.org/abs/2610.03599v1)**  
  Authors: Antonio Canela, Jordi Sànchez-Riera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03599v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://a-canela.github.io/manifoldsplat)  
  Keywords: high-fidelity, geometry, animation, 3d gaussian, semantic, gaussian splatting, head, ar, avatar  
- **[Budgeted-GS: Real-Time Large-Scale Gaussian Splatting via Factoring LOD](https://arxiv.org/abs/2610.03162v1)**  
  Authors: Haipeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03162v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, gaussian splatting, high quality, ar  
- **[SCION: Scene Composition with Instanced Neural Primitives](https://arxiv.org/abs/2610.02322v2)**  
  Authors: William Koch, Amogh Joshi, Cyrus Vachha, Cheng Zheng, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02322v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://light.princeton.edu/SCION)  
  Keywords: animation, 3d gaussian, compact, compression, gaussian splatting, lightweight, high quality, human, ar  
- **[EffGS: Efficient and High-Fidelity Gaussian Splatting](https://arxiv.org/abs/2609.39553v1)**  
  Authors: Changbai Li, Shuo Yang, Yichen Yang, Shuwei Shao, Huobin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39553v1.pdf)  
  Keywords: high-fidelity, compact, 3d gaussian, efficient, gaussian splatting, acceleration, ar  

### Ray Tracing

- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: ray tracing, 3d gaussian, efficient, gaussian splatting, head, ar, lighting  
- **[Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)**  
  Authors: Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/vorotracing)  
  Keywords: fast, ray tracing, motion, real-time rendering, 3d gaussian, compact, gaussian splatting, face, ar, nerf  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: reflection, ray tracing, fast, 3d gaussian, compact, shadow, efficient, gaussian splatting, ar, mapping, nerf  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: reflection, ray tracing, illumination, efficient, gaussian splatting, face, ar, relighting, lighting  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: high-fidelity, ray tracing, reflection, motion, geometry, 3d gaussian, dynamic, gaussian splatting, face, human, ar  

### Relighting

- **[Gaussian Splatting with Reflections Guided by What is Seen](https://arxiv.org/abs/2610.13757v1)**  
  Authors: Yiming Liang, Tianyu Xiao, Hiroshi Ishikawa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13757v1.pdf)  
  Keywords: reflection, 3d gaussian, gaussian splatting, nerf, ar  
- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: ray tracing, 3d gaussian, efficient, gaussian splatting, head, ar, lighting  
- **[OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs](https://arxiv.org/abs/2610.12461v1)**  
  Authors: You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12461v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ouroworld.userwei.com)  
  Keywords: motion, illumination, 3d gaussian, 4d, dynamic, gaussian splatting, ar, deformation  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: real-time rendering, geometry, illumination, 3d gaussian, dynamic, gaussian splatting, lightweight, face, ar  
- **[3DTexMOR: 3D Gaussian Multi-Object Removal via Texture-Space Inpainting](https://arxiv.org/abs/2610.11198v1)**  
  Authors: Kunxin Guang, Yonghao Zhao, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11198v1.pdf)  
  Keywords: reflection, geometry, 3d gaussian, nerf, ar  
- **[Casual Flash Lighting for Gaussian Splat Inverse Rendering](https://arxiv.org/abs/2610.06035v1)**  
  Authors: Jiamin Xu, Dongheng Wei, Jiarong Zhao, Qi Wang, James Tompkin, Weiwei Xu, Gang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.06035v1.pdf)  
  Keywords: lighting, geometry, illumination, relighting, ar  
- **[VolS-GS: Relightable Gaussian Splatting with Volumetric Subsurface Scattering](https://arxiv.org/abs/2610.04007v2)**  
  Authors: Junyeong Ahn, Jaegul Choo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04007v2.pdf)  
  Keywords: shadow, efficient, gaussian splatting, relightable, face, ar, relighting, lighting  
- **[EvenSplat: Coupled 2D-3D Decomposition for Gaussian Splatting under Exposure and Illumination Variation](https://arxiv.org/abs/2610.01876v1)**  
  Authors: Tongyu Wu, Jacob Edwards, Ziteng Cui, Caigui Jiang, Cheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01876v1.pdf)  
  Keywords: geometry, illumination, 3d gaussian, shadow, gaussian splatting, face, ar, lighting  
- **[EndoPrior-GS: Dynamic Endoscopic Reconstruction with a Joint Texture Prior](https://arxiv.org/abs/2609.37874v1)**  
  Authors: Jiaqi Huang, Shidong Wang, Tong Xin, Kabita Adhikari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiaqi-huang-77.github.io/EndoPrior-GS)  
  Keywords: real-time rendering, geometry, illumination, 3d gaussian, dynamic, gaussian splatting, ar, nerf  
- **[CollisionSplatting: Collision-Aware Motion Planning in 3DGS Scenes with Image-Conditioned Objectives and Adjustable Conservatism](https://arxiv.org/abs/2609.35619v1)**  
  Authors: R. Khorrambakht, Joaquim Ortiz-Haro, Stephan Weiss, Ludovic Righetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35619v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, vr, ar, lighting  

### SLAM

*Showing the latest 50 out of 75 papers*

- **[Splat2Act: From Captured Scenes to Personalized VLA Manipulation](https://arxiv.org/abs/2610.13945v1)**  
  Authors: Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, Gunjan Chhablani, Muhammad Zubair Irshad, Zsolt Kira  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13945v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, human, tracking, ar  
- **[OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception](https://arxiv.org/abs/2610.07569v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07569v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/OpenSplatGraph)  
  Keywords: high-fidelity, understanding, geometry, 3d gaussian, semantic, efficient, robotics, gaussian splatting, lightweight, mapping, ar  
- **[SURGE: Sonar-fUsed Reconstruction and localization via image-gated Graph Estimation](https://arxiv.org/abs/2610.07472v1)**  
  Authors: Mohammed Ibrahim M, Vallabh Deogaonkar, Trung Dong, Jane Shin, Abhilash Somayajula, Xiaomin Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07472v1.pdf)  
  Keywords: understanding, geometry, compact, gaussian splatting, ar, localization  
- **[FOCUS: Fine-Grained Open-Vocabulary Change Detection for Uncertainty-Aware Semi-Static Scenes](https://arxiv.org/abs/2610.05639v1)**  
  Authors: Can Xu, Mingfeng Yuan, Mahan Mohammadi, Steven L. Waslander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05639v1.pdf)  
  Keywords: geometry, 3d gaussian, semantic, mapping, ar  
- **[CellSplat4D: PSF-Aware 4D Gaussian Splatting for Sparse Robotic Live-Cell Imaging](https://arxiv.org/abs/2610.04199v1)**  
  Authors: Yingda Tao, Guoyu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04199v1.pdf)  
  Keywords: motion, 4d, gaussian splatting, tracking, ar  
- **[VoxelSynth3D: Interpretable Volumetric Image-Domain Metal Artifact Reduction with a Paired Synthetic CLINIC-Metal Benchmark](https://arxiv.org/abs/2610.01512v1)**  
  Authors: Amritesh Banerjee, Abdul Basit, Renil Renji Joseph, Nouhaila Innan, Muhammad Shafique  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01512v1.pdf)  
  Keywords: face, ar, localization, 3d gaussian  
- **[Lens Flare Removal and Reconstruction](https://arxiv.org/abs/2609.39527v1)**  
  Authors: Tarun Yenamandra, Jonathon Luiten, Daniel Cremers, Nathan Matsuda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39527v1.pdf)  
  Keywords: ar, gaussian splatting, localization  
- **[DispFlow-GS: Displacement Flow Supervision with Motion Disentangling for Monocular Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2609.36940v1)**  
  Authors: Thai Duy Nguyen, Haitian Zhang, Addison Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36940v1.pdf)  
  Keywords: motion, geometry, 3d gaussian, dynamic, gaussian splatting, localization, ar, deformation  
- **[EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation](https://arxiv.org/abs/2609.34853v1)**  
  Authors: Sungho Moon, Kota Shimomura, Junwoo Park, Wonhyeok Choi, Seunghun Lee, Takayoshi Yamashita, Sunghoon Im  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34853v1.pdf)  
  Keywords: understanding, compact, 3d gaussian, segmentation, gaussian splatting, ar, localization  
- **[Reliability-Regulated Trajectory Optimization for Progressive COLMAP-Free 3D Gaussian Splatting](https://arxiv.org/abs/2609.30865v1)**  
  Authors: Zijian Wu, Jinliang Wang, Zidian Lin, Ying Song, Ziqian Lu, Hanjie Ma, Zhen Ye, Mingfeng Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30865v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Zijian1026/RRTO-CF3DGS?style=social)](https://github.com/Zijian1026/RRTO-CF3DGS)  
  Keywords: motion, 3d gaussian, dynamic, gaussian splatting, tracking, ar  

### Scene Understanding

*Showing the latest 50 out of 97 papers*

- **[Measurable Semantic 3D Gaussian Splatting with Joint Region and Depth Supervision for Interactive Building Inspection](https://arxiv.org/abs/2610.13143v1)**  
  Authors: Yi Zhang, Tian Tan, Ray Kai Leung Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13143v1.pdf)  
  Keywords: geometry, 3d gaussian, semantic, gaussian splatting, face, 3d reconstruction, ar  
- **[PCAsplat: Gaussian Splatting with Local PCA Regularization](https://arxiv.org/abs/2610.11011v1)**  
  Authors: Vitor Matias, Filipe Nascimento, Kiyohiro Nakayama, João Paulo Lima, Márcus Lobo, Gordon Wetzstein, Leonidas Guibas, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11011v1.pdf)  
  Keywords: geometry, segmentation, gaussian splatting, face, ar, 3d reconstruction, nerf  
- **[Post-Training Semantic Lifting for 3D Gaussian Splatting: Separating Detector, Lifting and Representation Error](https://arxiv.org/abs/2610.08756v1)**  
  Authors: Iván Verdugo Guerra, Ezequiel López Rubio, Jorge García González  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.08756v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, 3d gaussian  
- **[View Matters: Keyframe-Guided Text-Driven 3D Gaussian Editing](https://arxiv.org/abs/2610.08179v1)**  
  Authors: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Xuanyu Wang, Feng Lei, Sha Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.08179v1.pdf)  
  Keywords: semantic, ar, 3d gaussian  
- **[OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception](https://arxiv.org/abs/2610.07569v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07569v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/OpenSplatGraph)  
  Keywords: high-fidelity, understanding, geometry, 3d gaussian, semantic, efficient, robotics, gaussian splatting, lightweight, mapping, ar  
- **[SURGE: Sonar-fUsed Reconstruction and localization via image-gated Graph Estimation](https://arxiv.org/abs/2610.07472v1)**  
  Authors: Mohammed Ibrahim M, Vallabh Deogaonkar, Trung Dong, Jane Shin, Abhilash Somayajula, Xiaomin Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07472v1.pdf)  
  Keywords: understanding, geometry, compact, gaussian splatting, ar, localization  
- **[MoonGS: High-quality Representation of the Lunar Surface via Gaussian Splatting Using Robust Depth Features from Image Pairs](https://arxiv.org/abs/2610.07110v1)**  
  Authors: Yun Jiang, Bo Zheng, Yingying Zhang, Xueming Xiao, Tao Hu, Hutao Cui, Zhiguo Meng, Ke Gao, Yang Gao, Meibao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07110v1.pdf) | [![GitHub](https://img.shields.io/github/stars/InRobots/MoonBlender?style=social)](https://github.com/InRobots/MoonBlender)  
  Keywords: 3d gaussian, semantic, gaussian splatting, head, face, ar, 3d reconstruction, nerf  
- **[MaRO-GS: Mask-Robust Object-Centric Gaussian Splatting from Inconsistent Multi-view Masks](https://arxiv.org/abs/2610.06472v1)**  
  Authors: Eunji Kim, Gahyeon Kim, Gianella Cravioto, Dong-hun Lee, Chaewon Moon, Chae-yeong Song, Sang-hyo Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.06472v1.pdf)  
  Keywords: head, segmentation, gaussian splatting, ar  
- **[FOCUS: Fine-Grained Open-Vocabulary Change Detection for Uncertainty-Aware Semi-Static Scenes](https://arxiv.org/abs/2610.05639v1)**  
  Authors: Can Xu, Mingfeng Yuan, Mahan Mohammadi, Steven L. Waslander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05639v1.pdf)  
  Keywords: geometry, 3d gaussian, semantic, mapping, ar  
- **[GS-Codec: A Gaussian-Splatting Bottleneck for Neural Audio Coding](https://arxiv.org/abs/2610.04651v1)**  
  Authors: Ron Aluf, Alon Canfi, Eliya Nachmani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04651v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ronaluf.github.io/gs-codec)  
  Keywords: compact, semantic, gaussian splatting, lightweight, ar  



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
