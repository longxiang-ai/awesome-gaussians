# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-05-14 00:54:37

## Categories

- [3DGS Surveys](#3dgs-surveys) (31 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (503 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1746 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (589 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (660 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (124 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (566 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (94 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (664 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (279 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (40 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (198 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (258 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (311 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: survey, ar, efficient, 3d reconstruction, gaussian splatting, fast  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: robotics, semantic, nerf, 3d gaussian, autonomous driving, ar, survey  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, 3d reconstruction, survey  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: understanding, geometry, sparse view, nerf, 3d gaussian, face, ar, 3d reconstruction, outdoor, gaussian splatting, survey  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: robotics, semantic, segmentation, 3d gaussian, lighting, ar, gaussian splatting, survey  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: dynamic, 3d gaussian, survey, lighting, ar, 3d reconstruction, gaussian splatting, motion, fast  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: real-time rendering, dynamic, 3d gaussian, ar, gaussian splatting, survey  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: semantic, ar, geometry, survey  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: real-time rendering, compression, nerf, 3d gaussian, ar, efficient, 3d reconstruction, gaussian splatting, survey  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: 4d, dynamic, nerf, lighting, ar, gaussian splatting, motion, survey, deformation  

### Acceleration

*Showing the latest 50 out of 503 papers*

- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539v1)**  
  Authors: Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07539v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xdimlab.github.io/GIFStream)  
  Keywords: 4d, real-time rendering, compression, ar, efficient, gaussian splatting, motion, fast, deformation  
- **[Virtualized 3D Gaussians: Flexible Cluster-based Level-of-Detail System for Real-Time Rendering of Composed Scenes](https://arxiv.org/abs/2505.06523v1)**  
  Authors: Xijie Yang, Linning Xu, Lihan Jiang, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.06523v1.pdf)  
  Keywords: real-time rendering, dynamic, 3d gaussian, ar, efficient, gaussian splatting  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: survey, ar, efficient, 3d reconstruction, gaussian splatting, fast  
- **[QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization](https://arxiv.org/abs/2505.05591v1)**  
  Authors: Yueh-Cheng Liu, Lukas Höllein, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05591v1.pdf)  
  Keywords: robotics, geometry, face, ar, gaussian splatting, fast  
- **[Steepest Descent Density Control for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2505.05587v1)**  
  Authors: Peihao Wang, Yuehao Wang, Dilin Wang, Sreyas Mohan, Zhiwen Fan, Lemeng Wu, Ruisi Cai, Yu-Ying Yeh, Zhangyang Wang, Qiang Liu, Rakesh Ranjan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05587v1.pdf)  
  Keywords: gaussian splatting, compact, 3d gaussian, ar, efficient rendering, efficient  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: avatar, human, real-time rendering, high-fidelity, 3d gaussian, face, ar, gaussian splatting, animation  
- **[Time of the Flight of the Gaussians: Optimizing Depth Indirectly in Dynamic Radiance Fields](https://arxiv.org/abs/2505.05356v1)**  
  Authors: Runfeng Li, Mikhail Okunev, Zixuan Guo, Anh Ha Duong, Christian Richardt, Matthew O'Toole, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05356v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://visual.cs.brown.edu/gftorf)  
  Keywords: geometry, high-fidelity, dynamic, 3d gaussian, ar, 3d reconstruction, gaussian splatting, motion, fast  
- **[SGCR: Spherical Gaussians for Efficient 3D Curve Reconstruction](https://arxiv.org/abs/2505.04668v1)**  
  Authors: Xinran Yang, Donghao Ji, Yuanqi Li, Jie Guo, Yanwen Guo, Junyuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04668v1.pdf)  
  Keywords: neural rendering, high quality, 3d gaussian, ar, efficient, 3d reconstruction, gaussian splatting, fast  
- **[GSsplat: Generalizable Semantic Gaussian Splatting for Novel-view Synthesis in 3D Scenes](https://arxiv.org/abs/2505.04659v1)**  
  Authors: Feng Xiao, Hongbin Xu, Wanlin Liang, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04659v1.pdf)  
  Keywords: understanding, semantic, segmentation, ar, efficient, gaussian splatting, fast  
- **[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](https://arxiv.org/abs/2505.03351v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Yang Li, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03351v1.pdf)  
  Keywords: avatar, human, tracking, 3d gaussian, body, ar, mapping, motion, fast, animation  

### Applications

*Showing the latest 50 out of 1746 papers*

- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539v1)**  
  Authors: Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07539v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xdimlab.github.io/GIFStream)  
  Keywords: 4d, real-time rendering, compression, ar, efficient, gaussian splatting, motion, fast, deformation  
- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: semantic, high-fidelity, segmentation, nerf, ar, outdoor, gaussian splatting  
- **[Virtualized 3D Gaussians: Flexible Cluster-based Level-of-Detail System for Real-Time Rendering of Composed Scenes](https://arxiv.org/abs/2505.06523v1)**  
  Authors: Xijie Yang, Linning Xu, Lihan Jiang, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.06523v1.pdf)  
  Keywords: real-time rendering, dynamic, 3d gaussian, ar, efficient, gaussian splatting  
- **[TeGA: Texture Space Gaussian Avatars for High-Resolution Dynamic Head Modeling](https://arxiv.org/abs/2505.05672v1)**  
  Authors: Gengyan Li, Paulo Gotardo, Timo Bolkart, Stephan Garbin, Kripasindhu Sarkar, Abhimitra Meka, Alexandros Lattas, Thabo Beeler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05672v1.pdf)  
  Keywords: avatar, head, dynamic, 3d gaussian, ar, gaussian splatting, motion, deformation  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: survey, ar, efficient, 3d reconstruction, gaussian splatting, fast  
- **[QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization](https://arxiv.org/abs/2505.05591v1)**  
  Authors: Yueh-Cheng Liu, Lukas Höllein, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05591v1.pdf)  
  Keywords: robotics, geometry, face, ar, gaussian splatting, fast  
- **[Steepest Descent Density Control for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2505.05587v1)**  
  Authors: Peihao Wang, Yuehao Wang, Dilin Wang, Sreyas Mohan, Zhiwen Fan, Lemeng Wu, Ruisi Cai, Yu-Ying Yeh, Zhangyang Wang, Qiang Liu, Rakesh Ranjan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05587v1.pdf)  
  Keywords: gaussian splatting, compact, 3d gaussian, ar, efficient rendering, efficient  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: avatar, human, real-time rendering, high-fidelity, 3d gaussian, face, ar, gaussian splatting, animation  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: robotics, semantic, nerf, 3d gaussian, autonomous driving, ar, survey  
- **[Time of the Flight of the Gaussians: Optimizing Depth Indirectly in Dynamic Radiance Fields](https://arxiv.org/abs/2505.05356v1)**  
  Authors: Runfeng Li, Mikhail Okunev, Zixuan Guo, Anh Ha Duong, Christian Richardt, Matthew O'Toole, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05356v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://visual.cs.brown.edu/gftorf)  
  Keywords: geometry, high-fidelity, dynamic, 3d gaussian, ar, 3d reconstruction, gaussian splatting, motion, fast  

### Avatar Generation

*Showing the latest 50 out of 589 papers*

- **[TeGA: Texture Space Gaussian Avatars for High-Resolution Dynamic Head Modeling](https://arxiv.org/abs/2505.05672v1)**  
  Authors: Gengyan Li, Paulo Gotardo, Timo Bolkart, Stephan Garbin, Kripasindhu Sarkar, Abhimitra Meka, Alexandros Lattas, Thabo Beeler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05672v1.pdf)  
  Keywords: avatar, head, dynamic, 3d gaussian, ar, gaussian splatting, motion, deformation  
- **[QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization](https://arxiv.org/abs/2505.05591v1)**  
  Authors: Yueh-Cheng Liu, Lukas Höllein, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05591v1.pdf)  
  Keywords: robotics, geometry, face, ar, gaussian splatting, fast  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: avatar, human, real-time rendering, high-fidelity, 3d gaussian, face, ar, gaussian splatting, animation  
- **[Bridging Geometry-Coherent Text-to-3D Generation with Multi-View Diffusion Priors and Gaussian Splatting](https://arxiv.org/abs/2505.04262v1)**  
  Authors: Feng Yang, Wenliang Qian, Wangmeng Zuo, Hui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04262v1.pdf)  
  Keywords: geometry, 3d gaussian, face, ar, gaussian splatting  
- **[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](https://arxiv.org/abs/2505.03351v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Yang Li, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03351v1.pdf)  
  Keywords: avatar, human, tracking, 3d gaussian, body, ar, mapping, motion, fast, animation  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: shape reconstruction, head, geometry, sparse view, face, ar, efficient, gaussian splatting, fast  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: shape reconstruction, geometry, sparse view, sparse-view, 3d gaussian, face, ar, 3d reconstruction, gaussian splatting, fast  
- **[GarmentGS: Point-Cloud Guided Gaussian Splatting for High-Fidelity Non-Watertight 3D Garment Reconstruction](https://arxiv.org/abs/2505.02126v1)**  
  Authors: Zhihao Tang, Shenghao Yang, Hongtao Zhang, Mingbo Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02126v1.pdf)  
  Keywords: real-time rendering, high-fidelity, 3d gaussian, face, ar, gaussian splatting, fast  
- **[SignSplat: Rendering Sign Language via Gaussian Splatting](https://arxiv.org/abs/2505.02108v1)**  
  Authors: Maksym Ivashechkin, Oscar Mendez, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02108v1.pdf)  
  Keywords: human, body, face, ar, gaussian splatting, motion  
- **[GenSync: A Generalized Talking Head Framework for Audio-driven Multi-Subject Lip-Sync using 3D Gaussian Splatting](https://arxiv.org/abs/2505.01928v1)**  
  Authors: Anushka Agarwal, Muhammad Yusuf Hassan, Talha Chafekar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01928v1.pdf)  
  Keywords: head, 3d gaussian, ar, efficient, gaussian splatting, fast  

### Dynamic Scene

*Showing the latest 50 out of 660 papers*

- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539v1)**  
  Authors: Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07539v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xdimlab.github.io/GIFStream)  
  Keywords: 4d, real-time rendering, compression, ar, efficient, gaussian splatting, motion, fast, deformation  
