# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-05-18 00:58:35

## Categories

- [3DGS Surveys](#3dgs-surveys) (33 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (506 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1762 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (595 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (668 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (124 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (569 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (98 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (672 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (279 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (40 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (198 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (263 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (314 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v1)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v1.pdf)  
  Keywords: 4d, body, ar, 3d gaussian, understanding, survey, motion, dynamic, gaussian splatting  
- **[A Survey of 3D Reconstruction with Event Cameras: From Event-based Geometry to Neural 3D Rendering](https://arxiv.org/abs/2505.08438v1)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v1.pdf)  
  Keywords: geometry, neural rendering, 3d reconstruction, ar, 3d gaussian, survey, motion, dynamic, gaussian splatting  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: efficient, fast, 3d reconstruction, ar, survey, gaussian splatting  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: autonomous driving, ar, 3d gaussian, nerf, survey, semantic, robotics  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d reconstruction, ar, 3d gaussian, survey, lighting  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: face, geometry, outdoor, 3d reconstruction, ar, sparse view, 3d gaussian, nerf, understanding, survey, gaussian splatting  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: ar, 3d gaussian, survey, semantic, robotics, segmentation, gaussian splatting, lighting  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: fast, 3d reconstruction, ar, 3d gaussian, survey, motion, dynamic, gaussian splatting, lighting  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: ar, 3d gaussian, real-time rendering, survey, dynamic, gaussian splatting  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: ar, semantic, survey, geometry  

### Acceleration

*Showing the latest 50 out of 506 papers*

- **[VRSplat: Fast and Robust Gaussian Splatting for Virtual Reality](https://arxiv.org/abs/2505.10144v1)**  
  Authors: Xuechang Tu, Lukas Radl, Michael Steiner, Markus Steinberger, Bernhard Kerbl, Fernando de la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10144v1.pdf)  
  Keywords: face, efficient, fast, head, ar, 3d gaussian, vr, gaussian splatting  
- **[FOCI: Trajectory Optimization on Gaussian Splats](https://arxiv.org/abs/2505.08510v1)**  
  Authors: Mario Gomez Andreu, Maximum Wilder-Smith, Victor Klemm, Vaishakh Patil, Jesus Tordesillas, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08510v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/foci/)  
  Keywords: fast, 3d reconstruction, ar, 3d gaussian, nerf, robotics, gaussian splatting  
- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539v1)**  
  Authors: Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07539v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xdimlab.github.io/GIFStream)  
  Keywords: efficient, fast, ar, real-time rendering, deformation, motion, 4d, gaussian splatting, compression  
- **[TUGS: Physics-based Compact Representation of Underwater Scenes by Tensorized Gaussian](https://arxiv.org/abs/2505.08811v1)**  
  Authors: Shijie Lian, Ziyi Zhang, Laurence Tianruo Yang and, Mengyu Ren, Debin Liu, Hua Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08811v1.pdf)  
  Keywords: face, efficient, lightweight, fast, ar, nerf, compact, gaussian splatting  
- **[Virtualized 3D Gaussians: Flexible Cluster-based Level-of-Detail System for Real-Time Rendering of Composed Scenes](https://arxiv.org/abs/2505.06523v1)**  
  Authors: Xijie Yang, Linning Xu, Lihan Jiang, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.06523v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, real-time rendering, dynamic, gaussian splatting  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: efficient, fast, 3d reconstruction, ar, survey, gaussian splatting  
- **[QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization](https://arxiv.org/abs/2505.05591v1)**  
  Authors: Yueh-Cheng Liu, Lukas Höllein, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05591v1.pdf)  
  Keywords: face, geometry, fast, ar, robotics, gaussian splatting  
- **[Steepest Descent Density Control for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2505.05587v1)**  
  Authors: Peihao Wang, Yuehao Wang, Dilin Wang, Sreyas Mohan, Zhiwen Fan, Lemeng Wu, Ruisi Cai, Yu-Ying Yeh, Zhangyang Wang, Qiang Liu, Rakesh Ranjan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05587v1.pdf)  
  Keywords: efficient, efficient rendering, ar, 3d gaussian, compact, gaussian splatting  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: face, avatar, high-fidelity, ar, 3d gaussian, real-time rendering, animation, gaussian splatting, human  
