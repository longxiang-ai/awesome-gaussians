# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-10-01 00:56:48

## 📰 Latest Updates

🔧 **[2025-06-26] HTTP 301 Redirect Issue Completely Resolved!** 
- Implemented multi-layer fallback strategy to thoroughly solve network compatibility issues

🔧 **[2025-06-26] Configurable Search Keywords Feature Added!**
- You can now customize search keywords by modifying `data/search_config.json`
- Support for different search scopes: abstract-only, title-only, or both
- Flexible keyword configuration for targeted paper collection

- View detailed updates: [News.md](News.md) 📋

---

## Categories

- [3DGS Surveys](#3dgs-surveys) (21 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (258 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (329 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (383 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (71 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (314 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (74 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (413 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (160 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (16 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (114 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (150 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (196 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: nerf, efficient, survey, slam, understanding, neural rendering, gaussian splatting, fast, ar, 3d gaussian  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: nerf, lighting, survey, semantic, understanding, compact, gaussian splatting, segmentation, high-fidelity, 3d gaussian, ar  
- **[A Study of the Framework and Real-World Applications of Language
  Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: nerf, survey, semantic, robotics, understanding, gaussian splatting, ar, efficient, 3d gaussian  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned
  and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: nerf, human, survey, robotics, gaussian splatting, ar, 3d gaussian  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: vr, nerf, survey, robotics, geometry, sparse-view, motion, gaussian splatting, 3d reconstruction, ar, 3d gaussian  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v3)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Kaichen Zhou, Paul Pu Liang, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v3.pdf)  
  Keywords: vr, nerf, lighting, survey, human, slam, robotics, dynamic, gaussian splatting, fast, 3d reconstruction, ar, 3d gaussian  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: face, nerf, efficient, survey, autonomous driving, outdoor, dynamic, gaussian splatting, ar, high-fidelity, 3d gaussian  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: vr, nerf, survey, robotics, autonomous driving, neural rendering, gaussian splatting, 3d reconstruction, ar, high-fidelity, 3d gaussian  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: efficient, survey, semantic, understanding, outdoor, neural rendering, gaussian splatting, 3d reconstruction, segmentation, high-fidelity, 3d gaussian, ar  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: nerf, survey, semantic, slam, mapping, localization, gaussian splatting, segmentation, ar, efficient, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 258 papers*

