# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-04-07 00:53:30

## Categories

- [3DGS Surveys](#3dgs-surveys) (26 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (458 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1605 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (541 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (606 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (113 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (513 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (89 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (607 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (261 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (36 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (176 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (239 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (280 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: 3d gaussian, lighting, survey, ar, dynamic, 3d reconstruction, motion, gaussian splatting, fast  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: 3d gaussian, survey, ar, dynamic, real-time rendering, gaussian splatting  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: ar, survey, geometry, semantic  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: 3d gaussian, survey, ar, nerf, real-time rendering, 3d reconstruction, efficient, compression, gaussian splatting  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: lighting, survey, ar, nerf, dynamic, motion, 4d, gaussian splatting, deformation  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, survey, ar, gaussian splatting, ray tracing  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: mapping, lighting, survey, ar, localization, face, dynamic, slam, geometry, outdoor, tracking  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: 3d gaussian, illumination, survey, ar, recognition, gaussian splatting  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: lighting, autonomous driving, survey, ar, semantic, nerf, 3d reconstruction, dynamic, geometry, robotics, compact, gaussian splatting, high-fidelity  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: 3d gaussian, survey, ar, nerf, real-time rendering, robotics, gaussian splatting, understanding  

### Acceleration

*Showing the latest 50 out of 458 papers*

- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: 3d gaussian, mapping, ar, localization, face, dynamic, slam, gaussian splatting, tracking, fast  
- **[WorldPrompter: Traversable Text-to-Scene Generation](https://arxiv.org/abs/2504.02045v1)**  
  Authors: Zhaoyang Zhang, Yannick Hold-Geoffroy, Miloš Hašan, Chen Ziwen, Fujun Luan, Julie Dorsey, Yiwei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02045v1.pdf)  
  Keywords: ar, fast  
- **[Toward Real-world BEV Perception: Depth Uncertainty Estimation via Gaussian Splatting](https://arxiv.org/abs/2504.01957v2)**  
  Authors: Shu-Wei Lu, Yi-Hsuan Tsai, Yi-Ting Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01957v2.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, autonomous driving, fast  
- **[BOGausS: Better Optimized Gaussian Splatting](https://arxiv.org/abs/2504.01844v1)**  
  Authors: Stéphane Pateux, Matthieu Gendrin, Luce Morin, Théo Ladune, Xiaoran Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01844v1.pdf)  
  Keywords: 3d gaussian, ar, nerf, efficient, gaussian splatting, high-fidelity, fast  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: 3d gaussian, mapping, lighting, ar, nerf, real-time rendering, gaussian splatting  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: 3d gaussian, illumination, lighting, ar, face, real-time rendering, efficient, gaussian splatting, global illumination, ray tracing  
- **[DropGaussian: Structural Regularization for Sparse-view Gaussian Splatting](https://arxiv.org/abs/2504.00773v1)**  
  Authors: Hyunwoo Park, Gun Ryu, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DCVL-3D/DropGaussian?style=social)](https://github.com/DCVL-3D/DropGaussian)  
  Keywords: 3d gaussian, sparse-view, ar, face, gaussian splatting, fast  
- **[Scene4U: Hierarchical Layered 3D Scene Reconstruction from Single Panoramic Image for Your Immerse Exploration](https://arxiv.org/abs/2504.00387v1)**  
  Authors: Zilong Huang, Jun He, Junyan Ye, Lihan Jiang, Weijia Li, Yiping Chen, Ting Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00387v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LongHZ140516/Scene4U?style=social)](https://github.com/LongHZ140516/Scene4U)  
  Keywords: 3d gaussian, ar, semantic, dynamic, gaussian splatting, segmentation, fast  
- **[LITA-GS: Illumination-Agnostic Novel View Synthesis via Reference-Free 3D Gaussian Splatting and Physical Priors](https://arxiv.org/abs/2504.00219v1)**  
  Authors: Han Zhou, Wei Dong, Jun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00219v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LowLevelAI/LITA-GS?style=social)](https://github.com/LowLevelAI/LITA-GS)  
  Keywords: 3d gaussian, illumination, lighting, ar, nerf, motion, gaussian splatting, fast  
- **[ERUPT: Efficient Rendering with Unposed Patch Transformer](https://arxiv.org/abs/2503.24374v1)**  
  Authors: Maxim V. Shugaev, Vincent Chen, Maxim Karrenbach, Kyle Ashley, Bridget Kennedy, Naresh P. Cuntoor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24374v1.pdf)  
  Keywords: ar, nerf, efficient, gaussian splatting, efficient rendering  

### Applications

*Showing the latest 50 out of 1605 papers*

- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: 3d gaussian, mapping, ar, localization, face, dynamic, slam, gaussian splatting, tracking, fast  
- **[ConsDreamer: Advancing Multi-View Consistency for Zero-Shot Text-to-3D Generation](https://arxiv.org/abs/2504.02316v1)**  
  Authors: Yuan Zhou, Shilong Jin, Litao Hua, Wanjun Lv, Haoran Duan, Jungong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02316v1.pdf)  
  Keywords: 3d gaussian, ar, face, gaussian splatting  
- **[Digital-twin imaging based on descattering Gaussian splatting](https://arxiv.org/abs/2504.02278v1)**  
  Authors: Suguru Shimomura, Kazuki Yamanouchi, Jun Tanida  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02278v1.pdf)  
  Keywords: medical, gaussian splatting  
- **[UAVTwin: Neural Digital Twins for UAVs using Gaussian Splatting](https://arxiv.org/abs/2504.02158v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02158v1.pdf)  
  Keywords: 3d gaussian, high quality, human, ar, dynamic, motion, gaussian splatting, high-fidelity, neural rendering  
- **[WorldPrompter: Traversable Text-to-Scene Generation](https://arxiv.org/abs/2504.02045v1)**  
  Authors: Zhaoyang Zhang, Yannick Hold-Geoffroy, Miloš Hašan, Chen Ziwen, Fujun Luan, Julie Dorsey, Yiwei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02045v1.pdf)  
  Keywords: ar, fast  
- **[Diffusion-Guided Gaussian Splatting for Large-Scale Unconstrained 3D Reconstruction and Novel View Synthesis](https://arxiv.org/abs/2504.01960v1)**  
  Authors: Niluthpol Chowdhury Mithun, Tuan Pham, Qiao Wang, Ben Southall, Kshitij Minhas, Bogdan Matei, Stephan Mandt, Supun Samarasekera, Rakesh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01960v1.pdf)  
  Keywords: 3d gaussian, ar, nerf, 3d reconstruction, dynamic, gaussian splatting  
- **[Toward Real-world BEV Perception: Depth Uncertainty Estimation via Gaussian Splatting](https://arxiv.org/abs/2504.01957v2)**  
  Authors: Shu-Wei Lu, Yi-Hsuan Tsai, Yi-Ting Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01957v2.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, autonomous driving, fast  
- **[BOGausS: Better Optimized Gaussian Splatting](https://arxiv.org/abs/2504.01844v1)**  
  Authors: Stéphane Pateux, Matthieu Gendrin, Luce Morin, Théo Ladune, Xiaoran Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01844v1.pdf)  
  Keywords: 3d gaussian, ar, nerf, efficient, gaussian splatting, high-fidelity, fast  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v1)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v1.pdf)  
  Keywords: reflection, ar, nerf, motion, gaussian splatting, outdoor  
- **[FlowR: Flowing from Sparse to Dense 3D Reconstructions](https://arxiv.org/abs/2504.01647v1)**  
  Authors: Tobias Fischer, Samuel Rota Bulò, Yung-Hsu Yang, Nikhil Varma Keetha, Lorenzo Porzi, Norman Müller, Katja Schwarz, Jonathon Luiten, Marc Pollefeys, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01647v1.pdf)  
  Keywords: 3d gaussian, ar, vr, 3d reconstruction, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 541 papers*

- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: 3d gaussian, mapping, ar, localization, face, dynamic, slam, gaussian splatting, tracking, fast  
- **[ConsDreamer: Advancing Multi-View Consistency for Zero-Shot Text-to-3D Generation](https://arxiv.org/abs/2504.02316v1)**  
  Authors: Yuan Zhou, Shilong Jin, Litao Hua, Wanjun Lv, Haoran Duan, Jungong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02316v1.pdf)  
  Keywords: 3d gaussian, ar, face, gaussian splatting  
- **[UAVTwin: Neural Digital Twins for UAVs using Gaussian Splatting](https://arxiv.org/abs/2504.02158v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02158v1.pdf)  
  Keywords: 3d gaussian, high quality, human, ar, dynamic, motion, gaussian splatting, high-fidelity, neural rendering  
- **[RealityAvatar: Towards Realistic Loose Clothing Modeling in Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2504.01559v1)**  
  Authors: Yahui Li, Zhi Zeng, Liming Pang, Guixuan Zhang, Shuwu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01559v1.pdf)  
  Keywords: 3d gaussian, human, ar, nerf, dynamic, motion, efficient, gaussian splatting, high-fidelity, avatar, deformation  
- **[High-fidelity 3D Object Generation from Single Image with RGBN-Volume Gaussian Reconstruction Model](https://arxiv.org/abs/2504.01512v1)**  
  Authors: Yiyang Shen, Kun Zhou, He Wang, Yin Yang, Tianjia Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01512v1.pdf)  
  Keywords: 3d gaussian, ar, face, gaussian splatting, high-fidelity  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: 3d gaussian, illumination, lighting, ar, face, real-time rendering, efficient, gaussian splatting, global illumination, ray tracing  
- **[DropGaussian: Structural Regularization for Sparse-view Gaussian Splatting](https://arxiv.org/abs/2504.00773v1)**  
  Authors: Hyunwoo Park, Gun Ryu, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DCVL-3D/DropGaussian?style=social)](https://github.com/DCVL-3D/DropGaussian)  
  Keywords: 3d gaussian, sparse-view, ar, face, gaussian splatting, fast  
- **[Monocular and Generalizable Gaussian Talking Head Animation](https://arxiv.org/abs/2504.00665v1)**  
  Authors: Shengjie Gong, Haojie Li, Jiapeng Tang, Dongming Hu, Shuangping Huang, Hao Chen, Tianshui Chen, Zhuoman Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00665v1.pdf)  
  Keywords: 3d gaussian, animation, ar, head, gaussian splatting  
- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: sparse-view, ar, face, 3d reconstruction, geometry, gaussian splatting, neural rendering  
- **[Visual Acoustic Fields](https://arxiv.org/abs/2503.24270v2)**  
  Authors: Yuelei Li, Hyunjin Kim, Fangneng Zhan, Ri-Zhao Qiu, Mazeyu Ji, Xiaojun Shan, Xueyan Zou, Paul Liang, Hanspeter Pfister, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24270v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuelei0428.github.io/projects/Visual-Acoustic-Fields/.)  
  Keywords: 3d gaussian, human, ar, localization, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 606 papers*

- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: 3d gaussian, mapping, ar, localization, face, dynamic, slam, gaussian splatting, tracking, fast  
- **[UAVTwin: Neural Digital Twins for UAVs using Gaussian Splatting](https://arxiv.org/abs/2504.02158v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02158v1.pdf)  
  Keywords: 3d gaussian, high quality, human, ar, dynamic, motion, gaussian splatting, high-fidelity, neural rendering  
- **[Diffusion-Guided Gaussian Splatting for Large-Scale Unconstrained 3D Reconstruction and Novel View Synthesis](https://arxiv.org/abs/2504.01960v1)**  
  Authors: Niluthpol Chowdhury Mithun, Tuan Pham, Qiao Wang, Ben Southall, Kshitij Minhas, Bogdan Matei, Stephan Mandt, Supun Samarasekera, Rakesh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01960v1.pdf)  
  Keywords: 3d gaussian, ar, nerf, 3d reconstruction, dynamic, gaussian splatting  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v1)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v1.pdf)  
  Keywords: reflection, ar, nerf, motion, gaussian splatting, outdoor  
- **[RealityAvatar: Towards Realistic Loose Clothing Modeling in Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2504.01559v1)**  
  Authors: Yahui Li, Zhi Zeng, Liming Pang, Guixuan Zhang, Shuwu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01559v1.pdf)  
  Keywords: 3d gaussian, human, ar, nerf, dynamic, motion, efficient, gaussian splatting, high-fidelity, avatar, deformation  
