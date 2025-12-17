# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-12-17 00:53:07

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

- [3DGS Surveys](#3dgs-surveys) (23 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (249 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (343 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (400 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (84 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (346 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (73 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (401 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (193 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (16 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (125 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (148 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (208 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: dynamic, efficient, 3d reconstruction, compression, compact, survey, gaussian splatting, 3d gaussian, 4d, high-fidelity, ar  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v1)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v1.pdf)  
  Keywords: semantic, slam, localization, robotics, understanding, survey, gaussian splatting, 3d gaussian, nerf, mapping, ar  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: efficient, semantic, slam, localization, robotics, survey, gaussian splatting, mapping, 3d gaussian, high-fidelity, ar  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: 4d, geometry, survey, motion, gaussian splatting, 3d gaussian, fast, nerf, ar  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: efficient, 3d reconstruction, avatar, lighting, survey, real-time rendering, face, efficient rendering, gaussian splatting, 3d gaussian, animation, ar  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: human, efficient, lightweight, understanding, survey, gaussian splatting, nerf, ar  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: efficient, slam, understanding, survey, neural rendering, gaussian splatting, 3d gaussian, fast, nerf, ar  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: segmentation, semantic, lighting, understanding, compact, survey, gaussian splatting, 3d gaussian, nerf, high-fidelity, ar  
- **[A Study of the Framework and Real-World Applications of Language Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: efficient, semantic, robotics, understanding, survey, gaussian splatting, 3d gaussian, nerf, ar  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: human, robotics, survey, gaussian splatting, 3d gaussian, nerf, ar  

### Acceleration

*Showing the latest 50 out of 249 papers*

- **[Fast 2DGS: Efficient Image Representation with Deep Gaussian Prior](https://arxiv.org/abs/2512.12774v1)**  
  Authors: Hao Wang, Ashish Bastola, Chaoyi Zhou, Wenhui Zhu, Xiwen Chen, Xuanzhao Dong, Siyu Huang, Abolfazl Razi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.12774v1.pdf)  
  Keywords: efficient, lightweight, real-time rendering, gaussian splatting, fast, high-fidelity, ar  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: ray tracing, compact, real-time rendering, gaussian splatting, 3d gaussian, fast, high-fidelity, ar  
- **[Lightweight 3D Gaussian Splatting Compression via Video Codec](https://arxiv.org/abs/2512.11186v1)**  
  Authors: Qi Yang, Geert Van Der Auwera, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11186v1.pdf)  
  Keywords: lightweight, compression, gaussian splatting, 3d gaussian, fast, ar  
- **[GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](https://arxiv.org/abs/2512.10939v1)**  
  Authors: Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10939v1.pdf)  
  Keywords: avatar, head, gaussian splatting, tracking, fast, mapping, ar  
- **[Long-LRM++: Preserving Fine Details in Feed-Forward Wide-Coverage Reconstruction](https://arxiv.org/abs/2512.10267v1)**  
  Authors: Chen Ziwen, Hao Tan, Peng Wang, Zexiang Xu, Li Fuxin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10267v1.pdf)  
  Keywords: lightweight, compression, real-time rendering, gaussian splatting, ar  
- **[Splatent: Splatting Diffusion Latents for Novel View Synthesis](https://arxiv.org/abs/2512.09923v1)**  
  Authors: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09923v1.pdf)  
  Keywords: efficient, 3d reconstruction, face, efficient rendering, gaussian splatting, sparse-view, 3d gaussian, ar  
- **[MoRel: Long-Range Flicker-Free 4D Motion Modeling via Anchor Relay-based Bidirectional Blending with Hierarchical Densification](https://arxiv.org/abs/2512.09270v1)**  
  Authors: Sangwoon Kwak, Weeyoung Kwon, Jun Young Jeong, Geonho Kim, Won-Sik Cheong, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09270v1.pdf)  
  Keywords: dynamic, efficient, deformation, motion, real-time rendering, gaussian splatting, 3d gaussian, 4d, ar  
- **[HybridSplat: Fast Reflection-baked Gaussian Tracing using Hybrid Splatting](https://arxiv.org/abs/2512.08334v2)**  
  Authors: Chang Liu, Hongliang Yuan, Lianghao Zhang, Sichao Wang, Jianwei Guo, Shi-Sheng Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08334v2.pdf)  
  Keywords: fast, reflection, face, gaussian splatting, 3d gaussian, acceleration, nerf, high-fidelity, ar  
- **[Multi-view Pyramid Transformer: Look Coarser to See Broader](https://arxiv.org/abs/2512.07806v1)**  
  Authors: Gyeongjin Kang, Seungkwon Yang, Seungtae Nam, Younggeun Lee, Jungwoo Kim, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07806v1.pdf)  
  Keywords: compact, gaussian splatting, 3d gaussian, fast, ar  
- **[MeshSplatting: Differentiable Rendering with Opaque Meshes](https://arxiv.org/abs/2512.06818v1)**  
  Authors: Jan Held, Sanghyun Son, Renaud Vandeghen, Daniel Rebain, Matheus Gadelha, Yi Zhou, Anthony Cioppa, Ming C. Lin, Marc Van Droogenbroeck, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.06818v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://meshsplatting.github.io/.)  
  Keywords: efficient, geometry, neural rendering, real-time rendering, face, gaussian splatting, vr, 3d gaussian, fast, nerf, ar  

### Applications

*Showing the latest 50 out of 995 papers*

- **[Computer vision training dataset generation for robotic environments using Gaussian splatting](https://arxiv.org/abs/2512.13411v1)**  
  Authors: Patryk Niżeniec, Marcin Iwanowski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13411v1.pdf)  
  Keywords: shadow, segmentation, efficient, gaussian splatting, 3d gaussian, ar  
- **[Light Field Based 6DoF Tracking of Previously Unobserved Objects](https://arxiv.org/abs/2512.13007v1)**  
  Authors: Nikolai Goncharov, James L. Gray, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13007v1.pdf)  
  Keywords: semantic, autonomous driving, robotics, reflection, tracking, ar  
- **[Qonvolution: Towards Learning High-Frequency Signals with Queried Convolution](https://arxiv.org/abs/2512.12898v1)**  
  Authors: Abhinav Kumar, Tristan Aumentado-Armstrong, Lazar Valkov, Gopal Sharma, Alex Levinshtein, Radek Grzeszczuk, Suren Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.12898v1.pdf)  
  Keywords: gaussian splatting, ar  
- **[Fast 2DGS: Efficient Image Representation with Deep Gaussian Prior](https://arxiv.org/abs/2512.12774v1)**  
  Authors: Hao Wang, Ashish Bastola, Chaoyi Zhou, Wenhui Zhu, Xiwen Chen, Xuanzhao Dong, Siyu Huang, Abolfazl Razi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.12774v1.pdf)  
  Keywords: efficient, lightweight, real-time rendering, gaussian splatting, fast, high-fidelity, ar  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: ray tracing, compact, real-time rendering, gaussian splatting, 3d gaussian, fast, high-fidelity, ar  
- **[Prior-Enhanced Gaussian Splatting for Dynamic Scene Reconstruction from Casual Video](https://arxiv.org/abs/2512.11356v1)**  
  Authors: Meng-Li Shih, Ying-Huan Chen, Yu-Lun Liu, Brian Curless  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11356v1.pdf)  
  Keywords: segmentation, dynamic, geometry, motion, gaussian splatting, ar  
- **[Lightweight 3D Gaussian Splatting Compression via Video Codec](https://arxiv.org/abs/2512.11186v1)**  
  Authors: Qi Yang, Geert Van Der Auwera, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11186v1.pdf)  
  Keywords: lightweight, compression, gaussian splatting, 3d gaussian, fast, ar  
- **[GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](https://arxiv.org/abs/2512.10939v1)**  
  Authors: Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10939v1.pdf)  
  Keywords: avatar, head, gaussian splatting, tracking, fast, mapping, ar  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: high-fidelity, deformation, face, gaussian splatting, mapping, ar  
- **[Neural Hamiltonian Deformation Fields for Dynamic Scene Rendering](https://arxiv.org/abs/2512.10424v1)**  
  Authors: Hai-Long Qin, Sixian Wang, Guo Lu, Jincheng Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10424v1.pdf)  
  Keywords: dynamic, deformation, motion, gaussian splatting, mapping, ar  

### Avatar Generation

*Showing the latest 50 out of 343 papers*

- **[GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](https://arxiv.org/abs/2512.10939v1)**  
  Authors: Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10939v1.pdf)  
  Keywords: avatar, head, gaussian splatting, tracking, fast, mapping, ar  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: high-fidelity, deformation, face, gaussian splatting, mapping, ar  
- **[Splatent: Splatting Diffusion Latents for Novel View Synthesis](https://arxiv.org/abs/2512.09923v1)**  
  Authors: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09923v1.pdf)  
  Keywords: efficient, 3d reconstruction, face, efficient rendering, gaussian splatting, sparse-view, 3d gaussian, ar  
- **[YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos](https://arxiv.org/abs/2512.09903v1)**  
  Authors: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09903v1.pdf)  
  Keywords: human, localization, compact, gaussian splatting, mapping, 3d gaussian, recognition, ar  
- **[Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video](https://arxiv.org/abs/2512.09335v2)**  
  Authors: Seonghwa Choi, Moonkyeong Choi, Mingyu Jang, Jaekyung Kim, Jianfei Cai, Wen-Huang Cheng, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09335v2.pdf)  
  Keywords: human, relighting, dynamic, relightable, avatar, lighting, deformation, motion, gaussian splatting, body, 3d gaussian, nerf, high-fidelity, ar  
- **[GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars](https://arxiv.org/abs/2512.09162v1)**  
  Authors: Kelian Baert, Mae Younes, Francois Bourel, Marc Christie, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09162v1.pdf)  
  Keywords: relighting, efficient, relightable, avatar, lighting, geometry, head, gaussian splatting, mapping, ar  
- **[Visionary: The World Model Carrier Built on WebGPU-Powered Gaussian Splatting Platform](https://arxiv.org/abs/2512.08478v1)**  
  Authors: Yuning Gong, Yifei Liu, Yifan Zhan, Muyao Niu, Xueying Li, Yuanjun Liao, Jiaming Chen, Yuanyuan Gao, Jiaqi Chen, Minming Chen, Li Zhou, Yuning Zhang, Wei Wang, Xiaoqing Hou, Huaxi Huang, Shixiang Tang, Le Ma, Dingwen Zhang, Xue Yang, Junchi Yan, Yanchi Zhang, Yinqiang Zheng, Xiao Sun, Zhihang Zhong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08478v1.pdf)  
  Keywords: dynamic, efficient, lightweight, avatar, neural rendering, gaussian splatting, 3d gaussian, 4d, ar  
- **[HybridSplat: Fast Reflection-baked Gaussian Tracing using Hybrid Splatting](https://arxiv.org/abs/2512.08334v2)**  
  Authors: Chang Liu, Hongliang Yuan, Lianghao Zhang, Sichao Wang, Jianwei Guo, Shi-Sheng Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08334v2.pdf)  
  Keywords: fast, reflection, face, gaussian splatting, 3d gaussian, acceleration, nerf, high-fidelity, ar  
- **[Tessellation GS: Neural Mesh Gaussians for Robust Monocular Reconstruction of Dynamic Objects](https://arxiv.org/abs/2512.07381v1)**  
  Authors: Shuohan Tao, Boyao Zhou, Hanzhang Tu, Yuwang Wang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07381v1.pdf)  
  Keywords: dynamic, deformation, face, gaussian splatting, sparse-view, 3d gaussian, ar  
- **[MuSASplat: Efficient Sparse-View 3D Gaussian Splats via Lightweight Multi-Scale Adaptation](https://arxiv.org/abs/2512.07165v1)**  
  Authors: Muyu Xu, Fangneng Zhan, Xiaoqin Zhang, Ling Shao, Shijian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07165v1.pdf)  
  Keywords: efficient, lightweight, head, gaussian splatting, sparse-view, 3d gaussian, ar  

### Dynamic Scene

*Showing the latest 50 out of 400 papers*

- **[Prior-Enhanced Gaussian Splatting for Dynamic Scene Reconstruction from Casual Video](https://arxiv.org/abs/2512.11356v1)**  
  Authors: Meng-Li Shih, Ying-Huan Chen, Yu-Lun Liu, Brian Curless  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11356v1.pdf)  
  Keywords: segmentation, dynamic, geometry, motion, gaussian splatting, ar  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: high-fidelity, deformation, face, gaussian splatting, mapping, ar  
- **[Neural Hamiltonian Deformation Fields for Dynamic Scene Rendering](https://arxiv.org/abs/2512.10424v1)**  
  Authors: Hai-Long Qin, Sixian Wang, Guo Lu, Jincheng Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10424v1.pdf)  
  Keywords: dynamic, deformation, motion, gaussian splatting, mapping, ar  
- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v1)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: ar, 3d reconstruction, motion, gaussian splatting, 3d gaussian, high-fidelity, sparse view  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: ray tracing, dynamic, 3d reconstruction, geometry, reflection, gaussian splatting, high-fidelity, ar  
- **[ReMoSPLAT: Reactive Mobile Manipulation Control on a Gaussian Splat](https://arxiv.org/abs/2512.09656v1)**  
  Authors: Nicolas Marticorena, Tobias Fischer, Niko Suenderhauf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09656v1.pdf)  
  Keywords: motion, efficient, ar  
- **[Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video](https://arxiv.org/abs/2512.09335v2)**  
  Authors: Seonghwa Choi, Moonkyeong Choi, Mingyu Jang, Jaekyung Kim, Jianfei Cai, Wen-Huang Cheng, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09335v2.pdf)  
  Keywords: human, relighting, dynamic, relightable, avatar, lighting, deformation, motion, gaussian splatting, body, 3d gaussian, nerf, high-fidelity, ar  
- **[MoRel: Long-Range Flicker-Free 4D Motion Modeling via Anchor Relay-based Bidirectional Blending with Hierarchical Densification](https://arxiv.org/abs/2512.09270v1)**  
  Authors: Sangwoon Kwak, Weeyoung Kwon, Jun Young Jeong, Geonho Kim, Won-Sik Cheong, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09270v1.pdf)  
  Keywords: dynamic, efficient, deformation, motion, real-time rendering, gaussian splatting, 3d gaussian, 4d, ar  
- **[Visionary: The World Model Carrier Built on WebGPU-Powered Gaussian Splatting Platform](https://arxiv.org/abs/2512.08478v1)**  
  Authors: Yuning Gong, Yifei Liu, Yifan Zhan, Muyao Niu, Xueying Li, Yuanjun Liao, Jiaming Chen, Yuanyuan Gao, Jiaqi Chen, Minming Chen, Li Zhou, Yuning Zhang, Wei Wang, Xiaoqing Hou, Huaxi Huang, Shixiang Tang, Le Ma, Dingwen Zhang, Xue Yang, Junchi Yan, Yanchi Zhang, Yinqiang Zheng, Xiao Sun, Zhihang Zhong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08478v1.pdf)  
  Keywords: dynamic, efficient, lightweight, avatar, neural rendering, gaussian splatting, 3d gaussian, 4d, ar  
- **[Tessellation GS: Neural Mesh Gaussians for Robust Monocular Reconstruction of Dynamic Objects](https://arxiv.org/abs/2512.07381v1)**  
  Authors: Shuohan Tao, Boyao Zhou, Hanzhang Tu, Yuwang Wang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07381v1.pdf)  
  Keywords: dynamic, deformation, face, gaussian splatting, sparse-view, 3d gaussian, ar  

### Few-shot

*Showing the latest 50 out of 84 papers*

- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v1)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: ar, 3d reconstruction, motion, gaussian splatting, 3d gaussian, high-fidelity, sparse view  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: relighting, segmentation, lighting, geometry, light transport, gaussian splatting, sparse-view, ar  
- **[Splatent: Splatting Diffusion Latents for Novel View Synthesis](https://arxiv.org/abs/2512.09923v1)**  
  Authors: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09923v1.pdf)  
  Keywords: efficient, 3d reconstruction, face, efficient rendering, gaussian splatting, sparse-view, 3d gaussian, ar  
- **[Tessellation GS: Neural Mesh Gaussians for Robust Monocular Reconstruction of Dynamic Objects](https://arxiv.org/abs/2512.07381v1)**  
  Authors: Shuohan Tao, Boyao Zhou, Hanzhang Tu, Yuwang Wang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07381v1.pdf)  
  Keywords: dynamic, deformation, face, gaussian splatting, sparse-view, 3d gaussian, ar  
- **[MuSASplat: Efficient Sparse-View 3D Gaussian Splats via Lightweight Multi-Scale Adaptation](https://arxiv.org/abs/2512.07165v1)**  
  Authors: Muyu Xu, Fangneng Zhan, Xiaoqin Zhang, Ling Shao, Shijian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07165v1.pdf)  
  Keywords: efficient, lightweight, head, gaussian splatting, sparse-view, 3d gaussian, ar  
- **[C3G: Learning Compact 3D Representations with 2K Gaussians](https://arxiv.org/abs/2512.04021v1)**  
  Authors: Honggyu An, Jaewoo Jung, Mungyeom Kim, Sunghwan Hong, Chaehyun Kim, Kazumi Fukuda, Minkyeong Jeon, Jisang Han, Takuya Narihira, Hyuna Ko, Junsu Kim, Yuki Mitsufuji, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04021v1.pdf)  
  Keywords: segmentation, efficient, ar, understanding, compact, head, gaussian splatting, 3d gaussian, sparse view  
- **[Cross-Temporal 3D Gaussian Splatting for Sparse-View Guided Scene Update](https://arxiv.org/abs/2512.00534v1)**  
  Authors: Zeyuan An, Yanghang Xiao, Zhiying Leng, Frederick W. B. Li, Xiaohui Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00534v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, sparse-view, 3d gaussian, sparse view  
- **[Relightable Holoported Characters: Capturing and Relighting Dynamic Human Performance from Sparse Views](https://arxiv.org/abs/2512.00255v1)**  
  Authors: Kunwar Maheep Singh, Jianchun Chen, Vladislav Golyanik, Stephan J. Garbin, Thabo Beeler, Rishabh Dabral, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.00255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/RHC/)  
  Keywords: human, relighting, dynamic, efficient, ar, relightable, lighting, geometry, motion, illumination, body, sparse-view, 3d gaussian, tracking, sparse view  
- **[Observer Actor: Active Vision Imitation Learning with Sparse View Gaussian Splatting](https://arxiv.org/abs/2511.18140v1)**  
  Authors: Yilong Wang, Cheng Qian, Ruomeng Fan, Edward Johns  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18140v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://obact.github.io.)  
  Keywords: dynamic, ar, gaussian splatting, 3d gaussian, sparse view  
- **[Frequency-Adaptive Sharpness Regularization for Improving 3D Gaussian Splatting Generalization](https://arxiv.org/abs/2511.17918v1)**  
  Authors: Youngsik Yun, Dongjun Gu, Youngjung Uh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.17918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bbangsik13.github.io/FASR.)  
  Keywords: 3d gaussian, few-shot, gaussian splatting, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 346 papers*

- **[Prior-Enhanced Gaussian Splatting for Dynamic Scene Reconstruction from Casual Video](https://arxiv.org/abs/2512.11356v1)**  
  Authors: Meng-Li Shih, Ying-Huan Chen, Yu-Lun Liu, Brian Curless  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11356v1.pdf)  
  Keywords: segmentation, dynamic, geometry, motion, gaussian splatting, ar  
- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v1)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: ar, 3d reconstruction, motion, gaussian splatting, 3d gaussian, high-fidelity, sparse view  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: ray tracing, dynamic, 3d reconstruction, geometry, reflection, gaussian splatting, high-fidelity, ar  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: relighting, segmentation, lighting, geometry, light transport, gaussian splatting, sparse-view, ar  
- **[Splatent: Splatting Diffusion Latents for Novel View Synthesis](https://arxiv.org/abs/2512.09923v1)**  
  Authors: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09923v1.pdf)  
  Keywords: efficient, 3d reconstruction, face, efficient rendering, gaussian splatting, sparse-view, 3d gaussian, ar  
- **[GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars](https://arxiv.org/abs/2512.09162v1)**  
  Authors: Kelian Baert, Mae Younes, Francois Bourel, Marc Christie, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09162v1.pdf)  
  Keywords: relighting, efficient, relightable, avatar, lighting, geometry, head, gaussian splatting, mapping, ar  
- **[OpenMonoGS-SLAM: Monocular Gaussian Splatting SLAM with Open-set Semantics](https://arxiv.org/abs/2512.08625v1)**  
  Authors: Jisang Yoo, Gyeongjin Kang, Hyun-kyu Ko, Hyeonwoo Yu, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08625v1.pdf)  
  Keywords: segmentation, semantic, slam, geometry, localization, understanding, robotics, gaussian splatting, tracking, vr, 3d gaussian, mapping, ar  
- **[On-the-fly Large-scale 3D Reconstruction from Multi-Camera Rigs](https://arxiv.org/abs/2512.08498v1)**  
  Authors: Yijia Guo, Tong Hu, Zhiwei Li, Liwen Hu, Keming Qian, Xitong Lin, Shengbo Chen, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08498v1.pdf)  
  Keywords: efficient, lightweight, 3d reconstruction, gaussian splatting, 3d gaussian, ar  
- **[STRinGS: Selective Text Refinement in Gaussian Splatting](https://arxiv.org/abs/2512.07230v1)**  
  Authors: Abhinav Raundhal, Gaurav Behera, P J Narayanan, Ravi Kiran Sarvadevabhatla, Makarand Tapaswi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07230v1.pdf)  
  Keywords: semantic, 3d reconstruction, understanding, gaussian splatting, 3d gaussian, ar  
- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197v1)**  
  Authors: Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07197v1.pdf)  
  Keywords: dynamic, efficient, 3d reconstruction, compression, compact, survey, gaussian splatting, 3d gaussian, 4d, high-fidelity, ar  

