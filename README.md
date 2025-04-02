# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-04-02 00:52:06

## Categories

- [3DGS Surveys](#3dgs-surveys) (26 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (449 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1580 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (532 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (597 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (110 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (510 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (87 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (601 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (257 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (35 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (172 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (237 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (279 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: gaussian splatting, survey, fast, lighting, 3d reconstruction, motion, ar, dynamic, 3d gaussian  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: gaussian splatting, survey, real-time rendering, ar, dynamic, 3d gaussian  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: semantic, ar, geometry, survey  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: gaussian splatting, nerf, survey, compression, 3d reconstruction, real-time rendering, efficient, ar, 3d gaussian  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: survey, nerf, 4d, lighting, motion, ar, deformation, dynamic, gaussian splatting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, ray tracing, survey, ar, 3d gaussian  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: tracking, survey, outdoor, face, mapping, lighting, localization, ar, geometry, slam, dynamic  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: gaussian splatting, survey, illumination, recognition, ar, 3d gaussian  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: survey, nerf, semantic, robotics, lighting, 3d reconstruction, ar, geometry, autonomous driving, compact, high-fidelity, dynamic, gaussian splatting  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: gaussian splatting, survey, nerf, robotics, understanding, real-time rendering, ar, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 449 papers*

- **[ERUPT: Efficient Rendering with Unposed Patch Transformer](https://arxiv.org/abs/2503.24374v1)**  
  Authors: Maxim V. Shugaev, Vincent Chen, Maxim Karrenbach, Kyle Ashley, Bridget Kennedy, Naresh P. Cuntoor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24374v1.pdf)  
  Keywords: efficient rendering, nerf, efficient, ar, gaussian splatting  
- **[StochasticSplats: Stochastic Rasterization for Sorting-Free 3D Gaussian Splatting](https://arxiv.org/abs/2503.24366v1)**  
  Authors: Shakiba Kheradmand, Delio Vicini, George Kopanas, Dmitry Lagun, Kwang Moo Yi, Mark Matthews, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24366v1.pdf)  
  Keywords: efficient rendering, gaussian splatting, fast, efficient, ar, 3d gaussian  
- **[Gaussian Blending Unit: An Edge GPU Plug-in for Real-Time Gaussian-Based Rendering in AR/VR](https://arxiv.org/abs/2503.23625v1)**  
  Authors: Zhifan Ye, Yonggan Fu, Jingqun Zhang, Leshu Li, Yongan Zhang, Sixu Li, Cheng Wan, Chenxi Wan, Chaojian Li, Sreemanth Prathipati, Yingyan Celine Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23625v1.pdf)  
  Keywords: gaussian splatting, vr, real-time rendering, ar, 3d gaussian  
- **[Enhancing 3D Gaussian Splatting Compression via Spatial Condition-based Prediction](https://arxiv.org/abs/2503.23337v1)**  
  Authors: Jingui Ma, Yang Hu, Luyang Tang, Jiayu Yang, Yongqi Zhai, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23337v1.pdf)  
  Keywords: gaussian splatting, compression, real-time rendering, ar, 3d gaussian  
- **[CityGS-X: A Scalable Architecture for Efficient and Geometrically Accurate Large-Scale Scene Reconstruction](https://arxiv.org/abs/2503.23044v1)**  
  Authors: Yuanyuan Gao, Hao Li, Jiaqi Chen, Zhengyu Zou, Zhihang Zhong, Dingwen Zhang, Xiao Sun, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23044v1.pdf)  
  Keywords: gaussian splatting, fast, face, efficient, ar, dynamic, 3d gaussian  
- **[AH-GS: Augmented 3D Gaussian Splatting for High-Frequency Detail Representation](https://arxiv.org/abs/2503.22324v1)**  
  Authors: Chenyang Xu, XingGuo Deng, Rui Zhong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22324v1.pdf)  
  Keywords: gaussian splatting, nerf, real-time rendering, ar, 3d gaussian  
- **[Disentangled 4D Gaussian Splatting: Towards Faster and More Efficient Dynamic Scene Rendering](https://arxiv.org/abs/2503.22159v2)**  
  Authors: Hao Feng, Hao Sun, Wei Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22159v2.pdf)  
  Keywords: gaussian splatting, fast, 4d, efficient, ar, deformation, dynamic, 3d gaussian  
- **[Time-resolved dynamic CBCT reconstruction using prior-model-free spatiotemporal Gaussian representation (PMF-STGR)](https://arxiv.org/abs/2503.22139v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22139v1.pdf)  
  Keywords: fast, localization, efficient, motion, ar, deformation, dynamic, 3d gaussian  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: nerf, fast, outdoor, efficient, ar, geometry, high-fidelity, dynamic, gaussian splatting, reflection  
- **[Frequency-Aware Gaussian Splatting Decomposition](https://arxiv.org/abs/2503.21226v1)**  
  Authors: Yishai Lavi, Leo Segre, Shai Avidan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21226v1.pdf)  
  Keywords: gaussian splatting, fast, efficient, ar, geometry, dynamic, 3d gaussian  

### Applications

*Showing the latest 50 out of 1580 papers*

- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: sparse-view, face, 3d reconstruction, ar, geometry, gaussian splatting, neural rendering  
- **[ERUPT: Efficient Rendering with Unposed Patch Transformer](https://arxiv.org/abs/2503.24374v1)**  
  Authors: Maxim V. Shugaev, Vincent Chen, Maxim Karrenbach, Kyle Ashley, Bridget Kennedy, Naresh P. Cuntoor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24374v1.pdf)  
  Keywords: efficient rendering, nerf, efficient, ar, gaussian splatting  
- **[StochasticSplats: Stochastic Rasterization for Sorting-Free 3D Gaussian Splatting](https://arxiv.org/abs/2503.24366v1)**  
  Authors: Shakiba Kheradmand, Delio Vicini, George Kopanas, Dmitry Lagun, Kwang Moo Yi, Mark Matthews, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24366v1.pdf)  
  Keywords: efficient rendering, gaussian splatting, fast, efficient, ar, 3d gaussian  
- **[Visual Acoustic Fields](https://arxiv.org/abs/2503.24270v2)**  
  Authors: Yuelei Li, Hyunjin Kim, Fangneng Zhan, Ri-Zhao Qiu, Mazeyu Ji, Xiaojun Shan, Xueyan Zou, Paul Liang, Hanspeter Pfister, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24270v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuelei0428.github.io/projects/Visual-Acoustic-Fields/.)  
  Keywords: gaussian splatting, localization, human, ar, 3d gaussian  
- **[DiET-GS: Diffusion Prior and Event Stream-Assisted Motion Deblurring 3D Gaussian Splatting](https://arxiv.org/abs/2503.24210v1)**  
  Authors: Seungjun Lee, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24210v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://diet-gs.github.io)  
  Keywords: gaussian splatting, motion, ar, dynamic, 3d gaussian  
- **[Learning 3D-Gaussian Simulators from RGB Videos](https://arxiv.org/abs/2503.24009v1)**  
  Authors: Mikel Zhobro, Andreas René Geist, Georg Martius  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24009v1.pdf)  
  Keywords: gaussian splatting, lighting, body, ar, dynamic, 3d gaussian  
- **[ExScene: Free-View 3D Scene Reconstruction with Gaussian Splatting from a Single Image](https://arxiv.org/abs/2503.23881v1)**  
  Authors: Tianyi Gong, Boyan Li, Yifei Zhong, Fangxin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23881v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, ar  
- **[Gaussian Blending Unit: An Edge GPU Plug-in for Real-Time Gaussian-Based Rendering in AR/VR](https://arxiv.org/abs/2503.23625v1)**  
  Authors: Zhifan Ye, Yonggan Fu, Jingqun Zhang, Leshu Li, Yongan Zhang, Sixu Li, Cheng Wan, Chenxi Wan, Chaojian Li, Sreemanth Prathipati, Yingyan Celine Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23625v1.pdf)  
  Keywords: gaussian splatting, vr, real-time rendering, ar, 3d gaussian  
- **[Enhancing 3D Gaussian Splatting Compression via Spatial Condition-based Prediction](https://arxiv.org/abs/2503.23337v1)**  
  Authors: Jingui Ma, Yang Hu, Luyang Tang, Jiayu Yang, Yongqi Zhai, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23337v1.pdf)  
  Keywords: gaussian splatting, compression, real-time rendering, ar, 3d gaussian  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: gaussian splatting, segmentation, semantic, robotics, localization, understanding, ar, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 532 papers*

- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: sparse-view, face, 3d reconstruction, ar, geometry, gaussian splatting, neural rendering  
- **[Visual Acoustic Fields](https://arxiv.org/abs/2503.24270v2)**  
  Authors: Yuelei Li, Hyunjin Kim, Fangneng Zhan, Ri-Zhao Qiu, Mazeyu Ji, Xiaojun Shan, Xueyan Zou, Paul Liang, Hanspeter Pfister, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24270v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuelei0428.github.io/projects/Visual-Acoustic-Fields/.)  
  Keywords: gaussian splatting, localization, human, ar, 3d gaussian  
- **[Learning 3D-Gaussian Simulators from RGB Videos](https://arxiv.org/abs/2503.24009v1)**  
  Authors: Mikel Zhobro, Andreas René Geist, Georg Martius  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24009v1.pdf)  
  Keywords: gaussian splatting, lighting, body, ar, dynamic, 3d gaussian  
- **[CityGS-X: A Scalable Architecture for Efficient and Geometrically Accurate Large-Scale Scene Reconstruction](https://arxiv.org/abs/2503.23044v1)**  
  Authors: Yuanyuan Gao, Hao Li, Jiaqi Chen, Zhengyu Zou, Zhihang Zhong, Dingwen Zhang, Xiao Sun, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23044v1.pdf)  
  Keywords: gaussian splatting, fast, face, efficient, ar, dynamic, 3d gaussian  
- **[Audio-Plane: Audio Factorization Plane Gaussian Splatting for Real-Time Talking Head Synthesis](https://arxiv.org/abs/2503.22605v1)**  
  Authors: Shuai Shen, Wanhua Li, Yunpeng Zhang, Weipeng Hu, Yap-Peng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22605v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sstzal.github.io/Audio-Plane/.)  
  Keywords: head, 4d, ar, compact, dynamic, gaussian splatting  
- **[EndoLRMGS: Complete Endoscopic Scene Reconstruction combining Large Reconstruction Modelling and Gaussian Splatting](https://arxiv.org/abs/2503.22437v1)**  
  Authors: Xu Wang, Shuai Zhang, Baoru Huang, Danail Stoyanov, Evangelos B. Mazomenos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22437v1.pdf)  
  Keywords: ar, face, gaussian splatting  
- **[Follow Your Motion: A Generic Temporal Consistency Portrait Editing Framework with Trajectory Guidance](https://arxiv.org/abs/2503.22225v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22225v1.pdf)  
  Keywords: gaussian splatting, head, face, lighting, efficient, motion, ar, avatar, dynamic, 3d gaussian, relighting  
- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: deformation, 4d, face, motion, ar, high-fidelity, dynamic, gaussian splatting  
- **[PGC: Physics-Based Gaussian Cloth from a Single Pose](https://arxiv.org/abs/2503.20779v1)**  
  Authors: Michelle Guo, Matt Jen-Yuan Chiang, Igor Santesteban, Nikolaos Sarafianos, Hsiao-yu Chen, Oshri Halimi, Aljaž Božič, Shunsuke Saito, Jiajun Wu, C. Karen Liu, Tuur Stuyck, Egor Larionov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys-gaussian-cloth.github.io)  
  Keywords: face, lighting, body, ar, 3d gaussian, relighting  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: gaussian splatting, tracking, 4d, face, 3d reconstruction, ar, deformation, 3d gaussian  

### Dynamic Scene

*Showing the latest 50 out of 597 papers*

- **[DiET-GS: Diffusion Prior and Event Stream-Assisted Motion Deblurring 3D Gaussian Splatting](https://arxiv.org/abs/2503.24210v1)**  
  Authors: Seungjun Lee, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24210v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://diet-gs.github.io)  
  Keywords: gaussian splatting, motion, ar, dynamic, 3d gaussian  
- **[Learning 3D-Gaussian Simulators from RGB Videos](https://arxiv.org/abs/2503.24009v1)**  
  Authors: Mikel Zhobro, Andreas René Geist, Georg Martius  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24009v1.pdf)  
  Keywords: gaussian splatting, lighting, body, ar, dynamic, 3d gaussian  
- **[CityGS-X: A Scalable Architecture for Efficient and Geometrically Accurate Large-Scale Scene Reconstruction](https://arxiv.org/abs/2503.23044v1)**  
  Authors: Yuanyuan Gao, Hao Li, Jiaqi Chen, Zhengyu Zou, Zhihang Zhong, Dingwen Zhang, Xiao Sun, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23044v1.pdf)  
  Keywords: gaussian splatting, fast, face, efficient, ar, dynamic, 3d gaussian  
- **[Audio-Plane: Audio Factorization Plane Gaussian Splatting for Real-Time Talking Head Synthesis](https://arxiv.org/abs/2503.22605v1)**  
  Authors: Shuai Shen, Wanhua Li, Yunpeng Zhang, Weipeng Hu, Yap-Peng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22605v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sstzal.github.io/Audio-Plane/.)  
  Keywords: head, 4d, ar, compact, dynamic, gaussian splatting  
- **[Follow Your Motion: A Generic Temporal Consistency Portrait Editing Framework with Trajectory Guidance](https://arxiv.org/abs/2503.22225v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22225v1.pdf)  
  Keywords: gaussian splatting, head, face, lighting, efficient, motion, ar, avatar, dynamic, 3d gaussian, relighting  
- **[Segment then Splat: A Unified Approach for 3D Open-Vocabulary Segmentation based on Gaussian Splatting](https://arxiv.org/abs/2503.22204v1)**  
  Authors: Yiren Lu, Yunlai Zhou, Yiran Qiao, Chaoda Song, Tuo Liang, Jing Ma, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22204v1.pdf)  
  Keywords: segmentation, robotics, motion, ar, dynamic, gaussian splatting  
- **[Disentangled 4D Gaussian Splatting: Towards Faster and More Efficient Dynamic Scene Rendering](https://arxiv.org/abs/2503.22159v2)**  
  Authors: Hao Feng, Hao Sun, Wei Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22159v2.pdf)  
  Keywords: gaussian splatting, fast, 4d, efficient, ar, deformation, dynamic, 3d gaussian  
- **[Time-resolved dynamic CBCT reconstruction using prior-model-free spatiotemporal Gaussian representation (PMF-STGR)](https://arxiv.org/abs/2503.22139v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22139v1.pdf)  
  Keywords: fast, localization, efficient, motion, ar, deformation, dynamic, 3d gaussian  
- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: deformation, 4d, face, motion, ar, high-fidelity, dynamic, gaussian splatting  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: nerf, fast, outdoor, efficient, ar, geometry, high-fidelity, dynamic, gaussian splatting, reflection  

### Few-shot

*Showing the latest 50 out of 110 papers*

- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: sparse-view, face, 3d reconstruction, ar, geometry, gaussian splatting, neural rendering  
- **[FreeSplat++: Generalizable 3D Gaussian Splatting for Efficient Indoor Scene Reconstruction](https://arxiv.org/abs/2503.22986v1)**  
  Authors: Yunsong Wang, Tianxin Huang, Hanlin Chen, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22986v1.pdf)  
  Keywords: gaussian splatting, sparse view, efficient, ar, 3d gaussian  
- **[CoMapGS: Covisibility Map-based Gaussian Splatting for Sparse Novel View Synthesis](https://arxiv.org/abs/2503.20998v1)**  
  Authors: Youngkyoon Jang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20998v1.pdf)  
  Keywords: ar, few-shot, gaussian splatting, nerf  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: gaussian splatting, sparse-view, illumination, outdoor, ar, 3d gaussian  
- **[NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting](https://arxiv.org/abs/2503.18794v1)**  
  Authors: Yulong Zheng, Zicheng Jiang, Shengfeng He, Yandu Sun, Junyu Dong, Huaidong Zhang, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18794v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://usmizuki.github.io/NexusGS/.)  
  Keywords: gaussian splatting, sparse-view, few-shot, nerf, sparse view, ar, geometry, 3d gaussian  
- **[SplatVoxel: History-Aware Novel View Streaming without Temporal Training](https://arxiv.org/abs/2503.14698v1)**  
  Authors: Yiming Wang, Lucy Chai, Xuan Luo, Michael Niemeyer, Manuel Lagunas, Stephen Lombardi, Siyu Tang, Tiancheng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14698v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://19reborn.github.io/SplatVoxel/)  
  Keywords: sparse-view, tracking, efficient, motion, ar, gaussian splatting  
- **[RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2503.14198v1)**  
  Authors: Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14198v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iSEE-Laboratory/RoGSplat?style=social)](https://github.com/iSEE-Laboratory/RoGSplat)  
  Keywords: gaussian splatting, sparse view, body, human, ar, geometry, high-fidelity, 3d gaussian  
- **[RI3D: Few-Shot Gaussian Splatting With Repair and Inpainting Diffusion Priors](https://arxiv.org/abs/2503.10860v1)**  
  Authors: Avinash Paliwal, Xilong Zhou, Wei Ye, Jinhui Xiong, Rakesh Ranjan, Nima Khademi Kalantari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10860v1.pdf)  
  Keywords: ar, few-shot, gaussian splatting  
- **[Physics-Aware Human-Object Rendering from Sparse Views via 3D Gaussian Splatting](https://arxiv.org/abs/2503.09640v1)**  
  Authors: Weiquan Wang, Jun Xiao, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09640v1.pdf)  
  Keywords: gaussian splatting, sparse-view, sparse view, efficient, human, ar, 3d gaussian  
- **[Multi-Modal 3D Mesh Reconstruction from Images and Text](https://arxiv.org/abs/2503.07190v1)**  
  Authors: Melvin Reka, Tessa Pulli, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07190v1.pdf)  
  Keywords: few-shot, robotics, 3d reconstruction, ar, geometry, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 510 papers*

- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: sparse-view, face, 3d reconstruction, ar, geometry, gaussian splatting, neural rendering  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: nerf, fast, outdoor, efficient, ar, geometry, high-fidelity, dynamic, gaussian splatting, reflection  
- **[LandMarkSystem Technical Report](https://arxiv.org/abs/2503.21364v2)**  
  Authors: Zhenxiang Ma, Zhenyu Yang, Miao Tao, Yuanzhen Zhou, Zeyu He, Yuchang Zhang, Rong Fu, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21364v2.pdf) | [![GitHub](https://img.shields.io/github/stars/InternLandMark/LandMarkSystem?style=social)](https://github.com/InternLandMark/LandMarkSystem)  
  Keywords: gaussian splatting, nerf, 3d reconstruction, efficient, ar, autonomous driving, dynamic, 3d gaussian  
- **[Frequency-Aware Gaussian Splatting Decomposition](https://arxiv.org/abs/2503.21226v1)**  
  Authors: Yishai Lavi, Leo Segre, Shai Avidan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21226v1.pdf)  
  Keywords: gaussian splatting, fast, efficient, ar, geometry, dynamic, 3d gaussian  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: motion, geometry, ar, urban scene, dynamic, gaussian splatting  
- **[EVPGS: Enhanced View Prior Guidance for Splatting-based Extrapolated View Synthesis](https://arxiv.org/abs/2503.21816v1)**  
  Authors: Jiahe Li, Feiyu Wang, Xiaochao Qu, Chengjing Wu, Luoqi Liu, Ting Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21816v1.pdf)  
  Keywords: ar, geometry, gaussian splatting  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: gaussian splatting, tracking, 4d, face, 3d reconstruction, ar, deformation, 3d gaussian  
- **[PartRM: Modeling Part-Level Dynamics with Large Cross-State Reconstruction Model](https://arxiv.org/abs/2503.19913v1)**  
  Authors: Mingju Gao, Yike Pan, Huan-ang Gao, Zongzheng Zhang, Wenyi Li, Hao Dong, Hao Tang, Li Yi, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19913v1.pdf)  
  Keywords: 4d, robotics, understanding, motion, geometry, ar, dynamic, 3d gaussian  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: gaussian splatting, survey, fast, lighting, 3d reconstruction, motion, ar, dynamic, 3d gaussian  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: gaussian splatting, fast, outdoor, real-time rendering, efficient, ar, geometry, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 87 papers*

- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: nerf, fast, outdoor, efficient, ar, geometry, high-fidelity, dynamic, gaussian splatting, reflection  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: motion, geometry, ar, urban scene, dynamic, gaussian splatting  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: gaussian splatting, nerf, fast, real-time rendering, efficient, ar, autonomous driving, urban scene, 3d gaussian  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: gaussian splatting, sparse-view, illumination, outdoor, ar, 3d gaussian  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: outdoor, localization, efficient, ar, gaussian splatting  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: gaussian splatting, fast, outdoor, real-time rendering, efficient, ar, geometry, 3d gaussian  
- **[PanopticSplatting: End-to-End Panoptic Gaussian Splatting](https://arxiv.org/abs/2503.18073v1)**  
  Authors: Yuxuan Xie, Xuan Yu, Changjian Jiang, Sitong Mao, Shunbo Zhou, Rui Fan, Rong Xiong, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18073v1.pdf)  
  Keywords: large scene, segmentation, nerf, understanding, ar, gaussian splatting  
- **[GaussianFocus: Constrained Attention Focus for 3D Gaussian Splatting](https://arxiv.org/abs/2503.17798v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17798v1.pdf)  
  Keywords: large scene, gaussian splatting, 3d reconstruction, ar, 3d gaussian, neural rendering  
- **[OccluGaussian: Occlusion-Aware Gaussian Splatting for Large Scene Reconstruction and Rendering](https://arxiv.org/abs/2503.16177v1)**  
  Authors: Shiyong Liu, Xiao Tang, Zhihao Li, Yingfan He, Chongjie Ye, Jianzhuang Liu, Binxiao Huang, Shunbo Zhou, Xiaofei Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://occlugaussian.github.io.)  
  Keywords: gaussian splatting, large scene, fast, ar, 3d gaussian  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: efficient rendering, outdoor, deformation, efficient, ar, geometry, high-fidelity, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 601 papers*

- **[ERUPT: Efficient Rendering with Unposed Patch Transformer](https://arxiv.org/abs/2503.24374v1)**  
  Authors: Maxim V. Shugaev, Vincent Chen, Maxim Karrenbach, Kyle Ashley, Bridget Kennedy, Naresh P. Cuntoor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24374v1.pdf)  
  Keywords: efficient rendering, nerf, efficient, ar, gaussian splatting  
- **[StochasticSplats: Stochastic Rasterization for Sorting-Free 3D Gaussian Splatting](https://arxiv.org/abs/2503.24366v1)**  
  Authors: Shakiba Kheradmand, Delio Vicini, George Kopanas, Dmitry Lagun, Kwang Moo Yi, Mark Matthews, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24366v1.pdf)  
  Keywords: efficient rendering, gaussian splatting, fast, efficient, ar, 3d gaussian  
- **[Enhancing 3D Gaussian Splatting Compression via Spatial Condition-based Prediction](https://arxiv.org/abs/2503.23337v1)**  
  Authors: Jingui Ma, Yang Hu, Luyang Tang, Jiayu Yang, Yongqi Zhai, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23337v1.pdf)  
  Keywords: gaussian splatting, compression, real-time rendering, ar, 3d gaussian  
- **[NeuralGS: Bridging Neural Fields and 3D Gaussian Splatting for Compact 3D Representations](https://arxiv.org/abs/2503.23162v1)**  
  Authors: Zhenyu Tang, Chaoran Feng, Xinhua Cheng, Wangbo Yu, Junwu Zhang, Yuan Liu, Xiaoxiao Long, Wenping Wang, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23162v1.pdf)  
  Keywords: gaussian splatting, nerf, compression, ar, compact, 3d gaussian  
- **[CityGS-X: A Scalable Architecture for Efficient and Geometrically Accurate Large-Scale Scene Reconstruction](https://arxiv.org/abs/2503.23044v1)**  
  Authors: Yuanyuan Gao, Hao Li, Jiaqi Chen, Zhengyu Zou, Zhihang Zhong, Dingwen Zhang, Xiao Sun, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23044v1.pdf)  
  Keywords: gaussian splatting, fast, face, efficient, ar, dynamic, 3d gaussian  
- **[FreeSplat++: Generalizable 3D Gaussian Splatting for Efficient Indoor Scene Reconstruction](https://arxiv.org/abs/2503.22986v1)**  
  Authors: Yunsong Wang, Tianxin Huang, Hanlin Chen, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22986v1.pdf)  
  Keywords: gaussian splatting, sparse view, efficient, ar, 3d gaussian  
- **[VizFlyt: Perception-centric Pedagogical Framework For Autonomous Aerial Robots](https://arxiv.org/abs/2503.22876v1)**  
  Authors: Kushagra Srivastava, Rutwik Kulkarni, Manoj Velmurugan, Nitin J. Sanket  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22876v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pear.wpi.edu/research/vizflyt.html)  
  Keywords: gaussian splatting, robotics, localization, efficient, ar, 3d gaussian  
- **[Audio-Plane: Audio Factorization Plane Gaussian Splatting for Real-Time Talking Head Synthesis](https://arxiv.org/abs/2503.22605v1)**  
  Authors: Shuai Shen, Wanhua Li, Yunpeng Zhang, Weipeng Hu, Yap-Peng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22605v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sstzal.github.io/Audio-Plane/.)  
  Keywords: head, 4d, ar, compact, dynamic, gaussian splatting  
- **[Follow Your Motion: A Generic Temporal Consistency Portrait Editing Framework with Trajectory Guidance](https://arxiv.org/abs/2503.22225v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22225v1.pdf)  
  Keywords: gaussian splatting, head, face, lighting, efficient, motion, ar, avatar, dynamic, 3d gaussian, relighting  
- **[Disentangled 4D Gaussian Splatting: Towards Faster and More Efficient Dynamic Scene Rendering](https://arxiv.org/abs/2503.22159v2)**  
  Authors: Hao Feng, Hao Sun, Wei Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22159v2.pdf)  
  Keywords: gaussian splatting, fast, 4d, efficient, ar, deformation, dynamic, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 257 papers*

- **[ExScene: Free-View 3D Scene Reconstruction with Gaussian Splatting from a Single Image](https://arxiv.org/abs/2503.23881v1)**  
  Authors: Tianyi Gong, Boyan Li, Yifei Zhong, Fangxin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23881v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, ar  
- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: deformation, 4d, face, motion, ar, high-fidelity, dynamic, gaussian splatting  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: nerf, fast, outdoor, efficient, ar, geometry, high-fidelity, dynamic, gaussian splatting, reflection  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: semantic, robotics, mapping, localization, ar, slam, high-fidelity, dynamic, 3d gaussian  
- **[LLGS: Unsupervised Gaussian Splatting for Image Enhancement and Reconstruction in Pure Dark Environment](https://arxiv.org/abs/2503.18640v1)**  
  Authors: Haoran Wang, Jingwei Huang, Lu Yang, Tianchen Deng, Gaojing Zhang, Mingrui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18640v1.pdf)  
  Keywords: gaussian splatting, robotics, ar, high-fidelity, 3d gaussian  
- **[Unraveling the Effects of Synthetic Data on End-to-End Autonomous Driving](https://arxiv.org/abs/2503.18108v1)**  
  Authors: Junhao Ge, Zuhong Liu, Longteng Fan, Yifan Jiang, Jiaqi Su, Yiming Li, Zhejun Zhang, Siheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18108v1.pdf)  
  Keywords: gaussian splatting, nerf, face, efficient, ar, autonomous driving, high-fidelity, dynamic, 3d gaussian  
- **[PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](https://arxiv.org/abs/2503.17973v1)**  
  Authors: Hanxiao Jiang, Hao-Yu Hsu, Kaifeng Zhang, Hsin-Ni Yu, Shenlong Wang, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17973v1.pdf)  
  Keywords: robotics, motion, geometry, ar, high-fidelity, dynamic  
- **[TaoAvatar: Real-Time Lifelike Full-Body Talking Avatars for Augmented Reality via 3D Gaussian Splatting](https://arxiv.org/abs/2503.17032v1)**  
  Authors: Jianchuan Chen, Jingchuan Hu, Gaige Wang, Zhonghua Jiang, Tiansong Zhou, Zhiwen Chen, Chengfei Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17032v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, body, lightweight, human, ar, avatar, deformation, 3d gaussian  
- **[HandSplat: Embedding-Driven Gaussian Splatting for High-Fidelity Hand Rendering](https://arxiv.org/abs/2503.14736v1)**  
  Authors: Yilan Dong, Haohe Liu, Qing Wang, Jiahao Yang, Wenqing Wang, Gregory Slabaugh, Shanxin Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14736v1.pdf)  
  Keywords: gaussian splatting, efficient, motion, geometry, ar, high-fidelity, dynamic, 3d gaussian  
- **[RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2503.14198v1)**  
  Authors: Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14198v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iSEE-Laboratory/RoGSplat?style=social)](https://github.com/iSEE-Laboratory/RoGSplat)  
  Keywords: gaussian splatting, sparse view, body, human, ar, geometry, high-fidelity, 3d gaussian  

### Ray Tracing

- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: global illumination, fast, illumination, light transport, face, lighting, real-time rendering, dynamic, 3d gaussian  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: gaussian splatting, ray tracing, fast, shadow, ar, reflection, 3d gaussian, neural rendering  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: relightable, tracking, ray tracing, 4d, face, lighting, real-time rendering, efficient, ar, geometry, dynamic  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: ray tracing, face, lighting, shadow, gaussian splatting, reflection  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, ray tracing, survey, ar, 3d gaussian  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: acceleration, ray tracing, light transport, efficient, ar, gaussian splatting, reflection  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: gaussian splatting, ray tracing, shadow, ar, 3d gaussian, reflection  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v2)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v2.pdf)  
  Keywords: ray tracing, lighting, efficient, ar, reflection, gaussian splatting, relighting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v2)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v2.pdf) | [![GitHub](https://img.shields.io/github/stars/nv-tlabs/3dgrut?style=social)](https://github.com/nv-tlabs/3dgrut)  
  Keywords: gaussian splatting, ray tracing, lighting, real-time rendering, efficient, ar, high-fidelity, 3d gaussian, reflection  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: global illumination, fast, illumination, nerf, face, mapping, efficient, ar, geometry, gaussian splatting  

### Relighting

*Showing the latest 50 out of 172 papers*

- **[Learning 3D-Gaussian Simulators from RGB Videos](https://arxiv.org/abs/2503.24009v1)**  
  Authors: Mikel Zhobro, Andreas René Geist, Georg Martius  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24009v1.pdf)  
  Keywords: gaussian splatting, lighting, body, ar, dynamic, 3d gaussian  
- **[TranSplat: Lighting-Consistent Cross-Scene Object Transfer with 3D Gaussian Splatting](https://arxiv.org/abs/2503.22676v1)**  
  Authors: Boyang, Yu, Yanlin Jin, Ashok Veeraraghavan, Akshat Dave, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22676v1.pdf)  
  Keywords: gaussian splatting, segmentation, lighting, ar, 3d gaussian, relighting  
- **[Follow Your Motion: A Generic Temporal Consistency Portrait Editing Framework with Trajectory Guidance](https://arxiv.org/abs/2503.22225v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22225v1.pdf)  
  Keywords: gaussian splatting, head, face, lighting, efficient, motion, ar, avatar, dynamic, 3d gaussian, relighting  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: nerf, fast, outdoor, efficient, ar, geometry, high-fidelity, dynamic, gaussian splatting, reflection  
- **[PGC: Physics-Based Gaussian Cloth from a Single Pose](https://arxiv.org/abs/2503.20779v1)**  
  Authors: Michelle Guo, Matt Jen-Yuan Chiang, Igor Santesteban, Nikolaos Sarafianos, Hsiao-yu Chen, Oshri Halimi, Aljaž Božič, Shunsuke Saito, Jiajun Wu, C. Karen Liu, Tuur Stuyck, Egor Larionov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys-gaussian-cloth.github.io)  
  Keywords: face, lighting, body, ar, 3d gaussian, relighting  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: gaussian splatting, survey, fast, lighting, 3d reconstruction, motion, ar, dynamic, 3d gaussian  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: gaussian splatting, sparse-view, illumination, outdoor, ar, 3d gaussian  
- **[MATT-GS: Masked Attention-based 3DGS for Robot Perception and Object Detection](https://arxiv.org/abs/2503.19330v1)**  
  Authors: Jee Won Lee, Hansol Lim, SooYeun Yang, Jongseong Brad Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19330v1.pdf)  
  Keywords: gaussian splatting, lighting, recognition, ar, 3d gaussian  
- **[ReconDreamer++: Harmonizing Generative and Reconstructive Models for Driving Scene Representation](https://arxiv.org/abs/2503.18438v1)**  
  Authors: Guosheng Zhao, Xiaofeng Wang, Chaojun Ni, Zheng Zhu, Wenkang Qin, Guan Huang, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18438v1.pdf)  
  Keywords: face, lighting, ar, autonomous driving, deformation, 3d gaussian  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: global illumination, fast, illumination, light transport, face, lighting, real-time rendering, dynamic, 3d gaussian  

### SLAM

*Showing the latest 50 out of 237 papers*

- **[Visual Acoustic Fields](https://arxiv.org/abs/2503.24270v2)**  
  Authors: Yuelei Li, Hyunjin Kim, Fangneng Zhan, Ri-Zhao Qiu, Mazeyu Ji, Xiaojun Shan, Xueyan Zou, Paul Liang, Hanspeter Pfister, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24270v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuelei0428.github.io/projects/Visual-Acoustic-Fields/.)  
  Keywords: gaussian splatting, localization, human, ar, 3d gaussian  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: gaussian splatting, segmentation, semantic, robotics, localization, understanding, ar, 3d gaussian  
- **[VizFlyt: Perception-centric Pedagogical Framework For Autonomous Aerial Robots](https://arxiv.org/abs/2503.22876v1)**  
  Authors: Kushagra Srivastava, Rutwik Kulkarni, Manoj Velmurugan, Nitin J. Sanket  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22876v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pear.wpi.edu/research/vizflyt.html)  
  Keywords: gaussian splatting, robotics, localization, efficient, ar, 3d gaussian  
- **[Time-resolved dynamic CBCT reconstruction using prior-model-free spatiotemporal Gaussian representation (PMF-STGR)](https://arxiv.org/abs/2503.22139v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22139v1.pdf)  
  Keywords: fast, localization, efficient, motion, ar, deformation, dynamic, 3d gaussian  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: semantic, robotics, mapping, localization, ar, slam, high-fidelity, dynamic, 3d gaussian  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: gaussian splatting, tracking, 4d, face, 3d reconstruction, ar, deformation, 3d gaussian  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: outdoor, localization, efficient, ar, gaussian splatting  
- **[GI-SLAM: Gaussian-Inertial SLAM](https://arxiv.org/abs/2503.18275v1)**  
  Authors: Xulang Liu, Ning Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18275v1.pdf)  
  Keywords: gaussian splatting, tracking, mapping, localization, real-time rendering, ar, geometry, slam, 3d gaussian  
- **[Is there anything left? Measuring semantic residuals of objects removed from 3D Gaussian Splatting](https://arxiv.org/abs/2503.17574v1)**  
  Authors: Simona Kocour, Assia Benbihi, Aikaterini Adam, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17574v1.pdf)  
  Keywords: gaussian splatting, semantic, mapping, human, ar, 3d gaussian  
- **[Splat-LOAM: Gaussian Splatting LiDAR Odometry and Mapping](https://arxiv.org/abs/2503.17491v1)**  
  Authors: Emanuele Giacomini, Luca Di Giammarino, Lorenzo De Rebotti, Giorgio Grisetti, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17491v1.pdf)  
  Keywords: nerf, robotics, mapping, lightweight, motion, ar, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 279 papers*

- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: gaussian splatting, segmentation, semantic, robotics, localization, understanding, ar, 3d gaussian  
- **[TranSplat: Lighting-Consistent Cross-Scene Object Transfer with 3D Gaussian Splatting](https://arxiv.org/abs/2503.22676v1)**  
  Authors: Boyang, Yu, Yanlin Jin, Ashok Veeraraghavan, Akshat Dave, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22676v1.pdf)  
  Keywords: gaussian splatting, segmentation, lighting, ar, 3d gaussian, relighting  
- **[ABC-GS: Alignment-Based Controllable Style Transfer for 3D Gaussian Splatting](https://arxiv.org/abs/2503.22218v1)**  
  Authors: Wenjie Liu, Zhongliang Liu, Xiaoyan Yang, Man Sha, Yang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22218v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vpx-ecnu.github.io/ABC-GS-website.)  
  Keywords: gaussian splatting, segmentation, nerf, ar, 3d gaussian  
- **[Segment then Splat: A Unified Approach for 3D Open-Vocabulary Segmentation based on Gaussian Splatting](https://arxiv.org/abs/2503.22204v1)**  
  Authors: Yiren Lu, Yunlai Zhou, Yiran Qiao, Chaoda Song, Tuo Liang, Jing Ma, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22204v1.pdf)  
  Keywords: segmentation, robotics, motion, ar, dynamic, gaussian splatting  
- **[Semantic Consistent Language Gaussian Splatting for Point-Level Open-vocabulary Querying](https://arxiv.org/abs/2503.21767v1)**  
  Authors: Hairong Yin, Huangying Zhan, Yi Xu, Raymond A. Yeh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21767v1.pdf)  
  Keywords: gaussian splatting, segmentation, semantic, ar, 3d gaussian  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: semantic, robotics, mapping, localization, ar, slam, high-fidelity, dynamic, 3d gaussian  
- **[Feature4X: Bridging Any Monocular Video to 4D Agentic AI with Versatile Gaussian Feature Fields](https://arxiv.org/abs/2503.20776v2)**  
  Authors: Shijie Zhou, Hui Ren, Yijia Weng, Shuwang Zhang, Zhen Wang, Dejia Xu, Zhiwen Fan, Suya You, Zhangyang Wang, Leonidas Guibas, Achuta Kadambi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20776v2.pdf)  
  Keywords: segmentation, 4d, semantic, ar, dynamic, gaussian splatting  
- **[PartRM: Modeling Part-Level Dynamics with Large Cross-State Reconstruction Model](https://arxiv.org/abs/2503.19913v1)**  
  Authors: Mingju Gao, Yike Pan, Huan-ang Gao, Zongzheng Zhang, Wenyi Li, Hao Dong, Hao Tang, Li Yi, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19913v1.pdf)  
  Keywords: 4d, robotics, understanding, motion, geometry, ar, dynamic, 3d gaussian  
- **[COB-GS: Clear Object Boundaries in 3DGS Segmentation Based on Boundary-Adaptive Gaussian Splitting](https://arxiv.org/abs/2503.19443v2)**  
  Authors: Jiaxin Zhang, Junjun Jiang, Youyu Chen, Kui Jiang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19443v2.pdf) | [![GitHub](https://img.shields.io/github/stars/ZestfulJX/COB-GS?style=social)](https://github.com/ZestfulJX/COB-GS)  
  Keywords: gaussian splatting, segmentation, semantic, understanding, ar, 3d gaussian  
- **[Divide-and-Conquer: Dual-Hierarchical Optimization for Semantic 4D Gaussian Spatting](https://arxiv.org/abs/2503.19332v1)**  
  Authors: Zhiying Yan, Yiyuan Liang, Shilv Cai, Tao Zhang, Sheng Zhong, Luxin Yan, Xu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19332v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sweety-yan.github.io/DHO.)  
  Keywords: 4d, semantic, understanding, ar, dynamic, gaussian splatting  



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