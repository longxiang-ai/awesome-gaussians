# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-12-22 01:00:16

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

- [3DGS Surveys](#3dgs-surveys) (22 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (252 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (347 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (401 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (81 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (347 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (72 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (406 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (195 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (17 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (127 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (147 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (206 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197v1)**  
  Authors: Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07197v1.pdf)  
  Keywords: compression, 4d, compact, dynamic, gaussian splatting, 3d reconstruction, survey, efficient, ar, high-fidelity, 3d gaussian  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v1)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v1.pdf)  
  Keywords: robotics, semantic, nerf, mapping, gaussian splatting, slam, survey, ar, localization, 3d gaussian, understanding  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: localization, robotics, semantic, mapping, gaussian splatting, slam, survey, efficient, ar, high-fidelity, 3d gaussian  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: fast, motion, nerf, 4d, gaussian splatting, geometry, survey, ar, 3d gaussian  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: avatar, efficient rendering, animation, face, lighting, gaussian splatting, 3d reconstruction, survey, efficient, ar, 3d gaussian, real-time rendering  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: nerf, lightweight, human, gaussian splatting, survey, efficient, ar, understanding  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: fast, nerf, gaussian splatting, slam, survey, efficient, ar, 3d gaussian, neural rendering, understanding  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: semantic, nerf, compact, lighting, gaussian splatting, segmentation, survey, ar, high-fidelity, 3d gaussian, understanding  