### Large Scene

*Showing the latest 50 out of 73 papers*

- **[Flux4D: Flow-based Unsupervised 4D Reconstruction](https://arxiv.org/abs/2512.03210v1)**  
  Authors: Jingkang Wang, Henry Che, Yun Chen, Ze Yang, Lily Goli, Sivabalan Manivasagam, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03210v1.pdf)  
  Keywords: dynamic, efficient, 4d, outdoor, robotics, motion, gaussian splatting, 3d gaussian, nerf, ar  
- **[PhysGS: Bayesian-Inferred Gaussian Splatting for Physical Property Estimation](https://arxiv.org/abs/2511.18570v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18570v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://samchopra2003.github.io/physgs.)  
  Keywords: outdoor, 3d reconstruction, geometry, understanding, gaussian splatting, 3d gaussian, ar  
- **[Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525v1)**  
  Authors: Samarth Chopra, Jing Liang, Gershom Seneviratne, Yonghan Lee, Jaehoon Choi, Jianyu An, Stephen Cheng, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.18525v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://splatblox.github.io)  
  Keywords: outdoor, semantic, geometry, gaussian splatting, fast, ar  
- **[Training-Free Multi-View Extension of IC-Light for Textual Position-Aware Scene Relighting](https://arxiv.org/abs/2511.13684v1)**  
  Authors: Jiangnan Ye, Jiedong Zhuang, Lianrui Mu, Wenjie Zheng, Jiaqi Hu, Xingze Zou, Jing Wang, Haoji Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.13684v1.pdf)  
  Keywords: relighting, efficient, segmentation, outdoor, semantic, lighting, geometry, face, illumination, gaussian splatting, high-fidelity, ar  
- **[Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes](https://arxiv.org/abs/2511.06765v1)**  
  Authors: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06765v1.pdf)  
  Keywords: outdoor, geometry, gaussian splatting, 3d gaussian, high-fidelity, ar  
- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632v1)**  
  Authors: Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.06632v1.pdf)  
  Keywords: human, dynamic, 4d, autonomous driving, gaussian splatting, urban scene, ar  
