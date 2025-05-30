# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-05-30 00:55:11

## Categories

- [3DGS Surveys](#3dgs-surveys) (35 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (524 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1829 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (616 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (689 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (132 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (595 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (106 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (701 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (295 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (41 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (204 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (273 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (327 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: high-fidelity, 3d reconstruction, 3d gaussian, semantic, gaussian splatting, ar, outdoor, segmentation, neural rendering, understanding, efficient, survey  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, gaussian splatting, segmentation, localization, mapping, slam, nerf, efficient, survey  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: 3d gaussian, body, ar, gaussian splatting, dynamic, understanding, motion, 4d, survey  
- **[A Survey of 3D Reconstruction with Event Cameras: From Event-based Geometry to Neural 3D Rendering](https://arxiv.org/abs/2505.08438v1)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, ar, gaussian splatting, neural rendering, dynamic, geometry, motion, survey  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, fast, efficient, survey  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: semantic, 3d gaussian, robotics, ar, autonomous driving, nerf, survey  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, ar, lighting, survey  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: sparse view, 3d reconstruction, 3d gaussian, ar, gaussian splatting, understanding, outdoor, geometry, nerf, face, survey  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: semantic, 3d gaussian, robotics, gaussian splatting, ar, segmentation, lighting, survey  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, ar, gaussian splatting, fast, lighting, dynamic, motion, survey  

### Acceleration

*Showing the latest 50 out of 524 papers*

- **[STDR: Spatio-Temporal Decoupling for Real-Time Dynamic Scene Rendering](https://arxiv.org/abs/2505.22400v1)**  
  Authors: Zehao Li, Hao Jiang, Yujun Cai, Jianing Chen, Baolong Bi, Shuqin Gao, Honglong Zhao, Yiwei Wang, Tianlu Mao, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22400v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, gaussian splatting, ar, dynamic, motion, deformation  
- **[3D-UIR: 3D Gaussian for Underwater 3D Scene Reconstruction via Physics Based Appearance-Medium Decoupling](https://arxiv.org/abs/2505.21238v2)**  
  Authors: Jieyu Yuan, Yujun Li, Yuanlin Zhang, Chunle Guo, Xiongxin Tang, Ruixing Wang, Chongyi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21238v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bilityniu.github.io/3D-UIR.)  
  Keywords: 3d gaussian, body, real-time rendering, gaussian splatting, ar  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: 3d gaussian, compact, real-time rendering, gaussian splatting, lightweight, urban scene, ar, geometry, efficient  
- **[Weather-Magician: Reconstruction and Rendering Framework for 4D Weather Synthesis In Real Time](https://arxiv.org/abs/2505.19919v1)**  
  Authors: Chen Sang, Yeqiang Qian, Jiale Zhang, Chunxiang Wang, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19919v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, ar, dynamic, efficient, vr, 4d  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: 3d reconstruction, ar, gaussian splatting, sparse-view, fast, motion, face  
- **[K-Buffers: A Plug-in Method for Enhancing Neural Fields with Multiple Buffers](https://arxiv.org/abs/2505.19564v1)**  
  Authors: Haofan Ren, Zunjie Zhu, Xiang Chen, Ming Lu, Rongfeng Lu, Chenggang Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19564v1.pdf)  
  Keywords: acceleration, 3d gaussian, ar, gaussian splatting  
- **[Triangle Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2505.19175v1)**  
  Authors: Jan Held, Renaud Vandeghen, Adrien Deliege, Abdullah Hamdi, Silvio Giancola, Anthony Cioppa, Andrea Vedaldi, Bernard Ghanem, Andrea Tagliasacchi, Marc Van Droogenbroeck  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19175v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://trianglesplatting.github.io/)  
  Keywords: 3d gaussian, ar, gaussian splatting, fast, nerf, efficient  
- **[FHGS: Feature-Homogenized Gaussian Splatting](https://arxiv.org/abs/2505.19154v1)**  
  Authors: Q. G. Duan, Benyun Zhao, Mingqiao Han Yijun Huang, Ben M. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19154v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fhgs.cuastro.org/.)  
  Keywords: semantic, 3d gaussian, real-time rendering, gaussian splatting, ar, efficient rendering, mapping, understanding, efficient  
- **[Veta-GS: View-dependent deformable 3D Gaussian Splatting for thermal infrared Novel-view Synthesis](https://arxiv.org/abs/2505.19138v1)**  
  Authors: Myeongseok Nam, Wongi Park, Minsol Kim, Hyejin Hur, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19138v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, gaussian splatting, ar, deformation  
- **[Efficient Differentiable Hardware Rasterization for 3D Gaussian Splatting](https://arxiv.org/abs/2505.18764v1)**  
  Authors: Yitian Yuan, Qianyue He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18764v1.pdf)  
  Keywords: head, 3d gaussian, ar, gaussian splatting, acceleration, fast, nerf, efficient  

### Applications

*Showing the latest 50 out of 1829 papers*

- **[STDR: Spatio-Temporal Decoupling for Real-Time Dynamic Scene Rendering](https://arxiv.org/abs/2505.22400v1)**  
  Authors: Zehao Li, Hao Jiang, Yujun Cai, Jianing Chen, Baolong Bi, Shuqin Gao, Honglong Zhao, Yiwei Wang, Tianlu Mao, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22400v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, gaussian splatting, ar, dynamic, motion, deformation  
- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: high-fidelity, 3d gaussian, semantic, tracking, gaussian splatting, ar, localization, mapping, slam, dynamic, efficient, motion  
- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, sparse-view, geometry, nerf, efficient  
- **[Hyperspectral Gaussian Splatting](https://arxiv.org/abs/2505.21890v1)**  
  Authors: Sunil Kumar Narayanan, Lingjun Zhao, Lu Gan, Yongsheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21890v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, ar, gaussian splatting, nerf, face  
- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, illumination, gaussian splatting, ar, relightable, lighting, shadow, neural rendering, human, ray tracing, geometry, relighting, face  
- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: 3d gaussian, illumination, ar, lighting, shadow, mapping, efficient  
- **[Empowering Vector Graphics with Consistently Arbitrary Viewing and View-dependent Visibility](https://arxiv.org/abs/2505.21377v1)**  
  Authors: Yidi Li, Jun Xiao, Zhengda Lu, Yiqun Wang, Haiyong Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21377v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting  
- **[Structure from Collision](https://arxiv.org/abs/2505.21335v1)**  
  Authors: Takuhiro Kaneko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21335v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, nerf, face  
- **[3D-UIR: 3D Gaussian for Underwater 3D Scene Reconstruction via Physics Based Appearance-Medium Decoupling](https://arxiv.org/abs/2505.21238v2)**  
  Authors: Jieyu Yuan, Yujun Li, Yuanlin Zhang, Chunle Guo, Xiongxin Tang, Ruixing Wang, Chongyi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21238v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bilityniu.github.io/3D-UIR.)  
  Keywords: 3d gaussian, body, real-time rendering, gaussian splatting, ar  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: 3d gaussian, compact, real-time rendering, gaussian splatting, lightweight, urban scene, ar, geometry, efficient  

### Avatar Generation

*Showing the latest 50 out of 616 papers*

- **[Hyperspectral Gaussian Splatting](https://arxiv.org/abs/2505.21890v1)**  
  Authors: Sunil Kumar Narayanan, Lingjun Zhao, Lu Gan, Yongsheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21890v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, ar, gaussian splatting, nerf, face  
- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, illumination, gaussian splatting, ar, relightable, lighting, shadow, neural rendering, human, ray tracing, geometry, relighting, face  
- **[Structure from Collision](https://arxiv.org/abs/2505.21335v1)**  
  Authors: Takuhiro Kaneko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21335v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, nerf, face  
- **[3D-UIR: 3D Gaussian for Underwater 3D Scene Reconstruction via Physics Based Appearance-Medium Decoupling](https://arxiv.org/abs/2505.21238v2)**  
  Authors: Jieyu Yuan, Yujun Li, Yuanlin Zhang, Chunle Guo, Xiongxin Tang, Ruixing Wang, Chongyi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21238v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bilityniu.github.io/3D-UIR.)  
  Keywords: 3d gaussian, body, real-time rendering, gaussian splatting, ar  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, sparse-view, motion, face  
- **[OmniIndoor3D: Comprehensive Indoor 3D Reconstruction](https://arxiv.org/abs/2505.20610v1)**  
  Authors: Xiaobao Wei, Xiaoan Zhang, Hao Wang, Qingpo Wuwu, Ming Lu, Wenzhao Zheng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20610v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ucwxb.github.io/OmniIndoor3D/)  
  Keywords: 3d reconstruction, 3d gaussian, ar, lightweight, understanding, geometry, face  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: 3d reconstruction, ar, gaussian splatting, sparse-view, fast, motion, face  
- **[Efficient Differentiable Hardware Rasterization for 3D Gaussian Splatting](https://arxiv.org/abs/2505.18764v1)**  
  Authors: Yitian Yuan, Qianyue He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18764v1.pdf)  
  Keywords: head, 3d gaussian, ar, gaussian splatting, acceleration, fast, nerf, efficient  
- **[Pose Splatter: A 3D Gaussian Splatting Model for Quantifying Animal Pose and Appearance](https://arxiv.org/abs/2505.18342v1)**  
  Authors: Jack Goffinet, Youngjo Min, Carlo Tomasi, David E. Carlson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18342v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, human, geometry, face  
- **[SplatCo: Structure-View Collaborative Gaussian Splatting for Detail-Preserving Rendering of Large-Scale Unbounded Scenes](https://arxiv.org/abs/2505.17951v1)**  
  Authors: Haihong Xiao, Jianan Zou, Yuxin Zhou, Ying He, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17951v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SCUT-BIP-Lab/SplatCo?style=social)](https://github.com/SCUT-BIP-Lab/SplatCo)  
  Keywords: high-fidelity, ar, gaussian splatting, outdoor, face  

### Dynamic Scene

*Showing the latest 50 out of 689 papers*

- **[STDR: Spatio-Temporal Decoupling for Real-Time Dynamic Scene Rendering](https://arxiv.org/abs/2505.22400v1)**  
  Authors: Zehao Li, Hao Jiang, Yujun Cai, Jianing Chen, Baolong Bi, Shuqin Gao, Honglong Zhao, Yiwei Wang, Tianlu Mao, Zhaoqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22400v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, gaussian splatting, ar, dynamic, motion, deformation  
- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: high-fidelity, 3d gaussian, semantic, tracking, gaussian splatting, ar, localization, mapping, slam, dynamic, efficient, motion  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, sparse-view, motion, face  
- **[WeatherEdit: Controllable Weather Editing with 4D Gaussian Field](https://arxiv.org/abs/2505.20471v1)**  
  Authors: Chenghao Qian, Wenjing Li, Yuhu Guo, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/w-edit)  
  Keywords: ar, lighting, dynamic, autonomous driving, 4d  
- **[ParticleGS: Particle-Based Dynamics Modeling of 3D Gaussians for Prior-free Motion Extrapolation](https://arxiv.org/abs/2505.20270v1)**  
  Authors: Jinsheng Quan, Chunshi Wang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20270v1.pdf) | [![GitHub](https://img.shields.io/github/stars/QuanJinSheng/ParticleGS?style=social)](https://github.com/QuanJinSheng/ParticleGS)  
  Keywords: 3d reconstruction, 3d gaussian, ar, gaussian splatting, dynamic, motion, deformation  
- **[Weather-Magician: Reconstruction and Rendering Framework for 4D Weather Synthesis In Real Time](https://arxiv.org/abs/2505.19919v1)**  
  Authors: Chen Sang, Yeqiang Qian, Jiale Zhang, Chunxiang Wang, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19919v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, ar, dynamic, efficient, vr, 4d  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: 3d reconstruction, ar, gaussian splatting, sparse-view, fast, motion, face  
- **[ADD-SLAM: Adaptive Dynamic Dense SLAM with Gaussian Splatting](https://arxiv.org/abs/2505.19420v1)**  
  Authors: Wenhua Wu, Chenpeng Su, Siting Zhu, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19420v1.pdf)  
  Keywords: semantic, 3d gaussian, recognition, tracking, gaussian splatting, ar, segmentation, localization, mapping, slam, dynamic, nerf  
- **[Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse Views by Jointly Training Hemisphere Sampled Synthetic Images](https://arxiv.org/abs/2505.19264v1)**  
  Authors: Guangan Chen, Anh Minh Truong, Hanhe Lin, Michiel Vlaminck, Wilfried Philips, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19264v1.pdf)  
  Keywords: sparse view, 3d gaussian, ar, gaussian splatting, sparse-view, motion  
- **[Veta-GS: View-dependent deformable 3D Gaussian Splatting for thermal infrared Novel-view Synthesis](https://arxiv.org/abs/2505.19138v1)**  
  Authors: Myeongseok Nam, Wongi Park, Minsol Kim, Hyejin Hur, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19138v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, gaussian splatting, ar, deformation  

### Few-shot

*Showing the latest 50 out of 132 papers*

- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, sparse-view, geometry, nerf, efficient  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, sparse-view, motion, face  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: 3d reconstruction, ar, gaussian splatting, sparse-view, fast, motion, face  
- **[Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse Views by Jointly Training Hemisphere Sampled Synthetic Images](https://arxiv.org/abs/2505.19264v1)**  
  Authors: Guangan Chen, Anh Minh Truong, Hanhe Lin, Michiel Vlaminck, Wilfried Philips, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19264v1.pdf)  
  Keywords: sparse view, 3d gaussian, ar, gaussian splatting, sparse-view, motion  
- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: head, 3d reconstruction, compact, ar, gaussian splatting, sparse-view, dynamic, efficient, motion, deformation, 4d  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, robotics, gaussian splatting, sparse-view, ar  
- **[X-GRM: Large Gaussian Reconstruction Model for Sparse-view X-rays to Computed Tomography](https://arxiv.org/abs/2505.15235v2)**  
  Authors: Yifan Liu, Wuyang Li, Weihao Yu, Chenxin Li, Alexandre Alahi, Max Meng, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15235v2.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/X-GRM?style=social)](https://github.com/CUHK-AIM-Group/X-GRM)  
  Keywords: efficient, ar, gaussian splatting, sparse-view  
- **[SpatialCrafter: Unleashing the Imagination of Video Diffusion Models for Scene Reconstruction from Limited Observations](https://arxiv.org/abs/2505.11992v1)**  
  Authors: Songchun Zhang, Huiyao Xu, Sitong Guo, Zhongwei Xie, Pengwei Liu, Hujun Bao, Weiwei Xu, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11992v1.pdf)  
  Keywords: sparse view, 3d gaussian, semantic, ar, efficient  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: sparse view, head, ar, gaussian splatting, fast, shape reconstruction, geometry, efficient, face  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: sparse view, 3d reconstruction, 3d gaussian, ar, gaussian splatting, sparse-view, fast, shape reconstruction, geometry, face  

### Geometry Reconstruction

*Showing the latest 50 out of 595 papers*

- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, sparse-view, geometry, nerf, efficient  
- **[Hyperspectral Gaussian Splatting](https://arxiv.org/abs/2505.21890v1)**  
  Authors: Sunil Kumar Narayanan, Lingjun Zhao, Lu Gan, Yongsheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21890v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, ar, gaussian splatting, nerf, face  
- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, illumination, gaussian splatting, ar, relightable, lighting, shadow, neural rendering, human, ray tracing, geometry, relighting, face  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: 3d gaussian, compact, real-time rendering, gaussian splatting, lightweight, urban scene, ar, geometry, efficient  
- **[OmniIndoor3D: Comprehensive Indoor 3D Reconstruction](https://arxiv.org/abs/2505.20610v1)**  
  Authors: Xiaobao Wei, Xiaoan Zhang, Hao Wang, Qingpo Wuwu, Ming Lu, Wenzhao Zheng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20610v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ucwxb.github.io/OmniIndoor3D/)  
  Keywords: 3d reconstruction, 3d gaussian, ar, lightweight, understanding, geometry, face  
- **[CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting](https://arxiv.org/abs/2505.20469v1)**  
  Authors: Lei Tian, Xiaomin Li, Liqian Ma, Hefei Huang, Zirui Zheng, Hao Yin, Taiqing Li, Huchuan Lu, Xu Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://epsilontl.github.io/CCL-LGS/.)  
  Keywords: semantic, 3d reconstruction, 3d gaussian, compact, gaussian splatting, robotics, ar, autonomous driving, understanding  
- **[ParticleGS: Particle-Based Dynamics Modeling of 3D Gaussians for Prior-free Motion Extrapolation](https://arxiv.org/abs/2505.20270v1)**  
  Authors: Jinsheng Quan, Chunshi Wang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20270v1.pdf) | [![GitHub](https://img.shields.io/github/stars/QuanJinSheng/ParticleGS?style=social)](https://github.com/QuanJinSheng/ParticleGS)  
  Keywords: 3d reconstruction, 3d gaussian, ar, gaussian splatting, dynamic, motion, deformation  
- **[HaloGS: Loose Coupling of Compact Geometry and Gaussian Splats for 3D Scenes](https://arxiv.org/abs/2505.20267v1)**  
  Authors: Changjian Jiang, Kerui Ren, Linning Xu, Jiong Chen, Jiangmiao Pang, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20267v1.pdf)  
  Keywords: 3d reconstruction, compact, ar, lightweight, outdoor, geometry  
- **[OB3D: A New Dataset for Benchmarking Omnidirectional 3D Reconstruction Using Blender](https://arxiv.org/abs/2505.20126v1)**  
  Authors: Shintaro Ito, Natsuki Takama, Toshiki Watanabe, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20126v1.pdf)  
  Keywords: high-fidelity, 3d reconstruction, 3d gaussian, ar, gaussian splatting, nerf  
- **[ErpGS: Equirectangular Image Rendering enhanced with 3D Gaussian Regularization](https://arxiv.org/abs/2505.19883v1)**  
  Authors: Shintaro Ito, Natsuki Takama, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19883v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, ar, nerf  

### Large Scene

*Showing the latest 50 out of 106 papers*

- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: 3d gaussian, compact, real-time rendering, gaussian splatting, lightweight, urban scene, ar, geometry, efficient  
- **[HaloGS: Loose Coupling of Compact Geometry and Gaussian Splats for 3D Scenes](https://arxiv.org/abs/2505.20267v1)**  
  Authors: Changjian Jiang, Kerui Ren, Linning Xu, Jiong Chen, Jiangmiao Pang, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20267v1.pdf)  
  Keywords: 3d reconstruction, compact, ar, lightweight, outdoor, geometry  
- **[VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale Scenes](https://arxiv.org/abs/2505.18992v1)**  
  Authors: Tianchen Deng, Wenhua Wu, Junjie He, Yue Pan, Xirui Jiang, Shenghai Yuan, Danwei Wang, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18992v1.pdf) | [![GitHub](https://img.shields.io/github/stars/dtc111111/vpgs-slam?style=social)](https://github.com/dtc111111/vpgs-slam)  
  Keywords: 3d gaussian, compact, tracking, gaussian splatting, ar, outdoor, mapping, slam  
- **[SplatCo: Structure-View Collaborative Gaussian Splatting for Detail-Preserving Rendering of Large-Scale Unbounded Scenes](https://arxiv.org/abs/2505.17951v1)**  
  Authors: Haihong Xiao, Jianan Zou, Yuxin Zhou, Ying He, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17951v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SCUT-BIP-Lab/SplatCo?style=social)](https://github.com/SCUT-BIP-Lab/SplatCo)  
  Keywords: high-fidelity, ar, gaussian splatting, outdoor, face  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: high-fidelity, 3d reconstruction, 3d gaussian, semantic, gaussian splatting, ar, outdoor, segmentation, neural rendering, understanding, efficient, survey  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: ar, gaussian splatting, lightweight, outdoor, lighting, localization, human, face  
- **[Gaussian Splatting as a Unified Representation for Autonomy in Unstructured Environments](https://arxiv.org/abs/2505.11794v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11794v1.pdf)  
  Keywords: semantic, outdoor, ar, gaussian splatting  
- **[EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes](https://arxiv.org/abs/2505.10787v1)**  
  Authors: Jianlin Guo, Haihong Xiao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10787v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, gaussian splatting, ar, outdoor, geometry, nerf, efficient, face  
- **[Consistent Quantity-Quality Control across Scenes for Deployment-Aware Gaussian Splatting](https://arxiv.org/abs/2505.10473v2)**  
  Authors: Fengdi Zhang, Hongkun Cao, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10473v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhang-fengdi.github.io/ControlGS/)  
  Keywords: semantic, 3d gaussian, compact, ar, gaussian splatting, outdoor  
- **[Large-Scale Gaussian Splatting SLAM](https://arxiv.org/abs/2505.09915v1)**  
  Authors: Zhe Xin, Chenyang Wu, Penghui Huang, Yanyong Zhang, Yinian Mao, Guoquan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09915v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lsg-slam.github.io.)  
  Keywords: 3d gaussian, recognition, tracking, gaussian splatting, ar, outdoor, slam, nerf  

### Model Compression

*Showing the latest 50 out of 701 papers*

- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: high-fidelity, 3d gaussian, semantic, tracking, gaussian splatting, ar, localization, mapping, slam, dynamic, efficient, motion  
- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, sparse-view, geometry, nerf, efficient  
- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: 3d gaussian, illumination, ar, lighting, shadow, mapping, efficient  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: 3d gaussian, compact, real-time rendering, gaussian splatting, lightweight, urban scene, ar, geometry, efficient  
- **[ProBA: Probabilistic Bundle Adjustment with the Bhattacharyya Coefficient](https://arxiv.org/abs/2505.20858v1)**  
  Authors: Jason Chui, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20858v1.pdf)  
  Keywords: 3d gaussian, efficient, slam, ar  
- **[Wideband RF Radiance Field Modeling Using Frequency-embedded 3D Gaussian Splatting](https://arxiv.org/abs/2505.20714v1)**  
  Authors: Zechen Li, Lanqing Yang, Yiheng Bian, Hao Pan, Yongjian Fu, Yezhou Wang, Yi-Chao Chen, Guangtao Xue, Ju Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20714v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sim-2-real/Wideband3DGS?style=social)](https://github.com/sim-2-real/Wideband3DGS)  
  Keywords: 3d gaussian, efficient, ar, gaussian splatting  
- **[OmniIndoor3D: Comprehensive Indoor 3D Reconstruction](https://arxiv.org/abs/2505.20610v1)**  
  Authors: Xiaobao Wei, Xiaoan Zhang, Hao Wang, Qingpo Wuwu, Ming Lu, Wenzhao Zheng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20610v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ucwxb.github.io/OmniIndoor3D/)  
  Keywords: 3d reconstruction, 3d gaussian, ar, lightweight, understanding, geometry, face  
- **[CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting](https://arxiv.org/abs/2505.20469v1)**  
  Authors: Lei Tian, Xiaomin Li, Liqian Ma, Hefei Huang, Zirui Zheng, Hao Yin, Taiqing Li, Huchuan Lu, Xu Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://epsilontl.github.io/CCL-LGS/.)  
  Keywords: semantic, 3d reconstruction, 3d gaussian, compact, gaussian splatting, robotics, ar, autonomous driving, understanding  
- **[HaloGS: Loose Coupling of Compact Geometry and Gaussian Splats for 3D Scenes](https://arxiv.org/abs/2505.20267v1)**  
  Authors: Changjian Jiang, Kerui Ren, Linning Xu, Jiong Chen, Jiangmiao Pang, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20267v1.pdf)  
  Keywords: 3d reconstruction, compact, ar, lightweight, outdoor, geometry  
- **[Weather-Magician: Reconstruction and Rendering Framework for 4D Weather Synthesis In Real Time](https://arxiv.org/abs/2505.19919v1)**  
  Authors: Chen Sang, Yeqiang Qian, Jiale Zhang, Chunxiang Wang, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19919v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, ar, dynamic, efficient, vr, 4d  

### Quality Enhancement

*Showing the latest 50 out of 295 papers*

- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: high-fidelity, 3d gaussian, semantic, tracking, gaussian splatting, ar, localization, mapping, slam, dynamic, efficient, motion  
- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, illumination, gaussian splatting, ar, relightable, lighting, shadow, neural rendering, human, ray tracing, geometry, relighting, face  
- **[OB3D: A New Dataset for Benchmarking Omnidirectional 3D Reconstruction Using Blender](https://arxiv.org/abs/2505.20126v1)**  
  Authors: Shintaro Ito, Natsuki Takama, Toshiki Watanabe, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20126v1.pdf)  
  Keywords: high-fidelity, 3d reconstruction, 3d gaussian, ar, gaussian splatting, nerf  
- **[SplatCo: Structure-View Collaborative Gaussian Splatting for Detail-Preserving Rendering of Large-Scale Unbounded Scenes](https://arxiv.org/abs/2505.17951v1)**  
  Authors: Haihong Xiao, Jianan Zou, Yuxin Zhou, Ying He, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17951v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SCUT-BIP-Lab/SplatCo?style=social)](https://github.com/SCUT-BIP-Lab/SplatCo)  
  Keywords: high-fidelity, ar, gaussian splatting, outdoor, face  
- **[CGS-GAN: 3D Consistent Gaussian Splatting GANs for High Resolution Human Head Synthesis](https://arxiv.org/abs/2505.17590v1)**  
  Authors: Florian Barthel, Wieland Morgenstern, Paul Hinzer, Anna Hilsmann, Peter Eisert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17590v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fraunhoferhhi.github.io/cgs-gan/)  
  Keywords: head, 3d gaussian, ar, gaussian splatting, efficient rendering, human, high quality, efficient  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: high-fidelity, 3d reconstruction, 3d gaussian, semantic, gaussian splatting, ar, outdoor, segmentation, neural rendering, understanding, efficient, survey  
- **[Render-FM: A Foundation Model for Real-time Photorealistic Volumetric Rendering](https://arxiv.org/abs/2505.17338v1)**  
  Authors: Zhongpai Gao, Meng Zheng, Benjamin Planche, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17338v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/renderfm/.)  
  Keywords: high-fidelity, ar, gaussian splatting, medical, neural rendering, efficient  
- **[Motion Matters: Compact Gaussian Streaming for Free-Viewpoint Video Reconstruction](https://arxiv.org/abs/2505.16533v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Youneng Bao, Xiandong Meng, Fanyang Meng, Ronggang Wang, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16533v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, compact, head, gaussian splatting, ar, dynamic, efficient, motion, face  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, robotics, gaussian splatting, sparse-view, ar  
- **[PlantDreamer: Achieving Realistic 3D Plant Models with Diffusion-Guided Gaussian Splatting](https://arxiv.org/abs/2505.15528v1)**  
  Authors: Zane K J Hartley, Lewis A G Stuart, Andrew P French, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15528v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, ar, gaussian splatting, geometry  

### Ray Tracing

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, illumination, gaussian splatting, ar, relightable, lighting, shadow, neural rendering, human, ray tracing, geometry, relighting, face  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: ar, gaussian splatting, fast, relightable, lighting, shadow, human, ray tracing, geometry, relighting, avatar  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, acceleration, lighting, efficient rendering, ray tracing, efficient, relighting  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: 3d gaussian, compact, ar, gaussian splatting, acceleration, animation, dynamic, ray marching, efficient  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: 3d gaussian, real-time rendering, gaussian splatting, illumination, ar, lighting, ray tracing, global illumination, efficient, face  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, illumination, fast, lighting, face, dynamic, global illumination, light transport  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, fast, shadow, neural rendering, reflection, ray tracing  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: tracking, real-time rendering, ar, relightable, lighting, face, dynamic, ray tracing, geometry, efficient, 4d  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: gaussian splatting, lighting, shadow, reflection, ray tracing, face  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, ray tracing, survey  

### Relighting

*Showing the latest 50 out of 204 papers*

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, illumination, gaussian splatting, ar, relightable, lighting, shadow, neural rendering, human, ray tracing, geometry, relighting, face  
- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: 3d gaussian, illumination, ar, lighting, shadow, mapping, efficient  
- **[WeatherEdit: Controllable Weather Editing with 4D Gaussian Field](https://arxiv.org/abs/2505.20471v1)**  
  Authors: Chenghao Qian, Wenjing Li, Yuhu Guo, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/w-edit)  
  Keywords: ar, lighting, dynamic, autonomous driving, 4d  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: ar, gaussian splatting, lightweight, outdoor, lighting, localization, human, face  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: high-fidelity, 3d reconstruction, 3d gaussian, ar, gaussian splatting, lighting, motion  
- **[3D Gaussian Adaptive Reconstruction for Fourier Light-Field Microscopy](https://arxiv.org/abs/2505.12875v1)**  
  Authors: Chenyu Xu, Zhouyu Jin, Chengkang Shen, Hao Zhu, Zhan Ma, Bo Xiong, You Zhou, Xun Cao, Ning Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12875v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, lighting, nerf  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, ar, lighting, survey  
- **[TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians](https://arxiv.org/abs/2504.18768v2)**  
  Authors: Letian Huang, Dongwei Ye, Jialin Dan, Chengzhi Tao, Huiwen Liu, Kun Zhou, Bo Ren, Yuanqi Li, Yanwen Guo, Jie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18768v2.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, fast, reflection, efficient  
- **[RGS-DR: Reflective Gaussian Surfels with Deferred Rendering for Shiny Objects](https://arxiv.org/abs/2504.18468v3)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18468v3.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry, lighting, reflection, nerf, relighting, face  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: 3d gaussian, ar, gaussian splatting, fast, lighting, mapping, nerf, vr  

### SLAM

*Showing the latest 50 out of 273 papers*

- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: high-fidelity, 3d gaussian, semantic, tracking, gaussian splatting, ar, localization, mapping, slam, dynamic, efficient, motion  
- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: 3d gaussian, illumination, ar, lighting, shadow, mapping, efficient  
- **[ProBA: Probabilistic Bundle Adjustment with the Bhattacharyya Coefficient](https://arxiv.org/abs/2505.20858v1)**  
  Authors: Jason Chui, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20858v1.pdf)  
  Keywords: 3d gaussian, efficient, slam, ar  
- **[ADD-SLAM: Adaptive Dynamic Dense SLAM with Gaussian Splatting](https://arxiv.org/abs/2505.19420v1)**  
  Authors: Wenhua Wu, Chenpeng Su, Siting Zhu, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19420v1.pdf)  
  Keywords: semantic, 3d gaussian, recognition, tracking, gaussian splatting, ar, segmentation, localization, mapping, slam, dynamic, nerf  
- **[FHGS: Feature-Homogenized Gaussian Splatting](https://arxiv.org/abs/2505.19154v1)**  
  Authors: Q. G. Duan, Benyun Zhao, Mingqiao Han Yijun Huang, Ben M. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19154v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fhgs.cuastro.org/.)  
  Keywords: semantic, 3d gaussian, real-time rendering, gaussian splatting, ar, efficient rendering, mapping, understanding, efficient  
- **[VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale Scenes](https://arxiv.org/abs/2505.18992v1)**  
  Authors: Tianchen Deng, Wenhua Wu, Junjie He, Yue Pan, Xirui Jiang, Shenghai Yuan, Danwei Wang, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18992v1.pdf) | [![GitHub](https://img.shields.io/github/stars/dtc111111/vpgs-slam?style=social)](https://github.com/dtc111111/vpgs-slam)  
  Keywords: 3d gaussian, compact, tracking, gaussian splatting, ar, outdoor, mapping, slam  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, avatar, body, tracking, ar, neural rendering, face, human, geometry, motion, deformation  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: ar, gaussian splatting, lightweight, outdoor, lighting, localization, human, face  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, gaussian splatting, segmentation, localization, mapping, slam, nerf, efficient, survey  
- **[GTR: Gaussian Splatting Tracking and Reconstruction of Unknown Objects Based on Appearance and Geometric Complexity](https://arxiv.org/abs/2505.11905v1)**  
  Authors: Takuya Ikeda, Sergey Zakharov, Muhammad Zubair Irshad, Istvan Balazs Opra, Shun Iwase, Dian Chen, Mark Tjersland, Robert Lee, Alexandre Dilly, Rares Ambrus, Koichi Nishiwaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11905v1.pdf)  
  Keywords: high-fidelity, 3d reconstruction, 3d gaussian, tracking, gaussian splatting, ar, geometry  

### Scene Understanding

*Showing the latest 50 out of 327 papers*

- **[UP-SLAM: Adaptively Structured Gaussian SLAM with Uncertainty Prediction in Dynamic Environments](https://arxiv.org/abs/2505.22335v1)**  
  Authors: Wancai Zheng, Linlin Ou, Jiajie He, Libo Zhou, Xinyi Yu, Yan Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aczheng-cai.github.io/up_slam.github.io/)  
  Keywords: high-fidelity, 3d gaussian, semantic, tracking, gaussian splatting, ar, localization, mapping, slam, dynamic, efficient, motion  
- **[OmniIndoor3D: Comprehensive Indoor 3D Reconstruction](https://arxiv.org/abs/2505.20610v1)**  
  Authors: Xiaobao Wei, Xiaoan Zhang, Hao Wang, Qingpo Wuwu, Ming Lu, Wenzhao Zheng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20610v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ucwxb.github.io/OmniIndoor3D/)  
  Keywords: 3d reconstruction, 3d gaussian, ar, lightweight, understanding, geometry, face  
- **[CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting](https://arxiv.org/abs/2505.20469v1)**  
  Authors: Lei Tian, Xiaomin Li, Liqian Ma, Hefei Huang, Zirui Zheng, Hao Yin, Taiqing Li, Huchuan Lu, Xu Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://epsilontl.github.io/CCL-LGS/.)  
  Keywords: semantic, 3d reconstruction, 3d gaussian, compact, gaussian splatting, robotics, ar, autonomous driving, understanding  
- **[ADD-SLAM: Adaptive Dynamic Dense SLAM with Gaussian Splatting](https://arxiv.org/abs/2505.19420v1)**  
  Authors: Wenhua Wu, Chenpeng Su, Siting Zhu, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19420v1.pdf)  
  Keywords: semantic, 3d gaussian, recognition, tracking, gaussian splatting, ar, segmentation, localization, mapping, slam, dynamic, nerf  
- **[FHGS: Feature-Homogenized Gaussian Splatting](https://arxiv.org/abs/2505.19154v1)**  
  Authors: Q. G. Duan, Benyun Zhao, Mingqiao Han Yijun Huang, Ben M. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19154v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fhgs.cuastro.org/.)  
  Keywords: semantic, 3d gaussian, real-time rendering, gaussian splatting, ar, efficient rendering, mapping, understanding, efficient  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: high-fidelity, 3d reconstruction, 3d gaussian, semantic, gaussian splatting, ar, outdoor, segmentation, neural rendering, understanding, efficient, survey  
- **[Scan, Materialize, Simulate: A Generalizable Framework for Physically Grounded Robot Planning](https://arxiv.org/abs/2505.14938v1)**  
  Authors: Amine Elhafsi, Daniel Morton, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.14938v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, gaussian splatting, segmentation, dynamic, understanding  
- **[TACOcc:Target-Adaptive Cross-Modal Fusion with Volume Rendering for 3D Semantic Occupancy](https://arxiv.org/abs/2505.12693v1)**  
  Authors: Luyao Lei, Shuo Xu, Yifan Bai, Xing Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12693v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, gaussian splatting, geometry, face  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, gaussian splatting, segmentation, localization, mapping, slam, nerf, efficient, survey  
- **[SpatialCrafter: Unleashing the Imagination of Video Diffusion Models for Scene Reconstruction from Limited Observations](https://arxiv.org/abs/2505.11992v1)**  
  Authors: Songchun Zhang, Huiyao Xu, Sitong Guo, Zhongwei Xie, Pengwei Liu, Hujun Bao, Weiwei Xu, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11992v1.pdf)  
  Keywords: sparse view, 3d gaussian, semantic, ar, efficient  



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