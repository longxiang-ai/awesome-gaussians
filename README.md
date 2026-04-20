# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-04-20 01:45:41

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
- [Acceleration](#acceleration) (106 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (498 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (166 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (198 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (35 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (215 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (19 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (206 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (127 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (18 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (70 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (78 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (128 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: motion, ar, 3d reconstruction, geometry, efficient, gaussian splatting, survey, tracking, slam, 3d gaussian  
- **[Nevis Digital Twin: Photogrammetry and Immersive Visualization of Historical Sites](https://arxiv.org/abs/2603.20560v1)**  
  Authors: Alex Apffel, Huy Tran, Vuthea Chheang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20560v1.pdf)  
  Keywords: ar, gaussian splatting, vr, survey, 3d gaussian  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: ray tracing, ar, gaussian splatting, survey, mapping, 3d gaussian  
- **[Towards Next-Generation SLAM: A Survey on 3DGS-SLAM Focusing on Performance, Robustness, and Future Directions](https://arxiv.org/abs/2602.04251v1)**  
  Authors: Li Wang, Ruixuan Gong, Yumo Han, Lei Yang, Lu Yang, Ying Li, Bin Xu, Huaping Liu, Rong Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04251v1.pdf)  
  Keywords: face, localization, motion, dynamic, ar, efficient, gaussian splatting, survey, tracking, mapping, slam, 3d gaussian  
- **[Intellectual Property Protection for 3D Gaussian Splatting Assets: A Survey](https://arxiv.org/abs/2602.03878v1)**  
  Authors: Longjie Zhao, Ziming Hong, Jiaxin Huang, Runnan Chen, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03878v1.pdf)  
  Keywords: ar, robotics, gaussian splatting, survey, 3d gaussian  
- **[TreeDGS: Aerial Gaussian Splatting for Distant DBH Measurement](https://arxiv.org/abs/2601.12823v3)**  
  Authors: Belal Shaheen, Minh-Hieu Nguyen, Bach-Thuan Bui, Shubham, Tim Wu, Michael Fairley, Matthew David Zane, Michael Wu, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12823v3.pdf)  
  Keywords: ar, geometry, nerf, efficient, gaussian splatting, survey, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 106 papers*

- **[Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction](https://arxiv.org/abs/2604.15941v1)**  
  Authors: Haato Watanabe, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15941v1.pdf)  
  Keywords: face, fast, ar, 3d reconstruction, nerf, gaussian splatting, real-time rendering, lightweight, 3d gaussian  
- **[CLOTH-HUGS: Cloth Aware Human Gaussian Splatting](https://arxiv.org/abs/2604.15875v1)**  
  Authors: Sadia Mubashshira, Nazanin Amini, Kevin Desai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15875v1.pdf)  
  Keywords: body, human, dynamic, ar, deformation, real-time rendering, gaussian splatting, neural rendering  
- **[Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2604.15862v1)**  
  Authors: Yijia Guo, Wenkai Huang, Tong Hu, Gaolei Li, Yang Li, Yuxin Hong, Liwen Hu, Xitong Ling, Jianhua Li, Shengbo Chen, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15862v1.pdf)  
  Keywords: dynamic, fast, ar, 3d reconstruction, efficient, 4d, gaussian splatting, mapping, 3d gaussian  
- **[GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens](https://arxiv.org/abs/2604.15284v2)**  
  Authors: Roni Itkin, Noam Issachar, Yehonatan Keypur, Xingyu Chen, Anpei Chen, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15284v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://r-itk.github.io/globalsplat)  
  Keywords: fast, ar, compact, geometry, efficient, gaussian splatting, 3d gaussian  
- **[Rethinking Image-to-3D Generation with Sparse Queries: Efficiency, Capacity, and Input-View Bias](https://arxiv.org/abs/2604.13905v1)**  
  Authors: Zhiyuan Xu, Jiuming Liu, Yuxin Chen, Masayoshi Tomizuka, Chenfeng Xu, Chensheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13905v1.pdf)  
  Keywords: fast, ar, compact, geometry, efficient, 3d gaussian  
- **[Any3DAvatar: Fast and High-Quality Full-Head 3D Avatar Reconstruction from Single Portrait Image](https://arxiv.org/abs/2604.13856v1)**  
  Authors: Yujie Gao, Yao Xiao, Xiangnan Zhu, Ya Li, Yiyi Zhang, Liqing Zhang, Jianfu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13856v1.pdf)  
  Keywords: face, avatar, fast, ar, geometry, high-fidelity, 3d gaussian, head  
- **[RobotPan: A 360$^\circ$ Surround-View Robotic Vision System for Embodied Perception](https://arxiv.org/abs/2604.13476v1)**  
  Authors: Jiahao Ma, Qiang Zhang, Peiran Liu, Zeran Su, Pihai Sun, Gang Han, Wen Zhao, Wei Cui, Zhang Zhang, Zhiyuan Xu, Renjing Xu, Jian Tang, Miaomiao Liu, Yijie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13476v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotpan.github.io)  
  Keywords: face, motion, human, dynamic, ar, 3d reconstruction, sparse-view, compact, robotics, real-time rendering, 3d gaussian, head  
- **[ArtifactWorld: Scaling 3D Gaussian Splatting Artifact Restoration via Video Generation Models](https://arxiv.org/abs/2604.12251v1)**  
  Authors: Xinliang Wang, Yifeng Shi, Zhenyu Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12251v1.pdf)  
  Keywords: ar, 3d reconstruction, sparse-view, gaussian splatting, real-time rendering, high-fidelity, 3d gaussian  
- **[VVGT: Visual Volume-Grounded Transformer](https://arxiv.org/abs/2604.12217v1)**  
  Authors: Yuxuan Wang, Qibiao Li, Youcheng Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12217v1.pdf)  
  Keywords: face, fast, ar, geometry, gaussian splatting, vr, 3d gaussian  
- **[Ψ-Map: Panoptic Surface Integrated Mapping Enables Real2Sim Transfer](https://arxiv.org/abs/2604.10982v1)**  
  Authors: Xuan Yu, Yuxuan Xie, Changjian Jiang, Shichao Zhai, Rong Xiong, Yu Zhang, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10982v1.pdf)  
  Keywords: face, ar, efficient, segmentation, semantic, robotics, gaussian splatting, mapping, efficient rendering, 3d gaussian, understanding  

### Applications

*Showing the latest 50 out of 498 papers*

- **[Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction](https://arxiv.org/abs/2604.15941v1)**  
  Authors: Haato Watanabe, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15941v1.pdf)  
  Keywords: face, fast, ar, 3d reconstruction, nerf, gaussian splatting, real-time rendering, lightweight, 3d gaussian  
- **[CLOTH-HUGS: Cloth Aware Human Gaussian Splatting](https://arxiv.org/abs/2604.15875v1)**  
  Authors: Sadia Mubashshira, Nazanin Amini, Kevin Desai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15875v1.pdf)  
  Keywords: body, human, dynamic, ar, deformation, real-time rendering, gaussian splatting, neural rendering  
- **[Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2604.15862v1)**  
  Authors: Yijia Guo, Wenkai Huang, Tong Hu, Gaolei Li, Yang Li, Yuxin Hong, Liwen Hu, Xitong Ling, Jianhua Li, Shengbo Chen, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15862v1.pdf)  
  Keywords: dynamic, fast, ar, 3d reconstruction, efficient, 4d, gaussian splatting, mapping, 3d gaussian  
