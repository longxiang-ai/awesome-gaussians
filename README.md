# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-05-09 00:54:10

## Categories

- [3DGS Surveys](#3dgs-surveys) (29 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (494 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1732 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (586 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (654 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (124 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (562 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (93 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (658 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (275 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (40 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (198 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (257 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (307 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: survey, ar, 3d reconstruction, 3d gaussian, lighting  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: sparse view, face, understanding, survey, nerf, geometry, ar, 3d reconstruction, 3d gaussian, gaussian splatting, outdoor  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: robotics, survey, semantic, ar, segmentation, 3d gaussian, gaussian splatting, lighting  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: dynamic, survey, ar, 3d reconstruction, lighting, 3d gaussian, gaussian splatting, fast, motion  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: dynamic, survey, ar, real-time rendering, 3d gaussian, gaussian splatting  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: geometry, ar, survey, semantic  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: nerf, survey, compression, efficient, ar, 3d reconstruction, real-time rendering, 3d gaussian, gaussian splatting  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: dynamic, deformation, nerf, survey, ar, gaussian splatting, lighting, motion, 4d  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, ar, 3d gaussian, gaussian splatting, ray tracing  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: dynamic, face, localization, mapping, survey, geometry, ar, slam, lighting, tracking, outdoor  

### Acceleration

*Showing the latest 50 out of 494 papers*

- **[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](https://arxiv.org/abs/2505.03351v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Yang Li, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03351v1.pdf)  
  Keywords: body, mapping, human, animation, avatar, ar, 3d gaussian, fast, tracking, motion  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: shape reconstruction, sparse view, face, geometry, efficient, head, ar, gaussian splatting, fast  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: shape reconstruction, sparse view, face, geometry, ar, 3d reconstruction, 3d gaussian, gaussian splatting, fast, sparse-view  
- **[GarmentGS: Point-Cloud Guided Gaussian Splatting for High-Fidelity Non-Watertight 3D Garment Reconstruction](https://arxiv.org/abs/2505.02126v1)**  
  Authors: Zhihao Tang, Shenghao Yang, Hongtao Zhang, Mingbo Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02126v1.pdf)  
  Keywords: high-fidelity, face, ar, real-time rendering, 3d gaussian, gaussian splatting, fast  
- **[GenSync: A Generalized Talking Head Framework for Audio-driven Multi-Subject Lip-Sync using 3D Gaussian Splatting](https://arxiv.org/abs/2505.01928v1)**  
  Authors: Anushka Agarwal, Muhammad Yusuf Hassan, Talha Chafekar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01928v1.pdf)  
  Keywords: efficient, head, ar, 3d gaussian, gaussian splatting, fast  
- **[AquaGS: Fast Underwater Scene Reconstruction with SfM-Free Gaussian Splatting](https://arxiv.org/abs/2505.01799v1)**  
  Authors: Junhao Shi, Jisheng Xu, Jianping He, Zhiliang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01799v1.pdf)  
  Keywords: face, nerf, ar, 3d gaussian, gaussian splatting, fast, motion  
- **[EfficientHuman: Efficient Training and Reconstruction of Moving Human using Articulated 2D Gaussian](https://arxiv.org/abs/2504.20607v1)**  
  Authors: Hao Tian, Rui Liu, Wen Shen, Yilong Hu, Zhihao Zheng, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20607v1.pdf)  
  Keywords: dynamic, body, face, human, efficient, ar, 3d gaussian, gaussian splatting, fast  
- **[GSFeatLoc: Visual Localization Using Feature Correspondence on 3D Gaussian Splatting](https://arxiv.org/abs/2504.20379v2)**  
  Authors: Jongwon Lee, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20379v2.pdf)  
  Keywords: localization, nerf, ar, 3d gaussian, gaussian splatting, fast  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: sparse view, face, nerf, geometry, ar, gaussian splatting, fast, sparse-view, motion  
- **[Mesh-Learner: Texturing Mesh with Spherical Harmonics](https://arxiv.org/abs/2504.19938v1)**  
  Authors: Yunfei Wan, Jianheng Liu, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/Mesh-Learner?style=social)](https://github.com/hku-mars/Mesh-Learner)  
  Keywords: robotics, mapping, efficient, ar, 3d reconstruction, 3d gaussian, gaussian splatting, fast  

### Applications

*Showing the latest 50 out of 1732 papers*

- **[Bridging Geometry-Coherent Text-to-3D Generation with Multi-View Diffusion Priors and Gaussian Splatting](https://arxiv.org/abs/2505.04262v1)**  
  Authors: Feng Yang, Wenliang Qian, Wangmeng Zuo, Hui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04262v1.pdf)  
  Keywords: face, geometry, ar, 3d gaussian, gaussian splatting  
- **[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](https://arxiv.org/abs/2505.03351v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Yang Li, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03351v1.pdf)  
  Keywords: body, mapping, human, animation, avatar, ar, 3d gaussian, fast, tracking, motion  
- **[3D Gaussian Splatting Data Compression with Mixture of Priors](https://arxiv.org/abs/2505.03310v1)**  
  Authors: Lei Liu, Zhenghao Chen, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03310v1.pdf)  
  Keywords: nerf, compression, efficient, ar, lightweight, 3d gaussian, gaussian splatting  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: shape reconstruction, sparse view, face, geometry, efficient, head, ar, gaussian splatting, fast  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: shape reconstruction, sparse view, face, geometry, ar, 3d reconstruction, 3d gaussian, gaussian splatting, fast, sparse-view  
- **[GarmentGS: Point-Cloud Guided Gaussian Splatting for High-Fidelity Non-Watertight 3D Garment Reconstruction](https://arxiv.org/abs/2505.02126v1)**  
  Authors: Zhihao Tang, Shenghao Yang, Hongtao Zhang, Mingbo Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02126v1.pdf)  
  Keywords: high-fidelity, face, ar, real-time rendering, 3d gaussian, gaussian splatting, fast  
- **[SignSplat: Rendering Sign Language via Gaussian Splatting](https://arxiv.org/abs/2505.02108v1)**  
  Authors: Maksym Ivashechkin, Oscar Mendez, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02108v1.pdf)  
  Keywords: body, face, human, ar, gaussian splatting, motion  
- **[HybridGS: High-Efficiency Gaussian Splatting Data Compression using Dual-Channel Sparse Representation and Point Cloud Encoder](https://arxiv.org/abs/2505.01938v1)**  
  Authors: Qi Yang, Le Yang, Geert Van Der Auwera, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Qi-Yangsjtu/HybridGS?style=social)](https://github.com/Qi-Yangsjtu/HybridGS)  
  Keywords: compression, ar, 3d gaussian, gaussian splatting, compact  
- **[GenSync: A Generalized Talking Head Framework for Audio-driven Multi-Subject Lip-Sync using 3D Gaussian Splatting](https://arxiv.org/abs/2505.01928v1)**  
  Authors: Anushka Agarwal, Muhammad Yusuf Hassan, Talha Chafekar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01928v1.pdf)  
  Keywords: efficient, head, ar, 3d gaussian, gaussian splatting, fast  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: survey, ar, 3d reconstruction, 3d gaussian, lighting  

### Avatar Generation

*Showing the latest 50 out of 586 papers*

- **[Bridging Geometry-Coherent Text-to-3D Generation with Multi-View Diffusion Priors and Gaussian Splatting](https://arxiv.org/abs/2505.04262v1)**  
  Authors: Feng Yang, Wenliang Qian, Wangmeng Zuo, Hui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04262v1.pdf)  
  Keywords: face, geometry, ar, 3d gaussian, gaussian splatting  
- **[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](https://arxiv.org/abs/2505.03351v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Yang Li, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03351v1.pdf)  
  Keywords: body, mapping, human, animation, avatar, ar, 3d gaussian, fast, tracking, motion  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: shape reconstruction, sparse view, face, geometry, efficient, head, ar, gaussian splatting, fast  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: shape reconstruction, sparse view, face, geometry, ar, 3d reconstruction, 3d gaussian, gaussian splatting, fast, sparse-view  
- **[GarmentGS: Point-Cloud Guided Gaussian Splatting for High-Fidelity Non-Watertight 3D Garment Reconstruction](https://arxiv.org/abs/2505.02126v1)**  
  Authors: Zhihao Tang, Shenghao Yang, Hongtao Zhang, Mingbo Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02126v1.pdf)  
  Keywords: high-fidelity, face, ar, real-time rendering, 3d gaussian, gaussian splatting, fast  
- **[SignSplat: Rendering Sign Language via Gaussian Splatting](https://arxiv.org/abs/2505.02108v1)**  
  Authors: Maksym Ivashechkin, Oscar Mendez, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02108v1.pdf)  
  Keywords: body, face, human, ar, gaussian splatting, motion  
- **[GenSync: A Generalized Talking Head Framework for Audio-driven Multi-Subject Lip-Sync using 3D Gaussian Splatting](https://arxiv.org/abs/2505.01928v1)**  
  Authors: Anushka Agarwal, Muhammad Yusuf Hassan, Talha Chafekar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01928v1.pdf)  
  Keywords: efficient, head, ar, 3d gaussian, gaussian splatting, fast  
- **[AquaGS: Fast Underwater Scene Reconstruction with SfM-Free Gaussian Splatting](https://arxiv.org/abs/2505.01799v1)**  
  Authors: Junhao Shi, Jisheng Xu, Jianping He, Zhiliang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01799v1.pdf)  
  Keywords: face, nerf, ar, 3d gaussian, gaussian splatting, fast, motion  
- **[Real-Time Animatable 2DGS-Avatars with Detail Enhancement from Monocular Videos](https://arxiv.org/abs/2505.00421v1)**  
  Authors: Xia Yuan, Hai Yuan, Wenyi Ge, Ying Fu, Xi Wu, Guanyu Xing  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00421v1.pdf)  
  Keywords: dynamic, deformation, face, human, animation, avatar, ar, gaussian splatting  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: sparse view, face, understanding, survey, nerf, geometry, ar, 3d reconstruction, 3d gaussian, gaussian splatting, outdoor  

### Dynamic Scene

*Showing the latest 50 out of 654 papers*

- **[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](https://arxiv.org/abs/2505.03351v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Yang Li, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03351v1.pdf)  
  Keywords: body, mapping, human, animation, avatar, ar, 3d gaussian, fast, tracking, motion  
- **[SignSplat: Rendering Sign Language via Gaussian Splatting](https://arxiv.org/abs/2505.02108v1)**  
  Authors: Maksym Ivashechkin, Oscar Mendez, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02108v1.pdf)  
  Keywords: body, face, human, ar, gaussian splatting, motion  
- **[AquaGS: Fast Underwater Scene Reconstruction with SfM-Free Gaussian Splatting](https://arxiv.org/abs/2505.01799v1)**  
  Authors: Junhao Shi, Jisheng Xu, Jianping He, Zhiliang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01799v1.pdf)  
  Keywords: face, nerf, ar, 3d gaussian, gaussian splatting, fast, motion  
- **[FalconWing: An Open-Source Platform for Ultra-Light Fixed-Wing Aircraft Research](https://arxiv.org/abs/2505.01383v1)**  
  Authors: Yan Miao, Will Shen, Hang Cui, Sayan Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01383v1.pdf)  
  Keywords: dynamic, ar, lightweight, 3d gaussian, gaussian splatting, motion  
- **[Compensating Spatiotemporally Inconsistent Observations for Online Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2505.01235v1)**  
  Authors: Youngsik Yun, Jeongmin Bae, Hyunseung Son, Seoha Kim, Hahyun Lee, Gun Bang, Youngjung Uh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01235v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://bbangsik13.github.io/OR2.)  
  Keywords: gaussian splatting, dynamic, ar, 3d gaussian  
- **[Real-Time Animatable 2DGS-Avatars with Detail Enhancement from Monocular Videos](https://arxiv.org/abs/2505.00421v1)**  
  Authors: Xia Yuan, Hai Yuan, Wenyi Ge, Ying Fu, Xi Wu, Guanyu Xing  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00421v1.pdf)  
  Keywords: dynamic, deformation, face, human, animation, avatar, ar, gaussian splatting  
- **[HoloTime: Taming Video Diffusion Models for Panoramic 4D Scene Generation](https://arxiv.org/abs/2504.21650v1)**  
  Authors: Haiyang Zhou, Wangbo Yu, Jiawen Guan, Xinhua Cheng, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21650v1.pdf)  
  Keywords: vr, high-fidelity, dynamic, ar, gaussian splatting, 4d  
- **[GauSS-MI: Gaussian Splatting Shannon Mutual Information for Active 3D Reconstruction](https://arxiv.org/abs/2504.21067v1)**  
  Authors: Yuhan Xie, Yixi Cai, Yinqiang Zhang, Lei Yang, Jia Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21067v1.pdf)  
  Keywords: nerf, efficient, ar, 3d reconstruction, 3d gaussian, gaussian splatting, motion  
- **[EfficientHuman: Efficient Training and Reconstruction of Moving Human using Articulated 2D Gaussian](https://arxiv.org/abs/2504.20607v1)**  
  Authors: Hao Tian, Rui Liu, Wen Shen, Yilong Hu, Zhihao Zheng, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20607v1.pdf)  
  Keywords: dynamic, body, face, human, efficient, ar, 3d gaussian, gaussian splatting, fast  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: sparse view, face, nerf, geometry, ar, gaussian splatting, fast, sparse-view, motion  

### Few-shot

*Showing the latest 50 out of 124 papers*

- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: shape reconstruction, sparse view, face, geometry, efficient, head, ar, gaussian splatting, fast  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: shape reconstruction, sparse view, face, geometry, ar, 3d reconstruction, 3d gaussian, gaussian splatting, fast, sparse-view  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: sparse view, face, understanding, survey, nerf, geometry, ar, 3d reconstruction, 3d gaussian, gaussian splatting, outdoor  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: sparse view, face, nerf, geometry, ar, gaussian splatting, fast, sparse-view, motion  
- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v2)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v2.pdf)  
  Keywords: dynamic, body, efficient, ar, gaussian splatting, few-shot  
- **[IXGS-Intraoperative 3D Reconstruction from Sparse, Arbitrarily Posed Real X-rays](https://arxiv.org/abs/2504.14699v1)**  
  Authors: Sascha Jecklin, Aidana Massalimova, Ruyi Zha, Lilian Calvet, Christoph J. Laux, Mazda Farshad, Philipp Fürnstahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14699v1.pdf)  
  Keywords: gaussian splatting, sparse-view, ar, 3d reconstruction  
- **[VGNC: Reducing the Overfitting of Sparse-view 3DGS via Validation-guided Gaussian Number Control](https://arxiv.org/abs/2504.14548v1)**  
  Authors: Lifeng Lin, Rongfeng Lu, Quan Chen, Haofan Ren, Ming Lu, Yaoqi Sun, Chenggang Yan, Anke Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14548v1.pdf)  
  Keywords: ar, 3d reconstruction, 3d gaussian, gaussian splatting, sparse-view  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: geometry, efficient, ar, 3d gaussian, gaussian splatting, sparse-view, outdoor  
- **[DropoutGS: Dropping Out Gaussians for Better Sparse-view Rendering](https://arxiv.org/abs/2504.09491v1)**  
  Authors: Yexing Xu, Longguang Wang, Minglin Chen, Sheng Ao, Li Li, Yulan Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuyx55.github.io/DropoutGS/.)  
  Keywords: sparse view, ar, 3d gaussian, gaussian splatting, sparse-view  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: body, human, head, avatar, ar, 3d gaussian, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 562 papers*

- **[Bridging Geometry-Coherent Text-to-3D Generation with Multi-View Diffusion Priors and Gaussian Splatting](https://arxiv.org/abs/2505.04262v1)**  
  Authors: Feng Yang, Wenliang Qian, Wangmeng Zuo, Hui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.04262v1.pdf)  
  Keywords: face, geometry, ar, 3d gaussian, gaussian splatting  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: shape reconstruction, sparse view, face, geometry, efficient, head, ar, gaussian splatting, fast  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: shape reconstruction, sparse view, face, geometry, ar, 3d reconstruction, 3d gaussian, gaussian splatting, fast, sparse-view  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: survey, ar, 3d reconstruction, 3d gaussian, lighting  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: sparse view, face, understanding, survey, nerf, geometry, ar, 3d reconstruction, 3d gaussian, gaussian splatting, outdoor  
- **[GauSS-MI: Gaussian Splatting Shannon Mutual Information for Active 3D Reconstruction](https://arxiv.org/abs/2504.21067v1)**  
  Authors: Yuhan Xie, Yixi Cai, Yinqiang Zhang, Lei Yang, Jia Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21067v1.pdf)  
  Keywords: nerf, efficient, ar, 3d reconstruction, 3d gaussian, gaussian splatting, motion  
- **[Creating Your Editable 3D Photorealistic Avatar with Tetrahedron-constrained Gaussian Splatting](https://arxiv.org/abs/2504.20403v1)**  
  Authors: Hanxi Liu, Yifang Men, Zhouhui Lian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20403v1.pdf)  
  Keywords: vr, localization, geometry, avatar, ar, 3d gaussian, gaussian splatting  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: sparse view, face, nerf, geometry, ar, gaussian splatting, fast, sparse-view, motion  
- **[Mesh-Learner: Texturing Mesh with Spherical Harmonics](https://arxiv.org/abs/2504.19938v1)**  
  Authors: Yunfei Wan, Jianheng Liu, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/Mesh-Learner?style=social)](https://github.com/hku-mars/Mesh-Learner)  
  Keywords: robotics, mapping, efficient, ar, 3d reconstruction, 3d gaussian, gaussian splatting, fast  
- **[CE-NPBG: Connectivity Enhanced Neural Point-Based Graphics for Novel View Synthesis in Autonomous Driving Scenes](https://arxiv.org/abs/2504.19557v1)**  
  Authors: Mohammad Altillawi, Fengyi Shen, Liudi Yang, Sai Manoj Prakhya, Ziyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19557v1.pdf)  
  Keywords: geometry, ar, 3d gaussian, gaussian splatting, autonomous driving  

### Large Scene

*Showing the latest 50 out of 93 papers*

- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: sparse view, face, understanding, survey, nerf, geometry, ar, 3d reconstruction, 3d gaussian, gaussian splatting, outdoor  
- **[HUG: Hierarchical Urban Gaussian Splatting with Block-Based Reconstruction](https://arxiv.org/abs/2504.16606v1)**  
  Authors: Zhongtao Wang, Mai Su, Huishan Au, Yilong Li, Xizhe Cao, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16606v1.pdf)  
  Keywords: efficient, urban scene, ar, 3d gaussian, gaussian splatting  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: geometry, efficient, ar, 3d gaussian, gaussian splatting, sparse-view, outdoor  
- **[You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting](https://arxiv.org/abs/2504.09062v1)**  
  Authors: Zhijie Shen, Chunyu Lin, Shujuan Huang, Lang Nie, Kang Liao, Yao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09062v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhijieshen-bjtu/TPGS?style=social)](https://github.com/zhijieshen-bjtu/TPGS)  
  Keywords: face, ar, 3d reconstruction, 3d gaussian, gaussian splatting, outdoor  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: outdoor, reflection, nerf, ar, gaussian splatting, motion  
- **[UnIRe: Unsupervised Instance Decomposition for Dynamic Urban Scene Reconstruction](https://arxiv.org/abs/2504.00763v1)**  
  Authors: Yunxuan Mao, Rong Xiong, Yue Wang, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00763v1.pdf)  
  Keywords: dynamic, urban scene, ar, 3d gaussian, gaussian splatting, autonomous driving, 4d  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: high-fidelity, dynamic, reflection, nerf, geometry, efficient, ar, gaussian splatting, fast, outdoor  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: dynamic, geometry, urban scene, ar, gaussian splatting, motion  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: nerf, efficient, urban scene, ar, real-time rendering, 3d gaussian, gaussian splatting, fast, autonomous driving  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: illumination, ar, 3d gaussian, gaussian splatting, sparse-view, outdoor  

### Model Compression

*Showing the latest 50 out of 658 papers*

- **[3D Gaussian Splatting Data Compression with Mixture of Priors](https://arxiv.org/abs/2505.03310v1)**  
  Authors: Lei Liu, Zhenghao Chen, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03310v1.pdf)  
  Keywords: nerf, compression, efficient, ar, lightweight, 3d gaussian, gaussian splatting  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: shape reconstruction, sparse view, face, geometry, efficient, head, ar, gaussian splatting, fast  
- **[HybridGS: High-Efficiency Gaussian Splatting Data Compression using Dual-Channel Sparse Representation and Point Cloud Encoder](https://arxiv.org/abs/2505.01938v1)**  
  Authors: Qi Yang, Le Yang, Geert Van Der Auwera, Zhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Qi-Yangsjtu/HybridGS?style=social)](https://github.com/Qi-Yangsjtu/HybridGS)  
  Keywords: compression, ar, 3d gaussian, gaussian splatting, compact  
- **[GenSync: A Generalized Talking Head Framework for Audio-driven Multi-Subject Lip-Sync using 3D Gaussian Splatting](https://arxiv.org/abs/2505.01928v1)**  
  Authors: Anushka Agarwal, Muhammad Yusuf Hassan, Talha Chafekar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01928v1.pdf)  
  Keywords: efficient, head, ar, 3d gaussian, gaussian splatting, fast  
- **[FalconWing: An Open-Source Platform for Ultra-Light Fixed-Wing Aircraft Research](https://arxiv.org/abs/2505.01383v1)**  
  Authors: Yan Miao, Will Shen, Hang Cui, Sayan Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01383v1.pdf)  
  Keywords: dynamic, ar, lightweight, 3d gaussian, gaussian splatting, motion  
- **[GauSS-MI: Gaussian Splatting Shannon Mutual Information for Active 3D Reconstruction](https://arxiv.org/abs/2504.21067v1)**  
  Authors: Yuhan Xie, Yixi Cai, Yinqiang Zhang, Lei Yang, Jia Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21067v1.pdf)  
  Keywords: nerf, efficient, ar, 3d reconstruction, 3d gaussian, gaussian splatting, motion  
- **[EfficientHuman: Efficient Training and Reconstruction of Moving Human using Articulated 2D Gaussian](https://arxiv.org/abs/2504.20607v1)**  
  Authors: Hao Tian, Rui Liu, Wen Shen, Yilong Hu, Zhihao Zheng, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20607v1.pdf)  
  Keywords: dynamic, body, face, human, efficient, ar, 3d gaussian, gaussian splatting, fast  
- **[Mesh-Learner: Texturing Mesh with Spherical Harmonics](https://arxiv.org/abs/2504.19938v1)**  
  Authors: Yunfei Wan, Jianheng Liu, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/Mesh-Learner?style=social)](https://github.com/hku-mars/Mesh-Learner)  
  Keywords: robotics, mapping, efficient, ar, 3d reconstruction, 3d gaussian, gaussian splatting, fast  
- **[IM-Portrait: Learning 3D-aware Video Diffusion for Photorealistic Talking Heads from Monocular Videos](https://arxiv.org/abs/2504.19165v2)**  
  Authors: Yuan Li, Ziqian Bai, Feitong Tan, Zhaopeng Cui, Sean Fanello, Yinda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19165v2.pdf)  
  Keywords: vr, nerf, efficient, avatar, head, 3d reconstruction, ar, 3d gaussian  
- **[4DGS-CC: A Contextual Coding Framework for 4D Gaussian Splatting Data Compression](https://arxiv.org/abs/2504.18925v2)**  
  Authors: Zicong Chen, Zhenghao Chen, Wei Jiang, Wei Wang, Lei Liu, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18925v2.pdf)  
  Keywords: dynamic, compression, ar, 3d gaussian, gaussian splatting, 4d  

### Quality Enhancement

*Showing the latest 50 out of 275 papers*

- **[GarmentGS: Point-Cloud Guided Gaussian Splatting for High-Fidelity Non-Watertight 3D Garment Reconstruction](https://arxiv.org/abs/2505.02126v1)**  
  Authors: Zhihao Tang, Shenghao Yang, Hongtao Zhang, Mingbo Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02126v1.pdf)  
  Keywords: high-fidelity, face, ar, real-time rendering, 3d gaussian, gaussian splatting, fast  
- **[HoloTime: Taming Video Diffusion Models for Panoramic 4D Scene Generation](https://arxiv.org/abs/2504.21650v1)**  
  Authors: Haiyang Zhou, Wangbo Yu, Jiawen Guan, Xinhua Cheng, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21650v1.pdf)  
  Keywords: vr, high-fidelity, dynamic, ar, gaussian splatting, 4d  
- **[STP4D: Spatio-Temporal-Prompt Consistent Modeling for Text-to-4D Gaussian Splatting](https://arxiv.org/abs/2504.18318v1)**  
  Authors: Yunze Deng, Haijun Xiong, Bin Feng, Xinggang Wang, Wenyu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18318v1.pdf)  
  Keywords: high-fidelity, deformation, ar, real-time rendering, gaussian splatting, 4d  
- **[When Gaussian Meets Surfel: Ultra-fast High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2504.17545v1)**  
  Authors: Keyang Ye, Tianjia Shao, Kun Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17545v1.pdf)  
  Keywords: high-fidelity, geometry, ar, 3d gaussian, fast, compact  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: dynamic, quality enhancement, nerf, semantic, human, ar, real-time rendering, 3d gaussian, gaussian splatting, lighting  
- **[CAGE-GS: High-fidelity Cage Based 3D Gaussian Splatting Deformation](https://arxiv.org/abs/2504.12800v1)**  
  Authors: Yifei Tong, Runze Tian, Xiao Han, Dingyao Liu, Fenggen Yu, Yan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12800v1.pdf)  
  Keywords: high-fidelity, deformation, ar, 3d gaussian, gaussian splatting  
- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: high-fidelity, human, efficient, head, ar, real-time rendering, 3d gaussian, gaussian splatting, lighting, recognition  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: high-fidelity, dynamic, nerf, efficient, ar, acceleration, gaussian splatting  
- **[TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting](https://arxiv.org/abs/2504.09588v1)**  
  Authors: Zhicong Wu, Hongbin Xu, Gang Xu, Ping Nie, Zhixin Yan, Jinkai Zheng, Liangqiong Qu, Ming Li, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09588v1.pdf)  
  Keywords: high-fidelity, semantic, ar, 3d reconstruction, segmentation, 3d gaussian, gaussian splatting, understanding  
- **[A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds](https://arxiv.org/abs/2504.09129v1)**  
  Authors: Jizong Peng, Tze Ho Elden Tse, Kai Xu, Wenchao Gao, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09129v1.pdf)  
  Keywords: high-fidelity, geometry, ar, 3d reconstruction, 3d gaussian, gaussian splatting, motion  

### Ray Tracing

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: shadow, human, geometry, ray tracing, avatar, ar, lighting, gaussian splatting, fast, relightable, relighting  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: relighting, efficient rendering, 3d gaussian, efficient, ar, acceleration, gaussian splatting, lighting, ray tracing  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: dynamic, 3d gaussian, animation, ray marching, efficient, ar, acceleration, gaussian splatting, compact  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: illumination, face, efficient, ar, real-time rendering, 3d gaussian, gaussian splatting, lighting, ray tracing, global illumination  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: illumination, dynamic, face, light transport, real-time rendering, lighting, 3d gaussian, fast, global illumination  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: shadow, reflection, neural rendering, ar, 3d gaussian, gaussian splatting, fast, ray tracing  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: dynamic, tracking, face, geometry, efficient, ar, real-time rendering, lighting, relightable, ray tracing, 4d  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: shadow, face, reflection, gaussian splatting, lighting, ray tracing  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, ar, 3d gaussian, gaussian splatting, ray tracing  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: reflection, light transport, efficient, ar, acceleration, gaussian splatting, ray tracing  

### Relighting

*Showing the latest 50 out of 198 papers*

- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: survey, ar, 3d reconstruction, 3d gaussian, lighting  
- **[TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians](https://arxiv.org/abs/2504.18768v2)**  
  Authors: Letian Huang, Dongwei Ye, Jialin Dan, Chengzhi Tao, Huiwen Liu, Kun Zhou, Bo Ren, Yuanqi Li, Yanwen Guo, Jie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18768v2.pdf)  
  Keywords: reflection, efficient, ar, 3d gaussian, gaussian splatting, fast  
- **[RGS-DR: Reflective Gaussian Surfels with Deferred Rendering for Shiny Objects](https://arxiv.org/abs/2504.18468v3)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18468v3.pdf)  
  Keywords: face, reflection, nerf, geometry, ar, 3d gaussian, gaussian splatting, lighting, relighting  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: vr, mapping, nerf, ar, lighting, 3d gaussian, gaussian splatting, fast  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: dynamic, quality enhancement, nerf, semantic, human, ar, real-time rendering, 3d gaussian, gaussian splatting, lighting  
- **[Immersive Teleoperation Framework for Locomanipulation Tasks](https://arxiv.org/abs/2504.15229v1)**  
  Authors: Takuya Boehringer, Jonathan Embley-Riches, Karim Hammoud, Valerio Modugno, Dimitrios Kanoulas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15229v1.pdf)  
  Keywords: vr, face, ar, lighting, gaussian splatting, fast  
- **[Metamon-GS: Enhancing Representability with Variance-Guided Densification and Light Encoding](https://arxiv.org/abs/2504.14460v1)**  
  Authors: Junyan Su, Baozhu Zhao, Xiaohan Zhang, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14460v1.pdf)  
  Keywords: gaussian splatting, lighting, ar, 3d gaussian  
- **[SLAM&Render: A Benchmark for the Intersection Between Neural Rendering, Gaussian Splatting and SLAM](https://arxiv.org/abs/2504.13713v2)**  
  Authors: Samuel Cerezo, Gaetano Meli, Tomás Berriel Martins, Kirill Safronov, Javier Civera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13713v2.pdf)  
  Keywords: illumination, localization, mapping, nerf, slam, neural rendering, ar, gaussian splatting, lighting  
- **[Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation](https://arxiv.org/abs/2504.13175v1)**  
  Authors: Sizhe Yang, Wenye Yu, Jia Zeng, Jun Lv, Kerui Ren, Cewu Lu, Dahua Lin, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13175v1.pdf)  
  Keywords: face, ar, 3d gaussian, gaussian splatting, lighting  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: robotics, survey, semantic, ar, segmentation, 3d gaussian, gaussian splatting, lighting  

### SLAM

*Showing the latest 50 out of 257 papers*

- **[GUAVA: Generalizable Upper Body 3D Gaussian Avatar](https://arxiv.org/abs/2505.03351v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Yang Li, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.03351v1.pdf)  
  Keywords: body, mapping, human, animation, avatar, ar, 3d gaussian, fast, tracking, motion  
- **[Creating Your Editable 3D Photorealistic Avatar with Tetrahedron-constrained Gaussian Splatting](https://arxiv.org/abs/2504.20403v1)**  
  Authors: Hanxi Liu, Yifang Men, Zhouhui Lian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20403v1.pdf)  
  Keywords: vr, localization, geometry, avatar, ar, 3d gaussian, gaussian splatting  
- **[GSFeatLoc: Visual Localization Using Feature Correspondence on 3D Gaussian Splatting](https://arxiv.org/abs/2504.20379v2)**  
  Authors: Jongwon Lee, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20379v2.pdf)  
  Keywords: localization, nerf, ar, 3d gaussian, gaussian splatting, fast  
- **[Mesh-Learner: Texturing Mesh with Spherical Harmonics](https://arxiv.org/abs/2504.19938v1)**  
  Authors: Yunfei Wan, Jianheng Liu, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/Mesh-Learner?style=social)](https://github.com/hku-mars/Mesh-Learner)  
  Keywords: robotics, mapping, efficient, ar, 3d reconstruction, 3d gaussian, gaussian splatting, fast  
- **[GSFF-SLAM: 3D Semantic Gaussian Splatting SLAM via Feature Field](https://arxiv.org/abs/2504.19409v1)**  
  Authors: Zuxing Lu, Xin Yuan, Shaowen Yang, Jingyu Liu, Jiawei Wang, Changyin Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19409v1.pdf)  
  Keywords: mapping, semantic, geometry, ar, segmentation, 3d gaussian, gaussian splatting, slam, tracking  
- **[PerfCam: Digital Twinning for Production Lines Using 3D Gaussian Splatting and Vision Models](https://arxiv.org/abs/2504.18165v1)**  
  Authors: Michel Gokan Khan, Renan Guarese, Fabian Johnson, Xi Vincent Wang, Anders Bergman, Benjamin Edvinsson, Mario Romero, Jérémy Vachier, Jan Kronqvist  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18165v1.pdf)  
  Keywords: mapping, ar, 3d reconstruction, 3d gaussian, gaussian splatting, tracking  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: vr, mapping, nerf, ar, lighting, 3d gaussian, gaussian splatting, fast  
- **[ToF-Splatting: Dense SLAM using Sparse Time-of-Flight Depth and Multi-Frame Integration](https://arxiv.org/abs/2504.16545v1)**  
  Authors: Andrea Conti, Matteo Poggi, Valerio Cambareri, Martin R. Oswald, Stefano Mattoccia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16545v1.pdf)  
  Keywords: vr, mapping, geometry, efficient, ar, 3d gaussian, gaussian splatting, slam, tracking  
- **[SmallGS: Gaussian Splatting-based Camera Pose Estimation for Small-Baseline Videos](https://arxiv.org/abs/2504.17810v1)**  
  Authors: Yuxin Yao, Yan Zhang, Zhening Huang, Joan Lasenby  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17810v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuxinyao620.github.io/SmallGS)  
  Keywords: dynamic, ar, gaussian splatting, slam, motion  
- **[NVSMask3D: Hard Visual Prompting with Camera Pose Interpolation for 3D Open Vocabulary Instance Segmentation](https://arxiv.org/abs/2504.14638v1)**  
  Authors: Junyuan Fang, Zihan Wang, Yejun Zhang, Shuzhe Wang, Iaroslav Melekhov, Juho Kannala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14638v1.pdf)  
  Keywords: localization, ar, segmentation, 3d gaussian, gaussian splatting, recognition  

### Scene Understanding

*Showing the latest 50 out of 307 papers*

- **[FreeInsert: Disentangled Text-Guided Object Insertion in 3D Gaussian Scene without Spatial Priors](https://arxiv.org/abs/2505.01322v1)**  
  Authors: Chenxi Li, Weijie Wang, Qiang Li, Bruno Lepri, Nicu Sebe, Weizhi Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01322v1.pdf)  
  Keywords: ar, semantic, 3d gaussian  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: sparse view, face, understanding, survey, nerf, geometry, ar, 3d reconstruction, 3d gaussian, gaussian splatting, outdoor  
- **[GSFF-SLAM: 3D Semantic Gaussian Splatting SLAM via Feature Field](https://arxiv.org/abs/2504.19409v1)**  
  Authors: Zuxing Lu, Xin Yuan, Shaowen Yang, Jingyu Liu, Jiawei Wang, Changyin Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19409v1.pdf)  
  Keywords: mapping, semantic, geometry, ar, segmentation, 3d gaussian, gaussian splatting, slam, tracking  
- **[Visibility-Uncertainty-guided 3D Gaussian Inpainting via Scene Conceptional Learning](https://arxiv.org/abs/2504.17815v1)**  
  Authors: Mingxuan Cui, Qing Guo, Yuyi Wang, Hongkai Yu, Di Lin, Qin Zou, Ming-Ming Cheng, Xi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17815v1.pdf)  
  Keywords: dynamic, nerf, semantic, efficient, ar, 3d gaussian, gaussian splatting, fast  
- **[Text-based Animatable 3D Avatars with Morphable Model Alignment](https://arxiv.org/abs/2504.15835v1)**  
  Authors: Yiqian Wu, Malte Prinzler, Xiaogang Jin, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15835v1.pdf)  
  Keywords: dynamic, semantic, geometry, animation, head, avatar, ar  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: dynamic, quality enhancement, nerf, semantic, human, ar, real-time rendering, 3d gaussian, gaussian splatting, lighting  
- **[NVSMask3D: Hard Visual Prompting with Camera Pose Interpolation for 3D Open Vocabulary Instance Segmentation](https://arxiv.org/abs/2504.14638v1)**  
  Authors: Junyuan Fang, Zihan Wang, Yejun Zhang, Shuzhe Wang, Iaroslav Melekhov, Juho Kannala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14638v1.pdf)  
  Keywords: localization, ar, segmentation, 3d gaussian, gaussian splatting, recognition  
- **[RoboOcc: Enhancing the Geometric and Semantic Scene Understanding for Robots](https://arxiv.org/abs/2504.14604v1)**  
  Authors: Zhang Zhang, Qiang Zhang, Wei Cui, Shuai Shi, Yijie Guo, Gang Han, Wen Zhao, Hengle Ren, Renjing Xu, Jian Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14604v1.pdf)  
  Keywords: semantic, geometry, ar, 3d gaussian, understanding  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: deformation, human, efficient, neural rendering, ar, 3d reconstruction, 3d gaussian, gaussian splatting, tracking, understanding  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: robotics, survey, semantic, ar, segmentation, 3d gaussian, gaussian splatting, lighting  



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