- **[Time of the Flight of the Gaussians: Optimizing Depth Indirectly in Dynamic Radiance Fields](https://arxiv.org/abs/2505.05356v1)**  
  Authors: Runfeng Li, Mikhail Okunev, Zixuan Guo, Anh Ha Duong, Christian Richardt, Matthew O'Toole, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05356v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://visual.cs.brown.edu/gftorf)  
  Keywords: geometry, high-fidelity, fast, 3d reconstruction, ar, 3d gaussian, motion, dynamic, gaussian splatting  

### Applications

*Showing the latest 50 out of 1762 papers*

- **[Consistent Quantity-Quality Control across Scenes for Deployment-Aware Gaussian Splatting](https://arxiv.org/abs/2505.10473v1)**  
  Authors: Fengdi Zhang, Hongkun Cao, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10473v1.pdf)  
  Keywords: outdoor, ar, 3d gaussian, compact, semantic, gaussian splatting  
- **[VRSplat: Fast and Robust Gaussian Splatting for Virtual Reality](https://arxiv.org/abs/2505.10144v1)**  
  Authors: Xuechang Tu, Lukas Radl, Michael Steiner, Markus Steinberger, Bernhard Kerbl, Fernando de la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10144v1.pdf)  
  Keywords: face, efficient, fast, head, ar, 3d gaussian, vr, gaussian splatting  
- **[ToonifyGB: StyleGAN-based Gaussian Blendshapes for 3D Stylized Head Avatars](https://arxiv.org/abs/2505.10072v1)**  
  Authors: Rui-Yang Ju, Sheng-Yen Huang, Yi-Ping Hung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10072v1.pdf)  
  Keywords: face, avatar, efficient, head, ar, 3d gaussian, animation  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v1)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v1.pdf)  
  Keywords: 4d, body, ar, 3d gaussian, understanding, survey, motion, dynamic, gaussian splatting  
- **[Large-Scale Gaussian Splatting SLAM](https://arxiv.org/abs/2505.09915v1)**  
  Authors: Zhe Xin, Chenyang Wu, Penghui Huang, Yanyong Zhang, Yinian Mao, Guoquan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09915v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lsg-slam.github.io.)  
  Keywords: recognition, outdoor, slam, ar, 3d gaussian, nerf, gaussian splatting, tracking  
- **[Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware](https://arxiv.org/abs/2505.09601v1)**  
  Authors: Justin Yu, Letian Fu, Huang Huang, Karim El-Refai, Rares Andrei Ambrus, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2render2real.com)  
  Keywords: geometry, ar, 3d gaussian, motion, dynamic, gaussian splatting, human, tracking  
- **[Sparse Point Cloud Patches Rendering via Splitting 2D Gaussians](https://arxiv.org/abs/2505.09413v1)**  
  Authors: Ma Changfeng, Bi Ran, Guo Jie, Wang Chongjun, Guo Yanwen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09413v1.pdf) | [![GitHub](https://img.shields.io/github/stars/murcherful/GauPCRender?style=social)](https://github.com/murcherful/GauPCRender)  
  Keywords: ar, 3d gaussian, nerf  
- **[Neural Video Compression using 2D Gaussian Splatting](https://arxiv.org/abs/2505.09324v1)**  
  Authors: Lakshya Gupta, Imran N. Junejo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09324v1.pdf)  
  Keywords: ar, gaussian splatting, motion, compression  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v1)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v1.pdf)  
  Keywords: efficient, outdoor, localization, ar, mapping, dynamic, gaussian splatting, human  
- **[DLO-Splatting: Tracking Deformable Linear Objects Using 3D Gaussian Splatting](https://arxiv.org/abs/2505.08644v1)**  
  Authors: Holly Dinkel, Marcel Büsching, Alberta Longhini, Brian Coltin, Trey Smith, Danica Kragic, Mårten Björkman, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08644v1.pdf)  
  Keywords: ar, 3d gaussian, dynamic, gaussian splatting, tracking  

### Avatar Generation

*Showing the latest 50 out of 595 papers*

- **[VRSplat: Fast and Robust Gaussian Splatting for Virtual Reality](https://arxiv.org/abs/2505.10144v1)**  
  Authors: Xuechang Tu, Lukas Radl, Michael Steiner, Markus Steinberger, Bernhard Kerbl, Fernando de la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10144v1.pdf)  
  Keywords: face, efficient, fast, head, ar, 3d gaussian, vr, gaussian splatting  
- **[ToonifyGB: StyleGAN-based Gaussian Blendshapes for 3D Stylized Head Avatars](https://arxiv.org/abs/2505.10072v1)**  
  Authors: Rui-Yang Ju, Sheng-Yen Huang, Yi-Ping Hung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10072v1.pdf)  
  Keywords: face, avatar, efficient, head, ar, 3d gaussian, animation  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v1)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v1.pdf)  
  Keywords: 4d, body, ar, 3d gaussian, understanding, survey, motion, dynamic, gaussian splatting  
- **[Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware](https://arxiv.org/abs/2505.09601v1)**  
  Authors: Justin Yu, Letian Fu, Huang Huang, Karim El-Refai, Rares Andrei Ambrus, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2render2real.com)  
  Keywords: geometry, ar, 3d gaussian, motion, dynamic, gaussian splatting, human, tracking  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v1)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v1.pdf)  
  Keywords: efficient, outdoor, localization, ar, mapping, dynamic, gaussian splatting, human  
