# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2024-12-09 00:53:14

## Categories

- [3DGS Surveys](#3dgs-surveys) (19 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (321 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1084 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (366 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (394 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (73 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (364 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (59 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (390 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (180 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (24 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (121 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (158 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (185 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: recognition, gaussian splatting, 3d gaussian, ar, survey, illumination  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: lighting, high-fidelity, dynamic, nerf, compact, robotics, 3d reconstruction, ar, semantic, autonomous driving, survey, geometry, gaussian splatting  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v1)**  
  Authors: Siting Zhu, Guangming Wang, Dezhi Kong, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v1.pdf)  
  Keywords: understanding, real-time rendering, nerf, robotics, 3d gaussian, ar, survey, gaussian splatting  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  Authors: Zhengren Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  Keywords: lighting, high-fidelity, nerf, 3d gaussian, ar, survey, gaussian splatting  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v1)**  
  Authors: Fangjinhua Wang, Qingtian Zhu, Di Chang, Quankai Gao, Junlin Han, Tong Zhang, Richard Hartley, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v1.pdf)  
  Keywords: nerf, robotics, 3d reconstruction, 3d gaussian, ar, autonomous driving, survey, vr, gaussian splatting  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  Authors: Khaled Said, Cullan Howlett, Tamara Davis, John Lucey, Christoph Saulder, Kelly Douglass, Alex G. Kim, Anthony Kremin, Caitlin Ross, Greg Aldering, Jessica Nicole Aguilar, Steven Ahlen, Segev BenZvi, Davide Bianchi, David Brooks, Todd Claybaugh, Kyle Dawson, Axel de la Macorra, Biprateep Dey, Peter Doel, Kevin Fanning, Simone Ferraro, Andreu Font-Ribera, Jaime E. Forero-Romero, Enrique Gaztañaga, Satya Gontcho A Gontcho, Julien Guy, Klaus Honscheid, Robert Kehoe, Theodore Kisner, Andrew Lambert, Martin Landriau, Laurent Le Guillou, Marc Manera, Aaron Meisner, Ramon Miquel, John Moustakas, Andrea Muñoz-Gutiérrez, Adam Myers, Jundan Nie, Nathalie Palanque-Delabrouille, Will Percival, Francisco Prada, Graziano Rossi, Eusebio Sanchez, David Schlegel, Michael Schubnell, Joseph Harry Silber, David Sprayberry, Gregory Tarlé, Mariana Vargas Magana, Benjamin Alan Weaver, Risa Wechsler, Zhimin Zhou, Hu Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  Keywords: 3d gaussian, ar, survey  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v1)**  
  Authors: Yanqi Bao, Tianyu Ding, Jing Huo, Yaoli Liu, Yuxin Li, Wenbin Li, Yang Gao, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v1.pdf)  
  Keywords: understanding, real-time rendering, 3d gaussian, efficient, ar, survey, gaussian splatting  
- **[Survey on Fundamental Deep Learning 3D Reconstruction Techniques](https://arxiv.org/abs/2407.08137v1)**  
  Authors: Yonge Bai, LikHang Wong, TszYin Twan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.08137v1.pdf)  
  Keywords: lighting, nerf, 3d reconstruction, 3d gaussian, ar, survey, gaussian splatting  
- **[Panopticon: a telescope for our times](https://arxiv.org/abs/2407.05103v2)**  
  Authors: Will Saunders, Timothy Chin, Michael Goodwin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05103v2.pdf)  
  Keywords: ar, survey  