- **[Virtualized 3D Gaussians: Flexible Cluster-based Level-of-Detail System for Real-Time Rendering of Composed Scenes](https://arxiv.org/abs/2505.06523v1)**  
  Authors: Xijie Yang, Linning Xu, Lihan Jiang, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.06523v1.pdf)  
  Keywords: real-time rendering, dynamic, 3d gaussian, ar, efficient, gaussian splatting  
- **[TeGA: Texture Space Gaussian Avatars for High-Resolution Dynamic Head Modeling](https://arxiv.org/abs/2505.05672v1)**  
  Authors: Gengyan Li, Paulo Gotardo, Timo Bolkart, Stephan Garbin, Kripasindhu Sarkar, Abhimitra Meka, Alexandros Lattas, Thabo Beeler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05672v1.pdf)  
  Keywords: avatar, head, dynamic, 3d gaussian, ar, gaussian splatting, motion, deformation  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: avatar, human, real-time rendering, high-fidelity, 3d gaussian, face, ar, gaussian splatting, animation  
- **[Time of the Flight of the Gaussians: Optimizing Depth Indirectly in Dynamic Radiance Fields](https://arxiv.org/abs/2505.05356v1)**  
  Authors: Runfeng Li, Mikhail Okunev, Zixuan Guo, Anh Ha Duong, Christian Richardt, Matthew O'Toole, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05356v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://visual.cs.brown.edu/gftorf)  
  Keywords: geometry, high-fidelity, dynamic, 3d gaussian, ar, 3d reconstruction, gaussian splatting, motion, fast  
- **[MoRe-3DGSMR: Motion-resolved reconstruction framework for free-breathing pulmonary MRI based on 3D Gaussian representation](https://arxiv.org/abs/2505.04959v1)**  
  Authors: Tengya Peng, Ruyi Zha, Qing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04959v1.pdf)  
  Keywords: 3d gaussian, motion, ar, deformation  
- **[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](https://arxiv.org/abs/2505.03351v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Yang Li, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03351v1.pdf)  
  Keywords: avatar, human, tracking, 3d gaussian, body, ar, mapping, motion, fast, animation  
- **[SignSplat: Rendering Sign Language via Gaussian Splatting](https://arxiv.org/abs/2505.02108v1)**  
  Authors: Maksym Ivashechkin, Oscar Mendez, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02108v1.pdf)  
  Keywords: human, body, face, ar, gaussian splatting, motion  
- **[AquaGS: Fast Underwater Scene Reconstruction with SfM-Free Gaussian Splatting](https://arxiv.org/abs/2505.01799v1)**  
  Authors: Junhao Shi, Jisheng Xu, Jianping He, Zhiliang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01799v1.pdf)  
  Keywords: nerf, 3d gaussian, face, ar, gaussian splatting, motion, fast  
- **[FalconWing: An Open-Source Platform for Ultra-Light Fixed-Wing Aircraft Research](https://arxiv.org/abs/2505.01383v1)**  
  Authors: Yan Miao, Will Shen, Hang Cui, Sayan Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01383v1.pdf)  
  Keywords: dynamic, 3d gaussian, ar, gaussian splatting, motion, lightweight  

### Few-shot

*Showing the latest 50 out of 124 papers*

- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: shape reconstruction, head, geometry, sparse view, face, ar, efficient, gaussian splatting, fast  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: shape reconstruction, geometry, sparse view, sparse-view, 3d gaussian, face, ar, 3d reconstruction, gaussian splatting, fast  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: understanding, geometry, sparse view, nerf, 3d gaussian, face, ar, 3d reconstruction, outdoor, gaussian splatting, survey  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: geometry, sparse view, sparse-view, nerf, face, ar, gaussian splatting, motion, fast  
- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v2)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v2.pdf)  
  Keywords: dynamic, body, ar, efficient, few-shot, gaussian splatting  
