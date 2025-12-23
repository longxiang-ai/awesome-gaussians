# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-12-23 00:57:10

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
- [Acceleration](#acceleration) (253 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (346 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (399 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (81 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (347 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (71 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (407 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (198 papers) - Papers focusing on improving rendering quality
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
  Keywords: compression, efficient, ar, high-fidelity, gaussian splatting, dynamic, 3d reconstruction, survey, 3d gaussian, 4d, compact  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v1)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v1.pdf)  
  Keywords: nerf, ar, semantic, gaussian splatting, understanding, mapping, survey, 3d gaussian, robotics, slam, localization  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: efficient, ar, high-fidelity, gaussian splatting, semantic, mapping, survey, 3d gaussian, robotics, slam, localization  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: nerf, ar, gaussian splatting, survey, motion, 3d gaussian, geometry, 4d, fast  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: animation, efficient, ar, face, gaussian splatting, real-time rendering, 3d reconstruction, survey, 3d gaussian, lighting, efficient rendering, avatar  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: efficient, nerf, ar, gaussian splatting, lightweight, understanding, survey, human  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: efficient, nerf, ar, gaussian splatting, understanding, survey, 3d gaussian, neural rendering, slam, fast  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: nerf, ar, high-fidelity, gaussian splatting, semantic, understanding, survey, 3d gaussian, lighting, compact, segmentation  