- **[A Study of the Framework and Real-World Applications of Language Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: robotics, semantic, nerf, gaussian splatting, survey, efficient, ar, 3d gaussian, understanding  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: robotics, nerf, human, gaussian splatting, survey, ar, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 252 papers*

- **[Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation](https://arxiv.org/abs/2512.16893v1)**  
  Authors: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16893v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/instant4d)  
  Keywords: head, fast, motion, lightweight, animation, 4d, face, gaussian splatting, efficient, ar, avatar  
- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: fast, nerf, face, ray tracing, gaussian splatting, ar, 3d gaussian  
- **[Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering](https://arxiv.org/abs/2512.15711v1)**  
  Authors: Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Tomas Simon, Forrest Iandola, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15711v1.pdf)  
  Keywords: head, efficient rendering, face, gaussian splatting, 3d gaussian, efficient, ar, avatar  
- **[VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments](https://arxiv.org/abs/2512.15258v1)**  
  Authors: Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Yuxin Fan, Wenjun Li, Xin Zhou, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15258v1.pdf)  
  Keywords: fast, lightweight, gaussian splatting, efficient, ar, high-fidelity, 3d gaussian  
- **[HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis](https://arxiv.org/abs/2512.14352v1)**  
  Authors: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Caixia Yan, Haipeng Du, yugui xie, Yu-Hui Wen, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14352v1.pdf)  
  Keywords: nerf, compact, dynamic, gaussian splatting, deformation, efficient, ar, 3d gaussian, vr, real-time rendering  
- **[Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries](https://arxiv.org/abs/2512.13796v1)**  
  Authors: Victor Rong, Jan Held, Victor Chu, Daniel Rebain, Marc Van Droogenbroeck, Kiriakos N. Kutulakos, Andrea Tagliasacchi, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13796v1.pdf)  
  Keywords: fast, outdoor, compact, gaussian splatting, geometry, ar, 3d gaussian  
- **[Fast 2DGS: Efficient Image Representation with Deep Gaussian Prior](https://arxiv.org/abs/2512.12774v1)**  
  Authors: Hao Wang, Ashish Bastola, Chaoyi Zhou, Wenhui Zhu, Xiwen Chen, Xuanzhao Dong, Siyu Huang, Abolfazl Razi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.12774v1.pdf)  
  Keywords: fast, lightweight, gaussian splatting, efficient, ar, high-fidelity, real-time rendering  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: fast, ray tracing, compact, gaussian splatting, ar, high-fidelity, 3d gaussian, real-time rendering  
- **[Lightweight 3D Gaussian Splatting Compression via Video Codec](https://arxiv.org/abs/2512.11186v1)**  
  Authors: Qi Yang, Geert Van Der Auwera, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11186v1.pdf)  
  Keywords: fast, lightweight, compression, gaussian splatting, ar, 3d gaussian  
- **[GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](https://arxiv.org/abs/2512.10939v1)**  
  Authors: Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10939v1.pdf)  
  Keywords: fast, tracking, mapping, gaussian splatting, head, ar, avatar  

### Applications

*Showing the latest 50 out of 995 papers*

- **[Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation](https://arxiv.org/abs/2512.16893v1)**  
  Authors: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16893v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/instant4d)  
  Keywords: head, fast, motion, lightweight, animation, 4d, face, gaussian splatting, efficient, ar, avatar  
- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: fast, nerf, face, ray tracing, gaussian splatting, ar, 3d gaussian  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: semantic, nerf, human, face, lighting, gaussian splatting, segmentation, geometry, ar, high-fidelity, relightable  
- **[Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering](https://arxiv.org/abs/2512.15711v1)**  
  Authors: Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Tomas Simon, Forrest Iandola, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15711v1.pdf)  
  Keywords: head, efficient rendering, face, gaussian splatting, 3d gaussian, efficient, ar, avatar  
- **[Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2512.15508v1)**  
  Authors: Arthur Moreau, Richard Shaw, Michal Nazarczuk, Jisu Shin, Thomas Tanay, Zhensong Zhang, Songcen Xu, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15508v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, efficient, ar, 3d gaussian  
- **[VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments](https://arxiv.org/abs/2512.15258v1)**  
  Authors: Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Yuxin Fan, Wenjun Li, Xin Zhou, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15258v1.pdf)  
  Keywords: fast, lightweight, gaussian splatting, efficient, ar, high-fidelity, 3d gaussian  
- **[MVGSR: Multi-View Consistent 3D Gaussian Super-Resolution via Epipolar Guidance](https://arxiv.org/abs/2512.15048v1)**  
  Authors: Kaizhe Zhang, Shinan Chen, Qian Zhao, Weizhan Zhang, Caixia Yan, Yudeng Xin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15048v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian  
- **[Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos](https://arxiv.org/abs/2512.14406v1)**  
  Authors: Le Jiang, Shaotong Zhu, Yedi Luo, Shayda Moezzi, Sarah Ostadabbas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14406v1.pdf)  
  Keywords: nerf, dynamic, gaussian splatting, ar  
- **[HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis](https://arxiv.org/abs/2512.14352v1)**  
  Authors: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Caixia Yan, Haipeng Du, yugui xie, Yu-Hui Wen, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14352v1.pdf)  
  Keywords: nerf, compact, dynamic, gaussian splatting, deformation, efficient, ar, 3d gaussian, vr, real-time rendering  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: illumination, urban scene, face, gaussian splatting, 3d reconstruction, geometry, efficient, ar, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 347 papers*

- **[Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation](https://arxiv.org/abs/2512.16893v1)**  
  Authors: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16893v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/instant4d)  
  Keywords: head, fast, motion, lightweight, animation, 4d, face, gaussian splatting, efficient, ar, avatar  
- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: fast, nerf, face, ray tracing, gaussian splatting, ar, 3d gaussian  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: semantic, nerf, human, face, lighting, gaussian splatting, segmentation, geometry, ar, high-fidelity, relightable  
- **[Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering](https://arxiv.org/abs/2512.15711v1)**  
  Authors: Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Tomas Simon, Forrest Iandola, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15711v1.pdf)  
  Keywords: head, efficient rendering, face, gaussian splatting, 3d gaussian, efficient, ar, avatar  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: illumination, urban scene, face, gaussian splatting, 3d reconstruction, geometry, efficient, ar, 3d gaussian  
- **[GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](https://arxiv.org/abs/2512.10939v1)**  
  Authors: Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10939v1.pdf)  
  Keywords: fast, tracking, mapping, gaussian splatting, head, ar, avatar  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: face, mapping, gaussian splatting, deformation, ar, high-fidelity  
- **[Splatent: Splatting Diffusion Latents for Novel View Synthesis](https://arxiv.org/abs/2512.09923v1)**  
  Authors: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09923v1.pdf)  
  Keywords: sparse-view, efficient rendering, face, gaussian splatting, 3d reconstruction, efficient, ar, 3d gaussian  
- **[YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos](https://arxiv.org/abs/2512.09903v1)**  
  Authors: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09903v1.pdf)  
  Keywords: recognition, human, compact, mapping, gaussian splatting, ar, localization, 3d gaussian  
- **[Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video](https://arxiv.org/abs/2512.09335v2)**  
  Authors: Seonghwa Choi, Moonkyeong Choi, Mingyu Jang, Jaekyung Kim, Jianfei Cai, Wen-Huang Cheng, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09335v2.pdf)  
  Keywords: motion, body, nerf, avatar, human, relighting, lighting, gaussian splatting, dynamic, deformation, ar, high-fidelity, 3d gaussian, relightable  

### Dynamic Scene

*Showing the latest 50 out of 401 papers*

- **[Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation](https://arxiv.org/abs/2512.16893v1)**  
  Authors: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16893v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/instant4d)  
  Keywords: head, fast, motion, lightweight, animation, 4d, face, gaussian splatting, efficient, ar, avatar  
- **[Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos](https://arxiv.org/abs/2512.14406v1)**  
  Authors: Le Jiang, Shaotong Zhu, Yedi Luo, Shayda Moezzi, Sarah Ostadabbas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14406v1.pdf)  
  Keywords: nerf, dynamic, gaussian splatting, ar  
- **[HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis](https://arxiv.org/abs/2512.14352v1)**  
  Authors: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Caixia Yan, Haipeng Du, yugui xie, Yu-Hui Wen, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14352v1.pdf)  
  Keywords: nerf, compact, dynamic, gaussian splatting, deformation, efficient, ar, 3d gaussian, vr, real-time rendering  
- **[Prior-Enhanced Gaussian Splatting for Dynamic Scene Reconstruction from Casual Video](https://arxiv.org/abs/2512.11356v1)**  
  Authors: Meng-Li Shih, Ying-Huan Chen, Yu-Lun Liu, Brian Curless  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11356v1.pdf)  
  Keywords: motion, dynamic, gaussian splatting, segmentation, geometry, ar  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: face, mapping, gaussian splatting, deformation, ar, high-fidelity  
- **[Neural Hamiltonian Deformation Fields for Dynamic Scene Rendering](https://arxiv.org/abs/2512.10424v1)**  
  Authors: Hai-Long Qin, Sixian Wang, Guo Lu, Jincheng Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10424v1.pdf)  
  Keywords: motion, mapping, dynamic, gaussian splatting, deformation, ar  
- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v1)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: motion, sparse view, gaussian splatting, 3d reconstruction, ar, high-fidelity, 3d gaussian  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: reflection, ray tracing, dynamic, gaussian splatting, 3d reconstruction, geometry, ar, high-fidelity  
- **[ReMoSPLAT: Reactive Mobile Manipulation Control on a Gaussian Splat](https://arxiv.org/abs/2512.09656v1)**  
  Authors: Nicolas Marticorena, Tobias Fischer, Niko Suenderhauf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09656v1.pdf)  
  Keywords: ar, motion, efficient  
- **[Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video](https://arxiv.org/abs/2512.09335v2)**  
  Authors: Seonghwa Choi, Moonkyeong Choi, Mingyu Jang, Jaekyung Kim, Jianfei Cai, Wen-Huang Cheng, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09335v2.pdf)  
  Keywords: motion, body, nerf, avatar, human, relighting, lighting, gaussian splatting, dynamic, deformation, ar, high-fidelity, 3d gaussian, relightable  

### Few-shot

*Showing the latest 50 out of 81 papers*

- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v1)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: motion, sparse view, gaussian splatting, 3d reconstruction, ar, high-fidelity, 3d gaussian  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: light transport, sparse-view, relighting, lighting, gaussian splatting, segmentation, geometry, ar  
- **[Splatent: Splatting Diffusion Latents for Novel View Synthesis](https://arxiv.org/abs/2512.09923v1)**  
  Authors: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09923v1.pdf)  
  Keywords: sparse-view, efficient rendering, face, gaussian splatting, 3d reconstruction, efficient, ar, 3d gaussian  