- **[IXGS-Intraoperative 3D Reconstruction from Sparse, Arbitrarily Posed Real X-rays](https://arxiv.org/abs/2504.14699v1)**  
  Authors: Sascha Jecklin, Aidana Massalimova, Ruyi Zha, Lilian Calvet, Christoph J. Laux, Mazda Farshad, Philipp Fürnstahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14699v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, sparse-view, ar  
- **[VGNC: Reducing the Overfitting of Sparse-view 3DGS via Validation-guided Gaussian Number Control](https://arxiv.org/abs/2504.14548v1)**  
  Authors: Lifeng Lin, Rongfeng Lu, Quan Chen, Haofan Ren, Ming Lu, Yaoqi Sun, Chenggang Yan, Anke Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14548v1.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, 3d reconstruction, gaussian splatting  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: geometry, sparse-view, 3d gaussian, ar, efficient, outdoor, gaussian splatting  
- **[DropoutGS: Dropping Out Gaussians for Better Sparse-view Rendering](https://arxiv.org/abs/2504.09491v1)**  
  Authors: Yexing Xu, Longguang Wang, Minglin Chen, Sheng Ao, Li Li, Yulan Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuyx55.github.io/DropoutGS/.)  
  Keywords: sparse view, sparse-view, 3d gaussian, ar, gaussian splatting  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: avatar, human, head, sparse-view, 3d gaussian, body, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 566 papers*

- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: survey, ar, efficient, 3d reconstruction, gaussian splatting, fast  
- **[QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization](https://arxiv.org/abs/2505.05591v1)**  
  Authors: Yueh-Cheng Liu, Lukas Höllein, Matthias Nießner, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05591v1.pdf)  
  Keywords: robotics, geometry, face, ar, gaussian splatting, fast  
- **[Time of the Flight of the Gaussians: Optimizing Depth Indirectly in Dynamic Radiance Fields](https://arxiv.org/abs/2505.05356v1)**  
  Authors: Runfeng Li, Mikhail Okunev, Zixuan Guo, Anh Ha Duong, Christian Richardt, Matthew O'Toole, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05356v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://visual.cs.brown.edu/gftorf)  
  Keywords: geometry, high-fidelity, dynamic, 3d gaussian, ar, 3d reconstruction, gaussian splatting, motion, fast  
- **[Bridging Geometry-Coherent Text-to-3D Generation with Multi-View Diffusion Priors and Gaussian Splatting](https://arxiv.org/abs/2505.04262v1)**  
  Authors: Feng Yang, Wenliang Qian, Wangmeng Zuo, Hui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04262v1.pdf)  
  Keywords: geometry, 3d gaussian, face, ar, gaussian splatting  
- **[SGCR: Spherical Gaussians for Efficient 3D Curve Reconstruction](https://arxiv.org/abs/2505.04668v1)**  
  Authors: Xinran Yang, Donghao Ji, Yuanqi Li, Jie Guo, Yanwen Guo, Junyuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04668v1.pdf)  
  Keywords: neural rendering, high quality, 3d gaussian, ar, efficient, 3d reconstruction, gaussian splatting, fast  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: shape reconstruction, head, geometry, sparse view, face, ar, efficient, gaussian splatting, fast  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: shape reconstruction, geometry, sparse view, sparse-view, 3d gaussian, face, ar, 3d reconstruction, gaussian splatting, fast  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, 3d reconstruction, survey  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: understanding, geometry, sparse view, nerf, 3d gaussian, face, ar, 3d reconstruction, outdoor, gaussian splatting, survey  
- **[GauSS-MI: Gaussian Splatting Shannon Mutual Information for Active 3D Reconstruction](https://arxiv.org/abs/2504.21067v1)**  
  Authors: Yuhan Xie, Yixi Cai, Yinqiang Zhang, Lei Yang, Jia Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21067v1.pdf)  
  Keywords: nerf, 3d gaussian, ar, efficient, 3d reconstruction, gaussian splatting, motion  

### Large Scene

*Showing the latest 50 out of 94 papers*

- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: semantic, high-fidelity, segmentation, nerf, ar, outdoor, gaussian splatting  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: understanding, geometry, sparse view, nerf, 3d gaussian, face, ar, 3d reconstruction, outdoor, gaussian splatting, survey  
- **[HUG: Hierarchical Urban Gaussian Splatting with Block-Based Reconstruction](https://arxiv.org/abs/2504.16606v1)**  
  Authors: Zhongtao Wang, Mai Su, Huishan Au, Yilong Li, Xizhe Cao, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16606v1.pdf)  
  Keywords: 3d gaussian, ar, efficient, urban scene, gaussian splatting  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: geometry, sparse-view, 3d gaussian, ar, efficient, outdoor, gaussian splatting  
- **[You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting](https://arxiv.org/abs/2504.09062v1)**  
  Authors: Zhijie Shen, Chunyu Lin, Shujuan Huang, Lang Nie, Kang Liao, Yao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09062v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhijieshen-bjtu/TPGS?style=social)](https://github.com/zhijieshen-bjtu/TPGS)  
  Keywords: 3d gaussian, face, ar, 3d reconstruction, outdoor, gaussian splatting  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: nerf, ar, outdoor, gaussian splatting, motion, reflection  
- **[UnIRe: Unsupervised Instance Decomposition for Dynamic Urban Scene Reconstruction](https://arxiv.org/abs/2504.00763v1)**  
  Authors: Yunxuan Mao, Rong Xiong, Yue Wang, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00763v1.pdf)  
  Keywords: 4d, dynamic, autonomous driving, 3d gaussian, ar, urban scene, gaussian splatting  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: geometry, high-fidelity, dynamic, nerf, ar, efficient, outdoor, gaussian splatting, fast, reflection  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: geometry, dynamic, ar, urban scene, gaussian splatting, motion  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: real-time rendering, nerf, 3d gaussian, autonomous driving, ar, efficient, urban scene, gaussian splatting, fast  

### Model Compression

*Showing the latest 50 out of 664 papers*

- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539v1)**  
  Authors: Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07539v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xdimlab.github.io/GIFStream)  
  Keywords: 4d, real-time rendering, compression, ar, efficient, gaussian splatting, motion, fast, deformation  
- **[Virtualized 3D Gaussians: Flexible Cluster-based Level-of-Detail System for Real-Time Rendering of Composed Scenes](https://arxiv.org/abs/2505.06523v1)**  
  Authors: Xijie Yang, Linning Xu, Lihan Jiang, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.06523v1.pdf)  
  Keywords: real-time rendering, dynamic, 3d gaussian, ar, efficient, gaussian splatting  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: survey, ar, efficient, 3d reconstruction, gaussian splatting, fast  
- **[Steepest Descent Density Control for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2505.05587v1)**  
  Authors: Peihao Wang, Yuehao Wang, Dilin Wang, Sreyas Mohan, Zhiwen Fan, Lemeng Wu, Ruisi Cai, Yu-Ying Yeh, Zhangyang Wang, Qiang Liu, Rakesh Ranjan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05587v1.pdf)  
  Keywords: gaussian splatting, compact, 3d gaussian, ar, efficient rendering, efficient  
