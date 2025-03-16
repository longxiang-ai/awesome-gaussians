# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-03-16 00:53:53

## Categories

- [3DGS Surveys](#3dgs-surveys) (25 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (414 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1461 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (495 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (548 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (101 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (482 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (77 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (554 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (239 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (33 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (160 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (219 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (260 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, real-time rendering, dynamic, survey  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: semantic, ar, geometry, survey  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, real-time rendering, survey, compression, 3d reconstruction, nerf  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, 4d, motion, dynamic, survey, deformation, nerf  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, ray tracing, survey  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: face, lighting, ar, 3d gaussian, reflection, slam, outdoor, dynamic, geometry, survey, mapping, localization, tracking  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: illumination, gaussian splatting, 3d gaussian, ar, survey, recognition  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: lighting, gaussian splatting, ar, autonomous driving, robotics, semantic, high-fidelity, dynamic, compact, geometry, survey, 3d reconstruction, nerf  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, real-time rendering, robotics, survey, understanding, nerf  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: lighting, gaussian splatting, 3d gaussian, ar, high-fidelity, survey, nerf  

### Acceleration

*Showing the latest 50 out of 414 papers*

- **[Hybrid Rendering for Multimodal Autonomous Driving: Merging Neural and Physics-Based Simulation](https://arxiv.org/abs/2503.09464v1)**  
  Authors: Máté Tóth, Péter Kovács, Zoltán Bendefy, Zoltán Hortsin, Balázs Teréki, Tamás Matuszka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09464v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, segmentation, ar, autonomous driving, real-time rendering, dynamic, nerf  
- **[Better Together: Unified Motion Capture and 3D Avatar Reconstruction](https://arxiv.org/abs/2503.09293v1)**  
  Authors: Arthur Moreau, Mohammed Brahimi, Richard Shaw, Athanasios Papaioannou, Thomas Tanay, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09293v1.pdf)  
  Keywords: ar, 3d gaussian, body, real-time rendering, avatar, motion, human  
- **[FPGS: Feed-Forward Semantic-aware Photorealistic Style Transfer of Large-Scale Gaussian Splatting](https://arxiv.org/abs/2503.09635v1)**  
  Authors: GeonU Kim, Kim Youwang, Lee Hyoseok, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09635v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kim-geonu.github.io/FPGS/)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, real-time rendering, semantic, dynamic  
- **[TT-GaussOcc: Test-Time Compute for Self-Supervised Occupancy Prediction via Spatio-Temporal Gaussian Splatting](https://arxiv.org/abs/2503.08485v1)**  
  Authors: Fengyi Zhang, Huitong Yang, Zheng Zhang, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08485v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, fast, semantic, dynamic, geometry, understanding  
- **[S3R-GS: Streamlining the Pipeline for Large-Scale Street Scene Reconstruction](https://arxiv.org/abs/2503.08217v1)**  
  Authors: Guangting Zheng, Jiajun Deng, Xiaomeng Chu, Yu Yuan, Houqiang Li, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08217v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, efficient rendering, dynamic, head, 3d reconstruction  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, real-time rendering, dynamic, survey  
- **[MVGSR: Multi-View Consistency Gaussian Splatting for Robust Surface Reconstruction](https://arxiv.org/abs/2503.08093v2)**  
  Authors: Chenfeng Hou, Qi Xun Yeo, Mengqi Guo, Yongxin Su, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08093v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mvgsr.github.io).)  
  Keywords: face, gaussian splatting, 3d gaussian, segmentation, ar, fast, dynamic, lightweight  
- **[7DGS: Unified Spatial-Temporal-Angular Gaussian Splatting](https://arxiv.org/abs/2503.07946v1)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07946v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/7dgs/.)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, real-time rendering, 4d, dynamic  
- **[Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields](https://arxiv.org/abs/2503.06762v1)**  
  Authors: Abdelaziz Bouzidi, Hamid Laga, Hazem Wannous  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06762v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, fast, compact, geometry, 3d reconstruction, acceleration, lightweight  
- **[Pixel to Gaussian: Ultra-Fast Continuous Super-Resolution with 2D Gaussian Modeling](https://arxiv.org/abs/2503.06617v1)**  
  Authors: Long Peng, Anran Wu, Wenbo Li, Peizhe Xia, Xueyuan Dai, Xinjie Zhang, Xin Di, Haoze Sun, Renjing Pei, Yang Wang, Yang Cao, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06617v1.pdf)  
  Keywords: gaussian splatting, fast, mapping, ar  

### Applications

*Showing the latest 50 out of 1461 papers*

- **[LHM: Large Animatable Human Reconstruction Model from a Single Image in Seconds](https://arxiv.org/abs/2503.10625v1)**  
  Authors: Lingteng Qiu, Xiaodong Gu, Peihao Li, Qi Zuo, Weichao Shen, Junfei Zhang, Kejie Qiu, Weihao Yuan, Guanying Chen, Zilong Dong, Liefeng Bo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10625v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, body, ar, efficient, avatar, high-fidelity, head, geometry, deformation, human  
- **[MuDG: Taming Multi-modal Diffusion with Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2503.10604v1)**  
  Authors: Yingshuang Zou, Yikang Ding, Chuanrui Zhang, Jiazhe Guo, Bohan Li, Xiaoyang Lyu, Feiyang Tan, Xiaojuan Qi, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10604v1.pdf)  
  Keywords: gaussian splatting, ar, autonomous driving, semantic, urban scene  
- **[4D LangSplat: 4D Language Gaussian Splatting via Multimodal Large Language Models](https://arxiv.org/abs/2503.10437v1)**  
  Authors: Wanhua Li, Renping Zhou, Jiawei Zhou, Yingwei Song, Johannes Herter, Minghan Qin, Gao Huang, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10437v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, semantic, 4d, dynamic  
- **[VicaSplat: A Single Run is All You Need for 3D Gaussian Splatting and Camera Estimation from Unposed Video Frames](https://arxiv.org/abs/2503.10286v1)**  
  Authors: Zhiqi Li, Chengrui Dong, Yiming Chen, Zhangchi Huang, Peidong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10286v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lizhiqi49.github.io/VicaSplat.)  
  Keywords: gaussian splatting, 3d gaussian, head, ar  
- **[ROODI: Reconstructing Occluded Objects with Denoising Inpainters](https://arxiv.org/abs/2503.10256v1)**  
  Authors: Yeonjin Chang, Erqun Dong, Seunghyeon Seo, Nojun Kwak, Kwang Moo Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10256v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar  
- **[GS-SDF: LiDAR-Augmented Gaussian Splatting and Neural SDF for Geometrically Consistent Rendering and Reconstruction](https://arxiv.org/abs/2503.10170v1)**  
  Authors: Jianheng Liu, Yunfei Wan, Bowen Wang, Chunran Zheng, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10170v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/GS-SDF?style=social)](https://github.com/hku-mars/GS-SDF)  
  Keywords: face, gaussian splatting, ar, efficient, autonomous driving, robotics, high-fidelity, geometry  
- **[3D Student Splatting and Scooping](https://arxiv.org/abs/2503.10148v1)**  
  Authors: Jialin Zhu, Jiangbei Yue, Feixiang He, He Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10148v1.pdf)  
  Keywords: neural rendering, gaussian splatting, 3d gaussian, ar  
- **[GaussHDR: High Dynamic Range Gaussian Splatting via Learning Unified 3D and 2D Local Tone Mapping](https://arxiv.org/abs/2503.10143v1)**  
  Authors: Jinfeng Liu, Lingtong Kong, Bo Li, Dan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10143v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, dynamic, mapping  
- **[AI-assisted 3D Preservation and Reconstruction of Temple Arts](https://arxiv.org/abs/2503.10031v1)**  
  Authors: Naai-Jung Shih  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10031v1.pdf)  
  Keywords: face, ar, 3d reconstruction, animation, nerf  
- **[TGP: Two-modal occupancy prediction with 3D Gaussian and sparse points for 3D Environment Awareness](https://arxiv.org/abs/2503.09941v1)**  
  Authors: Mu Chen, Wenyu Chen, Mingchuan Yang, Yuan Zhang, Tao Han, Xinchi Li, Yunlong Li, Huaici Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09941v1.pdf)  
  Keywords: face, ar, 3d gaussian, autonomous driving, robotics, semantic, dynamic, understanding  

### Avatar Generation

*Showing the latest 50 out of 495 papers*

- **[LHM: Large Animatable Human Reconstruction Model from a Single Image in Seconds](https://arxiv.org/abs/2503.10625v1)**  
  Authors: Lingteng Qiu, Xiaodong Gu, Peihao Li, Qi Zuo, Weichao Shen, Junfei Zhang, Kejie Qiu, Weihao Yuan, Guanying Chen, Zilong Dong, Liefeng Bo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10625v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, body, ar, efficient, avatar, high-fidelity, head, geometry, deformation, human  
- **[VicaSplat: A Single Run is All You Need for 3D Gaussian Splatting and Camera Estimation from Unposed Video Frames](https://arxiv.org/abs/2503.10286v1)**  
  Authors: Zhiqi Li, Chengrui Dong, Yiming Chen, Zhangchi Huang, Peidong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10286v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lizhiqi49.github.io/VicaSplat.)  
  Keywords: gaussian splatting, 3d gaussian, head, ar  
- **[GS-SDF: LiDAR-Augmented Gaussian Splatting and Neural SDF for Geometrically Consistent Rendering and Reconstruction](https://arxiv.org/abs/2503.10170v1)**  
  Authors: Jianheng Liu, Yunfei Wan, Bowen Wang, Chunran Zheng, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10170v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/GS-SDF?style=social)](https://github.com/hku-mars/GS-SDF)  
  Keywords: face, gaussian splatting, ar, efficient, autonomous driving, robotics, high-fidelity, geometry  
- **[AI-assisted 3D Preservation and Reconstruction of Temple Arts](https://arxiv.org/abs/2503.10031v1)**  
  Authors: Naai-Jung Shih  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10031v1.pdf)  
  Keywords: face, ar, 3d reconstruction, animation, nerf  
- **[TGP: Two-modal occupancy prediction with 3D Gaussian and sparse points for 3D Environment Awareness](https://arxiv.org/abs/2503.09941v1)**  
  Authors: Mu Chen, Wenyu Chen, Mingchuan Yang, Yuan Zhang, Tao Han, Xinchi Li, Yunlong Li, Huaici Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09941v1.pdf)  
  Keywords: face, ar, 3d gaussian, autonomous driving, robotics, semantic, dynamic, understanding  
- **[Hybrid Rendering for Multimodal Autonomous Driving: Merging Neural and Physics-Based Simulation](https://arxiv.org/abs/2503.09464v1)**  
  Authors: Máté Tóth, Péter Kovács, Zoltán Bendefy, Zoltán Hortsin, Balázs Teréki, Tamás Matuszka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09464v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, segmentation, ar, autonomous driving, real-time rendering, dynamic, nerf  
- **[Online Language Splatting](https://arxiv.org/abs/2503.09447v1)**  
  Authors: Saimouli Katragadda, Cho-Ying Wu, Yuliang Guo, Xinyu Huang, Guoquan Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09447v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, slam, efficient, dynamic, mapping, human  
- **[GASPACHO: Gaussian Splatting for Controllable Humans and Objects](https://arxiv.org/abs/2503.09342v1)**  
  Authors: Aymen Mir, Arthur Moreau, Helisa Dhamo, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09342v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, deformation, human  
- **[Better Together: Unified Motion Capture and 3D Avatar Reconstruction](https://arxiv.org/abs/2503.09293v1)**  
  Authors: Arthur Moreau, Mohammed Brahimi, Richard Shaw, Athanasios Papaioannou, Thomas Tanay, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09293v1.pdf)  
  Keywords: ar, 3d gaussian, body, real-time rendering, avatar, motion, human  
- **[Physics-Aware Human-Object Rendering from Sparse Views via 3D Gaussian Splatting](https://arxiv.org/abs/2503.09640v1)**  
  Authors: Weiquan Wang, Jun Xiao, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09640v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, sparse-view, sparse view, human  

### Dynamic Scene

*Showing the latest 50 out of 548 papers*

- **[LHM: Large Animatable Human Reconstruction Model from a Single Image in Seconds](https://arxiv.org/abs/2503.10625v1)**  
  Authors: Lingteng Qiu, Xiaodong Gu, Peihao Li, Qi Zuo, Weichao Shen, Junfei Zhang, Kejie Qiu, Weihao Yuan, Guanying Chen, Zilong Dong, Liefeng Bo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10625v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, body, ar, efficient, avatar, high-fidelity, head, geometry, deformation, human  
- **[4D LangSplat: 4D Language Gaussian Splatting via Multimodal Large Language Models](https://arxiv.org/abs/2503.10437v1)**  
  Authors: Wanhua Li, Renping Zhou, Jiawei Zhou, Yingwei Song, Johannes Herter, Minghan Qin, Gao Huang, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10437v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, semantic, 4d, dynamic  
- **[GaussHDR: High Dynamic Range Gaussian Splatting via Learning Unified 3D and 2D Local Tone Mapping](https://arxiv.org/abs/2503.10143v1)**  
  Authors: Jinfeng Liu, Lingtong Kong, Bo Li, Dan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10143v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, dynamic, mapping  
- **[AI-assisted 3D Preservation and Reconstruction of Temple Arts](https://arxiv.org/abs/2503.10031v1)**  
  Authors: Naai-Jung Shih  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10031v1.pdf)  
  Keywords: face, ar, 3d reconstruction, animation, nerf  
- **[TGP: Two-modal occupancy prediction with 3D Gaussian and sparse points for 3D Environment Awareness](https://arxiv.org/abs/2503.09941v1)**  
  Authors: Mu Chen, Wenyu Chen, Mingchuan Yang, Yuan Zhang, Tao Han, Xinchi Li, Yunlong Li, Huaici Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09941v1.pdf)  
  Keywords: face, ar, 3d gaussian, autonomous driving, robotics, semantic, dynamic, understanding  
- **[Hybrid Rendering for Multimodal Autonomous Driving: Merging Neural and Physics-Based Simulation](https://arxiv.org/abs/2503.09464v1)**  
  Authors: Máté Tóth, Péter Kovács, Zoltán Bendefy, Zoltán Hortsin, Balázs Teréki, Tamás Matuszka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09464v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, segmentation, ar, autonomous driving, real-time rendering, dynamic, nerf  
- **[Online Language Splatting](https://arxiv.org/abs/2503.09447v1)**  
  Authors: Saimouli Katragadda, Cho-Ying Wu, Yuliang Guo, Xinyu Huang, Guoquan Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09447v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, slam, efficient, dynamic, mapping, human  
- **[GASPACHO: Gaussian Splatting for Controllable Humans and Objects](https://arxiv.org/abs/2503.09342v1)**  
  Authors: Aymen Mir, Arthur Moreau, Helisa Dhamo, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09342v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, deformation, human  
- **[SDD-4DGS: Static-Dynamic Aware Decoupling in Gaussian Splatting for 4D Scene Reconstruction](https://arxiv.org/abs/2503.09332v1)**  
  Authors: Dai Sun, Huhao Guan, Kun Zhang, Xike Xie, S. Kevin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09332v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, 4d, motion, dynamic  
- **[Better Together: Unified Motion Capture and 3D Avatar Reconstruction](https://arxiv.org/abs/2503.09293v1)**  
  Authors: Arthur Moreau, Mohammed Brahimi, Richard Shaw, Athanasios Papaioannou, Thomas Tanay, Zhensong Zhang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09293v1.pdf)  
  Keywords: ar, 3d gaussian, body, real-time rendering, avatar, motion, human  

### Few-shot

*Showing the latest 50 out of 101 papers*

- **[Physics-Aware Human-Object Rendering from Sparse Views via 3D Gaussian Splatting](https://arxiv.org/abs/2503.09640v1)**  
  Authors: Weiquan Wang, Jun Xiao, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09640v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, sparse-view, sparse view, human  
- **[Multi-Modal 3D Mesh Reconstruction from Images and Text](https://arxiv.org/abs/2503.07190v1)**  
  Authors: Melvin Reka, Tessa Pulli, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07190v1.pdf)  
  Keywords: gaussian splatting, ar, few-shot, robotics, geometry, 3d reconstruction  
- **[GaussianCAD: Robust Self-Supervised CAD Reconstruction from Three Orthographic Views Using 3D Gaussian Splatting](https://arxiv.org/abs/2503.05161v1)**  
  Authors: Zheng Zhou, Zhe Li, Bo Yu, Lina Hu, Liang Dong, Zijian Yang, Xiaoli Liu, Ning Xu, Ziwei Wang, Yonghao Dang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05161v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, sparse-view, 3d reconstruction  
- **[S2Gaussian: Sparse-View Super-Resolution 3D Gaussian Splatting](https://arxiv.org/abs/2503.04314v1)**  
  Authors: Yecong Wan, Mingwen Shao, Yuanshuo Cheng, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04314v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, sparse-view, sparse view, geometry  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: gaussian splatting, ar, human, efficient, few-shot, semantic, neural rendering, nerf  
- **[Seeing A 3D World in A Grain of Sand](https://arxiv.org/abs/2503.00260v1)**  
  Authors: Yufan Zhang, Yu Ji, Yu Guo, Jinwei Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00260v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, ar, sparse view, 3d reconstruction  
- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, high-fidelity, sparse view, 3d reconstruction  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: gaussian splatting, ar, slam, real-time rendering, sparse-view, geometry, mapping, tracking, nerf  
- **[DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform](https://arxiv.org/abs/2501.12637v2)**  
  Authors: Hung Nguyen, Blark Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12637v2.pdf)  
  Keywords: ar, fast, few-shot, head, nerf  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, sparse-view, semantic, 4d  

### Geometry Reconstruction

*Showing the latest 50 out of 482 papers*

- **[LHM: Large Animatable Human Reconstruction Model from a Single Image in Seconds](https://arxiv.org/abs/2503.10625v1)**  
  Authors: Lingteng Qiu, Xiaodong Gu, Peihao Li, Qi Zuo, Weichao Shen, Junfei Zhang, Kejie Qiu, Weihao Yuan, Guanying Chen, Zilong Dong, Liefeng Bo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10625v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, body, ar, efficient, avatar, high-fidelity, head, geometry, deformation, human  
- **[GS-SDF: LiDAR-Augmented Gaussian Splatting and Neural SDF for Geometrically Consistent Rendering and Reconstruction](https://arxiv.org/abs/2503.10170v1)**  
  Authors: Jianheng Liu, Yunfei Wan, Bowen Wang, Chunran Zheng, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10170v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/GS-SDF?style=social)](https://github.com/hku-mars/GS-SDF)  
  Keywords: face, gaussian splatting, ar, efficient, autonomous driving, robotics, high-fidelity, geometry  
- **[AI-assisted 3D Preservation and Reconstruction of Temple Arts](https://arxiv.org/abs/2503.10031v1)**  
  Authors: Naai-Jung Shih  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10031v1.pdf)  
  Keywords: face, ar, 3d reconstruction, animation, nerf  
- **[TT-GaussOcc: Test-Time Compute for Self-Supervised Occupancy Prediction via Spatio-Temporal Gaussian Splatting](https://arxiv.org/abs/2503.08485v1)**  
  Authors: Fengyi Zhang, Huitong Yang, Zheng Zhang, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08485v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, fast, semantic, dynamic, geometry, understanding  
- **[MVD-HuGaS: Human Gaussians from a Single Image via 3D Human Multi-view Diffusion Prior](https://arxiv.org/abs/2503.08218v1)**  
  Authors: Kaiqiang Xiong, Ying Feng, Qi Zhang, Jianbo Jiao, Yang Zhao, Zhihao Liang, Huachen Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08218v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, geometry, human  
- **[S3R-GS: Streamlining the Pipeline for Large-Scale Street Scene Reconstruction](https://arxiv.org/abs/2503.08217v1)**  
  Authors: Guangting Zheng, Jiajun Deng, Xiaomeng Chu, Yu Yuan, Houqiang Li, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08217v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, efficient rendering, dynamic, head, 3d reconstruction  
- **[ArticulatedGS: Self-supervised Digital Twin Modeling of Articulated Objects using 3D Gaussian Splatting](https://arxiv.org/abs/2503.08135v1)**  
  Authors: Junfu Guo, Yu Xin, Gaoyi Liu, Kai Xu, Ligang Liu, Ruizhen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08135v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, segmentation, ar, semantic, motion, geometry  
- **[GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats](https://arxiv.org/abs/2503.08071v1)**  
  Authors: Kai Deng, Jian Yang, Shenlong Wang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08071v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, slam, efficient, high-fidelity, outdoor, geometry, mapping, tracking, nerf  
- **[Multi-Modal 3D Mesh Reconstruction from Images and Text](https://arxiv.org/abs/2503.07190v1)**  
  Authors: Melvin Reka, Tessa Pulli, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07190v1.pdf)  
  Keywords: gaussian splatting, ar, few-shot, robotics, geometry, 3d reconstruction  
- **[DirectTriGS: Triplane-based Gaussian Splatting Field Representation for 3D Generation](https://arxiv.org/abs/2503.06900v1)**  
  Authors: Xiaoliang Ju, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06900v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, geometry, ar  

### Large Scene

*Showing the latest 50 out of 77 papers*

- **[MuDG: Taming Multi-modal Diffusion with Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2503.10604v1)**  
  Authors: Yingshuang Zou, Yikang Ding, Chuanrui Zhang, Jiazhe Guo, Bohan Li, Xiaoyang Lyu, Feiyang Tan, Xiaojuan Qi, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10604v1.pdf)  
  Keywords: gaussian splatting, ar, autonomous driving, semantic, urban scene  
- **[GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats](https://arxiv.org/abs/2503.08071v1)**  
  Authors: Kai Deng, Jian Yang, Shenlong Wang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08071v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, slam, efficient, high-fidelity, outdoor, geometry, mapping, tracking, nerf  
- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: semantic, outdoor, gaussian splatting, ar  
- **[OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation](https://arxiv.org/abs/2502.18041v4)**  
  Authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.18041v4.pdf)  
  Keywords: gaussian splatting, 3d gaussian, segmentation, ar, semantic, outdoor  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: gaussian splatting, 3d gaussian, ar, slam, high-fidelity, outdoor, geometry, mapping, tracking  
- **[RadSplatter: Extending 3D Gaussian Splatting to Radio Frequencies for Wireless Radiomap Extrapolation](https://arxiv.org/abs/2502.12686v1)**  
  Authors: Yiheng Wang, Ye Xue, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.12686v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, autonomous driving, efficient, outdoor  
- **[GS-GVINS: A Tightly-integrated GNSS-Visual-Inertial Navigation System Augmented by 3D Gaussian Splatting](https://arxiv.org/abs/2502.10975v1)**  
  Authors: Zelin Zhou, Saurav Uprety, Shichuang Nie, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10975v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, slam, motion, outdoor, dynamic, tracking  
- **[PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression](https://arxiv.org/abs/2502.04843v2)**  
  Authors: Feifei Li, Qi Song, Chi Zhang, Hui Shuai, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04843v2.pdf)  
  Keywords: outdoor, gaussian splatting, ar, nerf  
- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, efficient, outdoor  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: gaussian splatting, ar, slam, outdoor, dynamic, geometry, large scene, mapping, localization, nerf  

### Model Compression

*Showing the latest 50 out of 554 papers*

- **[LHM: Large Animatable Human Reconstruction Model from a Single Image in Seconds](https://arxiv.org/abs/2503.10625v1)**  
  Authors: Lingteng Qiu, Xiaodong Gu, Peihao Li, Qi Zuo, Weichao Shen, Junfei Zhang, Kejie Qiu, Weihao Yuan, Guanying Chen, Zilong Dong, Liefeng Bo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10625v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, body, ar, efficient, avatar, high-fidelity, head, geometry, deformation, human  
- **[4D LangSplat: 4D Language Gaussian Splatting via Multimodal Large Language Models](https://arxiv.org/abs/2503.10437v1)**  
  Authors: Wanhua Li, Renping Zhou, Jiawei Zhou, Yingwei Song, Johannes Herter, Minghan Qin, Gao Huang, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10437v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, semantic, 4d, dynamic  
- **[GS-SDF: LiDAR-Augmented Gaussian Splatting and Neural SDF for Geometrically Consistent Rendering and Reconstruction](https://arxiv.org/abs/2503.10170v1)**  
  Authors: Jianheng Liu, Yunfei Wan, Bowen Wang, Chunran Zheng, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10170v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/GS-SDF?style=social)](https://github.com/hku-mars/GS-SDF)  
  Keywords: face, gaussian splatting, ar, efficient, autonomous driving, robotics, high-fidelity, geometry  
- **[Online Language Splatting](https://arxiv.org/abs/2503.09447v1)**  
  Authors: Saimouli Katragadda, Cho-Ying Wu, Yuliang Guo, Xinyu Huang, Guoquan Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09447v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, slam, efficient, dynamic, mapping, human  
- **[SDD-4DGS: Static-Dynamic Aware Decoupling in Gaussian Splatting for 4D Scene Reconstruction](https://arxiv.org/abs/2503.09332v1)**  
  Authors: Dai Sun, Huhao Guan, Kun Zhang, Xike Xie, S. Kevin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09332v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, 4d, motion, dynamic  
- **[Physics-Aware Human-Object Rendering from Sparse Views via 3D Gaussian Splatting](https://arxiv.org/abs/2503.09640v1)**  
  Authors: Weiquan Wang, Jun Xiao, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09640v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, sparse-view, sparse view, human  
- **[FPGS: Feed-Forward Semantic-aware Photorealistic Style Transfer of Large-Scale Gaussian Splatting](https://arxiv.org/abs/2503.09635v1)**  
  Authors: GeonU Kim, Kim Youwang, Lee Hyoseok, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09635v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kim-geonu.github.io/FPGS/)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, real-time rendering, semantic, dynamic  
- **[PCGS: Progressive Compression of 3D Gaussian Splatting](https://arxiv.org/abs/2503.08511v1)**  
  Authors: Yihang Chen, Mengyao Li, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08511v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YihangChen-ee/PCGS?style=social)](https://github.com/YihangChen-ee/PCGS)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, compact, compression  
- **[Mitigating Ambiguities in 3D Classification with Gaussian Splatting](https://arxiv.org/abs/2503.08352v1)**  
  Authors: Ruiqi Zhang, Hao Zhu, Jingyi Zhao, Qi Zhang, Xun Cao, Zhan Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08352v1.pdf)  
  Keywords: face, gaussian splatting, ar, efficient  
- **[Uni-Gaussians: Unifying Camera and Lidar Simulation with Gaussians for Dynamic Driving Scenarios](https://arxiv.org/abs/2503.08317v1)**  
  Authors: Zikang Yuan, Yuechuan Pu, Hongcheng Luo, Fengtian Lang, Cheng Chi, Teng Li, Yingying Shen, Haiyang Sun, Bing Wang, Xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08317v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, autonomous driving, neural rendering, dynamic, nerf  

### Quality Enhancement

*Showing the latest 50 out of 239 papers*

- **[LHM: Large Animatable Human Reconstruction Model from a Single Image in Seconds](https://arxiv.org/abs/2503.10625v1)**  
  Authors: Lingteng Qiu, Xiaodong Gu, Peihao Li, Qi Zuo, Weichao Shen, Junfei Zhang, Kejie Qiu, Weihao Yuan, Guanying Chen, Zilong Dong, Liefeng Bo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10625v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, body, ar, efficient, avatar, high-fidelity, head, geometry, deformation, human  
- **[GS-SDF: LiDAR-Augmented Gaussian Splatting and Neural SDF for Geometrically Consistent Rendering and Reconstruction](https://arxiv.org/abs/2503.10170v1)**  
  Authors: Jianheng Liu, Yunfei Wan, Bowen Wang, Chunran Zheng, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10170v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/GS-SDF?style=social)](https://github.com/hku-mars/GS-SDF)  
  Keywords: face, gaussian splatting, ar, efficient, autonomous driving, robotics, high-fidelity, geometry  
- **[Motion Blender Gaussian Splatting for Dynamic Reconstruction](https://arxiv.org/abs/2503.09040v1)**  
  Authors: Xinyu Zhang, Haonan Chang, Yuhan Liu, Abdeslam Boularias  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09040v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mlzxy.github.io/mbgs.)  
  Keywords: gaussian splatting, 3d gaussian, ar, high-fidelity, motion, dynamic, nerf  
- **[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://arxiv.org/abs/2503.08224v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08224v1.pdf)  
  Keywords: face, lighting, gaussian splatting, 3d gaussian, ar, deformation, avatar, high-fidelity, head, tracking, relighting, relightable  
- **[MVD-HuGaS: Human Gaussians from a Single Image via 3D Human Multi-view Diffusion Prior](https://arxiv.org/abs/2503.08218v1)**  
  Authors: Kaiqiang Xiong, Ying Feng, Qi Zhang, Jianbo Jiao, Yang Zhao, Zhihao Liang, Huachen Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08218v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, geometry, human  
- **[GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats](https://arxiv.org/abs/2503.08071v1)**  
  Authors: Kai Deng, Jian Yang, Shenlong Wang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08071v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, slam, efficient, high-fidelity, outdoor, geometry, mapping, tracking, nerf  
- **[All That Glitters Is Not Gold: Key-Secured 3D Secrets within 3D Gaussian Splatting](https://arxiv.org/abs/2503.07191v1)**  
  Authors: Yan Ren, Shilin Lu, Adams Wai-Kin Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07191v1.pdf) | [![GitHub](https://img.shields.io/github/stars/RY-Paper/KeySS?style=social)](https://github.com/RY-Paper/KeySS)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, ar  
- **[REArtGS: Reconstructing and Generating Articulated Objects via 3D Gaussian Splatting with Geometric and Motion Constraints](https://arxiv.org/abs/2503.06677v2)**  
  Authors: Di Wu, Liu Liu, Zhou Linli, Anran Huang, Liangtu Song, Qiaojun Yu, Qi Wu, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06677v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sites.google.com/view/reartgs/home.)  
  Keywords: face, gaussian splatting, 3d gaussian, ar, high-fidelity, motion, dynamic, geometry, human  
- **[Bayesian Fields: Task-driven Open-Set Semantic Gaussian Splatting](https://arxiv.org/abs/2503.05949v1)**  
  Authors: Dominic Maggio, Luca Carlone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05949v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MIT-SPARK/Bayesian-Fields?style=social)](https://github.com/MIT-SPARK/Bayesian-Fields)  
  Keywords: gaussian splatting, 3d gaussian, ar, semantic, high-fidelity, mapping, 3d reconstruction  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v2)**  
  Authors: Jiahui Fan, Fujun Luan, Jian Yang, Miloš Hašan, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v2.pdf)  
  Keywords: lighting, gaussian splatting, 3d gaussian, ar, high quality, motion, relighting, relightable, lightweight, human  

### Ray Tracing

- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: face, lighting, ar, efficient, real-time rendering, ray tracing, 4d, dynamic, geometry, tracking, relightable  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: face, lighting, gaussian splatting, shadow, reflection, ray tracing  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, ray tracing, survey  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: light transport, gaussian splatting, ar, reflection, efficient, ray tracing, acceleration  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, reflection, shadow, ar, ray tracing  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, reflection, efficient, ray tracing, relighting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: lighting, gaussian splatting, 3d gaussian, reflection, ar, efficient, real-time rendering, high-fidelity, ray tracing  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: illumination, face, gaussian splatting, ar, efficient, fast, geometry, mapping, global illumination, nerf  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v2)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v2.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, efficient, ray tracing  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: ray tracing, gaussian splatting, 3d gaussian, ar  

### Relighting

*Showing the latest 50 out of 160 papers*

- **[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://arxiv.org/abs/2503.08224v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08224v1.pdf)  
  Keywords: face, lighting, gaussian splatting, 3d gaussian, ar, deformation, avatar, high-fidelity, head, tracking, relighting, relightable  
- **[D3DR: Lighting-Aware Object Insertion in Gaussian Splatting](https://arxiv.org/abs/2503.06740v1)**  
  Authors: Vsevolod Skorokhodov, Nikita Durasov, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06740v1.pdf)  
  Keywords: lighting, gaussian splatting, 3d gaussian, shadow, ar, dynamic, relighting  
- **[Introducing Unbiased Depth into 2D Gaussian Splatting for High-accuracy Surface Reconstruction](https://arxiv.org/abs/2503.06587v1)**  
  Authors: Xiaoming Peng, Yixin Yang, Yang Zhou, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06587v1.pdf)  
  Keywords: face, gaussian splatting, ar, reflection, geometry  
- **[ForestSplats: Deformable transient field for Gaussian Splatting in the Wild](https://arxiv.org/abs/2503.06179v1)**  
  Authors: Wongi Park, Myeongseok Nam, Siwon Kim, Sangwoo Jo, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06179v1.pdf)  
  Keywords: lighting, gaussian splatting, 3d gaussian, ar, efficient, real-time rendering, semantic  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v2)**  
  Authors: Jiahui Fan, Fujun Luan, Jian Yang, Miloš Hašan, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v2.pdf)  
  Keywords: lighting, gaussian splatting, 3d gaussian, ar, high quality, motion, relighting, relightable, lightweight, human  
- **[MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions](https://arxiv.org/abs/2503.05182v1)**  
  Authors: Qingyuan Zhou, Yuehu Gong, Weidong Yang, Jiaze Li, Yeqi Luo, Baixin Xu, Shuhao Li, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05182v1.pdf)  
  Keywords: illumination, face, gaussian splatting, 3d gaussian, ar, high-fidelity, geometry, 3d reconstruction  
- **[EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering](https://arxiv.org/abs/2502.20669v1)**  
  Authors: John J. Han, Jie Ying Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20669v1.pdf)  
  Keywords: face, lighting, gaussian splatting, 3d gaussian, ar, geometry, 3d reconstruction, medical  
- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941v1)**  
  Authors: Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16941v1.pdf)  
  Keywords: lighting, ar, efficient, 4d, nerf  
- **[RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection](https://arxiv.org/abs/2502.13071v1)**  
  Authors: Jingtong Yue, Zhiwei Lin, Xin Lin, Xiaoyu Zhou, Xiangtai Li, Lu Qi, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13071v1.pdf)  
  Keywords: face, lighting, ar, 3d gaussian  
- **[OMG: Opacity Matters in Material Modeling with Gaussian Splatting](https://arxiv.org/abs/2502.10988v2)**  
  Authors: Silong Yong, Venkata Nagarjun Pudureddiyur Manivannan, Bernhard Kerbl, Zifu Wan, Simon Stepputtis, Katia Sycara, Yaqi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10988v2.pdf)  
  Keywords: lighting, gaussian splatting, 3d gaussian, ar, real-time rendering, neural rendering, geometry  

### SLAM

*Showing the latest 50 out of 219 papers*

- **[GaussHDR: High Dynamic Range Gaussian Splatting via Learning Unified 3D and 2D Local Tone Mapping](https://arxiv.org/abs/2503.10143v1)**  
  Authors: Jinfeng Liu, Lingtong Kong, Bo Li, Dan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10143v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, dynamic, mapping  
- **[Online Language Splatting](https://arxiv.org/abs/2503.09447v1)**  
  Authors: Saimouli Katragadda, Cho-Ying Wu, Yuliang Guo, Xinyu Huang, Guoquan Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09447v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, slam, efficient, dynamic, mapping, human  
- **[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://arxiv.org/abs/2503.08224v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08224v1.pdf)  
  Keywords: face, lighting, gaussian splatting, 3d gaussian, ar, deformation, avatar, high-fidelity, head, tracking, relighting, relightable  
- **[GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats](https://arxiv.org/abs/2503.08071v1)**  
  Authors: Kai Deng, Jian Yang, Shenlong Wang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08071v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, slam, efficient, high-fidelity, outdoor, geometry, mapping, tracking, nerf  
- **[POp-GS: Next Best View in 3D-Gaussian Splatting with P-Optimality](https://arxiv.org/abs/2503.07819v1)**  
  Authors: Joey Wilson, Marcelino Almeida, Sachit Mahajan, Martin Labrie, Maani Ghaffari, Omid Ghasemalizadeh, Min Sun, Cheng-Hao Kuo, Arnab Sen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07819v1.pdf)  
  Keywords: slam, gaussian splatting, 3d gaussian, ar  
- **[Pixel to Gaussian: Ultra-Fast Continuous Super-Resolution with 2D Gaussian Modeling](https://arxiv.org/abs/2503.06617v1)**  
  Authors: Long Peng, Anran Wu, Wenbo Li, Peizhe Xia, Xueyuan Dai, Xinjie Zhang, Xin Di, Haoze Sun, Renjing Pei, Yang Wang, Yang Cao, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06617v1.pdf)  
  Keywords: gaussian splatting, fast, mapping, ar  
- **[Bayesian Fields: Task-driven Open-Set Semantic Gaussian Splatting](https://arxiv.org/abs/2503.05949v1)**  
  Authors: Dominic Maggio, Luca Carlone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05949v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MIT-SPARK/Bayesian-Fields?style=social)](https://github.com/MIT-SPARK/Bayesian-Fields)  
  Keywords: gaussian splatting, 3d gaussian, ar, semantic, high-fidelity, mapping, 3d reconstruction  
- **[LiDAR-enhanced 3D Gaussian Splatting Mapping](https://arxiv.org/abs/2503.05425v1)**  
  Authors: Jian Shen, Huai Yu, Ji Wu, Wen Yang, Gui-Song Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05425v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, dynamic, geometry, mapping, tracking  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: ar, efficient, semantic, dynamic, compact, geometry, tracking, human  
- **[GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting](https://arxiv.org/abs/2503.05152v2)**  
  Authors: Kohei Honda, Takeshi Ishita, Yasuhiro Yoshimura, Ryo Yonetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05152v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, head, localization  

### Scene Understanding

*Showing the latest 50 out of 260 papers*

- **[MuDG: Taming Multi-modal Diffusion with Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2503.10604v1)**  
  Authors: Yingshuang Zou, Yikang Ding, Chuanrui Zhang, Jiazhe Guo, Bohan Li, Xiaoyang Lyu, Feiyang Tan, Xiaojuan Qi, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10604v1.pdf)  
  Keywords: gaussian splatting, ar, autonomous driving, semantic, urban scene  
- **[4D LangSplat: 4D Language Gaussian Splatting via Multimodal Large Language Models](https://arxiv.org/abs/2503.10437v1)**  
  Authors: Wanhua Li, Renping Zhou, Jiawei Zhou, Yingwei Song, Johannes Herter, Minghan Qin, Gao Huang, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10437v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, semantic, 4d, dynamic  
- **[TGP: Two-modal occupancy prediction with 3D Gaussian and sparse points for 3D Environment Awareness](https://arxiv.org/abs/2503.09941v1)**  
  Authors: Mu Chen, Wenyu Chen, Mingchuan Yang, Yuan Zhang, Tao Han, Xinchi Li, Yunlong Li, Huaici Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09941v1.pdf)  
  Keywords: face, ar, 3d gaussian, autonomous driving, robotics, semantic, dynamic, understanding  
- **[Hybrid Rendering for Multimodal Autonomous Driving: Merging Neural and Physics-Based Simulation](https://arxiv.org/abs/2503.09464v1)**  
  Authors: Máté Tóth, Péter Kovács, Zoltán Bendefy, Zoltán Hortsin, Balázs Teréki, Tamás Matuszka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09464v1.pdf)  
  Keywords: face, gaussian splatting, 3d gaussian, segmentation, ar, autonomous driving, real-time rendering, dynamic, nerf  
- **[FPGS: Feed-Forward Semantic-aware Photorealistic Style Transfer of Large-Scale Gaussian Splatting](https://arxiv.org/abs/2503.09635v1)**  
  Authors: GeonU Kim, Kim Youwang, Lee Hyoseok, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09635v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kim-geonu.github.io/FPGS/)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, real-time rendering, semantic, dynamic  
- **[TT-GaussOcc: Test-Time Compute for Self-Supervised Occupancy Prediction via Spatio-Temporal Gaussian Splatting](https://arxiv.org/abs/2503.08485v1)**  
  Authors: Fengyi Zhang, Huitong Yang, Zheng Zhang, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08485v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, fast, semantic, dynamic, geometry, understanding  
- **[ArticulatedGS: Self-supervised Digital Twin Modeling of Articulated Objects using 3D Gaussian Splatting](https://arxiv.org/abs/2503.08135v1)**  
  Authors: Junfu Guo, Yu Xin, Gaoyi Liu, Kai Xu, Ligang Liu, Ruizhen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08135v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, segmentation, ar, semantic, motion, geometry  
- **[MVGSR: Multi-View Consistency Gaussian Splatting for Robust Surface Reconstruction](https://arxiv.org/abs/2503.08093v2)**  
  Authors: Chenfeng Hou, Qi Xun Yeo, Mengqi Guo, Yongxin Su, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08093v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mvgsr.github.io).)  
  Keywords: face, gaussian splatting, 3d gaussian, segmentation, ar, fast, dynamic, lightweight  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: semantic, ar, geometry, survey  
- **[CoDa-4DGS: Dynamic Gaussian Splatting with Context and Deformation Awareness for Autonomous Driving](https://arxiv.org/abs/2503.06744v1)**  
  Authors: Rui Song, Chenwei Liang, Yan Xia, Walter Zimmer, Hu Cao, Holger Caesar, Andreas Festag, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06744v1.pdf)  
  Keywords: gaussian splatting, ar, segmentation, autonomous driving, semantic, 4d, dynamic, deformation  



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

## Contribution Guidelines
Feel free to submit Pull Requests to improve this list! Please follow these formats:
- Paper entry format: `**[Paper Title](link)** - Brief description`
- Project entry format: `[Project Name](link) - Project description`

## License
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) 