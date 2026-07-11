# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2026-07-11 01:43:03

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

- [3DGS Surveys](#3dgs-surveys) (3 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (94 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (499 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (170 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (185 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (45 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (217 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (22 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (183 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (118 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (13 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (59 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (76 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (115 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: efficient, 3d gaussian, localization, slam, high-fidelity, ar, mapping, dynamic, tracking, survey  
- **[Recent Advances and Trends in Learning-based 3D Representations](https://arxiv.org/abs/2606.04871v1)**  
  Authors: Adrien Schockaert, Hamid Laga, Hazem Wannous, Vincent Magnier, Guillaume Dufaye, Jean-françois Witz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.04871v1.pdf)  
  Keywords: motion, 3d reconstruction, 3d gaussian, 4d, compact, gaussian splatting, autonomous driving, ar, medical, vr, recognition, neural rendering, survey  
- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137v1)**  
  Authors: Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00137v1.pdf)  
  Keywords: animation, gaussian splatting, ar, mapping, geometry, survey  

### Acceleration

*Showing the latest 50 out of 94 papers*

- **[NoDrift3R: Raymap-Guided Coupling for Drift-Robust Unposed Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2607.07168v1)**  
  Authors: Xiangyu Sun, Liu Liu, Seungkwon Yang, Jingbing Han, Seungtae Nam, Zhizhong Su, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07168v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, gaussian splatting, ar, fast, geometry  
- **[Real-Time LiDAR Gaussian Splatting SLAM](https://arxiv.org/abs/2607.04127v1)**  
  Authors: Seungjun Tak, Yewon Jeon, Jaeik Hwang, SukMin Hwang, Seongbo Ha, Hyeonwoo Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04127v1.pdf)  
  Keywords: gaussian splatting, slam, ar, fast, mapping, face, tracking, geometry  
