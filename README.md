# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-08-15 00:56:24

## 📰 Latest Updates

🔧 **[2025-06-26] HTTP 301 Redirect Issue Completely Resolved!** 
- Implemented multi-layer fallback strategy to thoroughly solve network compatibility issues

🔧 **[2025-06-26] Configurable Search Keywords Feature Added!**
- You can now customize search keywords by modifying `data/search_config.json`
- Support for different search scopes: abstract-only, title-only, or both
- Flexible keyword configuration for targeted paper collection

- View detailed updates: [News.md](News.md) 📋

---

## Categories

- [3DGS Surveys](#3dgs-surveys) (20 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (269 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (322 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (389 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (72 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (313 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (68 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (404 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (160 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (18 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (112 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (154 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (193 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v1)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v1.pdf)  
  Keywords: lighting, compact, high-fidelity, survey, ar, segmentation, semantic, nerf, gaussian splatting, 3d gaussian, understanding  
- **[A Study of the Framework and Real-World Applications of Language
  Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v1.pdf)  
  Keywords: survey, efficient, ar, semantic, robotics, nerf, gaussian splatting, 3d gaussian, understanding  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned
  and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: survey, human, robotics, nerf, gaussian splatting, 3d gaussian, ar  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: motion, survey, vr, geometry, 3d reconstruction, nerf, gaussian splatting, robotics, 3d gaussian, ar, sparse-view  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v2)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Hanspeter Pfister, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v2.pdf)  
  Keywords: lighting, survey, human, slam, vr, fast, 3d reconstruction, nerf, gaussian splatting, robotics, 3d gaussian, ar, dynamic  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: high-fidelity, face, survey, efficient, outdoor, autonomous driving, nerf, gaussian splatting, 3d gaussian, ar, dynamic  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: high-fidelity, survey, vr, autonomous driving, neural rendering, 3d reconstruction, nerf, gaussian splatting, robotics, 3d gaussian, ar  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: high-fidelity, survey, efficient, ar, outdoor, semantic, neural rendering, 3d reconstruction, segmentation, gaussian splatting, 3d gaussian, understanding  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: survey, efficient, slam, ar, localization, segmentation, semantic, nerf, gaussian splatting, 3d gaussian, mapping  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to
  Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: body, motion, survey, ar, 4d, gaussian splatting, 3d gaussian, understanding, dynamic  

### Acceleration

*Showing the latest 50 out of 269 papers*

- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event
  Cameras](https://arxiv.org/abs/2508.09912v1)**  
  Authors: Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09912v1.pdf)  
  Keywords: lighting, high-fidelity, motion, fast, 4d, gaussian splatting, ar, dynamic  
- **[SAGOnline: Segment Any Gaussians Online](https://arxiv.org/abs/2508.08219v1)**  
  Authors: Wentao Sun, Quanyun Wu, Hanqing Xu, Kyle Gao, Zhengsen Xu, Yiping Chen, Dedong Zhang, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08219v1.pdf)  
  Keywords: efficient, lightweight, vr, tracking, ar, real-time rendering, segmentation, nerf, gaussian splatting, 3d gaussian, understanding  
- **[DIP-GS: Deep Image Prior For Gaussian Splatting Sparse View Recovery](https://arxiv.org/abs/2508.07372v1)**  
  Authors: Rajaei Khatib, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07372v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, 3d gaussian, ar, sparse view, sparse-view  
- **[ExploreGS: Explorable 3D Scene Reconstruction with Virtual Camera
  Samplings and Diffusion Priors](https://arxiv.org/abs/2508.06014v1)**  
  Authors: Minsu Kim, Subin Jeon, In Cho, Mijin Yoo, Seon Joo Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06014v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://exploregs.github.io)  
  Keywords: gaussian splatting, 3d gaussian, ar, real-time rendering  
- **[Optimization-Free Style Transfer for 3D Gaussian Splats](https://arxiv.org/abs/2508.05813v1)**  
  Authors: Raphael Du Sablon, David Hart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05813v1.pdf)  
  Keywords: 3d gaussian, fast, face, ar  
- **[GAP: Gaussianize Any Point Clouds with Text Guidance](https://arxiv.org/abs/2508.05631v1)**  
  Authors: Weiqi Zhang, Junsheng Zhou, Haotian Geng, Wenyuan Zhang, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05631v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weiqi-zhang.github.io/GAP.)  
  Keywords: high-fidelity, face, fast, gaussian splatting, 3d gaussian, ar  
- **[3DGabSplat: 3D Gabor Splatting for Frequency-adaptive Radiance Field
  Rendering](https://arxiv.org/abs/2508.05343v1)**  
  Authors: Junyu Zhou, Yuyang Huang, Wenrui Dai, Junni Zou, Ziyang Zheng, Nuowen Kan, Chenglin Li, Hongkai Xiong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05343v1.pdf)  
  Keywords: high-fidelity, efficient, real-time rendering, head, gaussian splatting, 3d gaussian, ar  
- **[CF3: Compact and Fast 3D Feature Fields](https://arxiv.org/abs/2508.05254v2)**  
  Authors: Hyunjoon Lee, Joonkyu Min, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05254v2.pdf)  
  Keywords: compact, efficient, fast, gaussian splatting, 3d gaussian, ar  
- **[Perceive-Sample-Compress: Towards Real-Time 3D Gaussian Splatting](https://arxiv.org/abs/2508.04965v1)**  
  Authors: Zijian Wang, Beizhen Zhao, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04965v1.pdf)  
  Keywords: efficient, real-time rendering, compression, gaussian splatting, 3d gaussian, ar  
- **[Duplex-GS: Proxy-Guided Weighted Blending for Real-Time
  Order-Independent Gaussian Splatting](https://arxiv.org/abs/2508.03180v1)**  
  Authors: Weihang Liu, Yuke Li, Yuxuan Li, Jingyi Yu, Xin Lou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.03180v1.pdf)  
  Keywords: acceleration, head, gaussian splatting, 3d gaussian, ar  

### Applications

*Showing the latest 50 out of 995 papers*

- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v1)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v1.pdf)  
  Keywords: lighting, compact, high-fidelity, survey, ar, segmentation, semantic, nerf, gaussian splatting, 3d gaussian, understanding  
- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event
  Cameras](https://arxiv.org/abs/2508.09912v1)**  
  Authors: Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09912v1.pdf)  
  Keywords: lighting, high-fidelity, motion, fast, 4d, gaussian splatting, ar, dynamic  