- **[Tessellation GS: Neural Mesh Gaussians for Robust Monocular Reconstruction of Dynamic Objects](https://arxiv.org/abs/2512.07381v1)**  
  Authors: Shuohan Tao, Boyao Zhou, Hanzhang Tu, Yuwang Wang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07381v1.pdf)  
  Keywords: sparse-view, face, dynamic, gaussian splatting, deformation, ar, 3d gaussian  
- **[MuSASplat: Efficient Sparse-View 3D Gaussian Splats via Lightweight Multi-Scale Adaptation](https://arxiv.org/abs/2512.07165v1)**  
  Authors: Muyu Xu, Fangneng Zhan, Xiaoqin Zhang, Ling Shao, Shijian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07165v1.pdf)  
  Keywords: head, sparse-view, lightweight, gaussian splatting, efficient, ar, 3d gaussian  
- **[C3G: Learning Compact 3D Representations with 2K Gaussians](https://arxiv.org/abs/2512.04021v1)**  
  Authors: Honggyu An, Jaewoo Jung, Mungyeom Kim, Sunghwan Hong, Chaehyun Kim, Kazumi Fukuda, Minkyeong Jeon, Jisang Han, Takuya Narihira, Hyuna Ko, Junsu Kim, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04021v1.pdf)  
  Keywords: head, sparse view, compact, gaussian splatting, segmentation, efficient, ar, 3d gaussian, understanding  
