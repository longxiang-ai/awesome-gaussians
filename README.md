# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-06-05 00:55:49

## Categories

- [3DGS Surveys](#3dgs-surveys) (35 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (533 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1861 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (626 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (700 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (132 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (606 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (108 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (717 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (299 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (41 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (206 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (280 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (333 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, semantic, segmentation, outdoor, survey, understanding, neural rendering, 3d reconstruction, efficient, ar  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, slam, localization, nerf, semantic, segmentation, survey, mapping, efficient, ar  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: 3d gaussian, motion, body, gaussian splatting, dynamic, ar, survey, understanding, 4d  
- **[A Survey of 3D Reconstruction with Event Cameras](https://arxiv.org/abs/2505.08438v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v2.pdf)  
  Keywords: 3d gaussian, motion, gaussian splatting, robotics, autonomous driving, nerf, dynamic, ar, survey, illumination, neural rendering, 3d reconstruction, geometry  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: gaussian splatting, fast, survey, 3d reconstruction, efficient, ar  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: 3d gaussian, autonomous driving, robotics, nerf, semantic, survey, ar  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d gaussian, lighting, survey, 3d reconstruction, ar  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: 3d gaussian, sparse view, gaussian splatting, nerf, face, outdoor, ar, survey, understanding, 3d reconstruction, geometry  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: 3d gaussian, gaussian splatting, robotics, semantic, lighting, segmentation, survey, ar  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v3)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v3.pdf)  
  Keywords: 3d gaussian, gaussian splatting, dynamic, fast, lighting, ar, survey, 3d reconstruction, motion  

### Acceleration

*Showing the latest 50 out of 533 papers*