- **[GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow](https://arxiv.org/abs/2604.15612v1)**  
  Authors: Dong-Uk Seo, Jinwoo Jeon, Eungchang Mason Lee, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15612v1.pdf) | [![GitHub](https://img.shields.io/github/stars/url-kaist/gaussianflow-slam?style=social)](https://github.com/url-kaist/gaussianflow-slam)  
  Keywords: motion, ar, geometry, gaussian splatting, tracking, mapping, slam  
- **[GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens](https://arxiv.org/abs/2604.15284v2)**  
  Authors: Roni Itkin, Noam Issachar, Yehonatan Keypur, Xingyu Chen, Anpei Chen, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15284v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://r-itk.github.io/globalsplat)  
  Keywords: fast, ar, compact, geometry, efficient, gaussian splatting, 3d gaussian  
- **[TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens](https://arxiv.org/abs/2604.15239v1)**  
  Authors: Jiawei Ren, Michal Jan Tyszkiewicz, Jiahui Huang, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15239v1.pdf)  
  Keywords: dynamic, ar, geometry, efficient, gaussian splatting, 3d gaussian  
- **[4D Radar Gaussian Modeling and Scan Matching with RCS](https://arxiv.org/abs/2604.14868v1)**  
  Authors: Fernando Amodeo, Luis Merino, Fernando Caballero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14868v1.pdf)  
  Keywords: dynamic, ar, 4d, robotics, 3d gaussian  
- **[One-shot Compositional 3D Head Avatars with Deformable Hair](https://arxiv.org/abs/2604.14782v1)**  
  Authors: Yuan Sun, Xuan Wang, WeiLi Zhang, Wenxuan Zhang, Yu Guo, Fei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14782v1.pdf)  
  Keywords: animation, face, motion, avatar, dynamic, ar, geometry, semantic, gaussian splatting, deformation, 3d gaussian, head  
- **[NG-GS: NeRF-Guided 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/2604.14706v1)**  
  Authors: Yi He, Tao Wang, Yi Jin, Congyan Lang, Yidong Li, Haibin Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14706v1.pdf) | [![GitHub](https://img.shields.io/github/stars/BJTU-KD3D/NG-GS?style=social)](https://github.com/BJTU-KD3D/NG-GS)  
  Keywords: ar, efficient, nerf, segmentation, gaussian splatting, lightweight, 3d gaussian  
- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268v1)**  
  Authors: Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14268v1.pdf)  
  Keywords: lighting, ar, efficient, gaussian splatting, high-fidelity, 3d gaussian, understanding  

### Avatar Generation

*Showing the latest 50 out of 166 papers*

- **[Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction](https://arxiv.org/abs/2604.15941v1)**  
  Authors: Haato Watanabe, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15941v1.pdf)  
  Keywords: face, fast, ar, 3d reconstruction, nerf, gaussian splatting, real-time rendering, lightweight, 3d gaussian  
- **[CLOTH-HUGS: Cloth Aware Human Gaussian Splatting](https://arxiv.org/abs/2604.15875v1)**  
  Authors: Sadia Mubashshira, Nazanin Amini, Kevin Desai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15875v1.pdf)  
  Keywords: body, human, dynamic, ar, deformation, real-time rendering, gaussian splatting, neural rendering  
- **[One-shot Compositional 3D Head Avatars with Deformable Hair](https://arxiv.org/abs/2604.14782v1)**  
  Authors: Yuan Sun, Xuan Wang, WeiLi Zhang, Wenxuan Zhang, Yu Guo, Fei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14782v1.pdf)  
  Keywords: animation, face, motion, avatar, dynamic, ar, geometry, semantic, gaussian splatting, deformation, 3d gaussian, head  
- **[Any3DAvatar: Fast and High-Quality Full-Head 3D Avatar Reconstruction from Single Portrait Image](https://arxiv.org/abs/2604.13856v1)**  
  Authors: Yujie Gao, Yao Xiao, Xiangnan Zhu, Ya Li, Yiyi Zhang, Liqing Zhang, Jianfu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13856v1.pdf)  
  Keywords: face, avatar, fast, ar, geometry, high-fidelity, 3d gaussian, head  
- **[ClipGStream: Clip-Stream Gaussian Splatting for Any Length and Any Motion Multi-View Dynamic Scene Reconstruction](https://arxiv.org/abs/2604.13746v1)**  
  Authors: Jie Liang, Jiahao Wu, Chao Wang, Jiayu Yang, Xiaoyun Zheng, Kaiqiang Xiong, Zhanke Wang, Jinbo Yan, Feng Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13746v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://liangjie1999.github.io/ClipGStreamWeb)  
  Keywords: motion, dynamic, ar, efficient, gaussian splatting, vr, head  
- **[RobotPan: A 360$^\circ$ Surround-View Robotic Vision System for Embodied Perception](https://arxiv.org/abs/2604.13476v1)**  
  Authors: Jiahao Ma, Qiang Zhang, Peiran Liu, Zeran Su, Pihai Sun, Gang Han, Wen Zhao, Wei Cui, Zhang Zhang, Zhiyuan Xu, Renjing Xu, Jian Tang, Miaomiao Liu, Yijie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13476v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotpan.github.io)  
  Keywords: face, motion, human, dynamic, ar, 3d reconstruction, sparse-view, compact, robotics, real-time rendering, 3d gaussian, head  
- **[SSD-GS: Scattering and Shadow Decomposition for Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2604.13333v1)**  
  Authors: Iris Zheng, Guojun Tang, Alexander Doronin, Paul Teal, Fang-Lue Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13333v1.pdf) | [![GitHub](https://img.shields.io/github/stars/irisfreesiri/SSD-GS?style=social)](https://github.com/irisfreesiri/SSD-GS)  
  Keywords: relightable, face, lighting, illumination, ar, relighting, reflection, gaussian splatting, 3d gaussian, shadow  
- **[3DRealHead: Few-Shot Detailed Head Avatar](https://arxiv.org/abs/2604.13171v1)**  
  Authors: Jalees Nehvi, Timo Bolkart, Thabo Beeler, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13171v1.pdf)  
  Keywords: face, human, avatar, ar, few-shot, 3d gaussian, head  
- **[PatchPoison: Poisoning Multi-View Datasets to Degrade 3D Reconstruction](https://arxiv.org/abs/2604.13153v1)**  
  Authors: Prajas Wadekar, Venkata Sai Pranav Bachina, Kunal Bhosikar, Ankit Gangwal, Charu Sharma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13153v1.pdf)  
  Keywords: motion, human, ar, 3d reconstruction, geometry, nerf, gaussian splatting, lightweight, 3d gaussian  
- **[Habitat-GS: A High-Fidelity Navigation Simulator with Dynamic Gaussian Splatting](https://arxiv.org/abs/2604.12626v1)**  
  Authors: Ziyuan Xia, Jingyi Xu, Chong Cui, Yuanhong Yu, Jiazhao Zhang, Qingsong Yan, Tao Ni, Junbo Chen, Xiaowei Zhou, Hujun Bao, Ruizhen Hu, Sida Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12626v1.pdf)  
  Keywords: avatar, human, dynamic, ar, gaussian splatting, high-fidelity, 3d gaussian  

### Dynamic Scene

*Showing the latest 50 out of 198 papers*

- **[CLOTH-HUGS: Cloth Aware Human Gaussian Splatting](https://arxiv.org/abs/2604.15875v1)**  
  Authors: Sadia Mubashshira, Nazanin Amini, Kevin Desai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15875v1.pdf)  
  Keywords: body, human, dynamic, ar, deformation, real-time rendering, gaussian splatting, neural rendering  
- **[Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2604.15862v1)**  
  Authors: Yijia Guo, Wenkai Huang, Tong Hu, Gaolei Li, Yang Li, Yuxin Hong, Liwen Hu, Xitong Ling, Jianhua Li, Shengbo Chen, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15862v1.pdf)  
  Keywords: dynamic, fast, ar, 3d reconstruction, efficient, 4d, gaussian splatting, mapping, 3d gaussian  
- **[GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow](https://arxiv.org/abs/2604.15612v1)**  
  Authors: Dong-Uk Seo, Jinwoo Jeon, Eungchang Mason Lee, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15612v1.pdf) | [![GitHub](https://img.shields.io/github/stars/url-kaist/gaussianflow-slam?style=social)](https://github.com/url-kaist/gaussianflow-slam)  
  Keywords: motion, ar, geometry, gaussian splatting, tracking, mapping, slam  
- **[TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens](https://arxiv.org/abs/2604.15239v1)**  
  Authors: Jiawei Ren, Michal Jan Tyszkiewicz, Jiahui Huang, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15239v1.pdf)  
  Keywords: dynamic, ar, geometry, efficient, gaussian splatting, 3d gaussian  
- **[4D Radar Gaussian Modeling and Scan Matching with RCS](https://arxiv.org/abs/2604.14868v1)**  
  Authors: Fernando Amodeo, Luis Merino, Fernando Caballero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14868v1.pdf)  
  Keywords: dynamic, ar, 4d, robotics, 3d gaussian  
- **[One-shot Compositional 3D Head Avatars with Deformable Hair](https://arxiv.org/abs/2604.14782v1)**  
  Authors: Yuan Sun, Xuan Wang, WeiLi Zhang, Wenxuan Zhang, Yu Guo, Fei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14782v1.pdf)  
  Keywords: animation, face, motion, avatar, dynamic, ar, geometry, semantic, gaussian splatting, deformation, 3d gaussian, head  
- **[ClipGStream: Clip-Stream Gaussian Splatting for Any Length and Any Motion Multi-View Dynamic Scene Reconstruction](https://arxiv.org/abs/2604.13746v1)**  
  Authors: Jie Liang, Jiahao Wu, Chao Wang, Jiayu Yang, Xiaoyun Zheng, Kaiqiang Xiong, Zhanke Wang, Jinbo Yan, Feng Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13746v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://liangjie1999.github.io/ClipGStreamWeb)  
  Keywords: motion, dynamic, ar, efficient, gaussian splatting, vr, head  
- **[RobotPan: A 360$^\circ$ Surround-View Robotic Vision System for Embodied Perception](https://arxiv.org/abs/2604.13476v1)**  
  Authors: Jiahao Ma, Qiang Zhang, Peiran Liu, Zeran Su, Pihai Sun, Gang Han, Wen Zhao, Wei Cui, Zhang Zhang, Zhiyuan Xu, Renjing Xu, Jian Tang, Miaomiao Liu, Yijie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13476v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotpan.github.io)  
  Keywords: face, motion, human, dynamic, ar, 3d reconstruction, sparse-view, compact, robotics, real-time rendering, 3d gaussian, head  
- **[PatchPoison: Poisoning Multi-View Datasets to Degrade 3D Reconstruction](https://arxiv.org/abs/2604.13153v1)**  
  Authors: Prajas Wadekar, Venkata Sai Pranav Bachina, Kunal Bhosikar, Ankit Gangwal, Charu Sharma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13153v1.pdf)  
  Keywords: motion, human, ar, 3d reconstruction, geometry, nerf, gaussian splatting, lightweight, 3d gaussian  
- **[GGD-SLAM: Monocular 3DGS SLAM Powered by Generalizable Motion Model for Dynamic Environments](https://arxiv.org/abs/2604.12837v1)**  
  Authors: Yi Liu, Haoxuan Xu, Hongbo Duan, Keyu Fan, Zhengyang Zhang, Peiyu Zhuang, Pengting Luo, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12837v1.pdf)  
  Keywords: localization, motion, dynamic, ar, semantic, gaussian splatting, mapping, high-fidelity, slam, 3d gaussian  

### Few-shot

- **[RobotPan: A 360$^\circ$ Surround-View Robotic Vision System for Embodied Perception](https://arxiv.org/abs/2604.13476v1)**  
  Authors: Jiahao Ma, Qiang Zhang, Peiran Liu, Zeran Su, Pihai Sun, Gang Han, Wen Zhao, Wei Cui, Zhang Zhang, Zhiyuan Xu, Renjing Xu, Jian Tang, Miaomiao Liu, Yijie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13476v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotpan.github.io)  
  Keywords: face, motion, human, dynamic, ar, 3d reconstruction, sparse-view, compact, robotics, real-time rendering, 3d gaussian, head  
- **[3DRealHead: Few-Shot Detailed Head Avatar](https://arxiv.org/abs/2604.13171v1)**  
  Authors: Jalees Nehvi, Timo Bolkart, Thabo Beeler, Justus Thies  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13171v1.pdf)  
  Keywords: face, human, avatar, ar, few-shot, 3d gaussian, head  
- **[ArtifactWorld: Scaling 3D Gaussian Splatting Artifact Restoration via Video Generation Models](https://arxiv.org/abs/2604.12251v1)**  
  Authors: Xinliang Wang, Yifeng Shi, Zhenyu Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12251v1.pdf)  
  Keywords: ar, 3d reconstruction, sparse-view, gaussian splatting, real-time rendering, high-fidelity, 3d gaussian  
- **[Learning 3D Representations for Spatial Intelligence from Unposed Multi-View Images](https://arxiv.org/abs/2604.10573v1)**  
  Authors: Bo Zhou, Qiuxia Lai, Zeren Sun, Xiangbo Shu, Yazhou Yao, Wenguan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10573v1.pdf)  
  Keywords: ar, sparse-view, geometry, semantic, gaussian splatting, understanding, head  
- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370v1)**  
  Authors: Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08370v1.pdf)  
  Keywords: face, ar, sparse-view, geometry, efficient, gaussian splatting, 3d gaussian  
- **[DOC-GS: Dual-Domain Observation and Calibration for Reliable Sparse-View Gaussian Splatting](https://arxiv.org/abs/2604.06739v1)**  
  Authors: Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06739v1.pdf)  
  Keywords: ar, sparse-view, gaussian splatting, 3d gaussian, understanding  
- **[3D Gaussian Splatting for Annular Dark Field Scanning Transmission Electron Microscopy Tomography Reconstruction](https://arxiv.org/abs/2604.04693v1)**  
  Authors: Beiyuan Zhang, Hesong Li, Ruiwen Shao, Ying Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04693v1.pdf)  
  Keywords: ar, 3d reconstruction, sparse-view, efficient, gaussian splatting, high-fidelity, 3d gaussian  
- **[PR-IQA: Partial-Reference Image Quality Assessment for Diffusion-Based Novel View Synthesis](https://arxiv.org/abs/2604.04576v2)**  
  Authors: Inseong Choi, Siwoo Lee, Seung-Hun Nam, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04576v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kakaomacao.github.io/pr-iqa-project-page)  
  Keywords: ar, 3d reconstruction, sparse-view, gaussian splatting, 3d gaussian  
- **[4C4D: 4 Camera 4D Gaussian Splatting](https://arxiv.org/abs/2604.04063v1)**  
  Authors: Junsheng Zhou, Zhifan Yang, Liang Han, Wenyuan Zhang, Kanle Shi, Shenkun Xu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04063v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://junshengzhou.github.io/4C4D)  
  Keywords: dynamic, ar, sparse-view, geometry, 4d, gaussian splatting, high-fidelity  
- **[Rendering Multi-Human and Multi-Object with 3D Gaussian Splatting](https://arxiv.org/abs/2604.02996v2)**  
  Authors: Weiquan Wang, Jun Xiao, Feifei Shao, Yi Yang, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02996v2.pdf)  
  Keywords: human, dynamic, ar, sparse-view, robotics, gaussian splatting, vr, high-fidelity, 3d gaussian  

### Geometry Reconstruction

*Showing the latest 50 out of 215 papers*

- **[Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction](https://arxiv.org/abs/2604.15941v1)**  
  Authors: Haato Watanabe, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15941v1.pdf)  
  Keywords: face, fast, ar, 3d reconstruction, nerf, gaussian splatting, real-time rendering, lightweight, 3d gaussian  
- **[Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2604.15862v1)**  
  Authors: Yijia Guo, Wenkai Huang, Tong Hu, Gaolei Li, Yang Li, Yuxin Hong, Liwen Hu, Xitong Ling, Jianhua Li, Shengbo Chen, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15862v1.pdf)  
  Keywords: dynamic, fast, ar, 3d reconstruction, efficient, 4d, gaussian splatting, mapping, 3d gaussian  
- **[GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow](https://arxiv.org/abs/2604.15612v1)**  
  Authors: Dong-Uk Seo, Jinwoo Jeon, Eungchang Mason Lee, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15612v1.pdf) | [![GitHub](https://img.shields.io/github/stars/url-kaist/gaussianflow-slam?style=social)](https://github.com/url-kaist/gaussianflow-slam)  
  Keywords: motion, ar, geometry, gaussian splatting, tracking, mapping, slam  
- **[GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens](https://arxiv.org/abs/2604.15284v2)**  
  Authors: Roni Itkin, Noam Issachar, Yehonatan Keypur, Xingyu Chen, Anpei Chen, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15284v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://r-itk.github.io/globalsplat)  
  Keywords: fast, ar, compact, geometry, efficient, gaussian splatting, 3d gaussian  
- **[TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens](https://arxiv.org/abs/2604.15239v1)**  
  Authors: Jiawei Ren, Michal Jan Tyszkiewicz, Jiahui Huang, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15239v1.pdf)  
  Keywords: dynamic, ar, geometry, efficient, gaussian splatting, 3d gaussian  
- **[One-shot Compositional 3D Head Avatars with Deformable Hair](https://arxiv.org/abs/2604.14782v1)**  
  Authors: Yuan Sun, Xuan Wang, WeiLi Zhang, Wenxuan Zhang, Yu Guo, Fei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14782v1.pdf)  
  Keywords: animation, face, motion, avatar, dynamic, ar, geometry, semantic, gaussian splatting, deformation, 3d gaussian, head  
- **[Rethinking Image-to-3D Generation with Sparse Queries: Efficiency, Capacity, and Input-View Bias](https://arxiv.org/abs/2604.13905v1)**  
  Authors: Zhiyuan Xu, Jiuming Liu, Yuxin Chen, Masayoshi Tomizuka, Chenfeng Xu, Chensheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13905v1.pdf)  
  Keywords: fast, ar, compact, geometry, efficient, 3d gaussian  
- **[Any3DAvatar: Fast and High-Quality Full-Head 3D Avatar Reconstruction from Single Portrait Image](https://arxiv.org/abs/2604.13856v1)**  
  Authors: Yujie Gao, Yao Xiao, Xiangnan Zhu, Ya Li, Yiyi Zhang, Liqing Zhang, Jianfu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13856v1.pdf)  
  Keywords: face, avatar, fast, ar, geometry, high-fidelity, 3d gaussian, head  
- **[Dehaze-then-Splat: Generative Dehazing with Physics-Informed 3D Gaussian Splatting for Smoke-Free Novel View Synthesis](https://arxiv.org/abs/2604.13589v1)**  
  Authors: Yuchao Chen, Hanqing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13589v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, ar, gaussian splatting  
- **[RadarSplat-RIO: Indoor Radar-Inertial Odometry with Gaussian Splatting-Based Radar Bundle Adjustment](https://arxiv.org/abs/2604.13492v1)**  
  Authors: Pou-Chun Kung, Yuan Tian, Zhengqin Li, Yue Liu, Eric Whitmire, Wolf Kienzle, Hrvoje Benko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13492v1.pdf)  
  Keywords: lighting, localization, ar, recognition, geometry, gaussian splatting, mapping, slam  

### Large Scene

- **[DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis](https://arxiv.org/abs/2604.13416v1)**  
  Authors: Cheng-You Lu, Yi-Shan Hung, Wei-Ling Chi, Hao-Ping Wang, Charlie Li-Ting Tsai, Yu-Cheng Chang, Yu-Lun Liu, Thomas Do, Chin-Teng Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13416v1.pdf)  
  Keywords: outdoor, 3d gaussian, ar, gaussian splatting  
- **[RMGS-SLAM: Real-time Multi-sensor Gaussian Splatting SLAM](https://arxiv.org/abs/2604.12942v1)**  
  Authors: Dongen Li, Yi Liu, Junqi Liu, Zewen Sun, Zefan Huang, Shuo Sun, Jiahui Liu, Chengran Yuan, Hongliang Guo, Francis E. H. Tay, Marcelo H. Ang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12942v1.pdf)  
  Keywords: localization, ar, outdoor, large scene, gaussian splatting, mapping, slam, 3d gaussian  
- **[GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors](https://arxiv.org/abs/2604.11401v1)**  
  Authors: Qilin Zhang, Jinyu Zhu, Olaf Wysocki, Benjamin Busam, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11401v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Jinyzzz/GS4City?style=social)](https://github.com/Jinyzzz/GS4City)  
  Keywords: urban scene, ar, compact, geometry, segmentation, semantic, gaussian splatting, 3d gaussian, understanding  
- **[Neural Harmonic Textures for High-Quality Primitive Based Neural Reconstruction](https://arxiv.org/abs/2604.01204v2)**  
  Authors: Jorge Condor, Nicolas Moenne-Loccoz, Merlin Nimier-David, Piotr Didyk, Zan Gojcic, Qi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01204v2.pdf)  
  Keywords: ar, large scene, semantic, gaussian splatting, 3d gaussian  
- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion-scale-web)  
  Keywords: motion, dynamic, ar, neural rendering, geometry, large scene, efficient, 4d, gaussian splatting, high-fidelity, shadow, understanding  
- **[Hierarchical Visual Relocalization with Nearest View Synthesis from Feature Gaussian Splatting](https://arxiv.org/abs/2603.29185v1)**  
  Authors: Huaqi Tao, Bingxi Liu, Guangcheng Chen, Fulin Tang, Li He, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29185v1.pdf)  
  Keywords: localization, ar, outdoor, efficient, gaussian splatting  
- **[FilterGS: Traversal-Free Parallel Filtering and Adaptive Shrinking for Large-Scale LoD 3D Gaussian Splatting](https://arxiv.org/abs/2603.23891v1)**  
  Authors: Yixian Wang, Haolin Yu, Jiadong Tang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23891v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xenon-w/FilterGS?style=social)](https://github.com/xenon-w/FilterGS)  
  Keywords: face, ar, efficient, large scene, gaussian splatting, 3d gaussian, neural rendering, head  
- **[M^3: Dense Matching Meets Multi-View Foundation Models for Monocular Gaussian Splatting SLAM](https://arxiv.org/abs/2603.16844v1)**  
  Authors: Kerui Ren, Guanghao Li, Changjian Jiang, Yingxiang Xu, Tao Lu, Linning Xu, Junting Dong, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16844v1.pdf)  
  Keywords: dynamic, ar, outdoor, efficient, gaussian splatting, tracking, slam, head  
- **[Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty](https://arxiv.org/abs/2603.16538v1)**  
  Authors: Mangyu Kong, Jaewon Lee, Seongwon Lee, Euntai Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16538v1.pdf)  
  Keywords: localization, ar, outdoor, geometry, gaussian splatting, 3d gaussian  
- **[EntON: Eigenentropy-Optimized Neighborhood Densification in 3D Gaussian Splatting](https://arxiv.org/abs/2603.06216v1)**  
  Authors: Miriam Jäger, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06216v1.pdf)  
  Keywords: urban scene, face, ar, 3d reconstruction, geometry, gaussian splatting, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 206 papers*

- **[Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction](https://arxiv.org/abs/2604.15941v1)**  
  Authors: Haato Watanabe, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15941v1.pdf)  
  Keywords: face, fast, ar, 3d reconstruction, nerf, gaussian splatting, real-time rendering, lightweight, 3d gaussian  
- **[Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2604.15862v1)**  
  Authors: Yijia Guo, Wenkai Huang, Tong Hu, Gaolei Li, Yang Li, Yuxin Hong, Liwen Hu, Xitong Ling, Jianhua Li, Shengbo Chen, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15862v1.pdf)  
  Keywords: dynamic, fast, ar, 3d reconstruction, efficient, 4d, gaussian splatting, mapping, 3d gaussian  
- **[GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens](https://arxiv.org/abs/2604.15284v2)**  
  Authors: Roni Itkin, Noam Issachar, Yehonatan Keypur, Xingyu Chen, Anpei Chen, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15284v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://r-itk.github.io/globalsplat)  
  Keywords: fast, ar, compact, geometry, efficient, gaussian splatting, 3d gaussian  
- **[TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens](https://arxiv.org/abs/2604.15239v1)**  
  Authors: Jiawei Ren, Michal Jan Tyszkiewicz, Jiahui Huang, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15239v1.pdf)  
  Keywords: dynamic, ar, geometry, efficient, gaussian splatting, 3d gaussian  
- **[NG-GS: NeRF-Guided 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/2604.14706v1)**  
  Authors: Yi He, Tao Wang, Yi Jin, Congyan Lang, Yidong Li, Haibin Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14706v1.pdf) | [![GitHub](https://img.shields.io/github/stars/BJTU-KD3D/NG-GS?style=social)](https://github.com/BJTU-KD3D/NG-GS)  
  Keywords: ar, efficient, nerf, segmentation, gaussian splatting, lightweight, 3d gaussian  
- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268v1)**  
  Authors: Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14268v1.pdf)  
  Keywords: lighting, ar, efficient, gaussian splatting, high-fidelity, 3d gaussian, understanding  
- **[Rethinking Image-to-3D Generation with Sparse Queries: Efficiency, Capacity, and Input-View Bias](https://arxiv.org/abs/2604.13905v1)**  
  Authors: Zhiyuan Xu, Jiuming Liu, Yuxin Chen, Masayoshi Tomizuka, Chenfeng Xu, Chensheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13905v1.pdf)  
  Keywords: fast, ar, compact, geometry, efficient, 3d gaussian  
- **[ClipGStream: Clip-Stream Gaussian Splatting for Any Length and Any Motion Multi-View Dynamic Scene Reconstruction](https://arxiv.org/abs/2604.13746v1)**  
  Authors: Jie Liang, Jiahao Wu, Chao Wang, Jiayu Yang, Xiaoyun Zheng, Kaiqiang Xiong, Zhanke Wang, Jinbo Yan, Feng Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13746v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://liangjie1999.github.io/ClipGStreamWeb)  
  Keywords: motion, dynamic, ar, efficient, gaussian splatting, vr, head  
- **[RobotPan: A 360$^\circ$ Surround-View Robotic Vision System for Embodied Perception](https://arxiv.org/abs/2604.13476v1)**  
  Authors: Jiahao Ma, Qiang Zhang, Peiran Liu, Zeran Su, Pihai Sun, Gang Han, Wen Zhao, Wei Cui, Zhang Zhang, Zhiyuan Xu, Renjing Xu, Jian Tang, Miaomiao Liu, Yijie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13476v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotpan.github.io)  
  Keywords: face, motion, human, dynamic, ar, 3d reconstruction, sparse-view, compact, robotics, real-time rendering, 3d gaussian, head  
- **[MSGS: Multispectral 3D Gaussian Splatting](https://arxiv.org/abs/2604.13340v1)**  
  Authors: Iris Zheng, Guojun Tang, Alexander Doronin, Paul Teal, Fang-Lue Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13340v1.pdf)  
  Keywords: ar, compact, reflection, gaussian splatting, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 127 papers*

- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268v1)**  
  Authors: Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14268v1.pdf)  
  Keywords: lighting, ar, efficient, gaussian splatting, high-fidelity, 3d gaussian, understanding  
- **[Any3DAvatar: Fast and High-Quality Full-Head 3D Avatar Reconstruction from Single Portrait Image](https://arxiv.org/abs/2604.13856v1)**  
  Authors: Yujie Gao, Yao Xiao, Xiangnan Zhu, Ya Li, Yiyi Zhang, Liqing Zhang, Jianfu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13856v1.pdf)  
  Keywords: face, avatar, fast, ar, geometry, high-fidelity, 3d gaussian, head  
- **[GGD-SLAM: Monocular 3DGS SLAM Powered by Generalizable Motion Model for Dynamic Environments](https://arxiv.org/abs/2604.12837v1)**  
  Authors: Yi Liu, Haoxuan Xu, Hongbo Duan, Keyu Fan, Zhengyang Zhang, Peiyu Zhuang, Pengting Luo, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12837v1.pdf)  
  Keywords: localization, motion, dynamic, ar, semantic, gaussian splatting, mapping, high-fidelity, slam, 3d gaussian  
- **[Habitat-GS: A High-Fidelity Navigation Simulator with Dynamic Gaussian Splatting](https://arxiv.org/abs/2604.12626v1)**  
  Authors: Ziyuan Xia, Jingyi Xu, Chong Cui, Yuanhong Yu, Jiazhao Zhang, Qingsong Yan, Tao Ni, Junbo Chen, Xiaowei Zhou, Hujun Bao, Ruizhen Hu, Sida Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12626v1.pdf)  
  Keywords: avatar, human, dynamic, ar, gaussian splatting, high-fidelity, 3d gaussian  
- **[PDF-GS: Progressive Distractor Filtering for Robust 3D Gaussian Splatting](https://arxiv.org/abs/2604.12580v2)**  
  Authors: Kangmin Seo, MinKyu Lee, Tae-Young Kim, ByeongCheol Lee, JoonSeoung An, Jae-Pil Heo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12580v2.pdf) | [![GitHub](https://img.shields.io/github/stars/kangrnin/PDF-GS?style=social)](https://github.com/kangrnin/PDF-GS)  
  Keywords: ar, lightweight, gaussian splatting, high-fidelity, 3d gaussian, head  
- **[ArtifactWorld: Scaling 3D Gaussian Splatting Artifact Restoration via Video Generation Models](https://arxiv.org/abs/2604.12251v1)**  
  Authors: Xinliang Wang, Yifeng Shi, Zhenyu Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12251v1.pdf)  
  Keywords: ar, 3d reconstruction, sparse-view, gaussian splatting, real-time rendering, high-fidelity, 3d gaussian  
- **[Unfolding 3D Gaussian Splatting via Iterative Gaussian Synopsis](https://arxiv.org/abs/2604.11685v1)**  
  Authors: Yuqin Lu, Yang Zhou, Yihua Dai, Guiqing Li, Shengfeng He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11685v1.pdf)  
  Keywords: ar, compact, efficient, gaussian splatting, high-fidelity, 3d gaussian, head  
- **[Fast-SegSim: Real-Time Open-Vocabulary Segmentation for Robotics in Simulation](https://arxiv.org/abs/2604.10951v1)**  
  Authors: Xuan Yu, Yuxuan Xie, Shichao Zhai, Shuhao Ye, Rong Xiong, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10951v1.pdf)  
  Keywords: fast, ar, 3d reconstruction, nerf, segmentation, robotics, gaussian splatting, high-fidelity  
- **[Rein3D: Reinforced 3D Indoor Scene Generation with Panoramic Video Diffusion Models](https://arxiv.org/abs/2604.10578v2)**  
  Authors: Dehui Wang, Congsheng Xu, Rong Wei, Yue Shi, Shoufa Chen, Dingxiang Luo, Tianshuo Yang, Xiaokang Yang, Wei Sui, Yusen Qin, Rui Tang, Yao Mu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10578v2.pdf)  
  Keywords: ar, geometry, gaussian splatting, vr, high-fidelity, 3d gaussian  
- **[PointSplat: Efficient Geometry-Driven Pruning and Transformer Refinement for 3D Gaussian Splatting](https://arxiv.org/abs/2604.09903v1)**  
  Authors: Anh Thuan Tran, Jana Kosecka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.09903v1.pdf)  
  Keywords: ar, geometry, efficient, gaussian splatting, high-fidelity, 3d gaussian  

### Ray Tracing

- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138v1)**  
  Authors: Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/viserdex)  
  Keywords: lighting, ray tracing, dynamic, ar, efficient, semantic, robotics, gaussian splatting, tracking, 3d gaussian  
- **[RT-GS: Gaussian Splatting with Reflection and Transmittance Primitives](https://arxiv.org/abs/2604.00509v1)**  
  Authors: Kunnong Zeng, Chensheng Peng, Yichen Xie, Masayoshi Tomizuka, Cem Yuksel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00509v1.pdf)  
  Keywords: face, ray tracing, ar, reflection, gaussian splatting  
- **[UltraG-Ray: Physics-Based Gaussian Ray Casting for Novel Ultrasound View Synthesis](https://arxiv.org/abs/2603.29022v1)**  
  Authors: Felix Duelmer, Jakob Klaushofer, Magdalena Wysocki, Nassir Navab, Mohammad Farid Azampour  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29022v1.pdf)  
  Keywords: ar, efficient, ray casting, reflection, 3d gaussian  
- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781v1)**  
  Authors: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27781v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lif314/GS3LAM?style=social)](https://github.com/lif314/GS3LAM)  
  Keywords: face, localization, ray tracing, ar, efficient, semantic, gaussian splatting, tracking, mapping, slam, 3d gaussian  
- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637v2)**  
  Authors: Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23637v2.pdf)  
  Keywords: relightable, ray tracing, ar, reflection, gaussian splatting, mapping, 3d gaussian, shadow  
- **[GTSR: Subsurface Scattering Awared 3D Gaussians for Translucent Surface Reconstruction](https://arxiv.org/abs/2603.22036v1)**  
  Authors: Youwen Yuan, Xi Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22036v1.pdf)  
  Keywords: path tracing, face, ar, geometry, real-time rendering, 3d gaussian  
- **[RefracGS: Novel View Synthesis Through Refractive Water Surfaces with 3D Gaussian Ray Tracing](https://arxiv.org/abs/2603.21695v1)**  
  Authors: Yiming Shao, Qiyu Dai, Chong Gao, Guanbin Li, Yeqiang Wang, He Sun, Qiong Zeng, Baoquan Chen, Wenzheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21695v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yimgshao.github.io/refracgs)  
  Keywords: face, ray tracing, fast, ar, geometry, nerf, efficient, gaussian splatting, real-time rendering, high-fidelity, 3d gaussian  
- **[A Tutorial on Learning-Based Radio Map Construction: Data, Paradigms, and Physics-Awarenes](https://arxiv.org/abs/2603.17499v5)**  
  Authors: Xiucheng Wang, Yuhao Pan, Nan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17499v5.pdf)  
  Keywords: ray tracing, ar, gaussian splatting, survey, mapping, 3d gaussian  
- **[IRIS: Intersection-aware Ray-based Implicit Editable Scenes](https://arxiv.org/abs/2603.15368v1)**  
  Authors: Grzegorz Wilczyński, Mikołaj Zieliński, Krzysztof Byrski, Joanna Waczyńska, Dominik Belter, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gwilczynski95/iris?style=social)](https://github.com/gwilczynski95/iris)  
  Keywords: ar, efficient, gaussian splatting, real-time rendering, ray marching, high-fidelity, 3d gaussian  
- **[Spherical-GOF: Geometry-Aware Panoramic Gaussian Opacity Fields for 3D Scene Reconstruction](https://arxiv.org/abs/2603.08503v1)**  
  Authors: Zhe Yang, Guoqiang Zhao, Sheng Wu, Kai Luo, Kailun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08503v1.pdf) | [![GitHub](https://img.shields.io/github/stars/1170632760/Spherical-GOF?style=social)](https://github.com/1170632760/Spherical-GOF)  
  Keywords: fast, ar, geometry, efficient, ray casting, robotics, gaussian splatting, 3d gaussian  

### Relighting

*Showing the latest 50 out of 70 papers*

- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268v1)**  
  Authors: Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14268v1.pdf)  
  Keywords: lighting, ar, efficient, gaussian splatting, high-fidelity, 3d gaussian, understanding  
- **[RadarSplat-RIO: Indoor Radar-Inertial Odometry with Gaussian Splatting-Based Radar Bundle Adjustment](https://arxiv.org/abs/2604.13492v1)**  
  Authors: Pou-Chun Kung, Yuan Tian, Zhengqin Li, Yue Liu, Eric Whitmire, Wolf Kienzle, Hrvoje Benko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13492v1.pdf)  
  Keywords: lighting, localization, ar, recognition, geometry, gaussian splatting, mapping, slam  
- **[MSGS: Multispectral 3D Gaussian Splatting](https://arxiv.org/abs/2604.13340v1)**  
  Authors: Iris Zheng, Guojun Tang, Alexander Doronin, Paul Teal, Fang-Lue Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13340v1.pdf)  
  Keywords: ar, compact, reflection, gaussian splatting, 3d gaussian  
- **[SSD-GS: Scattering and Shadow Decomposition for Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2604.13333v1)**  
  Authors: Iris Zheng, Guojun Tang, Alexander Doronin, Paul Teal, Fang-Lue Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13333v1.pdf) | [![GitHub](https://img.shields.io/github/stars/irisfreesiri/SSD-GS?style=social)](https://github.com/irisfreesiri/SSD-GS)  
  Keywords: relightable, face, lighting, illumination, ar, relighting, reflection, gaussian splatting, 3d gaussian, shadow  
- **[AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation](https://arxiv.org/abs/2604.11674v1)**  
  Authors: Mingyang Li, Haofan Xu, Haowen Sun, Xinzhe Chen, Sihua Ren, Liqi Huang, Xinyang Sui, Chenyang Miao, Qiongjie Cui, Zeyang Liu, Xingyu Chen, Xuguang Lan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11674v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, lighting  
- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138v1)**  
  Authors: Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/viserdex)  
  Keywords: lighting, ray tracing, dynamic, ar, efficient, semantic, robotics, gaussian splatting, tracking, 3d gaussian  
- **[LumiMotion: Improving Gaussian Relighting with Scene Dynamics](https://arxiv.org/abs/2604.10994v1)**  
  Authors: Joanna Kaleta, Piotr Wójcik, Kacper Marzol, Tomasz Trzciński, Kacper Kania, Marek Kowalski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10994v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://joaxkal.github.io/LumiMotion)  
  Keywords: face, lighting, motion, dynamic, illumination, 3d reconstruction, ar, relighting, gaussian splatting, shadow  
- **[Appearance Decomposition Gaussian Splatting for Multi-Traversal Reconstruction](https://arxiv.org/abs/2604.05908v1)**  
  Authors: Yangyi Xiao, Siting Zhu, Baoquan Yang, Tianchen Deng, Yongbo Chen, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05908v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRMVLab/ADM-GS?style=social)](https://github.com/IRMVLab/ADM-GS)  
  Keywords: autonomous driving, face, lighting, illumination, ar, geometry, reflection, gaussian splatting, high-fidelity  
- **[HOIGS: Human-Object Interaction Gaussian Splatting](https://arxiv.org/abs/2604.04016v1)**  
  Authors: Taewoo Kim, Suwoong Yeom, Jaehyun Pyun, Geonho Cha, Dongyoon Wee, Joonsik Nam, Yun-Seong Jeong, Kyeongbo Kong, Suk-Ju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04016v1.pdf)  
  Keywords: lighting, motion, human, dynamic, ar, 4d, gaussian splatting, deformation, high-fidelity  
- **[SpectralSplat: Appearance-Disentangled Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2604.03462v1)**  
  Authors: Quentin Herau, Tianshuo Xu, Depu Meng, Jiezhi Yang, Chensheng Peng, Spencer Sherk, Yihan Hu, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03462v1.pdf)  
  Keywords: autonomous driving, lighting, ar, geometry, relighting, gaussian splatting, 3d gaussian  

### SLAM

*Showing the latest 50 out of 78 papers*

- **[Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2604.15862v1)**  
  Authors: Yijia Guo, Wenkai Huang, Tong Hu, Gaolei Li, Yang Li, Yuxin Hong, Liwen Hu, Xitong Ling, Jianhua Li, Shengbo Chen, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15862v1.pdf)  
  Keywords: dynamic, fast, ar, 3d reconstruction, efficient, 4d, gaussian splatting, mapping, 3d gaussian  