- **[Triangle Splatting+: Differentiable Rendering with Opaque Triangles](https://arxiv.org/abs/2509.25122v1)**  
  Authors: Jan Held, Renaud Vandeghen, Sanghyun Son, Daniel Rebain, Matheus Gadelha, Yi Zhou, Ming C. Lin, Marc Van Droogenbroeck, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25122v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://trianglesplatting2.github.io/trianglesplatting2/.)  
  Keywords: vr, nerf, efficient, real-time rendering, gaussian splatting, fast, ar, 3d gaussian, head  
- **[GEM: 3D Gaussian Splatting for Efficient and Accurate Cryo-EM
  Reconstruction](https://arxiv.org/abs/2509.25075v1)**  
  Authors: Huaizhi Qu, Xiao Wang, Gengwei Zhang, Jie Peng, Tianlong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25075v1.pdf)  
  Keywords: nerf, efficient, gaussian splatting, fast, 3d reconstruction, ar, compact, 3d gaussian, head  
- **[Proxy-GS: Efficient 3D Gaussian Splatting via Proxy Mesh](https://arxiv.org/abs/2509.24421v1)**  
  Authors: Yuanyuan Gao, Yuning Gong, Yifei Liu, Li Jingfeng, Zhihang Zhong, Dingwen Zhang, Yanci Zhang, Dan Xu, Xiao Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24421v1.pdf)  
  Keywords: face, gaussian splatting, fast, ar, efficient, head, 3d gaussian  
- **[CrashSplat: 2D to 3D Vehicle Damage Segmentation in Gaussian Splatting](https://arxiv.org/abs/2509.23947v1)**  
  Authors: Dragoş-Andrei Chileban, Andrei-Ştefan Bulzan, Cosmin Cernǎzanu-Glǎvan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23947v1.pdf)  
  Keywords: motion, gaussian splatting, fast, 3d reconstruction, segmentation, 3d gaussian, ar  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: nerf, efficient, survey, slam, understanding, neural rendering, gaussian splatting, fast, ar, 3d gaussian  
- **[Vision-Language Alignment from Compressed Image Representations using 2D
  Gaussian Splatting](https://arxiv.org/abs/2509.22615v1)**  
  Authors: Yasmine Omri, Connor Ding, Tsachy Weissman, Thierry Tambe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22615v1.pdf)  
  Keywords: semantic, gaussian splatting, fast, ar, compact, efficient, lightweight  
- **[PolGS: Polarimetric Gaussian Splatting for Fast Reflective Surface
  Reconstruction](https://arxiv.org/abs/2509.19726v1)**  
  Authors: Yufei Han, Bowen Tie, Heng Guo, Youwei Lyu, Si Li, Boxin Shi, Yunpeng Jia, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19726v1.pdf)  
  Keywords: face, shape reconstruction, gaussian splatting, fast, ar, efficient, 3d gaussian  
- **[Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model
  Self-Distillation](https://arxiv.org/abs/2509.19296v1)**  
  Authors: Sherwin Bahmani, Tianchang Shen, Jiawei Ren, Jiahui Huang, Yifeng Jiang, Haithem Turki, Andrea Tagliasacchi, David B. Lindell, Zan Gojcic, Sanja Fidler, Huan Ling, Jun Gao, Xuanchi Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19296v1.pdf)  
  Keywords: real-time rendering, robotics, autonomous driving, dynamic, gaussian splatting, 3d reconstruction, ar, 3d gaussian  
- **[Event-guided 3D Gaussian Splatting for Dynamic Human and Scene
  Reconstruction](https://arxiv.org/abs/2509.18566v1)**  
  Authors: Xiaoting Yin, Hao Shi, Kailun Yang, Jiajun Zhai, Shangwei Guo, Lin Wang, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18566v1.pdf)  
  Keywords: animation, human, semantic, motion, dynamic, gaussian splatting, fast, ar, 3d gaussian, deformation  
- **[FGGS-LiDAR: Ultra-Fast, GPU-Accelerated Simulation from General 3DGS
  Models to LiDAR](https://arxiv.org/abs/2509.17390v1)**  
  Authors: Junzhe Wu, Yufei Jia, Yiyi Yan, Zhixing Chen, Tiao Tan, Zifan Wang, Guangyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.17390v1.pdf)  
  Keywords: robotics, autonomous driving, outdoor, gaussian splatting, fast, ar, high-fidelity, 3d gaussian  

### Applications

*Showing the latest 50 out of 995 papers*

- **[Triangle Splatting+: Differentiable Rendering with Opaque Triangles](https://arxiv.org/abs/2509.25122v1)**  
  Authors: Jan Held, Renaud Vandeghen, Sanghyun Son, Daniel Rebain, Matheus Gadelha, Yi Zhou, Ming C. Lin, Marc Van Droogenbroeck, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25122v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://trianglesplatting2.github.io/trianglesplatting2/.)  
  Keywords: vr, nerf, efficient, real-time rendering, gaussian splatting, fast, ar, 3d gaussian, head  
- **[GEM: 3D Gaussian Splatting for Efficient and Accurate Cryo-EM
  Reconstruction](https://arxiv.org/abs/2509.25075v1)**  
  Authors: Huaizhi Qu, Xiao Wang, Gengwei Zhang, Jie Peng, Tianlong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25075v1.pdf)  
  Keywords: nerf, efficient, gaussian splatting, fast, 3d reconstruction, ar, compact, 3d gaussian, head  
- **[LVT: Large-Scale Scene Reconstruction via Local View Transformers](https://arxiv.org/abs/2509.25001v1)**  
  Authors: Tooba Imtiaz, Lucy Chai, Kathryn Heal, Xuan Luo, Jungyeon Park, Jennifer Dy, John Flynn  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25001v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://toobaimt.github.io/lvt/.)  
  Keywords: large scene, 3d gaussian, ar  
- **[DWGS: Enhancing Sparse-View Gaussian Splatting with Hybrid-Loss Depth
  Estimation and Bidirectional Warping](https://arxiv.org/abs/2509.24893v1)**  
  Authors: Yu Ma, Guoliang Wei, Yue Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24893v1.pdf)  
  Keywords: sparse-view, sparse view, gaussian splatting, 3d reconstruction, ar, high-fidelity, 3d gaussian  
- **[ExGS: Extreme 3D Gaussian Compression with Diffusion Priors](https://arxiv.org/abs/2509.24758v1)**  
  Authors: Jiaqi Chen, Xinhao Ji, Yuanyuan Gao, Hao Li, Yuning Gong, Yifei Liu, Dan Xu, Zhihang Zhong, Dingwen Zhang, Xiao Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24758v1.pdf)  
  Keywords: compression, neural rendering, gaussian splatting, ar, efficient, lightweight, 3d gaussian  
- **[Proxy-GS: Efficient 3D Gaussian Splatting via Proxy Mesh](https://arxiv.org/abs/2509.24421v1)**  
  Authors: Yuanyuan Gao, Yuning Gong, Yifei Liu, Li Jingfeng, Zhihang Zhong, Dingwen Zhang, Yanci Zhang, Dan Xu, Xiao Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24421v1.pdf)  
  Keywords: face, gaussian splatting, fast, ar, efficient, head, 3d gaussian  
- **[OMeGa: Joint Optimization of Explicit Meshes and Gaussian Splats for
  Robust Scene-Level Surface Reconstruction](https://arxiv.org/abs/2509.24308v1)**  
  Authors: Yuhang Cao, Haojun Yan, Danya Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24308v1.pdf)  
  Keywords: face, geometry, neural rendering, gaussian splatting, ar  
- **[CrashSplat: 2D to 3D Vehicle Damage Segmentation in Gaussian Splatting](https://arxiv.org/abs/2509.23947v1)**  
  Authors: Dragoş-Andrei Chileban, Andrei-Ştefan Bulzan, Cosmin Cernǎzanu-Glǎvan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23947v1.pdf)  
  Keywords: motion, gaussian splatting, fast, 3d reconstruction, segmentation, 3d gaussian, ar  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: nerf, efficient, survey, slam, understanding, neural rendering, gaussian splatting, fast, ar, 3d gaussian  
- **[Orientation-anchored Hyper-Gaussian for 4D Reconstruction from Casual
  Videos](https://arxiv.org/abs/2509.23492v1)**  
  Authors: Junyi Wu, Jiachen Tao, Haoxuan Wang, Gaowen Liu, Ramana Rao Kompella, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23492v1.pdf)  
  Keywords: 4d, geometry, motion, dynamic, gaussian splatting, ar, 3d gaussian, deformation  

### Avatar Generation

*Showing the latest 50 out of 329 papers*

- **[Triangle Splatting+: Differentiable Rendering with Opaque Triangles](https://arxiv.org/abs/2509.25122v1)**  
  Authors: Jan Held, Renaud Vandeghen, Sanghyun Son, Daniel Rebain, Matheus Gadelha, Yi Zhou, Ming C. Lin, Marc Van Droogenbroeck, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25122v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://trianglesplatting2.github.io/trianglesplatting2/.)  
  Keywords: vr, nerf, efficient, real-time rendering, gaussian splatting, fast, ar, 3d gaussian, head  
- **[GEM: 3D Gaussian Splatting for Efficient and Accurate Cryo-EM
  Reconstruction](https://arxiv.org/abs/2509.25075v1)**  
  Authors: Huaizhi Qu, Xiao Wang, Gengwei Zhang, Jie Peng, Tianlong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25075v1.pdf)  
  Keywords: nerf, efficient, gaussian splatting, fast, 3d reconstruction, ar, compact, 3d gaussian, head  
- **[Proxy-GS: Efficient 3D Gaussian Splatting via Proxy Mesh](https://arxiv.org/abs/2509.24421v1)**  
  Authors: Yuanyuan Gao, Yuning Gong, Yifei Liu, Li Jingfeng, Zhihang Zhong, Dingwen Zhang, Yanci Zhang, Dan Xu, Xiao Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24421v1.pdf)  
  Keywords: face, gaussian splatting, fast, ar, efficient, head, 3d gaussian  
- **[OMeGa: Joint Optimization of Explicit Meshes and Gaussian Splats for
  Robust Scene-Level Surface Reconstruction](https://arxiv.org/abs/2509.24308v1)**  
  Authors: Yuhang Cao, Haojun Yan, Danya Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24308v1.pdf)  
  Keywords: face, geometry, neural rendering, gaussian splatting, ar  
- **[GS-2M: Gaussian Splatting for Joint Mesh Reconstruction and Material
  Decomposition](https://arxiv.org/abs/2509.22276v1)**  
  Authors: Dinh Minh Nguyen, Malte Avenhaus, Thomas Lindemeier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22276v1.pdf)  
  Keywords: face, ar, 3d gaussian, gaussian splatting  
- **[Gaussian splatting holography](https://arxiv.org/abs/2509.20774v1)**  
  Authors: Shuhe Zhang, Liangcai Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20774v1.pdf)  
  Keywords: face, ar, compression, gaussian splatting  
- **[PolGS: Polarimetric Gaussian Splatting for Fast Reflective Surface
  Reconstruction](https://arxiv.org/abs/2509.19726v1)**  
  Authors: Yufei Han, Bowen Tie, Heng Guo, Youwei Lyu, Si Li, Boxin Shi, Yunpeng Jia, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19726v1.pdf)  
  Keywords: face, shape reconstruction, gaussian splatting, fast, ar, efficient, 3d gaussian  
- **[Seeing Through Reflections: Advancing 3D Scene Reconstruction in
  Mirror-Containing Environments with Gaussian Splatting](https://arxiv.org/abs/2509.18956v1)**  
  Authors: Zijing Guo, Yunyang Zhao, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18956v1.pdf)  
  Keywords: face, nerf, geometry, mapping, reflection, gaussian splatting, 3d reconstruction, ar, 3d gaussian  
- **[Event-guided 3D Gaussian Splatting for Dynamic Human and Scene
  Reconstruction](https://arxiv.org/abs/2509.18566v1)**  
  Authors: Xiaoting Yin, Hao Shi, Kailun Yang, Jiajun Zhai, Shangwei Guo, Lin Wang, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18566v1.pdf)  
  Keywords: animation, human, semantic, motion, dynamic, gaussian splatting, fast, ar, 3d gaussian, deformation  
- **[GeoSVR: Taming Sparse Voxels for Geometrically Accurate Surface
  Reconstruction](https://arxiv.org/abs/2509.18090v1)**  
  Authors: Jiahe Li, Jiawei Zhang, Youmin Zhang, Xiao Bai, Jin Zheng, Xiaohan Yu, Lin Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18090v1.pdf)  
  Keywords: face, ar, vr, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 383 papers*

- **[CrashSplat: 2D to 3D Vehicle Damage Segmentation in Gaussian Splatting](https://arxiv.org/abs/2509.23947v1)**  
  Authors: Dragoş-Andrei Chileban, Andrei-Ştefan Bulzan, Cosmin Cernǎzanu-Glǎvan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23947v1.pdf)  
  Keywords: motion, gaussian splatting, fast, 3d reconstruction, segmentation, 3d gaussian, ar  
- **[Orientation-anchored Hyper-Gaussian for 4D Reconstruction from Casual
  Videos](https://arxiv.org/abs/2509.23492v1)**  
  Authors: Junyi Wu, Jiachen Tao, Haoxuan Wang, Gaowen Liu, Ramana Rao Kompella, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23492v1.pdf)  
  Keywords: 4d, geometry, motion, dynamic, gaussian splatting, ar, 3d gaussian, deformation  
- **[Large Material Gaussian Model for Relightable 3D Generation](https://arxiv.org/abs/2509.22112v1)**  
  Authors: Jingrui Ye, Lingting Zhu, Runze Zhang, Zeyu Hu, Yingda Yin, Lanjiong Li, Lequan Yu, Qingmin Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22112v1.pdf)  
  Keywords: relightable, efficient, lighting, dynamic, gaussian splatting, ar, 3d gaussian, relighting  
- **[Drag4D: Align Your Motion with Text-Driven 3D Scene Generation](https://arxiv.org/abs/2509.21888v1)**  
  Authors: Minjun Kang, Inkyu Shin, Taeyeop Lee, In So Kweon, Kuk-Jin Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.21888v1.pdf)  
  Keywords: 4d, motion, gaussian splatting, 3d reconstruction, ar  
- **[Dynamic Novel View Synthesis in High Dynamic Range](https://arxiv.org/abs/2509.21853v1)**  
  Authors: Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.21853v1.pdf)  
  Keywords: 4d, lighting, mapping, dynamic, gaussian splatting, ar  
- **[4D Driving Scene Generation With Stereo Forcing](https://arxiv.org/abs/2509.20251v1)**  
  Authors: Hao Lu, Zhuang Ma, Guangfeng Jiang, Wenhang Ge, Bohan Li, Yuzhan Cai, Wenzhao Zheng, Yunpeng Zhang, Yingcong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20251v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiangxb98.github.io/PhiGensis}{PhiGensis}.)  
  Keywords: 4d, semantic, geometry, motion, dynamic, gaussian splatting, ar  
- **[Aerial-Ground Image Feature Matching via 3D Gaussian Splatting-based
  Intermediate View Rendering](https://arxiv.org/abs/2509.19898v1)**  
  Authors: Jiangxue Yu, Hui Wang, San Jiang, Xing Zhang, Dejin Zhang, Qingquan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19898v1.pdf)  
  Keywords: large scene, motion, gaussian splatting, ar, 3d gaussian  
- **[SeHDR: Single-Exposure HDR Novel View Synthesis via 3D Gaussian
  Bracketing](https://arxiv.org/abs/2509.20400v1)**  
  Authors: Yiyu Li, Haoyuan Wang, Ke Xu, Gerhard Petrus Hancke, Rynson W. H. Lau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20400v1.pdf)  
  Keywords: geometry, motion, dynamic, gaussian splatting, ar, 3d gaussian  
- **[Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model
  Self-Distillation](https://arxiv.org/abs/2509.19296v1)**  
  Authors: Sherwin Bahmani, Tianchang Shen, Jiawei Ren, Jiahui Huang, Yifeng Jiang, Haithem Turki, Andrea Tagliasacchi, David B. Lindell, Zan Gojcic, Sanja Fidler, Huan Ling, Jun Gao, Xuanchi Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19296v1.pdf)  
  Keywords: real-time rendering, robotics, autonomous driving, dynamic, gaussian splatting, 3d reconstruction, ar, 3d gaussian  
- **[DeblurSplat: SfM-free 3D Gaussian Splatting with Event Camera for Robust
  Deblurring](https://arxiv.org/abs/2509.18898v1)**  
  Authors: Pengteng Li, Yunfan Lu, Pinhao Song, Weiyu Guo, Huizai Yao, F. Richard Yu, Hui Xiong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18898v1.pdf)  
  Keywords: motion, dynamic, gaussian splatting, ar, high-fidelity, 3d gaussian  

### Few-shot

*Showing the latest 50 out of 71 papers*

- **[DWGS: Enhancing Sparse-View Gaussian Splatting with Hybrid-Loss Depth
  Estimation and Bidirectional Warping](https://arxiv.org/abs/2509.24893v1)**  
  Authors: Yu Ma, Guoliang Wei, Yue Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24893v1.pdf)  
  Keywords: sparse-view, sparse view, gaussian splatting, 3d reconstruction, ar, high-fidelity, 3d gaussian  
- **[OracleGS: Grounding Generative Priors for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2509.23258v1)**  
  Authors: Atakan Topaloglu, Kunyi Li, Michael Niemeyer, Nassir Navab, A. Murat Tekalp, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23258v1.pdf)  
  Keywords: nerf, sparse-view, sparse view, gaussian splatting, ar, 3d gaussian  
- **[WaveletGaussian: Wavelet-domain Diffusion for Sparse-view 3D Gaussian
  Object Reconstruction](https://arxiv.org/abs/2509.19073v1)**  
  Authors: Hung Nguyen, Runfa Li, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19073v1.pdf)  
  Keywords: nerf, efficient, sparse-view, gaussian splatting, ar, 3d gaussian, lightweight  
- **[FixingGS: Enhancing 3D Gaussian Splatting via Training-Free Score
  Distillation](https://arxiv.org/abs/2509.18759v1)**  
  Authors: Zhaorui Wang, Yi Gu, Deming Zhou, Renjing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18759v1.pdf)  
  Keywords: sparse-view, sparse view, gaussian splatting, 3d reconstruction, ar, 3d gaussian  
- **[SPFSplatV2: Efficient Self-Supervised Pose-Free 3D Gaussian Splatting
  from Sparse Views](https://arxiv.org/abs/2509.17246v1)**  
  Authors: Ranran Huang, Krystian Mikolajczyk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.17246v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ranrhuang.github.io/spfsplatv2/.)  
  Keywords: sparse view, gaussian splatting, ar, efficient, 3d gaussian  
- **[MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2509.15548v3)**  
  Authors: Deming Li, Kaiwen Jiang, Yutao Tang, Ravi Ramamoorthi, Rama Chellappa, Cheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.15548v3.pdf)  
  Keywords: nerf, semantic, geometry, sparse-view, motion, gaussian splatting, ar, 3d gaussian  
- **[LamiGauss: Pitching Radiative Gaussian for Sparse-View X-ray
  Laminography Reconstruction](https://arxiv.org/abs/2509.13863v1)**  
  Authors: Chu Chen, Ander Biguri, Jean-Michel Morel, Raymond H. Chan, Carola-Bibiane Schönlieb, Jizhou Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.13863v1.pdf)  
  Keywords: ar, sparse-view, efficient, gaussian splatting  
- **[Segmentation-Driven Initialization for Sparse-view 3D Gaussian Splatting](https://arxiv.org/abs/2509.11853v1)**  
  Authors: Yi-Hsin Li, Thomas Sikora, Sebastian Knorr, Måarten Sjöström  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.11853v1.pdf)  
  Keywords: real-time rendering, geometry, sparse-view, motion, gaussian splatting, fast, segmentation, 3d gaussian, ar  
- **[AD-GS: Alternating Densification for Sparse-Input 3D Gaussian Splatting](https://arxiv.org/abs/2509.11003v2)**  
  Authors: Gurutva Patle, Nilay Girgaonkar, Nagabhushan Somraj, Rajiv Soundararajan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.11003v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gurutvapatle.github.io/publications/2025/ADGS.html)  
  Keywords: geometry, sparse-view, gaussian splatting, ar, 3d gaussian  
- **[${C}^{3}$-GS: Learning Context-aware, Cross-dimension, Cross-scale
  Feature for Generalizable Gaussian Splatting](https://arxiv.org/abs/2508.20754v1)**  
  Authors: Yuxi Hu, Jun Zhang, Kuangyi Chen, Zhe Zhang, Friedrich Fraundorfer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.20754v1.pdf)  
  Keywords: geometry, sparse view, gaussian splatting, ar, lightweight  

### Geometry Reconstruction

*Showing the latest 50 out of 314 papers*

- **[GEM: 3D Gaussian Splatting for Efficient and Accurate Cryo-EM
  Reconstruction](https://arxiv.org/abs/2509.25075v1)**  
  Authors: Huaizhi Qu, Xiao Wang, Gengwei Zhang, Jie Peng, Tianlong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25075v1.pdf)  
  Keywords: nerf, efficient, gaussian splatting, fast, 3d reconstruction, ar, compact, 3d gaussian, head  
- **[DWGS: Enhancing Sparse-View Gaussian Splatting with Hybrid-Loss Depth
  Estimation and Bidirectional Warping](https://arxiv.org/abs/2509.24893v1)**  
  Authors: Yu Ma, Guoliang Wei, Yue Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24893v1.pdf)  
  Keywords: sparse-view, sparse view, gaussian splatting, 3d reconstruction, ar, high-fidelity, 3d gaussian  
- **[OMeGa: Joint Optimization of Explicit Meshes and Gaussian Splats for
  Robust Scene-Level Surface Reconstruction](https://arxiv.org/abs/2509.24308v1)**  
  Authors: Yuhang Cao, Haojun Yan, Danya Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24308v1.pdf)  
  Keywords: face, geometry, neural rendering, gaussian splatting, ar  
- **[CrashSplat: 2D to 3D Vehicle Damage Segmentation in Gaussian Splatting](https://arxiv.org/abs/2509.23947v1)**  
  Authors: Dragoş-Andrei Chileban, Andrei-Ştefan Bulzan, Cosmin Cernǎzanu-Glǎvan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23947v1.pdf)  
  Keywords: motion, gaussian splatting, fast, 3d reconstruction, segmentation, 3d gaussian, ar  
- **[Orientation-anchored Hyper-Gaussian for 4D Reconstruction from Casual
  Videos](https://arxiv.org/abs/2509.23492v1)**  
  Authors: Junyi Wu, Jiachen Tao, Haoxuan Wang, Gaowen Liu, Ramana Rao Kompella, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23492v1.pdf)  
  Keywords: 4d, geometry, motion, dynamic, gaussian splatting, ar, 3d gaussian, deformation  
- **[Learning Unified Representation of 3D Gaussian Splatting](https://arxiv.org/abs/2509.22917v1)**  
  Authors: Yuelin Xin, Yuheng Liu, Xiaohui Xie, Xinke Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22917v1.pdf)  
  Keywords: mapping, gaussian splatting, 3d reconstruction, ar, efficient, 3d gaussian  
- **[Drag4D: Align Your Motion with Text-Driven 3D Scene Generation](https://arxiv.org/abs/2509.21888v1)**  
  Authors: Minjun Kang, Inkyu Shin, Taeyeop Lee, In So Kweon, Kuk-Jin Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.21888v1.pdf)  
  Keywords: 4d, motion, gaussian splatting, 3d reconstruction, ar  
- **[4D Driving Scene Generation With Stereo Forcing](https://arxiv.org/abs/2509.20251v1)**  
  Authors: Hao Lu, Zhuang Ma, Guangfeng Jiang, Wenhang Ge, Bohan Li, Yuzhan Cai, Wenzhao Zheng, Yunpeng Zhang, Yingcong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20251v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiangxb98.github.io/PhiGensis}{PhiGensis}.)  
  Keywords: 4d, semantic, geometry, motion, dynamic, gaussian splatting, ar  
