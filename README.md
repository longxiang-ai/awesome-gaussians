# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-gaussians/)**: an interactive paper map, monthly trends, topic network and co-author network of every tracked paper.

> Last Update: 2026-10-13 04:28:53

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
  Keywords: ar, 3d gaussian, survey, geometry, gaussian splatting  
- **[OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones](https://arxiv.org/abs/2609.24253v1)**  
  Authors: Zhongrui You, Zhen Li, Junli Liu, Zhigang Wang, Bin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24253v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://openflyscan.github.io)  
  Keywords: high-fidelity, face, 3d gaussian, ar, survey, gaussian splatting  
- **[Quality Assessment of 3D Gaussian Splatting: Distortions, Benchmarks, and Open Challenges](https://arxiv.org/abs/2609.23027v1)**  
  Authors: Shuai Liu, Binqiang Liu, Qingyu Mao, Jiacong Chen, Yongsheng Liang, Youneng Bao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23027v1.pdf)  
  Keywords: ar, 3d gaussian, survey, gaussian splatting, compression  
- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: ar, 3d reconstruction, motion, survey, geometry, gaussian splatting, illumination  
- **[UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys](https://arxiv.org/abs/2608.06404v1)**  
  Authors: Junxiong Zhou, Xuechen Li, Chonghao Qiu, Lang Qiao, Xiaowei Jia, Qi Yang, Chishan Zhang, Leikun Yin, Nanshan You, Vipin Kumar, David Mulla, Ce Yang, Zhenong Jin, Licheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06404v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://link-dev.github.io/UAV3DCrop)  
  Keywords: ar, 3d gaussian, 3d reconstruction, survey, dynamic, nerf, geometry, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 80 papers*

- **[Make It Flow: Animating Water in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2610.13860v1)**  
  Authors: Kjell Keune, Florian Hahlbohm, Jannis Möller, Susana Castillo, Martin Eisemann, Marcus Magnor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13860v1.pdf)  
  Keywords: ar, 3d gaussian, motion, dynamic, animation, real-time rendering, gaussian splatting, human  
- **[NovaSplat: Model-Free 6D Object Pose Estimation via 3D Gaussian Splatting Onboarding and Refinement](https://arxiv.org/abs/2610.13309v1)**  
  Authors: Georgios Floros, Evangelos Sartinas, Orestis Vangelis, Maria Pateraki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13309v1.pdf) | [![GitHub](https://img.shields.io/github/stars/POSE-Lab/novasplat?style=social)](https://github.com/POSE-Lab/novasplat)  
  Keywords: ar, face, 3d gaussian, fast, gaussian splatting  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: ar, face, 3d gaussian, dynamic, geometry, lightweight, real-time rendering, gaussian splatting, illumination  
- **[Efficient 3D Gaussian Head Avatars for Edge Devices](https://arxiv.org/abs/2610.09821v1)**  
  Authors: Umar Farooq, Jean-Yves Guillemaut, Adrian Hilton, Marco Volino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09821v1.pdf)  
  Keywords: efficient, head, avatar, 3d gaussian, ar, efficient rendering, compression  
- **[LoCoSplat: Real-Time Feed-Forward 3D Gaussian Splatting with Minimal 3D Reasoning](https://arxiv.org/abs/2610.04351v1)**  
  Authors: Sinan Wang, Jinjin He, Yuchen Sun, Duowen Chen, Shenyifan Lu, Bo Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04351v1.pdf)  
  Keywords: ar, 3d gaussian, fast, dynamic, gaussian splatting  
- **[Budgeted-GS: Real-Time Large-Scale Gaussian Splatting via Factoring LOD](https://arxiv.org/abs/2610.03162v1)**  
  Authors: Haipeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03162v1.pdf)  
  Keywords: ar, 3d gaussian, high quality, real-time rendering, gaussian splatting  
- **[FactorSplat: Appearance-Controllable Gaussian Proxies for Medical Volume Rendering](https://arxiv.org/abs/2610.02382v1)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/FactorSplat)  
  Keywords: ar, fast, geometry, medical, gaussian splatting  
- **[One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time Avatars](https://arxiv.org/abs/2610.02207v1)**  
  Authors: Ramazan Fazylov, Stamatis Lefkimmiatis, Ivan Laptev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02207v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ramazan793.github.io/gala)  
  Keywords: efficient, ar, avatar, 3d gaussian, fast, dynamic, animation  
- **[Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation](https://arxiv.org/abs/2610.01114v1)**  
  Authors: Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01114v1.pdf)  
  Keywords: efficient, ar, fast, motion, deformation, gaussian splatting  
- **[Dirichlet Splatting: Differentiable Rendering for Wave-Based Inverse Problems](https://arxiv.org/abs/2610.00618v1)**  
  Authors: Xingyu Chen, Wuqiong Zhao, Xinyu Zhang, Tzu-Mao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00618v1.pdf)  
  Keywords: fast, ar, 3d gaussian, gaussian splatting  

### Applications

*Showing the latest 50 out of 500 papers*

- **[Splat2Act: From Captured Scenes to Personalized VLA Manipulation](https://arxiv.org/abs/2610.13945v1)**  
  Authors: Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, Gunjan Chhablani, Muhammad Zubair Irshad, Zsolt Kira  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13945v1.pdf)  
  Keywords: tracking, ar, 3d gaussian, geometry, gaussian splatting, human  
- **[Make It Flow: Animating Water in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2610.13860v1)**  
  Authors: Kjell Keune, Florian Hahlbohm, Jannis Möller, Susana Castillo, Martin Eisemann, Marcus Magnor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13860v1.pdf)  
  Keywords: ar, 3d gaussian, motion, dynamic, animation, real-time rendering, gaussian splatting, human  
- **[SimVTA: Simulation-Grounded Video-Trajectory Alignment for Driving World Action Models](https://arxiv.org/abs/2610.13781v1)**  
  Authors: Changhui Jing, Haochen Tian, Hongchen Li, Tianyu Li, Caojun Wang, Zihao Zhang, Yanhao Liu, Chengen Xie, Bailin Li, Hao Zhao, Zhenjie Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13781v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting  
- **[Gaussian Splatting with Reflections Guided by What is Seen](https://arxiv.org/abs/2610.13757v1)**  
  Authors: Yiming Liang, Tianyu Xiao, Hiroshi Ishikawa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13757v1.pdf)  
  Keywords: ar, 3d gaussian, nerf, reflection, gaussian splatting  
- **[AutoBio+: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories](https://arxiv.org/abs/2610.13643v1)**  
  Authors: Xuanye Wu, Yue Shi, Yongcan Yang, Yiqun Wang, Zhaoqi Wan, Dayu Xia, Jiezhang Cao, Xiangfei Li, Yao Mu, Guangtao Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13643v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://autobio-plus.github.io/AutoBioPlus)  
  Keywords: dynamic, ar, efficient  
- **[Efficient Confidence-Aware Densification for 3DGS](https://arxiv.org/abs/2610.13541v1)**  
  Authors: Manuel Hofer, Thomas Köhler, Felix Windisch, Bernhard Kerbl, Markus Steinberger, Lukas Radl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13541v1.pdf)  
  Keywords: 4d, ar, efficient, 3d gaussian, gaussian splatting  
- **[SplatQ: Interaction-Aware Pruning of 3D Gaussian Splatting via Quadratic Selection](https://arxiv.org/abs/2610.13503v1)**  
  Authors: Hongbin Ye, Haixu Liu, Shenwei Kang, Wenxiu Wei, Tinglan Wang, Hongdong Zhu, Fan Tang, Qi Gao, Yin Ma, Kai Wen, Hai Wei, Nuo Qian, Wei-Shi Zheng, Shaobo Chen, Fa-Ting Hong, Jingke Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13503v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting  
- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: efficient, head, ar, 3d gaussian, gaussian splatting, ray tracing, lighting  
- **[ManeuverFlow: Maneuver Hypothesis Generation with Future Evidence for Trajectory Evaluation and Refinement in End-to-End Autonomous Driving](https://arxiv.org/abs/2610.13409v1)**  
  Authors: Yuhao Wei, Yong Chen, Chen Yang, Yingchen Wang, Delin Ouyang, Lingfeng Qi, Qi Lan, Zhanhua Zhang, Jie Li, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13409v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wyh-autonomy/maneuverflow?style=social)](https://github.com/wyh-autonomy/maneuverflow)  
  Keywords: ar, lightweight, autonomous driving  
- **[NovaSplat: Model-Free 6D Object Pose Estimation via 3D Gaussian Splatting Onboarding and Refinement](https://arxiv.org/abs/2610.13309v1)**  
  Authors: Georgios Floros, Evangelos Sartinas, Orestis Vangelis, Maria Pateraki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13309v1.pdf) | [![GitHub](https://img.shields.io/github/stars/POSE-Lab/novasplat?style=social)](https://github.com/POSE-Lab/novasplat)  
  Keywords: ar, face, 3d gaussian, fast, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 171 papers*

- **[Splat2Act: From Captured Scenes to Personalized VLA Manipulation](https://arxiv.org/abs/2610.13945v1)**  
  Authors: Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, Gunjan Chhablani, Muhammad Zubair Irshad, Zsolt Kira  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13945v1.pdf)  
  Keywords: tracking, ar, 3d gaussian, geometry, gaussian splatting, human  
- **[Make It Flow: Animating Water in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2610.13860v1)**  
  Authors: Kjell Keune, Florian Hahlbohm, Jannis Möller, Susana Castillo, Martin Eisemann, Marcus Magnor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13860v1.pdf)  
  Keywords: ar, 3d gaussian, motion, dynamic, animation, real-time rendering, gaussian splatting, human  
- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: efficient, head, ar, 3d gaussian, gaussian splatting, ray tracing, lighting  
- **[NovaSplat: Model-Free 6D Object Pose Estimation via 3D Gaussian Splatting Onboarding and Refinement](https://arxiv.org/abs/2610.13309v1)**  
  Authors: Georgios Floros, Evangelos Sartinas, Orestis Vangelis, Maria Pateraki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13309v1.pdf) | [![GitHub](https://img.shields.io/github/stars/POSE-Lab/novasplat?style=social)](https://github.com/POSE-Lab/novasplat)  
  Keywords: ar, face, 3d gaussian, fast, gaussian splatting  
- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, ar, dynamic, compact, geometry, sparse view, gaussian splatting  
- **[Measurable Semantic 3D Gaussian Splatting with Joint Region and Depth Supervision for Interactive Building Inspection](https://arxiv.org/abs/2610.13143v1)**  
  Authors: Yi Zhang, Tian Tan, Ray Kai Leung Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13143v1.pdf)  
  Keywords: ar, face, 3d gaussian, 3d reconstruction, geometry, semantic, gaussian splatting  
- **[Volume Rendering with Metric--Phase Fields for Thin Structures and Sign-Ambiguous Geometry](https://arxiv.org/abs/2610.13088v1)**  
  Authors: Junkai Deng, Jiayi Kong, Xuhui Chen, Guanli Hou, Fei Hou, Junhui Hou, Wenping Wang, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13088v1.pdf)  
  Keywords: ar, face, geometry  
- **[2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map](https://arxiv.org/abs/2610.11752v1)**  
  Authors: Jiwon Park, Dong-Uk Seo, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11752v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://2dgs-planner.github.io)  
  Keywords: efficient, ar, face, geometry, gaussian splatting  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: ar, face, 3d gaussian, dynamic, geometry, lightweight, real-time rendering, gaussian splatting, illumination  
- **[Rendering-Free Lookahead for Question-Guided Active Vision](https://arxiv.org/abs/2610.11039v1)**  
  Authors: Koya Sakamoto, Daichi Azuma, Shuhei Kurita, Naoya Chiba, Yusuke Iwasawa, Yutaka Matsuo, Taiki Miyanishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11039v1.pdf)  
  Keywords: head, ar, 3d gaussian, motion, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 192 papers*

- **[Make It Flow: Animating Water in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2610.13860v1)**  
  Authors: Kjell Keune, Florian Hahlbohm, Jannis Möller, Susana Castillo, Martin Eisemann, Marcus Magnor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13860v1.pdf)  
  Keywords: ar, 3d gaussian, motion, dynamic, animation, real-time rendering, gaussian splatting, human  
- **[AutoBio+: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories](https://arxiv.org/abs/2610.13643v1)**  
  Authors: Xuanye Wu, Yue Shi, Yongcan Yang, Yiqun Wang, Zhaoqi Wan, Dayu Xia, Jiezhang Cao, Xiangfei Li, Yao Mu, Guangtao Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13643v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://autobio-plus.github.io/AutoBioPlus)  
  Keywords: dynamic, ar, efficient  
- **[Efficient Confidence-Aware Densification for 3DGS](https://arxiv.org/abs/2610.13541v1)**  
  Authors: Manuel Hofer, Thomas Köhler, Felix Windisch, Bernhard Kerbl, Markus Steinberger, Lukas Radl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13541v1.pdf)  
  Keywords: 4d, ar, efficient, 3d gaussian, gaussian splatting  
- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, ar, dynamic, compact, geometry, sparse view, gaussian splatting  
- **[OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs](https://arxiv.org/abs/2610.12461v1)**  
  Authors: You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12461v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ouroworld.userwei.com)  
  Keywords: 4d, ar, 3d gaussian, motion, dynamic, deformation, gaussian splatting, illumination  
- **[LVS: Local View Synthesis from Relative Camera Pose by Reusing Previous Views](https://arxiv.org/abs/2610.12127v1)**  
  Authors: Qizhou Huo, Xuan Sun, Yongfei Guo, Zhipeng Wang, Yuanhao Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12127v1.pdf)  
  Keywords: ar, 3d gaussian, motion, lightweight, gaussian splatting  
- **[CoCam4D: Geometry-Aware Cooperative 4D Perception for Camera-Only Autonomous Driving](https://arxiv.org/abs/2610.11577v1)**  
  Authors: Soham Pahari, Sudip Das, Arindam Das, Ujjwal Bhattacharya  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11577v1.pdf)  
  Keywords: 4d, efficient, ar, 3d gaussian, dynamic, compact, autonomous driving, geometry  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: ar, face, 3d gaussian, dynamic, geometry, lightweight, real-time rendering, gaussian splatting, illumination  
- **[MATE4D: Matrix-Guided Editable 4D Generation from a Single Image](https://arxiv.org/abs/2610.11181v1)**  
  Authors: Xiaotian Chen, Dongfu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11181v1.pdf)  
  Keywords: vr, 4d, ar, 3d gaussian, motion, dynamic, geometry, deformation, lightweight  
- **[Rendering-Free Lookahead for Question-Guided Active Vision](https://arxiv.org/abs/2610.11039v1)**  
  Authors: Koya Sakamoto, Daichi Azuma, Shuhei Kurita, Naoya Chiba, Yusuke Iwasawa, Yutaka Matsuo, Taiki Miyanishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11039v1.pdf)  
  Keywords: head, ar, 3d gaussian, motion, gaussian splatting  

### Few-shot

- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, ar, dynamic, compact, geometry, sparse view, gaussian splatting  
- **[OX-NeRF: 3D X-ray Tomography Reconstruction from Sparse Views Using Implicit Neural Representation](https://arxiv.org/abs/2610.11547v1)**  
  Authors: Thomas Welsch, Min-Hsin Tu, David J. Chapman, Daniel E. Eakins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11547v1.pdf)  
  Keywords: ar, 3d reconstruction, nerf, sparse view, gaussian splatting  
- **[DensiTok: Making Feed-Forward 3D Gaussian Splatting See More Views Than It Is Given](https://arxiv.org/abs/2610.07958v1)**  
  Authors: Minhyeok Lee, Jungho Lee, Minseok Kang, Heeseung Choi, Ig-Jae Kim, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07958v1.pdf)  
  Keywords: head, ar, 3d gaussian, sparse-view, compact, geometry, gaussian splatting  
- **[Sparse-View 4D Gaussian Splatting via Spatiotemporal Priors and Generative Assistance](https://arxiv.org/abs/2610.04606v2)**  
  Authors: Shengqi Wang, Zhengxian Yang, Kaiwen Tian, Yang Liu, Bowen Liu, Hua Du, Taicheng Huang, Jiamin Wu, Tao Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04606v2.pdf)  
  Keywords: 4d, ar, motion, dynamic, sparse-view, geometry, sparse view, gaussian splatting  
- **[Sparse-GS2Mesh: 3D Gaussian Splatting Guided by Novel Stereo Views and 2DGS for Sparse View Surface Reconstruction](https://arxiv.org/abs/2610.04203v2)**  
  Authors: Younghyun Noh, Minje Kim, Tae-Kyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04203v2.pdf)  
  Keywords: efficient, ar, face, 3d gaussian, sparse-view, sparse view, geometry, gaussian splatting  
- **[UGOD: Uncertainty-Guided Opacity and Dropout for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.39089v1)**  
  Authors: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Chenghao Qian, Ziyang Wang, Xinqi Fan, Liangxiu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39089v1.pdf)  
  Keywords: head, ar, 3d gaussian, sparse-view, nerf, compact, lightweight, gaussian splatting  
- **[Remote Sensing Sparse-View 3D Gaussian Splatting via Depth Image-Based Rendering](https://arxiv.org/abs/2609.35612v1)**  
  Authors: Jiaming Kang, Zhengxia Zou, Zhenwei Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35612v1.pdf) | [![GitHub](https://img.shields.io/github/stars/kanehub/DIBR-GS?style=social)](https://github.com/kanehub/DIBR-GS)  
  Keywords: ar, face, 3d gaussian, sparse-view, nerf, gaussian splatting  
- **[GAPS: Generative Active Pseudo-view Selection for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.23436v2)**  
  Authors: Hongfei Zhu, Haochen Deng, Sitao Zhang, Ling Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23436v2.pdf)  
  Keywords: ar, 3d gaussian, sparse-view, nerf, geometry, real-time rendering, gaussian splatting  
- **[D3GS: Depth, DINO, and RGB Diffusion Co-Guided 3D Gaussian Splatting for Sparse-View Reconstruction](https://arxiv.org/abs/2609.22941v1)**  
  Authors: Yunqi Gao, Zhanfeng Liao, Hanzhang Tu, Zhaoqi Su, Guoqing Zheng, Songtao Wang, Hongwen Zhang, Zhou Xue, Leyuan Liu, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.22941v1.pdf)  
  Keywords: ar, 3d gaussian, sparse-view, nerf, geometry, gaussian splatting  
- **[LINGO: Latent Initialization and Gradient Optimization for Sparse-view X-ray Novel View Synthesis and CT Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2609.22849v1)**  
  Authors: Lifeng Xing, Dequan Jin, Kunpeng Bu, Peigeng He, Shihui Ying  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.22849v1.pdf)  
  Keywords: ar, 3d gaussian, dynamic, sparse-view, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 208 papers*

- **[Splat2Act: From Captured Scenes to Personalized VLA Manipulation](https://arxiv.org/abs/2610.13945v1)**  
  Authors: Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, Gunjan Chhablani, Muhammad Zubair Irshad, Zsolt Kira  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13945v1.pdf)  
  Keywords: tracking, ar, 3d gaussian, geometry, gaussian splatting, human  
- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, ar, dynamic, compact, geometry, sparse view, gaussian splatting  
- **[Measurable Semantic 3D Gaussian Splatting with Joint Region and Depth Supervision for Interactive Building Inspection](https://arxiv.org/abs/2610.13143v1)**  
  Authors: Yi Zhang, Tian Tan, Ray Kai Leung Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13143v1.pdf)  
  Keywords: ar, face, 3d gaussian, 3d reconstruction, geometry, semantic, gaussian splatting  
- **[Volume Rendering with Metric--Phase Fields for Thin Structures and Sign-Ambiguous Geometry](https://arxiv.org/abs/2610.13088v1)**  
  Authors: Junkai Deng, Jiayi Kong, Xuhui Chen, Guanli Hou, Fei Hou, Junhui Hou, Wenping Wang, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13088v1.pdf)  
  Keywords: ar, face, geometry  
- **[2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map](https://arxiv.org/abs/2610.11752v1)**  
  Authors: Jiwon Park, Dong-Uk Seo, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11752v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://2dgs-planner.github.io)  
  Keywords: efficient, ar, face, geometry, gaussian splatting  
- **[CoCam4D: Geometry-Aware Cooperative 4D Perception for Camera-Only Autonomous Driving](https://arxiv.org/abs/2610.11577v1)**  
  Authors: Soham Pahari, Sudip Das, Arindam Das, Ujjwal Bhattacharya  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11577v1.pdf)  
  Keywords: 4d, efficient, ar, 3d gaussian, dynamic, compact, autonomous driving, geometry  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: ar, face, 3d gaussian, dynamic, geometry, lightweight, real-time rendering, gaussian splatting, illumination  
- **[OX-NeRF: 3D X-ray Tomography Reconstruction from Sparse Views Using Implicit Neural Representation](https://arxiv.org/abs/2610.11547v1)**  
  Authors: Thomas Welsch, Min-Hsin Tu, David J. Chapman, Daniel E. Eakins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11547v1.pdf)  
  Keywords: ar, 3d reconstruction, nerf, sparse view, gaussian splatting  
- **[FlyMark: Training-Free Invisible Watermarking of 3D Gaussian Splatting via a Fruit Fly Connectome](https://arxiv.org/abs/2610.11364v1)**  
  Authors: Ziyuan Luo, Haoliang Li, Renjie Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11364v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, geometry  
- **[3DTexMOR: 3D Gaussian Multi-Object Removal via Texture-Space Inpainting](https://arxiv.org/abs/2610.11198v1)**  
  Authors: Kunxin Guang, Yonghao Zhao, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11198v1.pdf)  
  Keywords: ar, 3d gaussian, nerf, reflection, geometry  

### Large Scene

- **[DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video](https://arxiv.org/abs/2610.09720v1)**  
  Authors: Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09720v1.pdf)  
  Keywords: 4d, high-fidelity, efficient, ar, outdoor, dynamic, geometry  
- **[LEGO-Anything: Coding Agents for 3D Scene Reconstruction](https://arxiv.org/abs/2609.36380v1)**  
  Authors: Xirui Li, Peng Shi, Mingwen Dong, Sheng Zhang, Zhuoyan Xu, Dongkyu Lee, Shuaichen Chang, Yi Xiang, Lin Pan, Jiarong Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36380v1.pdf)  
  Keywords: outdoor, ar, face, geometry  
- **[Federated 3D Gaussian Splatting for Large-Scale Scene Reconstruction at Wireless Edge](https://arxiv.org/abs/2609.32177v1)**  
  Authors: Guanlin Wu, Chao Hu, Pu Chen, Juyong Zhang, Han Hu, Shuguang Cui, Jie Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32177v1.pdf)  
  Keywords: efficient, ar, face, 3d gaussian, lightweight, gaussian splatting, large scene  
- **[ChronoFuseGS: Multi-Temporal Gaussian Fusion with Per-Splat Persistence and Change Visualization](https://arxiv.org/abs/2609.31339v1)**  
  Authors: Tobias Batik, Diana Marin, Peter Kán, Hannes Kaufmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31339v1.pdf)  
  Keywords: outdoor, ar, gaussian splatting  
- **[OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning](https://arxiv.org/abs/2609.29985v1)**  
  Authors: Haoran Wang, Shaoyu Cai, Adrian Azzarelli, Zhuodong Jiang, Guoxi Huang, Eng Tat Khoo, Brett Seymour, Fan Zhang, David Bull, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29985v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, 3d reconstruction, fast, nerf, compact, real-time rendering, gaussian splatting, large scene  
- **[Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models](https://arxiv.org/abs/2609.26007v1)**  
  Authors: Yuhang Zhang, Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Weiying Wang, Steven Yang, Qingsong Yan, Chao Yan, Mir Feroskhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26007v1.pdf)  
  Keywords: ar, 3d gaussian, motion, outdoor, gaussian splatting  
- **[Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking](https://arxiv.org/abs/2609.25746v1)**  
  Authors: Edward Beng Wai Tan, Siew-Kei Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25746v1.pdf)  
  Keywords: tracking, ar, face, 3d gaussian, outdoor, geometry, slam, gaussian splatting  
- **[Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene Reconstruction](https://arxiv.org/abs/2609.23796v2)**  
  Authors: Yang-Tian Sun, Tianjia Liu, Zehuan Huang, Yi-Hua Huang, Xiaoyang Lyu, Ziyi Yang, Zi-Xin Zou, Yuan-Chen Guo, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23796v2.pdf)  
  Keywords: ar, high-fidelity, face, outdoor, geometry  
- **[Cube-Splat: High-Fidelity 360° Gaussian Splatting SLAM via Cubemap Factorization and Adjoint-Consistent Optimization](https://arxiv.org/abs/2609.21347v1)**  
  Authors: Xiangfei Guo, Hao Shi, Yufan Zhang, Zhonghua Yi, Yongqi Mao, Xiaoting Yin, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21347v1.pdf) | [![GitHub](https://img.shields.io/github/stars/guoxf304/CubeSplat?style=social)](https://github.com/guoxf304/CubeSplat)  
  Keywords: tracking, high-fidelity, face, 3d gaussian, ar, mapping, outdoor, slam, gaussian splatting  
- **[4DGS-Fixer: Generative Sparse-View 4D Gaussian Splatting with Iterative Refinement Guided by Video Diffusion Priors](https://arxiv.org/abs/2609.21176v3)**  
  Authors: Haitao Huang, Shenghao Zhao, Boyuan Tian, Shin-Fang Chng, Songlin Yang, Sheila Lim, Huangying Zhan, Yi Xu, Anyi Rao, Frank Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21176v3.pdf)  
  Keywords: 4d, ar, dynamic, sparse-view, gaussian splatting, large scene  

### Model Compression

*Showing the latest 50 out of 203 papers*

- **[AutoBio+: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories](https://arxiv.org/abs/2610.13643v1)**  
  Authors: Xuanye Wu, Yue Shi, Yongcan Yang, Yiqun Wang, Zhaoqi Wan, Dayu Xia, Jiezhang Cao, Xiangfei Li, Yao Mu, Guangtao Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13643v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://autobio-plus.github.io/AutoBioPlus)  
  Keywords: dynamic, ar, efficient  
- **[Efficient Confidence-Aware Densification for 3DGS](https://arxiv.org/abs/2610.13541v1)**  
  Authors: Manuel Hofer, Thomas Köhler, Felix Windisch, Bernhard Kerbl, Markus Steinberger, Lukas Radl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13541v1.pdf)  
  Keywords: 4d, ar, efficient, 3d gaussian, gaussian splatting  
- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: efficient, head, ar, 3d gaussian, gaussian splatting, ray tracing, lighting  
- **[ManeuverFlow: Maneuver Hypothesis Generation with Future Evidence for Trajectory Evaluation and Refinement in End-to-End Autonomous Driving](https://arxiv.org/abs/2610.13409v1)**  
  Authors: Yuhao Wei, Yong Chen, Chen Yang, Yingchen Wang, Delin Ouyang, Lingfeng Qi, Qi Lan, Zhanhua Zhang, Jie Li, Guofa Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13409v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wyh-autonomy/maneuverflow?style=social)](https://github.com/wyh-autonomy/maneuverflow)  
  Keywords: ar, lightweight, autonomous driving  
- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, ar, dynamic, compact, geometry, sparse view, gaussian splatting  
- **[LVS: Local View Synthesis from Relative Camera Pose by Reusing Previous Views](https://arxiv.org/abs/2610.12127v1)**  
  Authors: Qizhou Huo, Xuan Sun, Yongfei Guo, Zhipeng Wang, Yuanhao Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12127v1.pdf)  
  Keywords: ar, 3d gaussian, motion, lightweight, gaussian splatting  
- **[2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map](https://arxiv.org/abs/2610.11752v1)**  
  Authors: Jiwon Park, Dong-Uk Seo, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11752v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://2dgs-planner.github.io)  
  Keywords: efficient, ar, face, geometry, gaussian splatting  
- **[CoCam4D: Geometry-Aware Cooperative 4D Perception for Camera-Only Autonomous Driving](https://arxiv.org/abs/2610.11577v1)**  
  Authors: Soham Pahari, Sudip Das, Arindam Das, Ujjwal Bhattacharya  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11577v1.pdf)  
  Keywords: 4d, efficient, ar, 3d gaussian, dynamic, compact, autonomous driving, geometry  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: ar, face, 3d gaussian, dynamic, geometry, lightweight, real-time rendering, gaussian splatting, illumination  
- **[MATE4D: Matrix-Guided Editable 4D Generation from a Single Image](https://arxiv.org/abs/2610.11181v1)**  
  Authors: Xiaotian Chen, Dongfu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11181v1.pdf)  
  Keywords: vr, 4d, ar, 3d gaussian, motion, dynamic, geometry, deformation, lightweight  

### Quality Enhancement

*Showing the latest 50 out of 71 papers*

- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, ar, dynamic, compact, geometry, sparse view, gaussian splatting  
- **[DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video](https://arxiv.org/abs/2610.09720v1)**  
  Authors: Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09720v1.pdf)  
  Keywords: 4d, high-fidelity, efficient, ar, outdoor, dynamic, geometry  
- **[OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception](https://arxiv.org/abs/2610.07569v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07569v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/OpenSplatGraph)  
  Keywords: efficient, high-fidelity, ar, 3d gaussian, mapping, understanding, geometry, semantic, lightweight, gaussian splatting, robotics  
- **[SteadySplats: Resampling of Low-Variance Gaussians for High-Fidelity Stochastic Rendering](https://arxiv.org/abs/2610.05576v2)**  
  Authors: Felix Windisch, Thomas Köhler, Lukas Radl, Chris Wyman, Georgios Kopanas, Bernhard Kerbl, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05576v2.pdf)  
  Keywords: efficient, ar, high-fidelity, 3d gaussian, gaussian splatting  
- **[Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting](https://arxiv.org/abs/2610.05289v1)**  
  Authors: Xiaobiao Du, Beixi Hao, Zhen Fang, Tianqing Zhu, Richard Hartley, Xin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05289v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiaobiaodu.github.io/mobile-4dgs-project)  
  Keywords: 4d, high-fidelity, head, 3d gaussian, ar, motion, dynamic, compact, deformation, lightweight, gaussian splatting  
- **[Return-to-Home Feasible Micro-Aerial Vehicle Exploration for 3D Gaussian Splatting Reconstruction](https://arxiv.org/abs/2610.04013v1)**  
  Authors: Prajit Krisshnakumar, Fan Yang, Koichiro Niinuma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04013v1.pdf)  
  Keywords: head, high-fidelity, ar, 3d gaussian, 3d reconstruction, geometry, lightweight, gaussian splatting  
- **[ManifoldSplat: Language-Guided Semantic Shape Editing of 3D Gaussian Head Avatars](https://arxiv.org/abs/2610.03599v1)**  
  Authors: Antonio Canela, Jordi Sànchez-Riera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03599v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://a-canela.github.io/manifoldsplat)  
  Keywords: head, high-fidelity, avatar, 3d gaussian, ar, geometry, animation, semantic, gaussian splatting  
- **[Budgeted-GS: Real-Time Large-Scale Gaussian Splatting via Factoring LOD](https://arxiv.org/abs/2610.03162v1)**  
  Authors: Haipeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03162v1.pdf)  
  Keywords: ar, 3d gaussian, high quality, real-time rendering, gaussian splatting  
- **[SCION: Scene Composition with Instanced Neural Primitives](https://arxiv.org/abs/2610.02322v2)**  
  Authors: William Koch, Amogh Joshi, Cyrus Vachha, Cheng Zheng, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02322v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://light.princeton.edu/SCION)  
  Keywords: ar, 3d gaussian, compact, animation, high quality, gaussian splatting, lightweight, human, compression  
- **[EffGS: Efficient and High-Fidelity Gaussian Splatting](https://arxiv.org/abs/2609.39553v1)**  
  Authors: Changbai Li, Shuo Yang, Yichen Yang, Shuwei Shao, Huobin Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39553v1.pdf)  
  Keywords: efficient, high-fidelity, ar, 3d gaussian, compact, acceleration, gaussian splatting  

### Ray Tracing

- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: efficient, head, ar, 3d gaussian, gaussian splatting, ray tracing, lighting  
- **[Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)**  
  Authors: Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/vorotracing)  
  Keywords: ray tracing, ar, face, 3d gaussian, fast, motion, nerf, compact, real-time rendering, gaussian splatting  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, fast, mapping, nerf, compact, reflection, gaussian splatting, ray tracing, shadow  
- **[Inter-Reflective Gaussian Splatting for Robust and Efficient Inverse Rendering](https://arxiv.org/abs/2607.22780v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22780v1.pdf)  
  Keywords: efficient, ar, face, relighting, reflection, gaussian splatting, ray tracing, illumination, lighting  
- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806v1)**  
  Authors: Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15806v1.pdf)  
  Keywords: high-fidelity, face, 3d gaussian, ar, motion, dynamic, reflection, geometry, gaussian splatting, ray tracing, human  

### Relighting

- **[Gaussian Splatting with Reflections Guided by What is Seen](https://arxiv.org/abs/2610.13757v1)**  
  Authors: Yiming Liang, Tianyu Xiao, Hiroshi Ishikawa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13757v1.pdf)  
  Keywords: ar, 3d gaussian, nerf, reflection, gaussian splatting  
- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: efficient, head, ar, 3d gaussian, gaussian splatting, ray tracing, lighting  
- **[OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs](https://arxiv.org/abs/2610.12461v1)**  
  Authors: You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12461v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ouroworld.userwei.com)  
  Keywords: 4d, ar, 3d gaussian, motion, dynamic, deformation, gaussian splatting, illumination  
- **[PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572v1)**  
  Authors: Kota Shimomura, Sungho Moon, Tsubasa Hirakawa, Takayoshi Yamashita, Sunghoon Im, Hironobu Fujiyoshi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11572v1.pdf)  
  Keywords: ar, face, 3d gaussian, dynamic, geometry, lightweight, real-time rendering, gaussian splatting, illumination  
- **[3DTexMOR: 3D Gaussian Multi-Object Removal via Texture-Space Inpainting](https://arxiv.org/abs/2610.11198v1)**  
  Authors: Kunxin Guang, Yonghao Zhao, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11198v1.pdf)  
  Keywords: ar, 3d gaussian, nerf, reflection, geometry  
- **[Casual Flash Lighting for Gaussian Splat Inverse Rendering](https://arxiv.org/abs/2610.06035v1)**  
  Authors: Jiamin Xu, Dongheng Wei, Jiarong Zhao, Qi Wang, James Tompkin, Weiwei Xu, Gang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.06035v1.pdf)  
  Keywords: ar, relighting, geometry, illumination, lighting  
- **[VolS-GS: Relightable Gaussian Splatting with Volumetric Subsurface Scattering](https://arxiv.org/abs/2610.04007v2)**  
  Authors: Junyeong Ahn, Jaegul Choo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04007v2.pdf)  
  Keywords: efficient, ar, face, relighting, relightable, gaussian splatting, shadow, lighting  
- **[EvenSplat: Coupled 2D-3D Decomposition for Gaussian Splatting under Exposure and Illumination Variation](https://arxiv.org/abs/2610.01876v1)**  
  Authors: Tongyu Wu, Jacob Edwards, Ziteng Cui, Caigui Jiang, Cheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01876v1.pdf)  
  Keywords: ar, face, 3d gaussian, geometry, gaussian splatting, illumination, shadow, lighting  
- **[EndoPrior-GS: Dynamic Endoscopic Reconstruction with a Joint Texture Prior](https://arxiv.org/abs/2609.37874v1)**  
  Authors: Jiaqi Huang, Shidong Wang, Tong Xin, Kabita Adhikari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiaqi-huang-77.github.io/EndoPrior-GS)  
  Keywords: ar, 3d gaussian, dynamic, nerf, geometry, real-time rendering, gaussian splatting, illumination  
- **[CollisionSplatting: Collision-Aware Motion Planning in 3DGS Scenes with Image-Conditioned Objectives and Adjustable Conservatism](https://arxiv.org/abs/2609.35619v1)**  
  Authors: R. Khorrambakht, Joaquim Ortiz-Haro, Stephan Weiss, Ludovic Righetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35619v1.pdf)  
  Keywords: vr, ar, 3d gaussian, motion, gaussian splatting, lighting  

### SLAM

*Showing the latest 50 out of 75 papers*

- **[Splat2Act: From Captured Scenes to Personalized VLA Manipulation](https://arxiv.org/abs/2610.13945v1)**  
  Authors: Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, Gunjan Chhablani, Muhammad Zubair Irshad, Zsolt Kira  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13945v1.pdf)  
  Keywords: tracking, ar, 3d gaussian, geometry, gaussian splatting, human  
- **[OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception](https://arxiv.org/abs/2610.07569v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07569v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/OpenSplatGraph)  
  Keywords: efficient, high-fidelity, ar, 3d gaussian, mapping, understanding, geometry, semantic, lightweight, gaussian splatting, robotics  
- **[SURGE: Sonar-fUsed Reconstruction and localization via image-gated Graph Estimation](https://arxiv.org/abs/2610.07472v1)**  
  Authors: Mohammed Ibrahim M, Vallabh Deogaonkar, Trung Dong, Jane Shin, Abhilash Somayajula, Xiaomin Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07472v1.pdf)  
  Keywords: ar, localization, understanding, compact, geometry, gaussian splatting  
- **[FOCUS: Fine-Grained Open-Vocabulary Change Detection for Uncertainty-Aware Semi-Static Scenes](https://arxiv.org/abs/2610.05639v1)**  
  Authors: Can Xu, Mingfeng Yuan, Mahan Mohammadi, Steven L. Waslander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05639v1.pdf)  
  Keywords: ar, 3d gaussian, mapping, geometry, semantic  
- **[CellSplat4D: PSF-Aware 4D Gaussian Splatting for Sparse Robotic Live-Cell Imaging](https://arxiv.org/abs/2610.04199v1)**  
  Authors: Yingda Tao, Guoyu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04199v1.pdf)  
  Keywords: 4d, ar, tracking, motion, gaussian splatting  
- **[VoxelSynth3D: Interpretable Volumetric Image-Domain Metal Artifact Reduction with a Paired Synthetic CLINIC-Metal Benchmark](https://arxiv.org/abs/2610.01512v1)**  
  Authors: Amritesh Banerjee, Abdul Basit, Renil Renji Joseph, Nouhaila Innan, Muhammad Shafique  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01512v1.pdf)  
  Keywords: localization, ar, face, 3d gaussian  
- **[Lens Flare Removal and Reconstruction](https://arxiv.org/abs/2609.39527v1)**  
  Authors: Tarun Yenamandra, Jonathon Luiten, Daniel Cremers, Nathan Matsuda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39527v1.pdf)  
  Keywords: localization, ar, gaussian splatting  
- **[DispFlow-GS: Displacement Flow Supervision with Motion Disentangling for Monocular Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2609.36940v1)**  
  Authors: Thai Duy Nguyen, Haitian Zhang, Addison Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36940v1.pdf)  
  Keywords: ar, 3d gaussian, motion, localization, dynamic, geometry, deformation, gaussian splatting  
- **[EviSplat: Preserving Multi-View Evidence in 3D Gaussian Splatting for Open-Vocabulary Segmentation](https://arxiv.org/abs/2609.34853v1)**  
  Authors: Sungho Moon, Kota Shimomura, Junwoo Park, Wonhyeok Choi, Seunghun Lee, Takayoshi Yamashita, Sunghoon Im  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34853v1.pdf)  
  Keywords: ar, 3d gaussian, segmentation, localization, understanding, compact, gaussian splatting  
- **[Reliability-Regulated Trajectory Optimization for Progressive COLMAP-Free 3D Gaussian Splatting](https://arxiv.org/abs/2609.30865v1)**  
  Authors: Zijian Wu, Jinliang Wang, Zidian Lin, Ying Song, Ziqian Lu, Hanjie Ma, Zhen Ye, Mingfeng Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30865v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Zijian1026/RRTO-CF3DGS?style=social)](https://github.com/Zijian1026/RRTO-CF3DGS)  
  Keywords: tracking, ar, 3d gaussian, motion, dynamic, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 97 papers*

- **[Measurable Semantic 3D Gaussian Splatting with Joint Region and Depth Supervision for Interactive Building Inspection](https://arxiv.org/abs/2610.13143v1)**  
  Authors: Yi Zhang, Tian Tan, Ray Kai Leung Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13143v1.pdf)  
  Keywords: ar, face, 3d gaussian, 3d reconstruction, geometry, semantic, gaussian splatting  
- **[PCAsplat: Gaussian Splatting with Local PCA Regularization](https://arxiv.org/abs/2610.11011v1)**  
  Authors: Vitor Matias, Filipe Nascimento, Kiyohiro Nakayama, João Paulo Lima, Márcus Lobo, Gordon Wetzstein, Leonidas Guibas, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11011v1.pdf)  
  Keywords: ar, face, segmentation, 3d reconstruction, nerf, geometry, gaussian splatting  
- **[Post-Training Semantic Lifting for 3D Gaussian Splatting: Separating Detector, Lifting and Representation Error](https://arxiv.org/abs/2610.08756v1)**  
  Authors: Iván Verdugo Guerra, Ezequiel López Rubio, Jorge García González  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.08756v1.pdf)  
  Keywords: ar, semantic, 3d gaussian, gaussian splatting  
- **[View Matters: Keyframe-Guided Text-Driven 3D Gaussian Editing](https://arxiv.org/abs/2610.08179v1)**  
  Authors: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Xuanyu Wang, Feng Lei, Sha Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.08179v1.pdf)  
  Keywords: ar, semantic, 3d gaussian  
- **[OpenSplatGraph: From Dense Semantic Maps to Structured Scene Graphs for Open-Vocabulary Robot Perception](https://arxiv.org/abs/2610.07569v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07569v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/OpenSplatGraph)  
  Keywords: efficient, high-fidelity, ar, 3d gaussian, mapping, understanding, geometry, semantic, lightweight, gaussian splatting, robotics  
- **[SURGE: Sonar-fUsed Reconstruction and localization via image-gated Graph Estimation](https://arxiv.org/abs/2610.07472v1)**  
  Authors: Mohammed Ibrahim M, Vallabh Deogaonkar, Trung Dong, Jane Shin, Abhilash Somayajula, Xiaomin Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07472v1.pdf)  
  Keywords: ar, localization, understanding, compact, geometry, gaussian splatting  
- **[MoonGS: High-quality Representation of the Lunar Surface via Gaussian Splatting Using Robust Depth Features from Image Pairs](https://arxiv.org/abs/2610.07110v1)**  
  Authors: Yun Jiang, Bo Zheng, Yingying Zhang, Xueming Xiao, Tao Hu, Hutao Cui, Zhiguo Meng, Ke Gao, Yang Gao, Meibao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07110v1.pdf) | [![GitHub](https://img.shields.io/github/stars/InRobots/MoonBlender?style=social)](https://github.com/InRobots/MoonBlender)  
  Keywords: head, ar, face, 3d gaussian, 3d reconstruction, nerf, semantic, gaussian splatting  
- **[MaRO-GS: Mask-Robust Object-Centric Gaussian Splatting from Inconsistent Multi-view Masks](https://arxiv.org/abs/2610.06472v1)**  
  Authors: Eunji Kim, Gahyeon Kim, Gianella Cravioto, Dong-hun Lee, Chaewon Moon, Chae-yeong Song, Sang-hyo Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.06472v1.pdf)  
  Keywords: head, ar, segmentation, gaussian splatting  
- **[FOCUS: Fine-Grained Open-Vocabulary Change Detection for Uncertainty-Aware Semi-Static Scenes](https://arxiv.org/abs/2610.05639v1)**  
  Authors: Can Xu, Mingfeng Yuan, Mahan Mohammadi, Steven L. Waslander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05639v1.pdf)  
  Keywords: ar, 3d gaussian, mapping, geometry, semantic  
- **[GS-Codec: A Gaussian-Splatting Bottleneck for Neural Audio Coding](https://arxiv.org/abs/2610.04651v1)**  
  Authors: Ron Aluf, Alon Canfi, Eliya Nachmani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.04651v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ronaluf.github.io/gs-codec)  
  Keywords: ar, compact, semantic, lightweight, gaussian splatting  



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
