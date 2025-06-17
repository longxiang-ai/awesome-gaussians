# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-06-17 00:56:10

## Categories

- [3DGS Surveys](#3dgs-surveys) (35 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (544 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1926 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (642 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (728 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (138 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (627 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (112 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (747 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (309 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (41 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (213 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (292 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (355 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: efficient, outdoor, understanding, neural rendering, 3d gaussian, gaussian splatting, semantic, survey, segmentation, high-fidelity, ar, 3d reconstruction  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, semantic, mapping, localization, survey, nerf, segmentation, slam, ar  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: body, understanding, 3d gaussian, gaussian splatting, motion, 4d, survey, ar, dynamic  
- **[A Survey of 3D Reconstruction with Event Cameras](https://arxiv.org/abs/2505.08438v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v2.pdf)  
  Keywords: robotics, autonomous driving, neural rendering, 3d gaussian, gaussian splatting, motion, geometry, survey, nerf, ar, dynamic, 3d reconstruction, illumination  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: efficient, gaussian splatting, fast, survey, ar, 3d reconstruction  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: autonomous driving, 3d gaussian, semantic, survey, nerf, ar, robotics  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d gaussian, lighting, survey, ar, 3d reconstruction  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: outdoor, understanding, 3d gaussian, gaussian splatting, geometry, survey, nerf, sparse view, ar, 3d reconstruction, face  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: 3d gaussian, gaussian splatting, lighting, semantic, survey, segmentation, ar, robotics  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v3)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v3.pdf)  
  Keywords: 3d gaussian, gaussian splatting, lighting, motion, fast, survey, ar, dynamic, 3d reconstruction  

### Acceleration

*Showing the latest 50 out of 544 papers*