- **[PolGS: Polarimetric Gaussian Splatting for Fast Reflective Surface
  Reconstruction](https://arxiv.org/abs/2509.19726v1)**  
  Authors: Yufei Han, Bowen Tie, Heng Guo, Youwei Lyu, Si Li, Boxin Shi, Yunpeng Jia, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19726v1.pdf)  
  Keywords: face, shape reconstruction, gaussian splatting, fast, ar, efficient, 3d gaussian  
- **[SeHDR: Single-Exposure HDR Novel View Synthesis via 3D Gaussian
  Bracketing](https://arxiv.org/abs/2509.20400v1)**  
  Authors: Yiyu Li, Haoyuan Wang, Ke Xu, Gerhard Petrus Hancke, Rynson W. H. Lau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20400v1.pdf)  
  Keywords: geometry, motion, dynamic, gaussian splatting, ar, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 74 papers*

- **[LVT: Large-Scale Scene Reconstruction via Local View Transformers](https://arxiv.org/abs/2509.25001v1)**  
  Authors: Tooba Imtiaz, Lucy Chai, Kathryn Heal, Xuan Luo, Jungyeon Park, Jennifer Dy, John Flynn  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25001v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://toobaimt.github.io/lvt/.)  
  Keywords: large scene, 3d gaussian, ar  
- **[Aerial-Ground Image Feature Matching via 3D Gaussian Splatting-based
  Intermediate View Rendering](https://arxiv.org/abs/2509.19898v1)**  
  Authors: Jiangxue Yu, Hui Wang, San Jiang, Xing Zhang, Dejin Zhang, Qingquan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19898v1.pdf)  
  Keywords: large scene, motion, gaussian splatting, ar, 3d gaussian  
- **[FGGS-LiDAR: Ultra-Fast, GPU-Accelerated Simulation from General 3DGS
  Models to LiDAR](https://arxiv.org/abs/2509.17390v1)**  
  Authors: Junzhe Wu, Yufei Jia, Yiyi Yan, Zhixing Chen, Tiao Tan, Zifan Wang, Guangyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.17390v1.pdf)  
  Keywords: robotics, autonomous driving, outdoor, gaussian splatting, fast, ar, high-fidelity, 3d gaussian  
- **[ROSGS: Relightable Outdoor Scenes With Gaussian Splatting](https://arxiv.org/abs/2509.11275v1)**  
  Authors: Lianjun Liao, Chunhui Zhang, Tong Wu, Henglei Lv, Bailin Deng, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.11275v1.pdf)  
  Keywords: nerf, efficient rendering, relightable, efficient, lighting, geometry, outdoor, gaussian splatting, ar, illumination, compact, 3d gaussian, head, relighting  
- **[VIM-GS: Visual-Inertial Monocular Gaussian Splatting via Object-level
  Guidance in Large Scenes](https://arxiv.org/abs/2509.06685v3)**  
  Authors: Shengkai Zhang, Yuhe Liu, Guanjun Wu, Jianhua He, Xinggang Wang, Mozi Chen, Kezhong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06685v3.pdf)  
  Keywords: large scene, motion, dynamic, gaussian splatting, ar  
- **[3DOF+Quantization: 3DGS quantization for large scenes with limited
  Degrees of Freedom](https://arxiv.org/abs/2509.06400v1)**  
  Authors: Matthieu Gendrin, Stéphane Pateux, Théo Ladune  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06400v1.pdf)  
  Keywords: large scene, 3d gaussian, gaussian splatting, ar  
- **[GSVisLoc: Generalizable Visual Localization for Gaussian Splatting Scene
  Representations](https://arxiv.org/abs/2508.18242v1)**  
  Authors: Fadi Khatib, Dror Moran, Guy Trostianetsky, Yoni Kasten, Meirav Galun, Ronen Basri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.18242v1.pdf)  
  Keywords: outdoor, localization, gaussian splatting, ar, 3d gaussian  
- **[MeSS: City Mesh-Guided Outdoor Scene Generation with Cross-View
  Consistent Diffusion](https://arxiv.org/abs/2508.15169v2)**  
  Authors: Xuyang Chen, Zhijun Zhai, Kaixuan Zhou, Zengmao Wang, Jianan He, Dong Wang, Yanfeng Zhang, mingwei Sun, Rüdiger Westermann, Konrad Schindler, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.15169v2.pdf)  
  Keywords: face, lighting, geometry, autonomous driving, outdoor, sparse view, gaussian splatting, ar, 3d gaussian, relighting  
- **[Reconstruction Using the Invisible: Intuition from NIR and Metadata for
  Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2508.14443v1)**  
  Authors: Gyusam Chang, Tuan-Anh Vu, Vivek Alumootil, Harris Song, Deanna Pham, Sangpil Kim, M. Khalid Jawed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14443v1.pdf)  
  Keywords: lighting, understanding, outdoor, gaussian splatting, 3d reconstruction, illumination, 3d gaussian, ar  
