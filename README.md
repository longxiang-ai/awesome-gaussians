# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-05-16 00:55:35

## Categories

- [3DGS Surveys](#3dgs-surveys) (32 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (505 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1757 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (592 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (666 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (124 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (569 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (96 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (669 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (279 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (40 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (198 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (262 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (311 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[A Survey of 3D Reconstruction with Event Cameras: From Event-based Geometry to Neural 3D Rendering](https://arxiv.org/abs/2505.08438v1)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, geometry, motion, gaussian splatting, survey, neural rendering, ar, dynamic  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: fast, 3d reconstruction, gaussian splatting, survey, ar, efficient  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: autonomous driving, semantic, 3d gaussian, survey, ar, nerf, robotics  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, survey, lighting, ar  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: 3d gaussian, 3d reconstruction, geometry, gaussian splatting, survey, sparse view, ar, nerf, face, understanding, outdoor  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: segmentation, semantic, 3d gaussian, gaussian splatting, survey, lighting, ar, robotics  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: fast, 3d gaussian, 3d reconstruction, motion, gaussian splatting, survey, lighting, ar, dynamic  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, gaussian splatting, survey, ar, dynamic  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: ar, semantic, survey, geometry  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, 3d reconstruction, gaussian splatting, survey, ar, nerf, compression, efficient  

### Acceleration

*Showing the latest 50 out of 505 papers*

- **[FOCI: Trajectory Optimization on Gaussian Splats](https://arxiv.org/abs/2505.08510v1)**  
  Authors: Mario Gomez Andreu, Maximum Wilder-Smith, Victor Klemm, Vaishakh Patil, Jesus Tordesillas, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08510v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/foci/)  
  Keywords: fast, 3d gaussian, 3d reconstruction, gaussian splatting, ar, nerf, robotics  
- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539v1)**  
  Authors: Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07539v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xdimlab.github.io/GIFStream)  
  Keywords: real-time rendering, fast, gaussian splatting, deformation, ar, compression, efficient, motion, 4d  
- **[TUGS: Physics-based Compact Representation of Underwater Scenes by Tensorized Gaussian](https://arxiv.org/abs/2505.08811v1)**  
  Authors: Shijie Lian, Ziyi Zhang, Laurence Tianruo Yang and, Mengyu Ren, Debin Liu, Hua Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08811v1.pdf)  
  Keywords: fast, gaussian splatting, ar, nerf, face, compact, efficient, lightweight  