- **[Cross-Temporal 3D Gaussian Splatting for Sparse-View Guided Scene Update](https://arxiv.org/abs/2512.00534v1)**  
  Authors: Zeyuan An, Yanghang Xiao, Zhiying Leng, Frederick W. B. Li, Xiaohui Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00534v1.pdf)  
  Keywords: sparse-view, sparse view, gaussian splatting, efficient, ar, 3d gaussian  
- **[Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views](https://arxiv.org/abs/2512.00255v1)**  
  Authors: Kunwar Maheep Singh, Jianchun Chen, Vladislav Golyanik, Stephan J. Garbin, Thabo Beeler, Rishabh Dabral, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/RHC/)  
  Keywords: motion, sparse-view, body, illumination, sparse view, human, tracking, relighting, lighting, dynamic, geometry, efficient, ar, 3d gaussian, relightable  
- **[Observer Actor: Active Vision Imitation Learning with Sparse View Gaussian Splatting](https://arxiv.org/abs/2511.18140v1)**  
  Authors: Yilong Wang, Cheng Qian, Ruomeng Fan, Edward Johns  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18140v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://obact.github.io.)  
  Keywords: sparse view, dynamic, gaussian splatting, ar, 3d gaussian  
- **[Frequency-Adaptive Sharpness Regularization for Improving 3D Gaussian Splatting Generalization](https://arxiv.org/abs/2511.17918v1)**  
  Authors: Youngsik Yun, Dongjun Gu, Youngjung Uh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bbangsik13.github.io/FASR.)  
  Keywords: few-shot, ar, gaussian splatting, 3d gaussian  

### Geometry Reconstruction

*Showing the latest 50 out of 347 papers*

- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: semantic, nerf, human, face, lighting, gaussian splatting, segmentation, geometry, ar, high-fidelity, relightable  
- **[Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2512.15508v1)**  
  Authors: Arthur Moreau, Richard Shaw, Michal Nazarczuk, Jisu Shin, Thomas Tanay, Zhensong Zhang, Songcen Xu, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15508v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, efficient, ar, 3d gaussian  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: illumination, urban scene, face, gaussian splatting, 3d reconstruction, geometry, efficient, ar, 3d gaussian  
- **[GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants](https://arxiv.org/abs/2512.14087v1)**  
  Authors: Yang Yang, Risa Shinoda, Hiroaki Santo, Fumio Okura  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14087v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, geometry, ar, high-fidelity, 3d gaussian  
- **[Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries](https://arxiv.org/abs/2512.13796v1)**  
  Authors: Victor Rong, Jan Held, Victor Chu, Daniel Rebain, Marc Van Droogenbroeck, Kiriakos N. Kutulakos, Andrea Tagliasacchi, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13796v1.pdf)  
  Keywords: fast, outdoor, compact, gaussian splatting, geometry, ar, 3d gaussian  
- **[Prior-Enhanced Gaussian Splatting for Dynamic Scene Reconstruction from Casual Video](https://arxiv.org/abs/2512.11356v1)**  
  Authors: Meng-Li Shih, Ying-Huan Chen, Yu-Lun Liu, Brian Curless  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11356v1.pdf)  
  Keywords: motion, dynamic, gaussian splatting, segmentation, geometry, ar  
- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v1)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: motion, sparse view, gaussian splatting, 3d reconstruction, ar, high-fidelity, 3d gaussian  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: reflection, ray tracing, dynamic, gaussian splatting, 3d reconstruction, geometry, ar, high-fidelity  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: light transport, sparse-view, relighting, lighting, gaussian splatting, segmentation, geometry, ar  
- **[Splatent: Splatting Diffusion Latents for Novel View Synthesis](https://arxiv.org/abs/2512.09923v1)**  
  Authors: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09923v1.pdf)  
  Keywords: sparse-view, efficient rendering, face, gaussian splatting, 3d reconstruction, efficient, ar, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 72 papers*

- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: illumination, urban scene, face, gaussian splatting, 3d reconstruction, geometry, efficient, ar, 3d gaussian  
- **[Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries](https://arxiv.org/abs/2512.13796v1)**  
  Authors: Victor Rong, Jan Held, Victor Chu, Daniel Rebain, Marc Van Droogenbroeck, Kiriakos N. Kutulakos, Andrea Tagliasacchi, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13796v1.pdf)  
  Keywords: fast, outdoor, compact, gaussian splatting, geometry, ar, 3d gaussian  
- **[Flux4D: Flow-based Unsupervised 4D Reconstruction](https://arxiv.org/abs/2512.03210v1)**  
  Authors: Jingkang Wang, Henry Che, Yun Chen, Ze Yang, Lily Goli, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03210v1.pdf)  
  Keywords: motion, robotics, nerf, outdoor, 4d, dynamic, gaussian splatting, efficient, ar, 3d gaussian  
- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: outdoor, gaussian splatting, 3d reconstruction, geometry, ar, 3d gaussian, understanding  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: fast, semantic, outdoor, gaussian splatting, geometry, ar  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: semantic, illumination, outdoor, face, lighting, relighting, gaussian splatting, segmentation, geometry, efficient, ar, high-fidelity  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: outdoor, gaussian splatting, geometry, ar, high-fidelity, 3d gaussian  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: autonomous driving, urban scene, human, 4d, dynamic, gaussian splatting, ar  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: fast, gaussian splatting, head, ar, 3d gaussian, large scene  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: motion, outdoor, mapping, gaussian splatting, slam, geometry, ar, 3d gaussian, understanding  

### Model Compression

*Showing the latest 50 out of 406 papers*

- **[Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation](https://arxiv.org/abs/2512.16893v1)**  
  Authors: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16893v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/instant4d)  
  Keywords: head, fast, motion, lightweight, animation, 4d, face, gaussian splatting, efficient, ar, avatar  
- **[Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering](https://arxiv.org/abs/2512.15711v1)**  
  Authors: Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Tomas Simon, Forrest Iandola, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15711v1.pdf)  
  Keywords: head, efficient rendering, face, gaussian splatting, 3d gaussian, efficient, ar, avatar  
- **[Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2512.15508v1)**  
  Authors: Arthur Moreau, Richard Shaw, Michal Nazarczuk, Jisu Shin, Thomas Tanay, Zhensong Zhang, Songcen Xu, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15508v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, efficient, ar, 3d gaussian  
- **[VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments](https://arxiv.org/abs/2512.15258v1)**  
  Authors: Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Yuxin Fan, Wenjun Li, Xin Zhou, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15258v1.pdf)  
  Keywords: fast, lightweight, gaussian splatting, efficient, ar, high-fidelity, 3d gaussian  
- **[HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis](https://arxiv.org/abs/2512.14352v1)**  
  Authors: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Caixia Yan, Haipeng Du, yugui xie, Yu-Hui Wen, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14352v1.pdf)  
  Keywords: nerf, compact, dynamic, gaussian splatting, deformation, efficient, ar, 3d gaussian, vr, real-time rendering  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: illumination, urban scene, face, gaussian splatting, 3d reconstruction, geometry, efficient, ar, 3d gaussian  
- **[Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere](https://arxiv.org/abs/2512.14180v1)**  
  Authors: Francesco Di Sario, Daniel Rebain, Dor Verbin, Marco Grangetto, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14180v1.pdf)  
  Keywords: reflection, gaussian splatting, efficient, ar, 3d gaussian  
- **[ASAP-Textured Gaussians: Enhancing Textured Gaussians with Adaptive Sampling and Anisotropic Parameterization](https://arxiv.org/abs/2512.14039v1)**  
  Authors: Meng Wei, Cheng Zhang, Jianmin Zheng, Hamid Rezatofighi, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14039v1.pdf)  
  Keywords: gaussian splatting, efficient, ar, high-fidelity, 3d gaussian  
- **[Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries](https://arxiv.org/abs/2512.13796v1)**  
  Authors: Victor Rong, Jan Held, Victor Chu, Daniel Rebain, Marc Van Droogenbroeck, Kiriakos N. Kutulakos, Andrea Tagliasacchi, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13796v1.pdf)  
  Keywords: fast, outdoor, compact, gaussian splatting, geometry, ar, 3d gaussian  
- **[Computer vision training dataset generation for robotic environments using Gaussian splatting](https://arxiv.org/abs/2512.13411v1)**  
  Authors: Patryk Niżeniec, Marcin Iwanowski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13411v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, segmentation, efficient, ar, shadow  

### Quality Enhancement

*Showing the latest 50 out of 195 papers*

- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: semantic, nerf, human, face, lighting, gaussian splatting, segmentation, geometry, ar, high-fidelity, relightable  
- **[VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments](https://arxiv.org/abs/2512.15258v1)**  
  Authors: Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Yuxin Fan, Wenjun Li, Xin Zhou, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15258v1.pdf)  
  Keywords: fast, lightweight, gaussian splatting, efficient, ar, high-fidelity, 3d gaussian  
- **[GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants](https://arxiv.org/abs/2512.14087v1)**  
  Authors: Yang Yang, Risa Shinoda, Hiroaki Santo, Fumio Okura  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14087v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, geometry, ar, high-fidelity, 3d gaussian  
- **[ASAP-Textured Gaussians: Enhancing Textured Gaussians with Adaptive Sampling and Anisotropic Parameterization](https://arxiv.org/abs/2512.14039v1)**  
  Authors: Meng Wei, Cheng Zhang, Jianmin Zheng, Hamid Rezatofighi, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14039v1.pdf)  
  Keywords: gaussian splatting, efficient, ar, high-fidelity, 3d gaussian  
- **[Fast 2DGS: Efficient Image Representation with Deep Gaussian Prior](https://arxiv.org/abs/2512.12774v1)**  
  Authors: Hao Wang, Ashish Bastola, Chaoyi Zhou, Wenhui Zhu, Xiwen Chen, Xuanzhao Dong, Siyu Huang, Abolfazl Razi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.12774v1.pdf)  
  Keywords: fast, lightweight, gaussian splatting, efficient, ar, high-fidelity, real-time rendering  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: fast, ray tracing, compact, gaussian splatting, ar, high-fidelity, 3d gaussian, real-time rendering  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: face, mapping, gaussian splatting, deformation, ar, high-fidelity  
- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v1)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: motion, sparse view, gaussian splatting, 3d reconstruction, ar, high-fidelity, 3d gaussian  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: reflection, ray tracing, dynamic, gaussian splatting, 3d reconstruction, geometry, ar, high-fidelity  
- **[Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video](https://arxiv.org/abs/2512.09335v2)**  
  Authors: Seonghwa Choi, Moonkyeong Choi, Mingyu Jang, Jaekyung Kim, Jianfei Cai, Wen-Huang Cheng, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09335v2.pdf)  
  Keywords: motion, body, nerf, avatar, human, relighting, lighting, gaussian splatting, dynamic, deformation, ar, high-fidelity, 3d gaussian, relightable  

### Ray Tracing

- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: fast, nerf, face, ray tracing, gaussian splatting, ar, 3d gaussian  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: fast, ray tracing, compact, gaussian splatting, ar, high-fidelity, 3d gaussian, real-time rendering  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: reflection, ray tracing, dynamic, gaussian splatting, 3d reconstruction, geometry, ar, high-fidelity  
- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: illumination, reflection, ray tracing, gaussian splatting, geometry, ar  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: ray marching, gaussian splatting, geometry, efficient, ar, 3d gaussian  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: light transport, real-time rendering, face, ray tracing, lighting, gaussian splatting, efficient, ar, shadow, relightable  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: light transport, illumination, reflection, relighting, lighting, gaussian splatting, global illumination, geometry, efficient, ar  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v2)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v2.pdf)  
  Keywords: fast, 4d, ray tracing, dynamic, gaussian splatting, ar  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: illumination, nerf, reflection, face, ray tracing, relighting, lighting, gaussian splatting, geometry, ar, high-fidelity, 3d gaussian  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: illumination, outdoor, face, relighting, lighting, gaussian splatting, shadow, global illumination, dynamic, ar, 3d gaussian, relightable  