- **[Online 3D Gaussian Splatting Modeling with Novel View Selection](https://arxiv.org/abs/2508.14014v2)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14014v2.pdf)  
  Keywords: slam, outdoor, gaussian splatting, ar, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 413 papers*

- **[Triangle Splatting+: Differentiable Rendering with Opaque Triangles](https://arxiv.org/abs/2509.25122v1)**  
  Authors: Jan Held, Renaud Vandeghen, Sanghyun Son, Daniel Rebain, Matheus Gadelha, Yi Zhou, Ming C. Lin, Marc Van Droogenbroeck, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25122v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://trianglesplatting2.github.io/trianglesplatting2/.)  
  Keywords: vr, nerf, efficient, real-time rendering, gaussian splatting, fast, ar, 3d gaussian, head  
- **[GEM: 3D Gaussian Splatting for Efficient and Accurate Cryo-EM
  Reconstruction](https://arxiv.org/abs/2509.25075v1)**  
  Authors: Huaizhi Qu, Xiao Wang, Gengwei Zhang, Jie Peng, Tianlong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25075v1.pdf)  
  Keywords: nerf, efficient, gaussian splatting, fast, 3d reconstruction, ar, compact, 3d gaussian, head  
- **[ExGS: Extreme 3D Gaussian Compression with Diffusion Priors](https://arxiv.org/abs/2509.24758v1)**  
  Authors: Jiaqi Chen, Xinhao Ji, Yuanyuan Gao, Hao Li, Yuning Gong, Yifei Liu, Dan Xu, Zhihang Zhong, Dingwen Zhang, Xiao Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24758v1.pdf)  
  Keywords: compression, neural rendering, gaussian splatting, ar, efficient, lightweight, 3d gaussian  
- **[Proxy-GS: Efficient 3D Gaussian Splatting via Proxy Mesh](https://arxiv.org/abs/2509.24421v1)**  
  Authors: Yuanyuan Gao, Yuning Gong, Yifei Liu, Li Jingfeng, Zhihang Zhong, Dingwen Zhang, Yanci Zhang, Dan Xu, Xiao Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24421v1.pdf)  
  Keywords: face, gaussian splatting, fast, ar, efficient, head, 3d gaussian  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: nerf, efficient, survey, slam, understanding, neural rendering, gaussian splatting, fast, ar, 3d gaussian  
- **[Learning Unified Representation of 3D Gaussian Splatting](https://arxiv.org/abs/2509.22917v1)**  
  Authors: Yuelin Xin, Yuheng Liu, Xiaohui Xie, Xinke Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22917v1.pdf)  
  Keywords: mapping, gaussian splatting, 3d reconstruction, ar, efficient, 3d gaussian  
- **[Vision-Language Alignment from Compressed Image Representations using 2D
  Gaussian Splatting](https://arxiv.org/abs/2509.22615v1)**  
  Authors: Yasmine Omri, Connor Ding, Tsachy Weissman, Thierry Tambe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22615v1.pdf)  
  Keywords: semantic, gaussian splatting, fast, ar, compact, efficient, lightweight  
- **[Large Material Gaussian Model for Relightable 3D Generation](https://arxiv.org/abs/2509.22112v1)**  
  Authors: Jingrui Ye, Lingting Zhu, Runze Zhang, Zeyu Hu, Yingda Yin, Lanjiong Li, Lequan Yu, Qingmin Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22112v1.pdf)  
  Keywords: relightable, efficient, lighting, dynamic, gaussian splatting, ar, 3d gaussian, relighting  
- **[PowerGS: Display-Rendering Power Co-Optimization for Neural Rendering in
  Power-Constrained XR Systems](https://arxiv.org/abs/2509.21702v1)**  
  Authors: Weikai Lin, Sushant Kondguli, Carl Marshall, Yuhao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.21702v1.pdf)  
  Keywords: neural rendering, gaussian splatting, ar, efficient, 3d gaussian  
- **[Gaussian splatting holography](https://arxiv.org/abs/2509.20774v1)**  
  Authors: Shuhe Zhang, Liangcai Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20774v1.pdf)  
  Keywords: face, ar, compression, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 160 papers*

- **[DWGS: Enhancing Sparse-View Gaussian Splatting with Hybrid-Loss Depth
  Estimation and Bidirectional Warping](https://arxiv.org/abs/2509.24893v1)**  
  Authors: Yu Ma, Guoliang Wei, Yue Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24893v1.pdf)  
  Keywords: sparse-view, sparse view, gaussian splatting, 3d reconstruction, ar, high-fidelity, 3d gaussian  
- **[DeblurSplat: SfM-free 3D Gaussian Splatting with Event Camera for Robust
  Deblurring](https://arxiv.org/abs/2509.18898v1)**  
  Authors: Pengteng Li, Yunfan Lu, Pinhao Song, Weiyu Guo, Huizai Yao, F. Richard Yu, Hui Xiong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18898v1.pdf)  
  Keywords: motion, dynamic, gaussian splatting, ar, high-fidelity, 3d gaussian  
- **[EmbodiedSplat: Personalized Real-to-Sim-to-Real Navigation with Gaussian
  Splats from a Mobile Device](https://arxiv.org/abs/2509.17430v2)**  
  Authors: Gunjan Chhablani, Xiaomeng Ye, Muhammad Zubair Irshad, Zsolt Kira  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.17430v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gchhablani.github.io/embodied-splat.)  
  Keywords: efficient, gaussian splatting, ar, high-fidelity, 3d gaussian  
- **[FGGS-LiDAR: Ultra-Fast, GPU-Accelerated Simulation from General 3DGS
  Models to LiDAR](https://arxiv.org/abs/2509.17390v1)**  
  Authors: Junzhe Wu, Yufei Jia, Yiyi Yan, Zhixing Chen, Tiao Tan, Zifan Wang, Guangyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.17390v1.pdf)  
  Keywords: robotics, autonomous driving, outdoor, gaussian splatting, fast, ar, high-fidelity, 3d gaussian  
- **[PGSTalker: Real-Time Audio-Driven Talking Head Generation via 3D
  Gaussian Splatting with Pixel-Aware Density Control](https://arxiv.org/abs/2509.16922v1)**  
  Authors: Tianheng Zhu, Yinfeng Yu, Liejun Wang, Fuchun Sun, Wendong Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.16922v1.pdf)  
  Keywords: nerf, avatar, dynamic, gaussian splatting, ar, high-fidelity, 3d gaussian, lightweight, head, deformation  
- **[ConfidentSplat: Confidence-Weighted Depth Fusion for Accurate 3D
  Gaussian Splatting SLAM](https://arxiv.org/abs/2509.16863v1)**  
  Authors: Amanuel T. Dufera, Yuan-Li Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.16863v1.pdf)  
  Keywords: efficient, geometry, slam, dynamic, gaussian splatting, ar, high-fidelity, 3d gaussian  
- **[MedGS: Gaussian Splatting for Multi-Modal 3D Medical Imaging](https://arxiv.org/abs/2509.16806v1)**  
  Authors: Kacper Marzol, Ignacy Kolton, Weronika Smolak-Dyżewska, Joanna Kaleta, Marcin Mazur, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.16806v1.pdf)  
  Keywords: face, medical, gaussian splatting, ar, high-fidelity, efficient  
- **[GS-Scale: Unlocking Large-Scale 3D Gaussian Splatting Training via Host
  Offloading](https://arxiv.org/abs/2509.15645v1)**  
  Authors: Donghyun Lee, Dawoon Jeong, Jae W. Lee, Hongil Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.15645v1.pdf)  
  Keywords: high quality, gaussian splatting, fast, ar, efficient, 3d gaussian  
- **[FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model
  Priors for 3D Monocular Avatar Reconstruction](https://arxiv.org/abs/2509.14739v1)**  
  Authors: Jinlong Fan, Bingyu Hu, Xingguang Li, Yuxiang Yang, Jing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.14739v1.pdf)  
  Keywords: face, human, semantic, avatar, gaussian splatting, ar, high-fidelity, 3d gaussian  
- **[MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for
  High-Fidelity Mapping](https://arxiv.org/abs/2509.14191v1)**  
  Authors: Zhihao Cao, Hanyu Wu, Li Wa Tang, Zizhou Luo, Zihan Zhu, Wei Zhang, Marc Pollefeys, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.14191v1.pdf)  
  Keywords: robotics, slam, mapping, autonomous driving, gaussian splatting, ar, high-fidelity, 3d gaussian  

### Ray Tracing

- **[Differentiable Light Transport with Gaussian Surfels via Adapted
  Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: light transport, lighting, geometry, reflection, global illumination, gaussian splatting, illumination, ar, efficient, relighting  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing
  for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v1)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v1.pdf)  
  Keywords: 4d, dynamic, ray tracing, gaussian splatting, fast, ar  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: face, nerf, lighting, geometry, reflection, ray tracing, gaussian splatting, ar, illumination, high-fidelity, 3d gaussian, relighting  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: face, relightable, shadow, lighting, outdoor, global illumination, dynamic, gaussian splatting, illumination, ar, 3d gaussian, relighting  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: face, lighting, path tracing, dynamic, gaussian splatting, ar, 3d gaussian  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: face, efficient rendering, relightable, efficient, lighting, geometry, gaussian splatting, ar, 3d gaussian, ray marching, relighting  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: real-time rendering, ray tracing, gaussian splatting, ar, high-fidelity, efficient  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v2)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v2.pdf)  
  Keywords: relightable, lighting, human, geometry, avatar, ray tracing, gaussian splatting, fast, shadow, ar, relighting  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: efficient rendering, efficient, lighting, ray tracing, gaussian splatting, ar, 3d gaussian, acceleration, relighting  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: efficient, animation, acceleration, dynamic, gaussian splatting, ar, compact, 3d gaussian, ray marching  

