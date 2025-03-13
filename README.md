# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-03-13 00:49:43

## Categories

- [3DGS Surveys](#3dgs-surveys) (25 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (411 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1442 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (485 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (536 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (99 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (479 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (76 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (547 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (236 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (33 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (160 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (217 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (255 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, survey, dynamic, ar, real-time rendering  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: survey, semantic, geometry, ar  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: compression, ar, 3d reconstruction, gaussian splatting, 3d gaussian, survey, nerf, efficient, real-time rendering  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: lighting, gaussian splatting, deformation, survey, dynamic, 4d, nerf, ar, motion  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, gaussian splatting, 3d gaussian, survey, ar  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: face, mapping, reflection, localization, lighting, 3d gaussian, survey, geometry, outdoor, dynamic, slam, tracking, ar  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: illumination, gaussian splatting, 3d gaussian, survey, recognition, ar  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: high-fidelity, ar, 3d reconstruction, lighting, autonomous driving, gaussian splatting, survey, compact, geometry, dynamic, nerf, semantic, robotics  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: robotics, understanding, gaussian splatting, 3d gaussian, survey, nerf, ar, real-time rendering  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: high-fidelity, lighting, gaussian splatting, 3d gaussian, survey, nerf, ar  

### Acceleration

*Showing the latest 50 out of 411 papers*

- **[TT-GaussOcc: Test-Time Compute for Self-Supervised Occupancy Prediction via Spatio-Temporal Gaussian Splatting](https://arxiv.org/abs/2503.08485v1)**  
  Authors: Fengyi Zhang, Huitong Yang, Zheng Zhang, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08485v1.pdf)  
  Keywords: ar, understanding, gaussian splatting, 3d gaussian, geometry, dynamic, semantic, fast  
- **[S3R-GS: Streamlining the Pipeline for Large-Scale Street Scene Reconstruction](https://arxiv.org/abs/2503.08217v1)**  
  Authors: Guangting Zheng, Jiajun Deng, Xiaomeng Chu, Yu Yuan, Houqiang Li, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08217v1.pdf)  
  Keywords: efficient rendering, ar, 3d reconstruction, gaussian splatting, 3d gaussian, dynamic, head, efficient  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, survey, dynamic, ar, real-time rendering  
- **[MVGSR: Multi-View Consistency Gaussian Splatting for Robust Surface Reconstruction](https://arxiv.org/abs/2503.08093v1)**  
  Authors: Chenfeng Hou, Qi Xun Yeo, Mengqi Guo, Yongxin Su, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08093v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mvgsr.github.io}{this)  
  Keywords: dynamic, face, gaussian splatting, 3d gaussian, lightweight, segmentation, ar, fast  
- **[7DGS: Unified Spatial-Temporal-Angular Gaussian Splatting](https://arxiv.org/abs/2503.07946v1)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07946v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/7dgs/.)  
  Keywords: ar, gaussian splatting, 3d gaussian, dynamic, 4d, efficient, real-time rendering  
- **[Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields](https://arxiv.org/abs/2503.06762v1)**  
  Authors: Abdelaziz Bouzidi, Hamid Laga, Hazem Wannous  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06762v1.pdf)  
  Keywords: ar, 3d reconstruction, acceleration, gaussian splatting, compact, geometry, lightweight, efficient, fast  
- **[Pixel to Gaussian: Ultra-Fast Continuous Super-Resolution with 2D Gaussian Modeling](https://arxiv.org/abs/2503.06617v1)**  
  Authors: Long Peng, Anran Wu, Wenbo Li, Peizhe Xia, Xueyuan Dai, Xinjie Zhang, Xin Di, Haoze Sun, Renjing Pei, Yang Wang, Yang Cao, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06617v1.pdf)  
  Keywords: gaussian splatting, mapping, ar, fast  
- **[StreamGS: Online Generalizable Gaussian Splatting Reconstruction for Unposed Image Streams](https://arxiv.org/abs/2503.06235v1)**  
  Authors: Yang LI, Jinglu Wang, Lei Chu, Xiao Li, Shiu-hong Kao, Ying-Cong Chen, Yan Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06235v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, fast  
- **[ForestSplats: Deformable transient field for Gaussian Splatting in the Wild](https://arxiv.org/abs/2503.06179v1)**  
  Authors: Wongi Park, Myeongseok Nam, Siwon Kim, Sangwoo Jo, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06179v1.pdf)  
  Keywords: ar, semantic, lighting, gaussian splatting, 3d gaussian, efficient, real-time rendering  
- **[SecureGS: Boosting the Security and Fidelity of 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2503.06118v1)**  
  Authors: Xuanyu Zhang, Jiarui Meng, Zhipei Xu, Shuzhou Yang, Yanmin Wu, Ronggang Wang, Jian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06118v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, nerf, efficient, real-time rendering  

### Applications

*Showing the latest 50 out of 1442 papers*

- **[PCGS: Progressive Compression of 3D Gaussian Splatting](https://arxiv.org/abs/2503.08511v1)**  
  Authors: Yihang Chen, Mengyao Li, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08511v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YihangChen-ee/PCGS?style=social)](https://github.com/YihangChen-ee/PCGS)  
  Keywords: compression, ar, gaussian splatting, 3d gaussian, compact, efficient  
- **[TT-GaussOcc: Test-Time Compute for Self-Supervised Occupancy Prediction via Spatio-Temporal Gaussian Splatting](https://arxiv.org/abs/2503.08485v1)**  
  Authors: Fengyi Zhang, Huitong Yang, Zheng Zhang, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08485v1.pdf)  
  Keywords: ar, understanding, gaussian splatting, 3d gaussian, geometry, dynamic, semantic, fast  
- **[Mitigating Ambiguities in 3D Classification with Gaussian Splatting](https://arxiv.org/abs/2503.08352v1)**  
  Authors: Ruiqi Zhang, Hao Zhu, Jingyi Zhao, Qi Zhang, Xun Cao, Zhan Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08352v1.pdf)  
  Keywords: gaussian splatting, face, efficient, ar  
- **[Uni-Gaussians: Unifying Camera and Lidar Simulation with Gaussians for Dynamic Driving Scenarios](https://arxiv.org/abs/2503.08317v1)**  
  Authors: Zikang Yuan, Yuechuan Pu, Hongcheng Luo, Fengtian Lang, Cheng Chi, Teng Li, Yingying Shen, Haiyang Sun, Bing Wang, Xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08317v1.pdf)  
  Keywords: ar, autonomous driving, gaussian splatting, neural rendering, dynamic, nerf, efficient  
- **[ELECTRA: A Symmetry-breaking Cartesian Network for Charge Density Prediction with Floating Orbitals](https://arxiv.org/abs/2503.08305v1)**  
  Authors: Jonas Elsborg, Luca Thiede, Alán Aspuru-Guzik, Tejs Vegge, Arghya Bhowmik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08305v1.pdf)  
  Keywords: gaussian splatting, efficient, compact, ar  
- **[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://arxiv.org/abs/2503.08224v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08224v1.pdf)  
  Keywords: face, high-fidelity, lighting, gaussian splatting, deformation, 3d gaussian, relighting, relightable, head, tracking, avatar, ar  
- **[MVD-HuGaS: Human Gaussians from a Single Image via 3D Human Multi-view Diffusion Prior](https://arxiv.org/abs/2503.08218v1)**  
  Authors: Kaiqiang Xiong, Ying Feng, Qi Zhang, Jianbo Jiao, Yang Zhao, Zhihao Liang, Huachen Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08218v1.pdf)  
  Keywords: high-fidelity, human, 3d gaussian, geometry, ar  
- **[S3R-GS: Streamlining the Pipeline for Large-Scale Street Scene Reconstruction](https://arxiv.org/abs/2503.08217v1)**  
  Authors: Guangting Zheng, Jiajun Deng, Xiaomeng Chu, Yu Yuan, Houqiang Li, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08217v1.pdf)  
  Keywords: efficient rendering, ar, 3d reconstruction, gaussian splatting, 3d gaussian, dynamic, head, efficient  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, survey, dynamic, ar, real-time rendering  
- **[ArticulatedGS: Self-supervised Digital Twin Modeling of Articulated Objects using 3D Gaussian Splatting](https://arxiv.org/abs/2503.08135v1)**  
  Authors: Junfu Guo, Yu Xin, Gaoyi Liu, Kai Xu, Ligang Liu, Ruizhen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08135v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry, segmentation, semantic, motion  

### Avatar Generation

*Showing the latest 50 out of 485 papers*

- **[Mitigating Ambiguities in 3D Classification with Gaussian Splatting](https://arxiv.org/abs/2503.08352v1)**  
  Authors: Ruiqi Zhang, Hao Zhu, Jingyi Zhao, Qi Zhang, Xun Cao, Zhan Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08352v1.pdf)  
  Keywords: gaussian splatting, face, efficient, ar  
- **[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://arxiv.org/abs/2503.08224v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08224v1.pdf)  
  Keywords: face, high-fidelity, lighting, gaussian splatting, deformation, 3d gaussian, relighting, relightable, head, tracking, avatar, ar  
- **[MVD-HuGaS: Human Gaussians from a Single Image via 3D Human Multi-view Diffusion Prior](https://arxiv.org/abs/2503.08218v1)**  
  Authors: Kaiqiang Xiong, Ying Feng, Qi Zhang, Jianbo Jiao, Yang Zhao, Zhihao Liang, Huachen Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08218v1.pdf)  
  Keywords: high-fidelity, human, 3d gaussian, geometry, ar  
- **[S3R-GS: Streamlining the Pipeline for Large-Scale Street Scene Reconstruction](https://arxiv.org/abs/2503.08217v1)**  
  Authors: Guangting Zheng, Jiajun Deng, Xiaomeng Chu, Yu Yuan, Houqiang Li, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08217v1.pdf)  
  Keywords: efficient rendering, ar, 3d reconstruction, gaussian splatting, 3d gaussian, dynamic, head, efficient  
- **[MVGSR: Multi-View Consistency Gaussian Splatting for Robust Surface Reconstruction](https://arxiv.org/abs/2503.08093v1)**  
  Authors: Chenfeng Hou, Qi Xun Yeo, Mengqi Guo, Yongxin Su, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08093v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mvgsr.github.io}{this)  
  Keywords: dynamic, face, gaussian splatting, 3d gaussian, lightweight, segmentation, ar, fast  
- **[REArtGS: Reconstructing and Generating Articulated Objects via 3D Gaussian Splatting with Geometric and Motion Constraints](https://arxiv.org/abs/2503.06677v2)**  
  Authors: Di Wu, Liu Liu, Zhou Linli, Anran Huang, Liangtu Song, Qiaojun Yu, Qi Wu, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06677v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sites.google.com/view/reartgs/home.)  
  Keywords: face, high-fidelity, human, gaussian splatting, 3d gaussian, geometry, dynamic, ar, motion  
- **[Introducing Unbiased Depth into 2D Gaussian Splatting for High-accuracy Surface Reconstruction](https://arxiv.org/abs/2503.06587v1)**  
  Authors: Xiaoming Peng, Yixin Yang, Yang Zhou, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06587v1.pdf)  
  Keywords: face, reflection, gaussian splatting, geometry, ar  
- **[StructGS: Adaptive Spherical Harmonics and Rendering Enhancements for Superior 3D Gaussian Splatting](https://arxiv.org/abs/2503.06462v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06462v1.pdf)  
  Keywords: ar, 3d reconstruction, gaussian splatting, 3d gaussian, dynamic, head, neural rendering  
- **[SplatTalk: 3D VQA with Gaussian Splatting](https://arxiv.org/abs/2503.06271v1)**  
  Authors: Anh Thai, Songyou Peng, Kyle Genova, Leonidas Guibas, Thomas Funkhouser  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06271v1.pdf)  
  Keywords: vr, human, understanding, gaussian splatting, 3d gaussian, ar, robotics  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v2)**  
  Authors: Jiahui Fan, Fujun Luan, Jian Yang, Miloš Hašan, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v2.pdf)  
  Keywords: human, lighting, gaussian splatting, lightweight, 3d gaussian, relighting, relightable, high quality, ar, motion  

### Dynamic Scene

*Showing the latest 50 out of 536 papers*

- **[TT-GaussOcc: Test-Time Compute for Self-Supervised Occupancy Prediction via Spatio-Temporal Gaussian Splatting](https://arxiv.org/abs/2503.08485v1)**  
  Authors: Fengyi Zhang, Huitong Yang, Zheng Zhang, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08485v1.pdf)  
  Keywords: ar, understanding, gaussian splatting, 3d gaussian, geometry, dynamic, semantic, fast  
- **[Uni-Gaussians: Unifying Camera and Lidar Simulation with Gaussians for Dynamic Driving Scenarios](https://arxiv.org/abs/2503.08317v1)**  
  Authors: Zikang Yuan, Yuechuan Pu, Hongcheng Luo, Fengtian Lang, Cheng Chi, Teng Li, Yingying Shen, Haiyang Sun, Bing Wang, Xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08317v1.pdf)  
  Keywords: ar, autonomous driving, gaussian splatting, neural rendering, dynamic, nerf, efficient  
- **[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://arxiv.org/abs/2503.08224v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08224v1.pdf)  
  Keywords: face, high-fidelity, lighting, gaussian splatting, deformation, 3d gaussian, relighting, relightable, head, tracking, avatar, ar  
- **[S3R-GS: Streamlining the Pipeline for Large-Scale Street Scene Reconstruction](https://arxiv.org/abs/2503.08217v1)**  
  Authors: Guangting Zheng, Jiajun Deng, Xiaomeng Chu, Yu Yuan, Houqiang Li, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08217v1.pdf)  
  Keywords: efficient rendering, ar, 3d reconstruction, gaussian splatting, 3d gaussian, dynamic, head, efficient  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, survey, dynamic, ar, real-time rendering  
- **[ArticulatedGS: Self-supervised Digital Twin Modeling of Articulated Objects using 3D Gaussian Splatting](https://arxiv.org/abs/2503.08135v1)**  
  Authors: Junfu Guo, Yu Xin, Gaoyi Liu, Kai Xu, Ligang Liu, Ruizhen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08135v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry, segmentation, semantic, motion  
- **[MVGSR: Multi-View Consistency Gaussian Splatting for Robust Surface Reconstruction](https://arxiv.org/abs/2503.08093v1)**  
  Authors: Chenfeng Hou, Qi Xun Yeo, Mengqi Guo, Yongxin Su, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08093v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mvgsr.github.io}{this)  
  Keywords: dynamic, face, gaussian splatting, 3d gaussian, lightweight, segmentation, ar, fast  
- **[7DGS: Unified Spatial-Temporal-Angular Gaussian Splatting](https://arxiv.org/abs/2503.07946v1)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07946v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/7dgs/.)  
  Keywords: ar, gaussian splatting, 3d gaussian, dynamic, 4d, efficient, real-time rendering  
- **[Frequency-Aware Density Control via Reparameterization for High-Quality Rendering of 3D Gaussian Splatting](https://arxiv.org/abs/2503.07000v1)**  
  Authors: Zhaojie Zeng, Yuesong Wang, Lili Ju, Tao Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07000v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, dynamic  
- **[CoDa-4DGS: Dynamic Gaussian Splatting with Context and Deformation Awareness for Autonomous Driving](https://arxiv.org/abs/2503.06744v1)**  
  Authors: Rui Song, Chenwei Liang, Yan Xia, Walter Zimmer, Hu Cao, Holger Caesar, Andreas Festag, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06744v1.pdf)  
  Keywords: ar, autonomous driving, gaussian splatting, deformation, dynamic, 4d, segmentation, semantic  

### Few-shot

*Showing the latest 50 out of 99 papers*

- **[Multi-Modal 3D Mesh Reconstruction from Images and Text](https://arxiv.org/abs/2503.07190v1)**  
  Authors: Melvin Reka, Tessa Pulli, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07190v1.pdf)  
  Keywords: few-shot, 3d reconstruction, gaussian splatting, geometry, ar, robotics  
- **[GaussianCAD: Robust Self-Supervised CAD Reconstruction from Three Orthographic Views Using 3D Gaussian Splatting](https://arxiv.org/abs/2503.05161v1)**  
  Authors: Zheng Zhou, Zhe Li, Bo Yu, Lina Hu, Liang Dong, Zijian Yang, Xiaoli Liu, Ning Xu, Ziwei Wang, Yonghao Dang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05161v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, 3d gaussian, sparse-view, ar  
- **[S2Gaussian: Sparse-View Super-Resolution 3D Gaussian Splatting](https://arxiv.org/abs/2503.04314v1)**  
  Authors: Yecong Wan, Mingwen Shao, Yuanshuo Cheng, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04314v1.pdf)  
  Keywords: sparse view, gaussian splatting, 3d gaussian, geometry, sparse-view, ar  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: few-shot, ar, human, semantic, gaussian splatting, neural rendering, nerf, efficient  
- **[Seeing A 3D World in A Grain of Sand](https://arxiv.org/abs/2503.00260v1)**  
  Authors: Yufan Zhang, Yu Ji, Yu Guo, Jinwei Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00260v1.pdf)  
  Keywords: sparse view, face, 3d reconstruction, gaussian splatting, 3d gaussian, ar  
- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: sparse view, high-fidelity, ar, 3d reconstruction, gaussian splatting, 3d gaussian, efficient  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: mapping, gaussian splatting, geometry, sparse-view, slam, tracking, nerf, ar, real-time rendering  
- **[DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform](https://arxiv.org/abs/2501.12637v2)**  
  Authors: Hung Nguyen, Blark Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12637v2.pdf)  
  Keywords: few-shot, head, nerf, ar, fast  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, sparse-view, 4d, semantic  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: ar, 3d reconstruction, gaussian splatting, 3d gaussian, sparse-view, nerf, efficient  

### Geometry Reconstruction

*Showing the latest 50 out of 479 papers*

- **[TT-GaussOcc: Test-Time Compute for Self-Supervised Occupancy Prediction via Spatio-Temporal Gaussian Splatting](https://arxiv.org/abs/2503.08485v1)**  
  Authors: Fengyi Zhang, Huitong Yang, Zheng Zhang, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08485v1.pdf)  
  Keywords: ar, understanding, gaussian splatting, 3d gaussian, geometry, dynamic, semantic, fast  
- **[MVD-HuGaS: Human Gaussians from a Single Image via 3D Human Multi-view Diffusion Prior](https://arxiv.org/abs/2503.08218v1)**  
  Authors: Kaiqiang Xiong, Ying Feng, Qi Zhang, Jianbo Jiao, Yang Zhao, Zhihao Liang, Huachen Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08218v1.pdf)  
  Keywords: high-fidelity, human, 3d gaussian, geometry, ar  
- **[S3R-GS: Streamlining the Pipeline for Large-Scale Street Scene Reconstruction](https://arxiv.org/abs/2503.08217v1)**  
  Authors: Guangting Zheng, Jiajun Deng, Xiaomeng Chu, Yu Yuan, Houqiang Li, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08217v1.pdf)  
  Keywords: efficient rendering, ar, 3d reconstruction, gaussian splatting, 3d gaussian, dynamic, head, efficient  
- **[ArticulatedGS: Self-supervised Digital Twin Modeling of Articulated Objects using 3D Gaussian Splatting](https://arxiv.org/abs/2503.08135v1)**  
  Authors: Junfu Guo, Yu Xin, Gaoyi Liu, Kai Xu, Ligang Liu, Ruizhen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08135v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry, segmentation, semantic, motion  
- **[GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats](https://arxiv.org/abs/2503.08071v1)**  
  Authors: Kai Deng, Jian Yang, Shenlong Wang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08071v1.pdf)  
  Keywords: mapping, high-fidelity, ar, gaussian splatting, 3d gaussian, geometry, outdoor, slam, tracking, nerf, efficient  
- **[Multi-Modal 3D Mesh Reconstruction from Images and Text](https://arxiv.org/abs/2503.07190v1)**  
  Authors: Melvin Reka, Tessa Pulli, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07190v1.pdf)  
  Keywords: few-shot, 3d reconstruction, gaussian splatting, geometry, ar, robotics  
- **[DirectTriGS: Triplane-based Gaussian Splatting Field Representation for 3D Generation](https://arxiv.org/abs/2503.06900v1)**  
  Authors: Xiaoliang Ju, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06900v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, geometry  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: survey, semantic, geometry, ar  
- **[Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields](https://arxiv.org/abs/2503.06762v1)**  
  Authors: Abdelaziz Bouzidi, Hamid Laga, Hazem Wannous  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06762v1.pdf)  
  Keywords: ar, 3d reconstruction, acceleration, gaussian splatting, compact, geometry, lightweight, efficient, fast  
- **[REArtGS: Reconstructing and Generating Articulated Objects via 3D Gaussian Splatting with Geometric and Motion Constraints](https://arxiv.org/abs/2503.06677v2)**  
  Authors: Di Wu, Liu Liu, Zhou Linli, Anran Huang, Liangtu Song, Qiaojun Yu, Qi Wu, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06677v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sites.google.com/view/reartgs/home.)  
  Keywords: face, high-fidelity, human, gaussian splatting, 3d gaussian, geometry, dynamic, ar, motion  

### Large Scene

*Showing the latest 50 out of 76 papers*

- **[GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats](https://arxiv.org/abs/2503.08071v1)**  
  Authors: Kai Deng, Jian Yang, Shenlong Wang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08071v1.pdf)  
  Keywords: mapping, high-fidelity, ar, gaussian splatting, 3d gaussian, geometry, outdoor, slam, tracking, nerf, efficient  
- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: gaussian splatting, semantic, outdoor, ar  
- **[OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation](https://arxiv.org/abs/2502.18041v4)**  
  Authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.18041v4.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, outdoor, segmentation, semantic  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: mapping, high-fidelity, gaussian splatting, 3d gaussian, outdoor, geometry, slam, tracking, ar  
- **[RadSplatter: Extending 3D Gaussian Splatting to Radio Frequencies for Wireless Radiomap Extrapolation](https://arxiv.org/abs/2502.12686v1)**  
  Authors: Yiheng Wang, Ye Xue, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.12686v1.pdf)  
  Keywords: ar, autonomous driving, gaussian splatting, 3d gaussian, outdoor, efficient  
- **[GS-GVINS: A Tightly-integrated GNSS-Visual-Inertial Navigation System Augmented by 3D Gaussian Splatting](https://arxiv.org/abs/2502.10975v1)**  
  Authors: Zelin Zhou, Saurav Uprety, Shichuang Nie, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10975v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, outdoor, slam, dynamic, tracking, ar, motion  
- **[PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression](https://arxiv.org/abs/2502.04843v2)**  
  Authors: Feifei Li, Qi Song, Chi Zhang, Hui Shuai, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04843v2.pdf)  
  Keywords: gaussian splatting, nerf, ar, outdoor  
- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, outdoor, efficient  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: mapping, localization, gaussian splatting, geometry, outdoor, dynamic, large scene, slam, nerf, ar  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: understanding, 3d gaussian, outdoor, dynamic, ar, real-time rendering, motion  

### Model Compression

*Showing the latest 50 out of 547 papers*

- **[PCGS: Progressive Compression of 3D Gaussian Splatting](https://arxiv.org/abs/2503.08511v1)**  
  Authors: Yihang Chen, Mengyao Li, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08511v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YihangChen-ee/PCGS?style=social)](https://github.com/YihangChen-ee/PCGS)  
  Keywords: compression, ar, gaussian splatting, 3d gaussian, compact, efficient  
- **[Mitigating Ambiguities in 3D Classification with Gaussian Splatting](https://arxiv.org/abs/2503.08352v1)**  
  Authors: Ruiqi Zhang, Hao Zhu, Jingyi Zhao, Qi Zhang, Xun Cao, Zhan Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08352v1.pdf)  
  Keywords: gaussian splatting, face, efficient, ar  
- **[Uni-Gaussians: Unifying Camera and Lidar Simulation with Gaussians for Dynamic Driving Scenarios](https://arxiv.org/abs/2503.08317v1)**  
  Authors: Zikang Yuan, Yuechuan Pu, Hongcheng Luo, Fengtian Lang, Cheng Chi, Teng Li, Yingying Shen, Haiyang Sun, Bing Wang, Xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08317v1.pdf)  
  Keywords: ar, autonomous driving, gaussian splatting, neural rendering, dynamic, nerf, efficient  
- **[ELECTRA: A Symmetry-breaking Cartesian Network for Charge Density Prediction with Floating Orbitals](https://arxiv.org/abs/2503.08305v1)**  
  Authors: Jonas Elsborg, Luca Thiede, Alán Aspuru-Guzik, Tejs Vegge, Arghya Bhowmik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08305v1.pdf)  
  Keywords: gaussian splatting, efficient, compact, ar  
- **[S3R-GS: Streamlining the Pipeline for Large-Scale Street Scene Reconstruction](https://arxiv.org/abs/2503.08217v1)**  
  Authors: Guangting Zheng, Jiajun Deng, Xiaomeng Chu, Yu Yuan, Houqiang Li, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08217v1.pdf)  
  Keywords: efficient rendering, ar, 3d reconstruction, gaussian splatting, 3d gaussian, dynamic, head, efficient  
- **[MVGSR: Multi-View Consistency Gaussian Splatting for Robust Surface Reconstruction](https://arxiv.org/abs/2503.08093v1)**  
  Authors: Chenfeng Hou, Qi Xun Yeo, Mengqi Guo, Yongxin Su, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08093v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mvgsr.github.io}{this)  
  Keywords: dynamic, face, gaussian splatting, 3d gaussian, lightweight, segmentation, ar, fast  
- **[GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats](https://arxiv.org/abs/2503.08071v1)**  
  Authors: Kai Deng, Jian Yang, Shenlong Wang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08071v1.pdf)  
  Keywords: mapping, high-fidelity, ar, gaussian splatting, 3d gaussian, geometry, outdoor, slam, tracking, nerf, efficient  
- **[7DGS: Unified Spatial-Temporal-Angular Gaussian Splatting](https://arxiv.org/abs/2503.07946v1)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07946v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/7dgs/.)  
  Keywords: ar, gaussian splatting, 3d gaussian, dynamic, 4d, efficient, real-time rendering  
- **[EigenGS Representation: From Eigenspace to Gaussian Image Space](https://arxiv.org/abs/2503.07446v2)**  
  Authors: Lo-Wei Tai, Ching-En Li, Cheng-Lin Chen, Chih-Jung Tsai, Hwann-Tzong Chen, Tyng-Luh Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07446v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, ar  
- **[Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields](https://arxiv.org/abs/2503.06762v1)**  
  Authors: Abdelaziz Bouzidi, Hamid Laga, Hazem Wannous  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06762v1.pdf)  
  Keywords: ar, 3d reconstruction, acceleration, gaussian splatting, compact, geometry, lightweight, efficient, fast  

### Quality Enhancement

*Showing the latest 50 out of 236 papers*

- **[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://arxiv.org/abs/2503.08224v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08224v1.pdf)  
  Keywords: face, high-fidelity, lighting, gaussian splatting, deformation, 3d gaussian, relighting, relightable, head, tracking, avatar, ar  
- **[MVD-HuGaS: Human Gaussians from a Single Image via 3D Human Multi-view Diffusion Prior](https://arxiv.org/abs/2503.08218v1)**  
  Authors: Kaiqiang Xiong, Ying Feng, Qi Zhang, Jianbo Jiao, Yang Zhao, Zhihao Liang, Huachen Gao, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08218v1.pdf)  
  Keywords: high-fidelity, human, 3d gaussian, geometry, ar  
- **[GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats](https://arxiv.org/abs/2503.08071v1)**  
  Authors: Kai Deng, Jian Yang, Shenlong Wang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08071v1.pdf)  
  Keywords: mapping, high-fidelity, ar, gaussian splatting, 3d gaussian, geometry, outdoor, slam, tracking, nerf, efficient  
- **[All That Glitters Is Not Gold: Key-Secured 3D Secrets within 3D Gaussian Splatting](https://arxiv.org/abs/2503.07191v1)**  
  Authors: Yan Ren, Shilin Lu, Adams Wai-Kin Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07191v1.pdf) | [![GitHub](https://img.shields.io/github/stars/RY-Paper/KeySS?style=social)](https://github.com/RY-Paper/KeySS)  
  Keywords: gaussian splatting, 3d gaussian, ar, high-fidelity  
- **[REArtGS: Reconstructing and Generating Articulated Objects via 3D Gaussian Splatting with Geometric and Motion Constraints](https://arxiv.org/abs/2503.06677v2)**  
  Authors: Di Wu, Liu Liu, Zhou Linli, Anran Huang, Liangtu Song, Qiaojun Yu, Qi Wu, Cewu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06677v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sites.google.com/view/reartgs/home.)  
  Keywords: face, high-fidelity, human, gaussian splatting, 3d gaussian, geometry, dynamic, ar, motion  
- **[Bayesian Fields: Task-driven Open-Set Semantic Gaussian Splatting](https://arxiv.org/abs/2503.05949v1)**  
  Authors: Dominic Maggio, Luca Carlone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05949v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MIT-SPARK/Bayesian-Fields?style=social)](https://github.com/MIT-SPARK/Bayesian-Fields)  
  Keywords: mapping, high-fidelity, ar, 3d reconstruction, gaussian splatting, 3d gaussian, semantic  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v2)**  
  Authors: Jiahui Fan, Fujun Luan, Jian Yang, Miloš Hašan, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v2.pdf)  
  Keywords: human, lighting, gaussian splatting, lightweight, 3d gaussian, relighting, relightable, high quality, ar, motion  
- **[MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions](https://arxiv.org/abs/2503.05182v1)**  
  Authors: Qingyuan Zhou, Yuehu Gong, Weidong Yang, Jiaze Li, Yeqi Luo, Baixin Xu, Shuhao Li, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05182v1.pdf)  
  Keywords: face, high-fidelity, 3d reconstruction, illumination, gaussian splatting, 3d gaussian, geometry, ar  
- **[EvolvingGS: High-Fidelity Streamable Volumetric Video via Evolving 3D Gaussian Representation](https://arxiv.org/abs/2503.05162v1)**  
  Authors: Chao Zhang, Yifeng Zhou, Shuheng Wang, Wenfa Li, Degang Wang, Yi Xu, Shaohui Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05162v1.pdf)  
  Keywords: dynamic, high-fidelity, compression, ar, human, gaussian splatting, 3d gaussian, high quality, efficient, fast, motion  
- **[GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2503.03984v1)**  
  Authors: Qianzhong Chen, Jiankai Sun, Naixiang Gao, JunEn Low, Timothy Chen, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03984v1.pdf)  
  Keywords: high-fidelity, ar, gaussian splatting, 3d gaussian, dynamic, efficient  

### Ray Tracing

- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: face, ar, ray tracing, lighting, geometry, relightable, dynamic, 4d, efficient, tracking, real-time rendering  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: face, shadow, reflection, ray tracing, lighting, gaussian splatting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, gaussian splatting, 3d gaussian, survey, ar  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: reflection, ar, ray tracing, acceleration, gaussian splatting, light transport, efficient  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: shadow, reflection, ray tracing, gaussian splatting, 3d gaussian, ar  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: reflection, ar, ray tracing, lighting, gaussian splatting, relighting, efficient  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: reflection, high-fidelity, ar, ray tracing, lighting, gaussian splatting, 3d gaussian, efficient, real-time rendering  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: global illumination, face, mapping, ar, illumination, gaussian splatting, geometry, nerf, efficient, fast  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v2)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v2.pdf)  
  Keywords: ar, ray tracing, gaussian splatting, 3d gaussian, efficient  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: gaussian splatting, ray tracing, 3d gaussian, ar  

### Relighting

*Showing the latest 50 out of 160 papers*

- **[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://arxiv.org/abs/2503.08224v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08224v1.pdf)  
  Keywords: face, high-fidelity, lighting, gaussian splatting, deformation, 3d gaussian, relighting, relightable, head, tracking, avatar, ar  
- **[D3DR: Lighting-Aware Object Insertion in Gaussian Splatting](https://arxiv.org/abs/2503.06740v1)**  
  Authors: Vsevolod Skorokhodov, Nikita Durasov, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06740v1.pdf)  
  Keywords: shadow, lighting, gaussian splatting, 3d gaussian, relighting, dynamic, ar  
- **[Introducing Unbiased Depth into 2D Gaussian Splatting for High-accuracy Surface Reconstruction](https://arxiv.org/abs/2503.06587v1)**  
  Authors: Xiaoming Peng, Yixin Yang, Yang Zhou, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06587v1.pdf)  
  Keywords: face, reflection, gaussian splatting, geometry, ar  
- **[ForestSplats: Deformable transient field for Gaussian Splatting in the Wild](https://arxiv.org/abs/2503.06179v1)**  
  Authors: Wongi Park, Myeongseok Nam, Siwon Kim, Sangwoo Jo, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06179v1.pdf)  
  Keywords: ar, semantic, lighting, gaussian splatting, 3d gaussian, efficient, real-time rendering  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v2)**  
  Authors: Jiahui Fan, Fujun Luan, Jian Yang, Miloš Hašan, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v2.pdf)  
  Keywords: human, lighting, gaussian splatting, lightweight, 3d gaussian, relighting, relightable, high quality, ar, motion  
- **[MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions](https://arxiv.org/abs/2503.05182v1)**  
  Authors: Qingyuan Zhou, Yuehu Gong, Weidong Yang, Jiaze Li, Yeqi Luo, Baixin Xu, Shuhao Li, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05182v1.pdf)  
  Keywords: face, high-fidelity, 3d reconstruction, illumination, gaussian splatting, 3d gaussian, geometry, ar  
- **[EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering](https://arxiv.org/abs/2502.20669v1)**  
  Authors: John J. Han, Jie Ying Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20669v1.pdf)  
  Keywords: face, 3d reconstruction, medical, lighting, gaussian splatting, 3d gaussian, geometry, ar  
- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941v1)**  
  Authors: Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16941v1.pdf)  
  Keywords: ar, lighting, 4d, nerf, efficient  
- **[RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection](https://arxiv.org/abs/2502.13071v1)**  
  Authors: Jingtong Yue, Zhiwei Lin, Xin Lin, Xiaoyu Zhou, Xiangtai Li, Lu Qi, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13071v1.pdf)  
  Keywords: face, 3d gaussian, ar, lighting  
- **[OMG: Opacity Matters in Material Modeling with Gaussian Splatting](https://arxiv.org/abs/2502.10988v2)**  
  Authors: Silong Yong, Venkata Nagarjun Pudureddiyur Manivannan, Bernhard Kerbl, Zifu Wan, Simon Stepputtis, Katia Sycara, Yaqi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10988v2.pdf)  
  Keywords: ar, lighting, gaussian splatting, 3d gaussian, geometry, neural rendering, real-time rendering  

### SLAM

*Showing the latest 50 out of 217 papers*

- **[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://arxiv.org/abs/2503.08224v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08224v1.pdf)  
  Keywords: face, high-fidelity, lighting, gaussian splatting, deformation, 3d gaussian, relighting, relightable, head, tracking, avatar, ar  
- **[GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats](https://arxiv.org/abs/2503.08071v1)**  
  Authors: Kai Deng, Jian Yang, Shenlong Wang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08071v1.pdf)  
  Keywords: mapping, high-fidelity, ar, gaussian splatting, 3d gaussian, geometry, outdoor, slam, tracking, nerf, efficient  
- **[POp-GS: Next Best View in 3D-Gaussian Splatting with P-Optimality](https://arxiv.org/abs/2503.07819v1)**  
  Authors: Joey Wilson, Marcelino Almeida, Sachit Mahajan, Martin Labrie, Maani Ghaffari, Omid Ghasemalizadeh, Min Sun, Cheng-Hao Kuo, Arnab Sen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07819v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, slam  
- **[Pixel to Gaussian: Ultra-Fast Continuous Super-Resolution with 2D Gaussian Modeling](https://arxiv.org/abs/2503.06617v1)**  
  Authors: Long Peng, Anran Wu, Wenbo Li, Peizhe Xia, Xueyuan Dai, Xinjie Zhang, Xin Di, Haoze Sun, Renjing Pei, Yang Wang, Yang Cao, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06617v1.pdf)  
  Keywords: gaussian splatting, mapping, ar, fast  
- **[Bayesian Fields: Task-driven Open-Set Semantic Gaussian Splatting](https://arxiv.org/abs/2503.05949v1)**  
  Authors: Dominic Maggio, Luca Carlone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05949v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MIT-SPARK/Bayesian-Fields?style=social)](https://github.com/MIT-SPARK/Bayesian-Fields)  
  Keywords: mapping, high-fidelity, ar, 3d reconstruction, gaussian splatting, 3d gaussian, semantic  
- **[LiDAR-enhanced 3D Gaussian Splatting Mapping](https://arxiv.org/abs/2503.05425v1)**  
  Authors: Jian Shen, Huai Yu, Ji Wu, Wen Yang, Gui-Song Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05425v1.pdf)  
  Keywords: mapping, gaussian splatting, 3d gaussian, geometry, dynamic, tracking, ar  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: ar, human, semantic, compact, geometry, dynamic, tracking, efficient  
- **[GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting](https://arxiv.org/abs/2503.05152v2)**  
  Authors: Kohei Honda, Takeshi Ishita, Yasuhiro Yoshimura, Ryo Yonetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05152v2.pdf)  
  Keywords: localization, gaussian splatting, 3d gaussian, head, ar  
- **[Instrument-Splatting: Controllable Photorealistic Reconstruction of Surgical Instruments Using Gaussian Splatting](https://arxiv.org/abs/2503.04082v1)**  
  Authors: Shuojue Yang, Zijian Wu, Mingxuan Hong, Qian Li, Daiyun Shen, Septimiu E. Salcudean, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04082v1.pdf)  
  Keywords: ar, 3d reconstruction, gaussian splatting, 3d gaussian, geometry, tracking, semantic  
- **[Direct Sparse Odometry with Continuous 3D Gaussian Maps for Indoor Environments](https://arxiv.org/abs/2503.03373v1)**  
  Authors: Jie Deng, Fengtian Lang, Zikang Yuan, Xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03373v1.pdf)  
  Keywords: localization, 3d gaussian, tracking, ar, robotics  

### Scene Understanding

*Showing the latest 50 out of 255 papers*

- **[TT-GaussOcc: Test-Time Compute for Self-Supervised Occupancy Prediction via Spatio-Temporal Gaussian Splatting](https://arxiv.org/abs/2503.08485v1)**  
  Authors: Fengyi Zhang, Huitong Yang, Zheng Zhang, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08485v1.pdf)  
  Keywords: ar, understanding, gaussian splatting, 3d gaussian, geometry, dynamic, semantic, fast  
- **[ArticulatedGS: Self-supervised Digital Twin Modeling of Articulated Objects using 3D Gaussian Splatting](https://arxiv.org/abs/2503.08135v1)**  
  Authors: Junfu Guo, Yu Xin, Gaoyi Liu, Kai Xu, Ligang Liu, Ruizhen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08135v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry, segmentation, semantic, motion  
- **[MVGSR: Multi-View Consistency Gaussian Splatting for Robust Surface Reconstruction](https://arxiv.org/abs/2503.08093v1)**  
  Authors: Chenfeng Hou, Qi Xun Yeo, Mengqi Guo, Yongxin Su, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08093v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mvgsr.github.io}{this)  
  Keywords: dynamic, face, gaussian splatting, 3d gaussian, lightweight, segmentation, ar, fast  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: survey, semantic, geometry, ar  
- **[CoDa-4DGS: Dynamic Gaussian Splatting with Context and Deformation Awareness for Autonomous Driving](https://arxiv.org/abs/2503.06744v1)**  
  Authors: Rui Song, Chenwei Liang, Yan Xia, Walter Zimmer, Hu Cao, Holger Caesar, Andreas Festag, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06744v1.pdf)  
  Keywords: ar, autonomous driving, gaussian splatting, deformation, dynamic, 4d, segmentation, semantic  
- **[SplatTalk: 3D VQA with Gaussian Splatting](https://arxiv.org/abs/2503.06271v1)**  
  Authors: Anh Thai, Songyou Peng, Kyle Genova, Leonidas Guibas, Thomas Funkhouser  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06271v1.pdf)  
  Keywords: vr, human, understanding, gaussian splatting, 3d gaussian, ar, robotics  
- **[ForestSplats: Deformable transient field for Gaussian Splatting in the Wild](https://arxiv.org/abs/2503.06179v1)**  
  Authors: Wongi Park, Myeongseok Nam, Siwon Kim, Sangwoo Jo, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06179v1.pdf)  
  Keywords: ar, semantic, lighting, gaussian splatting, 3d gaussian, efficient, real-time rendering  
- **[Feature-EndoGaussian: Feature Distilled Gaussian Splatting in Surgical Deformable Scene Reconstruction](https://arxiv.org/abs/2503.06161v1)**  
  Authors: Kai Li, Junhao Wang, William Han, Ding Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06161v1.pdf)  
  Keywords: ar, semantic, understanding, segmentation, gaussian splatting, deformation, 3d gaussian, dynamic, nerf, efficient  
- **[Bayesian Fields: Task-driven Open-Set Semantic Gaussian Splatting](https://arxiv.org/abs/2503.05949v1)**  
  Authors: Dominic Maggio, Luca Carlone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05949v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MIT-SPARK/Bayesian-Fields?style=social)](https://github.com/MIT-SPARK/Bayesian-Fields)  
  Keywords: mapping, high-fidelity, ar, 3d reconstruction, gaussian splatting, 3d gaussian, semantic  
- **[Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects](https://arxiv.org/abs/2503.05189v1)**  
  Authors: Justin Yu, Kush Hari, Karim El-Refai, Arnav Dalal, Justin Kerr, Chung Min Kim, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05189v1.pdf)  
  Keywords: ar, human, semantic, compact, geometry, dynamic, tracking, efficient  



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