- **[CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting](https://arxiv.org/abs/2511.04951v1)**  
  Authors: Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2511.04951v1.pdf)  
  Keywords: large scene, head, gaussian splatting, 3d gaussian, fast, ar  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: outdoor, slam, geometry, understanding, motion, gaussian splatting, 3d gaussian, mapping, ar  
- **[D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction](https://arxiv.org/abs/2510.25173v2)**  
  Authors: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25173v2.pdf)  
  Keywords: autonomous driving, geometry, gaussian splatting, urban scene, ar  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: 3d reconstruction, semantic, face, gaussian splatting, urban scene, ar  

### Model Compression

*Showing the latest 50 out of 401 papers*

- **[Computer vision training dataset generation for robotic environments using Gaussian splatting](https://arxiv.org/abs/2512.13411v1)**  
  Authors: Patryk Niżeniec, Marcin Iwanowski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13411v1.pdf)  
  Keywords: shadow, segmentation, efficient, gaussian splatting, 3d gaussian, ar  
- **[Fast 2DGS: Efficient Image Representation with Deep Gaussian Prior](https://arxiv.org/abs/2512.12774v1)**  
  Authors: Hao Wang, Ashish Bastola, Chaoyi Zhou, Wenhui Zhu, Xiwen Chen, Xuanzhao Dong, Siyu Huang, Abolfazl Razi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.12774v1.pdf)  
  Keywords: efficient, lightweight, real-time rendering, gaussian splatting, fast, high-fidelity, ar  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: ray tracing, compact, real-time rendering, gaussian splatting, 3d gaussian, fast, high-fidelity, ar  
