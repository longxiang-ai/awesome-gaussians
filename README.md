# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-02-26 00:47:08

## Categories

- [3DGS Surveys](#3dgs-surveys) (22 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (385 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1349 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (450 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (500 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (94 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (443 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (73 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (511 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (219 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (33 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (152 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (204 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (236 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: gaussian splatting, nerf, survey, ar, dynamic, deformation, motion, lighting, 4d  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, survey, ar, ray tracing  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: 3d gaussian, survey, ar, dynamic, outdoor, face, geometry, mapping, localization, lighting, slam, reflection, tracking  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, survey, ar, recognition, illumination  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: gaussian splatting, robotics, nerf, survey, 3d reconstruction, dynamic, semantic, ar, geometry, lighting, autonomous driving, high-fidelity, compact  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, survey, real-time rendering, robotics, ar, understanding  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, survey, ar, lighting, high-fidelity  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, survey, 3d reconstruction, robotics, ar, autonomous driving, vr  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: 3d gaussian, survey, ar  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v2)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, survey, ar, understanding, efficient  

### Acceleration

*Showing the latest 50 out of 385 papers*

- **[GaussianFlowOcc: Sparse and Weakly Supervised Occupancy Estimation using Gaussian Splatting and Temporal Flow](https://arxiv.org/abs/2502.17288v1)**  
  Authors: Simon Boeder, Fabian Gigengack, Benjamin Risse  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17288v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, fast, ar, dynamic, efficient, autonomous driving  
- **[GS-TransUNet: Integrated 2D Gaussian Splatting and Transformer UNet for Accurate Skin Lesion Analysis](https://arxiv.org/abs/2502.16748v1)**  
  Authors: Anand Kumar, Kavinder Roghit Kanthen, Josna John  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16748v1.pdf)  
  Keywords: gaussian splatting, fast, ar, medical, efficient, segmentation  
- **[GS-QA: Comprehensive Quality Assessment Benchmark for Gaussian Splatting View Synthesis](https://arxiv.org/abs/2502.13196v1)**  
  Authors: Pedro Martin, António Rodrigues, João Ascenso, Maria Paula Queluz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13196v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, fast, ar, geometry, human  
- **[GaussianMotion: End-to-End Learning of Animatable Gaussian Avatars with Pose Guidance from Text](https://arxiv.org/abs/2502.11642v1)**  
  Authors: Gyumin Shim, Sangmin Lee, Jaegul Choo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.11642v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient rendering, ar, efficient, face, avatar, motion, human  
- **[OMG: Opacity Matters in Material Modeling with Gaussian Splatting](https://arxiv.org/abs/2502.10988v1)**  
  Authors: Silong Yong, Venkata Nagarjun Pudureddiyur Manivannan, Bernhard Kerbl, Zifu Wan, Simon Stepputtis, Katia Sycara, Yaqi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10988v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, ar, geometry, lighting, neural rendering  
- **[E-3DGS: Event-Based Novel View Rendering of Large-Scale Scenes Using 3D Gaussian Splatting](https://arxiv.org/abs/2502.10827v1)**  
  Authors: Sohaib Zahid, Viktor Rudnev, Eddy Ilg, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10827v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, fast, ar, dynamic, motion, lighting  
- **[Self-Calibrating Gaussian Splatting for Large Field of View Reconstruction](https://arxiv.org/abs/2502.09563v1)**  
  Authors: Youming Deng, Wenqi Xian, Guandao Yang, Leonidas Guibas, Gordon Wetzstein, Steve Marschner, Paul Debevec  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09563v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, fast, ar, efficient  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, nerf, ar, sparse-view, geometry, mapping, slam, tracking  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: real-time rendering, ar, dynamic, tracking, efficient, face, geometry, lighting, 4d, relightable, ray tracing  
- **[Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors](https://arxiv.org/abs/2502.07615v1)**  
  Authors: Lin-Zhuo Chen, Kangjie Liu, Youtian Lin, Siyu Zhu, Zhihao Li, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07615v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/fds)  
  Keywords: gaussian splatting, 3d gaussian, fast, ar, geometry  

### Applications

*Showing the latest 50 out of 1349 papers*

- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: gaussian splatting, 3d gaussian, ar, 3d reconstruction, efficient, sparse view, high-fidelity  
- **[GaussianFlowOcc: Sparse and Weakly Supervised Occupancy Estimation using Gaussian Splatting and Temporal Flow](https://arxiv.org/abs/2502.17288v1)**  
  Authors: Simon Boeder, Fabian Gigengack, Benjamin Risse  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17288v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, fast, ar, dynamic, efficient, autonomous driving  
- **[VR-Pipe: Streamlining Hardware Graphics Pipeline for Volume Rendering](https://arxiv.org/abs/2502.17078v1)**  
  Authors: Junseo Lee, Jaisung Kim, Junyong Park, Jaewoong Sim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17078v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, head, vr  
- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941v1)**  
  Authors: Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16941v1.pdf)  
  Keywords: nerf, ar, efficient, lighting, 4d  
- **[GS-TransUNet: Integrated 2D Gaussian Splatting and Transformer UNet for Accurate Skin Lesion Analysis](https://arxiv.org/abs/2502.16748v1)**  
  Authors: Anand Kumar, Kavinder Roghit Kanthen, Josna John  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16748v1.pdf)  
  Keywords: gaussian splatting, fast, ar, medical, efficient, segmentation  
- **[Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration](https://arxiv.org/abs/2502.16652v1)**  
  Authors: Kim Jun-Seong, GeonU Kim, Kim Yu-Ji, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16652v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drsplat.github.io/)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, understanding, segmentation, localization, compact  
- **[Efficient 4D Gaussian Stream with Low Rank Adaptation](https://arxiv.org/abs/2502.16575v1)**  
  Authors: Zhenhuan Liu, Shuai Liu, Yidong Lu, Yirui Chen, Jie Yang, Wei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16575v1.pdf)  
  Keywords: 3d gaussian, ar, dynamic, deformation, efficient, 4d  
- **[Dragen3D: Multiview Geometry Consistent 3D Gaussian Generation with Drag-Based Control](https://arxiv.org/abs/2502.16475v1)**  
  Authors: Jinbo Yan, Alan Zhao, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16475v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, face, geometry, mapping  
- **[Pointmap Association and Piecewise-Plane Constraint for Consistent and Compact 3D Gaussian Segmentation Field](https://arxiv.org/abs/2502.16303v1)**  
  Authors: Wenhao Hu, Wenhao Chai, Shengyu Hao, Xiaotong Cui, Xuexiang Wen, Jenq-Neng Hwang, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16303v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, segmentation, compact  
- **[Para-Lane: Multi-Lane Dataset Registering Parallel Scans for Benchmarking Novel View Synthesis](https://arxiv.org/abs/2502.15635v2)**  
  Authors: Ziqian Ni, Sicong Du, Zhenghua Hou, Chenming Wu, Sheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15635v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nizqleo.github.io/paralane-dataset/.)  
  Keywords: nerf, ar, autonomous driving  

### Avatar Generation

*Showing the latest 50 out of 450 papers*

- **[VR-Pipe: Streamlining Hardware Graphics Pipeline for Volume Rendering](https://arxiv.org/abs/2502.17078v1)**  
  Authors: Junseo Lee, Jaisung Kim, Junyong Park, Jaewoong Sim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17078v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, head, vr  
- **[Dragen3D: Multiview Geometry Consistent 3D Gaussian Generation with Drag-Based Control](https://arxiv.org/abs/2502.16475v1)**  
  Authors: Jinbo Yan, Alan Zhao, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16475v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, face, geometry, mapping  
- **[DynamicGSG: Dynamic 3D Gaussian Scene Graphs for Environment Adaptation](https://arxiv.org/abs/2502.15309v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Zhuo Yang, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15309v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GeLuzhou/Dynamic-GSG?style=social)](https://github.com/GeLuzhou/Dynamic-GSG)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, dynamic, segmentation, human, high-fidelity  
- **[GS-Cache: A GS-Cache Inference Framework for Large-scale Gaussian Splatting Models](https://arxiv.org/abs/2502.14938v1)**  
  Authors: Miao Tao, Yuanzhen Zhou, Haoran Xu, Zeyu He, Zhenyu Yang, Yuchang Zhang, Zhongling Su, Linning Xu, Zhenxiang Ma, Rong Fu, Hengjie Li, Xingcheng Zhang, Jidong Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14938v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, face, vr, high-fidelity, neural rendering  
- **[OG-Gaussian: Occupancy Based Street Gaussians for Autonomous Driving](https://arxiv.org/abs/2502.14235v1)**  
  Authors: Yedong Shen, Xinran Zhang, Yifan Duan, Shiqi Zhang, Heng Li, Yilong Wu, Jianmin Ji, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14235v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, dynamic, head, autonomous driving  
- **[GlossGau: Efficient Inverse Rendering for Glossy Surface with Anisotropic Spherical Gaussian](https://arxiv.org/abs/2502.14129v1)**  
  Authors: Bang Du, Runfa Blark Li, Chen Du, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14129v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, ar, efficient, face  
- **[Inter3D: A Benchmark and Strong Baseline for Human-Interactive 3D Object Reconstruction](https://arxiv.org/abs/2502.14004v1)**  
  Authors: Gan Chen, Ying He, Mulin Yu, F. Richard Yu, Gang Xu, Fei Ma, Ming Li, Guang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14004v1.pdf)  
  Keywords: gaussian splatting, ar, 3d reconstruction, dynamic, efficient, motion, human, neural rendering  
- **[RAD: Training an End-to-End Driving Policy via Large-Scale 3DGS-based Reinforcement Learning](https://arxiv.org/abs/2502.13144v1)**  
  Authors: Hao Gao, Shaoyu Chen, Bo Jiang, Bencheng Liao, Yiang Shi, Xiaoyang Guo, Yuechuan Pu, Haoran Yin, Xiangyu Li, Xinbang Zhang, Ying Zhang, Wenyu Liu, Qian Zhang, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13144v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hgao-cv.github.io/RAD.)  
  Keywords: ar, face, autonomous driving, human  
- **[GS-QA: Comprehensive Quality Assessment Benchmark for Gaussian Splatting View Synthesis](https://arxiv.org/abs/2502.13196v1)**  
  Authors: Pedro Martin, António Rodrigues, João Ascenso, Maria Paula Queluz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13196v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, fast, ar, geometry, human  
- **[RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection](https://arxiv.org/abs/2502.13071v1)**  
  Authors: Jingtong Yue, Zhiwei Lin, Xin Lin, Xiaoyu Zhou, Xiangtai Li, Lu Qi, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13071v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, face  

### Dynamic Scene

*Showing the latest 50 out of 500 papers*

- **[GaussianFlowOcc: Sparse and Weakly Supervised Occupancy Estimation using Gaussian Splatting and Temporal Flow](https://arxiv.org/abs/2502.17288v1)**  
  Authors: Simon Boeder, Fabian Gigengack, Benjamin Risse  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17288v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, fast, ar, dynamic, efficient, autonomous driving  
- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941v1)**  
  Authors: Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16941v1.pdf)  
  Keywords: nerf, ar, efficient, lighting, 4d  
- **[Efficient 4D Gaussian Stream with Low Rank Adaptation](https://arxiv.org/abs/2502.16575v1)**  
  Authors: Zhenhuan Liu, Shuai Liu, Yidong Lu, Yirui Chen, Jie Yang, Wei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16575v1.pdf)  
  Keywords: 3d gaussian, ar, dynamic, deformation, efficient, 4d  
- **[DynamicGSG: Dynamic 3D Gaussian Scene Graphs for Environment Adaptation](https://arxiv.org/abs/2502.15309v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Zhuo Yang, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15309v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GeLuzhou/Dynamic-GSG?style=social)](https://github.com/GeLuzhou/Dynamic-GSG)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, dynamic, segmentation, human, high-fidelity  
- **[CDGS: Confidence-Aware Depth Regularization for 3D Gaussian Splatting](https://arxiv.org/abs/2502.14684v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Steffen Urban, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14684v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, 3d reconstruction, efficient, motion  
- **[Exploiting Deblurring Networks for Radiance Fields](https://arxiv.org/abs/2502.14454v1)**  
  Authors: Haeyun Choi, Heemin Yang, Janghyeok Han, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14454v1.pdf)  
  Keywords: 3d gaussian, motion, ar  
- **[OG-Gaussian: Occupancy Based Street Gaussians for Autonomous Driving](https://arxiv.org/abs/2502.14235v1)**  
  Authors: Yedong Shen, Xinran Zhang, Yifan Duan, Shiqi Zhang, Heng Li, Yilong Wu, Jianmin Ji, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14235v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, dynamic, head, autonomous driving  
- **[Inter3D: A Benchmark and Strong Baseline for Human-Interactive 3D Object Reconstruction](https://arxiv.org/abs/2502.14004v1)**  
  Authors: Gan Chen, Ying He, Mulin Yu, F. Richard Yu, Gang Xu, Fei Ma, Ming Li, Guang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14004v1.pdf)  
  Keywords: gaussian splatting, ar, 3d reconstruction, dynamic, efficient, motion, human, neural rendering  
- **[High-Dynamic Radar Sequence Prediction for Weather Nowcasting Using Spatiotemporal Coherent Gaussian Representation](https://arxiv.org/abs/2502.14895v1)**  
  Authors: Ziye Wang, Yiran Qin, Lin Zeng, Ruimao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14895v1.pdf)  
  Keywords: gaussian splatting, ar, dynamic, efficient, 4d, tracking  
- **[GaussianMotion: End-to-End Learning of Animatable Gaussian Avatars with Pose Guidance from Text](https://arxiv.org/abs/2502.11642v1)**  
  Authors: Gyumin Shim, Sangmin Lee, Jaegul Choo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.11642v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient rendering, ar, efficient, face, avatar, motion, human  

### Few-shot

*Showing the latest 50 out of 94 papers*

- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: gaussian splatting, 3d gaussian, ar, 3d reconstruction, efficient, sparse view, high-fidelity  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, nerf, ar, sparse-view, geometry, mapping, slam, tracking  
- **[DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform](https://arxiv.org/abs/2501.12637v2)**  
  Authors: Hung Nguyen, Blark Runfa Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.12637v2.pdf)  
  Keywords: fast, nerf, ar, few-shot, head  
- **[See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization](https://arxiv.org/abs/2501.11508v1)**  
  Authors: Zongqi He, Zhe Xiao, Kin-Chung Chan, Yushen Zuo, Jun Xiao, Kin-Man Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11508v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, sparse-view, 4d  
- **[RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering](https://arxiv.org/abs/2501.11102v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Yu Lin, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.11102v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, ar, 3d reconstruction, sparse-view, efficient  
- **[Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes](https://arxiv.org/abs/2501.08072v1)**  
  Authors: Yuhang Zhang, Joshua Maraval, Zhengyu Zhang, Nicolas Ramin, Shishun Tian, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08072v1.pdf)  
  Keywords: gaussian splatting, nerf, ar, dynamic, medical, face, sparse view, lighting, human  
- **[Synthetic Prior for Few-Shot Drivable Head Avatar Inversion](https://arxiv.org/abs/2501.06903v1)**  
  Authors: Wojciech Zielonka, Stephan J. Garbin, Alexandros Lattas, George Kopanas, Paulo Gotardo, Thabo Beeler, Justus Thies, Timo Bolkart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06903v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, few-shot, head, avatar  
- **[NVS-SQA: Exploring Self-Supervised Quality Representation Learning for Neurally Synthesized Scenes without References](https://arxiv.org/abs/2501.06488v1)**  
  Authors: Qiang Qu, Yiran Shen, Xiaoming Chen, Yuk Ying Chung, Weidong Cai, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.06488v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, ar, sparse view, human  
- **[FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency](https://arxiv.org/abs/2501.04628v1)**  
  Authors: Han Huang, Yulun Wu, Chao Deng, Ge Gao, Ming Gu, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.04628v1.pdf)  
  Keywords: gaussian splatting, fast, ar, sparse-view, face, sparse view  
- **[Dust to Tower: Coarse-to-Fine Photo-Realistic Scene Reconstruction from Sparse Uncalibrated Images](https://arxiv.org/abs/2412.19518v1)**  
  Authors: Xudong Cai, Yongcai Wang, Zhaoxin Fan, Deng Haoran, Shuo Wang, Wanting Li, Deying Li, Lun Luo, Minhang Wang, Jintao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19518v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, fast, ar, sparse-view, efficient  

### Geometry Reconstruction

*Showing the latest 50 out of 443 papers*

- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: gaussian splatting, 3d gaussian, ar, 3d reconstruction, efficient, sparse view, high-fidelity  
- **[Dragen3D: Multiview Geometry Consistent 3D Gaussian Generation with Drag-Based Control](https://arxiv.org/abs/2502.16475v1)**  
  Authors: Jinbo Yan, Alan Zhao, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16475v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, face, geometry, mapping  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: gaussian splatting, 3d gaussian, ar, outdoor, geometry, mapping, high-fidelity, slam, tracking  
- **[CDGS: Confidence-Aware Depth Regularization for 3D Gaussian Splatting](https://arxiv.org/abs/2502.14684v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Steffen Urban, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14684v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, 3d reconstruction, efficient, motion  
- **[3D Gaussian Splatting aided Localization for Large and Complex Indoor-Environments](https://arxiv.org/abs/2502.13803v1)**  
  Authors: Vincent Ress, Jonas Meyer, Wei Zhang, David Skuddis, Uwe Soergel, Norbert Haala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13803v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, geometry, localization, slam  
- **[Inter3D: A Benchmark and Strong Baseline for Human-Interactive 3D Object Reconstruction](https://arxiv.org/abs/2502.14004v1)**  
  Authors: Gan Chen, Ying He, Mulin Yu, F. Richard Yu, Gang Xu, Fei Ma, Ming Li, Guang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14004v1.pdf)  
  Keywords: gaussian splatting, ar, 3d reconstruction, dynamic, efficient, motion, human, neural rendering  
- **[GS-QA: Comprehensive Quality Assessment Benchmark for Gaussian Splatting View Synthesis](https://arxiv.org/abs/2502.13196v1)**  
  Authors: Pedro Martin, António Rodrigues, João Ascenso, Maria Paula Queluz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13196v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, fast, ar, geometry, human  
- **[PUGS: Zero-shot Physical Understanding with Gaussian Splatting](https://arxiv.org/abs/2502.12231v1)**  
  Authors: Yinghao Shuai, Ran Yu, Yuantao Chen, Zijian Jiang, Xiaowei Song, Nan Wang, Jv Zheng, Jianzhu Ma, Meng Yang, Zhicheng Wang, Wenbo Ding, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.12231v1.pdf) | [![GitHub](https://img.shields.io/github/stars/EverNorif/PUGS?style=social)](https://github.com/EverNorif/PUGS)  
  Keywords: gaussian splatting, ar, geometry, understanding  
- **[3D Gaussian Inpainting with Depth-Guided Cross-View Consistency](https://arxiv.org/abs/2502.11801v1)**  
  Authors: Sheng-Yu Huang, Zi-Ting Chou, Yu-Chiang Frank Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.11801v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, ar, geometry  
- **[OMG: Opacity Matters in Material Modeling with Gaussian Splatting](https://arxiv.org/abs/2502.10988v1)**  
  Authors: Silong Yong, Venkata Nagarjun Pudureddiyur Manivannan, Bernhard Kerbl, Zifu Wan, Simon Stepputtis, Katia Sycara, Yaqi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10988v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, ar, geometry, lighting, neural rendering  

### Large Scene

*Showing the latest 50 out of 73 papers*

- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: gaussian splatting, 3d gaussian, ar, outdoor, geometry, mapping, high-fidelity, slam, tracking  
- **[RadSplatter: Extending 3D Gaussian Splatting to Radio Frequencies for Wireless Radiomap Extrapolation](https://arxiv.org/abs/2502.12686v1)**  
  Authors: Yiheng Wang, Ye Xue, Shutao Zhang, Tsung-Hui Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.12686v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, outdoor, efficient, autonomous driving  
- **[GS-GVINS: A Tightly-integrated GNSS-Visual-Inertial Navigation System Augmented by 3D Gaussian Splatting](https://arxiv.org/abs/2502.10975v1)**  
  Authors: Zelin Zhou, Saurav Uprety, Shichuang Nie, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10975v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, dynamic, outdoor, motion, slam, tracking  
- **[PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression](https://arxiv.org/abs/2502.04843v2)**  
  Authors: Feifei Li, Qi Song, Chi Zhang, Hui Shuai, Rui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.04843v2.pdf)  
  Keywords: gaussian splatting, nerf, ar, outdoor  
- **[Sketch and Patch: Efficient 3D Gaussian Representation for Man-Made Scenes](https://arxiv.org/abs/2501.13045v1)**  
  Authors: Yuang Shi, Simone Gasparini, Géraldine Morin, Chenggang Yang, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.13045v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, outdoor, efficient  
- **[VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes](https://arxiv.org/abs/2501.08286v1)**  
  Authors: Ke Wu, Zicheng Zhang, Muer Tie, Ziqing Ai, Zhongxue Gan, Wenchao Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.08286v1.pdf)  
  Keywords: gaussian splatting, nerf, ar, dynamic, outdoor, large scene, geometry, mapping, localization, slam  
- **[STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes](https://arxiv.org/abs/2501.00602v1)**  
  Authors: Jiawei Yang, Jiahui Huang, Yuxiao Chen, Yan Wang, Boyi Li, Yurong You, Apoorva Sharma, Maximilian Igl, Peter Karkus, Danfei Xu, Boris Ivanovic, Yue Wang, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.00602v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, ar, dynamic, outdoor, understanding, motion  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, ar, outdoor, efficient, mapping, neural rendering, slam  
- **[WeatherGS: 3D Scene Reconstruction in Adverse Weather Conditions via Gaussian Splatting](https://arxiv.org/abs/2412.18862v3)**  
  Authors: Chenghao Qian, Yuhu Guo, Wenjing Li, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.18862v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/weather-gs.)  
  Keywords: gaussian splatting, 3d gaussian, ar, 3d reconstruction, outdoor  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: gaussian splatting, 3d gaussian, nerf, fast, ar, compression, large scene, face, high-fidelity  

### Model Compression

*Showing the latest 50 out of 511 papers*

- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: gaussian splatting, 3d gaussian, ar, 3d reconstruction, efficient, sparse view, high-fidelity  
- **[GaussianFlowOcc: Sparse and Weakly Supervised Occupancy Estimation using Gaussian Splatting and Temporal Flow](https://arxiv.org/abs/2502.17288v1)**  
  Authors: Simon Boeder, Fabian Gigengack, Benjamin Risse  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17288v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, fast, ar, dynamic, efficient, autonomous driving  
- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941v1)**  
  Authors: Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16941v1.pdf)  
  Keywords: nerf, ar, efficient, lighting, 4d  
- **[GS-TransUNet: Integrated 2D Gaussian Splatting and Transformer UNet for Accurate Skin Lesion Analysis](https://arxiv.org/abs/2502.16748v1)**  
  Authors: Anand Kumar, Kavinder Roghit Kanthen, Josna John  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16748v1.pdf)  
  Keywords: gaussian splatting, fast, ar, medical, efficient, segmentation  
- **[Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration](https://arxiv.org/abs/2502.16652v1)**  
  Authors: Kim Jun-Seong, GeonU Kim, Kim Yu-Ji, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16652v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drsplat.github.io/)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, understanding, segmentation, localization, compact  
- **[Efficient 4D Gaussian Stream with Low Rank Adaptation](https://arxiv.org/abs/2502.16575v1)**  
  Authors: Zhenhuan Liu, Shuai Liu, Yidong Lu, Yirui Chen, Jie Yang, Wei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16575v1.pdf)  
  Keywords: 3d gaussian, ar, dynamic, deformation, efficient, 4d  
- **[Dragen3D: Multiview Geometry Consistent 3D Gaussian Generation with Drag-Based Control](https://arxiv.org/abs/2502.16475v1)**  
  Authors: Jinbo Yan, Alan Zhao, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16475v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, face, geometry, mapping  
- **[Pointmap Association and Piecewise-Plane Constraint for Consistent and Compact 3D Gaussian Segmentation Field](https://arxiv.org/abs/2502.16303v1)**  
  Authors: Wenhao Hu, Wenhao Chai, Shengyu Hao, Xiaotong Cui, Xuexiang Wen, Jenq-Neng Hwang, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16303v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, segmentation, compact  
- **[CDGS: Confidence-Aware Depth Regularization for 3D Gaussian Splatting](https://arxiv.org/abs/2502.14684v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Steffen Urban, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14684v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, 3d reconstruction, efficient, motion  
- **[GS-Cache: A GS-Cache Inference Framework for Large-scale Gaussian Splatting Models](https://arxiv.org/abs/2502.14938v1)**  
  Authors: Miao Tao, Yuanzhen Zhou, Haoran Xu, Zeyu He, Zhenyu Yang, Yuchang Zhang, Zhongling Su, Linning Xu, Zhenxiang Ma, Rong Fu, Hengjie Li, Xingcheng Zhang, Jidong Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14938v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, face, vr, high-fidelity, neural rendering  

### Quality Enhancement

*Showing the latest 50 out of 219 papers*

- **[Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting](https://arxiv.org/abs/2502.17377v1)**  
  Authors: Chong Cheng, Gaochao Song, Yiyang Yao, Qinzheng Zhou, Gangjian Zhang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.17377v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/graphgs.)  
  Keywords: gaussian splatting, 3d gaussian, ar, 3d reconstruction, efficient, sparse view, high-fidelity  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: gaussian splatting, 3d gaussian, ar, outdoor, geometry, mapping, high-fidelity, slam, tracking  
- **[DynamicGSG: Dynamic 3D Gaussian Scene Graphs for Environment Adaptation](https://arxiv.org/abs/2502.15309v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Zhuo Yang, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15309v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GeLuzhou/Dynamic-GSG?style=social)](https://github.com/GeLuzhou/Dynamic-GSG)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, dynamic, segmentation, human, high-fidelity  
- **[GS-Cache: A GS-Cache Inference Framework for Large-scale Gaussian Splatting Models](https://arxiv.org/abs/2502.14938v1)**  
  Authors: Miao Tao, Yuanzhen Zhou, Haoran Xu, Zeyu He, Zhenyu Yang, Yuchang Zhang, Zhongling Su, Linning Xu, Zhenxiang Ma, Rong Fu, Hengjie Li, Xingcheng Zhang, Jidong Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14938v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, face, vr, high-fidelity, neural rendering  
- **[SIREN: Semantic, Initialization-Free Registration of Multi-Robot Gaussian Splatting Maps](https://arxiv.org/abs/2502.06519v1)**  
  Authors: Ola Shorinwa, Jiankai Sun, Mac Schwager, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.06519v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, high-fidelity  
- **[PINGS: Gaussian Splatting Meets Distance Fields within a Point-Based Implicit Neural Map](https://arxiv.org/abs/2502.05752v1)**  
  Authors: Yue Pan, Xingguang Zhong, Liren Jin, Louis Wiesmann, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05752v1.pdf)  
  Keywords: gaussian splatting, ar, mapping, high-fidelity, slam, high quality, compact  
- **[Seeing World Dynamics in a Nutshell](https://arxiv.org/abs/2502.03465v1)**  
  Authors: Qiuhong Shen, Xuanyu Yi, Mingbao Lin, Hanwang Zhang, Shuicheng Yan, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.03465v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Nut-World/NutWorld?style=social)](https://github.com/Nut-World/NutWorld)  
  Keywords: 3d gaussian, ar, dynamic, efficient, motion, high-fidelity  
- **[GARAD-SLAM: 3D GAussian splatting for Real-time Anti Dynamic SLAM](https://arxiv.org/abs/2502.03228v2)**  
  Authors: Mingrui Li, Weijian Chen, Na Cheng, Jingyuan Xu, Dong Li, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.03228v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, dynamic, face, mapping, segmentation, high-fidelity, slam, tracking  
- **[EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](https://arxiv.org/abs/2502.00654v1)**  
  Authors: Junuk Cha, Seongro Yoon, Valeriya Strizhkova, Francois Bremond, Seungryul Baek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.00654v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, face, head, motion, high-fidelity  
- **[JGHand: Joint-Driven Animatable Hand Avater via 3D Gaussian Splatting](https://arxiv.org/abs/2501.19088v1)**  
  Authors: Zhoutao Sun, Xukun Shen, Yong Hu, Yuyou Zhong, Xueyang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19088v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, ar, deformation, face, shadow, human, high-fidelity, neural rendering  

### Ray Tracing

- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: real-time rendering, ar, dynamic, tracking, efficient, face, geometry, lighting, 4d, relightable, ray tracing  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: gaussian splatting, face, shadow, lighting, reflection, ray tracing  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, survey, ar, ray tracing  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: gaussian splatting, acceleration, ar, efficient, reflection, light transport, ray tracing  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, shadow, reflection, ray tracing  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: gaussian splatting, ar, efficient, relighting, lighting, reflection, ray tracing  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, ar, efficient, lighting, high-fidelity, reflection, ray tracing  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: gaussian splatting, fast, nerf, global illumination, ar, efficient, face, geometry, mapping, illumination  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v2)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, ray tracing  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v2)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SunLab-UGA/RF-3DGS?style=social)](https://github.com/SunLab-UGA/RF-3DGS)  
  Keywords: gaussian splatting, 3d gaussian, ar, ray tracing  

### Relighting

*Showing the latest 50 out of 152 papers*

- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941v1)**  
  Authors: Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16941v1.pdf)  
  Keywords: nerf, ar, efficient, lighting, 4d  
- **[RobuRCDet: Enhancing Robustness of Radar-Camera Fusion in Bird's Eye View for 3D Object Detection](https://arxiv.org/abs/2502.13071v1)**  
  Authors: Jingtong Yue, Zhiwei Lin, Xin Lin, Xiaoyu Zhou, Xiangtai Li, Lu Qi, Yongtao Wang, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13071v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, face  
- **[OMG: Opacity Matters in Material Modeling with Gaussian Splatting](https://arxiv.org/abs/2502.10988v1)**  
  Authors: Silong Yong, Venkata Nagarjun Pudureddiyur Manivannan, Bernhard Kerbl, Zifu Wan, Simon Stepputtis, Katia Sycara, Yaqi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10988v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, real-time rendering, ar, geometry, lighting, neural rendering  
- **[E-3DGS: Event-Based Novel View Rendering of Large-Scale Scenes Using 3D Gaussian Splatting](https://arxiv.org/abs/2502.10827v1)**  
  Authors: Sohaib Zahid, Viktor Rudnev, Eddy Ilg, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10827v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, fast, ar, dynamic, motion, lighting  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: real-time rendering, ar, dynamic, tracking, efficient, face, geometry, lighting, 4d, relightable, ray tracing  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: gaussian splatting, face, shadow, lighting, reflection, ray tracing  
- **[TranSplat: Surface Embedding-guided 3D Gaussian Splatting for Transparent Object Manipulation](https://arxiv.org/abs/2502.07840v1)**  
  Authors: Jeongyun Kim, Jeongho Noh, Dong-Guw Lee, Ayoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07840v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://github.)  
  Keywords: gaussian splatting, 3d gaussian, robotics, ar, face, lighting  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: gaussian splatting, nerf, survey, ar, dynamic, deformation, motion, lighting, 4d  
- **[GaussRender: Learning 3D Occupancy with Gaussian Rendering](https://arxiv.org/abs/2502.05040v1)**  
  Authors: Loick Chambon, Eloi Zablocki, Alexandre Boulch, Mickael Chen, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.05040v1.pdf) | [![GitHub](https://img.shields.io/github/stars/valeoai/GaussRender?style=social)](https://github.com/valeoai/GaussRender)  
  Keywords: gaussian splatting, semantic, ar, understanding, efficient, geometry, lighting  
- **[VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion](https://arxiv.org/abs/2502.01536v1)**  
  Authors: Shaoting Zhu, Linzhan Mou, Derun Li, Baijun Ye, Runhan Huang, Hang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01536v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, geometry, motion, lighting, vr, tracking  

### SLAM

*Showing the latest 50 out of 204 papers*

- **[Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration](https://arxiv.org/abs/2502.16652v1)**  
  Authors: Kim Jun-Seong, GeonU Kim, Kim Yu-Ji, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16652v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drsplat.github.io/)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, understanding, segmentation, localization, compact  
- **[Dragen3D: Multiview Geometry Consistent 3D Gaussian Generation with Drag-Based Control](https://arxiv.org/abs/2502.16475v1)**  
  Authors: Jinbo Yan, Alan Zhao, Yixin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16475v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, efficient, face, geometry, mapping  
- **[RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes](https://arxiv.org/abs/2502.15633v1)**  
  Authors: Sicheng Yu, Chong Cheng, Yifan Zhou, Xiaojun Yang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15633v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dagentworld.github.io/opengs-slam/)  
  Keywords: gaussian splatting, 3d gaussian, ar, outdoor, geometry, mapping, high-fidelity, slam, tracking  
- **[Hier-SLAM++: Neuro-Symbolic Semantic SLAM with a Hierarchically Categorical Gaussian Splatting](https://arxiv.org/abs/2502.14931v1)**  
  Authors: Boying Li, Vuong Chi Hao, Peter J. Stuckey, Ian Reid, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14931v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, semantic, ar, understanding, mapping, slam, compact  
- **[3D Gaussian Splatting aided Localization for Large and Complex Indoor-Environments](https://arxiv.org/abs/2502.13803v1)**  
  Authors: Vincent Ress, Jonas Meyer, Wei Zhang, David Skuddis, Uwe Soergel, Norbert Haala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.13803v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, geometry, localization, slam  
- **[High-Dynamic Radar Sequence Prediction for Weather Nowcasting Using Spatiotemporal Coherent Gaussian Representation](https://arxiv.org/abs/2502.14895v1)**  
  Authors: Ziye Wang, Yiran Qin, Lin Zeng, Ruimao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14895v1.pdf)  
  Keywords: gaussian splatting, ar, dynamic, efficient, 4d, tracking  
- **[GS-GVINS: A Tightly-integrated GNSS-Visual-Inertial Navigation System Augmented by 3D Gaussian Splatting](https://arxiv.org/abs/2502.10975v1)**  
  Authors: Zelin Zhou, Saurav Uprety, Shichuang Nie, Hongzhou Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.10975v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, dynamic, outdoor, motion, slam, tracking  
- **[DenseSplat: Densifying Gaussian Splatting SLAM with Neural Radiance Prior](https://arxiv.org/abs/2502.09111v1)**  
  Authors: Mingrui Li, Shuhong Liu, Tianchen Deng, Hongyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09111v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, nerf, ar, sparse-view, geometry, mapping, slam, tracking  
- **[BevSplat: Resolving Height Ambiguity via Feature-Based Gaussian Primitives for Weakly-Supervised Cross-View Localization](https://arxiv.org/abs/2502.09080v1)**  
  Authors: Qiwei Wang, Shaoxun Wu, Yujiao Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09080v1.pdf)  
  Keywords: 3d gaussian, localization, semantic, ar  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: real-time rendering, ar, dynamic, tracking, efficient, face, geometry, lighting, 4d, relightable, ray tracing  

### Scene Understanding

*Showing the latest 50 out of 236 papers*

- **[GS-TransUNet: Integrated 2D Gaussian Splatting and Transformer UNet for Accurate Skin Lesion Analysis](https://arxiv.org/abs/2502.16748v1)**  
  Authors: Anand Kumar, Kavinder Roghit Kanthen, Josna John  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16748v1.pdf)  
  Keywords: gaussian splatting, fast, ar, medical, efficient, segmentation  
- **[Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration](https://arxiv.org/abs/2502.16652v1)**  
  Authors: Kim Jun-Seong, GeonU Kim, Kim Yu-Ji, Yu-Chiang Frank Wang, Jaesung Choe, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16652v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://drsplat.github.io/)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, understanding, segmentation, localization, compact  
- **[Pointmap Association and Piecewise-Plane Constraint for Consistent and Compact 3D Gaussian Segmentation Field](https://arxiv.org/abs/2502.16303v1)**  
  Authors: Wenhao Hu, Wenhao Chai, Shengyu Hao, Xiaotong Cui, Xuexiang Wen, Jenq-Neng Hwang, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.16303v1.pdf)  
  Keywords: 3d gaussian, semantic, ar, segmentation, compact  
- **[DynamicGSG: Dynamic 3D Gaussian Scene Graphs for Environment Adaptation](https://arxiv.org/abs/2502.15309v2)**  
  Authors: Luzhou Ge, Xiangyu Zhu, Zhuo Yang, Xuesong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.15309v2.pdf) | [![GitHub](https://img.shields.io/github/stars/GeLuzhou/Dynamic-GSG?style=social)](https://github.com/GeLuzhou/Dynamic-GSG)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, dynamic, segmentation, human, high-fidelity  
- **[Hier-SLAM++: Neuro-Symbolic Semantic SLAM with a Hierarchically Categorical Gaussian Splatting](https://arxiv.org/abs/2502.14931v1)**  
  Authors: Boying Li, Vuong Chi Hao, Peter J. Stuckey, Ian Reid, Hamid Rezatofighi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14931v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, nerf, semantic, ar, understanding, mapping, slam, compact  
- **[OG-Gaussian: Occupancy Based Street Gaussians for Autonomous Driving](https://arxiv.org/abs/2502.14235v1)**  
  Authors: Yedong Shen, Xinran Zhang, Yifan Duan, Shiqi Zhang, Heng Li, Yilong Wu, Jianmin Ji, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.14235v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, dynamic, head, autonomous driving  
- **[PUGS: Zero-shot Physical Understanding with Gaussian Splatting](https://arxiv.org/abs/2502.12231v1)**  
  Authors: Yinghao Shuai, Ran Yu, Yuantao Chen, Zijian Jiang, Xiaowei Song, Nan Wang, Jv Zheng, Jianzhu Ma, Meng Yang, Zhicheng Wang, Wenbo Ding, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.12231v1.pdf) | [![GitHub](https://img.shields.io/github/stars/EverNorif/PUGS?style=social)](https://github.com/EverNorif/PUGS)  
  Keywords: gaussian splatting, ar, geometry, understanding  
- **[BevSplat: Resolving Height Ambiguity via Feature-Based Gaussian Primitives for Weakly-Supervised Cross-View Localization](https://arxiv.org/abs/2502.09080v1)**  
  Authors: Qiwei Wang, Shaoxun Wu, Yujiao Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.09080v1.pdf)  
  Keywords: 3d gaussian, localization, semantic, ar  
- **[Interactive Holographic Visualization for 3D Facial Avatar](https://arxiv.org/abs/2502.08085v1)**  
  Authors: Tri Tung Nguyen Nguyen, Fujii Yasuyuki, Dinh Tuan Tran, Joo-Ho Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08085v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, dynamic, medical, efficient, recognition, avatar, human  
- **[SIREN: Semantic, Initialization-Free Registration of Multi-Robot Gaussian Splatting Maps](https://arxiv.org/abs/2502.06519v1)**  
  Authors: Ola Shorinwa, Jiankai Sun, Mac Schwager, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.06519v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, semantic, ar, high-fidelity  



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