### Relighting

*Showing the latest 50 out of 114 papers*

- **[Large Material Gaussian Model for Relightable 3D Generation](https://arxiv.org/abs/2509.22112v1)**  
  Authors: Jingrui Ye, Lingting Zhu, Runze Zhang, Zeyu Hu, Yingda Yin, Lanjiong Li, Lequan Yu, Qingmin Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22112v1.pdf)  
  Keywords: relightable, efficient, lighting, dynamic, gaussian splatting, ar, 3d gaussian, relighting  
- **[Dynamic Novel View Synthesis in High Dynamic Range](https://arxiv.org/abs/2509.21853v1)**  
  Authors: Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.21853v1.pdf)  
  Keywords: 4d, lighting, mapping, dynamic, gaussian splatting, ar  
- **[Seeing Through Reflections: Advancing 3D Scene Reconstruction in
  Mirror-Containing Environments with Gaussian Splatting](https://arxiv.org/abs/2509.18956v1)**  
  Authors: Zijing Guo, Yunyang Zhao, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18956v1.pdf)  
  Keywords: face, nerf, geometry, mapping, reflection, gaussian splatting, 3d reconstruction, ar, 3d gaussian  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted
  Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: light transport, lighting, geometry, reflection, global illumination, gaussian splatting, illumination, ar, efficient, relighting  
