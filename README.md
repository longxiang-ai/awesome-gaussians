# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-03-05 00:50:00

## Categories

- [3DGS Surveys](#3dgs-surveys) (23 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (388 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1361 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (454 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (503 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (94 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (446 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (75 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (517 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (219 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (33 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (153 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (204 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (240 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, real-time rendering, nerf, survey, efficient, gaussian splatting, ar, compression  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: 4d, nerf, motion, survey, gaussian splatting, lighting, deformation, ar, dynamic  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, survey, gaussian splatting, ray tracing, ar  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: localization, 3d gaussian, reflection, outdoor, survey, geometry, tracking, slam, mapping, lighting, face, ar, dynamic  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: illumination, 3d gaussian, survey, gaussian splatting, ar, recognition  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: 3d reconstruction, autonomous driving, robotics, nerf, survey, geometry, compact, gaussian splatting, semantic, high-fidelity, lighting, ar, dynamic  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: 3d gaussian, real-time rendering, robotics, nerf, survey, gaussian splatting, ar, understanding  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: 3d gaussian, nerf, survey, gaussian splatting, high-fidelity, lighting, ar  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, autonomous driving, robotics, nerf, vr, survey, gaussian splatting, ar  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: survey, 3d gaussian, ar  

### Acceleration

*Showing the latest 50 out of 388 papers*

- **[InsTaG: Learning Personalized 3D Talking Head from Few-Second Video](https://arxiv.org/abs/2502.20387v1)**  
  Authors: Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Jun Zhou, Lin Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20387v1.pdf)  
  Keywords: lightweight, motion, head, fast, ar, dynamic  
- **[Does 3D Gaussian Splatting Need Accurate Volumetric Rendering?](https://arxiv.org/abs/2502.19318v1)**  
  Authors: Adam Celarek, George Kopanas, George Drettakis, Michael Wimmer, Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19318v1.pdf)  
  Keywords: 3d gaussian, nerf, efficient, gaussian splatting, fast, ar  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, real-time rendering, nerf, survey, efficient, gaussian splatting, ar, compression  
- **[GaussianFlowOcc: Sparse and Weakly Supervised Occupancy Estimation using Gaussian Splatting and Temporal Flow](https://arxiv.org/abs/2502.17288v2)**  
  Authors: Simon Boeder, Fabian Gigengack, Benjamin Risse  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17288v2.pdf)  
  Keywords: 3d gaussian, autonomous driving, efficient, gaussian splatting, fast, ar, dynamic  
- **[GS-TransUNet: Integrated 2D Gaussian Splatting and Transformer UNet for Accurate Skin Lesion Analysis](https://arxiv.org/abs/2502.16748v1)**  
  Authors: Anand Kumar, Kavinder Roghit Kanthen, Josna John  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16748v1.pdf)  
  Keywords: efficient, segmentation, gaussian splatting, fast, medical, ar  
- **[GS-QA: Comprehensive Quality Assessment Benchmark for Gaussian Splatting View Synthesis](https://arxiv.org/abs/2502.13196v1)**  
  Authors: Pedro Martin, António Rodrigues, João Ascenso, Maria Paula Queluz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13196v1.pdf)  
  Keywords: 3d gaussian, nerf, geometry, gaussian splatting, fast, ar, human  
- **[GaussianMotion: End-to-End Learning of Animatable Gaussian Avatars with Pose Guidance from Text](https://arxiv.org/abs/2502.11642v1)**  
  Authors: Gyumin Shim, Sangmin Lee, Jaegul Choo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.11642v1.pdf)  
  Keywords: 3d gaussian, motion, efficient, efficient rendering, human, gaussian splatting, face, ar, avatar  
- **[OMG: Opacity Matters in Material Modeling with Gaussian Splatting](https://arxiv.org/abs/2502.10988v2)**  
  Authors: Silong Yong, Venkata Nagarjun Pudureddiyur Manivannan, Bernhard Kerbl, Zifu Wan, Simon Stepputtis, Katia Sycara, Yaqi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10988v2.pdf)  
  Keywords: 3d gaussian, real-time rendering, geometry, gaussian splatting, lighting, ar, neural rendering  
- **[E-3DGS: Event-Based Novel View Rendering of Large-Scale Scenes Using 3D Gaussian Splatting](https://arxiv.org/abs/2502.10827v1)**  
  Authors: Sohaib Zahid, Viktor Rudnev, Eddy Ilg, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10827v1.pdf)  
  Keywords: 3d gaussian, nerf, motion, gaussian splatting, fast, lighting, ar, dynamic  
- **[Self-Calibrating Gaussian Splatting for Large Field of View Reconstruction](https://arxiv.org/abs/2502.09563v1)**  
  Authors: Youming Deng, Wenqi Xian, Guandao Yang, Leonidas Guibas, Gordon Wetzstein, Steve Marschner, Paul Debevec  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09563v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, fast, ar  

### Applications

*Showing the latest 50 out of 1361 papers*

- **[FlexDrive: Toward Trajectory Flexibility in Driving Scene Reconstruction and Rendering](https://arxiv.org/abs/2502.21093v2)**  
  Authors: Jingqiu Zhou, Lue Fan, Linjiang Huang, Xiaoyu Shi, Si Liu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.21093v2.pdf)  
  Keywords: ar, 3d gaussian, compact, gaussian splatting  
- **[EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering](https://arxiv.org/abs/2502.20669v1)**  
  Authors: John J. Han, Jie Ying Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20669v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, gaussian splatting, lighting, face, medical, ar  
- **[InsTaG: Learning Personalized 3D Talking Head from Few-Second Video](https://arxiv.org/abs/2502.20387v1)**  
  Authors: Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Jun Zhou, Lin Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20387v1.pdf)  
  Keywords: lightweight, motion, head, fast, ar, dynamic  
- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: ar, semantic, gaussian splatting, outdoor  
- **[Efficient Gaussian Splatting for Monocular Dynamic Scene Rendering via Sparse Time-Variant Attribute Modeling](https://arxiv.org/abs/2502.20378v1)**  
  Authors: Hanyang Kong, Xingyi Yang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20378v1.pdf)  
  Keywords: motion, efficient, gaussian splatting, ar, dynamic  
- **[No Parameters, No Problem: 3D Gaussian Splatting without Camera Intrinsics and Extrinsics](https://arxiv.org/abs/2502.19800v1)**  
  Authors: Dongbo Shi, Shen Cao, Lubin Fan, Bojian Wu, Jinhui Guo, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19800v1.pdf)  
  Keywords: ar, 3d gaussian, face, gaussian splatting  
- **[Open-Vocabulary Semantic Part Segmentation of 3D Human](https://arxiv.org/abs/2502.19782v1)**  
  Authors: Keito Suzuki, Bang Du, Girish Krishnan, Kunyao Chen, Runfa Blark Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19782v1.pdf)  
  Keywords: 3d gaussian, vr, segmentation, gaussian splatting, semantic, ar, human  
- **[Does 3D Gaussian Splatting Need Accurate Volumetric Rendering?](https://arxiv.org/abs/2502.19318v1)**  
  Authors: Adam Celarek, George Kopanas, George Drettakis, Michael Wimmer, Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19318v1.pdf)  
  Keywords: 3d gaussian, nerf, efficient, gaussian splatting, fast, ar  
- **[Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting](https://arxiv.org/abs/2502.19459v1)**  
  Authors: Yu Liu, Baoxiong Jia, Ruijie Lu, Junfeng Ni, Song-Chun Zhu, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19459v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, ar, dynamic  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, real-time rendering, nerf, survey, efficient, gaussian splatting, ar, compression  

### Avatar Generation

*Showing the latest 50 out of 454 papers*

- **[EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering](https://arxiv.org/abs/2502.20669v1)**  
  Authors: John J. Han, Jie Ying Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20669v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, gaussian splatting, lighting, face, medical, ar  
- **[InsTaG: Learning Personalized 3D Talking Head from Few-Second Video](https://arxiv.org/abs/2502.20387v1)**  
  Authors: Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Jun Zhou, Lin Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20387v1.pdf)  
  Keywords: lightweight, motion, head, fast, ar, dynamic  
- **[No Parameters, No Problem: 3D Gaussian Splatting without Camera Intrinsics and Extrinsics](https://arxiv.org/abs/2502.19800v1)**  
  Authors: Dongbo Shi, Shen Cao, Lubin Fan, Bojian Wu, Jinhui Guo, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19800v1.pdf)  
  Keywords: ar, 3d gaussian, face, gaussian splatting  
- **[Open-Vocabulary Semantic Part Segmentation of 3D Human](https://arxiv.org/abs/2502.19782v1)**  
  Authors: Keito Suzuki, Bang Du, Girish Krishnan, Kunyao Chen, Runfa Blark Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19782v1.pdf)  
  Keywords: 3d gaussian, vr, segmentation, gaussian splatting, semantic, ar, human  
- **[VR-Pipe: Streamlining Hardware Graphics Pipeline for Volume Rendering](https://arxiv.org/abs/2502.17078v1)**  
  Authors: Junseo Lee, Jaisung Kim, Junyong Park, Jaewoong Sim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17078v1.pdf)  
  Keywords: 3d gaussian, vr, head, gaussian splatting, ar  
- **[Dragen3D: Multiview Geometry Consistent 3D Gaussian Generation with Drag-Based Control](https://arxiv.org/abs/2502.16475v1)**  
  Authors: Jinbo Yan, Alan Zhao, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16475v1.pdf)  
  Keywords: 3d gaussian, geometry, efficient, gaussian splatting, mapping, face, ar  
- **[DynamicGSG: Dynamic 3D Gaussian Scene Graphs for Environment Adaptation](https://arxiv.org/abs/2502.15309v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Zhuo Yang, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15309v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GeLuzhou/Dynamic-GSG?style=social)](https://github.com/GeLuzhou/Dynamic-GSG)  
  Keywords: 3d gaussian, segmentation, gaussian splatting, semantic, high-fidelity, ar, dynamic, human  
- **[GS-Cache: A GS-Cache Inference Framework for Large-scale Gaussian Splatting Models](https://arxiv.org/abs/2502.14938v1)**  
  Authors: Miao Tao, Yuanzhen Zhou, Haoran Xu, Zeyu He, Zhenyu Yang, Yuchang Zhang, Zhongling Su, Linning Xu, Zhenxiang Ma, Rong Fu, Hengjie Li, Xingcheng Zhang, Jidong Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14938v1.pdf)  
  Keywords: 3d gaussian, vr, efficient, gaussian splatting, high-fidelity, face, ar, neural rendering  
- **[OG-Gaussian: Occupancy Based Street Gaussians for Autonomous Driving](https://arxiv.org/abs/2502.14235v1)**  
  Authors: Yedong Shen, Xinran Zhang, Yifan Duan, Shiqi Zhang, Heng Li, Yilong Wu, Jianmin Ji, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14235v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, head, gaussian splatting, semantic, ar, dynamic  
- **[GlossGau: Efficient Inverse Rendering for Glossy Surface with Anisotropic Spherical Gaussian](https://arxiv.org/abs/2502.14129v1)**  
  Authors: Bang Du, Runfa Blark Li, Chen Du, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14129v1.pdf)  
  Keywords: 3d gaussian, nerf, efficient, gaussian splatting, face, ar  

### Dynamic Scene

*Showing the latest 50 out of 503 papers*

- **[InsTaG: Learning Personalized 3D Talking Head from Few-Second Video](https://arxiv.org/abs/2502.20387v1)**  
  Authors: Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Jun Zhou, Lin Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20387v1.pdf)  
  Keywords: lightweight, motion, head, fast, ar, dynamic  
- **[Efficient Gaussian Splatting for Monocular Dynamic Scene Rendering via Sparse Time-Variant Attribute Modeling](https://arxiv.org/abs/2502.20378v1)**  
  Authors: Hanyang Kong, Xingyi Yang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20378v1.pdf)  
  Keywords: motion, efficient, gaussian splatting, ar, dynamic  
- **[Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting](https://arxiv.org/abs/2502.19459v1)**  
  Authors: Yu Liu, Baoxiong Jia, Ruijie Lu, Junfeng Ni, Song-Chun Zhu, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19459v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, ar, dynamic  
- **[GaussianFlowOcc: Sparse and Weakly Supervised Occupancy Estimation using Gaussian Splatting and Temporal Flow](https://arxiv.org/abs/2502.17288v2)**  
  Authors: Simon Boeder, Fabian Gigengack, Benjamin Risse  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17288v2.pdf)  
  Keywords: 3d gaussian, autonomous driving, efficient, gaussian splatting, fast, ar, dynamic  
- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941v1)**  
  Authors: Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16941v1.pdf)  
  Keywords: 4d, nerf, efficient, lighting, ar  
- **[Efficient 4D Gaussian Stream with Low Rank Adaptation](https://arxiv.org/abs/2502.16575v1)**  
  Authors: Zhenhuan Liu, Shuai Liu, Yidong Lu, Yirui Chen, Jie Yang, Wei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16575v1.pdf)  
  Keywords: 4d, 3d gaussian, efficient, deformation, ar, dynamic  
- **[DynamicGSG: Dynamic 3D Gaussian Scene Graphs for Environment Adaptation](https://arxiv.org/abs/2502.15309v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Zhuo Yang, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15309v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GeLuzhou/Dynamic-GSG?style=social)](https://github.com/GeLuzhou/Dynamic-GSG)  
  Keywords: 3d gaussian, segmentation, gaussian splatting, semantic, high-fidelity, ar, dynamic, human  
- **[CDGS: Confidence-Aware Depth Regularization for 3D Gaussian Splatting](https://arxiv.org/abs/2502.14684v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Steffen Urban, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14684v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, motion, efficient, gaussian splatting, ar  
- **[Exploiting Deblurring Networks for Radiance Fields](https://arxiv.org/abs/2502.14454v1)**  
  Authors: Haeyun Choi, Heemin Yang, Janghyeok Han, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14454v1.pdf)  
  Keywords: ar, 3d gaussian, motion  
- **[OG-Gaussian: Occupancy Based Street Gaussians for Autonomous Driving](https://arxiv.org/abs/2502.14235v1)**  
  Authors: Yedong Shen, Xinran Zhang, Yifan Duan, Shiqi Zhang, Heng Li, Yilong Wu, Jianmin Ji, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14235v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, head, gaussian splatting, semantic, ar, dynamic  

### Few-shot

*Showing the latest 50 out of 94 papers*

- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: 3d reconstruction, 3d gaussian, efficient, gaussian splatting, sparse view, high-fidelity, ar  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: real-time rendering, nerf, tracking, geometry, slam, gaussian splatting, mapping, ar, sparse-view  
- **[DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform](https://arxiv.org/abs/2501.12637v2)**  
  Authors: Hung Nguyen, Blark Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12637v2.pdf)  
  Keywords: nerf, head, few-shot, fast, ar  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: 4d, 3d gaussian, gaussian splatting, semantic, ar, sparse-view  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, nerf, efficient, gaussian splatting, ar, sparse-view  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: nerf, gaussian splatting, sparse view, lighting, face, medical, ar, dynamic, human  
- **[Synthetic Prior for Few-Shot Drivable Head Avatar Inversion](https://arxiv.org/abs/2501.06903v1)**  
  Authors: Wojciech Zielonka, Stephan J. Garbin, Alexandros Lattas, George Kopanas, Paulo Gotardo, Thabo Beeler, Justus Thies, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06903v1.pdf)  
  Keywords: 3d gaussian, head, few-shot, gaussian splatting, ar, avatar  
- **[NVS-SQA: Exploring Self-Supervised Quality Representation Learning for Neurally Synthesized Scenes without References](https://arxiv.org/abs/2501.06488v1)**  
  Authors: Qiang Qu, Yiran Shen, Xiaoming Chen, Yuk Ying Chung, Weidong Cai, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06488v1.pdf)  
  Keywords: 3d gaussian, nerf, gaussian splatting, sparse view, ar, human  
- **[FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency](https://arxiv.org/abs/2501.04628v1)**  
  Authors: Han Huang, Yulun Wu, Chao Deng, Ge Gao, Ming Gu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04628v1.pdf)  
  Keywords: gaussian splatting, sparse view, fast, face, ar, sparse-view  
- **[Dust to Tower: Coarse-to-Fine Photo-Realistic Scene Reconstruction from Sparse Uncalibrated Images](https://arxiv.org/abs/2412.19518v1)**  
  Authors: Xudong Cai, Yongcai Wang, Zhaoxin Fan, Deng Haoran, Shuo Wang, Wanting Li, Deying Li, Lun Luo, Minhang Wang, Jintao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19518v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, fast, ar, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 446 papers*

- **[EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering](https://arxiv.org/abs/2502.20669v1)**  
  Authors: John J. Han, Jie Ying Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20669v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, gaussian splatting, lighting, face, medical, ar  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, real-time rendering, nerf, survey, efficient, gaussian splatting, ar, compression  
- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: 3d reconstruction, 3d gaussian, efficient, gaussian splatting, sparse view, high-fidelity, ar  
- **[Laplace-Beltrami Operator for Gaussian Splatting](https://arxiv.org/abs/2502.17531v1)**  
  Authors: Hongyu Zhou, Zorah Lähner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17531v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, gaussian splatting, ar  
- **[Dragen3D: Multiview Geometry Consistent 3D Gaussian Generation with Drag-Based Control](https://arxiv.org/abs/2502.16475v1)**  
  Authors: Jinbo Yan, Alan Zhao, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16475v1.pdf)  
  Keywords: 3d gaussian, geometry, efficient, gaussian splatting, mapping, face, ar  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: 3d gaussian, outdoor, tracking, geometry, slam, gaussian splatting, high-fidelity, mapping, ar  
- **[CDGS: Confidence-Aware Depth Regularization for 3D Gaussian Splatting](https://arxiv.org/abs/2502.14684v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Steffen Urban, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14684v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, motion, efficient, gaussian splatting, ar  
- **[3D Gaussian Splatting aided Localization for Large and Complex Indoor-Environments](https://arxiv.org/abs/2502.13803v1)**  
  Authors: Vincent Ress, Jonas Meyer, Wei Zhang, David Skuddis, Uwe Soergel, Norbert Haala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13803v1.pdf)  
  Keywords: localization, 3d gaussian, geometry, slam, gaussian splatting, ar  
- **[Inter3D: A Benchmark and Strong Baseline for Human-Interactive 3D Object Reconstruction](https://arxiv.org/abs/2502.14004v1)**  
  Authors: Gan Chen, Ying He, Mulin Yu, F. Richard Yu, Gang Xu, Fei Ma, Ming Li, Guang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14004v1.pdf)  
  Keywords: 3d reconstruction, motion, efficient, gaussian splatting, dynamic, ar, neural rendering, human  
- **[GS-QA: Comprehensive Quality Assessment Benchmark for Gaussian Splatting View Synthesis](https://arxiv.org/abs/2502.13196v1)**  
  Authors: Pedro Martin, António Rodrigues, João Ascenso, Maria Paula Queluz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13196v1.pdf)  
  Keywords: 3d gaussian, nerf, geometry, gaussian splatting, fast, ar, human  

### Large Scene

*Showing the latest 50 out of 75 papers*

- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: ar, semantic, gaussian splatting, outdoor  
- **[OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation](https://arxiv.org/abs/2502.18041v2)**  
  Authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.18041v2.pdf)  
  Keywords: 3d gaussian, outdoor, segmentation, semantic, gaussian splatting, ar  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: 3d gaussian, outdoor, tracking, geometry, slam, gaussian splatting, high-fidelity, mapping, ar  
- **[RadSplatter: Extending 3D Gaussian Splatting to Radio Frequencies for Wireless Radiomap Extrapolation](https://arxiv.org/abs/2502.12686v1)**  
  Authors: Yiheng Wang, Ye Xue, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.12686v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, outdoor, efficient, gaussian splatting, ar  
- **[GS-GVINS: A Tightly-integrated GNSS-Visual-Inertial Navigation System Augmented by 3D Gaussian Splatting](https://arxiv.org/abs/2502.10975v1)**  
  Authors: Zelin Zhou, Saurav Uprety, Shichuang Nie, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10975v1.pdf)  
  Keywords: 3d gaussian, outdoor, motion, tracking, slam, gaussian splatting, ar, dynamic  
- **[PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression](https://arxiv.org/abs/2502.04843v2)**  
  Authors: Feifei Li, Qi Song, Chi Zhang, Hui Shuai, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04843v2.pdf)  
  Keywords: ar, nerf, gaussian splatting, outdoor  
- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: 3d gaussian, outdoor, efficient, gaussian splatting, ar  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: localization, nerf, outdoor, large scene, geometry, slam, gaussian splatting, mapping, ar, dynamic  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, outdoor, motion, ar, dynamic, understanding  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: 3d gaussian, nerf, outdoor, efficient, slam, gaussian splatting, mapping, ar, neural rendering  

### Model Compression

*Showing the latest 50 out of 517 papers*

- **[FlexDrive: Toward Trajectory Flexibility in Driving Scene Reconstruction and Rendering](https://arxiv.org/abs/2502.21093v2)**  
  Authors: Jingqiu Zhou, Lue Fan, Linjiang Huang, Xiaoyu Shi, Si Liu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.21093v2.pdf)  
  Keywords: ar, 3d gaussian, compact, gaussian splatting  
- **[InsTaG: Learning Personalized 3D Talking Head from Few-Second Video](https://arxiv.org/abs/2502.20387v1)**  
  Authors: Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Jun Zhou, Lin Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20387v1.pdf)  
  Keywords: lightweight, motion, head, fast, ar, dynamic  
- **[Efficient Gaussian Splatting for Monocular Dynamic Scene Rendering via Sparse Time-Variant Attribute Modeling](https://arxiv.org/abs/2502.20378v1)**  
  Authors: Hanyang Kong, Xingyi Yang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20378v1.pdf)  
  Keywords: motion, efficient, gaussian splatting, ar, dynamic  
- **[Does 3D Gaussian Splatting Need Accurate Volumetric Rendering?](https://arxiv.org/abs/2502.19318v1)**  
  Authors: Adam Celarek, George Kopanas, George Drettakis, Michael Wimmer, Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19318v1.pdf)  
  Keywords: 3d gaussian, nerf, efficient, gaussian splatting, fast, ar  
- **[Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting](https://arxiv.org/abs/2502.19459v1)**  
  Authors: Yu Liu, Baoxiong Jia, Ruijie Lu, Junfeng Ni, Song-Chun Zhu, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19459v1.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, ar, dynamic  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, real-time rendering, nerf, survey, efficient, gaussian splatting, ar, compression  
- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: 3d reconstruction, 3d gaussian, efficient, gaussian splatting, sparse view, high-fidelity, ar  
- **[GaussianFlowOcc: Sparse and Weakly Supervised Occupancy Estimation using Gaussian Splatting and Temporal Flow](https://arxiv.org/abs/2502.17288v2)**  
  Authors: Simon Boeder, Fabian Gigengack, Benjamin Risse  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17288v2.pdf)  
  Keywords: 3d gaussian, autonomous driving, efficient, gaussian splatting, fast, ar, dynamic  
- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941v1)**  
  Authors: Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16941v1.pdf)  
  Keywords: 4d, nerf, efficient, lighting, ar  
- **[GS-TransUNet: Integrated 2D Gaussian Splatting and Transformer UNet for Accurate Skin Lesion Analysis](https://arxiv.org/abs/2502.16748v1)**  
  Authors: Anand Kumar, Kavinder Roghit Kanthen, Josna John  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16748v1.pdf)  
  Keywords: efficient, segmentation, gaussian splatting, fast, medical, ar  

### Quality Enhancement

*Showing the latest 50 out of 219 papers*

- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: 3d reconstruction, 3d gaussian, efficient, gaussian splatting, sparse view, high-fidelity, ar  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: 3d gaussian, outdoor, tracking, geometry, slam, gaussian splatting, high-fidelity, mapping, ar  
- **[DynamicGSG: Dynamic 3D Gaussian Scene Graphs for Environment Adaptation](https://arxiv.org/abs/2502.15309v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Zhuo Yang, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15309v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GeLuzhou/Dynamic-GSG?style=social)](https://github.com/GeLuzhou/Dynamic-GSG)  
  Keywords: 3d gaussian, segmentation, gaussian splatting, semantic, high-fidelity, ar, dynamic, human  
- **[GS-Cache: A GS-Cache Inference Framework for Large-scale Gaussian Splatting Models](https://arxiv.org/abs/2502.14938v1)**  
  Authors: Miao Tao, Yuanzhen Zhou, Haoran Xu, Zeyu He, Zhenyu Yang, Yuchang Zhang, Zhongling Su, Linning Xu, Zhenxiang Ma, Rong Fu, Hengjie Li, Xingcheng Zhang, Jidong Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14938v1.pdf)  
  Keywords: 3d gaussian, vr, efficient, gaussian splatting, high-fidelity, face, ar, neural rendering  
- **[SIREN: Semantic, Initialization-Free Registration of Multi-Robot Gaussian Splatting Maps](https://arxiv.org/abs/2502.06519v1)**  
  Authors: Ola Shorinwa, Jiankai Sun, Mac Schwager, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.06519v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, semantic, high-fidelity, ar  
- **[PINGS: Gaussian Splatting Meets Distance Fields within a Point-Based Implicit Neural Map](https://arxiv.org/abs/2502.05752v1)**  
  Authors: Yue Pan, Xingguang Zhong, Liren Jin, Louis Wiesmann, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05752v1.pdf)  
  Keywords: compact, slam, gaussian splatting, high-fidelity, mapping, high quality, ar  
- **[Seeing World Dynamics in a Nutshell](https://arxiv.org/abs/2502.03465v1)**  
  Authors: Qiuhong Shen, Xuanyu Yi, Mingbao Lin, Hanwang Zhang, Shuicheng Yan, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.03465v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Nut-World/NutWorld?style=social)](https://github.com/Nut-World/NutWorld)  
  Keywords: 3d gaussian, motion, efficient, high-fidelity, ar, dynamic  
- **[GARAD-SLAM: 3D GAussian splatting for Real-time Anti Dynamic SLAM](https://arxiv.org/abs/2502.03228v2)**  
  Authors: Mingrui Li, Weijian Chen, Na Cheng, Jingyuan Xu, Dong Li, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.03228v2.pdf)  
  Keywords: 3d gaussian, tracking, segmentation, slam, gaussian splatting, high-fidelity, mapping, face, ar, dynamic  
- **[EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](https://arxiv.org/abs/2502.00654v1)**  
  Authors: Junuk Cha, Seongro Yoon, Valeriya Strizhkova, Francois Bremond, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00654v1.pdf)  
  Keywords: 3d gaussian, motion, head, gaussian splatting, high-fidelity, face, ar  
- **[JGHand: Joint-Driven Animatable Hand Avater via 3D Gaussian Splatting](https://arxiv.org/abs/2501.19088v1)**  
  Authors: Zhoutao Sun, Xukun Shen, Yong Hu, Yuyou Zhong, Xueyang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19088v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, gaussian splatting, high-fidelity, shadow, deformation, face, ar, neural rendering, human  

### Ray Tracing

- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, real-time rendering, tracking, geometry, efficient, lighting, ray tracing, face, ar, dynamic, relightable  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: reflection, gaussian splatting, shadow, lighting, ray tracing, face  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, survey, gaussian splatting, ray tracing, ar  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: reflection, acceleration, light transport, efficient, gaussian splatting, ray tracing, ar  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: reflection, 3d gaussian, gaussian splatting, shadow, ray tracing, ar  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: reflection, relighting, efficient, gaussian splatting, lighting, ray tracing, ar  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: 3d gaussian, real-time rendering, reflection, efficient, gaussian splatting, high-fidelity, lighting, ray tracing, ar  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: illumination, nerf, geometry, efficient, gaussian splatting, fast, mapping, face, ar, global illumination  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v2)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v2.pdf)  
  Keywords: 3d gaussian, efficient, gaussian splatting, ray tracing, ar  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: ar, 3d gaussian, ray tracing, gaussian splatting  

### Relighting

*Showing the latest 50 out of 153 papers*

- **[EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering](https://arxiv.org/abs/2502.20669v1)**  
  Authors: John J. Han, Jie Ying Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20669v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, geometry, gaussian splatting, lighting, face, medical, ar  
- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941v1)**  
  Authors: Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16941v1.pdf)  
  Keywords: 4d, nerf, efficient, lighting, ar  
- **[RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection](https://arxiv.org/abs/2502.13071v1)**  
  Authors: Jingtong Yue, Zhiwei Lin, Xin Lin, Xiaoyu Zhou, Xiangtai Li, Lu Qi, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13071v1.pdf)  
  Keywords: ar, 3d gaussian, face, lighting  
- **[OMG: Opacity Matters in Material Modeling with Gaussian Splatting](https://arxiv.org/abs/2502.10988v2)**  
  Authors: Silong Yong, Venkata Nagarjun Pudureddiyur Manivannan, Bernhard Kerbl, Zifu Wan, Simon Stepputtis, Katia Sycara, Yaqi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10988v2.pdf)  
  Keywords: 3d gaussian, real-time rendering, geometry, gaussian splatting, lighting, ar, neural rendering  
- **[E-3DGS: Event-Based Novel View Rendering of Large-Scale Scenes Using 3D Gaussian Splatting](https://arxiv.org/abs/2502.10827v1)**  
  Authors: Sohaib Zahid, Viktor Rudnev, Eddy Ilg, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10827v1.pdf)  
  Keywords: 3d gaussian, nerf, motion, gaussian splatting, fast, lighting, ar, dynamic  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, real-time rendering, tracking, geometry, efficient, lighting, ray tracing, face, ar, dynamic, relightable  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: reflection, gaussian splatting, shadow, lighting, ray tracing, face  
- **[TranSplat: Surface Embedding-guided 3D Gaussian Splatting for Transparent Object Manipulation](https://arxiv.org/abs/2502.07840v1)**  
  Authors: Jeongyun Kim, Jeongho Noh, Dong-Guw Lee, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07840v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://github.)  
  Keywords: 3d gaussian, robotics, gaussian splatting, face, lighting, ar  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: 4d, nerf, motion, survey, gaussian splatting, lighting, deformation, ar, dynamic  
- **[GaussRender: Learning 3D Occupancy with Gaussian Rendering](https://arxiv.org/abs/2502.05040v1)**  
  Authors: Loick Chambon, Eloi Zablocki, Alexandre Boulch, Mickael Chen, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05040v1.pdf) | [![GitHub](https://img.shields.io/github/stars/valeoai/GaussRender?style=social)](https://github.com/valeoai/GaussRender)  
  Keywords: geometry, efficient, gaussian splatting, semantic, lighting, ar, understanding  

### SLAM

*Showing the latest 50 out of 204 papers*

- **[Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration](https://arxiv.org/abs/2502.16652v1)**  
  Authors: Kim Jun-Seong, GeonU Kim, Kim Yu-Ji, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16652v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drsplat.github.io/)  
  Keywords: localization, 3d gaussian, compact, segmentation, gaussian splatting, semantic, ar, understanding  
- **[Dragen3D: Multiview Geometry Consistent 3D Gaussian Generation with Drag-Based Control](https://arxiv.org/abs/2502.16475v1)**  
  Authors: Jinbo Yan, Alan Zhao, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16475v1.pdf)  
  Keywords: 3d gaussian, geometry, efficient, gaussian splatting, mapping, face, ar  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: 3d gaussian, outdoor, tracking, geometry, slam, gaussian splatting, high-fidelity, mapping, ar  
- **[Hier-SLAM++: Neuro-Symbolic Semantic SLAM with a Hierarchically Categorical Gaussian Splatting](https://arxiv.org/abs/2502.14931v1)**  
  Authors: Boying Li, Vuong Chi Hao, Peter J. Stuckey, Ian Reid, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14931v1.pdf)  
  Keywords: 3d gaussian, nerf, compact, slam, gaussian splatting, semantic, mapping, ar, understanding  
- **[3D Gaussian Splatting aided Localization for Large and Complex Indoor-Environments](https://arxiv.org/abs/2502.13803v1)**  
  Authors: Vincent Ress, Jonas Meyer, Wei Zhang, David Skuddis, Uwe Soergel, Norbert Haala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13803v1.pdf)  
  Keywords: localization, 3d gaussian, geometry, slam, gaussian splatting, ar  
- **[High-Dynamic Radar Sequence Prediction for Weather Nowcasting Using Spatiotemporal Coherent Gaussian Representation](https://arxiv.org/abs/2502.14895v1)**  
  Authors: Ziye Wang, Yiran Qin, Lin Zeng, Ruimao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14895v1.pdf)  
  Keywords: 4d, tracking, efficient, gaussian splatting, ar, dynamic  
- **[GS-GVINS: A Tightly-integrated GNSS-Visual-Inertial Navigation System Augmented by 3D Gaussian Splatting](https://arxiv.org/abs/2502.10975v1)**  
  Authors: Zelin Zhou, Saurav Uprety, Shichuang Nie, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10975v1.pdf)  
  Keywords: 3d gaussian, outdoor, motion, tracking, slam, gaussian splatting, ar, dynamic  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: real-time rendering, nerf, tracking, geometry, slam, gaussian splatting, mapping, ar, sparse-view  
- **[BevSplat: Resolving Height Ambiguity via Feature-Based Gaussian Primitives for Weakly-Supervised Cross-View Localization](https://arxiv.org/abs/2502.09080v1)**  
  Authors: Qiwei Wang, Shaoxun Wu, Yujiao Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09080v1.pdf)  
  Keywords: localization, 3d gaussian, ar, semantic  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: 4d, real-time rendering, tracking, geometry, efficient, lighting, ray tracing, face, ar, dynamic, relightable  

### Scene Understanding

*Showing the latest 50 out of 240 papers*

- **[ATLAS Navigator: Active Task-driven LAnguage-embedded Gaussian Splatting](https://arxiv.org/abs/2502.20386v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.20386v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://atlasnav.github.io)  
  Keywords: ar, semantic, gaussian splatting, outdoor  
- **[Open-Vocabulary Semantic Part Segmentation of 3D Human](https://arxiv.org/abs/2502.19782v1)**  
  Authors: Keito Suzuki, Bang Du, Girish Krishnan, Kunyao Chen, Runfa Blark Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19782v1.pdf)  
  Keywords: 3d gaussian, vr, segmentation, gaussian splatting, semantic, ar, human  
- **[OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation](https://arxiv.org/abs/2502.18041v2)**  
  Authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.18041v2.pdf)  
  Keywords: 3d gaussian, outdoor, segmentation, semantic, gaussian splatting, ar  
- **[UniGS: Unified Language-Image-3D Pretraining with Gaussian Splatting](https://arxiv.org/abs/2502.17860v2)**  
  Authors: Haoyuan Li, Yanpeng Zhou, Tao Tang, Jifei Song, Yihan Zeng, Michael Kampffmeyer, Hang Xu, Xiaodan Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17860v2.pdf)  
  Keywords: understanding, 3d gaussian, ar, gaussian splatting  
- **[GS-TransUNet: Integrated 2D Gaussian Splatting and Transformer UNet for Accurate Skin Lesion Analysis](https://arxiv.org/abs/2502.16748v1)**  
  Authors: Anand Kumar, Kavinder Roghit Kanthen, Josna John  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16748v1.pdf)  
  Keywords: efficient, segmentation, gaussian splatting, fast, medical, ar  
- **[Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration](https://arxiv.org/abs/2502.16652v1)**  
  Authors: Kim Jun-Seong, GeonU Kim, Kim Yu-Ji, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16652v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drsplat.github.io/)  
  Keywords: localization, 3d gaussian, compact, segmentation, gaussian splatting, semantic, ar, understanding  
- **[Pointmap Association and Piecewise-Plane Constraint for Consistent and Compact 3D Gaussian Segmentation Field](https://arxiv.org/abs/2502.16303v1)**  
  Authors: Wenhao Hu, Wenhao Chai, Shengyu Hao, Xiaotong Cui, Xuexiang Wen, Jenq-Neng Hwang, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16303v1.pdf)  
  Keywords: 3d gaussian, compact, segmentation, semantic, ar  
- **[DynamicGSG: Dynamic 3D Gaussian Scene Graphs for Environment Adaptation](https://arxiv.org/abs/2502.15309v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Zhuo Yang, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15309v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GeLuzhou/Dynamic-GSG?style=social)](https://github.com/GeLuzhou/Dynamic-GSG)  
  Keywords: 3d gaussian, segmentation, gaussian splatting, semantic, high-fidelity, ar, dynamic, human  
- **[Hier-SLAM++: Neuro-Symbolic Semantic SLAM with a Hierarchically Categorical Gaussian Splatting](https://arxiv.org/abs/2502.14931v1)**  
  Authors: Boying Li, Vuong Chi Hao, Peter J. Stuckey, Ian Reid, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14931v1.pdf)  
  Keywords: 3d gaussian, nerf, compact, slam, gaussian splatting, semantic, mapping, ar, understanding  
- **[OG-Gaussian: Occupancy Based Street Gaussians for Autonomous Driving](https://arxiv.org/abs/2502.14235v1)**  
  Authors: Yedong Shen, Xinran Zhang, Yifan Duan, Shiqi Zhang, Heng Li, Yilong Wu, Jianmin Ji, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14235v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, head, gaussian splatting, semantic, ar, dynamic  



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