- **[Lightweight 3D Gaussian Splatting Compression via Video Codec](https://arxiv.org/abs/2512.11186v1)**  
  Authors: Qi Yang, Geert Van Der Auwera, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11186v1.pdf)  
  Keywords: lightweight, compression, gaussian splatting, 3d gaussian, fast, ar  
- **[Long-LRM++: Preserving Fine Details in Feed-Forward Wide-Coverage Reconstruction](https://arxiv.org/abs/2512.10267v1)**  
  Authors: Chen Ziwen, Hao Tan, Peng Wang, Zexiang Xu, Li Fuxin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10267v1.pdf)  
  Keywords: lightweight, compression, real-time rendering, gaussian splatting, ar  
- **[Splatent: Splatting Diffusion Latents for Novel View Synthesis](https://arxiv.org/abs/2512.09923v1)**  
  Authors: Or Hirschorn, Omer Sela, Inbar Huberman-Spiegelglas, Netalee Efrat, Eli Alshan, Ianir Ideses, Frederic Devernay, Yochai Zvik, Lior Fritz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09923v1.pdf)  
  Keywords: efficient, 3d reconstruction, face, efficient rendering, gaussian splatting, sparse-view, 3d gaussian, ar  
- **[YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos](https://arxiv.org/abs/2512.09903v1)**  
  Authors: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09903v1.pdf)  
  Keywords: human, localization, compact, gaussian splatting, mapping, 3d gaussian, recognition, ar  