- **[HAIF-GS: Hierarchical and Induced Flow-Guided Gaussian Splatting for Dynamic Scene](https://arxiv.org/abs/2506.09518v1)**  
  Authors: Jianing Chen, Zehao Li, Yujun Cai, Hao Jiang, Chengxuan Qian, Juyuan Kang, Shuqin Gao, Honglong Zhao, Tianlu Mao, Yucheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09518v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, real-time rendering, motion, ar, dynamic, deformation  
- **[ODG: Occupancy Prediction Using Dual Gaussians](https://arxiv.org/abs/2506.09417v2)**  
  Authors: Yunxiao Shi, Yinhao Zhu, Shizhong Han, Jisoo Jeong, Amin Ansari, Hong Cai, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09417v2.pdf)  
  Keywords: autonomous driving, 3d gaussian, gaussian splatting, real-time rendering, semantic, geometry, ar, dynamic  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: efficient, outdoor, understanding, 3d gaussian, gaussian splatting, semantic, geometry, segmentation, ar, fast  
- **[4DGT: Learning a 4D Gaussian Transformer Using Real-World Monocular Videos](https://arxiv.org/abs/2506.08015v1)**  
  Authors: Zhen Xu, Zhengqin Li, Zhao Dong, Xiaowei Zhou, Richard Newcombe, Zhaoyang Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08015v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dgt.github.io)  
  Keywords: efficient, 4d, ar, efficient rendering, dynamic  
- **[Speedy Deformable 3D Gaussian Splatting: Fast Rendering and Compression of Dynamic Scenes](https://arxiv.org/abs/2506.07917v1)**  
  Authors: Allen Tu, Haiyang Ying, Alex Hanson, Yonghan Lee, Tom Goldstein, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07917v1.pdf)  
  Keywords: vr, 3d gaussian, gaussian splatting, motion, compression, 4d, nerf, ar, dynamic, fast, deformation  
- **[PIG: Physically-based Multi-Material Interaction with 3D Gaussians](https://arxiv.org/abs/2506.07657v1)**  
  Authors: Zeyu Xiao, Zhenyi Wu, Mingyang Sun, Qipeng Yan, Yufan Guo, Zhuoer Liang, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07657v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, mapping, segmentation, ar, dynamic, fast, deformation  
- **[Accelerating 3D Gaussian Splatting with Neural Sorting and Axis-Oriented Rasterization](https://arxiv.org/abs/2506.07069v1)**  
  Authors: Zhican Wang, Guanghui He, Dantong Liu, Lingjun Gao, Shell Xu Hu, Chen Zhang, Zhuoran Song, Nicholas Lane, Wayne Luk, Hongxiang Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07069v1.pdf)  
  Keywords: efficient, vr, autonomous driving, 3d gaussian, gaussian splatting, real-time rendering, head, ar, robotics  
- **[Hybrid Mesh-Gaussian Representation for Efficient Indoor Scene Reconstruction](https://arxiv.org/abs/2506.06988v1)**  
  Authors: Binxiao Huang, Zhihao Li, Shiyong Liu, Xiao Tang, Jiajun Tang, Jiaqi Lin, Yuxin Cheng, Zhenyu Chen, Xiaofei Wu, Ngai Wong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06988v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, real-time rendering, ar, 3d reconstruction  
- **[Parametric Gaussian Human Model: Generalizable Prior for Efficient and Realistic Human Avatar Modeling](https://arxiv.org/abs/2506.06645v1)**  
  Authors: Cheng Peng, Jingxiang Sun, Yushuo Chen, Zhaoqi Su, Zhuo Su, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06645v1.pdf)  
  Keywords: efficient, compact, 3d gaussian, gaussian splatting, avatar, geometry, human, head, ar, high-fidelity, fast, face  
- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, motion, slam, ar, large scene, fast  

### Applications

*Showing the latest 50 out of 1926 papers*

- **[Anti-Aliased 2D Gaussian Splatting](https://arxiv.org/abs/2506.11252v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.11252v1.pdf)  
  Keywords: efficient, gaussian splatting, mapping, ar, face  
- **[PointGS: Point Attention-Aware Sparse View Synthesis with Gaussian Splatting](https://arxiv.org/abs/2506.10335v1)**  
  Authors: Lintao Xiang, Hongpei Zheng, Yating Huang, Qijun Yang, Hujun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.10335v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, lightweight, nerf, sparse view, few-shot, ar  
- **[DGS-LRM: Real-Time Deformable 3D Gaussian Reconstruction From Monocular Videos](https://arxiv.org/abs/2506.09997v1)**  
  Authors: Chieh Hubert Lin, Zhaoyang Lv, Songyin Wu, Zhen Xu, Thu Nguyen-Phuoc, Hung-Yu Tseng, Julian Straub, Numair Khan, Lei Xiao, Ming-Hsuan Yang, Yuheng Ren, Richard Newcombe, Zhao Dong, Zhengqin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09997v1.pdf)  
  Keywords: 3d gaussian, motion, tracking, ar, dynamic, deformation  
- **[UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting](https://arxiv.org/abs/2506.09952v1)**  
  Authors: Ziyi Wang, Yanran Zhang, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09952v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wangzy22/UniPre3D?style=social)](https://github.com/wangzy22/UniPre3D)  
  Keywords: gaussian splatting, ar  
- **[The Less You Depend, The More You Learn: Synthesizing Novel Views from Sparse, Unposed Images without Any 3D Knowledge](https://arxiv.org/abs/2506.09885v1)**  
  Authors: Haoru Wang, Kai Ye, Yangyan Li, Wenzheng Chen, Baoquan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09885v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/Less3Depend/)  
  Keywords: geometry, nerf, ar  
- **[DynaSplat: Dynamic-Static Gaussian Splatting with Hierarchical Motion Decomposition for Scene Reconstruction](https://arxiv.org/abs/2506.09836v1)**  
  Authors: Junli Deng, Ping Shi, Qipei Li, Jinyang Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09836v1.pdf)  
  Keywords: efficient, compact, gaussian splatting, motion, ar, dynamic, deformation  
- **[Self-Supervised Multi-Part Articulated Objects Modeling via Deformable Gaussian Splatting and Progressive Primitive Segmentation](https://arxiv.org/abs/2506.09663v1)**  
  Authors: Haowen Wang, Xiaoping Yuan, Zhao Jin, Zhen Zhao, Zhengping Che, Yousong Xue, Jin Tian, Yakun Huang, Jian Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09663v1.pdf)  
  Keywords: compact, 3d gaussian, gaussian splatting, motion, geometry, human, segmentation, ar, deformation  
- **[SemanticSplat: Feed-Forward 3D Scene Understanding with Language-Aware Gaussian Fields](https://arxiv.org/abs/2506.09565v2)**  
  Authors: Qijing Li, Jingxiang Sun, Liang An, Zhaoqi Su, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09565v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://semanticsplat.github.io.)  
  Keywords: understanding, sparse-view, 3d gaussian, semantic, geometry, segmentation, ar, 3d reconstruction  
- **[Gaussian Herding across Pens: An Optimal Transport Perspective on Global Gaussian Reduction for 3DGS](https://arxiv.org/abs/2506.09534v1)**  
  Authors: Tao Wang, Mengyu Li, Geduo Zeng, Cheng Meng, Qiong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09534v1.pdf)  
  Keywords: efficient, neural rendering, 3d gaussian, gaussian splatting, compact, lightweight, geometry, ar  
- **[HAIF-GS: Hierarchical and Induced Flow-Guided Gaussian Splatting for Dynamic Scene](https://arxiv.org/abs/2506.09518v1)**  
  Authors: Jianing Chen, Zehao Li, Yujun Cai, Hao Jiang, Chengxuan Qian, Juyuan Kang, Shuqin Gao, Honglong Zhao, Tianlu Mao, Yucheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09518v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, real-time rendering, motion, ar, dynamic, deformation  

### Avatar Generation

*Showing the latest 50 out of 642 papers*

- **[Anti-Aliased 2D Gaussian Splatting](https://arxiv.org/abs/2506.11252v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.11252v1.pdf)  
  Keywords: efficient, gaussian splatting, mapping, ar, face  
- **[Self-Supervised Multi-Part Articulated Objects Modeling via Deformable Gaussian Splatting and Progressive Primitive Segmentation](https://arxiv.org/abs/2506.09663v1)**  
  Authors: Haowen Wang, Xiaoping Yuan, Zhao Jin, Zhen Zhao, Zhengping Che, Yousong Xue, Jin Tian, Yakun Huang, Jian Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09663v1.pdf)  
  Keywords: compact, 3d gaussian, gaussian splatting, motion, geometry, human, segmentation, ar, deformation  
- **[Synthetic Human Action Video Data Generation with Pose Transfer](https://arxiv.org/abs/2506.09411v1)**  
  Authors: Vaclav Knapp, Matyas Bohacek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09411v1.pdf)  
  Keywords: understanding, 3d gaussian, avatar, recognition, motion, human, ar, few-shot, autonomous driving  
- **[Hierarchical Scoring with 3D Gaussian Splatting for Instance Image-Goal Navigation](https://arxiv.org/abs/2506.07338v1)**  
  Authors: Yijie Deng, Shuaihang Yuan, Geeta Chandra Raju Bethala, Anthony Tzes, Yu-Shen Liu, Yi Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07338v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, semantic, head, ar  
- **[Accelerating 3D Gaussian Splatting with Neural Sorting and Axis-Oriented Rasterization](https://arxiv.org/abs/2506.07069v1)**  
  Authors: Zhican Wang, Guanghui He, Dantong Liu, Lingjun Gao, Shell Xu Hu, Chen Zhang, Zhuoran Song, Nicholas Lane, Wayne Luk, Hongxiang Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07069v1.pdf)  
  Keywords: efficient, vr, autonomous driving, 3d gaussian, gaussian splatting, real-time rendering, head, ar, robotics  
- **[Parametric Gaussian Human Model: Generalizable Prior for Efficient and Realistic Human Avatar Modeling](https://arxiv.org/abs/2506.06645v1)**  
  Authors: Cheng Peng, Jingxiang Sun, Yushuo Chen, Zhaoqi Su, Zhuo Su, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06645v1.pdf)  
  Keywords: efficient, compact, 3d gaussian, gaussian splatting, avatar, geometry, human, head, ar, high-fidelity, fast, face  
- **[BecomingLit: Relightable Gaussian Avatars with Hybrid Neural Shading](https://arxiv.org/abs/2506.06271v1)**  
  Authors: Jonathan Schmidt, Simon Giebenhain, Matthias Niessner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06271v1.pdf)  
  Keywords: relighting, 3d gaussian, lighting, avatar, relightable, head, ar, dynamic, illumination, face  
- **[Lumina: Real-Time Mobile Neural Rendering by Exploiting Computational Redundancy](https://arxiv.org/abs/2506.05682v1)**  
  Authors: Yu Feng, Weikai Lin, Yuge Cheng, Zihan Liu, Jingwen Leng, Minyi Guo, Chen Chen, Shixuan Sun, Yuhao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05682v1.pdf)  
  Keywords: neural rendering, 3d gaussian, gaussian splatting, head, ar  
- **[Synthetic Dataset Generation for Autonomous Mobile Robots Using 3D Gaussian Splatting for Vision Training](https://arxiv.org/abs/2506.05092v1)**  
  Authors: Aneesh Deogan, Wout Beks, Peter Teurlings, Koen de Vos, Mark van den Brand, Rene van de Molengraft  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05092v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, human, ar, robotics, dynamic  
- **[UAV4D: Dynamic Neural Rendering of Human-Centric UAV Imagery using Gaussian Splatting](https://arxiv.org/abs/2506.05011v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Christopher Maxey, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05011v1.pdf)  
  Keywords: neural rendering, gaussian splatting, 4d, human, ar, dynamic  

### Dynamic Scene

*Showing the latest 50 out of 728 papers*

- **[DGS-LRM: Real-Time Deformable 3D Gaussian Reconstruction From Monocular Videos](https://arxiv.org/abs/2506.09997v1)**  
  Authors: Chieh Hubert Lin, Zhaoyang Lv, Songyin Wu, Zhen Xu, Thu Nguyen-Phuoc, Hung-Yu Tseng, Julian Straub, Numair Khan, Lei Xiao, Ming-Hsuan Yang, Yuheng Ren, Richard Newcombe, Zhao Dong, Zhengqin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09997v1.pdf)  
  Keywords: 3d gaussian, motion, tracking, ar, dynamic, deformation  
- **[DynaSplat: Dynamic-Static Gaussian Splatting with Hierarchical Motion Decomposition for Scene Reconstruction](https://arxiv.org/abs/2506.09836v1)**  
  Authors: Junli Deng, Ping Shi, Qipei Li, Jinyang Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09836v1.pdf)  
  Keywords: efficient, compact, gaussian splatting, motion, ar, dynamic, deformation  
- **[Self-Supervised Multi-Part Articulated Objects Modeling via Deformable Gaussian Splatting and Progressive Primitive Segmentation](https://arxiv.org/abs/2506.09663v1)**  
  Authors: Haowen Wang, Xiaoping Yuan, Zhao Jin, Zhen Zhao, Zhengping Che, Yousong Xue, Jin Tian, Yakun Huang, Jian Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09663v1.pdf)  
  Keywords: compact, 3d gaussian, gaussian splatting, motion, geometry, human, segmentation, ar, deformation  
- **[HAIF-GS: Hierarchical and Induced Flow-Guided Gaussian Splatting for Dynamic Scene](https://arxiv.org/abs/2506.09518v1)**  
  Authors: Jianing Chen, Zehao Li, Yujun Cai, Hao Jiang, Chengxuan Qian, Juyuan Kang, Shuqin Gao, Honglong Zhao, Tianlu Mao, Yucheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09518v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, real-time rendering, motion, ar, dynamic, deformation  
- **[ODG: Occupancy Prediction Using Dual Gaussians](https://arxiv.org/abs/2506.09417v2)**  
  Authors: Yunxiao Shi, Yinhao Zhu, Shizhong Han, Jisoo Jeong, Amin Ansari, Hong Cai, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09417v2.pdf)  
  Keywords: autonomous driving, 3d gaussian, gaussian splatting, real-time rendering, semantic, geometry, ar, dynamic  
- **[Synthetic Human Action Video Data Generation with Pose Transfer](https://arxiv.org/abs/2506.09411v1)**  
  Authors: Vaclav Knapp, Matyas Bohacek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09411v1.pdf)  
  Keywords: understanding, 3d gaussian, avatar, recognition, motion, human, ar, few-shot, autonomous driving  
- **[StreamSplat: Towards Online Dynamic 3D Reconstruction from Uncalibrated Video Streams](https://arxiv.org/abs/2506.08862v1)**  
  Authors: Zike Wu, Qi Yan, Xuanyu Yi, Lele Wang, Renjie Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08862v1.pdf) | [![GitHub](https://img.shields.io/github/stars/nickwzk/StreamSplat?style=social)](https://github.com/nickwzk/StreamSplat)  
  Keywords: efficient, 3d gaussian, gaussian splatting, ar, dynamic, 3d reconstruction, deformation  
- **[4DGT: Learning a 4D Gaussian Transformer Using Real-World Monocular Videos](https://arxiv.org/abs/2506.08015v1)**  
  Authors: Zhen Xu, Zhengqin Li, Zhao Dong, Xiaowei Zhou, Richard Newcombe, Zhaoyang Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08015v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dgt.github.io)  
  Keywords: efficient, 4d, ar, efficient rendering, dynamic  
- **[Speedy Deformable 3D Gaussian Splatting: Fast Rendering and Compression of Dynamic Scenes](https://arxiv.org/abs/2506.07917v1)**  
  Authors: Allen Tu, Haiyang Ying, Alex Hanson, Yonghan Lee, Tom Goldstein, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07917v1.pdf)  
  Keywords: vr, 3d gaussian, gaussian splatting, motion, compression, 4d, nerf, ar, dynamic, fast, deformation  
- **[GaussianVAE: Adaptive Learning Dynamics of 3D Gaussians for High-Fidelity Super-Resolution](https://arxiv.org/abs/2506.07897v1)**  
  Authors: Shuja Khalid, Mohamed Ibrahim, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07897v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, lightweight, ar, high-fidelity, dynamic  

### Few-shot

*Showing the latest 50 out of 138 papers*

- **[PointGS: Point Attention-Aware Sparse View Synthesis with Gaussian Splatting](https://arxiv.org/abs/2506.10335v1)**  
  Authors: Lintao Xiang, Hongpei Zheng, Yating Huang, Qijun Yang, Hujun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.10335v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, lightweight, nerf, sparse view, few-shot, ar  
- **[SemanticSplat: Feed-Forward 3D Scene Understanding with Language-Aware Gaussian Fields](https://arxiv.org/abs/2506.09565v2)**  
  Authors: Qijing Li, Jingxiang Sun, Liang An, Zhaoqi Su, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09565v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://semanticsplat.github.io.)  
  Keywords: understanding, sparse-view, 3d gaussian, semantic, geometry, segmentation, ar, 3d reconstruction  
- **[Synthetic Human Action Video Data Generation with Pose Transfer](https://arxiv.org/abs/2506.09411v1)**  
  Authors: Vaclav Knapp, Matyas Bohacek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09411v1.pdf)  
  Keywords: understanding, 3d gaussian, avatar, recognition, motion, human, ar, few-shot, autonomous driving  
- **[UniForward: Unified 3D Scene and Semantic Field Reconstruction via Feed-Forward Gaussian Splatting from Only Sparse-View Images](https://arxiv.org/abs/2506.09378v1)**  
  Authors: Qijian Tian, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09378v1.pdf)  
  Keywords: understanding, 3d gaussian, gaussian splatting, semantic, segmentation, ar, sparse-view  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, sparse view, ar, high-fidelity  
- **[JointSplat: Probabilistic Joint Flow-Depth Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2506.03872v1)**  
  Authors: Yang Xiao, Guoan Xu, Qiang Wu, Wenjing Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03872v1.pdf)  
  Keywords: efficient, sparse-view, 3d gaussian, gaussian splatting, sparse view, ar, high-fidelity, 3d reconstruction, face  
- **[Learning Fine-Grained Geometry for Sparse-View Splatting via Cascade Depth Loss](https://arxiv.org/abs/2505.22279v1)**  
  Authors: Wenjun Lu, Haodong Chen, Anqi Yi, Yuk Ying Chung, Zhiyong Wang, Kun Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.22279v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, geometry, nerf, ar, sparse-view  
- **[Intern-GS: Vision Model Guided Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2505.20729v1)**  
  Authors: Xiangyu Sun, Runnan Chen, Mingming Gong, Dong Xu, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20729v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, motion, ar, sparse-view, face  
- **[Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854v2)**  
  Authors: Natsuki Takama, Shintaro Ito, Koichi Ito, Hwann-Tzong Chen, Takafumi Aoki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19854v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gsisaoki.github.io/SPARSE2DGS/)  
  Keywords: gaussian splatting, motion, fast, ar, 3d reconstruction, sparse-view, face  
- **[Improving Novel view synthesis of 360$^\circ$ Scenes in Extremely Sparse Views by Jointly Training Hemisphere Sampled Synthetic Images](https://arxiv.org/abs/2505.19264v1)**  
  Authors: Guangan Chen, Anh Minh Truong, Hanhe Lin, Michiel Vlaminck, Wilfried Philips, Hiep Luong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.19264v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, motion, sparse view, ar, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 627 papers*

- **[The Less You Depend, The More You Learn: Synthesizing Novel Views from Sparse, Unposed Images without Any 3D Knowledge](https://arxiv.org/abs/2506.09885v1)**  
  Authors: Haoru Wang, Kai Ye, Yangyan Li, Wenzheng Chen, Baoquan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09885v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/Less3Depend/)  
  Keywords: geometry, nerf, ar  
- **[Self-Supervised Multi-Part Articulated Objects Modeling via Deformable Gaussian Splatting and Progressive Primitive Segmentation](https://arxiv.org/abs/2506.09663v1)**  
  Authors: Haowen Wang, Xiaoping Yuan, Zhao Jin, Zhen Zhao, Zhengping Che, Yousong Xue, Jin Tian, Yakun Huang, Jian Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09663v1.pdf)  
  Keywords: compact, 3d gaussian, gaussian splatting, motion, geometry, human, segmentation, ar, deformation  
- **[SemanticSplat: Feed-Forward 3D Scene Understanding with Language-Aware Gaussian Fields](https://arxiv.org/abs/2506.09565v2)**  
  Authors: Qijing Li, Jingxiang Sun, Liang An, Zhaoqi Su, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09565v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://semanticsplat.github.io.)  
  Keywords: understanding, sparse-view, 3d gaussian, semantic, geometry, segmentation, ar, 3d reconstruction  
- **[Gaussian Herding across Pens: An Optimal Transport Perspective on Global Gaussian Reduction for 3DGS](https://arxiv.org/abs/2506.09534v1)**  
  Authors: Tao Wang, Mengyu Li, Geduo Zeng, Cheng Meng, Qiong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09534v1.pdf)  
  Keywords: efficient, neural rendering, 3d gaussian, gaussian splatting, compact, lightweight, geometry, ar  
- **[ODG: Occupancy Prediction Using Dual Gaussians](https://arxiv.org/abs/2506.09417v2)**  
  Authors: Yunxiao Shi, Yinhao Zhu, Shizhong Han, Jisoo Jeong, Amin Ansari, Hong Cai, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09417v2.pdf)  
  Keywords: autonomous driving, 3d gaussian, gaussian splatting, real-time rendering, semantic, geometry, ar, dynamic  
- **[StreamSplat: Towards Online Dynamic 3D Reconstruction from Uncalibrated Video Streams](https://arxiv.org/abs/2506.08862v1)**  
  Authors: Zike Wu, Qi Yan, Xuanyu Yi, Lele Wang, Renjie Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08862v1.pdf) | [![GitHub](https://img.shields.io/github/stars/nickwzk/StreamSplat?style=social)](https://github.com/nickwzk/StreamSplat)  
  Keywords: efficient, 3d gaussian, gaussian splatting, ar, dynamic, 3d reconstruction, deformation  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: efficient, outdoor, understanding, 3d gaussian, gaussian splatting, semantic, geometry, segmentation, ar, fast  
- **[Hybrid Mesh-Gaussian Representation for Efficient Indoor Scene Reconstruction](https://arxiv.org/abs/2506.06988v1)**  
  Authors: Binxiao Huang, Zhihao Li, Shiyong Liu, Xiao Tang, Jiajun Tang, Jiaqi Lin, Yuxin Cheng, Zhenyu Chen, Xiaofei Wu, Ngai Wong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06988v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, real-time rendering, ar, 3d reconstruction  
- **[SPC to 3D: Novel View Synthesis from Binary SPC via I2I translation](https://arxiv.org/abs/2506.06890v1)**  
  Authors: Sumit Sharma, Gopi Raju Matta, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06890v1.pdf)  
  Keywords: gaussian splatting, nerf, ar, 3d reconstruction, illumination  
- **[Parametric Gaussian Human Model: Generalizable Prior for Efficient and Realistic Human Avatar Modeling](https://arxiv.org/abs/2506.06645v1)**  
  Authors: Cheng Peng, Jingxiang Sun, Yushuo Chen, Zhaoqi Su, Zhuo Su, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06645v1.pdf)  
  Keywords: efficient, compact, 3d gaussian, gaussian splatting, avatar, geometry, human, head, ar, high-fidelity, fast, face  

### Large Scene

*Showing the latest 50 out of 112 papers*

- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: efficient, outdoor, understanding, 3d gaussian, gaussian splatting, semantic, geometry, segmentation, ar, fast  
- **[TraGraph-GS: Trajectory Graph-based Gaussian Splatting for Arbitrary Large-Scale Scene Rendering](https://arxiv.org/abs/2506.08704v1)**  
  Authors: Xiaohan Zhang, Sitong Wang, Yushen Yan, Yi Yang, Mingda Xu, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08704v1.pdf)  
  Keywords: gaussian splatting, ar, large scene  
- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, motion, slam, ar, large scene, fast  
- **[Photoreal Scene Reconstruction from an Egocentric Device](https://arxiv.org/abs/2506.04444v1)**  
  Authors: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04444v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.projectaria.com/photoreal-reconstruction/)  
  Keywords: outdoor, gaussian splatting, lighting, ar, dynamic  
- **[VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians](https://arxiv.org/abs/2506.02741v1)**  
  Authors: Pengchong Hu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.02741v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://machineperceptionlab.github.io/VTGaussian-SLAM-Project)  
  Keywords: efficient, 3d gaussian, tracking, geometry, mapping, localization, slam, ar, large scene  
- **[LODGE: Level-of-Detail Large-Scale Gaussian Splatting with Efficient Rendering](https://arxiv.org/abs/2505.23158v1)**  
  Authors: Jonas Kulhanek, Marie-Julie Rakotosaona, Fabian Manhardt, Christina Tsalicoglou, Michael Niemeyer, Torsten Sattler, Songyou Peng, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.23158v1.pdf)  
  Keywords: efficient, outdoor, 3d gaussian, gaussian splatting, real-time rendering, head, nerf, ar, efficient rendering, dynamic  
- **[CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians](https://arxiv.org/abs/2505.21041v3)**  
  Authors: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21041v3.pdf)  
  Keywords: efficient, compact, 3d gaussian, gaussian splatting, real-time rendering, lightweight, geometry, urban scene, ar  
- **[HaloGS: Loose Coupling of Compact Geometry and Gaussian Splats for 3D Scenes](https://arxiv.org/abs/2505.20267v1)**  
  Authors: Changjian Jiang, Kerui Ren, Linning Xu, Jiong Chen, Jiangmiao Pang, Yu Zhang, Bo Dai, Mulin Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.20267v1.pdf)  
  Keywords: outdoor, compact, lightweight, geometry, ar, 3d reconstruction  
- **[VPGS-SLAM: Voxel-based Progressive 3D Gaussian SLAM in Large-Scale Scenes](https://arxiv.org/abs/2505.18992v1)**  
  Authors: Tianchen Deng, Wenhua Wu, Junjie He, Yue Pan, Xirui Jiang, Shenghai Yuan, Danwei Wang, Hesheng Wang, Weidong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.18992v1.pdf) | [![GitHub](https://img.shields.io/github/stars/dtc111111/vpgs-slam?style=social)](https://github.com/dtc111111/vpgs-slam)  
  Keywords: outdoor, compact, 3d gaussian, gaussian splatting, tracking, mapping, slam, ar  
- **[SplatCo: Structure-View Collaborative Gaussian Splatting for Detail-Preserving Rendering of Large-Scale Unbounded Scenes](https://arxiv.org/abs/2505.17951v1)**  
  Authors: Haihong Xiao, Jianan Zou, Yuxin Zhou, Ying He, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17951v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SCUT-BIP-Lab/SplatCo?style=social)](https://github.com/SCUT-BIP-Lab/SplatCo)  
  Keywords: outdoor, gaussian splatting, ar, high-fidelity, face  

### Model Compression

*Showing the latest 50 out of 747 papers*

- **[Anti-Aliased 2D Gaussian Splatting](https://arxiv.org/abs/2506.11252v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.11252v1.pdf)  
  Keywords: efficient, gaussian splatting, mapping, ar, face  
- **[PointGS: Point Attention-Aware Sparse View Synthesis with Gaussian Splatting](https://arxiv.org/abs/2506.10335v1)**  
  Authors: Lintao Xiang, Hongpei Zheng, Yating Huang, Qijun Yang, Hujun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.10335v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, lightweight, nerf, sparse view, few-shot, ar  
- **[DynaSplat: Dynamic-Static Gaussian Splatting with Hierarchical Motion Decomposition for Scene Reconstruction](https://arxiv.org/abs/2506.09836v1)**  
  Authors: Junli Deng, Ping Shi, Qipei Li, Jinyang Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09836v1.pdf)  
  Keywords: efficient, compact, gaussian splatting, motion, ar, dynamic, deformation  
- **[Self-Supervised Multi-Part Articulated Objects Modeling via Deformable Gaussian Splatting and Progressive Primitive Segmentation](https://arxiv.org/abs/2506.09663v1)**  
  Authors: Haowen Wang, Xiaoping Yuan, Zhao Jin, Zhen Zhao, Zhengping Che, Yousong Xue, Jin Tian, Yakun Huang, Jian Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09663v1.pdf)  
  Keywords: compact, 3d gaussian, gaussian splatting, motion, geometry, human, segmentation, ar, deformation  
- **[Gaussian Herding across Pens: An Optimal Transport Perspective on Global Gaussian Reduction for 3DGS](https://arxiv.org/abs/2506.09534v1)**  
  Authors: Tao Wang, Mengyu Li, Geduo Zeng, Cheng Meng, Qiong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09534v1.pdf)  
  Keywords: efficient, neural rendering, 3d gaussian, gaussian splatting, compact, lightweight, geometry, ar  
- **[HAIF-GS: Hierarchical and Induced Flow-Guided Gaussian Splatting for Dynamic Scene](https://arxiv.org/abs/2506.09518v1)**  
  Authors: Jianing Chen, Zehao Li, Yujun Cai, Hao Jiang, Chengxuan Qian, Juyuan Kang, Shuqin Gao, Honglong Zhao, Tianlu Mao, Yucheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09518v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, real-time rendering, motion, ar, dynamic, deformation  
- **[TinySplat: Feedforward Approach for Generating Compact 3D Scene Representation](https://arxiv.org/abs/2506.09479v1)**  
  Authors: Zetian Song, Jiaye Fu, Jiaqi Zhang, Xiaohan Lu, Chuanmin Jia, Siwei Ma, Wen Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09479v1.pdf)  
  Keywords: compact, 3d gaussian, gaussian splatting, compression, ar  
- **[StreamSplat: Towards Online Dynamic 3D Reconstruction from Uncalibrated Video Streams](https://arxiv.org/abs/2506.08862v1)**  
  Authors: Zike Wu, Qi Yan, Xuanyu Yi, Lele Wang, Renjie Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08862v1.pdf) | [![GitHub](https://img.shields.io/github/stars/nickwzk/StreamSplat?style=social)](https://github.com/nickwzk/StreamSplat)  
  Keywords: efficient, 3d gaussian, gaussian splatting, ar, dynamic, 3d reconstruction, deformation  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: efficient, outdoor, understanding, 3d gaussian, gaussian splatting, semantic, geometry, segmentation, ar, fast  
- **[4DGT: Learning a 4D Gaussian Transformer Using Real-World Monocular Videos](https://arxiv.org/abs/2506.08015v1)**  
  Authors: Zhen Xu, Zhengqin Li, Zhao Dong, Xiaowei Zhou, Richard Newcombe, Zhaoyang Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08015v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dgt.github.io)  
  Keywords: efficient, 4d, ar, efficient rendering, dynamic  

### Quality Enhancement

*Showing the latest 50 out of 309 papers*

- **[GaussianVAE: Adaptive Learning Dynamics of 3D Gaussians for High-Fidelity Super-Resolution](https://arxiv.org/abs/2506.07897v1)**  
  Authors: Shuja Khalid, Mohamed Ibrahim, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07897v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, lightweight, ar, high-fidelity, dynamic  
- **[ProSplat: Improved Feed-Forward 3D Gaussian Splatting for Wide-Baseline Sparse Views](https://arxiv.org/abs/2506.07670v1)**  
  Authors: Xiaohan Lu, Jiaye Fu, Jiaqi Zhang, Zetian Song, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07670v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, sparse view, ar, high-fidelity  
- **[Parametric Gaussian Human Model: Generalizable Prior for Efficient and Realistic Human Avatar Modeling](https://arxiv.org/abs/2506.06645v1)**  
  Authors: Cheng Peng, Jingxiang Sun, Yushuo Chen, Zhaoqi Su, Zhuo Su, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06645v1.pdf)  
  Keywords: efficient, compact, 3d gaussian, gaussian splatting, avatar, geometry, human, head, ar, high-fidelity, fast, face  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: efficient, 3d gaussian, gaussian splatting, lighting, motion, geometry, ar, high-fidelity, 3d reconstruction  
- **[ODE-GS: Latent ODEs for Dynamic Scene Extrapolation with 3D Gaussian Splatting](https://arxiv.org/abs/2506.05480v1)**  
  Authors: Daniel Wang, Patrick Rim, Tian Tian, Alex Wong, Ganesh Sundaramoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05480v1.pdf)  
  Keywords: neural rendering, 3d gaussian, gaussian splatting, lightweight, nerf, ar, high-fidelity, dynamic, deformation  
- **[DSG-World: Learning a 3D Gaussian World Model from Dual State Videos](https://arxiv.org/abs/2506.05217v1)**  
  Authors: Wenhao Hu, Xuexiang Wen, Xi Li, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05217v1.pdf)  
  Keywords: efficient, 3d gaussian, lighting, semantic, segmentation, high-fidelity, ar, robotics, 3d reconstruction  
- **[Generating Synthetic Stereo Datasets using 3D Gaussian Splatting and Expert Knowledge Transfer](https://arxiv.org/abs/2506.04908v1)**  
  Authors: Filip Slezak, Magnus K. Gjerde, Joakim B. Haurum, Ivan Nikolov, Morten S. Laursen, Thomas B. Moeslund  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04908v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, geometry, nerf, ar, high-fidelity, fast  
- **[Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations](https://arxiv.org/abs/2506.04789v1)**  
  Authors: Gaia Di Lorenzo, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04789v1.pdf)  
  Keywords: understanding, 3d gaussian, gaussian splatting, semantic, geometry, localization, ar, high-fidelity, robotics  
- **[Splatting Physical Scenes: End-to-End Real-to-Sim from Imperfect Robot Data](https://arxiv.org/abs/2506.04120v2)**  
  Authors: Ben Moran, Mauro Comi, Arunkumar Byravan, Steven Bohez, Tom Erez, Zhibin Li, Leonard Hasenclever  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04120v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, motion, geometry, ar, high-fidelity, dynamic  
- **[JointSplat: Probabilistic Joint Flow-Depth Optimization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2506.03872v1)**  
  Authors: Yang Xiao, Guoan Xu, Qiang Wu, Wenjing Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03872v1.pdf)  
  Keywords: efficient, sparse-view, 3d gaussian, gaussian splatting, sparse view, ar, high-fidelity, 3d reconstruction, face  

### Ray Tracing

- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: relighting, shadow, neural rendering, 3d gaussian, gaussian splatting, lighting, relightable, geometry, human, ar, high-fidelity, illumination, ray tracing, face  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: relighting, shadow, gaussian splatting, lighting, avatar, relightable, geometry, human, ar, fast, ray tracing  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: efficient, relighting, 3d gaussian, gaussian splatting, lighting, efficient rendering, ar, acceleration, ray tracing  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: efficient, animation, compact, 3d gaussian, gaussian splatting, ray marching, ar, acceleration, dynamic  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: global illumination, efficient, 3d gaussian, gaussian splatting, lighting, real-time rendering, ar, illumination, ray tracing, face  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: global illumination, light transport, 3d gaussian, lighting, real-time rendering, dynamic, fast, illumination, face  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: reflection, shadow, neural rendering, 3d gaussian, gaussian splatting, ar, fast, ray tracing  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: efficient, lighting, real-time rendering, tracking, relightable, geometry, 4d, ar, dynamic, ray tracing, face  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: reflection, shadow, gaussian splatting, lighting, ray tracing, face  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, survey, ar, ray tracing  

### Relighting

*Showing the latest 50 out of 213 papers*

- **[R3D2: Realistic 3D Asset Insertion via Diffusion for Autonomous Driving Simulation](https://arxiv.org/abs/2506.07826v1)**  
  Authors: William Ljungbergh, Bernardo Taveira, Wenzhao Zheng, Adam Tonderski, Chensheng Peng, Fredrik Kahl, Christoffer Petersson, Michael Felsberg, Kurt Keutzer, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07826v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/R3D2/.)  
  Keywords: autonomous driving, shadow, neural rendering, 3d gaussian, gaussian splatting, lighting, lightweight, ar, dynamic, illumination  
- **[SPC to 3D: Novel View Synthesis from Binary SPC via I2I translation](https://arxiv.org/abs/2506.06890v1)**  
  Authors: Sumit Sharma, Gopi Raju Matta, Kaushik Mitra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06890v1.pdf)  
  Keywords: gaussian splatting, nerf, ar, 3d reconstruction, illumination  
- **[BecomingLit: Relightable Gaussian Avatars with Hybrid Neural Shading](https://arxiv.org/abs/2506.06271v1)**  
  Authors: Jonathan Schmidt, Simon Giebenhain, Matthias Niessner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06271v1.pdf)  
  Keywords: relighting, 3d gaussian, lighting, avatar, relightable, head, ar, dynamic, illumination, face  
- **[SurGSplat: Progressive Geometry-Constrained Gaussian Splatting for Surgical Scene Reconstruction](https://arxiv.org/abs/2506.05935v1)**  
  Authors: Yuchao Zheng, Jianing Zhang, Guochen Ning, Hongen Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05935v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgsplat.github.io/.)  
  Keywords: efficient, 3d gaussian, gaussian splatting, lighting, motion, geometry, ar, high-fidelity, 3d reconstruction  
- **[DSG-World: Learning a 3D Gaussian World Model from Dual State Videos](https://arxiv.org/abs/2506.05217v1)**  
  Authors: Wenhao Hu, Xuexiang Wen, Xi Li, Gaoang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05217v1.pdf)  
  Keywords: efficient, 3d gaussian, lighting, semantic, segmentation, high-fidelity, ar, robotics, 3d reconstruction  
- **[Photoreal Scene Reconstruction from an Egocentric Device](https://arxiv.org/abs/2506.04444v1)**  
  Authors: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04444v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.projectaria.com/photoreal-reconstruction/)  
  Keywords: outdoor, gaussian splatting, lighting, ar, dynamic  
- **[Robust Neural Rendering in the Wild with Asymmetric Dual 3D Gaussian Splatting](https://arxiv.org/abs/2506.03538v1)**  
  Authors: Chengqi Li, Zhihao Shi, Yangdi Lu, Wenbo He, Xiangyu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.03538v1.pdf)  
  Keywords: neural rendering, 3d gaussian, gaussian splatting, lighting, lightweight, geometry, ar, dynamic, 3d reconstruction  
- **[RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes](https://arxiv.org/abs/2506.01379v1)**  
  Authors: Pou-Chun Kung, Skanda Harisha, Ram Vasudevan, Aline Eid, Katherine A. Skinner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.01379v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://umautobots.github.io/radarsplat.)  
  Keywords: reflection, gaussian splatting, ar, high-fidelity, autonomous driving, 3d reconstruction  
- **[Generalizable and Relightable Gaussian Splatting for Human Novel View Synthesis](https://arxiv.org/abs/2505.21502v1)**  
  Authors: Yipengjing Sun, Chenyang Wang, Shunyuan Zheng, Zonglin Li, Shengping Zhang, Xiangyang Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21502v1.pdf)  
  Keywords: relighting, shadow, neural rendering, 3d gaussian, gaussian splatting, lighting, relightable, geometry, human, ar, high-fidelity, illumination, ray tracing, face  
- **[MV-CoLight: Efficient Object Compositing with Consistent Lighting and Shadow Generation](https://arxiv.org/abs/2505.21483v1)**  
  Authors: Kerui Ren, Jiayang Bai, Linning Xu, Lihan Jiang, Jiangmiao Pang, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.21483v1.pdf)  
  Keywords: efficient, shadow, 3d gaussian, lighting, mapping, ar, illumination  

### SLAM

*Showing the latest 50 out of 292 papers*

- **[Anti-Aliased 2D Gaussian Splatting](https://arxiv.org/abs/2506.11252v1)**  
  Authors: Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.11252v1.pdf)  
  Keywords: efficient, gaussian splatting, mapping, ar, face  
- **[DGS-LRM: Real-Time Deformable 3D Gaussian Reconstruction From Monocular Videos](https://arxiv.org/abs/2506.09997v1)**  
  Authors: Chieh Hubert Lin, Zhaoyang Lv, Songyin Wu, Zhen Xu, Thu Nguyen-Phuoc, Hung-Yu Tseng, Julian Straub, Numair Khan, Lei Xiao, Ming-Hsuan Yang, Yuheng Ren, Richard Newcombe, Zhao Dong, Zhengqin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09997v1.pdf)  
  Keywords: 3d gaussian, motion, tracking, ar, dynamic, deformation  
- **[PIG: Physically-based Multi-Material Interaction with 3D Gaussians](https://arxiv.org/abs/2506.07657v1)**  
  Authors: Zeyu Xiao, Zhenyi Wu, Mingyang Sun, Qipeng Yan, Yufan Guo, Zhuoer Liang, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07657v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, mapping, segmentation, ar, dynamic, fast, deformation  
- **[Gaussian Mapping for Evolving Scenes](https://arxiv.org/abs/2506.06909v1)**  
  Authors: Vladimir Yugay, Thies Kersten, Luca Carlone, Theo Gevers, Martin R. Oswald, Lukas Schmid  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06909v1.pdf)  
  Keywords: autonomous driving, 3d gaussian, gaussian splatting, semantic, motion, mapping, ar, dynamic, robotics  
- **[Hi-LSplat: Hierarchical 3D Language Gaussian Splatting](https://arxiv.org/abs/2506.06822v1)**  
  Authors: Chenlu Zhan, Yufei Zhang, Gaoang Wang, Hongwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06822v1.pdf)  
  Keywords: understanding, gaussian splatting, semantic, localization, segmentation, ar  
- **[GS4: Generalizable Sparse Splatting Semantic SLAM](https://arxiv.org/abs/2506.06517v1)**  
  Authors: Mingqi Jiang, Chanho Kim, Chen Ziwen, Li Fuxin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.06517v1.pdf)  
  Keywords: gaussian splatting, recognition, semantic, tracking, mapping, localization, slam, segmentation, ar  
- **[Dy3DGS-SLAM: Monocular 3D Gaussian Splatting SLAM for Dynamic Environments](https://arxiv.org/abs/2506.05965v1)**  
  Authors: Mingrui Li, Yiming Zhou, Hongxing Zhou, Xinggang Hu, Florian Roemer, Hongyu Wang, Ahmad Osman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05965v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, motion, tracking, geometry, mapping, localization, nerf, slam, ar, dynamic  
- **[On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images](https://arxiv.org/abs/2506.05558v1)**  
  Authors: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05558v1.pdf)  
  Keywords: efficient, 3d gaussian, gaussian splatting, motion, slam, ar, large scene, fast  
- **[Unifying Appearance Codes and Bilateral Grids for Driving Scene Gaussian Splatting](https://arxiv.org/abs/2506.05280v2)**  
  Authors: Nan Wang, Yuantao Chen, Lixing Xiao, Weiqing Xiao, Bohan Li, Zhaoxi Chen, Chongjie Ye, Shaocong Xu, Saining Zhang, Ziyang Yan, Pierre Merriaux, Lei Lei, Tianfan Xue, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.05280v2.pdf)  
  Keywords: autonomous driving, neural rendering, gaussian splatting, mapping, geometry, nerf, ar, dynamic  
- **[Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations](https://arxiv.org/abs/2506.04789v1)**  
  Authors: Gaia Di Lorenzo, Federico Tombari, Marc Pollefeys, Daniel Barath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.04789v1.pdf)  
  Keywords: understanding, 3d gaussian, gaussian splatting, semantic, geometry, localization, ar, high-fidelity, robotics  

### Scene Understanding

*Showing the latest 50 out of 355 papers*

- **[Self-Supervised Multi-Part Articulated Objects Modeling via Deformable Gaussian Splatting and Progressive Primitive Segmentation](https://arxiv.org/abs/2506.09663v1)**  
  Authors: Haowen Wang, Xiaoping Yuan, Zhao Jin, Zhen Zhao, Zhengping Che, Yousong Xue, Jin Tian, Yakun Huang, Jian Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09663v1.pdf)  
  Keywords: compact, 3d gaussian, gaussian splatting, motion, geometry, human, segmentation, ar, deformation  
- **[SemanticSplat: Feed-Forward 3D Scene Understanding with Language-Aware Gaussian Fields](https://arxiv.org/abs/2506.09565v2)**  
  Authors: Qijing Li, Jingxiang Sun, Liang An, Zhaoqi Su, Hongwen Zhang, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09565v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://semanticsplat.github.io.)  
  Keywords: understanding, sparse-view, 3d gaussian, semantic, geometry, segmentation, ar, 3d reconstruction  
- **[ODG: Occupancy Prediction Using Dual Gaussians](https://arxiv.org/abs/2506.09417v2)**  
  Authors: Yunxiao Shi, Yinhao Zhu, Shizhong Han, Jisoo Jeong, Amin Ansari, Hong Cai, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09417v2.pdf)  
  Keywords: autonomous driving, 3d gaussian, gaussian splatting, real-time rendering, semantic, geometry, ar, dynamic  
- **[Synthetic Human Action Video Data Generation with Pose Transfer](https://arxiv.org/abs/2506.09411v1)**  
  Authors: Vaclav Knapp, Matyas Bohacek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09411v1.pdf)  
  Keywords: understanding, 3d gaussian, avatar, recognition, motion, human, ar, few-shot, autonomous driving  
- **[UniForward: Unified 3D Scene and Semantic Field Reconstruction via Feed-Forward Gaussian Splatting from Only Sparse-View Images](https://arxiv.org/abs/2506.09378v1)**  
  Authors: Qijian Tian, Xin Tan, Jingyu Gong, Yuan Xie, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.09378v1.pdf)  
  Keywords: understanding, 3d gaussian, gaussian splatting, semantic, segmentation, ar, sparse-view  
- **[Gaussian2Scene: 3D Scene Representation Learning via Self-supervised Learning with 3D Gaussian Splatting](https://arxiv.org/abs/2506.08777v2)**  
  Authors: Keyi Liu, Weidong Yang, Ben Fei, Ying He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08777v2.pdf)  
  Keywords: 3d gaussian, gaussian splatting, understanding, ar  
- **[SceneSplat++: A Large Dataset and Comprehensive Benchmark for Language Gaussian Splatting](https://arxiv.org/abs/2506.08710v1)**  
  Authors: Mengjiao Ma, Qi Ma, Yue Li, Jiahuan Cheng, Runyi Yang, Bin Ren, Nikola Popovic, Mingqiang Wei, Nicu Sebe, Luc Van Gool, Theo Gevers, Martin R. Oswald, Danda Pani Paudel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.08710v1.pdf)  
  Keywords: efficient, outdoor, understanding, 3d gaussian, gaussian splatting, semantic, geometry, segmentation, ar, fast  
- **[OpenSplat3D: Open-Vocabulary 3D Instance Segmentation using Gaussian Splatting](https://arxiv.org/abs/2506.07697v1)**  
  Authors: Jens Piekenbrinck, Christian Schmidt, Alexander Hermans, Narunas Vaskevicius, Timm Linder, Bastian Leibe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07697v1.pdf)  
  Keywords: understanding, 3d gaussian, gaussian splatting, semantic, segmentation, ar  
- **[PIG: Physically-based Multi-Material Interaction with 3D Gaussians](https://arxiv.org/abs/2506.07657v1)**  
  Authors: Zeyu Xiao, Zhenyi Wu, Mingyang Sun, Qipeng Yan, Yufan Guo, Zhuoer Liang, Lihua Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07657v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, mapping, segmentation, ar, dynamic, fast, deformation  
- **[Hierarchical Scoring with 3D Gaussian Splatting for Instance Image-Goal Navigation](https://arxiv.org/abs/2506.07338v1)**  
  Authors: Yijie Deng, Shuaihang Yuan, Geeta Chandra Raju Bethala, Anthony Tzes, Yu-Shen Liu, Yi Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.07338v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, semantic, head, ar  



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