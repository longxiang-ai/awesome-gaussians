# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-03-31 00:54:10

## Categories

- [3DGS Surveys](#3dgs-surveys) (26 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (440 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1556 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (525 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (589 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (107 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (509 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (87 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (590 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (256 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (35 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (169 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (233 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (275 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: survey, gaussian splatting, dynamic, fast, 3d gaussian, 3d reconstruction, lighting, ar, motion  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: real-time rendering, survey, dynamic, gaussian splatting, 3d gaussian, ar  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: survey, geometry, semantic, ar  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: real-time rendering, survey, efficient, gaussian splatting, 3d gaussian, 3d reconstruction, ar, nerf, compression  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: survey, dynamic, gaussian splatting, deformation, 4d, lighting, ar, motion, nerf  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, ray tracing, gaussian splatting, 3d gaussian, ar  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: survey, dynamic, localization, geometry, face, ar, lighting, outdoor, tracking, mapping, slam  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: survey, illumination, gaussian splatting, 3d gaussian, recognition, ar  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: survey, gaussian splatting, dynamic, compact, geometry, semantic, 3d reconstruction, high-fidelity, lighting, robotics, autonomous driving, ar, nerf  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: real-time rendering, survey, gaussian splatting, understanding, 3d gaussian, robotics, ar, nerf  

### Acceleration

*Showing the latest 50 out of 440 papers*

- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: efficient, gaussian splatting, dynamic, reflection, fast, geometry, high-fidelity, outdoor, ar, nerf  
- **[Frequency-Aware Gaussian Splatting Decomposition](https://arxiv.org/abs/2503.21226v1)**  
  Authors: Yishai Lavi, Leo Segre, Shai Avidan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21226v1.pdf)  
  Keywords: efficient, dynamic, gaussian splatting, fast, geometry, 3d gaussian, ar  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: real-time rendering, efficient, urban scene, gaussian splatting, fast, 3d gaussian, autonomous driving, ar, nerf  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: survey, gaussian splatting, dynamic, fast, 3d gaussian, 3d reconstruction, lighting, ar, motion  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: real-time rendering, efficient, gaussian splatting, fast, geometry, 3d gaussian, outdoor, ar  
- **[Hardware-Rasterized Ray-Based Gaussian Splatting](https://arxiv.org/abs/2503.18682v1)**  
  Authors: Samuel Rota Bulò, Nemanja Bartolovic, Lorenzo Porzi, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18682v1.pdf)  
  Keywords: efficient, gaussian splatting, fast, 3d gaussian, ar  
- **[GI-SLAM: Gaussian-Inertial SLAM](https://arxiv.org/abs/2503.18275v1)**  
  Authors: Xulang Liu, Ning Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18275v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, localization, geometry, 3d gaussian, tracking, ar, mapping, slam  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: real-time rendering, light transport, illumination, dynamic, fast, 3d gaussian, face, lighting, global illumination  
- **[GS-LTS: 3D Gaussian Splatting-Based Adaptive Modeling for Long-Term Service Robots](https://arxiv.org/abs/2503.17733v1)**  
  Authors: Bin Fu, Jialin Li, Bin Zhang, Ruiping Wang, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17733v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vipl-vsu.github.io/3DGS-LTS.)  
  Keywords: efficient, dynamic, gaussian splatting, compact, fast, 3d gaussian, robotics, ar  
- **[ProtoGS: Efficient and High-Quality Rendering with 3D Gaussian Prototypes](https://arxiv.org/abs/2503.17486v2)**  
  Authors: Zhengqing Gao, Dongting Hu, Jia-Wang Bian, Huan Fu, Yan Li, Tongliang Liu, Mingming Gong, Kun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17486v2.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, lightweight, efficient rendering, ar, motion  

### Applications

*Showing the latest 50 out of 1556 papers*

- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: dynamic, gaussian splatting, deformation, face, 4d, high-fidelity, ar, motion  
- **[Semantic Consistent Language Gaussian Splatting for Point-Level Open-vocabulary Querying](https://arxiv.org/abs/2503.21767v1)**  
  Authors: Hairong Yin, Huangying Zhan, Yi Xu, Raymond A. Yeh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21767v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, segmentation, semantic, ar  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: efficient, gaussian splatting, dynamic, reflection, fast, geometry, high-fidelity, outdoor, ar, nerf  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: dynamic, localization, 3d gaussian, semantic, robotics, high-fidelity, ar, mapping, slam  
- **[LandMarkSystem Technical Report](https://arxiv.org/abs/2503.21364v2)**  
  Authors: Zhenxiang Ma, Zhenyu Yang, Miao Tao, Yuanzhen Zhou, Zeyu He, Yuchang Zhang, Rong Fu, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21364v2.pdf) | [![GitHub](https://img.shields.io/github/stars/InternLandMark/LandMarkSystem?style=social)](https://github.com/InternLandMark/LandMarkSystem)  
  Keywords: efficient, dynamic, gaussian splatting, 3d gaussian, 3d reconstruction, autonomous driving, ar, nerf  
- **[Frequency-Aware Gaussian Splatting Decomposition](https://arxiv.org/abs/2503.21226v1)**  
  Authors: Yishai Lavi, Leo Segre, Shai Avidan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21226v1.pdf)  
  Keywords: efficient, dynamic, gaussian splatting, fast, geometry, 3d gaussian, ar  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: urban scene, dynamic, gaussian splatting, geometry, ar, motion  
- **[PGC: Physics-Based Gaussian Cloth from a Single Pose](https://arxiv.org/abs/2503.20779v1)**  
  Authors: Michelle Guo, Matt Jen-Yuan Chiang, Igor Santesteban, Nikolaos Sarafianos, Hsiao-yu Chen, Oshri Halimi, Aljaž Božič, Shunsuke Saito, Jiajun Wu, C. Karen Liu, Tuur Stuyck, Egor Larionov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys-gaussian-cloth.github.io)  
  Keywords: relighting, body, 3d gaussian, face, lighting, ar  
- **[Feature4X: Bridging Any Monocular Video to 4D Agentic AI with Versatile Gaussian Feature Fields](https://arxiv.org/abs/2503.20776v2)**  
  Authors: Shijie Zhou, Hui Ren, Yijia Weng, Shuwang Zhang, Zhen Wang, Dejia Xu, Zhiwen Fan, Suya You, Zhangyang Wang, Leonidas Guibas, Achuta Kadambi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20776v2.pdf)  
  Keywords: dynamic, gaussian splatting, semantic, segmentation, 4d, ar  
- **[TC-GS: Tri-plane based compression for 3D Gaussian Splatting](https://arxiv.org/abs/2503.20221v1)**  
  Authors: Taorui Wang, Zitong Yu, Yong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20221v1.pdf) | [![GitHub](https://img.shields.io/github/stars/timwang2001/TC-GS?style=social)](https://github.com/timwang2001/TC-GS)  
  Keywords: ar, 3d gaussian, gaussian splatting, compression  

### Avatar Generation

*Showing the latest 50 out of 525 papers*

- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: dynamic, gaussian splatting, deformation, face, 4d, high-fidelity, ar, motion  
- **[PGC: Physics-Based Gaussian Cloth from a Single Pose](https://arxiv.org/abs/2503.20779v1)**  
  Authors: Michelle Guo, Matt Jen-Yuan Chiang, Igor Santesteban, Nikolaos Sarafianos, Hsiao-yu Chen, Oshri Halimi, Aljaž Božič, Shunsuke Saito, Jiajun Wu, C. Karen Liu, Tuur Stuyck, Egor Larionov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys-gaussian-cloth.github.io)  
  Keywords: relighting, body, 3d gaussian, face, lighting, ar  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: gaussian splatting, 3d gaussian, deformation, face, 4d, 3d reconstruction, tracking, ar  
- **[High-Quality Spatial Reconstruction and Orthoimage Generation Using Efficient 2D Gaussian Splatting](https://arxiv.org/abs/2503.19703v1)**  
  Authors: Qian Wang, Zhihao Zhan, Jialei He, Zhituo Tu, Xiang Zhu, Jie Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19703v1.pdf)  
  Keywords: ar, efficient, gaussian splatting, face  
- **[GaussianUDF: Inferring Unsigned Distance Functions through 3D Gaussian Splatting](https://arxiv.org/abs/2503.19458v2)**  
  Authors: Shujuan Li, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19458v2.pdf)  
  Keywords: gaussian splatting, neural rendering, 3d gaussian, face, ar  
- **[ReconDreamer++: Harmonizing Generative and Reconstructive Models for Driving Scene Representation](https://arxiv.org/abs/2503.18438v1)**  
  Authors: Guosheng Zhao, Xiaofeng Wang, Chaojun Ni, Zheng Zhu, Wenkang Qin, Guan Huang, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18438v1.pdf)  
  Keywords: 3d gaussian, deformation, face, lighting, autonomous driving, ar  
- **[Unraveling the Effects of Synthetic Data on End-to-End Autonomous Driving](https://arxiv.org/abs/2503.18108v1)**  
  Authors: Junhao Ge, Zuhong Liu, Longteng Fan, Yifan Jiang, Jiaqi Su, Yiming Li, Zhejun Zhang, Siheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18108v1.pdf)  
  Keywords: efficient, dynamic, gaussian splatting, 3d gaussian, face, high-fidelity, autonomous driving, ar, nerf  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: real-time rendering, light transport, illumination, dynamic, fast, 3d gaussian, face, lighting, global illumination  
- **[Is there anything left? Measuring semantic residuals of objects removed from 3D Gaussian Splatting](https://arxiv.org/abs/2503.17574v1)**  
  Authors: Simona Kocour, Assia Benbihi, Aikaterini Adam, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17574v1.pdf)  
  Keywords: gaussian splatting, human, 3d gaussian, semantic, ar, mapping  
- **[TaoAvatar: Real-Time Lifelike Full-Body Talking Avatars for Augmented Reality via 3D Gaussian Splatting](https://arxiv.org/abs/2503.17032v1)**  
  Authors: Jianchuan Chen, Jingchuan Hu, Gaige Wang, Zhonghua Jiang, Tiansong Zhou, Zhiwen Chen, Chengfei Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17032v1.pdf)  
  Keywords: gaussian splatting, human, body, 3d gaussian, deformation, avatar, lightweight, high-fidelity, ar  

### Dynamic Scene

*Showing the latest 50 out of 589 papers*

- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: dynamic, gaussian splatting, deformation, face, 4d, high-fidelity, ar, motion  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: efficient, gaussian splatting, dynamic, reflection, fast, geometry, high-fidelity, outdoor, ar, nerf  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: dynamic, localization, 3d gaussian, semantic, robotics, high-fidelity, ar, mapping, slam  
- **[LandMarkSystem Technical Report](https://arxiv.org/abs/2503.21364v2)**  
  Authors: Zhenxiang Ma, Zhenyu Yang, Miao Tao, Yuanzhen Zhou, Zeyu He, Yuchang Zhang, Rong Fu, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21364v2.pdf) | [![GitHub](https://img.shields.io/github/stars/InternLandMark/LandMarkSystem?style=social)](https://github.com/InternLandMark/LandMarkSystem)  
  Keywords: efficient, dynamic, gaussian splatting, 3d gaussian, 3d reconstruction, autonomous driving, ar, nerf  
- **[Frequency-Aware Gaussian Splatting Decomposition](https://arxiv.org/abs/2503.21226v1)**  
  Authors: Yishai Lavi, Leo Segre, Shai Avidan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21226v1.pdf)  
  Keywords: efficient, dynamic, gaussian splatting, fast, geometry, 3d gaussian, ar  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: urban scene, dynamic, gaussian splatting, geometry, ar, motion  
- **[Feature4X: Bridging Any Monocular Video to 4D Agentic AI with Versatile Gaussian Feature Fields](https://arxiv.org/abs/2503.20776v2)**  
  Authors: Shijie Zhou, Hui Ren, Yijia Weng, Shuwang Zhang, Zhen Wang, Dejia Xu, Zhiwen Fan, Suya You, Zhangyang Wang, Leonidas Guibas, Achuta Kadambi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20776v2.pdf)  
  Keywords: dynamic, gaussian splatting, semantic, segmentation, 4d, ar  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: gaussian splatting, 3d gaussian, deformation, face, 4d, 3d reconstruction, tracking, ar  
- **[PartRM: Modeling Part-Level Dynamics with Large Cross-State Reconstruction Model](https://arxiv.org/abs/2503.19913v1)**  
  Authors: Mingju Gao, Yike Pan, Huan-ang Gao, Zongzheng Zhang, Wenyi Li, Hao Dong, Hao Tang, Li Yi, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19913v1.pdf)  
  Keywords: dynamic, understanding, geometry, 3d gaussian, 4d, robotics, ar, motion  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: survey, gaussian splatting, dynamic, fast, 3d gaussian, 3d reconstruction, lighting, ar, motion  

### Few-shot

*Showing the latest 50 out of 107 papers*

- **[CoMapGS: Covisibility Map-based Gaussian Splatting for Sparse Novel View Synthesis](https://arxiv.org/abs/2503.20998v1)**  
  Authors: Youngkyoon Jang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20998v1.pdf)  
  Keywords: few-shot, nerf, gaussian splatting, ar  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: illumination, gaussian splatting, sparse-view, 3d gaussian, outdoor, ar  
- **[NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting](https://arxiv.org/abs/2503.18794v1)**  
  Authors: Yulong Zheng, Zicheng Jiang, Shengfeng He, Yandu Sun, Junyu Dong, Huaidong Zhang, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18794v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://usmizuki.github.io/NexusGS/.)  
  Keywords: gaussian splatting, sparse-view, geometry, 3d gaussian, sparse view, ar, few-shot, nerf  
- **[SplatVoxel: History-Aware Novel View Streaming without Temporal Training](https://arxiv.org/abs/2503.14698v1)**  
  Authors: Yiming Wang, Lucy Chai, Xuan Luo, Michael Niemeyer, Manuel Lagunas, Stephen Lombardi, Siyu Tang, Tiancheng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14698v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://19reborn.github.io/SplatVoxel/)  
  Keywords: efficient, gaussian splatting, sparse-view, tracking, ar, motion  
- **[RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2503.14198v1)**  
  Authors: Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14198v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iSEE-Laboratory/RoGSplat?style=social)](https://github.com/iSEE-Laboratory/RoGSplat)  
  Keywords: gaussian splatting, human, body, geometry, 3d gaussian, sparse view, high-fidelity, ar  
- **[RI3D: Few-Shot Gaussian Splatting With Repair and Inpainting Diffusion Priors](https://arxiv.org/abs/2503.10860v1)**  
  Authors: Avinash Paliwal, Xilong Zhou, Wei Ye, Jinhui Xiong, Rakesh Ranjan, Nima Khademi Kalantari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10860v1.pdf)  
  Keywords: few-shot, gaussian splatting, ar  
- **[Physics-Aware Human-Object Rendering from Sparse Views via 3D Gaussian Splatting](https://arxiv.org/abs/2503.09640v1)**  
  Authors: Weiquan Wang, Jun Xiao, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09640v1.pdf)  
  Keywords: efficient, gaussian splatting, human, sparse-view, 3d gaussian, sparse view, ar  
- **[Multi-Modal 3D Mesh Reconstruction from Images and Text](https://arxiv.org/abs/2503.07190v1)**  
  Authors: Melvin Reka, Tessa Pulli, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07190v1.pdf)  
  Keywords: gaussian splatting, geometry, 3d reconstruction, robotics, ar, few-shot  
- **[GaussianCAD: Robust Self-Supervised CAD Reconstruction from Three Orthographic Views Using 3D Gaussian Splatting](https://arxiv.org/abs/2503.05161v1)**  
  Authors: Zheng Zhou, Zhe Li, Bo Yu, Lina Hu, Liang Dong, Zijian Yang, Xiaoli Liu, Ning Xu, Ziwei Wang, Yonghao Dang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05161v1.pdf)  
  Keywords: gaussian splatting, sparse-view, 3d gaussian, 3d reconstruction, ar  
- **[S2Gaussian: Sparse-View Super-Resolution 3D Gaussian Splatting](https://arxiv.org/abs/2503.04314v1)**  
  Authors: Yecong Wan, Mingwen Shao, Yuanshuo Cheng, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04314v1.pdf)  
  Keywords: gaussian splatting, sparse-view, geometry, 3d gaussian, sparse view, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 509 papers*

- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: efficient, gaussian splatting, dynamic, reflection, fast, geometry, high-fidelity, outdoor, ar, nerf  
- **[LandMarkSystem Technical Report](https://arxiv.org/abs/2503.21364v2)**  
  Authors: Zhenxiang Ma, Zhenyu Yang, Miao Tao, Yuanzhen Zhou, Zeyu He, Yuchang Zhang, Rong Fu, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21364v2.pdf) | [![GitHub](https://img.shields.io/github/stars/InternLandMark/LandMarkSystem?style=social)](https://github.com/InternLandMark/LandMarkSystem)  
  Keywords: efficient, dynamic, gaussian splatting, 3d gaussian, 3d reconstruction, autonomous driving, ar, nerf  
- **[Frequency-Aware Gaussian Splatting Decomposition](https://arxiv.org/abs/2503.21226v1)**  
  Authors: Yishai Lavi, Leo Segre, Shai Avidan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21226v1.pdf)  
  Keywords: efficient, dynamic, gaussian splatting, fast, geometry, 3d gaussian, ar  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: urban scene, dynamic, gaussian splatting, geometry, ar, motion  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: gaussian splatting, 3d gaussian, deformation, face, 4d, 3d reconstruction, tracking, ar  
- **[PartRM: Modeling Part-Level Dynamics with Large Cross-State Reconstruction Model](https://arxiv.org/abs/2503.19913v1)**  
  Authors: Mingju Gao, Yike Pan, Huan-ang Gao, Zongzheng Zhang, Wenyi Li, Hao Dong, Hao Tang, Li Yi, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19913v1.pdf)  
  Keywords: dynamic, understanding, geometry, 3d gaussian, 4d, robotics, ar, motion  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: survey, gaussian splatting, dynamic, fast, 3d gaussian, 3d reconstruction, lighting, ar, motion  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: real-time rendering, efficient, gaussian splatting, fast, geometry, 3d gaussian, outdoor, ar  
- **[NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting](https://arxiv.org/abs/2503.18794v1)**  
  Authors: Yulong Zheng, Zicheng Jiang, Shengfeng He, Yandu Sun, Junyu Dong, Huaidong Zhang, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18794v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://usmizuki.github.io/NexusGS/.)  
  Keywords: gaussian splatting, sparse-view, geometry, 3d gaussian, sparse view, ar, few-shot, nerf  
- **[StableGS: A Floater-Free Framework for 3D Gaussian Splatting](https://arxiv.org/abs/2503.18458v2)**  
  Authors: Luchao Wang, Qian Ren, Kaimin Liao, Hua Wang, Zhi Chen, Yaohua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18458v2.pdf)  
  Keywords: ar, geometry, 3d gaussian, gaussian splatting  

### Large Scene

*Showing the latest 50 out of 87 papers*

- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: efficient, gaussian splatting, dynamic, reflection, fast, geometry, high-fidelity, outdoor, ar, nerf  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: urban scene, dynamic, gaussian splatting, geometry, ar, motion  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: real-time rendering, efficient, urban scene, gaussian splatting, fast, 3d gaussian, autonomous driving, ar, nerf  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: illumination, gaussian splatting, sparse-view, 3d gaussian, outdoor, ar  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: efficient, gaussian splatting, localization, outdoor, ar  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: real-time rendering, efficient, gaussian splatting, fast, geometry, 3d gaussian, outdoor, ar  
- **[PanopticSplatting: End-to-End Panoptic Gaussian Splatting](https://arxiv.org/abs/2503.18073v1)**  
  Authors: Yuxuan Xie, Xuan Yu, Changjian Jiang, Sitong Mao, Shunbo Zhou, Rui Fan, Rong Xiong, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18073v1.pdf)  
  Keywords: gaussian splatting, understanding, segmentation, ar, large scene, nerf  
- **[GaussianFocus: Constrained Attention Focus for 3D Gaussian Splatting](https://arxiv.org/abs/2503.17798v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17798v1.pdf)  
  Keywords: gaussian splatting, neural rendering, 3d gaussian, 3d reconstruction, ar, large scene  
- **[OccluGaussian: Occlusion-Aware Gaussian Splatting for Large Scene Reconstruction and Rendering](https://arxiv.org/abs/2503.16177v1)**  
  Authors: Shiyong Liu, Xiao Tang, Zhihao Li, Yingfan He, Chongjie Ye, Jianzhuang Liu, Binxiao Huang, Shunbo Zhou, Xiaofei Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://occlugaussian.github.io.)  
  Keywords: gaussian splatting, fast, 3d gaussian, ar, large scene  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: efficient, geometry, 3d gaussian, deformation, high-fidelity, efficient rendering, ar, outdoor  

### Model Compression

*Showing the latest 50 out of 590 papers*

- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: efficient, gaussian splatting, dynamic, reflection, fast, geometry, high-fidelity, outdoor, ar, nerf  
- **[LandMarkSystem Technical Report](https://arxiv.org/abs/2503.21364v2)**  
  Authors: Zhenxiang Ma, Zhenyu Yang, Miao Tao, Yuanzhen Zhou, Zeyu He, Yuchang Zhang, Rong Fu, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21364v2.pdf) | [![GitHub](https://img.shields.io/github/stars/InternLandMark/LandMarkSystem?style=social)](https://github.com/InternLandMark/LandMarkSystem)  
  Keywords: efficient, dynamic, gaussian splatting, 3d gaussian, 3d reconstruction, autonomous driving, ar, nerf  
- **[Frequency-Aware Gaussian Splatting Decomposition](https://arxiv.org/abs/2503.21226v1)**  
  Authors: Yishai Lavi, Leo Segre, Shai Avidan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21226v1.pdf)  
  Keywords: efficient, dynamic, gaussian splatting, fast, geometry, 3d gaussian, ar  
- **[TC-GS: Tri-plane based compression for 3D Gaussian Splatting](https://arxiv.org/abs/2503.20221v1)**  
  Authors: Taorui Wang, Zitong Yu, Yong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20221v1.pdf) | [![GitHub](https://img.shields.io/github/stars/timwang2001/TC-GS?style=social)](https://github.com/timwang2001/TC-GS)  
  Keywords: ar, 3d gaussian, gaussian splatting, compression  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: real-time rendering, efficient, urban scene, gaussian splatting, fast, 3d gaussian, autonomous driving, ar, nerf  
- **[High-Quality Spatial Reconstruction and Orthoimage Generation Using Efficient 2D Gaussian Splatting](https://arxiv.org/abs/2503.19703v1)**  
  Authors: Qian Wang, Zhihao Zhan, Jialei He, Zhituo Tu, Xiang Zhu, Jie Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19703v1.pdf)  
  Keywords: ar, efficient, gaussian splatting, face  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: efficient, gaussian splatting, localization, outdoor, ar  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: real-time rendering, efficient, gaussian splatting, fast, geometry, 3d gaussian, outdoor, ar  
- **[Hardware-Rasterized Ray-Based Gaussian Splatting](https://arxiv.org/abs/2503.18682v1)**  
  Authors: Samuel Rota Bulò, Nemanja Bartolovic, Lorenzo Porzi, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18682v1.pdf)  
  Keywords: efficient, gaussian splatting, fast, 3d gaussian, ar  
- **[4DGC: Rate-Aware 4D Gaussian Compression for Efficient Streamable Free-Viewpoint Video](https://arxiv.org/abs/2503.18421v1)**  
  Authors: Qiang Hu, Zihan Zheng, Houqiang Zhong, Sihua Fu, Li Song, XiaoyunZhang, Guangtao Zhai, Yanfeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18421v1.pdf)  
  Keywords: efficient, dynamic, gaussian splatting, compact, 3d gaussian, 4d, ar, motion, compression  

### Quality Enhancement

*Showing the latest 50 out of 256 papers*

- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: dynamic, gaussian splatting, deformation, face, 4d, high-fidelity, ar, motion  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: efficient, gaussian splatting, dynamic, reflection, fast, geometry, high-fidelity, outdoor, ar, nerf  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: dynamic, localization, 3d gaussian, semantic, robotics, high-fidelity, ar, mapping, slam  
- **[LLGS: Unsupervised Gaussian Splatting for Image Enhancement and Reconstruction in Pure Dark Environment](https://arxiv.org/abs/2503.18640v1)**  
  Authors: Haoran Wang, Jingwei Huang, Lu Yang, Tianchen Deng, Gaojing Zhang, Mingrui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18640v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, robotics, high-fidelity, ar  
- **[Unraveling the Effects of Synthetic Data on End-to-End Autonomous Driving](https://arxiv.org/abs/2503.18108v1)**  
  Authors: Junhao Ge, Zuhong Liu, Longteng Fan, Yifan Jiang, Jiaqi Su, Yiming Li, Zhejun Zhang, Siheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18108v1.pdf)  
  Keywords: efficient, dynamic, gaussian splatting, 3d gaussian, face, high-fidelity, autonomous driving, ar, nerf  
- **[PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](https://arxiv.org/abs/2503.17973v1)**  
  Authors: Hanxiao Jiang, Hao-Yu Hsu, Kaifeng Zhang, Hsin-Ni Yu, Shenlong Wang, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17973v1.pdf)  
  Keywords: dynamic, geometry, robotics, high-fidelity, ar, motion  
- **[TaoAvatar: Real-Time Lifelike Full-Body Talking Avatars for Augmented Reality via 3D Gaussian Splatting](https://arxiv.org/abs/2503.17032v1)**  
  Authors: Jianchuan Chen, Jingchuan Hu, Gaige Wang, Zhonghua Jiang, Tiansong Zhou, Zhiwen Chen, Chengfei Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17032v1.pdf)  
  Keywords: gaussian splatting, human, body, 3d gaussian, deformation, avatar, lightweight, high-fidelity, ar  
- **[HandSplat: Embedding-Driven Gaussian Splatting for High-Fidelity Hand Rendering](https://arxiv.org/abs/2503.14736v1)**  
  Authors: Yilan Dong, Haohe Liu, Qing Wang, Jiahao Yang, Wenqing Wang, Gregory Slabaugh, Shanxin Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14736v1.pdf)  
  Keywords: efficient, dynamic, gaussian splatting, geometry, 3d gaussian, high-fidelity, ar, motion  
- **[RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2503.14198v1)**  
  Authors: Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14198v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iSEE-Laboratory/RoGSplat?style=social)](https://github.com/iSEE-Laboratory/RoGSplat)  
  Keywords: gaussian splatting, human, body, geometry, 3d gaussian, sparse view, high-fidelity, ar  
- **[Light4GS: Lightweight Compact 4D Gaussian Splatting Generation via Context Model](https://arxiv.org/abs/2503.13948v1)**  
  Authors: Mufan Liu, Qi Yang, He Huang, Wenjie Huang, Zhenlong Yuan, Zhu Li, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13948v1.pdf)  
  Keywords: efficient, dynamic, gaussian splatting, compact, 3d gaussian, 4d, high-fidelity, lightweight, ar, motion, compression  

### Ray Tracing

- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: real-time rendering, light transport, illumination, dynamic, fast, 3d gaussian, face, lighting, global illumination  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: shadow, ray tracing, gaussian splatting, fast, reflection, neural rendering, 3d gaussian, ar  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: real-time rendering, ray tracing, efficient, dynamic, relightable, geometry, face, 4d, lighting, tracking, ar  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: shadow, ray tracing, gaussian splatting, reflection, face, lighting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, ray tracing, gaussian splatting, 3d gaussian, ar  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: acceleration, light transport, ray tracing, gaussian splatting, efficient, reflection, ar  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: shadow, ray tracing, gaussian splatting, reflection, 3d gaussian, ar  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v2)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v2.pdf)  
  Keywords: ray tracing, efficient, gaussian splatting, reflection, relighting, lighting, ar  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v2)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v2.pdf) | [![GitHub](https://img.shields.io/github/stars/nv-tlabs/3dgrut?style=social)](https://github.com/nv-tlabs/3dgrut)  
  Keywords: real-time rendering, ray tracing, efficient, gaussian splatting, reflection, 3d gaussian, high-fidelity, lighting, ar  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: illumination, efficient, gaussian splatting, fast, geometry, face, ar, nerf, global illumination, mapping  

### Relighting

*Showing the latest 50 out of 169 papers*

- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: efficient, gaussian splatting, dynamic, reflection, fast, geometry, high-fidelity, outdoor, ar, nerf  
- **[PGC: Physics-Based Gaussian Cloth from a Single Pose](https://arxiv.org/abs/2503.20779v1)**  
  Authors: Michelle Guo, Matt Jen-Yuan Chiang, Igor Santesteban, Nikolaos Sarafianos, Hsiao-yu Chen, Oshri Halimi, Aljaž Božič, Shunsuke Saito, Jiajun Wu, C. Karen Liu, Tuur Stuyck, Egor Larionov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys-gaussian-cloth.github.io)  
  Keywords: relighting, body, 3d gaussian, face, lighting, ar  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: survey, gaussian splatting, dynamic, fast, 3d gaussian, 3d reconstruction, lighting, ar, motion  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: illumination, gaussian splatting, sparse-view, 3d gaussian, outdoor, ar  
- **[MATT-GS: Masked Attention-based 3DGS for Robot Perception and Object Detection](https://arxiv.org/abs/2503.19330v1)**  
  Authors: Jee Won Lee, Hansol Lim, SooYeun Yang, Jongseong Brad Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19330v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, recognition, lighting, ar  
- **[ReconDreamer++: Harmonizing Generative and Reconstructive Models for Driving Scene Representation](https://arxiv.org/abs/2503.18438v1)**  
  Authors: Guosheng Zhao, Xiaofeng Wang, Chaojun Ni, Zheng Zhu, Wenkang Qin, Guan Huang, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18438v1.pdf)  
  Keywords: 3d gaussian, deformation, face, lighting, autonomous driving, ar  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: real-time rendering, light transport, illumination, dynamic, fast, 3d gaussian, face, lighting, global illumination  
- **[AV-Surf: Surface-Enhanced Geometry-Aware Novel-View Acoustic Synthesis](https://arxiv.org/abs/2503.12806v1)**  
  Authors: Hadam Baek, Hannie Shin, Jiyoung Seo, Chanwoo Kim, Saerom Kim, Hyeongbok Kim, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12806v1.pdf)  
  Keywords: gaussian splatting, reflection, geometry, 3d gaussian, face, ar  
- **[GS-I$^{3}$: Gaussian Splatting for Surface Reconstruction from Illumination-Inconsistent Images](https://arxiv.org/abs/2503.12335v2)**  
  Authors: Tengfei Wang, Yongmao Hou, Zhaoning Zhang, Yiwei Xu, Zongqian Zhan, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12335v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TFwang-9527/GS-3I?style=social)](https://github.com/TFwang-9527/GS-3I)  
  Keywords: illumination, gaussian splatting, 3d gaussian, face, lighting, ar, mapping  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: shadow, ray tracing, gaussian splatting, fast, reflection, neural rendering, 3d gaussian, ar  

### SLAM

*Showing the latest 50 out of 233 papers*

- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: dynamic, localization, 3d gaussian, semantic, robotics, high-fidelity, ar, mapping, slam  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: gaussian splatting, 3d gaussian, deformation, face, 4d, 3d reconstruction, tracking, ar  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: efficient, gaussian splatting, localization, outdoor, ar  
- **[GI-SLAM: Gaussian-Inertial SLAM](https://arxiv.org/abs/2503.18275v1)**  
  Authors: Xulang Liu, Ning Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18275v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, localization, geometry, 3d gaussian, tracking, ar, mapping, slam  
- **[Is there anything left? Measuring semantic residuals of objects removed from 3D Gaussian Splatting](https://arxiv.org/abs/2503.17574v1)**  
  Authors: Simona Kocour, Assia Benbihi, Aikaterini Adam, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17574v1.pdf)  
  Keywords: gaussian splatting, human, 3d gaussian, semantic, ar, mapping  
- **[Splat-LOAM: Gaussian Splatting LiDAR Odometry and Mapping](https://arxiv.org/abs/2503.17491v1)**  
  Authors: Emanuele Giacomini, Luca Di Giammarino, Lorenzo De Rebotti, Giorgio Grisetti, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17491v1.pdf)  
  Keywords: gaussian splatting, lightweight, robotics, ar, motion, nerf, mapping  
- **[4D Gaussian Splatting SLAM](https://arxiv.org/abs/2503.16710v1)**  
  Authors: Yanyan Li, Youxu Fang, Zunjie Zhu, Kunyi Li, Yong Ding, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16710v1.pdf)  
  Keywords: efficient, dynamic, gaussian splatting, 4d, tracking, ar, motion, slam  
- **[SplatVoxel: History-Aware Novel View Streaming without Temporal Training](https://arxiv.org/abs/2503.14698v1)**  
  Authors: Yiming Wang, Lucy Chai, Xuan Luo, Michael Niemeyer, Manuel Lagunas, Stephen Lombardi, Siyu Tang, Tiancheng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14698v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://19reborn.github.io/SplatVoxel/)  
  Keywords: efficient, gaussian splatting, sparse-view, tracking, ar, motion  
- **[Deblur Gaussian Splatting SLAM](https://arxiv.org/abs/2503.12572v1)**  
  Authors: Francesco Girlanda, Denys Rozumnyi, Marc Pollefeys, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12572v1.pdf)  
  Keywords: gaussian splatting, deformation, high-fidelity, ar, motion, mapping, slam  
- **[GS-I$^{3}$: Gaussian Splatting for Surface Reconstruction from Illumination-Inconsistent Images](https://arxiv.org/abs/2503.12335v2)**  
  Authors: Tengfei Wang, Yongmao Hou, Zhaoning Zhang, Yiwei Xu, Zongqian Zhan, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12335v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TFwang-9527/GS-3I?style=social)](https://github.com/TFwang-9527/GS-3I)  
  Keywords: illumination, gaussian splatting, 3d gaussian, face, lighting, ar, mapping  

### Scene Understanding

*Showing the latest 50 out of 275 papers*

- **[Semantic Consistent Language Gaussian Splatting for Point-Level Open-vocabulary Querying](https://arxiv.org/abs/2503.21767v1)**  
  Authors: Hairong Yin, Huangying Zhan, Yi Xu, Raymond A. Yeh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21767v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, segmentation, semantic, ar  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: dynamic, localization, 3d gaussian, semantic, robotics, high-fidelity, ar, mapping, slam  
- **[Feature4X: Bridging Any Monocular Video to 4D Agentic AI with Versatile Gaussian Feature Fields](https://arxiv.org/abs/2503.20776v2)**  
  Authors: Shijie Zhou, Hui Ren, Yijia Weng, Shuwang Zhang, Zhen Wang, Dejia Xu, Zhiwen Fan, Suya You, Zhangyang Wang, Leonidas Guibas, Achuta Kadambi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20776v2.pdf)  
  Keywords: dynamic, gaussian splatting, semantic, segmentation, 4d, ar  
- **[PartRM: Modeling Part-Level Dynamics with Large Cross-State Reconstruction Model](https://arxiv.org/abs/2503.19913v1)**  
  Authors: Mingju Gao, Yike Pan, Huan-ang Gao, Zongzheng Zhang, Wenyi Li, Hao Dong, Hao Tang, Li Yi, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19913v1.pdf)  
  Keywords: dynamic, understanding, geometry, 3d gaussian, 4d, robotics, ar, motion  
- **[COB-GS: Clear Object Boundaries in 3DGS Segmentation Based on Boundary-Adaptive Gaussian Splitting](https://arxiv.org/abs/2503.19443v2)**  
  Authors: Jiaxin Zhang, Junjun Jiang, Youyu Chen, Kui Jiang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19443v2.pdf) | [![GitHub](https://img.shields.io/github/stars/ZestfulJX/COB-GS?style=social)](https://github.com/ZestfulJX/COB-GS)  
  Keywords: gaussian splatting, understanding, 3d gaussian, segmentation, semantic, ar  
- **[Divide-and-Conquer: Dual-Hierarchical Optimization for Semantic 4D Gaussian Spatting](https://arxiv.org/abs/2503.19332v1)**  
  Authors: Zhiying Yan, Yiyuan Liang, Shilv Cai, Tao Zhang, Sheng Zhong, Luxin Yan, Xu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19332v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sweety-yan.github.io/DHO.)  
  Keywords: dynamic, gaussian splatting, understanding, semantic, 4d, ar  
- **[MATT-GS: Masked Attention-based 3DGS for Robot Perception and Object Detection](https://arxiv.org/abs/2503.19330v1)**  
  Authors: Jee Won Lee, Hansol Lim, SooYeun Yang, Jongseong Brad Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19330v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, recognition, lighting, ar  
- **[PanoGS: Gaussian-based Panoptic Segmentation for 3D Open Vocabulary Scene Understanding](https://arxiv.org/abs/2503.18107v1)**  
  Authors: Hongjia Zhai, Hai Li, Zhenzhe Li, Xiaokun Pan, Yijia He, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18107v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/panogs}{https://zju3dv.github.io/panogs}.)  
  Keywords: gaussian splatting, understanding, geometry, 3d gaussian, segmentation, ar  
- **[PanopticSplatting: End-to-End Panoptic Gaussian Splatting](https://arxiv.org/abs/2503.18073v1)**  
  Authors: Yuxuan Xie, Xuan Yu, Changjian Jiang, Sitong Mao, Shunbo Zhou, Rui Fan, Rong Xiong, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18073v1.pdf)  
  Keywords: gaussian splatting, understanding, segmentation, ar, large scene, nerf  
- **[SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining](https://arxiv.org/abs/2503.18052v1)**  
  Authors: Yue Li, Qi Ma, Runyi Yang, Huapeng Li, Mengjiao Ma, Bin Ren, Nikola Popovic, Nicu Sebe, Ender Konukoglu, Theo Gevers, Luc Van Gool, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18052v1.pdf)  
  Keywords: gaussian splatting, understanding, 3d gaussian, semantic, ar  



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