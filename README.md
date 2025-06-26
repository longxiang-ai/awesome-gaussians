# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-06-26 03:03:12

## Categories

- [3DGS Surveys](#3dgs-surveys) (19 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (276 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (332 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (382 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (75 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (313 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (61 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (395 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (163 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (18 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (106 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (158 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (183 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: high-fidelity, survey, 3d gaussian, gaussian splatting, dynamic, efficient, face, autonomous driving, nerf, outdoor, ar  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: neural rendering, high-fidelity, survey, 3d gaussian, gaussian splatting, vr, autonomous driving, ar, nerf, robotics, 3d reconstruction  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: neural rendering, high-fidelity, survey, 3d gaussian, gaussian splatting, efficient, semantic, segmentation, ar, outdoor, 3d reconstruction, understanding  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, efficient, mapping, segmentation, ar, slam, nerf, semantic, localization  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to
  Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: understanding, survey, 3d gaussian, dynamic, gaussian splatting, 4d, body, ar, motion  
- **[A Survey of 3D Reconstruction with Event Cameras](https://arxiv.org/abs/2505.08438v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v2.pdf)  
  Keywords: neural rendering, illumination, survey, 3d gaussian, gaussian splatting, dynamic, autonomous driving, ar, geometry, nerf, robotics, 3d reconstruction, motion  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: fast, survey, gaussian splatting, efficient, ar, 3d reconstruction  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: survey, 3d gaussian, ar, lighting, 3d reconstruction  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From
  Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting
  (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, face, ar, geometry, nerf, outdoor, sparse view, 3d reconstruction, understanding  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, segmentation, ar, lighting, robotics, semantic  

### Acceleration

*Showing the latest 50 out of 276 papers*

- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, efficient, ray tracing, real-time rendering, ar  
- **[Virtual Memory for 3D Gaussian Splatting](https://arxiv.org/abs/2506.19415v1)**  
  Authors: Jonathan Haberl, Philipp Fleck, Clemens Arth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19415v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, efficient, real-time rendering, ar  
- **[3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D
  Gaussian-Splatting](https://arxiv.org/abs/2506.14642v1)**  
  Authors: Yuke Xing, Jiarui Wang, Peizhi Niu, Wenjie Huang, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14642v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, compression, real-time rendering, human, ar  
- **[GS-2DGS: Geometrically Supervised 2DGS for Reflective Object
  Reconstruction](https://arxiv.org/abs/2506.13110v1)**  
  Authors: Jinguang Tong, Xuesong li, Fahira Afzal Maken, Sundaram Muthu, Lars Petersson, Chuong Nguyen, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13110v1.pdf)  
  Keywords: fast, 3d gaussian, gaussian splatting, face, relighting, real-time rendering, lighting, ar  
- **[Rasterizing Wireless Radiance Field via Deformable 2D Gaussian Splatting](https://arxiv.org/abs/2506.12787v2)**  
  Authors: Mufan Liu, Cixiao Zhang, Qi Yang, Yujie Cao, Yiling Xu, Yin Xu, Shu Sun, Mingzeng Dai, Yunfeng Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12787v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://evan-sudo.github.io/swiftwrf/.)  
  Keywords: fast, gaussian splatting, localization, lightweight, deformation, nerf, ar, compact  
- **[HAIF-GS: Hierarchical and Induced Flow-Guided Gaussian Splatting for
  Dynamic Scene](https://arxiv.org/abs/2506.09518v1)**  
  Authors: Jianing Chen, Zehao Li, Yujun Cai, Hao Jiang, Chengxuan Qian, Juyuan Kang, Shuqin Gao, Honglong Zhao, Tianlu Mao, Yucheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09518v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, efficient, deformation, real-time rendering, ar, motion  
- **[ODG: Occupancy Prediction Using Dual Gaussians](https://arxiv.org/abs/2506.09417v2)**  
  Authors: Yunxiao Shi, Yinhao Zhu, Shizhong Han, Jisoo Jeong, Amin Ansari, Hong Cai, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09417v2.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, autonomous driving, ar, geometry, real-time rendering, semantic  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language
  Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: fast, 3d gaussian, gaussian splatting, efficient, segmentation, ar, geometry, outdoor, semantic, understanding  
- **[Speedy Deformable 3D Gaussian Splatting: Fast Rendering and Compression
  of Dynamic Scenes](https://arxiv.org/abs/2506.07917v1)**  
  Authors: Allen Tu, Haiyang Ying, Alex Hanson, Yonghan Lee, Tom Goldstein, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07917v1.pdf)  
  Keywords: fast, vr, 3d gaussian, dynamic, gaussian splatting, compression, deformation, nerf, 4d, ar, motion  
- **[PIG: Physically-based Multi-Material Interaction with 3D Gaussians](https://arxiv.org/abs/2506.07657v1)**  
  Authors: Zeyu Xiao, Zhenyi Wu, Mingyang Sun, Qipeng Yan, Yufan Guo, Zhuoer Liang, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07657v1.pdf)  
  Keywords: fast, 3d gaussian, dynamic, gaussian splatting, mapping, segmentation, deformation, ar  

### Applications

*Showing the latest 50 out of 995 papers*

- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, efficient, ray tracing, real-time rendering, ar  
- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: understanding, dynamic, gaussian splatting, deformation, body, ar, motion  
- **[Virtual Memory for 3D Gaussian Splatting](https://arxiv.org/abs/2506.19415v1)**  
  Authors: Jonathan Haberl, Philipp Fleck, Clemens Arth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19415v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, efficient, real-time rendering, ar  
- **[HoliGS: Holistic Gaussian Splatting for Embodied View Synthesis](https://arxiv.org/abs/2506.19291v1)**  
  Authors: Xiaoyuan Wang, Yizhou Zhao, Botao Ye, Xiaojun Shan, Weijie Lyu, Lu Qi, Kelvin C. K. Chan, Yinxiao Li, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19291v1.pdf)  
  Keywords: dynamic, gaussian splatting, deformation, nerf, 4d, ar, head  
- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, tracking, slam, outdoor, ar  
- **[ViDAR: Video Diffusion-Aware 4D Reconstruction From Monocular Inputs](https://arxiv.org/abs/2506.18792v1)**  
  Authors: Michal Nazarczuk, Sibi Catley-Chandar, Thomas Tanay, Zhensong Zhang, Gregory Slabaugh, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18792v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vidar-4d.github.io)  
  Keywords: dynamic, gaussian splatting, geometry, 4d, ar, motion  
- **[3D Arena: An Open Platform for Generative 3D Evaluation](https://arxiv.org/abs/2506.18787v1)**  
  Authors: Dylan Ebert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18787v1.pdf)  
  Keywords: ar, understanding, human  
- **[Reconstructing Tornadoes in 3D with Gaussian Splatting](https://arxiv.org/abs/2506.18677v1)**  
  Authors: Adam Yang, Nadula Kadawedduwa, Tianfu Wang, Maria Molina, Christopher Metzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18677v1.pdf)  
  Keywords: ar, understanding, 3d gaussian, gaussian splatting  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: high-fidelity, survey, 3d gaussian, gaussian splatting, dynamic, efficient, face, autonomous driving, nerf, outdoor, ar  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: neural rendering, high-fidelity, survey, 3d gaussian, gaussian splatting, vr, autonomous driving, ar, nerf, robotics, 3d reconstruction  

### Avatar Generation

*Showing the latest 50 out of 332 papers*

- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: understanding, dynamic, gaussian splatting, deformation, body, ar, motion  
- **[HoliGS: Holistic Gaussian Splatting for Embodied View Synthesis](https://arxiv.org/abs/2506.19291v1)**  
  Authors: Xiaoyuan Wang, Yizhou Zhao, Botao Ye, Xiaojun Shan, Weijie Lyu, Lu Qi, Kelvin C. K. Chan, Yinxiao Li, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19291v1.pdf)  
  Keywords: dynamic, gaussian splatting, deformation, nerf, 4d, ar, head  
- **[3D Arena: An Open Platform for Generative 3D Evaluation](https://arxiv.org/abs/2506.18787v1)**  
  Authors: Dylan Ebert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18787v1.pdf)  
  Keywords: ar, understanding, human  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: high-fidelity, survey, 3d gaussian, gaussian splatting, dynamic, efficient, face, autonomous driving, nerf, outdoor, ar  
- **[Information-computation trade-offs in non-linear transforms](https://arxiv.org/abs/2506.15948v1)**  
  Authors: Connor Ding, Abhiram Rao Gorle, Jiwon Jeong, Naomi Sagan, Tsachy Weissman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15948v1.pdf)  
  Keywords: dynamic, gaussian splatting, efficient, compression, human, ar, compact  
- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads
  Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: high-fidelity, dynamic, gaussian splatting, face, efficient, ar, head  
- **[3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D
  Gaussian-Splatting](https://arxiv.org/abs/2506.14642v1)**  
  Authors: Yuke Xing, Jiarui Wang, Peizhi Niu, Wenjie Huang, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14642v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, compression, real-time rendering, human, ar  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty
  Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: neural rendering, 3d gaussian, gaussian splatting, efficient, lightweight, mapping, ar, nerf, 3d reconstruction, head  
- **[HRGS: Hierarchical Gaussian Splatting for Memory-Efficient
  High-Resolution 3D Reconstruction](https://arxiv.org/abs/2506.14229v1)**  
  Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Juan Zhang, Tongfei Chen, Shuo Yang, Shuwei Shao, Wenhao Dong, Baochang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14229v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, face, efficient, ar, 3d reconstruction  
- **[GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with
  Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2506.14009v1)**  
  Authors: Qianzhong Chen, Naixiang Gao, Suning Huang, JunEn Low, Timothy Chen, Jiankai Sun, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14009v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, efficient, lightweight, ar, head, compact  

### Dynamic Scene

*Showing the latest 50 out of 382 papers*

- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: understanding, dynamic, gaussian splatting, deformation, body, ar, motion  
- **[Virtual Memory for 3D Gaussian Splatting](https://arxiv.org/abs/2506.19415v1)**  
  Authors: Jonathan Haberl, Philipp Fleck, Clemens Arth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19415v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, efficient, real-time rendering, ar  
- **[HoliGS: Holistic Gaussian Splatting for Embodied View Synthesis](https://arxiv.org/abs/2506.19291v1)**  
  Authors: Xiaoyuan Wang, Yizhou Zhao, Botao Ye, Xiaojun Shan, Weijie Lyu, Lu Qi, Kelvin C. K. Chan, Yinxiao Li, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19291v1.pdf)  
  Keywords: dynamic, gaussian splatting, deformation, nerf, 4d, ar, head  
- **[ViDAR: Video Diffusion-Aware 4D Reconstruction From Monocular Inputs](https://arxiv.org/abs/2506.18792v1)**  
  Authors: Michal Nazarczuk, Sibi Catley-Chandar, Thomas Tanay, Zhensong Zhang, Gregory Slabaugh, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18792v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vidar-4d.github.io)  
  Keywords: dynamic, gaussian splatting, geometry, 4d, ar, motion  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: high-fidelity, survey, 3d gaussian, gaussian splatting, dynamic, efficient, face, autonomous driving, nerf, outdoor, ar  
- **[Information-computation trade-offs in non-linear transforms](https://arxiv.org/abs/2506.15948v1)**  
  Authors: Connor Ding, Abhiram Rao Gorle, Jiwon Jeong, Naomi Sagan, Tsachy Weissman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15948v1.pdf)  
  Keywords: dynamic, gaussian splatting, efficient, compression, human, ar, compact  
- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from
  RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: dynamic, gaussian splatting, sparse-view, ar, motion  
- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads
  Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: high-fidelity, dynamic, gaussian splatting, face, efficient, ar, head  
- **[GAF: Gaussian Action Field as a Dynamic World Model for Robotic
  Manipulation](https://arxiv.org/abs/2506.14135v2)**  
  Authors: Ying Chai, Litao Deng, Ruizhi Shao, Jiajun Zhang, Liangjun Xing, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14135v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://chaiying1.github.io/GAF.github.io/project_page/)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, geometry, 4d, ar, motion  
- **[GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with
  Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2506.14009v1)**  
  Authors: Qianzhong Chen, Naixiang Gao, Suning Huang, JunEn Low, Timothy Chen, Jiankai Sun, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14009v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, efficient, lightweight, ar, head, compact  

### Few-shot

*Showing the latest 50 out of 75 papers*

- **[Particle-Grid Neural Dynamics for Learning Deformable Object Models from
  RGB-D Videos](https://arxiv.org/abs/2506.15680v1)**  
  Authors: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15680v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kywind.github.io/pgnd)  
  Keywords: dynamic, gaussian splatting, sparse-view, ar, motion  
- **[PointGS: Point Attention-Aware Sparse View Synthesis with Gaussian
  Splatting](https://arxiv.org/abs/2506.10335v1)**  
  Authors: Lintao Xiang, Hongpei Zheng, Yating Huang, Qijun Yang, Hujun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.10335v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, lightweight, nerf, sparse view, few-shot, ar  
- **[UniForward: Unified 3D Scene and Semantic Field Reconstruction via
  Feed-Forward Gaussian Splatting from Only Sparse-View Images](https://arxiv.org/abs/2506.09378v1)**  
  Authors: Qijian Tian, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09378v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, ar, sparse-view, semantic, understanding  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline
  Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, gaussian splatting, sparse view, ar  
- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade
  Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, efficient, geometry, nerf, sparse-view, ar  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, face, sparse-view, ar, motion  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian
  Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: fast, gaussian splatting, face, ar, sparse-view, 3d reconstruction, motion  
- **[Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse
  Views by Jointly Training Hemisphere Sampled Synthetic Images](https://arxiv.org/abs/2505.19264v1)**  
  Authors: Guangan Chen, Anh Minh Truong, Hanhe Lin, Michiel Vlaminck, Wilfried Philips, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19264v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, sparse-view, sparse view, ar, motion  
- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane
  Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: dynamic, gaussian splatting, efficient, head, ar, deformation, 4d, sparse-view, 3d reconstruction, motion, compact  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater
  Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, gaussian splatting, sparse-view, robotics, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 313 papers*

- **[ViDAR: Video Diffusion-Aware 4D Reconstruction From Monocular Inputs](https://arxiv.org/abs/2506.18792v1)**  
  Authors: Michal Nazarczuk, Sibi Catley-Chandar, Thomas Tanay, Zhensong Zhang, Gregory Slabaugh, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18792v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vidar-4d.github.io)  
  Keywords: dynamic, gaussian splatting, geometry, 4d, ar, motion  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: neural rendering, high-fidelity, survey, 3d gaussian, gaussian splatting, vr, autonomous driving, ar, nerf, robotics, 3d reconstruction  
- **[RA-NeRF: Robust Neural Radiance Field Reconstruction with Accurate
  Camera Pose Estimation under Complex Trajectories](https://arxiv.org/abs/2506.15242v2)**  
  Authors: Qingsong Yan, Qiang Wang, Kaiyong Zhao, Jie Chen, Bo Li, Xiaowen Chu, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15242v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, slam, nerf, 3d reconstruction, localization  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty
  Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: neural rendering, 3d gaussian, gaussian splatting, efficient, lightweight, mapping, ar, nerf, 3d reconstruction, head  
- **[HRGS: Hierarchical Gaussian Splatting for Memory-Efficient
  High-Resolution 3D Reconstruction](https://arxiv.org/abs/2506.14229v1)**  
  Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Juan Zhang, Tongfei Chen, Shuo Yang, Shuwei Shao, Wenhao Dong, Baochang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14229v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, face, efficient, ar, 3d reconstruction  
- **[GAF: Gaussian Action Field as a Dynamic World Model for Robotic
  Manipulation](https://arxiv.org/abs/2506.14135v2)**  
  Authors: Ying Chai, Litao Deng, Ruizhi Shao, Jiajun Zhang, Liangjun Xing, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14135v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://chaiying1.github.io/GAF.github.io/project_page/)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, geometry, 4d, ar, motion  
- **[PF-LHM: 3D Animatable Avatar Reconstruction from Pose-free Articulated
  Human Images](https://arxiv.org/abs/2506.13766v1)**  
  Authors: Lingteng Qiu, Peihao Li, Qi Zuo, Xiaodong Gu, Yuan Dong, Weihao Yuan, Siyu Zhu, Xiaoguang Han, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13766v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, efficient, avatar, geometry, human, ar  
- **[Micro-macro Gaussian Splatting with Enhanced Scalability for
  Unconstrained Scene Reconstruction](https://arxiv.org/abs/2506.13516v1)**  
  Authors: Yihui Li, Chengxin Lv, Hongyu Yang, Di Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13516v1.pdf)  
  Keywords: illumination, gaussian splatting, ar, 3d reconstruction, motion  
- **[Multiview Geometric Regularization of Gaussian Splatting for Accurate
  Radiance Fields](https://arxiv.org/abs/2506.13508v1)**  
  Authors: Jungeon Kim, Geonsoo Park, Seungyong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13508v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, geometry, outdoor, ar  
- **[SPLATART: Articulated Gaussian Splatting with Estimated Object Structure](https://arxiv.org/abs/2506.12184v1)**  
  Authors: Stanley Lewis, Vishal Chandra, Tom Gao, Odest Chadwicke Jenkins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12184v1.pdf)  
  Keywords: gaussian splatting, segmentation, geometry, robotics, ar  

### Large Scene

*Showing the latest 50 out of 61 papers*

- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, tracking, slam, outdoor, ar  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: high-fidelity, survey, 3d gaussian, gaussian splatting, dynamic, efficient, face, autonomous driving, nerf, outdoor, ar  
- **[Multiview Geometric Regularization of Gaussian Splatting for Accurate
  Radiance Fields](https://arxiv.org/abs/2506.13508v1)**  
  Authors: Jungeon Kim, Geonsoo Park, Seungyong Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13508v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, geometry, outdoor, ar  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language
  Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: fast, 3d gaussian, gaussian splatting, efficient, segmentation, ar, geometry, outdoor, semantic, understanding  
- **[TraGraph-GS: Trajectory Graph-based Gaussian Splatting for Arbitrary
  Large-Scale Scene Rendering](https://arxiv.org/abs/2506.08704v1)**  
  Authors: Xiaohan Zhang, Sitong Wang, Yushen Yan, Yi Yang, Mingda Xu, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08704v1.pdf)  
  Keywords: ar, large scene, gaussian splatting  
- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from
  Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: fast, 3d gaussian, gaussian splatting, efficient, slam, large scene, ar, motion  
- **[Photoreal Scene Reconstruction from an Egocentric Device](https://arxiv.org/abs/2506.04444v1)**  
  Authors: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04444v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.projectaria.com/photoreal-reconstruction/)  
  Keywords: dynamic, gaussian splatting, lighting, outdoor, ar  
- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient
  Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, efficient, nerf, real-time rendering, outdoor, ar, head  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings
  and Residual Gaussians](https://arxiv.org/abs/2505.21041v3)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v3.pdf)  
  Keywords: 3d gaussian, gaussian splatting, efficient, lightweight, urban scene, geometry, real-time rendering, ar, compact  
- **[VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale
  Scenes](https://arxiv.org/abs/2505.18992v1)**  
  Authors: Tianchen Deng, Wenhua Wu, Junjie He, Yue Pan, Xirui Jiang, Shenghai Yuan, Danwei Wang, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18992v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, mapping, slam, tracking, outdoor, ar, compact  

### Model Compression

*Showing the latest 50 out of 395 papers*

- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, efficient, ray tracing, real-time rendering, ar  
- **[Virtual Memory for 3D Gaussian Splatting](https://arxiv.org/abs/2506.19415v1)**  
  Authors: Jonathan Haberl, Philipp Fleck, Clemens Arth  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19415v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, efficient, real-time rendering, ar  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: high-fidelity, survey, 3d gaussian, gaussian splatting, dynamic, efficient, face, autonomous driving, nerf, outdoor, ar  
- **[Information-computation trade-offs in non-linear transforms](https://arxiv.org/abs/2506.15948v1)**  
  Authors: Connor Ding, Abhiram Rao Gorle, Jiwon Jeong, Naomi Sagan, Tsachy Weissman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15948v1.pdf)  
  Keywords: dynamic, gaussian splatting, efficient, compression, human, ar, compact  
- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads
  Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: high-fidelity, dynamic, gaussian splatting, face, efficient, ar, head  
- **[3DGS-IEval-15K: A Large-scale Image Quality Evaluation Database for 3D
  Gaussian-Splatting](https://arxiv.org/abs/2506.14642v1)**  
  Authors: Yuke Xing, Jiarui Wang, Peizhi Niu, Wenjie Huang, Guangtao Zhai, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14642v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, compression, real-time rendering, human, ar  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty
  Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: neural rendering, 3d gaussian, gaussian splatting, efficient, lightweight, mapping, ar, nerf, 3d reconstruction, head  
- **[HRGS: Hierarchical Gaussian Splatting for Memory-Efficient
  High-Resolution 3D Reconstruction](https://arxiv.org/abs/2506.14229v1)**  
  Authors: Changbai Li, Haodong Zhu, Hanlin Chen, Juan Zhang, Tongfei Chen, Shuo Yang, Shuwei Shao, Wenhao Dong, Baochang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14229v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, face, efficient, ar, 3d reconstruction  
- **[GRaD-Nav++: Vision-Language Model Enabled Visual Drone Navigation with
  Gaussian Radiance Fields and Differentiable Dynamics](https://arxiv.org/abs/2506.14009v1)**  
  Authors: Qianzhong Chen, Naixiang Gao, Suning Huang, JunEn Low, Timothy Chen, Jiankai Sun, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14009v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, efficient, lightweight, ar, head, compact  
- **[PF-LHM: 3D Animatable Avatar Reconstruction from Pose-free Articulated
  Human Images](https://arxiv.org/abs/2506.13766v1)**  
  Authors: Lingteng Qiu, Peihao Li, Qi Zuo, Xiaodong Gu, Yuan Dong, Weihao Yuan, Siyu Zhu, Xiaoguang Han, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13766v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, efficient, avatar, geometry, human, ar  

### Quality Enhancement

*Showing the latest 50 out of 163 papers*

- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, efficient, ray tracing, real-time rendering, ar  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: high-fidelity, survey, 3d gaussian, gaussian splatting, dynamic, efficient, face, autonomous driving, nerf, outdoor, ar  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: neural rendering, high-fidelity, survey, 3d gaussian, gaussian splatting, vr, autonomous driving, ar, nerf, robotics, 3d reconstruction  
- **[SyncTalk++: High-Fidelity and Efficient Synchronized Talking Heads
  Synthesis Using Gaussian Splatting](https://arxiv.org/abs/2506.14742v1)**  
  Authors: Ziqiao Peng, Wentao Hu, Junyuan Ma, Xiangyu Zhu, Xiaomei Zhang, Hao Zhao, Hui Tian, Jun He, Hongyan Liu, Zhaoxin Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14742v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqiaopeng.github.io/synctalk++.)  
  Keywords: high-fidelity, dynamic, gaussian splatting, face, efficient, ar, head  
- **[PF-LHM: 3D Animatable Avatar Reconstruction from Pose-free Articulated
  Human Images](https://arxiv.org/abs/2506.13766v1)**  
  Authors: Lingteng Qiu, Peihao Li, Qi Zuo, Xiaodong Gu, Yuan Dong, Weihao Yuan, Siyu Zhu, Xiaoguang Han, Guanying Chen, Zilong Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13766v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, efficient, avatar, geometry, human, ar  
- **[GaussianVAE: Adaptive Learning Dynamics of 3D Gaussians for
  High-Fidelity Super-Resolution](https://arxiv.org/abs/2506.07897v1)**  
  Authors: Shuja Khalid, Mohamed Ibrahim, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07897v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, dynamic, gaussian splatting, lightweight, ar  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline
  Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, gaussian splatting, sparse view, ar  
- **[Parametric Gaussian Human Model: Generalizable Prior for Efficient and
  Realistic Human Avatar Modeling](https://arxiv.org/abs/2506.06645v1)**  
  Authors: Cheng Peng, Jingxiang Sun, Yushuo Chen, Zhaoqi Su, Zhuo Su, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06645v1.pdf)  
  Keywords: fast, high-fidelity, 3d gaussian, gaussian splatting, efficient, face, avatar, geometry, human, ar, head, compact  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for
  Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: high-fidelity, 3d gaussian, gaussian splatting, efficient, ar, geometry, lighting, 3d reconstruction, motion  
- **[ODE-GS: Latent ODEs for Dynamic Scene Extrapolation with 3D Gaussian
  Splatting](https://arxiv.org/abs/2506.05480v1)**  
  Authors: Daniel Wang, Patrick Rim, Tian Tian, Alex Wong, Ganesh Sundaramoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05480v1.pdf)  
  Keywords: neural rendering, high-fidelity, 3d gaussian, gaussian splatting, dynamic, lightweight, deformation, nerf, ar  

### Ray Tracing

- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, efficient, ray tracing, real-time rendering, ar  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: fast, gaussian splatting, avatar, ray tracing, shadow, relighting, relightable, lighting, geometry, human, ar  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: 3d gaussian, gaussian splatting, efficient, efficient rendering, ray tracing, relighting, lighting, acceleration, ar  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, efficient, animation, acceleration, ray marching, ar, compact  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: illumination, 3d gaussian, gaussian splatting, efficient, face, ray tracing, real-time rendering, global illumination, lighting, ar  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: neural rendering, fast, 3d gaussian, gaussian splatting, ray tracing, shadow, reflection, ar  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: gaussian splatting, face, ray tracing, shadow, reflection, lighting  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation
  Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, 3d gaussian, gaussian splatting, ray tracing, ar  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: light transport, gaussian splatting, efficient, ray tracing, reflection, acceleration, ar  
- **[RaySplats: Ray Tracing based Gaussian Splatting](https://arxiv.org/abs/2501.19196v1)**  
  Authors: Krzysztof Byrski, Marcin Mazur, Jacek Tabor, Tadeusz Dziarmaga, Marcin Kądziołka, Dawid Baran, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2501.19196v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ray tracing, shadow, reflection, ar  

### Relighting

*Showing the latest 50 out of 106 papers*

- **[Micro-macro Gaussian Splatting with Enhanced Scalability for
  Unconstrained Scene Reconstruction](https://arxiv.org/abs/2506.13516v1)**  
  Authors: Yihui Li, Chengxin Lv, Hongyu Yang, Di Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13516v1.pdf)  
  Keywords: illumination, gaussian splatting, ar, 3d reconstruction, motion  
- **[GS-2DGS: Geometrically Supervised 2DGS for Reflective Object
  Reconstruction](https://arxiv.org/abs/2506.13110v1)**  
  Authors: Jinguang Tong, Xuesong li, Fahira Afzal Maken, Sundaram Muthu, Lars Petersson, Chuong Nguyen, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13110v1.pdf)  
  Keywords: fast, 3d gaussian, gaussian splatting, face, relighting, real-time rendering, lighting, ar  
- **[Efficient multi-view training for 3D Gaussian Splatting](https://arxiv.org/abs/2506.12727v2)**  
  Authors: Minhyuk Choi, Injae Kim, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12727v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, efficient, lighting, nerf, ar, head  
- **[R3D2: Realistic 3D Asset Insertion via Diffusion for Autonomous Driving
  Simulation](https://arxiv.org/abs/2506.07826v1)**  
  Authors: William Ljungbergh, Bernardo Taveira, Wenzhao Zheng, Adam Tonderski, Chensheng Peng, Fredrik Kahl, Christoffer Petersson, Michael Felsberg, Kurt Keutzer, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07826v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/R3D2/.)  
  Keywords: neural rendering, illumination, 3d gaussian, gaussian splatting, dynamic, lightweight, autonomous driving, shadow, lighting, ar  
- **[SPC to 3D: Novel View Synthesis from Binary SPC via I2I translation](https://arxiv.org/abs/2506.06890v1)**  
  Authors: Sumit Sharma, Gopi Raju Matta, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06890v1.pdf)  
  Keywords: illumination, gaussian splatting, ar, nerf, 3d reconstruction  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for
  Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: high-fidelity, 3d gaussian, gaussian splatting, efficient, ar, geometry, lighting, 3d reconstruction, motion  
- **[Photoreal Scene Reconstruction from an Egocentric Device](https://arxiv.org/abs/2506.04444v1)**  
  Authors: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04444v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.projectaria.com/photoreal-reconstruction/)  
  Keywords: dynamic, gaussian splatting, lighting, outdoor, ar  
- **[Robust Neural Rendering in the Wild with Asymmetric Dual 3D Gaussian
  Splatting](https://arxiv.org/abs/2506.03538v1)**  
  Authors: Chengqi Li, Zhihao Shi, Yangdi Lu, Wenbo He, Xiangyu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03538v1.pdf)  
  Keywords: neural rendering, 3d gaussian, gaussian splatting, dynamic, lightweight, ar, geometry, lighting, 3d reconstruction  
- **[RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis
  and 3D Reconstruction of Autonomous Driving Scenes](https://arxiv.org/abs/2506.01379v1)**  
  Authors: Pou-Chun Kung, Skanda Harisha, Ram Vasudevan, Aline Eid, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01379v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/radarsplat.)  
  Keywords: high-fidelity, gaussian splatting, autonomous driving, ar, reflection, 3d reconstruction  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream
  Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: high-fidelity, 3d gaussian, gaussian splatting, ar, lighting, 3d reconstruction, motion  

### SLAM

*Showing the latest 50 out of 158 papers*

- **[GRAND-SLAM: Local Optimization for Globally Consistent Large-Scale
  Multi-Agent Gaussian SLAM](https://arxiv.org/abs/2506.18885v1)**  
  Authors: Annika Thomas, Aneesa Sonawalla, Alex Rose, Jonathan P. How  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18885v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, tracking, slam, outdoor, ar  
- **[RA-NeRF: Robust Neural Radiance Field Reconstruction with Accurate
  Camera Pose Estimation under Complex Trajectories](https://arxiv.org/abs/2506.15242v2)**  
  Authors: Qingsong Yan, Qiang Wang, Kaiyong Zhao, Jie Chen, Bo Li, Xiaowen Chu, Fei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.15242v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, ar, slam, nerf, 3d reconstruction, localization  
- **[Peering into the Unknown: Active View Selection with Neural Uncertainty
  Maps for 3D Reconstruction](https://arxiv.org/abs/2506.14856v1)**  
  Authors: Zhengquan Zhang, Feng Xu, Mengmi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.14856v1.pdf)  
  Keywords: neural rendering, 3d gaussian, gaussian splatting, efficient, lightweight, mapping, ar, nerf, 3d reconstruction, head  
- **[TextureSplat: Per-Primitive Texture Mapping for Reflective Gaussian
  Splatting](https://arxiv.org/abs/2506.13348v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.13348v1.pdf)  
  Keywords: ar, mapping, gaussian splatting, face  
- **[Rasterizing Wireless Radiance Field via Deformable 2D Gaussian Splatting](https://arxiv.org/abs/2506.12787v2)**  
  Authors: Mufan Liu, Cixiao Zhang, Qi Yang, Yujie Cao, Yiling Xu, Yin Xu, Shu Sun, Mingzeng Dai, Yunfeng Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12787v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://evan-sudo.github.io/swiftwrf/.)  
  Keywords: fast, gaussian splatting, localization, lightweight, deformation, nerf, ar, compact  
- **[Anti-Aliased 2D Gaussian Splatting](https://arxiv.org/abs/2506.11252v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.11252v1.pdf)  
  Keywords: gaussian splatting, mapping, face, efficient, ar  
- **[DGS-LRM: Real-Time Deformable 3D Gaussian Reconstruction From Monocular
  Videos](https://arxiv.org/abs/2506.09997v1)**  
  Authors: Chieh Hubert Lin, Zhaoyang Lv, Songyin Wu, Zhen Xu, Thu Nguyen-Phuoc, Hung-Yu Tseng, Julian Straub, Numair Khan, Lei Xiao, Ming-Hsuan Yang, Yuheng Ren, Richard Newcombe, Zhao Dong, Zhengqin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09997v1.pdf)  
  Keywords: 3d gaussian, dynamic, deformation, tracking, ar, motion  
- **[PIG: Physically-based Multi-Material Interaction with 3D Gaussians](https://arxiv.org/abs/2506.07657v1)**  
  Authors: Zeyu Xiao, Zhenyi Wu, Mingyang Sun, Qipeng Yan, Yufan Guo, Zhuoer Liang, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07657v1.pdf)  
  Keywords: fast, 3d gaussian, dynamic, gaussian splatting, mapping, segmentation, deformation, ar  
- **[Gaussian Mapping for Evolving Scenes](https://arxiv.org/abs/2506.06909v1)**  
  Authors: Vladimir Yugay, Thies Kersten, Luca Carlone, Theo Gevers, Martin R. Oswald, Lukas Schmid  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06909v1.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, mapping, autonomous driving, ar, robotics, semantic, motion  
- **[Hi-LSplat: Hierarchical 3D Language Gaussian Splatting](https://arxiv.org/abs/2506.06822v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06822v1.pdf)  
  Keywords: gaussian splatting, segmentation, ar, semantic, understanding, localization  

### Scene Understanding

*Showing the latest 50 out of 183 papers*

- **[ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical
  Gaussian World Model](https://arxiv.org/abs/2506.19842v1)**  
  Authors: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.19842v1.pdf)  
  Keywords: understanding, dynamic, gaussian splatting, deformation, body, ar, motion  
- **[3D Arena: An Open Platform for Generative 3D Evaluation](https://arxiv.org/abs/2506.18787v1)**  
  Authors: Dylan Ebert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18787v1.pdf)  
  Keywords: ar, understanding, human  
- **[Reconstructing Tornadoes in 3D with Gaussian Splatting](https://arxiv.org/abs/2506.18677v1)**  
  Authors: Adam Yang, Nadula Kadawedduwa, Tianfu Wang, Maria Molina, Christopher Metzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.18677v1.pdf)  
  Keywords: ar, understanding, 3d gaussian, gaussian splatting  
- **[SPLATART: Articulated Gaussian Splatting with Estimated Object Structure](https://arxiv.org/abs/2506.12184v1)**  
  Authors: Stanley Lewis, Vishal Chandra, Tom Gao, Odest Chadwicke Jenkins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.12184v1.pdf)  
  Keywords: gaussian splatting, segmentation, geometry, robotics, ar  
- **[ODG: Occupancy Prediction Using Dual Gaussians](https://arxiv.org/abs/2506.09417v2)**  
  Authors: Yunxiao Shi, Yinhao Zhu, Shizhong Han, Jisoo Jeong, Amin Ansari, Hong Cai, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09417v2.pdf)  
  Keywords: 3d gaussian, dynamic, gaussian splatting, autonomous driving, ar, geometry, real-time rendering, semantic  
- **[UniForward: Unified 3D Scene and Semantic Field Reconstruction via
  Feed-Forward Gaussian Splatting from Only Sparse-View Images](https://arxiv.org/abs/2506.09378v1)**  
  Authors: Qijian Tian, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09378v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, ar, sparse-view, semantic, understanding  
- **[Gaussian2Scene: 3D Scene Representation Learning via Self-supervised
  Learning with 3D Gaussian Splatting](https://arxiv.org/abs/2506.08777v2)**  
  Authors: Keyi Liu, Weidong Yang, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08777v2.pdf)  
  Keywords: ar, understanding, 3d gaussian, gaussian splatting  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language
  Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: fast, 3d gaussian, gaussian splatting, efficient, segmentation, ar, geometry, outdoor, semantic, understanding  
- **[OpenSplat3D: Open-Vocabulary 3D Instance Segmentation using Gaussian
  Splatting](https://arxiv.org/abs/2506.07697v1)**  
  Authors: Jens Piekenbrinck, Christian Schmidt, Alexander Hermans, Narunas Vaskevicius, Timm Linder, Bastian Leibe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07697v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, segmentation, ar, semantic, understanding  
- **[PIG: Physically-based Multi-Material Interaction with 3D Gaussians](https://arxiv.org/abs/2506.07657v1)**  
  Authors: Zeyu Xiao, Zhenyi Wu, Mingyang Sun, Qipeng Yan, Yufan Guo, Zhuoer Liang, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07657v1.pdf)  
  Keywords: fast, 3d gaussian, dynamic, gaussian splatting, mapping, segmentation, deformation, ar  



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