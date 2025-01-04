# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-01-04 00:45:08

## Categories

- [3DGS Surveys](#3dgs-surveys) (20 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (352 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1195 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (398 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (438 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (85 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (400 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (66 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (438 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (199 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (28 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (135 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (172 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (206 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: geometry, outdoor, localization, slam, tracking, lighting, mapping, dynamic, reflection, ar, survey, 3d gaussian, face  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: gaussian splatting, recognition, illumination, ar, survey, 3d gaussian  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: geometry, gaussian splatting, compact, semantic, autonomous driving, 3d reconstruction, robotics, nerf, lighting, ar, dynamic, survey, high-fidelity  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v2)**  
  Authors: Siting Zhu, Guangming Wang, Xin Kong, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v2.pdf)  
  Keywords: gaussian splatting, real-time rendering, robotics, nerf, ar, understanding, survey, 3d gaussian  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: gaussian splatting, nerf, lighting, ar, survey, 3d gaussian, high-fidelity  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v2)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v2.pdf)  
  Keywords: gaussian splatting, autonomous driving, 3d reconstruction, robotics, nerf, ar, vr, survey, 3d gaussian  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: survey, ar, 3d gaussian  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v2)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v2.pdf)  
  Keywords: gaussian splatting, real-time rendering, efficient, ar, understanding, survey, 3d gaussian  
