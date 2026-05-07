# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-05-07 01:56:28

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

- [3DGS Surveys](#3dgs-surveys) (6 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (104 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (497 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (160 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (202 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (42 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (220 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (20 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (200 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (115 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (15 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (68 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (83 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (120 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[ReefMapGS: Enabling Large-Scale Underwater Reconstruction by Closing the Loop Between Multimodal SLAM and Gaussian Splatting](https://arxiv.org/abs/2604.11992v1)**  
  Authors: Daniel Yang, Jungseok Hong, John J. Leonard, Yogesh Girdhar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11992v1.pdf)  
  Keywords: ar, 3d gaussian, slam, survey, efficient, gaussian splatting, 3d reconstruction, tracking, geometry, motion  
- **[A Survey of Spatial Memory Representations for Efficient Robot Navigation](https://arxiv.org/abs/2604.16482v1)**  
  Authors: Ma. Madecheen S. Pangaliman, Steven S. Sison, Erwin P. Quilloy, Rowel Atienza  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.16482v1.pdf)  
  Keywords: ar, slam, survey, efficient, semantic  
- **[Nevis Digital Twin: Photogrammetry and Immersive Visualization of Historical Sites](https://arxiv.org/abs/2603.20560v1)**  
  Authors: Alex Apffel, Huy Tran, Vuthea Chheang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20560v1.pdf)  
  Keywords: ar, 3d gaussian, survey, vr, gaussian splatting  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awareness](https://arxiv.org/abs/2603.17499v6)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v6.pdf) | [![GitHub](https://img.shields.io/github/stars/UNIC-Lab/Awesome-Radio-Map-Categorized?style=social)](https://github.com/UNIC-Lab/Awesome-Radio-Map-Categorized)  
  Keywords: ar, ray tracing, 3d gaussian, survey, gaussian splatting, mapping  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: ar, 3d gaussian, slam, survey, efficient, localization, gaussian splatting, tracking, mapping, face, motion, dynamic  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: ar, 3d gaussian, survey, gaussian splatting, robotics  

### Acceleration

*Showing the latest 50 out of 104 papers*

- **[ULF-Loc: Unbiased Landmark Feature for Robust Visual Localization with 3D Gaussian Splatting](https://arxiv.org/abs/2605.04730v1)**  
  Authors: Yingdong Gu, Shaocheng Yan, Zhenjun Zhao, Yuan Kou, Jianxin Luo, Pengcheng Shi, Jiayuan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04730v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, localization, gaussian splatting, geometry, efficient rendering  
- **[CoherentRaster: Efficient 3D Gaussian Splatting for Light Field Displays](https://arxiv.org/abs/2605.04509v1)**  
  Authors: Gyujin Sim, Seungjoo Shin, Hosung Jeon, Gwangsoon Lee, Hyon-Gon Choo, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04509v1.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, efficient, acceleration, gaussian splatting, head, mapping  
- **[Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](https://arxiv.org/abs/2605.01736v1)**  
  Authors: Sixian Zhang, Yiyao Wang, Xinhang Song, Keming Zhang, Zijian Xu, Shuqiang Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01736v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sx-zhang/GLMap?style=social)](https://github.com/sx-zhang/GLMap)  
  Keywords: ar, 3d gaussian, understanding, fast, efficient, gaussian splatting, compact, mapping, geometry, face, semantic  
- **[Beyond Heuristics: Learnable Density Control for 3D Gaussian Splatting](https://arxiv.org/abs/2605.00408v1)**  
  Authors: Zhenhua Ning, Xin Li, Jun Yu, Guangming Lu, Yaowei Wang, Wenjie Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00408v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AaronNZH/LeGS?style=social)](https://github.com/AaronNZH/LeGS)  
  Keywords: ar, 3d gaussian, real-time rendering, gaussian splatting, nerf  
- **[Stop Holding Your Breath: CT-Informed Gaussian Splatting for Dynamic Bronchoscopy](https://arxiv.org/abs/2604.28179v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Aarav Mehta, Xinqi Xiong, Raúl San José Estépar, Ron Alterovitz, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28179v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/RESPIRE)  
  Keywords: ar, fast, body, gaussian splatting, deformation, localization, geometry, lightweight, motion, dynamic  
- **[Faster 3D Gaussian Splatting Convergence via Structure-Aware Densification](https://arxiv.org/abs/2604.28016v1)**  
  Authors: Linjie Lyu, Ayush Tewari, Jianchun Chen, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28016v1.pdf)  
  Keywords: ar, 3d gaussian, fast, efficient, gaussian splatting  
- **[MesonGS++: Post-training Compression of 3D Gaussian Splatting with Hyperparameter Searching](https://arxiv.org/abs/2604.26799v1)**  
  Authors: Shuzhao Xie, Junchen Ge, Weixiang Zhang, Jiahang Liu, Chen Tang, Yunpeng Bai, Shijia Ge, Jingyan Jiang, Yuzhi Huang, Fengnian Yang, Cong Zhang, Xiaoyi Fan, Zhi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26799v1.pdf) | [![GitHub](https://img.shields.io/github/stars/mmlab-sigs/mesongs_plus?style=social)](https://github.com/mmlab-sigs/mesongs_plus)  
  Keywords: ar, 3d gaussian, real-time rendering, compression, gaussian splatting, geometry  
- **[Point Group Symmetry of Polyhedral Diagrams in Graphic Statics](https://arxiv.org/abs/2604.25695v1)**  
  Authors: Yefan Zhi, Yao Lu, Masoud Akbarzadeh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25695v1.pdf)  
  Keywords: ar, fast, geometry, efficient  
- **[Generalizable 3D Gaussian Splatting enabled Semantic Coding for Real-Time Immersive Video Communications](https://arxiv.org/abs/2604.25330v1)**  
  Authors: Dingxi Yang, Wenqi Guo, Yue Liu, Jungong Han, Zhijin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25330v1.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, compression, gaussian splatting, 3d reconstruction, high-fidelity, semantic, lightweight, human, dynamic  
- **[WildSplatter: Feed-forward 3D Gaussian Splatting with Appearance Control from Unconstrained Images](https://arxiv.org/abs/2604.21182v1)**  
  Authors: Yuki Fujimura, Takahiro Kushida, Kazuya Kitano, Takuya Funatomi, Yasuhiro Mukaigawa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21182v1.pdf)  
  Keywords: ar, 3d gaussian, lighting, illumination, real-time rendering, gaussian splatting  

### Applications

*Showing the latest 50 out of 497 papers*

- **[QuadBox: Accelerating 3D Gaussian Splatting with Geometry-Aware Boxes](https://arxiv.org/abs/2605.04844v1)**  
  Authors: Xinze Li, Bohan Yang, Pengxu Chen, Yiyuan Wang, Hongcheng Luo, Wentao Cheng, Weifeng Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04844v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Powertony102/QuadBox?style=social)](https://github.com/Powertony102/QuadBox)  
  Keywords: ar, 3d gaussian, efficient, gaussian splatting, geometry  
- **[ULF-Loc: Unbiased Landmark Feature for Robust Visual Localization with 3D Gaussian Splatting](https://arxiv.org/abs/2605.04730v1)**  
  Authors: Yingdong Gu, Shaocheng Yan, Zhenjun Zhao, Yuan Kou, Jianxin Luo, Pengcheng Shi, Jiayuan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04730v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, localization, gaussian splatting, geometry, efficient rendering  
- **[Velox: Learning Representations of 4D Geometry and Appearance](https://arxiv.org/abs/2605.04527v1)**  
  Authors: Anagh Malik, Dorian Chan, Xiaoming Zhao, David B. Lindell, Oncel Tuzel, Jen-Hao Rick Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04527v1.pdf)  
  Keywords: ar, 3d gaussian, 4d, tracking, geometry, face, dynamic  
- **[CoherentRaster: Efficient 3D Gaussian Splatting for Light Field Displays](https://arxiv.org/abs/2605.04509v1)**  
  Authors: Gyujin Sim, Seungjoo Shin, Hosung Jeon, Gwangsoon Lee, Hyon-Gon Choo, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04509v1.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, efficient, acceleration, gaussian splatting, head, mapping  
- **[Ilov3Splat: Instance-Level Open-Vocabulary 3D Scene Understanding in Gaussian Splatting](https://arxiv.org/abs/2605.04506v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Sridha Sridharan, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04506v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/Ilov3Splat)  
  Keywords: ar, 3d gaussian, understanding, efficient, gaussian splatting, geometry, robotics, segmentation, semantic  
- **[Ground4D: Spatially-Grounded Feedforward 4D Reconstruction for Unstructured Off-Road Scenes](https://arxiv.org/abs/2605.04435v1)**  
  Authors: Shuo Wang, Jilin Mei, Fuyang Liu, Wenfei Guan, Fanjie Kong, Zhihua Zhao, Shuai Wang, Chen Min, Yu Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04435v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wsnbws/Ground4D?style=social)](https://github.com/wsnbws/Ground4D)  
  Keywords: ar, 4d, efficient, gaussian splatting, geometry, face, autonomous driving, motion, dynamic  
- **[Large-Scale High-Quality 3D Gaussian Head Reconstruction from Multi-View Captures](https://arxiv.org/abs/2605.04035v1)**  
  Authors: Evangelos Ntavelis, Sean Wu, Mohamad Shahbazi, Fabio Maninchedda, Dmitry Kostiaev, Artem Sevastopolsky, Vittorio Megaro, Trevor Phillips, Alejandro Blumentals, Shridhar Ravikumar, Mehak Gupta, Reinhard Knothe, Jeronimo Bayer, Matthias Vestner, Simon Schaefer, Thomas Etterlin, Christian Zimmermann, Mathias Deschler, Peter Kaufmann, Stefan Brugger, Sebastian Martin, Brian Amberg, Tom Runia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04035v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, head, compact, human  
- **[FreeTimeGS++: Secrets of Dynamic Gaussian Splatting and Their Principles](https://arxiv.org/abs/2605.03337v1)**  
  Authors: Lucas Yunkyu Lee, Soonho Kim, Youngwook Kim, Sangmin Kim, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.03337v1.pdf)  
  Keywords: ar, understanding, 4d, gaussian splatting, dynamic  
- **[HumanSplatHMR: Closing the Loop Between Human Mesh Recovery and Gaussian Splatting Avatar](https://arxiv.org/abs/2605.02784v1)**  
  Authors: Yeheng Zong, Pou-Chun Kung, Yike Pan, Seth Isaacson, Yizhou Chen, Ram Vasudevan, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.02784v1.pdf)  
  Keywords: ar, gaussian splatting, deformation, high-fidelity, avatar, geometry, segmentation, human, nerf, motion  
- **[GETA-3DGS: Automatic Joint Structured Pruning and Quantization for 3D Gaussian Splatting](https://arxiv.org/abs/2605.02086v1)**  
  Authors: Baobing Zhang, Wanxin Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.02086v1.pdf)  
  Keywords: ar, 3d gaussian, compression, gaussian splatting, high-fidelity, nerf  

### Avatar Generation

*Showing the latest 50 out of 160 papers*

- **[Velox: Learning Representations of 4D Geometry and Appearance](https://arxiv.org/abs/2605.04527v1)**  
  Authors: Anagh Malik, Dorian Chan, Xiaoming Zhao, David B. Lindell, Oncel Tuzel, Jen-Hao Rick Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04527v1.pdf)  
  Keywords: ar, 3d gaussian, 4d, tracking, geometry, face, dynamic  
- **[CoherentRaster: Efficient 3D Gaussian Splatting for Light Field Displays](https://arxiv.org/abs/2605.04509v1)**  
  Authors: Gyujin Sim, Seungjoo Shin, Hosung Jeon, Gwangsoon Lee, Hyon-Gon Choo, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04509v1.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, efficient, acceleration, gaussian splatting, head, mapping  
- **[Ground4D: Spatially-Grounded Feedforward 4D Reconstruction for Unstructured Off-Road Scenes](https://arxiv.org/abs/2605.04435v1)**  
  Authors: Shuo Wang, Jilin Mei, Fuyang Liu, Wenfei Guan, Fanjie Kong, Zhihua Zhao, Shuai Wang, Chen Min, Yu Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04435v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wsnbws/Ground4D?style=social)](https://github.com/wsnbws/Ground4D)  
  Keywords: ar, 4d, efficient, gaussian splatting, geometry, face, autonomous driving, motion, dynamic  
- **[Large-Scale High-Quality 3D Gaussian Head Reconstruction from Multi-View Captures](https://arxiv.org/abs/2605.04035v1)**  
  Authors: Evangelos Ntavelis, Sean Wu, Mohamad Shahbazi, Fabio Maninchedda, Dmitry Kostiaev, Artem Sevastopolsky, Vittorio Megaro, Trevor Phillips, Alejandro Blumentals, Shridhar Ravikumar, Mehak Gupta, Reinhard Knothe, Jeronimo Bayer, Matthias Vestner, Simon Schaefer, Thomas Etterlin, Christian Zimmermann, Mathias Deschler, Peter Kaufmann, Stefan Brugger, Sebastian Martin, Brian Amberg, Tom Runia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04035v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, head, compact, human  
- **[HumanSplatHMR: Closing the Loop Between Human Mesh Recovery and Gaussian Splatting Avatar](https://arxiv.org/abs/2605.02784v1)**  
  Authors: Yeheng Zong, Pou-Chun Kung, Yike Pan, Seth Isaacson, Yizhou Chen, Ram Vasudevan, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.02784v1.pdf)  
  Keywords: ar, gaussian splatting, deformation, high-fidelity, avatar, geometry, segmentation, human, nerf, motion  
- **[Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](https://arxiv.org/abs/2605.01736v1)**  
  Authors: Sixian Zhang, Yiyao Wang, Xinhang Song, Keming Zhang, Zijian Xu, Shuqiang Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01736v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sx-zhang/GLMap?style=social)](https://github.com/sx-zhang/GLMap)  
  Keywords: ar, 3d gaussian, understanding, fast, efficient, gaussian splatting, compact, mapping, geometry, face, semantic  
- **[2D-SuGaR: Surface-Aware Gaussian Splatting for Geometrically Accurate Mesh Reconstruction](https://arxiv.org/abs/2605.00569v1)**  
  Authors: Prajwal Gupta C. R., Divyam Sheth, Jinjoo Ha, Mirela Ostrek, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00569v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, geometry, face, motion  
- **[GOR-IS: 3D Gaussian Object Removal in the Intrinsic Space](https://arxiv.org/abs/2605.00498v1)**  
  Authors: Yonghao Zhao, Yupeng Gao, Jian Yang, Jin Xie, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00498v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://applezyh.github.io/GOR-IS-project-page/) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://applezyh.github.io/GOR-IS-project-page)  
  Keywords: ar, 3d gaussian, lighting, gaussian splatting, geometry, face, nerf, light transport  
- **[FieryGS: In-the-Wild Fire Synthesis with Physics-Integrated Gaussian Splatting](https://arxiv.org/abs/2605.00177v1)**  
  Authors: Qianfan Shen, Ningxiao Tao, Qiyu Dai, Tianle Chen, Minghan Qin, Yongjie Zhang, Mengyu Chu, Wenzheng Chen, Baoquan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/FieryGS)  
  Keywords: ar, 3d gaussian, efficient, gaussian splatting, high-fidelity, outdoor, geometry, face, dynamic  
- **[Stop Holding Your Breath: CT-Informed Gaussian Splatting for Dynamic Bronchoscopy](https://arxiv.org/abs/2604.28179v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Aarav Mehta, Xinqi Xiong, Raúl San José Estépar, Ron Alterovitz, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28179v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/RESPIRE)  
  Keywords: ar, fast, body, gaussian splatting, deformation, localization, geometry, lightweight, motion, dynamic  

### Dynamic Scene

*Showing the latest 50 out of 202 papers*

- **[Velox: Learning Representations of 4D Geometry and Appearance](https://arxiv.org/abs/2605.04527v1)**  
  Authors: Anagh Malik, Dorian Chan, Xiaoming Zhao, David B. Lindell, Oncel Tuzel, Jen-Hao Rick Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04527v1.pdf)  
  Keywords: ar, 3d gaussian, 4d, tracking, geometry, face, dynamic  
- **[Ground4D: Spatially-Grounded Feedforward 4D Reconstruction for Unstructured Off-Road Scenes](https://arxiv.org/abs/2605.04435v1)**  
  Authors: Shuo Wang, Jilin Mei, Fuyang Liu, Wenfei Guan, Fanjie Kong, Zhihua Zhao, Shuai Wang, Chen Min, Yu Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04435v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wsnbws/Ground4D?style=social)](https://github.com/wsnbws/Ground4D)  
  Keywords: ar, 4d, efficient, gaussian splatting, geometry, face, autonomous driving, motion, dynamic  
- **[FreeTimeGS++: Secrets of Dynamic Gaussian Splatting and Their Principles](https://arxiv.org/abs/2605.03337v1)**  
  Authors: Lucas Yunkyu Lee, Soonho Kim, Youngwook Kim, Sangmin Kim, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.03337v1.pdf)  
  Keywords: ar, understanding, 4d, gaussian splatting, dynamic  
- **[HumanSplatHMR: Closing the Loop Between Human Mesh Recovery and Gaussian Splatting Avatar](https://arxiv.org/abs/2605.02784v1)**  
  Authors: Yeheng Zong, Pou-Chun Kung, Yike Pan, Seth Isaacson, Yizhou Chen, Ram Vasudevan, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.02784v1.pdf)  
  Keywords: ar, gaussian splatting, deformation, high-fidelity, avatar, geometry, segmentation, human, nerf, motion  
- **[From Concept to Capability: Evaluating 3D Gaussian Splatting for Synthetic Scene Editing in Autonomous Driving](https://arxiv.org/abs/2605.01995v1)**  
  Authors: Ali Nouri, Yifei Zhang, Yifan Zhang, Tayssir Bouraffa, Zhennan Fei, Zijian Han, Håkan Sivencrona, Anders Heyden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01995v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, autonomous driving, dynamic  
- **[A Principled Approach for Creating High-fidelity Synthetic Demonstrations for Imitation Learning](https://arxiv.org/abs/2605.01232v1)**  
  Authors: Moniruzzaman Akash, Momotaz Begum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01232v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, high-fidelity, motion, dynamic  
- **[2D-SuGaR: Surface-Aware Gaussian Splatting for Geometrically Accurate Mesh Reconstruction](https://arxiv.org/abs/2605.00569v1)**  
  Authors: Prajwal Gupta C. R., Divyam Sheth, Jinjoo Ha, Mirela Ostrek, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00569v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, geometry, face, motion  
- **[FieryGS: In-the-Wild Fire Synthesis with Physics-Integrated Gaussian Splatting](https://arxiv.org/abs/2605.00177v1)**  
  Authors: Qianfan Shen, Ningxiao Tao, Qiyu Dai, Tianle Chen, Minghan Qin, Yongjie Zhang, Mengyu Chu, Wenzheng Chen, Baoquan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/FieryGS)  
  Keywords: ar, 3d gaussian, efficient, gaussian splatting, high-fidelity, outdoor, geometry, face, dynamic  
- **[Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193v1)**  
  Authors: Vinayak Gupta, Chih-Hao Lin, Shenlong Wang, Anand Bhattad, Jia-Bin Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28193v1.pdf)  
  Keywords: ar, 3d gaussian, lighting, illumination, 3d reconstruction, sparse-view, outdoor, sparse view, semantic, segmentation, dynamic  
- **[Stop Holding Your Breath: CT-Informed Gaussian Splatting for Dynamic Bronchoscopy](https://arxiv.org/abs/2604.28179v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Aarav Mehta, Xinqi Xiong, Raúl San José Estépar, Ron Alterovitz, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28179v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/RESPIRE)  
  Keywords: ar, fast, body, gaussian splatting, deformation, localization, geometry, lightweight, motion, dynamic  

### Few-shot

- **[Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193v1)**  
  Authors: Vinayak Gupta, Chih-Hao Lin, Shenlong Wang, Anand Bhattad, Jia-Bin Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28193v1.pdf)  
  Keywords: ar, 3d gaussian, lighting, illumination, 3d reconstruction, sparse-view, outdoor, sparse view, semantic, segmentation, dynamic  
- **[Residual Gaussian Splatting for Ultra Sparse-View CBCT Reconstruction](https://arxiv.org/abs/2604.27552v1)**  
  Authors: Jian Lin, Jiancheng Fang, Shaoyu Wang, Changan Lai, Yikun Zhang, Yang Chen, Qiegen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27552v1.pdf)  
  Keywords: ar, 3d gaussian, neural rendering, efficient, gaussian splatting, sparse-view  
- **[Sparse-View 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2604.27422v1)**  
  Authors: Wongi Park, Jordan A. James, Myeongseok Nam, Minjae Lee, Soomok Lee, Sang-Hyun Lee, William J. Beksi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27422v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotic-vision-lab.github.io/SaveWildGS)  
  Keywords: ar, 3d gaussian, gaussian splatting, high-fidelity, sparse-view  
- **[Generalizable Human Gaussian Splatting via Multi-view Semantic Consistency](https://arxiv.org/abs/2604.25466v1)**  
  Authors: Jingi Kim, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25466v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, body, gaussian splatting, localization, sparse-view, human, semantic  
- **[Light 'em Up: Enabling Few-Shot Low-Light 3D Gaussian Splatting with Multi-Scale Explicit Retinex Illumination Decoupling](https://arxiv.org/abs/2604.24053v1)**  
  Authors: YuHao Yin, Zongji Wang, Yuanben Zhang, Biqing Li, Jiesong Bai, Junyi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24053v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YhuoyuH/MERID-GS?style=social)](https://github.com/YhuoyuH/MERID-GS)  
  Keywords: ar, reflection, 3d gaussian, illumination, gaussian splatting, head, sparse-view, few-shot, lightweight  
- **[DiffNR: Diffusion-Enhanced Neural Representation Optimization for Sparse-View 3D Tomographic Reconstruction](https://arxiv.org/abs/2604.21518v1)**  
  Authors: Shiyan Su, Ruyi Zha, Danli Shi, Hongdong Li, Xuelian Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21518v1.pdf)  
  Keywords: ar, efficient, 3d gaussian, sparse-view  
- **[GeoRect4D: Geometry-Compatible Generative Rectification for Dynamic Sparse-View 3D Reconstruction](https://arxiv.org/abs/2604.20784v1)**  
  Authors: Zhenlong Wu, Zihan Zheng, Xuanxuan Wang, Qianhe Wang, Hua Yang, Xiaoyun Zhang, Qiang Hu, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20784v1.pdf)  
  Keywords: ar, 4d, 3d reconstruction, high-fidelity, sparse-view, geometry, dynamic  
- **[GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds](https://arxiv.org/abs/2604.20155v1)**  
  Authors: Ao Gao, Jingyu Gong, Xin Tan, Zhizhong Zhang, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20155v1.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, gaussian splatting, sparse-view  
- **[FluSplat: Sparse-View 3D Editing without Test-Time Optimization](https://arxiv.org/abs/2604.20038v1)**  
  Authors: Haitao Huang, Shin-Fang Chng, Huangying Zhan, Qingan Yan, Yi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20038v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, 3d reconstruction, sparse-view, sparse view  
- **[Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation](https://arxiv.org/abs/2604.18468v1)**  
  Authors: Tianshi Cao, Jiawei Ren, Yuxuan Zhang, Jaewoo Seo, Jiahui Huang, Shikhar Solanki, Haotian Zhang, Mingfei Guo, Haithem Turki, Muxingzi Li, Yue Zhu, Sipeng Zhang, Zan Gojcic, Sanja Fidler, Kangxue Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18468v1.pdf)  
  Keywords: ar, 3d gaussian, sparse-view, geometry, autonomous driving  

### Geometry Reconstruction

*Showing the latest 50 out of 220 papers*

- **[QuadBox: Accelerating 3D Gaussian Splatting with Geometry-Aware Boxes](https://arxiv.org/abs/2605.04844v1)**  
  Authors: Xinze Li, Bohan Yang, Pengxu Chen, Yiyuan Wang, Hongcheng Luo, Wentao Cheng, Weifeng Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04844v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Powertony102/QuadBox?style=social)](https://github.com/Powertony102/QuadBox)  
  Keywords: ar, 3d gaussian, efficient, gaussian splatting, geometry  
- **[ULF-Loc: Unbiased Landmark Feature for Robust Visual Localization with 3D Gaussian Splatting](https://arxiv.org/abs/2605.04730v1)**  
  Authors: Yingdong Gu, Shaocheng Yan, Zhenjun Zhao, Yuan Kou, Jianxin Luo, Pengcheng Shi, Jiayuan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04730v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, localization, gaussian splatting, geometry, efficient rendering  
- **[Velox: Learning Representations of 4D Geometry and Appearance](https://arxiv.org/abs/2605.04527v1)**  
  Authors: Anagh Malik, Dorian Chan, Xiaoming Zhao, David B. Lindell, Oncel Tuzel, Jen-Hao Rick Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04527v1.pdf)  
  Keywords: ar, 3d gaussian, 4d, tracking, geometry, face, dynamic  
- **[Ilov3Splat: Instance-Level Open-Vocabulary 3D Scene Understanding in Gaussian Splatting](https://arxiv.org/abs/2605.04506v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Sridha Sridharan, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04506v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/Ilov3Splat)  
  Keywords: ar, 3d gaussian, understanding, efficient, gaussian splatting, geometry, robotics, segmentation, semantic  
- **[Ground4D: Spatially-Grounded Feedforward 4D Reconstruction for Unstructured Off-Road Scenes](https://arxiv.org/abs/2605.04435v1)**  
  Authors: Shuo Wang, Jilin Mei, Fuyang Liu, Wenfei Guan, Fanjie Kong, Zhihua Zhao, Shuai Wang, Chen Min, Yu Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04435v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wsnbws/Ground4D?style=social)](https://github.com/wsnbws/Ground4D)  
  Keywords: ar, 4d, efficient, gaussian splatting, geometry, face, autonomous driving, motion, dynamic  
- **[HumanSplatHMR: Closing the Loop Between Human Mesh Recovery and Gaussian Splatting Avatar](https://arxiv.org/abs/2605.02784v1)**  
  Authors: Yeheng Zong, Pou-Chun Kung, Yike Pan, Seth Isaacson, Yizhou Chen, Ram Vasudevan, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.02784v1.pdf)  
  Keywords: ar, gaussian splatting, deformation, high-fidelity, avatar, geometry, segmentation, human, nerf, motion  
- **[Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](https://arxiv.org/abs/2605.01736v1)**  
  Authors: Sixian Zhang, Yiyao Wang, Xinhang Song, Keming Zhang, Zijian Xu, Shuqiang Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01736v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sx-zhang/GLMap?style=social)](https://github.com/sx-zhang/GLMap)  
  Keywords: ar, 3d gaussian, understanding, fast, efficient, gaussian splatting, compact, mapping, geometry, face, semantic  
- **[2D-SuGaR: Surface-Aware Gaussian Splatting for Geometrically Accurate Mesh Reconstruction](https://arxiv.org/abs/2605.00569v1)**  
  Authors: Prajwal Gupta C. R., Divyam Sheth, Jinjoo Ha, Mirela Ostrek, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00569v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, geometry, face, motion  
- **[GOR-IS: 3D Gaussian Object Removal in the Intrinsic Space](https://arxiv.org/abs/2605.00498v1)**  
  Authors: Yonghao Zhao, Yupeng Gao, Jian Yang, Jin Xie, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00498v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://applezyh.github.io/GOR-IS-project-page/) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://applezyh.github.io/GOR-IS-project-page)  
  Keywords: ar, 3d gaussian, lighting, gaussian splatting, geometry, face, nerf, light transport  
- **[FieryGS: In-the-Wild Fire Synthesis with Physics-Integrated Gaussian Splatting](https://arxiv.org/abs/2605.00177v1)**  
  Authors: Qianfan Shen, Ningxiao Tao, Qiyu Dai, Tianle Chen, Minghan Qin, Yongjie Zhang, Mengyu Chu, Wenzheng Chen, Baoquan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/FieryGS)  
  Keywords: ar, 3d gaussian, efficient, gaussian splatting, high-fidelity, outdoor, geometry, face, dynamic  

### Large Scene

- **[FieryGS: In-the-Wild Fire Synthesis with Physics-Integrated Gaussian Splatting](https://arxiv.org/abs/2605.00177v1)**  
  Authors: Qianfan Shen, Ningxiao Tao, Qiyu Dai, Tianle Chen, Minghan Qin, Yongjie Zhang, Mengyu Chu, Wenzheng Chen, Baoquan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/FieryGS)  
  Keywords: ar, 3d gaussian, efficient, gaussian splatting, high-fidelity, outdoor, geometry, face, dynamic  
- **[Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193v1)**  
  Authors: Vinayak Gupta, Chih-Hao Lin, Shenlong Wang, Anand Bhattad, Jia-Bin Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28193v1.pdf)  
  Keywords: ar, 3d gaussian, lighting, illumination, 3d reconstruction, sparse-view, outdoor, sparse view, semantic, segmentation, dynamic  
- **[EnerGS: Energy-Based Gaussian Splatting with Partial Geometric Priors](https://arxiv.org/abs/2604.26238v1)**  
  Authors: Rui Song, Tianhui Cai, Markus Gross, Yun Zhang, Walter Zimmer, Zhiyu Huang, Olaf Wysocki, Jiaqi Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26238v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, outdoor, geometry  
- **[DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis](https://arxiv.org/abs/2604.13416v1)**  
  Authors: Cheng-You Lu, Yi-Shan Hung, Wei-Ling Chi, Hao-Ping Wang, Charlie Li-Ting Tsai, Yu-Cheng Chang, Yu-Lun Liu, Thomas Do, Chin-Teng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13416v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, outdoor  
- **[RMGS-SLAM: Real-time Multi-sensor Gaussian Splatting SLAM](https://arxiv.org/abs/2604.12942v2)**  
  Authors: Dongen Li, Yi Liu, Junqi Liu, Zewen Sun, Zefan Huang, Shuo Sun, Jiahui Liu, Chengran Yuan, Hongliang Guo, Francis E. H. Tay, Marcelo H. Ang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12942v2.pdf)  
  Keywords: ar, 3d gaussian, slam, localization, gaussian splatting, mapping, outdoor  
- **[GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors](https://arxiv.org/abs/2604.11401v1)**  
  Authors: Qilin Zhang, Jinyu Zhu, Olaf Wysocki, Benjamin Busam, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11401v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Jinyzzz/GS4City?style=social)](https://github.com/Jinyzzz/GS4City)  
  Keywords: ar, urban scene, 3d gaussian, understanding, gaussian splatting, compact, geometry, segmentation, semantic  
- **[Neural Harmonic Textures for High-Quality Primitive Based Neural Reconstruction](https://arxiv.org/abs/2604.01204v2)**  
  Authors: Jorge Condor, Nicolas Moenne-Loccoz, Merlin Nimier-David, Piotr Didyk, Zan Gojcic, Qi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01204v2.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, large scene, semantic  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: ar, understanding, neural rendering, 4d, efficient, gaussian splatting, high-fidelity, large scene, shadow, geometry, motion, dynamic  
- **[Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting](https://arxiv.org/abs/2603.29185v1)**  
  Authors: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29185v1.pdf)  
  Keywords: ar, efficient, localization, gaussian splatting, outdoor  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: ar, 3d gaussian, neural rendering, efficient, gaussian splatting, head, large scene, face  

### Model Compression

*Showing the latest 50 out of 200 papers*

- **[QuadBox: Accelerating 3D Gaussian Splatting with Geometry-Aware Boxes](https://arxiv.org/abs/2605.04844v1)**  
  Authors: Xinze Li, Bohan Yang, Pengxu Chen, Yiyuan Wang, Hongcheng Luo, Wentao Cheng, Weifeng Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04844v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Powertony102/QuadBox?style=social)](https://github.com/Powertony102/QuadBox)  
  Keywords: ar, 3d gaussian, efficient, gaussian splatting, geometry  
- **[ULF-Loc: Unbiased Landmark Feature for Robust Visual Localization with 3D Gaussian Splatting](https://arxiv.org/abs/2605.04730v1)**  
  Authors: Yingdong Gu, Shaocheng Yan, Zhenjun Zhao, Yuan Kou, Jianxin Luo, Pengcheng Shi, Jiayuan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04730v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, localization, gaussian splatting, geometry, efficient rendering  
- **[CoherentRaster: Efficient 3D Gaussian Splatting for Light Field Displays](https://arxiv.org/abs/2605.04509v1)**  
  Authors: Gyujin Sim, Seungjoo Shin, Hosung Jeon, Gwangsoon Lee, Hyon-Gon Choo, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04509v1.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, efficient, acceleration, gaussian splatting, head, mapping  
- **[Ilov3Splat: Instance-Level Open-Vocabulary 3D Scene Understanding in Gaussian Splatting](https://arxiv.org/abs/2605.04506v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Sridha Sridharan, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04506v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/Ilov3Splat)  
  Keywords: ar, 3d gaussian, understanding, efficient, gaussian splatting, geometry, robotics, segmentation, semantic  
- **[Ground4D: Spatially-Grounded Feedforward 4D Reconstruction for Unstructured Off-Road Scenes](https://arxiv.org/abs/2605.04435v1)**  
  Authors: Shuo Wang, Jilin Mei, Fuyang Liu, Wenfei Guan, Fanjie Kong, Zhihua Zhao, Shuai Wang, Chen Min, Yu Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04435v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wsnbws/Ground4D?style=social)](https://github.com/wsnbws/Ground4D)  
  Keywords: ar, 4d, efficient, gaussian splatting, geometry, face, autonomous driving, motion, dynamic  
- **[Large-Scale High-Quality 3D Gaussian Head Reconstruction from Multi-View Captures](https://arxiv.org/abs/2605.04035v1)**  
  Authors: Evangelos Ntavelis, Sean Wu, Mohamad Shahbazi, Fabio Maninchedda, Dmitry Kostiaev, Artem Sevastopolsky, Vittorio Megaro, Trevor Phillips, Alejandro Blumentals, Shridhar Ravikumar, Mehak Gupta, Reinhard Knothe, Jeronimo Bayer, Matthias Vestner, Simon Schaefer, Thomas Etterlin, Christian Zimmermann, Mathias Deschler, Peter Kaufmann, Stefan Brugger, Sebastian Martin, Brian Amberg, Tom Runia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04035v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, head, compact, human  
- **[GETA-3DGS: Automatic Joint Structured Pruning and Quantization for 3D Gaussian Splatting](https://arxiv.org/abs/2605.02086v1)**  
  Authors: Baobing Zhang, Wanxin Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.02086v1.pdf)  
  Keywords: ar, 3d gaussian, compression, gaussian splatting, high-fidelity, nerf  
- **[Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](https://arxiv.org/abs/2605.01736v1)**  
  Authors: Sixian Zhang, Yiyao Wang, Xinhang Song, Keming Zhang, Zijian Xu, Shuqiang Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01736v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sx-zhang/GLMap?style=social)](https://github.com/sx-zhang/GLMap)  
  Keywords: ar, 3d gaussian, understanding, fast, efficient, gaussian splatting, compact, mapping, geometry, face, semantic  
- **[FieryGS: In-the-Wild Fire Synthesis with Physics-Integrated Gaussian Splatting](https://arxiv.org/abs/2605.00177v1)**  
  Authors: Qianfan Shen, Ningxiao Tao, Qiyu Dai, Tianle Chen, Minghan Qin, Yongjie Zhang, Mengyu Chu, Wenzheng Chen, Baoquan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/FieryGS)  
  Keywords: ar, 3d gaussian, efficient, gaussian splatting, high-fidelity, outdoor, geometry, face, dynamic  
- **[Stop Holding Your Breath: CT-Informed Gaussian Splatting for Dynamic Bronchoscopy](https://arxiv.org/abs/2604.28179v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Aarav Mehta, Xinqi Xiong, Raúl San José Estépar, Ron Alterovitz, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28179v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/RESPIRE)  
  Keywords: ar, fast, body, gaussian splatting, deformation, localization, geometry, lightweight, motion, dynamic  

### Quality Enhancement

*Showing the latest 50 out of 115 papers*

- **[HumanSplatHMR: Closing the Loop Between Human Mesh Recovery and Gaussian Splatting Avatar](https://arxiv.org/abs/2605.02784v1)**  
  Authors: Yeheng Zong, Pou-Chun Kung, Yike Pan, Seth Isaacson, Yizhou Chen, Ram Vasudevan, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.02784v1.pdf)  
  Keywords: ar, gaussian splatting, deformation, high-fidelity, avatar, geometry, segmentation, human, nerf, motion  
- **[GETA-3DGS: Automatic Joint Structured Pruning and Quantization for 3D Gaussian Splatting](https://arxiv.org/abs/2605.02086v1)**  
  Authors: Baobing Zhang, Wanxin Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.02086v1.pdf)  
  Keywords: ar, 3d gaussian, compression, gaussian splatting, high-fidelity, nerf  
- **[A Principled Approach for Creating High-fidelity Synthetic Demonstrations for Imitation Learning](https://arxiv.org/abs/2605.01232v1)**  
  Authors: Moniruzzaman Akash, Momotaz Begum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01232v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, high-fidelity, motion, dynamic  
- **[TAIL-Safe: Task-Agnostic Safety Monitoring for Imitation Learning Policies](https://arxiv.org/abs/2605.01195v1)**  
  Authors: Riad Ahmed, Momotaz Begum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01195v1.pdf)  
  Keywords: ar, gaussian splatting, high-fidelity  
- **[FieryGS: In-the-Wild Fire Synthesis with Physics-Integrated Gaussian Splatting](https://arxiv.org/abs/2605.00177v1)**  
  Authors: Qianfan Shen, Ningxiao Tao, Qiyu Dai, Tianle Chen, Minghan Qin, Yongjie Zhang, Mengyu Chu, Wenzheng Chen, Baoquan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/FieryGS)  
  Keywords: ar, 3d gaussian, efficient, gaussian splatting, high-fidelity, outdoor, geometry, face, dynamic  
- **[Sparse-View 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2604.27422v1)**  
  Authors: Wongi Park, Jordan A. James, Myeongseok Nam, Minjae Lee, Soomok Lee, Sang-Hyun Lee, William J. Beksi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27422v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotic-vision-lab.github.io/SaveWildGS)  
  Keywords: ar, 3d gaussian, gaussian splatting, high-fidelity, sparse-view  
- **[GS-Playground: A High-Throughput Photorealistic Simulator for Vision-Informed Robot Learning](https://arxiv.org/abs/2604.25459v1)**  
  Authors: Yufei Jia, Heng Zhang, Ziheng Zhang, Junzhe Wu, Mingrui Yu, Zifan Wang, Dixuan Jiang, Zheng Li, Chenyu Cao, Zhuoyuan Yu, Xun Yang, Haizhou Ge, Yuchi Zhang, Jiayuan Zhang, Zhenbiao Huang, Tianle Liu, Shenyu Chen, Jiacheng Wang, Bin Xie, Xuran Yao, Xiwa Deng, Guangyu Wang, Jinzhi Zhang, Lei Hao, Zhixing Chen, Yuxiang Chen, Anqi Wang, Hongyun Tian, Yiyi Yan, Zhanxiang Cao, Yizhou Jiang, Hanyang Shao, Yue Li, Lu Shi, Bokui Chen, Wei Sui, Hanqing Cui, Yusen Qin, Ruqi Huang, Lei Han, Tiancai Wang, Guyue Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25459v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsplayground.github.io)  
  Keywords: ar, 3d gaussian, efficient, gaussian splatting, head, high-fidelity, motion  
- **[Generalizable 3D Gaussian Splatting enabled Semantic Coding for Real-Time Immersive Video Communications](https://arxiv.org/abs/2604.25330v1)**  
  Authors: Dingxi Yang, Wenqi Guo, Yue Liu, Jungong Han, Zhijin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25330v1.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, compression, gaussian splatting, 3d reconstruction, high-fidelity, semantic, lightweight, human, dynamic  
- **[Multivariate Gaussian NeRF for Wide Field-of-View Ultrasound Reconstruction](https://arxiv.org/abs/2604.24187v1)**  
  Authors: Patris Valera, Magdalena Wysocki, Felix Duelmer, Mohammad Farid Azampour, Sebastian Herz, Stefan Wörz, Nassir Navab  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24187v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, geometry, segmentation, nerf  
- **[You Only Gaussian Once: Controllable 3D Gaussian Splatting for Ultra-Densely Sampled Scenes](https://arxiv.org/abs/2604.21400v2)**  
  Authors: Jinrang Jia, Zhenjia Li, Yifeng Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21400v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jjrcn.github.io/yogo-project-home)  
  Keywords: ar, 3d gaussian, neural rendering, gaussian splatting, high-fidelity  

### Ray Tracing

- **[Power Foam: Unifying Real-Time Differentiable Ray Tracing and Rasterization](https://arxiv.org/abs/2604.24994v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Dor Verbin, Kwang Moo Yi, Anish Prabhu, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24994v1.pdf)  
  Keywords: ar, ray tracing, efficient, geometry, face  
- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138v1)**  
  Authors: Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/viserdex)  
  Keywords: ar, ray tracing, 3d gaussian, lighting, efficient, gaussian splatting, tracking, semantic, robotics, dynamic  
- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: ar, reflection, ray tracing, gaussian splatting, face  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: ar, reflection, 3d gaussian, efficient, ray casting  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: ar, ray tracing, 3d gaussian, slam, efficient, localization, gaussian splatting, tracking, mapping, face, semantic  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: ar, reflection, ray tracing, 3d gaussian, gaussian splatting, relightable, shadow, mapping  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: ar, path tracing, 3d gaussian, real-time rendering, geometry, face  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: ar, 3d gaussian, ray tracing, real-time rendering, fast, efficient, gaussian splatting, high-fidelity, geometry, face, nerf  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awareness](https://arxiv.org/abs/2603.17499v6)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v6.pdf) | [![GitHub](https://img.shields.io/github/stars/UNIC-Lab/Awesome-Radio-Map-Categorized?style=social)](https://github.com/UNIC-Lab/Awesome-Radio-Map-Categorized)  
  Keywords: ar, ray tracing, 3d gaussian, survey, gaussian splatting, mapping  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: ar, 3d gaussian, real-time rendering, efficient, gaussian splatting, high-fidelity, ray marching  

### Relighting

*Showing the latest 50 out of 68 papers*

- **[GOR-IS: 3D Gaussian Object Removal in the Intrinsic Space](https://arxiv.org/abs/2605.00498v1)**  
  Authors: Yonghao Zhao, Yupeng Gao, Jian Yang, Jin Xie, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00498v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://applezyh.github.io/GOR-IS-project-page/) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://applezyh.github.io/GOR-IS-project-page)  
  Keywords: ar, 3d gaussian, lighting, gaussian splatting, geometry, face, nerf, light transport  
- **[Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193v1)**  
  Authors: Vinayak Gupta, Chih-Hao Lin, Shenlong Wang, Anand Bhattad, Jia-Bin Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28193v1.pdf)  
  Keywords: ar, 3d gaussian, lighting, illumination, 3d reconstruction, sparse-view, outdoor, sparse view, semantic, segmentation, dynamic  
- **[Color-Encoded Illumination for High-Speed Volumetric Scene Reconstruction](https://arxiv.org/abs/2604.26920v1)**  
  Authors: David Novikov, Eilon Vaknin, Narek Tumanyan, Mark Sheinin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26920v1.pdf)  
  Keywords: ar, illumination, gaussian splatting, motion, dynamic  
- **[Light 'em Up: Enabling Few-Shot Low-Light 3D Gaussian Splatting with Multi-Scale Explicit Retinex Illumination Decoupling](https://arxiv.org/abs/2604.24053v1)**  
  Authors: YuHao Yin, Zongji Wang, Yuanben Zhang, Biqing Li, Jiesong Bai, Junyi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24053v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YhuoyuH/MERID-GS?style=social)](https://github.com/YhuoyuH/MERID-GS)  
  Keywords: ar, reflection, 3d gaussian, illumination, gaussian splatting, head, sparse-view, few-shot, lightweight  
- **[Bringing a Personal Point of View: Evaluating Dynamic 3D Gaussian Splatting for Egocentric Scene Reconstruction](https://arxiv.org/abs/2604.23803v1)**  
  Authors: Jan Warchocki, Xi Wang, Jonas Kulhanek, Jan van Gemert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23803v1.pdf)  
  Keywords: ar, 3d gaussian, lighting, 4d, efficient, gaussian splatting, 3d reconstruction, robotics, human, motion, dynamic  
- **[GS-DOT: Gaussian splatting-based image reconstruction for diffuse optical tomography](https://arxiv.org/abs/2604.23675v1)**  
  Authors: Jingjing Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23675v1.pdf)  
  Keywords: ar, efficient, localization, gaussian splatting, light transport  
- **[WildSplatter: Feed-forward 3D Gaussian Splatting with Appearance Control from Unconstrained Images](https://arxiv.org/abs/2604.21182v1)**  
  Authors: Yuki Fujimura, Takahiro Kushida, Kazuya Kitano, Takuya Funatomi, Yasuhiro Mukaigawa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21182v1.pdf)  
  Keywords: ar, 3d gaussian, lighting, illumination, real-time rendering, gaussian splatting  
- **[FurnSet: Exploiting Repeats for 3D Scene Reconstruction](https://arxiv.org/abs/2604.20093v1)**  
  Authors: Paul Dobre, Xin Wang, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20093v1.pdf)  
  Keywords: ar, lighting, geometry  
- **[BALTIC: A Benchmark and Cross-Domain Strategy for 3D Reconstruction Across Air and Underwater Domains Under Varying Illumination](https://arxiv.org/abs/2604.19133v2)**  
  Authors: Michele Grimaldi, David Nakath, Oscar Pizarro, Jonatan Scharff Willners, Ignacio Carlucho, Yvan R. Petillot  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19133v2.pdf)  
  Keywords: ar, illumination, 3d gaussian, lighting, gaussian splatting, 3d reconstruction, geometry, motion  
- **[E3VS-Bench: A Benchmark for Viewpoint-Dependent Active Perception in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2604.17969v2)**  
  Authors: Koya Sakamoto, Taiki Miyanishi, Daichi Azuma, Shuhei Kurita, Shu Morikuni, Naoya Chiba, Motoaki Kawanabe, Yusuke Iwasawa, Yutaka Matsuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17969v2.pdf)  
  Keywords: ar, 3d gaussian, lighting, gaussian splatting, high-fidelity, human, motion  

### SLAM

*Showing the latest 50 out of 83 papers*

- **[ULF-Loc: Unbiased Landmark Feature for Robust Visual Localization with 3D Gaussian Splatting](https://arxiv.org/abs/2605.04730v1)**  
  Authors: Yingdong Gu, Shaocheng Yan, Zhenjun Zhao, Yuan Kou, Jianxin Luo, Pengcheng Shi, Jiayuan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04730v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, localization, gaussian splatting, geometry, efficient rendering  
- **[Velox: Learning Representations of 4D Geometry and Appearance](https://arxiv.org/abs/2605.04527v1)**  
  Authors: Anagh Malik, Dorian Chan, Xiaoming Zhao, David B. Lindell, Oncel Tuzel, Jen-Hao Rick Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04527v1.pdf)  
  Keywords: ar, 3d gaussian, 4d, tracking, geometry, face, dynamic  
- **[CoherentRaster: Efficient 3D Gaussian Splatting for Light Field Displays](https://arxiv.org/abs/2605.04509v1)**  
  Authors: Gyujin Sim, Seungjoo Shin, Hosung Jeon, Gwangsoon Lee, Hyon-Gon Choo, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04509v1.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, efficient, acceleration, gaussian splatting, head, mapping  
- **[Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](https://arxiv.org/abs/2605.01736v1)**  
  Authors: Sixian Zhang, Yiyao Wang, Xinhang Song, Keming Zhang, Zijian Xu, Shuqiang Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01736v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sx-zhang/GLMap?style=social)](https://github.com/sx-zhang/GLMap)  
  Keywords: ar, 3d gaussian, understanding, fast, efficient, gaussian splatting, compact, mapping, geometry, face, semantic  
- **[Stop Holding Your Breath: CT-Informed Gaussian Splatting for Dynamic Bronchoscopy](https://arxiv.org/abs/2604.28179v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Aarav Mehta, Xinqi Xiong, Raúl San José Estépar, Ron Alterovitz, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28179v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/RESPIRE)  
  Keywords: ar, fast, body, gaussian splatting, deformation, localization, geometry, lightweight, motion, dynamic  
- **[FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115v1)**  
  Authors: Zeyu Jiang, Changqing Zhou, Xingxing Zuo, Changhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28115v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://the-masses.github.io/freeocc-web)  
  Keywords: ar, 3d gaussian, slam, geometry, semantic  
- **[Generalizable Human Gaussian Splatting via Multi-view Semantic Consistency](https://arxiv.org/abs/2604.25466v1)**  
  Authors: Jingi Kim, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25466v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, body, gaussian splatting, localization, sparse-view, human, semantic  
- **[GS-DOT: Gaussian splatting-based image reconstruction for diffuse optical tomography](https://arxiv.org/abs/2604.23675v1)**  
  Authors: Jingjing Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23675v1.pdf)  
  Keywords: ar, efficient, localization, gaussian splatting, light transport  
- **[Flow4DGS-SLAM: Optical Flow-Guided 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2604.22339v2)**  
  Authors: Yunsong Wang, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22339v2.pdf)  
  Keywords: ar, 3d gaussian, slam, 4d, efficient, localization, gaussian splatting, tracking, mapping, motion, dynamic  
- **[OT-UVGS: Revisiting UV Mapping for Gaussian Splatting as a Capacity Allocation Problem](https://arxiv.org/abs/2604.19127v1)**  
  Authors: Byunghyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19127v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, compact, mapping, lightweight, nerf  

### Scene Understanding

*Showing the latest 50 out of 120 papers*

- **[Ilov3Splat: Instance-Level Open-Vocabulary 3D Scene Understanding in Gaussian Splatting](https://arxiv.org/abs/2605.04506v1)**  
  Authors: Binh Long Nguyen, Kien Nguyen, Sridha Sridharan, Clinton Fookes, Peyman Moghadam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04506v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csiro-robotics.github.io/Ilov3Splat)  
  Keywords: ar, 3d gaussian, understanding, efficient, gaussian splatting, geometry, robotics, segmentation, semantic  
- **[FreeTimeGS++: Secrets of Dynamic Gaussian Splatting and Their Principles](https://arxiv.org/abs/2605.03337v1)**  
  Authors: Lucas Yunkyu Lee, Soonho Kim, Youngwook Kim, Sangmin Kim, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.03337v1.pdf)  
  Keywords: ar, understanding, 4d, gaussian splatting, dynamic  
- **[HumanSplatHMR: Closing the Loop Between Human Mesh Recovery and Gaussian Splatting Avatar](https://arxiv.org/abs/2605.02784v1)**  
  Authors: Yeheng Zong, Pou-Chun Kung, Yike Pan, Seth Isaacson, Yizhou Chen, Ram Vasudevan, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.02784v1.pdf)  
  Keywords: ar, gaussian splatting, deformation, high-fidelity, avatar, geometry, segmentation, human, nerf, motion  
- **[Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](https://arxiv.org/abs/2605.01736v1)**  
  Authors: Sixian Zhang, Yiyao Wang, Xinhang Song, Keming Zhang, Zijian Xu, Shuqiang Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01736v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sx-zhang/GLMap?style=social)](https://github.com/sx-zhang/GLMap)  
  Keywords: ar, 3d gaussian, understanding, fast, efficient, gaussian splatting, compact, mapping, geometry, face, semantic  
- **[Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193v1)**  
  Authors: Vinayak Gupta, Chih-Hao Lin, Shenlong Wang, Anand Bhattad, Jia-Bin Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28193v1.pdf)  
  Keywords: ar, 3d gaussian, lighting, illumination, 3d reconstruction, sparse-view, outdoor, sparse view, semantic, segmentation, dynamic  
- **[FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115v1)**  
  Authors: Zeyu Jiang, Changqing Zhou, Xingxing Zuo, Changhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28115v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://the-masses.github.io/freeocc-web)  
  Keywords: ar, 3d gaussian, slam, geometry, semantic  
- **[SandSim: Curve-Guided Gaussian Splatting for Reconstructing Sand Painting Processes](https://arxiv.org/abs/2604.27572v1)**  
  Authors: Yilin Wang, Haojie Huang, Chen Li, Yang Li, Changbo Wang, Chenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27572v1.pdf)  
  Keywords: ar, gaussian splatting, dynamic, geometry, semantic  
- **[Semantic Foam: Unifying Spatial and Semantic Scene Decomposition](https://arxiv.org/abs/2604.26262v2)**  
  Authors: Amr Sharafeldin, Shrisudhan Govindarajan, Thomas Walker, Aryan Mikaeili, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26262v2.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, segmentation, human, semantic  
- **[Generalizable Human Gaussian Splatting via Multi-view Semantic Consistency](https://arxiv.org/abs/2604.25466v1)**  
  Authors: Jingi Kim, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25466v1.pdf)  
  Keywords: ar, 3d gaussian, efficient, body, gaussian splatting, localization, sparse-view, human, semantic  
- **[Generalizable 3D Gaussian Splatting enabled Semantic Coding for Real-Time Immersive Video Communications](https://arxiv.org/abs/2604.25330v1)**  
  Authors: Dingxi Yang, Wenqi Guo, Yue Liu, Jungong Han, Zhijin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25330v1.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, compression, gaussian splatting, 3d reconstruction, high-fidelity, semantic, lightweight, human, dynamic  



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