- **[GSCodec Studio: A Modular Framework for Gaussian Splat Compression](https://arxiv.org/abs/2506.01822v1)**  
  Authors: Sicheng Li, Chengzhen Wu, Hao Li, Xiang Gao, Yiyi Liao, Lu Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01822v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JasonLSC/GSCodec_Studio?style=social)](https://github.com/JasonLSC/GSCodec_Studio)  
  Keywords: 3d gaussian, compression, compact, gaussian splatting, dynamic, ar, real-time rendering, 4d  
- **[CountingFruit: Real-Time 3D Fruit Counting with Language-Guided Semantic Gaussian Splatting](https://arxiv.org/abs/2506.01109v1)**  
  Authors: Fengze Li, Yangle Liu, Jieming Ma, Hai-Ning Liang, Yaochun Shen, Huangxiang Li, Zhijing Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01109v1.pdf)  
  Keywords: compact, gaussian splatting, efficient rendering, semantic, segmentation, neural rendering, 3d reconstruction, efficient, ar  
- **[PromptVFX: Text-Driven Fields for Open-World 3D Gaussian Animation](https://arxiv.org/abs/2506.01091v1)**  
  Authors: Mert Kiray, Paul Uhlenbruck, Nassir Navab, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01091v1.pdf)  
  Keywords: 3d gaussian, head, animation, fast, ar, vr, 4d  
- **[3D Gaussian Splat Vulnerabilities](https://arxiv.org/abs/2506.00280v1)**  
  Authors: Matthew Hull, Haoyang Yang, Pratham Mehta, Mansi Phute, Aeree Cho, Haoran Wang, Matthew Lau, Wenke Lee, Willian T. Lunardi, Martin Andreoni, Polo Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00280v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, ar  
- **[Adaptive Voxelization for Transform coding of 3D Gaussian splatting data](https://arxiv.org/abs/2506.00271v1)**  
  Authors: Chenjunjie Wang, Shashank N. Sridhara, Eduardo Pavez, Antonio Ortega, Cheng Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00271v1.pdf)  
  Keywords: 3d gaussian, compression, gaussian splatting, fast, efficient, ar  
- **[TC-GS: A Faster Gaussian Splatting Module Utilizing Tensor Cores](https://arxiv.org/abs/2505.24796v1)**  
  Authors: Zimu Liao, Jifeng Ding, Rong Fu, Siwei Cui, Ruixuan Gong, Li Wang, Boni Hu, Yi Wang, Hengjie Li, XIngcheng Zhang, Hui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TensorCore3DGS/3DGSTensorCore?style=social)](https://github.com/TensorCore3DGS/3DGSTensorCore)  
  Keywords: 3d gaussian, compression, gaussian splatting, acceleration, fast, mapping  
- **[GARLIC: GAussian Representation LearnIng for spaCe partitioning](https://arxiv.org/abs/2505.24608v1)**  
  Authors: Panagiotis Rigas, Panagiotis Drivas, Charalambos Tzamos, Ioannis Chamodrakas, George Ioannakis, Leonidas J. Guibas, Ioannis Z. Emiris  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24608v1.pdf)  
  Keywords: gaussian splatting, fast, semantic, efficient, ar  
- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: 3d gaussian, head, gaussian splatting, nerf, dynamic, efficient rendering, outdoor, real-time rendering, efficient, ar  
- **[3DGS Compression with Sparsity-guided Hierarchical Transform Coding](https://arxiv.org/abs/2505.22908v1)**  
  Authors: Hao Xu, Xiaolin Wu, Xi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22908v1.pdf)  
  Keywords: 3d gaussian, compression, head, gaussian splatting, fast, lightweight, ar  
- **[STDR: Spatio-Temporal Decoupling for Real-Time Dynamic Scene Rendering](https://arxiv.org/abs/2505.22400v1)**  
  Authors: Zehao Li, Hao Jiang, Yujun Cai, Jianing Chen, Baolong Bi, Shuqin Gao, Honglong Zhao, Yiwei Wang, Tianlu Mao, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22400v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, dynamic, deformation, ar, real-time rendering, motion  

### Applications

*Showing the latest 50 out of 1861 papers*

- **[LEG-SLAM: Real-Time Language-Enhanced Gaussian Splatting for SLAM](https://arxiv.org/abs/2506.03073v1)**  
  Authors: Roman Titkov, Egor Zubkov, Dmitry Yudin, Jaafar Mahmoud, Malik Mohrat, Gennady Sidorov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03073v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://titrom025.github.io/LEG-SLAM/)  
  Keywords: 3d gaussian, gaussian splatting, slam, localization, robotics, semantic, ar, mapping, motion  
- **[Large Processor Chip Model](https://arxiv.org/abs/2506.02929v1)**  
  Authors: Kaiyan Chang, Mingzhi Chen, Yunji Chen, Zhirong Chen, Dongrui Fan, Junfeng Gong, Nan Guo, Yinhe Han, Qinfen Hao, Shuo Hou, Xuan Huang, Pengwei Jin, Changxin Ke, Cangyuan Li, Guangli Li, Huawei Li, Kuan Li, Naipeng Li, Shengwen Liang, Cheng Liu, Hongwei Liu, Jiahua Liu, Junliang Lv, Jianan Mu, Jin Qin, Bin Sun, Chenxi Wang, Duo Wang, Mingjun Wang, Ying Wang, Chenggang Wu, Peiyang Wu, Teng Wu, Xiao Xiao, Mengyao Xie, Chenwei Xiong, Ruiyuan Xu, Mingyu Yan, Xiaochun Ye, Kuai Yu, Rui Zhang, Shuoming Zhang, Jiacheng Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02929v1.pdf)  
  Keywords: 3d gaussian, human, gaussian splatting, ar  
- **[Voyager: Real-Time Splatting City-Scale 3D Gaussians on Your Phone](https://arxiv.org/abs/2506.02774v2)**  
  Authors: Zheng Liu, He Zhu, Xinyang Li, Yirun Wang, Yujiao Shi, Wei Li, Jingwen Leng, Minyi Guo, Yu Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02774v2.pdf)  
  Keywords: 3d gaussian, motion, gaussian splatting, ar  
- **[RobustSplat: Decoupling Densification and Dynamics for Transient-Free 3DGS](https://arxiv.org/abs/2506.02751v1)**  
  Authors: Chuanyu Fu, Yuqi Zhang, Kunbin Yao, Guanying Chen, Yuan Xiong, Chuan Huang, Shuguang Cui, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02751v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fcyycf.github.io/RobustSplat/.)  
  Keywords: 3d gaussian, gaussian splatting, dynamic, semantic, ar  
- **[VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians](https://arxiv.org/abs/2506.02741v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02741v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/VTGaussian-SLAM-Project)  
  Keywords: 3d gaussian, slam, localization, tracking, ar, mapping, efficient, large scene, geometry  
- **[EyeNavGS: A 6-DoF Navigation Dataset and Record-n-Replay Software for Real-World 3DGS Scenes in VR](https://arxiv.org/abs/2506.02380v1)**  
  Authors: Zihao Ding, Cheng-Tse Lee, Mufeng Zhu, Tao Guan, Yuan-Chun Sun, Cheng-Hsin Hsu, Yao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02380v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://symmru.github.io/EyeNavGS/.)  
  Keywords: 3d gaussian, head, gaussian splatting, vr, ar  
- **[GSCodec Studio: A Modular Framework for Gaussian Splat Compression](https://arxiv.org/abs/2506.01822v1)**  
  Authors: Sicheng Li, Chengzhen Wu, Hao Li, Xiang Gao, Yiyi Liao, Lu Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01822v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JasonLSC/GSCodec_Studio?style=social)](https://github.com/JasonLSC/GSCodec_Studio)  
  Keywords: 3d gaussian, compression, compact, gaussian splatting, dynamic, ar, real-time rendering, 4d  
- **[WorldExplorer: Towards Generating Fully Navigable 3D Scenes](https://arxiv.org/abs/2506.01799v1)**  
  Authors: Manuel-Andreas Schneider, Lukas Höllein, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01799v1.pdf)  
  Keywords: 3d gaussian, motion, gaussian splatting, ar  
- **[WoMAP: World Models For Embodied Open-Vocabulary Object Localization](https://arxiv.org/abs/2506.01600v1)**  
  Authors: Tenny Yin, Zhiting Mei, Tao Sun, Lihan Zha, Emily Zhou, Jeremy Bao, Miyu Yamane, Ola Shorinwa, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01600v1.pdf)  
  Keywords: gaussian splatting, localization, dynamic, efficient, ar  
- **[RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes](https://arxiv.org/abs/2506.01379v1)**  
  Authors: Pou-Chun Kung, Skanda Harisha, Ram Vasudevan, Aline Eid, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01379v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/radarsplat.)  
  Keywords: autonomous driving, gaussian splatting, reflection, high-fidelity, 3d reconstruction, ar  

### Avatar Generation

*Showing the latest 50 out of 626 papers*

- **[Large Processor Chip Model](https://arxiv.org/abs/2506.02929v1)**  
  Authors: Kaiyan Chang, Mingzhi Chen, Yunji Chen, Zhirong Chen, Dongrui Fan, Junfeng Gong, Nan Guo, Yinhe Han, Qinfen Hao, Shuo Hou, Xuan Huang, Pengwei Jin, Changxin Ke, Cangyuan Li, Guangli Li, Huawei Li, Kuan Li, Naipeng Li, Shengwen Liang, Cheng Liu, Hongwei Liu, Jiahua Liu, Junliang Lv, Jianan Mu, Jin Qin, Bin Sun, Chenxi Wang, Duo Wang, Mingjun Wang, Ying Wang, Chenggang Wu, Peiyang Wu, Teng Wu, Xiao Xiao, Mengyao Xie, Chenwei Xiong, Ruiyuan Xu, Mingyu Yan, Xiaochun Ye, Kuai Yu, Rui Zhang, Shuoming Zhang, Jiacheng Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02929v1.pdf)  
  Keywords: 3d gaussian, human, gaussian splatting, ar  
- **[EyeNavGS: A 6-DoF Navigation Dataset and Record-n-Replay Software for Real-World 3DGS Scenes in VR](https://arxiv.org/abs/2506.02380v1)**  
  Authors: Zihao Ding, Cheng-Tse Lee, Mufeng Zhu, Tao Guan, Yuan-Chun Sun, Cheng-Hsin Hsu, Yao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02380v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://symmru.github.io/EyeNavGS/.)  
  Keywords: 3d gaussian, head, gaussian splatting, vr, ar  
- **[PromptVFX: Text-Driven Fields for Open-World 3D Gaussian Animation](https://arxiv.org/abs/2506.01091v1)**  
  Authors: Mert Kiray, Paul Uhlenbruck, Nassir Navab, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01091v1.pdf)  
  Keywords: 3d gaussian, head, animation, fast, ar, vr, 4d  
- **[Globally Consistent RGB-D SLAM with 2D Gaussian Splatting](https://arxiv.org/abs/2506.00970v1)**  
  Authors: Xingguang Zhong, Yue Pan, Liren Jin, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00970v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, slam, localization, face, ar, mapping, high-fidelity, 3d reconstruction, efficient, tracking  
- **[AdaHuman: Animatable Detailed 3D Human Generation with Compositional Multiview Diffusion](https://arxiv.org/abs/2505.24877v1)**  
  Authors: Yangyi Huang, Ye Yuan, Xueting Li, Jan Kautz, Umar Iqbal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24877v1.pdf)  
  Keywords: 3d gaussian, body, animation, human, ar, high-fidelity, avatar, motion  
- **[Radiant Triangle Soup with Soft Connectivity Forces for 3D Reconstruction and Novel View Synthesis](https://arxiv.org/abs/2505.23642v1)**  
  Authors: Nathaniel Burgdorfer, Philippos Mordohai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23642v1.pdf)  
  Keywords: 3d reconstruction, face, geometry, ar  
- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: 3d gaussian, head, gaussian splatting, nerf, dynamic, efficient rendering, outdoor, real-time rendering, efficient, ar  
- **[SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images](https://arxiv.org/abs/2505.23044v1)**  
  Authors: Yu Sheng, Jiajun Deng, Xinran Zhang, Yu Zhang, Bei Hua, Yanyong Zhang, Jianmin Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23044v1.pdf)  
  Keywords: 3d gaussian, compact, head, semantic, 3d reconstruction, efficient, ar  
- **[3DGS Compression with Sparsity-guided Hierarchical Transform Coding](https://arxiv.org/abs/2505.22908v1)**  
  Authors: Hao Xu, Xiaolin Wu, Xi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22908v1.pdf)  
  Keywords: 3d gaussian, compression, head, gaussian splatting, fast, lightweight, ar  
- **[4DTAM: Non-Rigid Tracking and Mapping via Dynamic Surface Gaussians](https://arxiv.org/abs/2505.22859v1)**  
  Authors: Hidenobu Matsuki, Gwangbin Bae, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22859v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, animation, slam, localization, dynamic, face, tracking, deformation, ar, mapping, 4d  

### Dynamic Scene

*Showing the latest 50 out of 700 papers*

- **[LEG-SLAM: Real-Time Language-Enhanced Gaussian Splatting for SLAM](https://arxiv.org/abs/2506.03073v1)**  
  Authors: Roman Titkov, Egor Zubkov, Dmitry Yudin, Jaafar Mahmoud, Malik Mohrat, Gennady Sidorov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03073v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://titrom025.github.io/LEG-SLAM/)  
  Keywords: 3d gaussian, gaussian splatting, slam, localization, robotics, semantic, ar, mapping, motion  
- **[Voyager: Real-Time Splatting City-Scale 3D Gaussians on Your Phone](https://arxiv.org/abs/2506.02774v2)**  
  Authors: Zheng Liu, He Zhu, Xinyang Li, Yirun Wang, Yujiao Shi, Wei Li, Jingwen Leng, Minyi Guo, Yu Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02774v2.pdf)  
  Keywords: 3d gaussian, motion, gaussian splatting, ar  
- **[RobustSplat: Decoupling Densification and Dynamics for Transient-Free 3DGS](https://arxiv.org/abs/2506.02751v1)**  
  Authors: Chuanyu Fu, Yuqi Zhang, Kunbin Yao, Guanying Chen, Yuan Xiong, Chuan Huang, Shuguang Cui, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02751v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fcyycf.github.io/RobustSplat/.)  
  Keywords: 3d gaussian, gaussian splatting, dynamic, semantic, ar  
- **[GSCodec Studio: A Modular Framework for Gaussian Splat Compression](https://arxiv.org/abs/2506.01822v1)**  
  Authors: Sicheng Li, Chengzhen Wu, Hao Li, Xiang Gao, Yiyi Liao, Lu Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01822v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JasonLSC/GSCodec_Studio?style=social)](https://github.com/JasonLSC/GSCodec_Studio)  
  Keywords: 3d gaussian, compression, compact, gaussian splatting, dynamic, ar, real-time rendering, 4d  
- **[WorldExplorer: Towards Generating Fully Navigable 3D Scenes](https://arxiv.org/abs/2506.01799v1)**  
  Authors: Manuel-Andreas Schneider, Lukas Höllein, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01799v1.pdf)  
  Keywords: 3d gaussian, motion, gaussian splatting, ar  
- **[WoMAP: World Models For Embodied Open-Vocabulary Object Localization](https://arxiv.org/abs/2506.01600v1)**  
  Authors: Tenny Yin, Zhiting Mei, Tao Sun, Lihan Zha, Emily Zhou, Jeremy Bao, Miyu Yamane, Ola Shorinwa, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01600v1.pdf)  
  Keywords: gaussian splatting, localization, dynamic, efficient, ar  
- **[PromptVFX: Text-Driven Fields for Open-World 3D Gaussian Animation](https://arxiv.org/abs/2506.01091v1)**  
  Authors: Mert Kiray, Paul Uhlenbruck, Nassir Navab, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01091v1.pdf)  
  Keywords: 3d gaussian, head, animation, fast, ar, vr, 4d  
- **[AdaHuman: Animatable Detailed 3D Human Generation with Compositional Multiview Diffusion](https://arxiv.org/abs/2505.24877v1)**  
  Authors: Yangyi Huang, Ye Yuan, Xueting Li, Jan Kautz, Umar Iqbal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24877v1.pdf)  
  Keywords: 3d gaussian, body, animation, human, ar, high-fidelity, avatar, motion  
- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: 3d gaussian, head, gaussian splatting, nerf, dynamic, efficient rendering, outdoor, real-time rendering, efficient, ar  
- **[4DTAM: Non-Rigid Tracking and Mapping via Dynamic Surface Gaussians](https://arxiv.org/abs/2505.22859v1)**  
  Authors: Hidenobu Matsuki, Gwangbin Bae, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22859v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, animation, slam, localization, dynamic, face, tracking, deformation, ar, mapping, 4d  

### Few-shot

*Showing the latest 50 out of 132 papers*

- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, sparse-view, nerf, ar, efficient, geometry  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, face, sparse-view, ar, motion  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: gaussian splatting, sparse-view, fast, face, ar, 3d reconstruction, motion  
- **[Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse Views by Jointly Training Hemisphere Sampled Synthetic Images](https://arxiv.org/abs/2505.19264v1)**  
  Authors: Guangan Chen, Anh Minh Truong, Hanhe Lin, Michiel Vlaminck, Wilfried Philips, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19264v1.pdf)  
  Keywords: 3d gaussian, sparse view, gaussian splatting, sparse-view, ar, motion  
- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: motion, compact, head, gaussian splatting, dynamic, sparse-view, deformation, ar, 3d reconstruction, efficient, 4d  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, robotics, sparse-view, high-fidelity, ar  
- **[X-GRM: Large Gaussian Reconstruction Model for Sparse-view X-rays to Computed Tomography](https://arxiv.org/abs/2505.15235v2)**  
  Authors: Yifan Liu, Wuyang Li, Weihao Yu, Chenxin Li, Alexandre Alahi, Max Meng, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15235v2.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/X-GRM?style=social)](https://github.com/CUHK-AIM-Group/X-GRM)  
  Keywords: sparse-view, efficient, gaussian splatting, ar  
- **[SpatialCrafter: Unleashing the Imagination of Video Diffusion Models for Scene Reconstruction from Limited Observations](https://arxiv.org/abs/2505.11992v1)**  
  Authors: Songchun Zhang, Huiyao Xu, Sitong Guo, Zhongwei Xie, Pengwei Liu, Hujun Bao, Weiwei Xu, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11992v1.pdf)  
  Keywords: 3d gaussian, sparse view, semantic, efficient, ar  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: sparse view, head, gaussian splatting, shape reconstruction, face, fast, ar, efficient, geometry  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: 3d gaussian, sparse view, gaussian splatting, shape reconstruction, sparse-view, fast, face, ar, 3d reconstruction, geometry  

### Geometry Reconstruction

*Showing the latest 50 out of 606 papers*

- **[VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians](https://arxiv.org/abs/2506.02741v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02741v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/VTGaussian-SLAM-Project)  
  Keywords: 3d gaussian, slam, localization, tracking, ar, mapping, efficient, large scene, geometry  
- **[RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes](https://arxiv.org/abs/2506.01379v1)**  
  Authors: Pou-Chun Kung, Skanda Harisha, Ram Vasudevan, Aline Eid, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01379v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/radarsplat.)  
  Keywords: autonomous driving, gaussian splatting, reflection, high-fidelity, 3d reconstruction, ar  
- **[CountingFruit: Real-Time 3D Fruit Counting with Language-Guided Semantic Gaussian Splatting](https://arxiv.org/abs/2506.01109v1)**  
  Authors: Fengze Li, Yangle Liu, Jieming Ma, Hai-Ning Liang, Yaochun Shen, Huangxiang Li, Zhijing Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01109v1.pdf)  
  Keywords: compact, gaussian splatting, efficient rendering, semantic, segmentation, neural rendering, 3d reconstruction, efficient, ar  
- **[Globally Consistent RGB-D SLAM with 2D Gaussian Splatting](https://arxiv.org/abs/2506.00970v1)**  
  Authors: Xingguang Zhong, Yue Pan, Liren Jin, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00970v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, slam, localization, face, ar, mapping, high-fidelity, 3d reconstruction, efficient, tracking  
- **[Understanding while Exploring: Semantics-driven Active Mapping](https://arxiv.org/abs/2506.00225v1)**  
  Authors: Liyan Chen, Huangying Zhan, Hairong Yin, Yi Xu, Philippos Mordohai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00225v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, semantic, ar, mapping, understanding, efficient, geometry  
- **[AnySplat: Feed-forward 3D Gaussian Splatting from Unconstrained Views](https://arxiv.org/abs/2505.23716v1)**  
  Authors: Lihan Jiang, Yucheng Mao, Linning Xu, Tao Lu, Kerui Ren, Yichen Jin, Xudong Xu, Mulin Yu, Jiangmiao Pang, Feng Zhao, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23716v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://city-super.github.io/anysplat/)  
  Keywords: 3d gaussian, geometry, gaussian splatting, neural rendering, ar  
- **[Radiant Triangle Soup with Soft Connectivity Forces for 3D Reconstruction and Novel View Synthesis](https://arxiv.org/abs/2505.23642v1)**  
  Authors: Nathaniel Burgdorfer, Philippos Mordohai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23642v1.pdf)  
  Keywords: 3d reconstruction, face, geometry, ar  
- **[SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images](https://arxiv.org/abs/2505.23044v1)**  
  Authors: Yu Sheng, Jiajun Deng, Xinran Zhang, Yu Zhang, Bei Hua, Yanyong Zhang, Jianmin Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23044v1.pdf)  
  Keywords: 3d gaussian, compact, head, semantic, 3d reconstruction, efficient, ar  
- **[Pose-free 3D Gaussian splatting via shape-ray estimation](https://arxiv.org/abs/2505.22978v1)**  
  Authors: Youngju Na, Taeyeon Kim, Jumin Lee, Kyu Beom Han, Woo Jae Kim, Sung-eui Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22978v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, efficient, geometry  
- **[4DTAM: Non-Rigid Tracking and Mapping via Dynamic Surface Gaussians](https://arxiv.org/abs/2505.22859v1)**  
  Authors: Hidenobu Matsuki, Gwangbin Bae, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22859v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, animation, slam, localization, dynamic, face, tracking, deformation, ar, mapping, 4d  

### Large Scene

*Showing the latest 50 out of 108 papers*

- **[VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians](https://arxiv.org/abs/2506.02741v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02741v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/VTGaussian-SLAM-Project)  
  Keywords: 3d gaussian, slam, localization, tracking, ar, mapping, efficient, large scene, geometry  
- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: 3d gaussian, head, gaussian splatting, nerf, dynamic, efficient rendering, outdoor, real-time rendering, efficient, ar  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: 3d gaussian, compact, gaussian splatting, ar, lightweight, real-time rendering, urban scene, efficient, geometry  
- **[HaloGS: Loose Coupling of Compact Geometry and Gaussian Splats for 3D Scenes](https://arxiv.org/abs/2505.20267v1)**  
  Authors: Changjian Jiang, Kerui Ren, Linning Xu, Jiong Chen, Jiangmiao Pang, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20267v1.pdf)  
  Keywords: compact, outdoor, lightweight, ar, 3d reconstruction, geometry  
- **[VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale Scenes](https://arxiv.org/abs/2505.18992v1)**  
  Authors: Tianchen Deng, Wenhua Wu, Junjie He, Yue Pan, Xirui Jiang, Shenghai Yuan, Danwei Wang, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18992v1.pdf) | [![GitHub](https://img.shields.io/github/stars/dtc111111/vpgs-slam?style=social)](https://github.com/dtc111111/vpgs-slam)  
  Keywords: 3d gaussian, compact, gaussian splatting, slam, outdoor, ar, mapping, tracking  
- **[SplatCo: Structure-View Collaborative Gaussian Splatting for Detail-Preserving Rendering of Large-Scale Unbounded Scenes](https://arxiv.org/abs/2505.17951v1)**  
  Authors: Haihong Xiao, Jianan Zou, Yuxin Zhou, Ying He, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17951v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SCUT-BIP-Lab/SplatCo?style=social)](https://github.com/SCUT-BIP-Lab/SplatCo)  
  Keywords: gaussian splatting, face, outdoor, high-fidelity, ar  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, semantic, segmentation, outdoor, survey, understanding, neural rendering, 3d reconstruction, efficient, ar  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: gaussian splatting, localization, face, human, lighting, outdoor, lightweight, ar  
- **[Gaussian Splatting as a Unified Representation for Autonomy in Unstructured Environments](https://arxiv.org/abs/2505.11794v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11794v1.pdf)  
  Keywords: semantic, gaussian splatting, ar, outdoor  
- **[EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes](https://arxiv.org/abs/2505.10787v1)**  
  Authors: Jianlin Guo, Haihong Xiao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10787v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, nerf, face, outdoor, ar, real-time rendering, efficient, geometry  

### Model Compression

*Showing the latest 50 out of 717 papers*

- **[VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians](https://arxiv.org/abs/2506.02741v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02741v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/VTGaussian-SLAM-Project)  
  Keywords: 3d gaussian, slam, localization, tracking, ar, mapping, efficient, large scene, geometry  
- **[GSCodec Studio: A Modular Framework for Gaussian Splat Compression](https://arxiv.org/abs/2506.01822v1)**  
  Authors: Sicheng Li, Chengzhen Wu, Hao Li, Xiang Gao, Yiyi Liao, Lu Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01822v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JasonLSC/GSCodec_Studio?style=social)](https://github.com/JasonLSC/GSCodec_Studio)  
  Keywords: 3d gaussian, compression, compact, gaussian splatting, dynamic, ar, real-time rendering, 4d  
- **[WoMAP: World Models For Embodied Open-Vocabulary Object Localization](https://arxiv.org/abs/2506.01600v1)**  
  Authors: Tenny Yin, Zhiting Mei, Tao Sun, Lihan Zha, Emily Zhou, Jeremy Bao, Miyu Yamane, Ola Shorinwa, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01600v1.pdf)  
  Keywords: gaussian splatting, localization, dynamic, efficient, ar  
- **[CountingFruit: Real-Time 3D Fruit Counting with Language-Guided Semantic Gaussian Splatting](https://arxiv.org/abs/2506.01109v1)**  
  Authors: Fengze Li, Yangle Liu, Jieming Ma, Hai-Ning Liang, Yaochun Shen, Huangxiang Li, Zhijing Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01109v1.pdf)  
  Keywords: compact, gaussian splatting, efficient rendering, semantic, segmentation, neural rendering, 3d reconstruction, efficient, ar  
- **[Globally Consistent RGB-D SLAM with 2D Gaussian Splatting](https://arxiv.org/abs/2506.00970v1)**  
  Authors: Xingguang Zhong, Yue Pan, Liren Jin, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00970v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, slam, localization, face, ar, mapping, high-fidelity, 3d reconstruction, efficient, tracking  
- **[Adaptive Voxelization for Transform coding of 3D Gaussian splatting data](https://arxiv.org/abs/2506.00271v1)**  
  Authors: Chenjunjie Wang, Shashank N. Sridhara, Eduardo Pavez, Antonio Ortega, Cheng Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00271v1.pdf)  
  Keywords: 3d gaussian, compression, gaussian splatting, fast, efficient, ar  
- **[Understanding while Exploring: Semantics-driven Active Mapping](https://arxiv.org/abs/2506.00225v1)**  
  Authors: Liyan Chen, Huangying Zhan, Hairong Yin, Yi Xu, Philippos Mordohai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00225v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, semantic, ar, mapping, understanding, efficient, geometry  
- **[TC-GS: A Faster Gaussian Splatting Module Utilizing Tensor Cores](https://arxiv.org/abs/2505.24796v1)**  
  Authors: Zimu Liao, Jifeng Ding, Rong Fu, Siwei Cui, Ruixuan Gong, Li Wang, Boni Hu, Yi Wang, Hengjie Li, XIngcheng Zhang, Hui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TensorCore3DGS/3DGSTensorCore?style=social)](https://github.com/TensorCore3DGS/3DGSTensorCore)  
  Keywords: 3d gaussian, compression, gaussian splatting, acceleration, fast, mapping  
- **[GARLIC: GAussian Representation LearnIng for spaCe partitioning](https://arxiv.org/abs/2505.24608v1)**  
  Authors: Panagiotis Rigas, Panagiotis Drivas, Charalambos Tzamos, Ioannis Chamodrakas, George Ioannakis, Leonidas J. Guibas, Ioannis Z. Emiris  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24608v1.pdf)  
  Keywords: gaussian splatting, fast, semantic, efficient, ar  
- **[3DGEER: Exact and Efficient Volumetric Rendering with 3D Gaussians](https://arxiv.org/abs/2505.24053v1)**  
  Authors: Zixun Huang, Cho-Ying Wu, Yuliang Guo, Xinyu Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24053v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, neural rendering, efficient, ar  

### Quality Enhancement

*Showing the latest 50 out of 299 papers*

- **[RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes](https://arxiv.org/abs/2506.01379v1)**  
  Authors: Pou-Chun Kung, Skanda Harisha, Ram Vasudevan, Aline Eid, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01379v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/radarsplat.)  
  Keywords: autonomous driving, gaussian splatting, reflection, high-fidelity, 3d reconstruction, ar  
- **[Globally Consistent RGB-D SLAM with 2D Gaussian Splatting](https://arxiv.org/abs/2506.00970v1)**  
  Authors: Xingguang Zhong, Yue Pan, Liren Jin, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00970v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, slam, localization, face, ar, mapping, high-fidelity, 3d reconstruction, efficient, tracking  
- **[AdaHuman: Animatable Detailed 3D Human Generation with Compositional Multiview Diffusion](https://arxiv.org/abs/2505.24877v1)**  
  Authors: Yangyi Huang, Ye Yuan, Xueting Li, Jan Kautz, Umar Iqbal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24877v1.pdf)  
  Keywords: 3d gaussian, body, animation, human, ar, high-fidelity, avatar, motion  
- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: 3d gaussian, gaussian splatting, slam, localization, dynamic, semantic, tracking, ar, mapping, high-fidelity, efficient, motion  
- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: 3d gaussian, ray tracing, gaussian splatting, face, neural rendering, human, lighting, relightable, shadow, ar, illumination, high-fidelity, relighting, geometry  
- **[OB3D: A New Dataset for Benchmarking Omnidirectional 3D Reconstruction Using Blender](https://arxiv.org/abs/2505.20126v1)**  
  Authors: Shintaro Ito, Natsuki Takama, Toshiki Watanabe, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20126v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, nerf, high-fidelity, 3d reconstruction, ar  
- **[SplatCo: Structure-View Collaborative Gaussian Splatting for Detail-Preserving Rendering of Large-Scale Unbounded Scenes](https://arxiv.org/abs/2505.17951v1)**  
  Authors: Haihong Xiao, Jianan Zou, Yuxin Zhou, Ying He, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17951v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SCUT-BIP-Lab/SplatCo?style=social)](https://github.com/SCUT-BIP-Lab/SplatCo)  
  Keywords: gaussian splatting, face, outdoor, high-fidelity, ar  
- **[CGS-GAN: 3D Consistent Gaussian Splatting GANs for High Resolution Human Head Synthesis](https://arxiv.org/abs/2505.17590v1)**  
  Authors: Florian Barthel, Wieland Morgenstern, Paul Hinzer, Anna Hilsmann, Peter Eisert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17590v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fraunhoferhhi.github.io/cgs-gan/)  
  Keywords: 3d gaussian, head, gaussian splatting, efficient rendering, human, high quality, efficient, ar  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, high-fidelity, semantic, segmentation, outdoor, survey, understanding, neural rendering, 3d reconstruction, efficient, ar  
- **[Render-FM: A Foundation Model for Real-time Photorealistic Volumetric Rendering](https://arxiv.org/abs/2505.17338v1)**  
  Authors: Zhongpai Gao, Meng Zheng, Benjamin Planche, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17338v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/renderfm/.)  
  Keywords: gaussian splatting, neural rendering, high-fidelity, efficient, ar, medical  

### Ray Tracing

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: 3d gaussian, ray tracing, gaussian splatting, face, neural rendering, human, lighting, relightable, shadow, ar, illumination, high-fidelity, relighting, geometry  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: ray tracing, gaussian splatting, fast, human, lighting, relightable, shadow, ar, avatar, relighting, geometry  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: 3d gaussian, ray tracing, gaussian splatting, acceleration, efficient rendering, lighting, efficient, relighting, ar  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: 3d gaussian, compact, gaussian splatting, acceleration, animation, dynamic, efficient, ray marching, ar  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: 3d gaussian, ray tracing, gaussian splatting, face, lighting, real-time rendering, global illumination, illumination, efficient, ar  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: 3d gaussian, dynamic, fast, face, lighting, light transport, real-time rendering, global illumination, illumination  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: 3d gaussian, ray tracing, gaussian splatting, fast, reflection, shadow, neural rendering, ar  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: ray tracing, dynamic, face, lighting, relightable, tracking, ar, real-time rendering, 4d, efficient, geometry  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: ray tracing, gaussian splatting, face, reflection, lighting, shadow  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, ray tracing, gaussian splatting, survey, ar  

### Relighting

*Showing the latest 50 out of 206 papers*

- **[RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes](https://arxiv.org/abs/2506.01379v1)**  
  Authors: Pou-Chun Kung, Skanda Harisha, Ram Vasudevan, Aline Eid, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01379v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/radarsplat.)  
  Keywords: autonomous driving, gaussian splatting, reflection, high-fidelity, 3d reconstruction, ar  
- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: 3d gaussian, ray tracing, gaussian splatting, face, neural rendering, human, lighting, relightable, shadow, ar, illumination, high-fidelity, relighting, geometry  
- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: 3d gaussian, lighting, shadow, mapping, illumination, efficient, ar  
- **[WeatherEdit: Controllable Weather Editing with 4D Gaussian Field](https://arxiv.org/abs/2505.20471v1)**  
  Authors: Chenghao Qian, Wenjing Li, Yuhu Guo, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/w-edit)  
  Keywords: autonomous driving, dynamic, lighting, ar, 4d  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: gaussian splatting, localization, face, human, lighting, outdoor, lightweight, ar  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, lighting, ar, high-fidelity, 3d reconstruction, motion  
- **[3D Gaussian Adaptive Reconstruction for Fourier Light-Field Microscopy](https://arxiv.org/abs/2505.12875v1)**  
  Authors: Chenyu Xu, Zhouyu Jin, Chengkang Shen, Hao Zhu, Zhan Ma, Bo Xiong, You Zhou, Xun Cao, Ning Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12875v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, nerf, lighting, ar  
- **[A Survey of 3D Reconstruction with Event Cameras](https://arxiv.org/abs/2505.08438v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v2.pdf)  
  Keywords: 3d gaussian, motion, gaussian splatting, robotics, autonomous driving, nerf, dynamic, ar, survey, illumination, neural rendering, 3d reconstruction, geometry  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d gaussian, lighting, survey, 3d reconstruction, ar  
- **[TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians](https://arxiv.org/abs/2504.18768v2)**  
  Authors: Letian Huang, Dongwei Ye, Jialin Dan, Chengzhi Tao, Huiwen Liu, Kun Zhou, Bo Ren, Yuanqi Li, Yanwen Guo, Jie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18768v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, fast, reflection, efficient, ar  

### SLAM

*Showing the latest 50 out of 280 papers*

- **[LEG-SLAM: Real-Time Language-Enhanced Gaussian Splatting for SLAM](https://arxiv.org/abs/2506.03073v1)**  
  Authors: Roman Titkov, Egor Zubkov, Dmitry Yudin, Jaafar Mahmoud, Malik Mohrat, Gennady Sidorov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03073v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://titrom025.github.io/LEG-SLAM/)  
  Keywords: 3d gaussian, gaussian splatting, slam, localization, robotics, semantic, ar, mapping, motion  
- **[VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians](https://arxiv.org/abs/2506.02741v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02741v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/VTGaussian-SLAM-Project)  
  Keywords: 3d gaussian, slam, localization, tracking, ar, mapping, efficient, large scene, geometry  
- **[WoMAP: World Models For Embodied Open-Vocabulary Object Localization](https://arxiv.org/abs/2506.01600v1)**  
  Authors: Tenny Yin, Zhiting Mei, Tao Sun, Lihan Zha, Emily Zhou, Jeremy Bao, Miyu Yamane, Ola Shorinwa, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01600v1.pdf)  
  Keywords: gaussian splatting, localization, dynamic, efficient, ar  
- **[Globally Consistent RGB-D SLAM with 2D Gaussian Splatting](https://arxiv.org/abs/2506.00970v1)**  
  Authors: Xingguang Zhong, Yue Pan, Liren Jin, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00970v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, slam, localization, face, ar, mapping, high-fidelity, 3d reconstruction, efficient, tracking  
- **[Understanding while Exploring: Semantics-driven Active Mapping](https://arxiv.org/abs/2506.00225v1)**  
  Authors: Liyan Chen, Huangying Zhan, Hairong Yin, Yi Xu, Philippos Mordohai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00225v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, semantic, ar, mapping, understanding, efficient, geometry  
- **[TC-GS: A Faster Gaussian Splatting Module Utilizing Tensor Cores](https://arxiv.org/abs/2505.24796v1)**  
  Authors: Zimu Liao, Jifeng Ding, Rong Fu, Siwei Cui, Ruixuan Gong, Li Wang, Boni Hu, Yi Wang, Hengjie Li, XIngcheng Zhang, Hui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TensorCore3DGS/3DGSTensorCore?style=social)](https://github.com/TensorCore3DGS/3DGSTensorCore)  
  Keywords: 3d gaussian, compression, gaussian splatting, acceleration, fast, mapping  
- **[4DTAM: Non-Rigid Tracking and Mapping via Dynamic Surface Gaussians](https://arxiv.org/abs/2505.22859v1)**  
  Authors: Hidenobu Matsuki, Gwangbin Bae, Andrew J. Davison  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22859v1.pdf)  
  Keywords: 3d gaussian, motion, geometry, animation, slam, localization, dynamic, face, tracking, deformation, ar, mapping, 4d  
- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: 3d gaussian, gaussian splatting, slam, localization, dynamic, semantic, tracking, ar, mapping, high-fidelity, efficient, motion  
- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: 3d gaussian, lighting, shadow, mapping, illumination, efficient, ar  
- **[ProBA: Probabilistic Bundle Adjustment with the Bhattacharyya Coefficient](https://arxiv.org/abs/2505.20858v1)**  
  Authors: Jason Chui, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20858v1.pdf)  
  Keywords: 3d gaussian, efficient, ar, slam  

### Scene Understanding

*Showing the latest 50 out of 333 papers*

- **[LEG-SLAM: Real-Time Language-Enhanced Gaussian Splatting for SLAM](https://arxiv.org/abs/2506.03073v1)**  
  Authors: Roman Titkov, Egor Zubkov, Dmitry Yudin, Jaafar Mahmoud, Malik Mohrat, Gennady Sidorov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03073v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://titrom025.github.io/LEG-SLAM/)  
  Keywords: 3d gaussian, gaussian splatting, slam, localization, robotics, semantic, ar, mapping, motion  
- **[RobustSplat: Decoupling Densification and Dynamics for Transient-Free 3DGS](https://arxiv.org/abs/2506.02751v1)**  
  Authors: Chuanyu Fu, Yuqi Zhang, Kunbin Yao, Guanying Chen, Yuan Xiong, Chuan Huang, Shuguang Cui, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02751v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fcyycf.github.io/RobustSplat/.)  
  Keywords: 3d gaussian, gaussian splatting, dynamic, semantic, ar  
- **[CountingFruit: Real-Time 3D Fruit Counting with Language-Guided Semantic Gaussian Splatting](https://arxiv.org/abs/2506.01109v1)**  
  Authors: Fengze Li, Yangle Liu, Jieming Ma, Hai-Ning Liang, Yaochun Shen, Huangxiang Li, Zhijing Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01109v1.pdf)  
  Keywords: compact, gaussian splatting, efficient rendering, semantic, segmentation, neural rendering, 3d reconstruction, efficient, ar  
- **[Understanding while Exploring: Semantics-driven Active Mapping](https://arxiv.org/abs/2506.00225v1)**  
  Authors: Liyan Chen, Huangying Zhan, Hairong Yin, Yi Xu, Philippos Mordohai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00225v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, semantic, ar, mapping, understanding, efficient, geometry  
- **[Tackling View-Dependent Semantics in 3D Language Gaussian Splatting](https://arxiv.org/abs/2505.24746v1)**  
  Authors: Jiazhong Cen, Xudong Zhou, Jiemin Fang, Changsong Wen, Lingxi Xie, Xiaopeng Zhang, Wei Shen, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24746v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SJTU-DeepVisionLab/LaGa?style=social)](https://github.com/SJTU-DeepVisionLab/LaGa)  
  Keywords: 3d gaussian, gaussian splatting, semantic, understanding, ar  
- **[GARLIC: GAussian Representation LearnIng for spaCe partitioning](https://arxiv.org/abs/2505.24608v1)**  
  Authors: Panagiotis Rigas, Panagiotis Drivas, Charalambos Tzamos, Ioannis Chamodrakas, George Ioannakis, Leonidas J. Guibas, Ioannis Z. Emiris  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24608v1.pdf)  
  Keywords: gaussian splatting, fast, semantic, efficient, ar  
- **[SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images](https://arxiv.org/abs/2505.23044v1)**  
  Authors: Yu Sheng, Jiajun Deng, Xinran Zhang, Yu Zhang, Bei Hua, Yanyong Zhang, Jianmin Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23044v1.pdf)  
  Keywords: 3d gaussian, compact, head, semantic, 3d reconstruction, efficient, ar  
- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: 3d gaussian, gaussian splatting, slam, localization, dynamic, semantic, tracking, ar, mapping, high-fidelity, efficient, motion  
- **[OmniIndoor3D: Comprehensive Indoor 3D Reconstruction](https://arxiv.org/abs/2505.20610v1)**  
  Authors: Xiaobao Wei, Xiaoan Zhang, Hao Wang, Qingpo Wuwu, Ming Lu, Wenzhao Zheng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20610v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ucwxb.github.io/OmniIndoor3D/)  
  Keywords: 3d gaussian, face, ar, lightweight, understanding, 3d reconstruction, geometry  
- **[CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting](https://arxiv.org/abs/2505.20469v1)**  
  Authors: Lei Tian, Xiaomin Li, Liqian Ma, Hefei Huang, Zirui Zheng, Hao Yin, Taiqing Li, Huchuan Lu, Xu Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://epsilontl.github.io/CCL-LGS/.)  
  Keywords: 3d gaussian, compact, gaussian splatting, robotics, autonomous driving, semantic, understanding, 3d reconstruction, ar  



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