- **[ReMoSPLAT: Reactive Mobile Manipulation Control on a Gaussian Splat](https://arxiv.org/abs/2512.09656v1)**  
  Authors: Nicolas Marticorena, Tobias Fischer, Niko Suenderhauf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09656v1.pdf)  
  Keywords: motion, efficient, ar  
- **[MoRel: Long-Range Flicker-Free 4D Motion Modeling via Anchor Relay-based Bidirectional Blending with Hierarchical Densification](https://arxiv.org/abs/2512.09270v1)**  
  Authors: Sangwoon Kwak, Weeyoung Kwon, Jun Young Jeong, Geonho Kim, Won-Sik Cheong, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09270v1.pdf)  
  Keywords: dynamic, efficient, deformation, motion, real-time rendering, gaussian splatting, 3d gaussian, 4d, ar  
- **[GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars](https://arxiv.org/abs/2512.09162v1)**  
  Authors: Kelian Baert, Mae Younes, Francois Bourel, Marc Christie, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09162v1.pdf)  
  Keywords: relighting, efficient, relightable, avatar, lighting, geometry, head, gaussian splatting, mapping, ar  

### Quality Enhancement

*Showing the latest 50 out of 193 papers*

- **[Fast 2DGS: Efficient Image Representation with Deep Gaussian Prior](https://arxiv.org/abs/2512.12774v1)**  
  Authors: Hao Wang, Ashish Bastola, Chaoyi Zhou, Wenhui Zhu, Xiwen Chen, Xuanzhao Dong, Siyu Huang, Abolfazl Razi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.12774v1.pdf)  
  Keywords: efficient, lightweight, real-time rendering, gaussian splatting, fast, high-fidelity, ar  
- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: ray tracing, compact, real-time rendering, gaussian splatting, 3d gaussian, fast, high-fidelity, ar  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: high-fidelity, deformation, face, gaussian splatting, mapping, ar  
- **[Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views](https://arxiv.org/abs/2512.10369v1)**  
  Authors: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10369v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://potatobigroom.github.io/CoherentGS/.)  
  Keywords: ar, 3d reconstruction, motion, gaussian splatting, 3d gaussian, high-fidelity, sparse view  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: ray tracing, dynamic, 3d reconstruction, geometry, reflection, gaussian splatting, high-fidelity, ar  
- **[Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video](https://arxiv.org/abs/2512.09335v2)**  
  Authors: Seonghwa Choi, Moonkyeong Choi, Mingyu Jang, Jaekyung Kim, Jianfei Cai, Wen-Huang Cheng, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09335v2.pdf)  
  Keywords: human, relighting, dynamic, relightable, avatar, lighting, deformation, motion, gaussian splatting, body, 3d gaussian, nerf, high-fidelity, ar  
- **[HybridSplat: Fast Reflection-baked Gaussian Tracing using Hybrid Splatting](https://arxiv.org/abs/2512.08334v2)**  
  Authors: Chang Liu, Hongliang Yuan, Lianghao Zhang, Sichao Wang, Jianwei Guo, Shi-Sheng Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08334v2.pdf)  
  Keywords: fast, reflection, face, gaussian splatting, 3d gaussian, acceleration, nerf, high-fidelity, ar  
- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197v1)**  
  Authors: Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07197v1.pdf)  
  Keywords: dynamic, efficient, 3d reconstruction, compression, compact, survey, gaussian splatting, 3d gaussian, 4d, high-fidelity, ar  
- **[AGORA: Adversarial Generation Of Real-time Animatable 3D Gaussian Head Avatars](https://arxiv.org/abs/2512.06438v2)**  
  Authors: Ramazan Fazylov, Sergey Zagoruyko, Aleksandr Parkin, Stamatis Lefkimmiatis, Ivan Laptev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.06438v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ramazan793.github.io/AGORA/)  
  Keywords: human, dynamic, lightweight, avatar, deformation, head, gaussian splatting, vr, 3d gaussian, nerf, high-fidelity, ar  
- **[TriaGS: Differentiable Triangulation-Guided Geometric Consistency for 3D Gaussian Splatting](https://arxiv.org/abs/2512.06269v1)**  
  Authors: Quan Tran, Tuan Dang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.06269v1.pdf)  
  Keywords: geometry, face, gaussian splatting, 3d gaussian, high-fidelity, ar  

### Ray Tracing

- **[Moment-Based 3D Gaussian Splatting: Resolving Volumetric Occlusion with Order-Independent Transmittance](https://arxiv.org/abs/2512.11800v1)**  
  Authors: Jan U. Müller, Robin Tim Landsgesell, Leif Van Holland, Patrick Stotko, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11800v1.pdf)  
  Keywords: ray tracing, compact, real-time rendering, gaussian splatting, 3d gaussian, fast, high-fidelity, ar  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: ray tracing, dynamic, 3d reconstruction, geometry, reflection, gaussian splatting, high-fidelity, ar  
- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: ray tracing, geometry, reflection, illumination, gaussian splatting, ar  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: efficient, geometry, gaussian splatting, 3d gaussian, ray marching, ar  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: ray tracing, shadow, efficient, relightable, lighting, real-time rendering, face, light transport, gaussian splatting, ar  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: relighting, efficient, global illumination, lighting, geometry, reflection, light transport, illumination, gaussian splatting, ar  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v2)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v2.pdf)  
  Keywords: ray tracing, dynamic, gaussian splatting, fast, 4d, ar  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: ray tracing, relighting, lighting, geometry, reflection, face, gaussian splatting, illumination, 3d gaussian, nerf, high-fidelity, ar  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: shadow, relighting, dynamic, outdoor, relightable, global illumination, lighting, face, gaussian splatting, illumination, 3d gaussian, ar  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: dynamic, lighting, face, path tracing, gaussian splatting, 3d gaussian, ar  

### Relighting

*Showing the latest 50 out of 125 papers*

- **[Computer vision training dataset generation for robotic environments using Gaussian splatting](https://arxiv.org/abs/2512.13411v1)**  
  Authors: Patryk Niżeniec, Marcin Iwanowski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13411v1.pdf)  
  Keywords: shadow, segmentation, efficient, gaussian splatting, 3d gaussian, ar  