- **[TUGS: Physics-based Compact Representation of Underwater Scenes by Tensorized Gaussian](https://arxiv.org/abs/2505.08811v1)**  
  Authors: Shijie Lian, Ziyi Zhang, Laurence Tianruo Yang and, Mengyu Ren, Debin Liu, Hua Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08811v1.pdf)  
  Keywords: face, efficient, lightweight, fast, ar, nerf, compact, gaussian splatting  
- **[TeGA: Texture Space Gaussian Avatars for High-Resolution Dynamic Head Modeling](https://arxiv.org/abs/2505.05672v1)**  
  Authors: Gengyan Li, Paulo Gotardo, Timo Bolkart, Stephan Garbin, Kripasindhu Sarkar, Abhimitra Meka, Alexandros Lattas, Thabo Beeler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05672v1.pdf)  
  Keywords: avatar, head, ar, 3d gaussian, deformation, motion, dynamic, gaussian splatting  
- **[QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization](https://arxiv.org/abs/2505.05591v1)**  
  Authors: Yueh-Cheng Liu, Lukas Höllein, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05591v1.pdf)  
  Keywords: face, geometry, fast, ar, robotics, gaussian splatting  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: face, avatar, high-fidelity, ar, 3d gaussian, real-time rendering, animation, gaussian splatting, human  
- **[Bridging Geometry-Coherent Text-to-3D Generation with Multi-View Diffusion Priors and Gaussian Splatting](https://arxiv.org/abs/2505.04262v1)**  
  Authors: Feng Yang, Wenliang Qian, Wangmeng Zuo, Hui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04262v1.pdf)  
  Keywords: face, geometry, ar, 3d gaussian, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 668 papers*

- **[ToonifyGB: StyleGAN-based Gaussian Blendshapes for 3D Stylized Head Avatars](https://arxiv.org/abs/2505.10072v1)**  
  Authors: Rui-Yang Ju, Sheng-Yen Huang, Yi-Ping Hung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10072v1.pdf)  
  Keywords: face, avatar, efficient, head, ar, 3d gaussian, animation  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v1)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v1.pdf)  
  Keywords: 4d, body, ar, 3d gaussian, understanding, survey, motion, dynamic, gaussian splatting  
- **[Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware](https://arxiv.org/abs/2505.09601v1)**  
  Authors: Justin Yu, Letian Fu, Huang Huang, Karim El-Refai, Rares Andrei Ambrus, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2render2real.com)  
  Keywords: geometry, ar, 3d gaussian, motion, dynamic, gaussian splatting, human, tracking  
- **[Neural Video Compression using 2D Gaussian Splatting](https://arxiv.org/abs/2505.09324v1)**  
  Authors: Lakshya Gupta, Imran N. Junejo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09324v1.pdf)  
  Keywords: ar, gaussian splatting, motion, compression  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v1)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v1.pdf)  
  Keywords: efficient, outdoor, localization, ar, mapping, dynamic, gaussian splatting, human  
- **[DLO-Splatting: Tracking Deformable Linear Objects Using 3D Gaussian Splatting](https://arxiv.org/abs/2505.08644v1)**  
  Authors: Holly Dinkel, Marcel Büsching, Alberta Longhini, Brian Coltin, Trey Smith, Danica Kragic, Mårten Björkman, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08644v1.pdf)  
  Keywords: ar, 3d gaussian, dynamic, gaussian splatting, tracking  
- **[A Survey of 3D Reconstruction with Event Cameras: From Event-based Geometry to Neural 3D Rendering](https://arxiv.org/abs/2505.08438v1)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v1.pdf)  
  Keywords: geometry, neural rendering, 3d reconstruction, ar, 3d gaussian, survey, motion, dynamic, gaussian splatting  
- **[ADC-GS: Anchor-Driven Deformable and Compressed Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2505.08196v1)**  
  Authors: He Huang, Qi Yang, Mufan Liu, Yiling Xu, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08196v1.pdf) | [![GitHub](https://img.shields.io/github/stars/H-Huang774/ADC-GS.git?style=social)](https://github.com/H-Huang774/ADC-GS.git)  
  Keywords: 4d, efficient, ar, deformation, motion, compact, dynamic, gaussian splatting  
- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539v1)**  
  Authors: Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07539v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xdimlab.github.io/GIFStream)  
  Keywords: efficient, fast, ar, real-time rendering, deformation, motion, 4d, gaussian splatting, compression  
- **[Virtualized 3D Gaussians: Flexible Cluster-based Level-of-Detail System for Real-Time Rendering of Composed Scenes](https://arxiv.org/abs/2505.06523v1)**  
  Authors: Xijie Yang, Linning Xu, Lihan Jiang, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.06523v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, real-time rendering, dynamic, gaussian splatting  

### Few-shot

*Showing the latest 50 out of 124 papers*

- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: face, geometry, efficient, fast, head, sparse view, ar, gaussian splatting, shape reconstruction  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: sparse-view, geometry, face, fast, 3d reconstruction, sparse view, 3d gaussian, ar, gaussian splatting, shape reconstruction  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: face, geometry, outdoor, 3d reconstruction, ar, sparse view, 3d gaussian, nerf, understanding, survey, gaussian splatting  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: sparse-view, geometry, face, fast, ar, sparse view, nerf, motion, gaussian splatting  
- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v2)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v2.pdf)  
  Keywords: body, efficient, ar, dynamic, gaussian splatting, few-shot  