- **[A Study of the Framework and Real-World Applications of Language Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: efficient, nerf, ar, gaussian splatting, semantic, understanding, survey, 3d gaussian, robotics  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: nerf, ar, gaussian splatting, survey, 3d gaussian, robotics, human  

### Acceleration

*Showing the latest 50 out of 253 papers*

- **[Voxel-GS: Quantized Scaffold Gaussian Splatting Compression with Run-Length Coding](https://arxiv.org/abs/2512.17528v1)**  
  Authors: Chunyang Fu, Xiangrui Liu, Shiqi Wang, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17528v1.pdf)  
  Keywords: compression, ar, high-fidelity, gaussian splatting, lightweight, compact, fast  
- **[Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation](https://arxiv.org/abs/2512.16893v1)**  
  Authors: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16893v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/instant4d)  
  Keywords: animation, efficient, head, face, gaussian splatting, lightweight, ar, motion, 4d, fast, avatar  
- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: nerf, ar, face, gaussian splatting, 3d gaussian, ray tracing, fast  
- **[Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering](https://arxiv.org/abs/2512.15711v1)**  
  Authors: Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Tomas Simon, Forrest Iandola, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15711v1.pdf)  
  Keywords: efficient, head, ar, face, gaussian splatting, 3d gaussian, efficient rendering, avatar  
- **[VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments](https://arxiv.org/abs/2512.15258v2)**  
  Authors: Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Yuxin Fan, Wenjun Li, Zhichao Han, Xin Zhou, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15258v2.pdf)  
  Keywords: efficient, ar, high-fidelity, gaussian splatting, lightweight, 3d gaussian, fast  
- **[HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis](https://arxiv.org/abs/2512.14352v1)**  
  Authors: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Caixia Yan, Haipeng Du, yugui xie, Yu-Hui Wen, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14352v1.pdf)  
  Keywords: efficient, nerf, ar, deformation, dynamic, gaussian splatting, vr, real-time rendering, 3d gaussian, compact  
- **[Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries](https://arxiv.org/abs/2512.13796v1)**  
  Authors: Victor Rong, Jan Held, Victor Chu, Daniel Rebain, Marc Van Droogenbroeck, Kiriakos N. Kutulakos, Andrea Tagliasacchi, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13796v1.pdf)  
  Keywords: ar, gaussian splatting, outdoor, 3d gaussian, geometry, compact, fast  
- **[Fast 2DGS: Efficient Image Representation with Deep Gaussian Prior](https://arxiv.org/abs/2512.12774v1)**  
  Authors: Hao Wang, Ashish Bastola, Chaoyi Zhou, Wenhui Zhu, Xiwen Chen, Xuanzhao Dong, Siyu Huang, Abolfazl Razi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.12774v1.pdf)  
  Keywords: efficient, ar, high-fidelity, gaussian splatting, lightweight, real-time rendering, fast  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, real-time rendering, 3d gaussian, ray tracing, compact, fast  
- **[Lightweight 3D Gaussian Splatting Compression via Video Codec](https://arxiv.org/abs/2512.11186v1)**  
  Authors: Qi Yang, Geert Van Der Auwera, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11186v1.pdf)  
  Keywords: compression, ar, gaussian splatting, lightweight, 3d gaussian, fast  

### Applications

*Showing the latest 50 out of 995 papers*

- **[Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding](https://arxiv.org/abs/2512.17817v1)**  
  Authors: Yue Li, Qi Ma, Runyi Yang, Mengjiao Ma, Bin Ren, Nikola Popovic, Nicu Sebe, Theo Gevers, Luc Van Gool, Danda Pani Paudel, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17817v1.pdf)  
  Keywords: efficient, ar, high-fidelity, semantic, gaussian splatting, 3d gaussian, segmentation  
- **[G3Splat: Geometrically Consistent Generalizable Gaussian Splatting](https://arxiv.org/abs/2512.17547v1)**  
  Authors: Mehdi Hosseinzadeh, Shin-Fang Chng, Yi Xu, Simon Lucey, Ian Reid, Ravi Garg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17547v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://m80hz.github.io/g3splat/).)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting  
- **[Voxel-GS: Quantized Scaffold Gaussian Splatting Compression with Run-Length Coding](https://arxiv.org/abs/2512.17528v1)**  
  Authors: Chunyang Fu, Xiangrui Liu, Shiqi Wang, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17528v1.pdf)  
  Keywords: compression, ar, high-fidelity, gaussian splatting, lightweight, compact, fast  
- **[Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation](https://arxiv.org/abs/2512.17349v1)**  
  Authors: Xijie Huang, Jinhan Li, Tianyue Wu, Xin Zhou, Zhichao Han, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17349v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, 3d gaussian, illumination  
- **[Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation](https://arxiv.org/abs/2512.16893v1)**  
  Authors: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16893v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/instant4d)  
  Keywords: animation, efficient, head, face, gaussian splatting, lightweight, ar, motion, 4d, fast, avatar  
- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: nerf, ar, face, gaussian splatting, 3d gaussian, ray tracing, fast  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: relightable, nerf, ar, high-fidelity, gaussian splatting, face, semantic, lighting, geometry, human, segmentation  
- **[Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering](https://arxiv.org/abs/2512.15711v1)**  
  Authors: Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Tomas Simon, Forrest Iandola, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15711v1.pdf)  
  Keywords: efficient, head, ar, face, gaussian splatting, 3d gaussian, efficient rendering, avatar  
- **[Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2512.15508v1)**  
  Authors: Arthur Moreau, Richard Shaw, Michal Nazarczuk, Jisu Shin, Thomas Tanay, Zhensong Zhang, Songcen Xu, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15508v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, 3d reconstruction, 3d gaussian  
- **[VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments](https://arxiv.org/abs/2512.15258v2)**  
  Authors: Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Yuxin Fan, Wenjun Li, Zhichao Han, Xin Zhou, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15258v2.pdf)  
  Keywords: efficient, ar, high-fidelity, gaussian splatting, lightweight, 3d gaussian, fast  

### Avatar Generation

*Showing the latest 50 out of 346 papers*

- **[Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation](https://arxiv.org/abs/2512.16893v1)**  
  Authors: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16893v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/instant4d)  
  Keywords: animation, efficient, head, face, gaussian splatting, lightweight, ar, motion, 4d, fast, avatar  
- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: nerf, ar, face, gaussian splatting, 3d gaussian, ray tracing, fast  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: relightable, nerf, ar, high-fidelity, gaussian splatting, face, semantic, lighting, geometry, human, segmentation  
- **[Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering](https://arxiv.org/abs/2512.15711v1)**  
  Authors: Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Tomas Simon, Forrest Iandola, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15711v1.pdf)  
  Keywords: efficient, head, ar, face, gaussian splatting, 3d gaussian, efficient rendering, avatar  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: efficient, ar, face, gaussian splatting, urban scene, 3d reconstruction, 3d gaussian, geometry, illumination  
- **[GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](https://arxiv.org/abs/2512.10939v1)**  
  Authors: Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10939v1.pdf)  
  Keywords: head, ar, gaussian splatting, mapping, fast, tracking, avatar  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: ar, face, deformation, high-fidelity, gaussian splatting, mapping  
- **[Splatent: Splatting Diffusion Latents for Novel View Synthesis](https://arxiv.org/abs/2512.09923v1)**  
  Authors: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09923v1.pdf)  
  Keywords: efficient, ar, face, gaussian splatting, sparse-view, 3d reconstruction, 3d gaussian, efficient rendering  
- **[YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos](https://arxiv.org/abs/2512.09903v1)**  
  Authors: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09903v1.pdf)  
  Keywords: ar, gaussian splatting, recognition, mapping, 3d gaussian, human, compact, localization  
- **[Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video](https://arxiv.org/abs/2512.09335v2)**  
  Authors: Seonghwa Choi, Moonkyeong Choi, Mingyu Jang, Jaekyung Kim, Jianfei Cai, Wen-Huang Cheng, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09335v2.pdf)  
  Keywords: relightable, nerf, relighting, high-fidelity, gaussian splatting, dynamic, deformation, ar, body, motion, 3d gaussian, lighting, human, avatar  

### Dynamic Scene

*Showing the latest 50 out of 399 papers*

- **[Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation](https://arxiv.org/abs/2512.16893v1)**  
  Authors: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16893v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/instant4d)  
  Keywords: animation, efficient, head, face, gaussian splatting, lightweight, ar, motion, 4d, fast, avatar  
- **[Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos](https://arxiv.org/abs/2512.14406v1)**  
  Authors: Le Jiang, Shaotong Zhu, Yedi Luo, Shayda Moezzi, Sarah Ostadabbas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14406v1.pdf)  
  Keywords: nerf, ar, dynamic, gaussian splatting  
- **[HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis](https://arxiv.org/abs/2512.14352v1)**  
  Authors: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Caixia Yan, Haipeng Du, yugui xie, Yu-Hui Wen, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14352v1.pdf)  
  Keywords: efficient, nerf, ar, deformation, dynamic, gaussian splatting, vr, real-time rendering, 3d gaussian, compact  
- **[Prior-Enhanced Gaussian Splatting for Dynamic Scene Reconstruction from Casual Video](https://arxiv.org/abs/2512.11356v1)**  
  Authors: Meng-Li Shih, Ying-Huan Chen, Yu-Lun Liu, Brian Curless  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11356v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, motion, geometry, segmentation  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: ar, face, deformation, high-fidelity, gaussian splatting, mapping  
- **[Neural Hamiltonian Deformation Fields for Dynamic Scene Rendering](https://arxiv.org/abs/2512.10424v1)**  
  Authors: Hai-Long Qin, Sixian Wang, Guo Lu, Jincheng Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10424v1.pdf)  
  Keywords: ar, deformation, dynamic, gaussian splatting, mapping, motion  
- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v1)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: ar, high-fidelity, gaussian splatting, 3d reconstruction, motion, 3d gaussian, sparse view  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, dynamic, 3d reconstruction, reflection, geometry, ray tracing  
- **[ReMoSPLAT: Reactive Mobile Manipulation Control on a Gaussian Splat](https://arxiv.org/abs/2512.09656v1)**  
  Authors: Nicolas Marticorena, Tobias Fischer, Niko Suenderhauf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09656v1.pdf)  
  Keywords: motion, efficient, ar  
- **[Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video](https://arxiv.org/abs/2512.09335v2)**  
  Authors: Seonghwa Choi, Moonkyeong Choi, Mingyu Jang, Jaekyung Kim, Jianfei Cai, Wen-Huang Cheng, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09335v2.pdf)  
  Keywords: relightable, nerf, relighting, high-fidelity, gaussian splatting, dynamic, deformation, ar, body, motion, 3d gaussian, lighting, human, avatar  

### Few-shot

*Showing the latest 50 out of 81 papers*

- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v1)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: ar, high-fidelity, gaussian splatting, 3d reconstruction, motion, 3d gaussian, sparse view  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: ar, relighting, gaussian splatting, sparse-view, light transport, geometry, lighting, segmentation  
- **[Splatent: Splatting Diffusion Latents for Novel View Synthesis](https://arxiv.org/abs/2512.09923v1)**  
  Authors: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09923v1.pdf)  
  Keywords: efficient, ar, face, gaussian splatting, sparse-view, 3d reconstruction, 3d gaussian, efficient rendering  
- **[Tessellation GS: Neural Mesh Gaussians for Robust Monocular Reconstruction of Dynamic Objects](https://arxiv.org/abs/2512.07381v1)**  
  Authors: Shuohan Tao, Boyao Zhou, Hanzhang Tu, Yuwang Wang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07381v1.pdf)  
  Keywords: ar, deformation, dynamic, gaussian splatting, face, sparse-view, 3d gaussian  
- **[MuSASplat: Efficient Sparse-View 3D Gaussian Splats via Lightweight Multi-Scale Adaptation](https://arxiv.org/abs/2512.07165v1)**  
  Authors: Muyu Xu, Fangneng Zhan, Xiaoqin Zhang, Ling Shao, Shijian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07165v1.pdf)  
  Keywords: efficient, head, ar, gaussian splatting, lightweight, sparse-view, 3d gaussian  
- **[C3G: Learning Compact 3D Representations with 2K Gaussians](https://arxiv.org/abs/2512.04021v1)**  
  Authors: Honggyu An, Jaewoo Jung, Mungyeom Kim, Sunghwan Hong, Chaehyun Kim, Kazumi Fukuda, Minkyeong Jeon, Jisang Han, Takuya Narihira, Hyuna Ko, Junsu Kim, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04021v1.pdf)  
  Keywords: efficient, head, ar, gaussian splatting, understanding, 3d gaussian, sparse view, compact, segmentation  
- **[Cross-Temporal 3D Gaussian Splatting for Sparse-View Guided Scene Update](https://arxiv.org/abs/2512.00534v1)**  
  Authors: Zeyuan An, Yanghang Xiao, Zhiying Leng, Frederick W. B. Li, Xiaohui Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00534v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, sparse-view, 3d gaussian, sparse view  
- **[Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views](https://arxiv.org/abs/2512.00255v1)**  
  Authors: Kunwar Maheep Singh, Jianchun Chen, Vladislav Golyanik, Stephan J. Garbin, Thabo Beeler, Rishabh Dabral, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/RHC/)  
  Keywords: relightable, efficient, relighting, ar, dynamic, sparse-view, body, motion, sparse view, 3d gaussian, lighting, geometry, illumination, human, tracking  
- **[Observer Actor: Active Vision Imitation Learning with Sparse View Gaussian Splatting](https://arxiv.org/abs/2511.18140v1)**  
  Authors: Yilong Wang, Cheng Qian, Ruomeng Fan, Edward Johns  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18140v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://obact.github.io.)  
  Keywords: ar, dynamic, gaussian splatting, 3d gaussian, sparse view  
- **[Frequency-Adaptive Sharpness Regularization for Improving 3D Gaussian Splatting Generalization](https://arxiv.org/abs/2511.17918v1)**  
  Authors: Youngsik Yun, Dongjun Gu, Youngjung Uh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bbangsik13.github.io/FASR.)  
  Keywords: 3d gaussian, ar, few-shot, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 347 papers*

- **[G3Splat: Geometrically Consistent Generalizable Gaussian Splatting](https://arxiv.org/abs/2512.17547v1)**  
  Authors: Mehdi Hosseinzadeh, Shin-Fang Chng, Yi Xu, Simon Lucey, Ian Reid, Ravi Garg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17547v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://m80hz.github.io/g3splat/).)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: relightable, nerf, ar, high-fidelity, gaussian splatting, face, semantic, lighting, geometry, human, segmentation  
- **[Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2512.15508v1)**  
  Authors: Arthur Moreau, Richard Shaw, Michal Nazarczuk, Jisu Shin, Thomas Tanay, Zhensong Zhang, Songcen Xu, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15508v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, 3d reconstruction, 3d gaussian  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: efficient, ar, face, gaussian splatting, urban scene, 3d reconstruction, 3d gaussian, geometry, illumination  
- **[GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants](https://arxiv.org/abs/2512.14087v1)**  
  Authors: Yang Yang, Risa Shinoda, Hiroaki Santo, Fumio Okura  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14087v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, 3d reconstruction, 3d gaussian, geometry  
- **[Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries](https://arxiv.org/abs/2512.13796v1)**  
  Authors: Victor Rong, Jan Held, Victor Chu, Daniel Rebain, Marc Van Droogenbroeck, Kiriakos N. Kutulakos, Andrea Tagliasacchi, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13796v1.pdf)  
  Keywords: ar, gaussian splatting, outdoor, 3d gaussian, geometry, compact, fast  
- **[Prior-Enhanced Gaussian Splatting for Dynamic Scene Reconstruction from Casual Video](https://arxiv.org/abs/2512.11356v1)**  
  Authors: Meng-Li Shih, Ying-Huan Chen, Yu-Lun Liu, Brian Curless  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11356v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, motion, geometry, segmentation  
- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v1)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: ar, high-fidelity, gaussian splatting, 3d reconstruction, motion, 3d gaussian, sparse view  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, dynamic, 3d reconstruction, reflection, geometry, ray tracing  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: ar, relighting, gaussian splatting, sparse-view, light transport, geometry, lighting, segmentation  

### Large Scene

*Showing the latest 50 out of 71 papers*

- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: efficient, ar, face, gaussian splatting, urban scene, 3d reconstruction, 3d gaussian, geometry, illumination  
- **[Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries](https://arxiv.org/abs/2512.13796v1)**  
  Authors: Victor Rong, Jan Held, Victor Chu, Daniel Rebain, Marc Van Droogenbroeck, Kiriakos N. Kutulakos, Andrea Tagliasacchi, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13796v1.pdf)  
  Keywords: ar, gaussian splatting, outdoor, 3d gaussian, geometry, compact, fast  
- **[Flux4D: Flow-based Unsupervised 4D Reconstruction](https://arxiv.org/abs/2512.03210v1)**  
  Authors: Jingkang Wang, Henry Che, Yun Chen, Ze Yang, Lily Goli, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03210v1.pdf)  
  Keywords: efficient, nerf, ar, dynamic, gaussian splatting, outdoor, motion, 3d gaussian, robotics, 4d  
- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: ar, gaussian splatting, understanding, 3d reconstruction, outdoor, 3d gaussian, geometry  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: ar, semantic, gaussian splatting, outdoor, geometry, fast  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: efficient, ar, relighting, high-fidelity, gaussian splatting, face, semantic, outdoor, lighting, geometry, illumination, segmentation  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, outdoor, 3d gaussian, geometry  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, urban scene, 4d, human, autonomous driving  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: head, ar, gaussian splatting, large scene, 3d gaussian, fast  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: ar, gaussian splatting, understanding, outdoor, mapping, motion, 3d gaussian, geometry, slam  

### Model Compression

*Showing the latest 50 out of 407 papers*

- **[Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding](https://arxiv.org/abs/2512.17817v1)**  
  Authors: Yue Li, Qi Ma, Runyi Yang, Mengjiao Ma, Bin Ren, Nikola Popovic, Nicu Sebe, Theo Gevers, Luc Van Gool, Danda Pani Paudel, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17817v1.pdf)  
  Keywords: efficient, ar, high-fidelity, semantic, gaussian splatting, 3d gaussian, segmentation  
- **[Voxel-GS: Quantized Scaffold Gaussian Splatting Compression with Run-Length Coding](https://arxiv.org/abs/2512.17528v1)**  
  Authors: Chunyang Fu, Xiangrui Liu, Shiqi Wang, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17528v1.pdf)  
  Keywords: compression, ar, high-fidelity, gaussian splatting, lightweight, compact, fast  
- **[Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation](https://arxiv.org/abs/2512.16893v1)**  
  Authors: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16893v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/instant4d)  
  Keywords: animation, efficient, head, face, gaussian splatting, lightweight, ar, motion, 4d, fast, avatar  
- **[Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering](https://arxiv.org/abs/2512.15711v1)**  
  Authors: Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Tomas Simon, Forrest Iandola, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15711v1.pdf)  
  Keywords: efficient, head, ar, face, gaussian splatting, 3d gaussian, efficient rendering, avatar  
- **[Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2512.15508v1)**  
  Authors: Arthur Moreau, Richard Shaw, Michal Nazarczuk, Jisu Shin, Thomas Tanay, Zhensong Zhang, Songcen Xu, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15508v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, 3d reconstruction, 3d gaussian  
- **[VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments](https://arxiv.org/abs/2512.15258v2)**  
  Authors: Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Yuxin Fan, Wenjun Li, Zhichao Han, Xin Zhou, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15258v2.pdf)  
  Keywords: efficient, ar, high-fidelity, gaussian splatting, lightweight, 3d gaussian, fast  
- **[HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis](https://arxiv.org/abs/2512.14352v1)**  
  Authors: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Caixia Yan, Haipeng Du, yugui xie, Yu-Hui Wen, Yong-Jin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14352v1.pdf)  
  Keywords: efficient, nerf, ar, deformation, dynamic, gaussian splatting, vr, real-time rendering, 3d gaussian, compact  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: efficient, ar, face, gaussian splatting, urban scene, 3d reconstruction, 3d gaussian, geometry, illumination  
- **[Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere](https://arxiv.org/abs/2512.14180v1)**  
  Authors: Francesco Di Sario, Daniel Rebain, Dor Verbin, Marco Grangetto, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14180v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, reflection, 3d gaussian  
- **[ASAP-Textured Gaussians: Enhancing Textured Gaussians with Adaptive Sampling and Anisotropic Parameterization](https://arxiv.org/abs/2512.14039v1)**  
  Authors: Meng Wei, Cheng Zhang, Jianmin Zheng, Hamid Rezatofighi, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14039v1.pdf)  
  Keywords: efficient, ar, high-fidelity, gaussian splatting, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 198 papers*

- **[Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding](https://arxiv.org/abs/2512.17817v1)**  
  Authors: Yue Li, Qi Ma, Runyi Yang, Mengjiao Ma, Bin Ren, Nikola Popovic, Nicu Sebe, Theo Gevers, Luc Van Gool, Danda Pani Paudel, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17817v1.pdf)  
  Keywords: efficient, ar, high-fidelity, semantic, gaussian splatting, 3d gaussian, segmentation  
- **[Voxel-GS: Quantized Scaffold Gaussian Splatting Compression with Run-Length Coding](https://arxiv.org/abs/2512.17528v1)**  
  Authors: Chunyang Fu, Xiangrui Liu, Shiqi Wang, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17528v1.pdf)  
  Keywords: compression, ar, high-fidelity, gaussian splatting, lightweight, compact, fast  
- **[Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation](https://arxiv.org/abs/2512.17349v1)**  
  Authors: Xijie Huang, Jinhan Li, Tianyue Wu, Xin Zhou, Zhichao Han, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17349v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, 3d gaussian, illumination  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: relightable, nerf, ar, high-fidelity, gaussian splatting, face, semantic, lighting, geometry, human, segmentation  
- **[VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments](https://arxiv.org/abs/2512.15258v2)**  
  Authors: Yuze Wu, Mo Zhu, Xingxing Li, Yuheng Du, Yuxin Fan, Wenjun Li, Zhichao Han, Xin Zhou, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.15258v2.pdf)  
  Keywords: efficient, ar, high-fidelity, gaussian splatting, lightweight, 3d gaussian, fast  
- **[GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants](https://arxiv.org/abs/2512.14087v1)**  
  Authors: Yang Yang, Risa Shinoda, Hiroaki Santo, Fumio Okura  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14087v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, 3d reconstruction, 3d gaussian, geometry  
- **[ASAP-Textured Gaussians: Enhancing Textured Gaussians with Adaptive Sampling and Anisotropic Parameterization](https://arxiv.org/abs/2512.14039v1)**  
  Authors: Meng Wei, Cheng Zhang, Jianmin Zheng, Hamid Rezatofighi, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14039v1.pdf)  
  Keywords: efficient, ar, high-fidelity, gaussian splatting, 3d gaussian  
- **[Fast 2DGS: Efficient Image Representation with Deep Gaussian Prior](https://arxiv.org/abs/2512.12774v1)**  
  Authors: Hao Wang, Ashish Bastola, Chaoyi Zhou, Wenhui Zhu, Xiwen Chen, Xuanzhao Dong, Siyu Huang, Abolfazl Razi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.12774v1.pdf)  
  Keywords: efficient, ar, high-fidelity, gaussian splatting, lightweight, real-time rendering, fast  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, real-time rendering, 3d gaussian, ray tracing, compact, fast  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: ar, face, deformation, high-fidelity, gaussian splatting, mapping  

### Ray Tracing

- **[SDFoam: Signed-Distance Foam for explicit surface reconstruction](https://arxiv.org/abs/2512.16706v1)**  
  Authors: Antonella Rech, Nicola Conci, Nicola Garau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16706v1.pdf)  
  Keywords: nerf, ar, face, gaussian splatting, 3d gaussian, ray tracing, fast  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, real-time rendering, 3d gaussian, ray tracing, compact, fast  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, dynamic, 3d reconstruction, reflection, geometry, ray tracing  
- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: ar, gaussian splatting, reflection, geometry, ray tracing, illumination  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: efficient, ar, gaussian splatting, 3d gaussian, ray marching, geometry  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: relightable, efficient, ar, face, gaussian splatting, real-time rendering, light transport, lighting, ray tracing, shadow  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: efficient, ar, relighting, gaussian splatting, reflection, light transport, lighting, geometry, illumination, global illumination  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v2)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v2.pdf)  
  Keywords: ar, dynamic, gaussian splatting, ray tracing, 4d, fast  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: nerf, relighting, high-fidelity, gaussian splatting, face, ar, reflection, 3d gaussian, lighting, ray tracing, illumination, geometry  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: relightable, ar, relighting, face, gaussian splatting, dynamic, outdoor, 3d gaussian, lighting, shadow, illumination, global illumination  

### Relighting

*Showing the latest 50 out of 127 papers*

- **[Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation](https://arxiv.org/abs/2512.17349v1)**  
  Authors: Xijie Huang, Jinhan Li, Tianyue Wu, Xin Zhou, Zhichao Han, Fei Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17349v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, 3d gaussian, illumination  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: relightable, nerf, ar, high-fidelity, gaussian splatting, face, semantic, lighting, geometry, human, segmentation  
- **[Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination](https://arxiv.org/abs/2512.14200v1)**  
  Authors: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14200v1.pdf)  
  Keywords: efficient, ar, face, gaussian splatting, urban scene, 3d reconstruction, 3d gaussian, geometry, illumination  
- **[Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere](https://arxiv.org/abs/2512.14180v1)**  
  Authors: Francesco Di Sario, Daniel Rebain, Dor Verbin, Marco Grangetto, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.14180v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, reflection, 3d gaussian  
- **[Computer vision training dataset generation for robotic environments using Gaussian splatting](https://arxiv.org/abs/2512.13411v1)**  
  Authors: Patryk Niżeniec, Marcin Iwanowski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13411v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, 3d gaussian, shadow, segmentation  
- **[Light Field Based 6DoF Tracking of Previously Unobserved Objects](https://arxiv.org/abs/2512.13007v1)**  
  Authors: Nikolai Goncharov, James L. Gray, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13007v1.pdf)  
  Keywords: ar, semantic, reflection, robotics, tracking, autonomous driving  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting, dynamic, 3d reconstruction, reflection, geometry, ray tracing  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: ar, relighting, gaussian splatting, sparse-view, light transport, geometry, lighting, segmentation  
- **[Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video](https://arxiv.org/abs/2512.09335v2)**  
  Authors: Seonghwa Choi, Moonkyeong Choi, Mingyu Jang, Jaekyung Kim, Jianfei Cai, Wen-Huang Cheng, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09335v2.pdf)  
  Keywords: relightable, nerf, relighting, high-fidelity, gaussian splatting, dynamic, deformation, ar, body, motion, 3d gaussian, lighting, human, avatar  
- **[GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars](https://arxiv.org/abs/2512.09162v1)**  
  Authors: Kelian Baert, Mae Younes, Francois Bourel, Marc Christie, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09162v1.pdf)  
  Keywords: relightable, efficient, relighting, head, gaussian splatting, ar, mapping, geometry, lighting, avatar  

### SLAM

*Showing the latest 50 out of 147 papers*

- **[Light Field Based 6DoF Tracking of Previously Unobserved Objects](https://arxiv.org/abs/2512.13007v1)**  
  Authors: Nikolai Goncharov, James L. Gray, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13007v1.pdf)  
  Keywords: ar, semantic, reflection, robotics, tracking, autonomous driving  
- **[GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](https://arxiv.org/abs/2512.10939v1)**  
  Authors: Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10939v1.pdf)  
  Keywords: head, ar, gaussian splatting, mapping, fast, tracking, avatar  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: ar, face, deformation, high-fidelity, gaussian splatting, mapping  
- **[Neural Hamiltonian Deformation Fields for Dynamic Scene Rendering](https://arxiv.org/abs/2512.10424v1)**  
  Authors: Hai-Long Qin, Sixian Wang, Guo Lu, Jincheng Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10424v1.pdf)  
  Keywords: ar, deformation, dynamic, gaussian splatting, mapping, motion  
- **[YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos](https://arxiv.org/abs/2512.09903v1)**  
  Authors: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09903v1.pdf)  
  Keywords: ar, gaussian splatting, recognition, mapping, 3d gaussian, human, compact, localization  
- **[GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars](https://arxiv.org/abs/2512.09162v1)**  
  Authors: Kelian Baert, Mae Younes, Francois Bourel, Marc Christie, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09162v1.pdf)  
  Keywords: relightable, efficient, relighting, head, gaussian splatting, ar, mapping, geometry, lighting, avatar  
- **[OpenMonoGS-SLAM: Monocular Gaussian Splatting SLAM with Open-set Semantics](https://arxiv.org/abs/2512.08625v1)**  
  Authors: Jisang Yoo, Gyeongjin Kang, Hyun-kyu Ko, Hyeonwoo Yu, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08625v1.pdf)  
  Keywords: ar, semantic, gaussian splatting, understanding, vr, mapping, 3d gaussian, robotics, geometry, slam, tracking, localization, segmentation  
- **[Tracking-Guided 4D Generation: Foundation-Tracker Motion Priors for 3D Model Animation](https://arxiv.org/abs/2512.06158v1)**  
  Authors: Su Sun, Cheng Zhao, Himangi Mittal, Gaurav Mittal, Rohith Kukkala, Yingjie Victor Chen, Mei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.06158v1.pdf)  
  Keywords: animation, ar, dynamic, gaussian splatting, motion, 4d, tracking  
- **[Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding](https://arxiv.org/abs/2512.03601v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion4d-web/.)  
  Keywords: ar, dynamic, gaussian splatting, semantic, understanding, motion, geometry, 4d, tracking, segmentation  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v1)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v1.pdf)  
  Keywords: nerf, ar, semantic, gaussian splatting, understanding, mapping, survey, 3d gaussian, robotics, slam, localization  

### Scene Understanding

*Showing the latest 50 out of 206 papers*

- **[Chorus: Multi-Teacher Pretraining for Holistic 3D Gaussian Scene Encoding](https://arxiv.org/abs/2512.17817v1)**  
  Authors: Yue Li, Qi Ma, Runyi Yang, Mengjiao Ma, Bin Ren, Nikola Popovic, Nicu Sebe, Theo Gevers, Luc Van Gool, Danda Pani Paudel, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17817v1.pdf)  
  Keywords: efficient, ar, high-fidelity, semantic, gaussian splatting, 3d gaussian, segmentation  
- **[Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture](https://arxiv.org/abs/2512.16397v1)**  
  Authors: Haodi He, Jihun Yu, Ronald Fedkiw  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.16397v1.pdf)  
  Keywords: relightable, nerf, ar, high-fidelity, gaussian splatting, face, semantic, lighting, geometry, human, segmentation  
- **[Computer vision training dataset generation for robotic environments using Gaussian splatting](https://arxiv.org/abs/2512.13411v1)**  
  Authors: Patryk Niżeniec, Marcin Iwanowski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13411v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, 3d gaussian, shadow, segmentation  
- **[Light Field Based 6DoF Tracking of Previously Unobserved Objects](https://arxiv.org/abs/2512.13007v1)**  
  Authors: Nikolai Goncharov, James L. Gray, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13007v1.pdf)  
  Keywords: ar, semantic, reflection, robotics, tracking, autonomous driving  
- **[Prior-Enhanced Gaussian Splatting for Dynamic Scene Reconstruction from Casual Video](https://arxiv.org/abs/2512.11356v1)**  
  Authors: Meng-Li Shih, Ying-Huan Chen, Yu-Lun Liu, Brian Curless  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11356v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, motion, geometry, segmentation  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: ar, relighting, gaussian splatting, sparse-view, light transport, geometry, lighting, segmentation  
- **[YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos](https://arxiv.org/abs/2512.09903v1)**  
  Authors: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09903v1.pdf)  
  Keywords: ar, gaussian splatting, recognition, mapping, 3d gaussian, human, compact, localization  
- **[OpenMonoGS-SLAM: Monocular Gaussian Splatting SLAM with Open-set Semantics](https://arxiv.org/abs/2512.08625v1)**  
  Authors: Jisang Yoo, Gyeongjin Kang, Hyun-kyu Ko, Hyeonwoo Yu, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08625v1.pdf)  
  Keywords: ar, semantic, gaussian splatting, understanding, vr, mapping, 3d gaussian, robotics, geometry, slam, tracking, localization, segmentation  
- **[Zero-Splat TeleAssist: A Zero-Shot Pose Estimation Framework for Semantic Teleoperation](https://arxiv.org/abs/2512.08271v1)**  
  Authors: Srijan Dokania, Dharini Raghavan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08271v1.pdf)  
  Keywords: ar, semantic, gaussian splatting, 3d gaussian, segmentation  
- **[STRinGS: Selective Text Refinement in Gaussian Splatting](https://arxiv.org/abs/2512.07230v1)**  
  Authors: Abhinav Raundhal, Gaurav Behera, P J Narayanan, Ravi Kiran Sarvadevabhatla, Makarand Tapaswi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07230v1.pdf)  
  Keywords: ar, semantic, understanding, gaussian splatting, 3d reconstruction, 3d gaussian  



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