- **[SGCR: Spherical Gaussians for Efficient 3D Curve Reconstruction](https://arxiv.org/abs/2505.04668v1)**  
  Authors: Xinran Yang, Donghao Ji, Yuanqi Li, Jie Guo, Yanwen Guo, Junyuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04668v1.pdf)  
  Keywords: neural rendering, high quality, 3d gaussian, ar, efficient, 3d reconstruction, gaussian splatting, fast  
- **[GSsplat: Generalizable Semantic Gaussian Splatting for Novel-view Synthesis in 3D Scenes](https://arxiv.org/abs/2505.04659v1)**  
  Authors: Feng Xiao, Hongbin Xu, Wanlin Liang, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04659v1.pdf)  
  Keywords: understanding, semantic, segmentation, ar, efficient, gaussian splatting, fast  
- **[3D Gaussian Splatting Data Compression with Mixture of Priors](https://arxiv.org/abs/2505.03310v1)**  
  Authors: Lei Liu, Zhenghao Chen, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03310v1.pdf)  
  Keywords: compression, nerf, 3d gaussian, ar, efficient, gaussian splatting, lightweight  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: shape reconstruction, head, geometry, sparse view, face, ar, efficient, gaussian splatting, fast  
- **[HybridGS: High-Efficiency Gaussian Splatting Data Compression using Dual-Channel Sparse Representation and Point Cloud Encoder](https://arxiv.org/abs/2505.01938v1)**  
  Authors: Qi Yang, Le Yang, Geert Van Der Auwera, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Qi-Yangsjtu/HybridGS?style=social)](https://github.com/Qi-Yangsjtu/HybridGS)  
  Keywords: compact, compression, 3d gaussian, ar, gaussian splatting  
- **[GenSync: A Generalized Talking Head Framework for Audio-driven Multi-Subject Lip-Sync using 3D Gaussian Splatting](https://arxiv.org/abs/2505.01928v1)**  
  Authors: Anushka Agarwal, Muhammad Yusuf Hassan, Talha Chafekar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01928v1.pdf)  
  Keywords: head, 3d gaussian, ar, efficient, gaussian splatting, fast  

### Quality Enhancement

*Showing the latest 50 out of 279 papers*

- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: semantic, high-fidelity, segmentation, nerf, ar, outdoor, gaussian splatting  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: avatar, human, real-time rendering, high-fidelity, 3d gaussian, face, ar, gaussian splatting, animation  
- **[Time of the Flight of the Gaussians: Optimizing Depth Indirectly in Dynamic Radiance Fields](https://arxiv.org/abs/2505.05356v1)**  
  Authors: Runfeng Li, Mikhail Okunev, Zixuan Guo, Anh Ha Duong, Christian Richardt, Matthew O'Toole, James Tompkin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05356v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://visual.cs.brown.edu/gftorf)  
  Keywords: geometry, high-fidelity, dynamic, 3d gaussian, ar, 3d reconstruction, gaussian splatting, motion, fast  
- **[SGCR: Spherical Gaussians for Efficient 3D Curve Reconstruction](https://arxiv.org/abs/2505.04668v1)**  
  Authors: Xinran Yang, Donghao Ji, Yuanqi Li, Jie Guo, Yanwen Guo, Junyuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04668v1.pdf)  
  Keywords: neural rendering, high quality, 3d gaussian, ar, efficient, 3d reconstruction, gaussian splatting, fast  
- **[GarmentGS: Point-Cloud Guided Gaussian Splatting for High-Fidelity Non-Watertight 3D Garment Reconstruction](https://arxiv.org/abs/2505.02126v1)**  
  Authors: Zhihao Tang, Shenghao Yang, Hongtao Zhang, Mingbo Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02126v1.pdf)  
  Keywords: real-time rendering, high-fidelity, 3d gaussian, face, ar, gaussian splatting, fast  
- **[HoloTime: Taming Video Diffusion Models for Panoramic 4D Scene Generation](https://arxiv.org/abs/2504.21650v2)**  
  Authors: Haiyang Zhou, Wangbo Yu, Jiawen Guan, Xinhua Cheng, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21650v2.pdf)  
  Keywords: 4d, vr, high-fidelity, dynamic, ar, gaussian splatting  
- **[STP4D: Spatio-Temporal-Prompt Consistent Modeling for Text-to-4D Gaussian Splatting](https://arxiv.org/abs/2504.18318v1)**  
  Authors: Yunze Deng, Haijun Xiong, Bin Feng, Xinggang Wang, Wenyu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18318v1.pdf)  
  Keywords: 4d, real-time rendering, high-fidelity, ar, gaussian splatting, deformation  
- **[When Gaussian Meets Surfel: Ultra-fast High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2504.17545v1)**  
  Authors: Keyang Ye, Tianjia Shao, Kun Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17545v1.pdf)  
  Keywords: geometry, compact, high-fidelity, 3d gaussian, ar, fast  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: human, real-time rendering, semantic, quality enhancement, dynamic, nerf, 3d gaussian, lighting, ar, gaussian splatting  
- **[CAGE-GS: High-fidelity Cage Based 3D Gaussian Splatting Deformation](https://arxiv.org/abs/2504.12800v1)**  
  Authors: Yifei Tong, Runze Tian, Xiao Han, Dingyao Liu, Fenggen Yu, Yan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12800v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, ar, gaussian splatting, deformation  

### Ray Tracing

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: avatar, relighting, human, geometry, relightable, ray tracing, lighting, shadow, ar, gaussian splatting, fast  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: relighting, acceleration, ray tracing, 3d gaussian, lighting, efficient, ar, efficient rendering, gaussian splatting  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: acceleration, compact, dynamic, ray marching, 3d gaussian, ar, efficient, gaussian splatting, animation  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: illumination, real-time rendering, ray tracing, global illumination, 3d gaussian, face, lighting, efficient, ar, gaussian splatting  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: light transport, illumination, real-time rendering, dynamic, global illumination, 3d gaussian, face, lighting, fast  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: neural rendering, ray tracing, 3d gaussian, ar, shadow, gaussian splatting, fast, reflection  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, geometry, real-time rendering, relightable, tracking, ray tracing, dynamic, face, lighting, ar, efficient  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: ray tracing, face, lighting, shadow, gaussian splatting, reflection  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, 3d gaussian, ar, gaussian splatting, survey  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: acceleration, light transport, ray tracing, ar, efficient, gaussian splatting, reflection  

### Relighting

*Showing the latest 50 out of 198 papers*

- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, 3d reconstruction, survey  
- **[TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians](https://arxiv.org/abs/2504.18768v2)**  
  Authors: Letian Huang, Dongwei Ye, Jialin Dan, Chengzhi Tao, Huiwen Liu, Kun Zhou, Bo Ren, Yuanqi Li, Yanwen Guo, Jie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18768v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, fast, reflection  
- **[RGS-DR: Reflective Gaussian Surfels with Deferred Rendering for Shiny Objects](https://arxiv.org/abs/2504.18468v3)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18468v3.pdf)  
  Keywords: relighting, geometry, nerf, 3d gaussian, face, lighting, ar, gaussian splatting, reflection  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: vr, nerf, 3d gaussian, lighting, ar, mapping, gaussian splatting, fast  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: human, real-time rendering, semantic, quality enhancement, dynamic, nerf, 3d gaussian, lighting, ar, gaussian splatting  
- **[Immersive Teleoperation Framework for Locomanipulation Tasks](https://arxiv.org/abs/2504.15229v1)**  
  Authors: Takuya Boehringer, Jonathan Embley-Riches, Karim Hammoud, Valerio Modugno, Dimitrios Kanoulas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15229v1.pdf)  
  Keywords: vr, face, ar, lighting, gaussian splatting, fast  
- **[Metamon-GS: Enhancing Representability with Variance-Guided Densification and Light Encoding](https://arxiv.org/abs/2504.14460v1)**  
  Authors: Junyan Su, Baozhu Zhao, Xiaohan Zhang, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14460v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, lighting  
- **[SLAM&Render: A Benchmark for the Intersection Between Neural Rendering, Gaussian Splatting and SLAM](https://arxiv.org/abs/2504.13713v2)**  
  Authors: Samuel Cerezo, Gaetano Meli, Tomás Berriel Martins, Kirill Safronov, Javier Civera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13713v2.pdf)  
  Keywords: slam, localization, illumination, neural rendering, nerf, lighting, ar, mapping, gaussian splatting  
- **[Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation](https://arxiv.org/abs/2504.13175v1)**  
  Authors: Sizhe Yang, Wenye Yu, Jia Zeng, Jun Lv, Kerui Ren, Cewu Lu, Dahua Lin, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13175v1.pdf)  
  Keywords: 3d gaussian, face, ar, lighting, gaussian splatting  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: robotics, semantic, segmentation, 3d gaussian, lighting, ar, gaussian splatting, survey  

### SLAM

*Showing the latest 50 out of 258 papers*

- **[Apply Hierarchical-Chain-of-Generation to Complex Attributes Text-to-3D Generation](https://arxiv.org/abs/2505.05505v1)**  
  Authors: Yiming Qin, Zhu Xu, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05505v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Wakals/GASCOL?style=social)](https://github.com/Wakals/GASCOL)  
  Keywords: semantic, 3d gaussian, localization, ar  
- **[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](https://arxiv.org/abs/2505.03351v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Yang Li, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03351v1.pdf)  
  Keywords: avatar, human, tracking, 3d gaussian, body, ar, mapping, motion, fast, animation  
- **[Creating Your Editable 3D Photorealistic Avatar with Tetrahedron-constrained Gaussian Splatting](https://arxiv.org/abs/2504.20403v1)**  
  Authors: Hanxi Liu, Yifang Men, Zhouhui Lian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20403v1.pdf)  
  Keywords: avatar, localization, geometry, vr, 3d gaussian, ar, gaussian splatting  
- **[GSFeatLoc: Visual Localization Using Feature Correspondence on 3D Gaussian Splatting](https://arxiv.org/abs/2504.20379v2)**  
  Authors: Jongwon Lee, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20379v2.pdf)  
  Keywords: localization, nerf, 3d gaussian, ar, gaussian splatting, fast  
- **[Mesh-Learner: Texturing Mesh with Spherical Harmonics](https://arxiv.org/abs/2504.19938v1)**  
  Authors: Yunfei Wan, Jianheng Liu, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/Mesh-Learner?style=social)](https://github.com/hku-mars/Mesh-Learner)  
  Keywords: mapping, robotics, 3d gaussian, ar, efficient, 3d reconstruction, gaussian splatting, fast  
- **[GSFF-SLAM: 3D Semantic Gaussian Splatting SLAM via Feature Field](https://arxiv.org/abs/2504.19409v1)**  
  Authors: Zuxing Lu, Xin Yuan, Shaowen Yang, Jingyu Liu, Jiawei Wang, Changyin Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19409v1.pdf)  
  Keywords: slam, geometry, tracking, semantic, segmentation, 3d gaussian, ar, mapping, gaussian splatting  
- **[PerfCam: Digital Twinning for Production Lines Using 3D Gaussian Splatting and Vision Models](https://arxiv.org/abs/2504.18165v1)**  
  Authors: Michel Gokan Khan, Renan Guarese, Fabian Johnson, Xi Vincent Wang, Anders Bergman, Benjamin Edvinsson, Mario Romero, Jérémy Vachier, Jan Kronqvist  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18165v1.pdf)  
  Keywords: mapping, tracking, 3d gaussian, ar, 3d reconstruction, gaussian splatting  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: vr, nerf, 3d gaussian, lighting, ar, mapping, gaussian splatting, fast  
- **[ToF-Splatting: Dense SLAM using Sparse Time-of-Flight Depth and Multi-Frame Integration](https://arxiv.org/abs/2504.16545v1)**  
  Authors: Andrea Conti, Matteo Poggi, Valerio Cambareri, Martin R. Oswald, Stefano Mattoccia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16545v1.pdf)  
  Keywords: slam, geometry, tracking, vr, 3d gaussian, ar, efficient, mapping, gaussian splatting  
- **[SmallGS: Gaussian Splatting-based Camera Pose Estimation for Small-Baseline Videos](https://arxiv.org/abs/2504.17810v1)**  
  Authors: Yuxin Yao, Yan Zhang, Zhening Huang, Joan Lasenby  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17810v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuxinyao620.github.io/SmallGS)  
  Keywords: slam, dynamic, ar, gaussian splatting, motion  

### Scene Understanding

*Showing the latest 50 out of 311 papers*

- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: semantic, high-fidelity, segmentation, nerf, ar, outdoor, gaussian splatting  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: robotics, semantic, nerf, 3d gaussian, autonomous driving, ar, survey  
- **[Apply Hierarchical-Chain-of-Generation to Complex Attributes Text-to-3D Generation](https://arxiv.org/abs/2505.05505v1)**  
  Authors: Yiming Qin, Zhu Xu, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05505v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Wakals/GASCOL?style=social)](https://github.com/Wakals/GASCOL)  
  Keywords: semantic, 3d gaussian, localization, ar  
- **[GSsplat: Generalizable Semantic Gaussian Splatting for Novel-view Synthesis in 3D Scenes](https://arxiv.org/abs/2505.04659v1)**  
  Authors: Feng Xiao, Hongbin Xu, Wanlin Liang, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04659v1.pdf)  
  Keywords: understanding, semantic, segmentation, ar, efficient, gaussian splatting, fast  
- **[FreeInsert: Disentangled Text-Guided Object Insertion in 3D Gaussian Scene without Spatial Priors](https://arxiv.org/abs/2505.01322v1)**  
  Authors: Chenxi Li, Weijie Wang, Qiang Li, Bruno Lepri, Nicu Sebe, Weizhi Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01322v1.pdf)  
  Keywords: semantic, 3d gaussian, ar  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: understanding, geometry, sparse view, nerf, 3d gaussian, face, ar, 3d reconstruction, outdoor, gaussian splatting, survey  
- **[GSFF-SLAM: 3D Semantic Gaussian Splatting SLAM via Feature Field](https://arxiv.org/abs/2504.19409v1)**  
  Authors: Zuxing Lu, Xin Yuan, Shaowen Yang, Jingyu Liu, Jiawei Wang, Changyin Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19409v1.pdf)  
  Keywords: slam, geometry, tracking, semantic, segmentation, 3d gaussian, ar, mapping, gaussian splatting  
- **[Visibility-Uncertainty-guided 3D Gaussian Inpainting via Scene Conceptional Learning](https://arxiv.org/abs/2504.17815v1)**  
  Authors: Mingxuan Cui, Qing Guo, Yuyi Wang, Hongkai Yu, Di Lin, Qin Zou, Ming-Ming Cheng, Xi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17815v1.pdf)  
  Keywords: semantic, dynamic, nerf, 3d gaussian, ar, efficient, gaussian splatting, fast  
- **[Text-based Animatable 3D Avatars with Morphable Model Alignment](https://arxiv.org/abs/2504.15835v1)**  
  Authors: Yiqian Wu, Malte Prinzler, Xiaogang Jin, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15835v1.pdf)  
  Keywords: avatar, head, geometry, semantic, dynamic, ar, animation  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: human, real-time rendering, semantic, quality enhancement, dynamic, nerf, 3d gaussian, lighting, ar, gaussian splatting  



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