- **[From Restoration to Reconstruction: Rethinking 3D Gaussian Splatting for
  Underwater Scenes](https://arxiv.org/abs/2509.17789v1)**  
  Authors: Guoxi Huang, Haoran Wang, Zipeng Qi, Wenjun Lu, David Bull, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.17789v1.pdf)  
  Keywords: nerf, gaussian splatting, 3d reconstruction, illumination, 3d gaussian, lightweight, ar  
- **[RadarGaussianDet3D: An Efficient and Effective Gaussian-based 3D
  Detector with 4D Automotive Radars](https://arxiv.org/abs/2509.16119v1)**  
  Authors: Weiyi Xiong, Bing Zhu, Tao Huang, Zewei Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.16119v1.pdf)  
  Keywords: 4d, efficient, lighting, autonomous driving, gaussian splatting, fast, ar, 3d gaussian  
- **[Camera Splatting for Continuous View Optimization](https://arxiv.org/abs/2509.15677v1)**  
  Authors: Gahye Lee, Hyomin Kim, Gwangjin Ju, Jooeun Son, Hyejeong Yoon, Seungyong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.15677v1.pdf)  
  Keywords: face, reflection, gaussian splatting, ar, 3d gaussian  
- **[ROSGS: Relightable Outdoor Scenes With Gaussian Splatting](https://arxiv.org/abs/2509.11275v1)**  
  Authors: Lianjun Liao, Chunhui Zhang, Tong Wu, Henglei Lv, Bailin Deng, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.11275v1.pdf)  
  Keywords: nerf, efficient rendering, relightable, efficient, lighting, geometry, outdoor, gaussian splatting, ar, illumination, compact, 3d gaussian, head, relighting  