- **[HumanGenesis: Agent-Based Geometric and Generative Modeling for
  Synthetic Human Dynamics](https://arxiv.org/abs/2508.09858v1)**  
  Authors: Weiqi Li, Zehao Zhang, Liang Lin, Guangrun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09858v1.pdf)  
  Keywords: motion, human, face, reflection, 4d, deformation, gaussian splatting, 3d gaussian, ar, dynamic  
- **[Toward Human-Robot Teaming: Learning Handover Behaviors from 3D Scenes](https://arxiv.org/abs/2508.09855v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09855v1.pdf)  
  Keywords: gaussian splatting, ar, human, sparse-view  
- **[GSFixer: Improving 3D Gaussian Splatting with Reference-Guided Video
  Diffusion Priors](https://arxiv.org/abs/2508.09667v1)**  
  Authors: Xingyilang Yin, Qi Zhang, Jiahao Chang, Ying Feng, Qingnan Fan, Xi Yang, Chi-Man Pun, Huaqi Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09667v1.pdf)  
  Keywords: geometry, semantic, 3d reconstruction, gaussian splatting, 3d gaussian, ar, sparse view, sparse-view  
- **[SkySplat: Generalizable 3D Gaussian Splatting from Multi-Temporal Sparse
  Satellite Images](https://arxiv.org/abs/2508.09479v1)**  
  Authors: Xuejun Huang, Xinyi Liu, Yi Wan, Zhi Zheng, Bin Zhang, Mingtao Xiong, Yingying Pei, Yongjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09479v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, ar, sparse-view  
- **[A new dataset and comparison for multi-camera frame synthesis](https://arxiv.org/abs/2508.09068v1)**  
  Authors: Conall Daly, Anil Kokaram  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09068v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar  
- **[Gradient-Direction-Aware Density Control for 3D Gaussian Splatting](https://arxiv.org/abs/2508.09239v1)**  
  Authors: Zheng Zhou, Yu-Jie Xiong, Chun-Ming Xia, Jia-Chen Zhang, Hong-Jian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09239v1.pdf)  
  Keywords: compact, head, gaussian splatting, 3d gaussian, ar, dynamic  
- **[Communication Efficient Robotic Mixed Reality with Gaussian Splatting
  Cross-Layer Optimization](https://arxiv.org/abs/2508.08624v1)**  
  Authors: Chenxuan Liu, He Li, Zongze Li, Shuai Wang, Wei Xu, Kejiang Ye, Derrick Wing Kwan Ng, Chengzhong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08624v1.pdf)  
  Keywords: gaussian splatting, ar, dynamic, efficient  
- **[ReferSplat: Referring Segmentation in 3D Gaussian Splatting](https://arxiv.org/abs/2508.08252v1)**  
  Authors: Shuting He, Guangquan Jie, Changshuo Wang, Yun Zhou, Shuming Hu, Guanbin Li, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08252v1.pdf)  
  Keywords: ar, segmentation, gaussian splatting, 3d gaussian, understanding  

### Avatar Generation

*Showing the latest 50 out of 322 papers*

- **[HumanGenesis: Agent-Based Geometric and Generative Modeling for
  Synthetic Human Dynamics](https://arxiv.org/abs/2508.09858v1)**  
  Authors: Weiqi Li, Zehao Zhang, Liang Lin, Guangrun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09858v1.pdf)  
  Keywords: motion, human, face, reflection, 4d, deformation, gaussian splatting, 3d gaussian, ar, dynamic  
- **[Toward Human-Robot Teaming: Learning Handover Behaviors from 3D Scenes](https://arxiv.org/abs/2508.09855v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09855v1.pdf)  
  Keywords: gaussian splatting, ar, human, sparse-view  
- **[Gradient-Direction-Aware Density Control for 3D Gaussian Splatting](https://arxiv.org/abs/2508.09239v1)**  
  Authors: Zheng Zhou, Yu-Jie Xiong, Chun-Ming Xia, Jia-Chen Zhang, Hong-Jian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09239v1.pdf)  
  Keywords: compact, head, gaussian splatting, 3d gaussian, ar, dynamic  
- **[Touch-Augmented Gaussian Splatting for Enhanced 3D Scene Reconstruction](https://arxiv.org/abs/2508.07717v1)**  
  Authors: Yuchen Gao, Xiao Xu, Eckehard Steinbach, Daniel E. Lucani, Qi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07717v1.pdf)  
  Keywords: lighting, face, geometry, gaussian splatting, 3d gaussian, ar  
- **[Multi-view Normal and Distance Guidance Gaussian Splatting for Surface
  Reconstruction](https://arxiv.org/abs/2508.07701v2)**  
  Authors: Bo Jia, Yanan Guo, Ying Chang, Benkui Zhang, Ying Xie, Kangning Du, Lin Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07701v2.pdf)  
  Keywords: face, outdoor, geometry, gaussian splatting, 3d gaussian, ar  
- **[GS4Buildings: Prior-Guided Gaussian Splatting for 3D Building
  Reconstruction](https://arxiv.org/abs/2508.07355v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07355v1.pdf)  
  Keywords: compact, motion, efficient, face, geometry, semantic, 3d reconstruction, gaussian splatting, urban scene, ar  
- **[DexFruit: Dexterous Manipulation and Gaussian Splatting Inspection of
  Fruit](https://arxiv.org/abs/2508.07118v1)**  
  Authors: Aiden Swann, Alex Qiu, Matthew Strong, Angelina Zhang, Samuel Morstein, Kai Rayle, Monroe Kennedy III  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07118v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dex-fruit.github.io)  
  Keywords: human, segmentation, gaussian splatting, 3d gaussian, ar  
- **[UW-3DGS: Underwater 3D Reconstruction with Physics-Aware Gaussian
  Splatting](https://arxiv.org/abs/2508.06169v1)**  
  Authors: Wenpeng Xing, Jie Chen, Zaifeng Yang, Changting Lin, Jianfeng Dong, Chaochao Chen, Xun Zhou, Meng Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06169v1.pdf)  
  Keywords: face, light transport, geometry, 3d reconstruction, nerf, gaussian splatting, 3d gaussian, ar  
- **[A 3DGS-Diffusion Self-Supervised Framework for Normal Estimation from a
  Single Image](https://arxiv.org/abs/2508.05950v1)**  
  Authors: Yanxing Liang, Yinghui Wang, Jinlong Yang, Wei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05950v1.pdf)  
  Keywords: face, light transport, ar, gaussian splatting, 3d gaussian, mapping  
- **[Optimization-Free Style Transfer for 3D Gaussian Splats](https://arxiv.org/abs/2508.05813v1)**  
  Authors: Raphael Du Sablon, David Hart  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05813v1.pdf)  
  Keywords: 3d gaussian, fast, face, ar  

### Dynamic Scene

*Showing the latest 50 out of 389 papers*

- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event
  Cameras](https://arxiv.org/abs/2508.09912v1)**  
  Authors: Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09912v1.pdf)  
  Keywords: lighting, high-fidelity, motion, fast, 4d, gaussian splatting, ar, dynamic  
- **[HumanGenesis: Agent-Based Geometric and Generative Modeling for
  Synthetic Human Dynamics](https://arxiv.org/abs/2508.09858v1)**  
  Authors: Weiqi Li, Zehao Zhang, Liang Lin, Guangrun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09858v1.pdf)  
  Keywords: motion, human, face, reflection, 4d, deformation, gaussian splatting, 3d gaussian, ar, dynamic  
- **[Gradient-Direction-Aware Density Control for 3D Gaussian Splatting](https://arxiv.org/abs/2508.09239v1)**  
  Authors: Zheng Zhou, Yu-Jie Xiong, Chun-Ming Xia, Jia-Chen Zhang, Hong-Jian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09239v1.pdf)  
  Keywords: compact, head, gaussian splatting, 3d gaussian, ar, dynamic  
- **[Communication Efficient Robotic Mixed Reality with Gaussian Splatting
  Cross-Layer Optimization](https://arxiv.org/abs/2508.08624v1)**  
  Authors: Chenxuan Liu, He Li, Zongze Li, Shuai Wang, Wei Xu, Kejiang Ye, Derrick Wing Kwan Ng, Chengzhong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08624v1.pdf)  
  Keywords: gaussian splatting, ar, dynamic, efficient  
- **[NeeCo: Image Synthesis of Novel Instrument States Based on Dynamic and
  Deformable 3D Gaussian Reconstruction](https://arxiv.org/abs/2508.07897v1)**  
  Authors: Tianle Zeng, Junlei Hu, Gerardo Loza Galindo, Sharib Ali, Duygu Sarikaya, Pietro Valdastri, Dominic Jones  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07897v1.pdf)  
  Keywords: motion, medical, tracking, deformation, localization, gaussian splatting, 3d gaussian, ar, dynamic  
- **[CharacterShot: Controllable and Consistent 4D Character Animation](https://arxiv.org/abs/2508.07409v1)**  
  Authors: Junyao Gao, Jiaxing Li, Wenran Liu, Yanhong Zeng, Fei Shen, Kai Chen, Yanan Sun, Cairong Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07409v1.pdf)  
  Keywords: animation, motion, 4d, gaussian splatting, ar, dynamic  
- **[GS4Buildings: Prior-Guided Gaussian Splatting for 3D Building
  Reconstruction](https://arxiv.org/abs/2508.07355v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07355v1.pdf)  
  Keywords: compact, motion, efficient, face, geometry, semantic, 3d reconstruction, gaussian splatting, urban scene, ar  
- **[3D Gaussian Representations with Motion Trajectory Field for Dynamic
  Scene Reconstruction](https://arxiv.org/abs/2508.07182v1)**  
  Authors: Xuesong Li, Lars Petersson, Vivien Rolland  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07182v1.pdf)  
  Keywords: compact, motion, efficient, nerf, gaussian splatting, 3d gaussian, ar, dynamic  
- **[EGS-SLAM: RGB-D Gaussian Splatting SLAM with Events](https://arxiv.org/abs/2508.07003v1)**  
  Authors: Siyu Chen, Shenghai Yuan, Thien-Minh Nguyen, Zhuyu Huang, Chenyang Shi, Jin Jing, Lihua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07003v1.pdf)  
  Keywords: high-fidelity, motion, slam, tracking, ar, 3d reconstruction, gaussian splatting, 3d gaussian, mapping, dynamic  
- **[Roll Your Eyes: Gaze Redirection via Explicit 3D Eyeball Rotation](https://arxiv.org/abs/2508.06136v1)**  
  Authors: YoungChan Choi, HengFei Wang, YiHua Cheng, Boeun Kim, Hyung Jin Chang, YoungGeun Choi, Sang-Il Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06136v1.pdf)  
  Keywords: deformation, nerf, gaussian splatting, 3d gaussian, ar  

### Few-shot

*Showing the latest 50 out of 72 papers*

- **[Toward Human-Robot Teaming: Learning Handover Behaviors from 3D Scenes](https://arxiv.org/abs/2508.09855v1)**  
  Authors: Yuekun Wu, Yik Lung Pang, Andrea Cavallaro, Changjae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09855v1.pdf)  
  Keywords: gaussian splatting, ar, human, sparse-view  
- **[GSFixer: Improving 3D Gaussian Splatting with Reference-Guided Video
  Diffusion Priors](https://arxiv.org/abs/2508.09667v1)**  
  Authors: Xingyilang Yin, Qi Zhang, Jiahao Chang, Ying Feng, Qingnan Fan, Xi Yang, Chi-Man Pun, Huaqi Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09667v1.pdf)  
  Keywords: geometry, semantic, 3d reconstruction, gaussian splatting, 3d gaussian, ar, sparse view, sparse-view  
- **[SkySplat: Generalizable 3D Gaussian Splatting from Multi-Temporal Sparse
  Satellite Images](https://arxiv.org/abs/2508.09479v1)**  
  Authors: Xuejun Huang, Xinyi Liu, Yi Wan, Zhi Zheng, Bin Zhang, Mingtao Xiong, Yingying Pei, Yongjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09479v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, ar, sparse-view  
- **[DIP-GS: Deep Image Prior For Gaussian Splatting Sparse View Recovery](https://arxiv.org/abs/2508.07372v1)**  
  Authors: Rajaei Khatib, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07372v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, 3d gaussian, ar, sparse view, sparse-view  
- **[UGOD: Uncertainty-Guided Differentiable Opacity and Soft Dropout for
  Enhanced Sparse-View 3DGS](https://arxiv.org/abs/2508.04968v1)**  
  Authors: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Liangxiu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04968v1.pdf)  
  Keywords: nerf, gaussian splatting, 3d gaussian, ar, sparse-view  
- **[DET-GS: Depth- and Edge-Aware Regularization for High-Fidelity 3D
  Gaussian Splatting](https://arxiv.org/abs/2508.04099v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04099v1.pdf)  
  Keywords: high-fidelity, efficient, semantic, gaussian splatting, 3d gaussian, ar, sparse-view  
- **[GR-Gaussian: Graph-Based Radiative Gaussian Splatting for Sparse-View CT
  Reconstruction](https://arxiv.org/abs/2508.02408v2)**  
  Authors: Yikuang Yuluo, Yue Ma, Kuan Shen, Tongtong Jin, Wang Liao, Yangpu Ma, Fuquan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.02408v2.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, sparse-view  
- **[No Pose at All: Self-Supervised Pose-Free 3D Gaussian Splatting from
  Sparse Views](https://arxiv.org/abs/2508.01171v1)**  
  Authors: Ranran Huang, Krystian Mikolajczyk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.01171v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ranrhuang.github.io/spfsplat/.)  
  Keywords: efficient, geometry, gaussian splatting, 3d gaussian, ar, sparse view  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: motion, survey, vr, geometry, 3d reconstruction, nerf, gaussian splatting, robotics, 3d gaussian, ar, sparse-view  
- **[DWTGS: Rethinking Frequency Regularization for Sparse-view 3D Gaussian
  Splatting](https://arxiv.org/abs/2507.15690v1)**  
  Authors: Hung Nguyen, Runfa Li, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15690v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 313 papers*

- **[GSFixer: Improving 3D Gaussian Splatting with Reference-Guided Video
  Diffusion Priors](https://arxiv.org/abs/2508.09667v1)**  
  Authors: Xingyilang Yin, Qi Zhang, Jiahao Chang, Ying Feng, Qingnan Fan, Xi Yang, Chi-Man Pun, Huaqi Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09667v1.pdf)  
  Keywords: geometry, semantic, 3d reconstruction, gaussian splatting, 3d gaussian, ar, sparse view, sparse-view  
- **[Touch-Augmented Gaussian Splatting for Enhanced 3D Scene Reconstruction](https://arxiv.org/abs/2508.07717v1)**  
  Authors: Yuchen Gao, Xiao Xu, Eckehard Steinbach, Daniel E. Lucani, Qi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07717v1.pdf)  
  Keywords: lighting, face, geometry, gaussian splatting, 3d gaussian, ar  
- **[Multi-view Normal and Distance Guidance Gaussian Splatting for Surface
  Reconstruction](https://arxiv.org/abs/2508.07701v2)**  
  Authors: Bo Jia, Yanan Guo, Ying Chang, Benkui Zhang, Ying Xie, Kangning Du, Lin Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07701v2.pdf)  
  Keywords: face, outdoor, geometry, gaussian splatting, 3d gaussian, ar  
- **[Novel View Synthesis with Gaussian Splatting: Impact on Photogrammetry
  Model Accuracy and Resolution](https://arxiv.org/abs/2508.07483v1)**  
  Authors: Pranav Chougule  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07483v1.pdf)  
  Keywords: gaussian splatting, ar, 3d reconstruction  
- **[GS4Buildings: Prior-Guided Gaussian Splatting for 3D Building
  Reconstruction](https://arxiv.org/abs/2508.07355v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07355v1.pdf)  
  Keywords: compact, motion, efficient, face, geometry, semantic, 3d reconstruction, gaussian splatting, urban scene, ar  
- **[EGS-SLAM: RGB-D Gaussian Splatting SLAM with Events](https://arxiv.org/abs/2508.07003v1)**  
  Authors: Siyu Chen, Shenghai Yuan, Thien-Minh Nguyen, Zhuyu Huang, Chenyang Shi, Jin Jing, Lihua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07003v1.pdf)  
  Keywords: high-fidelity, motion, slam, tracking, ar, 3d reconstruction, gaussian splatting, 3d gaussian, mapping, dynamic  
- **[Evaluating Fisheye-Compatible 3D Gaussian Splatting Methods on Real
  Images Beyond 180 Degree Field of View](https://arxiv.org/abs/2508.06968v1)**  
  Authors: Ulas Gunes, Matias Turkulainen, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06968v1.pdf)  
  Keywords: outdoor, 3d reconstruction, gaussian splatting, 3d gaussian, ar  
- **[UW-3DGS: Underwater 3D Reconstruction with Physics-Aware Gaussian
  Splatting](https://arxiv.org/abs/2508.06169v1)**  
  Authors: Wenpeng Xing, Jie Chen, Zaifeng Yang, Changting Lin, Jianfeng Dong, Chaochao Chen, Xun Zhou, Meng Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06169v1.pdf)  
  Keywords: face, light transport, geometry, 3d reconstruction, nerf, gaussian splatting, 3d gaussian, ar  
- **[MuGS: Multi-Baseline Generalizable Gaussian Splatting Reconstruction](https://arxiv.org/abs/2508.04297v1)**  
  Authors: Yaopeng Lou, Liao Shen, Tianqi Liu, Jiaqi Li, Zihao Huang, Huiqiang Sun, Zhiguo Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04297v1.pdf)  
  Keywords: outdoor, geometry, nerf, gaussian splatting, 3d gaussian, ar  
- **[SplitGaussian: Reconstructing Dynamic Scenes via Visual Geometry
  Decomposition](https://arxiv.org/abs/2508.04224v1)**  
  Authors: Jiahui Li, Shengeng Tang, Jingxuan He, Gang Huang, Zhangye Wang, Yantao Pan, Lechao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04224v1.pdf)  
  Keywords: motion, geometry, gaussian splatting, ar, dynamic  

### Large Scene

*Showing the latest 50 out of 68 papers*

- **[Multi-view Normal and Distance Guidance Gaussian Splatting for Surface
  Reconstruction](https://arxiv.org/abs/2508.07701v2)**  
  Authors: Bo Jia, Yanan Guo, Ying Chang, Benkui Zhang, Ying Xie, Kangning Du, Lin Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07701v2.pdf)  
  Keywords: face, outdoor, geometry, gaussian splatting, 3d gaussian, ar  
- **[GS4Buildings: Prior-Guided Gaussian Splatting for 3D Building
  Reconstruction](https://arxiv.org/abs/2508.07355v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07355v1.pdf)  
  Keywords: compact, motion, efficient, face, geometry, semantic, 3d reconstruction, gaussian splatting, urban scene, ar  
- **[Evaluating Fisheye-Compatible 3D Gaussian Splatting Methods on Real
  Images Beyond 180 Degree Field of View](https://arxiv.org/abs/2508.06968v1)**  
  Authors: Ulas Gunes, Matias Turkulainen, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06968v1.pdf)  
  Keywords: outdoor, 3d reconstruction, gaussian splatting, 3d gaussian, ar  
- **[MuGS: Multi-Baseline Generalizable Gaussian Splatting Reconstruction](https://arxiv.org/abs/2508.04297v1)**  
  Authors: Yaopeng Lou, Liao Shen, Tianqi Liu, Jiaqi Li, Zihao Huang, Huiqiang Sun, Zhiguo Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04297v1.pdf)  
  Keywords: outdoor, geometry, nerf, gaussian splatting, 3d gaussian, ar  
- **[VDEGaussian: Video Diffusion Enhanced 4D Gaussian Splatting for Dynamic
  Urban Scenes Modeling](https://arxiv.org/abs/2508.02129v1)**  
  Authors: Yuru Xiao, Zihan Lin, Chao Lu, Deming Zhai, Kui Jiang, Wenbo Zhao, Wei Zhang, Junjun Jiang, Huanran Wang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.02129v1.pdf)  
  Keywords: high-fidelity, face, fast, 4d, gaussian splatting, urban scene, ar, dynamic  
- **[Stereo 3D Gaussian Splatting SLAM for Outdoor Urban Scenes](https://arxiv.org/abs/2507.23677v1)**  
  Authors: Xiaohan Li, Ziren Gong, Fabio Tosi, Matteo Poggi, Stefano Mattoccia, Dong Liu, Jun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23677v1.pdf)  
  Keywords: high-fidelity, slam, fast, tracking, ar, outdoor, gaussian splatting, urban scene, 3d gaussian, mapping  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: lighting, face, relightable, relighting, illumination, shadow, outdoor, global illumination, gaussian splatting, 3d gaussian, ar, dynamic  
- **[SaLF: Sparse Local Fields for Multi-Sensor Rendering in Real-Time](https://arxiv.org/abs/2507.18713v1)**  
  Authors: Yun Chen, Matthew Haines, Jingkang Wang, Krzysztof Baron-Lis, Sivabalan Manivasagam, Ze Yang, Raquel Urtasun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18713v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://waabi.ai/salf/)  
  Keywords: high-fidelity, fast, large scene, nerf, gaussian splatting, 3d gaussian, ar  
- **[Unposed 3DGS Reconstruction with Probabilistic Procrustes Mapping](https://arxiv.org/abs/2507.18541v1)**  
  Authors: Chong Cheng, Zijian Wang, Sicheng Yu, Yu Hu, Nanjie Yao, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.18541v1.pdf)  
  Keywords: ar, outdoor, geometry, gaussian splatting, 3d gaussian, mapping  
- **[MUVOD: A Novel Multi-view Video Object Segmentation Dataset and A
  Benchmark for 3D Segmentation](https://arxiv.org/abs/2507.07519v1)**  
  Authors: Bangning Wei, Joshua Maraval, Meriem Outtas, Kidiyo Kpalma, Nicolas Ramin, Lu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.07519v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://volumetric-repository.labs.b-com.com/#/muvod.)  
  Keywords: motion, ar, 4d, outdoor, segmentation, nerf, gaussian splatting, 3d gaussian, understanding, dynamic  

### Model Compression

*Showing the latest 50 out of 404 papers*

- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v1)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v1.pdf)  
  Keywords: lighting, compact, high-fidelity, survey, ar, segmentation, semantic, nerf, gaussian splatting, 3d gaussian, understanding  
- **[SkySplat: Generalizable 3D Gaussian Splatting from Multi-Temporal Sparse
  Satellite Images](https://arxiv.org/abs/2508.09479v1)**  
  Authors: Xuejun Huang, Xinyi Liu, Yi Wan, Zhi Zheng, Bin Zhang, Mingtao Xiong, Yingying Pei, Yongjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09479v1.pdf)  
  Keywords: efficient, gaussian splatting, 3d gaussian, ar, sparse-view  
- **[Gradient-Direction-Aware Density Control for 3D Gaussian Splatting](https://arxiv.org/abs/2508.09239v1)**  
  Authors: Zheng Zhou, Yu-Jie Xiong, Chun-Ming Xia, Jia-Chen Zhang, Hong-Jian Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09239v1.pdf)  
  Keywords: compact, head, gaussian splatting, 3d gaussian, ar, dynamic  
- **[Communication Efficient Robotic Mixed Reality with Gaussian Splatting
  Cross-Layer Optimization](https://arxiv.org/abs/2508.08624v1)**  
  Authors: Chenxuan Liu, He Li, Zongze Li, Shuai Wang, Wei Xu, Kejiang Ye, Derrick Wing Kwan Ng, Chengzhong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08624v1.pdf)  
  Keywords: gaussian splatting, ar, dynamic, efficient  
- **[SAGOnline: Segment Any Gaussians Online](https://arxiv.org/abs/2508.08219v1)**  
  Authors: Wentao Sun, Quanyun Wu, Hanqing Xu, Kyle Gao, Zhengsen Xu, Yiping Chen, Dedong Zhang, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08219v1.pdf)  
  Keywords: efficient, lightweight, vr, tracking, ar, real-time rendering, segmentation, nerf, gaussian splatting, 3d gaussian, understanding  
- **[GS4Buildings: Prior-Guided Gaussian Splatting for 3D Building
  Reconstruction](https://arxiv.org/abs/2508.07355v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07355v1.pdf)  
  Keywords: compact, motion, efficient, face, geometry, semantic, 3d reconstruction, gaussian splatting, urban scene, ar  
- **[3D Gaussian Representations with Motion Trajectory Field for Dynamic
  Scene Reconstruction](https://arxiv.org/abs/2508.07182v1)**  
  Authors: Xuesong Li, Lars Petersson, Vivien Rolland  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07182v1.pdf)  
  Keywords: compact, motion, efficient, nerf, gaussian splatting, 3d gaussian, ar, dynamic  
- **[3DGS-VBench: A Comprehensive Video Quality Evaluation Benchmark for 3DGS
  Compression](https://arxiv.org/abs/2508.07038v1)**  
  Authors: Yuke Xing, William Gordon, Qi Yang, Kaifa Yang, Jiarui Wang, Yiling Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07038v1.pdf)  
  Keywords: gaussian splatting, compression, 3d gaussian, ar  
- **[3DGabSplat: 3D Gabor Splatting for Frequency-adaptive Radiance Field
  Rendering](https://arxiv.org/abs/2508.05343v1)**  
  Authors: Junyu Zhou, Yuyang Huang, Wenrui Dai, Junni Zou, Ziyang Zheng, Nuowen Kan, Chenglin Li, Hongkai Xiong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05343v1.pdf)  
  Keywords: high-fidelity, efficient, real-time rendering, head, gaussian splatting, 3d gaussian, ar  
- **[CF3: Compact and Fast 3D Feature Fields](https://arxiv.org/abs/2508.05254v2)**  
  Authors: Hyunjoon Lee, Joonkyu Min, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05254v2.pdf)  
  Keywords: compact, efficient, fast, gaussian splatting, 3d gaussian, ar  

### Quality Enhancement

*Showing the latest 50 out of 160 papers*

- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v1)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v1.pdf)  
  Keywords: lighting, compact, high-fidelity, survey, ar, segmentation, semantic, nerf, gaussian splatting, 3d gaussian, understanding  
- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event
  Cameras](https://arxiv.org/abs/2508.09912v1)**  
  Authors: Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09912v1.pdf)  
  Keywords: lighting, high-fidelity, motion, fast, 4d, gaussian splatting, ar, dynamic  
- **[EGS-SLAM: RGB-D Gaussian Splatting SLAM with Events](https://arxiv.org/abs/2508.07003v1)**  
  Authors: Siyu Chen, Shenghai Yuan, Thien-Minh Nguyen, Zhuyu Huang, Chenyang Shi, Jin Jing, Lihua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07003v1.pdf)  
  Keywords: high-fidelity, motion, slam, tracking, ar, 3d reconstruction, gaussian splatting, 3d gaussian, mapping, dynamic  
- **[GAP: Gaussianize Any Point Clouds with Text Guidance](https://arxiv.org/abs/2508.05631v1)**  
  Authors: Weiqi Zhang, Junsheng Zhou, Haotian Geng, Wenyuan Zhang, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05631v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weiqi-zhang.github.io/GAP.)  
  Keywords: high-fidelity, face, fast, gaussian splatting, 3d gaussian, ar  
- **[3DGabSplat: 3D Gabor Splatting for Frequency-adaptive Radiance Field
  Rendering](https://arxiv.org/abs/2508.05343v1)**  
  Authors: Junyu Zhou, Yuyang Huang, Wenrui Dai, Junni Zou, Ziyang Zheng, Nuowen Kan, Chenglin Li, Hongkai Xiong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05343v1.pdf)  
  Keywords: high-fidelity, efficient, real-time rendering, head, gaussian splatting, 3d gaussian, ar  
- **[DET-GS: Depth- and Edge-Aware Regularization for High-Fidelity 3D
  Gaussian Splatting](https://arxiv.org/abs/2508.04099v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04099v1.pdf)  
  Keywords: high-fidelity, efficient, semantic, gaussian splatting, 3d gaussian, ar, sparse-view  
- **[GENIE: Gaussian Encoding for Neural Radiance Fields Interactive Editing](https://arxiv.org/abs/2508.02831v1)**  
  Authors: Mikołaj Zieliński, Krzysztof Byrski, Tomasz Szczepanik, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.02831v1.pdf)  
  Keywords: high-fidelity, efficient, fast, real-time rendering, geometry, neural rendering, nerf, gaussian splatting, ar, dynamic  
- **[VDEGaussian: Video Diffusion Enhanced 4D Gaussian Splatting for Dynamic
  Urban Scenes Modeling](https://arxiv.org/abs/2508.02129v1)**  
  Authors: Yuru Xiao, Zihan Lin, Chao Lu, Deming Zhai, Kui Jiang, Wenbo Zhao, Wei Zhang, Junjun Jiang, Huanran Wang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.02129v1.pdf)  
  Keywords: high-fidelity, face, fast, 4d, gaussian splatting, urban scene, ar, dynamic  
- **[Gaussian Variation Field Diffusion for High-fidelity Video-to-4D
  Synthesis](https://arxiv.org/abs/2507.23785v1)**  
  Authors: Bowen Zhang, Sicheng Xu, Chuxin Wang, Jiaolong Yang, Feng Zhao, Dong Chen, Baining Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23785v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gvfdiffusion.github.io/.)  
  Keywords: animation, high-fidelity, motion, compact, efficient, 4d, ar, dynamic  
- **[Enhanced Velocity Field Modeling for Gaussian Video Reconstruction](https://arxiv.org/abs/2507.23704v1)**  
  Authors: Zhenyang Li, Xiaoyang Bai, Tongchen Zhang, Pengfei Shen, Weiwei Xu, Yifan Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23704v1.pdf)  
  Keywords: high-fidelity, motion, vr, real-time rendering, deformation, gaussian splatting, 3d gaussian, ar, dynamic  

### Ray Tracing

- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: lighting, face, relightable, relighting, illumination, shadow, outdoor, global illumination, gaussian splatting, 3d gaussian, ar, dynamic  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: lighting, face, path tracing, gaussian splatting, 3d gaussian, ar, dynamic  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: lighting, face, efficient, efficient rendering, relightable, relighting, ray marching, geometry, gaussian splatting, 3d gaussian, ar  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: high-fidelity, efficient, real-time rendering, ray tracing, gaussian splatting, ar  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar
  Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: lighting, human, relightable, relighting, fast, shadow, avatar, ray tracing, geometry, gaussian splatting, ar  
- **[Stochastic Ray Tracing of Transparent 3D Gaussians](https://arxiv.org/abs/2504.06598v3)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v3.pdf)  
  Keywords: lighting, efficient, efficient rendering, relighting, acceleration, ray tracing, gaussian splatting, 3d gaussian, ar  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for
  Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: animation, compact, efficient, acceleration, ray marching, gaussian splatting, 3d gaussian, ar, dynamic  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: lighting, face, efficient, illumination, real-time rendering, ray tracing, global illumination, gaussian splatting, 3d gaussian, ar  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: fast, reflection, shadow, ray tracing, neural rendering, gaussian splatting, 3d gaussian, ar  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: lighting, face, reflection, shadow, ray tracing, gaussian splatting  

### Relighting

*Showing the latest 50 out of 112 papers*

- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v1)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v1.pdf)  
  Keywords: lighting, compact, high-fidelity, survey, ar, segmentation, semantic, nerf, gaussian splatting, 3d gaussian, understanding  
- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event
  Cameras](https://arxiv.org/abs/2508.09912v1)**  
  Authors: Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09912v1.pdf)  
  Keywords: lighting, high-fidelity, motion, fast, 4d, gaussian splatting, ar, dynamic  
- **[HumanGenesis: Agent-Based Geometric and Generative Modeling for
  Synthetic Human Dynamics](https://arxiv.org/abs/2508.09858v1)**  
  Authors: Weiqi Li, Zehao Zhang, Liang Lin, Guangrun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09858v1.pdf)  
  Keywords: motion, human, face, reflection, 4d, deformation, gaussian splatting, 3d gaussian, ar, dynamic  
- **[Touch-Augmented Gaussian Splatting for Enhanced 3D Scene Reconstruction](https://arxiv.org/abs/2508.07717v1)**  
  Authors: Yuchen Gao, Xiao Xu, Eckehard Steinbach, Daniel E. Lucani, Qi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07717v1.pdf)  
  Keywords: lighting, face, geometry, gaussian splatting, 3d gaussian, ar  
- **[UW-3DGS: Underwater 3D Reconstruction with Physics-Aware Gaussian
  Splatting](https://arxiv.org/abs/2508.06169v1)**  
  Authors: Wenpeng Xing, Jie Chen, Zaifeng Yang, Changting Lin, Jianfeng Dong, Chaochao Chen, Xun Zhou, Meng Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.06169v1.pdf)  
  Keywords: face, light transport, geometry, 3d reconstruction, nerf, gaussian splatting, 3d gaussian, ar  
- **[A 3DGS-Diffusion Self-Supervised Framework for Normal Estimation from a
  Single Image](https://arxiv.org/abs/2508.05950v1)**  
  Authors: Yanxing Liang, Yinghui Wang, Jinlong Yang, Wei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05950v1.pdf)  
  Keywords: face, light transport, ar, gaussian splatting, 3d gaussian, mapping  
- **[OCSplats: Observation Completeness Quantification and Label Noise
  Separation in 3DGS](https://arxiv.org/abs/2508.01239v1)**  
  Authors: Han Ling, Xian Xu, Yinghui Sun, Quansen Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.01239v1.pdf)  
  Keywords: face, shadow, 3d reconstruction, gaussian splatting, 3d gaussian, ar, dynamic  
- **[I2V-GS: Infrastructure-to-Vehicle View Transformation with Gaussian
  Splatting for Autonomous Driving Data Generation](https://arxiv.org/abs/2507.23683v1)**  
  Authors: Jialei Chen, Wuhao Xu, Sipeng He, Baoru Huang, Dongchun Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23683v1.pdf)  
  Keywords: lighting, efficient, autonomous driving, 3d reconstruction, gaussian splatting, ar  
- **[MagicRoad: Semantic-Aware 3D Road Surface Reconstruction via Obstacle
  Inpainting](https://arxiv.org/abs/2507.23340v1)**  
  Authors: Xingyue Peng, Yuandong Lyu, Lang Zhang, Jian Zhu, Songtao Wang, Jiaxin Deng, Songxin Lu, Weiliang Ma, Dangen She, Peng Jia, XianPeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23340v1.pdf)  
  Keywords: lighting, face, efficient, ar, segmentation, semantic, autonomous driving, gaussian splatting, 3d gaussian, mapping, dynamic  
- **[GSFusion:Globally Optimized LiDAR-Inertial-Visual Mapping for Gaussian
  Splatting](https://arxiv.org/abs/2507.23273v1)**  
  Authors: Jaeseok Park, Chanoh Park, Minsu Kim, Soohwan Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23273v1.pdf)  
  Keywords: efficient, slam, illumination, ar, gaussian splatting, 3d gaussian, mapping  

### SLAM

*Showing the latest 50 out of 154 papers*

- **[SAGOnline: Segment Any Gaussians Online](https://arxiv.org/abs/2508.08219v1)**  
  Authors: Wentao Sun, Quanyun Wu, Hanqing Xu, Kyle Gao, Zhengsen Xu, Yiping Chen, Dedong Zhang, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08219v1.pdf)  
  Keywords: efficient, lightweight, vr, tracking, ar, real-time rendering, segmentation, nerf, gaussian splatting, 3d gaussian, understanding  
- **[NeeCo: Image Synthesis of Novel Instrument States Based on Dynamic and
  Deformable 3D Gaussian Reconstruction](https://arxiv.org/abs/2508.07897v1)**  
  Authors: Tianle Zeng, Junlei Hu, Gerardo Loza Galindo, Sharib Ali, Duygu Sarikaya, Pietro Valdastri, Dominic Jones  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07897v1.pdf)  
  Keywords: motion, medical, tracking, deformation, localization, gaussian splatting, 3d gaussian, ar, dynamic  
- **[EGS-SLAM: RGB-D Gaussian Splatting SLAM with Events](https://arxiv.org/abs/2508.07003v1)**  
  Authors: Siyu Chen, Shenghai Yuan, Thien-Minh Nguyen, Zhuyu Huang, Chenyang Shi, Jin Jing, Lihua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07003v1.pdf)  
  Keywords: high-fidelity, motion, slam, tracking, ar, 3d reconstruction, gaussian splatting, 3d gaussian, mapping, dynamic  
- **[A 3DGS-Diffusion Self-Supervised Framework for Normal Estimation from a
  Single Image](https://arxiv.org/abs/2508.05950v1)**  
  Authors: Yanxing Liang, Yinghui Wang, Jinlong Yang, Wei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05950v1.pdf)  
  Keywords: face, light transport, ar, gaussian splatting, 3d gaussian, mapping  
- **[Stereo 3D Gaussian Splatting SLAM for Outdoor Urban Scenes](https://arxiv.org/abs/2507.23677v1)**  
  Authors: Xiaohan Li, Ziren Gong, Fabio Tosi, Matteo Poggi, Stefano Mattoccia, Dong Liu, Jun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23677v1.pdf)  
  Keywords: high-fidelity, slam, fast, tracking, ar, outdoor, gaussian splatting, urban scene, 3d gaussian, mapping  
- **[Gaussian Splatting Feature Fields for Privacy-Preserving Visual
  Localization](https://arxiv.org/abs/2507.23569v1)**  
  Authors: Maxime Pietrantoni, Gabriela Csurka, Torsten Sattler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23569v1.pdf)  
  Keywords: localization, segmentation, geometry, gaussian splatting, 3d gaussian, ar  
- **[MagicRoad: Semantic-Aware 3D Road Surface Reconstruction via Obstacle
  Inpainting](https://arxiv.org/abs/2507.23340v1)**  
  Authors: Xingyue Peng, Yuandong Lyu, Lang Zhang, Jian Zhu, Songtao Wang, Jiaxin Deng, Songxin Lu, Weiliang Ma, Dangen She, Peng Jia, XianPeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23340v1.pdf)  
  Keywords: lighting, face, efficient, ar, segmentation, semantic, autonomous driving, gaussian splatting, 3d gaussian, mapping, dynamic  
- **[GSFusion:Globally Optimized LiDAR-Inertial-Visual Mapping for Gaussian
  Splatting](https://arxiv.org/abs/2507.23273v1)**  
  Authors: Jaeseok Park, Chanoh Park, Minsu Kim, Soohwan Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.23273v1.pdf)  
  Keywords: efficient, slam, illumination, ar, gaussian splatting, 3d gaussian, mapping  
- **[No Redundancy, No Stall: Lightweight Streaming 3D Gaussian Splatting for
  Real-time Rendering](https://arxiv.org/abs/2507.21572v2)**  
  Authors: Linye Wei, Jiajun Tang, Fan Fei, Boxin Shi, Runsheng Wang, Meng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.21572v2.pdf)  
  Keywords: face, efficient, lightweight, ar, real-time rendering, autonomous driving, gaussian splatting, 3d gaussian, mapping  
- **[RaGS: Unleashing 3D Gaussian Splatting from 4D Radar and Monocular Cues
  for 3D Object Detection](https://arxiv.org/abs/2507.19856v2)**  
  Authors: Xiaokai Bai, Chenxu Zhou, Lianqing Zheng, Si-Yuan Cao, Jianan Liu, Xiaohan Zhang, Zhengzhuang Zhang, Hui-liang Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19856v2.pdf)  
  Keywords: efficient, ar, 4d, localization, autonomous driving, geometry, semantic, gaussian splatting, 3d gaussian, understanding, dynamic  

### Scene Understanding

*Showing the latest 50 out of 193 papers*

- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v1)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v1.pdf)  
  Keywords: lighting, compact, high-fidelity, survey, ar, segmentation, semantic, nerf, gaussian splatting, 3d gaussian, understanding  
- **[GSFixer: Improving 3D Gaussian Splatting with Reference-Guided Video
  Diffusion Priors](https://arxiv.org/abs/2508.09667v1)**  
  Authors: Xingyilang Yin, Qi Zhang, Jiahao Chang, Ying Feng, Qingnan Fan, Xi Yang, Chi-Man Pun, Huaqi Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09667v1.pdf)  
  Keywords: geometry, semantic, 3d reconstruction, gaussian splatting, 3d gaussian, ar, sparse view, sparse-view  
- **[ReferSplat: Referring Segmentation in 3D Gaussian Splatting](https://arxiv.org/abs/2508.08252v1)**  
  Authors: Shuting He, Guangquan Jie, Changshuo Wang, Yun Zhou, Shuming Hu, Guanbin Li, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08252v1.pdf)  
  Keywords: ar, segmentation, gaussian splatting, 3d gaussian, understanding  
- **[SAGOnline: Segment Any Gaussians Online](https://arxiv.org/abs/2508.08219v1)**  
  Authors: Wentao Sun, Quanyun Wu, Hanqing Xu, Kyle Gao, Zhengsen Xu, Yiping Chen, Dedong Zhang, Lingfei Ma, John S. Zelek, Jonathan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.08219v1.pdf)  
  Keywords: efficient, lightweight, vr, tracking, ar, real-time rendering, segmentation, nerf, gaussian splatting, 3d gaussian, understanding  
- **[GS4Buildings: Prior-Guided Gaussian Splatting for 3D Building
  Reconstruction](https://arxiv.org/abs/2508.07355v1)**  
  Authors: Qilin Zhang, Olaf Wysocki, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07355v1.pdf)  
  Keywords: compact, motion, efficient, face, geometry, semantic, 3d reconstruction, gaussian splatting, urban scene, ar  
- **[DexFruit: Dexterous Manipulation and Gaussian Splatting Inspection of
  Fruit](https://arxiv.org/abs/2508.07118v1)**  
  Authors: Aiden Swann, Alex Qiu, Matthew Strong, Angelina Zhang, Samuel Morstein, Kai Rayle, Monroe Kennedy III  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.07118v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dex-fruit.github.io)  
  Keywords: human, segmentation, gaussian splatting, 3d gaussian, ar  
- **[A Study of the Framework and Real-World Applications of Language
  Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v1.pdf)  
  Keywords: survey, efficient, ar, semantic, robotics, nerf, gaussian splatting, 3d gaussian, understanding  
- **[DET-GS: Depth- and Edge-Aware Regularization for High-Fidelity 3D
  Gaussian Splatting](https://arxiv.org/abs/2508.04099v1)**  
  Authors: Zexu Huang, Min Xu, Stuart Perry  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04099v1.pdf)  
  Keywords: high-fidelity, efficient, semantic, gaussian splatting, 3d gaussian, ar, sparse-view  
- **[Trace3D: Consistent Segmentation Lifting via Gaussian Instance Tracing](https://arxiv.org/abs/2508.03227v1)**  
  Authors: Hongyu Shen, Junfeng Ni, Yixin Chen, Weishuo Li, Mingtao Pei, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.03227v1.pdf)  
  Keywords: gaussian splatting, ar, segmentation, semantic  
- **[H3R: Hybrid Multi-view Correspondence for Generalizable 3D
  Reconstruction](https://arxiv.org/abs/2508.03118v1)**  
  Authors: Heng Jia, Linchao Zhu, Na Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.03118v1.pdf)  
  Keywords: face, efficient, fast, semantic, 3d reconstruction, gaussian splatting, 3d gaussian, ar  



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

## 📋 Project Features

### 🛠️ Core Features
- **Configurable Search System**: Customize search keywords through `data/search_config.json` for targeted paper collection
- **Automated Paper Collection**: Daily automatic crawling of latest Gaussian Splatting related papers
- **Intelligent Classification System**: Automatically categorize papers into different topics (Acceleration, Applications, Dynamic Scenes, etc.)
- **Flexible Search Scopes**: Support for abstract-only, title-only, or combined searches
- **Cross-Platform Compatibility**: Support for Windows/Linux/macOS with automatic environment detection

### 🛠️ Technical Features
- **Robust Error Handling**: Multi-layer retry and fallback strategies ensure stable operation
- **GitHub Actions Integration**: Automated CI/CD workflows
- **Real-time Update Mechanism**: Daily automatic paper data updates
- **Detailed Logging**: Comprehensive logging for debugging and monitoring

### 📚 Documentation System
- **User Guides**: Detailed configuration and usage instructions
- **Update Logs**: [News.md](News.md) - Records all important updates
- **Validation Reports**: Automated testing and validation results

## 🚀 Quick Start

### Customize Search Keywords
Edit `data/search_config.json` to target specific research areas:

```json
{
  "search_config": {
    "both_abstract_and_title": [
      "gaussian splatting",
      "3d gaussian",
      "neural rendering"
    ],
    "abstract_only": [
      "volumetric rendering",
      "point cloud reconstruction"
    ],
    "title_only": [
      "real-time rendering",
      "3D reconstruction"
    ]
  }
}
```

### Run the Crawler
```bash
# Basic usage
python scripts/arxiv_crawler.py

# Custom number of papers
python scripts/arxiv_crawler.py --max-results 200

# Validate configuration
python scripts/validate_search_config.py
```

## Contribution Guidelines
Feel free to submit Pull Requests to improve this list! Please follow these formats:
- Paper entry format: `**[Paper Title](link)** - Brief description`
- Project entry format: `[Project Name](link) - Project description`

## License
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) 