- **[3DGS.zip: A survey on 3D Gaussian Splatting Compression Methods](https://arxiv.org/abs/2407.09510v4)**  
  Authors: Milena T. Bagdasarian, Paul Knoll, Yi-Hsin Li, Florian Barthel, Anna Hilsmann, Peter Eisert, Wieland Morgenstern  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.09510v4.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://w-m.github.io/3dgs-compression-survey/)  
  Keywords: compression, compact, 3d gaussian, efficient, head, ar, survey, gaussian splatting  

### Acceleration

*Showing the latest 50 out of 321 papers*

- **[Turbo3D: Ultra-fast Text-to-3D Generation](https://arxiv.org/abs/2412.04470v1)**  
  Authors: Hanzhe Hu, Tianwei Yin, Fujun Luan, Yiwei Hu, Hao Tan, Zexiang Xu, Sai Bi, Shubham Tulsiani, Kai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04470v1.pdf)  
  Keywords: efficient, fast, ar, gaussian splatting  
- **[QUEEN: QUantized Efficient ENcoding of Dynamic Gaussians for Streaming Free-viewpoint Videos](https://arxiv.org/abs/2412.04469v1)**  
  Authors: Sharath Girish, Tianye Li, Amrita Mazumdar, Abhinav Shrivastava, David Luebke, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/queen)  
  Keywords: fast, high quality, 3d gaussian, efficient, ar, gaussian splatting, dynamic  
- **[Monocular Dynamic Gaussian Splatting is Fast and Brittle but Smooth Motion Helps](https://arxiv.org/abs/2412.04457v1)**  
  Authors: Yiqing Liang, Mikhail Okunev, Mikaela Angelina Uy, Runfeng Li, Leonidas Guibas, James Tompkin, Adam W. Harley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04457v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lynl7130.github.io/MonoDyGauBench.github.io/)  
  Keywords: motion, fast, ar, gaussian splatting, dynamic  
- **[InfiniCube: Unbounded and Controllable Dynamic 3D Driving Scene Generation with World-Guided Video Models](https://arxiv.org/abs/2412.03934v1)**  
  Authors: Yifan Lu, Xuanchi Ren, Jiawei Yang, Tianchang Shen, Zhangjie Wu, Jun Gao, Yue Wang, Siheng Chen, Mike Chen, Sanja Fidler, Jiahui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03934v1.pdf)  
  Keywords: 3d gaussian, dynamic, fast, ar  
- **[DGNS: Deformable Gaussian Splatting and Dynamic Neural Surface for Monocular Dynamic 3D Reconstruction](https://arxiv.org/abs/2412.03910v1)**  
  Authors: Xuesong Li, Jinguang Tong, Jie Hong, Vivien Rolland, Lars Petersson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03910v1.pdf)  
  Keywords: geometry, fast, 3d reconstruction, ar, gaussian splatting, face, dynamic  
- **[Splats in Splats: Embedding Invisible 3D Watermark within Gaussian Splatting](https://arxiv.org/abs/2412.03121v1)**  
  Authors: Yijia Guo, Wenkai Huang, Yang Li, Gaolei Li, Hang Zhang, Liwen Hu, Jianhua Li, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03121v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://water-gs.github.io.)  
  Keywords: fast, 3d reconstruction, 3d gaussian, efficient, ar, gaussian splatting, mapping  
- **[Gaussian Splatting Under Attack: Investigating Adversarial Noise in 3D Objects](https://arxiv.org/abs/2412.02803v1)**  
  Authors: Abdurrahman Zeybey, Mehmet Ergezer, Tommy Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02803v1.pdf)  
  Keywords: human, robotics, fast, 3d gaussian, ar, autonomous driving, gaussian splatting  
- **[AniGS: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction](https://arxiv.org/abs/2412.02684v1)**  
  Authors: Lingteng Qiu, Shenhao Zhu, Qi Zuo, Xiaodong Gu, Yuan Dong, Junfei Zhang, Chao Xu, Zhe Li, Weihao Yuan, Liefeng Bo, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02684v1.pdf)  
  Keywords: real-time rendering, animation, human, 3d reconstruction, efficient, ar, gaussian splatting, avatar, 4d  
- **[SparseGrasp: Robotic Grasping via 3D Semantic Gaussian Splatting from Sparse Multi-View RGB Images](https://arxiv.org/abs/2412.02140v1)**  
  Authors: Junqiu Yu, Xinlin Ren, Yongchong Gu, Haitao Lin, Tianyu Wang, Yi Zhu, Hang Xu, Yu-Gang Jiang, Xiangyang Xue, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02140v1.pdf)  
  Keywords: human, fast, 3d gaussian, efficient, semantic, ar, gaussian splatting, sparse-view  
- **[Planar Gaussian Splatting](https://arxiv.org/abs/2412.01931v1)**  
  Authors: Farhad G. Zanjani, Hong Cai, Hanno Ackermann, Leila Mirvakhabova, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01931v1.pdf)  
  Keywords: neural rendering, fast, ar, gaussian splatting, face, geometry, segmentation  

### Applications

*Showing the latest 50 out of 1084 papers*

- **[Turbo3D: Ultra-fast Text-to-3D Generation](https://arxiv.org/abs/2412.04470v1)**  
  Authors: Hanzhe Hu, Tianwei Yin, Fujun Luan, Yiwei Hu, Hao Tan, Zexiang Xu, Sai Bi, Shubham Tulsiani, Kai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04470v1.pdf)  
  Keywords: efficient, fast, ar, gaussian splatting  
- **[QUEEN: QUantized Efficient ENcoding of Dynamic Gaussians for Streaming Free-viewpoint Videos](https://arxiv.org/abs/2412.04469v1)**  
  Authors: Sharath Girish, Tianye Li, Amrita Mazumdar, Abhinav Shrivastava, David Luebke, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/queen)  
  Keywords: fast, high quality, 3d gaussian, efficient, ar, gaussian splatting, dynamic  
- **[Sparse Voxels Rasterization: Real-time High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2412.04459v1)**  
  Authors: Cheng Sun, Jaesung Choe, Charles Loop, Wei-Chiu Ma, Yu-Chiang Frank Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04459v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, efficient, ar, gaussian splatting, dynamic, 4d  
- **[Monocular Dynamic Gaussian Splatting is Fast and Brittle but Smooth Motion Helps](https://arxiv.org/abs/2412.04457v1)**  
  Authors: Yiqing Liang, Mikhail Okunev, Mikaela Angelina Uy, Runfeng Li, Leonidas Guibas, James Tompkin, Adam W. Harley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04457v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lynl7130.github.io/MonoDyGauBench.github.io/)  
  Keywords: motion, fast, ar, gaussian splatting, dynamic  
- **[PBDyG: Position Based Dynamic Gaussians for Motion-Aware Clothed Human Avatars](https://arxiv.org/abs/2412.04433v1)**  
  Authors: Shota Sasaki, Jane Wu, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04433v1.pdf)  
  Keywords: human, motion, 3d gaussian, ar, deformation, gaussian splatting, dynamic, avatar, body  
- **[EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding](https://arxiv.org/abs/2412.04380v1)**  
  Authors: Yuqi Wu, Wenzhao Zheng, Sicheng Zuo, Yuanhui Huang, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04380v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YkiWu/EmbodiedOcc?style=social)](https://github.com/YkiWu/EmbodiedOcc)  
  Keywords: understanding, human, 3d gaussian, efficient, semantic, ar  
- **[InfiniCube: Unbounded and Controllable Dynamic 3D Driving Scene Generation with World-Guided Video Models](https://arxiv.org/abs/2412.03934v1)**  
  Authors: Yifan Lu, Xuanchi Ren, Jiawei Yang, Tianchang Shen, Zhangjie Wu, Jun Gao, Yue Wang, Siheng Chen, Mike Chen, Sanja Fidler, Jiahui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03934v1.pdf)  
  Keywords: 3d gaussian, dynamic, fast, ar  
- **[Multi-View Pose-Agnostic Change Localization with Zero Labels](https://arxiv.org/abs/2412.03911v1)**  
  Authors: Chamuditha Jayanga Galappaththige, Jason Lai, Lloyd Windrim, Donald Dansereau, Niko Suenderhauf, Dimity Miller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03911v1.pdf)  
  Keywords: lighting, localization, 3d gaussian, ar, gaussian splatting  
- **[DGNS: Deformable Gaussian Splatting and Dynamic Neural Surface for Monocular Dynamic 3D Reconstruction](https://arxiv.org/abs/2412.03910v1)**  
  Authors: Xuesong Li, Jinguang Tong, Jie Hong, Vivien Rolland, Lars Petersson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03910v1.pdf)  
  Keywords: geometry, fast, 3d reconstruction, ar, gaussian splatting, face, dynamic  
- **[HybridGS: Decoupling Transients and Statics with 2D and 3D Gaussian Splatting](https://arxiv.org/abs/2412.03844v1)**  
  Authors: Jingyu Lin, Jiaqi Gu, Lubin Fan, Bojian Wu, Yujing Lou, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03844v1.pdf)  
  Keywords: 3d gaussian, ar, outdoor, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 366 papers*

- **[PBDyG: Position Based Dynamic Gaussians for Motion-Aware Clothed Human Avatars](https://arxiv.org/abs/2412.04433v1)**  
  Authors: Shota Sasaki, Jane Wu, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04433v1.pdf)  
  Keywords: human, motion, 3d gaussian, ar, deformation, gaussian splatting, dynamic, avatar, body  
- **[EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding](https://arxiv.org/abs/2412.04380v1)**  
  Authors: Yuqi Wu, Wenzhao Zheng, Sicheng Zuo, Yuanhui Huang, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04380v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YkiWu/EmbodiedOcc?style=social)](https://github.com/YkiWu/EmbodiedOcc)  
  Keywords: understanding, human, 3d gaussian, efficient, semantic, ar  
- **[DGNS: Deformable Gaussian Splatting and Dynamic Neural Surface for Monocular Dynamic 3D Reconstruction](https://arxiv.org/abs/2412.03910v1)**  
  Authors: Xuesong Li, Jinguang Tong, Jie Hong, Vivien Rolland, Lars Petersson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03910v1.pdf)  
  Keywords: geometry, fast, 3d reconstruction, ar, gaussian splatting, face, dynamic  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: urban scene, ar, semantic, deformation, gaussian splatting, face, dynamic, 4d  
- **[2DGS-Room: Seed-Guided 2D Gaussian Splatting with Geometric Constrains for High-Fidelity Indoor Scene Reconstruction](https://arxiv.org/abs/2412.03428v1)**  
  Authors: Wanting Zhang, Haodong Xiang, Zhichao Liao, Xiansong Lai, Xinghui Li, Long Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03428v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, ar, gaussian splatting, face, dynamic  
- **[Volumetrically Consistent 3D Gaussian Rasterization](https://arxiv.org/abs/2412.03378v1)**  
  Authors: Chinmay Talegaonkar, Yash Belhe, Ravi Ramamoorthi, Nicholas Antipa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03378v1.pdf)  
  Keywords: 3d gaussian, ar, face, gaussian splatting  
- **[Gaussian Splatting Under Attack: Investigating Adversarial Noise in 3D Objects](https://arxiv.org/abs/2412.02803v1)**  
  Authors: Abdurrahman Zeybey, Mehmet Ergezer, Tommy Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02803v1.pdf)  
  Keywords: human, robotics, fast, 3d gaussian, ar, autonomous driving, gaussian splatting  
- **[AniGS: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction](https://arxiv.org/abs/2412.02684v1)**  
  Authors: Lingteng Qiu, Shenhao Zhu, Qi Zuo, Xiaodong Gu, Yuan Dong, Junfei Zhang, Chao Xu, Zhe Li, Weihao Yuan, Liefeng Bo, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02684v1.pdf)  
  Keywords: real-time rendering, animation, human, 3d reconstruction, efficient, ar, gaussian splatting, avatar, 4d  
- **[Towards Rich Emotions in 3D Avatars: A Text-to-3D Avatar Generation Benchmark](https://arxiv.org/abs/2412.02508v1)**  
  Authors: Haidong Xu, Meishan Zhang, Hao Ju, Zhedong Zheng, Hongyuan Zhu, Erik Cambria, Min Zhang, Hao Fei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02508v1.pdf)  
  Keywords: human, motion, mapping, 3d gaussian, ar, dynamic, avatar  
- **[TimeWalker: Personalized Neural Space for Lifelong Head Avatars](https://arxiv.org/abs/2412.02421v1)**  
  Authors: Dongwei Pan, Yang Li, Hongsheng Li, Kwan-Yee Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02421v1.pdf)  
  Keywords: animation, compact, motion, human, ar, head, deformation, gaussian splatting, dynamic, avatar  

### Dynamic Scene

*Showing the latest 50 out of 394 papers*

- **[QUEEN: QUantized Efficient ENcoding of Dynamic Gaussians for Streaming Free-viewpoint Videos](https://arxiv.org/abs/2412.04469v1)**  
  Authors: Sharath Girish, Tianye Li, Amrita Mazumdar, Abhinav Shrivastava, David Luebke, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/queen)  
  Keywords: fast, high quality, 3d gaussian, efficient, ar, gaussian splatting, dynamic  
- **[Sparse Voxels Rasterization: Real-time High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2412.04459v1)**  
  Authors: Cheng Sun, Jaesung Choe, Charles Loop, Wei-Chiu Ma, Yu-Chiang Frank Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04459v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, efficient, ar, gaussian splatting, dynamic, 4d  
- **[Monocular Dynamic Gaussian Splatting is Fast and Brittle but Smooth Motion Helps](https://arxiv.org/abs/2412.04457v1)**  
  Authors: Yiqing Liang, Mikhail Okunev, Mikaela Angelina Uy, Runfeng Li, Leonidas Guibas, James Tompkin, Adam W. Harley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04457v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lynl7130.github.io/MonoDyGauBench.github.io/)  
  Keywords: motion, fast, ar, gaussian splatting, dynamic  
- **[PBDyG: Position Based Dynamic Gaussians for Motion-Aware Clothed Human Avatars](https://arxiv.org/abs/2412.04433v1)**  
  Authors: Shota Sasaki, Jane Wu, Ko Nishino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04433v1.pdf)  
  Keywords: human, motion, 3d gaussian, ar, deformation, gaussian splatting, dynamic, avatar, body  
- **[InfiniCube: Unbounded and Controllable Dynamic 3D Driving Scene Generation with World-Guided Video Models](https://arxiv.org/abs/2412.03934v1)**  
  Authors: Yifan Lu, Xuanchi Ren, Jiawei Yang, Tianchang Shen, Zhangjie Wu, Jun Gao, Yue Wang, Siheng Chen, Mike Chen, Sanja Fidler, Jiahui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03934v1.pdf)  
  Keywords: 3d gaussian, dynamic, fast, ar  
- **[DGNS: Deformable Gaussian Splatting and Dynamic Neural Surface for Monocular Dynamic 3D Reconstruction](https://arxiv.org/abs/2412.03910v1)**  
  Authors: Xuesong Li, Jinguang Tong, Jie Hong, Vivien Rolland, Lars Petersson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03910v1.pdf)  
  Keywords: geometry, fast, 3d reconstruction, ar, gaussian splatting, face, dynamic  
- **[Feed-Forward Bullet-Time Reconstruction of Dynamic Scenes from Monocular Videos](https://arxiv.org/abs/2412.03526v1)**  
  Authors: Hanxue Liang, Jiawei Ren, Ashkan Mirzaei, Antonio Torralba, Ziwei Liu, Igor Gilitschenski, Sanja Fidler, Cengiz Oztireli, Huan Ling, Zan Gojcic, Jiahui Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03526v1.pdf)  
  Keywords: motion, 3d gaussian, ar, gaussian splatting, dynamic  
- **[Dense Scene Reconstruction from Light-Field Images Affected by Rolling Shutter](https://arxiv.org/abs/2412.03518v1)**  
  Authors: Hermes McGriff, Renato Martins, Nicolas Andreff, Cedric Demonceaux  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03518v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ICB-Vision-AI/DenseRSLF?style=social)](https://github.com/ICB-Vision-AI/DenseRSLF)  
  Keywords: ar, motion, deformation  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: urban scene, ar, semantic, deformation, gaussian splatting, face, dynamic, 4d  
- **[2DGS-Room: Seed-Guided 2D Gaussian Splatting with Geometric Constrains for High-Fidelity Indoor Scene Reconstruction](https://arxiv.org/abs/2412.03428v1)**  
  Authors: Wanting Zhang, Haodong Xiang, Zhichao Liao, Xiansong Lai, Xinghui Li, Long Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03428v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, ar, gaussian splatting, face, dynamic  

### Few-shot

*Showing the latest 50 out of 73 papers*

- **[SparseLGS: Sparse View Language Embedded Gaussian Splatting](https://arxiv.org/abs/2412.02245v2)**  
  Authors: Jun Hu, Zhang Chen, Zhong Li, Yi Xu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02245v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ustc3dv.github.io/SparseLGS)  
  Keywords: understanding, sparse view, ar, semantic, gaussian splatting  
- **[How to Use Diffusion Priors under Sparse Views?](https://arxiv.org/abs/2412.02225v1)**  
  Authors: Qisen Wang, Yifan Zhao, Jiawei Ma, Jia Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02225v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iCVTEAM/IPSM?style=social)](https://github.com/iCVTEAM/IPSM)  
  Keywords: sparse view, 3d reconstruction, 3d gaussian, ar, semantic, gaussian splatting, geometry, sparse-view  
- **[SparseGrasp: Robotic Grasping via 3D Semantic Gaussian Splatting from Sparse Multi-View RGB Images](https://arxiv.org/abs/2412.02140v1)**  
  Authors: Junqiu Yu, Xinlin Ren, Yongchong Gu, Haitao Lin, Tianyu Wang, Yi Zhu, Hang Xu, Yu-Gang Jiang, Xiangyang Xue, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02140v1.pdf)  
  Keywords: human, fast, 3d gaussian, efficient, semantic, ar, gaussian splatting, sparse-view  
- **[DynSUP: Dynamic Gaussian Splatting from An Unposed Image Pair](https://arxiv.org/abs/2412.00851v1)**  
  Authors: Weihang Li, Weirong Chen, Shenhan Qian, Jiajie Chen, Daniel Cremers, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00851v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://colin-de.github.io/DynSUP/.)  
  Keywords: high-fidelity, sparse view, motion, 3d gaussian, ar, gaussian splatting, dynamic  
- **[FlashSLAM: Accelerated RGB-D SLAM for Real-Time 3D Scene Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2412.00682v1)**  
  Authors: Phu Pham, Damon Conover, Aniket Bera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00682v1.pdf)  
  Keywords: sparse view, fast, 3d reconstruction, tracking, 3d gaussian, efficient, ar, gaussian splatting, slam  
- **[NovelGS: Consistent Novel-view Denoising via Large Gaussian Reconstruction Model](https://arxiv.org/abs/2411.16779v1)**  
  Authors: Jinpeng Liu, Jiale Xu, Weihao Cheng, Yiming Gao, Xintao Wang, Ying Shan, Yansong Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16779v1.pdf)  
  Keywords: fast, 3d gaussian, ar, gaussian splatting, sparse-view  
- **[GPS-Gaussian+: Generalizable Pixel-wise 3D Gaussian Splatting for Real-Time Human-Scene Rendering from Sparse Views](https://arxiv.org/abs/2411.11363v1)**  
  Authors: Boyao Zhou, Shunyuan Zheng, Hanzhang Tu, Ruizhi Shao, Boning Liu, Shengping Zhang, Liqiang Nie, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.11363v1.pdf)  
  Keywords: sparse view, real-time rendering, human, 3d gaussian, ar, gaussian splatting, geometry, sparse-view  
- **[SPARS3R: Semantic Prior Alignment and Regularization for Sparse 3D Reconstruction](https://arxiv.org/abs/2411.12592v1)**  
  Authors: Yutao Tang, Yuxiang Guo, Deming Li, Cheng Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12592v1.pdf)  
  Keywords: motion, 3d reconstruction, ar, semantic, sparse-view  
- **[4D Gaussian Splatting in the Wild with Uncertainty-Aware Regularization](https://arxiv.org/abs/2411.08879v1)**  
  Authors: Mijeong Kim, Jongwoo Lim, Bohyung Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.08879v1.pdf)  
  Keywords: few-shot, motion, fast, ar, gaussian splatting, dynamic, 4d  
- **[SplatFormer: Point Transformer for Robust 3D Gaussian Splatting](https://arxiv.org/abs/2411.06390v2)**  
  Authors: Yutong Chen, Marko Mihajlovic, Xiyi Chen, Yiming Wang, Sergey Prokudin, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.06390v2.pdf)  
  Keywords: 3d gaussian, ar, sparse view, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 364 papers*

- **[DGNS: Deformable Gaussian Splatting and Dynamic Neural Surface for Monocular Dynamic 3D Reconstruction](https://arxiv.org/abs/2412.03910v1)**  
  Authors: Xuesong Li, Jinguang Tong, Jie Hong, Vivien Rolland, Lars Petersson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03910v1.pdf)  
  Keywords: geometry, fast, 3d reconstruction, ar, gaussian splatting, face, dynamic  
- **[Splats in Splats: Embedding Invisible 3D Watermark within Gaussian Splatting](https://arxiv.org/abs/2412.03121v1)**  
  Authors: Yijia Guo, Wenkai Huang, Yang Li, Gaolei Li, Hang Zhang, Liwen Hu, Jianhua Li, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03121v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://water-gs.github.io.)  
  Keywords: fast, 3d reconstruction, 3d gaussian, efficient, ar, gaussian splatting, mapping  
- **[RoDyGS: Robust Dynamic Gaussian Splatting for Casual Videos](https://arxiv.org/abs/2412.03077v1)**  
  Authors: Yoonwoo Jeong, Junmyeong Lee, Hoseung Choi, Minsu Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03077v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rodygs.github.io/.)  
  Keywords: high-fidelity, geometry, motion, ar, gaussian splatting, dynamic  
- **[AniGS: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction](https://arxiv.org/abs/2412.02684v1)**  
  Authors: Lingteng Qiu, Shenhao Zhu, Qi Zuo, Xiaodong Gu, Yuan Dong, Junfei Zhang, Chao Xu, Zhe Li, Weihao Yuan, Liefeng Bo, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02684v1.pdf)  
  Keywords: real-time rendering, animation, human, 3d reconstruction, efficient, ar, gaussian splatting, avatar, 4d  
- **[Realistic Surgical Simulation from Monocular Videos](https://arxiv.org/abs/2412.02359v1)**  
  Authors: Kailing Wang, Chen Yang, Keyang Zhao, Xiaokang Yang, Wei Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02359v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://namaenashibot.github.io/SurgiSim/.)  
  Keywords: high-fidelity, dynamic, motion, 3d gaussian, ar, deformation, geometry  
- **[GSGTrack: Gaussian Splatting-Guided Object Pose Tracking from RGB Videos](https://arxiv.org/abs/2412.02267v1)**  
  Authors: Zhiyuan Chen, Fan Lu, Guo Yu, Bin Li, Sanqing Qu, Yuan Huang, Changhong Fu, Guang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02267v1.pdf)  
  Keywords: tracking, 3d gaussian, ar, gaussian splatting, geometry  
- **[Multi-robot autonomous 3D reconstruction using Gaussian splatting with Semantic guidance](https://arxiv.org/abs/2412.02249v1)**  
  Authors: Jing Zeng, Qi Ye, Tianle Liu, Yang Xu, Jin Li, Jinming Xu, Liang Li, Jiming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02249v1.pdf)  
  Keywords: high quality, 3d reconstruction, 3d gaussian, ar, semantic, gaussian splatting, face, segmentation  
- **[How to Use Diffusion Priors under Sparse Views?](https://arxiv.org/abs/2412.02225v1)**  
  Authors: Qisen Wang, Yifan Zhao, Jiawei Ma, Jia Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02225v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iCVTEAM/IPSM?style=social)](https://github.com/iCVTEAM/IPSM)  
  Keywords: sparse view, 3d reconstruction, 3d gaussian, ar, semantic, gaussian splatting, geometry, sparse-view  
- **[Gaussian Object Carver: Object-Compositional Gaussian Splatting with surfaces completion](https://arxiv.org/abs/2412.02075v1)**  
  Authors: Liu Liu, Xinjie Wang, Jiaxiong Qiu, Tianwei Lin, Xiaolin Zhou, Zhizhong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02075v1.pdf)  
  Keywords: 3d gaussian, efficient, ar, vr, gaussian splatting, face, geometry  
- **[Planar Gaussian Splatting](https://arxiv.org/abs/2412.01931v1)**  
  Authors: Farhad G. Zanjani, Hong Cai, Hanno Ackermann, Leila Mirvakhabova, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01931v1.pdf)  
  Keywords: neural rendering, fast, ar, gaussian splatting, face, geometry, segmentation  

### Large Scene

*Showing the latest 50 out of 59 papers*

- **[HybridGS: Decoupling Transients and Statics with 2D and 3D Gaussian Splatting](https://arxiv.org/abs/2412.03844v1)**  
  Authors: Jingyu Lin, Jiaqi Gu, Lubin Fan, Bojian Wu, Yujing Lou, Renjie Chen, Ligang Liu, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03844v1.pdf)  
  Keywords: 3d gaussian, ar, outdoor, gaussian splatting  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: urban scene, ar, semantic, deformation, gaussian splatting, face, dynamic, 4d  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: understanding, lighting, localization, nerf, tracking, slam, ar, gaussian splatting, dynamic, mapping, outdoor  
- **[Horizon-GS: Unified 3D Gaussian Splatting for Large-Scale Aerial-to-Ground Scenes](https://arxiv.org/abs/2412.01745v1)**  
  Authors: Lihan Jiang, Kerui Ren, Mulin Yu, Linning Xu, Junting Dong, Tao Lu, Feng Zhao, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01745v1.pdf)  
  Keywords: high-fidelity, urban scene, 3d gaussian, ar, gaussian splatting  
- **[Tortho-Gaussian: Splatting True Digital Orthophoto Maps](https://arxiv.org/abs/2411.19594v1)**  
  Authors: Xin Wang, Wendi Zhang, Hong Xie, Haibin Ai, Qiangqiang Yuan, Zongqian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19594v1.pdf)  
  Keywords: urban scene, 3d gaussian, ar, gaussian splatting, face  
- **[UrbanCAD: Towards Highly Controllable and Photorealistic 3D Vehicles for Urban Scene Simulation](https://arxiv.org/abs/2411.19292v1)**  
  Authors: Yichong Lu, Yichi Cai, Shangzhan Zhang, Hongyu Zhou, Haoji Hu, Huimin Yu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19292v1.pdf)  
  Keywords: lighting, high-fidelity, urban scene, relighting, ar, autonomous driving  
- **[Unleashing the Power of Data Synthesis in Visual Localization](https://arxiv.org/abs/2412.00138v1)**  
  Authors: Sihang Li, Siqi Tan, Bowen Chang, Jing Zhang, Chen Feng, Yiming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00138v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ai4ce.github.io/RAP/)  
  Keywords: localization, robotics, fast, 3d gaussian, ar, dynamic, outdoor  
- **[UniGaussian: Driving Scene Reconstruction from Multiple Camera Models via Unified Gaussian Representations](https://arxiv.org/abs/2411.15355v1)**  
  Authors: Yuan Ren, Guile Wu, Runhao Li, Zheyuan Yang, Yibo Liu, Xingxin Chen, Tongtong Cao, Bingbing Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15355v1.pdf)  
  Keywords: understanding, real-time rendering, urban scene, fast, 3d gaussian, ar, semantic, autonomous driving, gaussian splatting  
- **[LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments](https://arxiv.org/abs/2411.12185v1)**  
  Authors: Renxiang Xiao, Wei Liu, Yushuai Chen, Liang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12185v1.pdf)  
  Keywords: localization, fast, tracking, 3d gaussian, slam, semantic, ar, gaussian splatting, mapping, outdoor, segmentation  
- **[BillBoard Splatting (BBSplat): Learnable Textured Primitives for Novel View Synthesis](https://arxiv.org/abs/2411.08508v2)**  
  Authors: David Svitov, Pietro Morerio, Lourdes Agapito, Alessio Del Bue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.08508v2.pdf)  
  Keywords: compression, nerf, efficient, ar, gaussian splatting, outdoor  

### Model Compression

*Showing the latest 50 out of 390 papers*

- **[Turbo3D: Ultra-fast Text-to-3D Generation](https://arxiv.org/abs/2412.04470v1)**  
  Authors: Hanzhe Hu, Tianwei Yin, Fujun Luan, Yiwei Hu, Hao Tan, Zexiang Xu, Sai Bi, Shubham Tulsiani, Kai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04470v1.pdf)  
  Keywords: efficient, fast, ar, gaussian splatting  
- **[QUEEN: QUantized Efficient ENcoding of Dynamic Gaussians for Streaming Free-viewpoint Videos](https://arxiv.org/abs/2412.04469v1)**  
  Authors: Sharath Girish, Tianye Li, Amrita Mazumdar, Abhinav Shrivastava, David Luebke, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/queen)  
  Keywords: fast, high quality, 3d gaussian, efficient, ar, gaussian splatting, dynamic  
- **[Sparse Voxels Rasterization: Real-time High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2412.04459v1)**  
  Authors: Cheng Sun, Jaesung Choe, Charles Loop, Wei-Chiu Ma, Yu-Chiang Frank Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04459v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, efficient, ar, gaussian splatting, dynamic, 4d  
- **[EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding](https://arxiv.org/abs/2412.04380v1)**  
  Authors: Yuqi Wu, Wenzhao Zheng, Sicheng Zuo, Yuanhui Huang, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04380v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YkiWu/EmbodiedOcc?style=social)](https://github.com/YkiWu/EmbodiedOcc)  
  Keywords: understanding, human, 3d gaussian, efficient, semantic, ar  
- **[Splats in Splats: Embedding Invisible 3D Watermark within Gaussian Splatting](https://arxiv.org/abs/2412.03121v1)**  
  Authors: Yijia Guo, Wenkai Huang, Yang Li, Gaolei Li, Hang Zhang, Liwen Hu, Jianhua Li, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03121v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://water-gs.github.io.)  
  Keywords: fast, 3d reconstruction, 3d gaussian, efficient, ar, gaussian splatting, mapping  
- **[AniGS: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction](https://arxiv.org/abs/2412.02684v1)**  
  Authors: Lingteng Qiu, Shenhao Zhu, Qi Zuo, Xiaodong Gu, Yuan Dong, Junfei Zhang, Chao Xu, Zhe Li, Weihao Yuan, Liefeng Bo, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02684v1.pdf)  
  Keywords: real-time rendering, animation, human, 3d reconstruction, efficient, ar, gaussian splatting, avatar, 4d  
- **[RelayGS: Reconstructing Dynamic Scenes with Large-Scale and Complex Motions via Relay Gaussians](https://arxiv.org/abs/2412.02493v1)**  
  Authors: Qiankun Gao, Yanmin Wu, Chengxiang Wen, Jiarui Meng, Luyang Tang, Jie Chen, Ronggang Wang, Jian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02493v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gqk/RelayGS?style=social)](https://github.com/gqk/RelayGS)  
  Keywords: compact, motion, 3d gaussian, ar, gaussian splatting, dynamic, 4d  
- **[TimeWalker: Personalized Neural Space for Lifelong Head Avatars](https://arxiv.org/abs/2412.02421v1)**  
  Authors: Dongwei Pan, Yang Li, Hongsheng Li, Kwan-Yee Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02421v1.pdf)  
  Keywords: animation, compact, motion, human, ar, head, deformation, gaussian splatting, dynamic, avatar  
- **[SparseGrasp: Robotic Grasping via 3D Semantic Gaussian Splatting from Sparse Multi-View RGB Images](https://arxiv.org/abs/2412.02140v1)**  
  Authors: Junqiu Yu, Xinlin Ren, Yongchong Gu, Haitao Lin, Tianyu Wang, Yi Zhu, Hang Xu, Yu-Gang Jiang, Xiangyang Xue, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02140v1.pdf)  
  Keywords: human, fast, 3d gaussian, efficient, semantic, ar, gaussian splatting, sparse-view  
- **[Gaussian Object Carver: Object-Compositional Gaussian Splatting with surfaces completion](https://arxiv.org/abs/2412.02075v1)**  
  Authors: Liu Liu, Xinjie Wang, Jiaxiong Qiu, Tianwei Lin, Xiaolin Zhou, Zhizhong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02075v1.pdf)  
  Keywords: 3d gaussian, efficient, ar, vr, gaussian splatting, face, geometry  

### Quality Enhancement

*Showing the latest 50 out of 180 papers*

- **[QUEEN: QUantized Efficient ENcoding of Dynamic Gaussians for Streaming Free-viewpoint Videos](https://arxiv.org/abs/2412.04469v1)**  
  Authors: Sharath Girish, Tianye Li, Amrita Mazumdar, Abhinav Shrivastava, David Luebke, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04469v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/amri/projects/queen)  
  Keywords: fast, high quality, 3d gaussian, efficient, ar, gaussian splatting, dynamic  
- **[Sparse Voxels Rasterization: Real-time High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2412.04459v1)**  
  Authors: Cheng Sun, Jaesung Choe, Charles Loop, Wei-Chiu Ma, Yu-Chiang Frank Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04459v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, efficient, ar, gaussian splatting, dynamic, 4d  
- **[2DGS-Room: Seed-Guided 2D Gaussian Splatting with Geometric Constrains for High-Fidelity Indoor Scene Reconstruction](https://arxiv.org/abs/2412.03428v1)**  
  Authors: Wanting Zhang, Haodong Xiang, Zhichao Liao, Xiansong Lai, Xinghui Li, Long Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03428v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, ar, gaussian splatting, face, dynamic  
- **[RoDyGS: Robust Dynamic Gaussian Splatting for Casual Videos](https://arxiv.org/abs/2412.03077v1)**  
  Authors: Yoonwoo Jeong, Junmyeong Lee, Hoseung Choi, Minsu Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03077v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rodygs.github.io/.)  
  Keywords: high-fidelity, geometry, motion, ar, gaussian splatting, dynamic  
- **[Realistic Surgical Simulation from Monocular Videos](https://arxiv.org/abs/2412.02359v1)**  
  Authors: Kailing Wang, Chen Yang, Keyang Zhao, Xiaokang Yang, Wei Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02359v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://namaenashibot.github.io/SurgiSim/.)  
  Keywords: high-fidelity, dynamic, motion, 3d gaussian, ar, deformation, geometry  
- **[Multi-robot autonomous 3D reconstruction using Gaussian splatting with Semantic guidance](https://arxiv.org/abs/2412.02249v1)**  
  Authors: Jing Zeng, Qi Ye, Tianle Liu, Yang Xu, Jin Li, Jinming Xu, Liang Li, Jiming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02249v1.pdf)  
  Keywords: high quality, 3d reconstruction, 3d gaussian, ar, semantic, gaussian splatting, face, segmentation  
- **[HDGS: Textured 2D Gaussian Splatting for Enhanced Scene Rendering](https://arxiv.org/abs/2412.01823v1)**  
  Authors: Yunzhou Song, Heguang Lin, Jiahui Lei, Lingjie Liu, Kostas Daniilidis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01823v1.pdf)  
  Keywords: high-fidelity, neural rendering, ar, gaussian splatting, face, geometry  
- **[Horizon-GS: Unified 3D Gaussian Splatting for Large-Scale Aerial-to-Ground Scenes](https://arxiv.org/abs/2412.01745v1)**  
  Authors: Lihan Jiang, Kerui Ren, Mulin Yu, Linning Xu, Junting Dong, Tao Lu, Feng Zhao, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01745v1.pdf)  
  Keywords: high-fidelity, urban scene, 3d gaussian, ar, gaussian splatting  
- **[Driving Scene Synthesis on Free-form Trajectories with Generative Prior](https://arxiv.org/abs/2412.01717v1)**  
  Authors: Zeyu Yang, Zijie Pan, Yuankun Yang, Xiatian Zhu, Li Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01717v1.pdf)  
  Keywords: face, ar, high-fidelity, gaussian splatting  
- **[Diffusion Models with Anisotropic Gaussian Splatting for Image Inpainting](https://arxiv.org/abs/2412.01682v2)**  
  Authors: Jacob Fein-Ashley, Benjamin Fein-Ashley  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01682v2.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting  

### Ray Tracing

- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v1)**  
  Authors: Lihao Zhang, Haijian Sun, Samuel Berweger, Camillo Gentile, Rose Qingyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v1.pdf)  
  Keywords: 3d gaussian, ar, ray tracing, gaussian splatting  
- **[URAvatar: Universal Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2410.24223v1)**  
  Authors: Junxuan Li, Chen Cao, Gabriel Schwartz, Rawal Khirodkar, Christian Richardt, Tomas Simon, Yaser Sheikh, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24223v1.pdf)  
  Keywords: real-time rendering, human, 3d gaussian, global illumination, efficient, relightable, light transport, head, ar, avatar, illumination  
- **[Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization](https://arxiv.org/abs/2410.16978v1)**  
  Authors: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, Ralf Gutjahr, Daniel Roth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16978v1.pdf)  
  Keywords: understanding, medical, path tracing, efficient, head, ar, vr, gaussian splatting  
- **[GS^3: Efficient Relighting with Triple Gaussian Splatting](https://arxiv.org/abs/2410.11419v1)**  
  Authors: Zoubin Bi, Yixin Zeng, Chong Zeng, Fan Pei, Xiang Feng, Kun Zhou, Hongzhi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11419v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://GSrelight.github.io/.)  
  Keywords: lighting, shadow, global illumination, relighting, efficient, ar, gaussian splatting, geometry, illumination  
- **[RGM: Reconstructing High-fidelity 3D Car Assets with Relightable 3D-GS Generative Model from a Single Image](https://arxiv.org/abs/2410.08181v1)**  
  Authors: Xiaoxue Chen, Jv Zheng, Hao Huang, Haoran Xu, Weihao Gu, Kangliang Chen, He xiang, Huan-ang Gao, Hao Zhao, Guyue Zhou, Yaqin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08181v1.pdf)  
  Keywords: lighting, high-fidelity, nerf, 3d gaussian, relighting, global illumination, relightable, ar, autonomous driving, geometry, illumination  
- **[6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering](https://arxiv.org/abs/2410.04974v2)**  
  Authors: Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04974v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaozhongpai.github.io/6dgs/)  
  Keywords: real-time rendering, nerf, high quality, 3d gaussian, ar, ray tracing, gaussian splatting  
- **[GI-GS: Global Illumination Decomposition on Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2410.02619v1)**  
  Authors: Hongze Chen, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.02619v1.pdf)  
  Keywords: lighting, high-fidelity, shadow, path tracing, lightweight, 3d gaussian, global illumination, relighting, efficient, ar, gaussian splatting, geometry, illumination  
- **[EVER: Exact Volumetric Ellipsoid Rendering for Real-time View Synthesis](https://arxiv.org/abs/2410.01804v5)**  
  Authors: Alexander Mai, Peter Hedman, George Kopanas, Dor Verbin, David Futschik, Qiangeng Xu, Falko Kuester, Jonathan T. Barron, Yinda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.01804v5.pdf)  
  Keywords: nerf, 3d gaussian, ar, ray tracing, gaussian splatting  
- **[SpikeGS: Learning 3D Gaussian Fields from Continuous Spike Stream](https://arxiv.org/abs/2409.15176v5)**  
  Authors: Jinze Yu, Xin Peng, Zhengda Lu, Laurent Kneip, Yiqun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.15176v5.pdf) | [![GitHub](https://img.shields.io/github/stars/520jz/SpikeGS?style=social)](https://github.com/520jz/SpikeGS)  
  Keywords: lighting, real-time rendering, 3d gaussian, ray marching, ar, dynamic, illumination  
- **[CrossRT: A cross platform programming technology for hardware-accelerated ray tracing in CG and CV applications](https://arxiv.org/abs/2409.12617v1)**  
  Authors: Vladimir Frolov, Vadim Sanzharov, Garifullin Albert, Maxim Raenchuk, Alexei Voloboy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.12617v1.pdf)  
  Keywords: nerf, path tracing, 3d gaussian, efficient, ar, ray tracing, gaussian splatting, acceleration, face  

### Relighting

*Showing the latest 50 out of 121 papers*

- **[Multi-View Pose-Agnostic Change Localization with Zero Labels](https://arxiv.org/abs/2412.03911v1)**  
  Authors: Chamuditha Jayanga Galappaththige, Jason Lai, Lloyd Windrim, Donald Dansereau, Niko Suenderhauf, Dimity Miller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03911v1.pdf)  
  Keywords: lighting, localization, 3d gaussian, ar, gaussian splatting  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: understanding, lighting, localization, nerf, tracking, slam, ar, gaussian splatting, dynamic, mapping, outdoor  
- **[HUGSIM: A Real-Time, Photo-Realistic and Closed-Loop Simulator for Autonomous Driving](https://arxiv.org/abs/2412.01718v1)**  
  Authors: Hongyu Zhou, Longzhong Lin, Jiabao Wang, Yichong Lu, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01718v1.pdf)  
  Keywords: lighting, 3d gaussian, ar, autonomous driving, gaussian splatting, dynamic  
- **[Ref-GS: Directional Factorization for 2D Gaussian Splatting](https://arxiv.org/abs/2412.00905v1)**  
  Authors: Youjia Zhang, Anpei Chen, Yumin Wan, Zikai Song, Junqing Yu, Yawei Luo, Wei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00905v1.pdf)  
  Keywords: lighting, efficient, head, ar, gaussian splatting, face, geometry  
- **[A Lesson in Splats: Teacher-Guided Diffusion for 3D Gaussian Splats Generation with 2D Supervision](https://arxiv.org/abs/2412.00623v1)**  
  Authors: Chensheng Peng, Ido Sobol, Masayoshi Tomizuka, Kurt Keutzer, Chenfeng Xu, Or Litany  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00623v1.pdf)  
  Keywords: 3d gaussian, ar, lighting  
- **[UrbanCAD: Towards Highly Controllable and Photorealistic 3D Vehicles for Urban Scene Simulation](https://arxiv.org/abs/2411.19292v1)**  
  Authors: Yichong Lu, Yichi Cai, Shangzhan Zhang, Hongyu Zhou, Haoji Hu, Huimin Yu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19292v1.pdf)  
  Keywords: lighting, high-fidelity, urban scene, relighting, ar, autonomous driving  
- **[InstanceGaussian: Appearance-Semantic Joint Gaussian Representation for 3D Instance-Level Perception](https://arxiv.org/abs/2411.19235v1)**  
  Authors: Haijie Li, Yanmin Wu, Jiarui Meng, Qiankun Gao, Zhiyao Zhang, Ronggang Wang, Jian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19235v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lhj-git.github.io/InstanceGaussian/)  
  Keywords: understanding, lighting, robotics, 3d gaussian, efficient, semantic, ar, autonomous driving, gaussian splatting, segmentation  
- **[SuperGaussians: Enhancing Gaussian Splatting Using Primitives with Spatially Varying Colors](https://arxiv.org/abs/2411.18966v1)**  
  Authors: Rui Xu, Wenyue Chen, Jiepeng Wang, Yuan Liu, Peng Wang, Lin Gao, Shiqing Xin, Taku Komura, Xin Li, Wenping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18966v1.pdf)  
  Keywords: lighting, compact, ar, gaussian splatting, geometry  
- **[NexusSplats: Efficient 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2411.14514v4)**  
  Authors: Yuzhou Tang, Dejun Xu, Yongjie Hou, Zhenzhong Wang, Min Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.14514v4.pdf)  
  Keywords: lighting, 3d gaussian, efficient, ar, gaussian splatting, mapping  
- **[PR-ENDO: Physically Based Relightable Gaussian Splatting for Endoscopy](https://arxiv.org/abs/2411.12510v1)**  
  Authors: Joanna Kaleta, Weronika Smolak-Dyżewska, Dawid Malarz, Diego Dall'Alba, Przemysław Korzeniowski, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12510v1.pdf)  
  Keywords: lighting, 3d gaussian, relighting, ar, relightable, gaussian splatting, illumination  

### SLAM

*Showing the latest 50 out of 158 papers*

- **[Multi-View Pose-Agnostic Change Localization with Zero Labels](https://arxiv.org/abs/2412.03911v1)**  
  Authors: Chamuditha Jayanga Galappaththige, Jason Lai, Lloyd Windrim, Donald Dansereau, Niko Suenderhauf, Dimity Miller  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03911v1.pdf)  
  Keywords: lighting, localization, 3d gaussian, ar, gaussian splatting  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: understanding, lighting, localization, nerf, tracking, slam, ar, gaussian splatting, dynamic, mapping, outdoor  
- **[Splats in Splats: Embedding Invisible 3D Watermark within Gaussian Splatting](https://arxiv.org/abs/2412.03121v1)**  
  Authors: Yijia Guo, Wenkai Huang, Yang Li, Gaolei Li, Hang Zhang, Liwen Hu, Jianhua Li, Tiejun Huang, Lei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03121v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://water-gs.github.io.)  
  Keywords: fast, 3d reconstruction, 3d gaussian, efficient, ar, gaussian splatting, mapping  
- **[Towards Rich Emotions in 3D Avatars: A Text-to-3D Avatar Generation Benchmark](https://arxiv.org/abs/2412.02508v1)**  
  Authors: Haidong Xu, Meishan Zhang, Hao Ju, Zhedong Zheng, Hongyuan Zhu, Erik Cambria, Min Zhang, Hao Fei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02508v1.pdf)  
  Keywords: human, motion, mapping, 3d gaussian, ar, dynamic, avatar  
- **[GSGTrack: Gaussian Splatting-Guided Object Pose Tracking from RGB Videos](https://arxiv.org/abs/2412.02267v1)**  
  Authors: Zhiyuan Chen, Fan Lu, Guo Yu, Bin Li, Sanqing Qu, Yuan Huang, Changhong Fu, Guang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02267v1.pdf)  
  Keywords: tracking, 3d gaussian, ar, gaussian splatting, geometry  
- **[CTRL-D: Controllable Dynamic 3D Scene Editing with Personalized 2D Diffusion](https://arxiv.org/abs/2412.01792v1)**  
  Authors: Kai He, Chin-Hsuan Wu, Igor Gilitschenski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01792v1.pdf)  
  Keywords: tracking, 3d gaussian, ar, gaussian splatting, dynamic  
- **[6DOPE-GS: Online 6D Object Pose Estimation using Gaussian Splatting](https://arxiv.org/abs/2412.01543v1)**  
  Authors: Yufeng Jin, Vignesh Prasad, Snehal Jauhri, Mathias Franzius, Georgia Chalvatzaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01543v1.pdf)  
  Keywords: robotics, fast, tracking, efficient, ar, autonomous driving, gaussian splatting, dynamic  
- **[RGBDS-SLAM: A RGB-D Semantic Dense SLAM Based on 3D Multi Level Pyramid Gaussian Splatting](https://arxiv.org/abs/2412.01217v2)**  
  Authors: Zhenzhong Cao, Chenyang Zhao, Qianyi Zhang, Jinzheng Guang, Yinuo Song Jingtai Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01217v2.pdf) | [![GitHub](https://img.shields.io/github/stars/zhenzhongcao/RGBDS-SLAM?style=social)](https://github.com/zhenzhongcao/RGBDS-SLAM)  
  Keywords: 3d gaussian, ar, semantic, gaussian splatting, slam  
- **[FlashSLAM: Accelerated RGB-D SLAM for Real-Time 3D Scene Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2412.00682v1)**  
  Authors: Phu Pham, Damon Conover, Aniket Bera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00682v1.pdf)  
  Keywords: sparse view, fast, 3d reconstruction, tracking, 3d gaussian, efficient, ar, gaussian splatting, slam  
- **[LineGS : 3D Line Segment Representation on 3D Gaussian Splatting](https://arxiv.org/abs/2412.00477v1)**  
  Authors: Chenggang Yang, Yuang Shi, Wei Tsang Ooi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00477v1.pdf)  
  Keywords: localization, 3d reconstruction, 3d gaussian, efficient, ar, gaussian splatting, face, geometry, mapping  

### Scene Understanding

*Showing the latest 50 out of 185 papers*

- **[EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding](https://arxiv.org/abs/2412.04380v1)**  
  Authors: Yuqi Wu, Wenzhao Zheng, Sicheng Zuo, Yuanhui Huang, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.04380v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YkiWu/EmbodiedOcc?style=social)](https://github.com/YkiWu/EmbodiedOcc)  
  Keywords: understanding, human, 3d gaussian, efficient, semantic, ar  
- **[Urban4D: Semantic-Guided 4D Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473v1)**  
  Authors: Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03473v1.pdf)  
  Keywords: urban scene, ar, semantic, deformation, gaussian splatting, face, dynamic, 4d  
- **[NeRF and Gaussian Splatting SLAM in the Wild](https://arxiv.org/abs/2412.03263v1)**  
  Authors: Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.03263v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iis-esslingen/nerf-3dgs-benchmark?style=social)](https://github.com/iis-esslingen/nerf-3dgs-benchmark)  
  Keywords: understanding, lighting, localization, nerf, tracking, slam, ar, gaussian splatting, dynamic, mapping, outdoor  
- **[Multi-robot autonomous 3D reconstruction using Gaussian splatting with Semantic guidance](https://arxiv.org/abs/2412.02249v1)**  
  Authors: Jing Zeng, Qi Ye, Tianle Liu, Yang Xu, Jin Li, Jinming Xu, Liang Li, Jiming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02249v1.pdf)  
  Keywords: high quality, 3d reconstruction, 3d gaussian, ar, semantic, gaussian splatting, face, segmentation  
- **[SparseLGS: Sparse View Language Embedded Gaussian Splatting](https://arxiv.org/abs/2412.02245v2)**  
  Authors: Jun Hu, Zhang Chen, Zhong Li, Yi Xu, Juyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02245v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ustc3dv.github.io/SparseLGS)  
  Keywords: understanding, sparse view, ar, semantic, gaussian splatting  
- **[How to Use Diffusion Priors under Sparse Views?](https://arxiv.org/abs/2412.02225v1)**  
  Authors: Qisen Wang, Yifan Zhao, Jiawei Ma, Jia Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02225v1.pdf) | [![GitHub](https://img.shields.io/github/stars/iCVTEAM/IPSM?style=social)](https://github.com/iCVTEAM/IPSM)  
  Keywords: sparse view, 3d reconstruction, 3d gaussian, ar, semantic, gaussian splatting, geometry, sparse-view  
- **[SparseGrasp: Robotic Grasping via 3D Semantic Gaussian Splatting from Sparse Multi-View RGB Images](https://arxiv.org/abs/2412.02140v1)**  
  Authors: Junqiu Yu, Xinlin Ren, Yongchong Gu, Haitao Lin, Tianyu Wang, Yi Zhu, Hang Xu, Yu-Gang Jiang, Xiangyang Xue, Yanwei Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02140v1.pdf)  
  Keywords: human, fast, 3d gaussian, efficient, semantic, ar, gaussian splatting, sparse-view  
- **[Planar Gaussian Splatting](https://arxiv.org/abs/2412.01931v1)**  
  Authors: Farhad G. Zanjani, Hong Cai, Hanno Ackermann, Leila Mirvakhabova, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01931v1.pdf)  
  Keywords: neural rendering, fast, ar, gaussian splatting, face, geometry, segmentation  
- **[Occam's LGS: A Simple Approach for Language Gaussian Splatting](https://arxiv.org/abs/2412.01807v1)**  
  Authors: Jiahuan Cheng, Jan-Nico Zaech, Luc Van Gool, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01807v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insait-institute.github.io/OccamLGS/)  
  Keywords: understanding, compression, 3d reconstruction, 3d gaussian, efficient, semantic, ar, gaussian splatting  
- **[3DSceneEditor: Controllable 3D Scene Editing with Gaussian Splatting](https://arxiv.org/abs/2412.01583v1)**  
  Authors: Ziyang Yan, Lei Li, Yihua Shao, Siyu Chen, Wuzong Kai, Jenq-Neng Hwang, Hao Zhao, Fabio Remondino  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01583v1.pdf)  
  Keywords: efficient, semantic, ar, gaussian splatting, segmentation  



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