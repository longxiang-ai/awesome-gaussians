# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-06-03 00:57:06

## Categories

- [3DGS Surveys](#3dgs-surveys) (35 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (528 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1845 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (622 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (693 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (132 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (601 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (107 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (710 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (297 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (41 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (204 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (275 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (329 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: high-fidelity, efficient, understanding, gaussian splatting, semantic, 3d reconstruction, outdoor, survey, segmentation, 3d gaussian, neural rendering, ar  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: slam, efficient, nerf, mapping, gaussian splatting, semantic, segmentation, localization, survey, ar, 3d gaussian  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: body, motion, dynamic, 4d, gaussian splatting, understanding, ar, survey, 3d gaussian  
- **[A Survey of 3D Reconstruction with Event Cameras: From Event-based Geometry to Neural 3D Rendering](https://arxiv.org/abs/2505.08438v1)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v1.pdf)  
  Keywords: motion, dynamic, gaussian splatting, ar, 3d reconstruction, geometry, survey, 3d gaussian, neural rendering  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: efficient, fast, gaussian splatting, ar, 3d reconstruction, survey  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: nerf, semantic, ar, survey, robotics, 3d gaussian, autonomous driving  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: ar, 3d reconstruction, survey, lighting, 3d gaussian  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: face, nerf, sparse view, understanding, gaussian splatting, ar, 3d reconstruction, geometry, survey, outdoor, 3d gaussian  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: gaussian splatting, semantic, segmentation, ar, survey, lighting, 3d gaussian, robotics  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: motion, dynamic, fast, gaussian splatting, ar, 3d reconstruction, survey, lighting, 3d gaussian  

### Acceleration

*Showing the latest 50 out of 528 papers*

- **[TC-GS: A Faster Gaussian Splatting Module Utilizing Tensor Cores](https://arxiv.org/abs/2505.24796v1)**  
  Authors: Zimu Liao, Jifeng Ding, Rong Fu, Siwei Cui, Ruixuan Gong, Li Wang, Boni Hu, Yi Wang, Hengjie Li, XIngcheng Zhang, Hui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TensorCore3DGS/3DGSTensorCore?style=social)](https://github.com/TensorCore3DGS/3DGSTensorCore)  
  Keywords: compression, mapping, fast, gaussian splatting, 3d gaussian, acceleration  
- **[GARLIC: GAussian Representation LearnIng for spaCe partitioning](https://arxiv.org/abs/2505.24608v1)**  
  Authors: Panagiotis Rigas, Panagiotis Drivas, Charalambos Tzamos, Ioannis Chamodrakas, George Ioannakis, Leonidas J. Guibas, Ioannis Z. Emiris  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24608v1.pdf)  
  Keywords: efficient, fast, gaussian splatting, ar, semantic  
- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: efficient, nerf, dynamic, head, gaussian splatting, ar, outdoor, 3d gaussian, real-time rendering, efficient rendering  
- **[3DGS Compression with Sparsity-guided Hierarchical Transform Coding](https://arxiv.org/abs/2505.22908v1)**  
  Authors: Hao Xu, Xiaolin Wu, Xi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22908v1.pdf)  
  Keywords: compression, lightweight, fast, gaussian splatting, head, ar, 3d gaussian  
- **[STDR: Spatio-Temporal Decoupling for Real-Time Dynamic Scene Rendering](https://arxiv.org/abs/2505.22400v1)**  
  Authors: Zehao Li, Hao Jiang, Yujun Cai, Jianing Chen, Baolong Bi, Shuqin Gao, Honglong Zhao, Yiwei Wang, Tianlu Mao, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22400v1.pdf)  
  Keywords: motion, deformation, dynamic, gaussian splatting, ar, 3d gaussian, real-time rendering  
- **[3D-UIR: 3D Gaussian for Underwater 3D Scene Reconstruction via Physics Based Appearance-Medium Decoupling](https://arxiv.org/abs/2505.21238v2)**  
  Authors: Jieyu Yuan, Yujun Li, Yuanlin Zhang, Chunle Guo, Xiongxin Tang, Ruixing Wang, Chongyi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21238v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bilityniu.github.io/3D-UIR.)  
  Keywords: body, gaussian splatting, ar, 3d gaussian, real-time rendering  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: efficient, lightweight, gaussian splatting, ar, geometry, 3d gaussian, real-time rendering, compact, urban scene  
- **[Weather-Magician: Reconstruction and Rendering Framework for 4D Weather Synthesis In Real Time](https://arxiv.org/abs/2505.19919v1)**  
  Authors: Chen Sang, Yeqiang Qian, Jiale Zhang, Chunxiang Wang, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19919v1.pdf)  
  Keywords: vr, efficient, 4d, dynamic, gaussian splatting, ar, real-time rendering  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: face, motion, fast, gaussian splatting, ar, 3d reconstruction, sparse-view  
- **[K-Buffers: A Plug-in Method for Enhancing Neural Fields with Multiple Buffers](https://arxiv.org/abs/2505.19564v1)**  
  Authors: Haofan Ren, Zunjie Zhu, Xiang Chen, Ming Lu, Rongfeng Lu, Chenggang Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19564v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian, acceleration  

### Applications

*Showing the latest 50 out of 1845 papers*

- **[AdaHuman: Animatable Detailed 3D Human Generation with Compositional Multiview Diffusion](https://arxiv.org/abs/2505.24877v1)**  
  Authors: Yangyi Huang, Ye Yuan, Xueting Li, Jan Kautz, Umar Iqbal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24877v1.pdf)  
  Keywords: high-fidelity, body, motion, animation, ar, 3d gaussian, human, avatar  
- **[Tackling View-Dependent Semantics in 3D Language Gaussian Splatting](https://arxiv.org/abs/2505.24746v1)**  
  Authors: Jiazhong Cen, Xudong Zhou, Jiemin Fang, Changsong Wen, Lingxi Xie, Xiaopeng Zhang, Wei Shen, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24746v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SJTU-DeepVisionLab/LaGa?style=social)](https://github.com/SJTU-DeepVisionLab/LaGa)  
  Keywords: understanding, gaussian splatting, semantic, ar, 3d gaussian  
- **[GARLIC: GAussian Representation LearnIng for spaCe partitioning](https://arxiv.org/abs/2505.24608v1)**  
  Authors: Panagiotis Rigas, Panagiotis Drivas, Charalambos Tzamos, Ioannis Chamodrakas, George Ioannakis, Leonidas J. Guibas, Ioannis Z. Emiris  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24608v1.pdf)  
  Keywords: efficient, fast, gaussian splatting, ar, semantic  
- **[LTM3D: Bridging Token Spaces for Conditional 3D Generation with Auto-Regressive Diffusion Framework](https://arxiv.org/abs/2505.24245v1)**  
  Authors: Xin Kang, Zihan Zheng, Lei Chu, Yue Gao, Jiahao Li, Hao Pan, Xuejin Chen, Yan Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24245v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian  
- **[3DGEER: Exact and Efficient Volumetric Rendering with 3D Gaussians](https://arxiv.org/abs/2505.24053v1)**  
  Authors: Zixun Huang, Cho-Ying Wu, Yuliang Guo, Xinyu Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24053v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, 3d gaussian, neural rendering  
- **[ZPressor: Bottleneck-Aware Compression for Scalable Feed-Forward 3DGS](https://arxiv.org/abs/2505.23734v2)**  
  Authors: Weijie Wang, Donny Y. Chen, Zeyu Zhang, Duochao Shi, Akide Liu, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23734v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lhmd.top/zpressor.)  
  Keywords: compression, efficient, lightweight, gaussian splatting, ar, 3d gaussian, compact  
- **[AnySplat: Feed-forward 3D Gaussian Splatting from Unconstrained Views](https://arxiv.org/abs/2505.23716v1)**  
  Authors: Lihan Jiang, Yucheng Mao, Linning Xu, Tao Lu, Kerui Ren, Yichen Jin, Xudong Xu, Mulin Yu, Jiangmiao Pang, Feng Zhao, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://city-super.github.io/anysplat/)  
  Keywords: gaussian splatting, ar, geometry, 3d gaussian, neural rendering  
- **[Mobi-$π$: Mobilizing Your Robot Learning Policy](https://arxiv.org/abs/2505.23692v1)**  
  Authors: Jingyun Yang, Isabella Huang, Brandon Vu, Max Bajracharya, Rika Antonova, Jeannette Bohg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23692v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian  
- **[Radiant Triangle Soup with Soft Connectivity Forces for 3D Reconstruction and Novel View Synthesis](https://arxiv.org/abs/2505.23642v1)**  
  Authors: Nathaniel Burgdorfer, Philippos Mordohai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23642v1.pdf)  
  Keywords: ar, 3d reconstruction, geometry, face  
- **[Holistic Large-Scale Scene Reconstruction via Mixed Gaussian Splatting](https://arxiv.org/abs/2505.23280v1)**  
  Authors: Chuandong Liu, Huijiao Wang, Lei Yu, Gui-Song Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23280v1.pdf) | [![GitHub](https://img.shields.io/github/stars/azhuantou/MixGS?style=social)](https://github.com/azhuantou/MixGS)  
  Keywords: gaussian splatting, vr, ar, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 622 papers*

- **[AdaHuman: Animatable Detailed 3D Human Generation with Compositional Multiview Diffusion](https://arxiv.org/abs/2505.24877v1)**  
  Authors: Yangyi Huang, Ye Yuan, Xueting Li, Jan Kautz, Umar Iqbal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24877v1.pdf)  
  Keywords: high-fidelity, body, motion, animation, ar, 3d gaussian, human, avatar  
- **[Radiant Triangle Soup with Soft Connectivity Forces for 3D Reconstruction and Novel View Synthesis](https://arxiv.org/abs/2505.23642v1)**  
  Authors: Nathaniel Burgdorfer, Philippos Mordohai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23642v1.pdf)  
  Keywords: ar, 3d reconstruction, geometry, face  
- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: efficient, nerf, dynamic, head, gaussian splatting, ar, outdoor, 3d gaussian, real-time rendering, efficient rendering  
- **[SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images](https://arxiv.org/abs/2505.23044v1)**  
  Authors: Yu Sheng, Jiajun Deng, Xinran Zhang, Yu Zhang, Bei Hua, Yanyong Zhang, Jianmin Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23044v1.pdf)  
  Keywords: efficient, head, semantic, ar, 3d reconstruction, 3d gaussian, compact  
- **[3DGS Compression with Sparsity-guided Hierarchical Transform Coding](https://arxiv.org/abs/2505.22908v1)**  
  Authors: Hao Xu, Xiaolin Wu, Xi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22908v1.pdf)  
  Keywords: compression, lightweight, fast, gaussian splatting, head, ar, 3d gaussian  
- **[4DTAM: Non-Rigid Tracking and Mapping via Dynamic Surface Gaussians](https://arxiv.org/abs/2505.22859v1)**  
  Authors: Hidenobu Matsuki, Gwangbin Bae, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22859v1.pdf)  
  Keywords: face, slam, motion, animation, deformation, dynamic, 4d, mapping, ar, geometry, localization, 3d gaussian, tracking  
- **[Hyperspectral Gaussian Splatting](https://arxiv.org/abs/2505.21890v1)**  
  Authors: Sunil Kumar Narayanan, Lingjun Zhao, Lu Gan, Yongsheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21890v1.pdf)  
  Keywords: face, nerf, gaussian splatting, ar, 3d reconstruction, 3d gaussian  
- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: high-fidelity, face, illumination, relightable, gaussian splatting, ar, geometry, ray tracing, relighting, 3d gaussian, neural rendering, lighting, shadow, human  
- **[Structure from Collision](https://arxiv.org/abs/2505.21335v1)**  
  Authors: Takuhiro Kaneko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21335v1.pdf)  
  Keywords: face, nerf, gaussian splatting, ar, 3d gaussian  
- **[3D-UIR: 3D Gaussian for Underwater 3D Scene Reconstruction via Physics Based Appearance-Medium Decoupling](https://arxiv.org/abs/2505.21238v2)**  
  Authors: Jieyu Yuan, Yujun Li, Yuanlin Zhang, Chunle Guo, Xiongxin Tang, Ruixing Wang, Chongyi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21238v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bilityniu.github.io/3D-UIR.)  
  Keywords: body, gaussian splatting, ar, 3d gaussian, real-time rendering  

### Dynamic Scene

*Showing the latest 50 out of 693 papers*

- **[AdaHuman: Animatable Detailed 3D Human Generation with Compositional Multiview Diffusion](https://arxiv.org/abs/2505.24877v1)**  
  Authors: Yangyi Huang, Ye Yuan, Xueting Li, Jan Kautz, Umar Iqbal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24877v1.pdf)  
  Keywords: high-fidelity, body, motion, animation, ar, 3d gaussian, human, avatar  
- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: efficient, nerf, dynamic, head, gaussian splatting, ar, outdoor, 3d gaussian, real-time rendering, efficient rendering  
- **[4DTAM: Non-Rigid Tracking and Mapping via Dynamic Surface Gaussians](https://arxiv.org/abs/2505.22859v1)**  
  Authors: Hidenobu Matsuki, Gwangbin Bae, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22859v1.pdf)  
  Keywords: face, slam, motion, animation, deformation, dynamic, 4d, mapping, ar, geometry, localization, 3d gaussian, tracking  
- **[CLIPGaussian: Universal and Multimodal Style Transfer Based on Gaussian Splatting](https://arxiv.org/abs/2505.22854v1)**  
  Authors: Kornel Howil, Joanna Waczyńska, Piotr Borycki, Tadeusz Dziarmaga, Marcin Mazur, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22854v1.pdf)  
  Keywords: efficient, 4d, dynamic, gaussian splatting, ar, geometry  
- **[STDR: Spatio-Temporal Decoupling for Real-Time Dynamic Scene Rendering](https://arxiv.org/abs/2505.22400v1)**  
  Authors: Zehao Li, Hao Jiang, Yujun Cai, Jianing Chen, Baolong Bi, Shuqin Gao, Honglong Zhao, Yiwei Wang, Tianlu Mao, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22400v1.pdf)  
  Keywords: motion, deformation, dynamic, gaussian splatting, ar, 3d gaussian, real-time rendering  
- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: high-fidelity, slam, motion, efficient, dynamic, mapping, gaussian splatting, semantic, localization, ar, 3d gaussian, tracking  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: face, motion, gaussian splatting, ar, 3d gaussian, sparse-view  
- **[WeatherEdit: Controllable Weather Editing with 4D Gaussian Field](https://arxiv.org/abs/2505.20471v1)**  
  Authors: Chenghao Qian, Wenjing Li, Yuhu Guo, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/w-edit)  
  Keywords: 4d, dynamic, ar, lighting, autonomous driving  
- **[ParticleGS: Particle-Based Dynamics Modeling of 3D Gaussians for Prior-free Motion Extrapolation](https://arxiv.org/abs/2505.20270v1)**  
  Authors: Jinsheng Quan, Chunshi Wang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20270v1.pdf) | [![GitHub](https://img.shields.io/github/stars/QuanJinSheng/ParticleGS?style=social)](https://github.com/QuanJinSheng/ParticleGS)  
  Keywords: motion, deformation, dynamic, gaussian splatting, ar, 3d reconstruction, 3d gaussian  
- **[Weather-Magician: Reconstruction and Rendering Framework for 4D Weather Synthesis In Real Time](https://arxiv.org/abs/2505.19919v1)**  
  Authors: Chen Sang, Yeqiang Qian, Jiale Zhang, Chunxiang Wang, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19919v1.pdf)  
  Keywords: vr, efficient, 4d, dynamic, gaussian splatting, ar, real-time rendering  

### Few-shot

*Showing the latest 50 out of 132 papers*

- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: efficient, nerf, gaussian splatting, ar, geometry, 3d gaussian, sparse-view  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: face, motion, gaussian splatting, ar, 3d gaussian, sparse-view  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: face, motion, fast, gaussian splatting, ar, 3d reconstruction, sparse-view  
- **[Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse Views by Jointly Training Hemisphere Sampled Synthetic Images](https://arxiv.org/abs/2505.19264v1)**  
  Authors: Guangan Chen, Anh Minh Truong, Hanhe Lin, Michiel Vlaminck, Wilfried Philips, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19264v1.pdf)  
  Keywords: motion, sparse view, gaussian splatting, ar, 3d gaussian, sparse-view  
- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: motion, efficient, deformation, 4d, dynamic, gaussian splatting, head, 3d reconstruction, ar, compact, sparse-view  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, robotics, 3d gaussian, sparse-view  
- **[X-GRM: Large Gaussian Reconstruction Model for Sparse-view X-rays to Computed Tomography](https://arxiv.org/abs/2505.15235v2)**  
  Authors: Yifan Liu, Wuyang Li, Weihao Yu, Chenxin Li, Alexandre Alahi, Max Meng, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15235v2.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/X-GRM?style=social)](https://github.com/CUHK-AIM-Group/X-GRM)  
  Keywords: gaussian splatting, efficient, ar, sparse-view  
- **[SpatialCrafter: Unleashing the Imagination of Video Diffusion Models for Scene Reconstruction from Limited Observations](https://arxiv.org/abs/2505.11992v1)**  
  Authors: Songchun Zhang, Huiyao Xu, Sitong Guo, Zhongwei Xie, Pengwei Liu, Hujun Bao, Weiwei Xu, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11992v1.pdf)  
  Keywords: efficient, sparse view, semantic, ar, 3d gaussian  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: face, shape reconstruction, efficient, sparse view, fast, gaussian splatting, head, geometry, ar  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: face, shape reconstruction, sparse view, fast, gaussian splatting, ar, 3d reconstruction, geometry, 3d gaussian, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 601 papers*

- **[AnySplat: Feed-forward 3D Gaussian Splatting from Unconstrained Views](https://arxiv.org/abs/2505.23716v1)**  
  Authors: Lihan Jiang, Yucheng Mao, Linning Xu, Tao Lu, Kerui Ren, Yichen Jin, Xudong Xu, Mulin Yu, Jiangmiao Pang, Feng Zhao, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://city-super.github.io/anysplat/)  
  Keywords: gaussian splatting, ar, geometry, 3d gaussian, neural rendering  
- **[Radiant Triangle Soup with Soft Connectivity Forces for 3D Reconstruction and Novel View Synthesis](https://arxiv.org/abs/2505.23642v1)**  
  Authors: Nathaniel Burgdorfer, Philippos Mordohai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23642v1.pdf)  
  Keywords: ar, 3d reconstruction, geometry, face  
- **[SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images](https://arxiv.org/abs/2505.23044v1)**  
  Authors: Yu Sheng, Jiajun Deng, Xinran Zhang, Yu Zhang, Bei Hua, Yanyong Zhang, Jianmin Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23044v1.pdf)  
  Keywords: efficient, head, semantic, ar, 3d reconstruction, 3d gaussian, compact  
- **[Pose-free 3D Gaussian splatting via shape-ray estimation](https://arxiv.org/abs/2505.22978v1)**  
  Authors: Youngju Na, Taeyeon Kim, Jumin Lee, Kyu Beom Han, Woo Jae Kim, Sung-eui Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22978v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, geometry, 3d gaussian  
- **[4DTAM: Non-Rigid Tracking and Mapping via Dynamic Surface Gaussians](https://arxiv.org/abs/2505.22859v1)**  
  Authors: Hidenobu Matsuki, Gwangbin Bae, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22859v1.pdf)  
  Keywords: face, slam, motion, animation, deformation, dynamic, 4d, mapping, ar, geometry, localization, 3d gaussian, tracking  
- **[CLIPGaussian: Universal and Multimodal Style Transfer Based on Gaussian Splatting](https://arxiv.org/abs/2505.22854v1)**  
  Authors: Kornel Howil, Joanna Waczyńska, Piotr Borycki, Tadeusz Dziarmaga, Marcin Mazur, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22854v1.pdf)  
  Keywords: efficient, 4d, dynamic, gaussian splatting, ar, geometry  
- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: efficient, nerf, gaussian splatting, ar, geometry, 3d gaussian, sparse-view  
- **[Hyperspectral Gaussian Splatting](https://arxiv.org/abs/2505.21890v1)**  
  Authors: Sunil Kumar Narayanan, Lingjun Zhao, Lu Gan, Yongsheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21890v1.pdf)  
  Keywords: face, nerf, gaussian splatting, ar, 3d reconstruction, 3d gaussian  
- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: high-fidelity, face, illumination, relightable, gaussian splatting, ar, geometry, ray tracing, relighting, 3d gaussian, neural rendering, lighting, shadow, human  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: efficient, lightweight, gaussian splatting, ar, geometry, 3d gaussian, real-time rendering, compact, urban scene  

### Large Scene

*Showing the latest 50 out of 107 papers*

- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: efficient, nerf, dynamic, head, gaussian splatting, ar, outdoor, 3d gaussian, real-time rendering, efficient rendering  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: efficient, lightweight, gaussian splatting, ar, geometry, 3d gaussian, real-time rendering, compact, urban scene  
- **[HaloGS: Loose Coupling of Compact Geometry and Gaussian Splats for 3D Scenes](https://arxiv.org/abs/2505.20267v1)**  
  Authors: Changjian Jiang, Kerui Ren, Linning Xu, Jiong Chen, Jiangmiao Pang, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20267v1.pdf)  
  Keywords: lightweight, ar, 3d reconstruction, outdoor, geometry, compact  
- **[VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale Scenes](https://arxiv.org/abs/2505.18992v1)**  
  Authors: Tianchen Deng, Wenhua Wu, Junjie He, Yue Pan, Xirui Jiang, Shenghai Yuan, Danwei Wang, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18992v1.pdf) | [![GitHub](https://img.shields.io/github/stars/dtc111111/vpgs-slam?style=social)](https://github.com/dtc111111/vpgs-slam)  
  Keywords: slam, mapping, gaussian splatting, ar, outdoor, 3d gaussian, compact, tracking  
- **[SplatCo: Structure-View Collaborative Gaussian Splatting for Detail-Preserving Rendering of Large-Scale Unbounded Scenes](https://arxiv.org/abs/2505.17951v1)**  
  Authors: Haihong Xiao, Jianan Zou, Yuxin Zhou, Ying He, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17951v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SCUT-BIP-Lab/SplatCo?style=social)](https://github.com/SCUT-BIP-Lab/SplatCo)  
  Keywords: high-fidelity, face, gaussian splatting, ar, outdoor  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: high-fidelity, efficient, understanding, gaussian splatting, semantic, 3d reconstruction, outdoor, survey, segmentation, 3d gaussian, neural rendering, ar  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: face, lightweight, gaussian splatting, ar, localization, outdoor, lighting, human  
- **[Gaussian Splatting as a Unified Representation for Autonomy in Unstructured Environments](https://arxiv.org/abs/2505.11794v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11794v1.pdf)  
  Keywords: gaussian splatting, semantic, outdoor, ar  
- **[EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes](https://arxiv.org/abs/2505.10787v1)**  
  Authors: Jianlin Guo, Haihong Xiao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10787v1.pdf)  
  Keywords: face, efficient, nerf, gaussian splatting, ar, geometry, outdoor, 3d gaussian, real-time rendering  
- **[Consistent Quantity-Quality Control across Scenes for Deployment-Aware Gaussian Splatting](https://arxiv.org/abs/2505.10473v2)**  
  Authors: Fengdi Zhang, Hongkun Cao, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10473v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhang-fengdi.github.io/ControlGS/)  
  Keywords: gaussian splatting, semantic, ar, outdoor, 3d gaussian, compact  

### Model Compression

*Showing the latest 50 out of 710 papers*

- **[TC-GS: A Faster Gaussian Splatting Module Utilizing Tensor Cores](https://arxiv.org/abs/2505.24796v1)**  
  Authors: Zimu Liao, Jifeng Ding, Rong Fu, Siwei Cui, Ruixuan Gong, Li Wang, Boni Hu, Yi Wang, Hengjie Li, XIngcheng Zhang, Hui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TensorCore3DGS/3DGSTensorCore?style=social)](https://github.com/TensorCore3DGS/3DGSTensorCore)  
  Keywords: compression, mapping, fast, gaussian splatting, 3d gaussian, acceleration  
- **[GARLIC: GAussian Representation LearnIng for spaCe partitioning](https://arxiv.org/abs/2505.24608v1)**  
  Authors: Panagiotis Rigas, Panagiotis Drivas, Charalambos Tzamos, Ioannis Chamodrakas, George Ioannakis, Leonidas J. Guibas, Ioannis Z. Emiris  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24608v1.pdf)  
  Keywords: efficient, fast, gaussian splatting, ar, semantic  
- **[3DGEER: Exact and Efficient Volumetric Rendering with 3D Gaussians](https://arxiv.org/abs/2505.24053v1)**  
  Authors: Zixun Huang, Cho-Ying Wu, Yuliang Guo, Xinyu Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24053v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, 3d gaussian, neural rendering  
- **[ZPressor: Bottleneck-Aware Compression for Scalable Feed-Forward 3DGS](https://arxiv.org/abs/2505.23734v2)**  
  Authors: Weijie Wang, Donny Y. Chen, Zeyu Zhang, Duochao Shi, Akide Liu, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23734v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lhmd.top/zpressor.)  
  Keywords: compression, efficient, lightweight, gaussian splatting, ar, 3d gaussian, compact  
- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: efficient, nerf, dynamic, head, gaussian splatting, ar, outdoor, 3d gaussian, real-time rendering, efficient rendering  
- **[SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images](https://arxiv.org/abs/2505.23044v1)**  
  Authors: Yu Sheng, Jiajun Deng, Xinran Zhang, Yu Zhang, Bei Hua, Yanyong Zhang, Jianmin Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23044v1.pdf)  
  Keywords: efficient, head, semantic, ar, 3d reconstruction, 3d gaussian, compact  
- **[Pose-free 3D Gaussian splatting via shape-ray estimation](https://arxiv.org/abs/2505.22978v1)**  
  Authors: Youngju Na, Taeyeon Kim, Jumin Lee, Kyu Beom Han, Woo Jae Kim, Sung-eui Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22978v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, geometry, 3d gaussian  
- **[3DGS Compression with Sparsity-guided Hierarchical Transform Coding](https://arxiv.org/abs/2505.22908v1)**  
  Authors: Hao Xu, Xiaolin Wu, Xi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22908v1.pdf)  
  Keywords: compression, lightweight, fast, gaussian splatting, head, ar, 3d gaussian  
- **[CLIPGaussian: Universal and Multimodal Style Transfer Based on Gaussian Splatting](https://arxiv.org/abs/2505.22854v1)**  
  Authors: Kornel Howil, Joanna Waczyńska, Piotr Borycki, Tadeusz Dziarmaga, Marcin Mazur, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22854v1.pdf)  
  Keywords: efficient, 4d, dynamic, gaussian splatting, ar, geometry  
- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: high-fidelity, slam, motion, efficient, dynamic, mapping, gaussian splatting, semantic, localization, ar, 3d gaussian, tracking  

### Quality Enhancement

*Showing the latest 50 out of 297 papers*

- **[AdaHuman: Animatable Detailed 3D Human Generation with Compositional Multiview Diffusion](https://arxiv.org/abs/2505.24877v1)**  
  Authors: Yangyi Huang, Ye Yuan, Xueting Li, Jan Kautz, Umar Iqbal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24877v1.pdf)  
  Keywords: high-fidelity, body, motion, animation, ar, 3d gaussian, human, avatar  
- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: high-fidelity, slam, motion, efficient, dynamic, mapping, gaussian splatting, semantic, localization, ar, 3d gaussian, tracking  
- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: high-fidelity, face, illumination, relightable, gaussian splatting, ar, geometry, ray tracing, relighting, 3d gaussian, neural rendering, lighting, shadow, human  
- **[OB3D: A New Dataset for Benchmarking Omnidirectional 3D Reconstruction Using Blender](https://arxiv.org/abs/2505.20126v1)**  
  Authors: Shintaro Ito, Natsuki Takama, Toshiki Watanabe, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20126v1.pdf)  
  Keywords: high-fidelity, nerf, gaussian splatting, ar, 3d reconstruction, 3d gaussian  
- **[SplatCo: Structure-View Collaborative Gaussian Splatting for Detail-Preserving Rendering of Large-Scale Unbounded Scenes](https://arxiv.org/abs/2505.17951v1)**  
  Authors: Haihong Xiao, Jianan Zou, Yuxin Zhou, Ying He, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17951v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SCUT-BIP-Lab/SplatCo?style=social)](https://github.com/SCUT-BIP-Lab/SplatCo)  
  Keywords: high-fidelity, face, gaussian splatting, ar, outdoor  
- **[CGS-GAN: 3D Consistent Gaussian Splatting GANs for High Resolution Human Head Synthesis](https://arxiv.org/abs/2505.17590v1)**  
  Authors: Florian Barthel, Wieland Morgenstern, Paul Hinzer, Anna Hilsmann, Peter Eisert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17590v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fraunhoferhhi.github.io/cgs-gan/)  
  Keywords: efficient, head, gaussian splatting, high quality, ar, 3d gaussian, human, efficient rendering  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: high-fidelity, efficient, understanding, gaussian splatting, semantic, 3d reconstruction, outdoor, survey, segmentation, 3d gaussian, neural rendering, ar  
- **[Render-FM: A Foundation Model for Real-time Photorealistic Volumetric Rendering](https://arxiv.org/abs/2505.17338v1)**  
  Authors: Zhongpai Gao, Meng Zheng, Benjamin Planche, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17338v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/renderfm/.)  
  Keywords: high-fidelity, efficient, medical, gaussian splatting, ar, neural rendering  
- **[Motion Matters: Compact Gaussian Streaming for Free-Viewpoint Video Reconstruction](https://arxiv.org/abs/2505.16533v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Youneng Bao, Xiandong Meng, Fanyang Meng, Ronggang Wang, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16533v1.pdf)  
  Keywords: high-fidelity, face, motion, efficient, dynamic, head, gaussian splatting, ar, 3d gaussian, compact  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, robotics, 3d gaussian, sparse-view  

### Ray Tracing

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: high-fidelity, face, illumination, relightable, gaussian splatting, ar, geometry, ray tracing, relighting, 3d gaussian, neural rendering, lighting, shadow, human  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: relightable, gaussian splatting, fast, geometry, ar, ray tracing, relighting, lighting, shadow, human, avatar  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: efficient, gaussian splatting, ar, ray tracing, relighting, 3d gaussian, acceleration, lighting, efficient rendering  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: efficient, animation, dynamic, gaussian splatting, ar, 3d gaussian, acceleration, compact, ray marching  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: face, global illumination, illumination, efficient, gaussian splatting, ar, ray tracing, lighting, 3d gaussian, real-time rendering  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: face, global illumination, illumination, light transport, dynamic, fast, lighting, 3d gaussian, real-time rendering  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: reflection, fast, gaussian splatting, ar, ray tracing, shadow, 3d gaussian, neural rendering  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: face, efficient, dynamic, relightable, 4d, ar, geometry, ray tracing, lighting, real-time rendering, tracking  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: face, reflection, gaussian splatting, ray tracing, shadow, lighting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, ar, survey, ray tracing, 3d gaussian  

### Relighting

*Showing the latest 50 out of 204 papers*

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: high-fidelity, face, illumination, relightable, gaussian splatting, ar, geometry, ray tracing, relighting, 3d gaussian, neural rendering, lighting, shadow, human  
- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: illumination, efficient, mapping, ar, shadow, lighting, 3d gaussian  
- **[WeatherEdit: Controllable Weather Editing with 4D Gaussian Field](https://arxiv.org/abs/2505.20471v1)**  
  Authors: Chenghao Qian, Wenjing Li, Yuhu Guo, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/w-edit)  
  Keywords: 4d, dynamic, ar, lighting, autonomous driving  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: face, lightweight, gaussian splatting, ar, localization, outdoor, lighting, human  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: high-fidelity, motion, gaussian splatting, ar, 3d reconstruction, lighting, 3d gaussian  
- **[3D Gaussian Adaptive Reconstruction for Fourier Light-Field Microscopy](https://arxiv.org/abs/2505.12875v1)**  
  Authors: Chenyu Xu, Zhouyu Jin, Chengkang Shen, Hao Zhu, Zhan Ma, Bo Xiong, You Zhou, Xun Cao, Ning Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12875v1.pdf)  
  Keywords: nerf, gaussian splatting, ar, lighting, 3d gaussian  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: ar, 3d reconstruction, survey, lighting, 3d gaussian  
- **[TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians](https://arxiv.org/abs/2504.18768v2)**  
  Authors: Letian Huang, Dongwei Ye, Jialin Dan, Chengzhi Tao, Huiwen Liu, Kun Zhou, Bo Ren, Yuanqi Li, Yanwen Guo, Jie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18768v2.pdf)  
  Keywords: efficient, reflection, fast, gaussian splatting, ar, 3d gaussian  
- **[RGS-DR: Reflective Gaussian Surfels with Deferred Rendering for Shiny Objects](https://arxiv.org/abs/2504.18468v3)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18468v3.pdf)  
  Keywords: face, nerf, reflection, gaussian splatting, ar, geometry, relighting, lighting, 3d gaussian  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: vr, nerf, mapping, fast, gaussian splatting, ar, lighting, 3d gaussian  

### SLAM

*Showing the latest 50 out of 275 papers*

- **[TC-GS: A Faster Gaussian Splatting Module Utilizing Tensor Cores](https://arxiv.org/abs/2505.24796v1)**  
  Authors: Zimu Liao, Jifeng Ding, Rong Fu, Siwei Cui, Ruixuan Gong, Li Wang, Boni Hu, Yi Wang, Hengjie Li, XIngcheng Zhang, Hui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TensorCore3DGS/3DGSTensorCore?style=social)](https://github.com/TensorCore3DGS/3DGSTensorCore)  
  Keywords: compression, mapping, fast, gaussian splatting, 3d gaussian, acceleration  
- **[4DTAM: Non-Rigid Tracking and Mapping via Dynamic Surface Gaussians](https://arxiv.org/abs/2505.22859v1)**  
  Authors: Hidenobu Matsuki, Gwangbin Bae, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22859v1.pdf)  
  Keywords: face, slam, motion, animation, deformation, dynamic, 4d, mapping, ar, geometry, localization, 3d gaussian, tracking  
- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: high-fidelity, slam, motion, efficient, dynamic, mapping, gaussian splatting, semantic, localization, ar, 3d gaussian, tracking  
- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: illumination, efficient, mapping, ar, shadow, lighting, 3d gaussian  
- **[ProBA: Probabilistic Bundle Adjustment with the Bhattacharyya Coefficient](https://arxiv.org/abs/2505.20858v1)**  
  Authors: Jason Chui, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20858v1.pdf)  
  Keywords: ar, efficient, slam, 3d gaussian  
- **[ADD-SLAM: Adaptive Dynamic Dense SLAM with Gaussian Splatting](https://arxiv.org/abs/2505.19420v1)**  
  Authors: Wenhua Wu, Chenpeng Su, Siting Zhu, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19420v1.pdf)  
  Keywords: slam, nerf, dynamic, mapping, gaussian splatting, semantic, segmentation, recognition, localization, ar, 3d gaussian, tracking  
- **[FHGS: Feature-Homogenized Gaussian Splatting](https://arxiv.org/abs/2505.19154v1)**  
  Authors: Q. G. Duan, Benyun Zhao, Mingqiao Han Yijun Huang, Ben M. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19154v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fhgs.cuastro.org/.)  
  Keywords: efficient, mapping, understanding, gaussian splatting, semantic, ar, 3d gaussian, real-time rendering, efficient rendering  
- **[VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale Scenes](https://arxiv.org/abs/2505.18992v1)**  
  Authors: Tianchen Deng, Wenhua Wu, Junjie He, Yue Pan, Xirui Jiang, Shenghai Yuan, Danwei Wang, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18992v1.pdf) | [![GitHub](https://img.shields.io/github/stars/dtc111111/vpgs-slam?style=social)](https://github.com/dtc111111/vpgs-slam)  
  Keywords: slam, mapping, gaussian splatting, ar, outdoor, 3d gaussian, compact, tracking  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: high-fidelity, body, face, motion, deformation, ar, tracking, geometry, 3d gaussian, neural rendering, human, avatar  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: face, lightweight, gaussian splatting, ar, localization, outdoor, lighting, human  

### Scene Understanding

*Showing the latest 50 out of 329 papers*

- **[Tackling View-Dependent Semantics in 3D Language Gaussian Splatting](https://arxiv.org/abs/2505.24746v1)**  
  Authors: Jiazhong Cen, Xudong Zhou, Jiemin Fang, Changsong Wen, Lingxi Xie, Xiaopeng Zhang, Wei Shen, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24746v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SJTU-DeepVisionLab/LaGa?style=social)](https://github.com/SJTU-DeepVisionLab/LaGa)  
  Keywords: understanding, gaussian splatting, semantic, ar, 3d gaussian  
- **[GARLIC: GAussian Representation LearnIng for spaCe partitioning](https://arxiv.org/abs/2505.24608v1)**  
  Authors: Panagiotis Rigas, Panagiotis Drivas, Charalambos Tzamos, Ioannis Chamodrakas, George Ioannakis, Leonidas J. Guibas, Ioannis Z. Emiris  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24608v1.pdf)  
  Keywords: efficient, fast, gaussian splatting, ar, semantic  
- **[SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images](https://arxiv.org/abs/2505.23044v1)**  
  Authors: Yu Sheng, Jiajun Deng, Xinran Zhang, Yu Zhang, Bei Hua, Yanyong Zhang, Jianmin Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23044v1.pdf)  
  Keywords: efficient, head, semantic, ar, 3d reconstruction, 3d gaussian, compact  
- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: high-fidelity, slam, motion, efficient, dynamic, mapping, gaussian splatting, semantic, localization, ar, 3d gaussian, tracking  
- **[OmniIndoor3D: Comprehensive Indoor 3D Reconstruction](https://arxiv.org/abs/2505.20610v1)**  
  Authors: Xiaobao Wei, Xiaoan Zhang, Hao Wang, Qingpo Wuwu, Ming Lu, Wenzhao Zheng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20610v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ucwxb.github.io/OmniIndoor3D/)  
  Keywords: face, lightweight, understanding, ar, 3d reconstruction, geometry, 3d gaussian  
- **[CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting](https://arxiv.org/abs/2505.20469v1)**  
  Authors: Lei Tian, Xiaomin Li, Liqian Ma, Hefei Huang, Zirui Zheng, Hao Yin, Taiqing Li, Huchuan Lu, Xu Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://epsilontl.github.io/CCL-LGS/.)  
  Keywords: understanding, gaussian splatting, semantic, 3d reconstruction, ar, robotics, 3d gaussian, compact, autonomous driving  
- **[ADD-SLAM: Adaptive Dynamic Dense SLAM with Gaussian Splatting](https://arxiv.org/abs/2505.19420v1)**  
  Authors: Wenhua Wu, Chenpeng Su, Siting Zhu, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19420v1.pdf)  
  Keywords: slam, nerf, dynamic, mapping, gaussian splatting, semantic, segmentation, recognition, localization, ar, 3d gaussian, tracking  
- **[FHGS: Feature-Homogenized Gaussian Splatting](https://arxiv.org/abs/2505.19154v1)**  
  Authors: Q. G. Duan, Benyun Zhao, Mingqiao Han Yijun Huang, Ben M. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19154v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fhgs.cuastro.org/.)  
  Keywords: efficient, mapping, understanding, gaussian splatting, semantic, ar, 3d gaussian, real-time rendering, efficient rendering  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: high-fidelity, efficient, understanding, gaussian splatting, semantic, 3d reconstruction, outdoor, survey, segmentation, 3d gaussian, neural rendering, ar  
- **[Scan, Materialize, Simulate: A Generalizable Framework for Physically Grounded Robot Planning](https://arxiv.org/abs/2505.14938v1)**  
  Authors: Amine Elhafsi, Daniel Morton, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.14938v1.pdf)  
  Keywords: dynamic, understanding, gaussian splatting, semantic, segmentation, ar, 3d gaussian  



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