- **[IXGS-Intraoperative 3D Reconstruction from Sparse, Arbitrarily Posed Real X-rays](https://arxiv.org/abs/2504.14699v1)**  
  Authors: Sascha Jecklin, Aidana Massalimova, Ruyi Zha, Lilian Calvet, Christoph J. Laux, Mazda Farshad, Philipp Fürnstahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14699v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, sparse-view  
- **[VGNC: Reducing the Overfitting of Sparse-view 3DGS via Validation-guided Gaussian Number Control](https://arxiv.org/abs/2504.14548v1)**  
  Authors: Lifeng Lin, Rongfeng Lu, Quan Chen, Haofan Ren, Ming Lu, Yaoqi Sun, Chenggang Yan, Anke Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14548v1.pdf)  
  Keywords: sparse-view, 3d reconstruction, ar, 3d gaussian, gaussian splatting  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: sparse-view, geometry, efficient, outdoor, ar, 3d gaussian, gaussian splatting  
- **[DropoutGS: Dropping Out Gaussians for Better Sparse-view Rendering](https://arxiv.org/abs/2504.09491v1)**  
  Authors: Yexing Xu, Longguang Wang, Minglin Chen, Sheng Ao, Li Li, Yulan Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuyx55.github.io/DropoutGS/.)  
  Keywords: sparse-view, ar, sparse view, 3d gaussian, gaussian splatting  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: sparse-view, avatar, body, head, ar, 3d gaussian, human  

### Geometry Reconstruction

*Showing the latest 50 out of 569 papers*

- **[Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware](https://arxiv.org/abs/2505.09601v1)**  
  Authors: Justin Yu, Letian Fu, Huang Huang, Karim El-Refai, Rares Andrei Ambrus, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2render2real.com)  
  Keywords: geometry, ar, 3d gaussian, motion, dynamic, gaussian splatting, human, tracking  
- **[FOCI: Trajectory Optimization on Gaussian Splats](https://arxiv.org/abs/2505.08510v1)**  
  Authors: Mario Gomez Andreu, Maximum Wilder-Smith, Victor Klemm, Vaishakh Patil, Jesus Tordesillas, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08510v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/foci/)  
  Keywords: fast, 3d reconstruction, ar, 3d gaussian, nerf, robotics, gaussian splatting  
- **[A Survey of 3D Reconstruction with Event Cameras: From Event-based Geometry to Neural 3D Rendering](https://arxiv.org/abs/2505.08438v1)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v1.pdf)  
  Keywords: geometry, neural rendering, 3d reconstruction, ar, 3d gaussian, survey, motion, dynamic, gaussian splatting  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: efficient, fast, 3d reconstruction, ar, survey, gaussian splatting  
- **[QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization](https://arxiv.org/abs/2505.05591v1)**  
  Authors: Yueh-Cheng Liu, Lukas Höllein, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05591v1.pdf)  
  Keywords: face, geometry, fast, ar, robotics, gaussian splatting  
- **[Time of the Flight of the Gaussians: Optimizing Depth Indirectly in Dynamic Radiance Fields](https://arxiv.org/abs/2505.05356v1)**  
  Authors: Runfeng Li, Mikhail Okunev, Zixuan Guo, Anh Ha Duong, Christian Richardt, Matthew O'Toole, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05356v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://visual.cs.brown.edu/gftorf)  
  Keywords: geometry, high-fidelity, fast, 3d reconstruction, ar, 3d gaussian, motion, dynamic, gaussian splatting  
- **[Bridging Geometry-Coherent Text-to-3D Generation with Multi-View Diffusion Priors and Gaussian Splatting](https://arxiv.org/abs/2505.04262v1)**  
  Authors: Feng Yang, Wenliang Qian, Wangmeng Zuo, Hui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04262v1.pdf)  
  Keywords: face, geometry, ar, 3d gaussian, gaussian splatting  
- **[SGCR: Spherical Gaussians for Efficient 3D Curve Reconstruction](https://arxiv.org/abs/2505.04668v1)**  
  Authors: Xinran Yang, Donghao Ji, Yuanqi Li, Jie Guo, Yanwen Guo, Junyuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04668v1.pdf)  
  Keywords: neural rendering, efficient, 3d reconstruction, fast, ar, 3d gaussian, high quality, gaussian splatting  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: face, geometry, efficient, fast, head, sparse view, ar, gaussian splatting, shape reconstruction  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: sparse-view, geometry, face, fast, 3d reconstruction, sparse view, 3d gaussian, ar, gaussian splatting, shape reconstruction  

### Large Scene

*Showing the latest 50 out of 98 papers*

- **[Consistent Quantity-Quality Control across Scenes for Deployment-Aware Gaussian Splatting](https://arxiv.org/abs/2505.10473v1)**  
  Authors: Fengdi Zhang, Hongkun Cao, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10473v1.pdf)  
  Keywords: outdoor, ar, 3d gaussian, compact, semantic, gaussian splatting  
- **[Large-Scale Gaussian Splatting SLAM](https://arxiv.org/abs/2505.09915v1)**  
  Authors: Zhe Xin, Chenyang Wu, Penghui Huang, Yanyong Zhang, Yinian Mao, Guoquan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09915v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lsg-slam.github.io.)  
  Keywords: recognition, outdoor, slam, ar, 3d gaussian, nerf, gaussian splatting, tracking  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v1)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v1.pdf)  
  Keywords: efficient, outdoor, localization, ar, mapping, dynamic, gaussian splatting, human  
- **[SLAG: Scalable Language-Augmented Gaussian Splatting](https://arxiv.org/abs/2505.08124v1)**  
  Authors: Laszlo Szilagyi, Francis Engelmann, Jeannette Bohg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08124v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://slag-project.github.io/.)  
  Keywords: efficient, ar, 3d gaussian, large scene, robotics, gaussian splatting  
- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: high-fidelity, outdoor, ar, nerf, semantic, segmentation, gaussian splatting  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: face, geometry, outdoor, 3d reconstruction, ar, sparse view, 3d gaussian, nerf, understanding, survey, gaussian splatting  
- **[HUG: Hierarchical Urban Gaussian Splatting with Block-Based Reconstruction](https://arxiv.org/abs/2504.16606v1)**  
  Authors: Zhongtao Wang, Mai Su, Huishan Au, Yilong Li, Xizhe Cao, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16606v1.pdf)  
  Keywords: urban scene, efficient, ar, 3d gaussian, gaussian splatting  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: sparse-view, geometry, efficient, outdoor, ar, 3d gaussian, gaussian splatting  
- **[You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting](https://arxiv.org/abs/2504.09062v1)**  
  Authors: Zhijie Shen, Chunyu Lin, Shujuan Huang, Lang Nie, Kang Liao, Yao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09062v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhijieshen-bjtu/TPGS?style=social)](https://github.com/zhijieshen-bjtu/TPGS)  
  Keywords: face, outdoor, 3d reconstruction, ar, 3d gaussian, gaussian splatting  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: outdoor, ar, reflection, nerf, motion, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 672 papers*

- **[Consistent Quantity-Quality Control across Scenes for Deployment-Aware Gaussian Splatting](https://arxiv.org/abs/2505.10473v1)**  
  Authors: Fengdi Zhang, Hongkun Cao, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10473v1.pdf)  
  Keywords: outdoor, ar, 3d gaussian, compact, semantic, gaussian splatting  
- **[VRSplat: Fast and Robust Gaussian Splatting for Virtual Reality](https://arxiv.org/abs/2505.10144v1)**  
  Authors: Xuechang Tu, Lukas Radl, Michael Steiner, Markus Steinberger, Bernhard Kerbl, Fernando de la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10144v1.pdf)  
  Keywords: face, efficient, fast, head, ar, 3d gaussian, vr, gaussian splatting  
- **[ToonifyGB: StyleGAN-based Gaussian Blendshapes for 3D Stylized Head Avatars](https://arxiv.org/abs/2505.10072v1)**  
  Authors: Rui-Yang Ju, Sheng-Yen Huang, Yi-Ping Hung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10072v1.pdf)  
  Keywords: face, avatar, efficient, head, ar, 3d gaussian, animation  
- **[Neural Video Compression using 2D Gaussian Splatting](https://arxiv.org/abs/2505.09324v1)**  
  Authors: Lakshya Gupta, Imran N. Junejo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09324v1.pdf)  
  Keywords: ar, gaussian splatting, motion, compression  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v1)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v1.pdf)  
  Keywords: efficient, outdoor, localization, ar, mapping, dynamic, gaussian splatting, human  