- **[Light Field Based 6DoF Tracking of Previously Unobserved Objects](https://arxiv.org/abs/2512.13007v1)**  
  Authors: Nikolai Goncharov, James L. Gray, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13007v1.pdf)  
  Keywords: semantic, autonomous driving, robotics, reflection, tracking, ar  
- **[TraceFlow: Dynamic 3D Reconstruction of Specular Scenes Driven by Ray Tracing](https://arxiv.org/abs/2512.10095v1)**  
  Authors: Jiachen Tao, Junyi Wu, Haoxuan Wang, Zongxin Yang, Dawen Cai, Yan Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10095v1.pdf)  
  Keywords: ray tracing, dynamic, 3d reconstruction, geometry, reflection, gaussian splatting, high-fidelity, ar  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: relighting, segmentation, lighting, geometry, light transport, gaussian splatting, sparse-view, ar  
- **[Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video](https://arxiv.org/abs/2512.09335v2)**  
  Authors: Seonghwa Choi, Moonkyeong Choi, Mingyu Jang, Jaekyung Kim, Jianfei Cai, Wen-Huang Cheng, Sanghoon Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09335v2.pdf)  
  Keywords: human, relighting, dynamic, relightable, avatar, lighting, deformation, motion, gaussian splatting, body, 3d gaussian, nerf, high-fidelity, ar  
- **[GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars](https://arxiv.org/abs/2512.09162v1)**  
  Authors: Kelian Baert, Mae Younes, Francois Bourel, Marc Christie, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09162v1.pdf)  
  Keywords: relighting, efficient, relightable, avatar, lighting, geometry, head, gaussian splatting, mapping, ar  
- **[HybridSplat: Fast Reflection-baked Gaussian Tracing using Hybrid Splatting](https://arxiv.org/abs/2512.08334v2)**  
  Authors: Chang Liu, Hongliang Yuan, Lianghao Zhang, Sichao Wang, Jianwei Guo, Shi-Sheng Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08334v2.pdf)  
  Keywords: fast, reflection, face, gaussian splatting, 3d gaussian, acceleration, nerf, high-fidelity, ar  
- **[COREA: Coarse-to-Fine 3D Representation Alignment Between Relightable 3D Gaussians and SDF via Bidirectional 3D-to-3D Supervision](https://arxiv.org/abs/2512.07107v2)**  
  Authors: Jaeyoon Lee, Hojoon Jung, Sungtae Hwang, Jihyong Oh, Jongwon Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07107v2.pdf)  
  Keywords: relighting, relightable, lighting, geometry, face, gaussian splatting, 3d gaussian, ar  
- **[RobustSplat++: Decoupling Densification, Dynamics, and Illumination for In-the-Wild 3DGS](https://arxiv.org/abs/2512.04815v1)**  
  Authors: Chuanyu Fu, Guanying Chen, Yuqi Zhang, Kunbin Yao, Yuan Xiong, Chuan Huang, Shuguang Cui, Yasuyuki Matsushita, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04815v1.pdf)  
  Keywords: dynamic, semantic, illumination, gaussian splatting, 3d gaussian, ar  
- **[PolarGuide-GSDR: 3D Gaussian Splatting Driven by Polarization Priors and Deferred Reflection for Real-World Reflective Scenes](https://arxiv.org/abs/2512.02664v1)**  
  Authors: Derui Shan, Qian Qiao, Hao Lu, Tao Du, Peng Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02664v1.pdf)  
  Keywords: efficient, geometry, real-time rendering, reflection, efficient rendering, face, gaussian splatting, 3d gaussian, nerf, high-fidelity, ar  

### SLAM

*Showing the latest 50 out of 148 papers*

- **[Light Field Based 6DoF Tracking of Previously Unobserved Objects](https://arxiv.org/abs/2512.13007v1)**  
  Authors: Nikolai Goncharov, James L. Gray, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13007v1.pdf)  
  Keywords: semantic, autonomous driving, robotics, reflection, tracking, ar  
- **[GaussianHeadTalk: Wobble-Free 3D Talking Heads with Audio Driven Gaussian Splatting](https://arxiv.org/abs/2512.10939v1)**  
  Authors: Madhav Agarwal, Mingtian Zhang, Laura Sevilla-Lara, Steven McDonagh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10939v1.pdf)  
  Keywords: avatar, head, gaussian splatting, tracking, fast, mapping, ar  
- **[DeMapGS: Simultaneous Mesh Deformation and Surface Attribute Mapping via Gaussian Splatting](https://arxiv.org/abs/2512.10572v1)**  
  Authors: Shuyi Zhou, Shengze Zhong, Kenshi Takayama, Takafumi Taketomi, Takeshi Oishi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10572v1.pdf)  
  Keywords: high-fidelity, deformation, face, gaussian splatting, mapping, ar  
- **[Neural Hamiltonian Deformation Fields for Dynamic Scene Rendering](https://arxiv.org/abs/2512.10424v1)**  
  Authors: Hai-Long Qin, Sixian Wang, Guo Lu, Jincheng Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.10424v1.pdf)  
  Keywords: dynamic, deformation, motion, gaussian splatting, mapping, ar  
- **[YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos](https://arxiv.org/abs/2512.09903v1)**  
  Authors: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09903v1.pdf)  
  Keywords: human, localization, compact, gaussian splatting, mapping, 3d gaussian, recognition, ar  