### Relighting

*Showing the latest 50 out of 127 papers*

- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: semantic, nerf, human, face, lighting, gaussian splatting, segmentation, geometry, ar, high-fidelity, relightable  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: illumination, urban scene, face, gaussian splatting, 3d reconstruction, geometry, efficient, ar, 3d gaussian  
- **[Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere](https://arxiv.org/abs/2512.14180v1)**  
  Authors: Francesco Di Sario, Daniel Rebain, Dor Verbin, Marco Grangetto, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14180v1.pdf)  
  Keywords: reflection, gaussian splatting, efficient, ar, 3d gaussian  
- **[Computer vision training dataset generation for robotic environments using Gaussian splatting](https://arxiv.org/abs/2512.13411v1)**  
  Authors: Patryk Niżeniec, Marcin Iwanowski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13411v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, segmentation, efficient, ar, shadow  
- **[Light Field Based 6DoF Tracking of Previously Unobserved Objects](https://arxiv.org/abs/2512.13007v1)**  
  Authors: Nikolai Goncharov, James L. Gray, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13007v1.pdf)  
  Keywords: autonomous driving, robotics, semantic, reflection, tracking, ar  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: reflection, ray tracing, dynamic, gaussian splatting, 3d reconstruction, geometry, ar, high-fidelity  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: light transport, sparse-view, relighting, lighting, gaussian splatting, segmentation, geometry, ar  
- **[Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video](https://arxiv.org/abs/2512.09335v2)**  
  Authors: Seonghwa Choi, Moonkyeong Choi, Mingyu Jang, Jaekyung Kim, Jianfei Cai, Wen-Huang Cheng, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09335v2.pdf)  
  Keywords: motion, body, nerf, avatar, human, relighting, lighting, gaussian splatting, dynamic, deformation, ar, high-fidelity, 3d gaussian, relightable  
- **[GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars](https://arxiv.org/abs/2512.09162v1)**  
  Authors: Kelian Baert, Mae Younes, Francois Bourel, Marc Christie, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09162v1.pdf)  
  Keywords: head, mapping, relighting, lighting, gaussian splatting, geometry, efficient, ar, avatar, relightable  
- **[HybridSplat: Fast Reflection-baked Gaussian Tracing using Hybrid Splatting](https://arxiv.org/abs/2512.08334v2)**  
  Authors: Chang Liu, Hongliang Yuan, Lianghao Zhang, Sichao Wang, Jianwei Guo, Shi-Sheng Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08334v2.pdf)  
  Keywords: fast, nerf, acceleration, reflection, face, gaussian splatting, ar, high-fidelity, 3d gaussian  

### SLAM

*Showing the latest 50 out of 147 papers*

- **[Light Field Based 6DoF Tracking of Previously Unobserved Objects](https://arxiv.org/abs/2512.13007v1)**  
  Authors: Nikolai Goncharov, James L. Gray, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13007v1.pdf)  
  Keywords: autonomous driving, robotics, semantic, reflection, tracking, ar  
- **[GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](https://arxiv.org/abs/2512.10939v1)**  
  Authors: Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10939v1.pdf)  
  Keywords: fast, tracking, mapping, gaussian splatting, head, ar, avatar  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: face, mapping, gaussian splatting, deformation, ar, high-fidelity  
- **[Neural Hamiltonian Deformation Fields for Dynamic Scene Rendering](https://arxiv.org/abs/2512.10424v1)**  
  Authors: Hai-Long Qin, Sixian Wang, Guo Lu, Jincheng Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10424v1.pdf)  
  Keywords: motion, mapping, dynamic, gaussian splatting, deformation, ar  
- **[YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos](https://arxiv.org/abs/2512.09903v1)**  
  Authors: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09903v1.pdf)  
  Keywords: recognition, human, compact, mapping, gaussian splatting, ar, localization, 3d gaussian  
- **[GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars](https://arxiv.org/abs/2512.09162v1)**  
  Authors: Kelian Baert, Mae Younes, Francois Bourel, Marc Christie, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09162v1.pdf)  
  Keywords: head, mapping, relighting, lighting, gaussian splatting, geometry, efficient, ar, avatar, relightable  
- **[OpenMonoGS-SLAM: Monocular Gaussian Splatting SLAM with Open-set Semantics](https://arxiv.org/abs/2512.08625v1)**  
  Authors: Jisang Yoo, Gyeongjin Kang, Hyun-kyu Ko, Hyeonwoo Yu, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08625v1.pdf)  
  Keywords: robotics, semantic, tracking, mapping, segmentation, gaussian splatting, geometry, slam, vr, ar, localization, 3d gaussian, understanding  
- **[Tracking-Guided 4D Generation: Foundation-Tracker Motion Priors for 3D Model Animation](https://arxiv.org/abs/2512.06158v1)**  
  Authors: Su Sun, Cheng Zhao, Himangi Mittal, Gaurav Mittal, Rohith Kukkala, Yingjie Victor Chen, Mei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.06158v1.pdf)  
  Keywords: motion, animation, 4d, tracking, dynamic, gaussian splatting, ar  
- **[Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding](https://arxiv.org/abs/2512.03601v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion4d-web/.)  
  Keywords: motion, semantic, 4d, tracking, dynamic, gaussian splatting, segmentation, geometry, ar, understanding  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v1)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v1.pdf)  
  Keywords: robotics, semantic, nerf, mapping, gaussian splatting, slam, survey, ar, localization, 3d gaussian, understanding  