- **[GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow](https://arxiv.org/abs/2604.15612v1)**  
  Authors: Dong-Uk Seo, Jinwoo Jeon, Eungchang Mason Lee, Hyun Myung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15612v1.pdf) | [![GitHub](https://img.shields.io/github/stars/url-kaist/gaussianflow-slam?style=social)](https://github.com/url-kaist/gaussianflow-slam)  
  Keywords: motion, ar, geometry, gaussian splatting, tracking, mapping, slam  
- **[RadarSplat-RIO: Indoor Radar-Inertial Odometry with Gaussian Splatting-Based Radar Bundle Adjustment](https://arxiv.org/abs/2604.13492v1)**  
  Authors: Pou-Chun Kung, Yuan Tian, Zhengqin Li, Yue Liu, Eric Whitmire, Wolf Kienzle, Hrvoje Benko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13492v1.pdf)  
  Keywords: lighting, localization, ar, recognition, geometry, gaussian splatting, mapping, slam  
- **[RMGS-SLAM: Real-time Multi-sensor Gaussian Splatting SLAM](https://arxiv.org/abs/2604.12942v1)**  
  Authors: Dongen Li, Yi Liu, Junqi Liu, Zewen Sun, Zefan Huang, Shuo Sun, Jiahui Liu, Chengran Yuan, Hongliang Guo, Francis E. H. Tay, Marcelo H. Ang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12942v1.pdf)  
  Keywords: localization, ar, outdoor, large scene, gaussian splatting, mapping, slam, 3d gaussian  
- **[GGD-SLAM: Monocular 3DGS SLAM Powered by Generalizable Motion Model for Dynamic Environments](https://arxiv.org/abs/2604.12837v1)**  
  Authors: Yi Liu, Haoxuan Xu, Hongbo Duan, Keyu Fan, Zhengyang Zhang, Peiyu Zhuang, Pengting Luo, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12837v1.pdf)  
  Keywords: localization, motion, dynamic, ar, semantic, gaussian splatting, mapping, high-fidelity, slam, 3d gaussian  
- **[ReefMapGS: Enabling Large-Scale Underwater Reconstruction by Closing the Loop Between Multimodal SLAM and Gaussian Splatting](https://arxiv.org/abs/2604.11992v1)**  
  Authors: Daniel Yang, Jungseok Hong, John J. Leonard, Yogesh Girdhar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11992v1.pdf)  
  Keywords: motion, ar, 3d reconstruction, geometry, efficient, gaussian splatting, survey, tracking, slam, 3d gaussian  
- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138v1)**  
  Authors: Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/viserdex)  
  Keywords: lighting, ray tracing, dynamic, ar, efficient, semantic, robotics, gaussian splatting, tracking, 3d gaussian  