- **[ADC-GS: Anchor-Driven Deformable and Compressed Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2505.08196v1)**  
  Authors: He Huang, Qi Yang, Mufan Liu, Yiling Xu, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08196v1.pdf) | [![GitHub](https://img.shields.io/github/stars/H-Huang774/ADC-GS.git?style=social)](https://github.com/H-Huang774/ADC-GS.git)  
  Keywords: 4d, efficient, ar, deformation, motion, compact, dynamic, gaussian splatting  
- **[SLAG: Scalable Language-Augmented Gaussian Splatting](https://arxiv.org/abs/2505.08124v1)**  
  Authors: Laszlo Szilagyi, Francis Engelmann, Jeannette Bohg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08124v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://slag-project.github.io/.)  
  Keywords: efficient, ar, 3d gaussian, large scene, robotics, gaussian splatting  
- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539v1)**  
  Authors: Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07539v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xdimlab.github.io/GIFStream)  
  Keywords: efficient, fast, ar, real-time rendering, deformation, motion, 4d, gaussian splatting, compression  
- **[TUGS: Physics-based Compact Representation of Underwater Scenes by Tensorized Gaussian](https://arxiv.org/abs/2505.08811v1)**  
  Authors: Shijie Lian, Ziyi Zhang, Laurence Tianruo Yang and, Mengyu Ren, Debin Liu, Hua Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08811v1.pdf)  
  Keywords: face, efficient, lightweight, fast, ar, nerf, compact, gaussian splatting  
- **[Virtualized 3D Gaussians: Flexible Cluster-based Level-of-Detail System for Real-Time Rendering of Composed Scenes](https://arxiv.org/abs/2505.06523v1)**  
  Authors: Xijie Yang, Linning Xu, Lihan Jiang, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.06523v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, real-time rendering, dynamic, gaussian splatting  

### Quality Enhancement

*Showing the latest 50 out of 279 papers*

- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: high-fidelity, outdoor, ar, nerf, semantic, segmentation, gaussian splatting  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: face, avatar, high-fidelity, ar, 3d gaussian, real-time rendering, animation, gaussian splatting, human  
- **[Time of the Flight of the Gaussians: Optimizing Depth Indirectly in Dynamic Radiance Fields](https://arxiv.org/abs/2505.05356v1)**  
  Authors: Runfeng Li, Mikhail Okunev, Zixuan Guo, Anh Ha Duong, Christian Richardt, Matthew O'Toole, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05356v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://visual.cs.brown.edu/gftorf)  
  Keywords: geometry, high-fidelity, fast, 3d reconstruction, ar, 3d gaussian, motion, dynamic, gaussian splatting  
- **[SGCR: Spherical Gaussians for Efficient 3D Curve Reconstruction](https://arxiv.org/abs/2505.04668v1)**  
  Authors: Xinran Yang, Donghao Ji, Yuanqi Li, Jie Guo, Yanwen Guo, Junyuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04668v1.pdf)  
  Keywords: neural rendering, efficient, 3d reconstruction, fast, ar, 3d gaussian, high quality, gaussian splatting  
- **[GarmentGS: Point-Cloud Guided Gaussian Splatting for High-Fidelity Non-Watertight 3D Garment Reconstruction](https://arxiv.org/abs/2505.02126v2)**  
  Authors: Zhihao Tang, Shenghao Yang, Hongtao Zhang, Mingbo Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02126v2.pdf)  
  Keywords: face, high-fidelity, fast, ar, 3d gaussian, real-time rendering, gaussian splatting  
- **[HoloTime: Taming Video Diffusion Models for Panoramic 4D Scene Generation](https://arxiv.org/abs/2504.21650v2)**  
  Authors: Haiyang Zhou, Wangbo Yu, Jiawen Guan, Xinhua Cheng, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21650v2.pdf)  
  Keywords: 4d, high-fidelity, ar, vr, dynamic, gaussian splatting  
- **[STP4D: Spatio-Temporal-Prompt Consistent Modeling for Text-to-4D Gaussian Splatting](https://arxiv.org/abs/2504.18318v1)**  
  Authors: Yunze Deng, Haijun Xiong, Bin Feng, Xinggang Wang, Wenyu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18318v1.pdf)  
  Keywords: high-fidelity, ar, real-time rendering, deformation, 4d, gaussian splatting  
- **[When Gaussian Meets Surfel: Ultra-fast High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2504.17545v1)**  
  Authors: Keyang Ye, Tianjia Shao, Kun Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17545v1.pdf)  
  Keywords: geometry, high-fidelity, fast, ar, 3d gaussian, compact  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: quality enhancement, ar, 3d gaussian, nerf, real-time rendering, semantic, dynamic, human, gaussian splatting, lighting  
- **[CAGE-GS: High-fidelity Cage Based 3D Gaussian Splatting Deformation](https://arxiv.org/abs/2504.12800v1)**  
  Authors: Yifei Tong, Runze Tian, Xiao Han, Dingyao Liu, Fenggen Yu, Yan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12800v1.pdf)  
  Keywords: high-fidelity, ar, 3d gaussian, deformation, gaussian splatting  

### Ray Tracing

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: geometry, avatar, fast, shadow, ar, relightable, ray tracing, relighting, human, gaussian splatting, lighting  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: efficient rendering, efficient, ar, 3d gaussian, ray tracing, acceleration, relighting, gaussian splatting, lighting  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: efficient, ar, 3d gaussian, acceleration, ray marching, animation, compact, dynamic, gaussian splatting  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: face, efficient, ar, global illumination, 3d gaussian, illumination, ray tracing, real-time rendering, gaussian splatting, lighting  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: face, fast, global illumination, 3d gaussian, illumination, real-time rendering, dynamic, light transport, lighting  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: neural rendering, fast, shadow, ar, 3d gaussian, reflection, ray tracing, gaussian splatting  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: face, geometry, 4d, efficient, ar, relightable, ray tracing, real-time rendering, dynamic, lighting, tracking  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: face, shadow, reflection, ray tracing, gaussian splatting, lighting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ar, 3d gaussian, ray tracing, survey, gaussian splatting  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: efficient, ar, reflection, ray tracing, acceleration, light transport, gaussian splatting  

### Relighting

*Showing the latest 50 out of 198 papers*

- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d reconstruction, ar, 3d gaussian, survey, lighting  
- **[TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians](https://arxiv.org/abs/2504.18768v2)**  
  Authors: Letian Huang, Dongwei Ye, Jialin Dan, Chengzhi Tao, Huiwen Liu, Kun Zhou, Bo Ren, Yuanqi Li, Yanwen Guo, Jie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18768v2.pdf)  
  Keywords: efficient, fast, ar, reflection, 3d gaussian, gaussian splatting  
- **[RGS-DR: Reflective Gaussian Surfels with Deferred Rendering for Shiny Objects](https://arxiv.org/abs/2504.18468v3)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18468v3.pdf)  
  Keywords: face, geometry, ar, 3d gaussian, reflection, nerf, relighting, gaussian splatting, lighting  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: fast, ar, 3d gaussian, nerf, vr, mapping, gaussian splatting, lighting  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: quality enhancement, ar, 3d gaussian, nerf, real-time rendering, semantic, dynamic, human, gaussian splatting, lighting  
- **[Immersive Teleoperation Framework for Locomanipulation Tasks](https://arxiv.org/abs/2504.15229v1)**  
  Authors: Takuya Boehringer, Jonathan Embley-Riches, Karim Hammoud, Valerio Modugno, Dimitrios Kanoulas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15229v1.pdf)  
  Keywords: face, fast, ar, vr, gaussian splatting, lighting  
- **[Metamon-GS: Enhancing Representability with Variance-Guided Densification and Light Encoding](https://arxiv.org/abs/2504.14460v1)**  
  Authors: Junyan Su, Baozhu Zhao, Xiaohan Zhang, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14460v1.pdf)  
  Keywords: lighting, ar, gaussian splatting, 3d gaussian  
- **[SLAM&Render: A Benchmark for the Intersection Between Neural Rendering, Gaussian Splatting and SLAM](https://arxiv.org/abs/2504.13713v2)**  
  Authors: Samuel Cerezo, Gaetano Meli, Tomás Berriel Martins, Kirill Safronov, Javier Civera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13713v2.pdf)  
  Keywords: neural rendering, localization, slam, ar, illumination, nerf, mapping, gaussian splatting, lighting  
- **[Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation](https://arxiv.org/abs/2504.13175v1)**  
  Authors: Sizhe Yang, Wenye Yu, Jia Zeng, Jun Lv, Kerui Ren, Cewu Lu, Dahua Lin, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13175v1.pdf)  
  Keywords: face, ar, 3d gaussian, gaussian splatting, lighting  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: ar, 3d gaussian, survey, semantic, robotics, segmentation, gaussian splatting, lighting  

### SLAM

*Showing the latest 50 out of 263 papers*

- **[Large-Scale Gaussian Splatting SLAM](https://arxiv.org/abs/2505.09915v1)**  
  Authors: Zhe Xin, Chenyang Wu, Penghui Huang, Yanyong Zhang, Yinian Mao, Guoquan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09915v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lsg-slam.github.io.)  
  Keywords: recognition, outdoor, slam, ar, 3d gaussian, nerf, gaussian splatting, tracking  
- **[Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware](https://arxiv.org/abs/2505.09601v1)**  
  Authors: Justin Yu, Letian Fu, Huang Huang, Karim El-Refai, Rares Andrei Ambrus, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2render2real.com)  
  Keywords: geometry, ar, 3d gaussian, motion, dynamic, gaussian splatting, human, tracking  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v1)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v1.pdf)  
  Keywords: efficient, outdoor, localization, ar, mapping, dynamic, gaussian splatting, human  
- **[DLO-Splatting: Tracking Deformable Linear Objects Using 3D Gaussian Splatting](https://arxiv.org/abs/2505.08644v1)**  
  Authors: Holly Dinkel, Marcel Büsching, Alberta Longhini, Brian Coltin, Trey Smith, Danica Kragic, Mårten Björkman, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08644v1.pdf)  
  Keywords: ar, 3d gaussian, dynamic, gaussian splatting, tracking  
- **[Monocular Online Reconstruction with Enhanced Detail Preservation](https://arxiv.org/abs/2505.07887v2)**  
  Authors: Songyin Wu, Zhaoyang Lv, Yufeng Zhu, Duncan Frost, Zhengqin Li, Ling-Qi Yan, Carl Ren, Richard Newcombe, Zhao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07887v2.pdf)  
  Keywords: mapping, ar, 3d gaussian, tracking  
- **[Apply Hierarchical-Chain-of-Generation to Complex Attributes Text-to-3D Generation](https://arxiv.org/abs/2505.05505v1)**  
  Authors: Yiming Qin, Zhu Xu, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05505v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Wakals/GASCOL?style=social)](https://github.com/Wakals/GASCOL)  
  Keywords: ar, 3d gaussian, semantic, localization  
- **[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](https://arxiv.org/abs/2505.03351v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Yang Li, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03351v1.pdf)  
  Keywords: avatar, body, fast, ar, 3d gaussian, mapping, animation, motion, human, tracking  
- **[Creating Your Editable 3D Photorealistic Avatar with Tetrahedron-constrained Gaussian Splatting](https://arxiv.org/abs/2504.20403v1)**  
  Authors: Hanxi Liu, Yifang Men, Zhouhui Lian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20403v1.pdf)  
  Keywords: avatar, geometry, localization, ar, 3d gaussian, vr, gaussian splatting  
- **[GSFeatLoc: Visual Localization Using Feature Correspondence on 3D Gaussian Splatting](https://arxiv.org/abs/2504.20379v2)**  
  Authors: Jongwon Lee, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20379v2.pdf)  
  Keywords: localization, fast, ar, 3d gaussian, nerf, gaussian splatting  
- **[Mesh-Learner: Texturing Mesh with Spherical Harmonics](https://arxiv.org/abs/2504.19938v1)**  
  Authors: Yunfei Wan, Jianheng Liu, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/Mesh-Learner?style=social)](https://github.com/hku-mars/Mesh-Learner)  
  Keywords: efficient, fast, 3d reconstruction, ar, 3d gaussian, mapping, robotics, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 314 papers*

- **[Consistent Quantity-Quality Control across Scenes for Deployment-Aware Gaussian Splatting](https://arxiv.org/abs/2505.10473v1)**  
  Authors: Fengdi Zhang, Hongkun Cao, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10473v1.pdf)  
  Keywords: outdoor, ar, 3d gaussian, compact, semantic, gaussian splatting  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v1)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v1.pdf)  
  Keywords: 4d, body, ar, 3d gaussian, understanding, survey, motion, dynamic, gaussian splatting  