- **[On the Geometric Accuracy of Implicit and Primitive-based
  Representations Derived from View Rendering Constraints](https://arxiv.org/abs/2509.10241v2)**  
  Authors: Elias De Smijter, Renaud Detry, Christophe De Vleeschouwer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10241v2.pdf)  
  Keywords: lighting, robotics, geometry, gaussian splatting, ar, compact  
- **[DreamLifting: A Plug-in Module Lifting MV Diffusion Models for 3D Asset
  Generation](https://arxiv.org/abs/2509.07435v1)**  
  Authors: Ze-Xin Yin, Jiaxiong Qiu, Liu Liu, Xinjie Wang, Wei Sui, Zhizhong Su, Jian Yang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.07435v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zx-yin.github.io/dreamlifting/.)  
  Keywords: relightable, geometry, gaussian splatting, ar, efficient, lightweight  

### SLAM

*Showing the latest 50 out of 150 papers*

- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: nerf, efficient, survey, slam, understanding, neural rendering, gaussian splatting, fast, ar, 3d gaussian  
- **[Learning Unified Representation of 3D Gaussian Splatting](https://arxiv.org/abs/2509.22917v1)**  
  Authors: Yuelin Xin, Yuheng Liu, Xiaohui Xie, Xinke Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22917v1.pdf)  
  Keywords: mapping, gaussian splatting, 3d reconstruction, ar, efficient, 3d gaussian  
- **[Dynamic Novel View Synthesis in High Dynamic Range](https://arxiv.org/abs/2509.21853v1)**  
  Authors: Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.21853v1.pdf)  
  Keywords: 4d, lighting, mapping, dynamic, gaussian splatting, ar  
- **[Seeing Through Reflections: Advancing 3D Scene Reconstruction in
  Mirror-Containing Environments with Gaussian Splatting](https://arxiv.org/abs/2509.18956v1)**  
  Authors: Zijing Guo, Yunyang Zhao, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18956v1.pdf)  
  Keywords: face, nerf, geometry, mapping, reflection, gaussian splatting, 3d reconstruction, ar, 3d gaussian  
- **[ConfidentSplat: Confidence-Weighted Depth Fusion for Accurate 3D
  Gaussian Splatting SLAM](https://arxiv.org/abs/2509.16863v1)**  
  Authors: Amanuel T. Dufera, Yuan-Li Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.16863v1.pdf)  
  Keywords: efficient, geometry, slam, dynamic, gaussian splatting, ar, high-fidelity, 3d gaussian  
- **[MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for
  High-Fidelity Mapping](https://arxiv.org/abs/2509.14191v1)**  
  Authors: Zhihao Cao, Hanyu Wu, Li Wa Tang, Zizhou Luo, Zihan Zhu, Wei Zhang, Marc Pollefeys, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.14191v1.pdf)  
  Keywords: robotics, slam, mapping, autonomous driving, gaussian splatting, ar, high-fidelity, 3d gaussian  
- **[MemGS: Memory-Efficient Gaussian Splatting for Real-Time SLAM](https://arxiv.org/abs/2509.13536v1)**  
  Authors: Yinlong Bai, Hongxin Zhang, Sheng Zhong, Junkai Niu, Hai Li, Yijia He, Yi Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.13536v1.pdf)  
  Keywords: face, slam, gaussian splatting, ar, efficient, 3d gaussian  
- **[On the Skinning of Gaussian Avatars](https://arxiv.org/abs/2509.11411v1)**  
  Authors: Nikolaos Zioulis, Nikolaos Kotarelas, Georgios Albanis, Spyridon Thermos, Anargyros Chatzitofis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.11411v1.pdf)  
  Keywords: human, mapping, avatar, gaussian splatting, fast, ar, efficient, deformation  
- **[Real-time Photorealistic Mapping for Situational Awareness in Robot
  Teleoperation](https://arxiv.org/abs/2509.06433v2)**  
  Authors: Ian Page, Pierre Susbielle, Olivier Aycard, Pierre-Brice Wieber  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06433v2.pdf)  
  Keywords: slam, mapping, understanding, gaussian splatting, ar, efficient  
