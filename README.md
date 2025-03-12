# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-03-12 00:49:08

## Categories

- [3DGS Surveys](#3dgs-surveys) (24 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (405 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1427 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (478 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (527 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (99 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (475 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (75 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (538 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (232 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (33 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (159 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (214 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (251 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: survey, ar, geometry, semantic  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: 3d reconstruction, real-time rendering, 3d gaussian, survey, efficient, gaussian splatting, compression, nerf, ar  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: motion, survey, dynamic, gaussian splatting, 4d, lighting, deformation, nerf, ar  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, 3d gaussian, survey, gaussian splatting, ar  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: localization, 3d gaussian, survey, dynamic, outdoor, geometry, face, lighting, tracking, mapping, slam, ar, reflection  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: 3d gaussian, survey, gaussian splatting, recognition, illumination, ar  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: 3d reconstruction, compact, high-fidelity, survey, dynamic, gaussian splatting, geometry, semantic, robotics, lighting, nerf, ar, autonomous driving  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: real-time rendering, 3d gaussian, survey, gaussian splatting, robotics, understanding, nerf, ar  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, survey, gaussian splatting, lighting, nerf, ar  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: vr, 3d reconstruction, 3d gaussian, survey, gaussian splatting, robotics, nerf, ar, autonomous driving  

### Acceleration

*Showing the latest 50 out of 405 papers*

- **[Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields](https://arxiv.org/abs/2503.06762v1)**  
  Authors: Abdelaziz Bouzidi, Hamid Laga, Hazem Wannous  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06762v1.pdf)  
  Keywords: fast, acceleration, 3d reconstruction, compact, efficient, gaussian splatting, geometry, lightweight, ar  
- **[Pixel to Gaussian: Ultra-Fast Continuous Super-Resolution with 2D Gaussian Modeling](https://arxiv.org/abs/2503.06617v1)**  
  Authors: Long Peng, Anran Wu, Wenbo Li, Peizhe Xia, Xueyuan Dai, Xinjie Zhang, Xin Di, Haoze Sun, Renjing Pei, Yang Wang, Yang Cao, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06617v1.pdf)  
  Keywords: fast, gaussian splatting, ar, mapping  
- **[StreamGS: Online Generalizable Gaussian Splatting Reconstruction for Unposed Image Streams](https://arxiv.org/abs/2503.06235v1)**  
  Authors: Yang LI, Jinglu Wang, Lei Chu, Xiao Li, Shiu-hong Kao, Ying-Cong Chen, Yan Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06235v1.pdf)  
  Keywords: 3d gaussian, fast, gaussian splatting, ar  
- **[ForestSplats: Deformable transient field for Gaussian Splatting in the Wild](https://arxiv.org/abs/2503.06179v1)**  
  Authors: Wongi Park, Myeongseok Nam, Siwon Kim, Sangwoo Jo, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06179v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, efficient, semantic, gaussian splatting, lighting, ar  
- **[SecureGS: Boosting the Security and Fidelity of 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2503.06118v1)**  
  Authors: Xuanyu Zhang, Jiarui Meng, Zhipei Xu, Shuzhou Yang, Yanmin Wu, Ronggang Wang, Jian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06118v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, efficient, gaussian splatting, nerf, ar  
- **[D2GV: Deformable 2D Gaussian Splatting for Video Representation in 400FPS](https://arxiv.org/abs/2503.05600v1)**  
  Authors: Mufan Liu, Qi Yang, Miaoran Zhao, He Huang, Le Yang, Zhu Li, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05600v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Evan-sudo/D2GV?style=social)](https://github.com/Evan-sudo/D2GV)  
  Keywords: fast, compact, efficient, gaussian splatting, compression, ar  
- **[CoMoGaussian: Continuous Motion-Aware Gaussian Splatting from Motion-Blurred Images](https://arxiv.org/abs/2503.05332v1)**  
  Authors: Jungho Lee, Donghyeong Kim, Dogyoon Lee, Suhwan Cho, Minhyeok Lee, Wonjoon Lee, Taeoh Kim, Dongyoon Wee, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05332v1.pdf)  
  Keywords: ar, motion, real-time rendering, 3d gaussian, gaussian splatting, body  
- **[SeeLe: A Unified Acceleration Framework for Real-Time Gaussian Splatting](https://arxiv.org/abs/2503.05168v2)**  
  Authors: Xiaotong Huang, He Zhu, Zihan Liu, Weikai Lin, Xiaohong Liu, Zhezhi He, Jingwen Leng, Minyi Guo, Yu Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05168v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, acceleration  
- **[EvolvingGS: High-Fidelity Streamable Volumetric Video via Evolving 3D Gaussian Representation](https://arxiv.org/abs/2503.05162v1)**  
  Authors: Chao Zhang, Yifeng Zhou, Shuheng Wang, Wenfa Li, Degang Wang, Yi Xu, Shaohui Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05162v1.pdf)  
  Keywords: fast, motion, 3d gaussian, high-fidelity, dynamic, gaussian splatting, efficient, human, compression, high quality, ar  
- **[GaussianVideo: Efficient Video Representation and Compression by Gaussian Splatting](https://arxiv.org/abs/2503.04333v1)**  
  Authors: Inseo Lee, Youngyoon Choi, Joonseok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04333v1.pdf)  
  Keywords: fast, dynamic, efficient, gaussian splatting, lightweight, compression, ar  

### Applications

*Showing the latest 50 out of 1427 papers*

- **[SOGS: Second-Order Anchor for Advanced 3D Gaussian Splatting](https://arxiv.org/abs/2503.07476v1)**  
  Authors: Jiahui Zhang, Fangneng Zhan, Ling Shao, Shijian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07476v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar  
- **[EigenGS Representation: From Eigenspace to Gaussian Image Space](https://arxiv.org/abs/2503.07446v1)**  
  Authors: Lo-Wei Tai, Ching-En Li, Cheng-Lin Chen, Chih-Jung Tsai, Hwann-Tzong Chen, Tyng-Luh Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07446v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, ar  
- **[All That Glitters Is Not Gold: Key-Secured 3D Secrets within 3D Gaussian Splatting](https://arxiv.org/abs/2503.07191v1)**  
  Authors: Yan Ren, Shilin Lu, Adams Wai-Kin Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07191v1.pdf) | [![GitHub](https://img.shields.io/github/stars/RY-Paper/KeySS?style=social)](https://github.com/RY-Paper/KeySS)  
  Keywords: 3d gaussian, gaussian splatting, ar, high-fidelity  
- **[Multi-Modal 3D Mesh Reconstruction from Images and Text](https://arxiv.org/abs/2503.07190v1)**  
  Authors: Melvin Reka, Tessa Pulli, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07190v1.pdf)  
  Keywords: 3d reconstruction, few-shot, gaussian splatting, geometry, robotics, ar  
- **[Frequency-Aware Density Control via Reparameterization for High-Quality Rendering of 3D Gaussian Splatting](https://arxiv.org/abs/2503.07000v1)**  
  Authors: Zhaojie Zeng, Yuesong Wang, Lili Ju, Tao Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07000v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, dynamic  
- **[DirectTriGS: Triplane-based Gaussian Splatting Field Representation for 3D Generation](https://arxiv.org/abs/2503.06900v1)**  
  Authors: Xiaoliang Ju, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06900v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry  
- **[ActiveInitSplat: How Active Image Selection Helps Gaussian Splatting](https://arxiv.org/abs/2503.06859v1)**  
  Authors: Konstantinos D. Polyzos, Athanasios Bacharis, Saketh Madhuvarasu, Nikos Papanikolopoulos, Tara Javidi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06859v1.pdf)  
  Keywords: gaussian splatting, ar  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: survey, ar, geometry, semantic  
- **[Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields](https://arxiv.org/abs/2503.06762v1)**  
  Authors: Abdelaziz Bouzidi, Hamid Laga, Hazem Wannous  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06762v1.pdf)  
  Keywords: fast, acceleration, 3d reconstruction, compact, efficient, gaussian splatting, geometry, lightweight, ar  
- **[CoDa-4DGS: Dynamic Gaussian Splatting with Context and Deformation Awareness for Autonomous Driving](https://arxiv.org/abs/2503.06744v1)**  
  Authors: Rui Song, Chenwei Liang, Yan Xia, Walter Zimmer, Hu Cao, Holger Caesar, Andreas Festag, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06744v1.pdf)  
  Keywords: dynamic, semantic, gaussian splatting, 4d, segmentation, deformation, ar, autonomous driving  

### Avatar Generation

*Showing the latest 50 out of 478 papers*

- **[REArtGS: Reconstructing and Generating Articulated Objects via 3D Gaussian Splatting with Geometric and Motion Constraints](https://arxiv.org/abs/2503.06677v1)**  
  Authors: Di Wu, Liu Liu, Zhou Linli, Anran Huang, Liangtu Song, Qiaojun Yu, Qi Wu, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06677v1.pdf)  
  Keywords: motion, 3d gaussian, high-fidelity, dynamic, gaussian splatting, geometry, human, face, ar  
- **[Introducing Unbiased Depth into 2D Gaussian Splatting for High-accuracy Surface Reconstruction](https://arxiv.org/abs/2503.06587v1)**  
  Authors: Xiaoming Peng, Yixin Yang, Yang Zhou, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06587v1.pdf)  
  Keywords: gaussian splatting, geometry, face, ar, reflection  
- **[StructGS: Adaptive Spherical Harmonics and Rendering Enhancements for Superior 3D Gaussian Splatting](https://arxiv.org/abs/2503.06462v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06462v1.pdf)  
  Keywords: 3d reconstruction, head, 3d gaussian, dynamic, gaussian splatting, neural rendering, ar  
- **[SplatTalk: 3D VQA with Gaussian Splatting](https://arxiv.org/abs/2503.06271v1)**  
  Authors: Anh Thai, Songyou Peng, Kyle Genova, Leonidas Guibas, Thomas Funkhouser  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06271v1.pdf)  
  Keywords: vr, 3d gaussian, human, gaussian splatting, robotics, understanding, ar  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v1)**  
  Authors: Jiahui Fan, Fujun Luan, Miloš Hašan, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, human, lightweight, relighting, lighting, high quality, ar, relightable  
- **[Self-Modeling Robots by Photographing](https://arxiv.org/abs/2503.05398v1)**  
  Authors: Kejun Hu, Peng Yu, Ning Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05398v1.pdf)  
  Keywords: motion, 3d gaussian, human, gaussian splatting, deformation, ar  
- **[CoMoGaussian: Continuous Motion-Aware Gaussian Splatting from Motion-Blurred Images](https://arxiv.org/abs/2503.05332v1)**  
  Authors: Jungho Lee, Donghyeong Kim, Dogyoon Lee, Suhwan Cho, Minhyeok Lee, Wonjoon Lee, Taeoh Kim, Dongyoon Wee, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05332v1.pdf)  
  Keywords: ar, motion, real-time rendering, 3d gaussian, gaussian splatting, body  
- **[STGA: Selective-Training Gaussian Head Avatars](https://arxiv.org/abs/2503.05196v1)**  
  Authors: Hanzhi Guo, Yixiao Chen, Dongye Xiaonuo, Zeyu Tian, Dongdong Weng, Le Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05196v1.pdf)  
  Keywords: head, 3d gaussian, dynamic, animation, avatar, ar  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: compact, dynamic, efficient, semantic, human, geometry, tracking, ar  
- **[MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions](https://arxiv.org/abs/2503.05182v1)**  
  Authors: Qingyuan Zhou, Yuehu Gong, Weidong Yang, Jiaze Li, Yeqi Luo, Baixin Xu, Shuhao Li, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05182v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, high-fidelity, gaussian splatting, geometry, face, illumination, ar  

### Dynamic Scene

*Showing the latest 50 out of 527 papers*

- **[Frequency-Aware Density Control via Reparameterization for High-Quality Rendering of 3D Gaussian Splatting](https://arxiv.org/abs/2503.07000v1)**  
  Authors: Zhaojie Zeng, Yuesong Wang, Lili Ju, Tao Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07000v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, dynamic  
- **[CoDa-4DGS: Dynamic Gaussian Splatting with Context and Deformation Awareness for Autonomous Driving](https://arxiv.org/abs/2503.06744v1)**  
  Authors: Rui Song, Chenwei Liang, Yan Xia, Walter Zimmer, Hu Cao, Holger Caesar, Andreas Festag, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06744v1.pdf)  
  Keywords: dynamic, semantic, gaussian splatting, 4d, segmentation, deformation, ar, autonomous driving  
- **[D3DR: Lighting-Aware Object Insertion in Gaussian Splatting](https://arxiv.org/abs/2503.06740v1)**  
  Authors: Vsevolod Skorokhodov, Nikita Durasov, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06740v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, relighting, shadow, lighting, ar  
- **[REArtGS: Reconstructing and Generating Articulated Objects via 3D Gaussian Splatting with Geometric and Motion Constraints](https://arxiv.org/abs/2503.06677v1)**  
  Authors: Di Wu, Liu Liu, Zhou Linli, Anran Huang, Liangtu Song, Qiaojun Yu, Qi Wu, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06677v1.pdf)  
  Keywords: motion, 3d gaussian, high-fidelity, dynamic, gaussian splatting, geometry, human, face, ar  
- **[StructGS: Adaptive Spherical Harmonics and Rendering Enhancements for Superior 3D Gaussian Splatting](https://arxiv.org/abs/2503.06462v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06462v1.pdf)  
  Keywords: 3d reconstruction, head, 3d gaussian, dynamic, gaussian splatting, neural rendering, ar  
- **[Feature-EndoGaussian: Feature Distilled Gaussian Splatting in Surgical Deformable Scene Reconstruction](https://arxiv.org/abs/2503.06161v1)**  
  Authors: Kai Li, Junhao Wang, William Han, Ding Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06161v1.pdf)  
  Keywords: 3d gaussian, dynamic, efficient, gaussian splatting, semantic, segmentation, understanding, deformation, nerf, ar  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v1)**  
  Authors: Jiahui Fan, Fujun Luan, Miloš Hašan, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, human, lightweight, relighting, lighting, high quality, ar, relightable  
- **[LiDAR-enhanced 3D Gaussian Splatting Mapping](https://arxiv.org/abs/2503.05425v1)**  
  Authors: Jian Shen, Huai Yu, Ji Wu, Wen Yang, Gui-Song Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05425v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, geometry, tracking, mapping, ar  
- **[Self-Modeling Robots by Photographing](https://arxiv.org/abs/2503.05398v1)**  
  Authors: Kejun Hu, Peng Yu, Ning Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05398v1.pdf)  
  Keywords: motion, 3d gaussian, human, gaussian splatting, deformation, ar  
- **[CoMoGaussian: Continuous Motion-Aware Gaussian Splatting from Motion-Blurred Images](https://arxiv.org/abs/2503.05332v1)**  
  Authors: Jungho Lee, Donghyeong Kim, Dogyoon Lee, Suhwan Cho, Minhyeok Lee, Wonjoon Lee, Taeoh Kim, Dongyoon Wee, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05332v1.pdf)  
  Keywords: ar, motion, real-time rendering, 3d gaussian, gaussian splatting, body  

### Few-shot

*Showing the latest 50 out of 99 papers*

- **[Multi-Modal 3D Mesh Reconstruction from Images and Text](https://arxiv.org/abs/2503.07190v1)**  
  Authors: Melvin Reka, Tessa Pulli, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07190v1.pdf)  
  Keywords: 3d reconstruction, few-shot, gaussian splatting, geometry, robotics, ar  
- **[GaussianCAD: Robust Self-Supervised CAD Reconstruction from Three Orthographic Views Using 3D Gaussian Splatting](https://arxiv.org/abs/2503.05161v1)**  
  Authors: Zheng Zhou, Zhe Li, Bo Yu, Lina Hu, Liang Dong, Zijian Yang, Xiaoli Liu, Ning Xu, Ziwei Wang, Yonghao Dang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05161v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, gaussian splatting, sparse-view, ar  
- **[S2Gaussian: Sparse-View Super-Resolution 3D Gaussian Splatting](https://arxiv.org/abs/2503.04314v1)**  
  Authors: Yecong Wan, Mingwen Shao, Yuanshuo Cheng, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04314v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, geometry, sparse-view, ar, sparse view  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: few-shot, efficient, semantic, gaussian splatting, human, neural rendering, nerf, ar  
- **[Seeing A 3D World in A Grain of Sand](https://arxiv.org/abs/2503.00260v1)**  
  Authors: Yufan Zhang, Yu Ji, Yu Guo, Jinwei Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00260v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, gaussian splatting, face, ar, sparse view  
- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: 3d reconstruction, 3d gaussian, high-fidelity, efficient, gaussian splatting, ar, sparse view  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, geometry, sparse-view, tracking, mapping, nerf, slam, ar  
- **[DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform](https://arxiv.org/abs/2501.12637v2)**  
  Authors: Hung Nguyen, Blark Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12637v2.pdf)  
  Keywords: fast, head, few-shot, nerf, ar  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: 3d gaussian, semantic, gaussian splatting, 4d, sparse-view, ar  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, efficient, gaussian splatting, sparse-view, nerf, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 475 papers*

- **[Multi-Modal 3D Mesh Reconstruction from Images and Text](https://arxiv.org/abs/2503.07190v1)**  
  Authors: Melvin Reka, Tessa Pulli, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07190v1.pdf)  
  Keywords: 3d reconstruction, few-shot, gaussian splatting, geometry, robotics, ar  
- **[DirectTriGS: Triplane-based Gaussian Splatting Field Representation for 3D Generation](https://arxiv.org/abs/2503.06900v1)**  
  Authors: Xiaoliang Ju, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06900v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: survey, ar, geometry, semantic  
- **[Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields](https://arxiv.org/abs/2503.06762v1)**  
  Authors: Abdelaziz Bouzidi, Hamid Laga, Hazem Wannous  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06762v1.pdf)  
  Keywords: fast, acceleration, 3d reconstruction, compact, efficient, gaussian splatting, geometry, lightweight, ar  
- **[REArtGS: Reconstructing and Generating Articulated Objects via 3D Gaussian Splatting with Geometric and Motion Constraints](https://arxiv.org/abs/2503.06677v1)**  
  Authors: Di Wu, Liu Liu, Zhou Linli, Anran Huang, Liangtu Song, Qiaojun Yu, Qi Wu, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06677v1.pdf)  
  Keywords: motion, 3d gaussian, high-fidelity, dynamic, gaussian splatting, geometry, human, face, ar  
- **[Introducing Unbiased Depth into 2D Gaussian Splatting for High-accuracy Surface Reconstruction](https://arxiv.org/abs/2503.06587v1)**  
  Authors: Xiaoming Peng, Yixin Yang, Yang Zhou, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06587v1.pdf)  
  Keywords: gaussian splatting, geometry, face, ar, reflection  
- **[StructGS: Adaptive Spherical Harmonics and Rendering Enhancements for Superior 3D Gaussian Splatting](https://arxiv.org/abs/2503.06462v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06462v1.pdf)  
  Keywords: 3d reconstruction, head, 3d gaussian, dynamic, gaussian splatting, neural rendering, ar  
- **[Bayesian Fields: Task-driven Open-Set Semantic Gaussian Splatting](https://arxiv.org/abs/2503.05949v1)**  
  Authors: Dominic Maggio, Luca Carlone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05949v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MIT-SPARK/Bayesian-Fields?style=social)](https://github.com/MIT-SPARK/Bayesian-Fields)  
  Keywords: 3d reconstruction, 3d gaussian, semantic, high-fidelity, gaussian splatting, mapping, ar  
- **[LiDAR-enhanced 3D Gaussian Splatting Mapping](https://arxiv.org/abs/2503.05425v1)**  
  Authors: Jian Shen, Huai Yu, Ji Wu, Wen Yang, Gui-Song Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05425v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, geometry, tracking, mapping, ar  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: compact, dynamic, efficient, semantic, human, geometry, tracking, ar  

### Large Scene

*Showing the latest 50 out of 75 papers*

- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: semantic, gaussian splatting, ar, outdoor  
- **[OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation](https://arxiv.org/abs/2502.18041v4)**  
  Authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.18041v4.pdf)  
  Keywords: 3d gaussian, semantic, gaussian splatting, outdoor, segmentation, ar  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, geometry, outdoor, tracking, mapping, slam, ar  
- **[RadSplatter: Extending 3D Gaussian Splatting to Radio Frequencies for Wireless Radiomap Extrapolation](https://arxiv.org/abs/2502.12686v1)**  
  Authors: Yiheng Wang, Ye Xue, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.12686v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, outdoor, ar, autonomous driving  
- **[GS-GVINS: A Tightly-integrated GNSS-Visual-Inertial Navigation System Augmented by 3D Gaussian Splatting](https://arxiv.org/abs/2502.10975v1)**  
  Authors: Zelin Zhou, Saurav Uprety, Shichuang Nie, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10975v1.pdf)  
  Keywords: motion, 3d gaussian, dynamic, gaussian splatting, outdoor, tracking, slam, ar  
- **[PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression](https://arxiv.org/abs/2502.04843v2)**  
  Authors: Feifei Li, Qi Song, Chi Zhang, Hui Shuai, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04843v2.pdf)  
  Keywords: nerf, gaussian splatting, ar, outdoor  
- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, outdoor, ar  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: ar, localization, dynamic, gaussian splatting, geometry, outdoor, mapping, nerf, slam, large scene  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: motion, real-time rendering, 3d gaussian, dynamic, outdoor, understanding, ar  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: mapping, 3d gaussian, efficient, gaussian splatting, outdoor, neural rendering, nerf, slam, ar  

### Model Compression

*Showing the latest 50 out of 538 papers*

- **[EigenGS Representation: From Eigenspace to Gaussian Image Space](https://arxiv.org/abs/2503.07446v1)**  
  Authors: Lo-Wei Tai, Ching-En Li, Cheng-Lin Chen, Chih-Jung Tsai, Hwann-Tzong Chen, Tyng-Luh Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07446v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, ar  
- **[Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields](https://arxiv.org/abs/2503.06762v1)**  
  Authors: Abdelaziz Bouzidi, Hamid Laga, Hazem Wannous  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06762v1.pdf)  
  Keywords: fast, acceleration, 3d reconstruction, compact, efficient, gaussian splatting, geometry, lightweight, ar  
- **[ForestSplats: Deformable transient field for Gaussian Splatting in the Wild](https://arxiv.org/abs/2503.06179v1)**  
  Authors: Wongi Park, Myeongseok Nam, Siwon Kim, Sangwoo Jo, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06179v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, efficient, semantic, gaussian splatting, lighting, ar  
- **[Feature-EndoGaussian: Feature Distilled Gaussian Splatting in Surgical Deformable Scene Reconstruction](https://arxiv.org/abs/2503.06161v1)**  
  Authors: Kai Li, Junhao Wang, William Han, Ding Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06161v1.pdf)  
  Keywords: 3d gaussian, dynamic, efficient, gaussian splatting, semantic, segmentation, understanding, deformation, nerf, ar  
- **[SecureGS: Boosting the Security and Fidelity of 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2503.06118v1)**  
  Authors: Xuanyu Zhang, Jiarui Meng, Zhipei Xu, Shuzhou Yang, Yanmin Wu, Ronggang Wang, Jian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06118v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, efficient, gaussian splatting, nerf, ar  
- **[D2GV: Deformable 2D Gaussian Splatting for Video Representation in 400FPS](https://arxiv.org/abs/2503.05600v1)**  
  Authors: Mufan Liu, Qi Yang, Miaoran Zhao, He Huang, Le Yang, Zhu Li, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05600v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Evan-sudo/D2GV?style=social)](https://github.com/Evan-sudo/D2GV)  
  Keywords: fast, compact, efficient, gaussian splatting, compression, ar  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v1)**  
  Authors: Jiahui Fan, Fujun Luan, Miloš Hašan, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, human, lightweight, relighting, lighting, high quality, ar, relightable  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: compact, dynamic, efficient, semantic, human, geometry, tracking, ar  
- **[EvolvingGS: High-Fidelity Streamable Volumetric Video via Evolving 3D Gaussian Representation](https://arxiv.org/abs/2503.05162v1)**  
  Authors: Chao Zhang, Yifeng Zhou, Shuheng Wang, Wenfa Li, Degang Wang, Yi Xu, Shaohui Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05162v1.pdf)  
  Keywords: fast, motion, 3d gaussian, high-fidelity, dynamic, gaussian splatting, efficient, human, compression, high quality, ar  
- **[GaussianVideo: Efficient Video Representation and Compression by Gaussian Splatting](https://arxiv.org/abs/2503.04333v1)**  
  Authors: Inseo Lee, Youngyoon Choi, Joonseok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04333v1.pdf)  
  Keywords: fast, dynamic, efficient, gaussian splatting, lightweight, compression, ar  

### Quality Enhancement

*Showing the latest 50 out of 232 papers*

- **[All That Glitters Is Not Gold: Key-Secured 3D Secrets within 3D Gaussian Splatting](https://arxiv.org/abs/2503.07191v1)**  
  Authors: Yan Ren, Shilin Lu, Adams Wai-Kin Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07191v1.pdf) | [![GitHub](https://img.shields.io/github/stars/RY-Paper/KeySS?style=social)](https://github.com/RY-Paper/KeySS)  
  Keywords: 3d gaussian, gaussian splatting, ar, high-fidelity  
- **[REArtGS: Reconstructing and Generating Articulated Objects via 3D Gaussian Splatting with Geometric and Motion Constraints](https://arxiv.org/abs/2503.06677v1)**  
  Authors: Di Wu, Liu Liu, Zhou Linli, Anran Huang, Liangtu Song, Qiaojun Yu, Qi Wu, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06677v1.pdf)  
  Keywords: motion, 3d gaussian, high-fidelity, dynamic, gaussian splatting, geometry, human, face, ar  
- **[Bayesian Fields: Task-driven Open-Set Semantic Gaussian Splatting](https://arxiv.org/abs/2503.05949v1)**  
  Authors: Dominic Maggio, Luca Carlone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05949v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MIT-SPARK/Bayesian-Fields?style=social)](https://github.com/MIT-SPARK/Bayesian-Fields)  
  Keywords: 3d reconstruction, 3d gaussian, semantic, high-fidelity, gaussian splatting, mapping, ar  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v1)**  
  Authors: Jiahui Fan, Fujun Luan, Miloš Hašan, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, human, lightweight, relighting, lighting, high quality, ar, relightable  
- **[MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions](https://arxiv.org/abs/2503.05182v1)**  
  Authors: Qingyuan Zhou, Yuehu Gong, Weidong Yang, Jiaze Li, Yeqi Luo, Baixin Xu, Shuhao Li, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05182v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, high-fidelity, gaussian splatting, geometry, face, illumination, ar  
- **[EvolvingGS: High-Fidelity Streamable Volumetric Video via Evolving 3D Gaussian Representation](https://arxiv.org/abs/2503.05162v1)**  
  Authors: Chao Zhang, Yifeng Zhou, Shuheng Wang, Wenfa Li, Degang Wang, Yi Xu, Shaohui Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05162v1.pdf)  
  Keywords: fast, motion, 3d gaussian, high-fidelity, dynamic, gaussian splatting, efficient, human, compression, high quality, ar  
- **[GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2503.03984v1)**  
  Authors: Qianzhong Chen, Jiankai Sun, Naixiang Gao, JunEn Low, Timothy Chen, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03984v1.pdf)  
  Keywords: 3d gaussian, efficient, high-fidelity, gaussian splatting, dynamic, ar  
- **[2DGS-Avatar: Animatable High-fidelity Clothed Avatar via 2D Gaussian Splatting](https://arxiv.org/abs/2503.02452v1)**  
  Authors: Qipeng Yan, Mingyang Sun, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02452v1.pdf)  
  Keywords: fast, real-time rendering, 3d gaussian, high-fidelity, dynamic, gaussian splatting, geometry, human, avatar, nerf, ar  
- **[DQO-MAP: Dual Quadrics Multi-Object mapping with Gaussian Splatting](https://arxiv.org/abs/2503.02223v1)**  
  Authors: Haoyuan Li, Ziqin Ye, Yue Hao, Weiyang Lin, Chao Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LiHaoy-ux/DQO-MAP?style=social)](https://github.com/LiHaoy-ux/DQO-MAP)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, mapping, slam, ar  
- **[FGS-SLAM: Fourier-based Gaussian Splatting for Real-time SLAM with Sparse and Dense Map Fusion](https://arxiv.org/abs/2503.01109v1)**  
  Authors: Yansong Xu, Junlin Li, Wei Zhang, Siyu Chen, Shengyong Zhang, Yuquan Leng, Weijia Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01109v1.pdf)  
  Keywords: localization, 3d gaussian, efficient, high-fidelity, gaussian splatting, tracking, mapping, slam, ar  

### Ray Tracing

- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: ray tracing, real-time rendering, dynamic, efficient, geometry, face, 4d, lighting, tracking, ar, relightable  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: ray tracing, gaussian splatting, face, shadow, lighting, reflection  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, 3d gaussian, survey, gaussian splatting, ar  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: ray tracing, acceleration, efficient, gaussian splatting, light transport, ar, reflection  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: ray tracing, 3d gaussian, gaussian splatting, shadow, ar, reflection  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: ray tracing, efficient, gaussian splatting, relighting, lighting, ar, reflection  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: ray tracing, real-time rendering, 3d gaussian, high-fidelity, efficient, gaussian splatting, lighting, ar, reflection  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: fast, efficient, global illumination, gaussian splatting, geometry, face, illumination, mapping, nerf, ar  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v2)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v2.pdf)  
  Keywords: ray tracing, 3d gaussian, efficient, gaussian splatting, ar  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: 3d gaussian, ray tracing, gaussian splatting, ar  

### Relighting

*Showing the latest 50 out of 159 papers*

- **[D3DR: Lighting-Aware Object Insertion in Gaussian Splatting](https://arxiv.org/abs/2503.06740v1)**  
  Authors: Vsevolod Skorokhodov, Nikita Durasov, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06740v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, relighting, shadow, lighting, ar  
- **[Introducing Unbiased Depth into 2D Gaussian Splatting for High-accuracy Surface Reconstruction](https://arxiv.org/abs/2503.06587v1)**  
  Authors: Xiaoming Peng, Yixin Yang, Yang Zhou, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06587v1.pdf)  
  Keywords: gaussian splatting, geometry, face, ar, reflection  
- **[ForestSplats: Deformable transient field for Gaussian Splatting in the Wild](https://arxiv.org/abs/2503.06179v1)**  
  Authors: Wongi Park, Myeongseok Nam, Siwon Kim, Sangwoo Jo, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06179v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, efficient, semantic, gaussian splatting, lighting, ar  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v1)**  
  Authors: Jiahui Fan, Fujun Luan, Miloš Hašan, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v1.pdf)  
  Keywords: motion, 3d gaussian, gaussian splatting, human, lightweight, relighting, lighting, high quality, ar, relightable  
- **[MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions](https://arxiv.org/abs/2503.05182v1)**  
  Authors: Qingyuan Zhou, Yuehu Gong, Weidong Yang, Jiaze Li, Yeqi Luo, Baixin Xu, Shuhao Li, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05182v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, high-fidelity, gaussian splatting, geometry, face, illumination, ar  
- **[EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering](https://arxiv.org/abs/2502.20669v1)**  
  Authors: John J. Han, Jie Ying Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20669v1.pdf)  
  Keywords: medical, 3d reconstruction, 3d gaussian, gaussian splatting, geometry, face, lighting, ar  
- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941v1)**  
  Authors: Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16941v1.pdf)  
  Keywords: efficient, 4d, lighting, nerf, ar  
- **[RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection](https://arxiv.org/abs/2502.13071v1)**  
  Authors: Jingtong Yue, Zhiwei Lin, Xin Lin, Xiaoyu Zhou, Xiangtai Li, Lu Qi, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13071v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, face  
- **[OMG: Opacity Matters in Material Modeling with Gaussian Splatting](https://arxiv.org/abs/2502.10988v2)**  
  Authors: Silong Yong, Venkata Nagarjun Pudureddiyur Manivannan, Bernhard Kerbl, Zifu Wan, Simon Stepputtis, Katia Sycara, Yaqi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10988v2.pdf)  
  Keywords: real-time rendering, 3d gaussian, gaussian splatting, geometry, lighting, neural rendering, ar  
- **[E-3DGS: Event-Based Novel View Rendering of Large-Scale Scenes Using 3D Gaussian Splatting](https://arxiv.org/abs/2502.10827v1)**  
  Authors: Sohaib Zahid, Viktor Rudnev, Eddy Ilg, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10827v1.pdf)  
  Keywords: fast, motion, 3d gaussian, dynamic, gaussian splatting, lighting, nerf, ar  

### SLAM

*Showing the latest 50 out of 214 papers*

- **[Pixel to Gaussian: Ultra-Fast Continuous Super-Resolution with 2D Gaussian Modeling](https://arxiv.org/abs/2503.06617v1)**  
  Authors: Long Peng, Anran Wu, Wenbo Li, Peizhe Xia, Xueyuan Dai, Xinjie Zhang, Xin Di, Haoze Sun, Renjing Pei, Yang Wang, Yang Cao, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06617v1.pdf)  
  Keywords: fast, gaussian splatting, ar, mapping  
- **[Bayesian Fields: Task-driven Open-Set Semantic Gaussian Splatting](https://arxiv.org/abs/2503.05949v1)**  
  Authors: Dominic Maggio, Luca Carlone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05949v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MIT-SPARK/Bayesian-Fields?style=social)](https://github.com/MIT-SPARK/Bayesian-Fields)  
  Keywords: 3d reconstruction, 3d gaussian, semantic, high-fidelity, gaussian splatting, mapping, ar  
- **[LiDAR-enhanced 3D Gaussian Splatting Mapping](https://arxiv.org/abs/2503.05425v1)**  
  Authors: Jian Shen, Huai Yu, Ji Wu, Wen Yang, Gui-Song Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05425v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, geometry, tracking, mapping, ar  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: compact, dynamic, efficient, semantic, human, geometry, tracking, ar  
- **[GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting](https://arxiv.org/abs/2503.05152v2)**  
  Authors: Kohei Honda, Takeshi Ishita, Yasuhiro Yoshimura, Ryo Yonetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05152v2.pdf)  
  Keywords: localization, head, 3d gaussian, gaussian splatting, ar  
- **[Instrument-Splatting: Controllable Photorealistic Reconstruction of Surgical Instruments Using Gaussian Splatting](https://arxiv.org/abs/2503.04082v1)**  
  Authors: Shuojue Yang, Zijian Wu, Mingxuan Hong, Qian Li, Daiyun Shen, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04082v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, semantic, gaussian splatting, geometry, tracking, ar  
- **[Direct Sparse Odometry with Continuous 3D Gaussian Maps for Indoor Environments](https://arxiv.org/abs/2503.03373v1)**  
  Authors: Jie Deng, Fengtian Lang, Zikang Yuan, Xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03373v1.pdf)  
  Keywords: localization, 3d gaussian, robotics, tracking, ar  
- **[DQO-MAP: Dual Quadrics Multi-Object mapping with Gaussian Splatting](https://arxiv.org/abs/2503.02223v1)**  
  Authors: Haoyuan Li, Ziqin Ye, Yue Hao, Weiyang Lin, Chao Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.02223v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LiHaoy-ux/DQO-MAP?style=social)](https://github.com/LiHaoy-ux/DQO-MAP)  
  Keywords: 3d gaussian, high-fidelity, gaussian splatting, mapping, slam, ar  
- **[OpenGS-SLAM: Open-Set Dense Semantic SLAM with 3D Gaussian Splatting for Object-Level Scene Understanding](https://arxiv.org/abs/2503.01646v1)**  
  Authors: Dianyi Yang, Yu Gao, Xihan Wang, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01646v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://young-bit.github.io/opengs-github.github.io/.)  
  Keywords: fast, mapping, 3d gaussian, semantic, gaussian splatting, segmentation, tracking, understanding, slam, ar  
- **[FGS-SLAM: Fourier-based Gaussian Splatting for Real-time SLAM with Sparse and Dense Map Fusion](https://arxiv.org/abs/2503.01109v1)**  
  Authors: Yansong Xu, Junlin Li, Wei Zhang, Siyu Chen, Shengyong Zhang, Yuquan Leng, Weijia Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.01109v1.pdf)  
  Keywords: localization, 3d gaussian, efficient, high-fidelity, gaussian splatting, tracking, mapping, slam, ar  

### Scene Understanding

*Showing the latest 50 out of 251 papers*

- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: survey, ar, geometry, semantic  
- **[CoDa-4DGS: Dynamic Gaussian Splatting with Context and Deformation Awareness for Autonomous Driving](https://arxiv.org/abs/2503.06744v1)**  
  Authors: Rui Song, Chenwei Liang, Yan Xia, Walter Zimmer, Hu Cao, Holger Caesar, Andreas Festag, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06744v1.pdf)  
  Keywords: dynamic, semantic, gaussian splatting, 4d, segmentation, deformation, ar, autonomous driving  
- **[SplatTalk: 3D VQA with Gaussian Splatting](https://arxiv.org/abs/2503.06271v1)**  
  Authors: Anh Thai, Songyou Peng, Kyle Genova, Leonidas Guibas, Thomas Funkhouser  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06271v1.pdf)  
  Keywords: vr, 3d gaussian, human, gaussian splatting, robotics, understanding, ar  
- **[ForestSplats: Deformable transient field for Gaussian Splatting in the Wild](https://arxiv.org/abs/2503.06179v1)**  
  Authors: Wongi Park, Myeongseok Nam, Siwon Kim, Sangwoo Jo, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06179v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, efficient, semantic, gaussian splatting, lighting, ar  
- **[Feature-EndoGaussian: Feature Distilled Gaussian Splatting in Surgical Deformable Scene Reconstruction](https://arxiv.org/abs/2503.06161v1)**  
  Authors: Kai Li, Junhao Wang, William Han, Ding Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06161v1.pdf)  
  Keywords: 3d gaussian, dynamic, efficient, gaussian splatting, semantic, segmentation, understanding, deformation, nerf, ar  
- **[Bayesian Fields: Task-driven Open-Set Semantic Gaussian Splatting](https://arxiv.org/abs/2503.05949v1)**  
  Authors: Dominic Maggio, Luca Carlone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05949v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MIT-SPARK/Bayesian-Fields?style=social)](https://github.com/MIT-SPARK/Bayesian-Fields)  
  Keywords: 3d reconstruction, 3d gaussian, semantic, high-fidelity, gaussian splatting, mapping, ar  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: compact, dynamic, efficient, semantic, human, geometry, tracking, ar  
- **[Manboformer: Learning Gaussian Representations via Spatial-temporal Attention Mechanism](https://arxiv.org/abs/2503.04863v1)**  
  Authors: Ziyue Zhao, Qining Qi, Jianfa Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04863v1.pdf)  
  Keywords: 3d gaussian, ar, semantic, autonomous driving  
- **[Instrument-Splatting: Controllable Photorealistic Reconstruction of Surgical Instruments Using Gaussian Splatting](https://arxiv.org/abs/2503.04082v1)**  
  Authors: Shuojue Yang, Zijian Wu, Mingxuan Hong, Qian Li, Daiyun Shen, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04082v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, semantic, gaussian splatting, geometry, tracking, ar  
- **[GaussianGraph: 3D Gaussian-based Scene Graph Generation for Open-world Scene Understanding](https://arxiv.org/abs/2503.04034v1)**  
  Authors: Xihan Wang, Dianyi Yang, Yu Gao, Yufeng Yue, Yi Yang, Mengyin Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04034v1.pdf)  
  Keywords: 3d gaussian, semantic, dynamic, gaussian splatting, compression, segmentation, understanding, ar  



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