### Scene Understanding

*Showing the latest 50 out of 206 papers*

- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: semantic, nerf, human, face, lighting, gaussian splatting, segmentation, geometry, ar, high-fidelity, relightable  
- **[Computer vision training dataset generation for robotic environments using Gaussian splatting](https://arxiv.org/abs/2512.13411v1)**  
  Authors: Patryk Niżeniec, Marcin Iwanowski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13411v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, segmentation, efficient, ar, shadow  
- **[Light Field Based 6DoF Tracking of Previously Unobserved Objects](https://arxiv.org/abs/2512.13007v1)**  
  Authors: Nikolai Goncharov, James L. Gray, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13007v1.pdf)  
  Keywords: autonomous driving, robotics, semantic, reflection, tracking, ar  
- **[Prior-Enhanced Gaussian Splatting for Dynamic Scene Reconstruction from Casual Video](https://arxiv.org/abs/2512.11356v1)**  
  Authors: Meng-Li Shih, Ying-Huan Chen, Yu-Lun Liu, Brian Curless  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11356v1.pdf)  
  Keywords: motion, dynamic, gaussian splatting, segmentation, geometry, ar  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: light transport, sparse-view, relighting, lighting, gaussian splatting, segmentation, geometry, ar  
- **[YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos](https://arxiv.org/abs/2512.09903v1)**  
  Authors: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09903v1.pdf)  
  Keywords: recognition, human, compact, mapping, gaussian splatting, ar, localization, 3d gaussian  
- **[OpenMonoGS-SLAM: Monocular Gaussian Splatting SLAM with Open-set Semantics](https://arxiv.org/abs/2512.08625v1)**  
  Authors: Jisang Yoo, Gyeongjin Kang, Hyun-kyu Ko, Hyeonwoo Yu, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08625v1.pdf)  
  Keywords: robotics, semantic, tracking, mapping, segmentation, gaussian splatting, geometry, slam, vr, ar, localization, 3d gaussian, understanding  
- **[Zero-Splat TeleAssist: A Zero-Shot Pose Estimation Framework for Semantic Teleoperation](https://arxiv.org/abs/2512.08271v1)**  
  Authors: Srijan Dokania, Dharini Raghavan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08271v1.pdf)  
  Keywords: semantic, segmentation, gaussian splatting, ar, 3d gaussian  
- **[STRinGS: Selective Text Refinement in Gaussian Splatting](https://arxiv.org/abs/2512.07230v1)**  
  Authors: Abhinav Raundhal, Gaurav Behera, P J Narayanan, Ravi Kiran Sarvadevabhatla, Makarand Tapaswi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07230v1.pdf)  
  Keywords: semantic, gaussian splatting, 3d gaussian, 3d reconstruction, ar, understanding  
- **[4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer](https://arxiv.org/abs/2512.05060v1)**  
  Authors: Xianfeng Wu, Yajing Bai, Minghan Li, Xianzu Wu, Xueqi Zhao, Zhongyuan Lai, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05060v1.pdf)  
  Keywords: semantic, nerf, 4d, dynamic, gaussian splatting, geometry, ar, understanding  



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