- **[DyPho-SLAM : Real-time Photorealistic SLAM in Dynamic Environments](https://arxiv.org/abs/2509.00741v1)**  
  Authors: Yi Liu, Keyu Fan, Bin Lan, Houde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.00741v1.pdf)  
  Keywords: tracking, slam, mapping, localization, dynamic, gaussian splatting, ar, high-fidelity, efficient  

### Scene Understanding

*Showing the latest 50 out of 196 papers*

- **[CrashSplat: 2D to 3D Vehicle Damage Segmentation in Gaussian Splatting](https://arxiv.org/abs/2509.23947v1)**  
  Authors: Dragoş-Andrei Chileban, Andrei-Ştefan Bulzan, Cosmin Cernǎzanu-Glǎvan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23947v1.pdf)  
  Keywords: motion, gaussian splatting, fast, 3d reconstruction, segmentation, 3d gaussian, ar  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: nerf, efficient, survey, slam, understanding, neural rendering, gaussian splatting, fast, ar, 3d gaussian  
- **[Vision-Language Alignment from Compressed Image Representations using 2D
  Gaussian Splatting](https://arxiv.org/abs/2509.22615v1)**  
  Authors: Yasmine Omri, Connor Ding, Tsachy Weissman, Thierry Tambe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22615v1.pdf)  
  Keywords: semantic, gaussian splatting, fast, ar, compact, efficient, lightweight  
- **[Polysemous Language Gaussian Splatting via Matching-based Mask Lifting](https://arxiv.org/abs/2509.22225v1)**  
  Authors: Jiayu Ding, Xinpeng Liu, Zhiyi Pan, Shiqiang Long, Ge Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22225v1.pdf)  
  Keywords: semantic, understanding, gaussian splatting, segmentation, 3d gaussian, ar  
- **[4D Driving Scene Generation With Stereo Forcing](https://arxiv.org/abs/2509.20251v1)**  
  Authors: Hao Lu, Zhuang Ma, Guangfeng Jiang, Wenhang Ge, Bohan Li, Yuzhan Cai, Wenzhao Zheng, Yunpeng Zhang, Yingcong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20251v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiangxb98.github.io/PhiGensis}{PhiGensis}.)  
  Keywords: 4d, semantic, geometry, motion, dynamic, gaussian splatting, ar  
- **[SINGER: An Onboard Generalist Vision-Language Navigation Policy for
  Drones](https://arxiv.org/abs/2509.18610v1)**  
  Authors: Maximilian Adang, JunEn Low, Ola Shorinwa, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18610v1.pdf)  
  Keywords: semantic, gaussian splatting, ar, efficient, lightweight  
- **[Event-guided 3D Gaussian Splatting for Dynamic Human and Scene
  Reconstruction](https://arxiv.org/abs/2509.18566v1)**  
  Authors: Xiaoting Yin, Hao Shi, Kailun Yang, Jiajun Zhai, Shangwei Guo, Lin Wang, Kaiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18566v1.pdf)  
  Keywords: animation, human, semantic, motion, dynamic, gaussian splatting, fast, ar, 3d gaussian, deformation  
- **[ST-GS: Vision-Based 3D Semantic Occupancy Prediction with
  Spatial-Temporal Gaussian Splatting](https://arxiv.org/abs/2509.16552v1)**  
  Authors: Xiaoyang Yan, Muleilan Pei, Shaojie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.16552v1.pdf)  
  Keywords: semantic, geometry, understanding, autonomous driving, gaussian splatting, ar, head  
- **[FingerSplat: Contactless Fingerprint 3D Reconstruction and Generation
  based on 3D Gaussian Splatting](https://arxiv.org/abs/2509.15648v1)**  
  Authors: Yuwei Jia, Yutang Lu, Zhe Cui, Fei Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.15648v1.pdf)  
  Keywords: recognition, gaussian splatting, 3d reconstruction, ar, 3d gaussian  
- **[MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2509.15548v3)**  
  Authors: Deming Li, Kaiwen Jiang, Yutao Tang, Ravi Ramamoorthi, Rama Chellappa, Cheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.15548v3.pdf)  
  Keywords: nerf, semantic, geometry, sparse-view, motion, gaussian splatting, ar, 3d gaussian  



## Classic Papers
- **[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)** (SIGGRAPH 2023)  
  Authors: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis  
  Code: 🔗 [GitHub](https://github.com/graphdeco-inria/gaussian-splatting)  
  Keywords: Real-time Rendering, Neural Rendering, Point-based Graphics

## Open Source Projects
- [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) - Original implementation of 3D Gaussian Splatting
- [taichi-3d-gaussian-splatting](https://github.com/wanmeihuali/taichi-3d-gaussian-splatting) - 3D Gaussian Splatting implemented in Taichi

## Applications
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering Demo](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) - Online Demo

## Tutorials & Blogs
- [Introduction to 3D Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting) - Official Tutorial

## 📋 Project Features

### 🛠️ Core Features
- **Configurable Search System**: Customize search keywords through `data/search_config.json` for targeted paper collection
- **Automated Paper Collection**: Daily automatic crawling of latest Gaussian Splatting related papers
- **Intelligent Classification System**: Automatically categorize papers into different topics (Acceleration, Applications, Dynamic Scenes, etc.)
- **Flexible Search Scopes**: Support for abstract-only, title-only, or combined searches
- **Cross-Platform Compatibility**: Support for Windows/Linux/macOS with automatic environment detection

### 🛠️ Technical Features
- **Robust Error Handling**: Multi-layer retry and fallback strategies ensure stable operation
- **GitHub Actions Integration**: Automated CI/CD workflows
- **Real-time Update Mechanism**: Daily automatic paper data updates
- **Detailed Logging**: Comprehensive logging for debugging and monitoring

### 📚 Documentation System
- **User Guides**: Detailed configuration and usage instructions
- **Update Logs**: [News.md](News.md) - Records all important updates
- **Validation Reports**: Automated testing and validation results

## 🚀 Quick Start

### Customize Search Keywords
Edit `data/search_config.json` to target specific research areas:

```json
{
  "search_config": {
    "both_abstract_and_title": [
      "gaussian splatting",
      "3d gaussian",
      "neural rendering"
    ],
    "abstract_only": [
      "volumetric rendering",
      "point cloud reconstruction"
    ],
    "title_only": [
      "real-time rendering",
      "3D reconstruction"
    ]
  }
}
```

### Run the Crawler
```bash
# Basic usage
python scripts/arxiv_crawler.py

# Custom number of papers
python scripts/arxiv_crawler.py --max-results 200

# Validate configuration
python scripts/validate_search_config.py
```

## Contribution Guidelines
Feel free to submit Pull Requests to improve this list! Please follow these formats:
- Paper entry format: `**[Paper Title](link)** - Brief description`
- Project entry format: `[Project Name](link) - Project description`

## License
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) 