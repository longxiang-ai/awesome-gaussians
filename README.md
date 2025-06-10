# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-06-10 00:57:48

## Categories

- [3DGS Surveys](#3dgs-surveys) (35 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (535 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1887 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (635 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (714 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (133 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (616 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (110 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (729 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (306 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (41 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (211 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (286 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (339 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, high-fidelity, efficient, 3d reconstruction, segmentation, outdoor, semantic, understanding, neural rendering, survey  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, survey, mapping, nerf, segmentation, semantic, localization, slam, efficient  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: motion, ar, dynamic, gaussian splatting, 3d gaussian, body, 4d, understanding, survey  
- **[A Survey of 3D Reconstruction with Event Cameras](https://arxiv.org/abs/2505.08438v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v2.pdf)  
  Keywords: motion, ar, dynamic, gaussian splatting, 3d gaussian, 3d reconstruction, nerf, illumination, autonomous driving, geometry, robotics, neural rendering, survey  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: ar, gaussian splatting, survey, 3d reconstruction, efficient, fast  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: ar, 3d gaussian, nerf, semantic, autonomous driving, robotics, survey  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: ar, 3d gaussian, 3d reconstruction, lighting, survey  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: ar, gaussian splatting, 3d gaussian, sparse view, 3d reconstruction, nerf, outdoor, face, geometry, understanding, survey  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: ar, gaussian splatting, 3d gaussian, segmentation, semantic, robotics, lighting, survey  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v3)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v3.pdf)  
  Keywords: motion, ar, dynamic, gaussian splatting, 3d gaussian, 3d reconstruction, lighting, survey, fast  

### Acceleration

*Showing the latest 50 out of 535 papers*

- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, large scene, slam, efficient, fast  
- **[Generating Synthetic Stereo Datasets using 3D Gaussian Splatting and Expert Knowledge Transfer](https://arxiv.org/abs/2506.04908v1)**  
  Authors: Filip Slezak, Magnus K. Gjerde, Joakim B. Haurum, Ivan Nikolov, Morten S. Laursen, Thomas B. Moeslund  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04908v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, efficient, nerf, geometry, high-fidelity, fast  
- **[FlexGS: Train Once, Deploy Everywhere with Many-in-One Flexible 3D Gaussian Splatting](https://arxiv.org/abs/2506.04174v1)**  
  Authors: Hengyu Liu, Yuehao Wang, Chenxin Li, Ruisi Cai, Kevin Wang, Wuyang Li, Pavlo Molchanov, Peihao Wang, Zhangyang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04174v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://flexgs.github.io.)  
  Keywords: ar, gaussian splatting, 3d gaussian, nerf, efficient rendering, efficient  
- **[GSCodec Studio: A Modular Framework for Gaussian Splat Compression](https://arxiv.org/abs/2506.01822v1)**  
  Authors: Sicheng Li, Chengzhen Wu, Hao Li, Xiang Gao, Yiyi Liao, Lu Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01822v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JasonLSC/GSCodec_Studio?style=social)](https://github.com/JasonLSC/GSCodec_Studio)  
  Keywords: ar, dynamic, gaussian splatting, 3d gaussian, compression, 4d, real-time rendering, compact  
- **[CountingFruit: Real-Time 3D Fruit Counting with Language-Guided Semantic Gaussian Splatting](https://arxiv.org/abs/2506.01109v1)**  
  Authors: Fengze Li, Yangle Liu, Jieming Ma, Hai-Ning Liang, Yaochun Shen, Huangxiang Li, Zhijing Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01109v1.pdf)  
  Keywords: ar, gaussian splatting, 3d reconstruction, segmentation, efficient rendering, semantic, compact, neural rendering, efficient  
- **[PromptVFX: Text-Driven Fields for Open-World 3D Gaussian Animation](https://arxiv.org/abs/2506.01091v1)**  
  Authors: Mert Kiray, Paul Uhlenbruck, Nassir Navab, Benjamin Busam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01091v1.pdf)  
  Keywords: ar, 3d gaussian, vr, 4d, head, animation, fast  
- **[3D Gaussian Splat Vulnerabilities](https://arxiv.org/abs/2506.00280v1)**  
  Authors: Matthew Hull, Haoyang Yang, Pratham Mehta, Mansi Phute, Aeree Cho, Haoran Wang, Matthew Lau, Wenke Lee, Willian T. Lunardi, Martin Andreoni, Polo Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00280v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, fast  
- **[Adaptive Voxelization for Transform coding of 3D Gaussian splatting data](https://arxiv.org/abs/2506.00271v1)**  
  Authors: Chenjunjie Wang, Shashank N. Sridhara, Eduardo Pavez, Antonio Ortega, Cheng Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00271v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, compression, efficient, fast  
- **[TC-GS: A Faster Gaussian Splatting Module Utilizing Tensor Cores](https://arxiv.org/abs/2505.24796v1)**  
  Authors: Zimu Liao, Jifeng Ding, Rong Fu, Siwei Cui, Ruixuan Gong, Li Wang, Boni Hu, Yi Wang, Hengjie Li, XIngcheng Zhang, Hui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24796v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TensorCore3DGS/3DGSTensorCore?style=social)](https://github.com/TensorCore3DGS/3DGSTensorCore)  
  Keywords: gaussian splatting, 3d gaussian, mapping, compression, acceleration, fast  
- **[GARLIC: GAussian Representation LearnIng for spaCe partitioning](https://arxiv.org/abs/2505.24608v1)**  
  Authors: Panagiotis Rigas, Panagiotis Drivas, Charalambos Tzamos, Ioannis Chamodrakas, George Ioannakis, Leonidas J. Guibas, Ioannis Z. Emiris  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24608v1.pdf)  
  Keywords: ar, gaussian splatting, semantic, efficient, fast  

### Applications

*Showing the latest 50 out of 1887 papers*

- **[BecomingLit: Relightable Gaussian Avatars with Hybrid Neural Shading](https://arxiv.org/abs/2506.06271v1)**  
  Authors: Jonathan Schmidt, Simon Giebenhain, Matthias Niessner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06271v1.pdf)  
  Keywords: ar, dynamic, 3d gaussian, avatar, relightable, illumination, lighting, face, head, relighting  
- **[Dy3DGS-SLAM: Monocular 3D Gaussian Splatting SLAM for Dynamic Environments](https://arxiv.org/abs/2506.05965v1)**  
  Authors: Mingrui Li, Yiming Zhou, Hongxing Zhou, Xinggang Hu, Florian Roemer, Hongyu Wang, Ahmad Osman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05965v1.pdf)  
  Keywords: motion, ar, dynamic, gaussian splatting, 3d gaussian, tracking, mapping, nerf, localization, geometry, slam  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, efficient, 3d reconstruction, geometry, lighting, high-fidelity  
- **[Lumina: Real-Time Mobile Neural Rendering by Exploiting Computational Redundancy](https://arxiv.org/abs/2506.05682v1)**  
  Authors: Yu Feng, Weikai Lin, Yuge Cheng, Zihan Liu, Jingwen Leng, Minyi Guo, Chen Chen, Shixuan Sun, Yuhao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05682v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, head, neural rendering  
- **[VoxelSplat: Dynamic Gaussian Splatting as an Effective Loss for Occupancy and Flow Prediction](https://arxiv.org/abs/2506.05563v1)**  
  Authors: Ziyue Zhu, Shenlong Wang, Jin Xie, Jiang-jiang Liu, Jingdong Wang, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05563v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zzy816.github.io/VoxelSplat-Demo/.)  
  Keywords: motion, ar, dynamic, gaussian splatting, 3d gaussian, semantic  
- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, large scene, slam, efficient, fast  
- **[ODE-GS: Latent ODEs for Dynamic Scene Extrapolation with 3D Gaussian Splatting](https://arxiv.org/abs/2506.05480v1)**  
  Authors: Daniel Wang, Patrick Rim, Tian Tian, Alex Wong, Ganesh Sundaramoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05480v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, 3d gaussian, nerf, deformation, neural rendering, high-fidelity, lightweight  
- **[FreeTimeGS: Free Gaussian Primitives at Anytime and Anywhere for Dynamic Scene Reconstruction](https://arxiv.org/abs/2506.05348v2)**  
  Authors: Yifan Wang, Peishan Yang, Zhen Xu, Jiaming Sun, Zhanhua Zhang, Yong Chen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05348v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/freetimegs/)  
  Keywords: motion, ar, dynamic, 3d gaussian, 4d, deformation  
- **[Revisiting Depth Representations for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2506.05327v1)**  
  Authors: Duochao Shi, Weijie Wang, Donny Y. Chen, Zeyu Zhang, Jia-Wang Bian, Bohan Zhuang, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05327v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aim-uofa.github.io/PMLoss)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry, efficient  
- **[Unifying Appearance Codes and Bilateral Grids for Driving Scene Gaussian Splatting](https://arxiv.org/abs/2506.05280v2)**  
  Authors: Nan Wang, Yuantao Chen, Lixing Xiao, Weiqing Xiao, Bohan Li, Zhaoxi Chen, Chongjie Ye, Shaocong Xu, Saining Zhang, Ziyang Yan, Pierre Merriaux, Lei Lei, Tianfan Xue, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05280v2.pdf)  
  Keywords: ar, dynamic, gaussian splatting, mapping, nerf, autonomous driving, geometry, neural rendering  

### Avatar Generation

*Showing the latest 50 out of 635 papers*

- **[BecomingLit: Relightable Gaussian Avatars with Hybrid Neural Shading](https://arxiv.org/abs/2506.06271v1)**  
  Authors: Jonathan Schmidt, Simon Giebenhain, Matthias Niessner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06271v1.pdf)  
  Keywords: ar, dynamic, 3d gaussian, avatar, relightable, illumination, lighting, face, head, relighting  
- **[Lumina: Real-Time Mobile Neural Rendering by Exploiting Computational Redundancy](https://arxiv.org/abs/2506.05682v1)**  
  Authors: Yu Feng, Weikai Lin, Yuge Cheng, Zihan Liu, Jingwen Leng, Minyi Guo, Chen Chen, Shixuan Sun, Yuhao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05682v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, head, neural rendering  
- **[Synthetic Dataset Generation for Autonomous Mobile Robots Using 3D Gaussian Splatting for Vision Training](https://arxiv.org/abs/2506.05092v1)**  
  Authors: Aneesh Deogan, Wout Beks, Peter Teurlings, Koen de Vos, Mark van den Brand, Rene van de Molengraft  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05092v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, 3d gaussian, human, robotics  
- **[UAV4D: Dynamic Neural Rendering of Human-Centric UAV Imagery using Gaussian Splatting](https://arxiv.org/abs/2506.05011v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Christopher Maxey, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05011v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, human, 4d, neural rendering  
- **[HuGeDiff: 3D Human Generation via Diffusion with Gaussian Splatting](https://arxiv.org/abs/2506.04351v1)**  
  Authors: Maksym Ivashechkin, Oscar Mendez, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04351v1.pdf)  
  Keywords: ar, gaussian splatting, mapping, human, face, efficient  
- **[Pseudo-Simulation for Autonomous Driving](https://arxiv.org/abs/2506.04218v1)**  
  Authors: Wei Cao, Marcel Hallgarten, Tianyu Li, Daniel Dauner, Xunjiang Gu, Caojun Wang, Yakov Miron, Marco Aiello, Hongyang Li, Igor Gilitschenski, Boris Ivanovic, Marco Pavone, Andreas Geiger, Kashyap Chitta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04218v1.pdf) | [![GitHub](https://img.shields.io/github/stars/autonomousvision/navsim?style=social)](https://github.com/autonomousvision/navsim)  
  Keywords: ar, gaussian splatting, 3d gaussian, autonomous driving, head, face, efficient  
- **[JointSplat: Probabilistic Joint Flow-Depth Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2506.03872v1)**  
  Authors: Yang Xiao, Guoan Xu, Qiang Wu, Wenjing Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03872v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, sparse view, efficient, 3d reconstruction, sparse-view, face, high-fidelity  
- **[SplArt: Articulation Estimation and Part-Level Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2506.03594v1)**  
  Authors: Shengjie Lin, Jiading Fang, Muhammad Zubair Irshad, Vitor Campagnolo Guizilini, Rares Andrei Ambrus, Greg Shakhnarovich, Matthew R. Walter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03594v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ripl/splart?style=social)](https://github.com/ripl/splart)  
  Keywords: ar, gaussian splatting, 3d gaussian, segmentation, face, robotics  
- **[Gen4D: Synthesizing Humans and Scenes in the Wild](https://arxiv.org/abs/2506.05397v1)**  
  Authors: Jerrin Bright, Zhibo Wang, Yuhao Chen, Sirisha Rambhatla, John Zelek, David Clausi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05397v1.pdf)  
  Keywords: motion, ar, gaussian splatting, avatar, human, 4d, animation  
- **[Large Processor Chip Model](https://arxiv.org/abs/2506.02929v1)**  
  Authors: Kaiyan Chang, Mingzhi Chen, Yunji Chen, Zhirong Chen, Dongrui Fan, Junfeng Gong, Nan Guo, Yinhe Han, Qinfen Hao, Shuo Hou, Xuan Huang, Pengwei Jin, Changxin Ke, Cangyuan Li, Guangli Li, Huawei Li, Kuan Li, Naipeng Li, Shengwen Liang, Cheng Liu, Hongwei Liu, Jiahua Liu, Junliang Lv, Jianan Mu, Jin Qin, Bin Sun, Chenxi Wang, Duo Wang, Mingjun Wang, Ying Wang, Chenggang Wu, Peiyang Wu, Teng Wu, Xiao Xiao, Mengyao Xie, Chenwei Xiong, Ruiyuan Xu, Mingyu Yan, Xiaochun Ye, Kuai Yu, Rui Zhang, Shuoming Zhang, Jiacheng Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02929v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, human  

### Dynamic Scene

*Showing the latest 50 out of 714 papers*

- **[BecomingLit: Relightable Gaussian Avatars with Hybrid Neural Shading](https://arxiv.org/abs/2506.06271v1)**  
  Authors: Jonathan Schmidt, Simon Giebenhain, Matthias Niessner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06271v1.pdf)  
  Keywords: ar, dynamic, 3d gaussian, avatar, relightable, illumination, lighting, face, head, relighting  
- **[Dy3DGS-SLAM: Monocular 3D Gaussian Splatting SLAM for Dynamic Environments](https://arxiv.org/abs/2506.05965v1)**  
  Authors: Mingrui Li, Yiming Zhou, Hongxing Zhou, Xinggang Hu, Florian Roemer, Hongyu Wang, Ahmad Osman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05965v1.pdf)  
  Keywords: motion, ar, dynamic, gaussian splatting, 3d gaussian, tracking, mapping, nerf, localization, geometry, slam  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, efficient, 3d reconstruction, geometry, lighting, high-fidelity  
- **[VoxelSplat: Dynamic Gaussian Splatting as an Effective Loss for Occupancy and Flow Prediction](https://arxiv.org/abs/2506.05563v1)**  
  Authors: Ziyue Zhu, Shenlong Wang, Jin Xie, Jiang-jiang Liu, Jingdong Wang, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05563v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zzy816.github.io/VoxelSplat-Demo/.)  
  Keywords: motion, ar, dynamic, gaussian splatting, 3d gaussian, semantic  
- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, large scene, slam, efficient, fast  
- **[ODE-GS: Latent ODEs for Dynamic Scene Extrapolation with 3D Gaussian Splatting](https://arxiv.org/abs/2506.05480v1)**  
  Authors: Daniel Wang, Patrick Rim, Tian Tian, Alex Wong, Ganesh Sundaramoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05480v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, 3d gaussian, nerf, deformation, neural rendering, high-fidelity, lightweight  
- **[FreeTimeGS: Free Gaussian Primitives at Anytime and Anywhere for Dynamic Scene Reconstruction](https://arxiv.org/abs/2506.05348v2)**  
  Authors: Yifan Wang, Peishan Yang, Zhen Xu, Jiaming Sun, Zhanhua Zhang, Yong Chen, Hujun Bao, Sida Peng, Xiaowei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05348v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/freetimegs/)  
  Keywords: motion, ar, dynamic, 3d gaussian, 4d, deformation  
- **[Unifying Appearance Codes and Bilateral Grids for Driving Scene Gaussian Splatting](https://arxiv.org/abs/2506.05280v2)**  
  Authors: Nan Wang, Yuantao Chen, Lixing Xiao, Weiqing Xiao, Bohan Li, Zhaoxi Chen, Chongjie Ye, Shaocong Xu, Saining Zhang, Ziyang Yan, Pierre Merriaux, Lei Lei, Tianfan Xue, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05280v2.pdf)  
  Keywords: ar, dynamic, gaussian splatting, mapping, nerf, autonomous driving, geometry, neural rendering  
- **[Synthetic Dataset Generation for Autonomous Mobile Robots Using 3D Gaussian Splatting for Vision Training](https://arxiv.org/abs/2506.05092v1)**  
  Authors: Aneesh Deogan, Wout Beks, Peter Teurlings, Koen de Vos, Mark van den Brand, Rene van de Molengraft  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05092v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, 3d gaussian, human, robotics  
- **[UAV4D: Dynamic Neural Rendering of Human-Centric UAV Imagery using Gaussian Splatting](https://arxiv.org/abs/2506.05011v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Christopher Maxey, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05011v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, human, 4d, neural rendering  

### Few-shot

*Showing the latest 50 out of 133 papers*

- **[JointSplat: Probabilistic Joint Flow-Depth Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2506.03872v1)**  
  Authors: Yang Xiao, Guoan Xu, Qiang Wu, Wenjing Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03872v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, sparse view, efficient, 3d reconstruction, sparse-view, face, high-fidelity  
- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, sparse-view, nerf, geometry, efficient  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, sparse-view, face  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: motion, ar, gaussian splatting, 3d reconstruction, sparse-view, face, fast  
- **[Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse Views by Jointly Training Hemisphere Sampled Synthetic Images](https://arxiv.org/abs/2505.19264v1)**  
  Authors: Guangan Chen, Anh Minh Truong, Hanhe Lin, Michiel Vlaminck, Wilfried Philips, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19264v1.pdf)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, sparse view, sparse-view  
- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: motion, ar, dynamic, gaussian splatting, 3d reconstruction, sparse-view, 4d, compact, head, deformation, efficient  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, sparse-view, robotics, high-fidelity  
- **[X-GRM: Large Gaussian Reconstruction Model for Sparse-view X-rays to Computed Tomography](https://arxiv.org/abs/2505.15235v2)**  
  Authors: Yifan Liu, Wuyang Li, Weihao Yu, Chenxin Li, Alexandre Alahi, Max Meng, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15235v2.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/X-GRM?style=social)](https://github.com/CUHK-AIM-Group/X-GRM)  
  Keywords: sparse-view, gaussian splatting, efficient, ar  
- **[SpatialCrafter: Unleashing the Imagination of Video Diffusion Models for Scene Reconstruction from Limited Observations](https://arxiv.org/abs/2505.11992v1)**  
  Authors: Songchun Zhang, Huiyao Xu, Sitong Guo, Zhongwei Xie, Pengwei Liu, Hujun Bao, Weiwei Xu, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11992v1.pdf)  
  Keywords: ar, 3d gaussian, sparse view, semantic, efficient  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: ar, gaussian splatting, sparse view, shape reconstruction, face, head, geometry, efficient, fast  

### Geometry Reconstruction

*Showing the latest 50 out of 616 papers*

- **[Dy3DGS-SLAM: Monocular 3D Gaussian Splatting SLAM for Dynamic Environments](https://arxiv.org/abs/2506.05965v1)**  
  Authors: Mingrui Li, Yiming Zhou, Hongxing Zhou, Xinggang Hu, Florian Roemer, Hongyu Wang, Ahmad Osman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05965v1.pdf)  
  Keywords: motion, ar, dynamic, gaussian splatting, 3d gaussian, tracking, mapping, nerf, localization, geometry, slam  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, efficient, 3d reconstruction, geometry, lighting, high-fidelity  
- **[Revisiting Depth Representations for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2506.05327v1)**  
  Authors: Duochao Shi, Weijie Wang, Donny Y. Chen, Zeyu Zhang, Jia-Wang Bian, Bohan Zhuang, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05327v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aim-uofa.github.io/PMLoss)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry, efficient  
- **[Unifying Appearance Codes and Bilateral Grids for Driving Scene Gaussian Splatting](https://arxiv.org/abs/2506.05280v2)**  
  Authors: Nan Wang, Yuantao Chen, Lixing Xiao, Weiqing Xiao, Bohan Li, Zhaoxi Chen, Chongjie Ye, Shaocong Xu, Saining Zhang, Ziyang Yan, Pierre Merriaux, Lei Lei, Tianfan Xue, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05280v2.pdf)  
  Keywords: ar, dynamic, gaussian splatting, mapping, nerf, autonomous driving, geometry, neural rendering  
- **[DSG-World: Learning a 3D Gaussian World Model from Dual State Videos](https://arxiv.org/abs/2506.05217v1)**  
  Authors: Wenhao Hu, Xuexiang Wen, Xi Li, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05217v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, 3d reconstruction, segmentation, semantic, robotics, lighting, efficient  
- **[Generating Synthetic Stereo Datasets using 3D Gaussian Splatting and Expert Knowledge Transfer](https://arxiv.org/abs/2506.04908v1)**  
  Authors: Filip Slezak, Magnus K. Gjerde, Joakim B. Haurum, Ivan Nikolov, Morten S. Laursen, Thomas B. Moeslund  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04908v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, efficient, nerf, geometry, high-fidelity, fast  
- **[Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations](https://arxiv.org/abs/2506.04789v1)**  
  Authors: Gaia Di Lorenzo, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04789v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, semantic, localization, geometry, understanding, robotics, high-fidelity  
- **[Splatting Physical Scenes: End-to-End Real-to-Sim from Imperfect Robot Data](https://arxiv.org/abs/2506.04120v1)**  
  Authors: Ben Moran, Mauro Comi, Steven Bohez, Tom Erez, Zhibin Li, Leonard Hasenclever  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04120v1.pdf)  
  Keywords: motion, ar, dynamic, gaussian splatting, 3d gaussian, geometry, high-fidelity  
- **[JointSplat: Probabilistic Joint Flow-Depth Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2506.03872v1)**  
  Authors: Yang Xiao, Guoan Xu, Qiang Wu, Wenjing Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03872v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, sparse view, efficient, 3d reconstruction, sparse-view, face, high-fidelity  
- **[Robust Neural Rendering in the Wild with Asymmetric Dual 3D Gaussian Splatting](https://arxiv.org/abs/2506.03538v1)**  
  Authors: Chengqi Li, Zhihao Shi, Yangdi Lu, Wenbo He, Xiangyu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03538v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, 3d gaussian, 3d reconstruction, geometry, lighting, lightweight, neural rendering  

### Large Scene

*Showing the latest 50 out of 110 papers*

- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, large scene, slam, efficient, fast  
- **[Photoreal Scene Reconstruction from an Egocentric Device](https://arxiv.org/abs/2506.04444v1)**  
  Authors: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04444v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.projectaria.com/photoreal-reconstruction/)  
  Keywords: ar, dynamic, gaussian splatting, outdoor, lighting  
- **[VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians](https://arxiv.org/abs/2506.02741v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02741v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/VTGaussian-SLAM-Project)  
  Keywords: ar, 3d gaussian, tracking, mapping, localization, large scene, geometry, slam, efficient  
- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, 3d gaussian, nerf, efficient rendering, outdoor, real-time rendering, head, efficient  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v2)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v2.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, real-time rendering, geometry, compact, efficient, lightweight, urban scene  
- **[HaloGS: Loose Coupling of Compact Geometry and Gaussian Splats for 3D Scenes](https://arxiv.org/abs/2505.20267v1)**  
  Authors: Changjian Jiang, Kerui Ren, Linning Xu, Jiong Chen, Jiangmiao Pang, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20267v1.pdf)  
  Keywords: ar, 3d reconstruction, outdoor, geometry, compact, lightweight  
- **[VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale Scenes](https://arxiv.org/abs/2505.18992v1)**  
  Authors: Tianchen Deng, Wenhua Wu, Junjie He, Yue Pan, Xirui Jiang, Shenghai Yuan, Danwei Wang, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18992v1.pdf) | [![GitHub](https://img.shields.io/github/stars/dtc111111/vpgs-slam?style=social)](https://github.com/dtc111111/vpgs-slam)  
  Keywords: ar, gaussian splatting, 3d gaussian, tracking, mapping, outdoor, slam, compact  
- **[SplatCo: Structure-View Collaborative Gaussian Splatting for Detail-Preserving Rendering of Large-Scale Unbounded Scenes](https://arxiv.org/abs/2505.17951v1)**  
  Authors: Haihong Xiao, Jianan Zou, Yuxin Zhou, Ying He, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17951v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SCUT-BIP-Lab/SplatCo?style=social)](https://github.com/SCUT-BIP-Lab/SplatCo)  
  Keywords: ar, gaussian splatting, outdoor, face, high-fidelity  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, high-fidelity, efficient, 3d reconstruction, segmentation, outdoor, semantic, understanding, neural rendering, survey  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: ar, gaussian splatting, human, outdoor, face, localization, lighting, lightweight  

### Model Compression

*Showing the latest 50 out of 729 papers*

- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, efficient, 3d reconstruction, geometry, lighting, high-fidelity  
- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, large scene, slam, efficient, fast  
- **[ODE-GS: Latent ODEs for Dynamic Scene Extrapolation with 3D Gaussian Splatting](https://arxiv.org/abs/2506.05480v1)**  
  Authors: Daniel Wang, Patrick Rim, Tian Tian, Alex Wong, Ganesh Sundaramoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05480v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, 3d gaussian, nerf, deformation, neural rendering, high-fidelity, lightweight  
- **[Revisiting Depth Representations for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2506.05327v1)**  
  Authors: Duochao Shi, Weijie Wang, Donny Y. Chen, Zeyu Zhang, Jia-Wang Bian, Bohan Zhuang, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05327v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aim-uofa.github.io/PMLoss)  
  Keywords: ar, gaussian splatting, 3d gaussian, geometry, efficient  
- **[DSG-World: Learning a 3D Gaussian World Model from Dual State Videos](https://arxiv.org/abs/2506.05217v1)**  
  Authors: Wenhao Hu, Xuexiang Wen, Xi Li, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05217v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, 3d reconstruction, segmentation, semantic, robotics, lighting, efficient  
- **[Generating Synthetic Stereo Datasets using 3D Gaussian Splatting and Expert Knowledge Transfer](https://arxiv.org/abs/2506.04908v1)**  
  Authors: Filip Slezak, Magnus K. Gjerde, Joakim B. Haurum, Ivan Nikolov, Morten S. Laursen, Thomas B. Moeslund  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04908v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, efficient, nerf, geometry, high-fidelity, fast  
- **[HuGeDiff: 3D Human Generation via Diffusion with Gaussian Splatting](https://arxiv.org/abs/2506.04351v1)**  
  Authors: Maksym Ivashechkin, Oscar Mendez, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04351v1.pdf)  
  Keywords: ar, gaussian splatting, mapping, human, face, efficient  
- **[Pseudo-Simulation for Autonomous Driving](https://arxiv.org/abs/2506.04218v1)**  
  Authors: Wei Cao, Marcel Hallgarten, Tianyu Li, Daniel Dauner, Xunjiang Gu, Caojun Wang, Yakov Miron, Marco Aiello, Hongyang Li, Igor Gilitschenski, Boris Ivanovic, Marco Pavone, Andreas Geiger, Kashyap Chitta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04218v1.pdf) | [![GitHub](https://img.shields.io/github/stars/autonomousvision/navsim?style=social)](https://github.com/autonomousvision/navsim)  
  Keywords: ar, gaussian splatting, 3d gaussian, autonomous driving, head, face, efficient  
- **[FlexGS: Train Once, Deploy Everywhere with Many-in-One Flexible 3D Gaussian Splatting](https://arxiv.org/abs/2506.04174v1)**  
  Authors: Hengyu Liu, Yuehao Wang, Chenxin Li, Ruisi Cai, Kevin Wang, Wuyang Li, Pavlo Molchanov, Peihao Wang, Zhangyang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04174v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://flexgs.github.io.)  
  Keywords: ar, gaussian splatting, 3d gaussian, nerf, efficient rendering, efficient  
- **[JointSplat: Probabilistic Joint Flow-Depth Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2506.03872v1)**  
  Authors: Yang Xiao, Guoan Xu, Qiang Wu, Wenjing Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03872v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, sparse view, efficient, 3d reconstruction, sparse-view, face, high-fidelity  

### Quality Enhancement

*Showing the latest 50 out of 306 papers*

- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, efficient, 3d reconstruction, geometry, lighting, high-fidelity  
- **[ODE-GS: Latent ODEs for Dynamic Scene Extrapolation with 3D Gaussian Splatting](https://arxiv.org/abs/2506.05480v1)**  
  Authors: Daniel Wang, Patrick Rim, Tian Tian, Alex Wong, Ganesh Sundaramoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05480v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, 3d gaussian, nerf, deformation, neural rendering, high-fidelity, lightweight  
- **[DSG-World: Learning a 3D Gaussian World Model from Dual State Videos](https://arxiv.org/abs/2506.05217v1)**  
  Authors: Wenhao Hu, Xuexiang Wen, Xi Li, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05217v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, 3d reconstruction, segmentation, semantic, robotics, lighting, efficient  
- **[Generating Synthetic Stereo Datasets using 3D Gaussian Splatting and Expert Knowledge Transfer](https://arxiv.org/abs/2506.04908v1)**  
  Authors: Filip Slezak, Magnus K. Gjerde, Joakim B. Haurum, Ivan Nikolov, Morten S. Laursen, Thomas B. Moeslund  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04908v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, efficient, nerf, geometry, high-fidelity, fast  
- **[Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations](https://arxiv.org/abs/2506.04789v1)**  
  Authors: Gaia Di Lorenzo, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04789v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, semantic, localization, geometry, understanding, robotics, high-fidelity  
- **[Splatting Physical Scenes: End-to-End Real-to-Sim from Imperfect Robot Data](https://arxiv.org/abs/2506.04120v1)**  
  Authors: Ben Moran, Mauro Comi, Steven Bohez, Tom Erez, Zhibin Li, Leonard Hasenclever  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04120v1.pdf)  
  Keywords: motion, ar, dynamic, gaussian splatting, 3d gaussian, geometry, high-fidelity  
- **[JointSplat: Probabilistic Joint Flow-Depth Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2506.03872v1)**  
  Authors: Yang Xiao, Guoan Xu, Qiang Wu, Wenjing Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03872v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, sparse view, efficient, 3d reconstruction, sparse-view, face, high-fidelity  
- **[RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes](https://arxiv.org/abs/2506.01379v1)**  
  Authors: Pou-Chun Kung, Skanda Harisha, Ram Vasudevan, Aline Eid, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01379v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/radarsplat.)  
  Keywords: ar, gaussian splatting, 3d reconstruction, reflection, autonomous driving, high-fidelity  
- **[Globally Consistent RGB-D SLAM with 2D Gaussian Splatting](https://arxiv.org/abs/2506.00970v1)**  
  Authors: Xingguang Zhong, Yue Pan, Liren Jin, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00970v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, tracking, high-fidelity, 3d reconstruction, mapping, face, localization, slam, efficient  
- **[AdaHuman: Animatable Detailed 3D Human Generation with Compositional Multiview Diffusion](https://arxiv.org/abs/2505.24877v1)**  
  Authors: Yangyi Huang, Ye Yuan, Xueting Li, Jan Kautz, Umar Iqbal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24877v1.pdf)  
  Keywords: motion, ar, 3d gaussian, avatar, body, human, high-fidelity, animation  

### Ray Tracing

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: relighting, ar, gaussian splatting, 3d gaussian, relightable, illumination, human, lighting, face, shadow, geometry, neural rendering, high-fidelity, ray tracing  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: ar, gaussian splatting, avatar, relightable, human, lighting, shadow, geometry, relighting, ray tracing, fast  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, acceleration, lighting, efficient rendering, relighting, efficient, ray tracing  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: ar, dynamic, gaussian splatting, 3d gaussian, ray marching, acceleration, compact, efficient, animation  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: ar, gaussian splatting, 3d gaussian, global illumination, illumination, real-time rendering, face, lighting, efficient, ray tracing  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: dynamic, 3d gaussian, light transport, global illumination, illumination, real-time rendering, face, lighting, fast  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, reflection, shadow, neural rendering, ray tracing, fast  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: ar, dynamic, tracking, relightable, 4d, real-time rendering, face, geometry, lighting, efficient, ray tracing  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: gaussian splatting, reflection, lighting, face, shadow, ray tracing  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, survey, ray tracing  

### Relighting

*Showing the latest 50 out of 211 papers*

- **[BecomingLit: Relightable Gaussian Avatars with Hybrid Neural Shading](https://arxiv.org/abs/2506.06271v1)**  
  Authors: Jonathan Schmidt, Simon Giebenhain, Matthias Niessner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06271v1.pdf)  
  Keywords: ar, dynamic, 3d gaussian, avatar, relightable, illumination, lighting, face, head, relighting  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, efficient, 3d reconstruction, geometry, lighting, high-fidelity  
- **[DSG-World: Learning a 3D Gaussian World Model from Dual State Videos](https://arxiv.org/abs/2506.05217v1)**  
  Authors: Wenhao Hu, Xuexiang Wen, Xi Li, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05217v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, 3d reconstruction, segmentation, semantic, robotics, lighting, efficient  
- **[Photoreal Scene Reconstruction from an Egocentric Device](https://arxiv.org/abs/2506.04444v1)**  
  Authors: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04444v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.projectaria.com/photoreal-reconstruction/)  
  Keywords: ar, dynamic, gaussian splatting, outdoor, lighting  
- **[Robust Neural Rendering in the Wild with Asymmetric Dual 3D Gaussian Splatting](https://arxiv.org/abs/2506.03538v1)**  
  Authors: Chengqi Li, Zhihao Shi, Yangdi Lu, Wenbo He, Xiangyu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03538v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, 3d gaussian, 3d reconstruction, geometry, lighting, lightweight, neural rendering  
- **[RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes](https://arxiv.org/abs/2506.01379v1)**  
  Authors: Pou-Chun Kung, Skanda Harisha, Ram Vasudevan, Aline Eid, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01379v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/radarsplat.)  
  Keywords: ar, gaussian splatting, 3d reconstruction, reflection, autonomous driving, high-fidelity  
- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: relighting, ar, gaussian splatting, 3d gaussian, relightable, illumination, human, lighting, face, shadow, geometry, neural rendering, high-fidelity, ray tracing  
- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: ar, 3d gaussian, mapping, illumination, shadow, lighting, efficient  
- **[WeatherEdit: Controllable Weather Editing with 4D Gaussian Field](https://arxiv.org/abs/2505.20471v1)**  
  Authors: Chenghao Qian, Wenjing Li, Yuhu Guo, Gustav Markkula  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jumponthemoon.github.io/w-edit)  
  Keywords: ar, dynamic, 4d, autonomous driving, lighting  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: ar, gaussian splatting, human, outdoor, face, localization, lighting, lightweight  

### SLAM

*Showing the latest 50 out of 286 papers*

- **[Dy3DGS-SLAM: Monocular 3D Gaussian Splatting SLAM for Dynamic Environments](https://arxiv.org/abs/2506.05965v1)**  
  Authors: Mingrui Li, Yiming Zhou, Hongxing Zhou, Xinggang Hu, Florian Roemer, Hongyu Wang, Ahmad Osman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05965v1.pdf)  
  Keywords: motion, ar, dynamic, gaussian splatting, 3d gaussian, tracking, mapping, nerf, localization, geometry, slam  
- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, large scene, slam, efficient, fast  
- **[Unifying Appearance Codes and Bilateral Grids for Driving Scene Gaussian Splatting](https://arxiv.org/abs/2506.05280v2)**  
  Authors: Nan Wang, Yuantao Chen, Lixing Xiao, Weiqing Xiao, Bohan Li, Zhaoxi Chen, Chongjie Ye, Shaocong Xu, Saining Zhang, Ziyang Yan, Pierre Merriaux, Lei Lei, Tianfan Xue, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05280v2.pdf)  
  Keywords: ar, dynamic, gaussian splatting, mapping, nerf, autonomous driving, geometry, neural rendering  
- **[Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations](https://arxiv.org/abs/2506.04789v1)**  
  Authors: Gaia Di Lorenzo, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04789v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, semantic, localization, geometry, understanding, robotics, high-fidelity  
- **[HuGeDiff: 3D Human Generation via Diffusion with Gaussian Splatting](https://arxiv.org/abs/2506.04351v1)**  
  Authors: Maksym Ivashechkin, Oscar Mendez, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04351v1.pdf)  
  Keywords: ar, gaussian splatting, mapping, human, face, efficient  
- **[LEG-SLAM: Real-Time Language-Enhanced Gaussian Splatting for SLAM](https://arxiv.org/abs/2506.03073v1)**  
  Authors: Roman Titkov, Egor Zubkov, Dmitry Yudin, Jaafar Mahmoud, Malik Mohrat, Gennady Sidorov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03073v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://titrom025.github.io/LEG-SLAM/)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, mapping, semantic, localization, slam, robotics  
- **[VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians](https://arxiv.org/abs/2506.02741v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02741v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/VTGaussian-SLAM-Project)  
  Keywords: ar, 3d gaussian, tracking, mapping, localization, large scene, geometry, slam, efficient  
- **[WoMAP: World Models For Embodied Open-Vocabulary Object Localization](https://arxiv.org/abs/2506.01600v1)**  
  Authors: Tenny Yin, Zhiting Mei, Tao Sun, Lihan Zha, Emily Zhou, Jeremy Bao, Miyu Yamane, Ola Shorinwa, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01600v1.pdf)  
  Keywords: ar, dynamic, gaussian splatting, localization, efficient  
- **[Globally Consistent RGB-D SLAM with 2D Gaussian Splatting](https://arxiv.org/abs/2506.00970v1)**  
  Authors: Xingguang Zhong, Yue Pan, Liren Jin, Marija Popović, Jens Behley, Cyrill Stachniss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00970v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, tracking, high-fidelity, 3d reconstruction, mapping, face, localization, slam, efficient  
- **[Understanding while Exploring: Semantics-driven Active Mapping](https://arxiv.org/abs/2506.00225v1)**  
  Authors: Liyan Chen, Huangying Zhan, Hairong Yin, Yi Xu, Philippos Mordohai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00225v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, mapping, semantic, geometry, understanding, efficient  

### Scene Understanding

*Showing the latest 50 out of 339 papers*

- **[VoxelSplat: Dynamic Gaussian Splatting as an Effective Loss for Occupancy and Flow Prediction](https://arxiv.org/abs/2506.05563v1)**  
  Authors: Ziyue Zhu, Shenlong Wang, Jin Xie, Jiang-jiang Liu, Jingdong Wang, Jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05563v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zzy816.github.io/VoxelSplat-Demo/.)  
  Keywords: motion, ar, dynamic, gaussian splatting, 3d gaussian, semantic  
- **[DSG-World: Learning a 3D Gaussian World Model from Dual State Videos](https://arxiv.org/abs/2506.05217v1)**  
  Authors: Wenhao Hu, Xuexiang Wen, Xi Li, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05217v1.pdf)  
  Keywords: ar, 3d gaussian, high-fidelity, 3d reconstruction, segmentation, semantic, robotics, lighting, efficient  
- **[Point Cloud Segmentation of Agricultural Vehicles using 3D Gaussian Splatting](https://arxiv.org/abs/2506.05009v1)**  
  Authors: Alfred T. Christiansen, Andreas H. Højrup, Morten K. Stephansen, Md Ibtihaj A. Sakib, Taman S. Poojary, Filip Slezak, Morten S. Laursen, Thomas B. Moeslund, Joakim B. Haurum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05009v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, segmentation, semantic  
- **[Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations](https://arxiv.org/abs/2506.04789v1)**  
  Authors: Gaia Di Lorenzo, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04789v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, semantic, localization, geometry, understanding, robotics, high-fidelity  
- **[SplArt: Articulation Estimation and Part-Level Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2506.03594v1)**  
  Authors: Shengjie Lin, Jiading Fang, Muhammad Zubair Irshad, Vitor Campagnolo Guizilini, Rares Andrei Ambrus, Greg Shakhnarovich, Matthew R. Walter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03594v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ripl/splart?style=social)](https://github.com/ripl/splart)  
  Keywords: ar, gaussian splatting, 3d gaussian, segmentation, face, robotics  
- **[LEG-SLAM: Real-Time Language-Enhanced Gaussian Splatting for SLAM](https://arxiv.org/abs/2506.03073v1)**  
  Authors: Roman Titkov, Egor Zubkov, Dmitry Yudin, Jaafar Mahmoud, Malik Mohrat, Gennady Sidorov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03073v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://titrom025.github.io/LEG-SLAM/)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, mapping, semantic, localization, slam, robotics  
- **[RobustSplat: Decoupling Densification and Dynamics for Transient-Free 3DGS](https://arxiv.org/abs/2506.02751v1)**  
  Authors: Chuanyu Fu, Yuqi Zhang, Kunbin Yao, Guanying Chen, Yuan Xiong, Chuan Huang, Shuguang Cui, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02751v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fcyycf.github.io/RobustSplat/.)  
  Keywords: ar, dynamic, gaussian splatting, 3d gaussian, semantic  
- **[CountingFruit: Real-Time 3D Fruit Counting with Language-Guided Semantic Gaussian Splatting](https://arxiv.org/abs/2506.01109v1)**  
  Authors: Fengze Li, Yangle Liu, Jieming Ma, Hai-Ning Liang, Yaochun Shen, Huangxiang Li, Zhijing Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01109v1.pdf)  
  Keywords: ar, gaussian splatting, 3d reconstruction, segmentation, efficient rendering, semantic, compact, neural rendering, efficient  
- **[Understanding while Exploring: Semantics-driven Active Mapping](https://arxiv.org/abs/2506.00225v1)**  
  Authors: Liyan Chen, Huangying Zhan, Hairong Yin, Yi Xu, Philippos Mordohai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.00225v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, mapping, semantic, geometry, understanding, efficient  
- **[Tackling View-Dependent Semantics in 3D Language Gaussian Splatting](https://arxiv.org/abs/2505.24746v1)**  
  Authors: Jiazhong Cen, Xudong Zhou, Jiemin Fang, Changsong Wen, Lingxi Xie, Xiaopeng Zhang, Wei Shen, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.24746v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SJTU-DeepVisionLab/LaGa?style=social)](https://github.com/SJTU-DeepVisionLab/LaGa)  
  Keywords: ar, gaussian splatting, 3d gaussian, semantic, understanding  



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