# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-03-19 00:50:05

## Categories

- [3DGS Surveys](#3dgs-surveys) (25 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (424 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1487 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (504 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (558 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (102 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (488 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (78 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (562 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (247 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (34 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (163 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (223 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (262 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: survey, 3d gaussian, ar, dynamic, gaussian splatting, real-time rendering  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: survey, ar, geometry, semantic  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: efficient, nerf, 3d gaussian, survey, compression, ar, 3d reconstruction, gaussian splatting, real-time rendering  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: survey, nerf, lighting, ar, dynamic, deformation, gaussian splatting, 4d, motion  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, ar, 3d gaussian, ray tracing, gaussian splatting  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: survey, 3d gaussian, lighting, geometry, tracking, ar, dynamic, localization, outdoor, reflection, face, mapping, slam  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: recognition, survey, 3d gaussian, ar, gaussian splatting, illumination  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: nerf, survey, lighting, geometry, autonomous driving, ar, dynamic, 3d reconstruction, high-fidelity, gaussian splatting, compact, robotics, semantic  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: survey, nerf, 3d gaussian, ar, gaussian splatting, understanding, real-time rendering, robotics  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: survey, nerf, 3d gaussian, lighting, ar, high-fidelity, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 424 papers*

- **[Gaussian On-the-Fly Splatting: A Progressive Framework for Robust Near Real-Time 3DGS Optimization](https://arxiv.org/abs/2503.13086v1)**  
  Authors: Yiwei Xu, Yifei Yu, Wentian Gan, Tengfei Wang, Zongqian Zhan, Hao Cheng, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13086v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, high-fidelity, fast, gaussian splatting, motion  
- **[CAT-3DGS Pro: A New Benchmark for Efficient 3DGS Compression](https://arxiv.org/abs/2503.12862v1)**  
  Authors: Yu-Ting Zhan, He-bi Yang, Cheng-Yuan Ho, Jui-Chiu Chiang, Wen-Hsiao Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12862v1.pdf)  
  Keywords: efficient, nerf, 3d gaussian, compression, ar, fast, gaussian splatting, acceleration  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, geometry, high-fidelity, deformation, outdoor, efficient rendering  
- **[VRsketch2Gaussian: 3D VR Sketch Guided 3D Object Generation with Gaussian Splatting](https://arxiv.org/abs/2503.12383v1)**  
  Authors: Songen Gu, Haoxuan Song, Binjie Liu, Qian Yu, Sanyi Zhang, Haiyong Jiang, Jin Huang, Feng Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12383v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, vr, high-fidelity, fast, gaussian splatting  
- **[TopoGaussian: Inferring Internal Topology Structures from Visual Clues](https://arxiv.org/abs/2503.12343v1)**  
  Authors: Xiaoyu Xiong, Changyu Hu, Chunru Lin, Pingchuan Ma, Chuang Gan, Tao Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12343v1.pdf)  
  Keywords: ar, fast, gaussian splatting, face, robotics  
- **[Swift4D:Adaptive divide-and-conquer Gaussian Splatting for compact and efficient reconstruction of dynamic scene](https://arxiv.org/abs/2503.12307v1)**  
  Authors: Jiahao Wu, Rui Peng, Zhiyan Wang, Lu Xiao, Luyang Tang, Jinbo Yan, Kaiqiang Xiong, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12307v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WuJH2001/swift4d?style=social)](https://github.com/WuJH2001/swift4d)  
  Keywords: efficient, 3d gaussian, ar, dynamic, deformation, fast, gaussian splatting, 4d, compact  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: 3d gaussian, ar, ray tracing, fast, gaussian splatting, shadow, reflection, neural rendering  
- **[DynaGSLAM: Real-Time Gaussian-Splatting SLAM for Online Rendering, Tracking, Motion Predictions of Moving Objects in Dynamic Scenes](https://arxiv.org/abs/2503.11979v1)**  
  Authors: Runfa Blark Li, Mahdi Shaghaghi, Keito Suzuki, Xinshuang Liu, Varun Moparthi, Bang Du, Walker Curtis, Martin Renschler, Ki Myung Brian Lee, Nikolay Atanasov, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11979v1.pdf)  
  Keywords: 3d gaussian, ar, tracking, high quality, dynamic, localization, fast, gaussian splatting, motion, robotics, mapping, slam  
- **[Snapmoji: Instant Generation of Animatable Dual-Stylized Avatars](https://arxiv.org/abs/2503.11978v1)**  
  Authors: Eric M. Chen, Di Liu, Sizhuo Ma, Michael Vasilkovsky, Bing Zhou, Qiang Gao, Wenzhou Wang, Jiahao Luo, Dimitris N. Metaxas, Vincent Sitzmann, Jian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11978v1.pdf)  
  Keywords: efficient, avatar, 3d gaussian, ar, animation, dynamic, face, efficient rendering  
- **[Industrial-Grade Sensor Simulation via Gaussian Splatting: A Modular Framework for Scalable Editing and Full-Stack Validation](https://arxiv.org/abs/2503.11731v1)**  
  Authors: Xianming Zeng, Sicong Du, Qifeng Chen, Lizhe Liu, Haoyu Shu, Jiaxuan Gao, Jiarun Liu, Jiulong Xu, Jianyun Xu, Mingxia Chen, Yiru Zhao, Peng Chen, Yapeng Xue, Chunming Zhao, Sheng Yang, Qiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11731v1.pdf)  
  Keywords: nerf, ar, autonomous driving, dynamic, gaussian splatting, face, real-time rendering  

### Applications

*Showing the latest 50 out of 1487 papers*

- **[Generative Gaussian Splatting: Generating 3D Scenes with Video Diffusion Priors](https://arxiv.org/abs/2503.13272v1)**  
  Authors: Katja Schwarz, Norman Mueller, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13272v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://katjaschwarz.github.io/ggs/)  
  Keywords: ar, 3d gaussian, gaussian splatting  
- **[DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction](https://arxiv.org/abs/2503.13176v1)**  
  Authors: Rui Wang, Quentin Lohmeyer, Mirko Meboldt, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13176v1.pdf)  
  Keywords: nerf, ar, dynamic, 3d reconstruction, gaussian splatting  
- **[Gaussian On-the-Fly Splatting: A Progressive Framework for Robust Near Real-Time 3DGS Optimization](https://arxiv.org/abs/2503.13086v1)**  
  Authors: Yiwei Xu, Yifei Yu, Wentian Gan, Tengfei Wang, Zongqian Zhan, Hao Cheng, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13086v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, high-fidelity, fast, gaussian splatting, motion  
- **[CAT-3DGS Pro: A New Benchmark for Efficient 3DGS Compression](https://arxiv.org/abs/2503.12862v1)**  
  Authors: Yu-Ting Zhan, He-bi Yang, Cheng-Yuan Ho, Jui-Chiu Chiang, Wen-Hsiao Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12862v1.pdf)  
  Keywords: efficient, nerf, 3d gaussian, compression, ar, fast, gaussian splatting, acceleration  
- **[CompMarkGS: Robust Watermarking for Compression 3D Gaussian Splatting](https://arxiv.org/abs/2503.12836v1)**  
  Authors: Sumin In, Youngdong Jang, Utae Jeong, MinHyuk Jang, Hyeongcheol Park, Eunbyung Park, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12836v1.pdf)  
  Keywords: efficient, 3d gaussian, compression, ar, 3d reconstruction, gaussian splatting  
- **[AV-Surf: Surface-Enhanced Geometry-Aware Novel-View Acoustic Synthesis](https://arxiv.org/abs/2503.12806v1)**  
  Authors: Hadam Baek, Hannie Shin, Jiyoung Seo, Chanwoo Kim, Saerom Kim, Hyeongbok Kim, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12806v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting, reflection, face  
- **[Deblur Gaussian Splatting SLAM](https://arxiv.org/abs/2503.12572v1)**  
  Authors: Francesco Girlanda, Denys Rozumnyi, Marc Pollefeys, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12572v1.pdf)  
  Keywords: ar, high-fidelity, deformation, gaussian splatting, motion, mapping, slam  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, geometry, high-fidelity, deformation, outdoor, efficient rendering  
- **[MTGS: Multi-Traversal Gaussian Splatting](https://arxiv.org/abs/2503.12552v1)**  
  Authors: Tianyu Li, Yihang Qiu, Zhenhua Wu, Carl Lindström, Peng Su, Matthias Nießner, Hongyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12552v1.pdf)  
  Keywords: efficient, ar, geometry, dynamic, high-fidelity, gaussian splatting  
- **[SPC-GS: Gaussian Splatting with Semantic-Prompt Consistency for Indoor Open-World Free-view Synthesis from Sparse Inputs](https://arxiv.org/abs/2503.12535v1)**  
  Authors: Guibiao Liao, Qing Li, Zhenyu Bao, Guoping Qiu, Kanglin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12535v1.pdf)  
  Keywords: segmentation, ar, 3d gaussian, gaussian splatting, semantic  

### Avatar Generation

*Showing the latest 50 out of 504 papers*

- **[AV-Surf: Surface-Enhanced Geometry-Aware Novel-View Acoustic Synthesis](https://arxiv.org/abs/2503.12806v1)**  
  Authors: Hadam Baek, Hannie Shin, Jiyoung Seo, Chanwoo Kim, Saerom Kim, Hyeongbok Kim, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12806v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting, reflection, face  
- **[TopoGaussian: Inferring Internal Topology Structures from Visual Clues](https://arxiv.org/abs/2503.12343v1)**  
  Authors: Xiaoyu Xiong, Changyu Hu, Chunru Lin, Pingchuan Ma, Chuang Gan, Tao Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12343v1.pdf)  
  Keywords: ar, fast, gaussian splatting, face, robotics  
- **[GS-I$^{3}$: Gaussian Splatting for Surface Reconstruction from Illumination-Inconsistent Images](https://arxiv.org/abs/2503.12335v2)**  
  Authors: Tengfei Wang, Yongmao Hou, Zhaoning Zhang, Yiwei Xu, Zongqian Zhan, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12335v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TFwang-9527/GS-3I?style=social)](https://github.com/TFwang-9527/GS-3I)  
  Keywords: 3d gaussian, lighting, ar, gaussian splatting, face, illumination, mapping  
- **[3D Gaussian Splatting against Moving Objects for High-Fidelity Street Scene Reconstruction](https://arxiv.org/abs/2503.12001v2)**  
  Authors: Peizhen Zheng, Longfei Wei, Dongjing Jiang, Jianfei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12001v2.pdf)  
  Keywords: 3d gaussian, ar, autonomous driving, dynamic, 3d reconstruction, high-fidelity, gaussian splatting, face  
- **[Snapmoji: Instant Generation of Animatable Dual-Stylized Avatars](https://arxiv.org/abs/2503.11978v1)**  
  Authors: Eric M. Chen, Di Liu, Sizhuo Ma, Michael Vasilkovsky, Bing Zhou, Qiang Gao, Wenzhou Wang, Jiahao Luo, Dimitris N. Metaxas, Vincent Sitzmann, Jian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11978v1.pdf)  
  Keywords: efficient, avatar, 3d gaussian, ar, animation, dynamic, face, efficient rendering  
- **[Advancing 3D Gaussian Splatting Editing with Complementary and Consensus Information](https://arxiv.org/abs/2503.11601v1)**  
  Authors: Xuanqi Zhang, Jieun Lee, Chris Joslin, Wonsook Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11601v1.pdf)  
  Keywords: ar, 3d gaussian, face, gaussian splatting  
- **[Industrial-Grade Sensor Simulation via Gaussian Splatting: A Modular Framework for Scalable Editing and Full-Stack Validation](https://arxiv.org/abs/2503.11731v1)**  
  Authors: Xianming Zeng, Sicong Du, Qifeng Chen, Lizhe Liu, Haoyu Shu, Jiaxuan Gao, Jiarun Liu, Jiulong Xu, Jianyun Xu, Mingxia Chen, Yiru Zhao, Peng Chen, Yapeng Xue, Chunming Zhao, Sheng Yang, Qiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11731v1.pdf)  
  Keywords: nerf, ar, autonomous driving, dynamic, gaussian splatting, face, real-time rendering  
- **[Uncertainty-Aware Normal-Guided Gaussian Splatting for Surface Reconstruction from Sparse Image Sequences](https://arxiv.org/abs/2503.11172v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Jinpu Zhang, Lei Feng, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11172v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, gaussian splatting, face  
- **[LHM: Large Animatable Human Reconstruction Model from a Single Image in Seconds](https://arxiv.org/abs/2503.10625v1)**  
  Authors: Lingteng Qiu, Xiaodong Gu, Peihao Li, Qi Zuo, Weichao Shen, Junfei Zhang, Kejie Qiu, Weihao Yuan, Guanying Chen, Zilong Dong, Liefeng Bo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10625v1.pdf)  
  Keywords: efficient, avatar, 3d gaussian, body, geometry, head, ar, high-fidelity, deformation, gaussian splatting, face, human  
- **[VicaSplat: A Single Run is All You Need for 3D Gaussian Splatting and Camera Estimation from Unposed Video Frames](https://arxiv.org/abs/2503.10286v1)**  
  Authors: Zhiqi Li, Chengrui Dong, Yiming Chen, Zhangchi Huang, Peidong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10286v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lizhiqi49.github.io/VicaSplat.)  
  Keywords: ar, 3d gaussian, head, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 558 papers*

- **[DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction](https://arxiv.org/abs/2503.13176v1)**  
  Authors: Rui Wang, Quentin Lohmeyer, Mirko Meboldt, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13176v1.pdf)  
  Keywords: nerf, ar, dynamic, 3d reconstruction, gaussian splatting  
- **[Gaussian On-the-Fly Splatting: A Progressive Framework for Robust Near Real-Time 3DGS Optimization](https://arxiv.org/abs/2503.13086v1)**  
  Authors: Yiwei Xu, Yifei Yu, Wentian Gan, Tengfei Wang, Zongqian Zhan, Hao Cheng, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13086v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, high-fidelity, fast, gaussian splatting, motion  
- **[Deblur Gaussian Splatting SLAM](https://arxiv.org/abs/2503.12572v1)**  
  Authors: Francesco Girlanda, Denys Rozumnyi, Marc Pollefeys, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12572v1.pdf)  
  Keywords: ar, high-fidelity, deformation, gaussian splatting, motion, mapping, slam  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, geometry, high-fidelity, deformation, outdoor, efficient rendering  
- **[MTGS: Multi-Traversal Gaussian Splatting](https://arxiv.org/abs/2503.12552v1)**  
  Authors: Tianyu Li, Yihang Qiu, Zhenhua Wu, Carl Lindström, Peng Su, Matthias Nießner, Hongyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12552v1.pdf)  
  Keywords: efficient, ar, geometry, dynamic, high-fidelity, gaussian splatting  
- **[Swift4D:Adaptive divide-and-conquer Gaussian Splatting for compact and efficient reconstruction of dynamic scene](https://arxiv.org/abs/2503.12307v1)**  
  Authors: Jiahao Wu, Rui Peng, Zhiyan Wang, Lu Xiao, Luyang Tang, Jinbo Yan, Kaiqiang Xiong, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12307v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WuJH2001/swift4d?style=social)](https://github.com/WuJH2001/swift4d)  
  Keywords: efficient, 3d gaussian, ar, dynamic, deformation, fast, gaussian splatting, 4d, compact  
- **[3D Gaussian Splatting against Moving Objects for High-Fidelity Street Scene Reconstruction](https://arxiv.org/abs/2503.12001v2)**  
  Authors: Peizhen Zheng, Longfei Wei, Dongjing Jiang, Jianfei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12001v2.pdf)  
  Keywords: 3d gaussian, ar, autonomous driving, dynamic, 3d reconstruction, high-fidelity, gaussian splatting, face  
- **[DynaGSLAM: Real-Time Gaussian-Splatting SLAM for Online Rendering, Tracking, Motion Predictions of Moving Objects in Dynamic Scenes](https://arxiv.org/abs/2503.11979v1)**  
  Authors: Runfa Blark Li, Mahdi Shaghaghi, Keito Suzuki, Xinshuang Liu, Varun Moparthi, Bang Du, Walker Curtis, Martin Renschler, Ki Myung Brian Lee, Nikolay Atanasov, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11979v1.pdf)  
  Keywords: 3d gaussian, ar, tracking, high quality, dynamic, localization, fast, gaussian splatting, motion, robotics, mapping, slam  
- **[Snapmoji: Instant Generation of Animatable Dual-Stylized Avatars](https://arxiv.org/abs/2503.11978v1)**  
  Authors: Eric M. Chen, Di Liu, Sizhuo Ma, Michael Vasilkovsky, Bing Zhou, Qiang Gao, Wenzhou Wang, Jiahao Luo, Dimitris N. Metaxas, Vincent Sitzmann, Jian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11978v1.pdf)  
  Keywords: efficient, avatar, 3d gaussian, ar, animation, dynamic, face, efficient rendering  
- **[EgoSplat: Open-Vocabulary Egocentric Scene Understanding with Language Embedded 3D Gaussian Splatting](https://arxiv.org/abs/2503.11345v1)**  
  Authors: Di Li, Jie Feng, Jiahao Chen, Weisheng Dong, Guanbin Li, Guangming Shi, Licheng Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11345v1.pdf)  
  Keywords: segmentation, 3d gaussian, ar, tracking, dynamic, localization, gaussian splatting, understanding, semantic  

### Few-shot

*Showing the latest 50 out of 102 papers*

- **[RI3D: Few-Shot Gaussian Splatting With Repair and Inpainting Diffusion Priors](https://arxiv.org/abs/2503.10860v1)**  
  Authors: Avinash Paliwal, Xilong Zhou, Wei Ye, Jinhui Xiong, Rakesh Ranjan, Nima Khademi Kalantari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10860v1.pdf)  
  Keywords: few-shot, ar, gaussian splatting  
- **[Physics-Aware Human-Object Rendering from Sparse Views via 3D Gaussian Splatting](https://arxiv.org/abs/2503.09640v1)**  
  Authors: Weiquan Wang, Jun Xiao, Yueting Zhuang, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09640v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, sparse view, gaussian splatting, sparse-view, human  
- **[Multi-Modal 3D Mesh Reconstruction from Images and Text](https://arxiv.org/abs/2503.07190v1)**  
  Authors: Melvin Reka, Tessa Pulli, Markus Vincze  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07190v1.pdf)  
  Keywords: ar, geometry, 3d reconstruction, gaussian splatting, few-shot, robotics  
- **[GaussianCAD: Robust Self-Supervised CAD Reconstruction from Three Orthographic Views Using 3D Gaussian Splatting](https://arxiv.org/abs/2503.05161v1)**  
  Authors: Zheng Zhou, Zhe Li, Bo Yu, Lina Hu, Liang Dong, Zijian Yang, Xiaoli Liu, Ning Xu, Ziwei Wang, Yonghao Dang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05161v1.pdf)  
  Keywords: ar, 3d gaussian, 3d reconstruction, gaussian splatting, sparse-view  
- **[S2Gaussian: Sparse-View Super-Resolution 3D Gaussian Splatting](https://arxiv.org/abs/2503.04314v1)**  
  Authors: Yecong Wan, Mingwen Shao, Yuanshuo Cheng, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.04314v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, sparse view, gaussian splatting, sparse-view  
- **[LensDFF: Language-enhanced Sparse Feature Distillation for Efficient Few-Shot Dexterous Manipulation](https://arxiv.org/abs/2503.03890v1)**  
  Authors: Qian Feng, David S. Martinez Lema, Jianxiang Feng, Zhaopeng Chen, Alois Knoll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.03890v1.pdf)  
  Keywords: efficient, nerf, ar, gaussian splatting, human, few-shot, semantic, neural rendering  
- **[Seeing A 3D World in A Grain of Sand](https://arxiv.org/abs/2503.00260v1)**  
  Authors: Yufan Zhang, Yu Ji, Yu Guo, Jinwei Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.00260v1.pdf)  
  Keywords: 3d gaussian, ar, 3d reconstruction, sparse view, gaussian splatting, face  
- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: efficient, 3d gaussian, ar, 3d reconstruction, high-fidelity, sparse view, gaussian splatting  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: nerf, ar, geometry, tracking, gaussian splatting, sparse-view, real-time rendering, mapping, slam  
- **[DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform](https://arxiv.org/abs/2501.12637v2)**  
  Authors: Hung Nguyen, Blark Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12637v2.pdf)  
  Keywords: nerf, ar, head, fast, few-shot  

### Geometry Reconstruction

*Showing the latest 50 out of 488 papers*

- **[DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction](https://arxiv.org/abs/2503.13176v1)**  
  Authors: Rui Wang, Quentin Lohmeyer, Mirko Meboldt, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13176v1.pdf)  
  Keywords: nerf, ar, dynamic, 3d reconstruction, gaussian splatting  
- **[CompMarkGS: Robust Watermarking for Compression 3D Gaussian Splatting](https://arxiv.org/abs/2503.12836v1)**  
  Authors: Sumin In, Youngdong Jang, Utae Jeong, MinHyuk Jang, Hyeongcheol Park, Eunbyung Park, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12836v1.pdf)  
  Keywords: efficient, 3d gaussian, compression, ar, 3d reconstruction, gaussian splatting  
- **[AV-Surf: Surface-Enhanced Geometry-Aware Novel-View Acoustic Synthesis](https://arxiv.org/abs/2503.12806v1)**  
  Authors: Hadam Baek, Hannie Shin, Jiyoung Seo, Chanwoo Kim, Saerom Kim, Hyeongbok Kim, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12806v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting, reflection, face  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, geometry, high-fidelity, deformation, outdoor, efficient rendering  
- **[MTGS: Multi-Traversal Gaussian Splatting](https://arxiv.org/abs/2503.12552v1)**  
  Authors: Tianyu Li, Yihang Qiu, Zhenhua Wu, Carl Lindström, Peng Su, Matthias Nießner, Hongyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12552v1.pdf)  
  Keywords: efficient, ar, geometry, dynamic, high-fidelity, gaussian splatting  
- **[3D Gaussian Splatting against Moving Objects for High-Fidelity Street Scene Reconstruction](https://arxiv.org/abs/2503.12001v2)**  
  Authors: Peizhen Zheng, Longfei Wei, Dongjing Jiang, Jianfei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12001v2.pdf)  
  Keywords: 3d gaussian, ar, autonomous driving, dynamic, 3d reconstruction, high-fidelity, gaussian splatting, face  
- **[LHM: Large Animatable Human Reconstruction Model from a Single Image in Seconds](https://arxiv.org/abs/2503.10625v1)**  
  Authors: Lingteng Qiu, Xiaodong Gu, Peihao Li, Qi Zuo, Weichao Shen, Junfei Zhang, Kejie Qiu, Weihao Yuan, Guanying Chen, Zilong Dong, Liefeng Bo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10625v1.pdf)  
  Keywords: efficient, avatar, 3d gaussian, body, geometry, head, ar, high-fidelity, deformation, gaussian splatting, face, human  
- **[GS-SDF: LiDAR-Augmented Gaussian Splatting and Neural SDF for Geometrically Consistent Rendering and Reconstruction](https://arxiv.org/abs/2503.10170v1)**  
  Authors: Jianheng Liu, Yunfei Wan, Bowen Wang, Chunran Zheng, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10170v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/GS-SDF?style=social)](https://github.com/hku-mars/GS-SDF)  
  Keywords: efficient, ar, geometry, autonomous driving, high-fidelity, gaussian splatting, face, robotics  
- **[AI-assisted 3D Preservation and Reconstruction of Temple Arts](https://arxiv.org/abs/2503.10031v1)**  
  Authors: Naai-Jung Shih  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10031v1.pdf)  
  Keywords: nerf, ar, animation, 3d reconstruction, face  
- **[TT-GaussOcc: Test-Time Compute for Self-Supervised Occupancy Prediction via Spatio-Temporal Gaussian Splatting](https://arxiv.org/abs/2503.08485v1)**  
  Authors: Fengyi Zhang, Huitong Yang, Zheng Zhang, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08485v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, dynamic, fast, gaussian splatting, understanding, semantic  

### Large Scene

*Showing the latest 50 out of 78 papers*

- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, geometry, high-fidelity, deformation, outdoor, efficient rendering  
- **[MuDG: Taming Multi-modal Diffusion with Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2503.10604v1)**  
  Authors: Yingshuang Zou, Yikang Ding, Chuanrui Zhang, Jiazhe Guo, Bohan Li, Xiaoyang Lyu, Feiyang Tan, Xiaojuan Qi, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10604v1.pdf)  
  Keywords: ar, autonomous driving, gaussian splatting, urban scene, semantic  
- **[GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats](https://arxiv.org/abs/2503.08071v1)**  
  Authors: Kai Deng, Jian Yang, Shenlong Wang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08071v1.pdf)  
  Keywords: efficient, nerf, 3d gaussian, ar, geometry, tracking, high-fidelity, gaussian splatting, outdoor, mapping, slam  
- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: ar, outdoor, semantic, gaussian splatting  
- **[OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation](https://arxiv.org/abs/2502.18041v4)**  
  Authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.18041v4.pdf)  
  Keywords: segmentation, 3d gaussian, ar, gaussian splatting, outdoor, semantic  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: 3d gaussian, ar, geometry, tracking, high-fidelity, gaussian splatting, outdoor, mapping, slam  
- **[RadSplatter: Extending 3D Gaussian Splatting to Radio Frequencies for Wireless Radiomap Extrapolation](https://arxiv.org/abs/2502.12686v1)**  
  Authors: Yiheng Wang, Ye Xue, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.12686v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, autonomous driving, gaussian splatting, outdoor  
- **[GS-GVINS: A Tightly-integrated GNSS-Visual-Inertial Navigation System Augmented by 3D Gaussian Splatting](https://arxiv.org/abs/2502.10975v1)**  
  Authors: Zelin Zhou, Saurav Uprety, Shichuang Nie, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10975v1.pdf)  
  Keywords: 3d gaussian, ar, tracking, dynamic, gaussian splatting, outdoor, motion, slam  
- **[PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression](https://arxiv.org/abs/2502.04843v2)**  
  Authors: Feifei Li, Qi Song, Chi Zhang, Hui Shuai, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04843v2.pdf)  
  Keywords: ar, nerf, outdoor, gaussian splatting  
- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, gaussian splatting, outdoor  

### Model Compression

*Showing the latest 50 out of 562 papers*

- **[Gaussian On-the-Fly Splatting: A Progressive Framework for Robust Near Real-Time 3DGS Optimization](https://arxiv.org/abs/2503.13086v1)**  
  Authors: Yiwei Xu, Yifei Yu, Wentian Gan, Tengfei Wang, Zongqian Zhan, Hao Cheng, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13086v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, high-fidelity, fast, gaussian splatting, motion  
- **[CAT-3DGS Pro: A New Benchmark for Efficient 3DGS Compression](https://arxiv.org/abs/2503.12862v1)**  
  Authors: Yu-Ting Zhan, He-bi Yang, Cheng-Yuan Ho, Jui-Chiu Chiang, Wen-Hsiao Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12862v1.pdf)  
  Keywords: efficient, nerf, 3d gaussian, compression, ar, fast, gaussian splatting, acceleration  
- **[CompMarkGS: Robust Watermarking for Compression 3D Gaussian Splatting](https://arxiv.org/abs/2503.12836v1)**  
  Authors: Sumin In, Youngdong Jang, Utae Jeong, MinHyuk Jang, Hyeongcheol Park, Eunbyung Park, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12836v1.pdf)  
  Keywords: efficient, 3d gaussian, compression, ar, 3d reconstruction, gaussian splatting  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, geometry, high-fidelity, deformation, outdoor, efficient rendering  
- **[MTGS: Multi-Traversal Gaussian Splatting](https://arxiv.org/abs/2503.12552v1)**  
  Authors: Tianyu Li, Yihang Qiu, Zhenhua Wu, Carl Lindström, Peng Su, Matthias Nießner, Hongyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12552v1.pdf)  
  Keywords: efficient, ar, geometry, dynamic, high-fidelity, gaussian splatting  
- **[VRsketch2Gaussian: 3D VR Sketch Guided 3D Object Generation with Gaussian Splatting](https://arxiv.org/abs/2503.12383v1)**  
  Authors: Songen Gu, Haoxuan Song, Binjie Liu, Qian Yu, Sanyi Zhang, Haiyong Jiang, Jin Huang, Feng Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12383v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, vr, high-fidelity, fast, gaussian splatting  
- **[Swift4D:Adaptive divide-and-conquer Gaussian Splatting for compact and efficient reconstruction of dynamic scene](https://arxiv.org/abs/2503.12307v1)**  
  Authors: Jiahao Wu, Rui Peng, Zhiyan Wang, Lu Xiao, Luyang Tang, Jinbo Yan, Kaiqiang Xiong, Ronggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12307v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WuJH2001/swift4d?style=social)](https://github.com/WuJH2001/swift4d)  
  Keywords: efficient, 3d gaussian, ar, dynamic, deformation, fast, gaussian splatting, 4d, compact  
- **[Snapmoji: Instant Generation of Animatable Dual-Stylized Avatars](https://arxiv.org/abs/2503.11978v1)**  
  Authors: Eric M. Chen, Di Liu, Sizhuo Ma, Michael Vasilkovsky, Bing Zhou, Qiang Gao, Wenzhou Wang, Jiahao Luo, Dimitris N. Metaxas, Vincent Sitzmann, Jian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11978v1.pdf)  
  Keywords: efficient, avatar, 3d gaussian, ar, animation, dynamic, face, efficient rendering  
- **[LHM: Large Animatable Human Reconstruction Model from a Single Image in Seconds](https://arxiv.org/abs/2503.10625v1)**  
  Authors: Lingteng Qiu, Xiaodong Gu, Peihao Li, Qi Zuo, Weichao Shen, Junfei Zhang, Kejie Qiu, Weihao Yuan, Guanying Chen, Zilong Dong, Liefeng Bo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10625v1.pdf)  
  Keywords: efficient, avatar, 3d gaussian, body, geometry, head, ar, high-fidelity, deformation, gaussian splatting, face, human  
- **[4D LangSplat: 4D Language Gaussian Splatting via Multimodal Large Language Models](https://arxiv.org/abs/2503.10437v1)**  
  Authors: Wanhua Li, Renping Zhou, Jiawei Zhou, Yingwei Song, Johannes Herter, Minghan Qin, Gao Huang, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10437v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, dynamic, gaussian splatting, 4d, semantic  

### Quality Enhancement

*Showing the latest 50 out of 247 papers*

- **[Gaussian On-the-Fly Splatting: A Progressive Framework for Robust Near Real-Time 3DGS Optimization](https://arxiv.org/abs/2503.13086v1)**  
  Authors: Yiwei Xu, Yifei Yu, Wentian Gan, Tengfei Wang, Zongqian Zhan, Hao Cheng, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.13086v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, high-fidelity, fast, gaussian splatting, motion  
- **[Deblur Gaussian Splatting SLAM](https://arxiv.org/abs/2503.12572v1)**  
  Authors: Francesco Girlanda, Denys Rozumnyi, Marc Pollefeys, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12572v1.pdf)  
  Keywords: ar, high-fidelity, deformation, gaussian splatting, motion, mapping, slam  
- **[Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View](https://arxiv.org/abs/2503.12553v1)**  
  Authors: Xianzu Wu, Zhenxin Ai, Harry Yang, Ser-Nam Lim, Jun Liu, Huan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12553v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, geometry, high-fidelity, deformation, outdoor, efficient rendering  
- **[MTGS: Multi-Traversal Gaussian Splatting](https://arxiv.org/abs/2503.12552v1)**  
  Authors: Tianyu Li, Yihang Qiu, Zhenhua Wu, Carl Lindström, Peng Su, Matthias Nießner, Hongyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12552v1.pdf)  
  Keywords: efficient, ar, geometry, dynamic, high-fidelity, gaussian splatting  
- **[VRsketch2Gaussian: 3D VR Sketch Guided 3D Object Generation with Gaussian Splatting](https://arxiv.org/abs/2503.12383v1)**  
  Authors: Songen Gu, Haoxuan Song, Binjie Liu, Qian Yu, Sanyi Zhang, Haiyong Jiang, Jin Huang, Feng Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12383v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, vr, high-fidelity, fast, gaussian splatting  
- **[3D Gaussian Splatting against Moving Objects for High-Fidelity Street Scene Reconstruction](https://arxiv.org/abs/2503.12001v2)**  
  Authors: Peizhen Zheng, Longfei Wei, Dongjing Jiang, Jianfei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12001v2.pdf)  
  Keywords: 3d gaussian, ar, autonomous driving, dynamic, 3d reconstruction, high-fidelity, gaussian splatting, face  
- **[DynaGSLAM: Real-Time Gaussian-Splatting SLAM for Online Rendering, Tracking, Motion Predictions of Moving Objects in Dynamic Scenes](https://arxiv.org/abs/2503.11979v1)**  
  Authors: Runfa Blark Li, Mahdi Shaghaghi, Keito Suzuki, Xinshuang Liu, Varun Moparthi, Bang Du, Walker Curtis, Martin Renschler, Ki Myung Brian Lee, Nikolay Atanasov, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11979v1.pdf)  
  Keywords: 3d gaussian, ar, tracking, high quality, dynamic, localization, fast, gaussian splatting, motion, robotics, mapping, slam  
- **[Uncertainty-Aware Normal-Guided Gaussian Splatting for Surface Reconstruction from Sparse Image Sequences](https://arxiv.org/abs/2503.11172v1)**  
  Authors: Zhen Tan, Xieyuanli Chen, Jinpu Zhang, Lei Feng, Dewen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11172v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, gaussian splatting, face  
- **[LHM: Large Animatable Human Reconstruction Model from a Single Image in Seconds](https://arxiv.org/abs/2503.10625v1)**  
  Authors: Lingteng Qiu, Xiaodong Gu, Peihao Li, Qi Zuo, Weichao Shen, Junfei Zhang, Kejie Qiu, Weihao Yuan, Guanying Chen, Zilong Dong, Liefeng Bo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10625v1.pdf)  
  Keywords: efficient, avatar, 3d gaussian, body, geometry, head, ar, high-fidelity, deformation, gaussian splatting, face, human  
- **[GS-SDF: LiDAR-Augmented Gaussian Splatting and Neural SDF for Geometrically Consistent Rendering and Reconstruction](https://arxiv.org/abs/2503.10170v1)**  
  Authors: Jianheng Liu, Yunfei Wan, Bowen Wang, Chunran Zheng, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10170v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/GS-SDF?style=social)](https://github.com/hku-mars/GS-SDF)  
  Keywords: efficient, ar, geometry, autonomous driving, high-fidelity, gaussian splatting, face, robotics  

### Ray Tracing

- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: 3d gaussian, ar, ray tracing, fast, gaussian splatting, shadow, reflection, neural rendering  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: efficient, ar, lighting, geometry, tracking, dynamic, ray tracing, 4d, face, real-time rendering, relightable  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: lighting, ray tracing, gaussian splatting, shadow, reflection, face  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, ar, 3d gaussian, ray tracing, gaussian splatting  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: efficient, ar, ray tracing, gaussian splatting, acceleration, reflection, light transport  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: 3d gaussian, ar, ray tracing, gaussian splatting, shadow, reflection  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: efficient, ar, lighting, ray tracing, gaussian splatting, reflection, relighting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: efficient, 3d gaussian, lighting, ar, ray tracing, high-fidelity, gaussian splatting, reflection, real-time rendering  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: efficient, nerf, ar, geometry, fast, gaussian splatting, global illumination, face, illumination, mapping  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v2)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v2.pdf)  
  Keywords: efficient, ar, 3d gaussian, ray tracing, gaussian splatting  

### Relighting

*Showing the latest 50 out of 163 papers*

- **[AV-Surf: Surface-Enhanced Geometry-Aware Novel-View Acoustic Synthesis](https://arxiv.org/abs/2503.12806v1)**  
  Authors: Hadam Baek, Hannie Shin, Jiyoung Seo, Chanwoo Kim, Saerom Kim, Hyeongbok Kim, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12806v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, gaussian splatting, reflection, face  
- **[GS-I$^{3}$: Gaussian Splatting for Surface Reconstruction from Illumination-Inconsistent Images](https://arxiv.org/abs/2503.12335v2)**  
  Authors: Tengfei Wang, Yongmao Hou, Zhaoning Zhang, Yiwei Xu, Zongqian Zhan, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12335v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TFwang-9527/GS-3I?style=social)](https://github.com/TFwang-9527/GS-3I)  
  Keywords: 3d gaussian, lighting, ar, gaussian splatting, face, illumination, mapping  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: 3d gaussian, ar, ray tracing, fast, gaussian splatting, shadow, reflection, neural rendering  
- **[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://arxiv.org/abs/2503.08224v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08224v1.pdf)  
  Keywords: avatar, 3d gaussian, lighting, head, tracking, ar, high-fidelity, deformation, gaussian splatting, face, relighting, relightable  
- **[D3DR: Lighting-Aware Object Insertion in Gaussian Splatting](https://arxiv.org/abs/2503.06740v1)**  
  Authors: Vsevolod Skorokhodov, Nikita Durasov, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06740v1.pdf)  
  Keywords: 3d gaussian, lighting, ar, dynamic, gaussian splatting, shadow, relighting  
- **[Introducing Unbiased Depth into 2D Gaussian Splatting for High-accuracy Surface Reconstruction](https://arxiv.org/abs/2503.06587v1)**  
  Authors: Xiaoming Peng, Yixin Yang, Yang Zhou, Hui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06587v1.pdf)  
  Keywords: ar, geometry, gaussian splatting, reflection, face  
- **[ForestSplats: Deformable transient field for Gaussian Splatting in the Wild](https://arxiv.org/abs/2503.06179v1)**  
  Authors: Wongi Park, Myeongseok Nam, Siwon Kim, Sangwoo Jo, Soomok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06179v1.pdf)  
  Keywords: efficient, 3d gaussian, lighting, ar, gaussian splatting, real-time rendering, semantic  
- **[Free Your Hands: Lightweight Relightable Turntable Capture Pipeline](https://arxiv.org/abs/2503.05511v2)**  
  Authors: Jiahui Fan, Fujun Luan, Jian Yang, Miloš Hašan, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05511v2.pdf)  
  Keywords: relightable, 3d gaussian, lighting, ar, high quality, gaussian splatting, motion, human, relighting, lightweight  
- **[MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions](https://arxiv.org/abs/2503.05182v1)**  
  Authors: Qingyuan Zhou, Yuehu Gong, Weidong Yang, Jiaze Li, Yeqi Luo, Baixin Xu, Shuhao Li, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.05182v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, 3d reconstruction, high-fidelity, gaussian splatting, face, illumination  
- **[EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering](https://arxiv.org/abs/2502.20669v1)**  
  Authors: John J. Han, Jie Ying Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20669v1.pdf)  
  Keywords: 3d gaussian, lighting, geometry, ar, 3d reconstruction, gaussian splatting, face, medical  

### SLAM

*Showing the latest 50 out of 223 papers*

- **[Deblur Gaussian Splatting SLAM](https://arxiv.org/abs/2503.12572v1)**  
  Authors: Francesco Girlanda, Denys Rozumnyi, Marc Pollefeys, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12572v1.pdf)  
  Keywords: ar, high-fidelity, deformation, gaussian splatting, motion, mapping, slam  
- **[GS-I$^{3}$: Gaussian Splatting for Surface Reconstruction from Illumination-Inconsistent Images](https://arxiv.org/abs/2503.12335v2)**  
  Authors: Tengfei Wang, Yongmao Hou, Zhaoning Zhang, Yiwei Xu, Zongqian Zhan, Xin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12335v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TFwang-9527/GS-3I?style=social)](https://github.com/TFwang-9527/GS-3I)  
  Keywords: 3d gaussian, lighting, ar, gaussian splatting, face, illumination, mapping  
- **[DynaGSLAM: Real-Time Gaussian-Splatting SLAM for Online Rendering, Tracking, Motion Predictions of Moving Objects in Dynamic Scenes](https://arxiv.org/abs/2503.11979v1)**  
  Authors: Runfa Blark Li, Mahdi Shaghaghi, Keito Suzuki, Xinshuang Liu, Varun Moparthi, Bang Du, Walker Curtis, Martin Renschler, Ki Myung Brian Lee, Nikolay Atanasov, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11979v1.pdf)  
  Keywords: 3d gaussian, ar, tracking, high quality, dynamic, localization, fast, gaussian splatting, motion, robotics, mapping, slam  
- **[EgoSplat: Open-Vocabulary Egocentric Scene Understanding with Language Embedded 3D Gaussian Splatting](https://arxiv.org/abs/2503.11345v1)**  
  Authors: Di Li, Jie Feng, Jiahao Chen, Weisheng Dong, Guanbin Li, Guangming Shi, Licheng Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11345v1.pdf)  
  Keywords: segmentation, 3d gaussian, ar, tracking, dynamic, localization, gaussian splatting, understanding, semantic  
- **[GaussHDR: High Dynamic Range Gaussian Splatting via Learning Unified 3D and 2D Local Tone Mapping](https://arxiv.org/abs/2503.10143v1)**  
  Authors: Jinfeng Liu, Lingtong Kong, Bo Li, Dan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10143v1.pdf)  
  Keywords: ar, 3d gaussian, dynamic, gaussian splatting, mapping  
- **[Online Language Splatting](https://arxiv.org/abs/2503.09447v1)**  
  Authors: Saimouli Katragadda, Cho-Ying Wu, Yuliang Guo, Xinyu Huang, Guoquan Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09447v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, dynamic, gaussian splatting, human, mapping, slam  
- **[HRAvatar: High-Quality and Relightable Gaussian Head Avatar](https://arxiv.org/abs/2503.08224v1)**  
  Authors: Dongbin Zhang, Yunfei Liu, Lijian Lin, Ye Zhu, Kangjie Chen, Minghan Qin, Yu Li, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08224v1.pdf)  
  Keywords: avatar, 3d gaussian, lighting, head, tracking, ar, high-fidelity, deformation, gaussian splatting, face, relighting, relightable  
- **[GigaSLAM: Large-Scale Monocular SLAM with Hierachical Gaussian Splats](https://arxiv.org/abs/2503.08071v1)**  
  Authors: Kai Deng, Jian Yang, Shenlong Wang, Jin Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08071v1.pdf)  
  Keywords: efficient, nerf, 3d gaussian, ar, geometry, tracking, high-fidelity, gaussian splatting, outdoor, mapping, slam  
- **[POp-GS: Next Best View in 3D-Gaussian Splatting with P-Optimality](https://arxiv.org/abs/2503.07819v1)**  
  Authors: Joey Wilson, Marcelino Almeida, Sachit Mahajan, Martin Labrie, Maani Ghaffari, Omid Ghasemalizadeh, Min Sun, Cheng-Hao Kuo, Arnab Sen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.07819v1.pdf)  
  Keywords: ar, slam, 3d gaussian, gaussian splatting  
- **[Pixel to Gaussian: Ultra-Fast Continuous Super-Resolution with 2D Gaussian Modeling](https://arxiv.org/abs/2503.06617v1)**  
  Authors: Long Peng, Anran Wu, Wenbo Li, Peizhe Xia, Xueyuan Dai, Xinjie Zhang, Xin Di, Haoze Sun, Renjing Pei, Yang Wang, Yang Cao, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06617v1.pdf)  
  Keywords: ar, fast, mapping, gaussian splatting  

### Scene Understanding

*Showing the latest 50 out of 262 papers*

- **[SPC-GS: Gaussian Splatting with Semantic-Prompt Consistency for Indoor Open-World Free-view Synthesis from Sparse Inputs](https://arxiv.org/abs/2503.12535v1)**  
  Authors: Guibiao Liao, Qing Li, Zhenyu Bao, Guoping Qiu, Kanglin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12535v1.pdf)  
  Keywords: segmentation, ar, 3d gaussian, gaussian splatting, semantic  
- **[EgoSplat: Open-Vocabulary Egocentric Scene Understanding with Language Embedded 3D Gaussian Splatting](https://arxiv.org/abs/2503.11345v1)**  
  Authors: Di Li, Jie Feng, Jiahao Chen, Weisheng Dong, Guanbin Li, Guangming Shi, Licheng Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.11345v1.pdf)  
  Keywords: segmentation, 3d gaussian, ar, tracking, dynamic, localization, gaussian splatting, understanding, semantic  
- **[MuDG: Taming Multi-modal Diffusion with Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2503.10604v1)**  
  Authors: Yingshuang Zou, Yikang Ding, Chuanrui Zhang, Jiazhe Guo, Bohan Li, Xiaoyang Lyu, Feiyang Tan, Xiaojuan Qi, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10604v1.pdf)  
  Keywords: ar, autonomous driving, gaussian splatting, urban scene, semantic  
- **[4D LangSplat: 4D Language Gaussian Splatting via Multimodal Large Language Models](https://arxiv.org/abs/2503.10437v1)**  
  Authors: Wanhua Li, Renping Zhou, Jiawei Zhou, Yingwei Song, Johannes Herter, Minghan Qin, Gao Huang, Hanspeter Pfister  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.10437v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, dynamic, gaussian splatting, 4d, semantic  
- **[TGP: Two-modal occupancy prediction with 3D Gaussian and sparse points for 3D Environment Awareness](https://arxiv.org/abs/2503.09941v1)**  
  Authors: Mu Chen, Wenyu Chen, Mingchuan Yang, Yuan Zhang, Tao Han, Xinchi Li, Yunlong Li, Huaici Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09941v1.pdf)  
  Keywords: 3d gaussian, ar, autonomous driving, dynamic, understanding, face, robotics, semantic  
- **[Hybrid Rendering for Multimodal Autonomous Driving: Merging Neural and Physics-Based Simulation](https://arxiv.org/abs/2503.09464v1)**  
  Authors: Máté Tóth, Péter Kovács, Zoltán Bendefy, Zoltán Hortsin, Balázs Teréki, Tamás Matuszka  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09464v1.pdf)  
  Keywords: nerf, 3d gaussian, segmentation, ar, autonomous driving, dynamic, gaussian splatting, face, real-time rendering  
- **[FPGS: Feed-Forward Semantic-aware Photorealistic Style Transfer of Large-Scale Gaussian Splatting](https://arxiv.org/abs/2503.09635v1)**  
  Authors: GeonU Kim, Kim Youwang, Lee Hyoseok, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.09635v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kim-geonu.github.io/FPGS/)  
  Keywords: efficient, 3d gaussian, ar, dynamic, gaussian splatting, real-time rendering, semantic  
- **[TT-GaussOcc: Test-Time Compute for Self-Supervised Occupancy Prediction via Spatio-Temporal Gaussian Splatting](https://arxiv.org/abs/2503.08485v1)**  
  Authors: Fengyi Zhang, Huitong Yang, Zheng Zhang, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08485v1.pdf)  
  Keywords: 3d gaussian, ar, geometry, dynamic, fast, gaussian splatting, understanding, semantic  
- **[ArticulatedGS: Self-supervised Digital Twin Modeling of Articulated Objects using 3D Gaussian Splatting](https://arxiv.org/abs/2503.08135v1)**  
  Authors: Junfu Guo, Yu Xin, Gaoyi Liu, Kai Xu, Ligang Liu, Ruizhen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08135v1.pdf)  
  Keywords: segmentation, 3d gaussian, ar, geometry, gaussian splatting, motion, semantic  
- **[MVGSR: Multi-View Consistency Gaussian Splatting for Robust Surface Reconstruction](https://arxiv.org/abs/2503.08093v2)**  
  Authors: Chenfeng Hou, Qi Xun Yeo, Mengqi Guo, Yongxin Su, Yanyan Li, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08093v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mvgsr.github.io).)  
  Keywords: segmentation, 3d gaussian, ar, dynamic, fast, gaussian splatting, face, lightweight  



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