- **[Survey on Fundamental Deep Learning 3D Reconstruction Techniques](https://arxiv.org/abs/2407.08137v1)**  
  Authors: Yonge Bai, LikHang Wong, TszYin Twan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.08137v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, nerf, lighting, ar, survey, 3d gaussian  
- **[Panopticon: a telescope for our times](https://arxiv.org/abs/2407.05103v2)**  
  Authors: Will Saunders, Timothy Chin, Michael Goodwin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05103v2.pdf)  
  Keywords: survey, ar  

### Acceleration

*Showing the latest 50 out of 352 papers*

- **[KeyGS: A Keyframe-Centric Gaussian Splatting Method for Monocular Image Sequences](https://arxiv.org/abs/2412.20767v1)**  
  Authors: Keng-Wei Chang, Zi-Ming Wang, Shang-Hong Lai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20767v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, efficient, ar, 3d gaussian, motion  
- **[4D Gaussian Splatting: Modeling Dynamic Scenes with Native 4D Primitives](https://arxiv.org/abs/2412.20720v1)**  
  Authors: Zeyu Yang, Zijie Pan, Xiatian Zhu, Li Zhang, Yu-Gang Jiang, Philip H. S. Torr  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20720v1.pdf)  
  Keywords: geometry, gaussian splatting, real-time rendering, compact, 4d, ar, dynamic, understanding, vr, motion  
- **[MaskGaussian: Adaptive 3D Gaussian Representation from Probabilistic Masks](https://arxiv.org/abs/2412.20522v1)**  
  Authors: Yifei Liu, Zhihang Zhong, Yifan Zhan, Sheng Xu, Xiao Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20522v1.pdf) | [![GitHub](https://img.shields.io/github/stars/kaikai23/MaskGaussian?style=social)](https://github.com/kaikai23/MaskGaussian)  
  Keywords: gaussian splatting, real-time rendering, ar, dynamic, 3d gaussian  
- **[Dust to Tower: Coarse-to-Fine Photo-Realistic Scene Reconstruction from Sparse Uncalibrated Images](https://arxiv.org/abs/2412.19518v1)**  
  Authors: Xudong Cai, Yongcai Wang, Zhaoxin Fan, Deng Haoran, Shuo Wang, Wanting Li, Deying Li, Lun Luo, Minhang Wang, Jintao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19518v1.pdf)  
  Keywords: fast, gaussian splatting, efficient, ar, sparse-view, 3d gaussian  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: fast, gaussian splatting, large scene, nerf, ar, compression, 3d gaussian, high-fidelity, face  
- **[GeoTexDensifier: Geometry-Texture-Aware Densification for High-Quality Photorealistic 3D Gaussian Splatting](https://arxiv.org/abs/2412.16809v1)**  
  Authors: Hanqing Jiang, Xiaojun Xiang, Han Sun, Hongjie Li, Liyang Zhou, Xiaoyu Zhang, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.16809v1.pdf)  
  Keywords: geometry, gaussian splatting, efficient, ar, vr, 3d gaussian, face, efficient rendering  
- **[OmniSplat: Taming Feed-Forward 3D Gaussian Splatting for Omnidirectional Images with Editable Capabilities](https://arxiv.org/abs/2412.16604v1)**  
  Authors: Suyoung Lee, Jaeyoung Chung, Kihoon Kim, Jaeyoo Huh, Gunhee Lee, Minsoo Lee, Kyoung Mu Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.16604v1.pdf)  
  Keywords: fast, gaussian splatting, ar, segmentation, 3d gaussian  
- **[EGSRAL: An Enhanced 3D Gaussian Splatting based Renderer with Automated Labeling for Large-Scale Driving Scene](https://arxiv.org/abs/2412.15550v1)**  
  Authors: Yixiong Huo, Guangfeng Jiang, Hongyang Wei, Ji Liu, Song Zhang, Han Liu, Xingliang Huang, Mingjie Lu, Jinzhang Peng, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15550v1.pdf) | [![GitHub](https://img.shields.io/github/stars/jiangxb98/EGSRAL?style=social)](https://github.com/jiangxb98/EGSRAL)  
  Keywords: fast, gaussian splatting, ar, dynamic, 3d gaussian  
- **[LiHi-GS: LiDAR-Supervised Gaussian Splatting for Highway Driving Scene Reconstruction](https://arxiv.org/abs/2412.15447v2)**  
  Authors: Pou-Chun Kung, Xianling Zhang, Katherine A. Skinner, Nikita Jaipuria  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15447v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/lihi_gs)  
  Keywords: fast, gaussian splatting, autonomous driving, nerf, ar, dynamic, urban scene, 3d gaussian  
- **[GAGS: Granularity-Aware Feature Distillation for Language Gaussian Splatting](https://arxiv.org/abs/2412.13654v1)**  
  Authors: Yuning Peng, Haiping Wang, Yuan Liu, Chenglu Wen, Zhen Dong, Bisheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13654v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pz0826.github.io/GAGS-Webpage/)  
  Keywords: fast, gaussian splatting, semantic, ar, understanding, segmentation, 3d gaussian  

### Applications

*Showing the latest 50 out of 1195 papers*

- **[PERSE: Personalized 3D Generative Avatars from A Single Portrait](https://arxiv.org/abs/2412.21206v1)**  
  Authors: Hyunsoo Cha, Inhee Lee, Hanbyul Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.21206v1.pdf)  
  Keywords: gaussian splatting, avatar, ar, 3d gaussian, face  
- **[Prometheus: 3D-Aware Latent Diffusion Models for Feed-Forward Text-to-3D Scene Generation](https://arxiv.org/abs/2412.21117v2)**  
  Authors: Yuanbo Yang, Jiahao Shao, Xinyang Li, Yujun Shen, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.21117v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://freemty.github.io/project-prometheus/)  
  Keywords: geometry, efficient, 3d gaussian, ar  
- **[KeyGS: A Keyframe-Centric Gaussian Splatting Method for Monocular Image Sequences](https://arxiv.org/abs/2412.20767v1)**  
  Authors: Keng-Wei Chang, Zi-Ming Wang, Shang-Hong Lai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20767v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, efficient, ar, 3d gaussian, motion  
- **[4D Gaussian Splatting: Modeling Dynamic Scenes with Native 4D Primitives](https://arxiv.org/abs/2412.20720v1)**  
  Authors: Zeyu Yang, Zijie Pan, Xiatian Zhu, Li Zhang, Yu-Gang Jiang, Philip H. S. Torr  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20720v1.pdf)  
  Keywords: geometry, gaussian splatting, real-time rendering, compact, 4d, ar, dynamic, understanding, vr, motion  
- **[MaskGaussian: Adaptive 3D Gaussian Representation from Probabilistic Masks](https://arxiv.org/abs/2412.20522v1)**  
  Authors: Yifei Liu, Zhihang Zhong, Yifan Zhan, Sheng Xu, Xiao Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20522v1.pdf) | [![GitHub](https://img.shields.io/github/stars/kaikai23/MaskGaussian?style=social)](https://github.com/kaikai23/MaskGaussian)  
  Keywords: gaussian splatting, real-time rendering, ar, dynamic, 3d gaussian  
- **[DEGSTalk: Decomposed Per-Embedding Gaussian Fields for Hair-Preserving Talking Face Synthesis](https://arxiv.org/abs/2412.20148v1)**  
  Authors: Kaijun Deng, Dezhi Zheng, Jindong Xie, Jinbao Wang, Weicheng Xie, Linlin Shen, Siyang Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20148v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CVI-SZU/DEGSTalk?style=social)](https://github.com/CVI-SZU/DEGSTalk)  
  Keywords: gaussian splatting, efficient, ar, dynamic, 3d gaussian, face, motion  
- **[GSplatLoc: Ultra-Precise Camera Localization via 3D Gaussian Splatting](https://arxiv.org/abs/2412.20056v1)**  
  Authors: Atticus J. Zeller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20056v1.pdf)  
  Keywords: gaussian splatting, localization, robotics, mapping, ar, 3d gaussian, motion  
- **[DAS3R: Dynamics-Aware Gaussian Splatting for Static Scene Reconstruction](https://arxiv.org/abs/2412.19584v1)**  
  Authors: Kai Xu, Tze Ho Elden Tse, Jizong Peng, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19584v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kai422.github.io/DAS3R/})  
  Keywords: gaussian splatting, slam, ar, dynamic, motion  
- **[Dust to Tower: Coarse-to-Fine Photo-Realistic Scene Reconstruction from Sparse Uncalibrated Images](https://arxiv.org/abs/2412.19518v1)**  
  Authors: Xudong Cai, Yongcai Wang, Zhaoxin Fan, Deng Haoran, Shuo Wang, Wanting Li, Deying Li, Lun Luo, Minhang Wang, Jintao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19518v1.pdf)  
  Keywords: fast, gaussian splatting, efficient, ar, sparse-view, 3d gaussian  
- **[Learning Radiance Fields from a Single Snapshot Compressive Image](https://arxiv.org/abs/2412.19483v1)**  
  Authors: Yunhao Li, Xiang Liu, Xiaodong Wang, Xin Yuan, Peidong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19483v1.pdf)  
  Keywords: nerf, gaussian splatting, 3d gaussian, ar  

### Avatar Generation

*Showing the latest 50 out of 398 papers*

- **[PERSE: Personalized 3D Generative Avatars from A Single Portrait](https://arxiv.org/abs/2412.21206v1)**  
  Authors: Hyunsoo Cha, Inhee Lee, Hanbyul Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.21206v1.pdf)  
  Keywords: gaussian splatting, avatar, ar, 3d gaussian, face  
- **[DEGSTalk: Decomposed Per-Embedding Gaussian Fields for Hair-Preserving Talking Face Synthesis](https://arxiv.org/abs/2412.20148v1)**  
  Authors: Kaijun Deng, Dezhi Zheng, Jindong Xie, Jinbao Wang, Weicheng Xie, Linlin Shen, Siyang Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20148v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CVI-SZU/DEGSTalk?style=social)](https://github.com/CVI-SZU/DEGSTalk)  
  Keywords: gaussian splatting, efficient, ar, dynamic, 3d gaussian, face, motion  
- **[Generating Editable Head Avatars with 3D Gaussian GANs](https://arxiv.org/abs/2412.19149v1)**  
  Authors: Guohao Li, Hongyu Yang, Yifang Men, Di Huang, Weixin Li, Ruijie Yang, Yunhong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19149v1.pdf) | [![GitHub](https://img.shields.io/github/stars/liguohao96/EGG3D?style=social)](https://github.com/liguohao96/EGG3D)  
  Keywords: gaussian splatting, animation, illumination, nerf, deformation, avatar, ar, 3d gaussian, head, face  
- **[FaceLift: Single Image to 3D Head with View Generation and GS-LRM](https://arxiv.org/abs/2412.17812v1)**  
  Authors: Weijie Lyu, Yi Zhou, Ming-Hsuan Yang, Zhixin Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17812v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weijielyu.github.io/FaceLift.)  
  Keywords: animation, 4d, lighting, ar, human, head, face  
- **[GaussianPainter: Painting Point Cloud into 3D Gaussians with Normal Guidance](https://arxiv.org/abs/2412.17715v1)**  
  Authors: Jingqiu Zhou, Lue Fan, Xuesong Chen, Linjiang Huang, Si Liu, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17715v1.pdf)  
  Keywords: gaussian splatting, efficient, ar, 3d gaussian, face  
- **[LangSurf: Language-Embedded Surface Gaussians for 3D Scene Understanding](https://arxiv.org/abs/2412.17635v2)**  
  Authors: Hao Li, Roy Qin, Zhengyu Zou, Diqi He, Bohan Li, Bingquan Dai, Dingewn Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17635v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://langsurf.github.io}.)  
  Keywords: geometry, gaussian splatting, semantic, recognition, ar, understanding, segmentation, face  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: fast, gaussian splatting, large scene, nerf, ar, compression, 3d gaussian, high-fidelity, face  
- **[GeoTexDensifier: Geometry-Texture-Aware Densification for High-Quality Photorealistic 3D Gaussian Splatting](https://arxiv.org/abs/2412.16809v1)**  
  Authors: Hanqing Jiang, Xiaojun Xiang, Han Sun, Hongjie Li, Liyang Zhou, Xiaoyu Zhang, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.16809v1.pdf)  
  Keywords: geometry, gaussian splatting, efficient, ar, vr, 3d gaussian, face, efficient rendering  
- **[SOUS VIDE: Cooking Visual Drone Navigation Policies in a Gaussian Splatting Vacuum](https://arxiv.org/abs/2412.16346v1)**  
  Authors: JunEn Low, Maximilian Adang, Javier Yu, Keiko Nagami, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.16346v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://stanfordmsl.github.io/SousVide/.)  
  Keywords: gaussian splatting, lightweight, ar, dynamic, body  
- **[CoCoGaussian: Leveraging Circle of Confusion for Gaussian Splatting from Defocused Images](https://arxiv.org/abs/2412.16028v1)**  
  Authors: Jungho Lee, Suhwan Cho, Taeoh Kim, Ho-Deok Jang, Minhyeok Lee, Geonho Cha, Dongyoon Wee, Dogyoon Lee, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.16028v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, face, ar  

### Dynamic Scene

*Showing the latest 50 out of 438 papers*

- **[KeyGS: A Keyframe-Centric Gaussian Splatting Method for Monocular Image Sequences](https://arxiv.org/abs/2412.20767v1)**  
  Authors: Keng-Wei Chang, Zi-Ming Wang, Shang-Hong Lai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20767v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, efficient, ar, 3d gaussian, motion  
- **[4D Gaussian Splatting: Modeling Dynamic Scenes with Native 4D Primitives](https://arxiv.org/abs/2412.20720v1)**  
  Authors: Zeyu Yang, Zijie Pan, Xiatian Zhu, Li Zhang, Yu-Gang Jiang, Philip H. S. Torr  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20720v1.pdf)  
  Keywords: geometry, gaussian splatting, real-time rendering, compact, 4d, ar, dynamic, understanding, vr, motion  
- **[MaskGaussian: Adaptive 3D Gaussian Representation from Probabilistic Masks](https://arxiv.org/abs/2412.20522v1)**  
  Authors: Yifei Liu, Zhihang Zhong, Yifan Zhan, Sheng Xu, Xiao Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20522v1.pdf) | [![GitHub](https://img.shields.io/github/stars/kaikai23/MaskGaussian?style=social)](https://github.com/kaikai23/MaskGaussian)  
  Keywords: gaussian splatting, real-time rendering, ar, dynamic, 3d gaussian  
- **[DEGSTalk: Decomposed Per-Embedding Gaussian Fields for Hair-Preserving Talking Face Synthesis](https://arxiv.org/abs/2412.20148v1)**  
  Authors: Kaijun Deng, Dezhi Zheng, Jindong Xie, Jinbao Wang, Weicheng Xie, Linlin Shen, Siyang Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20148v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CVI-SZU/DEGSTalk?style=social)](https://github.com/CVI-SZU/DEGSTalk)  
  Keywords: gaussian splatting, efficient, ar, dynamic, 3d gaussian, face, motion  
- **[GSplatLoc: Ultra-Precise Camera Localization via 3D Gaussian Splatting](https://arxiv.org/abs/2412.20056v1)**  
  Authors: Atticus J. Zeller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20056v1.pdf)  
  Keywords: gaussian splatting, localization, robotics, mapping, ar, 3d gaussian, motion  
- **[DAS3R: Dynamics-Aware Gaussian Splatting for Static Scene Reconstruction](https://arxiv.org/abs/2412.19584v1)**  
  Authors: Kai Xu, Tze Ho Elden Tse, Jizong Peng, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19584v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kai422.github.io/DAS3R/})  
  Keywords: gaussian splatting, slam, ar, dynamic, motion  
- **[BeSplat -- Gaussian Splatting from a Single Blurry Image and Event Stream](https://arxiv.org/abs/2412.19370v1)**  
  Authors: Gopi Raju Matta, Reddypalli Trisha, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19370v1.pdf)  
  Keywords: gaussian splatting, nerf, ar, 3d gaussian, motion  
- **[Generating Editable Head Avatars with 3D Gaussian GANs](https://arxiv.org/abs/2412.19149v1)**  
  Authors: Guohao Li, Hongyu Yang, Yifang Men, Di Huang, Weixin Li, Ruijie Yang, Yunhong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19149v1.pdf) | [![GitHub](https://img.shields.io/github/stars/liguohao96/EGG3D?style=social)](https://github.com/liguohao96/EGG3D)  
  Keywords: gaussian splatting, animation, illumination, nerf, deformation, avatar, ar, 3d gaussian, head, face  
- **[FaceLift: Single Image to 3D Head with View Generation and GS-LRM](https://arxiv.org/abs/2412.17812v1)**  
  Authors: Weijie Lyu, Yi Zhou, Ming-Hsuan Yang, Zhixin Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17812v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weijielyu.github.io/FaceLift.)  
  Keywords: animation, 4d, lighting, ar, human, head, face  
- **[Exploring Dynamic Novel View Synthesis Technologies for Cinematography](https://arxiv.org/abs/2412.17532v1)**  
  Authors: Adrian Azzarelli, Nantheera Anantrasirichai, David R Bull  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17532v1.pdf)  
  Keywords: gaussian splatting, nerf, ar, dynamic, motion  

### Few-shot

*Showing the latest 50 out of 85 papers*

- **[Dust to Tower: Coarse-to-Fine Photo-Realistic Scene Reconstruction from Sparse Uncalibrated Images](https://arxiv.org/abs/2412.19518v1)**  
  Authors: Xudong Cai, Yongcai Wang, Zhaoxin Fan, Deng Haoran, Shuo Wang, Wanting Li, Deying Li, Lun Luo, Minhang Wang, Jintao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19518v1.pdf)  
  Keywords: fast, gaussian splatting, efficient, ar, sparse-view, 3d gaussian  
- **[CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting](https://arxiv.org/abs/2412.19142v1)**  
  Authors: Siyu Jiao, Haoye Dong, Yuyang Yin, Zequn Jie, Yinlong Qian, Yao Zhao, Humphrey Shi, Yunchao Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19142v1.pdf)  
  Keywords: gaussian splatting, few-shot, efficient, ar, 3d gaussian  
- **[SolidGS: Consolidating Gaussian Surfel Splatting for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2412.15400v1)**  
  Authors: Zhuowen Shen, Yuan Liu, Zhang Chen, Zhong Li, Jiepeng Wang, Yongqing Liang, Zhengming Yu, Jingdong Zhang, Yi Xu, Scott Schaefer, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15400v1.pdf)  
  Keywords: geometry, gaussian splatting, sparse view, ar, sparse-view, face  
- **[Improving Geometry in Sparse-View 3DGS via Reprojection-based DoF Separation](https://arxiv.org/abs/2412.14568v1)**  
  Authors: Yongsung Kim, Minjun Park, Jooyoung Choi, Sungroh Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.14568v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d reconstruction, ar, sparse-view, 3d gaussian  
- **[Real-time Free-view Human Rendering from Sparse-view RGB Videos using Double Unprojected Textures](https://arxiv.org/abs/2412.13183v1)**  
  Authors: Guoxing Sun, Rishabh Dabral, Heming Zhu, Pascal Fua, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13183v1.pdf)  
  Keywords: geometry, deformation, ar, body, sparse-view, human  
- **[4DRGS: 4D Radiative Gaussian Splatting for Efficient 3D Vessel Reconstruction from Sparse-View Dynamic DSA Images](https://arxiv.org/abs/2412.12919v1)**  
  Authors: Zhentao Liu, Ruyi Zha, Huangxuan Zhao, Hongdong Li, Zhiming Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12919v1.pdf)  
  Keywords: fast, gaussian splatting, geometry, compact, efficient, 4d, medical, dynamic, ar, sparse-view  
- **[TSGaussian: Semantic and Depth-Guided Target-Specific Gaussian Splatting from Sparse Views](https://arxiv.org/abs/2412.10051v1)**  
  Authors: Liang Zhao, Zehan Bao, Yi Xie, Hong Chen, Yaohui Chen, Weifu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10051v1.pdf) | [![GitHub](https://img.shields.io/github/stars/leon2000-ai/TSGaussian?style=social)](https://github.com/leon2000-ai/TSGaussian)  
  Keywords: geometry, gaussian splatting, compact, sparse view, semantic, ar, segmentation, 3d gaussian  
- **[FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction](https://arxiv.org/abs/2412.09573v1)**  
  Authors: Jiale Xu, Shenghua Gao, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09573v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, ar, sparse-view, 3d gaussian, high-fidelity  
- **[SLGaussian: Fast Language Gaussian Splatting in Sparse Views](https://arxiv.org/abs/2412.08331v1)**  
  Authors: Kangjie Chen, BingQuan Dai, Minghan Qin, Dongbin Zhang, Peihao Li, Yingshuang Zou, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08331v1.pdf)  
  Keywords: fast, gaussian splatting, localization, efficient, sparse view, semantic, robotics, tracking, ar, understanding, vr, segmentation  
- **[MV-DUSt3R+: Single-Stage Scene Reconstruction from Sparse Views In 2 Seconds](https://arxiv.org/abs/2412.06974v1)**  
  Authors: Zhenggang Tang, Yuchen Fan, Dilin Wang, Hongyu Xu, Rakesh Ranjan, Alexander Schwing, Zhicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.06974v1.pdf)  
  Keywords: fast, gaussian splatting, sparse view, ar, head  

### Geometry Reconstruction

*Showing the latest 50 out of 400 papers*

- **[Prometheus: 3D-Aware Latent Diffusion Models for Feed-Forward Text-to-3D Scene Generation](https://arxiv.org/abs/2412.21117v2)**  
  Authors: Yuanbo Yang, Jiahao Shao, Xinyang Li, Yujun Shen, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.21117v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://freemty.github.io/project-prometheus/)  
  Keywords: geometry, efficient, 3d gaussian, ar  
- **[4D Gaussian Splatting: Modeling Dynamic Scenes with Native 4D Primitives](https://arxiv.org/abs/2412.20720v1)**  
  Authors: Zeyu Yang, Zijie Pan, Xiatian Zhu, Li Zhang, Yu-Gang Jiang, Philip H. S. Torr  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20720v1.pdf)  
  Keywords: geometry, gaussian splatting, real-time rendering, compact, 4d, ar, dynamic, understanding, vr, motion  
- **[Reflective Gaussian Splatting](https://arxiv.org/abs/2412.19282v1)**  
  Authors: Yuxuan Yao, Zixuan Zeng, Chun Gu, Xiatian Zhu, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19282v1.pdf)  
  Keywords: geometry, gaussian splatting, nerf, lighting, ar, reflection, relighting  
- **[WeatherGS: 3D Scene Reconstruction in Adverse Weather Conditions via Gaussian Splatting](https://arxiv.org/abs/2412.18862v2)**  
  Authors: Chenghao Qian, Yuhu Guo, Wenjing Li, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.18862v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/weather-gs.)  
  Keywords: gaussian splatting, 3d gaussian, 3d reconstruction, ar, outdoor  
- **[Resolution-Robust 3D MRI Reconstruction with 2D Diffusion Priors: Diverse-Resolution Training Outperforms Interpolation](https://arxiv.org/abs/2412.18584v1)**  
  Authors: Anselm Krainovic, Stefan Ruschke, Reinhard Heckel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.18584v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, ar  
- **[LangSurf: Language-Embedded Surface Gaussians for 3D Scene Understanding](https://arxiv.org/abs/2412.17635v2)**  
  Authors: Hao Li, Roy Qin, Zhengyu Zou, Diqi He, Bohan Li, Bingquan Dai, Dingewn Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17635v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://langsurf.github.io}.)  
  Keywords: geometry, gaussian splatting, semantic, recognition, ar, understanding, segmentation, face  
- **[GeoTexDensifier: Geometry-Texture-Aware Densification for High-Quality Photorealistic 3D Gaussian Splatting](https://arxiv.org/abs/2412.16809v1)**  
  Authors: Hanqing Jiang, Xiaojun Xiang, Han Sun, Hongjie Li, Liyang Zhou, Xiaoyu Zhang, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.16809v1.pdf)  
  Keywords: geometry, gaussian splatting, efficient, ar, vr, 3d gaussian, face, efficient rendering  
- **[SolidGS: Consolidating Gaussian Surfel Splatting for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2412.15400v1)**  
  Authors: Zhuowen Shen, Yuan Liu, Zhang Chen, Zhong Li, Jiepeng Wang, Yongqing Liang, Zhengming Yu, Jingdong Zhang, Yi Xu, Scott Schaefer, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15400v1.pdf)  
  Keywords: geometry, gaussian splatting, sparse view, ar, sparse-view, face  
- **[GSRender: Deduplicated Occupancy Prediction via Weakly Supervised 3D Gaussian Splatting](https://arxiv.org/abs/2412.14579v1)**  
  Authors: Qianpu Sun, Changyong Shu, Sifan Zhou, Zichen Yu, Yan Chen, Dawei Yang, Yuan Chun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.14579v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, nerf, ar, dynamic, 3d gaussian  
- **[Improving Geometry in Sparse-View 3DGS via Reprojection-based DoF Separation](https://arxiv.org/abs/2412.14568v1)**  
  Authors: Yongsung Kim, Minjun Park, Jooyoung Choi, Sungroh Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.14568v1.pdf)  
  Keywords: geometry, gaussian splatting, 3d reconstruction, ar, sparse-view, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 66 papers*

- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: outdoor, gaussian splatting, slam, efficient, nerf, mapping, ar, neural rendering, 3d gaussian  
- **[WeatherGS: 3D Scene Reconstruction in Adverse Weather Conditions via Gaussian Splatting](https://arxiv.org/abs/2412.18862v2)**  
  Authors: Chenghao Qian, Yuhu Guo, Wenjing Li, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.18862v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/weather-gs.)  
  Keywords: gaussian splatting, 3d gaussian, 3d reconstruction, ar, outdoor  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: fast, gaussian splatting, large scene, nerf, ar, compression, 3d gaussian, high-fidelity, face  
- **[LiHi-GS: LiDAR-Supervised Gaussian Splatting for Highway Driving Scene Reconstruction](https://arxiv.org/abs/2412.15447v2)**  
  Authors: Pou-Chun Kung, Xianling Zhang, Katherine A. Skinner, Nikita Jaipuria  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15447v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/lihi_gs)  
  Keywords: fast, gaussian splatting, autonomous driving, nerf, ar, dynamic, urban scene, 3d gaussian  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: geometry, outdoor, localization, slam, tracking, lighting, mapping, dynamic, reflection, ar, survey, 3d gaussian, face  
- **[Momentum-GS: Momentum Gaussian Self-Distillation for High-Quality Large Scene Reconstruction](https://arxiv.org/abs/2412.04887v1)**  
  Authors: Jixuan Fan, Wanhua Li, Yifei Han, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04887v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jixuan-fan.github.io/Momentum-GS_Page/)  
  Keywords: gaussian splatting, large scene, ar, dynamic, 3d gaussian, head  
- **[HybridGS: Decoupling Transients and Statics with 2D and 3D Gaussian Splatting](https://arxiv.org/abs/2412.03844v2)**  
  Authors: Jingyu Lin, Jiaqi Gu, Lubin Fan, Bojian Wu, Yujing Lou, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03844v2.pdf)  
  Keywords: outdoor, gaussian splatting, 3d gaussian, ar  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: gaussian splatting, semantic, 4d, deformation, ar, dynamic, urban scene, face  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: gaussian splatting, localization, slam, nerf, lighting, tracking, dynamic, mapping, ar, understanding, outdoor  
- **[Horizon-GS: Unified 3D Gaussian Splatting for Large-Scale Aerial-to-Ground Scenes](https://arxiv.org/abs/2412.01745v1)**  
  Authors: Lihan Jiang, Kerui Ren, Mulin Yu, Linning Xu, Junting Dong, Tao Lu, Feng Zhao, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01745v1.pdf)  
  Keywords: gaussian splatting, ar, urban scene, 3d gaussian, high-fidelity  

### Model Compression

*Showing the latest 50 out of 438 papers*

- **[Prometheus: 3D-Aware Latent Diffusion Models for Feed-Forward Text-to-3D Scene Generation](https://arxiv.org/abs/2412.21117v2)**  
  Authors: Yuanbo Yang, Jiahao Shao, Xinyang Li, Yujun Shen, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.21117v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://freemty.github.io/project-prometheus/)  
  Keywords: geometry, efficient, 3d gaussian, ar  
- **[KeyGS: A Keyframe-Centric Gaussian Splatting Method for Monocular Image Sequences](https://arxiv.org/abs/2412.20767v1)**  
  Authors: Keng-Wei Chang, Zi-Ming Wang, Shang-Hong Lai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20767v1.pdf)  
  Keywords: gaussian splatting, real-time rendering, efficient, ar, 3d gaussian, motion  
- **[4D Gaussian Splatting: Modeling Dynamic Scenes with Native 4D Primitives](https://arxiv.org/abs/2412.20720v1)**  
  Authors: Zeyu Yang, Zijie Pan, Xiatian Zhu, Li Zhang, Yu-Gang Jiang, Philip H. S. Torr  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20720v1.pdf)  
  Keywords: geometry, gaussian splatting, real-time rendering, compact, 4d, ar, dynamic, understanding, vr, motion  
- **[DEGSTalk: Decomposed Per-Embedding Gaussian Fields for Hair-Preserving Talking Face Synthesis](https://arxiv.org/abs/2412.20148v1)**  
  Authors: Kaijun Deng, Dezhi Zheng, Jindong Xie, Jinbao Wang, Weicheng Xie, Linlin Shen, Siyang Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20148v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CVI-SZU/DEGSTalk?style=social)](https://github.com/CVI-SZU/DEGSTalk)  
  Keywords: gaussian splatting, efficient, ar, dynamic, 3d gaussian, face, motion  
- **[Dust to Tower: Coarse-to-Fine Photo-Realistic Scene Reconstruction from Sparse Uncalibrated Images](https://arxiv.org/abs/2412.19518v1)**  
  Authors: Xudong Cai, Yongcai Wang, Zhaoxin Fan, Deng Haoran, Shuo Wang, Wanting Li, Deying Li, Lun Luo, Minhang Wang, Jintao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19518v1.pdf)  
  Keywords: fast, gaussian splatting, efficient, ar, sparse-view, 3d gaussian  
- **[CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting](https://arxiv.org/abs/2412.19142v1)**  
  Authors: Siyu Jiao, Haoye Dong, Yuyang Yin, Zequn Jie, Yinlong Qian, Yao Zhao, Humphrey Shi, Yunchao Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19142v1.pdf)  
  Keywords: gaussian splatting, few-shot, efficient, ar, 3d gaussian  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: outdoor, gaussian splatting, slam, efficient, nerf, mapping, ar, neural rendering, 3d gaussian  
- **[ArtNVG: Content-Style Separated Artistic Neighboring-View Gaussian Stylization](https://arxiv.org/abs/2412.18783v1)**  
  Authors: Zixiao Gu, Mengtian Li, Ruhua Chen, Zhongxia Ji, Sichen Guo, Zhenye Zhang, Guangnan Ye, Zuo Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.18783v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, efficient, ar  
- **[GaussianPainter: Painting Point Cloud into 3D Gaussians with Normal Guidance](https://arxiv.org/abs/2412.17715v1)**  
  Authors: Jingqiu Zhou, Lue Fan, Xuesong Chen, Linjiang Huang, Si Liu, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17715v1.pdf)  
  Keywords: gaussian splatting, efficient, ar, 3d gaussian, face  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: fast, gaussian splatting, large scene, nerf, ar, compression, 3d gaussian, high-fidelity, face  

### Quality Enhancement

*Showing the latest 50 out of 199 papers*

- **[ActiveGS: Active Scene Reconstruction using Gaussian Splatting](https://arxiv.org/abs/2412.17769v1)**  
  Authors: Liren Jin, Xingguang Zhong, Yue Pan, Jens Behley, Cyrill Stachniss, Marija Popović  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17769v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, robotics, ar  
- **[CoSurfGS:Collaborative 3D Surface Gaussian Splatting with Distributed Learning for Large Scene Reconstruction](https://arxiv.org/abs/2412.17612v1)**  
  Authors: Yuanyuan Gao, Yalun Dai, Hao Li, Weicai Ye, Junyi Chen, Danpeng Chen, Dingwen Zhang, Tong He, Guofeng Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17612v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gyy456.github.io/CoSurfGS}.)  
  Keywords: fast, gaussian splatting, large scene, nerf, ar, compression, 3d gaussian, high-fidelity, face  
- **[SqueezeMe: Efficient Gaussian Avatars for VR](https://arxiv.org/abs/2412.15171v2)**  
  Authors: Shunsuke Saito, Stanislav Pidhorskyi, Igor Santesteban, Forrest Iandola, Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Frank Yu, Emanuel Garbin, Tomas Simon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15171v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://forresti.github.io/squeezeme.)  
  Keywords: high quality, gaussian splatting, efficient, avatar, ar, vr, human, head, motion  
- **[HyperGS: Hyperspectral 3D Gaussian Splatting](https://arxiv.org/abs/2412.12849v1)**  
  Authors: Christopher Thirgood, Oscar Mendez, Erin Chao Ling, Jon Storey, Simon Hadfield  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12849v1.pdf)  
  Keywords: gaussian splatting, 4d, ar, 3d gaussian, high-fidelity  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: gaussian splatting, ray tracing, real-time rendering, efficient, lighting, ar, reflection, 3d gaussian, high-fidelity  
- **[Deformable Radial Kernel Splatting](https://arxiv.org/abs/2412.11752v1)**  
  Authors: Yi-Hua Huang, Ming-Xian Lin, Yang-Tian Sun, Ziyi Yang, Xiaoyang Lyu, Yan-Pei Cao, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11752v1.pdf)  
  Keywords: geometry, gaussian splatting, efficient, ar, high-fidelity  
- **[SweepEvGS: Event-Based 3D Gaussian Splatting for Macro and Micro Radiance Field Rendering from a Single Sweep](https://arxiv.org/abs/2412.11579v1)**  
  Authors: Jingqian Wu, Shuo Zhu, Chutian Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11579v1.pdf)  
  Keywords: gaussian splatting, efficient, lighting, ar, dynamic, 3d gaussian, high-fidelity, motion  
- **[MAC-Ego3D: Multi-Agent Gaussian Consensus for Real-Time Collaborative Ego-Motion and Photorealistic 3D Reconstruction](https://arxiv.org/abs/2412.09723v1)**  
  Authors: Xiaohao Xu, Feng Xue, Shibo Zhao, Yike Pan, Sebastian Scherer, Xiaonan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09723v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Xiaohao-Xu/MAC-Ego3D?style=social)](https://github.com/Xiaohao-Xu/MAC-Ego3D)  
  Keywords: localization, efficient, 3d reconstruction, mapping, ar, high-fidelity, motion  
- **[FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction](https://arxiv.org/abs/2412.09573v1)**  
  Authors: Jiale Xu, Shenghua Gao, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09573v1.pdf)  
  Keywords: gaussian splatting, 3d reconstruction, ar, sparse-view, 3d gaussian, high-fidelity  
- **[PointTalk: Audio-Driven Dynamic Lip Point Cloud for 3D Gaussian-based Talking Head Synthesis](https://arxiv.org/abs/2412.08504v1)**  
  Authors: Yifan Xie, Tao Feng, Xin Zhang, Xiangyang Luo, Zixuan Guo, Weijiang Yu, Heng Chang, Fei Ma, Fei Richard Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.08504v1.pdf)  
  Keywords: ar, dynamic, understanding, human, 3d gaussian, head, high-fidelity  

### Ray Tracing

- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: gaussian splatting, ray tracing, efficient, lighting, ar, reflection, relighting  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: gaussian splatting, ray tracing, real-time rendering, efficient, lighting, ar, reflection, 3d gaussian, high-fidelity  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: fast, gaussian splatting, geometry, efficient, illumination, nerf, mapping, ar, global illumination, face  
- **[WRF-GS: Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2412.04832v1)**  
  Authors: Chaozheng Wen, Jingwen Tong, Yingdong Hu, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04832v1.pdf)  
  Keywords: gaussian splatting, ray tracing, efficient, ar, 3d gaussian  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v1)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ray tracing, ar  
- **[URAvatar: Universal Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2410.24223v1)**  
  Authors: Junxuan Li, Chen Cao, Gabriel Schwartz, Rawal Khirodkar, Christian Richardt, Tomas Simon, Yaser Sheikh, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24223v1.pdf)  
  Keywords: light transport, real-time rendering, efficient, illumination, avatar, ar, global illumination, relightable, human, 3d gaussian, head  
- **[Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization](https://arxiv.org/abs/2410.16978v1)**  
  Authors: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, Ralf Gutjahr, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16978v1.pdf)  
  Keywords: gaussian splatting, path tracing, efficient, medical, ar, understanding, vr, head  
- **[GS^3: Efficient Relighting with Triple Gaussian Splatting](https://arxiv.org/abs/2410.11419v1)**  
  Authors: Zoubin Bi, Yixin Zeng, Chong Zeng, Fan Pei, Xiang Feng, Kun Zhou, Hongzhi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11419v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://GSrelight.github.io/.)  
  Keywords: geometry, gaussian splatting, shadow, efficient, illumination, lighting, ar, global illumination, relighting  
- **[RGM: Reconstructing High-fidelity 3D Car Assets with Relightable 3D-GS Generative Model from a Single Image](https://arxiv.org/abs/2410.08181v1)**  
  Authors: Xiaoxue Chen, Jv Zheng, Hao Huang, Haoran Xu, Weihao Gu, Kangliang Chen, He xiang, Huan-ang Gao, Hao Zhao, Guyue Zhou, Yaqin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08181v1.pdf)  
  Keywords: geometry, autonomous driving, illumination, nerf, lighting, ar, relighting, global illumination, relightable, 3d gaussian, high-fidelity  
- **[6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering](https://arxiv.org/abs/2410.04974v2)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04974v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/6dgs/)  
  Keywords: high quality, gaussian splatting, ray tracing, real-time rendering, nerf, ar, 3d gaussian  

### Relighting

*Showing the latest 50 out of 135 papers*

- **[Reflective Gaussian Splatting](https://arxiv.org/abs/2412.19282v1)**  
  Authors: Yuxuan Yao, Zixuan Zeng, Chun Gu, Xiatian Zhu, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19282v1.pdf)  
  Keywords: geometry, gaussian splatting, nerf, lighting, ar, reflection, relighting  
- **[Generating Editable Head Avatars with 3D Gaussian GANs](https://arxiv.org/abs/2412.19149v1)**  
  Authors: Guohao Li, Hongyu Yang, Yifang Men, Di Huang, Weixin Li, Ruijie Yang, Yunhong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19149v1.pdf) | [![GitHub](https://img.shields.io/github/stars/liguohao96/EGG3D?style=social)](https://github.com/liguohao96/EGG3D)  
  Keywords: gaussian splatting, animation, illumination, nerf, deformation, avatar, ar, 3d gaussian, head, face  
- **[FaceLift: Single Image to 3D Head with View Generation and GS-LRM](https://arxiv.org/abs/2412.17812v1)**  
  Authors: Weijie Lyu, Yi Zhou, Ming-Hsuan Yang, Zhixin Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17812v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weijielyu.github.io/FaceLift.)  
  Keywords: animation, 4d, lighting, ar, human, head, face  
- **[IRGS: Inter-Reflective Gaussian Splatting with 2D Gaussian Ray Tracing](https://arxiv.org/abs/2412.15867v1)**  
  Authors: Chun Gu, Xiaofei Wei, Zixuan Zeng, Yuxuan Yao, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.15867v1.pdf)  
  Keywords: gaussian splatting, ray tracing, efficient, lighting, ar, reflection, relighting  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: geometry, outdoor, localization, slam, tracking, lighting, mapping, dynamic, reflection, ar, survey, 3d gaussian, face  
- **[EOGS: Gaussian Splatting for Earth Observation](https://arxiv.org/abs/2412.13047v1)**  
  Authors: Luca Savant Aira, Gabriele Facciolo, Thibaud Ehret  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13047v1.pdf)  
  Keywords: nerf, gaussian splatting, shadow, ar  
- **[3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507v1)**  
  Authors: Qi Wu, Janick Martinez Esturo, Ashkan Mirzaei, Nicolas Moenne-Loccoz, Zan Gojcic  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12507v1.pdf)  
  Keywords: gaussian splatting, ray tracing, real-time rendering, efficient, lighting, ar, reflection, 3d gaussian, high-fidelity  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: fast, gaussian splatting, geometry, efficient, illumination, nerf, mapping, ar, global illumination, face  
- **[SweepEvGS: Event-Based 3D Gaussian Splatting for Macro and Micro Radiance Field Rendering from a Single Sweep](https://arxiv.org/abs/2412.11579v1)**  
  Authors: Jingqian Wu, Shuo Zhu, Chutian Wang, Boxin Shi, Edmund Y. Lam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11579v1.pdf)  
  Keywords: gaussian splatting, efficient, lighting, ar, dynamic, 3d gaussian, high-fidelity, motion  
- **[GaussianProperty: Integrating Physical Properties to 3D Gaussians with LMMs](https://arxiv.org/abs/2412.11258v1)**  
  Authors: Xinli Xu, Wenhang Ge, Dicong Qiu, ZhiFei Chen, Dongyu Yan, Zhuoyun Liu, Haoyu Zhao, Hanfeng Zhao, Shunsi Zhang, Junwei Liang, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11258v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://Gaussian-Property.github.io}{this)  
  Keywords: recognition, robotics, lighting, ar, dynamic, understanding, segmentation, 3d gaussian  

### SLAM

*Showing the latest 50 out of 172 papers*

- **[GSplatLoc: Ultra-Precise Camera Localization via 3D Gaussian Splatting](https://arxiv.org/abs/2412.20056v1)**  
  Authors: Atticus J. Zeller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20056v1.pdf)  
  Keywords: gaussian splatting, localization, robotics, mapping, ar, 3d gaussian, motion  
- **[DAS3R: Dynamics-Aware Gaussian Splatting for Static Scene Reconstruction](https://arxiv.org/abs/2412.19584v1)**  
  Authors: Kai Xu, Tze Ho Elden Tse, Jizong Peng, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19584v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kai422.github.io/DAS3R/})  
  Keywords: gaussian splatting, slam, ar, dynamic, motion  
- **[MVS-GS: High-Quality 3D Gaussian Splatting Mapping via Online Multi-View Stereo](https://arxiv.org/abs/2412.19130v1)**  
  Authors: Byeonggwon Lee, Junkyu Park, Khang Truong Giang, Sungho Jo, Soohwan Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.19130v1.pdf)  
  Keywords: outdoor, gaussian splatting, slam, efficient, nerf, mapping, ar, neural rendering, 3d gaussian  
- **[GraphAvatar: Compact Head Avatars with GNN-Generated 3D Gaussians](https://arxiv.org/abs/2412.13983v1)**  
  Authors: Xiaobao Wei, Peng Chen, Ming Lu, Hui Chen, Feng Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13983v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ucwxb/GraphAvatar?style=social)](https://github.com/ucwxb/GraphAvatar)  
  Keywords: gaussian splatting, compact, nerf, tracking, avatar, ar, 3d gaussian, head, face  
- **[4D Radar-Inertial Odometry based on Gaussian Modeling and Multi-Hypothesis Scan Matching](https://arxiv.org/abs/2412.13639v1)**  
  Authors: Fernando Amodeo, Luis Merino, Fernando Caballero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13639v1.pdf)  
  Keywords: gaussian splatting, slam, 4d, ar, 3d gaussian  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v1)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: geometry, outdoor, localization, slam, tracking, lighting, mapping, dynamic, reflection, ar, survey, 3d gaussian, face  
- **[Gaussian Billboards: Expressive 2D Gaussian Splatting with Textures](https://arxiv.org/abs/2412.12734v1)**  
  Authors: Sebastian Weiss, Derek Bradley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12734v1.pdf)  
  Keywords: geometry, gaussian splatting, mapping, ar, face  
- **[GS-ProCams: Gaussian Splatting-based Projector-Camera Systems](https://arxiv.org/abs/2412.11762v1)**  
  Authors: Qingyue Deng, Jijiang Li, Haibin Ling, Bingyao Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11762v1.pdf)  
  Keywords: fast, gaussian splatting, geometry, efficient, illumination, nerf, mapping, ar, global illumination, face  
- **[SuperGSeg: Open-Vocabulary 3D Segmentation with Structured Super-Gaussians](https://arxiv.org/abs/2412.10231v1)**  
  Authors: Siyun Liang, Sen Wang, Kunyi Li, Michael Niemeyer, Stefano Gasperini, Nassir Navab, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.10231v1.pdf)  
  Keywords: gaussian splatting, localization, real-time rendering, efficient, semantic, ar, understanding, segmentation, 3d gaussian  
- **[RP-SLAM: Real-time Photorealistic SLAM with Efficient 3D Gaussian Splatting](https://arxiv.org/abs/2412.09868v1)**  
  Authors: Lizhi Bai, Chunqi Tian, Jun Yang, Siyu Zhang, Masanori Suganuma, Takayuki Okatani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.09868v1.pdf)  
  Keywords: gaussian splatting, compact, efficient, slam, mapping, ar, dynamic, 3d gaussian, face  

### Scene Understanding

*Showing the latest 50 out of 206 papers*

- **[4D Gaussian Splatting: Modeling Dynamic Scenes with Native 4D Primitives](https://arxiv.org/abs/2412.20720v1)**  
  Authors: Zeyu Yang, Zijie Pan, Xiatian Zhu, Li Zhang, Yu-Gang Jiang, Philip H. S. Torr  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.20720v1.pdf)  
  Keywords: geometry, gaussian splatting, real-time rendering, compact, 4d, ar, dynamic, understanding, vr, motion  
- **[LangSurf: Language-Embedded Surface Gaussians for 3D Scene Understanding](https://arxiv.org/abs/2412.17635v2)**  
  Authors: Hao Li, Roy Qin, Zhengyu Zou, Diqi He, Bohan Li, Bingquan Dai, Dingewn Zhang, Junwei Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.17635v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://langsurf.github.io}.)  
  Keywords: geometry, gaussian splatting, semantic, recognition, ar, understanding, segmentation, face  
- **[GSemSplat: Generalizable Semantic 3D Gaussian Splatting from Uncalibrated Image Pairs](https://arxiv.org/abs/2412.16932v1)**  
  Authors: Xingrui Wang, Cuiling Lan, Hanxin Zhu, Zhibo Chen, Yan Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.16932v1.pdf)  
  Keywords: gaussian splatting, semantic, ar, understanding, 3d gaussian  
- **[OmniSplat: Taming Feed-Forward 3D Gaussian Splatting for Omnidirectional Images with Editable Capabilities](https://arxiv.org/abs/2412.16604v1)**  
  Authors: Suyoung Lee, Jaeyoung Chung, Kihoon Kim, Jaeyoo Huh, Gunhee Lee, Minsoo Lee, Kyoung Mu Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.16604v1.pdf)  
  Keywords: fast, gaussian splatting, ar, segmentation, 3d gaussian  
- **[Interactive Scene Authoring with Specialized Generative Primitives](https://arxiv.org/abs/2412.16253v1)**  
  Authors: Clément Jambon, Changwoon Choi, Dongsu Zhang, Olga Sorkine-Hornung, Young Min Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.16253v1.pdf)  
  Keywords: gaussian splatting, efficient, semantic, lightweight, ar, 3d gaussian  
- **[GAGS: Granularity-Aware Feature Distillation for Language Gaussian Splatting](https://arxiv.org/abs/2412.13654v1)**  
  Authors: Yuning Peng, Haiping Wang, Yuan Liu, Chenglu Wen, Zhen Dong, Bisheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13654v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pz0826.github.io/GAGS-Webpage/)  
  Keywords: fast, gaussian splatting, semantic, ar, understanding, segmentation, 3d gaussian  
- **[Vivar: A Generative AR System for Intuitive Multi-Modal Sensor Data Presentation](https://arxiv.org/abs/2412.13509v1)**  
  Authors: Yunqi Guo, Kaiyuan Hou, Heming Fu, Hongkai Chen, Zhenyu Yan, Guoliang Xing, Xiaofan Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13509v1.pdf)  
  Keywords: gaussian splatting, semantic, ar, dynamic, understanding, 3d gaussian  
- **[GaussTR: Foundation Model-Aligned Gaussian Transformer for Self-Supervised 3D Spatial Understanding](https://arxiv.org/abs/2412.13193v1)**  
  Authors: Haoyi Jiang, Liu Liu, Tianheng Cheng, Xinjie Wang, Tianwei Lin, Zhizhong Su, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13193v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hustvl/GaussTR?style=social)](https://github.com/hustvl/GaussTR)  
  Keywords: semantic, autonomous driving, ar, understanding, 3d gaussian  
- **[CATSplat: Context-Aware Transformer with Spatial Guidance for Generalizable 3D Gaussian Splatting from A Single-View Image](https://arxiv.org/abs/2412.12906v1)**  
  Authors: Wonseok Roh, Hwanhee Jung, Jong Wook Kim, Seunggwan Lee, Innfarn Yoo, Andreas Lugmayr, Seunggeun Chi, Karthik Ramani, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.12906v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, understanding, ar  
- **[EditSplat: Multi-View Fusion and Attention-Guided Optimization for View-Consistent 3D Scene Editing with 3D Gaussian Splatting](https://arxiv.org/abs/2412.11520v1)**  
  Authors: Dong In Lee, Hyeongcheol Park, Jiyoung Seo, Eunbyung Park, Hyunje Park, Ha Dam Baek, Shin Sangheon, Sangmin kim, Sangpil Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.11520v1.pdf)  
  Keywords: gaussian splatting, efficient, semantic, ar, vr, 3d gaussian  



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