- **[Virtualized 3D Gaussians: Flexible Cluster-based Level-of-Detail System for Real-Time Rendering of Composed Scenes](https://arxiv.org/abs/2505.06523v1)**  
  Authors: Xijie Yang, Linning Xu, Lihan Jiang, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.06523v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, gaussian splatting, ar, efficient, dynamic  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: fast, 3d reconstruction, gaussian splatting, survey, ar, efficient  
- **[QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization](https://arxiv.org/abs/2505.05591v1)**  
  Authors: Yueh-Cheng Liu, Lukas Höllein, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05591v1.pdf)  
  Keywords: fast, geometry, gaussian splatting, ar, face, robotics  
- **[Steepest Descent Density Control for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2505.05587v1)**  
  Authors: Peihao Wang, Yuehao Wang, Dilin Wang, Sreyas Mohan, Zhiwen Fan, Lemeng Wu, Ruisi Cai, Yu-Ying Yeh, Zhangyang Wang, Qiang Liu, Rakesh Ranjan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05587v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, efficient rendering, ar, compact, efficient  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: real-time rendering, avatar, 3d gaussian, gaussian splatting, high-fidelity, ar, human, face, animation  
- **[Time of the Flight of the Gaussians: Optimizing Depth Indirectly in Dynamic Radiance Fields](https://arxiv.org/abs/2505.05356v1)**  
  Authors: Runfeng Li, Mikhail Okunev, Zixuan Guo, Anh Ha Duong, Christian Richardt, Matthew O'Toole, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05356v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://visual.cs.brown.edu/gftorf)  
  Keywords: fast, 3d gaussian, 3d reconstruction, geometry, motion, gaussian splatting, high-fidelity, ar, dynamic  
- **[SGCR: Spherical Gaussians for Efficient 3D Curve Reconstruction](https://arxiv.org/abs/2505.04668v1)**  
  Authors: Xinran Yang, Donghao Ji, Yuanqi Li, Jie Guo, Yanwen Guo, Junyuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04668v1.pdf)  
  Keywords: fast, 3d gaussian, 3d reconstruction, gaussian splatting, high quality, neural rendering, ar, efficient  

### Applications

*Showing the latest 50 out of 1757 papers*

- **[Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware](https://arxiv.org/abs/2505.09601v1)**  
  Authors: Justin Yu, Letian Fu, Huang Huang, Karim El-Refai, Rares Andrei Ambrus, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2render2real.com)  
  Keywords: geometry, 3d gaussian, motion, gaussian splatting, ar, human, dynamic, tracking  
- **[Sparse Point Cloud Patches Rendering via Splitting 2D Gaussians](https://arxiv.org/abs/2505.09413v1)**  
  Authors: Ma Changfeng, Bi Ran, Guo Jie, Wang Chongjun, Guo Yanwen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09413v1.pdf) | [![GitHub](https://img.shields.io/github/stars/murcherful/GauPCRender?style=social)](https://github.com/murcherful/GauPCRender)  
  Keywords: ar, nerf, 3d gaussian  
- **[Neural Video Compression using 2D Gaussian Splatting](https://arxiv.org/abs/2505.09324v1)**  
  Authors: Lakshya Gupta, Imran N. Junejo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09324v1.pdf)  
  Keywords: compression, motion, gaussian splatting, ar  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v1)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v1.pdf)  
  Keywords: localization, gaussian splatting, ar, human, mapping, efficient, dynamic, outdoor  
- **[DLO-Splatting: Tracking Deformable Linear Objects Using 3D Gaussian Splatting](https://arxiv.org/abs/2505.08644v1)**  
  Authors: Holly Dinkel, Marcel Büsching, Alberta Longhini, Brian Coltin, Trey Smith, Danica Kragic, Mårten Björkman, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08644v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, dynamic, tracking  
- **[FOCI: Trajectory Optimization on Gaussian Splats](https://arxiv.org/abs/2505.08510v1)**  
  Authors: Mario Gomez Andreu, Maximum Wilder-Smith, Victor Klemm, Vaishakh Patil, Jesus Tordesillas, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08510v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/foci/)  
  Keywords: fast, 3d gaussian, 3d reconstruction, gaussian splatting, ar, nerf, robotics  
- **[A Survey of 3D Reconstruction with Event Cameras: From Event-based Geometry to Neural 3D Rendering](https://arxiv.org/abs/2505.08438v1)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, geometry, motion, gaussian splatting, survey, neural rendering, ar, dynamic  
- **[ADC-GS: Anchor-Driven Deformable and Compressed Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2505.08196v1)**  
  Authors: He Huang, Qi Yang, Mufan Liu, Yiling Xu, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08196v1.pdf) | [![GitHub](https://img.shields.io/github/stars/H-Huang774/ADC-GS.git?style=social)](https://github.com/H-Huang774/ADC-GS.git)  
  Keywords: motion, gaussian splatting, deformation, ar, compact, efficient, dynamic, 4d  
- **[SLAG: Scalable Language-Augmented Gaussian Splatting](https://arxiv.org/abs/2505.08124v1)**  
  Authors: Laszlo Szilagyi, Francis Engelmann, Jeannette Bohg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08124v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://slag-project.github.io/.)  
  Keywords: 3d gaussian, large scene, gaussian splatting, ar, robotics, efficient  
- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539v1)**  
  Authors: Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07539v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xdimlab.github.io/GIFStream)  
  Keywords: real-time rendering, fast, gaussian splatting, deformation, ar, compression, efficient, motion, 4d  

### Avatar Generation

*Showing the latest 50 out of 592 papers*

- **[Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware](https://arxiv.org/abs/2505.09601v1)**  
  Authors: Justin Yu, Letian Fu, Huang Huang, Karim El-Refai, Rares Andrei Ambrus, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2render2real.com)  
  Keywords: geometry, 3d gaussian, motion, gaussian splatting, ar, human, dynamic, tracking  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v1)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v1.pdf)  
  Keywords: localization, gaussian splatting, ar, human, mapping, efficient, dynamic, outdoor  
- **[TUGS: Physics-based Compact Representation of Underwater Scenes by Tensorized Gaussian](https://arxiv.org/abs/2505.08811v1)**  
  Authors: Shijie Lian, Ziyi Zhang, Laurence Tianruo Yang and, Mengyu Ren, Debin Liu, Hua Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08811v1.pdf)  
  Keywords: fast, gaussian splatting, ar, nerf, face, compact, efficient, lightweight  
- **[TeGA: Texture Space Gaussian Avatars for High-Resolution Dynamic Head Modeling](https://arxiv.org/abs/2505.05672v1)**  
  Authors: Gengyan Li, Paulo Gotardo, Timo Bolkart, Stephan Garbin, Kripasindhu Sarkar, Abhimitra Meka, Alexandros Lattas, Thabo Beeler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05672v1.pdf)  
  Keywords: avatar, 3d gaussian, motion, gaussian splatting, head, deformation, ar, dynamic  
- **[QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization](https://arxiv.org/abs/2505.05591v1)**  
  Authors: Yueh-Cheng Liu, Lukas Höllein, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05591v1.pdf)  
  Keywords: fast, geometry, gaussian splatting, ar, face, robotics  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: real-time rendering, avatar, 3d gaussian, gaussian splatting, high-fidelity, ar, human, face, animation  
- **[Bridging Geometry-Coherent Text-to-3D Generation with Multi-View Diffusion Priors and Gaussian Splatting](https://arxiv.org/abs/2505.04262v1)**  
  Authors: Feng Yang, Wenliang Qian, Wangmeng Zuo, Hui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04262v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, ar, face  
- **[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](https://arxiv.org/abs/2505.03351v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Yang Li, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03351v1.pdf)  
  Keywords: fast, avatar, 3d gaussian, body, ar, human, mapping, animation, motion, tracking  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: fast, geometry, gaussian splatting, sparse view, shape reconstruction, ar, face, efficient, head  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: fast, geometry, 3d gaussian, 3d reconstruction, sparse-view, gaussian splatting, sparse view, shape reconstruction, ar, face  

### Dynamic Scene

*Showing the latest 50 out of 666 papers*

- **[Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware](https://arxiv.org/abs/2505.09601v1)**  
  Authors: Justin Yu, Letian Fu, Huang Huang, Karim El-Refai, Rares Andrei Ambrus, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2render2real.com)  
  Keywords: geometry, 3d gaussian, motion, gaussian splatting, ar, human, dynamic, tracking  
- **[Neural Video Compression using 2D Gaussian Splatting](https://arxiv.org/abs/2505.09324v1)**  
  Authors: Lakshya Gupta, Imran N. Junejo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09324v1.pdf)  
  Keywords: compression, motion, gaussian splatting, ar  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v1)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v1.pdf)  
  Keywords: localization, gaussian splatting, ar, human, mapping, efficient, dynamic, outdoor  
- **[DLO-Splatting: Tracking Deformable Linear Objects Using 3D Gaussian Splatting](https://arxiv.org/abs/2505.08644v1)**  
  Authors: Holly Dinkel, Marcel Büsching, Alberta Longhini, Brian Coltin, Trey Smith, Danica Kragic, Mårten Björkman, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08644v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, dynamic, tracking  
- **[A Survey of 3D Reconstruction with Event Cameras: From Event-based Geometry to Neural 3D Rendering](https://arxiv.org/abs/2505.08438v1)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, geometry, motion, gaussian splatting, survey, neural rendering, ar, dynamic  
- **[ADC-GS: Anchor-Driven Deformable and Compressed Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2505.08196v1)**  
  Authors: He Huang, Qi Yang, Mufan Liu, Yiling Xu, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08196v1.pdf) | [![GitHub](https://img.shields.io/github/stars/H-Huang774/ADC-GS.git?style=social)](https://github.com/H-Huang774/ADC-GS.git)  
  Keywords: motion, gaussian splatting, deformation, ar, compact, efficient, dynamic, 4d  
- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539v1)**  
  Authors: Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07539v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xdimlab.github.io/GIFStream)  
  Keywords: real-time rendering, fast, gaussian splatting, deformation, ar, compression, efficient, motion, 4d  
- **[Virtualized 3D Gaussians: Flexible Cluster-based Level-of-Detail System for Real-Time Rendering of Composed Scenes](https://arxiv.org/abs/2505.06523v1)**  
  Authors: Xijie Yang, Linning Xu, Lihan Jiang, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.06523v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, gaussian splatting, ar, efficient, dynamic  
- **[TeGA: Texture Space Gaussian Avatars for High-Resolution Dynamic Head Modeling](https://arxiv.org/abs/2505.05672v1)**  
  Authors: Gengyan Li, Paulo Gotardo, Timo Bolkart, Stephan Garbin, Kripasindhu Sarkar, Abhimitra Meka, Alexandros Lattas, Thabo Beeler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05672v1.pdf)  
  Keywords: avatar, 3d gaussian, motion, gaussian splatting, head, deformation, ar, dynamic  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: real-time rendering, avatar, 3d gaussian, gaussian splatting, high-fidelity, ar, human, face, animation  

### Few-shot

*Showing the latest 50 out of 124 papers*

- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: fast, geometry, gaussian splatting, sparse view, shape reconstruction, ar, face, efficient, head  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: fast, geometry, 3d gaussian, 3d reconstruction, sparse-view, gaussian splatting, sparse view, shape reconstruction, ar, face  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: 3d gaussian, 3d reconstruction, geometry, gaussian splatting, survey, sparse view, ar, nerf, face, understanding, outdoor  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: fast, geometry, sparse-view, gaussian splatting, sparse view, ar, nerf, face, motion  
- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v2)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v2.pdf)  
  Keywords: body, gaussian splatting, ar, few-shot, efficient, dynamic  
- **[IXGS-Intraoperative 3D Reconstruction from Sparse, Arbitrarily Posed Real X-rays](https://arxiv.org/abs/2504.14699v1)**  
  Authors: Sascha Jecklin, Aidana Massalimova, Ruyi Zha, Lilian Calvet, Christoph J. Laux, Mazda Farshad, Philipp Fürnstahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14699v1.pdf)  
  Keywords: ar, gaussian splatting, sparse-view, 3d reconstruction  
- **[VGNC: Reducing the Overfitting of Sparse-view 3DGS via Validation-guided Gaussian Number Control](https://arxiv.org/abs/2504.14548v1)**  
  Authors: Lifeng Lin, Rongfeng Lu, Quan Chen, Haofan Ren, Ming Lu, Yaoqi Sun, Chenggang Yan, Anke Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14548v1.pdf)  
  Keywords: sparse-view, 3d gaussian, 3d reconstruction, gaussian splatting, ar  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: geometry, 3d gaussian, sparse-view, gaussian splatting, ar, efficient, outdoor  
- **[DropoutGS: Dropping Out Gaussians for Better Sparse-view Rendering](https://arxiv.org/abs/2504.09491v1)**  
  Authors: Yexing Xu, Longguang Wang, Minglin Chen, Sheng Ao, Li Li, Yulan Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuyx55.github.io/DropoutGS/.)  
  Keywords: sparse-view, 3d gaussian, gaussian splatting, sparse view, ar  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: avatar, 3d gaussian, sparse-view, body, ar, human, head  

### Geometry Reconstruction

*Showing the latest 50 out of 569 papers*

- **[Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware](https://arxiv.org/abs/2505.09601v1)**  
  Authors: Justin Yu, Letian Fu, Huang Huang, Karim El-Refai, Rares Andrei Ambrus, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2render2real.com)  
  Keywords: geometry, 3d gaussian, motion, gaussian splatting, ar, human, dynamic, tracking  
- **[FOCI: Trajectory Optimization on Gaussian Splats](https://arxiv.org/abs/2505.08510v1)**  
  Authors: Mario Gomez Andreu, Maximum Wilder-Smith, Victor Klemm, Vaishakh Patil, Jesus Tordesillas, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08510v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/foci/)  
  Keywords: fast, 3d gaussian, 3d reconstruction, gaussian splatting, ar, nerf, robotics  
- **[A Survey of 3D Reconstruction with Event Cameras: From Event-based Geometry to Neural 3D Rendering](https://arxiv.org/abs/2505.08438v1)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, geometry, motion, gaussian splatting, survey, neural rendering, ar, dynamic  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: fast, 3d reconstruction, gaussian splatting, survey, ar, efficient  
- **[QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization](https://arxiv.org/abs/2505.05591v1)**  
  Authors: Yueh-Cheng Liu, Lukas Höllein, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05591v1.pdf)  
  Keywords: fast, geometry, gaussian splatting, ar, face, robotics  
- **[Time of the Flight of the Gaussians: Optimizing Depth Indirectly in Dynamic Radiance Fields](https://arxiv.org/abs/2505.05356v1)**  
  Authors: Runfeng Li, Mikhail Okunev, Zixuan Guo, Anh Ha Duong, Christian Richardt, Matthew O'Toole, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05356v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://visual.cs.brown.edu/gftorf)  
  Keywords: fast, 3d gaussian, 3d reconstruction, geometry, motion, gaussian splatting, high-fidelity, ar, dynamic  
- **[Bridging Geometry-Coherent Text-to-3D Generation with Multi-View Diffusion Priors and Gaussian Splatting](https://arxiv.org/abs/2505.04262v1)**  
  Authors: Feng Yang, Wenliang Qian, Wangmeng Zuo, Hui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04262v1.pdf)  
  Keywords: geometry, 3d gaussian, gaussian splatting, ar, face  
- **[SGCR: Spherical Gaussians for Efficient 3D Curve Reconstruction](https://arxiv.org/abs/2505.04668v1)**  
  Authors: Xinran Yang, Donghao Ji, Yuanqi Li, Jie Guo, Yanwen Guo, Junyuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04668v1.pdf)  
  Keywords: fast, 3d gaussian, 3d reconstruction, gaussian splatting, high quality, neural rendering, ar, efficient  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: fast, geometry, gaussian splatting, sparse view, shape reconstruction, ar, face, efficient, head  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: fast, geometry, 3d gaussian, 3d reconstruction, sparse-view, gaussian splatting, sparse view, shape reconstruction, ar, face  

### Large Scene

*Showing the latest 50 out of 96 papers*

- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v1)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v1.pdf)  
  Keywords: localization, gaussian splatting, ar, human, mapping, efficient, dynamic, outdoor  
- **[SLAG: Scalable Language-Augmented Gaussian Splatting](https://arxiv.org/abs/2505.08124v1)**  
  Authors: Laszlo Szilagyi, Francis Engelmann, Jeannette Bohg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08124v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://slag-project.github.io/.)  
  Keywords: 3d gaussian, large scene, gaussian splatting, ar, robotics, efficient  
- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: segmentation, semantic, gaussian splatting, high-fidelity, ar, nerf, outdoor  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: 3d gaussian, 3d reconstruction, geometry, gaussian splatting, survey, sparse view, ar, nerf, face, understanding, outdoor  
- **[HUG: Hierarchical Urban Gaussian Splatting with Block-Based Reconstruction](https://arxiv.org/abs/2504.16606v1)**  
  Authors: Zhongtao Wang, Mai Su, Huishan Au, Yilong Li, Xizhe Cao, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16606v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, urban scene, ar, efficient  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: geometry, 3d gaussian, sparse-view, gaussian splatting, ar, efficient, outdoor  
- **[You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting](https://arxiv.org/abs/2504.09062v1)**  
  Authors: Zhijie Shen, Chunyu Lin, Shujuan Huang, Lang Nie, Kang Liao, Yao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09062v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhijieshen-bjtu/TPGS?style=social)](https://github.com/zhijieshen-bjtu/TPGS)  
  Keywords: 3d gaussian, 3d reconstruction, gaussian splatting, ar, face, outdoor  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: reflection, gaussian splatting, ar, nerf, motion, outdoor  
- **[UnIRe: Unsupervised Instance Decomposition for Dynamic Urban Scene Reconstruction](https://arxiv.org/abs/2504.00763v1)**  
  Authors: Yunxuan Mao, Rong Xiong, Yue Wang, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00763v1.pdf)  
  Keywords: autonomous driving, 3d gaussian, gaussian splatting, urban scene, ar, dynamic, 4d  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: fast, reflection, geometry, gaussian splatting, high-fidelity, ar, nerf, efficient, dynamic, outdoor  

### Model Compression

*Showing the latest 50 out of 669 papers*

- **[Neural Video Compression using 2D Gaussian Splatting](https://arxiv.org/abs/2505.09324v1)**  
  Authors: Lakshya Gupta, Imran N. Junejo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09324v1.pdf)  
  Keywords: compression, motion, gaussian splatting, ar  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v1)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v1.pdf)  
  Keywords: localization, gaussian splatting, ar, human, mapping, efficient, dynamic, outdoor  
- **[ADC-GS: Anchor-Driven Deformable and Compressed Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2505.08196v1)**  
  Authors: He Huang, Qi Yang, Mufan Liu, Yiling Xu, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08196v1.pdf) | [![GitHub](https://img.shields.io/github/stars/H-Huang774/ADC-GS.git?style=social)](https://github.com/H-Huang774/ADC-GS.git)  
  Keywords: motion, gaussian splatting, deformation, ar, compact, efficient, dynamic, 4d  
- **[SLAG: Scalable Language-Augmented Gaussian Splatting](https://arxiv.org/abs/2505.08124v1)**  
  Authors: Laszlo Szilagyi, Francis Engelmann, Jeannette Bohg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08124v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://slag-project.github.io/.)  
  Keywords: 3d gaussian, large scene, gaussian splatting, ar, robotics, efficient  
- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539v1)**  
  Authors: Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07539v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xdimlab.github.io/GIFStream)  
  Keywords: real-time rendering, fast, gaussian splatting, deformation, ar, compression, efficient, motion, 4d  
- **[TUGS: Physics-based Compact Representation of Underwater Scenes by Tensorized Gaussian](https://arxiv.org/abs/2505.08811v1)**  
  Authors: Shijie Lian, Ziyi Zhang, Laurence Tianruo Yang and, Mengyu Ren, Debin Liu, Hua Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08811v1.pdf)  
  Keywords: fast, gaussian splatting, ar, nerf, face, compact, efficient, lightweight  
- **[Virtualized 3D Gaussians: Flexible Cluster-based Level-of-Detail System for Real-Time Rendering of Composed Scenes](https://arxiv.org/abs/2505.06523v1)**  
  Authors: Xijie Yang, Linning Xu, Lihan Jiang, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.06523v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, gaussian splatting, ar, efficient, dynamic  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: fast, 3d reconstruction, gaussian splatting, survey, ar, efficient  
- **[Steepest Descent Density Control for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2505.05587v1)**  
  Authors: Peihao Wang, Yuehao Wang, Dilin Wang, Sreyas Mohan, Zhiwen Fan, Lemeng Wu, Ruisi Cai, Yu-Ying Yeh, Zhangyang Wang, Qiang Liu, Rakesh Ranjan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05587v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, efficient rendering, ar, compact, efficient  
- **[SGCR: Spherical Gaussians for Efficient 3D Curve Reconstruction](https://arxiv.org/abs/2505.04668v1)**  
  Authors: Xinran Yang, Donghao Ji, Yuanqi Li, Jie Guo, Yanwen Guo, Junyuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04668v1.pdf)  
  Keywords: fast, 3d gaussian, 3d reconstruction, gaussian splatting, high quality, neural rendering, ar, efficient  

### Quality Enhancement

*Showing the latest 50 out of 279 papers*

- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: segmentation, semantic, gaussian splatting, high-fidelity, ar, nerf, outdoor  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: real-time rendering, avatar, 3d gaussian, gaussian splatting, high-fidelity, ar, human, face, animation  
- **[Time of the Flight of the Gaussians: Optimizing Depth Indirectly in Dynamic Radiance Fields](https://arxiv.org/abs/2505.05356v1)**  
  Authors: Runfeng Li, Mikhail Okunev, Zixuan Guo, Anh Ha Duong, Christian Richardt, Matthew O'Toole, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05356v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://visual.cs.brown.edu/gftorf)  
  Keywords: fast, 3d gaussian, 3d reconstruction, geometry, motion, gaussian splatting, high-fidelity, ar, dynamic  
- **[SGCR: Spherical Gaussians for Efficient 3D Curve Reconstruction](https://arxiv.org/abs/2505.04668v1)**  
  Authors: Xinran Yang, Donghao Ji, Yuanqi Li, Jie Guo, Yanwen Guo, Junyuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04668v1.pdf)  
  Keywords: fast, 3d gaussian, 3d reconstruction, gaussian splatting, high quality, neural rendering, ar, efficient  
- **[GarmentGS: Point-Cloud Guided Gaussian Splatting for High-Fidelity Non-Watertight 3D Garment Reconstruction](https://arxiv.org/abs/2505.02126v2)**  
  Authors: Zhihao Tang, Shenghao Yang, Hongtao Zhang, Mingbo Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02126v2.pdf)  
  Keywords: real-time rendering, fast, 3d gaussian, gaussian splatting, high-fidelity, ar, face  
- **[HoloTime: Taming Video Diffusion Models for Panoramic 4D Scene Generation](https://arxiv.org/abs/2504.21650v2)**  
  Authors: Haiyang Zhou, Wangbo Yu, Jiawen Guan, Xinhua Cheng, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21650v2.pdf)  
  Keywords: vr, gaussian splatting, high-fidelity, ar, dynamic, 4d  
- **[STP4D: Spatio-Temporal-Prompt Consistent Modeling for Text-to-4D Gaussian Splatting](https://arxiv.org/abs/2504.18318v1)**  
  Authors: Yunze Deng, Haijun Xiong, Bin Feng, Xinggang Wang, Wenyu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18318v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, deformation, high-fidelity, ar, 4d  
- **[When Gaussian Meets Surfel: Ultra-fast High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2504.17545v1)**  
  Authors: Keyang Ye, Tianjia Shao, Kun Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17545v1.pdf)  
  Keywords: fast, geometry, 3d gaussian, high-fidelity, ar, compact  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: quality enhancement, real-time rendering, semantic, 3d gaussian, gaussian splatting, lighting, ar, human, nerf, dynamic  
- **[CAGE-GS: High-fidelity Cage Based 3D Gaussian Splatting Deformation](https://arxiv.org/abs/2504.12800v1)**  
  Authors: Yifei Tong, Runze Tian, Xiao Han, Dingyao Liu, Fenggen Yu, Yan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12800v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, deformation, high-fidelity, ar  

### Ray Tracing

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: fast, avatar, geometry, shadow, gaussian splatting, relightable, lighting, relighting, human, ar, ray tracing  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, efficient rendering, lighting, relighting, ar, ray tracing, acceleration, efficient  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: 3d gaussian, ray marching, gaussian splatting, ar, compact, acceleration, animation, efficient, dynamic  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: global illumination, real-time rendering, 3d gaussian, gaussian splatting, lighting, ar, illumination, face, ray tracing, efficient  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: global illumination, real-time rendering, fast, 3d gaussian, lighting, illumination, face, dynamic, light transport  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: fast, 3d gaussian, reflection, shadow, gaussian splatting, neural rendering, ar, ray tracing  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: real-time rendering, geometry, relightable, lighting, ar, face, ray tracing, efficient, dynamic, 4d, tracking  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: reflection, shadow, gaussian splatting, lighting, face, ray tracing  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, survey, ar, ray tracing  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: reflection, gaussian splatting, ar, ray tracing, acceleration, efficient, light transport  

### Relighting

*Showing the latest 50 out of 198 papers*

- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d gaussian, 3d reconstruction, survey, lighting, ar  
- **[TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians](https://arxiv.org/abs/2504.18768v2)**  
  Authors: Letian Huang, Dongwei Ye, Jialin Dan, Chengzhi Tao, Huiwen Liu, Kun Zhou, Bo Ren, Yuanqi Li, Yanwen Guo, Jie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18768v2.pdf)  
  Keywords: fast, 3d gaussian, reflection, gaussian splatting, ar, efficient  
- **[RGS-DR: Reflective Gaussian Surfels with Deferred Rendering for Shiny Objects](https://arxiv.org/abs/2504.18468v3)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18468v3.pdf)  
  Keywords: 3d gaussian, reflection, geometry, gaussian splatting, lighting, relighting, ar, nerf, face  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: vr, fast, 3d gaussian, gaussian splatting, lighting, ar, nerf, mapping  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: quality enhancement, real-time rendering, semantic, 3d gaussian, gaussian splatting, lighting, ar, human, nerf, dynamic  
- **[Immersive Teleoperation Framework for Locomanipulation Tasks](https://arxiv.org/abs/2504.15229v1)**  
  Authors: Takuya Boehringer, Jonathan Embley-Riches, Karim Hammoud, Valerio Modugno, Dimitrios Kanoulas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15229v1.pdf)  
  Keywords: vr, fast, gaussian splatting, lighting, ar, face  
- **[Metamon-GS: Enhancing Representability with Variance-Guided Densification and Light Encoding](https://arxiv.org/abs/2504.14460v1)**  
  Authors: Junyan Su, Baozhu Zhao, Xiaohan Zhang, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14460v1.pdf)  
  Keywords: lighting, ar, gaussian splatting, 3d gaussian  
- **[SLAM&Render: A Benchmark for the Intersection Between Neural Rendering, Gaussian Splatting and SLAM](https://arxiv.org/abs/2504.13713v2)**  
  Authors: Samuel Cerezo, Gaetano Meli, Tomás Berriel Martins, Kirill Safronov, Javier Civera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13713v2.pdf)  
  Keywords: localization, gaussian splatting, neural rendering, lighting, ar, nerf, illumination, mapping, slam  
- **[Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation](https://arxiv.org/abs/2504.13175v1)**  
  Authors: Sizhe Yang, Wenye Yu, Jia Zeng, Jun Lv, Kerui Ren, Cewu Lu, Dahua Lin, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13175v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, lighting, ar, face  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: segmentation, semantic, 3d gaussian, gaussian splatting, survey, lighting, ar, robotics  

### SLAM

*Showing the latest 50 out of 262 papers*

- **[Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware](https://arxiv.org/abs/2505.09601v1)**  
  Authors: Justin Yu, Letian Fu, Huang Huang, Karim El-Refai, Rares Andrei Ambrus, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2render2real.com)  
  Keywords: geometry, 3d gaussian, motion, gaussian splatting, ar, human, dynamic, tracking  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v1)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v1.pdf)  
  Keywords: localization, gaussian splatting, ar, human, mapping, efficient, dynamic, outdoor  
- **[DLO-Splatting: Tracking Deformable Linear Objects Using 3D Gaussian Splatting](https://arxiv.org/abs/2505.08644v1)**  
  Authors: Holly Dinkel, Marcel Büsching, Alberta Longhini, Brian Coltin, Trey Smith, Danica Kragic, Mårten Björkman, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08644v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, dynamic, tracking  
- **[Monocular Online Reconstruction with Enhanced Detail Preservation](https://arxiv.org/abs/2505.07887v2)**  
  Authors: Songyin Wu, Zhaoyang Lv, Yufeng Zhu, Duncan Frost, Zhengqin Li, Ling-Qi Yan, Carl Ren, Richard Newcombe, Zhao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07887v2.pdf)  
  Keywords: tracking, ar, mapping, 3d gaussian  
- **[Apply Hierarchical-Chain-of-Generation to Complex Attributes Text-to-3D Generation](https://arxiv.org/abs/2505.05505v1)**  
  Authors: Yiming Qin, Zhu Xu, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05505v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Wakals/GASCOL?style=social)](https://github.com/Wakals/GASCOL)  
  Keywords: localization, semantic, 3d gaussian, ar  
- **[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](https://arxiv.org/abs/2505.03351v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Yang Li, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03351v1.pdf)  
  Keywords: fast, avatar, 3d gaussian, body, ar, human, mapping, animation, motion, tracking  
- **[Creating Your Editable 3D Photorealistic Avatar with Tetrahedron-constrained Gaussian Splatting](https://arxiv.org/abs/2504.20403v1)**  
  Authors: Hanxi Liu, Yifang Men, Zhouhui Lian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20403v1.pdf)  
  Keywords: localization, vr, avatar, geometry, 3d gaussian, gaussian splatting, ar  
- **[GSFeatLoc: Visual Localization Using Feature Correspondence on 3D Gaussian Splatting](https://arxiv.org/abs/2504.20379v2)**  
  Authors: Jongwon Lee, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20379v2.pdf)  
  Keywords: localization, fast, 3d gaussian, gaussian splatting, ar, nerf  
- **[Mesh-Learner: Texturing Mesh with Spherical Harmonics](https://arxiv.org/abs/2504.19938v1)**  
  Authors: Yunfei Wan, Jianheng Liu, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/Mesh-Learner?style=social)](https://github.com/hku-mars/Mesh-Learner)  
  Keywords: fast, 3d gaussian, 3d reconstruction, gaussian splatting, ar, mapping, robotics, efficient  
- **[GSFF-SLAM: 3D Semantic Gaussian Splatting SLAM via Feature Field](https://arxiv.org/abs/2504.19409v1)**  
  Authors: Zuxing Lu, Xin Yuan, Shaowen Yang, Jingyu Liu, Jiawei Wang, Changyin Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19409v1.pdf)  
  Keywords: segmentation, semantic, geometry, 3d gaussian, gaussian splatting, ar, mapping, slam, tracking  

### Scene Understanding

*Showing the latest 50 out of 311 papers*

- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: segmentation, semantic, gaussian splatting, high-fidelity, ar, nerf, outdoor  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: autonomous driving, semantic, 3d gaussian, survey, ar, nerf, robotics  
- **[Apply Hierarchical-Chain-of-Generation to Complex Attributes Text-to-3D Generation](https://arxiv.org/abs/2505.05505v1)**  
  Authors: Yiming Qin, Zhu Xu, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05505v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Wakals/GASCOL?style=social)](https://github.com/Wakals/GASCOL)  
  Keywords: localization, semantic, 3d gaussian, ar  
- **[GSsplat: Generalizable Semantic Gaussian Splatting for Novel-view Synthesis in 3D Scenes](https://arxiv.org/abs/2505.04659v1)**  
  Authors: Feng Xiao, Hongbin Xu, Wanlin Liang, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04659v1.pdf)  
  Keywords: segmentation, semantic, fast, gaussian splatting, ar, understanding, efficient  
- **[FreeInsert: Disentangled Text-Guided Object Insertion in 3D Gaussian Scene without Spatial Priors](https://arxiv.org/abs/2505.01322v1)**  
  Authors: Chenxi Li, Weijie Wang, Qiang Li, Bruno Lepri, Nicu Sebe, Weizhi Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01322v1.pdf)  
  Keywords: ar, semantic, 3d gaussian  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: 3d gaussian, 3d reconstruction, geometry, gaussian splatting, survey, sparse view, ar, nerf, face, understanding, outdoor  
- **[GSFF-SLAM: 3D Semantic Gaussian Splatting SLAM via Feature Field](https://arxiv.org/abs/2504.19409v1)**  
  Authors: Zuxing Lu, Xin Yuan, Shaowen Yang, Jingyu Liu, Jiawei Wang, Changyin Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19409v1.pdf)  
  Keywords: segmentation, semantic, geometry, 3d gaussian, gaussian splatting, ar, mapping, slam, tracking  
- **[Visibility-Uncertainty-guided 3D Gaussian Inpainting via Scene Conceptional Learning](https://arxiv.org/abs/2504.17815v1)**  
  Authors: Mingxuan Cui, Qing Guo, Yuyi Wang, Hongkai Yu, Di Lin, Qin Zou, Ming-Ming Cheng, Xi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17815v1.pdf)  
  Keywords: semantic, fast, 3d gaussian, gaussian splatting, ar, nerf, efficient, dynamic  
- **[Text-based Animatable 3D Avatars with Morphable Model Alignment](https://arxiv.org/abs/2504.15835v1)**  
  Authors: Yiqian Wu, Malte Prinzler, Xiaogang Jin, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15835v1.pdf)  
  Keywords: semantic, avatar, geometry, head, ar, animation, dynamic  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: quality enhancement, real-time rendering, semantic, 3d gaussian, gaussian splatting, lighting, ar, human, nerf, dynamic  



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