- **[Large-Scale Gaussian Splatting SLAM](https://arxiv.org/abs/2505.09915v1)**  
  Authors: Zhe Xin, Chenyang Wu, Penghui Huang, Yanyong Zhang, Yinian Mao, Guoquan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09915v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lsg-slam.github.io.)  
  Keywords: recognition, outdoor, slam, ar, 3d gaussian, nerf, gaussian splatting, tracking  
- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: high-fidelity, outdoor, ar, nerf, semantic, segmentation, gaussian splatting  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: autonomous driving, ar, 3d gaussian, nerf, survey, semantic, robotics  
- **[Apply Hierarchical-Chain-of-Generation to Complex Attributes Text-to-3D Generation](https://arxiv.org/abs/2505.05505v1)**  
  Authors: Yiming Qin, Zhu Xu, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05505v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Wakals/GASCOL?style=social)](https://github.com/Wakals/GASCOL)  
  Keywords: ar, 3d gaussian, semantic, localization  
- **[GSsplat: Generalizable Semantic Gaussian Splatting for Novel-view Synthesis in 3D Scenes](https://arxiv.org/abs/2505.04659v1)**  
  Authors: Feng Xiao, Hongbin Xu, Wanlin Liang, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04659v1.pdf)  
  Keywords: efficient, fast, ar, understanding, semantic, segmentation, gaussian splatting  
- **[FreeInsert: Disentangled Text-Guided Object Insertion in 3D Gaussian Scene without Spatial Priors](https://arxiv.org/abs/2505.01322v1)**  
  Authors: Chenxi Li, Weijie Wang, Qiang Li, Bruno Lepri, Nicu Sebe, Weizhi Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01322v1.pdf)  
  Keywords: ar, 3d gaussian, semantic  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: face, geometry, outdoor, 3d reconstruction, ar, sparse view, 3d gaussian, nerf, understanding, survey, gaussian splatting  
- **[GSFF-SLAM: 3D Semantic Gaussian Splatting SLAM via Feature Field](https://arxiv.org/abs/2504.19409v1)**  
  Authors: Zuxing Lu, Xin Yuan, Shaowen Yang, Jingyu Liu, Jiawei Wang, Changyin Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19409v1.pdf)  
  Keywords: geometry, slam, ar, 3d gaussian, mapping, semantic, segmentation, gaussian splatting, tracking  



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