# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-05-29 00:55:38

## Categories

- [3DGS Surveys](#3dgs-surveys) (35 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (523 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1825 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (615 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (687 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (131 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (593 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (106 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (699 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (294 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (41 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (204 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (272 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (326 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: outdoor, high-fidelity, segmentation, efficient, gaussian splatting, semantic, survey, neural rendering, understanding, ar, 3d gaussian, 3d reconstruction  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: nerf, slam, segmentation, localization, efficient, gaussian splatting, semantic, mapping, survey, ar, 3d gaussian  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: body, gaussian splatting, motion, survey, 4d, understanding, ar, dynamic, 3d gaussian  
- **[A Survey of 3D Reconstruction with Event Cameras: From Event-based Geometry to Neural 3D Rendering](https://arxiv.org/abs/2505.08438v1)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v1.pdf)  
  Keywords: gaussian splatting, motion, survey, geometry, neural rendering, ar, dynamic, 3d gaussian, 3d reconstruction  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: efficient, gaussian splatting, survey, ar, 3d reconstruction, fast  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: nerf, autonomous driving, robotics, semantic, survey, ar, 3d gaussian  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: survey, ar, lighting, 3d gaussian, 3d reconstruction  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: nerf, outdoor, face, gaussian splatting, sparse view, survey, geometry, understanding, ar, 3d gaussian, 3d reconstruction  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: segmentation, robotics, semantic, gaussian splatting, survey, ar, lighting, 3d gaussian  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: gaussian splatting, motion, survey, ar, lighting, dynamic, 3d gaussian, 3d reconstruction, fast  

### Acceleration

*Showing the latest 50 out of 523 papers*

- **[3D-UIR: 3D Gaussian for Underwater 3D Scene Reconstruction via Physics-Based Appearance-Medium Decouplin](https://arxiv.org/abs/2505.21238v1)**  
  Authors: Jieyu Yuan, Yujun Li, Yuanlin Zhang, Chunle Guo, Xiongxin Tang, Ruixing Wang, Chongyi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21238v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bilityniu.github.io/3D-UIR}{https://bilityniu.github.io/3D-UIR)  
  Keywords: body, gaussian splatting, ar, real-time rendering, 3d gaussian  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: compact, urban scene, gaussian splatting, efficient, geometry, ar, real-time rendering, 3d gaussian, lightweight  
- **[Weather-Magician: Reconstruction and Rendering Framework for 4D Weather Synthesis In Real Time](https://arxiv.org/abs/2505.19919v1)**  
  Authors: Chen Sang, Yeqiang Qian, Jiale Zhang, Chunxiang Wang, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19919v1.pdf)  
  Keywords: efficient, gaussian splatting, vr, 4d, ar, dynamic, real-time rendering  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v1)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v1.pdf)  
  Keywords: face, sparse-view, gaussian splatting, motion, ar, 3d reconstruction, fast  
- **[K-Buffers: A Plug-in Method for Enhancing Neural Fields with Multiple Buffers](https://arxiv.org/abs/2505.19564v1)**  
  Authors: Haofan Ren, Zunjie Zhu, Xiang Chen, Ming Lu, Rongfeng Lu, Chenggang Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19564v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, acceleration, ar  
- **[Triangle Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2505.19175v1)**  
  Authors: Jan Held, Renaud Vandeghen, Adrien Deliege, Abdullah Hamdi, Silvio Giancola, Anthony Cioppa, Andrea Vedaldi, Bernard Ghanem, Andrea Tagliasacchi, Marc Van Droogenbroeck  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19175v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://trianglesplatting.github.io/)  
  Keywords: nerf, efficient, gaussian splatting, ar, 3d gaussian, fast  
- **[FHGS: Feature-Homogenized Gaussian Splatting](https://arxiv.org/abs/2505.19154v1)**  
  Authors: Q. G. Duan, Benyun Zhao, Mingqiao Han Yijun Huang, Ben M. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19154v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fhgs.cuastro.org/.)  
  Keywords: efficient, gaussian splatting, semantic, mapping, understanding, ar, efficient rendering, real-time rendering, 3d gaussian  
- **[Veta-GS: View-dependent deformable 3D Gaussian Splatting for thermal infrared Novel-view Synthesis](https://arxiv.org/abs/2505.19138v1)**  
  Authors: Myeongseok Nam, Wongi Park, Minsol Kim, Hyejin Hur, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19138v1.pdf)  
  Keywords: deformation, gaussian splatting, ar, real-time rendering, 3d gaussian  
- **[Efficient Differentiable Hardware Rasterization for 3D Gaussian Splatting](https://arxiv.org/abs/2505.18764v1)**  
  Authors: Yitian Yuan, Qianyue He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18764v1.pdf)  
  Keywords: nerf, acceleration, efficient, gaussian splatting, head, ar, 3d gaussian, fast  
- **[SuperGS: Consistent and Detailed 3D Super-Resolution Scene Reconstruction via Gaussian Splatting](https://arxiv.org/abs/2505.18649v1)**  
  Authors: Shiyun Xie, Zhiru Wang, Yinghao Zhu, Xu Wang, Chengwei Pan, Xiwang Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18649v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, real-time rendering  

### Applications

*Showing the latest 50 out of 1825 papers*

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: face, high-fidelity, ray tracing, gaussian splatting, illumination, relightable, geometry, neural rendering, lighting, relighting, human, ar, 3d gaussian, shadow  
- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: efficient, mapping, illumination, ar, lighting, 3d gaussian, shadow  
- **[Empowering Vector Graphics with Consistently Arbitrary Viewing and View-dependent Visibility](https://arxiv.org/abs/2505.21377v1)**  
  Authors: Yidi Li, Jun Xiao, Zhengda Lu, Yiqun Wang, Haiyong Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21377v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar  
- **[Structure from Collision](https://arxiv.org/abs/2505.21335v1)**  
  Authors: Takuhiro Kaneko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21335v1.pdf)  
  Keywords: nerf, face, gaussian splatting, ar, 3d gaussian  
- **[3D-UIR: 3D Gaussian for Underwater 3D Scene Reconstruction via Physics-Based Appearance-Medium Decouplin](https://arxiv.org/abs/2505.21238v1)**  
  Authors: Jieyu Yuan, Yujun Li, Yuanlin Zhang, Chunle Guo, Xiongxin Tang, Ruixing Wang, Chongyi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21238v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bilityniu.github.io/3D-UIR}{https://bilityniu.github.io/3D-UIR)  
  Keywords: body, gaussian splatting, ar, real-time rendering, 3d gaussian  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: compact, urban scene, gaussian splatting, efficient, geometry, ar, real-time rendering, 3d gaussian, lightweight  
- **[ProBA: Probabilistic Bundle Adjustment with the Bhattacharyya Coefficient](https://arxiv.org/abs/2505.20858v1)**  
  Authors: Jason Chui, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20858v1.pdf)  
  Keywords: 3d gaussian, efficient, slam, ar  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: face, sparse-view, gaussian splatting, motion, ar, 3d gaussian  
- **[Wideband RF Radiance Field Modeling Using Frequency-embedded 3D Gaussian Splatting](https://arxiv.org/abs/2505.20714v1)**  
  Authors: Zechen Li, Lanqing Yang, Yiheng Bian, Hao Pan, Yongjian Fu, Yezhou Wang, Yi-Chao Chen, Guangtao Xue, Ju Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20714v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sim-2-real/Wideband3DGS?style=social)](https://github.com/sim-2-real/Wideband3DGS)  
  Keywords: 3d gaussian, gaussian splatting, efficient, ar  
- **[OmniIndoor3D: Comprehensive Indoor 3D Reconstruction](https://arxiv.org/abs/2505.20610v1)**  
  Authors: Xiaobao Wei, Xiaoan Zhang, Hao Wang, Qingpo Wuwu, Ming Lu, Wenzhao Zheng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20610v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ucwxb.github.io/OmniIndoor3D/)  
  Keywords: face, geometry, understanding, ar, 3d gaussian, 3d reconstruction, lightweight  

### Avatar Generation

*Showing the latest 50 out of 615 papers*

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: face, high-fidelity, ray tracing, gaussian splatting, illumination, relightable, geometry, neural rendering, lighting, relighting, human, ar, 3d gaussian, shadow  
- **[Structure from Collision](https://arxiv.org/abs/2505.21335v1)**  
  Authors: Takuhiro Kaneko  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21335v1.pdf)  
  Keywords: nerf, face, gaussian splatting, ar, 3d gaussian  
- **[3D-UIR: 3D Gaussian for Underwater 3D Scene Reconstruction via Physics-Based Appearance-Medium Decouplin](https://arxiv.org/abs/2505.21238v1)**  
  Authors: Jieyu Yuan, Yujun Li, Yuanlin Zhang, Chunle Guo, Xiongxin Tang, Ruixing Wang, Chongyi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21238v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bilityniu.github.io/3D-UIR}{https://bilityniu.github.io/3D-UIR)  
  Keywords: body, gaussian splatting, ar, real-time rendering, 3d gaussian  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: face, sparse-view, gaussian splatting, motion, ar, 3d gaussian  
- **[OmniIndoor3D: Comprehensive Indoor 3D Reconstruction](https://arxiv.org/abs/2505.20610v1)**  
  Authors: Xiaobao Wei, Xiaoan Zhang, Hao Wang, Qingpo Wuwu, Ming Lu, Wenzhao Zheng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20610v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ucwxb.github.io/OmniIndoor3D/)  
  Keywords: face, geometry, understanding, ar, 3d gaussian, 3d reconstruction, lightweight  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v1)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v1.pdf)  
  Keywords: face, sparse-view, gaussian splatting, motion, ar, 3d reconstruction, fast  
- **[Efficient Differentiable Hardware Rasterization for 3D Gaussian Splatting](https://arxiv.org/abs/2505.18764v1)**  
  Authors: Yitian Yuan, Qianyue He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18764v1.pdf)  
  Keywords: nerf, acceleration, efficient, gaussian splatting, head, ar, 3d gaussian, fast  
- **[Pose Splatter: A 3D Gaussian Splatting Model for Quantifying Animal Pose and Appearance](https://arxiv.org/abs/2505.18342v1)**  
  Authors: Jack Goffinet, Youngjo Min, Carlo Tomasi, David E. Carlson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18342v1.pdf)  
  Keywords: face, gaussian splatting, geometry, ar, 3d gaussian, human  
- **[SplatCo: Structure-View Collaborative Gaussian Splatting for Detail-Preserving Rendering of Large-Scale Unbounded Scenes](https://arxiv.org/abs/2505.17951v1)**  
  Authors: Haihong Xiao, Jianan Zou, Yuxin Zhou, Ying He, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17951v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SCUT-BIP-Lab/SplatCo?style=social)](https://github.com/SCUT-BIP-Lab/SplatCo)  
  Keywords: face, outdoor, high-fidelity, gaussian splatting, ar  
- **[CGS-GAN: 3D Consistent Gaussian Splatting GANs for High Resolution Human Head Synthesis](https://arxiv.org/abs/2505.17590v1)**  
  Authors: Florian Barthel, Wieland Morgenstern, Paul Hinzer, Anna Hilsmann, Peter Eisert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17590v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fraunhoferhhi.github.io/cgs-gan/)  
  Keywords: efficient, gaussian splatting, head, ar, efficient rendering, 3d gaussian, human, high quality  

### Dynamic Scene

*Showing the latest 50 out of 687 papers*

- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: face, sparse-view, gaussian splatting, motion, ar, 3d gaussian  
- **[WeatherEdit: Controllable Weather Editing with 4D Gaussian Field](https://arxiv.org/abs/2505.20471v1)**  
  Authors: Chenghao Qian, Wenjing Li, Yuhu Guo, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/w-edit)  
  Keywords: autonomous driving, 4d, ar, lighting, dynamic  
- **[ParticleGS: Particle-Based Dynamics Modeling of 3D Gaussians for Prior-free Motion Extrapolation](https://arxiv.org/abs/2505.20270v1)**  
  Authors: Jinsheng Quan, Chunshi Wang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20270v1.pdf) | [![GitHub](https://img.shields.io/github/stars/QuanJinSheng/ParticleGS?style=social)](https://github.com/QuanJinSheng/ParticleGS)  
  Keywords: deformation, gaussian splatting, motion, ar, dynamic, 3d gaussian, 3d reconstruction  
- **[Weather-Magician: Reconstruction and Rendering Framework for 4D Weather Synthesis In Real Time](https://arxiv.org/abs/2505.19919v1)**  
  Authors: Chen Sang, Yeqiang Qian, Jiale Zhang, Chunxiang Wang, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19919v1.pdf)  
  Keywords: efficient, gaussian splatting, vr, 4d, ar, dynamic, real-time rendering  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v1)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v1.pdf)  
  Keywords: face, sparse-view, gaussian splatting, motion, ar, 3d reconstruction, fast  
- **[ADD-SLAM: Adaptive Dynamic Dense SLAM with Gaussian Splatting](https://arxiv.org/abs/2505.19420v1)**  
  Authors: Wenhua Wu, Chenpeng Su, Siting Zhu, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19420v1.pdf)  
  Keywords: recognition, nerf, slam, segmentation, localization, semantic, gaussian splatting, mapping, tracking, ar, dynamic, 3d gaussian  
- **[Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse Views by Jointly Training Hemisphere Sampled Synthetic Images](https://arxiv.org/abs/2505.19264v1)**  
  Authors: Guangan Chen, Anh Minh Truong, Hanhe Lin, Michiel Vlaminck, Wilfried Philips, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19264v1.pdf)  
  Keywords: sparse-view, gaussian splatting, sparse view, motion, ar, 3d gaussian  
- **[Veta-GS: View-dependent deformable 3D Gaussian Splatting for thermal infrared Novel-view Synthesis](https://arxiv.org/abs/2505.19138v1)**  
  Authors: Myeongseok Nam, Wongi Park, Minsol Kim, Hyejin Hur, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19138v1.pdf)  
  Keywords: deformation, gaussian splatting, ar, real-time rendering, 3d gaussian  
- **[CTRL-GS: Cascaded Temporal Residue Learning for 4D Gaussian Splatting](https://arxiv.org/abs/2505.18306v1)**  
  Authors: Karly Hou, Wanhua Li, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18306v1.pdf)  
  Keywords: gaussian splatting, 4d, ar, dynamic, real-time rendering  
- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: deformation, sparse-view, efficient, gaussian splatting, head, motion, 4d, ar, dynamic, compact, 3d reconstruction  

### Few-shot

*Showing the latest 50 out of 131 papers*

- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: face, sparse-view, gaussian splatting, motion, ar, 3d gaussian  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v1)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v1.pdf)  
  Keywords: face, sparse-view, gaussian splatting, motion, ar, 3d reconstruction, fast  
- **[Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse Views by Jointly Training Hemisphere Sampled Synthetic Images](https://arxiv.org/abs/2505.19264v1)**  
  Authors: Guangan Chen, Anh Minh Truong, Hanhe Lin, Michiel Vlaminck, Wilfried Philips, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19264v1.pdf)  
  Keywords: sparse-view, gaussian splatting, sparse view, motion, ar, 3d gaussian  
- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: deformation, sparse-view, efficient, gaussian splatting, head, motion, 4d, ar, dynamic, compact, 3d reconstruction  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: high-fidelity, sparse-view, robotics, gaussian splatting, ar, 3d gaussian  
- **[X-GRM: Large Gaussian Reconstruction Model for Sparse-view X-rays to Computed Tomography](https://arxiv.org/abs/2505.15235v2)**  
  Authors: Yifan Liu, Wuyang Li, Weihao Yu, Chenxin Li, Alexandre Alahi, Max Meng, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15235v2.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/X-GRM?style=social)](https://github.com/CUHK-AIM-Group/X-GRM)  
  Keywords: efficient, gaussian splatting, sparse-view, ar  
- **[SpatialCrafter: Unleashing the Imagination of Video Diffusion Models for Scene Reconstruction from Limited Observations](https://arxiv.org/abs/2505.11992v1)**  
  Authors: Songchun Zhang, Huiyao Xu, Sitong Guo, Zhongwei Xie, Pengwei Liu, Hujun Bao, Weiwei Xu, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11992v1.pdf)  
  Keywords: semantic, efficient, sparse view, ar, 3d gaussian  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: face, efficient, shape reconstruction, gaussian splatting, sparse view, head, geometry, ar, fast  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: face, sparse-view, gaussian splatting, shape reconstruction, sparse view, geometry, ar, 3d gaussian, 3d reconstruction, fast  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: nerf, outdoor, face, gaussian splatting, sparse view, survey, geometry, understanding, ar, 3d gaussian, 3d reconstruction  

### Geometry Reconstruction

*Showing the latest 50 out of 593 papers*

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: face, high-fidelity, ray tracing, gaussian splatting, illumination, relightable, geometry, neural rendering, lighting, relighting, human, ar, 3d gaussian, shadow  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: compact, urban scene, gaussian splatting, efficient, geometry, ar, real-time rendering, 3d gaussian, lightweight  
- **[OmniIndoor3D: Comprehensive Indoor 3D Reconstruction](https://arxiv.org/abs/2505.20610v1)**  
  Authors: Xiaobao Wei, Xiaoan Zhang, Hao Wang, Qingpo Wuwu, Ming Lu, Wenzhao Zheng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20610v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ucwxb.github.io/OmniIndoor3D/)  
  Keywords: face, geometry, understanding, ar, 3d gaussian, 3d reconstruction, lightweight  
- **[CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting](https://arxiv.org/abs/2505.20469v1)**  
  Authors: Lei Tian, Xiaomin Li, Liqian Ma, Hefei Huang, Zirui Zheng, Hao Yin, Taiqing Li, Huchuan Lu, Xu Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://epsilontl.github.io/CCL-LGS/.)  
  Keywords: compact, autonomous driving, robotics, semantic, gaussian splatting, understanding, ar, 3d gaussian, 3d reconstruction  
- **[ParticleGS: Particle-Based Dynamics Modeling of 3D Gaussians for Prior-free Motion Extrapolation](https://arxiv.org/abs/2505.20270v1)**  
  Authors: Jinsheng Quan, Chunshi Wang, Yawei Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20270v1.pdf) | [![GitHub](https://img.shields.io/github/stars/QuanJinSheng/ParticleGS?style=social)](https://github.com/QuanJinSheng/ParticleGS)  
  Keywords: deformation, gaussian splatting, motion, ar, dynamic, 3d gaussian, 3d reconstruction  
- **[HaloGS: Loose Coupling of Compact Geometry and Gaussian Splats for 3D Scenes](https://arxiv.org/abs/2505.20267v1)**  
  Authors: Changjian Jiang, Kerui Ren, Linning Xu, Jiong Chen, Jiangmiao Pang, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20267v1.pdf)  
  Keywords: outdoor, geometry, ar, compact, 3d reconstruction, lightweight  
- **[OB3D: A New Dataset for Benchmarking Omnidirectional 3D Reconstruction Using Blender](https://arxiv.org/abs/2505.20126v1)**  
  Authors: Shintaro Ito, Natsuki Takama, Toshiki Watanabe, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20126v1.pdf)  
  Keywords: nerf, high-fidelity, gaussian splatting, ar, 3d gaussian, 3d reconstruction  
- **[ErpGS: Equirectangular Image Rendering enhanced with 3D Gaussian Regularization](https://arxiv.org/abs/2505.19883v1)**  
  Authors: Shintaro Ito, Natsuki Takama, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19883v1.pdf)  
  Keywords: 3d gaussian, nerf, 3d reconstruction, ar  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v1)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v1.pdf)  
  Keywords: face, sparse-view, gaussian splatting, motion, ar, 3d reconstruction, fast  
- **[Pose Splatter: A 3D Gaussian Splatting Model for Quantifying Animal Pose and Appearance](https://arxiv.org/abs/2505.18342v1)**  
  Authors: Jack Goffinet, Youngjo Min, Carlo Tomasi, David E. Carlson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18342v1.pdf)  
  Keywords: face, gaussian splatting, geometry, ar, 3d gaussian, human  

### Large Scene

*Showing the latest 50 out of 106 papers*

- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: compact, urban scene, gaussian splatting, efficient, geometry, ar, real-time rendering, 3d gaussian, lightweight  
- **[HaloGS: Loose Coupling of Compact Geometry and Gaussian Splats for 3D Scenes](https://arxiv.org/abs/2505.20267v1)**  
  Authors: Changjian Jiang, Kerui Ren, Linning Xu, Jiong Chen, Jiangmiao Pang, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20267v1.pdf)  
  Keywords: outdoor, geometry, ar, compact, 3d reconstruction, lightweight  
- **[VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale Scenes](https://arxiv.org/abs/2505.18992v1)**  
  Authors: Tianchen Deng, Wenhua Wu, Junjie He, Yue Pan, Xirui Jiang, Shenghai Yuan, Danwei Wang, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18992v1.pdf) | [![GitHub](https://img.shields.io/github/stars/dtc111111/vpgs-slam?style=social)](https://github.com/dtc111111/vpgs-slam)  
  Keywords: outdoor, compact, slam, gaussian splatting, mapping, tracking, ar, 3d gaussian  
- **[SplatCo: Structure-View Collaborative Gaussian Splatting for Detail-Preserving Rendering of Large-Scale Unbounded Scenes](https://arxiv.org/abs/2505.17951v1)**  
  Authors: Haihong Xiao, Jianan Zou, Yuxin Zhou, Ying He, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17951v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SCUT-BIP-Lab/SplatCo?style=social)](https://github.com/SCUT-BIP-Lab/SplatCo)  
  Keywords: face, outdoor, high-fidelity, gaussian splatting, ar  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: outdoor, high-fidelity, segmentation, efficient, gaussian splatting, semantic, survey, neural rendering, understanding, ar, 3d gaussian, 3d reconstruction  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: outdoor, face, localization, gaussian splatting, ar, lighting, human, lightweight  
- **[Gaussian Splatting as a Unified Representation for Autonomy in Unstructured Environments](https://arxiv.org/abs/2505.11794v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11794v1.pdf)  
  Keywords: semantic, gaussian splatting, outdoor, ar  
- **[EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes](https://arxiv.org/abs/2505.10787v1)**  
  Authors: Jianlin Guo, Haihong Xiao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10787v1.pdf)  
  Keywords: nerf, outdoor, face, efficient, gaussian splatting, geometry, ar, real-time rendering, 3d gaussian  
- **[Consistent Quantity-Quality Control across Scenes for Deployment-Aware Gaussian Splatting](https://arxiv.org/abs/2505.10473v2)**  
  Authors: Fengdi Zhang, Hongkun Cao, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10473v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhang-fengdi.github.io/ControlGS/)  
  Keywords: outdoor, compact, semantic, gaussian splatting, ar, 3d gaussian  
- **[Large-Scale Gaussian Splatting SLAM](https://arxiv.org/abs/2505.09915v1)**  
  Authors: Zhe Xin, Chenyang Wu, Penghui Huang, Yanyong Zhang, Yinian Mao, Guoquan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09915v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lsg-slam.github.io.)  
  Keywords: recognition, nerf, outdoor, slam, gaussian splatting, tracking, ar, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 699 papers*

- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: efficient, mapping, illumination, ar, lighting, 3d gaussian, shadow  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: compact, urban scene, gaussian splatting, efficient, geometry, ar, real-time rendering, 3d gaussian, lightweight  
- **[ProBA: Probabilistic Bundle Adjustment with the Bhattacharyya Coefficient](https://arxiv.org/abs/2505.20858v1)**  
  Authors: Jason Chui, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20858v1.pdf)  
  Keywords: 3d gaussian, efficient, slam, ar  
- **[Wideband RF Radiance Field Modeling Using Frequency-embedded 3D Gaussian Splatting](https://arxiv.org/abs/2505.20714v1)**  
  Authors: Zechen Li, Lanqing Yang, Yiheng Bian, Hao Pan, Yongjian Fu, Yezhou Wang, Yi-Chao Chen, Guangtao Xue, Ju Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20714v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sim-2-real/Wideband3DGS?style=social)](https://github.com/sim-2-real/Wideband3DGS)  
  Keywords: 3d gaussian, gaussian splatting, efficient, ar  
- **[OmniIndoor3D: Comprehensive Indoor 3D Reconstruction](https://arxiv.org/abs/2505.20610v1)**  
  Authors: Xiaobao Wei, Xiaoan Zhang, Hao Wang, Qingpo Wuwu, Ming Lu, Wenzhao Zheng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20610v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ucwxb.github.io/OmniIndoor3D/)  
  Keywords: face, geometry, understanding, ar, 3d gaussian, 3d reconstruction, lightweight  
- **[CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting](https://arxiv.org/abs/2505.20469v1)**  
  Authors: Lei Tian, Xiaomin Li, Liqian Ma, Hefei Huang, Zirui Zheng, Hao Yin, Taiqing Li, Huchuan Lu, Xu Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://epsilontl.github.io/CCL-LGS/.)  
  Keywords: compact, autonomous driving, robotics, semantic, gaussian splatting, understanding, ar, 3d gaussian, 3d reconstruction  
- **[HaloGS: Loose Coupling of Compact Geometry and Gaussian Splats for 3D Scenes](https://arxiv.org/abs/2505.20267v1)**  
  Authors: Changjian Jiang, Kerui Ren, Linning Xu, Jiong Chen, Jiangmiao Pang, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20267v1.pdf)  
  Keywords: outdoor, geometry, ar, compact, 3d reconstruction, lightweight  
- **[Weather-Magician: Reconstruction and Rendering Framework for 4D Weather Synthesis In Real Time](https://arxiv.org/abs/2505.19919v1)**  
  Authors: Chen Sang, Yeqiang Qian, Jiale Zhang, Chunxiang Wang, Ming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19919v1.pdf)  
  Keywords: efficient, gaussian splatting, vr, 4d, ar, dynamic, real-time rendering  
- **[Triangle Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2505.19175v1)**  
  Authors: Jan Held, Renaud Vandeghen, Adrien Deliege, Abdullah Hamdi, Silvio Giancola, Anthony Cioppa, Andrea Vedaldi, Bernard Ghanem, Andrea Tagliasacchi, Marc Van Droogenbroeck  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19175v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://trianglesplatting.github.io/)  
  Keywords: nerf, efficient, gaussian splatting, ar, 3d gaussian, fast  
- **[FHGS: Feature-Homogenized Gaussian Splatting](https://arxiv.org/abs/2505.19154v1)**  
  Authors: Q. G. Duan, Benyun Zhao, Mingqiao Han Yijun Huang, Ben M. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19154v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fhgs.cuastro.org/.)  
  Keywords: efficient, gaussian splatting, semantic, mapping, understanding, ar, efficient rendering, real-time rendering, 3d gaussian  

### Quality Enhancement

*Showing the latest 50 out of 294 papers*

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: face, high-fidelity, ray tracing, gaussian splatting, illumination, relightable, geometry, neural rendering, lighting, relighting, human, ar, 3d gaussian, shadow  
- **[OB3D: A New Dataset for Benchmarking Omnidirectional 3D Reconstruction Using Blender](https://arxiv.org/abs/2505.20126v1)**  
  Authors: Shintaro Ito, Natsuki Takama, Toshiki Watanabe, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20126v1.pdf)  
  Keywords: nerf, high-fidelity, gaussian splatting, ar, 3d gaussian, 3d reconstruction  
- **[SplatCo: Structure-View Collaborative Gaussian Splatting for Detail-Preserving Rendering of Large-Scale Unbounded Scenes](https://arxiv.org/abs/2505.17951v1)**  
  Authors: Haihong Xiao, Jianan Zou, Yuxin Zhou, Ying He, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17951v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SCUT-BIP-Lab/SplatCo?style=social)](https://github.com/SCUT-BIP-Lab/SplatCo)  
  Keywords: face, outdoor, high-fidelity, gaussian splatting, ar  
- **[CGS-GAN: 3D Consistent Gaussian Splatting GANs for High Resolution Human Head Synthesis](https://arxiv.org/abs/2505.17590v1)**  
  Authors: Florian Barthel, Wieland Morgenstern, Paul Hinzer, Anna Hilsmann, Peter Eisert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17590v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fraunhoferhhi.github.io/cgs-gan/)  
  Keywords: efficient, gaussian splatting, head, ar, efficient rendering, 3d gaussian, human, high quality  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: outdoor, high-fidelity, segmentation, efficient, gaussian splatting, semantic, survey, neural rendering, understanding, ar, 3d gaussian, 3d reconstruction  
- **[Render-FM: A Foundation Model for Real-time Photorealistic Volumetric Rendering](https://arxiv.org/abs/2505.17338v1)**  
  Authors: Zhongpai Gao, Meng Zheng, Benjamin Planche, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17338v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/renderfm/.)  
  Keywords: high-fidelity, efficient, gaussian splatting, neural rendering, ar, medical  
- **[Motion Matters: Compact Gaussian Streaming for Free-Viewpoint Video Reconstruction](https://arxiv.org/abs/2505.16533v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Youneng Bao, Xiandong Meng, Fanyang Meng, Ronggang Wang, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16533v1.pdf)  
  Keywords: compact, face, high-fidelity, efficient, gaussian splatting, head, motion, ar, dynamic, 3d gaussian  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: high-fidelity, sparse-view, robotics, gaussian splatting, ar, 3d gaussian  
- **[PlantDreamer: Achieving Realistic 3D Plant Models with Diffusion-Guided Gaussian Splatting](https://arxiv.org/abs/2505.15528v1)**  
  Authors: Zane K J Hartley, Lewis A G Stuart, Andrew P French, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15528v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, geometry, ar, 3d gaussian  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: deformation, face, high-fidelity, body, motion, geometry, neural rendering, tracking, ar, avatar, 3d gaussian, human  

### Ray Tracing

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: face, high-fidelity, ray tracing, gaussian splatting, illumination, relightable, geometry, neural rendering, lighting, relighting, human, ar, 3d gaussian, shadow  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: ray tracing, gaussian splatting, relightable, geometry, ar, lighting, relighting, avatar, shadow, human, fast  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: acceleration, ray tracing, efficient, gaussian splatting, ar, lighting, efficient rendering, relighting, 3d gaussian  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: compact, acceleration, efficient, gaussian splatting, animation, ar, ray marching, dynamic, 3d gaussian  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: face, ray tracing, efficient, gaussian splatting, global illumination, illumination, ar, lighting, real-time rendering, 3d gaussian  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: face, global illumination, illumination, light transport, lighting, real-time rendering, dynamic, 3d gaussian, fast  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: reflection, ray tracing, gaussian splatting, neural rendering, ar, 3d gaussian, shadow, fast  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: face, ray tracing, efficient, relightable, geometry, 4d, lighting, tracking, ar, real-time rendering, dynamic  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: face, ray tracing, gaussian splatting, lighting, shadow, reflection  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, gaussian splatting, survey, ar, 3d gaussian  

### Relighting

*Showing the latest 50 out of 204 papers*

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: face, high-fidelity, ray tracing, gaussian splatting, illumination, relightable, geometry, neural rendering, lighting, relighting, human, ar, 3d gaussian, shadow  
- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: efficient, mapping, illumination, ar, lighting, 3d gaussian, shadow  
- **[WeatherEdit: Controllable Weather Editing with 4D Gaussian Field](https://arxiv.org/abs/2505.20471v1)**  
  Authors: Chenghao Qian, Wenjing Li, Yuhu Guo, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/w-edit)  
  Keywords: autonomous driving, 4d, ar, lighting, dynamic  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: outdoor, face, localization, gaussian splatting, ar, lighting, human, lightweight  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, motion, ar, lighting, 3d gaussian, 3d reconstruction  
- **[3D Gaussian Adaptive Reconstruction for Fourier Light-Field Microscopy](https://arxiv.org/abs/2505.12875v1)**  
  Authors: Chenyu Xu, Zhouyu Jin, Chengkang Shen, Hao Zhu, Zhan Ma, Bo Xiong, You Zhou, Xun Cao, Ning Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12875v1.pdf)  
  Keywords: nerf, gaussian splatting, ar, lighting, 3d gaussian  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: survey, ar, lighting, 3d gaussian, 3d reconstruction  
- **[TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians](https://arxiv.org/abs/2504.18768v2)**  
  Authors: Letian Huang, Dongwei Ye, Jialin Dan, Chengzhi Tao, Huiwen Liu, Kun Zhou, Bo Ren, Yuanqi Li, Yanwen Guo, Jie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18768v2.pdf)  
  Keywords: fast, efficient, gaussian splatting, ar, 3d gaussian, reflection  
- **[RGS-DR: Reflective Gaussian Surfels with Deferred Rendering for Shiny Objects](https://arxiv.org/abs/2504.18468v3)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18468v3.pdf)  
  Keywords: nerf, face, gaussian splatting, geometry, ar, lighting, relighting, 3d gaussian, reflection  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: nerf, vr, gaussian splatting, mapping, ar, lighting, 3d gaussian, fast  

### SLAM

*Showing the latest 50 out of 272 papers*

- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: efficient, mapping, illumination, ar, lighting, 3d gaussian, shadow  
- **[ProBA: Probabilistic Bundle Adjustment with the Bhattacharyya Coefficient](https://arxiv.org/abs/2505.20858v1)**  
  Authors: Jason Chui, Daniel Cremers  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20858v1.pdf)  
  Keywords: 3d gaussian, efficient, slam, ar  
- **[ADD-SLAM: Adaptive Dynamic Dense SLAM with Gaussian Splatting](https://arxiv.org/abs/2505.19420v1)**  
  Authors: Wenhua Wu, Chenpeng Su, Siting Zhu, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19420v1.pdf)  
  Keywords: recognition, nerf, slam, segmentation, localization, semantic, gaussian splatting, mapping, tracking, ar, dynamic, 3d gaussian  
- **[FHGS: Feature-Homogenized Gaussian Splatting](https://arxiv.org/abs/2505.19154v1)**  
  Authors: Q. G. Duan, Benyun Zhao, Mingqiao Han Yijun Huang, Ben M. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19154v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fhgs.cuastro.org/.)  
  Keywords: efficient, gaussian splatting, semantic, mapping, understanding, ar, efficient rendering, real-time rendering, 3d gaussian  
- **[VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale Scenes](https://arxiv.org/abs/2505.18992v1)**  
  Authors: Tianchen Deng, Wenhua Wu, Junjie He, Yue Pan, Xirui Jiang, Shenghai Yuan, Danwei Wang, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18992v1.pdf) | [![GitHub](https://img.shields.io/github/stars/dtc111111/vpgs-slam?style=social)](https://github.com/dtc111111/vpgs-slam)  
  Keywords: outdoor, compact, slam, gaussian splatting, mapping, tracking, ar, 3d gaussian  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: deformation, face, high-fidelity, body, motion, geometry, neural rendering, tracking, ar, avatar, 3d gaussian, human  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: outdoor, face, localization, gaussian splatting, ar, lighting, human, lightweight  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: nerf, slam, segmentation, localization, efficient, gaussian splatting, semantic, mapping, survey, ar, 3d gaussian  
- **[GTR: Gaussian Splatting Tracking and Reconstruction of Unknown Objects Based on Appearance and Geometric Complexity](https://arxiv.org/abs/2505.11905v1)**  
  Authors: Takuya Ikeda, Sergey Zakharov, Muhammad Zubair Irshad, Istvan Balazs Opra, Shun Iwase, Dian Chen, Mark Tjersland, Robert Lee, Alexandre Dilly, Rares Ambrus, Koichi Nishiwaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11905v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, geometry, tracking, ar, 3d gaussian, 3d reconstruction  
- **[Large-Scale Gaussian Splatting SLAM](https://arxiv.org/abs/2505.09915v1)**  
  Authors: Zhe Xin, Chenyang Wu, Penghui Huang, Yanyong Zhang, Yinian Mao, Guoquan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09915v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lsg-slam.github.io.)  
  Keywords: recognition, nerf, outdoor, slam, gaussian splatting, tracking, ar, 3d gaussian  

### Scene Understanding

*Showing the latest 50 out of 326 papers*

- **[OmniIndoor3D: Comprehensive Indoor 3D Reconstruction](https://arxiv.org/abs/2505.20610v1)**  
  Authors: Xiaobao Wei, Xiaoan Zhang, Hao Wang, Qingpo Wuwu, Ming Lu, Wenzhao Zheng, Shanghang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20610v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ucwxb.github.io/OmniIndoor3D/)  
  Keywords: face, geometry, understanding, ar, 3d gaussian, 3d reconstruction, lightweight  
- **[CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting](https://arxiv.org/abs/2505.20469v1)**  
  Authors: Lei Tian, Xiaomin Li, Liqian Ma, Hefei Huang, Zirui Zheng, Hao Yin, Taiqing Li, Huchuan Lu, Xu Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://epsilontl.github.io/CCL-LGS/.)  
  Keywords: compact, autonomous driving, robotics, semantic, gaussian splatting, understanding, ar, 3d gaussian, 3d reconstruction  
- **[ADD-SLAM: Adaptive Dynamic Dense SLAM with Gaussian Splatting](https://arxiv.org/abs/2505.19420v1)**  
  Authors: Wenhua Wu, Chenpeng Su, Siting Zhu, Tianchen Deng, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19420v1.pdf)  
  Keywords: recognition, nerf, slam, segmentation, localization, semantic, gaussian splatting, mapping, tracking, ar, dynamic, 3d gaussian  
- **[FHGS: Feature-Homogenized Gaussian Splatting](https://arxiv.org/abs/2505.19154v1)**  
  Authors: Q. G. Duan, Benyun Zhao, Mingqiao Han Yijun Huang, Ben M. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19154v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fhgs.cuastro.org/.)  
  Keywords: efficient, gaussian splatting, semantic, mapping, understanding, ar, efficient rendering, real-time rendering, 3d gaussian  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: outdoor, high-fidelity, segmentation, efficient, gaussian splatting, semantic, survey, neural rendering, understanding, ar, 3d gaussian, 3d reconstruction  
- **[Scan, Materialize, Simulate: A Generalizable Framework for Physically Grounded Robot Planning](https://arxiv.org/abs/2505.14938v1)**  
  Authors: Amine Elhafsi, Daniel Morton, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.14938v1.pdf)  
  Keywords: segmentation, semantic, gaussian splatting, understanding, ar, dynamic, 3d gaussian  
- **[TACOcc:Target-Adaptive Cross-Modal Fusion with Volume Rendering for 3D Semantic Occupancy](https://arxiv.org/abs/2505.12693v1)**  
  Authors: Luyao Lei, Shuo Xu, Yifan Bai, Xing Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12693v1.pdf)  
  Keywords: face, semantic, gaussian splatting, geometry, ar, 3d gaussian  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: nerf, slam, segmentation, localization, efficient, gaussian splatting, semantic, mapping, survey, ar, 3d gaussian  
- **[SpatialCrafter: Unleashing the Imagination of Video Diffusion Models for Scene Reconstruction from Limited Observations](https://arxiv.org/abs/2505.11992v1)**  
  Authors: Songchun Zhang, Huiyao Xu, Sitong Guo, Zhongwei Xie, Pengwei Liu, Hujun Bao, Weiwei Xu, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11992v1.pdf)  
  Keywords: semantic, efficient, sparse view, ar, 3d gaussian  
- **[iSegMan: Interactive Segment-and-Manipulate 3D Gaussians](https://arxiv.org/abs/2505.11934v1)**  
  Authors: Yian Zhao, Wanshi Xu, Ruochong Zheng, Pengchong Qiao, Chang Liu, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11934v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhao-yian.github.io/iSegMan.)  
  Keywords: segmentation, efficient, ar, efficient rendering, 3d gaussian  



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