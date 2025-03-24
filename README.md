# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-03-24 00:52:46

## Categories

- [3DGS Surveys](#3dgs-surveys) (25 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (429 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1507 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (511 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (564 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (104 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (493 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (79 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (571 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (250 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (34 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (162 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (226 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (263 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: 3d gaussian, real-time rendering, ar, survey, dynamic, gaussian splatting  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: survey, geometry, semantic, ar  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, ar, nerf, survey, 3d reconstruction, compression, efficient, gaussian splatting  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: deformation, ar, nerf, survey, 4d, dynamic, lighting, gaussian splatting, motion  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, ar, survey, ray tracing, gaussian splatting  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: outdoor, mapping, ar, survey, localization, face, tracking, geometry, dynamic, slam, lighting  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: illumination, 3d gaussian, ar, survey, recognition, gaussian splatting  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: compact, semantic, high-fidelity, autonomous driving, nerf, survey, ar, 3d reconstruction, geometry, dynamic, lighting, gaussian splatting, robotics  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: 3d gaussian, real-time rendering, ar, nerf, survey, understanding, gaussian splatting, robotics  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, nerf, survey, lighting, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 429 papers*

- **[1000+ FPS 4D Gaussian Splatting for Dynamic Scene Rendering](https://arxiv.org/abs/2503.16422v1)**  
  Authors: Yuheng Yuan, Qiuhong Shen, Xingyi Yang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16422v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4DGS-1K.github.io.)  
  Keywords: head, ar, fast, 4d, dynamic, gaussian splatting  
- **[OccluGaussian: Occlusion-Aware Gaussian Splatting for Large Scene Reconstruction and Rendering](https://arxiv.org/abs/2503.16177v1)**  
  Authors: Shiyong Liu, Xiao Tang, Zhihao Li, Yingfan He, Chongjie Ye, Jianzhuang Liu, Binxiao Huang, Shunbo Zhou, Xiaofei Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://occlugaussian.github.io.)  
  Keywords: large scene, 3d gaussian, ar, fast, gaussian splatting  
- **[VideoRFSplat: Direct Scene-Level Text-to-3D Gaussian Splatting Generation with Flexible Pose and Multi-View Joint Modeling](https://arxiv.org/abs/2503.15855v1)**  
  Authors: Hyojun Go, Byeongjun Park, Hyelin Nam, Byung-Hoon Kim, Hyungjin Chung, Changick Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.15855v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, fast, ar  
- **[ClimateGS: Real-Time Climate Simulation with 3D Gaussian Style Transfer](https://arxiv.org/abs/2503.14845v1)**  
  Authors: Yuezhen Xie, Meiying Zhang, Qi Hao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14845v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, ar, nerf, efficient  
- **[Improving Adaptive Density Control for 3D Gaussian Splatting](https://arxiv.org/abs/2503.14274v1)**  
  Authors: Glenn Grubert, Florian Barthel, Anna Hilsmann, Peter Eisert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14274v1.pdf)  
  Keywords: 3d gaussian, ar, fast, face, efficient, gaussian splatting  
- **[Gaussian On-the-Fly Splatting: A Progressive Framework for Robust Near Real-Time 3DGS Optimization](https://arxiv.org/abs/2503.13086v1)**  
  Authors: Yiwei Xu, Yifei Yu, Wentian Gan, Tengfei Wang, Zongqian Zhan, Hao Cheng, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13086v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, fast, efficient, gaussian splatting, motion  
- **[CAT-3DGS Pro: A New Benchmark for Efficient 3DGS Compression](https://arxiv.org/abs/2503.12862v1)**  
  Authors: Yu-Ting Zhan, He-bi Yang, Cheng-Yuan Ho, Jui-Chiu Chiang, Wen-Hsiao Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12862v1.pdf)  
  Keywords: acceleration, 3d gaussian, ar, nerf, fast, compression, efficient, gaussian splatting  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: deformation, 3d gaussian, outdoor, high-fidelity, ar, efficient rendering, geometry, efficient  
- **[VRsketch2Gaussian: 3D VR Sketch Guided 3D Object Generation with Gaussian Splatting](https://arxiv.org/abs/2503.12383v1)**  
  Authors: Songen Gu, Haoxuan Song, Binjie Liu, Qian Yu, Sanyi Zhang, Haiyong Jiang, Jin Huang, Feng Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12383v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, fast, efficient, gaussian splatting, vr  
- **[TopoGaussian: Inferring Internal Topology Structures from Visual Clues](https://arxiv.org/abs/2503.12343v1)**  
  Authors: Xiaoyu Xiong, Changyu Hu, Chunru Lin, Pingchuan Ma, Chuang Gan, Tao Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12343v1.pdf)  
  Keywords: ar, fast, face, gaussian splatting, robotics  

### Applications

*Showing the latest 50 out of 1507 papers*

- **[1000+ FPS 4D Gaussian Splatting for Dynamic Scene Rendering](https://arxiv.org/abs/2503.16422v1)**  
  Authors: Yuheng Yuan, Qiuhong Shen, Xingyi Yang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16422v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4DGS-1K.github.io.)  
  Keywords: head, ar, fast, 4d, dynamic, gaussian splatting  
- **[M3: 3D-Spatial MultiModal Memory](https://arxiv.org/abs/2503.16413v1)**  
  Authors: Xueyan Zou, Yuchen Song, Ri-Zhao Qiu, Xuanbin Peng, Jianglong Ye, Sifei Liu, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16413v1.pdf)  
  Keywords: 3d gaussian, ar, compression, efficient, gaussian splatting  
- **[Gaussian Graph Network: Learning Efficient and Generalizable Gaussian Representations from Multi-view Images](https://arxiv.org/abs/2503.16338v1)**  
  Authors: Shengjun Zhang, Xin Fei, Fangfu Liu, Haixu Song, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16338v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, ar  
- **[OccluGaussian: Occlusion-Aware Gaussian Splatting for Large Scene Reconstruction and Rendering](https://arxiv.org/abs/2503.16177v1)**  
  Authors: Shiyong Liu, Xiao Tang, Zhihao Li, Yingfan He, Chongjie Ye, Jianzhuang Liu, Binxiao Huang, Shunbo Zhou, Xiaofei Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://occlugaussian.github.io.)  
  Keywords: large scene, 3d gaussian, ar, fast, gaussian splatting  
- **[Enhancing Close-up Novel View Synthesis via Pseudo-labeling](https://arxiv.org/abs/2503.15908v1)**  
  Authors: Jiatong Xia, Libo Sun, Lingqiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.15908v1.pdf)  
  Keywords: nerf, gaussian splatting, 3d gaussian, ar  
- **[Repurposing 2D Diffusion Models with Gaussian Atlas for 3D Generation](https://arxiv.org/abs/2503.15877v1)**  
  Authors: Tiange Xiang, Kai Li, Chengjiang Long, Christian Häne, Peihong Guo, Scott Delp, Ehsan Adeli, Li Fei-Fei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.15877v1.pdf)  
  Keywords: 3d gaussian, ar  
- **[VideoRFSplat: Direct Scene-Level Text-to-3D Gaussian Splatting Generation with Flexible Pose and Multi-View Joint Modeling](https://arxiv.org/abs/2503.15855v1)**  
  Authors: Hyojun Go, Byeongjun Park, Hyelin Nam, Byung-Hoon Kim, Hyungjin Chung, Changick Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.15855v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, fast, ar  
- **[BARD-GS: Blur-Aware Reconstruction of Dynamic Scenes via Gaussian Splatting](https://arxiv.org/abs/2503.15835v1)**  
  Authors: Yiren Lu, Yunlai Zhou, Disheng Liu, Tuo Liang, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.15835v1.pdf)  
  Keywords: 3d gaussian, ar, dynamic, gaussian splatting, motion  
- **[CHROME: Clothed Human Reconstruction with Occlusion-Resilience and Multiview-Consistency from a Single Image](https://arxiv.org/abs/2503.15671v1)**  
  Authors: Arindam Dutta, Meng Zheng, Zhongpai Gao, Benjamin Planche, Anwesha Choudhuri, Terrence Chen, Amit K. Roy-Chowdhury, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.15671v1.pdf)  
  Keywords: 3d gaussian, human, ar, 3d reconstruction  
- **[ClimateGS: Real-Time Climate Simulation with 3D Gaussian Style Transfer](https://arxiv.org/abs/2503.14845v1)**  
  Authors: Yuezhen Xie, Meiying Zhang, Qi Hao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14845v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, ar, nerf, efficient  

### Avatar Generation

*Showing the latest 50 out of 511 papers*

- **[1000+ FPS 4D Gaussian Splatting for Dynamic Scene Rendering](https://arxiv.org/abs/2503.16422v1)**  
  Authors: Yuheng Yuan, Qiuhong Shen, Xingyi Yang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16422v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4DGS-1K.github.io.)  
  Keywords: head, ar, fast, 4d, dynamic, gaussian splatting  
- **[CHROME: Clothed Human Reconstruction with Occlusion-Resilience and Multiview-Consistency from a Single Image](https://arxiv.org/abs/2503.15671v1)**  
  Authors: Arindam Dutta, Meng Zheng, Zhongpai Gao, Benjamin Planche, Anwesha Choudhuri, Terrence Chen, Amit K. Roy-Chowdhury, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.15671v1.pdf)  
  Keywords: 3d gaussian, human, ar, 3d reconstruction  
- **[Improving Adaptive Density Control for 3D Gaussian Splatting](https://arxiv.org/abs/2503.14274v1)**  
  Authors: Glenn Grubert, Florian Barthel, Anna Hilsmann, Peter Eisert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14274v1.pdf)  
  Keywords: 3d gaussian, ar, fast, face, efficient, gaussian splatting  
- **[RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2503.14198v1)**  
  Authors: Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14198v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iSEE-Laboratory/RoGSplat?style=social)](https://github.com/iSEE-Laboratory/RoGSplat)  
  Keywords: 3d gaussian, high-fidelity, ar, sparse view, geometry, body, human, gaussian splatting  
- **[AV-Surf: Surface-Enhanced Geometry-Aware Novel-View Acoustic Synthesis](https://arxiv.org/abs/2503.12806v1)**  
  Authors: Hadam Baek, Hannie Shin, Jiyoung Seo, Chanwoo Kim, Saerom Kim, Hyeongbok Kim, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12806v1.pdf)  
  Keywords: 3d gaussian, reflection, ar, face, geometry, gaussian splatting  
- **[TopoGaussian: Inferring Internal Topology Structures from Visual Clues](https://arxiv.org/abs/2503.12343v1)**  
  Authors: Xiaoyu Xiong, Changyu Hu, Chunru Lin, Pingchuan Ma, Chuang Gan, Tao Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12343v1.pdf)  
  Keywords: ar, fast, face, gaussian splatting, robotics  
- **[GS-I$^{3}$: Gaussian Splatting for Surface Reconstruction from Illumination-Inconsistent Images](https://arxiv.org/abs/2503.12335v2)**  
  Authors: Tengfei Wang, Yongmao Hou, Zhaoning Zhang, Yiwei Xu, Zongqian Zhan, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12335v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TFwang-9527/GS-3I?style=social)](https://github.com/TFwang-9527/GS-3I)  
  Keywords: illumination, 3d gaussian, mapping, ar, face, lighting, gaussian splatting  
- **[3D Gaussian Splatting against Moving Objects for High-Fidelity Street Scene Reconstruction](https://arxiv.org/abs/2503.12001v2)**  
  Authors: Peizhen Zheng, Longfei Wei, Dongjing Jiang, Jianfei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12001v2.pdf)  
  Keywords: 3d gaussian, high-fidelity, autonomous driving, ar, face, 3d reconstruction, dynamic, gaussian splatting  
- **[Snapmoji: Instant Generation of Animatable Dual-Stylized Avatars](https://arxiv.org/abs/2503.11978v1)**  
  Authors: Eric M. Chen, Di Liu, Sizhuo Ma, Michael Vasilkovsky, Bing Zhou, Qiang Gao, Wenzhou Wang, Jiahao Luo, Dimitris N. Metaxas, Vincent Sitzmann, Jian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11978v1.pdf)  
  Keywords: 3d gaussian, ar, avatar, face, efficient rendering, dynamic, efficient, animation  
- **[Advancing 3D Gaussian Splatting Editing with Complementary and Consensus Information](https://arxiv.org/abs/2503.11601v1)**  
  Authors: Xuanqi Zhang, Jieun Lee, Chris Joslin, Wonsook Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11601v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, face  

### Dynamic Scene

*Showing the latest 50 out of 564 papers*

- **[1000+ FPS 4D Gaussian Splatting for Dynamic Scene Rendering](https://arxiv.org/abs/2503.16422v1)**  
  Authors: Yuheng Yuan, Qiuhong Shen, Xingyi Yang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16422v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4DGS-1K.github.io.)  
  Keywords: head, ar, fast, 4d, dynamic, gaussian splatting  
- **[BARD-GS: Blur-Aware Reconstruction of Dynamic Scenes via Gaussian Splatting](https://arxiv.org/abs/2503.15835v1)**  
  Authors: Yiren Lu, Yunlai Zhou, Disheng Liu, Tuo Liang, Yu Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.15835v1.pdf)  
  Keywords: 3d gaussian, ar, dynamic, gaussian splatting, motion  
- **[HandSplat: Embedding-Driven Gaussian Splatting for High-Fidelity Hand Rendering](https://arxiv.org/abs/2503.14736v1)**  
  Authors: Yilan Dong, Haohe Liu, Qing Wang, Jiahao Yang, Wenqing Wang, Gregory Slabaugh, Shanxin Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14736v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, geometry, dynamic, efficient, gaussian splatting, motion  
- **[SplatVoxel: History-Aware Novel View Streaming without Temporal Training](https://arxiv.org/abs/2503.14698v1)**  
  Authors: Yiming Wang, Lucy Chai, Xuan Luo, Michael Niemeyer, Manuel Lagunas, Stephen Lombardi, Siyu Tang, Tiancheng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14698v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://19reborn.github.io/SplatVoxel/)  
  Keywords: sparse-view, ar, tracking, efficient, gaussian splatting, motion  
- **[Light4GS: Lightweight Compact 4D Gaussian Splatting Generation via Context Model](https://arxiv.org/abs/2503.13948v1)**  
  Authors: Mufan Liu, Qi Yang, He Huang, Wenjie Huang, Zhenlong Yuan, Zhu Li, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13948v1.pdf)  
  Keywords: 3d gaussian, compact, high-fidelity, ar, lightweight, 4d, compression, dynamic, efficient, gaussian splatting, motion  
- **[DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction](https://arxiv.org/abs/2503.13176v1)**  
  Authors: Rui Wang, Quentin Lohmeyer, Mirko Meboldt, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13176v1.pdf)  
  Keywords: ar, nerf, 3d reconstruction, dynamic, gaussian splatting  
- **[Gaussian On-the-Fly Splatting: A Progressive Framework for Robust Near Real-Time 3DGS Optimization](https://arxiv.org/abs/2503.13086v1)**  
  Authors: Yiwei Xu, Yifei Yu, Wentian Gan, Tengfei Wang, Zongqian Zhan, Hao Cheng, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13086v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, fast, efficient, gaussian splatting, motion  
- **[Deblur Gaussian Splatting SLAM](https://arxiv.org/abs/2503.12572v1)**  
  Authors: Francesco Girlanda, Denys Rozumnyi, Marc Pollefeys, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12572v1.pdf)  
  Keywords: deformation, mapping, high-fidelity, ar, slam, gaussian splatting, motion  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: deformation, 3d gaussian, outdoor, high-fidelity, ar, efficient rendering, geometry, efficient  
- **[MTGS: Multi-Traversal Gaussian Splatting](https://arxiv.org/abs/2503.12552v2)**  
  Authors: Tianyu Li, Yihang Qiu, Zhenhua Wu, Carl Lindström, Peng Su, Matthias Nießner, Hongyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12552v2.pdf)  
  Keywords: high-fidelity, ar, geometry, dynamic, efficient, gaussian splatting  

### Few-shot

*Showing the latest 50 out of 104 papers*

- **[SplatVoxel: History-Aware Novel View Streaming without Temporal Training](https://arxiv.org/abs/2503.14698v1)**  
  Authors: Yiming Wang, Lucy Chai, Xuan Luo, Michael Niemeyer, Manuel Lagunas, Stephen Lombardi, Siyu Tang, Tiancheng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14698v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://19reborn.github.io/SplatVoxel/)  
  Keywords: sparse-view, ar, tracking, efficient, gaussian splatting, motion  
- **[RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2503.14198v1)**  
  Authors: Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14198v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iSEE-Laboratory/RoGSplat?style=social)](https://github.com/iSEE-Laboratory/RoGSplat)  
  Keywords: 3d gaussian, high-fidelity, ar, sparse view, geometry, body, human, gaussian splatting  
- **[RI3D: Few-Shot Gaussian Splatting With Repair and Inpainting Diffusion Priors](https://arxiv.org/abs/2503.10860v1)**  
  Authors: Avinash Paliwal, Xilong Zhou, Wei Ye, Jinhui Xiong, Rakesh Ranjan, Nima Khademi Kalantari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10860v1.pdf)  
  Keywords: gaussian splatting, ar, few-shot  
- **[Physics-Aware Human-Object Rendering from Sparse Views via 3D Gaussian Splatting](https://arxiv.org/abs/2503.09640v1)**  
  Authors: Weiquan Wang, Jun Xiao, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09640v1.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, sparse view, human, efficient, gaussian splatting  
- **[Multi-Modal 3D Mesh Reconstruction from Images and Text](https://arxiv.org/abs/2503.07190v1)**  
  Authors: Melvin Reka, Tessa Pulli, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07190v1.pdf)  
  Keywords: ar, few-shot, 3d reconstruction, geometry, gaussian splatting, robotics  
- **[GaussianCAD: Robust Self-Supervised CAD Reconstruction from Three Orthographic Views Using 3D Gaussian Splatting](https://arxiv.org/abs/2503.05161v1)**  
  Authors: Zheng Zhou, Zhe Li, Bo Yu, Lina Hu, Liang Dong, Zijian Yang, Xiaoli Liu, Ning Xu, Ziwei Wang, Yonghao Dang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05161v1.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, 3d reconstruction, gaussian splatting  
- **[S2Gaussian: Sparse-View Super-Resolution 3D Gaussian Splatting](https://arxiv.org/abs/2503.04314v1)**  
  Authors: Yecong Wan, Mingwen Shao, Yuanshuo Cheng, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04314v1.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, sparse view, geometry, gaussian splatting  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: semantic, ar, neural rendering, nerf, few-shot, human, efficient, gaussian splatting  
- **[Seeing A 3D World in A Grain of Sand](https://arxiv.org/abs/2503.00260v1)**  
  Authors: Yufan Zhang, Yu Ji, Yu Guo, Jinwei Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00260v1.pdf)  
  Keywords: 3d gaussian, ar, sparse view, face, 3d reconstruction, gaussian splatting  
- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: 3d gaussian, high-fidelity, ar, sparse view, 3d reconstruction, efficient, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 493 papers*

- **[CHROME: Clothed Human Reconstruction with Occlusion-Resilience and Multiview-Consistency from a Single Image](https://arxiv.org/abs/2503.15671v1)**  
  Authors: Arindam Dutta, Meng Zheng, Zhongpai Gao, Benjamin Planche, Anwesha Choudhuri, Terrence Chen, Amit K. Roy-Chowdhury, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.15671v1.pdf)  
  Keywords: 3d gaussian, human, ar, 3d reconstruction  
- **[HandSplat: Embedding-Driven Gaussian Splatting for High-Fidelity Hand Rendering](https://arxiv.org/abs/2503.14736v1)**  
  Authors: Yilan Dong, Haohe Liu, Qing Wang, Jiahao Yang, Wenqing Wang, Gregory Slabaugh, Shanxin Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14736v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, geometry, dynamic, efficient, gaussian splatting, motion  
- **[RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2503.14198v1)**  
  Authors: Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14198v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iSEE-Laboratory/RoGSplat?style=social)](https://github.com/iSEE-Laboratory/RoGSplat)  
  Keywords: 3d gaussian, high-fidelity, ar, sparse view, geometry, body, human, gaussian splatting  
- **[BG-Triangle: Bézier Gaussian Triangle for 3D Vectorization and Rendering](https://arxiv.org/abs/2503.13961v1)**  
  Authors: Minye Wu, Haizhao Dai, Kaixin Yao, Tinne Tuytelaars, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13961v1.pdf)  
  Keywords: efficient, 3d reconstruction, ar  
- **[DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction](https://arxiv.org/abs/2503.13176v1)**  
  Authors: Rui Wang, Quentin Lohmeyer, Mirko Meboldt, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13176v1.pdf)  
  Keywords: ar, nerf, 3d reconstruction, dynamic, gaussian splatting  
- **[CompMarkGS: Robust Watermarking for Compression 3D Gaussian Splatting](https://arxiv.org/abs/2503.12836v1)**  
  Authors: Sumin In, Youngdong Jang, Utae Jeong, MinHyuk Jang, Hyeongcheol Park, Eunbyung Park, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12836v1.pdf)  
  Keywords: 3d gaussian, ar, 3d reconstruction, compression, efficient, gaussian splatting  
- **[AV-Surf: Surface-Enhanced Geometry-Aware Novel-View Acoustic Synthesis](https://arxiv.org/abs/2503.12806v1)**  
  Authors: Hadam Baek, Hannie Shin, Jiyoung Seo, Chanwoo Kim, Saerom Kim, Hyeongbok Kim, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12806v1.pdf)  
  Keywords: 3d gaussian, reflection, ar, face, geometry, gaussian splatting  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: deformation, 3d gaussian, outdoor, high-fidelity, ar, efficient rendering, geometry, efficient  
- **[MTGS: Multi-Traversal Gaussian Splatting](https://arxiv.org/abs/2503.12552v2)**  
  Authors: Tianyu Li, Yihang Qiu, Zhenhua Wu, Carl Lindström, Peng Su, Matthias Nießner, Hongyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12552v2.pdf)  
  Keywords: high-fidelity, ar, geometry, dynamic, efficient, gaussian splatting  
- **[3D Gaussian Splatting against Moving Objects for High-Fidelity Street Scene Reconstruction](https://arxiv.org/abs/2503.12001v2)**  
  Authors: Peizhen Zheng, Longfei Wei, Dongjing Jiang, Jianfei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12001v2.pdf)  
  Keywords: 3d gaussian, high-fidelity, autonomous driving, ar, face, 3d reconstruction, dynamic, gaussian splatting  

### Large Scene

*Showing the latest 50 out of 79 papers*

- **[OccluGaussian: Occlusion-Aware Gaussian Splatting for Large Scene Reconstruction and Rendering](https://arxiv.org/abs/2503.16177v1)**  
  Authors: Shiyong Liu, Xiao Tang, Zhihao Li, Yingfan He, Chongjie Ye, Jianzhuang Liu, Binxiao Huang, Shunbo Zhou, Xiaofei Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16177v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://occlugaussian.github.io.)  
  Keywords: large scene, 3d gaussian, ar, fast, gaussian splatting  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: deformation, 3d gaussian, outdoor, high-fidelity, ar, efficient rendering, geometry, efficient  
- **[MuDG: Taming Multi-modal Diffusion with Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2503.10604v1)**  
  Authors: Yingshuang Zou, Yikang Ding, Chuanrui Zhang, Jiazhe Guo, Bohan Li, Xiaoyang Lyu, Feiyang Tan, Xiaojuan Qi, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10604v1.pdf)  
  Keywords: semantic, ar, autonomous driving, urban scene, gaussian splatting  
- **[GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats](https://arxiv.org/abs/2503.08071v1)**  
  Authors: Kai Deng, Jian Yang, Shenlong Wang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08071v1.pdf)  
  Keywords: 3d gaussian, outdoor, mapping, high-fidelity, ar, nerf, tracking, geometry, slam, efficient, gaussian splatting  
- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: gaussian splatting, outdoor, semantic, ar  
- **[OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation](https://arxiv.org/abs/2502.18041v4)**  
  Authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.18041v4.pdf)  
  Keywords: 3d gaussian, outdoor, semantic, ar, segmentation, gaussian splatting  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: 3d gaussian, outdoor, mapping, high-fidelity, ar, tracking, geometry, slam, gaussian splatting  
- **[RadSplatter: Extending 3D Gaussian Splatting to Radio Frequencies for Wireless Radiomap Extrapolation](https://arxiv.org/abs/2502.12686v1)**  
  Authors: Yiheng Wang, Ye Xue, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.12686v1.pdf)  
  Keywords: 3d gaussian, outdoor, autonomous driving, ar, efficient, gaussian splatting  
- **[GS-GVINS: A Tightly-integrated GNSS-Visual-Inertial Navigation System Augmented by 3D Gaussian Splatting](https://arxiv.org/abs/2502.10975v1)**  
  Authors: Zelin Zhou, Saurav Uprety, Shichuang Nie, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10975v1.pdf)  
  Keywords: 3d gaussian, outdoor, ar, tracking, dynamic, slam, gaussian splatting, motion  
- **[PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression](https://arxiv.org/abs/2502.04843v2)**  
  Authors: Feifei Li, Qi Song, Chi Zhang, Hui Shuai, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04843v2.pdf)  
  Keywords: nerf, gaussian splatting, outdoor, ar  

### Model Compression

*Showing the latest 50 out of 571 papers*

- **[M3: 3D-Spatial MultiModal Memory](https://arxiv.org/abs/2503.16413v1)**  
  Authors: Xueyan Zou, Yuchen Song, Ri-Zhao Qiu, Xuanbin Peng, Jianglong Ye, Sifei Liu, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16413v1.pdf)  
  Keywords: 3d gaussian, ar, compression, efficient, gaussian splatting  
- **[Gaussian Graph Network: Learning Efficient and Generalizable Gaussian Representations from Multi-view Images](https://arxiv.org/abs/2503.16338v1)**  
  Authors: Shengjun Zhang, Xin Fei, Fangfu Liu, Haixu Song, Yueqi Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.16338v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, ar  
- **[ClimateGS: Real-Time Climate Simulation with 3D Gaussian Style Transfer](https://arxiv.org/abs/2503.14845v1)**  
  Authors: Yuezhen Xie, Meiying Zhang, Qi Hao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14845v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, ar, nerf, efficient  
- **[HandSplat: Embedding-Driven Gaussian Splatting for High-Fidelity Hand Rendering](https://arxiv.org/abs/2503.14736v1)**  
  Authors: Yilan Dong, Haohe Liu, Qing Wang, Jiahao Yang, Wenqing Wang, Gregory Slabaugh, Shanxin Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14736v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, geometry, dynamic, efficient, gaussian splatting, motion  
- **[SplatVoxel: History-Aware Novel View Streaming without Temporal Training](https://arxiv.org/abs/2503.14698v1)**  
  Authors: Yiming Wang, Lucy Chai, Xuan Luo, Michael Niemeyer, Manuel Lagunas, Stephen Lombardi, Siyu Tang, Tiancheng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14698v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://19reborn.github.io/SplatVoxel/)  
  Keywords: sparse-view, ar, tracking, efficient, gaussian splatting, motion  
- **[Improving Adaptive Density Control for 3D Gaussian Splatting](https://arxiv.org/abs/2503.14274v1)**  
  Authors: Glenn Grubert, Florian Barthel, Anna Hilsmann, Peter Eisert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14274v1.pdf)  
  Keywords: 3d gaussian, ar, fast, face, efficient, gaussian splatting  
- **[Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images](https://arxiv.org/abs/2503.14171v1)**  
  Authors: Simon Niedermayr, Christoph Neuhauser Rüdiger Westermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14171v1.pdf)  
  Keywords: lightweight, gaussian splatting, 3d gaussian, ar  
- **[BG-Triangle: Bézier Gaussian Triangle for 3D Vectorization and Rendering](https://arxiv.org/abs/2503.13961v1)**  
  Authors: Minye Wu, Haizhao Dai, Kaixin Yao, Tinne Tuytelaars, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13961v1.pdf)  
  Keywords: efficient, 3d reconstruction, ar  
- **[Light4GS: Lightweight Compact 4D Gaussian Splatting Generation via Context Model](https://arxiv.org/abs/2503.13948v1)**  
  Authors: Mufan Liu, Qi Yang, He Huang, Wenjie Huang, Zhenlong Yuan, Zhu Li, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13948v1.pdf)  
  Keywords: 3d gaussian, compact, high-fidelity, ar, lightweight, 4d, compression, dynamic, efficient, gaussian splatting, motion  
- **[Gaussian On-the-Fly Splatting: A Progressive Framework for Robust Near Real-Time 3DGS Optimization](https://arxiv.org/abs/2503.13086v1)**  
  Authors: Yiwei Xu, Yifei Yu, Wentian Gan, Tengfei Wang, Zongqian Zhan, Hao Cheng, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13086v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, fast, efficient, gaussian splatting, motion  

### Quality Enhancement

*Showing the latest 50 out of 250 papers*

- **[HandSplat: Embedding-Driven Gaussian Splatting for High-Fidelity Hand Rendering](https://arxiv.org/abs/2503.14736v1)**  
  Authors: Yilan Dong, Haohe Liu, Qing Wang, Jiahao Yang, Wenqing Wang, Gregory Slabaugh, Shanxin Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14736v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, geometry, dynamic, efficient, gaussian splatting, motion  
- **[RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2503.14198v1)**  
  Authors: Junjin Xiao, Qing Zhang, Yonewei Nie, Lei Zhu, Wei-Shi Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14198v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iSEE-Laboratory/RoGSplat?style=social)](https://github.com/iSEE-Laboratory/RoGSplat)  
  Keywords: 3d gaussian, high-fidelity, ar, sparse view, geometry, body, human, gaussian splatting  
- **[Light4GS: Lightweight Compact 4D Gaussian Splatting Generation via Context Model](https://arxiv.org/abs/2503.13948v1)**  
  Authors: Mufan Liu, Qi Yang, He Huang, Wenjie Huang, Zhenlong Yuan, Zhu Li, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13948v1.pdf)  
  Keywords: 3d gaussian, compact, high-fidelity, ar, lightweight, 4d, compression, dynamic, efficient, gaussian splatting, motion  
- **[Gaussian On-the-Fly Splatting: A Progressive Framework for Robust Near Real-Time 3DGS Optimization](https://arxiv.org/abs/2503.13086v1)**  
  Authors: Yiwei Xu, Yifei Yu, Wentian Gan, Tengfei Wang, Zongqian Zhan, Hao Cheng, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13086v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, fast, efficient, gaussian splatting, motion  
- **[Deblur Gaussian Splatting SLAM](https://arxiv.org/abs/2503.12572v1)**  
  Authors: Francesco Girlanda, Denys Rozumnyi, Marc Pollefeys, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12572v1.pdf)  
  Keywords: deformation, mapping, high-fidelity, ar, slam, gaussian splatting, motion  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: deformation, 3d gaussian, outdoor, high-fidelity, ar, efficient rendering, geometry, efficient  
- **[MTGS: Multi-Traversal Gaussian Splatting](https://arxiv.org/abs/2503.12552v2)**  
  Authors: Tianyu Li, Yihang Qiu, Zhenhua Wu, Carl Lindström, Peng Su, Matthias Nießner, Hongyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12552v2.pdf)  
  Keywords: high-fidelity, ar, geometry, dynamic, efficient, gaussian splatting  
- **[VRsketch2Gaussian: 3D VR Sketch Guided 3D Object Generation with Gaussian Splatting](https://arxiv.org/abs/2503.12383v1)**  
  Authors: Songen Gu, Haoxuan Song, Binjie Liu, Qian Yu, Sanyi Zhang, Haiyong Jiang, Jin Huang, Feng Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12383v1.pdf)  
  Keywords: 3d gaussian, high-fidelity, ar, fast, efficient, gaussian splatting, vr  
- **[3D Gaussian Splatting against Moving Objects for High-Fidelity Street Scene Reconstruction](https://arxiv.org/abs/2503.12001v2)**  
  Authors: Peizhen Zheng, Longfei Wei, Dongjing Jiang, Jianfei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12001v2.pdf)  
  Keywords: 3d gaussian, high-fidelity, autonomous driving, ar, face, 3d reconstruction, dynamic, gaussian splatting  
- **[DynaGSLAM: Real-Time Gaussian-Splatting SLAM for Online Rendering, Tracking, Motion Predictions of Moving Objects in Dynamic Scenes](https://arxiv.org/abs/2503.11979v1)**  
  Authors: Runfa Blark Li, Mahdi Shaghaghi, Keito Suzuki, Xinshuang Liu, Varun Moparthi, Bang Du, Walker Curtis, Martin Renschler, Ki Myung Brian Lee, Nikolay Atanasov, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11979v1.pdf)  
  Keywords: 3d gaussian, high quality, mapping, ar, localization, fast, tracking, dynamic, slam, gaussian splatting, motion, robotics  

### Ray Tracing

- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: 3d gaussian, reflection, ar, neural rendering, ray tracing, fast, shadow, gaussian splatting  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: real-time rendering, ar, ray tracing, 4d, face, tracking, geometry, dynamic, lighting, efficient, relightable  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: reflection, ray tracing, face, lighting, shadow, gaussian splatting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, ar, survey, ray tracing, gaussian splatting  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: acceleration, reflection, ar, ray tracing, light transport, efficient, gaussian splatting  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: 3d gaussian, reflection, ar, ray tracing, shadow, gaussian splatting  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: reflection, ar, relighting, ray tracing, lighting, efficient, gaussian splatting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, reflection, high-fidelity, ar, ray tracing, lighting, efficient, gaussian splatting  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: illumination, mapping, ar, nerf, fast, face, geometry, efficient, gaussian splatting, global illumination  
- **[Neural Representation for Wireless Radiation Field Reconstruction: A 3D Gaussian Splatting Approach](https://arxiv.org/abs/2412.04832v3)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v3.pdf)  
  Keywords: 3d gaussian, ar, ray tracing, face, dynamic, efficient, gaussian splatting  

### Relighting

*Showing the latest 50 out of 162 papers*

- **[AV-Surf: Surface-Enhanced Geometry-Aware Novel-View Acoustic Synthesis](https://arxiv.org/abs/2503.12806v1)**  
  Authors: Hadam Baek, Hannie Shin, Jiyoung Seo, Chanwoo Kim, Saerom Kim, Hyeongbok Kim, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12806v1.pdf)  
  Keywords: 3d gaussian, reflection, ar, face, geometry, gaussian splatting  
- **[GS-I$^{3}$: Gaussian Splatting for Surface Reconstruction from Illumination-Inconsistent Images](https://arxiv.org/abs/2503.12335v2)**  
  Authors: Tengfei Wang, Yongmao Hou, Zhaoning Zhang, Yiwei Xu, Zongqian Zhan, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12335v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TFwang-9527/GS-3I?style=social)](https://github.com/TFwang-9527/GS-3I)  
  Keywords: illumination, 3d gaussian, mapping, ar, face, lighting, gaussian splatting  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: 3d gaussian, reflection, ar, neural rendering, ray tracing, fast, shadow, gaussian splatting  
- **[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://arxiv.org/abs/2503.08224v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08224v1.pdf)  
  Keywords: deformation, 3d gaussian, head, high-fidelity, ar, relighting, avatar, face, gaussian splatting, tracking, lighting, relightable  
- **[D3DR: Lighting-Aware Object Insertion in Gaussian Splatting](https://arxiv.org/abs/2503.06740v1)**  
  Authors: Vsevolod Skorokhodov, Nikita Durasov, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06740v1.pdf)  
  Keywords: 3d gaussian, ar, relighting, dynamic, lighting, shadow, gaussian splatting  
- **[Introducing Unbiased Depth into 2D Gaussian Splatting for High-accuracy Surface Reconstruction](https://arxiv.org/abs/2503.06587v1)**  
  Authors: Xiaoming Peng, Yixin Yang, Yang Zhou, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06587v1.pdf)  
  Keywords: reflection, ar, face, geometry, gaussian splatting  
- **[ForestSplats: Deformable transient field for Gaussian Splatting in the Wild](https://arxiv.org/abs/2503.06179v1)**  
  Authors: Wongi Park, Myeongseok Nam, Siwon Kim, Sangwoo Jo, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06179v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, semantic, ar, lighting, efficient, gaussian splatting  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v2)**  
  Authors: Jiahui Fan, Fujun Luan, Jian Yang, Miloš Hašan, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v2.pdf)  
  Keywords: 3d gaussian, high quality, ar, relighting, lightweight, gaussian splatting, lighting, human, relightable, motion  
- **[MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions](https://arxiv.org/abs/2503.05182v1)**  
  Authors: Qingyuan Zhou, Yuehu Gong, Weidong Yang, Jiaze Li, Yeqi Luo, Baixin Xu, Shuhao Li, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05182v1.pdf)  
  Keywords: illumination, 3d gaussian, high-fidelity, ar, face, 3d reconstruction, geometry, gaussian splatting  
- **[EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering](https://arxiv.org/abs/2502.20669v1)**  
  Authors: John J. Han, Jie Ying Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20669v1.pdf)  
  Keywords: 3d gaussian, ar, face, 3d reconstruction, geometry, lighting, gaussian splatting, medical  

### SLAM

*Showing the latest 50 out of 226 papers*

- **[SplatVoxel: History-Aware Novel View Streaming without Temporal Training](https://arxiv.org/abs/2503.14698v1)**  
  Authors: Yiming Wang, Lucy Chai, Xuan Luo, Michael Niemeyer, Manuel Lagunas, Stephen Lombardi, Siyu Tang, Tiancheng Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14698v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://19reborn.github.io/SplatVoxel/)  
  Keywords: sparse-view, ar, tracking, efficient, gaussian splatting, motion  
- **[Deblur Gaussian Splatting SLAM](https://arxiv.org/abs/2503.12572v1)**  
  Authors: Francesco Girlanda, Denys Rozumnyi, Marc Pollefeys, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12572v1.pdf)  
  Keywords: deformation, mapping, high-fidelity, ar, slam, gaussian splatting, motion  
- **[GS-I$^{3}$: Gaussian Splatting for Surface Reconstruction from Illumination-Inconsistent Images](https://arxiv.org/abs/2503.12335v2)**  
  Authors: Tengfei Wang, Yongmao Hou, Zhaoning Zhang, Yiwei Xu, Zongqian Zhan, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12335v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TFwang-9527/GS-3I?style=social)](https://github.com/TFwang-9527/GS-3I)  
  Keywords: illumination, 3d gaussian, mapping, ar, face, lighting, gaussian splatting  
- **[DynaGSLAM: Real-Time Gaussian-Splatting SLAM for Online Rendering, Tracking, Motion Predictions of Moving Objects in Dynamic Scenes](https://arxiv.org/abs/2503.11979v1)**  
  Authors: Runfa Blark Li, Mahdi Shaghaghi, Keito Suzuki, Xinshuang Liu, Varun Moparthi, Bang Du, Walker Curtis, Martin Renschler, Ki Myung Brian Lee, Nikolay Atanasov, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11979v1.pdf)  
  Keywords: 3d gaussian, high quality, mapping, ar, localization, fast, tracking, dynamic, slam, gaussian splatting, motion, robotics  
- **[EgoSplat: Open-Vocabulary Egocentric Scene Understanding with Language Embedded 3D Gaussian Splatting](https://arxiv.org/abs/2503.11345v1)**  
  Authors: Di Li, Jie Feng, Jiahao Chen, Weisheng Dong, Guanbin Li, Guangming Shi, Licheng Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11345v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, segmentation, localization, tracking, dynamic, understanding, gaussian splatting  
- **[GaussHDR: High Dynamic Range Gaussian Splatting via Learning Unified 3D and 2D Local Tone Mapping](https://arxiv.org/abs/2503.10143v1)**  
  Authors: Jinfeng Liu, Lingtong Kong, Bo Li, Dan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10143v1.pdf)  
  Keywords: 3d gaussian, mapping, ar, dynamic, gaussian splatting  
- **[Online Language Splatting](https://arxiv.org/abs/2503.09447v1)**  
  Authors: Saimouli Katragadda, Cho-Ying Wu, Yuliang Guo, Xinyu Huang, Guoquan Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09447v1.pdf)  
  Keywords: 3d gaussian, mapping, ar, dynamic, slam, human, efficient, gaussian splatting  
- **[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://arxiv.org/abs/2503.08224v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08224v1.pdf)  
  Keywords: deformation, 3d gaussian, head, high-fidelity, ar, relighting, avatar, face, gaussian splatting, tracking, lighting, relightable  
- **[GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats](https://arxiv.org/abs/2503.08071v1)**  
  Authors: Kai Deng, Jian Yang, Shenlong Wang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08071v1.pdf)  
  Keywords: 3d gaussian, outdoor, mapping, high-fidelity, ar, nerf, tracking, geometry, slam, efficient, gaussian splatting  
- **[POp-GS: Next Best View in 3D-Gaussian Splatting with P-Optimality](https://arxiv.org/abs/2503.07819v1)**  
  Authors: Joey Wilson, Marcelino Almeida, Sachit Mahajan, Martin Labrie, Maani Ghaffari, Omid Ghasemalizadeh, Min Sun, Cheng-Hao Kuo, Arnab Sen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07819v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, slam, ar  

### Scene Understanding

*Showing the latest 50 out of 263 papers*

- **[Rethinking End-to-End 2D to 3D Scene Segmentation in Gaussian Splatting](https://arxiv.org/abs/2503.14029v1)**  
  Authors: Runsong Zhu, Shi Qiu, Zhengzhe Liu, Ka-Hei Hui, Qianyi Wu, Pheng-Ann Heng, Chi-Wing Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.14029v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Runsong123/Unified-Lift?style=social)](https://github.com/Runsong123/Unified-Lift)  
  Keywords: 3d gaussian, ar, segmentation, understanding, gaussian splatting  
- **[SPC-GS: Gaussian Splatting with Semantic-Prompt Consistency for Indoor Open-World Free-view Synthesis from Sparse Inputs](https://arxiv.org/abs/2503.12535v1)**  
  Authors: Guibiao Liao, Qing Li, Zhenyu Bao, Guoping Qiu, Kanglin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12535v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, segmentation, gaussian splatting  
- **[EgoSplat: Open-Vocabulary Egocentric Scene Understanding with Language Embedded 3D Gaussian Splatting](https://arxiv.org/abs/2503.11345v1)**  
  Authors: Di Li, Jie Feng, Jiahao Chen, Weisheng Dong, Guanbin Li, Guangming Shi, Licheng Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11345v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, segmentation, localization, tracking, dynamic, understanding, gaussian splatting  
- **[MuDG: Taming Multi-modal Diffusion with Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2503.10604v1)**  
  Authors: Yingshuang Zou, Yikang Ding, Chuanrui Zhang, Jiazhe Guo, Bohan Li, Xiaoyang Lyu, Feiyang Tan, Xiaojuan Qi, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10604v1.pdf)  
  Keywords: semantic, ar, autonomous driving, urban scene, gaussian splatting  
- **[4D LangSplat: 4D Language Gaussian Splatting via Multimodal Large Language Models](https://arxiv.org/abs/2503.10437v1)**  
  Authors: Wanhua Li, Renping Zhou, Jiawei Zhou, Yingwei Song, Johannes Herter, Minghan Qin, Gao Huang, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10437v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, 4d, dynamic, efficient, gaussian splatting  
- **[TGP: Two-modal occupancy prediction with 3D Gaussian and sparse points for 3D Environment Awareness](https://arxiv.org/abs/2503.09941v1)**  
  Authors: Mu Chen, Wenyu Chen, Mingchuan Yang, Yuan Zhang, Tao Han, Xinchi Li, Yunlong Li, Huaici Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09941v1.pdf)  
  Keywords: 3d gaussian, semantic, autonomous driving, ar, face, dynamic, understanding, robotics  
- **[Hybrid Rendering for Multimodal Autonomous Driving: Merging Neural and Physics-Based Simulation](https://arxiv.org/abs/2503.09464v1)**  
  Authors: Máté Tóth, Péter Kovács, Zoltán Bendefy, Zoltán Hortsin, Balázs Teréki, Tamás Matuszka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09464v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, autonomous driving, segmentation, nerf, ar, face, dynamic, gaussian splatting  
- **[FPGS: Feed-Forward Semantic-aware Photorealistic Style Transfer of Large-Scale Gaussian Splatting](https://arxiv.org/abs/2503.09635v1)**  
  Authors: GeonU Kim, Kim Youwang, Lee Hyoseok, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09635v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kim-geonu.github.io/FPGS/)  
  Keywords: 3d gaussian, real-time rendering, semantic, ar, dynamic, efficient, gaussian splatting  
- **[TT-GaussOcc: Test-Time Compute for Self-Supervised Occupancy Prediction via Spatio-Temporal Gaussian Splatting](https://arxiv.org/abs/2503.08485v1)**  
  Authors: Fengyi Zhang, Huitong Yang, Zheng Zhang, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08485v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, fast, geometry, dynamic, understanding, gaussian splatting  
- **[ArticulatedGS: Self-supervised Digital Twin Modeling of Articulated Objects using 3D Gaussian Splatting](https://arxiv.org/abs/2503.08135v1)**  
  Authors: Junfu Guo, Yu Xin, Gaoyi Liu, Kai Xu, Ligang Liu, Ruizhen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08135v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, segmentation, geometry, gaussian splatting, motion  



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