- **[Ψ-Map: Panoptic Surface Integrated Mapping Enables Real2Sim Transfer](https://arxiv.org/abs/2604.10982v1)**  
  Authors: Xuan Yu, Yuxuan Xie, Changjian Jiang, Shichao Zhai, Rong Xiong, Yu Zhang, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10982v1.pdf)  
  Keywords: face, ar, efficient, segmentation, semantic, robotics, gaussian splatting, mapping, efficient rendering, 3d gaussian, understanding  
- **[MonoEM-GS: Monocular Expectation-Maximization Gaussian Splatting SLAM](https://arxiv.org/abs/2604.10593v1)**  
  Authors: Evgenii Kruzhkov, Sven Behnke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10593v1.pdf)  
  Keywords: motion, ar, geometry, segmentation, gaussian splatting, mapping, slam  
- **[BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields](https://arxiv.org/abs/2604.08410v2)**  
  Authors: Fan Yang, Wenrui Chen, Guorun Yan, Ruize Liao, Wanjun Jia, Dongsheng Luo, Jiacheng Lin, Kailun Yang, Zhiyong Li, Yaonan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08410v2.pdf) | [![GitHub](https://img.shields.io/github/stars/PopeyePxx/BLaDA?style=social)](https://github.com/PopeyePxx/BLaDA)  
  Keywords: localization, ar, semantic, gaussian splatting, 3d gaussian, understanding  

### Scene Understanding

*Showing the latest 50 out of 128 papers*

- **[One-shot Compositional 3D Head Avatars with Deformable Hair](https://arxiv.org/abs/2604.14782v1)**  
  Authors: Yuan Sun, Xuan Wang, WeiLi Zhang, Wenxuan Zhang, Yu Guo, Fei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14782v1.pdf)  
  Keywords: animation, face, motion, avatar, dynamic, ar, geometry, semantic, gaussian splatting, deformation, 3d gaussian, head  
- **[NG-GS: NeRF-Guided 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/2604.14706v1)**  
  Authors: Yi He, Tao Wang, Yi Jin, Congyan Lang, Yidong Li, Haibin Ling  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14706v1.pdf) | [![GitHub](https://img.shields.io/github/stars/BJTU-KD3D/NG-GS?style=social)](https://github.com/BJTU-KD3D/NG-GS)  
  Keywords: ar, efficient, nerf, segmentation, gaussian splatting, lightweight, 3d gaussian  
- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268v1)**  
  Authors: Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14268v1.pdf)  
  Keywords: lighting, ar, efficient, gaussian splatting, high-fidelity, 3d gaussian, understanding  
- **[RadarSplat-RIO: Indoor Radar-Inertial Odometry with Gaussian Splatting-Based Radar Bundle Adjustment](https://arxiv.org/abs/2604.13492v1)**  
  Authors: Pou-Chun Kung, Yuan Tian, Zhengqin Li, Yue Liu, Eric Whitmire, Wolf Kienzle, Hrvoje Benko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13492v1.pdf)  
  Keywords: lighting, localization, ar, recognition, geometry, gaussian splatting, mapping, slam  
- **[GGD-SLAM: Monocular 3DGS SLAM Powered by Generalizable Motion Model for Dynamic Environments](https://arxiv.org/abs/2604.12837v1)**  
  Authors: Yi Liu, Haoxuan Xu, Hongbo Duan, Keyu Fan, Zhengyang Zhang, Peiyu Zhuang, Pengting Luo, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12837v1.pdf)  
  Keywords: localization, motion, dynamic, ar, semantic, gaussian splatting, mapping, high-fidelity, slam, 3d gaussian  
- **[AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation](https://arxiv.org/abs/2604.11674v1)**  
  Authors: Mingyang Li, Haofan Xu, Haowen Sun, Xinzhe Chen, Sihua Ren, Liqi Huang, Xinyang Sui, Chenyang Miao, Qiongjie Cui, Zeyang Liu, Xingyu Chen, Xuguang Lan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11674v1.pdf)  
  Keywords: semantic, ar, 3d gaussian, lighting  
- **[GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors](https://arxiv.org/abs/2604.11401v1)**  
  Authors: Qilin Zhang, Jinyu Zhu, Olaf Wysocki, Benjamin Busam, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11401v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Jinyzzz/GS4City?style=social)](https://github.com/Jinyzzz/GS4City)  
  Keywords: urban scene, ar, compact, geometry, segmentation, semantic, gaussian splatting, 3d gaussian, understanding  
- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138v1)**  
  Authors: Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/viserdex)  
  Keywords: lighting, ray tracing, dynamic, ar, efficient, semantic, robotics, gaussian splatting, tracking, 3d gaussian  
- **[Ψ-Map: Panoptic Surface Integrated Mapping Enables Real2Sim Transfer](https://arxiv.org/abs/2604.10982v1)**  
  Authors: Xuan Yu, Yuxuan Xie, Changjian Jiang, Shichao Zhai, Rong Xiong, Yu Zhang, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10982v1.pdf)  
  Keywords: face, ar, efficient, segmentation, semantic, robotics, gaussian splatting, mapping, efficient rendering, 3d gaussian, understanding  
- **[Fast-SegSim: Real-Time Open-Vocabulary Segmentation for Robotics in Simulation](https://arxiv.org/abs/2604.10951v1)**  
  Authors: Xuan Yu, Yuxuan Xie, Shichao Zhai, Shuhao Ye, Rong Xiong, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10951v1.pdf)  
  Keywords: fast, ar, 3d reconstruction, nerf, segmentation, robotics, gaussian splatting, high-fidelity  



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