- **[TemporalGS: Training-Free Plug-and-Play Acceleration for 3D Gaussian Splatting Rendering via Temporal Priors](https://arxiv.org/abs/2607.03390v1)**  
  Authors: Yuhongze Zhou, Zihao Yang, Xinxin Zuo, Juwei Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03390v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, ar, acceleration, fast, high-fidelity, geometry  
- **[Fast 3D Foundation Model Initialized Gaussian Splatting](https://arxiv.org/abs/2607.03209v1)**  
  Authors: Anurag Dalal, Daniel Hagen, Kjell G. Robbersmyr, Kristian Muri Knausgård  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03209v1.pdf)  
  Keywords: motion, 3d gaussian, sparse-view, gaussian splatting, nerf, robotics, ar, vr, fast  
- **[PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation](https://arxiv.org/abs/2607.01938v1)**  
  Authors: Peng Yun, Shouwang Huang, Hao Li, Jinxi Li, Jianan Wang, Bo Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01938v1.pdf)  
  Keywords: 3d gaussian, ar, fast, dynamic, geometry  
- **[PixGS: Pixel-Space Diffusion for Direct 3D Gaussian Splat Generation](https://arxiv.org/abs/2607.01803v2)**  
  Authors: Cao Duy, Phong Nguyen-Ha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01803v2.pdf)  
  Keywords: efficient, compression, 3d gaussian, ar, fast, face, geometry  
- **[The Turning Point of 3D Plant Phenotyping: 3D Foundation Models Enable Minute-to-Second Cross-Crop Reconstruction and Beyond](https://arxiv.org/abs/2607.01753v1)**  
  Authors: Hanyue Jia, Wei Zhou, Wenbo Zhou, Yanan Li, Hao Lu, Tingting Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01753v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, gaussian splatting, ar, semantic, fast, segmentation, geometry  
- **[Online Segment 3D Gaussians via Launching Virtual Drones](https://arxiv.org/abs/2607.01628v1)**  
  Authors: Liwei Liao, Rongjie Wang, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01628v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, real-time rendering, segmentation  
- **[FastBridge: Closing the Model-Based Realization Gap in Safety Filters on 3D Gaussian Splatting for Fast Quadrotor Flight](https://arxiv.org/abs/2607.01200v1)**  
  Authors: Tscholl Dario, Nakka Yashwanth Kumar, Gunter Brian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01200v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, acceleration, fast, dynamic, geometry  
- **[Relation-Centric Open-Vocabulary 3D Gaussian Segmentation](https://arxiv.org/abs/2607.01140v1)**  
  Authors: Eunsung Cha, Hyunjoon Lee, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01140v1.pdf)  
  Keywords: efficient, 3d gaussian, understanding, ar, segmentation, fast  

### Applications

*Showing the latest 50 out of 499 papers*

- **[Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction](https://arxiv.org/abs/2607.08769v1)**  
  Authors: Weijian Chen, Weibo Yao, Yuhang Zhang, Xiaolin Tang, Guo Wang, Weijun Zhang, Xitong Gao, Yihao Chen, Hongde Qin, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08769v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, outdoor, geometry  
- **[Track2Map: Online Deformable SLAM with Motion-Aware Pose Optimization in Robotic Surgery](https://arxiv.org/abs/2607.08408v1)**  
  Authors: Tianyi Song, Sierra Bonilla, Xinwei Ju, Evangelos Mazomenos, Danail Stoyanov, Adam Schmidt, Omid Mohareri, Sophia Bano, Francisco Vasconcelos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08408v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://track2map.github.io)  
  Keywords: motion, deformation, 3d reconstruction, 3d gaussian, gaussian splatting, slam, ar, mapping  
- **[On the Design of Mixture-of-Experts for Dynamic Gaussian Splatting](https://arxiv.org/abs/2607.08250v1)**  
  Authors: In-Hwan Jin, Hyeongju Mun, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08250v1.pdf) | [![GitHub](https://img.shields.io/github/stars/cvsp-lab/MoE-GS-studio?style=social)](https://github.com/cvsp-lab/MoE-GS-studio)  
  Keywords: motion, deformation, 3d gaussian, gaussian splatting, ar, dynamic  
- **[GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM](https://arxiv.org/abs/2607.07452v1)**  
  Authors: Lipu Zhou, Yaoyun Kang, Junxiang Pang, Shengkai Sun, Tingting Bao, Kehan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07452v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, slam, robotics, ar, illumination, mapping, geometry  
- **[PUF: Plug-and-Play Uncertainty-Aware Fusion for Online 3D Scene Graph Generation](https://arxiv.org/abs/2607.07170v1)**  
  Authors: Yi Yang, Myrna Castillo, Bodo Rosenhahn, Michael Ying Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07170v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yyyyangyi/PUF?style=social)](https://github.com/yyyyangyi/PUF)  
  Keywords: understanding, semantic, ar, 3d gaussian  
- **[NoDrift3R: Raymap-Guided Coupling for Drift-Robust Unposed Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2607.07168v1)**  
  Authors: Xiangyu Sun, Liu Liu, Seungkwon Yang, Jingbing Han, Seungtae Nam, Zhizhong Su, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07168v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, gaussian splatting, ar, fast, geometry  
- **[EscFOA: Enhancing Spatial Learning for Visually Impaired Learners via Generative Spatial Audio in 360-Degree Educational Environments](https://arxiv.org/abs/2607.07015v1)**  
  Authors: Ziyu Luo, Xiaowei Dai, Siying Zhu, Xiaoming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07015v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, high-fidelity, geometry  
- **[RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation](https://arxiv.org/abs/2607.06699v1)**  
  Authors: Shujie Zhang, Jingkun Yi, Weipeng Zhong, Zirui Zhou, Yangkun Zhu, Hanqing Wang, Xudong Xu, Weinan Zhang, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06699v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, ar, 3d gaussian  
- **[PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution](https://arxiv.org/abs/2607.06238v1)**  
  Authors: Lihua Wei, Huatong Gao, Jia Gong, Zhiyu Tan, Hao Li, Jun Liu, Zhihua Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06238v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, mapping, dynamic  
- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: efficient, 3d gaussian, localization, slam, high-fidelity, ar, mapping, dynamic, tracking, survey  

### Avatar Generation

*Showing the latest 50 out of 170 papers*

- **[WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images](https://arxiv.org/abs/2607.05347v1)**  
  Authors: Xiyu Zhang, Jingyu Zhuang, Hongjia Zhai, Zizheng Yan, Jinwei Chen, Guofeng Zhang, Qingnan Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05347v1.pdf)  
  Keywords: efficient, 3d reconstruction, 3d gaussian, gaussian splatting, ar, illumination, face, geometry  
- **[GUSH3R: Everyone Everywhere All at Once as Gaussians](https://arxiv.org/abs/2607.05243v1)**  
  Authors: Keito Abe, Kaede Shiohara, Takashi Otonari, Toshihiko Yamasaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05243v1.pdf)  
  Keywords: motion, efficient, 3d reconstruction, 3d gaussian, gaussian splatting, ar, human, dynamic, geometry  
- **[AdaptiveSplat:Texture Aware Controllable 3D Gaussian Allocation for Feed-Forward Reconstruction](https://arxiv.org/abs/2607.04256v1)**  
  Authors: Badrinath Singhal, Srihari K G, Sreehari Iyer, Ankit Dhiman, Venkatesh Babu Radhakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04256v1.pdf)  
  Keywords: ar, head, 3d reconstruction, 3d gaussian  
- **[Real-Time LiDAR Gaussian Splatting SLAM](https://arxiv.org/abs/2607.04127v1)**  
  Authors: Seungjun Tak, Yewon Jeon, Jaeik Hwang, SukMin Hwang, Seongbo Ha, Hyeonwoo Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04127v1.pdf)  
  Keywords: gaussian splatting, slam, ar, fast, mapping, face, tracking, geometry  
- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771v1)**  
  Authors: Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03771v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/VOP-GS)  
  Keywords: efficient, large scene, sparse view, 3d gaussian, gaussian splatting, ar, face, geometry  
- **[Sparse-View Surface Reconstruction using Gaussian Splatting through High-Confidence Depth Propagation with Normal Priors](https://arxiv.org/abs/2607.03765v1)**  
  Authors: Liang Han, Bangcai Wei, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03765v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/DP-GS)  
  Keywords: sparse view, 3d reconstruction, 3d gaussian, sparse-view, gaussian splatting, ar, face, high-fidelity, geometry  
- **[PixGS: Pixel-Space Diffusion for Direct 3D Gaussian Splat Generation](https://arxiv.org/abs/2607.01803v2)**  
  Authors: Cao Duy, Phong Nguyen-Ha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01803v2.pdf)  
  Keywords: efficient, compression, 3d gaussian, ar, fast, face, geometry  
- **[GaussianEmoTalker: Real-Time Emotional Talking Head Synthesis with Audio-Driven and Blendshape-Based 3D Gaussian Splatting](https://arxiv.org/abs/2607.00959v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Yixuan Dong, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00959v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://njust-yang.github.io/GaussianEmoTalker.github.io)  
  Keywords: motion, 3d gaussian, deformation, gaussian splatting, animation, ar, real-time rendering, head, high-fidelity, avatar  
- **[AnchorSplat: Fast and Structure Consistent Detail Synthesis for Gaussian Splatting](https://arxiv.org/abs/2607.01290v2)**  
  Authors: Dexu Zhu, Jiangnan Shao, Xiaofeng Wang, Junxian Duan, Jie Cao, Zheng Zhu, Huaibo Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01290v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, fast, mapping, high-fidelity, head  
- **[Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673v1)**  
  Authors: Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu, Krishna Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00673v1.pdf)  
  Keywords: deformation, 3d gaussian, ar, outdoor, human  

### Dynamic Scene

*Showing the latest 50 out of 185 papers*

- **[Track2Map: Online Deformable SLAM with Motion-Aware Pose Optimization in Robotic Surgery](https://arxiv.org/abs/2607.08408v1)**  
  Authors: Tianyi Song, Sierra Bonilla, Xinwei Ju, Evangelos Mazomenos, Danail Stoyanov, Adam Schmidt, Omid Mohareri, Sophia Bano, Francisco Vasconcelos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08408v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://track2map.github.io)  
  Keywords: motion, deformation, 3d reconstruction, 3d gaussian, gaussian splatting, slam, ar, mapping  
- **[On the Design of Mixture-of-Experts for Dynamic Gaussian Splatting](https://arxiv.org/abs/2607.08250v1)**  
  Authors: In-Hwan Jin, Hyeongju Mun, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08250v1.pdf) | [![GitHub](https://img.shields.io/github/stars/cvsp-lab/MoE-GS-studio?style=social)](https://github.com/cvsp-lab/MoE-GS-studio)  
  Keywords: motion, deformation, 3d gaussian, gaussian splatting, ar, dynamic  
- **[PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution](https://arxiv.org/abs/2607.06238v1)**  
  Authors: Lihua Wei, Huatong Gao, Jia Gong, Zhiyu Tan, Hao Li, Jun Liu, Zhihua Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06238v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, mapping, dynamic  
- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: efficient, 3d gaussian, localization, slam, high-fidelity, ar, mapping, dynamic, tracking, survey  
- **[GUSH3R: Everyone Everywhere All at Once as Gaussians](https://arxiv.org/abs/2607.05243v1)**  
  Authors: Keito Abe, Kaede Shiohara, Takashi Otonari, Toshihiko Yamasaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05243v1.pdf)  
  Keywords: motion, efficient, 3d reconstruction, 3d gaussian, gaussian splatting, ar, human, dynamic, geometry  
- **[DeGenseGS: Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting](https://arxiv.org/abs/2607.04761v1)**  
  Authors: Yimo Wang, Bin Kang, Shuojue Yang, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04761v1.pdf)  
  Keywords: deformation, 4d, gaussian splatting, understanding, ar, semantic, segmentation, dynamic  
- **[PRISM3D: Probabilistic Refinement and Robust Initialization for Physically Consistent Scene Modeling under Extreme Motion Blur](https://arxiv.org/abs/2607.03855v1)**  
  Authors: Gopi Raju Matta, Reddypalli Trisha, Vemunuri Divya Madhuri, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03855v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, ar, tracking, geometry  
- **[TemporalGS: Training-Free Plug-and-Play Acceleration for 3D Gaussian Splatting Rendering via Temporal Priors](https://arxiv.org/abs/2607.03390v1)**  
  Authors: Yuhongze Zhou, Zihao Yang, Xinxin Zuo, Juwei Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03390v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, ar, acceleration, fast, high-fidelity, geometry  
- **[Fast 3D Foundation Model Initialized Gaussian Splatting](https://arxiv.org/abs/2607.03209v1)**  
  Authors: Anurag Dalal, Daniel Hagen, Kjell G. Robbersmyr, Kristian Muri Knausgård  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03209v1.pdf)  
  Keywords: motion, 3d gaussian, sparse-view, gaussian splatting, nerf, robotics, ar, vr, fast  
- **[PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation](https://arxiv.org/abs/2607.01938v1)**  
  Authors: Peng Yun, Shouwang Huang, Hao Li, Jinxi Li, Jianan Wang, Bo Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01938v1.pdf)  
  Keywords: 3d gaussian, ar, fast, dynamic, geometry  

### Few-shot

- **[Rendering-Aware Bayesian 3D Gaussian Splatting with Native Uncertainty and Adaptive Complexity Control](https://arxiv.org/abs/2607.05522v1)**  
  Authors: Gaoxiang Jia, Vikram Appia, Junzhou Huang, Xinlei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05522v1.pdf)  
  Keywords: sparse view, 3d gaussian, gaussian splatting, ar, geometry  
- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771v1)**  
  Authors: Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03771v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/VOP-GS)  
  Keywords: efficient, large scene, sparse view, 3d gaussian, gaussian splatting, ar, face, geometry  
- **[Sparse-View Surface Reconstruction using Gaussian Splatting through High-Confidence Depth Propagation with Normal Priors](https://arxiv.org/abs/2607.03765v1)**  
  Authors: Liang Han, Bangcai Wei, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03765v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/DP-GS)  
  Keywords: sparse view, 3d reconstruction, 3d gaussian, sparse-view, gaussian splatting, ar, face, high-fidelity, geometry  
- **[Fast 3D Foundation Model Initialized Gaussian Splatting](https://arxiv.org/abs/2607.03209v1)**  
  Authors: Anurag Dalal, Daniel Hagen, Kjell G. Robbersmyr, Kristian Muri Knausgård  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03209v1.pdf)  
  Keywords: motion, 3d gaussian, sparse-view, gaussian splatting, nerf, robotics, ar, vr, fast  
- **[Improving Sparse-View 3DGS Generalization via Flat Minima Optimization](https://arxiv.org/abs/2607.00885v1)**  
  Authors: Kangmin Seo, Sangeek Hyun, MinKyu Lee, Jae-Pil Heo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00885v1.pdf)  
  Keywords: efficient, 3d gaussian, lightweight, sparse-view, gaussian splatting, nerf, ar, real-time rendering, fast, neural rendering, dynamic  
- **[AugSplat: Radiance Field-Informed Gaussian Splatting for Sparse-View Settings](https://arxiv.org/abs/2606.31556v1)**  
  Authors: Lorenzo Lazzaroni, Riccardo Bollati, Daniel Barath, Michael Niemeyer, Keisuke Tateno  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31556v1.pdf)  
  Keywords: sparse-view, gaussian splatting, nerf, ar, real-time rendering, geometry  
- **[StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors](https://arxiv.org/abs/2606.30545v2)**  
  Authors: Wenhao Yuan, Yiyuan Ge, Deli Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30545v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://stringerywh00.github.io/StereoGS_project_page)  
  Keywords: 3d gaussian, sparse-view, gaussian splatting, nerf, ar, face, dynamic, head, geometry  
- **[HiReFF: High-Resolution Feedforward Human Reconstruction from Uncalibrated Sparse-View Video](https://arxiv.org/abs/2606.29333v1)**  
  Authors: Yiming Jiang, Hanzhang Tu, Wenfeng Song, Siyou Lin, Liang An, Shuai Li, Aimin Hao, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29333v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://iridescentjiang.github.io/HiReFF)  
  Keywords: efficient, 3d gaussian, sparse-view, ar, vr, human, head  
- **[Occlusion-Robust Multi-Object Decoupling for Physics-Based Robotic Interaction](https://arxiv.org/abs/2606.29303v2)**  
  Authors: Xin Dong, Lihan Zhang, Tianru Dai, Wenfeng Deng, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.29303v2.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, sparse-view, gaussian splatting, ar, segmentation, dynamic, geometry  
- **[StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views](https://arxiv.org/abs/2606.28321v1)**  
  Authors: Jia-Chen Zhao, Beiqi Chen, Xinyang Chen, Guangcong Wang, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.28321v1.pdf) | [![GitHub](https://img.shields.io/github/stars/J-C-Zhao/StructSplat?style=social)](https://github.com/J-C-Zhao/StructSplat) | [![Project](https://img.shields.io/badge/-Project-blue)](https://structsplat.github.io)  
  Keywords: sparse view, 3d gaussian, gaussian splatting, ar, semantic, geometry  

### Geometry Reconstruction

*Showing the latest 50 out of 217 papers*

- **[Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction](https://arxiv.org/abs/2607.08769v1)**  
  Authors: Weijian Chen, Weibo Yao, Yuhang Zhang, Xiaolin Tang, Guo Wang, Weijun Zhang, Xitong Gao, Yihao Chen, Hongde Qin, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08769v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, outdoor, geometry  
- **[Track2Map: Online Deformable SLAM with Motion-Aware Pose Optimization in Robotic Surgery](https://arxiv.org/abs/2607.08408v1)**  
  Authors: Tianyi Song, Sierra Bonilla, Xinwei Ju, Evangelos Mazomenos, Danail Stoyanov, Adam Schmidt, Omid Mohareri, Sophia Bano, Francisco Vasconcelos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08408v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://track2map.github.io)  
  Keywords: motion, deformation, 3d reconstruction, 3d gaussian, gaussian splatting, slam, ar, mapping  
- **[GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM](https://arxiv.org/abs/2607.07452v1)**  
  Authors: Lipu Zhou, Yaoyun Kang, Junxiang Pang, Shengkai Sun, Tingting Bao, Kehan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07452v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, slam, robotics, ar, illumination, mapping, geometry  
- **[NoDrift3R: Raymap-Guided Coupling for Drift-Robust Unposed Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2607.07168v1)**  
  Authors: Xiangyu Sun, Liu Liu, Seungkwon Yang, Jingbing Han, Seungtae Nam, Zhizhong Su, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07168v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, gaussian splatting, ar, fast, geometry  
- **[EscFOA: Enhancing Spatial Learning for Visually Impaired Learners via Generative Spatial Audio in 360-Degree Educational Environments](https://arxiv.org/abs/2607.07015v1)**  
  Authors: Ziyu Luo, Xiaowei Dai, Siying Zhu, Xiaoming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07015v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, high-fidelity, geometry  
- **[GaussFusion: Towards Multimodal 3D Gaussian Pretraining](https://arxiv.org/abs/2607.05906v1)**  
  Authors: Zhixuan You, Jihua Zhu, Yiding Sun, Zihao Guo, Haozhe Cheng, Dongxu Zhang, Lin Chen, Hainan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05906v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, semantic, geometry  
- **[SSA-3DGS: Unsupervised Removal of Screen-Space Artifacts for 3D Gaussian Splatting](https://arxiv.org/abs/2607.05598v1)**  
  Authors: Kristof Overdulve, Lode Jorissen, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05598v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, 3d gaussian  
- **[Rendering-Aware Bayesian 3D Gaussian Splatting with Native Uncertainty and Adaptive Complexity Control](https://arxiv.org/abs/2607.05522v1)**  
  Authors: Gaoxiang Jia, Vikram Appia, Junzhou Huang, Xinlei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05522v1.pdf)  
  Keywords: sparse view, 3d gaussian, gaussian splatting, ar, geometry  
- **[WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images](https://arxiv.org/abs/2607.05347v1)**  
  Authors: Xiyu Zhang, Jingyu Zhuang, Hongjia Zhai, Zizheng Yan, Jinwei Chen, Guofeng Zhang, Qingnan Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05347v1.pdf)  
  Keywords: efficient, 3d reconstruction, 3d gaussian, gaussian splatting, ar, illumination, face, geometry  
- **[GUSH3R: Everyone Everywhere All at Once as Gaussians](https://arxiv.org/abs/2607.05243v1)**  
  Authors: Keito Abe, Kaede Shiohara, Takashi Otonari, Toshihiko Yamasaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05243v1.pdf)  
  Keywords: motion, efficient, 3d reconstruction, 3d gaussian, gaussian splatting, ar, human, dynamic, geometry  

### Large Scene

- **[Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction](https://arxiv.org/abs/2607.08769v1)**  
  Authors: Weijian Chen, Weibo Yao, Yuhang Zhang, Xiaolin Tang, Guo Wang, Weijun Zhang, Xitong Gao, Yihao Chen, Hongde Qin, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08769v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, outdoor, geometry  
- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771v1)**  
  Authors: Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03771v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/VOP-GS)  
  Keywords: efficient, large scene, sparse view, 3d gaussian, gaussian splatting, ar, face, geometry  
- **[Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673v1)**  
  Authors: Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu, Krishna Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00673v1.pdf)  
  Keywords: deformation, 3d gaussian, ar, outdoor, human  
- **[GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping](https://arxiv.org/abs/2606.30809v1)**  
  Authors: Annika Thomas, Mason Peterson, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30809v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, outdoor, mapping, geometry  
- **[Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes](https://arxiv.org/abs/2606.30436v1)**  
  Authors: Sicheng Yu, Dongxu Shen, Beizhen Zhao, Guanzhi Ding, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30436v1.pdf)  
  Keywords: motion, efficient, 3d gaussian, gaussian splatting, tracking, slam, high-fidelity, ar, outdoor, mapping, dynamic, head  
- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796v1)**  
  Authors: Leshu Li, Jie Peng, Yang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/UMN-ZhaoLab/Pocket-SLAM.git?style=social)](https://github.com/UMN-ZhaoLab/Pocket-SLAM.git)  
  Keywords: efficient, 3d gaussian, gaussian splatting, localization, slam, autonomous driving, ar, outdoor, mapping, face, geometry  
- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031v1)**  
  Authors: Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23031v1.pdf)  
  Keywords: efficient, large scene, 3d gaussian, dynamic, gaussian splatting, ar, fast, urban scene, high-fidelity, geometry  
- **[Point-Cloud-Assistant Localized Statistical Channel Prediction by Tangent Gaussian Splatting](https://arxiv.org/abs/2606.18734v1)**  
  Authors: Ye Xue, Yiheng Wang, Xinhua Shao, Qi Yan, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.18734v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, ar, outdoor, fast, geometry  
- **[MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization](https://arxiv.org/abs/2606.17935v1)**  
  Authors: Guo Pu, Yixuan Han, Haofeng Li, Yao Zhang, Hui Zhou, Zhouhui Lian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17935v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TrickyGo/MoonSplat?style=social)](https://github.com/TrickyGo/MoonSplat)  
  Keywords: efficient, 3d reconstruction, 3d gaussian, gaussian splatting, robotics, ar, outdoor, real-time rendering, vr, tracking  
- **[KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis](https://arxiv.org/abs/2606.03120v1)**  
  Authors: Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.03120v1.pdf)  
  Keywords: efficient, 3d gaussian, sparse-view, gaussian splatting, nerf, ar, outdoor, high-fidelity  

### Model Compression

*Showing the latest 50 out of 183 papers*

- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: efficient, 3d gaussian, localization, slam, high-fidelity, ar, mapping, dynamic, tracking, survey  
- **[WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images](https://arxiv.org/abs/2607.05347v1)**  
  Authors: Xiyu Zhang, Jingyu Zhuang, Hongjia Zhai, Zizheng Yan, Jinwei Chen, Guofeng Zhang, Qingnan Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05347v1.pdf)  
  Keywords: efficient, 3d reconstruction, 3d gaussian, gaussian splatting, ar, illumination, face, geometry  
- **[GUSH3R: Everyone Everywhere All at Once as Gaussians](https://arxiv.org/abs/2607.05243v1)**  
  Authors: Keito Abe, Kaede Shiohara, Takashi Otonari, Toshihiko Yamasaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05243v1.pdf)  
  Keywords: motion, efficient, 3d reconstruction, 3d gaussian, gaussian splatting, ar, human, dynamic, geometry  
- **[Semantic-Guided Progressive Object Removal with Gaussian Splatting](https://arxiv.org/abs/2607.04144v1)**  
  Authors: Xianliang Huang, Chen Xiao, Yuanxiang Ni, Guanming Liu, Mingkai Liu, Dikai Fan, Xiao Liu, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04144v1.pdf)  
  Keywords: efficient, gaussian splatting, robotics, ar, vr, semantic, high-fidelity  
- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771v1)**  
  Authors: Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03771v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/VOP-GS)  
  Keywords: efficient, large scene, sparse view, 3d gaussian, gaussian splatting, ar, face, geometry  
- **[Provable Pruning for Efficient 3D Gaussian Splatting via Coresets](https://arxiv.org/abs/2607.02721v1)**  
  Authors: Waseem Mousa, Alaa Maalouf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.02721v1.pdf) | [![GitHub](https://img.shields.io/github/stars/waseem-m/3dgs_provable_coresets?style=social)](https://github.com/waseem-m/3dgs_provable_coresets)  
  Keywords: efficient, compression, 3d gaussian, gaussian splatting, ar  
- **[X-Splat: Gaussian Splatting for 3D CBCT Generation from Single Panoramic Radiograph](https://arxiv.org/abs/2607.02099v1)**  
  Authors: Tomasz Szczepański, Szymon Płotka, Michal K. Grzeszczyk, Tomasz Trzciński, Arkadiusz Sitek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.02099v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tomek1911/X-Splat?style=social)](https://github.com/tomek1911/X-Splat)  
  Keywords: lightweight, gaussian splatting, nerf, ar, segmentation, geometry  
- **[PixGS: Pixel-Space Diffusion for Direct 3D Gaussian Splat Generation](https://arxiv.org/abs/2607.01803v2)**  
  Authors: Cao Duy, Phong Nguyen-Ha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01803v2.pdf)  
  Keywords: efficient, compression, 3d gaussian, ar, fast, face, geometry  
- **[Efficient Compression of Structured and Unstructured Volumes via Learned 3D Gaussian Representation](https://arxiv.org/abs/2607.01164v1)**  
  Authors: Landon Dyken, Sharmistha Chakrabarti, Nathan Debardeleben, Steve Petruzza, Qi Wu, Will Usher, Sidharth Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01164v1.pdf)  
  Keywords: efficient, compression, 3d gaussian, ar, geometry  
- **[Relation-Centric Open-Vocabulary 3D Gaussian Segmentation](https://arxiv.org/abs/2607.01140v1)**  
  Authors: Eunsung Cha, Hyunjoon Lee, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01140v1.pdf)  
  Keywords: efficient, 3d gaussian, understanding, ar, segmentation, fast  

### Quality Enhancement

*Showing the latest 50 out of 118 papers*

- **[EscFOA: Enhancing Spatial Learning for Visually Impaired Learners via Generative Spatial Audio in 360-Degree Educational Environments](https://arxiv.org/abs/2607.07015v1)**  
  Authors: Ziyu Luo, Xiaowei Dai, Siying Zhu, Xiaoming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07015v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, high-fidelity, geometry  
- **[RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation](https://arxiv.org/abs/2607.06699v1)**  
  Authors: Shujie Zhang, Jingkun Yi, Weipeng Zhong, Zirui Zhou, Yangkun Zhu, Hanqing Wang, Xudong Xu, Weinan Zhang, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06699v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, ar, 3d gaussian  
- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: efficient, 3d gaussian, localization, slam, high-fidelity, ar, mapping, dynamic, tracking, survey  
- **[Semantic-Guided Progressive Object Removal with Gaussian Splatting](https://arxiv.org/abs/2607.04144v1)**  
  Authors: Xianliang Huang, Chen Xiao, Yuanxiang Ni, Guanming Liu, Mingkai Liu, Dikai Fan, Xiao Liu, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04144v1.pdf)  
  Keywords: efficient, gaussian splatting, robotics, ar, vr, semantic, high-fidelity  
- **[MACRO: Training-free Multi-plane Attention for Closeup Render Optimization](https://arxiv.org/abs/2607.03875v1)**  
  Authors: Nitzan Hodos, Roy Amoyal, Lior Fritz, Ianir Ideses, Sagie Benaim, Netalee Efrat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03875v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nitzanhod.github.io/MACRO)  
  Keywords: gaussian splatting, high-fidelity, ar, 3d gaussian  
- **[SharpSplat: Edge-Regularized 3D Gaussian Splatting for High Fidelity Urban Building Reconstruction from UAV images](https://arxiv.org/abs/2607.03872v1)**  
  Authors: Porus Vaid, Shivam Chopra, Vaibhav Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03872v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, semantic, high-fidelity  
- **[CGGS: Consistency-Augmented Geometric Gaussian Splatting for Ego-centric 3D Scene Generation](https://arxiv.org/abs/2607.03819v2)**  
  Authors: Zhenyu Sun, Xiaohan Zhang, Qi Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03819v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cggs-26.github.io/cggs26)  
  Keywords: 3d gaussian, gaussian splatting, ar, semantic, high-fidelity  
- **[Sparse-View Surface Reconstruction using Gaussian Splatting through High-Confidence Depth Propagation with Normal Priors](https://arxiv.org/abs/2607.03765v1)**  
  Authors: Liang Han, Bangcai Wei, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03765v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanl2010.github.io/DP-GS)  
  Keywords: sparse view, 3d reconstruction, 3d gaussian, sparse-view, gaussian splatting, ar, face, high-fidelity, geometry  
- **[TemporalGS: Training-Free Plug-and-Play Acceleration for 3D Gaussian Splatting Rendering via Temporal Priors](https://arxiv.org/abs/2607.03390v1)**  
  Authors: Yuhongze Zhou, Zihao Yang, Xinxin Zuo, Juwei Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03390v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, ar, acceleration, fast, high-fidelity, geometry  
- **[DL-SLAM: Enabling High-Fidelity Gaussian Splatting SLAM in Dynamic Environments based on Dual-Level Probability](https://arxiv.org/abs/2607.01860v2)**  
  Authors: Ziheng Xu, Qingfeng Li, Xuefeng Liu, Chen Chen, Jianwei Niu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01860v2.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, localization, slam, high-fidelity, ar, semantic, mapping, dynamic, tracking  

### Ray Tracing

- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036v1)**  
  Authors: Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32036v1.pdf)  
  Keywords: compact, gaussian splatting, ar, ray casting, human, geometry  
- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869v1)**  
  Authors: Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30869v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/gray)  
  Keywords: ray tracing, 3d gaussian, gaussian splatting, ar, fast  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: efficient, ray tracing, 3d gaussian, gaussian splatting, ar, path tracing, real-time rendering, fast, geometry, reflection  
- **[RenderFormer++: Scalable and Physically Grounded Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v1)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jinyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v1.pdf)  
  Keywords: compact, light transport, ar, global illumination, illumination, neural rendering  
- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898v1)**  
  Authors: Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21898v1.pdf)  
  Keywords: efficient, 3d reconstruction, 3d gaussian, gaussian splatting, ar, global illumination, illumination, geometry  
- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159v1)**  
  Authors: Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16159v1.pdf)  
  Keywords: gaussian splatting, ar, global illumination, illumination, high-fidelity  
- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314v1)**  
  Authors: Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11314v1.pdf)  
  Keywords: lighting, motion, ray tracing, 3d reconstruction, 3d gaussian, lightweight, light transport, ar, relighting, neural rendering, dynamic, geometry  
- **[PTIR-GS: Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606v3)**  
  Authors: Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09606v3.pdf)  
  Keywords: lighting, ray tracing, shadow, 3d gaussian, compact, light transport, ar, path tracing, relighting, global illumination, illumination, reflection  
- **[RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation](https://arxiv.org/abs/2606.01261v1)**  
  Authors: Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.01261v1.pdf)  
  Keywords: efficient, ray tracing, 3d gaussian, gaussian splatting, ar, semantic, segmentation, geometry, reflection  
- **[Directed Distance Fields for Constant-Time Ray Queries on Gaussian Splatting](https://arxiv.org/abs/2606.00817v1)**  
  Authors: Subhankar MIshra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00817v1.pdf) | [![GitHub](https://img.shields.io/github/stars/smlab-niser/ddf-gs?style=social)](https://github.com/smlab-niser/ddf-gs)  
  Keywords: shadow, 3d gaussian, gaussian splatting, ar, global illumination, illumination, fast, face  

### Relighting

*Showing the latest 50 out of 59 papers*

- **[GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM](https://arxiv.org/abs/2607.07452v1)**  
  Authors: Lipu Zhou, Yaoyun Kang, Junxiang Pang, Shengkai Sun, Tingting Bao, Kehan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07452v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, slam, robotics, ar, illumination, mapping, geometry  
- **[PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution](https://arxiv.org/abs/2607.06238v1)**  
  Authors: Lihua Wei, Huatong Gao, Jia Gong, Zhiyu Tan, Hao Li, Jun Liu, Zhihua Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06238v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, mapping, dynamic  
- **[WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images](https://arxiv.org/abs/2607.05347v1)**  
  Authors: Xiyu Zhang, Jingyu Zhuang, Hongjia Zhai, Zizheng Yan, Jinwei Chen, Guofeng Zhang, Qingnan Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05347v1.pdf)  
  Keywords: efficient, 3d reconstruction, 3d gaussian, gaussian splatting, ar, illumination, face, geometry  
- **[InvSplat: Inverse Feed-Forward Scene Splatting](https://arxiv.org/abs/2607.02301v1)**  
  Authors: Polina Karpikova, Wenjing Bian, Haofei Xu, Hendrik Lensch, Andreas Geiger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.02301v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://poliik.github.io/invsplat)  
  Keywords: lighting, 3d reconstruction, 3d gaussian, ar, relighting, geometry  
- **[DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918v2)**  
  Authors: Junzhe Jiang, Zipei Ma, Zijie Pan, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31918v2.pdf)  
  Keywords: lighting, 3d gaussian, autonomous driving, ar, real-time rendering  
- **[Intrinsic decomposition and editing of 3D Gaussian splats](https://arxiv.org/abs/2606.31637v1)**  
  Authors: Alexandre Lanvin, Jeffrey Hu, Simon Lucas, Adrien Bousseau, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31637v1.pdf)  
  Keywords: lighting, 3d gaussian, gaussian splatting, ar, face  
- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861v1)**  
  Authors: Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections)  
  Keywords: efficient, ray tracing, 3d gaussian, gaussian splatting, ar, path tracing, real-time rendering, fast, geometry, reflection  
- **[RenderFormer++: Scalable and Physically Grounded Feed-Forward Neural Rendering](https://arxiv.org/abs/2606.30380v1)**  
  Authors: Huangsheng Du, Haoran Zhu, Youcheng Cai, Jinyang Meng, Ligang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30380v1.pdf)  
  Keywords: compact, light transport, ar, global illumination, illumination, neural rendering  
- **[Monte Carlo Energy Aggregation for Mobile 3D Gaussian Splatting](https://arxiv.org/abs/2606.30017v1)**  
  Authors: Xiaobiao Du, YuAn Wang, Hao Li, Bosheng Wang, Xun Sun, Xin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30017v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiaobiaodu.github.io/flux-gs-project)  
  Keywords: lighting, compression, 3d gaussian, compact, gaussian splatting, ar, high-fidelity, head  
- **[Shell-Supervised Gaussian Splatting for Urban Real-to-Sim Reconstruction](https://arxiv.org/abs/2606.30014v1)**  
  Authors: Yuan Yang, Peijun Lu, Fangzhou Lu, Sai Fan, Siqi Yan, Chenyuan Zhang, Haobo Liang, Yichen Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30014v1.pdf)  
  Keywords: 3d reconstruction, lightweight, gaussian splatting, ar, face, geometry, reflection  

### SLAM

*Showing the latest 50 out of 76 papers*

- **[Track2Map: Online Deformable SLAM with Motion-Aware Pose Optimization in Robotic Surgery](https://arxiv.org/abs/2607.08408v1)**  
  Authors: Tianyi Song, Sierra Bonilla, Xinwei Ju, Evangelos Mazomenos, Danail Stoyanov, Adam Schmidt, Omid Mohareri, Sophia Bano, Francisco Vasconcelos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08408v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://track2map.github.io)  
  Keywords: motion, deformation, 3d reconstruction, 3d gaussian, gaussian splatting, slam, ar, mapping  
- **[GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM](https://arxiv.org/abs/2607.07452v1)**  
  Authors: Lipu Zhou, Yaoyun Kang, Junxiang Pang, Shengkai Sun, Tingting Bao, Kehan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07452v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, slam, robotics, ar, illumination, mapping, geometry  
- **[PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution](https://arxiv.org/abs/2607.06238v1)**  
  Authors: Lihua Wei, Huatong Gao, Jia Gong, Zhiyu Tan, Hao Li, Jun Liu, Zhihua Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06238v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, mapping, dynamic  
- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)**  
  Authors: Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06222v1.pdf)  
  Keywords: efficient, 3d gaussian, localization, slam, high-fidelity, ar, mapping, dynamic, tracking, survey  
- **[Real-Time LiDAR Gaussian Splatting SLAM](https://arxiv.org/abs/2607.04127v1)**  
  Authors: Seungjun Tak, Yewon Jeon, Jaeik Hwang, SukMin Hwang, Seongbo Ha, Hyeonwoo Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04127v1.pdf)  
  Keywords: gaussian splatting, slam, ar, fast, mapping, face, tracking, geometry  
- **[PRISM3D: Probabilistic Refinement and Robust Initialization for Physically Consistent Scene Modeling under Extreme Motion Blur](https://arxiv.org/abs/2607.03855v1)**  
  Authors: Gopi Raju Matta, Reddypalli Trisha, Vemunuri Divya Madhuri, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03855v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, ar, tracking, geometry  
- **[DL-SLAM: Enabling High-Fidelity Gaussian Splatting SLAM in Dynamic Environments based on Dual-Level Probability](https://arxiv.org/abs/2607.01860v2)**  
  Authors: Ziheng Xu, Qingfeng Li, Xuefeng Liu, Chen Chen, Jianwei Niu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01860v2.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, localization, slam, high-fidelity, ar, semantic, mapping, dynamic, tracking  
- **[AnchorSplat: Fast and Structure Consistent Detail Synthesis for Gaussian Splatting](https://arxiv.org/abs/2607.01290v2)**  
  Authors: Dexu Zhu, Jiangnan Shao, Xiaofeng Wang, Junxian Duan, Jie Cao, Zheng Zhu, Huaibo Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01290v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, fast, mapping, high-fidelity, head  
- **[NoPA: Non-Parametric Online 3D Scene Graph Generation](https://arxiv.org/abs/2607.00529v1)**  
  Authors: Qi Xun Yeo, Seungjun Lee, Yan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00529v1.pdf)  
  Keywords: 3d gaussian, lightweight, ar, mapping, geometry  
- **[GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping](https://arxiv.org/abs/2606.30809v1)**  
  Authors: Annika Thomas, Mason Peterson, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30809v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, outdoor, mapping, geometry  

### Scene Understanding

*Showing the latest 50 out of 115 papers*

- **[PUF: Plug-and-Play Uncertainty-Aware Fusion for Online 3D Scene Graph Generation](https://arxiv.org/abs/2607.07170v1)**  
  Authors: Yi Yang, Myrna Castillo, Bodo Rosenhahn, Michael Ying Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07170v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yyyyangyi/PUF?style=social)](https://github.com/yyyyangyi/PUF)  
  Keywords: understanding, semantic, ar, 3d gaussian  
- **[GaussFusion: Towards Multimodal 3D Gaussian Pretraining](https://arxiv.org/abs/2607.05906v1)**  
  Authors: Zhixuan You, Jihua Zhu, Yiding Sun, Zihao Guo, Haozhe Cheng, Dongxu Zhang, Lin Chen, Hainan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05906v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, semantic, geometry  
- **[DeGenseGS: Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting](https://arxiv.org/abs/2607.04761v1)**  
  Authors: Yimo Wang, Bin Kang, Shuojue Yang, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04761v1.pdf)  
  Keywords: deformation, 4d, gaussian splatting, understanding, ar, semantic, segmentation, dynamic  
- **[Semantic-Guided Progressive Object Removal with Gaussian Splatting](https://arxiv.org/abs/2607.04144v1)**  
  Authors: Xianliang Huang, Chen Xiao, Yuanxiang Ni, Guanming Liu, Mingkai Liu, Dikai Fan, Xiao Liu, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04144v1.pdf)  
  Keywords: efficient, gaussian splatting, robotics, ar, vr, semantic, high-fidelity  
- **[SharpSplat: Edge-Regularized 3D Gaussian Splatting for High Fidelity Urban Building Reconstruction from UAV images](https://arxiv.org/abs/2607.03872v1)**  
  Authors: Porus Vaid, Shivam Chopra, Vaibhav Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03872v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, semantic, high-fidelity  
- **[CGGS: Consistency-Augmented Geometric Gaussian Splatting for Ego-centric 3D Scene Generation](https://arxiv.org/abs/2607.03819v2)**  
  Authors: Zhenyu Sun, Xiaohan Zhang, Qi Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03819v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cggs-26.github.io/cggs26)  
  Keywords: 3d gaussian, gaussian splatting, ar, semantic, high-fidelity  
- **[X-Splat: Gaussian Splatting for 3D CBCT Generation from Single Panoramic Radiograph](https://arxiv.org/abs/2607.02099v1)**  
  Authors: Tomasz Szczepański, Szymon Płotka, Michal K. Grzeszczyk, Tomasz Trzciński, Arkadiusz Sitek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.02099v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tomek1911/X-Splat?style=social)](https://github.com/tomek1911/X-Splat)  
  Keywords: lightweight, gaussian splatting, nerf, ar, segmentation, geometry  
- **[DL-SLAM: Enabling High-Fidelity Gaussian Splatting SLAM in Dynamic Environments based on Dual-Level Probability](https://arxiv.org/abs/2607.01860v2)**  
  Authors: Ziheng Xu, Qingfeng Li, Xuefeng Liu, Chen Chen, Jianwei Niu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01860v2.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, localization, slam, high-fidelity, ar, semantic, mapping, dynamic, tracking  
- **[The Turning Point of 3D Plant Phenotyping: 3D Foundation Models Enable Minute-to-Second Cross-Crop Reconstruction and Beyond](https://arxiv.org/abs/2607.01753v1)**  
  Authors: Hanyue Jia, Wei Zhou, Wenbo Zhou, Yanan Li, Hao Lu, Tingting Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01753v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, gaussian splatting, ar, semantic, fast, segmentation, geometry  
- **[Consistent Scene Understanding in 3D Gaussian Splatting via Multi-Cue Mask Refinement](https://arxiv.org/abs/2607.01708v1)**  
  Authors: Hyunjoon Park, Donghyeon Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01708v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, understanding, segmentation, semantic, high-fidelity  



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