# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-03-29 00:49:58

## Categories

- [3DGS Surveys](#3dgs-surveys) (26 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (441 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1556 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (525 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (590 papers) - Papers about dynamic scene reconstruction and rendering
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
  Keywords: lighting, fast, 3d reconstruction, survey, 3d gaussian, dynamic, ar, gaussian splatting, motion  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: ar, survey, dynamic, 3d gaussian, real-time rendering, gaussian splatting  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: ar, survey, geometry, semantic  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: ar, nerf, 3d reconstruction, compression, efficient, 3d gaussian, survey, real-time rendering, gaussian splatting  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: lighting, nerf, deformation, survey, dynamic, ar, gaussian splatting, 4d, motion  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, ray tracing, 3d gaussian, ar, gaussian splatting  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: tracking, lighting, face, mapping, survey, dynamic, geometry, slam, ar, localization, outdoor  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: illumination, recognition, survey, 3d gaussian, ar, gaussian splatting  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: lighting, high-fidelity, nerf, semantic, 3d reconstruction, compact, autonomous driving, survey, dynamic, geometry, ar, robotics, gaussian splatting  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: ar, understanding, nerf, survey, 3d gaussian, real-time rendering, robotics, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 441 papers*

- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: high-fidelity, fast, nerf, efficient, dynamic, geometry, ar, gaussian splatting, reflection, outdoor  
- **[Frequency-Aware Gaussian Splatting Decomposition](https://arxiv.org/abs/2503.21226v1)**  
  Authors: Yishai Lavi, Leo Segre, Shai Avidan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21226v1.pdf)  
  Keywords: fast, efficient, 3d gaussian, dynamic, geometry, ar, gaussian splatting  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: ar, fast, nerf, urban scene, efficient, autonomous driving, 3d gaussian, real-time rendering, gaussian splatting  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: lighting, fast, 3d reconstruction, survey, 3d gaussian, dynamic, ar, gaussian splatting, motion  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: ar, fast, efficient, 3d gaussian, geometry, real-time rendering, gaussian splatting, outdoor  
- **[Hardware-Rasterized Ray-Based Gaussian Splatting](https://arxiv.org/abs/2503.18682v1)**  
  Authors: Samuel Rota Bulò, Nemanja Bartolovic, Lorenzo Porzi, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18682v1.pdf)  
  Keywords: fast, efficient, 3d gaussian, ar, gaussian splatting  
- **[GI-SLAM: Gaussian-Inertial SLAM](https://arxiv.org/abs/2503.18275v1)**  
  Authors: Xulang Liu, Ning Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18275v1.pdf)  
  Keywords: ar, tracking, mapping, 3d gaussian, geometry, slam, real-time rendering, gaussian splatting, localization  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: lighting, fast, global illumination, illumination, light transport, face, 3d gaussian, dynamic, real-time rendering  
- **[GS-LTS: 3D Gaussian Splatting-Based Adaptive Modeling for Long-Term Service Robots](https://arxiv.org/abs/2503.17733v1)**  
  Authors: Bin Fu, Jialin Li, Bin Zhang, Ruiping Wang, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17733v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vipl-vsu.github.io/3DGS-LTS.)  
  Keywords: fast, compact, efficient, 3d gaussian, dynamic, ar, robotics, gaussian splatting  
- **[ProtoGS: Efficient and High-Quality Rendering with 3D Gaussian Prototypes](https://arxiv.org/abs/2503.17486v2)**  
  Authors: Zhengqing Gao, Dongting Hu, Jia-Wang Bian, Huan Fu, Yan Li, Tongliang Liu, Mingming Gong, Kun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17486v2.pdf)  
  Keywords: efficient rendering, lightweight, efficient, 3d gaussian, ar, gaussian splatting, motion  

### Applications

*Showing the latest 50 out of 1556 papers*

- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: high-fidelity, face, deformation, dynamic, ar, gaussian splatting, 4d, motion  
- **[Semantic Consistent Language Gaussian Splatting for Point-Level Open-vocabulary Querying](https://arxiv.org/abs/2503.21767v1)**  
  Authors: Hairong Yin, Huangying Zhan, Yi Xu, Raymond A. Yeh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21767v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, gaussian splatting, segmentation  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: high-fidelity, fast, nerf, efficient, dynamic, geometry, ar, gaussian splatting, reflection, outdoor  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: high-fidelity, semantic, mapping, 3d gaussian, dynamic, slam, ar, robotics, localization  
- **[LandMarkSystem Technical Report](https://arxiv.org/abs/2503.21364v1)**  
  Authors: Zhenxiang Ma, Zhenyu Yang, Miao Tao, Yuanzhen Zhou, Zeyu He, Yuchang Zhang, Rong Fu, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21364v1.pdf) | [![GitHub](https://img.shields.io/github/stars/InternLandMark/LandMarkSystem?style=social)](https://github.com/InternLandMark/LandMarkSystem)  
  Keywords: nerf, 3d reconstruction, efficient, autonomous driving, 3d gaussian, dynamic, ar, gaussian splatting  
- **[Frequency-Aware Gaussian Splatting Decomposition](https://arxiv.org/abs/2503.21226v1)**  
  Authors: Yishai Lavi, Leo Segre, Shai Avidan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21226v1.pdf)  
  Keywords: fast, efficient, 3d gaussian, dynamic, geometry, ar, gaussian splatting  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: urban scene, dynamic, geometry, ar, gaussian splatting, motion  
- **[PGC: Physics-Based Gaussian Cloth from a Single Pose](https://arxiv.org/abs/2503.20779v1)**  
  Authors: Michelle Guo, Matt Jen-Yuan Chiang, Igor Santesteban, Nikolaos Sarafianos, Hsiao-yu Chen, Oshri Halimi, Aljaž Božič, Shunsuke Saito, Jiajun Wu, C. Karen Liu, Tuur Stuyck, Egor Larionov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys-gaussian-cloth.github.io)  
  Keywords: lighting, face, body, relighting, 3d gaussian, ar  
- **[Feature4X: Bridging Any Monocular Video to 4D Agentic AI with Versatile Gaussian Feature Fields](https://arxiv.org/abs/2503.20776v1)**  
  Authors: Shijie Zhou, Hui Ren, Yijia Weng, Shuwang Zhang, Zhen Wang, Dejia Xu, Zhiwen Fan, Suya You, Zhangyang Wang, Leonidas Guibas, Achuta Kadambi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20776v1.pdf)  
  Keywords: semantic, dynamic, 4d, ar, gaussian splatting, segmentation  
- **[TC-GS: Tri-plane based compression for 3D Gaussian Splatting](https://arxiv.org/abs/2503.20221v1)**  
  Authors: Taorui Wang, Zitong Yu, Yong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20221v1.pdf) | [![GitHub](https://img.shields.io/github/stars/timwang2001/TC-GS?style=social)](https://github.com/timwang2001/TC-GS)  
  Keywords: gaussian splatting, compression, 3d gaussian, ar  

### Avatar Generation

*Showing the latest 50 out of 525 papers*

- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: high-fidelity, face, deformation, dynamic, ar, gaussian splatting, 4d, motion  
- **[PGC: Physics-Based Gaussian Cloth from a Single Pose](https://arxiv.org/abs/2503.20779v1)**  
  Authors: Michelle Guo, Matt Jen-Yuan Chiang, Igor Santesteban, Nikolaos Sarafianos, Hsiao-yu Chen, Oshri Halimi, Aljaž Božič, Shunsuke Saito, Jiajun Wu, C. Karen Liu, Tuur Stuyck, Egor Larionov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys-gaussian-cloth.github.io)  
  Keywords: lighting, face, body, relighting, 3d gaussian, ar  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: tracking, 3d reconstruction, face, deformation, 3d gaussian, ar, gaussian splatting, 4d  
- **[High-Quality Spatial Reconstruction and Orthoimage Generation Using Efficient 2D Gaussian Splatting](https://arxiv.org/abs/2503.19703v1)**  
  Authors: Qian Wang, Zhihao Zhan, Jialei He, Zhituo Tu, Xiang Zhu, Jie Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19703v1.pdf)  
  Keywords: ar, gaussian splatting, face, efficient  
- **[GaussianUDF: Inferring Unsigned Distance Functions through 3D Gaussian Splatting](https://arxiv.org/abs/2503.19458v1)**  
  Authors: Shujuan Li, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19458v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lisj575.github.io/GaussianUDF/)  
  Keywords: neural rendering, face, 3d gaussian, ar, gaussian splatting  
- **[ReconDreamer++: Harmonizing Generative and Reconstructive Models for Driving Scene Representation](https://arxiv.org/abs/2503.18438v1)**  
  Authors: Guosheng Zhao, Xiaofeng Wang, Chaojun Ni, Zheng Zhu, Wenkang Qin, Guan Huang, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18438v1.pdf)  
  Keywords: lighting, face, deformation, autonomous driving, 3d gaussian, ar  
- **[Unraveling the Effects of Synthetic Data on End-to-End Autonomous Driving](https://arxiv.org/abs/2503.18108v1)**  
  Authors: Junhao Ge, Zuhong Liu, Longteng Fan, Yifan Jiang, Jiaqi Su, Yiming Li, Zhejun Zhang, Siheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18108v1.pdf)  
  Keywords: high-fidelity, nerf, face, efficient, autonomous driving, 3d gaussian, dynamic, ar, gaussian splatting  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: lighting, fast, global illumination, illumination, light transport, face, 3d gaussian, dynamic, real-time rendering  
- **[Is there anything left? Measuring semantic residuals of objects removed from 3D Gaussian Splatting](https://arxiv.org/abs/2503.17574v1)**  
  Authors: Simona Kocour, Assia Benbihi, Aikaterini Adam, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17574v1.pdf)  
  Keywords: human, semantic, mapping, 3d gaussian, ar, gaussian splatting  
- **[TaoAvatar: Real-Time Lifelike Full-Body Talking Avatars for Augmented Reality via 3D Gaussian Splatting](https://arxiv.org/abs/2503.17032v1)**  
  Authors: Jianchuan Chen, Jingchuan Hu, Gaige Wang, Zhonghua Jiang, Tiansong Zhou, Zhiwen Chen, Chengfei Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17032v1.pdf)  
  Keywords: human, high-fidelity, lightweight, deformation, body, 3d gaussian, ar, gaussian splatting, avatar  

### Dynamic Scene

*Showing the latest 50 out of 590 papers*

- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: high-fidelity, face, deformation, dynamic, ar, gaussian splatting, 4d, motion  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: high-fidelity, fast, nerf, efficient, dynamic, geometry, ar, gaussian splatting, reflection, outdoor  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: high-fidelity, semantic, mapping, 3d gaussian, dynamic, slam, ar, robotics, localization  
- **[LandMarkSystem Technical Report](https://arxiv.org/abs/2503.21364v1)**  
  Authors: Zhenxiang Ma, Zhenyu Yang, Miao Tao, Yuanzhen Zhou, Zeyu He, Yuchang Zhang, Rong Fu, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21364v1.pdf) | [![GitHub](https://img.shields.io/github/stars/InternLandMark/LandMarkSystem?style=social)](https://github.com/InternLandMark/LandMarkSystem)  
  Keywords: nerf, 3d reconstruction, efficient, autonomous driving, 3d gaussian, dynamic, ar, gaussian splatting  
- **[Frequency-Aware Gaussian Splatting Decomposition](https://arxiv.org/abs/2503.21226v1)**  
  Authors: Yishai Lavi, Leo Segre, Shai Avidan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21226v1.pdf)  
  Keywords: fast, efficient, 3d gaussian, dynamic, geometry, ar, gaussian splatting  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: urban scene, dynamic, geometry, ar, gaussian splatting, motion  
- **[Feature4X: Bridging Any Monocular Video to 4D Agentic AI with Versatile Gaussian Feature Fields](https://arxiv.org/abs/2503.20776v1)**  
  Authors: Shijie Zhou, Hui Ren, Yijia Weng, Shuwang Zhang, Zhen Wang, Dejia Xu, Zhiwen Fan, Suya You, Zhangyang Wang, Leonidas Guibas, Achuta Kadambi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20776v1.pdf)  
  Keywords: semantic, dynamic, 4d, ar, gaussian splatting, segmentation  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: tracking, 3d reconstruction, face, deformation, 3d gaussian, ar, gaussian splatting, 4d  
- **[PartRM: Modeling Part-Level Dynamics with Large Cross-State Reconstruction Model](https://arxiv.org/abs/2503.19913v1)**  
  Authors: Mingju Gao, Yike Pan, Huan-ang Gao, Zongzheng Zhang, Wenyi Li, Hao Dong, Hao Tang, Li Yi, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19913v1.pdf)  
  Keywords: understanding, 3d gaussian, dynamic, geometry, ar, robotics, 4d, motion  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: lighting, fast, 3d reconstruction, survey, 3d gaussian, dynamic, ar, gaussian splatting, motion  

### Few-shot

*Showing the latest 50 out of 107 papers*

- **[CoMapGS: Covisibility Map-based Gaussian Splatting for Sparse Novel View Synthesis](https://arxiv.org/abs/2503.20998v1)**  
  Authors: Youngkyoon Jang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20998v1.pdf)  
  Keywords: ar, few-shot, gaussian splatting, nerf  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: illumination, sparse-view, 3d gaussian, ar, gaussian splatting, outdoor  
- **[NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting](https://arxiv.org/abs/2503.18794v1)**  
  Authors: Yulong Zheng, Zicheng Jiang, Shengfeng He, Yandu Sun, Junyu Dong, Huaidong Zhang, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18794v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://usmizuki.github.io/NexusGS/.)  
  Keywords: nerf, few-shot, sparse-view, sparse view, 3d gaussian, geometry, ar, gaussian splatting  
- **[SplatVoxel: History-Aware Novel View Streaming without Temporal Training](https://arxiv.org/abs/2503.14698v1)**  
  Authors: Yiming Wang, Lucy Chai, Xuan Luo, Michael Niemeyer, Manuel Lagunas, Stephen Lombardi, Siyu Tang, Tiancheng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14698v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://19reborn.github.io/SplatVoxel/)  
  Keywords: tracking, sparse-view, efficient, ar, gaussian splatting, motion  
- **[RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2503.14198v1)**  
  Authors: Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14198v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iSEE-Laboratory/RoGSplat?style=social)](https://github.com/iSEE-Laboratory/RoGSplat)  
  Keywords: human, high-fidelity, sparse view, body, 3d gaussian, geometry, ar, gaussian splatting  
- **[RI3D: Few-Shot Gaussian Splatting With Repair and Inpainting Diffusion Priors](https://arxiv.org/abs/2503.10860v1)**  
  Authors: Avinash Paliwal, Xilong Zhou, Wei Ye, Jinhui Xiong, Rakesh Ranjan, Nima Khademi Kalantari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10860v1.pdf)  
  Keywords: few-shot, gaussian splatting, ar  
- **[Physics-Aware Human-Object Rendering from Sparse Views via 3D Gaussian Splatting](https://arxiv.org/abs/2503.09640v1)**  
  Authors: Weiquan Wang, Jun Xiao, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09640v1.pdf)  
  Keywords: human, sparse-view, efficient, sparse view, 3d gaussian, ar, gaussian splatting  
- **[Multi-Modal 3D Mesh Reconstruction from Images and Text](https://arxiv.org/abs/2503.07190v1)**  
  Authors: Melvin Reka, Tessa Pulli, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07190v1.pdf)  
  Keywords: few-shot, 3d reconstruction, geometry, ar, robotics, gaussian splatting  
- **[GaussianCAD: Robust Self-Supervised CAD Reconstruction from Three Orthographic Views Using 3D Gaussian Splatting](https://arxiv.org/abs/2503.05161v1)**  
  Authors: Zheng Zhou, Zhe Li, Bo Yu, Lina Hu, Liang Dong, Zijian Yang, Xiaoli Liu, Ning Xu, Ziwei Wang, Yonghao Dang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05161v1.pdf)  
  Keywords: 3d reconstruction, sparse-view, 3d gaussian, ar, gaussian splatting  
- **[S2Gaussian: Sparse-View Super-Resolution 3D Gaussian Splatting](https://arxiv.org/abs/2503.04314v1)**  
  Authors: Yecong Wan, Mingwen Shao, Yuanshuo Cheng, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04314v1.pdf)  
  Keywords: sparse-view, sparse view, 3d gaussian, geometry, ar, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 509 papers*

- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: high-fidelity, fast, nerf, efficient, dynamic, geometry, ar, gaussian splatting, reflection, outdoor  
- **[LandMarkSystem Technical Report](https://arxiv.org/abs/2503.21364v1)**  
  Authors: Zhenxiang Ma, Zhenyu Yang, Miao Tao, Yuanzhen Zhou, Zeyu He, Yuchang Zhang, Rong Fu, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21364v1.pdf) | [![GitHub](https://img.shields.io/github/stars/InternLandMark/LandMarkSystem?style=social)](https://github.com/InternLandMark/LandMarkSystem)  
  Keywords: nerf, 3d reconstruction, efficient, autonomous driving, 3d gaussian, dynamic, ar, gaussian splatting  
- **[Frequency-Aware Gaussian Splatting Decomposition](https://arxiv.org/abs/2503.21226v1)**  
  Authors: Yishai Lavi, Leo Segre, Shai Avidan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21226v1.pdf)  
  Keywords: fast, efficient, 3d gaussian, dynamic, geometry, ar, gaussian splatting  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: urban scene, dynamic, geometry, ar, gaussian splatting, motion  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: tracking, 3d reconstruction, face, deformation, 3d gaussian, ar, gaussian splatting, 4d  
- **[PartRM: Modeling Part-Level Dynamics with Large Cross-State Reconstruction Model](https://arxiv.org/abs/2503.19913v1)**  
  Authors: Mingju Gao, Yike Pan, Huan-ang Gao, Zongzheng Zhang, Wenyi Li, Hao Dong, Hao Tang, Li Yi, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19913v1.pdf)  
  Keywords: understanding, 3d gaussian, dynamic, geometry, ar, robotics, 4d, motion  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: lighting, fast, 3d reconstruction, survey, 3d gaussian, dynamic, ar, gaussian splatting, motion  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: ar, fast, efficient, 3d gaussian, geometry, real-time rendering, gaussian splatting, outdoor  
- **[NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting](https://arxiv.org/abs/2503.18794v1)**  
  Authors: Yulong Zheng, Zicheng Jiang, Shengfeng He, Yandu Sun, Junyu Dong, Huaidong Zhang, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18794v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://usmizuki.github.io/NexusGS/.)  
  Keywords: nerf, few-shot, sparse-view, sparse view, 3d gaussian, geometry, ar, gaussian splatting  
- **[StableGS: A Floater-Free Framework for 3D Gaussian Splatting](https://arxiv.org/abs/2503.18458v2)**  
  Authors: Luchao Wang, Qian Ren, Kaimin Liao, Hua Wang, Zhi Chen, Yaohua Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18458v2.pdf)  
  Keywords: gaussian splatting, geometry, 3d gaussian, ar  

### Large Scene

*Showing the latest 50 out of 87 papers*

- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: high-fidelity, fast, nerf, efficient, dynamic, geometry, ar, gaussian splatting, reflection, outdoor  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: urban scene, dynamic, geometry, ar, gaussian splatting, motion  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: ar, fast, nerf, urban scene, efficient, autonomous driving, 3d gaussian, real-time rendering, gaussian splatting  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: illumination, sparse-view, 3d gaussian, ar, gaussian splatting, outdoor  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, localization, outdoor  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: ar, fast, efficient, 3d gaussian, geometry, real-time rendering, gaussian splatting, outdoor  
- **[PanopticSplatting: End-to-End Panoptic Gaussian Splatting](https://arxiv.org/abs/2503.18073v1)**  
  Authors: Yuxuan Xie, Xuan Yu, Changjian Jiang, Sitong Mao, Shunbo Zhou, Rui Fan, Rong Xiong, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18073v1.pdf)  
  Keywords: understanding, nerf, large scene, ar, gaussian splatting, segmentation  
- **[GaussianFocus: Constrained Attention Focus for 3D Gaussian Splatting](https://arxiv.org/abs/2503.17798v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17798v1.pdf)  
  Keywords: neural rendering, 3d reconstruction, large scene, 3d gaussian, ar, gaussian splatting  
- **[OccluGaussian: Occlusion-Aware Gaussian Splatting for Large Scene Reconstruction and Rendering](https://arxiv.org/abs/2503.16177v1)**  
  Authors: Shiyong Liu, Xiao Tang, Zhihao Li, Yingfan He, Chongjie Ye, Jianzhuang Liu, Binxiao Huang, Shunbo Zhou, Xiaofei Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://occlugaussian.github.io.)  
  Keywords: fast, large scene, 3d gaussian, ar, gaussian splatting  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: efficient rendering, high-fidelity, deformation, efficient, 3d gaussian, geometry, ar, outdoor  

### Model Compression

*Showing the latest 50 out of 590 papers*

- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: high-fidelity, fast, nerf, efficient, dynamic, geometry, ar, gaussian splatting, reflection, outdoor  
- **[LandMarkSystem Technical Report](https://arxiv.org/abs/2503.21364v1)**  
  Authors: Zhenxiang Ma, Zhenyu Yang, Miao Tao, Yuanzhen Zhou, Zeyu He, Yuchang Zhang, Rong Fu, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21364v1.pdf) | [![GitHub](https://img.shields.io/github/stars/InternLandMark/LandMarkSystem?style=social)](https://github.com/InternLandMark/LandMarkSystem)  
  Keywords: nerf, 3d reconstruction, efficient, autonomous driving, 3d gaussian, dynamic, ar, gaussian splatting  
- **[Frequency-Aware Gaussian Splatting Decomposition](https://arxiv.org/abs/2503.21226v1)**  
  Authors: Yishai Lavi, Leo Segre, Shai Avidan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21226v1.pdf)  
  Keywords: fast, efficient, 3d gaussian, dynamic, geometry, ar, gaussian splatting  
- **[TC-GS: Tri-plane based compression for 3D Gaussian Splatting](https://arxiv.org/abs/2503.20221v1)**  
  Authors: Taorui Wang, Zitong Yu, Yong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20221v1.pdf) | [![GitHub](https://img.shields.io/github/stars/timwang2001/TC-GS?style=social)](https://github.com/timwang2001/TC-GS)  
  Keywords: gaussian splatting, compression, 3d gaussian, ar  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: ar, fast, nerf, urban scene, efficient, autonomous driving, 3d gaussian, real-time rendering, gaussian splatting  
- **[High-Quality Spatial Reconstruction and Orthoimage Generation Using Efficient 2D Gaussian Splatting](https://arxiv.org/abs/2503.19703v1)**  
  Authors: Qian Wang, Zhihao Zhan, Jialei He, Zhituo Tu, Xiang Zhu, Jie Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19703v1.pdf)  
  Keywords: ar, gaussian splatting, face, efficient  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, localization, outdoor  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: ar, fast, efficient, 3d gaussian, geometry, real-time rendering, gaussian splatting, outdoor  
- **[Hardware-Rasterized Ray-Based Gaussian Splatting](https://arxiv.org/abs/2503.18682v1)**  
  Authors: Samuel Rota Bulò, Nemanja Bartolovic, Lorenzo Porzi, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18682v1.pdf)  
  Keywords: fast, efficient, 3d gaussian, ar, gaussian splatting  
- **[4DGC: Rate-Aware 4D Gaussian Compression for Efficient Streamable Free-Viewpoint Video](https://arxiv.org/abs/2503.18421v1)**  
  Authors: Qiang Hu, Zihan Zheng, Houqiang Zhong, Sihua Fu, Li Song, XiaoyunZhang, Guangtao Zhai, Yanfeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18421v1.pdf)  
  Keywords: compression, compact, efficient, 3d gaussian, dynamic, ar, gaussian splatting, 4d, motion  

### Quality Enhancement

*Showing the latest 50 out of 256 papers*

- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: high-fidelity, face, deformation, dynamic, ar, gaussian splatting, 4d, motion  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: high-fidelity, fast, nerf, efficient, dynamic, geometry, ar, gaussian splatting, reflection, outdoor  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: high-fidelity, semantic, mapping, 3d gaussian, dynamic, slam, ar, robotics, localization  
- **[LLGS: Unsupervised Gaussian Splatting for Image Enhancement and Reconstruction in Pure Dark Environment](https://arxiv.org/abs/2503.18640v1)**  
  Authors: Haoran Wang, Jingwei Huang, Lu Yang, Tianchen Deng, Gaojing Zhang, Mingrui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18640v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, ar, robotics, gaussian splatting  
- **[Unraveling the Effects of Synthetic Data on End-to-End Autonomous Driving](https://arxiv.org/abs/2503.18108v1)**  
  Authors: Junhao Ge, Zuhong Liu, Longteng Fan, Yifan Jiang, Jiaqi Su, Yiming Li, Zhejun Zhang, Siheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18108v1.pdf)  
  Keywords: high-fidelity, nerf, face, efficient, autonomous driving, 3d gaussian, dynamic, ar, gaussian splatting  
- **[PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](https://arxiv.org/abs/2503.17973v1)**  
  Authors: Hanxiao Jiang, Hao-Yu Hsu, Kaifeng Zhang, Hsin-Ni Yu, Shenlong Wang, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17973v1.pdf)  
  Keywords: high-fidelity, dynamic, geometry, ar, robotics, motion  
- **[TaoAvatar: Real-Time Lifelike Full-Body Talking Avatars for Augmented Reality via 3D Gaussian Splatting](https://arxiv.org/abs/2503.17032v1)**  
  Authors: Jianchuan Chen, Jingchuan Hu, Gaige Wang, Zhonghua Jiang, Tiansong Zhou, Zhiwen Chen, Chengfei Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17032v1.pdf)  
  Keywords: human, high-fidelity, lightweight, deformation, body, 3d gaussian, ar, gaussian splatting, avatar  
- **[HandSplat: Embedding-Driven Gaussian Splatting for High-Fidelity Hand Rendering](https://arxiv.org/abs/2503.14736v1)**  
  Authors: Yilan Dong, Haohe Liu, Qing Wang, Jiahao Yang, Wenqing Wang, Gregory Slabaugh, Shanxin Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14736v1.pdf)  
  Keywords: high-fidelity, efficient, 3d gaussian, dynamic, geometry, ar, gaussian splatting, motion  
- **[RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2503.14198v1)**  
  Authors: Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14198v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iSEE-Laboratory/RoGSplat?style=social)](https://github.com/iSEE-Laboratory/RoGSplat)  
  Keywords: human, high-fidelity, sparse view, body, 3d gaussian, geometry, ar, gaussian splatting  
- **[Light4GS: Lightweight Compact 4D Gaussian Splatting Generation via Context Model](https://arxiv.org/abs/2503.13948v1)**  
  Authors: Mufan Liu, Qi Yang, He Huang, Wenjie Huang, Zhenlong Yuan, Zhu Li, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13948v1.pdf)  
  Keywords: high-fidelity, compression, lightweight, compact, efficient, 3d gaussian, dynamic, ar, gaussian splatting, 4d, motion  

### Ray Tracing

- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: lighting, fast, global illumination, illumination, light transport, face, 3d gaussian, dynamic, real-time rendering  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: neural rendering, fast, shadow, 3d gaussian, ray tracing, ar, gaussian splatting, reflection  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: ar, tracking, lighting, relightable, face, efficient, ray tracing, dynamic, geometry, real-time rendering, 4d  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: lighting, shadow, face, ray tracing, gaussian splatting, reflection  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, ray tracing, 3d gaussian, ar, gaussian splatting  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: light transport, efficient, ray tracing, acceleration, ar, gaussian splatting, reflection  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: shadow, 3d gaussian, ray tracing, ar, gaussian splatting, reflection  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v2)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v2.pdf)  
  Keywords: lighting, efficient, relighting, ray tracing, ar, gaussian splatting, reflection  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v2)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v2.pdf) | [![GitHub](https://img.shields.io/github/stars/nv-tlabs/3dgrut?style=social)](https://github.com/nv-tlabs/3dgrut)  
  Keywords: ar, lighting, high-fidelity, efficient, 3d gaussian, ray tracing, real-time rendering, gaussian splatting, reflection  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: fast, global illumination, nerf, illumination, face, efficient, mapping, geometry, ar, gaussian splatting  

### Relighting

*Showing the latest 50 out of 169 papers*

- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v1)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: high-fidelity, fast, nerf, efficient, dynamic, geometry, ar, gaussian splatting, reflection, outdoor  
- **[PGC: Physics-Based Gaussian Cloth from a Single Pose](https://arxiv.org/abs/2503.20779v1)**  
  Authors: Michelle Guo, Matt Jen-Yuan Chiang, Igor Santesteban, Nikolaos Sarafianos, Hsiao-yu Chen, Oshri Halimi, Aljaž Božič, Shunsuke Saito, Jiajun Wu, C. Karen Liu, Tuur Stuyck, Egor Larionov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys-gaussian-cloth.github.io)  
  Keywords: lighting, face, body, relighting, 3d gaussian, ar  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: lighting, fast, 3d reconstruction, survey, 3d gaussian, dynamic, ar, gaussian splatting, motion  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: illumination, sparse-view, 3d gaussian, ar, gaussian splatting, outdoor  
- **[MATT-GS: Masked Attention-based 3DGS for Robot Perception and Object Detection](https://arxiv.org/abs/2503.19330v1)**  
  Authors: Jee Won Lee, Hansol Lim, SooYeun Yang, Jongseong Brad Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19330v1.pdf)  
  Keywords: lighting, recognition, 3d gaussian, ar, gaussian splatting  
- **[ReconDreamer++: Harmonizing Generative and Reconstructive Models for Driving Scene Representation](https://arxiv.org/abs/2503.18438v1)**  
  Authors: Guosheng Zhao, Xiaofeng Wang, Chaojun Ni, Zheng Zhu, Wenkang Qin, Guan Huang, Xingang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18438v1.pdf)  
  Keywords: lighting, face, deformation, autonomous driving, 3d gaussian, ar  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: lighting, fast, global illumination, illumination, light transport, face, 3d gaussian, dynamic, real-time rendering  
- **[AV-Surf: Surface-Enhanced Geometry-Aware Novel-View Acoustic Synthesis](https://arxiv.org/abs/2503.12806v1)**  
  Authors: Hadam Baek, Hannie Shin, Jiyoung Seo, Chanwoo Kim, Saerom Kim, Hyeongbok Kim, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12806v1.pdf)  
  Keywords: face, 3d gaussian, geometry, ar, gaussian splatting, reflection  
- **[GS-I$^{3}$: Gaussian Splatting for Surface Reconstruction from Illumination-Inconsistent Images](https://arxiv.org/abs/2503.12335v2)**  
  Authors: Tengfei Wang, Yongmao Hou, Zhaoning Zhang, Yiwei Xu, Zongqian Zhan, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12335v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TFwang-9527/GS-3I?style=social)](https://github.com/TFwang-9527/GS-3I)  
  Keywords: lighting, illumination, face, mapping, 3d gaussian, ar, gaussian splatting  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: neural rendering, fast, shadow, 3d gaussian, ray tracing, ar, gaussian splatting, reflection  

### SLAM

*Showing the latest 50 out of 233 papers*

- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: high-fidelity, semantic, mapping, 3d gaussian, dynamic, slam, ar, robotics, localization  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: tracking, 3d reconstruction, face, deformation, 3d gaussian, ar, gaussian splatting, 4d  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: efficient, ar, gaussian splatting, localization, outdoor  
- **[GI-SLAM: Gaussian-Inertial SLAM](https://arxiv.org/abs/2503.18275v1)**  
  Authors: Xulang Liu, Ning Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18275v1.pdf)  
  Keywords: ar, tracking, mapping, 3d gaussian, geometry, slam, real-time rendering, gaussian splatting, localization  
- **[Is there anything left? Measuring semantic residuals of objects removed from 3D Gaussian Splatting](https://arxiv.org/abs/2503.17574v1)**  
  Authors: Simona Kocour, Assia Benbihi, Aikaterini Adam, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17574v1.pdf)  
  Keywords: human, semantic, mapping, 3d gaussian, ar, gaussian splatting  
- **[Splat-LOAM: Gaussian Splatting LiDAR Odometry and Mapping](https://arxiv.org/abs/2503.17491v1)**  
  Authors: Emanuele Giacomini, Luca Di Giammarino, Lorenzo De Rebotti, Giorgio Grisetti, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17491v1.pdf)  
  Keywords: nerf, lightweight, mapping, ar, robotics, gaussian splatting, motion  
- **[4D Gaussian Splatting SLAM](https://arxiv.org/abs/2503.16710v1)**  
  Authors: Yanyan Li, Youxu Fang, Zunjie Zhu, Kunyi Li, Yong Ding, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16710v1.pdf)  
  Keywords: tracking, efficient, dynamic, slam, ar, gaussian splatting, 4d, motion  
- **[SplatVoxel: History-Aware Novel View Streaming without Temporal Training](https://arxiv.org/abs/2503.14698v1)**  
  Authors: Yiming Wang, Lucy Chai, Xuan Luo, Michael Niemeyer, Manuel Lagunas, Stephen Lombardi, Siyu Tang, Tiancheng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14698v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://19reborn.github.io/SplatVoxel/)  
  Keywords: tracking, sparse-view, efficient, ar, gaussian splatting, motion  
- **[Deblur Gaussian Splatting SLAM](https://arxiv.org/abs/2503.12572v1)**  
  Authors: Francesco Girlanda, Denys Rozumnyi, Marc Pollefeys, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12572v1.pdf)  
  Keywords: high-fidelity, deformation, mapping, slam, ar, gaussian splatting, motion  
- **[GS-I$^{3}$: Gaussian Splatting for Surface Reconstruction from Illumination-Inconsistent Images](https://arxiv.org/abs/2503.12335v2)**  
  Authors: Tengfei Wang, Yongmao Hou, Zhaoning Zhang, Yiwei Xu, Zongqian Zhan, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12335v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TFwang-9527/GS-3I?style=social)](https://github.com/TFwang-9527/GS-3I)  
  Keywords: lighting, illumination, face, mapping, 3d gaussian, ar, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 275 papers*

- **[Semantic Consistent Language Gaussian Splatting for Point-Level Open-vocabulary Querying](https://arxiv.org/abs/2503.21767v1)**  
  Authors: Hairong Yin, Huangying Zhan, Yi Xu, Raymond A. Yeh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21767v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, gaussian splatting, segmentation  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: high-fidelity, semantic, mapping, 3d gaussian, dynamic, slam, ar, robotics, localization  
- **[Feature4X: Bridging Any Monocular Video to 4D Agentic AI with Versatile Gaussian Feature Fields](https://arxiv.org/abs/2503.20776v1)**  
  Authors: Shijie Zhou, Hui Ren, Yijia Weng, Shuwang Zhang, Zhen Wang, Dejia Xu, Zhiwen Fan, Suya You, Zhangyang Wang, Leonidas Guibas, Achuta Kadambi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20776v1.pdf)  
  Keywords: semantic, dynamic, 4d, ar, gaussian splatting, segmentation  
- **[PartRM: Modeling Part-Level Dynamics with Large Cross-State Reconstruction Model](https://arxiv.org/abs/2503.19913v1)**  
  Authors: Mingju Gao, Yike Pan, Huan-ang Gao, Zongzheng Zhang, Wenyi Li, Hao Dong, Hao Tang, Li Yi, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19913v1.pdf)  
  Keywords: understanding, 3d gaussian, dynamic, geometry, ar, robotics, 4d, motion  
- **[COB-GS: Clear Object Boundaries in 3DGS Segmentation Based on Boundary-Adaptive Gaussian Splitting](https://arxiv.org/abs/2503.19443v2)**  
  Authors: Jiaxin Zhang, Junjun Jiang, Youyu Chen, Kui Jiang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19443v2.pdf) | [![GitHub](https://img.shields.io/github/stars/ZestfulJX/COB-GS?style=social)](https://github.com/ZestfulJX/COB-GS)  
  Keywords: understanding, semantic, 3d gaussian, ar, gaussian splatting, segmentation  
- **[Divide-and-Conquer: Dual-Hierarchical Optimization for Semantic 4D Gaussian Spatting](https://arxiv.org/abs/2503.19332v1)**  
  Authors: Zhiying Yan, Yiyuan Liang, Shilv Cai, Tao Zhang, Sheng Zhong, Luxin Yan, Xu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19332v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sweety-yan.github.io/DHO.)  
  Keywords: understanding, semantic, dynamic, ar, gaussian splatting, 4d  
- **[MATT-GS: Masked Attention-based 3DGS for Robot Perception and Object Detection](https://arxiv.org/abs/2503.19330v1)**  
  Authors: Jee Won Lee, Hansol Lim, SooYeun Yang, Jongseong Brad Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19330v1.pdf)  
  Keywords: lighting, recognition, 3d gaussian, ar, gaussian splatting  
- **[PanoGS: Gaussian-based Panoptic Segmentation for 3D Open Vocabulary Scene Understanding](https://arxiv.org/abs/2503.18107v1)**  
  Authors: Hongjia Zhai, Hai Li, Zhenzhe Li, Xiaokun Pan, Yijia He, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18107v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/panogs}{https://zju3dv.github.io/panogs}.)  
  Keywords: understanding, 3d gaussian, geometry, ar, gaussian splatting, segmentation  
- **[PanopticSplatting: End-to-End Panoptic Gaussian Splatting](https://arxiv.org/abs/2503.18073v1)**  
  Authors: Yuxuan Xie, Xuan Yu, Changjian Jiang, Sitong Mao, Shunbo Zhou, Rui Fan, Rong Xiong, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18073v1.pdf)  
  Keywords: understanding, nerf, large scene, ar, gaussian splatting, segmentation  
- **[SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining](https://arxiv.org/abs/2503.18052v1)**  
  Authors: Yue Li, Qi Ma, Runyi Yang, Huapeng Li, Mengjiao Ma, Bin Ren, Nikola Popovic, Nicu Sebe, Ender Konukoglu, Theo Gevers, Luc Van Gool, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18052v1.pdf)  
  Keywords: understanding, semantic, 3d gaussian, ar, gaussian splatting  



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