- **[GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars](https://arxiv.org/abs/2512.09162v1)**  
  Authors: Kelian Baert, Mae Younes, Francois Bourel, Marc Christie, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09162v1.pdf)  
  Keywords: relighting, efficient, relightable, avatar, lighting, geometry, head, gaussian splatting, mapping, ar  
- **[OpenMonoGS-SLAM: Monocular Gaussian Splatting SLAM with Open-set Semantics](https://arxiv.org/abs/2512.08625v1)**  
  Authors: Jisang Yoo, Gyeongjin Kang, Hyun-kyu Ko, Hyeonwoo Yu, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08625v1.pdf)  
  Keywords: segmentation, semantic, slam, geometry, localization, understanding, robotics, gaussian splatting, tracking, vr, 3d gaussian, mapping, ar  
- **[Tracking-Guided 4D Generation: Foundation-Tracker Motion Priors for 3D Model Animation](https://arxiv.org/abs/2512.06158v1)**  
  Authors: Su Sun, Cheng Zhao, Himangi Mittal, Gaurav Mittal, Rohith Kukkala, Yingjie Victor Chen, Mei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.06158v1.pdf)  
  Keywords: dynamic, motion, gaussian splatting, tracking, 4d, animation, ar  
- **[Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding](https://arxiv.org/abs/2512.03601v1)**  
  Authors: Haoran Zhou, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hrzhou2.github.io/motion4d-web/.)  
  Keywords: dynamic, segmentation, semantic, geometry, understanding, motion, gaussian splatting, tracking, 4d, ar  
- **[What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models](https://arxiv.org/abs/2512.03422v1)**  
  Authors: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03422v1.pdf)  
  Keywords: semantic, slam, localization, robotics, understanding, survey, gaussian splatting, 3d gaussian, nerf, mapping, ar  

### Scene Understanding

*Showing the latest 50 out of 208 papers*

- **[Computer vision training dataset generation for robotic environments using Gaussian splatting](https://arxiv.org/abs/2512.13411v1)**  
  Authors: Patryk Niżeniec, Marcin Iwanowski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13411v1.pdf)  
  Keywords: shadow, segmentation, efficient, gaussian splatting, 3d gaussian, ar  
- **[Light Field Based 6DoF Tracking of Previously Unobserved Objects](https://arxiv.org/abs/2512.13007v1)**  
  Authors: Nikolai Goncharov, James L. Gray, Donald G. Dansereau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.13007v1.pdf)  
  Keywords: semantic, autonomous driving, robotics, reflection, tracking, ar  
- **[Prior-Enhanced Gaussian Splatting for Dynamic Scene Reconstruction from Casual Video](https://arxiv.org/abs/2512.11356v1)**  
  Authors: Meng-Li Shih, Ying-Huan Chen, Yu-Lun Liu, Brian Curless  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11356v1.pdf)  
  Keywords: segmentation, dynamic, geometry, motion, gaussian splatting, ar  
- **[GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures](https://arxiv.org/abs/2512.09925v1)**  
  Authors: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://patrickbail.github.io/gains/)  
  Keywords: relighting, segmentation, lighting, geometry, light transport, gaussian splatting, sparse-view, ar  
- **[YOPO-Nav: Visual Navigation using 3DGS Graphs from One-Pass Videos](https://arxiv.org/abs/2512.09903v1)**  
  Authors: Ryan Meegan, Adam D'Souza, Bryan Bo Cao, Shubham Jain, Kristin Dana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.09903v1.pdf)  
  Keywords: human, localization, compact, gaussian splatting, mapping, 3d gaussian, recognition, ar  
- **[OpenMonoGS-SLAM: Monocular Gaussian Splatting SLAM with Open-set Semantics](https://arxiv.org/abs/2512.08625v1)**  
  Authors: Jisang Yoo, Gyeongjin Kang, Hyun-kyu Ko, Hyeonwoo Yu, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08625v1.pdf)  
  Keywords: segmentation, semantic, slam, geometry, localization, understanding, robotics, gaussian splatting, tracking, vr, 3d gaussian, mapping, ar  
- **[Zero-Splat TeleAssist: A Zero-Shot Pose Estimation Framework for Semantic Teleoperation](https://arxiv.org/abs/2512.08271v1)**  
  Authors: Srijan Dokania, Dharini Raghavan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08271v1.pdf)  
  Keywords: segmentation, semantic, gaussian splatting, 3d gaussian, ar  
- **[STRinGS: Selective Text Refinement in Gaussian Splatting](https://arxiv.org/abs/2512.07230v1)**  
  Authors: Abhinav Raundhal, Gaurav Behera, P J Narayanan, Ravi Kiran Sarvadevabhatla, Makarand Tapaswi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.07230v1.pdf)  
  Keywords: semantic, 3d reconstruction, understanding, gaussian splatting, 3d gaussian, ar  
- **[4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer](https://arxiv.org/abs/2512.05060v1)**  
  Authors: Xianfeng Wu, Yajing Bai, Minghan Li, Xianzu Wu, Xueqi Zhao, Zhongyuan Lai, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05060v1.pdf)  
  Keywords: dynamic, 4d, semantic, geometry, understanding, gaussian splatting, nerf, ar  
- **[RobustSplat++: Decoupling Densification, Dynamics, and Illumination for In-the-Wild 3DGS](https://arxiv.org/abs/2512.04815v1)**  
  Authors: Chuanyu Fu, Guanying Chen, Yuqi Zhang, Kunbin Yao, Yuan Xiong, Chuan Huang, Shuguang Cui, Yasuyuki Matsushita, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.04815v1.pdf)  
  Keywords: dynamic, semantic, illumination, gaussian splatting, 3d gaussian, ar  



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