- **[UnIRe: Unsupervised Instance Decomposition for Dynamic Urban Scene Reconstruction](https://arxiv.org/abs/2504.00763v1)**  
  Authors: Yunxuan Mao, Rong Xiong, Yue Wang, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00763v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, ar, urban scene, dynamic, 4d, gaussian splatting  
- **[Monocular and Generalizable Gaussian Talking Head Animation](https://arxiv.org/abs/2504.00665v1)**  
  Authors: Shengjie Gong, Haojie Li, Jiapeng Tang, Dongming Hu, Shuangping Huang, Hao Chen, Tianshui Chen, Zhuoman Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00665v1.pdf)  
  Keywords: 3d gaussian, animation, ar, head, gaussian splatting  
- **[Scene4U: Hierarchical Layered 3D Scene Reconstruction from Single Panoramic Image for Your Immerse Exploration](https://arxiv.org/abs/2504.00387v1)**  
  Authors: Zilong Huang, Jun He, Junyan Ye, Lihan Jiang, Weijia Li, Yiping Chen, Ting Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00387v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LongHZ140516/Scene4U?style=social)](https://github.com/LongHZ140516/Scene4U)  
  Keywords: 3d gaussian, ar, semantic, dynamic, gaussian splatting, segmentation, fast  
- **[LITA-GS: Illumination-Agnostic Novel View Synthesis via Reference-Free 3D Gaussian Splatting and Physical Priors](https://arxiv.org/abs/2504.00219v1)**  
  Authors: Han Zhou, Wei Dong, Jun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00219v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LowLevelAI/LITA-GS?style=social)](https://github.com/LowLevelAI/LITA-GS)  
  Keywords: 3d gaussian, illumination, lighting, ar, nerf, motion, gaussian splatting, fast  
- **[DiET-GS: Diffusion Prior and Event Stream-Assisted Motion Deblurring 3D Gaussian Splatting](https://arxiv.org/abs/2503.24210v1)**  
  Authors: Seungjun Lee, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24210v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://diet-gs.github.io)  
  Keywords: 3d gaussian, ar, dynamic, motion, gaussian splatting  

### Few-shot

*Showing the latest 50 out of 113 papers*

- **[DropGaussian: Structural Regularization for Sparse-view Gaussian Splatting](https://arxiv.org/abs/2504.00773v1)**  
  Authors: Hyunwoo Park, Gun Ryu, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DCVL-3D/DropGaussian?style=social)](https://github.com/DCVL-3D/DropGaussian)  
  Keywords: 3d gaussian, sparse-view, ar, face, gaussian splatting, fast  
- **[Coca-Splat: Collaborative Optimization for Camera Parameters and 3D Gaussians](https://arxiv.org/abs/2504.00639v1)**  
  Authors: Jiamin Wu, Hongyang Li, Xiaoke Jiang, Yuan Yao, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00639v1.pdf)  
  Keywords: 3d gaussian, ar, sparse view  
- **[Distilling Multi-view Diffusion Models into 3D Generators](https://arxiv.org/abs/2504.00457v3)**  
  Authors: Hao Qin, Luyuan Chen, Ming Kong, Mengxu Lu, Qiang Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00457v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://qinbaigao.github.io/DD3G_project/)  
  Keywords: 3d gaussian, sparse-view, ar, efficient, gaussian splatting  
- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: sparse-view, ar, face, 3d reconstruction, geometry, gaussian splatting, neural rendering  
- **[FreeSplat++: Generalizable 3D Gaussian Splatting for Efficient Indoor Scene Reconstruction](https://arxiv.org/abs/2503.22986v1)**  
  Authors: Yunsong Wang, Tianxin Huang, Hanlin Chen, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22986v1.pdf)  
  Keywords: 3d gaussian, ar, efficient, sparse view, gaussian splatting  
- **[CoMapGS: Covisibility Map-based Gaussian Splatting for Sparse Novel View Synthesis](https://arxiv.org/abs/2503.20998v1)**  
  Authors: Youngkyoon Jang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20998v1.pdf)  
  Keywords: nerf, ar, few-shot, gaussian splatting  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: 3d gaussian, illumination, sparse-view, ar, gaussian splatting, outdoor  
- **[NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting](https://arxiv.org/abs/2503.18794v1)**  
  Authors: Yulong Zheng, Zicheng Jiang, Shengfeng He, Yandu Sun, Junyu Dong, Huaidong Zhang, Yong Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18794v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://usmizuki.github.io/NexusGS/.)  
  Keywords: 3d gaussian, sparse-view, ar, nerf, geometry, sparse view, gaussian splatting, few-shot  
- **[SplatVoxel: History-Aware Novel View Streaming without Temporal Training](https://arxiv.org/abs/2503.14698v1)**  
  Authors: Yiming Wang, Lucy Chai, Xuan Luo, Michael Niemeyer, Manuel Lagunas, Stephen Lombardi, Siyu Tang, Tiancheng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14698v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://19reborn.github.io/SplatVoxel/)  
  Keywords: sparse-view, ar, motion, efficient, gaussian splatting, tracking  
- **[RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2503.14198v1)**  
  Authors: Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14198v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iSEE-Laboratory/RoGSplat?style=social)](https://github.com/iSEE-Laboratory/RoGSplat)  
  Keywords: 3d gaussian, human, ar, geometry, sparse view, gaussian splatting, high-fidelity, body  

### Geometry Reconstruction

*Showing the latest 50 out of 513 papers*

- **[Diffusion-Guided Gaussian Splatting for Large-Scale Unconstrained 3D Reconstruction and Novel View Synthesis](https://arxiv.org/abs/2504.01960v1)**  
  Authors: Niluthpol Chowdhury Mithun, Tuan Pham, Qiao Wang, Ben Southall, Kshitij Minhas, Bogdan Matei, Stephan Mandt, Supun Samarasekera, Rakesh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01960v1.pdf)  
  Keywords: 3d gaussian, ar, nerf, 3d reconstruction, dynamic, gaussian splatting  
- **[FlowR: Flowing from Sparse to Dense 3D Reconstructions](https://arxiv.org/abs/2504.01647v1)**  
  Authors: Tobias Fischer, Samuel Rota Bulò, Yung-Hsu Yang, Nikhil Varma Keetha, Lorenzo Porzi, Norman Müller, Katja Schwarz, Jonathon Luiten, Marc Pollefeys, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01647v1.pdf)  
  Keywords: 3d gaussian, ar, vr, 3d reconstruction, gaussian splatting  
- **[ADGaussian: Generalizable Gaussian Splatting for Autonomous Driving with Multi-modal Inputs](https://arxiv.org/abs/2504.00437v1)**  
  Authors: Qi Song, Chenghong Li, Haotong Lin, Sida Peng, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00437v1.pdf)  
  Keywords: ar, gaussian splatting, efficient, geometry, autonomous driving  
- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: sparse-view, ar, face, 3d reconstruction, geometry, gaussian splatting, neural rendering  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: reflection, ar, nerf, dynamic, efficient, geometry, gaussian splatting, outdoor, high-fidelity, fast  
- **[LandMarkSystem Technical Report](https://arxiv.org/abs/2503.21364v2)**  
  Authors: Zhenxiang Ma, Zhenyu Yang, Miao Tao, Yuanzhen Zhou, Zeyu He, Yuchang Zhang, Rong Fu, Hengjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21364v2.pdf) | [![GitHub](https://img.shields.io/github/stars/InternLandMark/LandMarkSystem?style=social)](https://github.com/InternLandMark/LandMarkSystem)  
  Keywords: 3d gaussian, autonomous driving, ar, nerf, 3d reconstruction, dynamic, efficient, gaussian splatting  
- **[Frequency-Aware Gaussian Splatting Decomposition](https://arxiv.org/abs/2503.21226v1)**  
  Authors: Yishai Lavi, Leo Segre, Shai Avidan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21226v1.pdf)  
  Keywords: 3d gaussian, ar, dynamic, efficient, geometry, gaussian splatting, fast  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: ar, urban scene, dynamic, motion, geometry, gaussian splatting  
- **[EVPGS: Enhanced View Prior Guidance for Splatting-based Extrapolated View Synthesis](https://arxiv.org/abs/2503.21816v1)**  
  Authors: Jiahe Li, Feiyu Wang, Xiaochao Qu, Chengjing Wu, Luoqi Liu, Ting Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21816v1.pdf)  
  Keywords: ar, geometry, gaussian splatting  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: 3d gaussian, ar, face, 3d reconstruction, 4d, gaussian splatting, tracking, deformation  

### Large Scene

*Showing the latest 50 out of 89 papers*

- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v1)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v1.pdf)  
  Keywords: reflection, ar, nerf, motion, gaussian splatting, outdoor  
- **[UnIRe: Unsupervised Instance Decomposition for Dynamic Urban Scene Reconstruction](https://arxiv.org/abs/2504.00763v1)**  
  Authors: Yunxuan Mao, Rong Xiong, Yue Wang, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00763v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, ar, urban scene, dynamic, 4d, gaussian splatting  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: reflection, ar, nerf, dynamic, efficient, geometry, gaussian splatting, outdoor, high-fidelity, fast  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: ar, urban scene, dynamic, motion, geometry, gaussian splatting  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, ar, urban scene, nerf, real-time rendering, efficient, gaussian splatting, fast  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: 3d gaussian, illumination, sparse-view, ar, gaussian splatting, outdoor  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: ar, localization, efficient, gaussian splatting, outdoor  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: 3d gaussian, ar, real-time rendering, efficient, geometry, gaussian splatting, outdoor, fast  
- **[PanopticSplatting: End-to-End Panoptic Gaussian Splatting](https://arxiv.org/abs/2503.18073v1)**  
  Authors: Yuxuan Xie, Xuan Yu, Changjian Jiang, Sitong Mao, Shunbo Zhou, Rui Fan, Rong Xiong, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18073v1.pdf)  
  Keywords: ar, large scene, nerf, gaussian splatting, understanding, segmentation  
- **[GaussianFocus: Constrained Attention Focus for 3D Gaussian Splatting](https://arxiv.org/abs/2503.17798v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17798v1.pdf)  
  Keywords: 3d gaussian, ar, large scene, 3d reconstruction, gaussian splatting, neural rendering  

### Model Compression

*Showing the latest 50 out of 607 papers*

- **[BOGausS: Better Optimized Gaussian Splatting](https://arxiv.org/abs/2504.01844v1)**  
  Authors: Stéphane Pateux, Matthieu Gendrin, Luce Morin, Théo Ladune, Xiaoran Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01844v1.pdf)  
  Keywords: 3d gaussian, ar, nerf, efficient, gaussian splatting, high-fidelity, fast  
- **[RealityAvatar: Towards Realistic Loose Clothing Modeling in Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2504.01559v1)**  
  Authors: Yahui Li, Zhi Zeng, Liming Pang, Guixuan Zhang, Shuwu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01559v1.pdf)  
  Keywords: 3d gaussian, human, ar, nerf, dynamic, motion, efficient, gaussian splatting, high-fidelity, avatar, deformation  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: 3d gaussian, illumination, lighting, ar, face, real-time rendering, efficient, gaussian splatting, global illumination, ray tracing  
- **[Distilling Multi-view Diffusion Models into 3D Generators](https://arxiv.org/abs/2504.00457v3)**  
  Authors: Hao Qin, Luyuan Chen, Ming Kong, Mengxu Lu, Qiang Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00457v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://qinbaigao.github.io/DD3G_project/)  
  Keywords: 3d gaussian, sparse-view, ar, efficient, gaussian splatting  
- **[ADGaussian: Generalizable Gaussian Splatting for Autonomous Driving with Multi-modal Inputs](https://arxiv.org/abs/2504.00437v1)**  
  Authors: Qi Song, Chenghong Li, Haotong Lin, Sida Peng, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00437v1.pdf)  
  Keywords: ar, gaussian splatting, efficient, geometry, autonomous driving  
- **[SonarSplat: Novel View Synthesis of Imaging Sonar via Gaussian Splatting](https://arxiv.org/abs/2504.00159v1)**  
  Authors: Advaith V. Sethuraman, Max Rucker, Onur Bagoren, Pou-Chun Kung, Nibarkavi N. B. Amutha, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00159v1.pdf)  
  Keywords: 3d gaussian, efficient, ar, gaussian splatting  
- **[ERUPT: Efficient Rendering with Unposed Patch Transformer](https://arxiv.org/abs/2503.24374v1)**  
  Authors: Maxim V. Shugaev, Vincent Chen, Maxim Karrenbach, Kyle Ashley, Bridget Kennedy, Naresh P. Cuntoor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24374v1.pdf)  
  Keywords: ar, nerf, efficient, gaussian splatting, efficient rendering  
- **[StochasticSplats: Stochastic Rasterization for Sorting-Free 3D Gaussian Splatting](https://arxiv.org/abs/2503.24366v1)**  
  Authors: Shakiba Kheradmand, Delio Vicini, George Kopanas, Dmitry Lagun, Kwang Moo Yi, Mark Matthews, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24366v1.pdf)  
  Keywords: 3d gaussian, fast, ar, efficient, gaussian splatting, efficient rendering  
- **[Enhancing 3D Gaussian Splatting Compression via Spatial Condition-based Prediction](https://arxiv.org/abs/2503.23337v1)**  
  Authors: Jingui Ma, Yang Hu, Luyang Tang, Jiayu Yang, Yongqi Zhai, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23337v1.pdf)  
  Keywords: 3d gaussian, ar, real-time rendering, compression, gaussian splatting  
- **[NeuralGS: Bridging Neural Fields and 3D Gaussian Splatting for Compact 3D Representations](https://arxiv.org/abs/2503.23162v1)**  
  Authors: Zhenyu Tang, Chaoran Feng, Xinhua Cheng, Wangbo Yu, Junwu Zhang, Yuan Liu, Xiaoxiao Long, Wenping Wang, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23162v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, nerf, compact, compression  

### Quality Enhancement

*Showing the latest 50 out of 261 papers*

- **[UAVTwin: Neural Digital Twins for UAVs using Gaussian Splatting](https://arxiv.org/abs/2504.02158v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02158v1.pdf)  
  Keywords: 3d gaussian, high quality, human, ar, dynamic, motion, gaussian splatting, high-fidelity, neural rendering  
- **[BOGausS: Better Optimized Gaussian Splatting](https://arxiv.org/abs/2504.01844v1)**  
  Authors: Stéphane Pateux, Matthieu Gendrin, Luce Morin, Théo Ladune, Xiaoran Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01844v1.pdf)  
  Keywords: 3d gaussian, ar, nerf, efficient, gaussian splatting, high-fidelity, fast  
- **[RealityAvatar: Towards Realistic Loose Clothing Modeling in Animatable 3D Gaussian Avatars](https://arxiv.org/abs/2504.01559v1)**  
  Authors: Yahui Li, Zhi Zeng, Liming Pang, Guixuan Zhang, Shuwu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01559v1.pdf)  
  Keywords: 3d gaussian, human, ar, nerf, dynamic, motion, efficient, gaussian splatting, high-fidelity, avatar, deformation  
- **[High-fidelity 3D Object Generation from Single Image with RGBN-Volume Gaussian Reconstruction Model](https://arxiv.org/abs/2504.01512v1)**  
  Authors: Yiyang Shen, Kun Zhou, He Wang, Yin Yang, Tianjia Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01512v1.pdf)  
  Keywords: 3d gaussian, ar, face, gaussian splatting, high-fidelity  
- **[ExScene: Free-View 3D Scene Reconstruction with Gaussian Splatting from a Single Image](https://arxiv.org/abs/2503.23881v1)**  
  Authors: Tianyi Gong, Boyan Li, Yifei Zhong, Fangxin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23881v1.pdf)  
  Keywords: 3d gaussian, ar, high-fidelity, gaussian splatting  
- **[X$^{2}$-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction](https://arxiv.org/abs/2503.21779v1)**  
  Authors: Weihao Yu, Yuanhao Cai, Ruyi Zha, Zhiwen Fan, Chenxin Li, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://x2-gaussian.github.io/.)  
  Keywords: ar, face, dynamic, motion, 4d, gaussian splatting, high-fidelity, deformation  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: reflection, ar, nerf, dynamic, efficient, geometry, gaussian splatting, outdoor, high-fidelity, fast  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: 3d gaussian, mapping, ar, localization, semantic, slam, dynamic, robotics, high-fidelity  
- **[LLGS: Unsupervised Gaussian Splatting for Image Enhancement and Reconstruction in Pure Dark Environment](https://arxiv.org/abs/2503.18640v1)**  
  Authors: Haoran Wang, Jingwei Huang, Lu Yang, Tianchen Deng, Gaojing Zhang, Mingrui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18640v1.pdf)  
  Keywords: 3d gaussian, ar, robotics, gaussian splatting, high-fidelity  
- **[Unraveling the Effects of Synthetic Data on End-to-End Autonomous Driving](https://arxiv.org/abs/2503.18108v1)**  
  Authors: Junhao Ge, Zuhong Liu, Longteng Fan, Yifan Jiang, Jiaqi Su, Yiming Li, Zhejun Zhang, Siheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18108v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, ar, face, nerf, dynamic, efficient, gaussian splatting, high-fidelity  

### Ray Tracing

- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: 3d gaussian, illumination, lighting, ar, face, real-time rendering, efficient, gaussian splatting, global illumination, ray tracing  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: 3d gaussian, illumination, light transport, lighting, face, dynamic, real-time rendering, global illumination, fast  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: 3d gaussian, reflection, ar, gaussian splatting, ray tracing, shadow, fast, neural rendering  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: lighting, ar, face, dynamic, real-time rendering, efficient, geometry, 4d, relightable, tracking, ray tracing  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: reflection, lighting, face, gaussian splatting, ray tracing, shadow  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, survey, ar, gaussian splatting, ray tracing  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: acceleration, reflection, light transport, ar, efficient, gaussian splatting, ray tracing  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: 3d gaussian, reflection, ar, gaussian splatting, ray tracing, shadow  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v2)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v2.pdf)  
  Keywords: reflection, lighting, ar, efficient, relighting, gaussian splatting, ray tracing  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v2)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v2.pdf) | [![GitHub](https://img.shields.io/github/stars/nv-tlabs/3dgrut?style=social)](https://github.com/nv-tlabs/3dgrut)  
  Keywords: 3d gaussian, reflection, lighting, ar, real-time rendering, efficient, gaussian splatting, high-fidelity, ray tracing  

### Relighting

*Showing the latest 50 out of 176 papers*

- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v1)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v1.pdf)  
  Keywords: reflection, ar, nerf, motion, gaussian splatting, outdoor  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: 3d gaussian, mapping, lighting, ar, nerf, real-time rendering, gaussian splatting  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: 3d gaussian, illumination, lighting, ar, face, real-time rendering, efficient, gaussian splatting, global illumination, ray tracing  
- **[LITA-GS: Illumination-Agnostic Novel View Synthesis via Reference-Free 3D Gaussian Splatting and Physical Priors](https://arxiv.org/abs/2504.00219v1)**  
  Authors: Han Zhou, Wei Dong, Jun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00219v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LowLevelAI/LITA-GS?style=social)](https://github.com/LowLevelAI/LITA-GS)  
  Keywords: 3d gaussian, illumination, lighting, ar, nerf, motion, gaussian splatting, fast  
- **[Learning 3D-Gaussian Simulators from RGB Videos](https://arxiv.org/abs/2503.24009v1)**  
  Authors: Mikel Zhobro, Andreas René Geist, Georg Martius  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24009v1.pdf)  
  Keywords: 3d gaussian, lighting, ar, dynamic, gaussian splatting, body  
- **[TranSplat: Lighting-Consistent Cross-Scene Object Transfer with 3D Gaussian Splatting](https://arxiv.org/abs/2503.22676v1)**  
  Authors: Boyang, Yu, Yanlin Jin, Ashok Veeraraghavan, Akshat Dave, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22676v1.pdf)  
  Keywords: 3d gaussian, lighting, ar, relighting, gaussian splatting, segmentation  
- **[Follow Your Motion: A Generic Temporal Consistency Portrait Editing Framework with Trajectory Guidance](https://arxiv.org/abs/2503.22225v1)**  
  Authors: Haijie Yang, Zhenyu Zhang, Hao Tang, Jianjun Qian, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22225v1.pdf)  
  Keywords: 3d gaussian, lighting, ar, face, dynamic, motion, efficient, head, relighting, gaussian splatting, avatar  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: reflection, ar, nerf, dynamic, efficient, geometry, gaussian splatting, outdoor, high-fidelity, fast  
- **[PGC: Physics-Based Gaussian Cloth from a Single Pose](https://arxiv.org/abs/2503.20779v1)**  
  Authors: Michelle Guo, Matt Jen-Yuan Chiang, Igor Santesteban, Nikolaos Sarafianos, Hsiao-yu Chen, Oshri Halimi, Aljaž Božič, Shunsuke Saito, Jiajun Wu, C. Karen Liu, Tuur Stuyck, Egor Larionov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys-gaussian-cloth.github.io)  
  Keywords: 3d gaussian, lighting, ar, face, relighting, body  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: 3d gaussian, lighting, survey, ar, dynamic, 3d reconstruction, motion, gaussian splatting, fast  

### SLAM

*Showing the latest 50 out of 239 papers*

- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: 3d gaussian, mapping, ar, localization, face, dynamic, slam, gaussian splatting, tracking, fast  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: 3d gaussian, mapping, lighting, ar, nerf, real-time rendering, gaussian splatting  
- **[Visual Acoustic Fields](https://arxiv.org/abs/2503.24270v2)**  
  Authors: Yuelei Li, Hyunjin Kim, Fangneng Zhan, Ri-Zhao Qiu, Mazeyu Ji, Xiaojun Shan, Xueyan Zou, Paul Liang, Hanspeter Pfister, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24270v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuelei0428.github.io/projects/Visual-Acoustic-Fields/.)  
  Keywords: 3d gaussian, human, ar, localization, gaussian splatting  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: 3d gaussian, ar, localization, semantic, robotics, gaussian splatting, understanding, segmentation  
- **[VizFlyt: Perception-centric Pedagogical Framework For Autonomous Aerial Robots](https://arxiv.org/abs/2503.22876v2)**  
  Authors: Kushagra Srivastava, Rutwik Kulkarni, Manoj Velmurugan, Nitin J. Sanket  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22876v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pear.wpi.edu/research/vizflyt.html)  
  Keywords: 3d gaussian, ar, localization, robotics, efficient, gaussian splatting  
- **[Time-resolved dynamic CBCT reconstruction using prior-model-free spatiotemporal Gaussian representation (PMF-STGR)](https://arxiv.org/abs/2503.22139v1)**  
  Authors: Jiacheng Xie, Hua-Chieh Shao, You Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22139v1.pdf)  
  Keywords: 3d gaussian, ar, localization, dynamic, motion, efficient, fast, deformation  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: 3d gaussian, mapping, ar, localization, semantic, slam, dynamic, robotics, high-fidelity  
- **[Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields](https://arxiv.org/abs/2503.19976v1)**  
  Authors: Navami Kairanda, Marc Habermann, Shanthika Naik, Christian Theobalt, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19976v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpiinf.mpg.de/ThinShellSfT.)  
  Keywords: 3d gaussian, ar, face, 3d reconstruction, 4d, gaussian splatting, tracking, deformation  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: ar, localization, efficient, gaussian splatting, outdoor  
- **[GI-SLAM: Gaussian-Inertial SLAM](https://arxiv.org/abs/2503.18275v1)**  
  Authors: Xulang Liu, Ning Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.18275v1.pdf)  
  Keywords: 3d gaussian, mapping, ar, localization, slam, real-time rendering, geometry, gaussian splatting, tracking  

### Scene Understanding

*Showing the latest 50 out of 280 papers*

- **[Scene4U: Hierarchical Layered 3D Scene Reconstruction from Single Panoramic Image for Your Immerse Exploration](https://arxiv.org/abs/2504.00387v1)**  
  Authors: Zilong Huang, Jun He, Junyan Ye, Lihan Jiang, Weijia Li, Yiping Chen, Ting Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00387v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LongHZ140516/Scene4U?style=social)](https://github.com/LongHZ140516/Scene4U)  
  Keywords: 3d gaussian, ar, semantic, dynamic, gaussian splatting, segmentation, fast  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: 3d gaussian, ar, localization, semantic, robotics, gaussian splatting, understanding, segmentation  
- **[TranSplat: Lighting-Consistent Cross-Scene Object Transfer with 3D Gaussian Splatting](https://arxiv.org/abs/2503.22676v1)**  
  Authors: Boyang, Yu, Yanlin Jin, Ashok Veeraraghavan, Akshat Dave, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22676v1.pdf)  
  Keywords: 3d gaussian, lighting, ar, relighting, gaussian splatting, segmentation  
- **[ABC-GS: Alignment-Based Controllable Style Transfer for 3D Gaussian Splatting](https://arxiv.org/abs/2503.22218v1)**  
  Authors: Wenjie Liu, Zhongliang Liu, Xiaoyan Yang, Man Sha, Yang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22218v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vpx-ecnu.github.io/ABC-GS-website.)  
  Keywords: 3d gaussian, ar, nerf, gaussian splatting, segmentation  
- **[Segment then Splat: A Unified Approach for 3D Open-Vocabulary Segmentation based on Gaussian Splatting](https://arxiv.org/abs/2503.22204v1)**  
  Authors: Yiren Lu, Yunlai Zhou, Yiran Qiao, Chaoda Song, Tuo Liang, Jing Ma, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22204v1.pdf)  
  Keywords: ar, dynamic, motion, robotics, gaussian splatting, segmentation  
- **[Semantic Consistent Language Gaussian Splatting for Point-Level Open-vocabulary Querying](https://arxiv.org/abs/2503.21767v1)**  
  Authors: Hairong Yin, Huangying Zhan, Yi Xu, Raymond A. Yeh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21767v1.pdf)  
  Keywords: 3d gaussian, ar, semantic, gaussian splatting, segmentation  
- **[STAMICS: Splat, Track And Map with Integrated Consistency and Semantics for Dense RGB-D SLAM](https://arxiv.org/abs/2503.21425v1)**  
  Authors: Yongxu Wang, Xu Cao, Weiyun Yi, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21425v1.pdf)  
  Keywords: 3d gaussian, mapping, ar, localization, semantic, slam, dynamic, robotics, high-fidelity  
- **[Feature4X: Bridging Any Monocular Video to 4D Agentic AI with Versatile Gaussian Feature Fields](https://arxiv.org/abs/2503.20776v2)**  
  Authors: Shijie Zhou, Hui Ren, Yijia Weng, Shuwang Zhang, Zhen Wang, Dejia Xu, Zhiwen Fan, Suya You, Zhangyang Wang, Leonidas Guibas, Achuta Kadambi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20776v2.pdf)  
  Keywords: ar, semantic, dynamic, 4d, gaussian splatting, segmentation  
- **[PartRM: Modeling Part-Level Dynamics with Large Cross-State Reconstruction Model](https://arxiv.org/abs/2503.19913v1)**  
  Authors: Mingju Gao, Yike Pan, Huan-ang Gao, Zongzheng Zhang, Wenyi Li, Hao Dong, Hao Tang, Li Yi, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19913v1.pdf)  
  Keywords: 3d gaussian, ar, dynamic, motion, robotics, geometry, 4d, understanding  
- **[COB-GS: Clear Object Boundaries in 3DGS Segmentation Based on Boundary-Adaptive Gaussian Splitting](https://arxiv.org/abs/2503.19443v2)**  
  Authors: Jiaxin Zhang, Junjun Jiang, Youyu Chen, Kui Jiang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19443v2.pdf) | [![GitHub](https://img.shields.io/github/stars/ZestfulJX/COB-GS?style=social)](https://github.com/ZestfulJX/COB-GS)  
  Keywords: 3d gaussian, ar, semantic, gaussian splatting, understanding, segmentation  



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